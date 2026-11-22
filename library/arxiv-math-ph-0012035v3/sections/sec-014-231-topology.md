---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action"
section_id: sec-014-231-topology
section_title: "Topology"
section_number: 2.3.1
pages: 30-33
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.993
doc_brief: "Non-Abelian Stokes theorem in action — In this short review main issues related to the non-Abelian Stokes theorem have been addressed."
---
Up to now we have investigated the non-Abelian Stokes theorem for topologically trivial situation. The term *topologically trivial situation* means, in this context, that the loop we are integrating along in the non-Abelian Stokes theorem is unknotted in the sense of theory of knots \[Rol76\]. It appears that in contradistinction to the Abelian case, the non-Abelian one is qualitatively different. If the loop $C$ is topologically non-trivial and the bounded surface $S$ ($\partial S=C$) is not simply connected, the parameter space given in the form of a unit square (as in the proof of the non-Abelian Stokes theorem) is not appropriate. The non-Abelian Stokes theorem presented in the original form applies only to a surface $S$ homeomorphic to a disk (square). But still, of course, the standard (topologically trivial) version of the non-Abelian Stokes theorem makes sense locally. What means *locally* will appear clear in the due course. The non-Abelian Stokes theorem for knots (and also for links---multicomponent loops) has been formulated by Hirayama, Kanno, Ueno and Yamokoshi in 1998 \[HKUY98\]. Interestingly, it follows from this new version of the non-Abelian Stokes theorem that the value of the line integral along $C$ can be non-trivial (different from 1 even for the field strenght $F_{\mu\nu}(x)$ vanishing everywhere on the surface $S$. It is an interesting result which could have some applications in physics. One can speculate that it could give rise to a new version of the Aharonov-Bohm effect.

To approach the non-Abelian Stokes theorem for knots we should recall a necessary portion of the standard lore of theory of knots. Since the first task is to find an oriented surface $S$ whose boundary is $C$, we should construct the, so-called, Seifert surface, satisfying the above-mentioned condition by definition. It appears that the Seifert surface for any knot assumes a standard form homeomorphic to a (flat) disk with $2g$ ("thin") strips attached. The number $g$ is called the genus. The strips may, of course, be horribly twisted and intertwined \[Rol76\].

Now we should decompose $C$ and next $S$ into pieces so that one can put from the pieces the slices of that are topologically trivial, and this way they are subject to the standard non-Abelian Stokes theorem. Such decomposition is shown in Fig.[1](#fig:seifert){reference-type="ref" reference="fig:seifert"}. Explicitly, it reads $$\begin{aligned}
    C&=&\left(C_{10(g-1)+9}\ldots C_{11}\right)
    \left(C_9C_7C_4C_1\right)C_0       \nonumber \\
    &=&\left(\prod_{k=0}^{g-1} C_{10k+9} C_{10k+7}
    C_{10k+4}  C_{10k+1} \right) C_0, 
    \qquad {\rm for}\quad g\geq1,
\end{aligned}$$ and $$C=C_0, \qquad {\rm for}\quad g=0.$$ Next $$\begin{aligned}
    C&=&\Big[C_{10(g-1)+6}
    \underbrace{\big(C_{10(g-1)+6}^{-1}
    \hskip-0.7cm\stackrel{\underbrace{C_{10(g-1)+10}^{-1}}}{}
    C_{10(g-1)+9} C_{10(g-1)+8}\big)}_{S_{4g}}
    C_{10(g-1)+3}\nonumber\\
     &&\quad\ldots C_{13} \underbrace{\big(C_{13}^{-1}
    C_{12}^{-1}C_{11}C_{10}\big)}_{S_5}\Big]\cdot
    \Big[
    C_6\underbrace{\big(C_6^{-1} C_{10}^{-1} C_9 C_8 
    \big)}_{S_4}   \nonumber \\
    &&\quad
    C_3^{-1}\underbrace{\big(C_3 C_8^{-1} C_7 C_5 
    \big)}_{S_3}
    C_6^{-1}\underbrace{\big(C_6 C_5^{-1} C_4 C_2 
    \big)}_{S_2}C_3\underbrace{\big(C_3^{-1} C_2^{-1}
    C_1 C_0 \big)}_{S_1}
    \Big]    \nonumber \\
    &=&
    \prod_{k=0}^{g-1} C_{10k+6}\underbrace{
    \big(C_{10k+6}^{-1}\underline{C_{10k+10}^{-1}}  
    C_{10k+9}C_{10k+8}\big)}_{S_{4k+4}}\nonumber\\
    &&\quad
    C_{10k+3}^{-1} \underbrace{\big(C_{10k+3}C_{10k+8}^{-1} 
    C_{10k+7}C_{10k+5}\big)}_{S_{4k+3}}\nonumber\\
    &&\quad
    C_{10k+6}^{-1} \underbrace{\big(C_{10k+6}C_{10k+5}^{-1} 
    C_{10k+4}C_{10k+2}\big)}_{S_{4k+2}}\nonumber\\
    &&\quad
    C_{10k+3} \underbrace{\big(C_{10k+3}^{-1}C_{10k+2}^{-1} 
    C_{10k+1}C_{10k}\big)}_{S_{4k+1}}\nonumber\\
    &=&
    \prod_{k=0}^{g-1}
    C_{10k+6} S_{4k+4}C_{10k+3}^{-1} S_{4k+3}
    C_{10k+6}^{-1} S_{4k+2}C_{10k+3} S_{4k+1},
    \nonumber
        
\end{aligned}$$

<figure id="fig:seifert">
<div class="center">

</div>
<figcaption>Decomposition of the knotted loop <span class="math inline"><em>C</em></span>.</figcaption>
</figure>

where $C_{10k+10}|_{k=g-1}
    \equiv
    C_{10g}=1$.

Further details are described in the original paper \[HKUY98\], and continued in \[BD01\].
