import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import { ArrowLeft, CheckCircle, Lightbulb, Loader2 } from 'lucide-react';
import { toast } from 'react-hot-toast';
import { apiService } from '../api';

const SolutionList = () => {
  const { problemId } = useParams();
  const navigate = useNavigate();
  const [solutions, setSolutions] = useState([]);
  const [problemText, setProblemText] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchSolutions();
  }, [problemId]);

  const fetchSolutions = async () => {
    try {
      setLoading(true);
      const data = await apiService.getSolutions(problemId);
      setSolutions(data);
      
      // Set problem text (we'll need to get this from the problem)
      setProblemText(`Problem #${problemId}`);
    } catch (error) {
      toast.error(error.message);
    } finally {
      setLoading(false);
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
        className="mb-6 sm:mb-8"
      >
        <button
          onClick={() => navigate(-1)}
          className="flex items-center space-x-2 text-blue-400 hover:text-blue-300 transition-colors mb-4 sm:mb-6"
        >
          <ArrowLeft className="w-4 h-4 sm:w-5 sm:h-5" />
          <span className="text-sm sm:text-base">Back to Problems</span>
        </button>
        
        <h1 className="text-2xl sm:text-3xl lg:text-4xl font-bold gradient-text mb-2">
          Solutions
        </h1>
        <p className="text-lg sm:text-xl text-gray-300 mb-4 sm:mb-6">
          Available solutions for {problemText}
        </p>
      </motion.div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4 sm:gap-6">
        {solutions.map((solution, index) => (
          <motion.div
            key={solution.id}
            initial={{ opacity: 0, y: 50 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: index * 0.1 }}
            whileHover={{ scale: 1.05, y: -5 }}
            className="glass-effect rounded-xl p-4 sm:p-6 card-hover group relative overflow-hidden"
          >
            <div className="absolute inset-0 bg-gradient-to-br from-green-500/10 to-emerald-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
            
            <div className="relative z-10">
              <motion.div
                whileHover={{ rotate: 360 }}
                transition={{ duration: 0.5 }}
                className="w-10 h-10 sm:w-12 sm:h-12 mb-3 sm:mb-4 p-2 sm:p-3 rounded-lg gradient-bg-accent flex items-center justify-center"
              >
                <CheckCircle className="w-5 h-5 sm:w-6 sm:h-6 text-white" />
              </motion.div>
              
              <h3 className="text-base sm:text-lg font-semibold text-white mb-2 sm:mb-3 group-hover:text-emerald-300 transition-colors">
                Solution {index + 1}
              </h3>
              
              <p className="text-gray-300 group-hover:text-gray-200 transition-colors leading-relaxed text-sm sm:text-base">
                {solution.solution_text}
              </p>
              
              <div className="mt-3 sm:mt-4 flex items-center space-x-2 text-emerald-400 group-hover:text-emerald-300 transition-colors">
                <Lightbulb className="w-3 h-3 sm:w-4 sm:h-4" />
                <span className="text-xs sm:text-sm font-medium">Recommended Solution</span>
              </div>
            </div>
          </motion.div>
        ))}
      </div>

      {solutions.length === 0 && !loading && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="text-center py-12"
        >
          <div className="w-24 h-24 mx-auto mb-6 rounded-full bg-gray-800 flex items-center justify-center">
            <CheckCircle className="w-12 h-12 text-gray-500" />
          </div>
          <h3 className="text-2xl font-bold text-gray-400 mb-2">No Solutions Available</h3>
          <p className="text-gray-500">There are currently no solutions for this problem.</p>
        </motion.div>
      )}
    </div>
  );
};

export default SolutionList;
