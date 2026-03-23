A **monoidal category** $(\mathcal{C}, \otimes, \mathbf{1})$ is a
category equipped with a bifunctor
$\otimes \colon \mathcal{C} \times \mathcal{C} \to \mathcal{C}$ (the
*tensor product*), a unit object $\mathbf{1}$, and natural
isomorphisms expressing associativity and unitality:

```tex
\[
\begin{gathered}
\begin{tikzcd}[column sep=3em]
  (X \otimes Y) \otimes Z
    \ar[r, "\alpha_{X,Y,Z}", "\sim"']
  & X \otimes (Y \otimes Z)
\end{tikzcd}
\\[-0.5em]
\text{\small associativity}
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
\text{\small unitality}
\end{gathered}
\]
```

The category is *rigid* if every object $V$ has a *dual*
$V^{\vee}$ together with morphisms
$\mathrm{ev}_V \colon V \otimes V^{\vee} \to \mathbf{1}$
and
$\mathrm{coev}_V \colon \mathbf{1} \to V^{\vee} \otimes V$
such that the following *snake identity* diagrams commute:

```tex
\begin{equation}\label{eq:snake-identities}
\begin{gathered}
\begin{tikzcd}[row sep=2em, column sep=2.5em]
  V
    \ar[r, "\mathrm{id} \otimes \mathrm{coev}"]
    \ar[dr, "\mathrm{id}_V"']
  & V \otimes V^{\vee} \otimes V
    \ar[d, "\mathrm{ev} \otimes \mathrm{id}"]
  \\
  & V
\end{tikzcd}
\\[-0.5em]
\text{\small left snake identity}
\end{gathered}
\qquad\qquad
\begin{gathered}
\begin{tikzcd}[row sep=2em, column sep=2.5em]
  V^{\vee}
    \ar[r, "\mathrm{coev} \otimes \mathrm{id}"]
    \ar[dr, "\mathrm{id}_{V^{\vee}}"']
  & V^{\vee} \otimes V \otimes V^{\vee}
    \ar[d, "\mathrm{id} \otimes \mathrm{ev}"]
  \\
  & V^{\vee}
\end{tikzcd}
\\[-0.5em]
\text{\small right snake identity}
\end{gathered}
\end{equation}
```

We say $\mathcal{C}$ is *$R$-linear* (for a commutative ring $R$)
if every hom-set is an $R$-module and composition is $R$-bilinear.
