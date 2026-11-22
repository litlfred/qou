---
doc_id: arxiv-1007.1250v4
doc_title: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES"
section_id: sec-006-6-stokes-theorem-in-dimension-two
section_title: "Stokes Theorem in Dimension Two"
section_number: 6
pages: 83-91
source_pdf: 1007.1250v4.pdf
source_sha256: 541ba4fb3068de8b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.974
doc_brief: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES — We construct a 2-dimensional twisted nonabelian multiplicative integral."
---
\label{sec:stokes2}

The purpose of this section is to prove Theorem \ref{thm:1}.
When $H = G$ (see Example \ref{exa:3}) this is just a fancy
version of Schlesinger's theorem. 

Let  $(X, x_0)$ be a pointed polyhedron.
Recall the notions of Lie quasi crossed module with additive feedback
\begin{equation}
\mbf{C} / X = (G, H, \Psi, \Phi_0, \Phi_X)
\end{equation}
over $(X, x_0)$, connection-curvature pair $(\alpha, \beta)$, and 
multiplicative integral \lb
$\opn{MI}(\alpha, \beta \vert \sigma, \tau)$;
see Definitions \ref{dfn:6}, \ref{dfn:19} and \ref{dfn:16}
respectively.


\subsection{Some Estimates}
In this subsection we assume that $(X, x_0) = (\mbf{I}^2, v_0)$.
We fix a Lie quasi crossed module with additive feedback
$\mbf{C} / {X}$ over $(\mbf{I}^2, v_0)$, in which $G = H$, as in Example
\ref{exa:2}. We also fix a connection-curvature pair $(\alpha, \beta)$ for
$\mbf{C} / {X}$. Note that the equality
\begin{equation} \label{eqn:75}
\beta = \d (\alpha) + \smfrac{1}{2} [\alpha, \alpha] 
\end{equation}
holds in $\Omega^2_{\mrm{pws}}(\mbf{I}^2)  \otimes \mfrak{g}$.
As in Section \ref{sec:pws} we choose a euclidean norm $\norm{-}_{\g}$
on the vector space $\g$; an open neighborhood $V_0(G)$ of $1$
in $G$ on which $\log_G$ is well-defined; a convergence radius
$\epsilon_0(G)$; and a commutativity constant $c_0(G)$.

In Proposition \ref{prop:22} we established certain constants 
$c_{2'}(\alpha, \beta)$ and \lb $\epsilon_{2'}(\alpha, \beta)$.

