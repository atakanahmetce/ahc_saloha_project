from adhoccomputing.GenericModel import GenericModel
from adhoccomputing.Generics import (
    ConnectorTypes,
    Event,
    EventTypes,
    GenericMessage,
    GenericMessageHeader,
)
from .app_layer import (
    SAlohaAppLayer,
    SAlohaAppLayerEventTypes,
    SAlohaAppLayerMessageTypes,
)


class GenericNode(GenericModel):
    def __init__(
        self,
        componentname,
        componentinstancenumber,
        context=None,
        configurationparameters=None,
        num_worker_threads=1,
        topology=None,
    ):
        super().__init__(
            componentname,
            componentinstancenumber,
            context,
            configurationparameters,
            num_worker_threads,
            topology,
        )
        self.application = SAlohaAppLayer("SAlohaAppLayer", componentinstancenumber)
        self.components.append(self.application)
        self.application.connect_me_to_component(ConnectorTypes.DOWN, self)
        self.connect_me_to_component(ConnectorTypes.UP, self.application)
        # self.incoming_packets = {}

    def on_init(self, eventobj: Event):
        pass

    def on_message_from_top(self, eventobj: Event):
        self.send_down(Event(self, EventTypes.MFRT, eventobj.eventcontent))
        # print("\nnew packet! => ", eventobj.eventcontent.payload, "\n")

    def on_message_from_bottom(self, eventobj: Event):
        self.send_up(Event(self, EventTypes.MFRB, eventobj.eventcontent))

    def send_message(self, dest_id, data):
        header = GenericMessageHeader(
            SAlohaAppLayerMessageTypes.DATA, self.componentinstancenumber, dest_id
        )
        message = GenericMessage(header, data)
        self.application.send_self(
            Event(self, SAlohaAppLayerEventTypes.SENDDATA, message)
        )
