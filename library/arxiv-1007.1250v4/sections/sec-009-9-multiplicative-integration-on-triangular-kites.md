---
doc_id: arxiv-1007.1250v4
doc_title: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES"
section_id: sec-009-9-multiplicative-integration-on-triangular-kites
section_title: "Multiplicative Integration on Triangular Kites"
section_number: 9
pages: 125-137
source_pdf: 1007.1250v4.pdf
source_sha256: 541ba4fb3068de8b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.973
doc_brief: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES — We construct a 2-dimensional twisted nonabelian multiplicative integral."
---
\label{sec:simpl}

In this section $(X, x_0)$ is a pointed manifold. 
Recall that by Convention \ref{conv:500} this means that $X$ is a smooth
manifold with sharp
corners (cf.\ Definition \ref{dfn:505}); so it could be a polyhedron.
We introduce triangular kites in $(X, x_0)$ and the corresponding multiplicative
integration. 


\subsection{Triangular Kites and balloons}

Recall that the polyhedra $\mbf{I}^1$ and $\bsym{\Delta}^1$ are identified via
the linear isomorphism $\bsym{\Delta}^1 \iso \mbf{I}^1$ that on vertices is
$(v_0, v_1) \mapsto (v_0, v_1)$. 

A {\em piecewise smooth path} in $X$ is a 
piecewise smooth map $\sigma: \mbf{I}^1 \to X$. 
When convenient we shall view such a path as a piecewise smooth map 
$\bsym{\Delta}^1 \to X$ using the identification above.

Suppose $\sigma_1, \sigma_2 : \mbf{I}^1 \to X$ are piecewise smooth paths
satisfying $\sigma_1(v_1) = \sigma_2(v_0)$. 
Their {\em product} is the piecewise smooth path
\[ \sigma_1 * \sigma_2 : \mbf{I}^1 \to X \]
defined as follows:
\[ (\sigma_1 * \sigma_2)(a) := 
\begin{cases}
\sigma_1(2 a) & \text{ if } 0 \leq a \leq \smfrac{1}{2} \\
\sigma_2(2 a - 1) & \text{ if } \smfrac{1}{2} \leq a \leq 1 .
\end{cases} \]
Note that this is the standard product used in homotopy theory, and it is
distinct from the concatenation operation on strings. In particular this product
is not associative nor unital.

The {\em inverse} of a piecewise smooth path
$\sigma : \mbf{I}^1 \to X$ is the piecewise smooth path
$\sigma^{-1} : \mbf{I}^1 \to X$ defined by
\[ \sigma^{-1}(a) := \sigma(1 - a) . \]

Suppose $Z$ is a polyhedron, $f : Z \to X$ is a piecewise smooth map, and 
$\sigma = (\sigma_1, \ldots, \sigma_m)$ is a
string in $Z$, with $m \geq 1$. This data gives rise to a piecewise smooth path
$f \circ \sigma$ in $X$ defined as follows:
\begin{equation} \label{eqn:227}
f \circ \sigma := \bigl( (f \circ \sigma_1) * (f \circ \sigma_2) \bigr)
* \cdots * (f \circ \sigma_m) .
\end{equation}
In this formula we view each $f \circ \sigma_i$ as a piecewise smooth path in
$X$, and the multiplication $*$ is that of paths. 
For the empty string $\sigma$ (i.e.\ $m = 0$) the path 
$f \circ \sigma$ is not always defined; but if $X$ has a base point $x_0$, then
we usually define $f \circ \sigma$ to be the constant path $x_0$.

\begin{dfn}
A {\em piecewise smooth triangular kite}
\index{Piecewise smooth triangular kite}
in $(X, x_0)$ is a pair 
$(\sigma, \tau)$, consisting of piecewise smooth maps
$\sigma : \mbf{I}^1 \to X$ and
$\tau : \bsym{\Delta}^2 \to X$, 
satisfying $\sigma(v_0) = x_0$ and
$\sigma(v_1) = \tau(v_0)$.
\end{dfn}

See Figure \ref{fig:80} for an illustration.

The {\em boundary} of $\bsym{\Delta}^2$ is the string
\begin{equation} \label{eqn:160}
\partial \bsym{\Delta}^2 := (v_0, v_1) * (v_1, v_2) * (v_2, v_0) 
\end{equation}
(consisting of $3$ pieces) in $\bsym{\Delta}^2$.

\begin{dfn} \label{dfn:31}
Let $(\sigma, \tau)$ be a piecewise smooth triangular kite in \lb $(X, x_0)$. 
Its {\em boundary} is the piecewise smooth path
\[ \partial (\sigma, \tau) := \bigl( \sigma * 
(\tau \circ \partial \bsym{\Delta}^2) \bigr) * \sigma^{-1} . \]
\end{dfn}

See Figure \ref{fig:81}.

\begin{dfn}
A {\em piecewise smooth triangular balloon} 
\index{Piecewise smooth triangular balloon}
in $(X, x_0)$ is a pair 
$(\sigma, \tau)$, consisting of piecewise smooth maps
$\sigma : \mbf{I}^1 \to X$ and
$\tau : \bsym{\Delta}^3 \to X$, 
satisfying $\sigma(v_0) = x_0$ and
$\sigma(v_1) = \tau(v_0)$.
\end{dfn}

See Figure \ref{fig:82} for an illustration.

Let $(Z, z_0)$ be a pointed polyhedron. 
By {\em linear triangular kite} in $(Z, z_0)$ we mean the obvious variant of
linear quadrangular kite. Namely this is a pair 
$(\sigma, \tau)$, consisting of a string $\sigma$ in $Z$ and a linear map
$\tau : \bsym{\Delta}^3 \to X$. These must satisfy 
$\sigma(v_0) = z_0$ and
$\sigma(v_1) = \tau(v_0)$.
Likewise we define {\em linear triangular balloons}.

