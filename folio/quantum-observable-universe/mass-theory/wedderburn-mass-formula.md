*Let $(Z, N)$ be a neutral atom with atomic braid
$\mathcal{A} \in H_{A+Z}(q)$
([atomic braid](#def:atomic-braid)).
For each generator $i$ of the braid, let $M_i$ denote the
$2 \times 2$ transfer matrix obtained by chaining the crossing
matrices of all strands $j > i$.  Then the atomic mass is*

$$
  \mathfrak{m}(Z, N)
  =
  Z \cdot m_{\mathfrak{p}}
  + N \cdot m_{\mathfrak{n}}
  + Z \cdot m_e
  + \alpha\bigl(
      \Phi_1
      - 2[3]_q \cdot \Phi_2
      + h_{\mathrm{A}}^2 \cdot \Phi_3
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
blocks of $H_n(R, q)$ (those associated with the symmetric $[n]$, standard
$[n{-}1,1]$, and alternating $[1^n]$ representations).  These three
extremal blocks exhaust the partition lattice if and only if $n \le 3$
($p(1)=1$, $p(2)=2$, $p(3)=3$, proved in Lean as
`extremal_exhausts_iff_n_le_three`); already at $n = 4$ ($p(4)=5$), two
non-extremal blocks $[2,2]$ and $[2,1,1]$ enter
(`non_extremal_irreps_at_n_eq_four`), and for $A \ge 3$ nucleons the
adjacent-chain bridge count $A - 1$ grows strictly slower than the
all-pairs count $A(A-1)/2$ (`adjacentChain_twice_lt_allPairs_twice`).
The partition-by-partition computation (the formal derivation) computes
all partitions exactly via Young's seminormal form in polynomial time.
The mass functional uses the three extremal invariants as the
leading-order formula; the full partition sum gives the exact Markov
trace.*

*The coefficients are:*
- *$\alpha = m_e \times 8G$
  ([binding scale](#conj:binding-scale-catalan)),*
- *$[3]_q = (q^3 - q^{-3})/(q - q^{-1})$, the quantum 3-integer
  ([degree-2 weight](#prop:degree-two-baryon-weight)),*
- *$h_{\mathrm{A}} = q - q^{-1}$, the Hecke parameter, satisfying the exact
  algebraic dependency $h_{\mathrm{A}}^2 = [3]_q - 3$, i.e.
  $2\beta_3 + \beta_2 + 6 = 0$ where $\beta_2 = -2[3]_q$ and
  $\beta_3 = h_{\mathrm{A}}^2$ (`QOU.Mass.WedderburnMassFormulaCoefficients.beta3_of_beta2`).*

*All quantities are derived from $q_0$ and $m_e$.  The formula has
zero fitted parameters.*
