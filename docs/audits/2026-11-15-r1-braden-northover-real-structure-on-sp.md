# R1: the Braden–Northover real structure does not fix the polarization phase `λ` without a choice

**Date:** 2026-11-15 · **Bean:** `qou-r1bn` (epic `qou-qs0e`) · **Stacked on:** draft PR #7825
(stream 6b) · **Lean:** [`QOU/StandardModel/BringRealStructureTransport.lean`](../../folio/quantum-observable-universe/lean/QOU/StandardModel/BringRealStructureTransport.lean)
· **Discipline:** no fit, no identification adopted, nothing wired.

## Question

Stream 6b showed that the polarization dictionary `(φ₀, φ₁) ↦ [φ₁ : λ φ₀]` on
`𝒮_p ≅ ℙ¹(ℂ)` has a free phase `λ ∈ U(1)`. Fixing it needs an antilinear involution
(a real structure) on `𝒮_p`. The model cone carries a whole `U(1)` of them, conjugation
`p ↦ u p ū` by `u = c j + d k`, and selects none. The one untested candidate was the
Braden–Northover real structure on `Jac(Bring)`
([`2026-07-18-alpha-em-bring-real-structure-grounding.md`](2026-07-18-alpha-em-bring-real-structure-grounding.md)).

**R1.** Does it induce an antilinear involution on `𝒮_p`? If so, does it fix `λ`
without a choice?

## Verdict

1. **Not derivable now (scope (a)).** The corpus has no map from Bring's curve `B`, or
   from `Jac(B)` or `H¹(B)`, to `𝒮_p`. Without such a map nothing is induced on `𝒮_p`.
2. **Structural result on the model, for any future map.** Bring's side has exactly one
   natural `ℙ¹`, `ℙ(M)` with `M = H¹(E, ℂ)` the multiplicity space in
   `H¹(B) = H¹(E) ⊗ std`. On `ℙ(M)` Bring supplies two canonical antiholomorphic
   involutions. Whichever is transported, `λ` stays unfixed:
   - the **coefficient (Hodge) conjugation `κ`** swaps the two Hodge points. Matched to
     the chart centres `∓i`, it is the reflection with normal `i`. That reflection
     commutes with every `λ`-rotation, so it is blind to `λ` (`refl_unitI_comm_cplx`);
   - **`κ ∘ σ*`, with `σ` the Braden–Northover involution,** fixes the two Hodge points.
     Matched to `∓i`, it is a member of the #7825 family, so it does select one real
     circle. But the identification `ℙ(M) ≅ 𝒮_p` that matches the points is unique only
     up to a rotation about the `i`-axis, and rotating it rotates the selected circle by
     the same angle (`conjBy_refl_conjBy`). **The choice of `arg λ` becomes the choice
     of the identification's phase. It is moved, not removed.**

   The two cases are exhaustive among reflections: the only `λ`-invariant normal is the
   axis `i` (`rot90_normal_axial`).

So the answer to R1 is **no**: the Braden–Northover real structure does not fix `λ`
without a choice. This is the expected "likely null" result.

## 1. Corpus and library check (six paths)

| Path | Query | Result |
|---|---|---|
| `docs/audits` | Braden, Northover, Jac(Bring), real structure | The 2026-07-18 grounding audit (real `j`-invariants imply a real structure exists on `Jac(Bring)`); the 2026-06-24 keystone audit (`H¹(Bring) = H¹(E) ⊗ std`, period matrix `Z = τ₀·C`); #7825's E2 table. None maps anything to `𝒮_p`. |
| `folio/` content | Bring + exceptional divisor / `𝒮_p` | `reeb-bundle.md`, `breit-wheeler-vertex.md` define `𝒮_p` as the exceptional divisor at a brane point, with the Hopf fibration. `photon-ir-zero-mode-bring.md` uses only `b₁ = 2g` and the area. **No block relates `B` or `Jac(B)` to `𝒮_p`.** |
| Lean | `BringCone*`, `Brings/` | `BringConeLinkEulerNumber.lean`: the quaternionic cone is a *local* model. Its link is the Hopf bundle (Euler number −1, trivial `π₁`), against the Bring cone's link (Euler number −6, infinite `π₁`). `BringConeIcosahedral.lean`: "the corpus does not establish that Bring's `S₅` (or its `A₅`) acts on this cone at all." |
| `computations/` | real structure, Bring | `alpha_em/alpha_em_bring_real_structure_probe.py`: the `j`-invariants only. |
| `library/` | INDEX, sections, ocr | Riera–Rodríguez 1992 is held (`the-period-matrix-of-bring-s-curve-1hik02mwva`), including §"B does not admit more automorphisms" (`Aut(B) = S₅`). **Braden–Northover 2012 is NOT held.** It is registered (`folio/references/braden-northover-2012.json`), but there is no full text. So which involution they construct is not checked here (see §4). |
| `beans/defs` | Braden, real structure | `qou-b5qg` (α_EM B1–B5 chain). It concerns `Jac(Bring)` and Hodge conjugation, not `𝒮_p`. |

