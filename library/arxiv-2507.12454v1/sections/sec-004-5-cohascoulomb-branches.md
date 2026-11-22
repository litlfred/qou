---
doc_id: arxiv-2507.12454v1
doc_title: "Cohomology rings of character varieties"
section_id: sec-004-5-cohascoulomb-branches
section_title: "COHAs/Coulomb branches"
section_number: 5
pages: 15-17
source_pdf: 2507.12454v1.pdf
source_sha256: 156fd9080847b4e7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.968
doc_brief: "Cohomology rings of character varieties — In this talk I give an introduction and present some recent progress towards understanding the cohomology rings of character varieties of Riemann surfaces"
---
In order to explain our approach we need to introduce some ideas.

## Cohomological Hall Algebra (COHA)

Denote by $\mathscr{H}_2$ the Lie algebra of Poisson vector fields on $\mathbb{C}^2$. Explicitly, it is the Lie algebra with basis elements $T_{r,s}$ for each pair $r,s\geq 0$, corresponding to the vector field with Hamiltonian $x^r y^s$. It is convenient not to impose $T_{0,0}=0$, although the corresponding vector field vanishes. The Lie bracket is given as follows: $$[T_{r,s}, T_{r',s'}] = (r's - r s') T_{r+r'-1,s+s'-1}\qquad(r,s\geq 0).$$ The tensor product $\mathscr{H}_2 \otimes H^*(C)$ is naturally a super-Lie algebra. Let $H^*(X)[x,y]$ be the cohomology ring with two formal variables $x$, $y$ adjoined. Let $n$ and $d$ be the rank and the degree of the Higgs bundles parameterized by the moduli space $X$, and let $\chi:=d + (1-g)n$ be the Euler characteristic.

::: theorem
The Lie algebra $\mathscr{H}_2 \otimes H^*(C)$ acts on $H^*(X)[x,y]$ in such a way that $T_{0,m}\otimes \xi$ satisfies $$\left((T_{0,m}\otimes \xi) f\right)(0,0) = \psi_m(\xi)(f) := \left(p_m(\xi) + m(1-g) p_{m-1}(\xi\cup \mathrm{pt})\right)\cup f \qquad (f\in H^*(X))$$ and $T_{1,0}\otimes \mathrm{pt}$, $T_{1,0}\otimes 1$, $T_{0,1}\otimes \mathrm{pt}$, $T_{0,1}\otimes 1$ act as $x$, $-n \frac{\partial}{\partial y}$, $y$, $n \frac{\partial}{\partial x} + \chi$ respectively.
:::

