---
doc_id: arxiv-1007.1250v4
doc_title: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 3-13
source_pdf: 1007.1250v4.pdf
source_sha256: 541ba4fb3068de8b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.99
doc_brief: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES — We construct a 2-dimensional twisted nonabelian multiplicative integral."
---
\numberwithin{equation}{subsection}



\subsection{}
In this paper we establish a theory of {\em twisted nonabelian multiplicative
integration of $2$-forms on surfaces}. 

Let us begin the exposition with a discussion of 
{\em $1$-dimensional nonabelian multiplicative integration}. 
This goes back to work of Volterra in the 19-th
century, and is also known by the names ``path ordered exponential integration''
and ``holonomy of a connection along a path''. See the book \cite{DF} and
the paper \cite{KMR} for history and various properties. 

In our setup the $1$-dimensional multiplicative integral looks like this. 
Let $X$ be an $n$-dimensional manifold (by which we mean a differentiable
manifold with corners), and let $G$ be a Lie group with Lie algebra $\g$, 
all over the field  $\R$. We denote by
\[ \Omega(X) = \boplus_{p = 0}^n \ \Omega^p(X) \]
the de Rham algebra of $X$ (i.e.\ the algebra of smooth differential forms).
By smooth path in $X$ we mean a smooth map 
$\sigma: \bsym{\Delta}^1 \to X$, where $\bsym{\Delta}^1$ is the $1$-dimensional
simplex. Let
\[ \alpha \in  \Omega^1(X) \otimes \g . \]
The {\em multiplicative integral of $\alpha$ on $\sigma$} is an element
\begin{equation} \label{eqn:163}
\opn{MI}(\alpha \vert \sigma) \in G , 
\end{equation}
obtained as the limit of {\em Riemann products}.
This operation is re-worked and extended in Section \ref{sec:dim1} of our
paper.


\subsection{}
For reasons explained in Subsection \ref{subsec:motiv} of the Introduction, we
found it necessary to devise a theory of {\em $2$-dimensional nonabelian
multiplicative integration}. Our work was guided by the problem at
hand, plus ideas borrowed from the papers \cite{BM, BS, Ko}. 

Instead of a single Lie group, the $2$-dimensional operation involves a pair
$(G, H)$ of Lie groups, with a certain interaction between them. 
This structure is called a {\em Lie crossed module}.
A Lie crossed module
\begin{equation} \label{eqn:230}
\mbf{C} = (G, H, \Psi, \Phi)
\end{equation}
consists, in addition to the Lie groups $H$ and $G$, of an analytic action
$\Psi$ of $G$ on $H$ by automorphisms of Lie groups,
which we call the {\em twisting}; and of a map of Lie groups
$\Phi : H \to G$, called the {\em feedback}. The conditions are that $\Phi$ is
$G$-equivariant (with respect to $\Psi$ and to the conjugation action
$\opn{Ad}_G$ of $G$ on itself); and 
\begin{equation} \label{eqn:165}
\Psi \circ \Phi = \opn{Ad}_H .
\end{equation} 
See  \cite{BM, BS}.
The integrand is now a pair $(\alpha, \beta)$, with 
\begin{equation} \label{eqn:162}
\alpha \in \Omega^1(X) \otimes \g \ \text{ and } \
\beta \in  \Omega^2(X) \otimes \h . 
\end{equation}
Here $\h$ is the Lie algebra of $H$.

Let $x_0$ be a point in $X$, so the pair $(X, x_0)$ is a pointed manifold.
The geometric data (the cycle) for the multiplicative integration is a {\em
kite} $(\sigma, \tau)$ in $(X, x_0)$. 
Let us denote by $v_0, \ldots, v_p$ the vertices of the 
$p$-dimensional simplex $\bsym{\Delta}^p$. By definition a {\em smooth
triangular kite} $(\sigma, \tau)$ in $(X, x_0)$ consists of smooth maps
$\sigma : \bsym{\Delta}^1 \to X$ and
$\tau : \bsym{\Delta}^2 \to X$, such that
$\sigma(v_0) = x_0$ and
$\sigma(v_1) = \tau(v_0)$. 
See Figure \ref{fig:80} for an illustration.

