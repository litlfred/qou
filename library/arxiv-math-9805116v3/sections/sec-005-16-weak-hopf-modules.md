---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras I: Integral Theory and C*-structure"
section_id: sec-005-16-weak-hopf-modules
section_title: "Weak Hopf modules"
section_number: 1.6
pages: 16-21
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.995
doc_brief: "Weak Hopf Algebras I: Integral Theory and C*-structure — We give an introduction to the theory of weak Hopf algebras proposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
Let $A$ be a WHA. Recall that a {\em left $A$-module} is a
$K$-linear
space $M$ carrying a left action of the algebra $A$, denoted by
$x\in A,m\in M\mapsto x\cdot m$. A {\em right $A$-module} is a
left module $M$ of the opposite algebra $A^{op}$ with action
denoted by $x\in A,m\in M\mapsto m\cdot x$. Since $A$ is unital,
all modules are assumed to be non-degenerate, i.e. $\1$ acts as
the identity. The left $A$-module $M$ is called {\em faithful} if
$x\cdot m=0$, $\forall m\in M$ implies $x=0$.
 
The $A$-modules know nothing about the coalgebra structure of $A$.
The {\em left $A$-comodules} $M$ in turn are the comodules of the
coalgebra $A$ and carry no information about the algebra structure
of $A$. The left coaction is denoted by $m\mapsto m_{-1}\o m_0\in
A\o M$. One defines the {\em right $A$-comodules} analogously and
denotes the coaction as $m\mapsto m_0\o m_1\in M\o A$.
 
Because of the finite dimensionality of $A$ there is a one-to-one
correspondence between left (right) $A$-coactions on $M$ and right
(left) $\duA$-actions on $M$ given by
\bea
m\cdot\varphi&=\ \bra\varphi,m_{-1}\ket m_0\ ,\qquad
m_{-1}\o m_0\ =&\sum_i b_i\o m\cdot\beta^i\\
\varphi\cdot m&=\ m_0\bra\varphi,m_1\ket\ ,\qquad
m_0\o m_1\ =&\sum_i \beta^i\cdot m\o b_i\ .
\eea
Here $\{b_i\}$ denotes an arbitrary basis of $A$ and $\{\beta^i\}$
is its dual basis: $\bra\beta^i,b_j\ket=\delta_{ij}$.
There are 8 basic examples of $A$ modules with the target space
$M$ being either $A$ itself or its dual $\duA$. These are the
following.
$$\begin{array}{rlcrl}
_AA::& x\cdot y=xy\,,&\qquad&A_A::&y\cdot x=yx\\
^AA::& x\cdot y=yS(x)\,,&\qquad&A^A::&y\cdot x=S(x)y\\
_A\duA::&x\cdot\varphi=x\la\varphi\,,&\qquad&\duA_A::&\varphi\cdot
                                                x=\varphi\ra x\\
^A\duA::&x\cdot\varphi=\varphi\ra S(x)\,,&\qquad&\duA^A::&
                       \varphi\cdot x=S(x)\la\varphi
\end{array}$$
where the Sweedler arrow notation (\ref{Sw arrow}) has been used.
They all are faithful and non-degenerate due to the existence of a
unit and a counit.
To each of the $A$-modules in the above list there is a
corresponding $\duA$-comodule denoted by the same symbol.
This identification is justified also by the fact that $N\subset
M$ is an $A$-submodule if and only if it is an $\duA$-subcomodule.
 
