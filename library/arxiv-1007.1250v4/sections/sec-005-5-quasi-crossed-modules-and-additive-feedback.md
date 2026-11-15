---
doc_id: arxiv-1007.1250v4
doc_title: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES"
section_id: sec-005-5-quasi-crossed-modules-and-additive-feedback
section_title: "Quasi Crossed Modules and Additive Feedback"
section_number: 5
pages: 71-83
source_pdf: 1007.1250v4.pdf
source_sha256: 541ba4fb3068de8b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.973
doc_brief: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES — We construct a 2-dimensional twisted nonabelian multiplicative integral."
---
\label{sec:LQC}

The full strength of multiplicative integration requires a more
elaborate setup than the twisting setup of Definition \ref{dfn:5}.


\subsection{Quasi Crossed Modules}
Let $(Y, y_0)$ be a pointed analytic manifold. By {\em automorphism of pointed
analytic manifolds} we mean an analytic
diffeomorphism $f : Y \to Y$ such that $f(y_0) = y_0$.
We denote by $\opn{Aut}(Y, y_0)$ the group of all such automorphisms.

Let $G$ be a Lie group. An analytic action of $G$ on $(Y, y_0)$ by
automorphisms of pointed manifolds is an analytic map
$\Psi : G \times Y \to Y$ having the following properties.
First, for any $g \in G$ the map
$\Psi(g) : Y \to Y$, $\Psi(g)(y) := \Psi(g,y)$, is an automorphism of
pointed analytic manifolds. Second, the function
$\Psi : G \to \opn{Aut}(Y, y_0)$,
$g \mapsto \Psi(g)$, is a group homomorphism.

Given an analytic action of $G$ on $(Y, y_0)$, and an element $g \in G$,
the differential
\[ \d_{y_0} \bigl( \Psi(g) \bigr) : \mrm{T}_{y_0} Y \to \mrm{T}_{y_0} Y \]
is an $\R$-linear automorphism of the tangent space 
$\mrm{T}_{y_0} Y$. In this way we get a map of Lie groups
$G \to \mrm{GL}(\mrm{T}_{y_0} Y)$, which we call the {\em linear action
induced by $\Psi$}.

Let $H$ be a Lie group, with unit element $1$. We view it as a
pointed analytic manifold $(H, 1)$.

\begin{dfn} \label{dfn:22}
A {\em Lie quasi crossed module} \index{Lie quasi crossed module}
is the data 
\[ \mbf{C} = (G, H, \Psi, \Phi_0) \]
consisting of:
\begin{enumerate}
\item Lie groups $G$ and $H$.

\item An analytic action $\Psi$ of $G$ on $H$ by automorphisms of
pointed manifolds, called the {\em multiplicative twisting}.

\item A map of Lie groups $\Phi_0 : H \to G$, called the {\em
multiplicative feedback}.
\end{enumerate}
The condition is:
\begin{enumerate}
\rmitem{$*$} Consider $\Psi$ as a group homomorphism
$\Psi : G \to \opn{Aut}(H, 1)$. Then there is equality
\[ \Psi \circ\, \Phi_0 = \opn{Ad}_H \]
as group homomorphisms $H \to \opn{Aut}(H, 1)$.
\end{enumerate}
\end{dfn}

\begin{rem} \label{rem:1}
Let $(G, H, \Psi, \Phi_0)$ be a Lie quasi crossed module.
Suppose $G_0$ is a closed Lie subgroup of $G$ such that the following hold:
$\Phi_0(H) \subset G_0$; $\Psi(g)$ is a group automorphism of $H$ for any
$g \in G_0$; and $\Phi_0 : H \to G_0$ is $G_0$-equivariant 
(relative to $\Psi$ and $\opn{Ad}_{G_0}$). 
Then $(G_0, H, \Psi, \Phi_0)$ is called a {\em Lie crossed module}.
See \cite{BM, BS}.
In this situation condition ($*$) is called the {\em Pfeiffer condition} in
the literature. 

Note that we can always find such a subgroup $G_0$: just take
$G_0$ to be the closure of $\Phi_0(H)$ in $G$. 
An easy calculation shows that this subgroup has the required properties.
\end{rem}

Here are three of examples of Lie quasi crossed modules. 

\begin{exa} \label{exa:4}
Suppose 
\[ 1 \to N \to H \xar{\Phi_0} G \to 1 \]
is a central extension of Lie groups. Since $\opn{Ad}_H(h)$ is trivial for
$h \in N$, the action $\opn{Ad}_H$ induces an action of $G$ on $H$, which we
denote by $\Psi$. We  get a Lie crossed module $(G, H, \Psi, \Phi_0)$.
\end{exa}

\begin{exa} \label{exa:2}
A very special case of Example \ref{exa:4} is when $H = G$ and 
$\Phi_0 = \opn{id}_G$. Namely
\[ (G, H, \Psi, \Phi_0) = (G, G, \opn{Ad}_G, \opn{id}_G) . \]
This is the situation dealt with in the classical work of Schlesinger. 
\end{exa}

\begin{exa} \label{exa:5}
Let $H$ be a {\em unipotent} Lie group, namely $H$ is nilpotent and simply
connected, and let $\h := \opn{Lie}(H)$. The map $\exp_H : \h \to H$ is then an
analytic diffeomorphism. 
Take $G := \opn{GL}(\h)$. The canonical action of $G$ on $\h$ becomes, via
$\exp_H$, and action of $G$ on $H$ by automorphisms of pointed manifolds, which
we denote by $\Psi$. The adjoint action $\opn{Ad}_{\h}$ of $H$ on $\h$ 
is a map of Lie groups $\Phi_0 : H \to G$. Then 
$(G, H, \Psi, \Phi_0)$ is a Lie quasi crossed module. 

Next let $G_0 \subset G$ be the group of Lie algebra automorphisms of $\h$. 
Then $(G_0, H, \Psi, \Phi_0)$ is a Lie crossed module. 
\end{exa}




