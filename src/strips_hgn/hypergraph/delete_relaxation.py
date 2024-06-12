from typing import Dict, List

from strips_hgn.hypergraph import Hyperedge, Node
from strips_hgn.hypergraph.hypergraph_view import HypergraphView
from strips_hgn.planning import STRIPSProblem
import matplotlib.pyplot as plt
import networkx as nx


class DeleteRelaxationHypergraphView(HypergraphView):
    """
    Delete-Relaxation Hypergraph view of a STRIPS problem where:
      - A node corresponds with a single proposition
      - A hyperedge corresponds with a relaxed action, connecting the
        preconditions to the additive effects
    """

    def __init__(self, problem: STRIPSProblem):
        super().__init__(problem)

        # Each node corresponds to a single proposition
        self._nodes = self.problem.propositions
        self._node_to_idx: Dict[Node, int] = {
            node: idx for idx, node in enumerate(self.nodes)
        }

        # Each hyperedge corresponds to a relaxed action where the senders
        # are the preconditions and the receivers are the additive effects.
        # Hence, the negative effects are ignored.
        self._hyperedges = [
            Hyperedge(
                name=action.name,
                weight=action.cost,
                senders=action.preconditions,
                receivers=action.add_effects,
                # Used to store context of delete-effects for feature mappers
                context={"delete_effects": action.del_effects},
            )
            for action in self.problem.actions
        ]
        self._hyperedge_to_idx: Dict[Hyperedge, int] = {
            hyperedge: idx for idx, hyperedge in enumerate(self._hyperedges)
        }

        self.plot_delete_relaxation_hypergraph_view()

    @property
    def nodes(self) -> List[Node]:
        return self._nodes

    def node_to_idx(self, node: Node) -> int:
        return self._node_to_idx[node]

    @property
    def hyperedges(self) -> List[Hyperedge]:
        return self._hyperedges

    def hyperedge_to_idx(self, hyperedge: Hyperedge) -> int:
        return self._hyperedge_to_idx[hyperedge]

    def plot_delete_relaxation_hypergraph_view(self):
        G = nx.DiGraph()

        # Add nodes to the graph
        node_labels = {}
        for node in self._nodes:
            idx = self.node_to_idx(node)
            G.add_node(idx, label=str(node))
            node_labels[idx] = str(node)

        # Add hyperedges to the graph
        for hyperedge in self._hyperedges:
            for sender in hyperedge.senders:
                for receiver in hyperedge.receivers:
                    G.add_edge(self.node_to_idx(sender), self.node_to_idx(
                        receiver), label=hyperedge.name, weight=hyperedge.weight)

        pos = nx.kamada_kawai_layout(G)
        edge_labels = nx.get_edge_attributes(G, 'label')

        plt.figure(figsize=(20, 16))
        nx.draw(G, pos, labels=node_labels, with_labels=True, node_size=6000,
                node_color='lightblue', font_size=12, font_weight='bold', arrowsize=20)

        # Position edge labels with bbox to avoid overlap
        # edge_labels = edge_labels,
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10, bbox=dict(
            facecolor='white', edgecolor='none', alpha=1.0))

        plt.title('Delete-Relaxation Hypergraph View')

        # Save the image
        # 'bbox_inches' to ensure everything fits
        plt.savefig("graph.jpg", bbox_inches='tight')
        plt.close()