By analogy with our definition of left integrals,
the space of {\em invariants}  of a left
$A$-module $M$ is defined to be the subspace
\beq
\Inv M\ :=\ \{\,m\in M\,|\, x\cdot m=\PL(x)\cdot m,\ \forall x\in
A\,\}
\eeq
By the same methods as in Lemma \ref{lem:embedtrivi},
$\Inv M$ is linearly isomorphic to $\Hom({_A\hat A^R},{_AM})$ via
\beq
\Inv M=\{f(\hat\1)\,|\, f\in\Hom({_A\hat A^R},{_AM})\}.
\eeq
By duality, we define the  {\em coinvariants} of a right
$A$-comodule $M$ as
\beq
\Coinv M\ :=\ \{\,m\in M\,|\, m_0\o m_1=m_0\o\PL(m_1)\}
\eeq
Thus, $m\in\Coinv M \Lra m_0\o m_1\in M\o A^L$ and for a
left $A$-module $M$, the invariants $\Inv M\subset M$  coincide with
$\Coinv M\subset M$ considered as an $\hat A$-comodule.
Similarly, for a right $A$-module (left $A$-comodule) $M$
the invariants (coinvariants) are
\bea
\Inv M &=& \{\,m\in M\,|\,m\cdot x=m\cdot\PR(x),\ \forall x\in A\,\}\\
\Coinv M &=&\{\,m\in M\,|\,m_{-1}\o m_0=\PR(m_{-1})\o m_0\}
.
\eea
Notice that the (co)invariants do not form a
sub(co)module, even not an
$A^{L/R}$-sub\-mod\-ule.
 
\begin{scho} \label{scho3.5}
The invariants of the left (right) regular $A$-module
are precisely the left (right) integrals of $A$:
\[
\Inv _AA\ =\ \IL\ ,\qquad \Inv A_A\ =\ \IR\ .
\]
The invariants of $_A\duA$ and $\duA_A$, on the other hand, yield
the left and right subalgebras, respectively:
\[
\Inv _A\duA\ =\ \duA^L\ ,\qquad \Inv \duA_A\ =\ \duA^R\ .
\]
\end{scho}
Investigating the structure of the mixed modules $_{\duA}\duA^A$
and
$^A\duA_{\duA}$, that incorporate the whole bialgebra structure of
$A$, one arrives to a weak generalization of the notion of Hopf
modules \cite{Abe,Sweedler}.
 
\begin{defi}                      \label{def: WHM}
A {\em right weak Hopf module} (right WHM) over $A$ is a right $A$
module $M$ which is also a right $A$-comodule such that
the compatibility relation
\beq                                   \label{WHM comp}
(m\cdot x)_0\o (m\cdot x)_1\ =\ m_0\cdot x\c\o m_1 x\cc
\eeq
holds for $x\in A,\ m\in M$.
\end{defi}
 
\begin{lem}      \label{lem3.7}
Let $M$ be a right WHM over $A$. Then for all $m\in M$
 
i) $m_0\cdot\PR(m_1) =m$
 
ii) $\Coinv M =\{m\in M\,|\,m_0\o m_1=m\cdot\1\c\o\1\cc\}$
and $\Coinv M$  is a right $A^L$ submodule.
 
iii) $E(m):=m_0\cdot S(m_1)$ provides a projection
$E:M\to\Coinv M$.
\end{lem}
 
