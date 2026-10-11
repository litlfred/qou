---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-001-16-irreducible-jack-characters
section_title: "Irreducible Jack characters"
section_number: 1.6
pages: 3-5
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Y oung diagrams which can be regarded as a natural one-parameter deformation of so me classi- cal Y"
text_source: latex
latex_prose_ratio: 0.901
latex_coverage_ratio: 0.982
---
In the current paper we will use another, more general, family $(\chi^{(\alpha)}_\lambda)$ of irreducible characters in [\[eq:proba-linearcomb\]](#eq:proba-linearcomb){reference-type="eqref" reference="eq:proba-linearcomb"}. Our starting point is the family of *Jack polynomials* $J^{(\alpha)}_\lambda$ [@Jack1970/1971] which can be regarded as a deformation of the family of Schur polynomials; a deformation that depends on the parameter $\alpha>0$. We use the normalization of Jack polynomials from [@Macdonald1995 Section VI.10].

We expand Jack polynomial in the basis of power-sum symmetric functions: $$\label{eq:definition-theta-A}
J^{(\alpha)}_\lambda = \sum_\pi \theta^{(\alpha)}_\pi(\lambda)\ p_\pi.$$ The above sum runs over partitions $\pi$ such that $|\pi|=|\lambda|$. For a given integer $n\geq 1$, any Young diagram $\lambda\in\mathbb{Y}_{n}$ and any partition $\pi\in\mathcal{P}_{n}$ we define the *irreducible Jack character $\chi^{(\alpha)}_\lambda$* as $$\label{eq:character-Jack-unnormalized-zmiana}
\chi^{(\alpha)}_\lambda(\pi) :=  \alpha^{-\frac{\|\pi\|}{2}}\ \frac{z_\pi}{n!}\ \theta^{(\alpha)}_\pi(\lambda).$$ Above, $$\|\pi\|:=|\pi|-\ell(\pi)$$ denotes the *length* of the partition $\pi=(\pi_1,\dots,\pi_l)$, while $\ell(\pi)=l$ denotes its *number of parts*. Also, the numerical factor $z_\lambda$ is defined by $$\label{eq:zlambda}
z_\lambda:= \prod_{i\geq 1} m_i(\lambda)!\ i^{m_i(\lambda)},$$ where $m_i(\lambda):=\big|\{k: \lambda_k=i\}\big|$ is the *multiplicity* of $i$ in the partition $\lambda$.

It is worth pointing out that in the special case $\alpha=1$ the corresponding Jack character $\chi^{(1)}_\lambda(\pi)=\chi_\lambda(\pi)$ coincides with the irreducible character [\[eq:character-irrep\]](#eq:character-irrep){reference-type="eqref" reference="eq:character-irrep"} of the symmetric group $\mathfrak{S}(n)$, see [@Lassalle2009; @DolegaFeray2014].

## Probability measures $\mathbb{P}^{(\alpha)}_\chi$

With $\chi_\lambda:=\chi_\lambda^{(\alpha)}$ given by the irreducible Jack characters, [\[eq:proba-linearcomb\]](#eq:proba-linearcomb){reference-type="eqref" reference="eq:proba-linearcomb"} takes the following more specific form $$\label{eq:proba-linearcomb-A}
\chi = \sum_{\lambda\in\mathbb{Y}_{n}} \mathbb{P}^{(\alpha)}_\chi(\lambda) \ \chi^{(\alpha)}_\lambda.$$ If the coefficients $\mathbb{P}^{(\alpha)}_\chi(\lambda)\geq 0$ are non-negative, we will say that $\chi$ is a *reducible Jack character*. The resulting probability measure $\mathbb{P}^{(\alpha)}_\chi$ on $\mathbb{Y}_{n}$ is in the focus of the current paper.

In the simplest example of $\chi:=\chi_{\mathop{\mathrm{reg}}}$ given by [\[eq:regular\]](#eq:regular){reference-type="eqref" reference="eq:regular"} the corresponding probability measure $\mathbb{P}^{(\alpha)}_{\chi_{\mathop{\mathrm{reg}}}}$ turns out to be the celebrated *Jack--Plancherel measure* [@Stanley1989; @Fulman2004; @Matsumoto2008; @DolegaFeray2014; @BorodinGorinGuionnet2015; @Moll2015] which is a one-parameter deformation of the Plancherel measure.

## Random Young diagrams related to Thoma's characters

An additional motivation for considering this particular class of random Young diagrams stems from the research related to the problem of finding extremal characters of the infinite symmetric group $\mathfrak{S}(\infty)$, solved by Thoma [@Thoma1964]. Vershik and Kerov [@VershikKerov1981a] found an alternative, more conceptual proof of Thoma's result, which was based on the observation that *characters of $\mathfrak{S}(\infty)$ are in a natural bijective correspondence with certain sequences $(\lambda_1\nearrow \lambda_2\nearrow\cdots)$ of growing random Young diagrams*.

The original Thoma's problem can be equivalently formulated as finding all homomorphisms from the ring of symmetric functions to real numbers which are *Schur-positive*, i.e. which take non-negative values on all Schur polynomials. In this formulation the problem naturally asks for generalizations in which Schur polynomials are replaced by another interesting family of symmetric functions. Kerov, Okounkov and Olshanski [@KerovOkounkovOlshanski1998] considered the particular case of *Jack polynomials* and they proved that a direct analogue of Thoma's result holds true also in this case. The main idea behind their proof was that the probabilistic viewpoint from the above-mentioned work of Vershik and Kerov [@VershikKerov1981a] can be adapted to the new setting of Jack polynomials. Thus, a side product of the work of Kerov, Okounkov and Olshanski is an interesting, natural class of random Young diagrams which fits into the framework which we consider in the current paper, see [\[example:removal-of-boxes\]](#example:removal-of-boxes){reference-type="ref" reference="example:removal-of-boxes"} and the forthcoming paper [@DolegaSniady-examples-AFP] for more details.
