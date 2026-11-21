---
doc_id: arxiv-hep-th-0006156v1
doc_title: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality"
section_id: sec-003-12-magri-bracket
section_title: "Magri bracket"
section_number: 1.2
pages: 3-4
source_pdf: 0006156v1.pdf
source_sha256: b799d4ef150291cf
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.952
doc_brief: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality — The quantum discrete Liouville model in the strongly cou- pled regime, 1 < c < 25, is formulated as a well"
---
The canonical Poisson bracket $$\{\varpi(x),\varphi(y)\}=\delta(x-y)$$ on the laboratory Cauchy data $$\varphi=\phi|_{t=0}\qquad\qquad
\varpi=\phi_t|_{t=0} ,$$ together with canonical total momentum and energy $$P=\int\varpi\varphi'dx\qquad\qquad
H={\tfrac12}\int(\varpi^2 +\varphi^{\prime2}+4e^{-2\varphi})dx$$ gives the equations of motion in the Hamiltonian formalism: $$\begin{aligned} \varphi'&=\{P,\varphi\}       \\
     \varpi'&=\{P,\varpi\} \end{aligned} \qquad\qquad\begin{aligned}
     \dot\varphi&=\varpi=\{H,\varphi\}             \\
     \dot\varpi&=\varphi''+4e^{-2\varphi} =\{H,\varpi\}.
   \end{aligned}$$ These equations lead to a single free motion equation $$\label{cr}
   \dot u=-u'=\{L_0,u\}     ,$$ with $L_0$ denoting the (slightly shifted) zero'th Fourier coefficient $$L_0=\int(u+{\tfrac14})\:dx
={\tfrac12}(H-P+\pi) .$$ The bracket involved is the same canonical bracket of course, but now we are prompted to express it, using formula ([\[se\]](#se){reference-type="ref" reference="se"}) at $t=0$, in terms of either $u$ itself or its Fourier coefficients $L_a=\int(u+{\tfrac14})e^{-iax}dx$. The Magri bracket [@magri] $$\label{mb}
   \{u(x),u(y)\}=(u(x)+u(y))\,\delta'(x-y)
   -{\tfrac12}\,\delta'''(x-y)$$ and yet more celebrated (Poisson bracket realization of) the Virasoro algebra $$- i\{L_a,L_b\}=(a-b)L_{a+b}
+\pi(a^3-a)\delta_{a,-b}$$ emerge. They will attract our attention in the next couple of (sub)sections where we shall try to treat the Magri bracket and the "chiral Hamiltonian" $L_0$ as a stand-alone dynamical system, not for the first time of course. We shall review some earlier attempts to get it properly discretized and quantized. It will give an idea how far we can go on bare common sense and formal algebra, without actually touching the Liouville equation.
