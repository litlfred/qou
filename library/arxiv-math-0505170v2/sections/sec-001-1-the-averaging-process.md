---
doc_id: arxiv-math-0505170v2
doc_title: "AN AVERAGING PROCESS FOR UNIPOTENT GROUP ACTIONS"
section_id: sec-001-1-the-averaging-process
section_title: "The Averaging Process"
section_number: 1
pages: 2-8
source_pdf: math0505170.pdf
source_sha256: 0846b74f9c7c55cb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.785
doc_brief: "AN AVERAGING PROCESS FOR UNIPOTENT GROUP ACTIONS — We present an averaging process for sections of a torsor under a unipotent group."
---
\label{sec1}

Throughout the paper $\K$ denotes a fixed base field of 
characteristic $0$. All schemes and all morphisms are over $\K$.

We begin by recalling some standard facts about the combinatorics
of simplicial objects. 
Let $\bsym{\Delta}$ denote the category with objects the ordered 
sets $[q] := \{ 0, 1, \ldots, q \}$, $q \in \mbb{N}$. The 
morphisms $[p] \to [q]$ are the order preserving functions,
and we write
$\bsym{\Delta}^q_p := \opn{Hom}_{\bsym{\Delta}}([p], [q])$. 
The $i$-th co-face map 
$\partial^i : [p] \to [p + 1]$
is the injective function that does not take the value $i$;
and the $i$-th co-degeneracy map
$\mrm{s}^i : [p] \to [p - 1]$
is the surjective function that takes the value $i$ twice.
All morphisms in $\bsym{\Delta}$ are compositions of various 
$\partial^i$ and $\mrm{s}^i$. 

An element of $\bsym{\Delta}^q_p$ may be thought of as a sequence
$\bsym{i} = (i_0, \ldots, i_p)$ of integers with
$0 \leq i_0 \leq \cdots \leq i_p \leq q$. 
Given $\bsym{i} \in \bsym{\Delta}^m_q$, 
$\bsym{j} \in \bsym{\Delta}_m^p$ and
$\alpha \in \bsym{\Delta}^q_p$, 
we sometimes write 
$\alpha_*(\bsym{i}) := \bsym{i} \circ \alpha \in \bsym{\Delta}^m_p$ 
and 
$\alpha^*(\bsym{j}) := \alpha  \circ\bsym{j} \in 
\bsym{\Delta}_m^q$.

Let $\cat{C}$ be some category. A {\em cosimplicial object} in 
$\cat{C}$ is a functor $C : \bsym{\Delta} \to \cat{C}$.
We shall usually refer to the cosimplicial object as
$C = \set{C^p}_{p \in \mbb{N}}$,
and for any $\alpha \in \bsym{\Delta}_p^q$ the corresponding 
morphism in $\cat{C}$ will be denoted by 
$\alpha^* : C^p \to C^q$.
A {\em simplicial object} in 
$\cat{C}$ is a functor $C : \bsym{\Delta}^{\mrm{op}} \to \cat{C}$.
The notation for a simplicial object
will be $C = \set{C_p}_{p \in \mbb{N}}$ and
$\alpha_* : C_q \to C_p$.

An important example is the cosimplicial scheme 
$\{ \bsym{\Delta}^p_{\K} \}_{p \in \mbb{N}}$.
The morphisms are defined as follows. 
For any $p$ we identify the ordered set 
$[p]$ with the set of vertices of $\bsym{\Delta}^p_{\K}$. 
Given $\alpha \in \bsym{\Delta}^q_{p}$ the morphism
$\alpha^* : \bsym{\Delta}^p_{\K} \to \bsym{\Delta}^q_{\K}$
is then the unique linear morphism extending 
$\alpha : [p] \to [q]$. 

Let $G$ be a unipotent (affine finite type)
algebraic group over $\K$, with 
(nilpotent) Lie algebra $\mfrak{g}$. We write $d(G)$ for the minimal 
number $d$ such that there exists a chain of closed normal subgroups
$G = G_0 \supset G_1 \cdots \supset G_d = 1$
with $G_k / G_{k+1}$ abelian 
for all $k \in \{ 0, \ldots, d-1 \}$. The exponential map
$\opn{exp}_G : \mfrak{g} \to G$ is an isomorphism
of schemes, with inverse $\opn{log}_G$; see 
\cite[Theorem VIII.1.1]{Ho}.

