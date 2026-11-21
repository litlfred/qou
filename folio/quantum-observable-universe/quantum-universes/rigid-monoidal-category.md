A **:refterm[monoidal category]{#monoidal-category}** $(\mathbf{C}, \otimes, \mathbf{1})$ is a category equipped with a bifunctor $\otimes \colon \mathbf{C} \times \mathbf{C} \to \mathbf{C}$, a unit object $\mathbf{1}$, and natural isomorphisms expressing associativity and unitality:

```tex
\begin{equation}\label{eq:monoidal-axioms}
\begin{gathered}
\begin{tikzcd}[column sep=3em]
  (X \otimes Y) \otimes Z
    \ar[r, "\alpha_{X,Y,Z}", "\sim"']
  & X \otimes (Y \otimes Z)
\end{tikzcd}
\\[-0.5em]
\text{\small (associativity)}
\end{gathered}
\qquad
\begin{gathered}
\begin{tikzcd}[column sep=2.5em]
  \mathbf{1} \otimes X
    \ar[r, "\ell_X", "\sim"']
  & X
  & X \otimes \mathbf{1}
    \ar[l, "\rho_X"', "\sim"]
\end{tikzcd}
\\[-0.5em]
\text{\small (unitality)}
\end{gathered}
\end{equation}
```

The category is *rigid* if every object $V$ has a dual $V^{\vee}$ together with morphisms $\mathrm{ev}_V \colon V \otimes V^{\vee} \to \mathbf{1}$ and $\mathrm{coev}_V \colon \mathbf{1} \to V^{\vee} \otimes V$ satisfying the [snake identities](#def:snake-identity).

The category $\mathbf{C}$ is *$R$-linear* for a commutative ring $R$ [without quasi-zeros](#rem:glossary-no-quasi-zeros) if every hom-set is an $R$-module and composition is $R$-bilinear.

The category is *braided monoidal* if it has a natural isomorphism $c_{X,Y} \colon X \otimes Y \xrightarrow{\sim} Y \otimes X$ compatible with the associator and satisfying the hexagon axioms. The braiding is *symmetric* when $c_{Y,X} \circ c_{X,Y} = \mathrm{id}$. Given a braiding, the *exterior power* $\Lambda^k V$ is the image of the antisymmetriser $\mathrm{Alt}_k = \sum_{\pi \in S_k} \mathrm{sgn}(\pi)\pi$ acting on $V^{\otimes k}$, where permutations act via $c$.
