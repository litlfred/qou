# The lepton two-term trace, derived from the Lagrangian and non-abelian Stokes (2026-11-21)

Bean `qou-99qc`. PR #8743. Pre-registration: [`PREREGISTRATION.md`](../../computations/probes/lepton_two_term_stokes/PREREGISTRATION.md) (commit `e4ad92f18d`, before any number).

**Owner, 2026-11-21**, on #8707's question (full braid group vs colour-preserving braids once a lepton strand is present): *"The two term came out from looking at the Lagrangian and tracking through non-abelian Stokes. Do the same for the lepton."*

## Answer

**The derivation settles the covariance question.** The Stokes step carries the charge insertion through every crossing of the closed boundary word. So the insertion must be carried through every crossing that occurs, with each strand's charge moving with the strand. For β words that includes quark–lepton crossings. So the group is the **full braid group on all strands, with species carried along**, which is neither of #8707's two readings:

- The pairs-only insertion `Σ_{a<b} Q_aQ_b` (the 16:44-ruled object) is carried at every quark–quark crossing and at **no** quark–lepton crossing for `q² ≠ 1` (Lean `pairOnly_quark_lepton_not_carried`; probe 0/6). So it is not admissible once a lepton strand braids with the quarks. This is a structural exclusion (b) within the class of species-weighted quadratic charge insertions. The invariant is the carry identity `quad_carry_iff`.
- The carried insertions form the family `(β/2)Q_tot² + κ Σ_a Q_a²/y_a`. Keeping the ruled nucleon object fixes `κ = −β y_q/2`, which forces a lepton self-term: the derived lepton two-term insertion is **`β·(Σ_{all pairs} Q_aQ_b + (2/3)Q_ℓ²)`** (Lean `lepton_self_weight_forced`, `natural_family_lepton`). On three quarks it is exactly the ruled all-pairs insertion (`natural_family_nucleon`).
- Every member of the family depends only on `T³_tot` and the species content (`natVal_eq_totals`). So it is a scalar on every total-weight space. Its **connected part is 0 on every word** (`connected_zero_of_scalar`; probe: 91 route quantities, exact zeros at q = 2 and 3/2, ≤ 2.4e-71 at q₀). It also takes the **same value on `n⊗ν` and `p⊗e⁻`** (`natural_beta_split_zero`; both `−β/3`).

**Consequence.** The scored two-term (connected) equals the one-term on every β route: P1/P4 (all ten words, both photon points), P2 families A and D, N2, route L. The two-term trace contributes **nothing** to `Q_β` and creates no new n/p separation. This agrees numerically with #8707's colour-block reading (also connected 0). It disagrees with the H_N reading, whose non-zero values (`h/3`, P4 `D = 0.00869` on W0, P2 `t₂/t₁ ≈ 0.04`) come from projecting a *positional* charge that the lepton strand does not carry. The Lagrangian produces no such projection.

## 1. The nucleon chain, step by step

