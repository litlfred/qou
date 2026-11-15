---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-010-the-gamma-factors-for-symmetric-and-anti-symmetr
section_title: "The gamma factors for symmetric and anti-symmetric representations"
section_number: null
pages: 19-21
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.875
latex_coverage_ratio: 0.987
doc_brief: "Volume Conjecture: Reﬁned and Categoriﬁed — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebraic curve, the zero"
---
In order to determine the gamma factors from the consistency condition ([\[consistency_gamma\]](#consistency_gamma){reference-type="ref" reference="consistency_gamma"}), one needs the explicit form of the Littlewood-Richardson coefficients $N_{RR}^Q$. For the symmetric representation $R=S^r$ and the anti-symmetric representation $R=\Lambda^r$, the explicit expression for the Littlewood-Richardson coefficients can be obtained from the Pieri formula: $$\begin{aligned}
N_{S^rS^r}^{S^{r+\ell,r-\ell}}
& = & \prod_{j=1}^{r-\ell} { 1-q_1^{j-1} q_2 \over 1-q_1^j }
\cdot \prod_{j=2\ell+1}^{r+\ell} { 1-q_1^{j-1} q_2^2 \over 1-q_1^j q_2 } \cdot \prod_{j=\ell+1}^{r}
\left( { 1-q_1^{j}  \over 1-q_1^{j-1} q_2 } \right)^2 \,, \label{LRsymm}
\\
N_{\Lambda^r\Lambda^r}^{\Lambda^{r+\ell,r-\ell}}
& = & \prod_{i=1}^{\ell} { 1-q_1 q_2^{i-1} \over 1-q_2^i } \cdot \prod_{i=\ell+1}^{2\ell} {1-q_2^{i} \over 1-q_1q_2^{i-1}} \,.
\label{LRantisymm}
\end{aligned}$$

<figure>
<div class="center">
<embed src="young.eps" style="width:10cm" />
</div>
<figcaption>Young diagrams for tensor products of symmetric and anti-symmetric representations.</figcaption>
</figure>

For the symmetric and anti-symmetric representations, the sign factors $\epsilon^{Q}_{RR}$ in $\lambda^{(+)}_Q(R,R)$ look like [@RGK; @Ramadevi_Sarkar]: $$\epsilon_{S^rS^r}^{S^{r+\ell,r-\ell}} = (-1)^{r-\ell} \,, \qquad
\epsilon_{\Lambda^r\Lambda^r}^{\Lambda^{r+\ell,r-\ell}} = (-1)^{\ell} \,.$$

With the explicit expression for the Macdonald polynomials $M_{R} (q_2^{\varrho};q_1,q_2)$ given in ([\[Mac_sp\]](#Mac_sp){reference-type="ref" reference="Mac_sp"}), we can solve the constraint ([\[consistency_gamma\]](#consistency_gamma){reference-type="ref" reference="consistency_gamma"}) and find the following gamma factors (see Appendix [\[sec:gamma_proof\]](#sec:gamma_proof){reference-type="ref" reference="sec:gamma_proof"} for details): $$\begin{aligned}
\gamma_{S^rS^r}^{S^{r+\ell,r-\ell}}
& = & \prod_{i=1}^{r-\ell}\frac{q_1^{\frac{r-i}{2}}q_2^{\frac{1}{2}}-q_1^{-\frac{r-i}{2}}q_2^{-\frac{1}{2}}}{q_1^{\frac{r-i+1}{2}}-q_1^{-\frac{r-i+1}{2}}} \,,
\label{gamma_sym}
\\
\gamma_{\Lambda^r\Lambda^r}^{\Lambda^{r+\ell,r-\ell}}
& = & \prod_{i=1}^{\ell}\frac{q_2^{\frac{i}{2}}-q_2^{-\frac{i}{2}}}{q_2^{\frac{i-1}{2}}q_1^{\frac{1}{2}}-q_2^{-\frac{i-1}{2}}q_1^{-\frac{1}{2}}} \,.
\label{gamma_anti-sym}
\end{aligned}$$ It would be very interesting to understand the physical meaning / origin of the gamma factors.

Collecting all the ingredients, [\[Mac_sp\]](#Mac_sp){reference-type="eqref" reference="Mac_sp"}, [\[braid_ref\]](#braid_ref){reference-type="eqref" reference="braid_ref"}, and [\[LRsymm\]](#LRsymm){reference-type="eqref" reference="LRsymm"}--[\[gamma_anti-sym\]](#gamma_anti-sym){reference-type="eqref" reference="gamma_anti-sym"}, we obtain a final expression for the partition function [\[ZrefTpqq\]](#ZrefTpqq){reference-type="eqref" reference="ZrefTpqq"} with $R=S^r$ and $R=\Lambda^r$: $$\begin{aligned}
R = S^r ~:\quad &&Z_{SU(N)}^{\text{ref}}({\bf S}^3,T^{2,2p+1}_{S^r};q_1,q_2) / Z_{SU(N)}^{\text{ref}}({\bf S}^3;q_1,q_2)
\nonumber \\
&& \quad = \; \sum_{\ell=0}^r
\frac{(q_2;q_1)_{\ell}(q_1;q_1)_r(A;q_1)_{r+\ell}(q_2^{-1}A;q_1)_{r-\ell}}
{(q_1;q_1)_{\ell}(q_2;q_1)_r(q_2;q_1)_{r+\ell}(q_1;q_1)_{r-\ell}}\frac{(1-q_2q_1^{2\ell})}{(1-q_2)}
\nonumber \\
&&\quad \quad\quad\quad\times
A^{-r}
q_1^{\frac{r-\ell}{2}}
q_2^{\frac{3r-\ell}{2}}
\left[
(-1)^{r-\ell}A^{\frac{r}{2}}q_1^{\frac{r^2-\ell^2}{2}}q_2^{-\frac{\ell}{2}}\right]^{2p+1} \,,
\label{Braid_symmetric}
\\
R = \Lambda^r ~:\quad && Z_{SU(N)}^{\text{ref}}({\bf S}^3,T^{2,2p+1}_{\Lambda^r};q_1,q_2) / Z_{SU(N)}^{\text{ref}}({\bf S}^3;q_1,q_2)
\nonumber \\
&&\quad = \; \sum_{\ell=0}^r\frac{(q_1;q_2)_{\ell}(q_2;q_2)_{r+\ell}(A^{-1};q_2)_{r+\ell}(q_1^{-1}A^{-1};q_2)_{r-\ell}}
{(q_2;q_2)_{\ell}(q_1q_2;q_2)_{r+\ell}(q_2;q_2)_{r+\ell}(q_2;q_2)_{r-\ell}}\frac{(1-q_1q_2^{2\ell})}{(1-q_2)}
\nonumber \\
&&\quad\quad\quad\quad \times
A^{r}q_1^{r-\frac{\ell}{2}}q_2^{r-\frac{\ell}{2}}
\left[(-1)^{\ell}A^{\frac{r}{2}}q_1^{\frac{\ell}{2}}q_2^{\frac{\ell^2-r^2}{2}}
\right]^{2p+1},
\label{Braid_anti-symmetric}
\end{aligned}$$ where we used the standard notation for the $q$-Pochhammer symbol $$(x;q)_n \; = \; \prod_{k=0}^{n-1} (1 - x q^k) = (1-x) (1-xq) (1-xq^2) \ldots (1-x q^{n-1}) \,,$$ and where we introduced $$A \; := \; q_2^N \,.$$ Now we have all the relevant formulas at our fingertips that one needs to write down the superpolynomials of $(2,2p+1)$ torus knots colored by the symmetric and anti-symmetric representations, $R = S^r$ and $R = \Lambda^r$.
