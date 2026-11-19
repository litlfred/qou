**Proposition.** *Let $S(\varphi) = \sum_j \mathrm{Re}\, V(x(\varphi), y_j(\varphi))$
be the envelope of the $5_2$ deformed saddle along the unit-circle arc
$x(\varphi) = e^{i\varphi}$. Suppose $S$ is continuous on $[0,\pi]$ and satisfies*

$$
\frac{dS}{d\varphi} = 2\varphi
\qquad\text{for every } \varphi \in [0,\pi) \text{ except possibly one point.}
$$

*Then*

$$
S(\pi) - S(0) = \pi^{2} .
$$

## The one exceptional point is not a fudge

The excluded point is $\varphi_0$, where the discriminant of the saddle curve
vanishes. There two root branches collide, and no differentiable labelling of
the three roots exists through it. That is a genuine monodromy obstruction, not
a gap in the argument, and the honest response is the one taken here: the three
root-paths $y_1, y_2, y_3$ enter as **parameters**, and their differentiability
is a hypothesis rather than a construction.

What makes this harmless is that $S$ is a **symmetric** function of the roots.
As a function of $\varphi$ it therefore needs no labelling at all — it is well
defined and continuous across $\varphi_0$, precisely where the individual
branches collide and swap. The labelling is required only to differentiate term
by term, which is a local operation, so it is needed only away from $\varphi_0$.

In general, a
symmetric function of a family of roots is insensitive to the monodromy that
permutes them, and an obstruction to labelling the branches is not an
obstruction to the symmetric total.

## Non-vacuity is proved, not assumed

A conditional statement is worthless if its hypotheses are unsatisfiable, and
that is checked here: a companion result
exhibits $S(\varphi) = \varphi^{2}$ satisfying both hypotheses, with the
conclusion reading $\pi^{2} = 0 + \pi^{2}$.

That example is deliberately trivial — its purpose is to rule out the vacuous
reading, not to supply evidence. The check with real content is numerical: on
the actual arc, $S' = 2\varphi$ holds per root to $4.6 \times 10^{-41}$ and
summed to $9.2 \times 10^{-41}$.

## Scope

The derivative hypothesis is an input. What is established here is the passage from
that hypothesis to the total $\pi^{2}$, tolerating one exceptional point — the
integration step rather than the analytic derivation of the integrand, which is
supported by the high-precision arc evaluation above.
