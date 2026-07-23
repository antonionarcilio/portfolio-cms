// Auto-generated from scripts/types-schema.yaml and scripts/content-schema.yaml
// Do not edit manually. Changes are committed automatically by the pre-commit hook.

export interface RootFields {
  achievements: string[];
  bio: string;
  company?: string[];
  contacts: string[];
  cover?: string;
  educations: string;
  experience_company: string[];
  experience_month?: number;
  expertise_area: string[];
  first_name: string;
  highlight_text?: string[];
  last_name: string;
  location: string;
  projects: string[];
  seniority: string;
  skills: string[];
}

export interface AboutFields {
  aliases: string[];
  description: string;
  excerpt: string;
}

export interface AchievementFields {
  aliases: string[];
  cover: string;
  description: string;
  year: number;
}

export interface ContactFields {
  aliases: string[];
  icon: string;
  label: string;
  tooltip: string;
  url: string;
}

export interface EducationFields {
  aliases: string[];
  degree_type: string;
  description: string;
  institution: string;
  year: number;
}

export interface ExperienceFields {
  aliases: string[];
  description: string;
  employment_type: string;
  end?: string;  // YYYY-MM-DD
  excerpt: string;
  expertise_area: string;
  site?: string;
  stacks: string[];
  start: string;  // YYYY-MM-DD
}

export interface ProjectFields {
  aliases: string[];
  company: string[];
  cover?: string;
  description: string;
  end?: string;  // YYYY-MM-DD
  excerpt: string;
  stack: string[];
  start: string;  // YYYY-MM-DD
  url?: string;
}

export interface SeniorityFields {
  aliases: string[];
}

export interface SkillFields {
  aliases: string[];
  description: string;
  icon: string;
  technologies: string[];
}

export interface TechnologyFields {
  aliases: string[];
  description: string;
}
