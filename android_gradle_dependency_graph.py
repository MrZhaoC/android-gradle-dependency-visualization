import networkx as nx


class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []


def format_input_dependency_file(file_path='dependencies.txt'):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    result = [line.replace('+---', '#').replace('|    ', '#').replace('\\---', '#')
              .replace("     ", "#").replace("(*)", "").replace("(c)", "").strip()
              for line in lines]

    return result


def build_tree(data):
    root = TreeNode("root")
    current_nodes = [root]

    for line in data:
        depth = line.count("#")
        node_name = line.lstrip("#").strip()
        new_node = TreeNode(node_name)

        if depth == 0:
            root.children.append(new_node)
        else:
            while len(current_nodes) <= depth:
                current_nodes.append(None)

            parent = current_nodes[depth - 1]
            parent.children.append(new_node)
            current_nodes[depth] = new_node

    return root


def print_tree(node, indent=0):
    print("#" * indent + " " + node.name)

    for child in node.children:
        if child:
            print_tree(child, indent + 1)


dependency_graph = nx.DiGraph()
node_map = {}


def convert_dependency_tree_2_graph(root, indent=0):
    root_name = root.name

    if '->' in root_name:
        node_names = root_name.split('->')
        node_name1 = node_names[0].strip()
        root_name = node_names[1].strip()

        if ':' not in node_names[1]:
            gav = node_name1.split(":")
            ga = gav[0] + ":" + gav[1]
            root_name = ga + ":" + node_names[1].strip()

    for child in root.children:
        if child:
            child_name = child.name

            if '->' in child_name:
                child_names = child_name.split('->')
                child_name1 = child_names[0].strip()
                child_name = child_names[1].strip()

                if ':' not in child_names[1]:
                    c_gav = child_name1.split(":")
                    c_ga = c_gav[0] + ":" + c_gav[1]
                    child_name = c_ga + ":" + child_names[1].strip()

            value = f"{root.name}-->{child.name}"

            if node_map.get(child_name):
                value_list = node_map.get(child_name)
                value_list.append(value)
                node_map[child_name] = value_list
            else:
                node_map[child_name] = [value]

            if not dependency_graph.has_edge(root_name, child.name):
                dependency_graph.add_edge(root_name, child_name)

            convert_dependency_tree_2_graph(child, indent + 1)

    return dependency_graph


def print_format_dependency_tree(node, indent=0):
    print("#" * indent + " " + node.name)

    for child in node.children:
        if child:
            print(child.name)


def get_curr_parents(graph, target_node_name):
    curr_node_parents = []

    for node_name in graph.nodes():
        if target_node_name in graph.neighbors(node_name):
            curr_node_parents.append(node_name)

    return curr_node_parents


if __name__ == "__main__":
    tree_root = build_tree(format_input_dependency_file())
    dependency_g = convert_dependency_tree_2_graph(tree_root)

    target_gav = r'androidx.savedstate:savedstate:1.2.0'

    for dependency_chain in node_map.get(target_gav):
        print(dependency_chain)

    parents = get_curr_parents(dependency_g, target_gav)
    for parent in parents:
        print(parent)