{\em Proof:}
i)  Let $M$ be a right WHM over $A$. Since
\beq\label{*}
m_0 \eps(m_1 x)= m_0\cdot \1_{(1)}\eps(m_1\1_{(2)} x)=
m_0\cdot \1_{(1)}\eps(m_1\1_{(2)})\eps(\1_{(3)} x)=
m\cdot \1_{(1)}\eps(\1_{(2)} x)
\eeq
for all $x\in A$, we have $m_0\o {\hat \1}\ra m_1=
m\cdot \1_{(1)} \o {\hat \1}\ra \1_{(2)}$, so that
\beq m_0\cdot \PR(m_1)=
m_0\cdot [({\hat \1}\ra m_1)\la \1]=
m\cdot \1\c [(\du1\ra \1\cc)\la \1]=
m\cdot \1_{(1)}\PR (\1_{(2)})=m.
\eeq
ii) The inclusion $\supset$ follows from (\ref{9}).
Conversely, if $m\in\Coinv M$ then $m_0\o m_1\in M\o A^L$,
implying by (2.3a), (\ref{LR=RL}) and (\ref{*})
$$
m_0\o m_1=m_0\o\eps(m_1\1\c)\1\cc =
m\cdot\1\c\o\eps(\1\cc\1_{(1')})\1_{(2')}=m\cdot\1\c\o\1\cc\,.
$$
Also $\cop({A^L})\subset A\o A^L$ and therefore $\Coinv M$ is a
right $A^L$-submodule.
 
iii) To check that $n:=m_0\cdot S(m_1)$ is a
coinvariant for all $m\in M$ we compute
\beanon
n_0\o n_1&=&(m_0\o m_1)(\cdot (S(m_2)\c\o S(m_2)\cc)=\\
   &=&m_0\cdot S(m_3)\o m_1 S(m_2)=m_0\cdot S(\1\cc m_1)\o
           S(\1\c)=\\
   &=&n\cdot \1\c\o\1\cc .
\eeanon
Since for $n\in \Coinv M$ we have
$n_0\cdot S(n_1)=n\cdot\1\c S(\1\cc)=n$, $E$ is a projection
onto $\Coinv M$.
\qed
 
\begin{exam}\label{ex:rWHM} The right weak Hopf module
$_{\duA}\duA^A$
 
\em As a linear space the module is the dual WHA $\duA$. The right
action and coaction are
\beq
\varphi\cdot x:= S(x)\la \varphi\,,\qquad
\varphi_0\o\varphi_1:=\sum _i\ \beta^i\varphi\o b_i\ .
\eeq
Clearly, the right $A$-coaction is dual to the left
$\hat A$-multiplication and therefore counital and
right-coassociative.
The compatibility condition (\ref{WHM comp}) can be seen as
follows.
\beanon
(\varphi\cdot x)_0\o (\varphi\cdot x)_1
     &=&\sum_i\beta^i(S(x)\la \varphi)\o b_i=\\
     &=&\sum_i\beta^i\left[S(x\c)\la x\cc
               S(x\ccc)\la\varphi\right]\o b_i=\\
     &=&\sum_i\beta^i\left[S(x\c)\la(x\cc\la\du1)\varphi\right]
               \o b_i=\\
     &=&\sum_i\beta^i\left[S(x\cc)x\ccc\la\du1\right]
              \left[S(x\c)\la\varphi\right]\o b_i=\\
     &=&\sum_i\left[S(x\cc)x\ccc\la\beta^i\right]
              \left[S(x\c)\la\varphi\right]\o b_i=\\
&=&\sum_iS(x\c)\la\left[(x\cc\la\beta^i)\varphi\right]
              \o b_i=\\
     &=&\sum_i S(x\c)\la(\beta^i\varphi)\o b_i x\cc=\\
     &=&\varphi_0\cdot x\c\o\varphi_1x\cc\ .
\eeanon
The $A$-coinvariants of this WHM coincide with the $\hat A$-invariants of
the dual left regular $\hat A$-module $_{\hat A}\hat A$ and therefore with
the space of left integrals in $\hat A$ by Scholium \ref{scho3.5},
\beq
\Coinv(_{\duA}\duA^A) = \duIL\,.
\eeq
\end{exam}
 
The Fundamental Theorem of Hopf modules generalizes to the weak
case as follows.
\begin{thm}
Let $A$ be a WHA, $M$ be a right WHM over $A$ and
let $N=\Coinv M$ denote
the set of coinvariants of $M$. Since $N$ is a
right $A^L$ submodule, one can form the $A^L$-module tensor
product $N\amalgo{A^L}A$ and make it into a right WHM by the
definitions
\beabc
(n\o a)\cdot x&:=&n\o ax\\
(n\o a)_0\o (n\o a)_1&:=&(n\o a\c)\o a\cc
\eeabc
where $a,x\in A, n\in N$. Then the map
\beq
\alpha\ \colon\ N\amalgo{A^L}A\ \to\ M\ ,\quad
n\o x\ \mapsto\ n\cdot x
\eeq
is an isomorphism of right WHM-s.
\end{thm}
Recall that an {\em isomorphism of WHM-s} is just a module
isomorphism which is a comodule isomorphism at the same time.
 
\Proof That $\alpha$ is a module map and comodule map is easy to
verify. To construct the inverse define
\bea
\beta&\colon&M\ \to\ N\amalgo{A^L}A\nn
\beta(m)&=&m_0\cdot S(m_1)\o m_2\ \equiv\ E(m_0)\o m_1\ .
\eea
Then $\beta$ is obviously a comodule map.
We show that it is also a module map.
\beanon
\beta(m\cdot x)&=&m_0\cdot x\c S(m_1 x\cc)\o m_2 x\ccc=\\
   &=&m_0\cdot \PL(x\c)S(m_1)\ \o\ m_2 x\cc=\\
   &=&m_0\cdot S(m_1\1\c)\ \o\ m_2\1\cc x=\\
   &=&\beta(m)\cdot x
\eeanon
We are left with showing that on the one hand
\beanon
\beta\circ\alpha(n\o x)&=&\beta(n\cdot x)=\beta(n)\cdot x=
       n\cdot\1\c S(\1\cc)\o \1\ccc x=\\
      &=&n\o\1\c S(\1\cc)\1\ccc x=\\
      &=&n\o x
\eeanon
and on the other hand
\[\alpha\circ\beta(m)\ =\ m_0\cdot S(m_1)m_2\ =\ m\]
where in the last equality Lemma \ref{lem3.7}i) has been used. \qed
 
