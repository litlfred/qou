---
doc_id: arxiv-2011.13340v1
doc_title: "A Matrix Bernstein Inequality for Strong Rayleigh Distributions *"
section_id: sec-001-2-matrix-valued-poincare-inequality-for-strong-r
section_title: "Matrix Valued Poincare Inequality for Strong Rayleigh measures"
section_number: 2
pages: 4-10
source_pdf: 2011.13340v1.pdf
source_sha256: e73876ed2c923608
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.993
doc_brief: "A Matrix Bernstein Inequality for Strong Rayleigh Distributions * — The Entropy method provides a powerful framework for proving scalar concentration in- equalities by establishing functional"
---
In this section, we prove our matrix valued Poincare inequality for measures satisfying the stochastic covering property (SCP). We first need some notation in order to define SCP measures. Let $\{e_i\}_{i=1}^{n}$ be the coordinate basis of $\mathbb{R}^n$. For $x,y \in \{ 0,1\}^n$, we write $x\triangleright y$ if $x$ can be obtained by $y$ by increasing at most one coordinate from 0 to 1, i.e.,
\begin{align*}
  x=y \ \text{ or } \ \exists i \in [n], \ x=y+e_i
\end{align*}
This \textit{covering} relation can be lifted to measures on $\{ 0,1\}^n$ by writing $\pi \triangleright \pi'$ whenever there is a coupling of $\pi$ and $\pi'$ which is supported on the set $\{(x,y): x \triangleright y\}$. We say that $\pi$ has the SCP if for any $S \subseteq [n]$ and $x,y \in \{0,1\}^S$, we have
\begin{align*}
  x \triangleright y \implies \pi(X_{S^c} = \cdot | X_S = y)\triangleright \pi(X_{S^c} = \cdot | X_S = x)
\end{align*}
This property was proposed by Pemantle and Peres \cite{PP14} and they proved that all strong Rayleigh measures satisfy the SCP. However, there are examples of matroids for which the uniform distribution has the SCP but do not have the strong Rayleigh property. Hermon and Salez \cite{HS19} consider the following local dynamics :
\begin{align*}
  x \sim y \iff x,y \text{ differ by a flip or a swap}
\end{align*}
where $x,y$ differ by a flip if $x=y \pm e_i$ for some $i$ and by a swap if $y=x+e_j-e_k$ for distinct $j$ and $k$. And then they say that $Q$ is a flip-swap walk Markov generator for $\pi$ which is reversible under $\pi$ and we have
\begin{align*}
  Q_{xy} > 0 \iff x\sim y
\end{align*}
If in addition, we have $\Delta(Q) = \max\{-Q_{xx} : x \in \Omega\} \leq 1$, we say that $Q$ is normalized and $Q$ may hence be written as $Q=P-I$ for some stochastic matrix $P$. \cite{HS19} proved that there is a normalized flip-swap walk for an SCP distribution has a modified log-Sobolev and Poincare constant $1/2k$. We will prove using their proof strategy that this walk actually has it's Matrix valued Poincare constant also $1/2k$.
\begin{theorem}\label{thm:mpc} If $\pi$ is a $k$-homogenous SCP measure, then there is a  normalized flip-swalk walk $Q$ for $\pi$ such that for any matrix valued function $\mathbf{f} : \Omega \rightarrow \mathbb{S}_d$
  \begin{align*}
    \lambda\mathbf{Var}[\mathbf{f}]\preceq \mathcal{E}(\mathbf{f},\mathbf{f})
  \end{align*}
  with $\lambda \geq \frac{1}{2k}$. Furthermore, the conclusion remains valid without the homogeneity assumption, with $k=n/2$
\end{theorem}
The proof of the scalar equivalent of the above statement in \cite{HS19} follows the chain decomposition framework of \cite{JSTV04} which we elaborate on next. Let $Q$ be any reversible Markov generator with respect to some probability distribution $\pi$ on a finite set $\Omega$. Consider any partition of the state space :
\begin{align*}
  \Omega = \bigcup\limits_{i \in \mathcal{I}}\Omega_i
