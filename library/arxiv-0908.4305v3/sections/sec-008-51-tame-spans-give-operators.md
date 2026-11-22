---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidiﬁcation"
section_id: sec-008-51-tame-spans-give-operators
section_title: "Tame Spans Give Operators"
section_number: 5.1
pages: 45-50
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.996
doc_brief: "Higher Dimensional Algebra VII: Groupoidiﬁcation — Groupoidiﬁcation is a form of categoriﬁcation in which vector spaces are replaced by groupoids and linear operators are replaced by spans of"
---
To prove that a tame span gives a well-defined operator, we begin with three lemmas that are of some interest in themselves. We postpone to Appendix [\[appendix\]](#appendix){reference-type="ref" reference="appendix"} some well-known facts about groupoids that do not involve the concept of degroupoidification. This Appendix also recalls the familiar concept of 'equivalence' of groupoids, which serves as a basis for this:

::: definition
Two groupoids over a fixed groupoid $X$, say $v \colon\Psi \rightarrow X$ and $w \colon\Phi \rightarrow X$, are **equivalent** as groupoids over $X$ if there is an equivalence $F \colon\Psi \rightarrow\Phi$ such that this diagram $$\xymatrix{
\Psi \ar[rr]^{F} \ar[dr]_{p} && \Phi \ar[dl]^{q} \\
&X&
}$$ commutes up to natural isomorphism.
:::

::: lemma
[]{#vectorswelldefined label="vectorswelldefined"} Let $v \colon\Psi \rightarrow X$ and $w \colon\Phi \rightarrow X$ be equivalent groupoids over $X$. If either one is tame, then both are tame, and $\utilde{\Psi} = \utilde{\Phi}$.
:::

::: proof
*Proof.* This follows directly from Lemmas [\[EQUIVGRPD\]](#EQUIVGRPD){reference-type="ref" reference="EQUIVGRPD"} and [\[ESSENTIALPULLBACK\]](#ESSENTIALPULLBACK){reference-type="ref" reference="ESSENTIALPULLBACK"} in Appendix [\[appendix\]](#appendix){reference-type="ref" reference="appendix"}. ◻
:::

::: lemma
[]{#addvectors label="addvectors"} Given tame groupoids $\Phi$ and $\Psi$ over $X$, $$\utilde{\Phi + \Psi} = \utilde{\Phi} + \utilde{\Psi}.$$ More generally, given any collection of tame groupoids $\Psi_i$ over $X$, the coproduct $\sum_i \Psi_i$ is naturally a groupoid over $X$, and if it is tame, then $$\utilde{\sum_i \Psi_i} = \sum_i \utilde{\Psi}_i$$ where the sum on the right hand side converges pointwise as a function on $\underline{X}$.
:::

::: proof
*Proof.* The full inverse image of any object $x \in X$ in the coproduct $\sum_i \Psi_i$ is the coproduct of its fulll inverse images in each groupoid $\Psi_i$. Since groupoid cardinality is additive under coproduct, the result follows. ◻
:::

::: lemma
[]{#linearity label="linearity"} Given a span of groupoids $$\xymatrix{
& S\ar[dl]_{q} \ar[dr]^{p} & \\
Y & & X
}$$ we have

1.  $S(\sum_i \Psi_i)\simeq \sum_i S\Psi_i$

2.  $S(\Lambda\times \Psi)\simeq \Lambda\times S\Psi$

whenever $v_i \colon\Psi_i \rightarrow X$ are groupoids over $X$, $v \colon\Psi \rightarrow X$ is a groupoid over $X$, and $\Lambda$ is a groupoid.
:::

::: proof
*Proof.* To prove 1, we need to describe a functor $$F\colon\sum_i S \Psi_i \rightarrow S(\sum_i \Psi_i)$$ that will provide our equivalence. For this, we simply need to describe for each $i$ a functor $F_i \colon S \Psi_i \rightarrow S(\sum_i
\Psi_i)$. An object in $S \Psi_i$ is a triple $(s,z,\alpha)$ where $s
\in S$, $z \in \Psi_i$ and $\alpha \colon p(s) \rightarrow v_i(z)$. $F_i$ simply sends this triple to the same triple regarded as an object of $S(\sum_i \Psi_i)$. One can check that $F$ extends to a functor and that this functor extends to an equivalence of groupoids over $S$.

To prove 2, we need to describe a functor $F \colon S(\Lambda\times
\Phi) \rightarrow\Lambda\times S\Phi$. This functor simply re-orders the entries in the quadruples which define the objects in each groupoid. One can check that this functor extends to an equivalence of groupoids over $X$. ◻
:::

Finally we need the following lemma, which simplifies the computation of groupoid cardinality:

::: lemma
[]{#ALTCARD label="ALTCARD"} If $X$ is a tame groupoid with finitely many objects in each isomorphism class, then $$|X| 
= \sum_{x \in X} \frac{1}{|{\rm Mor}(x,-)|}$$ where ${\rm Mor}(x,-) = \bigcup_{y\in X}{\rm hom}(x,y)$ is the set of morphisms whose source is the object $x \in X$.
:::

::: proof
*Proof.* We check the following equalities: $$\sum_{[x] \in \underline{X}} \frac{1}{|{\rm Aut}(x)|} 
= \sum_{[x] \in \underline{X}} \frac{|[x]|}{|{\rm Mor}(x,-)|} 
= \sum_{x \in X} \frac{1}{|{\rm Mor}(x,-)|} .$$ Here $[x]$ is the set of objects isomorphic to $x$, and $|[x]|$ is the ordinary cardinality of this set. To check the above equations, we first choose an isomorphism $\gamma_y \colon x \rightarrow y$ for each object $y$ isomorphic to $x$. This gives a bijection from $[x] \times 
{\rm Aut}(x)$ to ${\rm Mor}(x,-)$ that takes $(y, f \colon x \rightarrow x)$ to $\gamma_y f \colon x \rightarrow y$. Thus $$|[x]| \, |{\rm Aut}(x)| = |{\rm Mor}(x,-)| ,$$ and the first equality follows. We also get a bijection between ${\rm Mor}(y,-)$ and ${\rm Mor}(x,-)$ that takes $f \colon y \rightarrow z$ to $f\gamma_y \colon x \rightarrow z$. Thus, $|{\rm Mor}(y,-)| = |{\rm Mor}(x,-)|$ whenever $y$ is isomorphic to $x$. The second equation follows from this. ◻
:::

Now we are ready to prove the main theorem of this section:

::: thm
[]{#PROCESS1 label="PROCESS1"} Given a tame span of groupoids $$\xymatrix{
& S \ar[dl]_{q} \ar[dr]^{p} & \\
Y && X
}$$ there exists a unique linear operator $\utilde{S} \colon{\mathbb R}^{\underline{X}} \rightarrow{\mathbb R}^{\underline{Y}}$ such that $\utilde{S}\utilde{\Psi} = \utilde{S\Psi}$ for any vector $\utilde{\Psi}$ obtained from a tame groupoid $\Psi$ over $X$.
:::

::: proof
*Proof.* It is easy to see that these conditions uniquely determine $\utilde{S}$. Suppose $\psi \colon\underline{X} \rightarrow{\mathbb R}$ is any nonnegative function. Then we can find a groupoid $\Psi$ over $X$ such that $\utilde{\Psi} = \psi$. So, $\utilde{S}$ is determined on nonnegative functions by the condition that $\utilde{S}\utilde{\Psi} = \utilde{S\Psi}$. Since every function is a difference of two nonnegative functions and $\utilde{S}$ is linear, this uniquely determines $\utilde{S}$.

The real work is proving that $\utilde{S}$ is well-defined. For this, assume we have a collection $\lbrace v_i \colon\Psi_i \rightarrow X
\rbrace_{i\in I}$ of groupoids over $X$ and real numbers $\lbrace
\alpha_i \in {\mathbb R}\rbrace_{i\in I}$ such that $$\label{assumption1}
 \sum_i \alpha_i \, \utilde{\Psi_i} = 0.$$ We need to show that $$\label{fact0}
 \sum_i\alpha_i \, \utilde{S\Psi_i} = 0.$$

We can simplify our task as follows. First, recall that a **skeletal** groupoid is one where isomorphic objects are equal. Every groupoid is equivalent to a skeletal one. Thanks to Lemmas [\[vectorswelldefined\]](#vectorswelldefined){reference-type="ref" reference="vectorswelldefined"} and [\[skeletal\]](#skeletal){reference-type="ref" reference="skeletal"}, we may therefore assume without loss of generality that $S$, $X$, $Y$ and all the groupoids $\Psi_i$ are skeletal.

Second, recall that a skeletal groupoid is a coproduct of groupoids with one object. By Lemma [\[addvectors\]](#addvectors){reference-type="ref" reference="addvectors"}, degroupoidification converts coproducts of groupoids over $X$ into sums of vectors. Also, by Lemma [\[linearity\]](#linearity){reference-type="ref" reference="linearity"}, the operation of taking weak pullback distributes over coproduct. As a result, we may assume without loss of generality that each groupoid $\Psi_i$ has one object. Write $\ast_i$ for the one object of $\Psi_i$.

With these simplifying assumptions, Equation [\[assumption1\]](#assumption1){reference-type="ref" reference="assumption1"} says that for any $x \in X$, $$\label{assumption2}
 0  =  \displaystyle{\sum_{i \in I} \alpha_i \, \utilde{\Psi_i}([x])} 
    =  \displaystyle{\sum_{i \in I} \alpha_i \, |v_i^{-1} (x)|}   
    = \displaystyle{\sum_{i \in J} \frac{\alpha_i}{|{\rm Aut}(\ast_i)|}}$$ where $J$ is the collection of $i \in I$ such that $v_i(\ast_i)$ is isomorphic to $x$. Since all groupoids in sight are now skeletal, this condition implies $v_i(\ast_i) = x$.

Now, to prove Equation [\[fact0\]](#fact0){reference-type="ref" reference="fact0"}, we need to show that $$\sum_{i \in I} \alpha_i \, \utilde{S\Psi_i}([y]) = 0$$ for any $y \in Y$. But since the set $I$ is partitioned into sets $J$, one for each $x \in X$, it suffices to show $$\label{fact1}
\sum_{i \in J} \alpha_i \, \utilde{S\Psi_i}([y]) = 0 .$$ for any fixed $x \in X$ and $y \in Y$.

To compute $\utilde{S\Psi_i}$, we need to take this weak pullback: $$\xymatrix{
& & S\Psi_i \ar[dl]_{\pi_S}\ar[dr]^{\pi_{\Psi_i}} & \\
& S \ar[dl]_{q} \ar[dr]^{p} & & \Psi_i \ar[dl]_{v_i} \\
Y & & X &  
}$$ We then have $$\label{formula1}
    \utilde{S \Psi_i}([y]) = |(q \pi_S)^{-1}(y)| ,$$ so to prove Equation [\[fact1\]](#fact1){reference-type="ref" reference="fact1"} it suffices to show $$\label{fact2}
\sum_{i \in J} \alpha_i \, |(q \pi_S)^{-1}(y)| = 0 .$$

Using the definition of 'weak pullback', and taking advantage of the fact that $\Psi_i$ has just one object, which maps down to $x$, we can see that an object of $S \Psi_i$ consists of an object $s \in S$ with $p(s) = x$ together with an isomorphism $\alpha \colon x \rightarrow x$. This object of $S\Psi_i$ lies in $(q \pi_S)^{-1}(y)$ precisely when we also have $q(s) = y$.

So, we may briefly say that an object of $(q\pi_S)^{-1}(y)$ is a pair $(s, \alpha)$, where $s \in S$ has $p(s) = x$, $q(s) = y$, and $\alpha$ is an element of ${\rm Aut}(x)$. Since $S$ is skeletal, there is a morphism between two such pairs only if they have the same first entry. A morphism from $(s,\alpha)$ to $(s,\alpha')$ then consists of a morphism $f \in {\rm Aut}(s)$ and a morphism $g \in {\rm Aut}(\ast_i)$ such that $$\xymatrix{
x \ar[r]^{\alpha}\ar[d]_{p(f)} & x\ar[d]^{v_i(g)} \\
x \ar[r]_{\alpha'} & x
}$$ commutes.

A morphism out of $(s,\alpha)$ thus consists of an arbitrary pair $f
\in {\rm Aut}(s)$, $g \in {\rm Aut}(\ast_i)$, since these determine the target $(s,\alpha')$. This fact and Lemma [\[ALTCARD\]](#ALTCARD){reference-type="ref" reference="ALTCARD"} allow us to compute: $$\label{formula2}
\begin{array}{ccl}
\nonumber |(q\pi_S)^{-1}(y)| & = 
\displaystyle{ 
\sum_{(s,\alpha)\in (q\pi_S)^{-1}(y)}
\frac{1}{|{\rm Mor}((s,\alpha),-)|} 
}
\\
\\
& = 
\displaystyle{
\sum_{s \in p^{-1}(y) \cap q^{-1}(y)}
\frac{|{\rm Aut}(x)|}{|{\rm Aut}(s)||{\rm Aut}(\ast_i)|} \,.
} 
\end{array}$$ So, to prove Equation [\[fact2\]](#fact2){reference-type="ref" reference="fact2"}, it suffices to show $$\label{fact3}
\sum_{i \in J} \;\, \sum_{s \in p^{-1}(x) \cap q^{-1}(y) }
\frac{\alpha_i|{\rm Aut}(x)|}{|{\rm Aut}(s)||{\rm Aut}(\ast_i)|} = 0 \,.$$ But this easily follows from Equation [\[assumption2\]](#assumption2){reference-type="ref" reference="assumption2"}. So, the operator $\utilde{S}$ is well defined. ◻
:::

In Definition [\[EQUIVALENCE\]](#EQUIVALENCE){reference-type="ref" reference="EQUIVALENCE"} we recall the natural concept of 'equivalence' for spans of groupoids. The next theorem says that our process of turning spans of groupoids into linear operators sends equivalent spans to the same operator:

::: thm
[]{#linops_equivspans1 label="linops_equivspans1"} Given equivalent spans $$\xymatrix{
& S\ar[dl]_{q_S} \ar[dr]^{p_S} &  & & T\ar[dl]_{q_T} \ar[dr]^{p_T} &\\
Y & & X & Y & & X
}$$ the linear operators $\utilde{S}$ and $\utilde{T}$ are equal.
:::

::: proof
*Proof.* Since the spans are equivalent, there is a functor providing an equivalence of groupoids $F \colon S \rightarrow T$ along with a pair of natural isomorphisms $\alpha \colon p_S \Rightarrow p_TF$ and $\beta \colon q_S \Rightarrow q_TF$. Thus, the diagrams $$\xymatrix{
S \ar[dr] && \Phi \ar[dl] & & T \ar[dr] && \Phi \ar[dl] \\
& X & && & X &
}$$ are equivalent pointwise. It follows from Lemma [\[skeletal\]](#skeletal){reference-type="ref" reference="skeletal"} that the weak pullbacks $S\Psi$ and $T\Psi$ are equivalent groupoids with the equivalence given by a functor $\tilde{F} \colon S\Psi \rightarrow T\Psi$. From the universal property of weak pullbacks, along with $F$, we obtain a natural transformation $\gamma \colon F\pi_S \Rightarrow
\pi_T\tilde{F}$. We then have a triangle $$\def\objectstyle{\scriptstyle}
  \def\labelstyle{\scriptstyle}
   \xy
   (20,20)*+{S\Psi}="1";
   (-20,20)*+{T\Psi}="2";
   (10,0)*+{S}="3";
   (-10,0)*+{T}="4";
   (0,-20)*+{Y}="5";
        {\ar_{\tilde{F}} "1";"2"};
        {\ar^{\pi_S} "1";"3"};
        {\ar_{\pi_T} "2";"4"};
        {\ar^{q_S} "3";"5"};
        {\ar_{q_T} "4";"5"};
        {\ar_{F} "3";"4"};
        {\ar@{=>}_<<{\scriptstyle \gamma} (2,11); (-2,9)};
        {\ar@{=>}_<<{\scriptstyle \beta} (2,-9); (-2,-11)};

\endxy$$ where the composite of $\gamma$ and $\beta$ is $(q_T \cdot
\gamma)^{-1}\beta \colon q_S \pi_S \Rightarrow q_T\pi_T\tilde{F}$. Here $\cdot$ stands for whiskering: see Definition [\[whiskering\]](#whiskering){reference-type="ref" reference="whiskering"}.

We can now apply Lemma [\[ESSENTIALPULLBACK\]](#ESSENTIALPULLBACK){reference-type="ref" reference="ESSENTIALPULLBACK"}. Thus, for every $y \in
Y$, the full inverse images $(q_S\pi_S)^{-1}(y)$ and $(q_T\pi_T)^{-1}(y)$ are equivalent. It follows from Lemma [\[EQUIVGRPD\]](#EQUIVGRPD){reference-type="ref" reference="EQUIVGRPD"} that for each $y \in Y$, the groupoid cardinalities $|(q_S\pi_S)^{-1}(y)|$ and $|(q_T\pi_T)^{-1}(y)|$ are equal. Thus, the linear operators $\utilde{S}$ and $\utilde{T}$ are the same. ◻
:::
