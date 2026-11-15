---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-020-22-normalized-jack-characters
section_title: "Normalized Jack characters"
section_number: 2.2
pages: 15-17
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 0.905
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
---
The usual way of viewing the characters of the symmetric groups is to fix the irreducible representation $\lambda$ and to consider the character as a function of the conjugacy class $\pi$. However, there is also another very successful viewpoint due to Kerov and Olshanski [@KerovOlshanski1994], called *dual approach*, which suggests to do roughly the opposite. Lassalle [@Lassalle2008a; @Lassalle2009] adapted this idea to the framework of Jack characters. In order for this dual approach to be successful one has to choose the most convenient normalization constants. In the current paper we will use the normalization introduced by Dołęga and Féray [@DolegaFeray2014] which offers some advantages over the original normalization of Lassalle. Thus, with the right choice of the multiplicative constant, the unnormalized Jack character $\chi^{(\alpha)}_\lambda$ from [\[eq:character-Jack-unnormalized-zmiana\]](#eq:character-Jack-unnormalized-zmiana){reference-type="eqref" reference="eq:character-Jack-unnormalized-zmiana"} becomes the *normalized Jack character $\mathop{\mathrm{Ch}}^{(\alpha)}_\pi(\lambda)$*, defined as follows.

::: definition
[]{#def:jack-character-classical label="def:jack-character-classical"} Let $\alpha>0$ be given and let $\pi$ be a partition. For any Young diagram $\lambda$ the value of the *normalized Jack character $\mathop{\mathrm{Ch}}_\pi^{(\alpha)}(\lambda)$* is given by:

$$\label{eq:what-is-jack-character-zmiana}
    \mathop{\mathrm{Ch}}_{\pi}^{(\alpha)}(\lambda):=
    \begin{cases}
    |\lambda|^{\underline{|\pi|}}\ \chi^{(\alpha)}_\lambda(\pi)
    &\text{if }|\lambda| \ge |\pi| ;\\
    0 & \text{if }|\lambda| < |\pi|,
    \end{cases}$$ where $$n^{\underline{k}}:=n (n-1) \cdots (n-k+1)$$ denotes the falling power and $\chi^{(\alpha)}_\lambda(\pi)$ is the Jack character [\[eq:character-Jack-unnormalized-zmiana\]](#eq:character-Jack-unnormalized-zmiana){reference-type="eqref" reference="eq:character-Jack-unnormalized-zmiana"}. The choice of an empty partition $\pi=\emptyset$ is acceptable; in this case $\mathop{\mathrm{Ch}}_\emptyset^{(\alpha)}(\lambda)=1$.
:::

Each Jack character depends on the deformation parameter $\alpha$; in order to keep the notation light we will make this dependence implicit and we will simply write $\mathop{\mathrm{Ch}}_{\pi}(\lambda)$.
