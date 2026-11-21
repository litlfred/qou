---
doc_id: arxiv-1007.1250v4
doc_title: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES"
section_id: sec-008-8-stokes-theorem-in-dimension-three
section_title: "Stokes Theorem in Dimension Three"
section_number: 8
pages: 105-125
source_pdf: 1007.1250v4.pdf
source_sha256: 541ba4fb3068de8b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.972
doc_brief: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES — We construct a 2-dimensional twisted nonabelian multiplicative integral."
---
\label{sec:stokes-3}

The goal of this section is to prove Theorem \ref{thm:10}, which is the first
version of the main result of the paper. (The second version, dealing with the
triangular case, is Theorem \ref{thm:22}.)


\subsection{Balloons and their Boundaries} \label{subsec:ballbound}

\begin{dfn}
Let $(X, x_0)$ be a pointed polyhedron. A {\em linear quadrangular balloon} 
\index{Quadrangular balloon}
in $(X, x_0)$ is a pair $(\sigma, \tau)$, where
$\sigma$ is a string in $X$ (see Definition \ref{dfn:3}), and
$\tau : \mbf{I}^3 \to X$ is a linear map. The conditions are that
$\sigma(v_0) = x_0$ and $\sigma(v_1) = \tau(v_0)$.
\end{dfn}

In other words, a linear quadrangular balloon is the $3$-dimensional version of
a linear quadrangular kite. See Figure \ref{fig:51} for an illustration. 

All balloons in this section are linear quadrangular ones; so we shall
simply call them balloons. (This will change in Section \ref{sec:simpl}.)
If the image of $\tau$ is a cube in $X$, then we call 
$(\sigma, \tau)$ a {\em cubical balloon}. The length of the side of $\tau$ is
denoted by $\opn{side}(\tau)$. If $\opn{side}(\tau) > 0$ then 
$(\sigma, \tau)$ is said to be {\em nondegenerate}.

If $(\sigma, \tau)$ is a balloon in $(X, x_0)$, and
$(\sigma', \tau')$ is a balloon (resp.\ a kite) in $(\mbf{I}^{3}, v_0)$, then 
the composition $(\sigma, \tau) \circ (\sigma', \tau')$
(defined like (\ref{eqn:18})) is a balloon  (resp.\ a kite) in $(X, x_0)$.

The $k$-th binary subdivision of $\mbf{I}^{3}$ is its cellular decomposition 
into $8^k$ little cubes, each of side $(\smfrac{1}{2})^k$. We denote this
decomposition by $\opn{sd}^k \mbf{I}^3$.

A map $\sigma : \mbf{I}^p \to \mbf{I}^3$
is said to be {\em patterned on $\opn{sd}^k \mbf{I}^3$} if it is linear, and
its image is a $p$-cell in $\opn{sd}^k \mbf{I}^3$.
A string $\sigma = (\sigma_1, \ldots, \sigma_n)$ in $(\mbf{I}^{3}, v_0)$ is
said to be patterned on $\opn{sd}^k \mbf{I}^3$ if for every $i$ the map
$\sigma_i : \mbf{I}^1 \to \mbf{I}^3$ is patterned on $\opn{sd}^k \mbf{I}^3$.
A kite or balloon $(\sigma, \tau)$ in $(\mbf{I}^{3}, v_0)$ is said to be
patterned on $\opn{sd}^k \mbf{I}^3$ if the string $\sigma$
and the map $\tau : \mbf{I}^p \to \mbf{I}^3$ ($p = 2, 3$) are patterned on 
$\opn{sd}^k \mbf{I}^3$.

\begin{figure}
\includegraphics[scale=0.27]{fig51.jpg}
\caption{A cubical balloon $(\sigma, \tau)$ in the pointed polyhedron
$(\mbf{I}^3, v_0)$.} 
\label{fig:51}
\end{figure}

The $k$-th binary tessellation of $\mbf{I}^{3}$ is the sequence 
\begin{equation} \label{eqn:141}
\opn{tes}^k \mbf{I}^3 = 
\bigl( \opn{tes}^k_1 \mbf{I}^3, \ldots, \opn{tes}^k_{8^k} \mbf{I}^3 \bigr)
= \bigl( (\sigma^{k}_1, \tau^{k}_1) , \ldots, 
(\sigma^{k}_{8^k}, \tau^{k}_{8^k}) \bigr)
\end{equation}
of balloons patterned on $\opn{sd}^k \mbf{I}^3$, defined as follows.
For $k = 0$ we have the basic balloon
$(\sigma^{0}_1, \tau^{0}_1)$,
where $\sigma^{0}_1$ is the empty string, and 
$\tau^{0}_1 : \mbf{I}^3 \to \mbf{I}^3$
is the identity map. 

For $k = 1$ we choose, once and for all, a sequence 
\[ \opn{tes}^1 \mbf{I}^3 = 
\bigl( (\sigma^{1}_1, \tau^{1}_1) , \ldots, 
(\sigma^{1}_{8}, \tau^{1}_{8}) \bigr) \]
balloons patterned on $\opn{sd}^1 \mbf{I}^3$, satisfying these conditions:
\begin{enumerate}
\rmitem{a}  Each of the
$3$-cells of $\opn{sd}^1 \mbf{I}^3$ occurs exactly once as 
$\tau^{1}_{i}(\mbf{I}^3)$ for some $i$.
\rmitem{b} The maps $\tau^{1}_{i}$ are positively oriented.
\rmitem{c} The length of each string $\sigma^{1}_i$ is at most $3$. 
\end{enumerate}
This can be done of course.

For $k \geq 1$ we use the recursive definition
\[ \opn{tes}^{k+1} \mbf{I}^3 :=  
(\opn{tes}^1 \mbf{I}^3) \circ (\opn{tes}^{k} \mbf{I}^3) . \]
Here we use the convention (\ref{eqn:19}) for composition of sequences.

Given a balloon $(\sigma, \tau)$ in a pointed polyhedron $(X, x_0)$, 
an numbers $k \in \N$, $i \in \{ 1, \ldots, 8^k \}$, let
\begin{equation} \label{eqn:250}
\opn{tes}^{k}_i (\sigma, \tau) := 
(\sigma, \tau) \circ \opn{tes}^{k}_i \mbf{I}^3 = 
(\sigma, \tau) \circ (\sigma^{k}_i, \tau^{k}_i) . 
\end{equation}
The $k$-th binary tessellation of $(\sigma, \tau)$ is the sequence (of length
$8^k$) of balloons 
\begin{equation} \label{eqn:251}
\opn{tes}^{k} (\sigma, \tau) := (\sigma, \tau) \circ (\opn{tes}^{k} \mbf{I}^3)
= \bigl( \opn{tes}^{k}_1 (\sigma, \tau), \ldots, 
\opn{tes}^{k}_{8^k} (\sigma, \tau) \bigr) . 
\end{equation}

\newpage
\begin{dfn}   \label{dfn:36} \mbox{} 
\begin{enumerate}
\item For $i \in \{ 1, \ldots, 6 \}$ let
$\partial_i \mbf{I}^{3} := (\sigma^{\flat}_i, \tau^{\flat}_i)$ 
be the kites depicted in Figure \ref{fig:46}.
The {\em boundary of $\mbf{I}^{3}$} is the sequence of kites
\[ \partial \mbf{I}^3 = 
\bigl( \partial_1 \mbf{I}^{3}, \ldots, \partial_6 \mbf{I}^{3} \bigr) = 
\bigl( (\sigma^{\flat}_1, \tau^{\flat}_1) , \ldots, 
(\sigma^{\flat}_{6}, \tau^{\flat}_{6}) \bigr) . \]

\item Given a balloon $(\sigma, \tau)$ in a pointed polyhedron $(X, x_0)$, 
let
\[ \partial_i (\sigma, \tau) := (\sigma, \tau) \circ \partial_i \mbf{I}^{3}
= (\sigma, \tau) \circ (\sigma^{\flat}_i, \tau^{\flat}_i) . \]
The {\em boundary} of $(\sigma, \tau)$ is the sequence of kites
\[ \partial (\sigma, \tau) := 
\bigl( \partial_1 (\sigma, \tau), \ldots, 
\partial_6 (\sigma, \tau) \bigr)  \]
in  $(X, x_0)$.
\end{enumerate}
\end{dfn}

\begin{figure}
\includegraphics[scale=0.50]{fig46.jpg}

\caption{The kites $(\sigma^{\flat}_i, \tau^{\flat}_i)$,
$i = 1, \ldots, 6$, that make up the boundary of $\mbf{I}^3$.} 
\label{fig:46}
\end{figure}

If $(\sigma, \tau)$ is a balloon in $(\mbf{I}^3, v_0)$
patterned on $\opn{sd}^k \mbf{I}^3$, then 
$\partial (\sigma, \tau)$ is a sequence (of length $6$) of kites  patterned on 
$\opn{sd}^k \mbf{I}^3$, and 
$\partial \partial (\sigma, \tau)$ is a sequence of closed strings patterned on 
$\opn{sd}^k \mbf{I}^3$.

\begin{dfn} \label{dfn:35}
Let $(X, x_0)$ be a pointed polyhedron, let
$\mbf{C} / X$ be a Lie quasi crossed module with additive feedback
over $(X, x_0)$, and
let $(\alpha, \beta)$ be a piecewise smooth connection-curvature pair in 
$\mbf{C} / X$. Given a balloon $(\sigma, \tau)$ in $(X, x_0)$, we define
\[ \opn{MI}(\alpha, \beta \vert \partial(\sigma, \tau)) :=
\prod_{1 = 1}^6 \, \opn{MI}(\alpha, \beta \vert \partial_i(\sigma, \tau))
\in H . \]
\end{dfn}




\subsection{Some Algebraic Topology}
Let us denote by $\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^3)$
the fundamental group of the topological space 
$\opn{sk}_1 \opn{sd}^k \mbf{I}^3$, based at $v_0$. 
If $\sigma$ is a closed string patterned on $\opn{sd}^k \mbf{I}^3$ and based at
$v_0$, then we denote its class in 
$\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^3)$
by $[\sigma]$.

We now look at homology groups. Fix $k \geq 0$. On each $p$-cell $\tau$ in 
$\opn{sd}^k \mbf{I}^3$, $p \in \{0, 1, 2\}$, let us choose an orientation
(there are two options for $p > 0$).  
We denote by $\mrm{C}_p(\opn{sk}_2 \opn{sd}^k \mbf{I}^3)$
the free abelian group based on these oriented cells, called the group of
$p$-chains. 
The direct sum on all $p$ is a complex (with the usual boundary operator), and
the $p$-th homology is the singular homology
$\mrm{H}_p(\opn{sk}_2 \opn{sd}^k \mbf{I}^3)$ of the topological space
$\opn{sk}_2 \opn{sd}^k \mbf{I}^3$. 
The homology class of a cycle $\sum_i n_i \tau_i$ is denoted by
$[\sum_i n_i \tau_i]$.
Observe that a string $\sigma = (\sigma_1, \ldots, \sigma_n)$ patterned on
$\opn{sd}^k \mbf{I}^3$ represents an element
$\sum_i \sigma_i \in \mrm{C}_1(\opn{sk}_2 \opn{sd}^k \mbf{I}^3)$.
And a linear map $\tau : \mbf{I}^2 \to \mbf{I}^3$ patterned on
$\opn{sd}^k \mbf{I}^3$ represents an element
$\tau \in \mrm{C}_2(\opn{sk}_2 \opn{sd}^k \mbf{I}^3)$.

