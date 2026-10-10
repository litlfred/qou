---
# qou-mnho
title: 'INGEST: localized narrative description for images, including images extracted from PDFs'
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-15T21:51:46Z
updated_at: 2026-10-04T15:20:54Z
---

## Every narrative description names its author, human or agentic (owner, 2026-09-15)

A generated description is a CLAIM about the asset, and a reader has to be able
to tell who made it. So each one carries its provenance inline, not in a
changelog:

- **agent** — the model identifier AND its version, plus the prompt/skill that
  produced it and the date. "an LLM described this" is not attribution; two
  model versions disagree about the same image and a later reader needs to know
  which one spoke.
- **human** — the person, and the date.
- **mixed** — a machine draft a human corrected is BOTH, and says so in that
  order, because the human edit is what makes it citable.

This is not decoration: it is what separates an L1 node a content block may
cite from one it may not. Under the round-trip translation QA (`qou-9iks`) the
provenance is also what makes a mismatch diagnosable — a drift traced to a
specific model version is a finding, the same drift with no attribution is
noise.

Applies identically to a description of an image EXTRACTED FROM A PDF, which is
the case most likely to be forgotten because the PDF itself already has
authorship and the extracted figure silently inherits the appearance of it.

Vocabulary: `prov:` is already in the folio JSON-LD context
(`prov:wasDerivedFrom` is mapped), so the attribution has somewhere to live
without inventing a term. The exact predicate is part of `qou-mp5u` and is not
to be guessed — see the house rule recorded there.



## Reasons for Scrapping

Duplicate of `folio-assistant-d5f1` (platform bean in litlfred/folio-assistant) (work-plan reorganisation 2026-10-04). Evidence: [M] f-a bean folio-assistant-d5f1 "INGEST: narrative description per image, localized" (todo)
Content is untouched; only this work item is closed.
