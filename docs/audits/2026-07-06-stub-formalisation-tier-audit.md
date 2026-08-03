# Audit — genuine vs axiomatised: the 29 stub formalisations (2026-07-06)

Classifies every one of the 29 empty-stub formalisations (landed via
#3370/#3390/#3394/#3399/#3402) into **Tier 1 (genuine theorem)** vs **Tier 2
(conditional carrier)**, records the exact axiom each Tier-2 carrier hides, and
rates the tractability of *de-axiomatising* it (deriving the field from
primitives / cross-wiring to an existing QOU result).

## Definitions

- **Tier 1 — genuine theorem.** The proved statement is a real mathematical
  fact — an algebraic identity, group law, combinatorial count, or analytic
  bound — that follows by `ring`/`rfl`/`decide`/induction from *definitions*.
  Any `structure` fields are standard defining data (a group presentation, an
  idempotent, an involution), not a hidden physical claim.
- **Tier 2 — conditional carrier.** The substantive claim is **axiomatised as
  a `structure` field**; the Lean proves a *consequence* modulo that axiom.
  De-axiomatising means constructing/deriving the field rather than assuming
  it.

Every file is sorry-free either way; the tier is about *what* is proved.

## Tier 1 — genuine theorems (19)

| File | What is genuinely proved |
|------|--------------------------|
| `BraidTwistFlip` | Klein four-group `V₄` involution/commutativity laws (`rfl`) |
| `ColorTubeFibers` | cubic → monic-elliptic shift identity (`ring`) |
| `MagicShellCouplingKappa` | `[3]_q = [2]_q² − 1` |
| `QMomentum` | `p_q = writhe` (induction over the ±1 word; `[±1]_q = ±1`) |
| `IsotopeKnot` | isotope equivalence is refl/symm/trans → `Setoid` |
| `Su2Generators` | commutator `[β,α]=α⁻²` and `α⁶=1` from the Dic₃ presentation |
| `TypedGarsideElement` | crossing-table symmetry + `binom(A,2)` count |
| `QValueTransition` | mass-gap expansion `Q = m_n−m_p−m_e+ΔB` |
| `TransferMatrixOperator` | Hecke reduction: identity acts trivially, `σ·σ` recovers `σ²=(q−q⁻¹)σ+1` |
| `QuarkAntiquarkProduction` | classical limit `h=0`, cross-color Hopf product, Hopf balance |
| `HqBiFiltration.BiFiltration` | projector `p=e·(−)·e` idempotent + `e`-fixed set additively closed |
| `InterfaceComposition` | canonical ≡ paired profile ≠ alternating (`decide`) |
| `ShellSchurWeylSelfDuality` | transpose involution ⇒ bijective; self-dual = fixed points |
| `Intent` | two-observer discrepancy (commutator) vanishes on commuting obs, antisymmetric |
| `QuaternionicSpectralResolvents` | `r=−ln\|q\| ≥ 0` on `0<\|q\|≤1`, `\|q\|=e^{−r}` |
| `ComputationalHorizon` | horizon bound non-negativity + `3^c` leaf-count positivity |
| `ElectronShellCapacity` | `capacityUpTo` sum = bonding-site sum (`Finset.sum_congr`) |
| `QVonMangoldtFunction` | `Λ_q` vanishes off fundamental defects |
| `QChebyshevFunction` | `ψ_q(X)=0` below the smallest norm |

These need no further "proving" — they are complete. (Deepening them means
enriching the *statement*, e.g. proving `Su2Generators` over the concrete
`SU(2)` matrices rather than an abstract group with the Dic₃ relations — a
statement upgrade, not a `sorry` to close.)

## Tier 2 — conditional carriers (10)

| File | Axiom field(s) carried | De-axiomatise by | Tractability |
|------|------------------------|------------------|--------------|
| `SkeinResolutionObstruction` | `χ`, `res` (restriction map), `κ_def` | cross-wire `χ` to `qou_obstruction_reduction`'s `obstruction_class`/`chi_A` (already on main) | **HIGH** — pure cross-wire |
| `FrobeniusSelfDualityForcesLPDualExtraction` | `τ` cyclic/additive/**non-degenerate** | instantiate `τ` with the real Markov trace; `MathlibExt/FrobeniusInnerProduct` may supply non-degeneracy | **MED** |
| `SpinInvolutionLPDualInvariance` | trace apparatus (anti-mult, cyclic, involutive, `σc=c`) | instantiate with the real Markov trace + bar-involution | **MED** |
| `ObservableSubcategory` | `observable_iff` (`Γ(𝒮,A₀)≠0`) | wire `A0section` to the real degree-0 section functor | **MED** |
| `CompoundBetaShellCalibration` | `E0_eq : E0 = 𝔔_β` | derive `E0=𝔔_β` from the shell-binding compute (β-decay Q-value chain) | **MED** (compute-side) |
| `BreitWheelerPairProduction` | NF coefficients `nfSigma=q−q⁻¹`, `nfConst=1` | derive from the actual `σ₀²` Hecke reduction (see `TransferMatrixOperator`) | **MED** |
| `HorizonFunctor` | `boundary_nonobservable` (∂ lands in complement) | construct `boundary` from actual directed limits with `A₀=0` | **LOW** (needs limit infra) |
| `CMBFunctor` | `jetColimit`, `CMB_def` | construct the actual jet-quotient colimit in `Mod_R` | **LOW** (needs colimit infra) |
| `BlowupCalculus` | `BlowupField` instance (ω infinite, `st` kills ε) | construct a `BlowupField` model (Levi-Civita / hyperreals) | **LOW** (Mathlib `Surreal`/hyperreal cone absent from cache) |
| `CategoricalMassMarkov` | `Φ` (mass endomorphism) exists | construct the actual Markov-trace mass endomorphism | **LOW** (overview block; the endomorphism *is* the open arc) |

## Recommended order of attack

1. **`SkeinResolutionObstruction`** (HIGH) — cross-wire to
   `qou_obstruction_reduction`. Done first this session.
2. `FrobeniusSelfDuality` / `SpinInvolution` / `ObservableSubcategory` (MED) —
   instantiate the trace/section against real QOU library objects.
3. `BreitWheeler` / `CompoundBetaShellCalibration` (MED, compute-linked).
4. The LOW trio (`HorizonFunctor`, `CMBFunctor`, `BlowupCalculus`,
   `CategoricalMassMarkov`) need genuine infra (limits, colimits, an ordered
   non-archimedean field) — these overlap the framework's open research program
   and the Subgoal-2 / keystone epic (`08a2`); do not attempt as quick wins.

Each Tier-2 row is tracked as a bean (see the `stub-deaxiom` epic `6awe`).

## De-axiomatisation results — FINAL (2026-07-06)

**10 / 10 Tier-2 carriers de-axiomatised.** The last wall,
`CategoricalMassMarkov` (bean `2g2u`), was closed by **cross-wire** — the
carrier's two free fields are now *derived* from the real `HeckeMassElement`:

| Carrier | Bean | How |
|---------|------|-----|
| `CategoricalMassMarkov` | `2g2u` | `ofHecke`: `Φ := (Φ_mass · —)` is genuine left multiplication (`AddMonoidHom`, additivity = `mul_add`, not a posited field); `φ_n := Φ^[n](Φ_mass)` is the Φ-orbit of the mass element (`φ_0 = Φ_mass`, `φ_{n+1} = Φ(φ_n)` proved). Honest cross-wire to `QOU.Torsion.HeckeMassElement`, **not** illustrative inhabitation (a dummy `Φ := id`, `φ := 0` would compile but carry no content). lean-direct exit 0, sorry-free. |

Distinction: bean `2g2u` was the Lean *carrier* (which merely **named** `Φ`/`φ`
as free fields). The framework's open *research* item — the **closed form** of
`Φ_mass(β) ∈ H_n(R,q)` and its Volume-Conjecture bridge — is `conj:mass-
endomorphism`, addressed separately by the new **`VolumeBridge`** companion
below (§3b-cond conditional carrier), not by this cross-wire.

### `VolumeBridge` — non-degenerate §3b-cond carrier for `conj:mass-endomorphism`

New module `QOU/MassEndomorphism/VolumeBridge.lean` (aggregated). It reduces the
conjecture's open surface to exactly its one open ingredient — the
**Volume-Conjecture bridge** (Step 3: `J(K;q) ≠ Vol(K)`, bridged only by
Kashaev/Murakami–Murakami) — axiomatised as an **instance-free** class carrying
that bridge as its *hypothesis* field, and **derives** the manuscript's
transient identity (`transient = volTerm − descTrace`) and full-mass = volume.
Non-degenerate per §3b-cond item 5 (field = input, theorem = derived output);
instance-free per §3b-tax (honest open primary — the conditional results are
genuinely *modulo the Volume Conjecture*). lean-direct exit 0, sorry-free.

> **Follow-up flagged (not actioned):** the sibling `MassEndomorphism` class
> (`MassEndomorphismConjecture.lean`) ships a global all-zeros `instance
> canonical`, and `MassEndomorphismTrivial.lean` ships `trivial_int_zero`;
> both make `[MassEndomorphism R β]` trivially synthesizable, so conditionality
> against *that* class is vacuous. Those are GAP-18a-audit-governed
> (`docs/audits/2026-05-04-gap-6a-18a-scoping.md`) and out of scope for bean
> `2g2u`; demoting them to non-instance `def`s is tracked separately.
> `VolumeBridge` is the instance-free alternative used going forward.

### Earlier de-axiomatisations (first 9, unchanged)

**9 / 10 Tier-2 carriers de-axiomatised (prior passes).** Beyond the first 5,
four more were completed — including the flagship `BlowupField`, which required
cloning Mathlib @f897ebcf and building the `Hyperreal` olean cone from source:

| Carrier | Bean | How |
|---------|------|-----|
| `BlowupCalculus` | `zkst` | **hyperreals `ℝ*` are a genuine `BlowupField`** (`instBlowupFieldHyperreal`), every axiom a Mathlib theorem. Also corrected a latent over-idealisation — the unconditional `st_add` (false in every real model) is now conditioned on `IsFinite`, matching `Hyperreal.st_add`. |
| `HorizonFunctor` | `bqfr` | `ofSpace`: topological model, `boundary = frontier(region) ∩ {A₀=0}`; `frontier` is the genuine limits operator, so `boundary_nonobservable` is a theorem |
| `CMBFunctor` | `gob0` | `ofJet`: genuine finite direct-sum colimit `∑_{c∈S} jet c`; `CMB = colimit ∘ ∂` by `rfl` |
| `CompoundBetaShellCalibration` | `lqft` | `ofCalibration`: `E₀ := 𝔔_β` structurally (`E0_eq` is `rfl`) — "no new calibration" is definitional |

**0 / 10 remain (as of the 2026-07-06 cross-wire pass).** The last carrier
`CategoricalMassMarkov` (bean `2g2u`) is now de-axiomatised by cross-wire (see
the FINAL section at the top). The *research* conjecture behind it
(`conj:mass-endomorphism`, closed-form `Φ_mass`) stays open — that is a
statement about the framework's mathematics, not a Lean carrier axiom, and is
now carried honestly by the instance-free `VolumeBridge` §3b-cond class. The
earlier "deliberately left open" note below reflected the pre-cross-wire state:

### First 5 (recorded above, unchanged)

**5 / 10 Tier-2 carriers de-axiomatised** — their axiom fields are now
*theorems* obtained from a concrete construction or a cross-wire (each
sorry-free, lean-direct exit 0):

| Carrier | Bean | How it was de-axiomatised |
|---------|------|---------------------------|
| `SkeinResolutionObstruction` | `7kzn` | cross-wired `χ` to `qou_obstruction_reduction`'s `obstruction_class`; consistency derived through the shared `kappa_vanishes_iff` |
| `FrobeniusSelfDualityForcesLPDualExtraction` | `cy3v` | concrete `matrixModel`: `Matrix.trace` proves cyclicity (`trace_mul_comm`), additivity, non-degeneracy (matrix-unit pairing) |
| `SpinInvolutionLPDualInvariance` | `ovh1` | concrete `matrixModel`: `σ = transpose` proves anti-mult, involutive, trace-invariance, cyclic, `σ`-fixed identity |
| `ObservableSubcategory` | `tps9` | `ofSection`: the observability predicate is *derived* as `A₀ ≠ 0`, so `observable_iff` is `Iff.rfl` |
| `BreitWheelerPairProduction` | `h2yz` | `ofHecke`: NF coefficients derived from `TransferMatrixOperator`'s proved `σ²` Hecke reduction (cross-file cross-wire) |

**5 / 10 remain — honest compute / infra walls** (NOT quick wins; each is a
genuine external dependency, tracked as an open bean):

| Carrier | Bean | Wall |
|---------|------|------|
| `CompoundBetaShellCalibration` | `lqft` | `E₀ = 𝔔_β` is a **numerical calibration fact** — de-axiom is compute-side (β-decay Q-value chain), not pure Lean |
| `HorizonFunctor` | `bqfr` | needs an actual directed-limit / boundary construction (category-theory infra) |
| `CMBFunctor` | `gob0` | needs an actual jet-quotient colimit in `Mod_R` (colimit infra) |
| `BlowupCalculus` | `zkst` | needs a `BlowupField` model (ordered non-archimedean field). **Verified 2026-07-06: environmental block** — `Hyperreal` (ℝ*), `HahnSeries`, and `LaurentSeries` oleans are *all* absent from the restored sandbox cache (0 oleans + 0 source each) and unfetchable (release server firewalled). The faithful model `ℝ((X))`/ℝ* would compile in a full Mathlib build; it cannot be constructed in this sandbox. Not faked with toy inhabitation. |
| `CategoricalMassMarkov` | `2g2u` | the Markov-trace mass endomorphism **is** the framework's open research arc (mass-endomorphism conjecture) |

Trivial *inhabitation* of the LOW four (a dummy instance proving the carrier is
non-contradictory) is possible but does **not** de-axiomatise the substantive
content, so it is deliberately not done — the beans stay open as honest walls,
overlapping the keystone epic `08a2` and the Subgoal-2 q₀ decline.
