import time

from adhoccomputing.Experimentation.Topology import Topology
from adhoccomputing.Networking.LogicalChannels.GenericChannel import GenericChannel

from node_model.usrp_node import UsrpNode


def main():
    number_of_nodes = 4
    topo = Topology()
    topo.construct_winslab_topology_with_channels(
        number_of_nodes, UsrpNode, GenericChannel
    )
    topo.start()
    # tmp_neighbours = topo.get_neighbors(0)
    # print(tmp_neighbours)
    # print(topo.allpairs_shortest_path)

    for i in range(20):
        for node in range(number_of_nodes):
            tmp_neighbours = topo.get_neighbors(node)
            for neighbour in tmp_neighbours:
                seconds = round(time.time() * 100)
                slot = seconds % 100
                if slot < 15 and node == 0:
                    topo.nodes[node].send_message(neighbour, "x" * 128)
                elif slot < 40 and node == 1:
                    topo.nodes[node].send_message(neighbour, "x" * 128)
                elif slot < 65 and node == 2:
                    topo.nodes[node].send_message(neighbour, "x" * 128)
                elif slot < 90 and node == 3:
                    topo.nodes[node].send_message(neighbour, "x" * 128)
                time.sleep(0.25)

    time.sleep(10)
    print("######################################")
    for node in topo.nodes.values():
        print(node.application.identifier, " stats")
        print("**************************************")
        print("received packets: ", node.application.received_packets)
        print("sent     ack    : ", node.application.sent_ack)
        print("--------------------------------------")
        print("sent     packets: ", node.application.sent_packets)
        print("received ack    : ", node.application.received_ack)
        print("######################################")


if __name__ == "__main__":
    main()
