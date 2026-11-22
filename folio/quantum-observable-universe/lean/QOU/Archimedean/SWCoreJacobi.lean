/-
# Closed-form Jacobi data for the Stieltjes–Wigert core (KSel-2-ID A-1)

The u ≡ 1 promotion audit
(`docs/audits/2026-08-01-ksel2id-u1-promotion.md` §1.1) computed, by the
qd algorithm on the SW moment sequence `G_k = v^{k(k−1)/2}` (the moments
of the log-normal `LN(−L/2, L)`, `L = ln v`, `v = q̃ = √q` — Stieltjes'
1894 indeterminate example, which the KSel-2-ID factorization identifies
as the indeterminacy core of the balanced binding kernel), the classical
Stieltjes–Wigert / q-Laguerre three-term recurrence

    α_k = v^{k−1}(v^k(1+v) − 1),      β_{k+1} = v^{3k}(v^{k+1} − 1).

That was tier **exact-symbolic (probe)**. This module proves it in Lean,
sorry-free, over a generic field, at general `n` — the same shape as the
carrier induction of `QOU.Archimedean.BalancedCarrierJacobi`:

* `swVec_eq_closed_form` — THE MAIN INDUCTION: the full iterated Jacobi
  vector in closed form,

      (Mⁿe₀)_i = v^{C(n,2) + 2·C(i,2)} · ∏_{j=1}^{i}(v^{m+j} − 1),
      n = i + m,

  with the rising product `vRise` (conjectured from the symbolic sweep,
  proved here at general `n`, `i`);
* `swVec_zero_eq_swMoment` — its `i = 0` corollary: `(Mⁿ)₀₀ = v^{C(n,2)}
  = G_n`, i.e. **the displayed `α`, `β` really are the Jacobi data of the
  SW moment sequence** — the A-1 claim, now machine-checked rather than
  read off a symbolic sweep at finite depth;
* `vRise_eq_qRise` — the bridge `∏(v^{m+j} − 1) = (v−1)^i · [m+1]_v⋯[m+i]_v`
  to the carrier machinery: the SW closed form is the carrier closed form
  with the q-integers rescaled by `(v−1)`, which is why the two frames
  share a lattice class;
* `swBeta_one_eq_zero` / `swMoment_one` — the `q → 1` degeneration: at
  `v = 1` every off-diagonal vanishes and all moments are `1`, i.e. the
  SW Gaussian collapses to the point mass at `1` (the confluent limit is
  degenerate on this factor — the archimedean content lives in the
  Jackson factor, cf. `SWJacksonMomentFactorization`).

