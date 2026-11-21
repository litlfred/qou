---
doc_id: arxiv-1804.10084v1
doc_title: "Concentration of Lipschitz Functions of Negatively Dependent Variables"
section_id: sec-004-31-adaptive-martingale-analysis
section_title: "Adaptive martingale analysis"
section_number: 3.1
pages: 4-8
source_pdf: 1804.10084v1.pdf
source_sha256: 716da9708f06d930
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.996
doc_brief: "Concentration of Lipschitz Functions of Negatively Dependent Variables — We explore the question whether Lipschitz functions of random variables under various forms of negative correlation satisfy"
---
As we show in Appendix [\[app:error\]](#app:error){reference-type="ref" reference="app:error"}, it is not possible to replicate the martingale analysis of McDiarmid's inequality under negative regression, if we work with a fixed ordering of variables $X_1,\ldots,X_n$. The problem is that a particular variable $X_1$ might have a large influence on the distribution of the remaining variables, and hence affect significantly the conditional expectation of $f$ once the value of $X_1$ is revealed.

Our way around this issue is that we can choose variables *adaptively*, in order to construct a martingale with bounded differences. Our goal is to choose a variable that does not affect the remaining variables too heavily. Due to negative regression, we know that conditioning on $X_i=1$ can only affect the remaining variables negatively. Hence the only thing we have to worry about is that this negative effect is too large. However, the following lemma shows that there always exists a variable whose negative influence on the remaining variables is not too large.

::: lemma
[]{#lem:pick label="lem:pick"} Let $X_1, \ldots, X_n$ be $\{0,1\}$ random variables. Fix $K \subset [n]$ and $a_K \in \{0,1\}^K$ such that $Pr[X_K=a_K] > 0$. Then there exists $i \in [n] \setminus K$ such that either $X_i$ conditioned on $X_K=a_K$ is deterministic, or $$\sum_{\ell \in [n] \setminus (K \cup \{i\})} \left( {\mathbb E}[ X_\ell \mid X_K = a_K, X_i = 0] - {\mathbb E}[ X_\ell \mid X_K = a_K, X_i = 1] \right) \leq 1.$$
:::

::: proof
*Proof.* Let us denote $L = [n] \setminus K$. We consider the following quantity: $$\begin{aligned}
\mathsf{Var}\big[\sum_{i \in L} X_i \mid X_K=a_K\big] 
 = \sum_{i \in L} \left( \mathsf{Var}[X_i \mid X_K=a_K] + \sum_{j \in L \setminus \{i\}} \mathsf{Cov}[X_i, X_j \mid X_K=a_K] \right).
\end{aligned}$$ Variance is always nonnegative, so at least one term of the summation over $i \in L$ must be non-negative: $$\label{eq:1}
\mathsf{Var}[X_i \mid X_K=a_K] + \sum_{j \in L \setminus \{i\}} \mathsf{Cov}[X_i, X_j \mid X_K=a_K] \geq 0.$$ Let us denote $\pi_i = \Pr[X_i=1 \mid X_K=a_K]$. We can write $$\mathsf{Var}[X_i \mid X_K=a_K] = {\mathbb E}[X_i^2 \mid X_K=a_K] - ({\mathbb E}[X_i \mid X_K=a_k])^2 = \pi_i (1-\pi_i)$$ and $$\begin{aligned}
\mathsf{Cov}[X_i,X_j \mid X_K=a_K] & = & {\mathbb E}[X_i X_j \mid X_K=a_K] - {\mathbb E}[X_i \mid X_K=a_K] \, {\mathbb E}[X_j \mid X_K=a_K] \\
 & = & \pi_i ( {\mathbb E}[X_j \mid X_K=a_K, X_i=1] - {\mathbb E}[X_j \mid X_K=a_K] ).
\end{aligned}$$ Since ${\mathbb E}[X_j \mid X_K=a_K] = \pi_i  {\mathbb E}[X_j \mid X_K=a_K, X_i=1] + (1-\pi_i)  {\mathbb E}[X_j \mid X_K=a_K, X_i=0]$, we can rewrite this as $$\begin{aligned}
\mathsf{Cov}[X_i,X_j \mid X_K=a_K] = \pi_i (1-\pi_i) ( {\mathbb E}[X_j \mid X_K=a_K, X_i=1] -  {\mathbb E}[X_j \mid X_K=a_K, X_i=0]).
\end{aligned}$$ If $\pi_i=0$ or $\pi_i=1$, then $X_i$ conditioned on $X_K=a_K$ is deterministic, and we are done. Otherwise, substitute the expressions for $\mathsf{Var}[X_i \mid X_K=a_K]$ and $\mathsf{Cov}[X_i,X_j \mid X_K=a_K]$ in ([\[eq:1\]](#eq:1){reference-type="ref" reference="eq:1"}), divide by $\pi_i (1-\pi_i)$, and conclude that $$\sum_{\ell \in L \setminus \{i\}} \left( {\mathbb E}[ X_\ell \mid X_K = a_K, X_i = 0] - {\mathbb E}[ X_\ell \mid X_K = a_K, X_i = 1] \right) \leq 1.$$ ◻
:::

Next, we show that conditioning on $X_i$ indeed cannot affect the conditional expectation of $f$ too much. To prove this, we need one more tool, which is Strassen's monotone coupling theorem (easily proved from the max-flow min-cut theorem).

::: theorem
Consider two probability measures $\mu^{(0)}$ and $\mu^{(1)}$ on $\{0,1\}^L$. Suppose that for every down-closed $M \subset \{0,1\}^L$, $\mu^{(1)}(M) \geq \mu^{(0)}(M)$. Then there exists a coupling $\nu:\{0,1\}^L \times \{0,1\}^L \rightarrow [0,1]$ such that: $$\mu^{(1)}(x) = \sum_y \nu(x, y),$$ $$\mu^{(0)}(y) = \sum_x \nu(x, y),$$ and $\nu(x, y) = 0$ unless $x \leq y$ coordinate-wise.
:::

I.e., if $\mu^{(1)}$ dominates $\mu^{(0)}$ on every down-closed event, then it is possible to transform $\mu^{(0)}$ into $\mu^{(1)}$ in such a way that we only transfer probability mass *downwards* in $\{0,1\}^L$. From the condition of negative regression and Strassen's theorem, we get immediately the following.

::: corollary
[]{#cor:coupling label="cor:coupling"} For random variables $X_1,\ldots,X_n$ satisfying negative regression, $K \subset [n]$, $a_K \in \{0,1\}^K$, and $i \in [n] \setminus K$ such that $\Pr[X_K=a_k, X_i=0] > 0$, $\Pr[X_K=a_k, X_i=1] > 0$, there exists a coupling $\nu:\{0,1\}^L \times \{0,1\}^L \rightarrow [0,1]$ for $L = [n] \setminus (K \cup \{i\})$ such that $$\mu^{(1)}(a_L) = \Pr[X_L=a_L \mid X_K=a_K, X_i=1] = \sum_y \nu(a_L,y),$$ $$\mu^{(0)}(b_L) = \Pr[X_L=b_L \mid X_K=a_K, X_i=0] = \sum_x \nu(x,b_L),$$ and $\nu(x,y) = 0$ unless $x \leq y$.
:::

Now we are ready to construct a martingale with bounded differences. We formalize this as follows.

::: lemma
[]{#lem:martingale label="lem:martingale"} Given $\{0,1\}$ random variables $X_1,\ldots,X_n$ satisfying negative regression, and a $1$-Lipschitz function $f:\{0,1\}^n \rightarrow {\mathbb R}$, there exists an adaptive ordering (random permutation) $\pi(1), \pi(2), \ldots, \pi(n)$ such that:

::: compactitem
$\pi(1)$ is deterministic.

For each $1 \leq k<n$, $\pi(k+1)$ is determined by $\pi([k]) = \{\pi(1),\ldots,\pi(k)\} = K$ and $X_K = a_K$.

If we denote $Y_k = {\mathbb E}[f(X) \mid \pi([k]),X_{\pi([k])}]$, then $Y_0,Y_1,\ldots,Y_n$ is a martingale.

Conditioned on $\pi([k])=K, X_K=a_K$, there are $\alpha<\beta, \beta-\alpha \leq 2$, such that $Y_{k+1} - Y_k \in [\alpha,\beta]$ with prob. $1$.

For monotone $f$, $Y_{k+1} - Y_k \in [\alpha,\beta]$ where $\beta-\alpha \leq 1$.
:::
:::

::: proof
*Proof.* Let us fix $\pi([k]) = K$ and $X_K = a_K$. Given this conditioning, there exists $i \in [n] \setminus K$ as provided by Lemma [\[lem:pick\]](#lem:pick){reference-type="ref" reference="lem:pick"}. Let us define $\pi(k+1)$ to be the minimum index $i$ satisfying the conclusion of Lemma [\[lem:pick\]](#lem:pick){reference-type="ref" reference="lem:pick"}.

Now let us consider $Y_k = {\mathbb E}[f(X) \mid \pi([k])=K,X_K=a_K]$. Under this conditioning, $\pi(k+1)$ is deterministic and $X_{\pi(k+1)}$ could take two possible values ($0$ or $1$) which determines the value of $Y_{k+1}$. By construction, $Y_k = {\mathbb E}_{X_{\pi(k+1)}}[Y_{k+1} \mid \pi([k])=K, X_K=a_K]$. By averaging over all possible choices of $K$ and $a_K$ consistent with the same value of $Y_k$, we also get $Y_k = {\mathbb E}[Y_{k+1} \mid Y_k]$; i.e., the sequence $Y_0,Y_1,\ldots,Y_n$ forms a martingale.

Our goal now is to analyze how much $Y_{k+1}$ can deviate from $Y_k$. In the following we fix $\pi([k])=K$ and $X_K = a_K$. We have $Y_k = {\mathbb E}[f(X) \mid \pi([k])=K, X_K=a_K]$. Recall that this conditioning also determines the choice of $\pi(k+1)$ (but of course not the value of $X_{\pi(k+1)}$). If $X_{\pi(k+1)}$ attains only one possible value under this conditioning, then $Y_{k+1} = Y_k$ and we are done --- hence, let us assume that both values of $X_{\pi(k+1)}$ occur with positive probability. For $c=0,1$, let us denote $$Y_{k+1}^{(c)} = {\mathbb E}[f(X) \mid \pi(1),\ldots,\pi(k), \pi(k+1), X_{\pi(1)}, \ldots,X_{\pi(k)}; X_{\pi(k+1)}=c].$$ We claim that $|Y_{k+1}^{(1)} - Y_{k+1}^{(0)}| \leq 2$, and in the case of monotone $f$, $|Y_{k+1}^{(1)} - Y_{k+1}^{(0)}| \leq 1$; showing this will complete the proof.

Let $L = [n] \setminus \pi([k+1]) = [n] \setminus (K \cup \{ \pi(k+1) \})$. Denote by $\mu^{(c)}$ the probability distribution of $X_L \in \{0,1\}^L$ conditioned on $\pi([k])=K$, $X_K=a_K$, and $X_{\pi(k+1)} = c \in \{0,1\}$. By Corollary [\[cor:coupling\]](#cor:coupling){reference-type="ref" reference="cor:coupling"}, there is a monotone coupling $\nu(x,y)$ between $\mu^{(1)}$ and $\mu^{(0)}$. We can write $$\begin{aligned}
Y^{(1)}_{k+1} & = & {\mathbb E}[f(X) \mid \pi([k])=K, X_K=a_K, X_{\pi(k+1)}=1] \\
& = & \sum_{a_L \in \{0,1\}^L} \mu^{(1)}(a_L) \, f(X_K=a_K, X_{\pi(k+1)}=1, X_L=a_L) \\
& = & \sum_{a_L,b_L \in \{0,1\}^L} \nu(a_L,b_L) \, f(X_K=a_K, X_{\pi(k+1)}=1, X_L=a_L).
\end{aligned}$$ Similarly, $$\begin{aligned}
Y^{(0)}_{k+1} & = & {\mathbb E}[f(X) \mid \pi([k])=K, X_K=a_K, X_{\pi(k+1)}=0] \\
& = & \sum_{b_L \in \{0,1\}^L} \mu^{(0)}(b_L) \, f(X_K=a_K, X_{\pi(k+1)}=0, X_L=b_L) \\
& = & \sum_{a_L, b_L \in \{0,1\}^L} \nu(a_L,b_L) \, f(X_K=a_K, X_{\pi(k+1)}=0, X_L=b_L).
\end{aligned}$$ Now we can compare the values of $f$ in the two expressions. First we modify the coordinate $X_{\pi(k+1)}$, and then the remaining coordinates $X_L$. Since $f$ is $1$-Lipschitz, we have $$\abs{f(X_K=a_K, X_{\pi(k+1)}=1, X_L=a_L) - f(X_K=a_K, X_{\pi(k+1)}=0, X_L=a_L)} \leq 1.$$ Next, since $a_L \leq b_L$ in all the terms with $\nu(a_L,b_L) > 0$, we have $$\abs{f(X_K=a_k, X_{\pi(k+1)}=0, X_K=a_L) - f(X_K=a_k, X_{\pi(k+1)}=0, X_K=b_L)} \leq \| b_L \|_1 - \| a_L \|_1.$$ By the triangle inequality, $$\abs{f(X_K=a_k, X_{\pi(k+1)}=1, X_K=a_L) - f(X_K=a_k, X_{\pi(k+1)}=0, X_K=b_L)} \leq 1 + \| b_L \|_1 - \| a_L \|_1.$$ Hence $$\begin{aligned}
 \abs{Y^{(1)}_{k+1} - Y^{(0)}_{k+1}} & \leq & \sum_{a_L,b_L \in \{0,1\}^L} \nu(a_L,b_L) (1 + \|b_L\|_1 - \|a_L\|_1) \\
  & = & 1 + \sum_{b_L \in \{0,1\}^L} \mu^{(0)}(b_L) \, \| b_L \|_1 - \sum_{a_L \in \{0,1\}^L} \mu^{(1)}(a_L)\,  \| a_L \|_1 \\
  & = & 1 + \sum_{\ell \in L} {\mathbb E}[X_\ell \mid X_K=a_K, X_{\pi(k+1)}=0] - \sum_{\ell \in L} {\mathbb E}[X_\ell \mid X_K=a_K, X_{\pi(k+1)}=1]
\end{aligned}$$ by the properties of $\mu^{(0)}, \mu^{(1)}$ and $\nu$. Finally, we recall that $\pi(k+1)$ was chosen so as to satisfy the conclusion of Lemma [\[lem:pick\]](#lem:pick){reference-type="ref" reference="lem:pick"}: $$\sum_{\ell \in L} {\mathbb E}[X_\ell \mid X_K=a_K, X_{\pi(k+1)}=0] - \sum_{\ell \in L} {\mathbb E}[X_\ell \mid X_K=a_K, X_{\pi(k+1)}=1] \leq 1.$$ This concludes the proof that $|Y^{(1)}_{k+1} - Y^{(0)}_{k+1}| \leq 2$.

In the case of monotone $f$, we observe that we can improve some of the inequalities: we get $$0 \leq f(X_K=a_K, X_{\pi(k+1)}=1, X_L=a_L) - f(X_K=a_K, X_{\pi(k+1)}=0, X_L=a_L) \leq 1$$ and $$0 \geq f(X_K=a_k, X_{\pi(k+1)}=0, X_K=a_L) - f(X_K=a_k, X_{\pi(k+1)}=0, X_K=b_L)| \geq \| a_L \|_1 - \| b_L \|_1$$ whenever $a_L \leq b_L$. This implies that $$1 \geq f(X_K=a_k, X_{\pi(k+1)}=1 X_K=a_L) - f(X_K=a_k, X_{\pi(k+1)}=0, X_K=b_L) \geq \| a_L \|_1 - \| b_L \|_1$$ and by the same computations as above, we conclude that $1 \geq Y^{(1)}_{k+1} - Y^{(0)}_{k+1} \geq -1$. ◻
:::

Theorem [\[thm:Lipschitz-R\]](#thm:Lipschitz-R){reference-type="ref" reference="thm:Lipschitz-R"} now follows by standard exponential moment analysis; see for example [@McDiarmid89]. For completeness, we summarize the rest of the analysis as follows.

::: proof
*Proof of Theorem [\[thm:Lipschitz-R\]](#thm:Lipschitz-R){reference-type="ref" reference="thm:Lipschitz-R"}.* For a parameter $\lambda \in {\mathbb R}$, we estimate the exponential moment ${\mathbb E}[e^{\lambda f(X_1,\ldots,X_n)}] = {\mathbb E}[e^{\lambda Y_n}]$. Inductively, we prove that ${\mathbb E}[e^{\lambda (Y_k - Y_0)}] \leq e^{k \lambda^2 / 2}$ (for monotone $f$, the bound improves to $e^{k \lambda^2 / 8}$). The inductive step is that $${\mathbb E}[e^{\lambda (Y_{k+1} - Y_k)} \mid \pi([k])=K, X_K=a_K] \leq e^{\lambda^2 / 2}$$ which is true because under this conditioning, $Y_{k+1} - Y_k$ is a random variable of expectation $0$, confined to an interval of length $2$ (see Lemma [\[lem:martingale\]](#lem:martingale){reference-type="ref" reference="lem:martingale"}). It is known that the exponential moment of such a variable is upper-bounded by $e^{\lambda^2 / 2}$. By averaging over all choices of $K$ and $a_K$ that yield the same value of $Y_k$, we also obtain ${\mathbb E}[e^{\lambda (Y_{k+1} - Y_k)} \mid Y_k] \leq e^{\lambda^2 / 2}.$ In the case of $f$ monotone, $Y_{k+1} - Y_k$ is confined to an interval of length $1$ and the exponential moment is upper-bounded by $e^{\lambda^2 / 8}$.

From here, by induction, we obtain $${\mathbb E}[e^{\lambda (Y_{k+1} - Y_0)}] = {\mathbb E}_{Y_k}[ {\mathbb E}_{Y_{k+1}}[e^{\lambda (Y_{k+1} - Y_k)} \mid Y_k] \ e^{\lambda (Y_k-Y_0)}] \leq e^{\lambda^2 / 2} \ {\mathbb E}_{Y_k}[e^{\lambda(Y_k-Y_0)}] \leq e^{(k+1) \lambda^2 / 2}.$$ Therefore, ${\mathbb E}[e^{\lambda (Y_n - Y_0)}] \leq e^{n \lambda^2 / 2}$. (For $f$ monotone, the bound improves to $e^{n \lambda^2 / 8}$.)

Recall that $Y_0 = {\mathbb E}[f(X_1,\ldots,X_n)] = \mu$. By Markov's inequality applied to the exponential moment, we get $$\Pr[f(X_1,\ldots,X_n) > \mu+t] = \Pr[e^{\lambda (Y_n - Y_0)} \geq e^{\lambda t}] \leq \frac{{\mathbb E}[e^{\lambda (Y_n-Y_0)}]}{e^{\lambda t}} = e^{n \lambda^2 / 2 - \lambda t}.$$ The choice of $\lambda = t/n$ gives the upper-tail bound in Theorem [\[thm:Lipschitz-R\]](#thm:Lipschitz-R){reference-type="ref" reference="thm:Lipschitz-R"}; the other bounds follow similarly. ◻
:::
