---
doc_id: arxiv-0707.3799v3
doc_title: "Equivariant Satake category and Kostant-Whittaker reduction"
section_id: sec-017-47-quasiclassical-limit-of-ϕv
section_title: "Quasiclassical limit of ϕ(V )"
section_number: 4.7
pages: 19-20
source_pdf: 0707.3799v3.pdf
source_sha256: 0b29cbced7939f72
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.706
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

## Equivariant cohomology for $G=PGL(2)$ {#before}

Let us describe $H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,S(V))$ in the case $G=PGL(2)$. Then ${\check{G}}$ is isomorphic to $SL(2)$. For a positive integer $n$ let $V_n$ be the $n+1$-dimensional irreducible $SL(2)$-module. Let $\Gr_n$ be the closure of the $n$-dimensional ${\bf G_O}$-orbit in $\Gr_G$. It is known that $\Gr_n$ is rationally smooth, so we are interested in $H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_n)$ as a module over $H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr)$. The non-equivariant cohomology $H^\bullet(\Gr_n)$ is a cyclic $H^\bullet(\Gr)$-module (see e.g. [@G1]). Hence, by graded Nakayama lemma, $H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_n)$ is a cyclic module over $H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr)$. Recall that $H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr)\cong{\mathcal O}(N_{{\frak t}/W\times{\frak t}/W}\Delta)\oplus
{\mathcal O}(N_{{\frak t}/W\times{\frak t}/W}\Delta)$, and so $H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_n)$ is the structure sheaf of a subscheme $A_n\subset N_{{\frak t}/W\times{\frak t}/W}\Delta$ of a copy of $N_{{\frak t}/W\times{\frak t}/W}\Delta$ specified by the parity of $n$.

Now we describe the subscheme $A_n$. Let $P_n=\{n\omega,(n-2)\omega,\ldots,
(2-n)\omega,-n\omega\}$ be the set of weights of ${\check{G}}$-module $V_n$. We have $P_n\subset{\frak t}=\check{\mathfrak t}{}^*$. For $i=-n,-n+2,\ldots,n-2,n$, let $\Gamma_i\subset{\frak t}\times{\frak t}\times{\mathbb A}^1$ be a subscheme defined by the equations $\Gamma_i=\{(x_1,x_2,a):\
x_2=x_1+ia\omega\}$. Let $\Gamma(n)$ stand for the subscheme defined by the product of the above equations (over $i=-n,-n+2,\ldots,n-2,n$). Recall that $\pi$ stands for the projection ${\frak t}\to{\frak t}/W$, and consider the subscheme $(\pi,\pi,\Id)(\Gamma(n))\subset{\frak t}/W\times{\frak t}/W\times{\mathbb A}^1$. Finally, we can formulate

::: lem
[]{#top label="top"} $A_n$ is the proper preimage of $(\pi,\pi,\Id)(\Gamma(n))$ in $N_{{\frak t}/W\times{\frak t}/W}\Delta$.
:::

*Proof* : Since $H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}$ is a flat ${\mathcal O}({\frak t}/W\times{\mathbb A}^1)$-module, it suffices to identify $A_n$ with $(\pi,\pi,\Id)(\Gamma(n))$ generically over ${\frak t}/W\times{\mathbb A}^1$, or else to identify $(\pi,\Id,\Id)^{-1}(A_n)$ with $(\Id,\pi,\Id)(\Gamma(n))$ generically over ${\frak t}\times{\mathbb A}^1$. This was done in Lemma [\[Harvard\]](#Harvard){reference-type="ref" reference="Harvard"}. $\Box$
