import Mathlib.Tactic

/-!
# QOU.Molecular.aufbau_open_strand_perron — the open-strand Perron weight is `q^ℓ` on **every** block

This file anchors the structural lever for the open Aufbau-ordering gap
(`H_scalar`, see `docs/audits/2026-06-21-aufbau-open-strand-perron-dissolves-scalar.md`).

The merged `symmetric_block_domain_weight` gives the angular weight `q^ℓ` only on
the **scalar (trivial) block** — leaving the puzzle *"why does an orbital's
angular content project to the scalar block?"*. The lever here removes that
puzzle: the Hecke generator `σ_i` satisfies the quadratic
`σ² − (q−q⁻¹)σ − 1 = 0` in **every** representation, so its eigenvalues are
`{q, −q⁻¹}` in every block, and for the substrate `q > 1` the eigenvalue `q`
**strictly dominates** in modulus (`|−q⁻¹| = q⁻¹ < q`). Hence an **open** strand
(an on-shell electron worldline, not a closed Markov loop) is Perron-dominated
and weighs `q^ℓ` *on every block* — no scalar projection is required.

The residual `a=+2` overshoot `q^{2ℓ}` is then identified precisely: it is the
**square** of the open-strand weight, `q^{2ℓ} = (q^ℓ)²` — the closed-loop
q-dimension / top-weight of the **packaged** irrep `V_ℓ`. So the open item
`H_scalar` reduces to the single **open-vs-closed topology** choice for the bound
electron strand: open propagator (`q^ℓ`, a=+1, Madelung `n+ℓ`) vs closed q-dim
loop (`q^{2ℓ}`, a=+2). This file states the dichotomy as exact arithmetic;
**it does not assert which topology the bound electron has** (that is the open
derivation target, owner-STRICT not a fitted input).

## References
- [manuscript] Ch. 12, electron-shell program synthesis (Aufbau ordering gap)
-/

namespace QOU.Molecular

/-- **Hecke quadratic factors.** Over `ℝ` with `q ≠ 0`, the Hecke characteristic
polynomial `x² − (q−q⁻¹)x − 1` factors as `(x − q)(x + q⁻¹)`. This is the
defining quadratic of the generator `σ_i` (`σ² = (q−q⁻¹)σ + 1`), valid in every
representation. -/
theorem hecke_quadratic_factor (q x : ℝ) (hq : q ≠ 0) :
    x ^ 2 - (q - q⁻¹) * x - 1 = (x - q) * (x + q⁻¹) := by
  field_simp
  ring

/-- **Eigenvalues on every block.** Any eigenvalue `x` of the Hecke generator —
a root of its quadratic, which holds in *every* representation — is one of the
two roots `q` or `−q⁻¹`. The eigenvalue spectrum `{q, −q⁻¹}` is therefore
representation-independent. -/
theorem hecke_eigenvalue_mem (q x : ℝ) (hq : q ≠ 0)
    (h : x ^ 2 - (q - q⁻¹) * x - 1 = 0) : x = q ∨ x = -q⁻¹ := by
  rw [hecke_quadratic_factor q x hq] at h
  rcases mul_eq_zero.mp h with h1 | h2
  · exact Or.inl (by linarith)
  · exact Or.inr (by linarith)

/-- **`q⁻¹ < q` for the substrate `q > 1`** (used for Perron dominance). -/
theorem inv_lt_self_of_one_lt (q : ℝ) (hq : 1 < q) : q⁻¹ < q := by
  have h0 : (0 : ℝ) < q := lt_trans one_pos hq
  rw [inv_eq_one_div, div_lt_iff₀ h0]
  nlinarith

/-- **Perron dominance — the dominant eigenvalue is `q` on every block.** For the
substrate `q > 1`, the eigenvalue `q` strictly dominates `−q⁻¹` in modulus:
`|−q⁻¹| = q⁻¹ < q = |q|`. So the dominant (largest-modulus) eigenvalue of every
Hecke generator is `q`, independent of the representation — an **open** strand
(Perron-dominated transfer element) weighs `q^L` on *every* block, with no scalar
projection. -/
theorem perron_eigenvalue_is_q (q : ℝ) (hq : 1 < q) : |(-q⁻¹)| < |q| := by
  have h0 : (0 : ℝ) < q := lt_trans one_pos hq
  have hpos : (0 : ℝ) < q⁻¹ := by positivity
  rw [abs_neg, abs_of_pos hpos, abs_of_pos h0]
  exact inv_lt_self_of_one_lt q hq

/-- **Closed-loop overshoot is the SQUARE of the open weight.** The `a=+2`
reading `q^{2ℓ}` — the q-dimension / top-weight `q^{2ℓ}` of the packaged
`(2ℓ+1)`-dim irrep `V_ℓ` — equals the **square** of the open-strand weight
`q^ℓ`. So the entire Aufbau `a=+1` vs `a=+2` ambiguity is `open` vs `open²`: a
single open-vs-closed topology choice for the angular content, not a free
parameter. -/
theorem closed_loop_is_open_squared (q : ℝ) (ℓ : ℕ) :
    q ^ (2 * ℓ) = (q ^ ℓ) ^ 2 := by
  rw [mul_comm, pow_mul]

/-- **Madelung key vs closed key differ by one extra `q^ℓ`.** The open-strand
total weight `q^{n+ℓ}` (radial `n` + angular `ℓ` open transfer curls, Madelung
key `n+ℓ`) and the closed-loop total `q^{n+2ℓ}` (key `n+2ℓ`) differ by exactly
the extra angular factor `q^ℓ`: `q^{n+2ℓ} = q^{n+ℓ} · q^ℓ`. The open reading is
the one that gives Madelung. -/
theorem closed_key_exceeds_open (q : ℝ) (n ℓ : ℕ) :
    q ^ (n + 2 * ℓ) = q ^ (n + ℓ) * q ^ ℓ := by
  rw [← pow_add]
  congr 1
  omega

end QOU.Molecular
