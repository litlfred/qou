---
# qou-91w7
title: 'OWNER CALL: global reading of def:mass-energy (c_q^2 converts mass to energy, or pure number); E0 pole'
status: in-progress
type: task
priority: normal
created_at: 2026-11-22T10:47:45Z
updated_at: 2026-11-25T01:16:31Z
parent: qou-wxhi
---

FINDING 2026-11-22 (thread "Make the n-p gap vanish at q = 1", issue #9002, audit docs/audits/2026-11-22-np-gap-at-q-one-unit-map.md s5, commit 3e8ff68c7; relayed to the n-p cell thread):
E0 = m_e c_q^2 hbar_q has a pole at q = 1. Whether that pole is a defect depends on ONE global reading of def:mass-energy (E = m c_q^2):
- (A) c_q^2 converts mass to energy. Then every E0-scaled MeV row is an energy compared with a CODATA mass and must be divided by c_q^2 ~ 82.68 at q0: the n-p cell becomes 2 m_e hbar_q ln q = 0.01057 MeV (vanishes at q = 1, -99.18 % vs 1.29333), the beta-vertex budgets become 0.00508 MeV (placement B) and 0.00946 MeV (placement C), and Q_beta, the z_D cell and binding all land near -99 %.
- (B) c_q^2 is a pure number (experiment uses c = 1). Nothing is mixed; current rows and budgets stand; the q = 1 pole stays.
Reading (A) clashes with the q0 pin: CAL-2 (m_mu/m_e = Vol(4_1)/hbar_q^2) and the proton pin both put 1/hbar_q^2 = q^2 c_q^2 inside dimensionless mass ratios.
DEFAULT: (B) until the owner decides. OWNER DECISION needed. No code or content changes yet.



2026-11-22 PIPELINE TRACE (n-p cell thread, owner asked to talk it through the canonical chain):
- Steps 1-8 (R-matrix action, Stokes -> Hecke quadratic, Markov trace, Wedderburn, Frobenius pairing, weight-space/GB-NF): every object is in Q(q). No unit and no c_q appears. categorical-lagrangian.md has no c_q or hbar_q.
- def:information-speed-of-light: c_q := q^-1/hbar_q = 1/(q-1). It is a RATIO OF TWO COUPLING WEIGHTS, so an element of Q(q), dimensionless as defined. The prose calls it 'not set to 1', a Lieb-Robinson velocity.
- def:mass-energy: E(beta) = m(beta) c_q^2 with m(beta) = framing-corrected |tr_M| in R (def:mass-identity). Both sides are elements of R before tau.
- MeV enters ONLY at step 9 through CAL-1 m_e. Energies are attached to it two different ways in the corpus: (i) E0 = m_e c_q^2 hbar_q = m_e/(q(q-1)) (energy-scale-planck.md: 'energy of one Hecke reduction step'; used for Q_beta, the log binding functional, the n-p cell); (ii) cheat-sheet step 9 B = m_e*rho*[...] (energy = m_e x number, no c_q^2). So the corpus is internally mixed REGARDLESS of reading: two energies, one with c_q^2 and one without.
- The CAL-2 pin m_mu/m_e = Vol(4_1)/hbar_q^2 is dimensionless only if hbar_q is a pure number, and then c_q = q^-1/hbar_q is too. So reading A (c_q is the image of physical c, mapped to 1) contradicts the pin; reading B (c_q^2 an element of Q(q) evaluated at q0) is what the definitions literally say. Supports the other thread's point (2).
- Under B, def:mass-energy defines a categorical energy, not physical rest energy E = m c^2 (c = 1 would force c_q = 1). The q = 1 pole is then real: the MeV n-p cell tends to 2 m_e = 1.022 MeV as q -> 1. That is a model statement, not a defect.
- Agent's recommendation (judgement): keep reading B as the default, scope the 'speed of light' wording, and separately audit which energies use E0 and which use bare m_e (bean to follow if the owner agrees).



2026-11-22 OWNER: '\frakE is categorical energy.  Needs scaling (coming form CAL123 hopefully)'. Recorded in docs/coordination/owner-rulings.md. Reading A (c_q^2 converts to physical energy) is not adopted. Now OPEN (this bean, retitled in spirit): derive the map from categorical energy E to MeV from CAL-1/2/3 alone. Sub-tasks: (1) is E0 = m_e c_q^2 hbar_q that map, i.e. does m_e (CAL-1) fix the categorical MASS unit and what fixes the energy unit; (2) the step-9 binding uses B = m_e*rho*[...] without c_q^2, so the corpus uses two different scales; one is wrong or they need a derived relation; (3) every E0-scaled row (Q_beta, log binding, n-p cell, vertex budgets) is conditional on the answer.


2026-11-22 (Addendum 20, commit 4fc56e3342b): E₀'s c_q² shown to be the muon pin's c_q². Lean QOU/QBeta/E0MuonUnit.lean (sorry-free): 1/ℏ_q² = q²c_q²; E₀ = m_e c_q² ℏ_q; under the muon pin E₀ = m_μ ℏ_q/(q² Vol(4₁)); E₀ = m_e(ℏ_q/q²)/ℏ_q². Agrees to 1.8e-50 at muon q₀; 2.1e-7 at proton q₀ = μ–p tension. Implication: the MeV scale is m_e/ℏ_q² (CAL-1 + CAL-2), not m_e/𝔈_e; the −99 % reading used the wrong unit. n–p cell weight 2ℏ_q ln q/q² → 0 at q=1, consistent with closure mass. STILL OPEN: derive weight ℏ_q/q² from Hecke structure; 1/ℏ_q² is the CAL-2 pin, not derived.


2026-11-22 (PR #9013): is E₀'s weight w = ℏ_q/q² a convention-D Markov trace? None of the six preregistered candidates equals w. All six are certified ≠ w in Lean (QOU/QBeta/E0WeightCandidates.lean, sorry-free). The general obstruction is not in Lean: at q=1 every braid-word trace is 2^{c−n} > 0, while w(1) = 0, so no single braid word's trace can be w. Combinations and tower sums were deliberately not searched (that would be fitting). Scope (a). Audit §34; Lean coverage ledger §35.


2026-11-22 (PR #9023): two follow-ups on whether E₀'s weight w = ℏ_q/q² is a trace.
- All words, now in Lean: no braid word on any number of strands has convention-D state-sum trace w (QOU/QBeta/E0WeightAllWords.lean, traceD_ne_weight; sorry-free). The reason: at q=1 the trace is trClassical = 2^{c−n} > 0 and it is continuous there, while w(1) = 0.
- Tower-level, prereg Addendum 1. Candidates were checked by order of vanishing at q = 1.
  - Brane tower: order ≥ 2. Markov stabilisation tower and Σq⁻ᵏ: order 0. Both excluded in Lean.
  - Skein difference h·τ(β): order 1. It matches w to first order when the closure has n−1 components, but is never equal to w (hand argument, pole at q = −1).
- Conclusion: w ≈ h/2 to first order, where h = σ−σ⁻¹. The weight is still not derived. Free-coefficient combinations were not searched, because that would be fitting.


2026-11-22, prereg Addendum 2: tested the exact factor beyond h/2 using framed link invariants 𝔪 (def:mass-identity).
- Knot excess, 3₁ and 4₁: order 2 at q = 1, as predicted. So the muon knot cannot supply w.
- Linked-pair excess, Hopf± and the electron closure: order 1, with coefficient ±3 or ±12, never 1. The Hopf⁺ excess is −q⁻²·h·[3]/[2].
- No equality with w. The weight stays a definition: w = ℏ_q·(ℏ_q c_q)².
- The missing piece is a canonical object giving the one-sided deficit ℏ_q = h/(1+q).

2026-11-22 (W6, branch claude/energy-scale-cal-map-2026-11-22, commit 5438997b7, no PR yet): QOU/Observations/EnergyScaleMap.lean, sorry-free. The 𝔈→MeV map allowed by CAL-1/2/3 is Φ(𝔈)=m_e·𝔈/𝔈_e at q₀ (CAL-1 the MeV value, CAL-2 the point q₀, CAL-3 nothing here). c_q² cancels in it (energy_map_eq_mass_map); the −99 % reading is a mixing of an energy with the electron's mass (mixed_map). The calibrations cannot fix the unit/weight split nor whether c_q² sits in the weights (gauge, Chart.matches_rescale). The one open input is the electron's categorical weight 𝔈_e: the trace pipeline (σ₀σ₁σ₀, finite at q=1) and the mass formula (ℏ_q², order 2) use different ones. E₀/m_e = 1/(q(q−1)) is not a ratio of framed braid-word traces (E0_not_trace_ratio). Audit docs/audits/2026-11-22-energy-scale-cal-map.md.


2026-11-23 (W6, PR #9165, commit 05c92c799): derived the 70x unit split. tau_e = q^3 y_(3) (electron word trace 0 in (2,1)); y_(3) = 1/2 + h^2/(2[2]^2), bar-invariant; R = tau_e/hbar^2 = q^3/(2hbar^2) + q^5(q+1)^2/(2(q^2+1)^2) = 69.6509 + 0.7528 at proton q0. Mass chart cannot produce the electron (Vol(Hopf)=0, product_weight_ne): its electron weight hbar^2 is CAL-1 by hand. Trace chart: (s0 s1^-1)^2 / tau_e = 0.4054, 510x short of Vol(4_1)/hbar^2. Canonical chart still OPEN - neither derives both electron and muon. Lean QOU/Observations/ElectronUnitSplit.lean, audit section 8.


2026-11-23 (W6, ec0980bb1): owner chose 'search for one object for both'. q-volume derives the muon shape but gives the electron 0; trace+c*volume: carrier forces c = T_e(1) = 1/2 (Lean sum_family_forces_c), giving 150.33 at q0 (-27.3 %), scope-(a) negative. No single derived object yet. Audit section 9.


Claimed by claude/w6-joint-lepton-resolvent-20261123 (2026-11-23)

PR #9213 opened on claude/w6-joint-lepton-resolvent-20261123 (01ca9a6e9a9; Murakami real-q deformation excluded on sign, 29 theorems in InhomogeneousLeptonLoopResolvent.lean)


## 2026-11-25T01:16:31Z — OWNER RULING (relayed by the coordinator)
Verbatim: 'make it conjecture/contingent on BraidBoostInertialEquivalence and work BraidBoostInertialEquivalence'.
Done in PR #9402: new block conj:braid-boost-inertial-equivalence (information-theory/braid-boost-inertial-equivalence.{ts,md}, lean.ref to the class); conditional banner on prop:mass-energy, with the conjecture added to its uses[]; mass-energy-equivalence-interpretation no longer says 'not an independent postulate'.
NARROWED: this bean now waits on qou-2k68 (a definition of inertial mass independent of m, then the class) and on the E_e / 70x unit split, which are the same missing input seen from two sides. Route 1 is excluded (probe braid_boost_inertial_clock). Kept OPEN (Rule 13a).