\end{align*}
We define two chains using this partition. Let the \textit{projection chain} induced by this partition be the Markov chain whose state space is $\mathcal{I}$ and whose Markov generator $\hat{Q}$ is defined as follows: for any $i,j \in \Omega$,
\begin{align*}
  \hat{Q}(i,j) = \frac{1}{\hat{\pi}(i)}\sum\limits_{x \in \Omega_i, y \in \Omega_j} \pi(x) Q(x,y) \ \ \text{ where } \hat{\pi}(i) = \sum\limits_{x \in \Omega_i} \pi(x)
\end{align*}
Note that $\hat{\pi}$ is a probability distribution on $\mathcal{I}$ and that it is reversible under $\hat{Q}$,i.e.,
\begin{align*}
  \hat{\pi}(i) \hat{Q}(i,j) =   \hat{\pi}(j) \hat{Q}(j,i)
\end{align*}
We also have, that for each $i \in \mathcal{I}$, the \textit{restriction chain} on $\Omega_i$ is the Markov chain whose state space is $\Omega_i$ and whose Markov geneator $Q_i$ is defined as: for any states $x,y \in \Omega_i$,
\begin{align*}
  Q_i(x,y) = Q(x,y)
  \end{align*}
with the diagonal entries being adjusted so that the rows of $Q_i$ sum to zero. Clearly, then we have \begin{align*}\hat{\pi}_i(x) = \frac{\pi(x)}{\hat{\pi}(i)}\end{align*}
which is reversible under $Q_i$. Now suppose that for each $(i,j) \in \mathcal{I}^2$ with $\hat{Q}_{ij} > 0$, we are given a coupling $\kappa_{ij} : \Omega_i \times \Omega_j \rightarrow [0,1]$ of the probability distribution $\pi_i$ and $\pi_j$,i.e.,
\begin{align*}
  \forall x \in \Omega_i, \ \sum\limits_{y \in \Omega_j}\kappa_{ij}(x,y) = \pi_i(x)\\
  \forall y \in \Omega_j, \ \sum\limits_{x \in \Omega_i}\kappa_{ij}(x,y) = \pi_j(y)
\end{align*}
We will also need the following measure of quality of the coupling
\begin{align*}
  \chi = \min\bigg\{\frac{\pi(x)Q(x,y)}{\hat{\pi}(i)\hat{Q}(i,j)\kappa_{ij}(x,y)}\bigg\}
\end{align*}
where the minimum runs over all $(x,y,i,j)$ such that the denominator is positive.

The main idea of \cite{JSTV04} is to relate the Poincare and (modified) log-Sobolev constants of the original chain to the projection and restriction chains. Given the above setup, we would now like to prove recursive functional inequalities over the restriction and projection chains. Inequalities of this form are the workhorse of all applications of the induction/chain decomposition idea \cite{JSTV04}. Our next lemma establishes that scalar recursive Poincare inequalities can be lifted to matrix Poincare inequalities, using operator convexity properties of the square function. We first need the following proposition.
\begin{proposition}\label{prop:diffOC} The function $f(\mathbf{X},\mathbf{Y}) = (\mathbf{X}-\mathbf{Y})^2$ is jointly operator convex.
\end{proposition}
\begin{proof}
For any $t\in [0,1]$, $\mathbf{X}_1,\mathbf{X}_2,\mathbf{Y}_1,\mathbf{Y}_2$, we have
  \begin{align*}
    \big( (t \mathbf{X}_1 + (1-t)\mathbf{X}_2) - (t \mathbf{Y}_1 + (1-t)\mathbf{Y}_2)\big)^2&=\big( t (\mathbf{X}_1-\mathbf{Y}_1) + (1-t)(\mathbf{X}_2 -\mathbf{Y}_2)\big)^2\\
    &\preceq t(\mathbf{X}_1-\mathbf{Y}_1)^2+(1-t)(\mathbf{X}_1-\mathbf{Y}_1)^2
  \end{align*}
  where the last step follows from the operator convexity of the square function applied to $\mathbf{X}_1-\mathbf{Y}_1$ and $\mathbf{X}_2-\mathbf{Y}_2$
\end{proof}

