import axios from "axios";

const REFRESH_URL = 'http://127.0.0.1:8000/token/refresh/';
const LOGIN_PAGE = '/login/';

const jwtInterceptor = axios.create({});

jwtInterceptor.interceptors.request.use((config) => {
  const tokensData = JSON.parse(localStorage.getItem("tokens"));
  if (tokensData) {
    config.headers["Authorization"] = `Bearer ${tokensData.access}`;
  }
  return config;
});

jwtInterceptor.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {

    if (error.response.data.code === 'token_not_valid') {
      console.log('Access token has expired.');
      const originalRequest = error.config;
      const authData = JSON.parse(localStorage.getItem("tokens"));
      const payload = {
        refresh: authData.refresh,
      };

      const apiResponse = await axios.post(
        REFRESH_URL,
        payload
      ).catch((error) => {
        if (error.response.data.code === 'token_not_valid') {
          console.log('Refresh token has expired.');
          window.location.href = LOGIN_PAGE;
        } else {
          return Promise.reject(error)
        }
      });
      localStorage.setItem("tokens", JSON.stringify({ refresh: authData.refresh, ...apiResponse.data }));
      originalRequest.headers["Authorization"] = `Bearer ${apiResponse.data.access}`;
      return axios({ ...originalRequest, headers: originalRequest.headers.toJSON() });
    } else 
    // if (error.response.status === 401) {
    //   window.location.href = LOGIN_PAGE;
    // } else 
    {
      return Promise.reject(error);
    }
  }
);

export default jwtInterceptor;