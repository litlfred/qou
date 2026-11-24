import Mathlib.Tactic

/-!
# The `(1, 0, −1)` trace is not a super-dimension trace

The α_em linchpin needs the functional on `H₃` with block weights
`(w_(3), w_(2,1), w_(1³)) = (1, 0, −1)`
(`QOU.AlphaEM.T35TenLinchpin.t35_weights_unique`). A Schur–Weyl (super)trace
on `V^{⊗3}` has block weights equal to the (super)dimensions of the Schur
functors `S_λ V`. At `q = 1` these are polynomials in `d = sdim V`:

* `dim S_(3) V   = d(d+1)(d+2)/6`
* `dim S_(2,1) V = d(d−1)(d+1)/3`
* `dim S_(1³) V  = d(d−1)(d−2)/6`

`no_superdim_gives_young_trace`: no `d` makes these proportional to
`(1, 0, −1)` with a nonzero scale. So no single super vector space supplies
the weights through its supertrace. The `q`-deformed case and the
`U_q(gl(1|1))` weight-sector decomposition are checked exactly in
`computations/alpha_em/photon_gl11_supertrace_weights_probe.py`.
-/

namespace QOU.AlphaEM.YoungTrace

variable {K : Type*} [Field K] [CharZero K]

/-- Schur-functor dimensions at `q = 1`, as polynomials in `d = sdim V`. -/
def dimSym (d : K) : K := d * (d + 1) * (d + 2) / 6
def dimHook (d : K) : K := d * (d - 1) * (d + 1) / 3
def dimAlt (d : K) : K := d * (d - 1) * (d - 2) / 6

/-- **No super-dimension gives weights `c · (1, 0, −1)` with `c ≠ 0`.** -/
theorem no_superdim_gives_young_trace (d c : K) (hc : c ≠ 0) :
    ¬ (dimSym d = c ∧ dimHook d = 0 ∧ dimAlt d = -c) := by
  rintro ⟨h3, h21, h111⟩
  unfold dimSym dimHook dimAlt at *
  have hz : d * (d - 1) * (d + 1) = 0 := by
    have := h21; field_simp at this; linear_combination this
  rcases mul_eq_zero.1 hz with h | h
  · rcases mul_eq_zero.1 h with h0 | h1
    · subst h0; apply hc; rw [← h3]; ring
    · have : d = 1 := by linear_combination h1
      subst this; apply hc; linear_combination h111
  · have : d = -1 := by linear_combination h
    subst this; apply hc; rw [← h3]; ring

end QOU.AlphaEM.YoungTrace
