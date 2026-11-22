---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-051-112-bounds-and-limits-of-the-cumulants
section_title: "Bounds and limits of the cumulants"
section_number: 11.2
pages: 93-96
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.92
latex_coverage_ratio: 0.961
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\label{subsec:boundcumulantchmu} 

\subsubsection{The dependency graph for random character values} If $k=|\mu|$, we are interested in the non-commutative random variables
$$\varSigma_{\mu,n}=\sum_{A \in \arr(n,k)} \rho_{\mu}(A) \in \C\sym(n).$$
Again, to control the cumulants, we shall exhibit a dependency graph for the families of random variables $\{\rho_{\mu}(A)\}_{A \in \arr(n,k)}$.

Due to the multiplicative form of Equation \eqref{eq:def_tau_omega}, if $I$ and $J$ have disjoint subsets of $[n]$, the subalgebras $\C\sym(I)$ and $\C\sym(J)$ are tensor independent (here, $\sym(I)$ denotes the group of permutations of $I$, canonically included in $\sym(n)$). Therefore, one can associate to $\{\rho_{\mu}(A)\}_{A \in \arr(n,k)}$
the dependency graph $\B$ defined by: \vspace{2mm}
\begin{itemize}
    \item its vertex set is $\arr(n,k)$;\vspace{2mm}
    \item there is an edge between $A$ and $A'$ if  $|A \cap A'| \ge 1$.\vspace{2mm}
\end{itemize}
The graph $\B$ is obviously regular with degree strictly smaller than $k^{2}\,n\fall{k-1}$. On the other hand, all joint moments of the family $(\rho_{\mu}(A))_{A \in \arr(n,k)}$ are normalized characters of single permutations and hence bounded by $1$ in absolute value. So one can once again apply Theorem \ref{thm:dependencygraphsrefined} and we get:

\begin{proposition}\label{prop:boundcumulantcharacter} 
Fix a partition $\mu$ of size $k$. For any $r\le 1$, one has
\begin{align*} 
\big| \kappa^{(r)}(\varSigma_\mu) \big| &\le 2^{r-1} r^{r-2}\,  n\fall k\, (k^{2} n\fall{k-1})^{r-1};\\
\big| \kappa^{(r)}(\SubGraph_{\rho_\mu}) \big| &\le r^{r-2}\,  \left(\frac{2k^{2}}{n} \right)^{r-1}.
\end{align*}
\end{proposition}

\begin{remark}
Using Theorem~\ref{thm:boundjointcumulant}, one can also obtain a bound for joint cumulants of the $\SubGraph_{\rho_\mu}$, namely,
$$\left| \kappa\!\left (\SubGraph_{\rho_{\mu^{1}}},\dots,\SubGraph_{\rho_{\mu^{r}}}\right) \right| \le k_1 \cdots k_r\, \big(r \cdot \max_{1 \le i \le r} k_i \big)^{r-2} \, \left(\frac{2}{n}\right)^{r-1}$$
for integer partitions $\mu^1,\dots,\mu^r$ of sizes $k_1,\ldots,k_r$. In the following, we shall focus on the case of simple random variables $\SubGraph_{\rho_{\mu}}$, though most results also hold in the multi-dimensional setting. Actually, in order to compute the asymptotics of the first cumulants of $X_{\rho_{\mu}}$, it will be a bit clearer to manipulate joint cumulants of variables $\varSigma_{\mu^{1}},\ldots,\varSigma_{\mu^{r}}$ with arbitrary integer partitions.
\end{remark}
\bigskip



\subsubsection{Limits of the second and third cumulants}\label{subsubsec:limitchar_K2K3}
Because of Lemma \ref{lem:cumulantcharacterpoly} and Proposition \ref{prop:boundcumulantcharacter}, for any fixed integer partitions, $$\kappa\left(\SubGraph_{\rho_{\mu^{1}}},\dots,\SubGraph_{\rho_{\mu^{r}}}\right)\,n^{1-r}\simeq \kappa\left(\varSigma_{\mu^{1}},\ldots,\varSigma_{\mu^{r}}\right)\,n^{k_{1}+\cdots+k_{r}-(r-1)}$$ converges to a constant. Let us compute this limit when $r=2$ or $3$; we use the same reasoning as in Section \ref{subsec:sigma_L}.\bigskip

