---
# qou-jfx8
title: 'Formalize-first: state the structural claims the picture needs (shadow prices as directions of entanglement history; phase-space measure from the dual; relative Reeb angle as a jet-level datum) as Lean scaffolds or conjecture classes before any probe'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-16T00:47:53Z
updated_at: 2026-10-12T23:42:31Z
parent: qou-v2om
---

## 2026-09-16 — derived half landed; conjecture half held for the owner

LANDED: folio/quantum-observable-universe/lean/QOU/MassTheory/BlockMeasureFromFrobeniusPairing.lean — FrobeniusPairingData (trM = Σ y χ, χ(1)=dim, trM 1 = 1); blockMass_sum_eq_one; trM_eq_expectation; trM_le_of_normalised_le / le_trM_of_le_normalised (needs IsProbability, a HYPOTHESIS — positivity of convention-D y_λ is measured n=3..12, not proved at general n); entangledSupp + trM_eq_of_entangledSupp_empty + bindingForm_eq_zero_of_entangledSupp_empty (ℝ section); charSupp/level + level_one_eq_top + level_le_level_one. lean-direct -DautoImplicit=false -s 65536 exit 0, no warnings; #print axioms: propext, Classical.choice, Quot.sound on all seven. Registered in QOU.lean.

HELD (not committed): a primary conjecture class RelativeReebDatum for the owner's relative-angle datum — Lean text in the analysis doc §8 O3. Reason: §3b-tax needs content-bearing fields and the content is exactly what is undefined; owner's rule against speculative code. Also held: any Möbius-energy objective (O4) until qou-99qc pins classicalLimitConst.

