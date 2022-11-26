import axios from "axios";
import { createContext, useState } from "react";
import jwt_decode from "jwt-decode";
import { useNavigate } from "react-router-dom";
import jwtInterceptor from "./jwtInterceptor";

const CURRENT_USER_URL = "http://127.0.0.1:8000/users/me/"

const AuthContext = createContext();

const getUserInfo = async () => {
  return await jwtInterceptor
    .get(CURRENT_USER_URL)
    .then((response) => response.data)
    .catch(error => {
      console.log('Error during fetching user data, user is null');
      return null;
    });
};

export const AuthContextProvider = ({ children }) => {
  const [user, setUser] = useState(getUserInfo());

  const navigate = useNavigate();

  const login = async (payload) => {
    const apiResponse = await axios.post(
      "http://127.0.0.1:8000/token/",
      payload
    );
    localStorage.setItem("tokens", JSON.stringify(apiResponse.data));
    setUser(getUserInfo());
    navigate("/");
  };
  const logout = async () => {
    localStorage.removeItem("tokens");
    setUser(null);
    navigate("/");
  };
  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;