import React, { useEffect, useState } from 'react';
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


export function Diagram() {

  const [orders, setOrders] = useState([])

  useEffect(() =>{
    fetch("http://127.0.0.1:5000/", {
      method: "GET",
    })
    .then(response => response.json())
    .then(data => {setOrders(data.orders); console.log(data.orders)})
    .catch(e => console.log(e));
  },[])

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
        position: 'top',
      },
      title: {
        display: true,
        text: 'Chart.js Line Chart',
      },
    },
  };


  return <Line options={options} data={data} />;
}
