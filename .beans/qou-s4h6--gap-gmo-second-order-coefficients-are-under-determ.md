---
# qou-s4h6
title: 'GAP: GMO second-order coefficients are under-determined — two deviations, three coefficients, Y·d invisible'
status: in-progress
type: task
priority: normal
created_at: 2026-08-25T10:37:24Z
updated_at: 2026-08-25T10:53:58Z
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



---

**CORRECTION, same day (2026-08-25). The bean above asked the wrong question, and
this is my own error being fixed within the hour.**

I wrote that GMO is "two equations, three unknowns" and named "a proof that
$g = 0$" as the third constraint that would turn the fit into a prediction.
**Proving $g = 0$ would buy nothing**, because $g$ is not an independent
parameter on either multiplet. Proved, sorry-free, in the same file:

- `meson_octet_g_absorbed` — on the octet, $b \mapsto b + g/2$ reproduces every
  mass with $g = 0$. Exactly, all four states. Reason: hypercharge $\pm 1$
  forces $I = 1/2$, so $4I(I+1) - Y^2 = 2$ and $Y \cdot d$ collapses to $2Y$.
- `decuplet_g_absorbed` — on the decuplet, $b \mapsto b + 2g$ and
  $e \mapsto e + 3g/2$. Reason: $I = 1 + Y/2$ along the ladder, so
  $4I(I+1) - Y^2 = 8 + 6Y$ identically. The $3g/2$ matches the $6g$ already
  visible in `decuplet_second_order`, checked against it.

So $g$ can be set to zero by reparametrisation and the leftover one-parameter
family is a coordinate orbit, not a physical freedom.

**And the real obstruction is stronger than under-determination.**
`meson_octet_second_order_surjective`: at second order the even-in-$Y$
structures $1, Y^2, d^2$ already span **all** functions on the three independent
meson-octet masses ($\pi$, $\eta$, and the C-degenerate kaon). Explicit witness,
with $b = c = g = 0$ so it does not even need the odd sector. Hence
`gmo_combination_surjective`: the GMO combination takes **every** value.

**The verdict changes from "a fit" to "not a prediction at all".** There is no
value of the deviation that would count as evidence for or against a second-order
term, because at second order the ansatz can produce any octet spectrum
whatsoever. Scope-**(b)** for *this ansatz*, with the invariant named: the rank
count, three independent structures on three independent masses. **Not** a claim
about $SU(3)$ breaking in general.

**What would actually close it.** Not a third constraint on the coefficients, and
not a third measurement on these two multiplets: a **third multiplet in which
isospin is not a function of hypercharge**. The baryon octet is one — $\Lambda$
and $\Sigma$ share $Y = 0$ with different $I$ — which is why baryon GMO stays a
genuine relation where the meson one has gone vacuous. Formalising the baryon
case is the next step and is **not** done here.

Note also that refining the *structure list* cannot help on the decuplet: since
$d$ is affine in $Y$ there, adding cubic structures raises the polynomial degree
and **destroys** the last surviving relation (`decuplet_second_differences_equal`)
rather than creating a new one.
