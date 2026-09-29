**Proposition.** *The discriminant of the GGM curve vanishes somewhere on the
unit circle:*

$$
\exists\, x \in \mathbb{C}, \quad \|x\| = 1 \ \text{ and } \ \mathrm{disc}(x) = 0 .
$$

*So two of the three root branches collide on the arc.*

## What this refutes

The transport argument had recorded a sub-gap as closed on the grounds that

> the three branches $y_j(x)$ are continuous and **never collide on the arc**
> ($\min|\mathrm{disc}| = 0.348$), so $g$ is continuous,

and stated the envelope theorem's implicit-function hypothesis as satisfied on
the same constant. **Both are false.**

The $0.348$ was a *grid* minimum from an $\approx 360$-point scan of $[0,\pi]$.
The dip is narrow — $|\mathrm{disc}'| \approx 87$ near the zero — so refining the
scan gives $0.068$, then $0.0068$, then $0$. A minimum over samples is a bound on
the samples, not on the function.

## Why the refutation is short

It needs no analysis of the branches at all. Three ingredients:

**The discriminant is palindromic.** Hence $\mathrm{disc}(x) = x^{4}\,Q(x + 1/x)$
with

$$
Q(u) = u^{4} - 6u^{3} + 7u^{2} + 6u - 31 ,
$$

a `field_simp; ring` identity.

**$Q$ changes sign on $(-2,-1)$.** $Q(-2) = 49 > 0 > -23 = Q(-1)$, so the
intermediate value theorem gives a real root there. (It sits at
$u \approx -1.4844$.)

**$(-2,-1)$ is reachable.** The points of $\|x\| = 1$ are exactly those with
$x + 1/x$ real in $[-2,2]$, which contains $(-2,-1)$.

So the whole argument is polynomial algebra plus one application of the IVT, and
the two evaluations are `norm_num`.

## The conclusion survives; only the argument dies

This refutes the *reasoning*, not the transport's result. $S$ sums over **all**
roots and is therefore symmetric, and a collision merely permutes the roots — a
symmetric function cannot notice a permutation. Numerically,
$S(e^{i\varphi}) - S(1) = \varphi^{2}$ holds to $4 \times 10^{-40}$ **through**
the branch point.

What dies is the per-root labelling, and only the argument used labels. This is
why the envelope statement
([`prop:fivetwo-envelope-transport`](#prop:fivetwo-envelope-transport)) is phrased
to tolerate exactly one exceptional point: that point is this collision.

## Two appearances of $-23$, one meaningful and one not

At $x = 1$ the curve degenerates to the saddle cubic $y^{3} - 2y^{2} + 3y - 1$,
so $\mathrm{disc}(1) = -23$ **is** the trace-field discriminant
([`prop:fivetwo-trace-field`](#prop:fivetwo-trace-field)) — the same object,
recovered at the base point.

$Q(-1) = -23$ as well, and that one is a coincidence: $Q$ takes the value $-23$
at $u = -1$, $u = 1$ and $u = 2$ alike, and only $u = 2$ corresponds to $x = 1$.
Nothing is claimed from the other two.