\begin{lemma}{[Recursive Poincare inequalities]}\label{lem:recPI} With the above notation, we have
  \begin{align*}\lambda(Q) \geq \min\big\{\chi\lambda(\hat{Q}),\min\limits_{i \in \mathcal{I}}\lambda(Q_i)\big\}
  \end{align*}
  where the $\lambda(\cdot)$ represent the constant in the matrix valued Poincare inequality for the associated generator.
\end{lemma}
\begin{proof}
  Let $\mathbf{F}:\Omega \rightarrow \mathbb{S}_d$. The Dirichlet form can be written as
  \begin{align*}
    \mathcal{E}(\mathbf{F},\mathbf{F}) = \frac{1}{2}\sum\limits_{x,y\in\Omega}\pi(x)Q(x,y)(\mathbf{F(x)}-\mathbf{F(y)})^2
\end{align*}
We can also define the projection of a function $\hat{\mathbf{F}}:\mathcal{I}\rightarrow \mathbb{S}_d$ by $\hat{\mathbf{F}}(i)=\mathbb{E}_{\pi_i}[\mathbf{F}]$. Hence, we can also decompose the variance and Dirichlet form of a matrix valued function as follows:
\begin{align*}
  \mathbf{Var}_\pi[\mathbf{F}]&=\sum\limits_{i \in \mathcal{I}}\hat{\pi}(i)\mathbf{Var}_{\pi_i}[\mathbf{F}] + \mathbf{Var}_{\hat{\pi}}[\hat{\mathbf{F}}]\\
  \mathcal{E}_\pi(\mathbf{F},\mathbf{F}) &= \sum\limits_{i \in \mathcal{I}}\hat{\pi}(i)\mathcal{E}_{\pi_i}(\mathbf{F},\mathbf{F})+\frac{1}{2}\sum\limits_{i \neq j}\sum\limits_{x\in\Omega_i, y \in \Omega_j}\pi(x)Q(x,y)(\mathbf{F(x)}-\mathbf{F(y)})^2
\end{align*}
We would now like to make a term-by-term comparison between the right hand sides of the above two equations. In order to do this, we would like to replace the second term in the Dirichlet form equation by the Dirichlet form for $\mathcal{E}_{\hat{\pi}}(\mathbf{\hat{F}},\mathbf{\hat{F}})$. This is where the coupling is useful. Consider any pair $(i,j)\in\mathcal{I}$ such that $\hat{Q})i,j$>0
. Since $\kappa_{ij}$ is a coupling of $\pi_i$ and $\pi_j$, we have
\begin{align*}
  \mathbf{\hat{F}}(i) &= \sum\limits_{x\in\Omega_i,y\in\Omega_j}\kappa_{ij}(x,y)\mathbf{F}(x)\\
  \mathbf{\hat{F}}(j) &= \sum\limits_{x\in\Omega_i,y\in\Omega_j}\kappa_{ij}(x,y)\mathbf{F}(y)\\
\end{align*}
We can now use Lemma \ref{prop:diffOC} and operator Jensen's inequality (Lemma \ref{lem:jensen}) to conclude that
\begin{align*}
  \sum\limits_{x\in\Omega_i, y\in\Omega_j}\kappa_{ij}(x,y)(\mathbf{F(x)}-\mathbf{F(y)})^2 \succeq (\mathbf{\hat{F}(i)}-\mathbf{\hat{F}(j)})
\end{align*}
Multiplying the above equation by $\chi\hat{\pi}(i)\hat{Q}(i,j)$ we have
\begin{align*}
  \sum\limits_{x\in\Omega_i,y\in\Omega_j}\pi(x)Q(x,y)(\mathbf{F(x)}-\mathbf{F(y)})^2 \succeq \chi \hat{\pi}(i)\hat{Q}(i,j)(\mathbf{\hat{F}(i)}-\mathbf{\hat{F}(j)})^2