| step | what produces it | status |
|---|---|---|
| Two terms `ħ_q²·τ(ι_ξ∇)²` (QCD) + `ħ_q·τ(ψψ̄ ι_ξ∇)` (QED) | `ℒ = 𝒟² + ψ̄𝒟ψ`, `𝒟 = q⁻¹∇ + ħ_q ι_ξ∇`; `CategoricalLagrangianTwoTermBridge.lagrangian_five_term_expansion`, `trace_lagrangian_two_term_split` | **derived** (sorry-free) |
| QCD term = trace of the boundary word | non-abelian Stokes, `reeb_holonomy_leftTrace_eq_functional_hol` with the Stokes realisation as hypothesis `hStokes` (Yekutieli cited; chain step 2 "algebra proved, geometry asserted") | **derived modulo the asserted Stokes geometry** |
| **(a) pair structure** | the matter Reeb trace evaluated as a charge insertion on the boundary word: hypothesis `hMatReeb*` in the bridge; Gap 1 (`trace_matter_reeb_*_six_crossing_sum`) places one insertion per letter, i.e. the charges of the two strands meeting at each crossing | **entered as a hypothesis** (adjacent in #8518). The all-pairs set is what the Leibniz square gives (§2, `sq_total_three`) |
| **(b) charge insertion** `Q_aQ_b`, `Q = T³ + Y/2` | `NeutronProtonEMSign.chargeStructure` (corpus charges) | **derived from corpus charges** |
| **(c) covariance group** | insertion must commute with the crossing generators so the trace is a braid function (#8552 T1/T2/T6); owner ruling 2026-11-20 16:44 chose the covariant all-pairs `Q₁₂+Q₂₃+Q₁₃` | **owner-ruled** (option 2), justified by the carry principle |
| weighting | convention-D Markov trace = quantum trace `Tr(K^{⊗n}·)/[2]_q^n` (`qtrace_crossing_eq_zD`) | **derived** (given convention D, itself ruled) |
| **(d) connected subtraction** | per-weight-space mean removed (`deltaT_allPairs_connected_eq_zero`); the 16:44 ruling scores it | **owner-ruled** (raw vs connected was a selection before the ruling, #8524) |
| coupling scale `c_em` | `m_e` / `E₀` / `α_bind` | **selected** (#8524); never derived |

## 2. The same chain with a lepton strand

**Premise L (owner-undecided):** the lepton doublet `(ν, e⁻)` is a `C²` strand braided by the same Jimbo `Ř`, with `Q = T³ + Y/2`, `Y_ℓ = −1` (ν 0, e⁻ −1); quarks `Y_q = 1/3`.

- **(a) Pairs.** The Reeb contraction on a tensor product is additive (Leibniz rule; the contracted form passes the other factor by naturality of the braiding with the unit). So the charge is `Q_tot = ΣQ_a`. Its square has every pair with weight 2 and no species distinction: three quark–quark pairs, three quark–lepton pairs, and lepton–lepton pairs if there are several lepton strands (`sq_total_four`).
- **(c) Covariance.** Under Stokes the insertion is carried round the closed boundary. Basepoint independence requires it to be carried through every letter, with species moving with the strand. On one crossing (`diag_carry_iff`, `quad_carry_iff`), with strand data `(α_a, y_a)` for self-weights and `β` for the pair:

  `α₁Q₁² + α₂Q₂² + βQ₁Q₂` is carried  ⇔  `h·((2α₁ − β)y₁ − (2α₂ − β)y₂) = 0`,  `h = q − q⁻¹`.

  With a spectator strand of non-zero charge, the pair weights must agree (`pairWeight_uniform`). So for `h ≠ 0` the carried class is `(β/2)Q_tot² + κ Σ Q_a²/y_a`.
- **Pairs only fails at the mixed crossing**: `h·2β·(y_q − y_ℓ) = h·(8/3)β ≠ 0`.
- **A charge-0 "neutral" doublet** (#8707's colouring B) is **not admissible**: a strand braided by `Ř` must carry `T³` in its charge (`singleCharge_not_carried`; probe A5). Only colouring A (photon-pair strands as leptons) survives.
- **(d) Connected part.** Every carried member is a scalar on each `W_m`, so the connected part vanishes for every word. This is what makes the derived answer independent of `κ`, `β` and `c_em`.

**Alternative reading L′** (lepton not braided with the quarks, e.g. a spectator factor): no quark–lepton crossing occurs, so the carry condition is only imposed at same-species crossings. Pairs-only is then admissible, and it is constant on joint quark/lepton weight sectors (#8707 colour-block, Lean `pairSum_union`). Its connected part is again 0 on every word. **Both readings give scored two-term = one-term on every route.** They differ only in the unscored raw part.

**Electron ruling (2026-11-21: electron = σ₀σ₁σ₀ ∈ B₃).** If the lepton is several strands, lepton–lepton crossings have equal `Y` and are carried by the whole family (probe: `nat` and pairs both carried at ℓ–ℓ). The conclusion is unchanged.

## 3. Numbers (probe `lepton_two_term_stokes_probe.py`, 15/15 pass; witness `lepton-two-term-stokes.witness.json`)

Exact in `ℚ(q)` (zeros tested at q = 2, 3/2), at proton `q₀ = 1.10997858275138080759…`, 70 dps. The `q → 1` order is estimated from exact values at `1 + 10⁻³`, `1 + 10⁻⁴`. Words are #8707's, verbatim. `β = 1`, `κ = −1/6`.

| quantity | derived two-term (scored, connected) | one-term / comparison |
|---|---|---|
| P1/P4, 10 words × 2 photon points: `t₂` | **0 exact** | `t₁(W0) = 0.998562`, `t₁(W7) = 0.209839` |
| P4 `D` (n⊗ν − p⊗e⁻ sector), every word | **0 exact** | one-term `D`: W1 0.142082 O(q−1), W7 0.0830024 O(q−1), W0 0 |
| P2 family A (9 words), D (12 words), p and n | **0 exact** | — |
| N2 V1V2, V2V1, V1V1V1 | **0 exact** | — |
| route L balances | **move by 0** (functions of the above) | — |
| β insertion values `n⊗ν` / `p⊗e⁻` | `−1/3` / `−1/3` (split 0) | pairs-only `−1/3` / `−1` (split 2/3, #8704) |

Unscored raw part, comparison only (`κ`-dependent, not a prediction): P4 `D_raw` W1 0.0660316, W7 0.0385749, W0-Borromean 0.00414787 (O((q−1)³)); P2 A `(j,k)=(0,0)` `t₂^raw/t₁` p 1.04465, n 1.07097. CODATA `Q_β = 0.78233 MeV` appears only as comparison. No `c_em` is chosen and nothing was selected by a residual.

## 4. Is anything left to decide?

The covariance group is not a choice: it is forced, and it is the full braid group with species carried. The scored object is fixed by the 16:44 ruling plus the carry condition, and its value (0) does not depend on any remaining parameter. Two things stay open. Neither changes a scored number, so neither is put to the owner here:

- **Premise L vs L′** (is the lepton a braided strand?). Both give 0 for the scored two-term. The premise matters elsewhere (P1/P2/P4 one-term routes), which is where it is already tracked.
- **The raw part's `κ`.** It is fixed by the nucleon ruling (`α_ℓ = 2β/3`), but it only enters unscored raw rows.

If nothing is decided: the two-term rows for β stay equal to the one-term rows. #8707's H_N columns should be labelled as a non-carried (inadmissible) comparison. My judgement is that #8707 should adopt this result in place of its "owner decision" framing.

## Scope

- (b), within the class of species-weighted quadratic charge insertions (diagonal in the weight basis, quadratic in the strand charges), under premise L: pairs-only excluded at quark–lepton crossings; charge-0 doublets excluded. Invariant: `quad_carry_iff`, `singleCharge_not_carried`.
- Not excluded: non-diagonal insertions; insertions of charge degree > 2; a non-central (electroweak-mixed) photon coupling (cf. `2026-11-20-two-term-qed-derivation.md` §7.4); any derivation of `c_em`.
- The Stokes realisation itself (`hStokes`, `hMatReeb*`) is still a hypothesis in the corpus Lean. This tranche uses the carry principle it implies and does not prove that geometry.

## Verification

- Lean `QOU/QBeta/LeptonTwoTermStokesCovariance.lean`: `lean -DautoImplicit=false -s 65536` exit 0 against the Mathlib oleans; `#print axioms` on all 24 theorems gives `[propext, Classical.choice, Quot.sound]`, with no `sorryAx`. No `sorry`, `native_decide` or `axiom` in the file. Generic `[Field R]`. Where `1/2`, `1/3` matter, `(2 : R) ≠ 0` and `(3 : R) ≠ 0` are hypotheses.
- Probe: 15/15. It checks the engine against `t₁(σ) = z_D` at each exact field. Engine and words are copied verbatim from #8707 (`two_term_engine.py`, `beta_routes_words.py`).
