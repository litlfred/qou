A **threading link** is a single torus link that passes through
all atoms in a molecular ring simultaneously, replacing the
pairwise Hopf link picture with a non-local, correlated binding
structure.

**Definition.**
Let $\mathcal{A}_1, \ldots, \mathcal{A}_N$ be atoms arranged in
a cycle.  The **threading link** of the ring is the torus link

$$
  \mathcal{T}_N =  T(2, N),
$$

whose closure in the braid group $B_N$ is

$$
  \hat{\beta}_N
  = 
  (\sigma_1  \sigma_2  \cdots  \sigma_{N-1})^2.
$$

The threading link winds **twice** around the torus defined by
the $N$ atoms, passing through every atom on each winding.  It
has $2(N-1)$ crossings in the standard braid representation —
all of the same sign.

**Component structure.**
The number of components of $T(2,N)$ is $\gcd(2,N)$:

| $N$ | $\gcd(2,N)$ | Components | Each component |
|:---:|:---:|:---:|---|
| odd | 1 | 1 (knot) | $T(1, N)$ — unknot wrapping $N$ times |
| even | 2 | 2 (link) | each unknotted, wrapping $N/2$ times |

For even $N$ (the case of benzene, $N = 6$), the threading link
is a **2-component link**: two unknotted loops, each threading
through all $N$ atoms.  These two components are the topological
realisation of the two delocalised $\pi$ electrons.

**Alexander polynomial.**
To read off how the winding structure distinguishes threading
links of different ring sizes, we record the Alexander polynomial
of $T(2,N)$ — the standard topological invariant of the link — and
evaluate it at the substrate parameter, where the resulting
$q$-symmetric Laurent polynomial tracks the winding count $m = N/2$.
The Alexander polynomial of $T(2,N)$ for even $N = 2m$ is

$$
  \Delta_{T(2,2m)}(t)
  = 
  \frac{t^m - t^{-m}}{t - t^{-1}}.
$$

Evaluated at the substrate parameter $t = q$:

| Threading | $m$ | $\Delta(q)$ |
|-----------|:---:|-------------|
| $T(2,2)$ (Hopf) | 1 | $1$ |
| $T(2,4)$ | 2 | $q + q^{-1}$ |
| $T(2,6)$ | 3 | $q^2 + 1 + q^{-2}$ |
| $T(2,8)$ | 4 | $q^3 + q + q^{-1} + q^{-3}$ |
