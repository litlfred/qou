---
# qou-zx95
title: 'CITE: bichon2003 / etingof-ostrik2004 metadata is still UNVERIFIED — M — egress 403 again 2026-09-04; consumed by FibreFunctorDimensionNotCategorical'
status: todo
type: task
priority: normal
created_at: 2026-09-04T09:07:37Z
updated_at: 2026-09-04T09:07:37Z
parent: qou-8lxd
---

**Class M — two entries added on 2026-09-03 with their metadata explicitly marked
unverified; egress is still 403, so they are still unverified.**

`references.ts:8137` (`bichon2003`) and `:8150` (`etingof-ostrik2004`) both carry,
verbatim in their own `note`:

> *"NO DOI RECORDED and volume/issue/pages NOT verified against the publisher
> record: doi.org and arxiv.org are blocked by the sandbox egress proxy in this
> session … Verify before citing in print."*

**Re-attempted 2026-09-04 and it failed the same way.** `curl` to
`api.crossref.org` and `export.arxiv.org` both return
`CONNECT tunnel failed, response 403`; the proxy status endpoint confirms
`connect_rejected — gateway answered 403 to CONNECT (policy denial)` for
`api.crossref.org`. **So this bean records that the gap is unchanged, not that it
was re-checked and found wrong.**

**Neither entry appears in `content/bib-qa-verifications.json`** (442 entries) — so
there is no ledger row either, and nothing will flag them.

**What is claimed, and needs checking:**

- **Bichon, Julien**, *The representation category of the quantum group of a
  non-degenerate bilinear form*, Communications in Algebra **31** (2003) issue 10,
  pp. 4831–4851. arXiv preprint given as `math/0207256`. No DOI.
- **Etingof, Pavel & Ostrik, Viktor**, *Module categories over representations of
  `SL_q(2)` and graphs*, Mathematical Research Letters **11** (2004) issue 1,
  pp. 103–114. arXiv preprint given as `math/0302130`. No DOI.

**Where they bite.** Both are consumed by the eightfold front-2 result that a fibre
functor changes dimensions but not fusion rules —
`lean/QOU/Eightfold/FibreFunctorDimensionNotCategorical.lean` and
`computations/.../fibre_functor_dimension_not_categorical_probe.py`. That is an
*asserted* structural claim resting on a classification result, so the citation is
load-bearing, not decorative.

**Neither is held**: no `library:` block, and `library/INDEX.md` has no row for
either (`Bichon` 0; the three `Etingof` rows are Etingof–Nikshych–Ostrik on fusion
categories and the quantum Kazhdan–Lusztig functor — **different papers**, do not
substitute).

**Fix, when egress allows** (or from a machine that has it): confirm
volume/issue/pages, add DOIs (`10.1081/AGB-120022455` is the plausible Comm. Alg.
DOI shape — *unverified, do not paste it in without checking*), add a
`bib-qa-verifications.json` row, and ingest the two arXiv preprints so the
classification statements are greppable.

Found by the citation-gap sweep, `docs/audits/2026-09-04-citation-gap-inventory.md`.
