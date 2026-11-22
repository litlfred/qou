# PREREG — is Gresnigt's Clifford braid representation a Hecke representation?

Issue #9096. Branch `claude/helon-battery-chirality-2026-11-22`. Written and committed
**before** any computation in this directory.

## Source (what is actually held)

The task names `arxiv-1711.09011v1`. **It is not in `library/`** (measured: no
`library/*1711.09011*` directory, no `1711.09011` string in any `library/*/sections`).
The same representations are stated in a held paper by the same author:

- `library/arxiv-1901.01312v1` — Gresnigt, *Braided fermions from Hurwitz algebras*.
  - §4.2 (pp. 4–5, `sec-008-...`): Kauffman–Lomonaco Clifford braiding. In `Cl(n,0)`
    with `e_k² = 1`, anticommuting, `σ_k = (1 + e_{k+1} e_k)/√2` (1 ≤ k < n) and
    `σ_n = (1 + e_1 e_n)/√2` represent the circular braid group `B_n^c`. Stated also for
    `e_k² = −1`.
  - §4.3 (pp. 5–6, `sec-009-...`): complex rep of `B_2`, `σ_1 = (1+i)/√2`, order 8;
    quaternion rep of `B_3^c`, `σ_1 = (1+I)/√2, σ_2 = (1+J)/√2, σ_3 = (1+K)/√2`.

Whether 1901.01312 or one of its refs [19]/[20] is the arXiv number the task names is
**not asserted here**; the matrices tested are the ones in 1901.01312 §4.2–4.3.

## Conventions (repo)

Hecke: `(T − q)(T + q⁻¹) = 0`, i.e. `T² = (q − q⁻¹)T + 1`. Our `q` is formal. A point
`q = ζ₈` below is **fixed by Gresnigt's construction, not chosen by us**, and is not a
candidate for `q₀` (q₀ derivation is forbidden; nothing here is compared to data).

## Claims to test (exact arithmetic, sympy over ℚ(ζ₈); no floats)

- **C1** Each generator satisfies `σ² − √2 σ + 1 = 0`, eigenvalues `ζ₈^{±1}`, order 8.
- **C2** Braid relations hold on the actual matrices (B₂; B₃ and all three pairs of
  B₃^c for ℍ; B₄ from Cl(4,0)).
- **C3** (hand claim, unverified) `τ = iσ` satisfies `τ² = (q − q⁻¹)τ + 1` with `q = ζ₈`.
  Enumerate **all** scalars `c` such that `cσ` satisfies the repo Hecke relation for some
  `q`, and the full set of `q` per `c` (including the `q ↔ −q⁻¹` relabelling).
- **C4** Rescaling preserves the braid relation iff every generator gets the same `c`.
- **C5** Identify the irreducible `H_n(ζ₈)` constituents (n = 2, 3, 4); record `[k]_q`
  at `ζ₈` and whether `H_n(ζ₈)` is semisimple (`[n]_q! ≠ 0`).
- **C6** Does the representation factor through Temperley–Lieb (kills the 3-strand
  q-antisymmetriser, resp. symmetriser under the relabelling)?
- **C7** Is the normalised matrix trace a Markov trace on `H_2 ⊂ H_3` (and `H_3 ⊂ H_4`)?
  If so, which `z`; compare `z_D = q³/(q² + 1)` at `q = ζ₈` (note `q² + 1 = 1 + i ≠ 0`).

## Pass / fail

- **Verdict YES ("Hecke rep in disguise")** iff C1, C2 hold and some `c` makes every
  generator satisfy the repo Hecke relation with one common `q` (C3/C4), checked as exact
  zero matrices.
- **Verdict NO** if no scalar rescaling works (then report which deformed relation it
  does satisfy).
- C5–C7 are descriptive; each is reported as computed, including negatives. A Markov
  match with `z_D` is reported as a coincidence check at Gresnigt's fixed `q`, not as
  evidence for any `q₀`.
- No fitting, no selection: every number is a symbolic identity or its failure.
