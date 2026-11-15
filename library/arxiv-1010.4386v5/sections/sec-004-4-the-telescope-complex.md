---
doc_id: arxiv-1010.4386v5
doc_title: "ON THE HOMOLOGY OF COMPLETION AND TORSION"
section_id: sec-004-4-the-telescope-complex
section_title: "The Telescope Complex"
section_number: 4
pages: 16-22
source_pdf: 1010.4386v5.pdf
source_sha256: 168226dbb5a479ed
toc_source: outline
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.952
doc_brief: "ON THE HOMOLOGY OF COMPLETION AND TORSION — Let A be a commutative ring, and a a weakly proregular ideal in A."
---
\label{sec:tel}

The purpose of this section is to prove Theorem \ref{thm:250}. 

Let $A$ be a commutative ring (not necessarily noetherian). For a set $X$ and an
$A$-module $M$ we denote by
$\opn{F}(X, M)$ the set of all functions $f : X \to M$.
This is an $A$-module in the obvious way. We denote by 
$\opn{F}_{\mrm{fin}}(X, M)$ the submodule of $\opn{F}(X, M)$ consisting of
functions with finite support. Note that 
$\opn{F}_{\mrm{fin}}(X, A)$ is a free
$A$-module with basis the delta functions $\delta_x : X \to A$.
(This notation comes from \cite{Ye2}.)

\begin{dfn} \label{dfn:5} 
\begin{enumerate}
\item Given an element $a \in A$, the {\em telescope complex}
$\opn{Tel}(A; a)$ is the complex
\[ \opn{Tel}(A; a) :=
\bigl( \cdots \to 0 \to \opn{F}_{\mrm{fin}}( \N, A) \xar{\d}
\opn{F}_{\mrm{fin}}( \N, A) \to 0 \to \cdots \bigr) \]
concentrated in degrees $0$ and $1$. The differential $\d$ is
\[ \d(\delta_i) := 
\begin{cases}
\delta_0  & \tup{ if } i = 0 , \\
\delta_{i- 1} - a \delta_{i} & \tup{ if } i \geq 1 .
\end{cases} \]

\item Given a sequence $\bsym{a} = (a_1, \ldots, a_n)$ of elements of $A$, we
define
\[ \opn{Tel}(A; \bsym{a}) :=
\opn{Tel}(A; a_1) \otimes_A \cdots \otimes_A \opn{Tel}(A; a_n) . \]
\end{enumerate}
\end{dfn}

Note that $\opn{Tel}(A; \bsym{a})$ is a complex of free $A$-modules,
concentrated in degrees $0, \ldots, n$. 
This complex has an obvious functoriality in $(A; \bsym{a})$. 

Recall that for $j \in \N$ we write 
$[0, j] = \{ 0, \ldots, j \}$.
We view $\mrm{F}([0, j], A)$ as the free submodule of
$\opn{F}_{\mrm{fin}}(\N, A)$ with basis 
$\{ \delta_i \}_{ i  \in [0, j]}$.

Let $j \in \N$.
For any $a \in A$ let $\opn{Tel}_j(A; a)$ be the subcomplex 
\[ \opn{Tel}_j(A; a) :=
\bigl( \cdots \to 0 \to \opn{F}([0, j] , A) \xar{\d}
\opn{F}([0, j] , A) \to 0 \to \cdots \bigr) \]
of $\opn{Tel}(A; a)$.
For the sequence $\bsym{a} = (a_1, \ldots, a_n)$ we define 
\[ \opn{Tel}_j(A; \bsym{a}) :=
\opn{Tel}_j(A; a_1) \otimes_A \cdots \otimes_A \opn{Tel}_j(A; a_n) . \]
This is a subcomplex of $\opn{Tel}(A; \bsym{a})$. It is clear that 
\begin{equation} \label{eqn:214}
\opn{Tel}(A; \bsym{a}) = \bigcup_{j \geq 0} \, \opn{Tel}_j(A; \bsym{a}) . 
\end{equation}

