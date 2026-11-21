---
doc_id: arxiv-math-0408210v3
doc_title: "A simple algebraic proof of the algebraic index theorem"
section_id: sec-006-3-the-local-version-of-the-algebraic-index-theor
section_title: "The local version of the algebraic index theorem"
section_number: 3
pages: 12-15
source_pdf: 0408210v3.pdf
source_sha256: 16d5ccb83a86954f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.972
doc_brief: "A simple algebraic proof of the algebraic index theorem — In math.QA/0311303 B. Feigin, G. Felder, and B."
---
Let ${\cal M}$ be either a smooth real symplectic manifold of dimension $2n$ or a smooth affine algebraic variety (over ${\Bbb C}$) of the complex dimension $2n$ endowed with an algebraic symplectic form. Let $*$ be a star-product in the vector space $C({\cal M})(({\hbar}))$ of smooth (resp. regular) functions on ${\cal M}$. Throughout this section we denote the algebra $(C({\cal M})(({\hbar})),*)$ by ${\Bbb A}$ and the subalgebra $(C({\cal M})[[{\hbar}]],*)$ of ${\Bbb A}$ by ${\Bbb A}^+$

Due to remark $2$ after theorem [\[F\]](#F){reference-type="ref" reference="F"}, we may safely assume that $*$ is obtained by Fedosov's procedure. Since in this case the vector bundle is trivial the Fedosov star-product depends only on the pair $({\partial}^s, {\Omega}_{{\hbar}})$, where ${\partial}^s$ is the symplectic connection on ${\cal M}$ and ${\Omega}_{{\hbar}}\in {\hbar}{\Omega}^2({\cal M})[[{\hbar}]]$ is a series of closed two-forms. Let $D= {\nabla}+ {\hbar}^{-1}[A,\cdot\,]$ be the corresponding Fedosov connection.

For any idempotent $P$ in the matrix algebra ${\mathfrak{gl}}_N({\Bbb A}^+)$ we assign the top degree De Rham cohomology class $$\label{class}
cl(P) = [\Psi_D(P)] \in H^{2n}({\cal M})(({\hbar}))\,,$$ where $D$ is naturally extended to the Fedosov connection on the Weyl algebra bundle $W(End(L_N))$ associated with the trivial bundle $L_N$ of rank $N$ .

Due to statements $i)$ and $ii)$ ([\[class\]](#class){reference-type="ref" reference="class"}) gives a well-defined map $$cl \,:\, K_0({\Bbb A}^+) \mapsto H^{2n}({\cal M})(({\hbar}))$$ from the $K_0$-group of the algebra ${\Bbb A}^+$ to $H^{2n}({\cal M})(({\hbar}))$.

::: defi
The zeroth term $q=P|_{{\hbar}=0}$ of an idempotent $P\in {\mathfrak{gl}}_N({\Bbb A}^{+})$ is called the principal part of $P$ .
:::

It is obvious that $q$ is an idempotent in the matrix algebra ${\mathfrak{gl}}_N(C({\cal M}))$ and the operation of taking the principal part gives a well-defined principal symbol map $$\label{symb}
\Xi\,:\, K_0({\Bbb A}^+) \mapsto
K_0(C({\cal M}))\,.$$

Due to the observation of L. Boutet de Monvel and V. Guillemin [@BM-G] for any idempotent $q$ in the matrix algebra ${\mathfrak{gl}}_N(C({\cal M}))$ there exists an idempotent $P\in {\mathfrak{gl}}_N({\Bbb A}^+)$ whose principal part is $q$. (See the explicit formula for $P$ in [@F1], eq. ($6.1.4$))

Using standard arguments of the index theory we can prove that the cohomology class ([\[class\]](#class){reference-type="ref" reference="class"}) of an idempotent $P\in{\mathfrak{gl}}_N({\Bbb A}^+)$ depends only on its principal part. For our purposes we need a slightly more general statement:

::: pred
[]{#only label="only"} Let $V$ be a vector bundle over ${\cal M}$ and $*$ be the Fedosov star-product in $End_V[[{\hbar}]]$. Then if two idempotents $P_1, P_2\in (End_V[[{\hbar}]], *)$ have the same principal part $$P_1\Big|_{{\hbar}=0} = P_2\Big|_{{\hbar}=0}\,,$$ the cohomology classes $[\Psi_D(P_1)]$ and $[\Psi_D(P_2)]$ coincide.
:::

**Proof** is a straightforward generalization of the arguments in the proof of theorem $6.1.3$ in [@F1] . $\Box$

The precise dependence of the cohomology class $cl(P)$ on the principal part $q$ of $P$ is given by the local algebraic index theorem

::: teo
[]{#index label="index"} For any element $\Pi \in K_0({\Bbb A}^+)$ the cohomology class $cl(\Pi)$ coincides with the top component of the cup product $$cl(\Pi) = \Big[ \,{\hat{A}}({\cal M}) \exp\left(-\frac{F}{{\hbar}}\right)\, ch(\Xi(\Pi))\,
\Big]_{2n}\,,$$ of the ${\hat{A}}$-genus of ${\cal M}$, the exponent $\displaystyle e^{-\frac{F}{{\hbar}}}$ of the Deligne-Fedosov class $$F= \Big[ -{\omega}+ {\Omega}_{{\hbar}} \Big]$$ of the star-product in ${\Bbb A}^+$ and the Chern character $ch(\Xi(\Pi))$ of the principal symbol $\Xi(\Pi)$ of $\Pi$ .
:::

**Proof.** Let $P$ be an idempotent in the matrix algebra ${\mathfrak{gl}}_N({\Bbb A}^+)$ and $q\in {\mathfrak{gl}}_N(C({\cal M}))$ be the principal part of $P$. As an idempotent endomorphism of the trivial bundle $L_N$ or rank $N$, $q$ defines a subbundle $E= Im\,q\subset  L_N$.

It suffices to prove that the $2n$-form $\Psi_D(P)$ has the same cohomology class as the $2n$-th component of the form $$\det\Big(\frac{R/2}{sinh\,(R/2)}
\Big)^{1/2}\exp\left( \frac{{\omega}- {\Omega}_{{\hbar}}}{{\hbar}}\right)
\, tr \exp(R^E)\,,$$ where $R$ is the curvature form of the symplectic connection ${\partial}^s$, $R^E$ is the curvature form of the vector bundle $E$ , and $tr$ stands for the ordinary matrix trace.

We start with an observation that $q$ is a flat section of $End(L_{N})$ with respect to the connection $$\label{pa-L}
{\partial}^{L_N} = d + [q(dq)-(dq)q,\cdot\,]\,.$$

Let $D^{L_N}$ be the Fedosov connection ([\[F-conn\]](#F-conn){reference-type="ref" reference="F-conn"}) corresponding to the initial symplectic connection ${\partial}^s$ on ${\cal M}$, the initial series ${\Omega}_h$ of closed two-forms and the connection ([\[pa-L\]](#pa-L){reference-type="ref" reference="pa-L"}) on the trivial bundle $L_N$ . By claim $3$ of theorem [\[F\]](#F){reference-type="ref" reference="F"} there exists an element $U\in I_N \oplus W^1(End_{L_N})$ which establishes the equivalence between the connections $D$ and $D^{L_N}$ in the sense of definition [\[equiv\]](#equiv){reference-type="ref" reference="equiv"}. Therefore, by statement $iii)$ of theorem [\[main\]](#main){reference-type="ref" reference="main"} $$\Psi_{D}(P) - \Psi_{D^{L_N}}(\widetilde{P}) \in
d{\Omega}^{2n-1}({\cal M})(({\hbar}))\,,$$ where $\widetilde{P}= {\sigma}(U^{-1}\circ P \circ U)$ is an idempotent in the algebra $(End_{L_N}, \tilde{*})$, with the star-product $\tilde{*}$ corresponding to the Fedosov connection $D^{L_N}$ .

Notice that, $\widetilde{P}$ and $P$ have the same principal part $\widetilde{P}\Big|_{{\hbar}=0}=P\Big|_{{\hbar}=0}=q$. Let us consider $q$ as an element in the algebra $(End_{L_N}, \tilde{*})$ . By claim $1$ of theorem [\[F\]](#F){reference-type="ref" reference="F"} we may assume that $D^{L_N}$ satisfies normalization condition ([\[norm\]](#norm){reference-type="ref" reference="norm"}). Therefore, by lemma [\[Tech\]](#Tech){reference-type="ref" reference="Tech"} the element $q$ is flat with respect to $D^{L_N}$, and hence $q$ is an idempotent of the algebra $(End_{L_N}, \tilde{*})$ . By proposition [\[only\]](#only){reference-type="ref" reference="only"} we may safely assume that $\widetilde{P}=q$ .

We recall that $E= Im\,q\subset L_N$ is the subbundle of $L_N$ , corresponding to the idempotent $q$ and denote by $\widetilde{E}$ the subbundle $\widetilde{E}\subset L_N$ corresponding to the complementary idempotent $I_N-q\in End_{L_N}$ . Thus, our trivial vector bundle $L_N$ is isomorphic to the direct sum $E\oplus \widetilde{E}$ . Let us fix an isomorphism $u$ $$u\,:\, L ~\widetilde{\rightarrow}~ E\oplus \widetilde{E}\,.$$

Since $q_u= u q u^{-1}\in End_{E\oplus \widetilde{E}}$ is the projector onto $E$ along $\widetilde{E}$ $$\label{E-m}
q_u\, \Big|_{{\Gamma}(E)(({\hbar}))} = I_m\,, \qquad
q_u\, \Big|_{{\Gamma}(\widetilde{E})(({\hbar}))} = 0\,,$$ where $m$ is the rank of $E$ and $I_m$ is the identity endomorphism of $E$ .

Due to remark $1$ after theorem [\[F\]](#F){reference-type="ref" reference="F"} $$\label{conj}
D^{E\oplus \widetilde{E}} = D^{L_N} + [u D^{L_N}(u^{-1}), \cdot\,]$$ is the Fedosov connection on the Weyl algebra bundle $W(End_{E\oplus \widetilde{E}})$.

Furthermore, $q_u= u q u^{-1}$ is flat with respect to $D^{E\oplus \widetilde{E}}$, and hence the connection $D^{E\oplus \widetilde{E}}$ preserves the following subspaces of $End_{E\oplus \widetilde{E}}(({\hbar}))$ $$\{a\in End_{E\oplus \widetilde{E}}(({\hbar}))~|~ a\,\Big|_{{\Gamma}(E)(({\hbar}))}
\subset {\Gamma}(E)(({\hbar})),~ \ a\,\Big|_{{\Gamma}(\widetilde{E})(({\hbar}))}=0 \}\,,$$ $$\{a\in End_{E\oplus \widetilde{E}}(({\hbar}))~|~ a\,\Big|_{{\Gamma}(\widetilde{E})(({\hbar}))}
\subset {\Gamma}(\widetilde{E})(({\hbar})),~ \ a\,\Big|_{{\Gamma}(E)(({\hbar}))}=0 \}\,.$$ The latter implies that $D^{E\oplus \widetilde{E}}$ is a direct sum $D^E \oplus D^{\widetilde{E}}$ of the Fedosov connections $$\label{D-E}
D^E = {\nabla}^E  + \frac1{{\hbar}}[A^E, \cdot\,]\,,
\qquad
D^{\widetilde{E}} = {\nabla}^{\widetilde{E}}  + \frac1{{\hbar}}[A^{\widetilde{E}}, \cdot\,]$$ on the bundles $W(End_{E})$ and $W(End_{\widetilde{E}})$, respectively. Thus, due to ([\[E-m\]](#E-m){reference-type="ref" reference="E-m"}) and statement $i)$ of theorem [\[main\]](#main){reference-type="ref" reference="main"} we have $$\Psi_{D^{L_N}}(\widetilde{P}) = \Psi_{D^E}(I_m)\,,$$ where $I_m$ is as above the identity endomorphism of the vector bundle $E$ .

Using statement $iv)$ of theorem [\[main\]](#main){reference-type="ref" reference="main"} we get that $$\label{vot-ono}
\Psi_{D^E}(I_m) - \frac1{{\hbar}^n}\,Q_n(C(A^E,A^E), \dots, C(A^E,A^E))
\in d {\Omega}^{2n-1}({\cal M})(({\hbar}))\,,$$ where $Q_n\in ((S^n{\mathfrak{h}})^*)^{{\mathfrak{h}}}$ is the $n$-th component of the adjoint invariant form ([\[Qn\]](#Qn){reference-type="ref" reference="Qn"}), ${\mathfrak{h}}= {\mathfrak{gl}}_N \oplus {\mathfrak{sp}}_{2n}$ , $A^E\in {\Omega}^1(W(End_{E}))$ is the one-form of the Fedosov connection $D^E$ ([\[D-E\]](#D-E){reference-type="ref" reference="D-E"}), and $C$ is the fiberwise "curvature" ([\[curvature\]](#curvature){reference-type="ref" reference="curvature"}) of the projection ([\[pr\]](#pr){reference-type="ref" reference="pr"}).

To compute $C(A^E, A^E)$ we mention that since the Fedosov connection $D^{E\oplus\widetilde{E}}$ is obtained from the $D^{L_N}$ via conjugation ([\[conj\]](#conj){reference-type="ref" reference="conj"}) the connection $D^{E\oplus\widetilde{E}}$ has the same Fedosov-Weyl curvature ([\[Weyl-c\]](#Weyl-c){reference-type="ref" reference="Weyl-c"}) $${\hbar}(R+R^{E\oplus\widetilde{E}}) +2 {\nabla}^{E\oplus\widetilde{E}}
A^{E\oplus\widetilde{E}} + \frac1{{\hbar}}
[A^{E\oplus\widetilde{E}},  A^{E\oplus\widetilde{E}}] =
-{\omega}+ {\Omega}_{{\hbar}}\,.$$ Here $A^{E\oplus\widetilde{E}}$ is the one-form of the Fedosov connection $D^{E\oplus\widetilde{E}}$, ${\nabla}^{E\oplus\widetilde{E}}$ is the operator ([\[nabla\]](#nabla){reference-type="ref" reference="nabla"}) corresponding to the symplectic connection ${\partial}^s$ and the connection ${\partial}^{E\oplus\widetilde{E}}$ on $E\oplus \widetilde{E}$ obtained from ${\partial}^{L_N}$ via the isomorphism $u$ . Finally, $R^{E\oplus\widetilde{E}}$ is the curvature form of the connection ${\partial}^{E\oplus\widetilde{E}}$ .

On the other hand the Fedosov connection $D^{E\oplus\widetilde{E}}$ is a direct sum of the Fedosov connections $D^E$ and $D^{\widetilde{E}}$ . Hence, $$\label{the-same}
{\hbar}(R+ R^{E}) +2 {\nabla}^{E}
A^{E} + \frac1{{\hbar}}
[A^{E}, A^{E}] =
-{\omega}+ {\Omega}_{{\hbar}}\,,$$ where $R^E$ is the curvature form of the connection ${\partial}^E$ on $E$ and ${\nabla}^E$ is the operator ([\[nabla\]](#nabla){reference-type="ref" reference="nabla"}) corresponding to the symplectic connection ${\partial}^s$ on ${\cal M}$ and the connection ${\partial}^E$ .

Notice that, the projection $pr(A^E)$ may be non-zero. However, using the trick of proposition [\[absor\]](#absor){reference-type="ref" reference="absor"} we can absorb the terms that contribute to $pr(A^E)$ into the operator ${\nabla}^E$. In this way we change both[^1] the symplectic connection ${\partial}^s$ on ${\cal M}$ and the connection ${\partial}^E$ on $E$ , and therefore we change curvature forms $R$ and $R^E$. It is not hard to show that after this rearrangement equation ([\[the-same\]](#the-same){reference-type="ref" reference="the-same"}) still holds.

Since $pr(A^E)$ is now vanishing $pr {\nabla}(A^E)= {\nabla}pr (A^E)=0$ . Thus, applying $pr$ to both sides of ([\[the-same\]](#the-same){reference-type="ref" reference="the-same"}) we get $$\label{that}
C(A^E, A^E) = {\hbar}^2 R + {\hbar}^2 R_E - {\hbar}
(-{\omega}+ {\Omega}_{{\hbar}})\,.$$ Substituting ([\[that\]](#that){reference-type="ref" reference="that"}) into equation ([\[vot-ono\]](#vot-ono){reference-type="ref" reference="vot-ono"}) we complete the proof of the theorem. $\Box$

[^1]: Notice that, both the new Christoffel form ${\Gamma}$ and the new connection form ${\Gamma}^E$ become formal power series in ${\hbar}$ .