\begin{figure} 
\includegraphics[scale=0.27]{fig80.jpg}
\caption{A smooth triangular kite $(\sigma, \tau)$ in the pointed manifold 
$(X, x_0)$.} 
\label{fig:80}
\end{figure}

The next theorem summarizes our construction. It encapsulates many results
scattered throughout the paper.

\begin{thm}[Existence of MI on Triangles] \label{thm:18}
Let 
$\mbf{C} = (G, H, \Psi, \Phi)$
be a Lie crossed module, $(X, x_0)$ a pointed manifold, and
$(\alpha, \beta)$ a pair of differential forms as in \tup{(\ref{eqn:162})}.
Given any smooth triangular kite
$(\sigma, \tau)$ in $(X, x_0)$, there is an element
\[ \opn{MI} (\alpha, \beta \vert \sigma, \tau) \in H  \]
called the {\em twisted multiplicative integral of $(\alpha, \beta)$ on 
$(\sigma, \tau)$}.

The operation $\opn{MI}(-,-)$ enjoys these properties:
\begin{enumerate}
\rmitem{a} The element 
$\opn{MI} (\alpha, \beta \vert \sigma, \tau)$
has an explicit formula as the limit of Riemann products.

\rmitem{b} The operation $\opn{MI}(-,-)$ is functorial in 
$\mbf{C}$ and $(X, x_0)$.

\rmitem{c} If $H$ is abelian and $G$ is trivial, then 
\[ \opn{MI} (\alpha, \beta \vert \sigma, \tau) = 
\opn{exp}_H  \bigl( \int_{\tau} \beta \bigr) . \]
\end{enumerate}
\end{thm}

More on the construction in Subsections 
\ref{subsec:methods}-\ref{subsec:binary} and \ref{subsec:triangles} of the
Introduction.

As far as we know, this is the first construction of a nonabelian
multiplicative integration on surfaces of such generality. 
The very special case $G = H = \opn{GL}_m(\R)$ was done by Schlesinger in the
1920's; cf.\ \cite{DF, KMR}. 


\subsection{} \label{subsec:actually}
Actually, in the body of the paper we work in a much more complicated situation.
Instead of a Lie crossed module (\ref{eqn:230}), we work with a {\em Lie
quasi crossed module with additive feedback} (See Section \ref{sec:LQC}). 
The reason for the more complicated setup is that this is what was 
required, at the time, for our work on {\em twisted deformation quantization}
in the paper \cite{Ye3}. More on this in Subsection \ref{subsec:motiv} below.
In the Introduction we stick to the simpler
setup of a Lie crossed module, which is interesting enough. Note
however that all the results mentioned in the Introduction are valid also in the
more complicated setup.


\subsection{}
In this subsection we explain the nonabelian $2$-dimensional Stokes Theorem.
For this to hold it is necessary to
impose a condition on the integrand $(\alpha, \beta)$. 
Recall the feedback $\Phi : H \to G$. Consider the induced Lie algebra
homomorphism
\[ \opn{Lie}(\Phi) : \h \to \g . \]
By tensoring this induces a homomorphism of differential graded Lie algebras
\[ \phi : \Omega(X) \otimes \h \to \Omega(X) \otimes \g . \]
We say that $(\alpha, \beta)$ is a {\em connection-curvature pair}
for $\mbf{C} / X$ if
\begin{equation}  \label{eqn:164}
\phi(\beta) = \d(\alpha) + \smfrac{1}{2} [\alpha, \alpha]   
\end{equation}
in $\Omega^2(X) \otimes \g$.
(In \cite{BM} this condition is called the {\em vanishing of the fake
curvature}.) 

The boundary of a triangular kite $(\sigma, \tau)$ is the closed path 
$\partial (\sigma, \tau)$ depicted in Figure \ref{fig:81}.

