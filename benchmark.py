import time
from adhoccomputing.Experimentation.Topology import Topology
from adhoccomputing.Networking.LogicalChannels.GenericChannel import GenericChannel
from node_model.usrp_node import UsrpNode

def main():
  number_of_nodes = 4
  topo = Topology()
  topo.construct_winslab_topology_with_channels(number_of_nodes, UsrpNode, GenericChannel)
  topo.start()

  """
  shortest_paths = topo.allpairs_shortest_path()
  for sp in shortest_paths:
    print(shortest_paths[sp])
    print('------------------------')
  """

  for i in range(3):
    payload = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque semper augue sed arcu euismod placerat. Ut lorem odio, vulputate eget nibh eget, finibus mollis orci. Morbi vulputate dictum eros eget varius. Aenean lobortis in odio nec posuere. Donec laoreet blandit massa, in condimentum turpis molestie eget. Phasellus quis dapibus nulla, et vehicula nisl. Nulla tincidunt ligula lacus, in tristique urna faucibus at. Vestibulum sit amet purus a ante congue venenatis. Curabitur vulputate leo a scelerisque venenatis.Pellentesque lobortis, nisi eget molestie porttitor, ligula dui tincidunt arcu, sed mattis diam libero ut risus. Fusce accumsan, ligula at facilisis sodales, sem dolor euismod mi, sed pulvinar nunc leo non diam. Quisque imperdiet quam tempus nunc semper venenatis. Maecenas bibendum sodales turpis sed vehicula. Sed placerat felis sit amet eros venenatis efficitur. Sed nec diam ut lorem ornare maximus. Quisque ut lacinia nisl. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;Ut quis pharetra lectus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Ut gravida tortor quis tempor sodales. Donec tincidunt pulvinar purus quis mattis. Nunc mattis, sapien vel imperdiet lacinia, dolor elit sodales sapien, vitae elementum dolor metus sit amet eros. Suspendisse vel odio tristique, efficitur quam ut, lobortis tortor. Phasellus mollis elementum nulla. Maecenas quis eros laoreet, condimentum augue sit amet, ornare nibh. Ut lobortis mi et elementum tempus. Donec ut metus id tortor sollicitudin sollicitudin. Mauris cursus pulvinar sem in vehicula. Morbi ut mattis ligula.Suspendisse eget erat consectetur, venenatis felis id, faucibus sem. Pellentesque convallis dui eget nulla lacinia, nec tempus diam rhoncus. Nullam convallis risus est, sed porta urna consectetur vel. Phasellus cursus risus in purus venenatis, vel aliquet nisl viverra. Quisque gravida non metus nec vehicula. Vivamus eu facilisis purus, a auctor odio. Donec dignissim suscipit lorem, vel commodo mauris finibus ac. Morbi eget malesuada dolor. Mauris varius pellentesque leo vel consectetur. Fusce id rutrum sapien. Nulla turpis ante, ultricies vitae diam id, laoreet euismod neque.Pellentesque vitae diam justo. Nunc sit amet justo felis. Morbi convallis purus ac nulla laoreet, in euismod lectus semper. Nam nec nibh vestibulum, elementum orci ut, finibus quam. In consectetur massa ex. Nunc laoreet dolor at diam fringilla, nec sagittis leo varius. Vestibulum lacinia, risus ut tristique euismod, neque justo scelerisque neque, eget dictum purus arcu vel quam. Cras ac odio vitae quam placerat euismod. Vestibulum nec lectus facilisis est pharetra efficitur. Etiam pellentesque tortor lectus, quis venenatis felis gravida a.Sed sagittis egestas accumsan. Curabitur posuere vehicula imperdiet. Sed lacinia, dolor at egestas placerat, nulla velit dignissim nibh, eget varius ipsum turpis in ex. Integer nisi ante, imperdiet viverra porttitor vel, dictum eu massa. Phasellus ac tellus ac magna mollis accumsan mattis vel sapien. Fusce pretium rhoncus eros at pharetra. Donec eget nibh blandit, rutrum dolor non, cursus justo. Duis eu purus nec tellus placerat porttitor. Etiam pretium auctor ipsum sed sollicitudin. In hac habitasse platea dictumst. Vestibulum ornare vitae turpis eu porta. Morbi quis dolor nunc. Morbi vitae mi in nunc sodales molestie eu a nisl. Praesent lectus sem, ultrices id odio semper, scelerisque dignissim ex. Praesent at massa vel elit maximus dapibus sed varius magna.Morbi viverra consectetur risus. Cras non magna malesuada, semper lectus sed, sollicitudin sapien. Nullam ligula velit, rhoncus vel eros sed, laoreet laoreet augue. Maecenas eget bibendum enim. Pellentesque nec aliquam nisl. Etiam ut eros nec erat malesuada commodo non ut nisi. Sed laoreet quis augue id mattis. Mauris porttitor pharetra lacinia. Fusce eu rhoncus velit. Phasellus malesuada nisi ac tristique pellentesque. Etiam bibendum nunc ut tempor maximus. Sed sollicitudin ex a iaculis pharetra. Maecenas dolor metus amet."
    topo.nodes[0].send_message(1, payload)

    '''
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
    '''
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
