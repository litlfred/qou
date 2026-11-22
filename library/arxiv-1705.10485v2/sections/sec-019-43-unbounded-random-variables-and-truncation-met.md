---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-019-43-unbounded-random-variables-and-truncation-met
section_title: "Unbounded random variables and truncation methods"
section_number: 4.3
pages: 35-40
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.92
latex_coverage_ratio: 0.957
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
A possible generalization regards sums of *unbounded* random variables. In the following, we develop a truncation method that yields a criterion of asymptotic normality similar to Lyapunov's condition (see [@Bil95 Chapter 27]). A small modification of this method would similarly yield a Lindeberg type criterion. Let $S_n = \sum_{i=1}^{N_n} A_{i,n}$ be a sum of centered random variables, with $$\left(\mathbb{E}[|A_{i,n}|^{2+\delta}]\right)^{\frac{1}{2+\delta}} \leq A$$ for some constant $A$ independent of $i$ and $n$, and some $\delta>0$. We suppose as before that the family of random variables $(A_{i,n})_{i\in \left[\!\left[1,N_n\right]\!\right]}$ has a (true) dependency graph $G_n$ of parameters $N_n$ and $D_n$. Note that in this case, $$\begin{aligned}
\mathrm{Var}(S_n) &= \sum_{i,j=1}^{N_n} \mathrm{cov}(A_{i,n},A_{j,n}) \leq \sum_{i=1}^{N_n} \sum_{j \sim i} \|A_{i,n}\|_2\,\|A_{j,n}\|_2 \\
&\leq \sum_{i=1}^{N_n} \sum_{j \sim i} \|A_{i,n}\|_{2+\delta}\,\|A_{j,n}\|_{2+\delta} \leq A^2 \,N_n D_n.
\end{aligned}$$ We set $$\begin{aligned}
A_{i,n}^- &= A_{i,n}\,1_{|A_{i,n}| \leq L_n} \qquad;\qquad A_{i,n}^+ = A_{i,n}\,1_{|A_{i,n}| > L_n}\,; \\
S_n^- &=\sum_{i=1}^{N_n} A_{i,n}^- \qquad\qquad\,\,\,;\qquad S_n^+=\sum_{i=1}^{N_n} A_{i,n}^+\,;
\end{aligned}$$ where $L_n$ is a truncation level, to be chosen later. Notice that $G_n$ is still a dependency graph for the family of truncated random variables $(A_{i,n}^-)_{i \in \left[\!\left[1,N_n\right]\!\right]}$. Therefore, we can apply the previously developed machinery (Theorem [\[thm:boundcumulant\]](#thm:boundcumulant){reference-type="ref" reference="thm:boundcumulant"} and Corollary [\[cor:Cumulants_Kol\]](#cor:Cumulants_Kol){reference-type="ref" reference="cor:Cumulants_Kol"}) to the scaled sum $S_n^-/L_n$. On the other hand, by Markov's inequality, $$\begin{aligned}
d_\mathrm{Kol}(S_n,S_n^-) &= \sup_{s \in \mathbb{R}} |\mathbb{P}[S_n \geq s] - \mathbb{P}[S_n^- \geq s]| \leq \mathbb{P}[S_n^+ = 0] \\
&\leq \sum_{i=1}^{N_n} \mathbb{P}[|A_{i,n}| \geq L_n] \leq N_n\,\left(\frac{A}{L_n}\right)^{\!\!2+\delta}.
\end{aligned}$$ Combining the two arguments leads to the following result (this replaces the previous assumption of boundedness $|A_{i,n}| \leq A$).

::: theorem
[]{#thm:unbounded label="thm:unbounded"} Let $(S_n = \sum_{i=1}^{N_n} A_{i,n})_{n \in \mathbb{N}}$ be a sum of centered random variables, with dependency graphs of parameters $N_n \to +\infty$ and $D_n$, and with $$\|A_{i,n}\|_{2+\delta}=(\mathbb{E}[|A_{i,n}|^{2+\delta}])^{1/(2+\delta)} \leq A$$ for all $i,n$ and for some $\delta>0$. We set $Y_n = S_n/\sqrt{\mathrm{Var}(S_n)}$. Recall that $(\widetilde{\sigma}_n)^2 = \frac{\mathrm{Var}(S_n)}{N_n D_n}$.

1.  []{#hyp:unbounded1 label="hyp:unbounded1"} Set $$V_n=(\widetilde{\sigma}_n)^2\,\left(\frac{N_n}{D_n}\right)^{\!1/3} \,\frac{1}{(N_n)^{2/(2+\delta)}}$$ and suppose that $\lim_{n \to \infty} V_n= +\infty$ (which is only possible for $\delta > 4$). Then, for $n$ large enough, $$d_\mathrm{Kol}(Y_n,\,\mathcal{N}_{\mathbb{R}}(0,1)) \leq 78\left(\frac{A^2}{V_n}\right)^{\!\frac{3(\delta+2)}{2(\delta+5)}}=o\!\left(\frac{1}{V_n}\right).$$

2.  []{#hyp:unbounded2 label="hyp:unbounded2"} More generally, for $\varepsilon\in (\frac{2}{2+\delta},1)$, set $$W_n=(\widetilde{\sigma}_n)^2\,\left(\frac{N_n}{D_n}\right)^{\!\varepsilon} \,\frac{1}{(N_n)^{2/(2+\delta)}}$$ and suppose that $\lim_{n \to \infty} W_n= +\infty$. Then, $Y_n \rightharpoonup \mathcal{N}_{\mathbb{R}}(0,1)$.
:::

::: remark
It should be noticed that if $\delta \to +\infty$, then one essentially recovers the content of Corollary [\[cor:Cumulants_Kol\]](#cor:Cumulants_Kol){reference-type="ref" reference="cor:Cumulants_Kol"} (which can be applied because of Theorem [\[thm:boundcumulant\]](#thm:boundcumulant){reference-type="ref" reference="thm:boundcumulant"}). On the other hand, the inequality $\delta > 4$ amounts to the existence of bounded moments of order strictly higher than $6$ for the random variables $A_{i,n}$. In practice, one can for instance ask for bounded moments of order $7$ (*i.e.* $\delta=5$), in which case the first condition [\[hyp:unbounded1\]](#hyp:unbounded1){reference-type="ref" reference="hyp:unbounded1"} reads $$\lim_{n \to \infty} \frac{\mathrm{Var}(S_n)}{D_n\,N_n} \, \frac{(N_n)^{1/9}}{(D_n)^{1/3}} = +\infty.$$ Moreover, we will see in the proof of Theorem [\[thm:unbounded\]](#thm:unbounded){reference-type="ref" reference="thm:unbounded"} that in this setting ($\delta=5$), the constant $78$ can be improved to $39$, so that, for $n$ large enough: $$d_\mathrm{Kol}(Y_n,\,\mathcal{N}_{\mathbb{R}}(0,1))\leq 39\left(\frac{A^2}{V_n}\right)^{\frac{21}{20}}.$$
:::

::: proof
*Proof.* We write as usual $Y_n = \frac{S_n}{\sqrt{\mathrm{Var}(S_n)}}$, and $Y_n^- = \frac{S_n^-}{\sqrt{\mathrm{Var}(S_n^-)}}$. In all cases, we have $$\begin{aligned}
&d_\mathrm{Kol}(Y_n,\,\mathcal{N}_{\mathbb{R}}(0,1)) \leq d_\mathrm{Kol}(S_n,S_n^-) + d_\mathrm{Kol}\left(Y_n^-,\,\sqrt{\frac{\mathrm{Var}(S_n)}{\mathrm{Var}(S_n^-)}}\,\mathcal{N}_{\mathbb{R}}(0,1)\right) \\
&\leq N_n\left(\frac{A}{L_n}\right)^{2+\delta} + d_\mathrm{Kol}(Y_n^-,\mathcal{N}_{\mathbb{R}}(0,1)) + d_\mathrm{Kol}\left(\mathcal{N}_{\mathbb{R}}(0,1),\,\mathcal{N}_{\mathbb{R}}\!\left(0,\,\frac{\mathrm{Var}(S_n)}{\mathrm{Var}(S_n^-)}\right)\right)
\end{aligned}$$ by using the invariance of the Kolmogorov distance with respect to multiplication of random variables by a positive constant. In the sequel, we denote $a$, $b$ and $c$ the three terms on the second line of the inequality. The Kolmogorov distance between two Gaussian distributions is $$\begin{aligned}
d_\mathrm{Kol}(\mathcal{N}_{\mathbb{R}}(0,1),\,\mathcal{N}_{\mathbb{R}}(0,\lambda^2)) &= \frac{1}{\sqrt{2\pi}}\sup_{s \in \mathbb{R}_+} \left( \int_{s}^{\lambda s} \E^{-\frac{u^2}{2}}\,d\hspace*{-0.3mm}{u} \right)\\
&\leq \frac{\lambda-1}{\sqrt{2\pi}}\,\sup_{s \in \mathbb{R}_+} \left(s\,\E^{-\frac{s^2}{2}}\right) =\sqrt{\frac{1}{2\pi\E}}\,|\lambda-1|
\end{aligned}$$ if $\lambda \geq 1$. One gets the same result if $\lambda \leq 1$, hence, $$\begin{aligned}
d_\mathrm{Kol}\left(\mathcal{N}_{\mathbb{R}}(0,1),\,\mathcal{N}_{\mathbb{R}}\!\left(0,\,\frac{\mathrm{Var}(S_n)}{\mathrm{Var}(S_n^-)}\right)\right) &= d_\mathrm{Kol}\left(\mathcal{N}_{\mathbb{R}}(0,1),\,\mathcal{N}_{\mathbb{R}}\!\left(0,\,\frac{\mathrm{Var}(S_n^-)}{\mathrm{Var}(S_n)}\right)\right) \\
&\leq \sqrt{\frac{1}{2\pi\E}} \left|\sqrt{\frac{\mathrm{Var}(S_n^-)}{\mathrm{Var}(S_n)}}-1\right| \\
&\leq \sqrt{\frac{1}{2\pi\E}}\,\frac{|\mathrm{Var}(S_n^-)-\mathrm{Var}(S_n)|}{\mathrm{Var}(S_n)}.
\end{aligned}$$ To evaluate the difference between the variances, notice that $$\begin{aligned}
\mathrm{Var}(S_n^-) &= \mathrm{Var}\left(S_n - \sum_{i=1}^{N_n} A_{i,n}^+\right) \\
&=\mathrm{Var}(S_n) - 2 \sum_{i,j=1}^{N_n} \mathrm{Cov}(A_{i,n}^+,A_{j,n}) + \sum_{i,j=1}^{N_n} \mathrm{Cov}(A_{i,n}^+,A_{j,n}^+)
\end{aligned}$$ If $j$ is not connected to $i$ in $G_n$, or equal to $i$, then $A_{i,n}$ and $A_{j,n}$ are independent, hence, $\mathrm{Cov}(A_{i,n}^+,A_{j,n})=0$. Otherwise, using Hölder and Bienaymé-Chebyshev inequalities, $$\begin{aligned}
|\mathrm{Cov}(A_{i,n}^+,A_{j,n})| &\leq \sqrt{\mathbb{E}[(A_{i,n})^2\,1_{|A_{i,n}|\geq L_n}]\,\mathbb{E}[(A_{j,n})^2\,1_{|A_{i,n}|\geq L_n}]} \\
&\leq \sqrt{\mathbb{E}[(A_{i,n})^{2+\delta}]^{\frac{2}{2+\delta}}\,\mathbb{P}[|A_{i,n}| \geq L_n]^{\frac{2\delta}{2+\delta}}\,\mathbb{E}[(A_{j,n})^{2+\delta}]^{\frac{2}{2+\delta}} } \\
&\leq A^2\,\left(\frac{A}{L_n}\right)^{\!\delta}.
\end{aligned}$$ Similarly, $$\begin{aligned}
|\mathrm{Cov}(A_{i,n}^+,A_{j,n}^+)| &\leq \mathbb{E}[|A_{i,n}^+A_{j,n}^+|] + \mathbb{E}[|A_{i,n}^+|]\,\mathbb{E}[|A_{j,n}^+|]\\
&\leq A^2\left(\left(\frac{A}{L_n}\right)^\delta + \left(\frac{A}{L_n}\right)^{2+2\delta}\right),
\end{aligned}$$ hence, assuming that the level of truncation $L_n$ is larger than $A$, $$\frac{|\mathrm{Var}(S_n)^- - \mathrm{Var}(S_n)|}{\mathrm{Var}(S_n)} \leq \frac{N_n\,D_n}{\mathrm{Var}(S_n)}\,3A^2\,\left(\frac{A}{L_n}\right)^{\!\delta}.$$ Let us now place ourselves in the setting of Hypothesis [\[hyp:unbounded1\]](#hyp:unbounded1){reference-type="ref" reference="hyp:unbounded1"}; we set $$V_n = \frac{\mathrm{Var}(S_n)}{N_n\,D_n}\,\left(\frac{N_n}{D_n}\right)^{\!1/3}\,\frac{1}{(N_n)^{2/(2+\delta)}}.$$ Suppose that $L_n = K_n\,(N_n)^{\frac{1}{2+\delta}}$, with $K_n$ going to infinity. We then have $a \leq \frac{A^{2+\delta}}{(K_n)^{2+\delta}}$, and on the other hand, $$\begin{aligned}
\left|\frac{\mathrm{Var}(S_n^-)}{\mathrm{Var}(S_n)}-1\right| &\leq  3A^{2+\delta}\left(\frac{N_n\,D_n}{\mathrm{Var}(S_n)}\,\frac{1}{(N_n)^{\delta/(2+\delta)}}\,\frac{1}{(K_n)^{\delta}}\right) \\
&\leq 3A^{2+\delta} \left(\frac{1}{V_n\,(D_n)^{1/3}\,(N_n)^{2/3}\,(K_n)^\delta}\right) \to 0
\end{aligned}$$ since by hypothesis, $\lim_{n \to \infty} \frac{1}{V_n} = 0$. So, $$c \leq \frac{3A^{2+\delta}}{\sqrt{2\pi\E}}\,\frac{1}{V_n\,(D_n)^{1/3}\,(N_n)^{2/3}\,(K_n)^\delta} \leq \frac{3A^{2+\delta}}{\sqrt{2\pi\E}}\,\frac{1}{V_n\,(K_n)^\delta}.$$ Now, the sequence $(S_n^-/L_n)_{n \in \mathbb{N}}$ is a sequence of sums of centered random variables all bounded by $1$, and to apply Corollary [\[cor:Cumulants_Kol\]](#cor:Cumulants_Kol){reference-type="ref" reference="cor:Cumulants_Kol"} to this sequence, we need $$\lim_{n \to \infty} \frac{\mathrm{Var}(S_n^-)}{N_n\,D_n}\,\left(\frac{N_n}{D_n}\right)^{\!1/3}\,\frac{1}{(L_n)^2} = +\infty.$$ However, the previous computation shows that one can replace $\mathrm{Var}(S_n)$ by $\mathrm{Var}(S_n^-)$ in this expression without changing the asymptotic behavior, so $$\lim_{n \to \infty} \frac{\mathrm{Var}(S_n^-)}{N_n\,D_n}\,\left(\frac{N_n}{D_n}\right)^{\!1/3}\,\frac{1}{(L_n)^2} = \lim_{n \to \infty} \frac{V_n}{(K_n)^2},$$ which is $+\infty$ if $(K_n)^2$ is not growing too fast to $+\infty$ (in comparison to the sequence $V_n$). Then, by Corollary [\[cor:Cumulants_Kol\]](#cor:Cumulants_Kol){reference-type="ref" reference="cor:Cumulants_Kol"}, $$b=d_\mathrm{Kol}(Y_n^-,\,\mathcal{N}_{\mathbb{R}}(0,1)) \leq 77\, \frac{(K_n)^3}{(V_n)^{3/2}}$$ for $n$ large enough. Set $K_n = B(V_n)^{\frac{3}{2(5+\delta)}}$. Then, $$\begin{aligned}
d_\mathrm{Kol}(Y_n,\,\mathcal{N}_{\mathbb{R}}(0,1))&\leq a+b+c \leq \left(\frac{A^{2+\delta}}{B^{2+\delta}}+77\,B^3+o(1)\right) \left(\frac{1}{V_n}\right)^{\frac{3(2+\delta)}{2(5+\delta)}} \\
&\leq \left(\left(\frac{231}{2+\delta}\right)^{\frac{2+\delta}{5+\delta}} + 77\,\left(\frac{2+\delta}{231}\right)^{\frac{3}{5+\delta}}\right) \left(\frac{A^2}{V_n}\right)^{\frac{3(2+\delta)}{2(5+\delta)}}
\end{aligned}$$ for $n$ large enough, and by choosing $B$ in an optimal way. The term in parenthesis is maximal when $\delta=229$, and is then equal to $78$. This ends the proof of [\[hyp:unbounded1\]](#hyp:unbounded1){reference-type="ref" reference="hyp:unbounded1"}, and one gets a better constant smaller than $39$ when $\delta=5$.

Under the Hypothesis [\[hyp:unbounded2\]](#hyp:unbounded2){reference-type="ref" reference="hyp:unbounded2"}, we set $$W_n= \frac{\mathrm{Var}(S_n)}{N_n\, D_n}\,\left(\frac{N_n}{D_n}\right)^{\!\varepsilon} \,\frac{1}{(N_n)^{2/(2+\delta)}}.$$ In order to prove the convergence in law $Y_n \rightharpoonup \mathcal{N}_{\mathbb{R}}(0,1)$, it suffices to have:

-   $S_n-S_n^- = S_n^+$ that converges in probability to $0$. This happens as soon as the level $L_n$ is $K_n\, (N_n)^{1/(2+\delta)}$ with $K_n \to +\infty$.

-   $\frac{|\mathrm{Var}(S_n)-\mathrm{Var}(S_n^-)|}{\mathrm{Var}(S_n)} \to 0$. With $L_n = K_n\,(N_n)^{1/(2+\delta)}$, the previous computations show that this quantity is a $$O\left(\frac{1}{W_n\,(N_n)^{1 -\varepsilon}\,(D_n)^{\varepsilon}\,(K_n)^{\delta}}\right),$$ which goes to $0$.

-   and by Theorem [\[thm:CLT_Janson\]](#thm:CLT_Janson){reference-type="ref" reference="thm:CLT_Janson"}, $$\frac{\mathrm{Var}(S_n)}{N_n\,D_n}\left(\frac{N_n}{D_n}\right)^\varepsilon\,\frac{1}{(L_n)^2} \to +\infty .$$ This follows from the Hypothesis [\[hyp:unbounded2\]](#hyp:unbounded2){reference-type="ref" reference="hyp:unbounded2"} if $K_n$ is chosen to grow sufficiently slow.

Thus, the second part of Theorem [\[thm:unbounded\]](#thm:unbounded){reference-type="ref" reference="thm:unbounded"} is proven. 0◻ ◻
:::

::: example
Let $(X_i)_{i \in \left[\!\left[1,N\right]\!\right]}$ be a centered Gaussian vector with $\mathbb{E}[(X_i)^2]=1$ for any $i$, and with the covariance matrix $(\mathrm{Cov}(X_i,X_j))_{1\leq i,j \leq N}$ that is sparse in the following sense: for any $i$, the set of indices $j$ such that $\mathrm{Cov}(X_i,X_j) \neq 0$ has cardinality smaller than $D$. We set $A_i=\exp(X_i)$; the random variables $A_i$ follow the *log-normal distribution* of density $$\frac{1}{\sqrt{2\pi}}\,\frac{1}{u^{1+\frac{\log u}{2}}}\,1_{u>0}\,d\hspace*{-0.3mm}{u},$$ and they have moments of all order: $\mathbb{E}[(A_i)^{k}] = \mathbb{E}[\E^{kX_i}] = \E^{\frac{k^2}{2}}.$

<figure>
<div class="center">

</div>
<figcaption>The density of the log-normal distribution.</figcaption>
</figure>

The variables $A_i$ have the same dependency graph as the variables $X_i$. Moreover, if $\rho_{ij}=\mathrm{Cov}(X_i,X_j)$, then the covariance of two variables $A_i$ and $A_j$ is $\E(\E^{\rho_{ij}}-1)$. Using moments of order $2+\delta$, we see that if $$\begin{aligned}
Y_N &= \frac{\sum_{i=1}^N (A_i-\E^{\frac{1}{2}})}{\sqrt{\E \sum_{1\leq i,j\leq N} (\E^{\rho_{ij}}-1)}}\\ 
V_{N,\delta} &= \frac{\E\sum_{1\leq i,j\leq N} (\E^{\rho_{ij}}-1)}{ND} \frac{N^{\frac{1}{3}- \frac{2}{2+\delta} }}{D^{\frac{1}{3}}}\to +\infty,
\end{aligned}$$ then $d_\mathrm{Kol}(Y_N,\,\mathcal{N}_{\mathbb{R}}(0,1))\leq 78\left(\frac{\E^{\delta+2}}{V_{N,\delta}}\right)^{\frac{3(\delta+2)}{2(\delta+5)}}$ for $N$ large enough.

To make this result more explicit, let us consider the following dependency structure for the Gaussian vector $X = (X_i)_{i \in \left[\!\left[1,N\right]\!\right]}$: $$\mathrm{Cov}(X) = \begin{pmatrix}
1 & * & \cdots & * \\
* & 1 & \ddots & \vdots \\
\vdots & \ddots & \ddots & * \\
* & \cdots & * & 1
\end{pmatrix},$$ where the non-diagonal terms $*$ are all smaller than $\frac{\rho}{D}$ in absolute value, and with less than $D$ non-zero terms on each row or column. When $\rho \in [0,1)$, the matrix is diagonally dominant, hence positive-definite, so there exists indeed a Gaussian vector $X$ with these covariances. We then have $$V_{N,\delta} \geq \E\,(1-D(\E^{\frac{\rho}{D}}-1))\,\frac{N^{\frac{1}{3}-\frac{2}{2+\delta}}}{D^{\frac{4}{3}}} ,$$ so if $1 \ll D \ll N^{\frac{1}{4}-\varepsilon}$, then one can apply Theorem [\[thm:unbounded\]](#thm:unbounded){reference-type="ref" reference="thm:unbounded"} to get $$d_\mathrm{Kol}(Y_N,\,\mathcal{N}_{\mathbb{R}}(0,1)) \leq 78 \,\left(\frac{\E^{\frac{3}{2\varepsilon}-1}}{1-\rho}\right)^{\!\frac{3}{2}}\,\left(\frac{D}{N^{\frac{1}{4}-\varepsilon}}\right)^{\frac{2}{2\varepsilon+1}}$$ for $N$ large enough. Moreover, as soon as $1 \ll D \ll N^{\frac{1}{2}-\varepsilon}$, $Y_N \rightharpoonup \mathcal{N}_{\mathbb{R}}(0,1)$.
:::
