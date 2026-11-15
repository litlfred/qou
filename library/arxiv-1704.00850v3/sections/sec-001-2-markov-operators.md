---
doc_id: arxiv-1704.00850v3
doc_title: "Estimating the spectral gap of a trace-class Markov operator"
section_id: sec-001-2-markov-operators
section_title: "Markov operators"
section_number: 2
pages: 4-5
source_pdf: 1704.00850v3.pdf
source_sha256: 09dd9c99453ba251
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 1.0
doc_brief: "Estimating the spectral gap of a trace-class Markov operator — The utility of a Markov chain Monte Carlo algorithm is, in large part, determined by the size of the spectral gap of the corresponding"
---
[]{#MarkovOperators label="MarkovOperators"}

Assume that the Markov chain $\Phi$ has a Markov transition density, $p(u, \cdot),\,u \in S$, such that, for any measurable $A \subset S$ and $u \in S$, $$\mathbb{P}(\Phi_k \in A|\Phi_0 = u) = \int_A p^{(k)}(u,u') \,
        \mu(du') \,,$$ where $$p^{(k)}(u,\cdot) := \left\{
    \begin{array}{@{}ll@{}}
    p(u,\cdot)  & k=1 \\
    \int_S p^{(k-1)}(u,u') p(u',\cdot) \, \mu(du') & k > 1 \,
    \end{array} \right.$$ is the $k$-step Mtd corresponding to $p(u,\cdot)$. We will assume throughout that $\Phi$ is Harris ergodic, i.e. irreducible, aperiodic and Harris recurrent. Define a Hilbert space consisting of complex valued functions on $S$ that are square integrable with respect to $\pi(\cdot),$ namely $$L^2(\pi) := \Big\{ f:S \to \mathbb{C} \; \Big \arrowvert \,
        \int_{S} |f(u)|^2 \pi(u) \, \mu(du) < \infty \Big\} \,.$$ For $f, g \in L^2(\pi),$ their inner product is given by $$\langle f, g \rangle_{\pi} = \int_{S} f(u) \overline{g(u)}
        \pi(u) \, \mu(du) \,.$$ We assume that $\mathcal{U}$ is countably generated, which implies that $L^2(\pi)$ is separable and admits a countable orthonormal basis [see e.g. @billingsley2008probability Theorem 19.2]. The transition density $p(u,\cdot), \, u\in S$ defines the following linear operator $P.$ For any $f \in L^2(\pi),$ $$Pf(u) = \int_{S} p(u,u') f(u') \, \mu(du') \,.$$ The spectrum of a linear operator $L$ is defined to be $$\sigma(L) = \big \{ \lambda \in \mathbb{C} \, \big | \,
        (L-\lambda I)^{-1} \text{ doesn't exist or is unbounded} \big
        \} \,,$$ where $I$ is the identity operator. It is well-known that $\sigma(P)$ is a closed subset of the unit disk in $\mathbb{C}.$ Let $f_0 \in L^2(\pi)$ be the normalized constant function, i.e. $f_0(u) \equiv 1$, then $Pf_0 = f_0$. (This is just a fancy way of saying that 1 is an eigenvalue with constant eigenfunction, which is true of *all* Markov operators defined by ergodic chains.) Denote by $P_0$ the operator such that $P_0 f = Pf - \langle f, f_0 \rangle_{\pi} f_0$ for all $f \in
        L^2(\pi).$ Then the spectral gap of $P$ is defined as $$\delta = 1 - \sup \Big\{ |\lambda| \, \Big| \, \lambda \in
        \sigma(P_0) \Big\} \,.$$

For the remainder of this section, we assume that $P$ is non-negative (and thus self-adjoint) and compact. This implies that $\sigma(P) \subset [0,1]$, and that any non-vanishing element of $\sigma(P)$ is necessarily an eigenvalue of $P$. Furthermore, there are at most countably many eigenvalues, and they can accumulate only at the origin. Let $\lambda_0, \lambda_1, \dots, \lambda_{\kappa}$ be the decreasingly ordered strictly positive eigenvalues of $P$ taking into account multiplicity, where $0 \leq \kappa \leq
        \infty$. Then $\lambda_0=1$ and $\lambda_1$ is what we previously referred to as the "second largest eigenvalue" of the Markov operator. If $\kappa = 0$, we set $\lambda_1 = 0$ (which corresponds to the trivial case where $\{\Phi_k\}_{k=0}^{\infty}$ are iid). Since $\Phi$ is Harris ergodic, $\lambda_1$ must be strictly less than $1$. Also, the compactness of $P$ implies that of $P_0$, and it's easy to show that $\sigma(P_0) = \sigma(P) \backslash \{1\}$. Hence, $\Phi$ is geometrically ergodic and the spectral gap is $$\delta = 1-\lambda_1 > 0 \,.$$ For further background on the spectrum of a linear operator, see e.g. [@helmberg2014introduction] or [@ahues2001spectral].
