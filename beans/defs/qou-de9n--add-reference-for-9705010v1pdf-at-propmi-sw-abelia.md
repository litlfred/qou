---
# qou-de9n
title: Add reference for 9705010v1.pdf at prop:mi-sw-abelianisation
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:36:16Z
updated_at: 2026-08-21T17:03:30Z
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

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/arxiv-alg-geom-9705010v1/  ->  [donagi1997]
  Seiberg-Witten Integrable Systems

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
