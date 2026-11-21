---
doc_id: arxiv-1412.4229v4
doc_title: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS"
section_id: sec-001-1-some-facts-on-dg-rings-and-modules
section_title: "Some Facts on DG Rings and Modules"
section_number: 1
pages: 7-12
source_pdf: 1412.4229v4.pdf
source_sha256: 248d6a1e28a76a94
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.966
doc_brief: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS — Let A →B be a homomorphism of commutative rings."
---
\label{sec:facts-DG-mods}
\numberwithin{equation}{section}

In this section we review some known facts about DG rings and modules. 
We talk about central homomorphisms of DG rings. Finally, we introduce 
the cylinder construction for DG rings and modules.  

A {\em differential graded ring}, or {\em DG ring} for short, is a 
graded ring $A = \bigoplus_{i \in \Z} A^i$, together with an additive 
endomorphism $\d_A$ of degree $1$ called the {\em differential}. 
The differential $\d_A$ satisfies $\d_A \circ \d_A = 0$, and it is a graded 
derivation of $A$, namely it satisfies the graded Leibniz rule
\begin{equation} \label{eqn:320}
\d_A(a \cd b) = \d_A(a) \cd b + (-1)^{i} \cd a \cd \d_A(b) 
\end{equation}
for $a \in A^{i}$ and $b \in A^{j}$. (Most other texts would call such 
$A$ an associative unital DG algebra.)   

\begin{dfn}
We denote by $\cat{DGR}$ the category of all DG rings,
where the morphisms are the graded ring homomorphisms $u : A \to B$
that commute with the differentials.
\end{dfn}

We consider rings as DG rings concentrated in degree $0$. 
Thus the category of rings becomes a full subcategory of $\cat{DGR}$.

\begin{dfn} \label{dfn:400}
Let $A$ be a DG ring. A {\em DG ring over $A$}, or a {\em DG $A$-ring}, 
is a pair $(B, u)$, where $B$ is a DG ring and $u : A \to B$ is a DG ring
homomorphism. 

Suppose $(B, u)$ and $(B', u')$ are DG rings over $A$. 
A {\em homomorphism of DG rings over $A$}, or a {\em DG $A$-ring homomorphism}, 
is a homomorphism of DG rings $v : B \to B'$ such that $u' = v \circ u$.

We denote by $\cat{DGR} / A$ the category of DG rings over $A$.
\end{dfn}
 
