---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-015-52-some-natural-module-transformations
section_title: "Some natural module transformations"
section_number: 5.2
pages: 24-26
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.926
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B →C is an exact"
---
\label{subsection:nat-bimod} It is known that natural transformations between additive functors are additive. For example, if $(F,\xi)$ is an additive monoidal functor, then, natural isomorphisms
$$\xi_{A,B}:F(A)\ot F(B)\to F(A\ot B), $$
are additive in each variable. In this section, we shall study what happens when $F$ is a monoidal module functor. We aim at proving that $\xi$ is a \textit{module} natural transformation in  the second variable. 

\begin{lema}\label{left-mod-nat} If $\Bc$ is a right monoidal $\ca$-module category, then for any $A\in \Bc$, the functor $L_A:\Bc\to \Bc$, $L_A(B)=A\ot B$ is a $\ca$-module functor.
\end{lema}
\pf For any $B\in \Bc, V\in \ca$, the module structure  of the functor $L_A$ is given by
$$\eta_{B,V}: A\ot (B \triangleleft V)\to (A\ot B) \triangleleft V,$$
$$\eta_{B,V}= l^{-1}_{A\ot B, V}(\id_A\ot l_{B,V})$$ 
Let us prove that $\eta$ satisfies   \eqref{modfunctor11}. Using that isomorphisms $l$ satisfy diagram \eqref{tens-acting2}, it follows that for any $C\in \Bc$ and any $V, W\in \ca$ we have that
\begin{equation}\label{on-l-11}
l^{-1}_{C, V\ot W}= l^{-1}_{C\triangleleft V,  W}(l^{-1}_{C,V}\ot \id_{\uno \triangleleft W})(\id_C\ot l_{\uno \triangleleft V,W}).
\end{equation}
 On one hand we have that 
\begin{align*}
\eta_{B,V\ot W}=& l^{-1}_{A\ot B, V\ot W}(\id_A\ot l_{B,V\ot W})\\
=& l^{-1}_{(A\ot B)\triangleleft V,  W}(l^{-1}_{A\ot B,V}\ot \id_{\uno \triangleleft W})(\id_{A\ot B}\ot l_{\uno \triangleleft V,W}) (\id_{A\ot B}\ot l^{-1}_{\uno \triangleleft V,W})\\
& (\id_A\ot l_{B,V}\ot \id_{\uno \triangleleft W})(\id_A\ot l_{B\triangleleft V,W})\\
=&l^{-1}_{(A\ot B)\triangleleft V,  W}(l^{-1}_{A\ot B,V}\ot \id_{\uno \triangleleft W})  (\id_A\ot l_{B,V}\ot \id_{\uno \triangleleft W})(\id_A\ot l_{B\triangleleft V,W})
\end{align*}
The second equation follows from using \eqref{on-l-11}. On the other hand $$(\eta_{B,V}\triangleleft \id_W) \eta_{B\triangleleft V, W}$$ is equal to
\begin{align*} =&(l^{-1}_{A\ot B, V} \triangleleft\id_W)(\id_A\ot l_{B,V}\ot \id_{\uno \triangleleft W}) l^{-1}_{A\ot (B \triangleleft V), W} (\id_A\ot l_{B \triangleleft V, W})\\
=&(l^{-1}_{A\ot B, V} \triangleleft\id_W)  l^{-1}_{A\ot B \ot (\uno\triangleleft V), W}  (\id_A\ot l_{B,V}\ot \id_{\uno \triangleleft W})  (\id_A\ot l_{B \triangleleft V, W})\\
=&l^{-1}_{(A\ot B)\triangleleft V,  W}(l^{-1}_{A\ot B,V}\ot \id_{\uno \triangleleft W})  (\id_A\ot l_{B,V}\ot \id_{\uno \triangleleft W})(\id_A\ot l_{B\triangleleft V,W}).
\end{align*}
The second and third equalities follow from the naturality of $l$.
\epf



\begin{prop}\label{bimodule-funct} Assume that $\Bc$ is a monoidal right $\ca$-module category and $(F,  c, \xi):\Bc\to \ca$ a monoidal module functor. The following assertions hold.
\begin{enumerate}
\item[(i)] The category $\Bc$ has structure of $\ca$-bimodule category. 


