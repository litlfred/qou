Fix a quantum observable universe $(\mathbf{C}, \theta, G, \mathcal{S})$
with Markov trace
$\mathrm{tr}_M \colon \mathrm{End}_{\mathbf{C}}(A) \to \mathbf{1}_{\mathbf{C}}$
([adjoint trace](#rem:adjoint-trace)).  Let $H_q$ be the convolution
Hopf algebra of $\mathrm{End}_{\mathbf{C}}(A)$ under the
$q$-deformed convolution $\ast_q$.

**Categorical Laplace transform.**  The categorical Laplace transform
is the *monoidal functor*

$$
  \mathcal{L}\colon \bigl(\mathrm{End}_{\mathbf{C}}(A), \ast_q\bigr)
  \;\longrightarrow\;
  \bigl(\mathrm{End}_{\mathbf{C}}(A), \cdot\bigr)
$$

defined, for each spectral parameter $s \in \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, A)$,
by the Hopf pairing against the real exponential grouplike
$\exp_q(-s\cdot) \in G(H_q)$:

$$
  \mathcal{L}[f](s)
  \;=\;
  \mathrm{tr}_M\bigl(\exp_q(-s\cdot)  \cdot  f\bigr)
  \;=\;
  \bigl\langle \exp_q(-s\cdot),  f\bigr\rangle_{\mathrm{tr}_M}.
$$

No integral sign appears: the pairing is the Frobenius pairing
supplied by the rigid monoidal structure
([fibre-functor rigidity](#rem:fibre-functor-rigidity)).

**Defining property (monoidality).**  $\mathcal{L}$ intertwines
$q$-convolution with pointwise product,

$$
  \mathcal{L}[f \ast_q g]  =  \mathcal{L}[f] \cdot \mathcal{L}[g],
  \qquad
  \mathcal{L}[\mathbf{1}_{\ast_q}]  =  \mathbf{1}_{\cdot},
$$

and this property characterises $\mathcal{L}$ up to isomorphism — it
is the *mate* of the comultiplication $\Delta_q$ on $H_q$.

```tex
\begin{equation}\label{eq:categorical-laplace-square}
\begin{tikzcd}[row sep=2.5em, column sep=4em]
  H_q \otimes H_q
    \ar[r, "\ast_q"]
    \ar[d, "\mathcal{L} \otimes \mathcal{L}"']
  & H_q
    \ar[d, "\mathcal{L}"]
  \\
  H_q \otimes H_q
    \ar[r, "\cdot"']
  & H_q
\end{tikzcd}
\end{equation}
```

**Base-ring independence.**  Because $\exp_q(-s\cdot)$ is defined
abstractly as a grouplike of $H_q$ — not as a convergent series —
$\mathcal{L}$ makes sense over any base ring $R$ where $H_q$ has the
grouplike, i.e. anywhere $q \ne 1$ and $s$ is algebraic.  The familiar
integral

$$
  \mathcal{L}[f](s) \;=\; \int_0^\infty e^{-st} f(t)  dt
  \qquad (\mathbb{R}\text{-realisation})
$$

is recovered by evaluating the abstract pairing against the
archimedean realisation of the grouplike ($q \to 1$, $R = \mathbb{C}$,
Haar measure on $\mathbb{R}_{\ge 0}$).  Over $\mathbb{F}_p$ or
$\mathbb{Q}_p$ the integral is replaced by a sum over Frobenius
orbits, but $\mathcal{L}$ itself is unchanged.

**Role in the $q$-heat story.**  The $q$-heat equation
([$q$-heat equation](#def:q-heat-equation)) is turned by $\mathcal{L}$
into a *spectral* equation on the Hopf-algebraic side: differentiation
in $t$ becomes multiplication by $-s$, so $\partial_t u = \Delta_q u$
transforms to

$$
  -s  \mathcal{L}[u](s)
  \;=\;
  \widehat{\Delta_q}  \mathcal{L}[u](s),
$$

making $\mathcal{L}[u](s) = (\widehat{\Delta_q} + s)^{-1} u_0$ — the
*resolvent of the $q$-Laplacian*.  The heat kernel is the inverse
Laplace of the resolvent, and lives in the archimedean realisation.
