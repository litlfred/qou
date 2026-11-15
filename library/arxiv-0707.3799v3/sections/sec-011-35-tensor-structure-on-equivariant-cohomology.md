---
doc_id: arxiv-0707.3799v3
doc_title: "Equivariant Satake category and Kostant-Whittaker reduction"
section_id: sec-011-35-tensor-structure-on-equivariant-cohomology
section_title: "Tensor structure on equivariant cohomology"
section_number: 3.5
pages: 11-14
source_pdf: 0707.3799v3.pdf
source_sha256: 0b29cbced7939f72
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.934
doc_brief: "Equivariant Satake category and Kostant-Whittaker reduction — 24 sections: Front matter; Introduction; Notation and statements of the res"
---
[]{#tenscoh label="tenscoh"} A ${\bf G_O}\rtimes{{\mathbb G}_m}$-equivariant sheaf $\CF$ on $\Gr_G$ will be viewed as a sheaf on the stack ${\bf G_O}\rtimes{{\mathbb G}_m}\backslash{\bf G_F}\rtimes{{\mathbb G}_m}/{\bf G_O}\rtimes{{\mathbb G}_m}$. Given two such sheaves $\CF_1,\CF_2$ we define $\CF_1\boxtimes_{{\bf G_O}\rtimes{{\mathbb G}_m}}\CF_2$ as the descent of $\CF_1\boxtimes\CF_2$ from $$\left({\bf G_O}\rtimes{{\mathbb G}_m}\backslash{\bf G_F}\rtimes{{\mathbb G}_m}/{\bf G_O}\rtimes{{\mathbb G}_m}\right)\times
\left({\bf G_O}\rtimes{{\mathbb G}_m}\backslash{\bf G_F}\rtimes{{\mathbb G}_m}/{\bf G_O}\rtimes{{\mathbb G}_m}\right)$$ to ${\bf G_O}\rtimes{{\mathbb G}_m}\backslash({\bf G_F}\rtimes{{\mathbb G}_m}\times_{{\bf G_O}\rtimes{{\mathbb G}_m}}{\bf G_F}\rtimes{{\mathbb G}_m})/
{\bf G_O}\rtimes{{\mathbb G}_m}$. Clearly, $$H^\bullet(
{\bf G_O}\rtimes{{\mathbb G}_m}\backslash({\bf G_F}\rtimes{{\mathbb G}_m}\times_{{\bf G_O}\rtimes{{\mathbb G}_m}}{\bf G_F}\rtimes{{\mathbb G}_m})/
{\bf G_O}\rtimes{{\mathbb G}_m},\CF_1\boxtimes_{{\bf G_O}\rtimes{{\mathbb G}_m}}\CF_2)=$$ $$H^\bullet({\bf G_O}\rtimes{{\mathbb G}_m}\backslash{\bf G_F}\rtimes{{\mathbb G}_m}/{\bf G_O}\rtimes{{\mathbb G}_m},\CF_1)
\otimes_{H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(pt)}
H^\bullet({\bf G_O}\rtimes{{\mathbb G}_m}\backslash{\bf G_F}\rtimes{{\mathbb G}_m}/{\bf G_O}\rtimes{{\mathbb G}_m},\CF_2)=$$ $$H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,\CF_1)\otimes_{{\mathcal O}({\frak t}/W\times{\mathbb A}^1)}
H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,\CF_2)=:
H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,\CF_1)\star
H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,\CF_2).$$ The multiplication in ${\bf G_F}\rtimes{{\mathbb G}_m}$ gives rise to the map $$m:\ {\bf G_O}\rtimes{{\mathbb G}_m}\backslash({\bf G_F}\rtimes{{\mathbb G}_m}\times_{{\bf G_O}\rtimes{{\mathbb G}_m}}
{\bf G_F}\rtimes{{\mathbb G}_m})/
{\bf G_O}\rtimes{{\mathbb G}_m}\to{\bf G_O}\rtimes{{\mathbb G}_m}\backslash{\bf G_F}\rtimes{{\mathbb G}_m}/{\bf G_O}\rtimes{{\mathbb G}_m}.$$ The convolution $\CF_1*\CF_2$ is defined as $m_*(\CF_1\boxtimes_{{\bf G_O}\rtimes{{\mathbb G}_m}}\CF_2)$. Hence $$H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,\CF_1*\CF_2)=
H^\bullet({\bf G_O}\rtimes{{\mathbb G}_m}\backslash{\bf G_F}\rtimes{{\mathbb G}_m}/{\bf G_O}\rtimes{{\mathbb G}_m},\CF_1*\CF_2)=$$ $$H^\bullet(
{\bf G_O}\rtimes{{\mathbb G}_m}\backslash({\bf G_F}\rtimes{{\mathbb G}_m}\times_{{\bf G_O}\rtimes{{\mathbb G}_m}}{\bf G_F}\rtimes{{\mathbb G}_m})/
{\bf G_O}\rtimes{{\mathbb G}_m},\CF_1\boxtimes_{{\bf G_O}\rtimes{{\mathbb G}_m}}\CF_2)=$$ $$H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,\CF_1)\star
H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,\CF_2).$$ Now for $V_1,V_2\in Rep({\check{G}})$, and $\CF_1=S(V_1),\ \CF_2=S(V_2)$ we have a canonical isomorphism $S(V_1\otimes V_2){\stackrel{\sim}{\longrightarrow}}S(V_1)*S(V_2)$, and thus $$\ ^{\operatorname{top}}\omega_{V_1,V_2}:\ 
H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,S(V_1\otimes V_2)){\stackrel{\sim}{\longrightarrow}}
H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,S(V_1))\star
H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,S(V_2)).$$ According to Lemma [\[Harvard\]](#Harvard){reference-type="ref" reference="Harvard"} (cf. also Lemma [\[Chicago\]](#Chicago){reference-type="ref" reference="Chicago"}), we have a canonical isomorphism $$^{\operatorname{top}}\Xi_V=\ ^{\operatorname{top}}\Xi_{T,V}:\ 
gr(\pi,\Id,\Id)^*H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,S(V)){\stackrel{\sim}{\longrightarrow}}
(\Id,\pi,\Id)_*H^\bullet_{T\times{{\mathbb G}_m}}(\Gr_T,S_T(V|_{\check{T}{}})).$$ In the RHS we have the restriction of ${\mathcal O}({\frak t}\times{\frak t}\times{\mathbb A}^1)$-module $H^\bullet_{T\times{{\mathbb G}_m}}(\Gr_T,
S_T(V|_{\check{T}{}}))$ to ${\mathcal O}({\frak t}\times({\frak t}/W)\times{\mathbb A}^1)$. To save a bit of notation in what follows we will write simply $\ ^{\operatorname{top}}\Xi_V:\ 
gr(\pi,\Id,\Id)^*H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,S(V)){\stackrel{\sim}{\longrightarrow}}
H^\bullet_{T\times{{\mathbb G}_m}}(\Gr_T,S_T(V|_{\check{T}{}}))$. It follows that after tensoring with $\mathsf k({\frak t}\times{\mathbb A}^1)$ (over the first and third factors in ${\mathcal O}({\frak t}/W\times{\frak t}/W\times{\mathbb A}^1)$) we have a canonical isomorphism $$\ ^{\operatorname{top}}\Xi_V^\gen:\ H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,S(V))
\otimes_{{\mathcal O}({\frak t}/W\times{\mathbb A}^1)}\mathsf k({\frak t}\times{\mathbb A}^1)=$$ $$=gr(\pi,\Id,\Id)^*H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,S(V))
\otimes_{{\mathcal O}({\frak t}\times{\mathbb A}^1)}\mathsf k({\frak t}\times{\mathbb A}^1){\stackrel{\sim}{\longrightarrow}}$$ $${\stackrel{\sim}{\longrightarrow}}H^\bullet_{T\times{{\mathbb G}_m}}(\Gr_T,S_T(V|_{\check{T}{}}))
\otimes_{{\mathcal O}({\frak t}\times{\mathbb A}^1)}\mathsf k({\frak t}\times{\mathbb A}^1)=
\bigoplus_\lambda\left({\mathcal O}(\Gamma_\lambda)
\otimes_{{\mathcal O}({\frak t}\times{\mathbb A}^1)}\mathsf k({\frak t}\times{\mathbb A}^1)\right)\otimes\ 
_\lambda V$$ Now we have a canonical isomorphism ${\mathcal O}(\Gamma_\mu)\star{\mathcal O}(\Gamma_\nu):={\mathcal O}(\Gamma_\mu)
\otimes_{{\mathcal O}({\frak t}\times{\mathbb A}^1)}{\mathcal O}(\Gamma_\nu)={\mathcal O}(\Gamma_{\mu+\nu})$. Hence we get a canonical isomorphism $$\ ^{\operatorname{top}}\Xi_{V_1}^\gen\star\ 
^{\operatorname{top}}\Xi_{V_2}^\gen:\
(H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,S(V_1))\star
H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,S(V_2))) 
\otimes_{{\mathcal O}({\frak t}/W\times{\mathbb A}^1)}\mathsf k({\frak t}\times{\mathbb A}^1){\stackrel{\sim}{\longrightarrow}}$$ $${\stackrel{\sim}{\longrightarrow}}\bigoplus_{\mu+\nu=\lambda}\left({\mathcal O}(\Gamma_\lambda)
\otimes_{{\mathcal O}({\frak t}\times{\mathbb A}^1)}\mathsf k({\frak t}\times{\mathbb A}^1)\right)\otimes\
_\mu V_1\otimes\ _\nu V_2=$$ $$=\bigoplus_\lambda\left({\mathcal O}(\Gamma_\lambda)
\otimes_{{\mathcal O}({\frak t}\times{\mathbb A}^1)}\mathsf k({\frak t}\times{\mathbb A}^1)\right)\otimes\
_\lambda(V_1\otimes V_2)$$ We want to compare it with $\ ^{\operatorname{top}}\Xi_{V_1\otimes V_2}^\gen:$ $$H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G,
S(V_1\otimes V_2))\otimes_{{\mathcal O}({\frak t}/W\times{\mathbb A}^1)}\mathsf k({\frak t}\times{\mathbb A}^1)
{\stackrel{\sim}{\longrightarrow}}\bigoplus_\lambda\left({\mathcal O}(\Gamma_\lambda)
\otimes_{{\mathcal O}({\frak t}\times{\mathbb A}^1)}\mathsf k({\frak t}\times{\mathbb A}^1)\right)\otimes\
_\lambda(V_1\otimes V_2)$$

