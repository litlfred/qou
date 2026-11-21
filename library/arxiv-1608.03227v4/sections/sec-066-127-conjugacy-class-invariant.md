---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-066-127-conjugacy-class-invariant
section_title: "Conjugacy class invariant"
section_number: 12.7
pages: 71-72
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.954
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
In section [\[ssec: Cb\]](#ssec: Cb){reference-type="ref" reference="ssec: Cb"} we constructed for every word $\beta=\sigma_{i_1}^{\epsilon_1}\cdot\dots\cdot\sigma_{i_\ell}^{\epsilon_\ell}$ of length $\ell$ of generators of the braid group $\Brgr_n$ complexes $C_{\sigma_{i_1}^{\epsilon_1},\dots,\sigma_{i_\ell}^{\epsilon_\ell}}\in
\MF_{B^\ell\times G}(\calX_{\ell,fc},0)$. The group $\hat{G}$ acts only on the first and last factors in $\calX_{\ell,fc}$ there is a $\hat{G}$-equivariant projection $pr^{i}:\calX_{\ell,fc}\rightarrow \frg^2\times V$: $$pr^i(X,g_1,Y_1,\dots,g_\ell,Y_\ell,u)=(X,\Ad_{g_i}(Y_i),u).$$ The image of the map $pr^1$ restricted to $\calX^{crit}_{\ell,fc}$ consists of stable triples $(X,Y,u)$, $[X,Y]=0,\CC[X,Y]u=V$. Thus we have a well-defined map $pr^1:\St_\ell\to \Hilb_n$.

Since $C_{\sigma_{i_1}^{\epsilon_1},\dots,\sigma_{i_\ell}^{\epsilon_\ell}}\in \MFcrit_{B^\ell\times G}(\calX_{\ell,fc},0)$ we can apply the above constructions to obtain a complex of sheaves on $\Hilb_n$ $$\SymbolPrint{\calS_{\sigma_{i_1}^{\epsilon_1},\dots,\sigma_{i_\ell}^{\epsilon_\ell}}}:=pr^1_{*}(\calH_{B}(C_{\sigma_{i_1}^{\epsilon_1},\dots,\sigma_{i_\ell}^{\epsilon_\ell}}))^{\hat{G}}.$$

::: theorem
[]{#thm: conj inv label="thm: conj inv"} The sheaf $\calS_{\sigma_{i_1}^{\epsilon_1},\dots,\sigma_{i_\ell}^{\epsilon_\ell}}$ depends only on conjugacy class of $\beta=\sigma_{i_1}^{\epsilon_1}\cdot\dots\cdot\sigma_{i_\ell}^{\epsilon_\ell}$: $$\label{eq: 1 in mid}
  \calS_{\sigma_{i_1}^{\epsilon_1},\dots,1,\dots,\sigma_{i_\ell}^{\epsilon_\ell}}
  \sim\calS_{\sigma_{i_1}^{\epsilon_1},\dots,\sigma_{i_\ell}^{\epsilon_\ell}}$$ $$\label{eq: conj invce}
  \calS_{\sigma_{i_1}^{\epsilon_1},\dots,\sigma_{i_\ell}^{\epsilon_\ell}}=\calS_{\sigma_{i_2}^{\epsilon_2},
    \dots,\sigma_{i_\ell}^{\epsilon_\ell},\sigma_{i_1}^{\epsilon_1}}$$ $$\calS_{\sigma_k, \sigma_k^{-1},\sigma_{i_1}^{\epsilon_1}\dots}\sim\calS_{\sigma_{i_1}^{\epsilon_1},\dots},\quad \calS_{\sigma_k, \sigma_{k+1}, \sigma_k,\dots}=\calS_{\sigma_{k+1},\sigma_k,\sigma_{k+1},\dots}$$ where $\sim$ stands for the homotopy equivalence.
:::

::: proof
*Proof.* The conjugacy invariance ([\[eq: conj invce\]](#eq: conj invce){reference-type="ref" reference="eq: conj invce"}) follows almost immediately from the construction. Indeed, the definition of $pr^i$ implies that $$\calS_{\sigma_{i_2}^{\epsilon_2},
  \dots,\sigma_{i_\ell}^{\epsilon_\ell},\sigma_{i_1}^{\epsilon_1}}=pr^2_*(\calH_{B}(C_{\sigma_{i_1}^{\epsilon_1},\dots,\sigma_{i_\ell}^{\epsilon_\ell}})).$$ On the other hand $pr^1|_{\calX_{\ell,fc}^{crit}}=pr^2|_{\calX^{crit}_{\ell,fc}}$ and hence the equality.

To prove the rest of the theorem we introduce slightly more general definition: $$\calS_{\beta_1,\dots,\beta_m}:=pr^1_*(\mathcal{H}_B(\calX_{m,fc},\forg^*(\cl^*(\pi_{12}^*(\calC_{\beta_1})\otimes
    \dots\otimes  \pi_{m,m+1}^*(\calC_{\beta_m})))))^{\hat{G}}$$

Now let us observe that $pr^1=pr^1\circ \hat{\pi}_2$ where $\hat{\pi}_2:\calX_{m,fc}\rightarrow\calX_{m-1,fc}$ is the projection along the second factor. Hence we have $$\calS_{\beta_1,\beta_2,\dots,\beta_m}=\calS_{\beta_1\cdot\beta_2,\dots,\beta_m}$$ It implies the desired equations. ◻
:::

For an element $\beta\in \Brgr_n$ we denote by $[\beta]$ its conjugacy class. Thus for any element of the braid group $\beta\in \Brgr_n$ we have a quasi-coherent sheaf $\calS_{[\beta]}$ on $\Hilb_n$.

It is not obvious to us how one could attach sheaf on the flag Hilbert scheme to a conjugacy class in the braid group. There are well-defined maps $pr_i:\St_\ell\rightarrow \Hilb_{1,n}^L$ that send $(X,g_1,Y_1,\dots,g_\ell,Y_\ell,u)$ to $(\Ad_{g_i}^{-1}(X),Y_i),g^{-1}(u))$. Naively one could hope that the push-forwards $pr_{i*}(\calH^*_B(\calX_{2,fc},C_{\sigma_{i_1}^{\epsilon_1},\dots,\sigma_{i_\ell}^{\epsilon_\ell}}))$ for some $i$ is a such sheaf but it is unclear why it would satisfy the properties from the theorem. However, as we will see later, the push-forwards on the flag Hilbert schemes are useful for understanding Markov moves, since there are natural maps between the flag Hilbert schemes of different ranks. It is also clear from the argument of the previous theorem that for any $\beta=\sigma_{i_1}^{\epsilon_1}\cdot\dots\cdot\sigma_{i_\ell}^{\epsilon_\ell}$ there is a well-defined complex: $$\SymbolPrint{\mathcal{S}_\beta}:=pr_{1,*}(\calH^*_B(\calX_{2,fc},C_{\sigma_{i_1}^{\epsilon_1},\dots,\sigma_{i_\ell}^{\epsilon_\ell}}))\in D^{per}_{T_{sc}}(\Hilb_{1,n}^L).$$
