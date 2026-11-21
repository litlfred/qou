import Mathlib.Tactic

/-!
# Bar-odd D-ladder: the anchor-blindness (least-term-at-edge) mechanism

Companion to `QOU.QBeta.DLadderAccelerationComposition` (which proves the
fixed-order Borel–Leroy composition collapse) and to the resummation probe
`computations/qbeta/qbeta_dladder_barodd_borel_pade_laplace_probe.py`.

The probe measures — for the exact bar-odd Q_β D-ladder `D(ũ) = Σ_k d_k ũ^k`
evaluated at the real substrate `ũ₀ ≈ 0.00945` — that the optimal-truncation
least term sits at the **ladder edge** `N* = KMAX`, so the Stokes ambiguity
`δ_np = |d_{N*}| ũ₀^{N*} ≈ 5·10⁻²⁷` is exponentially suppressed and the resummed
value is **anchor-blind** (it reproduces `S_opt = Σ d_k ũ₀^k` to ≫1 ppQ but
carries no monodromy/Stokes datum). The genuine, unsuppressed Stokes datum
appears only above a rung-ratio threshold (the fibre branch `|ũ| ≳ 0.19`,
`docs/audits/2026-07-18-dladder-fibre-branch-stokes-ambiguity.md`).

This file formalises the **structural reason** the least term is at the edge on
the substrate, and its falsifiable converse — the substrate↔fibre transition
criterion. Both are sorry-free elementary facts about a finite positive
power-magnitude sequence `t_k = c_k · x^k` (with `c_k = |d_k| > 0`, `x = ũ₀ > 0`):

* `barOdd_leastTerm_at_edge` — if `x` is **below every rung-ratio radius**
  (`c_{k+1}·x ≤ c_k` for all `k < n`, i.e. `x ≤ c_k / c_{k+1}`), then the term
  magnitude is antitone on `[0, n]` and its **minimum is the edge index `n`**:
  `c_n x^n ≤ c_k x^k` for every `k ≤ n`. This is exactly `N* = n` (edge), so the
  Stokes ambiguity `δ_np = t_n` is the *smallest* term — maximally suppressed.

* `barOdd_ratio_exceeded_of_not_edge` — the contrapositive: if the least term is
  **not** at the edge, then some rung-ratio radius was exceeded
  (`∃ k < n, c_k < c_{k+1}·x`). Crossing a rung radius is precisely the fibre
  transition where the least term leaves the top and the Stokes datum turns on.

Stated over a generic ordered field `[Field R] [LinearOrder R] [IsStrictOrderedRing R]`
(§7c: no `Real.sqrt`/`Real.log`,
no archimedean construct — a pure ordered-field inequality); the substrate
specialisation `R := ℝ`, `c_k := |d_k|`, `x := ũ₀` is what the probe evaluates.

-- Ref: [leitner2026] docs/audits/2026-08-01-qborel-ecalle-resum-barodd.md
-- Ref: [leitner2026] docs/audits/2026-07-18-dladder-fibre-branch-stokes-ambiguity.md
-/

namespace QOU.QBeta

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- One rung step: if `x` is at or below the local ratio radius `c k / c (k+1)`
(equivalently `c (k+1) · x ≤ c k`) and `x ≥ 0`, then the term magnitude does
not increase from index `k` to `k+1`: `c (k+1) x^{k+1} ≤ c k x^k`. -/
theorem barOdd_term_step (c : ℕ → R) (x : R) (hx : 0 ≤ x) (k : ℕ)
    (hratio : c (k + 1) * x ≤ c k) :
    c (k + 1) * x ^ (k + 1) ≤ c k * x ^ k := by
  have hxk : (0 : R) ≤ x ^ k := pow_nonneg hx k
  have e : c (k + 1) * x ^ (k + 1) = (c (k + 1) * x) * x ^ k := by ring
  rw [e]
  exact mul_le_mul_of_nonneg_right hratio hxk

/-- **Anchor-blindness / least-term-at-edge.** If the argument `x ≥ 0` lies below
every rung-ratio radius on `[0, n)` (`c (k+1) · x ≤ c k` for all `k < n`), then
the power-magnitude sequence `t_k = c_k x^k` is antitone on `[0, n]` and attains
its minimum at the **edge index `n`**: `c n x^n ≤ c k x^k` for every `k ≤ n`.

Physical content: at the substrate `ũ₀`, the least term (the Stokes ambiguity
`δ_np`) is the *top* rung of the ladder — exponentially suppressed — so the
resummed value is anchor-blind. -/
theorem barOdd_leastTerm_at_edge {n : ℕ} (c : ℕ → R) (x : R) (hx : 0 ≤ x)
    (hratio : ∀ k, k < n → c (k + 1) * x ≤ c k) :
    ∀ k, k ≤ n → c n * x ^ n ≤ c k * x ^ k := by
  -- term magnitude is antitone along the chain `[0, n]`
  have hanti : ∀ i j, i ≤ j → j ≤ n → c j * x ^ j ≤ c i * x ^ i := by
    intro i j
    induction j with
    | zero =>
      intro hij _
      obtain rfl := Nat.le_zero.mp hij
      exact le_refl _
    | succ j ih =>
      intro hij hjn
      rcases hij.lt_or_eq with h | h
      · have hij' : i ≤ j := Nat.lt_succ_iff.mp h
        have hjn' : j ≤ n := le_trans (Nat.le_succ j) hjn
        have h1 : c (j + 1) * x ^ (j + 1) ≤ c j * x ^ j :=
          barOdd_term_step c x hx j
            (hratio j (lt_of_lt_of_le (Nat.lt_succ_self j) hjn))
        exact le_trans h1 (ih hij' hjn')
      · subst h; exact le_refl _
  intro k hk
  exact hanti k n hk (le_refl n)

/-- **Falsifiable converse — the substrate↔fibre transition criterion.** If the
least term is *not* at the edge (some `k ≤ n` has `c k x^k < c n x^n`), then a
rung-ratio radius was exceeded: `∃ k < n, c k < c (k+1) · x`. Crossing a rung
radius is exactly the fibre transition where the least term leaves the top and
the Stokes datum turns on (corpus threshold `r* = |d₃₀/d₃₁|`). -/
theorem barOdd_ratio_exceeded_of_not_edge {n : ℕ} (c : ℕ → R) (x : R) (hx : 0 ≤ x)
    (hnot : ¬ ∀ k, k ≤ n → c n * x ^ n ≤ c k * x ^ k) :
    ∃ k, k < n ∧ c k < c (k + 1) * x := by
  by_contra hcon
  push_neg at hcon
  exact hnot (barOdd_leastTerm_at_edge c x hx (fun k hk => hcon k hk))

end QOU.QBeta
