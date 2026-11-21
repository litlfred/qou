/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.QBeta.A3AntiSelfAdjointLift
import QOU.MathlibExt.QCharacter

/-!
# QOU.QBeta.BirkhoffAmplitudeE — CONSTRUCTING the C1 Birkhoff cross-ratio that carries the A=3 amplitude `E`; the precise next WALL is its VALUE.

**Scope (read this first).**  `QOU.QBeta.A3AntiSelfAdjointLift` (merged #4611) bracketed the
A=3 Δ_λ magnitude lift `r* = μ₃/c₃ ≈ 1.585` to EXACTLY ONE free real DOF — the
anti-self-adjoint off-block amplitude `E` (`E ↦ factor` a bijection: `amplitude_injective`
+ `amplitude_surjective`).  Its sibling `QOU.QBeta.StokesAmplitudeE` (#4811) proved the
**LOCAL** Stokes / resurgence route cannot supply `E`; PR #4810 (`DTIndexAmplitudeE`)
proved the DT-index route is bar-parity excluded.  Both pin `E`'s value to the **GLOBAL
`0↔∞` Birkhoff connection matrix** `P = (X^{(∞)})⁻¹ X^{(0)}` of the C1 module (= the DM
q-cubic `conj:qdifference-kernel-prolongation-symbol` = RSZ route-A `L1`), whose entries are
theta-valued.

**Convergence with the well-posedness sibling (`BirkhoffAmplitudeWellPosed.lean`,
sorry-free).**  A parallel agent proved the decisive *well-posedness* fact: because C1's
local solution bases are unique only up to a `q`-invariant (elliptic) diagonal
normalization (`QCharacter.IsQChar.ratio_qInvariant`), `P` carries the gauge
`P_{ij} ↦ (d_{∞,i})⁻¹ P_{ij} d_{0,j}`.  A single matrix ENTRY is therefore gauge-dependent
(`entry_not_gauge_invariant` / this file's `entry_gauge_movable`) — **ill-posed** as the
value of a physical scalar.  Since `E` is frame-free (`A3AntiSelfAdjointLift.amplitude_injective`),
`E` cannot be an entry: **`E` must be the unique gauge-invariant functional of `P`, the
cross-ratio** `χ(P) = P₀₁P₁₀/(P₀₀P₁₁)` (four entries − three gauge dims = one invariant).
This file *independently confirms* that fact (Part 2) and takes the assigned **construction**
angle on it (Part 1): build the cross-ratio's structure from the q-character infra, and
locate the precise remaining wall (Part 3–4).

**What is DETERMINED and what is OPEN (corpus state, all on main).**

* The **`0`-side** (Fuchsian) exponents of C1 are DETERMINED: the roots `c₀` of the indicial
  equation `c₀² + (q−1)c₀ + (q−1) = 0` (`C1FuchsianExponents`, `C1ZeroSideExponents`).
* The **`∞`-side** exponent is OPEN: C1 is slope-`½` irregular at `∞`, so its canonical
  solution needs the q-native wild / alien datum (`2026-08-08-rsz-c1-infinity-route-closed.md`;
  bean `qou-vkg5`).
* The **cross-ratio `χ(P)`** has a theta closed form whose *ellipticity* is PROVED
  (`C1ConnectionPoles.connRatio_elliptic`); `χ(P) = closed form` (that χ *equals* it, via
  the analytic construction / Jacobi triple product) is UNPROVED (bean `qou-wgnx`).

  **Value re-scope (2026-08-08).**  The closed form is on main and its NUMERIC value at the
  substrate is now COMPUTED, so "χ(P)'s value is open" is stale: `χ(P)|q₀` (proton pin) is a
  **pure unit-modulus phase**, `|χ| = 1` exactly, a `z`-dependent elliptic function — NOT a
  single real number and NOT the lift magnitude `r* = μ₃/c₃ ≈ 1.585`.  A unit phase cannot
  equal a real magnitude `> 1`, so the direct identity `χ(P) = r*` is a **scope-(a) negative**
  (witness `computations/qbeta/c1-chi-magnitude-vs-r-star.witness.json`, audit
  `2026-08-08-chi-p-magnitude-vs-r-star-evaluation.md`).  This does NOT refute `E = χ(P)`
  (the gauge argument never claimed χ(P) is the magnitude); the lift is *affine* in `E`
  (`factor_sa − (B·D⁻¹/A)·E`, `factor_sa ≤ 1`), so `r*` is a real functional of `E`, not `E`.
  What is now precisely open: the **phase→real-amplitude→lift bridge** — which real
  anti-self-adjoint `E` the unit-phase `χ(P)` supplies (a real `E` vs a complex phase is a
  genuine type tension) and whether it yields `r*` — plus the from-first-principles `∞`-side
  wild datum (bean `qou-vkg5`).  The cross-ratio's *value* is no longer the open item; the
  bridge is.

**The construction (Part 1, built on `QCharacter`).**  Each entry `P_{ij}` is a theta-quotient
q-character (RSZ pseudo-constant, `C1ConnectionPoles.thetaRatio_multiplier`): its σ_q-multiplier
is `c_{0,j}/c_{∞,i}` (`offBlock_multiplier`).  The genuinely new construction lemma
`crossRatio_conn_qInvariant` derives, straight from `IsQChar`, that the cross-ratio of the
four entries is **σ_q-invariant (elliptic) because the exponent multipliers cancel exactly**
(`(c₀₁/c∞₀)(c₀₀/c∞₁) = (c₀₀/c∞₀)(c₀₁/c∞₁)`).  This *constructs* the frame-free object's
ellipticity from the q-character algebra — the abstract reason `χ(P)` is theta-valued and
`C1ConnectionPoles.connRatio_elliptic` holds — confirming `χ(P)` (not any entry) is the
well-posed `E`-carrier.

**The sharpened wall (Parts 2–4).**  `E = χ(P)` is well-posed; deriving its VALUE is the open
keystone.  Part 2 proves the invariance of `χ(P)` and the gauge-movability of a bare entry
(so `E ≠ entry`).  Part 3 bridges to A3: since `E = χ(P)` is frame-free and `E ↦ factor` is
injective (`amplitude_injective`), the physical lift is a well-defined function of the
connection cross-ratio — so deriving `χ(P)` DOES pin the lift; what remains open is the
cross-ratio's *value*, whose `∞`-input is the slope-`½` wild datum (bean `qou-vkg5`) and
whose closed form is bean `qou-wgnx`.  Part 4 records the corrected open successor as a §3b
dependent conjecture `BirkhoffCrossRatioSuppliesAmplitude` with **NO instance**, carrying the
frame-free identity `E = χ(P)`, a **bar-odd** consistency clause (matching
`DTIndexAmplitudeE.amplitude_barOdd`), and the lift — aligned with the sibling's
`AmplitudeIsGaugeInvariantCrossRatio`.

**Honesty (STRICT — AGENTS.md §Axiomatization-is-NOT-a-Proof / §3b / §Strict Lean
Discipline).**  Every theorem is genuine algebra (a q-character multiplier law, a
multiplier-cancellation ellipticity, a gauge invariance, a gauge-movability, an injectivity
bridge), sorry-free, no `native_decide`, no trivial-true, no axiom.  The entry = q-character
bridge is a CITED RSZ model, stated conditionally, never a derivation of `E`'s value.  `E` is
never solved from `r*`/`μ₃`/`c₃`; *deriving* `χ(P)` is the goal, *choosing* it to hit `r*`
is the forbidden fit and is not done.  The carrier has **no instance**; `q₀`-derivation is
not routed through.

**Base ring (§7c).**  Parts 1–3 and the cross-ratio: generic `{K : Type*} [Field K]` (scalar
inverses genuinely required — the §7c `[Field K]` carve-out).  The lift/carrier reuse A3's
`[Field K] [LinearOrder K] [IsStrictOrderedRing K]` (the `> 1` ordering is genuinely
archimedean).  No `ℝ`, no `Real.*`; the numerics live only in the Python witness / audit.

## References

- [ramis-sauloy-zhang-2013] https://arxiv.org/abs/0903.0853 (q-characters, connection matrix,
  isoformal classification).
- [leitner2026] `QOU.MathlibExt.QCharacter` (`IsQChar`, `IsQChar.ratio_qInvariant`);
  `QOU.QBeta.A3AntiSelfAdjointLift` (`amplitude_nonzero`, `amplitude_surjective`,
  `amplitude_injective`, `evenFaceCorrection`, `crossTerm`);
  `QOU.QBeta.BirkhoffAmplitudeWellPosed` (`AmplitudeIsGaugeInvariantCrossRatio`,
  `entry_not_gauge_invariant`, `gauge_fixes_all_iff` — the well-posedness result this file
  converges with); `QOU.QBeta.StokesAmplitudeE`;
  `QOU.QBeta.C1FuchsianExponents` / `C1ZeroSideExponents`;
  `QOU.QBeta.C1ConnectionPoles` (`connRatio_elliptic`, `thetaRatio_multiplier`, the
  cross-ratio `χ`); `conj:qdifference-kernel-prolongation-symbol`; the audits
  `2026-08-01-branch-selection-birkhoff-connection-matrix.md`,
  `2026-08-08-rsz-c1-infinity-route-closed.md`, `2026-08-08-stokes-amplitude-e-local-wall.md`;
  beans `qou-wiub`, `qou-wgnx`, `qou-jqof`, `qou-vkg5`.
-/

noncomputable section

namespace QOU.QBeta.BirkhoffAmplitudeE

open QOU.QBeta.A3AntiSelfAdjointLift
open QOU.MathlibExt.QCharacter

/-! ### Part 1 — CONSTRUCTION: the connection cross-ratio is elliptic because the exponent
multipliers cancel.

Each entry `P_{ij}` of `P = (X^{(∞)})⁻¹ X^{(0)}` is a theta-quotient q-character (the RSZ
pseudo-constant, `C1ConnectionPoles.thetaRatio_multiplier`) with σ_q-multiplier
`c_{0,j}/c_{∞,i}` — the `0`-exponent of column `j` over the `∞`-exponent of row `i`.  Built on
`QCharacter.IsQChar`. -/

/-- **An off-block entry's σ_q-multiplier is the exponent ratio `c₀/c∞` (sorry-free).**  If a
    `0`-side component is a q-character (multiplier `c₀`) and an `∞`-side component a
    q-character (multiplier `c∞`), their ratio — the connection off-block model — satisfies
    `h(q·x) = (c₀/c∞)·h(x)` unconditionally in a field.  Amplitude-level content of
    `C1ConnectionPoles.thetaRatio_multiplier` for a ratio of two *different* exponents. -/
theorem offBlock_multiplier {K : Type*} [Field K] {q c0 cinf : K} {f g : K → K}
    (hf : IsQChar q c0 f) (hg : IsQChar q cinf g) (x : K) :
    f (q * x) / g (q * x) = (c0 / cinf) * (f x / g x) := by
  rw [hf x, hg x, mul_div_mul_comm]

/-- **The CONSTRUCTION lemma — the connection cross-ratio is σ_q-invariant (elliptic) because
    the exponent multipliers cancel (sorry-free).**  Let the four entries `P₀₀,P₀₁,P₁₀,P₁₁`
    be q-characters with multipliers `c₀₀,c₀₁,c₁₀,c₁₁`.  For a genuine connection matrix the
    multipliers are `c_{ij} = c_{0,j}/c_{∞,i}`, which satisfy the **balance**
    `c₀₁·c₁₀ = c₀₀·c₁₁` (both equal `c₀₀c₀₁/(c∞₀c∞₁)`).  Then the cross-ratio
    `χ(P) = P₀₁P₁₀/(P₀₀P₁₁)` is `q`-invariant: its σ_q-multiplier is `(c₀₁c₁₀)/(c₀₀c₁₁) = 1`.

    This *constructs* the frame-free object's ellipticity directly from the q-character
    algebra — the abstract reason `χ(P)` is theta-valued and `C1ConnectionPoles.connRatio_elliptic`
    holds — and singles out the cross-ratio (not any entry) as the well-posed `E`-carrier. -/
theorem crossRatio_conn_qInvariant {K : Type*} [Field K] {q c00 c01 c10 c11 : K}
    {P00 P01 P10 P11 : K → K}
    (h00 : IsQChar q c00 P00) (h01 : IsQChar q c01 P01)
    (h10 : IsQChar q c10 P10) (h11 : IsQChar q c11 P11)
    (hbal : c01 * c10 = c00 * c11) (h00ne : c00 ≠ 0) (h11ne : c11 ≠ 0) :
    QInvariant q (fun x => (P01 x * P10 x) / (P00 x * P11 x)) := by
  intro x
  show (P01 (q * x) * P10 (q * x)) / (P00 (q * x) * P11 (q * x))
      = P01 x * P10 x / (P00 x * P11 x)
  rw [h00 x, h01 x, h10 x, h11 x,
      show c01 * P01 x * (c10 * P10 x) = (c01 * c10) * (P01 x * P10 x) by ring,
      show c00 * P00 x * (c11 * P11 x) = (c00 * c11) * (P00 x * P11 x) by ring,
      hbal, mul_div_mul_left _ _ (mul_ne_zero h00ne h11ne)]

/-- **The connection multipliers `c_{ij} = c_{0,j}/c_{∞,i}` satisfy the balance
    `c₀₁·c₁₀ = c₀₀·c₁₁` (sorry-free).**  So `crossRatio_conn_qInvariant` applies to any genuine
    connection matrix: the ellipticity of `χ(P)` is automatic from the exponent structure, not
    an extra hypothesis.  Both sides equal `c₀₀c₀₁/(c∞₀c∞₁)`. -/
theorem connMultiplier_balance {K : Type*} [Field K] (x0 x1 y0 y1 : K) :
    (x1 / y0) * (x0 / y1) = (x0 / y0) * (x1 / y1) := by
  ring

/-- **Resonance `c₀ = c∞` ⇒ an off-block entry is itself elliptic (sorry-free).**  When the two
    exponents agree the multiplier is `1`, so the entry is σ_q-invariant — `IsQChar.ratio_qInvariant`.
    A generic connection entry is *non-resonant* (`c₀ ≠ c∞`), hence genuinely quasi-periodic;
    only the balanced cross-ratio, not the entry, is elliptic. -/
theorem offBlock_elliptic_of_resonant {K : Type*} [Field K] {q c : K} {f g : K → K}
    (hf : IsQChar q c f) (hg : IsQChar q c g) (hc : c ≠ 0) :
    QInvariant q (fun x => f x / g x) :=
  hf.ratio_qInvariant hg hc

/-! ### Part 2 — WELL-POSEDNESS: the cross-ratio is the invariant; a bare entry is not.

Independent confirmation of the sibling `BirkhoffAmplitudeWellPosed.lean`.  Under the
diagonal normalization gauge `P_{ij} ↦ (d_{∞,i})⁻¹ P_{ij} d_{0,j}` the cross-ratio is
invariant while a bare entry is free — so a frame-free scalar (`E`, by
`amplitude_injective`) must be the cross-ratio, never an entry. -/

/-- The frame-free **connection cross-ratio** `χ(P) = P₀₁P₁₀/(P₀₀P₁₁)` (sibling convention;
    reciprocal of `C1ConnectionPoles`'s `P₀₀P₁₁/(P₀₁P₁₀)`), on entries `(a,b,c,d) =
    (P₀₀,P₀₁,P₁₀,P₁₁)`. -/
def crossRatio {K : Type*} [Field K] (a b c d : K) : K := b * c / (a * d)

/-- **`χ(P)` is invariant under the diagonal normalization gauge (sorry-free).**  Rescaling
    the two bases, `P_{ij} ↦ (d_{∞,i})⁻¹ P_{ij} d_{0,j}` with `d_∞ = (u,v)`, `d_0 = (s,t)`,
    sends `(a,b,c,d)` to `(u⁻¹s·a, u⁻¹t·b, v⁻¹s·c, v⁻¹t·d)`; the four gauge scalars cancel. -/
theorem crossRatio_gauge_invariant {K : Type*} [Field K] (a b c d s t u v : K)
    (hs : s ≠ 0) (ht : t ≠ 0) (hu : u ≠ 0) (hv : v ≠ 0) :
    crossRatio (u⁻¹ * s * a) (u⁻¹ * t * b) (v⁻¹ * s * c) (v⁻¹ * t * d)
      = crossRatio a b c d := by
  unfold crossRatio
  field_simp

/-- **A bare entry is gauge-MOVABLE, hence ill-posed as `E` (sorry-free).**  For a base entry
    `b ≠ 0` and ANY nonzero target `e`, a diagonal gauge (here `s = u = v = 1`, `t = e·b⁻¹`)
    sends the entry to `e` while leaving `χ(P)` invariant.  A single entry therefore carries
    no frame-free content: it cannot be the value of the physical scalar `E`.  (Sibling:
    `entry_not_gauge_invariant`.) -/
theorem entry_gauge_movable {K : Type*} [Field K] (a b c d : K) (hb : b ≠ 0) (e : K)
    (he : e ≠ 0) :
    ∃ s t u v : K, s ≠ 0 ∧ t ≠ 0 ∧ u ≠ 0 ∧ v ≠ 0 ∧
      u⁻¹ * t * b = e ∧
      crossRatio (u⁻¹ * s * a) (u⁻¹ * t * b) (v⁻¹ * s * c) (v⁻¹ * t * d) = crossRatio a b c d := by
  refine ⟨1, e * b⁻¹, 1, 1, one_ne_zero, mul_ne_zero he (inv_ne_zero hb),
    one_ne_zero, one_ne_zero, ?_, ?_⟩
  · rw [inv_one, one_mul, mul_assoc, inv_mul_cancel₀ hb, mul_one]
  · exact crossRatio_gauge_invariant a b c d 1 (e * b⁻¹) 1 1
      one_ne_zero (mul_ne_zero he (inv_ne_zero hb)) one_ne_zero one_ne_zero

/-- **Distinct bare entries share one cross-ratio (sorry-free).**  Two nonzero entry values
    `e₁, e₂` are realized by diagonal gauges of the *same* base connection, both leaving
    `χ(P) = crossRatio a b c d` unchanged.  A bare entry thus fails to be a well-posed
    functional (many entries ↦ one invariant); the frame-free `E` is the invariant, not the
    entry. -/
theorem distinct_entries_share_crossRatio {K : Type*} [Field K] (a b c d : K) (hb : b ≠ 0)
    (e₁ e₂ : K) (h1 : e₁ ≠ 0) (h2 : e₂ ≠ 0) :
    ∃ (s₁ t₁ u₁ v₁ s₂ t₂ u₂ v₂ : K),
      (u₁⁻¹ * t₁ * b = e₁) ∧ (u₂⁻¹ * t₂ * b = e₂) ∧
      crossRatio (u₁⁻¹ * s₁ * a) (u₁⁻¹ * t₁ * b) (v₁⁻¹ * s₁ * c) (v₁⁻¹ * t₁ * d)
        = crossRatio (u₂⁻¹ * s₂ * a) (u₂⁻¹ * t₂ * b) (v₂⁻¹ * s₂ * c) (v₂⁻¹ * t₂ * d) := by
  obtain ⟨s₁, t₁, u₁, v₁, _, _, _, _, hb₁, hχ₁⟩ := entry_gauge_movable a b c d hb e₁ h1
  obtain ⟨s₂, t₂, u₂, v₂, _, _, _, _, hb₂, hχ₂⟩ := entry_gauge_movable a b c d hb e₂ h2
  exact ⟨s₁, t₁, u₁, v₁, s₂, t₂, u₂, v₂, hb₁, hb₂, by rw [hχ₁, hχ₂]⟩

/-! ### Part 3 — the bridge to the A=3 keystone: deriving `χ(P)` PINS the lift; only its value is open. -/

/-- **The lift is a well-defined, injective function of the connection cross-ratio
    (sorry-free).**  If the frame-free amplitude is the cross-ratio value, `E = χval`, then the
    even-face lift factor `evenFaceCorrection A (crossTerm B (Csa + E) D)` is determined by
    `χval`; and by `A3AntiSelfAdjointLift.amplitude_injective` distinct factors force distinct
    cross-ratio values.  So — opposite to a gauge-blind entry — DERIVING `χ(P)` pins the A=3
    lift with no residual ambiguity.  What remains open is the cross-ratio's *value*, not its
    role.  (This is the corrected bridge: `E = χ(P)`, well-posed, converging with
    `BirkhoffAmplitudeWellPosed`.) -/
theorem lift_injective_in_crossRatio {K : Type*} [Field K] (A B D Csa χ₁ χ₂ : K)
    (hA : A ≠ 0) (hB : B ≠ 0) (hD : D ≠ 0)
    (hfac : evenFaceCorrection A (crossTerm B (Csa + χ₁) D)
          = evenFaceCorrection A (crossTerm B (Csa + χ₂) D)) : χ₁ = χ₂ :=
  amplitude_injective A B D Csa χ₁ χ₂ hA hB hD hfac

/-- **A derived cross-ratio value reaches the lift only by derivation, never by fit
    (sorry-free).**  `A3AntiSelfAdjointLift.amplitude_surjective` at the cross-ratio level:
    every target factor `r` is hit by some cross-ratio value `E = χval`.  Combined with
    `lift_injective_in_crossRatio`, the map `χval ↦ factor` is a bijection — so the lift is
    pinned exactly when `χ(P)` is *derived* (bean `qou-wgnx`); *choosing* `χval` to land `r*`
    is the forbidden fit (witness `χval = (factor_sa − r)·A·D·B⁻¹`, anchor-inverted). -/
theorem lift_reachable_by_crossRatio {K : Type*} [Field K] (A B D Csa r : K)
    (hA : A ≠ 0) (hB : B ≠ 0) (hD : D ≠ 0) :
    ∃ χval : K, evenFaceCorrection A (crossTerm B (Csa + χval) D) = r :=
  amplitude_surjective A B D Csa r hA hB hD

/-! ### Part 4 — the OPEN successor, as an honest §3b dependent conjecture (no instance).

Corrects `StokesAmplitudeE.GlobalBirkhoffSuppliesAmplitude` (whose `multislope` necessary
condition is C1-inapplicable — C1's `∞` is single-slope, `rszIsoformalDim = 0`) and aligns
with `BirkhoffAmplitudeWellPosed.AmplitudeIsGaugeInvariantCrossRatio`: `E` is the frame-free
cross-ratio `χ(P)`, its value the open datum. -/

/-- **§3b dependent conjecture — the A=3 amplitude `E` is the frame-free, bar-odd cross-ratio
    of the GLOBAL Birkhoff connection matrix, and drives the lift.**

    `@conjecture: dependent` (its content depends on the OPEN value of `χ(P)` — the analytic
    theta closed form of the `0↔∞` cross-ratio, whose `∞`-input is C1's slope-`½` wild
    normalization; beans `qou-wgnx`, `qou-vkg5`).

    **Content-bearing, not self-assuming.**  `zero_exponent` carries the DETERMINED `0`-side
    Fuchsian datum (a root of C1's indicial equation — a real INPUT).  `infinity_exponent_open`
    records the single missing INPUT (a nonzero `∞`-exponent distinct from `c₀`, non-resonant so
    the entries are genuine theta amplitudes by `offBlock_multiplier`).  `amplitude_is_crossRatio`
    is the well-posed frame-free identity `E = χ(P)` (from the sibling: `E` frame-free
    (`amplitude_injective`) ⇒ `E` is the unique gauge invariant).  `bar_odd` is the consistency
    clause `σ E = −E` under the bar involution (matching `DTIndexAmplitudeE.amplitude_barOdd`).
    `gives_lift` carries the physical lift as a hypothesis.

    **No instance is supplied.**  Deriving `χ(P)`'s value from the analytic construction is the
    open successor; discharging this by *choosing* `E = χ(P)` to hit `κ`
    (`lift_reachable_by_crossRatio`) is the forbidden fit and is not done. -/
class BirkhoffCrossRatioSuppliesAmplitude {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] (σ : K →+* K)
    (q A B D Csa : K) (P00 P01 P10 P11 E κ : K) : Prop where
  /-- The DETERMINED `0`-side Fuchsian exponent: a root of C1's indicial equation
      `c₀² + (q−1)c₀ + (q−1) = 0` (`C1FuchsianExponents`, `C1ZeroSideExponents`). -/
  zero_exponent : ∃ c0 : K, c0 ^ 2 + (q - 1) * c0 + (q - 1) = 0
  /-- The single OPEN datum: a nonzero `∞`-side exponent distinct from the `0`-exponent
      (non-resonant ⇒ genuine theta entries), supplied by the slope-`½` wild construction that
      is not yet built (bean `qou-vkg5`). -/
  infinity_exponent_open :
    ∃ c0 cinf : K, c0 ^ 2 + (q - 1) * c0 + (q - 1) = 0 ∧ cinf ≠ 0 ∧ cinf ≠ c0
  /-- **Well-posed frame-free identity:** `E` is the cross-ratio of the connection matrix, the
      unique gauge invariant (`crossRatio_gauge_invariant` + `entry_gauge_movable`), never an
      entry (from `amplitude_injective`; sibling `AmplitudeIsGaugeInvariantCrossRatio`). -/
  amplitude_is_crossRatio : E = crossRatio P00 P01 P10 P11
  /-- **Bar-odd consistency:** the cross-ratio is bar-odd under the involution `σ`
      (`σ E = −E`), matching `DTIndexAmplitudeE.amplitude_barOdd`. -/
  bar_odd : σ E = -E
  /-- `E` is nonzero (forced by the strict lift via `amplitude_nonzero`)... -/
  amplitude_nonzero : E ≠ 0
  /-- ...and drives the even-face correction to the physical lift `κ > 1` (unreachable by the
      self-adjoint branching Schur complement, `A3OffBlockDerivation.magnitudeFactor_le_one`). -/
  gives_lift : evenFaceCorrection A (crossTerm B (Csa + E) D) = κ ∧ 1 < κ

end QOU.QBeta.BirkhoffAmplitudeE
