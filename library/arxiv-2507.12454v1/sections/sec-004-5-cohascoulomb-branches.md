---
doc_id: arxiv-2507.12454v1
doc_title: "COHOMOLOGY RINGS OF CHARACTER VARIETIES ANTON MELLIT"
section_id: sec-004-5-cohascoulomb-branches
section_title: "COHAs/Coulomb branches"
section_number: 5
pages: 15-17
source_pdf: 2507.12454v1.pdf
source_sha256: 156fd9080847b4e7
doc_brief: "COHOMOLOGY RINGS OF CHARACTER VARIETIES ANTON MELLIT — In this talk I give an introduction and present some recent progress towards understanding the cohomology rings of character varieties of"
---
In order to explain our approach we need to introduce some ideas.
5.1. Cohomological Hall Algebra (COHA). Denote by H2 the Lie algebra of Poisson
vector fields on C2. Explicitly, it is the Lie algebra with basis elements Tr,s for each pair
r,s≥ 0, corresponding to the vector field with Hamiltonian xrys. It is convenient not to
imposeT0,0 = 0, although the corresponding vector field vanishes. The Lie bracket is given
as follows:
[Tr,s,Tr′,s′] = (r′s−rs′)Tr+r′−1,s+s′−1 (r,s≥ 0).
The tensor product H2⊗H∗(C) is naturally a super-Lie algebra. Let H∗(X)[x,y ] be the
cohomology ring with two formal variables x,y adjoined. Let n andd be the rank and the
degree of the Higgs bundles parameterized by the moduli spaceX, and letχ :=d+(1−g)n
be the Euler characteristic.
Theorem 5.1 ([HMMS22], [MMSV23]). The Lie algebra H2⊗H∗(C) acts on H∗(X)[x,y ]
in such a way that T0,m⊗ξ satisfies
((T0,m⊗ξ)f) (0, 0) =ψm(ξ)(f) := (pm(ξ) +m(1−g)pm−1(ξ∪ pt))∪f (f∈H∗(X))
and T1,0⊗ pt, T1,0⊗ 1, T0,1⊗ pt, T0,1⊗ 1 act as x,−n ∂
∂y , y, n ∂
∂x +χ respectively.
Here pm(ξ) is defined similarly to em(ξ) in (4.1), except that we use the power sums
of the Chern roots, i.e. m! times the m-th component of the Chern character. Thus for
instance, the central operator T0,0⊗ pt acts via the multiplication by the rank of the Higgs
bundles n. The operator T0,1⊗ 1 commutes with y and acts on elements of H∗(X)[y] via
the multiplication by d + (1−g)n =χ.
Note that quadratic Hamiltonians correspond to the linear action ofSL(2, C) on C2, and
so the elements T2,0, T1,1 and T0,2 span a copy of sl2⊂ H2. In fact it is this sl2 that was
16 ANTON MELLIT
matched with the relative Lefschetz sl2 in [HMMS22] in order to pin down the perverse
filtration algebraically.
5.2. Coulomb branch. The construction described in [BFN18] associates to a pair of a
reductive group G and its representation N an affine Poisson algebraic variety called the
Coulomb branch. We are interested in the situation whereG =GLn× C∗ acts on the space
of matricesN = Cn×n: GLn acts by conjugation and C∗ by the scalar multiplication. Then
Higgs bundles can be seen as maps from the curve C to the stack N/G. Our hope is that
the Coulomb branch has something to do with the cohomology of our moduli spaces. This
is the situation of the adjoint representation with flavor and the Coulomb branch is related
to the Hilbert scheme ([BFN21]) of C∗× C, which is a symplectic resolution of singularities
of (C∗× C)n/Sn. It is not completely clear why we should pass to the Hilbert scheme of
C2, but our construction in [HMMS22], in fact first produces an algebra of Hamiltonian
fields on C∗× C, and only then it is degenerated to the algebra for C2. Hopefully, this
passage will be clarified by experts in Coulomb branches.
Now suppose we are on Hilb n(C2). Then H2 acts on many natural objects such as
functions, differential forms etc. So even if we do not completely understand the Coulomb
branch picture, it is a natural guess to look for our model of the cohomology ring among
natural objects living on the Hilbert scheme.
5.3. Geometric engineering. An indication similar to the one above is given in [CDDP15],
where a physical explanation of Conjecture 4.5 is provided via interpreting the left hand
side (the partition function) as
(5.1) Ω = χ(Hilbn(C2),P⊗k⊗ (Ω∗)⊗g⊗O(g− 1)).
Here P is the Procesi bundle ( Sn-equivariant bundle coming from Haiman’s identifica-
tion Hilbn(C2) = Sn− Hilb(C2n)), Ω∗ is the bundle of differential forms, χ denotes the
equivariant Euler characteristic.
5.4. Proposal. One problem with (5.1) is that the right hand side does not always have
positive coefficients. So the vector bundle on the right hand side of (5.1) has higher coho-
mologies. Thus there seem to be no way to upgrade the identity (4.3) to an isomorphism
between vector spaces using (5.1). One can trace the problem to the fact that the factor
− 1
(1−q)(1−t) is manifestly not positive, when expanded in q and t. To resolve this issue we
propose to expand in q−1 and t instead. Geometric meaning of this expansion is different
COHOMOLOGY RINGS OF CHARACTER V ARIETIES 17
from taking the global sections. Instead, we should take the local cohomology with respect
to a Lagrangian subvariety.
Theorem 5.2 (M.-Romero, in preparation). LetL⊂ Hilbn(C2) be the Lagrangian cut out
by the equations Pn
i=1xr
i = 0 (r >0). Let E be any vector bundle on Hilbn(C2). Then for
any i̸=n we have
Hi
L(Hilbn(C2),E) = 0.
Here Hi
L is the functor of local cohomology (see [Har67]), the derived functor to the
functor of taking sections supported at L. Then we expect that (4.3) has the following
interpretation:
Conjecture 5.3. Hn
L(P⊗k⊗ (Ω∗)⊗g⊗O(g− 1))ˇ∼=HBM
∗ (Higgs moduli stack).
Here it is not clear which precise Higgs moduli stack should be taken on the right hand
side. The whole Higgs moduli stack has infinitely many irreducible components and the
expectation is that we need to take a nice open substack containing only finitely many
components in each degree, possibly imposing a bound on the slope. For a bigraded vector
space M we denote by M ˇ the bigraded dual vector space.
