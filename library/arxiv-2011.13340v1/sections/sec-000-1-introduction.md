---
doc_id: arxiv-2011.13340v1
doc_title: "A Matrix Bernstein Inequality for Strong Rayleigh Distributions *"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 2011.13340v1.pdf
source_sha256: e73876ed2c923608
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.977
doc_brief: "A Matrix Bernstein Inequality for Strong Rayleigh Distributions * — The Entropy method provides a powerful framework for proving scalar concentration in- equalities by establishing functional"
---
Concentration inequalities bound tail probabilities of general functions of random variables. Several methods have been known to prove such inequalities, including martingale methods, information theoretic methods, Talagrand's induction method as well as a variety of problem-specific methods. Ledoux (see \cite{Led} for a survey) developed a powerful framework known as the "entropy method" for proving concentration inequalities. This framework is concerned with proving functional inequalities (like Poincare and log-Sobolev inequalities) which bound some global divergence of any function whose concentration properties are of interest to us by quantities which measure "local variation" of this function under some diffusion process whose stationary measure is our measure of interest. This framework can be used to recover strong forms of concentration results for scalar functions which seem to be inaccessible through many other strategies for proving concentration. One prominent example of this is concentration of scalar Lipshitz functionals of distributions which are the stationary measure of some rapid mixing markov chain. We refer to the excellent book \cite{BLM13} for details on this and other methods for proving scalar concentration inequalities. The entropy method has also been immensely useful in proving deep theorems in the analysis of boolean functions and we refer the reader to \cite{OD} for more details on this fascinating topic.

The field of Matrix valued concentration of measure is concerned with the phenomenon of matrix valued functions being close (usually in spectral norm) to their expected value with high probability. In comparison to scalar concentration inequalities, results on Matrix concentration are much more recent. However, they have already had tremendous applications in the field of computer science, statistics and information theory. Some examples include applications to spectral graph theory, statistical learning problems, deep learning, sketching . While a large class of applications can be handled using matrix concentration of sums of independent random matrices, there are several applications where there is some dependence structure in the sums of random matrices. Some examples of such applications are simplifying Laplacian linear equations (cite), semi-streaming graph sparsification among others.

Despite the recent flurry of activity in proving and using matrix concentration inequalities, as pointed out by \cite{CT13}, one frequently encounters random matrices that do not submit to existing techniques and the study of matrix concentration inequalities remains an active area of investigation.

Negative dependence of random variables is an intuitive property that suggests that it might help with concentration of measure. A class of negatively dependent measures are strong Rayleigh measures which were introduced and deeply studied in the work of \cite{BBL09}. Examples of such distributions include determinantal measures and random spanning tree distributions. \cite{BBL09} show that strong Rayleigh distributions satisfy the strongest form of negative dependence properties. These negative dependence properties were recently exploited
to design approximation algorithms  (cite) They have also been used in numerical linear algebra and algorithmic fairness for selecting subsets of elements which maximize some notion of diversity.

In this paper, we are interested in understanding matrix concentration of random matrices whose distribution is coming from the stationary distribution of a Markov chain. While some results in this line of work exist in the work of \cite{PMT,MJCFT} which extends Chaterjee's work \cite{Chaterjee} on proving scalar concentration inequalities via Stein's method. The kind of markov chains that this line of work can handle is fairly restricted as it requires a stringent condition known as the Dobrushin condition which is not always to prove. Nevertheless, these results imply strong matrix concentration results in a variety of scenarios, most notably matrix Efron Stein inequalities. Another line of work is the paper of Chen and Tropp \cite{CT13} where they are  interested in extending the entropy method to the matrix valued case. However, their results are fairly restrictive since they require rotational symmetry of the random matrices. The reason for the rotational symmetry requirement is the need for a "Herbst argument" which requires building a differential equation for the exponential moment generating function. However, since \cite{CT13} can only control trace of quantities similar to variance and Dirichlet form (which we also study here). Since they are only controlling the trace, they can only transform the trace of those functions into a differential form assuming rotational symmetry of those matrices which lets them ignore any non-commutative structure of the sums of those random matrices. We refer the reader to \cite{CT13} for a more detailed discussion. Our main idea here is to construct matrix valued functional inequalities and show how these can be used to derive matrix concentration inequalities without any rotational symmetry assumption. While we cannot prove matrix valued (modified) log-Sobolev inequalities we do show that matrix concentration by establishing matrix valued Poincare inequalities (which are far more common for various markov chains as opposed to modified log-sobolev). While our techniques seem to be fairly general, we illustrate it for deriving matrix concentration for strongly Rayleigh measures.

We now formally define strong Rayleigh measures. Let $\mu : 2^{[n]}\rightarrow \mathbb{R}_{+}$ be a probability distribution on the subsets of $[n]=\{1,2,\ldots,n\}$. In particular, we assume that $\mu(\cdot)$ is nonnegative and $\sum\limits_{S \subseteq [n]}\mu(S)=1$. We associate a multi-affine polynomial with variables $z_1,\ldots,z_n$ to $\mu$
\begin{align*}
  g_\mu(z_1,\ldots,z_n)=\sum\limits_{S \subseteq [n]}\mu(S)\prod_{i\in S}z_i
