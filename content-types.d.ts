// Auto-generated from scripts/types-schema.yaml and scripts/content-schema.yaml
// Do not edit manually. Changes are committed automatically by the pre-commit hook.

export interface RootFields {
  achievements: string | string[];
  bio: string;
  company?: string;
  contacts: string | string[];
  cover?: string;
  educations: string;
  experience_company: string | string[];
  experience_month?: number;
  expertise_area: string;
  first_name: string;
  highlight_text?: string | string[];
  last_name: string;
  location: string;
  projects: string | string[];
  seniority: string;
  skills: string | string[];
}

export interface AboutFields {
  aliases: string | string[];
  description: string;
  excerpt: string;
}

export interface AchievementFields {
  aliases: string | string[];
  cover: string;
  description: string;
  year: number;
}

export interface ContactFields {
  aliases: string | string[];
  icon: string;
  label: string;
  tooltip: string;
  url: string;
}

export interface EducationFields {
  aliases: string | string[];
  degree_type: string;
  description: string;
  institution: string;
  year: number;
}

export interface ExperienceFields {
  aliases: string | string[];
  description: string;
  employment_type: string;
  end?: string;  // YYYY-MM-DD
  excerpt: string;
  expertise_area: string;
  site?: string;
  stacks: string | string[];
  start: string;  // YYYY-MM-DD
}

export interface ProjectFields {
  aliases: string | string[];
  company: string | string[];
  cover?: string;
  description: string;
  end?: string;  // YYYY-MM-DD
  excerpt: string;
  stack: string | string[];
  start: string;  // YYYY-MM-DD
  url?: string;
}

export interface SeniorityFields {
  aliases: string | string[];
}

export interface SkillFields {
  aliases: string | string[];
  description: string;
  icon: string;
  technologies: string | string[];
}

export interface TechnologyFields {
  aliases: string | string[];
  description: string;
}
