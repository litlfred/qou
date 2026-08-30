---
# qou-brng
title: 'OPEN KERNEL: derive that the saturated nuclear binding fraction = ℏ_q² (mass/binding rung)'
status: todo
type: task
priority: normal
created_at: 2026-08-21T15:05:00Z
updated_at: 2026-08-30T15:52:00Z
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
