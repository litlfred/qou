---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
section_id: sec-011-selection-of-erdős-and-oeis-problems
section_title: "Selection of Erdős and OEIS Problems"
section_number: null
pages: 26-27
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
toc_source: outline
doc_brief: "Advancing Mathematics Research with AI-Driven Formal Proof Search — 29 sections: Front matter; Introduction; AlphaProof Nexus"
---
For the Erdős evaluation, we ran our agent on all Lean statements of Erdős problems available
in the Formal Conjectures repository [23] as of early February 2026 – 353 problems in total.
We did not select which problems to attempt; the set was determined entirely by what
the open-source community had formalized from the 1200+ problems catalogued on the
ErdosProblems site. We recognize that this process has a bias toward problems amenable to
formalization in Lean.
For the OEIS evaluation, we began with a corpus of 2649 open conjectures drawn from the
OEIS [56]. We prompted Gemini to select 500 problems that are non-trivial, mathematically
interesting, not famous open problems, and good candidates for automated theorem-proving,
and used a Gemini-based agent to formalize them. Of the 500 problems, 8 were excluded
due to incompatibilities introduced by a Lean version upgrade, yielding a final set of 492
problems.
26
Advancing Mathematics Research with AI-Driven Formal Proof Search
