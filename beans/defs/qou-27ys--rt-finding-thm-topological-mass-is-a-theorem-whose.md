---
# qou-27ys
title: 'RT finding: thm:topological-mass is a `theorem` whose Lean is a self-assuming projection and whose own proof says equality is open'
status: in-progress
type: bug
priority: high
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-20T16:30:00Z
parent: qou-ncxf
---

Found by the qou-ncxf pass-1 blind round-trip audit (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B08).

- Statement: `folio/quantum-observable-universe/mass-endomorphism/topological-mass.md`, kind `theorem` (`topological-mass.ts`).
- Lean: `folio/quantum-observable-universe/lean/QOU/Torsion/mass_decomposition_categorical.lean`. The proof term is `ctx.impl_mass_decomposition_categorical ctx.decomposition_active`. The conclusion is a field of `MassDecompositionCategoricalContext` applied to another field of the same class. RT-1 leg A and RT-2 leg B both flagged it independently as projection-of-assumption.
- Narrative proof: `folio/quantum-observable-universe/mass-endomorphism/topological-mass-proof.md`, lines 30–46. It proves only the upper bound m ≤ ‖Hol‖ + Σ Φ_q(z_i), and states that equality in the transient bound "is open". Two further gaps: orthogonality gives additivity of SQUARED norms, not of norms; and Φ_q(z_i) is used as a norm without an absolute value.

So the block's kind (`theorem`), its Lean (a projection) and its proof (a one-sided bound, equality open) disagree. Options: demote the block to `conjecture` (equality) plus a proposition (the ≤ bound); or keep it and state a conditional banner per §3b-cond (which fails rule 5, non-degenerate). This is mass-chapter scope (W1), so it is an owner/W1 decision. Asked on PR #8526. Do NOT close while the equality is open.

## 2026-11-20 owner ruling and implementation (W11)
The owner answered "Y" to the [W11 ask] on #8526, choosing option 1: split. Branch `claude/topological-mass-split-2026-11-20`:
- `thm:topological-mass` is now `conj:topological-mass` (kind conjecture). The projection `lean.ref` is dropped.
- New `prop:topological-mass-upper-bound` with sibling `topological-mass-upper-bound.lean`, declaring `QOU.Torsion.mass_upper_bound_localised`. It is generic seminormed group, sorry-free, lean-direct exit 0, and uses only the axioms propext, Classical.choice and Quot.sound.
- Both proof blocks are retargeted to the new prop. Each claimed norm-additivity from orthogonality; they now conclude `≤`, with the squared-norm caveat.
- All `thm:topological-mass` references are relinked in 21 content files. `prop:mobius-energy` only needed the mass definition, so it now points at `def:mass-identity`.
- Stays in-progress until merged. The equality itself is an open conjecture; follow-up items are in qou-tm3c.

## 2026-11-20 — tm (child of coordinator #8526): conjecture REDUCED to ray alignment (PR #8581)

**Not a closure.** The conjecture stays open; do not complete this bean on the strength of this note.

- New sorry-free Lean `QOU/Torsion/TopologicalMassEquality.lean` (lean -DautoImplicit=false -s 65536 exit 0; axioms propext/Classical.choice/Quot.sound only). `mass_decomposition_eq_iff`: given the proved split t = d + Σ τ_i, the conjecture ‖t‖ = ‖d‖ + Σ‖τ_i‖ holds iff d and all τ_i lie pairwise on a common ray (strictly convex real normed space; for ℝ: share a sign; for ℂ: share a phase). Necessary and sufficient.
- Corollaries: equality when all pieces ≥ 0 (`mass_decomposition_eq_of_nonneg`); STRICT inequality as soon as two pieces are anti-aligned (`mass_decomposition_lt_of_anti_aligned`, `..._desc_anti_aligned`); `Multiplicative ℝ` form of `TransientLocalisationNormEquality` (`transient_norm_equality_mult_iff`).
- `norm_add_lt_of_inner_eq_zero`: two non-zero orthogonal vectors give STRICT triangle inequality. So the `.md` sentence "when the splitting remains orthogonal … the mass decomposes additively" is false if read about the norms of the algebra pieces (scope (b), invariant = Pythagoras + positivity); read about the scalar traces, orthogonality says nothing about their phases. Same applies to `lem:topological-mass-eigenspace-decomp` (kind `lemma`, `.md` states norm equality, Lean proves only the vector split) and to the "Pythagoras" framing in `QOU/TopologicalMass/cat_eigenspace_decomposition.lean` docstring.
- Corpus data (probe `computations/probes/topological_mass_ray_alignment_probe.py`, mp.dps 60, proton pin q0 = 1.10997858275138…): the only producer with separate pieces, `mass_endomorphism.py::mass_from_tower`, gives all signed pieces POSITIVE for electron/proton/neutron (Π V̂_full = 0.673…, 1.0229…, 0.7594…; Φ_q values > 0), so the equality holds there. Scope (a), and weak: that producer DEFINES mass as the sum of norms (assumes the conjecture), and the sign of the transient trace value is not fixed by the corpus (`lem:topological-mass-dilogarithm` gives only its norm = Φ_q(z_i)).
- Open gap, precise: show the categorical trace pieces tr_desc(ϱ), tr_trans(ϱ,p_i) share a phase (e.g. trace positive on each summand and the pieces positive elements). No corpus artifact currently computes them as signed scalars from τ̂ and a categorical trace.
