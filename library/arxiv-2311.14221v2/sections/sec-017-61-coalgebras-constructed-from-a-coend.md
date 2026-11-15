---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-017-61-coalgebras-constructed-from-a-coend
section_title: "Coalgebras constructed from a coend"
section_number: 6.1
pages: 26-30
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.911
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B →C is an exact"
---
Let $\vc$ be a  tensor category, and $\Bc$ be a right $\vc$-module category. For the rest of this section, $(F,c):\Bc\to \vc$ will denote  a right exact module functor. 

\medbreak



 Consider the functor
$$S^F:\Bc^{\op}\times \Bc\to \vc, $$
$$S^F(A,B)=F(B)\ot {}^*F(A).$$
This functor has a canonical prebalancing, given by
\begin{equation}\label{preb-s2}\begin{split} \beta^X_{A,B}: F(B)\ot {}^*F(A \triangleleft X) \to F(B \triangleleft  {}^*X)\ot  {}^*F(A),\\
\beta^X_{A,B}=(c^{-1}_{B, {}^*X}\ot \id_{{}^*F(A)})(\id_{F(B)}\ot (\phi^l_{F(A),X})^{-1} {}^*(c^{-1}_{A,X})).
\end{split}
\end{equation}
We define
$$C(F,c)=C(F)=\oint^{B\in \Bc} (S^F,\beta)= \oint^{B\in \Bc} F(B)\ot {}^*F(B).$$
Let $\pi_B:F(B)\ot {}^*F(B)\to C(F)$ be the associated dinatural transformations. Existence of this coend follows from Corollary \ref{existence-coend1}.
The following Lemma is a generalization of \cite[Lemma 2.1.9]{PS}. Recall that, for any $M, N\in \Bc$, $X\in \vc$ we have natural isomorphisms
$$\psi^V_{F(M),F(N)}:\Hom_\vc(F(M)\ot {}^*F(N),V)\to \Hom_\vc(F(M),V\ot F(N))$$
described in \eqref{duals1}.
\begin{lema}\label{a-omega} The functor 
$V\mapsto \Nat_{\! m}(F, V\ot F)$
is represented by $C(F)$. That is, for any $V\in\vc$ there are natural isomorphisms
\begin{equation}\label{omega-isom}
\begin{split} \omega: \Hom_\vc(C(F),V)\to \Nat_{\! m}(F, V\ot F),\\
\omega(g)_B= (g\ot \id_{F(B)})\psi^{C(F)}_{F(B),F(B)}(\pi_B).
\end{split}
\end{equation}  
\end{lema}
\pf Fix some object $V\in \vc$. The functor $V\ot F$ is a right module functor, then we can consider the prebalancing of the functor
$$\Hom_\vc(F( -),V\ot F(- )): \Bc\times \Bc^{\op}\to \vect_\ku, $$
given by
$$\gamma^X_{B,N} :\Hom_\vc(F(N\triangleleft {}^*X),V\ot F(B  ))\to   \Hom_\vc(F(N ),V\ot F(B\triangleleft X)),$$
$$\gamma^X_{N,B}(f)=(\id_V\ot c_{B, X})(f\ot \id_X) (c^{-1}_{N, {}^*X}\ot \id_X)(\id_{F(N)}\ot \coev_X).$$
Note that here we are considering $\B^{\op}$ as a left $\vc$-module category, with action $X\triangleright B:=B\triangleleft {}^*X$.
Proposition \ref{compilat-r} (ii) tells us that there is an isomorphism
$$\oint_{B\in \Bc}  (\Hom_\vc(F(B),V\ot F(B)), \gamma) \simeq \Nat_{\! m}(F, V\ot F). $$
From the proof of Proposition \ref{int-hom}, one can see that the dinatural transformations of the end $\oint_{B\in \Bc}  \Hom_\vc(F(B)\ot {}^*F(B),V)$ are given by
$$\widehat{\pi}_B:\oint_{B\in \Bc}  \Hom_\vc(F(B)\ot {}^*F(B),V)\to \Hom_\vc(F(B)\ot {}^*F(B),V), $$
$$\widehat{\pi}_B(g)= g\circ \pi_B.$$
Here, we are using identification $$\oint_{B\in \Bc}  \Hom_\vc(F(B)\ot {}^*F(B),V)= \Hom_\vc(\oint^{B\in \Bc}  F(B)\ot {}^*F(B),V).$$


 It follows by a straightforward computation that
