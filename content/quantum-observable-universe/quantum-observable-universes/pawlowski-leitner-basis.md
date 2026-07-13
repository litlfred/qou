Let $V_{1/2} \cong \mathbb{C}^2$ be the fundamental representation of $G = \mathrm{SU}(2)$. For each simple object $V_j$ and tensor power $V_{1/2}^{\otimes n}$ with $n \geq 2j$, the intertwiner space $\mathrm{Hom}_{\mathrm{SU}(2)}\!\bigl(V_j, V_{1/2}^{\otimes n}\bigr)$ admits a canonical PawLei basis. This basis is indexed by standard Young tableaux of shape $\lambda \vdash n$ having at most two rows and satisfying $\lambda_1 - \lambda_2 = 2j$.

The construction relies on the PBW theorem over commutative rings: the unital Gröbner--Shirshov basis for $U(\mathfrak{su}(2))$ provides a monomial basis for the enveloping algebra. The intertwiner basis is then derived by contraction with the volume form.

```tex
\begin{equation}\label{eq:pawlei-basis-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathbf{1} \ar[r, "\epsilon^{\vee}"]
  & \Lambda^2 V_{1/2} \ar[r, hook]
  & V_{1/2}^{\otimes n} \ar[r, "\pi_j"]
  & V_j
\end{tikzcd}
\end{equation}
```

The volume form $\epsilon \colon \Lambda^2 V_{1/2} \to \mathbf{1}$ and its dual $\epsilon^{\vee}$ act as contraction operators. Each PawLei basis element is formed by applying a tableau-specified sequence of contractions to the highest-weight vector $e_+^{\otimes (j+m)} \otimes e_-^{\otimes (j-m)}$, followed by row symmetrization.

The dimension of the intertwiner space follows the hook-length formula:

$$
  \dim\mathrm{Hom}_{\mathrm{SU}(2)}\!\bigl(V_j, V_{1/2}^{\otimes n}\bigr)
  = 
  \frac{(2j+1) n!}{(\tfrac{n}{2}+j+1)!(\tfrac{n}{2}-j)!}
$$

for $n \equiv 2j ±od{2}$, and vanishes otherwise.