\subsection{Additive Feedback and Compatible Connections}
Let $(G, H, \Psi, \Phi_0)$ be a Lie quasi crossed module. 
We write $\g := \opn{Lie}(G)$ and $\h := \opn{Lie}(H)$.
Recall that the Lie algebra $\h$ is the tangent space to $H$ at the element
$1$. Hence the multiplicative twisting $\Psi$ induces a linear action 
\[ \Psi_{\h} : G \to \opn{GL}(\h) . \]
We see that from the Lie quasi crossed module 
$(G, H, \Psi, \Phi_0)$
we obtain a twisting setup 
$(G, H, \Psi_{\h})$. As in Section \ref{sec.MI}, we call 
$\Psi_{\h}$ the {\em additive twisting}. 

Recall that $\opn{Hom}(\h, \g)$ is the space of $\R$-linear maps
$\h \to \g$, and an element 
\[ \phi \in \mcal{O}_{\mrm{pws}}(X) \otimes \opn{Hom}_{\R}(\h, \g) \]
is called a piecewise smooth family of linear maps from $\h$ to $\g$.

\begin{dfn} \label{dfn:21}
Let $(G, H, \Psi, \Phi_0)$ be a Lie quasi crossed module, and let
$(X, x_0)$ be a pointed polyhedron. 
An {\em additive feedback  for $(G, H, \Psi, \Phi_0)$ over $(X, x_0)$}
\index{Additive feedback}
is an element
\[ \Phi_X \in \mcal{O}_{\mrm{pws}}(X) \otimes \opn{Hom}(\h, \g)  \]
satisfying this condition:
\begin{enumerate}
\rmitem{$**$} There is equality 
\[ \opn{Lie}(\Phi_0) = \Phi_X(x_0) \]
in $\opn{Hom}(\h, \g)$.
\end{enumerate}
\end{dfn}

\begin{dfn} \label{dfn:6}
Let $(X, x_0)$ be a pointed polyhedron. 
A {\em Lie quasi crossed module with additive feedback over $(X, x_0)$}
is the data 
\[  \mbf{C} / X = (G, H, \Psi, \Phi_0, \Phi_X) \]
consisting of:
\begin{itemize}
\item A Lie quasi crossed module 
$\mbf{C} = (G, H, \Psi, \Phi_0)$. 

\item An additive feedback $\Phi_X$ for $\mbf{C}$ over $(X, x_0)$.
\end{itemize}
\end{dfn}

When we talk about a Lie quasi crossed module with additive feedback 
$\mbf{C} / X$, by default we use the notation of Definitions \ref{dfn:21} and
\ref{dfn:6}, and we write
$\g := \opn{Lie}(G)$ and $\h := \opn{Lie}(H)$.

Let $\mbf{C} / X$ be a Lie quasi crossed
module with additive feedback
over $(X, x_0)$. Given a piecewise linear map
$f : (Y, y_0) \to (X, x_0)$ between pointed polyhedra, consider 
\[ f^*(\Phi_X) \in \mcal{O}_{\mrm{pws}}(Y) \otimes \opn{Hom}_{\R}(\h, \g) . \]
Then 
\begin{equation} \label{eqn:240}
f^* (\mbf{C} / X) := (G, H, \Psi, \Phi_0, f^*(\Phi_X)) 
\end{equation}
is a Lie quasi crossed module  with additive feedback
over $(Y, y_0)$.

\begin{dfn} \label{dfn:8}
Let $\mbf{C} / X$ be a Lie quasi crossed module with additive feedback over 
$(X, x_0)$. A {\em connection compatible with $\mbf{C} / X$} 
\index{Compatible connection}
is a differential form
\[ \alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g \]
satisfying the {\em holonomy condition}:
\begin{itemize}
\rmitem{$\Diamond$} Let $\sigma$ be a string in $X$, with
$x_0 = \sigma(v_0)$ and $x_1 := \sigma(v_1)$. Define
\[ g := \opn{MI}(\alpha \vert \sigma) \in G . \]
Then the diagram 
\[ \UseTips \xymatrix @C=9ex @R=5ex {
\h
\ar[d]_{\Phi_X(x_0)}
& \h
\ar[l]_{\Psi_{\h}(g)}
\ar[d]^{\Phi_X(x_1)} \\
\g
& \g
\ar[l]_{\opn{Ad}_{\g}(g)}
} \]
is commutative.
\end{itemize}
\end{dfn}

It could happen that $\mbf{C} / X$ does not admit any compatible connection. 

\begin{exa}  \label{exa:1}
Suppose $(G, H, \Psi, \Phi_0)$ is a Lie crossed module (see Remark \ref{rem:1})
and $(X, x_0)$ is a pointed polyhedron. Define 
$\Phi_X := \opn{Lie}(\Phi_0)$;
this is a $G$-equi\-variant Lie algebra map $\h \to \g$, which we view as a
constant element of 
$\mcal{O}_{\mrm{pws}}(X) \otimes \opn{Hom}(\h, \g)$.
In this way we obtain a 
Lie quasi crossed module with additive feedback 
$\mbf{C} / X := (G, H, \Psi, \Phi_0, \Phi_X)$ over $(X, x_0)$.
Since $\Phi_X$ is $G$-equivariant, it follows that any 
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$
is a connection compatible with $\mbf{C} / X$.
\end{exa}

An example of an additive feedback, and of a compatible connection, is given in
Subsection \ref{subsec:QTDGLie}.

To a Lie quasi crossed module with additive feedback $\mbf{C} / X$
there are two naturally associated twisting setups, namely
$(G, H, \Psi_{\h})$ and \lb $(G, G, \opn{Ad}_{\g})$.

\begin{prop} \label{prop:9}
Let  
\[ \mbf{C} / X = (G, H, \Psi, \Phi_0, \Phi_X) \]
be a Lie quasi crossed module with additive feedback
over $(X, x_0)$. Then:
\begin{enumerate}
\item The data $\bsym{\Theta}_X := (\opn{id}_G, \Phi_0, \Phi_X)$ is a
transfer of twisting setups
\[  (G, H, \Psi_{\h}) \to (G, G, \opn{Ad}_{\g}) \]
parametrized by $(X, x_0)$, in the sense of Definition 
\tup{\ref{dfn:7}}.