\bigskip\noindent
Applying this Theorem to the WHM of Example \ref{ex:rWHM}
we obtain the right WHM isomorphism
\beq \label{eq: fundamenta}
_{\duA}\duA^A\ \cong\ \I^L(\duA)\ \amalgo{A^L}\ _{\duA}A_A\ .
\eeq
\begin{coro}                        \label{coro: WHM}
In any WHA $A$ the space of left integrals
$\IL=S(\IR)$ is non-zero and $\duIL$ is the dual of $\IR$
with respect to the restriction of the canonical pairing.
Moreover, choosing a basis $\{\lambda^a\}$ in $\duIL$ and taking
its dual basis $\{r_a\}$ in $\IR$, we have
\bea
\du1&=&\sum_a S(r_a)\la\lambda_a  \label{eq:r-lambda}\\
\1&=&\sum_a r_a\ra\duS(\lambda_a)\  \label{eq:r-lambda-d}
\eea
\end{coro}
\Proof $\duIL\neq 0$ follows from (\ref{eq: fundamenta}).
By inspecting the form of the projection $E: M\to N$
in Example \ref{ex:rWHM} we get a projection
$L\colon A\to\IL$ onto the left integrals,
\beq                                    \label{eq: L}
L(x)\ =\ \sum_i\ \duS^2(\beta^i)\la(b_ix)\ .
\eeq
Therefore the projection to the right integrals is
\beq
R(x)=S\circ L\circ S^{-1}(x)\ =\ \sum_i\ (xb_i)\ra\duS^2(\beta^i)\
.
\eeq
Similar expressions define the projections $\hat L$ and $\hat R$
to the dual integrals. Now it is easy to check that
\beq
\bra \hat L(\varphi), x\ket\ =\ \bra\varphi, R(x)\ket
\eeq
proving the non-degeneracy of the restriction of the canonical
pairing to $\duIL\x\IR$.
 
The dual bases satisfy $\bra\lambda^a,r_b\ket=\delta_{ab}$
therefore
\bea
  \bra \lambda^a\,,\,x S(r_a)\ket &=&
      \bra {\hat L}(\beta^i)\,,\, x S(b_i) \ket =
      \bra S^2(b_j)\la \beta^j \beta^i\,,\, x S(b_i) \ket=
      \bra \beta^k , x S\circ \PR(b_k) \ket=\\
     &=& \bra \1\cc\la \du1 , x S(\1\c) \ket
\eea
where in the last step we used (\ref{pibb}). This proves
(\ref{eq:r-lambda}).
(\ref{eq:r-lambda-d}) is the twisted version in $A^{op}_{cop}$.
\qed
