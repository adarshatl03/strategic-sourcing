import Login from "./views/auth/Login";
import { Route, Routes, BrowserRouter } from "react-router-dom";
import Register from "./views/auth/Register";
import Dashboard from "./views/auth/Dashboard";
import Logout from "./views/auth/Logout";
import ForgotPassword from "./views/auth/ForgotPassword";
import CreatePassword from "./views/auth/CreatePassword";
import StoreHeader from "./views/base/StoreHeader";
import StoreFooter from "./views/base/StoreFooter";
import Products from "./views/store/Products";
import ProductDetails from "./views/store/ProductDetails";
function App() {
  return (
    <BrowserRouter>
      <StoreHeader />
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/forgot-password" element={<ForgotPassword />} />
        <Route path="/create-new-password" element={<CreatePassword />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/" element={<Products />} />
        <Route path="/product/:slug" element={<ProductDetails />} />
      </Routes>
      <StoreFooter />
    </BrowserRouter>
  );
}

export default App;
