import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import { ArrowLeft, AlertTriangle, ArrowRight, Loader2 } from 'lucide-react';
import { toast } from 'react-hot-toast';
import { apiService } from '../api';

const ProblemList = () => {
  const { boardId } = useParams();
  const navigate = useNavigate();
  const [problems, setProblems] = useState([]);
  const [boardName, setBoardName] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchProblems();
  }, [boardId]);

  const fetchProblems = async () => {
    try {
      setLoading(true);
      const data = await apiService.getProblems(boardId);
      setProblems(data);
      
      // Get board name from API
      const boards = await apiService.getBoards();
      const board = boards.find(b => b.id === parseInt(boardId));
      if (board) {
        setBoardName(board.name);
      } else {
        setBoardName(`Board ${boardId}`);
      }
    } catch (error) {
      toast.error(error.message);
    } finally {
      setLoading(false);
    }
  };

  const handleProblemClick = (problemId) => {
    navigate(`/solutions/${problemId}`);
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
        className="mb-6 sm:mb-8"
      >
        <button
          onClick={() => navigate('/')}
          className="flex items-center space-x-2 text-blue-400 hover:text-blue-300 transition-colors mb-4 sm:mb-6"
        >
          <ArrowLeft className="w-4 h-4 sm:w-5 sm:h-5" />
          <span className="text-sm sm:text-base">Back to Boards</span>
        </button>
        
        <h1 className="text-2xl sm:text-3xl lg:text-4xl font-bold gradient-text mb-2">
          {boardName} - Problems
        </h1>
        <p className="text-lg sm:text-xl text-gray-300">
          Select a problem to view available solutions
        </p>
      </motion.div>

      <div className="space-y-4">
        {problems.map((problem, index) => (
          <motion.div
            key={problem.id}
            initial={{ opacity: 0, x: -50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.5, delay: index * 0.1 }}
            whileHover={{ scale: 1.02, x: 5 }}
            whileTap={{ scale: 0.98 }}
            onClick={() => handleProblemClick(problem.id)}
            className="glass-effect rounded-xl p-4 sm:p-6 cursor-pointer card-hover group relative overflow-hidden"
          >
            <div className="absolute inset-0 bg-gradient-to-r from-amber-500/10 to-orange-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
            
            <div className="relative z-10">
              <div className="flex items-start space-x-3 sm:space-x-4">
                <motion.div
                  whileHover={{ rotate: 360 }}
                  transition={{ duration: 0.5 }}
                  className="w-10 h-10 sm:w-12 sm:h-12 p-2 sm:p-3 rounded-lg gradient-bg-secondary flex items-center justify-center flex-shrink-0"
                >
                  <AlertTriangle className="w-5 h-5 sm:w-6 sm:h-6 text-white" />
                </motion.div>
                
                <div className="flex-1 min-w-0">
                  <h3 className="text-base sm:text-lg font-semibold text-white mb-2 group-hover:text-orange-300 transition-colors">
                    Problem: {problem.problem_text}
                  </h3>
                </div>
                
                <motion.div
                  whileHover={{ x: 5 }}
                  className="flex items-center space-x-1 sm:space-x-2 text-orange-400 group-hover:text-orange-300 transition-colors flex-shrink-0"
                >
                  <span className="font-medium text-xs sm:text-sm">View Solutions</span>
                  <ArrowRight className="w-4 h-4 sm:w-5 sm:h-5" />
                </motion.div>
              </div>
            </div>
          </motion.div>
        ))}
      </div>

      {problems.length === 0 && !loading && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="text-center py-12"
        >
          <div className="w-24 h-24 mx-auto mb-6 rounded-full bg-gray-800 flex items-center justify-center">
            <AlertTriangle className="w-12 h-12 text-gray-500" />
          </div>
          <h3 className="text-2xl font-bold text-gray-400 mb-2">No Problems Found</h3>
          <p className="text-gray-500">There are currently no problems for this board.</p>
        </motion.div>
      )}
    </div>
  );
};

export default ProblemList;