Given a $\K$-scheme $X$ there is a Lie algebra 
$\mfrak{g} \times X$ (in the category of $X$-schemes), and a 
group-scheme $G \times X$. There is also an induced exponential 
map
\[ \opn{exp}_{G \times X} :=
\opn{exp}_G \times \bsym{1}_X  : 
\mfrak{g} \times X \to G \times X . \] 
We will need the following result. 

\begin{lem} \label{lem1.1}
Let $G, G'$ be two unipotent groups, with Lie algebras
$\mfrak{g}, \mfrak{g}'$. Let $X, X'$ be schemes, let 
$X \to X'$ be a morphism of schemes, and let
$\phi : G \times X \to G' \times X'$ be a morphism of 
group-schemes over $X'$. Denote by 
$\mrm{d} \phi : \mfrak{g} \times X \to \mfrak{g}' \times X'$
the induced Lie algebra morphism \tup{(}the differential of 
$\phi$\tup{)}. Then the diagram
\begin{equation} \label{eqn1.6}
\begin{CD}
\mfrak{g} \times X @>{\opn{exp}_{G \times X}}>> G \times X \\
@V{\mrm{d} \phi}VV @V{\phi}VV \\
\mfrak{g}' \times X' @>{\opn{exp}_{G' \times X'}}>> G' \times X'
\end{CD} 
\end{equation}
commutes.
\end{lem}

\begin{proof}
For the case $X = X' = \opn{Spec} \K$ this is contained in the 
proof of \cite[Theorem VIII.1.2]{Ho}.

In order to handle the general case we first recall the 
Campbell-Baker-Hausdorff formula:
\[ \opn{exp}_{G}(\gamma_1) \cdot \opn{exp}_{G}(\gamma_2) =
\opn{exp}_{G}(F(\gamma_1, \gamma_2)) , \]
where 
\[ F(\gamma_1, \gamma_2) = \gamma_1 + \gamma_2 + 
\smfrac{1}{2} [\gamma_1, \gamma_2] + \cdots \]
is a universal power series (see \cite[Section XVI.2]{Ho}).
Hence if we define 
$\gamma_1 * \gamma_2 := F(\gamma_1, \gamma_2)$,
then $(\mfrak{g}, *)$ becomes an algebraic group (with unit 
element $0$), and 
$\opn{exp}_{G} : (\mfrak{g}, *) \to (G, \cdot)$
is a group isomorphism. In this way we may eliminate $G$ 
altogether, and just look at the scheme $\mfrak{g}$ with its two 
structures: a Lie algebra and a group-scheme. Note that now
$\mfrak{g}$ is its own Lie algebra, as can be seen from the $2$-nd 
order term in the series $F(\gamma_1, \gamma_2)$. 

Consider a morphism 
$\phi : \mfrak{g} \times X \to \mfrak{g}' \times X'$
of $X'$-schemes. Then $\phi$ is a morphism of Lie algebras over 
$X'$ iff it is a morphism of group-schemes (for the 
multiplications $*$). And moreover $\mrm{d} \phi = \phi$. 
Therefore the diagram (\ref{eqn1.6}) is commutative.
\end{proof}

From now on we shall write $\opn{exp}_{G}$ instead of
$\opn{exp}_{G \times X}$, for the sake of brevity.

Consider the following setup: $X$ is a $\K$-scheme, 
and $Y, Z$ are two $X$-schemes.
Suppose $Z$ is a torsor under the group scheme $G \times X$. 
We denote the action of $G$ 
on $Z$ by $(g, z) \mapsto g \cdot z$.

