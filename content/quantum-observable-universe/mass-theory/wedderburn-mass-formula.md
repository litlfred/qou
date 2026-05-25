**Theorem.**
*Let $(Z, N)$ be a neutral atom with atomic braid
$\mathcal{A} \in H_{A+Z}(q)$
([atomic braid](#def:atomic-braid)).
For each generator $i$ of the braid, let $M_i$ denote the
$2 \times 2$ transfer matrix obtained by chaining the crossing
matrices of all strands $j > i$.  Then the atomic mass is*

$$
  \mathcal{M}(Z, N)
  =
  Z \cdot m_{\mathfrak{p}}
  + N \cdot m_{\mathfrak{n}}
  + Z \cdot m_e
  + \alpha\bigl(
      \Phi_1
      - 2[3]_q \cdot \Phi_2
      + H_A^2 \cdot \Phi_3
    \bigr)
$$

*where:*

$$
  \Phi_1 = \sum_i \ln\bigl\lvert
    z \cdot (M_i)_{12} + (M_i)_{22}
  \bigr\rvert,
  \qquad
  \Phi_2 = \sum_i \ln\bigl\lvert
    \det M_i
  \bigr\rvert,
  \qquad
  \Phi_3 = \sum_i \ln\left\lvert
    \frac{\lambda_i^{\mathrm{sym}}}
         {\lambda_i^{\mathrm{alt}}}
  \right\rvert.
$$

*The three invariants correspond to the three Wedderburn blocks of
$H_n(R, q)$:*

| Invariant | Wedderburn block | Matrix quantity |
|:----------|:-----------------|:----------------|
| $\Phi_1$ | standard (dim $n{-}1$) | trace of Markov-weighted product |
| $\Phi_2$ | sym $\times$ alt | determinant (product of eigenvalues) |
| $\Phi_3$ | sym $/$ alt | ratio of eigenvalues (chirality) |

*The three invariants correspond to the three **extremal** Wedderburn
blocks of $H_n(R, q)$ (those associated with the symmetric, standard,
and alternating representations).  For $n \geq 4$, the Hecke algebra
has additional irreducible representations (one per partition of $n$),
producing additional invariants not captured by the $2 \times 2$
transfer matrix.  The partition-by-partition computation
(`atom_mass_partition.py`) computes all partitions exactly via
Young's seminormal form in polynomial time.  The mass functional
uses the three extremal invariants as the leading-order formula;
the full partition sum gives the exact Markov trace.*

*The coefficients are:*
- *$\alpha = m_e \times 8G$
  ([binding scale](#prop:binding-scale-catalan)),*
- *$[3]_q = (q^3 - q^{-3})/(q - q^{-1})$, the quantum 3-integer
  ([degree-2 weight](#prop:degree-two-baryon-weight)),*
- *$H_A = q - q^{-1}$, the Hecke parameter.*

*All quantities are derived from $q_0$ and $m_e$.  The formula has
zero fitted parameters.*

*Proof sketch.*
The Wedderburn-Artin decomposition
$H_n(R, q) \cong M_1(R) \oplus M_{n-1}(R)
\oplus M_1(R)$
([three-parameter decomposition](#prop:three-parameters-wedderburn))
gives three independent representations.  The crossing matrix
$C = c \cdot \sigma_i + d \cdot \mathbf{1}$ has:

- symmetric eigenvalue $\lambda^{\mathrm{sym}} = cq + d$,
- alternating eigenvalue $\lambda^{\mathrm{alt}} = -c/q + d$,
- standard representation: the $2 \times 2$ matrix
  $\bigl[\begin{smallmatrix}
    c \cdot H_A + d & c \\ c & d
  \end{smallmatrix}\bigr]$.

The trace $\hat{V}_i = z \cdot a + b$ gives $\Phi_1$.
The determinant $\det M_i = \lambda^{\mathrm{sym}} \cdot
\lambda^{\mathrm{alt}}$ gives $\Phi_2$.
The ratio $\lambda^{\mathrm{sym}} / \lambda^{\mathrm{alt}}$ gives
$\Phi_3$.

The weight $-2[3]_q$ of $\Phi_2$ is derived from the baryon
structure: the three quark color channels produce pairwise products
whose count $\binom{3}{2} = 3$ is $q$-deformed to $[3]_q$, with
factor $2$ from the pn crossing doubling convention.
$\square$

**Witness**: `atom-mass-complete-wedderburn.witness.json`.
