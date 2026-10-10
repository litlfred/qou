---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-017-18-examples-of-fusion-categories-with-different-na
section_title: "Examples of fusion categories with different natural integral wdf"
section_number: 18
pages: 119-121
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
doc_brief: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem — We construct, for every complex simple Lie algebra g and every positive integer level k, a unitary modular"
---
18. Examples of fusion categories with different natural integral wdf
Motivated by Remark 17.4, it is natural to ask whether a given fusion category C may
admit more than one weak integral dimension function corresponding to a weak Hopf
algebra. In this subsection we construct examples indicating that this eventuality occurs.
The first class of examples is associated to pointed fusion categories over the cyclic group
ZN and relies on the basic example AW (slN , q, ℓ) for the minimal value of ℓ. The second
example shows that already for Z2 there are infinitely many weak dimension functions of
this kind, and are obtained using the general constructions of Sect. 9. We shall need the
ribbon structure naturally associated to the R-matrix of C(slN , q, ℓ). These formulas will
be recalled in the next section.
Example 18.1. Let G be a finite group and ω ∈ H3(G, C
×). The pointed fusion category
Vecω
G admits the natural dimension function taking value 1 on every irreducible and the
associated quasi-Hopf algebra is Fun(G, C)ω, see Example 5.13.6 in [50]. In particular, we
obtain a Hopf algebra if and only if ω is trivial in H3(G, C
×). We next see that for G = ZN
and ω = 1 for N odd (ω = −1 for N even) this fusion category may also be described as
the representation category of AW = AW (slN , q, N + 1). In other words, if g denotes the
natural generator of ZN , D(g) = N corresponds to a weak Hopf algebra.
Consider the fusion category C(slN , q, ℓ) for q = e
iπ/N+1 and let X denote the object corresponding to the vector representation of Uq(slN ). We have d(X) = 1 and the
Grothendieck ring Gr(C(slN , q)) is ZZN with basis given by the objects X = XΛ1, . . . , XΛN−1
corresponding to the fundamental weights. The fusion rules are given by Xk = XΛkfor
k ≤ N − 1 and XN = 1 [110]. It follows that C(slN , q) is tensor equivalent to Vecω
ZN
for
some ω ∈ H3(ZN , T), cf. Ex. 7.12. Hence in particular Vecω
ZN
admits a weak dimension
function as required, and we are left to determine ω. The group H3(ZN , T) is isomorphic
to the cyclic group ZN , that we write in multiplicative notation. An explicit isomorphism
associates the N-th root of unity w to the 3-cocycle ω is given by (25.1). For the category
C(slN , q, ℓ) the corresponding w may be determined following the procedure at the end
of page 126 in [110]. In this case, the middle map is identity since the category is strict.
Taking into account the equation appearing in Prop. A.5 in [25] with the additional information that S is an isomorphism for the minimum value of the level, we find that ω = 1
for N odd and ω = −1 for N even.

