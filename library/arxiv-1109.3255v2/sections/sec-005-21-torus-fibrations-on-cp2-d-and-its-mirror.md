---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE"
section_id: sec-005-21-torus-fibrations-on-cp2-d-and-its-mirror
section_title: "Torus fibrations on CP2 D and its mirror"
section_number: 2.1
pages: 11-16
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.989
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
[]{#sec:torus-fibrations label="sec:torus-fibrations"}

Let $$D = \{xyz-y^3 = 0\} \subset \CP^2$$ be a binodal cubic curve. We equip $\CP^2$ and $\CP^2 \setminus D$ with standard Fubini-Study symplectic forms. Both $\CP^2 \setminus D$ and its mirror $X^\vee = \{(u,v)\in
\C^2\mid uv \neq 1\}$ admit special Lagrangian torus fibrations. In fact, these spaces are diffeomorphic, each being $\C^2$ minus a conic. The torus fibrations are essentially the same on both sides, but we are interested in the *symplectic* affine structure associated to the fibration on $\CP^2 \setminus D$ and the *complex* affine structure associated to $X^\vee$.

The construction is of the torus fibrations is taken from [@auroux07 § 5]. We have that $\CP^2\setminus D$ is an affine algebraic variety with coordinates $x$ and $z$, where $xz\neq 1$. Hence we can define a map $$f: \CP^2\setminus D \to \C^* \quad f(x,z) = xz-1$$ This map is a Lefschetz fibration with critical point $(0,0)$ and critical value $-1$. The fibers are affine conics, and the map is invariant under the $S^1$ action $e^{i\theta}(x,z) = (e^{i\theta}x,e^{-i\theta}z)$ that rotates the fibers. Each fiber contains a distinguished $S^1$--orbit, namely the vanishing cycle $\{|x| = |z|\}$. We can parametrize the other $S^1$--orbits by the function $\delta(x,z)$ which denotes the signed symplectic area between the vanishing cycle and the orbit through $(x,z)$. The function $\delta$ is a moment map for the $S^1$-action. Symplectic parallel transport in every direction preserves the circle at level $\delta = \lambda$, and so by choosing any loop $\gamma \subset \C^*$, and $\lambda \in (-\Lambda,\Lambda)$ (where $\Lambda = \int_{\CP^1} \omega$ is the area of a line), we obtain a Lagrangian torus $T_{\gamma,\lambda} \subset \CP^2 \setminus
D$. If we let $T_{R,\lambda}$ denote the torus at level $\lambda$ over the circle of radius $R$ centered at the origin in $\C^*$, we find that $T_{R,\lambda}$ is special Lagrangian with respect to the form $$\Omega = dx\wedge dz/(xz-1).$$

The torus fibration on $X^\vee$ is essentially the same, except that the coordinates $(x,z)$ are changed to $(u,v)$. For the rest of the paper, we denote by $$w = uv-1$$ the quantity to which we project in order to obtain the Lagrangian tori $T_{R,\lambda}$ (and later the Lagrangian sections $L(d)$) as fibering over paths. For the time being, and in order to enable the explicit computations in section [\[sec:tropicalization\]](#sec:tropicalization){reference-type="ref" reference="sec:tropicalization"}, we will equip $X^\vee$ with the standard symplectic form in the $(u,v)$--coordinates, so the quantity $$\delta(u,v) =|u|^2-|v|^2$$ is the standard moment map. In summary, for $X^\vee$, we have $$T_{R,\lambda} = \{(u,v) \mid |w| = |uv-1| = R,
|u|^2-|v|^2 = \lambda\}.$$

Each torus fibration has a unique singular fiber $T_{1,0}$, which is a pinched torus.

Figure [1](#fig:torus-fibration){reference-type="ref" reference="fig:torus-fibration"} shows several fibers of the Lefschetz fibration, with a Lagrangian torus that maps to a circle in the base. The two marked points in the base represent a Lefschetz critical value (filled-in circle), and a puncture (open circle).

![The Lefschetz fibration with a torus that maps to a circle.](torus-fibration){#fig:torus-fibration width="2.5in"}

For the symplectic affine structure, the affine coordinates are obtained by integrating the symplectic two-form $\omega$ over one-cycles in the torus fibers to obtain one-forms on the base, which may be integrated to functions. For the complex affine structure, we instead integrate the imaginary part of the holomorphic volume form $\im \Omega$ over $(n-1)$ cycles in the fiber to obtain one-forms on the base, where in our case $n = 2$. See [@gross-syz-survey §2] for an explanation of this construction.

We begin by describing the symplectic affine structure on the base $B$ of the torus fibration on $\CP^2 \setminus D$. Recall that an integral affine structure has a canonically defined local system of integral tangent vectors. In the case when the affine manifold has singularities, this local system may have monodromy around the singular locus. The following result can be extracted from the analysis of [@auroux07 §5.2].

::: proposition
The integral affine manifold $B$ is topologically a disk. It has one singular point, with monodromy conjugate to $\begin{pmatrix}1&0\\1&1\end{pmatrix}$. In affine coordinates, the boundary of $B$ consists of two line segments that are straight with respect to the affine structure. The corners are locally equivalent, by an affine linear transformation, to the standard quadrant $\R_{\geq 0}^2 \subset \R^2$.
:::

::: proof
*Proof.* The symplectic affine coordinates are the symplectic areas of disks in $\CP^2$ with boundary on $T_{R,\lambda}$. Let $H$ denote the class of a line. We consider the cases $R > 1$ and $R < 1$.

On the $R > 1$ side, we take $\beta_1,\beta_2 \in
  H_2(\CP^2,T_{R,\lambda})$ to be the classes of two sections over the disk bounded by the circle of radius $R$ in the base, where $\beta_1$ intersects the $z$-axis and $\beta_2$ the $x$-axis. Then the torus fiber collapses onto line $\{y=0\}$ when $$\langle [\omega], H-\beta_1-\beta_2 \rangle = 0.$$

On the $R < 1$ side, we take $\alpha, \beta \in
  H_2(\CP^2,T_{R,\lambda})$, where $\beta$ is now the unique class of sections over the disk bounded by the circle of radius $R$, and $\alpha$ is the class of a disk connecting an $S^1$-orbit to the vanishing cycle within the conic fiber and capping off with the thimble. The torus fiber collapses onto the conic $\{xz-y^2 = 0\}$ when $$\langle [\omega], \beta \rangle = 0.$$

The two sides $R > 1$ and $R < 1$ are glued together along the wall at $R = 1$, but the gluing is different for $\lambda > 0$ than for $\lambda < 0$, leading to the monodromy. Let us take $\eta = \langle
  [\omega],\alpha\rangle$ and $\xi = \langle [\omega],\beta\rangle$ as affine coordinates in the $R < 1$ region. We continue these across the $\lambda > 0$ part of the wall using correspondence between homology classes: $$\begin{split}
      \alpha &\leftrightarrow \beta_1-\beta_2\\
      \beta &\leftrightarrow \beta_2\\
      H-2\beta-\alpha &\leftrightarrow H-\beta_1-\beta_2
      \end{split}$$ Thus, in the $\lambda > 0$ part of the base, the conic appears as $\xi = 0$, while the line appears as $$0 = \langle [\omega],H - 2\beta - \alpha\rangle = \Lambda - 2\xi - \eta$$ which is a line of slope of $-1/2$ with respect to the coordinates $(\eta,\xi)$. The pair of functions $\xi$ and $\Lambda -2\xi -\eta$ also form an affine coordinate system, and in this system the corner appears as a standard quadrant.

In the $\lambda < 0$ part of the base, we instead use $$\begin{split}
      \alpha &\leftrightarrow \beta_1-\beta_2\\
      \beta &\leftrightarrow \beta_1\\
      H-2\beta+\alpha &\leftrightarrow H-\beta_1-\beta_2
      \end{split}$$ Hence in this region the conic appears as $\xi = 0$ again, while the line appears as $$0 = \langle [\omega],H - 2\beta + \alpha\rangle = \Lambda - 2\xi + \eta$$ which is a line of slope $1/2$ with respect to the coordinates $(\eta,\xi)$. The pair of functions $\xi$ and $\Lambda -2\xi +\eta$ also form an affine coordinate system, and in this system the corner appears as a standard quadrant.

The discrepancy between the two gluings represents the monodromy. As we pass from $\{R > 1, \lambda > 0\} \to \{R< 1, \lambda > 0\} \to
  \{R < 1,\lambda < 0\} \to \{R > 1, \lambda < 0\} \to \{R > 1,\lambda
  > 0\}$, the coordinates $(\eta,\xi)$ under go the transformation $(\eta,\xi) \to (\eta, \xi-\eta)$, which is indeed a simple shear. ◻
:::

Figure [2](#fig:the-bigon){reference-type="ref" reference="fig:the-bigon"} shows the affine manifold $B$. The marked point is a singularity of the affine structure, and the dotted line is a cut in the affine coordinates. The affine coordinates $\eta,\xi,\psi$ are indicated. The function $\xi$ is undefined on the cut below the singularity, while $\psi$ is undefined at points directly above the singularity. Going around the singularity counterclockwise, the monodromy of the local system of integral tangent vectors $\begin{pmatrix}1&0\\1&1\end{pmatrix}$, which also serves as the gluing map along the cut. The edges of the picture are boundaries. The upper edge corresponds to points where the torus collapses onto the line $\{y=0\}$. It has slope zero in this picture. The lower edge corresponds to points where the torus collapses onto the conic $\{xz-y^2 = 0\}$. On the left portion the lower edge has slope $-1/2$, while on the right portion it has slope $1/2$. The lower edge is actually straight with respect to the affine structure, and the nontrivial gluing is what compensates for the apparent bend.

![The affine manifold $B$.](the-bigon){#fig:the-bigon width="3in"}

On the mirror side, we compute the complex affine structure (determined by the holomorphic volume form) on the base of the torus fibration on $X^\vee$. The holomorphic volume form is $$\label{eq:vol-form-uv}
  \Omega = \frac{du\wedge dv}{uv-1} = \frac{du\wedge dv}{w}.$$ Differentiating the defining equation $uv = 1 + w$ and substituting gives the other formulas $$\label{eq:vol-form-uw}
 \Omega = \frac{du}{u}\wedge \frac{dw}{w}, \quad \text{when}\ u \neq 0,$$ $$\label{eq:vol-form-vw}
  \Omega = -\frac{dv}{v}\wedge \frac{dw}{w}, \quad \text{when}\ v \neq 0.$$ The special Lagrangian fibration on $X^\vee$ to consider is constructed in [@auroux07]. The fibers are the tori $$\label{eq:slags}
  T_{R,\lambda} = \{(u,v)\in X^\vee \mid |uv-1| = R, |u|^2-|v|^2 =
  \lambda\}, \quad (R,\lambda) \in (0,\infty)\times (-\infty,\infty),$$ and the fiber $T_{1,0}$ is a pinched torus. Thus $(R,\lambda)$ are coordinates on the base of this fibration. They are not affine coordinates, which must be computed using $\im \Omega$. Due to the simple algebraic form of this fibration, it is possible to find an integral representation of the complex affine coordinates explicitly.

::: proposition
[]{#prop:affine-coords label="prop:affine-coords"} The following functions are affine linear with respect to affine structure induced by $\im \Omega$. $$\label{eq:affine-coords-uw}
    \begin{split}
      \eta &= \log|w| = \log R\\
      \xi &= \frac{1}{2\pi}\int_{T_{R,\lambda}\cap \{u \in \R_+\}}
      \log|u|\,
      d\arg(w)\\
      &= \frac{1}{2\pi}\int_0^{2\pi}
      \frac{1}{2}\log\left(\frac{\lambda +\sqrt{\lambda^2 + 4\cdot
            |1+Re^{i\theta}|^2}}{2}\right)\,d\theta\\
\psi&= \frac{1}{2\pi}\int_{T_{R,\lambda}\cap \{v\in \R_+\}} \log|v|\, d\arg(w)\\
      &= \frac{1}{2\pi}\int_0^{2\pi}
      \frac{1}{2}\log\left(\frac{-\lambda +\sqrt{\lambda^2 +
            4\cdot |1+Re^{i\theta}|^2}}{2}\right)\, d\theta
    \end{split}$$ ($\eta$ is defined everywhere, $\xi$ is defined where $u \neq 0$, and $\psi$ is defined where $v \neq 0$). They satisfy the following relations on their common domain of definition.

1.  At every point, $\eta$ is independent from $\xi$ and from $\psi$.

2.  In the subset where $R < 1$, the relation $\xi + \psi = 0$ holds.

3.  In the subset where $R > 1$, the relation $\xi + \psi = \eta$ holds.
:::

::: proof
*Proof.* This is essentially straightforward so we only give an example of the computation.

The general procedure for computing affine coordinates from the flux of the holomorphic volume form is as follows: we choose, over a local chart on the base, a collection of $(2n-1)$--manifolds $\{\Gamma_i\}_{i=1}^n$ in the total space $X$ such that the torus fibers $T_b$ intersect each $\Gamma_i$ in an $(n-1)$--cycle, and such that these $(n-1)$--cycles $T_b \cap \Gamma_i$ form a basis of $H_{n-1}(T_b;\Z)$. The affine coordinates $(y_i)_{i=1}^n$ are defined up to constant shift by the property that $$y_i(b')-y_i(b) = \frac{1}{2\pi}\int_{\Gamma_i \cap \pi^{-1}(\gamma)} \im \Omega$$ where $\gamma$ is any path in the local chart on the base connecting $b$ to $b'$. Because $\Omega$ is closed, this integral does not depend on the choice of $\gamma$.

To get the coordinate $\eta$, start with the submanifold $$\Gamma_1= \{w \in \R_+\}$$

The intersection $\Gamma_1 \cap T_{R,\lambda}$ is a loop on $T_{R,\lambda}$. The function $\arg(u)$ gives a coordinate on this loop (briefly, $w\in \R_+$ and $|w| = R$ determine $uv$, along with $|u|^2 - |v|^2 = \lambda$ this determines the $|u|$ and $|v|$; the only parameter left is $\arg(u)$ since $\arg(v) = - \arg(u)$), and we declare the loop to be oriented so that $-d\arg(u)$ restricts to a positive volume form on it. Using [\[eq:vol-form-uw\]](#eq:vol-form-uw){reference-type="eqref" reference="eq:vol-form-uw"} we see $$\label{eq:im-vol-form-uw}
    \im \Omega = d\arg(u) \wedge d\log|w| + d\log|u| \wedge d\arg(w)$$ Using the fact that $\arg(w)$ is constant on $\Gamma_1$, we see that for any path $\gamma$ in the subset of the base where $R < 1$ connecting $b = (R,\lambda)$ to $b'=(R',\lambda')$, we have $$\int_{\Gamma_1\cap \pi^{-1}(\gamma)} \im \Omega =
    \int_{\Gamma_1\cap \pi^{-1}(\gamma)} d\arg(u) \wedge d\log|w|.$$ But $d\arg(u) \wedge d\log|w| = d(-\log|w|\,d\arg(u)))$, so the integral above equals $$\int_{\Gamma_1 \cap T_{b'}} -\log|w|\,d\arg(u) -
    \int_{\Gamma_1\cap T_b} -\log|w|\,d\arg(u) = 2\pi(\log R' - \log R)$$ (the minus signs within the integrals are absorbed by the orientation convention for $\Gamma_1 \cap T_b$). Thus $\eta = \log
  R$ is the affine coordinate corresponding to $\Gamma_1$.

The same idea applied to $\Gamma_2 = \{u \in \R_+\}$ yields the affine coordinate $$\xi = \frac{1}{2\pi} \int_{\Gamma_2 \cap T_b} \log|u|\,d\arg(w)$$ To arrive at the second formula for $\xi$, we must solve for $|u|$ in terms of $R,\lambda$, and $\theta = \arg(w)$. The equations $uv =
  1 + Re^{i\theta}$ and $|u|^2 - |v|^2 = \lambda$ imply $|u|^4 -
  \lambda|u|^2 = |1+Re^{i\theta}|^2$. Solving for $|u|^2$ by the quadratic formula and taking logarithms gives the result.

The formulas for $\psi$ are obtained by applying the same method to $\Gamma'_2 = \{v \in \R_+\}$.

To prove the linear relations, we find that $\xi + \psi$ reduces by the law of logarithms and the Cauchy integral formula to $$\frac{1}{2\pi}\int_0^{2\pi} \log|1+Re^{i\theta}|\,d\theta = \begin{cases}0, & R<1\\ \log R, &R > 1\end{cases}$$ ◻
:::

Proposition [\[prop:affine-coords\]](#prop:affine-coords){reference-type="ref" reference="prop:affine-coords"} determines the monodromy around the singular point (at $\eta = \xi = \psi = 0$) of the base, and show that the affine structure is in fact integral. Once again, the monodromy is a shear.
