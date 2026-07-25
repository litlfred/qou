# The odd-face constraint on the c₃ Berezinian cross-term (2026-07-25)

**Branch:** `claude/c3-berezinian-odd-block-2026-07-25`. **Feeds:** PR #4140's
super-Berezinian `c₃`-mixing wall (`qou-jqof` / `qou-1dnr`, the `qCubicGradedSplit`
`odd_eq_ggm_decay` face). **Distinct angle:** this session's A_ω work characterizes the
**odd face**; #4140 owns the Berezinian derivation and the even (DM-cubic/C1) face. This
audit records the constraints the odd face imposes — it does **not** derive `c₃` (the open
wall — "derive, never fit").

## The bridge #4140 poses

`qCubicGradedSplit` (dependent conjecture, PR #4140) splits the super-cubic into a graded
pair: the **even** face (bar-even, cosh/mass) self-contracts to the binding kernel `C1`
(weight `κ`), and the **odd** face (bar-odd, sinh/decay) self-contracts to a decay weight
`γ`. The Berezinian is `Ber = det(A − B·D⁻¹·C)·(det D)⁻¹`, and the concrete 1ppQ hook
(`qou-1dnr`) reads **`c₃` = the first even/odd *mixing* order = the cross-term `B·D⁻¹·C`**,
with `|c₃|·u³ ≈` the 1279 ppb Q_β miss.

This session characterized the **odd face** on main:
`GZWeightSelection`/`GZWeightGeneral` (the odd A_ω ray is the integer `b=0` branch),
`OneInstantonNormalization` (the odd `N_odd` one-instanton shape realizes
`BarOddLadderShape`), and the residue-dictionary reconciliation (the odd amplitude is the
Borel–Padé residue). So `γ` — #4140's odd decay weight — is the object this A_ω work pins.

## Constraints the odd face `γ` must satisfy (feeding #4140)

1. **Bar-parity ⇒ the shadow zero is even, not `γ`.** A genuinely bar-odd `γ`
   (`γ(q⁻¹) = −γ(q)`) **vanishes at the bar-involution fixed point `q = 1`**
   (`OddDecayWeightParity.barOdd_vanishes_at_one`, Lean sorry-free). So the nonzero
   `c₃(q=1) = −2` (`= J_Hopf(1)`) is carried by the **bar-even** part
   (`shadow_is_bar_even`), **not** by `γ`. `γ` is the `q`-dependent *deviation* — the
   A_ω swing — with its zero at the substrate/decay-sector `q*`, not at the shadow
   (`odd_face_qstar_zero`, from `BarOddLadderShape.zero_at_qstar`). **Constraint:** #4140's
   `γ` must be the bar-odd deviation (shadow-vanishing), and the `−2` shadow belongs in the
   even/`κ` side of the split, not the odd side.

2. **`q*`-zero + slope.** `γ`, as the bar-odd ladder numerator, has a simple zero at `q*`
   with slope `A′ ≈ +2.37` (`BarOddLadderShape`), and — from the one-instanton realization
   — that slope is **log-derivative-free** at `q*` (a *consequence* of the product shape,
   `OneInstantonNormalization`). **Constraint:** the cross-term `B·D⁻¹·C`, restricted to
   the odd face, must reproduce a simple `q*`-zero with a log-derivative-free slope.

3. **Amplitude scale.** The odd face's magnitude is the Borel–Padé residue `|2πi·r̃|` at
   `u_sub` (the derived normalization), **not** a closed-form exponential prefactor
   (the #4260 magnitude probe + the residue reconciliation). **Constraint:** the cross-term
   must land the odd amplitude at the residue scale (`|N_odd| ~ 2.5×10⁻⁸` near the
   anchors), not a naive geometric exponential.

4. **Scale caveat on the cross-term (a genuine structural hazard for #4140).** The
   Berezinian correction is `A − B·D⁻¹·C` with `D` the **odd** block. If `D` is small
   (odd/decay scale `~N_odd ~ 10⁻⁸`), then `D⁻¹` is large, so `B·D⁻¹·C` is large **unless
   `B, C` (the off-diagonal mixing blocks) are correspondingly small**. For the cross-term
   to be the *small* `c₃`-order correction (not a dominant term), `B·C` must scale like
   `D·c₃`. This is a real constraint on the off-block magnitudes that any honest derivation
   of `c₃ = B·D⁻¹·C` must satisfy — flagged so #4140's derivation pins `B, C` consistently
   with the odd `D` scale rather than assuming an `O(1)` cross-term.

## Discipline

Constraints (proved parity invariant + the on-main A_ω characterization), **not** a
derivation of `c₃`, which stays the open wall. No fit; no `c_k` wired; nothing depends on
#4140's unmerged `SuperDMBerezinian` (the Lean brick uses only on-main `BarOddLadderShape`).
Posted as coordination on #4140.
