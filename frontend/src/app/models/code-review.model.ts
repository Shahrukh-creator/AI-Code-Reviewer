export interface ReviewRequest {
    language: string;
    code: string;
  }
  
  export interface ReviewIssue {
    severity: string;
    category: string;
    line: number | null;
    problem: string;
    explanation: string;
    suggestion: string;
  }
  
  export interface CodeReview {
    summary: string;
    score: number;
    issues: ReviewIssue[];
    strengths: string[];
  }
  
  export interface ReviewSource {
    source: string;
    category: string;
    distance: number;
  }
  
  export interface ReviewResponse {
    review: CodeReview;
    sources: ReviewSource[];
  }