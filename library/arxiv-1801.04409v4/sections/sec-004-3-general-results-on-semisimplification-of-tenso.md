---
doc_id: arxiv-1801.04409v4
doc_title: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES"
section_id: sec-004-3-general-results-on-semisimplification-of-tenso
section_title: "General results on semisimplification of tensor categories"
section_number: 3
pages: 8-14
source_pdf: 1801.04409v4.pdf
source_sha256: db61d011e3775aca
text_source: latex
latex_prose_ratio: 0.911
latex_coverage_ratio: 0.961
doc_brief: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES — We develop the theory of semisimpliﬁcations of ten- sor categories deﬁned by Barrett and Westbury."
---
## Splitting of the semisimplification functor for Tannakian categories in characteristic zero, reductive envelopes, and the Jacobson-Morozov lemma

For Tannakian categories in characteristic zero, André and Kahn showed that the semisimplification functor $\bold S$ admits a splitting $\bold S^*$, and used it to show the existence and uniqueness (up to conjugation) of the reductive envelope of any affine proalgebraic group in characteristic zero. In this subsection we review this theory (cf. [@AK],[@S]).

::: theorem
[]{#splitting label="splitting"} ([@AK], Theorem 1, Theorem 2) If ${\rm char}(\mathbf{k})=0$ and $\mathcal{C}=\mathop{\mathrm{Rep}}\nolimits G$ is a Tannakian category over $\mathbf{k}$ (where $G$ is an affine proalgebraic group over $\mathbf{k}$), then the functor $\bold S: \mathcal{C}\to \overline{\mathcal{C}}$ admits a splitting $\bold S^*: \overline{\mathcal{C}}\to {\mathcal{C}}$, a surjective tensor functor such that $\bold S^*(\overline X)\cong X$ for each indecomposable $X\in \mathcal{C}$, and ${\bold S}\circ \bold S^*\cong {\rm Id}$ as a symmetric tensor functor.
:::

Now let $\mathcal{C}$ be as above and $F$ be the forgetful functor $\mathcal{C}\to \mathrm{Vec}$. Then $F\circ \bold S^*: \overline{\mathcal{C}}\to \mathrm{Vec}$ is a fiber functor, so by the Tannakian formalism ([@DM]), we have $\overline{\mathcal{C}}=\mathop{\mathrm{Rep}}\nolimits\overline{G}$, where $\overline{G}:=\mathop{\mathrm{Aut}}\nolimits(F\circ \bold S^*)$ is a reductive affine proalgebraic group, equipped with a homomorphism $\psi_G: G\to \overline{G}$ (defined up to conjugation in $\overline{G}$) giving rise to the functor $\bold S^*$. Moreover, since $\bold S^*$ is surjective, $\psi_G$ is an inclusion.

::: definition
([@AK]) The group $\overline{G}$ equipped with the homomorphism $\psi_G$ (defined up to conjugation) is called the *reductive envelope* of $G$.
:::

::: theorem
([@AK], Theorem 3, Theorem 4)[]{#ak label="ak"} The reductive envelope $\overline{G}$ enjoys the following universal property: If $\phi: G\to L$ is a homomorphism from $G$ to a reductive proalgebraic group $L$, then there exists a homomorphism $\overline{\phi}: \overline{G}\to L$ such that $\phi=\overline{\phi}\circ \psi_G$. Moreover, $\overline{\phi}$ is unique up to conjugation in $L$ by elements commuting with $\phi(G)$.
:::

::: proof
*Proof.* The morphism $\phi$ gives rise to a symmetric tensor functor $\Phi: \mathop{\mathrm{Rep}}\nolimits L\to \mathop{\mathrm{Rep}}\nolimits G$. Consider the functor $\Phi':=\bold S\circ \Phi$. Even though $\bold S$ may not be exact on any side, the functor $\Phi'$ is exact since the category $\mathop{\mathrm{Rep}}\nolimits L$ is semisimple (as $L$ is reductive). Thus, $\Phi': \mathop{\mathrm{Rep}}\nolimits L\to \mathop{\mathrm{Rep}}\nolimits\overline{G}$ is a symmetric tensor functor. Hence, by Tannakian formalism ([@DM]) it comes from a homomorphism $\phi': \overline{G}\to L$ defined uniquely up to conjugation in $L$. Moreover, consider the functor $\bold S^*\circ \Phi'=\bold S^*\circ \bold S\circ \Phi$. This functor is exact since its source is a semisimple category, so it is a symmetric tensor functor, and it follows from Proposition 13.7.1 of [@AK] that it is naturally isomorphic to $\Phi$ as a tensor functor. This means that the homomorphisms $\phi$ and $\phi'\circ \psi_G$ are conjugate under $L$: $\phi(g)=\ell \phi'(\psi_G(g))\ell^{-1}$ for some $\ell\in L$ and all $g\in G$. Hence, $\phi(g)=\widetilde{\phi}(\psi_G(g))$ for all $g\in G$, where $\widetilde{\phi}(a):=\ell \phi'(a)\ell^{-1}$.

Finally, let us show that the homomorphism $\widetilde{\phi}$ in the theorem is determined uniquely up to conjugation in $L$ (automatically by elements commuting with $\phi(G)$). To this end, let $\widetilde\Phi: \mathop{\mathrm{Rep}}\nolimits L\to \mathop{\mathrm{Rep}}\nolimits G$ be the functor defined by $\widetilde{\phi}$. Then $\bold S^*\circ \widetilde{\Phi}=\Phi$, hence, postcomposing with $\bold S$, we get $\widetilde \Phi=\bold S\circ \Phi$. Thus, $\widetilde \Phi$ is uniquely determined and hence $\widetilde{\phi}$ is determined up to conjugation, as desired. ◻
:::

::: remark
A geometric proof of the existence and properties of the reductive envelope is given in [@S].
:::

::::: example
Consider the special case $G=\Bbb G_a$. In this case the indecomposable representations of $G$ are unipotent Jordan blocks $J_n$ of sizes $n=1,2,3...$, so it is easy to see that $\overline{\mathop{\mathrm{Rep}}\nolimits G}\cong \mathop{\mathrm{Rep}}\nolimits SL(2)$ (as the Grothendieck ring of $\overline{\mathop{\mathrm{Rep}}\nolimits G}$ coincides with that of $\mathop{\mathrm{Rep}}\nolimits SL(2)$, and the dimensions of nonzero objects of $\overline{\mathop{\mathrm{Rep}}\nolimits G}$ are positive). So in this case the existence of $\overline{G}$ is easy (namely, $\overline{G}=SL(2)$), and the existence of the splitting $\bold S^*$ is also straightforward (namely, $\bold S^*$ is induced by the standard inclusion $\psi_G: \Bbb G_a\hookrightarrow SL(2)$ as upper triangular matrices with ones on the diagonal). Thus, Theorem [\[ak\]](#ak){reference-type="ref" reference="ak"} in this case tells us that any homomorphism $\phi: \Bbb G_a\to L$ for a reductive proalgebraic group $L$ uniquely (up to conjugacy) factors through a homomorphism $\widetilde{\phi}: SL(2)\to L$. As pointed out in [@AK; @S], this implies the celebrated *Jacobson-Morozov Lemma*:

::: proposition
Let $L$ be a reductive algebraic group over $\mathbf{k}$, and $u\in L$ a unipotent element. Then there exists a homomorphism $\theta: SL(2)\to L$ such that $\theta\left(\begin{matrix} 1&1\\ 0&1\end{matrix}\right)=u$. Moreover, $\theta$ is unique up to conjugation by the centralizer $Z_u$ of $u$.
:::

::: proof
*Proof.* Let $G$ be the 1-parameter unipotent subgroup of $L$ generated by $u$, and $\phi: G\to L$ be the corresponding embedding. Identify $G$ with $\Bbb G_a$ by sending $u$ to $1$. Then it remains to apply Theorem [\[ak\]](#ak){reference-type="ref" reference="ak"} and set $\theta=\widetilde\phi$. ◻
:::
:::::

Note that when $G$ is an algebraic group then $\overline{G}$ is typically only a proalgebraic group (of infinite type), which can be very large. In fact, this is already so when $G=\Bbb G_a^2$, since the problem of classifying pairs of commuting matrices is well known to be wild; i.e., the case $G=\Bbb G_a$ (leading to the Jacobson-Morozov Lemma) is a rare exception. In other words, the whole category $\mathop{\mathrm{Rep}}\nolimits\overline{G}$ is typically unmanageable. However, it makes sense to consider tensor subcategories of this category generated by a single object, which are more manageable. Namely, we have the following corollary.

::: corollary
[]{#parenv label="parenv"} Let $G$ be an affine algebraic group over $\mathbf{k}$, and $V\in \mathop{\mathrm{Rep}}\nolimits G$ a faithful representation of $G$ (so that $G\hookrightarrow GL(V)$). Then there exists a reductive algebraic group $G_V\subset GL(V)$ containing $G$ (a quotient of $\overline{G}$) such that the subcategory $\mathcal{C}_V$ of $\overline{\mathop{\mathrm{Rep}}\nolimits G}\cong \mathop{\mathrm{Rep}}\nolimits\overline{G}$ tensor generated by $\overline{V}$ is naturally equivalent to $\mathop{\mathrm{Rep}}\nolimits G_V$.
:::

::: proof
*Proof.* Let $F_V: \mathcal{C}_{\overline{V}}\to \mathrm{Vec}$ be the restriction of the fiber functor of $\mathop{\mathrm{Rep}}\nolimits\overline{G}$ to $\mathcal{C}_{\overline{V}}$. Let $G_V:=\mathop{\mathrm{Aut}}\nolimits(F_V)$. Then $G_V\subset GL(V)$ is a reductive subgroup such that $\mathop{\mathrm{Rep}}\nolimits G_V=\mathcal{C}_{\overline{V}}$. Moreover, $G_V$ is a quotient of $\overline{G}$, hence we have a natural homomorphism $G\to G_V$, which is obviously injective, as desired. ◻
:::

::: definition
[]{#aksec label="aksec"} We will call $G_V$ the *reductive envelope of $G$ inside $GL(V)$*.
:::

::: remark
1\. Let $\mathcal{C}=\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}\Bbb Z/p$ , where ${\rm char}(\mathbf{k})=p\ge 5$. Then a tensor functor $\bold S^*: \overline{\mathcal{C}}\to \mathcal{C}$ does not exist, since $\overline{\mathcal{C}}={\rm Ver}_p$ contains objects of non-integer Frobenius-Perron dimension. Also, if $\mathcal{C}=\mathop{\mathrm{Rep}}\nolimits GL(n|1)$ over $\mathbf{k}$ of characteristic zero then a symmetric functor $\bold S^*$ as is Theorem [\[splitting\]](#splitting){reference-type="ref" reference="splitting"} does not exist, either. Indeed, if $V$ is the vector representation of $GL(n|1)$ then $\wedge^{n-1}\bold S(V)=0$ (cf. Example [\[ex1\]](#ex1){reference-type="ref" reference="ex1"}(3)), while $\wedge^{n-1}V\ne 0$ (it is a negligible but nonzero object in $\mathcal{C}$). In fact, it is clear that a splitting functor $\bold S^*$ with the properties stated in Theorem [\[splitting\]](#splitting){reference-type="ref" reference="splitting"} cannot exist if $\mathcal{C}$ has indecomposable objects of dimension $0$.

2\. Note that the existence of the group $\overline{G}$ such that $\mathop{\mathrm{Rep}}\nolimits\overline{G}\cong \overline{\mathop{\mathrm{Rep}}\nolimits G}$ follows from Deligne's theorem ([@D1], Theorem 7.1), since $\overline{\mathop{\mathrm{Rep}}\nolimits G}$ is a symmetric tensor category over $\mathbf{k}$ in which nonzero objects have positive integer dimensions. This is, in fact, used in the proof of Theorem [\[splitting\]](#splitting){reference-type="ref" reference="splitting"} in [@AK].

Moreover, using a more general version of Deligne's theorem for supergroups, [@D2], one can see that if $G$ is an affine proalgebraic supergroup over $\mathbf{k}$ of characteristic zero and $z\in G$ an element of order $\le 2$ acting on $O(G)$ by parity, and $\mathop{\mathrm{Rep}}\nolimits(G,z)$ is the category of representations of $G$ on superspaces on which $z$ acts by parity, then $\overline{\mathop{\mathrm{Rep}}\nolimits(G,z)}=\mathop{\mathrm{Rep}}\nolimits(\overline{G},\overline{z})$ for some reductive proalgebaric supergroup $\overline{G}$, i.e., one whose representation category is semisimple, see [@H], Theorem 2.2. In particular, for each $V\in \mathop{\mathrm{Rep}}\nolimits(G,z)$, $\overline{V}$ generates a category $\mathop{\mathrm{Rep}}\nolimits(G_V,\overline{z})$, where $G_V$ is a reductive algebraic supergroup (a quotient of $\overline{G}$). This means that the connected component of the identity $G_V^0$ of $G_V$ is of the form $G_V'/C$, where $C$ is a finite central subgroup and $G_V'=G_V^+\times G_V^-$, where $G_V^+$ is a usual reductive group, and ${\rm Lie}G_V^-$ is a direct sum of Lie superalgebras of type $\mathfrak{osp}(1|2n)$, see [@W].
:::

In fact, as was explained to us by Thorsten Heidersdorf, the symmetric structure of the category is not essential in the André-Kahn theorem on the existence of splitting of the semisimplification functor. Namely, Theorem 12.1.1 and 13.2.1 of [@AK] immediately imply the following theorem:

::: theorem
[]{#AKth label="AKth"} Let $\mathcal{C}$ be a Karoubian pivotal category as in Theorem [\[karpiv\]](#karpiv){reference-type="ref" reference="karpiv"}, such that the ideal ${\mathcal N}(\mathcal{C})$ of negligible morphisms in $\mathcal{C}$ coincides with the nilpotent radical ${\rm rad}(\mathcal{C})$ of $\mathcal{C}$ (where ${\rm rad}(\mathcal{C})(X,Y)$ is the intersection of the radical of the algebra ${\rm End}(X\oplus Y)$ with $\mathrm{Hom}_\mathcal{C}(X,Y)$); in other words, $\mathcal{C}$ has no nonzero indecomposable objects of zero dimension. Then the semisimplification functor $\bold S: \mathcal{C}\to \overline{\mathcal{C}}$ admits a monoidal splitting $\bold S^*:\overline{\mathcal{C}}\to \mathcal{C}$.
:::

::: corollary
[]{#AK2 label="AK2"} Let $\mathcal{C}$ be a Karoubian pivotal category as in Theorem [\[karpiv\]](#karpiv){reference-type="ref" reference="karpiv"}. Then following conditions are equivalent:

\(i\) Any indecomposable direct summand in a tensor product of two indecomposable objects of nonzero dimension also has nonzero dimension; in other words, indecomposables of nonzero dimension span a full monoidal subcategory of $\mathcal{C}$.

\(ii\) The semisimplification functor $\bold S: \mathcal{C}\to \overline{\mathcal{C}}$ admits a monoidal splitting $\bold S^*:\overline{\mathcal{C}}\to \mathcal{C}$.
:::

::: proof
*Proof.* It follows from Theorem [\[AKth\]](#AKth){reference-type="ref" reference="AKth"} that (i) implies (ii). To prove that (ii) implies (i), assume that (i) fails, and let $X,Y$ be simple objects of nonzero dimension such that $X\otimes Y\cong Z\oplus T$ where $Z\ne 0$ is indecomposable and has dimension zero. Then $\bold S(X)\otimes \bold S(Y)\cong \bold S(T)$. So if there is a monoidal splitting $\bold S^*$, then applying $\bold S^*$ to the last equality, we get $X\otimes Y\cong T$. Thus, $T\cong Z\oplus T$, which contradicts the Krull-Schmidt theorem. ◻
:::

In particular, this implies existence of reductive envelopes for quantum groups. Namely, let $H$ be a Hopf algebra over a field $\mathbf{k}$ in which the squared antipode is given by conjugation by a character $\chi\in H^*$ (thereby defining a pivotal structure on ${\rm Corep}(H)$), with no indecomposable finite dimensional comodules $M\ne 0$ of zero dimension. Then the category ${\rm Corep}(H)$ satisfies the assumptions of Theorem [\[AKth\]](#AKth){reference-type="ref" reference="AKth"}. Therefore, we obtain

::: proposition
[]{#AK1 label="AK1"} There exists a unique universal cosemisimple Hopf algebra $\overline{H}$ with a surjective homomorphism $s: \overline{H}\to H$ (in other words, any Hopf algebra homomorphism $H'\to H$ from a cosemisimple Hopf algebra $H'$ uniquely factors through $s$). Namely, ${\rm Corep}(\overline{H})=\overline{{\rm Corep}(H)}$
:::

The proof is analogous to the case when $H$ is commutative over $\Bbb C$ (i.e., the case of proalgebraic groups). Heuristically writing $G={\rm Spec}(H)$ and $\overline{G}={\rm Spec}(\overline{H})$, we may say that the reductive quantum group $\overline{G}$ is the reductive envelope of the quantum group $G$.

::: example
Let $q$ be a transcendental number, or, more generally, a complex number which is not a root of any polynomial with positive integer coefficients, say a positive real number or its image under an automorphism of $\Bbb C$. Let $B_q$ be the quantum Borel subgroup of the quantum group $G_q$ attached to a simple complex algebraic group $G$. The category $\mathop{\mathrm{Rep}}\nolimits(B_q)={\rm Corep}(O(B_q))$ has a pivotal structure given by the element $q^{2\rho}$ of the corresponding quantum enveloping algebra. Therefore, the dimension (both left and right) of any nonzero representation of $B_q$ is a Laurent polynomial in $q$ with positive integer coefficients. Thus, this dimension is nonzero. Hence Proposition [\[AK1\]](#AK1){reference-type="ref" reference="AK1"} applies, and $H:=O(B_q)$ is the quotient of some cosemisimple Hopf algebra $\overline{H}:=O(\overline{B_q})$ for some reductive quantum group $\overline{B}_q$, such that every representation of $B_q$ factors canonically through $\overline{B_q}$.
:::

## Compatibility of semisimplification with equivariantization

Now let $\mathcal{C}$ be a tensor category and $L$ be a finite group acting on $\mathcal{C}$. Let $\mathcal{C}^L$ be the $L$-equivariantization of $\mathcal{C}$ ([@EGNO], Subsection 4.15). The following lemma is easy ([@EGNO], Exercise 4.15.3).

::: lemma
[]{#equivar label="equivar"} If $$1\to N\to G\to L\to 1$$ is an exact sequence of groups then $L$ acts naturally on $\mathop{\mathrm{Rep}}\nolimits_{\bold k} N$, and $(\mathop{\mathrm{Rep}}\nolimits_{\bold k} N)^L\cong \mathop{\mathrm{Rep}}\nolimits_{\bold k} G$.
:::

Clearly, any action of $L$ on $\mathcal{C}$ descends to its action on the semisimplification $\overline{\mathcal{C}}$.

::: proposition
[]{#commu label="commu"} If $|L|\ne 0$ in $\mathbf{k}$ and $L$ preserves the spherical structure of $\mathcal{C}$ then $L$-eqiuvariantization commutes with semisimplification. In other words, we have a natural equivalence of tensor categories $\overline{\mathcal{C}^L}\cong \overline{\mathcal{C}}^L$.
:::

::: proof
*Proof.* We have a natural forgetful functor $F: \mathcal{C}^L\to \mathcal{C}$. We claim that if $X,Y\in \mathcal{C}^L$ and $f: X\to Y$ is negligible, then $F(f)$ is negligible. Indeed, recall that $\mathrm{Hom}(F(X),F(Y))$ carries a natural action of $L$, and that $F$ defines an isomorphism $\mathrm{Hom}(X,Y)\cong \mathrm{Hom}(F(X),F(Y))^L$. Now let $h\in \mathrm{Hom}(F(Y),F(X))$, and let us show that $\text{Tr}(F(f)\circ h)=0$. Let $\overline{h}=|L|^{-1}\sum_{\gamma\in L}\gamma(h)$. Then $\overline{h}=F(g)$ for a unique $g\in \mathrm{Hom}(X,Y)$. Thus, since $F(f)$ commutes with $L$ and the action of $L$ preserves traces, we have $$\text{Tr}(F(f)\circ h)=\text{Tr}(F(f)\circ \overline{h})=\text{Tr}(F(f)\circ F(g))=0,$$ as desired. Thus, the functor $F$ descends to a tensor functor $\overline{F}: \overline{\mathcal{C}^L}\to \overline{\mathcal{C}}$. Moreover, for any $T\in \overline{\mathcal{C}^L}$ the object $\overline{F}(T)$ has a natural structure of an $L$-equivariant object (coming from that of $T$), so the functor $\overline{F}$ factors naturally through a tensor functor $E:  \overline{\mathcal{C}^L}\to \overline{\mathcal{C}}^L$.

Suppose $T\in \overline{\mathcal{C}^L}$ is simple. Then $T=\overline{X}$, where $X\in \mathcal{C}^L$ is an indecomposable object of nonzero dimension. Thus $X=\text{Ind}_{L_Z}^L(\rho\otimes Z)$, where $Z$ is an indecomposable object of $\mathcal{C}$ of nonzero dimension, $L_Z$ is the stabilizer of $Z$ in $L$, and $\rho$ is an irreducible representation of $L_Z$ over $\mathbf{k}$. Then $E(T)=\text{Ind}_{L_Z}^L(\rho\otimes \overline{Z})$. Thus, $E(T)$ is simple (since so is $\overline{Z}$, and $L_{\overline{Z}}=L_Z$).

It remains to show that $E$ is essentially surjective, i.e. every simple object of $\overline{\mathcal{C}}^L$ is of the form $E(T)$. To this end, note that every simple object of $\overline{\mathcal{C}}^L$ has the form $W=\text{Ind}_{L_V}^L(\rho\otimes V)$, where $V=\overline{X}$ is a simple object of $\overline{\mathcal{C}}$ and $\rho$ is an irreducible representation of $L_V$. Since $|L_V|\ne 0$ in $\mathbf{k}$, we have $\dim \rho\ne 0$ in $\mathbf{k}$. Hence, $W=E(T)$, where $T=\text{Ind}_{L_V}^L(\rho\otimes X)$ is a simple object of $\overline{\mathcal{C}^L}$ (as $L_V=L_X$). The proposition is proved. ◻
:::

::: corollary
[]{#commu2 label="commu2"} In the setup of Lemma [\[equivar\]](#equivar){reference-type="ref" reference="equivar"} assume that $|L|\ne 0$ in $\mathbf{k}$. Then $\overline{\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}G}\cong \overline{\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}N}^L$.
:::

::: proof
*Proof.* This follows from Proposition [\[commu\]](#commu){reference-type="ref" reference="commu"} and Lemma [\[equivar\]](#equivar){reference-type="ref" reference="equivar"}. ◻
:::

::: remark
Similarly to Theorem [\[karpiv\]](#karpiv){reference-type="ref" reference="karpiv"}, Proposition [\[commu\]](#commu){reference-type="ref" reference="commu"} and its proof generalizes to Karoubian pivotal categories satisfying the assumptions of Theorem [\[karpiv\]](#karpiv){reference-type="ref" reference="karpiv"}.
:::

## Compatibility of negligible morphisms with surjective tensor functors

Let $\mathcal{C},\mathcal{D}$ be finite spherical tensor categories ([@EGNO], Section 6), and $F: \mathcal{C}\to \mathcal{D}$ a surjective tensor functor ([@EGNO], Subsection 6.3). Let $I: \mathcal{D}\to \mathcal{C}$ be the right adjoint of $F$. Note that $I$ is exact since $F$ maps projectives to projectives, ([@EGNO], Theorem 6.1.16).

::: definition
The *index* of $F$ is $d:=\dim I(\bold 1)$.
:::

::: definition
Let us say that $I$ is *dimension-scaling* if $\dim I(V)=d\dim V$ for all $V\in \mathcal{D}$.
:::

::: proposition
[]{#negli label="negli"} If $F$ has a nonzero index and $I$ is dimension-scaling then

\(i\) $\dim F(Y)=\dim Y$ for all $Y\in \mathcal{C}$;

\(ii\) for any negligible morphism $f$ in $\mathcal{C}$, the morphism $F(f)$ is negligible in $\mathcal{D}$.
:::

::::: proof
*Proof.* We have a functorial isomorphism $\varepsilon_Y: I(F(Y))\to I(\bold 1)\otimes Y$. Indeed, $$\mathrm{Hom}(X,I(F(Y)))=\mathrm{Hom}(F(X),F(Y))=\mathrm{Hom}(F(X)\otimes F(Y)^*,\bold 1)=$$ $$\mathrm{Hom}(F(X\otimes Y^*),\bold 1)=
\mathrm{Hom}(X\otimes Y^*,I(\bold 1))=
\mathrm{Hom}(X,I(\bold 1)\otimes Y).$$ Since $I$ is dimension-scaling, we have $$d\dim F(Y)=\dim I(F(Y))=\dim (I(\bold 1)\otimes Y)=d \dim Y.$$ Since $d\ne 0$, this implies (i).

Now let us prove (ii). For this, note that if $f: X\to Y$ is a morphism in $\mathcal{C}$ then $\varepsilon_Y\circ I(F(f))\circ \varepsilon_X^{-1}={\rm Id}_{I(\bold 1)}\otimes f$. Hence the morphism $I(F(f))$ is negligible.

::: lemma
[]{#scaletrace label="scaletrace"} If $h: V\to V$ is a morphism in $\mathcal{D}$ then one has $\text{Tr}(I(h))=d\text{Tr}(h)$.
:::

::: proof
*Proof.* By decomposing $V$ into generalized eigenobjects of $h$, we may assume that $h$ has a single eigenvalue $\lambda$. Then $h=\lambda{\rm Id}+h_0$, where $h_0$ is nilpotent, so $I(h)=\lambda {\rm Id}+I(h_0)$. Since $I(h_0)$ is nilpotent, the desired statement reduces to the identity $\dim I(V)=d\dim V$ for all $V\in \mathcal{D}$, which holds since $I$ is dimension-scaling. ◻
:::

Now let $g: F(Y)\to F(X)$ be a morphism. Then by Lemma [\[scaletrace\]](#scaletrace){reference-type="ref" reference="scaletrace"}, $$d\text{Tr}(F(f)\circ g)=\text{Tr}(I(F(f)\circ g))=\text{Tr}(I(F(f))\circ I(g)).$$ But this is zero, since $I(F(f))$ is negligible. Since $d\ne 0$, this implies that $\text{Tr}(F(f)\circ g)=0$, i.e., $F(f)$ is negligible, yielding (ii). ◻
:::::

Proposition [\[negli\]](#negli){reference-type="ref" reference="negli"} immediately implies

::: corollary
[]{#desc label="desc"} If $F$ has a nonzero index and $I$ is dimension-scaling then $F$ descends to a tensor functor $\overline{F}: \overline{\mathcal{C}}\to \overline{\mathcal{D}}$.
:::

Now let $H$ be an involutive finite dimensional Hopf algebra over any algebraically closed field $\mathbf{k}$ (i.e., $S^2=\text{Id}$, where $S$ is the antipode of $H$), and $K$ be a Hopf subalgebra in $H$; for example, $H$ is cocommutative (e.g., a group algebra). Then $\mathcal{C}=\mathop{\mathrm{Rep}}\nolimits H$ and $\mathcal{D}=\mathop{\mathrm{Rep}}\nolimits K$ are finite spherical tensor categories, where dimensions are the usual dimensions (projected to $\mathbf{k}$). Restriction from $H$ to $K$ defines a surjective tensor functor $F: \mathcal{C}\to \mathcal{D}$. Let $I: \mathop{\mathrm{Rep}}\nolimits(K)\to \mathop{\mathrm{Rep}}\nolimits(H)$ be the right adjoint to this functor, i.e., the induction functor, $I(V)=\mathrm{Hom}_K(H,V)$.

Recall that by the Nichols-Zoeller theorem [@NZ], $H$ is a free $K$-module, of some rank $d$.

::: corollary
[]{#invo label="invo"} Assume that $d\ne 0$ in $\mathbf{k}$. Then any negligible morphism $f: X\to Y$ of $H$-modules is also negligible as a morphism of $K$-modules. Thus, $F$ defines a tensor functor: $\overline{\mathop{\mathrm{Rep}}\nolimits H}\to \overline{\mathop{\mathrm{Rep}}\nolimits K}$.
:::

::: proof
*Proof.* We have $\dim I(V)=d\dim V$, i.e., $I$ is dimension-scaling. Thus, the result follows from Proposition [\[negli\]](#negli){reference-type="ref" reference="negli"}. ◻
:::