Let $f_0, \ldots, f_q : \bsym{\Delta}^q_{\K} \times Y \to Z$ 
be $X$-morphisms. 
We are going to define a new sequence of $X$-morphisms 
$f'_0, \ldots, f'_q : \bsym{\Delta}^q_{\K} \times Y \to Z$.
Because $Z$ is a torsor under $G \times X$, for any 
$i, j \in \set{0, \ldots, q}$ there exists a unique morphism
$g_{i, j} : \bsym{\Delta}^q_{\K} \times Y \to G$ 
such that $f_j(w, y) = g_{i, j}(w, y) \cdot f_i(w, y)$
for all points $w \in \bsym{\Delta}^q_{\K}$ and 
$y \in Y$. Here $w$ and $y$ are scheme-theoretic points,
i.e.\ 
$w \in \bsym{\Delta}^q_{\K}(U) = 
\opn{Hom}_{\K}(U, \bsym{\Delta}^q_{\K})$ 
and 
$y \in Y(U) = \opn{Hom}_{\K}(U, Y)$ 
for some $\K$-scheme $U$. Define
\begin{equation} \label{eqn6.X1}
f'_i(w, y) := \opn{exp}_G \Big( \sum_{j=0}^q t_j(w) \cdot
\opn{log}_G(g_{i, j}(w, y)) \Big) \cdot f_i(w, y) . 
\end{equation}
In this formula we view $t_j$ as a morphism 
$t_j : \bsym{\Delta}^q_{\K} \to \mbf{A}^1_{\K}$,
and we use the fact that $\mfrak{g}$ is a vector space
(in the category of $\K$-schemes).

For any set $S$ let us write 
$S^{\bsym{\Delta}^q_{0}}$ for the set of functions 
$\bsym{\Delta}^q_{0} \to S$, which is the same as the set of
sequences $(s_0, \ldots, s_q)$ in $S$. As usual 
$\opn{Hom}_X(\bsym{\Delta}^q_{\K} \times Y, Z)$
is the set of $X$-morphisms $\bsym{\Delta}^q_{\K} \times Y \to Z$. 
In this notation the sequences
$(f_0, \ldots, f_q)$ and $(f'_0, \ldots, f'_q)$ are
elements of 
$\opn{Hom}_X(\bsym{\Delta}^q_{\K} \times Y, Z)
^{\bsym{\Delta}^q_{0}}$. We denote by
\[ \opn{wsym}_G : \opn{Hom}_X(\bsym{\Delta}^q_{\K} \times Y, Z)
^{\bsym{\Delta}^q_{0}} \to
\opn{Hom}_X(\bsym{\Delta}^q_{\K} \times Y, Z)
^{\bsym{\Delta}^q_{0}} \]
the operation
$(f_0, \ldots, f_q) \mapsto (f'_0, \ldots, f'_q)$
given by the formula (\ref{eqn6.X1}). 

We will also need a similar operation
\[ \opn{w}_G : \opn{Hom}_X(Y, Z)^{\bsym{\Delta}^q_{0}} \to
\opn{Hom}_X(\bsym{\Delta}^q_{\K} \times Y, Z)
^{\bsym{\Delta}^q_{0}} , \]
defined by
\[ \opn{w}_G(f_0, \ldots, f_q) := (f'_0, \ldots, f'_q) \]
with
\begin{equation} \label{eqn1.3}
f'_i(w, y) := \opn{exp}_G \Big( \sum_{j=0}^q t_j(w) \cdot
\opn{log}_G(g_{i, j}(y)) \Big) \cdot f_i(y) .
\end{equation}

It is clear that for $q = 0$ both operations 
$\opn{w}_G$ and $\opn{wsym}_G$ act as the identity, i.e.\ 
$\opn{w}_G(f_0) = \opn{wsym}_G(f_0) = f_0$
for all $f_0 \in \opn{Hom}_X(Y, Z)$.
Both operations $\opn{w}_G$ and $\opn{wsym}_G$ are symmetric, 
namely they are equivariant for the simultaneous action of the 
permutation group of $\{ 0, \ldots, q \}$ on 
$\bsym{\Delta}^q_{0}$ and $\bsym{\Delta}^q_{\K}$.
Also if 
$\bsym{f} = (f_0, \ldots, f_q) \in 
\opn{Hom}_X(\bsym{\Delta}^q_{\K} \times Y, Z)
^{\bsym{\Delta}^q_{0}}$
is a constant sequence, i.e.\ $f_0 = \cdots = f_q$, then 
$\opn{wsym}_G(\bsym{f}) = \bsym{f}$.

