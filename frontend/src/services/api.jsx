import axios from "axios";

const API = axios.create({
    baseURL: "aisportsquizagent.railway.internal"
});

export default API;