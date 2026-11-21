---
doc_id: arxiv-1007.1250v4
doc_title: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES"
section_id: sec-003-3-multiplicative-integration-in-dimension-one
section_title: "Multiplicative Integration in Dimension One"
section_number: 3
pages: 35-51
source_pdf: 1007.1250v4.pdf
source_sha256: 541ba4fb3068de8b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.975
doc_brief: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES — We construct a 2-dimensional twisted nonabelian multiplicative integral."
---
\label{sec:dim1}


Nonabelian multiplicative integration in dimension $1$ is classical, dating back
to work of Volterra (cf.\ \cite{DF}).
In modern differential geometry it is
usually viewed as the holonomy of a connection along a path. We prefer
to do everything from scratch, for several reasons: this allows us to introduce
notation; it serves as a warm-up for the much more difficult
$2$-dimensional integration; and also to cover the case of piecewise smooth
differential forms. 


\subsection{Binary Tessellations}
Recall that $\mbf{I}^1$ is the unit line segment in 
$\mbf{A}^{1} = \mbf{A}^{1}(\R)$, which we view as an oriented
polyhedron (cf.\ Section \ref{sec:pws}). The vertices
(endpoints) of $\mbf{I}^1$ are $v_0 = 0$ and $v_1 = 1$, and the coordinate
function is $t_1$. 

Let $X$ be a polyhedron. 
Consider a linear map $\sigma : \mbf{I}^{1} \to X$.
The length of the line segment $Z := \sigma(\mbf{I}^{1}) \subset X$
(possibly zero) is denoted
by $\opn{len}(\sigma)$. If  $\sigma$ is not constant then it is a conformal map,
and the scaling factor is precisely $\opn{len}(\sigma)$. In this case $\sigma$ 
determines an orientation on the $1$-dimensional polyhedron $Z$. We may choose
an orthonormal linear coordinate
function $f_1$ on $Z$, such that $\d f_1$ is the orientation of $Z$. Then 
$\sigma^*(\d f_1) = \opn{len}(\sigma) \cdot \d t_1$.

Next consider a piecewise linear map $\sigma : \mbf{I}^{1} \to X$.
By definition (cf.\ Subsection \ref{subsec:pws})
there is a linear triangulation $\{ Y_j \}_{j \in J}$ of $\mbf{I}^{1}$ such
that 
$\sigma|_{Y_j} : Y_j \to X$ 
is a linear map for every $j \in J$. We define
\[ \opn{len}(\sigma) := \sum_{j \in J_1} \opn{len}(\sigma_j) . \]

It is convenient to have a composition operation for piecewise linear maps.
Suppose $\sigma : \mbf{I}^1 \to X$ and
$\rho: \mbf{I}^1 \to \mbf{I}^1$ are piecewise linear maps.
Then the set-theoretical composition
$\sigma \circ \rho$ is also a piecewise linear map $\mbf{I}^1 \to X$.
Given finite sequences 
$\bsym{\sigma} = ( \sigma_i )_{i = 1, \ldots, m}$ and 
$\bsym{\rho} = ( \rho_j )_{j = 1, \ldots, n}$ of piecewise linear maps
$\sigma_i : \mbf{I}^{1} \to X$ and $\rho_j : \mbf{I}^{1} \to \mbf{I}^{1}$,
we define the sequence of piecewise linear maps
\[ \bsym{\sigma} \circ \bsym{\rho} := 
( \sigma_i \circ \rho_j )_{(i, j) \in \{ 1, \ldots, m \} \times
\{ 1, \ldots, n \} } \]
in lexicographical order, i.e.\ 
\begin{equation} \label{eqn:19}
\bsym{\sigma} \circ \bsym{\rho} = 
(\sigma_1 \circ \rho_1,\, \sigma_1 \circ \rho_2,\, \cdots, 
\sigma_2 \circ \rho_1,\, \sigma_2 \circ \rho_2,\, \cdots,
\sigma_m \circ \rho_n ) \ .
\end{equation}

\begin{dfn} \label{dfn:41}
For any $k \geq 0$, the {\em $k$-th binary tessellation} of $\mbf{I}^1$ is the
sequence
\[ \opn{tes}^k \mbf{I}^1 = ( \sigma^k_1, \ldots, \sigma^k_{2^k} ) \]
of linear maps in $\sigma^k_i : \mbf{I}^{1} \to \mbf{I}^1$ defined recursively
as follows.
\begin{itemize}
\item For $k = 0$ we define $\sigma^0_1$ to be the identity map of $\mbf{I}^1$.

\item For $k = 1$ we take the linear maps
$\sigma^1_1, \sigma^1_2$ defined on vertices by
\[ \sigma^1_1(v_0, v_1) := (v_0, \smfrac{1}{2}) , \]
\[ \sigma^1_2(v_0, v_1) := (\smfrac{1}{2}, v_1) . \]

\item For $k \geq 1$ we define
\[ \opn{tes}^{k+1} \mbf{I}^1 := 
(\opn{tes}^1 \mbf{I}^1) \circ (\opn{tes}^k \mbf{I}^1) , \]
using the convention (\ref{eqn:19}).
\end{itemize}
\end{dfn}

We call $\sigma^0_1$ the {\em basic map}.

See Figure \ref{fig:40} for an illustration of $\opn{tes}^2 \mbf{I}^1$.

\begin{figure}
\includegraphics[scale=0.35]{fig40.jpg}
\caption{The $2$-nd binary tessellation of $\mbf{I}^{1}$. The arrowheads 
indicate the orientations of the linear maps 
$\sigma^2_i : \mbf{I}^{1} \to \mbf{I}^{1}$.} 
\label{fig:40}
\end{figure}


\subsection{Riemann Products}
Let $\g$ be a finite dimensional Lie algebra over $\R$. 
For any $n$-dimensional polyhedron $X$ we then have the DG Lie algebra  
of piecewise smooth $\g$-valued differential forms
\[ \Omega_{\mrm{pws}}(X) \otimes \mfrak{g} = \bigoplus_{p=0}^n \,
\Omega^p_{\mrm{pws}}(X) \otimes \mfrak{g}  \]
(Subsection \ref{subsec:pws}). 
The operations are as follows: for 
$\alpha_i \in \Omega^{p_i}_{\mrm{pws}}(X)$ and
$\gamma_i \in \g$ one has
\[ \d(\alpha_1 \otimes \gamma_1) = \d(\alpha_1) \otimes \gamma_1 
\in \Omega_{\mrm{pws}}^{p_1+1}(X) \otimes \g \]
and
\[ [ \alpha_1 \otimes \gamma_1,\, \alpha_2 \otimes \gamma_2 ] =
(\alpha_1 \wedge \alpha_2) \otimes [\gamma_1, \gamma_2] \in 
\Omega_{\mrm{pws}}^{p_1+ p_2}(X) \otimes \g . \]
By definition, any particular piecewise smooth differential form $\alpha$
belongs to 
$\Omega_{\mrm{pws}}(X; T) \otimes \mfrak{g}$, 
for some linear triangulation $T$ of $X$. 
This construction is functorial in the following sense. Suppose
$f : X \to Y$ is a piecewise linear map of polyhedra, and $\phi : \g \to \h$ is
map of Lie algebras. Then there is a homomorphism of DG Lie algebras
\[ f^* \otimes \phi : \Omega_{\mrm{pws}}(Y) \otimes \mfrak{g} \to 
\Omega_{\mrm{pws}}(X) \otimes \mfrak{h} . \]
In case $\h = \g$ and $\phi$ is the identity map, we shall often write
$f^*$ instead of $f^* \otimes \phi$.

{}From now on in this section we consider a Lie group $G$, with Lie
algebra $\mfrak{g}$, and a polyhedron $X$.
We fix some euclidean norm $\norm{-}$ on the vector space $\g$. As in
Section \ref{sec:pws} we also fix an open neighborhood $V_0(G)$ of $1$ in
$G$ on which $\log_G$ is defined, a convergence radius
$\epsilon_0(G)$, and a commutativity constant $c_0(G)$.
The choices of $V_0(G)$, $\epsilon_0(G)$ and $c_0(G)$ are auxiliary only; they
are needed for the proofs, but do not effect the results.

