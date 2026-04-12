Let $(\mathbf{C}, \otimes, \mathbf{1})$ be an $R$-linear rigid monoidal
category, and let $V$ be a simple object that is
*symplectically self-dual*: there exists an isomorphism
$\phi \colon V \xrightarrow{ \sim } V^{\vee}$ satisfying
$\phi^{\vee} = -\phi$ (alternating). The alternating condition forces
$\mathrm{rank}(V) = 2$: the composite
$\mathrm{ev}_V \circ (\mathrm{id} \otimes \phi)$ factors through
$\Lambda^2 V$, and for the resulting morphism
$\epsilon \colon \Lambda^2 V \to \mathbf{1}$ to be a non-degenerate
epimorphism one needs $\mathrm{rank}(\Lambda^2 V) = 1$, i.e.,
$\mathrm{rank}(V) = 2$. The factorisation is (the
*volume form factorisation*):

```tex
\begin{equation}\label{eq:volume-form-factorisation}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  V \otimes V
    \ar[r, "\mathrm{id} \otimes \phi"]
    \ar[d, "\pi"', two heads]
  & V \otimes V^{\vee}
    \ar[d, "\mathrm{ev}_V"]
  \\
  \Lambda^2 V
    \ar[r, "\epsilon"', dashed]
  & \mathbf{1}
\end{tikzcd}
\end{equation}
```

and $\epsilon$ is non-degenerate; that is,
condition (iii) of
[quantum observable universe](#def:quantum-observable-universe) holds.

