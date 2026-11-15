---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-010-3-fusion-categories-over-c
section_title: "Fusion categories over C"
section_number: 3
pages: 10-12
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.939
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
The goal of this subsection is to prove Theorem [\[posi\]](#posi){reference-type="ref" reference="posi"}, Proposition [\[pivo\]](#pivo){reference-type="ref" reference="pivo"}, Proposition [\[modu\]](#modu){reference-type="ref" reference="modu"}, and discuss their consequences.

Let ${\mathcal C}$ denote a fusion category over ${\mathbb{C}}$. We will denote representatives of isomorphism classes of simple objects of ${\mathcal C}$ by $X_i$, $i\in I$, with $0\in I$ labeling the neutral object $\mathbf{1}$. Denote by $*: I\to I$ the dualization map. (We note that at the level of labels, there is no distinction between right and left dualization, since by Proposition [\[doubledual\]](#doubledual){reference-type="ref" reference="doubledual"}, $V$ is isomorphic to $V^{**}$ for any simple object $V$).

## Proof of Theorem [\[posi\]](#posi){reference-type="ref" reference="posi"}

By Theorem [\[fourstars\]](#fourstars){reference-type="ref" reference="fourstars"}, there exists an isomorphism of tensor functors $g: \text{Id}\to ****$. Let us fix such an isomorphism. So for each simple $V\in {\mathcal C}$ we have a morphism $g_V: V\to V^{****}$ such that $g_{V\otimes W}=g_V\otimes g_W$, and $g_{V^*}=(g_V^{-1})^*$. For all simple $V$, let us fix an isomorphism $a_V : V\to V^{**}$ such that $a_V^2=g_V$ ($a_V^2$ makes sense as ${\rm Hom}(V,V^{**})$ is canonically isomorphic to ${\rm Hom}(V^{**},V^{****})$, and so $a_V$ can also be regarded as an element of ${\rm Hom}(V^{**},V^{****})$). Then $a_{V^*}=\epsilon_V (a_V^{-1})^*$, where $\epsilon_V=\pm 1$, and $\epsilon_V\epsilon_{V^*}=1$. Define $d(V)=\text{Tr}_V(a_V)$, in particular $d_i=d(X_i)$. These numbers are not at all canonical -- they depend on the choices we made. Nevertheless, it is easy to see from the definition that $|V|^2=\epsilon_V d(V)d(V^*)$.

Now let us take any simple objects $V,W\in {\mathcal C}$ and consider the tensor product $a_V\otimes a_W: V\otimes W\to (V\otimes W)^{**}$. We have $V\otimes W=\oplus_U {\rm Hom}(U,V\otimes W)\otimes U$, so we have $a_V\otimes a_W=\oplus b_{U}^{VW}\otimes a_U$, where $b_U^{VW}: {\rm Hom}(U,V\otimes W)\to {\rm Hom}(U^{**},V^{**}\otimes W^{**})$. The source and target of this map are actually canonically isomorphic, so we can treat $b_U^{VW}$ as an automorphism of ${\rm Hom}(U,V\otimes W)$. Also, since $a_V^2=g_V$ and $g_{V\otimes W}=g_V\otimes g_W$, we get $(b_U^{VW})^2=1$.

Let $b_j^{ik}:=b_{X_j}^{X_iX_k}$. Let $T_j^{ik}={\rm tr}(b_j^{ik})$. Since $(b_j^{ik})^2=1$, its eigenvalues are $\pm 1$, hence $T_j^{ik}$ are integers.

By the definition of $b_j^{ik}$, we have $$d_id_k=\sum_{j\in I}T_j^{ik}d_j$$ Let $T_i$ be the matrix such that $(T_i)_{kj}=T_j^{ik}$, and let $\mathbf d$ be the vector with components $d_i$. This vector is clearly nonzero (e.g., $d_0\ne 0$), and we have $$T_i\mathbf d=d_i\mathbf d.$$ Thus, $\mathbf d$ is a common eigenvector of $T_i$ with eigenvalue $d_i$.

Let $\epsilon_i=\epsilon_{X_i}$. Then we have: $\mathbf d$ is an eigenvector of the matrix $A_i=\epsilon_i T_iT_{i^*}$ with eigenvalue $|X_i|^2$.

We claim that $T_{i^*}=\epsilon_i T_i^t$. This implies the theorem, as in this case $A_i=T_iT_i^t$, which is nonnegative definite (since the entries of $T_i$ are integer, hence real), so its eigenvalues, including $|X_i|^2$, have to be nonnegative.

To prove that $T_{i^*}=\epsilon_i T_i^t$, we need to show that $T_{j}^{i^*k}=\epsilon_i T_k^{ij}$. But this, in turn, follows from the equality $b_j^{i^*k}=\epsilon_i (b_k^{ij})^*$ (which makes sense since we have canonical isomorphisms ${\rm Hom}(U,V\otimes W)\to {\rm Hom}(V^*\otimes U,W)\to 
{\rm Hom}(W,V^*\otimes U)^*$, the latter by semisimplicity).

It remains to prove the last equality. Let $f: X_j\to X_i\otimes X_k$ be a morphism. By the definition, $b_j^{ik}f=(a_i\otimes a_k)fa_j^{-1}$. On the other hand, $f$ gives rise to an element $f': X_{i^*}\otimes X_j\to X_k$, given by $f'=({\rm ev}_i\otimes 1)(1\otimes f)$, and hence to a linear function on ${\rm Hom}(X_k,X_{i^*}\otimes X_j)$ given by $f''(h)=({\rm ev}_i\otimes 1)(1_{i^*}\otimes f)h\in {\rm End}(X_k)={\mathbb{C}}$ (for brevity we omit associativity maps and use the same notation for a morphism and its double dual). Now, we have $$\begin{aligned}
(b_j^{ik}f)''(h)
&=& ({\rm ev}_i\otimes 1)(1_{i^*}\otimes (a_i\otimes a_k)fa_j^{-1})h \\
&=& \epsilon_i a_k({\rm ev}_i\otimes 1)(a_{i^*}^{-1}\otimes fa_j^{-1})h \\
&=& \epsilon_i  ({\rm ev}_i\otimes 1)(1\otimes f)(a_{i^*}^{-1}\otimes a_j^{-1})ha_k \\
&=& \epsilon_i ({\rm ev}_i\otimes 1)(1\otimes f)(a_{i^*}\otimes a_j)ha_k^{-1},
\end{aligned}$$ where the last equality due to the facts that $g_{V\otimes W}=g_V\otimes g_W$, and $a_V=g_Va_V^{-1}$. Thus, $$(b_j^{ik}f)''(h)=
f''(b_k^{i^*j}h),$$ as desired. Theorem [\[posi\]](#posi){reference-type="ref" reference="posi"} is proved.

::: remark
[]{#pivotalization label="pivotalization"} Here is a modification of the above proof, which is simpler but requires an extension of the category ${\mathcal C}$.

The first step is to prove the result in the case of pivotal categories. This is a substantially simplified version of the above proof, since in the pivotal case $\epsilon_i$ and $b_j^{ik}$ are 1, so $T_j^{ik}$ are equal to $N_j^{ik}$, the multiplicity of $X_j$ in $X_i\otimes X_k$.

The second step is reduction to the pivotal case. To do this, take the isomorphism $g: Id\to ****$ as tensor functors constructed in the proof of Theorem [\[fourstars\]](#fourstars){reference-type="ref" reference="fourstars"}. Define the fusion category $\tilde {\mathcal C}$, whose simple objects are pairs $(X,f)$, where $X$ is a simple object of ${\mathcal C}$, and $f:X\to X^{**}$ is an isomorphism, such that $f^{**}f=g$. It is easy to see that this fusion category has a canonical pivotal structure. Thus, $|X|^2>0$ in $\tilde{\mathcal C}$. However, we have the forgetful functor $F:\tilde {\mathcal C}\to {\mathcal C}$, $F(X,f)=X$, which obviously preserves squared norms. Hence, $|V|^2>0$ for simple objects $V$ in ${\mathcal C}$ (since for any $V$ there exists $f:V\to
V^{**}$ such that $f^{**}f=g$), which completes the proof.
:::
