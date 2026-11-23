# PRE-REGISTRATION — the residual symmetry of the convention-D colour twist (bean `qou-ni4b`)

Date 2026-11-22. Branch `claude/qcd-heat-kernel-beta0-sign-2026-11-22`, PR #9059.
Committed and pushed **before** the probe exists. Not edited afterwards; results go to `RESULT.md`.

## Question

`computations/probes/qcd_colour_full_tower/RESULT.md` (T1) found that on `(ℂ³)^⊗n` with the
Jimbo `U_q(gl₃)` action, convention D (`z_D = q³/(q²+1)`) is realised exactly by a rank-2 diagonal
twist `K` that switches one colour off, and that the twisted trace functional is invariant under
`E₁, F₁, K₁, K₂` only, i.e. `U_q(gl₂) × U(1)`. The owner asks what this residual symmetry means.
It *looks* like SU(2) × U(1). That is speculation until tested; this file fixes the tests first.

Photon (owner ruling 2026-11-20, STRICT): `γ(φ₀, φ₁, φ₀₁) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹`.
Electron (ruling 2026-11-21): `σ₀σ₁σ₀ ∈ B₃`, Hopf-link closure (trefoil `σ₀³` is the backup).
Up quark (ruling 2026-11-20): an unknot strand of the Borromean braid; `def:down-quark`: the same
strand with reversed crossing orientation. So the quark "letters" are single crossings `σ_i^{±1}`.

## 0. Prior art (corpus-grep, 2026-11-22)

- `corpus_search` CLI, `--limit 200`. The combined query "electroweak SU(2) U(1) hypercharge weak
  isospin" returned **0 seeds** (multi-word query; uninformative). Separate queries:
  - "hypercharge": `conj:sm-hypercharge-invariant`, `rem:su5-hypercharge-n3-gate`,
    `rem:flavor-charge-assignments`, `def:strand-twist-datum`;
  - "electroweak": `conj:electroweak-higgs-torus-link-triplet`,
    `thm:ew-triplet-charge-spin-from-involution`, `prop:electroweak-triplet-bring-embedding`;
  - "Weinberg": `conj:weinberg-angle-categorical`, `conj:staircase-ew-residual`;
  - "weak isospin": library only (Furey 2018).
- Grep paths (`folio`, `computations`, `docs/audits`, `beans/defs`):

