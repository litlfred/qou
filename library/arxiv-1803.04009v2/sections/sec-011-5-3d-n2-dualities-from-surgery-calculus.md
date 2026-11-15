---
doc_id: arxiv-1803.04009v2
doc_title: "Symmetry enhancement and closing of knots in 3d/3d correspondence"
section_id: sec-011-5-3d-n2-dualities-from-surgery-calculus
section_title: "3d N=2 Dualities from Surgery calculus"
section_number: 5
pages: 43-44
source_pdf: 1803.04009v2.pdf
source_sha256: 8b34299b739cd2b0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.972
doc_brief: "Symmetry enhancement and closing of knots in 3d/3d correspondence — We revisit Dimofte-Gaiotto-Gukov’s construction of 3d gauge theories asso- ciated to 3-manifolds with a torus boundary."
---
[]{#sec: Duality/Surgery label="sec: Duality/Surgery"}

The DGG's construction is based on an ideal triangulation of a knot complement $N$. Different ideal triangulations give different field theory descriptions of $T^{DGG}[N]$ theory related by a duality. In our construction $T^{6d}_{\rm irred}[M]$ for a closed 3-manifold $M$, we use a Dehn filling description of the closed 3-manifold, $M=N_A$, with a hyperbolic knot complement $N$ and a primitive boundary cycle $A$. The construction can be straightforwardly generalized to the case when $M$ can be given by Dehn fillings on a link complement. According to the Lickorish-Wallace theorem [@Lickorish][@Wallace], every closed orientable 3-manifold $M$ can be obtained by performing Dehn surgery along a link $L$ in $S^3$.

$$\begin{aligned}
\begin{split}
M &= (S^3\backslash L)_{p_1 \mu_1 +q_1\lambda_1, p_2 \mu_2 +q_2\lambda_2,\ldots, p_l \mu_l +q_l\lambda_l}\;, \quad \textrm{$l=|L|$ : $\sharp$ of components of a  link $L$}\;.
\end{split}
\end{aligned}$$

The Dehn surgery representation is not unique and there are different choices of $(L,\{p_i,q_i\})$ and $(L',\{p_i',q_i'\})$ which give a same closed 3-manifold. Different Dehn surgery presentations of $M$ give different gauge theory descriptions of $T^{6d}_{\rm irred}[M]$ related by a 3d duality. A rational surgery calculus [@rolfsen1984rational] studies the equivalence relation among the choices. Every pair of equivalent Dehn surgery representations are known to be related by a sequence of basic local moves depicted in figure  [1](#fig:rational-surgery-moves){reference-type="ref" reference="fig:rational-surgery-moves"}. The basic moves may corresponds to basic 3d $\mathcal{N}=2$ dualities among $T^{6d}_{\rm irred}[M]$. Identifying the basic dualities would be interesting and we leave it as future work.

<figure id="fig:rational-surgery-moves">
<div class="center">
<p><embed src="basic-surgery-moves.pdf" /> <embed src="4152.pdf" /></p>
</div>
<figcaption>Left : Basic moves in rational surgery calculus <span class="citation" data-cites="rolfsen1984rational"></span>. The rational number <span class="math inline"><em>r</em><sub><em>i</em></sub></span> next to <span class="math inline"><em>i</em></span>-th component of link <span class="math inline"><em>K</em></span> represent Dehn filling slope and <span class="math inline"><strong>l</strong><strong>k</strong>(<em>i</em>,1)</span> denotes the linking number between <span class="math inline"><em>i</em></span>-th component and 1st component. Right: A sequence of basic moves showing <span class="math inline">(<em>S</em><sup>3</sup>∖<strong>4</strong><sub><strong>1</strong></sub>)<sub>−5<em>μ</em> + <em>λ</em></sub> = (<em>S</em><sup>3</sup>∖<strong>5</strong><sub><strong>2</strong></sub>)<sub>5<em>μ</em> + <em>λ</em></sub></span> </figcaption>
</figure>

#### Example :

As depicted in figure [1](#fig:rational-surgery-moves){reference-type="ref" reference="fig:rational-surgery-moves"}, topologically $(S^3\backslash \mathbf{4_1})_{-5\mu+\lambda} = (S^3 \backslash \mathbf{5_2})_{5\mu+\lambda}$. Combining the topological fact with eq. [\[Theory for m003/m004 Dehn-filled\]](#Theory for m003/m004 Dehn-filled){reference-type="eqref" reference="Theory for m003/m004 Dehn-filled"}, we have a 3d duality between following twos

$$\begin{aligned}
\begin{split}
&T^{6d}_{\rm irred}[(S^3 \backslash \mathbf{4_1})_{-5\mu+\lambda}] = \frac{\textrm{A $u(1)_0$ vector coupled to 2 chrials of charge +1}  }{SO(3)_{-5}} \quad \textrm{and}
\\
&T^{6d}_{\rm irred}[(S^3 \backslash \mathbf{5_2})_{5\mu+\lambda}] = \frac{\textrm{A $u(1)_{-1/2}$ vector coupled to 3 chrials of charge +1}  }{SO(3)_{1}}\;. \label{duality-surgery-example}
\end{split}
\end{aligned}$$

The theory in the numerator of the first line is the theory $T^{6d}_{\rm irred} [S^3 \backslash \mathbf{4_1}, \mu]= T^{DGG}[ S^3\backslash \mathbf{4_1}, \mu]$ which is claimed to have $SU(3)$ in section [\[sec:SU(3)\]](#sec:SU(3)){reference-type="eqref" reference="sec:SU(3)"}. The theory in in the first line is obtained by gauging $SO(3)$ subgroup of the $SU(3)$ flavor symmetry with CS level $-5$.

We are grateful to Yuji Tachikawa for very helpful discussions and for collaboration during part of this project. The work of DG was supported by Samsung Science and Technology Foundation under Project Number SSTBA1402-08. The work of KY is supported in part by the WPI Research Center Initiative (MEXT, Japan), and also supported by JSPS KAKENHI Grant-in-Aid (17K14265).