\begin{dfn} \label{dfn:1}
Let
$\alpha \in \Omega^1_{\mrm{pws}}(\mbf{I}^1) \otimes \mfrak{g}$. 
The {\em basic Riemann product of $\alpha$ on $\mbf{I}^1$} 
is the element 
\[ \opn{RP}_0(\alpha \vert \mbf{I}^1) \in G \]
defined as follows. Let 
$w := \smfrac{1}{2}$, namely the midpoint of $\mbf{I}^{1}$. 
\begin{itemize}
\item Suppose $w$ is a smooth point of $\alpha$. Then there is
some $1$- \lb dimensional simplex $Y$ in $\mbf{I}^{1}$, such that 
$w \in \opn{Int} Y$ and $\alpha|_{Y}$ is smooth. 
Let $\til{\alpha} \in \mcal{O}(Y) \otimes \mfrak{g}$ be the coefficient of
$\alpha|_Y$, as in Definition \ref{dfn:24}; namely
\[ \alpha|_Y = \til{\alpha} \cdot \d t_1 . \]
We define 
\[ \opn{RP}_{0}(\alpha \vert \mbf{I}^{1}) :=
\opn{exp}_G \bigl(  \til{\alpha}(w) \bigr) . \]

\item If $w$ is a singular point of $\alpha$, then we let
$\opn{RP}_{0}(\alpha \vert \mbf{I}^{1}) := 1$.
\end{itemize}
\end{dfn}

Observe that the element $\til{\alpha}(w) \in \g$ in the definition above is
independent of
the simplex $Y$. 

\begin{dfn} \label{dfn:12}
Let 
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \mfrak{g}$,
and let $\sigma : \mbf{I}^{1} \to X$ be a piecewise linear map. Then
$\sigma^*(\alpha) \in \Omega^1_{\mrm{pws}}(\mbf{I}^1) \otimes \mfrak{g}$,
and we define the 
{\em basic Riemann product of $\alpha$ along $\sigma$} to be 
\[ \opn{RP}_{0}(\alpha \vert \sigma) :=
\opn{RP}_{0} \bigl( \sigma^*(\alpha) \vert \mbf{I}^{1} \bigr) \in G . \]
\end{dfn}

Note that if $\sigma$ is a constant map then 
$\sigma^*(\alpha) = 0$, so 
$\opn{RP}_{0}(\alpha \vert \bsym{\sigma}) = 1$.

\begin{dfn} \label{dfn:2}
Let 
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \mfrak{g}$,
and let $\sigma : \mbf{I}^{1} \to X$ be a piecewise linear map.
For $k \geq 0$ we define the {\em $k$-th refined Riemann product of $\alpha$
along $\sigma$} to be 
\[ \opn{RP}_{k}(\alpha \vert \sigma) :=
\prod_{i = 1}^{2^k} \,
\opn{RP}_{0} ( \alpha \vert \sigma \circ \sigma^k_i ) \in G , \]
using the $k$-th binary tessellation
$\opn{tes}^k \mbf{I}^1 = ( \sigma^k_1, \ldots, \sigma^k_{2^k})$
and the convention (\ref{eqn:6}).
\end{dfn}


\subsection{Convergence of Riemann Products}
As before we are given a form
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$. 
Recall $\norm{\alpha}_{\mrm{Sob}}$, the Sobolev norm to order $2$ of $\alpha$,
from Subsection \ref{subsec:sob}.

\begin{lem} \label{lem:1}
There are constants $c_1(\alpha)$ and $\epsilon_1(\alpha)$ with the
following properties.
\begin{enumerate}
\rmitem{i} These inequalities hold:
\begin{gather*}
0 < \epsilon_1(\alpha) \leq 1 \, , \\
c_1(\alpha) \geq 1 \, , \\
\epsilon_1(\alpha) \cdot c_1(\alpha) \leq \smfrac{1}{2} \cdot
\epsilon_0(G) \ .
\end{gather*}

\rmitem{ii} For any piecewise linear map 
$\sigma : \mbf{I}^1 \to X$ 
such that $\opn{len}(\sigma) < \epsilon_1(\alpha)$, and for any sufficiently
large $k$, one has
\[ \opn{RP}_{k}(\alpha \vert \sigma) \in V_0(G)  \]
and 
\[ \norm{\, \opn{log}_G \bigl( 
\opn{RP}_{k}(\alpha \vert \sigma) \bigr) \, }
\leq c_1(\alpha) \cdot \opn{len}(\sigma) . \]

\rmitem{iii} Moreover, if the map $\sigma$ in \tup{(ii)} is linear, then the
assertions there hold for any $k \geq 0$.
\end{enumerate} 
\end{lem}

\begin{proof}
We are given a piecewise linear map $\sigma : \mbf{I}^1 \to X$.
Let us write $\epsilon := \opn{len}(\sigma)$.
Excluding the trivial case, we may assume that $\epsilon > 0$.

Take $k \geq 0$. For any index
$i \in \{ 1, \ldots, 2^k \}$ let
$W_i := \sigma^k_i(\mbf{I}^1)$ and 
$w_i := \sigma^k_i(\smfrac{1}{2})$; so
$w_i$ is the midpoint of the segment ($1$-dimensional polyhedron) $W_i$. 
Define
$\epsilon_i := \opn{len}(\sigma \circ \sigma^k_i)$,
$Z_i := \sigma(W_i)$ and $z_i := \sigma(w_i)$. 
Note that 
$\sum_{i} \epsilon_i = \epsilon$.

We will say that an index $i$ is good if the map
$\sigma|_{W_i}$ is linear and injective. 
In this case $Z_i$ is a segment of length $\epsilon_i$ and midpoint $z_i$. 
Otherwise we will call $i$ a bad index.
The sets of good and bad indices are denoted by $\opn{good}(k)$ and 
$\opn{bad}(k)$ respectively. Let $m$ be the number of singular points of the map
$\sigma$. Then $\abs{ \opn{bad}(k) } \leq m$. In particular, if $\sigma$ is
linear then $\opn{bad}(k) = \emptyset$.

