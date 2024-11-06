import { useAuthStore } from "../store/auth";
import apiInstance from "./axios";
import * as jwtDecode from 'jwt-decode';

import Cookies from "js-cookie";

export const login = async (email, password) => {
  try {
    const { data, status } = await apiInstance.post("auth/login/", {
      email,
      password,
    });
    if (status === 200) {
      setAuthUser(data?.access, data?.refresh);
    }
    return { data, error: null };
  } catch (error) {
    return {
      data: null,
      error: error.response?.data?.detail || "Something went wrong",
    };
  }
};

export const register = async (
  full_name,
  email,
  phone,
  password,
  password2
) => {
  try {
    const { data } = await apiInstance.post("auth/register/", {
      full_name,
      email,
      phone,
      password,
      password2,
    });
    await login(email, password);
    return { data, error: null };
  } catch (error) {
    return {
      data: null,
      error: error.response?.data?.detail || "Something went wrong",
    };
  }
};

export const logout=()=>{
    Cookies.remove("access_token")
    Cookies.remove("refresh_token")
    useAuthStore.getState().setUser(null)
}

export const setUser=async()=>{
    const refreshToken=Cookie.get("refresh_token")
    const accessToken=Cookie.get("access_token")
    if(!accessToken||!refreshToken){
        return;
    }

    if(isAccessTokenExpired(accessToken)){
        const response = await getRefreshToken(refreshToken)
        setAuthUser(response?.access, response?.refresh)
    }else{
        setAuthUser(accessToken,refreshToken)
    }
}


export const setAuthUser=(access_token,refresh_token)=>{
    Cookies.set("access_token",access_token,{
        expires:1,secure:true
    })
    Cookies.set("refresh_token",refresh_token,{
        expires:7,secure:true
    })

    const user =jwtDecode (access_token)??null

    if(user){
        useAuthStore.getState().setUser(user)
    }

    useAuthStore.getState().setLoading(false)
}

export const getRefreshToken=async()=>{

    const refresh_token=Cookies.get("refresh_token")
    const response = await apiInstance.post("auth/refresh/",{
        refresh:refresh_token
    })

    return response.data
}

export const isAccessTokenExpired=(access_token)=>{
    try{
        const decodedToken=jwtDecode (access_token)
        return decodedToken.exp<Date.now()/100
    }catch(error){
        console.error(error)
        return true
    }
}