---
doc_id: arxiv-math-0005038v1
doc_title: "Braid groups are linear"
section_id: sec-009-32-proof-of-the-key-lemma
section_title: "Proof of the Key Lemma"
section_number: 3.2
pages: 8-9
source_pdf: 0005038v1.pdf
source_sha256: db0b9b7a8534f161
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.791
latex_coverage_ratio: 0.936
doc_brief: "Braid groups are linear — The braid groups Bn can be deﬁned as the mapping class group of the n-punctured disc."
---
Let $N$ be a noodle and let $F$ be a fork. By applying a preliminary isotopy, we can assume that $T(F)$ intersects $N$ transversely at a finite number of points, which we label $z_1,\dots,z_l$. Further, we can assume that $l$ is the minimal possible number of points of intersection. Let $F'$ be a parallel copy of $F$. Choose $F'$ so that and $T(F')$ intersects $N$ transversely at $z'_1,\dots,z'_l$, where $z_i$ and $z'_i$ are joined by a short arc in $N$ which meets no other $z_j$ or $z'_j$.

If $l = 0$ then clearly $\langle N,F \rangle = 0$. We now assume $l > 0$ and show that $\langle N,F \rangle \neq 0$. We use the following lexicographic ordering on the set of monomials $q^a t^b$.

::: defn
We say $q^a t^b \le q^{a'}t^{b'}$ if and only if either

-   $a < a'$, or

-   $a = a'$ and $b \le b'$.

For $i,j \in \{1,\dots,l\}$ we say that $m_{i,j}$ is *maximal* if $m_{i,j} \ge m_{i',j'}$ for all $i',j' \in \{1,\dots,l\}$.
:::

::: clm
[]{#keyclaim label="keyclaim"} If $m_{i,j}$ is maximal then $m_{i,i} = m_{j,j} = m_{i,j}$.
:::

::: proof
*Proof.* Suppose $m_{i,j}$ is maximal. Then $a_{i,j}$ is maximal among all the integers $a_{k,l}$. By Claim [\[a\]](#a){reference-type="ref" reference="a"} it follows that $a_i$ and $a_j$ are maximal among all the integers $a_{k}$. Thus $a_{i,i} = a_{j,j} = a_{i,j}$.

We now show that $b_{i,i} = b_{i,j}$. Suppose not. Then $b_{i,i} < b_{i,j}$. Let $\alpha$ be an embedded arc from $z'_i$ to $z'_j$ along $T(F')$. Let $\beta$ be an embedded arc from $z'_j$ to $z'_i$ along $N$.

If $\beta$ does not pass through the point $z_i$, let $\delta = \alpha \beta$ and let $w$ be the winding number of $\delta$ around $z_i$. Then $b_{i,j} - b_{i,i} = 2w$.

If $\beta$ does pass through $z_i$, first modify $\beta$ in a small neighborhood of $z_i$ so that $z_i$ lies to its left. Next let $\delta = \alpha \beta$ and let $w$ be the winding number of $\delta$ around $z_i$. Then $b_{i,j} - b_{i,i} = 2w-1$.

In either case, $w$ is greater than zero.

Let $D_1 = D \setminus \{z_i\}$. Let $\tilde{D}_1$ be the universal cover of $D_1$. Let $\tilde{\alpha}$ be a lift of $\alpha$ to $\tilde{D}_1$. Let $\tilde{\beta}$ be the lift of $\beta$ to $\tilde{D}_1$ which starts at $\tilde{\alpha}(1)$. Let $\tilde{\gamma}$ be an embedded arc in $\tilde{D}_1$ from $\tilde{\beta}(1)$ to $\tilde{\alpha}(0)$ which intersects $\tilde{\alpha}$ and $\tilde{\beta}$ only at its endpoints. Let $\gamma$ be the projection of $\tilde{\gamma}$ to $D_1$. Choose $\tilde{\gamma}$ so that $\gamma$ does not wind around any puncture points.

Let $\tilde{z}'_k$ be the first point on $\tilde{\alpha}$ which intersects $\tilde{\beta}$ (possibly $\tilde{\alpha}(1)$). This lies in the fiber over $z'_k$ for some $k=1,\dots,l$. Let $\tilde{\alpha}'$ be the initial segment of $\tilde{\alpha}$ ending at $\tilde{z}'_k$. Let $\tilde{\beta}'$ be the final segment of $\tilde{\beta}$ starting at $\tilde{z}'_k$. Let $\tilde{\delta}' = \tilde{\alpha}' \tilde{\beta}' \tilde{\gamma}$.

Now $\tilde{\delta}'$ is a simple closed curve in $\tilde{D}_1$, so by the Jordan curve theorem it must bound a disc $\tilde{B}$. Since $\gamma$ passes clockwise around $z_i$, there is a non-compact region to the right of $\tilde{\delta}'$, so $\tilde{\delta}'$ must pass counterclockwise around $\tilde{B}$.

Let $\delta'$ be the projection of $\tilde{\delta}'$ to $D$. Then $a_k - a_i$ is equal to the sum of the winding numbers of $\delta'$ around each of the points in $P$. This is equal to the number of points in $\tilde{B}$ which are lifts of a point on $P$. This must be greater than zero, since otherwise we could isotope $T(F')$ so as to have fewer points of intersection with $N$. Thus $a_k - a_i$ is greater than zero, contradicting the fact that $a_i$ is maximal among all integers $a_{i'}$. Therefore our assumption that $b_{i,j} > b_{i,i}$ must have been false, so $b_{i,j} = b_{i,i}$.

The proof that $b_{i,j} = b_{j,j}$ is similar. This completes the proof of the claim. ◻
:::

This claim, together with the formula for $\epsilon_{i,j}$ given in Claim [\[sign\]](#sign){reference-type="ref" reference="sign"}, implies that if $m_{i,j}$ is maximal then $\epsilon_{i,j} = -m_{i,j}|(q=1,t=-1)$. Thus all maximal monomials occur with the same sign in equation ([\[pairsum\]](#pairsum){reference-type="ref" reference="pairsum"}). Therefore $\langle N,F \rangle$ cannot equal zero. This completes the proof of the Key Lemma.