| item | what it settles for this question |
|---|---|
| `def:coulomb-charge` | `Q = ½(n₊ − n₋)` (halved writhe). Its block says the identification with an electromagnetic charge is **open**. |
| `rem:flavor-charge-assignments`, `conj:sm-hypercharge-invariant` | `I₃` is the writhe coordinate (derived on the nucleon doublet). **Hypercharge `Y` is open**; the writhe is falsified as `Y` (p and n share Y). Ribbon-twist candidate recorded without endorsement. |
| `QOU/QuarkState/OverStrandWeight.lean` (#7971 arc) | At level 2 on `ℂ²`, D **forces** `K = diag(q, q⁻¹)` for its Ř (h on `e₂e₁`); `u = e₁`, i.e. `T³ = +½` under `K = q^{2T³}`. Identification of flavour with the gl₂ weight space is "stated, not derived". |
| `PhotonChargeConservation.no_scaling_of_hecke` | `H_n(q)` admits no U(1) grading scaling `σ`. |
| `PhotonU1NeutralCut` (owner ruling 2026-11-21) | The γγ U(1) is a *linking-count* neutrality on whole braids, not a grading of `H₃(q)`. |
| `rem:su5-hypercharge-n3-gate`, `qou-yk03`, `qou-txc1` | Levels `z_r` are alternatives, not stages; the framework sits at `r = 2`; no construction supplies a level-3 fibre; SU(5)/`3/8` is downstream of an open gate and re-scoped to math only. |
| `conj:weinberg-angle-categorical` | `cot θ_W ≟ q⁻⁴` at the pure pattern; fails the target. Open. |
| `qou-kl39`, `qou-fg1j` | `Y = B − L` cannot be assembled (no state → L map); the writhe ladder matches `I₃`, not `Q` or `Y`. |

Nothing in the corpus reads the D twist's stabiliser `U_q(gl₂) × U(1)` as anything. That is what
this probe adds.

## 1. Tests

All exact over ℚ(q) (sympy) and exact integers. No float, no `q₀`. R and the coproduct are taken
from the T1 probe verbatim (same Jimbo convention and coproduct variant), and the OverStrandWeight
Ř (h on `e₂e₁`) is used as the second convention where stated.

**R1 — branching and forced data.**
- (a) Under the residual `U_q(gl₂) × U(1)` of the support-{1,2} twist, `ℂ³ = ℂ²(colours 1,2) ⊕ ℂ¹(colour 3)`.
- (b) Write `K_D = g · M` with `g` the gl₃ pivotal `diag(q⁻⁴, q⁻², 1)`. Prediction: `M ∝ P₁₂`, the
  projector off colour 3, and `K_D|ℂ²` is the `U_q(gl₂)` pivotal. So the twisted trace equals the
  `U_q(gl₂)` quantum trace on the sub-module `(ℂ²)^⊗n`. Check: that `(ℂ²)^⊗n` is `Ř`-stable, and
  that both traces agree on every `T_w`, `n ≤ 3`.
- (c) U(1) charges. The U(1)s commuting with the residual `gl₂` inside the gl₃ Cartan form the
  2-dimensional span of `diag(1,1,0)` and `diag(0,0,1)`. On a fixed `(ℂ³)^⊗n` one combination is the
  total number `n`, so one U(1) is left mod the centre: `N₃` (the colour-3 occupation number).
  The **forced** datum is the selection rule "D sees only the `N₃ = 0` sector" (`K^{⊗n} N₃ = 0`).
  The **charge values are not forced**: any `a·n + b·N₃`, with `b ≠ 0`, is equally the U(1). The traceless
  (sl₃) representative `diag(1,1,−2)` is recorded as one convention, not as a derived charge.
- (d) Orientation cross-check against OverStrandWeight. The doublet twist should be `∝ diag(q⁻¹, q)`
  under the T1 Ř (h on `e₁e₂`), and `∝ diag(q, q⁻¹)` under the OverStrandWeight Ř (h on `e₂e₁`).
  So "which doublet member carries `K = q`" is tied to the Ř convention.

**R2 — commutation and charges of particle words.**
- (a) `N₃` (and each gl₃ Cartan element, via its coproduct) commutes with `Ř` on `(ℂ³)^⊗n`, `n ≤ 3`.
- (b) The twisted trace commutes with it: `tr(K^{⊗n} [N₃, x]) = 0`, and `tr(K^{⊗n} N₃ x) = 0` for all `x`.
- (c) The adjoint U(1) charge `[N₃, ρ(w)]` of each word, on `(ℂ³)^⊗3`: the photon
  `1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹` (φ symbolic), the electron `σ₀σ₁σ₀`, and the quark letters
  `σ₀^{±1}, σ₁^{±1}`. **Prediction: 0 for every word**, because `ρ(H_n)` and `U_q(gl₃)` are
  mutual commutants (Schur–Weyl). That would mean the U(1) labels *states* (colour vectors), never
  braid words; it would not contradict `no_scaling_of_hecke`. Record the D-trace of each word as data.
- Assigning a colour state to a corpus particle is not attempted. The corpus does not fix one, and
  choosing one to produce a target charge would be selection.

**R3 — which colour is switched off.**
- (a) Over all three rank-2 supports {1,2}, {1,3}, {2,3}, test invariance under `E₁, F₁, E₂, F₂, K₁, K₂`
  and the non-simple root vectors `E₁₃ = E₁E₂ − c·E₂E₁`, `F₁₃ = F₂F₁ − c·F₁F₂` (solve for `c`).
- Prediction: {1,2} keeps the α₁ root sl₂ and {2,3} keeps α₂. For {1,3}, `M = g⁻¹K ∝ diag(q, 0, q⁻¹)`
  is not a projector, so the prediction is the Cartan only (no root `sl₂`).
- (b) All three give the same trace on `H_n` (same Schur weights, already in T1). So no `H_n`
  observable can tell them apart.
- Classification to report: the choice is **not forced** by `H_n`. It is invisible to every
  Hecke-side observable, and visible only in which colour subalgebra survives. Picking {1,2}
  (simple root, largest stabiliser) is a **selection**, and is flagged as one.

**R4 — charge ratios (coincidence checks, declared in advance as NOT evidence).**
- Report any exact ratio the residual algebra produces. The traceless U(1) `diag(1,1,−2)` gives a
  ratio of −2 between the singlet and doublet charges. This is forced by sl₃ tracelessness on any
  2+1 split; it is the same arithmetic as flavour hypercharge `(1/3, 1/3, −2/3)`.
- A match to 1/3, 2/3 or to `Q_u/Q_d = −2` is therefore a **coincidence check, not evidence**. No
  Weinberg angle is expected: there is a single algebra and no relative coupling is fixed. Test
  whether any normalisation-free mixing ratio exists; the prediction is none.

## 2. What would change the reading

- The residual reads as electroweak only if the twist **forces** (i) a U(1) charge normalisation,
  (ii) a nonzero charge on corpus particle *words*, or (iii) a parameter-free mixing ratio.
- Predicted outcome: none of the three. Then the residual is the stabiliser of a colour-breaking
  twist, a subalgebra of colour `U_q(gl₃)`. Standard-Model SU(2)_L × U(1)_Y commutes with colour, so
  a subgroup of colour is not it. That is a reading argument, stated as such; it is not a proved
  invariant.

## 3. Rules

- No fitting, no selection against targets, `q₀` not used. The gluon stays open.
- Negatives are scope (a) unless a proved invariant (Schur–Weyl commutant, centre commutativity)
  excludes them.
