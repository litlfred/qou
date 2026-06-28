A nuclear shell at nucleon count $n \in \mathfrak{M} = \{2, 8, 20,
28, 50, 82, 126\}$ is **saturated** in the QOU framework: the
algebraic structure of the shell admits no further crossing-energy
absorption. This refactor block names the categorical content of
saturation directly, replacing matrix-evaluation evidence (Hoefsmit
seminormal forms at $k = 3, \dots, 10$, blocked at $k \geq 12$ by
combinatorial growth) with a homological / algebraic-geometry
statement about a global section.

## Notation

Let $\mathbf{C}$ be the rigid :refterm[braided monoidal category]{#braided-monoidal-category} of the QOU
substrate (Frobenius–Hopf object $A$, fibre functor $\tau$). For
$n \in \mathbb{N}$ write

* $H_n(q)$ for the Iwahori–Hecke algebra at parameter $q$, generated
 by $\sigma_1, \dots, \sigma_{n-1}$ subject to the braid relations
 and $\sigma_i^2 = (q - q^{-1}) \sigma_i + 1$
 ([AGENTS.md §7a](../../../AGENTS.md));
* $\Delta_n^2 = (\sigma_1 \sigma_2 \cdots \sigma_{n-1})^n
  \in Z(B_n)$ for the **full-twist** generator of the centre of the
 braid group, mapped under the Hecke quotient to the central
 element $\Delta_n^2 \in Z(H_n(q))$
 \cite{kassel1995, geckpfeiffer2000};
* $\Phi_n \in \mathrm{End}_{\mathbf{C}}(A^{\otimes n})$ for the
 **categorical mass endomorphism** at level $n$ —
 the global section of the mass functor over the rigid braided
 :refterm[monoidal category]{#monoidal-category}, related to the Hecke-mass element
 $\Phi_{\mathrm{mass}}$ by
 $\Phi_{\mathrm{mass}}(\beta) = (\tau \otimes \cdots \otimes \tau) \circ \Phi_n \circ \rho(\beta)$
 ([Hecke mass element](#def\:hecke-mass-element));
* $\mathfrak{M} = \{2, 8, 20, 28, 50, 82, 126\}$ for the seven
 observed nuclear magic numbers.

## Statement

**Proposition (Conjecture — categorical neutrality of saturated
shells).**
*Let $\mathbf{C}$ be a rigid :refterm[braided monoidal category]{#braided-monoidal-category} satisfying the
QOU substrate axioms ([Frobenius–Hopf substrate](#def\:frobenius-hopf-substrate))
and let $\Phi_n$ be the categorical mass endomorphism at level $n$
([mass-endomorphism conjecture](#conj\:mass-endomorphism)). Then for
every $n \in \mathfrak{M}$ the full-twist
$\Delta_n^2$ acts as the identity on $\Phi_n$:*

$$
  \Delta_n^2 \cdot \Phi_n \;=\; \Phi_n \cdot \Delta_n^2 \;=\; \Phi_n
  \qquad\text{for all } n \in \mathfrak{M}.
$$

*Equivalently, $\Phi_n \in \mathrm{End}_{\mathbf{C}}(A^{\otimes n})^{\Delta_n^2}$ —
the categorical mass at a saturated shell is a fixed point of the
full-twist action.*
