---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-021-65-the-antipode-of-hf
section_title: "The antipode of H(F)"
section_number: 6.5
pages: 40-44
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.924
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B →C is an exact"
---
In the next results we shall  construct an antipode $S:H(F)\to H(F)$, making the bialgebra $ H(F)$ a Hopf algebra in $\vc$.



\begin{lema}\label{antipode-lema}  Let $(\vc,\sigma)$ be a braided tensor category, and $\Bc$ be a monoidal  right  $\vc$-module category.
Let $(F,c):\Bc\to \vc$ be an exact and faithful  monoidal module functor.  For any $B\in \Bc$, $V\in \vc$ there are natural isomorphisms \begin{equation}\label{ts} t_{B,V}: {}^*(B \triangleleft V)\to {}^*B \triangleleft {}^*V\end{equation} such that the diagram
\begin{equation}\label{diagram-ts}
\xymatrix{
{}^*F(B \triangleleft V) \ar[d]^{{}^*(c^{-1}_{B,V})}\ar[rr]^{\qquad\; \qquad \; \qquad F(t_{B,V})\qquad \; \qquad\; \qquad}&& F({}^*B \triangleleft {}^*V)
 \ar[d]^{c_{{}^*B,{}^*V}} \\
 {}^*(F(B)\ot  V)\ar[rr]_{\qquad \qquad \; \qquad\sigma_{ {}^*V, {}^*F(B)} (\phi^l_{F(B),V})^{-1} \qquad \; \qquad\; \qquad}&&  F({}^*B) \ot {}^*V,}
\end{equation}
is commutative. 
\end{lema}
\pf  We shall freely use the fact that $F({}^*B)= {}^*F(B)$, for any $B\in \Bc$. Since we are under the same hypothesis as Theorem \ref{recons-th}, the functor $F:\Bc\to {}^H\vc$ is full. Since $F({}^*B \triangleleft {}^*V)$ is a left $H$-comodule, and the composition 
$$h=c^{-1}_{{}^*B,{}^*V} \sigma_{ {}^*V, F(B)} (\phi^l_{F(B),V})^{-1} {}^*(c^{-1}_{B,V}):{}^*F(B \triangleleft V)\to F({}^*B \triangleleft {}^*V),$$
 is an isomorphism, we can endow ${}^*F(B \triangleleft V)$ with some $H$-comodule structure such that, $h$ is a $H$-comodule map. Fullness of $F$ implies that, there exist some $t_{B,V}$ such that $F(t_{B,V})=h$.
\epf 