\begin{figure} 
\includegraphics[scale=0.30]{fig81.jpg}
\caption{The boundary $\partial(\sigma, \tau)$ of the
kite $(\sigma, \tau)$  from Figure \ref{fig:80}.} 
\label{fig:81}
\end{figure}

\begin{thm}[Stokes Theorem for Triangles] \label{thm:19}
Let $\mbf{C} = (G, H, \Psi, \Phi)$
be a Lie crossed module, $(X, x_0)$ a pointed manifold, and
$(\alpha, \beta)$ a connection-curvature pair for $\mbf{C} / X$.
Given any smooth triangular kite 
$(\sigma, \tau)$ in $(X, x_0)$, one has
\[ \Phi \bigl( \opn{MI} (\alpha, \beta \vert \sigma, \tau) \bigr)
= \opn{MI} (\alpha \vert \partial(\sigma, \tau)) \]
in $G$.
\end{thm}

The special case $G = H = \opn{GL}_m(\R)$ is Schlesinger's Theorem 
(see \cite{DF, KMR}).



\subsection{}
We now approach the main result of the paper, namely the nonabelian
$3$-dimensional Stokes Theorem. 

A {\em smooth triangular balloon} in $(X, x_0)$ is a pair $(\sigma, \tau)$,
consisting of smooth maps
$\sigma : \bsym{\Delta}^1 \to X$ and
$\tau : \bsym{\Delta}^3 \to X$, such that
$\sigma(v_0) = x_0$ and
$\sigma(v_1) = \tau(v_0)$. 
See Figure \ref{fig:82} for an illustration.

\begin{figure} 
\includegraphics[scale=0.27]{fig82.jpg}
\caption{A smooth triangular balloon $(\sigma, \tau)$ in the pointed manifold 
$(X, x_0)$.} 
\label{fig:82}
\end{figure}

The {\em boundary} of a balloon $(\sigma, \tau)$ is a sequence
\[ \partial (\sigma, \tau) =
\bigl( \partial_1 (\sigma, \tau),\, \partial_2 (\sigma, \tau),\, 
\partial_3 (\sigma, \tau),\, \partial_4 (\sigma, \tau) \bigr) \]
of triangular kites. See Figure \ref{fig:86}. We write
\begin{equation} \label{eqn:166}
\opn{MI}(\alpha, \beta \vert \partial (\sigma, \tau)) :=
\prod_{1 = 1}^4 \ \opn{MI}(\alpha, \beta \vert \partial_i (\sigma, \tau)) , 
\end{equation}
where the order of the product is left to right.

\begin{figure} 
\includegraphics[scale=0.36]{fig86.jpg}
\caption{The four triangular kites that make up the sequence 
$\partial (\sigma, \tau)$. Here $(\sigma, \tau)$ is the triangular balloon
from Figure \ref{fig:82}.} 
\label{fig:86}
\end{figure}

Let $H_0 := \opn{Ker}(\Phi)$, which is a closed Lie subgroup of $H$. We call it
the {\em inertia subgroup}, and 
$\h_0 := \opn{Lie}(H_0)$ is called the {\em inertia subalgebra}.
Note that $H_0$ is contained in the center of $H$, so $H_0$ is an abelian Lie
group.  A form 
\[ \gamma \in \Omega^p(X) \otimes \h_0  \]
is called an {\em inert $p$-form}.

We say that a form 
$\alpha \in \Omega^1(X) \otimes \g$
is {\em tame connection} if it belongs to some 
connection-curvature pair $(\alpha, \beta)$.
We show (in Subsection \ref{subsec:inert}) that given a tame connection 
$\alpha$ and an inert $3$-form $\gamma$, there is a well defined
{\em twisted abelian multiplicative integral}
\[ \opn{MI}(\alpha, \gamma \vert \sigma, \tau) \in H_0 . \]

