---
# qou-fm7s
title: 'NS vector 1: geometric depletion (Constantin–Fefferman) mapped to the QOU direction/Levi field'
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T20:57:48Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-vo9t
---

Owner (2026-10-12): pursue NS attack vectors 1, 2, 3 and 5 (unforced NS). This bean is v1. Formalize first: a genuine Lean core lemma where one exists, honest conditional statements otherwise, and an audit doc.

## 2026-10-13 — v1 delivered on branch `ns-v1` (status stays in-progress: the mapping question is open)

- **Lean [sorry-free]:** `QOU/FluidDynamics/GeometricDepletion.lean`. It holds the kernel algebra D(e₁,e₂,e₃) = (e₁·e₃)det(e₁,e₂,e₃): D = 0 on e₃ = ±e₂; D is even in e₃ and odd under a global flip; and for unit vectors D² ≤ |e₂×e₃|² ≤ min(|e₃−e₂|², |e₃+e₂|²). Verified with lean-direct, exit 0; axioms are propext, Classical.choice and Quot.sound. No PDE statement or carrier.
- **Mapping verdict:** no QOU quantity is the Constantin–Fefferman hypothesis.
  - On a 3D contact manifold the corpus forces ker Θ = ξ^⊥ only on the filament.
  - The Levi data is one scalar, ξ·curl ξ, so the two eigenvalues and cond in core-levi-form are undefined in dimension 3.
  - Under that reading, branch (A) "non-degenerate ⇒ singular" is false: u = e^{−νt}(sin z, cos z, 0) on T³ is a counterexample.
- **True conditional statement (contrapositive of Beirão da Veiga–Berselli):** a smooth-solution blowup forces the vorticity line field to lose ½-Hölder coherence. The corpus's anti-parallel argument never addresses filament bending.
- **Audit:** `docs/audits/2026-10-12-ns-v1-geometric-depletion.md`.
- **Next:** filament-curvature probe; owner decision on what Θ is off the filament; ingest the literature.

## 2026-10-13: owner Q1 enacted on branch `ns-q1-levi` (status stays in-progress; the conjecture is open)

Owner decision, verbatim: "Q1 Θ = f·ξ♭". The Levi chain is re-scoped onto the vorticity line field on the 3D flow domain (ℝ³ or T³, not 𝒮).
- **`prop:core-levi-form`** (`c1ab1bf9fb`, `6e44754d91`): the statement is now unconditional geometry.
  - ker Θ = ξ^⊥.
  - Θ∧dΘ = f²(ξ·curl ξ) vol, so contact iff ξ·curl ξ ≠ 0, independently of f.
  - dΘ restricted to ker Θ is the single scalar f(ξ·curl ξ) times the area form.
  - ω·curl ω = |ω|²(ξ·curl ξ).
  - Removed: the two-eigenvalue pair, cond, the aspect identities (a)–(e) and the conditional banner. They are recorded in an authorNotes caveat. Lean `QOU.FluidDynamics.CoreLevi` (generic CommRing): `helicity_rescale`, `contact_iff_rescale`, `levi_restriction_rank_one`, `core_levi_form`.
- **`conj:levi-degeneracy`** (`90111696b4`):
  - Branch (A) is withdrawn, refuted under this reading by the Beltrami solution (scope (b) for that implication). Lean `beltrami_refutes_branchA` checks curl ξ = ξ, ξ·curl ξ = 1, the heat equation and |ω|² ≤ 1.
  - C_L, β and regime (C) are withdrawn as undefined.
  - Branch (B) is kept as the open conjecture, restated on the Levi scalar, with a note that CF/BdVB do not support it. It is an open carrier, `LeviDegeneracy` (no instance).
  - Added the standard-cited BdVB contrapositive. `BeiraoDaVeigaBerselliCriterion` carries the cited theorem as its only field, and `blowup_forces_direction_incoherence` is derived from it.
  - The old q-ladder degeneracy-set class is removed (no other consumer).
- **`rem:townsend-biot-savart-strain`** (`b2f09afea9`): κ² is the core aspect ratio, not a Levi condition number. The inference "flattening ⇒ branch (B)" is removed, and a stale "limit is a sorry" docstring is corrected.
- **`rem:crow-approach-amplification`** (`b0bcf51191`): the consequences are re-attached to the 2D reduction, and Crow bending is tied to the BdVB necessary condition (scope (a)).
- **refs** (`d2681faa2b`): `constantin1993` and `beiraodaveiga2002`. DOIs are not verified and are omitted; the primary texts are not held.
- **Verification:**
  - lean-direct `-DautoImplicit=false -s 65536` exits 0 on all three changed .lean files.
  - Axioms are ⊆ {propext, Classical.choice, Quot.sound}.
  - No sorry, axiom, native_decide or `: True`.
  - Validate gives 8 issues, the baseline, none in these blocks.
  - qa-sweep attestations were regenerated.
- **Not edited, still written against the old statement (owner call):**
  - `rem:core-levi-interpretation` and `rem:hyperbolic-overlap-saturation` both assert the withdrawn branch (A).
  - `rem:observability-fluid-context`, `rem:q-metric-contact-deformation`, `rem:observability-independent-motivation`, `prop:ns-obstruction-tower` and `rem:ns-obstruction-tower-summary` use Levi eigenvalues or the condition number.
  - The library files `levi_growth_trichotomy.lean` and `levi_pair_channel_branch_b.lean` still carry the β / condition-number encoding.


