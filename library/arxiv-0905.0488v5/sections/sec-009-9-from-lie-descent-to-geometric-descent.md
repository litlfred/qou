---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES"
section_id: sec-009-9-from-lie-descent-to-geometric-descent
section_title: "From Lie Descent to Geometric Descent"
section_number: 9
pages: 39-42
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.957
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES — Let X be a smooth algebraic variety over a ﬁeld K containing the real numbers. We introduce the notion of twisted associative (resp."
---
\label{sec:Lie-Geo}

Suppose $\mcal{G}$ is a sheaf of abelian groups on a topological space $X$. 
Let us recall how to construct the \v{C}ech cosimplicial abelian group
$\mrm{C}(\bsym{U}, \mcal{G})$ associated to $\mcal{G}$ and to an  
open covering $\bsym{U} = \{ U_k \}_{k \in K}$ of $X$. 
For $p \in \mbb{N}$ we take the abelian group
\begin{equation} \label{eqn:Lie-Geo.103}
\mrm{C}^p(\bsym{U}, \mcal{G}) := 
\prod_{\bsym{k} \in \bsym{\Delta}_p(K)}
\Gamma(U_{\bsym{k}}, \mcal{G}) .
\end{equation}
See formula (\ref{eqn:mdd.111}) regarding the set $\bsym{\Delta}_p(K)$.
If $\bsym{k} \in \bsym{\Delta}_q(K)$ and
$\alpha \in \bsym{\Delta}^q_p$, then
$\al(\bsym{k}) \in \bsym{\Delta}_p(K)$, and there is an inclusion of open sets
$U_{\bsym{k}} \subset U_{\alpha(\bsym{k})}$,
so by restriction there is an induced homomorphism
$\mrm{C}^p(\bsym{U}, \mcal{G}) \to 
\mrm{C}^q(\bsym{U}, \mcal{G})$.
If $\mcal{G}$ is a sheaf of DG Lie algebras, then $\mrm{C}(\bsym{U}, \mcal{G})$
is a cosimplicial DG Lie algebra.

Now suppose 
$\bsym{U}' = \{ U_k \}_{k \in K'}$
is another open covering of $X$, and 
$\rho : \bsym{U}' \to \bsym{U}$ is a refinement.
Then there is a homomorphism of cosimplicial DG Lie algebras 
\begin{equation} \label{eqn:Lie-Geo.106}
\rho^* : \mrm{C}(\bsym{U}, \mcal{G}) \to 
\mrm{C}(\bsym{U}', \mcal{G}) ,
\end{equation}
with an obvious formula. 

\begin{setup} \label{setup:6}
$\K$ is a field of characteristic $0$; $(R, \m)$ is a parameter 
algebra over $\K$; and $X$ is a smooth algebraic variety
over $\K$, with structure sheaf $\mcal{O}_X$.
\end{setup}

This is the same as Setup \ref{setup:200}, except that here $X$ is a smooth
algebraic variety.

In Section \ref{sec:defs-DG-Lie} we discussed the sheaves of DG Lie algebras  
$\mcal{T}_{\mrm{poly}, X}$, $\mcal{D}_{\mrm{poly}, X}$ and 
$\mcal{D}_{\mrm{poly}, X}^{\mrm{nor}}$ on the variety $X$. 
Lie descent data $\opn{Desc}(\opn{Del}((\g, R))$ for a cosimplicial quantum
type DG Lie algebra $\g$ was introduced in Section \ref{sec:Lie-desc}, and
its functorial properties were shown.

Recall the stacks of crossed groupoids $\twocat{AssDef}(R, \mcal{O}_X)$ 
and $\twocat{PoisDef}(R, \mcal{O}_X)$ from Section \ref{sec:tw.sh}.
Let us write $\twocat{P}(R, X)$ for either of these stacks. 
The geometric descent data 
$\opn{Desc} \bigl( \opn{C}(\bsym{U}, \twocat{P}(R, X)) \bigr)$ was introduced in
Section \ref{sec:mdd}. The functorial dependence of 
$\ol{\opn{Desc}} \bigl( \opn{C}(\bsym{U}, \twocat{P}(R, X)) \bigr)$ on
the open covering $\bsym{U}$ is shown in
formula (\ref{eqn:23}). Regarding the dependence on $R$, consider a
homomorphism of parameter algebras $\sigma : R \to R'$.
Given a descent datum 
\[ \bsym{d} = \bigl( \{ \mcal{A}_{k_0} \}_{k_0 \in K}, \ldots \bigr) \in
\opn{Desc} \bigl( \opn{C}(\bsym{U}, \twocat{P}(R, X)) \bigr) \]
as in (\ref{eqn:mdd.120}),
let $\mcal{A}'_{k_0} := R' \hatotimes{R} \mcal{A}_{k_0}$, which by 
Proposition \ref{prop:206} is an
$R'$-deformation of $\mcal{O}_{U_{k_0}}$.
There are induced $R'$-linear gauge transformations
$g'_{k_0, k_1}$ and induced gauge elements
$a'_{k_0, k_1, k_2}$, and together these make up a descent datum
$\sigma(\bsym{d}) =  \bigl( \{ \mcal{A}'_{k_0} \}, \ldots \bigr)$.
This construction is a function
\begin{equation} \label{eqn:24}
\sigma : \opn{Desc} \bigl( \opn{C}(\bsym{U}, \twocat{P}(R, X)) \bigr)
\to \opn{Desc} \bigl( \opn{C}(\bsym{U} , \twocat{P}(R', X)) \bigr) , 
\end{equation}
which respects gauge equivalence.

\begin{thm}[Geometrization of Descent Data] \label{thm:11}
Let $(R, \m)$ and $X$ be as in Setup \tup{\ref{setup:6}}, and let
$\bsym{U}$ be a finite affine open covering of $X$.
We consider two cases\tup{:}
\begin{enumerate}
\item[$\vartriangleright$] The associative case, in which 
\[ \twocat{P}(R, X) := \twocat{AssDef}(R, \mcal{O}_X) \quad
\text{and} \quad
\g(\bsym{U}) := \mrm{C}(\bsym{U}, 
\mcal{D}_{\mrm{poly}, X}^{\mrm{nor}})
. \] 

\item[$\vartriangleright$] The Poisson case, in which 
\[ \twocat{P}(R, X) := \twocat{PoisDef}(R, \mcal{O}_X) \quad
\text{and} \quad
\g(\bsym{U}) := \mrm{C}(\bsym{U}, \mcal{T}_{\mrm{poly}, X}) . \] 
\end{enumerate}
So $\opn{C}(\bsym{U} , \twocat{P}(R, X))$
and 
$\opn{Del}(\g(\bsym{U}) , R)$ are cosimplicial crossed groupoids. 

In both cases there is a bijection
\[  \ol{\opn{geo}} : 
\ol{\opn{Desc}} \bigl( \opn{Del}(\g(\bsym{U}) , R) \bigr)
\iso
\ol{\opn{Desc}} \bigl( \opn{C}(\bsym{U} , \twocat{P}(R, X)) \bigr) , \]
which we call {\em geometrization}. The bijection $\opn{geo}$ respect
homomorphisms of parameter algebras $R \to R'$, and
refinements of coverings $\bsym{U}' \to \bsym{U}$.
\end{thm}

\begin{proof}
By Theorem \ref{thm:205} there is a weak equivalence of cosimplicial crossed 
groupoids  
\[  \opn{geo} :  \opn{Del}(\g(\bsym{U}) , R) \to
\opn{C}(\bsym{U} , \twocat{P}(R, X))  . \]
(Actually this is an equivalence of crossed groupoids in each cosimplicial
dimension.) Theorem \ref{thm:100} says that 
$\ol{\opn{geo}} := \ol{\opn{Desc}}(\opn{geo})$ is a bijection.
The functorial dependence on $R$ and $\bsym{U}$ is clear.
\end{proof}

\begin{rem}
More generally, if $\mcal{G}$ is any sheaf of quantum type DG Lie
algebras on a topological space $X$, 
$\bsym{U}$ is an open covering of $X$,
$\g(\bsym{U}) := \mrm{C}(\bsym{U}, \mcal{G})$
and 
$\bsym{\delta} \in \opn{Desc}\bigl( \opn{Del}(\g(\bsym{U}), R) \bigr)$, 
then $\opn{geo}(\bsym{\delta})$ is a geometric descent datum for a gerbe 
$\gerbe{H}$ on $X$. For an index $k \in K$ 
there is an object
$k \in \opn{Ob} (\gerbe{H}(U_k))$, and its sheaf of automorphisms
is 
$\gerbe{H}(k) = \opn{Exp}(\m \hot \mcal{G}^{-1})_{\om_{k}}$.
It might be interesting to study the kind of gerbes that arise in
this way.
\end{rem}

Suppose $X'$ is another smooth algebraic variety, and $g : X' \to X$ is an
\'etale morphism. 
It follows from \cite[Proposition 4.6]{Ye2} that there are
induced homomorphisms of sheaves of DG Lie algebras 
\begin{equation}
g^* : \mcal{T}^{}_{\mrm{poly}, X} \to
g_* (\mcal{T}^{}_{\mrm{poly}, X'})
\end{equation}
and
\begin{equation}
g^* : \mcal{D}_{\mrm{poly}, X}^{\mrm{nor}} \to 
g_* (\mcal{D}_{\mrm{poly}, X'}^{\mrm{nor}})
\end{equation}
on $X$, extending the ring homomorphism
$g^* : \mcal{O}_X \to g_* (\mcal{O}_{X'}$).

Let $\bsym{U} = \{ U_k \}_{k \in K}$ be an open covering of $X$,
and $\bsym{U}' = \{ U'_k \}_{k \in K'}$ an open covering of
$X'$. A {\em morphism of coverings extending $g$}
is a function $\rho : K' \to K$, such that $g(U'_k) \subset U_{\rho(k)}$ for
every $k \in K'$. We also say that
$\rho : \bsym{U}' \to \bsym{U}$
is a morphism of coverings extending $g$.

Suppose $\bsym{V} = \{ V_l \}_{l \in L}$ is another open
covering of $X$. We get a new open covering 
$\bsym{U} \coprod \bsym{V} := \{ W_m \}_{m \in M}$ of $X$, where
$M := K \coprod L$, $W_m := U_m$ if $m \in K$, and 
$W_m := V_m$ if $m \in L$. (Of course $\bsym{U} \coprod \bsym{V}$ has a
lot of redundancy.) If $\tau : \bsym{V}' \to \bsym{V}$
is a morphism of coverings extending $g$, then 
$\rho \amalg \tau : \bsym{U}' \coprod \bsym{V}' \to \bsym{U} \coprod \bsym{V}$
is also a morphism of coverings extending $g$.

Given a morphism of coverings
$\rho : \bsym{U}' \to \bsym{U}$ extending $g$, 
there is an induced homomorphism of cosimplicial DG Lie algebras
$\rho^* : \g(\bsym{U}) \to \g(\bsym{U}')$.
Here we use the notation of Theorem \ref{thm:11}, with obvious
modifications; e.g.\ 
$\g(\bsym{U}') := \mrm{C}(\bsym{U}', \mcal{T}_{\mrm{poly}, X'})$
in the Poisson case.

\begin{thm} \label{thm:7}
Let $R$ and $X$ be as in Setup \tup{\ref{setup:6}}, 
let $g : X' \to X$ be an \'etale morphism of varieties, and let 
$\si : R \to R'$ be a homomorphism of parameter algebras.
We use the notation of Theorem
\tup{\ref{thm:11}}, with obvious modifications pertaining to the
variety $X'$ and the algebra $R'$. Then, both in the Poisson case and
in the associative case, there is a unique function
\[ \opn{ind}_{\si, g} : 
\ol{\opn{TwOb}} \bigl( \twocat{P}(R, X) \bigr) \to 
\ol{\opn{TwOb}} \bigl( \twocat{P}(R', X') \bigr)  \]
with this property\tup{:}
\begin{enumerate}
\rmitem{$\lozenge$} Suppose $\bsym{U}$ \tup{(}resp.\ $\bsym{U}'$\tup{)}
is a finite affine open covering of $X$
\tup{(}resp.\ $X'$\tup{)}, and
$\rho : \bsym{U}' \to \bsym{U}$
is a morphism of coverings extending $g$.
Then the diagram of sets \tup{(\ref{eqn:220})} is commutative.
\end{enumerate}

\begin{equation} \label{eqn:220}
\UseTips \xymatrix @C=5ex @R=5ex {
\ol{\opn{Desc}} \bigl( \opn{Del}(\g(\bsym{U}), R) \bigr)
\ar[r]^(0.46){\ol{\opn{geo}}}
\ar[d]_{\ol{\opn{Desc}} (\opn{Del}(\rho^*, \si ))}
& 
\ol{\opn{Desc}} \bigl( \opn{C}(\bsym{U}, \twocat{P}(R, X)) \bigr)
& 
\ol{\opn{TwOb}} \bigl( \twocat{P}(R, X) \bigr) 
\ar[l]_(0.45){\ol{\opn{dec}}}
\ar[d]^{\opn{ind}_{\si, g}} 
\\
\ol{\opn{Desc}} \bigl( \opn{Del}(\g(\bsym{U}'), R') \bigr)
\ar[r]^(0.46){\ol{\opn{geo}}}
& 
\ol{\opn{Desc}} \bigl( \opn{C}(\bsym{U}', \twocat{P}(R', X')) \bigr)
& 
\ol{\opn{TwOb}} \bigl( \twocat{P}(R', X') \bigr) 
\ar[l]_(0.45){\ol{\opn{dec}}}
}
\end{equation}
Here $\ol{\opn{dec}}$ is the decomposition from Theorem \tup{\ref{thm:glu.1}},
$\ol{\opn{geo}}$ is the geometrization from Theorem \tup{\ref{thm:11}}, and 
$\ol{\opn{Desc}} ( \opn{Del}( \rho^*, \si ))$ is the function from Theorem
\tup{\ref{thm:Lie-desc.101}}.
\end{thm}

\begin{proof}
Choose coverings  $\bsym{U}$ and $\bsym{U}'$, and a morphism of
coverings
$\rho : \bsym{U}' \to \bsym{U}$, 
as in property ($\lozenge$). This is possible of course. 
The horizontal arrows in the diagram are bijections.
Define 
\[ \opn{ind}_{\si, g} :
\ol{\opn{TwOb}} \bigl( \twocat{P}(R, X) \bigr) \to 
\ol{\opn{TwOb}} \bigl( \twocat{P}(R', X') \bigr) \]
to be the unique function that makes the diagram commute.

It remains to show that the function
$\opn{ind}_{\si, g}$ is independent of
the choice of open coverings $\bsym{U}$ and $\bsym{U}'$, and the of morphism 
$\rho$ between them. So let $\bsym{V}$ be another finite affine
open covering of $X$, let $\bsym{V}'$ be another such covering of $X'$, and let
$\tau : \bsym{V}' \to \bsym{V}$
be a morphism of coverings extending $g$.
Consider the open covering 
$\bsym{W} := \bsym{U} \coprod \bsym{V}$ of $X$, the open covering 
$\bsym{W}' := \bsym{U}' \coprod \bsym{V}'$ of $X'$,
and the morphism of coverings 
$\chi := \rho \amalg \tau : \bsym{W}' \to \bsym{W}$
extending $g$. We obtain a commutative diagram of morphisms of coverings
\begin{equation} \label{eqn:Lie-Geo.15}
\UseTips \xymatrix @C=6ex @R=4ex {
\bsym{U}
\ar[r]
&
\bsym{W}
&
\bsym{V}
\ar[l]
\\
\bsym{U}'
\ar[u]^{\rho}
\ar[r]
& 
\bsym{W}' 
\ar[u]_{\chi}
&
\bsym{V}'
\ar[l]
\ar[u]_{\tau}
}
\end{equation}
extending $g$ vertically, and extending $\bsym{1}_X$ and  $\bsym{1}_{X'}$
horizontally.  
The functoriality in Theorem \ref{thm:11} and in Proposition
\ref{prop:bitorsors.6}, applied to the left square in diagram
(\ref{eqn:Lie-Geo.15}), and to the homomorphism $\si : R \to R'$,
yields a big commutative diagram in the shape of a rectangular box. 
The front face of this big diagram is the diagram in property ($\lozenge$),
and the rear face is the same diagram but with $\bsym{W}$ instead of
$\bsym{U}$. All horizontal arrows in the big diagram are bijections. 
It follows that the function $\opn{ind}_{\si, g}$ is the same when defined
using $\chi : \bsym{W}' \to \bsym{W}$.
But then, working with the right square in diagram (\ref{eqn:Lie-Geo.15}),
we see that the function $\opn{ind}_{\si, g}$ is also the same when defined
using $\tau : \bsym{V}' \to \bsym{V}$.
\end{proof}
