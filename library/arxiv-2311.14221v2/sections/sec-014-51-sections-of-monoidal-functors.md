---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-014-51-sections-of-monoidal-functors
section_title: "Sections of monoidal functors"
section_number: 5.1
pages: 22-24
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.941
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B →C is an exact"
---
\begin{defi}\label{def_section}  Let $\vc, \Bc$ be tensor categories. If $F:\Bc\to \vc$ is a tensor functor, a \textit{section} to $F$ is a right exact tensor functor $G:\vc\to \Bc$ such that $F\circ G\simeq \Id_\vc$ as monoidal functors. 
\end{defi} 
\begin{exa} \begin{enumerate}
\item Any (linear) tensor functor $F:\Bc \to \vect_\ku$ has a canonical section given by
$$G:\vect_\ku \to \Bc,$$
$$G(V)= V  \bullet \uno.$$
\medbreak
Here the action $\bullet:\vect_\ku\times \Bc\to \Bc$, is the one presented in  \eqref{vect-action}.



\item The previous example can be generalized to  other kinds of fiber functors. If $\vc$ is a tensor category that acts on another tensor category $\Bc$ then, any monoidal functor $F:\Bc\to \vc$ that is also a $\vc$-module functor has a section given by $G:\vc\to \Bc$, $G(V)=V\triangleright \uno$. See Proposition \ref{lm_section} below. 


\medbreak




\item If $(\vc,\sigma)$ is a braided tensor category, and $H\in \vc$ is a Hopf algebra with unit given by $u:\uno\to H$, then the forgetful functor $\uc: {}^H\vc\to \vc$ has a section given by $G:\vc\to {}^H\vc$, $G(V)=(V,\rho^t_V)$. Here  $\rho^t_V=u\ot \id_V$ is the trivial comodule structure.

\medbreak
\item Let $H$ be a Hopf algebra and $R$ be a  Hopf algebra in the category of Yetter-Drinfeld modules ${}^H_H\YD$. Consider the corresponding Hopf algebra obtained by bosonization $R\# H$. Let us consider the functor $$F:\Rep(R\# H)\to \Rep(H), \quad F(V)=V.$$ The action of $H$ on $V$ is given by $h\cdot v= (1\# h)\cdot v$. The functor $F$ has a section given by $G:\Rep(H)\to \Rep(R\# H)$ given by $G(V)=V$, where the action of $R\# H$ on $V$ is given by
$$(r\# h)\cdot v=\varepsilon(r) h\cdot v.$$

\item Let $(\vc,\sigma)$ be a braided tensor category. The forgetful functor from the center of $\vc$, $\uc :Z(\vc)\to \vc$,  has a section given by the inclusion $\vc \hookrightarrow Z(\vc)$, $V\mapsto (V,\sigma)$.

\end{enumerate}
\end{exa}



\begin{prop}\label{lm_section} Let $\Bc, \vc$ be tensor categories, and $(F,\xi):\Bc\to \vc$ be a monoidal functor. The following notions are equivalent:
\begin{itemize}
\item[(i)] The functor $F$   has a section;

\item[(ii)] $\Bc$ is a right monoidal $\vc$-module category (in the sense of Definition \ref{definition:monoidal-mod}) and $F$ is a  monoidal module  functor.
\end{itemize}
\end{prop}
\pf Let us only give a sketch of the proof.  (i) implies (ii): Assume that $(G, \zeta):\vc\to \Bc$ is a monoidal section to $F$. Let $\alpha:F\circ G\to \Id$ be a natural monoidal isomorphism. Define the right action of $\vc$ on $\Bc$ as
$$B \triangleleft V:= B\ot G(V), $$
for any $B\in \Bc$, $V\in \vc$. The associativity of this action is given by
$$ m_{B,V,W}: B \triangleleft (V\ot W)\to (B \triangleleft  V) \triangleleft W,$$
$$m_{B,V,W}= \id_B\ot \zeta^{-1}_{V,W},$$
for any $B\in \Bc$, $V, W\in \ca$. Turns out that $\Bc$ is a monoidal module category with isomorphisms
$$l_{B,V}: B \triangleleft V\to B\ot (\uno \triangleleft V),$$
$$l_{B,V}=\id_{B\ot G(V)}.$$ 



With this action, $F$ is a module functor. The module structure of the functor $F$ is given by
$$ c_{B,V}:F(B \triangleleft V)\to F(B)\ot V,$$
$$ c_{B,V}= (\id_{F(B)}\ot \alpha_V) \xi^{-1}_{B,G(V)} F(l_{B,V}).$$
Since $c_{\uno,V}=\alpha_V$, then it follows that Equation \eqref{monoidal-mod-functor} is fulfilled, that is $(F,\xi, c)$ is a monoidal module functor. 

\medbreak
Let us prove now that (ii) implies (i): Assume that $(F,\xi, c):\Bc\to \ca$ is a monoidal $\ca$-module functor. Define 
$G:\vc\to \Bc$, $G(V)=\uno \triangleleft V $. Axiom \eqref{tens-acting2} implies that  isomorphisms
$$l^{-1}_{\uno\triangleleft V, W }: G(V)\ot G(W)  \to G(V\ot W),$$
endow $G$ with the structure of monoidal functor. Define natural isomorphisms $\alpha_V:F(G(V))=F(\uno \triangleleft V)\to V$, $\alpha_V=c_{\uno, V}$. Let us check that they are monoidal natural isomorphisms. For this, we need to verify that equation
\begin{equation}\label{nat-c1} (c_{\uno, V}\ot c_{\uno, W})= c_{\uno, V\ot W} F(l^{-1}_{\uno \triangleleft V,W}) \xi_{\uno \triangleleft V,\uno \triangleleft W}
\end{equation}
is satisfied. Using that $c$ satisfies diagram \eqref{modfunctor11}, it follows that the right hand side of Equation  \eqref{nat-c1}  is equal to
\begin{align*} &=(c_{\uno, V}\ot \id_W) c_{\uno \triangleleft V, W} F(l^{-1}_{\uno \triangleleft V,W}) \xi_{\uno \triangleleft V,\uno \triangleleft W}\\
&=(c_{\uno, V}\ot \id_W) (\id_{F(\uno \triangleleft V)}\ot c_{\uno, W} ) \xi^{-1}_{\uno \triangleleft V,\uno \triangleleft W} F(l_{\uno \triangleleft V,W}) F(l^{-1}_{\uno \triangleleft V,W}) \xi_{\uno \triangleleft V,\uno \triangleleft W}\\
&=(c_{\uno, V}\ot c_{\uno, W}).
\end{align*}
The second equation follows from \eqref{monoidal-mod-functor}
\epf

\begin{rmk} Constructions in Proposition \ref{lm_section} are reciprocal in the following sense. If $\Bc$ is a right monoidal $\ca$-module category and $G:\ca\to \Bc$ is the monoidal functor $G(V)= \uno\triangleleft V$, then one can endow $\Bc$ with a  right $\ca$-module structure
$$ B\blacktriangleleft V= B\ot G(V),$$
for any $B\in \Bc$, $V\in \ca$. Turns out, that the identity functor $\Id: (\Bc, \triangleleft)\to (\Bc, \blacktriangleleft)$ is an equivalence of module categories.
\end{rmk}
