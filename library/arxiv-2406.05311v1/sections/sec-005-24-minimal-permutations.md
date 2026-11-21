---
doc_id: arxiv-2406.05311v1
doc_title: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD"
section_id: sec-005-24-minimal-permutations
section_title: "Minimal permutations"
section_number: 2.4
pages: 5-7
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.976
doc_brief: "A quantum Murnaghan–Nakayama rule for the flag manifold — In this paper, we give a rule for the multiplication of a Schubert class by a tautological class in the (small) quantum cohomology ring of"
---
[]{#minimal-permutations label="minimal-permutations"}

A permutation $\zeta$ is if ${\mathcal L}(\zeta) = \#\mathop{\mathrm{supp}}(\zeta) - s(\zeta)$, where ${\color{RoyalBlue}s(\zeta)}$ is the number of (nontrivial) cycles in the factorization of $\zeta$ into disjoint cycles. Minimality is a central concept in this paper. This terminology (introduced in [@BS-Bruhat]) arises from the inequality ${\mathcal L}(\zeta) \geq \#\mathop{\mathrm{supp}}(\zeta) - s(\zeta)$, so that a minimal permutation has the minimal possible rank given its cycle structure. For example, $\zeta_1 = (2,3,5,7,4)$ is minimal, because $${\mathcal L}(\zeta_1) = \ell(68357421) - \ell(68235741) = 22 - 18 = 4 = \#\mathop{\mathrm{supp}}(\zeta_1) - s(\zeta_1);$$ and $\zeta_2 = (1,7,4)(3,6)$ is not minimal, because $${\mathcal L}(\zeta_2) = \ell(6274135) - \ell(3217465) = 12 - 7 = 5 > 3 = \#\mathop{\mathrm{supp}}(\zeta_2) - s(\zeta_2).$$

Related to minimality is the notion of crossing. Let $l_1<l_2$ and $m_1<m_2$ be two disjoint pairs of numbers, and suppose that $l_1<m_1$. There are three possibilities for $l_2$. Either $l_2<m_1$ or $m_1<l_2<m_2$ or $m_2<l_2$. When the second occurs, we say that the pairs are , otherwise they are . This refers to arcs connecting elements of each pair, when the numbers are marked along a number line. $$\begin{picture}(110,55)(0,-24)
    \put(0,0){\includegraphics{nonnesting.eps}}
    \put(6,-9){$l_1$}  \put(36,-9){$l_2$}  \put(66,-9){$m_1$}  \put(96,-9){$m_2$}
    \put(24,-24){noncrossing}
   \end{picture}
   \qquad
   \begin{picture}(110,55)(0,-24)
    \put(0,0){\includegraphics{crossing.eps}}
    \put(6,-9){$l_1$}  \put(36,-9){$m_1$}  \put(66,-9){$l_2$}  \put(96,-9){$m_2$}
    \put(34,-24){crossing}
   \end{picture}
   \qquad
   \begin{picture}(110,55)(0,-24)
    \put(0,0){\includegraphics{nesting.eps}}
    \put(6,-9){$l_2$}  \put(36,-9){$m_1$}  \put(66,-9){$m_2$}  \put(96,-9){$l_2$}
    \put(24,-24){noncrossing}
   \end{picture}$$ Let $A,B\subset[n]$ be disjoint and suppose that each has at least two elements. If there exist a pair of elements of $A$ and a pair of elements of $B$ that are crossing, then $A$ and $B$ are ; otherwise they are .

A product $\zeta\cdot\eta$ of two permutations is when $\mathop{\mathrm{supp}}(\zeta)$ and $\mathop{\mathrm{supp}}(\eta)$ are disjoint and noncrossing. A permutation $\zeta$ is if it cannot be written nontrivially as a noncrossing product. Any permutation factors uniquely as a noncrossing product of irreducible permutations. In [@BS-Bruhat], $s(\zeta)$ counted the number of irreducible factors in the noncrossing factorization of $\zeta$ for minimal permutations. By [@BS-Bruhat Lem. 3.3.1] we have that $s(\zeta)$ is the number of cycles (this is also explained in the proof below). We give a characterization of minimal permutations in terms of peakless chains in the Grassmannian--Bruhat order.

<figure id="F:product">
<div class="picture">
<p>(26,80)(-11,0) (0,0)<span><embed src="row.eps" /></span> (-12,50)<span><span class="math inline">(176)</span></span> (-10,25)<span><span class="math inline">(16)</span></span> (-1,0)<span><span class="math inline"><em>e</em></span></span></p>
</div>
<div class="picture">
<p>(74,85)(-1,0) (10,0)<span><embed src="hook.eps" /></span> (21,75)<span><span class="math inline">(2354)</span></span> (-0.5,50)<span><span class="math inline">(354)</span></span> (49,50)<span><span class="math inline">(234)</span></span> (27,25)<span><span class="math inline">(34)</span></span> (34.5,0)<span><span class="math inline"><em>e</em></span></span></p>
</div>
<div class="picture">
<p>(275,135)(-13,0) (-1,0)<span><embed src="product.eps" /></span> (11,125)<span><span class="math inline">(176)(2354)</span></span> (-13,100)<span><span class="math inline">(176)(354)</span></span> (47.5,100)<span><span class="math inline">(176)(234)</span></span> (19.5,75)<span><span class="math inline">(176)(34)</span></span> (29,50)<span><span class="math inline">(176)</span></span></p>
<p>(108,100)<span><span class="math inline">(16)(2354)</span></span> (80.5,75)<span><span class="math inline">(16)(354)</span></span> (141,75)<span><span class="math inline">(16)(234)</span></span> (114,50)<span><span class="math inline">(16)(34)</span></span> (124,25)<span><span class="math inline">(16)</span></span></p>
<p>(208,75)<span><span class="math inline">(2354)</span></span> (180,50)<span><span class="math inline">(354)</span></span> (240,50)<span><span class="math inline">(234)</span></span> (212,25)<span><span class="math inline">(34)</span></span> (220,0)<span><span class="math inline"><em>e</em></span></span></p>
</div>
<figcaption>If <span class="math inline"><em>ζ</em> ⋅ <em>η</em></span> is a noncrossing product, then the interval <span class="math inline">[<em>e</em>,<em>ζ</em>⋅<em>η</em>]<sub>≼</sub></span> is isomorphic to the product of the intervals <span class="math inline">[<em>e</em>,<em>ζ</em>]<sub>≼</sub></span> and <span class="math inline">[<em>e</em>,<em>η</em>]<sub>≼</sub></span>, and the chains in <span class="math inline">[<em>e</em>,<em>ζ</em>⋅<em>η</em>]<sub>≼</sub></span> are shuffles of chains in each of the factors.</figcaption>
</figure>

::: lemma
[]{#L:properties-noncrossing-products label="L:properties-noncrossing-products"} Let $\zeta$ be a permutation and $\zeta=\zeta_1\dotsb \zeta_s$ its unique factorization into a noncrossing product of irreducible permutations.

1.  ${\mathcal L}(\zeta)= {\mathcal L}(\zeta_1)+\dotsb+{\mathcal L}(\zeta_s).$

2.  $[e,\zeta]_\preceq\ \simeq\  [e,\zeta_1]_\preceq\ \times\ \dotsb\ \times\  [e,\zeta_s]_\preceq.$

3.  $[e,\zeta]_\preceq$ has a peakless chain if and only if each interval $[e,\zeta_i]_\preceq$ has a peakless chain.

4.  $\zeta$ is a minimal permutation if and only if each $\zeta_i$ is a minimal permutation.

5.  If $\zeta$ is minimal and irreducible, then $\zeta$ is a cycle.
:::

::: proof
*Proof.* (1) By [@BS-Bruhat Lem. 3.3.1], ${\mathcal L}(\zeta)= {\mathcal L}(\zeta_1)+\dotsb+{\mathcal L}(\zeta_s)$ as this is a noncrossing product.

\(2\) [@BS-Bruhat Lem. 3.3.3] implies that $[e,\zeta]_\preceq\ \simeq\  [e,\zeta_1]_\preceq\ \times\ \dotsb\ \times\  [e,\zeta_s]_\preceq$.

\(3\) If each interval $[e, \zeta_i]_{\preceq}$ has a peakless chain $\gamma_i$, then shuffling these chains appropriately gives a peakless chain $\gamma$ in $[e,\zeta]_\preceq$ by (2). Conversely, if $\gamma$ is a peakless chain in $[e,\zeta]_\preceq$, restricting it to each $[e,\zeta_i]_\preceq$ gives a peakless chain $\gamma_i$. Figure [1](#F:product){reference-type="ref" reference="F:product"} illustrates this for the noncrossing product of the two minimal permutations $\zeta=(1,7,6)$ and $\eta=(2,3,5,4)$. The peakless chains are indicated, and commas in cycles are omitted for display purposes.

\(4\) follows from (1) and (2).

\(5\) Suppose that $\zeta$ is minimal and irreducible. If $\zeta$ is not a single cycle, then $\zeta=\eta\cdot \eta'$, where $\eta$ and $\eta'$ have disjoint supports that are crossing. By [@BS-Bruhat Lem. 3.3.1], ${\mathcal L}(\zeta)> {\mathcal L}(\eta) + {\mathcal L}(\eta')$, which contradicts that $\zeta$ is minimal. This inequality is illustrated by $\zeta=(1,7,4)(3,6)$. We showed that ${\mathcal L}(\zeta)=5$, but ${\mathcal L}(1,7,4) = 2$ and ${\mathcal L}(3,6)=1$. ◻
:::

::: proposition
[]{#P:peaklessChains label="P:peaklessChains"} A permutation $\zeta$ is minimal if and only if the interval $[e,\zeta]_\preceq$ has a peakless chain. The number of peakless chains of height $a$ in $[e,\zeta]_\preceq$ is the binomial coefficient $\left(\begin{smallmatrix} s(\zeta)-1 \\ \mathop{\mathrm{ht}}(\zeta)-a \end{smallmatrix}\right)$.
:::

::: proof
*Proof.* We begin by showing that the first statement follows from the corresponding result for irreducible permutations. Let $\zeta=\zeta_1\dotsb \zeta_s$ be the unique factorization of $\zeta$ into a noncrossing product of irreducible permutations. By Lemma [\[L:properties-noncrossing-products\]](#L:properties-noncrossing-products){reference-type="ref" reference="L:properties-noncrossing-products"}, $\zeta$ is minimal if and only if each $\zeta_i$ is minimal. Since $\zeta_i$ is irreducible, $\zeta$ is minimal if and only if each interval $[e, \zeta_i]_{\preceq}$ has a peakless chain. By Lemma [\[L:properties-noncrossing-products\]](#L:properties-noncrossing-products){reference-type="ref" reference="L:properties-noncrossing-products"}, this holds if and only if $[e, \zeta]_{\preceq}$ has a peakless chain.

We now prove the result for irreducible permutations. Suppose that $\zeta$ is minimal and irreducible. By Lemma [\[L:properties-noncrossing-products\]](#L:properties-noncrossing-products){reference-type="ref" reference="L:properties-noncrossing-products"}, $\zeta$ is a single cycle. In [@BS-iso Lem. 6.7] it is proved that if $\zeta$ is a minimal cycle, then there is a unique peakless chain in the interval $[e, \zeta]_\preceq$, which proves the forward direction. Conversely, suppose that $[e, \zeta]_\preceq$ has a peakless chain. Let $a$ be the height of that chain and set ${\color{RoyalBlue}b}\vcentcolon={\mathcal L}(\zeta){-}a{+}1$. Replacing $\zeta$ by a shape-equivalent permutation if necessary, we may assume that $\mathop{\mathrm{supp}}(\zeta)=[n]$ (so that $\zeta\in S_n$) and thus ${\mathcal L}(\zeta) \geq
\#\mathop{\mathrm{supp}}(\zeta) - s(\zeta) = n-1$.

Since $e \preceq \zeta$, there is a $k < n$ and $u \in S_n$ such that $u \leq_k \zeta u$ and $[e, \zeta]_\preceq \simeq [u, \zeta u]_k$. By [@BS-Bruhat Thm. 3.1.5], we have $$\{i \mid i < \zeta(i)\}\ \subseteq\ \{u^{-1}(1), \ldots, u^{-1}(k)\}
    \quad\text{and}\quad
    \{i \mid i > \zeta(i)\}\ \subseteq\ \{u^{-1}(k + 1), \ldots, u^{-1}(n)\}$$ so that $$\mathop{\mathrm{ht}}(\zeta)\ =\ \#\{i \mid i < \zeta(i)\} \leq k
    \quad\text{and}\quad
    n - \mathop{\mathrm{ht}}(\zeta)\ =\ \#\{i \mid i > \zeta(i)\} \leq n - k.$$ Together, these imply that $\mathop{\mathrm{ht}}(\zeta) = k$. Since there is a peakless chain in $[e,\zeta]_\preceq$ and $[e,\zeta]_\preceq\simeq[u,\zeta u]_k$, it follows from Formula [\[eq:schubert-times-hook-via-peakless-chains\]](#eq:schubert-times-hook-via-peakless-chains){reference-type="eqref" reference="eq:schubert-times-hook-via-peakless-chains"} below that the coefficient $c^{\zeta u}_{u, v((b,1^{a-1}),k)}$ is nonzero. This implies that $v((b,1^{a-1}),k)\leq_k \zeta u$. As $\zeta u\in S_n$, we have $v((b,1^{a-1}),k)\in S_n$. Thus $a\leq k<n$ and $b\leq n{-}k$, so that ${\mathcal L}(\zeta)=a{+}b{-}1\leq n{-}1$. This implies that ${\mathcal L}(\zeta)=n{-}1$, $a=k$, and $b=n{-}k$. As $n=\#\mathop{\mathrm{supp}}(\zeta)$, we conclude that $\zeta$ is a minimal cycle and that $[e, \zeta]_\preceq$ has a unique peakless chain. Note that since $s(\zeta) = 1$ and $\mathop{\mathrm{ht}}(\zeta) = a$, we have $\left(\begin{smallmatrix} s(\zeta)-1 \\ \mathop{\mathrm{ht}}(\zeta)-a \end{smallmatrix}\right)
= \left(\begin{smallmatrix} 0 \\ 0 \end{smallmatrix}\right) = 1$.

Finally, suppose that $\zeta=\zeta_1\dotsb\zeta_s$ is the noncrossing factorization of a minimal permutation $\zeta$ into disjoint minimal cycles $\zeta_1,\dotsc,\zeta_s$. Recall from Lemma [\[L:properties-noncrossing-products\]](#L:properties-noncrossing-products){reference-type="ref" reference="L:properties-noncrossing-products"} that $[e,\zeta]_\preceq \simeq  [e,\zeta_1]_\preceq \times \dotsb \times  [e,\zeta_s]_\preceq.$ We count the shuffles of peakless chains $\gamma_i$ in $[e,\zeta_i]_\preceq$ with a given height. We need only consider the sequence of labels, and note that as the cycles $\zeta_i$ have disjoint supports, the set of labels on the chains $\gamma_i$ are disjoint. Partition a peakless chain (represented by its labels)

$$\label{Eq:Peakless_Partition}
    l_1\ >\ \dotsb\ >\ l_{a-1} \ >\  l_a\ <\ l_{a+1}\ <\ \dotsb\ <\ l_{a+b-1}$$

into three subsets. Call $l_1> \dotsb>l_{a-1}$ the decreasing segment, $l_a$ the minimum, and $l_{a+1} <\dotsb<l_{a+b-1}$ the increasing segment.

In a peakless chain [\[Eq:Peakless_Partition\]](#Eq:Peakless_Partition){reference-type="eqref" reference="Eq:Peakless_Partition"} of height $a$ in $[e,\zeta]_\preceq$, its decreasing segment contains the decreasing segments of each $\gamma_i$, and the same for increasing segments. Its minimum $l_a$ is the minimum of all the minima of the $\gamma_i$. The only choices possible are distributing the remaining $s{-}1$ minima between the decreasing and increasing segments of [\[Eq:Peakless_Partition\]](#Eq:Peakless_Partition){reference-type="eqref" reference="Eq:Peakless_Partition"}, which may be done independently. Since $\mathop{\mathrm{ht}}(\zeta)=\mathop{\mathrm{ht}}(\zeta_1)+\dotsb+\mathop{\mathrm{ht}}(\zeta_s)$, we see that placing $\mathop{\mathrm{ht}}(\zeta)-a$ of these remaining minima in the increasing segment gives a peakless chain of height $a$. This completes the proof. ◻
:::