\end{align*}
It is easy to see that the above equation also holds when $\hat{Q}(i,j)=0$ rather than just when $\hat{Q}(i,j)=0$. Now, summing up over all distinct $i,j\in \mathcal{I}$, we get that
\begin{align*}
  \frac{1}{2}\sum\limits_{i \neq j}\sum\limits_{x\in\Omega_i, y \in \Omega_j}\pi(x)Q(x,y)(\mathbf{F(x)}-\mathbf{F(y)})^2&\succeq\chi \mathcal{E}_{\hat{\pi}}[\mathbf{\hat{F}},\mathbf{\hat{F}}]\\
  \implies \mathcal{E}_\pi[\mathbf{F},\mathbf{F}]\succeq \sum\limits_{i \in \mathcal{I}}\hat{\pi}(i)\mathcal{E}_{\pi_i}[\mathbf{F},\mathbf{F}]+\chi\mathcal{E}_{\hat{\pi}}[\mathbf{\hat{F}},\mathbf{\hat{F}}]
  \end{align*}
Comparing this with the Variance decomposition, we get
  \begin{align*}\begin{cases}
  \mathcal{E_{\hat{\pi}}}[\mathbf{\hat{F}},\mathbf{\hat{F}}]&\succeq \hat{\kappa}\mathbf{Var}_{\hat{\pi}}[\mathbf{\hat{F]}}\\
  \mathcal{E}_{\pi_i}[\mathbf{F},\mathbf{F}]&\succeq \kappa_{i}\mathbf{Var}_{\pi_{i}}[\mathbf{F}]\forall i\in\mathcal{I},
  \end{cases}\implies\mathcal{E}_{\pi}[\mathbf{F}]\succeq\min\{\chi\hat{\kappa},\min_{i\in\mathcal{{I}}}\kappa_{i}\}\mathbf{Var}_{\pi}[\mathbf{F}]
\end{align*}
Since we did not assume anything about our function $\mathbf{F}$, we get the desired conclusion.
\end{proof}

We will also need the following estimate on the quality of the coupling. Since the proof does not depend on the function (and hence there is no difference in the scalar and matrix valued case), we present the lemma without proof.
\begin{lemma}{[Crude lower-bound on $\chi$, Lemma 2 in \cite{HS19}]} We always have
  \begin{align*}
    \frac{\pi(x) Q(x,y)}{\hat{\pi}(i) \hat{Q}(i,j)\kappa_{ij}(x,y)}\geq \max\bigg\{\frac{Q(x,y)}{\hat{Q}(i,j)},\frac{Q(y,x)}{\hat{Q}(j,i)}\bigg\}
  \end{align*}
\end{lemma}

\subsection{Proof of Theorem \ref{thm:mpc}}


  

To prove Theorem \ref{thm:mpc}, we will first need to use the inductive framework to prove some functional-analytic estimates for SCP measures.

  
    
  
  



  



  
  
  \begin{lemma}\label{lem:2stPI} Given a generator $\hat{Q}$ for a two state $(\{ 0,1\})$ chain. We have for any $\mathbf{F}:\{ 0,1\}\rightarrow \mathbb{S}_d$,
    \begin{align*}
      (a+b)\mathbf{Var}[\mathbf{F}]\preceq \mathcal{E}_{\hat{Q}}[\mathbf{F},\mathbf{F}]
    \end{align*}
  \end{lemma}
  \begin{proof}
    It is easy to prove that for a Markov chain with generator Q, the stationary distribution $\pi$ satisfies $\pi(1)=\frac{a}{a+b}$ and $\pi(0)=\frac{b}{a+b}$.
    Now we can focus on understanding the Dirichlet form and variance of any matrix valued function $\mathbf{F}$ .
    \begin{align*}
      \mathcal{E}[\mathbf{F},\mathbf{F}] &= \frac{b}{a+b}\cdot a(\mathbf{F}(0)-\mathbf{F}(1))^2\\
      \mathbf{Var}[\mathbf{F}] &= \mathbb{E}[\mathbf{F}^2] - (\mathbb{E}[\mathbf{F}])^2\\
      &=\frac{1}{a+b}(b\mathbf{F}(0)^2 + a\mathbf{F}(1)^2) - \frac{1}{(a+b)^2}(b\mathbf{F}(0) + a\mathbf[F](1))^2\\
      &=\frac{ab}{(a+b)^2}(\mathbf{F}(0)-\mathbf{F}(1))^2
    \end{align*}
    which concludes that the Poincare constant is $(a+b)$
  \end{proof}
