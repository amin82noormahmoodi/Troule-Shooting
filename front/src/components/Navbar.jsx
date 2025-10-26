import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { Cpu, Home } from 'lucide-react';

const Navbar = () => {
  return (
    <motion.nav
      initial={{ y: -100, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.5 }}
      className="glass-effect border-b border-white/20"
    >
      <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-3 sm:py-4">
        <div className="flex items-center justify-between">
          <Link to="/" className="flex items-center space-x-2 sm:space-x-3 group">
            <motion.div
              whileHover={{ rotate: 360 }}
              transition={{ duration: 0.5 }}
              className="p-1.5 sm:p-2 rounded-lg gradient-bg-primary"
            >
              <Cpu className="w-5 h-5 sm:w-6 sm:h-6 text-white" />
            </motion.div>
            <span className="text-lg sm:text-xl lg:text-2xl font-bold gradient-text">
              Board Troubleshooter
            </span>
          </Link>
          
          <Link
            to="/"
            className="flex items-center space-x-1 sm:space-x-2 px-3 sm:px-4 py-2 rounded-lg glass-effect hover:neon-glow-blue transition-all duration-300 group"
          >
            <Home className="w-4 h-4 sm:w-5 sm:h-5 text-blue-400 group-hover:text-blue-300" />
            <span className="text-white group-hover:text-blue-300 text-sm sm:text-base">Home</span>
          </Link>
        </div>
      </div>
    </motion.nav>
  );
};

export default Navbar;