Probe: computations/probes/deuteron_block_measure_entangled_support_probe.py (6/6, committed inputs only, weight_family declared). Bean stays in-progress per rule 13a (the picture's structural claims are open).


Correction (same hour): the ℝ theorem bindingForm_eq_zero_of_entangledSupp_empty lives in the §7c companion QOU/MassTheory/BlockMeasureBindingFormArchimedean.lean, not in the generic file — check-sidecars flagged the mixed file and it was split before commit.



## 2026-09-16 — owner: 'formalize and work on RelativeReebDatum conjecture class'

Owner clarification (verbatim gist): the relative Reeb angle between two knots 'is supposed to be the evaluation/trace of the substrate phase space at the point'. That is explicit consent for the held class. Branch claude/lr-a3-reeb-datum-composition-program-2026-09-16 from main 1a5059cffb; committing RelativeReebDatum as a content-bearing primary conjecture class (no instance), with derived consequences as theorems taking the class as hypothesis.



## 2026-09-16 — RelativeReebDatum committed (class, no instance)

QOU/MassTheory/RelativeReebDatum.lean: class over BranchingData ℝ A₁ A₁ A Λ₁ Λ₁ Λ with lightCone, compose, Entangled; clauses compose_eq (a ⋈ b = (a⊗b)·lightCone), lightCone_of_not_entangled (= 1), trM_lightCone_mem (∈ [−1,1]); phaseSpace (block vector of the light cone), relAngle := arccos ∘ trM ∘ lightCone; proved sum_phaseSpace and the four no-shared-history consequences (composite = free product, trace factorises, bindingForm 0, relAngle 0). Probe relative_reeb_datum_trace_angle_probe.py (7/7): trace-level candidate θ = arccos(∏(z_D+d)) defined and monotone (D 59.45°, 3He 71.86°, T 78.16°, 4He 82.78°); block-level ratio NOT definable (|χ_atom/χ_free| > 1 on T (5,4), 3He (9),(5,4)). Roast: on the only defined candidate the angle is the binding form under cos θ = exp(−B/α) — redundant. Stays in-progress (rule 13a: lightCone is data, the conjecture is open); options doc §8 O2/O5.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-16 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-12 — owner reformulation: segment collision (replaces the light-cone reading)

Owner: only ONE braid segment from each particle meets at p on the exceptional divisor; history enters as the categorical trace of the γγ tower; incoming angle = relative minimum of local rotational energy (O'Hara + Bring), starting the Reeb/geodesic flow (cf. qou-rydq: the Bring cone link is UT(Σ₄), so the Reeb flow is the geodesic flow of Σ₄ and an incoming direction at p is a point of UT(Σ₄)).

Landed (Lean `QOU/MassTheory/SegmentCollisionDatum.lean`, lean-direct exit 0 with -DautoImplicit=false, 14 theorems, axioms propext/Classical.choice/Quot.sound only; probe `computations/probes/segment_collision_probe.py`, 9/9):

- **A. Single-segment marginal is UNIVERSAL** (conditional on DisjointBlockMultiplicative, itself conditional on TowerSpan): tr(a·(α+βσ+γσ⁻¹)·b) = (α+βz+γz⁻)·tr a·tr b. Measured on p, n, core × p, n, σ³ in H₆: ratios (1, z_D, z_D−h) to 4e-50. So the "unknown initial photonic state" provably drops out — but so does everything else: a single-segment collision CANNOT separate particles of equal trace (`bridge_cannot_separate`).
- **Dichotomy**: a two-segment probe (σ₁σ₂, one strand into a's history) is NOT universal: p 1.2441, n 1.4706, core 0.3801 (depends on a only).
- **B. Channels**: Sym (q⁴+q²+1)/(q²+1)² = 0.75270, Alt q²/(q²+1)² = 0.24730 — exactly y_(2), y_(1,1) at n = 2; both live.
- **C. Local O'Hara cross term is chirality-blind** (θ↦π−θ and d↦−d, both proved); a reflection-symmetric energy with a unique minimiser selects θ = π/2 (proved). Measured min at π/2 for ℓ/d ∈ {0.5,2,10,50}; log coefficient → 2π/sin θ.
- **D. `SegmentCollisionDatum` class, no instance**: θ* = π/2 whenever the Bring term is achiral. Any σ-vs-σ⁻¹ selection must come from a chiral Bring term. Note: `isMin` is unused by that theorem (only uniqueness is).

Promising? Partly. The localisation is clean and the history-forgetting is a theorem, but it makes the single-segment collision blind to which particles collide, and O'Hara alone picks the achiral perpendicular angle. Live directions: (i) widen the collision window to k segments from each (k = 2 already sees history), (ii) derive a chiral Bring term on UT(Σ₄). Status stays todo: open conjecture class.


## 2026-10-12 (later) — k-window and chiral Bring term
- k-window (probe segment_window_bring_chirality_probe.py, 11/11; Lean Part E window_cannot_separate): on the production T and ³He words, windows k = 1, 2, 3 on the colliding side give identical states (≤ 1e-50); k = 4, the first window reaching the bond at generator 5, separates them (worst |φ_T − φ_He| = 0.921 on x = σ₇σ₅). The minimal separating depth is FORCED by the 3-strand nucleon block, not chosen: one segment past the top block.
- Chiral Bring term: NOT derived as an energy. Proved (BringConjugationChirality.lean): Bring's curve is real, so conjugation is a fixed-point-free orientation-reversing isometry; any metric-only energy averaged over a conjugate pair is even and selects no crossing sign. The chiral DATUM that exists: the 5-cycle rotates the tangent line at its fixed point p_j by ζ^(−j) (proved in ZMod 5, checked by Jacobian kernel to 1e-60); conjugate points carry conjugate rotations, none real. The corpus Reeb angle arccos(χ(C₅)/dim) keeps only the real part, i.e. discards exactly this sign. Turning it into a σ-vs-σ⁻¹ preference needs the rule bar involution ↔ conjugation: ChiralityMatching class, no instance — owner decision.


## 2026-10-12 — chirality: scope correction and the q-metric literature
CORRECTION to my earlier claim 'metric-only Bring energies are achiral': that holds for links in Σ × I (ι × id has Jacobian det −1, swaps σ ↔ σ⁻¹). On UT(Σ₄), where the corpus puts the Reeb flow, the natural lift of ι is its differential (x,y,θ) ↦ (x,−y,−θ), det +1: orientation-preserving, so it does NOT swap crossing signs. Lean: sigmaI_lift_reverses, ut_lift_preserves. ChiralityMatching's letterSign_conj is the Σ × I reading and fails under the natural UT lift. Literature (agent, verified algebra): quantum disc relation z*z − q²zz* = 1 − q² (held: arxiv-2507.13873v1) becomes the q⁻¹ relation under z ↔ z*; skein theory: orientation reversal of the 3-manifold sends A ↦ A⁻¹ and links to mirrors (arXiv:1610.04728; Bonahon–Wong 1009.0084 for genus g); DGG (held arxiv-1112.5179v1): conjugation = q ↦ q⁻¹ at |q| = 1. Corpus block c-equals-bar-iff-all-1dim: σ ↦ σ⁻¹ and q ↦ q⁻¹ agree on characters only if all irreps are 1-dim, so 'conjugation = bar' can only be a joint symmetry. Reading: on a 3-manifold, chirality is set by q₀ > 1 against the ambient orientation, not by position on Σ₄. Derived for Σ × I; open (motivated) for UT(Σ₄): the gap is that the Hecke q is the quantization parameter of Σ₄.


## 2026-10-12 — option 1: what IS derivable (BringUTContactChirality.lean, exit 0; probe ut_contact_orientation_probe.py 5/5, exact)
1. The geodesic flow fixes the orientation: Liouville form α = (cos θ dx + sin θ dy)/y has α∧dα = −(1/y²) dx∧dy∧dθ, nowhere zero; canonical orientation of UT(Σ₄), opposite to the naive complex one (consistent with BringConeLinkEulerNumber's 'orientation reversed').
2. Conjugation lifts to a STRICT contactomorphism (pullback α = α, det +1); α is metric-defined so every isometry's lift preserves it (dilation, inversion checked). Conjugation cannot carry chirality on UT(Σ₄).
3. UT(Σ₄) is chiral: e = −6 ≠ 0, no fibre-preserving orientation reversal (fibre-preservation of homeos for SL̃₂ geometry is cited, not proved).
Verdict: on UT(Σ₄) the σ/σ⁻¹ preference is fixed by (canonical contact orientation, q₀ > 1) up to ONE global sign convention ('positive crossing = positive for α∧dα'), equivalent to the q₀ > 1 choice already made. ChiralityMatching (per-collision, via conjugation) has the wrong shape for UT(Σ₄) and should not get an instance. Remaining derivation gap (unchanged): that the Hecke q is the quantization parameter of Σ₄ / UT(Σ₄). Note: the probe's first run failed on the inversion check because my pushed-angle formula had a spurious +π (w' = 1/z², angle θ − 2 arg z); fixed before commit.


## 2026-10-12 — the last bit removed (for Reeb strands)
The Hecke↔skein identification is the corpus's own dictionary (AGENTS.md §7a: σ = L₊, Hecke relation ↔ L₊ − L₋ = (q − q⁻¹)L₀), so 'is the Hecke q the skein parameter' is settled by convention; the open question was only what orients crossings in UT(Σ₄). Proved (BringUTContactChirality §4, exit 0; probe 9/9): the geodesic spray R = (y cos θ, y sin θ, −cos θ) is the Reeb field of α (α(R) = 1, ι_R dα = 0), so Reeb strands are positively transverse to ker α. α then fixes both strand direction and ambient orientation, hence every crossing sign (Bennequin, cited). With §7a and q₀ > 1, the σ/σ⁻¹ preference at a collision of Reeb strands is DERIVED, no convention left. Input stated, not proved: the owner's picture that strands follow the Reeb flow. Deliberately not done: an instance of ChiralityMatching (wrong shape on UT).


## 2026-10-12 — CORRECTION: two Reeb flows, opposite chirality (owner question: why was strands-follow-Reeb not clear?)
My previous entry said the σ/σ⁻¹ preference is 'derived, no convention left'. That holds only for strands following the GEODESIC flow. UT(Σ₄) has two canonical contact forms: Liouville α (Reeb = geodesic spray) and the connection form η = dθ + dx/y (Reeb = fibre rotation ∂_θ, the Seifert circle action = Sasakian Reeb of the cone link). Proved (BringUTContactChirality §5, exit 0; probe 13/13): α∧dα = −1/y², η∧dη = +1/y² — OPPOSITE orientations; each flow is Legendrian for the other (η(R) = 0, α(∂θ) = 0). The corpus never states that strands follow the Reeb flow; fermion-boson-knot-link-proof has strands WIND AROUND 'the Reeb direction' (vertical = fibre), with signed winding ±1 — the fibre reading. Owner (2026-10-12): strands follow 'Reeb flow/geodesic' — these are different flows, so this is a modelling decision, not a Lean proof. Not affected: everything else (window, towers, descending step). Contaminated: my issue #7740 comment of 670ff8c658 ('no convention left'), corrected there.


## 2026-10-12 — 🟧 OWNER RULING: strands follow the FIBRE Reeb flow ('2 fibre'); chirality wired; both flows checked
BringUTContactChirality §6–7 + SegmentCollisionDatum Part G (both lean-direct exit 0). Fibre reading: orientation +dx∧dy∧dθ independent of fibre direction ((−η)∧d(−η) = η∧dη); e = −6; chiral invariant = torsion linking residue of the fibre class ℓ = −1/e = 1/6 ∈ ℚ/ℤ (H₁ = ℤ⁸ ⊕ ℤ/6), ℓ ≢ −ℓ. Geodesic reading (checked on owner request): reversed orientation, e = +6, ℓ = −1/6 ≡ 5/6, also chiral. So both flows give chirality, mirror-image; the flow fixes only its sign. Part G: for a covariant Bring energy E(π−θ, ℓ) = E(θ, −ℓ), reflection symmetry ⇔ residue-evenness; a residue-sensitive E is chiral and Part D's θ* = π/2 no longer follows. Fit check: fermion-boson-knot-link-proof's opposite vertical windings ±1 read naturally as particle/antiparticle = oppositely oriented fibre strands (supports, does not prove, the ruling). NOT derived: E's residue dependence (a formula for the Bring energy). Owner follow-up (2026-10-12, mid-turn): 'flow by the knot convolution operator' — queued.


## 2026-10-12 — 'flow by the knot convolution operator'
The convolution letter σ generates the flow σ^t = q^t P_S + q^{−t} e^{±iπt} P_A: on the Alt channel each crossing is a rotation by π, the full twist σ² is one full turn — the algebraic counterpart of the fibre rotation; the ± branch is the chirality, the real part q^{−t}cos(πt) is branch-free. Consequence measured: the A = 2 parity finding is cos(πt) and is scope-limited (see qou-8r6b). Open: identifying the π-per-crossing Alt phase with the geometric fibre rotation of UT(Σ₄) (a conjecture, not proved).


## 2026-10-12 — the convolution flow's half-turn IS the fibre rotation of the relative direction (ConvolutionFlowFibre.lean, exit 0)
Modelling reading (stated): two nearby fibre strands over p and p+r; the relative direction r/|r| is a point of the fibre UT_pΣ₄ (owner's 'relative vector in computation velocity space'). Proved: exchange fixes the centre and sends r ↦ −r (sign rep = q→1 limit of the Alt channel); the half twist r·e^{iπt} is a flow, one half twist = exchange, two = full turn; on a unit r = e^{iθ} it is the fibre Reeb flow θ ↦ θ + πt; the Alt eigenvalue −q⁻¹ has phase π and modulus q⁻¹, and the flow q^{−t}e^{iπt} = q^{−t}·halfTwist t 1. Verdict: the Alt-channel phase of σ^t is the fibre rotation of the relative direction; the q-deformation is pure modulus. Branch fixed by the right-hand rule with strands along +∂θ in the ruled orientation: σ ↔ e^{+iπ}. Not established: a geometric meaning for the modulus q^{−t}; strands not nearby.


## 2026-10-12 — owner refinement: 'geodesic is for a single braid; the knot-convolution operator # changes this'
Formalized (BringUTContactChirality §8, exit 0): during a convolution the velocity is X + κV; η(X + κV) = κ is the geodesic curvature (free strands: κ = 0, η-horizontal); α(X + κV) = 1 for all κ, so strands are always positively transverse to ker α, while η changes sign with the turn. FLAG: this makes the α (geodesic) orientation the one fixed by transversality, residue −1/6 — the mirror of the +1/6 recorded under the earlier 'fibre' ruling. The fibre flow enters as the convolution's turning (π per half twist, ConvolutionFlowFibre), not as strand direction. Owner to confirm which orientation is canonical.
## 2026-10-12 — MY ERROR in the molecular junction question
I told the owner the corpus bond is 'σ² (Hopf link) per shared pair' and electrons add Z strands; owner picked σ² and 3A+Z on that basis. The corpus actually says (covalent-bond-shared-trefoil.md): L_b = ∏_e σ⁻¹_{g_e(p_j)}·σ⁻¹_{g_e(p_i)} — each shared electron crosses a proton of EACH atom with σ⁻¹ (writhe −2 per electron; a NEGATIVE Hopf link), and each electron is a trefoil σ₀σ₁σ₀ in its own local H₃ (3 strands, so 3A + 3Z), while molecular-braid.md says n_i = A + Z. molecular-crossing-table.md DOES exist (inter-atomic pp σ, pn/nn identity, p e σ⁻¹). Nothing built; owner re-asked.


## 2026-10-12 — 🟧 OWNER RULINGS (final for this session)
1. Orientation: 'Geodesic α, ℓ = −1/6'. Free strands follow geodesics; the knot-convolution operator # adds fibre turning κ = η(velocity); crossings are oriented by α∧dα. Canonical residue −1/6 (BringUTContactChirality §9, canonicalResidue; §6's +1/6 kept as the superseded record). Part G updated (canonical_residue_not_self_mirror). Lean exit 0.
2. Molecular bond operator: corpus L_b (σ⁻¹ to a proton of each atom per shared electron, plus crossing table). 3. Electron strands: 3A + 3Z (electron = trefoil in local H₃). Build dispatched to a background agent (branch claude/molecular-word-corpus-lb-2026-10-12, stacked on #7769); unfixed layout choices are to be listed, not chosen.


## 2026-10-12 — residue dependence of the Bring energy DERIVED (given one stated modelling step)
BringResidueEnergy.lean (exit 0) + bring_residue_energy_probe.py (8/8). Step (stated, not proved): ambient fibre linking ℓ enters as the convolution-flow time t = 2ℓ (fractional twist σ^{2ℓ}); exact for the abelian/linking part; consistency e·ℓ = −1 (six pairs = one full negative twist). Energy E(ℓ) = −log μ(2ℓ), μ(t) = q^t w_S + q^{−t} cos(πt) w_A (convention-D bridge weights; μ(1) = z_D, μ(−1) = z_D − h checked). Proved: mirror = bar involution (μ_q(−t) = μ_{1/q}(t)); classical limit q = 1 achiral; chiral part factors μ(t) − μ(−t) = (q^t − q^{−t})(w_S − cos(πt) w_A) with the second factor > 0 under convention D, so chirality ⇔ q ≠ 1 and ℓ ≠ 0, sign = sign(ℓ ln q). At q₀, ℓ = −1/6: μ = 0.854998, E = 0.156656; mirror μ = 0.898764, E = 0.106735; gap 0.049921. Not derived: angle dependence E(θ, ℓ), overall scale α.


## 2026-10-12 — relative minimum (owner's principle) gives a preferred twist and a turning angle
BringResidueEnergy (exit 0): μ'(0) = ln q·(w_S − w_A) (hasDerivAt_mu_zero); under convention D w_S − w_A = (q⁴+1)/(q²+1)² > 0, so for q > 1 the relative minimum of E sits at t* > 0 — a preferred twist direction (σ side, canonical orientation), absent at q = 1. Probe (12/12): t* = 0.0217944 (μ'' = −2.408), collision twist s* = t* − 2ℓ = 0.355128, turning angle π s* = 63.923°. The angle reading uses ConvolutionFlowFibre's identification (flow time s turns the relative direction by πs) and the stated modelling step (ℓ enters as flow time 2ℓ). Nothing fitted.


## 2026-10-12 — owner checks 1 and 2 on the residue energy (fractional_twist_consistency_probe.py, 7/7)
(0) Owner question 'what collision? doesn't it depend on the knots?': at TRACE level t* = 0.021794 is identical for pp, pn, nn — Part A universality; the 63.92° is knot-blind. Block level it depends on the knots and even flips sign: t*_(5,1) = −0.0058 (pp), −0.0102 (pn), −0.0123 (nn); t*_(3,3) = 0.0076, 0.0160, 0.0271; (4,2) 0.0024, 0.0139, 0.0034.
(1) Non-abelian step: group law, (σ^{2ℓ})⁶ = σ^{−2}, far commutativity and the trace-level fractional Markov property hold on all H₃/H₆ blocks; the BRAID RELATION FAILS for fractional t on the (2,1) block (defect 0.5688 at t = ±1/3, 0 at t = 1). σ^{2ℓ} is consistent only as a single-bridge object, not a braid action. Trace value of σ₂^{−1/3} on the deuteron: 0.854998 − 0.221746i (real part = μ).
(2) Cross-check: 63.92° = 60° (residue: 180°·|2ℓ|) + 3.92° (t*). Corpus Reeb angles A 0°, T₁ 57.36°, H 90°, T₂ 101.89°, G 104.48°; C₅ rotations 72°, 144°. Nearest T₁ (Δ 6.56°); no match within 1°. Recorded, not fitted.

## Round 78 progress (PR #8351)
- Advanced in PR #8351 (`5905e086a748f98972bca5ebd225e0c19c3a6223`).
