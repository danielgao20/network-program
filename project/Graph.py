import networkx as nx
import plotly.graph_objs as go


class Graph:

    def __init__(self, programmer_name, node_list, tooltip_list, connections):
        self.programmer_name = programmer_name
        self.node_list = node_list
        self.tooltip_list = tooltip_list
        self.from_list = []
        self.to_list = []

        for i in range(len(node_list)):
            for j in range(len(connections[i])):
                self.from_list.append(i)
                self.to_list.append(connections[i][j])

    def draw_graph(self):
        G = nx.Graph()
        for i in range(len(self.node_list)):
            G.add_node(self.node_list[i])
        for i in range(len(self.from_list)):
            G.add_edges_from([(self.from_list[i], self.to_list[i])])

        pos = nx.spring_layout(G, k=0.5, iterations=100)
        for n, p in pos.items():
            G.nodes[n]['pos'] = p

        edge_trace = go.Scatter(
            x=[],
            y=[],
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines')
        for edge in G.edges():
            x0, y0 = G.nodes[edge[0]]['pos']
            x1, y1 = G.nodes[edge[1]]['pos']
            edge_trace['x'] += tuple([x0, x1, None])
            edge_trace['y'] += tuple([y0, y1, None])

        node_trace = go.Scatter(
            x=[],
            y=[],
            hovertemplate=[],
            text=[],
            mode='markers+text',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                colorscale='pinkyl',
                reversescale=True,
                color=[],
                size=37,
                colorbar=dict(
                    thickness=1,
                    title='Node Connections',
                    xanchor='left',
                    titleside='right'
                ),
                line=dict(width=0)))
        for node in G.nodes():
            x, y = G.nodes[node]['pos']
            node_trace['x'] += tuple([x])
            node_trace['y'] += tuple([y])

        for node, adjacencies in enumerate(G.adjacency()):
            node_trace['marker']['color'] += tuple([len(adjacencies[1])])
            node_info = adjacencies[0]
            node_trace['text'] += tuple([node_info])
            node_trace['hovertemplate'] += tuple([f"{self.tooltip_list[node]}"])

        title = "Network Graph Demonstration"
        fig = go.Figure(data=[edge_trace, node_trace],
                        layout=go.Layout(
                        title=title,
                        titlefont=dict(size=16),
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=21, l=5, r=5, t=40),
                        annotations=[dict(
                            text="By " + self.programmer_name,
                            showarrow=False,
                            xref="paper", yref="paper")],
                        xaxis=dict(showgrid=False, zeroline=False,
                                   showticklabels=False, mirror=True),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, mirror=True)))

        fig.show()
