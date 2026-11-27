A three-dimensional CR manifold also arises on the Lorentzian side. In a
four-dimensional spacetime with a shear-free congruence of null geodesics,
the space of rays inherits a CR structure, and the congruence twists exactly
when the contact form of that structure is non-degenerate
\cite{nurowski-trautman2002}. The principal congruence of the
Schwarzschild metric has no twist; that of the Kerr metric twists. Conversely,
Lewandowski, Nurowski and Tafel construct the Lorentzian metrics carrying a
given CR structure on their space of rays, and show that the vacuum Einstein
equations force the CR structure to be realizable, that is, locally embeddable
as a hypersurface in $\mathbb{C}^2$ \cite{lewandowski-nurowski-tafel1990}.

On any strictly pseudoconvex contact CR three-manifold $(M^3, H, J, \theta)$
with contact distribution $H = \ker\theta$, complex structure $J$ on $H$,
positive-definite Levi form $L_\theta$ of principal eigenvalues
$\ell_1, \ell_2 > 0$, and Reeb vector field $R_\theta$, Charles L. Fefferman's
canonical conformal circle-bundle construction \cite{fefferman1976} — in John
M. Lee's intrinsic pseudohermitian contact-form formulation \cite{lee1986} on
the canonical circle bundle $\pi \colon C(M^3) \to M^3$ with vertical
$S^1$-fibre generator $\partial_\sigma$ and connection $1$-form $\omega_0$
($\omega_0(\partial_\sigma) = 1$) — defines the symmetric bilinear metric

$$
  g_\theta(u, v)
  \;=\;
  \theta(u)\,\omega_0(v) + \theta(v)\,\omega_0(u) + L_\theta(\pi_* u, \pi_* v).
$$

Its Gram determinant $\det G_{\mathrm{Feff}} = -\ell_1 \ell_2 < 0$ is
independent of the Reeb connection shift $\omega_0(R_\theta)$, and an explicit
unimodular congruence diagonalises $g_\theta$ to
$\mathrm{diag}(-1, 1, \ell_1, \ell_2)$, establishing kinematic Lorentzian
signature $(3, 1)$ with null $S^1$-fibre $g_\theta(\partial_\sigma, \partial_\sigma) = 0$,
horizon-screen restriction $g_\theta|_H = L_\theta$, and zero tunable
parameters once $\theta$ is fixed. The $q$-exterior derivative does not select
a deformed CR structure: on functions it rescales the horizontal differential
by $q^{-1}$ and leaves both $H$ and $J$ unchanged.

This completes the relational progression initiated in the introduction
\cite{leibniz-clarke1717,earman1989} without positing a substantival
four-manifold or a classical Euclidean configuration quotient
$\mathbb{R}^{3N}/\mathrm{E}(3)$ \cite{barbour-bertotti1982}: operational
indiscernibility quotients the $n$-strand braid algebra modulo the null radical
of the Jones--Markov trace ($z = q^3/(q^2 + 1)$, nontrivial for $n \ge 3$) onto
the planar Temperley--Lieb algebra
([Temperley--Lieb trace-radical quotient](#ex:rieffel-quotient-temperley-lieb));
Marc A. Rieffel's Lipschitz seminorm built from the categorical Dirac operator
induces a faithful Kantorovich--Rubinstein transport metric on the quotient
state space
([Rieffel quotient faithfulness](#rem:rieffel-metric-quotient-faithfulness),
[Gram degeneracy](#prop:gram-degeneracy-blocks-connes)) \cite{rieffel1999}; and
the strictly pseudoconvex three-dimensional contact CR boundary lifts
canonically via $(C(M^3), g_\theta)$ to kinematic $(3, 1)$ Lorentzian signature
with Reeb chronological flow $\phi_t = \exp(t\xi)$. Along the null Killing
fibre $K = \partial_\sigma$, contact twist forces $\mathrm{Ric}(K, K) = 1/2 \neq 0$,
ruling out a vacuum Einstein metric $\mathrm{Ric} = \Lambda g_\theta$; deriving
dynamical Einstein field equations
$\delta G_{ab} k^a k^b = (8\pi G/c^4)\,\delta T_{ab} k^a k^b$ for metric
perturbations of $(C(M^3), g_\theta)$ from the categorical action is not
established in this paper and remains conjectural.