We shall use the same notation as in previous sections. We denote by
$$\pi_A:F(A)\ot {}^*F(A)\to H(F)=\oint^{B\in \Bc} F(B)\ot {}^*F(B) $$
the dinatural transformations of the relative coend $H(F)$. Also, recall from Proposition \ref{factorization-F}, that for any $A\in \Bc$ we have that $(F(A),\rho_A)$ is a left $H(F)$-comodule, with structure given by
$$\rho_A=\psi^{H(F)}_{F(A),F(A)}(\pi_A)=(\pi_A\ot \id_{F(A)})(\id_{F(A)} \ot  \coev_{F(A)}).$$
Henceforth, for simplicity, we shall denote $H=H(F)$.
\begin{lema}\label{lemma-antip} Let $(\vc,\sigma)$ be a braided tensor category, and $\Bc$ be a monoidal  right  $\vc$-module category. For any $B\in \Bc$, $V\in \vc$, let us recall morphisms $ d_{B,V}$, defined in Lemma \ref{def-d1}, as
$$d_{B,V}:{}^*F(B\triangleleft V)\to  {}^*V\ot{}^*F(B) , $$
$$ d_{B,V}= \big(\phi^l_{F(B), V} \big)^{-1} {}^*(c^{-1}_{B,V}).$$
Then, for any $B\in \Bc$, $V\in\vc$, we have
\begin{equation}\label{about-rho1} (\sigma^{-1}_{ {}^*V, H}\ot \id_{ {}^* F(B)})(\id_H\ot d_{B,V})\rho_{ {}^*(B\triangleleft V )}=(\id_{{}^*V}\ot \rho_{{}^*B}) d_{B,V}.
\end{equation}
\end{lema}
\pf 
Using Lemma \ref{antipode-lema}, there are natural isomorphisms $t_{B,V}: {}^*(B \triangleleft V)\to {}^*B \triangleleft {}^*V$ such that
\begin{equation}\label{a-t} c_{{}^*B, {}^*V}F(t_{B,V})=\sigma_{{}^*V, F(B)} d_{B,V}.
\end{equation}
The naturality of $\phi^l$ and $c$ implies that
\begin{equation}\label{nat-phi9} 
F({}^*(\id_B\triangleleft \coev_V ))=({}^*(\coev_V)\ot \id_{{}^*F(B)}) d_{B,{}^*V\ot V },
\end{equation}
for any $B\in \Bc$, $V\in \vc$. Using the dinaturality of $\pi$ we obtain that
\begin{equation}\label{pi-and-t} 
\pi_{{}^*(B\triangleleft V)}= \pi_{{}^*B\triangleleft {}^*V}\big(F(t_{B,V})\ot {}^*F(t^{-1}_{B,V})  \big),
\end{equation}
 for any $B\in \Bc$, $V\in \vc$. Also, dinatural transformations $\pi$ satisfy \eqref{dinat:coend:module:right}, this implies that, for any $B\in \Bc$, $V\in \vc$, we have
 \begin{align}\label{pi-sp} \begin{split} \pi_{B \triangleleft {}^*V}= &\pi_B \big(\id_{F(B)}\ot F({}^*(\id_B\triangleleft \coev_V )) \big)    \big(\id_{F(B)}\ot d^{-1}_{B\triangleleft {}^*V,V} \big)\\
 &\big( c_{B,{}^*V} \ot \id_{{}^*F(B\triangleleft {}^*V)}\big) .
 \end{split}
 \end{align}
Next, when it is not absolutely necessary, as a space saving measure, we shall write the identities $\id$, without using subscripts. Using the definition or $\rho$ we obtain that 
$$(\sigma^{-1}_{ {}^*V, H}\ot \id_{ {}^* F(B)})(\id_H\ot d_{B,V})\rho_{ {}^*(B\triangleleft V )} d^{-1}_{B,V}$$ is equal to
\begin{align*} &=(\sigma^{-1}_{ {}^*V, H}\ot \id_{ {}^* F(B)})(\id_H\ot d_{B,V}) (\pi_{{}^*(B\triangleleft V)}\ot \id)(\id\ot \coev_{{}^*F(B\triangleleft V)})d^{-1}_{B,V}\\
&=(\sigma^{-1}_{ {}^*V, H}\ot \id_{ {}^* F(B)}) (\pi_{{}^*B\triangleleft {}^*V} \ot d_{B,V}) (F(t_{B,V})\ot {}^*F(t^{-1}_{B,V})\ot \id)\\
&(\id\ot \coev_{{}^*F(B\triangleleft V)})d^{-1}_{B,V}\\
&=(\sigma^{-1}_{ {}^*V, H}\ot \id_{ {}^* F(B)}) (\pi_{{}^*B\triangleleft {}^*V} \ot d_{B,V}) (F(t_{B,V})\ot \id_{{}^*F({}^*B \triangleleft {}^*V)} \ot  F(t^{-1}_{B,V}))\\
&(\id\ot \coev_{F({}^*B\triangleleft {}^*V)})d^{-1}_{B,V}\\
&=(\sigma^{-1}_{ {}^*V, H}\ot \id_{ {}^* F(B)})(\pi_{{}^*B}\ot \id) (\id\ot F({}^*(\id_{{}^*B}\triangleleft \coev_V ))\ot \id)(\id\ot d_{{}^*B \triangleleft {}^*V,V}\ot \id)\\
& (c_{{}^*B, {}^*V}\ot \id)\big(F(t_{B,V})d^{-1}_{B,V}\ot \id_{{}^*F({}^*B \triangleleft {}^*V)} \ot  d_{B,V} F(t^{-1}_{B,V})\big) (\id\ot d^{-1}_{{}^*B,{}^*V}\ot c^{-1}_{{}^*B, {}^*V} )\\
&(\id\ot \coev_{{}^*F(B)}\ot \id_{{}^*V})(\id_{{}^* F(B\triangleleft V)} \ot \coev_{{}^*V} )\\
&=(\sigma^{-1}_{ {}^*V, H}\ot \id_{ {}^* F(B)})(\pi_{{}^*B}\ot \id) (\id\ot ({}^*(\coev_V)\ot \id_{{}^*B}))d_{B,{}^*V\ot V }\ot \id)\\ &(\id\ot d_{{}^*B \triangleleft {}^*V,V}\ot \id)
 \big(c_{{}^*B, {}^*V} F(t_{B,V})d^{-1}_{B,V}\ot \id_{{}^*F({}^*B \triangleleft {}^*V)} \ot  d_{B,V} F(t^{-1}_{B,V})c^{-1}_{{}^*B, {}^*V}\big)\\ & (\id\ot d^{-1}_{{}^*B,{}^*V}\ot \id )
