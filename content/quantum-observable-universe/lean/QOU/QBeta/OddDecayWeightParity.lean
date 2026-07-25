import QOU.QBeta.BarOddLadderShape

/-!
# Bar-parity constraint on the odd decay weight (the Berezinian cross-term's odd face)

Standalone, on-main constraint feeding the `qCubicGradedSplit.odd_eq_ggm_decay` face of
the super-Berezinian `c₃`-mixing wall (`qou-jqof` / `qou-1dnr`, PR #4140). That conjecture
posits the **odd** (bar-odd, sinh/decay) face of the graded super-cubic self-contracts to a
nonzero decay weight `γ` — the GGM/decay face that this session's A_ω work
(`OneInstantonNormalization`, `BarOddLadderShape`, `GZWeightGeneral`) characterizes. The
`c₃` = Berezinian cross-term `B·D⁻¹·C` hook then reads `c₃` as the first even/odd **mixing**
order (even = C1/mass, odd = this decay face).

This file records the **bar-parity constraint** any genuinely bar-odd decay weight must
satisfy, without depending on PR #4140's (unmerged) `SuperDMBerezinian` structure: a
bar-odd function of `q` (i.e. `f(q⁻¹) = −f(q)`) **vanishes at the bar-involution fixed
point** `q = 1`. So the *bar-odd* part of the decay weight has a **zero at the `q = 1`
shadow** — which is why the nonzero `c₃(q=1) = −2` (the `J_Hopf(1)` shadow) is **not** the
bar-odd `γ` but the even/shadow part: the bar-odd decay face `γ` is the `q`-dependent
*deviation* that carries the A_ω swing, whose `q*`-behaviour is
`BarOddLadderShape` (`A(q*) = 0`, `A′ ≈ 2.37`).

Discipline: this is a **parity constraint** (a proved invariant), not a derivation of `c₃`
— which stays the open wall (`qou-jqof`, "derive, never fit"). It constrains PR #4140's
`γ` (the odd face must be bar-odd ⇒ its shadow vanishes), complementary to their even-face
DM-cubic derivation. No fit; no `c_k` wired. Verified `lean`-direct (exit 0), sorry-free.

-- Ref: [manuscript] docs/audits/2026-07-25-c3-berezinian-odd-face-constraint.md
-/

namespace QOU.QBeta.OddDecayWeightParity

/-- **A bar-odd weight vanishes at the bar-involution fixed point `q = 1`.** If
`f(q⁻¹) = −f(q)` for all `q`, then `f(1) = 0` (the fixed point `1⁻¹ = 1` forces
`f(1) = −f(1)`). The elementary parity fact behind "the bar-odd decay face has a zero at
the `q = 1` shadow". -/
theorem barOdd_vanishes_at_one {f : ℝ → ℝ} (h : ∀ q : ℝ, f (1 / q) = -f q) : f 1 = 0 := by
  have h1 := h 1
  simp only [div_one] at h1
  linarith

/-- **The nonzero `q = 1` value is carried by the bar-even part, not the bar-odd face.**
Decompose any weight `g = gEven + gOdd` into bar-even (`gEven(q⁻¹) = gEven(q)`) and bar-odd
(`gOdd(q⁻¹) = −gOdd(q)`) parts. Then `g(1) = gEven(1)`: the value at the shadow is purely
even. So a nonzero shadow `c₃(1) = −2` lives entirely in the **even** part; the bar-odd
decay weight `γ = gOdd` contributes `0` there — it is the `q`-dependent deviation, not the
constant shadow. -/
theorem shadow_is_bar_even {gEven gOdd : ℝ → ℝ}
    (hOdd : ∀ q : ℝ, gOdd (1 / q) = -gOdd q) :
    (gEven + gOdd) 1 = gEven 1 := by
  have hz : gOdd 1 = 0 := barOdd_vanishes_at_one hOdd
  simp [Pi.add_apply, hz]

/-- **The bar-odd decay face realises `BarOddLadderShape`'s zero — at `q*`, not the shadow.**
Records the two distinct zeros the odd face carries: the parity zero at the `q = 1` shadow
(`barOdd_vanishes_at_one`) and the substrate/decay-sector zero at `q*` (the
`BarOddLadderShape.zero_at_qstar` this session's A_ω normalization pins). They are
different loci; the A_ω swing lives on the `q*` zero, not the shadow. This is a pure
restatement tying the parity constraint to the ladder, exhibiting that the file's content
is joint with the on-main A_ω structure. -/
theorem odd_face_qstar_zero {S A u : ℝ → ℝ} {qstar A' : ℝ}
    [h : BarOddLadderShape S A u qstar A'] : A qstar = 0 :=
  h.zero_at_qstar

end QOU.QBeta.OddDecayWeightParity
