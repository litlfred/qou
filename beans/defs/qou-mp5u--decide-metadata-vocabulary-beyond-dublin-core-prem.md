---
# qou-mp5u
title: 'DECIDE: metadata vocabulary beyond Dublin Core (PREMIS fixity, CSVW tabular)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-09-15T21:51:48Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-n4r9
---

## The method is already decided in the corpus — read it before proposing one (2026-09-15)

I first answered this from memory, proposing "DC for description + PREMIS for
fixity + CSVW for tabular + a small folio: namespace". That framing is wrong in
an instructive way: it presents as a NEW proposal something the project already
does, and it skips the house rule that governs how a term gets added.

`folio-assistant/schemas/jsonld.ts`, `CONTENT_CONTEXT`, already composes SIX
vocabularies — `folio`, `doco`, `deo`, `cito`, `oa`, `prov`, `skos`, `dcterms`,
`fhir`. So "compose several vocabularies" is not a decision to take; it is the
established shape. What is open is only WHICH TERMS.

And the rule for that is written into the file, in its own words, at the
`contains` mapping:

> `contains` maps to `dcterms:hasPart` rather than DoCO's own containment
> property. DoCO does not define one: it imports `po:contains` from the Pattern
> Ontology, which is documented as a sub-property of `dcterms:hasPart`. The
> Pattern Ontology namespace could not be verified from this sandbox
> (`sparontologies.github.io` is egress-blocked), and a published context is
> the wrong place to guess an IRI — so this uses the verified super-property.
> **Generalising is sound; inventing is not.** Narrow it to `po:contains` once
> the namespace can be checked.

A second instance, same rule: there is no `certainty` term yet, because "the
exact predicate wants checking against a real IG rather than guessed", deferred
to the writer that first emits one.

### What that means for this bean

1. **Do not write PREMIS or CSVW IRIs into the context from memory.** That is
   precisely what the `contains` note refuses. The pattern is: use a verified
   broader term now, record the narrower one to adopt later, and say why.
2. **`folio:` is the sanctioned escape hatch** when no vocabulary models the
   thing — already used for `uses`, `interprets`, `foreshadows`, `provenance`,
   `pageStart`/`pageEnd`. A checksum or a sheet name can live under `folio:`
   honestly while PREMIS/CSVW remain unverifiable, and that is a smaller lie
   than a guessed external IRI.
3. **The egress constraint is not new.** Measured again 2026-09-15:
   `dublincore.org` and `w3.org` are blocked (000); `raw.githubusercontent.com`
   IS reachable (200 on `dcmi/dctap`) — an earlier session-note of mine that
   raw.githubusercontent was blocked was wrong, it was a 404 on a mistyped path.
   So a future session CAN verify a term given a known raw URL; it cannot find
   one by browsing, and `github.com/dcmi/dcmi-terms` and `dcmi/vocabularies` do
   not exist under those names.

### Still open, and still not to be guessed

Which specific IRIs carry: a checksum, a row/column structure, a sheet name, a
transcript-to-audio relation, and a localized description's provenance. The
`dcterms:description` half is safe — it is already in the context and JSON-LD
language tags handle localization natively.

**This bean stays open.** Recording the method is not deciding the terms.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Not started. This story is owner-gated (AGENTS.md 'ask the owner before changing things') and needs work in a platform repo as well as qou, so it was not started in the wave-1 drain.