(\id\ot \coev_{{}^*F(B)}\ot \id_{{}^*V})(\id_{{}^* F(B\triangleleft V)} \ot \coev_{{}^*V} )\\
&= (\id_{{}^*V} \ot \pi_{{}^*B}\ot \id) (\sigma^{-1}_{ {}^*V, F({}^*B)\ot {}^*F({}^*B) }\ot \id)(\id \ot \ev_{{}^*V}\ot \id_{{}^*F({}^*B)\ot {}^*V\ot {}^*F(B)})\\
&(\sigma_{{}^*V, {}^*F(B)}\ot \id_{{}^{**}V\ot {}^*F({}^*B)} \ot \sigma_{{}^*V, {}^*F(B)}) (\id_{{}^*V\ot {}^*F(B)\ot  {}^{**}V}\ot \coev_{{}^*F(B)}\ot \id_{{}^*V})\\
&(\id\ot \coev_{{}^*V})\\
&=(\id_{{}^*V}\ot \rho_{{}^* B}).
\end{align*}
The second equality follows from \eqref{pi-and-t}, the third equality follows from \eqref{duality-iso}, the fourth one follows from \eqref{pi-sp}, the fifth equality follows from \eqref{nat-phi9}. The sixth equality follows by using \eqref{coev-of-dual} and \eqref{a-t}, and the last equality follows by using the rigidity axioms and \eqref{braiding1}.
\epf


Recall that, sometimes we are denoting $H=H(F)$.

\begin{teo}\label{antipode-natural}  Let $\vc$ be a tensor category, and $\Bc$ be a monoidal  right  $\vc$-module category.
Let $(F,c):\Bc\to \vc$ be an exact and faithful  monoidal module functor. There exists a map  $S:H(F)\to H(F)$, such that, it corresponds, under isomorphism $$\omega: \Hom_\vc(H(F),V)\to \Nat_{\! m}(F, V\ot F)$$ presented in \eqref{omega-isom}, to the natural module transformation $\alpha:F\to H(F)\ot F,$
\begin{align*}
\alpha_B=(\ev_{F(B)}&\ot \id_{H(F)\ot F(B)})(\id_{F(B)}\ot \sigma^{-1}_{{}^*F(B),H(F)}\ot \id_{F(B)})\\
& (\id_{F(B)}\ot \rho_{{}^*B}\ot \id_{F(B)})(\id_{F(B)}\ot \coev_{F(B)}).
\end{align*} 
That is $\omega(S)=\alpha$.
\end{teo}
\pf  We only need to prove that, indeed, $\alpha$ is a \textit{module} natural transformation, that is
$$(\id_H\ot c_{B,V}) \alpha_{B\triangleleft V}= (\alpha_B\ot\id_V) c_{B,V},$$
for any $B\in \Bc$, $V\in \vc$.  Equations \eqref{evaluation-mod} and \eqref{coevaluation-mod} implies that
\begin{equation}\label{ev-coev}\begin{split} \ev_{F(B\triangleleft V )} = \ev_{F(B)}\big(\id\ot \ev_V\ot \id \big)\big(c_{B,V}\ot d_{B,V}\big),\\
\coev_{F(B\triangleleft V )}= \big( d^{-1}_{B,V}\ot c^{-1}_{B,V}\big)\big(\id\ot \coev_{F(B)}\ot\id\big) \coev_V
\end{split}
\end{equation} 