\begin{dfn}
The {\em boundary} of $\bsym{\Delta}^3$ is the sequence of linear triangular
kites
\[ \partial \bsym{\Delta}^3 =
\bigl( \partial_1 \bsym{\Delta}^3, 
\partial_2 \bsym{\Delta}^3, 
\partial_3 \bsym{\Delta}^3, 
\partial_4 \bsym{\Delta}^3 \bigr) \]
in $(\bsym{\Delta}^3, v_0)$
defined as follows.
\begin{itemize}
\item Let $\sigma^{\flat}_2, \sigma^{\flat}_3, \sigma^{\flat}_4$ be the
empty strings in $\bsym{\Delta}^3$.  And let 
$\sigma^{\flat}_1 : \mbf{I}^1 \to \bsym{\Delta}^3$ 
be the linear map defined on vertices by
\[ \sigma^{\flat}_1(v_0, v_1) := (v_0, v_1) . \]

\item Let 
$\tau^{\flat}_i : \bsym{\Delta}^2 \to \bsym{\Delta}^3$
be the linear maps given on vertices by:
\[ \tau^{\flat}_1(v_0, v_1, v_2) := (v_1, v_2, v_3) , \]
\[ \tau^{\flat}_2(v_0, v_1, v_2) := (v_0, v_1, v_3) , \]
\[ \tau^{\flat}_3(v_0, v_1, v_2) := (v_0, v_3, v_2) , \]
\[ \tau^{\flat}_4(v_0, v_1, v_2) := (v_0, v_2, v_1) . \]

\item The kite are 
\[ \partial_i \bsym{\Delta}^3 := (\sigma^{\flat}_i, \tau^{\flat}_i) . \]
\end{itemize}
\end{dfn}

See Figure \ref{fig:83}.

Warning: the kites $(\sigma^{\flat}_i, \tau^{\flat}_i)$ above should be confused
with the quadrangular kites from Definition \ref{dfn:36}, despite the shared
notation. 

\begin{figure} 
\includegraphics[scale=0.3]{fig83.jpg}
\caption{The boundary of $\mbf{\Delta}^3$.} 
\label{fig:83}
\end{figure}

\begin{dfn} \label{dfn:30}
Let $(\sigma, \tau)$ be a piecewise smooth triangular balloon in $(X, x_0)$. Its
{\em
boundary} is the sequence of piecewise smooth triangular kites
\[ \partial (\sigma, \tau) :=
\bigl( \partial_1 (\sigma, \tau), \, \partial_2 (\sigma, \tau), \,
\partial_3 (\sigma, \tau), \, \partial_4 (\sigma, \tau) \bigr) \]
in $(X, x_0)$, where
\[ \partial_i (\sigma, \tau) :=  
(\sigma, \tau)  \circ (\sigma^{\flat}_i, \tau^{\flat}_i) . \]
\end{dfn}

See Figure \ref{fig:86} for an illustration.



\subsection{MI on Triangular Kites}
As before, $(X, x_0)$ is a pointed manifold.

Let
\[ \mbf{C} := (G, H, \Psi, \Phi_0) \]
be a Lie quasi crossed module (Definition \ref{dfn:22}). As usual we write
$\g := \opn{Lie}(G)$ and $\h := \opn{Lie}(H)$. 
An additive feedback for 
$\mbf{C}$ over $(X, x_0)$ is an element
\[ \Phi_X \in \mcal{O}(X) \otimes \opn{Hom}(\h, \g) \]
satisfying condition ($**$) of Definition \ref{dfn:21}.
Just like in Definition \ref{dfn:6}, we call the data 
\[ \mbf{C} / X := (G, H, \Psi, \Phi_0, \Phi_X) \]
a {\em Lie quasi crossed module with additive feedback} over $(X, x_0)$.

