---
# qou-hzhi
title: 'Session: QCD-comparison structural gaps — three variances, five collisions, general ansatz-content theorem'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T05:11:09Z
updated_at: 2026-10-04T15:11:31Z
---

## Session outcome 2026-09-13 — merged as `3cb26d4b9f8` (PR #7255)

Started from a question about whether the framework speaks to the ALICE
incoherent-J/ψ result. **It does not**, and the interesting part is *why*, which
turned into statements about the framework's own predictive reach — testable with
no reference to ALICE at all.

| child bean | state | what landed |
|---|---|---|
| `qou-w9up` | **completed** | `AnsatzContentDichotomy.lean` — the size-free general form; "empty" and "vacuous" are ONE failure mode |
| `qou-r44k` | **completed** | six QCD name-collisions in the notation register |
| `qou-2ss0` | in-progress | `B3AggSecantCharacterisation` + `InterfaceMonotoneBlocksSignMixed`; open per §13a |
| `qou-c6s9` | in-progress | three distinct second-moment structures — open |
| `qou-jogb` | todo | Gap 1 re-scoped to a POINTER; the charge radius is NOT gated on the ALICE gap |
| `qou-plb2` | todo | `lean-build-bg.sh` anti-eviction guard is inert on a trace-paired restore |
| `qou-md01` | todo | **new** — the merge endpoint 500s deterministically on merge-commit-carrying branches |

Also: 22 queued PDFs ingested from `uploads/` into `library/` so corpus-grep
**path 5** can see them — it searches `library/` only, so a PDF in `uploads/` is
invisible to every "has the corpus got this?" check. Two clusters the upload
turned out to contain: **cluster-expansion / virial** (Fernández–Procacci, Tate,
both carrying *Groeneveld* and *Ursell* — landing directly on the open
`b₃ = −φᵀ₃` front) and **KLR / quiver-Hecke** (AGENTS.md §7b territory).

## Four claims of mine were WRONG, and they share one root cause

Recorded because the pattern is more reusable than any of the four:

1. *"QOU has no ensemble."* It does — `non-commutative-probability-dictionary`
   states Wedderburn idempotents are events and `w_λ(q) = tr_M(e_λ)` assigns
   probability mass; plus the q-CLT, `κ₂^(q)`, and 26 covariance-epic witnesses.
2. *"Gap 1 is a blank."* The greps were true (`impact parameter` 0,
   `transverse plane` 0) and the inference was false — `qou-usft` already derives
   a radius from the binding length `1/κ = ℏc/√(2μ S_sep)`.
3. *"Groeneveld is not in `library/`."* Asserted **twice**. I ran tier 1
   (`INDEX.md`) only. The better diagnosis came from the ingesting agent, not
   me: INDEX.md is one line per *document*, so a body-text term can **never**
   appear there — structural, not staleness. `sections/` holds Groeneveld 2,
   Ursell 6, Mayer 39, Ruelle 12, and `UrsellPartitionFunctionB3.lean:73`
   **already cited Jansen–Kolesnikov by DOI**.
4. *"Four of five uploads are heavy-ion/DIS."* Judged 22 papers from the 5 that
   had title metadata.

**Same root cause every time: generalising from the subset the tool could see.**

Also corrected: commit `8522f4af2` contains 22 PDF renames its message never
mentions — `git add <paths>` followed by a **bare** `git commit` commits the
whole index, and a concurrent agent had staged 409 files into it. The safe form
is `git commit -F- -- <paths>`.



## Summary of Changes

Session log closed 2026-10-04 (owner decision 2): open children were reparented to programme epics and prose follow-ups extracted as their own beans. Kept as a record, not deleted.
