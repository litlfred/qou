*The affine cone $C(\mathcal{B})$ of
[the tetraplectic structure](#def:bring-cone-tetraplectic-structure) is a real
$4$-manifold, so the link of its singularity is $3$-dimensional. Where the bulk
carries the invariant volume form, that link carries a* **3-Sasakian**
*(degenerate quaternionic-contact) structure: in place of a single Reeb vector
field there is an $\mathrm{SU}(2)$ triad of contact forms and dual Reeb fields.*

*Following Foth–Leitner \cite{fothleitner2003} for quaternionic flag manifolds,
model the triad on the quaternions by right-multiplication by the imaginary
units — $M_x(p) = p\,x$ for $x \in \{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$, or
in $2 \times 2$ block form*

```tex
M_x = \begin{pmatrix} x & 0 \\ 0 & x \end{pmatrix} .
```

*Write $[M_x, M_y] := M_y \circ M_x - M_x \circ M_y$. Then*

$$
  [M_x, M_y] \;=\; 2\,M_{x \cdot y}
  \qquad (x \neq y),
$$

*that is, $[M_i, M_j] = 2M_k$, $[M_j, M_k] = 2M_i$, $[M_k, M_i] = 2M_j$ — the
$\mathfrak{su}(2)$ commutation relations with structure constant $+2$.*

*Geometrically this is the* **quaternionic twist**: *flowing along $M_i$
preserves its own complex structure but rotates the two complementary
structures into one another, and the bracket above measures exactly that
torsion.*
