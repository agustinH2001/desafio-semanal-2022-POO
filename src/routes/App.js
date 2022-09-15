import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "../containers/Home";
import Semanal from "../containers/Semanal";
import Mensual from "../containers/Mensual";
import Layout from "../components/Layout";
import Login from "../components/Login";
import Registro from "../components/Registro";
import "../assets/css/App.css";
import AuthContex from "../context/AuthContex";
import RtdbContex from "../context/RtdbContex";
import ProtetecRoute from "../components/ProtetecRoute";
function App() {
  return (
    <>
      <BrowserRouter>
        <AuthContex>
          <Layout>
            <Routes>
              <Route exact path="/login" element={<Login />}></Route>
              <Route exact path="/registro" element={<Registro />}></Route>
              <Route exact path="/" element={<ProtetecRoute><Home /></ProtetecRoute>}></Route>
              <Route exact path="/semanales2022" element={<ProtetecRoute><RtdbContex><Semanal /></RtdbContex></ProtetecRoute>}></Route>
              <Route exact path="/mensuales2022" element={<ProtetecRoute><RtdbContex><Mensual /></RtdbContex></ProtetecRoute>}></Route>
            </Routes>
          </Layout>
        </AuthContex>
      </BrowserRouter>
    </>
  );
}

export default App;
