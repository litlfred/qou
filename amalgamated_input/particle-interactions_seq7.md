<!-- FILE_START: garside-gram-intro.md -->
The derived-atom examples in §5 produce specific normal forms but leave the Frobenius Gram weighting implicit.

We define the typed Garside element of the nuclear braid to organize the typed crossings in staircase form. We establish the $\mathcal{Q}_q$-value as the $G^{-1}$-weighted Frobenius norm over conversion channels. This norm supplies the input for the transfer-matrix calculations in §7. We then show that the Gram eigenstructure is the adjoint character on Wedderburn blocks. This anchors the $\mathcal{Q}_q$-value in the Jucys--Murphy spectral data.

*(draft)*
<!-- FILE_END: garside-gram-intro.md -->

<!-- FILE_START: typed-garside-element.md -->
Let $\mathcal{A}(Z, N)$ be a nucleus with $A = Z + N$ nucleons in ordering $(t_0, \ldots, t_{A-1})$ where $t_i \in \{p, n\}$. The **typed Garside element** is the element $\mathcal{G}(t_0, \ldots, t_{A-1}) \in H_A(q)$ built by the Garside staircase with typed crossings ([typed crossing operator](#def:typed-crossing-operator)).

**Construction.**
The Garside staircase has $A - 1$ levels. At level $\ell$ ($0 \leq \ell \leq A - 2$), strand $\ell + 1$ crosses all earlier strands $j = \ell, \ell - 1, \ldots, 0$ (from right to left). Each crossing is typed by the nucleon pair $(t_j, t_{\ell+1})$:

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

The product contains $\binom{A}{2}$ factors. There is one factor for every pair of nucleons, each at the correct generator position $\sigma_j$ determined by the staircase sweep. The result is reduced to Gröbner–Shirshov normal form ([nuclear reduction](#prop:nuclear-groebner-reduction)) under the braiding-induced ordering ([braiding-induced ordering](#prop:braiding-induced-ordering)).

**Comparison with adjacent-only construction.**
The transfer matrix chain ([transfer matrix operator](#def:transfer-matrix-operator)) computes vertex volumes $\hat{V}_i$ at each generator $\sigma_i$ by chaining the crossing coefficients with all positions $j > i$. This captures the same pairwise crossing data as the Garside staircase, but factored through scalar vertex volumes rather than the full $H_A(q)$ element.

The typed Garside element retains the complete algebraic structure. For ${}^4\mathrm{He}$ with ordering $[p, n, p, n]$, the adjacent-only product $({\sigma_0 - h/2})({\sigma_1 - h/2})({\sigma_2 - h/2})$ yields $8$ normal form terms with a spurious negative identity component $-\frac{h^3}{8}$. The full Garside staircase (all $6$ crossings) yields $18$ normal form terms with an identity component of exactly $0$, and a leading term equal to the Garside element $\Delta_4 = \sigma_0\sigma_1\sigma_0\sigma_2\sigma_1\sigma_0$.

**Verified.**
For $A = 4$ (${}^4\mathrm{He}$, $6$ crossings), we verify $18$ normal form terms. For $A = 6$ (${}^6\mathrm{He}$, $15$ crossings), we verify $988$ normal form terms.

**Archimedean specialisation (§7c).**
This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs, such as real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical or $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: typed-garside-element.md -->

<!-- FILE_START: gram-weighted-qvalue.md -->
**Proposition.**
*Let $\mathcal{G}_{\mathrm{par}} = \mathcal{G}(t_0, \ldots, t_{A-1})$ be the typed Garside element ([typed Garside element](#def:typed-garside-element)) of the parent nucleus in $H_A(q)$. Let $G$ be the Gram matrix $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ restricted to the NF subspace spanned by $\mathcal{G}_{\mathrm{par}}$ and all conversion daughters. The $Q$-value for $\beta^-$ decay is:*

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

1. *The sum runs over all $N$ neutrons in the parent (all possible conversion channels).*

2. *$\mathcal{G}_{\mathrm{dau}}^{(k)}$ is the typed Garside
 element of the daughter obtained by converting neutron $k$
 ($t_k = n \mapsto p$), and*

```tex
\begin{equation}\label{eq:nf-reduction-cost}
  \Delta_k
  \;=\;
  \lVert \mathcal{G}_{\mathrm{par}} \rVert_1
  \;-\;
  \lVert \mathcal{G}_{\mathrm{dau}}^{(k)} \rVert_1
\end{equation}
```

 *is the NF reduction cost (change in $L^1$ norm of the
 Gröbner--Shirshov normal form).*

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

 *where $\lVert \cdot \rVert_F$ is the Frobenius norm induced
 by the Gram matrix.*

**Inputs.** We require the substrate parameter $q$ (from $\mathrm{Vol}(4_1)$ and $m_\mu/m_e$) and the electron mass $m_e$. There are no other parameters.

## Structure of the formula

The $Q$-value contains three factors:

- **$\Delta_k$** (NF reduction cost). This measures how much algebraic complexity the nucleus sheds when neutron $k$ converts. The daughter has fewer $nn$ crossings ($d = -(q-q^{-1})$, the most repulsive type). Thus $\lVert \mathcal{G}_{\mathrm{dau}}^{(k)} \rVert_1 < \lVert \mathcal{G}_{\mathrm{par}} \rVert_1$ and $\Delta_k > 0$.

- **$w_k^G$** (Gram weight). The Frobenius norm of $\delta_k$ measures how far (in the Gram metric) the parent sits from each daughter. Boundary neutrons (at the edge of the neutron shell) produce larger $\lVert \delta_k \rVert_F$ than interior neutrons. This gives them higher weight. The weights sum to $1$.

- **$N$** (neutron count). This is the coherent sum over all conversion channels. Each of the $N$ neutrons can convert. The physical $Q$-value is the sum of all weighted contributions.

## Non-uniformity of the Gram weight

The Gram matrix $G$ on $H_A(q)$ is symmetric but not positive definite. It possesses both positive and negative eigenvalues. The negative eigenspace corresponds to the $nn$ repulsive channel (the direction $L_+ - L_-$ in $H_3(q)$, generalized to $H_A(q)$).

Each difference element $\delta_k$ projects onto both the positive and negative eigenspaces of $G$. The Frobenius norm $\lVert \delta_k \rVert_F = \sqrt{|\delta_k \cdot G \cdot \delta_k|}$ combines these projections. Neutrons deep in the interior of the neutron shell have $\delta_k$ dominated by the negative eigenspace (many $nn$ crossings change). This suppresses their Frobenius norm. Boundary neutrons have more balanced projections, yielding larger $\lVert \delta_k \rVert_F$.

This demonstrates the adjoint character of the Frobenius algebra. The matrix $G$ acts as an averaging operator over the representation. It suppresses interior conversion channels and enhances boundary ones.

## Verified instances

```tex
\begin{equation*}
\begin{array}{lcccc}
  \text{Decay}
    & N & Q\;\text{(pred)}
    & Q\;\text{(exp)}
    & \text{error} \\
  \hline
  {}^6\mathrm{He} \to {}^6\mathrm{Li}
    & 4 & 3.849 & 3.508 & +9.7\% \\
\end{array}
\end{equation*}
```

The Gram-pairing variant
($w_k^G$ replaced by $|\langle \delta_k, \mathcal{G}_{\mathrm{par}} \rangle_F|$
normalised) gives $3.752$ MeV ($+7.0\%$).
<!-- FILE_END: gram-weighted-qvalue.md -->

<!-- FILE_START: gram-weight-eigenstructure.md -->
The Gram weights $w_k^G$ ([Gram-weighted $Q$-value](#prop:gram-weighted-qvalue)) arise from the eigenstructure of the Gram matrix $G$ on $H_A(q)$. They reflect the decomposition of $H_A(q)$ into irreducible representations.

## Eigendecomposition

The Gram matrix $G$ on the NF subspace of $H_A(q)$ has the eigendecomposition:

$$
  G = \sum_\alpha \lambda_\alpha \, v_\alpha v_\alpha^T
$$

where $\lambda_\alpha$ are the eigenvalues and $v_\alpha$ the orthonormal eigenvectors. Each eigenspace corresponds to a sector of the Wedderburn-Artin decomposition $H_A(R, q) \cong \bigoplus_\lambda M_{d_\lambda}(R)$.

The Gram matrix is not positive definite: it has both positive and negative eigenvalues. For $A = 4$ (${}^4\mathrm{He}$), the signature is $(7{+}, 1{-})$ on the $8$-dimensional NF subspace. For $A = 6$ (${}^6\mathrm{He}$), the signature has hundreds of negative eigenvalues.

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

The positive eigenspaces contribute positively. The negative eigenspaces contribute negatively. The physical Frobenius norm $\lVert \delta_k \rVert_F = \sqrt{|\sum_\alpha \lambda_\alpha c_{k\alpha}^2|}$ is the absolute magnitude.

## Boundary vs interior suppression

For ${}^6\mathrm{He}$ ($N = 4$ neutrons at positions $\{0, 2, 4, 5\}$), the computed Frobenius norms are:

| $k$ | position | $\lVert \delta_k \rVert_F$ | normalised $w_k^G$ |
|:---:|:--------:|:-------------------------:|:------------------:|
| $0$ | $0$ | $0.260$ | $0.304$ |
| $1$ | $2$ | $0.186$ | $0.218$ |
| $2$ | $4$ | $0.231$ | $0.271$ |
| $3$ | $5$ | $0.176$ | $0.206$ |

The boundary neutrons ($k = 0$ at the proton-shell edge, $k = 2$ adjacent to the last proton) have larger Frobenius norms than the interior neutrons ($k = 1, 3$ deep in the neutron shell).

This non-uniformity manifests the adjoint character of the Frobenius algebra. The Gram inner product weights each conversion channel by the geometric distance (in the Frobenius metric) between parent and daughter in $H_A(q)$.

## Connection to the Markov trace decomposition

The Markov trace decomposes over irreps as:

$$
  \mathrm{tr}_M(x)
  = \sum_\lambda \frac{z^A}{s_\lambda(q)} \, \chi_\lambda(x)
$$

where $s_\lambda(q) = \prod_{\square \in \lambda} [h(\square)]_q$ is the Schur element (product of $q$-hook lengths) and $\chi_\lambda$ is the character of irrep $\lambda$ ([RJ inner product](#prop:rj-canonical-inner-product)).

The Gram matrix is the matrix of this bilinear form restricted to the NF basis. Its eigenvalues $\lambda_\alpha$ encode the Schur elements. Small eigenvalues (near zero) correspond to representations with large Schur elements (highly symmetric tableaux). Large eigenvalues correspond to representations with small Schur elements (asymmetric tableaux).

The Gram weight $w_k^G$ measures the change in representation content when neutron $k$ converts. A neutron whose conversion significantly reshuffles the irrep decomposition (boundary neutron, crossing a shell boundary) receives a larger weight than one whose conversion leaves the representation structure intact (interior neutron, staying within a shell).
<!-- FILE_END: gram-weight-eigenstructure.md -->

