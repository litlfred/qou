---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-031-51-cohomology-and-duality
section_title: "Cohomology and duality"
section_number: 5.1
pages: 18-19
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.949
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — We show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼ = νA1[d]."
---
[]{#xxsec5.1 label="xxsec5.1"}

We begin with some definitions parallel to those introduced for homology in ([\[xxsec3.1\]](#xxsec3.1){reference-type="ref" reference="xxsec3.1"}). Let $A$ be an algebra, and let $\sigma$ be an algebra automorphism of $A.$ The *twisted Hochschild cohomology groups* $HH^{\ast}_{\sigma}(A)$ of $A$ with respect to $\sigma$ were defined in [@KMT] in a way exactly analogous to the twisted homology groups discussed in ([\[xxsec3.1\]](#xxsec3.1){reference-type="ref" reference="xxsec3.1"}). When $\sigma$ is diagonalisable the argument of [@HK1 Proposition 2.1] applies to show that, for all $i \geq
0$, $$HH_{\sigma}^i (A) \; \cong \; H^i (A,\, ^\sigma A).$$ Moreover [@We Corollary 9.1.5] can be invoked to show that, for all $i \geq 0,$ $$H^i(A,{^\sigma A})\; \cong \; \mathop{\mathrm{Ext}}_{A^e}^i(A,{^\sigma A}).$$

::: definition
1.  The *Hochschild cohomological dimension* of $A$ is $$\mathop{\mathrm{Hcdim}}A=\max\{i\;|\; HH^i(A)=H^{i}(A,A)\neq 0 \}.$$

2.  The *twisted Hochschild cohomological dimension* of $A$ is $$\mathop{\mathrm{tHcdim}}A=\max\{i\;|\; H^{i}(A,{^\sigma A})\neq 0
    \; \text{for some automorphism $\sigma$ of $A$}\}.$$

3.  We say that $A$ has *finite homological dimension* if there is an integer $d$ such that $H^i(A,-)=0$ for all $i>d$.
:::

In the presence of the Van den Bergh condition introduced in ([\[xxsec4.3\]](#xxsec4.3){reference-type="ref" reference="xxsec4.3"}) there is a beautiful twisted version of Poincar$\acute{\mathrm{e}}$ duality for $A$.

An object $X$ in the derived category $\mathop{\mathrm{{\sf D}}}(A$-$\mathop{\mathrm{{\sf Mod}}})$ is called *compact* if the functor $\mathop{\mathrm{Hom}}_{\mathop{\mathrm{{\sf D}}}(A-\mathop{\mathrm{{\sf Mod}}})}(X,-)$ commutes with coproducts. It is well-known that $X$ is compact if and only $X$ is quasi-isomorphic to a perfect complex over $A$ (namely, $X$ is quasi-isomorphic to a bounded complex of finitely generated projective $A$-modules).

::: proposition
[@VdB1] Let $A$ be an algebra of finite homological dimension $d$. Suppose that the Van den Bergh condition holds, and that $A$ is a compact object in $\mathop{\mathrm{{\sf D}}}(A^e$-$\mathop{\mathrm{{\sf Mod}}})$. Then for every $A$-bimodule $N$, $$H^i(A,N)=H_{d-i}(A,U\otimes_A N)$$ for all $i$, where $U$ is the invertible $A$-bimodule $\mathop{\mathrm{Ext}}^d_{A^e}(A,A^e)$.
:::

The above result provides further evidence that, at least for rigid Gorenstein algebras, twisted (co)homology is an important and necessary part of the study of Hochschild homology and cohomology.

Note that the hypothesis of $A$ being compact in $\mathop{\mathrm{{\sf D}}}(A^e$-$\mathop{\mathrm{{\sf Mod}}})$ does not appear in [@VdB1]; it has been pointed out to us by Van den Bergh that this is an oversight.

::: corollary
Let $A$ be a noetherian rigid Gorenstein algebra with Nakayama automorphism $\nu$. Suppose that $A$ has finite homological dimension $d$ and that $A$ is a compact object in $\mathop{\mathrm{{\sf D}}}(A^e$-$\mathop{\mathrm{{\sf Mod}}})$.

1.  $$H_d(A,{A^{\nu}}) \; \cong\;  Z(A) \neq 0,$$ and so $\mathop{\mathrm{tHdim}}A=d$.

2.  $$H^d(A,{^{\nu}A}) \;\cong \; A/[A,A].$$ If $A$ has a non-zero module of finite $k$-dimension then $\mathop{\mathrm{tHcdim}}A=d$.
:::

::: proof
*Proof.* By definition $U\, = \,{^1A^{\nu}}$. Let $V = U^{-1}\, =\, {^{\nu}A^1}$.

\(a\) By Proposition [\[xxsec5.1\]](#xxsec5.1){reference-type="ref" reference="xxsec5.1"}, $$H_d(A,{^1A^{\nu}}) \cong
 H^0(A,A) \cong Z(A)\supset k.$$

\(b\) By Proposition [\[xxsec5.1\]](#xxsec5.1){reference-type="ref" reference="xxsec5.1"}, $$H^d(A,{^{\nu}A^1}) \; \cong \; H_0 (A,U \otimes_A {^{\nu}A^1})
\;\cong \; H_0(A,A) \; = \; A/[A,A].$$

Suppose that $A$ has a non-zero finite dimensional module. We claim that $1\not\in [A,A]$, so that $A/[A,A]\neq 0$. To see this we can pass to a finite dimensional factor ring of $A$ and assume that $A$ is a simple finite dimensional algebra, hence a central simple algebra. In that case it is well-known that $1\not\in
[A,A]$.

When $A/[A,A]\neq 0$, then $H^d(A,{^{\nu}A^1})\neq 0$ and hence $\mathop{\mathrm{tHcdim}}A=d$. ◻
:::