For $g \in G$ there is a Lie group automorphism
$\Psi(g) : H \to H$. Its derivative is
\[ \Psi_{\h}(g) := \opn{Lie}(\Psi(g)) : \h \to \h . \]
As $g$ varies we get a map of Lie groups
\begin{equation} \label{eqn:231}
\Psi_{\h} : G \to \opn{GL}(\h) . 
\end{equation}
The derivative of $\Psi_{\h}$ is a map of Lie algebras
\[ \opn{Lie}(\Psi_{\h}) : \g \to  
\mfrak{gl}(\h) = \opn{End}(\h) . \]
This extends by tensor product to a homomorphism of differential graded Lie
algebras
\[ \psi_{\h} :  \Omega(X) \otimes \g \to \Omega(X) \otimes \opn{End}(\h) . \]
Given a connection-curvature $(\alpha, \beta)$, its {\em $3$-curvature}
is the form
\begin{equation} \label{eqn:167}
\gamma := \d(\beta) + \psi_{\h}(\alpha)(\beta) \in 
\Omega^3 \otimes \h .
\end{equation}
(This is the name given in \cite{BM}.)

We can now state the main result of the paper. (See Theorem \ref{thm:22} for the
full version.)

\begin{thm}[Stokes Theorem for Tetrahedra] \label{thm:20}
Let $\mbf{C} = (G, H, \Psi, \Phi)$
be a Lie crossed module, $(X, x_0)$ a pointed manifold, and
$(\alpha, \beta)$ a connection-curvature pair for $\mbf{C} / X$.
Let $\gamma$ be the $3$-curvature of $(\alpha, \beta)$. Then:
\begin{enumerate}
\item The form $\gamma$ is inert.
\item Given any smooth triangular balloon 
$(\sigma, \tau)$ in $(X, x_0)$, one has
\[ \opn{MI} (\alpha, \beta \vert \partial(\sigma, \tau)) =
\opn{MI} (\alpha, \gamma \vert \sigma, \tau) \]
in $H$.
\end{enumerate}
\end{thm}

In this generality, Theorem \ref{thm:20} appears to have no precursor
in the literature. The special (but most important) case, namely
$\gamma = 0$, was taken to be true in some papers (e.g.\ \cite{Ko, BS}), but
no proofs were provided there. 

Assertion (1) in the theorem can be viewed as a {\em generalized Bianchi
identity}. 



\subsection{} \label{subsec:methods}
In this and the next few subsections we will explain some of the work
leading to the theorems mentioned above.

The methods used in the constructions and proofs are of two kinds: geometric
and infinitesimal. The geometric methods consist of dividing kites into smaller
ones, and studying the effect on the corresponding approximations (Riemann
products). The infinitesimal methods involve Taylor expansions and estimates
for the nonabelian exponential map. 

Throughout most of the paper we work with {\em linear quadrangular kites}
in {\em polyhedra}, and with {\em piecewise smooth differential forms},
rather than with smooth triangular kites in manifolds and smooth differential
forms. The reason for choosing quadrangular kites is mainly that it is much
easier to carry out calculations of Taylor expansions on squares, as compared to
triangles. Also the combinatorics of quadrangular kites and their binary
subdivisions is simpler than that of triangles. See Subsections 
\ref{subsec:kites}-\ref{subsec:bintes}. A review of the piecewise linear
geometry of poyhedra, and of piecewise smooth differential forms, can be found
in Section \ref{sec:pws}.

The key technical result that allows us to calculate nonabelian products is 
Theorem \ref{thm:6} on estimates for the nonabelian exponential map. These
estimates are gotten from the CBH formula. Section \ref{sec:expon} is devoted
to the proof of these estimates.

For heuristic purposes we introduce the concept of ``tiny scale''. By tiny scale
(depending on context of course) we mean
geometric or algebraic elements that are so small that the relevant estimates
(arising from the CBH formula or Taylor expansion) apply to them. See Remark
\ref{rem:3}.



