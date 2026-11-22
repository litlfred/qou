import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds
import Mathlib.Topology.Algebra.Order.Field
import Mathlib.Order.Filter.AtTopBot.Basic
import Mathlib.Tactic

/-!
# QOU.QBeta.Stokes3LargeOrderAmplitude — the resurgent large-order route to `A_ω`

The GGM integer Stokes constant `A_ω = 3` of the figure-eight `4₁` is established
**algebraically** by the state-integral / 3d-index
(`computations/probes/qbeta_g3_ggm_stokes_41.py`, `S⁺(q→0) = [[1,3],[0,1]]`,
exact) and as the exact q-independent **symmetry constant**
(`QOU.QBeta.StokesSymmetryConstant`). This file formalizes the *resurgence
large-order* route probed in
`computations/qbeta/qbeta_stokes3_largeorder_amplitude_probe.py` (+ `_fit.py`),
which splits `A_ω` into two objects that must not be conflated:

* the **instanton ACTION** `A` — the Borel-plane singularity *location* (the
  denominator of the factorial growth `κ_n ~ P·Γ(n+β)/A^{n+β}`), and
* the **Stokes CONSTANT** — the *amplitude* `P` of that singularity.

**What the 12-order probe found (honest).**

* **ACTION — clean confirmation.** The ratio law `κ_{n+1}/κ_n = (n+β)/A` gives,
  via a ratio-slope fit AND the Aitken-accelerated `A_n = n·κ_n/κ_{n+1}`, a
  single **real, positive** Borel singularity at `A = Vol(4₁)/π ≈ 0.6461` to
  ~0.3%. `A_n` rises **monotonically** (0.55 → 0.64), and the Borel–Padé leading
  pole is real (`arg = 0`). This **sharpens** the 6-order 2026-07-07 reading
  ("action complex / oscillating / preliminary") to "action = Vol/π, real": the
  earlier apparent conjugate-pair oscillation was a two-term low-order transient.
* **AMPLITUDE — honest negative.** With `A = Vol/π`, the large-order amplitude
  `2πP → ≈ 1` (O(1)), **not** the integer `3`, in any natural normalization. So
  the naive large-order route does **not** independently reproduce the GGM `3`;
  the `A_ω = 3` identification stays the **state-integral algebraic** statement
  (consistent with the corpus position that the derivation route is the exact
  GGM state-integral, not float extraction from finitely many rungs).

Two honest Lean layers below:

* **Provable, sorry-free:**
  - `amplitude_extraction_single` — the extraction machinery: if a tower is
    governed by a single singularity (`κ n = P·g n·(1+ε n)`, `ε → 0`), the
    functional `κ n / g n → P`.
  - `action_recip_tendsto` — conditional on the (open) `GeometricKappaAction`
    carrier, derives the reciprocal action limit `κ_{n+1}/(n·κ_n) → A⁻¹` by
    inverting the action limit (a genuine derivation from the class field).
  - `cos_envelope`, `cos_ratio_le_one` — the conjugate-pair envelope bound that
    the data *ruled out* (had the singularity been a genuine `±𝔙` pair, the
    amplitude would have oscillated within `|P|`; instead it is monotone).

* **Open, content-bearing carrier** (NO instance ⇒ open; NOT `True`, NOT
  `native_decide`, NO fabricated instance): `GeometricKappaAction` asserts that
  the derived `4₁` geometric κ-tower's action limit `n·κ_n/κ_{n+1} → A` (with
  `A = Vol/π` numerically). This is the numerically-confirmed-but-unproved
  resurgent action; the amplitude `= 3` is deliberately **not** asserted (the
  probe refutes it at the naive normalization).

**Anti-laundering (explicit).** Nothing here derives `3` from the categorical
drivers, and nothing claims the resurgent amplitude identification is closed.
Base ring is `ℝ` (archimedean: `Real.cos`, order, limits).

-- Ref: [garoufalidis-gu-marino2021] GGM 2012.00062 (Stokes constant 3; eq 46/60)
-- Ref: [leitner2026] docs/audits/2026-08-01-stokes3-largeorder-amplitude-41.md
-/

namespace QOU.QBeta.Stokes3LargeOrderAmplitude

open Filter Topology

/-! ## Provable layer 1 — single-singularity amplitude extraction -/

