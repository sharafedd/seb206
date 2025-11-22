"use client";

import {
  Chart as ChartJS,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale
} from "chart.js";
import { Line } from "react-chartjs-2";

ChartJS.register(LineElement, PointElement, CategoryScale, LinearScale);

export default function GoldsteinChart({ history }: { history: number[] }) {
  return (
    <div className="mt-4">
      <Line
        data={{
          labels: history.map((_, i) => `Week ${i + 1}`),
          datasets: [
            {
              label: "Goldstein Score",
              data: history,
              borderWidth: 2,
              tension: 0.3
            }
          ]
        }}
        options={{
          scales: {
            y: { beginAtZero: false }
          }
        }}
      />
    </div>
  );
}
