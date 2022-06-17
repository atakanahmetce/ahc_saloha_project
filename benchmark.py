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

    bytes = [8, 16, 32, 64, 128]
    # bytes = [8]
    measurements = []

    for node in range(number_of_nodes):
        tmp_neighbours = topo.get_neighbors(node)
        for neighbour in tmp_neighbours:
            for b in bytes:
                start = time.time()
                for i in range(20):
                    topo.nodes[node].send_message(neighbour, "x" * b)
                end = time.time()
                measurements.append(
                    {
                        "node": node,
                        "neighbour": neighbour,
                        "bytes_send": b,
                        "time": end - start,
                    }
                )
                """
                print(
                    node,
                    "#",
                    neighbour,
                    " ==> ",
                    b,
                    " bytes of 20 packets send in " + str(end - start) + " seconds!",
                )
                """
    time.sleep(3)
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
