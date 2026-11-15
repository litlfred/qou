---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-052-113-asymptotics-of-the-random-character-values-a
section_title: "Asymptotics of the random character values and partitions"
section_number: 11.3
pages: 96-100
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.973
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\label{subsec:asymptoticrcv}
Fix an integer $k \ge 2$, and consider the random variable
$$V_{n,k}=n^{2/3}\,(\SubGraph_{\rho}-p_{k}(\omega)),$$ 
where $\rho$ is a $k$-cycle. If $p_{2k-1}(\omega)-(p_{k}(\omega))^{2}>0$, then the previous results show that  
$$\esper[\E^{zV_{n,k}}]=\exp\left(\frac{n^{1/3}}{2}\,\sigma^2\,z^2 + \frac{1}{6} \,L \,z^3\right)
(1+o(1))\!,$$ 
where $\sigma$ and $L$ are the quantities given in the statement of Theorem~\ref{thm:modgaussianrcv}.
This ends the proof of Theorem \ref{thm:modgaussianrcv} and Corollary \ref{cor:moderatedeviationcharacter}. Note that the speed of convergence of the cumulants is each time a $O((\alpha_{n})^{-1})$ because of the polynomial behavior established in Lemma \ref{lem:cumulantcharacterpoly}; therefore, one can indeed apply Proposition \ref{prop:largedeviationscumulants} with $\alpha_{n}=n$ and $\beta_{n}=n^{-1}$. The theorem can be extended to other permutations $\rho$ of $\sym(\infty)$
than cycles: if $\rho$ has cycle-type $\mu$, then define
\[V_{n,\mu} = n^{2/3}\,(\SubGraph_{\rho}-p_{\mu}(\omega)).\]
Then the  generating series of $V_{n,\mu}$ is asymptotically given by:
$$\esper[\E^{zV_{n,\mu}}]=\exp\left(\frac{n^{1/3}}{2}\,\sigma^2(\mu)\,z^2 + \frac{1}{6} \,L(\mu) \,z^3\right)\!,$$ 
where $\sigma^2(\mu)=\lim_{n \to \infty}n\,\kappa^{(2)}(\SubGraph_{\rho_{\mu}})$ and $L(\mu)=\lim_{n \to \infty}n^{2}\,\kappa^{(3)}(\SubGraph_{\rho_{\mu}})$ are the limiting quantities given in Section \ref{subsubsec:limitchar_K2K3}.
Hence, \emph{provided that $\sigma^{2}(\mu)>0$}, one has mod-Gaussian convergence of $V_{n,\mu}$, and the limiting variance $\sigma^{2}(\mu)$ is non-zero under the same conditions as those given in Remark \ref{rem:limitvarianceispositive}. Under these conditions, one can also easily establish mod-Gaussian convergence for every vector of 
renormalized random character values $(V_{n,\mu_1},\dots, V_{n,\mu_\ell})$
\bigskip


\begin{remark} There is one case which is not covered by our theorem,
but is of particular interest: the case $\omega=((0,0,\ldots),(0,0,\ldots))$.
This parameter of the Thoma simplex corresponds to the Plancherel measures of the symmetric groups, and in this case, since $p_{2}(\omega)=p_{3}(\omega)=\cdots=0$, the parameters of the mod-Gaussian convergence are all equal to $0$. Indeed, the random character values under Plancherel measures do not have fluctuations of order $n^{-1/2}$. For instance, Kerov's central limit theorem (\emph{cf.} \cite{Hora98,IO02}) ensures that the random character values
$$\frac{n^{k/2}\,\widehat{\chi}^{\lambda}(c_{k})}{\sqrt{k}}$$
on cycles $c_{k}$ of lengths $k \geq 2$ converges in law towards independent Gaussian variables; so the fluctuations are of order $n^{-k/2}$ instead of $n^{-1/2}$. One still expects a mod-Gaussian convergence for adequate renormalizations of the random character values; however, the combinatorics underlying the asymptotics of Plancherel measures are much more complex than those of general central measures --- see \cite{Sni06a} --- and we have not been able to prove mod-Gaussian convergence here.\bigskip
\end{remark}

