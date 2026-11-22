---
doc_id: arxiv-2404.19155v2
doc_title: "Octahedral coordinates from the Wirtinger presentation"
section_id: sec-003-gauge-transformations
section_title: "Gauge transformations"
section_number: null
pages: 13-14
source_pdf: 2404.19155v2.pdf
source_sha256: 45b9ed90006536b3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.655
latex_coverage_ratio: 0.936
doc_brief: "Octahedral coordinates from the Wirtinger presentation — Let ρ be a representation of a knot group (or more generally, the funda- mental group of a tangle complement) into SL2(C) expressed in terms"
---
[]{#sec:gauge-transformations label="sec:gauge-transformations"}

In this section we discuss how gauge transformation (conjugation) of the representation $\rho$ interacts with the decorations and shadows. In this context it is natural to break gauge transformations into two separate types. We then use gauge transformations to prove that every decorated representation is gauge-equivalent to an admissible one (i.e.one that is the holonomy of an octahedral coloring).

::: definition
Let $i \mapsto (g_i, L_i)$, $j \mapsto u_j$ be a decorated shadow $\slg$ coloring of a tangle diagram $D$. A of it is a coloring of the form

-   $i \mapsto (h^{-1} g_i h, L_i h)$ and $j \mapsto g^{-1} u_j$

-   $i \mapsto (g_i, L_i)$ and $j \mapsto h^{-1} u_j$

for some $h \in \slg$. We say the new colorings are the images of and gauge transformations .
:::

It is not hard to see that the gauge transformation of a coloring is still a coloring and that the corresponding representation $\rho : \pi(D) \to \slg$ is conjugated under a type (A) transformation and unchanged under type (B). We can use type (B) transformations to choose the shadow of a single region arbitrarily as in [\[thm:shadow-colors-free\]](#thm:shadow-colors-free){reference-type="ref" reference="thm:shadow-colors-free"}.

<figure id="fig:gauge-transformation">

<figcaption> Graphical description of gauge transformations. The thick strands represent bundles of incoming and outgoing segments (possibly empty) with arbitrary colorings. </figcaption>
</figure>

The letters A and B are chosen because a type (A) transformation comes from pulling a strand colored by $h$ across and **A**bove the diagram, while for type (B) we pull across and **B**elow. Both are shown in [1](#fig:gauge-transformation){reference-type="ref" reference="fig:gauge-transformation"}. These are quite similar to the diagrammatic gauge transformations of @Blanchet2018 [Section 3.3]. Combinatorially they come from Reidemeister moves for shadow colored diagrams.

Let $i \mapsto \chi_i$ be the octahedral coloring associated to a shadow coloring. We can immediately compute that under a type (A) transformation by $h$ the new associated coloring is $$\label{eq:type-A-gauge}
  i \mapsto
  \tilde{\chi}_i
  =
  \left(
    \frac{
      \det( h^{-1} u_{\dnr{i}} , \evec{2} )
    }{
      \det( h^{-1} u_{\upr{i}} , \evec{2} )
    }
    ,
    -
    \frac{
      v_i h \evec{2}
    }{
      v_i h h^{-1} u_j
    }
    ,
    m_i
  \right)
  =
  \left(
    \frac{
      \det( u_{\dnr{i}} , h \evec{2} )
    }{
      \det( u_{\upr{i}} , h \evec{2} )
    }
    ,
    -
    \frac{
      v_i h \evec{2}
    }{
      v_i u_{\upr{i}}
    }
    ,
    m_i
  \right)$$ while under type (B) it is $$\label{eq:type-B-gauge}
  i \mapsto
  \tilde{\chi}_i
  =
  \left(
    \frac{
      \det( h^{-1} u_{\dnr{i}} , \evec{2} )
    }{
      \det( h^{-1} u_{\upr{i}} , \evec{2} )
    }
    ,
    -
    \frac{
      v_i \evec{2}
    }{
      v_i  h^{-1} u_j 
    }
    ,
    m_i
  \right)
  =
  \left(
    \frac{
      \det( u_{\dnr{i}} , h \evec{2} )
    }{
      \det( u_{\upr{i}} , h \evec{2} )
    }
    ,
    -
    \frac{
      v_i \evec{2}
    }{
      v_i  h^{-1} u_{\upr{i}}
    }
    ,
    m_i
  \right)$$

::: bigtheorem
[]{#thm:gauge-equivalent-to-admissible label="thm:gauge-equivalent-to-admissible"} Let $D$ be any tangle diagram and $\rho : \pi(D) \to \slg$ any decorated representation. Then $\rho$ is gauge-equivalent to an admissible representation, in the sense that there is a conjugate $h^{-1} \rho h$ of $\rho$ that gives an admissible decorated shadow coloring of $D$.
:::

Another way to state this theorem is to consider the holonomy as a map from the space of octahedral colorings of $D$ to the space of decorated $\slg$ representations of $D$. This map is not surjective because there are inadmissible shadow colorings, but it is surjective up to gauge in the sense that the image intersects the orbit of any $\rho$.

::: proof
*Proof.* Fix a shadow coloring $i \mapsto (g_i, v_i), j \mapsto u_j$ of $D$. We need to show that some gauge transformation of it is admissible. The coloring obtained by applying a type (A) gauge transformation by $A$ then a type (B) by $B^{-1}$ is admissible when $$\det(B u_j , A \evec{2} ), v_i A \evec{2}, v_i B u_{i^{\uparrow}} \ne 0$$ for every region $j$ and segment $i$, where as usual the $v_i$ are representatives of the eigenspaces $L_i$. Thinking of the $u_j$ and $v_i$ as fixed we need to show that there are $A, B \in \slg$ for which this condition holds.

$V = \slg \times \slg$ is an algebraic set in $\mathbb{C}^{8}$. For each region $j$ write $$X_1(j) = \left\{ \def\given{\ \middle| \ }  (A,B) \in V | \det(A u_j , B \evec{2}) = 0  \right\}$$ and for each segment $i$ write $$\begin{gathered}
      X_2(i) = \left\{ \def\given{\ \middle| \ }  (A,B) \in V | v_i A \evec{2} = 0  \right\}  
    \\
    X_3(i) = \left\{ \def\given{\ \middle| \ }  (A,B) \in V | v_i B u_{i^{\uparrow}} = 0  \right\}  
    .
    \end{gathered}$$ These are all Zariki closed proper subsets of $V$. Our goal is to prove that the union $$X =
    \bigcup_{\text{regions } j} X_1(j)
    \cup
    \bigcup_{\text{segments } i} X_2(i) \cup X_3(i)$$ is not all of $\slg \times \slg$, or equivalently that $$V \setminus X = 
    \bigcap_{\text{regions } j} U_1(j)
    \cap
    \bigcap_{\text{segments } i} U_2(i) \cap U_3(i)$$ is nonempty, where $U_l(k) = V \setminus X_l(k)$. Each complement $U_l(k)$ is Zariski open and dense. A finite intersection of such sets is also Zariski open and dense, and in particular is nonempty. ◻
:::
