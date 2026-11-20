---
# qou-m0bv
title: 'GAP: 4 particle-existence blocks prove a degenerate witness (zero-mass proton, two-unknot hadron)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T19:26:21Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-wp3h
---


Full analysis:
[`docs/audits/2026-08-08-narrative-lean-equivalence-nonempty-kernels.md`](docs/audits/2026-08-08-narrative-lean-equivalence-nonempty-kernels.md).

## The four

| block | witness actually proved |
|---|---|
| `predicted-spectra/categorical-proton-exists` | zero-mass degenerate proton |
| `predicted-spectra/categorical-neutron-exists` | zero-mass degenerate neutron |
| `knots-particles-confinement/hadron-exists` | a "hadron" made of two unknots |
| `lifting-and-descent/quantum-characteristic-classes-exists` | zero obstruction class over ℤ |

Every one is honestly commented ("Trivial witness…", "The intended … witness
is sharper but requires the Hecke NF reduction infrastructure"). The defect is
that a degenerate witness sits under a headline theorem name —
`CategoricalProton.exists` reads as "the categorical proton exists".

## Why a better witness is not the fix

`CategoricalProton` has four fields (`skein_uu`, `skein_ud`, `mass`,
`chirality`) and **no properties**. The Lean docstring claims the witness has
"negative crossing energy and Frobenius stability"; the `.md` claims an
element of $H_3(q)$ with Frobenius stability $G x[\gamma] \ge 0$. The
structure has no field for any of it, so those claims are **unstatable**, not
merely unproved.

So the order is:

1. Give the structures fields carrying their defining properties (crossing
   energy, Frobenius stability, the Borromean B₃ relation).
2. *Then* the existence theorem is a real obligation, and the intended
   Borromean witness discharges it.

Step 1 is the formalisation project. Both steps need the Hecke NF reduction
infrastructure the comments already name, so this is correctly **blocked**,
not merely undone.

## Do not delete the theorems

For what the statements currently say, the proofs are correct. Deleting them
would misrepresent trivial statements as open conjectures — the mirror of the
defect fixed in #4797. Same rule as `qou-g4x1`.

## Follow-up pass (2026-08-08, same day) — the narrative side

The pass above compared each proof term to the **Lean docstring** above it,
not to the `.md` sibling. Reading the four `.md` files changed two things:

- **`quantum-characteristic-classes-exists` is Class A + Class B.** Its `.md`
  asserts existence *for every $n \ge 0$*; the Lean is `Nonempty` at a single
  level. Restoring the quantifier is statable (`level : ℕ` exists) and one
  line, and was **deliberately not done** — every such class has `κ = 0`, so a
  `∀ n` over them is equally vacuous and would only make the theorem read as
  stronger.
- **`hadron-exists` is the sharper worked case**, not the proton: its `.md`
  asserts $\mathfrak{E}_{\mathrm{cross}} < 0$ flatly, with no hedge, while
  `Hadron` has no energy field at all.

**Unblocked repair applied:** all four `.ts` manifests now carry an §4d
`authorNotes` caveat naming the degenerate witness and the blocker. The Lean
itself remains correctly blocked.

## Detector note

This class is invisible to every existing audit — no `sorry`, no `True`, no
unsound quantifier, and the statements are *true*. Found by scanning for
kernels whose entire content is `Nonempty X`, then asking whether `X` is
substantive. Triage rules that make the signal usable (376 raw hits → 14 real,
4 findings): strip comments first, exclude `.lake` and `have`/`haveI`/`letI`,
and treat `Nonempty` fields *inside content-bearing structures*
(`fibre_nonempty`, `exceptional_nonempty`, …) as legitimate non-degeneracy
side-conditions rather than findings.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.

## Progress Update (Round 90 — lane-cf11)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/BipartitionTransseriesAndCubicDimensionKernelBrick.lean` with 80-dps probe `computations/probes/bipartition_transseries_and_cubic_dimension_kernel_brick_probe.py` and witness `computations/probes/bipartition-transseries-and-cubic-dimension-kernel-brick.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8339 (`feat/qou-b9cj-m0bv-m6gp-mbz4-mdbh-mssy`, HEAD `8369032c8c6c736ecfb79467000a84fa918a7d04`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8339, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
