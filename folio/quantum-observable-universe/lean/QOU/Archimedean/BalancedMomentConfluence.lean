/-
# Per-`n` balanced moment confluence — discharging the `hmom` hypothesis
# of `balanced_kernel_tendsto_schwinger`

The Lean tranche the merged `BalancedKernelConfluence` module named as its
own residual: the balanced q-Borel normalizer

  `N^bal_q(n) = q^{−(n−1)(n−2)/4} · [n−1]_q!`

(probe: `computations/probes/qborel_confluence_pos_probe.py`, audit:
`docs/audits/2026-07-25-qborel-confluence-pos-attack.md`) formalized, its
exact fibre algebra proved, and its archimedean `q → 1` limit
`N^bal_q(n) → (n−1)!` proved — which converts the merged theorem's
explicit moment-convergence hypothesis `hmom` into the balanced-moment
*representability* hypothesis (the conjecture's genuine (REP) content).

## The quarter-power formulation (honest choice, stated up front)

`q^{(n−1)(n−2)/4}` needs quarter-powers of `q`, which do not exist in a
generic field. The probe's own C4b split resolves this: work in the
half-variable `v = q^{1/2}` (the probe's `q̃ = √q`), where the exponent
`(n−1)(n−2)/4` in `q` becomes `(n−1)(n−2)/2 = C(n−1, 2)` in `v` — an
**integer** (`Nat.choose (n−1) 2`), since `(n−1)(n−2)` is a product of
consecutive integers. So:

* generic side (§7c, `Field K`, no `ℝ`): `balancedNormalizer v n :=
  (v^{C(n−1,2)})⁻¹ · [n−1]_{v²}!` — every exponent a natural number, no
  `rpow`, no ordering;
* archimedean side (`ℝ`): `balancedNormalizerR q n :=
  balancedNormalizer (√q) n`, which for `q > 0` is exactly
  `q^{−(n−1)(n−2)/4}·[n−1]_q!` since `(√q)^{C(n−1,2)} = q^{(n−1)(n−2)/4}`.

PROVED here (sorry-free):

* `pow_mul_qint_inv` / `pow_choose_mul_qfact_inv` — the bar transform of
  the q-integer and q-factorial: `q^k·[k+1]_{q⁻¹} = [k+1]_q` and
  `q^{C(m,2)}·[m]_{q⁻¹}! = [m]_q!` (exact fibre algebra, generic field).
* `balancedNormalizer_inv` — **bar-invariance** (the Attack-E repair, now
  Lean-exact, previously probe-only): `N^bal_{v⁻¹}(n) = N^bal_v(n)`.
* `sq_balancedNormalizer` — the geometric-mean identity
  `N^bal(n)² = [n−1]_{q}!·[n−1]_{q⁻¹}!` at `q = v²` (probe C1b), fully
  polynomial — the squared form needs no quarter-powers at all.
* `balancedNormalizer_succ` — the exact positive-kernel split (probe C4d):
  `N^bal(k+1) = [k]_{q⁻¹}!·v^{C(k,2)}`, i.e. `A(k)·B(k)` with
  `B(k) = q^{k(k−1)/4}` realized as the integer power `v^{k(k−1)/2}`.
* `tendsto_balancedNormalizerR` — **the per-`n` confluence limit**
  (archimedean): `N^bal_q(n) → (n−1)!` as `q → 1` — a finite product of
  terms continuous at `q = 1`, evaluated by `[k]_1 = k`.
* `balanced_kernel_tendsto_schwinger_of_confluence` — **the `hmom`
  discharge**: the merged conditional theorem restated with `hmom`
  replaced by (i) `qs → 1` and (ii) the balanced-moment representability
  `∫ s^k dK_j = N^bal_{q_j}(k+1)` — hypothesis (ii) is the conjecture's
  open (REP) content; the moment *convergence* is now proved, not
  assumed.
* `sum_c2_closed_form` — the quantitative `h²` coefficient's closed form
  `Σ_{k=1}^{n−1}(k²−1)/24 = (n−1)(n−2)(2n+3)/144` as exact finite-sum
  algebra over `ℚ` (probe C2's symbolic summation, now Lean-proved).

NOT proved here (the honest residual):

* the full quantitative asymptotic `log(N^bal_{e^h}(n)/(n−1)!) =
  c₂(n)h² + O(h⁴)` — needs `Real.log` power-series expansion machinery;
  carried as the content-bearing hypothesis class `BalancedH2Expansion`
  (probe-exact at every tested order, sympy; NO instance in this repo —
  fabricating one would violate §Axiomatization-is-NOT-a-Proof). Nothing
  downstream consumes it; the qualitative `hmom` discharge above needs
  only the proved limit.
* the two classical Mathlib-gap classes (Fréchet–Shohat, Carleman
  determinacy) — unchanged, inherited from `BalancedKernelConfluence`.
* the (REP) hypothesis itself — that the substrate's kernels carry the
  balanced moments; at `q ≠ 1` moments do not even pin the kernel
  (audit §3.1), so this needs derivation input beyond moments.

Base ring (§7c): the fibre algebra is generic `{K : Type*} [Field K]`
(inverses are algebraic, no ordering); only the confluence limit and the
`h²`-expansion class are wall-side `ℝ` (continuity, `Real.sqrt`,
`Real.exp`/`Real.log`).

-- Ref: [leitner2026] predicted-spectra, conj:schwinger-measure-computational-time;
--      computations/probes/qborel_confluence_pos_probe.py (C1, C2, C4);
--      docs/audits/2026-07-25-qborel-confluence-pos-attack.md §1-§2;
--      docs/audits/2026-07-25-balanced-moment-confluence-lean.md.
-/

import QOU.Mass.QDifferenceConfluentObstruction
import QOU.Archimedean.BalancedKernelConfluence
import Mathlib.Data.Real.Sqrt
import Mathlib.Analysis.SpecialFunctions.Log.Basic

namespace QOU.Archimedean.BalancedMomentConfluence

open Finset Filter Topology MeasureTheory
open QOU.Mass.QDifferenceConfluentObstruction (qint qfact)
open QOU.MathlibExt.FrechetShohat

/-! ## Fibre algebra (generic field — §7c: no `ℝ`, no ordering) -/

section Fibre

variable {K : Type*} [Field K]

/-- **Bar transform of the quantum integer.**
`q^k · [k+1]_{q⁻¹} = [k+1]_q` — the reflection `i ↦ k − i` of the
geometric sum, exact over any field with `q ≠ 0`. -/
theorem pow_mul_qint_inv (q : K) (hq : q ≠ 0) (k : ℕ) :
    q ^ k * qint q⁻¹ (k + 1) = qint q (k + 1) := by
  simp only [qint]
  rw [← Finset.sum_range_reflect (fun j => q ^ j) (k + 1), Finset.mul_sum]
  refine Finset.sum_congr rfl fun i hi => ?_
  rw [Finset.mem_range, Nat.lt_succ_iff] at hi
  rw [inv_pow, Nat.add_sub_cancel, pow_sub₀ q hq hi]

/-- **Bar transform of the q-factorial.**
`q^{C(m,2)} · [m]_{q⁻¹}! = [m]_q!` (`C(m,2) = m(m−1)/2 = Nat.choose m 2`):
the probe's exact identity `N_q(n) = q^{(n−1)(n−2)/2}·N_{q⁻¹}(n)` in
multiplied (division-free) form. -/
theorem pow_choose_mul_qfact_inv (q : K) (hq : q ≠ 0) (m : ℕ) :
    q ^ (m.choose 2) * qfact q⁻¹ m = qfact q m := by
  induction m with
  | zero => simp [qfact]
  | succ m ih =>
      have hchoose : (m + 1).choose 2 = m + m.choose 2 := by
        rw [Nat.choose_succ_succ, Nat.choose_one_right]
      calc q ^ ((m + 1).choose 2) * qfact q⁻¹ (m + 1)
          = (q ^ m * qint q⁻¹ (m + 1)) * (q ^ (m.choose 2) * qfact q⁻¹ m) := by
            rw [hchoose, pow_add,
              show qfact q⁻¹ (m + 1) = qint q⁻¹ (m + 1) * qfact q⁻¹ m from rfl]
            ring
        _ = qint q (m + 1) * qfact q m := by
            rw [pow_mul_qint_inv q hq m, ih]
        _ = qfact q (m + 1) := rfl

/-- **The balanced q-Borel normalizer in the half-variable** `v = q^{1/2}`:
`N^bal(n) = v^{−C(n−1,2)} · [n−1]_{v²}!`. For `v² = q` this is exactly the
probe's `q^{−(n−1)(n−2)/4}·[n−1]_q!` — the quarter-power of `q` is the
integer power `C(n−1,2) = (n−1)(n−2)/2` of `v`. -/
def balancedNormalizer (v : K) (n : ℕ) : K :=
  (v ^ ((n - 1).choose 2))⁻¹ * qfact (v ^ 2) (n - 1)

/-- **Bar-invariance of the balanced normalizer** (the Attack-E repair,
previously probe-only, now Lean-exact): the balanced form equals its
bar-transform, `N^bal_{v⁻¹}(n) = N^bal_v(n)`. At `q = v²` this is
bar-covariance `q ↦ q⁻¹` of the balanced q-Borel weight. -/
theorem balancedNormalizer_inv (v : K) (hv : v ≠ 0) (n : ℕ) :
    balancedNormalizer v⁻¹ n = balancedNormalizer v n := by
  have hv2 : (v ^ 2 : K) ≠ 0 := pow_ne_zero _ hv
  have hb := pow_choose_mul_qfact_inv (v ^ 2) hv2 (n - 1)
  unfold balancedNormalizer
  simp only [inv_pow, inv_inv]
  rw [← hb, ← pow_mul, two_mul, pow_add]
  field_simp

/-- **Geometric-mean (squared) factorization** (probe C1b):
`N^bal(n)² = [n−1]_{q}! · [n−1]_{q⁻¹}!` at `q = v²` — the balanced
normalizer is the geometric mean of the bar pair. The squared form is
fully polynomial in `q` and needs no quarter-powers at all. -/
theorem sq_balancedNormalizer (v : K) (hv : v ≠ 0) (n : ℕ) :
    balancedNormalizer v n ^ 2
      = qfact (v ^ 2) (n - 1) * qfact ((v ^ 2)⁻¹) (n - 1) := by
  have hv2 : (v ^ 2 : K) ≠ 0 := pow_ne_zero _ hv
  have hb := pow_choose_mul_qfact_inv (v ^ 2) hv2 (n - 1)
  unfold balancedNormalizer
  rw [← hb, ← pow_mul, two_mul, pow_add]
  field_simp

/-- **The exact positive-kernel split** (probe C4d / audit (i)):
`N^bal(k+1) = [k]_{q⁻¹}! · q^{k(k−1)/4}` with the half-weight factor
`q^{k(k−1)/4}` realized as the integer power `v^{C(k,2)}`
(`C(k,2) = k(k−1)/2`). This is the `A(k)·B(k)` factorization whose two
factors the probe realizes as manifestly positive kernels (Jackson
q-Gamma × theta/log-normal). -/
theorem balancedNormalizer_succ (v : K) (hv : v ≠ 0) (k : ℕ) :
    balancedNormalizer v (k + 1)
      = qfact ((v ^ 2)⁻¹) k * v ^ (k.choose 2) := by
  have hv2 : (v ^ 2 : K) ≠ 0 := pow_ne_zero _ hv
  have hb := pow_choose_mul_qfact_inv (v ^ 2) hv2 k
  unfold balancedNormalizer
  rw [Nat.add_sub_cancel, ← hb, ← pow_mul, two_mul, pow_add]
  field_simp

@[simp] theorem qint_one (k : ℕ) : qint (1 : K) k = (k : K) := by
  simp [qint]

@[simp] theorem qfact_one (m : ℕ) : qfact (1 : K) m = (m.factorial : K) := by
  induction m with
  | zero => simp [qfact]
  | succ m ih =>
      show qint (1 : K) (m + 1) * qfact (1 : K) m = _
      rw [qint_one, ih, Nat.factorial_succ]
      push_cast
      ring

/-- At `v = 1` (the confluence point `q = 1`) the balanced normalizer is
the classical `(n−1)!`. -/
@[simp] theorem balancedNormalizer_one (n : ℕ) :
    balancedNormalizer (1 : K) n = ((n - 1).factorial : K) := by
  simp [balancedNormalizer]

end Fibre

/-! ## Archimedean side (`ℝ` — wall-side by construction: continuity,
`Real.sqrt`) -/

/-- The real balanced normalizer in the substrate variable `q`:
`N^bal_q(n) = balancedNormalizer (√q) n`. For `q > 0` this is exactly
`q^{−(n−1)(n−2)/4}·[n−1]_q!` (the probe's normalizer), the quarter-powers
of `q` being integer powers of `√q`. -/
noncomputable def balancedNormalizerR (q : ℝ) (n : ℕ) : ℝ :=
  balancedNormalizer (Real.sqrt q) n

theorem continuous_qint (k : ℕ) : Continuous fun v : ℝ => qint v k := by
  simp only [qint]
  exact continuous_finset_sum _ fun i _ => continuous_pow i

theorem continuous_qfact (m : ℕ) : Continuous fun v : ℝ => qfact v m := by
  induction m with
  | zero =>
      show Continuous fun _ : ℝ => (1 : ℝ)
      exact continuous_const
  | succ m ih =>
      show Continuous fun v : ℝ => qint v (m + 1) * qfact v m
      exact (continuous_qint (m + 1)).mul ih

theorem continuousAt_balancedNormalizer {v : ℝ} (hv : v ≠ 0) (n : ℕ) :
    ContinuousAt (fun w : ℝ => balancedNormalizer w n) v := by
  simp only [balancedNormalizer]
  exact ((continuous_pow _).continuousAt.inv₀ (pow_ne_zero _ hv)).mul
    ((continuous_qfact _).comp (continuous_pow 2)).continuousAt

/-- **The per-`n` balanced moment confluence** (the audit-§2 qualitative
statement, PROVED): `N^bal_q(n) → (n−1)!` as `q → 1`. The normalizer is a
finite product of terms continuous at `q = 1` (each `[k]_q → k`), so the
limit is the evaluation `[n−1]_1! = (n−1)!`. -/
theorem tendsto_balancedNormalizerR (n : ℕ) :
    Tendsto (fun q : ℝ => balancedNormalizerR q n) (𝓝 1)
      (𝓝 ((n - 1).factorial : ℝ)) := by
  have h : ContinuousAt (fun q : ℝ => balancedNormalizerR q n) 1 := by
    have h2 : ContinuousAt (fun v : ℝ => balancedNormalizer v n) (Real.sqrt 1) := by
      rw [Real.sqrt_one]
      exact continuousAt_balancedNormalizer one_ne_zero n
    exact h2.comp Real.continuous_sqrt.continuousAt
  have hval : balancedNormalizerR (1 : ℝ) n = ((n - 1).factorial : ℝ) := by
    simp [balancedNormalizerR, Real.sqrt_one]
  simpa [hval] using h.tendsto

/-- Sequence form of the confluence: along any `qs → 1`,
`N^bal_{qs j}(n) → (n−1)!`. This is exactly the shape of the `hmom`
hypothesis of `balanced_kernel_tendsto_schwinger`. -/
theorem tendsto_balancedNormalizerR_seq {qs : ℕ → ℝ}
    (hqs : Tendsto qs atTop (𝓝 1)) (n : ℕ) :
    Tendsto (fun j => balancedNormalizerR (qs j) n) atTop
      (𝓝 ((n - 1).factorial : ℝ)) :=
  (tendsto_balancedNormalizerR n).comp hqs

/-! ## The quantitative `h²` layer -/

/-- **The `c₂(n)` closed-form sum identity** (probe C2's symbolic
summation, Lean-proved): with `m = n − 1`,
`Σ_{k=1}^{m} (k²−1)/24 = m(m−1)(2m+5)/144`, i.e.
`Σ_{k=1}^{n−1}(k²−1)/24 = (n−1)(n−2)(2n+3)/144` — Attack E's predicted
`h²` coefficient of `log(N^bal_{e^h}(n)/(n−1)!)`. Pure finite-sum algebra
over `ℚ`. -/
theorem sum_c2_closed_form (m : ℕ) :
    ∑ k ∈ Finset.range m, (((k : ℚ) + 1) ^ 2 - 1) / 24
      = (m : ℚ) * ((m : ℚ) - 1) * (2 * (m : ℚ) + 5) / 144 := by
  induction m with
  | zero => simp
  | succ m ih =>
      rw [Finset.sum_range_succ, ih]
      push_cast
      field_simp
      ring

/-- `n`-indexed form of `sum_c2_closed_form` for `n ≥ 1`:
`c₂(n) = Σ_{k=1}^{n−1}(k²−1)/24 = (n−1)(n−2)(2n+3)/144`. -/
theorem sum_c2_closed_form_of_one_le {n : ℕ} (hn : 1 ≤ n) :
    ∑ k ∈ Finset.range (n - 1), (((k : ℚ) + 1) ^ 2 - 1) / 24
      = ((n : ℚ) - 1) * ((n : ℚ) - 2) * (2 * (n : ℚ) + 3) / 144 := by
  obtain ⟨m, rfl⟩ := Nat.exists_eq_add_of_le hn
  rw [Nat.add_sub_cancel_left, sum_c2_closed_form]
  push_cast
  ring

/-- **The quantitative `h²` asymptotic (probe-exact, Lean-open) —
content-bearing hypothesis class, NO instance in this repo.** The probe
proves (sympy, exact rationals, every order tested through `h³`):
`log(N^bal_{e^h}(n)/(n−1)!) = c₂(n)·h² + O(h⁴)` with `h¹ = h³ = 0` and
`c₂(n) = (n−1)(n−2)(2n+3)/144` (the sum identity `sum_c2_closed_form`).
Formalizing the remainder bound needs `Real.log`/series-expansion
machinery out of scope this tranche; the class carries the statement so
any future consumer wears it in its type (§3b-cond). Fabricating an
instance would violate §Axiomatization-is-NOT-a-Proof. Nothing in this
file consumes it — the `hmom` discharge needs only the PROVED qualitative
limit `tendsto_balancedNormalizerR`. -/
class BalancedH2Expansion : Prop where
  expansion : ∀ n : ℕ, ∃ C : ℝ, 0 < C ∧ ∃ δ : ℝ, 0 < δ ∧
    ∀ h : ℝ, 0 < h → h < δ →
      |Real.log (balancedNormalizerR (Real.exp h) n / ((n - 1).factorial : ℝ))
          - (((n - 1) * (n - 2) * (2 * n + 3) : ℕ) : ℝ) / 144 * h ^ 2|
        ≤ C * h ^ 4

/-! ## The `hmom` discharge -/

/-- **Balanced-kernel weak convergence with `hmom` DISCHARGED** — the
corollary of the merged `balanced_kernel_tendsto_schwinger` in which the
bare moment-convergence hypothesis `hmom` is *replaced by the proved
per-`n` confluence*: if the kernels' Stieltjes moments are the balanced
normalizers at fibre parameters `qs j → 1` (hypothesis `hrep` — the
conjecture's open (REP) representability content), then the kernels
converge weakly to the unit Schwinger measure `e^{−s}·ds`, conditional
only on the two classical Mathlib-gap classes. The hypothesis surface
shrinks: moment *convergence* is now a theorem
(`tendsto_balancedNormalizerR_seq`); what remains is *representability*
(`hrep`) plus the two named classical theorems. -/
theorem balanced_kernel_tendsto_schwinger_of_confluence
    [FrechetShohatStieltjes] [CarlemanDeterminacyStieltjes]
    (K : ℕ → ProbabilityMeasure ℝ) (qs : ℕ → ℝ)
    (hqs : Tendsto qs atTop (𝓝 1))
    (hsupp : ∀ j, (K j : Measure ℝ) (Set.Iio 0) = 0)
    (hint : ∀ j k, Integrable (fun s : ℝ => s ^ k) (K j : Measure ℝ))
    (hrep : ∀ j k, ∫ s, s ^ k ∂(K j : Measure ℝ)
      = balancedNormalizerR (qs j) (k + 1)) :
    Tendsto K atTop (𝓝 schwingerProbabilityMeasure) := by
  refine QOU.Archimedean.BalancedKernelConfluence.balanced_kernel_tendsto_schwinger
    K hsupp hint fun k => ?_
  have h := tendsto_balancedNormalizerR_seq hqs (k + 1)
  rw [Nat.add_sub_cancel] at h
  simpa [hrep] using h

end QOU.Archimedean.BalancedMomentConfluence
