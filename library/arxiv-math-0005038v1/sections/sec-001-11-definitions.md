---
doc_id: arxiv-math-0005038v1
doc_title: "Braid groups are linear"
section_id: sec-001-11-definitions
section_title: "Definitions"
section_number: 1.1
pages: 1-2
source_pdf: 0005038v1.pdf
source_sha256: db0b9b7a8534f161
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.909
doc_brief: "Braid groups are linear — The braid groups Bn can be deﬁned as the mapping class group of the n-punctured disc."
---
Let $D$ be an oriented disc in the complex plane. Fix a set $P \subset D$ consisting of $n$ distinct points $p_1,\dots,p_n$ in the interior of $D$. Let ${\mathcal{H}}(D,P)$ be the group of all homeomorphisms $h \colon\thinspace D \rightarrow D$ such that $h(P) = P$ and $h$ fixes $\partial D$ pointwise. Let ${\mathcal{I}}(D,P)$ be the group of all such homeomorphisms which are isotopic to the identity relative to $P \cup \partial D$. We define the braid group $B_n$ to be the group ${\mathcal{H}}(D,P)/{\mathcal{I}}(D,P)$. See [@birman] for other equivalent definitions of these groups and a good introduction to their basic properties.

Let $C$ denote the space of all unordered pairs of distinct points in $D \setminus P$. In other words, $$C = 
\frac
{((D \setminus P) \times (D \setminus P)) \setminus \{(x,x)\}}
{(x,y) \sim (y,x)}
.$$ Let $d_1$ and $d_2$ be distinct points in $\partial D$. Let $c_0 = \{d_1,d_2\}$ be a basepoint for $C$.

We now define a map $\phi$ from $\pi_1(C,c_0)$ to the free Abelian group with basis $\{q,t\}$. Let $\alpha$ be a closed curve in $C$ based at $c_0$ representing an element $[\alpha]$ of $\pi_1(C,c_0)$. We can write $\alpha$ in the form $$\alpha(s) = \{\alpha_1(s),\alpha_2(s)\}$$ for some arcs $\alpha_1$ and $\alpha_2$ in $D \setminus P$. Let $$a = 
\frac{1}{2\pi i}
\sum_{j=1}^n
\left(
\int_{\alpha_1} \frac{dz}{z-p_j} + \int_{\alpha_2} \frac{dz}{z-p_j}
\right).$$ Let $$b = \frac{1}{\pi i} \int_{\alpha_1 - \alpha_2} \frac{dz}{z}.$$ Let $\phi([\alpha]) = q^a t^b$.

This definition requires some explanation. If $\alpha_1$ and $\alpha_2$ are closed loops then $a$ is the sum of the winding numbers of $\alpha_1$ and $\alpha_2$ around each of the puncture points, and $b$ is twice the winding number of $\alpha_1$ and $\alpha_2$ around each other. However $\alpha_1$ and $\alpha_2$ are not necessarily closed loops, but may "switch places". In this case, $a$ is the sum of the winding numbers of the closed loop $\alpha_1\alpha_2$ around each of the puncture points, and $\alpha_1 - \alpha_2$ satisfies $$(\alpha_1 - \alpha_2)(1) = - (\alpha_1 - \alpha_2)(0),$$ which implies that $b$ is an odd integer.

Let $\tilde{C}$ be the covering space of $C$ whose fundamental group is the kernel of $\phi$. Choose a lift $\tilde{c}_0$ of $c_0$ to $\tilde{C}$. Let $\Lambda$ denote the ring ${\bf{Z}}[q^{\pm 1},t^{\pm 1}]$. The homology group $H_2(\tilde{C})$ can be considered as a $\Lambda$-module, where $q$ and $t$ act by covering transformations.

Let $\sigma \in B_n$. There is an induced action of $\sigma$ on $C$. Let $\tilde{\sigma}$ be the lift of $\sigma$ to a map from $\tilde{C}$ to itself which fixes $\tilde{c}_0$. This induces a $\Lambda$-module automorphism $\tilde{\sigma}_*$ of $H_2(\tilde{C})$. The Lawrence-Krammer representation is the map from $B_n$ to $GL(H_2(\tilde{C}))$ taking $[\sigma]$ to $\tilde{\sigma}_*$.
