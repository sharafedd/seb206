"use client";

import { useEffect, useRef } from "react";
import ForceGraph from "force-graph";

// Types for graph data
interface GraphNode {
  id: string;
  label: string;
}

interface GraphLink {
  source: string;
  target: string;
  goldstein: number;
}

interface GraphData {
  nodes: GraphNode[];
  edges: GraphLink[];
}

// Minimal typed wrapper for the ForceGraph API
interface ForceGraphAPI {
  graphData(data: { nodes: GraphNode[]; links: GraphLink[] }): ForceGraphAPI;
  nodeLabel(fn: (node: GraphNode) => string): ForceGraphAPI;
  nodeAutoColorBy(key: keyof GraphNode): ForceGraphAPI;
  linkColor(fn: (link: GraphLink) => string): ForceGraphAPI;
  linkWidth(fn: (link: GraphLink) => number): ForceGraphAPI;
}

type ForceGraphFactory = (element?: HTMLElement) => ForceGraphAPI;

export default function CountryGraph() {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const element = containerRef.current;
    if (!element) {
      return;
    }

    const FG = ForceGraph as unknown as ForceGraphFactory;

    fetch("/data/graph.json")
      .then((res) => res.json())
      .then((data: GraphData) => {
        const graph = FG(element);

        graph
          .graphData({
            nodes: data.nodes,
            links: data.edges,
          })
          .nodeLabel((node) => node.label)
          .nodeAutoColorBy("id")
          .linkColor((link) =>
            link.goldstein > 0 ? "green" : "red"
          )
          .linkWidth((link) =>
            Math.max(1, Math.abs(link.goldstein) * 0.5)
          );
      });
  }, []);

  return (
    <div
      ref={containerRef}
      style={{ width: "100%", height: "600px" }}
    />
  );
}
