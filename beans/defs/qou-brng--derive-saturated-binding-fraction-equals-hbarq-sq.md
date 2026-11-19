---
# qou-brng
title: 'OPEN KERNEL: derive that the saturated nuclear binding fraction = ℏ_q² (mass/binding rung)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T15:05:00Z
updated_at: 2026-11-19T00:40:00Z
parent: qou-v2om
---

Arc bk-crossing-coordination, item 3b→1 crux (PR #5346). The mass/binding ℏ_q-rung split was
attacked in `computations/binding_mass_rung_derivation_probe.py` /
`docs/audits/2026-08-21-binding-mass-rung-derivation.md`. What CLOSED:

- **Traced** — the mass multiplier's `1/ℏ_q²` is the CAL-2 muon-anchor cusp factor
  (`m_μ/m_e = Vol(4₁)/ℏ_q²`), not a free choice; the binding ansatz `B = m_e·Vol·M` does not
  re-apply it.
- **Proved (Lean, sorry-free)** — `QOU.Mass.BindingMassRung`: the analytic dichotomy — mass
  multiplier `lw/ℏ_q²` is an order-2 pole with residue `lw` (rest mass diverges as ℏ_q→0);
  `binding/mass = (M/lw)·ℏ_q² → 0` (binding is an O(ℏ_q²) quantum correction, regular at q=1).

What is OPEN (this bean): a **first-principles proof that the mass-difference cancellation lands
binding at EXACTLY the ℏ_q² rung** — i.e. that the *saturated* nuclear binding fraction `B/A/m_N`
is `ℏ_q²` and not merely `O(ℏ_q²)`. Empirically the fraction rises monotonically toward ℏ_q² with
A (²H 0.12·ℏ_q² → ⁴He 0.77 → ⁴⁰Ca 0.93 → ⁵⁶Fe 0.95·ℏ_q²); the ≈0.95·ℏ_q² Fe value is a scope-(a)
forward observation under the numerology guard, NOT a derivation.

Candidate routes:
- ~~The volume-defect picture `B = (m_e·lw/ℏ_q²)·ΔVol`~~ — **REFUTED 2026-08-21 (scope-a)**,
  `computations/binding_volume_defect_route_refuted.py`. The knot-volume defect `ΔVol/Vol` is O(1)
  (1.65 ³H, 2.00 ³He, 3.00 ⁴He), NOT O(ℏ_q²), so `B_pred ~ GeV`, overpredicting binding by 102–250×
  (≈1/ℏ_q²). Binding is not a mass-scale volume defect; the O(1/ℏ_q²) mass terms do not cancel to
  O(ℏ_q²) at the volume level.
- Why the coordination count `M` (integer, cusp-independent) is the correct binding multiplier
  while the mass carries the q-dim-weighted `lw` — a categorical statement about linking (mutual)
  vs self-energy (self-linking) amplitudes in the substrate. **Still open — the surviving route.**

**Updated verdict (2026-08-21):** with the volume-defect route refuted, the saturated-fraction
≈ ℏ_q² coincidence has lost its one candidate mechanism and is — on current evidence — **more
likely numerology than a derived prediction**. Do NOT wire the 0.95·ℏ_q² match; do NOT fit a
correction to force it to 1·ℏ_q². The honest state: analytic dichotomy proved (Lean); the exact
ℏ_q² saturation value is open AND now more suspect. Needs a genuinely new structural mechanism
(the linking-vs-self-energy route) or a scoped owner decision on whether it is worth pursuing.


---
**Update 2026-08-30 (session qou-d3i9, PR #6125).** Partial progress on the surviving
(linking-vs-self-energy) route — the TYPE question is resolved; two sub-questions stay open.

CORPUS CORRECTION that reframed it: the ³He/⁴He carrier L6a4 is BRUNNIAN (pairwise Gauss
lk ≡ 0), so M cannot be a linking number — it is a coordination COUNT (graph degree z=A−1).
The em-linking sibling thread proved the same obstruction (docs/audits/2026-08-01-em-linking-reads-round1.md,
O1 antisymmetry + topological-vs-metric pairing).

PROVED (Lean, sorry-free — QOU.Mass.BrunnianBindingChannel, built on the proved
CrossingEnergy.decomposition): the mutual crossing energy splits into a signed writhe/linking
channel (n₊−n₋=2·lk) and an unsigned count/coordination channel (n₊+n₋). For a Brunnian pair
n₊=n₋ so the signed channel is ZERO and the whole binding energy is the unsigned count channel,
strictly positive for a crossing pair at q>1 — binding SURVIVES the Brunnian vanishing where the
linking number does not. This is why M is a coordination count, discrete analogue of the
em-linking thread's "route around O1 is an UNSIGNED quantity" (Khesin Rmk 3.5). Audit:
docs/audits/2026-08-30-brunnian-binding-channel.md.

STILL OPEN (the sharpened kernel — a future attack aims here):
1. exact map n₊+n₋ → z=A−1 (the channel is proved; the coefficient is not);
2. why the surviving count channel enters as a BARE INTEGER while the self/mass channel keeps the
   full q-dim self-trace lw (self = closed quantum trace over Wedderburn channels; mutual = pairing
   of two fixed components, no internal channel sum — plausible but NOT proved);
3. the exact ℏ_q² saturation value stays numerology-suspect (unchanged; not touched, not forced).


---
**Update 2026-08-30 (session qou-xjup, PR #6145) — residuals R1/R2/R3 worked.**

R2 (mass=self, binding=mutual) PROVED at the additive-energy level — QOU.Mass.SelfMutualPartition
(sorry-free): the crossing energy partitions into self+mutual; binding := Σ(isolated self) − assembly
= −(mutual), self-energies cancel (binding_eq_neg_mutualEnergy, binding_indep_of_self). The
assignment is a theorem of the partition + mass-deficit definition, not a postulate. Residual: the
mass-observable ↔ crossing-energy identification at Markov-trace granularity (self closes to lw;
m=m_e·Vol·lw/ℏ_q²) — a named modelling step, not lifted.

R1 (crossing-count → coordination) PROVED for the clasp model: coordinationUnits = ½·|inter
crossings|; complete minimal-clasp graph ⇒ C(A,2), per-nucleon z=A−1. Residual: which link realizes
the A-body carrier (topological input, saturation-limited).

R3 (exact ℏ_q² saturation) MEASURED (brng_hbarq2_saturation_genericity_probe.py, no float64,
scope-(a)): B/A/m_N PEAKS at 0.954·ℏ_q² (⁶²Ni) and FALLS (²³⁸U 0.82·ℏ_q²) — never reaches ℏ_q², not
a saturation limit. The match is to the empirical B/A peak (a volume−surface−Coulomb balance near
A≈60), NOT the fundamental volume coefficient a_V/m_N ≈ 1.71·ℏ_q². 3/7 trivial constants match within
6%. Verdict: numerology — confirms & sharpens the 2026-08-21 suspicion; do NOT wire, do NOT force.

Net: type question PROVED (#6125); R1 PROVED (clasp model); R2 PROVED (additive level); R3 = numerology.
Sole surviving genuinely-open item: the R2 mass-observable=closed-self-trace identification at the
archimedean boundary. Audit: docs/audits/2026-08-30-brng-residuals-worked.md.


---
**Update 2026-08-30 (session qou-0qkt, PR #6145) — R2 residual LIFTED.**
The additive self/mutual partition is now lifted to the mass observable via the archimedean functor
τ=log — QOU.Mass.ArchimedeanTraceBridge (sorry-free): Markov/Jones trace multiplicative under
connected sum ⇒ free energy E=log T additive (freeEnergy_connectedSum/_prod) ⇒ the additivity
SelfMutualPartition assumed is DERIVED; binding = −log I = connected/interaction free energy
(binding_eq_bindingFreeEnergy), =0 ⟺ independence, >0 ⟺ amplitude suppressed. Two named modelling
inputs remain (NOT open derivations): (1) substrate assembly amplitude = the multiplicative Markov
trace (citable Jones, carried as hypothesis); (2) dressing m=m_e·Vol·lw/ℏ_q² (calibration+geometry).
Net: type question, R1 coefficient, R2 additive+lift all PROVED; R3 = numerology. Audit:
docs/audits/2026-08-30-brng-residuals-worked.md.

---
**Update 2026-08-30 (session link-vs-self, PR #6226) — a hidden hypothesis in R2, and a reframing of this bean's own question.**

Adversarial read of the same-day closure (#6125 / #6145 ×2), not a new attack on the magnitude.
Nothing here retracts any of it. Scope-(a) throughout; no number moved, nothing wired.

**1. `SelfMutualPartition.binding_eq_neg_mutualEnergy` carries an unstated hypothesis.** Its
`binding` is *defined* as `selfEnergy − assemblyEnergy`, justified in the docstring by "the self
crossings are exactly those present in isolation". The mass-deficit definition is `B = (Σ ISOLATED
masses) − assembled`; substituting `selfEnergy` presumes assembly changes no component's own
self-crossing content. Now explicit, sorry-free, `lean`-direct exit 0, all 8 decls on
propext/Classical.choice/Quot.sound — `QOU.Mass.SelfCrossingInvarianceGate`:

    binding = −mutual + selfDefect          selfDefect := isolatedMassTotal − selfEnergy
    binding = −mutual  ↔  selfDefect = 0    (the landed theorem is exactly this slice)

`gate_has_content` is the falsifiable witness: one assembly (1 inter + 1 self crossing, unit
energy) read two ways — self-crossing pre-existed vs created by assembly. **Mutual energy is 1 in
both; binding is −1 vs −2.** So `binding_indep_of_self` is a consequence of the gate, not of the
crossing partition. `binding_eq_neg_mutualEnergy_of_gate` recovers the landed result.

**2. Why it is not free (the OCR tier did the work).** Călugăreanu–White–Pohl `SL = Wr + Tw` — only
the SUM is the isotopy invariant. Moffatt & Ricca §1: writhe and twist jump by equal and opposite
amounts through an inflexion; "any deformation whose projection on any plane involves a type I
Reidemeister move … must involve passage through an inflexional configuration. General deformations
(or 'ambient isotopies') do therefore **typically** involve such passage"; Pohl's `SL = W + T` is
for **regular** isotopy. A type-I move is exactly creation/removal of a SELF-crossing. Formalized
generic over `[AddCommGroup R]` (§7c). **This citation is invisible to corpus-grep path 5:**
`library/procrsoclondona92/sections/` is 1,916 B of JSTOR banner vs 46,511 B in `ocr/`, so a
`sections/` grep for *helicity* or *Călugăreanu* returns nothing on that document.

**3. Applied the criterion to `lw` — it does NOT bite, deflating my own finding.**
`computations/lw_is_framing_independent_probe.py`, 3/3 PASS, mpmath 65 dps + exact `Fraction`, no
float64. `linking_weight_family_a` has signature `(q, q_inv=None) -> mpf` — **no knot, no diagram,
no framing** (a type fact, inspected not measured). It is `(1/4)·Σ_{λ⊢4} dim_q V_λ`, verified
IDENTICAL to `5/2 + (3/4)h²` over ℚ at 5 rational points (exact, not "to N digits");
`lw(q₀) = 2.53277965639939149205151450176`. So `selfDefect = 0` holds for the mass multiplier and
the assignment is safe from this objection.

**4. What survives — a reframing of THIS BEAN's question.** `lw` is called a "linking weight" and
is not a linking quantity. This bean asks *"why the binding multiplier is the mutual (coordination)
linking count while the mass multiplier is the self-linking weight `lw`"* — presenting them as two
readings of one linking notion. **They are not that:** `M` is a topological coordination count,
`lw` is a representation-theoretic Wedderburn q-dimension sum. Two different kinds of object, so
the question as written asks why one linking notion splits two ways when that is not the situation.
A reframing, NOT an answer. Same name-vs-content class as `markovZ`/`markovZc`.

**Open after this, and what I did NOT claim.** `lw`'s H₄ Wedderburn-count interpretation stays
**posited** per its own producer docstring (at q₀ a CODATA-implied near-match to the λ ≈ 2.46 that
round-trips m_p; five refuted paths in `2026-06-04-three-paths-refuted-roadmap-update.md`) —
untouched. R1's topological input and `ArchimedeanTraceBridge`'s two named modelling inputs are
unaffected. R3 stays numerology. **A possible author decision is framed in §8 of the audit**
(rename `lw` / restate this bean's question / do nothing), with costs, risks and a recommendation
of *do nothing now, restate when the arc is next worked* — the default is safe.

Audit: `docs/audits/2026-08-30-self-crossing-invariance-gate.md`.

---
**Update 2026-08-30 (session assembly-shortfall, PR #6271) — the "3x shortfall" is NOT this
bean's extensive term, and it is not a coefficient either.**

Scope (a) for the numbers, (b) for one exclusion. Nothing refuted, nothing wired.

**A withdrawal first.** `bond_rule_dashboard_comparison_probe` (merged today, #6212 — my own)
reported "both rules are ~3x short for A >= 4" and attributed it to "the extensivity problem
(qou-brng)". **That attribution is wrong and is withdrawn.** The refuting numbers were in that
probe's own output; they were read as a level rather than as a sequence in A.

**Not extensivity.** The chain assembly lays down exactly A-1 bonds, so B_model is affine in
(Z,N) — both second differences vanish to 0.0 exactly — and B_model/A converges to the closed
form -(alpha/2)ln(f_pp*f_nn) = 2.92424631376189350737739190987 MeV/nucleon (monotone to 3.0e-4
at A=10^4). model/AME is bounded BELOW by 0.307 over A=2..238, with an interior minimum near
the AME peak and a RISE past it:

    4He 0.3068  12C 0.3480  40Ca 0.3332  62Ni 0.3366  208Pb 0.3933  238U 0.4108

An extensivity deficit sends that ratio to zero. This assembly is extensive by construction.

**Not a coefficient.** (1) B_model/A is strictly increasing along N=Z and bounded above by its
limit, so it can never turn over; AME B/A turns over at 62Ni. Any positive constant preserves
monotonicity, so NO constant reproduces the fall — scope (b), invariant: monotonicity of an
affine-in-(Z,N) functional over A. (2) The deuteron refuses a uniform factor 3 outright: the
bare model already OVER-binds 2H by 1.2736x; tripling gives 3.8207x.

**A THIRD instance of this arc's own trap, recorded as a negative.** 3*model/AME is 1.00091 at
56Fe and 0.99945 at 40Ca — 0.06%, from the integer 3, nothing fitted — and it is worthless: the
same quantity is 1.401 at 7Li and 1.180 at 208Pb. A constant-B/A model can only CROSS a
rising-peaking-falling curve and it crosses near the peak. Identical in shape to R3's
0.954*hbar_q^2 "saturation" (a match to the empirical B/A PEAK, not a fundamental coefficient)
and to qou-vudb's flat line crossing a rising curve. Do NOT quote the 0.06%.

**Where the gap actually is.** The fall past 62Ni is Coulomb, counting proton PAIRS Z(Z-1).
QOU.MassTheory.CrossingCountAffine.no_crossing_combination_is_protonPairs (merged today, #6212,
sorry-free, coefficients quantified first) proves no linear functional of the crossing counts is
Z(Z-1) — second difference 2 against 0. So the object missing from the absolute binding table is
the SAME one that theorem excludes, reached from the opposite side (that theorem was measured
against mirror splittings; this against the table).

**Consequence for this bean and for qou-0c19.** Both frame the target as a missing additive
EXTENSIVE term. For the chain assembly that framing does not apply. The live target is the
Z(Z-1) multiplicity plus the A^{1/3} geometry of a Coulomb energy — neither reachable from the
crossing counts. This narrows the arc; it does not open anything.

Probe: computations/probes/assembly_shortfall_shape_probe.py (8/8, no float64, mpmath 65 dps,
AME read as exact decimal text).


---
**🛑 CORRECTION 2026-08-30 (bean `qou-bsfg`) — the R2-lift entry above overstates.**
That entry says "Markov/Jones trace multiplicative under connected sum ⇒ free energy additive ⇒ the
additivity SelfMutualPartition assumed is DERIVED; binding = −log I, =0 ⟺ independence". Two fixes:
(a) the proved matrix theorem (Kronecker) models the DISJOINT UNION, which carries the loop value
`δ = [2]_q` — `J(K₁⊔K₂) = δ·J·J` — not the connected sum, for which `J(K₁#K₂) = J·J` is exact; the
connected-sum reading was not licensed by what was proved. (b) consequently "=0 ⟺ independence" is
wrong as physics: an independent assembly has `I = δ`, so it carries `log δ ≈ 0.699` per
juxtaposition (≈2.10 for ⁴He), and additivity holds only up to that factor
(`QOU.Mass.ClosureNormalisationDefect.freeEnergy_closureNorm_additive_iff`: additivity iff δ=1,
excluded for q>1). The R2 lift therefore stands as "log turns a multiplicative amplitude into an
additive free energy" — which is `Real.log_mul` — but NOT as a discharge of the multiplicativity
input; see the retraction on `qou-301d`.
---
**Update 2026-08-30 (convergence note) — R3's verdict now has TWO independent
structural arguments, from opposite directions.**

A sibling landed `QOU.Mass.SaturationPeakStructure` on main (`3109e09818`,
sorry-free — verified directly, 0 sorry / 0 axiom, hypotheses `0 < a_S`,
`0 ≤ a_C`, `0 < u`, not vacuous). For the volume−surface−Coulomb shape
`f(u) = a_V − a_S/u − a_C·u²` in `u = A^{1/3}` it proves `perNucleon_lt_volume`
(the curve is strictly below `a_V` for EVERY `u > 0`) and `peak_is_not_bulk`, so
the empirical B/A peak is an interior maximum of a surface/Coulomb competition —
*"matching any constant to it is a category error, whatever the constant."*

That is the DATA-side argument. PR #6271 (this session, merged) is the same
conclusion from the MODEL side: `B_model/A` is strictly increasing along `N = Z`
and bounded above by its limit, so it can never turn over; multiplying by any
positive constant preserves monotonicity; therefore the model can only CROSS the
peaked curve, and the 0.06 % agreement of `3×model` at ⁴⁰Ca/⁵⁶Fe is that
crossing, not evidence.

Neither derives the other and neither was aware of the other while running.
Together they say: the peak is not a bulk quantity (sibling), and a monotone
model's near-match to it is an artifact (mine). Both point at the same missing
ingredient — the sibling's `a_C·u²` Coulomb term with `u = A^{1/3}`, which is
exactly the `Z(Z−1)` multiplicity plus `A^{1/3}` geometry #6271 named as the
live target, and which `CrossingCountAffine.no_crossing_combination_is_protonPairs`
proves the crossing counts cannot supply.

No number moved; nothing wired. Recorded so the corroboration is not lost.


---
**Coordination cross-check 2026-08-31 — the "two named modelling inputs" count is short by one,
and the third is a refutation.**

`348cf21d8d` (`qou-v7ro×qou-brng`, Milnor deficit) measured `|D_A|` falling geometrically —
`1.44e-3 → 8.2e-9` over `A = 3…8`, ratio `−h²(h²+2) = −0.0893226497` at every step — against a
rising binding, and concluded `D_A` is the Milnor order/parity marker, not the magnitude. **That is
right and is not disputed**; it holds under any normalisation, since a five-order-of-magnitude fall
runs opposite to the binding read per-nucleon, per-cluster or per-body-order alike.

Its forward sentence is what needs correcting: *"the magnitude lives in the `qou-brng` coordination
free energy … whose only open pieces are two named modelling inputs"* (Markov-trace-as-amplitude;
the `m = m_e·Vol·lw/ℏ_q²` dressing).

**There is a third piece and it is not a modelling input.** `binding = −log I` is a *shape* with `I`
unspecified. The corpus's filling for `I` is the coordination coefficient —
`complete_minimal_clasp_coordination`, `C(A,2)` units at one per bonded pair, `z = A−1` — and that
filling is **pair-local**, which forces `b₃ = 0`:

* `CrossingModelPairLocality.b3_eq_zero_of_pairLocal` (`d2ed45489f`);
* `InteractionFactorNotPairwise.pairFactorised_b3_eq_zero` (same) — the multiplicative face;
* `CountChannelCarrierLocus.canonical_carriers_b3_eq_zero` (`773366d004`) — the count channel on the
  Hopf/Borromean carriers sits *exactly* on that locus, `μ_Borromean = 3 = 3·μ_Hopf`.

Measured `b₃ = +1.4262225 MeV`; model `0`. The scale cancels (`b3_over_b2_eq`), so it is
zero-parameter, and the alternative full-energy reading gives `−3(q+q⁻¹) < 0` for every `q > 0`.

**Timing:** `d2ed45489f` was on `main` 2 h 17 m before `348cf21d8d`; `773366d004` landed 7 minutes
after. So this is a coordination miss, not a disagreement — recorded in
`docs/coordination/2026-08-30-milnor-brunnian-deficit-arc.md` at the point the claim was made.

**Net effect on this bean:** the open list is *type question proved, coordination coefficient
proved, `binding = −log I` proved* — **plus** an unfilled `I` that must carry irreducibly many-body
structure, with a one-line acceptance test (`carrier_must_break_three_to_one`: any carrier must
break `μ_t = 3·μ_p`). The channel is not obstructed — small half-integer multiplicities reach the
measured ratio to 0.27 % — so the burden is on **deriving** the crossing numbers; two free integers
against one ratio is a fit.


## Carrier crossing numbers ARE derivable — and every derivation gives b₃ ≤ 0 (2026-08-31)

**The question is answered, and the answer is a quantisation obstruction with a
width: 16.98 %.** Lean `QOU/Mass/CarrierCrossingQuantisation.lean` (11 decls,
sorry-free, standard three axioms); probe
`computations/probes/carrier_crossing_quantisation_probe.py` (8/8, exact
`Fraction`, no free parameters).

**The identity.** `CountChannelCarrierLocus` already fixes `μ = (n₊+n₋)/2` =
half the carrier's crossing count, and the scale cancels, so
`b₃/b₂ = c₃/c₂ − 3`. Both `c` are crossing counts of braid words, hence
**integers**.

**Why the retracted quantisation argument is now live.** That file records the
half-integer argument as WRONG *because it assumed `μ_pair = 1` while `μ_pair`
was free*. That retraction stands. **Owner ruling A of 2026-08-29 supplies the
hypothesis** — the deuteron carrier is the canonical braid closure, Hopf,
`σ_g²`, `c₂ = 2`. With `c₂` pinned the freedom collapses to one integer.

**Four rules the corpus derives, all consistent, all `b₃/b₂ ≤ 0`:**

| rule | `c₂` | `c₃` | `b₃/b₂` |
|---|---|---|---|
| min-length enumeration (`binding-k-enumerator`) | 2 | 2 | −2 |
| chain / coordination `z = A−1` | 2 | 4 | −1 |
| canonical Brunnian (Hopf, Borromean) | 2 | 6 | **0** |
| census volume-match (AME-inverted) | 6 | 7 | −11/6 |

Measured `+0.6411239316`.

**Two findings inside that table.** (1) The `binding-k-enumerator` returns
`bindingKWord = [3,3] = σ₃²` for deuterium, tritium **and** helium-3 alike — the
`6₂`/`8₁₁`/`L6a4` on those Lean instances are retained *census names*, not what
was enumerated. Its criterion (shortest PSD-feasible even word at `L ≤ 3`)
cannot see `A`, so it can only ever give constant `μ`. (2) The census tier is
flagged **AME-inverted by the atlas registry itself** — circular, not a
derivation.

**🛑 TRAP — the straddle manufactures the right sign.** `c₂ = 2` (owner-ruled
Hopf) with `c₃ = 7` (census A=3 average) gives `+1/2` — right sign, 22 % low,
and meaningless: two different carrier assignments. Read the census
consistently and it is `−11/6`. I made exactly this error before catching it;
`straddle_manufactures_the_sign` records the arithmetic so it is not
rediscovered as a result.

**The obstruction.** With `c₂ = 2`, `b₃/b₂` lands on the half-integer lattice
(single A=3 carrier) or the quarter-integer lattice (distinct ³H/³He carriers).
Measured value sits in a gap of both: nearest is `c(³H)+c(³He) = 15` →
`3/4`, **+16.98 %**; single-carrier nearest is `c₃ = 7` → `1/2`, −22.01 %
(`c₃ = 8` → `1`, +55.98 %). `quarter_lattice_gap` proves `≥ 161468/1483044` for
**every** integer.

**The selection principle points the wrong way — this is the substantive
obstacle.** Escaping needs `c₃ > 6`, above the Borromean. But `6` is *minimal*:
`QOU.Knots.KauffmanTL3` machine-checks no braid word of length `< 6` is both
Brunnian and nontrivial. So a working carrier must be a **non-minimal** Brunnian
representative, while the only selection principle the corpus derives —
shortest PSD-feasible word — returns the minimum by construction.

**Scope (b)** on the conjunction {count channel, `μ = c/2`, Hopf pair carrier,
integer crossing counts}, invariant named: integrality of a crossing count.
**(a)** on each ingredient; `brunnian_binding_survives` untouched. Conditional
on owner ruling A.

**Next, in priority order.** (1) `μ = c/2` is the cheapest thing to release — a
multiplicity that is not half a crossing count is not lattice-valued, and this
whole obstruction evaporates. Nothing derives `μ = c/2`; it is
`countChannel`'s definition. (2) Find a selection principle that is not
minimality. (3) Neither is started.


### Sibling `be017ea57b` closes the other route (2026-08-31, same hour)

Another session landed a numerology guard on this bean from the opposite
direction: **inverting** the `CoordinationSaturation` plateau for a coordination
number `k` is generic — 27 of 30 (`ε`, target) combinations land inside the
plausible window — so `k ≈ 6` or `≈ 12` is not the framework predicting a
lattice. Together with the result above, **both routes to a multiplicity are
closed**: inverting an anchor for it is a fit, and deriving it from the carrier
gives the wrong sign.

Do not conflate the two `k`s. Theirs is a *bounded* degree; the `chain /
coordination z = A−1` row above is the **complete** graph, which
`CoordinationSaturation` already excludes by saturation. The chain row
re-derives that excluded case from the crossing side (`−1`); it is not a second
measurement of their `k`.


### 🛑 Correcting my own recommendation: releasing `μ = c/2` is the MOST expensive escape, not the cheapest (2026-08-31)

I recommended, above and in #6321, that *"the cheapest escape is releasing
`μ = c/2`, which nothing derives — it is `countChannel`'s definition."*
**Both halves are wrong.**

**It IS a definition, and the constant is forced.** `countChannel`'s `½` is the
unique solution of `BrunnianBindingChannel.pairEnergy_decomp` — the `ring`
identity splitting `n₊q − n₋q⁻¹` into its bar-even and bar-odd parts,
`½(n₊−n₋)(q+q⁻¹) + ½(n₊+n₋)(q−q⁻¹)`. Solving that 2×2 system in the basis
`{q+q⁻¹, q−q⁻¹}` gives the `½`; it is not a convention anyone chose.

**And dropping it would not help anyway.** `bRatio_scale_invariant` (new, proved):
`b₃/b₂` is invariant under `μ ↦ κμ` for every `κ ≠ 0`. So `μ = c` gives the
identical ratio to `μ = c/2` (`muOfCrossings_halving_immaterial`). The constant is
not load-bearing in either direction.

**What this does to the result — it STRENGTHENS it.** The hypothesis actually in
force is not `μ = c/2` but the far weaker `μ ∝ c`. Escaping the lattice needs a
**nonlinear** `μ(c)`, and `pairEnergy_decomp` is linear in `(n₊, n₋)` by
construction. So the escape route runs through **`def:crossing-energy` itself**,
upstream of the whole mass sector — not through a convention.

**Revised next steps.** The `μ` route is closed harder than I said. What is left:
(1) a selection principle that is not minimality — still unstarted, still the
live one; (2) accept that the count channel does not carry `b₃` and look for the
extensive term elsewhere, which is `qou-brng`'s original framing.


### Two further corrections, both mine, before #6321 merges (2026-08-31)

**(1) The selection principle is NOT minimality — I asserted it was.** Read
`binding_k_enumerator.py`'s sort key, not the Lean instances' proxy field:
`(0 if PSD_feasible else 1, markov_residual_to_target, L_K)`. **Length is the
THIRD key, a tiebreak.** The criterion is **Frobenius-residual minimisation**,
which depends on `tr_M` at `H_{3A}(q₀)` and is therefore `A`-dependent.

The Lean instances carry `bindingKMinimalLength := length ≤ 4`, a decidable
*proxy* field, and reading that as the criterion is exactly what makes minimality
look load-bearing. So the reason all three nuclei returned `σ_g²` is
**truncation, not principle**: the run used `L_K_max = 4 / 3 / 3`.

**The range that matters has never been searched.** `c₃ ≥ 8` means word length
`≥ 8`; over the 4 inter-nucleon generators that is ~87,000 words against the ~84
actually tried. **This is a compute question with a definite answer, not a
structural impasse** — and it is the live next step.

**(2) Brunnian parity EXCLUDES both points the published gap was attained at.**
`n₊ = n₋` (the condition emptying the signed channel) forces `c = n₊ + n₋`
**even**. The two nearest approaches I published — `c(³H)+c(³He) = 15` and
`c₃ = 7` — are **both odd**, hence unreachable.

| | published | corrected under parity |
|---|---|---|
| distinct ³H/³He carriers | `15` → `3/4`, **+16.98 %** | `14` → `1/2`, **−22.01 %** |
| single A=3 carrier | `7` → `1/2`, −22.01 % | `8` → `1`, **+55.98 %** |

So the gap **widens**, and for a single Brunnian carrier `b₃/b₂` is an outright
integer. This is not a refinement of the bound — parity deletes the points the
bound was attained at. `even_lattice_gap` proves `≥ 209293/1483044` for every
integer; `brunnian_crossings_even` and `single_brunnian_carrier_integer_valued`
carry the rest. The `A = 2` Hopf carrier is unaffected: it is **not** Brunnian
(`lk = 1`, `n₊ = 2`, `n₋ = 0`), the boundary case where `lk = z = 1`.

File is now 20 declarations; probe 11/11.


## GS tower / jet order — the degree index is not body order past 3He (PR #6393, 2026-08-31)

The 'full GS tower, not just degree 0' step. Two probes, one finding.

**1. `gs_tower_jet_degree_body_order_probe`** — `lem:bond-order-eq-jet-degree`
reads the jet degree index as BODY order ('the n-nucleon cluster sub-word at jet
vertical degree n'). Measured on the filtration's own graded dimension
[A]_q! = sum_l M(A,l) q^l, that reading is inconsistent from A=4. Two exact facts,
run as gates on A=2..8: deg [A]_q! = C(A,2), and every coefficient on 0..C(A,2) is
strictly positive. So there is a non-zero graded piece at every degree up to
C(A,2) — read as body order, non-zero n-body clusters for n up to C(A,2) among
only A nucleons. C(A,2) > A exactly when A > 3, so it holds at D and T/3He and
breaks first at 4He — where this arc's closures wall and where mu_4 = -4.591 sits.
Weight in the impossible degrees at the proton pin: 20.85 % at A=4, 49.49 % at
A=5, 73.98 % at A=6, 96.12 % at A=8. Not a tail effect.

The reading that survives is the block's own LaTeX LABEL — BOND order. C(A,2) is
the complete-graph bond count. Not a rescue by relabelling: CoordinationSaturation
caps rho_A <= C(A,2) from the coordination side with no reference to the jet
filtration. Same number, reached twice.

**2. `graded_reference_simplex_basis_span_probe`** — the coordination basis
C(A,2), C(A,3), C(A,4) that #4316/#4320 decomposes in cannot span rho_grad.
Expanding rho_grad ALONE (no AME, no rho_strong, so not a fit) and pinning on
A=2,3,4: exact at those three by construction, then 0.5639 at A=5, 0.1901 at A=6,
0.007037 at A=8 — a factor 142 short. Cross-check run as a gate: the solve returns
g_4 = 8.371447988, reproducing the '+8.37' helium_four_body_cluster_probe quotes
as the graded reference's own 4-body simplex coefficient. rho_grad grows
factorially (ratios 3.34, 4.71, 6.23, 7.91, 9.78, 11.86) while the basis is
polynomial of degree <= 4. The basis fails exactly where probe 1 shows the
coefficient mass goes.

**NOT claimed** (recorded so it is not written down later): bodyorder_eq_jet_total
stays true — body_eq_graded is a hypothesis FIELD composed with total_eq, a
legitimate 3b-cond conditional, not a self-assuming projection; what is measured
is that its premise cannot be instantiated past 3He. NOT that #4316/#4320 is a fit
— a 3-point solve for 3 coefficients has no freedom to fit with; the charge is
against the basis's SPAN. NOT that the sign pattern is wrong — mu_2=0, mu_3>0,
mu_4<0 is correct arithmetic at its three points; what is added is that the signs
inherit the same restriction to A<=4 as the values, so mu_4<0 is about 4He and not
about 4-body clusters generally. Nothing about rho_strong.

**Corpus-grep note.** My working thesis entering this — 'every live binding
producer computes only the n=2 graded piece, nothing evaluates the tower' — was
WRONG and was caught before being written. 18 producers reference rho_grad and the
deltalambda family already decomposes the residual into mu_2/mu_3/mu_4. Fifth
near-miss of this arc; the four earlier ones landed.

Scope (a) throughout. Nothing wired.


### Third probe (same PR #6393): 'a PURE >=3-body residual' is 1 - 1 = 0

`mu2_vanishing_is_a_normalisation_identity_probe`.
deltalambda_kappa_interface_residual_simplex_probe sets mu2 = M(2) and
residual_pure_ge3body = abs(mu2) < 1e-40, emitting 'Residual is a PURE >=3-body
object: NO edge/2-body component' into its witness. Both A=2 inputs are
self-ratios: rho_grad(2) = [2]_q!/[2]_q! is an empty product returning 1 for ANY
q, and rho_strong(2) = B(2H)/B(2H) = 1 is a literal whose own comment says it is
'the deuteron self-reference ... NOT an independent AME datum'. So mu2 = 1-1 = 0
identically and the flag is True unconditionally.

Demonstrated over 30 combinations (six moduli q = 0.5..2.0, five rho_strong
scalings 0.25x..4x): mu2 exactly 0 at every point, while mu3 ranges
-6.0468..13.5012 and mu4 ranges -85.8784..3.16385.

THE DISTINCTION, and it is the whole point: the kappa refutation next to it is
SOUND -- the #4316 model predicts M(2) = s with s > 0 (fit gives 0.4708), and a
model that CONTRADICTS an identity is refuted by it, so kappa = t/s is ill-posed.
What is NOT supported is reading the same identity as 'a PURE >=3-body residual',
a structural claim about where binding lives. Refuting a model that contradicts
an identity uses the identity correctly; concluding a physical ABSENCE from an
identity does not.

NOT said: not that mu2 is non-zero or that the residual HAS a 2-body component
(the measurement is silent, and an uninformative statistic is not evidence for
the opposite conclusion either); not that #4316/#4320 is a fit; nothing about
mu3 = +0.4708 or mu4 = -4.591, which the transcription reproduces and which is
what validates it.


### Fourth probe (same PR #6393): the log channel does NOT rescue the basis — my own conjecture, refuted

`log_channel_does_not_rescue_simplex_basis_probe`. Conjecture: rho_grad is a
product, so its additive object is the log, and log[k]_q ~ k log q would give
log rho_grad ~ C(A,2) log q — the bond count a THIRD time, aligned with the log
channel the binding producers already use.

REFUTED (i): at the proton pin log q0 = 0.10434, so k*log q does not reach 1
until k = 9.58, and that is optimistic. Measured, log[k]_q is nearer the NAIVE
log k all the way to k = 20; k*log q takes over only between 20 and 50. So
log rho_grad/(C(A,2) log q) is 4.40 at A=4 and DECLINES to 3.34 at A=12.

REFUTED (ii): in the simplex basis, log pred/true goes 0.3741 (A=5), -1.0401
(A=6), -6.78 (A=8), -33.05 (A=12) — sign inversion — against linear's collapse
to 4.53e-7. Neither spans it.

BY-PRODUCT: the log solve also returns g2 = 0 EXACTLY (log rho_grad(2) = log 1 =
0), so the mu_2 = 0 normalisation identity is CHANNEL-INDEPENDENT — it survives
any monotone reparametrisation fixing 1 -> 0. Independent confirmation of the
third probe.

WHAT rho_grad IS at nuclear A: rho/(A!/2) runs 1.31 (A=4) to 39.5 (A=12) while
rho/q^C(A,2) runs 8.42 to 9.67e6. Far nearer the plain factorial (permutation
count, q->1 limit) than the asymptotic. At nuclear A the q-deformation is
SUBLEADING and the leading content is the bare permutation count. This does not
disturb the tower probe (height and positivity are exact combinatorial facts
independent of q) but it does mean the C(A,2) coincidence is about DEGREE
STRUCTURE, not magnitudes.

No replacement basis. After four probes the constructive question — what basis
carries a factorially-growing graded reference — is OPEN, and the two obvious
candidates (polynomial-in-A, and its log) are both measured to fail.


### Cross-PR synthesis with #6394 (2026-08-31)

Sibling #6394 (`qou-23dn`/`qou-gcmn`/`qou-brng`) proves a scope-(b) exclusion:
the chain binding has the exact closed form B(A) = E0*S_off(A0)*g^(A-A0)*(1-f^(A-1))
(four points at 1e-30, two constants), and NO value of g makes it extensive —
bounded if g<=1, at least geometric if g>1. Its f_pp reproduces z_D to 2.8e-31.

That and PR #6393's probe 2 are the same shape-mismatch from opposite ends:
framework objects are MULTIPLICATIVE (geometric g^A; factorial [A]_q!) while the
targets are ADDITIVE (extensive cA; the polynomial coordination basis C(A,k)).

SCOPE, settled from binding_channel_taxonomy_probe (already on main, same bean —
I raised it as an open question on #6394 and then found the corpus had it):

  * #6394's exclusion scopes to the MULTIPLICATIVE trace-difference channel
    (taxonomy channel 1, what binding_canonical ships) — neither extensive nor
    additive over bonds, for any bond set.
  * The LOG / per-bond-energy channels (3, 4, 5) ARE extensive and additive over
    bonds by measurement. They are NOT covered by that exclusion. Their failure
    is separate: a 2-3x magnitude shortfall against AME (at 4He, 24 % pairwise
    share and a 21.4 MeV many-body residual).
  * So: trace-difference family excluded on EXTENSIVITY; log family excluded on
    MAGNITUDE; neither exclusion reaches the other's channel. Recorded on #6394
    so a later reader does not take the (b) wider than its invariant supports.

Probe 4's log-channel refutation does not conflict: it kills taking the log of a
[A]_q!-shaped object at nuclear A (pre-asymptotic), not the log of a geometric
one, whose log IS exactly linear.


## The <g,g> tower walk (PR #6396, 2026-08-31) — rank is Catalan, pairing factors through Temperley-Lieb

TWO probes, answering 'where does the binding error come in' from both ends.

### 1. mirror_pair_em_isolation_probe — the error is NOT electromagnetic
3H/3He are mirror nuclei; in B_sym = alpha[(Z-1)L_pp + L_pn + (N-1)L_nn] the L_pn
terms cancel identically and so does the flavour split delta (it enters only
d_pn), leaving Delta_model = alpha*ln(z(1-h)/(z-h)) -- q0 and the CAL-1 scale
ONLY, no EM input.
  Delta_exp (AME)  = 0.76375488 MeV
  Delta_model      = 0.76532019 MeV     ratio 1.002049 -> 0.205 %
Same fact from the other side: deficits 2.341727 (3H) vs 2.343293 (3He), equal to
0.07 % -- the model's error is ISOSPIN-BLIND.
Writhe normalisation is load-bearing (without it 2.287x) and Lean-proved unique
up to sign, so it cannot have been tuned. It also DISCRIMINATES: B_qCLT_fac gives
0.668x on the same pair.
=> EM right to 0.205 %; the whole residual is STRONG. Weak is not probed by
B(A,Z) at all.

### 2. gg_gram_tower_walk_probe — where the strong channel goes missing
The recorded scope-(a) negative (deuteron_real_sdp at H_6) used the WEDDERBURN
BLOCK basis, where G_lm = tr_M(P_l P_m) = delta_lm tr_M(P_l) is DIAGONAL BY
CONSTRUCTION (orthogonal central idempotents). Its degeneracy is a property of
the basis, not of <g,g>; the one non-zero result was the AME value fed in as the
constraint. NOT overturned -- re-scoped.

On the GB normal-form basis, G_vw = tr_M(T_v T_w), calibrated to 4.94e-51
against pyhecke.gram_matrix_mp at n=3:
  n   dim   rank  corank   C_n
  2     2      2       0     2
  3     6      5       1     5
  4    24     14      10    14
  5   120     42      78    42
RANK = CATALAN NUMBER = dim TL_n, gated. The Markov trace form's radical is
ker(H_n -> TL_n): <g,g> FACTORS THROUGH TEMPERLEY-LIEB. The q-antisymmetriser
(-1/q)^len(w) -- a JET-DEGREE-indexed vector -- lies in the radical at every
level (projection norm 1.0).

Atom at n = 3A, visible fraction C_{3A}/(3A)!: A=1 83.3 %, A=2 18.3 %,
A=3 1.34 %, A=4 0.043 %. PREDICTION from the gated rank law, not measured past
n=5.

DOES NOT explain the deficit quantitatively: if it scaled with the invisible
fraction, 4He would miss by ~2300x; it misses by 3.26. What IS established is
structural -- an SDP on <g,g> cannot select among Hecke elements differing only
in the radical, which is most of them.

CONVERGENCE with qou-unqc / #6395: both say the licensing object cannot be the
Markov trace itself -- there from KMS/traciality, here from the TL radical.


## Convention D IS the Temperley-Lieb specialisation (PR #6397, 2026-08-31)

Follows the tower walk (#6396: rank <g,g> = C_n = dim TL_n at the canonical z).
Two proposed routes out, both measured.

BASIS CANNOT BE THE CAUSE, by pure algebra: rank of a bilinear form is
basis-independent, and a surjection from a larger algebra induces the identical
form on the quotient. So 'do the GB in an algebra projecting onto H_n' cannot
move the rank. Demonstrated: rank(P^T G P) = rank(G) = 14 at n=4.

z_D = q^3/(q^2+1) = q^2 * [1/(q + 1/q)] (identity checked to 1.3e-51). Sweeping
z = q^a/(q+1/q) at n=3,4:
  a     -2  -1   0  0.5   1  1.5   2  2.5   3
  n=3    6   6   6    6   6    6   5    6   6
  n=4   24  24  24   24  24   24  14   24  24
ONLY a=2 degenerates -- an ISOLATED point flanked by full rank at 1.5 and 2.5.

STRUCTURAL IN q: z=q^3/(q^2+1) gives rank (5,14)=(C_3,C_4) at q = 0.8, 1.01,
1.10998, 1.5, 2.0, 3.0 -- every value tested.

=> z_D is not NEAR a TL point, it IS the TL specialisation, exactly, for all q.
Choosing convention D is mathematically the same act as choosing to make the
Frobenius pairing factor through Temperley-Lieb and discard n! - C_n of the
algebra.

ANSWERS. Q1 (pairing not factoring through TL): YES, every z but this one point.
Q2 (fix = v=sqrt(q) with GB upstairs): NO on both halves -- GB by
basis-independence, and sqrt(q) does no work either since half-integer exponents
AND every integer but 2 are full rank. z_C is fine because it is not a=2, not
because it has a sqrt(q). I reported the misleading 'sqrt(q) is the
non-degenerate one' form before running the sweep; corrected in the probe.

TENSION FOR THE OWNER: convention D canonical (ruling 2026-08-15) and convention
D = the TL specialisation were decided on different grounds and never weighed
together. Not a claim the ruling is wrong; a claim that an <g,g>/SDP binding
derivation under D is asking a pairing to distinguish what it provably cannot see.

NOT ESTABLISHED: the symbolic det G(z,q) factorisation TIMED OUT at 600 s, so the
q-independence is EMPIRICAL over six q values, not proved. Which lambda-blocks
die was not computed (rank=C_n implies the >=3-row level-2 Wenzl reading but the
weights were not checked). And NOT that a full-rank pairing would source the
binding.

GIT NOTE: the merge agent checked out its branch under this session's shell
mid-command and my probe commit briefly landed on PR #6395's branch. Caught via
reflog, moved to its own branch, agent's branch restored to origin. Nothing lost
either way. Shared-worktree hazard when dispatching a merge agent while working.


## The two obstructions are INDEPENDENT, and the KMS one costs the link invariant (PR #6399, 2026-08-31)

Explores the convergence of #6395 (KMS: state must be non-tracial) and #6397
(rank: pairing must be off z_D).

1. NON-TRACIALITY DOES NOT RESTORE RANK. Rank of <x,y> = tr_M(h.xy) at z_D:
     h = 1 (plain)                   5   14
     h = T_1 (non-central, invert.)  5   14
     h = T_1 + 2                     5   14
   Identical. For invertible h, x -> hx is a BIJECTION, so
   rad(tr_M(h x y)) = h^-1 . rad(tr_M(xy)) -- same dimension. A unit permutes
   the algebra; it cannot shrink a radical, exactly as a change of basis cannot
   change a rank. T_1's invertibility checked (T_1(T_1-h)=1) not asserted.
   => the two requirements are ORTHOGONAL. Changing z fixes rank but the Markov
   trace at ANY z is still a TRACE (nothing for KMS); a non-tracial weight fixes
   KMS but with invertible h does nothing for rank. BOTH knobs must move.

2. AND (2) IS NOT FREE: MARKOV MOVE I IS TRACIALITY. Markov's theorem needs
   (I) conjugation invariance; for a linear functional phi(g b g^-1) = phi(b)
   holds EXACTLY WHEN phi(ab) = phi(ba). Same condition, not three related ones.
   Measured on H_3, all 36 ordered pairs:
     h = 1    max |phi(ab)-phi(ba)| = 0.0 EXACTLY      move I holds
     h = T_1  max |phi(ab)-phi(ba)| = 0.75270211       move I FAILS
   witness a=(1,0,2), b=(1,2,0); the violation is order the Gram's own singular
   values (0.7527 is its four-fold repeated SV).

TRILEMMA:
  (1) keep tr_M tracial -> KMS only at beta=0, alpha*ln(ratio) unlicensed;
  (2) go non-tracial -> finite-temperature dynamics but MARKOV I FAILS, so it is
      not a link invariant and not the framework's trace in any sense;
  (3) either way the rank problem needs z off the isolated TL point.
(2) is not a cost the framework can obviously pay -- the Jones polynomial, tr_M
as a link invariant, and the braid-closure picture of nucleons all rest on
conjugation invariance.

NOT ESTABLISHED: the non-invertible h case (x -> hx not surjective, so it can
only make the radical LARGER -- not measured); no candidate (h,z) pair proposed;
no SDP run, no binding energy computed. And the trilemma's leg (2) is a
DEFINITIONAL identity -- the measurement demonstrates it, the definition
establishes it.


**2026-08-31 — #6405: widening the isotope table is near-worthless; I proposed it**

Widened 5 → 12 isotopes (³H … ¹⁶O). **Zero shapes changed verdict**; per-α
window 1.29 % tighter ([11.1145, 17.4638] → [11.1145, 17.2392]). Every
exclusion at 12 was already available at A ≤ 7. Correcting my own claim that
this was "the highest-value cheap move" — it was cheap and nearly
information-free.

What it did establish: the discriminator among 8 shapes is **not** growth rate
(`A` excluded, `floor(A/4)` survives despite being 4× smaller asymptotically).
Two small-A constraints do the work — must vanish at A=3 (A=3 caps T at 2.34,
⁴He demands ≥ 11.11), must not increment before A=8 (⁶Li → c ≤ 5.82, ⁷Li →
5.35). So the survivor is a **step function counting complete 4-blocks**.

Caveat recorded in the probe: `floor(A/4)` is built to satisfy those two
constraints, so its survival is weak evidence, not support. The defensible
claim is the negative one.

`computations/wide_isotope_window_test_probe.py`, PR #6405.


**CORRECTION, same day — the corpus already had the 4-block shape (sixth
near-miss on this arc)**

`docs/audits/2026-08-02-alpha-cluster-su4-extensive-term.md` (`qou-0c19`,
`qou-uclw`) identified the extensive term as the α-cluster SU(4) `[1⁴]` volume
term on 2026-08-02, **with the shape written as `n_α = ⌊A/4⌋`**, backed by the
sorry-free `QOU.MassTheory.su4_supermultiplet_dim_vanishes_iff`
(`Nat.choose 4 A = 0 ↔ 4 < A`). Block size four is structural: no `[1⁵]`.

Cuts both ways. **For me:** `⌊A/4⌋` predates the test, so it is pre-registered,
not post-hoc — my "close to circular" caveat was wrong and understated the
result. **Against me:** the other seven shapes are still mine, chosen knowing
which should survive, so the caveat relocates rather than vanishes.

New, narrowly: 2026-08-02 was a scaling observation on α-conjugate nuclei only;
this is an exclusion test including the non-α-conjugate ones (³H ³He ⁶Li ⁷Li
⁹Be ¹⁰B ¹¹B ¹⁴N). The two small-A constraints independently rediscover the gate
from the AME side.

Not a conflict: audit's ~29.8 MeV is the TOTAL per α; `c ∈ [11.11, 17.24]` is
the EXCESS over pairwise. ⁴He reconstructs to `B_AME = 28.2957`.

**Follow-up WITHDRAWN.** "Derive the 4-block counting" is partly answered
(gate proved) and partly forbidden: the bridge to `B = n_α·B_α` is reasoned-not-
proved, and the dimensionful per-α scale is FOREVER-GATED — `8G·c·m_e`,
`c = 7.956`, was tested there and refused as numerology. Do not re-propose it.

PR #6405 commit `be3797f5e5`.


**2026-08-31 — #6407: the ruled trefoil beats production 9.45× on the deuteron**

Joined Owner Ruling A (deuteron knot = trefoil `T(2,3)`, a **volume** ruling) to
the already-tabulated writhe-normalised stacked scalar. `T(2,3)` = closure of
`σ³` in `B₂` ⇒ the ruling fixes `m = 3`, and that row was already in the table:
**2.1601931 MeV, −2.89 %** against production's **+27.36 %**.

Hopf (`σ²`) lands at −78.5 %, so the ruling's *own* canonical/linear-chain
distinction picks out the working one — a fit would have taken either.

**Suggestive, not a result.** Look-elsewhere `p ≈ 0.121` (computed: 11 positive
candidates over 0.48–12.2 MeV); `mu_eff` is a braid-WORD property not a link
invariant; and it leaves the sector's real defect untouched.

**Strategic finding (the important half):** the two-nucleon sector's failure is
a **SIGN** error, not a precision one — the framework binds the diproton
(+2.5416) and dineutron (+3.3069) where nature has none, and
`QOU.QBeta.single_crossing_binds` proves sorry-free that no single crossing can
unbind while `q³ < q²+1`. **No amount of magnitude work reaches L2 while a
predicted observable has the wrong sign.** Signs before digits.


**2026-08-31 — the even-negative stacked branch is CLOSED (two exclusions), and
#6407's framing retracted**

Worked the branch named in `SingleCrossingAlwaysBinds` as the one survivor
("a repair *direction*, not a repair"). **It is not a direction.**

**Scope (a) — 6.13× is a MINIMUM.** `m = −60..60`: 30 unbinding powers, all
even-negative, `|B|` monotone in `|m|`. `σ^-2` at −0.6127 MeV is the global
minimum; every other member is worse. Exact mechanism: `mu_eff(-2k) ~
A·(q²/(1−h))^k`, `q²/(1−h) = 1.5577`, measured ratios 1.203→1.255→1.310→1.364.
Nature needs `mu_eff = 1.0242`; smallest available excess over 1 is 0.1576 vs a
needed 0.0242.

**Scope (b) — projector ∘ stacking excluded, invariant named.** At `m = 2` it
looks promising (`B(T=1) = −0.0375`, within 2× not 6×) then dies for every `m`
on `mu₊ + mu₋ = 1` — the partition of unity holds for any substituted scalar, so
`mu₊ > 1 ⟺ mu₋ < 0` and `B` is undefined. **Unbinding T=1 destroys the T=0
channel that must hold the deuteron.**

**RETRACTED my own #6407 framing** (arithmetic stands). It said "one leg of
three"; there are **four** channels, and pn ³S₁ / pn ¹S₀ share content with
opposite boundness ⇒ a content-keyed word is refuted in Lean
(`content_keyed_interface_refuted`). The −2.89 % survives only if keyed on
isospin `T`.

**Sector status: every mechanism in the algebra is now excluded for the unbound
channels** — single-crossing (b), stacked-alone (a), projector∘stacking (b), and
T=0-as-deuteron (the `α·ln4 = 5.803` floor, AME 61.7 % below). Selection is
derived; magnitude has no surviving carrier. Needs something outside the family;
no candidate proposed.

**2026-08-31 — owner selected all four routes; 2 and 3 worked**

**Route 2 (Hoefsmit off-diagonal) — CLOSED, scope (b), #6408.** Solved the
`V_(2,1)` block in closed form from the braid relation (residual 4.7e-51). Four
exact identities: `a = −(z−h)`, `d = z`, `b·c = μ₊`, `z(z−h) = μ₋`. **So the
projectors ARE the bond family's block** — one 2×2 object read two ways, never
two independent attempts. `|b| = √(1 − z(z−h)) = 0.8676 < 1` ⇒ binds, and for
every `q` since `h < z` is `h_lt_markov_z` (sorry-free). Unbinding needs `h > z`
— the same wall, missed by 24 %.

**Route 3 (re-scope ¹S₀) — SPLIT; only the smaller half survives.**
- **Withdrawn:** the −0.066 MeV *energy* as a target. It is a virtual state
  (second-sheet pole, `a_s ≈ −23.7 fm` vs ~1.4 fm range), not a bound-state
  energy, and reaching it from `α = 4.186 MeV` needs a 1.6 % cancellation with
  no small parameter. Pre-emptive: nothing currently scores it.
- **🛑 RETAINED and FAILED:** "pp and nn are unbound". `B(pp) = +2.5416`,
  `B(nn) = +3.3069`. **Boundness is a sign, not a magnitude.** Re-scoping the
  energy does not retire the sign error, and a re-scope that took the whole row
  would be using a real observation about one quantity to retire a failure about
  another.

L2 headline **unchanged**: 1/5 scoreable, 0/5 unconditional. No number improved.

**Remaining: routes 1 (non-separable `(S,L)` coupling, `qou-vbyi`) and 4
(non-tracial functional).** Neither is an object already in the algebra — which
is now the point: every excluded route is a *scalar read off one block*, and two
of them were the same scalar.


## 2026-09-03 — the extensive term MEASURED at four nuclei, and the ceiling reached

PR #6427. The corrected binding path (Rust LP-accumulator kernel + the
braid-satisfying seminormal family) runs end to end for the first time. Writing
B_true = B_pred + E(A):

    atom       A  B_pred (MeV)   AME2020     E = AME-B_pred   E/C(A,2)
    deuterium  2  -7.271102125   +2.224566    9.496           9.496
    tritium    3  -7.742121347   +8.481796   16.224           5.408
    he3        3  -7.456199506   +7.718041   15.174           5.058
    he4        4  -6.828594293  +28.295662   35.124           5.854

THE PREDICTION IS FLAT WHERE BINDING IS EXTENSIVE. Prediction spread 12.5% of its
mean against an AME range of 12.7x; |pred| vs AME r = -0.731. 4He is sharpest:
LOWEST |pred| at the HIGHEST binding. Neither a sign flip nor a constant rescale
repairs it (ratios run 3.269 .. 0.241, spanning 13.6x) -- nothing multiplicative
fixes a quantity that is flat where the target is extensive.

This is the FIRST DIRECT MEASUREMENT of this bean's missing term. Prior work
inferred it from six failed closures; this exhibits it, at four nuclei.

TARGET, and its weakness stated. Excluding the deuteron (owner-ruled special),
E/C(A,2) = 5.408, 5.058, 5.854 -- spread 14.6%, against E/A 58% and E/(A-1) 45%.
So E ~= 5.4 MeV x C(A,2) for A >= 3. BUT: two distinct A values, and the
within-A noise floor is 6.7% (tritium vs he3 at the same A), so the signal is only
2.2x noise. A TARGET, not a determination.

TENSION WITH THE PROVED CAP, flagged not smoothed. An E scaling AS C(A,2) is
pairwise-shaped, while this bean's framing says super-pairwise and
exchangeDet_pow_two_le_four proves rho_A <= C(A,2). Three readings: two-point
artefact; E SATURATES the cap (<= permits proportional-to); or super-pairwise
growth visible only above A~5.

DISCRIMINATOR NOT MEASURED. 6Li (C(A,2)=15 vs 4He's 6) is where the forms
diverge. THREE attempts, all killed, each earlier than the last (~900s / 326s /
124s). Cause undetermined -- dmesg unavailable, OOM neither confirmed nor
excluded. A=2..4 complete reliably (942/1568/1496/2425s) including across long
idles, so this is specific to A=6.

CEILING: the corrected binding path reaches A=4 in this container, not A=6.

TWO ROUTES TO SETTLE IT, neither attempted:
  1. A=6 on a machine that holds the process. Nothing about the computation is
     known to be wrong; it is scheduling.
  2. A=4 and A=6 both at reduced k_exact -- not comparable to the k=11 points,
     but comparable to EACH OTHER, so E(6)/E(4) discriminates cheaply. A
     different measurement needing its own gate.

## 2026-09-03 — RETRACTION of the `E ≈ 5.4 × C(A,2)` target above, and what replaced it

**The target in the previous entry is WITHDRAWN. Do not carry it forward.** It
is mostly an artefact of the arithmetic, not a finding about the framework.

The mechanism: `E := AME − B_pred`, and the entry immediately above establishes
that `B_pred ≈ −7.3 MeV` is **near-constant** across nuclei. So
`E ≈ AME + 7.3`, and `E/C(A,2) ≈ (AME + 7.3)/C(A,2)` — a statement about
**AME2020 plus an offset**, with almost no framework content in it. Measured:

    nucleus   A    AME     E/C(A,2)   (AME+7.3)/C(A,2)
    ²H        2    2.225     9.496          9.525
    ³H        3    8.482     5.408          5.261
    ³He       3    7.718     5.058          5.006
    ⁴He       4   28.296     5.854          5.933

The last two columns agree to **~1 %**. And `AME/C(A,2)` is not constant — it
is 2.225, 2.827, **4.716**, 2.133, 1.869, 1.396 for ²H/³H/⁴He/⁶Li/⁷Li/¹²C: it
**peaks at ⁴He and falls steeply**. The near-constancy was a three-point
coincidence in the region where the AME curve happens to turn over; ⁶Li breaks
it on AME grounds alone (≈2.62 with the offset), before the framework is
consulted.

The `E/C(A,2)` figure therefore does **not** bear on the pairwise-cap tension
flagged in the previous entry — that tension is withdrawn along with the
figure, not resolved.

### What the retraction bought: a better experiment

The informative measurement is **`B_pred` itself as a function of `A`**, with
no experimental normalisation anywhere in it — so nothing about AME can
contaminate it. Run as a **paired** comparison of ⁴He and ⁶Li at *matched*
truncation `k_exact`, which also sidesteps the A=6 wall (three full
`binding_energy` attempts at ⁶Li were killed at ~900 s / 326 s / 124 s):

    k_exact   ⁴He (A=4)      ⁶Li (A=6)      ratio li6/he4
      5      -0.375110164   -0.539212954       1.4375
      6      -0.838749076   -0.992757495       1.1836
      7      -1.515118319   -1.414063111       0.9333
      8      -2.153722974   -2.183158129       1.0137
      9      -3.711581534   -3.404340982       0.9172
     10      -5.669659692   -5.467686217       0.9644

`A` grows 1.5×; `C(A,2)` grows 2.5×; the accumulator ratio sits in
**0.917 … 1.014 for k ≥ 7** (mean 0.957). **The flatness extends to A = 6** —
`B_pred` carries essentially no `A`-dependence over a range where binding grows
by 3.5×. That is the finding the withdrawn target was obscuring, and it is the
direct measurement this bean's missing extensive term needs.

Scope: this is a scope-(a) statement about the current `unified_iterative_correction`
path at truncations k = 5…10 — not a structural exclusion of any ingredient.
Audit: `docs/audits/2026-09-02-binding-energy-first-corrected-value.md`; PR #6427.


### k = 11 (production truncation) — both legs, added 2026-09-03

The ladder above was extended to the production truncation. Both legs completed:

    he4   A=4  k=11   uic = -8.201558468      1104 s
    li6   A=6  k=11   uic = -7.794544740      1269 s
                            ratio li6/he4 = 0.9504

So the k >= 7 ratios are 0.933, 1.014, 0.917, 0.964, **0.950** — mean **0.956**,
spread ±5 %, no trend in k, while `A` grows 1.5x and `C(A,2)` grows 2.5x.
**k = 11 was the one rung that is not a reduced-cost proxy, and it behaves like
the rest.** The flatness is not a truncation artefact.

(The 6Li leg took two attempts: the first died to a worker-process restart at
~1919 s, an environment event, NOT the A=6 compute ceiling the three earlier
full-`binding_energy` kills established. The driver is resumable, so only that
one cell was recomputed.)

**A separate defect surfaced by the same run, worth its own attention:** 4He's
|uic| runs 1.52 -> 2.15 -> 3.71 -> 5.67 -> 8.20 across k = 7..11 with the
increments still GROWING (0.64, 1.56, 1.96, 2.53). **The accumulator is not
converged at the production truncation.** The absolute B_pred values in the
four-nucleus table are therefore truncation-limited; the matched-k ratio is not,
which is why the flatness claim rests on the ratio and not on the values.

## 2026-09-01 — two exclusions, both against invariants rather than fits (PR #6414)

**1. All-pairs-with-distance-decay is excluded by R8's t-ladder interior maximum.**
Tested against `saturating_shared_channel_probe`'s invariant, not against AME.
CLAIM A (formalize-first, stated before the scan): if every `L_XY > 0` and the
`k -> k+1` step appends a contiguous block without splitting an adjacency, every
existing pair keeps its separation and every new pair adds a strictly positive
`L*r^(s-1)`, so `V(k)` strictly increases for EVERY `(r_pp, r_nn, r_pn) in
(0,1]^3` and P1 excludes it. **Decay buys nothing** — it shrinks contributions
but never removes one. Confirmed, 0 violations / 1000 grid points. The two
SPLITTING orderings also went non-monotone at zero points, which Claim A does not
predict. At the framework's own derived rates `V = 12.79, 30.41, 54.11, 83.52`,
monotone. The arrangement-free bound is INCONCLUSIVE and is kept as such
(`Lo(19)=44.46` vs `Up(15)=72.60`, overlapping); a 400-sample arrangement search
closes it empirically only (margin +22.58).

**2. The 22.25:1 channel asymmetry is excluded by an EXACT inequality.** The
eigenvalue criterion's falsification named 'whatever breaks the bar symmetry',
and `delta` is the sector's only bar-breaking. Checked exactly: `d_pn = w*d_nn +
(1-w)*d_pp` with `w = 1/2 - delta/4`, so `delta/4` IS the isospin-mixing
asymmetry. Then for `R(d) = |log|l_-||/|log|l_+||` (alpha-free):

    R(d) <= 1 for every admissible d in [-h,0],
    equality iff |l_+| = |l_-| OR |det T| = 1.

Proof: `|det T| = 1 + s(h-s) >= 1` so `log|l_+| + log|l_-| >= 0`; both cases give
`R <= 1`. Nature needs `R ~ 22.25 > 1`, so the family is excluded **on the wrong
side of 1**, not merely short. `delta` is a 1.4e-3 displacement inside that
range and could not have helped. Scope (b).

**Two corrections to my own claims, both caught by the sweep and both recorded
with assertions:** I first called R's range 'a narrow band around 1' (false — min
is 0.00119), and I first stated equality as 'iff |det| = 1' (incomplete — the
midpoint `d = -h/2` has `|det| = 1.0109` yet `R = 1`, because the moduli coincide).

**Found on the way, unsought:** `L_nn > L_pn > L_pp`. In the bond-graph functional
a larger `L` is MORE binding, so the hierarchy is n-n most bound, p-p least —
inverted against the two-nucleon data. Does not contradict the eigenvalue
criterion's 4/4 signs (different functional, built from eigenvalues not `L`), but
the one that gets the channels wrong is the one the whole bond-graph binding path
is built on. Flagged, not chased.

**Also found:** R9 states its invariant as `0 = M(1) < ...`; its own `modelg_miss`
returns `M(1) = +0.1219` and the witness row carries `resid_MeV = -0.1218526` —
witness and consumer define the residual with opposite signs. The invariant is
unaffected (P1 needs the turnover), but the `0 =` is a simplification of the
code's output, not a computed zero.

**Where this leaves the arc:** the missing structure is not in the bond letter,
and not in a decayed pair sum. Next candidates are outside the one-crossing
algebra.

## 2026-09-01 (later) — RETRACTION + the blind-sector determinant (PR #6414)

**RETRACTED, same PR, same day:** my scope-(b) claim that "a bigger irrep does
NOT escape the R <= 1 bound — det rho(w) = +-1 in every irrep". **False.**
Verified on ONE irrep (H_3's 2-dim, where m+ = m- by accident of that block) and
generalised. Counterexample in any H_n: the sign rep `sigma -> -1/q` satisfies
the Hecke quadratic exactly, `|det| = 1/q = 0.90092 < 1` — the escape condition
my own bound names.

**Correct statement (exact):** `|det rho_lambda(sigma_i)| = q^(m+ - m-)` with
m+/m- the SYT counts placing i,i+1 in a row/column. So `|det| = 1` iff m+ = m-,
and the escape is open on **column-heavy** partitions — combinatorial, not
accidental.

**What I expected and did NOT find.** Column-heavy = many rows, and Step 27 says
convention D's SU(2)/TL trace is blind above two rows, so I expected escape-set
== blind-set. Measured over all 65 partitions of n = 2..8: **they do not
coincide.** One-way only —
`column-heavy ==> TL-blind` (1 exception, `(1,1)` at n=2);
`TL-blind =/=> column-heavy` (14 counterexamples). Escape set strictly smaller.

**At n = 6** (deuteron 3A): 5 escaping blocks — (3,1,1,1), (2,2,2), (2,2,1,1),
(2,1,1,1,1), (1^6), 30 dims. Sum of squared dims = 720 = 6!, the same 720 Step
27 reports, from the Wedderburn side — one object, two analyses.

**Discriminates Step 27's two blocks,** which it treats symmetrically (sums their
phases): `(3,2,1)` is **det-locked** (m+=m-=8, |det|=1 for every braid word at
every writhe); `(2,2,1,1)` is **free** (|det| = q^-3e).

**Scope limit, stated:** `Delta_bind = beta_atom - beta_free` is a DIFFERENCE of
braid words, not group-like, so its det is unconstrained in either block. This
does NOT discriminate Step 27's eigenphases directly — only which mechanisms
built from braid words alone are available.

**The R <= 1 bound is UNAFFECTED** (regular rep, computed directly, never via the
irrep argument). Retraction landed on both surfaces — new probe + the original's
docstring, 3 print sites and its assertion message.

## 2026-09-01 (third pass) — |det| = 1 does NOT close a d > 2 block

**Third retraction in one arc, and this one reaches the physics.** Section [3c]
of `irrep_determinant_escape_probe` said "(3,2,1) is det-locked, so the R <= 1
argument closes that block outright". The det-lock is real; **the closure does
not follow.** `R <= 1` was derived for a 2x2, where `sum_i log|l_i| = log|det|`
is one equation on TWO unknowns and pins their ratio. In dimension d it leaves
`d-2` free — and `dim (3,2,1) = 16`.

**Demonstrated** in the 6-dim regular rep of H_3 (quadratic, braid relation and
inverse all asserted): `s1^2 s2^2` has `|det| = 1` and log-modulus ratio
**exactly 2** — moduli `q^4, q^2, q^2, q^-2, q^-2, q^-4`, each checked against
the exact power of q to 1e-18.

**So the R <= 1 bound is a TWO-DIMENSIONAL fact and does not extend** — which is
exactly why the blind sector's high-dimensional blocks are not excluded by it.

**Near-miss:** my first test was `s1`, `s1*s2`, `s1*s2*s1` — all ratio 1.0, and
on those three I was about to retract a *correct* correction. Their 2-dim block
is elliptic. One more crossing breaks it.

**Two further corrections caught before shipping:**
1. With the near-unit floor at 1e-15 the enumeration returned ratio **7.75e9**
   at `AABAAB` and read "reaches 22.25: True". Artefact — four moduli are 1 to
   within 8.08e-11 (repeated char-poly root), so the ratio divided a real
   log-modulus by dust. Floor now 1e-8. **Honest max: 5.0 at `abaab` over all
   5456 words of length <= 6, 0 unresolved. Does NOT reach 22.2457.**
2. I claimed "the achievable set is DISCRETE — ratios of integers" while
   printing ROUNDED k beside my own check's "all integers? False" for `Baa`. The
   rounding hid the counterexample. Measured: all-**positive** words have
   integer-power moduli; mixed-sign need not (`Baa` -> ratio 2.032154824). Not
   discrete; only its positive-word part is.

**Unaffected:** the `R <= 1` bound on the bond-letter family stands (genuinely
2x2, in H_2's regular rep).

**Open:** whether the per-channel R (two eigenvalues of a d-dim block assigned to
the two isospin channels) is even well-defined — unanswered, and it gates any
use of the blind sector for the asymmetry.

## 2026-09-01 (fourth pass) — the isospin-channel R is EXACTLY 1 everywhere

**Strongest result of the arc, and it is one line.** Every Hecke generator
satisfies `(sigma - q)(sigma + 1/q) = 0`, so its **minimal polynomial divides**
`(x-q)(x+1/q)` in ANY representation. Hence `spec(rho(sigma_i)) ⊂ {q, -1/q}` at
every dimension — only multiplicities vary. The isospin channels are `sigma`'s
**spectral projectors**, each carrying one of those two eigenvalues whatever its
rank. So `B(T=1) = -alpha log q`, `B(T=0) = +alpha log q`, **`R = 1` exactly, in
every block, at every dimension.** Nature needs 22.2457.

**The single-crossing isospin criterion is excluded EVERYWHERE** — not just the
bond-letter family, not just 2-dim, blind sector included.

Verified by **exact matrix identity, no root-finding**: `(M-qI)(M+I/q)` residual
`5.584e-42` for s1, s2 and two conjugates.

**🛑 This undercuts my own previous entry.** I had written that the `R <= 1`
bound is 2-dimensional "which is why the blind sector's high-dimensional blocks
are not excluded by it". True about the *bound*, misleading about the physics —
the argument above excludes them anyway, with no determinant reasoning.
"Not excluded by THAT bound" ≠ "not excluded". Corrected at source.

**Does not contradict the measured 5.0 spread** — different operators. `sigma`
satisfies the quadratic (5.6e-42); the word `s1^2 s2^2` does not (same product =
0.429342), so its spectrum genuinely spreads. But a word's eigenprojectors are
not `sigma`'s, so the spread is unavailable to the channels as defined.

**Where the problem now sits:**
| construction | asymmetry | status |
|---|---|---|
| single crossing, any dim | R = 1 exactly | EXCLUDED |
| bond-letter family, 2-dim | R <= 1 | EXCLUDED |
| multi-crossing word, d > 2 | up to 5.0 | **OPEN** |

Only the third survives, and its obstacle is **not a bound** — nobody has said
which operator the two isospin channels are the spectral projectors OF once the
object is a word rather than a crossing. **Definitional question, and now the
gate.**

**Method note worth more than the result:** my first check was numerical
(eigenvalues, membership in `{q,1/q}` at 1e-25) and reported FALSE against a
one-line proof — `polyroots` resolves a triple root to only ~3e-15, so the
tolerance was tighter than the instrument. **When a claim is algebraic, test it
algebraically.** Three root-finding artefacts have misled this session:
`mp.eig` non-convergence, a 7.75e9 ratio from a repeated root, and this.

## 2026-09-01 (fifth pass) — the pairwise route is CLOSED FROM BOTH ENDS

Completes the minimal-polynomial argument from adjacent crossings to **arbitrary
separation**. A pair at separation `s > 1` exchanges via the **band generator**
`a_ij = (s_{j-1}...s_{i+1}) s_i (s_{i+1}^-1...s_{j-1}^-1)`, a **conjugate of
`s_i` by construction**. Conjugation preserves spectrum ⇒ spectrum `{q, -1/q}`
⇒ **`R = 1` for that pair too**.

Verified two ways, not asserted: `a_ij` really is the `(i,j)` transposition
(checked in `S_4` at separations 1, 2, 3), and the H_3 instance
`a_02 = s2 s1 s2^-1` satisfies the Hecke quadratic to `5.584e-42`.

**⇒ THE ENTIRE PAIRWISE-EXCHANGE PICTURE HAS R = 1** — every pair, every
separation, every representation. The channel asymmetry cannot come from any
single exchange.

**How it composes:** `allpairs_decay_turnover_exclusion_probe` ruled out
*summing* pairwise contributions with distance decay; this rules out the
pairwise contributions *themselves* carrying the asymmetry. **Closed from both
ends, by two independent arguments sharing no machinery.**

**Surviving space:** only genuinely NON-CONJUGATE multi-crossing objects — a
product `sigma_i sigma_j`, or `Delta_bind` — and those are not exchanges of a
pair. Obstacle is definitional, not a bound: which operator are the two isospin
channels the spectral projectors OF, once the object is not a pair exchange?
**That is the gate.**

## 2026-09-01 (sixth pass) — the full catalogue; a far-commuting product is ALSO R = 1

**Closes a row I had named as surviving.** Last pass I listed "a product
`sigma_i sigma_j`" as a live candidate. It is not.

**Far-commuting product.** For `|i-j| >= 2` the generators commute, span
`H_2 ⊗ H_2`, and the product's spectrum is the **product set**
`{q,-1/q} × {q,-1/q} = {q², -1, -1, 1/q²}`. Moduli `{q², 1, 1, 1/q²}` — the two
non-unit log-moduli are **both `2 log q`**, so **R = 1 exactly**. Verified on the
exact `H_2 ⊗ H_2` model: commutator 0.0, quadratic 0.0, ratio asserted to 1e-12.

Physically: nucleons far enough apart that their generators commute cannot carry
the asymmetry even as a product. With the band-generator result, **no separated
pair contributes by any route.**

**THE CATALOGUE (all measured in PR #6414):**

| object | R |
|---|---|
| single crossing, any rep, any dimension | 1 exactly |
| pair exchange at ANY separation (band generator) | 1 exactly |
| `sigma_i^k`, any power k (checked k=1..5) | 1 exactly |
| far-commuting product `sigma_i sigma_j` | 1 exactly |
| adjacent 2-crossing product `sigma_i sigma_j` | 1 |
| **>= 3 crossings, BOTH non-commuting generators** | **up to 5.0** |

Measured minimum for any spread: **both generators present AND total length >= 3.**
Nothing of length 1 or 2 spreads; no power of a single generator spreads at any
exponent.

**⇒ THE ASYMMETRY REQUIRES AN ADJACENT, MULTIPLY-BRAIDED OBJECT** — three or more
crossings on two non-commuting strands. Not a pair, not a product, not a power:
it needs the braid-relation region itself. Against nature's 22.2457, the measured
spread reaches only 5.0 (a lower bound — length <= 6 in H_3).

This agrees with the corpus's own super-pairwise conclusion reached from the AME
side, by a completely different route.

**Gate (definitional, not a bound):** which operator are the two isospin channels
the spectral projectors OF, once the object is not a pair exchange? Do not invent
an identification and fit to it.

## 2026-09-01 (correction) — the target ratio is 33.7055, not 22.2457

**What I asserted.** **Five** sites above quote nature's channel asymmetry as
the superseded figure, under **two spellings** — and a grep for either spelling
alone finds under half of them:

| spelling | site |
|---|---|
| `22.25` | "The 22.25:1 channel asymmetry is excluded by an EXACT inequality" (two exclusions) |
| `22.25` | "Nature needs `R ~ 22.25 > 1`, so the family is excluded on the wrong side of 1" |
| `22.2457` | "Does NOT reach 22.2457" (the length-<=6 regular-rep sweep) |
| `22.2457` | "Nature needs 22.2457" (the exactly-`R = 1` minimal-polynomial result) |
| `22.2457` | "Against nature's 22.2457, the measured spread reaches only 5.0" |

(A sixth occurrence, "reaches 22.25: True", is the label of a *rejected*
7.75e9 artefact and is part of that entry's own correction, not a claim.)

Those five sentences are left standing above as the dated record of what was
measured against; this section is what supersedes the figure in them.

**I got this wrong once already, in this very section.** It first said "three
entries", having grepped only `22.2457` — the exact one-spelling miss AGENTS.md
records for the `4.6e6`/`4.66e6` figure. Corrected on re-measure. If you drain
this figure further, grep **both** spellings.

**What is actually true.** The error was methodological, not arithmetic. A
*channel* asymmetry must compare **the same pair** across two isospin channels.
I compared the deuteron (np, T=0, +2.224566 MeV) against pp/nn (~0.1 MeV) — a
**different pair** — which conflates pair identity with isospin. The correct
denominator is the np ¹S₀ **virtual state** (~0.066 MeV): the same np pair,
differing only in isospin.

    2.224566 / 0.066 = 33.7055   correct   (67.4 at half, 16.9 at double)
    2.224566 / 0.1   = 22.2457   what the three entries above quote

Caught by `main`'s `1d9d3500f5` (beans `t7qv` / `m896`), which reached this
arc's central result independently from Pauli.

**Every conclusion in this bean is unaffected or strengthened; none flips.**

- `R <= 1` on the bond-letter hull — unaffected. `33.7 > 22.25 > 1`.
- The fine-tuning verdict is **sharper by three and a half orders**. The letter
  that would reach nature's ratio sits **5.94e-11** from the isospin projector,
  where the 22.2457 comparison put it at 1.78e-7. A 2e-7 fine-tuning was already
  the reason to read that localisation as evidence *against* the letter; 6e-11
  is more so.
- The regular-rep spread still maxes at **5.0** and still does not reach the
  target — "reaches it? False" under either figure, by a wider margin under the
  correct one.

**Where else the figure went, and where it now stands.** It was live in four
probe scripts and in this bean. All four probes were drained in
`fix(qou-brng): drain the 22.2457 -> 33.7055 correction to all four probes`,
at every computational site and in prose, with the reason recorded at each site:

- `computations/probes/allpairs_decay_turnover_exclusion_probe.py`
- `computations/probes/channel_asymmetry_letter_family_bound_probe.py`
- `computations/probes/irrep_determinant_escape_probe.py`
- `computations/probes/regular_rep_modulus_spread_probe.py`

The bean was the fifth surface and was missed by that pass — which is the exact
trap that commit message names ("correcting one surface and leaving the others").
Recorded here rather than by editing the three dated entries, so the record of
what was compared against remains readable.

## 2026-09-02 — the n=2 isospin cap does NOT survive the 3-strand lift; ceiling is 9

`computations/probes/block_transposition_lift_probe.py` (PR #6415, commit b17fc1b609).
Takes the step main's `t7qv/m896` flagged as out of scope: 'this is the n=2
interface only, not lifted to the 3-strands-per-nucleon construction'.

A nucleon is three strands, so the exchange operator is the 3-block transposition
Delta_{3,3} = (s3 s2 s1)(s4 s3 s2)(s5 s4 s3) in B_6 — 9 crossings, verified to
induce the block swap exactly. Forced by the construction, not selected.

Exhaustive over all 11 Wedderburn blocks of H_6:

  * **Every eigenvalue modulus is exactly q^k, k an INTEGER.** Deviation falls
    3.4e-7 / 9.1e-10 / 1.2e-14 / 1.8e-22 at dps 30/40/60/90 — exact, not
    approximate. So the asymmetry is a COUNTING quantity and cannot be tuned.
  * **The n=2 cap of 1 breaks**: max 5 in-block at (4,2) — a 2-row, TL-VISIBLE
    block — and 9 across blocks. Achievable set is discrete {1, 2, 5}.
  * **But the ceiling is 9 against nature's 33.7.** Scope (a): Delta_{3,3} alone
    does not supply the observed channel asymmetry from its trace-visible
    spectrum. A closure adding a further term is untouched.
  * **Three blocks carry k=0 (|lambda|=1), for which the ratio is UNBOUNDED** —
    and every one of those is trace-blind (rows > 2), while no trace-visible
    block carries one. Both directions exact, asserted. So the unbounded
    asymmetry exists in this construction but lives entirely in the sector the
    Markov trace cannot see under convention D's row cap l(lambda) <= 2. That
    is the 'computable but not directly observable' class the owner raised.

Internal checks asserted: trivial/sign reps give k = +9/-9 (9 crossings at
sigma -> q and -1/q); conjugation duality k(lambda') = -k(lambda) holds for all
11 blocks.

TRAP recorded in-probe: the first version thresholded near-unit moduli at
UNIT_FLOOR=1e-8 and reported ratio 8888561 for (3,2,1) — numerical dust, the
same artefact class caught twice earlier this session at a 1e-15 floor. Fix was
NOT a bigger floor: the integer quantization removes the need for a threshold
entirely, and a threshold-free test cannot be defeated by choosing the threshold
badly. That version also filtered k=0 silently, which would have made 'ceiling
9' stronger than the measurement supports; now stated with the proviso explicit.

OPEN: whether the unbounded trace-blind sector is reachable by subtraction.
Locating it is not reaching it.

## 2026-09-02 — subtraction-recovery of the blind sector is CLOSED (negative)

`computations/probes/markov_trace_family_rank_probe.py` (PR #6415, 9f97474c46).
Answers the question the lift probe left open, negatively.

The Ocneanu weight at z_N = q^N/[N]_q is the SU(N) quantum dimension (quantum
hook-content formula), vanishing exactly when ell(lambda) > N — row cap asserted
on 178 (lambda,N) pairs. Higher N lifts the cap, so the hope was a finite
combination isolating a blind block.

MEASURED (SVD and Gram-Schmidt, agreeing at every n):

    n       2   3   4   5   6   7
    p(n)    2   3   5   7  11  15
    rank    2   3   4   5   6   7     -> rank = n EXACTLY

Singular-value gap at n=6: 2.23e-13 retained vs 1.74e-121 discarded, ~108
orders. Not a threshold judgement.

**Only the two ONE-DIMENSIONAL blocks are individually recoverable.** So the
answer is no — and the reason is stronger than the question assumed: **the
recoverability boundary is NOT the row cap.** (4,2) is trace-VISIBLE, carries
the largest finite asymmetry found (ratio 5), and is still not isolable.

Also settles the H_3 three-trace combination (6.22044128, -33.41778449,
28.19734321): it works because p(3)=3=rank, i.e. n=3 is COMPLETE. It does NOT
generalise — from n=4 on, p(n) > n. Asserted at both ends.

Scope (a), narrowly: excludes the Ocneanu/Markov trace family parameterised by
N and nothing else. Non-Markov-trace functionals untouched — that is where a
closure must now come from. rank=n is measured at n=2..7, not proved; a proof
would upgrade this to scope (b) and is the obvious formalize-first target.

TRAPS recorded in-probe: (1) mp.lu_solve does not raise on a singular system —
returned 1e57 coefficients with residual 1.0 at 60 dps; precision scaling
(1e119 at 120 dps, 'numerically singular' at 240) is what settled singular vs
ill-conditioned. (2) Column normalisation changes the row space, so residual
distances from a normalised SVD answer a different question; rank and
membership survive, distances do not. Conjugation symmetry exposed it.

CONSEQUENCE for the arc: the three routes past the ceiling of 9 that I could
name are now (i) a non-Markov-trace functional, (ii) a further additive term in
the closure, (iii) higher n. Subtraction over the trace family is closed.

## 2026-09-02 — sibling convergence with qou-r1yj: same spectrum, no conflict

de5c18f588 (t7qv/r1yj, `main`) did the SAME six-strand lift from a different
session, same day, neither knowing of the other. Reconciled in
`block_transposition_lift_probe` (a42e580e0b / rebased 5828849a49) as an
ASSERTION, not a remark.

**Spectra identical.** Union of exponents over the four trace-visible blocks is
{-3,-1,2,3,5,6,9} = r1yj's seven magnitudes. Independent confirmation.

**Sign convention differs** — r1yj reports L/log q negated, so its bound {3,1}
and unbound {-2,-3,-5,-6,-9} are that set negated. Recorded so nobody
'corrects' one into the other.

**The ratios answer different questions, and are NOT in conflict:**
  * r1yj APPLIES the isospin assignment -> 3/2 (assigned value)
  * this branch makes NO assignment -> 5 in-block, 9 across (ceiling over ALL)

3/2 <= 5 <= 9, and the ceiling BOUNDS what any re-assignment of r1yj's channels
could reach: its 22.47x miss cannot be repaired by choosing channels
differently, best conceivable 33.7/9 = 3.7x. Strengthens its negative.

**What this branch adds:** r1yj scans the four LIVE blocks; this scans all 11,
and the extra seven are where the k=0 (unbounded-ratio) eigenvalues live —
absent from the visible four, consistent with r1yj seeing no unit modulus.

qou-m896's n=2 cap of 1 stands at the two-strand interface. All three quote
together.

## Lean: the mechanism, in the canonical carrier (verification pending)

Corpus-grep found `QOU/SchurWeyl/OcneanuWeight.lean` ALREADY carries
`ocneanuWeight q z mu` with exactly the formula used, plus a content-(-2)
numerator vanishing lemma and the convention-D row cap. So the degree argument
belongs IN that file, not a new one. Four declarations appended:

  ocneanuNumFactor_affine          — z-coefficient is q^(2j+1) - q^(2i+1)
  ocneanuNumFactor_diagonal_z_free — at i=j the z terms cancel IDENTICALLY,
                                     no hypothesis on q at all
  ocneanuNum_diagonal_split        — the z-dependence is confined to the
                                     off-diagonal cells (Finset product split)
  mem_cells_diag_zero              — every non-empty diagram has (0,0), so
                                     d >= 1 and z^|mu| always dies

Proves the MECHANISM, not the degree count: turning it into deg_z <= |mu| -
d(mu) needs the polynomial-degree argument over the product and is NOT done.
rank = n stays measured (n=2..7), so the exclusion stays scope-(a).

NOT COMMITTED until lean-direct verification returns.

## 2026-09-03 — the Lean is VERIFIED sorry-free (lean-direct, real import cone)

Four declarations in `QOU/SchurWeyl/OcneanuWeight.lean` (commit 2cb1d14a5e,
rebased) now verified. The dispatched lean-verifier subagent never returned —
the session restarted — so this was run directly.

COMMAND (root mathlib had traces ~= oleans, i.e. genuinely built, so lean-direct
was safe; `lake build` NOT run, per the restored-cache trap):

    LP="$PWD/folio/quantum-observable-universe/lean/.lake/build/lib/lean"
    for p in mathlib batteries aesop Qq proofwidgets importGraph plausible \
             LeanSearchClient; do
      LP="$LP:$PWD/.lake/packages/$p/.lake/build/lib/lean"
    done
    LEAN_PATH="$LP" lean \
      folio/quantum-observable-universe/lean/QOU/SchurWeyl/OcneanuWeight.lean

exit 0, no diagnostics. Note exit 0 ALONE is not the gate — lean exits 0 on a
`sorry` (it is a warning), so #print axioms is what settles it:

    ocneanuNumFactor_affine          [propext, Quot.sound]
    ocneanuNumFactor_diagonal_z_free [propext, Quot.sound]
    ocneanuNum_diagonal_split        [propext, Classical.choice, Quot.sound]
    mem_cells_diag_zero              [propext, Classical.choice, Quot.sound]

No sorryAx. Only the three standard Mathlib axioms; the two `ring` proofs do
not even need Classical.choice. The only 'sorry' string in the file is a
docstring quoting 'sorry-free'.

Re-verified after rebasing onto main (38 commits, clean): lean-direct exit 0
again, and all three probes exit 0 again. A clean rebase is not evidence the
code still works, so both were re-run rather than assumed.

SCOPE UNCHANGED by this verification: the Lean proves the MECHANISM (z-dependence
confined to off-diagonal cells; diagonal factors z-free unconditionally), NOT
the degree count deg_z <= |mu| - d(mu), and NOT rank = n. Those stay measured
(exact symbolic n=2..6, numeric to n=7), so the exclusion stays scope-(a).

## 2026-09-03 — the rank bound is PROVED (the <= half); scope still (a)

Commits 8a8457991f (degree bound) and 18cbcd439b (rank bound), both lean-direct
verified, **11 declarations, zero sorryAx**.

CHAIN, now end-to-end in Lean:

  1. each cell's numerator factor is affine in z, coefficient q^(2j+1)-q^(2i+1)
  2. that coefficient is ZERO on the diagonal i=j — identically, no hypothesis
     on q at all (the two z terms cancel term-for-term)
  3. hence deg_z(numerator) <= #off-diagonal cells = |mu| - d(mu), d = Durfee
     (via natDegree_prod_le: product degree <= sum of factor degrees, diagonal
     factors constant, off-diagonal linear)
  4. every non-empty diagram has (0,0), so d >= 1 and deg <= |mu| - 1
  5. a degree-<=d family evaluated at z lies in the span of its d+1 coefficient
     vectors — for EVERY z, not just sampled ones
  6. therefore the Ocneanu family at level n spans **at most n dimensions**,
     against p(n) for the full space of trace functionals

Step 6 is `ocneanuFamily_finrank_le`. Steps 5-6 are stated for an arbitrary
finite family of polynomials — nothing about the Ocneanu weight is used, which
is what makes the argument checkable rather than entangled with the formula.

**This is the <= half only.** rank = n EXACTLY is still measured (exact
symbolic over Q(q) at n=2..6, numeric to n=7), and so is
deg_z = |mu| - d(mu) exactly. A proved upper bound on the rank is not a proof
that the rank is attained, so the exclusion of the Markov-trace family stays
**scope-(a)**. What changed: the bound direction no longer rests on
measurement — it rests on the degree of a polynomial.

AXIOM REPORT CHANGED, honestly noted: the two `ring` proofs previously showed
[propext, Quot.sound] and now show Classical.choice too. Nothing in those
proofs changed — the added LinearAlgebra imports changed instance resolution
file-wide. Earlier text claiming they 'do not even need Classical.choice' was
corrected in the same pass rather than left standing.

MATHLIB TRAPS for the next agent (all cost me a cycle):
  * Mathlib.LinearAlgebra.Finrank does NOT exist in this version;
    Dimension/Finrank and Dimension/Constructions do.
  * Submodule.finrank_mono and finrank_span_le_card are in
    Dimension/Constructions — importing Dimension/Finrank alone is not enough.
  * finrank_span_le_card needs a Fintype on the range, NOT automatic; wants
    (Set.finite_range _).fintype plus Module.Finite.span_of_finite.
  * natDegree_C_mul_X_le does not exist; build from natDegree_mul_le.
  * Finset.sum_le_sum cannot infer its bounding function — name it
    (g := fun _ => 1).
  * `simp` distributes C across a product (C (a*b) -> C a * C b) rather than
    discharging a natDegree goal; the diagonal case wants explicit rewrites.

## SIGN ATTACKED 2026-09-03 — positive at A=3, NEGATIVE at A=4

`computations/probes/manybody_sign_by_bond_topology_probe.py`, 5/5, mpmath.
Many-body term defined at FIXED NUCLEON CONTENT (`L(bond set) - sum of
single-bond L` on the same braid), NOT by subset-Mobius. That difference is why
the A=3 sign differs from t7qv's.

    A=3 exhaustive   two-bond sets   EXACTLY ZERO (1.3e-51), band-routed included
                     the triangle    POSITIVE in ALL SIX orders, 0.0746 to 0.1810
    A=4              chain           EXACTLY ZERO (5.3e-51)
                     complete graph  NEGATIVE in all 3 orders, -1.073/-0.561/-0.531

**A positive many-body term DOES exist — at A=3. It flips NEGATIVE at A=4**,
which is exactly where the alpha lives. So the sign attack fails at the mass
number that needs it.

Magnitude: best A=4 order gives `B = 10.083 MeV` against AME `28.296`, **2.81x
short** (consistent with t7qv's independently computed 10.387277). The additive
route capped at 20.649 MeV with per-bond values free. **Both routes closed.**

### Confirmed t7qv's no-distance-decay result, 37 orders tighter

All six A=4 nucleon pairs give `L = 0.48989938425513485141`, max deviation
**1.47e-50**, against their float64 `3.4e-13`. Independent implementation.

### A correction I nearly published

A first run used `HF = h/2` and produced an apparent LINEAR decay with
separation (0.4899, 0.3018, 0.1136) with an exactly constant decrement
0.188144 -- which I was one step from reporting as contradicting t7qv. **My
error**: their `HF = float(_H)` is `h`, confirmed by their own `bond_d` (an nn
bond takes `-HF` and `d_for_ctype("sigma_inv", h) = -h`). A pattern clean to six
digits is not evidence the constant feeding it is right.

## WHAT ELSE COULD CARRY EXTENSIVE BINDING — the corpus already answers

`docs/audits/2026-08-02-alpha-cluster-su4-extensive-term.md`: the missing term
is **linear in A**, per-nucleon `B/A -> ~8 MeV` (0-fit A-scaling, CV 0.148) --
NOT `C(A,2)` or `C(A,3)`. Structure derived (SU(4) `[1^4]` alpha-cluster volume
term); **scale still open**. And a surface term now exists:
`QOU.Mass.SaturationPeakStructure` (landed 2026-08-30).

Quantified against my measured slopes:

    log-ratio per-nucleon   pp 2.0507   pn 2.8338   nn 3.7978  MeV/nucleon
    alpha-cluster target                ~8 MeV/nucleon
    supplies                25.6 % to 47.5 %   -- short by 2.11x to 3.90x

**My exclusions SHARPEN the alpha-cluster route rather than block it.** The
`[1^4]` singlet is a 4-body SU(4) object, not a bond-graph object, so the
bond-topology exclusions (additive: capped; non-additive: negative at A=4) do
not apply to it. What they do is remove the bond graph as a competitor, leaving
the alpha-cluster term as the carrier that has to supply the missing ~3/4.
### The selection principle EXISTS and is broken three ways — extending L_K_max is futile (2026-08-31)

I proposed extending the enumeration to `L ≥ 8` as the live next step. **Do not
run it.** The residual criterion is already there, and read off the enumerator's
**own recorded output** it has three independent fatal defects.

**First, correcting my own correction.** I said "the principle is not
minimality". Right about the *code* (sort key is `(PSD, residual, length)`),
**wrong about the corpus**: the Lean instances' `bindingKWord = [3,3]` came from
the witness's `min_length_psd_feasible_candidates`, **not** the residual-ranked
`psd_feasible_top_k`. The recorded carrier *is* the min-length pick.

**Defect 1 — the residual's rank-1 pick is a SELF-CROSSING.** With
`offsets = [0,3,6]` in `B₉`, `σ_i` is inter-component iff `3 | i`, so only `σ₃`
and `σ₆` qualify. **`inter_nucleon_generators_extended` has 8 of 12 entries
intra-nucleon** and its name says otherwise. Rank-1 for **both** ³H and ³He is
`[-8,-8] = σ₈⁻²`, inside nucleon 3 — zero inter-component crossings, so
`countChannel = 0` and it binds nothing. Rank-2 `[-5,-5]` likewise. The first
genuine interface appears at rank 3.

**Defect 2 — the rank-1/rank-2 order is float64 noise.** `σ₅` and `σ₈` are the
same generator of two different blocks, so block symmetry makes their residuals
**equal**. Recorded gap: **exactly 2 ULP** (`2.220e-16` at `0.93`, where eps is
`1.110e-16`), in both nuclei. The top slot is decided by rounding. Same 2-ULP
split for `[-4,-4]`/`[-7,-7]` and `[7,7]`/`[4,4]`.

**Defect 3 — the two genuine interfaces are exactly degenerate.** `[-3,-3]` and
`[-6,-6]` record the *identical* residual to every digit. The criterion cannot
tell the `1|2` interface from `2|3`. That is a symmetry, not a bug — any
trace-only criterion will tie them — so breaking it needs information the trace
does not carry.

**Also: the minimal set cannot carry a Brunnian link at any length.** `σ₃` and
`σ₆` are distant hence commute, so `⟨σ₃,σ₆⟩` is free abelian; every word reduces
to `σ₃^a σ₆^b` with linking numbers `a/2, b/2, 0`, and Brunnian forces
`a = b = 0`. The corpus's own Borromean `(σ₁σ₂⁻¹)³` needs **adjacent**
generators, so it was never reachable there.

**Revised next step.** Repair the criterion before searching wider: restrict to
`3 | i`, carry the residual in `mpf` not `float64`, and find a tie-breaker for
the exact `1|2`/`2|3` symmetry. Lean
`QOU/Mass/EnumeratorSelectionDegeneracy.lean` (8 decls, sorry-free); probe
`enumerator_selection_criterion_audit.py` (7/7, nothing re-run).


**Follow-up measurement — the minimal-set search is both redundant and
unnecessary.** Because `σ₃` and `σ₆` commute, at `L ≤ 8` the enumerator would
walk **87,380 words for 145 distinct group elements — 99.83 % redundant.** And
the answer needs no search at all: Brunnian forces `a = b = 0`. `lk(1,3) = 0` is
forced by *reachability* — `σ₃` transposes positions 3,4 and `σ₆` positions 6,7,
so a block-1 strand and a block-3 strand never meet — hence the Borromean, which
needs all three pairs linked, is **unreachable in this layout**.

That is the real open question now: **what braid presentation of three nucleons
admits a Brunnian carrier at all?** It is a design question about the
construction, not a search.


### The fix is the GENERATOR SET, and it is a known one — band generators (2026-08-31)

Not the strand layout: `n = 3A` is forced corpus-wide by the three-quark
structure, and re-labelling which strands belong to which nucleon is a
conjugation, which the Markov trace cannot see.

The braid group's **band (Birman–Ko–Lee) generators**
`a_{t,s} = (σ_{t-1}⋯σ_{s+1}) σ_s (σ_{s+1}⁻¹⋯σ_{t-1}⁻¹)` link strands `s` and `t`
**directly**, and satisfy `a_{s+1,s} = σ_s` — so the adjacent transpositions the
enumerator used are a **proper subset** of the bands. Counted in `B₉`:

| | count |
|---|---|
| inter-nucleon band generators | **27** |
| searched by the enumerator | **2** (`σ₃`, `σ₆`) |
| bands reaching the `1|3` pair | **9** |
| of those, searched | **0** |

Every `1|3` band has `|t−s| ≥ 4`, so none is an adjacent transposition and none
could have been in the search set. **The subset chosen excludes precisely the
pair a Brunnian carrier needs** — which is why the Borromean was unreachable.

**Corpus-grepped, absent:** no band / Birman–Ko–Lee generator anywhere in
`content/`, `computations/` or `docs/`. The single `BKL` hit is **BKLR**
(Bischoff–Kawahigashi–Longo–Rehren), a Frobenius-algebra theory — a substring
false positive. **Four library documents** cover the band presentation, so
adopting it is a **citation, not a derivation**.

**This is the concrete next step**, and it is a rewrite of the search set rather
than a longer search: re-run the binding-K enumeration over the 27 inter-nucleon
bands (in `mpf`, not float64), which is a *smaller* space than the 87,380 words
the length-extension would have walked.


### 🛑 RETRACTED: "the band route is cheaper". It is ~4,400× LARGER (2026-08-31)

I asserted, in the bean and in #6366, that re-running the enumeration over the
27 inter-nucleon bands would be *cheaper* than the length-extension it replaces.
**I did not compute it. It is wrong.**

A Brunnian carrier needs `n₊ = n₋ ≥ 1` on **each** of the 3 nucleon-pairs, so at
least **6** band letters:

| | candidates |
|---|---|
| naive, 54 signed band letters, `L = 6` | 24,794,911,296 |
| structured (one `+`/`−` per pair, ordered) | **382,637,520** |
| the length-extension it replaces | 87,380 |
| | **4,379× larger** |

The band set is still the **only** one that can *reach* a Brunnian carrier — it
is **necessary, not cheap**. Do not quote "cheaper".

### And the correction produces the better result: the binding cannot see WHICH band

`countChannel np nn q` depends only on `n₊ + n₋`
(`countChannel_depends_only_on_total`, proved), and `SelfMutualPartition` makes
binding a sum over inter-component crossings. **So all 9 bands joining a given
nucleon-pair are binding-equivalent.** The binding-relevant content of a carrier
is the triple `(m₁, m₂, m₃)` — **20 triples** at `c ≤ 12` against 382,637,520
band words, a collapse of **1.9 × 10⁷**.

**This subsumes Defect 3 rather than sitting beside it.** The residual is being
asked to make a distinction *the binding does not use*; the exact `1|2`-vs-`2|3`
tie is the two-generator shadow of the same fact. **So no repair of the
arithmetic — `mpf` instead of float64 — can make a trace criterion select among
binding-equivalent carriers.** The float64 fix is still right, but it fixes a
smaller thing than I said.

**Confirmed at the source, not just in the recorded output:**
`_eval_word_per_block_cached` builds `np.eye(dim)` and multiplies float64
matrices, so defect 2's root cause is in the producer.

**Revised next step.** Search the **20 binding-relevant triples**, not band
words — and select on something that is not the Markov trace, since the trace
provably cannot separate binding-equivalent carriers.


### The A=3 count-channel carrier route is EXHAUSTED — there was nothing to search (2026-08-31)

The authorised next step was *"search the 20 binding-relevant triples and select
on something that is not the Markov trace."* **There is nothing to search.** The
space collapses once more, to a single integer, and enumerating it is a proof.

**Second collapse.** With `c₂ = 2` (owner-ruled Hopf pair) and `c₃ = 2(m₁+m₂+m₃)`,
`bRatio_hopf_pair` gives `b₃/b₂ = M − 3` with `M := m₁+m₂+m₃`. **`b₃` cannot see
the triple either — only its sum.** So 20 triples → 4 values of `M`.

| `M` | `c₃` | `b₃/b₂` | vs measured | triples |
|---|---|---|---|---|
| 3 | 6 | `0` | −100 % | 1 — forced `(1,1,1)`, the Borromean |
| 4 | 8 | `1` | **+55.98 %** | 3 |
| 5 | 10 | `2` | +211.95 % | 6 |
| 6 | 12 | `3` | +367.93 % | 10 |

`M ≥ 3`, so `b₃/b₂` is a **non-negative integer** while measured is
`950815/1483044 ≈ 0.6411`, strictly between 0 and 1. Nothing hits it; every `M`
misses by `≥ 532229/1483044 ≈ 0.35888` = **55.98 %**, attained at `M = 4`.

**`c ≤ 12` was never a restriction.** `b₃/b₂ = M − 3` *increases* with `M`, so
nothing above `M = 4` does better. **The exclusion is complete over every
crossing number** — there is no larger search that could exist.

**Scope (b)** on the conjunction {`b₃` carried by the count channel, `μ ∝ c`,
Hopf pair carrier, Brunnian A=3 carrier}, invariant named: `M` is an integer.
**(a)** on each ingredient; `brunnian_binding_survives` untouched.

**The live ingredient is the FIRST one** — that `b₃` is carried by the count
channel at all. Owner ruling A fixes the pair carrier; dropping Brunnian-ness
hits `brunnian_not_pairLocal`; `bRatio_scale_invariant` shows `μ ∝ c` is not a
relaxable convention. So this returns `qou-brng` to its original framing: **the
extensive term is somewhere the crossing count does not reach.**

Lean `QOU/Mass/BrunnianTripleExhaustion.lean` (8 decls, sorry-free, imports
`rMeasured` from `CarrierCrossingQuantisation` rather than restating it, so the
two cannot drift); probe 6/6.


### Which ingredient is actually free — RESOLVED, not guessed (2026-08-31)

I wrote that the free ingredient is *"that `b₃` is carried by the count channel at
all"*. Resolving it to its source names it exactly, and it is sharper than that.

`SelfMutualPartition.binding_eq_neg_mutualEnergy` is **a definitional partition**,
not an empirical claim: it takes `energy : C → ℝ` as a **parameter** and proves
`binding = −mutualEnergy` by `unfold` + `ring`. Nothing there pins what `energy`
is.

The pinning is in **`def:crossing-energy`**, which *defines*
`𝔈_cross = Σ_crossings (q for L₊, −q⁻¹ for L₋)` — **one weight per crossing, the
same whichever components it joins.** That uniformity **is** `μ ∝ c`: summing a
constant over crossings is counting them. A pair-dependent weight would make `μ`
a weighted sum, and the integrality driving the whole exclusion would vanish.

**So the same defect sits at two levels, and the corpus already refuted the upper
one.** `CrossingModelPairLocality` proved assembly-independent *pair* weights
force `b₃ = 0`; one level down, crossing-independent *crossing* weights force
`b₃/b₂ ∈ ℤ`. **The measured `b₃` refutes uniformity twice**, and the second
refutation is what this arc supplies.

**TRAP recorded — `ℝ` auto-binds silently.** `BrunnianTripleExhaustion` must
`import Mathlib.Data.Real.Basic` explicitly; `CarrierCrossingQuantisation` does
not, and without it Lean **auto-binds `ℝ` as a fresh type variable rather than
erroring**, so the weight lemmas type-check over a meaningless type. Caught only
because a `ring` failed downstream and the goal display showed `ℝ : Type u_1`.

File now 12 declarations, sorry-free.


### CAPSTONE — every evaluable channel gives `b₃` the wrong sign, the shipped one included (2026-09-02)

Each earlier exclusion in this arc carried the same caveat: production ships
something else, so none of it bound production. **This removes the caveat.**

| channel | `b₃/b₂` | vs measured |
|---|---|---|
| **ch1 observe-early — SHIPPED** | **−1.3995** | −318.3 % |
| ch3 log-ratio | −0.9679 | −251.0 % |
| ch4 bar-norm log | −0.9681 | −251.0 % |
| ch5 pairwise sum | −1.0205 | −259.2 % |
| **measured** | **+0.6411239316** | |

**And the two structural families fail SEPARATELY.** ch3/ch4/ch5 cluster near
`−1` because on the chain they sum one term per bond and A=3 has twice A=2's bond
count — the ratio-of-2 `TypeWeightedChainRatio` proves pins `b₃/b₂` to `−1`. ch1
sits at `−1.3995` precisely because it is **not** additive (its `|tr_p|^Z|tr_n|^N`
prefactor is exponential in A). So the joint negative cannot be blamed on one
shared modelling choice.

**The failure is a SIGN.** No magnitude, normalisation, anchor or convention
reaches it. Independently corroborated by the `t7qv` arc, which measured the
many-body term directly: negative in all eight A=3 flavour orderings, α-free
ceiling short by `2.0975×`.

**Scope (b)** on the four **evaluable** channels, invariant named: the sign of
`b₃`. **(a)** on ch2/ch6/ch7, which the taxonomy classifies from source and
neither it nor I re-evaluated — calling the arc closed over all seven would
overstate it.

**Precision, stated:** B/A comes from the taxonomy producer at ~8 significant
figures, re-run in this container and reproducing the audit byte-for-byte. Ample
for a sign test at 251–318 % margins; not a precision claim, and none is made.

Probe 5/5, exact `Fraction` over the producer's decimal strings.


## 2026-09-03 — the three additive channels' `b₃ ≈ −1` is the INVERSION, and no uniform bond model can be positive

**Reframes my own capstone.** `all_channels_b3_sign_probe` measured `b₃/b₂ < 0`
for all four evaluable channels and read the three bond-additive ones clustering
at `≈ −1` as a shared *physical* failure. For those three it is arithmetic.

**The mismatch.** The Ursell inversion `b₃ = B̄(3) − 3b₂` subtracts `C(3,2) = 3`
pair terms; the bond set is a chain with `A−1` bonds, forced by
`StrandLayoutForcesChain`. The counts agree at `A = 2` (1 = 1) and diverge from
`A = 3` (3 vs 2) — exactly where `b₃` lives. For chain-additive `B(A) = (A−1)b`:
`b₂ = b`, `b₃ = 2b − 3b = −b`, so **`b₃/b₂ = −1` identically, for every `b`**.
Measured over five bond values spanning sign and eight orders of magnitude:
exactly `−1` in all five.

**The generalisation — the part worth having.** Changing the bond set does not
help. For binding additive over a bond set with a **uniform** bond value the
value cancels and only the counts survive: `b₃/b₂ = n(3)/n(2) − 3`. Two bound
nucleons have exactly one bond, and a simple bond set on three has at most
`C(3,2) = 3`, so

| `n(3)` | 0 | 1 | 2 (chain) | 3 (all-pairs, MAX) |
|---|---|---|---|---|
| `b₃/b₂` | −3 | −2 | **−1** | **0** |

`b₃/b₂ = n(3) − 3 ≤ 0` for **every** uniform pairwise-bond model, against a
measured `+0.6411239316`. **The chain is not the culprit; the uniformity is.**

**The surviving escape, measured not asserted.** All-pairs with an `A=3` bond `w`
against a deuteron bond `w_d` gives `3w/w_d − 3`, which hits the measured value
exactly at `w/w_d = 5399947/4449132 = 1.2137079772` (> 1). **Non-uniformity is
NOT excluded** and is the next direction on this leg.

**What is NOT affected.** `ch1 = −1.3995`, the **shipped** channel, is not
bond-additive (trace prefactor exponential in `A`) and fails for its own reasons.
Distance-from-`−1` measured per channel to separate them rather than assume it:
ch3 0.0321, ch4 0.0319, ch5 0.0205 — ch1 **0.3995**, 12× further. The AME
`b₃/b₂` is data; no inversion convention alters it.

**Scope (b)** on uniform pairwise-bond-additive models, invariant named: `n(3)`
capped at 3 while the inversion subtracts 3. **Scope (a)** on everything else.

**Artifacts.** `QOU/Mass/UrsellChainMismatch.lean` — 12 decls, `lean`-direct
exit 0, sorry-free, axioms only `[propext, Classical.choice, Quot.sound]` (three
theorems need none). `computations/probes/ursell_chain_mismatch_probe.py` — 9/9,
exact `Fraction`, P30-stamped, zero raw float64. PR #6366.

## Sub-q #2 assessed 2026-09-03 (session): NOT one-session closable — needs ribbon-cat infra; finset re-encoding would LAUNDER

Audit: docs/audits/2026-09-03-brng-subq2-bare-integer-vs-qdim.md.

Surveyed this frontier to pick a non-duplicative angle; sub-q #2 (mutual=bare count vs self=q-dim lw) is the only clean non-gated positive target, but it is a ribbon-category statement:
- self = tr_q(id_X) = Σ_λ n_λ qdim(V_λ) = lw (closed trace, sums over the object's simple summands);
- mutual = pairing of two FIXED simples = single S-matrix entry S_ab / bare crossing count (NO internal decomposition, because a,b are fixed simples not a co-traced composite).
The Σ_λ appears in one and not the other for a structural (ribbon/braided) reason. Mathlib has NO ribbon/fusion categories, quantum dimension, or S-matrix — same infra gap that blocks the R2 lift (qou-301d).

TWO SHORTCUTS BOTH FORBIDDEN:
- (A magnitude) b_αα do-not-attempt (qou-ebs6); ℏ_q² saturation numerology-suspect — do not force.
- (B structural) DO NOT extend SelfMutualPartition with a channel index set and 'prove' mutualCount has no Λ-sum — defining it without Λ then observing no Λ ASSUMES the answer (define≠derive laundering).

BindingMassRung does NOT close it: it treats M, lw as free params and only forces q-REGULARITY (order ℏ_q²), not bare-INTEGER-ness. Its own docstring says it does not derive why binding lacks the cusp factor.

RECOMMENDATION: leave sub-q #2 open+unfabricated; the tractable adjacent formalization is the shared quantum-trace/connected-sum-multiplicativity infra (qou-301d), which would foundation BOTH sub-q #2 and R2. Default no-op is safe (nothing moves). Higher-leverage item this frontier sits under: the two-nucleon SIGN defect (binds diproton/dineutron; qou-vbyi route 1) — signs before digits.

## 🛑 2026-09-03 — RETRACTION: the uniform-bond exclusion above DUPLICATES `qou-edt7`

**The mathematics of the entry above is correct; the claim that it was new is
not, and it was mine.**

`QOU.Mass.UniformBondSimpleGraphExclusion` landed on `main` `c9d47234ce` on
**2026-08-30**, four days before #6366 merged, under bean **`qou-edt7`**. It
proves the same exclusion and proves it **more generally**:

| here | `qou-edt7` |
|---|---|
| `bondAdditive_nonpositive` — `n(3) − 3 ≤ 0` at `n(2) = 1`, needing `b₂ ≠ 0` | `b3Uniform_nonpos` — `ε(e₃ − 3e₂) ≤ 0` for `e₃ ≤ 3`, `e₂ ≥ 1`, `ε ≥ 0` |
| `bRatioOfBondCounts_chain` | `b3Uniform_neg_of_chain` |
| `bRatioOfBondCounts_allPairs` | `b3Uniform_eq_zero_of_complete` |
| `no_uniform_bond_model_reproduces_b3` | `not_uniform_simple_of_b3_pos` |

Same invariant: a simple graph on three vertices has at most `C(3,2) = 3` edges
while the Ursell inversion subtracts three.

**The "surviving escape" was not a new direction either.** `w/w_d =
5399947/4449132 = 1.2137079772` **is** the corpus's `w(2)/w(1)`, recorded to 60
digits in `coordination-weight-rise-and-turnover.witness.json` as
`1.21370760735284029758…`, whose own source line calls it *"the entire content of
`b₃ > 0`"*. They agree to `3.05e-7`. And the obvious mechanism on that axis —
single-ratio (Markov-power) scaling `ε(z) = ε(1)·r^{z−1}` — is **already
REFUTED** there (~44 % disagreement between the two available ratios, for every
`r`, convention-independently).

**Trap, recorded because it is the whole point of the checklist.** I ran the
six-path corpus-grep *after* merging instead of before. Path 3 surfaces
`coordination_weight_rise_and_turnover_probe.py` on the **first pattern tried**,
and its docstring names `UniformBondSimpleGraphExclusion` in the third paragraph.
The grep is cheap; I ran it at the wrong point in the sequence. **A "next
direction" line in a bean or PR body is a novelty claim and needs the checklist
exactly as much as an "open" declaration does.**

**What survives as this arc's own:** the link between the exclusion and the four
**measured** channel values — ch3/ch4/ch5 within 0.032 of `−1` because they are
one identity, ch1 at 0.3995 because it is not bond-additive. That reframes my own
capstone and is not in `qou-edt7`.

CEILING: the corrected binding path reaches A=4 in this container, not A=6.

TWO ROUTES TO SETTLE IT, neither attempted:
  1. A=6 on a machine that holds the process. Nothing about the computation is
     known to be wrong; it is scheduling.
  2. A=4 and A=6 both at reduced k_exact -- not comparable to the k=11 points,
     but comparable to EACH OTHER, so E(6)/E(4) discriminates cheaply. A
     different measurement needing its own gate.

## 2026-09-03 — RETRACTION of the `E ≈ 5.4 × C(A,2)` target above, and what replaced it

**The target in the previous entry is WITHDRAWN. Do not carry it forward.** It
is mostly an artefact of the arithmetic, not a finding about the framework.

The mechanism: `E := AME − B_pred`, and the entry immediately above establishes
that `B_pred ≈ −7.3 MeV` is **near-constant** across nuclei. So
`E ≈ AME + 7.3`, and `E/C(A,2) ≈ (AME + 7.3)/C(A,2)` — a statement about
**AME2020 plus an offset**, with almost no framework content in it. Measured:

    nucleus   A    AME     E/C(A,2)   (AME+7.3)/C(A,2)
    ²H        2    2.225     9.496          9.525
    ³H        3    8.482     5.408          5.261
    ³He       3    7.718     5.058          5.006
    ⁴He       4   28.296     5.854          5.933

The last two columns agree to **~1 %**. And `AME/C(A,2)` is not constant — it
is 2.225, 2.827, **4.716**, 2.133, 1.869, 1.396 for ²H/³H/⁴He/⁶Li/⁷Li/¹²C: it
**peaks at ⁴He and falls steeply**. The near-constancy was a three-point
coincidence in the region where the AME curve happens to turn over; ⁶Li breaks
it on AME grounds alone (≈2.62 with the offset), before the framework is
consulted.

The `E/C(A,2)` figure therefore does **not** bear on the pairwise-cap tension
flagged in the previous entry — that tension is withdrawn along with the
figure, not resolved.

### What the retraction bought: a better experiment

The informative measurement is **`B_pred` itself as a function of `A`**, with
no experimental normalisation anywhere in it — so nothing about AME can
contaminate it. Run as a **paired** comparison of ⁴He and ⁶Li at *matched*
truncation `k_exact`, which also sidesteps the A=6 wall (three full
`binding_energy` attempts at ⁶Li were killed at ~900 s / 326 s / 124 s):

    k_exact   ⁴He (A=4)      ⁶Li (A=6)      ratio li6/he4
      5      -0.375110164   -0.539212954       1.4375
      6      -0.838749076   -0.992757495       1.1836
      7      -1.515118319   -1.414063111       0.9333
      8      -2.153722974   -2.183158129       1.0137
      9      -3.711581534   -3.404340982       0.9172
     10      -5.669659692   -5.467686217       0.9644

`A` grows 1.5×; `C(A,2)` grows 2.5×; the accumulator ratio sits in
**0.917 … 1.014 for k ≥ 7** (mean 0.957). **The flatness extends to A = 6** —
`B_pred` carries essentially no `A`-dependence over a range where binding grows
by 3.5×. That is the finding the withdrawn target was obscuring, and it is the
direct measurement this bean's missing extensive term needs.

Scope: this is a scope-(a) statement about the current `unified_iterative_correction`
path at truncations k = 5…10 — not a structural exclusion of any ingredient.
Audit: `docs/audits/2026-09-02-binding-energy-first-corrected-value.md`; PR #6427.


### k = 11 (production truncation) — both legs, added 2026-09-03

The ladder above was extended to the production truncation. Both legs completed:

    he4   A=4  k=11   uic = -8.201558468      1104 s
    li6   A=6  k=11   uic = -7.794544740      1269 s
                            ratio li6/he4 = 0.9504

So the k >= 7 ratios are 0.933, 1.014, 0.917, 0.964, **0.950** — mean **0.956**,
spread ±5 %, no trend in k, while `A` grows 1.5x and `C(A,2)` grows 2.5x.
**k = 11 was the one rung that is not a reduced-cost proxy, and it behaves like
the rest.** The flatness is not a truncation artefact.

(The 6Li leg took two attempts: the first died to a worker-process restart at
~1919 s, an environment event, NOT the A=6 compute ceiling the three earlier
full-`binding_energy` kills established. The driver is resumable, so only that
one cell was recomputed.)

**A separate defect surfaced by the same run, worth its own attention:** 4He's
|uic| runs 1.52 -> 2.15 -> 3.71 -> 5.67 -> 8.20 across k = 7..11 with the
increments still GROWING (0.64, 1.56, 1.96, 2.53). **The accumulator is not
converged at the production truncation.** The absolute B_pred values in the
four-nucleus table are therefore truncation-limited; the matched-k ratio is not,
which is why the flatness claim rests on the ratio and not on the values.


### LOCALISED 2026-09-03 — the A-dependence dies in the y_λ-weighted SUM

`computations/probes/where_the_a_dependence_is_lost_probe.py`, 6/6. Three layers
instrumented separately.

**L1 chain — A-dependence is fed in, correctly.** `_step_chain_generic` appends
one inter-nucleon crossing per previous nucleon: he4 50 crossings / 6 inter,
li6 81 / 15 — exactly `C(4,2)` and `C(6,2)`. The coordination count IS present
in the input.

**L2 per-partition trace — it SURVIVES.** Same partition, both nuclei, final
`ln|tr|` at 50 dps: partition (3,1) gives -1.29903 vs +0.09426 (differ in SIGN);
(5,1) gives +0.58294 vs +0.13563.

**L3 the weighted sum — it is GONE, and Pass 2's gate is NOT the cause.** The
natural hypothesis (the complementary-slackness gate selects a
nucleus-independent subset) is refuted:

    k   he4 raw     li6 raw     RAW ratio   he4 gated   li6 gated  GATED   tight
    5   -0.736660   -0.923253     1.2533    -0.375110   -0.539213  1.4375  5->10
    7   -2.471104   -2.855260     1.1555    -1.515118   -1.414063  0.9333 18->22
    9   -6.691821   -7.266773     1.0859    -3.711582   -3.404341  0.9172 42->48

The RAW pre-gate sum is ALREADY flat, and gets flatter with k (1.253 -> 1.156 ->
1.086) while C(A,2) grows 2.5x. The gate is A-aware (tight 5->10, 18->22,
42->48) and roughly neutral on the ratio.

**So the cancellation is in the y_λ-weighted telescoped sum over partitions** —
downstream of the trace, upstream of Pass 2. A fix has to look there; the chain
builder, the `g % n_gens` generator wrapping, and the gate are all exonerated.

Scope-(a): localises the symptom at k = 5,7,9 in this one path. Does NOT
identify the cancellation mechanism and excludes no ingredient.

**Relation to the sibling sign work above (`manybody_sign_by_bond_topology_probe`):
complementary, not conflicting.** That probe builds its object from
`atom_canonical_crossings` bond topology; this path builds chains from
`_step_chain_generic`. Different constructions, checked — no shared call. Their
object IS A-dependent (positive A=3, negative A=4); this one is not. Do not read
either as confirming the other.


### 2026-09-03 — E₀-conditionality flagged by a sibling; it splits this arc's results in two

Sibling #6443 (merged `4b83e4cf53`) warned on #6427 that "N× short" figures in
the extensive lane are E₀-conditional — `derivation_chain.E_0_CONVENTIONS` spans
**5.35x** between conventions A and B. Checked at the source; the warning is live
for part of the arc and inert for the rest.

`binding_energy` = `unified_iterative_correction` (m_e scale) +
`sdp_cross_channel_contribution` + `binding_from_frobenius_pairing`, and term 3
is literally `E_0_CALIBRATION_MEV * (abs(free_tr) - abs(atom_tr))`.

**E₀-CONDITIONAL — do not quote as convention-free:** the four-nucleus `B_pred`
table, every `|pred|/AME` ratio, and the "target varies 12.7x, prediction varies
12.5 %" comparison. E₀ multiplies ONLY term 3, whose share differs per nucleus,
so even a spread-of-ratios is not invariant under a convention change.

**NOT affected:** the paired `k_exact` ladder (the 0.9504 flatness) — it measured
`unified_iterative_correction` ALONE, which carries `M_E_MEV` not E₀, and it is a
ratio at matched truncation so scale cancels a second time independently. Also
unaffected: the layer-1/2/3 localisation, all of which sits inside `uic`.

So the two load-bearing results survive and the headline table does not. Stated
plainly because the strongest-sounding table was the one carrying the unmarked
dependence.

**Still open:** the per-term decomposition. Existence of the E₀ exposure is
established FROM THE SOURCE; its magnitude is unmeasured (a run was launched and
had produced no output at time of writing).


### 2026-09-03 — the term-3 decomposition, all four nuclei

    atom  A    B_pred      term3    terms1+2      AME  | E_0x5.351  hbq^2x11.783 | flip
    2H    2  -7.271102   1.876634  -9.147736   2.2246  |   +0.8941      +12.9646  | x   4.87
    3H    3  -7.742121   0.221623  -7.963744   8.4818  |   -6.7778       -5.3524  | x  35.93
    3He   3  -7.456200   0.006659  -7.462858   7.7180  |   -7.4272       -7.3844  | x1120.8
    4He   4  -6.828594   1.372964  -8.201558  28.2957  |   -0.8548       +7.9761  | x   5.97

`flip` = the E_0 multiple at which B_pred crosses zero. Registered ceiling is
hbar_q^2*m_N at x11.783. **Two of four flip under some registered convention**,
and 4He is the alpha, not an owner-ruled special case. Scoping: E_0-conditional
at A=2 and A=4; robust at A=3, both isobars.

**TERM 2 IS ZERO.** terms1+2 at 4He = -8.201558468 matches the independently
measured uic(4He,k=11) to 1.5e-10 (the rounding limit of the recorded B_pred).
`sdp_cross_channel_contribution` contributes nothing at 4He; `binding_energy`
advertises three terms in its docstring and delivers two.

**THE 12.5% FLATNESS FIGURE IS PARTLY MANUFACTURED.** terms1+2 spread 20.56%
against B_pred's 12.47% -- term 3 is largest exactly where terms1+2 are most
negative (2H 1.877/-9.148, 4He 1.373/-8.202 vs 3He 0.0067/-7.463), so it
OFFSETS their variation and the flatter number is the total. **The accumulator
varies 20.6%, not 12.5%.**

The 0.9504 paired result is untouched, structurally: it measured uic ALONE at
matched truncation, term 3 not in it. uic varies 20.6% across 2H-4He and 5%
between 4He and 6Li -- both true, of different comparisons. Against AME's 12.7x
range, 20.6% is still flat in the sense the argument needs.

Term 3 spans **282x**, non-monotonic in A, unrelated to AME. Sharpest case: 3H
vs 3He differ **33-fold** in term 3 at identical mass number while their totals
differ 3.8% -- terms1+2 absorb nearly the whole swing. That is a far larger
within-A variation than the 6.7% noise floor quoted earlier in this arc, in the
one term characterised as the scale-exposed outlier rather than as scatter. No
explanation offered and none guessed.

Method note worth keeping: three successive readings of the sign question were
each overturned by the next nucleus. Four points did not support any of the
first three conclusions drawn from them.

Corrections pushed: retraction banners on `UrsellChainMismatch.lean` and the
probe, witness description/caveats rewritten to lead with the priority note, and
a new check 6 verifying my ratio against the recorded 60-digit value so the
duplication is an explicit corroboration rather than an implicit collision.
Nothing deleted.

## 2026-09-03 — the mu-bar route is RETIRED as stated: wrong mu-bar (type error)

`docs/audits/2026-09-03-two-mubars-selector-vs-magnitude.md`.

After the rank bound closed trace-subtraction, this arc named 'mu-bar_123, the
sorry-free triple-linking object' as the non-trace route. That names the WRONG
object, and SecondCrossingInvariant.lean says so in a section titled 'two mu-bars
in the corpus (do not conflate)'. Caught by reading the carriers before building
the probe.

  topological mu-bar_123   {0, +-1}          a SELECTOR (baryon vs meson)
  mubarMeasured A          (3/4)(-2)^(A-3)   a MAGNITUDE — the Markov-trace
                           = 3/4, -3/2, 3, -6  deficit coefficient (Lean examples)

The binding asymmetry is a real ratio (~33.7). A {0,+-1} invariant cannot supply
it — the same integer-type wall as the Delta_{3,3} ceiling of 9. The one with the
right type is DEFINED as a Markov-trace deficit, and
cyclic_trace_kills_iterCommTower (MassTheory) already proves a cyclic trace cannot
reach it.

CONVERGENCE: that theorem and this arc's rank bound (ocneanuFamily_finrank_le) are
two independent proofs, no shared machinery, that the Markov trace cannot deliver
the object. Neither was derived with the other in view.

RETIRED: 'mu-bar_123 carries the asymmetry'. SURVIVES (weaker, honest): mu-bar_123
as the coefficient SELECTING which magnitude applies, magnitude from elsewhere.
UNTOUCHED: rank-bound scope — still (a), still excludes only the Markov family.
No new compute; every value cited from a verified carrier.


## 2026-09-03 — B done, A closed (negative): rank = n PROVED; mu-bar_123 is channel-blind

**B — rank = n, both halves now in Lean** (`OcneanuWeight.lean`, 8944047236). The n
HOOKS (n-k,1^k) are linearly independent, via a triangular evaluation: hook k
vanishes at leg root z_m iff m <= k, and THE LEG ROOTS ARE THE OCNEANU FAMILY
z_i = q^i/[i]_q. The row cap and the rank are one phenomenon. Verified
symbolically at n=4,5,6 first (vanishing pattern, nonzero cyclotomic
determinant, z_i identity), then formalised: linearIndependent_of_triangular
(generic, strong induction), armFactor/legFactor/legRoot, two vanishing lemmas,
hooks_linearIndependent. All sorry-free, lean-direct. HONEST SCOPE: genericity
conditions on q (distinct leg roots, arm roots off leg roots, q^2 != 1) are
HYPOTHESES not proved; hookNum == ocneanuNumPoly(hook diagram) is NOT proved
(YoungDiagram.cells plumbing). So: 'n explicit hook numerators are
independent', conditional on genericity.

**A — closed, negative, no probe needed.** mu-bar_123 is typed on SINGLE
objects (B : S -> Q) and applied only to single hadrons (confined triple,
Borromean rings, 2-tube meson, baryon/vacuum). Both isospin channels are
two-baryon states; mu-bar_123 = +-1 on every baryon => +-1 on BOTH channels
=> CHANNEL-BLIND. Cannot select T=0 from T=1; the channels differ by the
EXCHANGE (Delta_3,3), not by what each nucleon is. The 'selector survives'
weak form is retired too. Honest residue: an exchange-sensitive invariant of
the six-strand two-nucleon link, which the corpus does not carry. A bounded
grep for mu-bar_123 + isospin timed out; not cited as evidence.


## 2026-09-03 — the linking-data class is closed: lk IS I₃, and both channels sit at I₃ = 0

Closes the residue this arc named the same day ("an invariant of the six-strand
two-nucleon link that is sensitive to the exchange"), **for the linking-data
class specifically**. Probe:
`computations/probes/two_nucleon_linking_matrix_channel_blind_probe.py` (exact
integer arithmetic, no witness, asserts are the gate).

**The composition.** Two facts the corpus already holds, neither applied to the
two-nucleon link by its own carrier:

- **(F1)** `inter_nucleon_linked_channel.py` derives the inter-nucleon arc as the
  minimal non-Brunnian 2-component link `T(2,2k)` — `pp → lk +1`, `nn → lk −1`,
  `pn → lk 0` — stating "NO numeric is tuned"; `u1_hypercharge_assignment.py:336`
  names the same datum *"I_3 = writhe/2-of-inter-nucleon-arc"*. Since
  `lk(T(2,2k)) = k = writhe/2`, **the inter-nucleon linking number IS I₃**.
- **(F2)** Milnor indeterminacy — already the scope-(b) exclusion of the Milnor
  route for ⁴He (`2026-08-29-gap2-he4-milnor-indeterminacy-exclusion.md`).

**Result (scope b).** The ³S₁ (T=0) and ¹S₀ (T=1) np channels have the same
flavour content, so `I₃ = 0` in both, so their linking matrices are **identical
on all 15 pairs** — verified under both the single-arc and all-nine-pairs
readings, so the verdict does not rest on that modelling choice. Every function
of the linking data is therefore equal on the two channels: achievable asymmetry
**exactly 1**, against **33.7055** required. Not a bound a better choice inside
the class might beat; the two inputs are one matrix.

**By-product.** The Milnor tower is DEAD across the interface at `I₃ = ±1`
(pp, nn: `ℤ/1 = 0`) and ALIVE only at `I₃ = 0` (np: `ℤ/0 = ℤ`) — where **both**
channels sit. Surviving is precisely what does not help.

**So do NOT propose a higher-`μ̄` or linking-integral route for the T=0/T=1
split** — including the Evans–Berger nth-order linking integrals the sweep found
in `library/1992evansberger/ocr/` (they are inside this closed class).

**NOT excluded:** an invariant reading the braid word beyond its linking data
(the `Δ₃,₃` spectrum is such an object, capped at 9 by the separate
integer-exponent argument); a non-Milnor super-pairwise object; anything
carrying **spin**, which is what actually separates the channels.

**Convergence, with its limit stated.** `qou-7zob` reaches the same wall from the
flavour side (*"NO map from strand position to orbital angular momentum anywhere
in the corpus"*), and `t7qv`'s `det T = −1` caps the ratio at 1. This supplies a
*reason* those ratios are 1 rather than merely small. It is corroboration, **not**
a fourth independent measurement — these routes share the (F1) assignment.

**Correction made in-flight:** the probe's first draft labelled the deuteron's eV
digits as keV and printed the shortfall as 33705x, a clean factor of 1000, which
the `> 1` assert passed. The assert now pins 33.7055 to four decimals.

Also: corpus-grepper memory updated (`MEMORY.md` trimmed 202 → 200 lines,
detail in `resolved-topics.md`), since its own entry ended by handing over the
gate that this closes.
## 2026-09-03 — a NON-bond-graph structural source for the extensive term exists in the trace (qou-kru4)
The bond-graph routes are closed from every direction above. Separately: the Markov trace is NOT bond-multiplicative at n=4 — the interleaved word s0 s1 s0 s2 s1 carries the exact cross term z(z^2-hz-1) = z * (conv-D Markov defect), negative (extra binding), confirmed two independent ways. This is a WORD-CLASS effect (bonds re-crossing after a neighbour bond), not a bond-graph count, so none of the bond-graph exclusions apply to it. It is a candidate source, not a closure: the production word is sequential (no number moves) and which word class a nucleus is remains qou-5vhf. See qou-ls86's 2026-09-03 entry and docs/audits/2026-09-03-markov-trace-not-bond-multiplicative-n4.md.


## 2026-09-04 — CORRECTION: spin is NOT the residue, and I cited a bean for the opposite of what it says

Retracts the last line of the 2026-09-03 section above. **The linking-matrix
result is untouched** — `lk` IS `I₃`, both channels at `I₃ = 0`, achievable
asymmetry exactly 1. What was wrong was its *"still open"* list, which ended:

> anything carrying **spin**, which is what actually separates the channels

**Why that is wrong.** The channels do differ in `S` (1 vs 0), so it is not
false as physics — it is false as a statement about the *search*, which is what
it was being used for. In the S-wave Pauli **locks** spin to isospin: space
symmetric ⇒ spin and isospin symmetry opposite, so `S=1 ⟺ T=0` and `S=0 ⟺ T=1`.
A Pauli-consistent interface carries a projector in each SU(2) with the roles
exchanged, and the same two scalars multiply to the same number —
`QOU.QBeta.InterfaceScalar.separable_interface_degenerate`
(`InterfaceScalar.lean:628`, sorry-free).

**The sharper half, which I had missed.** That carrier's own docstring: *"The
conclusion holds for **every** `fSpace`, so no choice of space index rescues a
separable interface."* So neither a spin factor nor a space factor escapes while
the interface is separable. And the one surviving shape `qou-vbyi` names — the
non-separable `(S,L)` tensor coupling — is closed by
`TensorCouplingCannotUnbindSinglet` (#6488), which landed the same day I wrote
the error.

**The citation error, which is the part worth keeping.** I credited bean
`qou-7zob` as *"reaching the same wall from the flavour side"*. It does not: its
body **refutes** the spin route, stating the Pauli lock in as many words. I
matched it on topic and cited it on agreement without reading it, and that
citation shipped in five merged artifacts (#6461). Recorded as a TRAP in
`.claude/agent-memory/corpus-grepper/MEMORY.md`: a title tells you the subject,
never the verdict.

**WHERE THE RESIDUE ACTUALLY IS.** `separable_interface_degenerate` *assumes*
`fSpin s1 = fIso t1` and `fSpin s0 = fIso t0` — that the **same two projector
scalars** serve both SU(2)s. Hypothesis, not derivation. A framework giving the
two SU(2)s different scalars breaks the lock and the degeneracy with it. Nothing
in the corpus shows they must be equal; nothing shows they may differ.

And note the *shape* of that question: it is about **how the interface is
constructed**, not about which quantum number is attached to it. All four routes
this arc has closed — trace subtraction, `μ̄`, linking data, spin — were of the
second kind. That may be the more useful finding than any one of the closures.

Sites corrected (PR #6553): the probe (×2), the audit doc, corpus-grepper
`resolved-topics.md`, and this bean.


## 2026-09-04 — the Pauli lock's hypothesis, measured: two SU(2)s of different origin, and D9 has no witness

Follows the correction above, which named `separable_interface_degenerate`'s
equal-scalars hypothesis as the residue without quantifying it. Audit:
`docs/audits/2026-09-04-pauli-lock-rests-on-an-unexamined-su2-identification.md`.

**What the hypothesis asserts.** `hplus`/`hminus` say the **same two projector
scalars** serve both SU(2)s. Concretely those are the Hecke spectral projector
weights of a **single `σ`** (`μ± = y_(2), y_(1,1)`). So one `σ`'s scalars are
asked to represent two symmetries — and the corpus does **not** treat them as
one symmetry. Per `docs/duality-tracker.md`: **D9** isospin `SU(2)_I` is a
flavour swap `u ↔ d` on colour-sheet flavour triples (canonical bowtie); **D10**
spin `SU(2)_S` is an icosahedral rotation via `S₅ → A₅ ≅ I ⊂ SO(3)`. Different
constructions; nothing obliges them to share a pair of scalars.

**Can the corpus settle it? The obstruction is ASYMMETRIC.**

- **D9 — no witness.** `class IsospinFromCanonicalBowtie` has **no instance**
  corpus-wide; the only "instance" in its file is the docstring calling it the
  conjectural witness. Corroborated by `WignerSU4FromSpinIsospin.lean:4` —
  *"Once … are formalized"*. Matches the tracker's own **"D9 is the bottleneck"**.
- **D10 — IS constructed, but builds something else.** `BringFiberAction` has a
  content-bearing instance `bringFiberAction_icosahedral` — the genuine
  icosahedral Reeb map `θ_λ = arccos(χ_λ(C₅)/dim_λ)`, `five_distinct_classes`
  proved from the A₅ character table. But it builds a map **A₅ irrep → rotation**,
  not projector scalars for the spin channel, and its own scope note leaves the
  `W_λ = d_q²/D²` Plancherel obligation open.

**A correction I caught before shipping.** My first draft of that audit said
*"neither is constructed"*. The D10 instance refutes it. Caught by grepping for
an instance rather than trusting the stub's *"conjectural witness"* docstring —
which is the same failure mode as the `qou-7zob` miscitation one section above,
twice in one day. The file is renamed off the wrong claim and records the
correction rather than hiding it.

**Two staleness findings**, neither fixed (out of scope, worth a follow-up):
`S5SO3FiberAction.lean`'s class docstring still says *"no global instance is
provided, so downstream theorems are genuinely conditional on it"* — they are
not; and both D9/D10 content stubs advertise `lean/QOU/BraidsAndKnots/*.lean`
files that **do not exist**, so their `lean.ref` resolves only by sibling
fallback.

**Status change.** The four closures (rank `= n`, `μ̄` selector, linking data,
`Δ₃,₃` ceiling 9) are untouched and rest on their own arguments. The fifth —
"the Pauli lock closes the channel asymmetry" — is now: *closes it **provided**
the two SU(2)s carry the same projector scalars*, an identification between
constructions of different origin, one without a witness. That is materially
weaker and should not be listed beside the other four.

**Scope: a scope statement, NOT a refutation.** It does not claim the scalars
differ — exactly as unestablished as the converse.

**Next.** Not a sixth invariant. A witness for D9 would make the equal-scalars
question decidable for the first time. Larger than anything in this arc; already
tracked in `docs/duality-tracker.md`.
## 2026-09-04 (qou-sorn) — the word-level route dies of the same gap. Formalize-first: the only non-monotone shape carrying a Markov-trace cross term is the cyclic square (g_m g_{m+1})^2 (RevisitClassCrossTerm.lean); measured on 2H–4He with the production binding law it gives ≤1 MeV total and SHRINKS with A (3He 1.00 → 4He 0.68 MeV) against residuals growing 7 → 27 MeV, because it multiplies a product of sub-unit letter traces. Same intensive/extensive gap as the four bond-graph routes. Judgement: the extensive term is not a functional of the single atom word's tr_M.

## 2026-09-04 — the Pauli lock is a PAIR-LAYER claim; a sibling's result applies to it independently

Sibling `88ca3408d4` landed within the hour on this same bean, by a different
route, and it bears on the section above. Neither was written with the other in
view.

**Their result.** `QOU.MassTheory.PairIsospinAssignment` — no `C`-invariant total
isospin label separates the two `H₂` blocks (`C` swaps them, `T` is `C`-invariant,
so `T` is constant) — with the explicit warning that this is *easy to over-read*
as closing the channel asymmetry. It does not: the argument turns on ONE `C`-orbit
covering both blocks, and at the forced six-strand carrier `H₆`, `C` acts on 11
blocks in **6** orbits.

Verified here independently rather than cited (exact partition arithmetic, no
floats): `n=2` → 2 blocks, **1** orbit; `n=6` → 11 blocks, **6** orbits, `(3,2,1)`
self-conjugate.

**Why it applies to my section above.** `separable_interface_degenerate`'s `μ±`
are `y₂`, `y₁₁` — the weights of the two **1-dimensional blocks of `H₂`**
(`InterfaceScalar.lean:365–384`). So the Pauli lock is a **pair-layer** statement,
structurally the same layer as `PairIsospinAssignment`. By the sibling's own
argument a pair-layer obstruction does not propagate to six strands — and the
two-nucleon link's forced carrier **is** `H₆`.

**Consequence — two independent, non-overlapping reasons the fifth closure is
weak:**

1. **Conditional** on an unexamined identification of the spin/isospin `SU(2)`
   projector scalars, one side of which (D9) has no witness. *(my finding)*
2. **Pair-layer**: it does not reach the layer where the question lives.
   *(the sibling's)*

**Scope.** Does **not** claim a `T`-labelling of `H₆` exists — the sibling
disclaims that too. Does **not** reopen the magnitude, still bounded by the
integer-exponent crossing budget `R ≤ s² = 9` (`block_transposition_lift_probe`,
which the sibling's commit cites for exactly this role). Two layers, two
obstructions, neither subsuming the other: the pair layer cannot **label** the
distinction; the six-strand layer can label it but cannot reach the **magnitude**.

**Convergence.** Two agents, adjacent conclusions on one bean within an hour, by
different routes — `C`-orbit structure of Wedderburn blocks vs the projector-scalar
hypothesis of an interface theorem. Recorded as two arguments rather than merged
into one claim, because they remain independent.

## 2026-09-04 later (qou-rp9i) — under #6611's log law the cyclic-triple reorder IS extensive (per-bond constants), so 'not a functional of tr_M' from earlier today is too strong as stated; but the class over-shoots 3–8× with the retracted +N−Z asymmetry sign. Word-level route: closed for this class under both laws.


## 2026-09-05 (qou-o43i) — CORRECTION to the 2026-09-04 "Next": a D9 witness cannot settle the equal-scalars question, and the hypothesis is not a corpus claim

The 2026-09-04 entry above names `separable_interface_degenerate`'s equal-scalars
hypothesis as *"where the residue actually is"* and sets the next step as *"a witness for
D9 would make the equal-scalars question decidable for the first time."* Two measured
corrections; the **linking-matrix result is untouched**, as is the sibling's pair-layer
obstruction.

**1. The theorem has ZERO instantiation sites.** Measured over every tracked file with
Lean comments stripped: **1 declaration, 0 applications, 28 prose citations in 13 files**
(`scripts/separable-interface-instantiation-audit.py`, `--selftest` 5/5, `--strict`
gates, so the claim cannot go stale silently). `fSpin`/`fIso` are arbitrary functions on
arbitrary types, so `hplus`/`hminus` are the antecedent of a universally-quantified
implication — not a claim about this corpus that any witness could settle. The
`μ± ↔ y₂/y₁₁` identification lives in the theorem's **docstring**; the entry above cites
`InterfaceScalar.lean:365–384` for it, which is `weight_eq_proj_scalar` in a different
section, about different variables.

**2. D9's carrier was rebuilt around a different claim on the same day.** #6671 replaced
the content-free `holds : Prop` with three fields — `0 < q`, `q ≠ 1`, and one real
equation for `Δm/M_N`. Its own header states the categorical half (crystal functional,
isospin swap) is **NOT encoded**. So an instance supplies a real-number identity while the
equal-scalars question is about projector scalars of a swap construction: the two objects
do not touch. Worth knowing before a tranche is spent building the witness.

**3. Formalised — the closure is carried entirely by its hypotheses.** Two sorry-free
library files, split per §7c (`SeparableInterfaceHypothesesHaveContent.lean` generic +
`…Real.lean` archimedean): drop the hypotheses and the conclusion is **false**
(`separability_hypotheses_have_content`); keep them and the residual mathematics is
`mul_comm` (`degeneracy_is_commutativity`); release them and the channel ratio is
**unconstrained** — every field element, positivity preserved over `ℝ`, the measured
**33.7055** among them (`asymmetry_attainable_with_distinct_scalars`,
`distinct_positive_scalars_reach_any_ratio`, `measured_asymmetry_attainable`). Scope (b)
on {separable interface, distinct scalar pairs}, invariant: a field has no nontrivial
multiplicative constraint between two free elements.

**NOT claimed:** that the two SU(2)s carry different scalars — as unestablished as its
converse. Nothing refuted; `separable_interface_degenerate` is correct. Detail, including
a `check-sidecars.sh` `(R :=` blind spot deliberately left unswept: `qou-o43i`.


---
**Update 2026-09-07 (session alien-calculus, PR #6988) — the `Brunnian` hypothesis this bean's surviving route leans on is NOT satisfied by L6a4, and the corpus already proved it. Sorry-free both ways.**

Went to compute `w3` for L6a4 — the triple-mutual crossing energy that `b3_eq_neg_tripleMutual_of_brunnian` says *is* `b3` — and the theorem's hypothesis does not hold for the carrier.

**`QOU/Mass/` carries THREE unrelated definitions named `Brunnian`** (`CrossingModelPairLocality:103`, `MilnorIndeterminacyGate:137`, `FreedmanHeGenusHandleNeedsVanishingLinking.BrunnianAt:70`). Two matter here and they are different properties:

| name | condition | true of L6a4? |
|---|---|---|
| topological Brunnian | pairwise Gauss linking number `= 0` (`n₊ = n₋`) | **yes** |
| `CrossingModel.Brunnian` | pairwise mutual **energy** `w₂ = 0` | **no** |

**And this bean's own 2026-08-30 result is what proves the first does not imply the second.** `BrunnianBindingChannel.brunnian_binding_survives` gives `0 < countChannel m m q` for a crossing pair at `q > 1` — *"the mutual energy is nonzero even though the pairwise linking number is zero. This is the crux of `qou-brng`'s surviving route."* Binding **survives** the Brunnian vanishing; that is the whole point.

**A false cross-reference carried the conflation.** `CrossingModelPairLocality`'s docstring read *"(`QOU.Mass.BrunnianBindingChannel` establishes that the ³He/⁴He carrier `L6a4` has this property.)"* — of `w₂ = 0`. It establishes the opposite. Corrected in place.

**Formalised, `QOU.Mass.BrunnianHypothesisNotSatisfied`** (lean-direct exit 0, `-DautoImplicit=false -s 65536`, no `sorryAx`):

- `not_brunnian_of_pair_binding_ne_zero` — **data route**: the pair cumulant is `−w₂`, so the measured `b₂ = 2.2245662 MeV` refutes `CrossingModel.Brunnian`, by the same contrapositive the corpus already uses one theorem over for `b₃`.
- `not_brunnian_of_countChannel` — **structure route**: a crossing pair at `q > 1` has strictly positive count-channel energy, so `w₂ ≠ 0`, with **no appeal to data**.
- `brunnian_forces_both` — states what a Brunnian model would need, so the two routes visibly deny one thing.

**Nothing in `CrossingModelPairLocality` is refuted** — every theorem there stays true. What is established is that the hypothesis is unavailable for this carrier, so **`b₃` does not cleanly pin the bare triple channel**; the pair contamination the theorem discards is nonzero.

**The same misreading was committed to a witness and is fixed at the producer.** `pair-locality-shortfall.witness.json` asserted *"With a Brunnian carrier the pair terms vanish and b3 is exactly the triple channel"* while recording `b₂ = 2.2245662` in the same file. Producer description + second assertion re-scoped; the assertion still PASSES because what it tests is `b₃ > 0`. Re-run 6/6, **no numeric change** — text and provenance only. The shortfall figures were never Brunnian-dependent and are untouched.

**What this costs the surviving route.** The route is *"why the coordination count `M` is the binding multiplier while the mass carries the self-linking weight `lw`"*. That is unaffected — it rests on `CrossingEnergy.decomposition` and the count channel, both intact. What is lost is the shortcut that would have read `b₃` off as the triple channel directly. `w₃` still needs computing; it just cannot be obtained by identifying it with the measured `b₃`.


**Follow-up same session: renamed, and the forward computation turns out to be ALREADY CLOSED NEGATIVE.**

`CrossingModel.Brunnian` → **`NoIsolatedPairEnergy`** (#6988). Measured first: it and its three downstream theorems have **zero consumers** outside their own file — the four other importers use only the pair-locality half. Renamed rather than deleted because the implications are true and `not_pairLocal_of_noIsolatedPairEnergy` depends on **no axioms at all**; the name was the trap, not the mathematics. There are five `Brunnian`s in the tree and this was the only one meaning *energy* rather than *linking number*, and the only one false of L6a4.

**The file header was the worst of it** and is rewritten. It asserted the corpus "already establishes that the ³He/⁴He carrier L6a4 is Brunnian (`BrunnianBindingChannel`, #6125)" and that `b3_eq_neg_tripleMutual_of_brunnian` "is the falsifiable payoff … Measuring `b₃` therefore pins the Brunnian triple channel to a specific number."

**THE PAYOFF WAS COLLECTED, AND IT IS A NEGATIVE — this is the part that matters for this bean.** `QOU.Mass.BrunnianTripleExhaustion` already computes the count-channel prediction directly, and it is sorry-free:

- `no_carrier_reproduces_b3` — `b₃/b₂ = M − 3` is an **integer** for any total crossing count `M`, while the measured ratio lies strictly in `(0,1)`. **No carrier of any crossing number works.**
- `gap_increases_beyond_four` — the exhaustion covers **every** `M`; no larger search exists to run.
- `carrier_gap_bounded_below` — the miss is at least `532229/1483044 ≈ 0.35888`, **55.98 %** of the measured value, attained at `M = 4`.
- `borromean_is_the_unique_minimal_carrier` + `minimal_carrier_bRatio_eq_zero` — L6a4 itself (`M = 3`) gives `b₃/b₂ = **0** exactly`.

So the forward route I proposed one turn earlier — *compute `w₃` for L6a4 from the count channel, predict `b₃`* — **was already run and is closed**. The count channel predicts `b₃ = 0` for the Borromean carrier against a measured `+1.4262225 MeV`. Reading `b₃` off as the triple mutual energy, via the hypothesis that does not hold, would have concealed exactly this.

**What that means for this bean's surviving route.** The route is *"why the coordination count `M` is the binding multiplier while the mass carries the self-linking weight `lw`"*. It is **not refuted** — `CrossingEnergy.decomposition` and `brunnian_binding_survives` stand. But the count channel **alone**, with a uniform per-crossing weight, provably cannot produce the measured three-body cumulant, for *any* carrier. `pairDependent_weight_not_a_count` in the same file is the shape of the escape: a weight that varies per pair is not a count. So the open question sharpens to whether there is a *derived* per-pair weight — and per the anti-fit rule, a per-pair weight chosen to hit `b₃` is a fit with three free numbers, which is worse than the honest miss.

Verification note for whoever touches this next: a bare `lean`-direct pass is **not** sufficient after a rename — a dependent compiles against the cached olean, which still carries the old name. Build the renamed module into a hardlinked shadow first, then compile the dependents against that. All four are green; axioms unchanged; no `sorryAx`.

## Claimed 2026-09-08 ~09:00Z by session qou-vyvt (owner authorised overlap with sibling #7155 Avenue 2). Angle: the SURVIVING route named in this bean — linking (mutual) vs self-energy (self-linking) amplitudes — approached from the three bounds that landed today: #7165 (bond-cut identity: all layout dependence of a positive pair-additive count is delta*n_pn, and no convex interface supplies the symmetry energy), #7174 (the residual is 98.6 percent a UNIFORM factor, undecidable against a uniform bond rescaling at fixed law), #7155 (every expressible edge set is a linear layout, and a linear layout has no bulk). Distinct from #7155: that PR excludes edge sets; this front asks what object supplies the extensive term GIVEN the exclusion, i.e. why the binding multiplier is the mutual linking count while the mass multiplier is the self-linking weight lw.

--------

## 2026-09-11 (session qou-vyvt, front `brng`, PR #7181) — the extensive term, attacked from the complement of #7165. One class DECIDED, scope-(b). The bean stays open.

Owner-authorised overlap with #7155; intent posted there naming the distinct
angle. #7155 excludes edge sets *inside* the bond-count class; this front asks
what lives *outside* it.

### The candidate enumeration, and which #7165 hypothesis each escapes

`QOU/Hecke/BondCutSymmetry.lean` excludes **positive pair-additive bond
counts**. Its two load-bearing theorems name their hypotheses, so the live
complement is readable off them rather than guessed:

| # | class | hypothesis of #7165 it escapes | status |
|---|---|---|---|
| A | genuine 3-body / higher connected cumulant | the `bondSum` SHAPE — `bondSum` is literally `e_pp·n_pp + e_pn·n_pn + e_nn·n_nn`, three terms | **heavily blocked already.** `MayerThreeBodySign` (sign threshold-forced, wrong against AME, bond-set independent); `BrunnianTripleExhaustion.no_carrier_reproduces_b3` (`b₃/b₂ = M−3` is an integer for every crossing count `M`, measured ratio is in (0,1) — no carrier of any `M`); `BodyOrderRecurrenceDepth` (depth ≥ 3 forced, 3 terms cannot test it) |
| B | a bond energy that is **not sign-definite** (`e_t < 0`, i.e. `b_t > 1`) | `bondSum_nonneg`'s `0 ≤ epp`, `0 ≤ epn`, `0 ≤ enn`; hence `bondSum_ne_semf_neutronMatter` | **live, smallest escape, and it is the one the physics wants** — a repulsive bond is what unbinds neutron matter. Not attacked here. Note `qou-ib3g` already measured that the framework *can* produce `b > 1`: at crossing multiplicity `m = 2` both `b_pp` and `b_pn` exceed 1, i.e. a negative bond energy. So the class is not merely conceivable, it is realised. |
| C | not a bond count at all — a **trace / spectral** object, `Σ_λ y_λ χ^λ Δ_λ` | BOTH at once: not the `bondSum` shape, and `0 ≤ n_t` fails because `Δ_λ = (−1)^{n(λ)}·dim V_λ` is **signed** | **this is what I attacked.** Its *multiplicity* sub-channel is now excluded (below); its *dominant-summand* sub-channel is untouched and is the live remainder |
| D | fibre-level / higher order in `q` (a Habiro element whose order-zero rendering is the observable) | every #7165 statement is at order zero | live, not attacked here. Note the 2026-09-03 owner ruling makes the full tower mandatory, so this class is not optional in the long run |

### What was decided, and it is a negative

**`QOU/Mass/MultiplicityCountingBound.lean` + `QOU/Mass/MultiplicityNotExtensive.lean`
— 11 theorems, sorry-free, `lean`-direct exit 0 (`-DautoImplicit=false -s 65536`)
in import order, every declaration on exactly `[propext, Classical.choice,
Quot.sound]`, no `sorryAx`.**

A trace sum over `λ ⊢ 3A` can be large two ways: one summand large, or many
summands. The second — the **multiplicity channel** — is capped by the triangle
inequality at `log(card)`, for any signs, any weights, any braid word. That
bound is one-sided *in the direction that decides it*: cancellation only makes
the sum smaller, and the claim under test is that many summands make the
binding bigger.

With `card = p(3A)` and Hardy–Ramanujan `log p(n) ≤ π√(2n/3)` — carried as an
explicit `_of_` hypothesis, not proved — the channel is `O(√A)`.
**Sub-extensive. It cannot be the extensive term.**

Three forms, none turning on the undetermined `E₀`:

* `sqrt_lt_linear_of_sq_lt` — explicit threshold `A > (c/a)²`, not a limit;
* `card_ge_exp_of_linear_le_log_card` — to supply rate `a` the summand count
  must be `≥ exp(a·A)`, **exponential**, against `p(3A) = exp(O(√A))`;
* `sqrt_law_shortfall` / `sqrt_per_nucleon_antitone` — the scale-free form.

### Measured (`computations/brng_multiplicity_channel_bound_probe.py`, 9/9, 70 dps, proton pin, exact integer partition counts, AME2020 as `Decimal`)

* **R1** discharges the Hardy–Ramanujan hypothesis numerically for every
  `A ∈ 2..400` with exact counts — tightest at `A = 2`, slack 3.885.
* **R2** exact counts sit strictly *below* the asymptotic bound everywhere
  (ratio 0.382 at ²H → 0.876 at ²³⁸U), so using them is conservative.
* **R3** (`E₀`-dependent, labelled): cap/B = 0.449 (¹²C), 0.225 (⁵⁶Fe),
  0.141 (²³⁸U) — falling.
* **R4** ⁵⁶Fe needs `10^50.6` summands, `p(168)` gives `10^11.4` — short by
  **39.2 orders**; ²³⁸U short by **159.0 orders**.
* **R5 headline, `E₀` cancels**: normalising at ¹²C, the measured binding ratio
  outruns the multiplicity ratio by **1.140 at ¹⁶O rising monotonically to
  3.191 at ²³⁸U**. A constant mismatch would be a *scale* error; a growing one
  is a *shape* error — and per #7174 / `qou-v8ct` the scale is undecidable at
  fixed law, so only a scale-free argument can settle this.

**Where it does NOT bite, recorded as its own assertion rather than buried in a
table: at `A = 2` the cap EXCEEDS the binding by 4.56×** — `p(6) = 11` summands
is more than the `exp(B/E₀) = 1.7` required. That is not a defect; it is what
the explicit threshold says. With exact counts the crossing falls between
`A = 2` and `A = 4`, so the exclusion bites from ⁴He up and strengthens
monotonically.

### Scope, and what stays open

**Scope-(b) structural exclusion** — the invariant is the triangle inequality
plus sub-exponential growth of `p(n)`, so it excludes the *ingredient*
(multiplicity of the partition sum), not one construction's magnitude. It
excludes that channel **alone**.

**The live remainder, and it is now sharper than before**: the extensive term,
if the trace sum carries one, must live in the **dominant summand's own
log-weight** `log|y_λ χ^λ(β_A)|`. The atom word on `3A` strands has length
`Θ(A)`, so a single character's log *can* grow linearly — right growth class.
This is an **independent, unconditional** reason for the concentration that
`QOU/BraidKnot/BindingConcentration.lean` argues from LP sparsity: there,
concentration is a property of the chosen linear program; here it is forced by
counting, whatever program is written.

Classes B and D are untouched and stay live.

**The saturated-fraction ≈ 0.95·ℏ_q² match was not used, not wired, not forced,
and no route was ranked by its residual.** Nothing existing moved.

**Bean stays OPEN** (rule 13a — its subject is an open conjecture).

--------

## 2026-09-12 (session class-b, PR #7204) — CLASS B attacked. It escapes invariant (2) and NOT invariant (1). Bean stays open.

Row B of this bean's own escape enumeration: *"a bond energy that is not
sign-definite (`e_t < 0`, i.e. `b_t > 1`) — live, smallest escape, and the one
the physics wants."* Attacked against the named hypotheses of #7165.

### The decisive reading, and it was available without any new mathematics

`BondCutSymmetryLogBound.energySlope_convex_le` takes `0 < b_nn`, `b_nn ≤ b_pp`,
`0 ≤ w ≤ 1` — and **never `b ≤ 1`**. `b ≤ 1` is exactly what makes the energies
non-negative, so **invariant (1), the `δ ≤ 2 ln q` cap, was never a consequence
of positivity.** Class B escapes `bondSum_nonneg` and is capped by the same
number as the positive class, *identically*. Positivity was the binding
constraint on ONE thing only — the layout-free neutron-matter argument,
invariant (2).

Of #7165's twenty declarations exactly **two** carry a sign hypothesis on an
energy: `bondSum_nonneg` and, through it, `bondSum_ne_semf_neutronMatter`.
Every other statement — the cut identity, the segregated and well-mixed
decompositions, `symmetryCoeff_pos_iff`, `cut_le_degree_bound`, and the whole
log-bound file — quantifies over the energies with no sign constraint, and so
is a class-B theorem already.

### Lean (20 declarations, sorry-free, `lean`-direct exit 0 in import order)

`QOU/Hecke/BondCutSymmetryNoSignDefinite.lean` (generic, §7c) +
`QOU/Hecke/BondCutSymmetryNoSignDefiniteLogBound.lean` (archimedean). Verified
with `lean -DautoImplicit=false -s 65536`; `#print axioms` on all 20 gives
`[propext, Classical.choice, Quot.sound]` on 19 and `[propext]` alone on
`bondSum_energyShift` (strictly weaker, not a defect). **No `sorryAx`
anywhere.** Counted from an UNTRUNCATED log: the first capture was piped through
`tail -50` and showed only 16 of the 20, which is exactly the kind of
overstatement worth not making -- re-run and count.

* **`energySlope_energyShift` / `symmetryCoeff_energyShift`** — a **uniform**
  energy shift leaves `δ` and the symmetry coefficient *identically* fixed.
  `δ` is a second difference; a common additive constant cancels.
* **`bondSum_wellMixed_totalCount` / `bondSum_wellMixed_energyShift`** — the
  well-mixed layout's total bond count is `k·A/2` *independently of the mixing
  density `μ`*, so the shift contributes `s·k·A/2`: a **pure volume term**. It
  cannot produce, cancel or rescale a `(N−Z)²`.
* **`enn_neg_of_semf_neutronMatter`** — the escape is real and it is **priced**:
  any bond count reproducing the SEMF at pure neutron matter *forces*
  `e_nn < 0`, i.e. `b_nn > 1`. A falsifiable condition on a derived quantity,
  which converts a structural exclusion into a measurement.
* **`energySlope_gt_convexCap_iff`** — beating the cap is **equivalent** to
  `e_pn > e_nn`, i.e. `b_pn` strictly below *both* like-species bonds and
  outside the convex hull `weight_of_convention` derives it in.
* **`exists_bondRescale_all_energies_neg`** — from any positive law there is a
  common `c > 0` making all three energies negative, with `δ` unchanged.
* **`classB_symmetryCoeff_le_of_convex` / `classB_rescaled_symmetryCoeff_le`** —
  the composition: class B's cap **equals** the positive class's cap.

### Measured (`computations/qbeta/qbeta_class_b_nonsigndefinite_bond_probe.py`, 20/20, 50 dps, proton pin, convention D, mpmath + exact `Fraction`, no float64)

Every bond factor is *derived* — the two-strand convention-D Markov trace
`tr(a·σ + b) = a·z_D + b` of the canonical interface letter, `z_D = q³/(q²+1)`,
with the letters as `atom_braid_word_3A` emits them. Nothing chosen.

* **R1** `b_pp = z_D` **exactly** — the p–p bond factor *is* the convention-D
  Markov parameter — and `(q²+1)` divides all three denominators, checked
  exactly over `Fraction` at a rational sample `q` (the convention test that
  keys on the ANSWER, per AGENTS.md).
* **R3 — the headline. At the canonical multiplicity the derived energies are
  ALL POSITIVE:** `b_pp = 0.6126880371`, `b_pn = 0.5082297894`,
  `b_nn = 0.4036277384`, giving `e = +0.4899 / +0.6768 / +0.9073`. **The
  corpus's own law is not in class B.** Class B is a hypothesis about a
  construction the framework does not have.
* **R4** `δ = −0.0217592325` (wrong SEMF sign), matching the #7165 record.
* **R5** cap `2 ln q₀ = 0.2086814406`; `a_A^eff ≤ 0.441 MeV` at `k = 2` and
  `2.647 MeV` at `k = 12`, i.e. **53.7× and 9.0× short** of the SEMF 23.7 MeV —
  **with no sign hypothesis anywhere in the derivation.**
* **R6** the class-B rescaling `c = 1/b_pp + 1/b_pn + 1/b_nn = 6.0773` drives all
  three to `b' = (3.723, 3.089, 2.453)`, every energy negative, and `δ` moves by
  `< 1e-40` — the numerical companion to `energySlope_bondRescale`.
* **R7** the price: `b_nn > 1` required, `b_nn = 0.4036` derived — **short by
  2.478×**. The escape's necessary condition fails on the derived number.
* **R8** to supply `a_A` at `k = 12` a law needs `δ = 1.8687` (9.0× the cap) and
  hence `b_pn = 0.07674`, **5.26× below** `b_nn` — far outside the convex hull.
  Choosing that number is a one-parameter fit and is forbidden.
* **R9 — the sharpest cell.** The only mechanism in the corpus that produces
  `b > 1` is the interface multiplicity `m` (this bean's own `qou-ib3g`, already
  REFUTED there: repeating a letter on the SAME generator stays in a 2-dim
  subalgebra, so `m` is not a multiplicity of bond strength). Scanning
  `m = 1..12` — the **whole table**, no `m` selected, since selecting one for
  its residual is the discrete-parameter fit the directive names — **class B
  DOES flip the sign**, `δ > 0` from `m = 2` on, and at `m = 12` all three bonds
  are repulsive with `δ = +0.4702`. **And `a_A^eff` reaches only 5.963 MeV, still
  4.0× short.** `m = 7, 9, 11` are undefined (a bond factor crosses zero).
  Flipping the sign is cheap; the magnitude is not on offer.

### A correction to my own verification claim, and it is the sharper one

I first reported `scripts/precision-gates.sh --changed` as **exit 0**. That was
the exit status of `tail`, not of the gate: re-run with the output redirected to
a file, **`GATE_EXIT=1`**. The gate is RED on this tree.

**It is not red because of this branch, and that part IS measured rather than
inferred.** Every red list in that gate enumerates its offenders, and
`qbeta_class_b_nonsigndefinite_bond_probe` appears in **none** of them (grep
count 0 over the whole 494-line log). The probe **writes no witness at all** — it
prints its JSON to stdout — so it is structurally invisible to every
witness-keyed ratchet, and both extra-root scans report `NEW dirty witnesses: 0`.
The two `.lean` files cannot move a Python/witness ratchet. The reds are
corpus-wide baseline state: 994 witnesses carrying raw float64 (28,151 fields),
130 NEW q0-anchor-missing, 5 NEW stale.

**What was NOT measured:** the gate was not separately run on `origin/main` to
confirm the same reds there. The observation that decides it is the weaker but
sufficient one — the offender lists name no file from this branch.

Recorded because the pattern is the one AGENTS.md names twice: a pipeline's exit
status is not the command's, and a gate's red is not evidence about your diff
until you have read WHICH files it names.

### A normalisation trap, recorded because it cost a red assertion

`qou-ib3g`'s *"factors at m=3: 0.335 (pp), 0.984 (pn), 1.709 (nn)"* are **energy
ratios `L(m)/L(1)`**, not bond factors. As bond factors `b(3) = 0.8485 / 0.5139
/ 0.2122`, and comparing the two disagrees by 8× on the nn leg. Reproduced
against the quantity each claim actually names: the `m = 3` figures as ratios
(0.335281 / 0.983526 / 1.70864) and the `m = 2` `b > 1` claim as bond factors
(1.12809 / 1.011). Same error class as the `c₃` 3.47 %/3.35 % pair AGENTS.md
flags.

### Scope, stated per the (a)/(b) rule

* **scope-(b), structural.** *Class B does not escape invariant (1).* Invariant:
  `energySlope_convex_le` + `half_splitting_pinned`, whose hypotheses are
  `0 < b_nn ≤ b_pp` and `0 ≤ w ≤ 1` — no sign condition. Composed in
  `classB_symmetryCoeff_le_of_convex` / `classB_rescaled_symmetryCoeff_le`.
* **scope-(b), structural.** *A uniform passage into class B is powerless on the
  symmetry term.* Invariant: `energySlope_energyShift`, a ring identity; the
  shift is a pure volume term by `bondSum_wellMixed_energyShift`.
* **scope-(b), structural.** *Beating the cap is equivalent to leaving the
  convex hull.* Invariant: `energySlope_gt_convexCap_iff`, an iff with no sign
  hypothesis.
* **scope-(a), scope-limited negative.** *The corpus's derived law is not in
  class B, and the one mechanism that reaches it supplies no magnitude.* This is
  a measurement of one construction at `m = 1..12`; it constrains this
  construction's magnitudes, not the ingredient. A different derived interface —
  one landing `b_pn` below the hull for a reason — is **not** excluded by it.

### What class B genuinely buys, and it is not nothing

It **does** escape invariant (2): at `Z = 0` the bond sum is `e_nn·n_nn`, which
a negative `e_nn` makes negative, so a class-B law *can* unbind neutron matter —
which is what the physics wants and what #7165 forbade. The exclusion of class B
is therefore **weaker** than the exclusion of the positive class: it is not
layout-free, it runs through the magnitude cap instead. **The open question is
unchanged and now sharper: what derived object puts `b_pn` more than 5× below
both like-species bonds?** Nothing here answers it, and picking the number
answers nothing.

**Bean stays OPEN** (rule 13a — its subject is an open conjecture). Classes A, C
(dominant-summand sub-channel) and D remain as #7181 left them.

## 2026-09-12 — the live remainder (dominant summand's own log-weight) is being TESTED — bean qou-m8f3

Branch `claude/dominant-summand-extensive-test-2026-09-12`. Ursell inversion of `L(A) = log|y_λ* χ^λ*(β_A)|` (largest |term| of the trace, no choice) on the live alternating-core word for A = 2, 3, 4, proton pin, convention D. Result appended to `qou-m8f3` and, on completion, below this entry. Append-only.


### 2026-09-12 RESULT (qou-m8f3, PR #7200) — the dominant-summand log-weight is NOT the extensive term at A ≤ 4: scope (b)

For every typed cluster with A ≤ 4 the trace's dominant summand on the live alternating-core word is the ONE-ROW block `[3A]` (margin ≥ 24.6 %); its character is a product over letters (ring hom; verified 1.2e-49; `QOU/Mass/OneRowBlockLetterProduct.lean`, generic ring, uncompiled here), so `log|y_λ* χ^λ*|` = word-free `log y_(3A)` + an EXACTLY chain-edge-additive letter sum (7.4e-51). Complete-graph cumulants are the chain's missing-edge accounting (`b₃ = −b₂`, ratio −1 exactly; AME +0.81/+0.47); the only other piece of `ΔL` is the free-side argmax switch (bond-free), which is 100.6 % of ⁴He's `E₀·ΔL = 3.93 MeV`. Uniform-e₂: e₂ = −0.023 MeV, b₃(³H) = +0.483, b₃(³He) = −0.391 MeV (opposite signs on the mirror pair). No connected many-body term with nuclear content. The live remainder named on 2026-09-11 is CLOSED at A ≤ 4; at ⁶Li the dominant block is two-row `[15,3]` (E₀·ΔL = 8.5 vs 32.0 MeV) and the channel is scope (a) there. Classes B and D untouched and live. Secondary (binding-sum argmax `|yχΔ|` = BindingConcentration's `(5,1)/(6,3)/(9,3)`, two-row): uniform b₃(³H) = +1.016, b₃(³He) = +0.747 MeV (0.56×/0.72×) but typed b₃(ppn) < 0, b₄(⁴He) = −4.27 (wrong sign), b₃ monotone in N−Z — reported, NOT wired. Audit: `docs/audits/2026-09-12-dominant-summand-extensive-test.md`. Bean stays OPEN.


---
**Update 2026-09-12 (session ursell-partition-function, PR #7198, bean `qou-rwhv`).** The Mayer/Ursell vocabulary on the 3-body cumulant is now CLOSED, and closed the other way from the 2026-08-30 reading. The corpus `b3` is the third Ursell coefficient (with the Mayer sign, `−phi^T_3`) of the hard-core lattice gas on the nucleon sites with the interface-letter traces as pair weights, grand-canonical over sub-clusters; `b3 < 0` for EVERY bond triple in (0,1) — no 2/3 threshold — by the Ursell alternation (Lean `UrsellPartitionFunctionB3`, sorry-free). The "missing (−1)^(n−1)" is the same expansion at negative activity. So the extensive-term frontier's bullet 4 is STRENGTHENED, not contradicted: the multiplicative assembly cannot give `b3 > 0` at any `f_pn`. Within Mayer, a positive term needs an attractive channel (a letter with trace > 1; none present, scope a); outside it, a non-Mayer assembly. Magnitude untouched: the Mayer coefficient at the live chain bonds is −1.23 MeV (3H) / −0.80 MeV (3He) against AME +1.81 / +1.04. Audit: docs/audits/2026-09-12-ursell-partition-function-for-b3.md.

2026-09-12 pointer: the A ≥ 6 remainder (two-row dominant block at 6Li, scope (a) in PR #7200 §5) is being tested in bean qou-vn6h, branch claude/two-row-dominant-block-a6-2026-09-12. Append-only; nothing here changes.

2026-09-12 (qou-vn6h, PR #7211): dominant-summand channel measured at 5 <= A <= 7. The trace's dominant block is two-row from A = 5 ([12,3]; [15,3]; [18,3] / [15,6]), it is NOT letter-multiplicative (Lean MixedSpectrumCharacterNotLetterMultiplicative + fixed-n residual 0.09 log units + Moebius interface cumulants non-zero at every order, non-local: non-adjacent pp-nn pair 22x the adjacent pp-pp), and its connected content is ANTI-binding: -3.50 MeV at 6Li, -3.62 MeV at 7Li, against AME shortfalls of +23.5 / +27.8 MeV. B/A of the dominant summand grows 0.98 -> 1.63 from A = 4 to 7 with no plateau. So the channel supplies no positive extensive term at any A tested (A <= 4: none, #7200; A = 5-7: negative, small). Scope (a) on the physics, (b) on the non-extension of the one-row argument. Classes B and D remain the live remainder. Audit: docs/audits/2026-09-12-two-row-dominant-block-a6.md.

---
**Update 2026-09-12 (session graded-binding-sign-convention, PR #7223, bean `qou-zlra`) — a note on row D of the escape enumeration (fibre-level / higher order in q). Bean stays OPEN.**

Row D was left "live, not attacked". Attacked at Vassiliev type two, on the chain, with the corpus's own functional: it does NOT supply the symmetry term through the live law. `QOU.Mass.GradedBindingFunctionalPairTerm` (sorry-free): the pair convolution `sum_{i<j} b_i b_j` that carries `(N-Z)^2` at type two is present in the BARE product for either sign and absent from EVERY product-additive functional (log, -log, alpha log) — and the live binding law is such a functional by owner ruling ("log is the unique map carrying multiplicative to additive"). So under the live law the higher orders in `q` inherit additivity order by order: the tower does not reopen row D for the chain. Measured: second differences in Z of `[h^2] log(tr_free/tr_atom)` are 0 at every A = 3..12 (both signs); of the bare `[h^2]` product they are 4.

What row D still has, and it is the only live thread this leaves: `unified-iterative-correction`'s per-BLOCK log `ln|tr_lambda(prod (c sigma + d))|` is NOT product-additive even on the chain (single-block `[h^2] log` has nonzero, non-constant second differences in Z for (3,1), (3,2), (4,1); computed signs, mixed). That functional is a different object from the live law (two inequivalent log readings coexist — recorded as a collision, not resolved), and the production accumulator was not scanned (> 300 s at A = 4 here). Row D is therefore narrowed to: the per-block log functional, if the framework means it, is the one place a type-two two-bond correlation survives on the chain. Scope (b) for the live law (invariant `additive_census` + `L_chain_eq_sum_of_intra`); scope (a) for the per-block rows (11 shapes, A <= 8, UIC-shaped word).

Also, for `qou-eqwg`'s open item: there is no non-commutativity inside a generator (transfer matrices commute exactly); the within-generator non-multiplicativity is the two-branch state sum, exercised only when two interface letters share a generator, which the chain never does. Audit: `docs/audits/2026-09-12-graded-binding-sign-convention.md`.


## 2026-09-12 (session stalled-agent-takeover) — class B's open "third bond family" is narrowed: the pn letter is an AVERAGE

This bean excludes the two derived families at the VALUE level (production letters
by `d <= 0`; isospin projectors by `mu_+ + mu_- = 1`) and records as open: *"a THIRD
bond family that supplies the sign-mixed pattern by derivation"*.

**The pn letter is not an independent third value — it is an AVERAGE, and an average
is never an extremum.** The required pattern `mu_pn > 1 > mu_pp, mu_nn` makes `mu_pn`
the strict MAXIMUM of the three. But `d_pn = (1/2 + delta/4) d_pp + (1/2 - delta/4) d_nn`
with both weights strictly positive for `delta in (-2,2)`, and the interface law
`mu = z + d` is affine, so `mu_pn` is a strict convex combination of `mu_pp` and
`mu_nn` — strictly between them, for EVERY `q`, EVERY admissible `delta`, and every
pair of like-pair offsets, whatever their values.

**Consequence for the open item:** a third bond family cannot rescue the pattern by
moving letters above 1. It must break the AVERAGING of the pn letter, or break
AFFINENESS of the interface law. Those are the only two hypotheses used, and neither
mentions a numerical value.

Lean `QOU/MassTheory/PnBetweennessBlocksSignMixed.lean` (6 decls, sorry-free,
lean-direct `-DautoImplicit=false -s 65536` exit 0, zero warnings, axioms
propext/Classical.choice/Quot.sound only). Probe
`computations/probes/pn_betweenness_blocks_sign_mixed_probe.py` 8/8, 70 dps, proton
pin, convention D, no float64 — including a CONTROL row showing the pattern becomes
satisfiable the moment `mu_pn` is unpinned from the average, which is what
establishes that the hypothesis and not the values carries the exclusion. Audit
`docs/audits/2026-09-12-pn-betweenness-blocks-sign-mixed.md`.

Scope (b); invariant = strict convexity + affineness. NOT claimed: that no third
family exists. Magnitude untouched. Composes with the existing
`the_pn_bond_is_an_average_and_cannot_be_extremal_probe`, which established the
ordering `L_pp < L_pn < L_nn`; this adds what it means for the `b_3 > 0` requirement
specifically, which that probe predates.

## 2026-09-12 — class D order-zero leg: the UIC per-block log measured (`qou-zlra`, PR #7230)

Row D of the escape enumeration asked whether any corpus functional outside the
product-additive class can carry the two-bond correlation a valley needs. #7223
closed the additive class by theorem; the ONE functional outside it was
`prop:unified-iterative-correction`'s per-block log, unmeasured because the
production call exceeded 300 s per atom.

Measured now, A = 3..8, every Z, k_exact = 4..9 (36 cells), proton pin,
convention D, mpmath end to end.

**It IS outside the additive class.** Third difference in Z nonzero in every
cell, GATED AND UNGATED alike — so the non-additivity is the per-block log
itself, not the Pass-2 selector. Mechanism proved sorry-free
(`QOU/Mass/UICPerBlockLogPairTerm.lean`): a two-branch block trace has
non-multiplicativity defect `wP*wM*(x-y)^2`, which under convention D is exactly
`wP(q)` and is INDEPENDENT OF BOTH BOND OFFSETS.

**Nothing comes through it.** No valley: argmax_Z does not track N=Z (it
coincides in only 3 of 36 cells, never at more than one tier per A -- it is not
true that it never lands there), sits at an endpoint in 15 of 36, and is not
converged in k_exact. The functional also has the wrong SIGN and the wrong
A-scaling before the Z-shape is reached. And the one FORCED fact points the wrong way — the
all-pairs symmetry curvature `L_pp + L_nn - 2 L_pn = +0.0435` is positive
(`symmetryCurvature_pos`, sorry-free, holds for every q > 1 given
`deltaPN_nonneg`), so the additive part makes the symmetric nucleus the LEAST
bound.

`qou-brng` STAYS OPEN (rule 13a): the extensive-term coefficient/mechanism is
untouched by this. What is closed is the order-zero leg of row D, and it closes
for a DIFFERENT reason than the additive class — the additive class cannot carry
a pair term at all, whereas this one can and does, but carries the wrong shape
and the wrong sign.

Note for whoever picks row D up: the UIC layout is the COMPLETE GRAPH
(`_step_chain_generic` crosses each nucleon with every previous one), which
`QOU.Mass.CoordinationSaturation.complete_graph_no_saturation` already refutes
on saturation grounds. So even a valley found here would have sat on an excluded
layout.

---
**2026-09-08 — TOOK OVER qou-qqm4's unanswered target and computed it. The answer is NO: the derived kind-dependent bond weight is real but FAR TOO WEAK.**

**Takeover.** `qou-qqm4` was `in-progress`, last updated `2026-09-07T11:13Z`, **16 h stale** against the 3 h threshold, with no response to the target posted on #7000 at 17:09Z. Owner instruction: *"take over — No ρ_pp yet."*

**Method — right-to-left, as the rule required.** `ρ_pp` computed **independently** from the corpus's own derived bond factors and then compared. Nothing inverted from `rMeasured`.

Inputs, both from the corpus: `bond_pn_kind_order_four_discriminator_probe.py`'s exact rational series in `ε = q−1` (`pp = z` exactly; `pn` = the `averaged_weighted` kind; `nn = z′`), and `CarrierCrossingQuantisation.rMeasured = 950815/1483044`. Seeded from `Q_50_DIGIT_STR`, **not** the float64 `q_parameter.Q` — the exact defect a sibling fixed in this cone on 2026-09-07 (`87bf88379`).

**Result — four identifications, and the PRINCIPLED one misses worst:**

| identification | ρ_pp | miss |
|---|---|---|
| A multiplicative `pp/pn` | 1.2056 | 26.5 % |
| **B additive `log pp / log pn`** | **0.7238** | **55.9 %** ← principled |
| C shifted additive | 1.1869 | 27.7 % |
| D inverse | 0.8295 | 49.5 % |

against `target = 1 + rMeasured = 1.64112393`. **B is the principled one** — the binding law is `B = E₀·log(tr ratio)`, so interface factors multiply in the trace and their *logs* add; an additive per-pair weight must be a log, not a ratio. Reporting A because it is closest would be selection against the target, which §NO FITTING names.

**And no carrier rescues it.** Scanning every `m_pp, m_pn ∈ 1..6` (³He = ppn → pairs pp, pn, pn): A's closest miss is **67.9 %** (*worse* than uniform's 55.98 %); B's is **30.2 %**, at `(m_pp, m_pn) = (2,1)`. That is reported as a **bound** — "even the best small carrier misses by 30 %" — not as a carrier determination; reading a carrier off the residual is the same fit one level down.

**Verdict: real structurally, insufficient quantitatively.** `kind_ratio_not_determined_by_sum` stands — a kind-dependent weight *does* break the integrality that made the exhaustion exhaustive. But the kind-dependence the corpus derives needs `ρ_pp ≈ 1.64` and delivers 0.72–1.21. The **sign** is right (`bond_pp > bond_pn`); the magnitude is roughly half what is needed under the most favourable reading and wrong-way under the principled one.

**What this does and does not change.** It does **not** restore `no_carrier_reproduces_b3` — that exclusion's premise is still derived-false, and #7097's re-scoping stands unaltered. What it removes is the hope that the *already-derived* kind-dependence closes the three-body gap. So `qou-brng`'s surviving route now needs a **further** source of per-pair variation beyond the bond kind, or the count channel is not where `b₃` lives.

Probe: `computations/probes/rho_pp_kind_weight_does_not_close_b3_probe.py`, 7/7, witness alongside.



2026-09-08 (owner): Avenue 2 sharpened — both derived edge sets on main are affine in A, and an affine count can never be a surface term, so the prior question is: what edge set has a BULK at all? Decide by a proved invariant, not a fit; a negative closes Avenue 2 outright. Claimed on branch claude/brng-avenue2-bulk-edge-set-2026-09-08.



2026-09-08 (Avenue 2 CLOSED over the encoding — branch claude/brng-avenue2-bulk-edge-set-2026-09-08). Invariant: LINEAR LAYOUT. atom_braid_word_3A emits every inter-nucleon letter at generator 3k+2, so the coordination graph of any word it can build (any ordering, any multiplicities) is a subgraph of the path on the ordering. Lean QOU/Mass/LinearLayoutNoBulk.lean (sorry-free, lean-direct exit 0): degree ≤ 2; |E| ≤ n; connected ⇒ the path, |E| = n−1, surface = 2; linearLayout_family_not_hasBulk. Probe linear_layout_no_bulk_probe.py 4/4: all 246 words A=2..8 × all orderings are the path (position-based AND strand-tracked); max-contact 3A−6, complete graph C(A,2) and the sub-affine true packing all violate |E| ≤ A and are inexpressible. Scope-(b): no edge set the encoding can express has a bulk. STILL OPEN (do not close this bean): the extensive term itself — a bulk needs either a different encoding with a DERIVED non-linear strand layout, or an extensive term that is not a coordination count; neither is derived, and choosing a layout to match the surface term would be selection against the target. Audit docs/audits/2026-09-08-linear-layout-no-bulk.md.



## 2026-09-13 (session #7155, main review after 425 commits) — Avenue 2 branch rebased; workplan adjusted

**State.** PR #7155 (Avenue 2: every expressible edge set is a linear layout ⇒ no bulk) was NOT merged; it sat conflicted on this bean file only. Rebased onto main c9fd78b0ad (union of both bean tails); the only dependency that moved on main is a docstring-only change to `mass_at_3A_proper.py` (qou-m6gp hyperbolic-branch note), so the probe premise is unchanged — re-run 4/4, witness byte-identical. Three documents on main already cite #7155's result as the current state of this bean (`2026-09-08-l2-1ppq-research-program-gaps.md` §2 lines 256/268, `2026-09-12-dominant-summand-extensive-test.md` line 116, cheat-sheet 9b currency block), while the Lean and probe are NOT on main — landing #7155 is the workplan priority for this front, so the citations resolve.

**What landed on main and how it bears here.** (i) The escape enumeration (PR #7181, classes A–D) and its decisions — class C multiplicity sub-extensive (b), class B escapes invariant (2) not (1) (#7204), pn-averaging narrows class B (#7234), class D order-zero leg measured (#7230), dominant-summand channel none/anti-binding at A ≤ 7 (#7200, #7211), Ursell b₃ < 0 for every bond triple (#7198). None is an edge-set question inside the encoding; none contradicts or supersedes Avenue 2. The live remainder (classes B and D) lies outside what a coordination-graph invariant can decide. (ii) **Owner ruling qou-ales (2026-09-08): braid words are to be SELECTED by γγ production + confinement SDP at q₀, no census** (steps 1–10 landed). This is the one landing that touches Avenue 2's SCOPE: the invariant was measured on the template encoding `atom_braid_word_3A`. Structural note, not yet proved: a γγ vertex `σᵢσᵢ₊₁⁻¹` acts on strand positions i, i+1, i+2, which on the 3A-strand block line lie in at most two CONSECUTIVE blocks, so the position-based linear-layout invariant holds for every γγ-produced word on that line as well — `card_edgeFinset_le` and `linearLayout_family_not_hasBulk` apply unchanged. What does NOT transfer automatically is the strand-tracked graph: the template's vertices never migrate a strand across two interfaces (measured, 42/42 words); a γγ-selected word with vertices straddling interfaces could. **New workplan item:** once qou-ales produces selected atom words (step 2 admissibility per nucleus), measure the strand-tracked coordination graph on them and, if linear, state the γγ extension in Lean (a vertex touches ≤ 2 consecutive blocks). Until then Avenue 2 is closed over the template encoding only, as stated.

**Untouched fronts still mine:** qou-gr3t (InteriorMarkov from the Hecke tower; #7153 reports TowerSpan proved from the braid relations — the missing piece), qou-d0qq steps 3–5, qou-8uxw, qou-denm (Kohno 1987 ingestion). No sibling appended to any of them since 2026-09-07.



2026-09-13: PR #7155 (Avenue 2 — every expressible edge set is a linear layout; a linear layout has no bulk) MERGED to main by rebase (owner: "go"), merge sha 47cbb3153750d1b40d7571a13dad93622a2f66a5. The three main citations of #7155 now resolve. Bean stays OPEN (classes B and D; the γγ-selected-word strand-tracked follow-up).


## 2026-09-12 — one more selection principle excluded, structurally (qou-8urh, PR #7251)

This bean's open target is the linking-vs-self-energy amplitude assignment — why
the binding multiplier is the mutual (coordination) linking count. A candidate
that keeps getting reached for is the operator-selection LP's dual: its active
set `{lambda : y_lambda* > 0}` looks like exactly the "which blocks does the
bound state saturate" object this bean wants. **It cannot be, and the reason is
structural rather than numerical.**

Wedderburn block projectors are orthogonal idempotents, so the Frobenius Gram on
the block basis is diagonal by construction,
`G_{lm} = tr_M(P_l P_m) = delta_{lm} tr_M(P_l)`. Complementary slackness then
decouples to `s_l * G_ll * x_l = 0`
(`QOU.MassTheory.UICGateLP.complementarySlackness_diagonal_iff`, sorry-free) —
a condition on the multipliers, the block norms and the SELECTED operator's
coefficients, in which the atom's own traces never appear. The LP's
discriminating power lives entirely in the OFF-diagonal Gram (operator overlap),
and an orthogonal basis has none.

Measured confirmation, two independent routes:

* `computations/probes/h6_block_selection_lp_probe.py` (pre-existing, H_6): the
  active set is never fewer than 10 of 11 at any reachable target; a controlled
  diagnostic changing only `G` gives 5-of-6 active for `G = diag(t)` against
  3-of-6 for a dense PSD `G`.
* `computations/probes/uic_gate_vs_lp_complementary_slackness_probe.py` (new,
  the k <= 4 blocks at 2H and 4He, mp.dps = 70, proton pin, convention D):
  active 9 of 10 at every target for both atoms.

**Scope (b) structural exclusion**; invariant = orthogonality of the Wedderburn
projectors. Holds for every n, q and trace convention.

**What it does NOT exclude**, and this is the live direction: a **non-orthogonal**
operator basis. Actual braid sub-words overlap, so their Gram is dense and the LP
recovers discriminating power. That is the natural next thing to try for this
bean, and nothing here touches it.

**One measured contrast worth having.** The NF-basis degeneracy (optimal value
identically 0, `y_0* = 0`, `y_0_eq_zero_of_radical`) does **NOT** transfer to the
block instance — it needs the cost vector to be a row of the Gram, which holds
for the identity-containing NF basis and fails for a diagonal one. Measured
`y_0* = 0.0347` (2H) and `0.0130` (4He). Do not quote "the LP's y_0* is zero"
without naming the basis.

Audit: `docs/audits/2026-09-12-uic-gate-primal-lp-hunt.md`. Stays OPEN.



## 2026-09-12 — note from the UIC functional resolution (PR #7237, bean `qou-t6be`)

Not a step on this bean's open problem; recorded because it changes what a reader
of `unified_iterative_correction`'s output is looking at.

Under the owner's ruling *"resolve functionals ... what lean provable"*,
`prop:unified-iterative-correction` was restated to match the producer: the
q-Laplacian resolvent `rho_lambda(s_*)` the block omitted is now in the formula,
`u_lambda` is stated as the closed form rather than as an "LP shadow price"
(refuted on both available readings), and the summation range is stated as the
gated set rather than "strictly over all lambda". **No producer changed and no
number moved.**

**What this bean should take from it.** The gate — Pass 2's restriction to
`tr M_lambda <= 0` — is now marked in the corpus as **asserted, not derived**,
with the disproof cited: genuine complementary slackness for `<Phi, pi> >= 0`
makes "tight" mean `tr = 0`, under which the functional collapses to
`(sum c_lambda) * f(0)` and reads NOTHING about the atom
(`QOU.MassTheory.UICFunctionalSelection.uicGated_cs_eq`, sorry-free); measured,
0 of 10 active blocks sit at `tr = 0`. Combined with `y_0_eq_zero_of_radical`
(the LP prices nothing), the gate has no derivation at all.

That matters here because `uic_sign_forced_by_gate_probe` already showed the
gate FORCES `B < 0` for any nucleus and explains the measured A-independence. So
the wrong-signed, A-independent binding that this bean's extensive-term frontier
is trying to explain is, to that extent, a property of an **undefended selection
rule** rather than of the nucleus. Whether to keep the gate is an owner call and
was deliberately NOT taken in #7237 — dropping it moves every binding number by
3.4-4.6x on an argument that only refutes a justification (scope-(a), not
scope-(b)).

**This bean stays OPEN.**

Audit: `docs/audits/2026-09-12-uic-functional-resolution.md`.

**Cross-reference.** The 2026-09-12 note above (PR #7237) reports that
`y_0_eq_zero_of_radical` makes the LP "price nothing" and that the Pass-2 gate has
no derivation. That is the same LP reached from the **dual** side; the entry below
reaches it from the **active-set** side. Neither subsumes the other — `y_0*` is the
net-constraint shadow price and the active set is `{i : y_i* > 0}` — but together
they leave the operator-selection LP with no surviving route to a binding
multiplier.

## 2026-09-14 — the non-orthogonal escape does not exist; |active| is pinned by a DIMENSION COUNT

The 2026-09-12 entry above named a live direction: *"a **non-orthogonal**
operator basis. Actual braid sub-words overlap, so their Gram is dense and the LP
recovers discriminating power. That is the natural next thing to try for this
bean, and nothing here touches it."*

**It is not there.** The active-set cardinality is `d - 1` whatever the Gram.

**Lean** (sorry-free, `lean`-direct exit 0, `#print axioms` = propext /
Classical.choice / Quot.sound only):
`QOU/MassTheory/LPActiveSetDimension.lean` — `exists_slack`,
`tightSetCard_lt`, `activeSetCard_lt`, `activeSetCard_le_pred`.

Complementary slackness gives `(G x*)_i = ⟨e_i, Φ*⟩_F` with `Φ* = Σ_j x*_j e_j`,
so an active index is a basis element Frobenius-orthogonal to the selected
operator. Then

| | |
|---|---|
| **upper** | `G` invertible, `n_target ≠ 0` ⇒ at most `d−1` tight. All `d` tight ⇒ `Gx = 0` ⇒ `x = 0` ⇒ `1ᵀx = 0 ≠ n_target`. |
| **lower** | a basic optimum needs `d` independent active constraints; the equality gives 1, the box gives 0 at an interior optimum, so `d−1` come from `Gx ≥ 0`. |

`activeSetCard_lt`'s **statement** is the finding: it mentions neither the cost
vector `t`, nor `n_target` beyond its non-vanishing, nor any property of `G`
beyond invertibility — **in particular not its sparsity**. The active set counts
the **basis**, not the nucleus. A binding multiplier must depend on the nucleus.

**Measured** (`computations/probes/lp_active_set_is_pinned_by_dimension_probe.py`,
all assertions pass). Corpus-derived non-orthogonal basis, no new Markov traces:
`e_S := Σ_{l∈S} P_l` over cyclic windows of the H₆ blocks, so
`⟨e_S,e_T⟩ = Σ_{l∈S∩T} tr_M(P_l)`. Off-diagonal fraction **0.000 → 1.000**, rank
11 of 11 throughout, every duality gap `< 1e-20`, and `|active| = 10 = d−1` at
every window width and every target.

**The two escapes are the two degenerate cases, and the corpus is in both** —
singular `G` (kernel, but the operators are then not a basis: production
interface templates, **rank 6 of 11**) and indefinite `G` (LP unbounded, box
corner: the braid sub-word basis, eigenvalues `[-1.579, -1.140, 0.441, 8.43, …]`).
So `h6_block_selection_lp_probe.py` **already tried the sub-word basis and
RETRACTED it** (2026-08-16) as a box artifact — the "nothing here touches it"
above is stale against the very file that entry cites as independent confirmation.

### 🛑 A number in the entry above should not be quoted

It reports *"a controlled diagnostic changing only `G` gives 5-of-6 active for
`G = diag(t)` against 3-of-6 for a dense PSD `G`"* and reads the 3 as the dense
Gram recovering discriminating power. Reproduced exactly (same seed 7, same
matrices, `h6_block_selection_lp_probe.py:145-150`), **the 3-of-6 solve is
invalid**:

    max|x*|     = 3.7135e+06   against M_bound = 1e6
    primal_obj  = -357264      for a MAXIMisation
    duality_gap = 3.5726e+05   where well-posed solves give < 1e-20

It is the same box artifact that file retracts one screen below; the retraction
was applied to the sub-word half and not to the controlled-diagnostic half. A
well-posed dense PSD instance gives **5 = d−1**, like everything else.

**Scope (b)** structural exclusion; invariant = invertibility of the Gram plus a
non-zero net constraint; over any field, so every `n`, `q` and trace convention.

**NOT touched, and still this bean's real target:** the extensive term itself
(a bulk, not a surface); the LP's optimal **value** and `y_0*` (this is about the
active set only); the γγ-selected-word strand-tracked follow-up (blocked on
`qou-ales` step 2); escape classes B and D of PR #7181. **Bean stays OPEN.**



## 2026-09-14 — class B: the AVERAGING escape is closed at the corpus's own `δ`

The 2026-09-12 entry narrowed class B's remaining escape to two hypotheses —
break the **averaging** of the pn letter, or break **affineness** of the
interface law — and noted *"neither mentions a numerical value"*.

`pn_betweenness_blocks_signMixed` carries the averaging half under
`-2 < δ < 2`, the range on which `corpusWeight δ = 1/2 + δ/4` is a strict convex
weight. Read as a Lean hypothesis, that looks like something a third bond family
might violate. **It is not an assumption — `δ` is derived, and lands three orders
of magnitude inside.**

| | |
|---|---|
| `δ(q₀)` | `0.00137571080703` |
| `2 / δ(q₀)` | **1453.7939** — factor inside the range |
| `δ(q) = 2` at | `q = 3.458099300`, i.e. **3.115×** the substrate modulus |
| sign | `δ > 0` for every `q > 1`, so `w > 1/2` always — never near either end of `(0,1)` |

**Identification checked, not assumed** (two `delta` across two layers is the
`da-arity-conflation` trap). Derived symbolically, exact:

- `z(1/q) − (z − h) = 0`, so `f_nn = z − h` (the constants' `fNN_eq_fPP_bar`);
- `w·f_pp + (1−w)·f_nn − (z − h(1/2 − δ/4)) = 0` with `w = 1/2 + δ/4`;
- `δ − ħ_q²·h_q·[2]_q/3 = 0`, the docstring's alternative spelling.

So `pyhecke.constants`' `eps = δ/4` convention (canonical `bring_color_weighted`,
owner ruling R3) **is** the Lean's `corpusWeight`. Cross-checked:
`pn_interface_offset(q0)` matches `−h(1−δ/2)/2` to **0.0** at 70 dps.

**Consequence: affineness of `μ = z + d` is the sole surviving class-B
hypothesis.** Untouched here.

Scope (b) for the averaging half — it discharges an existing sorry-free theorem's
hypothesis from a derived quantity rather than assuming it. **NOT claimed:** that
no third bond family exists, that class B is excluded, or anything about
**magnitude** — *"what derived object puts `b_pn` more than 5× below both
like-species bonds"* is untouched and is still this bean's real target.

Probe: `computations/probes/pn_averaging_weight_is_derived_probe.py`, all
assertions pass, 70 dps, proton pin, convention D, no float64.



## 2026-09-14 — class B: multiplicity BREAKS affineness, and still cannot make pn extremal

The affineness half of class B's remaining escape. **The escape is real. It does
not deliver.**

**The escape exists.** Affineness is an `m = 1` fact. `tr(σ_g + d·I) = z + d` is
affine, but `(σ_g + d·I)^m` has trace of **degree `m`** in `d` — already
`(d²+1) + (2d+h)z` at `m = 2`, verified symbolically. Measured, **betweenness
itself fails from `m = 12`.** So `pn_betweenness_blocks_signMixed`'s hypothesis is
genuinely breakable, which is what the 2026-09-12 entry said class B needs.

**It breaks the wrong way.** Diagonalising, `σ_g` has Hecke eigenvalues `q` and
`−q⁻¹`, so `F_m(d) = w₊(d+q)^m + w₋(d−q⁻¹)^m` with `w₊+w₋ = 1`, and
`F_m′ = m·F_{m−1}` — monotonicity in `d`, hence betweenness, survives exactly
while `F_{m−1} > 0`. That stops at `m = 7` (`F_7(d_nn) < 0`). But the `b₃ > 0`
pattern needs `μ_pn` to be the strict **MAXIMUM**, and it is at **no `m` in
1..200**; betweenness breaks by pn becoming the strict **minimum**.

**Why — the invariant.** The pn letter sits at the spectral **balance point**. At
`d = −h/2` exactly, `(d+q) + (d−q⁻¹) = 0`: the two eigenvalue magnitudes coincide
at `[2]_q/2`. The corpus's `bring_color_weighted` letter is displaced from it by
exactly `h·δ/4 = 7.190163e-05` — the number `pyhecke/constants.py` records in its
own convention note. So

| letter | `d` | spectral radius |
|---|---|---|
| pp | `0` | `q` |
| nn | `−h` | `q` |
| pn | `≈ −h/2` | `≈ [2]_q/2` |

and **AM-GM** gives `q > [2]_q/2 > 1` for every `q > 1`. Measured growth rates at
`m = 200`: **1.10840** (pp), **1.00549** (pn), **1.10225** (nn), against
`q = 1.10998` and `[2]_q/2 = 1.00545`.

The gap is closed-form: `q/([2]_q/2) = 2q²/(q²+1) = 1 + tanh(ln q)` — exactly
**`1 + δ_CP`**, the crossing discriminant `qou-hjs8` proved θ-free and
`QOU.Braiding.em_strong_ratio_tanh` already carries.

**Lean** `QOU/MassTheory/PnBalancePointSpectralGap.lean`, 7 declarations,
sorry-free, `lean`-direct exit 0, `#print axioms` = propext / Classical.choice /
Quot.sound only.

**Scope (b)** asymptotically; invariant = AM-GM on the two Hecke eigenvalues,
which mentions no numerical value. Small-`m` is **measured** (1..200), not proved.

**NOT excluded:** a derived pn letter **not** at the balance point. That is now
the whole of class B's remaining room, and it is far narrower than "break
affineness" — the displacement from balance is `7.19e-05`, and it would have to
move `ρ_pn` above `q`. **Untouched: MAGNITUDE** (this bean's real target), class D,
and the extensive term. **Bean stays OPEN.**
## 2026-09-14 — the MAGNITUDE: the "4.0× short" headline is quoted at an inexpressible degree

This bean's magnitude question is calibrated against `a_A^eff = 5.963 MeV` vs the
SEMF's `23.7`, i.e. **4.0× short** — the figure AGENTS.md quotes. **It is
evaluated at `k = 12`.**

`qbeta_class_b_nonsigndefinite_bond_probe` computes
`a_A^eff(k,m) = E₀·δ(m)·k/4`, and its own constant reads
`K_DEGREES = (2, 12)  # chain and close-packed`.
`QOU.Mass.LinearLayoutNoBulk` (sorry-free, merged **PR #7155**) proves the
encoding **cannot express degree 12** — its docstring names the case: *"the
max-contact packing (degree up to 12) and the complete graph (degree `n−1`) are
not linear-layout graphs"*. `atom_braid_word_3A` emits every inter-nucleon letter
at generator `3k+2`, so any word it builds has a **path** coordination graph,
`k ≤ 2`.

**Neither the probe nor R5/R8/R9 mentions `LinearLayout`** (grep: zero hits in
the probe). Both results are on `main` and have never been composed.

**Measured** — same bond factors, same formula, only `k` differs:

| | `a_A^eff` | vs SEMF 23.7 |
|---|---|---|
| quoted, `k = 12` (close-packed, **not expressible**) | 5.962911209 MeV | **3.97457×** short |
| expressible, `k = 2` (the chain the encoding emits) | 0.9938185348 MeV | **23.8474×** short |

exactly the degree ratio `12/2 = 6` (asserted to 1e-30). The R5 cells reproduce
the recorded 0.441 / 2.647 MeV, so the formula is untouched.

**And the m-scan is not available as a selection** — R9 reports the whole
`m = 1..12` table precisely because picking the maximising `m` is the
discrete-parameter fit the NO FITTING directive names. At the canonical `m = 1`
and expressible `k = 2` the derived law gives **−0.045993397 MeV**: negative, the
wrong SEMF sign, before magnitude is reached at all. **So at the encoding's own
layout and canonical multiplicity the gap is not a shortfall — it is a SIGN
failure, and the magnitude question arises only on cells the layout result
excludes.**

### A correction I made and retracted inside the session

I first read `E₀·δ·k/4` as substituting the degree `k` into
`symmetryCoeff = energySlope·μ/4`'s **mixing** parameter `μ`, reconstructed
`μ ≤ 2k/A` from `bondSum_wellMixed`'s own non-negativity, and concluded the cap
was understated 2×. **Wrong.** `SymmetrySignAmGm.lean` states the well-mixed
assignment as `E_pn ≈ 2E·ZN/A²`, i.e. `μ = k/A` — the **value**, where I used a
**bound** 2× looser; with `μ = k/A` the SEMF's own `1/A` cancels it and the
probe's formula is exactly right. The retracted claim flattered the framework;
the surviving one does not.

### Inherited scope limit — load-bearing

`LinearLayoutNoBulk` is closed over the **template** encoding
`atom_braid_word_3A` only. The γγ-selected words of owner ruling `qou-ales` have
**not** been measured strand-tracked, and that is this bean's existing open
workplan item. If such a word expresses a higher degree, the 4.0× could return.

**Scope: a correction to a quoted figure.** No derivation, bond factor or formula
changes. It makes the gap **wider**. NOT claimed: that `k = 2` is the right
physical model (`bondSum_wellMixed` is a mean-field model by its own docstring
and a chain is not well-mixed); that the magnitude is closed, narrowed or
reopened; that any bond family is excluded. **Bean stays OPEN.**

Probe: `computations/qbeta/qbeta_magnitude_at_the_expressible_degree_probe.py`.


## The amplitude: what is proved, what is open, where it enters (2026-09-14)

Answering the owner's question — *"what are properties/constraints of amplitude?
where is it emerging in canonical derivation/cheat sheet for mass/binding?"* —
as a consolidation of corpus facts. No new derivation; every line below cites an
existing sorry-free file or an owner ruling.

### There are TWO amplitudes, and the whole bean is about their assignment

At fixed hyperbolic volume (`BindingMassRung.lean:8-9`):

    mass    :  m(K) = m_e · Vol(K) · lw / hbar_q^2      lw = SELF-linking weight
    binding :  B(K) = m_e · Vol(K) · M                  M  = MUTUAL coordination count

`lw` is the density factor of step **9a**; `M` is the multiplicity of step **9b**.
Vol(K) is common to both — the amplitude is the *density* half, not the geometry.

### Properties, each with its carrier

| property | mass amplitude `lw` | binding amplitude `M` | carrier |
|---|---|---|---|
| bar parity | **even** (cosh / signed channel) | **odd** (sinh / count channel) | `BrunnianBindingChannel` |
| type | q-dimension, rational in q | bare integer count | ibid. (open item ii) |
| sign | writhe, sign-changing | unsigned, non-negative | ibid. |
| order in hbar_q | O(hbar^-2) — order-2 pole, residue `lw` | O(1) | `BindingMassRung` |
| classical limit q->1 | `lw(1) = 5/2` finite nonzero => pole genuine | A-dependent integer | `MuWenzlClosure` |
| closed form at the proton | `(3q^2+4+3q^-2)/4 = 5/2 + (3/4)h^2` | `M_n = n-1` (chain) | `MassVolDensity`, `LinearChainBondCount` |
| degree bound | — | `deg <= 2` (no bulk); complete graph excluded | `LinearLayoutNoBulk`, `CoordinationSaturation` |

### The assignment is FORCED, not postulated — three sorry-free results

1. **Partition is a theorem.** Every crossing is intra- or inter-component, so
   assembly = self + mutual exactly; with `B := sum(isolated) - assembled` the self
   energies cancel and `binding_eq_neg_mutualEnergy` gives `B = -(mutual)`.
   Falsifiable corollary `binding_indep_of_self`: binding depends on NO self-crossing.
   (`SelfMutualPartition`)
2. **Parity picks the channel.** `signed = (n+ - n-)(q+q^-1)/2` (writhe = 2 lk),
   `unsigned = (n+ + n-)(q-q^-1)/2` (count). The 3He/4He carrier L6a4 is **Brunnian**:
   every pairwise lk is 0, so `n+ = n-` and the signed channel is EMPTY. Binding must
   therefore ride the unsigned count channel — which is why `M` is a count and not a
   linking number. (`BrunnianBindingChannel`)
3. **The bar-odd shape is unique.** The bar-odd part is free rank one over the
   bar-even, generated by `h = q - q^-1`. The `h` prefactor of the count channel is
   not a choice. (`BarParityRankOne.isBarOdd_iff`)

### The rung dichotomy, exactly

    massMultiplier_pole_residue :  hbar^2 * (lw/hbar^2) = lw
    bindingOverMass_eq          :  B/m = (M/lw) * hbar_q^2
    bindingOverMass_tendsto_zero:  B/m -> 0  as hbar_q -> 0

So mass DIVERGES and binding VANISHES at the classical point: rest mass is generated
by the deformation being small; nuclear binding is an O(hbar_q^2) quantum correction.

Numerics at the proton pin, mp.dps = 50 (recomputed 2026-09-14):

    q0        = 1.1099785827513808076
    h         = 0.20906029879563931545
    hbar_q    = 0.099081716044258507846
    hbar_q^2  = 0.0098171864542750738119
    lw_A(q0)  = 2.5327796563993914921
    lw/hbar^2 = 257.99445372624517683

    (M/lw)*hbar^2 :  M=1 -> 3.87605e-3   M=2 -> 7.75210e-3   M=3 -> 1.16282e-2
    AME B/m       :  d 1.18605e-3        4He 7.59130e-3      56Fe 9.45010e-3

**FLAG, not a finding.** M=2 lands 2.1 % from 4He's AME B/m. That is NOT evidence:
no derived rule gives M=2 for 4He (the arc's own z = A-1 gives 3, and
`CoordinationSaturation` excludes the complete graph that produces it). Choosing M
because it lands is selection against the target — AGENTS.md NO FITTING. Coincidence
until a rule derives it; recorded here so the next agent does not rediscover it and
mistake it for a result.

### What the corpus already REFUTED about `lw`

`lw = lambda_A` is **excised for absolute mass** (owner ruling 2026-06-24). The form
`m(K) = m_e Vol(K) lw/hbar_q^2` read at K = B_3 gives m_p ~ 966 MeV (+2.96 %), and the
long-quoted "+2.89-3.86 % absolute-mass gap" is the **lambda_A fit artifact**, not a
missing wire-up (`2026-06-24-lambda-a-refutation-artifact-audit.md`). Absolute mass is
excised as a prediction entirely (2026-08-11). What survives:
* the ALGEBRAIC identity `lw = (1/4) sum_{lam |- 4} dim_q V_lam` (proved) — `lw` is a
  derived object;
* `vol_density_per_block` for **binding ratios only**, where the scale cancels.

So the mass amplitude is derived as algebra and refuted as an absolute-mass amplitude.
Its live role is the ratio.

### The three open residuals, in the sources' own words

* `BindingMassRung`: *"It does NOT derive **why** binding lacks the cusp factor — that
  residual kernel is the open item."*  (Why does 1/hbar_q^2 attach to the self channel
  and not the mutual one? CAL-2 puts it in `m_mu/m_e = Vol(4_1)/hbar_q^2`; nothing
  derives that the mutual channel escapes it.)
* `BrunnianBindingChannel`: *"(i) the exact map from `n+ + n-` to the graph-degree
  `z = A-1`; (ii) why the surviving count channel enters as a **bare integer** while
  the self/mass channel keeps the full q-dimension self-trace `lw`."*
* `SelfMutualPartition`: *"the identification of the substrate mass observable with this
  crossing energy at the full Markov-trace granularity ... its lift to the exact mass
  formula is the remaining modelling step, not a fit."*

(ii) and the `BindingMassRung` item are the SAME question from two sides: integer vs
q-dimension is exactly cusp-factor-absent vs cusp-factor-present. That is this bean.

### Magnitude, the other half — where it currently stands

The binding amplitude's magnitude is capped by `delta <= 2 ln q0 = 0.2086814406` with
`a_A^eff = E0 * delta * k / 4`. At the only degree the layout can express (`k = 2`, the
chain, `LinearLayoutNoBulk` degree <= 2) this gives **0.9938185348 MeV against the SEMF
`a_A = 23.7 MeV` — 23.8474x short**, and at the canonical multiplicity m = 1 the sign is
wrong (-0.045993397 MeV). PR #7373.

So the amplitude's ASSIGNMENT is forced and proved; its MAGNITUDE is short by 23.8x at
the expressible degree. Those are the two halves of this bean, and only the first is done.
## 2026-09-14 — the ideal-Fermi-gas lead, evaluated and NEGATIVE

A corpus-grep sweep of this front surfaced the one lead with **no corpus
trace**, from `library/arxiv-nucl-th-0507064v2` (Horowitz–Schwenk, low-density
neutron matter): *"for the ideal Fermi gas `b^(3)_n = 3^{-5/2} = 0.06`"* —
positive, from exchange statistics alone, with **no pair interaction at all**.
Since every corpus mechanism for `b₃` is a bond object and
`b3corpus_chain_pos_iff` is a statement about bond factors, a degeneracy
contribution is invisible to it. It looked like a live escape.

**It is not, and the reason is worth more than the lead: the two `b₃` are in
opposite sign conventions.** Derived in
`computations/audits/b3_ideal_fermi_gas_lead_evaluation_probe.py` (8/8):

- the classical cluster integral is `b₃^cluster ∝ +∫φᵀ₃`, so it carries the
  sign of `+φᵀ₃`;
- the corpus defines `b₃^corpus = −φᵀ₃` (the minus is what makes `b₃ > 0` mean
  binding-increasing when binding is `−α·log μ`);
- hence `sign(b₃^corpus) = −sign(b₃^cluster)`, identically.

So the ideal gas's `+0.064` maps to **negative** in corpus convention — the
same sign the corpus already has, and the same sign that blocks this front.

**And the anomaly dissolves entirely.** A classical gas with purely
**repulsive** pair interaction also has `b₃^cluster > 0`, because that *is* the
Ursell alternation. The ideal Fermi gas does not carry an unusual sign in its
own convention; it carries the ordinary one. There was never a sign anomaly to
exploit — there was a convention difference.

### What survives, narrowly

In the corpus frame the free case (`μ_e = 1`) gives `b₃ = 0` **exactly** over
ℚ, while a free Fermi gas does not. That is a concrete, physically-realised
witness that the **non-Mayer escape class is non-empty** — the one route the
2026-09-12 Ursell audit lists as explicitly scope-(a) un-excluded. It is a
witness that the class is non-empty. It is **not** a mechanism, **not** a sign,
and **not** a magnitude.

And it cuts against itself: exchange statistics in this framework **are** the
Hecke algebra (`H_n(q)` is the q-deformation of `S_n`, and the statistics
content already sits inside `tr_M = Σ_λ y_λ χ^λ`), so this is **class C**,
already attacked on two channels — multiplicity (sub-extensive, scope (b)) and
dominant summand (wrong sign at `A ≥ 5`, scope (a)). Whether the ideal-gas
analogue is a *third* class-C channel is open and is not settled.

**Recommendation, marked as judgement:** do not spend a tranche here. Recorded
as evaluated-and-negative so the next agent who greps `nucl-th-0507064` does
not re-open it. The two routes the same sweep found genuinely live are
unchanged — the γγ-selected word's **strand-tracked** coordination graph
(blocked on `qou-ales` step 2) and `qou-2ss0`'s **superlinearity** question.

Section 1 of the probe also re-derives the corpus identity exactly over ℚ:
`Δ³W = +φᵀ₃`, collapsing on a chain to `g₀₁·g₁₂`, matching `b3corpus_chain`.

PR #7375. `mpmath` dps 60 + `Fraction`; no float anywhere.

### Cross-link (2026-10-11)

the p-n interface factor's canonicity is conditional — `pn_averaging_unique` is sorry-free but carries `BarInvariant` as an instance hypothesis, which the canonical convention fails. Record: [`2026-10-11-atom-word-provenance.md`](../../docs/audits/2026-10-11-atom-word-provenance.md).

## 2026-11-15 — salvage of three stalled PRs onto today's main (#7407, #6358, #7216)

Owner pick on the qou-brng card (2026-11-15 11:33Z): "Both, salvage then Lean".
The three PRs sat 2587–6621 commits behind main and two conflicted, so their
files are carried onto one branch from main and each claim re-run there. The
claims are the PRs' own, unchanged; this note records only the re-verification.

- **#7407** — `computations/probes/bar_anomaly_of_the_two_amplitudes_probe.py`
  (sympy, exact). Re-run on main: **12/12**. Survives as stated in its own
  body: ω(1/ħ_q²) = q² matches the Ocneanu framing quantum a_N = q^N at N = 2
  and no other N, plus the naming bridge between `markovZ_bar_weight` (q⁻⁴) and
  `markov_framing_ratio_eq` (a² = q⁴). Its four retractions R1–R4 stand; every
  cited corpus site still exists (now under `folio/`). Residual (ii) is NOT
  closed by it.
- **#6358** — `computations/probes/nf_bond_count_injectivity_probe.py` +
  witness (exact, `Fraction`). Re-run on main: 222 configurations, **0
  normal-form collisions** against 115 grade-shape collisions; 4/4 witness
  assertions. Scope-(a) positive on the swept sample, not a proof of
  injectivity. The committed witness is kept as authored (a re-run here
  recorded a thinner environment block, so it was not substituted).
- **#7216** — `QOU/Hecke/BondCutSymmetryFibreTower.lean` and
  `…FibreTowerBound.lean`, moved from `content/` to `folio/` unchanged, plus
  `computations/qbeta/qbeta_class_d_fibre_tower_probe.py`.
  `lean-direct-cone.sh QOU.Hecke.BondCutSymmetryFibreTowerBound -B`: 4/4
  modules rebuilt from source, exit 0; `#print axioms` on all 28 theorems:
  ⊆ {propext, Classical.choice, Quot.sound}, no sorryAx. Probe: **28/28**.
  Class D (fibre tower / higher q-order) is NOT an independent escape from the
  bond-count caps (scope-(b) for the shape statement, by the ring-map
  transfer); the SEMF inequality a_V < a_A enters the Lean only as a
  hypothesis, never as a number.

The bean stays OPEN. Next on this front: the γγ-vertex lemma recorded above
(a vertex σᵢσᵢ₊₁⁻¹ touches ≤ 2 consecutive blocks, so LinearLayoutNoBulk
extends to γγ-selected words).

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.



## 2026-11-17 sibling sweep
Residual (ii) work in CuspFactorBarAnomaly.lean from a sibling session. Left: verify, decide whether it closes residual (ii).
Recorded 2026-11-17 from the stale-sibling-session sweep (table: /mnt/project-files/qou-sibling-consolidation/table.md). Source session archived; work not lost.

## 2026-11-19 — #7418 ported as #8522

PR #7418 (single-crossing chain factorizes; R12 reduces the b₃ cross term to `TowerSpan`) was 2311 commits behind main and is closed as superseded by #8522, which carries its Lean file, two probes and audit onto main. Re-verified there: lean-direct exit 0, 18 theorems with no sorryAx, both probes 6/6. A scope note marks R11 as measured on the superseded `atom_braid_word_3A`. Residual (ii) is unchanged and still open; the bean stays open.