Let
\[ \alpha' := \sigma^*(\alpha) \in \Omega^1_{\mrm{pws}}(\mbf{I}^1) \otimes \g .
\]
For an index $i$ we define an element
$\lambda_i \in \g$ as follows. If $w_i$ is a smooth point of $\alpha'$, then let
$\til{\alpha}'_i$ be the coefficient of $\alpha'$ near $w_i$, and let
\[ \lambda_i := (\smfrac{1}{2})^k \cdot \til{\alpha}'_i(w_i) . \]
Otherwise we let 
$\lambda_i := 0$.
In any case we have
\[ \exp_G(\lambda_i) = \opn{RP}_{0}(\alpha' \vert \sigma^k_i) = 
\opn{RP}_{0}(\alpha \vert \sigma \circ \sigma^k_i) . \]
Therefore
\begin{equation} \label{eqn:174}
\prod_{i = 1}^{2^k} \, \exp_G(\lambda_i) = 
\opn{RP}_{k}(\alpha \vert \sigma) .
\end{equation}
Furthermore, if $i$ is a good index and $w_i$ is a smooth point of $\alpha'$,
then $z_i$ is a smooth point $\alpha|_{Z_i}$, and then 
\begin{equation} \label{eqn:175}
\lambda_i = \epsilon_i \cdot \til{\alpha}_i(z_i) , 
\end{equation}
where $\til{\alpha}_i$ is the coefficient of $\alpha|_{Z_i}$ near $z_i$. 

Now here are the estimates. For any index $i$  we have 
\[ \norm{ \lambda_i } \leq (\smfrac{1}{2})^k \cdot \norm{ \alpha' }_{\mrm{Sob}}
\, . \]
If $i$ is a good index then by (\ref{eqn:175}) we have
\[ \norm{ \lambda_i } \leq \epsilon_i \cdot \norm{ \alpha }_{\mrm{Sob}} \, . \]
Hence
\begin{equation} \label{eqn:176}
\begin{aligned}
& \sum_{i = 1}^{2^k} \, \norm{ \lambda_i } = 
\sum_{i \in \opn{good}(k)} \, \norm{ \lambda_i } + 
\sum_{i \in \opn{bad}(k)} \, \norm{ \lambda_i } \\
& \qquad \leq 
\epsilon \cdot \norm{ \alpha }_{\mrm{Sob}} +
m \cdot (\smfrac{1}{2})^k \cdot \norm{ \alpha' }_{\mrm{Sob}} \, . 
\end{aligned}
\end{equation}

Let
\[ \epsilon_1(\alpha) := \smfrac{1}{2} \cdot 
(1 + \norm{ \alpha }_{\mrm{Sob}})^{-1} \cdot \epsilon_0(G) \]
and
\[ c_1(\alpha) := 2 \cdot \bigl( 1 + c_0(G) \cdot \norm{ \alpha }_{\mrm{Sob}}
\bigr) \, . \]
Choose $k_0$ large enough so that 
\[ m \cdot (\smfrac{1}{2})^{k_0} \cdot \norm{ \alpha' }_{\mrm{Sob}} < 
\min \bigl( \smfrac{1}{2} \cdot \epsilon_0(G), \,
\smfrac{1}{2} \cdot c_1(\alpha) \cdot \epsilon \cdot 
(1 + c_0(G))^{-1} \bigr) \, . \]
If $\sigma$ is linear then $m = 0$, and we may take $k_0 := 0$.

Now suppose that $\epsilon < \epsilon_1(\alpha)$ and $k \geq k_0$.
According to inequality (\ref{eqn:176}) we have
\[ \sum_{i = 1}^{2^k} \, \norm{ \lambda_i } < \epsilon_0(G) \, . \]
Therefore by property (ii) of Theorem \ref{thm:6} and by formula
(\ref{eqn:174}) we get
\[ \opn{RP}_{k}(\alpha \vert \sigma) \in V_0(G)  \]
and 
\[ \norm{\, \opn{log}_G \bigl( 
\opn{RP}_{k}(\alpha \vert \sigma) \bigr) \, }
\leq c_0(G) \cdot \bigl( \bosum_{i = 1}^{2^k} \, \norm{ \lambda_i } \bigr)
\leq c_1(\alpha) \cdot \epsilon \, . \]
\end{proof}

\begin{rem} \label{rem:3}
Heuristically we think of $\epsilon$ in the proof of the lemma above as a
``tiny'' size. In the ``tiny scale'' we can measure things (i.e.\ 
$\norm{\log_G(g)}$ is defined), and we can use Taylor series and CBH series. 
\end{rem}

\begin{lem} \label{lem:30}
There are constants $c_2(\alpha)$ and $\epsilon_2(\alpha)$ with the
following properties.
\begin{enumerate}
\rmitem{i} These inequalities hold:
\begin{gather*}
0 < \epsilon_2(\alpha) \leq \epsilon_1(\alpha)  \, , \\
c_2(\alpha) \geq c_1(\alpha) \,  .
\end{gather*}

\rmitem{ii} Suppose $\sigma : \mbf{I}^{1} \to X$ is a linear map
such that $\opn{len}(\sigma) < \epsilon_2(\alpha)$, and 
$\alpha|_{\sigma(\mbf{I}^{1})}$ is smooth.
Then for any $k \geq 0$ one has 
\[ \Norm{ 
\opn{log}_G \bigl( \opn{RP}_{k}(\alpha \vert \sigma) \bigr) -
\opn{log}_G \bigl( \opn{RP}_{0}(\alpha \vert \sigma) \bigr) }
\leq c_2(\alpha) \cdot \opn{len}(\sigma)^3 . \]
\end{enumerate}
\end{lem}

\begin{proof}\item
Take
\[ \epsilon_2(\alpha) := \min \bigl( \epsilon_1(\alpha), \,
\smfrac{1}{4} \epsilon_0(G) \cdot (1 + \norm{\alpha}_{\mrm{Sob}})^{-1} 
\bigr) \, . \]

Let $\sigma$ be a linear map with $\epsilon := \opn{len}(\alpha)$ satisfying
$0 < \epsilon < \epsilon_2(\alpha)$.
Let $Z := \sigma(\mbf{I}^{1})$, which is a $1$-dimensional oriented polyhedron,
and $z := \sigma(\smfrac{1}{2})$, the midpoint of $Z$.
Choose a positively oriented orthonormal linear coordinate function $s_1$
on $Z$, such that $s_1(z) = 0$.

Let $\til{\alpha} \in \mcal{O}(Z) \otimes \g$ be the coefficient of
$\alpha|_Z$, i.e.\ 
$\alpha|_Z = \til{\alpha} \cdot \d t_1$. 
Consider the Taylor expansion to second order of the smooth function
$\til{\alpha} : Z \to \g$, around the point $z$:
\begin{equation} \label{eqn:67}
\til{\alpha}(x) =  a_0 + s_1(x) \cdot a_1 + s_1(x)^2 \cdot g(x) 
\end{equation}
for $x \in Z$, where
$a_0 := \til{\alpha}(z) \in \g$,
$a_1 := (\smfrac{\partial}{\partial s_1} \til{\alpha})(z) \in \g$,
and $g : Z \to \g$ is a continuous function.
We know that
\begin{equation*} 
\norm{a_0} , \,
\norm{a_1} , \,
\norm{g(x)} \leq \norm{\alpha}_{\mrm{Sob}}  \, .
\end{equation*}
And, as we have seen before, 
\begin{equation} \label{eqn:71}
 \opn{RP}_{0}(\alpha \vert \sigma) = 
\opn{exp}_G \bigl(  \epsilon a_0 \bigr) .
\end{equation}

Take $k \geq 0$. For $i \in \{ 1, \ldots, 2^k \}$ let
$\sigma_i := \sigma \circ \sigma^k_i$ and
$z_i := \sigma_i(\smfrac{1}{2})$. 
Since 
$\epsilon < \epsilon_2(\alpha)$ it follows that 
\begin{equation} \label{eqn:66}
\sum_{i = 1}^{2^k} \,
\norm{ (\smfrac{1}{2})^k \epsilon \cdot a_0 } 
\leq \epsilon \cdot \norm{\alpha}_{\mrm{Sob}} \leq \smfrac{1}{4} \epsilon_0(G)
\, .
\end{equation}
Because  
$\abs{ s_1(z_i) } \leq  \smfrac{1}{2} \epsilon$ we also have
\begin{equation} \label{eqn:10}
\sum_{i = 1}^{2^k} \,
\norm{ (\smfrac{1}{2})^k \epsilon \cdot s_1(z_i) \cdot a_1 } 
\leq \smfrac{1}{2} \epsilon^2 \cdot \norm{\alpha}_{\mrm{Sob}}
\leq \smfrac{1}{4} \epsilon_0(G) 
\end{equation}
and 
\begin{equation} \label{eqn:8}
\sum_{i = 1}^{2^k} \,
\norm{ (\smfrac{1}{2})^k \epsilon \cdot s_1(z_i)^2 \cdot g(z_i) } 
\leq \smfrac{1}{4} \epsilon^3  \cdot \norm{\alpha}_{\mrm{Sob}}
\leq \smfrac{1}{4} \epsilon_0(G) \, .
\end{equation}

Define
\[ \lambda_i := (\smfrac{1}{2})^k \epsilon \cdot \til{\alpha}(z_i) \in \g . \]
By the Taylor expansion (\ref{eqn:67}) we have
\begin{equation} \label{eqn:69}
\lambda_i =  (\smfrac{1}{2})^k \epsilon \cdot a_0 + 
(\smfrac{1}{2})^k \epsilon \cdot s_1(z_i) \cdot a_1 + 
(\smfrac{1}{2})^k \epsilon \cdot s_1(z_i)^2 \cdot g(z_i)  .
\end{equation}
Since $\sigma^*(\d s_1) = \epsilon \cdot \d t_1$, we see that 
\[ \opn{RP}_{0}(\alpha \vert \sigma_i) = 
\opn{exp}_G(\lambda_i) , \]
and hence 
\begin{equation} \label{eqn:70}
\opn{RP}_{k}(\alpha \vert \sigma) = 
\prod_{i = 1}^{2^k} \ 
\opn{exp}_G (\lambda_i) . 
\end{equation}

Because the constant terms in the Taylor expansions (\ref{eqn:69}) of the
$\lambda_i$ are all equal to 
$(\smfrac{1}{2})^k \epsilon \cdot  a_0$, 
we can use property (v) of Theorem \ref{thm:6}, together with the estimates 
(\ref{eqn:66}), (\ref{eqn:10}), (\ref{eqn:8}), to deduce
\begin{equation}  \label{eqn:15}
\begin{aligned}
& \Norm{ \log_G \Bigl( \boprod_{i = 1}^{2^k}  \, \exp_G (\lambda_i) \Bigr)
 - \bosum_{i = 1}^{2^k} \, \lambda_i } \\
& \qquad \leq c_0(G) \cdot \bigl( 
\epsilon \cdot \norm{\alpha}_{\mrm{Sob}} \cdot 
(1 + \smfrac{1}{2} \epsilon + \smfrac{1}{4} \epsilon^2 ) \bigr)
\cdot \bigl( \epsilon \cdot \norm{\alpha}_{\mrm{Sob}} \cdot 
(\smfrac{1}{2} \epsilon + \smfrac{1}{4} \epsilon^2 ) \bigr) \\
& \qquad \leq \epsilon^3 \cdot c_0(G) \cdot 
\norm{\alpha}_{\mrm{Sob}}^2 \cdot 2 \, . 
\end{aligned} 
\end{equation}
Trivially the sum of the constant terms of the Taylor expansions of the
$\lambda_i$ is
\[ \sum_{i=1}^{2^k}\,  (\smfrac{1}{2})^k \epsilon \cdot a_0 = 
\epsilon \cdot a_0 . \]
The linear terms satisfy
\[ s_1(z_i) = - s_1(z_{2^{k} - i}) \]
because of symmetry; and therefore they cancel out:
\[ \sum_{i=1}^{2^k}\,  (\smfrac{1}{2})^k \epsilon \cdot
s_1(z_i) \cdot a_1 = 0 . \]
Therefore, using the estimate (\ref{eqn:8}) to eliminate the quadratic terms of
the Taylor expansions, we conclude that
\begin{equation} \label{eqn:13}
\Norm{ \bosum_{i = 1}^{2^k} \,  \lambda_i - \epsilon a_0 } \leq 
\smfrac{1}{4} \epsilon^3  \cdot \norm{\alpha}_{\mrm{Sob}} . 
\end{equation}

Finally we define
\[ c_2(\alpha) := \max \bigl( c_1(\alpha), \, 
2 c_0(G) \cdot \norm{\alpha}_{\mrm{Sob}}^2 + 
\smfrac{1}{4} \cdot \norm{\alpha}_{\mrm{Sob}} \bigr) \, . \]
Combining equations (\ref{eqn:71}) and (\ref{eqn:70}), plus the estimates
(\ref{eqn:13}) and (\ref{eqn:15}), we obtain 
\[ \Norm{ \log_G \bigl( \opn{RP}_0 (\alpha \vert \sigma) \bigl) - 
\log_G \bigl( \opn{RP}_{k} (\alpha \vert \sigma) \bigl) } 
\leq c_2(\alpha) \cdot \epsilon^3  \, . \]
\end{proof}

\begin{dfn} \label{dfn:13}
Let us fix a constant $\epsilon_2(\alpha)$ as in Lemma
\ref{lem:30}. A piecewise linear map $\sigma : \mbf{I}^1 \to X$ with 
$\opn{len}(\sigma) < \epsilon_2(\alpha)$
will be called an {\em $\alpha$-tiny piecewise linear map} (in this section).
\end{dfn}

\begin{rem}
We shall use the term ``tiny'' several times in the paper, each time with a new
meaning, depending on context. The notion ``tiny'' should be considered as
``local to each section''. 
\end{rem}

\begin{lem} \label{lem:31}
Let $\sigma : \mbf{I}^{1} \to X$ be an $\alpha$-tiny linear map. Then
there is a constant $c_3(\alpha, \sigma) \geq 0$, 
such that for any integers $k' \geq k \geq 0$ one has
\[ \Norm{ \log_G \bigl( \opn{RP}_{k'} (\alpha \vert \sigma) \bigl) - 
\log_G \bigl( \opn{RP}_{k} (\alpha \vert \sigma) \bigl) }
\leq c_3(\alpha, \sigma) \cdot \opn{len}(\sigma) \cdot (\smfrac{1}{2})^k \, .
\]
\end{lem}

\begin{proof}
We may assume that $\opn{len}(\sigma) > 0$. 
Let $Z := \sigma(\mbf{I}^{1}) \subset X$, and let $m$ be the number of singular
points of the differential form $\alpha|_Z$. 

Take $k \geq 0$. For an index $i \in \{ 1, \ldots, 2^k \}$ define
$\sigma_i := \sigma \circ \sigma^k_i$
and $Z_i := \sigma_i(\mbf{I}^{1})$. We say that $i$ is good if 
$\alpha|_{Z_i}$ is smooth, and otherwise $i$ is bad. The set of good and
bad indices are denoted by $\opn{good}(k)$ and $\opn{bad}(k)$ respectively.
Since for any singular point $x$ of $\alpha|_Z$ there is at most one index $i$
such that $x \in \opn{Int} Z_i$, 
it follows that the cardinality of $\opn{bad}(k)$ is at most $m$. 

Next take $k' \geq k \geq 0$, and let $l := k' - k$. 
By the recursive definition of the binary tessellations we have
\[ \opn{RP}_{k}(\alpha \vert \sigma) =
\prod_{i = 1}^{2^k} \,  \opn{RP}_{0}(\alpha \vert \sigma_i)  \]
and
\[ \opn{RP}_{k'}(\alpha \vert \sigma) =
\prod_{i = 1}^{2^k} \,  \opn{RP}_{l}(\alpha \vert \sigma_i) . \]
If $i \in \opn{good}(k)$ then by Lemma \ref{lem:30} we know that 
\[ \Norm{ 
\opn{log}_G \bigl( \opn{RP}_{l}(\alpha \vert \sigma_i) \bigr) -
\opn{log}_G \bigl( \opn{RP}_{0}(\alpha \vert \sigma)_i \bigr) }
\leq c_2(\alpha) \cdot \opn{len}(\sigma)^3 \cdot (\smfrac{1}{2})^{3 k} . \]
On the other hand, $i \in \opn{bad}(k)$, then by Lemma \ref{lem:1} we know
that 
\[ \Norm{ 
\opn{log}_G \bigl( \opn{RP}_{l}(\alpha \vert \sigma_i) \bigr) -
\opn{log}_G \bigl( \opn{RP}_{0}(\alpha \vert \sigma)_i \bigr) }
\leq 
2 \cdot c_1(\alpha) \cdot \opn{len}(\sigma) \cdot (\smfrac{1}{2})^{k} . \]
Therefore by property (iv) of Theorem \ref{thm:6} we have
\[ \begin{aligned}
& \Norm{ 
\opn{log}_G \bigl( \opn{RP}_{k'}(\alpha \vert \sigma) \bigr) -
\opn{log}_G \bigl( \opn{RP}_{k}(\alpha \vert \sigma) \bigr) } \\
& \qquad = \Norm{ \opn{log}_G \Bigl( \boprod_{i = 1}^{2^k} \,
\opn{RP}_{l}(\alpha \vert \sigma_i) \Bigr) -
\opn{log}_G \bigl( \opn{RP}_{0}(\alpha \vert \sigma_i) \bigr) } \\
& \qquad \leq
c_0(G) \cdot \bigl( 
\abs{ \opn{bad}(k) } \cdot 2 \cdot c_1(\alpha) \cdot \opn{len}(\sigma) 
 \cdot (\smfrac{1}{2})^{k} \\
& \qquad \quad +
\abs{ \opn{good}(k) } \cdot
c_2(\alpha) \cdot \opn{len}(\sigma)^3 \cdot (\smfrac{1}{2})^{3 k}
\bigr) . 
\end{aligned} \]
Thus we may take
\[ c_3(\alpha, \sigma) := c_0(G) \cdot \bigl( 2 m \cdot c_1(\alpha) +
c_2(\alpha) \bigr) \, . \]
\end{proof}

\begin{thm} \label{thm:13}
Let $X$ be a polyhedron, let 
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$,
and let $\sigma : \mbf{I}^{1} \to X$ be a piecewise linear map. Then the limit
$\lim_{k \to \infty} \opn{RP}_{k}(\alpha \vert \sigma)$
exists.
\end{thm}

\begin{proof}
For any $k$ we have
\[ \begin{aligned}
& \opn{RP}_{k}(\alpha \vert \sigma) = 
\prod_{i = 1}^{2^k} \, \opn{RP}_{0}(\alpha \vert \sigma \circ \sigma^k_i) =
\prod_{i = 1}^{2^k} \, \opn{RP}_{0} \bigl( (\sigma \circ \sigma^k_i)^*(\alpha)
\vert \mbf{I}^1 \bigr) \\
& \qquad = 
\prod_{i = 1}^{2^k} \, \opn{RP}_{0} \bigl( \sigma^*(\alpha)
\vert \sigma^k_i \bigr) = 
\opn{RP}_{k} \bigl( \sigma^*(\alpha) \vert \sigma^0_1 \bigr) 
\end{aligned} \]
by definition. 
So after replacing $\alpha$ with $\sigma^*(\alpha)$, we can assume that 
$X = \mbf{I}^1$, and we have to prove that the limit 
$\lim_{k \to \infty} \opn{RP}_{k}(\alpha \vert \sigma^0_1)$ exists. 

Take $k$ large enough such that for each $i \in \{ 1, \ldots, 2^k \}$
the linear map $\sigma^k_i$ is $\alpha$-tiny. 
For any $k' \geq 0$ we have
\[ \opn{RP}_{k + k'}(\alpha \vert \sigma^0_1) = 
\prod_{i = 1}^{2^k}  \, \opn{RP}_{k'}(\alpha \vert \sigma^k_i) . \]
Thus it suffices to prove that for any $i$ the limit
$\lim_{k' \to \infty} \opn{RP}_{k'}(\alpha \vert \sigma^k_i)$
exists.

We have now reduced our problem to showing that for any $\alpha$-tiny
linear map $\sigma : \mbf{I}^1 \to X$ the limit
$\lim_{k \to \infty} \opn{RP}_{k}(\alpha \vert \sigma)$
exists. But this follows immediately from Lemma \ref{lem:31}.
\end{proof}

\begin{dfn} \label{dfn:28}
In the situation of Theorem \ref{thm:13}, the 
{\em multiplicative integral of $\alpha$ on $\sigma$} is 
\[ \opn{MI}(\alpha \vert \sigma) := 
\lim_{k \to \infty} \opn{RP}_{k}(\alpha \vert \sigma) \in G . \] 

If $X = \mbf{I}^{1}$ and $\sigma = \sigma^0_1$, the basic map, then we write
$\opn{MI}(\alpha \vert \mbf{I}^{1}) := \opn{MI}(\alpha \vert \sigma^0_1)$.
\end{dfn}

\begin{rem}
If the group $G$ is {\em abelian}, then 
$\opn{RP}_k(\alpha \vert \sigma)$
is the exponential of a Riemann sum, and therefore in the limit we get
\[ \opn{MI}(\alpha \vert \sigma) = 
\exp_G \bigl( \int_{\sigma} \alpha \bigr) . \]
\end{rem}

\begin{prop} \label{prop:5}
Let $\sigma : \mbf{I}^{1} \to X$ be a piecewise linear map.
\begin{enumerate}
\item If $\sigma$ is $\alpha$-tiny \tup{(}see Definition \tup{\ref{dfn:13})},
then 
$\opn{MI}(\alpha \vert \sigma) \in V_0(G)$, and 
\[ \Norm{ \opn{log}_G \bigl( \opn{MI}(\alpha \vert \sigma) \bigr) }
\leq c_1(\alpha) \cdot  \opn{len}(\sigma) \, . \]

\item If $\sigma$ is linear and $\alpha$-tiny, and if 
$\alpha|_{\sigma(\mbf{I}^{1})}$ is smooth, then for any $k \geq 0$ one has
\[ \Norm{ \opn{log}_G \bigl( \opn{MI}(\alpha \vert \sigma) \bigr) -
\opn{log}_G \bigl( \opn{RP}_0(\alpha \vert \sigma) \bigr) }
\leq c_2(\alpha) \cdot \opn{len}(\sigma)^3 \, . \]

\item For any $k \geq 0$ one has
\[ \opn{MI}(\alpha \vert \sigma)  =
\prod_{i = 1}^{2^k}  \, \opn{MI}(\alpha \vert \sigma \circ \sigma^k_i ) . \]
\end{enumerate}
\end{prop}

\begin{proof}
(1) By Lemma \ref{lem:1}, for sufficiently large $k$ we have
$\opn{RP}_k(\alpha \vert \sigma) \in V_0(G)$ and 
\[ \Norm{ \opn{log}_G \bigl( \opn{RP}_k(\alpha \vert \sigma) \bigr) } 
\leq c_1(\alpha) \cdot \opn{len}(\sigma) \leq 
\smfrac{1}{2} \cdot \epsilon_0(G) \ . \]
Let $B$ be the closed ball of radius $\smfrac{1}{2} \epsilon_0(G)$ in
$\g$, and let $Z := \opn{exp}_G(B)$, which is a compact subset of $G$.
Since for every $k$ one has
$\opn{RP}_k(\alpha \vert \sigma) \in Z$, it follows that in the limit
$\opn{MI}(\alpha \vert \sigma) \in Z \subset V_0(G)$.
The bound on 
$\Norm{ \opn{log}_G \bigl( \opn{MI}(\alpha \vert \sigma) \bigr) }$
is then obvious.

\medskip \noindent
(2) This is immediate from Lemma \ref{lem:30}.

\medskip \noindent
(3) For every $k' \geq 0$ we have by definition
\[ \opn{RP}_{k + k'}(\alpha \vert \sigma) = 
\prod_{i = 1}^{2^k}  \, \opn{RP}_{k'}(\alpha \vert \sigma \circ \sigma^k_i ) .
\]
Now pass to the limit $k' \to  \infty$.
\end{proof}


\subsection{Functoriality of the MI}
The next results are on the functoriality of the multiplicative integral with
respect to $G$ and $X$. 

\begin{prop}  \label{prop:6}
Let $\Phi : G \to H$ be a map of Lie groups, with induced Lie algebra map
$\phi := \opn{Lie}(\Phi) : \g \to \h$. Let $f : Y \to X$ be a piecewise linear
map between polyhedra, and let
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$.
Then for any piecewise linear map $\sigma : \mbf{I}^{1} \to Y$ one has
\[ \Phi \bigl( \opn{MI}(\alpha \vert f \circ \sigma) \bigr) = 
\opn{MI} \bigl( (f^* \otimes \phi)(\alpha) \vert \sigma \bigr) \]
in $H$.
\end{prop}

\begin{proof}
It suffices to consider $f$ and $\Phi$ separately; so we look at two cases.

\medskip \noindent
Case 1. $H = G$ and $\Phi$ is the identity map. Here for every $k \geq 0$
and $i \in \{ 1, \ldots, 2^k \}$ we have
\[ \opn{RP}_{0}(\alpha \vert f \circ \sigma \circ \sigma^k_i) 
\bigr) =
\opn{RP}_{0} \bigl( (f \circ \sigma)^*(\alpha) \vert \sigma^k_i \bigr) =
\opn{RP}_{0} \bigl( f^*(\alpha) \vert \sigma \circ \sigma^k_i \bigr) . \]
Hence
\[ \opn{RP}_{k}(\alpha \vert f \circ \sigma) =
\opn{RP}_{k} \bigl( (f \circ \sigma)^*(\alpha)  \vert \mbf{I}^{1} \bigr) =
\opn{RP}_{k} \bigl( f^*(\alpha) \vert \sigma \bigr) . \]
Going to the limit in $k$ we see that 
\[ \opn{MI}(\alpha \vert f \circ \sigma) =
\opn{MI} \bigl( (f \circ \sigma)^*(\alpha)  \vert \mbf{I}^{1} \bigr) =
\opn{MI} \bigl( f^*(\alpha) \vert \sigma \bigr) . \]


\medskip \noindent
Case 2. 
Here we assume that $Y = X$ and $f$ is the identity map. 
Since 
\[ \opn{MI}(\alpha \vert \sigma) = \opn{MI}(\sigma^*(\alpha) \vert \sigma^0_1)
\]
and 
\[ \opn{MI}(\phi(\alpha) \vert \sigma) = 
\opn{MI}((\sigma^* \otimes \phi)(\alpha) \vert \sigma^0_1) =
\opn{MI}(\phi(\sigma^*(\alpha)) \vert \sigma^0_1) , \]
we can replace $\sigma$ with $\sigma^0_1$ and $\alpha$ with
$\sigma^*(\alpha)$. Therefore we can assume that $\sigma$ is a linear map. 

Put a euclidean norm on $\h$ such that $\phi : \g \to \h$ has operator norm 
$\norm{\phi} \leq 1$. 
This implies that 
$\norm{ \phi(\alpha) }_{\mrm{Sob}} \leq \norm{\alpha}_{\mrm{Sob}}$.
So we can assume that
$\epsilon_1(\phi(\alpha)) \geq \epsilon_1(\alpha)$
and
$c_1(\phi(\alpha)) \leq c_1(\alpha)$
(cf.\ proof of Lemma \ref{lem:1}).

Take $k$ large enough such that 
$\sigma \circ \sigma^k_i$ is $\alpha$-tiny for every 
$i \in \{ 1, \ldots, 2^k \}$.
Then $\sigma \circ \sigma^k_i$ is also $\phi(\alpha)$-tiny.

By part (3) of Proposition \ref{prop:5} we have
\[ \opn{MI}(\alpha \vert \sigma )  =
\prod_{i = 1}^{2^k}  \, 
\opn{MI}(\alpha \vert \sigma \circ \sigma^k_i )  \]
and
\[ \opn{MI} \bigl( \phi(\alpha) \vert \sigma \bigr) =
\prod_{i = 1}^{2^k}  \, 
\opn{MI} \bigl( \phi(\alpha) \vert \sigma \circ \sigma^k_i \bigr) . \]
So it suffices to prove that 
\[ \Phi \bigl( \opn{MI}(\alpha \vert \sigma \circ \sigma^k_i) \bigr) = 
\opn{MI} \bigl( \phi(\alpha) \vert \sigma \circ \sigma^k_i \bigr) \]
for every $i$. 

By this reduction we can assume that 
$\sigma$ is $\alpha$-tiny and also $\phi(\alpha)$-tiny.
Take any $k \geq 0$, and for every $i \in \{ 1, \ldots, 2^k \}$ let 
$w_i := \sigma^k_i(\smfrac{1}{2}) \in \mbf{I}^{1}$. 
If $w_i$ is a smooth point of 
\[ \sigma^*(\alpha) \in \Omega^1_{\mrm{pws}}(\mbf{I}^{1}) \otimes 
\g , \]
then it is also a smooth point of 
\[ (\sigma^* \otimes \phi)(\alpha)  
\in \Omega^1_{\mrm{pws}}(\mbf{I}^{1}) \otimes \h .  \]
In this case we have
\begin{equation} \label{eqn:72}
\Phi \bigl( \opn{RP}_{0}(\alpha \vert \sigma \circ \sigma^k_i) 
\bigr) =
\opn{RP}_0 \bigl( \phi(\alpha) \vert \sigma \circ \sigma^k_i \bigr) .
\end{equation}

In case $w_i$ is a singular point of
$(\sigma^* \otimes \phi)(\alpha)$,
then it is also a singular point of 
$\sigma^*(\alpha)$.
Hence (\ref{eqn:72}) also holds (both sides are $1$). 

The only problem is when $w_i$ is a smooth point of
$(\sigma^* \otimes \phi)(\alpha)$
but a singular point of $\sigma^*(\alpha)$.

Now we use the estimate provided by Lemma \ref{lem:1}
(noting that $\phi \circ \log_G = \log_H \circ\, \Phi$):
\[ \begin{aligned}
& \Norm{ \log_H \bigl( \Phi \bigl( \opn{RP}_{0} 
(\alpha \vert \sigma \circ \sigma^k_i ) \bigl) \bigr) - 
\log_H \bigl( \opn{RP}_{0} \bigl( \phi(\alpha) \vert 
\sigma \circ \sigma^k_i \bigr) \bigr) } \\
& \qquad 
\leq 2 \cdot c_1(\alpha) \cdot \opn{len}(\sigma) \cdot (\smfrac{1}{2})^k \, .
\end{aligned} \]

Let $m$ be the number of singular points of $\sigma^*(\alpha)$. 
Then using property (iv) of Theorem \ref{thm:6} we get
\[ \begin{aligned}
& \Norm{ \log_H \bigl( \Phi \bigl( \opn{RP}_{k} 
(\alpha \vert \sigma) \bigl) \bigr) - 
\log_H \bigl( \opn{RP}_{k} \bigl( \phi(\alpha) \vert 
\sigma \bigr) \bigr) } \\
& \qquad 
\leq 2 m \cdot c_1(\alpha) \cdot \opn{len}(\sigma) \cdot (\smfrac{1}{2})^k \, .
\end{aligned} \]
Since $m$ is independent of $k$, in the limit $k \to \infty$ we get
\[ \Phi \bigl( \opn{MI} (\alpha \vert \sigma) \bigl) = 
\opn{MI} \bigl( \phi(\alpha) \vert \sigma \bigr) . \]
\end{proof}

A particular case of the above is when we are given a representation of $G$,
namely a map of Lie groups 
$\Phi : G \to \mrm{GL}_m(\R)$ for some $m$. 
The Lie algebra of $\mrm{GL}_m(\R)$ is
$\mfrak{gl}_m(\R) = \mrm{M}_m(\R)$, the algebra of $m \times m$ matrices.
For a matrix $a \in \mrm{M}_m(\R)$ let us denote by $\norm{a}$ its operator
norm, as linear operator $a : \R^m \to \R^m$, 
where $\R^m$ has the standard euclidean inner product.

\begin{prop} \label{prop:4}
Let $\Phi : G \to \mrm{GL}_m(\R)$ be a representation, and let
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$.
Then there is a constant $c_4(\alpha, \Phi) \geq 0$ such that the following
holds:
\begin{enumerate}
\item[($*$)] Given a piecewise linear map
$\sigma : \mbf{I}^{1} \to X$, let 
$g := \opn{MI}(\alpha \vert \sigma) \in G$.
Then
\[ \norm{ \Phi(g) } \leq \exp \bigl( c_4(\alpha, \Phi) \cdot
\opn{len}(\sigma)
\bigr) \, , \]
where $\exp$ the usual real exponential function.
\end{enumerate}
\end{prop}

\begin{proof}
Let's write $H := \mrm{GL}_m(\R)$,
$\h := \mfrak{gl}_m(\R)$ and
$\alpha' := \opn{Lie}(\Phi)(\alpha) \in$ \lb 
$\Omega^1_{\mrm{pws}}(X) \otimes \h$. 
We use the operator norm on $\h$ to determine the constants 
$\epsilon_1(\alpha')$ and $c_1(\alpha')$ in
Definition \ref{dfn:13}.

Take $k$ large enough so that $\sigma \circ \sigma^k_i$ is $\alpha'$-tiny
for every $i \in \{ 1, \ldots, 2^k \}$. 
Let $d := \opn{len}(\sigma)$ and $d_i := \opn{len}(\sigma \circ \sigma_i)$,
so $d = \sum_{i = 1}^{2^k}  \, d_i$.
Define $h_i := \opn{MI}(\alpha' \vert \sigma \circ \sigma^k_i) \in H$. 
Then $h_i \in V_0(H)$, and we can define 
$\gamma_i := \log_{H} (h_i) \in \h$.

Since the matrix $\gamma_i$ satisfies
\[ \norm{ \gamma_i } \leq c_1(\alpha') \cdot d_i , \]
it follows that its exponential $h_i$ satisfies
\[ \norm{ h_i } \leq \exp \bigl( c_1(\alpha') \cdot d_i \bigr) \, . \]
Now 
\[ \Phi(g) = \opn{MI}(\alpha' \vert \sigma) = \prod_{i = 1}^{2^k}  \, h_i , \]
so we obtain
\[ \norm{\Phi(g)} \leq \exp \bigl( c_1(\alpha') \cdot d \bigr) \, . \]
Therefore we can take 
$c_4(\alpha, \Phi) := c_1(\alpha')$.
\end{proof}


\subsection{Strings}
\begin{dfn} \label{dfn:3}
Let $X$ be a polyhedron. A {\em string} in $X$ is a sequence 
$\sigma = (\sigma_1, \ldots, \sigma_m)$ of piecewise
linear maps $\sigma_i : \mbf{I}^1 \to X$, such that 
$\sigma_i(v_1) = \sigma_{i+1}(v_0)$ for all $i$. 
The maps $\sigma_i : \mbf{I}^1 \to X$ are called the {\em pieces} of $\sigma$.  
We write $\sigma(v_0) := \sigma_1(v_0)$ and
$\sigma(v_1) := \sigma_m(v_1)$, and call these points the {\em initial} and
{\em terminal} points of $\sigma$, respectively. 
The {\em length} of $\sigma$ is
$\opn{len}(\sigma) := \sum_{i = 1}^m \opn{len}(\sigma_i)$.
\end{dfn}

Suppose $\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$.
We say that $\sigma$ is an {\em $\alpha$-tiny string} if
$\opn{len}(\sigma) < \epsilon_1(\alpha)$; cf.\ Definition \ref{dfn:13}.

Here are a few operations on strings. 
Suppose $\sigma = (\sigma_1, \ldots, \sigma_m)$ and
$\tau = (\tau_1, \ldots, \tau_l)$ are two strings in
$X$, with $\tau(v_0) = \sigma(v_1)$. 
Then we define the {\em concatenated string}
\begin{equation} \label{eqn12}
\sigma * \tau := (\sigma_1, \ldots, \sigma_m, \tau_1, \ldots, \tau_l) .
\end{equation}
See Figure \ref{fig:41} for an illustration.

\begin{figure}
\includegraphics[scale=0.27]{fig41.jpg}
\caption{The strings $\sigma = (\sigma_1, \sigma_2, \sigma_3)$,
$\tau = (\tau_1, \tau_2)$ and
$\sigma * \tau$ in the polyhedron $X$.} 
\label{fig:41}
\end{figure}

The {\em flip} of $\mbf{I}^{1}$ is the linear bijection
$\opn{flip} : \mbf{I}^{1} \to \mbf{I}^{1}$
defined on vertices by
\[ \opn{flip}(v_0, v_1) := (v_1, v_0) . \]
Given a piecewise linear map $\sigma : \mbf{I}^{1} \to X$ we let
\begin{equation}
\sigma^{-1} := \sigma \circ  \opn{flip} : \mbf{I}^{1} \to X .
\end{equation}
For a string $\sigma = (\sigma_1, \ldots, \sigma_m)$ in $X$ we define the
{\em inverse string}
\begin{equation} \label{eqn13}
\sigma^{-1} := (\sigma_m^{-1}, \ldots, \sigma_1^{-1}) .
\end{equation}

The empty string is the unique string of length $0$, and we denote it by
$\emptyset$. For any string $\sigma$ we let
$\sigma * \emptyset := \sigma$ and 
$\emptyset * \sigma := \sigma$.

Let $f : X \to Y$ be a piecewise linear map between polyhedra, and let
$\sigma = (\sigma_1, \ldots, \sigma_m)$ be a string in $X$.
We define the string $f \circ \sigma$ in
$Y$ to be
\begin{equation} \label{eqn14}
f \circ \sigma := (f \circ \sigma_1, \ldots, f \circ \sigma_m) .
\end{equation}

\begin{rem}
The reason for working with strings (rather than with paths, as is the custom
in algebraic topology) is that composition of strings, as defined above, is
associative, whereas composition of paths is only associative up to homotopy.
\end{rem}

It will be convenient to integrate along a string. 
As before $G$ is a Lie group with Lie algebra $\g$.

\begin{dfn} \label{dfn:10}
Suppose $\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \mfrak{g}$
and 
$\sigma = (\sigma_1, \ldots, \sigma_m)$
is a string in $X$. The multiplicative integral 
\index{Multiplicative integral on strings}
$\opn{MI}(\alpha \vert \sigma)$ of $\alpha$ on $\sigma$ is 
\[ \opn{MI}(\alpha \vert \sigma) :=
\prod_{i=1}^m\ \opn{MI}(\alpha \vert \sigma_i) \in G . \]
\end{dfn}

\begin{prop} \label{prop:1}
Let 
$\alpha \in \Omega_{\mrm{pws}}^1(X) \otimes \mfrak{g}$.
\begin{enumerate}
\item Given strings $\sigma$ and $\tau$ in $X$ such that
$\tau(v_0) = \sigma(v_1)$, one has
\[ \opn{MI}(\alpha \vert \sigma * \tau) = 
\opn{MI}(\alpha \vert \sigma) \cdot \opn{MI}(\alpha \vert \tau) . \]

\item Given a string $\sigma$ in $X$ , one has
\[ \opn{MI}(\alpha \vert \sigma^{-1}) = 
\opn{MI}(\alpha \vert \sigma)^{-1} . \]

\item If $\sigma$ is an $\alpha$-tiny string in $X$ 
\tup{(}i.e\ 
$\opn{len}(\sigma) < \epsilon_1(\alpha)$\tup{)}, then 
$\opn{MI}(\alpha \vert \sigma) \in V_0(G)$, and 
\[ \Norm{ \opn{log}_G \bigl( \opn{MI}(\alpha \vert \sigma) \bigr) }
\leq c_1(\alpha) \cdot \opn{len}(\sigma) \, . \]
\end{enumerate}
\end{prop}

\begin{proof}
(1) This is trivial.

\medskip \noindent
(2) By part (1) it suffices to consider a piecewise linear map 
$\sigma : \mbf{I}^{1} \to X$.
Since the flip reverses orientation on $\mbf{I}^1$, it follows that 
\[ \opn{RP}_0(\alpha \vert \sigma^{-1}) = 
\opn{RP}_0(\alpha \vert \sigma)^{-1} . \]
{}From this, and the symmetry of the binary tessellations, it follows that for
every $k \geq 0$ one has
\[ \opn{RP}_{k}(\alpha \vert \sigma^{-1}) = 
\opn{RP}_{k}(\alpha \vert \sigma)^{-1} . \]
In the limit we get
$\opn{MI}(\alpha \vert \sigma^{-1}) = 
\opn{MI}(\alpha \vert \sigma)^{-1}$.

\medskip \noindent
(3) Say $\sigma  = (\sigma_1, \ldots, \sigma_m)$.
Take $k$ large enough so that $2^k \geq m$. Let
$\sigma' : \mbf{I}^1 \to X$ be the unique piecewise linear map satisfying
$\sigma' \circ \sigma^k_i = \sigma_i$ for $i \leq m$, and
$\sigma' \circ \sigma^k_i$ is the constant map $\sigma(v_1)$ for $i > m$.
Note that $\opn{len}(\sigma') = \opn{len}(\sigma)$.
By Definition \ref{dfn:10} and Proposition \ref{prop:5}(3) we have
$\opn{MI}(\alpha \vert \sigma') = 
\opn{MI}(\alpha \vert \sigma)$.
Now use Proposition \ref{prop:5}(1).
\end{proof}

\begin{prop} \label{prop:12}
Let $\Phi : G \to H$ be a map of Lie groups, let $f : Y \to X$ be a piecewise
linear map between polyhedra, and let
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$.
Then for any string $\sigma$ in $Y$ one has
\[ \Phi \bigl( \opn{MI}(\alpha \vert f \circ \sigma) \bigr) = 
\opn{MI} \bigl( (f^* \otimes \opn{Lie}(\Phi))(\alpha) \vert \sigma \bigr) 
\in H . \]
\end{prop}

\begin{proof}
This is an immediate consequence of Proposition \ref{prop:1}(1) and \lb
Proposition \ref{prop:6}.
\end{proof}

\begin{prop} \label{prop:13}
Let $\Phi : G \to \opn{GL}_m(\R)$ be a representation, and let
$\alpha \in \Omega_{\mrm{pws}}^1(X) \otimes \mfrak{g}$.
Given a string $\sigma$ in $X$ let $g := \opn{MI}(\alpha \vert \sigma)$.
Then the norm of the operator $\Phi(g)$ on $\R^m$ satisfies
\[ \norm{ \Phi(g) } \leq  \exp \bigl( c_4(\alpha, \Phi) \cdot
\opn{len}(\sigma) \bigr) \, , \]
where $c_4(\alpha, \Phi)$ is the constant from Proposition \tup{\ref{prop:4}}.
\end{prop}

\begin{proof}
By part (1) of Proposition \ref{prop:1} 
the left side of this inequality is multiplicative with respect
to the operation $*$. And clearly the right side is also multiplicative with
respect to $*$. So it suffices to consider a piecewise linear map 
$\sigma : \mbf{I}^{1} \to X$. Now we can use Proposition \ref{prop:4}.
\end{proof}

For a string $\sigma = (\sigma_1, \ldots, \sigma_m)$ 
and a form 
$\alpha \in \Omega_{\mrm{pws}}^1(X) \otimes \mfrak{g}$
we write
\[ \int_{\sigma} \alpha := \sum_{i = 1}^m \int_{\sigma_i} \alpha \in \g , \]
where 
\[ \int_{\sigma_i} \alpha = \int_{\mbf{I}^1} \sigma_i^*(\alpha) \] 
is the usual integral of this $\g$-valued piecewise smooth differential form. 

\begin{prop} \label{prop:16}
Let $\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$, and let $\sigma$ be an
$\alpha$-tiny string in $X$. Then 
\[ \Norm{ \log_G \bigl( \opn{MI}(\alpha \vert \sigma) \bigr) - 
\int_{\sigma} \alpha } \leq 
c_0(G) \cdot c_1(\alpha)^2 \cdot \opn{len}(\sigma)^2 \ . \]
\end{prop}

What this result says, is that in the tiny scale the nonabelian 
integral is very close to the abelian integral.

\begin{proof}
Step 1. 
We begin the proof with a reduction to the case $m = 1$, and
$\sigma = \sigma_1$ is a single linear map $\mbf{I}^1 \to X$. 
First we append a few empty strings at the
end of $\sigma$, so that the number of linear pieces becomes 
$m = 2^k$ for some $k$. This does not change $\opn{len}(\sigma)$ nor
$\opn{MI}(\alpha \vert \sigma)$.
Let $Z$ be an oriented $1$-dimensional polyhedron (a line segment) of length 
$\opn{len}(\sigma)$, partitioned into segments
$Z_1, \ldots, Z_m$, with $\opn{len}(Z_i) = \opn{len}(\sigma_i)$.
Let $\sigma' : \mbf{I}^1 \to Z$ be the unique oriented linear bijection.
There is a unique piecewise linear map $f : Z \to X$, such that 
$\sigma_i = f \circ \sigma' \circ \sigma^k_i$ as piecewise linear maps
$\mbf{I}^1 \to X$ for every $i$.
Let $\alpha' := f^*(\alpha) \in \Omega^1_{\mrm{pws}}(Z) \otimes \g$.
According to Propositions \ref{prop:5}(3), \ref{dfn:10} and \ref{prop:12} we
have
\[ \opn{MI}(\alpha \vert \sigma) = \opn{MI}(\alpha' \vert \sigma') . \]
And clearly 
\[ \int_{\sigma} \alpha = \int_{\sigma'} \alpha' . \]
Because the piecewise linear map $f : Z \to X$ is a linear metric
embedding on each of its linear pieces, it follows that 
$\norm{\alpha'}_{\mrm{Sob}} \leq \norm{\alpha}_{\mrm{Sob}}$; and hence we can
choose
$\epsilon_1(\alpha') \geq \epsilon_1(\alpha)$ and 
$c_1(\alpha') \leq c_1(\alpha)$.

Note that 
\[ \opn{len}(\sigma') = \opn{len}(Z) = \opn{len}(\sigma) < \epsilon_1(\alpha)
\, . \]
So we can replace $X$ with $Z$, $\sigma$ with $\sigma'$ and $\alpha$ with
$\alpha'$. Doing so, we can now assume that $m = 1$ and $\sigma$ is a single
linear map.

\medskip \noindent
Step 2. Here we assume that $\sigma$ is an $\alpha$-tiny linear map, and we let
$\epsilon := \opn{len}(\sigma)$.
Take any $k \geq 0$. We know that
\[ \opn{RP}_{k}(\alpha \vert \sigma) = 
\prod_{i = 1}^{2^k} \,  \opn{RP}_{0}(\alpha \vert \sigma \circ \sigma^k_i) . \]
Also (by Lemma \ref{lem:1}) we have
\[ \opn{RP}_{k}(\alpha \vert \sigma), 
\opn{RP}_{0}(\alpha \vert \sigma \circ \sigma^k_i) \in V_0(G) . \]
For any $i$ let
\[ \lambda_i := \log_G \bigl( \opn{RP}_{0}(\alpha \vert \sigma \circ \sigma^k_i)
\bigr) \in \g , \]
so 
\[ \opn{RP}_{k}(\alpha \vert \sigma) = 
\prod_{i = 1}^{2^k} \, \exp_G(\lambda_i) . \]
Let us write
\[ \opn{RS}_k(\alpha \vert \sigma) := \sum_{i = 1}^{2^k} \,  \lambda_i . \]
This is a Riemann sum for the usual integral.

By Lemma \ref{lem:1} we have
\[ \norm{ \lambda_i } \leq 
c_1(\alpha) \cdot (\smfrac{1}{2})^k \cdot \epsilon  \]
for every $i$. Using property (ii) of Theorem \ref{thm:6} we see that
\[ \begin{aligned}
& \Norm{ 
\log_G \bigl( \opn{RP}_{k}(\alpha \vert \sigma) \bigr) -
\opn{RS}_{k}(\alpha \vert \sigma) } \\
& \qquad \leq 
c_0(G) \cdot \bigl( \sum\nolimits_{i = 1}^{2^k} \,  \norm{\lambda_i} \bigr)^2 
\leq c_0(G) \cdot c_1(\alpha)^2 \cdot \epsilon^2 \ . 
\end{aligned} \]

In the limit $k \to \infty$ we have
\[ \lim_{k \to \infty} \opn{RS}_{k}(\alpha \vert \sigma) = 
\int_{\sigma} \alpha \]
and 
\[ \lim_{k \to \infty} \opn{RP}_{k}(\alpha \vert \sigma) = 
\opn{MI}_{}(\alpha \vert \sigma) , \]
so the proof is done.
\end{proof}

\begin{cor} \label{cor:7}
Let $\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$, and let $\sigma$ be an
$\alpha$-tiny closed string in $X$ which bounds a polygon $Z$. Then
\[ \Norm{ \log_G \bigl( \opn{MI}(\alpha \vert \sigma) \bigr) } \leq 
c_0(G) \cdot c_1(\alpha)^2 \cdot \opn{len}(\sigma)^2 +
\opn{area}(Z) \cdot \norm{\alpha}_{\mrm{Sob}} \, . \]
\end{cor}

\begin{proof}
Choose an orientation on $Z$.
By the abelian Stokes Theorem (Theorem \ref{thm:15}) we have
\[ \Norm{ \int_{\sigma} \alpha } = \Norm{ \int_Z \d(\alpha) }
\leq \opn{area}(Z) \cdot \norm{\alpha}_{\mrm{Sob}} \, . \]
Now combine this estimate with the Proposition above.
\end{proof}

\begin{prop} \label{prop:21}
Let $\Phi : G \to \opn{GL}_m(\R)$ be a representation,
and let $\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$.
Then there are constants $\epsilon_5(\alpha, \Phi)$ and
$c_5(\alpha, \Phi)$ such that 
\[ 0 < \epsilon_5(\alpha, \Phi) \leq 1 \quad \text{and} \quad
c_5(\alpha, \Phi) \geq 1 \, , \]
and such that conditions \tup{(i)-(iii)} below  hold for every 
string $\sigma$ in $X$ satisfying 
$\opn{len}(\sigma) < \epsilon_5(\alpha, \Phi)$.
Let us write
\[ \alpha' := \opn{Lie}(\Phi)(\alpha) \in 
\Omega^1_{\mrm{pws}}(X) \otimes \mfrak{gl}_n(\R) , \]
and
\[ g' := \opn{MI}(\alpha' \vert \sigma) = \Phi 
\bigl( \opn{MI}(\alpha \vert \sigma) \bigr) \in \opn{GL}_m(\R) . \]
Let $\bsym{1}$ be the identity operator on $\R^m$, and let $\norm{-}$ denote
the operator norm on $\R^m$. 
The conditions are:
\begin{itemize}
\rmitem{i} 
\[ \norm{ g' - \bsym{1} } \leq  c_5(\alpha, \Phi) \cdot \opn{len}(\sigma) \, .
\]
\rmitem{ii}
\[ \Norm{ g' - \bigl( \bsym{1} + \int_{\sigma} \alpha' \bigr) } 
\leq c_5(\alpha, \Phi) \cdot \opn{len}(\sigma)^2 \, . \]
\rmitem{iii} 
Assume $\alpha'$ is smooth. Let $x_0$ be the initial point of $\sigma$, and let
$\alpha'(x_0)$ be the constant form defined in Definition 
\tup{\ref{dfn:26}}. Then
\[ \Norm{ g' - \bigl( \bsym{1} + \int_{\sigma} \alpha'(x_0) \bigr) } 
\leq c_5(\alpha, \Phi) \cdot \opn{len}(\sigma)^2 \, . \]
\end{itemize}
\end{prop}

\begin{proof}
Let us write $H := \opn{GL}_m(\R)$ and
$\h := \mfrak{gl}_n(\R)$. 
Define $\epsilon_5(\alpha, \Phi) := \epsilon_1(\alpha')$, in the sense of
Definition \ref{dfn:13}, and let
$d := c_1(\alpha') \cdot \epsilon_1(\alpha')$.

By reasons of convergence of analytic functions on compact domains,
there is a constant $c$ such that 
for every matrix $\lambda \in \h$ with 
$\norm{\lambda} \leq d$ the inequalities
\begin{equation} \label{eqn:144}
\Norm{ \exp_H(\lambda) - \bsym{1} } \leq c \cdot \norm{\lambda}
\end{equation}
and
\begin{equation} \label{eqn:145}
\Norm{ \exp_H(\lambda) - (\bsym{1} + \lambda) } \leq c \cdot \norm{\lambda}^2 
\end{equation}
hold. 

Take a string $\sigma$ with 
$\epsilon := \opn{len}(\sigma) < \epsilon_5(\alpha, \Phi)$.
By Proposition \ref{prop:1}(3) we have
$g' \in V_0(H)$ and 
\[ \norm{\lambda} \leq c_1(\alpha') \cdot \epsilon \leq  d \, , \]
for the elements
$g' := \opn{MI}(\alpha' \vert \sigma)$ and
$\lambda := \log_H(g') \in \h$.
Inequality (\ref{eqn:144}) gives
\begin{equation} \label{eqn:146}
\norm{ g' - \bsym{1} } \leq c \cdot  c_1(\alpha') \cdot \epsilon 
\, . 
\end{equation}
Next,  using Proposition \ref{prop:16} and
inequality (\ref{eqn:145}) we have 
\begin{equation} \label{eqn:147}
\begin{aligned}
& \Norm{ g' - \bigl( \bsym{1} + \int_{\sigma} \alpha' \bigr) } \leq 
\Norm{ g' - (\bsym{1} + \lambda) } +
\norm{ \lambda - \int_{\sigma} \alpha' } \\
& \qquad \leq c \cdot c_1(\alpha')^2  \cdot \epsilon^2
+  c_1(\alpha')^2 \cdot \epsilon^2 \, . 
\end{aligned}
\end{equation}

Finally, assume that $\alpha'$ is smooth. By Taylor expansion of the
coefficients of $\alpha'$ (cf.\ (\ref{eqn:67})) we have the estimate
\[ \Norm{ \alpha'(x) - \alpha'(x_0) } \leq \norm{ \alpha' }_{\mrm{Sob}} \cdot 
\epsilon \]
for every point $x$ in the image of the string $\sigma$. 
Therefore
\begin{equation} \label{eqn:148}
\Norm{ \int_{\sigma} \alpha' - \int_{\sigma} \alpha'(x_0) } \leq
\norm{ \alpha' }_{\mrm{Sob}} \cdot \epsilon^2 \, .
\end{equation}

{}From the inequalities (\ref{eqn:146}), (\ref{eqn:147}) and (\ref{eqn:148})
we can now easily extract a constant $c_5(\alpha, \Phi)$ for which all three
conditions hold.
\end{proof}

 




\cleardoublepage
