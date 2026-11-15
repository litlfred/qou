---
doc_id: arxiv-0801.0083v4
doc_title: "CENTRAL EXTENSIONS OF GERBES"
section_id: sec-004-4-obstruction-classes
section_title: "Obstruction Classes"
section_number: 4
pages: 19-25
source_pdf: 0801.0083v4.pdf
source_sha256: 8e38b9e56d246709
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.978
doc_brief: "CENTRAL EXTENSIONS OF GERBES — We introduce the notion of central extension of gerbes on a topo- logical space X."
---
We fix a topological space $X$. 
Given a sheaf $\mcal{N}$ of abelian groups on $X$, and an open covering
$\bsym{U} = \{ U_k \}_{k \in K}$ of $X$, there are the \v{C}ech
cohomology groups $\check{\mrm{H}}^p(\bsym{U}, \mcal{N})$
for  $p \geq 0$. Passing to the limit over all such open coverings 
we obtain the \v{C}ech cohomology groups $\check{\mrm{H}}^p(X, \mcal{N})$.

{} From here until the end of this section we consider a central
extension of gerbes
\begin{equation} \label{eqn:5}
1 \to  \mcal{N} \to \gerbe{G} \xar{F} \gerbe{H} \to 1 
\end{equation}
on $X$ (see Definition \ref{dfn:2} and Proposition \ref{prop:12}). 

\begin{construction} \label{const2}
Let $i, j \in \opn{Ob} \gerbe{G}(X)$, and let
$h \in \gerbe{H}(X) \bigl( F(i), F(j) \bigr)$. 
Since $F$ is a weak epimorphism, there exists an open covering 
$\bsym{U} = \{ U_k \}_{k \in K}$ of $X$, such that for every $k \in K$ 
there is an isomorphism $g_k \in \gerbe{G}(U_k)(i, j)$ with $F(g_k) = h$.
For every $k_0, k_1 \in K$ we define
\[ g_{k_0, k_1} := g_{k_1}^{-1} \circ g_{k_0}
\in \gerbe{G}(U_{k_0, k_1})(i, i) . \]
Since $F(g_{k_0, k_1}) = 1$ we see that in fact
$g_{k_0, k_1} \in \mcal{N}(U_{k_0, k_1})$.
An easy calculation shows that the collection
\begin{equation} 
c := \{ g_{k_0, k_1} \}_{k_0, k_1 \in K}
\end{equation}
is a \v{C}ech $1$-cocycle for the covering $\bsym{U}$ with values in
the sheaf of groups $\mcal{N}$. 
\end{construction}

\begin{lem}
Let $i, j \in \opn{Ob} \gerbe{G}(X)$ and let
$h \in \gerbe{H}(X) \bigl( F(i), F(j) \bigr)$. 
Suppose that $c$ and $c'$ are $1$-cocycles with values in $\mcal{N}$, for open
coverings $\bsym{U}$  and $\bsym{U}'$, obtained as in Construction
\tup{\ref{const2}}, for the same isomorphism $h$. 
Then their \v{C}ech cohomology classes 
$[c], [c'] \in \check{\mrm{H}}^1(X, \mcal{N})$ are equal. 
\end{lem}

\begin{proof}
Say $\bsym{U}' = \{ U'_k \}_{k \in K'}$.
Suppose that in the course of constructing the cocycle $c'$ we chose,
for every $k \in K'$, an isomorphism 
$g'_k \in \gerbe{G}(U'_k)(i, j)$ with $F(g'_k) = h$.
So
$g'_{k_0, k_1} = {g'}_{k_1}^{-1} \circ g'_{k_0}$
and $c' = \{ g'_{k_0, k_1} \}_{k_0, k_1 \in K'}$. 

Take some open covering
$\bsym{V} = \{ V_l \}_{l \in L}$ of $X$ which refines both 
$\bsym{U}$ and $\bsym{U}'$. Thus there are functions
$\phi : L \to K$ and $\phi' : L \to K'$, such that
$V_l \subset U_{\phi(l)}$ and $V_l \subset U'_{\phi'(l)}$ for all $l \in L$. 
We get cocycles
\[ \phi^*(c) := \{ g_{\phi(l_0), \phi(l_1)} \}_{ l_0, l_1 \in L} \]
and
\[ {\phi'}^*(c') := \{ g'_{\phi'(l_0), \phi'(l_1)} \}_{ l_0, l_1 \in L} . \]
For any $l \in L$ let
\[ f_l := g_{\phi(l)}^{-1} \circ g'_{\phi'(l)}  \in \gerbe{G}(V_l)(i, i) . \]
Now
\[ F(f_l) = F(g_{\phi(l)})^{-1} \circ F(g'_{\phi'(l)}) = 
h^{-1} \circ h = 1 . \]
So $b := \{ f_l \}_{l \in L}$ is a $0$-cochain 
with values in $\mcal{N}$. 

