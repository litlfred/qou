---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-019-63-reconstruction-results
section_title: "Reconstruction results"
section_number: 6.3
pages: 32-35
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.928
latex_coverage_ratio: 0.925
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B →C is an exact"
---
The following Theorem is one of our main results and is a generalization of \cite[Thm. 2.2.8]{PS}.


\begin{teo}\label{recons-th} Let $\vc$ be a tensor category, and $\Bc$ be a  right  $\vc$-module category. 
Let $(F,c):\Bc\to \vc$ be an exact and faithful  module functor. Let $C=\oint^{B\in \Bc} F(B)\ot {}^*F(B)\in\vc$ be the relative coend coalgebra introduced in Proposition \ref{coalg-coend} and consider its category of comodules ${}^C\vc$. Then the functor $F$ factorizes into an equivalence of $\vc$-module categories $\widehat{F}: \Bc\stackrel{\sim}{\longrightarrow} {}^C\vc$  and the forgetful functor $\uc:{}^C\vc \to\vc$:
\begin{equation}
\xymatrix{
\Bc
\ar[rr]^-{\widehat{F}}
\ar[dr]_-{F}
&&
{}^C\vc
\ar[dl]^-{\uc}\ar@{}[d]|{}&\\
&\vc.&
}
\end{equation} 
\end{teo}
\pf Recall that we denote by
$$\pi_A:F(A)\ot {}^*F(A)\to \oint^{B\in \Bc} F(B)\ot {}^*F(B) $$
the dinatural transformations of the relative coend $C(F)$. The definition of the functor $\widehat{F}:\Bc\to {}^C\vc$ was given in Proposition \ref{factorization-F}. Since $F$ is faithful, $\widehat{F}$ is also faithful. We need to prove that $\widehat{F}$ is essentially surjective and full.


\medbreak

Let us prove first that $\widehat{F}$ is essentially surjective. Take $(M,\rho)\in {}^C\vc$. We endowed $C\ot M$ structure of left $C$-comodule via $\Delta$, then $\rho:M\to C\ot M$ is actually a morphism in ${}^C\vc$. We begin with the observation that, $(M,\rho)$ is the kernel (in ${}^C\vc$) of the difference of morphisms
\begin{equation*}
\xymatrix{
 C \ot M \ar@<0.8ex>[r]^-{\,\, \Delta\ot \id\,\,}\ar@<-0.8ex>[r]_-{ \id\ot \rho}&  C \ot C \ot M.
}
\end{equation*}
Recall from Proposition \ref{factorization-F} that, for any $A\in \Bc$, the object $F(A)$ has a left $H$-comodule structure given by $\rho_A=\psi^C_{F(A),F(A)}(\pi_A).$ Hence, for any $V\in \vc$, the object $F(A)\ot V$ has a left comodule structure given by $\rho_A\ot\id_V$. The next Claim will be crucial for the proof. To prove this claim, it is essential that the dinatural maps $\pi$ satisfy equation \eqref{dinat:coend:module:right}.


