---
# qou-col1
title: 'C1 kernel: the LEVEL reading — L_K is a recurrence on the residue sequence across jet levels, not a t-shift operator; re-scope #6582/#6610'
status: completed
type: task
priority: normal
created_at: 2026-09-04T10:42:55Z
updated_at: 2026-09-04T12:28:29Z
---

## Correction of my own axis (2026-09-04)

`conj:qdifference-kernel-prolongation-symbol` writes `x = q^m` with `m` the **body order = jet degree** (its own text; `prop:binding-genfun-qdifference` has `G(x;q) = Σ B_n x^n` in body order `n`). So `σ : x ↦ qx` is the **level** step and `L_K` is a second-order recurrence on a level-indexed sequence — the residues `r_n = (D^n X)(−2)` of the jet tower, i.e. the periods of `prop:sw-period-residue-sum`. `D_q : J^n → J^{n+1}` is first-order in the level, so `L_K` is not `D_q` at all; it is the relation `D_q`'s residue tower must satisfy.

#6582 (`qou-33hb`) and #6610 (`qou-w0tx`) both read `σ` as a shift in the **t-exponent** `e` of a single jet. That reading is the pure-shift-1 special case (where level and exponent lock: `r_n = c^n a_{n−2}`), not the conjecture's reading. Their theorems stand as mathematics about those t-operators; the interpretive sentences ("if the conjecture holds, `D_q` has a non-derivative component" / "the `(−1)^m` twist is not produced by `D_q`'s iteration" / "W2 = which t-shift σ is") are re-scoped here.

## PLAN

1. Lean `QOU.Mass.C1KernelLevelReading`: `residueSeq D X n := (D^[n] X)(−2)`; `C1Rec q r := ∀ n, qint q (n+2) * r (n+2) = r (n+1) + r n`; (A) a C1 sequence with two zero initial values is zero (q not a root of unity); (B) a C1 sequence with `r 0 = 0` is `r 1 · c1Basis`; (C) `residueSeq D X 0 = 0` on any power-series seed, for ANY operator — so the body-order index is offset from the jet level, or `b_0 = 0`; (D) `twoOp` level-1 residue `= c₂(−2) a₀`; (E) derivative-like shift-2 ⇒ at offset 0 the C1 residue tower is zero; at offset 1 it is `c₁(−2)c₂(−1) a₁ · c1Basis`, vanishing at its first slot; (F) pure shift-1 locking `r_n = (∏ c) a_{n−2}`.
2. Exact probe.
3. Audit doc with the contamination list (2 audit docs, 2 scope paragraphs on the conjecture block, 2 PR bodies, 2 beans, 2 Lean docstrings); re-scope the two paragraphs on the conjecture block; corrections appended to `qou-33hb` / `qou-w0tx`.


## RESULT (2026-09-04, PR #6628)

**σ in L_K is the level step; L_K is the recurrence on the residue tower r_n = (Dⁿ X)(−2), never D itself.** `QOU.Mass.C1KernelLevelReading`, sorry-free, axioms propext/choice/Quot.sound:
- `c1RecFrom_ext`: rank 2 (two base cases) for q not a root of unity.
- `residueSeq_zero_of_powerSeries`: r_0 = 0 for every operator; carrier has b_0 = b_1 = 1, b_2 = 2/(q+1), so no tower equals it at level 0.
- `twoOp_residueSeq_one`: r_1 = c₂(−2)a₀. `derivativeLike_twoOp_c1Rec_zero`: c₂(−2) = 0 ⇒ C1-from-0 residue tower ≡ 0 — #6582's clause on the correct axis.
- `twoOp_c1RecFrom_two_iff`: derivative-only tower, κ = c₁(−2)c₂(−1) ≠ 0: C1 from level 2 on residues ⇔ [m+4]_q s_{m+2} = s_{m+1} + s_m on t¹-coefficients s_m.
- `shiftOne_const_residueSeq`: locking r_n = cⁿ a_{n−2} (the t-shift reading's special case).

Probe measurement (Jackson + q-d/dz): κ = −1 (balanced) / −1/q (geometric); level-m constraint reads a_{m+3}..a_{2m+5}; first four have rank 4; NO constraint mentions a₀. Probe defect fixed pre-commit: finite-sum q-integer is 0 at negative index (killed c₁(−2)).

Re-scoped: both #6582/#6610 scope paragraphs on the conjecture block rewritten; audit doc with contamination list; corrections appended to qou-33hb / qou-w0tx. Withdrawn as statements about D_q: "the (−1)^m twist is not produced by D_q's iteration", "W2 = which t-shift σ is". Survives: the derivative-only exclusion (from level 0). New open: solve the shifted-C1 constraint on (c₁, c₂, X) — that IS the symbol identification on the level axis.

Waiting on: owner merge permission for #6628.



## Merged as #6628 (rebase, 2026-09-04). Follow-up: test C1-on-the-residue-tower against the ACTUAL Σ seed (next bean).
