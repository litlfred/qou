---
# qou-mjt3
title: 'Lean scaffolds owed for the chi/tetraplectic arc (the ''all assertions lean proved?'' ledger): WignerAxiom class; equivariance no-go (S_5-equivariant map from a 1-dim space to HH^2(M_0) is zero); K_0 -> HH_0 -> k factorisation of dim_q; link Euler number = chi_eu'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-lean
created_at: 2026-09-15T21:23:32Z
updated_at: 2026-10-10T08:08:05Z
parent: qou-8lxd
---

Owner instruction 2026-09-15: 'bean up and roast as recommended'. LEDGER of the arc's assertions by epistemic tier (measured 2026-09-15). LEAN, sorry-free, on the branch: (a) S_5 character arithmetic — H^1(T_{Sigma_4}) = [4,1]+[3,2], Sym^2/Sym^3/Alt^2 of V_4, V_4 (x) [3,2], forms on [3,2] and on H^1(T), the S_5-invariant Hochschild ledger of the base (QOU/Brings/S5CharactersOnBringDeformations.lean, decide, axioms [propext]); (b) the exact rational identities behind the two regularisations of dim_q(O_q(SU(2))) and [2]_q = q + q^-1 (QOU/Information/DimqRegularisationIdentities.lean, field_simp); (c) pre-existing: categorical trace = Markov trace under convention D at n=3 (markovWeights_eq_jones_of_fibre_categorical), Cartan contraction lemmas, the quaternion bracket (BringCone.lean), gammaGamma_length_even. PROBE-MEASURED, exact rationals, NOT Lean: brute-force check of the power-sum formulas over 120 permutations (the Lean takes the formulas as definitions). CITED THEOREMS, not formalised: HKR for a smooth curve; Serre duality; the normal-bundle splitting N_C = O(2)+O(3) and H^1(T_P3|_C) = 0 (route 2); Max Noether (route 1); Whitehead's lemmas; Brown–Zhang twisted duality; the zeta-continuation convention; deg K = 2g-2 and the link-of-cone = circle bundle of O(-1) (bean on the 3-Sasakian finding). NOT YET WRITTEN (this bean): (1) class WignerAxiom over a field k with fields finrank_obstruction_eq_one and euler_image (the archimedean image of the generator is the Euler class of T_{M_0}) — the §3b-cond carrier for def:skein-resolution-obstruction / thm:qou-obstruction-reduction, which E1 already made conditional on conj:wigner-axiom; (2) equivariance no-go: given the decomposition (a), any S_5-equivariant linear map from a trivial 1-dim representation into H^1(T) is zero — Schur, finite; states in Lean what bean qou-nnyn's analysis says in prose; (3) K_0 -> HH_0 -> k: dim_q(V_n) = [n+1]_q as the evaluation of ch on the Wedderburn blocks (needs the QuantumUniverse.dimQ field; scaffold as a def + the n=1 identity); (4) link Euler number: e(T_{Sigma_4}) = 2 - 2g = -6 = -deg(B) with deg = 2*3 — trivial arithmetic, but it pins the -6 to the cone geometry. Items 1-2 are the ones that make thm:qou-obstruction-reduction honest under §3b-cond; do them first.


2026-09-15 THREE OWED ITEMS WRITTEN (owner: "make sure all lean done too"). (1) K₀ → HH₀ → k factorisation: lean/QOU/QuantumObservableUniverse/GrothendieckChern.lean — K0 U = U.blocks →₀ ℤ, chernCharacter, evDimQ, dimQK0, theorem dimQK0_eq_evDimQ_chernCharacter (dim_q = ev ∘ ch); content def:grothendieck-group-of-a-qou + def:chern-character + ex:su2-characters-and-quantum-dimension (sibling su2-characters-and-quantum-dimension.lean: ch(V_n)(1) = n+1, (q−q⁻¹)·ch(V_n)(q) = q^{n+1} − q^{−(n+1)}). (2) Equivariance no-go: lean/QOU/Brings/WignerTargetEquivariance.lean — equivariant_map_vanishes_of_no_invariants (abstract) + no_invariant_in_hh2_of_base / two_invariants_in_hh0_of_base read off S5Char.hochschild_invariants_of_base; the character-theory bridge ⟨χ,1⟩ = dim N^G is the one cited input (Fulton–Harris 2.11). (3) Link Euler number: lean/QOU/Brings/BringConeLinkEulerNumber.lean — canonical_link_euler_eq_chi (−deg K = 2 − 2g), bring_link_euler (−6), hopf_link_euler (−1), bring_over_hopf; content change to the corpus lemma stays owner-gated (qou-rydq). Also: the audit doc named EulerCharacteristicOfHochschild.lean before it existed — now written: lean/QOU/Information/EulerCharacteristicOfHochschild.lean (hhEuler_eq_hodgeEuler for any Hodge square via Int.negOnePow; hhEuler_curve = 2 − 2g; hhEuler_bring = −6). Verification status recorded on the PR at push time; lean-direct with -DautoImplicit=false -s 65536 against the /tmp/ov7422 overlay.


## CLOSED 2026-10-10 — all FOUR owed Lean items verified present and sorry-free

The 2026-09-15 append reported *three* items written and left item (1) — the
`WignerAxiom` §3b-cond carrier — reading as outstanding, which is what kept this
bean `todo`. **Item (1) is also written.** Measured on the live post-rename tree
(`folio/quantum-observable-universe/lean/`), every `sorry` match in all five
files is a *docstring mention* ("no `sorry`", "sorry-free"); none is a tactic:

| owed item | file | lines |
|---|---|---:|
| (1) `class WignerAxiom` | `QOU/AlgebraicSubstrate/WignerAxiom.lean` | 124 |
| (2) equivariance no-go | `QOU/Brings/WignerTargetEquivariance.lean` | 72 |
| (3) `K₀ → HH₀ → k` | `QOU/GrothendieckChern.lean` | — |
| (4) link Euler number | `QOU/Brings/BringConeLinkEulerNumber.lean` | 66 |
| (extra) Hochschild Euler char | `QOU/Information/EulerCharacteristicOfHochschild.lean` | 127 |

**Path correction for the next reader.** The 2026-09-15 append names item (3) as
`lean/QOU/QuantumObservableUniverse/GrothendieckChern.lean`. It is at
`lean/QOU/GrothendieckChern.lean` — one directory up. A `test -f` on the recorded
path reports MISSING, which is how this bean read as one-item-short.

**`WignerAxiom` is content-bearing, not an empty marker** (§3b-tax, the check
that matters for a conjecture carrier): three real `Prop` fields —
`finrank_obs_eq_one : finrank k Obs = 1`, `euler_mem_range : euler ∈ range realise`,
`euler_ne_zero`. Two `-- Ref:` citations. **No instance is provided**, which is
the honest open state for `conj:wigner-axiom`, and two derived theorems consume
the fields (`exists_generator`, `eq_smul_of_ne_zero`, `pairing_of_generator`) —
so it derives rather than projecting its own conclusion (§3b-cond item 5).

**Rule 13a.** This bean's subject is *"Lean scaffolds owed"* — a mechanical
deliverable, not a conjecture. `conj:wigner-axiom` stays open and un-instanced;
closing this records that its carrier exists, not that it holds.

**Not closed by this, deliberately:** the corpus content change (rewording
`lem:bring-cone-reeb-quaternionic-twist` / `rem:tetraplectic-su2-gauge-reading`)
is owner-gated and lives at **`qou-rydq`**, now re-filed to `8f-decide`.
