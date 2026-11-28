---
name: evidence-gathering-and-provenance
roles: [collaborator, owner]
description: >
  Mandatory evidence-gathering, multi-database literature/data retrieval,
  Knowledge Graph ingestion, relevancy assessment, and authoring provenance
  workflow for QOU research and authoring agents (owner directive 2026-11-28).
  Use whenever researching an open mathematical or physical topic, surveying
  prior art, or authoring/updating content blocks grounded in external papers
  or reference datasets.
allowed-tools: Read Write Edit Bash Grep Glob Agent WebFetch
---

# Evidence Gathering, Multi-Database KG Ingestion & Authoring Provenance

Governing BPMN process: [`processes/content/evidence-gathering-and-provenance.bpmn`](../../../processes/content/evidence-gathering-and-provenance.bpmn).

Owner directive (`2026-11-28`, verbatim):
> *"research agents need to also use evidence gathering skills and process (may need to add this / update this in KG) when researching a topic... write up topic areas of research, for each, develop a short list of papers, data etc needed, retrieve and ingest into KG, assess for relevancy. also make use of other databases that agent or user may have access to google scholar, DOI, arxiv, pubmed, etc... this should be a part of document authoring. provenance of paper recorded as part of notes in authoring process and linked in paper as relevant"*

## 1. Scope Topic Areas & Build an Evidence Shortlist First

Before launching long symbolic derivations, Lean formalizations, or numerical probes on a research question:

1. **Write up the distinct topic areas** touched by the question (e.g., Iwahori–Hecke / Temperley–Lieb character formulas, Gröbner–Shirshov confluence for Coxeter/braid algebras, knot hyperbolic volume & Habiro cyclotomic expansions, interior-point SDP duality, nuclear/particle reference datasets).
2. **Check what QOU already holds** across the corpus-grep paths (`folio/references/`, `library/*/structure.json` + `library/*/sections/*.md`, `test/attestations/bib-verification/`, `beans/defs/`, `docs/audits/`).
3. **Develop a targeted shortlist of missing papers and datasets** per topic area (exact theorem/lemma needed, candidate authors/venues, or empirical constant table needed at the comparison boundary).

## 2. Query Multiple Bibliographic & Scientific Databases

Use every bibliographic, preprint, and reference database available to the agent or user (via MCP tools, APIs, CLI scripts, or user-assisted retrieval when behind authentication/anti-bot gates):

| Database / Registry | Primary Use in QOU |
|---|---|
| **Crossref / DOI (`doi.org`)** | Authoritative CSL-JSON bibliographic metadata, journal/volume/page verification, exact DOI resolution. |
| **arXiv** | Mathematics (`math.QA`, `math.GT`, `math.RT`, `math.OA`) and physics (`hep-th`, `nucl-th`, `math-ph`) preprints + LaTeX source bundles. |
| **INSPIRE-HEP** | High-energy, nuclear, and mathematical-physics citation graphs, PDG cross-links, and exact preprint-to-published joins. |
| **Semantic Scholar / OpenAlex / Google Scholar** | Forward/backward citation traversal, theorem-statement discovery across adjacent subfields, and interdisciplinary literature search. |
| **PubMed / PMC** | Biophysics, molecular/chemical spectroscopy, radiobiology, and WHO/clinical reference literature where applicable. |
| **CODATA / PDG / AME2020** | Authoritative experimental comparison-boundary datasets (`library/` reference datasets & `computations/codata_constants.py` — never inline raw magic numbers). |

*Boundary rule:* Never bypass CAPTCHAs, paywalls, or anti-bot gates; if a shortlisted source is gated, record the exact DOI/citation and ask the user via a structured card (`AskUserQuestion`, `🟡` + chat mirror) whether they wish to drop the PDF into `uploads/`.

## 3. Ingest Retrieved Papers & Datasets into QOU's Knowledge Graph

Retrieved sources MUST enter the Knowledge Graph rather than remaining ephemeral chat links or scratch notes:

1. **Bibliography node (`references` KG):**
   - Create `folio/references/<key>.json` (`folio-reference/v1` CSL-JSON) and register `<key>` in `folio/schema/references.ts` (`ORDER`), then regenerate/check `references.bib` (`bun run scripts/check-references-bib.ts`; see [`bib-qa.md`](bib-qa.md)).
2. **Full-text / dataset intake (`library` KG):**
   - Place raw PDFs/sources in `uploads/` and ingest into `library/<doc-id>/` (`structure.json`, `sections/*.md`, `candidates.json`) via [`document-intake.md`](document-intake.md), then sync `library` blocks in `folio/references/<key>.json` (`python3 scripts/sync-references-library.py --check`).
3. **Source-ledger attestation (`attestations` KG):**
   - Record the join and examination state in `test/attestations/bib-verification/<key>.json` (`source-ledger/v1`, read/written through `cat-harness/schemas/bib-attestations.ts`).

## 4. Assess Relevancy & Exact Claim Scope

Run [`paper-relevance-triage.md`](paper-relevance-triage.md) on every newly ingested source:

- Assign an explicit relevance verdict (`core`, `supporting`, `tangential`, `not-relevant`, or `undetermined` with reason).
- Separate **`claim_domain: "math"`** (deductive theorems/definitions reusable in QOU's mathematical model or `folio/unital-groebner-bases/`) from **`claim_domain: "science"`** (empirical measurements that enter *only* at QOU's comparison boundary).
- Verify **`evidence_location: "in-paper"` vs `"elsewhere"`**: cite the paper that actually proves the theorem or measures the datum, never a secondary survey that merely quotes it without proof.

## 5. Record Provenance in Authoring Notes & Link in the Paper

Literature and data provenance is an integral part of document authoring:

1. **Authoring-process provenance notes (`authorNotes` in `<block>.ts`):**
   - Record in the block's `authorNotes` array (`{ id, author: "claude", date, kind: "note", body }`) which shortlisted source(s) supplied the background construction, comparison datum, or proof technique, naming exact theorem/equation/page numbers and how QOU's hypotheses map onto the source's conventions.
2. **Formal & prose links (`cites`, markdown citations, Lean `-- Ref:`):**
   - Declare every cited key in the block manifest's `cites: ["<key>", ...]` array.
   - Cite it in `<block>.md` prose (`\cite{<key>}` / `[<key>](#cite:<key>)`) at the exact sentence or comparison point where it bears, respecting [`one-voice-style-guide.md`](one-voice-style-guide.md) and [`md-authoring.md`](md-authoring.md).
   - Where a Lean declaration or temporary `sorry` relies on a classical mathematical theorem pending formalization in `QOU/MathlibExt/`, cite `-- Ref: [<key>] Theorem X.Y, p. Z` in the `.lean` docstring.
