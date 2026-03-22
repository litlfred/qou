
The gauge group $G$ is defined via Tannaka--Krein duality as
the group scheme of tensor-preserving natural automorphisms of the fibre
functor $\omega$. An element $g \in G$ assigns an invertible linear map
$g_X \colon \omega(X) \to \omega(X)$ to every object $X \in \mathcal{C}$.

Because $g$ is a natural transformation, it commutes with all morphisms
in $\mathcal{C}$, including the volume constraint
$\epsilon \colon \Lambda^2 V \to \mathbf{1}$
\eqref{eq:categorical-volume-constraint}. Applying $\omega$ yields the
commutative diagram of $R$-modules

```tex
\begin{equation}\label{eq:su2-emergence-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  \Lambda^2 \omega(V)
    \ar[r, "\Lambda^2 g_V"]
    \ar[d, "\omega(\epsilon)"']
  & \Lambda^2 \omega(V)
    \ar[d, "\omega(\epsilon)"]
  \\
  \omega(\mathbf{1})
    \ar[r, "g_{\mathbf{1}} = \mathrm{id}"']
  & \omega(\mathbf{1})
\end{tikzcd}
\end{equation}
```

The fundamental object $V$ has categorical dimension $2$, so
$\omega(V)$ is a rank-$2$ free $R$-module and $\Lambda^2 \omega(V)$ has
rank $1$. The induced operator $\Lambda^2 g_V$ acts on this rank-$1$
module as scalar multiplication by $\det(g_V)$. Following
diagram \eqref{eq:su2-emergence-diagram} from the top-left to the
bottom-right:
$$
  \omega(\epsilon) \circ \Lambda^2 g_V
  =
  g_{\mathbf{1}} \circ \omega(\epsilon)
  =
  \omega(\epsilon).
$$
Since $\omega(\epsilon)$ is non-degenerate (hence non-zero), this forces

```tex
\begin{equation}\label{eq:det-one}
  \det(g_V) \;=\; 1,
\end{equation}
```

restricting the natural automorphisms from $\mathrm{GL}(2)$ to the
special subgroup $\mathrm{SL}(2)$.

The QOU non-degeneracy axiom ensures the Frobenius form
$\lambda \colon A \to \mathbf{1}$ is non-degenerate, inducing the
Frobenius self-duality $A \cong A^{\vee}$
([Proposition](#prop:fiber-adjoint-involution)). Define a dagger on
morphisms by $f^{\dagger} = \lambda \circ \mu(S(f) \otimes -)$, where
$S$ is the antipode. Non-degeneracy of $\lambda$ and faithfulness
of $\omega$ imply $f^{\dagger} \circ f = 0 \Rightarrow f = 0$, so this
is a positive-definite dagger structure
([Definition](#def:positive-definite-dagger)). Every tensor
automorphism $g \in G$ preserves the dagger (it commutes with $S$ and
$\lambda$), forcing $g_V^{-1} = g_V^{\dagger}$ and locking the group
into its unitary real form $\mathrm{SU}(2)$.
