---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-057-19-analytic-classification-of-linear-q-differenc
section_title: "Analytic classification of linear $q$-difference equations"
section_number: 19
pages: 99-100
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.897
latex_coverage_ratio: 0.771
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#section:analyticclassificationCZ label="section:analyticclassificationCZ"}

We now return to the classification problem, with the notations of chapter [\[chapter:isoformalclasses\]](#chapter:isoformalclasses){reference-type="ref" reference="chapter:isoformalclasses"}. In particular, we consider a block diagonal matrice $A_{0}$ as in [\[eqn:formestandarddiagonaleentiere\]](#eqn:formestandarddiagonaleentiere){reference-type="eqref" reference="eqn:formestandarddiagonaleentiere"} page , and the corresponding space ${\mathcal{F}}(P_{1},\ldots,P_{k})$ of isoformal analytic classes within the formal class defined by $A_{0}$.

The space of block upper triangular matrices $A_{U}$ as in [\[eqn:formestandardtriangulaireentiere\]](#eqn:formestandardtriangulaireentiere){reference-type="eqref" reference="eqn:formestandardtriangulaireentiere"} page such that moreover each rectangular block $U_{i,j}$ belongs to ${\text{Mat}}_{r_{i},r_{j}}(K_{\mu_{i},\mu_{j}})$ (according to the notations of the beginning of subsection [\[subsection:twointegralslopes\]](#subsection:twointegralslopes){reference-type="ref" reference="subsection:twointegralslopes"}) will be written for short ${{\mathcal C}_{A_0}}$. []{#not80 label="not80"} It follows from proposition [\[prop:kintegralslopesspace\]](#prop:kintegralslopesspace){reference-type="ref" reference="prop:kintegralslopesspace"} that sending $A_{U}$ to its class induces an isomorphism of ${{\mathcal C}_{A_0}}$ with ${\mathcal{F}}(P_{1},\ldots,P_{k})$.

Let $A \in {{\mathcal C}_{A_0}}$ et consider the conjugation equation: $$\label{eqn:conjugaison}
(\sigma_qF) A_0 = A F;$$ We saw in the first part of [\[subsection:computnormalform\]](#subsection:computnormalform){reference-type="ref" reference="subsection:computnormalform"} that this admits a unique solution $\hat F = (\hat F_{ij})$ in ${\mathfrak{G}}({{\mathbf C}[[z]]})$. After J.P. Bézivin [@Bezivin], this solution satisfies the following $q$-Gevrey condition: $$\forall i < j ~,~
\hat F_{ij} \in {\text{Mat}}_{r_i,r_j}\bigl({{\mathbf C}[[z]]}_{q;1/(\mu_{j}-\mu_{j-1})}\bigr)~.$$

In this section, we shall first prove that the formal power series $\hat F$ is multisummable according to definition [\[defi:msommabilite\]](#defi:msommabilite){reference-type="ref" reference="defi:msommabilite"}. We shall deduce the existence of solutions that are asymptotic to the formal solution $\hat F$ at zero along divisors $(\Lambda_1,\Lambda)$ (see definition [\[defi:Lambda1Lambda\]](#defi:Lambda1Lambda){reference-type="ref" reference="defi:Lambda1Lambda"}). Last, in [\[subsection:Stokes\]](#subsection:Stokes){reference-type="ref" reference="subsection:Stokes"}, we shall prove that the Stokes multipliers make up a complete set of analytic invariants.

In the following, a matrix-valued function will be said to be summable or multisummable or to have an asymptotic expansion if each coefficient of the matrix is such a function. In this way, we will be led to consider spaces ${\mathfrak{G}}({\mathbb A}_{q}^\Lambda)$, ${\text{Mat}}_{n_1,n_2}({\mathbb O}_{(\Lambda_1,\ldots,\Lambda_{m})}^{\Lambda})$, etc.
