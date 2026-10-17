---
doc_id: arxiv-1007.1250v4
doc_title: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES"
section_id: sec-004-4-multiplicative-integration-in-dimension-two
section_title: "Multiplicative Integration in Dimension Two"
section_number: 4
pages: 51-71
source_pdf: 1007.1250v4.pdf
source_sha256: 541ba4fb3068de8b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.979
doc_brief: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES — We construct a 2-dimensional twisted nonabelian multiplicative integral."
---
\label{sec.MI}

We pass up to dimension $2$. Here it turns out that things are
really much more complicated, for geometrical reasons.

A rudimentary multiplicative integration on surfaces was already
introduced by Schlesinger in 1928, in his
nonabelian $2$-dimensional Stokes Theorem
(see \cite[Appendix A.II,9]{DF}).
However we need stronger results, for which a more complicated
multiplicative integration procedure is required.

It turns out (this was already in Schlesinger's work) that the correct
multiplicative integral is twisted: there is a $2$-form, say $\beta$,
that is integrated, but this integration is twisted by a $1$-form
$\alpha$. The geometric cycles on which integration is performed are
the kites, to be defined now.


\subsection{Kites} \label{subsec:kites}
By a {\em pointed polyhedron} $(X, x_0)$ we mean a polyhedron $X$
(see Section \ref{sec:pws}), together with a base point $x_0 \in X$.
As base point for $\mbf{I}^2$ we always take the vertex
$v_0$; cf.\ (\ref{eqn:1}). 

\begin{dfn}
Let $(X, x_0)$ be a pointed polyhedron.
\index{Quadrangular kite}
\begin{enumerate}
\item A {\em quadrangular kite} in $(X, x_0)$ is a pair $(\sigma, \tau)$, where
$\sigma$ is a string in $X$ (see Definition \ref{dfn:3}), and 
$\tau : \mbf{I}^2 \to X$
is a linear map. The conditions are that
$\sigma(v_0) = x_0$ and
$\sigma(v_1) = \tau(v_0)$.

\item If $\tau(\mbf{I}^{2})$ is $2$-dimensional then we call $(\sigma, \tau)$
a {\em nondegenerate kite}. 

\item If $\tau(\mbf{I}^{2})$ is a square in $X$ (of positive size), then we
call $(\sigma, \tau)$ a {\em square kite}.
\end{enumerate} 
\end{dfn}

See Figure \ref{fig:1} for illustration. 

Until Section \ref{sec:simpl}, where triangular kites are introduced, we shall
only encounter quadrangular kites. Hence is Sections
\ref{sec.MI}-\ref{sec:stokes-3} a kite shall always mean a quadrangular kite.

Consider a kite $(\sigma, \tau)$. The image $\tau(\mbf{I}^{2})$ 
is a parallelogram in $X$. We denote the area of 
$\tau(\mbf{I}^{2})$ by $\opn{area}(\tau)$. 
If $\tau(\mbf{I}^{2})$ is a square, then we denote the side of this square by
$\opn{side}(\tau)$. 

We view $(\mbf{I}^2, v_0)$ as an oriented pointed polyhedron.
Suppose $(\sigma, \tau)$ is a nondegenerate kite in $(\mbf{I}^2, v_0)$.
If the orientation of $\tau$ is positive, then we say that the kite
$(\sigma, \tau)$ is positively oriented.

We shall need the following composition operation on kites.
Suppose $(\sigma_1, \tau_1)$ is a kite in $(X, x_0)$, and 
$(\sigma_2, \tau_2)$ is  a kite in $(\mbf{I}^2, v_0)$. 
Then 
$\tau_1 \circ \tau_2 : \mbf{I}^{2} \to X$ 
is a linear map, and 
$\sigma_1 * (\tau_1 \circ \sigma_2)$
is a string in $X$. (See (\ref{eqn12}) for the concatenation
operation $\ast$.) We define
\begin{equation} \label{eqn:18}
(\sigma_1, \tau_1) \circ (\sigma_2, \tau_2) :=
\bigl( \sigma_1 \ast (\tau_1 \circ \sigma_2), \tau_1 \circ \tau_2 \bigr) ,
\end{equation}
which is also a kite in $(X, x_0)$.  
Note that this composition operation is associative.
For an illustration see Figures \ref{fig:1} and \ref{fig:2}.

\begin{figure} 
\includegraphics[scale=0.25]{fig1.jpg}
\caption{A linear quadrangular kite $(\sigma, \tau)$ in the pointed polyhedron
$(X, x_0)$, and a linear quadrangular kite $(\sigma', \tau')$ in the pointed
polyhedron $(\mbf{I}^{2}, v_0)$.} 
\label{fig:1}
\end{figure}

\begin{figure} 
\includegraphics[scale=0.23]{fig2.jpg}
\caption{Continued from Figure \ref{fig:1}: the linear quadrangular kite 
$(\sigma, \tau) \circ (\sigma', \tau')$ 
in the pointed polyhedron $(X, x_0)$.} 
\label{fig:2}
\end{figure}

Let $(\sigma, \tau)$ be a kite in $(X, x_0)$, and let 
$f : (X, x_0) \to (Y, y_0)$ be a piecewise linear map 
between pointed polyhedra. Assume that the restriction of $f$ to the 
subpolyhedron $\tau(\mbf{I}^2) \subset X$ is linear. 
As in formula (\ref{eqn14}) we have a string 
$f \circ \sigma$ in $Y$. We define 
\begin{equation} \label{eqn:116}
f \circ (\sigma, \tau) := (f \circ \sigma, f \circ \tau) ,
\end{equation}
which is a kite in $(Y, y_0)$.

Given a kite $(\sigma, \tau)$ in $(X, x_0)$, its {\em boundary} 
is the closed string $\partial (\sigma, \tau)$ defined as follows.
First we define
\begin{equation} \label{eqn:126}
\partial \mbf{I}^2 := 
(v_0, v_1) \ast (v_1, (1, 1)) \ast 
((1, 1), v_2) \ast (v_2, v_0) \, . 
\end{equation}
This is a closed string in $\mbf{I}^2$, based at $v_0$. Next we let
$\partial \tau := \tau \circ (\partial \mbf{I}^2)$,
where composition is in the sense of (\ref{eqn14}). 
So $\partial \tau$ is a closed string in $X$. Finally  we define
\begin{equation}
\partial (\sigma, \tau) :=
\sigma \ast (\partial \tau) \ast \sigma^{-1} , 
\end{equation}
where $\sigma^{-1}$ is the inverse string from (\ref{eqn13}).
See Figure \ref{fig:23}.

\begin{figure}
\includegraphics[scale=0.23]{fig23.jpg}
\caption{The boundary 
$\partial (\sigma, \tau) = \sigma * \partial \tau * \sigma^{-1}$ 
of the kite
$(\sigma, \tau)$ from Figure \ref{fig:1}.} 
\label{fig:23}
\end{figure}

Here is a useful fact about the geometry of kites.

\begin{prop} \label{prop:14}
Let $(\sigma, \tau)$ be a kite in $(X, x_0)$. Then there is a square kite
$(\sigma', \tau')$ in $(\mbf{I}^{2}, v_0)$, and a piecewise linear map of
pointed polyhedra
$f : (\mbf{I}^{2}, v_0) \to (X, x_0)$, 
such that $\opn{len}(\sigma') \leq 1$, 
$f$ is linear on $\tau'(\mbf{I}^{2})$, and 
\[ (\sigma, \tau) = f \circ (\sigma', \tau') \]
as kites in $(X, x_0)$.
\end{prop}

\begin{proof}
Say $\sigma = (\sigma_1, \ldots, \sigma_m)$ is the decomposition of $\sigma$
into pieces. 
If $m = 0$ (i.e.\ $\sigma$ is the empty string), then
we let $\sigma'$ also be the empty string, and we take
$\tau' := \opn{id}_{\mbf{I}^{2}}$ and $f := \tau$.

Otherwise, if $m > 0$, then we define the square kite 
$(\sigma', \tau')$ in $(\mbf{I}^{2}, v_0)$ as follows. 
The square map $\tau' : \mbf{I}^{2} \to \mbf{I}^{2}$ is defined on vertices by
the formula
\[ \tau'(v_0, v_1, v_2) := \bigl( (\smfrac{1}{2}, \smfrac{1}{2}), 
(1, \smfrac{1}{2}), (\smfrac{1}{2}, 1) \bigr) . \]
And we let
$Y := \tau'(\mbf{I}^{2})$. 

Next consider the oriented line segment $Z$ going from $v_0$ to 
$(\smfrac{1}{2}, \smfrac{1}{2})$. We divide $Z$ into $m$ equal pieces,
labeled $Z_1, \ldots, Z_m$. We let $\sigma'_i : \mbf{I}^{1} \to Z$
be the positively oriented linear map with image $Z_i$. 
And we let $\sigma'$ be the string 
$\sigma' := (\sigma'_1, \ldots, \sigma'_m)$.

The map $f|_{Y}$ is defined to be the unique linear map $Y \to X$ such that 
$f \circ \tau' = \tau$. And for every $i$ the map $f|_{Z_i}$ defined to be the
unique piecewise linear map $Z_i \to X$ such that 
$f \circ \sigma'_i = \sigma_i$. 
We thus have a map 
$f|_{Y \cup Z} : Y \cup Z \to X$; see Figure \ref{fig:67} for an illustration.

Finally let $g : \mbf{I}^{2} \to Y \cup Z$ be any piecewise linear retraction;
for instance as suggested by Figure \ref{fig:43}.
We define 
$f := f|_{Y \cup Z} \circ g : \mbf{I}^{2} \to X$. 
See Figure \ref{fig:42}.
\end{proof}

\begin{figure}
\includegraphics[scale=0.35]{fig67.jpg}
\caption{The map
$f|_{Y \cup Z} : Y \cup Z \to X$, where
$Z = Z_1 \cup Z_2 \cup Z_3$.} 
\label{fig:67}
\end{figure}

\begin{figure}
\includegraphics[scale=0.34]{fig43.jpg}
\caption{A piecewise linear retraction
$g : \mbf{I}^{2} \to Y \cup Z$.} 
\label{fig:43}
\end{figure}

\begin{figure}
\includegraphics[scale=0.35]{fig42.jpg}
\caption{The piecewise linear map
$f := f|_{Y \cup Z} \circ g$, and the kite $(\sigma', \tau')$ such that 
$f \circ (\sigma', \tau') = (\sigma, \tau)$.} 
\label{fig:42}
\end{figure}



\newpage

\subsection{Binary Tessellations of $\mbf{I}^2$} \label{subsec:bintes}
For $k \geq 0$ the {\em $k$-th binary subdivision of $\mbf{I}^2$} is the
cellular subdivision $\opn{sd}^k \mbf{I}^2$ of $\mbf{I}^2$ into $4^k$ squares,
each of side $(\smfrac{1}{2})^k$.
The $1$-skeleton of $\opn{sd}^k \mbf{I}^2$ is the set 
$\opn{sk}_1 \opn{sd}^k \mbf{I}^2$ 
consisting of the union of all edges (i.e.\
$1$-cells) in $\opn{sd}^k \mbf{I}^2$. Thus $\opn{sk}_1 \opn{sd}^k \mbf{I}^2$
is a grid.
See Figure \ref{fig:22}. 

\begin{figure}
\includegraphics[scale=0.22]{fig22.jpg}
\caption{The $1$-st binary subdivision $\opn{sd}^1 \mbf{I}^2$ of
$\mbf{I}^2$. Here $w := (\smfrac{1}{2} , \smfrac{1}{2})$.}
\label{fig:22}
\end{figure}


\begin{dfn}
Let $k$ be a natural number.
\begin{enumerate}
\item Let $p = 0, 1, 2$. 
A linear map $\sigma : \mbf{I}^{p} \to \mbf{I}^{2}$
is said to be {\em patterned on $\opn{sd}^k \mbf{I}^2$}
if the image $\sigma(\mbf{I}^{p})$ is  a $p$-cell of  
$\opn{sd}^k \mbf{I}^2$.

\item  A string $\sigma = (\sigma_1, \ldots, \sigma_m)$ in $\mbf{I}^{2}$
is said to be patterned on $\opn{sd}^k \mbf{I}^2$
if each piece $\sigma_i : \mbf{I}^{1} \to \mbf{I}^{2}$ is a linear map patterned
on $\opn{sd}^k \mbf{I}^2$.

\item A square kite $(\sigma, \tau)$ in $(\mbf{I}^{2}, v_0)$ is said to be 
patterned on $\opn{sd}^k \mbf{I}^2$ if both the linear map $\tau$ and the
string $\sigma$ are patterned on $\opn{sd}^k \mbf{I}^2$.
\end{enumerate}
\end{dfn}

The fundamental group 
of the topological space $\opn{sk}_1 \opn{sd}^k \mbf{I}^2$, based at
$v_0$, is denoted by
$\bsym{\pi}_1 (\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$.
It is a free group on $4^k$ generators.
Given a closed string $\sigma$ patterned on 
$\opn{sd}^k \mbf{I}^2$ and based at
$v_0$, we denote by $[\sigma]$ the corresponding element of
$\bsym{\pi}_1 (\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$.
In particular, if $(\sigma, \tau)$ is a kite patterned on 
$\opn{sd}^k \mbf{I}^2$, then the
boundary $\partial (\sigma, \tau)$ represents an element 
\[ [\partial (\sigma, \tau)] \in 
\bsym{\pi}_1 (\opn{sk}_1 \opn{sd}^k \mbf{I}^2) . \]

Recall the boundary $\partial \mbf{I}^2$ from equation (\ref{eqn:126}).

\begin{dfn} \label{dfn:4}
Let $k$ be a natural number.
A {\em tessellation of $\mbf{I}^{2}$ patterned on $\opn{sd}^k \mbf{I}^2$} is a
sequence
\[ \bsym{\rho} = \bigl( (\sigma_1, \tau_1), \ldots, 
(\sigma_{4^k}, \tau_{4^k}) \bigr) \]
of kites in $(\mbf{I}^{2}, v_0)$, satisfying these two
conditions:
\begin{enumerate}
\rmitem{i} Each kite  $(\sigma_i, \tau_i)$ is patterned on 
$\opn{sd}^k \mbf{I}^2$.
\rmitem{ii} One has
\[ \prod_{i = 1}^{4^k} \ [\partial (\sigma_i, \tau_i)] = 
[\partial \mbf{I}^{2}] \]
in the group $\bsym{\pi}_1 (\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$.
The product is according to the convention (\ref{eqn:6}). 
\end{enumerate}
\end{dfn}

\begin{rem}
Suppose $\bsym{\rho}$ is a tessellation of $\mbf{I}^{2}$ patterned on 
$\opn{sd}^k \mbf{I}^2$. Then, in the notation of the definition, each kite 
$(\sigma_i, \tau_i)$ is positively oriented, and 
each $2$-cell of $\opn{sd}^k \mbf{I}^2$ occurs as
$\tau_i(\mbf{I}^{2})$ for exactly one index $i$.

This assertion (that we will not use in the paper) can be proved directly, by a
topological argument. But it also follows from
Corollary \ref{cor:2}, by taking the abelian Lie groups $G := 1$ and $H :=
\mrm{GL}_1(\R)$, and the differential forms
$\alpha := 0$ and 
$\beta := f \cdot \d t_1 \wedge \d t_1$, where 
$f : \mbf{I}^{2} \to \R$ is a smooth nonnegative bump
function supported in the interior of a given $2$-cell of 
$\opn{sd}^k \mbf{I}^2$.
\end{rem}

The {\em probe} is the string 
\begin{equation} \label{eqn:237}
\sigma_{\mrm{pr}} := \bigl( v_0, (0, \smfrac{1}{2}) \bigr) * 
\bigl( (0, \smfrac{1}{2}), (\smfrac{1}{2}, \smfrac{1}{2}) \bigr) 
\end{equation}
(with two pieces) in $\mbf{I}^2$. 
See Figure \ref{fig:73} for an illustration and Remark \ref{rem:4} for an
explanation.

\begin{figure}
\includegraphics[scale=0.20]{fig73.jpg}
\caption{The probe $\sigma_{\mrm{pr}}$ in $\mbf{I}^2$. Here 
$w := (\smfrac{1}{2}, \smfrac{1}{2})$.} 
\label{fig:73}
\end{figure}

\begin{dfn} \label{dfn:14}
\index{Binary tessellation of the square}
Let $k$ be a natural number. The {\em $k$-th binary tessellation of
$\mbf{I}^{2}$} is the sequence
\[ \opn{tes}^k \mbf{I}^2 = 
\bigl( \opn{tes}^k_1 \mbf{I}^2, \ldots, \opn{tes}^k_{4^k} \mbf{I}^2  \bigr)
= \bigl( (\sigma^k_1, \tau^k_1), \ldots, (\sigma^k_{4^k}, \tau^k_{4^k}) \bigr)
\] 
of kites in $(\mbf{I}^{2}, v_0)$, patterned on $\opn{sd}^k \mbf{I}^2$, that is
 defined recursively as follows. 
\begin{enumerate}
\item For $k = 0$ let $\sigma^0_1$ be the empty string, and let
$\tau^0_1$ be the identity map of $\mbf{I}^{2}$.

\item For $k = 1$ all four strings $\sigma^1_i$ are the same; they are
$\sigma^1_i := \sigma_{\mrm{pr}}$. The four linear maps 
$\tau^1_i : \mbf{I}^{2} \to \mbf{I}^{2}$ 
are patterned on $\opn{sd}^1 \mbf{I}^2$, positively oriented, and have
$\tau^1_i(v_0) = (\smfrac{1}{2}, \smfrac{1}{2})$. 
It remains to specify the points $\tau^1_i(v_1)$:
\[ \tau^1_1(v_1) = (\smfrac{1}{2}, 0) , \
\tau^1_2(v_1) = (1, \smfrac{1}{2}) , \
\tau^1_3(v_1) = (\smfrac{1}{2}, 1) , \
\tau^1_4(v_1) = (0, \smfrac{1}{2}) . \]

\item For $k \geq 2$ we define
\[ \opn{tes}^k \mbf{I}^2 :=
(\opn{tes}^1 \mbf{I}^2) \circ (\opn{tes}^{k-1} \mbf{I}^2) . \]
Here composition of sequences of kites is using the
operations (\ref{eqn:18}) and (\ref{eqn:19}).
\end{enumerate}
\end{dfn}

See Figures \ref{fig:24} and \ref{fig:25} for an illustration.

\begin{figure}
\includegraphics[scale=0.36]{fig24.jpg}
\caption{The $1$-st binary tessellation $\opn{tes}^{1} \mbf{I}^{2}$.
The arrowheads indicate the orientation of the linear maps.} 
\label{fig:24}
\end{figure}

\begin{figure}
\includegraphics[scale=0.22]{fig25.jpg}
\caption{The kite $(\sigma^{2}_7, \tau^{2}_7)$ in 
$\opn{tes}^{2} \mbf{I}^{2}$.} 
\label{fig:25}
\end{figure}

It is clear that sequence $\opn{tes}^k \mbf{I}^2$ is a tessellation of
$\mbf{I}^{2}$ patterned on $\opn{sd}^k \mbf{I}^2$, in the sense of Definition 
\tup{\ref{dfn:4}}.
We call $(\sigma^0_1, \tau^0_1)$ the {\em basic kite}.

Hopefully there will be no confusion between the linear map 
$\sigma^k_i$ belonging $\opn{tes}^k \mbf{I}^1$, and the string 
$\sigma^k_i$ belonging $\opn{tes}^k \mbf{I}^2$; these are distinct objects that
share the same notation. 

An easy calculation shows that
\begin{equation} \label{eqn:127}
\opn{len}(\sigma^k_i) \leq 2
\end{equation}
for all $k$ and $i$.

\begin{dfn} \label{dfn:44}
Let $(\sigma, \tau)$ be a kite in $(X, x_0)$. For $k \in \N$ and 
$i \in \{ 1, \ldots, 4^k \}$ let
\[ \opn{tes}^k_i (\sigma, \tau) := (\sigma, \tau) \circ \opn{tes}^k_i \mbf{I}^2
= (\sigma, \tau) \circ (\sigma^k_i, \tau^k_i) , \]
which is also a kite in $(X, x_0)$.
The sequence of kites
\[ \opn{tes}^k (\sigma, \tau) := 
\bigl( \opn{tes}^k_1 (\sigma, \tau), \ldots, 
\opn{tes}^k_{4^k} (\sigma, \tau) \bigr) \]
is called the {\em $k$-th binary tessellation} of $(\sigma, \tau)$.
\end{dfn}

\begin{rem}
The choice of strings for the kites in the binary tessellations (and
the ordering of the kites) is clearly artificial, and also very
asymmetrical. As we shall see later, in favorable situations this
will not matter at all -- any other tessellation works! See
Corollary \ref{cor:2}.
\end{rem}


\subsection{Additive Twisting and Riemann Products} \label{subsec:rp}
Let $\h$ be a finite dimensional vector space (over $\R$). We denote by
$\opn{GL}(\h)$ the group of linear automorphisms of $\h$, which is a Lie group
(noncanonically isomorphic to $\opn{GL}_d(\R)$ for $d := \opn{dim} \h$).

\begin{dfn} \label{dfn:5}
\index{Twisting setup}
A {\em twisting setup} is the data 
$\mbf{C} = (G, H, \Psi_{\h})$, consisting of:
\begin{enumerate}
\item Lie groups $G$ and $H$, with Lie algebras $\g$ and $\h$ respectively.

\item A map of Lie groups
$\Psi_{\h} : G \to \opn{GL}(\h)$, called an {\em additive twisting}.
\end{enumerate}
\end{dfn}

Warning: we do not assume that the map
$\Psi_{\h}(g) : \h \to \h$, for $g \in G$,
is an automorphism of Lie algebras!

\begin{exa}
Let $G$ be any Lie group. Take $H := G$ and
$\Psi_{\h} := \opn{Ad}_{\h}$, the adjoint action of $H = G$ on its Lie algebra.
Then $(G, H, \Psi_{\h})$ is a twisting setup. Here $\Psi_{\h}(g)$ is in
fact an automorphism of Lie groups.
\end{exa}

Let us fix, for the rest of this section, a twisting setup
$\mbf{C} = (G, H, \Psi_{\h})$. 
The Lie algebras of $G$ and $H$ are $\g$ and $\h$ respectively. 

We choose some euclidean norm $\norm{-}_{\g}$ on the vector space $\g$.
As in Section \ref{sec:expon} we also choose an open neighborhood $V_0(G)$ of
$1$ in $G$ on which $\log_G$ is well-defined, a convergence radius
$\epsilon_0(G)$, and a commutativity constant $c_0(G)$. Likewise we choose
$\norm{-}_{\h}$, $V_0(H)$, $\epsilon_0(H)$ and $c_0(H)$.
Given $g \in G$, the linear operator $\Psi_{\h}(g) \in \opn{End}(\h)$ is given
the operator norm $\norm{\Psi_{\h}(g)}$.
It should be noted that these choices are auxiliary only, and do not effect
the definition of the multiplicative integration.

Piecewise smooth differential forms were discussed in Subsection
\ref{subsec:pws}. The string $\sigma_{\mrm{pr}}$ (the probe) was introduced in 
(\ref{eqn:237}).

\begin{dfn}[Basic Riemann Product] \label{dfn:11}
Let $(X, x_0)$ be a pointed polyhedron, let
\[ \alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g , \] 
let
\[ \beta \in \Omega^2_{\mrm{pws}}(X) \otimes \h ,  \]
and let $(\sigma, \tau)$ be a kite in $(X, x_0)$.
We define an element
\[ \opn{RP}_0(\alpha, \beta \vert \sigma, \tau) \in H , \]
called the {\em basic Riemann product of $(\alpha, \beta)$ on 
$(\sigma, \tau)$}, as follows. Write
$Z := \tau(\mbf{I}^2)$ and $z := \tau(\smfrac{1}{2}, \smfrac{1}{2}) \in Z$. 
There are two cases to consider:
\begin{enumerate}
\item Assume $\opn{dim} Z = 2$ and $z$ is a smooth point of the form 
$\beta|_Z$. Put on $Z$ the orientation compatible with $\tau$. 
Choose a triangle $Y$ in $Z$ such that $z \in \opn{Int} Y$ and 
$\beta|_Y$ is smooth, and let 
$\til{\beta} \in \mcal{O}(Y) \otimes \h$
be the coefficient of $\beta|_Y$ with respect to the orientation form of $Y$
(see Definition \ref{dfn:24}). Also let 
\[ g := \opn{MI}(\alpha \vert \sigma * (\tau \circ \sigma_{\mrm{pr}})) \in G .
\]
We define
\[ \opn{RP}_0(\alpha, \beta \vert \sigma, \tau) := 
\exp_H \bigl( \opn{area}(Z) \cdot \Psi_{\h}(g)(\til{\beta}(z)) \bigr)  . \]

\item If $\opn{dim} Z < 2$, or $\opn{dim} Z = 2$ and $z$ is a singular point of
$\beta|_Z$, we define
\[ \opn{RP}_0(\alpha, \beta \vert \sigma, \tau) := 1   . \]
\end{enumerate}
\end{dfn}

It is obvious that case (1) of the definition is independent of the triangle
$Y$. See Figure \ref{fig:74} for an illustration. 

\begin{figure}
\includegraphics[scale=0.31]{fig74.jpg}
\caption{Calculating $\opn{RP}_0(\alpha, \beta \vert \sigma, \tau)$ in the
smooth case. Here $Z = \tau(\mbf{I}^2)$, 
$z = \tau(\smfrac{1}{2}, \smfrac{1}{2})$, and $Y$ is a triangle
in $Z$ such that $\beta|_Y$ is smooth.} 
\label{fig:74}
\end{figure}

\begin{rem} \label{rem:4}
We call the string $\sigma_{\mrm{pr}}$ ``the probe'' because it reaches into
the middle of the square $\mbf{I}^2$. The ``reading'' it gives, namely the
formula for $\opn{RP}_0(\alpha, \beta \vert \sigma, \tau)$ in part (1) of the
definition above, is better than (\ref{eqn:238}), because it converges to the
limit faster: order of $\opn{side}(\tau)^4$ versus $\opn{side}(\tau)^3$.
Cf.\ Lemma \ref{lem:5} below.
\end{rem}

Suppose we are given a finite sequence of kites
\[ \bsym{\rho} =  
\bigl( (\sigma_1, \tau_1), \ldots, (\sigma_m, \tau_m) \bigr) \]
in $(X, x_0)$. We write
\begin{equation} \label{eqn:128}
\opn{RP}_{0} (\alpha, \beta \vert \bsym{\rho}) :=
\prod_{i = 1}^{m} \,
\opn{RP}_{0} \bigl( \alpha , \beta \vert \sigma_i, \tau_i \bigr) . 
\end{equation}

Recall the binary tessellation $\opn{tes}^k (\sigma, \tau)$ from Definition
\ref{dfn:44}.

\begin{dfn}[Refined Riemann Product]
\index{Refined Riemann product}
Let $(X, x_0)$ be a pointed polyhedron, let
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$, let
$\beta \in \Omega^2_{\mrm{pws}}(X) \otimes \h$, and let
$(\sigma, \tau)$ be a kite in $(X, x_0)$.
For $k \geq 0$ we define 
\[ \opn{RP}_{k}(\alpha, \beta \vert \sigma, \tau) :=
\opn{RP}_{0} \bigl( \alpha, \beta \vert \opn{tes}^k (\sigma , \tau) \bigr) = 
\prod_{i = 1}^{4^k} \,
\opn{RP}_{0} \bigl( \alpha, \beta \vert (\sigma, \tau) \circ 
(\sigma^k_i, \tau^k_i) \bigr) . \]
\end{dfn}

\begin{lem} \label{lem:38}
Let $f : (X', x'_0) \to (X, x_0)$ be a piecewise linear map of pointed
polyhedra,
and let $(\sigma', \tau')$ be a kite in $(X', x'_0)$. Assume that $f$ is linear
on $\tau'(\mbf{I}^2)$, and let
\[ (\sigma, \tau) := f \circ (\sigma', \tau') , \] 
which is a kite in $(X, x_0)$.
Let $\alpha' := f^*(\alpha)$ and 
$\beta' := f^*(\beta)$. Then
\[ \opn{RP}_k(\alpha, \beta \vert \sigma, \tau) = 
\opn{RP}_k(\alpha', \beta' \vert \sigma', \tau') \]
for any $k \geq 0$.
\end{lem}

\begin{proof}
Take $k \geq 0$ and $i \in \{ 1, \ldots, 4^k \}$.
We will prove that 
\begin{equation} \label{eqn:149}
 \opn{RP}_0(\alpha, \beta \vert (\sigma, \tau) \circ 
(\sigma^k_i, \tau^k_i)) = 
\opn{RP}_0(\alpha', \beta' \vert (\sigma', \tau') \circ 
(\sigma^k_i, \tau^k_i)) .
\end{equation}

Let $Z := \tau(\mbf{I}^2) \subset X$
and $Z' := \tau'(\mbf{I}^2) \subset X'$.
If $\opn{dim} Z < 2$ then 
$\beta|_{Z} = 0$ and $\beta'|_{Z'} = 0$, and hence both sides of
(\ref{eqn:149}) equal $1$. 

If $\opn{dim} Z = 2$ then the linear map 
$f|_{Z'} : Z' \to Z$ is bijective. Let
$w := (\smfrac{1}{2}, \smfrac{1}{2}) \in \mbf{I}^2$,
$z_i := (\tau \circ \tau^k_i)(w) \in Z$ and 
$z'_i := (\tau' \circ \tau^k_i)(w) \in Z'$.
Then $z_i$ is a smooth point of $\beta|_Z$ if and only if 
$z'_i$ is a smooth point of $\beta'|_{Z'}$. In the singular case again 
both sides of (\ref{eqn:149}) equal $1$. 

In the smooth case we know (by Proposition \ref{prop:12}) that
\[ \opn{MI}(\alpha \vert \sigma * (\tau \circ \sigma^k_i) *  
(\tau \circ \tau^k_i \circ \sigma_{\mrm{pr}})) = 
\opn{MI}(\alpha' \vert \sigma' * (\tau' \circ \sigma^k_i) *  
(\tau' \circ \tau^k_i \circ \sigma_{\mrm{pr}})) . \]
This says the twistings are the same. 
Let $\til{\beta}_i$ be the coefficient of $\beta$ near $z_i$, as in
case (1) of Definition \ref{dfn:11}; and let $\til{\beta}'_i$ be 
the coefficient of $\beta'$ near $z'_i$. Then
\[ \opn{area}(Z_i) \cdot \til{\beta}_i(z_i) =  
\opn{area}(Z'_i) \cdot \til{\beta}'_i(z'_i) . \]
So in this case we also get equality in (\ref{eqn:149}).
\end{proof}





\subsection{Convergence of Riemann Products}
We continue with the setup of Subsection \ref{subsec:rp}.
Fix differential forms
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$ and
$\beta \in \Omega^2_{\mrm{pws}}(X) \otimes \h$.

\begin{lem} \label{lem:4}
There are constants $c_1(\alpha, \beta)$ and
$\epsilon_1(\alpha, \beta)$ with the following properties.
\begin{enumerate}
\rmitem{i} The inequalities below hold:
\begin{gather*}
1 \leq c_1(\alpha, \beta) \\
0 < \epsilon_1(\alpha, \beta) \leq 1 \\
\epsilon_1(\alpha, \beta) \cdot c_1(\alpha, \beta)
\leq \smfrac{1}{4} \epsilon_0(H) \, .
\end{gather*}

\rmitem{ii} Suppose $(\sigma, \tau)$ is a square kite in $(X, x_0)$
such that 
$\opn{side}(\tau) < \epsilon_1(\alpha, \beta)$
and
$\opn{len}(\sigma) \leq 4 \cdot \opn{diam}(X)$.
Then for any $k \geq 0$ one has  
\[ \opn{RP}_{k}(\alpha, \beta \vert \sigma, \tau) \in V_0(H) \]
and
\[ \Norm{ \opn{log}_H \bigl( \opn{RP}_{k}(\alpha, \beta \vert \sigma, \tau)
\bigr) } \leq 
c_1(\alpha, \beta) \cdot \opn{side}(\tau)^2 \, . \]
\end{enumerate}
\end{lem}

\begin{proof}
Let $w := (\smfrac{1}{2}, \smfrac{1}{2}) \in \mbf{I}^2$.
Given a square kite $(\sigma, \tau)$, let 
$Z := \tau(\mbf{I}^2)$, $z := \tau(w)$ and $\epsilon := \opn{side}(\tau)$.

For $i \in \{ 1 ,\ldots, 4^k \}$ define 
\begin{equation} \label{eqn:150}
(\sigma_i, \tau_i) := (\sigma, \tau) \circ (\sigma^k_i, \tau^k_i) . 
\end{equation}
This is a square kite in $(X, x_0)$ satisfying
$\opn{side}(\tau_i) = (\smfrac{1}{2})^k  \epsilon$
and
$\opn{area}(\tau_i) = (\smfrac{1}{4})^k \epsilon^2$.
Let 
$Z_i := \tau_i(\mbf{I}^2)$ and $z_i := \tau_i(w)$.  
see Figures \ref{fig:60} and \ref{fig:61} for illustration. 
Since $\opn{len}(\sigma^k_i) \leq 2$ and 
$\epsilon \leq \opn{diam}(X)$, we have 
\begin{equation} \label{eqn:151}
\opn{len}(\sigma_i * (\tau_i \circ \sigma_{\mrm{pr}})) = 
\opn{len}(\sigma) + \epsilon \cdot \opn{len}(\sigma^k_i) 
+ (\smfrac{1}{2})^k  \epsilon 
\leq 7 \cdot \opn{diam}(X) .
\end{equation}

\begin{figure}
\includegraphics[scale=0.22]{fig60.jpg}
\caption{The kite $(\sigma, \tau)$ in $(X, x_0)$ and the 
 points $z_1, \ldots, z_{4^k}$ in $\tau(\mbf{I}^{2})$. Here 
$k = 1$.} 
\label{fig:60}
\end{figure}

\begin{figure}
\includegraphics[scale=0.22]{fig61.jpg}
\caption{The kite $(\sigma_2, \tau_2)$ in $(X, x_0)$.} 
\label{fig:61}
\end{figure}

Consider the group elements
\[ g_i := \opn{MI}(\alpha \vert \sigma_i * (\tau_i \circ \sigma_{\mrm{pr}})) \in
G \]
and
\[ h_i := \opn{RP}_0(\alpha, \beta \vert \sigma_i, \tau_i) \in H . \]
By definition of the Riemann product we have
\[ \opn{RP}_k(\alpha, \beta \vert \sigma, \tau) = 
\prod_{i = 1}^{4^k} \, h_i . \]

Take $i \in \{ 1 ,\ldots, 4^k \}$. If $z_i$ is a smooth point of 
$\beta|_{Z}$ (this is the good case), then let $\til{\beta}_i$ be the
coefficient of $\beta|_Z$ near $z_i$, and let
\[ \lambda_i := (\smfrac{1}{4})^k \cdot \epsilon^2 \cdot
\Psi_{\h}(g_i)(\til{\beta}_i(z_i)) \in \h . \]
Otherwise, if  $z_i$ is a singular point of $\beta|_{Z}$ (this is the bad
case), then we let $\lambda_i := 0$. In any case, by definition we have
$h_i = \exp_H(\lambda_i)$.

According to Proposition \ref{prop:4} and the inequality (\ref{eqn:151})
we have 
\[ \norm{\Psi_{\h}(g_i)} \leq 
\exp \, \bigl( c_4(\alpha, \Psi_{\h}) \cdot
7 \cdot \opn{diam}(X) \bigr)  \]
for some constant $c_4(\alpha, \Psi_{\h})$. Note that this bound is
independent of $k$ and $(\sigma, \tau)$.

Let
\[ c := \exp \, \bigl( c_4(\alpha, \Psi_{\h}) \cdot
7 \cdot \opn{diam}(X) \bigr) \cdot  \norm{\beta}_{\mrm{Sob}} + 1 , \]
\[ \epsilon_1(\alpha, \beta) := \epsilon_0(H)^{\smfrac{1}{2}}  
\cdot c^{-\smfrac{1}{2}}  \]
and
\[ c_1(\alpha, \beta) := c \cdot \bigl( c_0(H) + 1 \bigr) . \]
Now assume our kite satisfies $\epsilon < \epsilon_1(\alpha, \beta)$. 
Because 
$\norm{\til{\beta}_i(z_i)} \leq \norm{\beta}_{\mrm{Sob}}$
in the good case, and $\lambda_i = 0$ in the bad case, we see that 
\begin{equation*} \label{eqn:104}
\norm{\lambda_i} \leq (\smfrac{1}{4})^k \cdot \epsilon^2 \cdot c
< (\smfrac{1}{4})^k \cdot \epsilon_0(H) .
\end{equation*}
Hence 
$\sum_{i = 1}^{4^k} \norm{\lambda_i} < \epsilon_0(H)$, 
and by property (ii) of Theorem \ref{thm:6} we can deduce that
\[ \prod\nolimits_{i = 1}^{4^k} \, h_i \in V_0(H) \]
and
\[ \Norm{ \log_H \bigl( \prod\nolimits_{i = 1}^{4^k} \, h_i \bigr) }
\leq c_0(H) \cdot \bigl( \sum\nolimits_{i = 1}^{4^k} \, \norm{\lambda_i} \bigr)
\leq c_0(H) \cdot \epsilon^2 \cdot c 
\leq c_1(\alpha, \beta) \cdot \epsilon^2 \, . \]
\end{proof}

\begin{lem} \label{lem:5}
There are constant $\epsilon_2(\alpha, \beta)$ and
$c_2(\alpha, \beta)$ with the following properties:
\begin{itemize}
\rmitem{i} $c_2(\alpha, \beta) \geq c_1(\alpha, \beta)$ and
$0 < \epsilon_2(\alpha, \beta) \leq \epsilon_1(\alpha, \beta)$.

\rmitem{ii} Suppose $(\sigma, \tau)$ is a square kite in $(X, x_0)$ such that 
$\beta|_{\tau(\mbf{I}^{2})}$ is smooth,
$\opn{side}(\tau) < \epsilon_2(\alpha, \beta)$ and
$\opn{len}(\sigma) \leq 4 \cdot \opn{diam}(X)$. Then 
\[ \Norm{ \opn{log}_H \bigl( \opn{RP}_{k}(\alpha, \beta \vert \sigma, \tau)
\bigr) -
\opn{log}_H \bigl( \opn{RP}_{0}(\alpha, \beta \vert \sigma, \tau)
\bigr) } \leq 
c_2(\alpha, \beta) \cdot \opn{side}(\tau)^4  \]
for every $k \geq 0$.
\end{itemize}
\end{lem}

The exponent $4$ in ``$\opn{side}(\tau)^4$'' in the inequality above will be of
utmost importance later on. On the other hand, the factor $4$ appearing in
``$4 \cdot \opn{diam}(X)$'' is quite arbitrary (any number bigger than $2$ would
probably do just as well). 

\begin{proof}
Let $w := (\smfrac{1}{2}, \smfrac{1}{2}) \in \mbf{I}^2$.
Suppose $(\sigma, \tau)$ is some square kite in $(X, x_0)$. Write
$Z:= \tau(\mbf{I}^2)$, $z_0 := \tau(w) \in Z$ and 
$\epsilon := \opn{side}(Z)$. Assume that $\epsilon > 0$ and 
$\beta|_Z$ is smooth (otherwise there is nothing to prove). 
Put on $Z$ the orientation compatible with $\tau$. 

Let $\til{\beta} \in \mcal{O}(Z) \otimes \h$ be the coefficient of $\beta|_Z$,
as in Definition \ref{dfn:24}. Let
\[ g_0 := \opn{MI}(\alpha \vert \sigma * (\tau \circ \sigma_{\mrm{pr}})) \in G ,
\]
and 
\begin{equation*} \label{eqn:157}
\lambda_0 := \epsilon^2 \cdot \Psi_{\h}(g_0)(\til{\beta}(z_0)) \in \h .
\end{equation*}
So by definition
\[ \exp_H(\lambda_0) = \opn{RP}_0(\alpha, \beta \vert \sigma, \tau) . \]

Suppose $\pi$ is some string in $Z$, with initial point $z_0$. Let
$z$ be the terminal point of $\pi$.  
See Figure \ref{fig:76}.

\begin{figure}
\includegraphics[scale=0.18]{fig76.jpg}
\caption{A string $\pi$ in $Z = \tau(\mbf{I}^2)$, with initial point 
$z_0$ and terminal point $z$.} 
\label{fig:76}
\end{figure}

We shall need the following variant of
the Taylor expansion of $\til{\beta}(z)$ to second order around $z_0$:
\begin{equation*} \label{eqn:152}
\til{\beta}(z) = \til{\beta}(z_0) +  
\int_{\pi} (\d \til{\beta})(z_0) + \opn{R}^2(\til{\beta}, \pi) .
\end{equation*}
Here 
$\d \til{\beta} \in \Omega^1(Z) \otimes \h$, 
and 
$(\d \til{\beta})(z_0) \in \Omega^1_{\mrm{const}}(Z) \otimes \h$
is the associated constant form (see Definition \ref{dfn:26}). Thus 
$\int_{\pi} (\d \til{\beta})(z_0)$ is the linear term in the expansion -- it
depends linearly on $\pi$. And the quadratic remainder term 
$\opn{R}^2(\til{\beta}, \pi) \in \h$ has this bound:
\[ \norm{ \opn{R}^2(\til{\beta}, \pi) } \leq
\norm{ \beta }_{\mrm{Sob}} \cdot \opn{len}(\pi)^2 \, . \]
Therefore we get the estimate
\begin{equation} \label{eqn:154}
\Norm{ \til{\beta}(z) - \bigl( \til{\beta}(z_0) +  
\int_{\pi} (\d \til{\beta})(z_0) \bigr) } \leq
\norm{ \beta }_{\mrm{Sob}} \cdot \opn{len}(\pi)^2 \, . 
\end{equation}

Next let
\[ g := \opn{MI}(\alpha \vert \pi) \in G  \]
and 
\[ \alpha' := \opn{Lie}(\Psi_{\h})(\alpha) \in 
\Omega^1_{\mrm{pws}}(X) \otimes \opn{End}(\h) . \]
Assume that
$\opn{len}(\pi) < \epsilon_5(\alpha, \Psi_{\h})$. 
According to Proposition \ref{prop:21} we have this estimate for the operator
$\Psi_{\h}(g) \in \opn{End}(\h)$:
\begin{equation} \label{eqn:153}
\Norm{ \Psi_{\h}(g) - \bigl( \bsym{1} + \int_{\pi} \alpha'(z_0) \bigr) }
\leq c_5(\alpha, \Psi_{\h}) \cdot \opn{len}(\pi)^2 \, . 
\end{equation}
And by Proposition \ref{prop:13} we have the bound
\begin{equation} \label{eqn:155}
\Norm{ \Psi_{\h}(g) } \leq \exp( c_4(\alpha, \Psi_{\h}) \cdot 
\epsilon_5(\alpha, \Psi_{\h})) \, . 
\end{equation}

By combining inequalities (\ref{eqn:154}), (\ref{eqn:153}) and (\ref{eqn:155}),
we see that there exists a constant 
$c(\alpha, \beta)$ such that 
\begin{equation} \label{eqn:156}
\begin{aligned}
& \Norm{ \Psi_{\h}(g)(\til{\beta}(z)) - 
\Bigl( \til{\beta}(z_0) + \bigl( \int_{\pi} \alpha'(z_0) \bigl)
(\til{\beta}(z_0)) +  
\int_{\pi} (\d \til{\beta})(z_0) \Bigr) } \\
& \qquad \leq 
c(\alpha, \beta) \cdot \opn{len}(\pi)^2 \, . 
\end{aligned} 
\end{equation}
This holds for every string $\pi$ in $Z$ with 
$\opn{len}(\pi) < \epsilon_5(\alpha, \Psi_{\h})$,
$\pi(v_0) = z_0$ and $\pi(v_1) = z$.

Now take $k \geq 0$. For any index 
$i \in \{ 1, \ldots, 4^k \}$ 
let $\pi_i$ be the unique string in $Z$ such that
\[ (\tau \circ \sigma_{\mrm{pr}}) * \pi_i = 
(\tau \circ \sigma^k_i) * (\tau \circ \tau^k_i \circ \sigma_{\mrm{pr}}) \]
as strings. This is a string with initial point $z_0$, and with 
terminal point
\[ z_i := (\tau \circ \tau^k_i)(w) . \]
Notice that for $i \leq 2^k$ the strings $\pi_i$ and $\pi_{2^k + i}$
are reflections of each other relative to the point $z_0$. 
See Figure \ref{fig:77}.

\begin{figure}
\includegraphics[scale=0.28]{fig77.jpg}
\caption{The strings $\pi_1$ and $\pi_3$ in $Z$. Here $k = 1$.} 
\label{fig:77}
\end{figure}

Define
\[  g_i := \opn{MI}(\alpha \vert \pi_i) \in G  \]
and
\[ \lambda_i := (\smfrac{1}{4})^k \cdot \epsilon^2 \cdot
\Psi_{\h}(g_0 \cdot g_i)(\til{\beta}(z_i)) \in \h . \]
So we have
\[ \exp_H(\lambda_i) = 
\opn{RP}_0(\alpha, \beta \vert (\sigma, \tau) \circ (\sigma^k_i, \tau^k_i) ) .
\]
And the bound for $\lambda_i$ is 
\begin{equation} \label{eqn:159}
\norm{ \lambda_i } \leq (\smfrac{1}{4})^k \cdot \epsilon^2 \cdot 
c'(\alpha, \beta) \, ,
\end{equation}
where we write
\[ c'(\alpha, \beta) :=  \exp( c_4(\alpha, \Psi_{\h}) \cdot 
7 \cdot \opn{diam}(X) ) \cdot \norm{ \beta }_{\mrm{Sob}} + 1  \, . \]
Using the abbreviation
\[ \gamma := \epsilon^2 \cdot \Psi_{\h}(g_0)(\d \til{\beta}) \in 
\Omega^1_{\mrm{pws}}(Z) \otimes \h , \]
formula (\ref{eqn:156}), and the inequality
$\opn{len}(\pi_i) \leq \epsilon$, we obtain
\begin{equation} \label{eqn:158}
\begin{aligned}
& \Norm{ \lambda_i - (\smfrac{1}{4})^k \cdot 
\Bigl( \lambda_0 + \bigl( \int_{\pi_i} \alpha'(z_0) \bigl)
(\lambda_0) +  \int_{\pi_i} \gamma(z_0) \Bigr) } \\
& \qquad \leq 
c(\alpha, \beta) \cdot (\smfrac{1}{4})^k \cdot \epsilon^4 \, . 
\end{aligned} 
\end{equation}
For this to be true we should assume that 
$\epsilon < \epsilon_5(\alpha, \Psi_{\h})$.

Let us set
\[ \epsilon_2(\alpha, \beta) := 
\min \bigl( \epsilon_1(\alpha, \beta), \, 
c'(\alpha, \beta)^{- 1/2} \cdot \epsilon_0(H)^{1/2} , \,
\epsilon_5(\alpha, \Psi_{\h}) \bigl) \, , \]
We now assume furthermore that 
$\epsilon < \epsilon_2(\alpha, \beta)$.
In particular, from (\ref{eqn:159}) we obtain 
\[ \sum_{i = 1}^{4^k} \, \norm{ \lambda_i } \leq \epsilon_0(H) \, . \]
We know that
\[ \prod_{i = 1}^{4^k} \, \exp_H(\lambda_0) = 
\opn{RP}_k(\alpha, \beta \vert \sigma, \tau) . \]
Therefore we can use property (ii) of Theorem \ref{thm:6} to deduce that
\[ \Norm{ \log_H \bigl( \opn{RP}_k(\alpha, \beta \vert \sigma, \tau) \bigr) 
- \sum_{i = 1}^{4^k} \, \lambda_i } \leq
c_0(H) \cdot \epsilon^4 \cdot c'(\alpha, \beta)^2 \, . \]
The geometric symmetry of the sequence of strings $\pi_1. \ldots, \pi_{4^k}$
implies that
\[ \bigl( \int_{\pi_i} \alpha'(z_0) \bigl)(\lambda_0) = 
- \bigl( \int_{\pi_{2^k + i}} \alpha'(z_0) \bigl)(\lambda_0) \]
for $i \leq 2^k$; and therefore 
\[ \sum_{i = 1}^{4^k} \, \bigl( \int_{\pi_i} \alpha'(z_0) \bigl)(\lambda_0) 
= 0 . \]
Similarly 
\[ \sum_{i = 1}^{4^k} \, \int_{\pi_i} \gamma(z_0) = 0 . \]
Plugging in the estimate (\ref{eqn:158}) we obtain 
\[  \Norm{ \sum_{i = 1}^{4^k} \, \lambda_i - \lambda_0 } \leq 
c(\alpha, \beta) \cdot \epsilon^4 \, . \]
We see that the constant 
\[ c_2(\alpha, \beta) := c(\alpha, \beta) + 
c_0(H) \cdot c'(\alpha, \beta)^2 + c_1(\alpha, \beta) \, . \]
works.
\end{proof}

\begin{dfn}
Let us fix constants $\epsilon_2(\alpha, \beta)$ and
$c_2(\alpha, \beta)$ as in Lemma \ref{lem:5}.
A square kite $(\sigma, \tau)$ in $(X, x_0)$
will be called {\em $(\alpha, \beta)$-tiny} in this section if 
\[ \opn{side}(\tau) < \epsilon_2(\alpha, \beta) \]
and 
\[ \opn{len}(\sigma) \leq 4 \cdot \opn{diam}(X) \,  . \]
\end{dfn}

\begin{dfn} \label{dfn:45}
Let $(\sigma, \tau)$ be a nondegenerate kite in $(X, x_0)$. 
For $k \in \N$ and $i \in \{ 1, \ldots, 4^k \}$ let 
$Z_i := (\tau \circ \tau^k_i)(\mbf{I}^2) \subset X$. 
An index $i$ is called {\em good} if the forms
$\alpha|_{Z_i}$ and $\beta|_{Z_i}$ are smooth. Otherwise $i$ is called {\em
bad}. The sets of good and bad indices are denoted by 
$\opn{good}(\tau, k)$ and $\opn{bad}(\tau, k)$ respectively.
\end{dfn}

\begin{lem} \label{lem:51}
Let $Z$ be a $2$-dimensional subpolyhedron of $X$. There exist constants
$a_0(\alpha, \beta, Z)$ and $a_1(\alpha, \beta, Z)$ such that for any 
nondegenerate kite $(\sigma, \tau)$ in $(X, x_0)$ with 
$\tau(\mbf{I}^2) \subset Z$, one has
\[ \abs{ \opn{bad}(\tau, k) } \leq 
a_0(\alpha, \beta, Z) + a_1(\alpha, \beta, Z) \cdot 2^k \, . \]
\end{lem}

\begin{proof} 
Let $Z_1, \ldots, Z_m$ be line segments in $Z$ such that 
the singular locus of $\alpha$ and the singular locus of $\beta$ are
contained in $\bigcup_{j = 1}^m Z_j$. Take
$a_0(\alpha, \beta, Z) := 2 m$ and 
$a_1(\alpha, \beta, Z) := 2 \cdot \sum_{j = 1}^m \, \opn{len} (Z_j)$.
\end{proof}

\begin{lem} \label{lem:6}
Let $Z$ be a $2$-dimensional subpolyhedron of $X$.  Then there is a constant
$c_3(\alpha, \beta, Z) \geq 0$, such that for any 
$(\alpha, \beta)$-tiny kite $(\sigma, \tau)$ satisfying
$\tau(\mbf{I}^2) \subset Z$, and any $k' \geq k \geq 0$, one has
\[ \begin{aligned}
& \Norm{ \opn{log}_H \bigl( \opn{RP}_{k'}(\alpha, \beta \vert 
\sigma, \tau) \bigr) -
\opn{log}_H \bigl( \opn{RP}_{k}(\alpha, \beta \vert \sigma, \tau) \bigr) } \\
& \qquad \leq (\smfrac{1}{4})^k \cdot c_3(\alpha, \beta, Z) \cdot 
\opn{side}(\tau)^2  \, .
\end{aligned}  \]
\end{lem}

\begin{proof}
Let $(\sigma, \tau)$ an $(\alpha, \beta)$-tiny kite such that 
$\tau(\mbf{I}^2) \subset Z$. Write $\epsilon := \opn{side}(\tau)$. For 
$i \in \{ 1 ,\ldots, 4^k \}$ let $(\sigma_i, \tau_i)$ be as in equation
(\ref{eqn:150}), and let $Z_i := \tau_i(\mbf{I}^2) \subset Z$. 
Note that 
$\opn{side}(Z_i) = (\smfrac{1}{2})^k \cdot \epsilon$.

Let $l := k' - k$. If $i \in \opn{good}(\tau, k)$, then by Lemma 
\ref{lem:5} we know that
\[ \Norm{ \opn{log}_H \bigl( \opn{RP}_{l}(\alpha, \beta \vert 
\sigma_i, \tau_i) \bigr) -
\opn{log}_H \bigl( \opn{RP}_{0}(\alpha, \beta \vert \sigma_i, \tau_i)
\bigr) } \leq 
c_2(\alpha, \beta) \cdot ((\smfrac{1}{2})^k \cdot \epsilon)^4 \, . \]
If $i \in \opn{bad}(\tau, k)$, then by Lemma \ref{lem:4} we know that
\[ \Norm{ \opn{log}_H \bigl( \opn{RP}_{l}(\alpha, \beta \vert 
\sigma_i, \tau_i) \bigr) -
\opn{log}_H \bigl( \opn{RP}_{0}(\alpha, \beta \vert \sigma_i, \tau_i)
\bigr) } \leq 
2 c_1(\alpha, \beta) \cdot ((\smfrac{1}{2})^k \cdot \epsilon)^2 \, . \]
Therefore by property (iv) of Theorem \ref{thm:6}
and Lemma \ref{lem:51}  we have
\[ \begin{aligned}
& \Norm{ \opn{log}_H \bigl( \opn{RP}_{k'}(\alpha, \beta \vert 
\sigma, \tau) \bigr) -
\opn{log}_H \bigl( \opn{RP}_{k}(\alpha, \beta \vert \sigma, \tau) \bigr) } \\
& \qquad =
\Norm{ \opn{log}_H \bigl( 
\prod\nolimits_{i = 1}^{4^k} \, 
\opn{RP}_{l}(\alpha, \beta \vert \sigma_i, \tau_i \bigr) -
\opn{log}_H \bigl( 
\prod\nolimits_{i = 1}^{4^k} \, 
\opn{RP}_{0}(\alpha, \beta \vert \sigma_i, \tau_i \bigr) } \\
& \qquad \leq c_0(H) \cdot \bigl(
\abs{ \opn{good}(\tau, k) } \cdot c_2(\alpha, \beta) \cdot 
(\smfrac{1}{2})^{4 k} \cdot \epsilon^4 \\
& \qquad \qquad +
\abs{ \opn{bad}(\tau, k) } \cdot 2 c_1(\alpha, \beta) \cdot 
(\smfrac{1}{2})^{2 k} \cdot \epsilon^2 \bigr) \\
& \qquad \leq c_3(\alpha, \beta, Z) \cdot (\smfrac{1}{2})^k \cdot \epsilon^2 
\end{aligned} \]


where we take (very generously)
\[ c_3(\alpha, \beta, Z) := c_0(H) \cdot \bigl( c_2(\alpha, \beta) +
2 (a_0(\alpha, \beta, Z) + a_1(\alpha, \beta, Z)) \cdot c_1(\alpha, \beta)
\bigr) . \]
\end{proof}

\begin{thm} \label{thm:12}
Let $(X, x_0)$ be a pointed polyhedron, let
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$, let
$\beta \in \Omega^2_{\mrm{pws}}(X) \otimes \h$, and let
$(\sigma, \tau)$ be a kite in $(X, x_0)$. 
Then the limit
\[ \lim_{k \to \infty} \, \opn{RP}_{k}(\alpha, \beta \vert  \sigma, \tau)
\]
exists in $H$.
\end{thm}

\begin{proof}
According to Proposition \ref{prop:14} and Lemma \ref{lem:38} we can assume
that $(X, x_0) = (\mbf{I}^2, v_0)$ and 
$\opn{len}(\sigma) \leq 1$. 

Take $k$ large enough such that for each $i \in \{ 1, \ldots, 4^k \}$
the kite $(\sigma_i, \tau_i)$, in the notation of (\ref{eqn:150}), 
is $(\alpha, \beta)$-tiny. For any $k' \geq 0$ we have
\[ \opn{RP}_{k + k'} (\alpha, \beta \vert  \sigma, \tau) = 
\prod_{i = 1}^{4^k}  \, \opn{RP}_{k'}
(\alpha, \beta \vert  \sigma_i, \tau_i) . \]
Thus it suffices to prove that for any $i$ the limit
\[ \lim_{k' \to \infty} \opn{RP}_{k'}(\alpha, \beta \vert  \sigma_i, \tau_i) \]
exists. Now Lemma \ref{lem:6} says that the sequence 
\[ \bigl( \opn{RP}_{k'}(\alpha, \beta \vert  \sigma_i, \tau_i) 
\bigr)_{k' \geq 0} \]
is a Cauchy sequence in $H$; and therefore it converges.
\end{proof}

\begin{dfn}[Multiplicative Integral] \label{dfn:16}
\index{Multiplicative integral on kites}
Let $(G, H, \Psi_{\h})$ be a twisting setup, let
$(X, x_0)$ be a pointed polyhedron, let
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$, let
$\beta \in \Omega^2_{\mrm{pws}}(X) \otimes \h$, and let
$(\sigma, \tau)$ be a kite in $(X, x_0)$. We define the
{\em multiplicative integral of $\beta$ twisted by
$\alpha$ on $(\sigma, \tau)$} to be
\[ \opn{MI}(\alpha, \beta \vert \sigma, \tau) :=
 \lim_{k \to \infty} \, \opn{RP}_{k}(\alpha, \beta \vert  \sigma, \tau)
\in H . \]

If $(X, x_0) = (\mbf{I}^{2}, v_0)$ then we write
\[  \opn{MI}(\alpha, \beta \vert \mbf{I}^{2}) :=
 \opn{MI}(\alpha, \beta \vert \sigma^0_1, \tau^0_1) , \]
where $(\sigma^0_1, \tau^0_1)$ is the basic kite.
\end{dfn}



\subsection{Some Properties of $\opn{MI}$}
We continue with the setup of the previous subsections.

\begin{prop} \label{prop:3}
In the situation of Definition \tup{\ref{dfn:16}}, for any $k \geq 0$ one
has
\[ \opn{MI}(\alpha, \beta \vert \sigma, \tau) =
\prod_{i = 1}^{4^k} \,
\opn{MI} \bigl( \alpha, \beta \vert (\sigma, \tau) \circ 
(\sigma^k_i, \tau^k_i) \bigr) . \]
\end{prop}

\begin{proof}
For any $k' \geq 0$ we have
\[ \opn{RP}_{k + k'}(\alpha, \beta \vert \sigma, \tau) =
\prod_{i = 1}^{4^k} \,
\opn{RP}_{k'} \bigl( \alpha, \beta \vert (\sigma, \tau) \circ 
(\sigma^k_i, \tau^k_i) \bigr) . \]
Now take the limit $\lim_{k' \to \infty}$.
\end{proof}

\begin{prop} \label{prop:8}
Consider the situation of Definition \tup{\ref{dfn:16}}, and assume that 
$(\sigma, \tau)$ is an $(\alpha, \beta)$-tiny kite.
\begin{enumerate}
\item One has
\[ \opn{MI}(\alpha, \beta \vert \sigma, \tau) \in V_0(H) , \]
and
\[ \Norm{ \opn{log}_H \bigl( \opn{MI}(\alpha, \beta \vert \sigma, \tau)
\bigr) } \leq 
c_1(\alpha, \beta) \cdot \opn{side}(\tau)^2 \, . \]

\item If $\beta|_{\tau(\mbf{I}^{2})}$ is smooth then 
\[ \Norm{ \opn{log}_H \bigl( \opn{MI}(\alpha, \beta \vert 
\sigma, \tau) \bigr) -
\opn{log}_H \bigl( \opn{RP}_{0}(\alpha, \beta \vert \sigma, \tau) \bigr) } 
\leq c_2(\alpha, \beta) \cdot \opn{side}(\tau)^4  \, .
\]

\item Let $Z$ be a $2$-dimensional subpolyhedron of $X$ containing 
$\tau(\mbf{I}^2)$. For any $k \geq 0$ one has
\[ \begin{aligned}
& \Norm{ \opn{log}_H \bigl( \opn{MI}(\alpha, \beta \vert 
\sigma, \tau) \bigr) -
\opn{log}_H \bigl( \opn{RP}_{k}(\alpha, \beta \vert \sigma, \tau) \bigr) } \\
& \quad \leq (\smfrac{1}{2})^k \cdot c_3(\alpha, \beta, Z) \cdot 
\opn{side}(\tau)^2  \, .
\end{aligned} \]
\end{enumerate}
\end{prop}

\begin{proof}
Immediate from Lemmas \ref{lem:4}, \ref{lem:5} and \ref {lem:6}.
\end{proof}

\begin{prop}[Functoriality in $X$] \label{prop:10}
Let $f : (Y, y_0) \to (X, x_0)$ be a piecewise linear map between pointed
polyhedra, let
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$, let
$\beta \in \Omega^2_{\mrm{pws}}(X) \otimes \h$, 
and let $(\sigma, \tau)$ be a kite in $(Y, y_0)$.
Assume that $f$ is linear on $\tau(\mbf{I}^2)$. Then
\[ \opn{MI}(\alpha, \beta \vert f \circ \sigma, f \circ \tau) = 
\opn{MI} \bigl( f^*(\alpha), f^*(\beta) \vert  \sigma, \tau \bigl) . \]
\end{prop}

\begin{proof}
Immediate from Lemma \ref{lem:38}.
\end{proof}

The next proposition says that ``in the tiny scale the $2$-dimensional MI is
abelian''. 

\begin{prop} \label{prop:22}
There are constant $\epsilon_{2'}(\alpha, \beta)$ and
$c_{2'}(\alpha, \beta)$ with the following properties:
\begin{itemize}
\rmitem{i} $c_{2'}(\alpha, \beta) \geq c_2(\alpha, \beta)$ and
$0 < \epsilon_{2'}(\alpha, \beta) \leq \epsilon_2(\alpha, \beta)$.

\rmitem{ii} Suppose $(\sigma, \tau)$ is a square kite in $(X, x_0)$ such that 
$\opn{side}(\tau) < \epsilon_{2'}(\alpha, \beta)$
and
$\opn{len}(\sigma) \leq 4 \cdot \opn{diam}(X)$. 
Let
$g := \opn{MI}(\alpha \vert \sigma) \in G$.
Then 
\[ \Norm{ \opn{log}_H \bigl( \opn{MI}(\alpha, \beta \vert \sigma, \tau)
\bigr) -
\Psi_{\h}(g)\bigl( \int_{\tau} \beta \bigr)  } \leq 
c_{2'}(\alpha, \beta) \cdot \opn{side}(\tau)^3 \, .  \]
\end{itemize}
\end{prop}

Actually with more effort we can get a better estimate (order 
$\opn{side}(\tau)^4$) in property (ii) above. 

\begin{proof}
This is very similar to Proposition \ref{prop:16}.
Take 
\[ \epsilon_{2'}(\alpha, \beta) := \min \bigl( 
\epsilon_{2}(\alpha, \beta), \, \epsilon_{5}(\alpha, \Psi_{\h}) \bigr) \, , \]
where $\epsilon_{5}(\alpha, \Psi_{\h})$ is the constant from Proposition
\ref{prop:21}. 
Let's write $\epsilon := \opn{side}(\tau)$
and $Z := \tau(\mbf{I}^2)$. Assume that 
$\epsilon < \epsilon_{2'}(\alpha, \beta)$. 

Take $k \geq 0$. For $i \in \{ 1, \ldots, 4^k \}$ let
\[ (\sigma_i, \tau_i) := 
(\sigma, \tau) \circ (\sigma^k_i, \tau^k_i) = 
\opn{tes}^k_i (\sigma, \tau) . \]
Write
$Z_i := \tau_i(\mbf{I}^2)$ and $z_i := \tau_i(w)$, where
$w := (\smfrac{1}{2}, \smfrac{1}{2}) \in \mbf{I}^2$ as usual. 
The sets $\opn{good}(\tau, k)$ and $\opn{bad}(\tau, k)$ were defined in
Definition \ref{dfn:45}. 

Define 
\[ g'_0 := \opn{MI}(\alpha \vert \tau \circ \sigma_{\mrm{pr}}) \in G , \]
\[ g'_i := \opn{MI}(\alpha \vert 
(\tau \circ \sigma^k_i) * (\tau \circ \tau^k_i \circ \sigma_{\mrm{pr}})) \]
and 
\[ \lambda_i :=  \opn{log}_H \bigl( 
\opn{RP}_0(\alpha, \beta \vert \sigma_i, \tau_i) \bigr) \in \h  \]
for $i \in \{ 1, \ldots, 4^k \}$.
{}From Definition \ref{dfn:11} and Proposition \ref{prop:13} we know that
\begin{equation} \label{eqn:195}
\norm{ \lambda_i } \leq (\smfrac{1}{4})^k \cdot \epsilon^2 \cdot 
\norm{\Psi_{\h}(g \cdot g'_i)} \cdot \norm{\beta}_{\mrm{Sob}} 
\leq (\smfrac{1}{4})^k \cdot \epsilon^2 \cdot c  \, ,
\end{equation}
where we let
\[ c := \exp \bigl( c_4(\alpha, \phi) \cdot 6 \opn{diam}(X) \bigl) \cdot 
\norm{\beta}_{\mrm{Sob}} \, . \]
According to property (ii) of Theorem \ref{thm:6} we have
\begin{equation} \label{eqn:193}
\begin{aligned}
& \Norm{ \log_H \bigl( \opn{RP}_k(\alpha, \beta \vert \sigma, \tau) \bigr)
- \bosum_{i = 1}^{4^k} \, \lambda_i } \\
& \qquad \leq c_0(H) \cdot \bigl( \bosum_{i = 1}^{4^k} \norm{ \lambda_i }
\bigr)^2 \leq 
c_0(H) \cdot (\smfrac{1}{4})^{2 k} \cdot \epsilon^4 \cdot c^2  \, .
\end{aligned}
\end{equation}

For $i \in \opn{good}(\tau, k)$ let $\til{\beta}_i$ be the coefficient of 
$\beta|_{Z_i}$. Define 
\[ \mu_i := 
\begin{cases}
(\smfrac{1}{4})^k \cdot \epsilon^2 \cdot 
\Psi_{\h}(g) \bigl( \til{\beta}_i(z_i) \bigr) &
\text{ if } i \text{ is good }, \\
0 & \text{ otherwise} 
\end{cases} \]
and
\[ \opn{RS}_k(\alpha, \beta \vert \sigma, \tau) := 
\sum_{i = 1}^{4^k}\, \mu_i . \]

Now let us compare $\mu_i$ to $\lambda_i$. 
If $i$ is a bad index, then
\[ \norm{ \mu_i - \lambda_i } = \norm{\lambda_i} \leq 
(\smfrac{1}{4})^k \cdot \epsilon^2 \cdot c  \]
by (\ref{eqn:195}). On the other hand, if $i$ is a good index then 
\[ \mu_i = \Psi_{\h}(g \cdot g'_0 \cdot g'^{-1}_i \cdot g^{-1}) (\lambda_i) . \]
By Proposition \ref{prop:13} the operators $\Psi_{\h}(g)$ and
$\Psi_{\h}(g^{-1})$ have known \lb bounds (since the length of the string 
$\sigma$ is bounded by $4 \cdot \opn{diam}(X)$).
Hence there is a bound for the conjugation operator
$\opn{Ad}(\Psi_{\h}(g))$ on $\opn{End}(\h)$. 
And by Proposition \ref{prop:21} there is an estimate for the norm of the
operator 
$\Psi_{\h}(g'_0 \cdot g'^{-1}_i) - \bsym{1}$,
where $\bsym{1}$ denotes the identity operator of $\h$.
Since $\opn{Ad}(\Psi_{\h}(g))$ fixes $\bsym{1}$, we can conclude that 
there is a constant $c'$
(independent of of $(\sigma, \tau)$ or $k$) such that
\[ \begin{aligned}
& \Norm{ \Psi_{\h}(g \cdot g'_0 \cdot g'^{-1}_i \cdot g^{-1}) - \bsym{1} } \\
& \qquad = \Norm{ \opn{Ad}(\Psi_{\h}(g)) \bigl( 
\Psi_{\h}(g'_0 \cdot g'^{-1}_i) - \bsym{1} \bigr) } 
\leq c' \cdot \epsilon \, . 
\end{aligned} \]
Hence using (\ref{eqn:195}) we get
\[ \norm{ \mu_i - \lambda_i } \leq c' \cdot c \cdot
(\smfrac{1}{4})^k \cdot \epsilon^3 \, . \]
Summing over all $i$ we see that
\[ \begin{aligned}
& \Norm{ \bosum_{i = 1}^{4^k} \, \lambda_i - 
\bosum_{i = 1}^{4^k} \, \mu_i } 
\leq \sum_{i = 1}^{4^k} \, \norm{ \mu_i - \lambda_i } \\
& \qquad \leq \abs{\opn{good}(\tau, k)} \cdot 
c' \cdot c \cdot (\smfrac{1}{4})^k \cdot \epsilon^3 +
\abs{\opn{bad}(\tau, k)} \cdot (\smfrac{1}{4})^k \cdot \epsilon^2 \cdot c \\
& \qquad \leq 4^k \cdot c' \cdot c \cdot (\smfrac{1}{4})^k \cdot \epsilon^3 +
(a_0 + a_1 \cdot 2^k)  \cdot
(\smfrac{1}{4})^k \cdot \epsilon^2 \cdot c \, .  
\end{aligned} \]
Here $a_0 := a_0(\alpha, \beta, Z)$ and $a_1 := a_1(\alpha, \beta, Z)$ are the
constants from Lemma \ref{lem:51}. 
Combining this estimate with (\ref{eqn:193}) we obtain
\begin{equation} \label{eqn:196}
\begin{aligned}
& \Norm{ \log_H \bigl( \opn{RP}_k(\alpha, \beta \vert \sigma, \tau) \bigr) - 
\opn{RS}_k(\alpha, \beta \vert \sigma, \tau) } \\
& \qquad \leq 
c_0(H) \cdot (\smfrac{1}{4})^{2 k} \cdot \epsilon^4 \cdot c^2 +
4^k \cdot c' \cdot c \cdot (\smfrac{1}{4})^k \cdot \epsilon^3 \\
& \qquad \qquad +
(a_0 + a_1 \cdot 2^k)  \cdot (\smfrac{1}{4})^k \cdot \epsilon^2 \cdot c \, . 
\end{aligned}
\end{equation}

Finally, by properties of the usual Riemann integration we have
\begin{equation*} \label{eqn:194}
\lim_{k \to  \infty} \opn{RS}_k(\alpha, \beta \vert \sigma, \tau) = 
\Psi_{\h}(g)\bigl( \int_{\tau} \beta \bigr) .
\end{equation*}
Hence in the limit $k \to \infty$ we get
\[ \Norm{ \opn{log}_H \bigl( \opn{MI}(\alpha, \beta \vert \sigma, \tau)
\bigr) -
\Psi_{\h}(g)\bigl( \int_{\tau} \beta \bigr)  } \leq 
c' \cdot c \cdot  \epsilon^3 \, , \]
and we can take
$c_{2'}(\alpha, \beta) := c' \cdot c$.
\end{proof}




\subsection{Transfer of Twisting Setups}

Suppose $H'$ is another Lie group, with Lie algebra $\h'$. 
The vector space of $\R$-linear maps $\h \to \h'$ is denoted by
$\opn{Hom}(\h, \h')$. 
Consider the $\mcal{O}_{\mrm{pws}}(X)$-module 
$\mcal{O}_{\mrm{pws}}(X) \otimes \opn{Hom}(\h, \h')$.
An element 
\[ \phi \in \mcal{O}_{\mrm{pws}}(X) \otimes \opn{Hom}_{\R}(\h, \h') \]
is called a {\em piecewise smooth family of linear maps} from $\h$ to $\h'$.
Indeed, we may view $\phi$ as a piecewise smooth map
\[ \phi : X \to \opn{Hom}(\h, \h') . \]
For any point $x \in X$ there is a linear map
$\phi(x) : \h \to \h'$.

\begin{dfn} \label{dfn:7}
Suppose $\mbf{C} = (G, H, \Psi_{\h})$ and 
$\mbf{C}' = (G', H', \Psi'_{\h'})$ are two twisting
setups. A {\em transfer of twisting setups} from $\mbf{C}$
to $\mbf{C}'$, parametrized by $(X, x_0)$, is the data
\[ \bsym{\Theta}_X = (\Theta_G, \Theta_H, \Theta_{\h, X}) , \] 
consisting of:
\begin{enumerate}
\item Maps of Lie groups
$\Theta_G : G \to G'$ and 
$\Theta_H : H \to H'$.

\item An element
$\Theta_{\h, X} \in \mcal{O}_{\mrm{pws}}(X) \otimes \opn{Hom}(\h, \h')$.
\end{enumerate}

The following condition is required: 
\begin{itemize}
\rmitem{$*$} The equality 
\[ \opn{Lie}(\Theta_H) = \Theta_{\h, X}(x_0) \]
holds in $\opn{Hom}(\h, \h')$.
\end{itemize}

We denote this transfer by
$\bsym{\Theta}_X : \mbf{C} \to \mbf{C}'$.
\end{dfn}

Note that for $x \neq x_0$ the linear map
$\phi(x) : \h \to \h'$ might fail to be a Lie algebra homomorphism.

\begin{dfn} \label{dfn:17}
Let $\bsym{\Theta}_X : \mbf{C} \to \mbf{C}'$ be a transfer of twisting
setups as in Definition \ref{dfn:7}, and let 
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$. 
We say that $\alpha$ is a {\em connection compatible with 
$\bsym{\Theta}_X$} if the following condition, called the
{\em holonomy condition}, holds.
\begin{itemize}
\rmitem{$\Diamond$} Let $\sigma$ be a string in $X$, with
$x_0 = \sigma(v_0)$ and $x_1 := \sigma(v_1)$. Define
\[ g := \opn{MI}(\alpha \vert \sigma) \in G  \]
and $g' := \Theta_G(g) \in G'$.
Then the diagram 
\[ \UseTips \xymatrix @C=9ex @R=5ex {
\h
\ar[d]_{\Theta_{\h, X}(x_0)}
& \h
\ar[d]^{\Theta_{\h, X}(x_1)} 
\ar[l]_{\Psi_{\h}(g)}
\\
\h'
& \h'
\ar[l]^{\Psi'_{\h'}(g')}
} \]
is commutative.
\end{itemize}
\end{dfn}

\begin{rem}
The holonomy condition for $\alpha$ can be stated as a differential equation.
We shall not need this equation in our treatment. 
\end{rem}

Consider a transfer of twisting setups $\bsym{\Theta}_X$ as above. 
The family of linear maps
$\Theta_{\h, X}$ induces, by tensoring, a homomorphism of graded
$\Omega_{\mrm{pws}}(X)$-modules
\begin{equation} \label{eqn:140}
\Theta_{\h, X} : \Omega_{\mrm{pws}}(X) \otimes \h \to 
\Omega_{\mrm{pws}}(X) \otimes \h' .
\end{equation}
Warning: usually $\Theta_{\h, X}$ does not commute with the de Rham operator
$\d$.

\begin{prop}[Functoriality in $\mbf{C}$] \label{prop:2}
Let $\bsym{\Theta}_X : \mbf{C} \to \mbf{C}'$ be a transfer of twisting
setups, let 
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$,
and let 
$\beta \in \Omega^2_{\mrm{pws}}(X) \otimes \h$.
Assume that $\alpha$ is a connection compatible with $\bsym{\Theta}_X$. 
We write
\[ \alpha' := \opn{Lie}(\Theta_G)(\alpha) \in  
\Omega^1_{\mrm{pws}}(X) \otimes \g' \]
and 
\[ \beta' := \Theta_{\h, X}(\beta)  \in  
\Omega^2_{\mrm{pws}}(X) \otimes \h' . \]
Then for every kite $(\sigma, \tau)$ in $(X, x_0)$ one has
\[ \Theta_H \bigl( \opn{MI}(\alpha, \beta \vert \sigma, \tau) \bigr) = 
\opn{MI} \bigl( \alpha', \beta' \vert \sigma, \tau \bigr)  \]
in $H'$.
\end{prop}

\begin{proof}
Consider a kite $(\sigma', \tau')$ in $(\mbf{I}^2, v_0)$ and a piecewise linear
map $f$ like in Proposition \ref{prop:14}. By Proposition \ref{prop:10} we have
\[ \opn{MI}(\alpha, \beta \vert \sigma, \tau) =
\opn{MI} \bigl( f^*(\alpha) , f^*(\beta) \vert \sigma', \tau' \bigr) . \]
On the other hand
$\bigl( \Theta_G, \Theta_H, f^*(\Theta_{\h, X}) \bigr)$ 
is a transfer of twisting setups \lb parametrized by 
$(\mbf{I}^2, v_0)$, and by Proposition \ref{prop:10} we have
\[ \begin{aligned}
& \opn{MI} \bigl( \alpha', \beta' \vert \sigma, \tau \bigr) =
\opn{MI} \bigl( f^*(\alpha'), f^*(\beta') \vert 
\sigma', \tau' \bigr) \\
& \qquad =
\opn{MI} \bigl( \opn{Lie}(\Theta^1)(f^*(\alpha)), f^*(\Theta_{\h,
X})(f^*(\beta)) \vert \sigma', \tau' \bigr) .
\end{aligned} \]
Therefore we can assume that 
$(X, x_0) = (\mbf{I}^2, v_0)$ and $\opn{len}(\sigma) \leq 1$.
Using Proposition \ref{prop:3} we can further assume that 
$(\sigma, \tau)$ is $(\alpha, \beta)$-tiny and $(\alpha', \beta')$-tiny.

Fix $k \geq 0$. 
For $i \in \{ 1, \ldots, 4^k \}$ let
\[ (\sigma_i, \tau_i) := 
(\sigma, \tau) \circ (\sigma^k_i, \tau^k_i) . \]
Define 
\[ g_i := \opn{MI}(\alpha \vert \sigma_i * (\tau_i \circ \sigma_{\mrm{pr}})) \in
G \]
and
\[ g'_i := \opn{MI}(\alpha' \vert \sigma_i * (\tau_i \circ \sigma_{\mrm{pr}}))
\in G' . \]
By Proposition \ref{prop:12} we have
$g'_i = \Theta_G(g_i)$. 
Also define $Z_i := \tau_i(\mbf{I}^2)$ and 
$z_i := \tau_i(\smfrac{1}{2}, \smfrac{1}{2})$.

Suppose that $i \in \opn{good}(\tau, k)$, with notation as in 
Definition \ref{dfn:45}. Then there is a function 
$\til{\beta}_i \in \mcal{O}(Z_i) \otimes \h$,
called the coefficient of $\beta|_{Z_i}$, satisfying
\[ \beta|_{Z_i} = \til{\beta}_i \cdot \d t_1 \wedge \d t_2 . \]
The function 
\[ \til{\beta}'_i := \Theta_{\h, X}(\til{\beta}_i) \in \mcal{O}(Z_i) \otimes
\h' , \]
is then the coefficient of $\beta'|_{Z_i}$.
Note that 
\[  \til{\beta}'_i(z_i) = \Theta_{\h, X}(z_i) \bigl( \til{\beta}(z_i) \bigr) \]
in $\h'$. By condition ($*$) of Definition \ref{dfn:7} and condition
($\Diamond$) of Definition \ref{dfn:17} we have
\[ \begin{aligned}
& \Psi'_{\h'}(g'_i) \bigl( \til{\beta}'_i(z_i) \bigr) = 
\Psi'_{\h'}(g'_i) \bigl(  \Theta_{\h, X}(z_i) \bigl( \til{\beta}_i(z_i) \bigr)
\bigr) \\
& \qquad = \Theta_{\h, X}(x_0) \bigl( \Psi_{\h}(g_i)
\bigl( \til{\beta}_i(z_i) \bigr) \bigr) \\
& \qquad = \opn{Lie}(\Theta_H)
\bigl( \Psi_{\h}(g_i) \bigl( \til{\beta}_i(z_i) \bigr) \bigr) . 
\end{aligned} \]
By definition we have
\[ \opn{RP}_0(\alpha, \beta \vert \sigma_i, \tau_i) = 
\exp_H \bigl( (\smfrac{1}{4})^k \cdot \opn{area}(\tau) \cdot 
\Psi_{\h}(g_i)(\til{\beta}_i(z_i)) \bigr) \]
and
\[ \opn{RP}_0(\alpha', \beta' \vert \sigma_i, \tau_i) = 
\exp_{H'} \bigl( (\smfrac{1}{4})^k \cdot \opn{area}(\tau) \cdot 
\Psi_{\h}(g'_i)(\til{\beta}'_i(z_i)) \bigr) . \]
Since
\[ \exp_{H'} \circ \opn{Lie}(\Theta_H) = \Theta_H \circ \exp_H \]
we conclude that 
\begin{equation} \label{eqn:132}
\opn{RP}_0(\alpha', \beta' \vert \sigma_i, \tau_i) =
\Theta_H \bigl( \opn{RP}_0(\alpha, \beta \vert \sigma_i, \tau_i) \bigr) . 
\end{equation}

Like in Lemma \ref{lem:51} we can find a bound for
$\abs{ \opn{bad}(\tau, k) }$, and like in the proof of Lemma \ref{lem:6}
we can estimate 
\[ \Norm{ \log_{H'} \bigl( \Theta_H \bigl(  
\opn{RP}_0 ( \alpha, \beta \vert \sigma_i, \tau_i)  \bigr) \bigr) -
\log_{H'} \bigl( 
\opn{RP}_0 \bigl( \alpha', \beta' \vert \sigma_i, \tau_i) \bigr) }  \]
when $i \in \opn{bad}(\tau, k)$. 
From these estimates and from (\ref{eqn:132}) 
we conclude that there is a constant $c$, independent of
$k$, such that
\[  \Norm{ \log_{H'} \bigl( \Theta_H \bigl(
\opn{RP}_k ( \alpha, \beta \vert \sigma, \tau)  \bigr) \bigr) -
\log_{H'} \bigl( 
\opn{RP}_k \bigl( \alpha', \beta' \vert \sigma, \tau) \bigr) } 
\leq c \cdot (\smfrac{1}{2})^k \, . \]
In the limit $k \to \infty$ we see that
\[ \Theta_H \bigl( \opn{MI} (\alpha, \beta \vert \sigma, \tau) \bigr) =
\opn{MI} (\alpha', \beta' \vert \sigma, \tau). \]
\end{proof}








\cleardoublepage
