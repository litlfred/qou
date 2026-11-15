---
doc_id: arxiv-1804.10084v1
doc_title: "Concentration of Lipschitz Functions of Negatively Dependent Variables"
section_id: sec-002-2-notions-of-negative-dependence
section_title: "Notions of negative dependence"
section_number: 2
pages: 2-3
source_pdf: 1804.10084v1.pdf
source_sha256: 716da9708f06d930
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.932
doc_brief: "Concentration of Lipschitz Functions of Negatively Dependent Variables — We explore the question whether Lipschitz functions of random variables under various forms of negative correlation satisfy"
---
[]{#sec:neg-dep label="sec:neg-dep"}

Let us survey here several notions of negative dependence and their known relationships. In this paper, we restrict attention to (correlated) Bernoulli random variables, i.e. probability measures on $\{0,1\}^n$.

#### Pairwise Negative Correlation.

This is the weakest notion of negative dependence considered here. Variables $X_1,\ldots,X_n$ are pairwise negatively correlated, if $$\mathsf{Cov}[X_i,X_j] = {\mathbb E}[X_i X_j] - {\mathbb E}[X_i] {\mathbb E}[X_j] \leq 0$$ for all $i,j \in [n]$. Pairwise negative correlation allows one to use Chebyshev's inequality, but it is too weak to imply exponential tail bounds. For example, $n$ pairwise independent variables defined by the $n \times n$ Hadamard matrix have probability $\Omega(1/n)$ of being all equal to $1$.

#### Negative Cylinder Dependence.

$X_1,\ldots,X_n$ are negative cylinder dependent, if for every $S \subseteq [n]$, $${\mathbb E}[ \prod_{i \in S} X_i] \leq \prod_{i \in S} {\mathbb E}[X_i]$$ and $${\mathbb E}[ \prod_{i \in S} (1-X_i)] \leq \prod_{i \in S} {\mathbb E}[1-X_i].$$ Negative cylinder dependence is strictly stronger than pairwise negative correlation. It is known to imply exponential concentration bounds for linear functions of $X_1,\ldots,X_n$.

#### Negative Association.

$X_1,\ldots,X_n$ are negatively associated if for any $I,J \subset [n], I \cap J = \emptyset$ and any pair of non-decreasing functions $f:\{0,1\}^I \rightarrow {\mathbb R}$, $g:\{0,1\}^J \rightarrow {\mathbb R}$, $${\mathbb E}[f(X_I) g(X_J)] \leq {\mathbb E}[f(X_I)] {\mathbb E}[g(X_J)].$$ (Here and in the following, $X_S \in \{0,1\}^S$ denotes the $|S|$-tuple of random variables indexed by $S$.)

Negative association is strictly stronger than negative cylinder dependence. Whether negative association implies exponential concentration bounds for Lipschitz functions is an interesting question (posed by Elchanan Mossel [@PemPeres14] and still open as far as we know).

#### Negative Regression.

$X_1,\ldots,X_n$ satisfy negative regression, if for any $I,J \subset [n], I \cap J = \emptyset$, any non-decreasing function $f:\{0,1\}^I \rightarrow {\mathbb R}$ and $a \leq b \in \{0,1\}^J$, $${\mathbb E}[f(X_I) \mid X_J = a] \geq {\mathbb E}[f(X_I) \mid X_J = b].$$ Negative regression is the main subject of this paper; we prove a concentration bound for Lipschitz functions under negative regression here. The relationship of negative association and negative regression is not completely understood. It is known that negative association does not imply negative regression [@DubhashiRanjan98] but the status of the opposite implication is unknown. Negative regression is preserved under conditioning of variables, while negative association is not. It is easy to see that both properties are implied by the following.

#### Conditional Negative Association.

$X_1,\ldots,X_n$ are conditionally negatively associated, if for any $I \subset [n]$ and $a \in \{0,1\}^I$, $(X_j: j \in [n] \setminus I)$ conditioned on $X_I = a$ are negatively associated.

 

Pemantle [@Pemantle00] conjectured that conditional negative association is equivalent to negative regression. He also defined several related notions that entail the "negative lattice condition\" (log-submodularity) and "external fields\". We will not discuss these here.

#### Stochastic Covering.

$X_1,\ldots,X_n$ satisfy the stochastic covering property, if for any $I \subset [n]$ and $a \geq a' \in \{0,1\}^I$ such that $\| a' - a \|_1 = 1$, there is a coupling $\nu$ of the distributions $\mu, \mu'$ of $(X_j: j \in [n] \setminus I)$ conditioned on $X_I = a$ or $X_I=a'$, respectively, such that $\nu(x,y)=0$ unless $x \leq y$ and $\|x-y\|_1 \leq 1$.

 

This property is discussed in [@PemPeres14]. It is stronger than negative regression (which is equivalent to a similar coupling condition, without the requirement that the coupling is supported on pairs of distance at most $1$; this follows from Strassen's theorem as we discuss further).

#### The Strong Rayleigh Property.

$X_1,\ldots,X_n$ satisfy the strong Rayleigh property if the generating function $F(z_1,\ldots,z_n) = {\mathbb E}[\prod_{j=1}^{n} z_j^{X_j}]$ is a real stable polynomial, which means it has no root $(z_1,\ldots,z_n) \in {\mathbb C}^n$ with all imaginary components strictly positive.

The strong Rayleigh property is intimately tied to the theory of stable polynomials, and it was shown in [@BBL09] to imply all the other forms of negative dependence discussed above. Hence, it can be viewed as a very strong and robust notion of negative dependence --- it is closed under several natural operations, and exhibits a number of other desirable properties. Particularly relevant to this paper is the result of [@PemPeres14] that any Lipschitz function of random variables under a strong Rayleigh measure satisfies concentration bounds similar to independent random variables. Furthermore, [@PemPeres14] also proves a concentration bound for Lipschitz functions for homogeneous random variables ($\sum_{i=1}^{n} X_i = k$ for some constant $k$, with probability $1$) satisfying the stochastic covering property.
