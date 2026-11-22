---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-008-27-ocneanu-rigidity
section_title: "Ocneanu rigidity"
section_number: 2.7
pages: 9-10
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
toc_source: outline
text_source: latex
latex_prose_ratio: 0.736
latex_coverage_ratio: 0.947
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
The statement that a fusion category over a field of characteristic zero cannot be nontivially deformed is known as Ocneanu rigidity, because its formulation and proof for unitary categories was suggested (but not published) by Ocneanu. Later Blanchard and Wassermann ([@BWa; @Wa]) proposed an algebraic version of Ocneanu's argument, which proves the following result.

::: theorem
[]{#ocnrig label="ocnrig"} A fusion category does not admit nontrivial deformations. In particular, the number of such categories (up to equivalence) with a given Grothendieck ring (=fusion rules) is finite.
:::

::: remark
This theorem is proved in [@BWa; @Wa] under the assumption that $\dim({\mathcal C})\ne 0$, but as we know from Theorem [\[posi\]](#posi){reference-type="ref" reference="posi"}, this assumption is superfluous in zero characteristic.
:::

In fact, one has the following somewhat more general theorem.

::: theorem
[]{#multocnrig label="multocnrig"} Theorem [\[ocnrig\]](#ocnrig){reference-type="ref" reference="ocnrig"} is valid for multi-fusion categories.
:::

This theorem follows directly from Theorem [\[van\]](#van){reference-type="ref" reference="van"} for $i=3$ and $F=\text{Id}$ (this is, essentially, the proof of Ocneanu-Blanchard-Wassermann). A sketch of proof is given in Section 7.

Note that Theorem [\[multocnrig\]](#multocnrig){reference-type="ref" reference="multocnrig"} implies that any multi-fusion category is defined over an algebraic number field.

**Question.** Is any multi-fusion category defined over a cyclotomic field?

Note that the answer is yes for fusion categories coming from quantum groups at roots of unity, for the categories of [@TY], and for group-theoretical categories discussed in Section 8. Also, it follows from the results of subsection [\[cy\]](#cy){reference-type="ref" reference="cy"} that the global dimension of a fusion category belongs to a cyclotomic field.

We also have

::: theorem
[]{#ocnrigfun label="ocnrigfun"} A (unital) tensor functor between multi-fusion categories does not have nontrivial deformations. In particular, the number of such functors (up to equivalence) for fixed source and target categories is finite.
:::

::: remark
In particular, Theorem [\[ocnrigfun\]](#ocnrigfun){reference-type="ref" reference="ocnrigfun"} implies that a given fusion category has finitely many fiber functors. This is also shown in [@IK] in the special case of categories coming from subfactors (see Theorem 2.4 in [@IK]).
:::

::: remark
Theorem [\[ocnrigfun\]](#ocnrigfun){reference-type="ref" reference="ocnrigfun"} also implies Ocneanu's result that a given fusion category has finitely many braidings. Indeed, any braiding in particular defines an equivalence of tensor categories between ${\mathcal C}$ and ${\mathcal C}^{op}$.
:::

The proof of Theorem [\[ocnrigfun\]](#ocnrigfun){reference-type="ref" reference="ocnrigfun"} is analogous to the proof of Theorem [\[multocnrig\]](#multocnrig){reference-type="ref" reference="multocnrig"}. Namely, the first part of the result follows directly from Theorem [\[van\]](#van){reference-type="ref" reference="van"} for $i=2$. The second part is a consequence of a combinatorial fact that there are only finitely many homomorphisms between the Grothendieck rings of the categories under consideration; this fact is a consequence of Proposition 2.1 of [@O] since the second Grothendieck ring can be considered as a based module over the first one.

::: remark
One says that an indecomposable multi-fusion category ${\mathcal C}'$ is a quotient category of an indecomposable multi-fusion category ${\mathcal C}$ if there exists a tensor functor $F:{\mathcal C}\to {\mathcal C}'$ such that any object of ${\mathcal C}'$ is a subobject of $F(X),\;
X\in {\mathcal C}$ (See Section 5). It follows from the above that a given multi-fusion category ${\mathcal C}$ has only finitely many quotient categories.
:::

::: corollary
[]{#ocnrigmod label="ocnrigmod"} A module category ${\mathcal M}$ over a multi-fusion category ${\mathcal C}$ does not admit nontrivial deformations. In particular, the number of such module categories (up to equivalence) with a given number of simple objects is finite.
:::

To prove Corollary [\[ocnrigmod\]](#ocnrigmod){reference-type="ref" reference="ocnrigmod"}, it suffices to choose a semisimple algebra $R$ with number of blocks equal to the number of simple objects in ${\mathcal M}$, and apply Theorem [\[ocnrigfun\]](#ocnrigfun){reference-type="ref" reference="ocnrigfun"} to the functor $F:{\mathcal C}\to R-\text{bimod}$ associated with ${\mathcal M}$.

::: remark
We note that this result was conjectured in [@O].
:::
