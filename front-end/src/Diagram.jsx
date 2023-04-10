import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);


export function Diagram({orders}) {

  const labels = orders.map((order)=>order.delivery_date);

  const data = {
    labels,
    datasets: [
      {
        label: 'Dataset 1',
        data: orders.map((order)=>order.price_rub),
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        display: false,
      },
    },
  };


  return <Line options={options} data={data} className="diagram"/>;
}