$$\gamma^X_{M,N} (\psi^V_{F(M\triangleleft {}^*X ),F(N )}(f))=\psi^V_{F(M ),F(N\triangleleft X)}(f\circ \beta^X_{N,M} ),$$
for any $M, N\in \Bc$ and any $f\in \Hom_\Bc(F(M \triangleleft {}^*X)\ot {}^*F(N ),V)$. This implies, using Proposition \ref{compilat-r} (i) that, for any $V\in \vc$, there exists an isomorphism 
$$ \widehat{\psi}^V:\oint_{B\in \Bc}  \Hom_\vc(F(B)\ot {}^*F(B),V)\to \oint_{B\in \Bc}  \Hom_\vc(F(B),V\ot F(B)),$$
such that $\mu_B\circ\widehat{\psi}^V= \psi^V_{F(B),F(B)}\circ \widehat{\pi}_B.$ For any $V\in \vc$ we have that 
\begin{align*}  \Hom_\vc(C(F),V)&\simeq \oint_{B\in \Bc}  \Hom_\vc(F(B)\ot {}^*F(B),V)\\
&\simeq \oint_{B\in \Bc}  \Hom_\vc(F(B),V\ot F(B))\\
&\simeq \Nat_{\! m}(F, V\ot F).
\end{align*}
The first isomorphism is Proposition \ref{int-hom}. Tracing this chain of isomorphisms, one can see that, the composition coincides with $\omega$ defined by Equation \eqref{omega-isom}.
\epf


\begin{prop}\label{coalg-coend} Let $\vc$ be a  tensor category, and $\Bc$ be a right $\vc$-module category. Let $(F,c):\Bc\to \vc$ be  a right exact module functor. The object $C(F)\in\vc$ has a coalgebra structure $\Delta:C(F)\to C(F)\ot C(F)$, $\varepsilon:C(F)\to \uno$ determined by diagramms
\begin{equation}\label{coproduct-c}
\xymatrix{
 F(B)\ot {}^*F(B) \ar[d]_{\id\ot \mathrm{coev}_{F(B)} \ot\mathrm{id}}\ar[rr]^{\pi_B}&& C(F)
 \ar[d]^{\Delta} \\
 F(B)\ot {}^*F(B)\ot  F(B)\ot {}^*F(B) \ar[rr]_{\qquad\pi_B\ot \pi_B }&& C(F)\ot C(F),}
\end{equation}
\begin{equation}\label{counit-c}
\xymatrix{ F(B)\ot {}^*F(B)    \ar[rr]^{\pi_B}
\ar[dr]_{ \mathrm{ev}_{F(B)}  }&& C(F)
\ar[dl]^{\varepsilon }\\ & \uno,&}
\end{equation}
for any $B\in \Bc$.
\end{prop}
\pf It follows by a straightforward computation that, the maps
$$ \ev_{F(B)}:F(B)\ot {}^*F(B)\to \uno,  $$
$$(\pi_B\ot \pi_B )(\id\ot \coev_{F(B)} \ot\id): F(B)\ot {}^*F(B)\to C(F)\ot C(F), $$
are dinatural maps. It follows from Diagram \eqref{evaluation-mod} that $ \ev_{F(B)}$  satisfies \eqref{dinat:coend:module:right}.  It follows from Diagram \eqref{coevaluation-mod} and the fact that $\pi$ satisfies \eqref{dinat:coend:module:right} that, $(\pi_B\ot \pi_B )(\id\ot \coev_{F(B)} \ot\id)$ also satisfies Equation \eqref{dinat:coend:module:right}. Whence, the existence of $\Delta$ and $\varepsilon$ follow from the universal property of the relative coend. 
\medbreak

The proof that $(C(F),\Delta, \varepsilon)$ is a coalgebra is standard, and it follows from Diagrams \eqref{coproduct-c}, \eqref{counit-c}.
\epf 

Let $\vc$ be a tensor category and $C\in \vc$ be a coalgebra. The category ${}^C\vc$, of left $C$-comodules in $\vc$, is a right $\vc$-module category. The action is given as follows. If $(W,\rho)\in {}^C\vc$, then $W \triangleleft Y=W\ot Y$, where the coaction on $W\ot Y$ is given by $\rho\ot \id_Y.$
The forgetful functor $\uc:{}^C\vc\to \vc$ is a $\vc$-module functor. The next result says that the coalgebra reconstructed from the forgetful functor $\uc$ coincides with $C$.

\bigbreak

