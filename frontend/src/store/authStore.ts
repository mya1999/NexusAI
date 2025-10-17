import { create } from 'zustand';
import { authAPI } from '../lib/api';

interface AuthState {
  token: string | null;
  user: any | null;
  isAuthenticated: boolean;
  login: (email: string, password: string) => Promise<void>;
  register: (email: string, username: string, password: string) => Promise<void>;
  logout: () => void;
  loadUser: () => Promise<void>;
}

export const useAuthStore = create<AuthState>((set) => ({
  token: null,
  user: null,
  isAuthenticated: false,

  login: async (email: string, password: string) => {
    try {
      const response = await authAPI.login({ email, password });
      const { access_token } = response.data;
      localStorage.setItem('token', access_token);
      set({ token: access_token, isAuthenticated: true });
      
      // Load user data
      const userResponse = await authAPI.getMe();
      set({ user: userResponse.data });
    } catch (error) {
      throw error;
    }
  },

  register: async (email: string, username: string, password: string) => {
    try {
      await authAPI.register({ email, username, password });
    } catch (error) {
      throw error;
    }
  },

  logout: () => {
    localStorage.removeItem('token');
    set({ token: null, user: null, isAuthenticated: false });
  },

  loadUser: async () => {
    const token = localStorage.getItem('token');
    if (token) {
      try {
        const response = await authAPI.getMe();
        set({ token, user: response.data, isAuthenticated: true });
      } catch (error) {
        localStorage.removeItem('token');
        set({ token: null, user: null, isAuthenticated: false });
      }
    }
  },
}));
