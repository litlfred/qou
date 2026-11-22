---
doc_id: arxiv-0707.3799v3
doc_title: "Equivariant Satake category and Kostant-Whittaker reduction"
section_id: sec-018-47-quasiclassical-limit-of-ϕv
section_title: "Quasiclassical limit of ϕ(V )"
section_number: 4.7
pages: 19-19
source_pdf: 0707.3799v3.pdf
source_sha256: 0b29cbced7939f72
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.955
doc_brief: "Equivariant Satake category and Kostant-Whittaker reduction — 24 sections: Front matter; Introduction; Notation and statements of the res"
---
[]{#secr label="secr"} For $V\in Rep({\check{G}})$, Lemma [\[Mit\]](#Mit){reference-type="ref" reference="Mit"} implies that the ${\mathcal O}(\check{\mathfrak t}{}^*/W)$-bimodule $\phi(V)$ is supported at the diagonal $\Delta\subset\check{\mathfrak t}{}^*/W\times\check{\mathfrak t}{}^*/W$. It follows that the action of ${\mathcal O}(\check{\mathfrak t}{}^*/W\times\check{\mathfrak t}{}^*/W\times{\mathbb A}^1)$ on $\phi(V)$ actually extends to the action of ${\mathcal O}(N_{\check{\mathfrak t}{}^*/W\times\check{\mathfrak t}{}^*/W}\Delta)$. As we know from [\[quasic\]](#quasic){reference-type="ref" reference="quasic"}, ${\mathcal O}(N_{\check{\mathfrak t}{}^*/W\times\check{\mathfrak t}{}^*/W}\Delta)/\hbar\simeq{\mathcal O}(\bT(\check{\mathfrak t}{}^*/W))$ is the universal centralizer.

::: lem
[]{#MIt label="MIt"} For $V\in Rep({\check{G}})$, the ${\mathcal O}(\bT(\check{\mathfrak t}{}^*/W))$-module $\phi(V)|_{\hbar=0}$ is canonically isomorphic to the module ${\mathcal O}(\Sigma)\otimes V$ over the universal centralizer.
:::

*Proof* : Consider the ${\mathcal O}(\check{\mathfrak g}{}^*)^{{\check{G}}}$-module $Pol(\check{\mathfrak g}{}^*,\check{\mathfrak g}{})^{{\check{G}}}$ of ${\check{G}}$-invariant polynomial maps from $\check{\mathfrak g}{}^*$ to $\check{\mathfrak g}{}$; this is a vector bundle over $Spec{\mathcal O}(\check{\mathfrak g}{}^*)^{{\check{G}}}=\Sigma$. Given a polynomial $P\in{\mathcal O}(\check{\mathfrak g}{}^*)^{{\check{G}}}$, its differential $dP$ defines a section of this vector bundle. For a central element $z\in Z(U(\check{\mathfrak g}{}))={\mathcal O}(\check{\mathfrak g}{}^*)^{{\check{G}}}$ we denote the corresponding section by $\sigma_z$. If $z$ runs through a set of generators of $Z(U(\check{\mathfrak g}{}))$, the corresponding sections $\sigma_z$ form a basis of the universal centralizer bundle, and identify it with the cotangent bundle $\bT^*(\Sigma)$.

Thus it suffices to check the following statement about the free $\hbar$-Harish-Chandra bimodule $U_\hbar\otimes V$. Let $z^{(1)}$ (resp. $z^{(2)}$) stand for the left (resp. right) action of $z$ in $U_\hbar\otimes V$. Then the action of $\frac{z^{(1)}-z^{(2)}}{\hbar}|_{\hbar=0}$ on $(U_\hbar\otimes V)|_{\hbar=0}=
{\mathcal O}(\check{\mathfrak g}{}^*)\otimes V$ coincides with the action of $\sigma_z\in
{\mathcal O}(\check{\mathfrak g}{}^*)\otimes\check{\mathfrak g}{}$.

In effect, if $v\in V$, and $z=\sum_{\underline{i}} 
a_{\underline{i}}x_{i_1}\ldots x_{i_k}$ where $x_{i_l}\in\check{\mathfrak g}{}$, and $\tilde{y}\in U_\hbar$ is a lift of $y\in{\mathcal O}(\check{\mathfrak g}{}^*)=U_\hbar|_{\hbar=0}$, then $\frac{z(\tilde{y}\otimes v)-(\tilde{y}\otimes v)z}{\hbar}|_{\hbar=0}=
\sum_{i_l\in\underline{i}}
a_{\underline{i}}x_{i_1}\ldots\widehat{x_{i_l}}\ldots 
x_{i_k}y\otimes x_{i_l}(v)=\sigma_z(y\otimes v)$.

The lemma is proved. $\Box$

# Rank 1
