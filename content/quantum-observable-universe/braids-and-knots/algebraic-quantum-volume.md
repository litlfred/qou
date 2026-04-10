**Definition.**
*The **algebraic quantum volume** of a braid element
$\beta \in H_n(q)$ is the product of traced volumes:*

$$
  \mathrm{Vol}_q(\beta)
  \;=\;
  \prod_{i=0}^{n-2} \hat{V}_i(q)
  \;\in\;
  \mathbb{Z}[q^{1/2}, q^{-1/2}]
$$

*where $\hat{V}_i(q) = z(q) \cdot a_i(q) + b_i(q)$ is the
traced volume of generator $i$, with $a_i(q)$ and $b_i(q)$
the Laurent polynomial entries of the transfer matrix chain
([Markov trace product](#thm:markov-trace-product)).*

*The algebraic quantum volume lives in
$\mathbb{Z}[q^{1/2}, q^{-1/2}]$ — the ring of Laurent
polynomials in $q^{1/2}$.  It is an algebraic object, not
a real number.  The archimedean (real-valued) quantum
dilogarithm is its shadow:*

$$
  \Phi_1
  \;=\;
  \ln\lvert\mathrm{Vol}_{q_0}(\beta)\rvert
  \;=\;
  \sum_{i=0}^{n-2} \ln\lvert\hat{V}_i(q_0)\rvert
$$

*The three Wedderburn invariants of the mass formula
([three-invariant mass formula](#thm:wedderburn-mass-formula))
correspond to three algebraic volumes:*

| Invariant | Algebraic volume | Ring |
|:----------|:-----------------|:-----|
| $\Phi_1$ | $\prod \hat{V}_i$ | trace of std rep |
| $\Phi_2$ | $\prod \det(M_i)$ | sym $\times$ alt product |
| $\Phi_3$ | $\prod (\lambda_i^{\mathrm{sym}}/\lambda_i^{\mathrm{alt}})$ | sym/alt ratio |

*Each factor is algebraic in $q$.  The mass formula evaluates
these products at $q_0$ and takes the logarithm:*

$$
  \mathcal{M}
  = M_{\mathrm{free}}
  + \alpha \cdot \ln\left\lvert
    \mathrm{Vol}_q^{(1)} \cdot
    \bigl(\mathrm{Vol}_q^{(2)}\bigr)^{-2[3]_q} \cdot
    \bigl(\mathrm{Vol}_q^{(3)}\bigr)^{H_A^2}
  \right\rvert_{q=q_0}
$$

*The only transcendental operation is the logarithm at the
final evaluation step.  All intermediate computations —
ground-state ordering, electron insertion, transfer matrix
chain, partition traces — are algebraic in $q$.*

*For the Habiro ring: the algebraic volume embeds into
$\widehat{\mathbb{Z}[q]}$ (the cyclotomic completion),
where it coexists with the colored Jones polynomials at all
roots of unity.  The mass at $q_0$ is the evaluation at a
non-root-of-unity point.*
