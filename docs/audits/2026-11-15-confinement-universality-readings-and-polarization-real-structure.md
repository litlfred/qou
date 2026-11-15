# Confinement universality: two readings. Polarization: no canonical real structure.

**Date:** 2026-11-15 · **Bean:** `qou-qs2u` (epic `qou-qs0e`) · **PR:** #7825 (draft) ·
**Status:** analysis only. No reading is adopted and no identification is written into
content.

This answers owner items E1 (explore readings (a) and (b) of
`prop:confinement-universality`, without picking one), E2 (check the corpus for an
antilinear involution on `𝒮_p`) and D2.3 (state the dictionary results without choosing
`λ`).

## 1. E1: two readings of `prop:confinement-universality`

### Facts both readings start from (proved or computed on PR #7825)

- **The pair-production stage.** `γ(φ)·γ(ψ)` has six channel coefficients. They are
  integer polynomials in `φ, ψ, h`, recomputed exactly in
  `computations/probes/gamma_gamma_pair_nf_h3_probe.py`; all six match
  `trivial-knot-photon-interpretation-table5-data.md`.
- **At the reference point.** At `φ = ψ = 0` the product is the vacuum `1`, with every
  crossing channel zero (`QOU.Interactions.GammaGamma.pair_vacuum_at_zero`). So the
  chain produces no quark there, and the conjecture's reference value
  `N(0,0,0) = NF(B₃·crossings)` is not the chain's output at `0`.
- **The up channel moves.** The `σ₀` (up-quark) channel depends on `φ`
  (`sigma0_channel_nonconstant`).
- **The confinement stage.** By construction, `B₃ · C(f₁,f₂;σ₀) · C(f₁,f₃;σ₀) · C(f₂,f₃;σ₁)`
  takes only the flavour labels as input (`four-term-pair-nucleon.md`). This is also how
  `DerivedAtom.confinement_universality` is proved: `crossingCoeffsWithPol` discards its
  polarization argument (bean `qou-k6is`).

### (a) Definitional reading

- **What it asserts.** The nucleon NF is a function of `q` and the flavour assignment
  only, and the photon coefficients do not enter the confinement stage. As a theorem
  this is true by construction: the stage-2 word contains no `φ`.
- **What it loses.** It loses the physics reading the block currently gives: *"the
  strong interaction washes out the electromagnetic initial conditions … the categorical
  expression of asymptotic freedom"*. Under (a), nothing is washed out, because the
  photon was never an input to stage 2. The sentence "sweeping `φ₀₁` from `0` to `0.2`
  leaves the proton and neutron NFs unchanged" (`four-term-pair-nucleon.md`) becomes a
  tautology rather than a test. The "for all `φ`" quantifier becomes vacuous, and so does
  the `N(0,0,0)` normalisation.
- **What it keeps.** It keeps a correct, cheap statement, and the corollary that
  anything read off `N_F` cannot depend on the photon
  (`inherited_unit_invisible_of_confinement`).

### (b) Substantive reading

- **What it asserts.** Let `F(φ)` be the flavour assignment the chain produces from
  three γγ collisions, and let `Φ_N = F⁻¹(nucleon flavours)`. Universality is the claim
  that `N` is constant on `Φ_N`.
- **The structural observation.** Once `F` exists and `N = G ∘ F`, constancy on a fibre
  of `F` is automatic. So reading (b)'s content is **not** the independence claim; it is
  the **existence, non-emptiness and geometry of `Φ_N`**, i.e. that the chain can
  produce a nucleon at all, and for which photon states.
