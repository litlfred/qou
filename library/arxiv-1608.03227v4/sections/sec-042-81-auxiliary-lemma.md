---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-042-81-auxiliary-lemma
section_title: "Auxiliary Lemma"
section_number: 8.1
pages: 42-45
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.971
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
In the proof of the braid relations and Markov moves we will use some generalization of the previous corollary which we explain below. The statement that we prove in this section allows us to use smaller intermediate space for computation of the convolution.

Let us introduce notation $\SymbolPrint{Q_{k\dots m}}\subset G_n$ for subgroup with Lie algebra $\SymbolPrint{\frq_{k\dots m}}$ spanned by $E_{ij}$, $i\le j$, $i,j\in [1,n]$ and by $E_{ij}$, $i>j$, $i,j\in [k,m]$. Respectively, we denote by $\SymbolPrint{\Pi_+^{\overline{k\dots m}}}$ the projection map $\Lie(G_n)\to \frq_{k\dots m}$ and $\SymbolPrint{\Pi_{--}^{\overline{k\dots m}}}$ is defined by $\mathrm{Id}=\Pi_+^{\overline{k\dots m}}+\Pi_{--}^{\overline{k\dots m}}$. Similarly we define $\SymbolPrint{\Pi_{++}^{\overline{k\dots m}}}(X)=\Pi_{--}^{\overline{k\dots m}}(X^t)^t$, where $t$ stands for transpose. Let us also denote by $\SymbolPrint{\Pi^{\overline{k\dots m}}}$ the projection $\frg_n\to \frg_{m-k+1}$ that extracts the block of the matrix elements with entries $ij$, $i,j\in [k,m]$. We use the same notation for the maps of the corresponding groups.

Let us introduce the space $\SymbolPrint{\calX^\circ_3(G_n,G_{k\dots m})}=\frg_n\times G_n\times G_{k-m+1}\times \frn_n\times \frn_{k-m+1}\times \frn_n$. Let us also fix an embedding $\SymbolPrint{i_{k\dots m}}$ of this space inside $\calX_3$:

$$i_{k\dots m}(X,g_{12},g_{23},\vec{Y})=(X,g_{12},i_{k\dots m}(g_{23}),Y_1,i_{k\dots m}(Y_2)+\Pi_{++}^{\overline{k\dots m}}(\Ad_{g_{23}}(Y_3)),Y_3),$$ where $\vec{Y}=(Y_1,Y_2,Y_3)$, $i_{k\dots m}:G_{k-m+1}\to G_n$ and $i_{k\dots m}: \frn_{k-m+1}\to \frn_n$ are the natural embeddings.

