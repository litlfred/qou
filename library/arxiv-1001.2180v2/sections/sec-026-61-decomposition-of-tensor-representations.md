---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-026-61-decomposition-of-tensor-representations
section_title: "Decomposition of tensor representations"
section_number: 6.1
pages: 23-24
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.972
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
[]{#subsect:def_SW label="subsect:def_SW"} We consider the following representation of the symmetric group: $\mathfrak{S}_n$ acts on the space $(\mathbb{C}^N)^{\otimes n}$ by commuting the vectors of the pure tensors. Its character is very easy to compute: $\chi(\rho)=N^{\ell(\rho)}$, where $\ell(\rho)$ is the number of parts of the partition $\rho$ (or, equivalently, the number of cycles of any permutation of type $\rho$).

This representation can be decomposed into irreducible representations of $\mathfrak{S}_n$: let us denote $m_\lambda$ the multiplicity of the irreducible module $S_\lambda$. We associate to this decomposition the following measure on partitions $$\mathbb{P}[\lambda] = \frac{m_\lambda \cdot \dim(S_\lambda)}{N^n}.$$ In other words, $\mathbb{P}[\lambda]$ is the dimension of the isotypic component of type $\lambda$ divided by the total dimension of the module $(\mathbb{C}^N)^{\otimes n}$. Note that this is a very natural way to construct a measure on Young diagrams of a given size: the same construction with the regular representation gives rise to the Plancherel measure.

What is interesting with this kind of measure is that the expectation of rescaled character values is proportional to the character of the representation. In the case we are looking at (the action of $\mathfrak{S}_n$ on $(\mathbb{C}^N)^{\otimes n}$), $$\begin{aligned}
 \mathbb{E}[\Sigma_\rho] & = n^{\downarrow |\rho|} \cdot \frac{\chi(\rho 1^{n-|\rho|})}{N^n} \\ &= n^{\downarrow |\rho|} \cdot N^{\ell(\rho) - |\rho|}.
\end{aligned}$$ Let us finish this paragraph with a little remark. By Schur-Weyl duality, one has the following isomorphism of $\mathfrak{S}_n \times \mathrm{GL}(N,\mathbb{C})$-modules $$(\mathbb{C}^N)^{\otimes n} \simeq \bigoplus_{\lambda \vdash n,\ell(\lambda)\leq N} V_\lambda \otimes U_\lambda,$$ where $U_\lambda$ is an irreducible $\mathrm{GL}(N,\mathbb{C})$-module. Moreover, the dimension of $U_\lambda$ is the number of semi-standard tableaux of shape $\lambda$ with entries lower or equal than $N$. So, $$\mathbb{P}[\lambda] = \frac{\left|\left\{\text{\begin{tabular}{c}
                         standard tableaux\\
             of shape $\lambda$
                        \end{tabular}}\right\}\right|
                \cdot
\left|\left\{\text{\begin{tabular}{c}
                         semistandard tableaux\\
             of shape $\lambda$ (entries $\leq N$)
                        \end{tabular}}\right\}\right|
}{N^n}.$$ This implies, as mentioned in paragraph [\[subsect:ss_suite_croissante\]](#subsect:ss_suite_croissante){reference-type="ref" reference="subsect:ss_suite_croissante"}, that this measure is in fact the image of the uniform distribution on words of length $n$ and letters from $1$ to $N$ by the RSK algorithm. On the other hand, notice that the Schur-Weyl measure charges only the Young diagrams whose lengths are smaller than $N$.
