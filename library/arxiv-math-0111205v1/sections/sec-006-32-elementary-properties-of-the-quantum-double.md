---
doc_id: arxiv-math-0111205v1
doc_title: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001"
section_id: sec-006-32-elementary-properties-of-the-quantum-double
section_title: "Elementary properties of the quantum double"
section_number: 3.2
pages: 9-13
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.944
doc_brief: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001 — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
\bdefin The center $\2Z_1(\2C)$ of a strict monoidal category $\2C$ has as objects pairs
$(X,  e_X)$, where $X\in\2C$ and $ e_X$ is a half braiding. The morphisms are given by 
\bea \lefteqn{ \Hom_{\2Z_1(\2C)}((X, e_X),(Y, e_Y)= \{ t\in\Hom_\2C(X,Y) \ | } \nn \\
 && \quad\quad \id_X\otimes t \mcirc e_X(Z)= e_Y(Z)\mcirc t\otimes\id_X \quad 
\forall Z\in\2C \}. \label{dmor}\eea
The tensor product of objects is given by 
$(X, e_X)\otimes(Y, e_Y)=(XY, e_{XY})$, where
\begin{equation} e_{XY}(Z)= e_X(Z)\otimes\id_Y\mcirc\id_X\otimes e_Y(Z).
\label{dprod}\end{equation}
The tensor unit is $(\11,e_\11)$ where $e_\11(X)=\id_X$. The composition and tensor
product of morphisms are inherited from $\2C$. The braiding is given by 
\[  c((X, e_X),(Y, e_Y))=  e_X(Y). \]
\label{defdouble}
\edefin

For the proof that $\2Z_1(\2C)$ is a strict braided tensor category we refer to \cite{ka}. 
The following is immediate from the definition of the center $\2Z_1(\2C)$:

\blemma If $\2C$ is $\7F$-linear then so is $\2Z_1(\2C)$. 
If the unit $\11$ of $\2C$ is simple, then $\11_{\2Z_1(\2C)}$ is simple.
\elemma

In \cite[Proposition 1]{s} it is proven that the center of an abelian monoidal category is
abelian. In this paper we do not use the language of abelian categories since the notions
of (co)kernels are not really needed. (Yet semisimple categories are abelian if we assume
existence of a zero object.) Therefore, we prove two lemmas which show that the center
construction behaves nicely w.r.t.\ direct sums and subobjects. The first result is
contained in \cite{s}, but we repeat it for the sake of completeness.

\blemma If $\2C$ has direct sums then also $\2Z_1(\2C)$ has direct sums. \elemma 
\prf Let $(Y, e_Y), (U, e_U)$ be objects in $\2Z_1(\2C)$. Let
$\2C\ni Z\cong Y\oplus U$ with morphisms $v\in\Hom_\2C(Y,Z), w\in\Hom_\2C(U,Z)$,
$v'\in\Hom_\2C(Z,Y), w'\in\Hom_\2C(Z,U)$ satisfying 
$v'\circ v=\id_Y,w'\circ w=\id_U, v\circ v'+w\circ w'=\id_Z$.
Defining $ e_Z(X)\in\Hom_\2C(Z X,XZ)$ for all $X\in\2C$ by
\[  e_Z(X)= \id_X\otimes v \mcirc e_Y(X)\mcirc v'\otimes\id_X +
   \id_X\otimes w \mcirc e_U(X)\mcirc w'\otimes\id_X, \]
we claim that $(Z,  e_Z)$ is an object of $\2Z_1(\2C)$ and 
\begin{equation}(Z, e_Z)\cong(Y, e_Y)\oplus (U, e_U). 
\label{sum}\end{equation}
Naturality of $ e_Z(X)$ w.r.t.\ $X$ is obvious, and (\ref{hb-ii}) is very
easily verified using $v'\circ w=0$. Finally, we have
\[  e_Z(X)\mcirc v\otimes\id_X= \id_X\otimes v \mcirc e_Y(X), \]
which is just the statement that 
$v\in\Hom_{\2Z_1(\2C)}((Y, e_Y),(Z, e_Z)$. The analogous statement holding
for $v', w, w'$, (\ref{sum}) follows. \qed

\blemma If $\2C$ has subobjects then also $\2Z_1(\2C)$ has subobjects.  
\label{subobj}\elemma
\prf Let $(Y, e_Y)\in \2Z_1(\2C)$ and let $e$ be an idempotent in 
$\End_{\2Z_1(\2C)}((Y,e_Y))$. By definition of $\2Z_1(\2C)$ this means that $e$ is an
idempotent in $\End_\2C(Y)$ such that 
\begin{equation}\id_X\otimes e\mcirc e_Y(X)= e_Y(X)\mcirc e\otimes\id_X \quad 
  \forall X\in\2C. 
\label{ez}\end{equation}
Since $\2C$ has subobjects there are $U\in\2C$ and $v\in\Hom_\2C(U,Y), v'\in\Hom_\2C(Y,U)$ 
such that $v\circ v'=e$ and $v'\circ v=\id_U$. Defining
\[  e_U(X)=\id_X\otimes v'\mcirc  e_Y(X)\mcirc v\otimes\id_X
  \in\Hom_\2C(U X,XU),   \quad X\in\2C, \]
naturality w.r.t.\ $X$ is again obvious. Now,
\bean \lefteqn{ e_U(X_1X_2) =\id_{X_1X_2}\otimes v'\mcirc 
   e_Y(X_1X_2)\mcirc v\otimes\id_{X_1X_2}} \\
  &&= \id_{X_1X_2}\otimes v'  \mcirc\id_{X_1}\otimes e_Y(X_2) \mcirc
    e_Y(X_1)\otimes\id_{X_2}\mcirc v\otimes\id_{X_1X_2} \\
  &&= \id_{X_1X_2}\otimes v'  \mcirc\id_{X_1}\otimes e_Y(X_2) \mcirc
 \id_{X_1}\otimes v\otimes\id_{X_2} \\
  && \quad\mcirc\id_{X_1}\otimes v'\otimes\id_{X_2} \mcirc
    e_Y(X_1)\otimes\id_{X_2}\mcirc v\otimes\id_{X_1X_2} \\
  &&= \id_{X_1}\otimes e_U(X_2) \mcirc   e_U(X_1)\otimes\id_{X_2},
\eean
whereby $ e_U$ is a half braiding and $(U, e_U)$ an object in $\2Z_1(\2C)$. 
We used $v\mcirc v'=e$, (\ref{ez}) and $e\mcirc v=v\mcirc v'\mcirc v=v$.
Using the same facts we finally compute
\[ \id_X\otimes v\mcirc e_U(X)=\id_X\otimes v\mcirc\id_X\otimes v'
  \mcirc  e_Y(X)\mcirc v\otimes\id_X=
   e_Y(X)\mcirc v\otimes\id_X. \]
Thus $v\in\Hom_{\2Z_1(\2C)}((U, e_U),(Y, e_Y))$ and we have 
$(U, e_U)\prec(Y, e_Y)$. \qed

\blemma \label{l3}
Let $\2C$ be pivotal and $e_Y$ a half braiding satisfying (i-iv). Then
\begin{equation} e_Y(\ol{X})=\id_{\ol{X}Y}\otimes \ol{\ve}(X) \mcirc
   \id_{\ol{X}}\otimes e_Y(X)^{-1}\otimes\id_{\ol{X}}\mcirc \ve(\ol{X})
   \otimes \id_{Y\ol{X}}. \label{vebar}\end{equation}
\elemma
\prf By naturality and the braid relation we have
\[ \ve(\ol{X})\otimes\id_Y = e_Y(\ol{X}X) \mcirc\id_Y\otimes \ve(\ol{X})=
  \id_{\ol{X}}\otimes e_Y(X)\mcirc e_Y(\ol{X})\otimes\id_X\mcirc
  \id_Y\otimes \ve(\ol{X}) \]
and using the invertibility of $e_Y(X)$ we get
\[ \id_{\ol{X}}\otimes e_Y(X)^{-1}\mcirc \ve(\ol{X})\otimes\id_Y  = 
   e_Y(\ol{X})\otimes\id_X \mcirc \id_Y\otimes \ve(\ol{X}). \]
Now (\ref{vebar}) follows by a use of the duality equations, see, e.g., 
\cite[Subsection 2.3]{mue09}.
\qed 

\bprop \label{hb-conj}
Let $\2C$ be (strict) pivotal. Then also $\2Z_1(\2C)$ is (strict) pivotal, the
dual $\ol{(Y, e_Y)}$ being given by $(\ol{Y}, e_{\ol{Y}})$, where $e_{\ol{Y}}(X)$ is
defined by 
\[
\begin{diagram}
\ol{Y}\otimes X & \rTo^{\id_{\ol{Y}X}\otimes \ve(Y)} & \ol{Y}\otimes X\otimes Y\otimes\ol{Y} &
\rTo^{\id_{\ol{Y}}\otimes e_Y(X)^{-1}\otimes\id_{\ol{Y}}} & \ol{Y}\otimes Y\otimes X\otimes\ol{Y} & \rTo 
\end{diagram}
\]
\be
\begin{diagram}
   & \rTo^{\ol{\ve}(\ol{Y})\otimes\id_{X\ol{Y}}} & X\otimes\ol{Y}
\end{diagram}
\label{eybar}\end{equation}



The evaluation and coevaluation maps are inherited from $\2C$:
\[ \ve((Y,  e_Y))=\ve(Y), \quad \ol{\ve}((Y,  e_Y))=\ol{\ve}(Y). 
\]
If $\2C$ is spherical then also $\2Z_1(\2C)$ is spherical.
\eprop
\prf We begin by showing that $e_{\ol{Y}}(\cdot)$ is a half braiding for $\ol{Y}$. By
construction we have $ e_{\ol{Y}}(X)\in\Hom_\2C(\ol{Y}X,X\ol{Y})$, and naturality
w.r.t.\ $X$ follows easily from the corresponding property for $ e_Y$. Now
\bean \lefteqn{ e_{\ol{Y}}(X_1X_2) = \ol{\ve}(\ol{Y})\otimes\id_{X_1X_2\ol{Y}}
  \mcirc \id_{\ol{Y}}\otimes e_Y(X_1X_2)^{-1}\otimes\id_{\ol{Y}} 
  \mcirc \id_{\ol{Y}X_1X_2}\otimes \ve(Y) } \\
 &&= \ol{\ve}(\ol{Y})\otimes\id_{X_1X_2\ol{Y}}\mcirc \id_{\ol{Y}}\otimes
   e_Y(X_1)^{-1}\otimes\id_{X_2\ol{Y}} \\
  && \quad\quad\mcirc\id_{\ol{Y}X_1}
  \otimes e_Y(X_2)^{-1}\otimes\id_{\ol{Y}}\mcirc
  \id_{\ol{Y}X_1X_2}\otimes \ve(Y) \\
 &&= \id_{X_1}\otimes \ol{\ve}(\ol{Y})\otimes\id_{X_2\ol{Y}} \mcirc
  \id_{X_1\ol{Y}}\otimes e_Y(X_2)^{-1}\otimes\id_{\ol{Y}}\mcirc
  \id_{X_1\ol{Y}X_2}\otimes \ve(Y) \\
  && \quad\quad\mcirc  \ol{\ve}(\ol{Y})\otimes\id_{X_1\ol{Y}X_2}\mcirc
  \id_{\ol{Y}}\otimes e_Y(X_1)^{-1}\otimes\id_{\ol{Y}X_2}\mcirc
  \id_{\ol{Y}X_1}\otimes\ve(Y)\otimes\id_{X_2}\\
 &&=\id_{X_1}\otimes e_{\ol{Y}}(X_2)\mcirc e_{\ol{Y}}(X_1)\otimes
   \id_{X_2}.
\eean
In the third equality we have used the duality equation 
$\id_Y\otimes \ol{\ve}(\ol{Y})\mcirc \ve(Y)\otimes\id_Y=\id_Y$ and the interchange law. 

In view of the definition (\ref{eybar}) of $e_{\ol{Y}}(X)$ together with
$e_Y(\11)=\id_Y$ and the duality equation we have $e_{\ol{Y}}(\11)=\id_{\ol{Y}}$. Now
Lemma \ref{iii-iv} implies invertibility of $e_{\ol{Y}}(X)$ for all $X$.

It remains to show that $\ve(Y):\11_\2C\rarr Y\otimes\ol{Y}$ is actually in
\[ \Hom_{\2Z_1(\2C)}(\11_{\2Z_1(\2C)},(Y,e_Y)\otimes(\ol{Y},e_{\ol{Y}}))=
   \Hom_{\2Z_1(\2C)}((\11,\id),(Y\ol{Y},e_{Y\ol{Y}})), \]
which in view of (\ref{dmor}) amounts to 
\begin{equation} \label{conjd}
\begin{tangle}
\object{Z}\Step\object{Y}\Step\object{\ol{Y}}\\
\id\Step\ev\\
\object{Z}
\end{tangle}
\quad=\quad
\begin{tangle}
\object{Z}\Step\object{Y}\Step\object{\ol{Y}}\\
\xx\mobj{e_Y(Z)}\Step\id\\
\id\Step\xx\mobj{e_{\ol{Y}}(Z)}\\
\ev\Step\id\\
\step[4]\object{Z}
\end{tangle}
\end{equation}
With the definition (\ref{eybar}) of $e_{\ol{Y}}$ the right hand side equals
\[
\begin{tangle}
\object{Z}\Step\object{Y}\Step\object{\ol{Y}}\\
\xx\mobj{e_Y(Z)}\Step\id\\
\id\Step\d\step\id\\
\hh\id\step\hcoev\step\id\step\id\\
\id\step\id\step\hx\step\id\mobj{e_Y(Z)^{-1}}\\
\hh\hev\step\id\step\hev\\
\Step\object{Z}
\end{tangle}
\quad\quad=\quad\quad
\begin{tangle}
\object{Z}\Step\object{Y}\Step\object{\ol{Y}}\\
\xx\mobj{e_Y(Z)}\Step\id\\
\x\step[-.2]\mmobj{e_Y(Z)^{-1}}\step[2.2]\id\\
\id\Step\ev\\
\object{Z}
\end{tangle}
\]
which coincides with the left hand side of (\ref{conjd}) as desired. That $\ol{\ve}(Y)$ is
a morphism in $\2Z_1(\2C)$ is shown analogously. The composition of morphisms being the
same in $\2Z_1(\2C)$ as in $\2C$, $\ve(X), \ol{\ve}(X)$ inherit from $\2C$ all equations
needed to make $\2Z_1(\2C)$ pivotal (spherical). If the pivotal structure of $\2C$ is strict
then the same clearly holds for $\2Z_1(\2C)$.
\qed\\
