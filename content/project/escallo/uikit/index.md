---
aliases:
  - UIKit
description: |-
  Biblioteca de componentes desenvolvida para padronização de interfaces, redução de inconsistências visuais entre aplicações e diminuição da dependência de bibliotecas externas, garantindo maior escalabilidade, manutenção e alinhamento ao Design System da empresa.

  Atuei na implementação, manutenção e evolução da biblioteca, desenvolvendo componentes reutilizáveis e escaláveis, desde elementos básicos, como botões e checkboxes, até componentes mais complexos, como picklists/transfers e inputs com máscaras dinâmicas (CPF, CNPJ, telefone, entre outros).

  Contribuí para melhorar a consistência visual entre produtos, acelerar o desenvolvimento das aplicações e aumentar a reutilização de código entre diferentes projetos da empresa.
excerpt: Biblioteca de componentes reutilizáveis e escaláveis para padronização de interfaces e alinhamento ao Design System da empresa.
objective: |-
  Criar uma **biblioteca compartilhada de componentes** para centralizar elementos do Design System utilizados por diferentes aplicações, reduzindo duplicação de código e facilitando a manutenção, evolução e reutilização dos componentes entre projetos.

  A iniciativa surgiu a partir da necessidade de manter dois projetos desenvolvidos simultaneamente e que compartilhavam o mesmo Design System. A centralização permitiu transformar componentes que antes eram mantidos separadamente em uma **solução reutilizável para diferentes aplicações e novos projetos da empresa**.
what_i_built: |-
  Identifiquei a necessidade de centralizar os componentes compartilhados e **tomei a iniciativa de criar a biblioteca**, sendo responsável por sua implementação, evolução e manutenção.

  Desenvolvi componentes reutilizáveis para diferentes necessidades dos projetos, desde elementos básicos, como **botões e checkboxes**, até componentes mais complexos, como **Picklists/Transfers** e inputs com **máscaras dinâmicas** para formatos como CPF, CNPJ e telefone.

  Também fui responsável pela **documentação da API dos componentes**, descrevendo suas propriedades, comportamentos e formas de utilização para facilitar a adoção e manutenção da biblioteca pelos projetos consumidores.

  Além da implementação funcional, trabalhei na definição de **transições, animações e microinterações dos componentes**, buscando criar comportamentos visualmente atrativos e uma identidade própria para a biblioteca. Também realizei otimizações nessas animações para equilibrar a qualidade visual com o desempenho da interface.

  Outro foco importante foi a **experiência em dispositivos móveis**. Adaptei componentes e comportamentos para diferentes tamanhos de tela, buscando aproximar a experiência de uso da familiaridade encontrada em aplicações nativas. Entre os comportamentos implementados, estavam padrões como **modais, popups e dropdowns que, em telas menores, assumiam comportamentos semelhantes a gavetas que surgem a partir da parte inferior da tela**, além de outras adaptações específicas para interação por toque.

  Também trabalhei na estrutura necessária para **empacotamento e distribuição privada da biblioteca**, permitindo que ela fosse consumida pelos diferentes projetos da empresa.
challenge: |-
  Um dos principais desafios foi definir uma forma de **distribuir a biblioteca de maneira privada**. Como os componentes faziam parte de soluções internas da empresa, não seria adequado disponibilizá-los publicamente. Foi necessário pesquisar alternativas gratuitas disponíveis no mercado e avaliar diferentes possibilidades até definir o **GitLab Registry** como solução para armazenamento e distribuição privada dos pacotes.

  Outro desafio foi compreender todo o processo necessário para **criar e empacotar uma biblioteca de componentes**, incluindo a escolha de uma solução de bundling adequada. Como ainda não possuía experiência nesse tipo de arquitetura, precisei estudar as alternativas disponíveis, considerando principalmente soluções amplamente utilizadas e com menor curva de aprendizado, de forma a implementar a biblioteca com agilidade.

  Também enfrentei desafios relacionados à **disponibilização da biblioteca nos ambientes de produção**. Como os projetos consumidores eram executados em diferentes VPS e utilizavam Docker, foi necessário encontrar uma forma de fazer com que a biblioteca privada fosse obtida **durante a etapa de instalação das dependências da aplicação**, permitindo que o pacote estivesse disponível corretamente durante a construção do ambiente de produção.

  Esse processo exigiu um estudo mais aprofundado sobre o fluxo de instalação de dependências em aplicações executadas com Docker e sobre a forma adequada de autenticar e disponibilizar um pacote privado durante esse processo.

  Outro desafio foi **otimizar a biblioteca para que o bundle final fosse o menor possível**, analisando sua estrutura e o processo de empacotamento para reduzir conteúdo desnecessário e tornar a instalação e atualização da biblioteca mais eficientes.

  Também houve desafios relacionados à criação de **animações e transições consistentes e performáticas**. Foi necessário considerar duração, comportamento, fluidez e impacto no desempenho para que as microinterações tornassem os componentes mais atrativos sem prejudicar a experiência de uso.

  No contexto mobile, o desafio foi adaptar componentes originalmente pensados para interfaces web tradicionais para que apresentassem **comportamentos mais naturais em telas menores e interações por toque**. Isso envolveu repensar a forma como elementos como modais, dropdowns e popups eram apresentados e interagiam com o usuário, buscando uma experiência mais próxima dos padrões aos quais usuários de dispositivos móveis já estão habituados.

  Todos esses desafios precisaram ser resolvidos em um contexto de **alta demanda no início do projeto**, exigindo agilidade na pesquisa, tomada de decisões e implementação, sem perder de vista a necessidade de criar uma solução reutilizável e sustentável.
result: |-
  A criação da biblioteca centralizou os componentes compartilhados em uma **única base de código**, eliminando a necessidade de manter implementações duplicadas entre diferentes aplicações.

  A biblioteca passou a contar com uma estrutura de **distribuição privada**, permitindo que os projetos consumidores utilizassem os componentes sem expor os pacotes ou o código-fonte publicamente.

  A documentação da API estabeleceu uma referência para **propriedades, comportamentos e formas de utilização dos componentes**, facilitando seu consumo e manutenção.

  A definição de **animações, transições e microinterações próprias** contribuiu para criar uma identidade visual e comportamental mais consistente para os componentes, tornando as interfaces mais atrativas sem abrir mão da preocupação com desempenho.

  As adaptações para dispositivos móveis proporcionaram uma experiência mais adequada a **interações por toque e telas menores**, incorporando padrões de comportamento que tornavam componentes como modais, dropdowns e popups mais naturais nesse contexto.

  As otimizações realizadas no processo de empacotamento também reduziram o **tamanho final da biblioteca**, tornando sua instalação e atualização mais eficientes nos projetos consumidores.

  Como resultado, a biblioteca se tornou uma **solução reutilizável para diferentes projetos da empresa**, proporcionando maior consistência visual e comportamental entre aplicações, reduzindo duplicação de código e centralizando a evolução dos componentes.
company: "[[content/experience/escallo/index.md|Escallo]]"
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
  - "[[content/technology/typescript/index|TypeScript]]"
  - "[[content/technology/react/index|React]]"
  - "[[content/technology/storybook/index|Storybook]]"
  - "[[content/technology/css-modules/index|CSS Modules]]"
  - "[[content/technology/rollup/index|Rollup]]"
  - "[[content/technology/framer-motion/index|Framer Motion]]"
team:
  - "[[content/team-member/antonio-mascarenhas/index|Antônio Mascarenhas]]"
team_roles:
  - Creator & Developer
---