\begin{claim}\label{claim:cmodule} For any $A\in \Bc$, $V\in \vc,$ morphisms $c_{A,V}:F(A\triangleleft V)\to F(A)\ot V$ are $C$-comodule maps.
\end{claim}
\pf[Proof of Claim] We need to prove that
\begin{equation*}
(\psi^H_{F(A),F(A)}(\pi_A)\ot \id_V)c_{A,V}=(\id_H\ot c_{A,V}) \psi^H_{F(A\triangleleft V),F(A\triangleleft V)}(\pi_{A\triangleleft V})
\end{equation*}
This equation is equivalent to
\begin{equation}\label{c-comod-maps} 
(\pi_A\ot \id_{F(A)\ot V}) (\id \ot \coev_{F(A)}\ot \id_V) c_{A,V}= (\pi_{A\triangleleft V}\ot c_{A,V})(\id\ot \coev_{F(A\triangleleft V)} ).
\end{equation}
Since $\pi$ satisfies equation \eqref{dinat:coend:module:right}, it follows that
$$\pi_{A\triangleleft V}= \pi_A (\id_{F(A)}\ot {}^*(F(\id_A \triangleleft \coev_{V^*})) ) \big(\beta^{V^*}_{A\triangleleft V, A}  \big)^{-1}.$$
Using the description of the prebalancing $\beta$ given in \eqref{preb-s1}, we obtain that
\begin{align}\label{pi1}\begin{split} \pi_{A\triangleleft V}= &\pi_A (\id_{F(A)}\ot {}^*(c_{A\triangleleft V, V^*}  F(\id_A \triangleleft \coev_{V^*})) ) (\id\ot \phi^l_{F(A\triangleleft V),V^*})\\
&(c_{A,V}\ot \id_{{}^*F(A\triangleleft V)}).
\end{split} \end{align}
It follows from the naturality of $c$ that
$$c_{A, V\ot V^*} F(\id_A \triangleleft \coev_{V^*})=(\id_{F(A)}\ot \coev_{V^*}). $$
Using Equation \eqref{modfunctor11}, it follows that
$$c_{A\triangleleft V, V^*} F(\id_A \triangleleft \coev_{V^*})= (c^{-1}_{A,V}\ot \id_{V^*} )(\id_{F(A)}\ot \coev_{V^*}). $$
Whence
\begin{align}\label{pi2}\begin{split} 
\pi_{A\triangleleft V}&=\pi_A  (\id_{F(A)}\ot {}^*(\id_{F(A)}\ot \coev_{V^*})) (\id_{F(A)}\ot {}^*(c^{-1}_{A,V}\ot \id_{V^*} ) )\\
&(\id_{F(A)}\ot \phi^l_{F(A\triangleleft V),V^*})(c_{A,V}\ot \id_{{}^*F(A\triangleleft V)})\\
&=\pi_A  (\id_{F(A)}\ot {}^*(\id_{F(A)}\ot \coev_{V^*})) (\id_{F(A)}\ot \phi^l_{V^*,F(A)\ot V} )\\
&  ( c_{A,V}\ot {}^*(c^{-1}_{A,V}) ).
\end{split} 
\end{align}
The second equality follows from the naturality of $\phi^l$. It follows by a tedious, but straightforward, computation that
\begin{align}\label{coev-phi}\begin{split} \big({}^*(\id_{F(A)}\ot\coev_{V^*})\ot \id_{F(A)\ot V} \big)&\big( \phi^l_{V^*,F(A)\ot V}\ot\id_{F(A)\ot V}\big)\\&\big( \id_{V}\ot\coev_{F(A)\ot V}\big)= \coev_{F(A)}\ot\id_{V}
\end{split}
\end{align}
Let us prove now equation \eqref{c-comod-maps}.  The right hand side of \eqref{c-comod-maps} is equal to
\begin{align*}  &=(\pi_{A\triangleleft V} \ot\id_{F(A)\ot V} ) (\id\ot c_{A,V}) (\id_{F(A\triangleleft V)}\ot \coev_{F(A\triangleleft V)}) \\
&= \big(\pi_A \ot\id_{F(A)\ot V}  \big) \big(\id_{F(A)}\ot {}^*(\id_{F(A)}\ot \coev_{V^*})\ot\id_{F(A)\ot V}\big)\\
& \big(\id_{F(A)}\ot \phi^l_{V^*,F(A)\ot V}\ot \id_{F(A)\ot V} \big) \big(  c_{A,V} \ot {}^*(c^{-1}_{A,V})\ot \id_{F(A)\ot V} \big)\\
& (\id\ot c_{A,V}) (\id_{F(A\triangleleft V)} \ot\coev_{F(A\triangleleft V)})  \\
&=\big(\pi_A \ot\id_{F(A)\ot V}  \big) \big(\id_{F(A)}\ot {}^*(\id_{F(A)}\ot \coev_{V^*})\ot\id_{F(A)\ot V}\big)\\
& \big(\id_{F(A)}\ot \phi^l_{V^*,F(A)\ot V}\ot \id_{F(A)\ot V} \big) \big( c_{A,V}\ot \coev_{F(A)\ot V} \big)\\
&=(\pi_A\ot \id_{F(A)\ot V}) (\id_{F(A)} \ot \coev_{F(A)}\ot \id_V) c_{A,V}.
\end{align*}
The second equality follows from Equation \eqref{pi2}, the third equality follows from \eqref{duality-iso}, and the last equality follows from \eqref{coev-phi}. This finishes the proof of the Claim.
\epf

