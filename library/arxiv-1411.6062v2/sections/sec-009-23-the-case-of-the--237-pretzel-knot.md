---
doc_id: arxiv-1411.6062v2
doc_title: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS"
section_id: sec-009-23-the-case-of-the--237-pretzel-knot
section_title: "The case of the (-2,3,7) pretzel knot"
section_number: 2.3
pages: 11-13
source_pdf: 1411.6062v2.pdf
source_sha256: 5abd328d027de43c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 0.92
doc_brief: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS — Multi-dimensional state-integrals of products of Faddeev’s quantum diloga- rithms arise frequently in Quantum Topology, quantum Teichm¨uller theory"
---
[]{#sub.pretzel label="sub.pretzel"}

The second author computed the state-integral invariant of the $(-2,3,7)$ pretzel knot. The result of the long computation is the following 1-dimensional state integral, which we take as input to our analysis:

$$\label{eq.I237}
I_{(-2,3,7)}(b)=\int_{\mathbbm R+ i \epsilon} \operatorname{\Phi}_{\mathsf{b}}(x)^2 
\operatorname{\Phi}_{\mathsf{b}}(2x-c_{\mathsf{b}}) e^{-2 \pi \mathsf{i}x^2} dx$$ The integral is absolutely convergent, and the statement and proof of Theorem [\[thm.1\]](#thm.1){reference-type="ref" reference="thm.1"} applies using the following definition of the functions $\operatorname{f}(x)$, $\operatorname{g^\pm}_k(x,q)$ and $\operatorname{g}(x)$: $$\begin{align}
\operatorname{f}(x-c_{\mathsf{b}}) &= 
\operatorname{\Phi}_{\mathsf{b}}(x)^2 \operatorname{\Phi}_{\mathsf{b}}(2x-c_{\mathsf{b}})e^{-2 \pi \mathsf{i}x^2} \\
\operatorname{g^\pm}_k(x,q) &=  \frac{
q^{k(k+1)} \!x^{2k} }{\left(q x;q\right)^{2}_k\!\left(q x^2;q\right)_{2k}}   \\
\operatorname{g}(x) &= \frac{x^2}{\left(1-x\right)^2\!\left(1-x^2\right)^2} \,.
\end{align}$$ Observe that $\operatorname{f}(z)$ is non-vanishing and absolutely integrable along the line $\mathcal{C}_{\lambda}$ if $$-(M+N)/4<\lambda<0,$$ and $\operatorname{f}(z+\mathsf{s}\mathsf{i})\ne \operatorname{f}(z)$ if $\lambda$ is in general position.

We now discuss the solutions of the gluing equations $\operatorname{g}(x)=1$ and the matching with the set of nonabelian parabolic $\mathrm{PSL}(2,\mathbbm C)$ representations, illustrating Remark [\[rem.parabolic\]](#rem.parabolic){reference-type="ref" reference="rem.parabolic"}.

The equation $\operatorname{g}(x)=1$ has 6 solutions that come from two cubic equations: $$\label{eq.2cubic}
\frac{z}{(1-z^2)(1-z)} = \pm 1 \,.$$ Each triple of solutions lies in number fields $F_+$ and $F_-$ of discriminant $-23$ and $49$ and type $[1,1]$ and $[3,0]$ respectively.

On the other hand, there are 6 nonabelian parabolic $\mathrm{PSL}(2,\mathbbm C)$ representations of the $(-2,3,7)$ pretzel knot. These may be found using the Ptolemy methods of [@ptolemy] and their `snappy` implementation [@snappy]. An alternative method is to use the $A$-polynomial of the pretzel knot from [@Culler:Apoly]

$$A(m,l)=l^6 - l^5 m^8 + 2 l^5 m^9 - l^5 m^{10} - 2 l^4 m^{18} - l^4 m^{19} + 
l^2 m^{36} + 2 l^2 m^{37} + l m^{45} - 2 l m^{46} + l m^{47} - m^{55}$$ Observe that $A(1,l)=(l-1)^3(l+1)^3$. Setting $(m,l)=(1+t,\pm 1+c_{\pm} t + O(t^2))$ we obtain that $$-6119 + 2012 c_- - 220 c_-^2 + 8 c_-^3 =0, \qquad
-6193 - 2020 c_+ - 220 c_+^2 - 8 c_+^3 =0$$ Then, we have $F_\pm=\mathbbm Q(c_\pm)$. If $z$ is a solution to [\[eq.2cubic\]](#eq.2cubic){reference-type="eqref" reference="eq.2cubic"}, let $\rho_z$ denote the corresponding nonabelian parabolic $\mathrm{PSL}(2,\mathbbm C)$ representation. The Rogers dilogarithm of $z$ agrees with the complex volume of $\rho_z$, and $\operatorname{g}'(x)$ agrees with the 1-loop invariant of $\rho_z$.

Incidentally, if $z \in F_+$, a totally real field, then the corresponding triple of elements of the Bloch group is torsion and triple of complex volumes is given by $$\left(\mathsf{e}\left(-\frac{19}{42}\right), 
\mathsf{e}\left(-\frac{13}{42}\right),
\mathsf{e}\left(\frac{11}{42}\right) \right)= 
\mathsf{e}\left(-\frac{19}{42}\right) 
\left(1, 
\mathsf{e}\left(\frac{1}{7}\right),
\mathsf{e}\left(-\frac{2}{7}\right) \right)
\,,$$ where $\mathsf{e}(x)$ is given by Equation [\[eq.ex\]](#eq.ex){reference-type="eqref" reference="eq.ex"}.
