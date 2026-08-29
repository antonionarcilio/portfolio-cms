---
aliases:
  - Portal
description: |-
  Aplicação desenvolvida para **centralizar o acesso às diferentes soluções do ecossistema da empresa**, permitindo que o usuário se autentique uma única vez e acesse produtos e funcionalidades de acordo com suas permissões. **Atuei como desenvolvedor frontend** ao longo do desenvolvimento, manutenção e evolução contínua do produto, contribuindo também com **UI/UX** na definição e melhoria de alguns fluxos e interfaces.

  Em parceria com outro desenvolvedor, participei da **implementação da aplicação desde sua concepção inicial**, desenvolvendo funcionalidades centrais como o **sistema de controle de acesso**, que permitia gerenciar usuários e definir seus respectivos **níveis de acesso**. A partir desses níveis, eram determinadas as funcionalidades disponíveis para cada usuário, como possibilidade de acesso a soluções externas, **gerenciamento de assinaturas e notas fiscais** e um **MVP de pipeline de vendas**.

  Com a evolução do produto, também assumi a continuidade do **Design System**, cuja estrutura inicial havia sido prototipada por um designer. Conforme a aplicação ganhou maturidade, passei a evoluir componentes, padrões visuais e comportamentos de interface de acordo com as necessidades identificadas durante o desenvolvimento.

  Durante esse processo, também atuei na **investigação e resolução de problemas técnicos e de performance**. Entre eles, diagnostiquei um comportamento presente apenas em builds de produção que fazia componentes do layout compartilhado, como o sidebar, serem remontados durante a navegação, provocando a reexecução indesejada de animações de entrada. Após investigar o comportamento do **App Router do Next.js**, implementei um controle manual do estado das animações para garantir sua execução apenas nos momentos apropriados.

  Também trabalhei na **otimização da comunicação com a API**, reduzindo requisições redundantes por meio da consolidação de queries GraphQL em uma única chamada por página.
excerpt: Plataforma que centraliza autenticação e controle de acesso às soluções da empresa. Atuei no frontend desde a concepção, evoluindo funcionalidades, Design System, UI/UX e performance.
objective: Centralizar o acesso às diferentes soluções do ecossistema da empresa, oferecendo aos clientes uma experiência unificada de autenticação, acesso e gerenciamento de permissões. Ao longo da evolução do produto, também passou a incorporar soluções internas utilizadas por diferentes áreas da empresa.
what-i-built: |-
  Atuei, em parceria com outro desenvolvedor, na implementação do produto desde sua concepção inicial, como **desenvolvedor frontend** na construção e evolução das principais funcionalidades. Com a evolução do produto, também assumi responsabilidades relacionadas a **UI/UX e design de interfaces**.

  Fui responsável pela implementação do **sistema de controle de acesso**, permitindo o gerenciamento de usuários e a definição de seus níveis de permissão, além de funcionalidades relacionadas ao gerenciamento de assinaturas e notas fiscais e à implementação de um **MVP de pipeline de vendas**.

  Também contribuí com a definição e evolução de fluxos e interfaces e assumi a continuidade do **Design System**, evoluindo componentes, padrões visuais e comportamentos de interface conforme as necessidades identificadas ao longo do desenvolvimento.
challenge: |-
  Manter a consistência dos componentes entre diferentes projetos que compartilhavam o mesmo Design System se tornou um desafio à medida que as aplicações evoluíam. Para solucionar esse problema, desenvolvi uma **biblioteca compartilhada de componentes**, posteriormente utilizada em mais dois produtos distintos.

  Também enfrentei desafios relacionados à **experiência de navegação e responsividade**, incluindo a reformulação de parte do layout e a definição de uma nova abordagem para o sidebar, baseada em referências de produtos de terceiros com navegação hierárquica em diferentes níveis.

  No aspecto técnico, investiguei um comportamento identificado apenas em produção que provocava a remontagem de componentes compartilhados durante a navegação e a execução indevida de animações. A solução envolveu o **gerenciamento manual do estado das animações**, garantindo maior controle sobre quando elas deveriam ser executadas.

  Além disso, trabalhei na **otimização da comunicação com a API**, identificando requisições redundantes e consolidando queries GraphQL em chamadas mais abrangentes durante o carregamento das páginas.
result: |-
  O produto evoluiu para uma aplicação **moderna, responsiva e visualmente consistente**, com uma experiência de navegação fluida e interações que reforçavam os fluxos e o feedback visual durante a utilização.

  A evolução do Design System e das interfaces também contribuiu para consolidar uma **identidade visual própria para o produto**, estabelecendo padrões de componentes, elementos visuais e comportamentos que tornaram a experiência mais coesa e reconhecível ao longo da aplicação.
company: "[[content/experience/escallo/index.md|Escallo]]"
expertise_area: Frontend
url:
start: 2025-03-01
end: 2026-02-01
cover:
carrousel:
stack:
  - "[[content/technology/typescript/index|TypeScript]]"
  - "[[content/technology/nextjs/index|Next.js]]"
  - "[[content/technology/tailwindcss/index|Tailwind CSS]]"
  - "[[content/technology/material-ui/index|Material UI]]"
  - "[[content/technology/zustand/index|Zustand]]"
  - "[[content/technology/zod/index|Zod]]"
  - "[[content/technology/docker/index|Docker]]"
  - "[[content/technology/figma/index|Figma]]"
  - "[[content/technology/graphql/index|GraphQL]]"
---
