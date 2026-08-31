---
# qou-brng
title: 'OPEN KERNEL: derive that the saturated nuclear binding fraction = ℏ_q² (mass/binding rung)'
status: todo
type: task
priority: normal
created_at: 2026-08-21T15:05:00Z
updated_at: 2026-08-31T10:40:36Z
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
