import Login from "./views/auth/Login";
import { Route, Routes, BrowserRouter } from 'react-router-dom'; 
import Register from "./views/auth/Register";
import Dashboard from "./views/auth/Dashboard";
import Logout from "./views/auth/Logout";
function App() {
  return   <BrowserRouter>
  <Routes>
    <Route path="/login" element={<Login />}/>
    <Route path="/register" element={<Register />}/>
    <Route path="/logout" element={<Logout />}/>
    <Route path="/" element={<Dashboard />}/>
      

  </Routes>
  
  </BrowserRouter>;
}

export default App;
