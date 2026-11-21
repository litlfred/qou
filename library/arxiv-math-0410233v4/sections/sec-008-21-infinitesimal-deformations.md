---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMATION"
section_id: sec-008-21-infinitesimal-deformations
section_title: "Infinitesimal deformations"
section_number: 2.1
pages: 7-9
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.971
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp shape."
---
Now, we may study deformations by considering possible "derivatives at time $t$" of $X_t$, or infinitesimal deformations of hyperbolic structure,

for any time $t$.

Each of these infinitesimal deformations corresponds to an element in a certain cohomology group $H^1(X; E)$, where recall $X=M-\Sigma$. We will be manipulating elements of $H^1(X;E)$, so we recall some information on their structure.

### Cohomology

Given $\omega$ in $H^1(X;E)$, $\omega$ is a one--form on $X$ with values in the vector bundle $E$ of infinitesimal isometries of $X$. The bundle $E$ has fiber $sl(2,{\mathbb{C}})$, which is the Lie algebra of infinitesimal isometries of ${\mathbb{H}}^3$. Recall that this Lie algebra has a complex structure. Geometrically, if $s$ represents an infinitesimal translation in the direction of $s$, then $i s$ represents an infinitesimal rotation with axis in the direction of $s$. Thus on $X$ we can identify $E$ with the complexified tangent bundle $TX \otimes {\mathbb{C}}$, and write any $\omega \in H^1(X;E)$ in complex form: $\omega = v + iw$.

By the Hodge theorem proved in [@hk:cone-rigid], in each cohomology class of $H^1(X;E)$ there is a *harmonic* representative of the form $$\omega = \eta + i*D\eta,$$ where $\eta$ is a unique $TX$-valued 1--form on $X = M-\Sigma$ that satisfies: $$D^*\eta=0,$$ $$D^*D\eta + \eta =0.
\label{eqn:d*deta}$$ Here $D$ is the exterior covariant derivative on such forms and $D^*$ is its adjoint.

Thus we may assume that our cone deformation is chosen such that at each time $t$, the infinitesimal deformation of hyperbolic structure of $X_t$ corresponds to a *harmonic* element $\omega$ in $H^1(X;E)$.

### Tubular and Horoball neighborhoods

For purposes of this paper, we are particularly interested in the effect of the deformation in a neighborhood of the singular locus or in a horoball neighborhood of a cusp. So in this subsection, we will review a decomposition of $\omega$ (and $\eta$) into a nice form in these types of neighborhoods.

Select a component of the singular locus $\Sigma$ of $M$. Let $V$ be a tubular neighborhood of that component, with tube radius $R$. $V$ is a solid torus with a singular core curve. During the cone deformation, the geometric structure on $V$ is changing in meridional, longitudinal, and radial directions. We can write $\omega$ in $V$ to reflect this: $$\omega = \omega_0 + \omega_c.
\label{eqn:omega-decomp}$$ Here only $\omega_0 = \eta_0 + i*D\eta_0$ changes the holonomy of the meridian and longitude on the torus $\partial V$, and $\omega_c$ is a correction term.

We can further decompose $\omega_0$ as follows: $$\omega_0 = u\, \omega_m + (x+iy)\,\omega_\ell.
\label{eqn:omega_0-decomp}$$ Here, $u$, $x$, and $y$ are real numbers. The 1--forms $\omega_m$ and $\omega_\ell$ are standard forms, calculated in [@hk:cone-rigid], which depend only on the tube radius $R$ of $V$. The form $\omega_m =
\eta_m + i*D\eta_m$ gives the change in the meridional direction. In particular, it represents the infinitesimal deformation which decreases the cone angle but doesn't change the real part of the complex length of the meridian. The form $\omega_\ell = \eta_\ell
+i*D\eta_\ell$ stretches the singular locus, but leaves the holonomy of the meridian unchanged.

Since we will use the explicit formula for the standard form $\omega_\ell$ in a calculation in a later section, we will restate that form here. Let $e_1$, $e_2$, and $e_3$ be an orthonormal frame for $V$ in cylindrical coordinates, with $e_1$ pointing in the radial direction and $e_2$ tangent to the meridian. Let $R$ be the radius of the tube $V$. Recall $\omega_\ell$ is a ($TX\otimes{\mathbb{C}}$)--valued 1--form, which can be viewed as an element of $Hom(TX, TX\otimes{\mathbb{C}})$. Thus it can be described as a matrix in the cylindrical coordinates $e_1$, $e_2$, $e_3$. $$\omega_\ell(R) = \left[
    \begin{array}{ccccc}
      (\cosh R)^{-2} & \hspace{.1in} & 0 &\hspace{.1in}& 0 \\
      0 && -1 && -i\tanh R \\
      0 && -i\tanh R && 1+ (\cosh R)^{-2}
    \end{array}
    \right]
  \label{eqn:omega_l}$$

Now, so far, our decomposition of $\omega$ has been in a tubular neighborhood $V$ of a component of the singular locus. We can do a similar decomposition of $\omega$ in a horoball neighborhood $U$ of a cusp. In fact, we may consider $U$ as a tubular neighborhood of a 1--dimensional submanifold of $M$ on which the cone angle remains $0$ throughout the deformation, and the tube radius is infinite. Again we may decompose $\omega$ as $\omega_0 + \omega_c$, where only $\omega_c$ affects the holonomy of the torus $\partial U$. But now, since the cone angle at the core of $U$ is not changing, the meridional part of $\omega_0$ is identically $0$. Thus in this case, $$\omega_0 = (x + iy)\, \omega_\ell,$$ where again $x$ and $y$ are real numbers, and $\omega_\ell$ is a standard form. Since the tube radius of $U$ is infinite, to write down the formula for $\omega_\ell$ explicitly we let $R$ go to infinity in equation ([\[eqn:omega_l\]](#eqn:omega_l){reference-type="ref" reference="eqn:omega_l"}). $$\omega_\ell(\infty) = \left[
    \begin{array}{ccc}
      0 & 0 & 0\\
      0 & -1 & -i\\
      0 & -i & 1
    \end{array}\right]
  \label{eqn:omega_l-cusp}$$
