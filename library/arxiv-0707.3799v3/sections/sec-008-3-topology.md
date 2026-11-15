---
doc_id: arxiv-0707.3799v3
doc_title: "Equivariant Satake category and Kostant-Whittaker reduction"
section_id: sec-008-3-topology
section_title: "Topology"
section_number: 3
pages: 8-10
source_pdf: 0707.3799v3.pdf
source_sha256: 0b29cbced7939f72
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.691
doc_brief: "Equivariant Satake category and Kostant-Whittaker reduction — 24 sections: Front matter; Introduction; Notation and statements of the res"
---
## Proof of Theorem [\[normocon\]](#normocon){reference-type="ref" reference="normocon"}

a\) First we construct the morphism $\alpha:\
{\mathcal O}(N_{\check{\mathfrak t}{}^*/W\times \check{\mathfrak t}{}^*/W}\Delta)\to H^\bullet_{{\bf G_O}\rtimes {{\mathbb G}_m}}(\Gr)$. Recall that $H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr)=
H^\bullet_{{{\mathbb G}_m}}({\bf G_O}\backslash{\bf G_F}/{\bf G_O})$, whence two morphisms $pr_1^*, pr_2^*:\ {\mathcal O}({\frak t}/W)=H^\bullet_{\bf G_O}(pt)\to
H^\bullet_{{\bf G_O}\rtimes {{\mathbb G}_m}}(\Gr)$. We also have a morphism $pr^*:\ \mathsf k[\hbar]=H^\bullet_{{\mathbb G}_m}(pt)\to
H^\bullet_{{\bf G_O}\rtimes {{\mathbb G}_m}}(\Gr)$. Since $H^\bullet_{{\bf G_O}\rtimes {{\mathbb G}_m}}(\Gr)|_{\hbar=0}=
H^\bullet_{\bf G_O}(\Gr)$, it follows that $pr_1^*|_{\hbar=0}=pr_2^*|_{\hbar=0}$. Hence the morphism $(pr_1^*,pr_2^*,pr^*):\ {\mathcal O}({\frak t}/W\times{\frak t}/W\times{\mathbb A}^1)\to
H^\bullet_{{\bf G_O}\rtimes {{\mathbb G}_m}}(\Gr)$ factors through the desired morphism ${\mathcal O}({\frak t}/W\times{\frak t}/W\times{\mathbb A}^1)\to
{\mathcal O}(N_{{\frak t}/W\times {\frak t}/W}\Delta)\overset{\alpha}{\to} 
H^\bullet_{{\bf G_O}\rtimes {{\mathbb G}_m}}(\Gr)$.