Take any $l_0, l_1 \in L$. Then
\[ \begin{aligned}
& (f_{l_1}^{-1} \circ f_{l_0}) \circ g_{\phi(l_0), \phi(l_1)} \\
& \quad = 
(g_{\phi(l_1)}^{-1} \circ g_{\phi'(l_1)}')^{-1} \circ
(g_{\phi(l_0)}^{-1} \circ g_{\phi'(l_0)}') \circ 
(g_{\phi(l_1)}^{-1} \circ g_{\phi(l_0)}) \\
& \quad = 
g_{\phi'(l_1)}'^{-1} \circ g_{\phi'(l_0)}' =
g'_{\phi'(l_0), \phi'(l_1)} \, . 
\end{aligned} \]
Denoting the \v{C}ech coboundary operator by $\d$, we see that
\[ \d(b) \cdot \phi^*(c) = {\phi'}^*(c') . \]
\end{proof}

In view of this lemma, the following definition makes sense. 

\begin{dfn} \label{dfn.6}
Let $i, j \in \opn{Ob} \gerbe{G}(X)$, and let
$h \in \gerbe{H}(X) \bigl( F(i), F(j) \bigr)$. 
Take any $1$-cocycle $c$ as in Construction \tup{\ref{const2}}.
We define the obstruction class 
\[ \opn{cl}^1_{F}(h) := [c] \in \check{\mrm{H}}^1(X, \mcal{N}) . \]
\end{dfn}

\begin{thm}[Obstruction to lifting isomorphisms] \label{thm.3}
Consider a central extension of gerbes 
\[ 1 \to  \mcal{N} \to \gerbe{G} \xar{F} \gerbe{H} \to 1 . \]
Let $i, j \in \opn{Ob} \gerbe{G}(X)$, and let
$h \in \gerbe{H}(X) \bigl( F(i), F(j) \bigr)$. 
Then there exists an isomorphism 
$g \in \gerbe{G}(X)(i,j)$ satisfying 
$F(g) = h$ if and only if
\[ \opn{cl}_F^1(h) = 1 . \]
\end{thm}

In other words, the class $\opn{cl}_F^1(h)$ is the obstruction to lifting the
isomorphism 
$h : F(i) \to F(j)$
to an isomorphism 
$g : i \to j$.

\begin{proof}
First assume there exists a lifting $g$. 
We construct a cocycle $c$ as follows: for the open covering 
$\bsym{U} = \{ U_k \}_{k \in K}$ we take 
$K := \{ 0 \}$ and $U_0 := X$. We then take $g_0 := g$. 
The resulting cocycle is $c$ is trivial, and hence
$\opn{cl}_F^1(h) = 1$. 

Conversely, assume that $\opn{cl}_F^1(h) = 1$. 
Let $c' = \{ g'_{k_0, k_1} \}_{k_0, k_1 \in K}$ be a $1$-cocycle that represents
$\opn{cl}_F^1(h)$ on some open covering
$\bsym{U}$. Say $g'_k \in \gerbe{G}(U_k)(i, j)$ are the isomorphisms
chosen in the construction of $c'$, so that
$g'_{k_0, k_1} =  g'^{-1}_{k_1} \circ g'_{k_0}$. 

By replacing $\bsym{U}$ with a suitable refinement, we can assume
that $c'$ is a coboundary; i.e.\ there is a $0$-cochain
$b := \{ f_k \}_{k \in K}$ with values in $\mcal{N}$
such that $c' = \d(b)$. Define
\[ g_k := g'_k \circ f^{-1}_k \in  \gerbe{G}(U_k)(i, j) . \]
A calculation shows that $\{ g_k \}_{k \in K}$ is a $0$-cocycle with values in
the sheaf of sets $\gerbe{G}(i, j)$. 
Hence it glues to a global isomorphism
$g \in \gerbe{G}(X)(i, j)$. And by construction we have
$F(g) = h$.
\end{proof}

\begin{cor} \label{cor:1}
Given a central extension of gerbes as above, let 
$i, j \in \opn{Ob} \gerbe{G}(X)$. Then 
$\gerbe{G}(X)(i, j) \neq \emptyset$
if and only if there exists some 
$h \in \gerbe{H}(X) \bigl( F(i), F(j) \bigr)$
such that
$\opn{cl}_F^1(h) = 1$.
\end{cor}

\begin{proof}
This is an immediate consequence of the theorem.
\end{proof}

\begin{rem}
In an earlier version of this paper we claimed that 
$\opn{cl}_F^1(h) = \opn{cl}_F^1(h')$ for any
$h, h' \in \gerbe{H}(X) \bigl( F(i), F(j) \bigr)$. 
However the referee discovered a mistake in our proof.
\end{rem}

\begin{construction} \label{const1}
Let $j \in \opn{Ob} \gerbe{H}(X)$. 
Choose some open covering
$\bsym{U} = \{ U_k \}_{k \in K}$ of $X$. For every $k \in K$ choose,
if possible, an object
$i_k \in \opn{Ob} \gerbe{G}(U_k)$ and an isomorphism
\[ h_k \in \gerbe{H}(U_k) \bigl( F(i_k), j \bigr)  . \]
For every $(k_0, k_1) \in K \times K$ define
\[ h_{k_0, k_1} := h_{k_1}^{-1} \circ h_{k_0}
\in \gerbe{H}(U_{k_0, k_1}) \bigl( F(i_{k_0}), F(i_{k_1}) \bigr)
. \]
Choose, if possible, an isomorphism
\[ g_{k_0, k_1} \in \gerbe{G}(U_{k_0, k_1})(i_{k_0}, i_{k_1}) \]
that lifts $h_{k_0, k_1}$, i.e.\
$F(g_{k_0, k_1}) = h_{k_0, k_1}$. Define
\[ g_{k_0, k_1, k_2} := g_{k_0, k_2}^{-1} \circ g_{k_1, k_2} \circ
g_{k_0, k_1} \in \gerbe{G}(U_{k_0, k_1, k_2})(i_{k_0}, i_{k_0})
. \]
Thus we get a collection of elements
\begin{equation} \label{eqn:2}
c := \{ g_{k_0, k_1, k_2} \}_{k_0, k_1, k_2 \in K} . 
\end{equation}
\end{construction}

\begin{lem} \label{lem:10}
The collection $c$ from this construction is a \v{C}ech $2$-cocycle with values
in $\mcal{N}$.
\end{lem}

\begin{proof}
Since $F(g_{k_0, k_1, k_2}) = 1$ it follows that 
$g_{k_0, k_1, k_2} \in \mcal{N}(U_{k_0, k_1, k_2})$. 

Let us now calculate the value of the coboundary of $c$ in
$\mcal{N}(U_{k_0, k_1, k_2, k_3})$, using the fact that $\mcal{N}$ is
central in $\mcal{G}$:
\[ \begin{aligned}
& g_{k_1, k_2, k_3} \circ g_{k_0, k_2, k_3}^{-1} \circ 
g_{k_0, k_1, k_3} \circ g_{k_0, k_1, k_2}^{-1} \\
& \quad = g_{k_1, k_2, k_3} 
\circ ( g_{k_0, k_3}^{-1} \circ g_{k_2, k_3} \circ 
g_{k_0, k_2} )^{-1} \\
& \qquad \quad  \circ 
( g_{k_0, k_3}^{-1} \circ g_{k_1, k_3} \circ g_{k_0, k_1} ) 
\circ ( g_{k_0, k_2}^{-1} \circ g_{k_1, k_2} \circ 
g_{k_0, k_1} )^{-1} \\
& \quad = g_{k_1, k_2, k_3} \circ 
g_{k_0, k_2}^{-1} \circ g_{k_2, k_3}^{-1} \circ 
g_{k_0, k_3}  \\
& \qquad  \quad \circ g_{k_0, k_3}^{-1} \circ g_{k_1, k_3} \circ g_{k_0, k_1}
\circ g_{k_0, k_1}^{-1} \circ g_{k_1, k_2}^{-1} \circ 
g_{k_0, k_2} \\
& \quad =  g_{k_0, k_2}^{-1} \circ g_{k_2, k_3}^{-1} 
\circ g_{k_1, k_3} \circ g_{k_1, k_2, k_3}
\circ g_{k_1, k_2}^{-1} \circ 
g_{k_0, k_2} \\
& \quad =  g_{k_0, k_2}^{-1} \circ g_{k_2, k_3}^{-1} 
\circ g_{k_1, k_3} \\
& \qquad \quad  \circ (g_{k_1, k_3}^{-1} \circ g_{k_2, k_3} \circ 
g_{k_1, k_2}) \circ g_{k_1, k_2}^{-1} \circ 
g_{k_0, k_2} \\
& \quad =  1 .
\end{aligned} \]
\end{proof}

\begin{lem} \label{lem.4}
Let $j \in \opn{Ob} \gerbe{H}(X)$. 
Suppose that $c$ and $c'$ are $2$-cocycles with values in $\mcal{N}$, for open
coverings $\bsym{U}$  and $\bsym{U}'$, obtained as in Construction
\tup{\ref{const1}}. Then their \v{C}ech cohomology classes 
$[c], [c'] \in \check{\mrm{H}}^2(X, \mcal{N})$ are equal. 
\end{lem}

\begin{proof}
The cocycle $c'$ is constructed using some open covering
$\bsym{U}' = \{ U'_k \}_{k \in K'}$,
objects
$i'_k \in \opn{Ob} \gerbe{G}(U'_k)$
that lift $j$, isomorphisms
$h'_k \in \gerbe{H}(U'_k) \bigl( F(i'_k), j \bigr)$,
and isomorphisms 
$g'_{k_0, k_1} \in \gerbe{G}(U'_{k_0, k_1})(i'_{k_0}, i'_{k_1})$
that lift 
$h'_{k_0, k_1} := {h'}_{k_1}^{-1} \circ h'_{k_0}$. 

The proof proceeds in four steps, labeled (a)-(d). 

\medskip \noindent 
(a) Suppose $\bsym{U}' = \bsym{U}$, 
$i'_k = i_k$ and $h'_k = h_k$, but we choose some other lifting
$g'_{k_0, k_1}$ of $h_{k_0, k_1}$. 
The $2$-cocycle $c' = \{ g'_{k_0, k_1, k_2} \}$ is
\begin{equation} \label{eqn:4}
g'_{k_0, k_1, k_2} := g_{k_0, k_2}'^{-1} \circ g_{k_1, k_2}' \circ
g_{k_0, k_1}'  \in \gerbe{G}(U_{k_0, k_1, k_2})(i_{k_0}, i_{k_0}) .
\end{equation} 
Now there are unique elements
\[ n_{k_0, k_1} \in \mcal{N}(U_{k_0, k_1})(i_{k_0}, i_{k_0}) \]
such that
\[ g'_{k_0, k_1} = n_{k_0, k_1} \circ g_{k_0, k_1} . \]
Consider the \v{C}ech $1$-cochain 
$b := \{ n_{k_0, k_1} \}$ with values in $\mcal{N}$. A little calculation shows
that
\[ g'_{k_0, k_1, k_2} = g_{k_0, k_1, k_2} \circ 
(n_{k_0, k_2}^{-1} \circ  n_{k_0, k_1} \circ n_{k_1, k_2}) ; \]
so that 
$c' = c \cdot \d(b)$. We see that $c$ and $c'$ have
the same cohomology class. 

\medskip \noindent 
(b) Next suppose $\bsym{U}' = \bsym{U}$ and $i'_k = i_k$, but we 
choose other isomorphisms
$h'_k \in \gerbe{H}(U_k)(F(i_k), j)$.
Define
\[ h'_{k_0, k_1} := h_{k_1}'^{-1} \circ h'_{k_0} 
\in \gerbe{H}(U_{k_0, k_1})(F(i_{k_0}), F(i_{k_1})) . \]
Consider the elements
\[ f_k := h_k^{-1} \circ h'_k \in \gerbe{H}(U_k)
(F(i_k), F(i_k)) . \]
Take some open covering $\bsym{V} = \{ V_l \}_{l \in L}$ that refines 
$\bsym{U}$, with comparison function $\phi : L \to K$, such that for every 
$l \in L$ the isomorphism $f_{\phi(l)}$ lifts to some
$g_l \in \bsym{\gerbe{G}}(V_l)(i_{\phi(l)}, i_{\phi(l)})$.
This is possible since $F$ is locally surjective on isomorphism sheaves. 
By replacing $\bsym{U}$ with $\bsym{V}$, we can now assume that each
$f_k$ lifts to some
$g_k \in \bsym{\gerbe{G}}(U_k)(i_{k}, i_{k})$.

Now let us define
\[ g''_{k_0, k_1} := g_{k_1}^{-1} \circ g_{k_0, k_1} \circ
g_{k_0} \in \gerbe{G}(U_{k_0, k_1})(i_{k_0}, i_{k_1}) . \]
Then $g''_{k_0, k_1}$ is a lifting of $h'_{k_0, k_1}$. Proceeding as in equation
(\ref{eqn:4}), we obtain a \v{C}ech $2$-cocycle
$c'' = \{ g''_{k_0, k_1, k_2} \}$.
However, it is easy to see that 
\[ g''_{k_0, k_1, k_2} = g_{k_0}^{-1} \circ g_{k_0, k_1, k_2} \circ
g_{k_0} . \]
Since $g_{k_0, k_1, k_2}$ is central in $\gerbe{G}$ it follows
that in fact
$g''_{k_0, k_1, k_2} =  g_{k_0, k_1, k_2}$, so that $c'' = c$.
On the other hand, from step (a) we see that 
$[c''] = [c']$ in $\check{\mrm{H}}^2(X, \mcal{N})$. 

\medskip \noindent 
(c) Now suppose $\bsym{U}' = \bsym{U}$, but 
we choose another object
$i'_k \in \opn{Ob} \gerbe{G}(U_k)$ for each $k$. 
Take some open covering $\bsym{V} = \{ V_l \}_{l \in L}$ that refines 
$\bsym{U}$, with comparison function $\phi : L \to K$, such that for every 
$l \in L$ one has
\[ \gerbe{G}(V_l)(i_{\phi(l)}, i'_{\phi(l)}) \neq \emptyset . \]
This can be done because $\gerbe{G}$ is locally connected. 
After replacing $\bsym{U}$ with $\bsym{V}$, we can assume that there is some
$f_k \in \gerbe{G}(U_k)(i_k, i'_k)$ for every $k \in K$.

In view of steps (a-b) we might as well take
\[ h'_k := h_k \circ F(f_k)^{-1} \in 
\gerbe{H}(U_k) \bigl( F(i'_k), j \bigr) , \]
and then lift
\begin{equation}
h'_{k_0, k_1} := h_{k_1}'^{-1} \circ h'_{k_0} 
\in \gerbe{H}(U_{k_0, k_1}) \bigl( F(i'_{k_0}), F(i'_{k_1}) \bigr)
\end{equation}
to
\[ g_{k_0, k_1}' := f_{k_1} \circ g_{k_0, k_1} \circ f_{k_0}^{-1} 
\in \gerbe{G}(U_{k_0, k_1})(i'_{k_0}, i'_{k_1}) . \]
The resulting $2$-cocycle $c' = \{ g'_{k_0, k_1, k_2} \}$ defined as in 
(\ref{eqn:4}) will satisfy
\[ g'_{k_0, k_1, k_2} = f_{k_0}^{-1}  \circ 
g_{k_0, k_1, k_2} \circ f_{k_0} . \]
Because $\mcal{N}$ is central we get $c' = c$.

\medskip \noindent 
(d) Finally let's see what happens when we take a new open covering
$\bsym{U}' = \{ U_k \}_{k \in K'}$ of $X$, for which we can construct a
cocycle $c'$. Let $\bsym{V} = \{ V_l \}_{l \in L}$ be a common refinement,
namely there are functions $\phi : L \to K$ and $\phi' : L \to K'$, such that
$V_l \subset U_{\phi(l)}$ and $V_l \subset U'_{\phi'(l)}$ for all $l \in L$. 
Let $\phi^*(c)$ and $\phi'^*(c')$ be the pullback $2$-cocycles on the open
covering $\bsym{V}$. These are both cocycles that are constructed like in
Construction \ref{const1}, for the obvious choices of objects etc. By steps
(a-c) we know that $[\phi^*(c)] = [\phi'^*(c')]$. But on the other hand
$[\phi^*(c)] = [c]$ and $[\phi'^*(c')] = [c']$.
\end{proof}

The lemma justifies the next definition.

\begin{dfn} \label{dfn.4}
Let $j \in \opn{Ob} \gerbe{H}(X)$.
If there exists a $2$-cocycle $c$ as in Construction
\tup{\ref{const1}}, for some open covering $\bsym{U}$, then we
define the {\em obstruction class to lifting objects} to be
\[ \opn{cl}^2_F(j) := [c] \in \check{\mrm{H}}^2(X, \mcal{N}) . \]
Otherwise we say that this obstruction class is undefined.
\end{dfn}

In Section \ref{sec.suff} we shall see sufficient conditions for the
obstruction class $\opn{cl}^2_F(j)$ to be defined.

\begin{prop} \label{prop:10}
Let $j \in \opn{Ob} \gerbe{H}(X)$ be such that the obstruction class
$\opn{cl}^2_F(j)$ is defined. 
Suppose $j' \in \opn{Ob} \gerbe{H}(X)$ is such that
$\gerbe{H}(X)(j,j') \neq \emptyset$. Then
the obstruction class $\opn{cl}_F^2(j')$ is also defined, and moreover
\[ \opn{cl}^2_F(j') = \opn{cl}_F^2(j) . \]
\end{prop}

What the proposition says is that two isomorphic objects have the same 
obstruction class. 

\begin{proof}
We want to construct a \v{C}ech $2$-cocycle $c'$, starting with $j'$ 
instead of $j$. Take any $f \in \gerbe{H}(X)(j, j')$. 
Using this isomorphism we may define
\[ h'_k := f \circ h_k \in \gerbe{H}(U_k)(F(i_k), j') , \]
where $i_k$ is the lifting of $j$ that was used in the construction of $c$,
and $h_k \in \gerbe{H}(U_k)(F(i_k), j)$ is the isomorphism that was
chosen. 

Let 
\[ h'_{k_0, k_1} := h_{k_1}'^{-1} \circ h_{k_0}'
 \in \gerbe{H}(U_{k_0, k_1})(F(i_{k_0}), F(i_{k_1})) . \]
Then $h'_{k_0, k_1} = h_{k_0, k_1}$; so continuing with 
Construction \ref{const1} we get a cocycle $c'$ that equals $c$. 
\end{proof}

\begin{thm}[Obstruction to lifting objects] \label{thm.2}
Consider a central extension of gerbes 
\[ 1 \to  \mcal{N} \to \gerbe{G} \xar{F} \gerbe{H} \to 1 . \]
Let $j \in \opn{Ob} \gerbe{H}(X)$ be such that
the obstruction class $\opn{cl}_F^2(j)$ is defined. Then 
there exists an object 
$i \in \opn{Ob} \gerbe{G}(X)$ with 
\[ \gerbe{H}(X) \bigl( F(i), j \bigr) \neq \emptyset \]
if and only if
\[ \opn{cl}_F^2(j) = 1 . \]
\end{thm}

What the theorem says is that $\opn{cl}_F^2(j)$ is the obstruction to lifting 
$j$ to an object of $\gerbe{G}(X)$.

\begin{proof}
Assume $j$ lifts to an object $i \in \opn{Ob} \gerbe{G}(X)$.
So there exists some isomorphism
$h \in \gerbe{H}(X)(F(i), j)$.
In Construction \ref{const1} we may choose
$i_k := i|_{U_k} \in \opn{Ob} \gerbe{G}(U_k)$. 
Having done so, we take
\[ h_k := h|_{U_k} \in \gerbe{H}(U_k)(F(i_k), j) . \]
Proceeding with the construction, we get
\[ h_{k_0, k_1} = 1 \in 
\gerbe{G}(U_{k_0, k_1})(F(i), F(i)) , \]
which can then be lifted to
\[ g_{k_0, k_1} = 1 \in \gerbe{G}(U_{k_0, k_1})(i, i)  . \]
The resulting $2$-cocycle $c = \{ g_{k_0, k_1, k_2} \}$ is trivial.

Conversely, suppose $\opn{cl}^2_F(j) = 1$. From 
construction \ref{const1} and the choices made there we get a a 
$2$-cocycle $c = \{ g_{k_0, k_1, k_2} \}$ with values in $\mcal{N}$,
on some open covering $\bsym{U}$. By replacing $\bsym{U}$ with a suitable
refinement, we may assume it is a coboundary. Namely there is a $1$-cochain 
$b = \{ f_{k_0, k_1} \}$ with values in $\mcal{N}$, such that 
$c = \d (b)$. 

Consider the isomorphisms
\[ g'_{k_0, k_1} := g_{k_0, k_1} \circ f_{k_0, k_1}^{-1}
\in \gerbe{G}(U_{k_0, k_1})(i_{k_0}, i_{k_1}) , \] 
where $g_{k_0, k_1}$ are the isomorphisms chosen when constructing the cocycle
$c$. 
Then $\{ g_{k_0, k_1}' \}$ is a $1$-cocycle. Since $\gerbe{G}$ is a 
stack, the collection of objects $\{ i_k \}_{k \in K}$ can be glued. I.e.\
there is an object
$i \in \opn{Ob} \gerbe{G}(X)$, and isomorphisms
$g'_k \in \gerbe{G}(U_{k})(i_{k}, i)$,
such that
\[ g_{k_1}'^{-1} \circ g_{k_0}' = g_{k_0, k_1}'  . \]
Define
\[ e_{k} := F(g'_k) \circ h_k^{-1} \in 
\gerbe{H}(U_k) \bigl( j, F(i) \bigr) . \]
Then one checks that 
\[ e_{k_0} = e_{k_1} \in \gerbe{H}(U_{k_0, k_1}) \bigl(j, F(i) \bigr) . \]
The sheaf property says that these glue to an isomorphism
$e \in \gerbe{H}(X) \bigl( j, F(i) \bigr)$.
\end{proof}

\begin{rem}
If we were to use open hypercoverings in Construction \ref{const1},
then the obstruction class $\opn{cl}^2_F(j)$ would always be defined,
as an element of $\mrm{H}^2(X, \mcal{N})$. However the technicalities
involved in proving the corresponding version of Theorem \ref{thm.2}
would be enormous. Since Construction \ref{const1} works in the cases
that interest us, we chose to limit ourselves to this weaker
approach.
\end{rem}

\begin{rem}
L. Breen [private communication] proposed looking at the
the central extension of gerbes (\ref{eqn:5}) in the following way:
$\gerbe{G}$ is a gerbe over $\gerbe{H}$, with band $\mcal{N}$. 
Perhaps this point of view can yield a stronger version of
Theorem \ref{thm.2}.
\end{rem}
