# Two-term QED: is there a derived second term? (2026-11-20)

Owner instruction, 2026-11-20 15:00: *"Derive to make two-term primary."*

Today the two-term QED correction is primary on the L2 scorecard only because the owner ruled it so. The term it uses is a selection: the adjacent quark pairs 1-2 and 2-3 are kept, 1-3 is dropped, and the `m_e` scale is chosen (`canonical_mass.proton_qed_self_energy_borromean_mev`, bean `qou-99qc`). This audit asks whether a derived term exists, and where any proton-only term would have to put `q₀`.

**Verdict.** No derived two-term exists in the classes formalised here. Every covariant term through Vassiliev degree 3 vanishes on `V³` or does not depend on the braid at all. Separately, and whatever the term is: a correction that acts only on the proton identity cannot fix `m_μ` without breaking `α_em⁻¹`, because the `α_em` form-B tower pins `q₀` within 0.053 ppb of the proton pin. That evidence puts the μ–p residual in the **muon** relation, not the proton one. So two-term cannot be made primary as a derivation on the proton side. A derived term, if one exists, has to correct the muon carrier (bean `qou-6gf9`).

**Update (same day, owner: *"Keep trying to derive and lean prove"*).** §7 derives `c₃` and the degree-0 coefficients `k₁, k₂` along the route the owner named: colour the three strands by `U(1)` charges and expand the coloured invariant. In that class all three are **exactly 0**, at every order, for proton and neutron. So the derivation produces no two-term correction; the scorecard is the one-term scorecard (§7.3).

Lean: [`QEDHigherOrderCovariance.lean`](../../folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/QEDHigherOrderCovariance.lean), 28 theorems. Probe: [`two_term_qed_derivation_joint_pin_probe.py`](../../computations/probes/two_term_qed_derivation_joint_pin_probe.py), witness `two-term-qed-derivation-joint-pin.witness.json` (5/5 assertions pass).

This builds on PR #8552 (`NucleonQEDCovariance`, the commutant of the crossing action) and PR #8557 (`CrossingCovariantQED`, the first-order local insertion). Neither is on `main`, so this file imports only `NucleonWeightSpaceTwoTerm` and `BorromeanPairwiseLinking` and redefines the small amount of shared vocabulary it needs.

## 1. Second order and beyond: the local class, exactly

**Setting.** Read the braid word letter by letter and carry the strand labels along. Each letter that exchanges strands `{a,b}` is replaced by an arbitrary element of the algebra its own crossing generates, `σ ↦ x_{ab} σ + y_{ab}`. That is every element of `span{1, σ}`, with no expansion in a coupling, so the statement holds at every order.

**Theorem `exact_local_covariant`.** Require all `x ≠ 0`, `q² ≠ 1`, `2 ≠ 0`, and the braid relation for the six labellings. Then `y_{ab} = t · x_{ab}` for one `t` common to all three pairs, with `t = 0` or `t = −(q − q⁻¹)`.

- `t = −h` gives `x σ⁻¹`, the mirror.
- The branch connected to the identity is `t = 0`: a per-pair **scalar rescaling** `σ ↦ u_{ab} σ`.

The proof uses only the `(0,1)` entry of the defect (`defect3_01`) for two labellings per pair. Their sum and difference give `h(t_i + t_j) + 2 t_i t_j = 0` for every two pairs, and `ratios_core` solves that system. For uniform coefficients there is a closed form: the defect is `x y (x h + y) • (σ₁ − σ₂)` (`defect3_uniform`). The negative control `defect3_uniform_ne_zero` shows that a generic `(x, y)` breaks the braid relation.

**Theorem `facU_borromean` / `trace_defWordU_borromean`.** With `σ^e ↦ u_{ab}^e σ^e`, the deformed `V³` equals `(Π u_{ab}^{e}) • V³`. On `V³` the letters exchange `{0,1}, {0,2}, {1,2}, {1,0}, {2,0}, {2,1}` with alternating signs, so the product is exactly `1` for any symmetric `u` with no zero values. The trace is therefore unchanged **at every order** of any series `u_{ab}(ε) = 1 + εα + ε²β + …`. In particular the second-order (two-insertion) coefficient is `0`, for proton and neutron alike. Control: on the Hopf word the factor is `u₀₁²` (`facU_hopf`).

This extends #8557's first-order result (the coloured writhe) to all orders. The first-order coloured writhe is the logarithm of this factor.

## 2. The naive photon-exchange double sum

The textbook two-vertex object is `D = Σ_{c<c'} w_c w_{c'}` with `w_c = e_c Q_a Q_b`.

