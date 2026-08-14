---
# qou-gjg6
title: 'GAP (im9l residual): general-lambda Hoefsmit braid — size-6 S3-orbit Yang-Baxter identity'
status: todo
type: task
created_at: 2026-08-11T01:05:26Z
updated_at: 2026-08-11T01:05:26Z
parent: qou-59vq
---

## Residual after SW-4-gen scaffolding pass (2026-08-11)

`hoefsmit_seminormal_rep` in
`content/quantum-observable-universe/lean/QOU/SchurWeyl/HoefsmitRep.lean`
still carries ONE `-- Ref:`-cited `sorry` (the general `∀ λ ⊢ N` statement).
Everything else in the file is sorry-free (`#print axioms` →
`[propext, Classical.choice, Quot.sound]`, no `sorryAx`).

### What landed sorry-free this pass (reusable for the general build)
- `seminormalBlock q a` — the generic axial-distance 2×2 orbit block
  (top-right 1, trace q−q⁻¹, det −1, one free param `a`).
- `seminormalBlock_quadratic` — Hecke quadratic relation, ALL q≠0, ALL a.
- `seminormalBlock_ne_scalar` — non-degeneracy (off-diagonal 1≠0).
- `S1_eq_seminormalBlock` — `S1 q = seminormalBlock q (-1/(q³+q))`.
- `S1_ne_scalar`.
- `seminormalRep22 : Hecke ℝ q q⁻¹ 3 →ₐ[ℝ] M₂(ℝ)` (λ=(2,2), N=4) with
  σ0/σ1/σ2 lemmas + `seminormalRep22_nonScalar`. First 4-strand rep;
  first NON-VACUOUS far-commutation σ0σ2=σ2σ0. All relations reduce to
  the (2,1) lemmas `S0_quadratic`/`S1_quadratic`/`S0_S1_braid`.

### What remains open (the hard core)
1. Enumerate the `s_i`-orbits of `SYT λ` (Lean: SYT type is
   `QOU.Mathlib.StandardYoungTableau`; `dLambda`=Fintype.card). Each orbit
   has size 1 (entries i+1,i+2 same row → scalar q; same column → −q⁻¹) or
   size 2 (both s_i·T standard → a `seminormalBlock` with `a` the axial-
   distance rational function). Need a Lean map `Fin (dLambda λ) → SYT λ`
   and the orbit trichotomy as a decidable case split.
2. Assemble the block-diagonal generator matrix `ρ_λ(σ_i)` from the orbits.
3. **BRAID for arbitrary λ** — the Yang-Baxter / axial-distance identity
   across the S₃-orbit of three consecutive entries i,i+1,i+2. Orbit sizes
   1/2/3 reduce to the (2,1)/(2,2)-style 2×2 identities (already have the
   template `S0_S1_braid`); the GENERIC size-6 orbit is a real
   6-dimensional identity NOT reducible to 2×2 blocks. This is Hoefsmit's
   thesis theorem. Refs: [hoefsmit1974], [ram1997] (axial-distance formulas).

### Suggested next step
Formalize the size-6 braid as a standalone lemma over ℝ: given the three
axial distances of an S₃-orbit, the two 6×6 generator matrices (each two
`seminormalBlock`s + two scalars, in the seminormal basis ordering) satisfy
`ρ(σ_i)ρ(σ_{i+1})ρ(σ_i) = ρ(σ_{i+1})ρ(σ_i)ρ(σ_{i+1})`. If that single
`field_simp;ring` 6×6 identity closes, the general theorem is within reach
(the orbit bookkeeping is then plumbing). If it does NOT close as one ring
identity, that is the true blocker to report.

Env: lean-direct against main-repo oleans (worktree has none); NEVER
`lake build`. Restore recipe in AGENTS.md / lean-environment-setup.md.