Thus $\cat{DGR} / A$ is the usual ``coslice category'', except that we say 
``over'' instead of ``under''. See Remark \ref{rem:1016} regarding the 
direction of arrows. There is an obvious forgetful functor 
$\cat{DGR} / A \to \cat{DGR}$.
A morphism $v$ in $\cat{DGR} / A$ is shown in this commutative diagram:
\[ \UseTips \xymatrix @C=6ex @R=6ex {
B
\ar[r]^{v}
&
B'
\\
A
\ar[u]^{u}
\ar[ur]_{u'}
} \]

\begin{rem} \label{rem:1025}
We should probably justify the use of ``DG ring'', instead of the traditional 
``DG algebra''. We maintain that more generally, whenever we have a 
homomorphism $A \to B$ in the category of rings, then $B$ ought to be called 
an {\em $A$-ring}. Below is an explanation. 

Consider a commutative base ring $\K$. Given a ring homomorphism 
$\K \to A$ such that the target $A$ is commutative, we simply 
say that ``$A$ is a commutative $\K$-ring''. In the noncommutative context 
things are more delicate. When one says that ``$A$ is a $\K$-algebra'' 
(associative and unital), the meaning is that the ring homomorphism 
$\K \to A$ is central; namely the image of $\K$ is in the center of $A$. We 
suggest instead to use ``$A$ is a central $\K$-ring''. 

In the DG context, one says that ``$A$ is a DG $\K$-algebra'' (again 
associative and unital) if the image of $\K$ lies inside the subring of degree 
$0$ central cocycles of $A$. We propose to use ``central DG $\K$-ring'' 
instead, as in Definition \ref{dfn:750} below. 

Notice that the name ``ring'' allows us to drop the adjectives ``associative'' 
and ``unital''; and it also separates DG rings from DG Lie algebras etc. 

In the present paper we actually need to consider DG ring 
homomorphisms $u : A \to B$, where the source $A$ is a genuine DG ring, and 
in some cases it is even noncommutative. Thus $u(A)$ is sometimes not in the  
center of $B$, nor in the subring of cocycles, and we can't say that ``$B$ is a 
DG $A$-algebra''. But we can, and do, say that ``$B$ is a DG $A$-ring''.  
The homomorphism $u$ might be central nonetheless, as in Definition 
\ref{dfn:750}.
\end{rem}

Consider a graded ring $A$. For homogeneous elements $a \in A^i$ and 
$b \in A^j$ we define the graded commutator to be 
\begin{equation} \label{eqn:750}
\opn{ad}(a)(b) := a \cd b - (-1)^{i j} \cd b \cd a . 
\end{equation}
This extends to all $a, b \in A$ using bilinearity. Namely, if 
$a = \sum_k a_k$ and $b = \sum_l b_l$, with $a_k \in A^{i_k}$ and 
$b_l \in A^{j_l}$, then 
\[ \opn{ad}(a)(b) := \sum_{k, l} \opn{ad}(a_k)(b_l) . \]
Often the notation $[a, b]$ is used for the graded commutator. 

\begin{dfn} \label{dfn:750}
Let $A$ be a DG ring. 
\begin{enumerate}
\item The {\em center} of $A$ is the DG subring 
\[ A^{\mrm{ce}} := \{ a \in A \mid \opn{ad}(a)(b) = 0 \ \, \tup{for all} \ \,
b \in A \} . \]

\item The DG ring $A$ is called {\em weakly commutative} if 
$A^{\mrm{ce}} = A$. In other words, if 
\[ a \cd b = (-1)^{i j} \cd b \cd a \]
for all $a \in A^i$ and $b \in A^j$.

\item A homomorphism $u : A \to B$ in $\cat{DGR}$ is called {\em central} if 
$u(A^{\mrm{ce}}) \subseteq B^{\mrm{ce}}$. 
In this case, the resulting DG ring homomorphism $A^{\mrm{ce}} \to B^{\mrm{ce}}$
is denoted by $u^{\mrm{ce}}$.

\item We denote by $\cat{DGR} \centover A$ to be the the full subcategory of 
$\cat{DGR} / A$ consisting of pairs $(B, u)$ such that $u : A \to B$ is 
central.  
\end{enumerate}
\end{dfn}

Implicit in item (1) of the definition above is the (easy to check) fact that 
$A^{\mrm{ce}}$ is indeed a DG subring of $A$. The DG ring $A^{\mrm{ce}}$ itself 
is weakly commutative. 
As for item (4): a morphism $v : B \to B'$ in the category
$\cat{DGR} \centover A$ is not required to be central; the centrality condition 
is only on $A \xar{u} B$ and $A \xar{u'} B'$. 

If $u : A \to B$ and $v : B \to C$ are central homomorphisms 
in $\cat{DGR}$, then $v \circ u : A \to C$ is also central.
Thus we get a subcategory $\cat{DGR}_{\vec{\mrm{ce}}}$ of $\cat{DGR}$,
consisting of all objects, but only the central homomorphisms. 
Letting $\cat{DGR}_{\mrm{wc}}$ be the full subcategory of  $\cat{DGR}$ on the 
weakly commutative DG rings, we get a functor 
\[ (-)^{\mrm{ce}} : \cat{DGR}_{\vec{\mrm{ce}}} \to \cat{DGR}_{\mrm{wc}} . \]

Let $A$ be a DG ring. Recall that a left DG $A$-module is a left graded
$A$-module $M = \bigoplus_{i \in \Z} M^i$, with 
differential $\d_M$ of degree $1$, that satisfies $\d_M \circ \d_M = 0$ and
the graded Leibniz rule (equation (\ref{eqn:320}), but with $m \in M^{j}$ 
instead of $b$). Right DG $A$-modules are defined similarly. 
By default all DG modules in this paper are left DG modules. 

Let $A$ be a DG ring, let $M$ and $N$ be left DG $A$-modules, and let 
$\phi : M \to N$ be a degree $k$ 
additive (i.e.\ $\Z$-linear) homomorphism. We say that $\phi$ is $A$-linear if 
\begin{equation} \label{eqn:310}
\phi(a \cd m) =  (-1)^{i k} \cd a \cd \phi(m)
\end{equation}
for all $a \in A^i$ and $m \in M^j$. 
(This is the sign convention of \cite{ML}.)
The abelian group of $A$-linear homomorphisms of degree $k$ is denoted by 
$\opn{Hom}_{A}(M, N)^k$, and we let 
\begin{equation} \label{eqn:316}
\opn{Hom}_{A}(M, N) := \bigoplus_{k \in \Z} \,
\opn{Hom}_{A}(M, N)^{k} .
\end{equation}
The graded abelian group $\opn{Hom}_{A}(M, N)$ has a  differential $\d$ given by
\begin{equation} \label{eqn:690}
\d(\phi) := \d_N \circ \phi - (-1)^{k} \cd \phi \circ \d_M 
\end{equation}
for $\phi \in \opn{Hom}_A(M, N)^k$.
In particular, for $N = M$ we get a DG ring 
\begin{equation} \label{eqn:664}
\opn{End}_{A}(M) := \opn{Hom}_{A}(M, M) . 
\end{equation}

Suppose $A$ is a DG ring and $M$ a DG abelian group (i.e.\ a DG $\Z$-module). 
From (\ref{eqn:310}) we see that a DG $A$-module structure on $M$ is the same 
as a DG ring homomorphism $A \to \opn{End}_{\Z}(M)$. 

If $M$ is a right DG $A$-module and $N$ is a left DG $A$-module, then 
the usual tensor product $M \ot_A N$ is a graded abelian group: 
\[ M \ot_A N = \bigoplus_{k \in \Z} \, (M \ot_A N)^k , \]
where $(M \ot_A N)^k$ is the subgroup generated by the tensors $m \ot n$ 
such that $m \in M^i$ and $n \in N^{k - i}$. 
The graded abelian group 
$M \ot_A N$ has a differential $\d$ satisfying
\begin{equation} \label{eqn:220}
\d(m \ot n) := \d_M(m) \ot n + (-1)^i \cd m \ot \d_N(n)
\end{equation}
for $m, n$ as above.
  
Let $A$ and $B$ be DG rings. The tensor product $A \ot_{\Z} B$ is a DG ring, 
with multiplication 
\begin{equation} \label{eqn:820}
(a_1 \ot b_1) \cd (a_2 \ot b_2) := 
(-1)^{i_2 j_1} \cd (a_1 \cd a_2) \ot (b_1 \cd b_2)
\end{equation}
for $a_k \in A^{i_k}$ and $b_k \in B^{j_k}$, and with differential like in 
(\ref{eqn:220}). 

Let $B$ be a DG ring. Its  opposite DG ring $B^{\mrm{op}}$ is the 
same DG abelian group, but we denote its elements by 
$b^{\mrm{op}}$, $b \in B$. The multiplication in $B^{\mrm{op}}$ is
\[ b_1^{\mrm{op}} \cd b_2^{\mrm{op}} := 
(-1)^{j_1 j_2} \cd (b_2 \cd b_1)^{\mrm{op}} \]
for $b_k \in B^{j_k}$. 
Note that the centers satisfy
$(B^{\mrm{op}})^{\mrm{ce}} = (B^{\mrm{ce}})^{\mrm{op}}$,
and $B^{\mrm{op}} = B$ iff $B$ is weakly commutative.

If $M$ is a right DG $B$-module, then it can be seen as a left DG 
$B^{\mrm{op}}$-module, with action 
\[ b^{\mrm{op}} \cd m := (-1)^{k j} \cd m \cd b \]
for $b \in B^j$ and $m \in M^k$. 
Because of this observation, working only with left DG modules is 
not a limitation. We shall switch between notations according to convenience. 

Now consider a DG $A$-$B$-bimodule $M$, namely $M$ has a left $A$ action and a 
right $B$ action, and they commute, i.e.\ 
$a \cd (m \cd b) = (a \cd m) \cd b$. Then $M$ can be 
viewed as a left 
$A \ot_{\Z} B^{\mrm{op}}$ -module with action 
\begin{equation} \label{eqn:321}
(a \ot b^{\mrm{op}}) \cd m := (-1)^{k j} \cd a \cd m \cd b
\end{equation}
for $a \in A^{i}$, $b \in B^{j}$ and $m \in M^k$.
Thus a DG $A$-$B$-bimodule structure on a DG abelian group $M$ is the 
same as a homomorphism of DG rings  
\[ A \ot_{\Z} B^{\mrm{op}} \to \opn{End}_{\Z}(M) . \]

Let $A$ be a weakly commutative DG ring. Any $B \in \cat{DGR} \centover A$ is a 
DG $A$-bimodule.
If $B, C \in \cat{DGR} \centover A$, then the DG $A$-module
$B \ot_A C$ has an obvious DG ring structure, and moreover
$B \ot_A C \in \cat{DGR} \centover A$. Given a DG $B$-module $M$ 
and and a DG $C$-module $N$, the tensor product $M \ot_A N$ 
is a DG module over $B \ot_A C$, with action 
\[ (b \ot c) \cd (m \ot n) := (-1)^{i j} \cd (b \cd m) \ot (c \cd n) \]
for $c \in C^i$ and $m \in M^j$.

\begin{dfn}
Let $A$ be a DG ring. 
We denote by $\cat{DGMod} A$ the category of left DG $A$-modules,
where the morphisms are the $A$-linear homomorphisms
$\phi : M \to N$ of degree $0$ that commute with the differentials. 
Since the name is too long, we mostly use the abbreviation
$\cat{M}(A) := \cat{DGMod} A$.
\end{dfn}

The category $\cat{M}(A)$ is abelian. 
The set $\cat{M}(A)$ also has a DG category structure on it, in which the 
set of morphisms $M \to N$ is the DG abelian group 
$\opn{Hom}_{A}(M, N)$. The relation between these structures is 
\begin{equation} \label{eqn:1015}
\opn{Hom}_{\cat{M}(A)}(M, N) = \mrm{Z}^0 \bigl( 
\opn{Hom}_A(M, N) \bigr) ,
\end{equation}
the group of $0$-cocycles.

Let $M = \bigoplus_{i \in \Z} \, M^i$ be a graded abelian group. Recall that 
the shift (or twist, or translation, or suspension) of $M$ is the graded 
abelian group $\opn{T}(M) = \bigoplus_{i \in \Z} \, \opn{T}(M)^i$ defined as 
follows. The graded component of degree $i$ of $\opn{T}(M)$ is 
$\opn{T}(M)^i := M^{i + 1}$.
Note that as (ungraded) abelian groups we have $\opn{T}(M) = M$, but the 
gradings are different. Thus the identity automorphism of $M$ becomes a 
degree $-1$ invertible homomorphism of graded abelian groups
$\opn{t} : M \to \opn{T}(M)$. 
We shall usually represent elements of $\opn{T}(M)^i$ as 
$\opn{t}(m)$, with $m \in M^{i + 1}$.

If $M$ is a DG $A$-module, then $\opn{T}(M)$ has the following structure of DG 
$A$-module. The differential $\d_{\opn{T}(M)}$ is 
\begin{equation} \label{eqn:680}
\d_{\opn{T}(M)}(\opn{t}(m)) := - \opn{t}(\d_M(m)) =  \opn{t}(- \d_M(m))
\end{equation}
for $m \in M^k$. The action of $A$ is 
\begin{equation} \label{eqn:681}
a \cd \opn{t}(m) := (-1)^i \cd \opn{t}(a \cd m) = \opn{t}((-1)^i \cd a \cd m)
\end{equation}
for $a \in A^i$. 
If $M$ is a DG right module, or a DG bimodule, then the structure of 
$\opn{T}(M)$ is determined by (\ref{eqn:680}), (\ref{eqn:681}) and 
(\ref{eqn:321}). Concretely, 
\[ a \cd \opn{t}(m) \cd b = (-1)^i \cd \opn{t}(a \cd m \cd b) \]
for $a \in A^i$, $m \in M^k$ and $b \in A^j$.
Note that our sign conventions for the shift are such that the canonical 
bijection
\[ \opn{T}(\Z) \ot_{\Z} M \to \opn{T}(M) , \
\opn{t}(c) \ot m \mapsto \opn{t}(c \cd m) = c \cd \opn{t}(m) , \]
for $c \in \Z$ and $m \in M$, is an isomorphism of DG $A$-bimodules. 

For any $k \in \Z$, the $k$-th power of $\opn{T}$ is denoted by $\opn{T}^k$. 
There is a corresponding degree $-k$ homomorphism of graded abelian groups 
\begin{equation} \label{eqn:1025}
\opn{t}^k : M \to \opn{T}^k(M) , 
\end{equation}
which is the identity on the underlying ungraded abelian group. 
Note that \lb $\opn{T}^{l}(\opn{T}^k(M)) = \opn{T}^{k + l}(M)$,
and $\opn{T}^k$ is an automorphism of the category $\cat{M}(A)$.
As usual, we write $M[k] := \opn{T}^k(M)$. 

We now recall the {\em cone} construction, as it looks using the operator 
$\opn{t}$. Let $A$ be a DG ring, and let 
$\phi : M \to N$ be a homomorphism in $\cat{M}(A)$. The cone of $\phi$ is 
the DG $A$-module 
$\opn{Cone}(\phi) := N \oplus M[1]$, 
whose differential, when we express this module as the column
$\sbmat{N \\ M[1]}$, is left multiplication by the matrix of degree $1$ 
abelian group homomorphisms
$\sbmat{\d_N & \phi \circ \opn{t}^{-1} \\ 0 & \d_{M[1]}}$.

We learned the concept of {\em cylinder DG ring}, defined below, from B. 
Keller. It appears (without this name) in his \cite{Ke2}. 

Consider the matrix DG ring 
\begin{equation} \label{eqn:817}
\opn{Cyl}(\Z) := \bmat{\Z & \Z[-1] \\ 0 & \Z} 
= \Bigl\{ \bmat{a_0 & b \cd \xi \\ 0 & a_1} 
\big| \, a_0, a_1, b \in \Z \Bigr\} ,
\end{equation}
where the element $\xi := \opn{t}^{-1}(1) \in \Z[-1]$ has degree $1$. 
The multiplication is 
\begin{equation} \label{eqn:704}
\bmat{a_0 & b \cd \xi \\ 0 & a_1} \cd 
\bmat{a'_0 & b' \cd \xi \\ 0 & a'_1} := 
\bmat{a_0 \cd a'_0 & (a_0 \cd b' + b \cd a'_1) \cd \xi 
\\ 0 & a_1 \cd a'_1}
\end{equation}
where $a'_0, a'_1, b' \in \Z$. 
The differential is 
$\d_{\mrm{cyl}} := \opn{ad}( \sbmat{0 & \xi \\ 0 & 0} )$,
the graded commutator with the element
$\sbmat{0 & \xi \\ 0 & 0}$. Explicitly we have  
\begin{equation} \label{eqn:210}
\d_{\mrm{cyl}} ( \bmat{a_0 & b \cd \xi \\ 0 & a_1} ) 
= \bmat{ 0 & (-a_0 + a_1) \cd \xi \\ 0 & 0 } .
\end{equation}
There are DG ring homomorphisms 
$\Z \xar{\ep} \opn{Cyl}(\Z) \xar{\eta_i} \Z$, for $i = 0, 1$, with formulas 
\begin{equation} \label{eqn:703}
\ep(a) := \bmat{a & 0 \\ 0 & a} \quad \text{and} \quad 
\eta_i(\bmat{a_0 & b \cd \xi \\ 0 & a_1}) := a_i .
\end{equation}
It is easy to see that $\ep$ and $\eta_i$ are quasi-isomorphisms, and 
$\eta_i \circ \ep = \opn{id}_{\Z}$, the identity automorphism of $\Z$.

\begin{dfn} \label{dfn:700}
Let $A$ be a DG ring. The {\em cylinder} of $A$ is the DG ring 
\[ \opn{Cyl}(A) := \opn{Cyl}(\Z) \ot_{\Z} A 
\cong \bmat{A & A[-1] \\ 0 & A} , \] 
with multiplication induced from (\ref{eqn:704}), and differential 
induced from (\ref{eqn:210}), using  formulas (\ref{eqn:820}) and
(\ref{eqn:220}).
\end{dfn}

It will be convenient to denote elements of $\opn{Cyl}(A)$ as matrices 
$\sbmat{a_0 & \xi \cd b \\ 0 & a_0}$, rather than as tensors. 
Note that the element $\xi$ is central and has degree $1$, so 
$b \cd \xi = (-1)^k \cd \xi \cd b$ for $b \in A^k$. 

\begin{prop} \label{prop:700}
Let $A$ be a DG ring. Consider the induced DG ring homomorphisms 
$A \xar{\ep} \opn{Cyl}(A) \xar{\eta_i} A$. 
\begin{enumerate}
\item The homomorphisms $\ep$ and $\eta_i$ are DG ring quasi-isomorphisms.

\item The homomorphisms $\ep$ and $\eta_i$ are central, and moreover the induced
homomorphisms 
$\ep^{\mrm{ce}} : A^{\mrm{ce}} \xar{} \opn{Cyl}(A)^{\mrm{ce}}$
and
$\eta_i^{\mrm{ce}} : \opn{Cyl}(A)^{\mrm{ce}} \to A^{\mrm{ce}}$
are bijective. 
\end{enumerate}
\end{prop}

\begin{proof}
Since $\opn{Cyl}(\Z)$ is a free graded $\Z$-module (via $\ep$, and forgetting 
the differential), these are  direct consequences of the corresponding 
assertions for $\Z$; and those are clear.
\end{proof}

\begin{dfn} \label{dfn:815}
Let $A$ be a DG ring and $M$ a DG $A$-module. The {\em cylinder} of $M$ is 
the DG $\opn{Cyl}(A)$-module  
\[ \opn{Cyl}(M) := \opn{Cyl}(\Z) \ot_{\Z} M 
\cong \opn{Cyl}(A) \ot_{A} M
\cong \bmat{M & M[-1] \\ 0 & M} , \] 
with multiplication induced from (\ref{eqn:704}), and differential 
induced from (\ref{eqn:210}).
\end{dfn}

The definition above relates also to right DG modules and to bimodules, as 
explained in (\ref{eqn:321}). 

\begin{prop} \label{prop:701}
Let $A$ be a DG ring and let $M$ be a DG $A$-module.
The induced DG module homomorphisms $\ep : M \to \opn{Cyl}(M)$ and 
$\eta_i : \opn{Cyl}(M) \to M$ are quasi-isomorphisms. 
\end{prop}

When considering the homomorphism 
$\ep : M \to \opn{Cyl}(M)$, we view $\opn{Cyl}(M)$ as 
a DG $A$-module via the DG ring homomorphism $\ep : A \to \opn{Cyl}(A)$.
Likewise, when considering the homomorphism 
$\eta_i : \opn{Cyl}(M) \to M$, we view $M$ as 
a DG $\opn{Cyl}(A)$-module via the DG ring homomorphism 
$\eta_i : \opn{Cyl}(A) \to A$.

\begin{proof}
As in Proposition \ref{prop:700}(1), this is immediate from the fact that 
 $\ep : \Z \to \opn{Cyl}(\Z)$ and 
$\eta_i : \opn{Cyl}(\Z) \to \Z$ are quasi-isomorphisms. 
\end{proof}

The cylinder operation (on DG rings and modules) has the following 
functoriality. If $u : A \to B$ is a DG ring homomorphism, then there is an 
induced DG ring homomorphism 
$\opn{Cyl}(u) : \opn{Cyl}(A) \to \opn{Cyl}(B)$, 
$\opn{Cyl}(u) := \opn{id}_{\opn{Cyl}(\Z)} \ot \, u$. 
Explicitly the formula is
\begin{equation} \label{eqn:702}
\opn{Cyl}(u)( \bmat{a_0 & \xi \cd b \\ 0 & a_1}) =
\bmat{u(a_0) & \xi \cd u(b) \\ 0 & u(a_1)} . 
\end{equation}
Likewise for modules.

\begin{rem} \label{rem:1016}
In the abstract categorical sense, the DG ring $\opn{Cyl}(A)$
plays a role dual to that of a cylinder; so perhaps we should have called it  
``the path object of $A$''. 
Indeed, this is precisely the path object described on page 503 of \cite{ScSh}.

We decided to adhere to the name ``cylinder'' for two reasons. First, this is 
the name used in \cite{YZ2}. The second reason is that we are dealing with 
rings here, and so (as happens in algebraic geometry) arrows tend to be 
reversed. The same reversal occurs in Definition \ref{dfn:400}: we talk about 
``DG rings over $A$'', rather than about ``DG rings under $A$'', as the 
categorical convention would dictate. 
\end{rem}
