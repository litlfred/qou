---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-035-113-the-ptolemy-variety-ept-and-the-a-polynomial
section_title: "The Ptolemy variety EP(T) and the A-polynomial"
section_number: 11.3
pages: 24-25
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
toc_source: outline
text_source: latex
latex_prose_ratio: 0.846
latex_coverage_ratio: 0.947
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety for SL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
[]{#sec:Apolyexample label="sec:Apolyexample"} A fundamental rectangle for the boundary of $M$ is shown in Figure [1](#fig:FundamentalRectangle){reference-type="ref" reference="fig:FundamentalRectangle"}. Using the rules illustrated in Figure [\[fig:FundRectIdentifications\]](#fig:FundRectIdentifications){reference-type="ref" reference="fig:FundRectIdentifications"} we obtain that the identification relations are given by

<figure id="fig:FundamentalRectangle">

<figcaption>Fundamental rectangle for <code>m009</code>.</figcaption>
</figure>

$$\begin{gathered}
c_{23,0}\overset{t_2}{=}-m^2c_{23,2}\overset{c}{=}-m^2c_{01,1}\overset{d}{=}m^2c_{01,2}\overset{b}{=}-mc_{01,0}\overset{a}{=}-c_{23,1},\\
c_{13,0}\overset{t_1}{=}c_{12,1}\overset{c}{=}-c_{13,2}\overset{d}{=}-c_{03,1},\\
c_{13,1}\overset{d}{=}c_{03,2}\overset{t_2}{=}m^{-1}lc_{02,0}\overset{b}{=}m^{-1}lc_{12,2}\overset{c}{=}-m^{-1}lc_{02,1}\overset{a}{=}lc_{03,0}\overset{t_2}{=}mc_{02,2}\overset{b}{=}c_{12,0},
\end{gathered}$$ where the symbol $\overset{\alpha}{=}$ indicates that the identification is via the face pairing $\alpha$. Hence, the Ptolemy relations become $$\label{eq:ExmlPtolemy}
mz^2-lx^2-m^2yz,\qquad m^2ly^2-lx^2-m^3z^2,\qquad m^5z^2-lx^2+m^3lyz.$$ One easily checks that there are no non-trivial solutions with $x=0$. The edge relation [\[eq:EdgeEquationsEnhanced\]](#eq:EdgeEquationsEnhanced){reference-type="eqref" reference="eq:EdgeEquationsEnhanced"} around edge 2 is $$\frac{ml^{-1}z}{-m^{-1}xz}+\frac{y}{(-z)m^{-2}x}+\frac{-m^{-1}z}{-m^{-2}x(-z)}+\frac{y}{zx}=0\iff m^2z+m^2ly+mlz-ly=0$$ Adding this equation to the Ptolemy relations [\[eq:ExmlPtolemy\]](#eq:ExmlPtolemy){reference-type="eqref" reference="eq:ExmlPtolemy"} and substituting $z=1$, one can check (using magma [@Magma]) that the system is equivalent to $$\begin{gathered}
        x^2 + yl - m^8 + 3m^6 + m^5l + m^4 - m^3l - 3m^2 - ml=0,\\
        y^2l + yl^2 + m^4l - m^3 - m^2l - ml^2 - m - l=0,\\
        ym + yl + m^4 - m^2 - ml - 1=0,\\
        yl^3 - yl - m^5l + m^4l^2 + m^3l + m^2 - ml^3 + 2ml - l^2=0,\\
        m^6l - 2m^4l - m^3l^2 - m^3 - 2m^2l + l=0.
\end{gathered}$$ This shows that the $A$-polynomial of `m009` is given by $$A(m,l)=m^6l - 2m^4l - m^3l^2 - m^3 - 2m^2l + l.$$ It also follows that $\mathcal E\overline P(\mathcal T)$ is a branched cover over the $A$-polynomial curve of degree 2. Another magma computation shows that it is given explicitly by $$\label{eq:EPOverA}
x^2=-\frac{-m^4-2m^3l+ml}{l^2(m^2-1)},\qquad y=-\frac{m^2+ml}{m^2l - l},\qquad z=1,\qquad A(m,l)=0.$$ Note that $y$ and $x^2$ are regular functions on the $A$-polymial curve.
