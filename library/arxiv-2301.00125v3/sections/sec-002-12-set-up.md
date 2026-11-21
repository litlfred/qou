---
doc_id: arxiv-2301.00125v3
doc_title: "Generating Function for Pinsky’s Combinatorial Second Moment Formula for the Generalized Ulam Problem"
section_id: sec-002-12-set-up
section_title: "Set-up"
section_number: 1.2
pages: 2-3
source_pdf: 2301.00125v3.pdf
source_sha256: 7ecd0cff7d6c2ec4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 1.0
doc_brief: "Generating Function for Pinsky’s Combinatorial Second Moment Formula for the Generalized Ulam Problem — Given a uniform random permutation π ∈Sn, let Zn,k be equal to the number of increasing"
---
{
Ulam's problem is a problem that involves a combination of tools and techniques
from the intersection of various subfields and specialities in mathematics, statistics  and physics.
It has been studied by many top researchers.
The main results are beautiful but diffficult.


The depth of the results related to Ulam's problem is well-known.
There are good reviews. 
See, for example, the review article of Aldous and Diaconis \cite{AldousDiaconis}. 
Many new and important results have been discovered since the publication of that particular paper.
One notable recent development is the directed landscape perspective \cite{Virag}.

We will state the actual problem known as Ulam's problem.
Let $\pi$ be a random permutation in $S_n$, chosen according to the uniform measure.
So for any permutation in $S_n$, the probability for $\pi$ to equal that one permutation is 
$1/n!$.
Ulam's problem involves increasing subsequences for $\pi$.
Given a cardinality $k$ subset of $\{1,\dots,n\}$, we may write the set as 
$\{i_1,\dots,i_k\}$ for 
\begin{equation}
1\leq i_1<\dots<i_k\leq n\, . 
\end{equation}
Then we say that 
$(i_1,\dots,i_k)$ is an increasing subsequence for $\pi$ if 
\begin{equation}
\pi_{i_1}\, <\, \dots\, <\, \pi_{i_k}\, .
\end{equation}
If we fix $(i_1,\dots,i_k)$ and vary over $\pi$, then the probability of the event,
``$(i_1,\dots,i_k)$
is an increasing subsequence for $\pi$,'' is equal to $1/k!$.
This is because if we are given $k$ numbers $\{j_1,\dots,j_k\}$
satisfying
\begin{equation}
\label{eq:jIncreasing}
1\, \leq\, j_1\, <\, \dots\, <\, j_k\, \leq\,  n\, ,
\end{equation}
and we are told that we have equality of the sets
\begin{equation}
\label{eq:jpiSubset}
	\{\pi_{i_1},\dots,\pi_{i_k}\}\, =\, \{j_1,\dots,j_k\}\, ,
\end{equation}
then there are still $k!$ possible permutations $\sigma=(\sigma_1,\dots,\sigma_k) \in S_k$ 
such that 
\begin{equation}
\label{eq:jpiOrdered}
	\forall r \in \{1,\dots,k\}\, ,\ \text{ we have }\ \pi_{i_r} = j_{\sigma_r}\, .
\end{equation}
But for $(i_1,\dots,i_r)$ to be an increasing subsequence for $\pi$, then we want $\pi_{i_r} = j_r$ for all $r$.
That means $\sigma = (1,2,\dots,k)$, the identity element of $S_k$, which is just one of the $k!$ possible permutations.

Ulam's problem is to determine the distribution of $L(n)$, the length of the longest increasing subsequence for $\pi$:
the largest $k$ such that there is at least one subsequence $(i_1,\dots,i_k)$ which is increasing for $\pi$.
Hammersley used Markov's bound and Kingman's subadditive theorem to garner information about $L(n)$
in the large $n$ limit.
Let $Z_{n,k}(\pi)$ denote the number of subsequences of cardinality $k$ which are increasing for $\pi$:
\begin{equation}
\label{eq:defZnk}
	Z_{n,k}(\pi)\, =\, \sum_{i_1,\dots,i_k=1}^{n} \prod_{r=1}^{n-1} \left(\mathbf{1}_{(0,\infty)}(i_{r+1}-i_r) \cdot \mathbf{1}_{(0,\infty)}(\pi_{i_{r+1}}-\pi_{i_r})\right)\, .
\end{equation}
Then $\sum_{i_1,\dots,i_k=1}^{n}  \prod_{r=1}^{n-1} \mathbf{1}_{(0,\infty)}(i_{r+1}-i_r)$ is equal to $n$-choose-$k$,
and for each $(i_1,\dots,i_k)$ we know 
\begin{equation}
	 \mathbf{P}(\pi_{i_1}<\dots<\pi_{i_k})\, =\, \frac{1}{k!}\, ,
\end{equation}
where the probability is over the uniform measure on $\pi \in S_n$ (with $(i_1,\dots,i_k)$ held fixed).
 Therefore,
\begin{equation}
\label{eq:Zmean}
	\mathbf{E}[Z_{n,k}]\, =\, \binom{n}{k} \cdot \frac{1}{k!}\, .
\end{equation}
Then, using Markov's inequality, it is easily seen that
\begin{equation}
\label{ineq:Markov}
	\mathbf{P}(Z_{n,k}>0)\, =\, \mathbf{P}(L(n)\geq k)\, \leq\, \mathbf{E}[Z_{n,k}]\, .
\end{equation}
Then, by Stirling's formula, writing $x$ for $k/\sqrt{n}$,
\begin{equation}
\label{eq:FirstMoment}
	\binom{n}{k} \cdot \frac{1}{k!}\,  \sim\, \frac{\exp\left(-2x n^{1/2}\, \ln\left(x/e\right) -\frac{1}{2}\, x^2+ \delta_n(x)\right)}{2 \pi x n^{1/2} (1 - x n^{-1/2})^{1/2}}\, ,
\end{equation}
in the limit $k \to \infty$, $n-k \to \infty$, where
\begin{equation}
	\delta_n(x)\, =\, x n^{1/2} \ln\left(1-x n^{-1/2}\right)- 
n\, \ln\left(e^{x n^{-1/2}}\left(1-x n^{-1/2}\right)\right)+\frac{x^2}{2}\, ,
\end{equation}
which would be $o(1)$ as long as $xn^{-1/2} = o(1)$.
In \cite{Hammersley}, Hammersley used the subadditive ergodic theorem to prove that 
\begin{equation}
	\liminf_{n \to \infty} n^{-1/2}\, \mathbf{E}[L_n]\, =\, \limsup_{n \to \infty} n^{-1/2}\, \mathbf{E}[L_n]\, =\, c\, ,
\end{equation}
for some number $c$ which {\em a priori} could have been in $(0,\infty]$.
But by equation (\ref{eq:FirstMoment}), he noted $c\leq e$.
In fact, an equally simple argument using the Erd\"os-Szekeres theorem
gives $c\geq 1/2$.
See, for example, Section 1.4 of J.M.~Steele's monograph \cite{Steele}.

The actual mean is approximately $c\, n^{1/2}$ for $c=2$,
by a result of Vershik and Kerov \cite{VershikKerov}, and a partial result of Logan and Shepp \cite{LoganShepp}.
Moreover, there is a
complete characterization of the leading-order fluctuations for large $n$, according to the Baik-Deift-Johannson theorem
\cite{BDJ}.
And new results are being continually discovered for the leading-order fluctuations, such as the ``directed landscape'' picture \cite{Virag}.
