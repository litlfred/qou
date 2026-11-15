---
doc_id: arxiv-2302.05903v2
doc_title: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials"
section_id: sec-010-strong-superintegrability-in-the-p-gaussian-mode
section_title: "Strong superintegrability in the p-Gaussian model"
section_number: null
pages: 9-11
source_pdf: 2302.05903v2.pdf
source_sha256: 9a17abd36cc8a317
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.967
doc_brief: "On combinatorial generalization(s) of Borel transform: Averaging method in combinatorics of symmetric polynomials — We elaborate on the recent suggestion to consider averaging of Cauchy identities"
---
In the $p$-Gaussian model with the measure ([\[Gm\]](#Gm){reference-type="ref" reference="Gm"}), which is under our consideration in this paper, there is a formula for the bilinear correlator similar to ([\[da\]](#da){reference-type="ref" reference="da"}), however, in this case, one has to deal with the operators[^1] $\hat W_\Delta^{(0)}$. They are defined as $$\begin{aligned}
\hat W_\Delta^{(0)}={1\over z_\Delta}\ :\ \prod_{i=1}^{l_\Delta}{\rm Tr}\,\left(\Lambda{\partial\over\partial\Lambda}\right)^{\delta_i}\ :
\end{aligned}$$ where $\Lambda$ is a matrix such that the $p_k$-variables are parameterized as $p_k={\rm Tr}\,\Lambda^k$, and the invariant operators $\hat W_\Delta^{(0)}$ can be rewritten as operators in $p_k$-variables. The normal ordering here, $:\ldots:$ means that all the derivatives are placed to the rightmost positions.

Note that these operators $\hat W_\Delta^{(0)}$ require the normal ordering, otherwise they would depend on the size of the $\Lambda$ matrix [@MMN]. In the case of operators $\hat W_\Delta^{(-)}$ in ([\[da\]](#da){reference-type="ref" reference="da"}), normal ordering did not affect the answer. Note that the Schur functions form a set of eigenfunctions of $\hat W_\Delta^{(0)}$: $$\begin{aligned}
\hat W_\Delta^{(0)}S_R=\phi_R(\Delta)S_R
\end{aligned}$$ where the eigenvalue $\phi_R(\Delta)$ is manifestly expressed through the symmetric group characters $\psi_\mu(\Delta)$ by [@IK; @Ok; @MMNspin] $$\begin{aligned}
\phi_R(\Delta)=\sum_{\mu\vdash\Delta} {S_{R/\mu}\{\delta_{k,1}\}\over S_R\{\delta_{k,1}\}}{\psi_\mu(\Delta)\over z_\Delta}
\end{aligned}$$ Now using the identity $$\begin{aligned}
\sum_{\Delta\vdash P}\psi_P(\Delta)\phi_R(\Delta)={S_{R/P}\{\delta_{k,1}\}\over S_{R}\{\delta_{k,1}\}}
\end{aligned}$$ which follows from the orthogonality relation $$\begin{aligned}
\sum_\Delta{\psi_P(\Delta)\psi_R(\Delta)\over z_\Delta}=\delta_{PR}
\end{aligned}$$ one finally comes to the formula $$\begin{aligned}
\boxed{
\Big<S_P\{\hat W^{(-)}_k\}\cdot S_R\{p_k\}\Big>^{\bf A}={S_{R/P}\{\delta_{k,1}\}\over S_{R}\{\delta_{k,1}\}}
}
\end{aligned}$$

Now, using integration by parts, one could again recast the action of the $S_P(\hat W^{(0)}_k)$-operators into the action to the measure ([\[Gm\]](#Gm){reference-type="ref" reference="Gm"}) in order to produce a complete set of polynomials $K_P\{p_k\}$ of $p_k$: $$\begin{aligned}
\Big<S_P\{\hat W^{(-)}_k\}\cdot S_R\{p_k\}\Big>^{\bf A}=\int d\mu^{\bf A}S_P\{\hat W^{(-)}_k\}\cdot S_R\{p_k\}=\int d\mu^{\bf A}S_P\{{\overleftarrow{W^{(0)}}}\}\cdot S_R\{p_k\}=\int d\mu^{\bf A}K_P\{p_k\}\cdot S_R\{p_k\}
\end{aligned}$$ where we use the left arrow to denote the operator acting to the left. Thus, one could construct this way the map $S_P\{{\overleftarrow{W^{(0)}}}\}\longrightarrow K_P\{p_k\}$. However, there is a problem in doing this.

To see the problem, let us consider the simplest case of the operator $\hat W_{[1]}^{(0)}$, which is manifestly given by $$\begin{aligned}
\hat W_{[1]}^{(0)}=\sum_{a=1}^\infty ap_a{\partial\over\partial p_a}
\end{aligned}$$ When integrating by parts, this operator acts to the measure ([\[Gm\]](#Gm){reference-type="ref" reference="Gm"}) as $$\begin{aligned}
\overleftarrow{W_{[1]}^{(0)}}=-\sum_{a=1}^\infty a{\partial\over\partial p_a}\cdot p_a=-\sum_{a=1}^\infty ap_a{\partial\over\partial p_a}-\sum_{a=1}^\infty a
\end{aligned}$$ The last sum requires some regularization $\sum_{a=1}^\infty a\longrightarrow\sigma_{reg}$, and, when acting to the measure, this operator produces a function, not a polynomial. Still, the Schur functions are eigenfunctions of this operator. If one acts to the Gaussian measure ([\[Gm\]](#Gm){reference-type="ref" reference="Gm"}) with this operator, one obtains $$\begin{aligned}
\left(-\sum_{a=1}^\infty ap_a{\partial\over\partial p_a}-\sigma_{reg}\right)\cdot\underbrace{\prod_{k=1}^\infty
dp_k\exp\left(-\frac{(p_{2k-1}-1)^2}{2(2k-1)} - \frac{p_{2k}^2}{4k}\right)}_{d\mu}
=\left(\sum_{k=1}^\infty (p_k^2-p_{2k-1})-\sigma_{reg}\right)\cdot d\mu
\end{aligned}$$ i.e. $$\begin{aligned}
K_{[1]}\{p_k\}=\sum_{k=1}^\infty (p_k^2-p_{2k-1})-\sigma_{reg}
\end{aligned}$$ At the second level, the formulas are even more involved. Indeed, consider the operator $\overleftarrow{W^{(0)}_{[2]}}$, which is given by $$\begin{aligned}
\overleftarrow{W^{(0)}_{[2]}}=\sum_{a,b}^\infty abp_{a+b}{\partial^2\over\partial p_a\partial p_b}-\sum_{a,b}^\infty (a+b)p_ap_b{\partial\over\partial p_{a+b}}
\end{aligned}$$ In this case, there are no infinite sums emerging from differentiating within the operator, however, in contrast with the standard $\hat W^{(0)}_{[2]}$-operator [@GJ; @MMN], $$\begin{aligned}
\overrightarrow{W^{(0)}_{[2]}}=\sum_{a,b}^\infty abp_{a+b}{\partial^2\over\partial p_a\partial p_b}+\sum_{a,b}^\infty (a+b)p_ap_b{\partial\over\partial p_{a+b}}
\end{aligned}$$ whose eigenfunctions are the Schur functions, the eigenfunctions of $\overleftarrow{W^{(0)}_{[2]}}$ do not form a complete basis in the space of graded polynomials of $p_k$. For instance, at grading 3, $$\begin{aligned}
\overleftarrow{W^{(0)}_{[2]}}S_R=A_{RP}S_P
\end{aligned}$$ where the matrix $$\begin{aligned}
A_{RP}=\left(
\begin{array}{ccc}
0&-4&2\cr
4&0&-4\cr
-2&4&0
\end{array}
\right)
\end{aligned}$$ is degenerate: it has rank 2. Here we labelled the indices: $[3]\to 1$, $[21]\to 2$, $[111]\to 3$.

The action of $\overleftarrow{W^{(0)}_{[2]}}$ to the Gaussian measure ([\[Gm\]](#Gm){reference-type="ref" reference="Gm"}) is now cubic in $p_k$: $$\begin{aligned}
\left(\sum_{a,b}^\infty abp_{a+b}{\partial^2\over\partial p_a\partial p_b}-\sum_{a,b}^\infty (a+b)p_ap_b{\partial\over\partial p_{a+b}}\right)d\mu
=\\
=\left(4\sum_{k=1}^\infty p_k^2p_{2k}-4\Big(\sum_{k=1}^\infty p_{2k-1}\Big)\Big(\sum_{k=1}^\infty p_{2k}\Big)
+2\sum_{a>b\ge 1}^\infty p_ap_bp_{a+b}\right)\cdot d\mu
\end{aligned}$$ i.e. $$\begin{aligned}
K_{[2]}=4\sum_{k=1}^\infty p_k^2p_{2k}-4\Big(\sum_{k=1}^\infty p_{2k-1}\Big)\Big(\sum_{k=1}^\infty p_{2k}\Big)
+2\sum_{a>b\ge 1}^\infty p_ap_bp_{a+b}
\end{aligned}$$ This is a general rule: any $K_R$ is a polynomial of degree $|R|+1$ in $p_k$, however, it involves $p_k$ with arbitrary large index $k$, and also involves infinite sums, which require a regularization. All this requires a careful treatment, which we postpone for a separate publication.

[^1]: The superscript "0\" here refers to a commutative part of the $w_{\infty}$ algebra, while the superscript "-\" in the previous subsection to its Borel part.