Recall the dual Koszul complex 
$\opn{K}^{\vee}_{}(A; \bsym{a})$ from formula (\ref{eqn:5.2}). 
For any $j \geq 0$ we define a homomorphism of complexes
\begin{equation} \label{eqn:204}
w_{a, j} : \opn{Tel}_j(A; a) \to \opn{K}^{\vee}_{}(A; a^j) 
\end{equation}
as follows, using the presentation (\ref{eqn:203}) of 
$\opn{K}^{\vee}_{}(A; a^j)$. 
In degree $0$ the homomorphism 
\[ w_{a, j}^0 : \opn{Tel}_j(A; a)^0 = \opn{F}([0, j] , A) \to 
\opn{K}^{\vee}_{}(A; a^j)^0 = A \]
is defined to be
\[  w_{a, j}^0(\delta_i) :=
\begin{cases}
1  & \tup{ if } i = 0 , \\
0 & \tup{ if } i \geq 1 .
\end{cases} \]
In degree $1$ the homomorphism 
\[ w_{a, j}^1 : \opn{Tel}^j(A; a)^1 = \opn{F}([0, j] , A) \to 
\opn{K}^{\vee}_{}(A; a^j)^1 = A \]
is defined to be 
$w_{a, j}^1(\delta_i) := a^{j-i}$. 
This makes sense since $i \in [0, j]$.

For a sequence $\bsym{a} = (a_1, \ldots, a_n)$ we define 
\begin{equation}
w_{\bsym{a}, j} :=
w_{a_1, j} \otimes \cdots \otimes  w_{a_n, j} :
\opn{Tel}_j(A; \bsym{a}) \to \opn{K}^{\vee}_{}(A; \bsym{a}^j) . 
\end{equation}
The homomorphisms of complexes $w_{\bsym{a}, j}$ are functorial in $j$, so in
the direct limit we get a homomorphism of complexes 
\begin{equation} \label{eqn:206}
w_{\bsym{a}} := \lim_{j \to} w_{\bsym{a}, j} : \opn{Tel}(A; \bsym{a}) \to 
\opn{K}^{\vee}_{\infty}(A; \bsym{a}) .
\end{equation}
Of course 
$w_{\bsym{a}} =  w_{a_1} \ot \cdots \ot  w_{a_n}$.
Let us also define 
\begin{equation}
u_{\bsym{a}} : \opn{Tel}(A; \bsym{a}) \to A \ , \
u_{\bsym{a}} := e_{\bsym{a}, \infty}^{\vee} \circ w_{\bsym{a}} \ ;
\end{equation}
cf.\ (\ref{eqn:213}).

\begin{lem} \label{lem:201}
The homomorphism $w_{\bsym{a}, j}$ is a homotopy equivalence, and the
homomorphism $w_{\bsym{a}}$ is a quasi-isomorphism.
\end{lem}

\begin{proof}
First consider the case $n = 1$, $A = \Z[t]$, the polynomial ring in the 
variable $t$, and $a = t$. The fact that $w_{t,j}$ is a quasi-isomorphism is an
easy calculation, once we notice that 
\[ \mrm{H}^0 \bigl( \opn{Tel}_j(\Z[t]; t) \bigr) = 
\mrm{H}^0 \bigl( \opn{K}^{\vee}_{}(\Z[t]; t^j) \bigr) = 0 , \]
and 
\[ \mrm{H}^1 \bigl( \opn{Tel}_j(\Z[t]; t) \bigr) \cong 
\mrm{H}^1 \bigl( \opn{K}^{\vee}_{}(\Z[t]; t^j) \bigr) \cong \Z[t] / (t^j) . \]

Next, for any $(A; a)$ we have a ring homomorphism $\Z[t] \to A$ sending 
$t \mapsto a$. Since $w_{a, j}$ is gotten from 
$w_{t, j}$ by the base change $A \ot_{\Z[t]} -$, and since 
$\opn{Tel}_j(\Z[t]; t)$ and $\opn{K}^{\vee}_{}(\Z[t]; t^j)$ are bounded
complexes of flat $\Z[t]$-modules, it follows that $w_{a, j}$ is also a
quasi-isomorphism. 

