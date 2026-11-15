---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidiﬁcation"
section_id: sec-012-62-functoriality-of-degroupoidification
section_title: "Functoriality of Degroupoidification"
section_number: 6.2
pages: 53-56
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.994
doc_brief: "Higher Dimensional Algebra VII: Groupoidiﬁcation — Groupoidiﬁcation is a form of categoriﬁcation in which vector spaces are replaced by groupoids and linear operators are replaced by spans of"
---
In this section we prove that our process of turning groupoids into vector spaces and spans of groupoids into linear operators is indeed a functor. We first show that the process preserves identities, then show associativity of composition, from which many other things follow, including the preservation of composition. The lemmas in this section add up to a proof of the following theorem:

::: thm
[]{#functor label="functor"} Degroupoidification is a functor from the category of groupoids and equivalence classes of tame spans to the category of real vector spaces and linear operators.
:::

::: proof
*Proof.* As mentioned above, the proof follows from Lemmas [\[identities\]](#identities){reference-type="ref" reference="identities"} and [\[composition\]](#composition){reference-type="ref" reference="composition"}. ◻
:::

::: lemma
[]{#identities label="identities"} Degroupoidification preserves identities, i.e., given a groupoid $X$, $\utilde{1_X} = 1_{{\mathbb R}^{\utilde{X}}}$, where $1_X$ is the identity span from $X$ to $X$ and $1_{{\mathbb R}^{\utilde{X}}}$ is the identity operator on ${\mathbb R}^{\utilde{X}}$.
:::

::: proof
*Proof.* This follows from the explicit formula given in Theorem [\[matrix1\]](#matrix1){reference-type="ref" reference="matrix1"}. ◻
:::

We now want to prove the associativity of composition of tame spans. Amongst the consequences of this proposition we can derive the preservation of composition under degroupoidification. Given a triple of composable spans: $$\xymatrix{
 & T \ar[dl]_{q_T}\ar[dr]^{p_T} && S \ar[dl]_{q_S}\ar[dr]^{p_S} && R \ar[dl]_{q_R}\ar[dr]^{p_R} &\\
Z && Y && X && W
}$$ we want to show that composing in the two possible orders---$T(SR)$ or $(TS)R$---will provide equivalent spans of groupoids. In fact, since groupoids, spans of groupoids, and isomorphism classes of maps between spans of groupoids naturally form a bicategory, there exists a natural isomorphism called the **associator**. This tells us that the spans $T(SR)$ and $(TS)R$ are in fact equivalent. But since we have not constructed this bicategory, we will instead give an explicit construction of the equivalence $T(SR) \stackrel{\sim}\rightarrow
(TS)R$.

::: proposition
[]{#associativity label="associativity"} Given a composable triple of tame spans, the operation of composition of tame spans by weak pullback is associative up to equivalence of spans of groupoids.
:::

::: proof
*Proof.* We consider the above triple of spans in order to construct the aforementioned equivalence. The equivalence is simple to describe if we first take a close look at the groupoids $T(SR)$ and $(TS)R$. The composite $T(SR)$ has objects $(t,(s,r,\alpha),\beta)$ such that $r\in
R$, $s\in S$, $t\in T$, $\alpha\colon q_R(r)\rightarrow p_S(s)$, and $\beta\colon q_S(s)\rightarrow p_T(t)$, and morphisms $f \colon
(t,(s,r,\alpha),\beta) \rightarrow(t',(s',r',\alpha'),\beta')$, which consist of a map $g \colon(s,r,\alpha) \rightarrow(s',r',\alpha')$ in $SR$ and a map $h \colon t \rightarrow t'$ such that the following diagram commutes: $$\xymatrix{
q_S\pi_s((s,r,\alpha)) \ar[r]^---{\beta} \ar[d]_{q_S\pi_S(g)} & p_T(t) \ar[d]^{p_T(h)} \\
q_S\pi_s((s',r',\alpha')) \ar[r]_---{\beta'} & p_T(t')
}$$ where $\pi_S$ maps the composite $SR$ to $S$. Further, $g$ consists of a pair of maps $k\colon r \rightarrow r'$ and $j \colon s\rightarrow s'$ such that the following diagram commutes: $$\xymatrix{
q_R(r) \ar[r]^{\alpha} \ar[d]_{q_S(k)} & p_S(s) \ar[d]^{p_S(j)} \\
q_R(r') \ar[r]_{\alpha'} & p_S(s')
}$$

The groupoid $(TS)R$ has objects $((t,s,\alpha),r,\beta)$ such that $r\in R$, $s\in S$, $t\in T$, $\alpha\colon q_S(s)\rightarrow p_T(t)$, and $\beta\colon q_R(r)\rightarrow p_S(s)$, and morphisms $f \colon
((t,s,\alpha),r,\beta) \rightarrow((t',s',\alpha'),r',\beta')$, which consist of a map $g \colon(t,s,\alpha) \rightarrow(t',s',\alpha')$ in $TS$ and a map $h \colon r \rightarrow r'$ such that the following diagram commutes: $$\xymatrix{
p_R(r) \ar[d]_{p_R(h)}\ar[r]^---{\beta} & p_S\pi_s((t,s,\alpha)) 
 \ar[d]^{p_S\pi_S(g)}   \\
p_R(r')  \ar[r]_---{\beta'} & p_S\pi_s((t',s',\alpha')) 
}$$ Further, $g$ consists of a pair of maps $k\colon s \rightarrow s'$ and $j \colon
t\rightarrow t'$ such that the following diagram commutes: $$\xymatrix{
q_S(s) \ar[r]^{\alpha} \ar[d]_{q_S(k)} & p_T(t) \ar[d]^{p_T(j)} \\
q_S(s') \ar[r]_{\alpha'} & p_T(t')
}$$

We can now write down a functor $F\colon T(SR) \rightarrow(TS)R$: $$(t,(s,r,\alpha),\beta) \mapsto ((t,s,\beta),r,\alpha)$$ Again, a morphism $f \colon(t,(s,r,\alpha),\beta) \rightarrow
(t',(s',r',\alpha'),\beta')$ consists of maps $k\colon r \rightarrow r'$, $j
\colon s\rightarrow s'$, and $h \colon t \rightarrow t'$. We need to define $F(f) \colon
((t,s,\beta),r,\alpha) \rightarrow((t',s',\beta'),r',\alpha')$. The first component $g' \colon(t,s,\beta) \rightarrow(t',s',\beta')$ consists of the maps $j\colon s\rightarrow s'$ and $h\colon t \rightarrow t'$, and the following diagram commutes: $$\xymatrix{
q_S(s) \ar[r]^{\beta}\ar[d]_{q_S(j)} & p_T(t) \ar[d]^{p_T(h)} \\
q_S(s') \ar[r]_{\beta'} & p_T(t')
}$$ The other component map of $F(f)$ is $k \colon r \rightarrow r'$ and we see that the following diagram also commutes: $$\xymatrix{
p_R(r) \ar[d]_{p_R(k)}\ar[rr]^---{\alpha} && p_S\pi_s((t,s,\beta))  \ar[d]^{p_S\pi_S(g')}   \\
p_R(r')  \ar[rr]_---{\alpha'} && p_S\pi_s((t',s',\beta')) 
}$$ thus, defining a morphism in $(TS)R$.

We now just need to check that $F$ preserves identities and composition and that it is indeed an isomorphism. We will then have shown that the apexes of the two spans are isomorphic. First, given an identity morphism $1\colon(t,(s,r,\alpha),\beta) \rightarrow
(t,(s,r,\alpha),\beta)$, then $F(1)$ is the identity morphism on $((t,s,\beta),r,\alpha)$. The components of the identity morphism are the respective identity morphisms on the objects $r$,$s$, and $t$. By the construction of $F$, it is clear that $F(1)$ will then be an identity morphism.

Given a pair of composable maps $f \colon(t,(s,r,\alpha),\beta) \rightarrow
(t',(s',r',\alpha'),\beta')$ and $f' \colon(t',(s',r',\alpha'),\beta')
\rightarrow(t'',(s'',r'',\alpha''),\beta'')$ in $T(SR)$, the composite is a map $f'f$ with components $g'g \colon(s,r,\alpha) \rightarrow
(s'',r'',\alpha'')$ and $h'h\colon t \rightarrow t''$. Further, $g'g$ has component morphisms $k'k \colon r\rightarrow r''$ and $j'j \colon s\rightarrow s'$. It is then easy to check that under the image of $F$ this composition is preserved.

The construction of the inverse of $F$ is implicit in the construction of $F$, and it is easy to verify that each composite $FF^{-1}$ and $F^{-1}F$ is an identity functor. Further, the natural isomorphisms required for an equivalence of spans can each be taken to be the identity. ◻
:::

It follows from the associativity of composition that degroupoidification preserves composition:

::: lemma
[]{#composition label="composition"} Degroupoidification preserves composition. That is, given a pair of composable tame spans: $$\xymatrix{
  & T\ar[dr]\ar[dl]  &   & S\ar[dr]\ar[dl] & \\
Z &                  & Y &                 & X
}$$ we have $$\utilde{T}\utilde{S} = \utilde{TS}.$$
:::

::: proof
*Proof.* Consider the composable pair of spans above along with a groupoid $\Psi$ over $X$: $$\xymatrix{
  & T\ar[dr]\ar[dl]  &   & S\ar[dr]\ar[dl] &  & \Psi\ar[dr]\ar[dl] &\\
Z &                  & Y &                 & X &     & 1
}$$ We can consider the groupoid over $X$ as a span by taking the right leg to be the unique map to the terminal groupoid. We can compose this triple of spans in two ways; either $T(S\Psi)$ or $(TS)\Psi$. By the Proposition [\[associativity\]](#associativity){reference-type="ref" reference="associativity"} stated above, these spans are equivalent. By Theorem [\[linops_equivspans1\]](#linops_equivspans1){reference-type="ref" reference="linops_equivspans1"}, degroupoidification produces the same linear operators. Thus, composition is preserved. That is, $$\utilde{T}\utilde{S}\utilde{\Psi} = \utilde{TS}\utilde{\Psi}.$$ ◻
:::
