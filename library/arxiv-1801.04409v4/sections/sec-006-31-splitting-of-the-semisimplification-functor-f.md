---
doc_id: arxiv-1801.04409v4
doc_title: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES"
section_id: sec-006-31-splitting-of-the-semisimplification-functor-f
section_title: "Splitting of the semisimplification functor for Tannakian categories in characteristic zero, reductive envelopes, and the Jacobson-Morozov lemma"
section_number: 3.1
pages: 8-13
source_pdf: 1801.04409v4.pdf
source_sha256: db61d011e3775aca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.988
doc_brief: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES — We develop the theory of semisimpliﬁcations of ten- sor categories deﬁned by Barrett and Westbury."
---
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

::: example
Consider the special case $G=\Bbb G_a$. In this case the indecomposable representations of $G$ are unipotent Jordan blocks $J_n$ of sizes $n=1,2,3...$, so it is easy to see that $\overline{\mathop{\mathrm{Rep}}\nolimits G}\cong \mathop{\mathrm{Rep}}\nolimits SL(2)$ (as the Grothendieck ring of $\overline{\mathop{\mathrm{Rep}}\nolimits G}$ coincides with that of $\mathop{\mathrm{Rep}}\nolimits SL(2)$, and the dimensions of nonzero objects of $\overline{\mathop{\mathrm{Rep}}\nolimits G}$ are positive). So in this case the existence of $\overline{G}$ is easy (namely, $\overline{G}=SL(2)$), and the existence of the splitting $\bold S^*$ is also straightforward (namely, $\bold S^*$ is induced by the standard inclusion $\psi_G: \Bbb G_a\hookrightarrow SL(2)$ as upper triangular matrices with ones on the diagonal). Thus, Theorem [\[ak\]](#ak){reference-type="ref" reference="ak"} in this case tells us that any homomorphism $\phi: \Bbb G_a\to L$ for a reductive proalgebraic group $L$ uniquely (up to conjugacy) factors through a homomorphism $\widetilde{\phi}: SL(2)\to L$. As pointed out in [@AK; @S], this implies the celebrated *Jacobson-Morozov Lemma*:

::: proposition
Let $L$ be a reductive algebraic group over $\mathbf{k}$, and $u\in L$ a unipotent element. Then there exists a homomorphism $\theta: SL(2)\to L$ such that $\theta\left(\begin{matrix} 1&1\\ 0&1\end{matrix}\right)=u$. Moreover, $\theta$ is unique up to conjugation by the centralizer $Z_u$ of $u$.
:::

::: proof
*Proof.* Let $G$ be the 1-parameter unipotent subgroup of $L$ generated by $u$, and $\phi: G\to L$ be the corresponding embedding. Identify $G$ with $\Bbb G_a$ by sending $u$ to $1$. Then it remains to apply Theorem [\[ak\]](#ak){reference-type="ref" reference="ak"} and set $\theta=\widetilde\phi$. ◻
:::
:::

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
