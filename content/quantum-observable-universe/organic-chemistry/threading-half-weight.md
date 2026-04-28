**Statement.**
For every even integer $N = 2m \ge 2$,

$$
  \lim_{q \to 1}\, \frac{\Delta_{T(2,2m)}(q)}{N}
   = 
  \frac{1}{2}.
$$

In other words, in the classical limit the threading link's Alexander
weight is exactly **one half** of the pairwise-Hopf weight $N$.

**Proof.**
By [closed form of $\Delta_{T(2,N)}(q)$](#lem:alexander-T2N-closed-form),
for $N = 2m$ the Alexander polynomial is the symmetric Laurent
polynomial
$\Delta_{T(2,2m)}(q) = q^{m-1} + q^{m-3} + \cdots + q^{-(m-1)}$,
which has $m$ terms.  Specialising at $q = 1$ gives
$\Delta_{T(2,2m)}(1) = m = N/2$, and the limit is therefore $1/2$.
$\square$

**Significance.**
This factor of $\tfrac{1}{2}$ is the **central topological claim** of
the chapter: it propagates directly into the molecular crossing
energy and halves the predicted ring-closure barrier relative to the
pairwise-Hopf prediction (compare
[ring-closure energy barrier](#prop:ring-closure-barrier)).  Without
it, the chain $\to$ ring transition would be energetically neutral
rather than favourable.

The witness `alexander-weight-ratio.witness.json` records both the
symbolic limit and the numerical deviation at the substrate value
$q_0$ for $N = 2, 4, 6, 8, 10, 12, 14$.
