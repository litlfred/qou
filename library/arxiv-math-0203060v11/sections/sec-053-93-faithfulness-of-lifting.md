---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-053-93-faithfulness-of-lifting
section_title: "Faithfulness of lifting"
section_number: 9.3
pages: 45-47
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.976
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
In this section we will show that the lifting procedure of nondegenerate fusion (braided, symmetric) categories is faithful, i.e. if two such categories over $k$ have equivalent liftings, then they are equivalent. We will also show that if two tensor functors from a nondegenerate fusion category over $k$ to another fusion category have isomorphic liftings, then they are isomorphic.

Let $R$ be a complete local ring, $\Bbb F$ the fraction field of $R$, $I\subset R$ the maximal ideal, and $k=R/I$ the residue field.

::: theorem
[]{#faithlif label="faithlif"} (i) Let ${\mathcal C}_1,{\mathcal C}_2$ be fusion categories defined over $R$, such that the fusion categories ${\mathcal C}_1/I$, ${\mathcal C}_2/I$ are nondegenerate, and the categories ${\mathcal C}_1\otimes_R\Bbb F,{\mathcal C}_2\otimes_R\Bbb F$ are tensor equivalent. Then ${\mathcal C}_1,{\mathcal C}_2$ (and hence ${\mathcal C}_1/I,{\mathcal C}_2/I$) are tensor equivalent.

\(ii\) The same statement is valid for braided and symmetric fusion categories.
:::

::: proof
*Proof.* (i) Pick a tensor equivalence $E: {\mathcal C}_1\otimes_R \Bbb F\to
{\mathcal C}_2\otimes_R\Bbb F$. Now pick an equivalence of ${\mathcal C}_1$, ${\mathcal C}_2$ as *additive* categories, which is the same as $E$ at the level of isomorphism classes of objects. By doing this, we may assume without loss of generality that ${\mathcal C}_1$ and ${\mathcal C}_2$ are really one category $({\mathcal C},\otimes)$ over $R$ with two different associativity isomorphisms $\Phi_1,\Phi_2$ and evaluation maps ${\rm ev}_1,{\rm ev}_2$ (the coevaluation maps of simple objects of both categories may be identified with any fixed collection of such maps by renormalization).

We know that there exists an invertible element $J$ of $C^2({\mathcal C})\otimes_R \Bbb F$ such that $(\Phi_1,{\rm ev}_1)^J=
(\Phi_2,{\rm ev}_2)$. (where ${}^J$ denotes the twisting by $J$). Our job is to show that such $J$ can be found in $C^2({\mathcal C})$, without localization to $\Bbb F$.

Consider the affine group scheme $T$ (defined over $R$) of all invertible elements of $C^2({\mathcal C})$. Let $T_0$ be the subscheme of $T$ consisting of "trivial" twists, i.e. those of the form $\Delta(x)(x^{-1}\otimes x^{-1})$, where $x$ is an invertible element of $C^1({\mathcal C})$ (i.e. the center of ${\mathcal C}$). It is clear that $T_0$ is central in $T$.

**Remark.** Since the algebra $C^2({\mathcal C})$ is a direct sum of matrix algebras (split over $R$), $T$ is a direct product of general linear groups.

Let $Z$ be the affine scheme of all invertible associators $\Phi$ and collections of evaluation morphisms ${\rm ev}$ satisfying (together with the fixed coevaluation morphisms) the axioms for a rigid tensor category (i.e. the pentagon relation, the unit object axiom, and the duality axioms). The group scheme $T$ acts on $Z$ by twisting (and then renormalizing the coevaluations to be the fixed ones): $(\Phi,{\rm ev})\to (\Phi,
{\rm ev})^J$. The restriction of this action to $T_0$ is trivial, so we get an action of $T/T_0$ on $Z$. Consider the regular mapping $\phi: T/T_0\to Z$, given by $J\to (\Phi_1,{\rm ev_1})^J$.

::: lemma
[]{#fin label="fin"} The mapping $\phi$ is finite.
:::

::: proof
*Proof.* By Nakayama's lemma, it is sufficient to check the finiteness of the reduction $\phi|_k$ of $\phi$ modulo $I$.

First of all, we have $H^2({\mathcal C}_1/I)=0$, which implies that the stabilizer of $(\Phi_1,{\rm ev}_1)$ in $T/T_0$ is a finite group. Thus the map $\phi|_k: T/T_0\to \phi|_k(T/T_0)$ is a finite covering.

It remains to show that $\phi|_k(T/T_0)$ is closed in $Z$. To do this, consider its closure $Z'$. Points of $Z'$ represent fusion categories over $k$, all of which are nondegenerate Indeed, the global dimension is a regular (in fact, locally constant) function on $Z$, and it is nonzero on ${\mathcal C}_1/I$, so it must be nonzero for all points of $Z'$. But for a nondegenerate fusion category ${\mathcal D}$ over $k$ we have $H^3({\mathcal D})=0$, which implies that the action of $T/T_0$ on $Z'$ is locally transitive. This means that $Z'$ is in fact a single orbit of $T/T_0$, i.e. $\phi|_k(T/T_0)$ is closed. The lemma is proved. ◻
:::

Thus we have a homomorphism $\phi^*: R[Z]\to R[T/T_0]$, which makes $R[T/T_0]$ into a finitely generated $R[Z]$-module.

Now let $J\in (T/T_0)(\Bbb F)$ be such that $(\Phi_1,{\rm ev}_1)^J=
(\Phi_2,{\rm ev}_2)$. Thus, $J$ can be regarded as a homomorphism $J: R[T/T_0]\to \Bbb F$. This homomorphism satisfies the condition $J(af)=\gamma(a)J(f)$, $f\in R[T/T_0]$, $a\in R[Z]$. where $\gamma: R[Z]\to R$ corresponds to the point $(\Phi_2,{\rm ev}_2)$. Now, by Lemma [\[fin\]](#fin){reference-type="ref" reference="fin"}, for any $f\in R[T/T_0]$ there exist $b_1,...,b_n\in R[Z]$ such that $f^n+b_1f^{n-1}+...+b_n=0$. But then $J(f)^n+\gamma(b_1)J(f)^{n-1}+...+\gamma(b_n)=0$. Now, since $\gamma(b_i)$ are integers, we see that $J(f)$ is an integer, so $J$ in fact belongs to $(T/T_0)(R)$. But it is easy to see that the map $T(R)\to (T/T_0)(R)$ is surjective. Hence, there exists $J\in T(R)$ such that $(\Phi_1,{\rm ev}_1)^J=(\Phi_2,{\rm ev}_2)$, as desired. The theorem is proved.

\(ii\) The proof is the same, since, as we showed, the integrality of $J\in T/T_0$ follows already from the equation $(\Phi_1,{\rm ev}_1)^J=(\Phi_2,{\rm ev}_2)$. ◻
:::

::: theorem
[]{#faithfun label="faithfun"} Let ${\mathcal C},{\mathcal C}'$ be fusion categories defined over $R$, such that the fusion category ${\mathcal C}/I$ is nondegenerate. Let $F_1,F_2: {\mathcal C}\to {\mathcal C}'$ be tensor functors, which become isomorphic after tensoring with $\Bbb F$. Then $F_1,F_2$ (and hence their reductions modulo $I$) are isomorphic.
:::

::: proof
*Proof.* The proof is analogous to the proof of Theorem [\[faithlif\]](#faithlif){reference-type="ref" reference="faithlif"}. As in Theorem [\[faithlif\]](#faithlif){reference-type="ref" reference="faithlif"}, we may assume that $F_1=F_2=F$ as additive functors, with two different tensor structures $J_1,J_2$. Let $G$ be the group scheme of invertible elements of $C^1_F({\mathcal C})$. Let $S$ be the scheme of tensor structures on $F$. The group scheme $G$ naturally acts on $S$ by "gauge transformations", $J\to J^g$. We know there exists $g\in G(\Bbb F)$ such that $J_1^g=J_2$, and need to show that this $g$ is in fact in $G(R)$.

Using the fact that $H^1_F({\mathcal C})=H^2_F({\mathcal C})=0$, one finds that the action map $\chi:G\to S$ given by $g\to J_1^g$ is finite. Now the proof that $g\in G(R)$ runs analogously to the proof that $J\in
(T/T_0)(R)$ in Theorem [\[faithlif\]](#faithlif){reference-type="ref" reference="faithlif"}. Theorem [\[faithfun\]](#faithfun){reference-type="ref" reference="faithfun"} is proved. ◻
:::

Now let $K$ be the algebraic closure of the field of quotients of $W(k)$.

::: corollary
[]{#faithlif1 label="faithlif1"} (i) If two nondegenerate fusion (braided, symmetric) categories over $k$ have equivalent liftings to $K$, then they are equivalent.

\(ii\) If two tensor functors between nondegenerate fusion categories over $k$ have isomorphic liftings to $K$, then they are isomorphic.
:::

::: proof
*Proof.* (i) follows easily from Theorem [\[faithlif\]](#faithlif){reference-type="ref" reference="faithlif"}, (ii) from Theorem [\[faithfun\]](#faithfun){reference-type="ref" reference="faithfun"}. ◻
:::

To give the next corollary, recall that in [@EG1] it was proved that a semisimple cosemisimple Hopf algebra over $k$ has a unique lifting to $K$. In fact, this is a special case of the lifting theory developed in this paper, since a semisimple cosemisimple Hopf algebra is nothing but a pair $({\mathcal C},F)$, where ${\mathcal C}$ is a nondegenerate fusion category over $k$, and $F$ a fiber functor on ${\mathcal C}$.

::: corollary
[]{#faithhopf label="faithhopf"} If two semisimple cosemisimple Hopf algebras over $k$ have isomorphic liftings to $K$ then they are isomorphic.
:::

::: proof
*Proof.* We can regard these two Hopf algebras as pairs $({\mathcal C}_1,F_1)$ and $({\mathcal C}_2,F_2)$. By theorem [\[faithlif1\]](#faithlif1){reference-type="ref" reference="faithlif1"}(i), we can assume that ${\mathcal C}_1={\mathcal C}_2$; then by theorem [\[faithlif1\]](#faithlif1){reference-type="ref" reference="faithlif1"}(ii), $F_1$ is isomorphic to $F_2$. The Corollary is proved. ◻
:::

The same theorem applies to quasitriangular, triangular Hopf algebras. The proof is parallel.

.1in

**Warning.** (Added in April 2017.) Unfortunately, the proof of Lemma [\[fin\]](#fin){reference-type="ref" reference="fin"} (and hence of the main results on faithfulness of the lifting given in this subsection) is incomplete; namely, the Nakayama lemma is not sufficient here, and one needs to use the fact that $T$ is a reductive group, see [@Et]. A complete proof of Lemma [\[fin\]](#fin){reference-type="ref" reference="fin"}, as well as alternative proofs of the results of this subsection are given in [@Et], Section 4. This paper also gives an affirmative answer to the question in Remark [\[nondq\]](#nondq){reference-type="ref" reference="nondq"} below.
