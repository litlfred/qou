---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-010-31-existence-of-coends
section_title: "Existence of (co)ends"
section_number: 3.1
pages: 15-17
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.876
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B →C is an exact"
---
\label{Section_coendExists}

In this Section we shall prove that certain (co)ends exists. All these (co)ends will be used in subsequent sections. We shall use ideas from \cite{Sh5}.

\medbreak

Let $\vc$ be a tensor category, $\Bc$  be  a right $\vc$-module category. Since our definition of module category includes that the action is right exact in each variable, hypothesis  of \cite[Thm. 2.24]{DSS} are fulfilled. This means that, there exists an algebra $A\in \vc$ such that 
\begin{equation}\label{eq-ma}
\Bc\simeq {}_{A}\vc
\end{equation} 
as module categories. Consider $\vc$ as a right $\vc$-module category with the regular action. We shall denote by $\Rex_\vc(\Bc, \vc)$ the category of right exact $\vc$-module functors. The functor 
$$\Phi:\Bc^{\op} \to \Rex_\vc(\Bc, \vc),$$
$$\Phi(B)(D)= \uhom(D,B)^*$$
is an equivalence of categories, since, under identification \eqref{eq-ma}, the functor $\Phi$ is the composition of equivalences
$$ ({}_A\vc)^{\op} \xrightarrow{( -)^*} \vc_A\xrightarrow{\, R \,} \Rex_\vc({}_{A}\vc,\vc).$$
Here $R:  \vc_{A}  \to \Rex_\vc({}_A\vc,\vc)$ is the functor given by $R(V)(W)=V\ot_{A} W.$
Let be $(F,c)\in \Rex_\vc(\Bc, \vc)$. In particular, we have natural isomorphisms
$$c_{B,X}: F(B \triangleleft X)\to F(B) \ot X,$$
for $B\in\Bc, X\in\vc$. Consider the functor
$$\Bc^{\op}\times \Bc\to \Bc, $$
$$(D, B)\mapsto D \triangleleft {}^*F(B). $$
 This functor posses a $\vc$-prebalancing
\begin{equation}\label{prebalancing-gamma}
    \gamma^V_{B,D}: D\triangleleft {}^*F(B \triangleleft V) \to D\triangleleft {}^*V\ot{}^*F(B ),
\end{equation} 
$$\gamma^V_{B,D}=\id_{D}\triangleleft   (\phi^l_{F(B),V})^{-1} {}^*(c^{-1}_{B,V}). $$
\begin{prop}\label{existence-coend0} Let $\Bc$  be  a right $\vc$-module category. For any right exact $\vc$-module functor $(F,c):\Bc\to \vc$ the coend
$$\widetilde{C}(F,c)=\oint^{B\in \Bc} (B \triangleleft {}^*F(B), \gamma)\in \Bc,$$
exists. Moreover, the functor $(F,c)\mapsto \widetilde{C}(F,c)$ is a quasi-inverse of $\Phi$.
\end{prop}
\pf For any $D\in \Bc$ we have
\begin{align*}
\Nat_{\! m}(\Phi(D), F)& \simeq \oint_{B\in \Bc} \Hom_\vc(\Phi(D)(B), F(B))\\
&\simeq \oint_{B\in \Bc} \Hom_\vc(\uhom_{\Bc}(B,D)^*, F(B))\\
&\simeq \oint_{B\in \Bc} \Hom_\vc( {}^*F(B), \uhom_{\Bc}(B,D))\\
&\simeq \oint_{B\in \Bc} \Hom_\Bc(B \triangleleft {}^*F(B), D)\\
&\simeq \Hom_\Bc( \oint^{B\in \Bc}  B \triangleleft {}^*F(B), D)\\
&=\Hom_{\Bc^{\op}}(D, \oint^{B\in \Bc}  B \triangleleft {}^*F(B)).
\end{align*} 
The first isomorphism is Proposition \ref{compilat-r} (ii), and the fifth isomorphism is Proposition \ref{int-hom}. Observe that, to prove the existence of the  fourth isomorphism, one has to check that the natural isomorphisms
$$\Hom_\vc( {}^*F(B), \uhom_{\Bc}(B,D)\simeq \Hom_\Bc(B \triangleleft {}^*F(B), D)$$
commute with the respective prebalancings and then use Proposition \ref{compilat-r} (i). This calculation is left to the reader.
This proves both, that the coend  $\widetilde{C}(F,c)$ exists and that the quasi-inverse of $\Phi$ is given by 
$$\bar{\Phi}:  \Rex_\vc(\Bc, \vc) \to\Bc^{\op}, $$ $$\bar{\Phi}(F,c)= \oint^{B\in \Bc} (B \triangleleft {}^*F(B), \gamma).$$\epf

For a pair of  module functors $(F,c), (\widetilde F, \tilde c):\Bc\to \vc$, the functor
$$\Bc^{\op}\times \Bc\to \vc, $$
$$ (A,B)\mapsto \widetilde{F}(B)\ot {}^*F(A)$$
 has a canonical prebalancing, given by
\begin{equation}\label{preb-s1}\begin{split} \beta^X_{A,B}: \widetilde{F}(B)\ot {}^*F(A \triangleleft X) \to \widetilde{F}(B \triangleleft  {}^*X)\ot  {}^*F(A),\\
\beta^X_{A,B}=(\tilde{c}^{-1}_{B, {}^*X}\ot \id)(\id_{\widetilde F(B)}\ot (\phi^l_{F(A),X})^{-1} {}^*(c^{-1}_{A,X})).
\end{split}
\end{equation}

As a consequence of Lemma \ref{right-exact-on-coend}, one can apply $\widetilde F $ to the coend in Proposition \ref{existence-coend0}. Thus we get the next result.
\begin{cor}\label{existence-coend1}  For any pair of right exact $\vc$-module functors $F, \widetilde F:\Bc\to \vc$, the coend
$$\oint^{B\in \Bc} (\widetilde F(B) \ot {}^*F(B), \beta)\in \Bc,$$
exists.\qed
\end{cor}