The flatness argument, with induction, also proves that for sequence $\bsym{a}$
of length $n \geq 2$ the homomorphism $w_{\bsym{a}, j}$ is a quasi-isomorphism.
Because $\opn{Tel}_j(A; \bsym{a})$ and $\opn{K}^{\vee}(A; \bsym{a}^j)$ are
bounded complexes of free $A$-modules, it follows that $w_{\bsym{a}, j}$ is a
homotopy equivalence.

Finally going to the direct limit preserves exactness, so $w_{\bsym{a}}$ is
a quasi-iso\-mor\-phism.
\end{proof}

Warning: the quasi-isomorphism $w_{\bsym{a}}$ is {\em not a homotopy
equivalence} (except in trivial cases). 

\begin{prop} \label{prop:251}
Let $\bsym{a}$ be a weakly proregular sequence in $A$, and $\a$ the ideal
generated by $\bsym{a}$.
For any $M \in \cat{D}(\cat{Mod} A)$ there is an isomorphism
\[ v^{\mrm{R}}_{\bsym{a}, M} : \mrm{R} \Gamma_{\a} (M) \to 
\opn{Tel}(A; \bsym{a}) \otimes_A M \]
in $\cat{D}(\cat{Mod} A)$. The isomorphism $v^{\mrm{R}}_{\bsym{a}, M}$ is
functorial in $M$, and satisfies 
\[ (u_{\bsym{a}} \ot 1_M) \circ v^{\mrm{R}}_{\bsym{a}, M}=
\sigma^{\mrm{R}}_M  \]
as morphisms $\mrm{R} \Gamma_{\a}  (M) \to M$.
\end{prop}

\begin{proof}
Combine Lemma \ref{lem:201} and Corollary \ref{cor:kosz.1}.
\end{proof}

Let us denote by $\a$ the ideal of $A$ generated by the sequence 
$\bsym{a} = (a_1, \ldots, a_n)$.
Recall that $A_j = A / \a^{j+1}$. Since 
$\a^{j n} \subset (\bsym{a}^j) \subset \a^j$
it follows that the canonical homomorphism
\begin{equation} \label{eqn:5.1}
\lim_{\leftarrow j} \, \bigl( A / (\bsym{a}^{j + 1}) \otimes_A M \bigr) \to
\lim_{\leftarrow j} \, \bigl( A_j \otimes_A M \bigr)  = \Lambda_{\a} (M)
\end{equation}
is bijective for any module $M$.

Let us write
\begin{equation}
 \opn{Tel}_j^{\vee}(A; \bsym{a}) := 
\opn{Hom}_A \bigl( \opn{Tel}_j(A; \bsym{a}), A \bigr) .
\end{equation}
We refer it as the {\em dual telescope complex}. 
Note that $\opn{Tel}_j^{\vee}(A; \bsym{a})$ is a complex of finite rank free
$A$-modules, concentrated in degrees $-n, \ldots, 0$.
The dual of the homomorphism $w_{\bsym{a}, j}$ 
is \begin{equation}
w_{\bsym{a}, j}^{\vee} : \opn{K}_{}(A; \bsym{a}^j) 
 \to \opn{Tel}_j^{\vee}(A; \bsym{a}) .
\end{equation}
Since $w_{\bsym{a}, j}$ is a homotopy equivalence, it
follows that $w_{\bsym{a}, j}^{\vee}$ is also a homotopy equivalence. 
Therefore
\[ \mrm{H}^0 (w_{\bsym{a}, j}^{\vee}) : 
\mrm{H}^0 ( \opn{Tel}_j^{\vee}(A; \bsym{a}) ) 
\to \mrm{H}^0 ( \opn{K}_{}(A; \bsym{a}^j) ) \]
is an isomorphism of $A$-modules. Define  
\begin{equation} \label{eqn:216}
\opn{tel}_{\bsym{a}, j} : 
\opn{Tel}_j^{\vee}(A; \bsym{a}) \to A / (\bsym{a}^j)
\end{equation}
to be the unique homomorphism of complexes such that 
\[ \mrm{H}^0 (\opn{tel}_{\bsym{a}, j}) \circ 
\mrm{H}^0 (w_{\bsym{a}, j}^{\vee})^{-1} : 
\mrm{H}^0 ( \opn{K}_{}(A; \bsym{a}^j) ) \to  A / (\bsym{a}^j) \]
is the canonical $A$-algebra  isomorphism (\ref{eqn:217}). 

