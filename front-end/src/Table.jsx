

export function Table({orders}) {
    const tabContentJSX = orders.map((element)=>
        <tr key={element.order_id}>
            <td>{element.number}</td>
            <td>{element.order_id}</td>
            <td>{element.price_usd.toFixed(2)}</td>
            <td>{element.price_rub.toFixed(2)}</td>
            <td>{element.delivery_date.toString()}</td>
        </tr>
    )
    return (
        <div>
            <table className="orders-table">
                <thead>
                    <tr>
                        <th>№</th>
                        <th>заказ №</th>
                        <th>стоимость,$</th>
                        <th>стоимость,₽</th>
                        <th>срок поставки</th>
                    </tr>
                </thead>
                <tbody>
                    {tabContentJSX}
                </tbody>
            </table>
        </div>
    )
}