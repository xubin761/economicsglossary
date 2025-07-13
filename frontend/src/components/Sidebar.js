import React from 'react';
import { Link } from 'react-router-dom';
import { 
  Stethoscope, 
  FileCheck, 
  BookOpen, 
  FileEdit, 
  FileText
} from 'lucide-react';

const Sidebar = ({ width }) => {
  return (
    <div className="bg-white shadow-lg" style={{ width: `${width}px` }}>
      <div className="p-5">
        <img src="/images/economics.jpg" alt="医疗图标" className="w-16 h-16 mx-auto mb-4" />
        <h1 className="text-xl font-bold mb-2">经济术语工具箱</h1>
        <p className="text-sm text-gray-600 mb-4">强大的经济术语工具集</p>
      </div>
      <nav className="mt-5">
        <Link to="/stand" className="flex items-center p-3 text-gray-700 hover:bg-gray-100">
          <FileCheck className="mr-3" /> 经济术语标准化
        </Link>
           </nav>
    </div>
  );
};

export default Sidebar;