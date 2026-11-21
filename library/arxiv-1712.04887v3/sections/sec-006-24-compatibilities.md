---
doc_id: arxiv-1712.04887v3
doc_title: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE"
section_id: sec-006-24-compatibilities
section_title: "Compatibilities"
section_number: 2.4
pages: 14-15
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
toc_source: outline
text_source: latex
latex_prose_ratio: 0.927
latex_coverage_ratio: 0.943
doc_brief: "BLOCH GROUPS, ALGEBRAIC K -THEORY, UNITS, AND NAHM’S CONJECTURE — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn ="
---
[]{#sub.primepowers label="sub.primepowers"}

In this section, we discuss the compatibility of the map $R_\zeta$ with respect to $n$, and in particular we compare $R_{\zeta}$ to $R_{\zeta^q}$ for any divisor $q$ of $n$. This will be important in Section [\[sec.cRcompare\]](#sec.cRcompare){reference-type="ref" reference="sec.cRcompare"}, where we consider the relation of our map and the Chern class in $K$-theory. We also discuss the compatibility of $R_{\zeta}$ with respect to a change of field.

::: lemma
[]{#lemma:compatibility label="lemma:compatibility"} Let $(n,w_F)=1$ and $\zeta=\zeta_n$ as usual. Then the following compatibilities hold:

1.  []{#lemma:compatibilitytwo label="lemma:compatibilitytwo"} If $(n,k) = 1$, then $R_{\zeta^k}(X) = R_\zeta(X)^{k^{-1}}$.

2.  Let $n= qr$, and let $\zeta_{r} = \zeta^{q}_n$. Then the image of $R_{\zeta_n}(X)$ modulo $r$th powers is equal to the image of $R_{\zeta_{r}}(X)$ under the map $$\label{warning}
    \left(F_r^{\times}/F_r^{\times r}\right)^{\chi^{-1}} \rightarrow 
    \left(F_n^{\times}/F_n^{\times r}\right)^{\chi^{-1}}$$ induced by the inclusion.
:::

We note in passing that the map ([\[warning\]](#warning){reference-type="ref" reference="warning"}) is not always injective (a fact exploited in the proof of Lemma [\[invertible\]](#invertible){reference-type="ref" reference="invertible"}).

::: proof
*Proof.* The first statement reflects the fact that $g R_{\zeta}  = R_{g (\zeta)}$ for $g \in G = \mathrm{Gal}(F_n/F)$. For the second claim, we first note by Lemma [\[lem.Rz\]](#lem.Rz){reference-type="ref" reference="lem.Rz"}[\[partb.Rz\]](#partb.Rz){reference-type="ref" reference="partb.Rz"} that $D_{\zeta_n}(1) = \zeta^{n/3}_n \equiv \zeta^{r/3}_r = D_{\zeta_r}(1)$, where the equivalence is modulo $r$th powers. (Either $3|r$ in which case both sides are literally equal, or $(3,r) = 1$ and $3$rd roots of unity are $r$th powers.) Then we calculate $$\begin{aligned}
{D_{\zeta_n}(1) P_{\zeta_n}(X)}
&\;=\; \prod_{k\;\text{\rm mod}\;n}\bigl(1-\zeta_n^kx\bigr)^k
\;=\; \prod_{\substack{i\;\text{\rm mod}\;q\\ j\;\text{\rm mod}\;r}}\bigl(1-\zeta_n^{ri+j}x\bigr)^{ri+j} \\
&\;\equiv\;  \prod_{\substack{i\;\text{\rm mod}\;q\\ j\;\text{\rm mod}\;r}} \bigl(1-\zeta_q^i\zeta_n^jx\bigr)^j


\;=\; \prod_{j\;\text{\rm mod}\;r}\bigl(1-\zeta_r^jx^q\bigr)^j \;=\; 
{D_{\zeta_r}(1) P_{\zeta_r}(X)},
\end{aligned}$$ where the congruence is modulo $r$th powers. ◻
:::

Next, we discuss a reduction of the map $P_{\zeta_n}$ to the case that $n$ is a prime power.

::: lemma
[]{#lem.mab label="lem.mab"} Let $n=ab$ with $(a,b)=1$ and $\zeta$ a primitive $n$th root of unity. If $X \in A(F;\mathbf Z/n\mathbf Z)$, let $u_n=R_{\zeta}(X)$, $u_a=R_{\zeta^b}(X)$ and $u_b=R_{\zeta^a}(X)$. Then $u_n$ determines and is uniquely determined by $u_a$ and $u_b$.
:::

::: proof
*Proof.* Part (2) of Lemma [\[lemma:compatibility\]](#lemma:compatibility){reference-type="ref" reference="lemma:compatibility"} shows that the image of $u_n$ in $F_n^\times/F_n^{\times a}$ is the image of $u_a$ under the natural map $$F_a^\times/F_a^{\times a} \to F_n^\times/F_n^{\times a} \,.$$ Equivalently, $u_a$ determines $u_n$ up to an $a$th power, and similarly $u_b$ determines $u_n$ up to a $b$th power. This is enough to determine $u_n$ completely since $a$ and $b$ are coprime. The converse has already been shown. ◻
:::

::: remark
Both lemmas hold also for $(n,w_F)>1$ if we replace $R_\zeta$ by $R^{w_F}_{\zeta}$.
:::

We also have:

::: lemma
[]{#lemma:compatibility2 label="lemma:compatibility2"} Let $E/F$ be a field extension, and assume that $(n,w_E) = 1$ and $\zeta= \zeta_{n}$. Then the following diagram commutes:

::: diagram
B(F)/n B(F) & \_R\_ & (F_n\^/F_n\^r)\^\^-1\
& &\
B(E)/n B(E) & \_R\_ & (E_n\^/E_n\^r)\^\^-1.
:::
:::

::: proof
*Proof.* By construction, the maps $P_{\zeta}(\xi)$ are compatible where the targets on the RHS are replaced by the corresponding universal Kummer extensions. But by the uniqueness of the lift $R_{\zeta}(\xi)$ (Proposition [\[prop.Pdef\]](#prop.Pdef){reference-type="ref" reference="prop.Pdef"}(b)), the diagram commutes. ◻
:::
