The Iwahori--Hecke algebra where normal-form computations occur is the quotient of the braid-group algebra by the minimal polynomial of the categorical braiding.

The endomorphism $\sigma = \tau(c_{V,V})$ satisfies the Hecke relation:
$$
  (\sigma - q)(\sigma + q^{-1}) =  0,
$$
where $q$ is the braiding eigenvalue. Consequently, the Iwahori--Hecke algebra on $n$ strands over a commutative base ring $R$ containing a unit $q \in R^\times$ is:
$$
  H_n(R, q) =  R[B_n] \big/
  \bigl\langle (\sigma_i - q)(\sigma_i + q^{-1})  \big| 
  i = 1, \ldots, n{-}1 \bigr\rangle.
$$
The parameter $q$ is a fixed categorical datum determined by the braiding. The per-crossing weights $q$ and $-q^{-1}$ are exactly the eigenvalues of $\sigma$ on $S^{2} V \oplus \Lambda^{2} V$, forced by the categorical volume constraint.

Partition channels of $H_n(R, q)$ require no Wedderburn semisimplicity axiom; they arise across three distinct mathematical regimes depending on the base ring $R$:

1. **Integral and cellular regime (over $\mathbb{Z}[q, q^{-1}]$, zero inversions).** On the standard Kazhdan--Lusztig basis $\{T_w : w \in S_n\}$, Ocneanu's Markov trace $\mathrm{tr}_M \colon H_n(q) \to \mathbb{Z}[q^{\pm 1}, z^{\pm 1}]$ is defined combinatorially by the skein recursion without denominators: the hook poles of the individual partition weights cancel in the total sum. Independently, Graham--Lehrer cellularity supplies an integral two-sided cell filtration indexed by partitions $\lambda \vdash n$, integral cell (Specht) modules $S^\lambda$, canonical invariant bilinear forms $\langle -,- \rangle_\lambda$, and simple heads $L^\lambda = S^\lambda / \mathrm{rad}\,\langle -,- \rangle_\lambda$ over any commutative ring $R$, including at roots of unity and in positive characteristic.
2. **Negligible and non-semisimple regime ($\dim_q(\lambda) = 0$).** When a quantum dimension vanishes (such as the antisymmetric block $\lambda = (1^3)$ at rank $N = 2$, where $\dim_q(1^3) = 0$) or when $q$ is a root of unity where $\mathrm{rad}\,\langle -,- \rangle_\lambda \neq 0$, the Geer--Patureau-Mirand modified trace provides a non-degenerate cyclic trace on projective and ambidextrous ideals without dividing by $\dim_q(\lambda)$.
3. **Wedderburn splitting as an unconditional theorem (Dipper--James, Wenzl).** In the Laurent polynomial ring $\mathbb{Z}[q, q^{-1}]$ the group of units is $\{\pm q^k : k \in \mathbb{Z}\}$, whereas each quantum integer $[m]_q = \sum_{j=0}^{m-1} q^j$ (or its balanced counterpart) factors into cyclotomic polynomials $\Phi_d(q)$ of degree $d \ge 2$ via $q^m - 1 = (q - 1)\,[m]_q$. Whenever the quantum factorial $[n]_q!$ is invertible in $R$ --- in particular over the universal $q$-generic localization $R = \mathbb{Z}[q, q^{-1}]\bigl[\Phi_d(q)^{-1} : 2 \le d \le n\bigr]$ (which retains the classical point $q = 1$ in $\mathrm{Spec}\,R$ because $\Phi_1(q) = q - 1$ is never inverted), and **automatically for every real parameter $q > 0$** (including $q = 1$ and the physical substrate $q_0 > 1$, where every summand $q^j > 0$ makes $[m]_q > 0$ a unit in $\mathbb{R}$) --- the bilinear forms $\langle -,- \rangle_\lambda$ are non-degenerate ($\mathrm{rad}\,\langle -,- \rangle_\lambda = 0$) and the cellular filtration splits into orthogonal Wedderburn block projectors $e_\lambda \in H_n(R, q)$ as a theorem rather than an assumption.
