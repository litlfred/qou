---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-020-the-chern-character-and-inner-products
section_title: "The Chern character and inner products."
section_number: null
pages: 24-25
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.972
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasizing the importance of a pairing which generalizes Mukai’s pairing on the cohomology of K3"
---
One reading of the Hirzebruch-Riemann-Roch Theorem is that it says that the usual Chern character map $\mathop{\mathrm{ch}}\colon \mathop{\mathrm{K}}_0\to \mathsf H^\bullet(X)$ is a map of inner product spaces when $\mathop{\mathrm{K}}_0(X)$ is equipped with the Euler pairing (see below) and $\mathsf H^\bullet(X)$ is equipped with the pairing $\langle x_1,x_2\rangle:=(x_1\cup x_2 \cup \mathop{\mathrm{td}}_X)\cap [X]$. It is shown in [@CalHH2] that the Hochschild homology Chern character composed with the Hochschild-Kostant-Rosenberg map $I_{\text{HKR}}$ gives the usual Chern character: $$\mathop{\mathrm{K}}_0\xrightarrow{\mathop{\mathrm{ch}}}\mathop{\mathrm{HH}}_0(X)\xrightarrow{I_\text{HKR}}
\bigoplus_p \mathsf H^{p,p}(X).$$ Here we show that the Hochschild homology Chern character is an inner-product map when $\mathop{\mathrm{HH}}_\bullet(X)$ is equipped with the Mukai pairing.

First recall that the Euler pairing on $\mathop{\mathrm{K}}_0(X)$ is defined by $$\chi({\mathscr E},{\mathscr F}):=\sum_i (-1)^i \dim \mathop{\mathrm{Ext}}^i_X({\mathscr E}, {\mathscr F}).$$

::: Theorem
[]{#thm:hrr label="thm:hrr"} The Chern character $$\mathop{\mathrm{ch}}\colon \mathop{\mathrm{K}}_0\to \mathop{\mathrm{HH}}_0(X)$$ is a map of inner-product spaces: in other words, for ${\mathscr E}, {\mathscr F}\in
\mathbf{D}(X)$ we have $${\ensuremath{\left\langle \mathop{\mathrm{ch}}({\mathscr E}),\, \mathop{\mathrm{ch}}({\mathscr F})\right\rangle_{\rm M}}} = \chi({\mathscr E}, {\mathscr F}).$$
:::

::: Proof
The first thing to do is to get an interpretation of the Euler pairing. Considering the totality of $\mathop{\mathrm{Ext}}$-groups $\mathop{\mathrm{Ext}}^\bullet({\mathscr E},{\mathscr F})$ as a graded vector space, the Euler characteristic is just the graded dimension of $\mathop{\mathrm{Ext}}^\bullet({\mathscr E},{\mathscr F})$, which is to say it is the trace of the identity map on $\mathop{\mathrm{Ext}}^\bullet({\mathscr E},{\mathscr F})$. Moreover, if ${\mathbf R}\pi_*\colon
  \mathbf{D}(X)\to \mathbf{D}({\mathsf{pt}})$ is the derived functor coming from the map $X\to
  {\mathsf{pt}}$, then $$\mathop{\mathrm{Ext}}^\bullet({\mathscr E},{\mathscr F})\cong
  \mathsf H^\bullet(X,{\mathscr E}^{\scriptscriptstyle\vee}\otimes{\mathscr F})\cong {\mathbf R}\pi_*({\mathscr E}^{\scriptscriptstyle\vee}\otimes{\mathscr F})$$ and the latter is just the composition ${\mathscr E}^{\scriptscriptstyle\vee}\circ {\mathscr F}$, where ${\mathscr E}^{\scriptscriptstyle\vee}$ and ${\mathscr F}$ are considered as kernels respectively $X\to
  {\mathsf{pt}}$ and ${\mathsf{pt}}\to X$. Thus, using the invariance of the Serre trace under the partial trace map, $$\begin{aligned}
    \chi({\mathscr E},{\mathscr F})&=\mathop{\mathrm{Tr}}(\mathsf {Id}_{{\mathscr E}^{\scriptscriptstyle\vee}\circ {\mathscr F}})
    =\mathop{\mathrm{Tr}}\left(\raisebox{-.45\height}{}\right)
    =\mathop{\mathrm{Tr}}\left(\raisebox{-.45\height}{}\right)\\&={\ensuremath{\Biggl\langle \raisebox{-.45\height}{},\, \raisebox{-.45\height}{}\Biggr\rangle_{\rm M}}}
    ={\ensuremath{\left\langle \mathop{\mathrm{ch}}({\mathscr E}),\, \mathop{\mathrm{ch}}({\mathscr F})\right\rangle_{\rm M}}}.\qedhere
  
\end{aligned}$$
:::
