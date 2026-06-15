Let $\mathfrak{S}_q$ be the
([categorical action](#def\:categorical-action)).  The three variational
equations are:

1. *Gravity (vary $\int_A$)*:
   $\delta\mathfrak{S}_q / \delta\!\int_A = 0$ yields the
   *categorical Einstein equation*:

   $$
     R_{\int} - \tfrac{1}{2}\mathrm{tr}(R_{\int})\mathrm{id}_A
     =  T_q[\nabla, \psi],
   $$

   where $T_q$ is the stress-energy endomorphism constructed from the
   gauge and matter terms.

2. *Gauge (vary $\nabla$)*:
   $\delta\mathfrak{S}_q / \delta\nabla = 0$ yields the
   *categorical Yang--Mills equation*:

   $$
     \nabla \star_q F_\nabla + q \cdot [F_\nabla, \star_q F_\nabla]
     =  J_\psi,
   $$

   where $J_\psi = \psi^* \otimes D_\nabla\psi - D_\nabla\psi^* \otimes \psi$
   is the matter current.

3. *Matter (vary $\psi$)*:
   $\delta\mathfrak{S}_q / \delta\psi = 0$ yields the
   *:refterm[categorical transport]{#categorical-transport} equation*:

   $$
     D_\nabla\psi =  0.
   $$

```tex
\begin{equation}\label{eq:variational-equations-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathfrak{S}_q \ar[r, "\delta/\delta\!\int_A"]
    \ar[d, "\delta/\delta\nabla"']
    \ar[dr, "\delta/\delta\psi"]
  & R_{\int} - \tfrac{1}{2}\mathrm{tr}(R_{\int})\mathrm{id} = T_q \\
  \nabla \star_q F + q[F, \star_q F] = J_\psi
  & D_\nabla \psi = 0 \ar[from=ul, crossing over]
\end{tikzcd}
\qquad\text{(variational equations)}
\end{equation}
```