For any $M \in \cat{C}(\cat{Mod} A)$ and $j \in \N$ 
there is a canonical isomorphism of complexes
\begin{equation} \label{eqn:tel.12}
\opn{Hom}_A \bigl( \opn{Tel}_j(A; \bsym{a}), M \bigr) \cong 
\opn{Tel}^{\vee}_j(A; \bsym{a}) \otimes_A M . 
\end{equation}
There is also  a canonical isomorphism of complexes
\begin{equation} \label{eqn:tel.6}
\opn{Hom}_A \bigl( \opn{Tel}(A; \bsym{a}), M \bigr) \cong \lim_{\leftarrow j} \,
\opn{Hom}_A \bigl( \opn{Tel}_j(A; \bsym{a}), M \bigr) 
\end{equation}
coming from (\ref{eqn:214}).
We define a homomorphism of complexes 
\begin{equation}
\begin{aligned}
\opn{tel}_{\bsym{a}, M, j} & : 
\opn{Hom}_A \bigl( \opn{Tel}_j(A; \bsym{a}), M \bigr) \to 
A / (\bsym{a}^j) \otimes_A M \ ,
\\
\opn{tel}_{\bsym{a}, M, j} & := \opn{tel}_{\bsym{a}, j} \otimes \, 1_M \ ,
\end{aligned}
\end{equation}
using the isomorphism (\ref{eqn:tel.12}).

\begin{dfn} \label{dfn:280}
For any $M \in \cat{C}(\cat{Mod} A)$ let 
\[ \opn{tel}_{\bsym{a}, M} : 
\opn{Hom}_A \bigl( \opn{Tel}(A; \bsym{a}), M \bigr) \to  \Lambda_{\a} (M) \]
be the homomorphism of complexes 
\[ \opn{tel}_{\bsym{a}, M} := 
\lim_{\leftarrow j} \, \opn{tel}_{\bsym{a}, M, j} 
= \lim_{\leftarrow j} \, (\opn{tel}_{\bsym{a}, j} \otimes \, 1_M) \ . \]
Here we use the isomorphisms (\ref{eqn:tel.6}) and (\ref{eqn:5.1}).
\end{dfn}

Note that $\opn{tel}_{\bsym{a}, M}$ is functorial in $M$.

\begin{rem} \label{rem:tel.1}
For a module $M$ the homomorphism 
\[ \opn{tel}_{\bsym{a}, M} :  
\opn{Hom}_A \bigl( \opn{Tel}(A; \bsym{a})^0, M \bigr) \to \La_{\a}(M) \]
can be expressed explicitly as an $\a$-adically convergent power series. First
we note that an element 
$f \in \opn{Hom}_A \bigl( \opn{Tel}(A; \bsym{a})^0, M \bigr)$
is the same as a function $f : \N^n \to M$.
For $a \in A$ and $i \in \N$ we define the ``modified $i$-th power'' 
$p(a, i) \in A$ to be
$p(a, 0) := 1$, $p(a, 1) := -1$ and 
$p(a, i) := -a^{i-1}$ if $i \geq 2$.
Then 
\begin{equation} \label{eqn:tel.13}
 \opn{tel}_{\bsym{a}, M}(f) = \sum_{(i_1, \ldots, i_n) \in \N^n} \ 
p(a_1, i_1) \cdots p(a_n, i_n)  f(i_1, \ldots, i_n) \in 
\Lambda_{\a} (M) .
\end{equation}
We shall not require this formula.
\end{rem}

