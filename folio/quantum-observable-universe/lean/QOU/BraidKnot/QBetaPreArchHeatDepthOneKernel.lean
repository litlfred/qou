import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# QOU.BraidKnot.QBetaPreArchHeatDepthOneKernel

**Pre-archimedean depth-1 q-difference backbone of the q-heat flow** — the
formalize-first layer under the heat-route candidate family for the open
c_k-recursion kernel `R(q, ξ)` of
`prop:q-beta-c-k-recursion-from-habiro-q-difference`.

The corpus's q-exponential is the abstract grouplike `exp_q ∈ G(ℋ_q)` over
`ℤ[q, q⁻¹]` (`def:q-exponential`), characterised by the Jackson equation
`D_q exp_q = exp_q` (`prop:q-exponential-taylor` is its archimedean
realisation). Cleared of denominators, that defining equation IS a depth-1
q-difference equation

  `exp_q (q·x) = (1 + (q-1)·x) · exp_q x`,

so every Peter–Weyl heat mode `t ↦ exp_q (-(μ_λ·t))` (content-Casimir
eigenvalue `μ_λ(q)`, `prop:q-heat-kernel-peter-weyl`) carries the exact
per-mode kernel `1 - (q-1)·μ_λ·t`, and finite sums of modes (heat-trace
truncations `Z_q`) satisfy explicit division-free depth-2 compositions.

Everything here is generic-`R` commutative algebra (AGENTS.md §7c): no
ordering, no `Real.*`, no archimedean constructs — the statements live at
the fibre level where the Habiro kernel hunt operates. The candidate family
these lemmas back is UNGATED: per
`QOU.BraidKnot.QBetaCKRecursionKernelConstraints` it must still produce a
bar-odd leading coefficient `a₁ = -c₃` and survive the constant-depth-2
`c₄` refutation. Gate evaluation happens in the Stage-B probe
(`computations/qbeta/`), not here.

## References
- `def:q-exponential`, `prop:q-exponential-taylor` (information-theory).
- `prop:q-heat-kernel-peter-weyl` — `μ_λ(q) = ℏ_q² Σ [c]_q [c+1]_q`.
- `prop:q-beta-c-k-recursion-from-habiro-q-difference` (open kernel).
- Synthesis: `docs/audits/2026-06-10-qbeta-ck-state-of-play-synthesis.md` §3-bis.
-/

namespace QOU.BraidKnot

/-- **The Jackson fixed-point equation is a depth-1 q-difference equation.**
Denominator-free form of `D_q f = f`: if `f (q·x) - f x = (q-1)·x·f x`
(the Jackson derivative equation cleared of its `(q-1)·x` denominator),
then `f` satisfies the depth-1 shift equation with kernel `1 + (q-1)·x`.
This is the pre-archimedean form of the q-exponential's defining equation —
the prototype cyclotomic kernel. -/
theorem jackson_fixed_shift_kernel {R : Type*} [CommRing R]
    (f : R → R) (q x : R)
    (h : f (q * x) - f x = (q - 1) * x * f x) :
    f (q * x) = (1 + (q - 1) * x) * f x := by
  linear_combination h

/-- **Per-mode heat kernel: depth-1 with kernel `1 - (q-1)·μ·t`.** If `f`
satisfies the depth-1 shift equation (e.g. `f = exp_q`), then the heat mode
`t ↦ f (-(μ·t))` — `μ` a content-Casimir eigenvalue `μ_λ(q)` — satisfies
the depth-1 equation whose kernel `1 - (q-1)·μ·t` has its zero located by
the spectrum. -/
theorem heat_mode_depth_one_kernel {R : Type*} [CommRing R]
    (f : R → R) (q μ : R)
    (hf : ∀ x, f (q * x) = (1 + (q - 1) * x) * f x) (t : R) :
    f (-(μ * (q * t))) = (1 - (q - 1) * (μ * t)) * f (-(μ * t)) := by
  have h := hf (-(μ * t))
  have e : q * -(μ * t) = -(μ * (q * t)) := by ring
  rw [e] at h
  rw [h]; ring

