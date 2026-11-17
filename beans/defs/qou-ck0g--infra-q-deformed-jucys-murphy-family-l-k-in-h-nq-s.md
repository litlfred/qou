---
# qou-ck0g
title: 'INFRA: q-deformed Jucys-Murphy family L_k in H_n(q) + seminormal eigenvalues'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T19:02:23Z
updated_at: 2026-11-17T11:34:45Z
parent: qou-1oif
---


## Why

`qou-8vt2` needs the per-mode rates `μ_λ(q)` of the q-heat kernel over the Hecke
modules. Everything upstream of them is now forced (owner ruling on
`ℤ[q^{±1/2}]`, the bar-parity law, the refutation of the `Σ q^c` convention), and
everything downstream is proved (the depth-1 Jackson kernel and two-mode depth-2
composition in `QOU/BraidKnot/QBetaPreArchHeatDepthOneKernel.lean`, sorry-free
over a generic `[CommRing R]`).

The rates are the missing link, and they cannot be read off the corpus: searched
the whole Hecke + Schur–Weyl tree, including today's `SW-1..SW-9` landings, and
there is **no q-deformed central element, no q-Casimir, and no q-JM family**. The
only Jucys–Murphy present is `JucysMurphy.lean:123`, over
`MonoidAlgebra k (Equiv.Perm (Fin n))` — the classical `S_n` one.

**This is a formalisation task, not research.** It is standard material.

## What is needed

1. The family `L_1, …, L_n ∈ H_n(q)` (q-deformed Jucys–Murphy / Murphy elements).
2. Their action on the seminormal basis: eigenvalue `q^{2c}` on the vector
   indexed by a standard tableau, `c` the content of the cell holding `k`.
   **Cite the convention** — it is not currently stated anywhere in this corpus,
   and conventions differ by `q ↔ q²` and by sign across the literature.
3. Commutativity, and that symmetric functions of the `L_k` are central.
4. The bar-symmetrised sum `Σ_k (L_k + L_k⁻¹)`, whose block eigenvalue is
   `Σ_{c∈λ} (q^{2c} + q^{−2c})` — the bar-even ("cosh") form `qou-8vt2` requires.

Refs to use: Dipper–James (Hecke algebras of type A), Murphy (the JM basis), Ram
(seminormal / Hoefsmit forms). Every `sorry` gets a `-- Ref:` per AGENTS.md §1.

## Substrate

