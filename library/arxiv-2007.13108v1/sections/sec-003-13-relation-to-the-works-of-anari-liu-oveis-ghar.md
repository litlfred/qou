---
doc_id: arxiv-2007.13108v1
doc_title: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-003-13-relation-to-the-works-of-anari-liu-oveis-ghar
section_title: "Relation to the works of Anari, Liu, Oveis-Gharan and Vinzant"
section_number: 1.3
pages: 5-6
source_pdf: 2007.13108v1.pdf
source_sha256: b298478f5f5b948d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 1.0
doc_brief: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube — It is well-known that measures whose density is the form e−V where V is a uniformly convex potential on Rn attain"
---
A seemingly related notion of log-concavity of measures on the discrete hypercube was given in a series of works by Anari, Liu, Oveis-Gharan and Vinzant in \cite{AOV2,AOV1}. Given $\{-1,1\}$-Bernoulli random variables $X_1,\dots,X_n$ distributed according to a law $\nu$, which can be identified with a random subset $A \subset [n]$ by $X_i = 2 \mathbf{1}_{i \in A} - 1$, they consider the generating polynomial
$$
p_\nu(z_1,...,z_n) = \EE \prod_{i \in A} z_i.
$$
They show that if $p$ is both log-concave on the positive orthant and homogeneous (which is equivalent to the fact $\sum_i X_i$ is supported on one point), then the law of $X_1,...X_n$ admits, among other things, strong concentration properties in the form of a spectral gap (with respect to the Glauber dynamics). 

It is not hard to check that the log-concavity of the polynomial $p_\nu$ is equivalent to the condition
\begin{equation}\label{eq:condaov}
\nabla^2 \mathcal{L}[\nu] (x) \preceq 2 \left (\mathrm{diag} \left (\nabla \mathcal{L}[\nu] (x) \right ) + \Id \right ), ~~ \forall x \in \RR^n.
\end{equation}
Since $\nabla \mathcal{L}[\nu] (x) \in [-1,1]^n$, the above condition is strictly stronger our semi-log-concavity condition \eqref{eq:semilc} with $\beta=4$. 

On a first glance it may seem that Theorem \ref{thm:main} is effectively similar to \cite[Theorem 1.1]{AOV2} (and could perhaps follow from the same methods), however we believe that this is not the case, and the resemblance between the two results is mainly on a superficial level. A crucial difference between the results is that our notion of log-concavity is invariant under reflections about the coordinate axes, whereas in the latter notion, the direction $(1,...,1)$ has a special role. In cases of interest, such as homogeneous distributions where $|A| \ll n$, condition \eqref{eq:condaov} is actually closer to strict log-concavity. 

Since the multi-linear polynomial $p_\nu$ is harmonic, its log-concavity implies that the Hessian matrix can have only one non-negative eigenvalue. In this sense, condition \eqref{eq:condaov} is much more rigid than our condition. Respectively, while our proof is based mainly on analytic methods, the proof in \cite{AOV2} has a more algebraic flavor (and is also based the theory of high-dimensional expanders). We do not know if there is a deeper connection between the results, but it doesn't seem that any of the two follows from the other. 

On the other hand, Theorem \ref{thm:entropy} seems rather closely related to \cite[Theorem 5.2]{AOV1}, and the former can be thought of as a soft and modified version of the latter: Indeed, condition \eqref{eq:semilc2}, compared to \eqref{eq:condaov} is invariant under coordinate reflections and softer in the sense that $\beta$ can be larger than $1$, but otherwise rather similar. The proof of the latter is simpler and basically reduces to an application of Jensen's inequality, whereas our proof (a small variation thereof also implies the latter bound) is slightly more complicated and uses stochastic calculus; we do not know if it can be attained by more elementary techniques.

Finally, in relation to Corollary \ref{cor:TNC}, a result of a similar spirit appears in \cite{anari2020spectral}. A corollary of the main theorem there shows that if $\nu$ is $d$-homogeneous and all measures obtainable from $\nu$ by conditioning are pairwise-negatively correlated, then it has a spectral gap polynomial in $n$. It seems however, that the assumption of homogeneouity is crucial in this case. 


\subsubsection{Acknowledgements}
We'd like to thank Bo'az Klartag for a fruitful discussion, as well as Nima Anari and Jan Vondrak and Pranav Nuti for some enlightening comments on a preliminary version of this manuscript.
