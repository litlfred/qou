# Gap study: running α_s, β₀, string tension, Λ_QCD in qou (2026-11-22)

Owner, 2026-11-22: *investigate the gaps — running α_s, β₀, string-tension value, Λ_QCD.*
This is a **gap analysis**, not a derivation. Nothing here is computed beyond the one
evaluation in §1.3, nothing is wired, no bean is created, and no gluon is selected (the
step-4 gluon stays open, owner ruling 2026-11-22).

Inputs: `CORPUS-GREP-gluon-dynamics.md` (the six-path inventory, commit 874db75007e) and
`LITERATURE-COMPARISON.md` §47–§50. Branch `claude/mn-own-identity-2026-11-21`. Every file
reference below was opened on this checkout. Every bean was read on the `beans/defs` mount
(5875 beans).

## 0. The decision, in two sentences

Each of the four quantities needs **two objects qou does not have**: (i) a **scale
variable** along which a coupling can run, and (ii) a **non-abelian colour action on qou's
own state space** that fixes the sign and size of the running (C_A). The second object is
already an open gap (bean `qou-ni4b`). The first has never been named as a gap. So the
first decision is whether to open a bean for the scale variable. Every route to a number
for α_s(μ) or Λ_QCD passes through it, and the routes that skip it are all fits or
selections.

**Recommendation (judgement, not a finding):** open the scale-variable bean (B1 in §6) and
the β₀ bridge bean (B2). Leave α_s and Λ_QCD as values blocked behind them. Do not attempt
a string-tension value until a Wilson-loop object exists (B3). §5 gives the reasons.