\begin{lem} \label{lem6.X1}
Both operations $\opn{w}_G$ and $\opn{wsym}_G$ are simplicial.
Namely, given $\alpha \in \bsym{\Delta}^q_{p}$ the diagram
\[ \begin{CD}
\opn{Hom}_X(\bsym{\Delta}^q_{\K} \times Y, Z)
^{\bsym{\Delta}^q_{0}}
@>{\opn{wsym}_G}>>
\opn{Hom}_X(\bsym{\Delta}^q_{\K} \times Y, Z)
^{\bsym{\Delta}^q_{0}} \\
@V{\alpha_*}VV @V{\alpha_*}VV \\
\opn{Hom}_X(\bsym{\Delta}^p_{\K} \times Y, Z)
^{\bsym{\Delta}^p_{0}}
@>{\opn{wsym}_G}>>
\opn{Hom}_X(\bsym{\Delta}^p_{\K} \times Y, Z)
^{\bsym{\Delta}^p_{0}}
\end{CD} \]
is commutative, and likewise for $\opn{w}_G$.
\end{lem}

\begin{proof}
It suffices to consider $\alpha = \partial^i$ or 
$\alpha = \mrm{s}^i$. Since $\opn{wsym}_G$ is symmetric,
we may assume that 
$\alpha = \partial^q : [q-1] \to [q]$ or
$\alpha = \mrm{s}^q : [q+1] \to [q]$.
Fix a sequence
$\bsym{f} = (f_0, \ldots, f_q) \in 
\opn{Hom}_X(\bsym{\Delta}^q_{\K} \times Y, Z)
^{\bsym{\Delta}^q_{0}}$.
Let $g_{i,j} \in \opn{Hom}_{\K}(\bsym{\Delta}^q_{\K} \times Y, G)$
be such that
$f_{j} = g_{i,j} \cdot f_i$,
and let
$\bsym{f}' = (f'_0, \ldots, f'_q) :=  
\opn{wsym}_G(\bsym{f})$. 

