interface Job {
  id: string;
  title: string;
  company: string;
  location: string;
  salary?: string;
  description: string;
  requirements: string[];
  posted: string;
}

interface JobCardProps {
  job: Job;
  onAnalyze?: (job: Job) => void;
}

export default function JobCard({ job, onAnalyze }: JobCardProps) {
  return (
    <div className="bg-white rounded-lg shadow-md p-6 mb-4 hover:shadow-lg transition-shadow">
      <div className="flex justify-between items-start mb-4">
        <div>
          <h3 className="text-xl font-semibold text-gray-800">{job.title}</h3>
          <p className="text-gray-600">{job.company}</p>
          <p className="text-sm text-gray-500">{job.location}</p>
        </div>
        {job.salary && (
          <div className="text-right">
            <p className="text-lg font-medium text-green-600">{job.salary}</p>
          </div>
        )}
      </div>
      
      <div className="mb-4">
        <p className="text-gray-700 line-clamp-3">{job.description}</p>
      </div>
      
      <div className="mb-4">
        <h4 className="font-medium text-gray-800 mb-2">Requirements:</h4>
        <ul className="text-sm text-gray-600">
          {job.requirements.slice(0, 3).map((req, index) => (
            <li key={index} className="mb-1">• {req}</li>
          ))}
          {job.requirements.length > 3 && (
            <li className="text-gray-500">... and {job.requirements.length - 3} more</li>
          )}
        </ul>
      </div>
      
      <div className="flex justify-between items-center">
        <p className="text-xs text-gray-500">Posted: {job.posted}</p>
        {onAnalyze && (
          <button
            onClick={() => onAnalyze(job)}
            className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
          >
            Analyze Match
          </button>
        )}
      </div>
    </div>
  );
}