---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-058-191-summability-of-formal-solutions
section_title: "Summability of formal solutions"
section_number: 19.1
pages: 100-105
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.983
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:sommabilite label="subsection:sommabilite"}

Consider the equation [\[eqn:conjugaison\]](#eqn:conjugaison){reference-type="eqref" reference="eqn:conjugaison"} and keep the notation [\[eqn:formestandardtriangulaireentiere\]](#eqn:formestandardtriangulaireentiere){reference-type="eqref" reference="eqn:formestandardtriangulaireentiere"}. To each pair $(i,j)$ such that $i < j$, we associate a divisor $\Lambda_{i,j}$ with degree $\mu_j - \mu_i$; we assume that $\Lambda_{i+1,j} < \Lambda_{i,j} < \Lambda_{i,j+1}$, meaning that $\Lambda_{i,j} = \sum\limits_{\ell=i}^{j-1}\Lambda_{\ell,\ell+1}$. Put $\Lambda_j := \Lambda_{j-1,j}$ and $\Lambda := \sum\limits_{j=2}^{k}\Lambda_j$; then $\Lambda_{i,j} = \sum\limits_{\ell=i+1}^{j}\Lambda_j$ and $|\Lambda| = \mu_k - \mu_1$. By convention, we write $\Lambda_{i,i} = {\rm\bf O}$, the null divisor.

In order to establish the summability of the formal solution $\hat F$, we need a genericity condition on divisors.

::: defi
[]{#defi:compatible label="defi:compatible"} Let $A_{0}$ be as in [\[eqn:formestandarddiagonaleentiere\]](#eqn:formestandarddiagonaleentiere){reference-type="eqref" reference="eqn:formestandarddiagonaleentiere"} and let $\Lambda$ be a divisor of degree $\vert \Lambda\vert = \mu_k - \mu_1$. A partition $(\Lambda_1,\ldots,\Lambda_m)$ is called *compatible with $A_0$* if $m = k-1$ and if, for $i$ from $1$ to $(k-1)$, one has $\vert\Lambda_i\vert = \mu_{i+1} - \mu_i$ ; when this is the case, the partition is called *generic for $A_0$* if it moreover satisfies the following non-resonancy condition: $\Vert \Lambda_i \Vert \not\equiv \dfrac{\alpha_i}{\alpha_j} \pmod~ q^{\mathbf Z}$ for any eigenvalues $\alpha_i$ of $A_i$ and $\alpha_j$ of $A_j$, $j>i$.
:::

The following theorem makes more precise the result [@JSStokes Theorem 3.7]. Here, we prove that the *unique* meromorphic solution $F = F_{(\Lambda_1,\ldots,\Lambda_{k-1})}$, found by both methods, is *asymptotic to the unique formal solution $\hat F$*, in the sense of definition [\[defi:Lambda1Lambda\]](#defi:Lambda1Lambda){reference-type="ref" reference="defi:Lambda1Lambda"}). Moreover, its construction is different [@zh2] and uses the theorem of Borel-Ritt [\[theo:BorelRitt\]](#theo:BorelRitt){reference-type="ref" reference="theo:BorelRitt"}.\

::: tabular
p7cm c

::: rema
[]{#rema:dictionnary label="rema:dictionnary"} The two approaches can be compared with help of the following dictionary (see also subsection [\[subsection:algebraicsummation\]](#subsection:algebraicsummation){reference-type="ref" reference="subsection:algebraicsummation"}):
:::

&

  Here         [@JSStokes]
  ------------ -------------------
  partition    summation divisor
  compatible   adapted
  generic      allowed
:::

::: theo
[]{#theo:sommabilite label="theo:sommabilite"} Let $A \in {{\mathcal C}_{A_0}}$, let $\Lambda$ be a divisor and $(\Lambda_1,\ldots,\Lambda_{k-1})$ a generic partition of $\Lambda$ for $A_0$. For $i < j$, put $\Lambda_{i,j} := \sum\limits_{\ell=i}^{j-1} \Lambda_\ell$. Then the conjugacy equation $(\sigma_qF) A_0 = A F$ admits a unique solution $F = (F_{ij})$ in ${\mathfrak{G}}$ such that $F_{ij} \in {\text{Mat}}_{r_i,r_j}({\mathbb O}_{\Lambda_i,\ldots,\Lambda_{j-1}}^{\Lambda_{i,j}})$ for $i < j$
:::

::: proof
*Proof.* Take $A$ in the form [\[eqn:formestandardtriangulaireentiere\]](#eqn:formestandardtriangulaireentiere){reference-type="eqref" reference="eqn:formestandardtriangulaireentiere"}. The conjugacy equation [\[eqn:conjugaison\]](#eqn:conjugaison){reference-type="eqref" reference="eqn:conjugaison"} is equivalent to the following system; for$1 \leq i < j \leq k$: $$z^{\mu_j-\mu_i}(\sigma_qF_{ij})A_j =
A_i F_{ij} + z^{-\mu_i} \sum_{\ell=i+1}^j U_{i\ell} F_{\ell j}.$$ After J.P. Bézivin [@Bezivin], we know that the formal solution $\hat F_{ij}$ has $q$-Gevrey order $1/(\mu_j - \mu_{j-1})$ for $i < j$.

Let $1 < j \leq k$ and consider the formal solution $\hat F_{j-1,j}$ of equation: $$\label{eqn:Fj-1j}
z^{\mu_j-\mu_{j-1}}(\sigma_qY)~A_j = A_{j-1}~Y + z^{-\mu_{j-1}} U_{j-1,j}.$$ After the theorem of Borel-Ritt [\[theo:BorelRitt\]](#theo:BorelRitt){reference-type="ref" reference="theo:BorelRitt"}, there exists a function $\Phi_{j-1,j} \in {\mathbb A}_q^{\Lambda_{j-1}}$ with $\hat F_{j-1,j}$ as an asymptotic expansion at zero. Putting $Y = Z + \Phi_{j-1,j}$ in equation [\[eqn:Fj-1j\]](#eqn:Fj-1j){reference-type="eqref" reference="eqn:Fj-1j"}, one gets, from theorem [\[theo:Lambdaplate\]](#theo:Lambdaplate){reference-type="ref" reference="theo:Lambdaplate"}: $$z^{\mu_j-\mu_{j-1}}(\sigma_qY)~A_j = 
A_{j-1}~Y + \frac{H_{j-1,j}}{\theta_{\Lambda_{j-1}}}~,$$ where $H_{j-1,j}$ denotes a meromorphic function in a neighborhood of $z = 0$. Putting $Z := \dfrac{X}{\theta_{\Lambda_{j-1}}}$ one finds: $$\Vert\Lambda_{j-1}\Vert(\sigma_qX)~A_j = A_{j-1}~X + H_{j-1,j}~.$$ By the non-resonancy assumption, this yields a unique solution that is meromorphic at $z = 0$. It follows that the equation admits a unique solution in class ${\mathbb A}_q^{\Lambda_{j-1}}$ which is asymptotic to the series $\hat F_{j-1,j}$; the uniqueness is obvious. This solution will be written $F_{j-1,j}$.

Now consider the equation satisfied by $\hat F_{j-2,j}$: $$\label{eqn:Fj-2j}
z^{\mu_j-\mu_{j-2}}(\sigma_qY)~A_j =
A_{j-2}~Y + z^{-\mu_{j-2}}~\bigl(U_{j-2,j-1} F_{j-1,j} + U_{j-2,j}\bigr).$$ Choosing a function $\Phi_{j-2,j}$ in ${\mathbb A}_q^{\Lambda_{j-1}}$ with $\hat F_{j-2,j}$ as an asymptotic expansion, the change of unknown function $Y = \dfrac{Z+\Phi_{j-2,j}}{\theta_{\Lambda_{j-1}}}$ transforms [\[eqn:Fj-2j\]](#eqn:Fj-2j){reference-type="eqref" reference="eqn:Fj-2j"} into: $$\Vert\Lambda_{j-1}\Vert~z^{\mu_{j-1}-\mu_{j-2}}~(\sigma_qX)~A_j =
A_{j-2}~X+H_{j-2,j}~,$$ where $H_{j-2,j}$ is a function meromorphic at $z = 0$. We are thus led back to a similar situation as in equation [\[eqn:Fj-1j\]](#eqn:Fj-1j){reference-type="eqref" reference="eqn:Fj-1j"}, with $\mu_{j-1} - \mu_{j-2}$ instead of $\mu_j - \mu_{j-1}$. One thus gets a solution of [\[eqn:Fj-2j\]](#eqn:Fj-2j){reference-type="eqref" reference="eqn:Fj-2j"} in ${\mathbb O}_{\Lambda_{j-2},\Lambda_{j-1}}$ which is asymptotic to $\hat F_{j-2,j}$ along the divisors $(\Lambda_{j-2},\Lambda_{j-1}+\Lambda_{j-2})$. By considering the associated homogeneous equation, one checks that this solution is unique.

Iterating the process, one shows that there is a unique solution $F_{i,j}$ in ${\mathbb O}_{\Lambda_i,\ldots,\Lambda_{j-1}}^{\Lambda_{i,j}}$ which is asymptotic to the formal solution $\hat F_{ij}$ for all $i < j$. ◻
:::

Theorem [\[theo:sommabilite\]](#theo:sommabilite){reference-type="ref" reference="theo:sommabilite"} can be extended in the following way.

::: coro
[]{#coro:sommabilite label="coro:sommabilite"} Let $B_1, B_2 \in {\mathfrak{G}}({\mathbf C}\{z\})$ be such that $(A_0)^{-1}~B_i\in{\mathfrak{G}}({\mathbf C}\{z\})$, $i=1$, $2$, and consider the associated $q$-difference equation: $$\label{eqn:YB12}
(\sigma_q Y)~B_1 = B_2Y ~.$$ Then, for any given generic partition of divisors $(\Lambda_1,\ldots,\Lambda_{k-1})$ for $A_0$, there exists, in ${\mathfrak{G}}$, a unique matrix solution $Y:=(Y_{i,j})$ of [\[eqn:YB12\]](#eqn:YB12){reference-type="eqref" reference="eqn:YB12"} and such that, for each pair $i < j$ of indices, $Y_{i,j} \in {\text{Mat}}_{r_i,r_j}({\mathbb O}_{\Lambda_i,\ldots,\Lambda_{j-1}}^{\Lambda_{i,j}})$.
:::

::: proof
*Proof.* Recall that [\[eqn:YB12\]](#eqn:YB12){reference-type="eqref" reference="eqn:YB12"} is analytically conjugated to an equation of form [\[eqn:conjugaison\]](#eqn:conjugaison){reference-type="eqref" reference="eqn:conjugaison"}; see section [\[section:analyticisoformalclassification\]](#section:analyticisoformalclassification){reference-type="ref" reference="section:analyticisoformalclassification"}. The result follows from proposition [\[prop:OOmodule\]](#prop:OOmodule){reference-type="ref" reference="prop:OOmodule"} and the fact that ${\mathbb O}_{\Lambda_i,\ldots,\Lambda_{j-1}}^{\Lambda_{i,j}} \subset
{\mathbb O}_{\Lambda_i,\ldots,\Lambda_{j}}^{\Lambda_{i,j+1}})$ for all $i < j$. ◻
:::

An obvious consequence of theorem [\[theo:sommabilite\]](#theo:sommabilite){reference-type="ref" reference="theo:sommabilite"} and corollary [\[coro:sommabilite\]](#coro:sommabilite){reference-type="ref" reference="coro:sommabilite"} is the following.

::: theo
[]{#theo:solutionsasymptotiques label="theo:solutionsasymptotiques"} The functions $F = (F_{i,j})$ and $Y = (Y_{i,j})$ respectively considered in theorem [\[theo:sommabilite\]](#theo:sommabilite){reference-type="ref" reference="theo:sommabilite"} and corollary [\[coro:sommabilite\]](#coro:sommabilite){reference-type="ref" reference="coro:sommabilite"} both admit an asymptotic expansion in the following sense: for all pairs $(i,j)$ with $i < j$, the blocks $F_{i,j}$ and $Y_{i,j}$ have an asymptotic expansion at $0$ along divisors $(\Lambda_j,\Lambda_{i,j})$, according to definition [\[defi:Lambda1Lambda\]](#defi:Lambda1Lambda){reference-type="ref" reference="defi:Lambda1Lambda"}.
:::

::: proof
*Proof.* Immediate, with help of theorem [\[theo:masymptotique\]](#theo:masymptotique){reference-type="ref" reference="theo:masymptotique"}. ◻
:::

### Stokes phenomenon and analytic classification {#subsection:Stokes}

[]{#not81 label="not81"} Write $F^A_{(\Lambda_1,\ldots,\Lambda_{k-1})}$ the solution of [\[eqn:conjugaison\]](#eqn:conjugaison){reference-type="eqref" reference="eqn:conjugaison"} obtained in theorem [\[theo:sommabilite\]](#theo:sommabilite){reference-type="ref" reference="theo:sommabilite"}, which can be seen as a sum of the formal solution $\hat F$ with respect to generic partition $(\Lambda_1,\ldots,\Lambda_{k-1})$. One thereby deduces a summation process of $\hat F$ with respect to each generic partition of divisors for $A_0$; we shall denote: $${{{\mathcal{F}}}}^A: (\Lambda_1,\ldots,\Lambda_{k-1})
\mapsto F^A_{(\Lambda_1,\ldots,\Lambda_{k-1})}.$$ The $q$-analogue of Stokes phenomenon is displayed by the existence of various \"sums\" of $\hat F$.

::: prop
[]{#prop:AA0 label="prop:AA0"} In theorem [\[theo:sommabilite\]](#theo:sommabilite){reference-type="ref" reference="theo:sommabilite"}, one has $A = A_0$ if, and only if, the map ${{{\mathcal{F}}}}^A$ is constant on the set of generic partitions of divisors for $A_0$.
:::

::: proof
*Proof.* If $A = A_0$, the formal solution boils down to the identity matrix, which plainly coincides with $F^A_{(\Lambda_1,\ldots,\Lambda_{k-1})}$ for any compatible partition $(\Lambda_1,\ldots,\Lambda_{k-1})$.

On the other hand, if $A \not= A_0$, the polynomial $U_{i,j}$ in [\[eqn:formestandardtriangulaireentiere\]](#eqn:formestandardtriangulaireentiere){reference-type="eqref" reference="eqn:formestandardtriangulaireentiere"} are not all $0$. To begin with, assume that $U_{j-1,j} \not= 0$ for some index $j$. Since $\hat F_{j-1,j}$ diverges, its sum along divisor $\Lambda_j$ will be distinct from its sum along any different divisor. More generally, when $U_{i,j} \not= 0$, the solution $F^A_{(\Lambda_1,\ldots,\Lambda_{k-1})}$ will depend in a one-to-one way on divisor $\Lambda_j$; details are left to the reader. ◻
:::

[]{#not82 label="not82"} For any $\lambda\in{\mathbf C}^*$, let $[\lambda;q:{A_0}]$ be the ordered partition of divisors generated by the spiral $[\lambda;q]$ in the following way: $$[\lambda;q:{A_0}] :=
\bigl((\mu_2-\mu_1)[\lambda;q],(\mu_3-\mu_2)[\lambda;q],\ldots,
(\mu_k-\mu_{k-1})[\lambda;q]\bigr)~,$$ where $\mu_j$ are as in [\[eqn:formestandarddiagonaleentiere\]](#eqn:formestandarddiagonaleentiere){reference-type="eqref" reference="eqn:formestandarddiagonaleentiere"}, *i.e.* $A_0 = \text{diag}\left(z^{\mu_1} A_1,\ldots,z^{\mu_k} A_k\right)$.

If $[\lambda;q:{A_0}]$ is generic with respect to $A_0$, we will write $\lambda \in \{A_0\}$ and say that *$\lambda$ is generic for $A_0$*.

::: theo
[]{#theo:Stokes label="theo:Stokes"} Fix some $\lambda_0 \in \{A_0\}$ and for any $\lambda \in \{A_0\}$ and $A \in {{\mathcal C}_{A_0}}$, set: $$\label{not83}
\text{St}_{\lambda_0}(\lambda;A) := 
\bigl(F_{[\lambda_0;q:{A_0}]}^A\bigr)^{-1}~F_{[\lambda;q:{A_0}]}^A~.$$ The following conditions are equivalent.

1.  There exists $\lambda \in \{A_0\}$ such that $[\lambda;q] \neq [\lambda_0;q]$ but $\text{St}_{\lambda_0}(\lambda;A) = Id$.

2.  For all $\lambda \in \{A_0\}$, the equality $\text{St}_{\lambda_0}(\lambda;A)=Id$ holds.

3.  One has $A=A_0$.
:::

::: proof
*Proof.* It follows immediately from proposition [\[prop:AA0\]](#prop:AA0){reference-type="ref" reference="prop:AA0"} ◻
:::

In the previous theorem, each $\text{St}_{\lambda_0}(\lambda;A)$ represents an upper-triangular unipotent matrix-valued function that is analytic in some disk $0 < \left |z \right |< R$ except at spirals $[\lambda;q]$ and $[\lambda_0;q]$; moreover, it is infinitely close to the identity matrix as $z \to 0$. If $Y := \text{St}_{\lambda_0}(\lambda;A) - I_{n}$, then $Y$ is flat at zero and satifies the relation: $$(\sigma_q Y)~A_0 = A_0~Y.$$

Theorem [\[theo:Stokes\]](#theo:Stokes){reference-type="ref" reference="theo:Stokes"} implies that each matrix $A$ chosen within the isoformal class ${{\mathcal C}_{A_0}}$ reduces to the normal form $A_0$ whenever the Stokes matrix $\text{St}_{\lambda_0}(\lambda;A)$ becomes trivial for some couple of generic parameters $\lambda_0$, $\lambda$ such that $\lambda\not=\lambda_0 \bmod q^{\mathbf Z}$.\
We shall now show that for any given pair of generic parameters $\lambda_0$, $\lambda$ that are not $q$-congruent, the data $\{\text{St}_{\lambda_0}(\lambda;A), A_0\}$ constitutes a complete set of analytical invariants associated to the $q$-difference module determined by $A$.\
Indeed, the notation $\text{St}_{\lambda_0}(\lambda;A)$ introduced for any $A \in {{\mathcal C}_{A_0}}$ can be naturally generalized for any matrix $B \in {\mathfrak{G}}({\mathbf C}\{z\})$ that belongs to the same formal class as $A_0$. To simplify, assume that $(A_0)^{-1}B \in {\mathfrak{G}}({{\mathbf C}\{z\}})$; this is for instance the case if $B$ is taken in Birkhoff-Guenther normal form (definition [\[defi:BirkhoffGuenthernormalform\]](#defi:BirkhoffGuenthernormalform){reference-type="ref" reference="defi:BirkhoffGuenthernormalform"}). From corollary [\[coro:sommabilite\]](#coro:sommabilite){reference-type="ref" reference="coro:sommabilite"} it follows that the corresponding conjugacy equation: $$(\sigma_q Y)~B = A_0~Y$$ admits, in ${\mathfrak{G}}$, a unique solution in the space of multi-summable functions associated to any given generic ordered partition of divisors $[\lambda;q:A_0]$. Thus, we are led to the notations ${{{\mathcal{F}}}}^B_{[\lambda;q:A_0]}$ and $\text{St}_{\lambda_0}(\lambda;B)$ as in the case of $A \in {{\mathcal C}_{A_0}}$.

::: coro
[]{#coro:Stokes label="coro:Stokes"} Suppose that $B_1$ and $B_2$ are two matrices such that $(A_0)^{-1}B_i \in {\mathfrak{G}}({{\mathbf C}\{z\}})$. Then the following assertions are equivalent.

1.  There exists $(\lambda_0,\lambda) \in \{A_0\}\times\{A_0\}$ such that $[\lambda;q] \neq [\lambda_0;q]$ but $\text{St}_{\lambda_0}(\lambda;B_1) = \text{St}_{\lambda_0}(\lambda;B_2)$.

2.  The equality $\text{St}_{\lambda_0}(\lambda;B_1) =
    \text{St}_{\lambda_0}(\lambda;B_2)$ holds for all $\lambda_0$, $\lambda\in \{A_0\}$.

3.  The matrices $B_1$ and $B_2$ give rise to analytically equivalent $q$-difference modules.
:::

::: proof
*Proof.* The only point to prove is that (1) implies (3). To do that, notice that from (1) we obtain the equality $${{{\mathcal{F}}}}^{B_2}_{[\lambda_0;q:A_0]}~\bigl({{{\mathcal{F}}}}^{B_1}_{[\lambda_0;q:A_0]}\bigr)^{-1} =
{{{\mathcal{F}}}}^{B_2}_{[\lambda;q:A_0]}~\bigl({{{\mathcal{F}}}}^{B_1}_{[\lambda;q:A_0]}\bigr)^{-1}~,$$ in which the left hand side and the right hand side are both solution to the same equation [\[eqn:YB12\]](#eqn:YB12){reference-type="eqref" reference="eqn:YB12"}. Since these solutions are analytical in some disk $0 < \left |z \right |< R$ except maybe respectively on the $q$-spiral $[\lambda_0;q]$ or $[\lambda;q]$ and that they have the same asymptotic expansion at zero, they must be analytic at $z=0$ and we arrive at assertion (3). ◻
:::

# Geometry of the space of classes {#chapter:geometryofF(M)}

In this chapter we describe to some extent the geometry of the space ${\mathcal{F}}(M_{0})$ of analytic isoformal classes in the formal class $M_{0}$. In subsection [\[subsection:BGNF\]](#subsection:BGNF){reference-type="ref" reference="subsection:BGNF"}, we already used the Birkhoff-Guenther normal form to find coordinates on ${\mathcal{F}}(M_{0})$. Here, we rather use the identification of ${\mathcal{F}}(M_{0})$ with $H^{1}({\mathbf{E}_{q}},\Lambda_I(M_0))$ proved in theorem [\[theo:secondqMalgrangeSibuya\]](#theo:secondqMalgrangeSibuya){reference-type="ref" reference="theo:secondqMalgrangeSibuya"} and completed in section [\[section:analyticclassificationCZ\]](#section:analyticclassificationCZ){reference-type="ref" reference="section:analyticclassificationCZ"}. The description given here will be further pursued in a separate work [@JSmoduli].
