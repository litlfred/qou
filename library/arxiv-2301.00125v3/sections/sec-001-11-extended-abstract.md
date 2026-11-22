---
doc_id: arxiv-2301.00125v3
doc_title: "Generating Function for Pinsky’s Combinatorial Second Moment Formula for the Generalized Ulam Problem"
section_id: sec-001-11-extended-abstract
section_title: "Extended abstract"
section_number: 1.1
pages: 1-2
source_pdf: 2301.00125v3.pdf
source_sha256: 7ecd0cff7d6c2ec4
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.934
doc_brief: "Generating Function for Pinsky’s Combinatorial Second Moment Formula for the Generalized Ulam Problem — Given a uniform random permutation π ∈Sn, let Zn,k be equal to the number of increasing"
---
In two papers Ross Pinsky considered a random variable $Z_{n,k}$ equal to the number of increasing subsequences of length $k$
in a uniform random permutation $\pi \in S_n$. 
That investigation may be called the ``generalized Ulam problem,'' because: 
if $L_n$ is the length of the longest increasing subsequence for a uniform random $\pi \in S_n$, then $\left(L_n< k\right)
\Leftrightarrow \left(Z_{n,k}=0\right)$. 
The generalized Ulam problem is to investigate the distribution $\mathbf{P}(Z_{n,k}\leq j)$,
possibly asymptotically as $n \to \infty$, for both variables $j$ and $k$.





Among other things, Pinsky proved $\mathbf{E}\big[Z_{n,k}^2\big]$
is equal to $\sum_{i} A(k-i,i)B(n,2k-i)$, where for any nonnegative integers $N$ and $j$, we have $B(N,j) =  C(N,j)/j!$.
Let us use $C(N,j)$ for the binomial
coefficient $(j! (N-j)!)^{-1} N!$, throughout.
The combinatorial array $A(N,j)$, which is a nonnegative
integer for each $N,j \in \{0,1,\dots\}$, is
equal to $4^{N} \mathbf{E}[Q_{N,j} \cdot R_N]$,
where $R_N$ and $Q_{N,j}$ are random variables defined on the sample space for a $d=2$ dimensional SRW.
If a sample path of the SRW up to time $2N$ is $(0,0)=(U_0,V_0),(U_1,V_1),\dots,(U_{2N},V_{2N})$, then 
$Q_{N,j}$ is the number of choices of $(t_0,\dots,t_{j-1}) \in \Z^{j}$
such that $0=t_0\leq t_1\leq \dots\leq t_{j-1}<2N$ satisfying $U_{t_1}=\dots=U_{t_j}=0$, and 
$R_N$
is the indicator for the event that $(U_{2N},V_{2N})=(0,0)$.
If the occupation time of the $y$-axis is $\tau_{N}$ then $Q_{N,j}$ equals $C(\tau_{N}+j-1,j)$
by the ``stars-and-stripes'' problem.

Pinsky obtained rigorous general bounds which are sufficient to determine the applicability of the Paley-Zygmund method to prove a weak law of large numbers for $Z_{n,k}$: $k=k_n$ is {\fontsize{6}{7}{${\mathcal{O}}$}}$(n^{2/5})$ as $n \to \infty$.
In a follow-up paper he also proved a regime where the weak law does not hold for $Z_{n,k}$:
$k=k_n$ is such that $1/k_n$ is  {\fontsize{6}{7}{${\mathcal{O}}$}}$(1/n^{4/9})$ as $n \to \infty$.
We calculate the generating function for his $A(N,j)$ sequence. Our method is 
the complex analysis approach, as in the excellent reference of Pemantle and Wilson.
We find a closed formula for $\alpha(z,w)=\sum_{N=0}^{\infty} \sum_{j=0}^{2N} A(N,j) z^N w^j$ 
which involves elliptic integrals of the third kind $\Pi$.
Recall P\'olya's
generating function formula for the return time of a random walk: $g(z) = \sum_{N} z^{2N} \mathbf{E}[R_N]$ equals $K(z)/\pi$, where $K$ is the complete elliptic integral of the first kind.
This satisfies $g(z)=\alpha(z,0)$.
We also give some motivation.
