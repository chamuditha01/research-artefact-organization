# Research Artefact Organisation Template

This repository provides a reusable folder structure that can be used to organise a
thesis or dissertation research project, from the initial idea through to the final
submission. It is intended as an organised home for everything the project produces -
documents, the artefact, ongoing progress and the final deliverables. Each top-level
folder contains its own README describing what should be placed inside it and how it
should be maintained.

## Folder structure

- `Meta/` - governing documents that define the project task (descriptor, rubric, deadlines).
- `Brainstorm/` - early-stage ideas, scope iterations and rejected directions.
- `References/` - the literature tracking sheet and stored copies of reviewed sources.
- `Templates/` - blank starter documents that can be reused for consistent formatting.
- `Administrative/` - supervision records and formal documents requiring sign-off.
- `Artefact/` - reference information about the implementation (repository links, architecture notes, dependencies), data, results and validation material. Source code lives in its own repository.
- `Dissertation_Drafts/` - idea seeds and written drafts for the thesis, proposal and presentations, through to the OneDrive-linked submission copy.

## Naming and version convention

Files should be named without spaces. Successive drafts should be versioned as `v1`,
`v2`, and so on, with the submission-ready copy marked `_FINAL`.

## Suggested workflow

The folders are intended to be used roughly in order:
Meta -> Brainstorm -> References -> Templates -> Administrative -> Artefact -> Dissertation_Drafts.

## Version control

Large, temporary and environment-specific files should not be committed; these are
excluded through `.gitignore`.