## 2026-10-13 — consumers re-scoped (owner option 2), branch `ns-levi-consumers`

Base `f56e6d2b1f`. All nine consumers named above as "not edited" are re-scoped onto the Levi scalar ξ·curl ξ:

- `rem:core-levi-interpretation`: "NS blows up ⟺ Levi non-degenerate ⟺ κ=O(1)", both outcome readings and the root-of-unity aspect-ratio-as-Levi bound withdrawn; restated as what ξ·curl ξ measures + open branch (B) + cited BdV–B contrapositive. Title changed; uses drops prop:root-of-unity-truncation.
- `rem:hyperbolic-overlap-saturation`: ODE lock κ² = πν/(2Γ+πν) > 0 kept as a core-shape result (Lean unchanged); "Levi non-degenerate / both eigenvalues / branch (A) ⇒ blow-up" withdrawn. Stale πν/Γ in the opening corrected to its own boxed value.
- `rem:observability-fluid-context`, `rem:q-metric-contact-deformation`, `rem:observability-independent-motivation` (+ table row): Levi-translation sentences withdrawn, other readings untouched.
- `prop:ns-obstruction-tower`: proof step (d) (H¹ ≠ 0 ⟺ λ∥,λ⊥ > 0 ⟺ κ ∈ (0,∞)) withdrawn; statement and Lean unaffected (no Levi field), kind stays proposition. `rem:ns-obstruction-tower-summary` follows.
- Lean: `LeviGrowthTrichotomy` → `GrowthExponent` (branchA/branchB/leviNonDegenerate removed, `levi_branches_exclusive` removed); `linear_condNumber_degenerate` withdrawn; `linear_seq_forces_beta_one` kept as an aspect-ratio statement. Old theorem names kept as deprecated aliases. lean-direct exit 0, axioms ⊆ {propext, Classical.choice, Quot.sound}.

Old text of every block is recorded verbatim in its authorNotes. run-validate 9 → 8 (the drop is the no-orphan-sidecar warning clearing once qa-sweep created test/results; no content change).

**Still carrying withdrawn statements, NOT in the nine and NOT edited (owner call):** `QOU/FluidDynamics/yekutieli_levi_unification.lean` (step (d) as a class field; branch A/B theorems), `QOU/FluidDynamics/qou_ns_in_qou.lean` (`QOUFluidUniverseLevi`, `qou_levi_nondegenerate`, branch A), `ns-singularity-descartes-proof.md` (lists "non-degeneracy of the Levi form via the core-Levi equivalence" as input 3 of the NS-singularity theorem), `ns-singularity-descartes-interpretation.md` ("core-Levi bounding"), and the stale titles for prop:core-levi-form / conj:levi-degeneracy in `index-of-definitions/definition-index.md`. The conjecture (branch B) remains open; this bean stays in-progress.

## 2026-11-15 — leftovers re-scoped (owner option 1), commit bb9fbdf6d on `claude/bold-gates-00l1bl`

Owner chose option 1 ("re-scope all five, and search for files the old scan missed") in the project thread "Settle open-problem leftovers".
- `yekutieli_levi_unification.lean`: step (d) fields and the branch A/B theorems removed; steps (c)/(e) kept as `ns_obstruction_iff_localCohom`.
- `qou_ns_in_qou.lean`: `QOUFluidUniverseLevi`, `qou_levi_nondegenerate` removed. **Flagged, not changed:** the base chain still models `NS(A) = e(ξ)|_Σ` with `χ ≠ 0 → NS(A) ≠ 0`, which contradicts the restated `thm:ns-singularity-descartes` item 3 (`H²(Σ,·) = 0`). Owner call.
- `ns-singularity-descartes-proof.md` (step 3 withdrawn), `-interpretation` (rewritten, old text in authorNotes), `definition-index.md` (three stale rows).
- **Missed by the earlier scan:** `prop:root-of-unity-truncation` (box "NS blows up ⟺ Levi non-degenerate ⟺ κ = O(1)" and the κ² = condition-number paragraph) plus its library twin `root_of_unity_truncation.lean`; `ns-obstruction-intro.md` (two stale titles). Re-scoped the same way.
- Not touched: `Elaboration.lean` `GeneralisedLeviConditions` (CR-manifold Levi signature, unrelated).
Status stays in-progress: branch (B) is open.

## 2026-11-15 — base chain restated on the global class (owner option 1)

`qou_ns_in_qou.lean`: the obstruction field is now the global Euler class
`e(ξ) ∈ H²(S, ℤ)` (degree `χ(A)`), not `e(ξ)|_Σ`. Step 2 is `deg e(ξ) = χ(A)`;
the Kummer justification is dropped. Field names and `descartesQOU` unchanged.
lean-direct exit 0; `qou_internal_ns_singular` uses no axioms,
`descartes_internal_ns_singular` only `propext`.

## 2026-11-21 (bean-drain sibling bring-gerbe-ns, session_01Qmmkt6JCxoNkQcgaG1tFNF, issue #8808)

Superseded-premise check (owner, 2026-11-21: photon L±, virtual photons, old γγ letters, T(2,n_s), convention C, single-term trace, trefoil electron, c_2 = −1, χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean; its subject is surface topology / gerbes / NS and touches none of them.
No change on main since 2026-11-15; branch (B) of conj:levi-degeneracy remains open. Not touched in this pass.
