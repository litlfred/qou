/-
# Carrier Jacobi data of the balanced q-Borel moment functional — the
# q-deformed Gaussian, closed at general k

The KSel-2 queued induction (`docs/audits/2026-08-01-ksel2-gns-favard-canonicity.md`
§3 finding 2 + §5 item 1): the carrier frame of the binding moment problem — the
Lean-proved q-involution numerators `S_q(n)` (`S(0) = S(1) = 1`,
`S(n+2) = S(n+1) + [n+1]_q·S(n)`, the hypothesis of
`QOU.Mass.KeystoneBridgeC1Binding.keystone_bridge_binding_qlift`) read as a
Hamburger moment sequence — has monic Jacobi data

  `α_k = q^k`  (diagonal),   `β_k = q^{k−1}·[k]_q`  (k ≥ 1, off-diagonal),

a q-deformation of the Gaussian `N(1,1)` data `(α, β) = (1, k)`. The probe
(`computations/probes/ksel2_favard_jacobi_probe.py`, K1/K3) verified the
GNS moment-reproduction identity `(Mⁿ)₀₀ = S_q(n)` exactly for `n ≤ 12`
(symbolic q) — a verified-range identity, explicitly NOT a general-k proof.
This file closes it at **general k, sorry-free**, by proving a closed form for
the ENTIRE vector `Mⁿe₀`, not just its top entry:

  `(Mⁿe₀)_i = q^{C(i,2)} · [m+1]_q[m+2]_q⋯[m+i]_q · S_q(m)`,   `n = i + m`
  (and `(Mⁿe₀)_i = 0` for `i > n`),

where `M` is the semi-infinite monic Jacobi matrix of the data above (probe
convention `monic_jacobi_pow00`: diagonal `α_i`, superdiagonal `1`,
subdiagonal `β_i`). The induction consumes exactly two identities: the
q-integer splitting `[a+b]_q = [a]_q + q^a·[b]_q` and the S-recurrence — the
q-lift of Stein's characterization of the Gaussian, whose classical shadow
(`q = 1`: `α_k = 1`, `β_k = k`, moments = involution numbers = `N(1,1)`
moments) is also proved here.

PROVED here (sorry-free):

* `qint_add` — the q-integer splitting `[a+b]_q = [a]_q + q^a·[b]_q`
  (generic field, exact fibre algebra).
* `carrierMoment` + `carrierMoment_unique` — the carrier moment sequence
  `S_q(n)` (the q-involution recurrence of
  `keystone_bridge_binding_qlift`, concrete), and its uniqueness: any
  sequence with the same recurrence and initial values equals it.
* `jacobiVec_eq_closed_form` — **THE MAIN INDUCTION**: the full closed form
  for `Mⁿe₀` above, at general `n`, `i` (with `jacobiVec_eq_zero_of_lt` for
  the vanishing regime `i > n`).