We will also need the following lemma which characterizes the quality of the couplings for SCP measures.
\begin{lemma}{[Exploiting the SCP, Lemma 4 in \cite{HS19}]}\label{lem:lem4} If $\pi$ has the SCP, then there is a coupling $\kappa$ of $\pi_0, \pi_1$ supported on
  \begin{align*}
    \{(x,y)\in \Omega_0 \times \Omega_1 : x \sim y\}
  \end{align*}
  In particular, taking $\kappa_{01}$ and $\kappa_{10}$ to be $\kappa$ and its transpose respectively, we obtain
  \begin{align*}
    \chi \geq \frac{\overline{\mathscr{M}}(Q)}{\max\{a,b\}}
  \end{align*}
  where $\overline{\mathscr{M}}(Q) = \min\limits_{\substack{x,y\in\Omega\\x\sim y}}\max\{Q(x,y),Q(y,x)\}$
\end{lemma}



  



  




  


We will now prove theorem \ref{thm:mpc}.
\begin{proof}{[of Theorem \ref{thm:mpc}]} The proof is unchanged from the proof in \cite{HS19}. We will induct on the number of elements $n$. We will change the normalization of the generator : For any distribution $\pi$ on $\{0,1\}^n$ with the SCP, our goal is to prove the existence of a flip-swap walk $Q$ for $\pi$ such that $\lambda(Q)\geq 1$ and $\Delta(Q)\leq \begin{cases}
n& \text{always}\\
2k&\text{ if } \pi \text{ is k-homogenous}
\end{cases}$
Once we have established this, after dividing $Q$ by $\Delta(Q)$, we will be done.
As before, take a coordinate $\ell\in[n]$ and define the sets $\Omega_0 = \{x\in\Omega : x_\ell =0\}$ and $\Omega_1 = \{x\in\Omega : x_\ell = 1\}$ are both non-empty. We now consider the projection and restriction chains. Let their stationary distributions be $\hat{\pi},\pi_0,\pi_1$ respectively. We can of course view $\pi_0,\pi_1$ as distributions on $\{ 0,1 \}^{n-1} $ and both distributions are SCP. If $\pi$ is $k$-homogenous, then $\pi_0$ is also $k$-homogenous while $\pi_1$ is $(k-1)$-homogenous. Thus, using our induction hypothesis, we can say that there exists a flip-swap walk generator $Q_i$ for $\pi_i$ (for i=0,1) satisfying $\lambda(Q_i)\geq 1$ and $\Delta(Q_i)\leq \begin{cases}
n-1& \text{always}\\
2(k-i)&\text{ if } \pi \text{ is k-homogenous}
\end{cases}$
We also have, from Lemma \ref{lem:lem4}, a coupling $\kappa$ of $\pi_0$ and $\pi_1$ supported on $\{x\in\Omega_0,y\in\Omega_1 : x\sim y\}$.
\end{proof}
Hermon and Salez \cite{HS19} define the following flip-swap walk $Q$ for $\pi$ as follows : for $x\neq y \in\Omega$,
$Q(x,y)=\begin{cases}
Q_0(x,y) & \text{if } (x,y) \in \Omega_0\times\Omega_0\\
Q_1(x,y) & \text{if } (x,y) \in \Omega_1\times\Omega_1\\
\frac{\hat{\pi}(0)\hat{\pi}(1)\kappa(x,y)}{\pi(x)} & \text{if } (x,y) \in \Omega_0\times\Omega_1\\
\frac{\hat{\pi}(0)\hat{\pi}(1)\kappa(y,x)}{\pi(y)} & \text{if } (x,y) \in \Omega_1\times\Omega_0
\end{cases}$
and the diagonal is adjusted to make the row sums 0.
We will now use Lemma \ref{lem:recPI} with $\Omega_0,\Omega_1$ as our partition and the couplings $\kappa_{01}$ being $\kappa$ and $\kappa{10}$ being transpose of $\kappa$. We also have that the projection generator $\hat{Q}$ satisfies $\lambda(\hat{Q})\geq \hat{Q}(0,1)+\hat{Q}(1,0)$ from Lemma \ref{lem:2stPI}. We also have that for any $x\in\Omega_0, y\in\Omega_1$ with $\kappa(x,y)>0$,
\begin{align*}
  \frac{\pi(x)Q(x,y)}{\hat{\pi}(0)\hat{Q}(0,1)\kappa_{01}(x,y)} = \frac{\hat{\pi}(1)}{\hat{Q}(0,1)} =\frac{\hat{\pi}(0)}{\hat{Q}(1,0)} = \frac{\pi(y)Q(y,x)}{\hat{\pi}(1)\hat{Q}(1,0)\kappa_{01}(y,x)}
  \end{align*}
  where the second equality follows from reversibility. Hence, we get
  \begin{align*}
    \chi = \frac{\hat{\pi}(0)}{\hat{Q}(1,0)}=\frac{\hat{\pi}(1)}{\hat{Q}(0,1)}
  \end{align*}
  Finally combining the two inequalities above, we get
  \begin{align*}
    \chi\lambda(\hat{Q})\geq \hat{\pi}(0)+\hat{\pi}(1) = 1
  \end{align*}
  From our induction hypothesis, we had $\lambda(Q_i)\geq 1$, so we can use Lemma \ref{lem:recPI} to get that $\lambda(Q)\geq 1$. We just need to bound the diagonal of $Q$ now. For $x \in \Omega_0$, we have by construction
  \begin{align*}
    -Q(x,x)=\sum\limits_{y \in \Omega_0 \diagdown x}Q_0(x,y) + \frac{\hat{\pi}(0)\hat{\pi}(1)}{\pi(x)}\sum\limits_{y\in\Omega_1}\kappa(x,y)
  \end{align*}
