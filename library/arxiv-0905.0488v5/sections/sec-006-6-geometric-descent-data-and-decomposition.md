---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES"
section_id: sec-006-6-geometric-descent-data-and-decomposition
section_title: "Geometric Descent Data and Decomposition"
section_number: 6
pages: 28-33
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.979
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES — Let X be a smooth algebraic variety over a ﬁeld K containing the real numbers. We introduce the notion of twisted associative (resp."
---
\label{sec:mdd}

In this section we study the decomposition of twisted objects on open
coverings.

Given a set $K$ and $p \in \N$, we let 
\begin{equation} \label{eqn:mdd.111}
\bsym{\Delta}_p(K) := \{ (k_0, \ldots, k_p) \mid k_i \in K \} .
\end{equation}
The collection $\{ \bsym{\Delta}_p(K) \}_{p \in \N}$ is a simplicial set. 
Recall that for an open covering $\bsym{U} = \{ U_k \}_{k \in K}$ of a
topological space $X$, and for 
$\bsym{k} = (k_0, \ldots, k_p) \in \bsym{\Delta}_p(K)$, 
we write 
$U_{\bsym{k}} = U_{k_0} \cap \cdots \cap U_{k_p}$.

Let $\{ G^j \}_{j \in J}$ be a collection of crossed groupoids
indexed by some set $J$.
Their product is the crossed groupoid  
$\prod_{j \in J} G^j$, with set of objects 
$\opn{Ob}(\prod_{j \in J} G^j) := 
\prod_{j \in J} \opn{Ob}(G^j)$
etc.

The notion of stack of crossed groupoids
\[ \twocat{P} = ( \twocat{P}_1, \twocat{P}_2, 
\opn{Ad}_{\twocat{P}_1 \crvar \twocat{P}_{2}}, \opn{D} ) \]
on a topological space $X$ was introduced in Definition \ref{dfn:200}.
We will make frequent use of the functor of stacks 
$\opn{IG} : \twocat{P}_1 \to \twocat{Grp}(X)$,
and the natural transformation
$\opn{ig} : \opn{IG} \twoto \opn{Ad}_{\twocat{P}_1}$,
from Proposition \ref{prop:201}.

\begin{dfn} \label{dfn:mdd.101}
Let $\twocat{P}$ be a stack of crossed groupoids on a
topological space $X$, and let $\bsym{U} = \{ U_k \}_{k \in K}$ be an
open covering of $X$. For any $p \in \N$ define the crossed groupoid 
\[ \opn{C}^p(\bsym{U}, \twocat{P}) := 
\prod_{\bsym{k} \in \bsym{\Delta}_p(K)} \twocat{P}(U_{\bsym{k}}) . \]

The restriction morphisms 
$\mrm{rest}^{}_{V / U}$ induce a morphism of crossed groupoids 
$\opn{C}^p(\bsym{U}, \twocat{P}) \to \opn{C}^q(\bsym{U}, \twocat{P})$
for any $\al : p \to q$ in $\bsym{\Delta}$. 
In this way we obtain a cosimplicial crossed groupoid 
$\opn{C}(\bsym{U}, \twocat{P}) = 
\{ \opn{C}^p(\bsym{U}, \twocat{P}) \}_{p \in \N}$,
which we refer to as the {\em \v{C}ech cosimplicial crossed groupoid}
associated to $\twocat{P}$ and $\bsym{U}$. 
\end{dfn}

The set of combinatorial descent data 
$\opn{Desc}(G)$ in a cosimplicial crossed groupoid $G$ 
was defined in Definition \ref{dfn:101}.

\begin{dfn} \label{dfn:21}
Let $\twocat{P}$ be a stack of crossed groupoids on a
topological space $X$, and let $\bsym{U} = \{ U_k \}_{k \in K}$ be an
open covering of $X$. A {\em geometric descent datum} for 
$(\bsym{U}, \twocat{P})$ is an element of the set 
$\opn{Desc}(\opn{C}(\bsym{U}, \twocat{P}))$.

Given $\bsym{d}, \bsym{d}' \in \opn{Desc}(\opn{C}(\bsym{U}, \twocat{P}))$,
a {\em gauge transformation} 
$\bsym{f} : \bsym{d} \to \bsym{d}'$ is a gauge transformation
of combinatorial descent data, in the sense of Definition \ref{dfn:100}.
Passing to gauge equivalence classes we get the set
$\ol{\opn{Desc}}(\opn{C}(\bsym{U}, \twocat{P}))$.
\end{dfn}

Here is an explicit interpretation of geometric descent data,
gotten by unraveling the definitions. A descent datum 
$\bsym{d} \in \opn{Desc}(\opn{C}(\bsym{U}, \twocat{P}))$ 
is actually a collection 
\begin{equation} \label{eqn:mdd.120}
\bsym{d} = \bigl( \{ \mcal{A}_{k_0} \}_{k_0 \in K}, \,
\{ g_{k_0, k_1} \}_{k_0, k_1 \in K}, \,
\{ a_{k_0, k_1, k_2} \}_{k_0, k_1, k_2 \in K} \bigr) ,
\end{equation}
where
$ \mcal{A}_{k_0} \in \opn{Ob} (\twocat{P}(U_{k_0}))$,
$g_{k_0, k_1}: \mcal{A}_{k_0}|_{U_{k_0, k_1}} \to 
\mcal{A}_{k_1}|_{U_{k_0, k_1}}$
is an isomorphism in $\twocat{P}_1(U_{k_0, k_1})$, and
$a_{k_0, k_1, k_2} \in 
\Gamma \bigl( U_{k_0, k_1, k_2}, \opn{IG}(\mcal{A}_{k_0}) \bigr)$.
Conditions (i-ii) of Definition \ref{dfn:101} say that
\begin{equation} \label{eqn:bitorsors.11}
 g_{k_0, k_2}^{-1} \circ g_{k_1, k_2} \circ g_{k_0, k_1} =
\opn{ig}(a_{k_0, k_1, k_2})
\end{equation}
as automorphisms of
$\mcal{A}_{k_0}|_{U_{k_0, k_1, k_2}}$
in $\twocat{P}_1(U_{k_0, k_1, k_2})$, and 
\begin{equation} \label{eqn:bitorsors.12}
a_{k_0, k_1, k_3}^{-1} \cdot a_{k_0, k_2, k_3} \cdot 
a_{k_0, k_1, k_2} = \opn{IG}(g_{k_0, k_1}^{-1})
(a_{k_1, k_2, k_3})
\end{equation}
in the group
$\Gamma \bigl( U_{k_0, \ldots, k_3}, \opn{IG}(\mcal{A}_{k_0})
\bigr)$.
See Figure \ref{fig:5} for an illustration. 

\begin{figure}
\begin{center}
\includegraphics[scale=0.35]{fig-4.pdf}

\caption{Geometric descent datum on an open covering
$\{ U_k \}_{k \in K}$ of a topological space.}
\label{fig:5}
\end{center}
\end{figure}

Given another descent datum 
$\bsym{d}' = \bigl( \{ \mcal{A}'_{k_0} \}, \{ g'_{k_0, k_1} \},
\{ a'_{k_0, k_1, k_2} \} \bigr)$,
a gauge transformation 
$\bsym{f} : \bsym{d} \to \bsym{d}'$ 
is actually a collection 
\begin{equation} \label{eqn:bitorsors.14}
\bsym{f} = \bigl( \{ f_{k_0} \}, \{ b_{k_0, k_1} \} \bigr) ,
\end{equation}
where
$f_{k_0} : \mcal{A}_{k_0} \to \mcal{A}'_{k_0}$
is an isomorphism in $\twocat{P}_1(U_{k_0})$, and
$b_{k_0, k_1} \in \lb \Gamma(U_{k_0, k_1}, \opn{IG}(\mcal{A}_{k_0}))$.
Conditions (i-ii) of Definition \ref{dfn:100} say that  
\begin{equation} \label{eqn:bitorsors.6}
g'_{k_0, k_1} =  f_{k_1} \circ g_{k_0, k_1} \circ \opn{ig}(b_{k_0, k_1})
\circ f_{k_0}^{-1}
\end{equation}
as isomorphisms 
$\mcal{A}'_{k_0}|_{U_{k_0, k_1}} \to \mcal{A}'_{k_1}|_{U_{k_0, k_1}}$,
and 
\begin{equation} \label{eqn:bitorsors.7}
a'_{k_0, k_1, k_2} = \opn{IG}(f_{k_0}) \bigl(  
b_{k_0, k_2}^{-1} \cdot a_{k_0, k_1, k_2} \cdot 
\opn{IG}(g_{k_0, k_1}^{-1})(b_{k_1, k_2}) \cdot b_{k_0, k_1} \bigr)
\end{equation}
in the group $\opn{IG}(\mcal{A}'_{k_0}|_{U_{k_0, k_1, k_2}})$.

\begin{rem}
The similarity between our notion of geometric descent data and
the usual notion of descent data for gerbes (cf.\ \cite[Section IV.3.5]{Gi} or
\cite[Section 5]{Br}) is no coincidence. Indeed, as shown in Example
\ref{exa:21}, gerbes are an instance of twisted objects. Likewise for gauge
transformations between descent data.

In \cite{Ko2}, geometric descent data, for 
$\twocat{P} = \twocat{Assoc}(R, X)$, is called a {\em combinatorial
description of algebroids}.
Note that in the paper \cite{BGNT1} the authors refer to a
geometric descent datum as a ``stack''.
\end{rem}

\begin{dfn} \label{dfn:bitorsors.3}
Let $\gerbe{G}$ be a gerbe on $X$, and let 
$\bsym{U} = \{ U_k \}_{k \in K}$ be an open covering of $X$.  
A {\em trivialization datum} of $\gerbe{G}$ on $\bsym{U}$ is a collection 
$\bsym{s} = \bigl( \{ i_{k_0} \} , \{ s_{k_0, k_1} \} \bigr)$,
where $i_{k_0} \in \opn{Ob}(\gerbe{G}(U_{k_0}))$ and 
$s_{k_0, k_1} \in \gerbe{G}(U_{k_0, k_1})(i_{k_0}, i_{k_1})$.
\end{dfn}

Consider a twisted object
$(\gerbe{G}, \gerbe{A}, \opn{cp})$
of the stack of crossed groupoids $\twocat{P}$, 
and a trivialization datum 
$\bsym{s} = \bigl( \{ i_{k_0} \} , \{ s_{k_0, k_1} \} \bigr)$ 
of the gauge gerbe $\gerbe{G}$ on the open covering $\bsym{U}$. Define 
\begin{equation}
\begin{aligned}
\mcal{A}_{k_0} & := \gerbe{A}(i_{k_0}) \in \opn{Ob}(\twocat{P}(U_{k_0})) , 
\\
g_{k_0, k_1} & := \gerbe{A}(s_{k_0, k_1}) \in 
\twocat{P}_1(U_{k_0, k_1})(i_{k_0}, i_{k_1}) , 
\\
a_{k_0, k_1, k_2} & := \opn{cp} ( s_{k_0, k_2}^{-1} \circ s_{k_1, k_2} \circ
s_{k_0, k_1} ) \in \Gamma(U_{k_0, k_1, k_2}, \opn{IG}(\mcal{A}_{k_0})) . 
\end{aligned}
\end{equation}
The resulting collection of elements, arranged as in (\ref{eqn:mdd.120}),
is denoted by $\opn{dec}(\gerbe{A}, \bsym{s})$.

\begin{lem}   \label{lem:bitorsors.2}
Let $(\gerbe{G}, \gerbe{A}, \opn{cp})$ be a twisted object of $\twocat{P}$,
and let $\bsym{s}$ be a trivialization datum for $\gerbe{G}$ on $\bsym{U}$.
\begin{enumerate}
\item The collection $\opn{dec}(\gerbe{A}, \bsym{s})$ is a geometric descent
datum for $(\bsym{U}, \twocat{P})$. 

\item Let $(\gerbe{G}', \gerbe{A}', \opn{cp}')$ be another another twisted
object of $\twocat{P}$, which is twisted gauge equivalent to 
$(\gerbe{G}, \gerbe{A}, \opn{cp})$, 
and let $\bsym{s}'$ be a trivialization datum for $\gerbe{G}'$ on $\bsym{U}$.
Assume that the groupoids 
$\gerbe{G}(U_k)$ are connected for all $k \in K$. Then 
the descent data $\opn{dec}(\gerbe{A}, \bsym{s})$ and 
$\opn{dec}(\gerbe{A}', \bsym{s}')$ are gauge equivalent.
\end{enumerate}
\end{lem}

\begin{proof}
(1) This is a simple calculation.

\medskip \noindent
(2) First assume that 
$(\gerbe{G}', \gerbe{A}', \opn{cp}') = 
(\gerbe{G}, \gerbe{A}, \opn{cp})$, 
but 
$\bsym{s}' = \bigl( \{ i'_{k_0} \} , \{ s'_{k_0, k_1} \} \bigr)$ 
is a different descent datum. Since the groupoids 
$\gerbe{G}(U_k)$ are connected, we can find elements 
$t_k \in \gerbe{G}(U_k)(i_k, i'_k)$. 
Define $f_k := \gerbe{A}(t_k)$, which is an isomorphism 
$\mcal{A}_k \to \mcal{A}'_k$ in $\twocat{P}_1$, 
and
\[ b_{k_0, k_1} := \opn{cp}( s_{k_0, k_1}^{-1}  \circ 
t_{k_1}^{-1}  \circ s'_{k_0, k_1}  \circ t_{k_0} ) \in 
\Gamma(U_{k_0, k_1}, \opn{IG}(\mcal{A}_{k_0})) . \]
A calculation shows that the collection $\bsym{f}$, with notation as in 
(\ref{eqn:bitorsors.14}), is a gauge transformation 
$\opn{dec}(\gerbe{A}, \bsym{s}) \to \opn{dec}(\gerbe{A}', \bsym{s}')$.

Now consider a twisted gauge transformation 
$(\Phi_{\mrm{gau}}, \Phi_{\mrm{rep}}) : 
(\gerbe{G}, \gerbe{A}, \opn{cp}) \to \lb (\gerbe{G}', \gerbe{A}', \opn{cp}')$.
Since $\Phi_{\mrm{gau}} : \gerbe{G} \to \gerbe{G}'$
is an equivalence of gerbes, it follows that the groupoids 
$\gerbe{G}'(U_k)$ are all connected. So, by the previous paragraph, we don't
care which trivialization datum we use for $\gerbe{G}'$.
Let us define $\bsym{s}'$ to be 
$i'_k := \Phi_{\mrm{gau}}(i_k)$ and 
$s'_{k_0, k_1} :=  \Phi_{\mrm{gau}}(s_{k_0, k_1})$. 
Take 
$f_k := \Phi_{\mrm{rep}} : \mcal{A}_{k} \to \mcal{A}'_{k}$
and $b_{k_0, k_1} := 1$. 
The resulting collection $\bsym{f}$ is a gauge transformation 
$\opn{dec}(\gerbe{A}, \bsym{s}) \to \opn{dec}(\gerbe{A}', \bsym{s}')$.
\end{proof}

\begin{dfn} \label{dfn:18}
Let $\gerbe{G}$ be a gerbe on a topological space $X$, and let 
$\bsym{U} = \{ U_k \}_{k \in K}$ be an open covering of $X$. We say
that $\bsym{U}$ {\em totally trivializes} $\gerbe{G}$ if 
for every $p \in \{ 0, 1 \}$ and $\bsym{k} \in \bsym{\Delta}_p(K)$ the 
groupoid $\gerbe{G}(U_{\bsym{k}})$ is nonempty and connected.
\end{dfn}

\begin{dfn} \label{dfn:bitorsors.10}
Let $\twocat{P}$ be a stack of crossed groupoids on a topological space $X$,
and let $\bsym{U}$ be an open covering of $X$. 
\begin{enumerate}
\item Let $(\gerbe{G}, \gerbe{A}, \opn{cp})$ be a twisted
object of $\twocat{P}$. We say that $\bsym{U}$ totally trivializes
$(\gerbe{G}, \gerbe{A}, \opn{cp})$ if it totally trivializes the gauge gerbe
$\gerbe{G}$.

\item We say that $\bsym{U}$ totally trivializes 
$\twocat{P}$ if it totally trivializes all twisted objects of $\twocat{P}$.
\end{enumerate}
\end{dfn}

\begin{rem}
In general there is no reason to expect that totally trivializing open
coverings should exist. If we were to work with hypercoverings,
then such a difficulty would not arise; but then the combinatorics would be
more complicated. Cf.\ \cite[Section 5]{Br}.

We shall see in Corollary \ref{cor:4}  that for
the stacks with inner gauge groups \lb
$\twocat{AssDef}(R,\mcal{O}_X)$ and $\twocat{PoisDef}(R, \mcal{O}_X)$
there do exist totally trivializing open coverings.
\end{rem}

\begin{prop} \label{prop:bitorsors.5}
Let $\bsym{U}$ be an open covering of $X$ that totally trivializes 
the stack of crossed groupoids $\twocat{P}$. Then  there is a function 
\[ \ol{\opn{dec}} :  \ol{\opn{TwOb}}(\twocat{P}) \to 
\ol{\opn{Desc}}(\opn{C}(\bsym{U}, \twocat{P})) \]
called {\em decomposition}, 
which is represented by $\opn{dec}(\gerbe{A}, \bsym{s})$
for any representative $\gerbe{A} \in \opn{TwOb}(\twocat{P})$ 
and any trivialization datum $\bsym{s}$ for $\gerbe{A}$ on $\bsym{U}$.
\end{prop}

\begin{proof}
Take any twisted object $(\gerbe{G}, \gerbe{A}, \opn{cp})$. 
Since the groupoids $\gerbe{G}(U_{k_0})$ are \lb nonempty, and
the groupoids $\gerbe{G}(U_{k_0, k_1})$ are connected, we can find 
a trivialization datum $\bsym{s}$. By Lemma \ref{lem:bitorsors.2}(1) we get 
a geometric descent datum $\opn{dec}(\gerbe{A}, \bsym{s})$.
Since the groupoids $\gerbe{G}(U_{k_0})$ are connected, 
by Lemma \ref{lem:bitorsors.2}(2) this gives a well-defined function on
equivalence classes.
\end{proof}

Recall that a refinement of  $\bsym{U}$ is an open covering 
$\bsym{U}' = \{ U'_k \}_{k \in K'}$ of $X$, together with a function
$\rho : K' \to K$, such that 
$U'_k \subset U_{\rho(k)}$ for every $k \in K'$.
Sometimes we say that $\rho : \bsym{U}' \to \bsym{U}$ is a
refinement. Given such a refinement, there is a function
\begin{equation} \label{eqn:23}
\rho^* : \opn{Desc}(\opn{C}(\bsym{U}, \twocat{P}))
\to \opn{Desc}(\opn{C}(\bsym{U}', \twocat{P})) . 
\end{equation}
The formula is obvious: say 
$\bsym{d} = \bigl( \{ \mcal{A}_k \}_{k \in K}, \ldots \bigr)$;
then 
$\rho^*(\bsym{d}) = \bigl( \{ \mcal{A}'_k \}_{k \in K'}, \ldots
\bigr)$, 
where $\mcal{A}'_{k} := \mcal{A}_{\rho(k)}|_{U'_k}$, etc. 
It is easy to see that this function preserves the equivalence
relation.
Thus $\ol{\opn{Desc}}(\opn{C}(\bsym{U}, \twocat{P}))$ is
contravariant with respect
to refinements $\bsym{U}' \to \bsym{U}$.

\begin{prop} \label{prop:bitorsors.6}
Let $\bsym{U}$ and $\bsym{U}'$ be open coverings of $X$ that totally
trivialize the stack of crossed groupoids $\twocat{P}$, and let 
$\rho : \bsym{U} \to \bsym{U}'$ be a refinement. 
Then the diagram 
\[ \UseTips \xymatrix @C=9ex @R=5ex {
\ol{\opn{TwOb}}(\twocat{P})
\ar[r]^(0.4){\ol{\opn{dec}}}
\ar[dr]_{\ol{\opn{dec}}}
&
\ol{\opn{Desc}}(\opn{C}(\bsym{U}, \twocat{P}))
\ar[d]^{\rho^*} 
\\
&
\ol{\opn{Desc}}(\opn{C}(\bsym{U}', \twocat{P})) 
} \]
is commutative.
\end{prop}

\begin{proof}
This is immediate from the construction; cf.\ proof of Lemma
\ref{lem:bitorsors.2}(2).
\end{proof}

In the rest of this section we will show how to glue twisted objects from
descent data. This construction will be inverse to the decomposition operation.
But before attempting to glue twisted objects, we have to
understand how to pass from descent data to connected groupoids. 

Let $K$ be some nonempty set. By {\em groupoid descent datum} indexed by $K$
we mean a collection 
$\bsym{d} = \bigl( \{ G_{k_0} \}, \{ \phi_{k_0, k_1} \},
\{ a_{k_0, k_1, k_2} \} \bigr)$, 
where $k_0, k_1, k_2 \in K$, $G_{k_0}$ is a group,
$\phi_{k_0, k_1} : G_{k_0} \to G_{k_1}$ is a group isomorphism, and
$a_{k_0, k_1, k_2} \in G_{k_0}$.
These satisfy conditions  (\ref{eqn:bitorsors.11})
and (\ref{eqn:bitorsors.12}), with the obvious modifications in notation (e.g.\
$\phi_{k_0, k_1}$ instead of $g_{k_0, k_1}$). 

Suppose $\bsym{d}$ and $\bsym{d}'$ are groupoid descent data indexed by $K$. 
A gauge transformation $\bsym{f} : \bsym{d} \to \bsym{d}'$ is a 
collection 
$\bsym{f} = \bigl( \{ \psi_{k_0} \}, \{ b_{k_0, k_1} \} \bigr)$
of group isomorphisms $\psi_{k_0} : G_{k_0} \to G'_{k_1}$, and of
elements $b_{k_0, k_1} \in G_{k_0}$. The conditions are the translations of
formulas (\ref{eqn:bitorsors.6}) and (\ref{eqn:bitorsors.7}) to the present
context.

A trivialization datum for a connected groupoid $G$ is a collection 
$\bsym{s} = \{  s_{k_0, k_1} \}$ of elements 
$s_{k_0, k_1} \in G(k_0, k_1)$,
indexed by the set $K := \opn{Ob}(G)$.
We call the pair $(G, \bsym{s})$ a trivialized groupoid. 
By isomorphism of trivialized groupoids 
$F : (G, \bsym{s}) \to (G', \bsym{s}')$
we mean an isomorphism of groupoids $F :G \to G'$
such that $F(s_{k_0, k_1}) = s'_{F(k_0), F(k_1)}$.
Just like in Lemma \ref{lem:bitorsors.2}(1), to any trivialized groupoid 
$(G, \bsym{s})$ there is a corresponding groupoid descent datum 
$\opn{dec}(G, \bsym{s})$.

\begin{lem} \label{lem:bitorsors.3}
Let $\bsym{d}$ be a groupoid descent datum indexed by a nonempty set $K$. 
\begin{enumerate}
\item There is a connected groupoid $G$, with 
trivialization datum $\bsym{s}$, such that 
$\opn{dec}(G, \bsym{s}) = \bsym{d}$.
The trivialized groupoid $(G, \bsym{s})$ is unique up to a unique
isomorphism. We write $\opn{glu}(\bsym{d}) := G$.

\item Let $\bsym{d}'$ be another groupoid descent datum indexed by
$K$, and let $\bsym{f} : \bsym{d} \to \bsym{d}'$ be a gauge
transformation. We describe $\bsym{f}$ as in \tup{(\ref{eqn:bitorsors.14})}.
Then there is a unique isomorphism of groupoids 
$\opn{glu}(\bsym{f}) : \opn{glu}(\bsym{d}) \to \opn{glu}(\bsym{d}')$ 
such that 
$\opn{glu}(\bsym{f})(s_{k_0, k_1} \cdot b_{k_0, k_1}) = s'_{k_0, k_1}$.
\end{enumerate}
\end{lem}

\begin{proof}
(1) This seems to be known (cf.\ \cite[Appendix A1]{Ko2}), but here is a sketch
anyhow. Write $\bsym{d}$ as in (\ref{eqn:mdd.120}).
For any $k_0, k_1 \in K$ we take $G(k_0, k_1)$ to be the 
$G_{k_1}$-$G_{k_0}$-bitorsor with basis 
$s_{k_0, k_1}$, such that 
$s_{k_0, k_1} \cdot a = \phi_{k_0, k_1}(a) \cdot s_{k_0, k_1}$
for any $a \in G_{k_0}$.
The composition $\circ$ in $G$ is specified by its value on the basis
elements:
\[ s_{k_1, k_2} \circ s_{k_0, k_1} := s_{k_0, k_2} \cdot a_{k_0, k_2, k_2} . \]

\medskip \noindent
(2) A direct calculation.
\end{proof}

\begin{lem}  \label{lem:bitorsors.9}
There is a function 
\[ \opn{glu} : \opn{Desc}(\opn{C}(\bsym{U}, \twocat{P})) \to 
\opn{TwOb}(\twocat{P}) \]
having these properties\tup{:}
\begin{enumerate}
\rmitem{i} If 
$\bsym{d}, \bsym{d}' \in \opn{Desc}(\opn{C}(\bsym{U}, \twocat{P}))$
are gauge equivalent, then $\opn{glu}(\bsym{d})$ and 
$\opn{glu}(\bsym{d}')$ are twisted gauge equivalent.

\rmitem{ii} For any $\bsym{d} \in \opn{Desc}(\opn{C}(\bsym{U}, \twocat{P}))$
the twisted object 
$(\gerbe{G}, \gerbe{A}, \opn{cp}) := \opn{glu}(\bsym{d})$ has a 
trivialization datum $\bsym{s}$ such that 
$\opn{dec}(\gerbe{A}, \bsym{s})= \bsym{d}$.

\rmitem{iii} Let $(\gerbe{G}, \gerbe{A}, \opn{cp})$
be a twisted object of $\twocat{P}$, with trivialization datum
$\bsym{s}$, and let $\bsym{d} := \opn{dec}(\gerbe{A}, \bsym{s})$.
Then $\opn{glu}(\bsym{d})$ is twisted gauge equivalent to 
$(\gerbe{G}, \gerbe{A}, \opn{cp})$.
\end{enumerate}
\end{lem}

\begin{proof}
Take any $\bsym{d} \in \opn{Desc}(\opn{C}(\bsym{U}, \twocat{P}))$, which we
describe as in (\ref{eqn:mdd.120}).
For a nonempty open set $V \subset X$ let 
$K(V) := \{ k \in K \mid V \subset U_k \}$. 
Consider the collection 
\[ \opn{IG}(\bsym{d}, V) := 
\bigl( \{ \Gamma(V, \opn{IG}(\mcal{A}_{k_0})) \}, 
\{ \opn{IG}(g_{k_0, k_1}) \}, \{ a_{k_0, k_1, k_2} \} \bigr) \]
in which $k_0, k_1, k_2 \in K(V)$. So $\opn{IG}(\bsym{d}, V)$ is a 
groupoid descent datum indexed by the set $K(V)$. 
If $K(V) \neq \emptyset$, then by Lemma \ref{lem:bitorsors.3}(1) there is a
nonempty connected groupoid 
$\gerbe{G}(V) := \opn{glu}(\opn{IG}(\bsym{d}, V))$.
If If $K(V) = \emptyset$ we let $\gerbe{G}(V)$ be the empty groupoid.
For $V = U_k$ there is a distinguished object $k \in \opn{Ob}(\gerbe{G}(U_k))$, 
and for $V = U_{k_0, k_1}$ there is a distinguished isomorphism 
$s_{k_0, k_1} : k_0 \to k_1$ in the groupoid $\gerbe{G}(U_{k_0, k_1})$.
Also there is a tautological group isomorphism 
$\opn{cp} : \gerbe{G}(V)(k_0, k_0) \to 
\Gamma(V, \opn{IG}(\mcal{A}_{k_0}))$
for  $k_0 \in K(V)$.

If $V' \subset V$ then $K(V) \subset K(V')$. 
By construction of the groupoids $\opn{glu}(-)$ there is an induced morphism
of groupoids $\gerbe{G}(V) \to \gerbe{G}(V')$, 
which on the automorphism groups of $k_0 \in K(V)$ it is the restriction
homomorphism
$\Gamma(V, \opn{IG}(\mcal{A}_{k_0})) \to \Gamma(V', \opn{IG}(\mcal{A}_{k_0}))$.
In this way we obtain a presheaf of groupoids $\gerbe{G}$ on $X$, which is a
separated prestack (the isomorphism presheaves are sheaves).
The group isomorphisms $\opn{cp}$ above induce an isomorphism of sheaves of
groups 
$\opn{cp} : \gerbe{G}(k_0, k_0) \to 
\opn{IG}(\mcal{A}_{k_0})$ on $U_{k_0}$.

Let $\til{\gerbe{G}}$ be the stackification of $\gerbe{G}$; so
$\til{\gerbe{G}}$ is a gerbe on $X$, and there is a weak equivalence of
prestacks $F : \gerbe{G} \to \til{\gerbe{G}}$. Note that $\til{\gerbe{G}}$
is equipped with a trivialization datum
$\bsym{s} = \bigl( \{ i_{k_0} \} , \{ s_{k_0, k_1} \} \bigr)$
on $\bsym{U}$,
where $i_{k_0} := F(k_0) \in \opn{Ob}(\til{\gerbe{G}}(U_{k_0}))$.

For any $V \subset X$ open there is a morphism of groupoids 
$\gerbe{A}(V) : \gerbe{G}(V) \to \twocat{P}_1(V)$,
namely $\gerbe{A}(V)(k_0) := \mcal{A}_{k_0}$ for 
$k_0 \in K(V) = \opn{Ob}(\gerbe{G}(V))$,
and
$\gerbe{A}(V)(s_{k_0, k_1} \cdot a) := 
g_{k_0, k_1} \circ \opn{ig}(a)$
for $a \in \gerbe{G}(V)(k_0, k_0) = \Gamma(V, \opn{IG}(\mcal{A}_{k_0}))$.
Note that $\opn{ig}(a)$ is an automorphism of $\mcal{A}_{k_0}|_V$,
and $g_{k_0, k_1} : \mcal{A}_{k_0}|_V \to \mcal{A}_{k_1}|_V$
is an isomorphism, all in the stack of groupoids $\twocat{P}_1$.
It is a direct calculation to check that $\gerbe{A}(V)$ respects compositions,
so it is indeed a morphism of groupoids. 
As $V$ varies we get a morphism of prestacks 
$\gerbe{A} : \gerbe{G} \to \twocat{P}_1$. 
This induces a morphism of stacks 
$\til{\gerbe{A}\, \, } \! \! : \til{\gerbe{G}} \to \twocat{P}_1$.

Take a local object $i$ of $\til{\gerbe{G}}$ which is not a local object of 
$\gerbe{G}$. This new local object $i$ is created by gluing a collection of
local objects of $\gerbe{G}$ using local isomorphisms in $\gerbe{G}$. 
The same gluing operation also 
determines an isomorphism of sheaves of groups 
$\til{\opn{cp}} : \til{\gerbe{G}}(i, i) \to 
\opn{IG}( \til{\gerbe{A}\, \, } \!  (i))$. 
We thus get a twisted object
$\opn{glu}(\bsym{d}) = 
(\til{\gerbe{G}}, \til{\gerbe{A}\, \, } \! ,  \til{\opn{cp}})$.
By construction we see that the descent datum
$\opn{dec}(\opn{glu}(\bsym{d}), \bsym{s})$ equals $\bsym{d}$, so property (ii)
holds.

Suppose $\bsym{d}'$ is another normalized descent datum, and 
$\bsym{f} : \bsym{d} \to \bsym{d}'$ is a gauge transformation, described like
in (\ref{eqn:bitorsors.14}). Let's write 
$\opn{glu}(\bsym{d}') = (\til{\gerbe{G}}', {\til{\gerbe{A}\, \, } \! }', 
\til{\opn{cp}}')$.
Lemma \ref{lem:bitorsors.3}(2) implies that for every open set $V$ there's an
induced isomorphism of group\-oids 
$\gerbe{G}(V) \to \gerbe{G}'(V)$. Hence we get an equivalence of prestacks of
groupoids 
$\Phi_{\mrm{gau}} : \gerbe{G} \to \gerbe{G}'$.
Next there is an isomorphism 
$\Phi_{\mrm{rep}} : \gerbe{A} \to \gerbe{A}' \circ \Phi_{\mrm{gau}}$
of functors of prestacks $\gerbe{G} \to \gerbe{G}'$, which for an index
$k_0 \in K$ is
$\Phi_{\mrm{rep}} := f_{k_0} : \mcal{A}_{k_0} \to \mcal{A}'_{k_0}$. 
The stackification extends these to an equivalence of gerbes  
$\Phi_{\mrm{gau}} : \til{\gerbe{G}} \to \til{\gerbe{G}}'$
and an isomorphism of functors of stacks
$\Phi_{\mrm{rep}} : \til{\gerbe{A}\, \, } \! \! \to 
{\til{\gerbe{A}\, \, } \! \! }' \circ \Phi_{\mrm{gau}}$.
We obtain a twisted gauge equivalence 
$(\Phi_{\mrm{gau}}, \Phi_{\mrm{rep}}) : \opn{glu}(\bsym{d}) \to
\opn{glu}(\bsym{d}')$
between these twisted objects; so property (i) holds.
 
Finally take any twisted object $(\gerbe{G}, \gerbe{A}, \opn{cp})$ of 
$\twocat{P}$ and a trivialization datum $\bsym{s}$.
The step-by-step construction of 
$\opn{glu}(\bsym{d}) = 
(\til{\gerbe{G}}, \til{\gerbe{A}\, \, } \! , \til{\opn{cp}})$
shows that it is twisted gauge equivalent to  
$(\gerbe{G}, \gerbe{A}, \opn{cp})$. We see that property (iii) holds.
\end{proof}

\begin{thm}[Decomposition] \label{thm:glu.1}
Let $X$ be a topological space, $\bsym{U}$ an open covering of $X$,
and $\twocat{P}$ a stack of crossed groupoids on $X$. 
Assume that $\bsym{U}$ totally trivializes $\twocat{P}$. Then the
function 
\[ \ol{\opn{dec}} :  \ol{\opn{TwOb}}(\twocat{P}) \to 
\ol{\opn{Desc}}(\opn{C}(\bsym{U}, \twocat{P}))  \]
from Proposition \tup{\ref{prop:bitorsors.5}} is bijective.
\end{thm}

\begin{proof}
By property (i) Lemma \ref{lem:bitorsors.9} there is a
well-defined function 
\[ \ol{\opn{glu}} :  \ol{\opn{Desc}}(\opn{C}(\bsym{U}, \twocat{P})) \to 
\ol{\opn{TwOb}}(\twocat{P}) . \]
Properties (ii-iii) of the lemma say that $\ol{\opn{glu}}$ is the 
inverse of $\ol{\opn{dec}}$.
\end{proof}

We end this section with a simple example.

\begin{exa} \label{exa:19}
Let $\mcal{A}_0 \in \opn{Ob}(\twocat{P}(X))$. Consider the open covering
$\bsym{U} = \{ U_0 \}$, with $U_0 := X$. 
Take $g_{0,0} := \bsym{1}$ and $a_{0,0,0} := 1$.
Then 
$\bigl( \{ \mcal{A}_0 \}, \{ g_{0,0} \}, \{ a_{0,0,0} \} \bigr)$
is a geometric descent datum. {}From Theorem \ref{thm:glu.1} we get a twisted
object $\gerbe{A}$,
and  $\mcal{A}_0$ is a global object of $\gerbe{A}$. We refer to $\gerbe{A}$
as the twisted object generated by $\mcal{A}_0$.
Conversely, any twisted object $\gerbe{A}$ which is not really twisted
arises in this way (up to twisted gauge equivalence). 
\end{exa}
