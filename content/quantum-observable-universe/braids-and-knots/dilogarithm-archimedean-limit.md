**Conjecture (Archimedean limit of the partial product).**
*Let $q$ be the substrate parameter — the QOU substrate has
$q_0 \approx 1.11$ — and let $x \in (0, 1)$ be a state variable so
that $|x q^k| < 1$ along the truncation. Let $\Phi_n(x; q)$ be the
$q$-Pochhammer partial product
([definition](#def:q-pochhammer-partial-product)).
Under the joint Faddeev scaling $q \to 1$, $n \to \infty$,
$n\lvert 1 - q\rvert \to \infty$, the rescaled logarithm of the
partial product converges to the classical dilogarithm:*

$$
  \boxed{\;
  \lim_{\substack{q \to 1 \\ n \to \infty \\ n |1-q| \to \infty}}
  (1 - q) \cdot \log \Phi_n(x; q)
  \;=\;
  \mathrm{Li}_2(x)
  \;:=\;
  -\!\int_0^x \frac{\log(1 - t)}{t}\, dt.
  \;}
$$

*The limit is taken from $q \to 1^-$ in the convergence regime
$|q| < 1$ and is extended to $q \to 1^+$ (the QOU substrate side) by
analytic continuation. Equivalently, the algebraic logarithmic
singularities of the denominator factors $(1 - x q^k)$ at
$x = q^{-k}$ converge, under the Archimedean realization
$\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$
([archimedean realization functor](#def:archimedean-realization-functor)),
to the logarithmic singularity at $t = 1$ of the integrand
$-\log(1-t)/t$ in the classical $\mathrm{Li}_2$.*

## Saddle-point story

Take logarithms inside the partial product:

$$
  \log \Phi_n(x; q)
  \;=\;
  -\!\sum_{k=0}^{n-1} \log\bigl(1 - x q^k\bigr).
$$

Setting $q = e^{-\hbar}$ and $x = e^{-y}$ and rescaling $k = s/\hbar$,
the sum becomes a Riemann sum for the integral
$\hbar^{-1}\!\int_0^{n\hbar} -\log\!\bigl(1 - e^{-y - s}\bigr)\, ds$.
Substituting $t = e^{-y-s}$ and taking $n\hbar \to \infty$ produces
$\hbar^{-1} \cdot \mathrm{Li}_2(e^{-y}) = \hbar^{-1} \cdot
\mathrm{Li}_2(x)$, so $(1 - q) \log \Phi_n(x; q) \sim \hbar
\log \Phi_n \to \mathrm{Li}_2(x)$. This is the standard
Faddeev–Kashaev quasi-classical limit
[`faddeev1994`, `kashaev1997`].

## Why it is conjectural

The rigorous statement requires:

1. **Uniform control of the Riemann-sum error** as $q \to 1$.
   Standard results give pointwise convergence; the conjecture
   asserts the convergence is uniform on compact subsets of
   $\{0 < x < 1\}$ — strong enough to commute with applications
   of $\tau_{\mathrm{arch}}$ in mass-formula evaluations.

2. **Branch-cut compatibility.** The classical $\mathrm{Li}_2$
   carries a branch cut on $[1, \infty)$; the partial product
   $\Phi_n(x; q)$ has $n$ poles approaching this cut as $q \to 1$.
   The conjecture asserts the limit is the **principal-branch**
   $\mathrm{Li}_2$, i.e. that the algebraic poles cancel against
   themselves before the limit is taken (Frobenius pairing with a
   fixed $T_w$ kills the poles above GB-depth $k_\star(T_w)$ —
   see [stratified Φ$_q$](#prop:quantum-dilogarithm-stratified)).

3. **Mathlib infrastructure.** A Lean proof would need
   `Complex.dilog`, asymptotic expansions of $q$-series, and a
   uniform Tauberian theorem — none currently formalised in
   Mathlib. The Lean theorem
   `QOU.QPochhammer.partialProduct_archimedean_limit` is therefore
   a stated identity (see CLAUDE.md §3b).

## Bridge to the geometric side

The conjecture is the **algebraic half** of the Kashaev volume
conjecture
([Kashaev volume conjecture](#conj:kashaev-volume-conjecture)).
The geometric half ([Bloch–Wigner volume](#rem:kashaev-volume-density))
asserts that $\mathrm{Im}\bigl(\mathrm{Li}_2(z) + \log z \cdot
\log(1 - z)\bigr) = D(z)$ is the hyperbolic volume of an ideal
tetrahedron with shape parameter $z$. Together, the two halves
give the QOU-native formulation of Kashaev:

$$
  \tau_{\mathrm{arch}}\!\bigl(\Phi_n(x; q_0)\bigr)
  \;\xrightarrow[\text{this conj.}]{}
  \;\mathrm{Li}_2(x)
  \;\xrightarrow[\text{Bloch-Wigner}]{}
  \;\mathrm{Vol}_{\mathrm{hyp}}(\Delta_z)
  \;=\;
  D(z),
$$

with the shape parameter $z$ matching the algebraic state variable
$x$ at the same denominator zero — the content of
[shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy).