Using the definition of $\alpha$ we obtain that $(\id_H\ot c_{B,V}) \alpha_{B\triangleleft V} c^{-1}_{B,V}$ is equal to
\begin{align*} &= (\ev_{F(B\triangleleft V)}\ot \id_{H\ot F(B)\ot V)})(\id_{F(B\triangleleft V)}\ot \sigma^{-1}_{{}^*F(B\triangleleft V),H}\ot c_{B,V} )\\ &
 (\id_{F(B\triangleleft V)}\ot \rho_{{}^*(B\triangleleft V)}\ot \id_{F(B\triangleleft V)})(\id_{F(B\triangleleft V)}\ot \coev_{F(B\triangleleft V)})c^{-1}_{B,V}\\
 &=(\ev_{F(B)}\ot \id_{H\ot F(B)\ot V)})
 \big(\id\ot \ev_V\ot \id_{{}^*F(B) \ot H\ot F(B)\ot V} \big)\\
 &
 (\id_{F(B)\ot V}\ot \sigma^{-1}_{{}^*V\ot {}^*F(B),H}\ot \id_{F(B)\ot V} ) \big(c_{B,V}\ot  \id_{H}\ot d_{B,V} \ot c_{B,V}\big)\\
 &(\id_{F(B\triangleleft V)}\ot \rho_{{}^*(B\triangleleft V)}\ot \id_{F(B\triangleleft V)})\big( \id_{F(B\triangleleft V)}\ot d^{-1}_{B,V}\ot c^{-1}_{B,V}\big) \\ &\big(\id_{F(B\triangleleft V)\ot {}^*V}\ot \coev_{F(B)}\ot\id_V\big) (\id_{F(B\triangleleft V)}\ot \coev_V) c^{-1}_{B,V}\\
 &=(\ev_{F(B)}\ot \id_{H\ot F(B)\ot V)})
 \big(\id\ot \ev_V\ot \id_{{}^*F(B) \ot H\ot F(B)\ot V} \big)\\
 &(\id\ot \sigma^{-1}_{{}^*F(B),H}\ot \id)(\id\ot \sigma^{-1}_{{}^*V,H}\ot \id) \big(\id\ot (\id_{H}\ot d_{B,V} ) \rho_{{}^*(B\triangleleft V)} d^{-1}_{B,V} \ot \id \big)\\
 &\big(\id_{F(B\triangleleft V)\ot {}^*V}\ot \coev_{F(B)}\ot\id_V\big) (\id_{F(B\triangleleft V)}\ot \coev_V)\\
 &=\alpha_B\ot\id_V.
\end{align*}
The second equality follows from \eqref{ev-coev} and the naturality of $\sigma$, the third equality follows by \eqref{braiding1}. The last equality follows from \eqref{about-rho1} and rigidity axioms.
\epf

\begin{rmk} The above result is the most sensitive statement to prove in order to prove the existence of the antipode for $H(F)$. In the case $\vc=\vect_\ku$, the isomorphism
$$\omega: \Hom_\vc(H(F),V)\to \Nat(F, V\ot F)$$
lands in the space of \textit{all} natural transformations. So, in that case, there is nothing to prove, and the existence of $S$ is guaranteed by the fact that $\omega$ is an isomorphism.
\end{rmk}