120 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Alternatively, we may determine ω in a more direct way as follows. On one hand it is
not difficult to see that the only possible values are ω = ±1. (We shall see a more general
statement for higher levels in Prop. 25.9.) On the other, by the general criterion in Exercise
8.4.11 (iii) pag. 206 in [50], if a pointed fusion category Vecω
G is braided with braiding c then
ω = 1 if and only if for any element γ ∈ G of order some power of 2, say 2r, the associated
quadratic form q(γ) = c(Y, Y ), with Y simple of class γ, is of order ≤ 2
r
. This immediately
leads to triviality of ω if N is odd. For N even we use the fact that q(XΛk
) equals the
ribbon structure θXΛk
, see Subsect. 25.1, and that θXΛk
= q
k(N−k)(N+1)
N = e
iπk(N−k)
N , by the
proof of Prop. 25.15. Writing N = 2rh with h an odd integer, it follows that Λh has order
N
h = 2r but q(XΛh
)
p ̸= 1 for all 1 ≤ p ≤ 2r
.
Example 18.2. We give examples of infinitely many weak dimension functions corresponding to weak Hopf algebras on the fusion categories Vecω
Z2
. They are given by
D(g) = 2h + 1 for VecZ2 and D(g) = 2h for Vec−1
Z2
, for h ≥ 1, with g the group generator and ω ∈ H3
(Z2, T) ≃ Z2.
Consider the fusion category C(sl2, q, ℓ) with q = e
iπ/ℓ and ℓ ≥ 3, and the associated
Grothendieck ring (the Verlinde ring) R2,ℓ with basis given by the equivalence classes of
selfconjugate irreducible objects X0 = I, X1, . . . , Xk. Fusion rules are given by XiXj = Pmin{i,j}
max{i+j−k,0} Xi+j−2r, see [24, 50]. The element X = Xk satisfies X2 = I, so it generates
a pointed full fusion subcategory Ck ≃ Vecω
Z2
. We determine ω ∈ {±1} by means of
Ex. 8.4.11 iii) in [50] again, so in this case ω = 1 precisely when the quadratic form
q(g) = c(X, X) associated to restricted braiding of Ck satisfies q(g) = 1 or q(g)
2 = 1.
Arguments similar to those of the previous example give q(g) = θX, with θ the usual
ribbon structure of c, whose value on X = Xk is θX = q
k(k+2)/2 = eiπk/2
cf. Prop. 25.15.
It follows that ω = 1 if and only if k is even. On the other hand, C(sl2, q, ℓ) is tensor
equivalent to the representation category of AW (sl2, q, ℓ) so Ck is tensor equivalent to a
quotient weak Hopf algebra A → Bk by Cor. 9.11. Since X corresponds to a representation
of A of dimension k + 1, we have Bk = C ⊕ Mk+1(C) and a weak dimension function D on
Ck, and therefore on Vecω
Z2
as required.
Example 18.3. The methods of the above examples may be combined to construct more
examples of weak Hopf algebras. a) For example, if g ∈ ZN is the natural generator, for
k ≤ N − 1, g
k generates a cyclic subgroup of order M =
N
gcd{k,N}
. Therefore the full
subcategory of C(slN , q, ℓ) for q = e
iπ/N+1 generated by XΛk
, which is pointed over ZM,
corresponds to a quotient of AW (slN , q, N + 1) (with dimension of the natural generator
of ZM given by D(h) = N
k

) and also to AW (slM, q, M + 1) (with dimension D′(h) = M)
with a possibly twisted associator. b) The even subcategory of C(sl2, q, ℓ) for q = e
iπ/ℓ is
an example of non-pointed full fusion subcategory, and therefore it gives rise to a quotient
weak Hopf algebra B = C⊕M2 ⊕M4 . . . . c) More information on full fusion subcategories
of C(slN , q, ℓ) for q = e
iπ/ℓ may be found in [166].
Remark 18.4. Ribbon structures first appeared as statistics phases for WZW and coset
models in conformal field theory. Some formulae for the statistics phases, including the

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 121
automorphism case of interest in Ex. 18.2, have been generalized by Rehren in the framework of conformal nets. Most importantly, in that paper the author derives the axioms
of a modular category extending previous work for certain conformal models [153] and
references therein. The ribbon structure in the conformal net approach to CFT is given
by θX = e
2πihX with hX the minimal eigenvalue of the conformal Hamiltonian L0 in the
irreducible representation X, by the conformal spin and statistics theorem [79]. In the
framework of vertex operator algebras one has an analogous formula [90, 92, 93].
Remark 18.5. In the setting of rigid tensor C
∗
-categories with infinitely many simple
objects, Van Daele and Wang constructed compact quantum groups Ao(F) associated to
an invertible matrix F with rk(F) ≥ 2 satisfying suitable properties [175], which reduce
to Woronowicz compact quantum groups SUq(2) for rk(F) = 2. For a given q > 1,
Rep(Ao(F)) turns out to be tensor equivalent to Rep(SUq(2)) with q suitably determined
by F [7, 8]. It follows that Rep(SUq(2)) admits the (non-weak) dimension function taking
the generating representation to the rank of F. Note that only finitely many (non-weak)
integral dimension functions arise in this way. This follows from the fact that rk(F) is
bounded above by the quantum dimension [190]. In this setting, it is important to recall
the remarkable work by Neshveyev and Yamashita on the classification of compact quantum
groups that beyond the fusion rules, share the integral dimensions with a given compact
simple simply connected Lie group G, see [142] and references therein.