- `two_D_add_sq`: `2D + Σ w_c² = S²`, where `S` is the coloured writhe.
- `doubleSum_r2_borromean`: prefixing the cancelling pair `σ₁σ₁⁻¹`, which is the identity braid, shifts `D` by `−(Q₀Q₁)²`. So `D` is **not** a braid invariant.
- `doubleSum_completion_borromean`: the completion `D + ½Σw²` equals `S²/2 = 0` on `V³`.

Exact values on `V³` (probe, `Fraction`):

| | `S` | `Σw²` | `D` | shift of `D` under `σ₁σ₁⁻¹·` |
|---|---|---|---|---|
| proton `(2/3, 2/3, −1/3)` | 0 | 16/27 | −8/27 | −16/81 |
| neutron `(2/3, −1/3, −1/3)` | 0 | 2/9 | −1/9 | −4/81 |

The nonzero `D` changes with the presentation of the braid, so it cannot be a derived term.

## 3. The Milnor channel at order α

A covariant coupling to `μ̄₁₂₃`, which changes sign under any transposition, needs a charge weight that also changes sign under every transposition. `quad_alternating_eq_zero` shows that every such weight of degree `≤ 2` is **identically zero**, not merely zero on repeated charges. Order `α_em` is quadratic in charge, so the Milnor channel is empty at order α. The first alternating polynomial is the cubic Vandermonde `(Q₁−Q₂)(Q₁−Q₃)(Q₂−Q₃)`. The negative control confirms that it is not identically zero, but it vanishes on both nucleons (`alternating_vanishes_on_pair`). What survives is the even, degree-4 `c₃ Q₁Q₂Q₃ μ̄²` of #8557, with `c₃` not derived (bean `qou-qc3d`).

## 4. What survives: degree 0, the scale question

Everything covariant up to degree 3 is braid-independent on `V³`. That leaves the degree-0 charge-symmetric quadratic `k₁ ΣQ² + k₂ Σ_{a<b} Q_aQ_b`. It takes the value `k₁` on the proton and `(2/3)k₁ − (1/3)k₂` on the neutron (`degreeZero_values`; main already carries `QSelfP = 1`, `QPairP = 0`, `QPairN = −1/3`).

**How it enters the QCD functional.** The canonical identity, from `m_p_substrate_identity_50dps.py` behind the `canonical_mass` facade, is

    m_p = 2 m_μ |tr_M(β_Bor)| [3]_q! / q³ − 12 m_e,   m_μ = m_e Vol(4₁)/ℏ_q².

A scalar insertion `(1 + a)` on the trace shifts the proton by exactly `a · 2 m_μ |tr_M| [3]!/q³` (`scalar_insertion_shift`). The multiplier is the whole F_Bor term, 944 404.08 keV at the proton pin. No separate electromagnetic scale appears anywhere in the functional: the only thing that multiplies the QED trace is the QCD term itself.

The relative coupling a proton-only scalar would need to close the μ–p gap is **a = 2.4228e-7**. That is a 0.2288 keV shift. The figure is a requirement, not a derivation, and it is **not** compared with α, α², α³ or any other candidate: picking among them by residual would be selection against the target. The coefficients `k₁, k₂` are not derived (bean `qou-bn8e`, intra-nucleon EM self-energy magnitude).

The scalar is also degenerate with `q₀` on the proton alone. The proton mass fixes only one combination of `a` and `q₀`.

## 5. The joint pin, independent of any QED term

`mp.dps = 70`, CODATA 2022 from the registry, `q` solved from the corpus's own closed forms:

| pin | `q` | Δq vs proton (ppb) | `m_p` resid (ppb) | `m_μ` resid (ppb) | `α⁻¹` form-B resid (ppb) |
|---|---|---|---|---|---|
| proton identity | 1.10997858275138080759… | 0 | 0 | +211.206 | −0.365 |
| muon identity | 1.10997859564273904668… | +11.614 | −243.860 | 0 | **+78.998** |
| α_em form B | 1.10997858281070609712… | +0.0534 | −1.122 | +210.234 | 0 |

Sensitivities at the proton pin: `d ln m_p/d ln q = −20.997`, `d ln m_μ/d ln q = −18.185`, `d ln α⁻¹/d ln q = +6.833`, and the Form-A `d ln Q_β/d ln q = −2.597`.

**The finding.** The `α_em` derivation and the proton identity agree on `q₀` to 0.053 ppb. The muon identity sits 11.6 ppb away. A proton-only correction can only move `q₀` along the line between the proton and muon pins. It can satisfy `m_μ` only by moving `α⁻¹` to +79 ppb, about 515 σ_α. No single `q` satisfies `m_μ` and `α_em` together under these forms.