\subsection{}
For $n \geq 0$ let $\mbf{I}^n$ be the $n$-dimensional cube. We give names 
to some vertices:
$v_0 := (0, \ldots, 0)$, and
\[ v_i := (0, \ldots, 1, \ldots, 0) \]
with $1$ in the $i$-th position, for $i = 1, \ldots, n$.
The base point for $\mbf{I}^n$ is $v_0$. 

Let $(X, x_0)$ be a pointed polyhedron. By {\em linear string} in 
$X$ we mean a sequence
$\sigma = (\sigma_1, \ldots, \sigma_m)$ of 
piecewise linear maps $\sigma_i : \mbf{I}^1 \to X$,
such that $\sigma_i(v_1) = \sigma_{i+1}(v_0)$. 
The maps $\sigma_i$ are called the pieces of $\sigma$. 
In Section \ref{sec:dim1} we construct the nonabelian multiplicative 
integral $\opn{MI}(\alpha \vert \sigma)$
of a piecewise smooth differential form
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$
on a string $\sigma$. This construction is quite simple and essentially the
same as the classical one. We also prove a few basic properties of this
MI. 



\subsection{} \label{subsec:binary}
In Section \ref{sec.MI} we construct the $2$-dimensional
nonabelian multiplicative integral
$\opn{MI}(\alpha, \beta \vert \sigma, \tau)$. 
Here $(\sigma, \tau)$ is a linear quadrangular kite in the pointed polyhedron
$(X, x_0)$. By definition this means that $\sigma$ is a string in $X$, and
$\tau : \mbf{I}^2 \to X$ is a linear map. The conditions are that the initial
point of $\sigma$ is $x_0$, and the terminal point of $\sigma$ is 
$\tau(v_0)$. The integrand $(\alpha, \beta)$ consists of piecewise smooth
differential forms:
\[ \alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g \ \text{ and } \
\beta \in  \Omega^2_{\mrm{pws}}(X) \otimes \h . \]

The coarse approximation of the $2$-dimensional
nonabelian multiplicative integral is as follows. 
Given a kite  $(\sigma, \tau)$ in $(X, x_0)$, let
\[ g := \opn{MI}(\alpha \vert \sigma) \in G ; \]
so applying the operator $\Psi_{\h}(g)$ from (\ref{eqn:231})
we have a new (twisted) $2$-form
\[ \Psi_{\h}(g)(\beta) \in \Omega_{\mrm{pws}}^2(X) \otimes \h . \]
We define the {\em basic Riemann product} 
of $(\alpha, \beta)$ on $(\sigma, \tau)$ to be
\begin{equation} \label{eqn:238}
\opn{RP}_0(\alpha, \beta \vert \sigma, \tau) :=
 \exp_H \Bigl( \int_{\tau} \Psi_{\h}(g)(\beta) \Bigr) \in H .
\end{equation}
(Actually in the body of the paper we use another formula for \lb
$\opn{RP}_0(\alpha, \beta \vert \sigma, \tau)$, that converges
faster; see Definition \ref{dfn:11} and Remark \ref{rem:4}.)

For the limiting process we introduce the {\em binary
subdivisions} of $\mbf{I}^2$. The $k$-th binary subdivision is the cellular
decomposition of $\mbf{I}^2$ into $4^k$ equal squares, and we denote it by
$\opn{sd}^k \mbf{I}^2$. The $1$-skeleton of $\opn{sd}^k \mbf{I}^2$ is denoted
by $\opn{sk}_1 \opn{sd}^k \mbf{I}^2$. Its fundamental group (based at $v_0$) is
denoted by
$\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$. 
It is very important that the group 
$\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$ is a  free group on $4^k$
generators. 
We say that a kite $(\sigma, \tau)$ is {\em patterned on $\opn{sd}^k \mbf{I}^2$}
if for every piece $\sigma_i$ of the string $\sigma$, the image
$\sigma_i(\mbf{I}^1)$ is a $1$-cell of $\opn{sd}^k \mbf{I}^2$, and
$\tau(\mbf{I}^2)$ is a $2$-cell of $\opn{sd}^k \mbf{I}^2$.

