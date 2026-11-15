---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidiﬁcation"
section_id: sec-013-63-inner-products-and-adjoints
section_title: "Inner Products and Adjoints"
section_number: 6.3
pages: 56-58
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.985
doc_brief: "Higher Dimensional Algebra VII: Groupoidiﬁcation — Groupoidiﬁcation is a form of categoriﬁcation in which vector spaces are replaced by groupoids and linear operators are replaced by spans of"
---
[]{#innerprodandadjoint label="innerprodandadjoint"}

Now we prove our results about the inner product of groupoids over a fixed groupoid, and the adjoint of a span:

::: thm
[]{#innerprod_theorem label="innerprod_theorem"} Given a groupoid $X$, there is a unique inner product $\langle \cdot,\cdot \rangle$ on the vector space $L^2(X)$ such that $$\langle \utilde{\Phi},\utilde{\Psi} \rangle = |\langle \Phi,\Psi \rangle|$$ whenever $\Phi$ and $\Psi$ are square-integrable groupoids over $X$. With this inner product $L^2(X)$ is a real Hilbert space.
:::

::: proof
*Proof.* Uniqueness of the inner product follows from the formula, since every vector in $L^2(X)$ is a finite-linear combination of vectors $\utilde{\Psi}$ for square-integrable groupoids $\Psi$ over $X$. To show the inner product exists, suppose that $\Psi_i, \Phi_i$ are square-integrable groupoids over $X$ and $\alpha_i, \beta_i \in {\mathbb R}$ for $1 \le i \le n$. Then we need to check that $$\sum_{i}\alpha_i\utilde{\Psi}_i 
= \sum_{j}\beta_j \utilde{\Phi}_j = 0$$ implies $$\sum_{i,j} \alpha_i\beta_j \, 
 |\langle \Psi_i, \Phi_j \rangle | = 0.$$ The proof here closely resembles the proof of existence in Theorem [\[PROCESS1\]](#PROCESS1){reference-type="ref" reference="PROCESS1"}. We leave to the reader the task of checking that $L^2(X)$ is complete in the norm corresponding to this inner product. ◻
:::

::: proposition
[]{#innerprod_adjoint label="innerprod_adjoint"} Given a span $$\xymatrix{
& S \ar[dl]_{q} \ar[dr]^{p} & \\
Y & & X
}$$ and a pair $v \colon\Psi \rightarrow X$, $w \colon\Phi \rightarrow Y$ of groupoids over $X$ and $Y$, respectively, there is an equivalence of groupoids $$\langle \Phi,S\Psi \rangle \simeq \langle S^\dagger\Phi,\Psi \rangle.$$
:::

::: proof
*Proof.* We can consider the groupoids over $X$ and $Y$ as spans with one leg over the terminal groupoid $1$. Then the result follows from the equivalence given by associtativity in Lemma [\[associativity\]](#associativity){reference-type="ref" reference="associativity"} and Theorem [\[linops_equivspans1\]](#linops_equivspans1){reference-type="ref" reference="linops_equivspans1"}. Explicitly, $\langle \Phi,S\Psi \rangle$ is the composite of spans $S\Psi$ and $\Phi$, while $\langle S^\dagger\Phi,\Psi \rangle$ is the composite of spans $S^\dagger\Phi$ and $\Psi$. ◻
:::

::: proposition
[]{#adjoint_comp label="adjoint_comp"} Given spans $$\xymatrix{
  & T \ar[dl]_{q_T} \ar[dr]^{p_T}  & & & S \ar[dl]_{q_S} \ar[dr]^{p_S} &\\
 Z & & Y & Y & & X 
}$$ there is an equivalence of spans $$(ST)^\dagger \simeq T^\dagger S^\dagger.$$
:::

::: proof
*Proof.* This is clear by the definition of composition. ◻
:::

::: proposition
[]{#adjoint_add label="adjoint_add"} Given spans $$\xymatrix{
& S \ar[dl]_{q_S} \ar[dr]^{p_S} & & & T \ar[dl]_{q_T} \ar[dr]^{p_T} & \\
Y & & X & Y & & X
}$$ there is an equivalence of spans $$(S+T)^\dagger \simeq S^\dagger + T^\dagger.$$
:::

::: proof
*Proof.* This is clear since the addition of spans is given by coproduct of groupoids. This construction is symmetric with respect to swapping the legs of the span. ◻
:::

::: proposition
[]{#innerprodandadjointprops label="innerprodandadjointprops"} Given a groupoid $\Lambda$ and square-integrable groupoids $\Phi$, $\Psi$, and $\Psi'$ over $X$, we have the following equivalences of groupoids:

1.  $$\langle \Phi,\Psi \rangle \simeq \langle \Psi,\Phi \rangle.$$

2.  $$\langle \Phi,\Psi + \Psi' \rangle \simeq \langle \Phi,\Psi \rangle + \langle \Phi,\Psi' \rangle.$$

3.  $$\langle \Phi,\Lambda \times \Psi \rangle \simeq \Lambda \times \langle \Phi,\Psi \rangle.$$
:::

::: proof
*Proof.* Each part will follow easily from the definition of weak pullback. First we label the maps for the groupoids over $X$ as $v\colon\Phi\rightarrow X$, $w\colon\Psi\rightarrow X$, and $w' \colon\Psi' \rightarrow X$.

1.  $\langle \Phi,\Psi \rangle \simeq \langle \Psi,\Phi \rangle.$\
    By definition of weak pullback, an object of $\langle \Phi,\Psi \rangle$ is a triple $(a,b,\alpha)$ such that $a\in\Phi, b\in\Psi,$ and $\alpha\colon
    v(a)\rightarrow w(b)$. Similarly, an object of $\langle \Psi,\Phi \rangle$ is a triple $(b,a,\beta)$ such that $b\in\Psi, a\in\Phi,$ and $\beta\colon w(b) \rightarrow
    v(a)$. Since $\alpha$ is invertible, there is an evident equivalence of groupoids.

2.  $\langle \Phi,\Psi + \Psi' \rangle \simeq \langle \Phi,\Psi \rangle + \langle \Phi,\Psi' \rangle.$\
    Recall that in the category of groupoids, the coproduct is just the disjoint union over objects and morphisms. With this it is easy to see that the definition of weak pullback will 'split' over union.

3.  $\langle \Phi,\Lambda \times \Psi \rangle \simeq \Lambda \times \langle \Phi,\Psi \rangle.$\
    This follows from the associativity (up to isomorphism) of the cartesian product.

 ◻
:::

### Acknowledgements

We thank James Dolan, Todd Trimble, and the denizens of the $n$-Category Café, especially Urs Schreiber and Bruce Bartlett, for many helpful conversations. AH was supported by the National Science Foundation under Grant No. 0653646. CW was supported by an FQXi grant.
