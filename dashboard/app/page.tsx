"use client";

import { useEffect, useState } from "react";
import GoldsteinChart from "../components/GoldsteinChart";

type Dyad = {
  dyad: string;
  goldstein_history: number[];
  goldstein_pred: number;
  quadclass: number[];
};

export default function Home() {
  const [dyads, setDyads] = useState<Dyad[]>([]);

  useEffect(() => {
    fetch("/data/dyads.json")
      .then((res) => res.json())
      .then((data: Dyad[]) => setDyads(data));
  }, []);

  return (
    <main className="p-10">
      <h1 className="text-3xl font-bold mb-6">Echo Dashboard MVP</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {dyads.map((d) => (
          <div
            key={d.dyad}
            className="p-4 border rounded-lg shadow bg-white dark:bg-gray-900"
          >
            {/* Dyad Title */}
            <h2 className="text-xl font-semibold">{d.dyad}</h2>

            {/* Predicted Goldstein */}
            <p className="mt-2">
              <strong>Predicted Goldstein:</strong> {d.goldstein_pred}
            </p>

            {/* Goldstein History + Chart */}
            <h3 className="mt-3 font-semibold">Goldstein History</h3>
            <GoldsteinChart history={d.goldstein_history} />

            {/* QuadClass */}
            <h3 className="mt-3 font-semibold">QuadClass Distribution</h3>
            <ul className="text-sm text-gray-700 dark:text-gray-300">
              <li>Verbal Cooperation: {d.quadclass[0]}</li>
              <li>Material Cooperation: {d.quadclass[1]}</li>
              <li>Verbal Conflict: {d.quadclass[2]}</li>
              <li>Material Conflict: {d.quadclass[3]}</li>
            </ul>
          </div>
        ))}
      </div>
    </main>
  );
}
