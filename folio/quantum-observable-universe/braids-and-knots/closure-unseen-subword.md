**Proposition.** *Let $R$ be a commutative ring and $A$ an $R$-algebra. Call an $R$-linear map
$t : A \to M$ a trace if $t(xy) = t(yx)$ for all $x, y \in A$, and let $[A, A]$ be the
$R$-span of all $xy - yx$.*

1. *For $a, b \in A$, every trace satisfies $t(a) = t(b)$ if and only if
   $a - b \in [A, A]$. The quotient map $A \to A/[A, A] = \mathrm{HH}_0(A)$ is the universal trace.*
2. *For a unit $u \in A$ and any $w \in A$, every trace satisfies $t(u w u^{-1}) = t(w)$.*
3. *Let $\Omega = \sum_i e_i \otimes e_i \in R^n \otimes R^n$. For every
   $X \in M_n(R)$,*

   $$
     (X \otimes 1)\,\Omega = (1 \otimes X^{\mathsf T})\,\Omega,
     \qquad
     \langle \Omega, (X \otimes 1)\,\Omega \rangle = \mathrm{tr}\,X .
   $$

**Proof.** (1) A trace vanishes on each generator $xy - yx$ of $[A, A]$, so by linearity it
vanishes on $[A, A]$; this gives the reverse direction. The quotient map
$A \to A/[A, A]$ is itself a trace, because $xy - yx \in [A, A]$. Applying the hypothesis to it
gives $a - b \in [A, A]$. (2) $u w u^{-1} - w = (uw)u^{-1} - u^{-1}(uw)$ is a commutator, so (1)
applies. (3) Both sides of the first identity have $(i, j)$ entry $X_{ij}$, and
$\langle \Omega, (X \otimes 1)\Omega \rangle = \sum_i X_{ii}$. $\square$

In the braid setting, $A = H_n(q)$ and the closure of a braid word is a trace on $A$
([Markov trace](#thm:jones-markov-trace)). Item (1) says what a closure cannot see. The
relation $a \sim b \iff a - b \in [A, A]$ is exactly the fibre of the map to
[Hochschild homology](#def:hochschild-homology) $\mathrm{HH}_0$. Item (3) is the form closure
takes on a matrix algebra: the coevaluation prepares $\Omega$, the evaluation projects onto it.