Recall the free monoid with involution $\opn{Wrd}^{\pm 1}(\bsym{s})$ from
Subsection
\ref{subec:freemon}.

\begin{lem} \label{lem:20}
Let 
$\bigl( (\sigma_1, \tau_1), \ldots, (\sigma_n, \tau_n) \bigr)$
be a sequence of kites patterned on $\opn{sk}_2 \opn{sd}^k \mbf{I}^3$, for some
$k \geq 0$. Write
\[ a_i := [\partial (\sigma_i, \tau_i)] \in 
\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^3) . \]
Let $w(\bsym{s}) \in \opn{Wrd}^{\pm 1}(s_1, \ldots, s_n)$ be a word such that
$w(a_1, \ldots, a_n) = 1$. 
Then the  $2$-chain 
\[ w(\tau_1, \ldots, \tau_n) \in \mrm{C}_2(\opn{sk}_2 \opn{sd}^k \mbf{I}^3) \]
is a cycle.
\end{lem}

\begin{proof}
Say $m$ is the number of $1$-cells in $\opn{sd}^k \mbf{I}^3$. 
We choose orientations, and arrange these oriented $1$-cells in a sequence
$(\rho_1, \ldots, \rho_m)$.
For every $i$ let $u_i(\bsym{t}) \in$ 
$\opn{Wrd}^{\pm 1}(t_1, \ldots, t_m)$
be the word such that
\[ \partial (\sigma_i, \tau_i) = u_i(\rho_1, \ldots, \rho_m) \]
as strings patterned on $\opn{sd}^k \mbf{I}^3$.
Define
\[ u(\bsym{t}) := w( u_1(\bsym{t}), \ldots, u_n(\bsym{t})) \in \opn{Wrd}^{\pm 1}
(\bsym{t}) . \]
Then $u(\rho_1, \ldots, \rho_m)$ is a closed string, and its homotopy class is
trivial in the group $\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^3)$.
According to Lemma \ref{lem:15} we have
$u(\bsym{t})  \sim_{\mrm{can}} 1$ in 
$\opn{Wrd}^{\pm 1}(\bsym{t})$.

On the other hand we have 
$\partial(\tau_i) = \partial (\sigma_i, \tau_i)$
as additive $1$-chains, i.e.\ as elements of
$\mrm{C}_1(\opn{sk}_2 \opn{sd}^k \mbf{I}^3)$.
Hence
\[ \partial(w(\tau_1, \ldots, \tau_n)) = 
w(\partial (\sigma_1, \tau_1), \ldots, \partial (\sigma_n, \tau_n))
= u(\rho_1, \ldots, \rho_m) = 0 \]
as elements of $\mrm{C}_2(\opn{sk}_2 \opn{sd}^k \mbf{I}^3)$.
\end{proof}

\begin{lem} \label{lem:21}
Recall the boundary of $\mbf{I}^3$ from Definition \tup{\ref{dfn:36}}.
For any $i$ let
\[ a^{\flat}_i := [\partial (\sigma^{\flat}_{i}, \tau^{\flat}_{i})] \in 
\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^0 \mbf{I}^3) \]
and
\[ b^{\flat}_i := \tau^{\flat}_i \in 
\mrm{C}_2(\opn{sk}_1 \opn{sd}^0 \mbf{I}^3) . \]
Then:
\begin{enumerate}
\item The fundamental group 
$\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^0 \mbf{I}^3)$ is generated by
the sequence of elements
$(a^{\flat}_1, \ldots, a^{\flat}_6)$, 
and there is one relation:
\[  \prod_{i = 1, \ldots, 6} \, a^{\flat}_i = 1 . \]
Thus $\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^0 \mbf{I}^3)$ is a free group
of rank $5$.  

\item The homology group $\mrm{H}_2(\opn{sk}_2 \opn{sd}^0 \mbf{I}^3)$
is a free abelian group of rank $1$, with basis 
$[\sum_{i = 1, \ldots, 6} \, \tau_{i}]$.
\end{enumerate}
\end{lem}

\begin{proof}
This is obvious from looking at the pictures.
\end{proof}

Given a balloon $(\sigma, \tau)$, its boundary 
$\partial(\sigma, \tau)$ is a sequence of $6$ kites, and
$\partial \partial(\sigma, \tau)$ is a sequence of $6$ closed strings.

\begin{lem} \label{lem:22} \mbox{}
\begin{enumerate}
\item The fundamental group 
$\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^1 \mbf{I}^3)$ is generated by
the \linebreak sequence of closed strings 
\[ \partial \partial (\opn{tes}^1 \mbf{I}^3)
= \bigl( \partial \partial (\sigma^{k}_1, \tau^{k}_1) , \ldots, 
\partial \partial (\sigma^{k}_{8^k}, \tau^{k}_{8^k}) \bigr) .
\]
This sequence has length $48$. 
There are $20$ relations, and they are of two kinds:
\begin{enumerate}
\item For any two distinct kites 
$(\sigma_{i}, \tau_{i}), (\sigma_{j}, \tau_{j})$
in $\partial \partial (\opn{tes}^1 \mbf{I}^3)$
such that $\tau_i(\mbf{I}^2) = \tau_j(\mbf{I}^2)$, namely for any of
the $12$ interior faces of $\opn{sd}^1 \mbf{I}^3$, there is a relation
\[ [\partial (\sigma_{i}, \tau_{i})] = [g_i] \cdot
[\partial (\sigma_{j}, \tau_{j})^{-1}] \cdot [g_i^{-1}] \]
for some word $g_i$ in the $48$ generators.

\item For any of the $8$ balloons 
$(\sigma^{k}_i, \tau^{k}_i)$
in $\opn{tes}^1 \mbf{I}^3$ there is a
relation as in Lemma \tup{\ref{lem:21}(1)}.
\end{enumerate}
Thus $\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^1 \mbf{I}^3)$ is a free group
of rank $28$.  

\item The homology group $\mrm{H}_2(\opn{sk}_2 \opn{sd}^1 \mbf{I}^3)$
is a free abelian group of rank $8$, with basis the $8$ boundaries of
the $8$ balloons in $\opn{tes}^1 \mbf{I}^3$.
\end{enumerate}
\end{lem}

\begin{proof}
Use Lemma \ref{lem:21} together with the Van-Campen and Mayer- \lb Vietoris
theorems.
\end{proof}



\subsection{Inert Forms} \label{subsec:inert}
Let $(X, x_0)$ be a pointed polyhedron, and let
\[ \mbf{C} / X = (G, H, \Psi, \Phi_0, \Phi_X) \]
be a Lie quasi crossed module with additive feedback over $(X, x_0)$.
Recall that the additive feedback
$\Phi_X$ is an element of 
$\mcal{O}_{\mrm{pws}}(X) \otimes \opn{Hom}(\h, \g)$, so for any point
$x \in X$ we have a linear function
$\Phi_X(x) : \h \to \g$. 

Suppose $Z \subset X$ is some sub-polyhedron.
As in equation (\ref{eqn:140}), but restricting to $Z$, for every $p$ we have an
$\mcal{O}_{\mrm{pws}}(Z)$-linear homomorphism
\[ \Phi_X|_Z : \Omega^p_{\mrm{pws}}(Z) \otimes \h \to 
\Omega^p_{\mrm{pws}}(Z) \otimes \g . \]
Note that for $p = 0$, an element 
\[ f \in \Omega^0_{\mrm{pws}}(Z) \otimes \h   = 
\mcal{O}_{\mrm{pws}}(Z) \otimes \h \]
is a piecewise smooth function $f : Z \to \h$; and in this case
\[ \Phi_X|_Z(f)(z) = \Phi_X(z)(f(z)) \in \g \]
for any point $z \in Z$. 

\begin{dfn} Let $Z \subset X$ be a subpolyhedron.
\begin{enumerate}
\item A function $f \in \mcal{O}_{\mrm{pws}}(Z) \otimes \h$ is called an {\em
inert function} (relative to $\mbf{C} / X$) if $\Phi_X|_Z(f) = 0$.

\item A form $\gamma \in  \Omega^p_{\mrm{pws}}(Z) \otimes \h$ is called an 
{\em inert $p$-form} \index{Inert form}
(relative to $\mbf{C} / X$) if $\Phi_X|_Z(\gamma) = 0$.
\end{enumerate}
\end{dfn}

Let $\gamma \in \Omega^p_{\mrm{pws}}(X) \otimes \h$.
Choose some linear coordinate system 
$\bsym{s} = (s_1, \ldots, s_n)$ on $X$. Also choose a smoothing triangulation
$\{ X_j \}_{j \in J}$ for $\gamma$; so that 
$\gamma|_{X_j} \in \Omega^p(X_j) \otimes \h$ for every $j$. See Subsection 
\ref{subsec:pws} for details. For each index $j$ let 
$f_{j, \bsym{i}} \in \mcal{O}(X_j) \otimes \h$
be the coefficients of $\gamma|_{X_j}$ relative to $\bsym{s}$, in the sense of
Definition \ref{dfn:27}. Namely
\begin{equation} \label{eqn:222}
\gamma|_{X_j} = \sum_{\bsym{i}} \, f_{j, \bsym{i}} \cdot 
\d s_{i_1} \wedge \cdots \wedge \d s_{i_p} \in 
\Omega^p(X_j) \otimes \h ,
\end{equation}
where $\bsym{i} = (i_1, \ldots, i_p)$ runs over the set of strictly increasing
multi-indices in \lb $\{ 1, \ldots, n \}^p$.

\begin{lem} \label{lem:47}
In the situation above, the following are equivalent:
\begin{enumerate}
\rmitem{i} The form $\gamma \in \Omega^p_{\mrm{pws}}(X) \otimes \h$ is inert.
\rmitem{iii} The functions  
$f_{j, \bsym{i}} \in \mcal{O}(X_j) \otimes \h$ are all inert.
\end{enumerate}
\end{lem}

We omit the easy proof. 

\begin{dfn}
The closed subgroup
\[ H_0 := \opn{Ker}(\Phi_0) \subset H \]
is called the {\em inertia subgroup} (relative to $\mbf{C} / X$).
Its Lie algebra
\[ \h_0 := \opn{Lie}(H_0) = \opn{Ker}(\opn{Lie}(\Phi_0)) \]
is called the {\em inertia subalgebra}.
\end{dfn}

\begin{prop}
The subgroup $H_0$ is central in $H$, and the subalgebra $\h_0$ is central
in $\h$.
\end{prop}

\begin{proof}
Take $h \in H_0$, so $\Phi_0(h) = 1$. By the Pfeiffer condition (i.e.\
condition ($*$) of Definition \ref{dfn:22}) we have
\[ \opn{Ad}_H(h) = \Psi(\Phi_0(h)) = \Psi(1) = \opn{id}_H , \]
which says that 
\[ h \in \opn{Ker}(\opn{Ad}_H) = \opn{Z}(H) . \]

Since $H_0 \subset  \opn{Z}(H)$ it follows that 
\[ \h_0 \subset \opn{Lie}(\opn{Z}(H)) \subset \opn{Z}(\h) . \]
(Note that $H$ could be disconnected, in which case 
$\opn{Z}(\h)$ could be bigger than
$\opn{Lie}(\opn{Z}(H))$.)
\end{proof}