First let's look at the case $\alpha = \partial^q$. 
Take $w \in \bsym{\Delta}^{q-1}_{\K}$ and
$y \in Y$, and let $v := \alpha^*(w) \in \bsym{\Delta}^q_{\K}$.
The coordinates of $v$ are
$t_j(v) = t_j(w)$ for $j \leq q-1$, and $t_q(v) = 0$.
Then for any $i$ the $i$-th term in the sequence
$\alpha_*(\bsym{f}')$, evaluated at $(w,y)$, equals
\begin{equation} \label{eqn6.X2}
\begin{aligned}
f'_i(v,y) & =
\opn{exp}_G \Big( \sum_{j=0}^q t_j(v) \cdot
\opn{log}_G(g_{i, j}(v, y)) \Big) \cdot f_i(v, y) \\
& = \opn{exp}_G \Big( \sum_{j=0}^{q-1} t_j(w) \cdot
\opn{log}_G(g_{i, j}(v, y)) \Big) \cdot f_i(v, y) .
\end{aligned}
\end{equation}
On the other hand, the $i$-th term of the 
sequence $\opn{wsym}_G(\alpha_*(\bsym{f}))$ is
\[ \begin{aligned}
& \opn{exp}_G \Big( \sum_{j=0}^{q-1} t_j(w) \cdot
\opn{log}_G( \alpha_*(g_{i, j})(w, y)) \Big) \cdot 
\alpha_*(f_i)(w, y) \\
& \qquad = \opn{exp}_G \Big( \sum_{j=0}^{q-1} t_j(w) \cdot
\opn{log}_G( g_{i, j}(v, y)) \Big) \cdot f_i(v, y) .
\end{aligned} \]
So indeed
$\alpha_* \circ \opn{wsym}_G = \opn{wsym}_G \circ\, \alpha_*$ in 
this case.

Next consider the case $\alpha = \mrm{s}^q$. Take
$w \in \bsym{\Delta}^{q+1}_{\K}$ and
$y \in Y$, and let $v := \alpha^*(w) \in \bsym{\Delta}^q_{\K}$.
The coordinates of $v$ are
$t_j(v) = t_j(w)$ for $j \leq q-1$, and 
$t_q(v) = t_q(w) + t_{q+1}(w)$.
For any $i \leq q$ the $i$-th term in the sequence 
$\alpha_*(\bsym{f})$, evaluated at $(w,y)$, is
$f'_i(v,y)$, which was calculated in (\ref{eqn6.X2}). 
The $(q+1)$-st term is also $f'_q(v,y)$.
On the other hand, 
for any $i \leq q$ the $i$-th term in the sequence 
$\opn{wsym}_G(\alpha_*(\bsym{f}'))$, evaluated at $(w,y)$, is
\[ z_i := \opn{exp}_G \Big( \sum_{j=0}^{q+1} t_j(w) \cdot
\opn{log}_G( \alpha_*(g_{i, j})(w, y)) \Big) \cdot 
\alpha_*(f_i)(w, y) . \]
But 
$t_q(w) + t_{q+1}(w) = t_q(v)$, 
$\alpha_*(g_{i,j})(w,y) = g_{i,j}(v,y)$ for $j \leq q$, and
\linebreak $\alpha_*(g_{i, q+1})(w, y) = g_{i, q}(v, y)$.
Therefore
\[ z_i = \opn{exp}_G \Big( \sum_{j=0}^{q} t_j(v) \cdot
\opn{log}_G( g_{i, j}(v, y)) \Big) \cdot f_i(v, y) . \]
For $i = q+1$ one has $z_{q+1} = z_q$. We conclude that 
$\alpha_* \circ \opn{wsym}_G = \opn{wsym}_G \circ\, \alpha_*$ in 
this case too.

The proof for $\opn{w}_G$ is the same.
\end{proof}

\begin{lem} \label{lem6.X2}
Both operations $\opn{w}_G$ and $\opn{wsym}_G$ are functorial in 
the data \linebreak $(G, X, Y, Z)$. Namely, given another such 
quadruple $(G', X', Y', Z')$, a morphism 
of schemes $X \to X'$, a morphism of schemes
$e : Y' \to Y$ over $X'$, a morphism of group-schemes 
$\phi : G \times X \to G' \times X'$ over $X'$, and a 
$G \times X$ -equivariant morphism of 
schemes $f : Z \to Z'$ over $X'$, the diagram
\[ \begin{CD}
\opn{Hom}_X(\bsym{\Delta}^q_{\K} \times Y, Z)
^{\bsym{\Delta}^q_{0}}
@>{\opn{wsym}_G}>>
\opn{Hom}_X(\bsym{\Delta}^q_{\K} \times Y, Z)
^{\bsym{\Delta}^q_{0}} \\
@V{(e, f)}VV @V{(e, f)}VV \\
\opn{Hom}_{X'}(\bsym{\Delta}^q_{\K} \times Y', Z')
^{\bsym{\Delta}^q_{0}}
@>{\opn{wsym}_{G'}}>>
\opn{Hom}_{X'}(\bsym{\Delta}^q_{\K} \times Y', Z')
^{\bsym{\Delta}^q_{0}} 
\end{CD} \]
is commutative, and likewise for $\opn{w}_G$.
\end{lem}

\begin{proof}
This is due to the functoriality of the exponential map, see Lemma 
\ref{lem1.1}.
\end{proof}

\begin{lem} \label{lem6.X3}
Assume $G$ is abelian. Then for any
$(f_0, \ldots, f_q) \in \opn{Hom}_X(\bsym{\Delta}^q_{\K} \times Y, Z)
^{\bsym{\Delta}^q_{0}}$
the sequence
$\opn{wsym}_{G}(f_0, \ldots, f_q)$ is constant. 
\end{lem}

\begin{proof}
In this case $\opn{exp} : \mfrak{g} \to G$ is an isomorphism of 
algebraic groups, where $\mfrak{g}$ is viewed as an additive 
group. So we may assume that $Z$ is a torsor under 
$\mfrak{g} \times X$. Let
$(f'_0, \ldots, f'_q) := \opn{wsym}_{G}(f_0, \ldots, f_q)$,
and let 
$\gamma_{i,j} : \bsym{\Delta}^q_{\K} \times Y \to \mfrak{g}$
be morphisms such that 
$f_j  = \gamma_{i, j} + f_i$. 
Take $(w, y) \in \bsym{\Delta}^q_{\K} \times Y$. Then 
\[ f'_i(w,y) = 
\Big( \sum_{j=0}^q t_j(w) \cdot \gamma_{i,j}(w,y) \Big)
+ f_i(w,y) \]
for any $i$. Because
$\gamma_{i,j} = - \gamma_{j,i} = \gamma_{0,j} - \gamma_{0,i}$,
$f_i = f_0 + \gamma_{0,i}$ and 
$\sum_{j=0}^q t_j(w) = 1$, 
it follows that
$f'_i(w,y) = f'_0(w,y)$.
\end{proof}

Let's write $\opn{wsym}_{G}^d$ for the $d$-th iteration of the 
operation $\opn{wsym}_{G}$.

\begin{lem} \label{lem6.X4}
For any
$\bsym{f} = (f_0, \ldots, f_q) 
\in \opn{Hom}_X(\bsym{\Delta}^q_{\K} \times Y, Z)
^{\bsym{\Delta}^q_{0}}$
the sequence $\opn{wsym}_{G}^{d(G)}(\bsym{f})$ is constant.
For any $d \geq d(G)$ one has
$\opn{wsym}_{G}^{d}(\bsym{f}) = \opn{wsym}_{G}^{d(G)}(\bsym{f})$.
\end{lem}

\begin{proof}
For any $k$, the orbit of 
$f_0 \in \opn{Hom}_X(\bsym{\Delta}^q_{\K} \times Y, Z)$ 
under the action of the group
$G_k(\bsym{\Delta}^q_{\K} \times Y)$ will be denoted by
$G_k(\bsym{\Delta}^q_{\K} \times Y) \cdot f_0$.
Let 
$(f'_0, \ldots, f'_q) := \opn{wsym}_{G}(f_0, \ldots, f_q)$.
We will prove that if
$f_1, \ldots, f_q \in G_k(\bsym{\Delta}^q_{\K} \times Y) \cdot 
f_0$
then 
$f'_1, \ldots, f'_q
\in G_{k+1}(\bsym{\Delta}^q_{\K} \times Y) \cdot f'_0$.
The assertions of the lemma will then follow. 

Let $\til{Y} = \til{X} :=  \bsym{\Delta}^q_{\K} \times Y$ and
$\til{Z} := \til{X} \times_X Z$. 
So $\til{Z}$ is a torsor under $G \times \til{X}$, and $f_0$
induces a morphism 
$\til{f}_0 \in \opn{Hom}_{\til{X}}(\til{Y}, \til{Z})$.
The morphism
$\tau : G \times \til{X} \to \til{Z}$, 
$(g, \til{x}) \mapsto g \cdot \til{f}_0(\til{x})$,
is an isomorphism of $\til{X}$-schemes. Define 
$\til{W} := \tau(G_k \times \til{X}) \subset \til{Z}$. 
Then $\til{W}$ 
is the ``geometric orbit'' of $\til{f}_0$ under 
$G_k \times \til{X}$; and in particular $\til{W}$ is a torsor under 
$G_k \times \til{X}$. By assumption 
$\til{f}_1, \ldots, \til{f}_q \in 
\opn{Hom}_{\til{X}}(\til{Y}, \til{W})$. 
Define
$(\til{f}'_0, \ldots, \til{f}'_q) :=
\opn{wsym}_{G_k}(\til{f}_0, \ldots, \til{f}_q)$.
By Lemma \ref{lem6.X2} it suffices to prove that 
$\til{f}'_1, \ldots, \til{f}'_q \in
G_{k+1}(\til{Y}) \cdot \til{f}'_0$.

Define $\bar{W} := \til{W} / G_{k+1}$. 
This is a torsor under the group scheme
$(G_k / G_{k+1}) \times \til{X}$. Let
$\bar{f}_0, \ldots, \bar{f}_q \in 
\opn{Hom}_{\til{X}}(\til{Y}, \bar{W})$
be the images of $(\til{f}_0, \ldots, \til{f}_q)$.
Because the group $G_k / G_{k+1}$ is abelian, Lemma \ref{lem6.X3} 
says that 
$\opn{wsym}_{G_k / G_{k+1}}(\bar{f}_0, \ldots, \bar{f}_q)$
is a constant sequence. 
Again using Lemma \ref{lem6.X2}, we see that in fact
$\til{f}'_1, \ldots, \til{f}'_q \in
G_{k+1}(\til{Y}) \cdot \til{f}'_0$.
\end{proof}

Given an $X$-scheme $Y$ the collections
$\bigl\{ \opn{Hom}_{X}(\bsym{\Delta}^q_{\K} 
\times Y, Z) \bigr\}_{q \in \mbb{N}}$ and \linebreak
$\bigl\{ \opn{Hom}_{X}(Y, Z)
^{\bsym{\Delta}^q_0} \bigr\}_{q \in \mbb{N}}$
are simplicial sets. For $q = 0$ there are equalities
\begin{equation} \label{eqn6.2}
\opn{Hom}_{X}(\bsym{\Delta}^0_{\K} \times Y, Z) = 
\opn{Hom}_{X}(Y, Z) 
= \opn{Hom}_{X}(Y, Z)^{\bsym{\Delta}^0_0} . 
\end{equation}

\begin{thm} \label{thm5.1}
Let $G$ be a unipotent algebraic group over 
$\K$, let $X$ be a $\K$-scheme, and let $Z \to X$ be a $G$-torsor 
over $X$. For any $X$-scheme $Y$ and natural number $q$ 
there is a function
\[ \opn{wav}_G : \opn{Hom}_X(Y, Z)^{\bsym{\Delta}^q_{0}} \to
\opn{Hom}_X(\bsym{\Delta}^q_{\K} \times Y, Z) \]
called the {\em weighted average}. The function $\opn{wav}_G$ 
enjoys the following properties.
\begin{enumerate}
\item Symmetric: $\opn{wav}_G$ is equivariant for the  
action of the permutation group of $\{ 0, \ldots, q \}$ on 
$\bsym{\Delta}^q_{0}$ and on $\bsym{\Delta}^q_{\K}$.

\item Simplicial: $\opn{wav}_G$ is a map of simplicial sets 
\[ \bigl\{ \opn{Hom}_{X}(Y, Z)
^{\bsym{\Delta}^q_0} \bigr\}_{q \in \mbb{N}}  \to
\bigl\{ \opn{Hom}_{X}(\bsym{\Delta}^q_{\K} 
\times Y, Z) \bigr\}_{q \in \mbb{N}} . \]

\item Functorial: given another such 
quadruple $(G', X', Y', Z')$, a morphism 
of schemes $X \to X'$, a morphism of $X'$-group-schemes 
$G \times X \to G' \times X'$,
a $G \times X$ -equivariant morphism of 
$X'$-schemes $f : Z \to Z'$ and a morphism of $X'$-schemes
$e : Y' \to Y$, the diagram
\[ \begin{CD}
\opn{Hom}_X(Y, Z)^{\bsym{\Delta}^q_{0}}
@>{\opn{wav}_G}>>
\opn{Hom}_X(\bsym{\Delta}^q_{\K} \times Y, Z) \\
@V{(e, f)}VV @V{(e, f)}VV \\
\opn{Hom}_{X'}(Y', Z')^{\bsym{\Delta}^q_{0}}
@>{\opn{wsym}_{G'}}>>
\opn{Hom}_{X'}(\bsym{\Delta}^q_{\K} \times Y', Z')
\end{CD} \]
is commutative.

\item If $q = 0$ then $\opn{wav}_G$ is the identity map of 
$\opn{Hom}_X(Y, Z)$.
\end{enumerate}
\end{thm}

\begin{proof}
Given a sequence
$\bsym{f} = 
(f_0, \ldots, f_q) \in \opn{Hom}_X(Y, Z)^{\bsym{\Delta}^q_{0}}$
define 
$\opn{wav}_G(\bsym{f}) := f' \in  
\opn{Hom}_X(\bsym{\Delta}^q_{\K} \times Y, Z)$
to be the morphism such that
\[ (\opn{wsym}^{d(G)}_G \circ \opn{w}_G)(f_0, \ldots, f_q) = 
(f', \ldots, f') ; \]
see Lemma \ref{lem6.X4}. Properties (1)-(4) follow from the 
corresponding properties of $\opn{w}_G$ and $\opn{wsym}_G$.
\end{proof}

\begin{proof}[Proof of Corollary \tup{\ref{cor0.1}}]
Take $X = Y := \opn{Spec} \K$ in Theorem \ref{thm5.1}, and 
consider the $G$-torsor $\ul{Z} := G$. 
Choose any base point $z \in Z$;
this defines an isomorphism of left $G(\K)$-sets 
$\ul{Z}(\K) \cong Z$.
The weight sequence $\bsym{w}$ can be considered as a 
$\K$-rational point of $\bsym{\Delta}^q_{\K}$, and we define
\[ \opn{wav}_{G, \bsym{w}}(\bsym{z}) :=
\opn{wav}_{G}(\bsym{z})(\bsym{w}) \in Z . \]
If we were to choose another base point $z' \in Z$ this would 
amount to applying an automorphism of the torsor $\ul{Z}$,
namely right multiplication by some element of $G(\K)$. Due to the 
functoriality of $\opn{wav}_{G}$ the point  
$\opn{wav}_{G, \bsym{w}}(\bsym{z})$ will be unchanged.

The properties of this set-theoretical
averaging process are now immediate consequences of 
the corresponding properties of the geometric average. 
\end{proof}

\begin{rem} \label{rem1.1}
Z. Reichstein observed that our averaging process provides a new 
proof (in characteristic $0$)
of the fact that a unipotent group $G$ is special, namely 
any $G$-torsor $Z$ over $\K$ has a $\K$-rational point. Let us 
explain the idea. 

Let $z_0 \in Z$ be some closed point. Choose a finite Galois 
extension $L$ of $\K$ containing the residue field 
$\bsym{k}(z_0)$. Let $\Gamma$ be the Galois group of $L$ over 
$\K$, which acts on the set $Z(L)$.
Let $z_0, \ldots, z_q \in Z(L)$ 
be the $\Gamma$-conjugates of $z_0$. The group $\Gamma$ acts on 
the sequence 
$\bsym{z} := (z_0, \ldots, z_q)$ by permutations. 
Thus the simultaneous action of $\Gamma$ on 
\[ Z(L)^{\bsym{\Delta}^q_{0}} = 
\opn{Hom}_{\opn{Spec} \K}(\opn{Spec} L, Z)^{\bsym{\Delta}^q_{0}} \]
fixes $\bsym{z}$.

We know that the operator $\mrm{wav}_G$ is symmetric. 
And functoriality says that the action of the Galois group 
on $\opn{Spec} L$ is also respected. 
Since $\bsym{z}$ is fixed by the simultaneous action of
$\Gamma$, so is $\opn{wav}_G(\bsym{z})$. 
Take the uniform weight sequence 
$\bsym{w} := (\frac{1}{q+1}, \ldots, \frac{1}{q+1})$
and define
$z' := \opn{wav}_G(\bsym{z})(\bsym{w}) \in Z(L)$.
Because $\bsym{w}$ is fixed by the permutation group we conclude 
that $z'$ is $\Gamma$-invariant, and hence $z' \in Z(\K)$.
\end{rem}

\begin{rem}
Theorem \ref{thm5.1} has a rather obvious parallel in differential 
geometry. Indeed, a simply connected nilpotent Lie group is the 
same as the group $G(\mbb{R})$ of rational points of a unipotent 
algebraic group $G$ over $\mbb{R}$. 
\end{rem}