::: prop
[]{#tenstop label="tenstop"} $^{\operatorname{top}}\Xi_{V_1\otimes V_2}^\gen=
(\ ^{\operatorname{top}}\Xi_{V_1}^\gen\star\ 
^{\operatorname{top}}\Xi_{V_2}^\gen)
\circ\ ^{\operatorname{top}}\omega_{V_1,V_2}$.
:::

*Proof* : The equality readily reduces to the following compatibility. Let $\Phi_{MV}=\bigoplus\limits_\lambda\Phi_{MV}^\lambda :\CF\mapsto \bigoplus\limits_\lambda 
\fj_\lambda^*\imath_\lambda^!\CF$ be the Mirković-Vilonen fiber functor on the Satake category $Perv_{{\bf G_O}}(\Gr)$ (notations of [\[can\]](#can){reference-type="ref" reference="can"}, see [@MV]). The (proof of) Lemma 1 provides a canonical isomorphism $$\label{isoten}
gr(H^\bullet_{T\times {{\mathbb G}_m}}(Gr_G,\F) )\cong \bigoplus\limits
\Phi_{MV}^\lambda\otimes \CO(\Gamma_\lambda).$$ We have to check that this isomorphism is compatible with the tensor structure, i.e. for $\CF,\CG\in Perv_{{\bf G_O}}(\Gr)$ we have to check coincidence of the two embeddings from $\Phi_{MV}(\CF)\otimes \Phi_{MV}(\CG)$ in $gr(H^\bullet_{T\times {{\mathbb G}_m}}(Gr_G,\F*\CG) )$, where the first one comes from the isomorphisms [\[isoten\]](#isoten){reference-type="eqref" reference="isoten"} for $\CF$, $\CG$ and tensor structure on the functor $gr(H^\bullet_{T\times {{\mathbb G}_m}})$, and the second one comes from the tensor structure on the functor $\Phi_{MV}$ and isomorphism [\[isoten\]](#isoten){reference-type="eqref" reference="isoten"} for $\CF*\CG$.

To check the equality, we recall a "filtration" in the $I$-equivariant derived category on a ${\bf G_O}$ equivariant perverse sheaf $\F$, which induces the above filtration on $H^\bullet_{T\times {{\mathbb G}_m}}(Gr_G,\F)$. Here and below by a "filtration" on an object $X$ of a triangulated category we mean a collection of object $X_0=0,\dots, X_n=X$ and distinguished triangles $X_i\to X_{i+1} \to Y_i$; the objects $Y_i$ will be called the "subquotients" of the filtration.

Let $\CalC$, $\CalD$ be the equivariant constructible derived category with respect to the natural action of ${\bf I}\rtimes{{\mathbb G}_m}$ on $\Gr_G$ and on $\Fl_G$ respectively. Thus convolution $*_I$ provides $\CalD$ with a monoidal structure, and $\CalC$ with an action of the monoidal category $\CalD$.

Recall the *Wakimoto sheaves* $J_\lambda\in \CalD$, characterized by the following properties: $J_{\lambda+\mu}\cong J_\lambda*_I J_\mu$, while for a dominant weight $\lambda\in \Lambda^+$ the sheaf $J_\lambda$ is the $*$-extension of the constant perverse sheaf from the Iwahori orbit corresponding to $\lambda$, see, e.g. [@AB].

Recall that $p$ stands for the projection $\Fl_G\to\Gr_G$. We set $J_\lambda^{\Gr}=p_*(J_\lambda)$. It is not hard to show that for $\F\in D_{{\bf G_O}\ltimes {{\mathbb G}_m}}(\Gr)$, $J_\lambda^{\Gr}*\F\cong J_\lambda*_I \F$ canonically. Also $J^{\Gr}_\lambda$ can be characterized by $\fj_\mu^*\imath_\mu^!J_\lambda^{\Gr} = \mathsf k^{\delta_{\lambda,\mu}}$ (cf. [@AB]).

Fix $\F\in Perv_ {{\bf G_O}\ltimes {{\mathbb G}_m}}(\Gr)$, and choose a coweight $\lambda$ deep inside the dominant chamber. Then one shows that $j_\nu^!(J_\lambda*\F)\cong 
\mathsf k[\dim Gr_\nu] \otimes \fj_{\nu-\lambda}^* \imath_{\nu-\lambda}^!\F$ for all $\nu$. Thus one can consider the Cousin "filtration" on $J_\lambda*\F$ with subquotients $j_{\nu*}j_\nu^! (J_\lambda*\F)$ and apply the functor $J_{-\lambda}*_I\ \ $ to it, thereby obtaining a "filtration" on $\CF$ with "subquotients\" $\Phi_{MV}^\mu(\F)\otimes J_\mu^{\Gr}$. It is clear that this "filtration" induces the above filtration on $H_{T\times {{\mathbb G}_m}}(\F)$.

Let now $\CF,\CG$ be a pair of objects of $Perv_{{\bf G_O}\ltimes {{\mathbb G}_m}}(\Gr)$. The above "filtration" on $\CF$ induces a \"filtration\" on $\CF*\CG$ with "subquotients" $$\Phi_{MV}^\mu(\F)\otimes J_\mu^{\Gr} *\CG=
\Phi_{MV}^\mu(\F)\otimes J_\mu*_I \CG.$$ Using the "filtration" on $\CG$ with "subquotients" $\Phi_{MV}^\nu(\CG)\otimes
J_\nu^{\Gr}$ we get a "filtration" on $\CF*\CG$ with "subquotients" $$\Phi_{MV}^\mu(\F)\otimes \Phi_{MV}^\nu(\G) \otimes J_\mu*_I J_\nu^{\Gr}=
\Phi_{MV}^\mu(\F)\otimes \Phi_{MV}^\nu(\G) \otimes J_{\mu+\nu}^{\Gr}.$$ Comparing it with the "filtration" on $\CF*\CG$ with "subquotients" $\Phi_{MV}^\eta (\F*\G)$ we get an isomorphism $\Phi_{MV}(\CF*\CG)\cong \Phi_{MV}(\CF)\otimes \Phi_{MV}(\CG)$. It is not hard to see that this isomorphism coincides with any of the standard definitions of tensor structure on $\Phi_{MV}$; in fact, a close description of the tensor structure appears in [@BG], Theorem 3.2.8.

Now we see that the isomorphism $$gr\, H_{T\times {{\mathbb G}_m}}^\bullet(\CF*\CG ) \cong 
gr\, H_{T\times {{\mathbb G}_m}}^\bullet(\CF)\star\ 
gr\, H_{T\times {{\mathbb G}_m}}^\bullet(\CG )$$ breaks as a direct sum of maps $$\left(\Phi_{MV}^\mu(\CF) \otimes 
H_{T\times {{\mathbb G}_m}}^\bullet(J_\mu^{\Gr})\right)\star\ 
\left(\Phi_{MV}^\nu(\CG) \otimes H_{T\times {{\mathbb G}_m}}^\bullet(J_\nu^{\Gr})\right)
\to \Phi_{MV}^{\mu+\nu}
(\CF*\CG) \otimes  H_{T\times {{\mathbb G}_m}}^\bullet(J_{\mu+\nu}^{\Gr}),$$ coming from the map $\Phi_{MV}^\mu(\CF)\otimes \Phi_{MV}^\nu(\CG)
\to \Phi_{MV}^{\mu+\nu}(\CF*\CG)$ induced by the tensor structure on $\Phi_{MV}$, and the natural isomorphism $$\CO(\Gamma_\mu)\star\CO(\Gamma_\nu)=
H_{T\times {{\mathbb G}_m}}^\bullet(J_\mu^{\Gr})\star
 H_{T\times {{\mathbb G}_m}}^\bullet(J_\nu^{\Gr})
 \cong  H_{T\times {{\mathbb G}_m}}^\bullet(J_{\mu+\nu}^{\Gr})=\CO(\Gamma_{\mu+\nu}).$$ The claim follows. $\Box$