\item A form
$\alpha \in \Omega_{\mrm{pws}}^1(X) \otimes \g$
is a connection compatible with $\mbf{C} / X$ if and only if it is a 
connection compatible with $\bsym{\Theta}_X$, in the sense of 
Definition \tup{\ref{dfn:17}}.
\end{enumerate}
\end{prop}

\begin{proof}
Immediate from the definitions.
\end{proof}

\begin{prop} \label{prop:15}
Let $\mbf{C} / X$ be a Lie quasi crossed module with additive feedback over
$(X, x_0)$, and let $\alpha$ be a compatible connection for $\mbf{C} / X$. 
Suppose $f : (Y, y_0) \to (X, x_0)$ is a piecewise linear map between pointed
polyhedra. Then $f^*(\alpha)$ is a compatible connection for
$f^* (\mbf{C} / X)$.
\end{prop}

\begin{proof}
Take a string $\sigma$ in $Y$ with $\sigma(v_0) = y_0$, and let
$y_1 := \sigma(v_1)$. Then $f \circ \sigma$ is a string in $X$. According to
Proposition \ref{prop:12} we have 
\[ \opn{MI}(\alpha \vert f \circ \sigma) = 
\opn{MI}( f^*(\alpha) \vert \sigma)  . \]
Let's call this element $g$. Let $x_1 := f(y_1)$. Then 
\[ \Phi_X(x_i) = f^*(\Phi_X)(y_i) \] 
as homomorphisms $\h \to \g$, for $i = 0, 1$. 
We see that the holonomy condition is satisfied for 
$f^*(\alpha)$, relative to $f^* (\mbf{C} / X)$.
\end{proof}