Consider the homomorphism of complexes 
\begin{equation}
\opn{Hom}(u_{\bsym{a}}, 1_M) : M \cong \opn{Hom}_A(A, M) \to 
\opn{Hom}_A \bigl( \opn{Tel}(A; \bsym{a}), M \bigr) 
\end{equation}
induced by 
$u_{\bsym{a}} : \opn{Tel}(A; \bsym{a}) \to A$. 

\begin{lem} \label{lem:203}
For any $M \in \cat{Mod} A$ there is equality
$\opn{tel}_{\bsym{a}, M} \circ \opn{Hom}(u_{\bsym{a}}, 1_M) = \tau_M$ , 
as homomorphisms 
$M \to \Lambda_{\a}(M)$.
\end{lem}

\begin{proof}
It suffices to prove that for every $j \geq 0$ there is equality 
\[ \opn{tel}_{\bsym{a}, M,j} \circ \opn{Hom}(u_{\bsym{a}, j}, 1_M)  = 
f_j \circ 1_M \]
as homomorphisms $M \to A / (\bsym{a}^j)$, where 
$f_j : A \to  A / (\bsym{a}^j)$ is the canonical ring homomorphism, and
$u_{\bsym{a}, j} := e_{\bsym{a}, j}^{\vee} \circ w_{\bsym{a} ,j}$.
But everything is functorial in $M$, so we can restrict attention to $M = A$. 
Thus we have to show that 
$\opn{tel}_{\bsym{a}, j} \circ\, u_{\bsym{a}, j}^{\vee} = f_j$.

Consider the diagram
\[ \UseTips \xymatrix @C=7ex @R=7ex {
A
\ar[r]^{e_{\bsym{a}, j}}
\ar[dr]_{u_{\bsym{a}, j}^{\vee}}
\ar@(u,u)[rr]^{f_j}
&
\opn{K}(A; \bsym{a}^j)
\ar[r]^{g_j}
\ar[d]^{w_{\bsym{a} ,j}}
&
A / (\bsym{a}^j)
\\
& 
\opn{Tel}_j^{\vee}(A; \bsym{a})
\ar[ur]_{\opn{tel}_{\bsym{a}, j} }
} \]
where $g_j$ is the DG algebra homomorphism. 
By definition the three triangles are commutative. Hence the whole diagram is
commutative.
\end{proof}

\begin{thm} \label{thm:250}
Let $A$ be any ring, let $\bsym{a}$ be a weakly proregular sequence in $A$, 
and let $P$ be a flat  $A$-module. Then  the homomorphism
\[ \opn{tel}_{\bsym{a}, P} : 
\opn{Hom}_A \bigl( \opn{Tel}(A; \bsym{a}), P \bigr) \to \Lambda_{\a} (P) \]
is a quasi-isomorphism.
\end{thm}

\begin{proof}
Given an inverse system $\{ M_j \}_{j \in \N}$ of complexes of abelian
groups, for every integer $k$ there is a canonical homomorphism
\[ \psi^k : \mrm{H}^k \Bigl( \lim_{\leftarrow j} \, M_j \Bigr) \to 
\lim_{\leftarrow j} \, \bigl( \mrm{H}^k (M_j) \bigr) . \]

By definition of $\opn{tel}_{\bsym{a}, P}$, for $k = 0$ there is a
commutative diagram
\[ \UseTips \xymatrix @C=18ex @R=6ex {
\mrm{H}^k \Bigl(  \opn{Hom}_A \bigl( \opn{Tel}(A; \bsym{a}), P \bigr) \Bigr)
\ar[r]^{\mrm{H}^k (\opn{tel}_{\bsym{a}, P}) }
\ar[d]_{\cong}
&
\Lambda_{\a} (P)
\ar[d]^{\cong}
\\
\mrm{H}^k \Bigl( \lim_{\leftarrow j} \,  
\bigl( \opn{Tel}^{\vee}_j(A; \bsym{a}) \ot_A P \bigr) \Bigr) 
\ar[r]^(0.54){\mrm{H}^k ( \lim_{\leftarrow j} \, \opn{tel}_{\bsym{a}, P, j}) }
\ar[d]_{\psi^k}
&
\lim_{\leftarrow j} \,  \bigl( ( A / (\bsym{a}^j) ) \ot_A P \bigr)
\\
\lim_{\leftarrow j} \, \mrm{H}^k 
\bigl( \opn{Tel}^{\vee}_j(A; \bsym{a}) \ot_A P \bigr) 
\ar[ur]_(0.54){\quad \quad \lim_{\leftarrow j} \, \mrm{H}^k ( 
\opn{tel}_{\bsym{a}, P, j}) }
} \]
The left part of the diagram makes sense for every $k$.
We will prove that:
\begin{enumerate}
\item 
$\lim_{\leftarrow j} \, \mrm{H}^k 
\bigl( \opn{Tel}^{\vee}_j(A; \bsym{a}) \ot_A P \bigr) = 0$
for all $k \neq 0$. 

