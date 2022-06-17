import time
from adhoccomputing.Experimentation.Topology import Topology
from adhoccomputing.Networking.LogicalChannels.GenericChannel import GenericChannel
from node_model.generic_node import GenericNode

from adhoccomputing.Networking.MacProtocol.GenericMAC

def main():
  number_of_nodes = 4
  topo = Topology()
  topo.construct_winslab_topology_with_channels(number_of_nodes, GenericNode, GenericChannel)
  topo.start()

  """
  shortest_paths = topo.allpairs_shortest_path()
  for sp in shortest_paths:
    print(shortest_paths[sp])
    print('------------------------')
  """

  for i in range(5):
    topo.nodes[0].send_message(1, "0#1")
    topo.nodes[0].send_message(2, "0#2")
    topo.nodes[0].send_message(3, "0#1")
    topo.nodes[1].send_message(0, "1#0")
    topo.nodes[1].send_message(2, "1#2")
    topo.nodes[1].send_message(3, "1#3")
    topo.nodes[2].send_message(0, "2#0")
    topo.nodes[2].send_message(1, "2#1")
    topo.nodes[2].send_message(3, "2#3")
    topo.nodes[3].send_message(0, "3#0")
    topo.nodes[3].send_message(1, "3#1")
    topo.nodes[3].send_message(2, "3#2")
    time.sleep(0.25)

  

  
  print("######################################")
  for node in topo.nodes.values():
    print(node.application.identifier, ' stats')
    print("**************************************")
    print("received packets: ",node.application.received_packets)
    print("sent     ack    : ",node.application.sent_ack)
    print("--------------------------------------")
    print("sent     packets: ",node.application.sent_packets)
    print("received ack    : ",node.application.received_ack)
    print("######################################")
  
  """  
  for i in range(number_of_nodes):
  neighbours = topo.get_neighbors(1)
  print(neighbours)
  """

if __name__ == '__main__':
  main()