In this case, the functor $S^\uc$ has a prebalancing given by
$$\beta^X_{A,B}=\id_B\ot (\phi^l_{A,X})^{-1},$$
for any $A, B\in {}^C\vc$, $X\in \vc$. 
\begin{lema}\label{cc} There exists an isomorphism of coalgebras $C(\uc)\simeq C$ in $\vc$.
\end{lema}
\pf  In this particular case, if $T\in\vc$ is an object, and $\lambda_W:W\ot {}^*W\to T$ is a dinatural transformation, Equation \eqref{dinat:coend:module:right} writes as
\begin{equation}\label{new.3.5} 
\lambda_{W\ot {}^*V}(\id_W\ot (\phi^l_{W\ot {}^*V,V})^{-1}) =\lambda_W (\id_W\ot {}^*(\id_W\ot \coev_V)),
\end{equation}
for any $W\in {}^C\vc, V\in \vc.$

If $W\in {}^C\vc$ has comodule structure given by $\rho_W\to C\ot W$, then we define
$\pi_W:W\ot {}^*W\to  C,$ the morphisms given by $\pi_W=\bar{\psi}^C_{W,W}(\rho)$. Recall that, natural isomorphisms $\bar{\psi}$ were defined in \eqref{duals2}. Maps $\pi_W$ are dinatural transformations, and they satisfy Equation \eqref{new.3.5}.

Let $A\in \vc$ be another object, equipped with dinatural transformations $\lambda_W:W\ot {}^*W\to  A$ such that they satisfy Equation \eqref{new.3.5}. Define $h$ as the composition
$$h: C\xrightarrow{\id_C\ot {}^*\varepsilon}C\ot {}^*C   \xrightarrow{\lambda_C} A.$$
Since $\lambda$ is dinatural, and it satisfies  \eqref{new.3.5}, one can see that $h\circ \pi_W= \lambda_W$. This proves that, indeed, $C(\uc)\simeq C$.
\epf



\begin{prop}\label{factorization-F} Let $\Bc$ be a right $\vc$-module category, and $(F,c):\Bc\to \vc$ be a right exact module functor. Set $C=C(F)$ the coalgebra defined in Proposition \ref{coalg-coend}.
\begin{itemize}

\item[1.] The functor $(F,c):\Bc\to \vc$ factorizes as
\begin{equation}
\xymatrix{
&{}^C\vc\ar[dr]^-{\uc}\ar@{}[d]|{}&\\
\Bc\ar[ru]^-{\widehat{F}}\ar[rr]_-{F}&&\vc.
}
\end{equation} 
Here $\uc:{}^C\vc \to\vc$ is the forgetful functor, and the functor $\widehat{F}$ is a $\vc$-module functor.
\item[2.] If $F$ is exact (respect. faithful) then $\widehat{F}$ is exact (respect. faithful). 
\end{itemize}
\end{prop}
\pf 1. For any $A\in \Bc$, define $\widehat{F}(A)=(F(A),\rho_A),$ where 
$$\rho_A=\psi^C_{F(A),F(A)}(\pi_A):F(A)\to C\ot F(A).$$ Using diagrams \eqref{coproduct-c}, \eqref{counit-c}, one can prove that
$$(\id_C\ot \rho_A)\rho_A=(\Delta\ot \id)\rho_A,$$
$$(\varepsilon\ot\id)\rho_A=\id_{F(A)}.$$


\bigbreak

2. Clearly, if $F$ is faithful, then $\widehat{F}$ is faithful. Assume that $F$ is left exact. Let $f:A\to B$ be a morphism in $\Bc$ with kernel $k=\ker f: K\to A$. Since $F$ is left exact, then, $F(k)=\ker F(f)$. We only need to prove that, the morphism $F(k):F(K)\to F(A)$ is a map of $C$-comodules. That is, we need to prove the equality
\begin{equation}\label{exact-F} (\id\ot F(k))  \psi^C_{F(K),F(K)}(\pi_K)= \psi^C_{F(A),F(A)}(\pi_A)  F(k).
\end{equation}
Using the naturality of $\psi$, it follows that
\begin{align*}  \psi^C_{F(A),F(A)}(\pi_A)  F(k)&=  \psi^C_{F(K),F(A)}(\pi_A (F(k)\ot \id))\\
&=\psi^C_{F(K),F(A)}(\pi_K (\id \ot {}^*F(k)))\\
&=(\id \ot F(k)) \psi^C_{F(K),F(K)}(\pi_K ).
\end{align*}
The second equality follows from the dinaturality of $\pi$, the third equality follows again by the naturality of $\psi$. The proof that, if $F$ is right exact, then $\widehat{F}$ is right exact, follows similarly.
\epf