`#8554` reports the same tension at its exact two-term pin: `m_μ` 8.06 ppb, `α⁻¹` +75.97 ppb. That is a point on this line near the muon end.

**Q_β, m_n, Δ_pn.** If a proton term holds `m_p` at CODATA, moving to the muon pin changes `Q_β` by −30.2 ppb (Form-A sensitivity, used as a proxy for the ruled base). That changes `m_n` by about 0.025 ppb and `Δ_pn` by about 18 ppb. The scorecard misses on these rows are of order 10⁸ ppb, so the pin choice does not affect them. They are not affected by anything in this audit.

**Scope.** This is (a): it is conditional on the `α_em` form-B tower. That tower is structurally motivated but not derived: its Schwinger factor is not derived, and `α_em` is conditional on the Witten-κ Gram `sorry`. If form B is replaced, the conclusion has to be re-measured. The probe re-runs in seconds.

## 6. Scope of the exclusions (AGENTS.md (a)/(b))

- §1: structural (b) **within the class** of local insertions valued in `span{1, σ}`. The cited invariant is the braid relation, proved for all orders.
- §2: about the specific double sum written. Not every bilinear non-local functional is excluded.
- §3: structural (b) for polynomial charge weights of degree ≤ 2.
- §5: (a), conditional on `α_em` form B.
- §7: structural (b) within the central-`U(1)` colouring class (`c₃ = k₁ = k₂ = 0`).
- Not excluded: the even degree-4 `c₃ μ̄²` term from a non-central photon coupling; non-local insertions outside §2; a correction to the muon carrier `Vol(4₁)/ℏ_q²`, which is where §5 points.

## 7. Deriving `c₃` and `k₁, k₂` from the `U(1)`-coloured invariant

**Setting.** Give strand `a` the charge `Q_a` of a central `U(1)` (the photon direction of `𝔲(1) ⊕ 𝔤`). On `V_{Q_a} ⊗ V_{Q_b}` the `U(1)` R-matrix is the scalar `t^{Q_aQ_b}`, so each letter `σ^e` becomes `t^{eQ_aQ_b} σ^e`. The closure adds the ribbon twist `θ^{Q_c² w_c}` for each component `c`, where `w_c` is the self-writhe of `c`. `t` and `θ` are arbitrary units; expanding them as `e^{ε·…}` gives every order of the coupling at once.

### 7.1 The result (Lean §U, sorry-free)

- `finalPos_borromean`: `V³` is a pure braid, so each strand closes on itself and the three components are the three labels.
- `selfW_borromean`: each component has self-writhe `0`. Every crossing of `V³` is between two different components.
- `u1Trace_borromean`: the coloured trace equals `tr(V³)` for every `t`, `θ` and every integer charge assignment. `u1Trace_borromean_charge_independent` says the same thing as a statement of independence from the charges.

So the coloured value is a constant function of `(Q₀, Q₁, Q₂)`. Every charge monomial therefore has coefficient `0`. That includes the cubic `Q₀Q₁Q₂` multiplying `μ̄²` (this is `c₃`, bean `qou-qc3d`) and the self-energy `ΣQ²` and `ΣQ_aQ_b` (these are `k₁`, `k₂`, bean `qou-bn8e`).

**Why `k₁ = 0` here.** In this class a single charged strand contributes through two things only. The ribbon twist is `θ^{Q²w}` with `w = 0` on `V³`. The quantum dimension of a one-dimensional `U(1)` representation is `1`. So neither produces a self-energy. A nonzero `k₁` would have to come from a framing other than the blackboard framing of the braid closure, and choosing that framing would be a choice, not a derivation.

**Controls**, both of which fail as required (negative-control `decide` runs are rejected by Lean):

| word | proton `t`-exponent | proton `θ`-exponent | neutron `t`-exponent | neutron `θ`-exponent |
|---|---|---|---|---|
| `V³` | **0** | **0** | **0** | **0** |
| Hopf `σ₁²` | 8/9 | 0 | −4/9 | 0 |
| `σ₁³` (two strands merge; self-writhe 3) | 4/3 | 4/3 | −2/3 | 4/3 |

(The `σ₁³` row is a mechanism check only. Its merged component carries two different charges in the neutron labelling, so it is not a physical neutron.)

### 7.1a The canonical photon form (Lean §P)

Owner ruling 2026-11-18, re-confirmed 2026-11-20: the canonical photon is `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹`, and `β_Bor = γ(0,0,qh)·γ(0,0,−q⁻¹h)`. Writing `X = σ₀σ₁⁻¹`, the product is `1 + h²X − h²X²`.

