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

  I developed reusable components for different project needs, from basic elements like **buttons and checkboxes** to more complex components like **Picklists/Transfers** and inputs with **dynamic masks** for formats such as CPF, CNPJ, and phone numbers.

  I was also responsible for **API documentation of the components**, describing their properties, behaviors, and usage patterns to facilitate adoption and maintenance by consuming projects.

  Beyond the functional implementation, I worked on defining **transitions, animations, and microinteractions** for the components, seeking to create visually appealing behaviors and a distinct identity for the library. I also optimized these animations to balance visual quality with interface performance.

  Another important focus was the **experience on mobile devices**. I adapted components and behaviors for different screen sizes, seeking to bring the usage experience closer to what users find in native applications. Among the implemented behaviors were patterns such as **modals, popups, and dropdowns that, on smaller screens, took on behavior similar to drawers sliding up from the bottom of the screen**, along with other specific adaptations for touch interaction.

  I also worked on the structure needed for **private packaging and distribution of the library**, allowing it to be consumed by the different company projects.
challenge: |-
  One of the main challenges was defining a way to **distribute the library privately**. Since the components were part of internal company solutions, making them publicly available would not be appropriate. I researched available free alternatives and evaluated different possibilities before choosing **GitLab Registry** as the solution for private package storage and distribution.

  Another challenge was understanding the entire process required to **create and package a component library**, including choosing an adequate bundling solution. Since I did not yet have experience with this type of architecture, I studied available alternatives, mainly considering widely used solutions with a lower learning curve, in order to implement the library quickly.

  I also faced challenges related to **making the library available in production environments**. Since consuming projects ran on different VPSs and used Docker, I needed to find a way to obtain the private library **during the application dependency installation step**, ensuring the package was correctly available during the production environment build process.

  This process required a deeper study of the dependency installation flow in applications run with Docker and the proper way to authenticate and make a private package available during that process.

  Another challenge was **optimizing the library so the final bundle would be as small as possible**, analyzing its structure and the packaging process to reduce unnecessary content and make library installation and updates more efficient.

  There were also challenges related to creating **consistent and performant animations and transitions**. It was necessary to consider duration, behavior, fluidity, and impact on performance so that the microinteractions made the components more appealing without harming the user experience.

  In the mobile context, the challenge was adapting components originally designed for traditional web interfaces so they presented **more natural behaviors on smaller screens and touch interactions**. This involved rethinking how elements such as modals, dropdowns, and popups were presented and interacted with users, seeking an experience closer to the patterns mobile device users are already accustomed to.

  All these challenges had to be solved in a context of **high demand at the beginning of the project**, requiring agility in research, decision-making, and implementation, without losing sight of the need to create a reusable and sustainable solution.
result: |-
  The creation of the library centralized shared components into a **single codebase**, eliminating the need to maintain duplicated implementations across different applications.

  The library gained a **private distribution structure**, allowing consuming projects to use the components without exposing packages or source code publicly.

  API documentation established a reference for **component properties, behaviors, and usage patterns**, facilitating consumption and maintenance.

  The definition of **distinct animations, transitions, and microinteractions** contributed to creating a more consistent visual and behavioral identity for the components, making interfaces more appealing without sacrificing performance concerns.

  The mobile adaptations provided an experience better suited to **touch interactions and smaller screens**, incorporating behavior patterns that made components such as modals, dropdowns, and popups more natural in that context.

  The optimizations made in the packaging process also reduced the **final library size**, making its installation and updates more efficient in consuming projects.

  As a result, the library became a **reusable solution for different company projects**, providing greater visual and behavioral consistency between applications, reducing code duplication, and centralizing component evolution.
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