Next we prove that $\alpha$ is an embedding. It suffices to prove that the localized morphism $$\alpha_{loc}:\ 
{\mathcal O}(N_{{\frak t}/W\times {\frak t}/W}\Delta)\otimes_{{\mathcal O}({\frak t}/W\times{\mathbb A}^1)}
\operatorname{Frac}({\mathcal O}({\frak t}\times{\mathbb A}^1))
\to H^\bullet_{{\bf G_O}\rtimes {{\mathbb G}_m}}(\Gr)\otimes_{{\mathcal O}({\frak t}/W\times{\mathbb A}^1)}
\operatorname{Frac}({\mathcal O}({\frak t}\times{\mathbb A}^1))$$ is an embedding. Note that the RHS is the localized equivariant cohomology $H^\bullet_{T\times{{\mathbb G}_m}}(\Gr)_{loc}$, which embeds into the inverse limit of the localized equivariant cohomology $H^\bullet_{T\times{{\mathbb G}_m}}(\Gr_\lambda)_{loc}$ of the ${\bf G_O}$-orbit closures $\Gr_\lambda\subset\Gr$. By the Localization Theorem for torus-equivariant cohomology, the latter is $\prod_\lambda\operatorname{Frac}({\mathcal O}({\frak t}\times{\mathbb A}^1))$ (cf. [\[can\]](#can){reference-type="ref" reference="can"}), and $\alpha_{loc}$ is an embedding.

Finally, it remains to check that the graded dimensions of $H^\bullet_{{\bf G_O}\rtimes {{\mathbb G}_m}}(\Gr)$, and of ${\mathcal O}(N_{{\frak t}/W\times {\frak t}/W}\Delta)$ coincide. Here the grading of ${\mathcal O}(N_{{\frak t}/W\times {\frak t}/W}\Delta)$ comes from the natural ${{\mathbb G}_m}$-actions on ${\frak t}$ and ${\mathbb A}^1$. To this end note that the graded dimension of $H^\bullet_{{\bf G_O}\rtimes {{\mathbb G}_m}}(\Gr)$ coincides with that of $H^\bullet_{\bf G_O}(pt)\otimes H^\bullet_{{\mathbb G}_m}(pt)\otimes H^\bullet(\Gr)$, that is $\mathsf k[x_1,\ldots,x_r,y_1,\ldots,y_r,\hbar]$. Here $r$ is the rank of $G$; the degree of $\hbar$ is 2; the degrees of $x$'s are twice the exponents of $\check{\mathfrak g}{}$; the degrees of $y$'s are twice the exponents of $\check{\mathfrak g}{}$ minus 2.

Now to compute the graded dimension of ${\mathcal O}(N_{{\frak t}/W\times {\frak t}/W}\Delta)$ we use that ${\frak t}/W$ is isomorphic to the vector space $\Sigma$. More generally, for vector spaces $V,V'$ we have an isomorphism $\beta: V\times V'\times{\mathbb A}^1{\stackrel{\sim}{\longrightarrow}}N_{V\times V'}V$. In effect, the map $\gamma: V\times V'\times{\mathbb A}^1\to V\times V'\times{\mathbb A}^1,\
(v,v',a)\mapsto(v,av',a)$, factors through the desired isomorphism: $V\times V'\times{\mathbb A}^1\overset{\beta}{\to}N_{V\times V'}V\to 
V\times V'\times{\mathbb A}^1$. We derive an isomorphism $N_{{\frak t}/W\times{\frak t}/W}\Delta\cong{\frak t}/W\times{\frak t}/W\times{\mathbb A}^1$ which lowers the ${{\mathbb G}_m}$-weights in the second copy of ${\frak t}/W$ by 1, whence the desired formula for the graded dimension of ${\mathcal O}(N_{{\frak t}/W\times{\frak t}/W}\Delta)$.

This completes the proof of the part a) of the theorem.

b)[^1] For a general $G$ (not necessarily simply connected), we will describe $H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr)$ as $W$-invariants in $H^\bullet_{T\times{{\mathbb G}_m}}(\Gr_G)$. First we describe the equivariant cohomology ring $H^\bullet_{T\times{{\mathbb G}_m}}(\Gr_{G^{\on{sc}}})$ of the neutral connected component of $\Gr_G$. To this end we consider the affinized Cartan subalgebra ${\frak t}_{\on{aff}}={\frak t}\times\BA^1$ (with extra coordinate $\hbar$) with its natural projection to $\BA^1$. Let $\Gamma\subset{\frak t}_{\on{aff}}\times_{\BA^1}({\frak t}_{\on{aff}}/W)$ be the graph of the projection ${\frak t}_{\on{aff}}\to{\frak t}_{\on{aff}}/W$ (note that the action of $W$ is trivial on $\BA^1$). The argument in the proof of a) shows that $H^\bullet_{T\times{{\mathbb G}_m}}(\Gr_{G^{\on{sc}}})={\mathcal O}\left(\on{Bl}^{\on{aff}}_\Gamma({\frak t}_{\on{aff}}\times_{\BA^1}({\frak t}_{\on{aff}}/W))\right)$. Note that the RHS has a natural $W$-action. Taking $W$-invariants, we reproduce the answer in a): $H^\bullet_{{\mathbf G}^{\on{sc}}_{\mathbf O} \rtimes {{\mathbb G}_m}}(\Gr_{G^{\on{sc}}})\cong
\Big({\mathcal O}\left(\on{Bl}^{\on{aff}}_\Gamma({\frak t}_{\on{aff}}\times_{\BA^1}({\frak t}_{\on{aff}}/W))\right)\Big)^W\cong{\mathcal O}(N_{\check{\mathfrak t}{}^*/W\times \check{\mathfrak t}{}^*/W}\Delta)$.