As $\kappa$ is invariant by simultaneous conjugacy of its arguments, the summand in Equation \eqref{eq:listequality} depends only on the graph $G=G_{\AA}$ associated to the collection $\AA=(A^1,\dots,A^r)$, and we shall denote it $\kappa(G)$.  We fix partitions $\mu^{1},\ldots,\mu^{r}$ of respective sizes $k_{1},\ldots,k_{r}$, and write $$\kappa(\varSigma_{\mu^{1}},\ldots,\varSigma_{\mu^{r}})=\sum_{G}\, \kappa(G)\,N_{G}.$$ 
Here, as in Section~\ref{sec:erdosrenyi}, $N_G$ denotes the number of list $\AA$ of arrangements with associated graph $G$.\medskip

When $r=2$, we have to look for graphs $G$ on vertex set $V_{\Bbbk}=[k_{1}]\sqcup [k_{2}]$ with $1$-contraction connected and at least $k_{1}+k_{2}-1$ connected components, because these are the ones that will give a contribution for the coefficient of $n^{k_{1}+k_{2}-1}$. For $i \in [\ell(\mu^{1})]$ and $j \in [\ell(\mu^{2})]$, denote $$(\mu^{1} \Join \mu^{2} )(i,j)=(\mu^{1} \setminus \mu_{i}^{1})\sqcup(\mu^{2} \setminus \mu_{j}^{2}) \sqcup \{\mu_{i}^{1}+\mu_{j}^{2}-1\}.$$ This is the cycle type of a permutation $\rho_{\mu^{1}}(A^{1})\,\rho_{\mu^{2}}(A^{2})$, where $G_{\AA}$ is the graph with one edge joining an element of $A^{1}$ in the cycle of length $\mu^{1}_{i}$ with an element of $A^{2}$ in the cycle of length $\mu^{2}_{j}$. These graphs are the only ones involved in our computation, and they yield 
$$\kappa(G)=p_{(\mu^{1} \Join \mu^{2} )(i,j)}(\omega)-p_{\mu^{1}\sqcup\mu^{2}}(\omega),$$
where for a partition $\mu$ we denote $p_{\mu}(\omega)$ the product $\prod_{i=1}^{\ell(\mu)}p_{\mu_{i}}(\omega)$. So,

\begin{proposition}
For any partitions $\mu$ and $\nu$, the limit of $n\,\kappa(\SubGraph_{\rho_\mu},\SubGraph_{\rho_\nu})$ is 
$$\sum_{i=1}^{\ell(\mu)}\sum_{j=1}^{\ell(\nu)} \,\mu_{i}\,\nu_{j}\,\big(p_{(\mu\Join \nu)(i,j)}(\omega)-p_{\mu\sqcup\nu}(\omega)\big).$$
\end{proposition}

\noindent In particular, for cycles $\mu=(k)$ and $\nu=(l)$,
$$\lim_{n \to \infty} n\,\,\kappa\!\left(\SubGraph_{k},\SubGraph_{l}\right)=kl\,\big(p_{k+l-1}(\omega)-p_{k,l}(\omega)\big).$$
On the other hand, if $\mu=\nu$, then the limit of $n\,\kappa^{(2)}(X^{(n)}_{\rho_{\mu}})$ is
$$(p_{\mu}(\omega))^{2}\sum_{1 \leq i,j\leq \ell(\mu)} \mu_{i}\,\mu_{j}\,\left(\frac{p_{(\mu_{i} \mu_{j}-1)}(\omega)}{p_{\mu_{i}}(\omega)\,p_{\mu_{j}}(\omega)}-1\right).$$
\bigskip

