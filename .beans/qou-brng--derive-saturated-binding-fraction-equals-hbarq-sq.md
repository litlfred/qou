---
# qou-brng
title: 'OPEN KERNEL: derive that the saturated nuclear binding fraction = ℏ_q² (mass/binding rung)'
status: todo
type: task
priority: normal
created_at: 2026-08-21T15:05:00Z
updated_at: 2026-09-03T04:57:24Z
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

    LP="$PWD/content/quantum-observable-universe/lean/.lake/build/lib/lean"
    for p in mathlib batteries aesop Qq proofwidgets importGraph plausible \
             LeanSearchClient; do
      LP="$LP:$PWD/.lake/packages/$p/.lake/build/lib/lean"
    done
    LEAN_PATH="$LP" lean \
      content/quantum-observable-universe/lean/QOU/SchurWeyl/OcneanuWeight.lean

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
