Let $(\mathcal{C}, \otimes, \mathbf{1})$ be an $R$-linear rigid monoidal
category, and let $V$ be an object of categorical dimension $2$ that is
*symplectically self-dual*: there exists an isomorphism
$\phi \colon V \xrightarrow{\;\sim\;} V^{\vee}$ satisfying
$\phi^{\vee} = -\phi$ (alternating). Then the composite
$\mathrm{ev}_V \circ (\mathrm{id} \otimes \phi)$ factors through
$\Lambda^2 V$ (the *volume form factorisation*):

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
[Definition](#def:quantum-observable-universe) holds.

---

Because $\phi$ is alternating, the pairing
$B = \mathrm{ev}_V \circ (\mathrm{id} \otimes \phi)$ satisfies
$B \circ \tau_{V,V} = -B$, where $\tau_{V,V}$ is the symmetry (or
braiding) isomorphism. Hence $B$ vanishes on symmetric tensors and
factors as $B = \epsilon \circ \pi$, where
$\pi \colon V \otimes V \twoheadrightarrow \Lambda^2 V$ is the
canonical projection. Non-degeneracy of $\epsilon$ follows from
non-degeneracy of $\mathrm{ev}_V$ (guaranteed by rigidity) and the
isomorphism $\phi$. The duality axioms
$(\mathrm{ev}_V \otimes \mathrm{id}) \circ
(\mathrm{id} \otimes \mathrm{coev}_V) = \mathrm{id}_V$ ensure that
$\epsilon$ is preserved by the rigid dualities of $\mathcal{C}$.
