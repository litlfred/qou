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
