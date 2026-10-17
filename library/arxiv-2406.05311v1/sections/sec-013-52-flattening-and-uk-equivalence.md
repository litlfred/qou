---
doc_id: arxiv-2406.05311v1
doc_title: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD"
section_id: sec-013-52-flattening-and-uk-equivalence
section_title: "Flattening and (u,k)-equivalence"
section_number: 5.2
pages: 17-19
source_pdf: 2406.05311v1.pdf
source_sha256: c431fca150329547
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.967
doc_brief: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD — In this paper, we give a rule for the multiplication of a Schubert class by a tautological class in the (small)"
---
[]{#SS:Shape-equivalence label="SS:Shape-equivalence"}

Equivalence among classical operators, [\[Eq:monoid-relations\]](#Eq:monoid-relations){reference-type="eqref" reference="Eq:monoid-relations"} and Proposition [\[Prop:monoid\]](#Prop:monoid){reference-type="ref" reference="Prop:monoid"}, depends only upon the relative order of the indices, and not their actual values. We establish a version for quantum operators. We begin with some definitions.

Let $a=(a_1,\dotsc,a_t)$ be a sequence of integers and set $m\vcentcolon=\#\{a_1,\dotsc,a_t\}$, the number of distinct integers in this sequence. The of $a$ is the sequence $(c_1,\dotsc,c_t)$ where each $c_i\in[m]$ and $c_i>c_j$ if and only if $a_i>a_j$. For example, the flattening of $(3,6,1,6,8,3,1)$ is $(2,3,1,3,4,2,1)$. Sequences are if they have the same flattening. The flattening of an operator ${\mathbf v}_{a_r b_r}\dotsb{\mathbf v}_{a_1 b_1}$ is ${\mathbf v}_{c_r d_r}\dotsb{\mathbf v}_{c_1 d_1}$, where $(c_r,d_r,\dotsc,c_1,d_1)$ is the flattening of $(a_r,b_r,\dotsc,a_1,b_1)$. Operators ${\mathbf v}$ and ${\mathbf v}'$ are if they have the same flattening. This extends the notion of shape-equivalence of permutations $\zeta$ from Section [\[SS:GBO\]](#SS:GBO){reference-type="ref" reference="SS:GBO"}.

The of an operator ${\mathbf v}={\mathbf v}_{a_r b_r}\dotsb{\mathbf v}_{a_1 b_1}$ is $\mathop{\mathrm{supp}}({\mathbf v})\vcentcolon=\{a_r,b_r,\dotsc,a_1,b_1\}$. The operator ${\mathbf v}$ is if the factorization of $\zeta=\zeta({\mathbf v})=(a_r,b_r)\dotsb(a_1,b_1)$ into transpositions has minimal length in that $r=\#\mathop{\mathrm{supp}}(\zeta)-s(\zeta)$. As $r$ is the minimal possible number of transpositions whose product is $\zeta$, we have that $\mathop{\mathrm{supp}}(\zeta({\mathbf v}))=\{a_r,b_r,\dotsc,a_1,b_1\}=\mathop{\mathrm{supp}}({\mathbf v})$. Furthermore, if ${\mathbf v}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u=q^\alpha w$, then as $\zeta({\mathbf v})=wu^{-1}$, the interval $[u,q^\alpha w]_k^q$ is minimal in the sense of Section [\[sec:Qminim\]](#sec:Qminim){reference-type="ref" reference="sec:Qminim"}. Later, in the proof of Theorem [\[Th:nonZero\]](#Th:nonZero){reference-type="ref" reference="Th:nonZero"} in Section [\[sec:final\]](#sec:final){reference-type="ref" reference="sec:final"}, we will show that the permutation $\zeta({\mathbf v})$ is a minimal permutation in the sense of Section [\[minimal-permutations\]](#minimal-permutations){reference-type="ref" reference="minimal-permutations"}.

Shape-equivalence preserves equivalence to ${\mathbf 0}$ and for minimal operators, $(u,k)$-equivalence.

::: theorem
[]{#Th:shape-equivalence label="Th:shape-equivalence"} Let ${\mathbf v}$ be an operator with flattening ${\mathbf v}'$. Then ${\mathbf v}\equiv{\mathbf 0}$ if and only if ${\mathbf v}'\equiv{\mathbf 0}$.

Suppose that ${\mathbf v}$ is nonzero and minimal, and that ${\mathbf u}$ is an operator that is $(u,k)$-equivalent to ${\mathbf v}$ for some $u\in S_n$ and $k<n$. Then ${\mathbf u}$ is minimal and $\mathop{\mathrm{supp}}({\mathbf v})=\mathop{\mathrm{supp}}({\mathbf u})$. Furthermore, if ${\mathbf v}'$ is the flattening of ${\mathbf v}$ and ${\mathbf u}'$ the flattening of ${\mathbf u}$, then there exist $x\in S_m$ and $l<m$, where $m=\#\mathop{\mathrm{supp}}({\mathbf v})$, such that ${\mathbf v}'$ is $(x,l)$-equivalent to ${\mathbf u}'$.
:::

We deduce Theorem [\[Th:shape-equivalence\]](#Th:shape-equivalence){reference-type="ref" reference="Th:shape-equivalence"} at the end of this subsection after establishing some preliminary lemmas and definitions. Let $s\in[n]$. Define the truncation map ${\color{RoyalBlue}\tau_s}\colon[n]\to[n{-}1]$ by

$$\tau_s(j)\ =\ \left\{ \begin{array}{rcl} j&\ &\mbox{if }j<s\\ j{-}1&&\mbox{if } j\geq s\end{array}\right. \ .$$

This extends to operators. For distinct $a,b,s\in[n]$, define ${\color{RoyalBlue}\tau_s({\mathbf v}_{a,b})}\vcentcolon={\mathbf v}_{\tau_s(a),\tau_s(b)}$. If ${\mathbf v}$ is an operator and $s\not\in\mathop{\mathrm{supp}}({\mathbf v})$, then we may apply $\tau_s$ to every operator ${\mathbf v}_{a,b}$ in ${\mathbf v}$, and we define $\tau_s({\mathbf v})$ to be the composition of the $\tau_s({\mathbf v}_{a,b})$. For example, $\tau_3({\mathbf v}_{45}{\mathbf v}_{51}{\mathbf v}_{25})={\mathbf v}_{34}{\mathbf v}_{41}{\mathbf v}_{24}$.

For $u\in S_n$ and $r\in[n]$, let ${\color{RoyalBlue}u/r}\in S_{n-1}$ be the permutation obtained by deleting the $r$th column and $u(r)$th row of the permutation matrix of $u$. In one-line notation, this is obtained by omitting the $r$th value of $u$ and then flattening, so that $(41\underline{3}652)/3=31542$. Omitting the $s$th component of $\alpha\in{\mathbb N}^{n-1}$ gives $\alpha/s\in{\mathbb N}^{n-2}$, which is the sequence $(\alpha_1,\dotsc,\alpha_{s-1},\alpha_{s+1},\dotsc,\alpha_{n-1})$. Thus $(3,1,\underline{2},4,0)/3 = (3,1,4,0)$.

We also have an expansion map ${\color{RoyalBlue}\iota_s}\colon[n{-}1]\to[n]$ defined by

$$\iota_s(j)\ =\ \left\{ \begin{array}{rcl} j&\ &\mbox{if }j<s,\\ j{+}1&&\mbox{if } j\geq s.\end{array}\right.$$

This extends to operators in the same way as $\tau_s$ extended to operators. For $r,s\in[n{+}1]$ and $v\in S_n$, define a permutation $u=\varepsilon_{r,s}(v)\in S_{n+1}$ by $u(r)=s$ and $u/r=v$. For $\alpha\in{\mathbb N}^{n-1}$, define $\varepsilon_{r,s}(\alpha)\vcentcolon=(\alpha_1,\dotsc,\alpha_{r{-}1},s,\alpha_r,\dotsc,\alpha_{n-1})\in{\mathbb N}^{n}$.

::: lemma
[]{#L:relative-labels label="L:relative-labels"} Let ${\mathbf v}$ be a nonzero operator with ${\mathbf v}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u=q^\alpha w$.

1.  []{#L:r-l:i label="L:r-l:i"} For $s\not\in\mathop{\mathrm{supp}}({\mathbf v})$, set $r=u^{-1}(s)$. Then $r=w^{-1}(s)$ and $\tau_s({\mathbf v}) {\mathop{\mathrm{{\scriptstyle \bullet}}}}_{\tau_r(k)} (u/r) = q^{\alpha/r} w/r$.

2.  []{#L:r-l:ii label="L:r-l:ii"} Suppose that $r\leq u^{-1}(a)$ for all $a\in\mathop{\mathrm{supp}}({\mathbf v})$ or $r>u^{-1}(a)$ for all $a\in\mathop{\mathrm{supp}}({\mathbf v})$. Then for any $s\in[n{+}1]$, $\iota_s({\mathbf v})\mathop{\mathrm{{\scriptstyle \bullet}}}_{\iota_r(k)} \varepsilon_{r,s}(u) = q^{\varepsilon_{r,0}(\alpha)}\varepsilon_{r,s}(w)$.
:::

::: proof
*Proof.* Both statements follow (by composition) from the case when ${\mathbf v}={\mathbf v}_{ab}$ is a single operator. As $u\lessdot_k q^\alpha w={\mathbf v}_{ab}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u$, we have $w=(a,b)u=u(i,j)$, where $i=u^{-1}(a)\leq k < u^{-1}(b)=j$ and either $q^\alpha=1$ when $a<b$ or $q^\alpha=q_{i,j}$ when $a>b$. The statements follow from the definitions of $\tau_s$, $\iota_s$, $/r$, $\varepsilon_{r,s}$, and the characterizations of covers in Propositions [\[nothing-in-between-is-in-between\]](#nothing-in-between-is-in-between){reference-type="ref" reference="nothing-in-between-is-in-between"} and [\[prop:quantum-k-bruhat-covers\]](#prop:quantum-k-bruhat-covers){reference-type="ref" reference="prop:quantum-k-bruhat-covers"}, in a case-by-case analysis depending upon the relative positions of $s$ with $a,b$ and $r$ with $i,j$. While we omit that analysis, we illustrate three cases in Example [\[Ex:three_cases\]](#Ex:three_cases){reference-type="ref" reference="Ex:three_cases"} below.

Note that when $a<b$, ${\mathbf v}_{ab}$ is classical, which is treated in [@BS-Bruhat; @BS-Monoid]. ◻
:::

::: example
[]{#Ex:three_cases label="Ex:three_cases"} Let $u=154\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}32$. Then ${\mathbf v}_{53}\mathop{\mathrm{{\scriptstyle \bullet}}}_3 u = q_2q_3 13452$. We illustrate Lemma [\[L:relative-labels\]](#L:relative-labels){reference-type="ref" reference="L:relative-labels"}[\[L:r-l:i\]](#L:r-l:i){reference-type="ref" reference="L:r-l:i"}. Consider each case of $s\in\{1,2,4\}=[5]\smallsetminus\mathop{\mathrm{supp}}({\mathbf v}_{53})$.

-   If $s=1$ then $r=1$, $\tau_1(3)=2$, and $u/1=4321$. Thus, we have ${\mathbf v}_{42}\mathop{\mathrm{{\scriptstyle \bullet}}}_2 43\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}21= q_1q_2 2341$.

-   If $s=2$ then $r=5$, $\tau_5(3)=3$, and $u/5=1432$. Thus, we have ${\mathbf v}_{42}\mathop{\mathrm{{\scriptstyle \bullet}}}_3 143\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}2= q_2 q_3 1234$.

-   If $s=4$ then $r=3$, $\tau_3(3)=2$, and $u/3=1432$. Thus, we have ${\mathbf v}_{43}\mathop{\mathrm{{\scriptstyle \bullet}}}_2 14\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}32= q_2 1342$.

For Lemma [\[L:relative-labels\]](#L:relative-labels){reference-type="ref" reference="L:relative-labels"}[\[L:r-l:ii\]](#L:r-l:ii){reference-type="ref" reference="L:r-l:ii"}, $r$ is either at most 2 or greater than 4.

-   $r=1$. Let $s=4$. Then $\iota_4({\mathbf v}_{53})={\mathbf v}_{63}$, $\iota_1(3)=4$, and $\varepsilon_{1,4}(u)=416532$. We have ${\mathbf v}_{63}\mathop{\mathrm{{\scriptstyle \bullet}}}_4 4165\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}32=q_3q_4 413562$.

-   $r=5$. Let $s=3$. Then $\iota_3({\mathbf v}_{53})={\mathbf v}_{64}$, $\iota_5(3)=3$, and $\varepsilon_{5,3}(u)=165432$. We have ${\mathbf v}_{64}\mathop{\mathrm{{\scriptstyle \bullet}}}_3 165\raisebox{-1pt}{\hspace{0.55pt}\color{magenta}\rule{0.75pt}{11pt}}\hspace{0.55pt}432=q_2q_3 145632$. $\diamond$
:::

::: corollary
[]{#C:single_equivalences label="C:single_equivalences"} Let ${\mathbf v}$ be a composition of operators.

1.  []{#C:SE_1 label="C:SE_1"} For $s\in[n]\smallsetminus\mathop{\mathrm{supp}}({\mathbf v})$, we have that ${\mathbf v}\equiv{\mathbf 0}$ if and only if $\tau_s({\mathbf v})\equiv{\mathbf 0}$.

2.  For $s\in[n{+}1]$, we have that ${\mathbf v}\equiv{\mathbf 0}$ if and only if $\iota_s({\mathbf v})\equiv{\mathbf 0}$.

3.  []{#C:SE_3 label="C:SE_3"} Suppose that ${\mathbf v}$ is nonzero and ${\mathbf v}'$ is a composition that is $(u,k)$-equivalent to ${\mathbf v}$ for some $u\in S_n$ and $k<n$.

    1.  []{#C:SE_3_i label="C:SE_3_i"} Let $s\in[n]\smallsetminus(\mathop{\mathrm{supp}}({\mathbf v})\cup\mathop{\mathrm{supp}}({\mathbf v}'))$ and set $r\vcentcolon= u^{-1}(s)$. Then $\tau_s({\mathbf v})$ and $\tau_s({\mathbf v}')$ are $(u/r,\tau_r(k))$-equivalent.

    2.  For any $s\in[n{+}1]$ and any $r$ such that either $r\leq u^{-1}(a)$ for all $a\in\mathop{\mathrm{supp}}({\mathbf v})\cup\mathop{\mathrm{supp}}({\mathbf v}')$ or $r>u^{-1}(a)$ for all $a\in\mathop{\mathrm{supp}}({\mathbf v})\cup\mathop{\mathrm{supp}}({\mathbf v}')$, we have that $\iota_s({\mathbf v})$ and $\iota_s({\mathbf v}')$ are $(\varepsilon_{r,s}(u), \iota_r(k))$-equivalent.
:::

::: proof
*Proof.* The third statement holds by Lemma [\[L:relative-labels\]](#L:relative-labels){reference-type="ref" reference="L:relative-labels"}. This also proves the (contrapositive of) the implication $\Leftarrow$ in the first two statements. As in (1), ${\mathbf v}=\iota_s(\tau_s({\mathbf v}))$ and in (2), $s\not\in\mathop{\mathrm{supp}}(\iota_s({\mathbf v}))$ and ${\mathbf v}=\tau_s(\iota_s({\mathbf v}))$, the other directions also hold. ◻
:::

::: proof
*Proof of Theorem [\[Th:shape-equivalence\]](#Th:shape-equivalence){reference-type="ref" reference="Th:shape-equivalence"}.* As flattening is induced by applying truncation operators, the first statement of Theorem [\[Th:shape-equivalence\]](#Th:shape-equivalence){reference-type="ref" reference="Th:shape-equivalence"} follows from Corollary [\[C:single_equivalences\]](#C:single_equivalences){reference-type="ref" reference="C:single_equivalences"} [\[C:SE_1\]](#C:SE_1){reference-type="ref" reference="C:SE_1"}.

Suppose that ${\mathbf v}$ is nonzero and minimal. Let ${\mathbf u}$ be an operator that is $(u,k)$-equivalent to ${\mathbf v}$. Then there exist $w\in S_n$ and $\alpha\in{\mathbb N}^{n-1}$ such that ${\mathbf v}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u={\mathbf u}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u=q^\alpha w$. As $\zeta({\mathbf v})=wu^{-1}$, $\zeta({\mathbf u})=\zeta({\mathbf v})$. As $(u,k)$-equivalence is ranked, both ${\mathbf v}$ and ${\mathbf u}$ involve the same number of elementary operators ${\mathbf v}_{ab}$. This implies that ${\mathbf u}$ is minimal and that $\mathop{\mathrm{supp}}({\mathbf v})=\mathop{\mathrm{supp}}({\mathbf u})$.

Consequently, any sequence of truncation operators that flattens ${\mathbf v}$ also flattens ${\mathbf u}$. The existence of $x$ and $l$ in the final part of Theorem [\[Th:shape-equivalence\]](#Th:shape-equivalence){reference-type="ref" reference="Th:shape-equivalence"} follows by applying Corollary [\[C:single_equivalences\]](#C:single_equivalences){reference-type="ref" reference="C:single_equivalences"} [\[C:SE_3\]](#C:SE_3){reference-type="ref" reference="C:SE_3"} [\[C:SE_3_i\]](#C:SE_3_i){reference-type="ref" reference="C:SE_3_i"} along this same sequence of truncation operators. ◻
:::