Respectively we define maps $$\pi_{12}^{\circ}:\calX^\circ_3(G_n,G_{k\dots m})\to \calX_2(G_{n}),$$ $$\pi_{23}^{\circ}:\calX^\circ_3(G_n,G_{k\dots m})\to \calX_2(G_{m-k+1}),$$ $$\pi_{13}^{\circ}:\calX^\circ_3(G_n,G_{k\dots m})\to \calX_2(G_n),$$ $$\label{eq: pi12}
\pi_{12}^{\circ}(X,g_{12},g_{23},Y_1,Y_2,Y_3)=(X,g_{12},Y_1,i_{k\dots m}(Y_2)+\Pi_{++}^{\overline{k\dots m}}(\Ad_{g_{23}}(Y_3)).$$ $$\label{eq: pi23}
\pi_{23}^{\circ}(X,g_{12},g_{23},Y_1,Y_2,Y_3)=(\Pi^{\overline{k\dots m}}( \Ad_{g_{12}}^{-1}(X)),g_{23},Y_2,\Pi^{\overline{k\dots m}}(Y_3)),$$ $$\pi_{13}^{\circ}(X,g_{12},g_{23},Y_1,Y_2,Y_3)=(X,g_{12}g_{23},Y_1,Y_3).$$ These maps are the restrictions of the corresponding maps from $\calX_3$ on the embedded subvariety $\calX^\circ_3(G_n,G_{k\dots m})$.

Similarly, we define $\calX^\circ_3(G_{k\dots m},G_n)=\frg_n\times G_{k\dots m}\times G_n\times \frn_n\times \frn_{k-m+1}\times \frn_n$. Let us also fix an embedding $i_{k\dots m}$ of this space inside $\calX_3$: $$i_{k\dots m}(X,g_{12},g_{23},\vec{Y})=(X,i_{k\dots m}(g_{12}),g_{23},Y_1,i_{k\dots m}(Y_2)+\Pi_{++}^{\overline{k\dots m}}(\Ad^{-1}_{g_{12}}(Y_1)),Y_3),$$ $\vec{Y}=(Y_1,Y_2,Y_3)$. The maps $\pi_{ij}^{\circ}$ are defined analogously to the previous case: by the restriction from ambient space.

The spaces $\calX^\circ_3(G_n,G_{k\dots m})$ and $\SymbolPrint{\calX^\circ_3(G_{k\dots m},G_n)}$ have unique $B_n^3$ equivariant structure that makes the maps $\pi_{ij}^\circ$ $B_n^3$-equivariant.

::: lemma
[]{#prop: small flag label="prop: small flag"} For any $$\calF\in \MF_{B_{m-k+1}^2}(\calX_2(G_{m-k+1}),W),\calG\in \MF_{B_n^2}(\calX_2(G_n),W)$$ we have $$\calG\star\Ind_{k\dots m}(\calF)=\CE_{\frn_{m-k+1}^{(2)}}\pi_{13*}^\circ(\pi_{12}^{\circ*}(\calG)\otimes \pi_{23}^{\circ*}(\calF))^{T^{(2)}_{m-k+1}},$$ $$\Ind_{k\dots m}(\calF)\star \calG=\CE_{\frn_{m-k+1}^{(2)}}\pi_{13*}^\circ(\pi_{12}^{\circ*}(\calF)\otimes \pi_{23}^{\circ*}(\calG))^{T^{(2)}_{m-k+1}},$$
:::

The key observation in the proof is an alternative description of the induction functor $\Ind_{k\dots m}$. The space $\SymbolPrint{\calX^\bullet_2(Q_{k\dots m})}:=
\frg_n\times Q_{k\dots m}\times \frn_{m-k+1}\times \frn_n$ can be mapped into $\calX_2(G_n)$ with the map: $$\SymbolPrint{j_{k\dots m}}(X,g,Y_1,Y_2)=(X,j_{k\dots m}(g),i_{k\dots m}(Y_1)+\Pi_{++}^{\overline{k\dots m}}(\Ad_g(Y_2)),Y_2)$$ where $j_{k\dots m}: Q_{k\dots m}\to G_n$ is the natural embedding.

There is also a natural projection map $\Pi^{\overline{k\dots m}}:\calX^\bullet_2(Q_{k\dots m})\to \calX_2^\circ(G_{m-k+1})$ defined by: $$\Pi^{\overline{k\dots m}}(X,g,Y_1,Y_2)=(\Pi^{\overline{k\dots m}}(X),\Pi^{\overline{k\dots m}}(g),\Pi^{\overline{k\dots m}}(Y_1),\Pi^{\overline{k\dots m}}(Y_2)).$$ Both of these maps are $B_n^3$-equivariant. In particular, we have a commuting diagram: $$\begin{tikzcd}
 \calX_2^{\bullet}(Q_{k\dots m}) \arrow[dotted]{r}{i'}\arrow[dotted]{d}{\Pi'_1\times\Pi^{\overline{k\dots m}}\times\Pi'_3}   & \calX^\circ_2(P_{k,m})\arrow{d}{p_{k,m}}\arrow{r}{i_{k,m}}&\calX''_{2,n}\\
 \calX'_{2,k}\times \calX''_{2,m-k+1}\times \calX'_{2,n-m} \arrow{r}{i^{\parallel}\times 1\times i^{\parallel}}\arrow{d}{\pi_2} &
 \calX''_{2,k}\times\calX''_{2,m-k+1}\times \calX''_{2,n-m}&\\
\calX^\circ_2(G_{m-k+1})&&
\end{tikzcd}$$ where $\calX'_{2,k}:=\frg_k\times B_k\times \frb_k\times \frb_k=\calX^{\circ}_2(B_k)$, $\calX''_{2,k}:=\frg_k\times G_k\times \frb_k\times\frb_k=\calX^{\circ}_2(G_k)$ and the dotted arrow maps are: $$i'(X,g,Y_1,Y_2)=(\Pi^{\overline{k\dots m}}_+(X),j_{k\dots m}(g),i_{k\dots m}(Y_1)+
  \Pi^{\overline{k\dots m}}_{++}(\Ad_g(Y_2)),Y_2),$$ $$\Pi'_i(X,g,Y_1,Y_2)=(p_{k,m}^{(i)}(X),p_{k,m}^{(i)}(g),p_{k,m}^{(i))}(\Ad_g(Y_2)),p_{k,m}^{(i)}(Y_2)),$$ here $p_{k,m}^{(1)}$, $p_{k,m}^{(3)}$ are the compositions of $p_{k,m}$ with the projections on $k\times k$ and $(n-m)\times(n-m)$ blocks.

Using the base change in our previous diagram we obtain $$\begin{gathered}
\Ind_{k\dots m}=i_{k,m,*}\circ p_{k,m}^*\circ (i^{\parallel}\times 1\times i^{\parallel})\circ \pi_2^*=i_{k,m,*}\circ i'_*\circ (\Pi'_1\times\Pi^{\overline{k\dots m}}\times\Pi'_3)^*\circ\pi_2^*\\=
j_{k\dots m,*}\circ \Pi^{\overline{k\dots m},*}.
\end{gathered}$$

::: proof
*Proof of proposition [\[prop: small flag\]](#prop: small flag){reference-type="ref" reference="prop: small flag"}.* We prove the first formula the second is analogous. We have the following commuting diagram of the maps: $$\begin{tikzcd}
 \calX_3^{\circ}(G_n,Q_{k\dots m}) \arrow[dotted]{r}{i_{k\dots m}}\arrow[dotted]{d}{\pi_{12}^\circ\times\pi_{23}^\circ}   & \calX^\circ_3\arrow{d}{\pi_{12}^\circ\times\pi_{23}^\circ}\arrow{r}{\pi_{13}^{\circ}}&\calX^\circ_2\\
\calX_2^\circ\times \calX_2^\bullet(Q_{k\dots m}) \arrow{r}{1\times j_{k\dots m}}\arrow{d}{1\times\Pi^{\overline{k\dots m}}} &                                  \calX^\circ_2\times\calX^\circ_2&\\
\calX^\circ_2(G_n)\times\calX^\circ_2(G_{m-k+1})&&
 \end{tikzcd}$$ where the dotted arrow map $\pi_{12}^\circ\times\pi_{23}^\circ$ is given by $$\pi_{12}^{\circ}(X,g_{12},g_{23},Y_1,Y_2,Y_3)=(X,g_{12},Y_1,i_{k\dots m}(Y_2)+\Pi_{++}^{\overline{k\dots m}}(\Ad_{g_{23}}(Y_3)),$$ $$\pi_{23}^{\circ}(X,g_{12},g_{23},Y_1,Y_2,Y_3)=(\Ad_{g_{12}}^{-1}(X),g_{23},Y_2,\Pi_{-}^{\overline{k\dots m}}(Y_3)).$$

Now we can use the base change formula to simplify $\calG\star\Ind_{k\dots m}(\calF)$ : $$\begin{gathered}
\CE_{\frn_n^{(2)}}(\pi^\circ_{13*}\circ (\pi^\circ_{12}\times \pi_{23}^\circ)^*\circ (\mathrm{Id}\times j_{k\dots m})_*\circ (\mathrm{Id}\times\Pi^{\overline{k\dots m}})^*(\calG\boxtimes \calF)))^{T^{(2)}_n}=\\
 \CE_{\frn_n^{(2)}}(\pi^\circ_{13*} \circ  (i_{k\dots m})_*\circ  (\pi^\circ_{12}\times \pi_{23}^\circ)^* \circ(\mathrm{Id}\times\Pi^{\overline{k\dots m}})^*(\calG\boxtimes \calF)))^{T^{(2)}_n}=\\
  \CE_{\frn_n^{(2)}}(\pi^\circ_{13*}\circ (\pi^\circ_{12}\times \pi_{23}^\circ)^*(\calG\boxtimes \calF)))^{T^{(2)}_n},
\end{gathered}$$ where in the last equation we use $\pi^\circ_{13}\circ i_{k\dots m}=\pi_{13}^\circ$ and $\mathrm{Id}\times\Pi^{\overline{k\dots m}}\circ \pi^\circ_{12}\times \pi_{23}^\circ=\pi^\circ_{12}\times \pi_{23}^\circ$ where the maps in the product $\pi^\circ_{12}\times \pi_{23}^\circ: \calX_3^\circ(G_n,Q_{k\dots m})\to \calX^\circ_2(G_n)\times\calX^\circ_2(G_{m-k+1})$ are given by the formulas ([\[eq: pi12\]](#eq: pi12){reference-type="ref" reference="eq: pi12"}), ([\[eq: pi23\]](#eq: pi23){reference-type="ref" reference="eq: pi23"}).

Let us denote by $C$ the matrix factorization $\pi^\circ_{13*}\circ (\pi^\circ_{12}\times \pi_{23}^\circ)^*(\calG\boxtimes \calF)$ For last step we use Hochschild-Serre spectral sequence to compute functor $\CE_{\frn_n^{(2)}}$: $$\CE_{\frn_{m-k+1}^{(2)}}(\CE_{\Lie(J'_{k\dots m})}(C))\Rightarrow \CE_{\frn_n^{(2)}}(C)$$ where $J_{k\dots m}$ is the kernel of the projection homomorphism $Q_{k\dots m}\to G_{m-k+1}$ and $J'_{k\dots m}$ is its unipotent part. Let us abbreviate the quotient $J_{k\dots m}/J'_{k\dots m}$ by $J/J'$. We have $$\label{eq: CE}
 \CE_{\Lie(J'_{k\dots m})}(C)^{J/J'}=\pi^\circ_{13*}(\CE_{\Lie(J'_{k\dots m})}(\pi^\circ_{12}\times \pi_{23}^\circ)^*(\calG\boxtimes \calF)).$$ On the other hand the formulas for the maps $\pi^\circ_{12}$ and $\pi^\circ_{23}$ imply that the differentials of the pull back $(\pi^\circ_{12}\times \pi_{23}^\circ)^*(\calG\boxtimes \calF)$ are invariant with respect to the action of $J'_{k\dots m}$. Hence to complete the computation of ([\[eq: CE\]](#eq: CE){reference-type="ref" reference="eq: CE"}) we need to compute $$\mathrm{H}_{\Lie}^*(J'_{k\dots m},\CC[\calX^\circ_3(G_n,Q_{k\dots m})])^{J/J'}$$ which is a tensor product of $\CC[\frb\times G_n\times \frn_{m-k+1}\times \frn_n]$ and $\mathrm{H}_{\Lie}^*(J'_{k\dots m},\CC[Q_{k\dots m}])^{J/J'},$ and in proposition below we show that $\CE_{J'_{k\dots m}}(\CC[Q_{k\dots m}])^{J'/J}=\CC[G_{m-k+1}].$ Hence the statement follows since $T^{(2)}_n=(J/J')\times T_{m-k+1}$ where $T_{m-k+1}$ is the maximal torus of $G_{m-k+1}\subset G_n$. ◻
:::

::: proposition
[]{#prop: Lie cohs label="prop: Lie cohs"} For any $k,m$, $1\le k<m\le n$ we have $$\CE_{\Lie(J'_{k\dots m})}(\CC[Q_{k\dots m}])=\CC[G_{m-k+1}]\otimes \CC[J/J'].$$
:::

::: proof
*Proof.* We show slightly more general statement $$\CE_{\Lie(J'_{k\dots m})}(\CC[Q_{k'\dots m'}])=
\CC[Q_{k-k'+1\dots m-k'+1}\subset G_{m-k+1}]\otimes \CC[(J/J')],$$ where $k\ge k'$, $m'\le m$.

We use induction by $m-k$ and the Hochschild-Serre Spectral sequence ([@Wei], sect 7.5). Since we have short exact sequence of groups $$1\to J'_{k+1,\dots, m}\longrightarrow J'_{k\dots n}\longrightarrow \CC^{m-k+1}\to 1,$$ the spectra sequence tells us that $$\CE_{\CC^{m-k+1}}(\CE_{\Lie\left(J'_{k+1\dots m}\right)}(\CC[Q_{ \kappa '\dots m'}]))\Rightarrow \CE_{J_{k\dots m}}(\CC[Q_{k'\dots m'}]).$$ By induction we have $\CE_{\Lie(J'_{k+1\dots m})}(\CC[Q_{k'\dots m'}])=\CC[Q_{k-k'+2\dots m-k'+1}\subset G_{m-k+2}]$. After relabeling matrix indices our statement is equivalent to the computation of the following cohomology $\mathrm{H}^*_{\Lie}(\CC^{m-k+1},\CC[Q_{k-k'+2\dots m-k'+1}])$. The ring of polynomial functions on $Q_{k-k'+2\dots m-k'+1}$ is generated by the elements $E_{kl}^\vee$ dual to the matrix units $E_{kl}$ of $E$. The generators $\partial_i$ of the commutative algebra $\CC^{m-k+1}$ act on the ring generators by the formula: $$\partial_i E^\vee_{kl}=\delta_{k1} E_{il}^\vee.$$ We can apply invertible linear transformation to our system of differential operators to obtain new system of generators: $$\tilde{\partial}_k=\sum_{i=2}^{m-k+2} (-1)^{i+k}\Delta_{ik}\partial_k,$$ where $\Delta_{ik}\in \CC[Q_{k-k'+2\dots m-k'+1}]$ is the determinant of $(m-k)\times (m-k)$ obtained from $E$ by removing columns and rows containing $11$ and $ik$ entries. Then we have: $$\tilde{\partial}_i E^\vee_{kl}=\delta_{k1}\delta_{il} E_{11}^\vee.$$ and by Poincare lemma we obtain $$\mathrm{H}^*_{\Lie}(\CC^{m-k+1},\CC[Q_{k-k'+2\dots m-k'+1}])=\CC[Q_{k-k'+2\dots m-k'+1}]/(E_{12}^\vee,\dots,E_{1,m-k+2}^\vee)$$ and the statement follows. ◻
:::