A {\em tessellation} of $\mbf{I}^2$ is by definition a sequence
$\bigl( (\sigma_i, \tau_i) \bigr)_{i = 1, \ldots, 4^k}$
of square kites in $(\mbf{I}^2, v_0)$, each patterned on 
$\opn{sd}^k \mbf{I}^2$, satisfying the following topological condition.
Let us denote by $[\partial (\sigma_i, \tau_i)]$ the element of
$\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$
represented by the closed string $\partial (\sigma_i, \tau_i)$. Then
\begin{equation} \label{eqn:168}
\prod_{1 = 1}^{4^k}\ [\partial (\sigma_i, \tau_i)] = 
[\partial \mbf{I}^2] 
\end{equation}
in $\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$.

For the construction we choose a particular tessellation for every $k$. It is
called the {\em $k$-th binary tessellation}, and the notation is
$\opn{tes}^k  \mbf{I}^2$. The actual definition of $\opn{tes}^k  \mbf{I}^2$
is not important (since it is
quite arbitrary, and chosen for convenience). All that is important are its two
properties:
\begin{itemize}
\item It is a tessellation; i.e.\ equation (\ref{eqn:168}) holds.
\item It has a recursive (self similar) nature.
\end{itemize}

For fixed $k$ and a kite $(\sigma, \tau)$ we obtain, by a simple geometric
operation, the $k$-binary tessellation 
\[ \opn{tes}^k (\sigma, \tau) = 
\bigl( \opn{tes}^k_i (\sigma, \tau) \bigr)_{i = 1, \ldots, 4^k} \]
of $(\sigma, \tau)$, which is a sequence of kites in $(X, x_0)$. 
(See Definition \ref{dfn:44}.)

For every $i \in \{ 1, \ldots, 4^k \}$ we have the basic Riemann product
\[ \opn{RP}_0(\alpha, \beta \vert \opn{tes}^k_i (\sigma, \tau)) \]
on the kite $\opn{tes}^k_i (\sigma, \tau)$. 
We define the {\em $k$-th Riemann product} to be 
\begin{equation} \label{eqn:170}
\opn{RP}_k(\alpha, \beta \vert \sigma, \tau) :=
\prod_{1 = 1}^{4^k}\ 
\opn{RP}_0(\alpha, \beta \vert \opn{tes}^k_i (\sigma, \tau)) .
\end{equation}

In Theorem \ref{thm:12} we prove that the limit
\[ \lim_{k \to \infty} \opn{RP}_k(\alpha, \beta \vert \sigma, \tau) \]
exists in $H$. The proof goes like this: for sufficiently large $k$ the 
kites $\opn{tes}^k_i (\sigma, \tau)$ are all tiny. We use estimates 
to show that the limits
\[ \lim_{k' \to \infty} \opn{RP}_{k'}(\alpha, \beta \vert 
\opn{tes}^k_i (\sigma, \tau) ) \]
exist for every $i$. Due to the recursive nature of the binary tessellations,
this is enough.  We can finally define
\begin{equation} 
\opn{MI}(\alpha, \beta \vert \sigma, \tau) := 
\lim_{k \to \infty} \opn{RP}_k(\alpha, \beta \vert \sigma, \tau) . 
\end{equation}



\subsection{}
In Section \ref{sec:stokes2} we prove the $2$-dimensional Stokes Theorem.
It is the same as Theorem \ref{thm:19}, except that it talks about 
piecewise smooth forms on a pointed polyhedron and linear quadrangular kites. 
Again the proof is by reduction (using the recursive nature of the binary
tessellations) to the case of a tiny kite. And then we use approximations 
(both of Taylor expansions and the exponential map) to do the
calculation. 

A very important technical consequence of the $2$-dimensional Stokes Theorem
is:

