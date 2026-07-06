# Bond-dimension verdict — the p(3A) wall is intrinsic; heavy nuclei stay on the A→∞ extrapolation (2026-06-16)

**Branch:** `claude/atom-braid-bond-dimension-program-2026-06-16` (PR #2389)
**Resolves:** direction 1 (the decisive gate) of the
[atom-braid program workplan](../workplans/2026-06-16-atom-braid-bond-dimension-program.md).
**Verdict: NEGATIVE.** No basis change / symmetry breaks the `p(3A)` wall for *exact*
`tr_M`. The fine-Bratteli transfer is already the minimal-bond-dimension exact
method. **Formalize-first win:** an 11-second measurement closes a multi-week
MPS-building program before it started.

## The measurement

The atom braid's Markov trace `tr_M = Σ_{λ⊢3A} y_λ χ^λ` is a 1-D transfer
contraction; the effective bond dimension at strand-cut `k` is
`χ_eff(k) = #{λ⊢3k : amplitude ≠ 0}`. The hypothesis was that the atom's
non-genericity populates `≪ p(3k)` partitions. It does not:

**Structural** (`chi_atom_transfer.bratteli_state_sizes`, pure combinatorics):

| k (nucleons) | n=3k | p(3k) | #partitions reached | full? |
|---|---|---|---|---|
| 2 | 6 | 11 | 11 | YES |
| 3 | 9 | 30 | 30 | YES |
| 4 | 12 | 77 | 77 | YES |
| 5 | 15 | 176 | 176 | YES |
| 6 | 18 | 385 | 385 | YES |
| 7 | 21 | 792 | 792 | YES |
| 8 | 24 | 1575 | 1575 | YES |

**Numerical** (`chi_monotone_transfer.chi_all_lambda` at 40 dps — nonzero χ^λ):
D `11/11`, ³He `30/30`, ⁴He `77/77`. No accidental zeros.

**`χ_eff(k) = p(3k)` exactly**, structurally and numerically. The A-fold fusion of
H₃ reaches every partition of 3k, and at generic q₀ every amplitude is nonzero.

## Why every direction fails to break the wall

- **#1 restricted-support MPS — DEAD.** The support *is* the full `p(3k)`; there is
  nothing to restrict. The partition basis is already minimal.
- **#4 R-matrix MPS — DEAD.** The alternative bases are strictly worse: the full
  Bratteli-path count is super-exponential (`Σ running-multiplicity` = 3 → 36 → 814
  → 28 814 → 1.4M → 90M → 7.2B → 702B for k=1…8), and the colour/TL link-state basis
  is `~Catalan(n) ~ 4ⁿ`. The transfer already sums the 702B paths down to the 1575
  partition labels — that *is* the optimal collapse.
- **#2 S_Z×S_N symmetry — no scaling win.** The reached partitions are intrinsic
  irrep *labels*, not permutation-foldable; nucleon symmetry only reduces the
  *multiplicity* bookkeeping, which the transfer already sums to the label count.
  Constant factor at best.
- **#3 interface sparsity — survives, but only a constant factor.** `σ_i` is
  block-(1×1/2×2) in seminormal form, so the per-step transfer can be carried sparse
  — shaves the constant in front of `p(3A)`, does not change the scaling.

## Consequence

Exact `tr_M` is intrinsically bounded by `p(3A)` (the number of Wedderburn sectors),
and the production fine-Bratteli transfer already achieves it: ⁴He 0.09 s, ¹²C
~5.5 min, ¹⁶O (`p(48)=147 273`) ~hours — the practical ceiling. There is **no exact
route to the heavy-nuclei regime**; this is not a missing optimization but an
intrinsic property of the Jones–Markov trace at large strand count.

**This vindicates #2349's design choice:** heavy nuclei (beyond ~¹²C) are handled by
the **A→∞ colour-weighted q-CLT / magic-volume extrapolation**, not exact `tr_M`.
That was the right call, now confirmed from first principles rather than assumed.

## What remains worth doing

- **#3 sparsity** (optional, modest): carry the transfer operators sparse for a
  constant-factor speedup on the ⁸Be–¹²C range. Independent of this verdict.
- **Nothing else** in this program — the wall is intrinsic. Effort is better spent on
  the q-CLT extrapolation accuracy (the actual heavy-nuclei path) and the verified
  low-A operator-form correctness (#2365), not on chasing exact ¹⁶O.

## Discipline

Pure measurement; no production change, no truncation. The negative result is the
deliverable — it redirects effort away from a doomed exact-¹⁶O build and onto the
A→∞ extrapolation that #2349 already uses.
