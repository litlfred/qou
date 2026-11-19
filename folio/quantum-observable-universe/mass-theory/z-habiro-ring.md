**Definition (z-Habiro ring).**
*Let $R = \mathbb{Z}[q^{\pm 1}][z]$. The **$z$-Habiro ring** $\widehat{\mathbb{Z}[q^{\pm 1}][z]}_z$ is the inverse limit of the quotient rings $R / (P_n(q, z))$ as $n \to \infty$, where $P_n(q, z) = \prod_{k=1}^n (1 - q^{-k}z)$ is the $z$-Pochhammer analog:*

$$
  \widehat{\mathbb{Z}[q^{\pm 1}][z]}_z
  \;:=\;
  \varprojlim_n \frac{\mathbb{Z}[q^{\pm 1}][z]}{(P_n(q, z))}.
$$

*Elements are formal series $\sum_{n=0}^\infty c_n(q, z) \, P_n(q, z)$ with $c_n \in \mathbb{Z}[q^{\pm 1}][z]$.*

The $z$-Habiro ring provides the algebraic completion needed to formalize the brane-tower contributions. The infinite product $\Phi_q(z) = \prod_{k\geq 1} (1 - q^{-k}z)^{-1}$ is ill-defined as a polynomial but exists as a formal limit within this completion.

**Role in the mass formula.** The transient (brane-tower) component of the Hecke mass element resides in the $z$-Habiro ring. Its evaluation at physical $(q, z)$ values relies on the algebraic truncation properties of this ring.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs (real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$). Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
