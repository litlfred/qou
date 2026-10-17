---
doc_id: arxiv-math-0111205v1
doc_title: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001"
section_id: sec-006-32-elementary-properties-of-the-quantum-double
section_title: "Elementary properties of the quantum double"
section_number: 3.2
pages: 9-29
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.948
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







\subsection{Semisimplicity of $\2Z_1(\2C)$}
\blemma Let $\2C$ be semisimple spherical with simple unit. We assume that there are
only finitely many simple objects and that $\dim\2C\ne 0$. Let
$(X,e_X),(Y,e_Y)\in\2Z_1(\2C)$. Then the map
$E_{X,Y}: \Hom_\2C(X,Y)\rightarrow\Hom_\2C(X,Y)$ defined by 
\[ E_{X,Y}(t)=(\dim\2C)^{-1}\sum_{i\in \Gamma} d_i \ \ 
\begin{tangle}
\step\object{\ol{\ve}(X_i)}\Step\object{Y} \\
\step\hh\hcoev\step\id\\
\step\id\step\hxx\mobj{e_Y(\ol{X_i})}\\
\obj{X_i}\step\id\step\O t\step\id\hstep\obj{\ol{X_i}} \\
\step[-1.2]\mobj{e_X(X_i)}\step[2.2]\hxx\step\id \\
\step\hh\id\step\hev\\
\step\object{X}\step{\ve(X_i)}
\end{tangle}
\]
is a projection onto $\Hom_{\2Z_1(\2C)}((X,e_X),(Y,e_Y))\subset\Hom_\2C(X,Y)$. Here
$\{ X_i, i\in \Gamma\}$ is a basis of simple objects and we abbreviate $d_i=d(X_i)$.
The family of maps $E_{X,Y}$ is a conditional expectation in the sense that
\begin{equation}E_{X,T}(c\circ b\circ a)=c\circ E_{Y,Z}(b)\circ a
\label{cexp}\end{equation} 
if $a\in\Hom_{\2Z_1(\2C)}((X,e_X),(Y,e_Y)), b\in\Hom_\2C(Y,Z),
c\in\Hom_{\2Z_1(\2C)}((Z,e_Z),(T,e_T))$.
\label{condexp1}\elemma
\prf We compute
\[ \dim\2C \cdot \id_Z\otimes E_{X,Y}(t) \mcirc e_X(Z) = \sum_{i\in \Gamma} d_i \ \
\begin{tangle}
\object{Z}\step[3]\object{Y}\\
\hh\id\hstep\obj{\ol{\ve}(X_i)}\step[2.5]\id\\
\hh\id\step\hcoev\step\id\\
\id\step\id\step\hxx\\
\id\obj{X_i}\step\id\step\O t\step\id\obj{\ol{X_i}} \\
\id\step\hxx\step\id \\
\hh\id\step\id\step\hev\obj{\ve(X_i)}\\
\hxx\\
\object{X}\step\object{Z}
\end{tangle}
\quad=\ \ \sum_i\sum_{j,\alpha} d_i \quad \quad
\begin{tangle}
\object{Z}\step[3]\object{Y}\\
\hh\id\step\hcoev\step\id\\
\step[-0.5]\obj{X_j}\hstep\hcu\step\hxx\\
\step[-1]\mobj{{p'}_i^{j,\alpha}}\step\hcd\step\O t\step\id\obj{\ol{X_i}} \\
\id\step\hxx\step\id \\
\hh\id\step\id\step\hev\\
\hxx\\
\object{X}\step\object{Z}
\end{tangle}
\]

\[ = 
\sum_i\sum_{j,\alpha} d_i \ \ 
\begin{tangle}
\object{Z}\step[3]\object{Y}\\
\hh\id\step\hcoev\step\id\\
\step[-0.5]\obj{X_j}\hstep\hcu\step\hxx\\
\dh\step\O t\step\hd \\
\step\hxx\step[1.5]\id\obj{\ol{X_i}} \\
\hdd\hstep\hcd\step\id\\
\hh\hstep\id\step\id\step\hev\\
\hstep\object{X}\step\object{Z}
\end{tangle}
\quad = \ \ 
\sum_{i,j,\alpha} \frac{d_id_j}{d(Z)}\ \ 
\begin{tangle}
\step\hstep\object{Z}\step[1.5]\object{Y}\\
\step[-.2]\mobj{{q'}_{i,j}^\alpha}\step[1.2]\hcd\step\id\\
\obj{X_j}\step\id\step\hxx\\
\step\id\step\O t\step\id\obj{\ol{X_i}} \\
\step\hxx\step\id \\
\hh\step\id\step\hcu\mobj{q_{i,j}^\alpha}\\
\hh\step\id\step[1.5]\id\\
\step\object{X}\step[1.5]\object{Z}
\end{tangle}
\quad=\quad
\sum_j\sum_{i,\alpha} d_j \ \ 
\begin{tangle}
\step[2.5]\object{Z}\step\object{Y}\\
\hh\hstep\hcoev\step\id\step\id\\
\hstep\id\step\hcu\hstep\ddh\\
\hstep\id\step[1.5]\hxx\\
\obj{X_j}\dh\step\O t\step\hd\obj{\ol{X_i}} \\
\step\hxx\step\hcd\mobj{{r'}_j^{i\alpha}}\\
\hh\step\id\step\hev\step\id\\
\step\object{X}\step[3]\object{Z}
\end{tangle}
\]

\[ =
\sum_j\sum_{i,\alpha} d_j \ 
\begin{tangle}
\step[3]\object{Z}\step\object{Y}\\
\step[3]\hxx\\
\hh\step\hcoev\step\id\step\id\\
\step\id\step\hxx\step\id\\
\obj{X_j}\step\id\step\O t\step\hcu\obj{\ol{X_i}}\\
\step\hxx\step\hcd\\
\hh\step\id\step\hev\step\id\\
\step\object{X}\step[3]\object{Z}
\end{tangle}
\quad = \quad
\sum_i d_j\ 
\begin{tangle}
\step[3]\object{Z}\step\object{Y}\\
\step[3]\hxx\\
\hh\step\hcoev\step\id\step\id\\
\step\id\step\hxx\step\id\\
\obj{X_j}\step\id\step\O t\step\id\obj{\ol{X_j}}\step\id \\
\step\hxx\step\id\step\id \\
\hh\step\id\step\hev\step\id\\
\step\object{X}\step[3]\object{Z}
\end{tangle}
\quad = \dim\2C \cdot e_Y(Z)\mcirc E_{X,Y}(t)\otimes\id_{Z} 
\]
Here $\{ p_i^{j,\alpha}, \alpha=1,\ldots,N_{Z,X_i}^{X_j}\}$ is, for every $j\in \Gamma$, a
basis in $\Hom_\2C(X_j,ZX_i)$ with dual basis $\{{p'}_i^{j,\alpha}\}$ such that 
${p'}_i^{j,\alpha}\circ p_i^{k,\beta}=\delta_{j,k}\delta_{\alpha\beta}\,\id_{X_j}$ and
$\id_{ZX_i}=\sum_{j,\alpha} p^{j,\alpha}_i\circ {p'}^{j,\alpha}_i$.
We used the fact that $e_X(\cdot),e_Y(\cdot)$ are half-braidings, i.e.\ natural w.r.t.\
the second argument. Furthermore, the basis $\{ q_{i,j}^\alpha \}$ in
$\Hom_\2C(Z,X_jX_{\ol{\imath}})$ and its dual basis are normalized such that
$tr_Z({q'}_{i,j}^\beta\circ q_{i,j}^\alpha)=d(Z)\delta_{\alpha\beta}$. We used that a
basis together with its dual can be replaced  by another one provided the normalizations
are the same.

Since the above computation holds for all $Z\in\2C$ we conclude that $E_{X,Y}(t)$ is
in $\Hom_{\2Z_1(\2C)}((X,e_X),(Y,e_Y))$. The property (\ref{cexp}) for morphisms $a, c$ in
$\2Z_1(\2C)$ is obvious since by (\ref{dmor}) $a,c$ can be pulled through the half
braidings, changing the subscript of the conditional expectation $E$ appropriately. In
order to show that $E_{X,Y}$ is idempotent it thus suffices to show
$E_{X,X}(\id_X)=\id_X$, which follows from the definition of $\dim\2C$. 
\qed

\brem 1. Since the conditional expectations depend also on the half braidings we should
in principle denote them $E_{(X,e_X),(Y,e_Y)}$. We stick to $E_{X,Y}$ in order to keep the 
formulae simple.

2. The r\^{o}le of the assumption on the dimension is obvious: If $\dim\2C=0$ then
the map $E_{X,X}$ with the factor $(\dim\2C)^{-1}$ removed is identically zero on
$\End_{\2Z_1(\2C)}(X)$, thus we cannot use it to obtain a conditional expectation.

3. The proof uses a special instance of the `handle sliding' which is formalized in
\cite{brug3}. 
\erem

\blemma \label{condexp2}
For every $X\in\2C$ we have $tr_X\circ E_{X,X}=tr_X$, where $tr_X$ is the trace on 
$\End_\2C(X)$ provided by the spherical structure. 
\elemma
\prf Let $t\in\Hom_\2C(X,X)$. Using the fact that the spherical structure of $\2Z_1(\2C)$
is induced from $\2C$ we compute
\[ \dim\2C\,tr\circ E_{X,X} (t)=\sum_i d_i \quad
\begin{tangle}
\step[1.5]\object{\ol{\ve}(\ol{X})}\\
\Coev\Step \\
\hh\id\step\hcoev\step\id\\
\id\step\id\step\hxx\\
\id\obj{X_i}\step\id\step\O t\step\id\obj{\ol{X_i}} \\
\id\step\hxx\step\id \\
\hh\mobj{\ol{X}}\id\step\mobj{X}\id\step\hev\mobj{\ve(X_i)}\\
\hh\hev\obj{\ve(\ol{X})}
\end{tangle}
\quad = \sum_i d_i \quad
\begin{tangle}
\Coev \\
\hh\id\step\hcoev\step\id\\
\id\step\id\step\hxx\\
\id\obj{X_i}\step\id\step\O t\step\id\obj{\ol{X_i}} \\
\id\step\id\step\hx\\
\hh\id\step\hev\step\id\obj{X}\\
\Ev\Step\mobj{\ve(\ol{X})}
\end{tangle}
\ \ = \sum_i d_i \sum_{j,\alpha}\quad
\begin{tangle}
\coev\\
\id\step[1.5]\hcd \\
\id\step[1.5]\hxx\\
\id\step[1.5]\O t\step\id\hstep\obj{\ol{X_i}} \\
\id\step[1.5]\hx\obj{X}\\
\hh\id\step[1.5]\hcu\mobj{t^\alpha} \\
\hh\id\obj{\ol{X_j}}\Step\id\obj{X_j}\\
\ev\step[-1]\obj{\ve(\ol{X_j})}
\end{tangle}
\]
\[ \ \ = \ \sum_i d_i \sum_{j,\alpha} \quad
\begin{tangle}
\coev\\
\hh\id\step[1.5]\hcd \\
\obj{X_i}\id\step[1.5]\O t\step\id\step[.3]\obj{\ol{X_i}} \\
\hh\id\step[1.5]\hcu \\
\ev
\end{tangle}
\quad\quad =\ \sum_i d_i \quad\quad
\begin{tangle}
\Coev \\
\hh\id\step\hcoev\step\id\\
\step[-1]\obj{X_i}\step\id\step[.3]\obj{\ol{X}}\step[.7]\id\step\O t\step\id\step[.3]\obj{\ol{X_i}} \\
\hh\id\step\hev\step\id\\
\Ev\Step\mobj{\ve(X_i)}
\end{tangle}
\ \quad = \ \dim\2C \,tr(t).
\]
In the first step we have used Proposition \ref{hb-conj}, the second is based on standard
properties of categories with duals. In the next step we use that, given a basis 
$\{ t^\alpha \}$ in $\Hom_\2C(X_j,\ol{X_i}X)$ with dual basis $\{ \hat{t}^\alpha \}$,  
$\{ e_X(\ol{X_i}) \circ t^\alpha \}$ is a basis in $\Hom_\2C(X_j,X\ol{X_i})$ 
with dual basis $\{ \hat{t}^\alpha\circ e_X(\ol{X_i})^{-1} \}$. Replacing one basis by 
the other leaves the expression invariant. \qed\\

A trace on a finite dimensional $\7F$-algebra $A$ is a $\7F$-linear map $A\rarr\7F$ such
that $tr(ab)=tr(ba)$. It is non-degenerate if for every $a\ne 0$ there is $b$ such that
$tr(ab)\ne 0$. 

\blemma \label{semi}
Let $A$ be a finite dimensional $\7F$-algebra and $tr: A\rarr \7F$ a non-degenerate
trace. If $tr$ is vanishes on nilpotent elements then $A$ is semisimple. Conversely, every
trace (not necessarily non-degenerate) on a semisimple algebra vanishes on nilpotent
elements.
\elemma 
\prf Well known, but see, e.g., \cite{mue09}. \qed

\blemma \label{semisim1}
Let $A$ be a finite dimensional semisimple algebra over $\7F$ with a non-de\-ge\-ne\-rate
trace $tr: A\rightarrow \7F$. Let $B$ be a subalgebra containing the unit of $A$ and
assume there is a conditional expectation $E: A\rightarrow B$ (i.e.\ a linear map such
that $E(bab')=bE(a)b'$ for $a\in A, b,b'\in B$) such that $tr\circ E=tr$. Then $B$ is
semisimple. 
\elemma
\prf Let $0\ne x\in B$. By non-degeneracy of $tr$ there is $y\in A$ such that $tr(xy)\ne 0$. 
Now, using the properties of $E$ we compute $0\ne tr(xy)=tr\circ E(xy)=tr(xE(y))$. Since
$E(y)\in B$ we conclude that the restriction $tr_B\equiv tr\restr B$ is non-degenerate,
too. By Lemma \ref{semi} $tr$ vanishes on nilpotent elements, thus the same trivially
holds for $tr_B$. Now the other half of Lemma \ref{semi} applies and $B$ is semisimple.
\qed 

\brem Algebra extensions $A\supset B$ admitting a conditional expectation $E: A\rarr B$
(satisfying certain conditions) are well known as Frobenius extensions, cf., e.g.,
\cite{kad} and are called Markov extensions if there is an $E$-invariant trace on $A$.
\erem

Now we can put everything together:
\btheor \label{tsemisim}
Let $\7F$ be algebraically closed and $\2C$ a $\7F$-linear, spherical and
semisimple tensor category. We assume that there are only finitely many simple objects and
that $\dim\2C\ne 0$. Then the quantum double $\2Z_1(\2C)$ is spherical and semisimple. 
\etheor 
\prf Recall that by our definition of semisimplicity, $\2C$ has direct sums, subobjects
and a simple unit. By our earlier results also $\2Z_1(\2C)$ has these properties and is
spherical. It therefore only remains to show that the endomorphism algebra of every object
of $\2Z_1(\2C)$ is a multi matrix algebra.

Let $(X,e_X)\in\2Z_1(\2C)$. Then $\End_\2C(X)$ is a finite dimensional multi matrix
algebra by semisimplicity of $\2C$. The trace on $\End_\2C(X)$ provided by the duality
structure is non-degenerate, cf.\ e.g.\ \cite[Lemma 3.1]{gk}, and Lemmas \ref{condexp1},
\ref{condexp2} provide us with a trace preserving conditional expectation 
$E_X: \End_\2C(X)\rightarrow \End_{\2Z_1(\2C)}((X,e_X))$. Thus $\End_{\2Z_1(\2C)}((X,e_X))$ is
semisimple by Lemma \ref{semisim1} and therefore a multi matrix algebra since $\7F$ is
assumed algebraically closed. 
\qed

\brem 1. Even if $(X,e_X)$ is simple as an object of $\2Z_1(\2C)$ there is no reason why $X$ 
should be simple in $\2C$. Usually it is not. Since we do not know a priori which
non-simple objects of $\2C$ appear in the simple objects of $\2Z_1(\2C)$ we cannot dispense
with the assumption that $\2C$ has all finite direct sums as done, e.g., in \cite{t}.

2. Note that we do net yet know that $\2Z_1(\2C)$ has finitely many isomorphism classes of
simple objects. To show this will be our next aim.
\erem







\section{Weak Morita equivalence of $\2Z_1(\2C)$ and $\2C\boxtimes\2C^\op$}\label{sec-morita}

\subsection{A Frobenius Algebra in $\2C\boxtimes\2C^\op$}\label{ss-mcata}
Throughout this section $\2C$ will be a strict spherical tensor category with simple unit
over an algebraically closed field $\7F$. We require that $\2C$ is semisimple with
finite set $\Gamma$ of isomorphism classes of simple objects and $\dim\2C\ne 0$. The set
$\Gamma$ has a distinguished element $0$ representing the tensor unit and an involution
$i\mapsto\ol{\imath}$ which associates with every class the class of dual objects. We
choose representers $\{X_i,\ i\in \Gamma\}$ of these classes, which are arbitrary except
that we require $X_0=\11$. (We emphasize that we do not require $\ol{X_i}=X_{\ol{\imath}}$.
This can be achieved by a suitable strictification of the category if and only if all
self-dual objects are orthogonal \cite{bw1}. (The terms real vs.\ pseudo-real do not seem
appropriate if $\7F\ne\7C$.)) We choose once and for all square roots of the $d_i=d(X_i)$,
as well as $\lambda=\sqrt{\dim\2C}$  and $(\dim\2C)^{1/4}=\sqrt{\lambda}$. 
Let $N_{ij}^k$ be the dimension of the space $\Hom(X_k,X_iX_j)$, let 
$\{t_{ij}^{k\alpha},\ \alpha=1,\ldots,N_{ij}^k\}$ be a basis in $\Hom(X_k,X_iX_j)$ and
let $\{ {t'}_{ij}^{k\alpha} \}$ be the basis in $\Hom(X_iX_j,X_k)$ which is dual in the
sense of ${t'}_{ij}^{k\alpha}\circ t_{ij}^{k,\beta}=\delta_{\alpha\beta}$. Note that
this normalization of the dual basis differs from the one provided by the trace by a
factor of $d_k$. The present choice is more convenient since otherwise the dimensions
would appear in the equation 
\[ \sum_{k,\alpha} t_{ij}^{k\alpha}\circ {t'}_{ij}^{k\alpha}=\id_{X_iX_j}. \]
The choice of the of the square roots, the $X_i$ and of the bases $\{t_{ij}^{k\alpha}\}$
is immaterial but will be kept fixed throughout the rest of the paper, and the symbols  
$\Gamma, X_i, N_{ij}^k, t_{ij}^{k\alpha}$ will keep the above meanings. 

With these preparations we can embark on the 2-categorical approach to the quantum 
double. We define
\bea \2A & = & \2C\boxtimes\2C^\op, \\
 \hat{X}_i &=& X_i\boxtimes X_i^\op\in\obj\,\2A. \eea
By \cite[Lemma 2.9]{mue09}, $\2C^\op, \2C\otimes_\7F\2C^\op$ and $\2A$ are strict spherical
in a canonical way. Every $\hat{X}_i,\ i\in \Gamma$ is simple and if it is self-dual (i.e.\
if $i=\ol{\imath}$) then it is orthogonal irrespective of whether $X_i$ is orthogonal or
symplectic. 

The following is a very slight generalization of \cite[Proposition 4.10]{lre}.
\bprop Let $\7F$ be quadratically closed and let $\2C$ be $\7F$-linear semisimple
spherical with $\dim\2C\ne 0$. There is a normalized canonical Frobenius algebra
$\5Q=(Q,v,v',w,w')$ in $\2A=\2C\boxtimes\2C^\op$ (with $\lambda_1=\lambda_2=\lambda$) 
such that  
\begin{equation}Q\cong\bigoplus_{i\in \Gamma} \, \hat{X}_i. \label{gamma}\end{equation}
\eprop
\prf Clearly, $d(Q)=\dim\2C$. By definition of $Q$ there are morphisms 
\[ v_i\in\Hom(\hat{X}_i,Q),\quad v'_i\in\Hom(Q,\hat{X}_i),\ \ i\in \Gamma, \]
such that
\begin{equation}v'_i \circ v_j=\delta_{ij}\id_{\hat{X}_i},\quad \sum_i v_i\circ v'_i=\id_Q. 
\label{cuntz}\end{equation}
Defining $v=\lambda^{1/2} v_0, v'=\lambda^{1/2} v'_0$, (\ref{W5}) is trivial. With 
${t'}_{ij}^{k\alpha} \in\Hom_\2C(X_iX_j,X_k)\equiv\Hom_{\2C^\op}(X^\op_k,X^\op_iX^\op_j)$ 
the morphisms
\[ \hat{t}_{ij}^k= \sum_{\alpha=1}^{N_{ij}^k} t_{ij}^{k\alpha} \boxtimes 
   {t'}_{ij}^{k\alpha} \ \in \ \Hom_\2A(\hat{X}_k,\hat{X}_i\hat{X}_j) \]
are independent of the choices of the bases $\{t_{ij}^{k\alpha}\}$. Then
\begin{equation}w= \lambda^{-1/2} \ \sum_{i,j,k\in \Gamma} \sqrt{\frac{d_id_j}{d_k}} \,
   v_i \otimes v_j \mcirc \hat{t}_{ij}^k \mcirc v'_k \label{defW}\end{equation}
is in $\Hom_\2A(Q,Q^2)$, and $w'\in\Hom_\2A(Q^2,Q)$ is defined dually.
Eqs. (\ref{W2}, \ref{W2'}) of Definition \ref{d-Frob} are almost obvious. (Use
$N_{0i}^j=\delta_{ij}$). The proof that $w, w'$ satisfy (\ref{W1}, \ref{W1'}) and
(\ref{W3}) is omitted since it is entirely analogous to the one in \cite[p. 591]{lre}.
Finally, $w'\circ w=\lambda\id_Q$ is proven by a simple computation observing 
${\hat{t'}}^k_{ij} \circ \hat{t}_{ij}^k=N_{ij}^k\,\id_{\hat{X}_k}$ and using
\begin{equation}\label{ddN}
 \sum_{i,j} d_id_j N_{ij}^k=\sum_{i,j} d_id_j N_{j\ol{k}}^{\ol{\imath}}=\sum_j d_k d_j^2=
  d_k\dim\2C=d_k\lambda^2. \end{equation}
Thus $(Q,v,v',w,w')$ is a canonical Frobenius algebra in $\2A$. 
\qed

Thus Theorem \ref{Main} applies and yields a spherical bicategory $\2E$. ($\2E$ is strict as a
bicategory except for the existence of non-trivial unit constraints for $\11_\6B$ and
strict pivotal \cite{bw2} except for isomorphisms 
$\gamma_{X,Y}: \ol{Y}\circ\ol{X}\rarr\ol{X\circ Y}$ which are  non-trivial whenever
$\mbox{Ran}(Y)=\mbox{Src}(X)=\6B$.) In
particular, we have a spherical tensor category $\2B=\END_\2E(\6B)$.
In the rest of the paper $\2A, \5Q, \2E$ and $\2B$ will have the above meanings. By 
construction $Q$ contains the identity object of $\2A$ with multiplicity 1, thus $J, \oj $
and $\11_B$ are simple by \cite[Proposition 5.3]{mue09} and $d(J)=d(\oj)=\lambda$.
(The condition (iii) of that proposition can also easily be verified directly.) 

\blemma $\dim\2B=(\dim\2C)^2$. \elemma
\prf Follows from $\dim\2B=\dim\2A$ and $\dim\2A=(\dim\2C)^2$. The former is
\cite[Proposition 5.16]{mue09} and the latter is obvious since the simple objects of
$\2C\boxtimes\2C^\op$ are those of the form $X\boxtimes Y^\op$ with $X, Y$ simple. \qed 

In the sequel we will write $\11$ instead of $\11^\op$ in order to alleviate the
notation.







\subsection{A fully faithful tensor functor $F: \2Z_1(\2C)\rightarrow\2B$} \label{fff}
In this subsection we will construct a functor $F: \2Z_1(\2C)\rightarrow\2B$ and prove
that it is fully faithful and monoidal. This already implies that $\2Z_1(\2C)$ has finitely 
many isomorphism classes of simple objects, which is not at all obvious from
Definition \ref{defdouble}.

\blemma \label{11mor}
Let $X,Y\in\2C$. There is a one-to-one correspondence between morphisms 
$u\in \Hom_\2A((X\boxtimes\11)Q,Q(Y\boxtimes\11))\equiv\Hom_\2E(\oj (X\boxtimes\11)J,\oj (Y\boxtimes\11)J)$
and families $\{ u[i]\in\Hom_\2C(XX_i,X_iY),\ i\in \Gamma\}$. With $Z\in\2C$ and 
$v\in \Hom_\2A((Y\boxtimes\11)Q,Q(Z\boxtimes\11))\equiv\Hom_\2E(\oj (Y\boxtimes\11)J,\oj (Z\boxtimes\11)J)$ we have
\begin{equation}(v\bullet u)[k]= (d_k\,\lambda)^{-1} \sum_{i,j\in \Gamma}
   \sum_{\alpha=1}^{N_{ij}^k} d_i d_j \  
\begin{tangle}
\step[1.5]\hstep\object{X_k}\step[1.5]\object{Z}\\
\hh\mobj{{t'}_{ij}^{k\alpha}}\step[1.5]\hcd\step\id\\
\hh\step[1.5]\id\mobj{X_i}\step\id\mobj{X_j}\step\id\\
\hh\step[1.5]\id\step\frabox{v[j]} \\
\hh\step[1.5]\id\step\id\obj{Y}\step\id\\
\hh\step[1.5]\frabox{u[i]}\step\id \\
\hh\step[1.5]\id\step\id\mobj{X_i}\step\id\mobj{X_j}\\
\hh\step[1.5]\id\step\hcu\obj{t_{ij}^{k\alpha}}\\
\step[1.5]\object{X}\step[1.5]\object{X_k}
\end{tangle}
\label{mul}\end{equation}
\elemma
\prf Let $u\in \Hom_\2A((X\boxtimes\11)Q,Q(Y\boxtimes\11))$. Then
\[ v'_j\otimes\id_{Y\boxtimes\11}\mcirc u\mcirc \id_{X\boxtimes\11} \otimes v_i \]
is in
\[\Hom_\2A((X\boxtimes\11)\hat{X}_i,\hat{X}_j(Y\boxtimes\11)) 
  =\Hom_\2C(X X_i, X_jY)\otimes_\7F \Hom_{\2C^\op}(X^\op_i, X^\op_j), \]
which vanishes if $i\ne j$. Thus 
\[ v'_i\otimes\id_{Y\boxtimes\11} \mcirc u\mcirc \id_{X\boxtimes\11}
  \otimes v_i= u[i]\boxtimes\id_{X^\op_i} \]
defines $u[i]\in\Hom_\2C(X X_i,X_iY)$. Conversely, given
$\{ u[i]\in\Hom_\2C(X X_i,X_iY), i\in \Gamma\}$, 
\begin{equation}u=\sum_i v_i\otimes\id_{Y\boxtimes\11} \mcirc
   u[i]\boxtimes\id_{X^\op_i} \mcirc\id_{X\boxtimes\11} \otimes v'_i 
\label{U-ve}\end{equation}
defines a morphism $u\in\Hom_\2A((X\boxtimes\11)Q,Q(Y\boxtimes\11))$. 

Eq. (\ref{mul}) follows easily from (\ref{U-ve}), the definition 
\cite[Proposition 3.8]{mue09} of the $\bullet$-multiplication in $\2E$ and the formula
(\ref{defW}) for $w, w'$.
\qed

\blemma \label{uulemma}
Let $u\in\End_\2B(J(X\boxtimes\11)\oj)$. Then the associated family $\{ u[i]\}$ satisfies 
the braiding fusion equation 
\be
\begin{tangle}
\object{X_i}\step\object{X_j}\step\object{X}\\
\hh\id\step\id\step\id\\
\hh\id\step\frabox{u[j]}\\
\hh\id\step\id\obj{X}\step\id\\
\hh\frabox{u[i]}\step\id\\
\hh\id\step\id\mobj{X_i}\step\id\mobj{X_j}\\
\hh\id\step\frabox{t}\\
\hh\id\step[1.5]\id\\
\object{X}\step[1.5]\object{X_k}
\end{tangle} \ \ = \ \ \ \
\begin{tangle}
\object{X_i}\step\object{X_j}\step\object{X}\\
\hh\id\step\id\step\id\\
\hh\frabox{t}\step\id\\
\hh\step\id\obj{X_k}\step\id\\
\hh\step\frabox{u[k]}\\
\hh\step\id\step\id\\
\hh\step\object{X}\step\object{X_k}
\end{tangle}
\label{bfe}\end{equation}
for all $i,j,k\in \Gamma$ and all $t\in\Hom_\2C(X_k,X_iX_j)$ iff $u$ satisfies
\be
\begin{tangle}
\object{Q}\step\object{Q}\Step\object{X\boxtimes\11}\\
\hh\id\step\id\step\id\\
\hh\id\step\frabox{u}\\
\hh\id\step\id\step\id\\
\hh\frabox{u}\step\id\\
\hh\id\step\hcu\obj{w}\\
\hh\id\step[1.5]\id\\
\step[-.5]\object{X\boxtimes\11}\Step\object{Q}
\end{tangle} \ \ = \ \ \
\begin{tangle}
\object{Q}\step\object{Q}\step[1.7]\object{X\boxtimes\11}\\
\hh\id\step\id\hstep\id\\
\hh\step[-.3]\obj{w}\step[.3]\hcu\hstep\id\\
\hh\hstep\id\step\id\\
\hh\hstep\frabox{u}\\
\hh\hstep\id\step\id\\
\hh\hstep\id\step\mobj{Q}\\
\hstep\object{X\boxtimes\11}
\end{tangle}
\label{uu2}\end{equation}
\elemma
\prf In view of the definition (\ref{defW}) of $w\in\Hom_\2A(Q,Q^2)$ and of 
(\ref{U-ve}), the left hand side of (\ref{uu2}) is seen to equal
\begin{multline*}
 \lambda^{-1/2} \sum_{i,j,k}\sqrt{\frac{d_id_j}{d_k}} v_i\otimes
  v_j\otimes\id_{X\boxtimes\11} 
   \mcirc \id_{\hat{X}_i}\otimes u[j]\boxtimes\id_{X^\op_j}\mcirc
    u[i]\boxtimes\id_{X^\op_i}\otimes\id_{\hat{X}_j} \\
 \mcirc\id_{X\boxtimes\11}\otimes\hat{t}^k_{ij}\mcirc
  \id_{X\boxtimes\11}\otimes v'_k, 
\end{multline*}
whereas the right hand side equals
\[ \lambda^{-1/2}\sum_{i,j,k}\sqrt{\frac{d_id_j}{d_k}} v_i\otimes
   v_j\otimes\id_{X\boxtimes \11}\mcirc \hat{t}^k_{ij}\otimes\id_{X\boxtimes\11}\mcirc 
   u[k]\boxtimes \id_{X^\op_k}\mcirc\id_{X\boxtimes\11}\otimes
   v'_k. \]
In view of the orthogonality relation satisfied by the $v's$, these two expressions
are equal iff
\begin{multline*} \lefteqn{\id_{\hat{X}_i}\otimes u[j]\boxtimes\id_{X^\op_j}\mcirc
    u[i]\boxtimes\id_{X^\op_i}\otimes\id_{\hat{X}_i}\mcirc
   \id_{X\boxtimes\11}\otimes\hat{t}^k_{ij}} \\
   =\hat{t}^k_{ij}\otimes\id_{X\boxtimes\11}\mcirc u[k]\boxtimes
   \id_{X^\op_k} \quad\quad\forall i,j,k\in \Gamma. 
\end{multline*}
Inserting 
$\hat{t}^k_{ij}=\sum_\alpha t^{k\alpha}_{ij}\boxtimes {t'}^{k\alpha}_{ij}$,
this becomes 
\bea \sum_{\alpha=1}^{N_{ij}^k} \left( \id_{X_i}\otimes u[j]\mcirc
   u[i]\otimes\id_{X_j}\mcirc \id_X\otimes t_{ij}^{k\alpha}\right)
  &\boxtimes& {t'}^{k\alpha}_{ij} \nn\\ = \ \ 
  \sum_{\alpha=1}^{N_{ij}^k} \left( t_{ij}^{k\alpha}\otimes\id_X\mcirc u[k] \right) 
  &\boxtimes& {t'}^{k\alpha}_{ij}. \label{cond1}\eea
Multiplying from the right with 
$\id_{XX_k}\boxtimes {t}^{k\alpha}_{ij}$, we arrive at the condition
(\ref{bfe}). Conversely, $\boxtimes$-tensoring (\ref{bfe}) with 
${t'}^{k\alpha}_{ij}$ and summing over $\alpha$ we obtain (\ref{cond1}). 
\qed


\bprop \label{funcf}
There is a faithful functor $F: \2Z_1(\2C)\rightarrow\2B$.
\eprop
\prf Let $(X,e_X)\in\2Z_1(\2C)$. By Lemma \ref{11mor} the half braiding 
$\{ e_X(Z), Z\in\2C\}$ provides us with an element $p^0_X$ in 
$\End_\2B(\oj (X\boxtimes\11)J)\equiv\Hom_\2A((X\boxtimes\11)Q,Q(X\boxtimes\11))$.
Since $e_X(\cdot)$ satisfies the braiding fusion relation (\ref{bfe}), $p^0_X$ 
satisfies (\ref{uu2}). Now, multiplying (\ref{uu2}) from the left with 
$w'\otimes\id_{X\boxtimes\11}$ and using (\ref{W4}) we obtain 
\begin{equation}w'\otimes\id_{X\boxtimes\11}\mcirc\id_Q\otimes p^0_X\mcirc p^0_X\otimes 
  \id_Q\mcirc\id_{X\boxtimes\11}\otimes w = \lambda p^0_X, \label{idemp}\end{equation}
which is just $p^0_X\bullet p^0_X=\lambda p^0_X$ in $\End_\2E(\oj (X\boxtimes\11)J)$. 
Thus with $p_X=\lambda^{-1}p^0_X$, 
\begin{equation}F((X,e_X)):=(\oj (X\boxtimes\11)J, p_X) \label{deff}\end{equation}
is an object in $\2B$, which defines the functor $F$ on the objects. We will mostly write
$F(X,e_X)$ instead of $F((X,e_X))$. Let $(X,e_X)\in\2Z_1(\2C)$ with the above idempotent 
$p_X\in\Hom_\2A((X\otimes\11)Q,Q(X\otimes\11))\equiv\End_\2E(\oj (X\boxtimes\11)J)$
and similarly $(Y,e_Y),\ p_Y$. Consider now
$s\in\Hom_{\2Z_1(\2C)}((X,e_X),(Y,e_Y))\subset\Hom_\2C(X,Y)$. Then condition (\ref{dmor}) 
implies 
\begin{equation}\id_Q\otimes (s\boxtimes\id_{\11}) \circ p_X =
    p_Y \circ (s\boxtimes\id_{\11})\otimes\id_Q. \label{emor}\end{equation}
The element of $u\in\Hom_\2A((X\boxtimes\11)Q,Q(Y\boxtimes\11))\equiv\Hom_\2E(\oj
(X\boxtimes\11)J,\oj (Y\boxtimes\11)J)$ defined by (\ref{emor}) clearly satisfies
$p_Y\bullet u\bullet p_X=u$ and is therefore a morphism in 
$\Hom_\2E((\oj (X\boxtimes\11)J,p_X),(\oj (Y\boxtimes\11)J,p_Y)$. That the map 
$s\mapsto u$ is faithful follows from the first term in (\ref{emor}) and the fact that the
$e_X(X_i),\ i\in \Gamma$, and thus $p_X$ (as a morphism in $\2A$) are invertible. This
defines $F$ on the morphisms, and $F$ is faithful. The simple argument proving that $F$
respects the composition of morphisms is left to the reader. 
\qed


\bprop The functor $F$ is full. \label{fullf}\eprop
\prf We must show that every morphism in $\Hom_\2B(F(X,e_X),F(Y,e_Y))$, where
$(X,e_X),$ $(Y,e_Y)\in\2Z_1(\2C)$, is of the form $F(s)$ with 
$s\in\Hom_{\2Z_1(\2C)}((X,e_X),(Y,e_Y))$.
Now, the morphisms in $\Hom_\2B((\oj (X\boxtimes\11)J,p_X),(\oj (Y\boxtimes\11)J,p_Y))$
are those elements $s$ in $\Hom_\2B(\oj (X\boxtimes\11)J,\oj (Y\boxtimes\11)J)$ which
satisfy $s=p_Y\bullet s\bullet p_X$. $p_X, p_Y$ being idempotents, every such $s$
obviously is of the form $s=p_Y\bullet t\bullet p_X$ for some
$t\in\Hom_\2B(\oj (X\boxtimes\11)J,\oj (Y\boxtimes\11)J)$. By definition of $\2B$ and
by Lemma \ref{11mor}, $s$ and $t$ are represented by elements $\{s[i]\},\ \{t[i]\}$ of
$\bigoplus_{i\in \Gamma} \Hom_\2C(XX_i,X_iY)$.  Given arbitrary $t$ and setting 
$s=p_Y\bullet t\bullet p_X$ we will show that 
$s[0]\in\Hom_\2C(X,Y)$ is in fact in $\Hom_{\2Z_1(\2C)}((X,e_X),(Y,e_Y))$ and that
\[ s[m]= \id_{X_m}\otimes s[0] \mcirc e_X(X_m) \quad\forall m\in \Gamma, \]
which is equivalent to 
\[ s= \id_Q\otimes (s[0]\boxtimes\id_{\11}) \circ p_X = F(s[0]).
\]
Starting from the explicit statement of $s=p_Y\bullet t\bullet p_X$ we compute:
\[ d_m\lambda^4\cdot s[m]=\sum_{i,j,k,l\in \Gamma}\sum_{\alpha,\beta} d_id_jd_k \ \ 
\begin{tangle}
\hstep\object{X_m}\step[2.5]\object{Y}\\
\hh\step[-1]\mobj{{t'}_{kl}^{m\alpha}}\step\hcd\Step\id\\
\id\step\hdcd\step\id\\
\id\step\id\step\hxx\\
\hh\id\step\frabox{t[i]}\step\id \\
\hh\step[-1]\mobj{X_k}\step\id\step\id\step\id\mobj{X_i}\step\id\mobj{X_j}\\
\hxx\step\hddcu\step[-0.5]\mobj{X_l}\\
\hh\id\step\hcu\obj{t_{kl}^{m\alpha}}\\
\object{X}\step[1.5]\object{X_m}
\end{tangle}
\]
\[ =  \sum_{{i,j,k,l\in \Gamma}\atop{\alpha,\beta}} d_id_jd_k\frac{d_m}{d_k}\frac{d_l}{d_j}
\quad\quad
\begin{tangle}
\object{X_m}\step[2.5]\object{\ol{\ve}(\ol{X_l})}\step[2.5]\object{Y}\\
\id\step\Coev\Step\mobj{X_l}\step\id\\
\hh\id\step\id\step\hcoev\step\id\step\id\\
\id\step\id\step\id\step\hcu\step[-.4]\mobj{s_{\ol{\imath}l}^{j\beta}}\step[.9]\ddh\\
\id\step\id\step\id\mobj{X_i}\step[1.5]\hxx\\
\step[-.7]\mobj{s_{m\ol{l}}^{k\alpha}}\step[.7]\hcu\step\id\hstep\hdd\step\id\\
\hh\hstep\id\step[1.5]\frabox{t[i]}\step[1.5]\id\mobj{X_j} \\
\step[-.3]\mobj{X_k}\step[.3]\dh\step\id\step\id\mobj{X_i}\step\hcd\mobj{{s'}_{\ol{\imath}l}^{j\beta}}\\
\step\hxx\step\hev\step[-1.2]\mobj{\ve(X_i)}\step[2.2]\id\mobj{X_l}\\
\step\id\step\hdcd\mobj{{s'}_{m\ol{l}}^{k\alpha}}\Step\id\\
\step\id\step\id\step\ev\mobj{\ve(\ol{X_l})}\\
\step\object{X}\step\object{X_m}
\end{tangle} 
= \ \sum_{{i,j,k,l\in \Gamma}\atop{\alpha,\beta}} d_id_md_l \quad\quad
\begin{tangle}
\object{X_m}\step[2.5]\object{\ol{\ve}(\ol{X_l})}\step[2.5]\object{Y}\\
\id\step\Coev\step[3]\id\\
\id\step\id\step\hcoev\step\hxx\\
\id\step\id\step\id\step\hxx\step\id\mobj{X_l}\\
\hh\step[-1.2]\mmobj{s_{m\ol{l}}^{k\alpha}}\step[1.2]\hcu\step\id\step\id\step\hcu\mmobj{s_{\ol{\imath}l}^{j\beta}}\\
\hh\step[-0.5]\mobj{X_k}\step\id\step[1.5]\frabox{t[i]}\step[1.5]\id\mobj{X_j} \\
\hh\step[-1.2]\mmobj{{s'}_{m\ol{l}}^{k\alpha}}\step[1.2]\hcd\step\id\step\id\mobj{X_i}\step\hcd\mmobj{{s'}_{\ol{\imath}l}^{j\beta}}\\
\id\step\hxx\step\hev\step\id\mobj{X_l}\\
\hxx\step\Ev\step[1.5]\mobj{\ve(\ol{X_l})}\\
\object{X}\step\object{X_m}
\end{tangle}
\]
\[ = d_m \sum_{i,l\in \Gamma} d_id_l \ 
\begin{tangle}
\object{X_m}\step[2.5]\object{\ol{\ve}(\ol{X_l})}\step[2.5]\object{Y}\\
\id\step\Coev\step[3]\id\\
\id\step\id\step\hcoev\step\hxx\\
\id\step\id\step\id\step\hxx\step\id\\
\hh\id\step\id\step\frabox{t[i]}\step\id\step\id\mobj{X_l} \\
\hh\id\step\id\step\id\step\id\mobj{X_i}\step\id\step\id\\
\id\step\hxx\step\hev\step[-1]\mobj{\ve(X_i)}\Step\id\\
\hxx\step\Ev\step[1.5]\mobj{\ve(\ol{X_l})}\\
\object{X}\step\object{X_m}
\end{tangle}
\quad = \ \ d_m  \ \ 
\begin{tangle}
\object{X_m}\Step\object{Y}\\
\id\Step\id\\
\hh\id\step[1.5]\frabox{E_{X,Y}(u)}\\
\xx\\
\hh\id\Step\id\\
\object{X}\Step\object{X_m}
\end{tangle}
\]
where $u\in\Hom_\2C(X,Y)$ does not depend on $m$. (On the very left, $p_X, p_Y$ and each
of the $\bullet$-operations contribute one factor $\lambda$. Furthermore,
$s_{m\ol{l}}^{k\alpha}, \alpha=1,\ldots,N_{m\ol{l}}^k$ is a basis in 
$\Hom(X_k,X_m\ol{X_l})$ with dual basis $s'$. We do not use $t_{m\ol{l}}^{k\alpha}$ since
we cannot assume $\ol{X_l}=X_{\ol{l}}$ without losing generality.)
For $m=0$ we have $X_m=\11$ and thus
$s[0]=\lambda^{-4}E_{X,Y}(u)$, thus $s[0]\in\Hom_{\2Z_1(\2C)}((X,e_X), (Y,e_Y))$.
Plugging this into the above equation for $m\ne 0$ we obtain
$s[m]=\id_{X_m}\otimes s[0]\mcirc e_X(X_m)$ and therefore $s=F(\lambda s[0])$. 
We conclude that the functor $F$ is full. \qed

\bprop The functor $F$ is strong monoidal. \eprop
\prf First we observe that $F(\11_{\2Z_1(\2C)})=F(\11_\2C,\id_X)=(\oj J,\lambda^{-1}\id_Q)$,
which follows from (\ref{deff}) by putting $X=\11$ and $e_X(X_i)=\id_{X_i}\ \forall i$.
Comparing with \cite[Theorem 3.12]{mue09} we see $F(\11_{\2Z_1(\2C)})=\11_\6B$.

Now we have to show that $F(X,e_X)F(Y,e_Y)$ and $F((X,e_X)(Y,e_Y))$ are naturally
isomorphic. We compute 
\bean F(X,e_X)F(Y,e_Y) &=& (\oj (X\boxtimes\11)J,p_X)(\oj (Y\boxtimes\11)J,p_Y) \\
   &=&    (\oj (X\boxtimes\11)Q(Y\boxtimes\11)J,u_1(X,Y)), \\
   F((X,e_X)(Y,e_Y)) &=& F(XY,e_{XY}) = (\oj (XY\boxtimes\11)J,u_2(X,Y)), \eean
where
\[ u_1(X,Y) = \ \ 
\begin{tangle}
\step[1.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}\\
\hh\obj{Q}\step\id\step[1.5]\obj{Q}\step[1.5]\id\\
\hh\id\step\id\step\hcd\step\id\\
\hh\frabox{p_X}\step\id\step\frabox{p_Y}\\
\hh\id\step\hcu\step\id\step\id\\
\hh\id\step[1.5]\obj{Q}\step[1.5]\id\step\obj{Q}\\
\step[.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}
\end{tangle} \quad\quad\quad\quad\quad
u_2(X,Y) = \lambda \quad
\begin{tangle} 
\step[1.2]\object{X\boxtimes\11}\\
\hh\obj{Q}\step\id\Step\object{Y\boxtimes\11}\\
\hh\id\step\id\step\id\\
\hh\frabox{p_X}\step\id\\
\hh\id\step\id\mobj{Q}\step\id\\
\hh\id\step\frabox{p_Y}\\
\hh\id\step\id\step\id\\
\hh\step[-0.3]\object{X\boxtimes\11}\step[1.3]\id\step\obj{Q}\\
\step[1.2]\object{Y\boxtimes\11}
\end{tangle}
\]
Obviously, $F$ is not strict. But with 
$s(X,Y)\in\Hom_\2E((X\boxtimes\11)(Y\boxtimes\11), (X\boxtimes\11)Q(Y\boxtimes\11))$ and
$t(X,Y)\in\Hom_\2E((X\boxtimes\11)Q(Y\boxtimes\11),(X\boxtimes\11)(Y\boxtimes\11))$
defined by 
\[ s(X,Y)= \quad
\begin{tangle}
\step[1.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}\\
\hh\obj{Q}\step\id\step[1.5]\obj{Q}\step[1.5]\id\\
\hh\id\step\id\step\hcd\step\id\\
\hh\frabox{p_X}\step\id\step\frabox{p_Y}\\
\hh\id\step\hcu\step\id\step\id\\
\id\step[1.5]\counit\step[1.5]\id\step\id\\
\hh\id\step[3]\id\step\mobj{Q}\\
\step[.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}
\end{tangle} \quad\quad\quad\quad\quad
 t(X,Y)= \lambda\quad
\begin{tangle}
\step[1.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}\\
\obj{Q}\step\id\step[1.5]\unit\step[1.5]\id\\
\hh\id\step\id\step\hcd\step\id\\
\hh\frabox{p_X}\step\id\step\frabox{p_Y}\\
\hh\id\step\hcu\step\id\step\id\\
\hh\id\step[1.5]\obj{Q}\step[1.5]\id\step\obj{Q}\\
\step[.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}
\end{tangle}
\]
we compute
\[ t(X,Y)\bullet s(X,Y)= \lambda\quad
\begin{tangle}
\hstep\object{Q}\step[1.7]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}\\
\hcd\step\id\step[1.5]\unit\step[1.5]\id\\
\hh\id\step\id\step\id\step\hcd\step\id\\
\hh\id\step\frabox{p_X}\step\id\step\frabox{p_Y}\\
\hh\id\step\id\step\hcu\step\id\step\id\\
\hh\id\step\id\step\hcd\step\id\step\id\\
\hh\frabox{p_X}\step\id\step\frabox{p_Y}\step\id\\
\hh\id\step\hcu\step\id\step\id\step\id\\
\id\step[1.5]\counit\step[1.5]\id\step\hcu\\
\step[.2]\object{X\boxtimes\11}\step[2.7]\object{Y\boxtimes\11}\step[1.5]\object{Q}
\end{tangle} \ \ = \lambda\quad
\begin{tangle}
\hstep\object{Q}\step[1.7]\object{X\boxtimes\11}\step[5]\object{Y\boxtimes\11}\\
\hstep\id\step[1.5]\id\step[1.5]\coev\step[1.5]\id\\
\hh\hcd\step\id\step[1.5]\id\step[1.5]\hcd\step\id\\
\hh\id\step\frabox{p_X}\step[1.5]\id\step[1.5]\id\step\frabox{p_Y}\\
\hh\id\step\id\step\id\step[1.5]\id\step[1.5]\id\step\id\step\id\\
\hh\frabox{p_X}\step\id\step[1.5]\id\step[1.5]\frabox{p_Y}\step\id\\
\hh\id\step\hcu\step[1.5]\id\step[1.5]\id\step\hcu\\
\id\step[1.5]\ev\step[1.5]\id\step[1.5]\id\\
\step[.2]\object{X\boxtimes\11}\step[5]\object{Y\boxtimes\11}\step[1.5]\object{Q}
\end{tangle}
\]
Here the second equality follows (verify!) by repeated use of the equations
(\ref{W1}-\ref{W3}). Using $p_X\bullet p_X=p_X, p_Y\bullet p_Y=p_Y$ and the duality
equation for $Q$ we obtain $t(X,Y)\bullet s(X,Y)=u_2(X,Y)$. Now,
\[ s(X,Y)\bullet t(X,Y)= \lambda\quad
\begin{tangle}
\step\step[1.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}\\
\hh\hstep\obj{Q}\step[1.5]\id\step[1.5]\obj{Q}\step[1.5]\id\\
\hh\hcd\step\id\step\hcd\step\id\\
\hh\id\step\frabox{p_X}\step\id\step\frabox{p_Y}\\
\hh\id\step\id\step\hcu\step\id\step\id\\
\id\step\id\step[1.5]\counit\step[1.5]\id\step\id\\
\id\step\id\step[1.5]\unit\step[1.5]\id\step\id\\
\hh\id\step\id\step\hcd\step\id\step\id\\
\hh\frabox{p_X}\step\id\step\frabox{p_Y}\step\id\\
\hh\id\step\hcu\step\id\step\hcu\\
\hh\id\step[1.5]\obj{Q}\step[1.5]\id\step[1.5]\obj{Q}\\
\step[.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}
\end{tangle} \ \ = \lambda^{-1}\quad
\begin{tangle}
\step[1.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}\\
\hh\obj{Q}\step\id\Step\obj{Q}\step\id\\
\hh\id\step\id\Step\id\step\id \\
\hh\frabox{p_X}\Step\id\step\id\\
\hh\id\hstep\hcd\step\hcd\hstep\id\\
\hh\id\hstep\id\step\hev\step\id\hstep\id\\
\hh\id\hstep\id\step\hcoev\step\id\hstep\id\\
\hh\id\hstep\id\step\id\step\hcu\hstep\id\\
\hh\id\hstep\id\step\id\step[1.5]\frabox{p_Y}\\
\hh\id\hstep\hcu\step[1.5]\id\step\id\\
\hh\id\step\mobj{Q}\Step\id\step\mobj{Q}\\
\step[.2]\object{X\boxtimes\11}\step[3]\object{Y\boxtimes\11}
\end{tangle}
\]
Here we used that $p_X, p_Y$ come from half-braidings, implying that we have (\ref{uu2})
and its dual version by Lemma \ref{uulemma}. (Take into account two factors of $\lambda$
which come from the normalization of $p_{X/Y}$.) It is easy to see that the last
expression equals $u_1(X,Y)$. 

It remains to verify that the functor $F$ is coherent in the sense of
\cite[XI.2]{cwm}. The computations present no difficulties and are simplified by the fact
that the categories $\2Z_1(\2C)$ and $\2B$ are strict except for the unit in
$\2B=\End_\2E(\6B)$. We refrain from spelling out the details. \qed 







\subsection{$F$ is essentially surjective}\label{esssurj}
In order to conclude that $F$ establishes an equivalence 
$\2B\stackrel{\otimes}{\cong}\2Z_1(\2C)$ of tensor categories it remains to prove that $F$
is essentially surjective, viz. that for every object $Y$ of $\2B$ there is
$(X,e_X)\in\2Z_1(\2C)$ such that $F(X,e_X)\cong Y$. We begin with a result due to Izumi
\cite{iz2}. 

\blemma Let $Y\in\2C$ be simple. Then the 1-morphisms 
$(Y\boxtimes\11)J,\, (\11\boxtimes Y^\op)J: \ \6B\rarr\6A$ and 
$\oj(Y\boxtimes\11),\, \oj(\11\boxtimes Y^\op): \6A\rarr\6B$ are
simple. Furthermore, 
\bean 
  (Y\boxtimes\11)J &\cong & (\11\boxtimes\ol{Y}^\op)J, \\
  \oj(Y\boxtimes\11) &\cong & \oj(\11\boxtimes\ol{Y}^\op). 
\eean
\label{iz1}\elemma
\prf Let $Y,Z\in\2C$. By duality be have the isomorphism
\[ \Hom_\2E((Y\boxtimes\11)J, (Z\boxtimes\11)J)\cong
  \Hom_\2E((Y\boxtimes\11)J\oj, Z\boxtimes\11)=
  \Hom_\2A((Y\boxtimes\11)Q, Z\boxtimes\11) \]
of vector spaces. In view of $Q\cong\bigoplus_i X_i\boxtimes X^\op_i$ this
implies 
\[ \Hom_\2E((Y\boxtimes\11)J, (Z\boxtimes\11)J)\cong \Hom_\2C(Y,Z). \]
In particular, if $Y\in\2C$ is simple then 
$(Y\boxtimes\11)J\in\Hom_\2E(\6B,\6A)$ is simple, and so is
$(\11\boxtimes Y^\op)J$ by a similar argument. Furthermore,
\[ \Hom_\2E((Y\boxtimes\11)J, (\11\boxtimes\ol{Y}^\op)J)
  \cong \Hom_\2E(Y\boxtimes Y^\op, J\oj) = \Hom_\2A(Y\boxtimes Y^\op, Q). \]
Now, $Y\boxtimes Y^\op$ is simple and contained in $Q$ with
multiplicity one, thus these spaces are one dimensional and
\[ (Y\boxtimes\11)J \cong (\11\boxtimes\ol{Y}^\op)J. \]
Similar arguments apply to the $\6A-\6B$-morphisms. \qed

\bcoro \label{cor}
Let $X, Y\in\2C$. Then there is $Z\in\2C$ such that
\[ \oj(X\boxtimes Y^\op)J\cong \oj(Z\boxtimes\11)J \]
and such that the isomorphisms 
\bean e &\in& \Hom_\2E(\oj(X\boxtimes Y^\op)J, \oj(Z\boxtimes\11)J)
  \equiv\Hom_\2A((X\boxtimes Y^\op)Q, Q(Z\boxtimes\11)), \\
  f &\in& \Hom_\2E(\oj(Z\boxtimes\11)J, \oj(X\boxtimes Y^\op)J)\equiv
  \Hom_\2A((Z\boxtimes\11)Q, Q(X\boxtimes Y^\op)) \eean
can be chosen such that
\[ e=v\otimes \tilde{e},\quad f=v\otimes \tilde{f} \]
with $\tilde{e}\in\Hom_\2A((X\boxtimes Y^\op)Q, Z\boxtimes\11)$ and 
$\tilde{f}\in\Hom_\2A((Z\boxtimes\11)Q, X\boxtimes Y^\op)$. (Alternatively, one can 
find morphisms of the form $e=\tilde{e}\otimes v', f=\tilde{f}\otimes v'$.)
\ecoro
\prf Using the lemma we compute 
\[ \oj(X\boxtimes Y^\op)J=\oj(X\boxtimes\11)(\11\boxtimes Y^\op)J\cong
  \oj(X\boxtimes\11)(\ol{Y}\boxtimes\11)J=\oj(X\ol{Y}\boxtimes\11)J. \]
We put $Z=X\ol{Y}$ and denote by $\hat{e}$ the isomorphism 
$(\11\boxtimes Y^\op)J\rarr(\ol{Y}\boxtimes\11)J$ provided by the preceding lemma.
Now the claim follows with $\tilde{e}=\id_{X\boxtimes\11}\times\hat{e}$ if we keep in mind
that tensoring $\tilde{e}$ with $\id_{\oj}$ (in $\2E$) amounts to tensoring with $v$ in
$\2A$, as follows from the definition of $\2E$. $\tilde{f}$ is defined
similarly. Alternatively, using the isomorphism 
$\oj(X\boxtimes\11)\cong\oj(\11\boxtimes\ol{X}^\op)$ one obtains a solution with
$e=\tilde{e}\otimes v'$ etc.
\qed

The lemma implies that every object of $\2B$ is isomorphic to one of the form
$(\oj(X\otimes\11)J, p_X)$. This looks quite promising since also $F(X,e_X)$ has this
form. In fact, by Lemma \ref{11mor} and Lemma \ref{halfbr} we obtain a family of morphisms 
$\{ e_X(Y): XY\rarr YX,\ Y\in\2C\}$ natural w.r.t.\ $Y$. Yet, in order to conclude that
this is a half braiding (and therefore $(\oj(X\otimes\11)J, p)=F(X, e_X)$) we need that
$p$ satisfies (\ref{uu2}) and $p[0]=\id_X$. Not every object of $\2B$ satisfies these
conditions as is exemplified, e.g., the object
$\oj(X\boxtimes\11)J=(\oj(X\boxtimes\11)J,p)$ where 
\[ p=\id_{\oj(X\boxtimes\11)J}=v\otimes\id_{X\boxtimes\11}\otimes v'
  \in\Hom_\2A((X\boxtimes\11)Q,Q(X\boxtimes\11)). \]
One easily verifies that $p$ does not satisfy (\ref{uu2}). In view of
$p[i]=\delta_{i0}\id_X$ it is also clear that the corresponding $e_X(Y)$ fails to be
invertible for all $Y$.

The following result on the 2-category $\2E$ is quite general in that it does not rely on 
$\2A=\2C\boxtimes\2C^\op$.
\blemma \label{qq-lemma}
Let $X\in\2A$ and $p=p\bullet p\in\End_\2E(\oj XJ)$. Then there is $Y\in\2A$, 
$q=q\bullet q\in\End_\2E(\oj YJ)$ such that $(\oj YJ, q)\cong(\oj XJ, p)$ and in addition
\begin{equation} \label{qq}
\begin{tangle}
\object{Q}\step\object{Q}\step[.7]\object{Y}\\
\hh\id\step\id\hstep\id\\
\hcu\hstep\id\\
\hh\hstep\frabox{q}\\
\hstep\id\step\id\\
\hstep\object{Y}\step\object{Q}
\end{tangle}
\quad=\lambda\quad
\begin{tangle}
\object{Q}\step\object{Q}\step\object{Y}\\
\hh\id\step\id\step\id\\
\hh\id\step\frabox{q}\\
\hh\id\step\id\step\id\\
\hh\frabox{q}\step\id\\
\id\step\hcu\\
\object{Y}\step[1.5]\object{Q}
\end{tangle} 
\end{equation}
\elemma

\brem The condition (\ref{qq}) implies $q\bullet q=q$ as is seen by multiplication with
$w'\otimes\id_Y$ from the left.  
\erem
\prf Using the (non-strict) unit $\6B-\6B$ morphism $\11_\6B=(\oj J, \lambda^{-1}\id_Q)$
we put $(Y,q)=\11_\6B(X,p)=(QX, \lambda^{-1}\id_Q\times p)$. The isomorphism 
$(\oj YJ, q)\cong(\oj XJ, p)$ was proven in \cite[Theorem 3.12]{mue09}. We claim that $q$
satisfies (\ref{qq}). In terms of $(Y,q)$ (and keeping in mind that $Y=QX$ !) the left
hand side of (\ref{qq}) is given by 
\[ \lambda^{-1}\quad
\begin{tangle}
\hh\hcu\step\id\step[1.5]\id\\
\hh\hstep\id\step\hcd\step\id\\
\hh\hstep\id\step\id\step\frabox{p}\\
\hstep\hcu\step\id\step\id\\
\hstep\hstep\object{Q}\step[1.5]\object{X}\step\object{Q}
\end{tangle}
\]
For the right hand side we compute
\[ \lambda\cdot\lambda^{-2}\quad
\begin{tangle}
\id\hstep\hstep\id\step\hcd\step\id\\
\hh\id\hstep\hstep\id\step\id\step\frabox{p}\\
\hh\id\hstep\hstep\hcu\step\id\step\id\\
\hh\id\step\hcd\step\id\step\id\\
\hh\id\step\id\step\frabox{p}\step\id\\
\hh\hcu\step\id\step\id\step\id\\
\hh\hstep\id\step[1.5]\id\step\hcu\\
\hstep\object{Q}\step[1.5]\object{X}\step[1.5]\object{Q}
\end{tangle}
\quad=\lambda^{-1}\quad
\begin{tangle}
\id\step\cu\step[1.5]\id\\
\id\step\cd\step[1.5]\id\\
\hh\id\step\id\step[1.5]\hcd\step\id\\
\hh\id\step\id\step[1.5]\id\step\frabox{p}\\
\hh\id\step\id\step[1.5]\id\step\id\step\id\\
\hh\id\step\id\step[1.5]\frabox{p}\step\id\\
\hh\hcu\step[1.5]\id\step\id\step\id\\
\hh\hstep\id\Step\id\step\hcu\\
\hstep\object{Q}\Step\object{X}\step[1.5]\object{Q}
\end{tangle}
\quad=\lambda^{-1}\quad
\begin{tangle}
\hh\id\step\cu\step\id\\
\hh\id\step\cd\step\id\\
\hh\id\step\id\step\frabox{p}\\
\hcu\step\id\step\id\\
\hstep\object{Q}\step[1.5]\object{X}\step\object{Q}
\end{tangle}
\]
In the last step we have used $p\bullet p=p$. That the result coincides with the left hand
side follows now from a standard computation using the properties of a Frobenius algebra.
\qed

\bprop Every object of $\2B$ is isomorphic to one of the form
$(\oj(Z\boxtimes\11)J, q)$ where $q\in\End_\2B(\oj(Z\boxtimes\11)J)$ satisfies (\ref{qq})
(with $Y=Z\boxtimes\11$).
\eprop
\prf By the preceding lemma every object $(\oj(X\boxtimes Y^\op)J,p)$ of $\2B$ is
isomorphic to one which satisfies (\ref{qq}), which allows us to assume this property in
the rest of the proof. By Corollary \ref{cor} there is $Z\in\2C$ such that 
$\oj(X\boxtimes Y^\op)J\cong\oj(Z\boxtimes\11)J$. Let
$e: \oj(X\boxtimes Y^\op)J\rarr\oj(Z\boxtimes\11)J$, 
$f: \oj(Z\boxtimes\11)J\rarr\oj(X\boxtimes Y^\op)J$ be a pair of mutually inverse
isomorphisms. Then with $q=e\bullet p\bullet f$ we have
$(\oj(Z\boxtimes\11)J, q)\cong(\oj(X\boxtimes Y^\op)J, p)$. If we can show that 
also $q$ satisfies (\ref{qq}) Lemma \ref{uulemma} applies and the claim follows.
Now by Corollary  \ref{cor} $Z, e, f$ can be chosen such that $e=v\otimes\tilde{e},
f=v\otimes\tilde{f}$, where $\tilde{e}, \tilde{f}$ are mutually inverse 2-morphisms
between $(X\otimes Y)J$ and $(Z\otimes\11)J$. Therefore, 
\[ q=e\bullet p\bullet f =\quad
\begin{tangle}
\step\object{Q}\Step\object{Z}\\
\hh\step\id\Step\id\\
\sw1\id\se1\step\id\\
\hh\id\step\id\step\frabox{e}\\
\hh\id\step\id\step\id\mmobj{X}\step\id\\
\hh\id\step\frabox{p}\step\id\\
\hh\id\step\id\mmobj{X}\step\id\step\id\\
\hh\frabox{f}\step\id\step\id\\
\id\step\nw1\id\ne1\\
\hh\id\Step\id\\
\object{Z}\Step\object{Q}
\end{tangle}
\quad=\quad
\begin{tangle}
\step\object{Q}\Step\object{Z}\\
\hh\step\id\Step\id\\
\hh\step\id\step\frabox{\tilde{e}}\\
\hh\step\id\step\id\mmobj{X}\step\id\\
\hh\step\frabox{p}\step\id\\
\hh\step\id\mmobj{X}\step\id\step\id\\
\hh\frabox{\tilde{f}}\step\id\step\id\\
\id\step\nw1\id\ne1\\
\hh\id\Step\id\\
\object{Z}\Step\object{Q}
\end{tangle}
\]
where the four-fold vertices denote triple (co)products.
That $q$ satisfies (\ref{qq}) is now obvious from the respective property of $p$ and 
$\tilde{f}\bullet\tilde{e}=\id$.
\qed

\bprop \label{prop-ess}
The preceding proposition remains true if one adds the requirement that
$q[0]=\lambda^{-1}\id_Z$ (notation of Lemma \ref{11mor}).
\eprop
\prf Let $Z, q$ be as in the preceding proposition. Multiplying (\ref{qq}) with 
$v'\otimes v'\otimes\id_{Z\boxtimes\11}$ and using 
$v'\otimes\id_{Z\boxtimes\11}\circ q=q[0]\otimes v$ we obtain 
$\lambda q[0]^2=q[0]\in\End_\2C(Z)$. 
Let $f: \tilde{Z}\rarr Z,\, g: Z\rarr\tilde{Z}$ be a splitting of the idempotent
$\lambda q[0]$. Then it is easy to verify that with 
\[ \tilde{q}=\id_Q\otimes (g\boxtimes\id_\11) \mcirc q\mcirc (f\boxtimes\id_\11)\otimes\id_Q \]
we have $(\oj(\tilde{Z}\boxtimes\11)J, \tilde{q})\cong(\oj(Z\boxtimes\11)J, q)$. This
$\tilde{q}$ still verifies (\ref{qq}) and, in addition,
$\tilde{q}[0]=\lambda^{-1}\id_{\tilde{Z}}$.
\qed

Now we are ready to state our first main result.

\btheor The tensor categories $\2B$ and $\2Z_1(\2C)$ are equivalent as spherical categories,
thus we have the weak monoidal Morita equivalence (in the sense of \cite{mue09})
$\2Z_1(\2C)\approx\2C\boxtimes\2C^\op$. In particular,
\[ \dim\2Z_1(\2C)=(\dim\2C)^2. \]
\etheor
\prf We have shown that every simple object in $\2B$ isomorphic to the image under $F$ of
a simple object in $\2Z_1(\2C)$. Since $\2Z_1(\2C)$ and $\2B$ are both semisimple (in
particular closed under direct sums and subobjects) we conclude that $F$ is essentially
surjective. Since $F$ is also fully faithful we have an equivalence of categories by
\cite[Theorem IV.4.1]{cwm}. $F$ being monoidal we have an equivalence of monoidal categories
by \cite[I.4.4]{sr}. (This already implies that $\2B$ and $\2Z_1(\2C)$ have the same
dimension, since by \cite[Proposition 2.4]{mue09} the latter are well-defined independently of
the chosen spherical or $*$-structure and, of course, invariant under monoidal equivalence.)

It remains to show that the spherical structures are compatible. As to the conjugation
maps, we have
\bean \ol{F(X,e_X)} &=& \ol{(\oj(X\boxtimes\11)J,p_{e_X})}=(\oj(\ol{X}\boxtimes\11)J,\ol{p_{e_X}}), \\
   F(\ol{(X,e_X)}) &=& F((\ol{X},e_{\ol{X}}))=(\oj(\ol{X}\boxtimes\11)J, p_{e_{\ol{X}}}). \eean
Putting together Proposition \ref{hb-conj} and Lemma \ref{iii-iv}, $e_{\ol{X}}(X_i)$ is as in
Fig.\ \ref{fig1}, where the pair of unlabeled morphisms is any solution of the duality
equations. 
\begin{figure}
\[ e_{\ol{X}}(X_i)=\quad
\begin{tangle}
\step[1.5]\object{\ol{\ve}(\ol{X})}\step[2.5]\object{X_i}\step\object{\ol{X}}\\
\mcoev\step\id\step\id\\
\hh\id\step\hcoev\step\id\step\id\step\id\\
\hh\id\step\id\step\frabox{e_X(X_{\ol{\imath}})}\step\id\step\id\\
\hh\id\step\id\step\id\step\hev\step\id\\
\id\step\id\step\mev\\
\object{\ol{X}}\step\object{X_i}\step[2.5]\object{\ve(X)}
\end{tangle}
\quad\quad\quad\quad
\ol{p_{e_X}}=\quad
\begin{tangle}
\step[1.5]\object{\ol{\ve}(\ol{X}\boxtimes\11)}\step[2.5]\object{Q}\step[1.5]\object{\ol{X}\boxtimes\11}\\
\mcoev\step\id\step\id\\
\hh\id\step[.8]\mobj{r'}\step[.2]\hcoev\step\id\step\id\step\id\\
\hh\id\step\id\step\frabox{p_{e_X}}\step\id\step\id\\
\hh\id\step\id\step\id\step\hev\mobj{r}\step\id\\
\id\step\id\step\mev\\
\step[-.5]\object{\ol{X}\boxtimes\11}\step[1.5]\object{Q}\step[2.5]\object{\ve(X\boxtimes\11)}
\end{tangle}
\]
\caption{$e_{\ol{X}}(X_i)$ and $\ol{p_{e_X}}$}
\label{fig1}
\end{figure}
In view of the definition of $p_X$ in Proposition \ref{funcf} and of $\ol{p_{e_X}}$ in
\cite[Theorem 5.14]{mue09}, cf.\ Fig.\ \ref{fig1}, it is clear that
$\ol{p_{e_X}}=p_{e_{\ol{X}}}$ and therefore 
\[ \ol{F(X,e_X)}=F(\ol{(X,e_X)}). \]

Now by Proposition \ref{hb-conj}, the spherical structure of $\2Z_1(\2C)$ is inherited from 
$\2C$, concretely $\ve_{\2Z_1(\2C)}(X,e_X)=\ve_\2C(X)$. Considering how the spherical
structures of $\2E_0$ and $\2E$ arise from that of $\2A$ in \cite[Theorem 5.13]{mue09} it
is essentially obvious that $F: \2Z_1(\2C)\rarr\2B$ is an equivalence of spherical
categories irrespective of the fact that the latter is neither strict monoidal nor strict
spherical. We omit the easy details.
\qed

\brem 1. In the case where $\2C$ is the representation category of a finite dimensional
involutive semisimple and cosemisimple Hopf algebra $H$, $\2Z_1(\2C)$ is equivalent
\cite[Theorem XIII.5.1]{ka} to the representation category of the quantum double $D(H)$
and our result is just the fact $\dim D(H)=(\dim H)^2$.

2. It seems likely that a simpler proof of the theorem can be given using the
interpretation of the tensor category $\2B=\END_\2E(\6B)$ as bimodule category
$Q-\mbox{Mod}-Q$, together with the recent work \cite{ostr}.
\erem
