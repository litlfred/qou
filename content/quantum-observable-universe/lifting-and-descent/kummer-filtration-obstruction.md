The Yekutieli obstruction classes $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ ([quantum characteristic classes](#def:quantum-characteristic-classes)) reside in the second cohomology of the state bundle with coefficients in the band $\mathcal{B} = \mathcal{O}_M^\times$. In the archimedean realisation, $\mathcal{B} = \mathbb{G}_m$, the multiplicative group scheme. The torsion structure of $\mathbb{G}_m$ imposes a natural filtration on the obstruction space.

**The Kummer exact sequence.** For each integer $n \geq 1$, the $n$-th power map on $\mathbb{G}_m$ fits into a short exact sequence of sheaves on $\mathcal{S}$:
$$
  1  \longrightarrow  \mu_n
   \longrightarrow  \mathbb{G}_m
  \xrightarrow{(\cdot)^n}
  \mathbb{G}_m
   \longrightarrow  1.
$$
The group scheme $\mu_n = \{\zeta \in \mathbb{G}_m : \zeta^n = 1\}$ consists of the $n$-th roots of unity. The associated long exact sequence in cohomology provides a connecting homomorphism and a reduction map at every level $n$:
$$
  \cdots  \to 
  H^1(\mathcal{S}, \mathbb{G}_m)
  \xrightarrow{\partial}
  H^2(\mathcal{S}, \mu_n)
   \to 
  H^2(\mathcal{S}, \mathbb{G}_m)
  \xrightarrow{(\cdot)^n}
  H^2(\mathcal{S}, \mathbb{G}_m)
   \to  \cdots
$$
The **Kummer reduction** of an obstruction class $\kappa$ at level $n$ is its image under the quotient:
$$
  \kappa \bmod n
   \in 
  H^2(\mathcal{S}, \mathbb{G}_m)
  \big/
  nH^2(\mathcal{S}, \mathbb{G}_m).
$$
This reduction measures whether $\kappa$ is $n$-divisible in the obstruction group.