\begin{cor}\label{antipode-reconstruct} The bialgebra $H(F)$, from Definition \ref{definition:H(F)}, is actually a Hopf algebra. The antipode $S:H(F)\to H(F)$ is determined as  the unique morphism such that
\begin{equation}\label{antipode}
\xymatrix{
 F(B)\ot {}^*F(B) \ar[d]^{\nu_B}\ar[rr]^{\qquad\pi_B}&& H(F)
 \ar[d]^{S} \\
  F(B)\ot {}^*F( B) \ot H\ar[rr]^{\qquad \ev_{F(B)} \ot\id_{H(F)} }&& H(F),}
\end{equation}
is commutative. Here 
$$\nu_B= (\id_{F(B)}\ot  \sigma^{-1}_{{}^*F(B),H(F)})(\id_{F(B)}\ot \pi_{{}^*B}\ot\id_{{}^*F(B)})(\id_{F(B)\ot {}^*F(B)}\ot \coev_{{}^*F(B)}).$$
\end{cor}
\pf Taking the map $S:H(F)\to H(F)$ defined in Theorem \ref{antipode-natural}, and using the definition of $\alpha$, one can prove that $S$ satisfies Diagram \eqref{antipode}. 

Axioms $$m\circ (\id_H\ot S)\circ \Delta=u\circ \varepsilon,$$
 $$m\circ ( S\ot\id_H)\circ \Delta=u\circ \varepsilon,$$
 follow from \eqref{antipode} by a lengthy, but straightforward, computation.
\epf






\begin{rmk} A version of the Hopf algebra $H(F)$ has been previously considered in the work of Lyubashenko \cite{Li1},  \cite{Li2}, when $F$ is some fiber functor and in \cite{Li3},  \cite{Li4}, when $F$ is the identity functor. See also the work of  P. Schauenburg \cite{PS}, where $\vc$ is the category of finite dimensional vector spaces. However, there are new ingredients in our definition.  We require that $\Bc$ is actually a monoidal $\vc$-module category, and the functor $F$ is a monoidal  module functor.  The use of the \textit{relative} coend is another new feature of our construction.
\end{rmk}





Let $(H,\Delta, m, S)$ be a  Hopf algebra in $\vc$. In the next Proposition we shall see that the reconstructed antipode given in Theorem \ref{antipode-natural}, out of the forgetful functor $\uc:{}^H\vc\to\vc$, coincides with the original  antipode $S:H\to H$.

\begin{prop}  Let $(H,\Delta, m, S)$ be a  Hopf algebra in $\vc$. Using the identification $H=H(\uc)$ proven in Lemma \ref{cc}, the  reconstructed antipode obtained in Corollary \ref{antipode-reconstruct} coincides with the antipode $S$ of $H$. 
\end{prop}
\pf Let us denote by $\widehat{S}:H\to H$ the map reconstructed in Proposition \ref{antipode-reconstruct}. For any $V\in \vc$, recall the isomorphism \eqref{omega-isom}
\begin{equation*}
\begin{split} \omega: \Hom_\vc(H(\uc),V)\to \Nat_{\! m}(\uc, V\ot \uc),\\
\omega(g)_{(W,\rho_W)}= (g\ot \id_{W})\psi^{H}_{W,W}(\pi_W),
\end{split}
\end{equation*}  
for any $(W,\rho_W)\in {}^H\vc$.  Corollary \ref{antipode-natural} implies that, if $\alpha:\uc\to H\ot \uc$ is the module natural  transformation defined as
\begin{align*}
\alpha_{(W,\rho_W)}=( \ev_{W}&\ot \id_{H\ot W})(\id_{W}\ot \sigma^{-1}_{{}^*W,H}\ot \id_{ W})\\
& (\id_{W}\ot \rho_{{}^*W} \ot\id_{W})(\id_W\ot \coev_W),
\end{align*}
for any $(W,\rho_W)\in {}^H\vc$, then 
$$\omega(\widehat{S})=\alpha. $$ 
 Using formula  \eqref{antipode-com} for $\rho_{{}^*W}$ we get that
$$\alpha_{(W,\rho_W)}= (S\ot \id_{W})\, \rho_W=\omega(S)_{(W,\rho_W)}, $$
for any $(W,\rho_W)\in {}^H\vc$. Whence $S=\widehat{S}$.
\epf
