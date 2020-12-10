from anytree import Node, RenderTree
from anytree.exporter import DotExporter


# handy function
def find_node(root_node_top, searchable_name) -> Node:
    for pre, fill, node in RenderTree(root_node_top):
        if node.name == searchable_name:
            return node
    return None

numbers = [int(s) for s in open('input.txt').readlines()]
numbers.append(0)
numbers.sort()

print(numbers)

root_node = Node(0)
for i, x in enumerate(numbers):
    x_node = find_node(root_node, x)

    if x_node is None:  # node exists in the path
        # connect to x - 1
        x_minus1 = find_node(root_node, x-1)
        if x_minus1 is not None:
            Node(x, parent=x_minus1)

        # connect to x - 2
        x_minus2 = find_node(root_node, x-2)
        if x_minus2 is not None:
            Node(x, parent=x_minus2)

        # connect to x - 3
        x_minus3 = find_node(root_node, x-3)
        if x_minus3 is not None:
            Node(x, parent=x_minus3)


# print tree
for pre, fill, node in RenderTree(root_node):
    print("%s%s" % (pre, node.name))


# export as PNG
# with labels on the edges based on node attributes!
def create_edge_name(node, child):
    return 'label="%s:%s"' % (node.status, child.status)


DotExporter(root_node).to_picture("root.png")  # needs graphviz installed

