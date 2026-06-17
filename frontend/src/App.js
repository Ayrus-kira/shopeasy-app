import React, { useState } from "react";

const products = [
  { id: 1, name: "Laptop", price: 50000, stock: 10, icon: "💻" },
  { id: 2, name: "Phone", price: 25000, stock: 20, icon: "📱" },
  { id: 3, name: "Headphones", price: 2000, stock: 30, icon: "🎧" }
];

export default function App() {
  const [page, setPage] = useState("products");
  const [cart, setCart] = useState([]);
  const [orders, setOrders] = useState([]);

  const total = cart.reduce((sum, item) => sum + item.price, 0);

  const addToCart = (product) => {
    setCart([...cart, product]);
  };

  const payNow = () => {
    const order = {
      id: Date.now(),
      items: cart,
      total,
      status: "Paid",
      date: new Date().toLocaleString()
    };
    setOrders([order, ...orders]);
    setCart([]);
    setPage("orders");
  };

  return (
    <div style={styles.app}>
      <nav style={styles.nav}>
        <h2>🛒 ShopEasy</h2>
        <div>
          <button style={styles.navBtn} onClick={() => setPage("products")}>Products</button>
          <button style={styles.navBtn} onClick={() => setPage("cart")}>Cart ({cart.length})</button>
          <button style={styles.navBtn} onClick={() => setPage("orders")}>Orders</button>
        </div>
      </nav>

      {page === "products" && (
        <div style={styles.page}>
          <h2>🛍️ Products</h2>
          <div style={styles.grid}>
            {products.map((p) => (
              <div style={styles.card} key={p.id}>
                <div style={styles.icon}>{p.icon}</div>
                <h3>{p.name}</h3>
                <h2 style={styles.price}>₹{p.price.toLocaleString()}</h2>
                <p>Stock: {p.stock}</p>
                <button style={styles.btn} onClick={() => addToCart(p)}>
                  Add to Cart
                </button>
              </div>
            ))}
          </div>
        </div>
      )}

      {page === "cart" && (
        <div style={styles.page}>
          <h2>🛒 Your Cart</h2>
          {cart.length === 0 ? (
            <div style={styles.card}>
              <h3>Your cart is empty</h3>
              <button style={styles.btn} onClick={() => setPage("products")}>Shop Now</button>
            </div>
          ) : (
            <div style={styles.box}>
              {cart.map((item, i) => (
                <div style={styles.row} key={i}>
                  <span>{item.name}</span>
                  <b>₹{item.price.toLocaleString()}</b>
                </div>
              ))}
              <h2>Total: ₹{total.toLocaleString()}</h2>
              <button style={styles.clearBtn} onClick={() => setCart([])}>Clear Cart</button>
              <button style={styles.payBtn} onClick={() => setPage("payment")}>Checkout</button>
            </div>
          )}
        </div>
      )}

      {page === "payment" && (
        <div style={styles.page}>
          <h2>💳 Payment</h2>
          <div style={styles.box}>
            <h3>Order Summary</h3>
            {cart.map((item, i) => (
              <div style={styles.row} key={i}>
                <span>{item.name}</span>
                <b>₹{item.price.toLocaleString()}</b>
              </div>
            ))}
            <h2>Total: ₹{total.toLocaleString()}</h2>
            <button style={styles.payBtn} onClick={payNow}>Pay Now</button>
          </div>
        </div>
      )}

      {page === "orders" && (
        <div style={styles.page}>
          <h2>📦 Orders</h2>
          {orders.length === 0 ? (
            <div style={styles.card}>No orders yet</div>
          ) : (
            orders.map((order) => (
              <div style={styles.box} key={order.id}>
                <h3>Order #{order.id}</h3>
                <p>Status: ✅ {order.status}</p>
                <p>Date: {order.date}</p>
                {order.items.map((item, i) => (
                  <div style={styles.row} key={i}>
                    <span>{item.name}</span>
                    <b>₹{item.price.toLocaleString()}</b>
                  </div>
                ))}
                <h2>Total: ₹{order.total.toLocaleString()}</h2>
              </div>
            ))
          )}
        </div>
      )}
    </div>
  );
}

const styles = {
  app: { minHeight: "100vh", background: "#f5f5f5", fontFamily: "Arial" },
  nav: { background: "#1a1a2e", color: "white", padding: "20px", display: "flex", justifyContent: "space-between" },
  navBtn: { margin: "5px", padding: "10px", cursor: "pointer" },
  page: { padding: "30px" },
  grid: { display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))", gap: "20px" },
  card: { background: "white", padding: "25px", borderRadius: "12px", textAlign: "center", boxShadow: "0 2px 10px #ccc" },
  box: { background: "white", padding: "25px", borderRadius: "12px", maxWidth: "600px", boxShadow: "0 2px 10px #ccc" },
  icon: { fontSize: "50px" },
  price: { color: "#e94560" },
  btn: { background: "#1a1a2e", color: "white", border: "none", padding: "12px", borderRadius: "8px", cursor: "pointer" },
  payBtn: { background: "#e94560", color: "white", border: "none", padding: "12px", borderRadius: "8px", cursor: "pointer", margin: "5px" },
  clearBtn: { background: "white", color: "#e94560", border: "2px solid #e94560", padding: "12px", borderRadius: "8px", cursor: "pointer", margin: "5px" },
  row: { display: "flex", justifyContent: "space-between", padding: "12px", borderBottom: "1px solid #eee" }
};
