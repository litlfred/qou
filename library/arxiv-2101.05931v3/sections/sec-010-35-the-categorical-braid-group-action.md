---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-010-35-the-categorical-braid-group-action
section_title: "The categorical braid group action"
section_number: 3.5
pages: 9-10
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.923
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
Let $\cC$ be a categorical representation of $U_q(\fg), \mu \in X$ and $i\in I$.     
We define a complex of functors $\Theta_i\bone_\mu$, supported in nonpositive cohomological degrees, where for $r\geq0$ the $-r$ component is
\begin{align*}
(\Theta_i\bone_\mu)^{-r}=\begin{cases}\sE_i^{(-\mu_i+r)}\sF_i^{(r)}\bone_\mu\langle -s \rangle &\text{ if } \mu_i\leq0, \\
\sF_i^{(\mu_i+r)}\sE_i^{(r)}\bone_\mu\langle -r \rangle &\text{ if } \mu_i\geq0.
\end{cases}
\end{align*}
The differential $d^r:(\Theta_i\bone_\mu)^{-r} \to (\Theta_i\bone_\mu)^{-r+1}$ is defined using the counits of the bi-adjunctions relating $\sE_i$ and $\sF_i$ (see \cite[Section 4]{Cauclasp} for details).  This produces a functor $\Theta_i\bone_\mu:D^b(\cC_\mu)\to D^b(\cC_{s_i(\mu)})$, which following Chuang and Rouquier we call the \textbf{Rickard complex}.


It's straightforward to verify that the Rickard complex $\Theta_i\bone_\mu$ categorifies Lusztig's braid group operators $\st_i\sone_\mu$ (\cite[Section 2]{Cauclasp}).
On the level of categories we have the following two theorems of Chuang-Rouquier and Cautis-Kamnitzer, which are the fundamental results about  Rickard complexes.  Note that the latter theorem was conjectured in \cite[Conjecture 5.19]{Rou2KM}.

\begin{Theorem}\cite[Theorem 6.4]{CR}\label{thm:CR}
For any $\mu,i$, $\Theta_i\bone_\mu:D^b(\cC_\mu)\to D^b(\cC_{s_i(\mu)})$ is an equivalence of triangulated categories.
\end{Theorem}

\begin{Theorem}\cite[Theorem 6.3]{CK3}\label{thm:CK}
The Rickard complexes satisfy the braid relations:
\begin{align*}
\Theta_i\Theta_j\bone_\mu &\cong \Theta_j\Theta_i\bone_\mu \text{ if } (i,j)=0,\\
\Theta_i\Theta_j\Theta_i\bone_\mu &\cong \Theta_j\Theta_i\Theta_j\bone_\mu \text{ if } (i,j)=-1,
\end{align*}
thereby defining a weak action of $B$ on $D^b(\cC)$.
\end{Theorem}

This action is ``weak'' since we don't make any claim on the canonicity of the functorial isomorphisms.  Nevertheless, for $w \in W$ we define $\Theta_w\bone_\mu := \Theta_{i_1}\circ\cdots\circ\Theta_{i_\ell}\bone_\mu$, where $w=s_{i_1}\cdots s_{i_\ell}$ is a reduced expression.  Thus  $\Theta_w\bone_\mu$ is defined up to isomorphism, but not canonical isomorphism.  Luckily, everything we do in this paper only requires $\Theta_w\bone_\mu$ to be defined up to isomorphism.


As a consequence of their proof of Theorem \ref{thm:CR}, Chuang and Rouquier show that the inverse  of $\Theta_i\bone_\mu$ is its right adjoint.  We denote this functor by $\Theta_i'\bone_{\mu}:D^b(\cC_\mu)\to D^b(\cC_{s_i(\mu)})$, so that $\Theta_i\Theta_i'\bone_\mu \cong \Theta'_i\Theta_i\bone_\mu \cong \bone_\mu$.  As a complex of functors, $\Theta_i'\bone_\mu$ is supported in nonnegative cohomological degrees, where for $s\geq0$ the $s$ component is
\begin{align*}
(\Theta_i'\bone_\mu)^s =\begin{cases}
\sE_i^{(s)}\sF_i^{(\mu_i+s)}\bone_\mu\langle s(-2\mu_i-2s+1) \rangle &\text{ if } \mu_i \geq 0, \\
\sF_i^{(s)}\sE_i^{(-\mu_i+s)}\bone_\mu\langle s(-2\mu_i+2s+1) \rangle&\text{ if } \mu_i \leq 0.
\end{cases}
\end{align*}
