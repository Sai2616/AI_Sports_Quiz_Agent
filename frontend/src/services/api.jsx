import axios from "axios";

const API = axios.create({
    baseURL: "aisportsquizagent-production.up.railway.app"
});

export default API;