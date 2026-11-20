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
This is proved over any commutative ring in
`QOU/Eightfold/GellMannOkuboIdentity.lean`
, together with the sharper consequence
`gmo_cannot_discriminate`: two arbitrarily different breaking
patterns give the *same* value of the combination, namely zero.  In
particular $b$ --- the entire hypercharge dependence, which is the whole
content of a breaking mechanism --- cancels
.

Two consequences.  First, if the QOU crossing-energy splitting is
first-order octet then it reproduces Gell-Mann--Okubo automatically and
exactly, and doing so is **not evidence** for the framework: every
first-order octet model reproduces it equally well.  Second, the only
testable content is the $\approx 6\%$ *deviation*, which measures
the failure of first-order breaking --- second-order terms and
$\eta$--$\eta'$ singlet mixing.  The framework has derived no
second-order term, so it currently predicts deviation $0$.

The $\approx 3.3\%$ figure is not a competing prediction.  It is the
$q$-deformation of $\dim_q$ of the adjoint, a *dimension* rather
than a mass splitting, and not a quantity that can appear on either side
of the relation.  Comparing the two numbers was a category error, and the
comparison is withdrawn.

**Conditional on $N = 3$ and on $Y$.**
Mass splittings between isospin multiplets (for example $\pi$ against
$K$) depend on the hypercharge $Y$, which is open
([the flavour-representations section](#sec:flavor-representations)).
Within an isospin multiplet (for example $K^+$ against $K^0$), the
splitting is purely electromagnetic and arises from the writhe
difference, which is derived.
