---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-029-74-character-sheaves-again
section_title: "Character sheaves again"
section_number: 7.4
pages: 42-43
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
text_source: latex
latex_prose_ratio: 0.833
latex_coverage_ratio: 1.0
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
Now we apply our previous results to our motivating example when $X=BB$, $Y=BG$, for a reductive group $G$ and Borel subgroup $B\subset G$. We take $\tilde X = BN$, for the unipotent radical $N\subset B$, and take $\mathcal A_X = \pi_*\mathbb C_{BN} \in {\mathcal D}(BB)$ where $\pi:BN\to BB$ is the natural $H= B/N$ torsor. Thus we are studying the bimonodromic Hecke category $\tilde \mathcal H_G$ of unipotent bimonodromic ${\mathcal D}$-modules on $N\backslash G/N$.

::: theorem
[]{#thm mon char shvs label="thm mon char shvs"} The category of unipotent character sheaves ${Ch}_{G}$ is equivalent to both the trace and center of the bimonodromic Hecke category $\tilde \mathcal H_{G}$. The equivalences fit into natural adjoint commutative diagrams $$\xymatrix{
&  \tilde\mathcal H_{G} \ar[dl]_-\mathfrak {tr}\ar[d]<-1ex>_-{\tilde F}&\\
 \operatorname{Tr}(\tilde\mathcal H_{G}) \ar[r]^-\sim & \ar[u]<-1ex>_-{\tilde F^r} {Ch}_{G} \ar[r]^-\sim
 &  \ar[ul]_-\mathfrak z\operatorname{Z}(\tilde\mathcal H_G)
   }$$
:::