\end{align*}
The polynomial $g_\mu$ is known as the generating polynomial of $\mu$. We say $\mu$ is $k$-homogenous if $g_\mu$ is a homegenous polynomial of degree $k$. A polynomial $p(z_1,\ldots,z_n)\in \mathbb{C}[z_1,\ldots,z_n]$ is said to be stable if whenever Im$(z_i)>0$ for all $i\in[n]$, $p(z_1,\ldots,z_n)\neq 0$. We say $p$ is real stable is $p$ is stable and all its coefficients are real.
Anari et al. \cite{AGR16} proved a mixing time bound by proving a poincare constant for a bases exchange markov chain associated to strong Rayleigh measures. Hermon and Salez\cite{HS19} gave a unified proof of a log-sobolev and Poincare inequality in the scalar case. One of our main results is showing that one can effortlessly follow their exact proof and make minor modifications(using operator convexity of certain functions) to prove a matrix valued Poincare inequality (which has also been considered in \cite{CHT15,CH15,CH16}). Our second main result implies that one can use matrix valued Poincare inequalities to prove matrix Bernstein like concentration inequalities. See \cite{Led} for how to prove similar concentration inequalities for scalar lipshitz valued functions using Poincare and log-sobolev inequalities. Combining our two main theorems, we get the following result.

\begin{theorem}\label{thm:srBern} Given a $k$-homogenous strong Rayleigh measure $\pi$ supported on $n$ elements and given a L-Lipshitz matrix valued function $\mathbf{F}:\{0,1\}^n\rightarrow\mathbb{S}_d$ and let $\mathbf{\mu}=\mathbb{E}_{x\sim\pi}[\mathbf{F(x)}]$. We have for all $t>0$,
  \begin{align*}
    \mathsf{Pr}_{x \sim \pi}[\|\mathbf{F(x)-\mathbf{\mu}}\|\geq t]\leq 2 de^{-t^2/32(kL^2 + t\sqrt{k}L)}
  \end{align*}
\end{theorem}
A matrix valued function $\mathbf{F}:\Omega\rightarrow \mathbb{S}_d$ is L-Lipshitz if for all $x,y \in \Omega$
\begin{align*}
  \|\mathbf{F(x)}-\mathbf{F(y)}\|\leq L\cdot d(x,y)
\end{align*}
with respect to some distance function between states $d(x,y)$. In this paper, we will use the hamming distance.
We remark that a matrix Chernoff bound for strong Rayleigh measures was proven by \cite{KyngSong18} by martingale arguments inspired by the scalar concentration case by \cite{PP14}. Their application was to prove that spanning trees can be used to construct spectral sparsifiers. While our concentration result can't prove a similar statement, our result can be used in situations theirs cant. We compare our result with theirs in Section \ref{sec:ks}.

We finally define some terminology we will require pertaining to Markov chains and refer the reader to \cite{MT06,LPW} for more details.  Let the stationary distribution of a reversible Markov chain with state space $\Omega$ be $\mu$
\begin{align*}
  \mathbb{E}_\mu[\mathbf{F}]&= \sum\limits_{x \in \Omega}\mu(x)\mathbf{F(x)}\\
  \mathbf{Var}_\mu[\mathbf{F}]&=\mathbb{E}_\mu[\mathbf{F}^2]-(\mathbb{E}(\mathbf{F(x)})^2
\end{align*}
Consider a generator for the Markov chain $Q\in\mathbb{R}^{\Omega\times\Omega}$ with non-negative off-diagonal entries with each row summing up to 0 and satisfying the local balance equations
\begin{align*}
  \pi(x)Q(x,y) = \pi(y)Q(y,x)
\end{align*}
For \textit{normalized} generators, one can associate a stochastic matrix $P$ such that $Q=P-I$. In such cases, $P$ also satsifies local balance. Finally, the Dirchlet form for scalar functions is $\mathcal{E}_Q[f,g]=\sum_{x\in\Omega,y\in\Omega}\pi(x)Q(x,y)(f(x)-f(y))^2$. It is easy to see that $\mathcal{E}_Q[f,g]=\mathcal{E}_P[f,g]$. For matrix valued functions $\mathbf{F,G}:\Omega\rightarrow \mathbb{S}_d$, the dirchlet form is defined as $\mathcal{E}_Q[\mathbf{F},\mathbf{G}]=\mathcal{E}_P[\mathbf{F},\mathbf{G}]=\sum_{x\in\Omega,y\in\Omega}\pi(x)Q(x,y)(\mathbf{F(x)}-\mathbf{F(y)})^2$
where $\mathbb{S}_d$ is the space of symmetric matrices of size $d\times d$.