From this Claim follows that, natural isomorphisms $c$ endow the functor $\widehat{F}$ with structure of module functor.
Let $$\widetilde{C}=\widetilde{C}(F,c)=\oint^{B\in \Bc} B \triangleleft {}^*F(B)\in \Bc$$
be the object defined in Proposition \ref{existence-coend0}, together with themap
$$\delta:\widetilde{C}\to  \widetilde{C} \triangleleft C,$$
presented in Diagram \eqref{coproduct-tilde-c}.  Since $F(\widetilde{C})=C$, it also follows from Claim \ref{claim:cmodule} that,  there are $C$-comodule  isomorphisms
$$ F(\widetilde{C} \triangleleft  M )\simeq C \ot  M,$$
$$F(\widetilde{C} \triangleleft (C\ot M) )\simeq C\ot C \ot M.$$
Hence $(M,\rho)$ is the kernel of the difference of morphisms
\begin{equation*}
\xymatrix{
F(\widetilde{C} \triangleleft  M ) \ar@<0.8ex>[r]^-{\,\, F(h_1)\,\,}\ar@<-0.8ex>[r]_-{ F(h_2)}&  F(\widetilde{C} \triangleleft (C\ot  M) ),
}
\end{equation*}
where $h_1= \delta \triangleleft   \id_M, h_2=\id_{\widetilde{C}} \triangleleft   \rho$. Since $F$ is left exact $(M,\rho)\simeq F( \ker(h_1-h_2))$.  This proves that $\widehat{F}$ is essentially surjective. 

\medbreak

Let us prove now that $\widehat{F}$ is full. Take $A, B\in \Bc$ and $f:F(A)\to F(B)$ a $C$-comodule morphism. We have a commutative diagram
\begin{equation}\label{comodule}
\xymatrix{
 F(A)\ar[d]^{f}\ar[rr]^{\rho^A\quad}&& C\ot  F(A)  
 \ar[d]^{\id_H\ot f} \\
 F(B) \ar[rr]^{\rho^B }&&  C\ot  F(B).}
\end{equation}
 This implies that, we have a commutative diagram \begin{equation}\label{F-bef}
          \begin{split}
           \xymatrix{
         0 
         \ar[rr]  
         && 
         F(A)
         \ar[rr]^{ \rho_A} 
         \ar[d]^f 
         && 
         C \ot F(A )
		  \ar[rr]^{h^A_1-h^A_2}
		\ar[d]^{\id  \ot f } 
		&&
		C \ot (C\ot F(A ) )
		\ar[d]^{\id\ot f}
		\\
		
		 0
         \ar[rr] 
         && 
          F(B)
         \ar[rr]^{\rho_B} 
          && 
         C \ot F(B )
           \ar[rr]^{h^B_1-h^B_2}
			&&
			C \ot (C\ot F(B ) ).
\\
              }
           \end{split}
      \end{equation}
Where $h^A_1= \id_H\ot \rho_A, h^A_2=\Delta\ot \id_{F(A)}.$ Note that, by the universal property of the kernel, the map $f:F(A)\to F(B)$ is the unique morphism fitting in this diagram. Define
$$ \widetilde{C}=\widetilde{C}(F,c)=\oint^{B\in \Bc} B \triangleleft {}^*F(B)\in \Bc.$$
See Proposition \ref{existence-coend0} for the definition of this coend. Using Proposition \ref{exact-seq}, for any $B\in \Bc$, we have an exact sequence
$$0\to B\xrightarrow{\quad\widetilde{\rho}_B}
\widetilde{C} \triangleleft F(B ) \xrightarrow{\quad \widetilde{h}\quad }  \widetilde{C} \triangleleft (C\ot F(B ) ),
$$
where $\widetilde{h}_B=\id_{\widetilde{C} } \triangleleft \rho_B- \delta\triangleleft  \id_{F(B)}.$ For the definition of $\delta$ and $ \widetilde{\rho}_B$ see \eqref{coproduct-tilde-a}, \eqref{coproduct-tilde-c}. Since $f$ is a comodule morphism, by the universal property of the kernel, there exists a unique morphism $\eta$ that fits into the diagram

 \begin{equation}
          \begin{split}
           \xymatrix{
         0 
         \ar[rr]  
         && 
         A
         \ar[rr]^{ \widetilde{\rho}_A} 
         \ar[d]^\eta 
         && 
         \widetilde{C} \triangleleft F(A )
		  \ar[rr]^{\widetilde{h}_A}
		\ar[d]^{\id  \triangleleft f } 
		&&
		\widetilde{C} \triangleleft (C\ot F(A ) )
		\ar[d]^{\id \triangleleft (\id\ot f)}
		\\
		
		 0
         \ar[rr] 
         && 
          B
         \ar[rr]^{\widetilde{\rho}_B} 
          && 
          \widetilde{C} \triangleleft F(B )
           \ar[rr]^{\widetilde{h}_B}
			&&
			\widetilde{C} \triangleleft (C\ot F(B ) ).
\\
              }
           \end{split}
      \end{equation}
Applying $F$ to this diagram we obtain diagram \eqref{F-bef}. By the uniqueness of $f$, we get that $F(\eta)=f$, proving that $\widehat{F}$ is full. 
\epf