\begin{thm}[Fundamental Relation] \label{thm:21}
Let $\mbf{C} = (G, H, \Psi, \Phi)$
be a Lie crossed module, $(X, x_0)$ a pointed polyhedron, 
$(\alpha, \beta)$ a piecewise smooth \lb connection-curvature pair for 
$\mbf{C} / X$, and $(\sigma, \tau)$ a linear quadrangular kite in $(X, x_0)$.
Consider the elements
\[ g := \opn{MI} \bigl( \alpha \vert \partial (\sigma, \tau) \bigr) \in G \]
and
\[ h :=  \opn{MI} (\alpha, \beta \vert \sigma, \tau) \in H . \]
Then
\[ \Psi(g) = \opn{Ad}_H(h) \]
as automorphisms of the Lie group $H$. 
\end{thm}

In Section \ref{sec:stokes-3} we prove the first version of the main 
result of the paper,
namely the $3$-dimensional Stokes Theorem (Theorem \ref{thm:10}). 
This is like Theorem \ref{thm:20}, only for piecewise smooth
connection-curvature pairs, and for linear quadrangular balloons. 

The strategy of the proof is this. Using Theorem \ref{thm:21}, and a lot of
combinatorics of free groups (done in Section \ref{sec:puzzles}), we reduce the
problem to the case of a tiny balloon. And for a tiny balloon we use Taylor
expansions and the estimates from Theorem \ref{thm:6}.



