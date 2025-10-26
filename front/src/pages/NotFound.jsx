import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';
import { Home, ArrowLeft } from 'lucide-react';

const NotFound = () => {
  return (
    <div className="max-w-4xl mx-auto text-center px-4 sm:px-6 lg:px-8">
      <motion.div
        initial={{ opacity: 0, scale: 0.8 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5 }}
        className="py-12 sm:py-16 lg:py-20"
      >
        <motion.div
          animate={{ 
            y: [0, -10, 0],
            rotate: [0, 5, 0]
          }}
          transition={{ 
            duration: 2,
            repeat: Infinity,
            ease: "easeInOut"
          }}
          className="w-24 h-24 sm:w-32 sm:h-32 mx-auto mb-6 sm:mb-8 rounded-full gradient-bg-primary flex items-center justify-center"
        >
          <span className="text-4xl sm:text-6xl font-bold text-white">404</span>
        </motion.div>
        
        <h1 className="text-3xl sm:text-4xl lg:text-5xl font-bold gradient-text mb-3 sm:mb-4">
          Page Not Found
        </h1>
        
        <p className="text-lg sm:text-xl text-gray-300 mb-6 sm:mb-8">
          The page you're looking for doesn't exist or has been moved.
        </p>
        
        <div className="flex flex-col sm:flex-row gap-3 sm:gap-4 justify-center">
          <Link
            to="/"
            className="inline-flex items-center space-x-2 px-4 sm:px-6 py-3 rounded-lg glass-effect hover:neon-glow-blue transition-all duration-300 group"
          >
            <Home className="w-4 h-4 sm:w-5 sm:h-5 text-blue-400 group-hover:text-blue-300" />
            <span className="text-white group-hover:text-blue-300 text-sm sm:text-base">Back to Home</span>
          </Link>
          
          <button
            onClick={() => window.history.back()}
            className="inline-flex items-center space-x-2 px-4 sm:px-6 py-3 rounded-lg glass-effect hover:neon-glow-purple transition-all duration-300 group"
          >
            <ArrowLeft className="w-4 h-4 sm:w-5 sm:h-5 text-purple-400 group-hover:text-purple-300" />
            <span className="text-white group-hover:text-purple-300 text-sm sm:text-base">Go Back</span>
          </button>
        </div>
      </motion.div>
    </div>
  );
};

export default NotFound;
