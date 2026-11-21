---
doc_id: arxiv-math-0111205v1
doc_title: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001"
section_id: sec-018-81-an-adjoint-for-the-forgetful-functor-2z-12cri
section_title: "An adjoint for the forgetful functor $\2Z_1(\2C)\rightarrow\2C$"
section_number: 8.1
pages: 49-50
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.921
doc_brief: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001 — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
\label{ss-adj}
In Section \ref{sec-morita} we proved that the functor $F: \2Z_1(\2C)\rarr\2B$ is fully 
faithful and essentially surjective. By \cite[Theorem IV.4.1]{cwm} this implies that $F$
has a two-sided adjoint $G: \2B\rarr\2Z_1(\2C)$. Together with Lemma\ \ref{adj} this implies
\[ \Hom_\2C(X,Y)\cong\Hom_\2B(F(X,e_X),\oj (Y\boxtimes\11)J)\cong
   \Hom_{\2Z_1(\2C)}((X,e_X),G(\oj (Y\boxtimes\11)J)), \]
where $(X,e_X)\in\2Z_1(\2C), Y\in\2C$. With the forgetful functor 
$H: \2Z_1(\2C)\rarr\2C, (X,e_X)\mapsto X$ this becomes
\begin{equation}\Hom_\2C(H(X,e_X),Y)\cong \Hom_{\2Z_1(\2C)}((X,e_X),G(\oj (Y\boxtimes\11)J)).
\label{adjt}\end{equation}
We thus have  
\bprop The forgetful functor $H: \2Z_1(\2C)\rarr\2C, (X,e_X)\mapsto X$ has a two-sided
adjoint $K: \2C\rarr\2Z_1(\2C),\ X\mapsto G(\oj (X\boxtimes\11)J)$. On the objects one has
\begin{equation}K(Y)\cong \bigoplus_{(X,e_X)} \dim\Hom_\2C(X,Y) \, (X,e_X), 
\label{kf}\end{equation}
where the summation is over the isomorphism classes of simple objects in $\2Z_1(\2C)$. 
\eprop
\prf Eq.\ (\ref{adjt}) just says that $K$ is a right adjoint of $H$. That $K$ is also a
left adjoint of $H$ is proven in the same way. One must also show that the isomorphisms in
(\ref{adjt}) are natural w.r.t.\ $(X,e_X)$ and $Y$. We leave this to the reader. For
$Y=X_i$ and $(X,e_X)$ simple, (\ref{adjt}) implies that $K(X_i)$ contains $(X,e_X)$ with 
multiplicity $\dim\Hom_\2C(X,X_i)$. For general $Y$ we have
\[ K(Y)\cong \bigoplus_{i\in \Gamma} \dim\Hom(X_i,Y) \bigoplus_{(X,e_X)} 
   \dim\Hom_\2C(X,X_i) \, (X,e_X), \]
and (\ref{kf}) follows by semisimplicity of $\2C$. \qed

\brem By the general theory \cite{mue09} there is a dual Frobenius algebra 
$\hat{\5Q}=(\hat{Q},\ldots)$ in $\2B$, where $\hat{Q}=\oj J$. Under the equivalence 
$\2Z_1(\2C)\stackrel{\otimes}{\simeq}\2B$, $\hat{Q}$ corresponds to
\begin{equation} G(\oj J)=K(\11)\cong \bigoplus_{(X,e_X)} \dim\Hom_\2C(X,\11) \, (X,e_X).
\label{k_1}\end{equation}
Thus this object is part of the Frobenius algebra in $\2Z_1(\2C)$ which establishes the weak
monoidal Morita equivalence $\2Z_1(\2C)\approx\2C\boxtimes\2C^\op$. $K(\11)$ clearly
contains the unit $(\11,\id)$ of $\2Z_1(\2C)$ with multiplicity one. The reader might
find it amusing to identify explicitly the morphisms $w, w'$ in $\2Z_1(\2C)$ which come with
the canonical Frobenius algebra.
\erem