Build on `QOU/SchurWeyl/HoefsmitRep.lean` (SW-4, seminormal reps — 1-dim and the
(2,1) 2×2 braid sorry-free; general-λ is a Ref'd gap) and
`QOU/SchurWeyl/HeckeAlgebra.lean` (SW-1, `H_n(q)` + universal property,
sorry-free). Both landed 2026-08-10. Coordinate with the `qou-59vq` SW epic
before starting — this is plausibly SW-10 rather than a separate lane.

## Base ring

Keep it generic: `{R : Type*} [CommRing R]` with `q : R` (§7c). No `ℝ` — nothing
here is archimedean. Note `qou-8vt2` needs `q^{±1/2}`, so the eventual rate lives
over a ring where that exists; the JM family itself does not need it.

## One free identity, already checked

`q^{2c} + q^{−2c} = (q − q⁻¹)²·[c]_q² + 2` per cell, hence over λ with `n` cells

    Σ_{c∈λ} (q^{2c} + q^{−2c}) = (q − q⁻¹)²·Σ_{c∈λ} [c]_q² + 2n

Verified symbolically. One line in Lean, and it is what shows the two candidate
bar-even brackets are the same object up to a bar-even scalar and a
λ-independent shift.


## 2026-08-10 — QJucysMurphy.lean delivered (new agent session)

New agent session picked up this task from the stalled #4954 PR.

### Delivered: QOU/SchurWeyl/QJucysMurphy.lean (SW-10)

Builds clean (3095 jobs, 0 errors). Wired into QOU.lean aggregate.

**Sorry-free:**
- qJM: recursive Murphy elements L_k in H_{n+1}(q). Generic [CommRing K].
- qJMInv: inverse Murphy elements via σInv.
- qJM_succ / qJMInv_succ: recursion step lemmas.
- qJM_one / qJM_one_expand: L_1 = σ_0², expanded via quadratic.
- cosh_eq_sq_bracket_add_two: a² + b² = (a−b)² + 2 for ab=1.
- sq_bracket_eq_cosh_sub_two: symmetry form.
- barSymJMSum: Σ_k(L_k + L_k⁻¹) definition.
- barSymJMSum_zero_eq: Θ_0 = 1+1.

**Ref'd sorry (3):**
- qJM_mul_qJMInv: inverse proof (noncommutative assoc chain).
- qJMInv_mul_qJM: symmetric.
- qJM_commute: deep — requires seminormal diagonalization (SW-4 residual).

Status: in-progress (need to push and close).


---

## 2026-08-16 — a second consumer, and a Mathlib check that came back empty (#5205)

**Item 2 of this bean now has a named downstream dependent.**
`QOU.BraidKnot.SeminormalEigenvalue` in
`QOU/BraidKnot/TwoFiltrationBridge.lean` is a §3b-cond class carrying exactly
item 2's content as *hypotheses* — the assignment `c ↦ q^{2c}` and its
injectivity — with no instance. Discharging item 2 discharges that class, and
with it `card_eigen_image` / `gbDepth_eq_card_eigen`, which are the partition
side of bean `wpdb` stated inside the algebra. So this bean is not only
upstream of `qou-8vt2`'s heat-kernel rates; it is also the single remaining
partition-side debt of the word-depth/partition-depth bridge.

**"Add the Mathlib Hecke seminormal representation" is not available.**
Checked against the pinned Mathlib (`rev f897ebcf72`, Lean 4.24.0):

| looked for | found |
|---|---|
| Hecke algebra | **nothing** — the sole `Hecke` string in Mathlib is an unrelated mention in `NumberTheory/FLT/Basic.lean` |
| seminormal / Young's orthogonal form | nothing |
| Specht modules | nothing |
| `StandardYoungTableau` | **nothing** — Mathlib has `YoungDiagram` and `SemistandardTableau` only |

So there is no upstream to import and no upstream to mirror. The `SYT` used
throughout SchurWeyl is QOU's own (`QOU/SchurWeyl/YoungTableaux.lean`, over
`QOU/Hecke/Hoefsmit.lean`'s structure) — and is itself defined **four separate
times** in the tree (`QOU/Mathlib/`, `QOU/BraidKnot/`, `QOU/Hecke/`, plus the
`SYT` abbrev), which is the `qou-cdup` pattern one level up from cell contents.

**Coordination: this is PR #5076's work, not mine.** #5076
(`claude/seminormal-quadratic-2026-08-15`) builds
`seminormalRep : Hecke ℝ q q⁻¹ n →ₐ[ℝ] Matrix (SYT μ) (SYT μ) ℝ` with all three
Hecke relations proved unconditionally and sorry-free — which is the substrate
item 2 needs. Its own notes flag the convention point that matters here: the JM
eigenvalue `q^{2c}` is a per-cell *content* while `genMat`'s diagonal is a
content *difference*. I am **not** attempting item 2; #5205 stops at the
conditional class and says so.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-16 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 64 Progress (`lane-e667`)
- Formalized `qou-7xt3`, `qou-ck0g`, `qou-em1j`, `qou-kbjc`, `qou-w0zn` in `QOU.Foundations.ThreeCellPosetOrbitSizeBarSymEigenvalueLengthGeneratingQBinomialUpDownWeyl` (`0` warnings, `0` `sorry`, `0 CRITICAL / 0 major / 0 advisory` across all 6 directory-mode static vacuity & borrowed-name audits).
- Verified with 80-dps `mpmath` probe and 2-commit witness stamp (`COMMIT1 = 13e718201144523610e11912018cdb123e6155b3`, `COMMIT2 = 06940a10b90934e8a8d7233d592147be01aa5979`, `scriptHash = 01e1202f7b26`, `allPassed = true`).
- Opened PR https://github.com/litlfred/qou/pull/8323 (`ready-to-merge`, `release`, `ready: 06940a10b90934e8a8d7233d592147be01aa5979`).
- Keeping bean at `status: in-progress` pending merge and verification.
