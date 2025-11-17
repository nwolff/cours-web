import argparse
from xml.etree.ElementTree import XMLParser

import graphviz


class GraphvizBuilder:
    def __init__(self):
        self.node_number = 0
        self.parents = []

        g = graphviz.Graph(name="html.dot", directory="build")
        g.attr("node", shape="none")
        g.attr("edge", penwidth="0.4", color="blue")
        g.attr("graph", layout="dot")
        self.g = g

    def start(self, tag, _attrib):
        self.node_number += 1
        node_name = f"node_{self.node_number}"
        self.g.node(name=node_name, label=f"<{tag}> ")
        if self.parents:
            self.g.edge(self.parents[-1], node_name)
        self.parents.append(node_name)

    def end(self, _tag):
        self.parents.pop()

    def data(self, data):
        pass  # We do not need to do anything with data.

    def close(self):
        pass


def html_to_graphviz(path_to_html: str) -> graphviz.Graph:
    target = GraphvizBuilder()
    parser = XMLParser(target=target)
    with open(path_to_html) as f:
        contents = f.read()
        parser.feed(contents)
    parser.close()
    return target.g


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_html")

    args = parser.parse_args()

    graph = html_to_graphviz(args.input_html)
    graph.save()
