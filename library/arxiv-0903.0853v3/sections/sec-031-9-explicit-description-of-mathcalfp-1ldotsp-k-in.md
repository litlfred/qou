---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-031-9-explicit-description-of-mathcalfp-1ldotsp-k-in
section_title: "Explicit description of ${\mathcal{F}}(P_{1},\ldots,P_{k})$ in the case of integral slopes"
section_number: 9
pages: 42-43
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.833
latex_coverage_ratio: 0.962
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#section:explicitdescription label="section:explicitdescription"}

***FROM NOW ON, WE ASSUME THAT THE SLOPES ARE INTEGRAL:*** $\mu_{1},\ldots,\mu_{k} \in {\mathbf Z}$.\
It is then possible to make the results of sections [\[section:isoformalclasses\]](#section:isoformalclasses){reference-type="ref" reference="section:isoformalclasses"} and [\[section:indextheorems\]](#section:indextheorems){reference-type="ref" reference="section:indextheorems"} more algorithmic by using the matricial description of paragraph [\[subsection:matricialdescriptionofF(P1,\...,Pk)\]](#subsection:matricialdescriptionofF(P1,...,Pk)){reference-type="ref" reference="subsection:matricialdescriptionofF(P1,...,Pk)"}. Indeed, as explained in paragraph [\[subsubsection:integralslopes\]](#subsubsection:integralslopes){reference-type="ref" reference="subsubsection:integralslopes"}, our construction of normal forms and of explicit Stokes operators depends on the normal form [\[eqn:formestandardtriangulaireentiere\]](#eqn:formestandardtriangulaireentiere){reference-type="eqref" reference="eqn:formestandardtriangulaireentiere"} given herebelow for pure modules.\
For $i = 1,\ldots,k$, we thus write $P_{i} = ({{\mathbf C}(\{z\})}^{r_{i}},\Phi_{z^{\mu_{i}} A_{i}})$, with $A_{i} \in {\text{GL}}_{r_{i}}({\mathbf C})$. Then, putting $n := r_{1} + \cdots + r_{k}$, we have $M_{0} := P_{1} \oplus \cdots \oplus P_{k} = (K^{n},\Phi_{A_{0}})$, with $A_{0}$ as in equation [\[eqn:formestandarddiagonale\]](#eqn:formestandarddiagonale){reference-type="eqref" reference="eqn:formestandarddiagonale"} page from paragraph [\[subsection:matricialdescriptionofF(P1,\...,Pk)\]](#subsection:matricialdescriptionofF(P1,...,Pk)){reference-type="ref" reference="subsection:matricialdescriptionofF(P1,...,Pk)"}: $$\label{eqn:formestandarddiagonaleentiere}
A_{0} := \begin{pmatrix}
z^{\mu_{1}} A_{1}  & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots  & 0 & \ldots \\
0      & \ldots & \ldots   & \ldots & \ldots \\
\ldots & 0 & \ldots  & \ldots & \ldots \\
0      & \ldots & 0       & \ldots & z^{\mu_{k}} A_{k}    
\end{pmatrix}.$$ Any class in ${\mathcal{F}}(P_{1},\ldots,P_{k})$ can be represented by a module []{#not35 label="not35"} $M_{U} := (K^{n},\Phi_{A_{U}})$ for some $U := (U_{i,j})_{1 \leq i < j \leq k} \in 
\prod\limits_{1 \leq i < j \leq k} {\text{Mat}}_{r_{i},r_{j}}({{\mathbf C}(\{z\})})$, with, $A_{U}$ as in equation ([\[eqn:formestandardtriangulaire\]](#eqn:formestandardtriangulaire){reference-type="ref" reference="eqn:formestandardtriangulaire"}): $$\label{eqn:formestandardtriangulaireentiere}
A_{U} := \begin{pmatrix}
z^{\mu_{1}} A_{1} & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots  & U_{i,j} & \ldots \\
0      & \ldots & \ldots   & \ldots & \ldots \\
\ldots & 0 & \ldots  & \ldots & \ldots \\
0      & \ldots & 0       & \ldots & z^{\mu_{k}} A_{k} 
\end{pmatrix},$$ and $M_{U},M_{V}$ represent the same class if, and only if, the equation $(\sigma_qF) A_{V} = A_{U} F$ can be solved with $F \in {\mathfrak{G}}({{\mathbf C}(\{z\})})$. Such an $F$ is then unique.
