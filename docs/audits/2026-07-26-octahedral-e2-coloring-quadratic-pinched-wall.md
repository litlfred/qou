# `g₂` = the octahedral `e₂` finite part in the pinched limit — the exact 2509.02354 construction + the identified wall

**Date:** 2026-07-26 · **Branch:** `claude/octahedral-e2-g2-deuteron-2026-07-26` ·
**Axis:** Δ_λ binding — the μ₀ −9% closure, the bar-even coefficient `g₂` · **Owner steer:** *"go"*
(compute the octahedral `e₂` where `g₂` lives) · **Tier:** exact paper construction + symbolic
identities + **identified obstruction** (scope-(a); no fit to `g₂`; nothing wired).

## 0. Where this sits

PR #4309 proved the single shape modulus is *purely bar-odd* (the flat trefoil shape `z=½` is a
Rogers-dilog inflection), so `g₂` (bar-even) is entirely the **pairwise `e₂` coupling of the four
octahedral tetrahedra** (`FourDilogFirstOrder.e2`). This note grounds that `e₂` in the exact
construction of `2509.02354` and identifies precisely what remains.

## 1. The exact construction (McPhail-Snyder–Reshetikhin, eq 4.11–4.14, 4.19)

At a positive, non-pinched, log-colored crossing the χ-coloring gives **four tetrahedron shape-logs**:

- `ζ⁰_r = ε(β₂′ − β₁)`
- `ζ⁰_t = ε(β₂ − β₁ − μ₁)`
- `ζ⁰_l = ε(β₂ − β₁′ + μ₂ − μ₁)`
- `ζ⁰_b = ε(β₂′ − β₁′ + μ₂)`

with shapes `z_j = exp(2πi·ζ⁰_j)` and the ideal-tetrahedron relation
`exp(2πi·ζ¹_j) = 1/(1 − exp(2πi·ζ⁰_j))`. The R-matrix factorizes (eq 4.19) as
`(1/N)·Z_b·(Z_r ⊗ Z_l)·Z_t`, one quantum-dilogarithm `Λ(ζ⁰_j, ζ¹_j | ·)` per tetrahedron. The
amplitudes `a_j = log Λ_j` are bar-odd (linear in `ζ⁰_j` at leading order); `e₂ = Σ_{i<j} a_i a_j` is
bar-even — the object carrying `g₂`.

## 2. Verified symbolic identities (probe, from the paper formulas)

[`octahedral_e2_coloring_quadratic_probe.py`](../../computations/deltalambda/octahedral_e2_coloring_quadratic_probe.py)
(exit 0, 3/3):

- **A. Octahedral edge-gluing constraint** `ζ⁰_r + ζ⁰_l = ζ⁰_t + ζ⁰_b` holds *identically* ⇒
  `z_r·z_l = z_t·z_b`.
- **B. Bar-parity with the real shapes:** `e₁ = Σ ζ⁰_j` is bar-**odd** (the μ₀ first order),
  `e₂ = Σ_{i<j} ζ⁰_i ζ⁰_j` is bar-**even** (the `g₂` order) — confirming `FourDilogFirstOrder.e2` for
  the *actual* construction, not just the toy model.
- **C. `e₂` is an explicit quadratic form** in the six χ-coloring log-params `(β₁,β₂,β₁′,β₂′,μ₁,μ₂)`.
  `g₂` is its value at the deuteron trefoil coloring, in the pinched limit.

## 3. The pinched limit (why the deuteron is special)

The deuteron `σ₁³` = trefoil `T(2,3)` is a **torus knot** (flat, `Vol=0`, PR #4301). Its crossings
are **pinched**: `ζ⁰_j ∈ ℤ` ⇒ `z_j = 1` (degenerate tetrahedra) — the octahedral manifestation of
the flat shapes. `2509.02354` excludes pinched crossings from the generic formulas and handles them
as a **limit** (§5.2): the R-matrix is regular but the individual `Z_j` factors have poles/zeros. So

> **`g₂` is the *finite part* of `e₂` in the pinched limit — not the generic-coloring value.**

This is a *third* structural reason the naive routes failed (after: single-modulus inflection; and
the factor-2/9-8 double-counting): `e₂` at the deuteron is a singular (pinched) limit, and only its
finite part is `g₂`.

## 4. Correction (honest)

An earlier note (PR #4301 lineage) guessed `a_r = −a_l` (an exact conjugate pair). The real formulas
show the `r↔l` transposition lives in the **index convolution** of `Z_r`/`Z_l` (sums over `n′−n` vs
`n−n′`), *not* the shapes: `ζ⁰_r` and `ζ⁰_l` are independent. **Retracted.**

## 5. The wall (identified, not crossed) — honest scope

Computing the numeric `g₂` requires:

1. **Solve the trefoil boundary-parabolic coloring** — the six log-params pinned by the knot
   relations (`π₁ = ⟨a,b | a²b³⟩`), strand-conjugacy `μ₁ = μ₂ = μ` (single component ⇒ conjugate
   meridians), and the substrate pin `μ ↔ q₀`.
2. **Take the pinched-limit finite part** (§5.2).

`e₂` is a six-variable quadratic form; **all** coloring DOF must be pinned rigorously, or the residual
freedom *is* the wall — and tuning any residual to hit `g₂` is the forbidden §2e scan. This note sets
up the form and identifies the obstruction; it does **not** fabricate a coloring to hit `g₂`.

**scope-(a).** Proved/established: the exact `e₂` construction, the octahedral constraint, the `e₂`
bar-evenness with real shapes, and the pinched-limit identification. Not derived: the number `g₂`
(needs the pinched-limit coloring solution). Anti-laundering stands.

## 6. Next

The trefoil pinned-coloring + pinched-limit finite part of `e₂` is the concrete remaining computation.
It is a genuine (careful) calculation, not a scan — the coloring is *pinned*, so the finite part is a
forward number once the pinched limit is taken correctly. That is the point where `g₂` either emerges
or a residual coloring freedom is exposed as the true obstruction.

Refs: `library/arxiv-2509.02354v2/2509.02354v2.pdf` eq (4.11–4.14), (4.19), §5.2 (pinched);
probe [`octahedral_e2_coloring_quadratic_probe.py`](../../computations/deltalambda/octahedral_e2_coloring_quadratic_probe.py);
PR #4309 (`2026-07-26-coloring-hq0-map-rogers-inflection-g2-is-e2.md`, `RogersDilogInflection.lean`);
#4301 (deuteron = trefoil); #4127 (`FourDilogFirstOrder.e2`); #4158 W2b.
