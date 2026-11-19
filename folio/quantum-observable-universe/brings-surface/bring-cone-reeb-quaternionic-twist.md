*The affine cone $C(\mathcal{B})$ of
[the tetraplectic structure](#def:bring-cone-tetraplectic-structure) is a real
$4$-manifold, so the link of its singularity is $3$-dimensional. That link is
the unit tangent bundle $UT(\Sigma_4)$ with Seifert Euler number $-6$; it
carries the invariant contact structure whose Reeb flow is the geodesic flow,
and the triad of flows it supports closes into the* **split** *real form
$\mathfrak{sl}_2(\mathbb{R})$. The* **compact** *$\mathfrak{su}(2)$ triad
identified below is a statement about the quaternions $\mathbb{H} =
\mathbb{C}^2$ (the smooth local model of the cone, whose own link is the Hopf
fibration $S^3$ at Euler number $-1$) and is a local/frame statement, not a
structure on $UT(\Sigma_4)$.*

*Three independent facts fix this.* **(i)** *Bring's curve is canonically
embedded ($\mathcal{O}_{\mathcal{B}}(1) = K_{\mathcal{B}}$, $\deg K = 2g-2 = 6$
at $g = 4$), so the link is the unit circle bundle of
$\mathcal{O}(-1)|_{\mathcal{B}} = K^{-1} = T\mathcal{B}$, with Euler number
$-\deg K = 2 - 2g = \chi_{\mathrm{eu}}(\Sigma_4) = -6$ against $-1$ for
$\mathbb{H}$, a factor of $6$.* **(ii)** *A circle bundle over a genus-$4$
surface with non-zero Euler number has $\widetilde{\mathrm{SL}}_2$ geometry and
hence infinite $\pi_1$, whereas a $3$-Sasakian $3$-manifold is a spherical
space form $S^3/\Gamma$ with $\pi_1$ finite; a closed aspherical $3$-manifold
also admits no non-trivial $\mathrm{SU}(2)$-action, so three Reeb fields
closing into $\mathfrak{su}(2)$ cannot exist there.* **(iii)** *A
non-degenerate quaternionic-contact structure (a rank-$3$ contact object, three
forms $\alpha_a$ each with $\alpha_a \wedge (d\alpha_a)^n$ a volume form)
lives on a $(4n+3)$-manifold with $n \geq 1$, hence in dimension at least $7$.
The link has dimension $3$, so no non-degenerate quaternionic-contact structure
exists on it. (Dimension alone excludes nothing about $3$-Sasakian structures,
which allow $4n+3$ with $n = 0$: $S^3$ is $3$-Sasakian. It is (ii), not a
dimension count, that excludes that reading.)*

*The $\mathfrak{su}(2)$ does survive in this layer, as the structure group of
the quaternionic resolvent bundle rather than as a Reeb triad; see*
[the gauge reading](#rem:tetraplectic-su2-gauge-reading).

*Following Foth–Leitner \cite{fothleitner2003} for quaternionic flag manifolds,
model the triad on the quaternions by right-multiplication by the imaginary
units: $M_x(p) = p\,x$ for $x \in \{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$, or
in $2 \times 2$ block form*

$$
  M_x = \begin{pmatrix} x & 0 \\ 0 & x \end{pmatrix} .
$$

*Write $[M_x, M_y] := M_y \circ M_x - M_x \circ M_y$. Then*

$$
  [M_x, M_y] \;=\; 2\,M_{x \cdot y}
  \qquad (x \neq y),
$$

*that is, $[M_i, M_j] = 2M_k$, $[M_j, M_k] = 2M_i$, $[M_k, M_i] = 2M_j$, giving the
$\mathfrak{su}(2)$ commutation relations with structure constant $+2$.*

*Geometrically this is the* **quaternionic twist** *on the model*: *flowing
along $M_i$ preserves its own complex structure but rotates the two
complementary structures into one another, and the bracket above measures
exactly that torsion.*

*The same construction run on the split quaternions gives
$[M_i, M_j] = 2M_k$, $[M_j, M_k] = -2M_i$, $[M_k, M_i] = 2M_j$ (with one sign
flipped), which is the real form $UT(\Sigma_4)$ does carry, and the two
brackets are distinct.*
