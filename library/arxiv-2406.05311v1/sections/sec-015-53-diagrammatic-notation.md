---
doc_id: arxiv-2406.05311v1
doc_title: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD"
section_id: sec-015-53-diagrammatic-notation
section_title: "Diagrammatic notation"
section_number: 5.3
pages: 19-20
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
toc_source: outline
text_source: latex
latex_prose_ratio: 0.912
latex_coverage_ratio: 0.948
doc_brief: "A quantum Murnaghan–Nakayama rule for the flag manifold — In this paper, we give a rule for the multiplication of a Schubert class by a tautological class in the (small) quantum cohomology ring of"
---
[]{#SS:diagrammatic-notation label="SS:diagrammatic-notation"} We introduce a diagrammatic notation for compositions of operators ${\mathbf v}_{ab}$, which will facilitate our study of relations among them. Figure [1](#fig:classical-relations){reference-type="ref" reference="fig:classical-relations"} depicts the relations among classical operators in [\[Eq:monoid-relations\]](#Eq:monoid-relations){reference-type="eqref" reference="Eq:monoid-relations"} using this notation. Depict a classical operator ${\mathbf v}_{ab}$ with $a<b$ by a green line segment $[a,b]$ and a quantum operator ${\mathbf v}_{ab}$ with $a>b$ by a dotted red line segment $[b,a]$, drawn in a window with the positions of $1,\dotsc,n$ indicated by vertical dashed lines as follows,

$$\begin{array}{c@{\qquad}c@{\qquad}c}
    \begin{picture}(62,2)
   \put(0 ,-4){{\small 1}}\put(11.5,-4){{\small 2}}
   \put(23,-4){{\small 3}}\put(34.5,-4){{\small 4}}
   \put(46,-4){{\small 5}}\put(57.5,-4){{\small 6}}\end{picture}& \begin{picture}(62,2)
   \put(0 ,-4){{\small 1}}\put(11.5,-4){{\small 2}}
   \put(23,-4){{\small 3}}\put(34.5,-4){{\small 4}}
   \put(46,-4){{\small 5}}\put(57.5,-4){{\small 6}}\end{picture}& \begin{picture}(62,2)
   \put(0 ,-4){{\small 1}}\put(11.5,-4){{\small 2}}
   \put(23,-4){{\small 3}}\put(34.5,-4){{\small 4}}
   \put(46,-4){{\small 5}}\put(57.5,-4){{\small 6}}\end{picture}\\
    \valuediagram[padding=1, xmin=1, xmax=6]{{2,4}}
    &
    \valuediagram[padding=1, xmin=1, xmax=6]{{1,5}}
    &
    \valuediagram[padding=1, xmin=1, xmax=6]{{6,3}}
    \\[1ex]
    {\mathbf v}_{24} & {\mathbf v}_{15} & {\mathbf v}_{63}
\end{array}\ .$$ A composition of operators is depicted by stacking intervals. For example,

$$\begin{array}{c@{\qquad}c}
    \raisebox{-1pt}{\begin{picture}(85,2)
   \put(0 ,-4){{\small 1}}\put(11.5,-4){{\small 2}}
   \put(23,-4){{\small 3}}\put(34.5,-4){{\small 4}}
   \put(46,-4){{\small 5}}\put(57.5,-4){{\small 6}}
   \put(69,-4){{\small 7}}\put(80.5,-4){{\small 8}}\end{picture}} & \raisebox{2pt}{\begin{picture}(85,2)
   \put(0 ,-4){{\small 1}}\put(11.5,-4){{\small 2}}
   \put(23,-4){{\small 3}}\put(34.5,-4){{\small 4}}
   \put(46,-4){{\small 5}}\put(57.5,-4){{\small 6}}
   \put(69,-4){{\small 7}}\put(80.5,-4){{\small 8}}\end{picture}} \\
     \valuediagram[height=2, padding=1]{{1,2},{4,2},{6,8}}
    &
     \valuediagram[padding=1]{{1,4},{8,4},{5,7},{4,2}}
     \\[1ex]
    {\mathbf v}_{68}{\mathbf v}_{42}{\mathbf v}_{12} & {\mathbf v}_{42}{\mathbf v}_{57}{\mathbf v}_{84}{\mathbf v}_{14}
  \end{array}\ .$$ Since the operators act on the left, a composition acts by the rightmost operator first, which corresponds to reading the associated diagram from the bottom to the top.

::: remark
[]{#Rem:relative-labels label="Rem:relative-labels"} We may omit labeling the vertical dashed lines and dashed lines not in the support. For instance, the diagram $\valuediagram[height=.9, padding=.5]{{2,3},{3,1}}$ represents any composition of the form ${{\mathbf v}}_{ca} {{\mathbf v}}_{bc}$ with $a<b<c$.

One reason is that equivalence among classical operators, [\[Eq:monoid-relations\]](#Eq:monoid-relations){reference-type="eqref" reference="Eq:monoid-relations"} and Proposition [\[Prop:monoid\]](#Prop:monoid){reference-type="ref" reference="Prop:monoid"}, only depends upon the relative order of the indices. The other reason is that we are primarily concerned with equivalence to ${\mathbf 0}$ and $(u,k)$-equivalence for minimal operators. By Theorem [\[Th:shape-equivalence\]](#Th:shape-equivalence){reference-type="ref" reference="Th:shape-equivalence"}, these equivalences only depend upon the relative order of the indices. $\diamond$
:::

<figure id="fig:classical-relations">
<p><span class="math display">$$\begin{gathered}
        \begin{array}{rc@{\hskip3pt}c@{\hskip3pt}c@{\hskip3em}c@{\hskip3pt}c@{\hskip3pt}c}
            
            &amp; \valuediagram[scale=1.25]{{1,2},{3,4}}
            &amp; \stackrel{(i)}{\equiv}
            &amp; \valuediagram[scale=1.25]{{3,4},{1,2}}
            &amp; \valuediagram[scale=1.25]{{1,4},{2,3}}
            &amp; \stackrel{(i)}{\equiv}
            &amp; \valuediagram[scale=1.25]{{2,3},{1,4}}
        \end{array}
        \\[1ex]
        \begin{array}{rc@{\hskip3pt}c@{\hskip3pt}c@{\hskip3pt}c@{\hskip3pt}c@{\hskip3pt}c@{\hskip3pt}c@{\hskip3pt}c@{\hskip3pt}c@{\hskip3pt}c@{\hskip3pt}c@{\hskip3pt}c@{\hskip3pt}c@{\hskip3pt}c@{\hskip3pt}c}
            
            &amp; \valuediagram[scale=1.25]{{1,2},{1,2}}
            &amp; \stackrel{(ii)}{\equiv}
            &amp; \valuediagram[scale=1.25]{{1,2},{1,3}}
            &amp; \stackrel{(ii)}{\equiv}
            &amp; \valuediagram[scale=1.25]{{1,3},{1,2}}
            &amp; \stackrel{(ii)}{\equiv}
            &amp; \valuediagram[scale=1.25]{{1,3},{2,4}}
            &amp; \stackrel{(ii)}{\equiv}
            &amp; \valuediagram[scale=1.25]{{2,4},{1,3}}
            &amp; \stackrel{(ii)}{\equiv}
            &amp; \valuediagram[scale=1.25]{{1,3},{2,3}}
            &amp; \stackrel{(ii)}{\equiv}
            &amp; \valuediagram[scale=1.25]{{2,3},{1,3}}
            &amp; \stackrel{(ii)}{\equiv}
            &amp; {\mathbf 0}
        \end{array}
        \\[2ex]
        \begin{array}{rc@{\hskip3pt}c@{\hskip3pt}c@{\hskip2em}c@{\hskip3pt}c@{\hskip3pt}c@{\hskip2em}c@{\hskip3pt}c@{\hskip3pt}c@{\hskip3pt}c@{\hskip3pt}c}
            
            &amp; \valuediagram[scale=1.25]{{2,3},{3,4},{1,3}}
            &amp; \stackrel{(iii)}{\equiv}
            &amp; \valuediagram[scale=1.25]{{2,4},{1,2},{2,3}}
            
            &amp; \valuediagram[scale=1.25]{{1,3},{3,4},{2,3}}
            &amp; \stackrel{(iv)}{\equiv}
            &amp; \valuediagram[scale=1.25]{{2,3},{1,2},{2,4}}
            
            &amp; \valuediagram[scale=1.25]{{2,3},{1,2},{2,3}}
            &amp; \stackrel{(v)}{\equiv}
            &amp; \valuediagram[scale=1.25]{{1,2},{2,3},{1,2}}
            &amp; \stackrel{(v)}{\equiv}
            &amp; {\mathbf 0}
        \end{array}
    
\end{gathered}$$</span></p>
<figcaption>Diagrammatic notation for the relations <a href="#Eq:monoid-relations" data-reference-type="eqref" data-reference="Eq:monoid-relations">[Eq:monoid-relations]</a> among classical operators.</figcaption>
</figure>
