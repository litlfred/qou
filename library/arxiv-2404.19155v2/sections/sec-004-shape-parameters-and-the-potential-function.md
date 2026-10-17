---
doc_id: arxiv-2404.19155v2
doc_title: "Octahedral coordinates from the Wirtinger presentation"
section_id: sec-004-shape-parameters-and-the-potential-function
section_title: "Shape parameters and the potential function"
section_number: null
pages: 14-19
source_pdf: 2404.19155v2.pdf
source_sha256: 45b9ed90006536b3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.84
latex_coverage_ratio: 0.892
doc_brief: "Octahedral coordinates from the Wirtinger presentation — Let ρ be a representation of a knot group (or more generally, the funda- mental group of a tangle complement) into SL2(C) expressed in terms"
---
[]{#sec:potential label="sec:potential"}

One way to subdivide the octahedral decomposition is to split the octahedron at each crossing into four tetrahedra as in [1](#fig:shape-parameters-diagram){reference-type="ref" reference="fig:shape-parameters-diagram"}, with one for each region touching the crossing. We can geometrize the tetrahedra by placing their vertices in the boundary at infinity of hyperbolic space, i.e. $\psp$. Such geometric ideal tetrahedra are determined up to congruence by the cross-ratio of their vertices, usually called the . In this case these parameters are given by [\[eq:b-shapes\]](#eq:b-shapes){reference-type="ref" reference="eq:b-shapes"}. When a shape parameter is $0$, $1$, or $\infty$ it represents a geometrically degenerate tetrahedron whose vertices coincide. [\[thm:gauge-equivalent-to-admissible\]](#thm:gauge-equivalent-to-admissible){reference-type="ref" reference="thm:gauge-equivalent-to-admissible"} says that for a given representation we can always avoid tetrahedra with shape $0$ or $\infty$. In this section we study when tetrahedra with shape $1$ occur.

<figure id="fig:shape-parameters-diagram">

<figcaption> One can divide the octahedron at a crossing into four tetrahedra, one for each region touching the crossing. The shape parameters are then given as ratios of the <span class="math inline"><em>b</em></span> and <span class="math inline"><em>m</em></span>-coordinates, as in <a href="#eq:b-shapes" data-reference-type="ref" data-reference="eq:b-shapes">[eq:b-shapes]</a>. </figcaption>
</figure>

::: definition
An octahedral coloring of a crossing is if any of the shape parameters $$\label{eq:b-shapes}
    z_N
    =
    \frac{
      b_{2'}  
      }{
      b_1   
    }
    ,
    z_W
    =
    \frac{
      b_2
      }{
      m_1 b_1
    }
    ,
    z_S
    =
    \frac{
      m_2 b_2 
      }{
      m_1 b_{1'}
    }
    ,
    z_E
    =
    \frac{
      m_2 b_{2'}
      }{
      b_{1'}
    }$$ are $1$. (These quantities can never be $0$ or $\infty$ as part of the definition of octahedral coloring.) An octahedral coloring of a diagram is pinched if any of its crossings are.
:::

We can use [\[def:associated-octahedral\]](#def:associated-octahedral){reference-type="ref" reference="def:associated-octahedral"} to directly find the shape parameters of the octahedral coloring associated to a decorated representation. As a corollary we see that being pinched is a gauge-invariant property.

::: theorem
[]{#thm:shape-formula label="thm:shape-formula"} Let $D$ be a tangle diagram with an admissible decorated shadow $\slg$ coloring $i \mapsto (g_i, L_i), j \mapsto u_j$ and let $c$ be a crossing of $D$.

::: thmenum
[]{#thm:shape-formula:formula label="thm:shape-formula:formula"} The shape parameters of the crossing are given by $$\begin{aligned}
        \label{eq:zN-formula}
        z_N
      &=
      \frac{
        v_1 u_N
        }{
        v_1 \evec{2}
      }
      \frac{
        v_{2'} \evec{2}
        }{
        v_{2'} u_N
      }
      =
      \frac{
        h(v_{1} \upf{u_N})
        }{
        h(v_{2'} \upf{u_N})
      }
      \\
      \label{eq:zW-formula}
      z_W
      &=
      \frac{
        v_{1} u_W
        }{
        v_{1} \evec{2}
      }
      \frac{
        v_{2} \evec{2}
        }{
        v_{2} u_W
      }
      =
      \frac{
        h(v_{1} \upf{u_W})
        }{
        h(v_{2} \upf{u_W})
      }
      \\
      \label{eq:zS-formula}
      z_S
      &=
      \frac{
        v_{1'} u_S
        }{
        v_{1'} \evec{2}
      }
      \frac{
        v_{2'} \evec{2}
        }{
        v_{2'} u_S
      }
      =
      \frac{
        h(v_{1'} \upf{u_S})
        }{
        h(v_{2'} \upf{u_S})
      }
      \\
      \label{eq:zE-formula}
      z_E
      &=
      \frac{
        v_{1'} u_E
        }{
        v_{1'} \evec{2}
      }
      \frac{
        v_{2'} \evec{2}
        }{
        v_{2'} u_E
      }
      =
      \frac{
        h(v_{1'} \upf{u_E})
        }{
        h(v_{2'} \upf{u_E})
      }
    
\end{aligned}$$ in terms of the $$h\left(
        \begin{bmatrix}
          v^1 & v^2
        \end{bmatrix}
      \right)
      \mathrel{:=}\frac{v^1}{v^2}.$$ Here the regions and segments are labeled as in [\[fig:crossing-types\]](#fig:crossing-types){reference-type="ref" reference="fig:crossing-types"} and the $v_i$ are nonzero elements of the $L_i$ (i.e.representative eigenvectors).

[]{#thm:shape-formula:pinched label="thm:shape-formula:pinched"} The crossing is pinched if and only if $L_1 = L_2$. Note that this condition does not depend on the choice of shadow coloring and is invariant under gauge transformations.
:::
:::

::: proof
*Proof.* [\[thm:shape-formula:formula\]](#thm:shape-formula:formula){reference-type="ref" reference="thm:shape-formula:formula"} follows directly from the expressions for $b_1$ and $b_{2'}$ in [\[def:associated-octahedral\]](#def:associated-octahedral){reference-type="ref" reference="def:associated-octahedral"} and $$v_1 \upf{u_N} = \begin{bmatrix}
      v_1 u_N & v_1 \evec{2}
    \end{bmatrix}
    .$$ The same method gives $$z_W = 
    m_1^{-1}
    \frac{
      v_{1} u_N
      }{
      v_{1} \evec{2}
    }
    \frac{
      v_{2} \evec{2}
      }{
      v_{2} u_W
    }
    =
    m_1^{-1}
    \frac{
      h(v_{1} \upf{u_N})
      }{
      h(v_{2} \upf{u_W})
    }
    .$$ To obtain [\[eq:zW-formula\]](#eq:zW-formula){reference-type="ref" reference="eq:zW-formula"}, write $$m_1^{-1} v_1 u_N
    =
    v_1 g_1 u_N
    =
    v_1 u_W$$ as $u_W = g_1 u_N$ by the definition of shadow coloring. follow from the same argument.

[\[thm:shape-formula:pinched\]](#thm:shape-formula:pinched){reference-type="ref" reference="thm:shape-formula:pinched"} One can use [\[eq:b-transf-positive,eq:b-transf-negative\]](#eq:b-transf-positive,eq:b-transf-negative){reference-type="ref" reference="eq:b-transf-positive,eq:b-transf-negative"} to show that $z_W = 1$ if and only if the crossing is pinched. $\upf{u_W}$ is invertible, so $v_1 \upf{u_W}$ and $v_2 \upf{u_W}$ are dependent iff $v_1$ and $v_2$ are. ◻
:::

The following corollary is useful when defining state integrals for the quantum invariants constructed in [@McPhailSnyderVolume].

::: corollary
If $\rho : \pi(D) \to \slg$ is a non-pinched representation, then it is gauge-equivalent to a shadow coloring for which no shape parameter lies on the unit circle.
:::

::: proof
*Proof.* The argument is similar to the proof of [\[thm:gauge-equivalent-to-admissible\]](#thm:gauge-equivalent-to-admissible){reference-type="ref" reference="thm:gauge-equivalent-to-admissible"}. The shape parameter for a corner by segments $i$ and $k$ near region $j$ is $$z_{ik}^{j} =
    \frac{
      v_i u_j
      }{
      v_k u_j
    }
    \frac{
      v_k \evec{2}
      }{
      v_i \evec{2}
    }$$ By [\[eq:type-A-gauge\]](#eq:type-A-gauge){reference-type="ref" reference="eq:type-A-gauge"} after applying a type (A) gauge transformation by $A \in \slg$ the shape parameter $$z_{ik}^{j} =
    \frac{
      v_i u_j
      }{
      v_k u_j
    }
    \frac{
      v_k A \evec{2}
      }{
      v_i A \evec{2}
    }
    =
    C_{ik}^{j}
    \frac{
      v_k x
      }{
      v_j x
    }$$ where $C_{ik}^j = v_i u_u / v_k u_j$ and $x = A \evec{2}$. This is homogeneous in $x$ so we can think of it as a function defined on $\psp$. Let $$X_{i k}^j = 
    \left\{ \def\given{\ \middle| \ }   [x]  \given |C_{ik}^{j} v_j x|^2 = |v_k x|^2  \right\}   \subset \psp$$ be the set of points for which this particular shape parameter lies on the unit circle. Our claim is that the union $X = \bigcup X_{ik}^{j}$ is not all of $\psp$. Because this is a finite union it is enough to show that each $X_{ik}^{j}$ is a circle in the Riemann sphere.

Because no crossing is pinched $v_i$ and $v_k$ are independent, so there is a fractional linear transformation $B \in \slg$ with $v_i B = \evec{1}^{\mathrm{T}}$ and $v_k B = \evec{2}^{\mathrm{T}}$. If we change variables to $y = (y_0, y_1) = B x$ our equation becomes $$|C_{i,k}^{j}|^2 |y_0|^2 = |y_1|^2$$ Viewed as an equation for $h(y) = y_0/y_1$ in the Riemann sphere this describes a circle. Because fractional linear transformations preserve circles we see that $X_{ik}^{j}$ is a circle as well. ◻
:::

To explain the connection to the Volume Conjecture we introduce a version of the Neumann-Zagier--Yokota potential function of the diagram defined using the dilogarithm $$\mathop{\mathrm{Li_2}}(z)
  \mathrel{:=}
  \int_{0}^{z}
  \frac{
    - \log(1-t)
    }{
    t
  }
  dt
  .$$ $\mathop{\mathrm{Li_2}}$ has a branch point at $1$, where it is continuous but not differentiable. It can be used to compute the volumes [@Zagier2007] and Chern-Simons invariants [@Neumann2004] of hyperbolic $3$-manifolds. Set $$\mathop{\mathrm{L}}(\zeta)
  \mathrel{:=}
  \frac{
    \mathop{\mathrm{Li_2}}(e^{2\pi \mathsf{i}\zeta})
    }{
    2\pi \mathsf{i}
  }
  .$$ Let $D$ be a link with $\ell$ components. Fix a choice $\mu = (\mu_1, \dots, \mu_\ell)$ of complex number for each component of $\ell$ and introduce a variable $\beta_1, \dots, \beta_n$ for each segment of $D$. We think of the $\beta_i$ and $\mu_j$ as logarithms of the $b$ and $m$ coordinates of some octahedral coloring. For each crossing $c$ (as in [1](#fig:shape-parameters-diagram){reference-type="ref" reference="fig:shape-parameters-diagram"}) of $D$ set $$\potl[c]{} =
  \mathop{\mathrm{L}}(\beta_{2'} - \beta_{1})
  -\mathop{\mathrm{L}}(\beta_2 - \beta_1 - \mu_1)
  +\mathop{\mathrm{L}}(\beta_{2} - \beta_{1'} + \mu_2 - \mu_1)
  -\mathop{\mathrm{L}}(\beta_{2'} - \beta_{1'} + \mu_2)
  .$$ The arguments are logarithms of the shape parameters [\[eq:b-shapes\]](#eq:b-shapes){reference-type="eqref" reference="eq:b-shapes"}.

::: definition
The of $D$ with respect to $\mu$ is $$\label{eq:potential-function}
    \potl[D, \mu]{\beta_1, \dots, \beta_n}
    =     
    \sum_{\text{crossings } c}
    \epsilon(c) \Phi_c$$ where $\epsilon(c) = +1$ for positive crossings and $-1$ for negative crossings. Because $\mathop{\mathrm{Li_2}}$ has a branch point at $1$ this function is analytic when the arguments of the functions $\mathop{\mathrm{L}}$ (i.e.the logarithms of the shape parameters) are not in $2\pi \mathsf{i}\mathbb{Z}$.
:::

::: theorem
[]{#thm:critical-points-are-reps label="thm:critical-points-are-reps"} Let $\mathcal{C}_{D, \mu}$ be the set of generalized critical points of $\potl[D, \mu]{}$, i.e.points $\beta = (\beta_1, \dots, \beta_n)$ where $$\frac{
        \partial \potl[D, \mu]{}
      }{
        \partial \beta_i
      }
      \equiv
      0
      \pmod{2\pi \mathsf{i}}
      \text{ for }
      i = 1, \dots, n.$$ Then there are numbers $a_i$ so that $$i \mapsto (a_i, \exp(2\pi \mathsf{i}\beta_i), \exp(2\pi \mathsf{i}\mu_{k(i)}) )$$ is an octahedral coloring of $D$, where $\mu_{k(i)}$ is the meridian log-parameter associated with the component $k(i)$ of segment $i$.
:::

::: proof
*Proof.* By [@McPhailSnyder2022 Theorem 6.3] non-pinched colorings are in bijection with solutions of the of the diagram; these are a set of rational equations in the $b$-variables, with one for each segment. A solution of the segment equations determines an $a$-variable for each segment yielding an octahedral coloring, and it exists if and only if the gluing equations of the four-term decomposition have nondegenerate solutions. Because $$\frac{
      d
      }{
      d\zeta
    }
    \mathop{\mathrm{L}}(\zeta)
    =
    -
    \log(1 - e^{2\pi \mathsf{i}\zeta})$$ we can work out that $$\exp
    \frac{
      \partial \potl[D, \mu]{}
      }{
      \partial \beta_i
    }
    =
    1$$ is the segment equation of segment $i$. ◻
:::

One can easily handle pinched crossings by working directly with octahedral colorings or by using shadow $\slg$-colorings and [\[thm:holonomies-match\]](#thm:holonomies-match){reference-type="ref" reference="thm:holonomies-match"}. However, the smoothness of $\potl[D, \mu]{}$ is still significant for the Volume Conjecture. Most proofs follow @Yokota2000 by showing that the large $N$ asymptotics of the Kashaev invariant are given by a contour integral of the form $$\int_{\Gamma} e^{N \potl[D, \mu]{\beta_1, \dots, \beta_n}} \,d\beta_1 \cdots d\beta_n$$ as $N \to \infty$. The saddle-point method for determining the asymptotics of these integrals works best near analytic critical points of $\potl[D,\mu]{}$. More significantly the proof usually requires moving the contour $\Gamma$ through the parameter space which requires $\potl[D, \mu]{}$ to be complex-analytic.

As part of this argument it is important to know whether a representation $\rho$ occurs as the holonomy of an octahedral coloring from an *analytic* critical point. Typically we only care about $\rho$ up to conjugacy, which motivates the following definition:

::: definition
Let $\rho : \pi(L) \to \slg$ be a representation of a link group and $D$ a diagram of $L$. We say that $\rho$ is if it is conjugate to the holonomy of a non-pinched octahedral coloring $\chi$ of $D$, i.e.to the holonomy of a generalized critical point.
:::

::: corollary
[]{#thm:detection-condition label="thm:detection-condition"} Let $D$ be any link diagram and $\rho : \pi(D) \to \slg$ a decorated representation. Then $\rho$ is $D$-smooth if and only if for each crossing of $D$ the lines $L_1$ and $L_2$ are distinct.
:::

::: proof
*Proof.* [\[thm:shape-formula\]](#thm:shape-formula){reference-type="ref" reference="thm:shape-formula"}[\[thm:shape-formula:pinched\]](#thm:shape-formula:pinched){reference-type="ref" reference="thm:shape-formula:pinched"}. ◻
:::

In other words, $\rho$ corresponds to a pinched octahedral coloring if and only if at some crossing the images of the Wirtinger generators have the same distinguished fixed point when acting on $\psp$ by fractional linear transformations. If we restrict our attention to hyperbolic knots then we can give a purely group-theoretic characterization. Recall that the holonomy of the complete hyperbolic structure is a faithful, discrete representation $\rho : \pi(K) \to \pslg$. It is boundary-parabolic (the meridians have eigenvalues $\pm 1$) and always lifts to $\slg$. Because its meridians are parabolic it has a unique decoration.

::: definition
A tangle diagram $D$ is if at each crossing the Wirtinger generators of the over and under arcs are distinct elements of $\pi(T)$.
:::

::: bigtheorem
[]{#thm:arc-faithful label="thm:arc-faithful"} Let $D$ be a diagram of a hyperbolic knot. The holonomy $\rho$ of its complete hyperbolic structure is $D$-smooth if and only if $D$ is arc-faithful.
:::

::: proof
*Proof.* The only if is obvious: if two adjacent arcs have the same Wirtinger generators then their images always share a fixed point.

Conversely, suppose $\rho$ corresponds to a pinched octahedral coloring of $D$ so there are Wirtinger generators $w_1$ and $w_2$ for which $\rho(w_1)$ and $\rho(w_2)$ have the same fixed point. As $\rho(w_1)$ and $\rho(w_2)$ are parabolic this implies they commute, hence $w_1$ and $w_2$ commute as $\rho$ is faithful. By the classification of finitely generated abelian subgroups of $3$-manifold groups [@Hempel1976 Theorem 9.13] two commuting infinite-order elements generate a subgroup isomorphic to $\mathbb{Z}$ or $\mathbb{Z} \times \mathbb{Z}$. As $w_1$ and $w_2$ map to the same element of the first homology they must generate a $\mathbb{Z}$ subgroup. They are primitive and map to the same homology class so they must be equal. ◻
:::

The existence of analytic critical points of $\potl[D, \mu]{}$ has previously been studied, and we can express our results in this context. An edge of an ideal triangulation of a knot complement is (homtopically) if it is homotopic to a curve in the boundary of a regular neighborhood of the knot.

::: corollary
[]{#thm:non-peripheral label="thm:non-peripheral"} Let $D$ be a diagram of a hyperbolic knot.

::: thmenum
[]{#thm:non-peripheral:equiv label="thm:non-peripheral:equiv"} The edges of the four-term octahedral decomposition associated to $D$ are homotopically non-peripheral if and only if $D$ is arc-faithful.

[]{#thm:non-peripheral:alternating label="thm:non-peripheral:alternating"} If $D$ is reduced and alternating then it is arc-faithful.
:::
:::

::: proof
*Proof.* [\[thm:non-peripheral:equiv\]](#thm:non-peripheral:equiv){reference-type="ref" reference="thm:non-peripheral:equiv"} If $D$ is arc-faithful then there is a non-pinched octahedral coloring $\chi$ with holonomy the complete hyperbolic structure. From $\chi$ we can obtain a nondegenerate solution of the gluing equations of the octahedral decomposition, and by [@Dunfield2012 Lemma 3.5] the existence of such a solution implies the edges of the octahedral decomposition are homotopically non-peripheral.

Conversely, suppose the edges of the octahedral decomposition are homotopically non-peripheral. Then by the paragraph before [@Dunfield2012 Remark 3.4] the complete hyperbolic structure occurs as a non-degenerate solution of the gluing equations, hence as a non-pinched octahedral coloring.

[\[thm:non-peripheral:alternating\]](#thm:non-peripheral:alternating){reference-type="ref" reference="thm:non-peripheral:alternating"} @Garoufalidis2016 and @Sakuma2018 independently showed that the edges of the four-term decomposition of a reduced alternating diagram are non-peripheral. Part [\[thm:non-peripheral:equiv\]](#thm:non-peripheral:equiv){reference-type="ref" reference="thm:non-peripheral:equiv"} implies such a diagram is arc-faithful. ◻
:::

It is easy to find diagrams that are not arc-faithful. However, by avoiding these obvious bad configurations it also seems easy to find arc-faithful diagrams.

::: example
Any diagram with a kink

::: center
:::

is never-arc faithful. More generally any piece of a diagram that looks like

::: center
:::

will prevent arc-faithfulness.
:::

According to @DiagramSite's database [@DiagramSite] of boundary-parabolic representations every hyperbolic knot with at most $12$ crossings has an arc-faithful diagram. We conjecture this holds for all hyperbolic knots, and as discussed above this seems relevant to a general proof of the Volume Conjecture.

::: conjecture
Every hyperbolic knot has an arc-faithful diagram.
:::
