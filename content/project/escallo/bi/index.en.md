---
aliases:
  - BI
description: |-
  Application developed to centralize strategic metrics and operational indicators related to customer service and experience.

  I worked on developing dashboards, charts, and analytical interfaces focused on visualizing and tracking operational metrics, contributing to a clear and efficient presentation of strategic indicators and data.
excerpt: Centralizes strategic metrics and operational indicators with dashboards and analytical interfaces for efficient data visualization.
objective: To centralize and present **strategic metrics, operational indicators, and Customer Experience (CX) metrics** related to customer service and experience, making it easier to track and interpret data through dashboards and analytical interfaces.
what_i_built: |-
  I worked on **building the application from start to finish** alongside another developer, taking part in every stage of development. We split the implementation by type of visualization: I was responsible for building the **charts and dashboards**, while the other developer focused mostly on implementing the **tables**.

  I was responsible for implementing different types of **charts and data visualization components**, working on the presentation of operational metrics, strategic indicators, and CX metrics. I also took part in structuring the interfaces and organizing the information, aiming to make the data clearer and easier to interpret.

  I also developed a **permission management layer in the application**, responsible for identifying the user's access level and controlling which pages and features could be accessed according to their permissions.

  Throughout development, I also worked on **evolving and adapting the interfaces for different screen formats**, ranging from smaller devices to large-format displays used to showcase the indicators.
challenge: |-
  One of the main challenges was dealing with **more complex data visualizations**. In some cases, requirements involved charts with specific layouts and behaviors that were not available in the public libraries we used. It was necessary to study how these visualizations worked and develop certain parts manually to meet the project's specific needs.

  Another challenge was related to **API limitations**. The available structure demanded extra care in how data was consumed, making it necessary to implement strategies to **reduce unnecessary requests and optimize information processing**. These decisions were important to minimize loading impacts and provide a smoother experience when using the dashboards.

  The API limitations also extended to **access control**. Since there was no proper permission validation on the backend, users could access pages and information regardless of the access level defined for their accounts. In view of this, I developed a **permission management layer on the frontend**, structuring rules to control access to features and pages according to the user's profile.

  Defining this system also brought challenges related to **understanding and evolving the permission requirements**. During development, the rules structure went through recurring changes, requiring reviews and, in some cases, reworking parts that had already been implemented. This scenario demanded continuous adaptation of the solution and greater attention to how access rules were structured.

  The **responsiveness of the visualizations** also required different approaches. Some charts needed to adapt not only to smaller screens, but also to **large-format displays, including televisions**, where the application would be used frequently. It was necessary to consider each visualization's behavior at different dimensions individually, preserving their legibility and the correct presentation of data.
result: |-
  The project resulted in an application capable of centralizing **operational indicators, strategic metrics, and CX metrics** in an analytical interface, making it easier to track information related to customer service and experience.

  The implementation of the graphical visualizations made it possible to represent different data sets in a **clear way, suited to each context**, including custom charts developed to meet needs that were not covered by the available libraries.

  The permission management layer established **access control within the application**, directing users to the features and pages compatible with their respective permission levels.

  The optimizations made in the API communication contributed to **more efficient use of available resources and a smoother browsing experience**, while the visualization adaptations enabled the application to be used on different screen formats, from smaller devices to televisions.
company: "[[content/experience/escallo/index.en.md|Escallo]]"
expertise_area: Frontend
url:
start: 2022-04-04
end: 2022-12-30
cover:
carrousel:
  - https://res.cloudinary.com/do39nkgr5/image/upload/v1789240415/MacBook_Air_-_11_u9jjpm.png
  - https://res.cloudinary.com/do39nkgr5/image/upload/v1789240415/MacBook_Air_-_12_cfsz3y.png
  - https://res.cloudinary.com/do39nkgr5/image/upload/v1789240415/MacBook_Air_-_13_xzscva.png
stack:
  - "[[content/technology/javascript/index.en|JavaScript]]"
  - "[[content/technology/react/index.en|React]]"
  - "[[content/technology/styled-components/index.en|Styled Components]]"
  - "[[content/technology/redux/index.en|Redux]]"
  - "[[content/technology/material-ui/index.en|Material UI]]"
  - "[[content/technology/graphql/index.en|GraphQL]]"
---
