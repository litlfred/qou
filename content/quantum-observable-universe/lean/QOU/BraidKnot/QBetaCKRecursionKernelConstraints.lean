import QOU.BraidKnot.QBetaReebSinhParity

/-!
# QOU.BraidKnot.QBetaCKRecursionKernelConstraints

**Formalize-first constraints on the Q_β c_k-recursion kernel**, from the
`cos(Φ(u))` phase reframe (PR #1887) and the ladder anchors `c_1 = 0`,
`c_2 = -1`.

The on-`main` block `prop:q-beta-c-k-recursion-from-habiro-q-difference`
posits a depth-`d` kernel `{a_j}` with the recursion (on the Taylor
coefficients `f_n = [u^n] F(u)` of `F = Q_β/Q_A = cos(Φ(u))`)

  `f_n = Σ_{j=1}^d a_j(q_0) · f_{n-j}`,   asserted for `n ≥ d`,

with seed `f_0 = 1`, `f_1 = 0`, `f_2 = c_2 = -1`, `f_3 = c_3`, `f_4 = c_4`
(the product-form ladder `∏(1 + c_k u^k)` and the Taylor series agree through
`u⁴`; cross-terms start at `u⁵ = c_2 c_3`). The kernel is OPEN (must be
derived from the SW-residue / Hoefsmit-`H₃(q)` structure, PR #1871). These
lemmas **constrain** it without deriving it:

  1. depth ≥ 2 — a depth-1 kernel can't produce `f_2 = -1` from `f_1 = 0`;
  2. depth-2 second coefficient `a_2 = c_2 = -1` (from the `n=2` rung, `f_0=1`);
  3. depth-2 leading coefficient `a_1 = -c_3` (from the `n=3` rung, `f_1=0`);
  4. `a_1 = √2·Φ₂` (the #1887 phase relation `c_3 = -Φ₁Φ₂`, `Φ₁ = √2`) — the
     kernel's leading coefficient IS the #1887 Φ₂ target;
  5. a *constant* depth-2 kernel then predicts `c_4 = 1 - c_3²`, refuted by the
     fitted `c_4 ≈ -0.972` (companion probe);
  6. `a_1` is bar-odd (inherits `c_3`'s bar-antisymmetry, the #1887 Reeb-sinh
     parity wall) — pruning the kernel search to bar-odd leading coefficients.
  7. **C13 refutation (PR #2465):** the #1622 mode→ladder bridge, with the
     ladder seeded *linearly* from the even-in-ℏ part of `Δtr_M`, cannot
     produce `c_3 = -2`. Its two principled seedings give `c_3 = -100/(77 b)`
     (raw) and `c_3 = -175/(144 b)` (#1602 bar-even projection); each reaches
     the `J_Hopf(1) = -2` target only at a *specific* `b`, and the two required
     values differ (`50/77 ≠ 175/288`), so no single `b` lets the bridge hit
     `-2`. The surviving `f` is non-linear in `Δtr_M`.

LaTeX label: `prop:qbeta-ck-recursion-kernel-constraints`

## References
- Phase reframe: PR #1887 (`QBetaReebSinhParity`, `cos(Φ(u))`).
- c_k recursion block (open kernel): `prop:q-beta-c-k-recursion-from-habiro-q-difference`.
- c_2 = -1: PR #1602 (bar-even constraint).
- C13 bridge refutation: PR #2465 (`habiro_mode_to_ladder_bridge.py` +
  `habiro-mode-to-ladder-bridge.witness.json`); refuted-class map row C13.
-/

namespace QOU.BraidKnot

/-- **Depth-1 kernel refuted.** A depth-1 recursion gives `f_2 = a₁·f_1`; with
the ladder seed `f_1 = 0` this is `0`, contradicting the proved `f_2 = c_2 = -1`.
So the c_k-recursion kernel has depth ≥ 2. -/
theorem ck_recursion_depth_one_refuted (a₁ : ℝ) : a₁ * (0 : ℝ) ≠ -1 := by
  rw [mul_zero]; norm_num

/-- **Depth-2 second coefficient pinned: `a₂ = c₂` (`= -1`).** At the `n = 2`
rung `f_2 = a₁·f_1 + a₂·f_0` with `f_1 = 0`, `f_0 = 1`, so `c₂ = a₂`. -/
theorem ck_a2_eq_c2_depth_two (a₁ a₂ c₂ : ℝ)
    (hrec : c₂ = a₁ * 0 + a₂ * 1) : a₂ = c₂ := by
  rw [hrec]; ring

/-- **Depth-2 leading coefficient pinned: `a₁ = -c₃`.** At the `n = 3` rung
`f_3 = a₁·f_2 + a₂·f_1` with `f_2 = -1`, `f_1 = 0`, so `c₃ = -a₁` regardless of
`a₂`. -/
theorem ck_a1_eq_neg_c3_depth_two (a₁ a₂ c₃ : ℝ)
    (hrec : c₃ = a₁ * (-1) + a₂ * 0) : a₁ = -c₃ := by
  rw [hrec]; ring

/-- **The kernel's leading coefficient is the #1887 Φ₂ (up to √2).** Combining
`a₁ = -c₃` with the #1887 phase relation `c₃ = -(Φ₁·Φ₂)` and `Φ₁ = √2`:
`a₁ = √2·Φ₂`. The kernel's leading coefficient and the open Φ₂ are the same
object. -/
theorem ck_a1_eq_sqrt2_phi2 (a₁ c₃ Φ₂ : ℝ)
    (ha1 : a₁ = -c₃) (hphase : c₃ = -(Real.sqrt 2 * Φ₂)) :
    a₁ = Real.sqrt 2 * Φ₂ := by
  rw [ha1, hphase]; ring

/-- **Constant depth-2 kernel predicts `c₄ = 1 - c₃²`.** Constraints `a₂ = -1`
and `a₁ = -c₃` fully determine a *constant* depth-2 kernel; the `n = 4` rung
`f_4 = a₁·f_3 + a₂·f_2 = (-c₃)·c₃ + (-1)·(-1)` then forces `c₄ = 1 - c₃²`. The
companion probe shows this misses the fitted `c₄ ≈ -0.972` by ~3.4× at both
anchors ⇒ the recursion is depth ≥ 3 or non-constant (Habiro `(u;u)_m` basis). -/
theorem ck_c4_constant_depth_two_prediction (c₃ c₄ : ℝ)
    (hrec : c₄ = (-c₃) * c₃ + (-1) * (-1)) : c₄ = 1 - c₃ ^ 2 := by
  rw [hrec]; ring

/-- **Kernel leading coefficient is bar-ODD.** Since `a₁ = -c₃` pointwise in the
substrate angle `η` and `c₃` is bar-antisymmetric (`c₃(-η) = -c₃(η)`, the #1887
Reeb-sinh parity wall), `a₁` is bar-odd: `a₁(-η) = -a₁(η)`. The kernel
coefficient producing `c₃` from the bar-even seed `c₂` must be bar-odd
(sinh-type), pruning the open kernel search. -/
theorem ck_a1_bar_odd (c₃ a₁ : ℝ → ℝ)
    (hdef : ∀ η, a₁ η = -c₃ η) (hodd : ∀ η, c₃ (-η) = -c₃ η) (η : ℝ) :
    a₁ (-η) = -a₁ η := by
  rw [hdef, hodd, hdef]

/-- **C13 (raw seeding) — the bridge `c₃ = -100/(77 b)` hits `-2` only at
`b = 50/77`.** The #1622 mode→ladder bridge seeded by the raw even-in-ℏ part of
`Δtr_M`, scale-fixed to `c₂ = -1`, yields `c₃ = -100/(77 b)` (PR #2465 witness).
Forcing it to the `J_Hopf(1) = -2` target pins `b`. -/
theorem bridge_c3_raw_requires_b (b : ℝ) (hb : b ≠ 0)
    (h : -100 / (77 * b) = -2) : b = 50 / 77 := by
  rw [div_eq_iff (mul_ne_zero (by norm_num) hb)] at h
  linarith

/-- **C13 (#1602 bar-even seeding) — the bridge `c₃ = -175/(144 b)` hits `-2`
only at `b = 175/288`.** Same bridge with the bar-even projection of `Δtr_M`. -/
theorem bridge_c3_bareven_requires_b (b : ℝ) (hb : b ≠ 0)
    (h : -175 / (144 * b) = -2) : b = 175 / 288 := by
  rw [div_eq_iff (mul_ne_zero (by norm_num) hb)] at h
  linarith

/-- **C13 inconsistency — the two seedings need different `b`.** `50/77 ≠
175/288`, so the raw and bar-even seedings cannot both reach `-2` at one `b`. -/
theorem bridge_c3_seedings_inconsistent : (50 : ℝ) / 77 ≠ 175 / 288 := by
  norm_num

/-- **C13 refutation — the `Δtr_M`-seeded linear bridge cannot produce
`c₃ = -2`.** If both principled seedings reached `-2` at a single `b`, then
`b = 50/77` and `b = 175/288` simultaneously — impossible. Hence the mode→ladder
`f` is non-linear in `Δtr_M` (refuted-class map row C13, PR #2465). -/
theorem bridge_cannot_reach_c3_target (b : ℝ) (hb : b ≠ 0)
    (hraw : -100 / (77 * b) = -2) (hbar : -175 / (144 * b) = -2) : False := by
  have h1 := bridge_c3_raw_requires_b b hb hraw
  have h2 := bridge_c3_bareven_requires_b b hb hbar
  rw [h1] at h2; norm_num at h2

end QOU.BraidKnot