Using the definition of $\Delta(Q_0)$ and the fact that the first marginal of $\kappa$ is $\pi_0$, we deduce that
\begin{align*}
  -Q(x,x) \leq \Delta(Q_0) + \hat{\pi}(1) = \Delta(Q_0)+\mathbb{E}_{\pi}[X_\ell]
\end{align*}
Similarly, if $x\in\Omega_1$, we have
\begin{align*}
  -Q(x,x) \leq \Delta(Q_1)+\hat{\pi}(0)\leq\Delta(Q_1)+x_\ell
\end{align*}
as $x_\ell=1$. So using the induction hypothesis on $\Delta(Q_i)$, we get that for all $x\in\Omega$,
\begin{align*}\Delta(Q)\leq \begin{cases}
n& \text{always}\\
2k+\mathbb{E}_\pi[X_\ell]-x_\ell&\text{ if } \pi \text{ is k-homogenous}
\end{cases}\end{align*}
Finally to bound the second line by $2k$, we average over the coordinate $\ell$. The generator will be written as $Q^{(\ell)}$ to denote the dependence on $\ell$.For each $ell\in[n]$, the construction of our generator produces a flip-swap walk $Q^{(\ell)}$ for $\pi$ which satisfies $\lambda(Q^{(\ell)})\geq 1$ and $\Delta(Q^{(\ell)})\leq n$. Now we crucially notice that the matrix valued variance is unchanged under averaging (because it doesnt depend on the generator) and the Dirchlet form has a linear dependence on the generator $Q^{(\ell)}$. Hence, $\lambda(Q)$ and $\Delta(Q)$ is preserved under convex combinations. So we can define an average generator $Q^*=\frac{1}{n}\sum\limits_{\ell=1}^{n}Q^{(\ell)}$ automatically satisfies $\lambda(Q^*)\geq 1$ and $\Delta(Q^*)\leq n$. If $\pi$ is $k$-homogenous, then for every $x\in\Omega$, we get
\begin{align*}
  -Q^*(x,x)=-\frac{1}{n}\sum\limits_{\ell=1}^{n}Q^{(\ell)}(x,x) \leq \frac{1}{n}\sum\limits_{\ell=1}^{n}(2k + \mathbb{E}[X_\ell] - x_\ell) = 2k
\end{align*}
Thus $Q^{*}$ satisfies our desired properties and we are done.
