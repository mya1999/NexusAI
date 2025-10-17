'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { useAuthStore } from '@/store/authStore';
import { dataAPI, mlAPI } from '@/lib/api';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

export default function DashboardPage() {
  const router = useRouter();
  const { isAuthenticated, user, logout, loadUser } = useAuthStore();
  const [stats, setStats] = useState<any>(null);
  const [dataPoints, setDataPoints] = useState<any[]>([]);
  const [modelInfo, setModelInfo] = useState<any>(null);
  const [prediction, setPrediction] = useState<number | null>(null);

  useEffect(() => {
    loadUser().then(() => {
      if (!isAuthenticated) {
        router.push('/login');
      }
    });
  }, [isAuthenticated]);

  useEffect(() => {
    if (isAuthenticated) {
      loadDashboardData();
    }
  }, [isAuthenticated]);

  const loadDashboardData = async () => {
    try {
      const [statsRes, dataRes, modelRes] = await Promise.all([
        dataAPI.getStats(),
        dataAPI.getDataPoints({ limit: 20 }),
        mlAPI.getModelInfo(),
      ]);

      setStats(statsRes.data);
      setDataPoints(dataRes.data);
      setModelInfo(modelRes.data);
    } catch (error) {
      console.error('Failed to load dashboard data:', error);
    }
  };

  const handlePredict = async () => {
    try {
      const features = [Math.random(), Math.random(), Math.random()];
      const result = await mlAPI.predict(features);
      setPrediction(result.data.prediction);
    } catch (error) {
      console.error('Prediction failed:', error);
    }
  };

  const handleLogout = () => {
    logout();
    router.push('/login');
  };

  if (!isAuthenticated) {
    return <div>Loading...</div>;
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
          <h1 className="text-2xl font-bold text-gray-900">NexusAI Dashboard</h1>
          <div className="flex items-center space-x-4">
            <span className="text-sm text-gray-600">
              {user?.email}
            </span>
            <button
              onClick={handleLogout}
              className="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600"
            >
              Logout
            </button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-sm font-medium text-gray-500">Total Data Points</h3>
            <p className="mt-2 text-3xl font-semibold text-gray-900">
              {stats?.total_count || 0}
            </p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-sm font-medium text-gray-500">Average Value</h3>
            <p className="mt-2 text-3xl font-semibold text-gray-900">
              {stats?.average_value?.toFixed(2) || '0.00'}
            </p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-sm font-medium text-gray-500">Min Value</h3>
            <p className="mt-2 text-3xl font-semibold text-gray-900">
              {stats?.min_value?.toFixed(2) || '0.00'}
            </p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-sm font-medium text-gray-500">Max Value</h3>
            <p className="mt-2 text-3xl font-semibold text-gray-900">
              {stats?.max_value?.toFixed(2) || '0.00'}
            </p>
          </div>
        </div>

        {/* Chart */}
        <div className="bg-white p-6 rounded-lg shadow mb-8">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">Data Trends</h2>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={dataPoints}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="value" stroke="#3b82f6" />
            </LineChart>
          </ResponsiveContainer>
        </div>

        {/* ML Model Info & Prediction */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">ML Model Info</h2>
            {modelInfo && (
              <div className="space-y-2">
                <p><span className="font-medium">Model Type:</span> {modelInfo.model_type}</p>
                <p><span className="font-medium">Version:</span> {modelInfo.version}</p>
                <p><span className="font-medium">Accuracy:</span> {(modelInfo.accuracy * 100).toFixed(1)}%</p>
              </div>
            )}
          </div>

          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">Make Prediction</h2>
            <button
              onClick={handlePredict}
              className="w-full px-4 py-2 bg-primary text-white rounded hover:bg-blue-600"
            >
              Generate Prediction
            </button>
            {prediction !== null && (
              <div className="mt-4 p-4 bg-blue-50 rounded">
                <p className="text-sm text-gray-600">Prediction Result:</p>
                <p className="text-2xl font-bold text-primary">{prediction.toFixed(4)}</p>
              </div>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}
