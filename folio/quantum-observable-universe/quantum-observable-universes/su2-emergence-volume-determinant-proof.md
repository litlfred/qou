**Proof.**
The gauge group $G$ is defined via Tannaka--Krein duality as
the group scheme of tensor-preserving natural automorphisms of the fibre
functor $\tau$. An element $g \in G$ assigns an invertible linear map
$g_X \colon \tau(X) \to \tau(X)$ to every object $X \in \mathbf{C}$.

Because $g$ is a natural transformation, it commutes with all morphisms
in $\mathbf{C}$, including the volume constraint
$\epsilon \colon \Lambda^2 V \to \mathbf{1}$
[volume constraint](#eq:categorical-volume-constraint). Applying $\tau$ yields the
commutative diagram of $R$-modules

```tex
\begin{equation}\label{eq:su2-emergence-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  \Lambda^2 \tau(V)
    \ar[r, "\Lambda^2 g_V"]
    \ar[d, "\tau(\epsilon)"']
  & \Lambda^2 \tau(V)
    \ar[d, "\tau(\epsilon)"]
  \\
  \tau(\mathbf{1})
    \ar[r, "g_{\mathbf{1}} = \mathrm{id}"']
  & \tau(\mathbf{1})
\end{tikzcd}
\end{equation}
```

The volume constraint requires $\epsilon \colon \Lambda^2 V \to \mathbf{1}$
to be an isomorphism $\Lambda^2 V \cong \mathbf{1}$, not only an
epimorphism (an epimorphism allows any rank $r \geq 2$; see the
[quantum observable universe](#def:quantum-observable-universe)). This
forces $\mathrm{rank}(V) = 2$: $\epsilon$ is an isomorphism only
when $\Lambda^2 V$ has rank $1$, and
$\mathrm{rank}(\Lambda^2 V) = \binom{r}{2}$ equals $1$ precisely
for $r = 2$ (see the [fundamental object](#def:fundamental-object)). Thus
$\tau(V)$ is a rank-$2$ free $R$-module and $\Lambda^2 \tau(V)$ has
rank $1$. The induced operator $\Lambda^2 g_V$ acts on this rank-$1$
module as scalar multiplication by $\det(g_V)$. Following
diagram [above](#eq:su2-emergence-diagram) from the top-left to the
bottom-right:

$$
  \tau(\epsilon) \circ \Lambda^2 g_V
  =
  g_{\mathbf{1}} \circ \tau(\epsilon)
  =
  \tau(\epsilon).
$$

Since $\tau(\epsilon)$ is non-degenerate (hence non-zero), this forces

```tex
\begin{equation}\label{eq:det-one}
  \det(g_V) =  1,
\end{equation}
```

restricting the natural automorphisms from $\mathrm{GL}(2)$ to the
special subgroup $\mathrm{SL}(2)$. $\square$
