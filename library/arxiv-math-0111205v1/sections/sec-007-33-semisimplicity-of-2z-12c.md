---
doc_id: arxiv-math-0111205v1
doc_title: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001"
section_id: sec-007-33-semisimplicity-of-2z-12c
section_title: "Semisimplicity of $\2Z_1(\2C)$"
section_number: 3.3
pages: 13-16
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.69
latex_coverage_ratio: 0.939
doc_brief: "arXiv:math/0111205v1 [math.CT] 19 Nov 2001 — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
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
