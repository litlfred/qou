---
doc_id: arxiv-1411.6062v2
doc_title: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS"
section_id: sec-008-22-applications-to-1-dimensional-state-integrals
section_title: "Applications to 1-dimensional state-integrals: proof of Theorem 1.1"
section_number: 2.2
pages: 10-11
source_pdf: 1411.6062v2.pdf
source_sha256: 5abd328d027de43c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.896
latex_coverage_ratio: 0.908
doc_brief: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS — Multi-dimensional state-integrals of products of Faddeev’s quantum diloga- rithms arise frequently in Quantum Topology, quantum Teichm¨uller theory"
---
[]{#sub.application label="sub.application"}

In this section we prove Theorem [\[thm.1\]](#thm.1){reference-type="ref" reference="thm.1"}. Fix integers $A$ and $B$ with $B>A>0$. The values of particular interest are $(A,B)=(1,2)$ and $(1,3)$ which correspond to the state-integrals of the knots $4_1$ and $5_2$ respectively. For the $4_1$ knot, see  [@AK Eqn.38] and [@KLV Eqn.47] and [@state-integrals]. For the $5_2$ knot, see  [@KLV Eqn.53]. For the remaining values of $(A,B)$, although the 1-dimensional state integral makes sense, and it can be analyzed using our methods, there is no corresponding knot that we know of.

If $$\operatorname{f}(z-c_{\mathsf{b}})=\operatorname{\Phi}_{\mathsf{b}}(z)^Be^{-A\pi\mathsf{i}z^2},
\quad c_{\mathsf{b}}=(\mathsf{b}+\mathsf{b}^{-1})\mathsf{i}/2,$$ then $$\begin{align}
\label{gxAB}
\operatorname{g}\!\left(x\right) &= 
\left(-x \right)^A\! \left(1-x\right)^{-B}
\\
\operatorname{g^\pm}(x)&=\operatorname{g}\!\left(q_\pm x\right)
\\
\operatorname{g^\pm}_n(x;q_\pm)&=\left(-x \right)^{An}\!
q_\pm^{\frac{A}{2}n(n+1)}\!\left(q_\pm x;q_\pm\right)_{n}^{-B},\qquad 
\forall n\in\mathbb{Z}.
\end{align}$$ Observe that $\operatorname{f}(z)$ is non-vanishing and absolutely integrable along the line $\mathcal{C}_{\lambda}$ if $$-(M+N)/2<\lambda<0,$$ and $\operatorname{f}(z+\mathsf{s}\mathsf{i})\ne \operatorname{f}(z)$ if $\lambda$ is in general position. By using [\[eq.Phieval+\]](#eq.Phieval+){reference-type="eqref" reference="eq.Phieval+"}, we obtain that

$$\begin{aligned}
\label{fzAB}
\operatorname{f}(z)&=\operatorname{\Phi}_{\mathsf{b}}(z+c_{\mathsf{b}})^B
e^{-A\pi\mathsf{i}(z+c_{\mathsf{b}})^2} \\ \notag 
&
=\frac{e^{\frac{\mathsf{i}B}{2\pi\mathsf{s}^2}\operatorname{Li_2}(e^{2\pi\mathsf{s}z})}
\left(1-e^{2\pi\mathsf{s}z}\right)^{B+B\mathsf{i}z\mathsf{s}^{-1}}}{
\slashed{\operatorname{D}}_N(e^{2\pi\mathsf{b}z};q_+)^B
\slashed{\operatorname{D}}_M(e^{2\pi\mathsf{b}^{-1}z};q_-)^B}
e^{-A\pi\mathsf{i}(z+c_{\mathsf{b}})^2}.
\end{aligned}$$

By using the identity $$\begin{aligned}
e^{-A\pi\mathsf{i}(z+c_{\mathsf{b}})^2} &=
e^{-A\pi\mathsf{i}\left(c_{\mathsf{b}}+\frac{\mathsf{i}}{2\mathsf{s}}\right)^2}
e^{A(2\pi\mathsf{s}z-\pi\mathsf{i}) (1-4\mathsf{s}\mathsf{i}c_{\mathsf{b}} -2\mathsf{s}\mathsf{i}z)\mathsf{s}^{-2}/4}
\\
&=e^{A\pi\mathsf{i}\frac{(M+N+1)^2}{4 M N}}
e^{A(2\pi\mathsf{s}z-\pi\mathsf{i}) (1-4\mathsf{s}\mathsf{i}c_{\mathsf{b}} -2\mathsf{s}\mathsf{i}z)\mathsf{s}^{-2}/4}
\end{aligned}$$ and [\[gxAB\]](#gxAB){reference-type="eqref" reference="gxAB"}, we can rewrite [\[fzAB\]](#fzAB){reference-type="eqref" reference="fzAB"} in the form

$$\begin{aligned}
\label{eq.fzval}
\operatorname{f}(z)&=
\frac{e^{\frac{\mathsf{i}B}{2\pi \mathsf{s}^2}\operatorname{R}(e^{2\pi\mathsf{s}z})
(1-e^{2\pi\mathsf{s}z})^{\frac{(2N+1)(2M+1)}{4 M N}B}
}}{
\slashed{\operatorname{D}}_N(e^{2\pi\mathsf{b}z};q_+)^B
\slashed{\operatorname{D}}_M(e^{2\pi\mathsf{b}^{-1}z};q_-)^B} 
\,\, e^{\pi\mathsf{i}\frac{B+3A(M+N+1)^2}{12 M N}} 


\operatorname{g}\!\left(e^{2\pi\mathsf{s}z}
\right)^{\frac{1-4\mathsf{s}\mathsf{i}c_{\mathsf{b}} -2\mathsf{s}\mathsf{i}z}{4\mathsf{s}^{2}}},
\end{aligned}$$

where $R(x)$ is the Rogers dilogarithm [\[eq.rogers\]](#eq.rogers){reference-type="eqref" reference="eq.rogers"}.

It is easy to see that the only singularities in Equation [\[eq.main\]](#eq.main){reference-type="eqref" reference="eq.main"} are simple poles that come from solutions to the equation $1-\operatorname{g}\! \left(e^{2\pi\mathsf{s}z}\right)=1$. Moreover, if $z=\alpha$ is a solution with $0<\mathsf{s}\, \mathrm{Im}\alpha-\lambda<1$, then $$2\pi\mathsf{i}\operatorname{Res}_{z=\alpha}
\frac{\operatorname{f}(z)\operatorname{S}\!
\left(e^{2\pi\mathsf{b}z},e^{2\pi\mathsf{b}^{-1}z}\right)}{1-\operatorname{g}\!
\left(e^{2\pi\mathsf{s}z}\right)} =
\mathsf{i}^{-1} \mathsf{s}^{-1}
\frac{\operatorname{f}(\alpha)\operatorname{S}\!
\left(e^{2\pi\mathsf{b}\alpha},e^{2\pi\mathsf{b}^{-1}\alpha}\right)}{
e^{2\pi\mathsf{s}\alpha} \operatorname{g}'
\left(e^{2\pi\mathsf{s}\alpha}\right)} \,.$$ Combining Lemma [\[lem.main\]](#lem.main){reference-type="ref" reference="lem.main"} with Equation [\[eq.fzval\]](#eq.fzval){reference-type="eqref" reference="eq.fzval"} concludes the proof of Theorem [\[thm.1\]](#thm.1){reference-type="ref" reference="thm.1"}. 0◻
