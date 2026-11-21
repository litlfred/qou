import Mathlib.Tactic

/-!
# QOU.Molecular.aufbau_open_strand_perron — Perron eigenvalue `q` on every block; the open-strand `a=+1` reading and why it is defeated

This file is the sorry-free arithmetic companion to the Aufbau-ordering
refutation (`docs/audits/2026-06-21-h-scalar-refuted-post-hoc-functional-choice.md`,
on main) and its open-strand follow-up
(`docs/audits/2026-06-21-aufbau-open-strand-perron-defeated-by-rotation-invariance.md`).

**Context.** The merged `symmetric_block_domain_weight` gives the angular weight
`q^ℓ` only on the **scalar (trivial) block**. The refutation shows `H_scalar`
(orbital energy `= q^ℓ`, a=+1) is a *fit-by-functional-choice*: QOU's natural
observables **bracket** `a=+1` — the confinement-SDP dual gives `a=0`, the
rotation-invariant q-dimension trace gives `a=+2` — and **none produces `a=+1`**.

**What this file formalizes (true regardless).** The Hecke generator `σ_i`
satisfies `σ² − (q−q⁻¹)σ − 1 = 0` in **every** representation, so its eigenvalues
are `{q, −q⁻¹}` in every block, and for the substrate `q > 1` the eigenvalue `q`
**strictly dominates** in modulus (`|−q⁻¹| = q⁻¹ < q`). So the `a=+1` weight `q^ℓ`
is *not* special to the scalar block — it is the Perron power of an **open** strand
(`(σ^ℓ)` matrix element) in any block.

**Why the open-strand `a=+1` reading is nevertheless DEFEATED** (recorded in the
audit, not contradicted here): an **isolated** atom has full `SO(3)_q` symmetry,
so its energy is **rotation-invariant** — a *trace* (closed loop) — which is the
q-dimension `[2ℓ+1]_q ~ q^{2ℓ}` (a=+2). The open-strand matrix element `(σ^ℓ)₁₁`
is *not* rotation-invariant (it picks a preferred axis — a molecular `C_nv`
feature the isolated atom lacks). The arithmetic `q^{2ℓ} = (q^ℓ)²` below records
that the rotation-invariant (closed) reading is exactly the **square** of the
open-strand reading. So this file *confirms* the refutation: `a=+1` is a genuine
candidate weight but the isolated-atom symmetry selects `a=+2`. **Nothing is
wired; Madelung stays OPEN (owner STRICT).**

## References
- [leitner2026] Ch. 12, electron-shell program synthesis (Aufbau ordering gap)
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

/-- **Perron dominance — the dominant eigenvalue is `q` on every block.** For the
substrate `q > 1`, the eigenvalue `q` strictly dominates `−q⁻¹` in modulus:
`|−q⁻¹| = q⁻¹ < q = |q|`. So the dominant (largest-modulus) eigenvalue of every
Hecke generator is `q`, independent of the representation — an **open** strand
(Perron-dominated transfer element) weighs `q^L` on *every* block. (This does
*not* by itself give the orbital energy: the isolated atom's energy is the
rotation-invariant trace, not the open-strand matrix element — see file
docstring.) -/
theorem perron_eigenvalue_is_q (q : ℝ) (hq : 1 < q) : |(-q⁻¹)| < |q| := by
  have h0 : (0 : ℝ) < q := lt_trans one_pos hq
  have hpos : (0 : ℝ) < q⁻¹ := by positivity
  rw [abs_neg, abs_of_pos hpos, abs_of_pos h0]
  -- `q⁻¹ < q` for `q > 1`:
  rw [inv_eq_one_div, div_lt_iff₀ h0]
  nlinarith

/-- **Rotation-invariant (closed-loop) reading is the SQUARE of the open one.**
The `a=+2` weight `q^{2ℓ}` — the q-dimension / top weight `q^{2ℓ}` of the
packaged `(2ℓ+1)`-dim irrep `V_ℓ`, the rotation-invariant trace that *is* the
isolated atom's energy — equals the **square** of the open-strand weight `q^ℓ`.
So the Aufbau `a=+1` vs `a=+2` gap is `open` vs `open²`: the isolated-atom
symmetry (a trace) selects the closed reading `a=+2`. -/
theorem closed_loop_is_open_squared (q : ℝ) (ℓ : ℕ) :
    q ^ (2 * ℓ) = (q ^ ℓ) ^ 2 := by
  rw [mul_comm, pow_mul]

/-- **Closed key exceeds the open (Madelung) key by one extra `q^ℓ`.** The
open-strand total weight `q^{n+ℓ}` (Madelung key `n+ℓ`) and the
rotation-invariant closed total `q^{n+2ℓ}` (key `n+2ℓ`, the predicted ordering)
differ by exactly the extra angular factor `q^ℓ`: `q^{n+2ℓ} = q^{n+ℓ} · q^ℓ`. The
empirical Madelung order is the open key; the canonical (rotation-invariant)
observable predicts the closed key. -/
theorem closed_key_exceeds_open (q : ℝ) (n ℓ : ℕ) :
    q ^ (n + 2 * ℓ) = q ^ (n + ℓ) * q ^ ℓ := by
  rw [← pow_add]
  congr 1
  omega

end QOU.Molecular