Recall the notion of tame connection (Definition \ref{dfn:46}).

\begin{lem} \label{lem:45}
Let $\alpha$ be a tame connection for $\mbf{C} / X$, let $\sigma$ be a closed
string in $X$ based at $x_0$, and let
$g := \opn{MI}(\alpha \vert \sigma) \in G$. Then for any
$\lambda \in \h_0$ one has
\[ \Psi_{\h}(g)(\lambda) = \lambda . \]
\end{lem}

\begin{proof} Let $m$ be the number of pieces in $\sigma$, and choose $k$ large
enough such that $m \leq 2^{k+2}$. We may append to $\sigma$ a few
copies of the constant map $x_0$ at its end, so that now $\sigma$ has exactly 
$2^{k+2}$ pieces. The group element $g$ is unchanged. 

Denote by $\sigma'$ the closed string in
$\mbf{I}^2$ which is ``$k$-th subdivision'' of the boundary 
$\partial \mbf{I}^2$, based at $v_0$; so $\sigma'$ has 
$2^{k+2}= 4 \cdot 2^k$ pieces. We can construct a piecewise linear map
$f : \mbf{I}^2 \to X$ such that $f(v_0) = x_0$, and 
$f \circ \sigma' = \rho$ as strings. According to 
Propositions \ref{prop:12} and \ref{prop:5}(3) we have
\[ g = \opn{MI}(f^*(\alpha) \vert \sigma')
= \opn{MI}(f^*(\alpha) \vert \partial \mbf{I}^2)  . \]

Let $\beta \in \Omega^2_{\mrm{pws}}(X) \otimes \h$ be such that 
$(\alpha, \beta)$ is a connection-curvature pair for $\mbf{C} / X$.
By Proposition \ref{prop:11} the pair $(f^*(\alpha), f^*(\beta))$ is a
connection-curvature pair in $f^*(\mbf{C} / X)$.
Hence by Theorem \ref{thm:1} we have
$g = \Phi_0(h)$, where
\[ h := \opn{MI}(f^*(\alpha), f^*(\beta) \vert \mbf{I}^2) \in H . \]
Since $\lambda \in \opn{Lie}(\opn{Z}(H))$ it follows that
\[ \Psi_{\h}(g)(\lambda) = \Psi_{\h}(\Phi_0(h))(\lambda) = 
\opn{Ad}_{\h}(h)(\lambda) = \lambda . \]
\end{proof}

\begin{rem}
The lemma above shows that the holonomy group of a tame connection
$\alpha$ at $x_0$ acts trivially on the inertia subalgebra $\h_0$. Hence the
names.
\end{rem}

\begin{lem} \label{lem:46}
Let $\mbf{C} / X$ be a Lie quasi crossed module with additive feedback over
$(X, x_0)$, let $\alpha$ be a tame connection for $\mbf{C} / X$, and
let $Z \subset X$ be a subpolyhedron.
\begin{enumerate}
\item Let $f \in \mcal{O}_{\mrm{pws}}(Z) \otimes \h$ be an inert
function relative to $\mbf{C} / X$.
Then there is a unique function
\[ \Psi_{\h, \alpha}(f) : Z \to \h_0 \]
such that the following condition holds:
\begin{itemize}
\item[($*$)] Let $\sigma$ be a string in $X$, with initial point $x_0$
and terminal point $z := \sigma(v_1) \in Z$, and let
$g := \opn{MI}(\alpha \vert \sigma) \in G$. 
Then 
\[ \Psi_{\h, \alpha}(f)(z) = \Psi_{\h}(g)(f(z)) . \]

\end{itemize}
\item The operation $\Psi_{\h, \alpha}$
is linear over the ring $\mcal{O}_{\mrm{pws}}(Z)$.

\item The function $\Psi_{\h, \alpha}(f)$ is continuous.
\end{enumerate}
\end{lem}

\begin{proof}
Take a point $z \in Z$. Choose any string $\sigma$ connecting $x_0$ to $z$,
and let 
\[ \lambda  := \Psi_{\h}(g)(f(z)) \in \h \]
as in condition ($*$). Since $\alpha$ is a compatible connection 
(see Definition \ref{dfn:8}), and since $f$ is inert, we know that 
\[ \opn{Lie}(\Phi_0)(\lambda) = \Phi_X(x_0)(\lambda) = 
\opn{Ad}_{\g}(g)(\Phi_X(z)(f(z))) = 0 . \]
This shows that $\lambda \in \h_0$. 

If we were to choose another string $\sigma'$ with the same initial and terminal
points, then for 
$g' := \opn{MI}(\alpha \vert \sigma')$ we would have
\[ (\Psi_{\h}(g') \circ \Psi_{\h}(g)^{-1})(\lambda) = \lambda , \]
this according to Lemma \ref{lem:45}.
Hence $\lambda =  \Psi_{\h}(g')(f(z))$. 
We see that $\lambda$ is independent of the string $\sigma$, and 
we can define 
$\Psi_{\h, \alpha}(f)(z) := \lambda$.
We obtain a function $\Psi_{\h, \alpha}(f) : Z \to \h_0$.
This proves part (1). 

Part (2) is true because the operator $\Psi_{\h}(g) : \h \to \h$ is linear.

It remains to prove part (3). We need to prove that the function \lb 
$\Psi_{\h, \alpha}(f) : Z \to \h_0$ is continuous. So let's fix a point
$z_0 \in Z$, and a string $\sigma$ starting at $x_0$ and ending at $z_0$. Let
$g := \opn{MI}(\alpha \vert \sigma)$.
For any point $z \in Z$ let $\sigma_z : \mbf{I}^1 \to Z$ be the unique linear
map with initial point $z_0$ and terminal point $z$, and let
$g_z := \opn{MI}(\alpha \vert \sigma_z)$. So
\[ \Psi_{\h, \alpha}(f)(z) = \Psi_{\h}(g \cdot g_z)(f(z)) 
=  (\Psi_{\h}(g) \circ \Psi_{\h}(g_z))(f(z)) . \]
But according to Proposition \ref{prop:21} we know that 
$\Psi_{\h}(g_z) \to \bsym{1} \in \opn{End}(\h)$ as $z \to z_0$;
and $f(z) \to f(z_0)$ by continuity of $f$. 
Therefore 
\[ \Psi_{\h, \alpha}(f)(z) \to \Psi_{\h, \alpha}(f)(z_0) \] 
as $z \to z_0$.
\end{proof}

To summarize, the lemma says that there is an 
$\mcal{O}_{\mrm{pws}}(Z)$-linear homomorphism
\begin{equation} \label{eqn:224}
\Psi_{\h, \alpha} : \{ \text{inert functions on } Z \} 
\to \mcal{O}_{\mrm{cont}}(Z) \otimes \h_0 ,
\end{equation}
where $\mcal{O}_{\mrm{cont}}(Z)$ is the ring of continuous functions 
$Z \to \R$. 

Recall the module $\Omega^p_{\mrm{pwc}}(X)$ of piecewise continuous
differential forms, from Subsection \ref{subsec:pwc}.

\begin{prop} \label{prop:18}
Let $\alpha$ be a tame connection, and let
$\gamma \in \Omega^p_{\mrm{pws}}(X) \otimes \h$ be an inert form.
Then there is a unique piecewise continuous form
\[ \Psi_{\h, \alpha}(\gamma) \in \Omega^p_{\mrm{pwc}}(X) \otimes \h_0 \]
with the following property:
\begin{enumerate}
\item[($*$)] Choose a linear coordinate system 
$\bsym{s} = (s_1, \ldots, s_n)$ on $X$, and a smoothing
triangulation $\{ X_j \}_{j \in J}$ for $\gamma$. 
Let $f_{j, \bsym{i}} \in \mcal{O}(X_j) \otimes \h$
be the coefficients of $\gamma|_{X_j}$, as in \tup{(\ref{eqn:222})}.
Then
\[ \Psi_{\h, \alpha}(\gamma)|_{X_j} = 
\sum_{\bsym{i}} \, \Psi_{\h, \alpha}(f_{j, \bsym{i}}) \cdot 
\d s_{i_1} \wedge \cdots \wedge \d s_{i_p} . \]
\end{enumerate}
\end{prop}

Note that by Lemma \ref{lem:47} the functions $f_{j, \bsym{i}}$ are inert, 
so the continuous functions
$\Psi_{\h, \alpha}(f_{j, \bsym{i}}) \in \mcal{O}_{\mrm{cont}}(X_j)$ are defined.

\begin{proof}
This is immediate from the uniqueness of the coefficients
$f_{j, \bsym{i}}$, and the properties of the homomorphism
$\Psi_{\h, \alpha}$ listed in Lemma \ref{lem:46}.
\end{proof}

\begin{rem}
Actually a lot more can be said here. Presumably, one can show that 
\[ \opn{Ker}(\Phi_X) \subset \mcal{O}_{\mrm{pws}}(X) \otimes \h  \]
is the set of piecewise smooth sections of a piecewise smooth
vector bundle $E$ over $X$, which is a sub-bundle of the
trivial vector bundle $X \times \h$. 
And the operation $\Psi_{\h, \alpha}$ corresponds to a piecewise smooth
isomorphism of vector bundles
\[ E \iso  X \times \h_0 . \]

If so, then it would follow that for any inert form 
$\gamma \in \Omega^p_{\mrm{pws}}(Z) \otimes \h$, the form 
$\Psi_{\h, \alpha}(\gamma)$ is actually piecewise smooth (not just piecewise
continuous). And we would have an $\mcal{O}_{\mrm{pws}}(X)$-linear bijection
\[ \Psi_{\h, \alpha} : \{ \text{inert $p$-forms on } Z \} 
\to \Omega^p_{\mrm{pws}}(Z) \otimes \h_0 . \]
However we did not verify these assertions.
\end{rem}

Suppose we are given a piecewise continuous form
$\delta \in \Omega^p_{\mrm{pwc}}(X) \otimes \h$
and a piecewise linear map $\tau : \mbf{I}^p \to X$.
Extending the formula (\ref{eqn:221}) linearly to $\h_0$-valued forms we obtain
$\int_{\tau} \delta \in \h_0$.

\begin{dfn}[Integration of Inert Forms] \label{dfn:43}
\index{Twisted multiplicative integral of inert form}
Let  $\mbf{C} / X$ be a Lie quasi crossed module with additive feedback
over $(X, x_0)$. Given a tame connection $\alpha$, an inert form
$\gamma \in \Omega^p_{\mrm{pws}}(X) \otimes \h$ and a piecewise linear map
$\tau : \mbf{I}^p \to X$, we define the {\em twisted multiplicative integral}
\[ \opn{MI}(\alpha, \gamma \vert \tau) \in H_0 \] 
as follows: 
\[ \opn{MI}(\alpha, \gamma \vert \tau) :=
\exp_H \Bigl( \int_{\tau} \Psi_{\h, \alpha}(\gamma) \Bigr) . \]
\end{dfn}

\begin{prop} \label{prop:20}
Let $f : Y \to X$ and $\tau : \mbf{I}^p \to Y$ be piecewise linear maps
between polyhedra, let 
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$ 
be a tame connection, and let
$\gamma \in \Omega^p_{\mrm{pws}}(X) \otimes \h$ be an inert form. Then 
$f^*(\alpha) \in \Omega^1_{\mrm{pws}}(Y) \otimes \g$ 
is a tame connection, 
$f^*(\gamma) \in \Omega^p_{\mrm{pws}}(Y) \otimes \h$ is an inert form, and
\[ \opn{MI}(\alpha, \gamma \vert f \circ \tau) = 
\opn{MI} \bigl( f^*(\alpha), f^*(\gamma) \vert \tau \bigl) . \]
\end{prop}

\begin{proof}
The connection $f^*(\alpha)$ is tame for $f^*(\mbf{C} / X)$ by Corollary
\ref{cor:8}. It is easy to see directly from the definitions that $f^*(\gamma)$
is inert, and moreover 
\[ \Psi_{\h, f^*(\alpha)}(f^*(\gamma)) = 
f^*( \Psi_{\h, \alpha}(\gamma)) \in \Omega^p_{\mrm{pwc}}(Y) \otimes \h . \]
And Integration of piecewise continuous forms commutes with pullbacks (see
Subsection \ref{subsec:pwc}). 
\end{proof}





\subsection{Combinatorics and Integration} \label{subsec:combi3d}
In this subsection we work with the pointed polyhedron 
$(X, x_0) := \lb (\mbf{I}^3, v_0)$. We fix a Lie quasi crossed module
with additive feedback
\[ \mbf{C} / \mbf{I}^3 = (G, H, \Psi, \Phi_0, \Phi_X) , \] 
and a piecewise smooth connection-curvature pair 
$(\alpha, \beta)$ in $\mbf{C} / \mbf{I}^3$.
Let us also fix a euclidean norm $\norm{-}$ on $\h$, 
an open set $V_0(H)$ in $H$, and constants $\epsilon_0(H)$ and 
$c_0(H)$ as in Section \ref{sec:expon}.

\begin{lem} \label{lem:23}
Let $(\sigma, \tau)$ be a balloon in $(\mbf{I}^3, v_0)$. Then 
\[ \opn{MI} \bigl( \alpha, \beta \vert \partial (\sigma, \tau) \bigr)
\in H_0 . \]
\end{lem}

\begin{proof}
Let us write
$h := \opn{MI} \bigl( \alpha, \beta \vert \partial (\sigma, \tau) \bigr) \in H$
and 
$g := \opn{MI} \bigl( \alpha \vert \partial \partial (\sigma, \tau) \bigr) \in
G$.
According to Theorem \ref{thm:1} we have 
$\Phi_0(h) = g$. 

On the other hand, consider the word
$w(\bsym{s}) \in \opn{Wrd}^{\pm 1}(s_1, \ldots, s_{12})$ such that 
\[ \partial \partial \mbf{I}^3 = w(\rho_1, \ldots, \rho_{12}) , \]
where $\rho_1, \ldots, \rho_{12}$ are the oriented $1$-cells of 
$\opn{sd}^0 \mbf{I}^3$. Then 
$[w(\rho_1, \ldots, \rho_{12})] = 1$ in \linebreak
$\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^0 \mbf{I}^3)$. 
By Lemma \ref{lem:15} we know that
$w(\bsym{s}) \sim_{\mrm{can}} 1$ in $\opn{Wrd}^{\pm 1}(\bsym{s})$. 
Now writing $g_i := \opn{MI}(\alpha \vert \rho_i)$
we have
$g = w(g_1, \ldots, g_{12}) = 1$ in the group $G$. 
We see that 
$h \in  \opn{Ker}(\Phi_0) = H_0$.
\end{proof}

\begin{lem} \label{lem:24}
Take $k = 0, 1$. Let 
$\bsym{\rho} = \bigl( (\sigma_i, \tau_i) \bigr)_{i = 1, \ldots, n}$
be a sequence of kites in $(\mbf{I}^{3}, v_0)$, all patterned on 
$\opn{sd}^k \mbf{I}^3$. Write
\[ a_i := [\partial (\sigma_i, \tau_i)] \in 
\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^3) \]
and 
\[ h_i := \opn{MI} (\alpha, \beta \vert \sigma_i, \tau_i) \in H . \]
Let $w(\bsym{s}) \in \opn{Wrd}^{\pm 1}(s_1, \ldots, s_n)$ be a word such that
\[ w(a_1, \ldots, a_n) = 1 \]
in $\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^3)$ and
\[ [ w(\tau_1, \ldots, \tau_n) ] = 0 \]
in $\mrm{H}_2(\opn{sk}_2 \opn{sd}^k \mbf{I}^3)$. Then
\[ w(h_1, \ldots, h_n) = 1 \]
in $H$.
\end{lem}

Observe that by Lemma \ref{lem:20} the chain 
$w(\tau_1, \ldots, \tau_n)$ is a cycle, so we can talk about its homology class.

\begin{proof}
First assume $k = 0$. Let $p_i \in \{ 1, \ldots, 6 \}$, 
$d_i \in \{ 0, 1 \}$ and $e_i \in \{ 0, 1, 2, 3 \}$ be such that
\[ \tau_i = \opn{flip}^{d_i} ( \opn{turn}^{e_i} (\tau^{\flat}_{p_i} )) . \]
as maps $\mbf{I}^2 \to \mbf{I}^3$.
Let
$a^{\flat}_i := [\partial (\sigma^{\flat}_{i}, \tau^{\flat}_{i})]$
and
$h^{\flat}_i := \opn{MI} (\alpha, \beta \vert \sigma^{\flat}_i,
\tau^{\flat}_i)$,
in the notation of Definition \ref{dfn:36}. There are words 
$v_i(\bsym{t}) \in \opn{Wrd}^{\pm 1}(t_1, \ldots, t_6)$
such that 
\[ [\sigma_i] * [\sigma^{\flat}_{p_i}]^{-1} = 
v_i(a^{\flat}_1, \ldots, a^{\flat}_6) \]
in the group 
$\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^0 \mbf{I}^3)$.
According to Corollaries \ref{cor:2} and \ref{cor:6}, repeated, we have
\[ h_i = \opn{Ad}_H \bigl( v_i( h^{\flat}_1, \ldots, h^{\flat}_6 ) \bigr)
\bigl( (h^{\flat}_{p_i})^{(-1)^{d_i}} \bigr) . \]
Define
\[ u_i(\bsym{t}) := \opn{Ad}_{\opn{Wrd}^{\pm 1}(\bsym{t})}( v_i(\bsym{t}))
(y_{p_i}^{(-1)^{d_i}}) \in \opn{Wrd}^{\pm 1}(\bsym{t})  \]
using the conjugation operation from (\ref{eqn:249}). Then
$h_i = u_i(h^{\flat}_1, \ldots, h^{\flat}_6)$ and
$a_i = u_i(a^{\flat}_1, \ldots, a^{\flat}_6)$.

