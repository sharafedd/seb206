"use client";

import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
  Legend,
  Tooltip,
} from "chart.js";

ChartJS.register(
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
  Legend,
  Tooltip
);

interface GoldsteinChartProps {
  history: number[];
}

export default function GoldsteinChart({ history }: GoldsteinChartProps) {
  const data = {
    labels: history.map((_, i) => `Week ${i + 1}`),
    datasets: [
      {
        label: "Goldstein Score",
        data: history,
        borderWidth: 2,
        tension: 0.3,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      y: {
        beginAtZero: false,
      },
    },
  };

  return (
    <div style={{ width: "100%", height: "220px" }}>
      <Line data={data} options={options} />
    </div>
  );
}
