---
doc_id: arxiv-2404.19155v2
doc_title: "Octahedral coordinates from the Wirtinger presentation"
section_id: sec-001-octahedral-colorings
section_title: "Octahedral colorings"
section_number: null
pages: 4-7
source_pdf: 2404.19155v2.pdf
source_sha256: 45b9ed90006536b3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.818
latex_coverage_ratio: 0.925
doc_brief: "Octahedral coordinates from the Wirtinger presentation — Let ρ be a representation of a knot group (or more generally, the funda- mental group of a tangle complement) into SL2(C) expressed in terms"
---
[]{#sec:octahedral-colorings label="sec:octahedral-colorings"}

::: definition
The of a tangle $T$ is its complement as a submanifold of $[0,1]^{3}$. We write $\pi(T)$ for the fundamental group of the complement. Suppose $T$ has $n$ incoming and $m$ outgoing boundary points and let $D$ be a diagram of $T$. We can think of $D$ as a decorated $4$-valent graph $G$ embedded in $[0,1] \times [0,1]$ with $n$ edges intersecting $[0,1] \times \left\{ \def\given{\ \middle| \ }  0 \right\}$ and $m$ edges intersecting $[0,1] \times \left\{ \def\given{\ \middle| \ }  1 \right\}$. We assign names to various parts of $D$:

-   The of $D$ are the edges of $G$.

-   An of $D$ is a set of adjacent over-segments.

-   A of $D$ is a set of adjacent segments; these are in bijection with connected components of $T$.

-   A of $D$ is a connected component of the complement of $G$, equivalently a vertex of the dual graph of $G$. Regions are adjacent across segments, and our convention is to say that region $j'$ is region $j$ when they are arranged as in [\[fig:region-orientation-rule\]](#fig:region-orientation-rule){reference-type="ref" reference="fig:region-orientation-rule"}. In this case we call $j$ the region $i$ and write $j = \upr i$. Similarly $j'$ is the region $i$, written $j = \dnr i$.
:::

::: marginfigure
:::

::: proposition
[]{#thm:wirtinger label="thm:wirtinger"} Let $D$ be a diagram of a tangle $T$. The choice of $D$ gives a presentation for $\pi(T)$ with one generator $w_i$ for each arc and one relation $$\begin{gathered}
    \label{eq:wirtinger-positive}
    w_{2'} = w_{1}^{-1} w_{2} w_{1} \text{ (positive)}
    \\
    \label{eq:wirtinger-negative}
    w_{1'} = w_{2} w_{1} w_{2}^{-1} \text{ (negative)}
  
\end{gathered}$$ at each crossing, where the indices are as in [\[fig:crossing-types\]](#fig:crossing-types){reference-type="ref" reference="fig:crossing-types"}. (At a positive crossing $1$ and $1'$ are the same arc.) We call this the of $\pi(T)$ and denote it by $\pi(D)$. If $i$ is a segment of $D$ we write $w_{i}$ for the associated Wirtinger generator.
:::

::: definition
Let $D$ be a diagram of a tangle $T$ and $G$ be a group. A of $D$ is a function $i \mapsto g_i$ assigning each segment an element of $g$, subject to the Wirtinger relations [\[eq:wirtinger-positive\]](#eq:wirtinger-positive){reference-type="eqref" reference="eq:wirtinger-positive"} and [\[eq:wirtinger-negative\]](#eq:wirtinger-negative){reference-type="eqref" reference="eq:wirtinger-negative"} at each crossing.
:::

By [\[thm:wirtinger\]](#thm:wirtinger){reference-type="ref" reference="thm:wirtinger"} $G$-colorings of $D$ are in bijection with representations $\rho : \pi(D) \to G$.

It turns out that octahedral coordinates correspond to slightly more data: they describe both a representation of $\pi(T)$ and some extra data on the boundary of a regular neighborhood of $T$.

<figure id="fig:decorated-quandle-rule">

<figcaption>Rules for decorated <span class="math inline">$\slg$</span> colorings.</figcaption>
</figure>

::: definition
A $\rho$ of a tangle $T$ is a representation $\rho : \pi(T) \to \slg$ with a choice of invariant line for each meridian of $T$.

More formally, each component $i$ of the oriented tangle has a conjugacy class of meridians $[w_i] \subset \pi(T)$. For a representative $w_i$ we choose a line $L_i \subset \mathbb{C}^2$ (thought of as a set of *row* vectors) with $$L_i \rho(w_i) = L_i.$$ This does not depend on the choice of representative: if $w_i' = y^{-1} w_i y$ is any other representative of the conjugacy class we assign it the line $L_i \rho(y)$, since $$L_i \rho(y) \rho(y^{-1} w_i y) = L_i \rho(y).$$ This choice is called a of component $i$, and a decoration of $\rho$ is a decoration of each of its components. A decoration of $\rho$ induces an equivalent decoration of any conjugate $g^{-1} \rho g$ in a similar way.
:::

Generically a knot has two decorations, as a diagonalizable matrix has two eigenspaces. When $\mathop{\mathrm{tr}}\rho(w) = \pm 2$ but $\rho \ne \pm 1$ is nontrivial (i.e. when $\rho$ is boundary-parabolic) there is only one decoration, and when $\rho(w) = \pm 1$ is trivial there are infinitely many. Similar statements apply to links and tangles.

::: definition
A assigns each segment $i$ a group element $g_i \in \slg$ and a $1$-dimensional subspace $L_i \subset \mathbb{C}^{2}$ invariant under $g_i$, subject to the rule that $$\begin{gathered}
    \label{eq:decorated-positive}
    L_{2'} = L_2 g_1  \text{ (positive)}
    \\
    \label{eq:decorated-negative}
    L_{1'} = L_{1} g_{2} \text{ (negative)}
  
\end{gathered}$$ These are summarized in [1](#fig:decorated-quandle-rule){reference-type="ref" reference="fig:decorated-quandle-rule"}.
:::

In our example we cannot multiply two segment colors because $(g, L)$ and $(h, L')$ do not determine an eigenspace of $gh$, but we can conjugate them. As such the set of pairs $(g, L)$ with the binary operation $$(g, L) \triangleleft (h, L') = (h^{-1} g h, L h)$$ form an algebraic structure $\mathcal{Q}$ called a . Quandles generalize the conjugation structure of a group and appear in many places in knot theory. Decorated $\slg$-colorings can be characterized as determining homomorphism from the fundamental quandle of the tangle to $\mathcal{Q}$.

::: proposition
Decorated representations $\rho : \pi(D) \to \slg$ are in bijection with decorated $\slg$-colorings of $D$.
:::

Because $\slg$ is the double cover of the isometry group $\pslg$ of hyperbolic space a choice of $\rho : \pi(T) \to \slg$ determines a (generalized) hyperbolic structure on the tangle complement. However, this description is rather abstract, and frequently one wants to instead describe the hyperbolic structure by gluing together geometric ideal tetrahedra. Any tangle diagram determines an [@Kim2016; @McPhailSnyder2022] of its complement in a standard way, which gives the topological data of the gluing. The geometric information is determined by complex numbers called shape parameters, which are in turn determined by an octahedral coloring of the digram as defined below. We discuss the shape parameters further in [\[sec:potential\]](#sec:potential){reference-type="ref" reference="sec:potential"}.

::: definition
[]{#def:octahedral-stuff label="def:octahedral-stuff"} An is a triple $\chi = (a, b, m) \in (\mathbb{C} \setminus \left\{ \def\given{\ \middle| \ }  0 \right\}   )^3$ of nonzero complex numbers. When we work with an indexed set $\left\{ \def\given{\ \middle| \ }  \chi_{i} \right\}  _{i \in I}$ of colors we typically write $a_i, b_i, m_i$ for their components. An of a tangle diagram $D$ is an assignment $i \mapsto \chi_i = (a_i, b_i, m_i)$ of an octahedral color to every segment $i$ so that at every positive crossing $$\begin{gathered}
    \label{eq:a-transf-positive}
    \begin{aligned}
      a_{1'}
      &=
      a_1 A^{-1}
      \\
      a_{2'}
      &=
      a_2 A \text{ where}
      \\
      A &= 1 - \frac{m_1 b_1}{b_2} \left(1 - \frac{a_1}{m_1}\right)\left(1 - \frac{1}{m_2 a_2}\right)
    \end{aligned}
    \\
    \label{eq:b-transf-positive}
    \begin{aligned}
      b_{1'}
      &=
      \frac{m_2 b_2}{m_1}
      \left(
        1 - m_2 a_2 \left( 1 - \frac{b_2}{m_1 b_1} \right)
      \right)^{-1}
      \\
      b_{2'}
      &=
      b_1
      \left(
        1 - \frac{m_1}{a_1}\left( 1 - \frac{b_2}{m_1 b_1} \right)
      \right)
    \end{aligned}
    \\
    \label{eq:m-transf-positive}
    \begin{aligned}
      m_{1'}
      &= m_1
      &
      m_{2'}
      &= m_2
    \end{aligned}
  
\end{gathered}$$ and at every negative crossing $$\begin{gathered}
    \label{eq:a-transf-negative}
    \begin{aligned}
      a_{1'}
      &=
      a_1 \tilde A^{-1} 
      \\
      a_{2'}
      &=
      a_2 \tilde A \text{ where}
      \\
      \tilde A 
      &=
      1 - \frac{b_2}{m_1 b_1}\left(1 - m_1 a_1 \right)\left(1 - \frac{m_2}{a_2}\right).
    \end{aligned}
    \\
    \label{eq:b-transf-negative}
    \begin{aligned}
      b_{1'}
      &=
      \frac{m_2 b_2}{m_1}
      \left(
        1 - \frac{a_2}{m_2} \left( 1 - \frac{m_1 b_1}{b_2} \right)
      \right)
      \\
      b_{2'}
      &=
      b_1
      \left(
        1 - \frac{1}{m_1 a_1} \left( 1 - \frac{m_1 b_1}{b_2} \right)
      \right)^{-1}
    \end{aligned}
    \\
    \label{eq:m-transf-negative}
    \begin{aligned}
      m_{1'}
      &= m_1
      &
      m_{2'}
      &= m_2
    \end{aligned}
  
\end{gathered}$$
:::

Our goal is to obtain an octahedral coloring from a decorated $\slg$-coloring. The relevant geometry of the ideal tetrahedra is most naturally described in terms of the face-pairing maps of the triangulation. These define a representation of a fundamental *groupoid* with one basepoint for each tetrahedron. This groupoid is closely related (but not quite the same as) the fundamental groupoid studied in [\[sec:holonomy\]](#sec:holonomy){reference-type="ref" reference="sec:holonomy"}. In contrast, the Wirtinger generators are global and have a single common basepoint. To relate these to the fundamental groupoid we need to keep track of change-of-basepoint data using additional colors called shadows.

::: definition
Let $i \mapsto g_i$ be a $\slg$-coloring of a tangle diagram $D$ (possibly decorated). A of $(D,g)$ is an assignment $j \mapsto u_j$ of nonzero column vectors in $\mathbb{C}^{2}$ to each region, subject to the rule $$u_{j'} = g_i u_j$$ when $j'$ is below $j$ across $i$ as in [\[fig:region-orientation-rule\]](#fig:region-orientation-rule){reference-type="ref" reference="fig:region-orientation-rule"}.
:::

::: lemma
[]{#thm:shadow-colors-free label="thm:shadow-colors-free"} For a fixed $\slg$-coloring the space of shadow colorings is nonempty and in bijection with $\mathbb{C}^2 \setminus \left\{ \def\given{\ \middle| \ }  0 \right\}$.
:::

::: marginfigure
:::

::: proof
*Proof.* To see that shadow colorings exist it is enough to check that the rules are consistent around each crossing. For a positive crossing (shown in [\[fig:shadow-rule-around\]](#fig:shadow-rule-around){reference-type="ref" reference="fig:shadow-rule-around"}) this is because $g_2 g_1 = g_1 (g_1^{-1} g_2 g_1)$, and negative crossings are similar.

Once the color $u_j$ of a single region $j$ is chosen the rules determine a unique color for every other region, so the space of shadow colorings is parametrized by $u_j \in \mathbb{C}^{2} \setminus \left\{ \def\given{\ \middle| \ }  0 \right\}$. ◻
:::

::: definition
[]{#def:associated-octahedral label="def:associated-octahedral"} Consider a $\slg$-shadow-colored digram $(D, g, u)$. For each segment $i$, let $v_i$ be a nonzero element of $L_i$; our definition is independent of this choice. Let $m_i$ be the *inverse* eigenvalue of $g_i$ on $v_i$: $$v_i g_i = m_{i}^{-1} v_{i}.$$ We say $(D, g, u)$ is if $$\begin{gathered}
    \det( u_{j}, \evec{2} ) \ne 0 \text{ for each region \(j\), and}
    \\
    v_i \evec{2}, v_i u_{\upr{i}} \ne 0 \text{ for each segment \(i\).}
  
\end{gathered}$$ In this case we can assign segment $i$ below region $\upr{i}$ and above region $\dnr{i}$ the octahedral color $$\label{eq:chi-formula}
    \chi_i =
    \left(
      \frac{
        \det( u_{\dnr{i}} , \evec{2} )
        }{
        \det( u_{\upr{i}} , \evec{2} )
      }
      ,
      -
      \frac{
        v_i \evec{2}
      }{
        v_i u_{\upr{i}}
      }
      ,
      m_i
    \right)$$ and we call this the octahedral coloring to $(D, g, u)$.
:::

::: theorem
The coloring $i \mapsto \chi_i$ defined by [\[eq:chi-formula\]](#eq:chi-formula){reference-type="eqref" reference="eq:chi-formula"} is an octahedral coloring: it satisfies the conditions of [\[def:octahedral-stuff\]](#def:octahedral-stuff){reference-type="ref" reference="def:octahedral-stuff"}.
:::

::: proof
*Proof.* We can parametrize the space of all $\slg$ decorated shadow colorings of a crossing by the coordinates of $g_1, g_2, L_1, L_2, u$ (in the notation of [1](#fig:decorated-quandle-rule){reference-type="ref" reference="fig:decorated-quandle-rule"}), say by using homogeneous coordinates for $L_1, L_2 \in \psp$. The components $a_i, b_i, m_i$ of the associated octahedral coloring are rational functions in these. One can check that these rational functions agree with [\[eq:a-transf-positive,eq:b-transf-positive,eq:m-transf-positive\]](#eq:a-transf-positive,eq:b-transf-positive,eq:m-transf-positive){reference-type="ref" reference="eq:a-transf-positive,eq:b-transf-positive,eq:m-transf-positive"}, and similarly [\[eq:a-transf-negative,eq:b-transf-negative,eq:b-transf-negative\]](#eq:a-transf-negative,eq:b-transf-negative,eq:b-transf-negative){reference-type="ref" reference="eq:a-transf-negative,eq:b-transf-negative,eq:b-transf-negative"} for a negative crossings. ◻
:::

Our proof is algebraic and not very enlightening. What we really want to know is that the holonomy of the octahedral coloring coming from the decomposition into geometric ideal tetrahedra agrees with the representation $\rho$, which is [\[thm:holonomies-match\]](#thm:holonomies-match){reference-type="ref" reference="thm:holonomies-match"} of [\[sec:holonomy\]](#sec:holonomy){reference-type="ref" reference="sec:holonomy"}.
