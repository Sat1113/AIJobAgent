interface Resume {
  personalInfo: {
    name: string;
    email: string;
    phone: string;
    location: string;
  };
  summary: string;
  experience: Array<{
    title: string;
    company: string;
    duration: string;
    description: string[];
  }>;
  education: Array<{
    degree: string;
    institution: string;
    year: string;
  }>;
  skills: string[];
}

interface ResumePreviewProps {
  resume: Resume;
  onEdit?: () => void;
}

export default function ResumePreview({ resume, onEdit }: ResumePreviewProps) {
  return (
    <div className="bg-white shadow-lg rounded-lg p-8 max-w-4xl mx-auto">
      <div className="flex justify-between items-start mb-6">
        <div>
          <h1 className="text-3xl font-bold text-gray-800">{resume.personalInfo.name}</h1>
          <div className="mt-2 text-gray-600">
            <p>{resume.personalInfo.email} | {resume.personalInfo.phone}</p>
            <p>{resume.personalInfo.location}</p>
          </div>
        </div>
        {onEdit && (
          <button
            onClick={onEdit}
            className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
          >
            Edit Resume
          </button>
        )}
      </div>

      <div className="mb-6">
        <h2 className="text-xl font-semibold text-gray-800 mb-3">Professional Summary</h2>
        <p className="text-gray-700 leading-relaxed">{resume.summary}</p>
      </div>

      <div className="mb-6">
        <h2 className="text-xl font-semibold text-gray-800 mb-3">Experience</h2>
        {resume.experience.map((exp, index) => (
          <div key={index} className="mb-4 last:mb-0">
            <div className="flex justify-between items-start mb-2">
              <div>
                <h3 className="text-lg font-medium text-gray-800">{exp.title}</h3>
                <p className="text-gray-600">{exp.company}</p>
              </div>
              <p className="text-sm text-gray-500">{exp.duration}</p>
            </div>
            <ul className="text-gray-700">
              {exp.description.map((desc, descIndex) => (
                <li key={descIndex} className="mb-1">• {desc}</li>
              ))}
            </ul>
          </div>
        ))}
      </div>

      <div className="mb-6">
        <h2 className="text-xl font-semibold text-gray-800 mb-3">Education</h2>
        {resume.education.map((edu, index) => (
          <div key={index} className="mb-2 last:mb-0">
            <div className="flex justify-between items-start">
              <div>
                <h3 className="text-lg font-medium text-gray-800">{edu.degree}</h3>
                <p className="text-gray-600">{edu.institution}</p>
              </div>
              <p className="text-sm text-gray-500">{edu.year}</p>
            </div>
          </div>
        ))}
      </div>

      <div>
        <h2 className="text-xl font-semibold text-gray-800 mb-3">Skills</h2>
        <div className="flex flex-wrap gap-2">
          {resume.skills.map((skill, index) => (
            <span
              key={index}
              className="px-3 py-1 bg-gray-100 text-gray-700 rounded-full text-sm"
            >
              {skill}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
}