NOT proved here (unchanged, per the audit's honest gap list): that the
`G_k` are the moments of an actual measure (Mathlib gap, bean `qou-jbo8`);
the Nevanlinna `D = c₀·z·A_{ṽ}` identification (numeric-functional tier);
the zero-asymptotics `ζ_n = v^{2n−1}(1 + O(v^{−n}))` (measured tier); and
the perturbation lemma transferring the lattice class from the SW core to
the balanced family (the named A-7 gap).

Base ring (§7c): generic `[Field K]` — the recurrence and the closed form
are rational identities in `v`; no ordering, no `Real.sqrt` (the
half-variable enters as the formal `v`, not as `Real.sqrt q`).

-- Ref: [leitner2026] docs/audits/2026-08-01-ksel2id-u1-promotion.md §1.1;
--      docs/audits/2026-08-01-ksel2id-friedrichs-sw-identification.md §1;
--      [christiansen2003sw] the SW moment problem; [moak1981] q-Laguerre.
-/

import QOU.Archimedean.BalancedCarrierJacobi

namespace QOU.Archimedean.SWCoreJacobi

open QOU.Mass.QDifferenceConfluentObstruction (qint)
open QOU.Archimedean.BalancedCarrierJacobi (qRise qRise_succ choose_two_succ)

variable {K : Type*} [Field K]

/-! ## The SW moment sequence and its Jacobi data -/

/-- **The SW core moment sequence** `G_n = v^{C(n,2)} = v^{n(n−1)/2}` —
the moments of the log-normal `LN(−L/2, L)` at `L = ln v`, i.e. the
Gaussian factor of the KSel-2-ID factorization
(`SWJacksonMomentFactorization.balancedNormalizer_mul_one_sub_pow`). -/
def swMoment (v : K) (n : ℕ) : K := v ^ (n.choose 2)

@[simp] theorem swMoment_zero (v : K) : swMoment v 0 = 1 := by
  simp [swMoment]

@[simp] theorem swMoment_one (v : K) : swMoment v 1 = 1 := by
  simp [swMoment]

/-- **SW Jacobi diagonal** `α_k = v^{k−1}(v^k(1+v) − 1)`, written
subtraction-free in the index (`α_0 = 1` is the `k = 0` value of the
displayed formula, whose `v^{−1}` cancels). -/
def swAlpha (v : K) : ℕ → K
  | 0 => 1
  | k + 1 => v ^ k * (v ^ (k + 1) * (1 + v) - 1)

/-- **SW Jacobi off-diagonal** — `swBeta v k` is `β_{k+1} = v^{3k}(v^{k+1} − 1)`,
index-shifted by one so that no `k − 1` appears. -/
def swBeta (v : K) (k : ℕ) : K := v ^ (3 * k) * (v ^ (k + 1) - 1)

@[simp] theorem swBeta_zero_val (v : K) : swBeta v 0 = v - 1 := by
  simp [swBeta]

/-- `q → 1` degeneration of the off-diagonal: at `v = 1` every `β`
vanishes — the SW Gaussian collapses to a point mass. -/
@[simp] theorem swBeta_one_eq_zero (k : ℕ) : swBeta (1 : K) k = 0 := by
  simp [swBeta]

/-- `q → 1` degeneration of the moments: `G_n ≡ 1`, the moments of `δ₁`. -/
@[simp] theorem swMoment_one_base (n : ℕ) : swMoment (1 : K) n = 1 := by
  simp [swMoment]

/-- One application of the monic Jacobi matrix `M` (diagonal `α_i`,
superdiagonal `1`, subdiagonal `β_i`) to a coordinate vector. -/
def swStep (v : K) (w : ℕ → K) : ℕ → K
  | 0 => swAlpha v 0 * w 0 + w 1
  | i + 1 => swBeta v i * w i + swAlpha v (i + 1) * w (i + 1) + w (i + 2)

/-- `swVec v n i = (Mⁿe₀)_i` — the iterated Jacobi vector. -/
def swVec (v : K) : ℕ → ℕ → K
  | 0 => fun i => match i with | 0 => 1 | _ + 1 => 0
  | n + 1 => swStep v (swVec v n)

@[simp] theorem swVec_zero_zero (v : K) : swVec v 0 0 = 1 := rfl

@[simp] theorem swVec_zero_succ (v : K) (i : ℕ) : swVec v 0 (i + 1) = 0 := rfl

theorem swVec_succ_zero (v : K) (n : ℕ) :
    swVec v (n + 1) 0 = swAlpha v 0 * swVec v n 0 + swVec v n 1 := rfl

theorem swVec_succ_succ (v : K) (n i : ℕ) :
    swVec v (n + 1) (i + 1)
      = swBeta v i * swVec v n i + swAlpha v (i + 1) * swVec v n (i + 1)
        + swVec v n (i + 2) := rfl

/-! ## The rising product `∏_{j=1}^{i}(v^{m+j} − 1)` -/

/-- `vRise v m i = (v^{m+1} − 1)(v^{m+2} − 1)⋯(v^{m+i} − 1)`. -/
def vRise (v : K) (m : ℕ) : ℕ → K
  | 0 => 1
  | i + 1 => vRise v m i * (v ^ (m + i + 1) - 1)

@[simp] theorem vRise_zero (v : K) (m : ℕ) : vRise v m 0 = 1 := rfl

theorem vRise_succ (v : K) (m i : ℕ) :
    vRise v m (i + 1) = vRise v m i * (v ^ (m + i + 1) - 1) := rfl

/-- Bottom extraction: `∏_{j=1}^{i+1}(v^{m+j} − 1)
= (v^{m+1} − 1)·∏_{j=1}^{i}(v^{m+1+j} − 1)`. -/
theorem vRise_succ_left (v : K) (m i : ℕ) :
    vRise v m (i + 1) = (v ^ (m + 1) - 1) * vRise v (m + 1) i := by
  induction i with
  | zero => rw [vRise_succ]; simp
  | succ i ih =>
      have e : m + 1 + i + 1 = m + (i + 1) + 1 := by omega
      rw [vRise_succ v m (i + 1), ih, vRise_succ v (m + 1) i, e]
      ring

/-- **Bridge to the carrier frame.** `∏_{j=1}^{i}(v^{m+j} − 1)
= (v − 1)^i · [m+1]_v⋯[m+i]_v`: the SW rising product is the carrier
rising q-factorial rescaled by `(v − 1)` per step. This is why the SW
closed form below and the carrier closed form of
`BalancedCarrierJacobi.jacobiVec_eq_closed_form` have the same shape. -/
theorem vRise_eq_qRise (v : K) (m : ℕ) :
    ∀ i, vRise v m i = (v - 1) ^ i * qRise v m i := by
  intro i
  induction i with
  | zero => simp
  | succ i ih =>
      have hgeom : v ^ (m + i + 1) - 1 = (v - 1) * qint v (m + i + 1) := by
        simp only [qint]
        linear_combination -geom_sum_mul v (m + i + 1)
      rw [vRise_succ, ih, qRise_succ, hgeom]
      ring

/-! ## Vanishing above the diagonal -/

theorem swVec_eq_zero_of_lt (v : K) : ∀ n i, n < i → swVec v n i = 0 := by
  intro n
  induction n with
  | zero =>
      intro i h
      obtain ⟨i', rfl⟩ : ∃ i', i = i' + 1 := ⟨i - 1, by omega⟩
      rfl
  | succ n ih =>
      intro i h
      obtain ⟨i', rfl⟩ : ∃ i', i = i' + 1 := ⟨i - 1, by omega⟩
      rw [swVec_succ_succ, ih i' (by omega), ih (i' + 1) (by omega),
        ih (i' + 2) (by omega)]
      ring

/-! ## The main induction -/

/-- **THE MAIN INDUCTION (general `n`, `i`; sorry-free).** The closed form
for the iterated Jacobi vector of the SW data:

    (Mⁿe₀)_i = v^{C(n,2) + 2·C(i,2)} · ∏_{j=1}^{i}(v^{m+j} − 1),  n = i + m.

Proved by induction on `n`; the four cases are `i = 0`, and `i+1` with
`m ∈ {0, 1, ≥2}` (the last two need one and two steps of bottom
extraction respectively). Conjectured from the audit's symbolic sweep
(depth ≤ 8); established here at every order. -/
theorem swVec_eq_closed_form (v : K) :
    ∀ n i m, n = i + m →
      swVec v n i = v ^ (n.choose 2 + 2 * i.choose 2) * vRise v m i := by
  intro n
  induction n with
  | zero =>
      intro i m h
      obtain ⟨rfl, rfl⟩ : i = 0 ∧ m = 0 := by omega
      simp
  | succ n ih =>
      intro i m h
      cases i with
      | zero =>
          obtain rfl : m = n + 1 := by omega
          rw [swVec_succ_zero]
          cases n with
          | zero => simp [swAlpha]
          | succ n' =>
              rw [ih 0 (n' + 1) (by omega), ih 1 n' (by omega)]
              simp only [swAlpha, vRise_zero, mul_one, one_mul, vRise_succ,
                show (0 : ℕ).choose 2 = 0 from rfl,
                show (1 : ℕ).choose 2 = 0 from rfl, mul_zero, add_zero]
              rw [choose_two_succ (n' + 1), pow_add]
              have e : n' + 0 + 1 = n' + 1 := by omega
              rw [e]
              ring
      | succ i' =>
          cases m with
          | zero =>
              have hn : n = i' := by omega
              subst hn
              rw [swVec_succ_succ, ih n 0 (by omega),
                swVec_eq_zero_of_lt v n (n + 1) (by omega),
                swVec_eq_zero_of_lt v n (n + 2) (by omega),
                choose_two_succ n, vRise_succ v 0 n]
              simp only [swBeta, mul_zero, add_zero]
              have e : 0 + n + 1 = n + 1 := by omega
              rw [e]
              have hex : n.choose 2 + 2 * n.choose 2 + 3 * n
                  = n + n.choose 2 + 2 * (n + n.choose 2) := by omega
              rw [show n.choose 2 + 2 * (n.choose 2) = n.choose 2 + 2 * n.choose 2
                from rfl]
              rw [← hex, pow_add]
              ring
          | succ m' =>
              cases m' with
              | zero =>
                  have hn : n = i' + 1 := by omega
                  subst hn
                  rw [swVec_succ_succ, ih i' 1 (by omega),
                    ih (i' + 1) 0 (by omega),
                    swVec_eq_zero_of_lt v (i' + 1) (i' + 2) (by omega),
                    vRise_succ_left v 0 i', vRise_succ v 1 i',
                    choose_two_succ (i' + 1), choose_two_succ i']
                  simp only [swAlpha, swBeta, vRise_zero, mul_one, add_zero]
                  ring
              | succ m'' =>
                  have hn : n = i' + (m'' + 1 + 1) := by omega
                  subst hn
                  have ha' : (i' + (m'' + 1 + 1) + 1).choose 2
                      = (i' + (m'' + 1 + 1)) + (i' + (m'' + 1 + 1)).choose 2 :=
                    choose_two_succ _
                  have hB2 : (i' + 1 + 1).choose 2 = (i' + 1) + (i' + 1).choose 2 :=
                    choose_two_succ (i' + 1)
                  have hA : (i' + 1).choose 2 = i' + i'.choose 2 := choose_two_succ i'
                  rw [swVec_succ_succ,
                    ih i' (m'' + 1 + 1) (by omega),
                    ih (i' + 1) (m'' + 1) (by omega),
                    ih (i' + 1 + 1) m'' (by omega),
                    vRise_succ_left v m'' (i' + 1),
                    vRise_succ_left v (m'' + 1) i',
                    vRise_succ v (m'' + 1 + 1) i',
                    ha', hB2, hA]
                  simp only [swAlpha, swBeta]
                  ring

/-- **A-1, the audit claim: the displayed `α`, `β` ARE the Jacobi data of
the SW moment sequence.** `(Mⁿ)₀₀ = v^{C(n,2)} = G_n` at every order —
the `i = 0` corollary of the main induction. -/
theorem swVec_zero_eq_swMoment (v : K) (n : ℕ) :
    swVec v n 0 = swMoment v n := by
  have h := swVec_eq_closed_form v n 0 n (by omega)
  simpa [swMoment, show (0 : ℕ).choose 2 = 0 from rfl] using h

end QOU.Archimedean.SWCoreJacobi
