---
# qou-s4h6
title: 'GAP: GMO second-order coefficients are under-determined — two deviations, three coefficients, Y·d invisible'
status: completed
type: task
priority: normal
created_at: 2026-08-25T10:37:24Z
updated_at: 2026-08-25T11:04:40Z
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



---

**SECOND CORRECTION, same session (2026-08-25). The "third multiplet" answer
above is wrong, and this retracts it.**

The correction immediately above closed the meson case and said the baryon octet
was where the relation survives, *"which is why baryon GMO stays a genuine
relation where the meson one has gone vacuous."* Measured, then proved: **the
baryon octet is surjective too.** Both octets go vacuous at second order.

My reasoning was that $\Lambda$ and $\Sigma$ share $Y = 0$ with different $I$,
so $d$ is not a function of $Y$ on the baryon octet. The premise is true; the
**inference is backwards**. A two-dimensional $(I,Y)$ pattern makes the space of
available structures *larger*, and a larger structure space makes surjectivity
**more** likely, not less. Rank counting:

| multiplet | independent masses | rank of second-order structure space | relations |
|---|---|---|---|
| meson octet | 3 ($K^+ = K^-$ by C) | 3 | **0** |
| baryon octet | 4 | 4 | **0** |
| decuplet | 4 | 3 ($I = 1 + Y/2$ ⇒ quadratic in $Y$) | **1** |

New sorry-free declarations, all axiom-clean: `gmo_baryon_second_order` (the
baryon combination has the *same* value $16(4e-3f)$ — the two octets carry the
same $(I,Y)$ pattern), `baryon_octet_g_absorbed`,
`baryon_octet_second_order_surjective`, `gmo_baryon_surjective`.

Adversarial checks run: first-order baryon GMO **is** an identity (so there is a
real relation being destroyed, not a vacuous one); $N$ and $\Xi$ genuinely split
when $b \neq 0$, so the fourth independent mass is real and this is not a
relabelled meson octet; and the surjectivity witness reaches $N = 5, \Xi = 9$,
so it is not secretly forcing degeneracy.

**Corrected prescription — and it is not another multiplet.** Two routes:

1. A multiplet with **more independent masses than the six available
   structures**. Nothing in this corpus supplies one.
2. **Derive $e, f, g$ categorically.** The rank counting says measurement can
   *never* make the octet masses predictions at this order, in either octet: a
   structure space that spans everything absorbs any spectrum. Only theory input
   can. **This is the honest end state of front 4**, and it is a
   formalize-first prune of the whole "fit a second-order term to the deviation"
   programme rather than a task waiting to be done.

**Three corrections on this one topic in one session** — "prove $g=0$" →
"$g$ is absorbable, but a third multiplet closes it" → "no multiplet closes it,
only a derivation does." Recording that rate because it is the useful signal: each
step was a rank/degeneracy count I could have done at the start, and did not.



---

**Closing this bean (2026-08-25).** The question it was opened on is answered,
and the answer is a **prune**, not a task hand-off.

Front 4 asked whether the $\approx 6\%$ GMO deviation can be predicted by a
second-order mass term. The answer is **no, and not for want of a measurement**:
at second order the structure space spans every function on the independent
masses of **both** octets, so any spectrum whatsoever is attainable and no value
of the deviation is evidence either way. The only surviving $SU(3)$ mass
relation among the three multiplets is the decuplet's equal-second-differences
rule, and refining the structure list destroys even that (cubic structures raise
the degree past the last relation).

So there is no "third constraint" to go find — the three successive answers this
bean recorded ("prove $g = 0$", then "a third multiplet", then "neither") all
collapse to the same place. **The only route left is deriving $e, f, g$ from the
categorical side**, which is not a GMO sub-task at all: it is the framework's
standing anti-fit requirement applied to this observable, and it is gated by the
same open objects the SM surface is gated by
(`content/quantum-observable-universe/appendix-standard-model/sm-gating-objects.md`).
Opening a successor bean for "derive the $SU(3)$-breaking coefficients" would
duplicate that surface rather than add to it.

Lean: `QOU/Eightfold/GellMannOkuboSecondOrder.lean`, 14 declarations, sorry-free,
axiom-clean.
