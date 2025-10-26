import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor
api.interceptors.request.use(
  (config) => {
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor
api.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    if (error.response) {
      // Server responded with error status
      console.error('API Error:', error.response.data);
    } else if (error.request) {
      // Request was made but no response received
      console.error('Network Error:', error.message);
    } else {
      // Something else happened
      console.error('Error:', error.message);
    }
    return Promise.reject(error);
  }
);

export const apiService = {
  // Get all boards
  getBoards: async () => {
    try {
      const response = await api.get('/boards');
      return response.data;
    } catch (error) {
      throw new Error(`Failed to fetch boards: ${error.message}`);
    }
  },

  // Get problems for a specific board
  getProblems: async (boardId) => {
    try {
      const response = await api.get(`/problems/${boardId}`);
      return response.data;
    } catch (error) {
      throw new Error(`Failed to fetch problems: ${error.message}`);
    }
  },

  // Get solutions for a specific problem
  getSolutions: async (problemId) => {
    try {
      const response = await api.get(`/solutions/${problemId}`);
      return response.data;
    } catch (error) {
      throw new Error(`Failed to fetch solutions: ${error.message}`);
    }
  },
};

export default api;

