*The $q$-deformation lifts the mass degeneracy of the meson octet.
The eight states share the same hexagonal weight pattern but their
masses split through the quantum dimension and crossing-energy
formulas of the Hecke algebra.*

The meson octet decomposition ($\mathbf{3} \otimes \bar{\mathbf{3}} =
\mathbf{8} \oplus \mathbf{1}$) determines *which* states exist.
The mass splitting of these states is a separate, $q$-dependent
phenomenon governed by the Markov trace and the crossing energy.

**$q$-independent structure.**
The weight lattice and the state assignments (which meson sits at
which $(I_3, Y)$) are $q$-independent
([Remark](#rem:q-deformation-weight-lattice)).
The hexagonal pattern itself --- $\pi^\pm$ at $(\pm 1, 0)$,
$K^\pm$ at $(\pm 1/2, \pm 1)$, $\pi^0$ and $\eta$ at the origin
--- is determined entirely by the Cartan matrix $A_2$, which the
Hecke relation encodes independently of $q$.

**$q$-dependent dynamics.**
Within the hexagonal pattern, the physical masses are governed by
three $q$-dependent ingredients:

1. **Quantum dimensions:** $\dim_q(V_\lambda) = \prod_{\alpha > 0}
   [\langle \lambda + \rho, \alpha^\vee \rangle]_q /
   [\langle \rho, \alpha^\vee \rangle]_q$.
   At $q = 1$ these reduce to the classical dimensions (all integer);
   at $q \neq 1$ they split.
2. **Crossing energy:**
   $\mathfrak{E}_\times(q) = \tfrac{1}{2}(q - q^{-1})$, the
   energy cost per crossing in the Hecke algebra.  This governs
   the mass contribution from each braid crossing in the meson's
   knot representative.
3. **Markov trace weights:**
   $\tau_q(\beta)$ assigns a $q$-dependent amplitude to each braid
   $\beta$, producing the mass endomorphism via the Frobenius
   integral.

**The Gell-Mann--Okubo mass formula.**
In standard $\mathrm{SU}(3)_{\mathrm{f}}$ flavour physics, the meson masses obey the
Gell-Mann--Okubo relation
$$
  4 m_K^2 = 3 m_\eta^2 + m_\pi^2.
$$

**Gell-Mann--Okubo cannot test this.** The relation is not something the
framework should *derive*, and its $\approx 6\%$ experimental deviation
is not comparable with the $\approx 3.3\%$ figure from the
$q$-deformation of the adjoint quantum dimension.

First-order $\mathrm{SU}(3)_{\mathrm{f}}$ breaking means the mass operator is a
singlet plus an octet piece transforming like $\lambda_8$, so that
$$
  m^2(I, Y) \;=\; a \;+\; b\,Y \;+\; c\left(I(I+1) - \tfrac{Y^2}{4}\right)
$$
for *some* constants $a, b, c$.  Evaluated on the pseudoscalar octet
--- $\pi$ at $(I,Y) = (1,0)$, $K$ at $(\tfrac12, \pm 1)$, $\eta$ at
$(0,0)$ --- the Gell-Mann--Okubo combination collapses identically:
$$
  4m_K^2 - 3m_\eta^2 - m_\pi^2 \;=\; 0
  \qquad\text{for \emph{all} } a, b, c .
$$
This is proved over any commutative ring, together with the sharper
consequence that two arbitrarily different breaking
patterns give the *same* value of the combination, namely zero.  In
particular $b$ --- the entire hypercharge dependence, which is the whole
content of a breaking mechanism --- cancels
.

Two consequences.  First, if the QOU crossing-energy splitting is
first-order octet then it reproduces Gell-Mann--Okubo automatically and
exactly, and doing so is **not evidence** for the framework: every
first-order octet model reproduces it equally well
\cite{gellmann1962,okubo1962}.  Second, the only testable content is the
$\approx 6.4\%$ *deviation*, which measures the failure of first-order
breaking through second-order operators and $\eta$--$\eta'$ singlet mixing.

**Second-order quantum Casimir curvature versus singlet mixing.**
An unconstrained second-order polynomial in $(I(I+1), Y)$ surjects onto
every scalar residual over $\mathbb{Q}$, so a second-order fit carries
no separating power unless the operator is fixed in advance.  Replacing
the classical isospin Casimir by the parameter-free rational quantum
Casimir $d_q(I, Y) = [I]_q[I+1]_q - [Y/2]_q^2$ \cite{kleinkreisler1996}
(which evaluates over any field without square roots to $d_q(1,0) =
q + q^{-1}$, $d_q(0,0) = 0$, and $d_q(\tfrac{1}{2}, \pm 1) =
(q + q^{-1})/(q + 2 + q^{-1})$) yields an $(a, b, c)$-independent ratio
for $M(I, Y) = a + b\,Y + c\,d_q(I, Y)$ ($c \neq 0$):
$$
  \frac{4 M_K - 3 M_\eta - M_\pi}{M_\pi - M_\eta}
  \;=\;
  -\left(\frac{q - 1}{q + 1}\right)^{\!2}
  \;=\;
  -\frac{(q - q^{-1})^2}{([2]_q + 2)^2}.
$$
At $q_0$, this bar-even ratio equals $-2.7168 \times 10^{-3}$.  Because
$m_\pi^2 - m_\eta^2 < 0$ on the pseudoscalar octet whereas $m_\Sigma -
m_\Lambda > 0$ on the baryon octet, the same negative factor predicts the
observed sign on *both* octets simultaneously ($4m_K^2 - 3m_\eta^2 -
m_\pi^2 > 0$ and $2(m_N + m_\Xi) - 3m_\Lambda - m_\Sigma < 0$).  In
magnitude, however, single-$q_0$ isospin curvature accounts for only
$1.21\%$ of the observed $6.43\%$ isospin-averaged meson deviation
(normalized ratio $-0.2247$) and $0.82\%$ of the $-0.57\%$ baryon
deviation (normalized ratio $-0.3330$), confirming that $\eta$--$\eta'$
singlet mixing and higher-order $\mathrm{SU}(3)_{\mathrm{f}}$ breaking dominate
the empirical residual.

The $\approx 3.3\%$ figure is not a competing prediction.  It is the
$q$-deformation of $\dim_q$ of the adjoint, a *dimension* rather
than a mass splitting, and not a quantity that can appear on either side
of the relation.  Comparing the two numbers was a category error, and the
comparison is withdrawn.

**Ordered 3-strand gluon clasp for neutral flavours.**
Two-strand torus closures $T(2, n)$ have vanishing hyperbolic volume and
cannot distinguish an ordered constituent pair $(n_1, n_2)$ from its
swap $(n_2, n_1)$ under symmetric content maps.  Mapping the ordered
antiquark--quark generation pair $(n_1, n_2) \in \{3, 5, 7\}^2$ to the
parameter-free 3-strand gluon-clasp braid
$\beta_{\mathrm{clasp}}(n_1, n_2) = \sigma_1^{n_1}\sigma_2^{-n_2}\sigma_1\sigma_2^{-1} \in B_3$
gives $\mathrm{SL}_2(\mathbb{Z})$ monodromy determinant $1$ and trace
$2 n_1 n_2 + n_1 + n_2 + 3 \in \{27, 41, 55, 63, 85, 115\} > 2$
(strictly pseudo-Anosov across all nine generation pairs, while the
real-aether $S^{(2,1)}$ trace at $q_0$ stays inside $(-0.760, -0.291)$
near its $q = 1$ value $-1$).  Although the $2 \times 2$ $S^{(2,1)}$
trace is symmetric under $n_1 \leftrightarrow n_2$, both the rank-$2$
($z_2$) and rank-$3$ ($z_3$) full $H_3(q)$ Markov traces separate
$\bar D^0 \mapsto (5, 3)$ from $K^0 \mapsto (3, 5)$ by exact closed-form
multiples of $q^2 - q^{-2}$ ($+0.2125$ at $z_2$ and $+0.1442$ at $z_3$
for $q = q_0$).

**Conditional on $N = 3$ and on $Y$.**
Mass splittings between isospin multiplets (for example $\pi$ against
$K$) depend on the hypercharge $Y$, which is open
([the flavour-representations section](#sec:flavor-representations)).
Within an isospin multiplet (for example $K^+$ against $K^0$), the
splitting is purely electromagnetic and arises from the writhe
difference, which is derived.