## 2. What the real structures on Bring's side are

**On the curve.** `B ⊂ ℙ⁴` is cut out by `Σxᵢ = Σxᵢ² = Σxᵢ³ = 0`. These have rational
coefficients, and `S₅` acts by real permutation matrices. So coordinate conjugation `c`
is an antiholomorphic involution that commutes with `S₅`. Since `Aut(B) = S₅`
(Riera–Rodríguez), every antiholomorphic automorphism is `c ∘ g`, and the real
structures are `c ∘ g` with `g² = 1`. There are **26** of them (1 + 10 transpositions
+ 15 double transpositions, checked by enumeration), in **3** conjugacy classes. **Only
`c` commutes with all of `Aut(B)`** (`bring_central_real_structure_unique`, via
`perm_comm_swaps_eq_one`: the centre of `S₅` is trivial).

**On `H¹`.** The corpus has `H¹(B) = H¹(E) ⊗ std` (2026-06-24 keystone, line 81;
isogeny-level, so it holds over `ℚ` and hence over `ℝ`). So `H¹(B, ℂ) = W ⊗ M` with
`M = Hom_{S₅}(W, H¹(B, ℂ)) ≅ H¹(E, ℂ) ≅ ℂ²`, and `ℙ(M) ≅ ℙ¹` is the one natural
projective line on Bring's side. It carries:

- two **Hodge points** `P = [M^{1,0}]` and `P̄ = [M^{0,1}]`. Relative to a real
  symplectic basis, `P` is the period point `τ₀` of `E` and `P̄` is `τ̄₀`;
- the **coefficient conjugation `κ`** from `H¹(B, ℝ)`. It exists for every curve, swaps
  `P ↔ P̄`, and fixes the circle `ℙ(H¹(E, ℝ))`, which separates them;
- the involution **`κ ∘ σ*`** for a real structure `σ` of `B`. It is antilinear, fixes
  `P` and `P̄`, and so fixes a circle through both.

Since `g ∈ S₅` acts on `W ⊗ M` as `ρ_W(g) ⊗ 1`, all 26 real structures `c ∘ g` induce
**the same** `κ ∘ σ*` on `ℙ(M)`. So the choice among them is invisible on `ℙ(M)`. Which
of the 26 Braden–Northover construct does not matter for R1. (This step is
representation theory: Schur's lemma on the single isotypic component. It is stated
here and not formalized.)

**A side remark on the 2026-07-18 audit.** That audit identifies "the Hodge conjugation"
with the Braden–Northover involution. On `H¹` these are different maps: `κ` exists
without any real structure on `B` and swaps the Hodge lines, while `κ ∘ σ*` preserves
them. This does not affect R1, since both are treated below. It may matter for the α_EM
B2 chain (`qou-b5qg`) and is flagged, not corrected, here.

## 3. Transport to `𝒮_p`: the dichotomy (Lean, on the model sphere)

On `S²` (pure quaternions) the reflection with unit normal `n` is
`refl n x = −n x n̄`. The facts:

| Lean | Statement |
|---|---|
| `hopf_realStr` | The #7825 real structure `p ↦ u p ū` acts on `S²` as `refl u`. So the #7825 family is exactly the reflections whose normal lies in the `j`–`k` plane. |
| `refl_orthW_unitI` | Every member of the family fixes the chart centre `i` (and hence `−i`). |
| `refl_unitI_unitI`, `refl_unitI_apply` | The reflection with normal `i` swaps `i ↔ −i`. Its mirror is the `j`–`k` circle. |
| `refl_unitI_comm_cplx` | The reflection with normal `i` commutes with every rotation `conjBy (a + b i)`, which are exactly the `λ`-rotations of `hopf_dict_rotate` (#7825). |
| `rot90_normal_axial` | If the 90° `λ`-rotation fixes a normal up to sign, the normal is along `i`. So no member of the family is `λ`-invariant. |
| `conjBy_refl_conjBy` | Covariance: rotating the sphere by `g` carries `refl n` to `refl (g n ḡ)`. |

**Case A: `κ` transported.** Any identification `φ: ℙ(M) → 𝒮_p` that sends the
distinguished pair `{P, P̄}` to the distinguished pair `{∓i}` carries `κ` to a reflection
swapping `±i`, that is, to `refl i` (for the round structure in which both pairs are
antipodal). That reflection is `λ`-invariant, so it fixes no value of `λ`. This does
not depend on the round structure: in the chart where `∓i` are `0, ∞`, an
antiholomorphic involution swapping them is `z ↦ a/z̄` with `a` real. For `a > 0` its
fixed circle is `|z| = √a`, which every rotation `z ↦ e z` preserves. Its fixed
circle, the equator `|v₁| = |v₂|`, is exactly the orbit that `λ` itself traces.

**Case B: `κ ∘ σ*` transported.** The same identification carries `κ ∘ σ*` to a
reflection fixing `±i`, which is a member of the #7825 family, so it does select a real
circle. But identifications matching the two pairs form a `ℂ*` (a `U(1)` once both
sides are given round structures). Changing `φ` by the rotation `e` changes the selected
normal by `e n ē` (`conjBy_refl_conjBy`), and by `rot90_normal_axial` no member is fixed
by that. So the selected circle is a function of `arg e`, and **choosing `λ` is choosing
the phase of `φ`.**

Can a further structure fix that phase? It would have to be on both sides:

- **Hermitian form.** `M` carries `i∫ω ∧ η̄`, of signature **(1,1)**. `𝒮_p`'s round
  structure comes from a *definite* form on `ℍ = ℂ²`, so there is no unitary
  identification to demand.
- **Integral or real lattice.** `H¹(E, ℤ)` and `H¹(E, ℝ)` exist on `M`, and nothing
  corresponding exists on `𝒮_p`.
- **Symmetry.** `S₅` acts trivially on `M` by construction. It cannot act faithfully on
  any `ℙ¹` anyway, since the finite subgroups of `PGL₂(ℂ)` are cyclic, dihedral, `A₄`,
  `S₄` or `A₅` (Klein). Even the icosahedral `A₅`, if it acted on the cone (it does not,
  per the corpus), would fix no member of the family: the 3-fold element `ω = 1+i+j+k`
  sends `c j + d k` to `4(d i + c k)` (`conjBy_omegaQ_orthW`, `no_omega_invariant_unit`).

## 4. What is NOT established

- **No map `ℙ(M) → 𝒮_p`**, or any map from Bring data to `𝒮_p`, is derived. Both cases
  are conditional on such a map, and the verdict "does not fix `λ` without a choice"
  holds for *every* such map that matches the distinguished pairs.
- **A map that does not match `{P, P̄}` to `{∓i}`** (for example, one sending both chart
  centres to real points of `ℙ(H¹(E, ℝ))`) makes `κ` a member of the family. But then
  the choice is *which two real points*, an `ℝℙ¹`-worth of data that no corpus structure
  supplies. Again the choice is moved, not removed.
- **Braden–Northover's text is not in `library/`.** That `Aut^±(B) = S₅ × ⟨c⟩`, and
  hence that their involution is some `c ∘ g`, rests on Riera–Rodríguez (held) and the
  rationality of Bring's equations. The claim that all `c ∘ g` agree on `ℙ(M)` is
  representation theory and is not formalized.
- The isometric picture (reflections of the round `S²`) is the model's. A general
  antiholomorphic involution of `ℙ¹` with a fixed circle is conjugate to one of these
  under `PGL₂(ℂ)`, and that conjugation is again an identification choice.

## 5. Owner decisions

None required. **Default:** R1 is answered "no, not without a choice"; `λ` stays free
and covariant (WLOG `λ = 1`, as in #7825). The one optional follow-up is to acquire the
Braden–Northover full text into `library/` and confirm their involution is `c`. That
would not change the R1 verdict, by §2.

## Cross-references

- 6b: draft PR #7825, `PolarizationRealStructure.lean`,
  [`2026-11-15-confinement-universality-readings-and-polarization-real-structure.md`](2026-11-15-confinement-universality-readings-and-polarization-real-structure.md)
- [`2026-07-18-alpha-em-bring-real-structure-grounding.md`](2026-07-18-alpha-em-bring-real-structure-grounding.md)
- [`2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md`](2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md)
- `QOU/Brings/BringConeLinkEulerNumber.lean`, `QOU/BringConeIcosahedral.lean`