From the estimates on the laws of the random character values, one can prove many estimates for the parts $\lambda_{1},\lambda_{2},\ldots$ of the random partitions taken under central measures. The arguments of algebraic combinatorics involved in these deductions are detailed in \cite{FM12,Mel12}, so here we shall only state results. Given a partition $\lambda=(\lambda_{1},\ldots,\lambda_{\ell})$ of size $n$, the Frobenius coordinates of $\lambda$ are the two sequences
$$\left(\lambda_{1}-\frac{1}{2},\lambda_{2}-\frac{3}{2},\ldots,\lambda_{d}-d+\frac{1}{2}\right),\left(\lambda_{1}'-\frac{1}{2},\lambda_{2}'-\frac{3}{2},\ldots,\lambda_{d}'-d+\frac{1}{2}\right)$$
where $\lambda_{1}'$, $\lambda_{2}'$, \emph{etc.} are the sizes of the columns of the Young diagram of $\lambda$, and $d$ is the size of the diagonal of the Young diagram. Denote $(a_{1},\ldots,a_{d}),(b_{1},\ldots,b_{d})$ these coordinates, and
$$X_{\lambda}=\sum_{i=1}^{d} \frac{a_{i}}{n}\,\delta_{\left(\frac{a_{i}}{n}\right)}+\sum_{i=1}^{d}\frac{b_{i}}{n}\,\delta_{\left(-\frac{b_{i}}{n}\right)}.$$
This is a (random) discrete probability measure on $[-1,1]$ whose moments
$$p_{k}(\lambda)=n^{k}\,\int_{-1}^{1} x^{k-1}\, X_{\lambda}(dx)$$
are also the moments of the Frobenius coordinates, so $X_{\lambda}$ encodes the geometry of the Young diagram $\lambda$. We shall also need
$$X_{\omega}=\sum_{i=1}^{d} \alpha_{i}\,\delta_{\left(\alpha_{i}\right)}+\sum_{i=1}^{d}\beta_{i}\,\delta_{\left(-\beta_{i}\right)}+\gamma\,\delta_{\left(0\right)},$$
which will appear in a moment as the limit of the random measures $X_{\lambda}$. Here, $\gamma=1-\sum_{i=1}^{\infty}\alpha_{i}-\sum_{i=1}^{\infty}\beta_{i}$. Notice that $\esper_{n,\omega}[\SubGraph_{k}]=\tau_{\omega}(c_{k})=X_{\omega}(x^{k-1})$.\bigskip

It is shown in \cite{IO02} that for any partition $\lambda$ of size $n$ and for any $k$,
$$p_{k}(\lambda)=\varSigma_{k}(\lambda)+\text{remainder},$$
where the remainder is a linear combination of symbols $\varSigma_{\mu}$ with $|\mu|<k$. It follows that the cumulants of the $p_{k}$'s satisfy the same estimates as the cumulants of the $\varSigma_{k}$'s. Therefore, the rescaled random variable 
$\nabla(x^{k-1})=n^{2/3}\,(X_{\lambda}(x^{k-1})-X_{\omega}(x^{k-1}))$
converges in the mod-Gaussian sense with parameters $n^{1/3}\,\sigma^{2}$ and limiting function $\psi(z)=\exp(L\,\frac{z^{3}}{6})$, where $\sigma^{2}$ and $L$ are given by the same formula as in the case of the random character value $\SubGraph_{k}$, that is to say
\begin{align*}
\sigma^{2}&=k^{2}\,\big(p_{2k-1}(\omega)-p_{k}(\omega)^{2}\big);\\
L&= k^{3}\,\big((3k-2)\,p_{3k-2}(\omega)-(6k-3)\,p_{2k-1}(\omega)\,p_{k}(\omega)+(3k-1)\,p_{k}(\omega)^{3}\big).
\end{align*}
Actually, one has mod-Gaussian convergence for any finite vector of random variables $\nabla(x^{k-1})$, $k \geq 1$.
\bigskip

We don't know how to obtain from there moderate deviations for the parts $\lambda_{1},\lambda_{2},\ldots$ of the partition; but one has at least a central limit theorem when one has strict inequalities $\alpha_{1} > \alpha_{2} > \cdots > \alpha_{i} > \cdots$ and $\beta_{1} > \beta_{2} > \cdots > \beta_{i} > \cdots$ (see \cite{Mel12}, and also \cite{Buf12}). Indeed, for any smooth test function $\psi_{i}$ equal to $1$  around $\alpha_{i}$ and to $0$ outside a neighborhood of this point, one has
\begin{equation}
X_{\lambda}(\psi_{i})-X_{\omega}(\psi_{i}) = \frac{a_{i}}{n}-\alpha_{i} \label{eq:almostalwaystrue}
\end{equation}
with probability going to $1$, and then the quantities in the left-hand side renomalized by $\sqrt{n}$ converge jointly towards a Gaussian vector with covariance
\begin{equation}\kappa(i,j)=\delta_{ij}\,\alpha_{i}-\alpha_{i}\alpha_{j}.\label{eq:last}\end{equation}
So, the fluctuations $$\sqrt{n}\left(\frac{\lambda_{i}}{n}-\alpha_{i}\right)$$ of the rows of the random partitions taken under central measures $\proba_{n,\omega}$ converge jointly towards a Gaussian vector with covariances given by Equation \eqref{eq:last}, and one can include in this result the fluctuations
$$\sqrt{n}\left(\frac{\lambda_{j}'}{n}-\beta_{j}\right)$$ of the columns of the random partitions, with a similar formula for their covariances. \bigskip

The reason why it becomes difficult to get by the same technique the moderate deviations of the rows and columns is that in Equation \eqref{eq:almostalwaystrue}, one throws away an event of probability going to zero (because of the law of large numbers satisfied by the rows and the columns, see \emph{e.g.} \cite{KV81}). However, one cannot \emph{a priori} neglect this event in comparison to rare events such as $\{ a_{i}-n\alpha_{i} \geq n^{2/3}\,x\};$ indeed, these rare events are themselves of probability going exponentially fast to zero. Also, there is the problem of approximation of smooth test functions by polynomials, which one has to control precisely when doing these computations. One still conjectures these moderate deviations to hold, and $n^{2/3}\left(\frac{a_{i}}{n}-\alpha_{i}\right)$ to converge in the mod-Gaussian sense with parameters $n^{1/3}(\alpha_{i}-\alpha_{i}^{2})$ and limiting function $$\psi(z)=\exp\left(\frac{\alpha_{i}-3\alpha_{i}^{2}+2\alpha_{i}^{3}}{6}\,z^{3}\right)$$ --- this is what one obtains if we ignore the previous caveats, and still suppose the $\alpha_{i}$ and $\beta_{j}$ all distinct. As explained in \cite{Mel12} (see also \cite{KV86}), this would give moderate deviations for the lengths of the longest increasing subsequences in a random permutation obtained by generalized riffle shuffle.\bigskip
\bigskip
\bigskip
























\newpage

\bibliographystyle{alpha}
