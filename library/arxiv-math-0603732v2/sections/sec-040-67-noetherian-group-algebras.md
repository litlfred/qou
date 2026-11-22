---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-040-67-noetherian-group-algebras
section_title: "Noetherian group algebras"
section_number: 6.7
pages: 26-29
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.968
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — We show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼ = νA1[d]."
---
[]{#xxsec6.7 label="xxsec6.7"}

::: theorem
Let $k$ be a field of characteristic $p \geq 0,$ and let $G$ be a polycyclic-by-finite group of Hirsch length $d.$

1.  $kG$ is noetherian Auslander Gorenstein and AS-Gorenstein of injective dimension $d.$

2.  $kG$ is AS-regular if and only if it is Auslander regular if and only if $G$ contains no elements of order $p.$
:::

::: proof
*Proof.* (a) First, $kG$ is noetherian by [@Pa Corollary 10.2.8]. Since we can find a poly-(infinite cyclic) normal subgroup $H$ of finite index in $G$ [@Pa Lemma 10.2.5], it is sufficient to prove that (i) $kH$ is AS-Gorenstein (respectively Auslander Gorenstein) when $H$ is poly-(infinite cyclic), and (ii) $kH$ AS-Gorenstein (respectively Auslander Gorenstein) implies that $kG$ is AS-Gorenstein (respectively Auslander Gorenstein) when $\mid G : H \mid$ is finite.

\(i\) We prove this by induction on the Hirsch number $d$ of $H.$ When $d = 0$ there is nothing to prove, so assume the result is true for all poly-(infinite cyclic) groups of Hirsch number less than $d$. Choose a normal subgroup $T$ of $H$ with $H/T =\langle
xT \rangle$ infinite cyclic.

AS-Gorenstein property: By the induction hypothesis, $\mathrm{Ext}^i_{kT}(k,kT) = \delta_{i,d-1}k.$ Applying $kH
\otimes_{kT} -$ to a projective $kT-$resolution of $k$, it is easy to prove that, for all $i \geq 0,$ $$\begin{aligned}
 \mathrm{Ext}^i_{kH}(kH \otimes_{kT} k, kH) \quad
\cong \quad \mathrm{Ext}^i_{kT}(k,kT)\otimes_{kT} kH
 
\end{aligned}$$ as right $kH-$modules. In particular, therefore, as right $k\langle x \rangle-$modules, $$\mathrm{Ext}^i_{kH}(kH \otimes_{kT} k, kH) \cong
\delta_{i,d-1}k\langle x \rangle.$$ Let's write $^H_T\negmedspace\uparrow \negmedspace k$ for $kH \otimes_{kT} k.$ The short exact sequence of left $kH-$modules $$0 \longrightarrow ^H_T\negmedspace \uparrow \negmedspace k
\longrightarrow ^H_T\negmedspace \uparrow \negmedspace
k \longrightarrow k \longrightarrow 0,$$ where the left-hand embedding is given by right multiplication by $x-1,$ induces exact sequences $$\mathrm{Ext}^i_{kH}(^H_T\negmedspace \uparrow \negmedspace k, kH)
\longrightarrow
\mathrm{Ext}^i_{kH}(^H_T\negmedspace \uparrow \negmedspace k, kH)
\longrightarrow
\mathrm{Ext}^{i+1}_{kH}(k,kH)\longrightarrow
\mathrm{Ext}^{i+1}_{kH}(^H_T\negmedspace \uparrow \negmedspace k,
kH),$$ where the left hand and right hand maps are left multiplication by $x-1,$ [@Br2 Lemma 2.1]. Taking $i< d-2$ here, and applying the induction hypothesis together with (6.7.1), shows that $\mathrm{Ext}_{kH}^{t}(k,kH) = 0$ for $t \leq d-2.$ Taking $i = d-2,$ we find in view of (6.7.1) that $\mathrm{Ext}_{kH}^{d-1}(k,kH)$ is the kernel of the map $$\mathrm{Ext}^{d-1}_{kH}(^H_T\negmedspace \uparrow \negmedspace
k,kH) \to \mathrm{Ext}^{d-1}_{kH}(^H_T\negmedspace \uparrow
\negmedspace k,kH),$$ a homomorphism $\rho$ between free $k\langle x \rangle-$modules of rank one given by multiplication by $x-1.$ Therefore, $\mathrm{Ext}_{kH}^{d-1}(k,kH)$ is $0.$ Moreover, since $\mathop{\mathrm{Ext}}^{d+1}_{kH}(^H_T\negmedspace \uparrow
\negmedspace k, kH)$ is $0$, by (6.7.1), the cokernel of $\rho$ is $\mathrm{Ext}^d_{kH}(k,kH)$. Thus $\mathrm{Ext}^d_{kH}(k,kH)$ has $k$-dimension one, as required.

Auslander Gorenstein property: Note that $kH=kT[t^{\pm 1};\sigma]$ for some automorphism $\sigma$ of $kT$. By the induction hypothesis, $kT$ is Auslander Gorenstein. By [@Ek Theorem 4.2], $kT[t;\sigma]$ is Auslander Gorenstein. By [@ASZ2 Proposition 2.1] the localization $kT[t^{\pm 1};\sigma]$ is Auslander Gorenstein.

\(ii\) This follows because crossed products of finite groups are Frobenius extensions - see [@AB Lemma 5.4].

\(b\) This follows from (a) and [@Pa Theorem 10.3.13]. ◻
:::

::: remarks
1.  It is an open question whether all noetherian group algebras $kG$ come from polycyclic-by-finite groups $G$.

2.  In general a noetherian group algebra $kG$ could have infinite GK-dimension [@KL Corollary 11.15]. Even when $\mathop{\mathrm{GKdim}}kG$ is finite, it could be larger than the global dimension of $kG$. Hence in these cases, $kG$ is not Cohen-Macaulay.
:::

Poincaré duality of group homology and cohomology was investigated by Bieri in a series of papers beginning with [@Bi1]. Given a commutative ring $R$, a non-negative integer $n$ and a group $G$, he defined [@Bi2 5.1.1] $G$ to be a *duality group of dimension $n$ over $R$* if there exists an $RG-$module $C$ such that, for each $RG-$module $A$ and each $k \in \mathbb{Z}$, there are isomorphisms $$H^k(G,A) \cong H_{n-k}(G, C \otimes_R A)$$ induced by the cap product. Moreover, [@Bi2 Definition 3.2], $G$ is a *Poincaré duality group of dimension $n$ over $R$* if $C$ above is $R$ with *almost trivial* $G-$structure, where this means that the image of $G$ in $\mathrm{Aut}_R(R)$ is $\{\pm \mathrm{Id} \}.$

It's clear that, for polycyclic-by-finite groups, Bieri's results describe the shadow at the level of group (co)homology of the existence and nature of the dualising complex for $kG$. On the other hand it is straightforward to apply the results of [@Bi1], [@Bi2] to determine the Nakayama automorphism for $kG$. In order to do this, we define the *adjoint trace* $\texttt{T}$ of the polycyclic-by-finite group $G$ as follows. Fix a series $$\begin{aligned}
 1 = G_0 \subseteq G_1 \subseteq \cdots \subseteq G_n = G
\end{aligned}$$ of normal subgroups $G_i$ of $G$ whose factors $G_i/G_{i-1}$ are either torsion-free Abelian, or finite. Provide each torsion-free factor $A_i = G_i/G_{i-1}$ with a $\mathbb{Z}-$basis (of cardinality $t_i$, say), so that conjugation by $g \in G$ assigns a matrix $\tilde{g}_i \in \mathrm{GL}_{t_i}(\mathbb{Z})$ to the pair $(g, A_i).$ Now define a map $$\texttt{T}: G \longrightarrow \{\pm 1 \} : g \mapsto
\prod_i \mathrm{det} (\tilde{g}_i) ,$$ where the product is taken over those $i$, $1 \leq i \leq n,$ such that $G_i/G_{i-1}$ is infinite. One checks easily that this definition doesn't depend on the choice of series (6.7.2), and that $\texttt{T}$ is a group homomorphism [@Bi1 §3.2]. Finally, set $\texttt{T}_k$ to be the composition of $\texttt{T}$ with the canonical homomorphism from $\{\pm 1 \}$ to $k$, and use the same symbol for the resulting representation of $kG$ on $k.$

::: proposition
Let $k$ be a field of characteristic $p \geq 0,$ and let $G$ be a polycyclic-by-finite group with Hirsch length $d.$ If $p > 0$ assume that $G$ contains no elements of order $p.$

1.  [@Bi2] $G$ is a Poincaré duality group over $k$. The dualising module $C$ is $H^d(G,kG);$ that is, $C$ is the left integral of $kG.$

2.  The Nakayama automorphism $\nu$ of $kG$ is the winding automorphism induced by the adjoint trace $\texttt{T}_k$ of $G$ in $k$. That is, $$\nu (g) \quad = \quad \texttt{T}_k (g) g$$ for all $g \in G.$ In particular, $\nu$ is diagonalisable.

3.  $H_d(kG,kG^{\nu}) \cong Z(kG) \neq 0,$ and $H^d(kG,\,^{\nu}kG)
    \cong kG/[kG,kG] \neq 0.$

4.  The integral order of $kG$ is either 1 or 2.
:::

::: proof
*Proof.* (a) The first statement is proved in [@Bi2 Theorems 5.6.2 and 5.6.4], and the second is [@Bi2 Proposition 5.2.1]. (Of course, (a) also follows from Theorem [\[xxsec6.7\]](#xxsec6.7){reference-type="ref" reference="xxsec6.7"} and Lemma [\[xxsec3.3\]](#xxsec3.3){reference-type="ref" reference="xxsec3.3"}.)

\(b\) By Theorem [\[xxsec6.7\]](#xxsec6.7){reference-type="ref" reference="xxsec6.7"}, $kG$ is AS-regular. Since the square of the antipode of $kG$ is the identity, Proposition [\[xxsec4.5\]](#xxsec4.5){reference-type="ref" reference="xxsec4.5"}(a) shows that the Nakayama automorphism of $kG$ is the winding automorphism induced by the right module structure of the left integral. The calculations in [@Bi1 §3.2] show that this right structure is given by $\texttt{T}_k$.

\(c\) This follows from Corollary [\[xxsec5.1\]](#xxsec5.1){reference-type="ref" reference="xxsec5.1"}.

\(d\) This is clear from part (b). ◻
:::
