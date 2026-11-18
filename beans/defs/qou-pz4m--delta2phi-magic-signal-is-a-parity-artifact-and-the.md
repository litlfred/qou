---
# qou-pz4m
title: delta2-Phi magic signal is a parity artifact, and the K=10 table has no producer
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T00:00:00Z
updated_at: 2026-10-04T15:14:49Z
parent: qou-5vkl
---

Found while answering a status question on magic-shell structure. No prior bean,
no `.qa.json` finding, and no audit doc covers either defect (corpus-grepped:
`docs/audits/`, `content/`, `computations/`, coordination ledgers, `library/`,
`.beans/` — all six paths).

Concerns `prop:magic-numbers-from-q`
(`folio/quantum-observable-universe/observations/magic-numbers-from-q.md`) and
its Lean `QOU.AtomicMass.MagicNumbersFromQ`.

## Defect 1 — the sign test is parity, not magic

The one recorded run of the signal is
`computations/_deprecated/shell-closure.witness.json`
(`data.forward_delta2`, `kmax = 12`, Z = 2..31). Measured over it:

**`sign(delta2-Phi(Z)) > 0` iff `Z` is even — zero exceptions in Z = 2..31.**

Every magic number is even, so the block's headline property is satisfied by
15 of 15 even Z and by no odd Z. It carries no information about magic-number
selection. The Lean headline
`magic_numbers_from_q : forall Z in [8,20,28], delta2_Phi 10 Z q_zero > 0`
states exactly this parity-satisfied property over three even points.

Worse for the weaker **elevation** claim the `.md` retreats to: among even Z the
sequence rises to a broad maximum at **Z = 12 (56.20)** and decays monotonically
after Z = 14. The only local maxima are **Z = 4 and Z = 12 — neither magic**.
None of 8, 20, 28 is a local maximum:

    Z= 6  47.73    Z=18  38.63    Z=26   8.89
    Z= 8  48.21 M  Z=20  26.78 M  Z=28   5.91 M
    Z=10  52.00    Z=22  18.65    Z=30   3.80

8 sits mid-rise; 20 and 28 sit mid-decay. So the recorded data does not support
"elevated at the magic numbers" either — 8 is *below* the non-magic 10 and 12.

Scope **(a)**, not (b): this is a negative about the `delta2-Phi` statistic at
`kmax = 12` as recorded. No invariant is proved forbidding a magic signal from
some other Hoefsmit-derived statistic.

## Defect 2 — the published K=10 table has no producer and no witness

The `.md` table and the Lean tabulation give `(8 -> 33.2, 20 -> 20.4, 28 -> 4.4)`
at `K = 10`. Measured:

- Those three values appear **nowhere** in any `*.witness.json` or producer in
  the tree. Corpus grep for `33.2` returns only narrative `.md` and the Lean
  docstring that restates it (plus unrelated `reviewed_at` timestamps).
- The Lean names its source as `shell_closure_compute.py` /
  `shell-closure.witness.json`. **Both are in `computations/_deprecated/`**, and
  that witness is `kmax = 12`, not `K = 10`. Its values at those Z are
  **48.21 / 26.78 / 5.91**, not 33.2 / 20.4 / 4.4.

So the K=10 numbers are of unrecorded provenance — the same class as the
`kappa ~ -1.0708` provenance loss in `qou-o16k`, one block over.

## Defect 3 — `Phi_signal` is a hardcoded lookup, and the Lean is near-vacuous

`Phi_signal (K Z : ℕ) (_q : ℝ)` **discards its `q` argument** (note the
underscore) and returns a 3-entry `if`-table, 0 elsewhere. Consequences:

- `Phi_signal_at_8 (q : ℝ) : Phi_signal 10 8 q = 33.2` is proved by
  `unfold; simp` **for every real q** — including `q = 0`. The file's own
  docstring is candid that this replaced axioms with a tabulation, but the
  resulting theorems are about the table, not about `q`.
- The `.md` claim *"computed purely from the substrate parameter q_0 ... no
  empirical input"* is therefore not what the Lean checks. The Lean cannot
  distinguish q_0 from any other real.
- The off-table zeros make `delta2_Phi` equal the central value by construction,
  so the "second difference" is the table entry itself.

Candidate criteria: `proof-claims-unencoded` (docstring asserts a q-dependence
the type does not carry) and the `def`-disguised-tabulation shape. Not currently
flagged by the vacuity audit — it keys on `: True` and trivial bodies, and a
lookup table is neither.

## Third reading of the same numbers (inconsistency, lower priority)

`observations/k12-barrier-bypass.md:30` calls `+33.2, +20.4, +4.4` *"agreement
deltas between framework predictions and CODATA at {2, 8, 20}"* — a different
quantity (agreement deltas, not character second differences) at a different
Z-set ({2,8,20} vs {8,20,28}). At most one reading is right.

## Next

1. Re-run the deprecated producer at `K = 10` to establish whether 33.2/20.4/4.4
   are reproducible at all, or are lost. This is the cheap decisive step and it
   gates everything else.
2. Given defect 1, demote `prop:` -> `conj:`, or re-scope the `.md` to state the
   parity result plainly and drop the elevation claim. Do **not** re-scope on the
   `kmax = 12` data alone until step 1 fixes the truncation question.
3. The parity structure is worth a look on its own: `Phi` alternating with
   period 2 in Z is a real feature of the Hoefsmit weights and may be the
   pairing term, which *is* nuclear physics — just not magic numbers.
