*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

Let $G = \mathrm{SU}(2)$ be the emergent gauge group
([$\mathrm{SU}(2)$ emergence](#thm:su2-emergence)) and let
$V_{1/2} \cong \mathbb{C}^2$ be the
[spin-$\tfrac{1}{2}$ representation](#rem:spin-half-representation).
For each simple object $V_j$ and tensor power
$V_{1/2}^{\otimes n}$ with $n \geq 2j$, the intertwiner space

$$
  \mathrm{Hom}_{\mathrm{SU}(2)}\!\bigl(V_j,
    V_{1/2}^{\otimes n}\bigr)
$$

admits a *canonical* basis — the **PawLei basis** — indexed by
standard Young tableaux of shape $\lambda \vdash n$ with at most
$2$ rows and with $\lambda_1 - \lambda_2 = 2j$.

The construction rests on the
[PBW theorem over commutative rings](unital-groebner-bases:cor:pbw): the unital Gröbner--Shirshov
basis for $U(\mathfrak{su}(2))$ provides a monomial basis for the
enveloping algebra, from which the intertwiner basis is derived by
contraction with the volume form.

```tex
\begin{equation}\label{eq:pawlei-basis-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathbf{1} \ar[r, "\epsilon^{\vee}"]
  & \Lambda^2 V_{1/2} \ar[r, hook]
  & V_{1/2}^{\otimes n} \ar[r, "\pi_j"]
  & V_j
\end{tikzcd}
\qquad\text{(PawLei contraction)}
\end{equation}
```

Concretely, the volume form
$\epsilon \colon \Lambda^2 V_{1/2} \to \mathbf{1}$ and its dual
$\epsilon^{\vee} \colon \mathbf{1} \to \Lambda^2 V_{1/2}$ generate
*contraction operators* on tensor powers. The PawLei basis elements
are obtained by applying a specific sequence of pairwise contractions
(determined by the tableau) to the highest-weight vector
$e_+^{\otimes (j+m)} \otimes e_-^{\otimes (j-m)}$, then
symmetrising according to the row structure of the tableau.

The dimension of the intertwiner space is given by the hook-length
formula:

$$
  \dim\mathrm{Hom}_{\mathrm{SU}(2)}\!\bigl(V_j,
    V_{1/2}^{\otimes n}\bigr)
  = 
  \frac{(2j+1) n!}{(\tfrac{n}{2}+j+1)!(\tfrac{n}{2}-j)!}
$$

when $n \equiv 2j \pmod{2}$, and zero otherwise.

The PBW basis underlying this construction is established via unital
Gröbner--Shirshov bases in \cite{leitnerpawloski2004}.
