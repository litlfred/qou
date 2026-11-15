---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE"
section_id: sec-009-31-symplectic-monodromy-associated-to-a-hessian
section_title: "Symplectic monodromy associated to a Hessian metric"
section_number: 3.1
pages: 20-22
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.966
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
[]{#sec:monodromy-hessian label="sec:monodromy-hessian"}

Let $B$ be a two-dimensional affine manifold with affine coordinates $(\eta,\xi)$ that embed $B$ as a subset of $\R^2$. In this subsection $B$ does not have any singularities. Suppose that $\eta: B \to \R$ is a submersion over some interval $I \subset \R$, and that the fibers of this map are connected intervals. For our purposes, we consider the case where $B$ is a quadrilateral, bounded on two opposite sides by line segments of constant $\eta$ (the *vertical* boundary $\partial^v B$), and on the other two sides by line segments that are transverse to the projection to $\eta$ (the *horizontal* boundary $\partial^h B$).

Associated to $B$ and $I$, we define complex manifolds $X(B)$ and $X(I)$. The space $X(B)$ is the subset of the complex torus $(\C^*)^2$ with coordinates $w$ and $z$ such that $(\eta,\xi) =
(\log|w|,\log|z|)$ lies in $B$, and $X(I)$ is the subset of $(\C^*)$ with coordinate $w$ such that $\eta = \log|w|$ lies in $I$. Thus $X(I)$ is an annulus, and we have a map $w : X(B) \to X(I)$, which is a non-singular fibration with fibers isomorphic to annuli. Philosophically speaking, the map $\eta: B \to I$ is a tropical model of the map $w: X(B)\to X(I)$.

In this situation, the most natural way to prescribe a Kähler structure on $X(B)$ is through a Hessian metric on the base $B$. This is a metric $g$ such that locally $g = \Hess K$ for some function $K:
B\to \R$, where the Hessian is computed with respect to an affine coordinate system. If $\pi: X(B) \to B$ denotes the projection, then $\phi = K\circ \pi$ is a Kähler potential on $X(B)$, and the positivity of $g = \Hess K$ corresponds to the positivity of the real closed $(1,1)$-form $\omega = -dd^c \phi$. Explicitly, if $y_1,\dots,
y_n$ are affine coordinates corresponding to complex coordinates $z_1,\dots,z_n$ on $(\C^*)^n$, then $$\label{eq:hessian-metric}
  g = \sum_{i,j=1}^n \frac{\partial^2 K}{\partial y_i\partial y_j}dy_idy_j$$ $$\label{eq:hessian-kahler-form}
  \omega = -dd^c \phi = \frac{\sqrt{-1}}{2}\sum_{i,j=1}^n  \frac{\partial^2 K}{\partial y_i\partial y_j}\frac{dz_i}{z_i} \wedge \frac{d\bar{z}_j}{\bar{z}_j}$$

Any such Kähler structure is invariant under the $S^1$--action $e^{i\theta}(z,w) = (e^{i\theta}z,w)$ that rotates the fibers of the map $w: X(B)\to X(I)$.

We now have a Kähler structure on $X(B)$ such that the fibration $w: X(B) \to X(I)$ has symplectic fibers. Thus there is a symplectic connection on this fibration whose horizontal subspaces are the symplectic orthogonal spaces to the fibers. This connection defines a notion of symplectic parallel transport along paths in the base $X(I)$, and symplectic monodromy around loops in the base. Since our fibers have boundary we must show that the symplectic parallel transport preserves the boundary. Given that, symplectic parallel transport defines symplectomorphisms between the fibers.

We now compute the symplectic connection. Let $X \in T_{(z,w)}X(B)$ denote a tangent vector. Let $Y \in \ker dw$ denote the general vertical vector. The relation defining the horizontal distribution is $\omega(X,Y) = 0$, or, $$\begin{split}
 0 &=  \left\{K_{\eta\eta}\frac{dw}{w} \wedge \frac{d\bar{w}}{\bar{w}} + K_{\eta\xi}\left(\frac{dw}{w}
 \wedge \frac{d\bar{z}}{\bar{z}} + \frac{dz}{z} \wedge \frac{d\bar{w}}{\bar{w}}\right) + K_{\xi\xi}
   \frac{dz}{z} \wedge \frac{d\bar{z}}{\bar{z}}\right\}(X,Y)\\
&= K_{\eta\xi}\left(\frac{dw(X)}{w}\frac{d\bar{z}(Y)}{\bar{z}} -
  \frac{d\bar{w}(X)}{\bar{w}}\frac{dz(Y)}{z}\right) +
K_{\xi\xi}\left(\frac{dz(X)}{z}\frac{d\bar{z}(Y)}{\bar{z}}-
  \frac{dz(Y)}{z}\frac{d\bar{z}(X)}{\bar{z}}\right)\\
&= \left(K_{\eta\xi}\frac{dw(X)}{w} + K_{\xi\xi}
  \frac{dz(X)}{z}\right)\frac{d\bar{z}(Y)}{\bar{z}} - \text{ complex conjugate}
\end{split}$$ Since $dz(Y)$ can have any phase, this shows that the quantity in parentheses on the last line must vanish: $$\label{eq:symplectic-connection}
  d\log z (X) = -\frac{K_{\eta\xi}}{K_{\xi\xi}}d\log w (X)$$ Tropically, this formula has the following interpretation: In the $(\eta,\xi)$ coordinates, the vertical tangent space is spanned by the vector $(0,1)$. The $g$-orthogonal to this space is spanned by the vector $(K_{\xi\xi}, -K_{\eta\xi})$, whose slope with respect to the affine coordinates is the factor $-K_{\eta\xi}/K_{\xi\xi}$ appearing in the formula for the connection.

::: lemma
[]{#lem:monodromy-hessian label="lem:monodromy-hessian"} Let $K$ be such that $\partial^h B$ is $g$-orthogonal to the fibers of the map $\eta: B\to I$, and assume that the slope $\sigma_F$ of each boundary face $F$ of $B$ is rational. Then

1.  parallel transport around the loop $\{|w|= R\}$ acts on the fiber over $w = R$ by rotating each circle of constant $|z|$ through a phase $2\pi (-K_{\eta\xi}/K_{\xi\xi})$, and

2.  for each boundary face $F$, we have $2\pi(-K_{\eta\xi}/K_{\xi\xi}) = 2\pi\sigma_F$, the part of $\partial^h X(B)$ lying over $F$ is foliated by multi-sections of the fibration that are horizontal with respect to the symplectic connection.
:::

::: proof
*Proof.* Consider the parallel transport of the connection around the loop $\{|w|
= R\}$, which is a generator of $\pi_1(X(I))$.

As $w$ traverses the path $R\exp(it)$, the initial condition $(z,w) = (r\exp(i\theta), R)$ generates the solution $(r\exp
(i \theta + (-K_{\eta\xi}/K_{\xi\xi})it), R\exp(it))$, where the expression $-K_{\eta\xi}/K_{\xi\xi}$ is constant along the solution curve. As a self-map of the fiber over $w = R$, this monodromy transformation maps circles of constant $|z|$ to themselves, but rotates each by the phase $2\pi (-K_{\eta\xi}/K_{\xi\xi})$.

We now consider the behavior of the symplectic connection near the horizontal boundary $\partial^h X(B)$. Let $F$ be a component of $\partial^h B$. Since $F$ is a straight line segment $g$-orthogonal to the fibers of $\eta$, the function $-K_{\eta\xi}/K_{\xi\xi}$ is constant on $F$ and equal to its slope, which we denote $\sigma = \sigma_F$. This slope is rational by assumption. The part of $X(B)$ lying over $F$ is defined by the condition $\log|z| = \sigma \log|w| + C$. Let $w = w_0\exp(\rho(t) + i
\phi(t))$ describe an arbitrary curve in the base annulus $X(I)$. If $(z_0,w_0)$ is an initial point that lies over $F$, then $$z = z_0\exp\left\{\sigma(\rho(t)+i\phi(t))\right\}, w = w_0\exp(\rho(t)+i\phi(t))$$ is a path in $X(B)$ that lies entirely over $F$, and which by virtue of this fact also solves the symplectic parallel transport equation. Thus the part of $\partial^h X(B)$ that lies over $F$ is foliated by horizontal sections of the fibration, namely $(w/w_0)^\sigma =
(z/z_0)$ where $\pi(z_0,w_0) \in F$. Take note that $\sigma$ is merely rational, so these horizontal sections may actually be multi-sections. ◻
:::

Examples of the Hessian metrics such that $\partial^hB$ is $g$-orthogonal to the fibers of $\eta$ may be constructed by starting with the function $$F(x,y) = x^2 + \frac{y^2}{x}$$ $$\Hess F = 
  \begin{pmatrix}
    2+ 2\frac{y^2}{x^3} & -2\frac{y}{x^2}\\
    -2 \frac{y}{x^2} & 2\frac{1}{x}
  \end{pmatrix}$$ $$\frac{-F_{xy}}{F_{yy}} = \frac{y}{x}$$ Thus the families of lines $x = c$ and $y = \sigma x$ form an orthogonal net for $\Hess F$. By taking $x$ and $y$ to be shifts of the affine coordinates $\eta$ and $\xi$ on $B$, we can obtain a Hessian metric on $B$ such that the vertical boundary consists of lines of the form $x = c$, while the horizontal boundary consists of lines of the form $y = \sigma x$.
