---
doc_id: arxiv-2404.19155v2
doc_title: "Octahedral coordinates from the Wirtinger presentation"
section_id: sec-002-the-holonomy-of-an-octahedral-coloring
section_title: "The holonomy of an octahedral coloring"
section_number: null
pages: 7-13
source_pdf: 2404.19155v2.pdf
source_sha256: 45b9ed90006536b3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.839
doc_brief: "Octahedral coordinates from the Wirtinger presentation — Let ρ be a representation of a knot group (or more generally, the funda- mental group of a tangle complement) into SL2(C) expressed in terms"
---
[]{#sec:holonomy label="sec:holonomy"}

In this section we define the holonomy representation of an octahedral coloring and show that it is compatible with our method of assigning an octahedral coloring to a shadowed decorated $\slg$-coloring, thus justifying [\[def:associated-octahedral\]](#def:associated-octahedral){reference-type="ref" reference="def:associated-octahedral"}. To define the holonomy we must first introduce a groupoid presentation of $\pi(D)$.

Recall the characterization of a group $G$ as a category with a single object $\bullet$ and an invertible morphism $g : \bullet \to \bullet$ for each $g \in G$. A is the natural generalization: there can be more than one object, but all morphisms are still invertible. For example, instead of the fundamental group of a topological space with a single basepoint, one can consider a fundamental groupoid with multiple basepoints whose morphisms $p \to q$ are homotopy classes of paths from $p$ to $q$. Two paths (morphisms) $f$ and $g$ are composable only when the endpoint (codomain) of $f$ is the startpoint (domain) of $g$. For a tangle complement it is natural to put one basepoint in each region.

::: marginfigure
:::

::: definition
[]{#def:tangle-groupoid label="def:tangle-groupoid"} Let $D$ be a tangle diagram. The $\gpoid{D}$ of $D$ has

-   one object (i.e.basepoint) for each region of $D$,

-   two generators $x_i^{\pm}$ for each segment $i$, representing paths above and below the segment (see [\[fig:tangle-groupoid-generators\]](#fig:tangle-groupoid-generators){reference-type="ref" reference="fig:tangle-groupoid-generators"}), and

-   three relations for each crossing:

    ::: marginfigure
    :::

    $$\begin{gathered}
        \label{eq:groupoid-relation-above}
        x_1^+ x_2^+ = x_{2'}^+ x_{1'}^+
        \\
        \label{eq:groupoid-relation-below}
        x_1^- x_2^- = x_{2'}^- x_{1'}^-
        \\
        \label{eq:groupoid-relation-thru}
        \begin{cases}
          x_1^{-} x_{2}^{+}
          =
          x_{2'}^{+} x_{1'}^{-}
          &
          \text{ for a positive crossing, or}
          \\
          x_1^{+} x_{2}^{-}
          =
          x_{2'}^{-} x_{1'}^{+}
          &
          \text{ for a negative crossing.} 
        \end{cases}
      
    \end{gathered}$$ where the indices $1,2, 1', 2'$ refer to the segments at the crossing as in [\[fig:crossing-types\]](#fig:crossing-types){reference-type="ref" reference="fig:crossing-types"}.
:::

One can derive relations ([\[eq:groupoid-relation-above\]](#eq:groupoid-relation-above){reference-type="ref" reference="eq:groupoid-relation-above"},[\[eq:groupoid-relation-below\]](#eq:groupoid-relation-below){reference-type="ref" reference="eq:groupoid-relation-below"},[\[eq:groupoid-relation-thru\]](#eq:groupoid-relation-thru){reference-type="ref" reference="eq:groupoid-relation-thru"}) by drawing diagrams like [\[fig:tangle-groupoid-relations\]](#fig:tangle-groupoid-relations){reference-type="ref" reference="fig:tangle-groupoid-relations"}. It is possible to prove that $\Pi(D)$ is equivalent to the fundamental group $\pi(T)$ and thus to $\pi(D)$ by using the groupoid version [@Brown2006 Chapter 9] of the van Kampen theorem. We do not need this result so we omit the details.

For an octahedral color $\chi = (a, b, m)$ we write $$\begin{gathered}
  \label{eq:chi-up-hol}
  \upf{\chi} \mathrel{:=}
  \begin{bmatrix}
    a & 0 \\
    (a - 1/m)/b & 1
  \end{bmatrix}
  \\
  \label{eq:chi-down-hol}
  \dnf{\chi} \mathrel{:=}
  \begin{bmatrix}
    1 & (a - m)b \\
    0 & a
  \end{bmatrix}
  \intertext{and}
  \label{eq:chi-around-hol}
  \aroundhol{\chi}
  \mathrel{:=}
  \upf{\chi} \dnf{\chi}^{-1}
  =
  \begin{bmatrix}
    a & -(a-m) b \\
    (a-1/m)/b & m + m^{-1} -a
  \end{bmatrix}
\end{gathered}$$

::: definition
[]{#def:holonomy label="def:holonomy"} Let $D$ be a tangle diagram with an octahedral coloring $\chi$. The is the representation (i.e.functor) $$\Hol{\chi} : \gpoid{D} \to \glg$$ defined by $$\Hol{\chi}(x^{+}_{i}) =
    \upf{\chi_i}
    \text{ and }
    \Hol{\chi}(x^{-}_{i}) =
    \dnf{\chi_i}$$ for each segment $i$ of $D$.
:::

::: lemma
$\Hol{\chi}$ is well-defined.
:::

::: proof
*Proof.* It is elementary (but tedious) to check that whenever the octahedral colors at a crossing are related as in [\[def:octahedral-stuff\]](#def:octahedral-stuff){reference-type="ref" reference="def:octahedral-stuff"} the holonomy matrices satisfy the relations of [\[def:tangle-groupoid\]](#def:tangle-groupoid){reference-type="ref" reference="def:tangle-groupoid"}. ◻
:::

The holonomy representation is related to the one generated by the face maps of the octahedral decomposition, as discussed in [@McPhailSnyder2022 Section 3]. To relate it to representations of $\pi(D)$ we define a functor $\pi(D) \to \Pi(D)$ constructed using a natural family of paths in $\Pi(D)$:

::: definition
[]{#def:shadows label="def:shadows"} Let $D$ be a tangle diagram with topmost region $0$ and let $j$ be a region of $D$. An $s_j^+$ is a path $0 \to j$ that passes over each strand. It is clear it unique up to homotopy.
:::

To write these paths as products of generators, choose a path of adjacent regions from $0$ to $j$. If that path crosses segments $i_1, \dots, i_k$ in that order, then $$\label{eq:shadow-path-rule}
  s_j^+ = \left(x_{i_1}^+\right)^{\epsilon_1} \cdots \left(x_{i_k}^+\right)^{\epsilon_k}$$ where $\epsilon_i = + 1$ if segment $i$ is oriented left-to-right as we cross it from the top and $-1$ otherwise, as in [\[fig:region-orientation-rule\]](#fig:region-orientation-rule){reference-type="ref" reference="fig:region-orientation-rule"}. Independence of [\[eq:shadow-path-rule\]](#eq:shadow-path-rule){reference-type="ref" reference="eq:shadow-path-rule"} from the choice of path follows from [\[eq:groupoid-relation-above,eq:groupoid-relation-below\]](#eq:groupoid-relation-above,eq:groupoid-relation-below){reference-type="ref" reference="eq:groupoid-relation-above,eq:groupoid-relation-below"}.

::: theorem
[]{#thm:functor label="thm:functor"} Let $D$ be a tangle diagram. For each segment $i$ write $\upr{i}$ for the region above $i$ and set $$\mathcal{F}(w_i) \mathrel{:=}s^+_{\upr{i}} \left[x_i^{+} x_i^{-} \right] (s_{\upr{i}}^+)^{-1}$$ where $w_i$ is the Wirtinger generator associated to $i$. Then $\mathcal{F}$ is a well-defined homomorphism (i.e.,functor) $\pi(D) \to \gpoid{D}$.
:::

An example is given in in [1](#fig:path-factorization){reference-type="ref" reference="fig:path-factorization"}.

::: proof
*Proof.* We need to check that $\mathcal{F}$ respects the relations of $\pi(D)$ coming from each crossing. Consider a positive crossing whose topmost region has over path $s^+$ and whose segments are labeled as in [\[fig:crossing-types\]](#fig:crossing-types){reference-type="ref" reference="fig:crossing-types"}. We have $$\mathcal{F}(w_{2'})
     =
     s^+
     x_{2'}^{+}
     \left(x_{2'}^{-}\right)^{-1}
     \left(s^+\right)^{-1}$$ while $$\begin{aligned}
     &
     \mathcal{F}(w_{1}^{-1} w_{2} w_{1})
     \\
     &=
     \left[
     s^+
       x_1^- \left(x_1^+\right)^{-1}
     \left(s^+\right)^{-1}
     \right]
     s^+
     x_{1}^{+}
     x_2^+ \left(x_2^-\right)^{-1}
     \left(s^{+} x_1^{+}\right)^{-1}
     \left[
     s^+
       x_1^+ \left(x_1^-\right)^{-1}
     \left(s^+\right)^{-1}
     \right]
     \\
     &=
     s^+
     x_1^-
     x_2^+ \left(x_2^-\right)^{-1}
     \left(x_1^-\right)^{-1}
     \left(s^+\right)^{-1}
   
\end{aligned}$$ and writing [\[eq:groupoid-relation-thru\]](#eq:groupoid-relation-thru){reference-type="eqref" reference="eq:groupoid-relation-thru"} and [\[eq:groupoid-relation-below\]](#eq:groupoid-relation-below){reference-type="eqref" reference="eq:groupoid-relation-below"} as $$x_{2'}^{+}
     =
     x_1^{-} x_2^{+} \left( x_{1'}^{-}\right)^{-1}
     \text{ and }
     \left(x_{2'}^{-}\right)^{-1}
     =
     x_{1'}^{-}
     \left( x_2^{-} \right)^{-1}
     \left( x_1^{-} \right)^{-1}$$ gives the relation $\mathcal{F}(w_{2'}) = \mathcal{F}(w_1^{-1} w_2 w_1)$. The relation at a negative crossing follows from a similar computation. ◻
:::

<figure id="fig:path-factorization">

<figcaption> This tangle has regions <span class="math inline">0, 1, 2, 3</span> and segments <span class="math inline">1, 2, 3</span>. The over path for region <span class="math inline">$2 = \upr{3}$</span> is <span class="math inline"><em>s</em><sup>+</sup> = <em>x</em><sub>1</sub><sup>+</sup><em>x</em><sub>2</sub><sup>+</sup></span>, so the Wirtinger generator <span class="math inline"><em>w</em><sub>3</sub> ∈ <em>π</em>(<em>D</em>)</span> of segment <span class="math inline">3</span> is mapped to <span class="math inline">$\mathcal{F}(w_3) = s^+ x_3^+ (x_3^-)^{-1} (s^+)^{-1} = x_1^+ x_2^+ x_3^+ \left(x_3^- \right)^{-1} \left(x_2^+\right)^{-1} \left(x_1^+\right)^{-1} \in  \gpoid{D}.$</span> </figcaption>
</figure>

According to the theorem, an octahedral coloring $i \mapsto \chi_i$ has the same holonomy as an $\slg$ representation $\rho$ if for each segment $i$ $$\rho(w_i) = \Hol{\chi}(s_{\upr{i}}^+) \aroundhol{\chi_i} \Hol{\chi}(s_{\upr{i}}^+)^{-1}.$$ Here $\rho(w_i) = g_i$ is the image of the corresponding Wirtinger generator, i.e.the color strand $i$ in the associated $\slg$-coloring. This gives an inductive method for finding $\chi$. For example, consider the tangle in [1](#fig:path-factorization){reference-type="ref" reference="fig:path-factorization"} with segments $1, 2, 3$ and regions $0, 1, 2, 3$. The octahedral color $\chi_1$ of strand $1$ is determined by $$g_1 = \Hol{\chi}(s_0^+) \aroundhol{\chi_1} \Hol{\chi}(s_0^+)^{-1}
  = \aroundhol{\chi_1}$$ as the over path $s_0^+$ for the topmost region is trivial. We can find such a $\chi_1$ whenever $g_1$ lies in the subset $$Y
  =
  \left\{ \def\given{\ \middle| \ }   
    \begin{bmatrix}
      a & -(a-m) b \\
      (a-1/m)/b & m + m^{-1} -a
    \end{bmatrix}
    \given
    a, b, m \in \mathbb{C} \setminus \{0\}
   \right\}  
  \subset \slg$$ of matrices of the form [\[eq:chi-around-hol\]](#eq:chi-around-hol){reference-type="eqref" reference="eq:chi-around-hol"}. Moving down the diagram, $\chi_2$ satisfies $$g_2 = \Hol{\chi}(s_1^+) \aroundhol{\chi_2} \Hol{\chi}(s_1^+)^{-1}
  = \upf{\chi_1} \aroundhol{\chi_2} \upf{\chi_1}^{-1}$$ and again this is possible when $$\upf{\chi_1}^{-1} g_2 \upf{\chi_1} \in Y.$$

More generally this method can be used to inductively find an octahedral coloring agreeing with $\rho$; this leads to the of of @Blanchet2018. However, it is not immediately clear for which $\rho$ this is possible, because the condition that $$\Hol{\chi}(s_{\upr{i}}^+)^{-1} g_i \Hol{\chi}(s_{\upr{i}}^+)
  \in Y$$ requires already determining the earlier colors in the over path $$\Hol{\chi}(s_{\upr{i}}^+) 
  =
  \upf{\chi_{i_1}} \cdots \upf{\chi_{i_k}}.$$

In addition, this definition is asymmetric: the segments adjacent to the top region are treated differently because its over path is always trivial. We can change this by modifying our notion of what it means for $\Hol{\chi}$ to agree with $\rho$. Extend our earlier notation by writing $$\upf{
    \begin{bmatrix}
      u^1 \\ u^2
    \end{bmatrix}
  }
  =
  \begin{bmatrix}
    u^{1} & 0 \\
    u^{2} & 1
  \end{bmatrix}$$ and define $$\hol{\chi, u_0}(w_i) = \upf{u_0} \Hol{\chi}(\mathcal{F}(w_i)) \upf{u_0}^{-1}.$$ This makes sense as long as the first entry of $u_0$ is nonzero, which it is in any admissible shadow coloring. When $u_0 = \evec{1}$ we simply have $\hol{\chi, \evec{1}} = \Hol{\chi} \mathcal{F}$, while the other representations $\hol{\chi, u_0}$ are conjugate by the matrices $\upf{u_0}$. We now rephrase our problem as asking whether $\rho$ agrees with some $\hol{\chi, u_0}$. This does not fundamentally change the problem because we are mostly interested in whether $\rho$ is *conjugate* to the holonomy of an octahedral coloring.

::: bigtheorem
[]{#thm:holonomies-match label="thm:holonomies-match"} Let $D$ be a tangle diagram and $i \mapsto g_i, j \mapsto u_j$ be a decorated shadow $\slg$-coloring of $D$ with $u_0$ the shadow of the topmost region. Let $\chi$ be the associated octahedral coloring of [\[def:associated-octahedral\]](#def:associated-octahedral){reference-type="ref" reference="def:associated-octahedral"}. Then its holonomy agrees with $\rho$ in the sense that $$\hol{\chi, u_0}(w_i) = \rho(w_i)$$ for each Wirtinger generator $w_i$.
:::

We begin with some matrix computations that reduce the proof to showing that the shadow coloring keeps track of the over path holonomies.

::: lemma
[]{#thm:shadow-lemma label="thm:shadow-lemma"} Suppose $$\upf{u} \aroundhol{\chi} \upf{u}^{-1} = g.$$ for an octahedral color $\chi$, a column vector $u \in \mathbb{C}^{2}$, and a matrix $g \in \slg$. Then $$\chi =
    \left(
      \frac{
        \det( g u , \evec{2} )
      }{
        \det( u , \evec{2} )
      }
      ,
      -
      \frac{
        v \evec{2}
      }{
        v u
      }
      ,
      m
    \right)$$ where $v$ is a nonzero *row* vector with $vg = m^{-1} v$.
:::

::: proof
*Proof.* Write $\chi = (a,b, m)$. By [\[eq:chi-around-hol\]](#eq:chi-around-hol){reference-type="ref" reference="eq:chi-around-hol"} we have $$\begin{bmatrix}
      -1 & b
    \end{bmatrix}
    \aroundhol{\chi}
    =
    m^{-1}
    \begin{bmatrix}
      -1 & b
    \end{bmatrix}$$ so $\begin{bmatrix}
      -1 & b
    \end{bmatrix}$ spans the $m^{-1}$-eigenspace of $\aroundhol{\chi}$. (When $m = \pm 1$ it spans the single eigenspace of $\tau{\chi}$.) Since $v$ spans the $m^{-1}$ eigenspace of $g = \upf{u}^{-1} \aroundhol{\chi} \upf{u}$ we conclude that $$\alpha
    \begin{bmatrix}
      -1 & b
    \end{bmatrix}
    =
    v
    \upf{u}
    =
    \begin{bmatrix}
      v u & v \evec{2}
    \end{bmatrix}$$ for some nonzero $\alpha \in \mathbb{C}$, which implies $$b = -
    \frac{
      v \evec{2}
      }{
      v u
    }$$ as claimed. It remains to establish the formula for $a$. Set $$u = \begin{bmatrix}
      u^1 \\ u^2
    \end{bmatrix}.$$ As for any column vector $\det(u, \evec{2}) = u^1 = \evec{1}^{\mathrm{T}} u$. In addition, $\upf{u}^{-1} u =  \evec{1}$ because $\upf{u} = \begin{bmatrix}
      u & \evec{2}
    \end{bmatrix}$ and $\dnf{\chi} \evec{1} = \evec{1}$ because $\dnf{\chi}$ is lower-triangular. We now compute $$\begin{aligned}
    \det(u, \evec{2}) 
    &=
    \evec{1}^{\mathrm{T}}
    g u
    \\
    &=
    \evec{1}^{\mathrm{T}}
    \upf{u} \upf{\chi} \dnf{\chi} \upf{u}^{-1} u 
    \\
    &=
    \evec{1}^{\mathrm{T}}
    \upf{u} \upf{\chi} \dnf{\chi} \evec{1}
    \\
    &=
    \evec{1}^{\mathrm{T}}
    \upf{u} \upf{\chi} \evec{1}
    \\
    &=
    \begin{bmatrix}
      u^1 & 0 
    \end{bmatrix}
    \begin{bmatrix}
      a \\
      (a-1/m)/b
    \end{bmatrix}
    \\
    &= u^1 a.
  
\end{aligned}$$ ◻
:::

::: proof
*Proof of [\[thm:holonomies-match\]](#thm:holonomies-match){reference-type="ref" reference="thm:holonomies-match"}.* Our goal is to show that for each segment $i$, $$\hol{\chi, u_0}(w_i)
    =
    \upf{u_0} \Hol{\chi}(s_{\upr{i}}^+)
    \aroundhol{\chi_i}
    \left( \upf{u_0} \Hol{\chi}(s_{\upr{i}}^+) \right)^{-1}
    =
    g_i.$$ By [\[thm:shadow-lemma\]](#thm:shadow-lemma){reference-type="ref" reference="thm:shadow-lemma"} it is sufficient to check that $$\label{eq:shadows-match-over}
    \upf{u_j} = \upf{u_0} \Hol{\chi}(s_j^+)$$ for each region $j$.

We prove this inductively. For the topmost region $0$, $s_0^+ = 1$ is trivial and [\[eq:shadows-match-over\]](#eq:shadows-match-over){reference-type="ref" reference="eq:shadows-match-over"} is tautological. Below we show that if [\[eq:shadows-match-over\]](#eq:shadows-match-over){reference-type="ref" reference="eq:shadows-match-over"} holds for one region then it holds for all adjacent regions, which establishes the theorem.

Suppose $$\upf{u_j} = \upf{u_0} \Hol{\chi}(s_j^+)$$ for a region $j$ and let $j'$ be adjacent across segment $i$. For notational simplicity we assume $j'$ is below $j$ (as in [\[fig:region-orientation-rule\]](#fig:region-orientation-rule){reference-type="ref" reference="fig:region-orientation-rule"}) but a similar argument works for the other orientation. By definition, $u_{j'} = g_i u_{j}$ so by the inductive hypothesis $$u_{j'}
    =
    \upf{u_j} \aroundhol{\chi_i} \upf{u_j}^{-1} u_{j}.$$ Then as in the proof of [\[thm:shadow-lemma\]](#thm:shadow-lemma){reference-type="ref" reference="thm:shadow-lemma"} $$u_{j'}
    =
    \upf{u_j} \aroundhol{\chi_i} \upf{u_j}^{-1} u_{j}
    =
    \upf{u_j} \upf{\chi_i} \dnf{\chi_i} \evec{1}
    =
    \upf{u_j} \upf{\chi_i} \evec{1}.$$ Now by the inductive hypothesis and the definition of over path $$\upf{u_j} \upf{\chi_i}
    =
    \upf{u_0} \Hol{\chi}(s_j^+) \upf{\chi_i}
    =
    \upf{u_0} \Hol{\chi}(s_{j'}^+)$$ so $$u_{j'}
    =
    \upf{u_0} \Hol{\chi}(s_{j'}^+) \evec{1}$$ and because $\upf{u} \evec{1} = u$ we conclude $\upf{u_{j'}} = \upf{u_0} \Hol{\chi}(s_{j'}^+)$ as claimed. ◻
:::
