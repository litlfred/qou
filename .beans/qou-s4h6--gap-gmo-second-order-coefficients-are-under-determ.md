---
# qou-s4h6
title: 'GAP: GMO second-order coefficients are under-determined — two deviations, three coefficients, Y·d invisible'
status: todo
type: task
priority: normal
created_at: 2026-08-25T10:37:24Z
updated_at: 2026-08-25T10:37:58Z
---

**Measured 2026-08-25** (PR #5744). Lean:
`content/quantum-observable-universe/lean/QOU/Eightfold/GellMannOkuboSecondOrder.lean`,
`lean`-direct exit 0, sorry-free, standard axioms.

**The finding, which is a negative.** The $\approx 6\%$ GMO deviation cannot be
*predicted* from the second-order mass operator as currently posed, because two
measurements do not determine three coefficients.

Write the general second-order mass term with coefficients $e, f, g$ on the
three quadratic Casimir-and-hypercharge invariants. Then, proved:

- `gmo_second_order` — the octet GMO combination
  $m_{16} = \tfrac14(3 m_\Lambda + m_\Sigma) - \tfrac12(m_N + m_\Xi)$
  evaluates to exactly $16(4e - 3f)$.
- `gmo_blind_to_Yd` — **the $Y \cdot d$ invariant is exactly invisible to GMO.**
  Its coefficient drops out identically, not approximately. So the octet
  deviation constrains one linear combination $4e - 3f$ and nothing else.
- `decuplet_second_order` — the decuplet analogue is $8(4e + 9f + 6g)$, a
  *different* combination, and it is the only other measurement available.
- `decuplet_second_differences_equal` — the decuplet equal-spacing rule survives
  at second order, so it supplies no third constraint.
- Independence witnesses accompany each, so "a different combination" is proved
  rather than eyeballed.

**Consequence.** Two equations, three unknowns $(e, f, g)$. Matching both the
octet $\approx 6\%$ and the decuplet deviation is therefore **a fit with one
free parameter left over, not a prediction**, and must be labelled as such
anywhere it is reported. This is the anti-laundering rule applied to a case
where the under-determination is provable rather than suspected.

**What would close it.** A third, independent constraint on $(e, f, g)$ derived
from the categorical side — not a third measurement. Candidates worth checking
before anything else: whether the Wedderburn block structure forces a relation
among the three invariants' coefficients, and whether $g$ is forced to vanish by
a parity or bar-symmetry argument (if $g = 0$ were *proved*, two equations would
determine $e, f$ and the deviation would become a genuine prediction). Neither
is attempted here.

**Scope, per the (a)/(b) discipline.** This is scope-(a): the second-order mass
operator *as posed*, alone, does not determine the deviation. It is **not** a
structural exclusion of a second-order account — a proved relation among the
coefficients would change the verdict, which is exactly what the "what would
close it" paragraph is asking for.
