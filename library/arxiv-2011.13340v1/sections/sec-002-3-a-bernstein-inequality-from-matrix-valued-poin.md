---
doc_id: arxiv-2011.13340v1
doc_title: "A Matrix Bernstein Inequality for Strong Rayleigh Distributions *"
section_id: sec-002-3-a-bernstein-inequality-from-matrix-valued-poin
section_title: "A Bernstein Inequality from Matrix valued Poincare inequalities"
section_number: 3
pages: 10-15
source_pdf: 2011.13340v1.pdf
source_sha256: e73876ed2c923608
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.982
doc_brief: "A Matrix Bernstein Inequality for Strong Rayleigh Distributions * — The Entropy method provides a powerful framework for proving scalar concentration in- equalities by establishing functional"
---
In this section we show how to use Matrix valued Poincare inequalities to obtain matrix Bernstein style inequalities.

We will need a well-known monotonicity property of the trace exponential \cite{TroppIntro15}
\begin{lemma}
  \label{lem:trMonotone}
  For any monotone function $f$, for any Hermitian matrices $\bf{A}$ and $\bf{H}$ such that $\bf{A} \preceq \bf{H}$, then $\Tr\big[f(\mathbf{A})\big] \leq \Tr\big[ f(\mathbf{H})\big]$
\end{lemma}














