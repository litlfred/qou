
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

The volume constraint requires a non-degenerate epimorphism
$\epsilon \colon \Lambda^2 V \to \mathbf{1}$, which forces
$\mathrm{rank}(V) = 2$: the epimorphism is non-degenerate only
when $\Lambda^2 V$ has rank $1$, and
$\mathrm{rank}(\Lambda^2 V) = \binom{r}{2}$ equals $1$ precisely
for $r = 2$ (see [Remark](#rem:fundamental-object-explication)). Thus
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
  \det(g_V) \;=\; 1,
\end{equation}
```

restricting the natural automorphisms from $\mathrm{GL}(2)$ to the
special subgroup $\mathrm{SL}(2)$.

The QOU non-degeneracy axiom ensures the Frobenius form
$\int_A \colon A \to \mathbf{1}$ is non-degenerate, inducing the
Frobenius self-duality $A \cong A^{\vee}$
([fibre adjoint involution](#prop:fiber-adjoint-involution)). Define a dagger on
morphisms by $f^{\dagger} = \int_A \circ \mu(S(f) \otimes -)$, where
$S$ is the antipode. Non-degeneracy of $\int_A$ and faithfulness
of $\tau$ imply $f^{\dagger} \circ f = 0 \Rightarrow f = 0$, so this
is a positive-definite dagger structure
([positive definite dagger](#prop:positive-definite-dagger)). Every tensor
automorphism $g \in G$ preserves the dagger (it commutes with $S$ and
$\int_A$), forcing $g_V^{-1} = g_V^{\dagger}$ and restricting $G$ to
the unitary subgroup $\mathrm{U}(2)$.

Combining both constraints:

$$
  G \;=\; \mathrm{SL}(2) \;\cap\; \mathrm{U}(2)
  \;=\; \mathrm{SU}(2).

$$

The volume constraint provides the special-linear condition
($\det = 1$), while the positive-definite dagger structure provides
the compactness (unitarity), locking the gauge group exclusively to
$\mathrm{SU}(2)$.
