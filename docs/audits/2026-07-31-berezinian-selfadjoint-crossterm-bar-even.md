# The graded-self-adjoint Berezinian cross-term is bar-EVEN — a parity obstruction (2026-07-31)

**Branch:** `claude/c3-berezinian-parity-forced-2026-07-31`. **Feeds:** the super-DM /
Berezinian `c₃`-mixing wall (`qCubicGradedSplit`, bean `qou-jqof`, PR #4140, off-main).
**Constraint, not closure.**

## What was checked, and a correction

The odd-face bricks (`OddDecayWeightParity`, on main) *model* `c₃` as the Berezinian
off-diagonal cross-term `t = B·D⁻¹·C` and *assume* it is bar-ODD via a factorization
`t = g·γ` (bar-even dressing × bar-odd weight). The natural way to try to **derive**
that parity is graded self-adjointness of the mass endomorphism `𝓜` (`Re 𝔙 = binding`,
bar-self-adjoint), which makes the odd off-diagonal blocks bar-conjugate, `C = −σ(B)`.

Computing the parity under that hypothesis gives the **opposite** of the assumed model:

> `QOU/QBeta/BerezinianSelfAdjointCrossTerm.lean` (sorry-free, `lean`-direct exit 0):
> **`selfadjoint_crossTerm_bar_even`** — with `C = −σB` and `Dinv` bar-even, the
> cross-term `t = B·Dinv·C = −B·Dinv·σB` satisfies `σ t = t`. It is **bar-EVEN** — a
> norm-squared object `|B|²/D`, intrinsically self-conjugate — for any ring involution
> `σ`.

The algebra: `σt = σB·Dinv·(−σ(σB)) = σB·Dinv·(−B) = −(σB·Dinv·B) = −(B·Dinv·σB)`
(CommRing) `= t` (since `t = −B·Dinv·σB`). No order needed; closes by `ring` over a
generic `CommRing`.

**Correction recorded.** A Front-3 scoping pass proposed a brick asserting the
self-adjoint cross-term is bar-*odd* ("parity forced from self-adjointness"). That is
**wrong** — the self-adjoint cross-term is bar-*even*. The proposed proof
(`subst; rw[...]; ring`) cannot close, because `ring` cannot identify `σ(σB)` with `B`
without the involution law, and once the involution law is applied the parity comes out
`σt = t`. The corrected, verified statement is the bar-EVEN one above.

## The structural consequence (the genuine constraint)

**`barOdd_crossTerm_forbids_selfadjoint`** (sorry-free): if the cross-term is bar-ODD
(`σ t = −t`, the parity `c₃` must have) with `Dinv` bar-even and the self-adjointness
relation `C = −σB`, then `2·t = 0`. So over a 2-torsion-free ring a **genuinely bar-odd**
cross-term **cannot** arise from bar-conjugate (self-adjoint) off-blocks.

Consequence for the wall: the `OddDecayWeightParity` `t = g·γ` (bar-odd) model is
consistent **only** with a **non-self-adjoint** super-structure — the off-diagonal
blocks `B, C` must be **independent**, *not* adjoint-linked `C = ±σB`. This corrects the
intuition that graded self-adjointness "forces" the bar-odd cross-term (it forces the
bar-EVEN one) and prunes the self-adjoint route to a bar-odd `c₃`.

Physically: the bar-EVEN self-adjoint cross-term `|B|²/D` is naturally the **binding /
mass** (bar-even, `Re 𝔙`) contribution, not the decay (`Im 𝔙`) one. So the Berezinian's
*self-adjoint* mixing feeds the **even** face; the bar-odd `c₃` needs a genuinely
non-self-adjoint (off-adjoint) block pair — a sharper requirement on any derivation of
`q_cubic = C1` than "the cross-term is odd."

## Scope (STRICT)

Parity obstruction (proved invariant), not a derivation of `c₃`. No `c_k` value derived;
nothing wired; no dependency on PR #4140's unmerged `SuperDMBerezinian.lean` (uses only
on-main `ZBarParity`). §7c-clean (generic `CommRing`, abstract bar involution, no `ℝ`).
This does not close the wall — it removes one route (self-adjoint ⇒ bar-odd) and names
the real requirement (independent off-blocks). Complementary to the on-main
`OddDecayWeightParity` (which models the odd factorization) and PR #4140's even-face
DM-cubic derivation.