When $r=3$, we look for graphs $G$ on vertex set $V_{\Bbbk}=[k_{1}]\sqcup [k_{2}]\sqcup [k_{3}]$ with $1$-contraction connected and at least $k_{1}+k_{2}+k_{3}-2$ connected components. They are of three kinds: \vspace{2mm}
\begin{enumerate}
\item One cycle in $\rho_{\mu^{2}}(A^{2})$ is connected to two cycles in $\rho_{\mu^{1}}(A^{1})$ and $\rho_{\mu^{3}}(A^{3})$, but not by the same point in this cycle of $\rho_{\mu^{2}}(A^{2})$. This gives for $\rho_{\mu^{1}}(A^{1})\,\rho_{\mu^{2}}(A^{2})\,\rho_{\mu^{3}}(A^{3})$ a permutation of cycle type
$$( \mu^{1} \Join \mu^{2} \Join \mu^{3}) (i,j,k)=(\mu^{1}\setminus \mu^{1}_{i})\sqcup (\mu^{2}\setminus \mu^{2}_{j})\sqcup (\mu^{3}\setminus \mu^{3}_{k})\sqcup\{\mu^{1}_{i}+\mu^{2}_{j}+\mu^{3}_{k}-2\};$$
and the corresponding cumulant is
\begin{align*}\kappa(G)&=p_{\mu^{1}\sqcup \mu^{2}\sqcup \mu^{3}}(\omega)+p_{(\mu^{1}\Join \mu^{2}\Join \mu^{3})(i,j,k)}(\omega) \\
&\,\,\,\,\,\,- p_{((\mu^{1}\Join \mu^{2})(i,j)) \sqcup \mu^{3}}(\omega)-p_{((\mu^{2}\Join \mu^{3})(j,k)) \sqcup \mu^{1}}(\omega).\end{align*}
In this description, one can permute cyclically the indices $1,2,3$, and this gives $3$ different graphs.\vspace{2mm}
\item One cycle in $\rho_{\mu^{2}}(A^{2})$ is connected to two cycles in $\rho_{\mu^{1}}(A^{1})$ and $\rho_{\mu^{3}}(A^{3})$, and by the same point in this cycle of $\rho_{\mu^{2}}(A^{2})$. In other words, there is an identity  $a^{1}_{s}=a^{2}_{t}=a^{3}_{u}$. This gives again for $\rho_{\mu^{1}}(A^{1})\,\rho_{\mu^{2}}(A^{2})\,\rho_{\mu^{3}}(A^{3})$ a permutation of cycle type $( \mu^{1} \Join \mu^{2} \Join \mu^{3}) (i,j,k)$, but the corresponding cumulant takes now the form
\begin{align*}\kappa(G)&=2\,p_{\mu^{1}\sqcup \mu^{2}\sqcup \mu^{3}}(\omega)+p_{(\mu^{1}\Join \mu^{2}\Join \mu^{3})(i,j,k)}(\omega) - p_{((\mu^{1}\Join \mu^{2})(i,j)) \sqcup \mu^{3}}(\omega)\\
&\,\,\,\,\,\,-p_{((\mu^{2}\Join \mu^{3})(j,k)) \sqcup \mu^{1}}(\omega)-p_{((\mu^{1}\Join \mu^{3})(i,k)) \sqcup \mu^{2}}(\omega).\end{align*}
Here, there is no need to permute cyclically the indices in the enumeration for $N_{G}$.\vspace{2mm}
\item Two distinct cycles in $\rho_{\mu^{2}}(A^{2})$ are connected to a cycle of $\rho_{\mu^{1}}(A^{1})$ and to a cycle of $\rho_{\mu^{3}}(A^{3})$, which gives a permutation of cycle type
\begin{align*}
&( \mu^{1} \Join \mu^{2} \Join \mu^{3}) (i,j;k,l)\\
&=(\mu^{1}\setminus \mu^{1}_{i})\sqcup (\mu^{2}\setminus \{\mu^{2}_{j},\mu^{2}_{k}\})\sqcup (\mu^{3}\setminus \mu^{3}_{l})\sqcup\{\mu^{1}_{i}+\mu^{2}_{j}-1,\mu^{2}_{k}+\mu^{3}_{l}-1\}.
\end{align*}
The cumulant corresponding to this last  case is
\begin{align*}\kappa(G)&=p_{\mu^{1}\sqcup \mu^{2}\sqcup \mu^{3}}(\omega)+p_{(\mu^{1}\Join \mu^{2}\Join \mu^{3})(i,j;k,l)}(\omega)\\
&\,\,\,\,\,\,-p_{((\mu^{1}\Join \mu^{2})(i,j)) \sqcup \mu^{3}}(\omega)-p_{((\mu^{2}\Join \mu^{3})(k,l)) \sqcup \mu^{1}}(\omega),\end{align*}
and again one can permute cyclically the indices $1,2,3$ to get $3$ different graphs.\vspace{2mm}
\end{enumerate}
Consequently:

