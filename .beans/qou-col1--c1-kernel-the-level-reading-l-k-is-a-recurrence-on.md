---
# qou-col1
title: 'C1 kernel: the LEVEL reading — L_K is a recurrence on the residue sequence across jet levels, not a t-shift operator; re-scope #6582/#6610'
status: todo
type: task
created_at: 2026-09-04T10:42:55Z
updated_at: 2026-09-04T10:42:55Z
---

## Correction of my own axis (2026-09-04)

`conj:qdifference-kernel-prolongation-symbol` writes `x = q^m` with `m` the **body order = jet degree** (its own text; `prop:binding-genfun-qdifference` has `G(x;q) = Σ B_n x^n` in body order `n`). So `σ : x ↦ qx` is the **level** step and `L_K` is a second-order recurrence on a level-indexed sequence — the residues `r_n = (D^n X)(−2)` of the jet tower, i.e. the periods of `prop:sw-period-residue-sum`. `D_q : J^n → J^{n+1}` is first-order in the level, so `L_K` is not `D_q` at all; it is the relation `D_q`'s residue tower must satisfy.

#6582 (`qou-33hb`) and #6610 (`qou-w0tx`) both read `σ` as a shift in the **t-exponent** `e` of a single jet. That reading is the pure-shift-1 special case (where level and exponent lock: `r_n = c^n a_{n−2}`), not the conjecture's reading. Their theorems stand as mathematics about those t-operators; the interpretive sentences ("if the conjecture holds, `D_q` has a non-derivative component" / "the `(−1)^m` twist is not produced by `D_q`'s iteration" / "W2 = which t-shift σ is") are re-scoped here.

## PLAN

1. Lean `QOU.Mass.C1KernelLevelReading`: `residueSeq D X n := (D^[n] X)(−2)`; `C1Rec q r := ∀ n, qint q (n+2) * r (n+2) = r (n+1) + r n`; (A) a C1 sequence with two zero initial values is zero (q not a root of unity); (B) a C1 sequence with `r 0 = 0` is `r 1 · c1Basis`; (C) `residueSeq D X 0 = 0` on any power-series seed, for ANY operator — so the body-order index is offset from the jet level, or `b_0 = 0`; (D) `twoOp` level-1 residue `= c₂(−2) a₀`; (E) derivative-like shift-2 ⇒ at offset 0 the C1 residue tower is zero; at offset 1 it is `c₁(−2)c₂(−1) a₁ · c1Basis`, vanishing at its first slot; (F) pure shift-1 locking `r_n = (∏ c) a_{n−2}`.
2. Exact probe.
3. Audit doc with the contamination list (2 audit docs, 2 scope paragraphs on the conjecture block, 2 PR bodies, 2 beans, 2 Lean docstrings); re-scope the two paragraphs on the conjecture block; corrections appended to `qou-33hb` / `qou-w0tx`.
