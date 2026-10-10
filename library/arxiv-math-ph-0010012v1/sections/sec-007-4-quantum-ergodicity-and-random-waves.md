---
doc_id: arxiv-math-ph-0010012v1
doc_title: "From random polynomials to symplectic geometry Steve Zelditch"
section_id: sec-007-4-quantum-ergodicity-and-random-waves
section_title: "Quantum ergodicity and random waves"
section_number: 4
pages: 6-7
source_pdf: 0010012v1.pdf
source_sha256: cd6eca5ccb81ff90
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.97
doc_brief: "From random polynomials to symplectic geometry Steve Zelditch — We review some recent results on random polynomials and their generalizations in complex and symplectic geometry."
---
We end with a brief discussion of the connection between random polynomials and quantum chaos. The intutitive idea that quantum chaotic eigenfunctions should resemble 'Gaussian random waves' seems to have been first suggested by M. V. Berry [@B]. A precise formulation of this random wave model and some numerical results are given in [@ABST] [@HR].

Random spherical harmonics on $S^m$, or random combinations of eigenfunctions of Laplacians on general compact Riemannian manifolds as described above, provide a rather different random wave model for quantum chaotic eigenfunctions. To motivate the model, we recall that the diagonal sums of squares $$\begin{equation}
\label{QE} S_p(\lambda) = \sum_{j: \lambda_j \leq \lambda} |(A \varphi_j, \varphi_j) - \bar{\sigma_A}|^p,\;\;\;
(\mbox{with}\;\;\bar{\sigma_A} = \int_{S^*M} \sigma_A d \mu),
\end{equation}$$ and their off-diagonal analogues, are used to characterize eigenfunctions as quantum ergodic, quantum mixing and so on. Here, $A$ is an observable (zeroth order pseudodifferential operator), $\sigma_A$ is its principal symbol. For quantizations of ergodic systems, $S_p(\lambda) \to 0$ as $\lambda \to \infty$, and it is of some interest to measure the rate and to relate it to the classical dynamics. In the random spherical harmonics model one has the following rate (for similar results see [@Ze2; @SZ1]):

::: theo
([@Ze1], Lemma (2.15)) Let $\{\varphi_{N j}\}$ be a random orthonormal basis of spherical harmonics of $S^2$. Then: $E (S_2(N)) = \frac{1}{N}[\frac{1}{vol(S^*S^2)} \int_{S^*S^2}|\sigma^{ave}_A(\zeta) - \bar{\sigma_A}|^2 d\mu(\zeta)] + O(1/N^2).$
:::

The optimist may conjecture a similar rate for quantum chaotic eigenfunctions. In [@Ze1] it is further proved that almost all orthonormal bases of spherical harmonics are quantum ergodic, and this was improved to quantum unique ergodicity by VanderKam [@V]. On the level of quantum mixing, however, random spherical harmonics do not provide a good model, but random combinations of Laplace eigefunctions on generic Riemannian manifolds do; that was the motivation for studying the model in [@Ze2]. Quantum mixing systems involve off-diagonal sums like ([\[QE\]](#QE){reference-type="ref" reference="QE"}) with constant gaps between eigenvalues. Conversely, if the eigenfunctions satisfy ([\[QE\]](#QE){reference-type="ref" reference="QE"}) and the analogous off-diagonal estimates for all gaps, then the system is classically mixing. Hence the random wave model is not a good model for ergodic systems which fail to be mixing (cf. [@HKZ]).

A further relation between Gaussian random waves and quantum chaotic eigenfunctions does not seem to have been explored, even numerically. Let $\{\varphi_{\lambda}\}$ be eigenfunctions of a quantum chaotic system, and consider the local rescaling $\varphi_{\lambda}(x_0 + \frac{u}{\lambda}).$ The rescaled eigenfunction is an eigenfunction of the rescaled operator, which is asymptotically Euclidean. Hence $\varphi_{\lambda}(x_0 + \frac{u}{\lambda})$ can be expanded asymptotically in terms of plane waves, and one might ask how the frequencies are distributed.