* `jacobiVec_zero_eq_carrierMoment` / `jacobiVec_zero_eq_of_recurrence` —
  the general-`n` GNS moment identity `(Mⁿ)₀₀ = S_q(n)`: the canonical
  monic Jacobi operator with data `α_k = q^k`, `β_k = q^{k−1}[k]_q` has the
  carrier binding data as moments — for every `n`, no longer verified-range.
  (By uniqueness of the Jacobi data of a positive-definite moment functional
  — Favard, classical, cited in the audit — these therefore ARE the carrier
  Jacobi coefficients; the positivity leg is the probe's exact K3/K4.)
* `jacobiAlpha_q_one` / `jacobiBeta_q_one` / `carrierMoment_q_one_recurrence`
  / `carrierMoment_q_one` — the `q = 1` degeneration: `α_k → 1`,
  `β_k → k` (index-shifted: `jacobiBeta 1 k = k+1` is `β_{k+1}`), the
  recurrence degenerates to Stein's `S(n+2) = S(n+1) + (n+1)S(n)`, and the
  moments are exactly the involution numbers `I(n)` of
  `QOU.Mass.involutionNumber` — the Gaussian `N(1,1)` moment data.
* `balancedNormalizer_two` / `balancedNormalizer_three` /
  `kernel_jacobi_beta_one` — the KERNEL-frame tie-in (audit §3 finding 1),
  reusing `BalancedMomentConfluence.balancedNormalizer` (NOT redefined): the
  balanced moments are `m₁ = N^bal(2) = 1`, `m₂ = N^bal(3) = v + v⁻¹`
  (`v = q^{1/2}`, the balanced half-variable), so the kernel frame's first
  Jacobi coefficient is `β₁ = m₂ − m₁² = v + v⁻¹ − 1 = 1 + (v−1)²·v⁻¹` —
  the Wenzl quantity with its manifest-positivity shape, exact in `K`; at
  `v = 1` it is the Laguerre `β₁ = 1` (`kernel_jacobi_beta_one_at_one`).

NOT proved here (the honest residual):

* the KERNEL-frame Jacobi data at general `k` — the audit derives no closed
  form for it (only `β₁`; `α₁, β₂` are recorded factored in the witness),
  so there is nothing general-`k` to formalize on that frame;
* Favard positivity (`Hankel Δ_k > 0`) and the determinacy/extension-circle
  layer (audit §4-§5) — analytic/measure-theoretic content, probe-exact at
  the evaluation points, outside this algebraic tranche;
* the uniqueness-of-Jacobi-data step itself (classical Favard; the audit's
  citation is [`simon1998`]) — this file proves the moment-reproduction
  identity that feeds it, not the classical theorem.

Base ring (§7c): generic `{K : Type*} [Field K]` throughout — no `ℝ`, no
ordering, no `Real.sqrt`; the balanced half-variable is a field element `v`
(the `BalancedMomentConfluence` convention), and every exponent is a natural
number. No hypothesis `q ≠ 0` is even needed for the carrier closed form —
it is subtraction-free polynomial algebra.

Probe: computations/probes/ksel2_favard_jacobi_probe.py (K1: symbolic
reproduction n ≤ 12; K3: exact-ℚ closed-form check k ≤ 8 at q = 6/5; K4:
60 dps at both q₀ pins). Witness:
computations/probes/ksel2-favard-jacobi.witness.json.

-- Ref: [leitner2026] predicted-spectra, conj:schwinger-measure-computational-time;
--      docs/audits/2026-08-01-ksel2-gns-favard-canonicity.md §3 + §5 item 1;
--      docs/audits/2026-07-20-keystone-bridge-c1-binding.md (the carrier
--      recurrence, Lean-proved);
--      Favard/Jacobi: B. Simon, "The classical moment problem as a
--      self-adjoint finite difference operator", Adv. Math. 137 (1998) 82-203.
-/

import Mathlib.Tactic
import QOU.Mass.QDifferenceConfluentObstruction
import QOU.Mass.InvolutionNumbers
import QOU.Archimedean.BalancedMomentConfluence

namespace QOU.Archimedean.BalancedCarrierJacobi

open Finset
open QOU.Mass.QDifferenceConfluentObstruction (qint qfact)
open QOU.Archimedean.BalancedMomentConfluence (balancedNormalizer qint_one)

section Fibre

variable {K : Type*} [Field K]

/-! ## q-integer fibre algebra (generic field — §7c: no `ℝ`, no ordering) -/

/-- One-step unfolding of the one-sided quantum integer:
`[k+1]_q = [k]_q + q^k`. -/
theorem qint_succ (q : K) (k : ℕ) : qint q (k + 1) = qint q k + q ^ k := by
  simp only [qint, Finset.sum_range_succ]

/-- `[1]_q = 1`. -/
theorem qint_one_val (q : K) : qint q 1 = 1 := by simp [qint]

/-- **The q-integer splitting** `[a+b]_q = [a]_q + q^a·[b]_q` — the single
algebraic identity driving the main induction (it is the `i ≤ n` case of
the classical `[n+1]_q = [i]_q + q^i·[n+1−i]_q`, stated subtraction-free). -/
theorem qint_add (q : K) (a b : ℕ) :
    qint q (a + b) = qint q a + q ^ a * qint q b := by
  induction b with
  | zero => simp [qint]
  | succ b ih =>
      have h : a + (b + 1) = (a + b) + 1 := by omega
      rw [h, qint_succ, ih, qint_succ, pow_add]
      ring

/-- `[m]_q!` at index `1`. -/
theorem qfact_index_one (q : K) : qfact q 1 = 1 := by
  show qint q 1 * qfact q 0 = 1
  rw [qint_one_val]
  show (1 : K) * 1 = 1
  rw [one_mul]

/-- `[2]_q! = [2]_q = 1 + q`. -/
theorem qfact_index_two (q : K) : qfact q 2 = 1 + q := by
  show qint q (1 + 1) * qfact q 1 = 1 + q
  rw [qint_succ, qint_one_val, qfact_index_one, mul_one, pow_one]

/-! ## The carrier moment sequence `S_q(n)` -/

/-- **The carrier moments** `S_q(n)`: the q-involution numerators of the
Lean-proved binding recurrence (`S(0) = S(1) = 1`,
`S(n+2) = S(n+1) + [n+1]_q·S(n)`) — exactly the sequence hypothesis of
`QOU.Mass.KeystoneBridgeC1Binding.keystone_bridge_binding_qlift`, made
concrete. Read as a Hamburger moment sequence (KSel-2 carrier frame). At
`q = 1` these are the involution numbers `I(n)`, the moments of the
Gaussian `N(1,1)` (`carrierMoment_q_one`). -/
def carrierMoment (q : K) : ℕ → K
  | 0 => 1
  | 1 => 1
  | n + 2 => carrierMoment q (n + 1) + qint q (n + 1) * carrierMoment q n

@[simp] theorem carrierMoment_zero (q : K) : carrierMoment q 0 = 1 := rfl

@[simp] theorem carrierMoment_index_one (q : K) : carrierMoment q 1 = 1 := rfl

/-- The defining q-involution (q-Stein) recurrence, as a rewrite lemma. -/
theorem carrierMoment_succ_succ (q : K) (n : ℕ) :
    carrierMoment q (n + 2)
      = carrierMoment q (n + 1) + qint q (n + 1) * carrierMoment q n := rfl

/-- **Uniqueness of the carrier sequence**: any sequence with the
q-involution recurrence and initial values `1, 1` — i.e. any sequence
admissible in `keystone_bridge_binding_qlift` with the standard seed — is
`carrierMoment`. -/
theorem carrierMoment_unique (q : K) (S : ℕ → K) (h0 : S 0 = 1) (h1 : S 1 = 1)
    (hrec : ∀ n, S (n + 2) = S (n + 1) + qint q (n + 1) * S n) :
    ∀ n, S n = carrierMoment q n
  | 0 => by simpa using h0
  | 1 => by simpa using h1
  | n + 2 => by
      rw [hrec n, carrierMoment_succ_succ,
        carrierMoment_unique q S h0 h1 hrec (n + 1),
        carrierMoment_unique q S h0 h1 hrec n]

/-! ## The carrier Jacobi data `α_k = q^k`, `β_k = q^{k−1}[k]_q` -/

/-- **Jacobi diagonal** `α_k = q^k` (audit §3, carrier frame; `q = 1`
limit: the Gaussian `α_k = 1`). -/
def jacobiAlpha (q : K) (k : ℕ) : K := q ^ k

/-- **Jacobi off-diagonal** — `jacobiBeta q k` is `β_{k+1} = q^k·[k+1]_q`,
the probe's `betas[k]`; index-shifted by one so the audit's
`β_j = q^{j−1}[j]_q` (`j ≥ 1`) is subtraction-free (`j = k+1`). `q = 1`
limit: the Gaussian `β_j = j`. -/
def jacobiBeta (q : K) (k : ℕ) : K := q ^ k * qint q (k + 1)

/-- One application of the monic Jacobi matrix `M` (diagonal `α_i`,
superdiagonal `1`, subdiagonal `β_i`) to a coordinate vector — the probe's
`monic_jacobi_pow00` step: `(Mv)_i = β_i·v_{i−1} + α_i·v_i + v_{i+1}`,
with the `β`-term absent at `i = 0`. -/
def jacobiStep (q : K) (v : ℕ → K) : ℕ → K
  | 0 => jacobiAlpha q 0 * v 0 + v 1
  | i + 1 => jacobiBeta q i * v i + jacobiAlpha q (i + 1) * v (i + 1) + v (i + 2)

/-- `jacobiVec q n i = (Mⁿe₀)_i` — the iterated Jacobi vector. Its top
entry `jacobiVec q n 0 = (Mⁿ)₀₀` is the GNS moment. -/
def jacobiVec (q : K) : ℕ → ℕ → K
  | 0 => fun i => match i with | 0 => 1 | _ + 1 => 0
  | n + 1 => jacobiStep q (jacobiVec q n)

@[simp] theorem jacobiVec_zero_zero (q : K) : jacobiVec q 0 0 = 1 := rfl

@[simp] theorem jacobiVec_zero_succ (q : K) (i : ℕ) :
    jacobiVec q 0 (i + 1) = 0 := rfl

theorem jacobiVec_succ_zero (q : K) (n : ℕ) :
    jacobiVec q (n + 1) 0
      = jacobiAlpha q 0 * jacobiVec q n 0 + jacobiVec q n 1 := rfl

theorem jacobiVec_succ_succ (q : K) (n i : ℕ) :
    jacobiVec q (n + 1) (i + 1)
      = jacobiBeta q i * jacobiVec q n i
        + jacobiAlpha q (i + 1) * jacobiVec q n (i + 1)
        + jacobiVec q n (i + 2) := rfl

/-! ## The rising q-factorial `[m+1]_q[m+2]_q⋯[m+i]_q` -/

/-- `qRise q m i = [m+1]_q·[m+2]_q⋯[m+i]_q` — the `i`-step rising product,
the subtraction-free form of the falling factorial `[n]_q⋯[n−i+1]_q` at
`n = m + i`. (`[i]_q!·qbinom(n,i) = qRise q (n−i) i`, so the closed form
below is the q-binomial form `c(n,i) ∝ qbinom(n,i)·S(n−i)` with the
weight `q^{C(i,2)}·[i]_q!` absorbed.) -/
def qRise (q : K) (m : ℕ) : ℕ → K
  | 0 => 1
  | i + 1 => qRise q m i * qint q (m + i + 1)

@[simp] theorem qRise_zero (q : K) (m : ℕ) : qRise q m 0 = 1 := rfl

theorem qRise_succ (q : K) (m i : ℕ) :
    qRise q m (i + 1) = qRise q m i * qint q (m + i + 1) := rfl

@[simp] theorem qRise_one (q : K) (m : ℕ) : qRise q m 1 = qint q (m + 1) := by
  have h := qRise_succ q m 0
  simpa using h

/-- Bottom extraction: `[m+1]⋯[m+i+1] = [m+1]·([m+2]⋯[m+i+1])`. -/
theorem qRise_succ_left (q : K) (m i : ℕ) :
    qRise q m (i + 1) = qint q (m + 1) * qRise q (m + 1) i := by
  induction i with
  | zero => rw [qRise_succ]; simp
  | succ i ih =>
      have e : m + 1 + i + 1 = m + (i + 1) + 1 := by omega
      rw [qRise_succ q m (i + 1), ih, qRise_succ q (m + 1) i, e]
      ring

/-- `C(i+1,2) = i + C(i,2)` — the exponent step for the `q^{C(i,2)}` weight. -/
theorem choose_two_succ (i : ℕ) : (i + 1).choose 2 = i + i.choose 2 := by
  rw [Nat.choose_succ_succ, Nat.choose_one_right]

/-! ## The main induction: the closed form for `Mⁿe₀` at general `n` -/

/-- Vanishing above the diagonal: `(Mⁿe₀)_i = 0` for `i > n` (the Jacobi
matrix moves the top entry down at most one level per step). -/
theorem jacobiVec_eq_zero_of_lt (q : K) : ∀ n i, n < i → jacobiVec q n i = 0 := by
  intro n
  induction n with
  | zero =>
      intro i h
      obtain ⟨i', rfl⟩ : ∃ i', i = i' + 1 := ⟨i - 1, by omega⟩
      rfl
  | succ n ih =>
      intro i h
      obtain ⟨i', rfl⟩ : ∃ i', i = i' + 1 := ⟨i - 1, by omega⟩
      rw [jacobiVec_succ_succ, ih i' (by omega), ih (i' + 1) (by omega),
        ih (i' + 2) (by omega)]
      ring

/-- **THE MAIN INDUCTION (general `k`, sorry-free).** The full closed form
for the iterated Jacobi vector of the carrier data `α_k = q^k`,
`β_k = q^{k−1}[k]_q`:

  `(Mⁿe₀)_i = q^{C(i,2)} · [m+1]_q[m+2]_q⋯[m+i]_q · S_q(m)`,  `n = i + m`.

The induction on `n` consumes exactly (i) the q-integer splitting
`qint_add` and (ii) the q-involution recurrence of `carrierMoment` — the
q-Stein identity. This is the general-`k` closure of the probe's K1
verified-range identity (audit §5 item 1, queued there, discharged here). -/
theorem jacobiVec_eq_closed_form (q : K) :
    ∀ n i m, n = i + m →
      jacobiVec q n i
        = q ^ i.choose 2 * qRise q m i * carrierMoment q m := by
  intro n
  induction n with
  | zero =>
      intro i m h
      obtain ⟨rfl, rfl⟩ : i = 0 ∧ m = 0 := by omega
      simp [show (0 : ℕ).choose 2 = 0 from rfl]
  | succ n ih =>
      intro i m h
      cases i with
      | zero =>
          obtain rfl : m = n + 1 := by omega
          rw [jacobiVec_succ_zero]
          cases n with
          | zero =>
              simp [jacobiAlpha, show jacobiVec q 0 1 = (0 : K) from rfl,
                show (0 : ℕ).choose 2 = 0 from rfl]
          | succ n'' =>
              rw [show n'' + 1 + 1 = n'' + 2 from rfl,
                ih 0 (n'' + 1) (by omega), ih 1 n'' (by omega),
                carrierMoment_succ_succ q n'']
              simp only [jacobiAlpha, pow_zero, one_mul, qRise_zero, mul_one,
                qRise_one, show (0 : ℕ).choose 2 = 0 from rfl,
                show (1 : ℕ).choose 2 = 0 from rfl]
      | succ i' =>
          cases m with
          | zero =>
              have hn : n = i' := by omega
              subst hn
              rw [jacobiVec_succ_succ, ih n 0 (by omega),
                jacobiVec_eq_zero_of_lt q n (n + 1) (by omega),
                jacobiVec_eq_zero_of_lt q n (n + 2) (by omega),
                choose_two_succ n, qRise_succ q 0 n,
                show 0 + n + 1 = n + 1 from by omega]
              simp only [jacobiBeta, jacobiAlpha, carrierMoment_zero,
                mul_one, mul_zero, add_zero, pow_add]
              ring
          | succ m' =>
              cases m' with
              | zero =>
                  have hn : n = i' + 1 := by omega
                  subst hn
                  rw [show (0 : ℕ) + 1 = 1 from rfl, jacobiVec_succ_succ,
                    ih i' 1 (by omega), ih (i' + 1) 0 (by omega),
                    jacobiVec_eq_zero_of_lt q (i' + 1) (i' + 2) (by omega),
                    choose_two_succ i', qRise_succ q 1 i',
                    show 1 + i' + 1 = i' + 1 + 1 from by omega,
                    qint_succ q (i' + 1), qRise_succ_left q 0 i',
                    show (0 : ℕ) + 1 = 1 from rfl, qint_one_val]
                  simp only [jacobiBeta, jacobiAlpha, carrierMoment_zero,
                    carrierMoment_index_one, mul_one, one_mul, add_zero,
                    pow_add]
                  ring
              | succ m'' =>
                  rw [show m'' + 1 + 1 = m'' + 2 from rfl, jacobiVec_succ_succ,
                    ih i' (m'' + 2) (by omega),
                    ih (i' + 1) (m'' + 1) (by omega),
                    ih (i' + 2) m'' (by omega),
                    carrierMoment_succ_succ q m'',
                    qRise_succ q (m'' + 2) i',
                    show m'' + 2 + i' + 1 = i' + 1 + (m'' + 2) from by omega,
                    qint_add q (i' + 1) (m'' + 2),
                    show i' + 2 = i' + 1 + 1 from rfl,
                    qRise_succ_left q m'' (i' + 1),
                    qRise_succ_left q (m'' + 1) i',
                    show m'' + 1 + 1 = m'' + 2 from rfl,
                    choose_two_succ (i' + 1), choose_two_succ i']
                  simp only [jacobiBeta, jacobiAlpha, pow_add]
                  ring

/-- **The GNS moment identity at general `n`** (the audit's queued
general-`k` statement, closed): `(Mⁿ)₀₀ = S_q(n)` — the canonical monic
Jacobi operator with carrier data `α_k = q^k`, `β_k = q^{k−1}[k]_q` has
the q-involution carrier sequence as its moments, for EVERY `n`. -/
theorem jacobiVec_zero_eq_carrierMoment (q : K) (n : ℕ) :
    jacobiVec q n 0 = carrierMoment q n := by
  have h := jacobiVec_eq_closed_form q n 0 n (by omega)
  simpa [show (0 : ℕ).choose 2 = 0 from rfl] using h

/-- Hypothesis-style form matching `keystone_bridge_binding_qlift`: for ANY
sequence `S` with the q-involution recurrence and standard seed, the Jacobi
moments reproduce `S` — `(Mⁿ)₀₀ = S(n)` for every `n`. -/
theorem jacobiVec_zero_eq_of_recurrence (q : K) (S : ℕ → K) (h0 : S 0 = 1)
    (h1 : S 1 = 1)
    (hrec : ∀ n, S (n + 2) = S (n + 1) + qint q (n + 1) * S n) (n : ℕ) :
    jacobiVec q n 0 = S n := by
  rw [jacobiVec_zero_eq_carrierMoment, carrierMoment_unique q S h0 h1 hrec n]

/-! ## `q = 1` degeneration: the classical Gaussian `N(1,1)` data -/

/-- At `q = 1` the Jacobi diagonal degenerates to the Gaussian `α_k = 1`. -/
theorem jacobiAlpha_q_one (k : ℕ) : jacobiAlpha (1 : K) k = 1 := one_pow k

/-- At `q = 1` the Jacobi off-diagonal degenerates to the Gaussian
`β_{k+1} = k + 1` (i.e. `β_j = j`). -/
theorem jacobiBeta_q_one (k : ℕ) : jacobiBeta (1 : K) k = (k : K) + 1 := by
  simp [jacobiBeta]

/-- At `q = 1` the carrier recurrence is Stein's characterization of the
Gaussian: `S(n+2) = S(n+1) + (n+1)·S(n)`. -/
theorem carrierMoment_q_one_recurrence (n : ℕ) :
    carrierMoment (1 : K) (n + 2)
      = carrierMoment 1 (n + 1) + ((n : K) + 1) * carrierMoment 1 n := by
  rw [carrierMoment_succ_succ]
  simp

/-- At `q = 1` the carrier moments ARE the involution numbers
`I(n) = QOU.Mass.involutionNumber n` — the moments of the Gaussian
`N(1,1)` (audit §3: the classical fibre of the q-deformed Gaussian). -/
theorem carrierMoment_q_one :
    ∀ n, carrierMoment (1 : K) n = (QOU.Mass.involutionNumber n : K)
  | 0 => by simp
  | 1 => by simp
  | n + 2 => by
      rw [carrierMoment_succ_succ, QOU.Mass.involutionNumber_succ_succ,
        carrierMoment_q_one (n + 1), carrierMoment_q_one n, qint_one]
      push_cast
      ring

/-! ## Kernel-frame tie-in: the first balanced-kernel Jacobi coefficient
(reusing `balancedNormalizer` — audit §3 finding 1) -/

/-- The first balanced kernel moment is `1`:
`m₁ = N^bal(2) = balancedNormalizer v 2 = 1`. -/
theorem balancedNormalizer_two (v : K) : balancedNormalizer v 2 = 1 := by
  show (v ^ ((1 : ℕ).choose 2))⁻¹ * qfact (v ^ 2) 1 = 1
  rw [qfact_index_one, mul_one, show (1 : ℕ).choose 2 = 0 from rfl, pow_zero,
    inv_one]

/-- The second balanced kernel moment in the half-variable `v = q^{1/2}`:
`m₂ = N^bal(3) = v⁻¹·[2]_{v²} = v + v⁻¹` — i.e. `q^{1/2} + q^{−1/2}`, the
Wenzl positivity quantity. -/
theorem balancedNormalizer_three (v : K) (hv : v ≠ 0) :
    balancedNormalizer v 3 = v + v⁻¹ := by
  show (v ^ ((2 : ℕ).choose 2))⁻¹ * qfact (v ^ 2) 2 = v + v⁻¹
  rw [qfact_index_two, show (2 : ℕ).choose 2 = 1 from rfl, pow_one]
  field_simp
  ring

/-- **The kernel frame's first Jacobi coefficient** (audit §3 finding 1):
`β₁ = m₂ − m₁² = v + v⁻¹ − 1 = 1 + (v − 1)²·v⁻¹` — the Wenzl quantity
`q^{1/2} + q^{−1/2} − 1`, with the audit's sum-of-squares positivity shape
(`β₁ − 1 = (v−1)²/v`) exact in the half-variable. This is the entire
general-`k` kernel-frame content the audit derives (no closed form exists
beyond `k = 1` there — honest residual, see module docstring). -/
theorem kernel_jacobi_beta_one (v : K) (hv : v ≠ 0) :
    balancedNormalizer v 3 - balancedNormalizer v 2 ^ 2
      = 1 + (v - 1) ^ 2 * v⁻¹ := by
  rw [balancedNormalizer_three v hv, balancedNormalizer_two]
  field_simp
  ring

/-- At `v = 1` (`q = 1`) the kernel frame's `β₁` is the monic-Laguerre
`β₁ = 1²  = 1` — the determinate archimedean (`e^{−s}ds`) pin. -/
theorem kernel_jacobi_beta_one_at_one :
    balancedNormalizer (1 : K) 3 - balancedNormalizer (1 : K) 2 ^ 2 = 1 := by
  rw [kernel_jacobi_beta_one (1 : K) one_ne_zero]
  simp

end Fibre

end QOU.Archimedean.BalancedCarrierJacobi