`photon_product_eq_borWord` proves that on the proton weight space this equals the word `V³ = X³`. So §7.1 is a statement about `β_Bor` in the ruled form. Nothing in §1–§7 uses the superseded `σ₀σ₁` photon, so no result depends on it. Negative control: flipping the sign of the second coefficient breaks the identity (Lean refutes the `(0,0)` entry at `q = 2`).

**The colouring acts on the braid, not on the terms of the expansion.** The terms `X` and `X²` are 3-cycle words. Each closes to a single component, which cannot carry the three different charges of `uud`. So colouring the photon expansion term by term is not defined for the nucleon. The only consistent colouring is the one on the pure braid `V³`, and that is the one §U computes.

### 7.2 The reason (Lean §K)

In the Kontsevich-integral picture, `log Z` is a sum of struts, which are weighted by linking numbers and framings, and connected trivalent graphs. The tree `Y` among these carries `μ̄₁₂₃` (Habegger–Masbaum). A trivalent vertex is weighted by `B(x, ⁅y, z⁆)`.

- `tripod_central_leg_zero`: for an invariant form `B`, any vertex with a central leg has weight `0`.
- `tripod_single_direction_zero`: a vertex with all three legs along one direction has weight `0` for every Lie algebra, central or not.
- Negative control `tripod_noncentral_nonzero`: the `𝔰𝔩₂` vertex `tr(H⁅E,F⁆) = 2 ≠ 0`.

So a central `U(1)` reaches the invariant only through struts, which on `V³` are all `0`. The full factorisation `Z^{𝔲(1)⊕𝔤} = exp(½ħ QᵀLQ) · Z^𝔤`, with `L` the framed linking matrix, is cited (Bar-Natan 1995; Habegger–Masbaum 2000). It is not formalised here; §U proves its consequence on `V³` directly at the Hecke level.

### 7.3 Joint check at the derived value

The derived correction is `0`, so the derived two-term pin is the proton-identity pin and every row is unchanged. From the probe (70 dps):

| row | value at the derived pin |
|---|---|
| `m_p` | 0 ppb (this is the pin) |
| `m_μ` | +211.206 ppb (970× the 100× target) |
| `α⁻¹` form B | −0.365 ppb |
| `Q_β`, `m_n`, `Δ_pn` | unchanged (the dashboard values, which miss by ~10⁸ ppb) |

Nothing was tuned. The μ–p residual is untouched, which is consistent with §5: it is not a proton-side term.

### 7.4 Scope

This is (b) **within the class** "central `U(1)` colouring": a charge-diagonal R-matrix together with the ribbon twist. The invariants cited are that `V³` is a pure braid, that its self-writhes are `0`, and that a central leg kills a vertex. Two things are outside the class and are not excluded:

- a **non-central** photon coupling, where the photon direction does not commute with the algebra the strands carry (an electroweak-mixed `𝔲(2)` is the standard example);
- non-local functionals outside §2.

Only these can give `c₃ ≠ 0`. The tripod lemma already rules out the pure `Q₀Q₁Q₂` vertex along a single direction even there. A nonzero `c₃` would need mixed legs, and so a non-abelian structure constant pairing the photon direction with another generator.

**Can two-term now be primary as a derivation?** No. The route the owner named derives the two-term correction to be exactly `0`.

## Open gaps

- `qou-qc3d`: `c₃ = 0` is now **derived** in the central-`U(1)` class (§7). It stays open for a non-central photon coupling, which is the only class left that could give a nonzero `c₃`.
- `qou-bn8e`: `k₁ = k₂ = 0` is **derived** in the central-`U(1)` class with blackboard framing (§7). A nonzero value needs a self-energy from outside that class.
- `qou-6gf9`: a correction to `m_μ/m_e = Vol(4₁)/ℏ_q²`. §5 is new evidence that the μ–p residual belongs here rather than on the proton.

## Verification

- `lean -DautoImplicit=false -s 65536` on the file: exit 0. The olean cone was `NucleonWeightSpaceTwoTerm` and `BorromeanPairwiseLinking`, restored read-only.
- `#print axioms` on all declarations checked (the 17 original and the 10 added in §U and §K), with the four combinatorial ones axiom-free: `[propext, Classical.choice, Quot.sound]`, with no `sorryAx`.
- Negative controls, both of which fail as required: the Hopf factor is not `1`, and the Vandermonde cubic is not identically `0`.
- Probe: mpmath at 70 dps and exact `Fraction`, with no float on any value path.
