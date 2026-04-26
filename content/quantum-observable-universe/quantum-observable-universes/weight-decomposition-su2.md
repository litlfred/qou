Continuing [maximal torus of $\mathrm{SU}(2)$](#ex:maximal-torus-su2), we
construct the [weight decomposition](#def:weight-decomposition)
explicitly, rather than invoking existence.

**Step 1: the $T$-action on $\mathcal{O}(\mathrm{SU}(2))$.** The
maximal torus $T = \mathrm{U}(1)$ acts on the coordinate ring
$A = \mathcal{O}(\mathrm{SU}(2))$ by left translation:
$(t \cdot f)(g) = f(t^{-1}g)$ for
$t = \mathrm{diag}(e^{i\varTheta}, e^{-i\varTheta})$. On the matrix
generators $\alpha, \beta, \bar\alpha, \bar\beta$
($\alpha\bar\alpha + \beta\bar\beta = 1$), the action is diagonal:

$$
  t \cdot \alpha = e^{i\varTheta}\,\alpha, \quad
  t \cdot \beta  = e^{-i\varTheta}\,\beta, \quad
  t \cdot \bar\alpha = e^{-i\varTheta}\,\bar\alpha, \quad
  t \cdot \bar\beta  = e^{i\varTheta}\,\bar\beta.
$$

**Step 2: weight-space projectors.** For each integer weight
$m \in \mathbb{Z}$, the isotypic projector is constructed by
torus averaging:

$$
  e_m(f) = \frac{1}{2\pi}\int_0^{2\pi}
    e^{-im\varTheta}\,(t_\varTheta \cdot f)\,d\varTheta.
$$

This is a concrete integral, not an abstract existence: evaluate it
on any polynomial in $\alpha, \beta, \bar\alpha, \bar\beta$ by
collecting powers of $e^{i\varTheta}$.

**Step 3: horizontal and vertical projectors.** The horizontal
projector is $\pi_H = e_0$ (the weight-zero component); the vertical
projector is $\pi_V = \mathrm{id} - e_0 = \sum_{m \neq 0} e_m$:

- $\pi_H(\alpha^j \bar\alpha^k \beta^\ell \bar\beta^n)
  = \alpha^j \bar\alpha^k \beta^\ell \bar\beta^n$ when $j - k - \ell + n = 0$,
  and $0$ otherwise.
- $\pi_V$ picks out the complementary monomials.

For the spin-$j$ representation $V_j = \mathrm{Span}\{v_m : m = -j, \ldots, j\}$,
the weight spaces are one-dimensional: $e_m(V_j) = \mathbb{C}\,v_m$.
The decomposition on $\Omega^k(A)$ extends by the Leibniz rule
$e_m(\alpha\,d\beta) = e^{im\varTheta}\,\alpha\,d\beta$ restricted to
forms of total weight $m$.

**Verification.** Complementarity $\pi_H + \pi_V = \mathrm{id}$
holds because $\sum_{m \in \mathbb{Z}} e_m = \mathrm{id}$ (Fourier
completeness on $\mathrm{U}(1)$). Idempotency
$\pi_H^2 = \pi_H$ follows from $e_0^2 = e_0$ (orthogonality of
characters: $\frac{1}{2\pi}\int e^{i(m-n)\varTheta}d\varTheta = \delta_{mn}$).

**Bring's surface specialisation.** On the Bring coordinate ring
$\mathcal{O}_q(\mathcal{B})$ with its $S_5$ symmetry, the maximal
torus is $T = \mathrm{U}(1) \subset \mathrm{SU}_q(2)$ acting on the
quantum generators. The projectors $e_m$ are the same torus integrals
with $q$-deformed matrix coefficients
$t^j_{m,m'}(q) \in \mathcal{O}_q(\mathrm{SU}(2))$ replacing the
classical ones. The weight-zero subspace $e_0(\mathcal{O}_q(\mathcal{B}))$
consists of $S_5$-invariant combinations of the five coordinates
$x_1, \ldots, x_5$ — precisely the symmetric functions that define
Bring's curve.
