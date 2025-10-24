# AI Job Agent Frontend

This is the frontend application for the AI Job Agent built with Next.js, TypeScript, and Tailwind CSS.

## Features

- **Job Analysis**: AI-powered analysis of job descriptions
- **Resume Optimization**: Automatically optimize resumes for specific jobs
- **Job Scraping**: Find and scrape job opportunities
- **Application Tracking**: Track job applications and their status

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Installation

1. Install dependencies:
```bash
npm install
```

2. Create a `.env.local` file with your environment variables:
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

3. Run the development server:
```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Project Structure

```
src/
├── app/              # Next.js App Router pages
├── components/       # Reusable React components
└── lib/             # Utilities and API client
```

## Components

- **JobCard**: Display job listings with key information
- **ResumePreview**: Preview and edit resume content
- **API Client**: Handle communication with backend services

## Development

The app uses:
- **Next.js 15** with App Router
- **TypeScript** for type safety
- **Tailwind CSS** for styling
- **ESLint** for code quality

## Build

```bash
npm run build
npm start
```