/-- **Amplitude extraction (single singularity).** If a tower factors as
`κ n = P · g n · (1 + ε n)` with `g n ≠ 0` and subleading corrections `ε n → 0`,
then the amplitude functional `κ n / g n` converges to the amplitude `P`. The
exact statement that the large-order amplitude recovers `P` **when** a single
Borel singularity governs the growth. -/
theorem amplitude_extraction_single
    (P : ℝ) (κ g ε : ℕ → ℝ) (hg : ∀ n, g n ≠ 0)
    (hε : Tendsto ε atTop (𝓝 0))
    (hκ : ∀ n, κ n = P * g n * (1 + ε n)) :
    Tendsto (fun n => κ n / g n) atTop (𝓝 P) := by
  have hfun : (fun n => κ n / g n) = (fun n => P * (1 + ε n)) := by
    funext n
    rw [hκ n]
    field_simp [hg n]
  rw [hfun]
  have h1 : Tendsto (fun n => (1 : ℝ) + ε n) atTop (𝓝 (1 + 0)) :=
    tendsto_const_nhds.add hε
  have h2 : Tendsto (fun n => P * (1 + ε n)) atTop (𝓝 (P * (1 + 0))) :=
    h1.const_mul P
  simpa using h2

/-! ## Provable layer 2 — the conjugate-pair envelope (the ruled-out case) -/

/-- **Conjugate-pair envelope bound.** A single conjugate-pair contribution
`A_amp · cos(θ n)` (`A_amp ≥ 0`) never exceeds its envelope `A_amp`. Had the `4₁`
leading singularity been a genuine `±𝔙` pair, such a term would make the
amplitude oscillate; the 12-order data instead shows a single real singularity
(monotone `A_n`), so this documents the alternative the probe **ruled out**. -/
theorem cos_envelope (A_amp : ℝ) (hA : 0 ≤ A_amp) (θ : ℕ → ℝ) (n : ℕ) :
    |A_amp * Real.cos (θ n)| ≤ A_amp := by
  rw [abs_mul, abs_of_nonneg hA]
  have hc : |Real.cos (θ n)| ≤ 1 := Real.abs_cos_le_one _
  nlinarith [hc, hA, abs_nonneg (Real.cos (θ n))]

/-- The normalized cosine ratio is bounded by `1` (companion to `cos_envelope`:
`A_amp` is the tight envelope of the oscillation). -/
theorem cos_ratio_le_one (θ : ℕ → ℝ) (n : ℕ) : |Real.cos (θ n)| ≤ 1 :=
  Real.abs_cos_le_one _

/-! ## Open layer — the resurgent action (content-bearing carrier) -/

/-- **OPEN conjecture-carrier.** The derived `4₁` geometric κ-tower's **action
limit** `n·κ_n/κ_{n+1} → A` exists and equals `A` — numerically `A = Vol(4₁)/π`
(this branch's probe, 12 orders, ~0.3%). Fields:

* `kpos` — the derived positivity of the Ohtsuki κ-tower;
* `hA` — the action is positive;
* `action_limit` — the action-extraction limit (the numerically-confirmed but
  unproved resurgent content).

The amplitude `= 3` is **deliberately not asserted** (the probe finds it `≈ 1`,
not `3`, so the GGM integer stays the state-integral algebraic value). NO
instance ⇒ open; the fields are genuine analytic content, not `True`. -/
class GeometricKappaAction (κ : ℕ → ℝ) (A : ℝ) : Prop where
  /-- the derived Ohtsuki κ-tower is positive -/
  kpos : ∀ n, 0 < κ n
  /-- the resurgent action is positive -/
  hA : 0 < A
  /-- the action-extraction limit `n·κ_n/κ_{n+1} → A` (numerically `Vol/π`) -/
  action_limit : Tendsto (fun n : ℕ => (n : ℝ) * κ n / κ (n + 1)) atTop (𝓝 A)

/-- **Conditional consequence (proved from the carrier).** If the resurgent
action holds, the reciprocal ratio `κ_{n+1}/(n·κ_n)` converges to `A⁻¹`. This
inverts the action limit — a genuine derivation of a *new* limit from the class
field (not a restatement), so the carrier is non-degenerate (§3b-cond item 5). -/
theorem action_recip_tendsto (κ : ℕ → ℝ) (A : ℝ)
    [inst : GeometricKappaAction κ A] :
    Tendsto (fun n : ℕ => κ (n + 1) / ((n : ℝ) * κ n)) atTop (𝓝 A⁻¹) := by
  have h := inst.action_limit.inv₀ (ne_of_gt inst.hA)
  exact h.congr (fun n => inv_div ((n : ℝ) * κ n) (κ (n + 1)))

/-- Two-sided interval bound `-A_amp ≤ A_amp * Real.cos (θ n) ∧ A_amp * Real.cos (θ n) ≤ A_amp`
for a conjugate-pair oscillation term with `0 ≤ A_amp`. -/
theorem cos_envelope_interval_bounds (A_amp : ℝ) (hA : 0 ≤ A_amp) (θ : ℕ → ℝ) (n : ℕ) :
    -A_amp ≤ A_amp * Real.cos (θ n) ∧ A_amp * Real.cos (θ n) ≤ A_amp :=
  abs_le.mp (cos_envelope A_amp hA θ n)

end QOU.QBeta.Stokes3LargeOrderAmplitude