\item[(ii)]  There are $\ca$-module funtors
$$H, \widetilde{H}:\Bc\boxtimes_\ca \Bc\to \ca,$$ such that
$$ H(A\boxtimes B)=F(A\ot B), \quad \widetilde{H}(A\boxtimes B)=F(A)\ot F(B),$$
for any $A, B\in \Bc$. 
\item[(iii)] The monoidal structure of the functor $F$ defines a natural module isomorphism $\xi:\widetilde{H} \to H$.
\end{enumerate}
\end{prop}
\pf (i). From Proposition \ref{lm_section} there is a section $G:\ca\to \Bc$ of the functor $F$. Define the left action $\triangleright:\ca\times \Bc\to \Bc$ as $V\triangleright B=G(V)\ot B$. With this action $\Bc$ becomes a $\ca$-bimodule category. Thus, we can consider the Deligne tensor product over $\ca$, $\Bc\boxtimes_\ca \Bc$. This category has an obvious right $\ca$-module category structure.

One can prove that functors $\Bc\times \Bc\to \ca$ given by
$$(A,B)\mapsto F(A\ot B), \quad (A,B)\mapsto F(A)\ot F(B),$$
are $\ca$-balanced, thus defining functors $H$ and $\widetilde{H}$. The (right) $\ca$-module structure of the functor $\widetilde{H}$ is the one inherited from the functor $F$. The module structure of the functor $H$ is more involved. One can prove that natural transformations
$$e_{A,B,V}: F(A\ot (B\triangleleft V))\to F(A\ot B) \ot V,$$
$$e_{A,B,V}= c_{A\ot B, V} F(l^{-1}_{A\ot B, V}(\id_A\ot l_{B,V})) $$
are $\ca$-balanced, thus defining natural transformations 
$$e_{X,V}: H(X\triangleleft V)\to H(X)\triangleleft V,$$
for any $X\in \Bc\boxtimes_\ca \Bc$, $V\in \ca$. One can prove also that $(H,e)$ is a module functor. Note that $e$ is the module structure resulting from the composition of module structures of $F$ and the functor $L_A$, presented in Lemma \ref{left-mod-nat}. This proves (ii).



(iii). To prove that $\xi$ is a natural module transformation in the second variable, we need to verify that the diagram
\begin{equation}\label{coproduct-cf}
\xymatrix{
 \widetilde{H}(A,B\triangleleft V) \ar[d]_{\id_{F(A)}\ot c_{B,V}}\ar[rr]^{\xi_{A,B\triangleleft V}}&& H(A ,B\triangleleft V) 
 \ar[d]^{e_{A,B,V}} \\
 \widetilde{H}(A,B) \ot V \ar[rr]_{\xi_{A,B}\ot \id_V }&& H(A ,B) \ot V,}
\end{equation}
is commutative for any $A, B\in \Bc$, $V\in \ca$. Here $$e_{A,B,V}= c_{A\ot B, V} F(l^{-1}_{A\ot B, V}(\id_A\ot l_{B,V})). $$ 
We have
\begin{align*} e_{A,B,V} &\xi_{A,B\triangleleft V}=  c_{A\ot B, V} F(l^{-1}_{A\ot B, V}(\id_A\ot l_{B,V}))\xi_{A,B\triangleleft V}\\
&=(\id\ot c_{\uno, V}) \xi^{-1}_{A\ot B, \uno\triangleleft V} F(\id_A\ot l_{B,V}) \xi_{A,B\triangleleft V}\\
&=(\id\ot c_{\uno, V}) \xi^{-1}_{A\ot B, \uno\triangleleft V} \xi_{A,B\ot (\uno \triangleleft V)}(\id_{F(A)}\ot F(l_{B,V}))\\
&=(\id\ot c_{\uno, V}) (\xi_{A,B}\ot \id_{F(\uno \triangleleft V)})(\id_{F(A)}\ot \xi^{-1}_{B, \uno \triangleleft V}) (\id_{F(A)}\ot F(l_{B,V}))\\
&=(\xi_{A,B}\ot \id_{ V}) (\id_{F(A)}\ot (\id_{F(B)}\ot c_{\uno, V})\xi^{-1}_{B, \uno \triangleleft V}  F(l_{B,V})) \\
&=(\xi_{A,B}\ot \id_{ V})  (\id_{F(A)}\ot c_{B, V}).
\end{align*}
The second equality follows from \eqref{monoidal-mod-functor}, the third equality follows from the naturality of $\xi$, the fourth one follows from \eqref{monoidal-functor}. The last equality follows  from \eqref{monoidal-mod-functor}.
\epf
