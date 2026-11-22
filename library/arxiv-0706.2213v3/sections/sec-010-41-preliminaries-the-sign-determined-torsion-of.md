---
doc_id: arxiv-0706.2213v3
doc_title: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS"
section_id: sec-010-41-preliminaries-the-sign-determined-torsion-of
section_title: "Preliminaries: the sign-determined torsion of a CW-complex"
section_number: 4.1
pages: 12-14
source_pdf: 0706.2213v3.pdf
source_sha256: 75dd29acc9e34bda
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.978
doc_brief: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS — This paper gives an explicit formula for the SL 2(C)−non–abelian Reidemeister torsion as deﬁned in [Dub06] in the case of twist knots."
---
We review the basic notions and results about the sign--determined Reidemeister torsion introduced by Turaev which are needed in this paper. Details can be found in Milnor's survey~\cite{Milnor:1966} and in Turaev's monograph~\cite{Turaev:2002}.


\subsubsection{Torsion of a chain complex}
Let $C_* = (\xymatrix@1@-.5pc{0 \ar[r] & C_n \ar[r]^-{d_n} & C_{n-1} \ar[r]^-{d_{n-1}} & \cdots \ar[r]^-{d_1} & C_0 \ar[r] & 0})$ be a chain complex of finite dimensional vector spaces over $\mathbb{C}$. Choose  a basis $\mathbf{c}^i$ of $C_i$ and  a basis $\mathbf{h}^i$ of the $i$-th homology group $H_i = H_i(C_*)$. The torsion of $C_*$ with respect to these choices of bases is defined as follows.

Let $\mathbf{b}^i$ be a sequence of vectors in $C_{i}$ such that $d_{i}(\mathbf{b}^i)$ is a basis of $B_{i-1}= \im(d_{i} \colon C_{i} \to C_{i-1})$ and let $\widetilde{\mathbf{h}}^i$ denote a lift of $\mathbf{h}^i$ in $Z_i = \ker(d_{i} \colon C_i \to C_{i-1})$. The set of vectors $d_{i+1}(\mathbf{b}^{i+1})\widetilde{\mathbf{h}}^i\mathbf{b}^i$ is a basis of $C_i$. Let $[d_{i+1}(\mathbf{b}^{i+1})\widetilde{\mathbf{h}}^i\mathbf{b}^i/\mathbf{c}^i] \in \mathbb{C}^*$ denote the determinant of the transition matrix between those bases (the entries of this matrix are coordinates of vectors in $d_{i+1}(\mathbf{b}^{i+1})\widetilde{\mathbf{h}}^i\mathbf{b}^i$ with respect to $\mathbf{c}^i$). The \emph{sign-determined Reidemeister torsion} of $C_*$ (with respect to the bases $\mathbf{c}^*$ and $\mathbf{h}^*$) is the following alternating product (see~\cite[Definition 3.1]{Turaev:2000}):
\begin{equation}
\label{Def:RTorsion}
\mathrm{Tor}(C_*, \mathbf{c}^*, \mathbf{h}^*) = (-1)^{|C_*|} \cdot  \prod_{i=0}^n [d_{i+1}(\mathbf{b}^{i+1})\widetilde{\mathbf{h}}^i\mathbf{b}^i/\mathbf{c}^i]^{(-1)^{i+1}} \in \mathbb{C}^*.
\end{equation}
Here  $$|C_*| = \sum_{k\geqslant 0} \alpha_k(C_*) \beta_k(C_*),$$ where $\alpha_i(C_*) = \sum_{k=0}^i \dim C_k$ and  $\beta_i(C_*)  = \sum_{k=0}^i \dim H_k$.

The torsion $\mathrm{Tor}(C_*, \mathbf{c}^*, \mathbf{h}^*)$ does not depend on the choices of $\mathbf{b}^i$ and $\widetilde{\mathbf{h}}^i$. 
Note that if $C_*$ is acyclic (i.e. if $H_i = 0$ for all $i$), then $|C_*| = 0$.










\subsubsection{Torsion of a CW-complex}
Let $W$ be a finite CW-complex and $\rho$ be an $\SL$-re\-pre\-sen\-ta\-tion of $\pi_1(W)$. We define the $\sll_{\rho}$-twisted chain complex of $W$ to be
\[
C_*(W; \sll_\rho) = C_*(\widetilde{W}; \ZZ) \otimes_{\ZZ[\pi_1(W)]} \sll_\rho.
\]
Here $C_*(\widetilde{W}; \ZZ)$ is the complex of the universal cover with integer coefficients which is in fact a $\ZZ[\pi_1(W)]$-module (via the action of $\pi_1(W)$ on $\widetilde{W}$ as the covering group), and $\sll_\rho$ denotes the $\ZZ[\pi_1(W)]$-module via the composition $Ad \circ \rho$, where $Ad \colon \SL \to \mathrm{Aut}(\sll), A \mapsto Ad_A$, is the adjoint representation. The chain complex $C_*(W; \sll_\rho)$ computes the {$\sll_\rho$-twisted homology} of $W$ which we denote as $H_*^\rho(W) = H_i(W; Ad \circ \rho)$.

