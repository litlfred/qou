---
doc_id: arxiv-0810.1064v1
doc_title: "Multiple polylogarithm values at roots of unity"
section_id: sec-003-level-p-and-p2-cases-p5-a-prime
section_title: "Level p and p2 cases (p5 a prime)"
section_number: null
pages: 4-9
source_pdf: 0810.1064v1.pdf
source_sha256: b2d7514c5382ceaa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.786
doc_brief: "Multiple polylogarithm values at roots of unity — For any positive integer N let µN be the group of the Nth roots of unity."
---
[]{#sec:pp label="sec:pp"} Let $p\ge 5$ be prime throughout this section. From Prop. [\[prop:DG\]](#prop:DG){reference-type="ref" reference="prop:DG"} we see that $d(2,p)\le (p+1)^2/4$. We will improve this bound in Theorem [\[thm:p\]](#thm:p){reference-type="ref" reference="thm:p"}.

Recall that $\calG=\iota(\mathop{\mathrm{{Lie}}}U_\om)$. By [@DG 6.13] one may safely replace $\calG_N^{(\ell)}$ by $\calG$ throughout [@G1]. In particular, Goncharov's results can now be used to study the structure of Galois Lie algebra $\calG_{\bullet,\bullet}(\mmu_N)=\sum_{w\ge 1,l\ge 1}\calG_{-w,-l}(\mmu_N)$ graded by the weight $w$ and depth $l$. The weight filtration is defined via the action of $\G_m$ and the depth filtration comes from the descending central series of $\ker f_*$, where $f_*:\pi_1(\G_m-\mmu_N,x) \lra \pi_1(\G_m)$ for any base point $x$ is induced from the embedding $\G_m-\mmu_N\hookrightarrow\G_m$.

::: thm
[]{#thm:p label="thm:p"} Let $p\ge 5$ be a prime. Then $$\label{equ:pbdd}
 d(2,p)\le \frac{(5p+7)(p+1)}{24}.$$ If Grothendieck's period conjecture (see [@DG 5.27(c)]) is true then the equality holds and all the $\Q$-linear relations in $\MPV(2,p)$ follow from the standard relations.
:::

::: proof
*Proof.* Let $\{\ ,\ \}$ be the Lie bracket in $\calG_{\bullet,\bullet}(\mmu_N)$. Now in depth 1 one has $\dim \calG_{-2,-1}(\mmu_p)=(p-1)/2$ (see [@G1 Theorem 2.1]). By [@G1 Cor. 2.16] $$\label{equ:diag2}
 \dim \calG_{-2,-2}(\mmu_p)=\frac{(p-1)(p-5)}{12}.$$ For any positive integer $N$ define $$\label{equ:beta}
 \beta_N:\bigwedge^2\calG_{-2,-1}(\mmu_N)  \lra \calG_{-2}(\mmu_N), \quad
  a\wedge b  \lms\{a,b\}.$$ Then $$\label{equ:kerbeta}
 \dim(\ker\beta_p)=\frac12\frac{p-1}{2}\left(\frac{p-1}2-1\right)-\frac{(p-1)(p-5)}{12}
=\frac{p^2-1}{24}.$$

Let $SR$ be the affine subgroup of $\Pi$ defined by only those polynomial equations satisfied by the coefficients of $\mathop{\mathrm{{dch}}}(\gs)$ which are deduced from the standard relations, plus "$2\pi i=0$", as explained in [@DG 5.22]. This is the group $\mathsf{DMRD}_0$ studied by Racinet in [@Rac §3.2, Thm. I]. Its Lie algebra $\mathop{\mathrm{{Lie}}}SR$ is graded by weight and depth, independent of the embedding by Prop. 4.1 of op. cit. and contains $\calG$ by [@DG 5.22]. Further, Goncharov shows [@G1 §7.7] that the standard relations provide a complete list of constraints on the diagonal part of the Lie algebra $\calG$ in depth $\le 2$, yielding $(\mathop{\mathrm{{Lie}}}SR)_{m,m}=\calG_{m,m}$ for $m=-1,-2$. Together with [\[equ:kerbeta\]](#equ:kerbeta){reference-type="eqref" reference="equ:kerbeta"} this means in the proof of [@DG 5.25] one can decrease the bound $D(2,p)$ by $(p^2-1)/24$ and arrive at the bound $(5p+7)(p+1)/24$.

Grothendieck's conjecture implies that $\calG=\mathop{\mathrm{{Lie}}}R$ where $R$ is the affine subgroup of $\Pi$ defined by all the polynomial equations satisfied by the coefficients of $\mathop{\mathrm{{dch}}}(\gs)$ plus "$2\pi i=0$". Therefore one obtains both the equality in [\[equ:pbdd\]](#equ:pbdd){reference-type="eqref" reference="equ:pbdd"} and the statement about the completeness of the standard relations. This concludes the proof of the theorem. ◻
:::

::: rem
\(a\) Notice that when $p\ge 11$ the vector space $\ker\beta_p$ contains a subspace isomorphic to the space of cusp forms of weight two on $X_1(p)$ which has dimension $(p-5)(p-7)/24$ (see [@G1 Lemma 2.3 & Theorem 7.8]). So it must contain another piece which has dimension $(p-3)/2$ by [\[equ:kerbeta\]](#equ:kerbeta){reference-type="eqref" reference="equ:kerbeta"}. What is this missing piece?

\(b\) When $w>2$ it's not too hard to improve the bound of $d(w,p)$ given in [@DG 5.24] by the same idea as used in the proof of the theorem (for example, decrease the bound by $(p^2-1)/24$). But they are often not the best.
:::

Turn now to the case of level $N=p^2$. Notice that $\varphi(p^2)(\varphi(p^2)-2)/4$ is a trivial upper bound of $\dim \calG_{-2,-2}(\mmu_{p^2})$ (see [@G1 Theorem 2.1]). If one had any nontrivial upper bound of $\dim \calG_{-2,-2}(\mmu_{p^2})$ one would have a nontrivial lower bound of $\dim(\ker \beta_{p^2})$ where $\beta_{p^2}$ is defined by [\[equ:beta\]](#equ:beta){reference-type="eqref" reference="equ:beta"}. This would in turn provide an improved upper bound of $d(2,p^2)$ similar to Theorem [\[thm:p\]](#thm:p){reference-type="ref" reference="thm:p"}. However, at present we can only show that

::: thm
If $p\ge 5$ is a prime then $\ker \beta_{p^2}\ne 0$ and $d(2,p^2)<p^2(p-1)^2/4.$
:::

::: proof
*Proof.* Fix a primitive $p^2$th root of unity $\mu$. Put $e(a)=e_{\mu^a}$ for all integer $a$. Define $$g_{k,j}=e(pk+j)+e(p^2-pk-j)+e(pj)+e(p^2-pj)$$ for $0\le k<(p-1)/2$, $1\le j\le p-1$, and for $k=(p-1)/2$, $1\le j\le (p-1)/2$. One only needs to prove the following

**Claim.** Let $h=(p-3)/2.$ Then one has $$\begin{aligned}
 \ &\sum_{k=0}^{h} \sum_{l=k}^{h}\sum_{j=2}^{p-2} \{g_{k,1},g_{l,j}\}
+\sum_{k=0}^{h+1} \sum_{j=2}^{h+1} \{g_{k,1},g_{h+1,j}\}
+\sum_{k=0}^{h} \sum_{l=k+1}^{h}\sum_{j=2}^{p-2} \{g_{k,p-1},g_{l,j}\}\\
+&\sum_{k=0}^{h} \sum_{j=2}^{h+1} \{g_{k,p-1},g_{h+1,j}\}
 -\sum_{k=0}^{h} \sum_{l=k}^{h}\sum_{j=2}^{p-2} \{g_{k,j},g_{l,p-1}\}
 -\sum_{k=0}^{h} \sum_{l=k}^{h}\sum_{j=2}^{p-2} \{g_{k,j},g_{l+1,1}\}
 =0.
\end{aligned}$$ There are $h(2h+3)^2=hp^2$ distinct terms on the left, each with coefficient $\pm 1$.

The proof of the claim is straight-forward by a little tedious change of indices and regrouping. $$-\sum_{k=0}^{h} \sum_{l=k}^{h}\sum_{j=2}^{p-2} \{g_{k,j},g_{l+1,1}\}
=\sum_{k=0}^{h} \sum_{l=0}^{k}\sum_{j=2}^{p-2} \{g_{k+1,1},g_{l,j}\}
=\sum_{k=1}^{h+1} \sum_{l=0}^{k-1}\sum_{j=2}^{p-2} \{g_{k,1},g_{l,j}\}.$$ Then the expression in the claim becomes $$\begin{aligned}
\ & \sum_{k=1}^{h} \sum_{l=0}^{h}\sum_{j=2}^{p-2} \{g_{k,1},g_{l,j}\}
+\sum_{l=0}^{h}\sum_{j=2}^{p-2} \{g_{0,1},g_{l,j}\}
 +\sum_{l=0}^{h}\sum_{j=2}^{p-2} \{g_{h+1,1},g_{l,j}\}
+\sum_{k=0}^{h+1} \sum_{j=2}^{h+1} \{g_{k,1},g_{h+1,j}\} \\
+&\sum_{k=0}^{h} \sum_{l=0}^{h}\sum_{j=2}^{p-2} \{g_{k,p-1},g_{l,j}\}
+\sum_{k=0}^{h} \sum_{j=2}^{h+1} \{g_{k,p-1},g_{h+1,j}\} \\
=\ & \sum_{k=0}^{h+1} \sum_{l=0}^{h}\sum_{j=2}^{p-2} \{g_{k,1},g_{l,j}\}
+\sum_{k=0}^{h+1} \sum_{j=2}^{h+1} \{g_{k,1},g_{h+1,j}\} \\
+&\sum_{k=0}^{h} \sum_{l=0}^{h}\sum_{j=2}^{p-2} \{g_{k,p-1},g_{l,j}\}
+\sum_{k=0}^{h} \sum_{j=2}^{h+1} \{g_{k,p-1},g_{h+1,j}\}
\end{aligned}$$ Let me use $\{a,b\}=\{e(a),e(b)\}$. By definition $$\begin{aligned}
 \{g_{k,1},g_{l,j}\}=&\{pk+1,pl+j\}
+\{-pk-1,pl+j\}+\{p,pl+j\}+\{-p,pl+j\} \\
+&\{pk+1,-pl-j\}
+\{-pk-1,-pl-j\}+\{p,-pl-j\}+\{-p,-pl-j\} \\
+&\{pk+1,pj\}
+\{-pk-1,pj\}+\{p,pj\}+\{-p,pj\} \\
+&\{pk+1,-pj\}
+\{-pk-1,-pj\}+\{p,-pj\}+\{-p,-pj\}\\
=&\{pk+1,pl+j\}
+\{p(p-k)-1,pl+j\}+\{p,pl+j\}+\{-p,pl+j\} \\
+&\{pk+1,p(p-1-l)+p-j\}
+\{p(p-k)-1,p(p-1-l)+p-j\} \\
\ &\hskip3cm  +\{p,p(p-1-l)+p-j\}+\{-p,p(p-1-l)+p-j\} \\
+&\{pk+1,pj\}
+\{p(p-k)-1,pj\}+\{p,pj\}+\{-p,pj\} \\
+&\{pk+1,p(p-j)\}
+\{p(p-k)-1,p(p-j)\}+\{p,p(p-j)\}+\{-p,p(p-j)\}
\end{aligned}$$ Then $$\begin{aligned}
\ & \sum_{k=0}^{h+1}  \sum_{l=0}^{h}\sum_{j=2}^{p-2} \{g_{k,1},g_{l,j}\}
=\sum_{k=0}^{h+1} \sum_{l=0}^{h}\sum_{j=2}^{p-2}
\{pk+1,pl+j\}
+\{p(p-k)-1,pl+j\}\\
+&\{pk+1,p(p-1-l)+j\}+\{p(p-k)-1,p(p-1-l)+j\} \\
\ +&\{p,pl+j\}+\{-p,pl+j\} +\{p,p(p-1-l)+j\}+\{-p,p(p-1-l)+j\} \\
+&2\{pk+1,pj\}+2\{p(p-k)-1,pj\}+2\{p,pj\}+2\{-p,pj\} \\
=&\sum_{k=0}^{h+1} \sum_{l=0,l\ne h+1}^{p-1}\sum_{j=2}^{p-2} \{pk+1,pl+j\}
+\sum_{k=h+2}^{p} \sum_{l=0,l\ne h+1}^{p-1}\sum_{j=2}^{p-2} \{pk-1,pl+j\}\\
\ +&\sum_{k=0}^{h+1} \sum_{l=0,l\ne h+1}^{p-1}\sum_{j=2}^{p-2} \Big(\{p,pl+j\}+\{-p,pl+j\}\Big)
+2(h+1)\sum_{k=0}^{h+1}\sum_{j=2}^{p-2} \{pk+1,pj\}\\
+&2(h+1)\sum_{k=h+2}^{p} \sum_{j=2}^{p-2} \{pk-1,pj\}
+2(h+2)(h+1) \sum_{j=2}^{p-2} \Big(\{p,pj\}+\{-p,pj\}\Big)
\end{aligned}$$ Thus $$\begin{aligned}
\ & \sum_{k=0}^{h+1} \sum_{l=0}^{h}\sum_{j=2}^{p-2} \{g_{k,1},g_{l,j}\}
+\sum_{k=0}^{h+1} \sum_{j=2}^{h+1} \{g_{k,1},g_{h+1,j}\} \\
=&\sum_{k=0}^{h+1} \sum_{l=0}^{p-1}\sum_{j=2}^{p-2} \{pk+1,pl+j\}
+\sum_{k=h+2}^{p} \sum_{l=0}^{p-1}\sum_{j=2}^{p-2} \{pk-1,pl+j\}\\
\ +&\frac{p+1}2\sum_{l=0}^{p-1}\sum_{j=2}^{p-2}\Big(\{p,pl+j\}+\{-p,pl+j\}\Big)
+p\sum_{k=0}^{h+1}\sum_{j=2}^{p-2} \{pk+1,pj\}\\
+&p\sum_{k=h+2}^{p} \sum_{j=2}^{p-2} \{pk-1,pj\}
+\frac{p^2-1}{2} \sum_{j=2}^{p-2} \Big(\{p,pj\}+\{-p,pj\}\Big)
\end{aligned}$$ Similarly, $$\begin{aligned}
\ & \sum_{k=0}^{h} \sum_{l=0}^{h}\sum_{j=2}^{p-2} \{g_{k,p-1},g_{l,j}\}
+\sum_{k=0}^{h} \sum_{j=2}^{h+1} \{g_{k,p-1},g_{h+1,j}\} \\
=&\sum_{k=1}^{h+1} \sum_{l=0}^{p-1}\sum_{j=2}^{p-2} \{pk-1,pl+j\}
+\sum_{k=h+2}^{p-1} \sum_{l=0}^{p-1}\sum_{j=2}^{p-2} \{pk+1,pl+j\}\\
\ +&\frac{p-1}2\sum_{l=0}^{p-1}\sum_{j=2}^{p-2} \Big(\{p,pl+j\}+\{-p,pl+j\}\Big)
+p\sum_{k=1}^{h+1}\sum_{j=2}^{p-2} \{pk-1,pj\}\\
+&p\sum_{k=h+2}^{p-1} \sum_{j=2}^{p-2} \{pk+1,pj\}
+\frac{(p-1)^2}{2} \sum_{j=2}^{p-2} \Big(\{p,pj\}+\{-p,pj\}\Big)
\end{aligned}$$ Altogether the expression in the claim is reduced to $$\begin{aligned}
\ &\sum_{k=0}^{p-1} \sum_{l=0}^{p-1}\sum_{j=2}^{p-2} \{pk+1,pl+j\}
 +\sum_{k=1}^{p} \sum_{l=0}^{p-1}\sum_{j=2}^{p-2}\{pk-1,pl+j\} \\
+&p\sum_{l=0}^{p-1}\sum_{j=2}^{p-2} \Big(\{p,pl+j\}+\{-p,pl+j\}\Big)
+p\sum_{k=0}^{p-1}\sum_{j=2}^{p-2} \{pk+1,pj\}\\
+&p\sum_{k=1}^{p}\sum_{j=2}^{p-2} \{pk-1,pj\}
+p(p-1)\sum_{j=2}^{p-2} \Big(\{p,pj\}+\{-p,pj\}\Big)
\end{aligned}$$ This is equal to $$\begin{aligned}
\sum_{k=0}^{p-1} \sum_{l=0}^{p-1}\sum_{j=2}^{p-2} \Big(&[pk+1,pl+j]-[p(k+l)+j+1,pl+j]+[p(k+l)+j+1,pk+1]\Big)\\
+\sum_{k=1}^p \sum_{l=0}^{p-1}\sum_{j=2}^{p-2} \Big(&[pk-1,pl+j]-[p(k+l)+j-1,pl+j]+[p(k+l)+j-1,pk+1]\Big)\\
+p\sum_{l=0}^{p-1}\sum_{j=2}^{p-2}
\Big(&[p,pl+j]-[p(l+1)+j,pl+j]+[p(l+1)+j,p]\\
+&[-p,pl+j]-[p(l-1)+j,pl+j]+[p(l-1)+j,-p] \Big)\\
+p\sum_{k=0}^{p-1}\sum_{j=2}^{p-2}
\Big(&[pk+1,pj]-[p(j+k)+1,pj]+[p(j+k)+1,pk+1]\Big)\\
+p\sum_{k=1}^{p}\sum_{j=2}^{p-2}
\Big(&[pk-1,pj]-[p(j+k)-1,pj]+[p(j+k)-1,pk-1]\Big)\\
+p(p-1)\sum_{j=2}^{p-2}
\Big(&[p,pj]-[p(j+1),pj]+[p(j+1),p]\\
+&[-p,pj]-[p(j-1),pj]+[p(j-1),-p]\Big)=0
\end{aligned}$$ after many cancelations. ◻
:::

We have verified the claim in the above proof for $p=5$ and $p=7$ numerically. In fact, we find that $\dim (\ker \beta_{25})=5$ and $\dim (\ker \beta_{49})=35$. This implies that $d(2,25)\le 116$ and $d(2,49)\le 449$. Further, if Grothendieck's transcendence conjecture is true then the equalities hold. With MAPLE we have verified $d(2,25)\le 116$ and $d(2,49)\le 449$ by using the standard relations so that these relations imply all the others.

It is convenient to say a level $N$ is *standard* if either (i) $N=1, 2$ or $3$, or (ii) $N$ is a prime power $p^n$ ($p\ge 5$). Otherwise $N$ is called *non-standard*. We prove in [@Zpolyrel] the following

::: thm
Suppose $N$ is non-standard. Then the non-standard relations exist in $\MPV(3,N)$ for $4\le N\le 12$ and in $\MPV(2,N)$ for $10\le N\le 48$.
:::

Preliminary results suggest that the following

::: conj
[]{#conj:stand label="conj:stand"} If $N$ is a standard level then the standard relations always provide the sharp bounds of $d(w,N)$, namely, all linear relations can be derived from the standard ones. If $N$ is a non-standard level then the bound in *[@DG Cor. 5.25]* is sharp and the non-standard relations exist in $\MPV(w,N)$ for all $w\ge 3$ (and in $\MPV(2,N)$ if $N\ge 10$).
:::

**Acknowledgements.** I would like to express my deepest gratitude to Prof. Deligne for patiently explaining [@DG] to me and suggesting to use octahedral symmetry in level four. This note was written when I was visiting the Institute for Advanced Study at Princeton whose financial support and hospitality is gratefully acknowledged.
