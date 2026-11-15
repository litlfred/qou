---
doc_id: arxiv-0707.3799v3
doc_title: "Equivariant Satake category and Kostant-Whittaker reduction"
section_id: sec-010-34-transitivity-for-a-pair-of-levi-subgroups
section_title: "Transitivity for a pair of Levi subgroups"
section_number: 3.4
pages: 11-11
source_pdf: 0707.3799v3.pdf
source_sha256: 0b29cbced7939f72
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.968
doc_brief: "Equivariant Satake category and Kostant-Whittaker reduction — 24 sections: Front matter; Introduction; Notation and statements of the res"
---
[]{#toppair label="toppair"} We have a canonical isomorphism $^{\operatorname{top}}\Xi_L:\ 
gr(\pi_L,\Id,\Id)^*H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,S(V))
{\stackrel{\sim}{\longrightarrow}}(\Id,\pi_L,\Id)_*
H^\bullet_{L({\mathbf O})\rtimes{{\mathbb G}_m}}(\Gr_L,S_L(V|_{\check{L}{}}))$. In the RHS we have the restriction of ${\mathcal O}({\frak t}/W_L\times{\frak t}/W_L\times{\mathbb A}^1)$-module $H^\bullet_{L({\mathbf O})\rtimes{{\mathbb G}_m}}(\Gr_L,S_L(V|_{\check{L}{}}))$ to ${\mathcal O}({\frak t}/W_L\times{\frak t}/W\times{\mathbb A}^1)$. To save a bit of notation in what follows we will write simply $$^{\operatorname{top}}\Xi_L:\ 
gr(\pi_L,\Id,\Id)^*H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,S(V))
{\stackrel{\sim}{\longrightarrow}}H^\bullet_{L({\mathbf O})\rtimes{{\mathbb G}_m}}(\Gr_L,S_L(V|_{\check{L}{}})).$$

If $\check{T}{}\subset\check{L}{}'\subset\check{L}{}$ is another Levi subgroup, then we denote by $\pi_{L'}^L$ the projection from ${\frak t}/W_{L'}$ to ${\frak t}/W_L$. Note that the filtration $F_{L'}^\bullet$ on $(\pi_{L'},\Id,\Id)^*H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,S(V))=
(\pi_{L'}^L,\Id,\Id)^*(\pi_L,\Id,\Id)^*H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,S(V))$ is a refinement of the filtration $(\pi_{L'}^L,\Id,\Id)^*F_L^\bullet$, and hence induces a canonical filtration $F_{L'}^{L\bullet}$ on $(\pi_{L'}^L,\Id,\Id)^*gr_{F_L^\bullet}(\pi_L,\Id,\Id)^*
H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,S(V))$. The isomorphism $(\pi_{L'}^L,\Id,\Id)^*\ ^{\operatorname{top}}\Xi_L$ carries the filtration $F_{L'}^{L\bullet}$ to the filtration $F_{L'}^\bullet$ on $(\pi_{L'}^L,\Id,\Id)^*
H^\bullet_{L({\mathbf O})\rtimes{{\mathbb G}_m}}(\Gr_L,S_L(V|_{\check{L}{}}))$. We have a canonical isomorphism $\ ^{\operatorname{top}}\Xi_{L'}^L:\ gr_{F_{L'}^\bullet}(\pi_{L'}^L,\Id,\Id)^*
H^\bullet_{L({\mathbf O})\rtimes{{\mathbb G}_m}}(\Gr_L,S_L(V|_{\check{L}{}})){\stackrel{\sim}{\longrightarrow}}
H^\bullet_{L'({\mathbf O})\rtimes{{\mathbb G}_m}}(\Gr_{L'},S_{L'}(V|_{\check{L}{}'}))$. We consider the composition $$\begin{CD} 
gr_{F_{L'}^\bullet}(\pi_{L'},\Id,\Id)^*H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,S(V))
@>gr_{F_{L'}^{L\bullet}}(\pi_{L'}^L,\Id,\Id)^*\ ^{\operatorname{top}}\Xi_L>>
\end{CD}$$ $$\begin{CD}
gr_{F_{L'}^\bullet}(\pi_{L'}^L,\Id,\Id)^*
H^\bullet_{L({\mathbf O})\rtimes{{\mathbb G}_m}}(\Gr_L,S_L(V|_{\check{L}{}}))
@>\ ^{\operatorname{top}}\Xi_{L'}^L>>
H^\bullet_{L'({\mathbf O})\rtimes{{\mathbb G}_m}}(\Gr_{L'},S_{L'}(V|_{\check{L}{}'}))
\end{CD}$$ Then we have

::: lem
[]{#tp label="tp"} $^{\operatorname{top}}\Xi_{L'}^L\circ gr_{F_{L'}^{L\bullet}}
(\pi_{L'}^L,\Id,\Id)^*\ ^{\operatorname{top}}\Xi_L=\ 
^{\operatorname{top}}\Xi_{L'}$.
:::

$\Box$
