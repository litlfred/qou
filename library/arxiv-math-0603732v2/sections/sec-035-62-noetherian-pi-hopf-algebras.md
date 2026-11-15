---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-035-62-noetherian-pi-hopf-algebras
section_title: "Noetherian PI Hopf algebras"
section_number: 6.2
pages: 21-23
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.977
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — We show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼ = νA1[d]."
---
[]{#xxsec6.2 label="xxsec6.2"}

Let $A$ be a noetherian affine PI Hopf algebra, and consider conditions (1) and (2) of (6.1). By Skryabin's result Proposition [\[xxsec1.1\]](#xxsec1.1){reference-type="ref" reference="xxsec1.1"}(b), the antipode of $A$ is bijective, so (2) is satisfied. As for (1), first note that $A$ is Auslander-Gorenstein, of dimension $d$, say, by [@WZ1 Theorem 0.1]. By [@Br2 Theorem A] there is an irreducible left $A$-module $W$ for which $\mathop{\mathrm{Ext}}^d_A(W,A) \neq 0$, so that [@BG1 Lemma 1.11] confirms that $\mathop{\mathrm{Ext}}^d_A(V,A) \neq 0$ for every left irreducible $A$-module $V$. Hence [@SZ Theorem 3.10(iii)(a)] ensures that $A$ is (Krull) Cohen-Macaulay. Since the Krull and GK-dimensions coincide for affine noetherian PI algebras by [@MR Proposition 13.10.6 and Theorem 6.4.8], we can conclude that $A$ is Auslander-Gorenstein and Cohen-Macaulay. Thus, by Lemma [\[xxsec6.1\]](#xxsec6.1){reference-type="ref" reference="xxsec6.1"}, $A$ is AS-Gorenstein.

The situation regarding (3) of (6.1) in the PI case is less straightforward, since it depends on the characteristic of $k.$ The enveloping algebra of the two-dimensional solvable non-abelian Lie algebra in positive characteristic demonstrates that diagonalisability of ${\xi}$ and thus of $\nu$ will fail in general for Hopf algebras which are finite modules over their centres. Nevertheless, in this setting $\nu$ has finite order up to an inner automorphism, and so Maschke's theorem comes into play in characteristic 0. Here is the required result:

::: proposition
Let $A$ be a noetherian affine PI Hopf algebra of finite global dimension.

1.  The winding automorphism ${\xi}$ has finite order.

2.  Some power of the antipode $S$ of $A$ is inner.

3.  The Nakayama automorphism $\nu$ has finite order up to inner automorphisms.
:::

::: proof
*Proof.* The discussion in the opening paragraph of this subsection shows that $A$ is homologically homogeneous, so that $A$ is a finite module over its centre by [@SZ Theorem 5.6(iv)].

\(a\) By [@LWZ Lemma 5.3(g)], $io(A)$ is finite. This is saying that ${\xi}$ has finite order.

(b,c) Follow from part (a) and Proposition [\[xxsec4.6\]](#xxsec4.6){reference-type="ref" reference="xxsec4.6"}(b,c). ◻
:::

Notice that the proof of the proposition works without the global dimension hypothesis provided $A$ is a finite module over its centre.

Given (b) of the proposition, it makes sense to ask:

::: question
If $A$ is a noetherian affine PI Hopf algebra, does the antipode of $A$ have finite order?
:::

For regular PI Hopf algebras the equalities (4) of (6.1) are valid. To see this, we need a lemma. Recall for its proof that the Nakayama automorphism acts trivially on the centre, by Proposition [\[xxsec4.4\]](#xxsec4.4){reference-type="ref" reference="xxsec4.4"}(b).

::: lemma
Let $A$ be a noetherian affine PI Hopf algebra of finite global dimension, and let $\nu={\xi}S^2$ be its Nakayama automorphism.

1.  $\nu, \nu^{-1}\in N(A).$

2.  If $\sigma\in N(A)$ and the restriction of $\sigma$ to the centre is the identity, then $${^\sigma A}/[A,{^\sigma A}]\;\neq \;0.$$
:::

::: proof
*Proof.* (a) By [@BG1 Corollary 1.8], $A$ is a direct sum of prime rings. The central idempotents corresponding to the direct summands of $A$ are fixed by $\nu.$ For this reason we may assume $A$ is a prime ring (and forget about the coalgebra structure for the rest of the proof).

Since $A$ is a noetherian affine prime PI algebra, the Goldie quotient ring $Q(A)$ is isomorphic to the central localization $AC^{-1}$, where $C=Z(A)\setminus\{0\}$. Clearly $Q(A)$ is a central simple algebra with centre $Z(A)C^{-1}$ [@MR Theorem 13.6.5]. The automorphism $\nu$ extends to $Q(A)$ naturally, still denoted by $\nu$. The restriction of $\nu$ to the centre $Z(Q)$ is the identity, and so, by the Skolem-Noether theorem, $\nu$ is an inner automorphism. Thus there is an invertible element $x\in Q(A)$ such that $\nu(b)=xbx^{-1}$ for all $b\in
Q(A)$. Write $x=ms^{-1}$ where $m\in A$ is not a zero divisor and $s\in Z(A)\setminus\{0\}.$ Then, for every $a\in A$, $$\nu(a) m\;=\; x a x^{-1} m\;=\; x a s\;=\; xs a\;=\;
ma.$$ Hence $\nu\in N(A)$. The proof works for any automorphism whose restriction to the centre is the identity, and in particular for $\nu^{-1}$.

\(b\) As in (a) we may assume $A$ is prime. Let $Q=Q(A)$. It suffices to show that there is an elememt $m\in A$ such that $m\not\in [Q,{^\sigma Q}]$. By the proof of (a), $\sigma$ is an inner automorphism, say $\sigma(b)=m b
m^{-1}$ for some regular element $m \in A$. For all $a,b\in Q$, $$\sigma(b)a-ab=mbm^{-1}a-ab\;=\; m(bm^{-1}a-m^{-1}ab)
\;=\; m[b,m^{-1}a].$$ This means that $[Q,{^\sigma Q}]=m[Q,Q]$. Since $1\not\in [Q,Q]$, we deduce $m\not\in
[Q,{^\sigma Q}]$. ◻
:::

::: theorem
Let $A$ be a noetherian affine PI Hopf algebra of GK-dimension $d$.

1.  $A$ has rigid dualising complex $^{\nu}A^1 [d]$ where $\nu = {\xi}S^2$ is the Nakayama automorphism of $A$.

2.  Suppose that $A$ has finite global dimension. Then $\mathop{\mathrm{Hdim}}A=\mathop{\mathrm{Hcdim}}A=\mathop{\mathrm{gldim}}A = d$.
:::

::: proof
*Proof.* (a) By the opening paragraph of ([\[xxsec6.2\]](#xxsec6.2){reference-type="ref" reference="xxsec6.2"}) $A$ is AS-Gorenstein of dimension $d$, so this is immediate from Proposition [\[xxsec4.5\]](#xxsec4.5){reference-type="ref" reference="xxsec4.5"}.

\(b\) This follows from the above lemma and Theorem [\[xxsec3.4\]](#xxsec3.4){reference-type="ref" reference="xxsec3.4"}(c) and [\[xxsec5.3\]](#xxsec5.3){reference-type="ref" reference="xxsec5.3"}(c). Note that the latter applies because $A$ (and hence $A^e$) are finite modules over their affine centres, by [@SZ Theorem 5.6(iv)]. ◻
:::
