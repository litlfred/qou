---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-018-62-some-auxiliary-results
section_title: "Some auxiliary results"
section_number: 6.2
pages: 30-32
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.885
latex_coverage_ratio: 0.898
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B →C is an exact"
---
In this section we shall present some technical results that will be used later. In particular, these results will be used in the proof of our main result Theorem \ref{recons-th}.

\medbreak


Let  $\Bc$ be a right $\vc$-module category, and $(F,c):\Bc\to \vc$ be a module functor. To make calculations easier, we shall assume that the associativity of the $\vc$-module category $\Bc$ is trivial. Recall the relative coend
\begin{equation}\label{tilde-c} \widetilde{C}(F,c)=\widetilde{C}=\oint^{B\in \Bc} B \triangleleft {}^*F(B)\in \Bc,
\end{equation}
presented in Proposition \ref{existence-coend0}. Let us denote by
$$\lambda_B:B \triangleleft {}^*F(B) \to \widetilde{C}(F,c),$$
the associated dinatural transformations. Analogous to the definition of $\Delta$, given in 
\eqref{coproduct-c}, we shall define a map
\begin{equation}\label{coproduct-tilde-a}\delta: \widetilde{C}(F,c)\to \widetilde{C}(F,c)\triangleleft C(F,c).\end{equation}
\begin{lema} There exists a unique morphism $\delta: \widetilde{C}(F,c)\to \widetilde{C}(F,c)\triangleleft C(F,c)$ such that
\begin{equation}\label{coproduct-tilde-c}
\xymatrix{
 B\triangleleft {}^*F(B) \ar[d]^{\id\triangleleft(\coev_{F(B)} \ot\id)}\ar[rr]^{\lambda_B}&& \widetilde{C}
 \ar[d]^{\delta} \\
 B\triangleleft {}^*F(B)\ot  F(B)\ot {}^*F(B) \ar[rr]^{\qquad \,\,\,\,\,\,\lambda_B\triangleleft\,\pi_B }&& \widetilde{C}\triangleleft C.}
