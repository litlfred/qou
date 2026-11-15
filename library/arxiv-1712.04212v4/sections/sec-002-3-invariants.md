---
doc_id: arxiv-1712.04212v4
doc_title: "1. Introduction"
section_id: sec-002-3-invariants
section_title: "Invariants"
section_number: 3
pages: 14-19
source_pdf: 1712.04212v4.pdf
source_sha256: 521911fc8724f3c2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.951
doc_brief: "1. Introduction — In this paper, we consider a concentration of measure problem on Riemannian manifolds with boundary."
---
\label{sec:Invariants}



\subsection{Isomophisms}
We first introduce the following notion:
\begin{defi}\label{defi:dominance}
For $i=1,2$,
let $X_{i}=(X_{i},d_{X_{i}},\mu_{X_{i}})$ be metric measure spaces with boundary.
We say that \textit{$X_{1}$ dominates $X_{2}$} if
there exists a $1$-Lipschitz map $\Phi:X_{1}\to X_{2}$ such that
\begin{equation}\label{eq:dominance}
\Phi_{\#}\mu_{X_{1}}=\mu_{X_{2}},\quad \Phi(\partial X_{1})\subset \partial X_{2},
\end{equation}
where $\Phi_{\#}\mu_{X_{1}}$ denotes the push-forward of $\mu_{X_{1}}$ by $\Phi$.
We also say that
$X_{1}$ and $X_{2}$ are \textit{isomorphic} to each other if
they dominate each other.
\end{defi}

\begin{rem}\label{rem:mm-spaces}
A triple $\mathcal{X}=(\mathcal{X},r_{\mathcal{X}},\sigma_{\mathcal{X}})$ is said to be an \textit{mm-space} when
$(\mathcal{X},r_{\mathcal{X}})$ is a complete separable metric space,
and $\sigma_{\mathcal{X}}$ is a Borel probability measure on $\mathcal{X}$.
For $i=1,2$,
let $\mathcal{X}_{i}=(\mathcal{X}_{i},r_{\mathcal{X}_{i}},\sigma_{\mathcal{X}_{i}})$ be mm-spaces.
They are said to be \textit{mm-isomorphic} to each other if 
there exists an isometry $\Phi:\supp \sigma_{\mathcal{X}_{1}}\to \supp \sigma_{\mathcal{X}_{2}}$ such that $\Phi_{\#}\sigma_{\mathcal{X}_{1}}=\sigma_{\mathcal{X}_{2}}$,
where $\supp \sigma_{\mathcal{X}_{i}}$ are the support of $\sigma_{\mathcal{X}_{i}}$.
It is said that
$\mathcal{X}_{1}$ \textit{dominates} $\mathcal{X}_{2}$ if
there exists a $1$-Lipschitz map $\Psi:\mathcal{X}_{1}\to \mathcal{X}_{2}$ such that $\Psi_{\#}\sigma_{\mathcal{X}_{1}}=\sigma_{\mathcal{X}_{2}}$.
It is well-known that
if $\mathcal{X}_{1}$ and $\mathcal{X}_{2}$ dominate each other,
then they are mm-isomorphic to each other (see e.g., Proposition 2.11 in \cite{Sh}).

For $i=1,2$,
let $X_{i}=(X_{i},d_{X_{i}},\mu_{X_{i}})$ be two metric measure spaces with boundary.
If $X_{1}$ and $X_{2}$ are isomorphic to each other in the sense of Definition \ref{defi:dominance},
then they dominate each other as mm-spaces;
in particular,
they are mm-isomorphic to each other.
\end{rem}

Let us show the following monotonicity of the partial inscribed radius defined as (\ref{eq:partial inscribed radius}) (cf. Proposition 2.18 in \cite{Sh}):
\begin{lem}\label{lem:monotonicity of the partial inscribed radius}
For $i=1,2$,
let $X_{i}=(X_{i},d_{X_{i}},\mu_{X_{i}})$ be metric measure spaces with boundary.
If $X_{1}$ dominates $X_{2}$,
then for every $\eta>0$
\begin{equation*}
\PI(X_{2};1-\eta)\leq \PI(X_{1};1-\eta).
\end{equation*}
\end{lem}
\begin{proof}
By the assumption for the dominance,
there exists a $1$-Lipschitz map $\Phi:X_{1}\to X_{2}$ such that (\ref{eq:dominance}).
We fix a Borel subset $\Omega \subset X_{1}$ with $\mu_{X_{1}}(\Omega)\geq 1-\eta$.
From $\Phi_{\#}\mu_{X_{1}}=\mu_{X_{2}}$
it follows that
\begin{equation}\label{lem:first key of the monotonicity of the partial inscribed radius}
\mu_{X_{2}}\bigl( \overline{\Phi(\Omega)}  \bigl)=\mu_{X_{1}}\bigl(\Phi^{-1}(\overline{\Phi(\Omega)} )\bigl) \geq \mu_{X_{1}}(\Omega)\geq 1-\eta,
\end{equation}
where $\overline{\Phi(\Omega)}$ denotes the closure of $\Phi(\Omega)$.

We now show
\begin{equation}\label{lem:second key of the monotonicity of the partial inscribed radius}
\IR \overline{\Phi(\Omega)} \leq \IR \Omega,
\end{equation}
where $\IR \overline{\Phi(\Omega)}$ and $\IR \Omega$ are the inscribed radii of $\overline{\Phi(\Omega)}$ and $\Omega$ defined as (\ref{eq:inscribed radius}),
respectively.
We fix $x_{2}\in \overline{\Phi(\Omega)}$,
and take a sequence $\{ x_{2,j} \}$ in $\Phi(\Omega)$ with $x_{2,j}\to x_{2}$.
For each $j$
we have $x_{1,j}\in \Omega$ satisfying $x_{2,j}=\Phi(x_{1,j})$.
By using the properness of $X_{1}$,
we can choose $z_{1,j}\in \partial X_{1}$ with $d_{X_{1}}(x_{1,j},z_{1,j})=\rho_{\partial X_{1}}(x_{1,j})$.
We set $z_{2,j}:=\Phi(x_{2,j})$.
From $\Phi(\partial X_{1})\subset \partial X_{2}$
we deduce $z_{2} \in \partial X_{2}$.
Since $\Phi$ is $1$-Lipschitz,
we see
\begin{equation*}
\rho_{\partial X_{2}}(x_{2,j})\leq d_{X_{2}}(x_{2,j},z_{2,j})\leq d_{X_{1}}(x_{1,j},z_{1,j})=\rho_{\partial X_{1}}(x_{1,j})\leq \IR \Omega.
\end{equation*}
Letting $j\to \infty$,
we derive $\rho_{\partial X_{2}}(x_{2})\leq \IR \Omega$.
This yields (\ref{lem:second key of the monotonicity of the partial inscribed radius}).
In virtue of (\ref{lem:first key of the monotonicity of the partial inscribed radius}) and (\ref{lem:second key of the monotonicity of the partial inscribed radius}),
we obtain
\begin{equation*}
\PI(X_{2};1-\eta)\leq \IR \overline{\Phi(\Omega)} \leq \IR \Omega.
\end{equation*}
The arbitrariness of $\Omega$ completes the proof.
\end{proof}

We also have the following monotonicity of the observable inscribed radius
introduced in Definition \ref{defi:observable inscribed radius} (cf. Proposition 2.18 in \cite{Sh}).
The proof is straightforward,
and we omit it.
\begin{lem}\label{lem:monotonicity of the observable inscribed radius}
For $i=1,2$,
let $X_{i}=(X_{i},d_{X_{i}},\mu_{X_{i}})$ be metric measure spaces with boundary.
If $X_{1}$ dominates $X_{2}$,
then for every $\eta>0$
\begin{equation*}
\OI(X_{2};-\eta)\leq \OI(X_{1};-\eta).
\end{equation*}
\end{lem}














According to Lemmas \ref{lem:monotonicity of the partial inscribed radius} and \ref{lem:monotonicity of the observable inscribed radius},
they are invariants under the isomorphism introduced in Definition \ref{defi:dominance}.



\subsection{Boundary separation distances}
Let $X=(X,d_{X},\mu_{X})$ be a metric measure space with boundary,
and let $k\geq 1$ be an integer.
For positive numbers $\eta_{1},\dots,\eta_{k}>0$,
we denote by $\mathcal{S}_{X}(\eta_{1},\dots,\eta_{k})$ the set of all sequences $\{\Omega_{\alpha}\}^{k}_{\alpha=1}$ of Borel subsets $\Omega_{\alpha}$ with $\mu_{X}(\Omega_{\alpha})\geq \eta_{\alpha}$.
For a sequence $\{\Omega_{\alpha}\}^{k}_{\alpha=1} \in \mathcal{S}_{X}(\eta_{1},\dots,\eta_{k})$,
we set
\begin{equation*}
\mathcal{D}_{X}\bigl(\{\Omega_{\alpha}\}^{k}_{\alpha=1}\bigl):=\min \left \{\, \min_{\alpha \neq \beta} d_{X}(\Omega_{\alpha},\Omega_{\beta}),\,\, \min_{\alpha} d_{X}(\Omega_{\alpha},\partial X)  \,\right\}.
\end{equation*}

We now define the following quantity:
\begin{defi}\label{defi:Dirichlet separation distance}
Let $X=(X,d_{X},\mu_{X})$ be a metric measure space with boundary.
For $\eta_{1},\dots,\eta_{k}>0$,
we define the \textit{$(\eta_{1},\dots,\eta_{k})$-boundary separation distance $\DS(X;\eta_{1},\dots,\eta_{k})$ of $X$} as follows:
If $\mathcal{S}_{X}(\eta_{1},\dots,\eta_{k})$ is non-empty,
then 
\begin{equation*}
\DS(X;\eta_{1},\dots,\eta_{k}):=\sup\,\mathcal{D}_{X}\bigl(\{\Omega_{\alpha}\}^{k}_{\alpha=1}\bigl),
\end{equation*}
where the supremum is taken over all $\{\Omega_{\alpha}\}^{k}_{\alpha=1} \in \mathcal{S}_{X}(\eta_{1},\dots,\eta_{k})$;
otherwise,
$\DS(X;\eta_{1},\dots,\eta_{k}):=0$.
\end{defi}
The boundary separation distance $\DS(X;\eta_{1},\dots,\eta_{k})$ is monotone non-increasing in $\eta_{\alpha}$ for each $\alpha=1,\dots,k$.

\begin{rem}\label{rem:Gromov separation distance}
The boundary separation distance is an analogue of the \textit{separation distance} on mm-spaces introduced by Gromov \cite{G}.
For later convenience,
we recall its precise definition:
Let $\mathcal{X}=(\mathcal{X},r_{\mathcal{X}},\sigma_{\mathcal{X}})$ be an mm-space (see Remark \ref{rem:mm-spaces}).
For positive numbers $\eta_{0}, \eta_{1},\dots,\eta_{k}>0$,
the \textit{$(\eta_{0}, \eta_{1},\dots,\eta_{k})$-separation distance} is defined as
\begin{equation}\label{eq:Gromov separation distance}
\SE(\mathcal{X};\eta_{0}, \eta_{1},\dots,\eta_{k}):=\sup\, \min_{\alpha \neq \beta} r_{\mathcal{X}}(\Omega_{\alpha},\Omega_{\beta}),
\end{equation}
where the supremum is taken over all sequences $\{\Omega_{\alpha}\}^{k}_{\alpha=0}$ of Borel subsets $\Omega_{\alpha} \subset \mathcal{X}$ with $\sigma_{\mathcal{X}}(\Omega_{\alpha})\geq \eta_{\alpha}$.
If there exists no such sequence,
then we set $\SE(\mathcal{X};\eta_{0}, \eta_{1},\dots,\eta_{k}):=0$.
\end{rem}

We verify the following monotonicity (cf. Lemma 2.25 in \cite{Sh}):
\begin{lem}\label{lem:monotonicity of Dirichlet separation distance}
For $i=1,2$,
let $X_{i}=(X_{i},d_{X_{i}},\mu_{X_{i}})$ be metric measure spaces with boundary.
If $X_{1}$ dominates $X_{2}$,
then for all $\eta_{1},\dots,\eta_{k}>0$
\begin{equation*}
\DS(X_{2};\eta_{1},\dots,\eta_{k})\leq \DS(X_{1};\eta_{1},\dots,\eta_{k}).
\end{equation*}
\end{lem}
\begin{proof}
We may assume $\mathcal{S}_{X_{2}}(\eta_{1},\dots,\eta_{k})\neq \emptyset$.
Fix a sequence $\{\Omega_{\alpha}\}^{k}_{\alpha=1} \in \mathcal{S}_{X_{2}}(\eta_{1},\dots,\eta_{k})$.
There exists a $1$-Lipschitz map $\Phi:X_{1}\to X_{2}$ such that (\ref{eq:dominance}).
Since $\Phi$ is $1$-Lipschitz,
for all $\alpha,\beta=1,\dots,k$,
we see
\begin{equation}\label{eq:monotonicity of distances between Borel subsets}
d_{X_{2}}(\Omega_{\alpha},\Omega_{\beta})\leq d_{X_{1}}(\Phi^{-1}(\Omega_{\alpha}),\Phi^{-1}(\Omega_{\beta})).
\end{equation}
Furthermore,
by $\Phi_{\#}\mu_{X_{1}}=\mu_{X_{2}}$,
for every $\alpha=1,\dots,k$,
\begin{equation}\label{eq:lower bound of volume}
\mu_{X_{1}}(\Phi^{-1}(\Omega_{\alpha}))=\mu_{X_{2}}(\Omega_{\alpha}) \geq \eta_{\alpha}.
\end{equation}

We show that
for every $\alpha=1,\dots,k$,
\begin{equation}\label{eq:distance monotonicity}
d_{X_{2}}(\Omega_{\alpha},\partial X_{2})\leq d_{X_{1}}(\Phi^{-1}(\Omega_{\alpha}),\partial X_{1}).
\end{equation}
Take $x_{1} \in \Phi^{-1}(\Omega_{\alpha})$,
and put $x_{2}:=\Phi(x_{1})\in \Omega_{\alpha}$.
From the properness of $X_{1}$,
there exists $z_{1} \in \partial X_{1}$ such that $d_{X_{1}}(x_{1},z_{1})=d_{X_{1}}(x_{1},\partial X_{1})$.
Put $z_{2}:=\Phi(z_{1})\in \partial X_{2}$.
It follows that
\begin{equation*}
d_{X_{2}}(\Omega_{\alpha},\partial X_{2})\leq d_{X_{2}}(x_{2},z_{2})\leq d_{X_{1}}(x_{1},z_{1})=d_{X_{1}}(x_{1},\partial X_{1}),
\end{equation*}
and
we obtain (\ref{eq:distance monotonicity}).
By combining (\ref{eq:monotonicity of distances between Borel subsets}), (\ref{eq:lower bound of volume}) and (\ref{eq:distance monotonicity}),
\begin{equation*}
\mathcal{D}_{X_{2}}\bigl(\{\Omega_{\alpha}\}^{k}_{\alpha=1}\bigl) \leq \mathcal{D}_{X_{1}}\bigl(\{   \Phi^{-1}(\Omega_{\alpha})   \}^{k}_{\alpha=1}\bigl) \leq \DS(X_{1};\eta_{1},\dots,\eta_{k}).
\end{equation*}
This completes the proof.
\end{proof}
Lemma \ref{lem:monotonicity of Dirichlet separation distance} tells us that
the boundary separation distance is an invariant under the isomorphism introduced in Definition \ref{defi:dominance}.



\subsection{Relations between invariants}

We present the following relation between our invariants (cf. Proposition 2.26 in \cite{Sh}):
\begin{lem}\label{lem:observable inscribed radius is smaller than Dirichlet separation distance}
Let $X=(X,d_{X},\mu_{X})$ be a metric measure space with boundary.
Then for every $\eta>0$
we have
\begin{equation*}
\OI(X;-\eta)\leq \DS(X;\eta).
\end{equation*}
In particular,
$\OI(X;-\eta)\leq \IR X$.
\end{lem}
\begin{proof}
We may assume $\eta<1$.
We fix a $1$-Lipschitz function $\varphi:X\to I$ with $\varphi|_{\partial X}=0$.
Let $m_{I,\varphi}$ be the Borel probability measure on the $\varphi$-screen $I_{\varphi}$ defined as (\ref{eq:screen}).
By $m_{I,\varphi}=\varphi_{\#}\mu_{X}$ and $\varphi(\partial X)\subset \partial I$,
the space $X$ dominates $I_{\varphi}$;
in particular,
Lemma \ref{lem:monotonicity of Dirichlet separation distance} yields
\begin{equation}\label{eq:monotonicity of Dirichlet separation distance under the screen}
\DS(I_{\varphi};\eta) \leq \DS(X;\eta).
\end{equation}
We put
\begin{equation*}
t_{0}:=\inf\{\,t\in I \mid m_{I,\varphi}((t,\infty))\leq \eta \,\}.
\end{equation*}
Note that
$m_{I,\varphi}((t_{0},\infty))\leq \eta$ and $m_{I,\varphi}([t_{0},\infty))\geq \eta$.
Since $m_{I,\varphi}([0,t_{0}])\geq 1-\eta$,
we have
\begin{equation}\label{eq:upper partial inscribed radius bound}
\PI(I_{\varphi};1-\eta)\leq \IR [0,t_{0}]= t_{0}.
\end{equation}
On the other hand,
$m_{I,\varphi}([t_{0},\infty))\geq \eta$ leads to
\begin{equation}\label{eq:lower Dirichlet separation distance bound}
t_{0}=d_{I}(\partial I,[t_{0},\infty)) \leq \DS(I_{\varphi};\eta).
\end{equation}
Now,
(\ref{eq:monotonicity of Dirichlet separation distance under the screen}) together with (\ref{eq:upper partial inscribed radius bound}), (\ref{eq:lower Dirichlet separation distance bound}) implies the desired one.
\end{proof}

\begin{rem}
A sequence $\{X_{n}\}$ of metric measure spaces with boundary is said to be \textit{inscribed radius collapsing} if 
$\IR X_{n} \to 0$ as $n\to \infty$.
Yamaguchi and Zhang \cite{YZ} have studied inscribed radius collapsing sequences of manifolds with boundary from the view point of the collapsing theory.
From Lemma \ref{lem:observable inscribed radius is smaller than Dirichlet separation distance},
it follows that
if a sequence of metric measure spaces with boundary is inscribed radius collapsing,
then it is a boundary concentration family introduced in Definition \ref{defi:Dirichlet Levy family}.
\end{rem}

We also possess the following relation (cf. Proposition 2.26 in \cite{Sh}):
\begin{lem}\label{lem:Dirichlet separation distance is smaller than observable inscribed radius}
Let $X=(X,d_{X},\mu_{X})$ be a metric measure space with boundary.
Then for all $\eta,\eta'>0$ with $\eta>\eta'$
we have
\begin{equation*}
\DS(X;\eta) \leq \OI(X;-\eta').
\end{equation*}
\end{lem}
\begin{proof}
We may assume $\DS(X;\eta)>0$.
Fix a Borel subset $\Omega \subset X$ with $\mu_{X}(\Omega)\geq \eta$,
and also fix $J \subset I$ with $m_{I,\rho_{\partial X}}(J) \geq 1-\eta'$.
Then
\begin{equation*}
m_{I,\rho_{\partial X}}(\overline{\rho_{\partial X}(\Omega)})+m_{I,\rho_{\partial X}}(J)\geq \mu_{X}(\Omega)+m_{I,\rho_{\partial X}}(J)\geq \eta+(1-\eta') >1,
\end{equation*}
and hence $\overline{\rho_{\partial X}(\Omega)} \cap J \neq \emptyset$,
where $\overline{\rho_{\partial X}(\Omega)}$ denotes the closure of $\rho_{\partial X}(\Omega)$.
For every $t_{0} \in \overline{\rho_{\partial X}(\Omega)} \cap J$
we see
\begin{align*}
\IR J &\geq d_{I}(t_{0},\partial I) \geq d_{I}(\overline{\rho_{\partial X}(\Omega)},\partial I)\\
        &=d_{I}(\rho_{\partial X}(\Omega),\partial I)=\inf_{x\in \Omega} \rho_{\partial X}(x)=d_{X}(\Omega,\partial X).
\end{align*}
This yields
\begin{equation*}
\OI(X;-\eta') \geq \PI(I_{\rho_{\partial X}};1-\eta')\geq \DS(X;\eta).
\end{equation*}
We arrive at the desired assertion.
\end{proof}

By combining Lemmas \ref{lem:observable inscribed radius is smaller than Dirichlet separation distance} and \ref{lem:Dirichlet separation distance is smaller than observable inscribed radius},
and by straightforward argument,
one can conclude the following equivalence:
\begin{prop}\label{prop:characterization of Dirichlet Levy}
Let $\{X_{n}\}$ be a sequence of metric measure spaces with boundary $X_{n}=(X_{n},d_{X_{n}},\mu_{X_{n}})$.
Then the following are equivalent:
\begin{enumerate}\setlength{\itemsep}{+0.7mm}
\item $\{X_{n}\}$ is a boundary concentration family;
\item for every sequence $\{\Omega_{n}\}$ of Borel subsets $\Omega_{n} \subset X_{n}$ satisfying $\liminf_{n\to \infty} \mu_{X_{n}}(\Omega_{n})>0$,
         we have $\lim_{n\to \infty}\, d_{X_{n}}(\Omega_{n},\partial X_{n})=0$;
\item for every $r>0$
         we have $\lim_{n\to \infty}\,\mu_{X_{n}}(B_{r}(\partial X_{n}))=1$.
\end{enumerate}
\end{prop}

Finally,
we observe the following fact for the equality case of Lemma \ref{lem:Dirichlet separation distance is smaller than observable inscribed radius}.
The statement and its proof are informed by Daisuke Kazukawa.
\begin{prop}\label{prop:Kazukawa}
Let $X=(X,d_{X},\mu_{X})$ be a metric measure space with boundary.
If $\supp \mu_{X}=X$,
then for every $\eta>0$
we have
\begin{equation*}
\OI(X;-\eta)=\DS(X;\eta).
\end{equation*}
\end{prop}
\begin{proof}
Lemma \ref{lem:observable inscribed radius is smaller than Dirichlet separation distance} tells us that
the left hand side is at most the right hand side.
We verify the opposite.
We may assume $\DS(X;\eta)>0$.
Fix a sufficiently small $\epsilon>0$.
Then there exists a Borel subset $\Omega \subset X$ with $\mu_{X}(\Omega) \geq \eta$ such that $d_{X}(\Omega,\partial X) >\DS(X;\eta)-\epsilon$.
Let us define a $1$-Lipschitz function $\varphi:X\to I$ by
\begin{equation*}
\varphi(x):=\max \left\{d_{X}(\Omega,\partial X)-d_{X}(x,\Omega),0\right\}.
\end{equation*}
Notice that
$\varphi|_{\partial X}=0,\,\varphi|_{\Omega}=d_{X}(\Omega,\partial X)$ and
\begin{equation*}
m_{I,\varphi}(\{ d_{X}(\Omega,\partial X)\})\geq \mu_{X}(\Omega) \geq \eta.
\end{equation*}
Furthermore,
$\supp \mu_{X}=X$ implies $\supp m_{I,\varphi}=[0,d_{X}(\Omega,\partial X)]$.

We now show
\begin{equation}\label{eq:Kazukawa}
\PI(I_{\varphi};1-\eta) \geq d_{X}(\Omega,X).
\end{equation}
The proof is by contradiction.
Suppose that
there exists a Borel subset $J \subset I$ with $m_{I,\varphi}(J)\geq 1-\eta$ such that $\IR J<d_{X}(\Omega,\partial X)$.
We put $\hat{J}:=(\IR J, d_{X}(\Omega,\partial X))$.
Then we have
\begin{align*}
1&   =   m_{I,\varphi}([0,\IR J])+m_{I,\varphi}(\hat{J})+m_{I,\varphi}(\{ d_{X}(\Omega,\partial X)\})\\
  &\geq m_{I,\varphi}(J)+m_{I,\varphi}(\hat{J})+\eta \geq 1+m_{I,\varphi}(\hat{J}),
\end{align*}
and hence $m_{I,\varphi}(\hat{J})=0$.
This contradicts $\supp m_{I,\varphi}=[0,d_{X}(\Omega,\partial X)]$.
From (\ref{eq:Kazukawa})
it follows that
\begin{equation*}
\DS(X;\eta)-\epsilon<d_{X}(\Omega,\partial X) \leq \OI(X;-\eta).
\end{equation*}
By letting $\epsilon \to 0$,
we complete the proof.
\end{proof}