Let 
\[ u(\bsym{t}) := w \bigl( u_1(\bsym{t}), \ldots, u_n(\bsym{t}) \bigr) 
\in \opn{Wrd}^{\pm 1}(\bsym{t}) . \]
We know that
$u(a^{\flat}_1, \ldots, a^{\flat}_6) = 1$ in 
$\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^0 \mbf{I}^3)$.
Hence by Lemmas \ref{lem:21}(1) and \ref{lem:15} we have
\[ u(\bsym{t}) \sim_{\mrm{can}} 
\opn{Ad}_{\opn{Wrd}^{\pm 1}(\bsym{t})} (v(\bsym{t})) \bigl( (y_1 \cdots y_6)^e 
\bigr)
\]
in $\opn{Wrd}^{\pm 1}(\bsym{t})$, for some word $v(\bsym{t})$ and integer $e$. 
Passing to the abelian group \linebreak 
$\mrm{H}_2(\opn{sk}_2 \opn{sd}^0 \mbf{I}^3)$, with additive notation, 
we get
\[ e \cdot [\tau^{\flat}_{1} + \cdots + \tau^{\flat}_{6}] = 
[u(\tau^{\flat}_{1} , \ldots , \tau^{\flat}_{6})] =
[w(\tau_1, \ldots, \tau_n)] = 0 . \]
Using Lemma \ref{lem:21}(2) we conclude that $e = 0$, and hence
$u(\bsym{t}) \sim_{\mrm{can}} 1$ in $\opn{Wrd}^{\pm 1}(\bsym{t})$.
Finally, evaluating in the group $H$ we get
\[ w(h_1, \ldots, h_n) = u(h^{\flat}_1, \ldots, h^{\flat}_6) = 1 . \]

For the case $k = 1$ the proof is the same, only using Lemma \ref{lem:22}
instead of Lemma \ref{lem:21}, and working with the  with words in the  monoid
$\opn{Wrd}^{\pm 1}(t_1, \ldots, t_{48})$ instead of 
$\opn{Wrd}^{\pm 1}(t_1, \ldots, t_{6})$.
\end{proof}


\subsection{Estimates} \label{subsec:est}
We continue with the setup of Subsection \ref{subsec:combi3d}.

Recall the constants $c_{2'}(\alpha, \beta)$ and $\epsilon_{2'}(\alpha, \beta)$
from Proposition \ref{prop:22}. \lb Among other things, these numbers satisfy
$c_{2'}(\alpha, \beta) \geq 1$ and $0 < \epsilon_{2'}(\alpha, \beta) \lb < 1$.

