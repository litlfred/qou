---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-013-21-restriction-via
section_title: "Restriction via"
section_number: 2.1
pages: 5-6
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.935
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — We show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼ = νA1[d]."
---
[]{#xxsec2.1 label="xxsec2.1"}

Let $A$ be a Hopf algebra. Let $\Delta: A\to A\otimes A$ be the coproduct. Then we may view $A$ as a subalgebra of the algebra $A\otimes A$ via $\Delta$. Define a functor $$\mathrm{Res}_A\; : \; (A\otimes A)-\mathop{\mathrm{{\sf Mod}}}\; \to\;  A-\mathop{\mathrm{{\sf Mod}}}$$ by restriction of the scalars via $\Delta$, so that $\mathrm{Res}_A$ is equivalent to the functor $\mathop{\mathrm{Hom}}_{A\otimes
A}({_{A\otimes A}(A\otimes A)}_A,-)$.

::: lemma
Let $A$ be a Hopf algebra and $B$ be any algebra.

1.  $\mathrm{Res}_A$ is an exact functor.

2.  Let $N$ be an $A\otimes B^{\sf op}$-module. Then $\mathrm{Res}_A(A\otimes N)$ with restriction of $B^{\sf op}$-module from $N$ is isomorphic to ${_AA}\otimes {_k N_B}$ as $A\otimes B^{\sf op}$-modules where the left $A$-module on ${_kN_B}$ is trivial. The isomorphism from $\mathrm{Res}_A(A\otimes N)$ to ${_AA}\otimes {_k N_B}$ is given by $$a\otimes n\mapsto \sum a_1\otimes S(a_2) n,$$ where $\Delta(a)=\sum a_1\otimes a_2$, with inverse $a'\otimes
    n'\mapsto \sum a'_1\otimes a'_2n'$.

3.  $\mathrm{Res}_A$

    preserves freeness. Similarly, $A\otimes A$ is a free right $A$-module via the coproduct $\Delta$.

4.  $\mathrm{Res}_A$ preserves projectivity.

5.  $\mathrm{Res}_A$ preserves injectivity.
:::

::: proof
*Proof.* (a) This is clear.

\(b\) By the left-module version of the fundamental theorem of Hopf modules [@Mo Theorem 1.9.4] $A\otimes N$ is free over $A$ with basis given by a $k$-basis of $N$, because $N$ is the space of coinvariants of the left $A$-comodule $A \otimes N$. It's easy to verify that the isomorphism given in the proof of [@Mo Theorem 1.9.4] has the desired form, and that it preserves the $B^{\sf op}$-module action.

\(c\) This follows from (b) and its right-hand analogue, with $N = A$.

\(d\) This is true because $\mathrm{Res}_A(A\otimes A)$ is free by (c).

\(e\) Let $M$ be an injective $A\otimes A$-module. Then $$\mathop{\mathrm{Hom}}_A(-,\mathrm{Res}_A(M))\; \cong \; \mathop{\mathrm{Hom}}_A(-,\mathop{\mathrm{Hom}}_{A\otimes A}
({_{A\otimes A}(A\otimes A)_A},M))\; =: \;  (*)$$ By the $\mathop{\mathrm{Hom}}-\otimes$ adjunction $$(*) \; \cong \; \mathop{\mathrm{Hom}}_{A\otimes A}({_{A\otimes A}(A\otimes A)_A}
\otimes_A -,M)\;  =: \; (**).$$ By (c) $(A\otimes A)_A$ is free, hence flat. Since $M$ is $A\otimes A$-injective, the functor $(**)$ is exact. Hence $\mathrm{Res}_A(M)$ is $A$-injective. ◻
:::