\begin{lem} \label{lem:9}
There are constants $c_3(\alpha, \beta)$ and
$\epsilon_3(\alpha, \beta)$ with these properties:
\begin{enumerate}
\item $c_3(\alpha, \beta) \geq c_{2'}(\alpha, \beta)$ and
$0 < \epsilon_3(\alpha, \beta) \leq \epsilon_{2'}(\alpha, \beta)$.
\item Suppose $(\sigma, \tau)$ is a square kite in $(\mbf{I}^2, v_0)$
such that 
$\opn{side}(\tau) < \epsilon_3(\alpha, \beta)$ and
$\opn{len}(\sigma) \leq 5$. Then
\[ \opn{MI} (\alpha, \beta \vert \sigma, \tau) , \,
\opn{MI} (\alpha \vert \partial(\sigma, \tau)) \in V_0(G)  \]
and
\[ \Norm{ \log_G \bigl( \opn{MI} (\alpha, \beta \vert \sigma, \tau) \bigr) }
\, , \, 
\Norm{ \log_G \bigl( \opn{MI} (\alpha \vert \partial(\sigma, \tau)) \bigr) }
\leq c_3(\alpha, \beta) \cdot \opn{side}(\tau)^2  \, . \]
\end{enumerate}
\end{lem}

\begin{proof}
For $\opn{MI} (\alpha, \beta \vert \sigma, \tau)$ we can use the estimate from
Proposition \ref{prop:8}.

For the boundary we have to do some work. Let's write
$\epsilon := \opn{side}(\tau)$, and suppose that 
$\epsilon < \smfrac{1}{4} \epsilon_1(\alpha)$, where 
$\epsilon_1(\alpha)$ is the constant from Definition \ref{dfn:13}.
Consider the closed string $\partial \tau$ of length $4 \epsilon$. 
Write $g_1 := \opn{MI}(\alpha \vert \partial \tau) \in G$. 
According to Proposition \ref{prop:16} we know that 
$g_1 \in V_0(G)$, and 
\[ \Norm{ \log_G (g_1) - \int_{\partial \tau} \alpha } \leq 
c_0(G) \cdot c_1(\alpha)^2 \cdot (4 \epsilon)^2 \ . \]
By the abelian Stokes Theorem (Theorem \ref{thm:15}) we have
\[ \int_{\partial \tau} \alpha =  \int_{\tau} \d(\alpha) . \]
Now
\[ \Norm{ \int_{\tau} \d(\alpha) } \leq 
\opn{area}(\tau) \cdot \norm{\alpha}_{\mrm{Sob}} 
= \epsilon^2 \cdot  \norm{\alpha}_{\mrm{Sob}} \ . \]
We conclude that
\[ \norm{ \log_G (g_1) } \leq 
\bigl( c_0(G) \cdot c_1(\alpha)^2 \cdot 16 + \norm{\alpha}_{\mrm{Sob}} \bigr)
\cdot \epsilon^2 \ . \]

Next let 
$g_2 := \opn{MI}(\alpha \vert \sigma) \in G$.
Consider the representation 
$\opn{Ad}_{\g} : G \to \opn{GL}(\g)$. 
By Proposition \ref{prop:13} the norm of the operator 
$\opn{Ad}_{\g}(g_2)$ satisfies 
\[ \norm{ \opn{Ad}_{\g}(g_2) } \leq 
\exp( c_4(\alpha, \opn{Ad}_{\g}) \cdot 5) \ . \]

Finally we look at 
$g := \opn{MI} (\alpha \vert \partial(\sigma, \tau))$. 
By definition 
\[ g = g_2 \cdot g_1 \cdot g_2^{-1} = \opn{Ad}_{G}(g_2)(g_1) . \]
The logarithm is 
\[ \log_G(g) = \opn{Ad}_{\g}(g_2)(\log_G(g_1)) . \]
By combining the estimates above we get
\[ \norm{ \log_G(g) } \leq 
\exp( c_4(\alpha, \opn{Ad}_{\g}) \cdot 5) \cdot 
\bigl( c_0(G) \cdot c_1(\alpha)^2 \cdot 16 + \norm{\alpha}_{\mrm{Sob}} \bigr)
\cdot \epsilon^2 \ . \]
We see that we can take the following constants:
\[ \epsilon_3(\alpha, \beta) := \min \bigl( \epsilon_2(\alpha, \beta), 
\smfrac{1}{4} \epsilon_1(\alpha) \bigr) \] 
and 
\[ \begin{aligned}
& c_4(\alpha, \beta) := \\
& \quad \max \bigl( c_2(\alpha, \beta),
\exp( c_4(\alpha, \opn{Ad}_{\g}) \cdot 5) \cdot 
( c_0(G) \cdot c_1(\alpha)^2 \cdot 16 + \norm{\alpha}_{\mrm{Sob}} )
\bigr) \ . 
\end{aligned} \]
\end{proof}

\begin{lem} \label{lem:10}
There are constants $c_4(\alpha, \beta)$ and
$\epsilon_4(\alpha, \beta)$ with these properties:
\begin{enumerate}
\item $c_3(\alpha, \beta) \leq c_4(\alpha, \beta)$ and
$0 < \epsilon_4(\alpha, \beta) \leq \epsilon_3(\alpha, \beta)$.
\item Suppose $(\sigma, \tau)$ is a square kite in $(\mbf{I}^2, v_0)$
such that 
$\opn{side}(\tau) < \epsilon_4(\alpha, \beta)$, \linebreak
$\opn{len}(\sigma) \leq 5$, and $\alpha|_{\tau(\mbf{I}^2)}$ is smooth.
Then
\[ \Norm{ \log_G \bigl( \opn{MI} (\alpha, \beta \vert \sigma, \tau) \bigr) -
\log_G \bigl( \opn{MI} (\alpha \vert \partial(\sigma, \tau)) \bigr) }
\leq c_4(\alpha, \beta) \cdot \opn{side}(\tau)^3  \, . \]
\end{enumerate}
\end{lem}

\begin{proof}
Let $\epsilon := \opn{side}(\tau)$, $Z := \tau(\mbf{I}^{2})$, and
$z := \tau(\smfrac{1}{2}, \smfrac{1}{2})$, which is the midpoint of the square
$Z$. Denote by 
$(\rho_1, \ldots, \rho_4)$ the closed string $\partial \tau$. For any 
$i \in \{ 1, \ldots, 4 \}$ let
$z_i$ be the midpoint of the edge $\rho_i(\mbf{I}^{1})$. 
See Figure \ref{fig:26} for an illustration.
Let $(s_1, s_2)$ be the positively oriented orthonormal linear
coordinate system on $Z$, such that 
\[ \tau^*(s_i) = \epsilon \cdot (t_i - \smfrac{1}{2}) . \]
So in particular $s_i(z) = 0$. 

\begin{figure}
\includegraphics[scale=0.28]{fig26.jpg}
\caption{Computing $\opn{RP}_{0}(\alpha \vert \partial \tau)$
for a tiny square kite $(\sigma, \tau)$ in  $(\mbf{I}^{2}, v_0)$.} 
\label{fig:26}
\end{figure}

Since $\alpha|_Z$ is smooth, there are functions
$\til{\alpha}_1, \til{\alpha}_2 \in \mcal{O}(Z) \otimes \g$ such that
\[ \alpha|_{Z} = \til{\alpha}_1 \cdot \d s_1 + \til{\alpha}_2 \cdot \d s_2 . \]
The Taylor expansion of $\til{\alpha}_j$ around $z$ to second order looks like
this:
\begin{equation} \label{eqn:241}
\til{\alpha}_j(x) = \til{\alpha}_j(z) + 
\sum_{1 \leq k \leq 2} 
(\smfrac{\partial}{\partial s_k} \til{\alpha}_j)(z) \cdot s_k(x) +
\sum_{1 \leq k, l \leq 2} 
g_{j, k, l}(x) \cdot s_k(x) \cdot s_l(x) 
\end{equation}
for $x \in Z$. Here 
$g_{j, k, l} : Z \to \g$ are continuous functions satisfying
\begin{equation} \label{eqn:242}
\norm{ g_{j, k, l} } \leq \norm{\alpha}_{\mrm{Sob}} \, . 
\end{equation}

We define elements $\lambda_i \in \g$ as follows:
\begin{equation}
\begin{aligned}
& \lambda_1 :=  \epsilon \cdot \til{\alpha}_1(z_1) , \\
& \lambda_2 :=  \epsilon \cdot \til{\alpha}_2(z_2) , \\
& \lambda_3 := -  \epsilon \cdot \til{\alpha}_1(z_3) , \\
& \lambda_4 := -  \epsilon \cdot \til{\alpha}_2(z_4) .
\end{aligned}
\end{equation}
Then, almost by definition,
\[ \opn{RP}_{0}(\alpha \vert \rho_i) = \exp_G(\lambda_i)  \]
and 
\begin{equation} \label{eqn:245}
\opn{RP}_{0}(\alpha \vert \partial \tau) =  
\prod_{i = 1}^{4} \, \exp_G(\lambda_i) .
\end{equation}

Now 
\[ s_k(z_i) \in \{ 0, \smfrac{1}{2} \epsilon, 
-  \smfrac{1}{2} \epsilon \} , \]
and the value $0$ occurs half the time. So the Taylor expansion 
(\ref{eqn:241}) for the point $z_i$ has only one summand of order $1$ in 
$\epsilon$ (instead of two). Let us define
\[ \mu_1 := \epsilon \cdot \til{\alpha}_1(z) , \quad
\mu'_1 := - \smfrac{1}{2} \epsilon^2 \cdot
(\smfrac{\partial}{\partial s_2} \til{\alpha}_1)(z)  ,  \]
\[ \mu_2 := \epsilon \cdot \til{\alpha}_2(z) , \quad
\mu'_2 := \smfrac{1}{2} \epsilon^2 \cdot 
(\smfrac{\partial}{\partial s_1} \til{\alpha}_2) (z) , \]
\[ \mu_3 := - \epsilon \cdot \til{\alpha}_1(z) , \quad
\mu'_3 := - \smfrac{1}{2} \epsilon^2 \cdot 
(\smfrac{\partial}{\partial s_2} \til{\alpha}_1)(z) , \]
\[ \mu_4 := - \epsilon \cdot \til{\alpha}_2(z) , \quad
\mu'_4 := \smfrac{1}{2} \epsilon^2 \cdot 
(\smfrac{\partial}{\partial s_1} \til{\alpha}_2)(z) . \]
Then using the estimate (\ref{eqn:242}) for the quadratic terms 
in (\ref{eqn:241}) we obtain
\begin{equation} \label{eqn:243}
\Norm{ \lambda_i - (\mu_i + \mu'_i) } \leq \epsilon^3 \cdot
\norm{\alpha}_{\mrm{Sob}} \, . 
\end{equation}
We also have these bounds:
\begin{equation} \label{eqn:246}
\norm{ \lambda_i } \leq \epsilon \cdot \norm{\alpha}_{\mrm{Sob}} \,
\end{equation}
and
\begin{equation} \label{eqn:247}
\norm{ \mu_i } \leq \epsilon \cdot \norm{\alpha}_{\mrm{Sob}} \ , \
\norm{ \mu'_i } \leq  \smfrac{1}{2} \epsilon^2 \cdot \norm{\alpha}_{\mrm{Sob}}
\, .
\end{equation}

According to property (iv) of Theorem \ref{thm:6}, the estimates
(\ref{eqn:243}) and (\ref{eqn:246}) yield 
\begin{equation} \label{eqn:22}
\begin{aligned}
& \Norm{ \log_G \Bigl( \boprod_{i = 1}^{4} \, \exp_G(\lambda_i) \Bigr)
- \log_G \Bigl( \boprod_{i = 1}^{4} \, \exp_G(\mu_i + \mu'_i) \Bigr) } \\
& \quad \quad \leq 4 \epsilon^3 \cdot c_0(G) \cdot \norm{\alpha}_{\mrm{Sob}} \,
. 
\end{aligned}
\end{equation}
for sufficiently small $\epsilon$. Similarly the estimates (\ref{eqn:247}) give
us
\begin{equation} \label{eqn:244}
\begin{aligned}
& \Norm{ \log_G \Bigl( \boprod_{i = 1}^{4} \, \exp_G(\mu_i + \mu'_i) \Bigr)
- \log_G \Bigl( \boprod_{i = 1}^{4} \, \exp_G(\mu_i) \Bigr)
- \bosum_{i = 1}^{4} \, \mu'_i } \\
& \quad \quad \leq 2 \epsilon^3 \cdot c_0(G) \cdot \norm{\alpha}_{\mrm{Sob}}^2
\, . 
\end{aligned}
\end{equation}

Now
$\mu_3 = -\mu_1$ and $\mu_4 = - \mu_2$, and hence
\[ \prod_{i = 1}^{4} \, \exp_G(\mu_i)  = 
\exp_G(\mu_1) \cdot \exp_G(\mu_2) \cdot \exp_G(- \mu_1) \cdot 
\exp_G(- \mu_2) . \]
According to property (iii) of Theorem \ref{thm:6} we see that
\begin{equation} \label{eqn:23}
\Norm{ \log_G \Bigl( \boprod_{i = 1}^{4} \, \exp_G(\mu_i) \Bigr)
- [\mu_1, \mu_2] }
\leq 2 \epsilon^3 \cdot c_0(G) \cdot \norm{\alpha}_{\mrm{Sob}}^3 \, .
\end{equation}
For the terms $\mu'_i$ we have
\begin{equation} \label{eqn:24}
\sum_{i = 1}^{4} \, \mu'_i = 
- \epsilon^2 \cdot (\smfrac{\partial}{\partial s_2} \til{\alpha}_1)(z) +
\epsilon^2 \cdot (\smfrac{\partial}{\partial s_1} \til{\alpha}_2) (z) \, . 
\end{equation}

Putting together equations (\ref{eqn:245}), (\ref{eqn:22}),
(\ref{eqn:244}), (\ref{eqn:23}) and (\ref{eqn:24})  
we conclude that for some 
$c \geq 1$ (depending on $(\alpha, \beta)$) the estimate
\[ \begin{aligned}
& \Norm{ \log_G \bigl( \opn{RP}_{0}(\alpha \vert \partial \tau) \bigr)
- \epsilon^2 \cdot \bigl(  [\til{\alpha}_1(z), \til{\alpha}_2(z)]  
- (\smfrac{\partial}{\partial s_2} \til{\alpha}_1)(z) +
(\smfrac{\partial}{\partial s_1} \til{\alpha}_2)(z) \bigr) } \\
& \qquad \leq \epsilon^3 \cdot c  
\end{aligned} \]
holds for sufficiently small $\epsilon$. 
Using Proposition \ref{prop:5}(2) we get
\begin{equation} \label{eqn:26}
\begin{aligned}
& \Norm{ \log_G \bigl( \opn{MI}(\alpha \vert \partial \tau) \bigr)
- \epsilon^2 \cdot \bigl(  [\til{\alpha}_1(z), \til{\alpha}_2(z)]  
- (\smfrac{\partial}{\partial s_2} \til{\alpha}_1)(z) +
(\smfrac{\partial}{\partial s_1} \til{\alpha}_2)(z) \bigr)  } \\
& \qquad \leq \epsilon^3 \cdot c' 
\end{aligned}
\end{equation}
for a suitable constant $c'$. 

Since equation (\ref{eqn:75}) holds, we know that $\beta$ is smooth on
$Z$. Let $\til{\beta} \in \mcal{O}(Z) \otimes \g$ be such that
$\beta|_{Z} = \til{\beta} \cdot \d s_1 \wedge \d s_2$.
Then (\ref{eqn:75}) becomes
\[ \til{\beta} = [\til{\alpha}_1, \til{\alpha}_2] - 
(\smfrac{\partial}{\partial s_2} \til{\alpha}_1) +
(\smfrac{\partial}{\partial s_1} \til{\alpha}_2) , \]
as smooth functions $Z \to \g$.
Thus we can rewrite (\ref{eqn:26}) as
\begin{equation} \label{eqn:27}
\Norm{ \log_G \bigl( \opn{MI}(\alpha \vert \partial \tau) \bigr)
- \epsilon^2 \cdot \til{\beta}(z) \bigr) } \leq \epsilon^3 \cdot c' \, .
\end{equation}
Letting
$g := \opn{MI}(\alpha \vert \sigma)$,
we have (by Proposition \ref{prop:1}):
\[ \opn{MI} \bigl( \alpha \vert \partial (\sigma, \tau) \bigr) =
g \cdot \opn{MI}(\alpha \vert \partial \tau) \cdot g^{-1} 
= \opn{Ad}_G(g) \bigl( \opn{MI}(\alpha \vert \partial \tau) \bigr) . \]
The map $\log_G$ sends $\opn{Ad}_G(g)$ to $\opn{Ad}_{\g}(g)$, and therefore
\[ \log_G \Bigl( \opn{MI} \bigl( \alpha \vert \partial (\sigma, \tau) \bigr) 
\Bigr) = \opn{Ad}_{\g}(g) \Bigl(
\log_G \bigl( \opn{MI}(\alpha \vert \partial \tau) \bigr) \Bigr) . \]
Recall that the length of $\sigma$ is bounded by $5$, so by 
Proposition \ref{prop:4} the norm of the operator 
$\opn{Ad}_{\g}(g)$ on $\g$ is also bounded. 
Plugging in the estimate (\ref{eqn:27})
we now arrive at
\begin{equation} \label{eqn:28}
\Norm{ \log_G \bigl( 
\opn{MI} \bigl( \alpha \vert \partial (\sigma, \tau) \bigr) \bigr)
- \epsilon^2 \cdot \opn{Ad}_{\g}(g) \bigl( \til{\beta}(z) \bigr) } \leq
\epsilon^3
\cdot c''' 
\end{equation}
for a suitable bound $c'''$, again depending on $(\alpha, \beta)$.

Finally, by definition we have
\[ \log_G \bigl( \opn{RP}_{0}(\alpha, \beta \vert \sigma, \tau) \bigr) = 
\epsilon^2 \cdot \opn{Ad}_{\g}(g) \bigl( \til{\beta}(z) \bigr) . \]
According to Proposition \ref{prop:8}(2) we know that
\[ \Norm{ \log_G \bigl(
\opn{RP}_{0}(\alpha, \beta \vert \sigma, \tau) \bigr)
- \log_G \bigl( \opn{MI}(\alpha, \beta \vert \sigma, \tau) \bigr) }
\leq c_2(\alpha, \beta) \cdot \epsilon^4 \, . \]
Combining this with (\ref{eqn:28}) we get
\[ \Norm{ \log_G \bigl( \opn{MI} (\alpha, \beta \vert \sigma, \tau) \bigr) -
\log_G \bigl( \opn{MI} (\alpha \vert \partial(\sigma, \tau)) \bigr) }
\leq c_4(\alpha, \beta) \cdot \epsilon^3   \]
for a sufficiently large constant $c_4(\alpha, \beta)$
and for all sufficiently small $\epsilon$. This gives us a value for
$\epsilon_4(\alpha, \beta)$.
\end{proof}

\begin{dfn} \label{dfn:34}
Let us fix constants $c_4(\alpha, \beta)$ and $\epsilon_4(\alpha, \beta)$ as in
Lemma \ref{lem:10}. 
A square kite $(\sigma, \tau)$ in $(\mbf{I}^2, v_0)$ will be
called {\em $(\alpha, \beta)$-tiny} in this section if 
$\opn{side}(\tau) < \epsilon_4(\alpha, \beta)$ and
$\opn{len}(\sigma) \leq 5$.
\end{dfn}

\begin{lem} \label{lem:7}
Let $(\sigma, \tau)$ be a kite in $(\mbf{I}^2, v_0)$. 
Take some $k \geq 0$. For $i \in \{ 1, \ldots, 4^k \}$ let 
\[ (\sigma_i, \tau_i) := (\sigma, \tau) \circ (\sigma^k_i, \tau^k_i)
= \opn{tes}^k_i (\sigma, \tau) . \]
Then
\[ \prod_{i = 1}^{4^k} \, 
\opn{MI} \bigl( \alpha \vert \partial(\sigma_i, \tau_i) \bigr) =
\opn{MI} \bigl( \alpha \vert \partial  (\sigma, \tau) \bigr) . \]
\end{lem}

\begin{proof}
By Proposition \ref{prop:1} we get cancellation of the contribution of all
inner edges. 
\end{proof}



\subsection{Stokes Theorem}

\begin{thm}[Nonabelian Stokes Theorem in Dimension $2$] \label{thm:1}
\index{Nonabelian Stokes Theorem for squares}
Let $(X, x_0)$ be a pointed polyhedron, let 	
$\mbf{C} / X$ be a Lie quasi crossed module with additive feedback over
$(X, x_0)$, and let $(\alpha, \beta)$ be a connection-curvature pair for
$\mbf{C} / X$.
Then for any kite $(\sigma, \tau)$ in $(X, x_0)$ one has
\[ \Phi_0 \bigl( \opn{MI} (\alpha, \beta \vert \sigma, \tau) \bigr) =
\opn{MI} \bigl( \alpha \vert \partial (\sigma, \tau) \bigr)  \]
in $G$.
\end{thm}

\begin{proof}
According to Proposition \ref{prop:9}(1) there is a transfer of
twisting setups
\[ (\opn{id}_G, \Phi_0, \Phi_X) :
(G, H, \Psi_{\h}) \to (G, G, \opn{Ad}_{\g}) \]
parametrized by $(X, x_0)$. Hence by Propositions \ref{prop:2} and
\ref{prop:11}(2) we can assume that $G = H$. 
Next, using Propositions \ref{prop:14}, \ref{prop:10} and \ref{prop:11}(1)
we can further assume that 
$(X, x_0) = (\mbf{I}^2, v_0)$, $(\sigma, \tau)$ is a square kite, and
$\opn{len}(\sigma) \leq 1$. We need to prove that 
\begin{equation}
\opn{MI} (\alpha, \beta \vert \sigma, \tau) = 
\opn{MI} (\alpha \vert \partial (\sigma, \tau))  
\end{equation}
in $G$.

Take $k$ large enough such that all the kites 
\begin{equation} \label{eqn:248}
(\sigma_i, \tau_i) := \opn{tes}^k_i (\sigma, \tau)
\end{equation}
in the $k$-th binary tessellation of $(\sigma, \tau)$ are 
$(\alpha, \beta)$-tiny. By Proposition \ref{prop:3} we have
\[ \opn{MI} (\alpha, \beta \vert \sigma, \tau) = 
\prod_{i = 1}^{4^k} \, 
\opn{MI} \bigl( \alpha, \beta \vert \sigma_i, \tau_i) . \]
Using Lemma \ref{lem:7} we see that it suffices to prove that 
\[ \opn{MI} \bigl( \alpha, \beta \vert \sigma_i, \tau_i) =
\opn{MI} \bigl( \alpha \vert \partial(\sigma_i, \tau_i) \bigr) \]
for every $i$. In this way we have reduced the problem to proving that 
\begin{equation} \label{eqn:29}
\opn{MI} (\alpha, \beta \vert \sigma, \tau) =
\opn{MI} \bigl( \alpha \vert \partial(\sigma, \tau) \bigr) 
\end{equation}
for any $(\alpha, \beta)$-tiny kite $(\sigma, \tau)$ in 
$(\mbf{I}^2, v_0)$.

So assume $(\sigma, \tau)$ is $(\alpha, \beta)$-tiny, with
$\epsilon := \opn{side}(\tau)$. Take some $k \geq 0$,
and let $(\sigma_i, \tau_i)$ be like in (\ref{eqn:248}). Then 
$\opn{side}(\tau_i) = (\smfrac{1}{2})^k \cdot \epsilon$.
We know that
\begin{equation} \label{eqn:30} 
\opn{MI} (\alpha, \beta \vert \sigma, \tau) =
\prod_{i = 1}^{4^k} \, 
\opn{MI} ( \alpha, \beta \vert \sigma_i, \tau_i)  
\end{equation}
and
\begin{equation} \label{eqn:31} 
\opn{MI} \bigl( \alpha \vert \partial  (\sigma, \tau) \bigr) = 
\prod_{i = 1}^{4^k} \, 
\opn{MI} \bigl( \alpha \vert \partial(\sigma_i, \tau_i) \bigr) . 
\end{equation}

Let us do some estimates now. If $i$ is a bad index (in the sense of 
Definition \ref{dfn:45}), then by Lemma \ref{lem:9} we know that
\[ \Norm{ \log_G \bigl( \opn{MI} (\alpha, \beta \vert \sigma_i, \tau_i) \bigr) 
} \leq c_3(\alpha, \beta) \cdot (\smfrac{1}{2})^{2 k} \epsilon^{2} \]
and
\[ \Norm{ \log_G \bigl( \opn{MI} (\alpha \vert \partial(\sigma_i, \tau_i))
\bigr) } \leq c_3(\alpha, \beta) \cdot (\smfrac{1}{2})^{2 k} \epsilon^{2} \, .
\]
On the other hand, if $i$ is a index kite, then Lemma
\ref{lem:10} says that 
\[ \Norm{ \log_G \bigl( \opn{MI} (\alpha, \beta \vert \sigma_i, \tau_i) \bigr) -
\log_G \bigl( \opn{MI} (\alpha \vert \partial(\sigma_i, \tau_i)) \bigr) }
\leq c_4(\alpha, \beta) \cdot  (\smfrac{1}{2})^{3 k} \epsilon^{3} \, . \]
Using these estimates, equations (\ref{eqn:30})-(\ref{eqn:31}),
Lemma \ref{lem:51} and property (iv) of Theorem \ref{thm:6}, we arrive at
\[ \begin{aligned}
& \Norm{ \log_G \bigl( \opn{MI} (\alpha, \beta \vert \sigma, \tau) \bigr)
- \log_G \bigl( \opn{MI} (\alpha \vert \partial(\sigma, \tau))
\bigr) } \\
& \qquad \leq 
\underset{\tup{good indices}}{\underbrace{4^k \cdot c_4(\alpha, \beta) \cdot 
(\smfrac{1}{2})^{3 k} \epsilon^{3}}} +
\underset{\tup{bad indices}}{\underbrace{
\bigl( a_0 + a_1 \cdot 2^k \bigr) \cdot 
c_3(\alpha, \beta) \cdot (\smfrac{1}{2})^{2 k} \epsilon^{2}}} \, .
\end{aligned} \]
Here 
$a_i := a_i(\alpha, \beta, \mbf{I}^2)$ are the constants from Lemma 
\ref{lem:51}. 
Since the right hand side of this inequality tends to $0$ as $k \to \infty$, 
we conclude that (\ref{eqn:29}) holds.
\end{proof}

\begin{exa} \label{exa:3}
A special case of the corollary is the situation of Example \ref{exa:2}. Take
any differential form 
$\alpha \in \Omega^1_{\mrm{pws}}(X) \otimes \g$, 
and let 
$\beta := \d (\alpha) + \smfrac{1}{2} [\alpha, \alpha]$. 
Then $(\alpha, \beta)$ is a connection-curvature pair, 
and the corollary says that
\[ \opn{MI} (\alpha, \beta \vert \sigma, \tau) =
\opn{MI} \bigl( \alpha \vert \partial (\sigma, \tau) \bigr) . \]
This is just Schlesinger's theorem \cite{DF}. 
\end{exa}



\subsection{The Fundamental Relation}

Here is an important consequence of Theorem \ref{thm:1}.

\begin{thm}[The Fundamental Relation] \label{thm:16}
\index{Fundamental Relation Theorem}
Let $(X, x_0)$ be a pointed polyhedron, let 	
$\mbf{C} / X$ be a Lie quasi crossed module with additive feedback over
$(X, x_0)$, let $(\alpha, \beta)$ be a connection-curvature pair for
$\mbf{C} / X$, and let $(\sigma, \tau)$ be a kite  in $(X, x_0)$.
Let us write 
\[ g := \opn{MI} \bigl( \alpha \vert \partial (\sigma, \tau) \bigr) \in G \]
and
\[ h :=  \opn{MI} (\alpha, \beta \vert \sigma, \tau) \in H . \]
Then
\[ \Psi(g) = \opn{Ad}_H(h) \]
as automorphisms of the pointed manifold $(H, 1)$. 
In particular, $\Psi(g)$ is a group automorphism of $H$.
\end{thm}

\begin{proof}
According to Theorem \ref{thm:1} we have
$g = \Phi_0(h)$, and by condition ($*$) of Definition \ref{dfn:22} we know that
\[ \Psi(g) = \Psi(\Phi_0(h)) = \opn{Ad}_{H}(h) . \]
\end{proof}

\begin{cor} \label{cor:6}
In the situation of Theorem \tup{\ref{thm:16}}, suppose 
$(\sigma', \tau')$ is
another kite in $(X, x_0)$. We get a closed string 
$\partial (\sigma', \tau')$ based at $x_0$, and a kite
$\bigl( \partial (\sigma', \tau') * \sigma, \tau \bigr)$. 

Then, writing
\[ h' :=  \opn{MI} (\alpha, \beta \vert \sigma', \tau') \in H , \]
one has
\[ \opn{MI} \bigl( \alpha, \beta \vert \partial (\sigma', \tau') * \sigma, \tau
\bigr) =
\opn{Ad}_H(h') (h)  \]
in $H$.
\end{cor}

See Figure \ref{fig:72}.

\begin{figure}
\includegraphics[scale=0.27]{fig72.jpg}
\caption{Illustration for Corollary \ref{cor:6}.} 
\label{fig:72}
\end{figure}

\begin{proof}
Let $\rho := \partial (\sigma', \tau')$, which is a closed string  based at
$x_0$, and let $g' :=  \opn{MI}(\alpha \vert \rho) \in G$.
By Theorem \ref{thm:16} we have $\Psi(g') = \opn{Ad}_H(h')$, so this is a group
automorphism of $H$. Consider the ``moving of the base point'' corresponding to
$\rho$. Since $\Psi(g')$ is a group
automorphism of $H$, it follows that $H^{g'} = H$, and 
\[ \opn{MI}^{g'}(\alpha, \beta \vert \sigma, \tau)  =
\opn{MI}(\alpha, \beta \vert \sigma, \tau) = h . \]
But from Theorem \ref{thm:14} we get
\[ \Psi(g') \bigl( \opn{MI}^{g'}(\alpha, \beta \vert \sigma, \tau) \bigr)  =
\opn{MI}(\alpha, \beta \vert \rho * \sigma, \tau)  . \]
\end{proof}









\cleardoublepage
