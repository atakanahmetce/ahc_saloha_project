from enum import Enum
from adhoccomputing.GenericModel import GenericModel
from adhoccomputing.Generics import Event, EventTypes, GenericMessage, GenericMessageHeader

# define your own message types
class SAlohaAppLayerMessageTypes(Enum):
  DATA = "DATA"
  ACK = "ACK"

# define your own message header structure
class SAlohaAppLayerMessageHeader(GenericMessageHeader):
  pass

class SAlohaAppLayerEventTypes(Enum):
  SENDDATA = "send_data"
  SENDACK = "send_ack"

class SAlohaAppLayer(GenericModel):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    # implementing layer events.
    self.eventhandlers[SAlohaAppLayerEventTypes.SENDDATA] = self.send_data
    self.eventhandlers[SAlohaAppLayerEventTypes.SENDACK] = self.send_ack

    # assign an identifier to node
    self.identifier = 'node#' + str(self.componentinstancenumber)
    self.node_id = self.componentinstancenumber

    # variables for keeping track of stats.
    self.received_packets = {}
    self.received_ack = {}
    self.sent_packets = {}
    self.sent_ack = {}
    print(self.identifier, " constructed on init")

  def on_message_from_bottom(self, eventobj: Event):
    
    # parse the incoming packet
    source      = eventobj.eventcontent.header.messagefrom
    destination = eventobj.eventcontent.header.messageto
    msg_type    = eventobj.eventcontent.header.messagetype
    payload     = eventobj.eventcontent.payload

    if destination != self.node_id:
      #print("destination != self.node_id\n")
      return

    #print('new packet source and dest: ', source, " # ",destination,  " # payload: ",payload)

    if msg_type == SAlohaAppLayerMessageTypes.ACK:
      # increase number of received ack from spesific node
      if source in self.received_ack:
        self.received_ack[source] += 1
      else:
        self.received_ack[source] = 1
      return

    if msg_type == SAlohaAppLayerMessageTypes.DATA:
      ack_header = SAlohaAppLayerMessageHeader(SAlohaAppLayerMessageTypes.ACK, self.node_id, source)
      #ack_msg = GenericMessage(ack_header, f"{self.node_id} acknowledges!")
      ack_msg = GenericMessage(ack_header, "ok       ")
      self.send_self(Event(self, SAlohaAppLayerEventTypes.SENDACK, ack_msg))

      print(payload)

      # increase number of received packets from spesific node
      if source in self.received_packets:
        self.received_packets[source] += 1
      else:
        self.received_packets[source] = 1
      return

  def send_data(self, eventobj: Event):
    source = eventobj.eventcontent.header.messagefrom
    destination = eventobj.eventcontent.header.messageto
    payload = eventobj.eventcontent.payload
    #print('sending payload: ', payload, ' # source and dest: ', source, '#', destination)

    data_header = SAlohaAppLayerMessageHeader(SAlohaAppLayerMessageTypes.DATA, source, destination)
    data_payload = GenericMessage(data_header, payload)
    self.send_down(Event(self, EventTypes.MFRT, data_payload))
    #self.sent_packets += 1
    # increase number of sent packets to spesific node
    if destination in self.sent_packets:
      self.sent_packets[destination] += 1
    else:
      self.sent_packets[destination] = 1
    return

  def send_ack(self, eventobj: Event):
    destination = eventobj.eventcontent.header.messageto

    payload = eventobj.eventcontent.payload
    source = eventobj.eventcontent.header.messagefrom
    #print('sending ack: ', payload, ' # source and dest: ', source, '#', destination)
    self.send_down(Event(self, EventTypes.MFRT, eventobj.eventcontent))
    if destination in self.sent_ack:
      self.sent_ack[destination] += 1
    else:
      self.sent_ack[destination] = 1
    return