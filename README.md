# portfolio-cms

Obsidian vault usado como headless CMS para o portfólio pessoal [antoniomascarenhas.com.br](https://antoniomascarenhas.com.br).

Este repositório contém apenas conteúdo em Markdown com frontmatter YAML — não há código de aplicação, build system ou test suite.

## Primeiros passos ao clonar

```bash
# 1. Instalar o pre-commit hook (valida estrutura dos arquivos antes de cada commit)
./scripts/install-hooks.sh

# 2. Verificar se PyYAML está disponível (o hook precisa para validar frontmatter)
python3 -c "import yaml; print('ok')"
# Se falhar: pip install pyyaml
```

## Estrutura

```
content/
├── index.md / index.en.md       # Perfil raiz (agregador do site)
├── about/                        # Bio
├── achievement/<entry>/          # Conquistas
├── contact/<channel>/            # Canais de contato
├── education/<entry>/            # Formação acadêmica
├── experience/<company>/         # Experiência profissional
├── project/<company>/<project>/  # Projetos
├── seniority/<level>/            # Níveis de senioridade
├── skill/<category>/             # Habilidades
└── technology/<tech>/            # Tecnologias
```

Todo entry tem dois arquivos: `index.md` (pt-BR) e `index.en.md` (en).

## Pre-commit hook

O hook valida a cada `git commit`:

- Tipos de conteúdo conhecidos
- Nomes de pastas em lowercase kebab-case
- Apenas `index.md` / `index.en.md` dentro de pastas de entry
- Bilíngue obrigatório (todo `index.md` precisa de `index.en.md`)
- Frontmatter YAML válido
- Campos obrigatórios por tipo de conteúdo (`scripts/content-schema.yaml`)
- Tipos dos campos correspondem ao esperado (`scripts/types-schema.yaml`)
- Campos obrigatórios no schema de tipos não estão vazios
- Nenhum campo não catalogado no schema de tipos
- Wikilinks apontando para arquivos que existem

Após a validação, o hook gera automaticamente o arquivo `content-types.d.ts` com as interfaces TypeScript de cada content type, que é incluído no mesmo commit.

## Schemas

- **`scripts/content-schema.yaml`** — define a estrutura esperada: tipos de conteúdo permitidos e campos obrigatórios (valida se a chave YAML existe no frontmatter).
- **`scripts/types-schema.yaml`** — define o tipo de cada campo e se ele pode ficar vazio. Serve como contrato com o frontend para geração de tipos TypeScript em `content-types.d.ts`.

Para alterar a estrutura do conteúdo, edite esses arquivos e faça commit junto com as mudanças nos arquivos de conteúdo. Qualquer campo presente no frontmatter que não esteja catalogado no `types-schema.yaml` será rejeitado.