Let $\left\{e^{(i)}_1, \ldots, e^{(i)}_{n_i}\right\}$ be the set of $i$-dimensional cells of $W$. We lift them to the universal cover and we choose an arbitrary order and an arbitrary orientation for the cells $\left\{ {\tilde{e}^{(i)}_1, \ldots, \tilde{e}^{(i)}_{n_i}} \right\}$. If $\mathcal{B} = \{\mathbf{a}, \mathbf{b}, \mathbf{c}\}$ is an orthonormal basis of $\sll$, then we consider the corresponding  basis over $\CC$
$$\mathbf{c}^{i}_{\mathcal{B}} = \left\{ \tilde{e}^{(i)}_{1} \otimes \mathbf{a}, \tilde{e}^{(i)}_{1} \otimes \mathbf{b}, \tilde{e}^{(i)}_{1} \otimes \mathbf{c}, \ldots, \tilde{e}^{(i)}_{n_i}\otimes \mathbf{a}, \tilde{e}^{(i)}_{n_i} \otimes \mathbf{b}, \tilde{e}^{(i)}_{n_i}\otimes \mathbf{c}\right\}$$ of $C_i(W; \sll_\rho) = C_*(\widetilde{W}; \ZZ) \otimes_{\ZZ[\pi_1(W)]} \sll_\rho$. Now choosing for each $i$ a basis $\mathbf{h}^{i}$ of the $\sll_\rho$-twisted homology $H_i^\rho(W)$, we can compute the torsion
$$\mathrm{Tor}(C_*(W; \sll_\rho), \mathbf{c}^*_{\mathcal{B}}, \mathbf{h}^{*}) \in \CC^*.$$

The cells $\left\{ \tilde{e}^{(i)}_j \right\}^{}_{0 \leqslant i \leqslant \dim W, 1 \leqslant j \leqslant n_i}$ are in one--to--one correspondence with the cells of $W$, their order and orientation induce an order and an orientation for the cells $\left\{ e^{(i)}_j \right\}^{}_{0 \leqslant i \leqslant \dim W, 1 \leqslant j \leqslant n_i}$. Again, corresponding to these choices, we get a basis $c^i$ over $\IR$ of $C_i(W; \IR)$. 

Choose an \emph{homology orientation} of $W$, which is an orientation of the real vector space $H_*(W; \IR) = \bigoplus_{i\geqslant 0} H_i(W; \IR)$. Let $\mathfrak{o}$ denote this chosen orientation. Provide each vector space $H_i(W; \IR)$ with a reference basis $h^i$ such that the basis $\left\{ {h^0, \ldots, h^{\dim W}} \right\}$ of $H_*(W; \IR)$ is {positively oriented} with respect to $\mathfrak{o}$. Compute the sign--determined Reidemeister torsion $\mathrm{Tor}(C_*(W; \IR), c^*, h^{*}) \in \IR^*$ of the resulting based and homology based chain complex and consider its sign $$\tau_0 = \mathrm{sgn}\left(\mathrm{Tor}(C_*(W; \IR), c^*, h^{*})\right) \in \{\pm 1\}.$$  

We define the (sign--refined)  twisted  Reidemeister torsion of $W$ {(with respect to $\mathbf{h}^{*}$ and $\mathfrak{o}$)} to be
\begin{equation}\label{EQ:TorsionRaff}
\mathrm{TOR}(W; \sll_\rho, \mathbf{h}^{*}, \mathfrak{o}) = \tau_0 \cdot \mathrm{Tor}(C_*(W; \sll_\rho), \mathbf{c}^*_{\mathcal{B}}, \mathbf{h}^{*}) \in \mathbb{C}^*.
\end{equation}
This definition only depends on the combinatorial class of $W$, the conjugacy class of $\rho$, the choice of $\mathbf{h}^{*}$ and the {homology} orientation $\mathfrak{o}$. It is independent of the orthonormal basis $\mathcal{B}$ of $\sll$, of the choice of the lifts $\tilde{e}^{(i)}_j$, and of the choice of the positively oriented basis of $H_*(W; \IR)$. Moreover, it is independent of the order and orientation of the cells (because they appear twice). 

One can prove that $\mathrm{TOR}$ is invariant under cellular subdivision, homeomorphism and simple homotopy equivalences. In fact, it is precisely the sign $(-1)^{|C_*|}$ in Eq.~(\ref{Def:RTorsion}) which ensures all these important invariance properties to hold.