**Default if the owner does nothing:** nothing changes. `qou-5iaz` and `qou-ni4b` stay
open. `sm-params-gauge-couplings.md` keeps *"α_s | open"*. No number is at risk, because
none of the four quantities is wired anywhere (corpus grep #1, #2, #11, #13).

## 1. Running α_s(μ)

### 1.1 What the corpus has nearest to it

| object | where | what it is | why it is not α_s(μ) |
|---|---|---|---|
| `1/α_s = q^p·[9]_q`, p a free parameter (`p + p' = 1`) | `computations/alpha_k_selection_rule_conditional.py` (docstring, rule 3); `docs/audits/2026-09-03-sm-26-term-status.md` §4.3 | a per-channel split of `1/α_EM = q[9]_q[10]_q`. Only the product `α_s·α_W = α_EM` is invariant. Conditional on `conj:e-hartree-categorical-derivation`. | p is undetermined. It has no scale. The channel `(2,1,1)` ↔ `T(2,9)` is a 2-strand carrier with no `l = 3` block (`docs/audits/2026-10-10-level3-su3-channel-test.md` row 2). |
| `α_s(M_Z) = q⁻¹/[7]_q` | `docs/beta-decay-handoff.md` (March 2026), reported in sm-26 §4.3 | a fit-shaped closed form | It names `M_Z` but has no mechanism that attaches `M_Z`. Bean `qou-5iaz` forbids wiring it. Under §NO FITTING it is selection against the target. |
| bean `qou-5iaz` (in-progress) | beans | GAP: no coupling extraction; three attack options (trace ratio; Λ via confinement / CAL-3; asymptotic freedom as q-CLT flow) | All three are blocked on `qou-ni4b` (SU(3) action) and `qou-lxh5`. |
| bean `qou-ni4b` (in-progress) | beans; `lean/QOU/StandardModel/ThreeStrandColourTowerCP.lean` (PR #8139, 0 sorry) | proves that H₃(q) is too small for su(3): every Specht module has dim ≤ 2 < 3, and the derived commutant Lie algebra has dim 3 < 8 | This is an **obstruction** on the level-2 nucleon model, so the gap is real. §48 says the same: the (C²)^⊗3 model sees only the SU(2) value 3/4, not C_F = 4/3. |
| KZ coupling κ | `lean/QOU/Mass/KZHolonomy/` (`kzBraidRep`, `continuous_kzBraidRep`, PR #7719); `QOU/KZ/GLnResidues.lean` (gl_n, so gl₃) | a one-parameter family of braid representations, continuous in κ. Via Drinfeld–Kohno, q = exp(κ·const) and R ∼ q^{2Ω} (§48). | **This is the nearest thing to a coupling that can vary.** It is a family in κ at a fixed configuration, though, not a flow in a scale. The identification with Jimbo R for n ≥ 3 is open (`qou-9634`). |
| "effective q flows toward 1 under Reeb dynamics" | `observations/color-confinement-observation.md:22` | prose | No flow equation exists anywhere. |
| "strands of T(2,9) locally parallel … asymptotic freedom" | `predicted-spectra/force-knot-identification.md:48` | prose | Same. `confinement-universality.ts:25` withdraws the related framing. |
| "not a running coupling ratio: no renormalisation scale is attached" | `observations/crossing-energy-interpretation.md:32` | an explicit disclaimer | The corpus already says that its channel ratios carry no scale. |

### 1.2 What object qou would need

1. **A scale variable μ, or log μ.** qou has a single substrate value q₀ (the proton pin
   for evaluation). Deriving q₀ is **forever gated** (owner 2026-08-02). A running
   coupling therefore cannot be "q₀ itself moves". It needs a second parameter that acts
   as RG time, with q₀ entering only as a boundary value. Candidates found in the corpus,
   none of them established as a scale:

   | candidate | where | for | against |
   |---|---|---|---|
   | **Hecke tower index n** (strand / crossing count; n = 3A for atoms) | the full-tower ruling 2026-09-03; `observations/archimedean-macroscopic-washout.md:1` (q-CLT, width √(κ₂/n)) | n already acts as a coarse-graining count: the q-CLT is a block-spin limit, so `log n` is a natural RG time. The full-tower ruling already requires every n. | n counts constituents, not momentum. A coupling that runs in n would run with **atom size**, which is a different physical claim from running with energy. |
   | **q-heat-kernel time t** | `information-theory/q-heat-kernel-peter-weyl.md` (spectrum μ_λ(q) = Σ [c][c+1]_q, the Reeb-holonomy Laplacian Δ_ξ^{(q)}) | heat-kernel time is the standard Wilsonian / proper-time RG parameter (t ∼ 1/μ²). Its spectrum is a content-Casimir, so a C_A-like quantity could appear in it. The α_EM per-loop work already uses the heat-kernel unit a₀ = 1/(4π) (`docs/audits/2026-07-18-alpha-em-perloop-measure-status-consolidation.md`). | t carries no unit. Turning t into μ needs a dimensionful step, see item 3. |
   | **KZ coupling κ ∼ log q** | KZHolonomy (above) | it is literally the coupling of the braid representation | Varying κ means varying q, which collides with the single-q₀ framework and, if it is used to fix q₀, with the forever gate. |
   | **jet / GB filtration depth, curvature-rank k** | `observations/confinement-curvature-rank.md` | it is already labelled the "confinement layer" | **Dead as a route.** Bean `qou-hnri` and `docs/audits/2026-09-04-depth-one-is-empty.md` record that the curvature 2-cocycle F has no established filtration to live on. One reading of J^• is provably zero, and another fails its dimension count. |
   | **ħ_q = 1 − q₀⁻¹ / u = b·ħ_q²** | the c_k ladder (AGENTS.md) | it is an expansion parameter | It is a function of q₀ alone, so it cannot run independently. |

2. **A map from crossing energy to a coupling.** α_EM has one, `1/α_EM = q[9]_q[10]_q`
   plus the Bring zero-mode fixed point (`Archimedean/EmCouplingBringZeroMode.lean`), at a
   single scale. A colour analogue needs the `l = 3` (N = 3) representation. §48 shows that
   on (C³)^⊗n with the U_q(sl₃) Jimbo R and framing q^{−1/3}, the crossing eigenvalues
   reproduce every one-gluon colour factor exactly (in log q). So **the static ingredient
   exists in the N = 3 representation**, but qou's nucleon model lives in N = 2
   (convention D is the N = 2 trace). The map from that crossing to α_s is the open part.

3. **A dimensionful unit.** Only CAL-1 (m_e) supplies MeV. Absolute masses are excised as
   predictions (owner 2026-08-11). So any μ or Λ has to come out as `m_e × (derived
   ratio)`, and only the ratio is a claim.

### 1.3 One measurement: the p-family carries no prediction

Exact symbolic `[n]_q`, evaluated once at the proton pin `q₀ = 1.10997858275138…`
(mpmath, 30 dps): `[9]_q₀ = 10.36351758814481`, `[7]_q₀ = 7.62534203713250`,
`ln q₀ = 0.10434072031952`.

| p | α_s = 1/(q₀^p [9]_q₀) |
|---|---|
| −1 | 0.10710442408 |
| 0 | 0.09649233395 |
| ½ (the symmetric split) | 0.09158735388 |
| 1 | 0.08693170792 |
| `q⁻¹/[7]_q` (the fit-shaped form) | 0.11814791777 |

Each unit of p moves α_s by a factor q₀ (about 11 %). Reaching the PDG value 0.1180 would
need p ≈ −1.9, and that p comes from nowhere. **Choosing p, or choosing the `[7]_q`
bracket, because it lands on 0.118 is selection against the target.** Without a scale the
comparison is not even well posed, since α_s(M_Z) is a value at one μ. This table is
recorded so that nobody re-derives it. It is not a candidate list.

### 1.4 Routes (six-part frame)

**R-α1. α_s as a trace ratio in the N = 3 representation (`qou-5iaz` option 1).**
- *Means:* compute the analogue of the α_EM Plancherel ratio for the U_q(sl₃) crossing on
  (C³)^⊗n, using §48's representation.
- *Costs:* one probe, exact ℚ(q^{1/3}). §48's machinery exists. About a day.
- *Risks:* the normalisation is a free choice. `qou-5iaz` says supplying one *"would be the
  fourth input"*. It gives at most a static value with no scale, so it is not α_s(μ). It
  also does not address the gap that qou's own nucleon model is N = 2.
- *Commits to:* treating colour as the N = 3 Jimbo representation **beside** the N = 2
  nucleon model. That is an unruled framework choice (see `qou-ni4b`, `qou-pa2f`).
- *Default:* nothing.
- *Blast radius:* `appendix-standard-model/sm-params-gauge-couplings.md` (the α_s row) and
  the sm-26 status audit. Nothing numeric reads α_s today.
- *Fit risk:* **high**, through the normalisation choice.

**R-α2. Running in the tower index n (q-CLT as block-spin RG).**
- *Means:* define g_eff(n) from the normalised n-strand trace of a fixed colour word.
  Pre-register the sign of d g_eff/d log n before computing.
- *Costs:* a probe plus a pre-registration. The tower data exist, but n ≥ 9 is expensive
  (`markov_peel` costs).
- *Risks:* n is not energy, so a decreasing g_eff(n) would show "weaker binding for larger
  systems", which is not asymptotic freedom. On N = 2 data, any C_A it shows is SU(2)'s.
- *Commits to:* n as RG time. That reading would also have to hold for α_EM.
- *Default:* nothing.
- *Blast radius:* none until something consumes it.
- *Fit risk:* low if pre-registered; the risk is a homonym ("running" in n).

**R-α3. Running in heat-kernel time t.**
- *Means:* write the one-loop effective coupling as the t-dependence of the q-heat-kernel
  trace on a colour isotypic component. Check whether the coefficient of log t is a
  content-Casimir that becomes C_A on the adjoint.
- *Costs:* research. It needs the N = 3 content formula (the corpus formula is SU_q(2)).
  It reuses the α_EM a₀ = 1/(4π) work.
- *Risks:* the outcome is unknown. A positive result would still only give the **sign and
  coefficient** (β₀-like), not a value.
- *Commits to:* t as the scale variable, which makes Λ a heat-kernel time converted to MeV
  through m_e.
- *Default:* nothing.
- *Blast radius:* the α_EM per-loop measure work shares a₀. A result here could
  reinterpret it, so coordinate with that arc.
- *Fit risk:* low. **This is the route I would take first (judgement).**

## 2. β₀

### 2.1 Nearest in the corpus

`lean/QOU/StandardModel/ElectroweakVevGaps.lean:192–196`:
`oneLoopB0 (CA weylT scalarT) = −(11/3)·C_A + (2/3)·ΣT(Weyl) + (1/3)·ΣT(scalar)`, with
positive meaning screening. Over `[Field K] [LinearOrder K] [IsStrictOrderedRing K]`. It
is used only for its **sign** (`b0_su2_sm = −19/6`, `signRule`, bean `qou-myxi`). QCD is
not instantiated, and C_A is an **input**, not read off any trace. The level-3 audit row 4
records that C_F = 4/3 and C_A = 3 are *"pure group theory, no corpus formula reading them
off a Markov trace"*. §48 reads the one-gluon factors (C_F) off the N = 3 crossing
**eigenvalues**. §49 shows that f^{abc} (and so C_A, through f f ∝ C_A δ) appears only as
order-ħ² cancellation structure in the braid relation, with choice-dependent projections.
The β₀..β₃ "proof" (`qou-n1ks`, scrapped) has no file on disk.

### 2.2 What qou would need

A derivation of `C_A` (the adjoint Casimir) from qou's own colour action, which is
`qou-ni4b` again, and a derivation of **why the gauge-boson self-loop enters with the
opposite sign to the matter loop** (the −11/3 against the +2/3). The sign is the whole
content of asymptotic freedom. qou has no loop expansion: virtual quanta are excluded
(owner 2026-11-21, recorded on `qou-t3zb`), so a "one-loop coefficient" needs a non-Feynman
meaning. The heat-kernel a₁-coefficient (R-α3) is one candidate.

### 2.3 Routes

**R-β1. Instantiate `oneLoopB0` for SU(3) (bookkeeping bridge).**
- *Means:* add `b0_su3_qcd (n_f) : oneLoopB0 3 (n_f) 0 = −(11 − 2n_f/3)` (n_f Dirac quarks
  = 2n_f Weyl fundamentals with T = ½, so weylT = n_f). Check: n_f = 6 gives −7.
- *Costs:* one `ring` lemma.
- *Risks:* **it imports the SM β-function.** It is not a fit (no measured value enters),
  but it is not a qou derivation either, and labelling it "derived" would be laundering.
  n_f and C_A are SM inputs.
- *Commits to:* nothing beyond what `ElectroweakVevGaps` already commits to for SU(2).
- *Default:* nothing; the SU(2) instance stays the only one.
- *Blast radius:* none.
- *Fit risk:* none, but it carries an **import** label that must stay attached.

**R-β2. C_A from the N = 3 braid representation.**
- *Means:* extend §48/§49. Read the adjoint Casimir off a crossing-derived quantity, for
  example the Ω-quadratic coefficient of a word that carries an adjoint (q q̄ octet)
  channel, and prove C_A = 3 = N in Lean for generic N.
- *Costs:* moderate; the §49 probe and `SlNFramingColourFactor.lean` are the starting
  points.
- *Risks:* by §48 this is the standard ribbon fact R ∼ q^{2Ω}, so the result would be
  correct and **not QOU-specific**. It would still sit in the N = 3 representation, not in
  the nucleon model.
- *Commits to:* the N = 3 representation as the colour carrier (as R-α1).
- *Default / blast radius:* nothing; none.
- *Fit risk:* none.

**R-β3. The sign of the gauge self-loop from a qou-native object** (R-α3 restricted to its
sign). This is the only β₀ route that could be QOU-specific. It is open research.

## 3. String tension σ

### 3.1 Nearest

- `observations/confinement-curvature-rank.md`: *"String tension = curvature 2-cocycle F"*
  on the GB filtration. This is a dictionary entry with no value. **Its premise is broken:**
  `qou-hnri` / `docs/audits/2026-09-04-depth-one-is-empty.md` find no established filtration
  for F to be a cocycle on, and declare that route dead. The block itself has not been
  updated to say so (a currency defect, noted here and not fixed: the change needs the owner).
- `mass-theory/confinement-categorical-proof.{md,lean}:21,34` (*"plays the role of"*).
- `lean/QOU/ParticleInteractions/MesonFluxTubeReduction.lean` (0 sorry): **two obstructions,
  no energy.** (A) the single-tube reduction 3 → 2 strands gives B₂ ≅ ℤ, so every tube is
  `T(2,k)` with Vol = 0 (`twoStrand_comm`, `twoStrand_winding_bijective`); (B) quark winding
  labels collide (`winding_content_not_injective`, `D_kaon_same_winding`). Bean `qou-qpj9`
  (todo) and its children.
- Level-3 audit row 7: *"needs a scale and a map; none in corpus."*

### 3.2 What qou would need

A **Wilson-loop object**: a family W(R,T) indexed by two lengths whose log grows like the
area R·T. That is a closed colour loop with geometric extent. qou's braids carry crossing
counts and hyperbolic volumes but no length. Obstruction A also says that a 2-strand tube
has no geometry to carry tension. The only linear-growth object in the corpus is
volume-conjecture growth `log|J_N| ∼ N·Vol/2π`, which grows in the **colour dimension N**,
not in a distance. Calling it a tension would be a homonym.

### 3.3 Routes

**R-σ1. Area law from a two-parameter family of closed braids.**
- *Means:* define W(m,k) = |tr_M| of an m×k "rectangular" braid (for example (σ₀σ₁⁻¹)^{mk}
  arranged as a grid). Test whether −log W grows like m·k (area) or like m+k (perimeter).
- *Costs:* one pre-registered probe.
- *Risks:* the grid word is an **unforced choice**, so the area law could depend on it.
  Volume-type growth would be hyperbolic, not area. A value of σ would still need the
  t ↔ distance conversion from §1.2.
- *Commits to:* a lattice reading of braid words. This overlaps `qou-jsx5`; coordinate.
- *Default:* nothing. *Blast radius:* `confinement-curvature-rank.md` would get a
  competitor to its dictionary entry.
- *Fit risk:* medium, through word selection. The protection is to pre-register the family
  and test area against perimeter **scaling**, never a value.

**R-σ2. Do nothing beyond flagging the dead dictionary entry.** Recommended until B1
exists.

## 4. Λ_QCD

### 4.1 Nearest

None as an object. `observations/deconfinement-golden-threshold.md:42` uses Λ_QCD as a
denominator (`k_B T_c/Λ_QCD ∼ (q₀ − 0.382)/q₀ ≈ 0.656`). `observations/observables-algebraic-independence.md:11`
**conjectures that T_c/Λ_QCD is not in ℚ(q₀)**. `qou-5iaz` option 2 points at CAL-3
(𝔇_π, proxy m_π) as the confinement scale. `qou-5iaz` puts Λ before α_s and *"neither
before `qou-ni4b`"*.

### 4.2 What qou would need

Λ is dimensional transmutation: Λ = μ₀·exp(−1/(2b·α_s(μ₀))) needs a **running law** (§1),
a **coefficient** (β₀, §2) and a **boundary value at a reference scale μ₀**. qou can
supply μ₀ only as `m_e × ratio` (CAL-1), or as m_π (CAL-3 proxy). The honest output is a
ratio such as Λ/m_π or Λ/m_e.

### 4.3 Routes

**R-Λ1. Dimensional transmutation from an existing α_s formula.**
- *Means:* feed `q^p[9]_q` or `q⁻¹/[7]_q` into the one-loop formula with μ₀ ∈ {m_e, m_π,
  m_p}.
- *Costs:* minutes.
- *Risks:* **forbidden as a prediction.** p is free, `[7]_q` is fit-shaped, and μ₀ is a
  discrete choice. Picking any of the three because Λ comes out near 200 MeV is selection
  against the target (§NO FITTING). It also imports β₀ (R-β1).
- *Commits to:* nothing useful. *Default:* not done. *Blast radius:* would contaminate
  `qou-5iaz` with a pseudo-value.
- **Not recommended. Listed so that it is recognised and refused.**

**R-Λ2. Λ as the scale where the R-α3 effective coupling diverges, in units of m_e.**
- *Means:* if R-α3 yields a flow, Λ is its Landau-pole time t_Λ, converted to energy by the
  CAL-1 unit and the derived t ↔ μ map.
- *Costs:* research, after R-α3.
- *Risks:* the t ↔ μ conversion is a new identification and must itself be derived.
- *Commits to:* the heat-kernel scale reading.
- *Default:* nothing. *Blast radius:* the observables-independence conjecture (item 5)
  would then become testable.
- *Fit risk:* low, provided μ₀ is fixed by the construction and not by the output.

## 5. Honest comparison points (comparison data, never inputs)

Values are quoted from standard references from memory. **None is held in `library/`**
(corpus grep #11, #13: no lattice σ value, Λ only as a phenomenological input in lattice
n–p papers). Each must be sourced to a held or newly ingested reference before use. All of
them are scheme-dependent.

| ratio | approximate comparison value | why it is a fair test | caveat |
|---|---|---|---|
| sign of β₀ (or of d g/d log μ) | negative (antiscreening) for SU(3), n_f ≤ 16 | dimensionless, scheme-independent, falsifiable by a **sign** | the cheapest honest target; R-α3 and R-β3 aim at it |
| C_A/C_F | 9/4 | pure group theory; tests whether qou's colour action is SU(3) | not held in the corpus (grep #9); R-β2 |
| √σ / Λ_MS̄ | ≈ 2 (n_f-dependent) | both are qou outputs once R-σ1 and R-Λ2 exist, so the unit cancels | scheme dependence on Λ |
| T_c / √σ | ≈ 0.63 (pure gauge) | unit cancels | the corpus already conjectures non-algebraicity in ℚ(q₀) |
| Λ_MS̄ / m_π, or Λ / m_p | ≈ 1.5, ≈ 0.2 | ratio to a CAL-3 proxy or the anchor mass | m_p is the q₀ pin, so Λ/m_p partly measures the pin |
| α_s(M_Z) | 0.1180(9) | the standard headline | needs both a running law and M_Z as a qou ratio. **Not well posed for any formula in the corpus today** |

## 6. Proposed beans (not created)

The beans mount is present. The task scope is read-only apart from this file, so the beans
are listed here and not created. Title search on the mount (`grep -l -i -E
'Lambda_QCD|string tension|beta_0'`) finds only `qou-5iaz`, `qou-jsx5`, `qou-pa2f`,
`qou-hnri`, the scrapped `qou-n1ks` and one unrelated bean, so none of these is a
duplicate. Run the todo-manager exact-title check before creating them.

- **B1. GAP: no scale variable for a running coupling.** Candidates: tower n, heat-kernel
  time t, KZ κ. Curvature-rank k is excluded by `qou-hnri`. Parent `qou-8lxd`; blocks
  `qou-5iaz`.
- **B2. β₀ bridge: SU(3) instance of `oneLoopB0`, labelled IMPORTED, plus C_A from the N = 3
  braid representation (R-β1 + R-β2).**
- **B3. GAP: no Wilson-loop / area-law object; the `confinement-curvature-rank` string-tension
  entry rests on a filtration `qou-hnri` declares dead.** Needs an owner decision on the
  block's wording.
- **B4. Research: heat-kernel time as RG time; sign of the colour one-loop coefficient
  (R-α3 / R-β3).** Pre-register the sign before computing. Coordinate with the α_EM
  per-loop arc (shared a₀).

## 7. What is NOT established here

- That any of n, t or κ **is** a renormalisation scale. Each is a candidate only.
- That qou's colour sector is SU(3) (`qou-ni4b`, `qou-pa2f`; `ThreeStrandColourTowerCP.lean`
  proves that H₃(q) is too small).
- Absence claims are scoped to the grep in `CORPUS-GREP-gluon-dynamics.md` plus the files
  opened here: "not found in the searched corpus", not "cannot exist".
- §5 values are recalled, not sourced.