Here $p_m(\xi)$ is defined similarly to $e_m(\xi)$ in [\[eq:definition e\]](#eq:definition e){reference-type="eqref" reference="eq:definition e"}, except that we use the power sums of the Chern roots, i.e. $m!$ times the $m$-th component of the Chern character. Thus for instance, the central operator $T_{0,0}\otimes\mathrm{pt}$ acts via the multiplication by the rank of the Higgs bundles $n$. The operator $T_{0,1}\otimes\mathrm{1}$ commutes with $y$ and acts on elements of $H^*(X)[y]$ via the multiplication by $d+(1-g)n = \chi$.

Note that quadratic Hamiltonians correspond to the linear action of $SL(2,\mathbb C)$ on $\mathbb C^2$, and so the elements $T_{2,0}$, $T_{1,1}$ and $T_{0,2}$ span a copy of $\mathfrak{sl}_2\subset \mathscr{H}_2$. In fact it is this $\mathfrak{sl}_2$ that was matched with the relative Lefschetz $\mathfrak{sl}_2$ in [@hausel2022p] in order to pin down the perverse filtration algebraically.

## Coulomb branch

The construction described in [@braverman2018towards] associates to a pair of a reductive group $G$ and its representation $N$ an affine Poisson algebraic variety called the Coulomb branch. We are interested in the situation where $G=GL_n\times \mathbb C^*$ acts on the space of matrices $N=\mathbb C^{n\times n}$: $GL_n$ acts by conjugation and $\mathbb C^*$ by the scalar multiplication. Then Higgs bundles can be seen as maps from the curve $C$ to the stack $N/G$. Our hope is that the Coulomb branch has something to do with the cohomology of our moduli spaces. This is the situation of the adjoint representation with flavor and the Coulomb branch is related to the Hilbert scheme ([@braverman2021line]) of $\mathbb C^*\times \mathbb C$, which is a symplectic resolution of singularities of $(\mathbb C^*\times \mathbb C)^n / S_n$. It is not completely clear why we should pass to the Hilbert scheme of $\mathbb C^2$, but our construction in [@hausel2022p], in fact first produces an algebra of Hamiltonian fields on $\mathbb C^*\times\mathbb C$, and only then it is degenerated to the algebra for $\mathbb C^2$. Hopefully, this passage will be clarified by experts in Coulomb branches.

Now suppose we are on $\mathrm{Hilb}^n(\mathbb C^2)$. Then $\mathscr{H}_2$ acts on many natural objects such as functions, differential forms etc. So even if we do not completely understand the Coulomb branch picture, it is a natural guess to look for our model of the cohomology ring among natural objects living on the Hilbert scheme.

## Geometric engineering

An indication similar to the one above is given in [@chuang2015parabolic], where a physical explanation of Conjecture [\[conj:partition function conjecture\]](#conj:partition function conjecture){reference-type="ref" reference="conj:partition function conjecture"} is provided via interpreting the left hand side (the partition function) as $$\label{eq:geometric engineering}
        \Omega = \chi(\mathrm{Hilb}_n(\mathbb{C}^2), P^{\otimes k} \otimes (\Omega^{*})^{\otimes g}\otimes O(g-1)).$$ Here $P$ is the Procesi bundle ($S_n$-equivariant bundle coming from Haiman's identification $\mathrm{Hilb}_n(\mathbb{C}^2)=S_n-\mathrm{Hilb}(\mathbb{C}^{2n})$), $\Omega^*$ is the bundle of differential forms, $\chi$ denotes the equivariant Euler characteristic.

## Proposal

One problem with [\[eq:geometric engineering\]](#eq:geometric engineering){reference-type="eqref" reference="eq:geometric engineering"} is that the right hand side does not always have positive coefficients. So the vector bundle on the right hand side of [\[eq:geometric engineering\]](#eq:geometric engineering){reference-type="eqref" reference="eq:geometric engineering"} has higher cohomologies. Thus there seem to be no way to upgrade the identity [\[eq:partition function conjecture\]](#eq:partition function conjecture){reference-type="eqref" reference="eq:partition function conjecture"} to an isomorphism between vector spaces using [\[eq:geometric engineering\]](#eq:geometric engineering){reference-type="eqref" reference="eq:geometric engineering"}. One can trace the problem to the fact that the factor $-\frac{1}{(1-q)(1-t)}$ is manifestly not positive, when expanded in $q$ and $t$. To resolve this issue we propose to expand in $q^{-1}$ and $t$ instead. Geometric meaning of this expansion is different from taking the global sections. Instead, we should take the local cohomology with respect to a Lagrangian subvariety.

::: theorem
Let $L\subset \mathrm{Hilb}_n(\mathbb{C}^2)$ be the Lagrangian cut out by the equations $\sum_{i=1}^n x_i^r=0$ ($r>0$). Let $\mathcal{E}$ be any vector bundle on $\mathrm{Hilb}_n(\mathbb{C}^2)$. Then for any $i\neq n$ we have $$H^i_L(\mathrm{Hilb}_n(\mathbb{C}^2), \mathcal{E})=0.$$
:::

Here $H^i_L$ is the functor of local cohomology (see [@hartshorne1967local]), the derived functor to the functor of taking sections supported at $L$. Then we expect that [\[eq:partition function conjecture\]](#eq:partition function conjecture){reference-type="eqref" reference="eq:partition function conjecture"} has the following interpretation:

::: conjecture
$H^n_L(P^{\otimes k} \otimes (\Omega^{*})^{\otimes g}\otimes O(g-1))\;\check{}\; \cong H_*^{\mathrm{BM}}(\text{Higgs moduli stack}).$
:::

Here it is not clear which precise Higgs moduli stack should be taken on the right hand side. The whole Higgs moduli stack has infinitely many irreducible components and the expectation is that we need to take a nice open substack containing only finitely many components in each degree, possibly imposing a bound on the slope. For a bigraded vector space $M$ we denote by $M\;\check{}\;$ the bigraded dual vector space.
