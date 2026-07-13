<!-- FILE_START: garside-gram-intro.md -->
The derived-atom examples in §5 produce specific normal forms but leave the Frobenius Gram weighting implicit. We define the typed Garside element of the nuclear braid to organize the typed crossings in staircase form. We establish the $\mathcal{Q}_q$-value as the $G^{-1}$-weighted Frobenius norm over conversion channels. This norm supplies the input for the transfer-matrix calculations in §7. We then show that the Gram eigenstructure is the adjoint character on Wedderburn blocks. This anchors the $\mathcal{Q}_q$-value in the Jucys--Murphy spectral data.
<!-- FILE_END: garside-gram-intro.md -->

<!-- FILE_START: typed-garside-element.md -->
**Definition.**
*Let $\mathcal{A}(Z, N)$ be a nucleus with $A = Z + N$ nucleons in ordering $(t_0, \ldots, t_{A-1})$ where $t_i \in \{p, n\}$. The **typed Garside element** is the element $\mathcal{G}(t_0, \ldots, t_{A-1}) \in H_A(q)$ built by the Garside staircase with typed crossings.*

**Construction.**
The Garside staircase has $A - 1$ levels. At level $\ell$, strand $\ell + 1$ crosses all earlier strands from right to left. Each crossing is typed by the nucleon pair $(t_j, t_{\ell+1})$:

```tex
\begin{equation}\label{eq:typed-garside}
  \mathcal{G}(t_0, \ldots, t_{A-1})
  \;=\;
  \prod_{\ell=0}^{A-2}
  \;\prod_{j=\ell}^{0}
  C(t_j,\, t_{\ell+1};\, \sigma_j),
\end{equation}
```

where $C(f_i, f_j; \sigma_k) = \sigma_k + d(f_i, f_j)$ is the typed crossing operator with coefficients:

$$
  d(p, p) = 0, \qquad
  d(n, n) = -(q - q^{-1}), \qquad
  d(p, n) = d(n, p) = -\tfrac{1}{2}(q - q^{-1}).
$$

The product contains $\binom{A}{2}$ factors. The result is reduced to Gröbner–Shirshov normal form under the braiding-induced ordering.

**Comparison with adjacent-only construction.**
The transfer matrix chain computes vertex volumes at each generator by chaining the crossing coefficients. This captures the same pairwise crossing data as the Garside staircase, but factored through scalar vertex volumes rather than the full $H_A(q)$ element. The typed Garside element retains the complete algebraic structure.

**Archimedean specialisation.**
This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs. Any generic categorical identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: typed-garside-element.md -->

<!-- FILE_START: gram-weighted-qvalue.md -->
**Proposition.**
*Let $\mathcal{G}_{\mathrm{par}} = \mathcal{G}(t_0, \ldots, t_{A-1})$ be the typed Garside element of the parent nucleus in $H_A(q)$. Let $G$ be the Gram matrix $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ restricted to the NF subspace spanned by $\mathcal{G}_{\mathrm{par}}$ and all conversion daughters. The $Q$-value for $\beta^-$ decay is:*

```tex
\begin{equation}\label{eq:gram-weighted-qvalue}
  Q(Z, N)
  \;=\;
  \biggl(
    \sum_{k=0}^{N-1}
    w_k^G \;\cdot\; \Delta_k
  \biggr)
  \,\times\, N \,\times\, m_e
\end{equation}
```

*where:*

1. *The sum runs over all $N$ neutrons in the parent.*
2. *$\mathcal{G}_{\mathrm{dau}}^{(k)}$ is the typed Garside element of the daughter obtained by converting neutron $k$, and*

```tex
\begin{equation}\label{eq:nf-reduction-cost}
  \Delta_k
  \;=\;
  \lVert \mathcal{G}_{\mathrm{par}} \rVert_1
  \;-\;
  \lVert \mathcal{G}_{\mathrm{dau}}^{(k)} \rVert_1
\end{equation}
```

 *is the NF reduction cost.*

3. *The Gram weight for neutron $k$ is:*