\item 
$\mrm{H}^0 ( \opn{tel}_{\bsym{a}, P, j})$ is bijective for every $j \geq 0$.

\item $\psi^k$ is bijective for every $k$.
\end{enumerate}
Together these imply that 
$\mrm{H}^k ( \opn{tel}_{\bsym{a}, P})$ is bijective for every $k$.

There are quasi-isomorphisms 
\[ w_{\bsym{a}, j}^{\vee}  : \opn{K}(A; \bsym{a}^j)  \to
\opn{Tel}^{\vee}_j(A; \bsym{a})  \]
that are compatible with $j$.
Since $P$ is flat, according to Corollary \ref{cor:293} we get induced
isomorphisms 
\begin{equation} \label{eqn:254}
\mrm{H}^k \bigl( \opn{Tel}^{\vee}_j(A; \bsym{a}) \ot_A P \bigr) \cong
\mrm{H}^k \bigl( \opn{K}(A; \bsym{a}^j) \ot_A P \bigr) \cong
\mrm{H}^k \bigl( \opn{K}(A; \bsym{a}^j) \bigr)  \ot_A P
\end{equation}
that are compatible with $j$.

There is a canonical ring isomorphism 
$\mrm{H}^0 \bigl( \opn{K}(A; \bsym{a}^j) \bigl) \cong A / (\bsym{a}^j)$.
By definition of $\opn{tel}_{\bsym{a}, j}$, the homomorphism 
\[ \mrm{H}^0 ( \opn{tel}_{\bsym{a}, j}) : 
\mrm{H}^0 \bigl( \opn{Tel}^{\vee}_j(A; \bsym{a}) \bigr) \to
A / (\bsym{a}^j) \]
is bijective. 
Hence, using Corollary \ref{cor:293} again, we see that
$\mrm{H}^0 ( \opn{tel}_{\bsym{a}, P, j})$ is also
bijective. This proves (2).