\end{equation}
\end{lema} 
\pf Let us denote $ d_{B,V}$ the following natural isomorphism
$$d_{B,V}:{}^*F(B\triangleleft V)\to  {}^*V\ot{}^*F(B) , $$
$$ d_{B,V}= \big(\phi^l_{F(B), V} \big)^{-1} {}^*(c^{-1}_{B,V}).$$
Recall from Equation \eqref{prebalancing-gamma}, that the prebalancing used in the coend $\widetilde{C}(F,c)$ is given by
$$\gamma^V_{B,D}: D\triangleleft {}^*F(B \triangleleft V) \to D\triangleleft {}^*V\ot{}^*F(B ), $$
$$\gamma^V_{B,D}=\id_{D}\triangleleft   d_{B,V}. $$
Using that $c$ satisfies \eqref{modfunctor11}, it is not difficult to prove that
\begin{equation}\label{about-d0} 
d_{B,{}^*V\ot V }=(\phi^l_{{}^*V,V}\ot \id)(\id_{{}^*V}\ot d_{B,{}^*V}) d_{B\triangleleft {}^*V, V },
\end{equation}
for any $B\in \Bc$, $V\in \vc$.
The naturality of $\phi^l$ and $c$ implies that
\begin{equation}\label{nat-phi90} 
F({}^*(\id_B\triangleleft \coev_V ))=({}^*(\coev_V)\ot \id_{{}^*F(B)}) d_{B,{}^*V\ot V },
\end{equation}
for any $B\in \Bc$, $V\in \vc$. Whence, using \eqref{coev-of-dual}, it follows that
\begin{equation}\label{f11} 
F({}^*(\id_B\triangleleft \coev_V )) d^{-1}_{B\triangleleft {}^*V, V }= (\ev_{{}^*V})\ot \id_{{}^*F(B)}) (\id_{{}^*V}\ot d_{B,{}^*V}).
\end{equation}
In this case, if $A\in \Bc$, a dinatural transformation $\nu_B: B\triangleleft {}^*F(B)\to A$ satisfies Equation \eqref{dinat:coend:module:right} if and only if
\begin{equation}\label{3.5-incase}  \nu_B \big( \id_B \triangleleft F({}^*(\id_B\triangleleft \coev_V )\big)= \nu_{B \triangleleft {}^*V}  \gamma^V_{B\triangleleft {}^*V,B}.
\end{equation}
Using that dinatural transformations $\lambda$ and $\pi$ both satisfy \eqref{dinat:coend:module:right} and using \eqref{f11}, it follows that dinatural transformation
$$(\lambda_B\triangleleft\,\pi_B) (\id_B\triangleleft(\coev_{F(B)} \ot\id_{{}^*F(B)}) $$
also satisfies \eqref{3.5-incase}. Now, existence of the map $\delta: \widetilde{C}(F,c)\to \widetilde{C}(F,c)\triangleleft C(F,c)$ satisfying \eqref{coproduct-tilde-c} follows from the universal property of the relative coend.
\epf


For any $A, B\in \Bc$ and $V\in \vc$, define
\begin{align}\label{duals01}\begin{split} \widetilde{\psi}^V_{B,A}:\Hom_\Bc(B\triangleleft {}^*V,A)\to \Hom_\Bc(B,A \triangleleft  V),\\
\widetilde{\psi}^V_{B,A}(f)=(f\triangleleft \id_V)(\id_B  \triangleleft \coev_V).
\end{split}
\end{align}
Compare with natural isomorphisms given in \eqref{duals1}. For any $B\in \Bc$, define also
\begin{equation}\label{coact1} \widetilde{\rho}_B= \widetilde{\psi}^{F(B)}_{B,\widetilde{C}}(\lambda_B):B\to \widetilde{C} \triangleleft F(B).
\end{equation}

One could check that, using Lemma \ref{right-exact-on-coend}, whenever $F$ is right exact, $F(\widetilde{C})=C$. The dinatural transformations of $F(\widetilde{C})$ is given by $F(\lambda_B)$. In particular, this implies that 
\begin{equation}\label{rho-tilde-rho} c_{\widetilde{C},F(B)}F(\widetilde{\rho}_B)=\rho_B,
\end{equation}
for any $B\in \Bc$. Using definition of $\Delta:C\to C\ot C$ given by diagramm \eqref{coalg-coend}, one can see that
\begin{equation}\label{D-d} c_{\widetilde{C}, C} F(\delta)=F(\Delta).
\end{equation}



If $h_1, h_2:C\ot F(B)\to C\ot C\ot F(B)$ are defined as
$$ h_1=\id_C\ot \rho_B, \quad h_2=\Delta\ot \id_{F(B)},$$
then, it is a standard result that, the kernel of the difference $h_1-h_2$ is $\rho_B$. Using   the above, we have the following:
\begin{prop}\label{exact-seq}  Assume that the module functor  $(F,c):\Bc\to \vc$ is faithful and  exact. The map $\widetilde{\rho}_B:B\to \widetilde{C} \triangleleft F(B)$ is the kernel of the difference of morphisms
\begin{equation*}
\xymatrix{
\widetilde{C} \triangleleft F(B ) \ar@<0.8ex>[r]^-{\,\, \widetilde{h}_1\,\,}\ar@<-0.8ex>[r]_-{ \widetilde{h}_2}&  \widetilde{C} \triangleleft (C\ot F(B ) ),
}
\end{equation*}
where $\widetilde{h}_1= \id_{\widetilde{C} } \triangleleft \rho_B$ and $\widetilde{h}_2= \delta\triangleleft  \id_{F(B)}.$
\end{prop}
\pf Note that, we are using that $F$ is right exact so that $F(\widetilde{C})=C$. See Lemma \ref{right-exact-on-coend}. Using \eqref{rho-tilde-rho}, \eqref{D-d} and the naturality of $c$ one can prove that
$$ c_{\widetilde{C}, C\ot F(B)} F(\widetilde{h}_1-\widetilde{h}_2)= (h_1-h_2) c_{\widetilde{C}, F(B)}.$$
This implies that $F (\widetilde{\rho}_B)=\ker F(\widetilde{h}_1-\widetilde{h}_2)=F(\ker \widetilde{h}_1-\widetilde{h}_2)$, since $F$ is also left exact. The result follows, since $F$ is faithful. 
\epf
