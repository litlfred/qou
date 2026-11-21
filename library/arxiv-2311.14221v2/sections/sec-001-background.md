---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-001-background
section_title: "Background"
section_number: null
pages: 2-3
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.971
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B →C is an exact"
---
The main objective of the present paper is to present a version of the Tannaka-Krein type reconstruction theorems. It is known that if $\Bc$ is a $\ku$-linear abelian locally finite category, $F:\Bc\to \vect_\ku$ is a fibre functor, that is an exact faithful functor, then the coend
$$ C=\int^{B\in \Bc} F(B)\otk F(B)^*,$$
has structure of $\ku$-coalgebra, and the functor $F$ factorizes as 
\begin{equation*}
\xymatrix{
\Bc
\ar[rrr]^-{\qquad\widehat{F}}
\ar[drr]_-{F}
&&&
\mathrm{Comod}(C)
\ar[dl]^-{\uc}\ar@{}[d]|{}&\\
&&\vect_\ku,&
}
\end{equation*} 
where $f:\mathrm{Comod}(C)\to \vect_\ku$ is the forgetful functor, and $\widehat{F}$ is a category equivalence. We refer the reader to \cite{H}, \cite{PS} and references therein. 
If, moreover, $\Bc$ is a monoidal rigid category, and $F$ is a monoidal functor, then it is possible to endow the coalgebra $C$ with structure of Hopf algebra. Succinctly, monoidality of $\Bc$ gives $C$ a product, turning it into a bialgebra, and rigidity of $\Bc$ endows $C$ with an antipode. 

\medbreak

Some generalizations of this result appeared in the literature. We only mention some of them. In these more general versions, a fibre functor $F:\Bc\to \vc$ is considered, where $\vc$ is an arbitrary monoidal category. In some versions, the object $C$ is not a Hopf algebra in $\ca$. For example in \cite{BV},  it is shown that if the functor $F$ has a right adjoint $G:\ca\to \Bc$, then, the associated monad to this adjunction $T=F\circ G:\vc\to \vc$ is a bimonad, and there is a commutative diagram
\begin{equation*}
\vspace{.1cm}
\xymatrix{
\Bc\;\;
\ar[rr]^-{\widehat{F}}
\ar[dr]_-{F}
&&
\mathcal{C}^T
\ar[dl]^-{\uc}\ar@{}[d]|{}&\\
&\;\mathcal{C}.
\ar@/^1.5pc/@[gray][ul]^{G\;\;}&
}
\end{equation*} 

Here $f: \vc^T\to \vc$ is the forgeful functor. Beck's monadicity Theorem implies that the functor $\widehat{F}:\Bc\to \ca^T$ is a monoidal equivalence. Rigidity of both monoidal categories $\Bc, \vc$ imply that $T$ has a Hopf monad structure. In \cite{Li1}, \cite{Li2} Lyubashenko reconstructed the object $C$ as a coend $\int^{B\in \Bc} F(B)\boxtimes F(B)^*$, belonging to some completion of the Deligne tensor product $\vc \boxtimes \vc$, and it turns out to be a {\it squared coalgebra}. In the work of Majid \cite{Majid}, he started with a monoidal functor $F:\Bc\to \vc$, where $\vc$ is a braided monoidal category, and he reconstructed a Hopf algebra $C=\int^{B\in \Bc} F(B)^*\ot F(B)$, and set up a commutative diagram
\begin{equation*}
\vspace{.1cm}
\xymatrix{
\Bc\;\;
\ar[rr]^-{\widehat{F}}
\ar[dr]_-{F}
&&
{}^C\mathcal{C}
\ar[dl]^-{\uc}\ar@{}[d]|{}&\\
&\;\mathcal{C}.&
}
\end{equation*}
With this generality, the functor $\widehat{F}$ no longer need to be an equivalence.