For a general $G$, the coweight lattice $\Lambda=X_*(T)$ contains the coroot lattice $Q$. We have a natural action of $\Lambda$ on ${\frak t}_{\on{aff}}$ : $\lambda(x,c\hbar)=(x+c\lambda,c\hbar)$, compatible with the action of $W$ on $\Lambda$ and on ${\frak t}_{\on{aff}}$. Thus we obtain an action of $\Lambda$ on ${\mathcal O}\left(\on{Bl}^{\on{aff}}_\Gamma({\frak t}_{\on{aff}}\times_{\BA^1}({\frak t}_{\on{aff}}/W))\right)$. In particular, the coroot lattice $Q\subset\Lambda$ acts. We will show that $H^\bullet_{T\times{{\mathbb G}_m}}(\Gr_G)\cong\mathsf k[\Lambda]\otimes_{\mathsf k[Q]}
{\mathcal O}\left(\on{Bl}^{\on{aff}}_\Gamma({\frak t}_{\on{aff}}\times_{\BA^1}({\frak t}_{\on{aff}}/W))\right)\cong\bigoplus_{\pi_1(G)}
{\mathcal O}\left(\on{Bl}^{\on{aff}}_\Gamma({\frak t}_{\on{aff}}\times_{\BA^1}({\frak t}_{\on{aff}}/W))\right)$ (note that $\pi_1(G)=\Lambda/Q$). It will follow that $H^*_{{\bf G_O}\rtimes {{\mathbb G}_m}}(\Gr_G)\cong\Big(\mathsf k[\Lambda]\otimes_{\mathsf k[Q]}{\mathcal O}\left(\on{Bl}^{\on{aff}}_\Gamma({\frak t}_{\on{aff}}\times_{\BA^1}({\frak t}_{\on{aff}}/W))\right)\Big)^W\cong\bigoplus_{\pi_1(G)}{\mathcal O}(N_{\check{\mathfrak t}{}^*/W\times \check{\mathfrak t}{}^*/W}\Delta)$.

Let $G^{\mathrm{sc}}$ stand for the simply connected cover of $G$. Then the Grassmannian $\Gr_G$ is a union of connected components indexed by $\chi\in\Lambda/Q$, and each connected component is isomorphic to $\Gr_{G^{\mathrm{sc}}}$. More precisely, we have a natural action of the coweight lattice $\Lambda=X_*(T)\subset{\mathbf G}_{\mathbf F}$ on $\Gr_G$. Let us pick a coweight $\lambda\in\Lambda$ sending the neutral component $\Gr_{G^{\mathrm{sc}}}$ to another component $\Gr_G^\chi$. Then we can $W$-equvariantly identify $H^\bullet_{T\times{{\mathbb G}_m}}(\Gr_{G^{\mathrm{sc}}})$ with $H^\bullet_{T\times{{\mathbb G}_m}}(\Gr_G^\chi)$ in the following way. The desired identification is the composition of the isomorphism induced by (the shift by) $\lambda$ on $\Gr_G$, with the inverse of the action of $\lambda$ on $\on{Bl}^{\on{aff}}_\Gamma({\frak t}_{\on{aff}}\times_{\BA^1}({\frak t}_{\on{aff}}/W))$. It is easy to see that the resulting isomorphism is independent of the choice of $\lambda$ and hence it is $W$-equivariant.

Now $H^\bullet_{T\times{{\mathbb G}_m}}(\Gr_G)$ is equal to $\bigoplus_{\chi\in\Lambda/Q}H^\bullet_{T\times{{\mathbb G}_m}}(\Gr_G^\chi)$. Finally, $H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G)=H^\bullet_{G\times{{\mathbb G}_m}}(\Gr_G)$ coincides with the $W$-invariants in $H^\bullet_{T\times{{\mathbb G}_m}}(\Gr_G)$. $\Box$

[^1]: The proof of this part of the Theorem in the published version contained a mistake, here we present a corrected proof. We thank Jakub Löwit for pointing out the issue.
