---
doc_id: arxiv-2111.04763v2
doc_title: "Resurgence of Chern-Simons theory at the trivial flat connection"
section_id: sec-002-12-a-summary-of-our-results
section_title: "A summary of our results"
section_number: 1.2
pages: 4-5
source_pdf: 2111.04763v2.pdf
source_sha256: 760a7f9794e8baaa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.964
doc_brief: "Resurgence of Chern-Simons theory at the trivial flat connection — Some years ago, it was conjectured by the first author that the Chern–Simons perturbation theory of a 3-manifold at the trivial flat"
---
[]{#sub.summary label="sub.summary"}

Our goal is to describe the Stokes constants and the resurgent structure of the missing asymptotic series $\Phi^{(\sigma_0)}(h)$ in terms of completing the matrix $\mathbf J^\mathrm{red}(x,q)$ to a square matrix with one extra row (namely $(1,0,\dots,0)^T$) and column, whose distinguished $(\sigma_0,\sigma_1)$ entry is conjecturally the Gukov--Manolescu series [@Gukov-Manolescu] (evaluated at $x=1$), and the remaining series in the top row are the descendants of the Gukov-Manolescu series.

Along the way of solving the resurgence problem for the $\Phi^{(\sigma_0)}(h)$ series, we solve several related problems, which we now discuss.

$\bullet$ **A $q$-series that sees $\Phi^{(\sigma_0)}(h)$.** This is a problem raised by Gukov and his collaborators (see e.g. [@Gukov:BPS; @Gukov-Manolescu]). More precisely, our Resurgence Conjecture [\[conj-exact-ra\]](#conj-exact-ra){reference-type="ref" reference="conj-exact-ra"} implies that the asymptotics as $q=e^{2\pi{\rm i}\tau}$ and $\tau \to 0$ in a sector of each of the $q$-series of the top row of the matrix $\mathbf J(q)$ is a linear combination of the $\Phi^{(\sigma)}(h)$ series which includes the $\Phi^{(\sigma_0)}(h)$ series.

$\bullet$ **A matrix-valued holomorphic quantum modular form.** In [@GZ:qseries] the first author and Don Zagier studied a matrix $\mathbf J^\mathrm{red}(q)$ of $q$-series with rows indexed by nontrivial flat connections, and conjectured that the corresponding value of the cocycle $\mathbf J(\tilde{q})^{-1} \Delta(\tau) \mathbf J(q)$[^1] at $S=\bigl(\smallmatrix 0&-1\\1&0\endsmallmatrix\bigr) \in \mathrm{SL}_2(\mathbbm Z)$, which a priori is an analytic function on $\mathbbm C\setminus\mathbbm R$, actually extends to the cut plane $\mathbbm C'$. A problem posed was to find an extension of the matrix $\mathbf J^\mathrm{red}(q)$ which includes the trivial flat connection. We do so in Sections [\[sub.41q3\]](#sub.41q3){reference-type="ref" reference="sub.41q3"}, [\[sub.41qx\]](#sub.41qx){reference-type="ref" reference="sub.41qx"} and [\[sub.52q3\]](#sub.52q3){reference-type="ref" reference="sub.52q3"} for the $\mathbf{4}_1$ and $\mathbf{5}_2$ knots.

$\bullet$ **An exact form of the Refined Quantum Modularity Conjecture.** In [@GZ:kashaev] a Refined Quantum Modularity Conjecture was formulated. The conjecture was numerically motivated by a smoothed optimal summation of the divergent series $\Phi^{\sigma)}(\tau)$, and the final result was a matrix-valued periodic function defined at the rational numbers. We conjecture that if we replace the smoothed optimal truncation by the median Borel resummation, all asymptotic statements in [@GZ:kashaev] become exact equalities, valid for finite (and not necessarily large) range of the parameters.

$\bullet$ **An analytic extension of the Kashaev invariant and of the colored Jones polynomial.** A consequence of the above conjecture is an exact formula for the Kashaev invariant at rational points as a linear combinations of three smooth functions, multiplied by the top row of $\mathbf J$.

::: conjecture
[]{#conj.ekashaev label="conj.ekashaev"} For every knot $K$ and every natural number $N$ we have: $$\label{ekashaev}
  \langle K \rangle_N = \sum_{\sigma} c^K_\sigma N^{\delta_\sigma} 
  s_{\rm med}( \Phi^{(K,\sigma)})(\tfrac{1}{N})$$ where $\delta_\sigma=3/2$ for $\sigma\neq \sigma_0$ and $\delta_{\sigma_0}=1$ and $(c^K_\sigma)$ is a vector of elements of the Habiro ring (tensor $\mathbbm Q$) evaluated at $q=1$, with $c^K_{\sigma_1}=c^K_{\sigma_0}=1$.
:::

The vector $(c_\sigma)$ for the $\mathbf{4}_1$ knot appears in Sec.4.2 of [@GZ:kashaev] and also as the top row of the matrix of Eqn.(92), and for the $\mathbf{5}_2$ knot it appears in Section 4.3 as well as the top row of the matrix of Eqn.(104) of ibid.

For the $\mathbf{4}_1$ and the $\mathbf{5}_2$ knots, we find numerically that $c^{\mathbf{4}_1}_{\sigma_2}=0$, $c^{\mathbf{5}_2}_{\sigma_2}=0$ and $c^{\mathbf{5}_2}_{\sigma_3}=-2$ in complete agreement with the results of [@GZ:kashaev]. A corollary of [\[ekashaev\]](#ekashaev){reference-type="eqref" reference="ekashaev"} is the Volume Conjecture $\langle K \rangle_N \sim N^{3/2} \Phi^{(K,\sigma)}(\tfrac{1}{N})$ to all orders in $1/N$ as $N \to \infty$.

::: conjecture
[]{#conj.ejones label="conj.ejones"} For every knot $K$, there is a neighborhood $U^K$ of $0$ in the complex plane, such that for every natural number $N$ and for $u \in U^K$, we have $$\label{ejones}
  J^K_N(e^{\frac{2\pi{\rm i}}{N}+\frac{u}{N}})=  \sum_{\sigma} \delta_\sigma(u,N) c^K_\sigma(\tilde{x})
  s_{\rm med}( \Phi^{(K,\sigma)})(e^u;\tau)$$ where $\delta_{\sigma}(u,N)=\tau^{-1/2} \frac{\tilde{x}^{1/2}-\tilde{x}^{-1/2}}{x^{1/2}-x^{-1/2}}$ for $\sigma\neq \sigma_0$ and $\delta_{\sigma_0}(x,\tau)=1$, where $x=e^u$, $\tilde{x}=e^{u/x}$, $\tau=\tfrac{u}{2\pi{\rm i}N}+\tfrac{1}{N}$, and $c^K_\sigma(\tilde{x}) \in \mathbbm Q[\tilde{x}^{\pm 1}]$ with $c^K_{\sigma_1}(\tilde{x})=c^K_{\sigma_0}(\tilde{x})=1$.
:::

For the $\mathbf{4}_1$ and the $\mathbf{5}_2$ knots, we find numerically that $c^{\mathbf{4}_1}_{\sigma_2}(\tilde{x})=-\frac{\tilde{x}-\tilde{x}^{-1}}{2}$, $c^{\mathbf{5}_2}_{\sigma_2}(\tilde{x})=-\frac{\tilde{x}-\tilde{x}^{-1}}{2}$ and $c^{\mathbf{5}_2}_{\sigma_3}(\tilde{x})=-1-\tilde{x}$.

Since $\lim_{u\to 0} \delta_\sigma(N,u)=N^{\delta_s}$, the above conjecture specialises to Conjecture [\[conj.ekashaev\]](#conj.ekashaev){reference-type="ref" reference="conj.ekashaev"} when $u \to 0$. Note also that the above conjecture implies the Generalised Volume Conjecture when $u \not\in \pi {\rm i}\mathbbm Q$ is fixed and $N \to \infty$. Indeed, $\delta(N,u)$ is nonzero and $J^{K}_N(e^{(2\pi{\rm i}+u)/N}) 
\sim \delta(N,u)\Phi^{(\sigma_1)}(e^u;\tau)$. Note finally that the above conjecture explains the failure of exponential growth when $u$ is a rational multiple of $2\pi{\rm i}$, known for all knots from theorems 1.10 and 1.11 of [@GL:asy], and theorem 5.3 of [@Murakami2011:ivc] valid for the $\mathbf{4}_1$ knot. Indeed, when $u=2\pi{\rm i}r/s$ for integers $r$ and $s$ with $r/s$ near zero, then $J^{K}_N(e^{(2\pi{\rm i}+u)/N})$ is a periodic function of $N$ (see [@Ha]), and so is $\delta(N,u)$ since $e^{u/\tau}=e^{2\pi{\rm i}N r/(r+s)}$. Moreover, $\delta(N,u)=0$ when $N$ is a multiple of $r+s$ which explains why in that case the colored Jones polynomial does not grow exponentially.

$\bullet$ **An extension of the 3D-index.** Our completed matrix proposes a computable extension of the 3D-index in the sector of the trivial connection $\sigma_0$, whose mathematical or physical definition is yet-to-be given.

[^1]: For a suitable diagonal matrix $\Delta(\tau)$ of weights.
