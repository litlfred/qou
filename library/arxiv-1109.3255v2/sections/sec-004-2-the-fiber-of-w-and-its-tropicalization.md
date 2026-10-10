---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE"
section_id: sec-004-2-the-fiber-of-w-and-its-tropicalization
section_title: "The fiber of W and its tropicalization"
section_number: 2
pages: 11-16
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
text_source: latex
latex_prose_ratio: 0.673
latex_coverage_ratio: 0.989
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped with a binodal cubic curve as"
---
[]{#sec:fiber-superpotential label="sec:fiber-superpotential"}

## Torus fibrations on $\CP^2 \setminus D$ and its mirror {#sec:torus-fibrations}

Let $$\begin{equation}
D = \{xyz-y^3 = 0\} \subset \CP^2
\end{equation}$$ be a binodal cubic curve. We equip $\CP^2$ and $\CP^2 \setminus D$ with standard Fubini-Study symplectic forms. Both $\CP^2 \setminus D$ and its mirror $X^\vee = \{(u,v)\in
\C^2\mid uv \neq 1\}$ admit special Lagrangian torus fibrations. In fact, these spaces are diffeomorphic, each being $\C^2$ minus a conic. The torus fibrations are essentially the same on both sides, but we are interested in the *symplectic* affine structure associated to the fibration on $\CP^2 \setminus D$ and the *complex* affine structure associated to $X^\vee$.

The construction is of the torus fibrations is taken from [@auroux07 § 5]. We have that $\CP^2\setminus D$ is an affine algebraic variety with coordinates $x$ and $z$, where $xz\neq 1$. Hence we can define a map $$\begin{equation}
f: \CP^2\setminus D \to \C^* \quad f(x,z) = xz-1
\end{equation}$$ This map is a Lefschetz fibration with critical point $(0,0)$ and critical value $-1$. The fibers are affine conics, and the map is invariant under the $S^1$ action $e^{i\theta}(x,z) = (e^{i\theta}x,e^{-i\theta}z)$ that rotates the fibers. Each fiber contains a distinguished $S^1$--orbit, namely the vanishing cycle $\{|x| = |z|\}$. We can parametrize the other $S^1$--orbits by the function $\delta(x,z)$ which denotes the signed symplectic area between the vanishing cycle and the orbit through $(x,z)$. The function $\delta$ is a moment map for the $S^1$-action. Symplectic parallel transport in every direction preserves the circle at level $\delta = \lambda$, and so by choosing any loop $\gamma \subset \C^*$, and $\lambda \in (-\Lambda,\Lambda)$ (where $\Lambda = \int_{\CP^1} \omega$ is the area of a line), we obtain a Lagrangian torus $T_{\gamma,\lambda} \subset \CP^2 \setminus
D$. If we let $T_{R,\lambda}$ denote the torus at level $\lambda$ over the circle of radius $R$ centered at the origin in $\C^*$, we find that $T_{R,\lambda}$ is special Lagrangian with respect to the form $$\begin{equation}
\Omega = dx\wedge dz/(xz-1).
\end{equation}$$

The torus fibration on $X^\vee$ is essentially the same, except that the coordinates $(x,z)$ are changed to $(u,v)$. For the rest of the paper, we denote by $$\begin{equation}
w = uv-1
\end{equation}$$ the quantity to which we project in order to obtain the Lagrangian tori $T_{R,\lambda}$ (and later the Lagrangian sections $L(d)$) as fibering over paths. For the time being, and in order to enable the explicit computations in section [0.3](#sec:tropicalization){reference-type="ref" reference="sec:tropicalization"}, we will equip $X^\vee$ with the standard symplectic form in the $(u,v)$--coordinates, so the quantity $$\begin{equation}
\delta(u,v) =|u|^2-|v|^2
\end{equation}$$ is the standard moment map. In summary, for $X^\vee$, we have $$\begin{equation}
T_{R,\lambda} = \{(u,v) \mid |w| = |uv-1| = R,
|u|^2-|v|^2 = \lambda\}.
\end{equation}$$

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
  H_2(\CP^2,T_{R,\lambda})$ to be the classes of two sections over the disk bounded by the circle of radius $R$ in the base, where $\beta_1$ intersects the $z$-axis and $\beta_2$ the $x$-axis. Then the torus fiber collapses onto line $\{y=0\}$ when $$\begin{equation}
    \langle [\omega], H-\beta_1-\beta_2 \rangle = 0.
\end{equation}$$

On the $R < 1$ side, we take $\alpha, \beta \in
  H_2(\CP^2,T_{R,\lambda})$, where $\beta$ is now the unique class of sections over the disk bounded by the circle of radius $R$, and $\alpha$ is the class of a disk connecting an $S^1$-orbit to the vanishing cycle within the conic fiber and capping off with the thimble. The torus fiber collapses onto the conic $\{xz-y^2 = 0\}$ when $$\begin{equation}
    \langle [\omega], \beta \rangle = 0.
\end{equation}$$

The two sides $R > 1$ and $R < 1$ are glued together along the wall at $R = 1$, but the gluing is different for $\lambda > 0$ than for $\lambda < 0$, leading to the monodromy. Let us take $\eta = \langle
  [\omega],\alpha\rangle$ and $\xi = \langle [\omega],\beta\rangle$ as affine coordinates in the $R < 1$ region. We continue these across the $\lambda > 0$ part of the wall using correspondence between homology classes: $$\begin{equation}
    \begin{split}
      \alpha &\leftrightarrow \beta_1-\beta_2\\
      \beta &\leftrightarrow \beta_2\\
      H-2\beta-\alpha &\leftrightarrow H-\beta_1-\beta_2
      \end{split}
\end{equation}$$ Thus, in the $\lambda > 0$ part of the base, the conic appears as $\xi = 0$, while the line appears as $$\begin{equation}
    0 = \langle [\omega],H - 2\beta - \alpha\rangle = \Lambda - 2\xi - \eta
\end{equation}$$ which is a line of slope of $-1/2$ with respect to the coordinates $(\eta,\xi)$. The pair of functions $\xi$ and $\Lambda -2\xi -\eta$ also form an affine coordinate system, and in this system the corner appears as a standard quadrant.

In the $\lambda < 0$ part of the base, we instead use $$\begin{equation}
    \begin{split}
      \alpha &\leftrightarrow \beta_1-\beta_2\\
      \beta &\leftrightarrow \beta_1\\
      H-2\beta+\alpha &\leftrightarrow H-\beta_1-\beta_2
      \end{split}
\end{equation}$$ Hence in this region the conic appears as $\xi = 0$ again, while the line appears as $$\begin{equation}
       0 = \langle [\omega],H - 2\beta + \alpha\rangle = \Lambda - 2\xi + \eta
\end{equation}$$ which is a line of slope $1/2$ with respect to the coordinates $(\eta,\xi)$. The pair of functions $\xi$ and $\Lambda -2\xi +\eta$ also form an affine coordinate system, and in this system the corner appears as a standard quadrant.

The discrepancy between the two gluings represents the monodromy. As we pass from $\{R > 1, \lambda > 0\} \to \{R< 1, \lambda > 0\} \to
  \{R < 1,\lambda < 0\} \to \{R > 1, \lambda < 0\} \to \{R > 1,\lambda
  > 0\}$, the coordinates $(\eta,\xi)$ under go the transformation $(\eta,\xi) \to (\eta, \xi-\eta)$, which is indeed a simple shear. ◻
:::

Figure [2](#fig:the-bigon){reference-type="ref" reference="fig:the-bigon"} shows the affine manifold $B$. The marked point is a singularity of the affine structure, and the dotted line is a cut in the affine coordinates. The affine coordinates $\eta,\xi,\psi$ are indicated. The function $\xi$ is undefined on the cut below the singularity, while $\psi$ is undefined at points directly above the singularity. Going around the singularity counterclockwise, the monodromy of the local system of integral tangent vectors $\begin{pmatrix}1&0\\1&1\end{pmatrix}$, which also serves as the gluing map along the cut. The edges of the picture are boundaries. The upper edge corresponds to points where the torus collapses onto the line $\{y=0\}$. It has slope zero in this picture. The lower edge corresponds to points where the torus collapses onto the conic $\{xz-y^2 = 0\}$. On the left portion the lower edge has slope $-1/2$, while on the right portion it has slope $1/2$. The lower edge is actually straight with respect to the affine structure, and the nontrivial gluing is what compensates for the apparent bend.

![The affine manifold $B$.](the-bigon){#fig:the-bigon width="3in"}

On the mirror side, we compute the complex affine structure (determined by the holomorphic volume form) on the base of the torus fibration on $X^\vee$. The holomorphic volume form is $$\begin{equation}
  \label{eq:vol-form-uv}
  \Omega = \frac{du\wedge dv}{uv-1} = \frac{du\wedge dv}{w}.
\end{equation}$$ Differentiating the defining equation $uv = 1 + w$ and substituting gives the other formulas $$\begin{equation}
 \label{eq:vol-form-uw}
 \Omega = \frac{du}{u}\wedge \frac{dw}{w}, \quad \text{when}\ u \neq 0,
\end{equation}$$ $$\begin{equation}
  \label{eq:vol-form-vw}
  \Omega = -\frac{dv}{v}\wedge \frac{dw}{w}, \quad \text{when}\ v \neq 0.
\end{equation}$$ The special Lagrangian fibration on $X^\vee$ to consider is constructed in [@auroux07]. The fibers are the tori $$\begin{equation}
  \label{eq:slags}
  T_{R,\lambda} = \{(u,v)\in X^\vee \mid |uv-1| = R, |u|^2-|v|^2 =
  \lambda\}, \quad (R,\lambda) \in (0,\infty)\times (-\infty,\infty),
\end{equation}$$ and the fiber $T_{1,0}$ is a pinched torus. Thus $(R,\lambda)$ are coordinates on the base of this fibration. They are not affine coordinates, which must be computed using $\im \Omega$. Due to the simple algebraic form of this fibration, it is possible to find an integral representation of the complex affine coordinates explicitly.

::: proposition
[]{#prop:affine-coords label="prop:affine-coords"} The following functions are affine linear with respect to affine structure induced by $\im \Omega$. $$\begin{equation}
    \label{eq:affine-coords-uw}
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
    \end{split}
\end{equation}$$ ($\eta$ is defined everywhere, $\xi$ is defined where $u \neq 0$, and $\psi$ is defined where $v \neq 0$). They satisfy the following relations on their common domain of definition.

1.  At every point, $\eta$ is independent from $\xi$ and from $\psi$.

2.  In the subset where $R < 1$, the relation $\xi + \psi = 0$ holds.

3.  In the subset where $R > 1$, the relation $\xi + \psi = \eta$ holds.
:::

::: proof
*Proof.* This is essentially straightforward so we only give an example of the computation.

The general procedure for computing affine coordinates from the flux of the holomorphic volume form is as follows: we choose, over a local chart on the base, a collection of $(2n-1)$--manifolds $\{\Gamma_i\}_{i=1}^n$ in the total space $X$ such that the torus fibers $T_b$ intersect each $\Gamma_i$ in an $(n-1)$--cycle, and such that these $(n-1)$--cycles $T_b \cap \Gamma_i$ form a basis of $H_{n-1}(T_b;\Z)$. The affine coordinates $(y_i)_{i=1}^n$ are defined up to constant shift by the property that $$\begin{equation}
    y_i(b')-y_i(b) = \frac{1}{2\pi}\int_{\Gamma_i \cap \pi^{-1}(\gamma)} \im \Omega
\end{equation}$$ where $\gamma$ is any path in the local chart on the base connecting $b$ to $b'$. Because $\Omega$ is closed, this integral does not depend on the choice of $\gamma$.

To get the coordinate $\eta$, start with the submanifold $$\begin{equation}
    \Gamma_1= \{w \in \R_+\}
\end{equation}$$

The intersection $\Gamma_1 \cap T_{R,\lambda}$ is a loop on $T_{R,\lambda}$. The function $\arg(u)$ gives a coordinate on this loop (briefly, $w\in \R_+$ and $|w| = R$ determine $uv$, along with $|u|^2 - |v|^2 = \lambda$ this determines the $|u|$ and $|v|$; the only parameter left is $\arg(u)$ since $\arg(v) = - \arg(u)$), and we declare the loop to be oriented so that $-d\arg(u)$ restricts to a positive volume form on it. Using [\[eq:vol-form-uw\]](#eq:vol-form-uw){reference-type="eqref" reference="eq:vol-form-uw"} we see $$\begin{equation}
    \label{eq:im-vol-form-uw}
    \im \Omega = d\arg(u) \wedge d\log|w| + d\log|u| \wedge d\arg(w)
\end{equation}$$ Using the fact that $\arg(w)$ is constant on $\Gamma_1$, we see that for any path $\gamma$ in the subset of the base where $R < 1$ connecting $b = (R,\lambda)$ to $b'=(R',\lambda')$, we have $$\begin{equation}
    \int_{\Gamma_1\cap \pi^{-1}(\gamma)} \im \Omega =
    \int_{\Gamma_1\cap \pi^{-1}(\gamma)} d\arg(u) \wedge d\log|w|.
\end{equation}$$ But $d\arg(u) \wedge d\log|w| = d(-\log|w|\,d\arg(u)))$, so the integral above equals $$\begin{equation}
    \int_{\Gamma_1 \cap T_{b'}} -\log|w|\,d\arg(u) -
    \int_{\Gamma_1\cap T_b} -\log|w|\,d\arg(u) = 2\pi(\log R' - \log R)
\end{equation}$$ (the minus signs within the integrals are absorbed by the orientation convention for $\Gamma_1 \cap T_b$). Thus $\eta = \log
  R$ is the affine coordinate corresponding to $\Gamma_1$.

The same idea applied to $\Gamma_2 = \{u \in \R_+\}$ yields the affine coordinate $$\begin{equation}
\xi = \frac{1}{2\pi} \int_{\Gamma_2 \cap T_b} \log|u|\,d\arg(w)
\end{equation}$$ To arrive at the second formula for $\xi$, we must solve for $|u|$ in terms of $R,\lambda$, and $\theta = \arg(w)$. The equations $uv =
  1 + Re^{i\theta}$ and $|u|^2 - |v|^2 = \lambda$ imply $|u|^4 -
  \lambda|u|^2 = |1+Re^{i\theta}|^2$. Solving for $|u|^2$ by the quadratic formula and taking logarithms gives the result.

The formulas for $\psi$ are obtained by applying the same method to $\Gamma'_2 = \{v \in \R_+\}$.

To prove the linear relations, we find that $\xi + \psi$ reduces by the law of logarithms and the Cauchy integral formula to $$\begin{equation}
    \frac{1}{2\pi}\int_0^{2\pi} \log|1+Re^{i\theta}|\,d\theta = \begin{cases}0, & R<1\\ \log R, &R > 1\end{cases}
\end{equation}$$ ◻
:::

Proposition [\[prop:affine-coords\]](#prop:affine-coords){reference-type="ref" reference="prop:affine-coords"} determines the monodromy around the singular point (at $\eta = \xi = \psi = 0$) of the base, and show that the affine structure is in fact integral. Once again, the monodromy is a shear.

## The topology of the map $W$ {#sec:topology-W}

A direct computation shows that the superpotential $W$ given by [\[eq:main-lg-model\]](#eq:main-lg-model){reference-type="eqref" reference="eq:main-lg-model"} has three critical points $$\begin{equation}
  \label{eq:W-crit-pts}
  \Crit(W) = \{(v = e^{\Lambda/3}e^{2\pi i (n/3)}, w = 1) \mid n = 0, 1, 2\},
\end{equation}$$ and corresponding critical values $$\begin{equation}
  \label{eq:W-crit-vals}
  \Critv(W) = \{3e^{-\Lambda/3}e^{-2\pi i (n/3)} \mid n = 0, 1, 2\}.
\end{equation}$$ As expected, $\Critv(W)$ is the set of eigenvalues of quantum multiplication by $c_1(T\CP^2)$ in $QH^*(\CP^2)$, that is, multiplication by $3h$ in the ring $\C[h]/\langle h^3 = e^{-\Lambda}\rangle$.

::: proposition
Any regular fiber $W^{-1}(c) \subset X^\vee$ is a twice-punctured elliptic curve.
:::

::: proof
*Proof.* In the $(u,v)$ coordinates, $W^{-1}(c)$ is defined by the equation $$\begin{equation}
    u + \frac{e^{-\Lambda}v^2}{uv-1} = c,
\end{equation}$$ $$\begin{equation}
    u(uv-1) + e^{-\Lambda}v^2 = c(uv-1).
\end{equation}$$ This is an affine cubic plane curve, and it is disjoint from the affine conic $\{uv - 1=0\}$. It is smooth as long as $c$ is a regular value.

The projective closure of $W^{-1}(c)$ in $(u,v)$ coordinates is given by the homogeneous equation (with $\xi$ as the third coordinate) $$\begin{equation}
    u(uv-\xi^2) + e^{-\Lambda}v^2\xi = c\xi(uv-\xi^2).
\end{equation}$$ This is a projective cubic plane curve, hence elliptic, and it intersects the line at infinity $\{\xi = 0\}$ when $u^2v = 0$. So it is tangent to the line at infinity at $(u:v:\xi) = (0:1:0)$ and intersects it transversely at $(u:v:\xi) = (1:0:0)$. Hence the affine curve is the projective curve minus these two points. ◻
:::

::: remark
The function $W$ above is to be compared to the "standard" superpotential for $\CP^2$, namely, $$\begin{equation}
    \label{eq:toric-W}
    W = x + y + \frac{e^{-\Lambda}}{xy}
\end{equation}$$ corresponding to the choice of the toric boundary divisor, a union of three lines, as anticanonical divisor. This $W$ has the same critical values, and its regular fibers are all thrice-punctured elliptic curves. Hence smoothing the anticanonical divisor to the union of a conic and a line corresponds to compactifying one of the punctures of $W^{-1}(c)$.
:::

## Tropicalization in a singular affine structure {#sec:tropicalization}

Our goal is to find the same affine manifold $B$ (that comes from symplectic structure of $\CP^2\setminus D$) embedded in the base of the torus fibration on $X^\vee$, equipped with the *complex* affine structure. We shall see that it is obtained as a bounded chamber inside a particular tropical curve, the tropicalization of the fiber of $W$.

For some real number $\epsilon > 0$, consider the curve $W^{-1}(e^{\epsilon \Lambda})$: $$\begin{equation}
  \label{eq:fiber-to-trop}
  W = u + \frac{e^{-\Lambda}v^2}{w} = e^{\epsilon \Lambda}
\end{equation}$$ The tropicalization corresponds to the limit $\Lambda \to \infty$, or $t := e^{-\Lambda} \to 0$. The amoeba of $A(W^{-1}(t^{-\epsilon}))$ is the image of the curve in the affine base of the torus fibration on $X^\vee$. We want to produce a tropical curve in the base that reflects the asymptotic geometry of these amoebas $A(W^{-1}(t^{-\epsilon}))$ as $t \to 0$. In the standard situation, this is done by rescaling the amoebas by $\log t$ and taking the Hausdorff limit. Our situation is not standard because the affine manifold in which our tropical curve is to live has a singularity. Thus, none of the standard tropicalization techniques [@tropical-AG] apply directly. Since we do not know of any general theory of tropicalization when the affine structure is singular, we will here content ourselves with an ad hoc method involving explicit computation in two coordinate charts, and checking that the results fit together in the singular affine structure.

In the standard picture of tropicalization, one considers a family of subvarieties of an algebraic torus $V_t \subset (\C^*)^n$. The map $\Log: (\C^*)^n \to \R^n$ given by $\Log(z_1,\dots,z_n) =
(\log|z_1|,\dots,\log|z_n|)$ projects these varieties to their amoebas $\Log(V_t)$, and the rescaled limit of these amoebas is the tropicalization of the family $V_t$. The tropicalization is also given as the non-archimedean amoeba of the defining equation of $V_t$.

The map $\Log: (\C^*)^n \to \R^n$ is special Lagrangian fibration. Its fibers are the tori $\{|z_1| = r_1, \dots,|z_n| = r_n\}$. These tori are Lagrangian with respect to the standard symplectic form, and they are special with respect to the holomorphic volume form $$\begin{equation}
  \label{eq:toric-vol-form}
  \Omega_{\text{toric}} = \frac{dz_1}{z_1} \wedge \cdots \wedge \frac{dz_n}{z_n},
\end{equation}$$ which has logarithmic poles along the coordinate hyperplanes in $\C^n$. The complex affine coordinates are $\log |z_i|$.

The torus fibration on $X^\vee$ is approximated by this standard structure as follows. Equation [\[eq:vol-form-uw\]](#eq:vol-form-uw){reference-type="eqref" reference="eq:vol-form-uw"} shows that in the $(w,u)$ coordinates (where $u \neq 0$), the holomorphic volume form is standard. If the special Lagrangian fibration were also standard, the affine coordinates would be $(\log|w|,\log|u|)$. Proposition [\[prop:affine-coords\]](#prop:affine-coords){reference-type="ref" reference="prop:affine-coords"} shows that, while $\eta = \log|w|$ is still an affine coordinate (reflecting the fact that there is still an $S^1$-symmetry), the other affine coordinate $\xi$ is the average value of $\log|u|$ along a loop in the fiber. We also see that as $|\lambda|$ becomes large, the approximation $\xi \approx \log|u|$ holds with increasing accuracy. Similarly, in the $(w,v)$ coordinates (when $v \neq 0$), the holomorphic volume form is standard, and $\eta
= \log|w|$ and $\psi \approx \log|v|$ form affine coordinates.

We shall see that as $t = e^{-\Lambda} \to 0$, the amoebas $A(W^{-1}(t^{-\epsilon}))$ move farther away from the singularity, where the approximations $\xi \approx \log|u|$ and $\psi \approx
\log|v|$ hold with increasing accuracy, while $\eta = \log|w|$ holds exactly everywhere.

The approximations $\xi \approx \log|u|$ and $\psi \approx \log|v|$ and the identity $\eta = \log|w|$ suggest the approach to finding the tropicalization. We represent the equation $W = u + e^{-\Lambda}v^2/w = e^{\epsilon \Lambda}$ as a polynomial equation in the coordinates $(w,u) \in (\C^*)^2$. We then compute the corresponding tropical curve, using the standard procedures [@tropical-AG], and we plot the result in the affine plane whose coordinates are $(\log|w|, \log|u|)$. This is shown in Figure [3](#fig:tropical-fiber){reference-type="ref" reference="fig:tropical-fiber"}(a). We repeat the process in the coordinate system $(w,v)$, and plot the resulting tropical curve in the affine plane whose coordinates are $(\log|w|, \log|v|)$. This is shown in Figure [3](#fig:tropical-fiber){reference-type="ref" reference="fig:tropical-fiber"}(b). We then transfer these tropical curves into the singular affine manifold by simply identifying $\xi$ with $\log|u|$ and $\psi$ with $\log|v|$.

We now observe that the two curves actually match up, at least away from the vertical line passing through the singularity, and we claim that the result is as depicted in Figure [3](#fig:tropical-fiber){reference-type="ref" reference="fig:tropical-fiber"}(c). This is evident in comparing the left-hand portions of parts (a) and (b) of Figure [3](#fig:tropical-fiber){reference-type="ref" reference="fig:tropical-fiber"}. On the right-hand portion, we must take into account that the coordinate $\psi \approx \log|v|$ has been affected by a shear in passing from (b) to (c).

There is apparently a problem along the vertical line passing through the singularity, since the curves depicted in (a) and (b) have vertical legs there, which we claim do not appear in (c). Our reasoning is this: the coordinate system $(w,u) \in (\C^*)^2$ only covers the locus where $u \neq 0$, which is also where the function $\xi$ is well defined. Thus we cannot expect the curve in (a) to be valid near the vertical going down from the singularity, it is valid above the singularity. Conversely, the figure in (b) is only valid in the region below the singularity. Thus the extra vertical legs are illusory.

We call the resulting tropical curve $T_\epsilon$.

::: proposition
[]{#prop:tropical-fiber label="prop:tropical-fiber"} For $\epsilon > 0$, $T_\epsilon$ is a trivalent graph with two vertices, a cycle of two finite edges, and two infinite edges.
:::

![The tropical fiber of $W$ for $\epsilon > 0$. (a) $(w,u)$ coordinates. (b) $(w,v)$ coordinates. (c) The tropical fiber $T_\epsilon$.](tropical-fiber){#fig:tropical-fiber width="5.75in"}

::: proposition
[]{#prop:tropical-fiber-chamber label="prop:tropical-fiber-chamber"} For $\epsilon > 0$, the complement of $T_\epsilon$ has a bounded component that is an integral affine manifold with singularities that is isomorphic, after rescaling, to the base $B$ of the special Lagrangian fibration on $\CP^2 \setminus D$ with the affine structure coming from the symplectic form.
:::

::: remark
The topology of the tropical curve $T_\epsilon$ corresponds to that of a twice-punctured elliptic curve.
:::

::: remark
We can apply the same patching procedure for $\epsilon$ in the range $(-1/3) < \epsilon < 0$. This changes Figure [3](#fig:tropical-fiber){reference-type="ref" reference="fig:tropical-fiber"} so that the triangles in (a) and (b) become smaller and they lie entirely below point marked with $\times$. Thus, assuming that (a) is valid above the singularity, while (b) is valid below the singularity, we find that $T_\epsilon$ is essentially the same as what appears in (b), but that the vertical leg must terminate at the singularity, in order to be consistent with the fact that in (a) no part of the curve appears above the singularity. Thus we find that $T_\epsilon$ is a trivalent graph with three vertices, a cycle of three finite edges, two infinite edges and one edge connecting a vertex to the singular point of the affine structure.

We note that the value $\epsilon = -1/3$ corresponds to the critical values of $W$.
:::

::: remark
This proposition is another case of the phenomenon, described in Abouzaid's paper [@abouzaid06], that for toric varieties, the bounded chamber of the fiber of the superpotential is isomorphic to the moment polytope. In the general case of a manifold $X$ with effective anticanonical divisor $D$, the boundary of the symplectic affine base of the torus fibration on $X\setminus D$ corresponds to a torus fiber collapsing onto $D$, a particular class of holomorphic disks having vanishing area, and the corresponding term of the superpotential having unit norm. On the other hand, the tropicalization of the fiber of the superpotential has some parts corresponding to one of the terms having unit norm, and it is expected that these bound a chamber which is isomorphic to the base of the original torus fibration.
:::