\begin{dfn}
Let $\alpha \in \Omega^1(X) \otimes \g$, and let $\sigma$ be a piecewise smooth
path in $X$.
Consider the piecewise smooth differential form
\[ \alpha' := \sigma^*(\alpha) \in 
\Omega^1_{\mrm{pws}}(\mbf{I}^1) \otimes \g . \]
We define
\[ \opn{MI}(\alpha \vert \sigma) := 
\opn{MI}(\alpha' \vert \mbf{I}^1) \in G  \]
(cf.\ Definition \ref{dfn:28}).
\end{dfn}

\begin{prop} \label{prop:23}
Let $\alpha \in \Omega^1(X) \otimes \g$.
\begin{enumerate}
\item Suppose $\sigma_1$ and $\sigma_2$ are piecewise smooth paths in $X$ such
that 
$\sigma_1 * \sigma_2$ is defined. Then
\[ \opn{MI}(\alpha \vert \sigma_1 * \sigma_2) = 
\opn{MI}(\alpha \vert \sigma_1) \cdot \opn{MI}(\alpha \vert \sigma_2) . \]

\item Let $\sigma$ be a piecewise smooth path in $X$. Then
\[ \opn{MI}(\alpha \vert \sigma^{-1}) = \opn{MI}(\alpha \vert \sigma)^{-1} . \]

\item Suppose $\sigma'$ is a string in a polyhedron $Z$, $f : Z \to X$ is a
piecewise smooth map, and 
$\sigma := f \circ \sigma'$ is the path in $X$ gotten by the operation
\tup{(\ref{eqn:227})}. Then
\[ \opn{MI}(\alpha \vert \sigma) = 
\opn{MI}(f^*(\alpha) \vert \sigma') . \]
\end{enumerate}
\end{prop}

\begin{proof}
(1) We could use the $2$-dimensional Stokes Theorem; but there is an elementary
proof. Let 
$\sigma^1_1, \sigma^1_2 : \mbf{I}^1 \to \mbf{I}^1$ be the linear maps belonging
to $\opn{tes}^1 \mbf{I}^1$, as in Definition \ref{dfn:41}. 
Let $\sigma : \mbf{I}^1 \to X$ be the piecewise smooth map such that
$\sigma \circ \sigma^1_i = \sigma_i$
for $i = 1, 2$. And let $\alpha' := \sigma^*(\alpha)$. 
Now by definition of $*$ we have
$\sigma = \sigma_1 * \sigma_2$ as paths in $X$. Hence
\[ \opn{MI}(\alpha \vert \sigma_1 * \sigma_2) = 
\opn{MI}(\alpha \vert \sigma) = \opn{MI}(\alpha' \vert \mbf{I}^1) . \]
Likewise
\[ \opn{MI}(\alpha \vert \sigma_i) = 
\opn{MI}(\alpha \vert \sigma \circ \sigma^1_i) = 
\opn{MI}(\alpha' \vert \sigma^1_i) . \]
On the other hand, by Proposition \ref{prop:5}(3) we know that
\[ \opn{MI}(\alpha' \vert \mbf{I}^1) = 
\opn{MI}(\alpha' \vert \sigma^1_1) \cdot \opn{MI}(\alpha' \vert \sigma^1_2)  .
\]

\medskip \noindent
(2) This is immediate from Proposition \ref{prop:1}(2).

\medskip \noindent
(3) This follows part (1) and induction on the number of pieces in the string
$\sigma'$.
\end{proof}

In order to define MI on triangular kites we shall need the following geometric
construction. Consider the linear triangular kite 
$(\sigma', \tau')$ in $(\mbf{I}^2, v_0)$, where the string $\sigma'$ has one
linear piece $\sigma' : \mbf{I}^1 \to \mbf{I}^2$ defined on vertices by
\[ \sigma'(v_0, v_1) := (v_0, (\smfrac{1}{2}, \smfrac{1}{2}) ) . \]
The linear map 
$\tau' : \bsym{\Delta}^2 \to \mbf{I}^2$ is defined on vertices by
\[ \tau'(v_0, v_1, v_2) := ( (\smfrac{1}{2}, \smfrac{1}{2}),
(1, \smfrac{1}{2}), (\smfrac{1}{2}, 1) ) . \]
We also need the linear quadrangular kite 
$(\sigma', \tau'')$ in $(\mbf{I}^2, v_0)$, where the linear map 
$\tau'' : \mbf{I}^2 \to \mbf{I}^2$ is defined on vertices by
\[ \tau''(v_0, v_1, v_2) := ( (\smfrac{1}{2}, \smfrac{1}{2}),
(1, \smfrac{1}{2}), (\smfrac{1}{2}, 1) ) . \]
We write
$Z := \sigma'(\mbf{I}^1)$ and $Y := \tau'(\bsym{\Delta}^2)$. 

Consider the  canonical  linear embedding 
$\bsym{\Delta}^2 \to  \mbf{I}^2$ 
which on vertices is
\[ (v_0, v_1, v_2) \mapsto (v_0, v_1, v_2) . \]
Let $h : \mbf{I}^2 \to \bsym{\Delta}^2$ be the piecewise linear retraction
which is linear on $\bsym{\Delta}^2$ and on the the triangle complementary to
it, and satisfies $h(1, 1) = v_1$. See Figure \ref{fig:55}.

\begin{lem}
There exists a piecewise linear retraction
$g : \mbf{I}^2 \to Y \cup Z$, such that
\[ g \circ \tau'' = \tau' \circ h \]
as piecewise linear maps $\mbf{I}^2 \to \mbf{I}^2$.
\end{lem}

\begin{proof}
Easy exercise. Cf.\ proof of Proposition \ref{prop:14}. And see Figure
\ref{fig:84}.
\end{proof}

\begin{figure} 
\includegraphics[scale=0.23]{fig55.jpg}
\caption{The piecewise linear retraction $h : \mbf{I}^2 \to \bsym{\Delta}^2$.} 
\label{fig:55}
\end{figure}

\begin{figure} 
\includegraphics[scale=0.29]{fig84.jpg}
\caption{The piecewise linear retraction $g : \mbf{I}^2 \to Y \cup Z$.
Here $w := (\smfrac{1}{2}, \smfrac{1}{2})$.} 
\label{fig:84}
\end{figure}


\begin{figure} 
\includegraphics[scale=0.35]{fig85.jpg}
\caption{The piecewise smooth map $f : \mbf{I}^2 \to X$
such that 
$f \circ (\sigma', \tau') = (\sigma, \tau)$.} 
\label{fig:85}
\end{figure}

Let us fix such a retraction $g$, which we also view as a piecewise linear map
$g : \mbf{I}^2 \to \mbf{I}^2$. 

\begin{dfn} \label{dfn:42}
\index{Multiplicative integral on triangular kites}
Let $\alpha \in \Omega^1(X) \otimes \g$ and 
$\beta \in \Omega^1(X) \otimes \h$. Given a piecewise smooth triangular kite 
$(\sigma, \tau)$ in $(X, x_0)$ we define its {\em multiplicative integral}
\[  \opn{MI}(\alpha, \beta \vert \sigma, \tau) \in H \]
as follows. Let $f : \mbf{I}^2 \to X$ be the unique piecewise smooth map such
that:
\begin{itemize}
\item $f \circ \sigma'  = \sigma$ as maps
$\mbf{I}^1 \to X$.
\item $f \circ \tau'  = \tau$ as maps
$\bsym{\Delta}^2 \to X$.
\item $f = f \circ g$ as maps $\mbf{I}^2 \to X$, where 
$g : \mbf{I}^2 \to \mbf{I}^2$ is the chosen retraction.
\end{itemize}
(See Figure \ref{fig:85}.) 
We get differential forms
\[ \alpha' := f^*(\alpha) \in 
\Omega^1_{\mrm{pws}}(\mbf{I}^2) \otimes \g \]
and
\[ \beta' := f^*(\beta) \in 
\Omega^2_{\mrm{pws}}(\mbf{I}^2) \otimes \h . \]
We define
\[ \opn{MI}(\alpha, \beta \vert \sigma, \tau) :=
\opn{MI}(\alpha', \beta' \vert \sigma', \tau'') , \]
where $(\sigma', \tau'')$ is the linear quadrangular kite in
$(\mbf{I}^2, v_0)$ defined above, and \lb
$\opn{MI}(\alpha', \beta' \vert \sigma', \tau'')$
is the multiplicative integral from Definition \ref{dfn:16}.
\end{dfn}

This definition might seem strange; but we shall soon see that it has all the
expected good properties.

\begin{prop}[Functoriality in $X$]
Let $e : (Y, y_0) \to (X, x_0)$ be a map of pointed manifolds, let
$\alpha \in \Omega^1(X) \otimes \g$, let
$\beta \in \Omega^2(X) \otimes \h$, 
and let $(\sigma, \tau)$ be a piecewise smooth triangular kite in $(Y, y_0)$.
Then
\[ \opn{MI}(\alpha, \beta \vert e \circ \sigma, e \circ \tau) = 
\opn{MI} \bigl( e^*(\alpha), e^*(\beta) \vert  \sigma, \tau \bigl) , \]
where the latter is calculated with respect to the Lie quasi crossed module
with additive feedback $e^*(\mbf{C} / X)$.
\end{prop}

\begin{proof}
This is immediate from the definition, since 
$(e \circ f)^* = f^* \circ e^*$ for a piecewise smooth map 
$f : \mbf{I}^2 \to Y$.
\end{proof}

\begin{prop}[Comparison to Quadrangular Kites] \label{prop:24}
Let $(Z, z_0)$ be a pointed polyhedron, 
$e : (Z, z_0) \to (X, x_0)$ a piecewise smooth map preserving base points, 
$(\sigma, \tau)$ a piecewise smooth triangular kite in $(X, x_0)$, 
$(\sigma', \tau')$ a  linear quadrangular kite in $(Z, z_0)$, 
$\alpha \in \Omega^1(X) \otimes \g$ and $\beta \in \Omega^2(X) \otimes \h$.
Assume that $\sigma = e \circ \sigma'$ as paths in $X$, and 
$\tau \circ h = e \circ \tau'$ as maps $\mbf{I}^2 \to X$, where
$h : \mbf{I}^2 \to \bsym{\Delta}^2$ is the retraction in
Figure \tup{\ref{fig:55}}.
Then
\[ \opn{MI}(\alpha, \beta \vert \sigma, \tau) =
\opn{MI}(e^*(\alpha), e^*(\beta) \vert \sigma', \tau') , \]
where the latter is calculated with respect to the Lie quasi crossed module
with additive feedback $e^*(\mbf{C} / X)$.
\end{prop}

\begin{proof}
The piecewise smooth map $f : \mbf{I}^2 \to X$ used in Definition \ref{dfn:42}
can be factored as $f = e \circ f'$ for a piecewise linear map 
$f' : (\mbf{I}^2, v_0) \to (Z, z_0)$ of pointed polyhedra.
The assertion now follows from Proposition \ref{prop:10}.
\end{proof}

The notion of compatible connection from Definition \ref{dfn:8} makes sense
here too, only we have to consider 
$\alpha \in \Omega^1(X) \otimes \g$
(and replace ``string'' with ``piecewise smooth path''). 

\begin{prop}[Moving the Base Point] \label{prop:25}
Let $\alpha \in \Omega^1(X) \otimes \g$
be a connection compatible with $\mbf{C} / X$, and let
$\rho$ be a piecewise smooth path in $X$, with initial point $x_0$ and terminal
point $x_1$. Define
$g := \opn{MI}(\alpha \vert \rho)$, 
and let
\[ \mbf{C}^g / X = (G, H^g, \Psi, \Phi_0^g, \Phi_X) \]
be the Lie quasi crossed module with additive feedback over $(X, x_1)$
constructed in Subsection \tup{\ref{subsec:moving}}.
Given a form 
$\beta \in \Omega^2(X) \otimes \h$ and a piecewise smooth triangular kite
$(\sigma, \tau)$ in  $(X, x_1)$, consider the element
\[ \opn{MI}^g(\alpha, \beta \vert \sigma, \tau) \in H^g  \]
calculated with respect to the Lie quasi crossed module
with additive feedback $\mbf{C}^g / X$. Then 
\[ \Psi(g) \bigl( \opn{MI}^g(\alpha, \beta \vert \sigma, \tau) \bigr)  =
\opn{MI}(\alpha, \beta \vert \rho * \sigma, \tau)  \]
in $H$. 
\end{prop}

\begin{proof}
It is possible to find a polyhedron $Z$, points  $z_0, z_1 \in Z$, a string
$\rho'$ in $Z$ with initial point $z_0$ and terminal point $z_1$, 
a linear quadrangular kite $(\sigma', \tau')$ in 
$(Z, z_1)$ and a piecewise smooth map 
$e : Z \to X$, such that $\rho = e \circ \rho'$ as paths and 
$(\sigma, \tau) = e \circ (\sigma', \tau')$ as kites. 
Define
$\alpha' := e^*(\alpha)$ and $\beta' := e^*(\beta)$.

Let $\mbf{C}' / Z := e^*(\mbf{C} / X)$ be the induced 
Lie quasi crossed module with additive feedback over the pointed polyhedron
$(Z, z_0)$. By Proposition \ref{prop:23}(3) we know that 
$\opn{MI}(\alpha' \vert \rho') = g$. Examining the definition of
$\mbf{C}^g / X$ in Subsection \ref{subsec:moving} we see that
\[ e^*(\mbf{C}^g / X) = (\mbf{C}')^g / Z \]
as Lie quasi crossed modules with additive feedback over the pointed polyhedron
$(Z, z_1)$. Therefore 
$\opn{MI}^g(\alpha', \beta' \vert \sigma', \tau')$
is unambiguous. 

By Proposition \ref{prop:24} we know that
\[ \opn{MI}^g(\alpha', \beta' \vert \sigma', \tau') = 
\opn{MI}^g(\alpha, \beta \vert \sigma, \tau ) \]
and
\[ \opn{MI}(\alpha', \beta' \vert \rho' * \sigma', \tau') = 
\opn{MI}(\alpha, \beta \vert  \rho * \sigma, \tau ) . \]
Finally, by Theorem \ref{thm:14} we have
\[ \opn{MI}^g(\alpha', \beta' \vert \sigma', \tau') = 
\opn{MI}(\alpha', \beta' \vert \rho' * \sigma', \tau') . \]
\end{proof}




\subsection{Stokes Theorems}
We continue with the setup from before: $(X, x_0)$ is a pointed manifold, and
\[ \mbf{C} / X = (G, H, \Psi, \Phi_0, \Phi_X) \]
be a Lie quasi crossed module with additive feedback. 

Just like in Definition \ref{dfn:19}, a {\em connection-curvature pair} for
$\mbf{C} / X$ is a pair $(\alpha, \beta)$, with 
$\alpha \in \Omega^1(X) \otimes \g$ and 
$\beta \in \Omega^1(X) \otimes \h$,
such that $\alpha$ is a compatible connection, and  the differential equation
\[ \Phi_X(\beta) = \d(\alpha) + \smfrac{1}{2} [\alpha, \alpha] \]
holds in $\Omega^2(X) \otimes \g$.

Recall that for a piecewise smooth triangular kite $(\sigma, \tau)$, its
boundary
$\partial (\sigma, \tau)$ was defined in Definition \ref{dfn:31}.

\begin{thm}[Stokes Theorem for Triangles] \label{thm:520}
\index{Nonabelian Stokes Theorem for triangles}
Let $(X, x_0)$ be a pointed manifold, let
\[ \mbf{C} / X := (G, H, \Psi, \Phi_0, \Phi_X) \]
be a Lie quasi crossed module with additive feedback over $(X, x_0)$,
let $(\alpha, \beta)$ be a \lb connection-curvature pair for
$\mbf{C} / X$, and let
$(\sigma, \tau)$ be a piecewise smooth triangular kite in $(X, x_0)$. Then
\[ \Phi_0 \bigl( \opn{MI}(\alpha, \beta \vert \sigma, \tau) \bigr) = 
\opn{MI}(\alpha, \beta \vert \partial (\sigma, \tau)) . \]
\end{thm}

\begin{proof}
As in the proof of Proposition \ref{prop:25}, we can find a pointed
polyhedron $(Z, z_0)$, a linear quadrangular kite $(\sigma', \tau')$ in 
$(Z, z_0)$ and a piecewise smooth map $f : Z \to X$, such that  
$(\sigma, \tau) = f \circ (\sigma', \tau')$ as kites. 
Define
$\alpha' := f^*(\alpha)$ and $\beta' := f^*(\beta)$.
According to Proposition \ref{prop:23}(3) we have
\[ \opn{MI}(\alpha, \beta \vert \partial (\sigma, \tau)) = 
\opn{MI}(\alpha' \vert \partial (\sigma', \tau')) . \]
And by Proposition \ref{prop:24} we have
\[ \opn{MI}(\alpha, \beta \vert \sigma, \tau)  = 
\opn{MI}(\alpha', \beta' \vert \sigma', \tau')  . \]
Finally by Theorem \ref{thm:1} we know that
\[ \opn{MI}(\alpha' \vert \partial (\sigma', \tau')) = 
\Phi_0 \bigl( \opn{MI}(\alpha', \beta' \vert \sigma', \tau') \bigr) . \]
\end{proof}

For the $3$-dimensional Stokes Theorem we shall need an auxiliary  geometric
construction, similar to the one in the
previous subsection. Consider the linear triangular balloon  
$(\sigma', \tau')$ in $(\mbf{I}^3, v_0)$, where the string $\sigma'$ has one
linear piece $\sigma' : \mbf{I}^1 \to \mbf{I}^3$ defined on vertices by
\[ \sigma'(v_0, v_1) := \bigl( v_0, (\smfrac{1}{2}, \smfrac{1}{2}, 0) \bigr) .
\]
The linear map 
$\tau' : \bsym{\Delta}^3 \to \mbf{I}^3$ is defined on vertices by
\[ \tau'(v_0, v_1, v_2, v_3) := \bigl( (\smfrac{1}{2}, \smfrac{1}{2}, 0),
(1, \smfrac{1}{2}, 0), (\smfrac{1}{2}, 1, 0), 
(\smfrac{1}{2}, \smfrac{1}{2}, \smfrac{1}{2}) \bigr) . \]
We also need the linear quadrangular balloon 
$(\sigma', \tau'')$ in $(\mbf{I}^3, v_0)$, where the linear map 
$\tau'' : \mbf{I}^3 \to \mbf{I}^3$ is defined on vertices by the same formula
as $\tau'$. We let 
$Z := \sigma'(\mbf{I}^1)$ and $Y := \tau'(\bsym{\Delta}^3)$.
See Figure \ref{fig:87}.

\begin{figure} 
\includegraphics[scale=0.44]{fig87.jpg}
\caption{The triangular linear balloon $(\sigma', \tau')$ and the 
quadrangular linear balloon $(\sigma', \tau'')$ in the 
pointed polyhedron $(\mbf{I}^3, v_0)$.} 
\label{fig:87}
\end{figure}
 
Consider the canonical linear embedding 
$\bsym{\Delta}^3 \to  \mbf{I}^3$ 
which on vertices is
\[ (v_0, \ldots, v_3) \mapsto (v_0, \ldots, v_3) . \]
Let $h : \mbf{I}^3 \to \bsym{\Delta}^3$ be the piecewise linear retraction
$h := h_2 \circ h_1$, where $h_1$ and $h_2$ are the retractions shown in Figure
\ref{fig:57}.

\begin{figure} 
\includegraphics[scale=0.32]{fig57.jpg}
\caption{The piecewise linear map $h_1$ retracts the cube $\mbf{I}^3$ to a
prism. The piecewise linear map $h_2$ retracts the prism to the tetrahedron
$\bsym{\Delta}^3$.} 
\label{fig:57}
\end{figure}

\begin{lem}
There is a piecewise linear retraction
$g : \mbf{I}^3 \to Z \cup Y$, such that
\[ g \circ \tau'' = \tau' \circ h \]
as maps $\mbf{I}^3 \to \mbf{I}^3$.  
\end{lem}

\begin{proof}
Nice exercise in piecewise linear geometry.
\end{proof}

Let us fix such a retraction$g$, which we also view as a piecewise linear map
$g : \mbf{I}^3 \to \mbf{I}^3$.

The notions of {\em tame connection} and 
{\em inert differential form}, from Subsections \ref{subsec:ccpair}
\ref{subsec:inert} respectively, make sense here, and all pertinent results
hold. Given a tame connection 
$\alpha \in \Omega^1(X) \otimes \g$, 
an inert form $\gamma \in \Omega^3(X) \otimes \h$
and  a piecewise smooth balloon $(\sigma, \tau)$ in $(X, x_0)$, we define the
{\em twisted
multiplicative integral}
\[ \opn{MI}(\alpha, \gamma \vert \sigma, \tau) \in H_0  \] 
as follows. Let $f : \mbf{I}^3 \to X$ be the unique piecewise smooth map
satisfying:
\begin{itemize}
\item $f \circ \sigma'  = \sigma$ as maps
$\mbf{I}^1 \to X$.
\item $f \circ \tau'  = \tau$ as maps
$\bsym{\Delta}^3 \to X$.
\item $f = f \circ g$ as maps $\mbf{I}^3 \to X$, where 
$g: \mbf{I}^3 \to \mbf{I}^3$ is the chosen retraction.
\end{itemize}
Now 
\[ \mbf{C}' / \mbf{I}^3 := f^*(\mbf{C} / X) = (G, H, \Psi, \Phi_0, f^*(\Phi_X))
\]
is a Lie quasi crossed module with additive feedback
over $(\mbf{I}^3, v_0)$,
\[ \alpha' := f^*(\alpha) \in \Omega^1_{\mrm{pws}}(\mbf{I}^3) \otimes \g \]
is a tame connection for $\mbf{C}' / X$, and 
\[ \gamma' := f^*(\gamma) \in \Omega^3_{\mrm{pws}}(\mbf{I}^3) \otimes \h \]
is an inert differential form. We define
\begin{equation} \label{eqn:161}
\opn{MI}(\alpha, \gamma \vert \sigma, \tau) :=
\opn{MI} \bigl( \alpha', \gamma' \vert \tau'') ,
\end{equation}
where $\tau'' : \mbf{I}^3 \to \mbf{I}^3$ is the linear map described above,
and 
$\opn{MI} \bigl( \alpha', \gamma' \vert \tau'')$
is the twisted multiplicative integral from Definition \ref{dfn:43}.

\begin{rem}
The reason that the path $\sigma$ is explicit in the expression \lb
$\opn{MI}(\alpha, \gamma \vert \sigma, \tau)$ 
is that this operation could depend on the homotopy class of $\sigma$, in case
the manifold $X$ is not simply connected. Since polyhedra are always simply
connected, we did not have to worry about strings in Definition \ref{dfn:43}.

It is easy to see that $\opn{MI}(\alpha, \gamma \vert \sigma, \tau)$ 
makes sense for an inert $p$-form $\gamma$ and a ``$p$-dimensional balloon''
$(\sigma, \tau)$, for any $p \geq 0$. Moreover, for $p = 2$ this coincides with
the nonabelian MI of Definition \ref{dfn:42}.
\end{rem}

Recall the boundary $\partial (\sigma, \tau)$ of a balloon 
$(\sigma, \tau)$ in $(X, x_0)$, from Definition \ref{dfn:30}.
As is our convention for the multiplicative integral of a sequence, we write
\[ \opn{MI}(\alpha, \beta \vert \partial (\sigma, \tau)) :=
\prod_{i = 1, \ldots, 4} \ 
\opn{MI}(\alpha, \beta \vert \partial_i(\sigma, \tau) ) . \]

As in Definition \ref{dfn:32}, the $3$-curvature of $(\alpha, \beta)$ is
the form
\[ \gamma := \d(\beta) + \psi_{\h}(\alpha)(\beta) \in 
\Omega^3(X) \otimes \h . \]

Here is the second version of the main result of the paper (the first version
was Theorem \ref{thm:10}.)

\begin{thm}[Stokes Theorem for Tetrahedra] \label{thm:22}
\index{Nonabelian Stokes Theorem for tetrahedra}
Let $(X, x_0)$ be a pointed manifold, let
$\mbf{C} / X$ be a Lie quasi crossed module with additive feedback, 
let $(\alpha, \beta)$ be a connection-curvature pair for 
$\mbf{C} / X$, and let $\gamma$ be the $3$-curvature of $(\alpha, \beta)$.
Then:
\begin{enumerate}
\item The differential form $\gamma$ is inert. 
\item For any piecewise smooth balloon $(\sigma, \tau)$ in $(X, x_0)$ one has
\[  \opn{MI} \bigl( \alpha, \beta \vert \partial (\sigma, \tau)
\bigr) = 
\opn{MI} (\alpha, \gamma \vert \sigma, \tau)  \]
in $H$.
\end{enumerate}
\end{thm}

\begin{proof}
(1) It suffices to prove that for any piecewise smooth map 
$f : \mbf{I}^3 \to X$ the form
\[ \gamma' := f^*(\gamma) \in \Omega^3_{\mrm{pws}}(\mbf{I}^3) \otimes \h \]
is inert. Define
\[ \alpha' := f^*(\alpha) \in \Omega^1_{\mrm{pws}}(\mbf{I}^3) \otimes \g \]
and
\[ \beta' := f^*(\beta) \in \Omega^2_{\mrm{pws}}(\mbf{I}^3) \otimes \h . \]
Then $(\alpha', \beta')$ is a connection curvature pair in 
$\mbf{C}' / \mbf{I}^3$ (this is a variant of Proposition \ref{prop:11}(1)), and
$\gamma'$ is the $3$-curvature of $(\alpha', \beta')$.
But according to Theorem \ref{thm:10}(1) the form $\gamma'$ is inert.

\medskip \noindent
(2) Let $f : (\mbf{I}^3, v_0) \to (X, x_0)$ be the pointed piecewise smooth map
constructed just before (\ref{eqn:161}). 
By definition we have
\[ \opn{MI}(\alpha, \gamma \vert \sigma, \tau) :=
\opn{MI} \bigl( \alpha', \gamma' \vert \tau'') . \]
By Proposition \ref{prop:24} we know that
\[ \opn{MI} \bigl( \alpha, \beta \vert \partial (\sigma, \tau) \bigr) = 
\opn{MI} \bigl( \alpha', \beta' \vert \partial (\sigma', \tau') \bigr) . \]
And by Theorem \ref{thm:10}(2) we know that
\[ \opn{MI} \bigl( \alpha', \beta' \vert \partial (\sigma', \tau'') \bigr) =
\opn{MI} \bigl( \alpha', \gamma' \vert \tau'') . \]
It remains to prove that
\begin{equation} \label{eqn:228}
\opn{MI} \bigl( \alpha', \beta' \vert \partial (\sigma', \tau') \bigr) = 
\opn{MI} \bigl( \alpha', \beta' \vert \partial (\sigma', \tau'') \bigr) .
\end{equation}

By definition we have
\[ \opn{MI} \bigl( \alpha', \beta' \vert \partial (\sigma', \tau') \bigr) = 
\prod_{i = 1, \ldots, 4} \ 
\opn{MI}(\alpha, \beta \vert \partial_i(\sigma', \tau') )  \]
and
\[ \opn{MI} \bigl( \alpha', \beta' \vert \partial (\sigma', \tau'') \bigr) = 
\prod_{i = 1, \ldots, 6} \ 
\opn{MI}(\alpha, \beta \vert \partial_i(\sigma', \tau'') ) . \]
Using Proposition \ref{prop:24} and looking at Figures
\ref{fig:87}, \ref{fig:83} and \ref{fig:46} we see that
\[ \opn{MI} \bigl( \alpha', \beta' \vert \partial_1(\sigma', \tau'') \bigr) = 1 
, \]
\[ \opn{MI} \bigl( \alpha', \beta' \vert \partial_2(\sigma', \tau'') \bigr) = 1
, \]
\[ \opn{MI} \bigl( \alpha', \beta' \vert \partial_3(\sigma', \tau'')  \bigr) = 
\opn{MI} \bigl( \alpha', \beta' \vert \partial_1(\sigma', \tau')  \bigr)  , \]
\[ \opn{MI} \bigl( \alpha', \beta' \vert \partial_4(\sigma', \tau'')  \bigr) = 
\opn{MI} \bigl( \alpha', \beta' \vert \partial_2(\sigma', \tau')  \bigr)  , \]
\[ \opn{MI} \bigl( \alpha', \beta' \vert \partial_5(\sigma', \tau'')  \bigr) = 
\opn{MI} \bigl( \alpha', \beta' \vert \partial_3(\sigma', \tau')  \bigr)   \]
and
\[ \opn{MI} \bigl( \alpha', \beta' \vert \partial_6(\sigma', \tau'')  \bigr) = 
\opn{MI} \bigl( \alpha', \beta' \vert \partial_4(\sigma', \tau')  \bigr) .  \]
Thus equation (\ref{eqn:228}) is true. 
\end{proof}

 

\subsection{Rationality of the Multiplicative Integral} \label{subsec:ration}
Let $\K$ be a subfield of $\R$. As common in algebraic geometry, let us denote
by $\mbf{A}^n(\K)$ the set of $\K$-rational points of $\mbf{A}^n(\R)$; namely
those points $x \in \mbf{A}^n(\R)$ whose coordinates satisfy $t_i(x) \in \K$,
$i = 1, \ldots, n$. 

By (embedded) {\em polyhedron defined over $\K$} we mean a polyhedron 
$X \subset \mbf{A}^n(\R)$, such that all the
vertices of $X$ belong to $\mbf{A}^n(\K)$. 
For such $X$, and for every field $L$ such that $\K \subset L \subset \R$, we
can talk about the set $X(L)$ of $L$-rational points of $X$.
The real polyhedron is of course $X(\R)$.

Suppose $Y$ is another polyhedron defined over $\K$. It makes sense to talk
about linear maps $f : X \to Y$ defined over $\K$. The condition is of course
that for any vertex $v \in X$ the point $f(v)$ is in $Y(\K)$. 

The simplices $\bsym{\Delta}^p$ are defined over $\mbb{Q}$. Therefore we have
the notion of linear triangulation of $X$ defined over $\K$. This lets 
us consider piecewise linear maps $f : Y \to X$ defined over $\K$.
In particular we have {\em kites in $X$ defined over
$\K$}. 

The polyhedron $X$ has a $\K$-subalgebra 
$\mcal{O}_{\mrm{alg}}(X(\K)) \subset \mcal{O}(X)$
of {\em $\K$-valued algebraic functions on $X(\K)$}, which is the restriction
to  $X(\K)$ of the polynomial algebra 
$\K[t_1, \ldots, t_n] \subset \mcal{O}(\mbf{A}^n(\R))$. 
Similarly one can define the DG algebra
$\Omega_{\mrm{alg}}(X(\K))$ of {\em $\K$-valued algebraic differential forms},
which is contained in $\Omega(X)$.
Using linear triangulations defined over $\K$ we can also consider the 
$\K$-algebra $\mcal{O}_{\mrm{pwa}}(X(\K))$ of {\em $\K$-valued piecewise
algebraic functions}, and the DG
algebra $\Omega_{\mrm{pwa}}(X(\K))$ of {\em $\K$-valued piecewise algebraic
differential forms}, which is a DG subalgebra of $\Omega_{\mrm{pws}}(X)$.

Suppose $X$ is a polyhedron and $Y \subset \mbf{A}^m$ is an
affine algebraic variety, both defined over $\K$. 
A map $f : X \to Y$ is said to be algebraic and defined over $\K$ if
for every $i$ the function $t_i \circ f : X(\K) \to \R$ belongs to
$\mcal{O}_{\mrm{alg}}(X(\K))$. Equivalently, $f$ extends to a map of algebraic
varieties $\til{f} : \mbf{A}^n \to \mbf{A}^m$ that's defined over $\K$.
Using linear triangulations defined over $\K$ we can also consider 
piecewise algebraic maps $f : X \to Y$ defined over $\K$. 

Now assume that we are given a Lie quasi crossed module with additive feedback
\[ \mbf{C}  = (G, H, \Psi, \Phi_0, \Phi_X) \]
in which $(X, x_0)$ is a pointed polyhedron defined over $\K$, 
the groups $G$ and $H$ are {\em affine unipotent} linear algebraic
groups defined over $\K$, the maps
$\Psi : G \times H \to H$ and $\Phi_0 : H \to G$ are maps of algebraic
varieties defined over $\K$, and 
\[ \Phi_X \in \mcal{O}_{\mrm{pwa}}(X(\K)) \otimes_{\K} 
\opn{Hom}_{\K}(\h(\K), \g(\K)). \]
We say that $\mbf{C} / X$ is an {\em algebraic unipotent quasi crossed
module with additive feedback defined over $\K$}. 
Note that the Lie groups in this setup are $G(\R)$ and
$H(\R)$. Also note that exponential maps $\exp_G : \g \to G$ and
$\exp_H : \h \to H$ are isomorphisms of algebraic varieties defined over $\K$
-- this is because the Lie algebras $\h$ and $\g$ are nilpotent.

The polyhedron $\mbf{I}^1$ is defined over $\mbb{Q}$. 
Suppose we are given a piecewise algebraic differential form
\[ \alpha \in \Omega^p_{\mrm{pwa}}(\mbf{I}^1(\K)) \otimes_{\K} \g(\K) . \]
It is not hard to show (using the ODE (\ref{eqn:225}), and the fact that 
$\exp_G$ is algebraic) that the map
$g : \mbf{I}^1 \to G$  of (\ref{eqn:252}) is piecewise algebraic and defined
over $\K$.  In particular we get
\[ g(1) = \opn{MI}(\alpha \vert \mbf{I}^1) \in G(\K) . \]
From this it follows that for any polyhedron $X$ defined over $\K$, any
\[ \alpha \in \Omega^1_{\mrm{alg}}(X(\K)) \otimes_{\K} \g(\K)  \]
and any piecewise algebraic string $\sigma$ in $X$ defined over $\K$, one has
\[ \opn{MI}(\alpha \vert \sigma) \in G(\K) . \]

We are led to make the following conjecture. A connection-curvature pairs
$(\alpha, \beta)$ is said to be algebraic if 
$\alpha \in \Omega^1_{\mrm{alg}}(X(\K)) \otimes_{\K} \g(\K)$ and
$\alpha \in \Omega^2_{\mrm{alg}}(X(\K)) \otimes_{\K} \h(\K)$.

\begin{conj} \label{conj:520}
Let $\mbf{C} / X$ be an algebraic unipotent quasi crossed
module with additive feedback defined over $\K$, let 
$(\alpha, \beta)$ be an algebraic connection-curvature pair in $\mbf{C} / X$, 
and let $(\sigma, \tau)$ be a piecewise algebraic kite in $(X, x_0)$.
Then 
\[ \opn{MI}(\alpha, \beta \vert \sigma, \tau) \in H(\K) \ . \]
\end{conj}

It seems that the very recent paper \cite{BGNT} may have a proof of this
conjecture in the special case when $\mbf{C} / X$ is a {\em crossed module} and 
{\em the $3$-curvature of $(\alpha, \beta)$ vanishes}. See Subsection
\ref{subsec:PDEs}.




\subsection{A Conjecture on Descent Data} \label{subsec:conj.desc}
Suppose $\f$ is a  cosimplicial nilpotent quantum type DG Lie algebra, just
like in Subsection \ref{subsec:CosDGLie}. Take an MC element 
$\til{\omega} = \{ \til{\omega}^{p, q} \}$ in the
Thom-Sullivan normalization $\til{\mrm{N}}(\f)$.
Then 
\[ \til{\omega}^{0, 0} \in \mcal{O}(\bsym{\Delta}^0) \otimes \f^{0, 1}
= \f^{0, 1} , \] 
\[ \til{\omega}^{1, 1} \in \Omega^1(\bsym{\Delta}^1) \otimes \f^{1, 0} \]
and 
\[ \til{\omega}^{2, 2} \in \Omega^2(\bsym{\Delta}^2) \otimes \f^{2, -1} . \]
Let us write 
\[ \omega := \til{\omega}^{0, 0} \in \f^{0, 1}  \]
(this notation is different from the one on Subsection \ref{subsec:CosDGLie}),
\[ g := \opn{MI}( \til{\omega}^{1, 1} \vert \bsym{\Delta}^1) \in 
\opn{exp}(\f^{1, 0}) \]
and 
\[ a :=  \opn{MI}( \til{\omega}^{2, 1} , \til{\omega}^{2, 2} 
\vert \bsym{\Delta}^2 ) \in 
\opn{exp}(\f^{2, -1})_{\til{\omega}^{2, 0}(v_0)}  . \]
This last multiplicative integral takes place in the Lie quasi crossed module
with additive feedback 
\[  \mbf{C}_{\til{\omega}^{2, 0}(v_0)}   / \bsym{\Delta}^2  =  
\bigl( G, H_{\til{\omega}^{2, 0}(v_0)}, 
\Psi, \Phi_{\til{\omega}^{2, 0}(v_0)}, \Phi_{\bsym{\Delta}^2} \bigr)  \]
as in (\ref{eqn:522}). In this way we assign to each 
$\til{\omega} \in \opn{MC}(\til{\mrm{N}}(\f))$ a triple 
\begin{equation} \label{eqn:523}
\opn{MI}(\til{\omega} \vert \bsym{\Delta}) := (\omega, g, a) .
\end{equation}

On the other hand, for every $p$ the nilpotent quantum type DG Lie algebra 
$\f^{p, \bdot}$ has its {\em Deligne $2$-groupoid} 
$\opn{Del}(\f^{p, \bdot})$, also known as the Deligne crossed groupoid; see 
\cite[Section 6]{Ye5}. The collection 
$\{ \opn{Del}(\f^{p, \bdot}) \}_{p \in \N}$ is then a cosimplicial crossed
groupoid. As explained in \cite[Section 5]{Ye3}, there is the set of
descent data 
$\opn{Desc}(\opn{Del}(\f))$, and its quotient set 
$\ol{\opn{Desc}}(\opn{Del}(\f))$.

Consider an MC element $\til{\omega} \in \opn{MC}(\til{\mrm{N}}(\f))$, 
and the triple 
$\opn{MI}(\til{\omega} \vert \bsym{\Delta}) = (\omega, g, a)$ from
(\ref{eqn:523}). The $2$-dimensional Stokes Theorem 
(Theorem \ref{thm:520}) implies that $(\omega, g, a)$ satisfies the ``failure
of $1$-cocycle'' condition of \cite[Definition 5.2]{Ye3}.
The $3$-dimensional Stokes Theorem (Theorem \ref{thm:22}) implies that 
$(\omega, g, a)$ satisfies the ``twisted $2$-cocycle'' condition of loc.\ cit.
This means that 
$(\omega, g, a) \in \opn{Desc}(\opn{Del}(\f))$.

Recall that the quotient set of $\opn{MC}(\til{\mrm{N}}(\f))$ by the action of
the gauge group $\opn{exp}(\til{\mrm{N}}(\f)^0)$ is denoted by 
$\ol{\opn{MC}}(\til{\mrm{N}}(\f))$.

\begin{conj} \label{conj:521}
Let $\f$ be a cosimplicial nilpotent quantum type DG Lie algebra. Then the
function 
\[ \opn{MI}(- \vert \bsym{\Delta}) : \opn{MC}(\til{\mrm{N}}(\f)) \to
\opn{Desc}(\opn{Del}(\f)) \]
induces a bijection 
\[ \ol{\opn{MC}}(\til{\mrm{N}}(\f)) \to \ol{\opn{Desc}}(\opn{Del}(\f)) . \]
\end{conj}





\cleardoublepage
