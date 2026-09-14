---
aliases:
  - UIKit
description: |-
  Component library developed to standardize interfaces, reduce visual inconsistencies between applications, and decrease dependency on external libraries, ensuring greater scalability, maintainability, and alignment with the company's Design System.

  I worked on implementing, maintaining, and evolving the library, developing reusable and scalable components, from basic elements like buttons and checkboxes to more complex components like picklists/transfers and inputs with dynamic masks (CPF, CNPJ, phone number, among others).

  I contributed to improving visual consistency between products, speeding up application development, and increasing code reuse across different company projects.
excerpt: Library of reusable and scalable components for interface standardization and alignment with the company's Design System.
objective: |-
  Create a **shared component library** to centralize Design System elements used by different applications, reducing code duplication and making maintenance, evolution, and component reuse across projects easier.

  The initiative arose from the need to maintain two projects developed simultaneously that shared the same Design System. Centralization allowed components that were previously maintained separately to become a **reusable solution for different applications and new company projects**.
what_i_built: |-
  I identified the need to centralize shared components and **took the initiative to create the library**, being responsible for its implementation, evolution, and maintenance.

  I developed reusable components for different project needs, from basic elements like **buttons and checkboxes** to more complex components like **Picklists/Transfers** and inputs with **dynamic masks** for formats such as CPF, CNPJ, and phone numbers, among others.

  I was also responsible for **API documentation of the components**, describing their properties, behaviors, and usage patterns to facilitate adoption and maintenance by consuming projects.

  Beyond component development, I worked on the necessary structure for **library packaging and distribution**, enabling it to be consumed privately by different company projects.

  I also handled maintenance and evolution of the library, performing fixes on **logic, behavior, and styles**, as well as bundle optimizations to reduce the final package size and make installation and updates more efficient.
challenge: |-
  One of the main challenges was defining a way to **distribute the library privately**. Since the components were part of internal company solutions, making them publicly available would not be appropriate. I researched available free alternatives and evaluated different possibilities before choosing **GitLab Registry** as the solution for private package storage and distribution.

  Another challenge was understanding the entire process required to **create and package a component library**, including choosing an adequate bundling solution. Since I did not yet have experience with this type of architecture, I studied available alternatives, mainly considering widely used solutions with a lower learning curve, in order to implement the library quickly.

  I also faced challenges related to **making the library available in development and especially production environments**. Since consuming projects ran on different VPSs and used Docker, I needed to find a way to obtain the private library **during the application dependency installation step**, ensuring the package was correctly available in the production environment build process.

  This process required a deeper study of the dependency installation flow in applications run with Docker and the proper way to authenticate and make a private package available during this process, ensuring the library could be consumed without compromising application distribution.

  Another challenge was **optimizing the library so the final bundle would be as small as possible**. I analyzed the package structure and packaging process, seeking to reduce unnecessary content distributed to consuming projects and making library installation and updates more efficient.

  All these challenges had to be solved in a context of **high demand at the beginning of the project**, requiring agility in research, decision-making, and implementation, without losing sight of the need to create a solution that could be reused and maintained over time.
result: |-
  The creation of the library centralized shared components into a **single codebase**, eliminating the need to maintain duplicated implementations across different applications.

  The library gained a **private distribution structure**, allowing consuming projects to use the components without exposing packages or source code publicly.

  API documentation established a reference for **component properties, behaviors, and usage patterns**, facilitating consumption and maintenance.

  Optimizations in the packaging process reduced the **final library size**, making installation and updates more efficient in consuming projects.

  As a result, the library became a **reusable solution for different company projects**, providing greater consistency between applications, reducing code duplication, and making component maintenance and evolution more centralized.
company: "[[content/experience/escallo/index.en.md|Escallo]]"
expertise_area: Frontend
url:
start: 2025-09-01
end: 2026-02-06
cover:
carrousel:
  - https://res.cloudinary.com/do39nkgr5/image/upload/v1789398493/MacBook_Air_-_14_cvwt7g.png
  - https://res.cloudinary.com/do39nkgr5/image/upload/v1789398495/MacBook_Air_-_15_ht2hr0.png
  - https://res.cloudinary.com/do39nkgr5/image/upload/v1789398494/MacBook_Air_-_16_k4jt8r.png
stack:
  - "[[content/technology/typescript/index.en|TypeScript]]"
  - "[[content/technology/react/index.en|React]]"
  - "[[content/technology/storybook/index.en|Storybook]]"
  - "[[content/technology/css-modules/index.en|CSS Modules]]"
  - "[[content/technology/rollup/index.en|Rollup]]"
  - "[[content/technology/framer-motion/index.en|Framer Motion]]"
---

