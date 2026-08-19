---
# qou-de9n
title: Add reference for 9705010v1.pdf at prop:mi-sw-abelianisation
status: todo
type: task
created_at: 2026-08-08T23:36:16Z
updated_at: 2026-08-08T23:36:16Z
---

The folio asserts an SW abelianisation, uses lambda_SW as a primitive, and cites only a physics paper; the mathematical account it is invoking has no ref() entry.

**From the source**
- Sect. 2 (Seiberg-Witten Differentials) — A Seiberg-Witten differential is a meromorphic 1-form lambda on the family, characterised by the property that its periods furnish the special local coordinates on the base.
  Use here: Gives lambda_SW a mathematical definition, which prop:sw-period-residue-sum and prop:mi-sw-abelianisation use as a primitive with only seiberg1994 behind it.
- Sect. 3 (Meromorphic Higgs bundles / The spectral curves) — The integrable system is the Jacobian fibration of a family of spectral curves of meromorphic Higgs bundles, with the SW differential induced from the tautological action 1-form.
  Use here: This is the classical abelianisation mechanism -- nonabelian Higgs field to a line bundle on the spectral cover -- i.e. the content an instance of the corpus's MISWAbelianisation class would have to exhibit. Explicitly NOT proposed as aid-proof: the corpus's object is a Yekutieli SURFACE-ordered multiplicative integral over an exceptional divisor with a jet filtration, and none of the spectral-curve hypotheses (a curve, a meromorphic Higgs bundle on it, a spectral cover) has been established there.

Source: `library/arxiv-alg-geom-9705010v1/9705010v1.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
