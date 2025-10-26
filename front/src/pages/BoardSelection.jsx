import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import { Cpu, ArrowRight, Loader2, Search } from 'lucide-react';
import { toast } from 'react-hot-toast';
import { apiService } from '../api';
import Dropdown from '../components/Dropdown';

const BoardSelection = () => {
  const [boards, setBoards] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedBoard, setSelectedBoard] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    fetchBoards();
  }, []);

  const fetchBoards = async () => {
    try {
      setLoading(true);
      const data = await apiService.getBoards();
      setBoards(data);
    } catch (error) {
      toast.error(error.message);
    } finally {
      setLoading(false);
    }
  };

  const handleBoardSelect = (board) => {
    setSelectedBoard(board);
  };

  const handleContinueClick = () => {
    if (selectedBoard) {
      navigate(`/problems/${selectedBoard.id}`);
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <motion.div
          animate={{ rotate: 360 }}
          transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
          className="w-12 h-12 border-4 border-cyan-500 border-t-transparent rounded-full"
        />
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="text-center mb-8 sm:mb-12"
      >
        <h1 className="text-3xl sm:text-4xl lg:text-5xl font-bold gradient-text mb-4">
          Board Troubleshooter
        </h1>
        <p className="text-lg sm:text-xl text-gray-300 mb-6 sm:mb-8 px-4">
          Select a board to view its troubleshooting problems
        </p>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 0.2 }}
        className="mb-8"
      >
        <div className="flex items-center justify-center mb-4 sm:mb-6">
          <Search className="w-5 h-5 sm:w-6 sm:h-6 text-blue-400 mr-2 sm:mr-3" />
          <h2 className="text-xl sm:text-2xl font-semibold text-white">Choose Your Board</h2>
        </div>
        
        <Dropdown
          options={boards}
          selectedOption={selectedBoard}
          onSelect={handleBoardSelect}
          placeholder="Select a board from the list..."
        />
      </motion.div>

      {selectedBoard && (
        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.4 }}
          className="text-center mb-8"
        >
          <div className="glass-effect rounded-2xl p-6 sm:p-8 max-w-2xl mx-auto">
            <motion.div
              whileHover={{ rotate: 360 }}
              transition={{ duration: 0.5 }}
              className="w-16 h-16 sm:w-20 sm:h-20 mx-auto mb-4 sm:mb-6 p-4 sm:p-5 rounded-2xl gradient-bg-primary flex items-center justify-center"
            >
              <Cpu className="w-8 h-8 sm:w-10 sm:h-10 text-white" />
            </motion.div>
            
            <h3 className="text-2xl sm:text-3xl font-bold text-white mb-3 sm:mb-4">
              {selectedBoard.name}
            </h3>
            
            <p className="text-gray-300 mb-4 sm:mb-6 text-sm sm:text-base">
              Ready to troubleshoot problems for this board
            </p>
            
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={handleContinueClick}
              className="inline-flex items-center space-x-2 sm:space-x-3 px-6 sm:px-8 py-3 sm:py-4 gradient-bg-primary rounded-xl text-white font-semibold hover:neon-glow-blue transition-all duration-300 shadow-lg hover:shadow-2xl text-sm sm:text-base"
            >
              <span>View Problems</span>
              <ArrowRight className="w-4 h-4 sm:w-5 sm:h-5" />
            </motion.button>
          </div>
        </motion.div>
      )}

      {boards.length === 0 && !loading && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="text-center py-12"
        >
          <div className="w-24 h-24 mx-auto mb-6 rounded-full bg-gray-800 flex items-center justify-center">
            <Cpu className="w-12 h-12 text-gray-500" />
          </div>
          <h3 className="text-2xl font-bold text-gray-400 mb-2">No Boards Available</h3>
          <p className="text-gray-500">There are currently no boards in the system.</p>
        </motion.div>
      )}
    </div>
  );
};

export default BoardSelection;
