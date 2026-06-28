Fix a quantum observable universe $(\mathbf{C}, \varTheta, G, \mathcal{S})$
with Markov trace
$\mathrm{tr}_M \colon \mathrm{End}_{\mathbf{C}}(A) \to \mathbf{1}_{\mathbf{C}}$
([adjoint trace](#rem\:adjoint-trace)).  Let $\mathcal{H}_q$ be the convolution
Hopf algebra of $\mathrm{End}_{\mathbf{C}}(A)$ under the
$q$-deformed convolution $\ast_q$.

**Categorical Laplace transform.**  The **categorical Laplace transform**
is the *:refterm[monoidal functor]{#monoidal-functor}*

$$
  \mathcal{L}\colon \bigl(\mathrm{End}_{\mathbf{C}}(A), \ast_q\bigr)
  \;\longrightarrow\;
  \bigl(\mathrm{End}_{\mathbf{C}}(A), \cdot\bigr)
$$

defined, for each spectral parameter $s \in \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, A)$,
by the Hopf pairing against the real exponential grouplike
$\exp_q(-s\cdot) \in G(\mathcal{H}_q)$:

$$
  \mathcal{L}[f](s)
  \;=\;
  \mathrm{tr}_M\bigl(\exp_q(-s\cdot)  \cdot  f\bigr)
  \;=\;
  \bigl\langle \exp_q(-s\cdot),  f\bigr\rangle_{\mathrm{tr}_M}.
$$

No integral sign appears: the pairing is the Frobenius pairing
supplied by the rigid monoidal structure
([fibre-functor rigidity](#rem\:fibre-functor-rigidity)).

**Defining property (monoidality).**  $\mathcal{L}$ intertwines
$q$-convolution with pointwise product,

$$
  \mathcal{L}[f \ast_q g]  =  \mathcal{L}[f] \cdot \mathcal{L}[g],
  \qquad
  \mathcal{L}[\mathbf{1}_{\ast_q}]  =  \mathbf{1}_{\cdot},
$$

and this property characterises $\mathcal{L}$ up to isomorphism — it
is the *mate* of the comultiplication $\Delta_q$ on $\mathcal{H}_q$.

```tex
\begin{equation}\label{eq:categorical-laplace-square}
\begin{tikzcd}[row sep=2.5em, column sep=4em]
  \mathcal{H}_q \otimes \mathcal{H}_q
    \ar[r, "\ast_q"]
    \ar[d, "\mathcal{L} \otimes \mathcal{L}"']
  & \mathcal{H}_q
    \ar[d, "\mathcal{L}"]
  \\
  \mathcal{H}_q \otimes \mathcal{H}_q
    \ar[r, "\cdot"']
  & \mathcal{H}_q
\end{tikzcd}
\end{equation}
```