\begin{proposition}
For any partitions $\mu$, $\nu$ and $\delta$, the limit of $n^{2}\,\kappa(\SubGraph_{\rho_\mu},\SubGraph_{\rho_\nu},\SubGraph_{\rho_\delta})$ is 
\begin{align*}\sum_{\Z/3\Z}&\left(\sum_{i=1}^{\ell(\mu)}\sum_{j=1}^{\ell(\nu)}\sum_{k =1}^{\ell(\delta)} \mu_{i}\,\nu_{j}\,(\nu_{j}-1)\,\delta_{k}\left(\substack{p_{\mu\sqcup \nu\sqcup \delta}(\omega)+p_{(\mu\Join \nu\Join \delta)(i,j,k)}(\omega)\\-p_{((\mu\Join \nu)(i,j)) \sqcup \delta}(\omega)-p_{((\nu\Join \delta)(j,k)) \sqcup \mu}(\omega)}\right)\right.\\
&\left.+\sum_{i=1}^{\ell(\mu)}\sum_{(j\neq k) =1}^{\ell(\nu)} \sum_{l=1}^{\ell(\delta)}\mu_{i}\,\nu_{j}\,\nu_{k}\,\delta_{l}\left(\substack{ p_{\mu\sqcup \nu\sqcup \delta}(\omega)+p_{(\mu\Join \nu\Join \delta)(i,j;k,l)}(\omega)\\-p_{((\mu\Join \nu)(i,j)) \sqcup \delta}(\omega)-p_{((\nu\Join \delta)(k,l)) \sqcup \mu}(\omega)}\right) \right)\\
&\!\!\!\!\!\!\!\!\!\!\!\!+ \sum_{i=1}^{\ell(\mu)}\sum_{j=1}^{\ell(\nu)}\sum_{k =1}^{\ell(\delta)} \mu_{i}\,\nu_{j}\,\delta_{k}\left(\substack{2\,p_{\mu\sqcup \nu\sqcup \delta}(\omega)+p_{(\mu\Join \nu\Join \delta)(i,j,k)}(\omega)-p_{((\mu\Join \nu)(i,j)) \sqcup \delta}(\omega)\\
-p_{((\nu\Join \delta)(j,k)) \sqcup \mu}(\omega)-p_{((\mu\Join \delta)(i,k))\sqcup \nu }(\omega)}\right),\end{align*}
where $\sum_{\Z/3\Z}$ means that one permutes cyclically the partitions $\mu,\nu,\delta$.
\end{proposition}
\noindent In particular, for cycles $\mu=(k)$, $\nu=(l)$ and $\delta=(m)$, $\lim_{n \to \infty} n^{2}\,\kappa(\SubGraph_{k},\SubGraph_{l},\SubGraph_{m})$ is equal to
\begin{align*}
klm&\big((k+l+m-1)\,p_{k,l,m}(\omega)+(k+l+m-2)\,p_{k+l+m-2}(\omega)\\
&-(k+l-1)\,p_{k+l-1,m}(\omega)-(l+m-1)\,p_{l+m-1,k}(\omega)-(l+m-1)\,p_{k+m-1,l}(\omega)\big).
\end{align*}
One recovers for $k=l=m$ the values of $\sigma^{2}$ and $L$ announced in Theorem \ref{thm:modgaussianrcv}. On the other hand, if $\mu=\nu=\delta$, then the limit of $\frac{n^{2}\,\kappa^{(3)}(X_{\rho_{\mu}}^{(n)})}{(p_{\mu}(\omega))^{3}}$ is 
\begin{align*}&\sum_{1 \leq  i,j,k \leq \ell(\mu)} 3\,\mu_{i}\,\mu_{j}^{2}\,\mu_{k}\left(1+\frac{p_{\mu_{i}+\mu_{j}+\mu_{k}-2}(\omega)}{p_{\mu_{i}}(\omega)\,p_{\mu_{j}}(\omega)\,p_{\mu_{k}}(\omega)}-\frac{p_{\mu_{i}+\mu_{j}-1}(\omega)}{p_{\mu_{i}}(\omega)\,p_{\mu_{j}}(\omega)}-\frac{p_{\mu_{j}+\mu_{k}-1}(\omega)}{p_{\mu_{j}}(\omega)\,p_{\mu_{k}}(\omega)}\right)\\
&\quad+\sum_{1\leq i,j\neq k,l \leq \ell(\mu)}3\,\mu_{i}\,\mu_{j}\,\mu_{k}\,\mu_{l}\left( 1- \frac{p_{\mu_{i}+\mu_{j}-1}(\omega)}{p_{\mu_{i}}(\omega)\,p_{\mu_{j}}(\omega)}\right)\left(1 - \frac{p_{\mu_{k}+\mu_{l}-1}(\omega)}{p_{\mu_{k}}(\omega)\,p_{\mu_{l}}(\omega)}\right) \\
&\quad+\sum_{1 \leq  i,j,k \leq \ell(\mu)} \mu_{i}\,\mu_{j}\,\mu_{k}\left(3\,\frac{p_{\mu_{i}+\mu_{j}-1}(\omega)}{p_{\mu_{i}}(\omega)\,p_{\mu_{j}}(\omega)}-2\,\frac{p_{\mu_{i}+\mu_{j}+\mu_{k}-2}(\omega)}{p_{\mu_{i}}(\omega)\,p_{\mu_{j}}(\omega)\,p_{\mu_{k}}(\omega)}-1\right).\end{align*}
\bigskip