The next lemma characterizes Jensen's inequality for matrices. The first statement about operator Jensen's inequality for matrices can be found in \cite{TroppIntro15}, while the Jensen inequality for the trace of a convex function is from \cite{HP03}
\begin{lemma}\label{lem:jensen} Given a decomposition of the identity of the form $\sum\limits_{i=1}^{n}\mathbf{K}_i^{*}\mathbf{K}_i = \mathbf{I}$ and an operator convex function $f$, we have for any set of Hermitian matrices $A_1,\ldots,A_n$,
  \begin{align*}
    f\bigg(\sum\limits_{i}^{n}\mathbf{K}_i^{*} \mathbf{A}_i\mathbf{K}_i\bigg) \preceq \sum\limits_{i}^{n}\mathbf{K}_i^{*}f(\mathbf{A}_i)\mathbf{K}_i
  \end{align*}
  For any convex function, we also have
  \begin{align*}
    \mathsf{Tr}\bigg[f\big(\sum\limits_{i}^{n}\mathbf{K}_i^{*}\mathbf{A}_i \mathbf{K}_i\big)\bigg]\leq \mathsf{Tr}\bigg[\sum\limits_{i=1}^{n}\mathbf{K}_i^{*}f(\mathbf({A}_i)\mathbf{K}_i\bigg]
  \end{align*}
\end{lemma}

Finally, we will need the following matrix identities which we will use to establish a mean value theorem for the Dirichlet form.

\begin{fact}{[Eqn 5.35 in \cite{Bhatia07}]}\label{fct:intNorm} Given any positive semi-definite $\mathbf{A},\mathbf{B}$, any Hermitian $\mathbf{X}$ and any unitarily invariant norm $\| \cdot \|$, we have
  \begin{align*}
    \bigg\|\small\intop_{0}^{1}\mathbf{A}^{t}\mathbf{XB}^{1-t}\mathrm{dt}\bigg\| \leq \frac{1}{2}\|\mathbf{AX} + \mathbf{XB}\|
  \end{align*}
\end{fact}

\begin{fact}{[Eqn 6.42 in \cite{Bhatia07}]}\label{fct:duhamel} For any Hermitian $\mathbf{X},\mathbf{Y}$, we have \begin{align*}
  e^\mathbf{X}-e^{\mathbf{Y}} = \intop_{0}^{1}e^{t\mathbf{X}}(\mathbf{X}-\mathbf{Y})e^{(1-t)\mathbf{Y}}\mathrm{dt}
\end{align*}
\end{fact}
\begin{lemma}\label{lem:var} Given random Hermitian matrices X and Y, we have
  \begin{align*}
    \mathsf{Tr}\big[ \mathbb{E}[(e^\mathbf{X}-e^\mathbf{Y})^2]\big]^p\leq \frac{1}{2}\mathbb{E}\big[\|\mathbf{X}-\mathbf{Y}\|^{2p}\mathsf{Tr}[e^{2p\mathbf{X}}+e^{2p\mathbf{Y}}]\big]
  \end{align*}
\end{lemma}
\begin{proof}
  We have
  \begin{align*}
    \mathsf{Tr}\big[ \mathbb{E}[(e^\mathbf{X}-e^\mathbf{Y})^2]\big]^p&\leq \mathbb{E}\big[\mathsf{Tr}\big[ (e^\mathbf{X}-e^\mathbf{Y})^{2p}\big] \ \ \ \text{(using Lemma \ref{lem:jensen})}\\
    &=\mathbb{E}\big[\mathsf{Tr}\big[ \intop_{0}^{1}e^{t\mathbf{X}}(\mathbf{X}-\mathbf{Y})e^{(1-t)\mathbf{Y}}\big]^{2p}\big] \ \ \ \text{(from Fact \ref{fct:duhamel}) }\\
    &=\mathbb{E}\bigg[\bigg\|\intop_{0}^{1}e^{t\mathbf{X}}(\mathbf{X}-\mathbf{Y})e^{(1-t)\mathbf{Y}}\bigg\|_{2p}^{2p}\bigg]&\\
    &\leq \mathbb{E}\bigg[\bigg(\frac{1}{2}\big\|e^{\mathbf{X}}(\mathbf{X-Y})+(\mathbf{X-Y})e^{\mathbf{Y}}\big\|_{2p}\bigg)^{2p}\bigg] \ \ \ \text{(using Fact \ref{fct:intNorm})}\\
    &\leq \mathbb{E}\bigg[\frac{1}{2^{2p}}\bigg(\big\|e^{\mathbf{X}}(\mathbf{X-Y})\big\|_{2p}+\big\|(\mathbf{X-Y})e^{\mathbf{Y}}\big\|_{2p}\bigg)^{2p}\bigg]\ \ \ \text{(using triangle inequality)}\\
    &\leq \mathbb{E}\bigg[\frac{1}{2}\bigg(\big\|e^{\mathbf{X}}(\mathbf{X-Y})\big\|_{2p}^{2p} + \big\|(\mathbf{X-Y})e^{\mathbf{Y}}\big\|_{2p}^{2p} \bigg)\bigg] \ \ \ \text{(using }(a+b)^p \leq 2^{p-1}(a^p + b^p) \ )\\
    &\leq \frac{1}{2}\mathbb{E}\bigg[\|X-Y\|^{2p}\big(\|e^{\mathbf{X}}\|_{2p}^{2p}+\|e^{\mathbf{Y}}\|_{2p}^{2p}\big)\\
    &=\frac{1}{2}\mathbb{E}\bigg[\|X-Y\|^{2p}\mathsf{Tr}\big[e^{2p\mathbf{X}}+e^{2p\mathbf{Y}}\big]\bigg]
  \end{align*}
\end{proof}
We now use this lemma to derive an upper bound on the trace power of the Dirichlet form.
\begin{lemma}\label{lem:dirichlet} Given a reversible Markov Chain with transition matrix $\mathbf{P}\in\mathbb{R}^{\Omega\times \Omega}$ and stationary measure $\mathbf{\pi}\in\mathbb{R}^{\Omega}$, any function $\mathbf{F} : \Omega \rightarrow \mathbb{S}_d$, we have
  \begin{align*}
    \mathsf{Tr}\big[\mathcal{E}(e^\mathbf{F}, e^\mathbf{F})\big]^p \leq v(F)^{2p} \mathsf{Tr}[\mathbb{E}_{x \sim \pi}[e^{2p\mathbf{F(x)}}]]
  \end{align*}
  where $v(F) = \max\limits_{\substack{x,y\in\Omega\\x\sim y}}\|\mathbf{F(x)}-\mathbf{F(y)}\|$
\end{lemma}
\begin{proof}

  Consider the trace power of the Dirchlet form,
  \begin{align*}
    \mathsf{Tr}\big[\mathcal{E}(e^\mathbf{F},e^\mathbf{F})\big]^p &= \mathsf{Tr}\big[\sum\limits_{x \in \Omega} \mathbb{\pi}_x \sum\limits_{y \in \Omega}\mathbf{P}_{xy}\big(e^\mathbf{F(x)}-e^\mathbf{F(y)}\big)^2\big]^p\\
     &\leq \sum\limits_{x\in\Omega}\pi_x\mathsf{Tr}\big[\sum\limits_{y \in \Omega}\mathbf{P}_{xy}\big(e^\mathbf{F(x)}-e^\mathbf{F(y)}\big)^2\big]^p \ \ \text{(using Lemma \ref{lem:jensen})}\\
    &\leq \frac{1}{2}\sum\limits_{x\in\Omega}\pi_x\sum\limits_{y\in\Omega}\mathbf{P}_{xy}\big(\|\mathbf{F(x)}-\mathbf{F(y)}\|^{2p}\mathsf{Tr}\big[e^{2p\mathbf{F(x)}}+e^{2p\mathbf{F(y)}}\big]\big)\big]\ \ \text{(using Lemma \ref{lem:var} with } \mathbf{X} = \mathbf{F(x)} \text{ and } \mathbf{Y} = \mathbf{F(y)}\text{ )}\\
    &\leq \frac{v(F)^{2p}}{2}\sum\limits_{x,y \in \Omega}\pi_x \mathbf{P}_{xy}\mathsf{Tr}[e^{2p\mathbf{F}(x)}+e^{2p\mathbf{F(y)}}]\\
    &\leq v(F)^{2p} \sum\limits_{x\in\Omega}\pi_x \mathsf{Tr}[e^{2p\mathbf{F(x)}}] \ \ \text{(using reversibility of \textbf{P})}\\
    &=v(F)^{2p} \mathsf{Tr}[\mathbf{E}_{x \sim \pi}[e^{2p\mathbf{F(x)}}]]
\end{align*}
\end{proof}
We are finally ready to use our Matrix valued Poincare inequality to prove our matrix concentration inequality. A standard method to prove matrix concentration uses the exponential moment generating function (mgf) which we state next.
\begin{proposition}{[Matrix Laplace Transform Method \cite{TroppIntro15}]}\label{prop:mgf} Let $\mathbf{X} \in \mathbb{H}_d$ be a random matrix with trace mgf $m(\theta) = \mathsf{Tr}[e^{\theta (\mathbf{X}-\mathbb{E}[\mathbf{X}])}]$. For every $t \in \mathbb{R}$,
  \begin{align*}
    \mathsf{Pr}[\|\mathbf{X}-\mathbb{E}[\mathbf{X}]\|\geq t] \leq 2 \inf\limits_{\theta > 0}e^{-\theta t + \log(m(\theta))}
  \end{align*}
\end{proposition}
Hence, to get our concentration inequality, we just need to get a bound on the moment generating function.
\begin{theorem}\label{thm:mgfBound}
Given a reversible Markov Chain with transition matrix $\mathbf{P}\in\mathbb{R}^{\Omega \times \Omega}$ and its stationary distribution $\pi\in \mathbb{R}^{\Omega}$, any function $\mathbf{F} : \Omega \rightarrow \mathbb{S}_d$ such that it satisfies the Matrix valued Poincare inequality with constant $\lambda$, we have
\begin{align*}\mathsf{Pr}_{x \sim \pi}[\|\mathbf{F}(x)-\mathbb{E}_{y \sim \pi}[\mathbf{F(y)}]\|\geq t] \leq 2d e^{-t^2/4(v(\mathbf{F})^2/\lambda + tv(\mathbf{F})/\sqrt{\lambda})}\end{align*}
  where $v(F) = \max\limits_{\substack{x,y\in\Omega\\x\sim y}}\|\mathbf{F(x)}-\mathbf{F(y)}\|$
\end{theorem}

\begin{proof}
  For notational convenience, we will write $\lambda$ as the inverse of the actual $\lambda$ value. Hence, our Poincare inequality now looks like $\mathbf{Var}[\mathbf{F}]\preceq\lambda\mathcal{E}[\mathbf{F},\mathbf{F}]$To use Proposition \ref{prop:mgf}, we need an upper bound on the mgf. The statement we want to prove, via induction, is \begin{equation}\label{eqn:indStmt}
  (1-\lambda v(F)^2 S_k )\mathsf{Tr}\big[\mathbb{E}[e^{\mathbf{F(x)}}]\big]\leq  \mathsf{Tr}[\mathbb{E}[e^{\mathbf{F(x)}/2^k}]]^{2^k}
\end{equation}

where $\lambda v(\mathbf{F})^2 \leq 1$ and $S_k = \sum\limits_{i=1}^{k}1/2^i$ which tends to 1 as $k \rightarrow \infty$.
Assuming the induction hypothesis, consider the RHS where $n=2^k$
\begin{align*}
  \mathsf{Tr}[\mathbb{E}[e^{\mathbf{F(x)}/n}]]^n&=\mathsf{Tr}[\sum\limits_{x \in \Omega}\pi_x (1+\mathbf{F(x)}/n + (\mathbf{F(x)}/n)^2/2!+\ldots)]^n\\
  &=\mathsf{Tr}[(1 + \mathbb{E}[F(x)]/n)^n] \rightarrow \mathsf{Tr}[e^{\mathbb{E}\mathbf[F(x)]}]
\end{align*}
where the second inequality follows as we can ignore the second order terms and beyond for $n\rightarrow \infty$.
Now notice that for any $\beta > 0$, we have $v(\beta \mathbf{F}) = \beta v(\mathbf{F})$. Now taking $\theta \mathbf{F}$ in place of $\mathbf{F}$ and the requirement of $\lambda v(\theta \mathbf{F})^2 \leq 1$ translates to $\theta^2 \lambda v(\mathbf{F})^2 \leq 1$, we plug this into Equation \ref{eqn:indStmt}, to get
\begin{equation}\label{eqn:mgfB}
  \mathsf{Tr}\big[\mathbb{E}_{x \sim \pi}[e^{\theta\mathbf{F(x)}}]\big]\leq \frac{\mathsf{Tr}[e^{\theta\mathbb{E}_{x \sim \pi}[\mathbf{F(x)}]}]}{1-\theta^2\lambda v(\mathbf{F})^2}
\end{equation}
Now, using Equation \ref{eqn:mgfB} with $\mathbf{F}$ being $\mathbf{F}-\mathbb{E}[\mathbf{F}]$ which is zero mean and noticing that $v(\mathbf{F}-\mathbb{E}[\mathbf{F}]) = v(\mathbf{F})$, we get that
\begin{equation}\label{eqn:mgfBo}
  \mathsf{Tr}\big[\mathbb{E}_{x \sim \pi}[e^{\theta\mathbf{F(x)}}]\big]\leq \frac{d}{1-\theta^2\lambda v(\mathbf{F})^2}
\end{equation}
Now, in the RHS for Proposition \ref{prop:mgf}, we have
\begin{align*}
  2\inf\limits_{\theta>0}e^{-\theta t + \log m(\theta)}&\leq 2\inf\limits_{\theta^2 \lambda v(\mathbf{F})^2\leq 1}e^{-\theta t + \log m(\theta)}\\
  &=2d\inf\limits_{\theta^2 \lambda v(\mathbf{F})^2\leq 1}e^{-\theta t - \log(1-\theta^2 \lambda v(\mathbf{F})^2)}\\
  &\leq 2d\inf\limits_{\theta^2 \lambda v(\mathbf{F})^2\leq 1}e^{-\theta t +\lambda v(\mathbf{F})^2\theta^2 + \frac{\lambda^2 v(\mathbf{F})^4\theta^4}{2(1-\lambda v(\mathbf{F})^2\theta^2)}}\\
\end{align*}
Differentiating w.r.t $\theta$ and setting to zero, we get that the probability is upper bounded by $2de^{-t^2/4(\lambda v(\mathbf{F})^2)+t \sqrt{\lambda}v(\mathbf{F}))}$ and we would be done.

Now, it just remains to prove the induction statement. Our proof proceeds by a doubling trick to transform the variance of $e^\mathbf{F}$ to the exponential moment generating function. We first prove the base case. Consider $k=1$ and consider the function $\mathbf{f}=\mathbf{F}/2$. Using the matrix valued Poincare inequality on $e^\mathbf{f}$, we have
\begin{align*}
  &\mathbf{Var}(e^\mathbf{f}) = \lambda \mathcal{E}(e^\mathbf{f},e^{\mathbf{f}})\\
  \implies&\mathbb{E}[e^\mathbf{2f}] \preceq (\mathbb{E}[e^\mathbf{f}])^2 + \mathcal{E}(e^\mathbf{f},e^{\mathbf{f}})\\
  &\mathbb{E}[e^\mathbf{F}] \preceq (\mathbb{E}[e^\mathbf{f}])^2 + \mathcal{E}(e^\mathbf{f},e^{\mathbf{f}})
\end{align*}
Taking trace on both sides, we have
\begin{align*}
  \mathsf{Tr}[\mathbb{E}[e^\mathbf{F}]]&\leq \mathsf{Tr}[(\mathbb{E}[e^{\mathbf{F}/2}])^2] + \mathsf{Tr}[\mathcal{E}(e^{\mathbf{F}/2},e^{\mathbf{F}/2})]\\
  &\leq \mathsf{Tr}[(\mathbb{E}[e^{\mathbf{F}/2}])^2] + v(\mathbf{F}/2)^2\mathsf{Tr}[\mathbb{E}_{x\sim\pi}[e^{\mathbf{F}}]] \ \ \text{(using Lemma \ref{lem:dirichlet})}\\
  &=\mathsf{Tr}[(\mathbb{E}[e^{\mathbf{F}/2}])^2] + \frac{v(\mathbf{F})^2}{4}\mathsf{Tr}[\mathbb{E}_{x\sim\pi}[e^{\mathbf{F}}]]\\
  &\leq \mathsf{Tr}[(\mathbb{E}[e^{\mathbf{F}/2}])^2] + \frac{\lambda v(\mathbf{F})^2 S_1}{2}\mathsf{Tr}[\mathbb{E}_{x\sim\pi}[e^{\mathbf{F}}]] \ \ \text{(using }\lambda \geq 1\text{ and } S_1 = 1/2\text{ )}\\
  \hspace{0.5em}\bigg(1-\frac{\lambda v(\mathbf{F})^2 S_1}{2}\bigg)\mathsf{Tr}[\mathbb{E}[e^\mathbf{F}]] &\leq  \mathsf{Tr}[(\mathbb{E}[e^{\mathbf{F}/2}])^2]
\end{align*}
which establishes our base case.
Now assume the induction hypothesis for k-1 and consider the function $\mathbf{f}=\mathbf{F}/2^k$. Denote $v_k = v(\mathbf{F}/2^{k}) = v(\mathbf{F})/2^k$ Using the matrix valued Poincare inequality on $e^\mathbf{f}$ and taking trace to the power $p=2^{k-1}$, we get,
\begin{align*}
  \mathsf{Tr}\big[\mathbb{E}[e^{\mathbf{F}/{2^{k-1}}}]\big]^{2^{k-1}} &\leq \mathsf{Tr}\big[(\mathbb{E}[e^{\mathbf{F}/2^{k}}])^2 + \lambda\mathcal{E}(e^{\mathbf{F}/2^k},e^{\mathbf{F}/2^k})\big]^{2^{k-1}}\\
  &=\mathsf{Tr}\big[(1-\lambda v_k^2 )\frac{(\mathbb{E}[e^{\mathbf{F}/2^{k}}])^2}{(1-\lambda v_k^2)} + \lambda v_k^2)(\mathcal{E}(e^{\mathbf{F}/2^k},e^{\mathbf{F}/2^k})/v_k^2)\big]^{2^{k-1}}\\
  &\leq \frac{\mathsf{Tr}\big[\mathbb{E}[e^{\mathbf{F}/2^{k}}]\big]^{2^k}}{(1-\lambda v_k)^{2^{k-1}-1}} + \lambda v_k^2\mathsf{Tr}\big[(\mathcal{E}(e^{\mathbf{F}/2^k},e^{\mathbf{F}/2^k})/v_k^2)\big]^{2^{k-1}}\ \ \text{(using Jensen's inequality as }\lambda v_k^2 \leq 1 \text{ )}\\
  &\leq \frac{\mathsf{Tr}\big[\mathbb{E}[e^{\mathbf{F}/2^{k}}]\big]^{2^k}}{(1-\lambda v_k^2)^{2^{k-1}-1}} + \lambda v_k^2\mathsf{Tr}[\mathbb{E}_{x \sim \pi}[e^{\mathbf{F}}]] \ \ \text{(using Lemma \ref{lem:dirichlet})}
\end{align*}
Now using the induction hypothesis, we can lower bound the LHS above to get,
\begin{align*}
  (1-\lambda v(F)^2 S_{k-1})\mathsf{Tr}[\mathbb{E}_{x\sim\pi}[e^\mathbf{F}]] &\leq \frac{\mathsf{Tr}\big[\mathbb{E}[e^{\mathbf{F}/2^{k}}]\big]^{2^k}}{(1-\lambda v_k^2)^{2^{k-1}-1}}+ \lambda v_k^2\mathsf{Tr}[\mathbb{E}_{x \sim \pi}[e^{\mathbf{F}}]]\\
  (1-\lambda v(F)^2 S_{k-1}-\lambda v_k^2)\mathsf{Tr}[\mathbb{E}_{x\sim\pi}[e^\mathbf{F}]]&\leq \frac{\mathsf{Tr}\big[\mathbb{E}[e^{\mathbf{F}/2^{k}}]\big]^{2^k}}{(1-\lambda v_k^2)^{2^{k-1}-1}}\\
  \mathsf{Tr}\big[\mathbb{E}[e^{\mathbf{F}/2^{k}}]\big]^{2^k}&\geq(1-\lambda v(F)^2 S_{k-1}-\lambda v_k^2)(1-\lambda v_k^2)^{2^{k-1}-1}\mathsf{Tr}[\mathbb{E}_{x\sim\pi}[e^\mathbf{F}]]\\
  &\geq(1-\lambda v(F)^2 S_{k-1}-\lambda v_k^2)(1-\lambda (2^{k-1}-1)v_k^2)\mathsf{Tr}[\mathbb{E}_{x\sim\pi}[e^\mathbf{F}]] \\
   &\geq (1-\lambda v(F)^2 S_{k-1}-\lambda 2^{k-1} v_k^2)\mathsf{Tr}[\mathbb{E}_{x\sim\pi}[e^\mathbf{F}]]\\
   &\geq (1-\lambda v(F)^2 S_{k-1}-\lambda 2^{k-1} v(F)^2/2^{2k})\mathsf{Tr}[\mathbb{E}_{x\sim\pi}[e^\mathbf{F}]]\\
   &\geq (1-\lambda v(F)^2 S_{k})\mathsf{Tr}[\mathbb{E}_{x\sim\pi}[e^\mathbf{F}]]
\end{align*}
where the fourth inequality follows from $(1-x)^n\geq(1-nx)$ and the last line follows as $2^{k-1}/2^{2k} = 1/2^{k+1} \leq 1/2^k$
\end{proof}
\begin{proof}{[of Theorem \ref{thm:srBern}]} Since our function $\mathbf{F}$ is L-Lipshitz, we know that $v(\mathbf{F})\leq 2L$ as the Hamming distance between any pair of connected states in the Markov Chain is 2. Hence, using Theorem \ref{thm:mgfBound} and the fact that $\lambda\geq1/{2k}$ (from \ref{thm:mpc}), we are done.
\end{proof}