\begin{lem} \label{lem:26}
There are constants $c_6(\alpha, \beta)$ and
$\epsilon_6(\alpha, \beta)$ with these properties:
\begin{enumerate}
\rmitem{i} $c_6(\alpha, \beta) \geq c_{2'}(\alpha, \beta)$ and
\[ 0 < \epsilon_6(\alpha, \beta) \leq \min \bigl(
\smfrac{1}{6} \cdot c_6(\alpha, \beta)^{-1} \cdot \epsilon_0(H) , \
\epsilon_{2'}(\alpha, \beta) \bigr) \, . \]

\rmitem{ii} Suppose $(\sigma, \tau)$ is a cubical balloon
$(\mbf{I}^3, v_0)$
such that 
$\opn{side}(\tau) < \epsilon_6(\alpha, \beta)$ 
and $\opn{len}(\sigma) \leq 6$. Then
\[ \opn{MI} \bigl( \alpha, \beta \vert 
\partial (\sigma, \tau) \bigr) \in V_0(H) \]
and
\[ \Norm{ \log_H \bigl( \opn{MI} \bigl( \alpha, \beta \vert 
\partial (\sigma, \tau) \bigr) \bigr) }
\leq c_6(\alpha, \beta) \cdot \opn{side}(\tau)^3  \, . \]
\end{enumerate}
\end{lem}

\begin{proof}
The proof is basically the same as that of Lemma \ref{lem:9}, but using
Proposition \ref{prop:22} instead of Proposition \ref{prop:16}.
\end{proof}

Suppose $(\sigma, \tau)$ is a nondegenerate cubical balloon in
$(\mbf{I}^3, v_0)$. Let us write $\epsilon := \opn{side}(\tau)$; 
$Z := \tau(\mbf{I}^3)$, which is an oriented cube in $\mbf{I}^3$; and 
$z_0 := \tau(\smfrac{1}{2}, \smfrac{1}{2}, \smfrac{1}{2})$, the midpoint of $Z$.
Let $\bsym{s} = (s_1, s_2, s_3)$ be the orthonormal linear coordinate system on
$Z$ such that 
$\tau^*(s_i) = \epsilon \cdot t_i$.

Assume that the forms $\alpha|_Z$ and $\beta|_Z$ are smooth. Let 
$\til{\alpha}_1, \til{\alpha}_2, \til{\alpha}_3 \in 
\mcal{O}(Z) \otimes \g$
be the coefficients of $\alpha|_Z$ relative to $\bsym{s}$, namely 
\[ \alpha|_Z = \sum_{1 \leq i \leq 3} \, \til{\alpha}_i \cdot \d s_i . \]
And let
$\til{\beta}_{1, 2}, \til{\beta}_{1, 3}, \til{\beta}_{2, 3}  \in 
\mcal{O}(Z) \otimes \h$
be the coefficients of $\beta|_Z$ relative to $\bsym{s}$, namely 
\[ \beta|_Z = \sum_{1 \leq i < j \leq 3} \, 
\til{\beta}_{i, j} \cdot \d s_i \wedge \d s_j . \]

Recall the Lie algebra map
\[ \psi_{\h} = \opn{Lie}(\Psi_{\h}) : \g \to \opn{End}(\h) . \]
For any $i$ we get a function
\[ \psi_{\h}(\til{\alpha}_i) \in \mcal{O}(Z) \otimes \opn{End}(\h) ; \]
so for any $i, j, k$ there is a function
\[ \psi_{\h}(\til{\alpha}_i)(\til{\beta}_{j, k}) \in 
\mcal{O}(Z) \otimes \h . \]
Define the function
\begin{equation} \label{eqn:197}
 \begin{aligned}
& \til{\gamma} := 
\smfrac{\partial}{\partial s_1}(\til{\beta}_{2, 3}) 
- \smfrac{\partial}{\partial s_2}(\til{\beta}_{1, 3})
+ \smfrac{\partial}{\partial s_3}(\til{\beta}_{1, 2}) \\
& \qquad \quad + \psi_{\h}(\til{\alpha}_1)(\til{\beta}_{2, 3}) 
- \psi_{\h}(\til{\alpha}_2)(\til{\beta}_{1, 3}) 
+ \psi_{\h}(\til{\alpha}_3)(\til{\beta}_{1, 2})
\in \mcal{O}(Z) \otimes \h .
\end{aligned}
\end{equation}

Let $\sigma_{\mrm{pr}}$ be the following string in $Z$:
\begin{equation} \label{eqn:204}
\sigma_{\mrm{pr}} := \tau \circ \bigl( v_0, (\smfrac{1}{2}, 0, 0) \bigr) * 
\bigl( (\smfrac{1}{2}, 0, 0), (\smfrac{1}{2}, \smfrac{1}{2}, 0) \bigr) *
\bigl( (\smfrac{1}{2}, \smfrac{1}{2}, 0), 
(\smfrac{1}{2}, \smfrac{1}{2}, \smfrac{1}{2}) \bigr) . 
\end{equation}
So $\sigma_{\mrm{pr}}$ has initial point $\tau(v_0)$ and
terminal point $z_0$; see Figure \ref{fig:50}. Define
\begin{equation} \label{eqn:215}
g_0 := \opn{MI}(\alpha \vert \sigma_{\mrm{pr}}) \ \text{ and } \
g := \opn{MI}(\alpha \vert \sigma) 
\end{equation}
in $G$. 

\begin{figure}
\includegraphics[scale=0.39]{fig50.jpg}

\caption{Illustration for Subsection \ref{subsec:est}.} 
\label{fig:50}
\end{figure}

For $i \in \{ 1, \ldots, 6 \}$ we consider the points $z_i \in Z$ defined as
follows:
\[ z_1 := \tau(\smfrac{1}{2}, 1, \smfrac{1}{2}) , \
z_2 := \tau(1, \smfrac{1}{2}, \smfrac{1}{2}) , \ 
z_3 := \tau(\smfrac{1}{2}, \smfrac{1}{2}, 1) , \]
\[ z_4 := \tau(\smfrac{1}{2}, 0, \smfrac{1}{2}) , \
z_5 := \tau(0, \smfrac{1}{2}, \smfrac{1}{2}) , \ 
z_6 := \tau(\smfrac{1}{2}, \smfrac{1}{2}, 0) . \]
See Figure \ref{fig:50}. We define the strings
\begin{equation} \label{eqn:216}
\rho'_i := (\tau \circ \sigma^{\flat}_i) * 
(\tau \circ \tau^{\flat}_i \circ \sigma_{\mrm{pr}}) ,
\end{equation}
where $\sigma_{\mrm{pr}}$ is the probe in $\mbf{I}^2$; see formula 
(\ref{eqn:237}). 
So $\rho'_i$ has initial point $\tau(v_0)$ and terminal point $z_i$. 
Let
\[ g'_i := \opn{MI}(\alpha \vert \rho'_i) \in G . \]

For $i \in \{ 1, \ldots, 6 \}$ we define elements $\lambda_i \in \h$ as
follows:
\begin{equation} \label{eqn:217}
\begin{aligned}
& \lambda_1 := - \epsilon^2 \cdot \Psi_{\h}(g \cdot g'_1)
\bigl( \til{\beta}_{1, 3}(z_1) \bigr) , \\
& \lambda_2 := \epsilon^2 \cdot \Psi_{\h}(g \cdot g'_2)
\bigl( \til{\beta}_{2, 3}(z_2) \bigr) , \\
& \lambda_3 := \epsilon^2 \cdot \Psi_{\h}(g \cdot g'_3)
\bigl( \til{\beta}_{1, 2}(z_3) \bigr) , \\
& \lambda_4 := - \epsilon^2 \cdot \Psi_{\h}(g \cdot g'_4)
\bigl( \til{\beta}_{1, 3}(z_4) \bigr) , \\
&  \lambda_5 := \epsilon^2 \cdot \Psi_{\h}(g \cdot g'_5)
\bigl( \til{\beta}_{2, 3}(z_5) \bigr) , \\
& \lambda_6 :=  \epsilon^2 \cdot \Psi_{\h}(g \cdot g'_6)
\bigl( \til{\beta}_{1, 2}(z_6) \bigr) .

\end{aligned}
\end{equation}

It is easy to see from Definition \ref{dfn:11} that
\begin{equation} \label{eqn:198}
\exp_H(\lambda_i) = 
\opn{RP}_0(\alpha, \beta \vert \partial_i(\sigma, \tau)) .
\end{equation}

\begin{lem} \label{lem:27}
There are constants $c_7(\alpha, \beta)$ and
$\epsilon_7(\alpha, \beta)$ with these properties:
\begin{enumerate}
\rmitem{i} $c_7(\alpha, \beta) \geq c_6(\alpha, \beta)$ and
\[ 0 < \epsilon_7(\alpha, \beta) \leq 
\min \bigl( \epsilon_6(\alpha, \beta), \, 
\smfrac{1}{10} \epsilon_1(\alpha) \bigr) \, . \]

\rmitem{ii} Let $(\sigma, \tau)$ be a nondegenerate cubical balloon in
$(\mbf{I}^3, v_0)$ with $\epsilon := \opn{side}(\tau)$. Assume that 
$\epsilon < \epsilon_7(\alpha, \beta)$,
$\opn{len}(\sigma) \leq 6$,
and the forms $\alpha|_Z$ and $\beta|_Z$ are smooth.
Then, with $\lambda_i$ as in \tup{(\ref{eqn:217})}, the following estimate
holds:
\[ \Norm{ \log_H \bigl( \opn{MI}(\alpha, \beta \vert 
\partial(\sigma, \tau)) \bigr)
- \bosum_{i = 1}^6 \lambda_i }
\leq c_7(\alpha, \beta)  \cdot \epsilon^4 \, . \]
\end{enumerate}
\end{lem}

\begin{proof}
Let us set
\[ c := 12 \cdot \max \bigl( c_2(\alpha, \beta), \, 
\exp ( c_4(\alpha, \Psi_{\h}) \cdot 9 ) \cdot 
\norm{\beta}_{\mrm{Sob}} \bigr) \, . \]
According to Proposition \ref{prop:8}(2), if
$\epsilon < \epsilon_2(\alpha, \beta)$ then 
\begin{equation} \label{eqn:199}
\Norm{ \log_H \bigl( \opn{MI}(\alpha, \beta \vert \partial_i(\sigma, \tau)) 
\bigr) - \lambda_i } 
\leq c_2(\alpha, \beta) \cdot \epsilon^4 
\leq \smfrac{1}{12} c \cdot \epsilon^4 \, . 
\end{equation}
And by Proposition \ref{prop:13} we know that
\begin{equation*} \label{eqn:200}
\norm{\lambda_i} \leq \exp \bigl( c_4(\alpha, \Psi_{\h}) \cdot 9 \bigr) \cdot 
\norm{\beta}_{\mrm{Sob}} \cdot \epsilon^2 
\leq \smfrac{1}{12} c \cdot \epsilon^2 \, .  
\end{equation*}
Hence
\begin{equation} \label{eqn:201}
\Norm{ \log_H \bigl( 
\opn{MI}(\alpha, \beta \vert \partial_i(\sigma, \tau)) \bigr) }
\leq \smfrac{1}{6}  c \cdot  \epsilon^2 \, .  
\end{equation}
We will take 
\[ \epsilon_7(\alpha, \beta) := \min \bigl( 
\epsilon_6(\alpha, \beta), \, 
c^{- 1/2} \cdot \epsilon_0(H)^{1/2} \bigr) \, . \]

Now assume that
$\epsilon <  \epsilon_7(\alpha, \beta)$. Then by property (ii) of Theorem
\ref{thm:6}, used in conjunction with the bound (\ref{eqn:201}), we get
\[ \begin{aligned}
& \Norm{ \log_H \bigl( \boprod_{i = 1}^6  
\opn{MI}(\alpha, \beta \vert \partial_i(\sigma, \tau)) \bigr)
- \bosum_{i = 1}^6  
\opn{MI}(\alpha, \beta \vert \partial_i(\sigma, \tau)) } \\
& \qquad \leq 
c_0(H) \cdot (c \cdot \epsilon^2)^2 = 
c_0(H) \cdot c^2 \cdot \epsilon^4 \, . 
\end{aligned} \]
Combining this with (\ref{eqn:199}) we obtain 
\begin{equation} \label{eqn:202}
\begin{aligned}
& \Norm{ \log_H \bigl( \boprod_{i = 1}^6  
\opn{MI}(\alpha, \beta \vert \partial_i(\sigma, \tau)) \bigr)
- \bosum_{i = 1}^6 \lambda_i } \\
& \qquad \leq 
\bigl( c_0(H) \cdot c^2 + \smfrac{1}{2} c \bigr) \cdot \epsilon^4 \, . 
\end{aligned} 
\end{equation}
Thus the constant
\[ c_7(\alpha, \beta) := \max \bigl( 
c_0(H) \cdot c^2 + \smfrac{1}{2} c, \, c_6(\alpha, \beta) \bigr)  \]
works.
\end{proof}

\begin{dfn}
\begin{enumerate}
\item Let $(\sigma, \tau)$ be a square kite in $(\mbf{I}^3, v_0)$. We
will say that $(\sigma, \tau)$ is
{\em $(\alpha, \beta)$-tiny} (in this section) if 
$\opn{side}(\tau) < \epsilon_7(\alpha, \beta)$ and
$\opn{len}(\sigma) \leq 9$. 
\item Let $(\sigma, \tau)$ be a cubical balloon in $(\mbf{I}^3, v_0)$. We
will say that $(\sigma, \tau)$ is
{\em $(\alpha, \beta)$-tiny} if 
$\opn{side}(\tau) < \epsilon_7(\alpha, \beta)$ and
$\opn{len}(\sigma) \leq 6$. 
\end{enumerate}
\end{dfn}

Note that if $(\sigma, \tau)$ is an $(\alpha, \beta)$-tiny cubical balloon,
then the kites $\partial_i(\sigma, \tau)$ are all $(\alpha, \beta)$-tiny.

Let $(\sigma, \tau)$  be a cubical balloon in $(\mbf{I}^2, v_0)$.
For $i \in \{ 1, \ldots, 6 \}$ let $\rho_i$ be the linear map 
$\mbf{I}^1 \to Z$ such that $\rho_i(v_0) = z$ and 
$\rho_i(v_1) = z_i$. Recall the string $\sigma_{\mrm{pr}}$ from
(\ref{eqn:204}). 
For every $i \in \{ 1, \ldots, 6 \}$ the string
$\sigma_{\mrm{pr}} * \rho_i$ has initial point $\tau(v_0)$ and terminal point
$z_i$.
Let
\[ g_i := \opn{MI}(\alpha \vert \rho_i) \in G . \]

The form $\alpha|_Z$ is smooth, and hence we have
\[ \alpha' := \psi_{\h}(\alpha|_Z) \in 
\Omega^1(Z) \otimes \opn{End}(\h) .  \] 
As in Definition \ref{dfn:26} there is an associated constant form at $z_0$:
\[ \alpha'(z_0) \in \Omega^1_{\mrm{const}}(Z) \otimes \opn{End}(\h) . \]
In this way for every $i$ we get 
\[ \int_{\rho_i} \alpha'(z_0) \in \opn{End}(\h) . \]

\begin{lem} \label{lem:44}
There is a constant $c_8(\alpha, \beta)$ with this property:
\begin{enumerate}
\rmitem{$*$} Let $(\sigma, \tau)$ be a nondegenerate $(\alpha, \beta)$-tiny 
cubical balloon in $(\mbf{I}^3, v_0)$,
with $\epsilon := \opn{side}(\tau)$. 
Then, in the notation above, the estimate
\[ \Norm{ \Psi_{\h}(g \cdot g'_i) - 
\Psi_{\h}(g \cdot g_0) \circ 
\bigl( \bsym{1} + \int_{\rho_i} \alpha'(z_0) \bigr) }
\leq c_8(\alpha, \beta) \cdot \epsilon^2  \]
holds for every $i \in \{ 1, \ldots, 6 \}$.
\end{enumerate}
\end{lem}

\begin{proof}
Consider such a balloon. 
Recall the strings $\rho'_i$ from formula (\ref{eqn:216}). 
Since 
$\epsilon < \epsilon_7(\alpha, \beta) \leq 
\smfrac{1}{10} \epsilon_1(\alpha)$, we see that for every $i$ 
the closed string $\rho'_i * (\sigma_{\mrm{pr}} * \rho_i)^{-1}$ has 
\[ \opn{len}(\rho'_i * (\sigma_{\mrm{pr}} * \rho_i)^{-1}) <
10 \cdot \epsilon \leq \epsilon_1(\alpha) . \]
And this closed string bounds an area less than 
$10 \cdot \epsilon^2$. Hence by Corollary \ref{cor:7} we have
\[ \Norm{ \log_G \bigl( g'_i \cdot (g_0 \cdot g_i)^{-1} \bigr) } \leq
c_0(G) \cdot c_1(\alpha)^2 \cdot (10 \cdot \epsilon)^2 +
(10 \cdot \epsilon^2) \cdot \norm{\alpha}_{\mrm{Sob}} \, . \]
Therefore there is a constant $c'$, depending only on $\alpha$, such that 
\begin{equation} \label{eqn:205}
\Norm{ \Psi_{\h}(g'_i) - \Psi_{\h}(g_0 \cdot g_i) } \leq c' \cdot 
\epsilon^2 \, .
\end{equation}
By Proposition \ref{prop:13} we know that
\begin{equation*} \label{eqn:206}
\norm{ \Psi_{\h}(g) } \leq \exp \bigl( c_4(\alpha, \Psi_{\h}) \cdot 9 \bigr)
\cdot \norm{\alpha}_{\mrm{Sob}}  
\end{equation*}
and
\[ \norm{ \Psi_{\h}(g_0) } \leq \exp \bigl( 
c_4(\alpha, \Psi_{\h}) \cdot 2 \epsilon \bigr)
\cdot \norm{\alpha}_{\mrm{Sob}}  \, . \]
Therefore
\begin{equation*} \label{eqn:207}
\begin{aligned}
& \Norm{ \Psi_{\h}(g \cdot g'_i) - \Psi_{\h}(g \cdot g_0 \cdot g_i) } = 
\Norm{ \Psi_{\h}(g) \circ \bigl( \Psi_{\h}(g'_i) - 
\Psi_{\h}(g_0 \cdot g_i) \bigr) } \\
& \qquad \leq 
\Norm{ \Psi_{\h}(g) } \cdot 
\Norm{ \Psi_{\h}(g'_i) - \Psi_{\h}(g_0 \cdot g_i) } \\
& \qquad \leq 
\exp \bigl( c_4(\alpha, \Psi_{\h}) \cdot 9 \bigr)
\cdot \norm{\alpha}_{\mrm{Sob}} \cdot 
 c' \cdot \epsilon^2 \, .
\end{aligned}
\end{equation*}
On the other hand, by Proposition \ref{prop:21} we have the estimate
\begin{equation*} \label{eqn:208}
\Norm{ \Psi_{\h}(g_i) - \bigl( \bsym{1} + 
\int_{\rho_i} \alpha'(z_0) \bigr) }
\leq c_5(\alpha, \Psi_{\h}) \cdot \smfrac{1}{4} \epsilon^2 \, .
\end{equation*}
We conclude that the constant 
\[ \begin{aligned}
& c_8(\alpha, \beta) := 
\exp \bigl( c_4(\alpha, \Psi_{\h}) \cdot 9 \bigr)
\cdot \norm{\alpha}_{\mrm{Sob}} \cdot  c' \\
& \qquad  \qquad +
c_5(\alpha, \Psi_{\h}) \cdot \smfrac{1}{4} \cdot 
\exp \bigl( c_4(\alpha, \Psi_{\h}) \cdot 12 \bigr)
\cdot \norm{\alpha}_{\mrm{Sob}}^2 \, . 
\end{aligned} \]
works.
\end{proof}

\begin{lem} \label{lem:43}
There is a constant $c_9(\alpha, \beta)$ with this property:
\begin{enumerate}
\rmitem{$*$} Let $(\sigma, \tau)$ be a nondegenerate $(\alpha, \beta)$-tiny 
cubical balloon in $(\mbf{I}^3, v_0)$, with 
$\epsilon := \opn{side}(\tau)$. 
Then, in the notation above, the following estimate holds:
\[ \Norm{ \bosum_{i = 1}^6 \lambda_i
- \epsilon^3 \cdot \Psi_{\h}(g \cdot g_0)(\til{\gamma}(z_0)) } 
\leq \epsilon^4 \cdot c_9(\alpha, \beta) \, . \]
\end{enumerate}
\end{lem}

\begin{proof}
The strategy is to try to estimate the elements $\lambda_i$.

We begin with $i = 1$. Define
\[ \begin{aligned}
& \mu_1 := \epsilon^2 \cdot \Psi_{\h}(g \cdot g_0) \Bigl(
- \til{\beta}_{1, 3}(z_0) 
- \smfrac{1}{2} \cdot \epsilon \cdot
\psi_{\h}(\til{\alpha}_2(z_0))(\til{\beta}_{1, 3}(z_0)) \\
& \qquad \qquad
- \smfrac{1}{2} \cdot \epsilon \cdot 
(\smfrac{\partial}{\partial s_2} \til{\beta}_{1, 3})(z_0) \Bigr) .
\end{aligned} \]
The Taylor expansion to first order of the function $\til{\beta}_{1, 3}$ around
$z_0$ gives us
\begin{equation} \label{eqn:210}
\Norm{ \til{\beta}_{1, 3}(z_1) - \bigl( \til{\beta}_{1, 3}(z_0)
- \smfrac{1}{2} \epsilon \cdot 
(\smfrac{\partial}{\partial s_2} \til{\beta}_{1, 3})(z_0) \bigr) }
\leq \smfrac{1}{4} \epsilon^2 \cdot \norm{\beta}_{\mrm{Sob}} \, . 
\end{equation}
And Lemma \ref{lem:44}, for $i = 1$, gives
\begin{equation} \label{eqn:211}
\Norm{ \Psi_{\h}(g \cdot g'_i) - 
\Psi_{\h}(g \cdot g_0) \circ 
\bigl( \bsym{1} - \smfrac{1}{2} \epsilon \cdot \til{\alpha}_2(z_0) \bigr) }
\leq c_8(\alpha, \beta) \cdot \epsilon^2 \, . 
\end{equation}
Let
\[ \begin{aligned}
& d := \exp \bigl( c_4(\alpha, \Psi_{\h}) \cdot 9 \bigr)
\cdot \smfrac{1}{4} \cdot \norm{\beta}_{\mrm{Sob}} +
c_8(\alpha, \beta) \cdot 2 \cdot \norm{\beta}_{\mrm{Sob}} \\
& \qquad  + \exp \bigl( c_4(\alpha, \Psi_{\h}) \cdot 9 \bigr) \cdot 
\smfrac{1}{2} \cdot \norm{\alpha'}_{\mrm{Sob}} \cdot
\norm{\beta}_{\mrm{Sob}} \, . 
\end{aligned} \]
By combining the estimates (\ref{eqn:210}) and (\ref{eqn:211})  we obtain
\begin{equation} \label{eqn:212}
\norm{ \lambda_1 - \mu_1 } \leq d \cdot \epsilon^4 \, .
\end{equation}

We do the same thing for $\lambda_4$: let 
\[ \begin{aligned}
& \mu_4 := \epsilon^2 \cdot \Psi_{\h}(g \cdot g_0) \Bigl(
\til{\beta}_{1, 3}(z_0) 
- \smfrac{1}{2} \cdot \epsilon \cdot
\psi_{\h}(\til{\alpha}_2(z_0))(\til{\beta}_{1, 3}(z_0)) \\
& \qquad \qquad  
- \smfrac{1}{2} \cdot \epsilon \cdot 
(\smfrac{\partial}{\partial s_2} \til{\beta}_{1, 3})(z_0) \Bigr) .
\end{aligned} \]
The same sort of calculation that got us (\ref{eqn:212}), now gives the
inequality
\begin{equation} \label{eqn:213}
\norm{ \lambda_4 - \mu_4 } \leq d \cdot \epsilon^4
\end{equation}
And clearly 
\[ \mu_1 + \mu_4 = 
\epsilon^3 \cdot \Psi_{\h}(g \cdot g_0) \bigl( 
- \psi_{\h}(\til{\alpha}_2(z_0))(\til{\beta}_{1, 3}(z_0)) 
- (\smfrac{\partial}{\partial s_2} \til{\beta}_{1, 3})(z_0) \bigr) . \]
Plugging inequalities  (\ref{eqn:212}) and (\ref{eqn:213}) into this 
we get
\begin{equation} \label{eqn:214}
\begin{aligned}
& \Norm{ (\lambda_1 + \lambda_4) - 
\bigl( \epsilon^3 \cdot \Psi_{\h}(g \cdot g_0) \bigl( 
- \psi_{\h}(\til{\alpha}_2(z_0))(\til{\beta}_{1, 3}(z_0)) 
- (\smfrac{\partial}{\partial s_2} \til{\beta}_{1, 3})(z_0) \bigr) \bigr) } \\
& \qquad \leq \epsilon^4 \cdot 2 d \, . 
\end{aligned}
\end{equation}

By a similar calculation for the pairs of indices $(2, 5)$ and $(3, 6)$ 
we get these analogues of formula (\ref{eqn:214}): 
\[ \begin{aligned}
& \Norm{ (\lambda_2 + \lambda_5) - 
\bigl( \epsilon^3 \cdot \Psi_{\h}(g \cdot g_0) \bigl( 
\psi_{\h}(\til{\alpha}_1(z_0))(\til{\beta}_{2, 3}(z_0)) 
+ (\smfrac{\partial}{\partial s_1} \til{\beta}_{2, 3})(z_0) \bigr) \bigr) } \\
& \qquad \leq \epsilon^4 \cdot 2 d  
\end{aligned} \]
and 
\[ \begin{aligned}
& \Norm{ (\lambda_3 + \lambda_6) - 
\bigl( \epsilon^3 \cdot \Psi_{\h}(g \cdot g_0) \bigl( 
\psi_{\h}(\til{\alpha}_3(z_0))(\til{\beta}_{1, 2}(z_0)) 
+ (\smfrac{\partial}{\partial s_3} \til{\beta}_{1, 2})(z_0) \bigr) \bigr) } \\
& \qquad \leq \epsilon^4 \cdot 2 d \, . 
\end{aligned} \]
Thus, plugging in the value of $\til{\gamma}(z_0)$ from (\ref{eqn:197}) we get
\[ \Norm{ \bosum_{i = 1}^6 \lambda_i - 
\epsilon^3 \cdot \Psi_{\h}(g \cdot g_0) (\til{\gamma}(z_0)) }
\leq \epsilon^4 \cdot 6 d \, . \]
To finish we take
$c_8(\alpha, \beta) :=  6 d$.
\end{proof}

The last two lemmas combined give us:

\begin{lem} \label{lem:49}
Let $(\sigma, \tau)$ be a nondegenerate $(\alpha, \beta)$-tiny 
cubical balloon in $(\mbf{I}^3, v_0)$, with 
$\epsilon := \opn{side}(\tau)$,
$Z := \tau(\mbf{I}^3)$ and 
$z := (\smfrac{1}{2}, \smfrac{1}{2}, \smfrac{1}{2})$. 
Assume that $\alpha|_Z$ and $\beta|_Z$ are smooth. Let
$\til{\gamma} \in \mcal{O}(Z) \otimes \h$ be the function from 
equation \tup{(\ref{eqn:197})}, and let $g, g_0 \in G$ be the group elements
from equation \tup{(\ref{eqn:215})}. Then
\[ \Norm{ \log_H \bigl( \opn{MI}(\alpha, \beta \vert 
\partial(\sigma, \tau)) \bigr) 
- \epsilon^3 \cdot \Psi_{\h}(g \cdot g_0)(\til{\gamma}(z_0)) } 
\leq \epsilon^4 \cdot c_{10}(\alpha, \beta) \, , \]
where
\[ c_{10}(\alpha, \beta) := c_8(\alpha, \beta) + c_9(\alpha, \beta) . \]

If, moreover, $\til{\gamma}$ happens to be an inert function, then 
\[ \Psi_{\h}(g \cdot g_0) (\til{\gamma}(z_0)) = 
\Psi_{\h, \alpha}(\til{\gamma})(z_0) , \]
and therefore
\[ \Norm{ \log_H \bigl( \opn{MI}(\alpha, \beta \vert 
\partial(\sigma, \tau)) \bigr) 
- \epsilon^3 \cdot \Psi_{\h, \alpha}(\til{\gamma})(z_0) } 
\leq \epsilon^4 \cdot c_{10}(\alpha, \beta) \, . \]
\end{lem}



\subsection{Stokes Theorem}

Here again we are in the general situation: 
$(X, x_0)$ is a pointed polyhedron, 
\[ \mbf{C} / X = (G, H, \Psi, \Phi_0, \Phi_X) \]
is a Lie quasi crossed module with additive feedback, and
$(\alpha, \beta)$ is a piecewise smooth connection-curvature pair in 
$\mbf{C} / X$.

The Lie group map
$\Psi_{\h} : G \to \opn{GL}(\h)$ induces a Lie algebra map
\[ \psi_{\h} := \opn{Lie}(\Psi_{\h}) : \g \to \mfrak{gl}(\h) = 
\opn{End}(\h) . \]
By tensoring with $\Omega_{\mrm{pws}}(X)$ this induces a map of DG Lie algebras
\[ \psi_{\h} : \Omega_{\mrm{pws}}(X) \otimes \g \to 
\Omega_{\mrm{pws}}(X) \otimes \opn{End}(\h) . \]
In this way from the pair $\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$
and 
$\beta \in \Omega^2_{\mrm{pws}}(X) \otimes \h$ we get
\[ \psi_{\h}(\alpha)(\beta) \in \Omega^3_{\mrm{pws}}(X) \otimes \h . \]

\begin{dfn} \label{dfn:32}
\index{$3$-curvature}
Let $(X, x_0)$ be a pointed polyhedron, let
\[ \mbf{C} / X = (G, H, \Psi, \Phi_0, \Phi_X) \]
be a Lie quasi crossed module with additive feedback, and
let $(\alpha, \beta)$ be a piecewise smooth connection-curvature pair in 
$\mbf{C} / X$. The {\em $3$-curvature of $(\alpha, \beta)$} is the form
\[ \gamma := \d(\beta) + \psi_{\h}(\alpha)(\beta) \in 
\Omega_{\mrm{pws}}^3(X) \otimes \h . \]
\end{dfn}

Recall the notion of orientation of a polyhedron (Subsection
\ref{subsec:orient}). If $Z$ is an oriented cube, and 
$(s_1, s_2, s_3)$ is a positively oriented orthonormal linear coordinate system
on $Z$, then 
\[ \opn{or}(Z) = \d s_1 \wedge \d s_2 \wedge \d s_3 . \] 

\begin{lem} \label{lem:48}
Assume that $(X, x_0) = (\mbf{I}^3, v_0)$, so that we are in the situation of
Subsection \tup{\ref{subsec:est}}. 
Let $Z \subset \mbf{I}^3$ be an oriented nondegenerate cube, such that 
$\alpha|_Z$ and $\beta|_Z$ are smooth. Let
$\til{\gamma} \in \mcal{O}(Z) \otimes \h$ be the function from formula
\tup{(\ref{eqn:197})}. Then $\til{\gamma}$ is the coefficient of $\gamma|_Z$;
Namely
\[ \gamma|_Z = \til{\gamma} \cdot \opn{or}(Z) . \]
\end{lem}

\begin{proof}
This amounts to expanding the formula in Definition \ref{dfn:32} into
coordinates.
\end{proof}

\begin{lem} \label{lem:39}
Let $(\sigma, \tau)$ be a balloon in $(X, x_0)$. Then
\[ \opn{MI} \bigl(\alpha, \beta \vert \partial (\sigma, \tau) \bigr) 
\in H_0 . \]
\end{lem}

\begin{proof}
By definition we have
\[ \opn{MI} \bigl(\alpha, \beta \vert \partial (\sigma, \tau) \bigr) = 
\prod_{i = 1, \ldots, 6} \,
\opn{MI} \bigl(\alpha, \beta \vert (\sigma, \tau) \circ 
(\sigma^{\flat}_i, \tau^{\flat}_i) \bigr)  \]
in the notation of Definition \ref{dfn:36}.
For every index $i$ we have, by Theorem \ref{thm:1}, an equality
\[ \Phi_0 \bigl( \opn{MI} \bigl(\alpha, \beta \vert (\sigma, \tau) \circ 
(\sigma^{\flat}_i, \tau^{\flat}_i) \bigr) =
\opn{MI} \bigl(\alpha \vert \partial \bigl(
(\sigma, \tau) \circ (\sigma^{\flat}_i, \tau^{\flat}_i) \bigr) \bigr)  \]
in the group $G$. 
Now from Figure \ref{fig:46} we see that the closed string
\[ \partial \partial \mbf{I}^3 =
\prod_{i = 1, \ldots, 6} \, \partial (\sigma^{\flat}_i, \tau^{\flat}_i) \]
is cancellation equivalent to the empty string in the monoid of strings
in $\mbf{I}^3$. Therefore the closed string
\[ \partial \partial (\sigma, \tau) = 
\prod_{i = 1, \ldots, 6} \, \partial \bigl(
(\sigma, \tau) \circ (\sigma^{\flat}_i, \tau^{\flat}_i) \bigr) \]
is cancellation equivalent to the empty string in the monoid of strings in 
$X$. By Proposition \ref{prop:1} we can conclude that 
\[ \prod_{i = 1, \ldots, 6} \,
\opn{MI} \bigl(\alpha, \beta \vert \partial \bigl(
(\sigma, \tau) \circ (\sigma^{\flat}_i, \tau^{\flat}_i) \bigr) \bigr) = 1 \]
in $G$. Hence
\[ \Phi_0 \bigl( 
\opn{MI} \bigl(\alpha, \beta \vert \partial (\sigma, \tau) \bigr)
\bigr) = 1 . \]
\end{proof}

\begin{lem} \label{lem:40}
Let $(\sigma, \tau)$ be a balloon in $(X, x_0)$. Then there is a piecewise
linear map $f : (\mbf{I}^3, v_0) \to (X, x_0)$, and a cubical balloon 
$(\sigma', \tau')$ in $(\mbf{I}^3, v_0)$, such that 
$\opn{len}(\sigma') \leq 2$, $f|_{\tau'(\mbf{I}^3)}$ is linear, and
\[ (\sigma, \tau) = f \circ (\sigma', \tau') \]
as balloons in $(X, x_0)$.
\end{lem}

\begin{proof}
Just like the proof of Proposition \ref{prop:14}.
\end{proof}

\begin{lem} \label{lem:25}
Let $(\sigma, \tau)$ be a balloon in $(X, x_0)$. 
Take any $k \geq 0$. Then 
\[ \opn{MI} \bigl( \alpha, \beta \vert  
\partial(\opn{tes}^k (\sigma, \tau)) \bigr) =
\opn{MI} \bigl( \alpha, \beta \vert  \partial (\sigma, \tau ) \bigl) . \]
\end{lem}

\begin{proof}
Due to the recursive nature of the tessellations it is enough to consider the
case $k=1$. As in the first paragraph in the proof of Lemma \ref{lem:41}, and
using Lemma \ref{lem:40}, we can assume that 
$(X, x_0) = (\mbf{I}^2, v_0)$ and 
$(\sigma, \tau) = (\sigma^0_1, \tau^0_1)$, the basic balloon.

The assertion is now an easy consequence of Lemma \ref{lem:24} and Corollary 
\ref{cor:2}.
\end{proof}

\begin{thm}[Nonabelian $3$-dimensional Stokes Theorem]
\label{thm:10}
\index{Nonabelian Stokes Theorem for cubes}
Let $(X, x_0)$ be a pointed polyhedron, let
$\mbf{C} / X$ be a Lie quasi crossed module with additive feedback, 
let $(\alpha, \beta)$ be a piecewise smooth connection-curvature pair in 
$\mbf{C} / X$, and let $\gamma$ be the $3$-curvature of $(\alpha, \beta)$.
Then:
\begin{enumerate}
\item The form $\gamma$ is inert. 
\item For any balloon $(\sigma, \tau)$ in $(X, x_0)$ one has
\[  \opn{MI} \bigl( \alpha, \beta \vert \partial (\sigma, \tau)
\bigr) = 
\opn{MI} (\alpha, \gamma \vert \tau)  \]
in $H$.
\end{enumerate}
\end{thm}

Note that assertion (1) of the theorem is a {\em generalized Bianchi identity}. 

\begin{proof}
(1) Since $\gamma$ is a $3$-form, it is enough to prove that the form 
$\gamma|_Z \in \Omega_{\mrm{pws}}^3(Z) \otimes \h$
is inert for every cube $Z$ in $X$. 
Given such a cube $Z$, choose a linear map $f : \mbf{I}^3 \to X$
such that $Z = f(\mbf{I}^3)$. Then $\gamma|_Z$ is inert if and only if
$f^*(\gamma) \in \Omega^3_{\mrm{pws}}(\mbf{I}^3) \otimes \h$
is inert, with respect to the induced Lie quasi crossed module with additive
feedback $f^*(\mbf{C} / X)$. Hence we might as well assume that 
$(X, x_0) = (\mbf{I}^3, v_0)$. 

Now the singular locus of $\alpha$ and the singular locus of $\beta$ are
contained in a finite union of polygons in $\mbf{I}^3$. So by continuity it is
enough to show that $\gamma|_Z$ is inert for cubes
$Z \subset \mbf{I}^3$ such that $\alpha|_Z$ and $\beta|_Z$ are smooth. 
In this case $\gamma$ is also smooth. 

Given such a cube $Z$, choose an orientation on it, and let
$\til{\gamma} \in \mcal{O}(Z) \otimes \h$ be the coefficient of 
$\gamma|_Z$ (in the sense of Definition \ref{dfn:24}). 
We have to prove that the function $\til{\gamma}$ is inert; namely that 
$\til{\gamma}(z) \in \opn{Ker}(\Phi_X(z))$ for every $z \in Z$. 
Again by continuity, it is enough to look at $z \in \opn{Int} Z$.

We are allowed to move the cube $Z$ around the point $z$ and to shrink it. 
Hence it is enough
to take an  $(\alpha, \beta)$-tiny balloon $(\sigma, \tau)$, and 
to show that $\til{\gamma}(z) \in \opn{Ker}(\Phi_X(z))$ for the midpoint
$z := \tau(\smfrac{1}{2}, \smfrac{1}{2}, \smfrac{1}{2})$ of
$Z := \tau(\mbf{I}^3)$. 

Let $g$ and $g_0$ be the group elements from equation
(\ref{eqn:215}). By Lemma \ref{lem:39} we have 
\[ \opn{MI} \bigl( \alpha, \beta \vert \partial (\sigma, \tau) \in H_0 , \]
and by Lemma \ref{lem:26} we have
\[ \opn{MI} \bigl( \alpha, \beta \vert 
\partial (\sigma, \tau) \bigr) \in V_0(H) . \]
Taking logarithms we see that 
\[ \log_H \bigl( \opn{MI} \bigl( \alpha, \beta \vert \partial (\sigma, \tau)
\bigr) \in \h_0 . \]
By Lemma \ref{lem:49} it follows that the distance of the
element \lb $\Psi_{\h}(g \cdot g_0)(\til{\gamma}(z))$ from the linear subspace
$\h_0$ is at most $c_{10} \cdot \epsilon^4$.

Now by Proposition \ref{prop:13}(1) there is a uniform bound on the norm of the
operator $\Psi_{\h}(g \cdot g_0)^{-1}$; say $c'$. So the distance of
$\til{\gamma}(z)$
from the subspace
$\opn{Ker}(\Phi_X(z)) \subset \h$
is at most $c' \cdot c \cdot \epsilon$.

Since we can make $\epsilon$ arbitrarily small, we conclude that
$\til{\gamma}(z) \in \lb \opn{Ker}(\Phi_X(z))$. 

\medskip \noindent
(2) By the functoriality of 
$\opn{MI} \bigl( \alpha, \beta \vert \partial (\sigma, \tau)\bigr)$
and 
$\opn{MI} (\alpha, \gamma \vert \tau)$
(see Propositions \ref{prop:10} and \ref{prop:20}), and using the construction
of Lemma \ref{lem:40}, we can assume that 
$(X, x_0) = (\mbf{I}^3, v_0)$ and 
$\opn{len}(\sigma) \leq 2$. 

Take any $k \geq 0$. Consider the sequence
\[ \opn{tes}^k(\sigma, \tau) = 
\bigl( (\sigma, \tau) \circ (\sigma^{k}_i, \tau^{k}_i) 
\bigr)_{i = 1, \ldots, 8^k} \]
which was defined in Subsection \ref{subsec:ballbound}.
The twisted multiplicative integration of inert forms is multiplicative:
\[ \opn{MI} (\alpha, \gamma \vert \tau) = 
\prod_{i = 1, \ldots, 8^k} \, 
\opn{MI} \bigl( \alpha, \gamma \vert \tau \circ \tau^k_i) . \]
On the other hand, by Lemma \ref{lem:25} we know that
\[ \opn{MI} \bigl( \alpha, \beta \vert \partial (\sigma, \tau) \bigr) = 
\prod_{i = 1, \ldots, 8^k} \, 
\opn{MI} \bigl( \alpha, \beta \vert \partial
((\sigma, \tau) \circ (\sigma^{k}_i, \tau^{k}_i)) \bigr) . \]
So it suffices to prove that 
\[ \opn{MI} \bigl( \alpha, \beta \vert \partial
((\sigma, \tau) \circ (\sigma^{k}_i, \tau^{k}_i)) \bigr) =
\opn{MI} \bigl( \alpha, \gamma \vert \tau \circ \tau^k_i) \]
for every $i \in \{ 1, \ldots, 8^k \}$. 

If $k$ is large enough then all the balloons in
$\opn{tes}^k (\sigma, \tau)$
are $(\alpha, \beta)$-tiny. We conclude that it suffices to prove 
the equality
\[  \opn{MI} \bigl( \alpha, \beta \vert \partial (\sigma, \tau)
\bigr) = 
\opn{MI} (\alpha, \gamma \vert \tau)  \]
for an $(\alpha, \beta)$-tiny balloon $(\sigma, \tau)$ in $(\mbf{I}^3, v_0)$.

Suppose we are given an $(\alpha, \beta)$-tiny balloon $(\sigma, \tau)$, and a
natural number $k$. Let $\epsilon := \opn{side}(\tau)$. 
For any index $i \in \{ 1, \ldots, 8^k \}$ let
$Z_i := \lb (\tau \circ \tau^k_i)(\mbf{I}^3)$, which is an oriented cube in
$\mbf{I}^3$ of side $(\smfrac{1}{2})^k \cdot \epsilon$, and let
$z_i :=  (\tau \circ \tau^k_i)(\smfrac{1}{2}, \smfrac{1}{2}, \smfrac{1}{2})$.
Define
\[ \opn{good}(\tau, k) := \{ i \mid \alpha|_{Z_i} \textup{ and } 
\beta|_{Z_i} \textup { are smooth } \} , \]
and define $\opn{bad}(\tau, k)$ to be the complement of $\opn{good}(\tau, k)$ in
$\{ 1, \ldots, 8^k \}$.
Since the singular loci of $\alpha$ and $\beta$ are contained in a finite union
of polygons, it follows that 
\[ \abs{ \opn{bad}(\tau, k) } \leq 
a_2(\alpha, \beta) \cdot 4^k + a_0(\alpha, \beta) \]
for some constants $a_0(\alpha, \beta), a_2(\alpha, \beta)$, that are
independent of $k$; cf.\ Lemma \ref{lem:51}.

For $i \in \opn{good}(\tau, k)$ let
$\til{\gamma}_i \in \mcal{O}(Z_i) \otimes \h$ be the coefficient of 
$\gamma|_{Z_i}$, in the sense of Definition \tup{\ref{dfn:24}}, 
and let
\[ \mu_i := (\smfrac{1}{2})^{3k} \cdot \epsilon^3 \cdot 
\Psi_{\h, \alpha}(\til{\gamma}_i)(z_i) \in \h_0  . \]
According to Lemmas \ref{lem:49} and \ref{lem:48} we know that 
\[ \Norm{ \log_H \bigl( \opn{MI} \bigl(\alpha, \beta \vert 
\partial ( (\sigma, \tau) \circ (\sigma^k_i, \tau^k_i) ) \bigr) \bigr)
- \mu_i } \leq 
(\smfrac{1}{2})^{4k} \cdot \epsilon^4 \cdot c_{10}(\alpha, \beta) \, .\]

On the other hand, for $i \in \opn{bad}(\tau, k)$ let
$\mu_i := 0 \in \h$. 
According to Lemma \ref{lem:26} we have the inequality
\[ \Norm{ \log_H \bigl( \opn{MI} \bigl(\alpha, \beta \vert 
\partial ( (\sigma, \tau) \circ (\sigma^k_i, \tau^k_i) ) \bigr) \bigr)
- \mu_i } \leq 
(\smfrac{1}{2})^{3k} \cdot \epsilon^3 \cdot c_6(\alpha, \beta) \, .\]

Let 
\[ \opn{RS}_k(\alpha, \gamma \vert \tau) := 
\sum_{i = 1}^{8^k} \, \mu_i \in \h_0 . \]
Applying property (iv) of Theorem \ref{thm:6} with the inequalities above we
get
\[ \begin{aligned}
& \Norm{ \log_H \bigl( \opn{MI} \bigl(\alpha, \beta \vert \sigma, \tau \bigr)
\bigr) - \opn{RS}_k(\alpha, \gamma \vert \tau) } \\
& \qquad \leq 
c_0(H) \cdot \bigl( 
8^k \cdot (\smfrac{1}{2})^{4k} \cdot \epsilon^4 \cdot c_{10}(\alpha, \beta) 
\\
& \qquad \qquad +
(a_2(\alpha, \beta) \cdot 4^k + a_0(\alpha, \beta)) \cdot 
(\smfrac{1}{2})^{3k} \cdot \epsilon^3 \cdot c_6(\alpha, \beta) \bigr) .
\end{aligned} \]
We see that the difference tends to $0$ as $k \to \infty$. But
\[ \lim_{k \to  \infty} \opn{RS}_k(\alpha, \gamma \vert \tau) = 
\log_H \bigl( \opn{MI}(\alpha, \gamma \vert \tau) \bigr) . \]
\end{proof}

\begin{rem}
Part (1) of Theorem \ref{thm:10} is a variant of the Bianchi identity.
\end{rem}













\cleardoublepage