/-- **Division-free two-mode composition (depth 2).** If `F`, `G` satisfy
depth-1 equations with kernels `A`, `B`, their sum `S = F + G` satisfies the
explicit depth-2 relation

  `(B t - A t)·(S (q²t) - A (qt)·S (qt)) = (B (qt) - A (qt))·B t·(S (qt) - A t·S t)`.

This is the assembly step from per-mode kernels toward heat-trace kernels
`∏_λ (1 - (q-1)·μ_λ·t)`: no division by the Casoratian is needed, so the
identity holds over any commutative ring — fully fibre-level. -/
theorem two_mode_depth_two_composition {R : Type*} [CommRing R]
    (F G A B : R → R) (q : R)
    (hF : ∀ t, F (q * t) = A t * F t) (hG : ∀ t, G (q * t) = B t * G t)
    (t : R) :
    (B t - A t) *
        ((F (q * (q * t)) + G (q * (q * t))) - A (q * t) * (F (q * t) + G (q * t)))
      = (B (q * t) - A (q * t)) * B t *
          ((F (q * t) + G (q * t)) - A t * (F t + G t)) := by
  have h1 := hF t
  have h2 := hG t
  have h3 := hF (q * t)
  have h4 := hG (q * t)
  rw [h3, h4, h1, h2]
  ring

/-- **Heat-mode specialization.** The two-mode composition with the concrete
per-mode heat kernels `A t = 1 - (q-1)·(μ₁·t)`, `B t = 1 - (q-1)·(μ₂·t)`
(content-Casimir eigenvalues `μ₁ = μ_λ`, `μ₂ = μ_λ'`): the rank-2 truncation
of the heat trace `Z_q` satisfies an explicit depth-2 q-difference relation
whose coefficients are polynomials in `q`, `μ₁`, `μ₂`, `t`. -/
theorem heat_two_mode_composition {R : Type*} [CommRing R]
    (F G : R → R) (q μ₁ μ₂ : R)
    (hF : ∀ t, F (q * t) = (1 - (q - 1) * (μ₁ * t)) * F t)
    (hG : ∀ t, G (q * t) = (1 - (q - 1) * (μ₂ * t)) * G t)
    (t : R) :
    ((1 - (q - 1) * (μ₂ * t)) - (1 - (q - 1) * (μ₁ * t))) *
        ((F (q * (q * t)) + G (q * (q * t)))
          - (1 - (q - 1) * (μ₁ * (q * t))) * (F (q * t) + G (q * t)))
      = ((1 - (q - 1) * (μ₂ * (q * t))) - (1 - (q - 1) * (μ₁ * (q * t)))) *
          (1 - (q - 1) * (μ₂ * t)) *
          ((F (q * t) + G (q * t)) - (1 - (q - 1) * (μ₁ * t)) * (F t + G t)) := by
  exact two_mode_depth_two_composition F G
    (fun s => 1 - (q - 1) * (μ₁ * s)) (fun s => 1 - (q - 1) * (μ₂ * s)) q hF hG t

/-- Subtracting the right-hand depth-two heat recurrence combination from the left-hand combination yields zero. -/
theorem heat_two_mode_composition_sub_eq_zero {R : Type*} [CommRing R]
    (F G : R → R) (q μ₁ μ₂ : R)
    (hF : ∀ t, F (q * t) = (1 - (q - 1) * (μ₁ * t)) * F t)
    (hG : ∀ t, G (q * t) = (1 - (q - 1) * (μ₂ * t)) * G t)
    (t : R) :
    (((1 - (q - 1) * (μ₂ * t)) - (1 - (q - 1) * (μ₁ * t))) *
        ((F (q * (q * t)) + G (q * (q * t)))
          - (1 - (q - 1) * (μ₁ * (q * t))) * (F (q * t) + G (q * t))))
      - (((1 - (q - 1) * (μ₂ * (q * t))) - (1 - (q - 1) * (μ₁ * (q * t)))) *
          (1 - (q - 1) * (μ₂ * t)) *
          ((F (q * t) + G (q * t)) - (1 - (q - 1) * (μ₁ * t)) * (F t + G t))) = 0 := by
  rw [heat_two_mode_composition F G q μ₁ μ₂ hF hG t, sub_self]

end QOU.BraidKnot
