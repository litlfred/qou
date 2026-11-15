---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-006-16-irreducible-jack-characters
section_title: "Irreducible Jack characters"
section_number: 1.6
pages: 3-4
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.848
latex_coverage_ratio: 0.952
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
---
In the current paper we will use another, more general, family $(\chi^{(\alpha)}_\lambda)$ of irreducible characters in [\[eq:proba-linearcomb\]](#eq:proba-linearcomb){reference-type="eqref" reference="eq:proba-linearcomb"}. Our starting point is the family of *Jack polynomials* $J^{(\alpha)}_\lambda$ [@Jack1970/1971] which can be regarded as a deformation of the family of Schur polynomials; a deformation that depends on the parameter $\alpha>0$. We use the normalization of Jack polynomials from [@Macdonald1995 Section VI.10].

We expand Jack polynomial in the basis of power-sum symmetric functions: $$\label{eq:definition-theta-A}
J^{(\alpha)}_\lambda = \sum_\pi \theta^{(\alpha)}_\pi(\lambda)\ p_\pi.$$ The above sum runs over partitions $\pi$ such that $|\pi|=|\lambda|$. For a given integer $n\geq 1$, any Young diagram $\lambda\in\mathbb{Y}_{n}$ and any partition $\pi\in\mathcal{P}_{n}$ we define the *irreducible Jack character $\chi^{(\alpha)}_\lambda$* as $$\label{eq:character-Jack-unnormalized-zmiana}
\chi^{(\alpha)}_\lambda(\pi) :=  \alpha^{-\frac{\|\pi\|}{2}}\ \frac{z_\pi}{n!}\ \theta^{(\alpha)}_\pi(\lambda).$$ Above, $$\|\pi\|:=|\pi|-\ell(\pi)$$ denotes the *length* of the partition $\pi=(\pi_1,\dots,\pi_l)$, while $\ell(\pi)=l$ denotes its *number of parts*. Also, the numerical factor $z_\lambda$ is defined by $$\label{eq:zlambda}
z_\lambda:= \prod_{i\geq 1} m_i(\lambda)!\ i^{m_i(\lambda)},$$ where $m_i(\lambda):=\big|\{k: \lambda_k=i\}\big|$ is the *multiplicity* of $i$ in the partition $\lambda$.

It is worth pointing out that in the special case $\alpha=1$ the corresponding Jack character $\chi^{(1)}_\lambda(\pi)=\chi_\lambda(\pi)$ coincides with the irreducible character [\[eq:character-irrep\]](#eq:character-irrep){reference-type="eqref" reference="eq:character-irrep"} of the symmetric group $\mathfrak{S}(n)$, see [@Lassalle2009; @DolegaFeray2014].
