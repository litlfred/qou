---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-030-51-cohomology-and-duality
section_title: "Cohomology and duality"
section_number: 5.1
pages: 18-21
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — W e show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼= ν A1[d]."
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.968
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

## Poincaré duality for Hopf algebras {#xxsec5.2}

In parallel to Proposition [\[xxsec3.3\]](#xxsec3.3){reference-type="ref" reference="xxsec3.3"} for Hochschild dimension, there is an easy upper bound for the twisted cohomological dimension of a Hopf algebra. Throughout this subsection we assume $S$ is bijective.

::: lemma
Let $A$ be a Hopf algebra of finite global dimension $d$.

1.  $A$ has finite homological dimension, bounded by $d$. This says that $A$ has a resolution of projective left $A^e$-modules bounded at position $-d$. Consequently, $\mathop{\mathrm{tHcdim}}A\leq d$.

2.  If $A$ is noetherian, then $k$ is a compact object in $\mathop{\mathrm{{\sf D}}}(A$-$\mathop{\mathrm{{\sf Mod}}})$.

3.  If $A$ is noetherian, then $A$ is a compact object in $\mathop{\mathrm{{\sf D}}}(A^e$-$\mathop{\mathrm{{\sf Mod}}})$.
:::

::: proof
*Proof.* (a) By [@We Corollary 9.1.5], for all $i \geq 0,$ $$H^i(A,M)\; \cong \; \mathop{\mathrm{Ext}}_{A^e}^i(A,M)$$ for every $A$-bimodule $M$. By Lemma [\[xxsec2.4\]](#xxsec2.4){reference-type="ref" reference="xxsec2.4"}(b), $$\mathop{\mathrm{Ext}}_{A^e}^i(A,M)\; \cong \; \mathop{\mathrm{Ext}}^i_A(k,L(M))\; =\; 0$$ for all $i>d$.

\(b\) This is trivial since $A$ is noetherian and $k$ has a bounded resolution of finitely generated projective left $A$-modules.

\(c\) By part (b) $k$ is quasi-isomorphic to a prefect complex in $\mathop{\mathrm{{\sf D}}}(A$-$\mathop{\mathrm{{\sf Mod}}})$. Hence, for each $i$, $\mathop{\mathrm{Ext}}^i_{A}(k,-)$ commutes with inductive direct limits in $A$-$\mathop{\mathrm{{\sf Mod}}}$. Recall that $A$-$\mathop{\mathrm{{\sf Mod}}}$ is a Grothendieck category and, in particular, inductive direct limits are exact [@Po Chapter 2]. Since $L(-)$ is a composition of a restriction functor with an invertible functor, it also commutes with inductive direct limits. Hence $\mathop{\mathrm{Ext}}^i_A(k,L(-))$ commutes with inductive direct limits in $A^e$-$\mathop{\mathrm{{\sf Mod}}}$. By Lemma [\[xxsec2.4\]](#xxsec2.4){reference-type="ref" reference="xxsec2.4"}(b), for any $A^e$-module $M$, $$\mathop{\mathrm{Ext}}^i_{A^e}(A,M)\cong \mathop{\mathrm{Ext}}^i_{A}(k,L(M))$$ for all $i$. Therefore $\mathop{\mathrm{Ext}}^i_{A^e}(A,-)$ commutes with inductive direct limits for all $i$. Together with part (a) and the claim in the next paragraph we show that $A$ is compact in $\mathop{\mathrm{{\sf D}}}(A^e$-$\mathop{\mathrm{{\sf Mod}}})$.

It remains to show the following: *if $M$ is a left $A^e$-module of finite projective dimension such that $\mathop{\mathrm{Ext}}^i_{A^e}(M,-)$ commutes with inductive direct limits for all $i$, then $M$ has a projective resolution such that each term in the resolution is a finitely generated projective left $A^e$-module.* Since $\mathop{\mathrm{Hom}}_{A^e}(M,-)$ commutes with inductive direct limits, $M$ is finitely presented by [@Po Theorem 3.5.10]. So we have a short exact sequence $$0\to M^{-1}\to P^0\to M\to 0$$ where $P^0$ is a finitely generated projective left $A^e$-module. Clearly $\mathop{\mathrm{Ext}}^i_{A^e}(P^0,-)$ commutes with inductive direct limits for all $i$. Using the long exact sequence we obtain that $\mathop{\mathrm{Ext}}^i_{A^e}(M^{-1},-)$ commutes with inductive direct limits for all $i$. Then induction on the projective dimension of the $A^e$-module $M$ shows that $M$ has a resolution by finitely generated projective left $A^e$-modules. ◻
:::

The following corollary is an immediate consequence of Propositions [\[xxsec5.1\]](#xxsec5.1){reference-type="ref" reference="xxsec5.1"} and [\[xxsec4.5\]](#xxsec4.5){reference-type="ref" reference="xxsec4.5"} and the above lemma.

::: corollary
Let $A$ be a noetherian AS-regular Hopf algebra of global dimension $d$.

Suppose that $S$ is bijective, and let ${\xi}$ be the winding automorphism induced by the left integral, (2.5.1). Then for every $A$-bimodule $M$ and for all $i$, $0 \leq i \leq d,$ $$H^i(A,M)=H_{d-i}(A,{^{{\xi}^{-1}S^{-2}}M}).$$
:::

## Proof of Theorem [\[xxsec0.4\]](#xxsec0.4){reference-type="ref" reference="xxsec0.4"}(b) {#xxsec5.3}

Given an $A$-bimodule $M,$ we let $[A,M]$ denote the $k$-subspace of $M$ spanned by $\{am-ma : a\in A,\,m\in M\}$. It is easy to see that $$H_0(A,M) = A\otimes_{A^e} M=M/[A,M].$$ The following result follows from Corollary [0.1](#xxsec5.2){reference-type="ref" reference="xxsec5.2"}, and incorporates the remainder of Theorem [\[xxsec0.4\]](#xxsec0.4){reference-type="ref" reference="xxsec0.4"}(b).

::: theorem
Let $A$ be a noetherian AS-regular Hopf algebra of global dimension $d$ and having bijective antipode $S.$

Define $\nu= \xi S^2.$

1.  For every algebra automorphism $\sigma$ of $A,$ $$H^d(A,{^\sigma A})\cong A\otimes_{A^e}{^{\nu^{-1}\sigma}A}
    \;=\; {^{\nu^{-1}\sigma}A}/[A,{^{\nu^{-1}\sigma}A}].$$

2.  In particular, $$H^d(A,{^{\nu}A}) \cong A/[A,A]\neq 0,$$ and so $\mathop{\mathrm{tHcdim}}A=d$.

3.  $\mathop{\mathrm{Hcdim}}A=d$ if and only if $A^\nu/[A,A^\nu]\neq 0$.
:::
