---
doc_id: arxiv-math-0203206v1
doc_title: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002"
section_id: sec-014-53-conjugates-and-antipodes-discrete-quantum-gro
section_title: "Conjugates and Antipodes: Discrete Quantum Groups"
section_number: 5.3
pages: 32-36
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.973
doc_brief: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002 — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups which are related to the Tannaka-Krein"
---
We have already seen that the concrete semisimple tensor $*$-categories $\mathrm{Rep}_f (A,\Delta)$ and $\mathrm{Corep}_f (\hat{A},\hat{\Delta})$ come with conjugates whenever $(A,\Delta)$ is a discrete aqg. In this section we prove the converse. We start off with a couple of preparatory results.

::: lem
[]{#l-inclusions label="l-inclusions"} Let ${\cal C}$ be a semisimple tensor $*$-category with conjugates and let $E :{\cal C}\rightarrow{\cal H}$ be an embedding functor. Then the coproduct $\Delta:A\rightarrow M(A\otimes A)$ for the discrete quantum semigroup $(A,\Delta)$ given by Proposition [\[p-cdisc\]](#p-cdisc){reference-type="ref" reference="p-cdisc"} has the following inclusion properties $$(1\otimes A)\Delta(A)\subset A\otimes A, \quad\quad (A\otimes 1)\Delta(A)\subset A\otimes A.$$
:::

*Proof. * We prove only the inclusion $(A\otimes 1)\Delta(A)\subset A\otimes A$, the proof of the inclusion $(1\otimes A)\Delta(A)\subset A\otimes A$ being completely analogous. We need to show that $(a\otimes 1)\Delta(b)\in A\otimes A$ for all $a,b\in A$. It is clearly sufficient to show this for $b=(b_i)$ where all components except $i=m$ vanish and for $a=I_n$. By the calculation done in the proof of Lemma [\[l-nondeg\]](#l-nondeg){reference-type="ref" reference="l-nondeg"} we have $$\Delta(b)_{ij}=b_{X_i\otimes X_j} = \sum_{k\in I_{\cal C}} \sum_{\alpha=1}^{N_{ij}^k} 
   E(V_{ij}^{k\alpha})\,\circ\,b_k\,\circ\,E(V_{ij}^{k\alpha*})\ \in\mathrm{End}\,E(X_i\otimes X_j).$$ In view of $a=I_n$ and $b_i=0$ for $i\ne m$ we obtain $$((a\otimes 1)\Delta(b))_{ij}=\delta_{i,n} \sum_{\alpha=1}^{N_{nj}^m} E(V_{nj}^{m\alpha})\,\circ\,
 b_m\,\circ\,E(V_{nj}^{m\alpha*}).$$ Now, since ${\cal C}$ has conjugates we have isomorphisms $\mathrm{Mor}(X_n\otimes X_j,X_m)\cong\mathrm{Mor}(X_j,\overline{X_n}\otimes X_m)$. By semisimplicity, for fixed $n,m$ the latter space is non-zero only for finitely many $j\in I_{\cal C}$. Thus $((a\otimes 1)\Delta(b))_{ij}$ is non-zero only for $i=n$ and finitely many $j$ and therefore $(a\otimes 1)\Delta(b)\in A\otimes A$.

::: prop
Let ${\cal C}$ be a semisimple tensor $*$-category with conjugates and let $E :{\cal C}\rightarrow{\cal H}$ be an embedding functor. Let $b=(b_{X,Y} )\in \mathrm{Nat}\,E\otimes$. Using the identifications $B((E(X\otimes Y))=B(E(X))\otimes B(E(Y))$, for any objects $X$ and $Y$ in ${\cal C}$, we may write $b_{X,X}=\sum_k a^k_X\otimes b^k_X\in B(E(X))\otimes B(E(X))$, and then define $\tilde{m}(b)_X\in B(E(X))$ by $$\tilde{m}(b)_X =\sum_k a^k_X\,\circ\,b^k_X,$$ for any object $X\in{\cal C}$. This gives a unital linear map $\tilde{m}:\mathrm{Nat}\,E\otimes \rightarrow\mathrm{Nat}\,E$ which sends $b\in Nat\,E\otimes$ to $\tilde{m}(b)$. Furthermore, it restricts to the linearized multiplication $m :A\otimes A\rightarrow A$ on $A\subset\mathrm{Nat}\,E$.
:::

*Proof. *The bilinear multiplication map from $B(E(X))\otimes B(E(X))$ to $B(E(X))$ exists since $E(X)$ is finite dimensional. The rest is obvious.

::: prop
[]{#p-coinv label="p-coinv"} Let ${\cal C}$ be a semisimple tensor $*$-category with conjugates and let $E :{\cal C}\rightarrow{\cal H}$ be an embedding functor. Then the discrete quantum semigroup $(A,\Delta)$ given by Proposition [\[p-cdisc\]](#p-cdisc){reference-type="ref" reference="p-cdisc"} is a discrete aqg. The coinverse $S:A\rightarrow A$ is given by $$S(a)_X =E(\mathrm{id}_X\otimes r^*_X )\,\circ\,\mathrm{id}_{E(X)}\otimes a_{\overline{X}}\otimes \mathrm{id}_{E(X)}
   \,\circ\,E(\overline{r}_X\otimes \mathrm{id}_X )$$ for all $a\in A\subset\mathrm{Nat}\,E$ and objects $X$ in ${\cal C}$, and where $(r_X, \overline{r}_X, \overline{X})$ is any solution of the conjugate equations associated to $X$.
:::

*Proof. * In view of Proposition [\[p-converse\]](#p-converse){reference-type="ref" reference="p-converse"} it is sufficient to show that $(A\otimes 1)\Delta(A)\subset A\otimes A$ and $(1\otimes A)\Delta(A)\subset A\otimes A$ and to produce an invertible coinverse $S$. We thus get an aqg since Theorem [\[thm-haar\]](#thm-haar){reference-type="ref" reference="thm-haar"} provides a (non-zero) left-invariant positive functional for discrete multiplier Hopf $*$-algebras. Now the inclusions $(A\otimes 1)\Delta(A)\subset A\otimes A$ and $(1\otimes A)\Delta(A)\subset A\otimes A$ are the content of Lemma [\[l-inclusions\]](#l-inclusions){reference-type="ref" reference="l-inclusions"}.

We show that the map $S:A\rightarrow A$ given by the formula in the theorem is well-defined. We first show that for $a\in A$ and $X\in{\cal C}$, the formula for $S(a)_X \in\mathrm{End}\,E(X)$ does not depend on the choice of solution $(r_X, \overline{r}_X, \overline{X})$ of the conjugate equations associated to $X$. Suppose therefore that $(r'_X, \overline{r}'_X, \overline{X}')$ is another solution of the conjugate equations associated to $X$. By [@LR] there exists a unique invertible $t\in\mathrm{Hom}(\overline{X},\overline{X}')$ such that $r'_X =t\otimes \mathrm{id}_X\,\circ\,r_X$ and $\overline{r}'_X =\mathrm{id}_X\otimes t^{*-1}\,\circ\,\overline{r}_X$. Thus $$\begin{aligned}
 \lefteqn{
 E(\mathrm{id}_X\otimes {r'}^*_X )\,\circ\,\mathrm{id}_{E(X)}\otimes a_{\overline{X}'}\otimes \mathrm{id}_{E(X)}
      \,\circ\,E(\overline{r}'_X\otimes \mathrm{id}_X ) } \\
 && =E(\mathrm{id}_X\otimes (r^*_X \,\circ\,t^*\otimes \mathrm{id}_X ))\,\circ\,\mathrm{id}_{E(X)}\otimes
      a_{\overline{X}'}\otimes \mathrm{id}_{E(X)} 
    \,\circ\,E((\mathrm{id}_X\otimes t^{*-1}\,\circ\,\overline{r}_X)\otimes \mathrm{id}_X ) \\
 &&=E(\mathrm{id}_X\otimes r^*_X )\,\circ\,\mathrm{id}_{E(t)}\otimes (E(t^* )\,\circ\,a_{\overline{X}'}\,\circ\,
      E(t^{*-1})) \otimes \mathrm{id}_{E(X)}\,\circ\,E(\overline{r}_X\otimes \mathrm{id}_X ) \\
 &&=E(\mathrm{id}_X\otimes r^*_X )\,\circ\,\mathrm{id}_{E(X)}\otimes (E(t^*\,\circ\,t^{*-1}\,\circ\,a_{\overline{X}})
    \otimes \mathrm{id}_{E(X)})\,\circ\,E(\overline{r}_X\otimes \mathrm{id}_X ) \\
 &&=E(\mathrm{id}_X\otimes r^*_X )\,\circ\,(\mathrm{id}_{E(X)}\otimes a_{\overline{X}}
    \otimes \mathrm{id}_{E(X)})\,\circ\,E(\overline{r}_X\otimes \mathrm{id}_X ),
\end{aligned}$$ and $S(a)_X \in\mathrm{End}\,E(X)$ does not depend on the choice of solution $(r_X, \overline{r}_X, \overline{X})$ of the conjugate equations associated with $X$.

Next we show that $S(a) =(S(a)_X )\in\mathrm{Nat}\,E$ for $a\in A$, i.e., we must show that $E(t)\,\circ\,S(a)_X =S(a)_Y\,\circ\,E(t)$, for all $a\in A$ and $t\in\mathrm{Hom}(X,Y)$. By the existence of the transpose $t^{\bullet *}\in\mathrm{Hom}(Y,X)$ given in [@LR], we get $$\begin{aligned}
E(t)\,\circ\,S(a)_X 
&=& E(\mathrm{id}_Y\otimes r_{X}^* )\,\circ\,E(t)\otimes a_{\overline{X}}
  \otimes \mathrm{id}_{E(X )}\,\circ\,E(\overline{r}_X\otimes \mathrm{id}_X) \\
&=& E(\mathrm{id}_Y\otimes r_{X}^* )\,\circ\,\mathrm{id}_{E(Y )}\otimes 
  a_{\overline{X}}\otimes \mathrm{id}_{E(X )}\,\circ\,
  E((t\otimes\mathrm{id}_{\overline{X}}\,\circ\,\overline{r}_X)\otimes \mathrm{id}_X) \\
&=& E(\mathrm{id}_Y\otimes r_X^* )\,\circ\,\mathrm{id}_{E(Y)}\otimes a_{\overline{X}}\otimes \mathrm{id}_{E(X )}\,\circ\,
  E((\mathrm{id}_Y\otimes t^{\bullet *}\,\circ\,\overline{r}_Y)\otimes \mathrm{id}_X) \\
&=& E(\mathrm{id}_Y\otimes r_X^* )\,\circ\,\mathrm{id}_{E(Y)}\otimes (a_{\overline{X}}\circ E(t^{\bullet *}))
   \otimes \mathrm{id}_{E(X )}\,\circ\,E(\overline{r}_{Y}\otimes \mathrm{id}_X) \\
&=& E(\mathrm{id}_{Y}\otimes r_X^* )\,\circ\,\mathrm{id}_{E(Y )}\otimes (E(t^{\bullet *})\circ a_{\overline{Y}})
   \otimes \mathrm{id}_{E(X )} \,\circ\,E(\overline{r}_Y\otimes \mathrm{id}_X) \\
&=& E(\mathrm{id}_Y\otimes (r_{X}^*\,\circ\,t^{\bullet *}\otimes \mathrm{id}_X ))
  \,\circ\,\mathrm{id}_{E(Y )}\otimes a_{\overline{Y}}\otimes \mathrm{id}_{E(X )}
  \,\circ\,E(\overline{r}_Y\otimes \mathrm{id}_X) \\
&=& E(\mathrm{id}_Y\otimes (r_Y^*\,\circ\,\mathrm{id}_{\overline{Y}}\otimes t))
  \,\circ\,\mathrm{id}_{E(Y )}\otimes a_{\overline{Y}}\otimes \mathrm{id}_{E(X )}
  \,\circ\,E(\overline{r}_Y\otimes \mathrm{id}_X) \\
&=& E(\mathrm{id}_Y\otimes r_Y^* )\,\circ\,\mathrm{id}_{E(Y )}\otimes
  a_{\overline{Y}}\otimes E(t)\,\circ\,E(\overline{r}_Y \otimes \mathrm{id}_Y ) \\
&=& S (a)_Y \,\circ\,E(t),
\end{aligned}$$ as desired.

Clearly, we have $S(a)\in A$ for all $a\in A$ and it is also clear that the map $S$ is linear. We must prove the two identities $$m(\iota\otimes S)((a\otimes 1)\Delta(b))=\varepsilon (b)a,\ \ \ \ \ \ \ 
m(S\otimes\iota )((1\otimes a)\Delta(b))=\varepsilon (b)a,$$ for all $a,b\in A$. We prove only the first one. Thus let $a,b\in A$ and write $(a\otimes 1)\Delta(b)=\sum_k a^k\otimes b^k$ for some $a^k, b^k\in A$. This means that $$(a_X\otimes 1_Y )\,\circ\,b_{X\otimes Y}=\sum_k a^k_X \otimes b^k_Y$$ for all objects $X$ and $Y$ of ${\cal C}$. Thus we get $$\begin{aligned}
 \lefteqn{
  m (\iota\otimes S)((a\otimes 1)\Delta(b))_X  \ \  =\ \  \sum_k m(a^k\otimes S(b^k ))_X \ \ 
  =\ \ \sum_k a^k_X\,\circ\,S(b^k )_X } \\
&& =\sum_k a^k_X\,\circ\,E(\mathrm{id}_X\otimes r^*_X )\,\circ\,\mathrm{id}_X\otimes b^k_{\overline{X}}\otimes\mathrm{id}_{E(X)}
  \,\circ\,E(\overline{r}_X\otimes\mathrm{id}_X ) \\
&&=E(\mathrm{id}_X\otimes r^*_X )\,\circ\,(\sum_k a^k_X\otimes b^k_{\overline{X}} )\otimes \mathrm{id}_{E(X)}
  \,\circ\,E(\overline{r}_X\otimes \mathrm{id}_X ) \\
&& =E(\mathrm{id}_X\otimes r^*_X )\,\circ\,(a_X\otimes \mathrm{id}_{E(\overline{X})}\,\circ\,b_{X\otimes\overline{X}})
  \otimes\mathrm{id}_{E(X)}\,\circ\,E(\overline{r}_X\otimes \mathrm{id}_X ) \\
&& =a_X\,\circ\,E(\mathrm{id}_X\otimes r^*_X )\,\circ\,b_{X\otimes\overline{X}}
  \otimes\mathrm{id}_{E(X)}\,\circ\,E(\overline{r}_X\otimes \mathrm{id}_X ) \\
&& =a_X\,\circ\,E(\mathrm{id}_X\otimes r^*_X )\,\circ\,E(\overline{r}_X\otimes \mathrm{id}_X )b_{{\bf 1}} \quad=\quad
  a_X\,\circ\,E(\mathrm{id}_X\otimes r^*_X \,\circ\,\overline{r}_X\otimes \mathrm{id}_X )b_{{\bf 1}} \\
&& =a_X\,\circ\,E(\mathrm{id}_X )b_{{\bf 1}} \quad=\quad a_X b_{{\bf 1}} \quad=\quad a_X \varepsilon (b) \quad=\quad
(\varepsilon (b)a)_X
\end{aligned}$$ for all objects $X$ in ${\cal C}$, so $m(\iota\otimes S)((a\otimes 1)\Delta(b))=\varepsilon (b)a$ as natural transformations.

It remains to show that $S$ is invertible. We do that by showing $S(S(a)^* )=a^*$ for all $a\in A$. Now with $X\in{\cal C}$, we calculate $$\begin{gathered}
 S (S (a)^* )_X=E(\mathrm{id}_{X}\otimes r_{X}^* )\,\circ\,\mathrm{id}_{E(X )}
   \otimes S (a)^*_{\overline{X}}\otimes \mathrm{id}_{E(X )}
   \,\circ\,E(\overline{r}_{X}\otimes \mathrm{id}_{X} ) \\
 =E(\mathrm{id}_{X}\otimes r_{X}^* )\,\circ\,\mathrm{id}_{E(X )}\otimes
  [E(\mathrm{id}_{\overline{X}}\otimes \overline{r}_{X}^* )\,\circ\,
  \mathrm{id}_{E(\overline{X})}\otimes a_X \otimes \mathrm{id}_{E(\overline{X})}
  \,\circ\,E(r_{X}\otimes \mathrm{id}_{\overline{X}})]^*
  \otimes \mathrm{id}_{E(X )}\,\circ\,E(\overline{r}_{X}\otimes \mathrm{id}_{X}), 
\end{gathered}$$ where we used $(\overline{r}_{X}, r_{X},X )$ as a solution of the conjugate equations for $\overline{X}\in{\cal C}$. Thus $$\begin{aligned}
\lefteqn{ S (S (a)^* )_X } \\
&=& E(\mathrm{id}_{X}\otimes r_{X}^* )
 \,\circ\,\mathrm{id}_{E(X )}\otimes [E(r_{X}^*\otimes \mathrm{id}_{\overline{X}})
 \,\circ\,\mathrm{id}_{E(\overline{X} )}\otimes a_X^*
 \otimes \mathrm{id}_{E(\overline{X} )}
 \,\circ\,E(\mathrm{id}_{\overline{X}}\otimes \overline{r}_{X})]
 \otimes \mathrm{id}_{E(X )}\,\circ\,E(\overline{r}_{X}\otimes \mathrm{id}_{X}) \\
&=& E(\mathrm{id}_{X}\otimes r_{X}^*\,\circ\,\mathrm{id}_{X}\otimes r_{X}^*
 \otimes \mathrm{id}_{\overline{X}\otimes X})\,\circ\,\mathrm{id}_{E(X\otimes\overline{X})}
 \otimes a_X ^*\otimes \mathrm{id}_{E(\overline{X}\otimes X)}\,\circ\,
 E(\mathrm{id}_{X\otimes\overline{X}}\otimes \overline{r}_{X}\otimes \mathrm{id}_{X}
 \,\circ\,\overline{r}_{X}\otimes \mathrm{id}_{X}) \\
&=& E(\mathrm{id}_{X}\otimes r_{X}^*\otimes r_{X}^* )\,\circ\,
 \mathrm{id}_{E(X\otimes\overline{X} )}\otimes a_X^*\otimes 
 \mathrm{id}_{E(\overline{X}\otimes X )}\,\circ\,E(\overline{r}_{X}\otimes
 \overline{r}_{X}\otimes \mathrm{id}_{X}) \\
&=& E(\mathrm{id}_{X}\otimes r_{X}^*\otimes r_{X}^*\,\circ\,
 \overline{r}_{X}\otimes \mathrm{id}_{X\otimes\overline{X}\otimes X})
 \,\circ\,a_X^*\otimes \mathrm{id}_{E(\overline{X}\otimes X )}\,\circ\,
 E(\overline{r}_{X}\otimes \mathrm{id}_{X}) \\
&=& E((\mathrm{id}_{X}\otimes r_{X}^* )\,\circ\,(\overline{r}_{X}
 \otimes \mathrm{id}_{X})\otimes \mathrm{id}_{\overline{X}\otimes X}\,\circ\,\mathrm{id}_{X}
 \otimes r_{X}^* )\,\circ\,a_X^*\otimes 
 \mathrm{id}_{E(\overline{X }\otimes X )}\,\circ\,E(\overline{r}_{X}\otimes \mathrm{id}_{X}) \\
&=& E(\mathrm{id}_{X}\otimes r_{X}^* )\,\circ\,a_X^*\otimes 
 \mathrm{id}_{E(\overline{X}\otimes X )}\,\circ\,E(\overline{r}_{X}\otimes \mathrm{id}_{X})
 =a_X^*\,\circ\,E(\mathrm{id}_{X}\otimes r_{X }^*\,\circ\,\overline{r}_{X}
 \otimes \mathrm{id}_{X}) \\
&=& a_X^*\,\circ\,\mathrm{id}_{E(X )} \ =\ a_X^* \ = \ (a^* )_X.
\end{aligned}$$

After these preparatory computations, the following Main Result is essentially a restatement of Theorem [\[t-mon-equiv\]](#t-mon-equiv){reference-type="ref" reference="t-mon-equiv"} and Proposition [\[p-coinv\]](#p-coinv){reference-type="ref" reference="p-coinv"}.

::: thm
[]{#t-main-equiv label="t-main-equiv"} Let ${\cal C}$ be a semisimple tensor $*$-category with conjugates and $E:{\cal C}\rightarrow{\cal H}$ an embedding functor. Let $(A,\Delta)$ be the corresponding discrete aqg. Then the functor $F: {\cal C}\rightarrow\mathrm{Rep}_f(A,\Delta)$ defined by $$F(X)=(E(X),\pi_X), \quad \pi_X(a)=a_X \ \forall a\in A,\quad F(s)=E(s)$$ provides an equivalence of tensor $*$-categories such that $K\,\circ\,F= E$.
:::

::: rema
1\. In combination with Theorem [\[t-dualcor\]](#t-dualcor){reference-type="ref" reference="t-dualcor"} this gives Woronowicz' generalized Tannaka-Krein result. Woronowicz constructs $\mathrm{Corep}_f (\hat{A},\hat{\Delta})$ for a compact aqg $(\hat{A},\hat{\Delta})$ more directly and uses the universal corepresentation $U$ of $(A,\Delta)$ implicitly. In his proof Woronowicz constructs a compact matrix pseudogroup from a category with a generator. Our result is more general in that this assumption is redundant.

2\. In view of Theorem [\[t-dual-comod\]](#t-dual-comod){reference-type="ref" reference="t-dual-comod"}, an alternative reconstruction theorem for a concrete semisimple tensor $*$-category ${\cal C}$ with conjugates would be that $${\cal C} \stackrel{\otimes}{\cong}{\mathrm{Comod}}_f (\hat{A},\hat{\Delta}^{op}),$$ where $(\hat{A},\hat{\Delta}^{op})$ is a Hopf $*$-algebra with a positive invariant functional. We refer to [@ulb; @JS1] for similar constructions, where concrete non-semisimple tensor categories are shown to be equivalent to tensor categories of finite dimensional comodules over (infinite dimensional) Hopf algebras (with no $*$-operation).
:::

We now discuss how the aqg $(A,\Delta)$ depends on the choice of the embedding functor $E$. This discussion is only preliminary and will be taken up again in part II of this series. We need the following

::: defin
Let ${\cal C},{\cal D}$ be strict tensor categories and $E,E':{\cal C}\rightarrow{\cal D}$ be tensor functors (with structural isomorphisms $e, e', d_{X,Y}, d'_{X,Y}$). Then $E,E'$ are said to be isomorphic as tensor functors, $E\stackrel{\otimes}{\cong}E'$, if the diagram $$\label{e-nat}
\begin{diagram} E(X)\otimes E(Y) & \rTo^{u_X\otimes u_Y} & E'(X)\otimes E'(Y) \\
\dTo_{d_{X,Y}} & & \dTo^{d'_{X,Y}} \\
E(X\otimes Y) & \rTo_{u_{X\otimes Y}} & E'(X\otimes Y)
\end{diagram}$$ commutes for all $X,Y\in{\cal C}$, where $u: E\rightarrow E'$ is a natural transformation whose components $u_X: E(X)\rightarrow E'(X)$ are isomorphisms. A similar and obvious commutative diagram involves the structural isomorphisms $e,e'$. If ${\cal C},{\cal D}$ are tensor $*$-categories and $E,E'$ are $*$-preserving then all $u_X$ must be unitary.
:::

::: prop
Let ${\cal C}$ be a semisimple tensor $*$-category ${\cal C}$ with conjugates. Let $E,E': {\cal C}\rightarrow{\cal H}$ be embedding functors, and let $(A,\Delta), (A',\Delta')$ be the corresponding discrete aqg. An isomorphism $u: E\stackrel{\otimes}{\cong} E'$ gives rise to an isomorphism $\theta: (A,\Delta)\cong (A', \Delta')$ with $\pi'_X\theta=\pi_X$ for all $X\in{\cal C}$.
:::

*Proof. *Let $u: E\rightarrow E'$ be a unitary equivalence of tensor $*$-functors. Then $\theta :\mathrm{Nat}E\rightarrow\mathrm{Nat}E'$ given by $\theta (a)_X =u_Xa_Xu_X^*$ for $a\in\mathrm{Nat}E$ and $X\in{\cal C}$ restricts to a unital $*$-homomorphism from $A$ to $A'$. Suppressing as usual the natural transformations $d$ and $d'$, we clearly have $\Delta'(\theta (a))_{(X,Y)}=u_{X\otimes Y}a_{X\otimes Y}u_{X\otimes Y}^*$, whereas $(\theta\otimes\theta )\Delta(a)_{(X,Y)}=(u_X\otimes u_Y )a_{X\otimes Y}(u_X^*\otimes u_Y^* )$, for all $a\in\mathrm{Nat}E$ and $X,Y\in{\cal C}$. Since $u_{X\otimes Y}=u_X\otimes u_Y$, for all $X,Y\in{\cal C}$, we get $(\theta\otimes\theta )\Delta=\Delta'\theta$, and $(A,\Delta)\cong (A',\Delta' )$.

The following definition will be useful in our discussion of embedded symmetric tensor categories.

::: defin
[]{#d-intr label="d-intr"} Let ${\cal C},{\cal D}$ be tensor categories and $E: {\cal C}\rightarrow{\cal D}$ a tensor functor. Then the automorphism group $\mathrm{Aut}^\otimes E$ consists of the natural isomorphisms of $E$ for which the diagram ([\[e-nat\]](#e-nat){reference-type="ref" reference="e-nat"}) commutes (with $E'=E$), together with the obvious componentwise group structure. If ${\cal C}$ is a tensor $*$-category and $E$ is a $*$-preserving embedding functor then the intrinsic group $G_E$ is the subgroup of $\mathrm{Aut}^\otimes E$ where all $u_X$ are unitaries.
:::