\subsection{} \label{subsec:triangles}
Finally, in Section \ref{sec:simpl}, we show how to pass from quadrangular
kites  to triangular ones. 
This is very easy, using the following trick. The triangle 
$\bsym{\Delta}^2$ is naturally embedded in the square $\mbf{I}^2$; and 
there is a piecewise linear retraction 
$h : \mbf{I}^2 \to \bsym{\Delta}^2$. 
Consider the ``universal triangular kite'' 
$(\sigma', \tau')$ , and the ``universal quadrangular kite''
$(\sigma', \tau'')$, both 
in $(\mbf{I}^2, v_0)$; see Figures \ref{fig:55}, \ref{fig:84} and \ref{fig:85}.
There is a piecewise linear retraction 
\[ g : \mbf{I}^2 \to \sigma'(\mbf{I}^1) \cup \tau'(\mbf{I}^2) . \]
These maps are
related by 
\[ \tau' \circ h = g \circ \tau'' , \]
as maps $\mbf{I}^2 \to \mbf{I}^2$.

Given a smooth kite $(\sigma, \tau)$ in a pointed manifold
$(X, x_0)$, there a piecewise smooth map
$f :  \mbf{I}^2 \to X$
such that 
$f \circ \sigma' = \sigma$ and
$f \circ \tau' = \tau$. Given a smooth connection-curvature pair
$(\alpha, \beta)$ for $\mbf{C} / X$, the pair
\[ (\alpha', \beta') := (f^*(\alpha), f^*(\beta)) \]
is a piecewise smooth connection-curvature pair
$(\alpha, \beta)$ for $\mbf{C} / \mbf{I}^2$.
We define
\begin{equation} \label{eqn:173}
\opn{MI}(\alpha, \beta \vert \sigma, \tau) :=
\opn{MI}(\alpha', \beta' \vert \sigma', \tau'') . 
\end{equation}

The results proved for quadrangular kites can be easily transferred to
triangular kites by similar geometric tricks.  



\subsection{} \label{subsec:motiv}
The reason we became interested in nonabelian multiplicative integration is its
application to twisted deformation quantization of algebraic
varieties, as developed in our paper \cite{Ye3} (see also the survey article
\cite{Ye4}). Twisted deformations of an algebraic variety $X$ are very close to
gerbes and to stacks of algebroids (in the sense of \cite{Ko}). 
Our original strategy was to classify these twisted deformations in
terms of Maurer-Cartan solutions in a DG Lie algebra gotten as the commutative
\v{C}ech resolution of a sheaf of DG Lie algebras on $X$. The multiplicative
integration was supposed to be a key component of this construction. Some of the
details are explained in Subsections \ref{subsec:QTDGLie}, \ref{subsec:CosDGLie}
and  \ref{subsec:conj.desc}.

In the meanwhile we discovered a more direct approach to the classification of
twisted deformations, using descent data in cosimplicial crossed groupoids, and
a related invariance result (see Sections 5-6 in the latest version of
\cite{Ye3}, and Theorem 0.1 in \cite{Ye6}). 

In the version of \cite{Ye3} dated 26 August 2009 there was a ``result''
labeled Theorem 11.2, about cosimplicial quantum type DG Lie algebras,
Deligne crossed groupoids and descent data. 
The proof of this ``result'' was only sketched, and we never completed the
proof (it was supposed to have appeared in a separate paper). It is now
presented as Conjecture \ref{conj:521} at the end of this paper. 

Speaking of conjectures, we should mention Conjecture \ref{conj:520} regarding
the rationality of the $2$-dimensional multiplicative integral when the Lie
groups $G$ and $H$ are unipotent algebraic groups. 

Despite the fact that the original motivation for this paper no longer exists,
we believe that the constructions and results presented here have 
independent value. This can be seen for instance by the role our work has in
the recent paper \cite{BGNT}. See the next subsection for a discussion of 
\cite{BGNT} and other related papers. 



\subsection{} \label{subsec:compare}
We end the introduction with a discussion of recent related work. 
Our $2$-dimensional nonabelian multiplicative integral is closely related to
the {\em differential geometry of gerbes}, as developed by Breen and Messing
\cite{BM}. Indeed, the notion of fake curvature, that goes into our definition
of connection-curvature pair, and the notion of $3$-curvature, are both taken
from \cite{BM}. 

There is a series of papers by Baez, Schreiber and Waldorf (\cite{BS},
\cite{SW1}, \cite{SW2} and others) on {\em nonabelian gauge theory}. They
develop a theory of nonabelian curvature that seems to be very similar to our 
$2$-dimensional nonabelian multiplicative integral, even though the flavor of
their work is very different (it is much more abstract). It seems that
\cite{SW2} contains a proof the $3$-dimensional Stokes Theorem in the special
case where the $3$-curvature is zero. 

Very recently the paper \cite{BGNT} by Bressler, Gorokhovsky, Nest and Tsygan
came out. The goal of this paper is to prove that several existing notions of
the nerve of a $2$-groupoid are equivalent (as simplicial sets). 
The comparison between the Hinich simplicial set and the Deligne-Getzler
simplicial set is done using  $2$-dimensional nonabelian multiplicative
integration. The method seems to be quite similar, at least morally, to our
original program (see previous subsection and Conjecture \ref{conj:521}). 
The $2$-dimensional nonabelian multiplicative integral that is developed in
Sections 4-5 of \cite{BGNT} is inspired by our work, and they obtain 
a version of our $3$-dimensional Stokes Theorem in their setting (see 
\cite[Theorems 5.1 and 5.2]{BGNT}). 

The difference between the construction in \cite{BGNT} and ours is that they
work in the special case of a Lie crossed module  $(G, H, \Psi, \Phi)$
consisting of unipotent algebraic groups $G$ and $H$, and an algebraic
connection-curvature pair $(\alpha, \beta)$ with vanishing $3$-curvature. The
construction goes like this: they write a particular partial differential
equation, and the multiplicative integral is its unique
solution. This construction is significantly shorter than ours; 
and presumably it coincides with our construction in this setup. 
Cf.\ Subsection \ref{subsec:PDEs} of our paper. 
See the end of Subsection \ref{subsec:ration} regarding the relation between
the work of \cite{BGNT} and Conjecture \ref{conj:520}.  



\medskip \noindent

\subsection{Acknowledgments}
Work on this paper began together with Fredrick Leitner, and I wish to
thank him for his contributions, without which the paper could not
have been written. Thanks also to Michael Artin, Maxim Kontsevich, 
Damien Calaque, Lawrence Breen, Amos Nevo, Yair Glasner, Barak Weiss and Victor
Vinnikov for assistance on various aspects of the paper. 







\cleardoublepage