We are given that $\bsym{a}$ is a weakly proregular sequence, which means that
the homomorphism
\[  \mrm{H}^k(p_{\bsym{a}, j', j}) :
 \mrm{H}^k \bigl( \opn{K}(A; \bsym{a}^{j'}) \bigr)   \to 
\mrm{H}^k \bigl( \opn{K}(A; \bsym{a}^j) \bigr)  \]
is zero for $k < 0$ and $j' \gg j$.
As for $k = 0$, we know that  
\[ \mrm{H}^0 \bigl( \opn{K}(A; \bsym{a}^{j'}) \bigr)   \to 
\mrm{H}^0 \bigl( \opn{K}(A; \bsym{a}^j) \bigr)  \]
is surjective for $j' \geq j$. Of course 
$\mrm{H}^k \bigl( \opn{K}(A; \bsym{a}^j) \bigr) = 0$ 
for $k > 0$. 
Thus for every $k$ the inverse system of modules 
\[ \bigl\{  \mrm{H}^k \bigl( \opn{Tel}^{\vee}_j(A; \bsym{a}) \ot_A P \bigr) 
\bigr\}_{j \in \N}  \cong
\bigl\{  \mrm{H}^k \bigl( \opn{K}(A; \bsym{a}^j) \bigr) \ot_A P 
\bigr\}_{j \in \N}  \]
satisfies the Mittag-Leffler condition.

The inverse system of complexes 
$\bigl\{ \opn{Tel}^{\vee}_j(A; \bsym{a}) \ot_A P \bigr\}_{j \in \N}$
also satisfies the Mittag-Leffler  condition, since it has surjective transition
maps.  (Warning: see Remark \ref{rem:251}.)
Therefore, by  \cite[Proposition 1.1.24]{KS1} or \cite[Theorem 3.5.8]{We},
the homomorphisms
\[ \psi^k : 
\mrm{H}^k \Bigl( 
\lim_{\leftarrow j} \, \bigl( \opn{Tel}^{\vee}_j(A; \bsym{a}) \ot_A P \bigr) 
\Bigr) \to
\lim_{\leftarrow j} \, \mrm{H}^k
\bigl( \opn{Tel}^{\vee}_j(A; \bsym{a}) \ot_A P \bigr) 
\]
are bijective. Thus (3) is true. 

Finally, weak proregularity, with the isomorphisms (\ref{eqn:254}),
tell us that the homomorphism 
\[  \mrm{H}^k \bigl( \opn{Tel}^{\vee}_{j'}(A; \bsym{a}) \ot_A P \bigr)   \to 
\mrm{H}^k \bigl( \opn{Tel}^{\vee}_j(A; \bsym{a}) \ot_A P \bigr)  \]
is zero for $k < 0$ and $j' \gg j$.
And everything is zero for $k > 0$. This implies (1). 
\end{proof}

\begin{cor} \label{cor:294}
Assume $\bsym{a}$ is a weakly proregular sequence in $A$. Then
for every K-flat complex $P$ the homomorphism
\[ \opn{tel}_{\bsym{a}, P} : \opn{Hom}_A ( \opn{Tel}(A; \bsym{a}), P) \to 
\Lambda_{\a}(P)  \]
is a quasi-isomorphism.
\end{cor}

\begin{proof}
By Proposition \ref{prop:28} we can assume that $P$ is a complex of flat
modules. By Proposition \ref{prop:1.1} we reduce to
the case of a single flat module $P$. This is the theorem above. 
\end{proof}

\begin{rem} \label{rem:251}
The inverse systems of complexes 
$\bigl\{ \opn{K}(A; \bsym{a}^j) \ot_A P \bigr\}_{j \in \N}$
does not satisfy the ML condition; so we can't expect to get a
quasi-isomorphism in the inverse limit: the homomorphism
\[ \lim_{\leftarrow j} \, (w_{\bsym{a}, j}^{\vee} \ot 1_P) : 
\lim_{\leftarrow j} \, \bigl( \opn{K}(A; \bsym{a}^j) \ot_A P \bigr) \to
\lim_{\leftarrow j} \, \bigl( \opn{Tel}^{\vee}_j(A; \bsym{a}) \ot_A P \bigr) \]
will usually not be a quasi-isomorphism.

Indeed, this will even fail for the ring $A := \K[t]$, the  polynomial algebra
over a field $\K$, with sequence $\bsym{a} := (t)$ and flat module $P := A$. 
Here we get
\[ \mrm{H}^0 \bigl( \lim_{\leftarrow j} \, \opn{Tel}^{\vee}_j(A; \bsym{a}) 
\bigr) \cong  
\mrm{H}^0 \bigl( 
\opn{Hom}_A \bigl( \opn{Tel}(A; \bsym{a}), A \bigr) \bigr)
\cong \Lambda_{\a} (A) \cong \K[[t]] . \]
But 
$\lim_{\leftarrow j} \, \opn{K}(A; \bsym{a}^j)^0 \cong A$
and
$\lim_{\leftarrow j} \, \opn{K}(A; \bsym{a}^j)^{-1} = 0$,
giving 
\[ \mrm{H}^0 \bigl( \lim_{\leftarrow j} \, \opn{K}(A; \bsym{a}^j) \bigr)
\cong  A = \K[t] .  \]
\end{rem}

\begin{cor} \label{cor:tel.1}
Assume $\bsym{a}$ is a weakly proregular sequence in $A$.
For any $M \in \cat{D}(\cat{Mod} A)$ there is an isomorphism
\[ \opn{tel}_{\bsym{a}, M}^{\mrm{L}} : 
\opn{Hom}_A \bigl( \opn{Tel}(A; \bsym{a}) , M \bigr) 
\iso \mrm{L} \Lambda_{\a} (M) \]
in $\cat{D}(\cat{Mod} A)$, functorial in $M$, such that
\[ \opn{tel}_{\bsym{a}, M} \circ \opn{Hom}(u_{\bsym{a}}, 1_M) 
= \tau^{\mrm{L}}_M , \] 
as morphisms $M \to \mrm{L} \Lambda_{\a}(M)$.
\end{cor}

\begin{proof}
It is enough to consider a K-flat complex $M = P$. 
For this we combine Theorem \ref{thm:250}, Proposition \ref{prop:26} and Lemma
\ref{lem:203}.
\end{proof}

The corollary says that the diagram 
\begin{equation}
\UseTips \xymatrix @C=10ex @R=6ex {
M
\ar[d]_{\opn{Hom}(u_{\bsym{a}}, 1_M)}
\ar[dr]^{\tau^{\mrm{L}} _M}
& 
\\
\opn{Hom}_A \bigl( \opn{Tel}(A; \bsym{a}), M \bigr)
\ar[r]_(0.65){\opn{tel}^{\mrm{L}} _{\bsym{a}, M}}
&
\mrm{L} \Lambda_{\a} (M)
} 
\end{equation}
is commutative.

\begin{cor} \label{cor:261}
Let $\a$ be a weakly proregular ideal in $A$. 
The cohomological dimension of the functor $\mrm{L} \Lambda_{\a}$
is finite. Indeed, if $\a$ can be generated by a weakly proregular sequence of
length $n$, then the cohomological dimension of $\mrm{L} \Lambda_{\a}$ is at
most $n$.
\end{cor}

\begin{proof}
This is immediate from Corollary \ref{cor:tel.1}.
\end{proof}

\begin{rem} \label{rem:280}
The name ``telescope complex'' is inspired by a standard construction in
algebraic topology; see \cite{GM}. However here we are looking at a specific
complex of $A$-modules, and we prove that it has the expected homological
properties.

The result  \cite[Theorem 4.5]{Sc}, which corresponds to our Theorem
\ref{thm:250}, only talks about {\em bounded
complexes} $M$, and there is an extra assumption that {\em each $a_i$ has
bounded torsion}. Moreover, Schenzel states that the question for unbounded
complexes is {\em open as far as he knows}. We answer this in the affirmative in
our Theorem \ref{thm:250}: our result holds for unbounded complexes, and there 
is no further assumption beyond the weak proregularity of the sequence 
$\bsym{a}$. 

In \cite{AJL1} there is an assertion similar to Theorem \ref{thm:250}
(more precisely, it corresponds to Theorem \ref{thm:mgm.3}). This is
\cite[formula $\tup{(0.3)}_{\tup{aff}}$]{AJL1},
that also refers to unbounded complexes, and makes no assumption except 
proregularity of the sequence $\bsym{a}$. In \cite[Correction]{AJL1} there is
some elaboration on the specific conditions needed for the proofs to be
correct. As far as we understand, the correct conditions are weak
proregularity for $\bsym{a}$, plus bounded torsion for each $a_i$. 
Hence our Theorem \ref{thm:250}, and also our Theorem
\ref{thm:mgm.3}, appear to be stronger than the affine versions of the results
in \cite{AJL1}. 

Our proof of Theorem \ref{thm:250}  does not depend on any of the results in
either \cite{AJL1} or \cite{Sc}. We believe our proof is quite transparent. 
Note also that we give an explicit formula for the homomorphism of complexes
$\opn{tel}_{\bsym{a}, P}$, that is not found in prior papers. 
\end{rem}