\begin{dfn} \label{dfn:18}
Suppose 
\[ \mbf{C} / X = (G, H, \Psi, \Phi_0, \Phi_X) \] 
and 
\[ \mbf{C}' / X = (G', H', \Psi', \Phi_0', \Phi'_X) \]
are two Lie quasi crossed
modules with additive feedbacks over $(X, x_0)$. 
A {\em transfer} between them is a transfer of twisting setups
\[ \bsym{\Theta}_X = (\Theta_G, \Theta_H, \Theta_{\h, X}) :
(G, H, \Psi_{\h}) \to (G', H', \Psi'_{\h'})  \]
parametrized by $(X, x_0)$,
in the sense of Definition \ref{dfn:7}, satisfying this condition:
\[ \Phi'_X \circ \Theta_{\h, X} = \opn{Lie}(\Theta_G) \circ \Phi_X \]
in 
$\mcal{O}_{\mrm{pws}}(X) \otimes \opn{Hom}(\h, \g')$.
\end{dfn}





\subsection{Connection-Curvature Pairs} \label{subsec:ccpair}

\begin{dfn} \label{dfn:19}
Let $\mbf{C} / X = (G, H, \Psi, \Phi_0, \Phi_X)$ be a 
Lie quasi crossed module with additive feedback over a pointed 
polyhedron $(X, x_0)$; see Definition \ref{dfn:6}. A 
{\em connection-curvature pair} 
\index{Connection-curvature pair}
for $\mbf{C} / X$ is a pair $(\alpha, \beta)$, consisting of Lie
algebra valued differential forms
\[ \alpha \in \Omega_{\mrm{pws}}^1(X) \otimes \g \]
and
\[ \beta \in \Omega_{\mrm{pws}}^2(X) \otimes \h , \]
satisfying the conditions below.
\begin{itemize}
\rmitem{i} $\alpha$ is a connection compatible with $\mbf{C} / X$
(Definition \ref{dfn:8}).

\rmitem{ii} The equation
\[ \Phi_X(\beta) = \d (\alpha) + \smfrac{1}{2} [\alpha, \alpha] \]
holds in $\Omega_{\mrm{pws}}^2(X) \otimes \g$.
\end{itemize}
\end{dfn}

\begin{rem}
Condition (ii) above is often referred to as 
{\em vanishing of the fake curvature}. See \cite{BM, BS}.
\end{rem}

\begin{prop} \label{prop:11}
Let $\mbf{C} / X$ be a Lie quasi crossed module with additive feedback over
$(X, x_0)$, and let $(\alpha, \beta)$ be a connection-curvature pair for
$\mbf{C} / X$. 
\begin{enumerate}
\item Let $f : (Y, y_0) \to (X, x_0)$ be a piecewise linear map between pointed
polyhedra. Then $\bigl( f^*(\alpha), f^*(\beta) \bigr)$ 
is a connection-curvature pair in \lb
$f^* (\mbf{C} / X)$.

\item Let $\mbf{C}' / X$ be another Lie quasi crossed module with additive
feedback over $(X, x_0)$, and let
\[ \bsym{\Theta}_X = (\Theta_G, \Theta_H, \Theta_{\h, X}) : \mbf{C} / X 
\to \mbf{C}' / X \]
be a morphism of Lie quasi crossed module with additive
feedback. Assume that $\alpha$ is
compatible with $\Theta_{\h, X}$. See Definitions \tup{\ref{dfn:18}} and
\tup{\ref{dfn:17}}. Then 
\[ \bigl( \opn{Lie}(\Theta_G)(\alpha), \Theta_{\h, X}(\beta) \bigr) \]
is a connection-curvature pair for $\mbf{C}' / X$.
\end{enumerate}
\end{prop}

\begin{proof}
(1) By Proposition \ref{prop:15} the form $\alpha' := f^*(\alpha)$ is a
connection compatible with $f^* (\mbf{C} / X)$.
Next let us write $\beta' := f^*(\beta)$ and 
$\Phi_X' := f^*(\Phi_X)$. . Since  
\[ f^* : \Omega^1_{\mrm{pws}}(X) \otimes \g \to 
\Omega^1_{\mrm{pws}}(Y) \otimes \g \]
is a DG Lie algebra homomorphism, we have
\[ \Phi_X'(\beta') = f^*(\Phi_X(\beta)) 
= f^* \bigl( \d (\alpha) + \smfrac{1}{2} [\alpha, \alpha] \bigr) 
= \d (\alpha') + \smfrac{1}{2} [\alpha', \alpha'] . \]

\medskip \noindent
(2) The fact that $\alpha$ is compatible with $\Theta_{\h, X}$, 
and that $\bsym{\Theta}_X$ satisfies the condition ($\Diamond$) in Definition
\ref{dfn:17}, imply directly that $\alpha' := \opn{Lie}(\Theta_G)(\alpha)$ is a
connection compatible with $\mbf{C}' / X$.

Let $\beta' := \Theta_{\h, X}(\beta)$. Then
\[ \Phi'_X(\beta') = \opn{Lie}(\Theta_G)(\Phi_X(\beta)) = 
\opn{Lie}(\Theta_G) \bigl( \d (\alpha) + \smfrac{1}{2} [\alpha, \alpha] \bigr)
= \d (\alpha') + \smfrac{1}{2} [\alpha', \alpha'] . \]
We see that condition (ii) of Definition \ref{dfn:19} holds.
\end{proof}

\begin{dfn}[Tame Connection] \label{dfn:46}
Let $\mbf{C} / X$ be a Lie quasi crossed module with additive feedback over
$(X, x_0)$. A form
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$
is called a {\em tame connection} \index{Tame connection}
for $\mbf{C} / X$ if there exists a form
$\beta \in \Omega^2_{\mrm{pws}}(X) \otimes \h$ 
such that $(\alpha, \beta)$ is a connection-curvature pair 
(as in Definition \ref{dfn:19}). 
\end{dfn}

In other words, $\alpha$ is a tame connection if it is a compatible connection
(Definition \ref{dfn:8}), and its curvature
$\d (\alpha) + \smfrac{1}{2} [\alpha, \alpha]$
comes from $\Omega^2_{\mrm{pws}}(X) \otimes \h$.

\begin{cor} \label{cor:8}
In the situation of Proposition \tup{\ref{prop:11}}, the forms 
$f^*(\alpha)$ and $\opn{Lie}(\Theta_G)(\alpha)$ are tame connections.
\end{cor}

The proof is trivial. 






\subsection{Moving the Base Point}
\label{subsec:moving}
In this subsection we consider the following setup: 
\[ \mbf{C} / X = (G, H, \Psi, \Phi_0, \Phi_X) \]
is a Lie quasi crossed module with additive feedback over a pointed 
polyhedron $(X, x_0)$. We are given a form
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$, which is a connection
compatible with $\mbf{C} / X$. And we are given a string $\rho$ in $X$, with
initial point $\rho(v_0) = x_0$ and terminal point $x_1 := \rho(v_1)$.
Let 
\[ g := \opn{MI}(\alpha \vert \rho) \in G . \]

Recall that $\Psi(g)$ is an automorphism of the pointed analytic manifold
$(H, 1)$. We define a new multiplication on the manifold $H$, by the formula
\[ h_1 \cdot^g h_2 := \Psi(g)^{-1} \bigl( \Psi(g)(h_1) \cdot 
\Psi(g)(h_2) \bigr) \]
for $h_1, h_2 \in H$. In this way we obtain a new Lie group, that is denoted by
$H^g$, and a Lie group isomorphism
\[ \Psi(g) : H^g \to H . \]
See Figure \ref{fig:70}.

\begin{figure} 
\includegraphics[scale=0.18]{fig70.jpg}
\caption{The string $\rho$ from $x_0$ to $x_1$, the group element
$g := \opn{MI}(\alpha \vert \rho) \in G$, and the group isomorphism
$\Psi(g) : H^g \to H$.} 
\label{fig:70}
\end{figure}

The Lie algebra of $H^g$ is $\h^g$. So 
$\h^g = \h$ as vector spaces (this is the tangent space to $H$ at $1$), and 
\[ \Psi_{\h}(g) : \h^g \to \h \]
is a Lie algebra isomorphism. There is a commutative diagram of maps
\begin{equation} \label{eqn:133}
\UseTips \xymatrix @C=7ex @R=5ex {
\h
\ar[d]_{\exp_H}
& \h^g
\ar[l]_{\Psi_{\h}(g)}
\ar[d]^{\exp_{H^g}} \\
H
& H^g
\ar[l]_{\Psi(g)}
} 
\end{equation}
Note that if $\Psi(g)$ is not a group automorphism of $H$, then $H^g$ is not
equal to $H$ as groups. In this case the maps of manifolds
\[ \exp_H, \exp_{H^g} : \h \to H \]
could be distinct. 

The data $(G, H^g, \Psi_{\h})$ is a twisting setup (as in Definition
\ref{dfn:5}), which in general is distinct from the twisting setup
$(G, H, \Psi_{\h})$, because of the possibly distinct exponential maps. Given
a form $\beta \in \Omega^2_{\mrm{pws}}(X) \otimes \h$ and a kite
$(\sigma, \tau)$ in  $(X, x_1)$, let us denote by 
\begin{equation} \label{eqn:123}
\opn{MI}^g(\alpha, \beta \vert \sigma, \tau) \in H^g
\end{equation}
the multiplicative integral with respect to the twisting setup
$(G, H^g, \Psi_{\h})$. 

We define a map of Lie groups
$\Phi_0^g : H^g \to G$ by the commutative diagram
\[ \UseTips \xymatrix @C=7ex @R=5ex {
H
\ar[d]_{\Phi_0}
& H^g
\ar[l]_{\Psi(g)}
\ar[d]^{\Phi_0^g} \\
G
& G 
\ar[l]_{\opn{Ad}_G(g)}
} \]

\begin{prop}
The data
\[ \mbf{C}^g := (G, H^g, \Psi, \Phi_0^g) \]
is a Lie quasi crossed module.
\end{prop}

\begin{proof}
Let's write
$H' := H^g$, $G' := G$, $u := \opn{Ad}_G(g) : G' \to G$,
$v := \Psi(g) : H' \to H$,
$\Psi' := \Psi$ and $\Phi_0' := \Phi_0^g$. 
There are commutative diagrams of group homomorphisms
\begin{equation} \label{eqn:120}
\UseTips \xymatrix @C=7ex @R=5ex {
H
\ar[d]_{\Phi_0}
& H'
\ar[l]_{v}
\ar[d]^{\Phi_0'} \\
G
& G'
\ar[l]_{u}
} 
\qquad 
\UseTips \xymatrix @C=7ex @R=5ex {
G
\ar[d]_{\Psi}
& G'
\ar[l]_{u}
\ar[d]^{\Psi'} \\
\opn{Aut}(H)
& \opn{Aut}(H') 
\ar[l]_(0.5){\opn{Ad}(v)}
}
\end{equation}
Here $\opn{Aut}(H) = \opn{Aut}(H')$ is the group of automorphisms of the pointed
manifold $H = H'$, and $v$ is seen as an element of this group. 
The first diagram is just the definition of $\Phi_0'$.
The second diagram is commutative since for every $g' \in G'$ we have 
\[ \begin{aligned}
& \Psi(u(g')) = \Psi(g \cdot g' \cdot g^{-1}) = 
\Psi(g) \cdot \Psi(g') \cdot \Psi(g^{-1}) \\
& \qquad = v \cdot \Psi(g') \cdot v^{-1} = 
(\opn{Ad}(v) \circ \Psi')(g') . 
\end{aligned} \]
And by general group theory we have a commutative diagram
\begin{equation} \label{eqn:122}
\UseTips \xymatrix @C=7ex @R=5ex {
H
\ar[d]_{\opn{Ad}_{H}}
& H'
\ar[l]_{v}
\ar[d]^{\opn{Ad}_{H'}} 
\\
\opn{Aut}(H)
& \opn{Aut}(H')
\ar[l]^(0.5){\opn{Ad}(v)}
}
\end{equation}

We are given that  
$\Psi \circ \Phi_0 = \opn{Ad}_H$ 
(this is condition ($*$) of Definition \ref{dfn:22} for the Lie quasi crossed
module $\mbf{C}$). Therefore by combining the three commutative diagrams we
see that
$\Psi' \circ \Phi'_0 = \opn{Ad}_{H'}$ 
\end{proof}

\begin{prop}
The element $\Phi_X$ is an additive feedback for the Lie quasi crossed module
$\mbf{C}^g$ over the pointed polyhedron $(X, x_1)$. Thus
\[ \mbf{C}^g / X := (G, H^g, \Psi, \Phi_0^g, \Phi_X) \]
is a Lie quasi crossed module with additive feedback over 
$(X, x_1)$.
\end{prop}

\begin{proof}
In the notation used in the proof of the previous proposition, and
with $\Phi'_X := \Phi_X$, we have to show that
$\Phi'_X(x_1) = \opn{Lie}(\Phi'_0)$, as linear maps
$\h' \to \g'$. 
We have commutative diagrams of linear maps
\[ \UseTips \xymatrix @C=7ex @R=5ex {
\h
\ar[d]_{\opn{Lie}(\Phi_0)}
& \h'
\ar[l]_{\opn{Lie}(v)}
\ar[d]^{\opn{Lie}(\Phi_0')} \\
\g
& \g' 
\ar[l]_{\opn{Lie}(u)}
} 
\qquad 
\UseTips \xymatrix @C=8ex @R=5ex {
\h
\ar[d]_{\Phi_X(x_0)}
& \h
\ar[l]_{\Psi_{\h}(g)}
\ar[d]^{\Phi_X(x_1)} \\
\g
& \g
\ar[l]_(0.5){\opn{Ad}_{\g}(g)}
} \]
The first diagram is the differential of the first diagram in (\ref{eqn:120}),
and the second diagram is the holonomy condition for $\alpha$ relative to 
$\mbf{C} / X$. Since $\Phi_X$ is an additive feedback for $\mbf{C}$
over $(X, x_0)$ we have
$\Phi_X(x_0) = \opn{Lie}(\Phi_0)$.
We know that
$\Psi_{\h}(g) = \opn{Lie}(v)$ and
$\opn{Ad}_{\g}(g) = \opn{Lie}(u)$.
It follows that
$\Phi'_X(x_1) = \Phi_X(x_1) = \opn{Lie}(\Phi'_0)$.
\end{proof}

\begin{prop}
The form $\alpha$ is a connection compatible with $\mbf{C}^g / X$.
\end{prop}

\begin{proof}
We continue with the notation of the previous proofs. 
Let $\sigma$ be a string in $X$ initial point $\sigma(v_0) = x_1$ and terminal
point $x_2 := \sigma(v_1)$. Define
$g' := \opn{MI}(\alpha \vert \sigma) \in G' = G$. 
Because $\alpha$ is a connection compatible with $\mbf{C} / X$, and 
because
$g \cdot g' = \opn{MI}(\alpha \vert \rho * \sigma)$,
we have a commutative diagram
\[ \UseTips \xymatrix @C=10ex @R=6ex {
\h
\ar[r]^{\Psi_{\h}(g)}
\ar[d]_{\Phi_X(x_1)}
& \h
\ar[d]^{\Phi_X(x_0)} 
&
\h
\ar[d]^{\Phi_X(x_2)} 
\ar[l]_{\Psi_{\h}(g \cdot g')}
\\
\g
\ar[r]_(0.5){\opn{Ad}_{\g}(g)}
& \g
& \g
\ar[l]^(0.5){\opn{Ad}_{\g}(g \cdot g')}
} \]
Since
\[ \Psi_{\h}(g)^{-1} \circ \Psi_{\h}(g \cdot g') = \Psi_{\h}(g') \]
and
\[ \opn{Ad}_{\g}(g)^{-1} \circ \opn{Ad}_{\g}(g \cdot g') = 
\opn{Ad}_{\g}(g') \]
we see that the diagram 
\[ \UseTips \xymatrix @C=8ex @R=5ex {
\h'
\ar[d]_{\Phi'_X(x_1)}
& \h'
\ar[l]_{\Psi'_{\h'}(g')}
\ar[d]^{\Phi'_X(x_2)} \\
\g'
& \g'
\ar[l]_(0.5){\opn{Ad}_{\g'}(g')}
} \]
is commutative.
\end{proof}

\begin{thm} \label{thm:14}
Let 
\[ \mbf{C} / X = (G, H, \Psi, \Phi_0, \Phi_X) \]
be a Lie quasi crossed module with additive feedback over a pointed 
polyhedron $(X, x_0)$, let 
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$
be a connection compatible with $\mbf{C} / X$, and let
$\rho$ be a string in $X$, with initial point $\rho(v_0) = x_0$.
Define
$g := \opn{MI}(\alpha \vert \rho)$, 
and let
\[ \mbf{C}^g / X = (G, H^g, \Psi, \Phi_0^g, \Phi_X) \]
be the Lie quasi crossed module with additive feedback over $(X, x_1)$
constructed above. 

Given a form 
$\beta \in \Omega^2_{\mrm{pws}}(X) \otimes \h$ and a kite
$(\sigma, \tau)$ in  $(X, x_1)$, consider the element
\[ \opn{MI}^g(\alpha, \beta \vert \sigma, \tau) \in H^g  \]
from \tup{(\ref{eqn:123})}. Then 
\[ \Psi(g) \bigl( \opn{MI}^g(\alpha, \beta \vert \sigma, \tau) \bigr)  =
\opn{MI}(\alpha, \beta \vert \rho * \sigma, \tau)  \]
in $H$. 
\end{thm}

See Figure \ref{fig:71}.

\begin{figure} 
\includegraphics[scale=0.18]{fig71.jpg}
\caption{The string $\rho$ from $x_0$ to $x_1$, and the kite
$(\sigma, \tau)$ in $(X, x_1)$.} 
\label{fig:71}
\end{figure}

\begin{proof}
We can assume that the kite $(\sigma, \tau)$ is nondegenerate. Define
$Z := \tau(\mbf{I}^2)$ and $g' := \opn{MI}^g(\alpha \vert \sigma)$.
Choose a positively oriented orthonormal linear coordinate system 
$(s_1, s_2)$ on $Z$.

Take $k \geq 0$ and $i \in \{ 1, \ldots, 4^k \}$, and 
define
$z_i := (\tau \circ \tau^k_i)(\smfrac{1}{2}, \smfrac{1}{2}) \in Z$
and
\[ g'_i := \opn{MI} \bigl( (\alpha \vert (\tau \circ \sigma^k_i) * 
(\tau \circ \tau^k_i \circ \sigma_{\opn{pr}}) \bigr) . \]
So
\[ \opn{MI} \bigl( \alpha \vert
\rho * \sigma * (\tau \circ \sigma^k_i) * 
(\tau \circ \tau^k_i \circ \sigma_{\opn{pr}})  \bigr) = 
g \cdot g' \cdot g'_i . \]

Assume that $z_i$ is a smooth point of $\beta|_Z$. Let $Y_i$ be a triangle
in $Z$, and let $\til{\beta}_i \in \mcal{O}(Y_i) \otimes \h$, such that
$z \in \opn{Int} Y_i$ and 
$\beta|_{Y_i} = \til{\beta}_i \cdot \d s_1 \wedge \d s_2$. According to 
Definition \ref{dfn:11}  and the commutative diagram (\ref{eqn:133}) we have
\[ \begin{aligned}
& \opn{RP_0} \bigl( \alpha, \beta \vert (\rho * \sigma, \tau) \circ 
(\sigma^k_i, \tau^k_i) \bigr) \\
& \qquad = 
\exp_H \bigl( (\smfrac{1}{4})^k \cdot \opn{area}(Z) \cdot 
\Psi_{\h}(g \cdot g' \cdot g'_i) (\til{\beta}_i(z_i)) \bigr) \\
& \qquad =
(\Psi(g) \circ \exp_{H^g}) \bigl( (\smfrac{1}{4})^k \cdot \opn{area}(Z) \cdot 
\Psi_{\h}(g' \cdot g'_i) (\til{\beta}_i(z_i)) \bigr) \\
& \qquad =
\Psi(g) \bigl( \opn{RP}_0^g \bigl( \alpha, \beta \vert 
(\sigma, \tau) \circ (\sigma^k_i, \tau^k_i) \bigr) \bigr) .
\end{aligned} \]

On the other hand, if $z_i$ is a singular point of $\beta|_Z$ then 
\[ \opn{RP}_0 \bigl( \alpha, \beta \vert (\rho * \sigma, \tau) \circ 
(\sigma^k_i, \tau^k_i) \bigr) = 1 =
\Psi(g) \bigl( \opn{RP}_0^g \bigl( \alpha, \beta \vert 
(\sigma, \tau) \circ (\sigma^k_i, \tau^k_i) \bigr) \bigr) . \]

We see that
\[ \opn{RP}_k (\alpha, \beta \vert \rho * \sigma, \tau) =
\Psi(g) \bigl( \opn{RP}_k^g ( \alpha, \beta \vert \sigma, \tau) \bigr) \]
for every $k$.
Passing to the limit $k \to  \infty$ finishes the proof.
\end{proof}


\subsection{Partial Differential Equations} \label{subsec:PDEs}
Let $\alpha \in \Omega^1(\mbf{I}^1) \otimes \g$. 
For $x \in \mbf{I}^1$ let $\sigma_x : \mbf{I}^1 \to \mbf{I}^1$
be the linear map defined on vertices by 
$\sigma_x(v_0, v_1) := (v_0, x)$.
Let
\begin{equation} \label{eqn:252}
g(x) := \opn{MI}(\alpha \vert \sigma_x) \in G .
\end{equation}
It is well known  that the function 
$g : \mbf{I}^1 \to G$ defined in this way is smooth, and moreover it satisfies
the differential equation
\begin{equation} \label{eqn:225}
\opn{dlog}(g) = \alpha
\end{equation}
with initial condition $g(0) = 1$.
See \cite{DF} for the case $G = \opn{GL}_n(\R)$, in which 
\[ \opn{dlog}(g) = g^{-1} \cdot \d g \]
as matrices. This ODE determines the function $g$. 

Now consider a Lie quasi-crossed module $\mbf{C}$, and a smooth
connection-cur\-vature
pair $(\alpha, \beta)$ in $\mbf{C} / \mbf{I}^2$. 
For a point $x \in \mbf{I}^2$ let 
$\tau_{x} : \mbf{I}^2 \to \mbf{I}^2$ be the linear map
defined on vertices by 
\[ \tau_x(v_0, v_1, v_1) := \bigl( v_0, (t_1(x), 0), (0, t_2(x)) \bigr) . \]
And let $\sigma$ be the empty string, so that 
$(\sigma, \tau_x)$ is a kite in $(\mbf{I}^2, v_0)$. Define
\[ h(x) := \opn{MI}(\alpha, \beta \vert \sigma, \tau_x) \in H . \]
Presumably the function 
$h : \mbf{I}^2 \to H$
is smooth, and it satisfies a partial differential equation generalizing 
(\ref{eqn:225}). We did not check this assertion.

In the very recent paper \cite{BGNT} the authors consider a special case:
the groups $G$ and $H$ are unipotent, $\mbf{C}$ is a crossed module, and the
pair $(\alpha, \beta)$ is algebraic. They write down a partial
differential equation, whose unique solution is declared to be the
multiplicative integral. Presumably this multiplicative integral coincides with
ours. For more in this direction see Subsection \ref{subsec:ration}.



\subsection{Quantum Type DG Lie Algebras} \label{subsec:QTDGLie}
Here we explain how Lie quasi crossed modules arise
from deformation theory. This is continued in the following subsection.

A {\em differential graded} (DG) Lie algebra is a graded $\R$-module
$\f = \boplus_{i \in \Z} \f^i$ \lb
equipped with a graded Lie bracket $[-,-]$ and a differential $\d$ (of degree
$1$) that satisfy the graded Leibniz rule. 
For instance, if $X$ is a manifold and $\g$ is a Lie algebra, then 
$\f := \Omega(X) \otimes \g$ is a DG Lie algebra. 
We say that $\f$ is a {\em quantum type} DG Lie algebra if
$\f^i = 0$ for all $i < -1$; i.e.\
$\f = \boplus_{i \geq -1} \f^i$.

Let us fix a quantum type DG Lie algebra $\f$, and assume that $\f$ is
nilpotent, and finite dimensional in each degree. 
(The assumptions of finiteness and nilpotence are for the sake of presentation;
the construction works even when $\f$ is infinite
dimensional  and pronilpotent.)

The Lie bracket $[-,-]$ of $\f$ makes the vector space $\g := \f^0$ into a
nilpotent Lie algebra. We denote by $G = \exp(\g)$ the corresponding unipotent
group. In order to be concrete, we take $G$ to be the analytic manifold $\g$, 
made into a Lie group by the CBH formula (cf.\ Section \ref{sec:expon}); in
particular $1_G := 0_{\g}$. The exponential map $\exp_G : \g \to G$ is just the
identity map here.

The Lie algebra $\g$ acts on the vector space $\f^i$ (any $i$) by the adjoint
action $\opn{ad}$, namely
\[ \opn{ad}(\alpha)(\beta) := [\alpha, \beta] \]
for $\alpha \in \g$ and $\beta \in \f^i$. Clearly $\opn{ad}(\alpha)$ is
$\R$-linear. 
There is a second action of $\g$ on $\f^1$, which we call the {\em affine
action}, and it is
\[ \opn{af}(\alpha)(\beta) := \d(\alpha) - [\alpha, \beta] \]
for $\beta \in \f^1$. The action $\opn{af}$ is usually not linear -- it is an
action by affine transformations. Both these actions integrate (or rather
exponentiate) to actions $\opn{Ad}$ and $\opn{Af}$ of the group $G$ on the
vector spaces $\f^i$ and $\f^1$ respectively. 

An element $\omega \in \f^1$ is called an {\em MC element} if it satisfies the
Maurer-Cartan equation
\[ \d(\omega)+ \smfrac{1}{2}[\omega, \omega] = 0 . \]
We denote by $\opn{MC}(\f)$ the set of all MC elements. 
It turns out that the action $\opn{Af}$ of $G$ on $\f^1$ preserves the subset 
$\opn{MC}(\f)$. Namely if $\omega \in \opn{MC}(\f)$ and $g \in G$, then 
$\omega' := \opn{Af}(g)(\omega)$ is also in $\opn{MC}(\f)$.
The quotient set by this action is denoted by $\ol{\opn{MC}}(\f)$.

Let us write $\h := \f^{-1}$. 
Say an MC element $\omega$ is given. Define an $\R$-linear map
$\d_{\omega} : \h \to \g$ by the formula
\begin{equation} \label{eqn:134}
\d_{\omega}(\beta) := \d(\beta) + [\omega, \beta]
\end{equation}
for $\beta \in \h$. And define an $\R$-bilinear operation 
$[-,-]_{\omega}$ on $\h$ by the formula
\begin{equation} \label{eqn:124}
[\beta_1, \beta_2]_{\omega} := [\d_{\omega}(\beta_1), \beta_2] . 
\end{equation}
An elementary calculation shows that the vector space $\h$ 
is a nilpotent Lie algebra with
respect to the bracket $[-,-]_{\omega}$, and we denote this Lie algebra by
$\h_{\omega}$. A similar calculation shows that 
$\d_{\omega} : \h_{\omega} \to \g$ is a Lie algebra map. 
Let us define
$H_{\omega} := \exp(\h_{\omega})$, the corresponding unipotent group, with
multiplication 
$h_1 \cdot_{\omega} h_2$ and inverse
$h_1^{-1_{\omega}}$, for $h_i \in H_{\omega}$.
So as analytic manifolds we have 
$H_{\omega} = \h_{\omega} = \h$, and 
$\exp_{H_{\omega}} : \h_{\omega} \to H_{\omega}$ is the identity map. 
There is a Lie group map
$\exp(\d_{\omega}) : H_{\omega} \to G$. 
It is easy to see from (\ref{eqn:124}) that for elements $h_1, h_2 \in
H_{\omega}$ one has
\[ \opn{Ad} \bigl( \exp(\d_{\omega})(h_1) \bigr)(h_2) = 
\opn{Ad}_{H_{\omega}}(h_1)(h_2) = 
h_1 \cdot_{\omega} h_2 \cdot_{\omega} h_1^{-1_{\omega}} .  \]

Suppose we are  given
$\omega \in \opn{MC}(\f)$ and $g \in G$. Define 
$\omega' := \opn{Af}(g)(\omega)$. A more difficult calculation shows that 
there is a commutative diagram of Lie algebra maps
\[ \UseTips \xymatrix @C=7ex @R=5ex {
\h_{\omega}
\ar[d]_{\d_{\omega}}
\ar[r]^{\opn{Ad}(g)}
& \h_{\omega'}
\ar[d]^{\d_{\omega'}}
\\
\g
\ar[r]^{\opn{Ad}(g)}
& \g
}  \]
See \cite[Section 1]{Ye5}. 
Hence there is also a commutative diagram of Lie group maps
\[ \UseTips \xymatrix @C=10ex @R=6ex {
H_{\omega}
\ar[d]_{\exp(\d_{\omega})}
\ar[r]^{\exp(\opn{Ad}(g))}
& H_{\omega'}
\ar[d]^{\exp(\d_{\omega'})}
\\
G
\ar[r]^{\exp(\opn{Ad}(g))}
& G
} \]
Observe that if 
$[-,-]_{\omega} \neq [-,-]_{\omega'}$ as Lie brackets, then 
$\h_{\omega} \neq \h_{\omega'}$ as Lie algebras, 
$H_{\omega} \neq H_{\omega'}$ as Lie groups, and
$\Psi(g) := \exp(\opn{Ad}(g))$ is not a Lie group automorphism of $H_{\omega}$;
it is only an automorphism of pointed analytic manifolds. 
At least we obtain in this way an action $\Psi$ of $G$ on $H_{\omega}$ by
automorphisms of pointed analytic manifolds. 

Take an MC element $\omega$, and define the map of Lie groups
\[ \Phi_{\omega} := \exp(\d_{\omega}) : H_{\omega} \to G . \]
What we have said so far implies that the data
\begin{equation} \label{eqn:125}
\mbf{C}_{\omega} := \bigl( G, H_{\omega}, \Psi, \Phi_{\omega} \bigr)
\end{equation}
is a Lie quasi crossed module. 


\subsection{Cosimplicial DG Lie Algebras} \label{subsec:CosDGLie}
Here we show how deformation quantization gives rise to Lie quasi \lb crossed
modules with additive feedback and con\-nection-curvature pairs. 

Suppose we are given a {\em cosimplicial nilpotent 
quantum type DG Lie algebra} $\f$. So 
$\f = \{ \f^{p, \bdot} \}_{p \in \N}$,
where each $\f^{p, \bdot} = \boplus_{i \geq -1} \f^{p,i}$
is a nilpotent quantum type DG Lie algebra.

{}From the cosimplicial object $\f$ one constructs its
Thom-Sullivan normalization $\til{\mrm{N}}(\f)$, which is a nilpotent 
quantum type DG Lie algebra, involving algebraic differential forms on all the
simplices $\bsym{\Delta}^p$, $p \geq 0$. For details see \cite[Section 2]{Ye2}.

Suppose $\til{\omega}$ is an MC element of
$\til{\mrm{N}}(\f)$. By definition 
$\til{\omega} = \{ \til{\omega}^{p, q} \}$, where
\[ \til{\omega}^{p, q} \in \Omega^q(\bsym{\Delta}^p) 
\otimes \f^{p, 1 - q} , \quad p \in \N,\ q \in \{ 0, 1, 2 \} .  \]
Let us fix a number $p$. We look at the components of $\til{\omega}$ with index
$p$:
\[ \omega := \til{\omega}^{p, 0} \in 
\mcal{O}(\bsym{\Delta}^p) \otimes \f^{p, 1} , \]
\[ \alpha := \til{\omega}^{p, 1} \in 
\Omega^1(\bsym{\Delta}^p) \otimes \f^{p, 0}  \]
and
\[ \beta := \til{\omega}^{p, 2} \in 
\Omega^2(\bsym{\Delta}^p) \otimes \f^{p, -1} . \]

Now let us write
$\g := \f^{p, 0}$, $\h := \f^{p, -1}$ and $X := \bsym{\Delta}^p$.
With this notation 
$\omega \in \mcal{O}(X) \otimes \f^{p, 1}$,
$\alpha \in \Omega^1(X) \otimes \g$
and
$\beta \in \Omega^2(X) \otimes \h$.

Choose some point $x_0 \in X$. The element 
$\omega(x_0) \in \f^{p, 1}$ turns out to be an MC element of the DG
Lie algebra $\f^{p, \bdot}$.
As in (\ref{eqn:125}), we have a Lie quasi crossed module 
\[  \mbf{C}_{\omega(x_0)}  =  
\bigl( G, H_{\omega(x_0)}, \Psi, \Phi_{\omega(x_0)} \bigr)  . \]
Next we define
\[ \Phi_{X} := \d_{\omega} \in 
\mcal{O}(X) \otimes \opn{Hom}(\h, \g) ; \]
see (\ref{eqn:134}). This is an additive feedback for $\mbf{C}_{\omega(x_0)}$
over the pointed polyhedron $(X, x_0)$, so we obtain a 
Lie quasi crossed module with additive feedback
\begin{equation} \label{eqn:522}
 \mbf{C}_{\omega(x_0)} / X  =  
\bigl( G, H_{\omega(x_0)}, \Psi, \Phi_{\omega(x_0)}, \Phi_{X} \bigr)  .
\end{equation}
Furthermore, it can be shown that the pair $(\alpha, \beta)$ is a
connection-curvature pair in 
$\mbf{C}_{\omega(x_0)} / X$. 
Taking any kite $(\sigma, \tau)$ in $(X, x_0)$ we thus obtain a group element 
\[ \opn{MI}(\alpha, \beta \vert \sigma, \tau) \in 
H_{\omega(x_0)} . \]

In Subsection \ref{subsec:conj.desc} we continue with this setup, and state
Conjecture \ref{conj:521}.






\cleardoublepage