```tex
\begin{equation}\label{eq:gram-weight}
  w_k^G
  \;=\;
  \frac{
    \lVert \delta_k \rVert_F
  }{
    \sum_{j=0}^{N-1} \lVert \delta_j \rVert_F
  },
  \qquad
  \delta_k
  \;=\;
  \mathcal{G}_{\mathrm{par}} - \mathcal{G}_{\mathrm{dau}}^{(k)},
  \qquad
  \lVert \delta_k \rVert_F
  \;=\;
  \sqrt{|\delta_k \cdot G \cdot \delta_k|}
\end{equation}
```

 *where $\lVert \cdot \rVert_F$ is the Frobenius norm induced by the Gram matrix.*

**Inputs.** We require the substrate parameter $q$ and the electron mass $m_e$. There are no other parameters.

## Structure of the formula

The $Q$-value contains three factors:

- **$\Delta_k$** (NF reduction cost). This measures how much algebraic complexity the nucleus sheds when neutron $k$ converts. The daughter has fewer $nn$ crossings. Thus $\lVert \mathcal{G}_{\mathrm{dau}}^{(k)} \rVert_1 < \lVert \mathcal{G}_{\mathrm{par}} \rVert_1$ and $\Delta_k > 0$.
- **$w_k^G$** (Gram weight). The Frobenius norm of $\delta_k$ measures how far the parent sits from each daughter. Boundary neutrons produce larger $\lVert \delta_k \rVert_F$ than interior neutrons. This gives them higher weight. The weights sum to $1$.
- **$N$** (neutron count). This is the coherent sum over all conversion channels.

## Non-uniformity of the Gram weight

The Gram matrix $G$ on $H_A(q)$ is symmetric but not positive definite. It possesses both positive and negative eigenvalues. Each difference element $\delta_k$ projects onto both the positive and negative eigenspaces of $G$. Neutrons deep in the interior of the neutron shell have $\delta_k$ dominated by the negative eigenspace. This suppresses their Frobenius norm. Boundary neutrons have more balanced projections, yielding larger $\lVert \delta_k \rVert_F$. This demonstrates the adjoint character of the Frobenius algebra. The matrix $G$ acts as an averaging operator over the representation. It suppresses interior conversion channels and enhances boundary ones.
<!-- FILE_END: gram-weighted-qvalue.md -->

<!-- FILE_START: gram-weight-eigenstructure.md -->
The Gram weights $w_k^G$ arise from the eigenstructure of the Gram matrix $G$ on $H_A(q)$. They reflect the decomposition of $H_A(q)$ into irreducible representations.

## Eigendecomposition

The Gram matrix $G$ on the NF subspace of $H_A(q)$ has the eigendecomposition:

$$
  G = \sum_\alpha \lambda_\alpha \, v_\alpha v_\alpha^T
$$

The Gram matrix is not positive definite: it has both positive and negative eigenvalues.

## Projection of the conversion difference

The difference element $\delta_k = \mathcal{G}_{\mathrm{par}} - \mathcal{G}_{\mathrm{dau}}^{(k)}$ decomposes as:

$$
  \delta_k = \sum_\alpha c_{k\alpha} \, v_\alpha
$$

Its squared Frobenius norm is:

$$
  \lVert \delta_k \rVert_F^2
  = \delta_k \cdot G \cdot \delta_k
  = \sum_\alpha \lambda_\alpha \, c_{k\alpha}^2.
$$

The physical Frobenius norm $\lVert \delta_k \rVert_F = \sqrt{|\sum_\alpha \lambda_\alpha c_{k\alpha}^2|}$ is the absolute magnitude.

## Boundary vs interior suppression

The boundary neutrons have larger Frobenius norms than the interior neutrons. This non-uniformity manifests the adjoint character of the Frobenius algebra. The Gram inner product weights each conversion channel by the geometric distance between parent and daughter in $H_A(q)$.

## Connection to the Markov trace decomposition

The Markov trace decomposes over irreps as:

$$
  \mathrm{tr}_M(x)
  = \sum_\lambda \frac{z^A}{s_\lambda(q)} \, \chi_\lambda(x)
$$

The Gram matrix is the matrix of this bilinear form restricted to the NF basis. Its eigenvalues $\lambda_\alpha$ encode the Schur elements. Small eigenvalues correspond to representations with large Schur elements. Large eigenvalues correspond to representations with small Schur elements.

The Gram weight $w_k^G$ measures the change in representation content when neutron $k$ converts. A neutron whose conversion significantly reshuffles the irrep decomposition receives a larger weight than one whose conversion leaves the representation structure intact.
<!-- FILE_END: gram-weight-eigenstructure.md -->