- **Is `Φ_N` non-empty, open, or a variety?** This cannot be decided yet, because `F` is
  not defined (bean `qou-usxh`, now owned by sibling 6a). Under the extraction rule
  "an up quark iff the `σ₀` channel is nonzero", the up-producing set is the complement
  of the hypersurface `φ₀ + ψ₀ + hφ₀ψ₀ + φ₀₁ψ₁ = 0`. That set is Zariski-open, and dense
  because the polynomial is not identically zero. The down quark is extracted as the
  typed crossing `σ₀ − ½h_A`, which is **not** one of the six NF channels, so the
  down-producing set is undefined until `F` is. If every condition in `F` is a
  non-vanishing condition, `Φ_N` is Zariski-open, and non-empty iff those polynomials
  have a common non-zero. If `F` also imposes vanishing conditions (for example "no
  electron channel"), `Φ_N` is constructible, and it can be a proper subvariety or empty.
- **What a proof needs.** Three things:
  1. the extraction map `F` (6a);
  2. a computation of `Φ_N` as a constructible set (a finite polynomial problem once `F`
     is fixed);
  3. the factorisation `N = G ∘ F`, which holds by the chain's construction.

### Downstream: who cites the block, and how each reading changes them

| Site | Kind | Under (a) | Under (b) |
|---|---|---|---|
| `knots-particles-confinement/knots-particles-confinement.ts` | chapter manifest | unchanged | unchanged |
| `four-term-pair-nucleon.md`, §Confinement universality | prose restating the claim, with a `φ₀₁` sweep | the sweep is tautological; reword as "by construction" | the sweep must be over `Φ_N`, which is undefined until `F` exists |
| `lean/QOU/Interactions/DerivedAtom.lean`, `confinement_universality` | Lean, definitional (`qou-k6is`) | already reading (a) | must be re-routed through `F` |
| `lean/QOU/Interactions/confinementUniversality.lean` | class + theorem + corollary | the class is satisfied by construction | the quantifier ranges over `Φ_N`, not all of `K³` |
| `molecular-construction/h2o-bond-angle-shift.ts`, authorNote | cites the old "ℝ by meaning" rationale | the rationale is superseded either way (coefficients are ring-generic) | same |
| `index-of-definitions/definition-index.md:485` | index row | unchanged | unchanged |

No block lists `prop:confinement-universality` in `uses[]`. So neither reading breaks a
dependency edge; the changes are to prose and to two Lean statements.

**Default:** nothing changes. The Scope paragraph added on PR #7825 records the
reference-point issue.

## 2. E2: is there an antilinear involution on `𝒮_p` in the corpus?

The six-path check was run for `antilinear`, `anti-linear`, `real structure` and
`complex conjugation`. It covered `docs/audits`, `docs/coordination`, `folio/` content,
`computations/`, `library/INDEX.md` + sections + ocr, and `beans/defs`. Each candidate
the owner named:

| Candidate | Where | Antilinear on `𝒮_p`? | Fixes `λ`? |
|---|---|---|---|
| Bar involution `q ↦ q⁻¹`, `σᵢ ↦ σᵢ⁻¹` | `mass-endomorphism/hecke-baer-star-generic.md` | It is antilinear on `Hₙ(q)` as a ring involution (Baer-*). It is not given as a map on `𝒮_p`. At real `q₀ > 1`, `q ↦ q⁻¹` is not complex conjugation; it coincides with conjugation only for `|q| = 1`. | No |
| CPT / type-B folding | `brings-surface/c-from-color-flavor-swap` (`conj:type-b-folding-cpt`) | It acts on crystal words / colour–flavour labels, not on the polarization line. | No |
| Complex conjugation on `ℙ¹(ℂ)` | `reeb-bundle.md`, `breit-wheeler-vertex.md` | Neither block defines one (grep: no hits). | — |
| Reeb triad's `j` (right multiplication) | model cone, `BringCone.lean` | Antilinear (`rightJ_antilinear`), but **`R_j² = −1`** (`rightJ_sq`): a quaternionic structure, not a real one. On `S²` it is the antipodal map (`hopf_rightJ`), which has no fixed point (`hopf_rightJ_no_fixed`), so it defines no real circle. | No |
| Hermitian form / Frobenius pairing / dagger | `dagger-su2.md`, `lusztig-vs-hermitian-bar-proof.md` | A Hermitian form gives the antilinear map `v ↦ ⟨v, ·⟩` to the dual, i.e. orthogonal complement. On `ℙ¹` this is again the antipode, not a real structure. | No |
| Conjugation by `u = c j + d k` (new, this PR) | `PolarizationRealStructure.lean` | **Yes**: antilinear (`realStr_antilinear`) and an involution (`realStr_involutive`) for **every** unit `u` in the `j`–`k` circle. `u = j` fixes `span(1,j)` (the `λ = 1` linear circle); `u = k` fixes `span(1,k)` (the `λ = i` circle). | **No**: the cone supplies a U(1) family and selects none. The choice of `u` is exactly the choice of `arg λ`. |

**Verdict.** No real structure on `𝒮_p` is fixed by the corpus. The quaternionic
structure the Reeb triad does supply squares to `−1`, so it cannot single out a circle of
real polarizations. Also: the Braden–Northover real structure
(`docs/audits/2026-07-18-alpha-em-bring-real-structure-grounding.md`) lives on
`Jac(Bring)`, not on `𝒮_p`, and nothing in the corpus maps it to `𝒮_p`. That link is
the one remaining candidate; it is untested here.

## 3. D2.3: the dictionary without choosing `λ`

`hopf_dict_rotate`: for a unit complex `e`, the dictionary with `v₂ ↦ ē² v₂` is the
original followed by conjugation by `e`, a rotation about the `i`-axis in the SU(2)
commutant of the Reeb triad. Since `ē²` ranges over all of U(1), **every `λ ∈ U(1)` is
the `λ = 1` dictionary followed by a rotation, so WLOG `λ = 1`, covariantly.** The
rotation acts on chirality gradings by the same conjugation
(`leftMul_conj_chiralGammaU`), so every chirality statement transports.

- **λ-independent, so they stand without a choice:**
  - the eigenline and ray theorems;
  - the orthogonal-pair chirality theorems;
  - transitivity of SU(2) on orthogonal pairs;
  - the H₃ obstruction (`no_automorphism_to_orthogonal_pair`);
  - the QED probe;
  - the axis images `σ₀ ↦ −i`, `σ₁ ↦ +i` (both fixed by the rotation).
- **λ-dependent:** only which real `φ` are linear and which are circular.
- **`|λ|`** is outside U(1). Requiring the dictionary to be an isometry for the
  Hermitian form fixes `|λ| = 1`; whether to require that is itself a choice, and it is
  recorded as such.
- **`φ₀₁`** (degree 2, `L₊`) has no point of `ℙ¹`. Any dictionary covers the degree-1
  part only.
