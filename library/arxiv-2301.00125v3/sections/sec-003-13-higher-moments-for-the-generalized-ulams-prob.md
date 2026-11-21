---
doc_id: arxiv-2301.00125v3
doc_title: "Generating Function for Pinsky’s Combinatorial Second Moment Formula for the Generalized Ulam Problem"
section_id: sec-003-13-higher-moments-for-the-generalized-ulams-prob
section_title: "Higher moments for the generalized Ulam's problem"
section_number: 1.3
pages: 3-4
source_pdf: 2301.00125v3.pdf
source_sha256: 7ecd0cff7d6c2ec4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.986
doc_brief: "Generating Function for Pinsky’s Combinatorial Second Moment Formula for the Generalized Ulam Problem — Given a uniform random permutation π ∈Sn, let Zn,k be equal to the number of increasing"
---
Suppose one seeks information for the distribution of $Z_{n,k}$. The event that $Z_{n,k}>0$
is equal to the event that $L_n\geq k$.
Thus, finding the distribution of $Z_{n,k}$ generalizes Ulam's problem, so it can be called the
``generalized Ulam problem.''
The easy bounds above for the event $Z_{n,k}>0$ follows from Markov's bounds.
But more precise bounds could in principle be obtained if we knew higher moments of $Z_{n,k}$.

In principle, the Bonferroni inequalities would give sharp bounds if one had sufficient information
on the moments. A good reference for this  topic is the combinatorics textbook
of Charalambides \cite{Charalambides}.
In Appendix \ref{sec:Bon} we will review this.
The first author, Samen Hossein, has an earlier unpublished article, submitted to a private organization, which treats this topic in more detail. That is available upon 
request. But, we will summarize it in the appendix.
Because of all this, it is interesting to know the distribution of $Z_{n,k}$, beyond just its mean.

In \cite{Pinsky1}, Pinsky investigated the second moment.
He obtained an exact combinatorial formula.
He then rigorously analyzed the formula obtaining upper and lower bounds of matching exponential growth
rates  although with different constant
multipliers.
\begin{proposition}[Pinsky's First Result]
If there is a sequence $k_n$ such that $\lim_{n \to \infty} k_n /n^{2/5}=0$ then 
\begin{equation}
	\frac{\mathbf{E}[Z_{n,k_n}^2]}{\big(\mathbf{E}[Z_{n,k_n}]\big)^2} - 1\, =\, \mathcal{O}\left(\frac{k_n^{5/2}}{n}\right)\, .
\end{equation}
If instead $\liminf_{n \to \infty} k_n/n^{2/5} > 0$ and $\limsup_{n\to\infty} k_n/n^{2/5} < \infty$ then 
\begin{equation}
	0\, <\, \liminf_{n \to \infty} \frac{\mathbf{E}[Z_{n,k_n}^2]}{\big(\mathbf{E}[Z_{n,k_n}]\big)^2}\, \leq\, 
	\limsup_{n \to \infty} \frac{\mathbf{E}[Z_{n,k_n}^2]}{\big(\mathbf{E}[Z_{n,k_n}]\big)^2}\, < \infty\, .
\end{equation}
If $\lim_{n \to \infty} n^{2/5}/k_n = 0$ then 
\begin{equation}
	\frac{\big(\mathbf{E}[Z_{n,k_n}]\big)^2}{\mathbf{E}[Z_{n,k_n}^2]}\, =\, \mathcal{O}\left(\frac{n}{k_n^{5/2}}\right)\, .
\end{equation}
\end{proposition}
Using this, he could determine exactly the criteria for the Paley-Zygmund second moment 
method to guarantee that $Z_{n,k}$ satisfies a weak law of large numbers type result.
Namely, that condition is that $\lim_{n \to \infty} k_n/n^{2/5}=0$.

Pinsky noted that just because the Paley-Zygmund method does not imply a weak law, that does
not mean that a weak law may not still be true, since it does not necessarily require vanishing of the variance
of the rescaled quantity.
So in \cite{Pinsky2}, Pinsky proved a threshold to be able to disprove a weak law for $Z_{n,k}$.
He showed
\begin{equation}
\forall \epsilon>0\, ,\ \lim_{n \to \infty} \frac{1}{n!} 
\left|\left\{\pi \in S_n\, :\, \left|\frac{Z_{n,k_n}(\pi)}{\mathbf{E}[Z_{n,k_n}]}
-1\right|<\epsilon\right\}\right|\, =\, 1\qquad \Rightarrow\qquad
\liminf_{n \to \infty} \frac{n^{4/9}}{k_n}\, >\, 0\, .
\end{equation}
He also  proved interesting equivalent formulations of his questions, and he has 
conjectures which remain as fascinating open problems.

We may follow the paradigm of iterating a random optimization problem.
See for example the {\em objective method} of Aldous and Steele \cite{AldousSteele}.
Especially, see the section on the ``Stalking horse,'' and distributional identities.
For the higher moments of the generalized Ulam problem,
the stalking horse is the covariance or even just the mixed moments
$$
\mathcal{Q}_n(k,\ell)\, =\, \mathbf{E}[Z_{n,k} Z_{n,\ell}]\, .
$$
This seems to be the first step towards iterating to go from the second moment to higher moments.
For example, for the third moment $\mathbf{E}[Z_{n,k} (Z_{n,k})^2]$, we may want to start
with $Q_n(k,2k)$. More precisely, the product $A(k-i,i) \cdot B(n,2k-i)$ gives the expected
number of pairs of increasing subsequence of $\pi \in S_n$, where each of the two subsequences
is of length $k$, and the number of points in the intersection is $i$. As before, $B(N,j)= C(N,j)/j!$
where $C(N,j)$ is the usual binomial coefficient $N! / (j! (N-j)!)$, throughout this article.

We would want to calculate the expectation for the pair of increasing subsequences of $\pi \in S_n$
where the first subsequence has length $k$ and the second subsequence has length $\ell$,
and the intersection has cardinality $i$.
Even though this seems like a clear goal, we will not pursue that goal in this article.
We hope to carry it out in a future article, either together or perhaps in a different collaboration
with one or both of the current authors.
Or perhaps, another researcher will do it first.
We hope that this is okay: we believe that the results already contained in the present article
are of interest to some readers, even without that further work (which is not done yet).
In this article, we just study the 2nd moment.
