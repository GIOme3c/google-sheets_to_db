
export function Total({orders}) {
    let totalSum = 0
    orders.forEach(element => {
        totalSum += element.price_rub
    });
    return (
        <div className="total">
            <div className="total-title">
                Total
            </div>
            <div className="total-sum">
                {totalSum.toFixed(2)}
            </div>
        </div>
    )
}