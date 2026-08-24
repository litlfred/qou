---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS IV AN SMITH"
section_id: sec-030-55-finite-determinacy
section_title: "Finite determinacy"
section_number: 5.5
pages: 62-67
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry bet ween a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
exterior algebra A = Λ ∗(V ). Suppose now V ∼= C3 is 3-dimensional, so A has graded summands
A0 = C⊕ Λ 2(V ); A1 =V⊕ Λ 3(V ).
According to [93, Theorem 3.3], the L∞-quasi-isomorphism Φ of Theorem 3.18 has linear term
Φ 1 which is given by restricting elements of Hom(Λ(V )⊗i, Λ(V )) to the subspace of symmetric
elements of Hom(V ⊗i, Λ(V )) (this is the Hochschild-Kostant-Rosenberg map). Since V is in odd
degree, αi(v1,...,v i)∈ Λ 0⊕ Λ 2 for all i and any vj∈V . In other words, taking the parities of
the αi into consideration, a Maurer-Cartan element comprises a pair
(W,η )∈ C[[V ∨]]⊕ C[[V ∨]]⊗ Λ 2(V )
of a formal function and a formal 2-form, satisfying
[W,W ] = 0; [ η,η ] = 0; [ W,η ] = 0.
Since the given A∞-structure does not deform the algebra structure on Λ( V ), we may suppose
thatW andη have no coeﬃcients of polynomial degree < 3. Note that the equation [ W,W ] = 0
always holds, since the Schouten bracket on polyvector ﬁelds involv es contraction of the diﬀeren-
tial form, hence vanishes identically on 0-forms. In particular, any formal function W together
with the trivial 2-form (W, 0) deﬁnes a Z2-gradedA∞-structure on Λ( C3). Gauge transformations
are now by pairs
(g1,g 3)∈
(
C[[V ∨]]⊗ Λ 1(V )
)
⊕
(
C[[V ∨]]⊗ Λ 3(V )
)
.
For vector ﬁelds vanishing at the origin the ﬁrst term acts on both c omponents (W,η ), by pullback
by the diﬀeomorphism obtained from exponentiating the vector ﬁeld . Explicitly, a vector ﬁeld
g1 acts on a formal function through the adjoint action
exp(g1)·W = W +
∑
n≥0
ad(g1)n
(n + 1)! [g1,W ] (5.9)
The second term acts by interior contraction
(0,g 3)· (W,η ) = ( W,η +ιdW (g3)). (5.10)
In this language, we can re-express the outcome of the previous s ection. Pick co-ordinates
ξ1,ξ 2,ξ 3 on V and dual co-ordinates ( v1,v 2,v 3) on V ∨∼= C3. Write O(k) for power series all
of whose terms have degree ≥ k. The action of G = Z2g+1 on V comes geometrically from the
rotation action on P1 permuting Lagrangian pentagram spheres, so the generator of G acts on
the hyperelliptic curve
y2 =z(z2g+1− 1) via ( y,z )↦→(ξg+1y,ξz ), with ξ =e
2iπ
2g+1.
Via Lemma 5.11, there is a basis with respect to which G acts on V by diagonal matrices with
entries which are non-trivial roots of unity; explicitly, there is a bas is for which G acts via the
diagonal matrix with entries ( ξ,ξ,ξ 2g−1).
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 63
Lemma 5.24. The formal function W deﬁning the A∞-structure on A(Z) has the form
W =λv1v2v3 +O(4) or W =λ(v2
1 +v2
2)v3 +O(4).
for some non-zero λ∈ C∗.
Proof. The generators vi of the exterior algebra correspond, up to scale, to the Floer gene rators
e +f,e −f,p of Section 5.4. Hyperelliptic invariance, exchanging f and−f , corresponds to
invariance under v1↔v2. Corollary 5.22 implies that either the term v1v2v3 in W has non-zero
coeﬃcient, or the term v2
1v3 (and hence by symmetry v2
2v3) has non-zero coeﬃcient. Moreover,
these two cases are mutually exclusive. The two cases cover the on ly possible cubic terms in W ,
by Z2g+1-invariance, which gives the result. □
We now explore more systematically the constraints imposed by Z2g+1-equivariance. One
can consider only G-equivariant Z2-graded A∞-structures on Λ( V ) by imposing G-equivariance
throughout the preceding discussion; in particular, the inverse Φ t o Kontsevich’s map Ψ gives
a quasi-isomorphism between equivariant Hochschild cochains and eq uivariant polyvector ﬁelds,
and G-equivariant gauge transformations act on the set of such G-equivariant Maurer-Cartan
solutions.
As in Section 3.6, Lemma 3.17 and the Formality Theorem 3.18 imply that t he Hochschild
cohomology of a Z2-graded A∞-structure on Λ( V ) deﬁned by a pair ( W,η ) is given by the
cohomology of the Z2-graded complex
C[[V ∨]]⊕ (C[[V ∨]]⊗ Λ 2(V ))
[·,η]⊕[·,W +η]
−−−−−−−−−−⇀↽−−−−−−−−−−
[·,W +η]⊕[·,W ]
(C[[V ∨]]⊗ Λ 1(V ))⊕ (C[[V ∨]]⊗ Λ 3(V )) (5.11)
noting that ξ ↦→[ξ,W ] = ιdW (ξ) vanishes on 0-forms, and similarly ξ ↦→[ξ,η ] vanishes on
3-forms, for degree reasons. The group HH ∗(A, A)Z2g+1 is computed by the complex
(C[[V ∨]]⊗ Λ ev(V )))Z2g+1 [·,W +η]
−−−−−−⇀↽−−−−−−
[·,W +η]
(
C[[V ∨]]⊗ Λ odd(V )
)Z2g+1
(5.12)
Note that 1 ∈ C[[V ∨]] always deﬁnes a non-trivial class in HH ev, since HH ∗ is a unital ring.
Therefore, Corollary 5.6 implies that in our case there is precisely one other non-trivial class.
The Maurer-Cartan equation implies that both W and η are themselves cocycles, so some some
linear combination of them must be a coboundary. The force of Lemm a 5.24 is that we can prove
that η is in fact already a coboundary in the Koszul complex associated to W .
The Koszul complex of a holomorphic function W is acyclic in degrees greater than the di-
mension of the critical locus of W , see [22, Ch. 6, Prop. 2.21]. The underlying acyclicity result
applies more generally to complexes of ﬁnitely generated free module s over a Noetherian local
ring R, which is useful in the context of formal rather than holomorphic f unctions. Indeed, [18,
Corollary 1] or [30, Section 20.3] says that a complex of free R-modules
0→Fn
φn
−− →Fn−1
φn−1
−−−→···→F2
φ2
−→F1
is exact if and only if
(1) rk(Fk) = rk(φk) + rk(φk+1) and
(2) the depth of the ideal I(φk)≥k− 1
for k = 2 ,...,n . Here, the rank of φk is the size of the largest non-vanishing minor in a
matrix representing φk, and I(φk) is the ideal in R generated by the determinants of all r×r
minors, where r = rk(φk). C[[v1,v 2,v 3]] is Noetherian [6, Corollary 10.27] and Cohen-Macaulay.
In a Cohen-Macaulay ring, depth of an ideal (maximal length of a reg ular sequence) equals its
codimension [30, Theorem 18.2], and the criterion above, applied to th e Koszul complex truncated
in degree >k of a holomorphic W with critical set of dimension k, recovers the familiar acyclicity
64 IV AN SMITH
result stated previously. Taking W to be a formal function in 3 variables, we would like to know
when the truncated complex
0→ Λ 3 [·,dW ]
−−−−→Λ 2 [·,dW ]
−−−−→Λ 1
is acyclic, with Λ i the free module of rank
(3
i
)
overR = C[[v1,v 2,v 3]]. It is easy to check that
wheneverW⁄= 0, the ﬁrst condition on the ranks of the maps and modules is satisﬁ ed. Since R
contains no zero-divisors, depth I(φ2)≥ 1 is trivial, so the key condition is
depthI(φ3)≥ 2.
This certainly holds if one can order the partial derivatives ( ∂iW,∂ jW,∂ kW ) in such a way that
some linear combination u.∂iW +v.∂jW is not a zero-divisor in R/⟨∂kW⟩. If u∂iW +v∂jW is
such a zero-divisor, then
φ· (u∂iW +v∂jW ) = ψ∂kW
for some formal functions φ,ψ with∂kW⁄|φ. Since R is moreover a unique factorisation domain,
this can happen for all u, v only if the partial derivatives share a common irreducible factor
(which is not a unit, so has vanishing constant term). However, this is precluded by Lemma 5.24.
We deduce:
Lemma 5.25. A(Z) is deﬁned by a Maurer-Cartan pair (W,η ) for which η is a coboundary in
the Koszul complex associated to W , so there is some formal 3-form g3 for which [g3,dW ] = η.
We can therefore apply a gauge transformation as in Equation 5.10 t o kill η, so up to gauge
equivalence, the A∞-structure on Z is deﬁned by a formal function W satisfying Lemma 5.24,
together with the trivial 2-form. Gauge transformations of A∞-structures induce the identity
on cohomology. There are also A∞-equivalences which act non-trivially on cohomology; in par-
ticular, A∞-structures on Λ( V ) ⋊G are invariant under G-equivariant linear transformations in
GL(V ). Since the cubic polynomials
v1v2v3 and ( v2
1 +v2
2)v3
are related by a linear transformation which commutes with G (which acts by ξ· id on the
subspace⟨v1,v 2⟩⊂ V ∨), we can suppose up to quasi-isomorphism that
W =λv1v2v3 +O(4) and η≡ 0. (5.13)
We next recall some background on Hochschild cohomology of semi-d irect products, see for
instance [97]. The Hochschild cohomology of a semi-direct product of a ﬁnite-dimensional algebra
with a ﬁnite group Γ has an eigenspace-type decomposition over con jugacy classes of Γ. In
particular, HH ∗(A ⋊ Zn, A ⋊ Zn) splits into a piece corresponding to id∈ Zn and (n− 1) other
summands indexed by the other characters:
HH ∗(A ⋊ Zn, A ⋊ Zn) =
⨁
γ∈Zn
Ext∗
bimod−A(A,Graph (γ))Zn (5.14)
The summand for γ = 1 is canonically identiﬁed with the invariant part HH ∗(A, A)Zn . In the
special case of an A∞-structure on the exterior algebra, each of the other summands is computed
by a cochain complex which actually deﬁnes a Koszul resolution of C, hence has one-dimensional
cohomology [90, Section 4b], whilst the invariant part of HH ∗(A, A) can be computed from the
complex of Equation 5.11. As an illustration, we explicitly verify that th e algebraic description
of the Fukaya category DπF(Σ g)≃ D(A ⋊ Z 2g+1) given in Section 3.7 is consistent with the
prediction of Corollary 3.11.
Lemma 5.26. HH ∗(DπF(Σ g))≃H ∗(Σ g) as Z2g+1-representations.
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 65
Proof. From the preceding discussion, we identify the invariant part HH ∗(A, A)Z2g+1 with the
invariant part of the Jacobian ring
J(Q) = C[[x1,x 2,x 3]]/⟨∂1Q,∂ 2Q,∂ 3Q⟩
under the inherited Z2g+1-action, where Q =−x1x2x3 +x2g+1
1 +x2g+1
2 +x2g+1
3 is the polynomial
superpotential controlling the A∞-structure on A = Λ( C3). In our case, the invariant part
J(Q)Z2g+1 is generated by the polynomials 1 and x1x2x3, noting that modulo the ideal of relations
⟨∂iQ⟩ one has
(x1x2x3)2∼ (x1x2x3)2g
and that 1 − (x1x2x3)2g−2 is invertible since we work over formal power series, hence x1x2x3
has order 2 in J(Q)Z2g+1 . The upshot is that the eigenspace decomposition of HH ∗ under the
Z2g+1-action has a two-dimensional zero-eigenspace and 2 g one-dimensional eigenspaces. This
matches the cohomology (= quantum cohomology) of Σ g, with Z2g+1 acting on H 1 with minimal
polynomial 1 + λ +λ2 +λ3 +··· +λ2g and acting trivially on H 0⊕H 2. □
The subcategory A(Z) is determined by a Z2g+1-equivariant Maurer-Cartan pair ( W, 0) as
in (5.13). Corollary 5.6 and the discussion around Equation 5.14 imply th at the Hochschild
cohomologyHH ∗(A ⋊ Z2g+1, A ⋊ Z2g+1) has 2g one-dimensional summands for the non-identity
elements, living in odd degree, and two even-degree classes (corre sponding to H 0 and H 2 of the
genusg curve).
Lemma 5.27. If the formal function W =λv1v2v3 +O(4),λ⁄= 0, determines an A∞-structure A
on Λ( C3) ⋊ Z2g+1 for which HH ∗(A, A)Z2g+1 has rank 2, then the coeﬃcients of the 3 monomials
v2g+1
i in W are all non-zero.
Proof. The Hochschild cohomology of the A∞-structure is the cohomology of the Koszul complex
0→ C[[V ∨]]⊗ Λ 3(V )
ιdW
−−→C[[V ∨]]⊗ Λ 2(V )
ιdW
−−→C[[V ∨]]⊗ Λ 1(V )
ιdW
−−→C[[V ∨]]→ 0. (5.15)
This contains in degree zero a copy of the Jacobian ring J(W ) = C[[V ∨]]/⟨∂iW⟩, which must
therefore contain a unique non-identity element.
If the coeﬃcient µi of the monomial v2g+1
i is zero, then v2g+1
i will survive into the Jacobian ring
(since this is the lowest monomial term that can occur in W by Z2g+1-invariance). Therefore, at
most one of the µi>0 can be zero, in fact µ3 since the A∞-structure is invariant under permuting
v1 and v2; and in this case W must contain a monomial v4g+2
3 (or the element [ v2g+1
3 ]∈ J(W )
will not have square zero). However, if W =λv1v2v3 +µ(v2g+1
1 +v2g+1
2 ) +µ3v4g+2
3 +p where all
terms of p of degree < 2g + 1 involve at least two variables, then [ v1v2v3] and [v2g+1
3 ] give distinct
elements of J(W ), which again contradicts the invariant part of HH ∗ having rank 2. □
We recall Noether’s classical result [75] that the invariant subring C[v1,v 2,v 3]G under a ﬁnite
group G is generated by monomials of degree at most the order of G. Let Q∈ C[[V ∨]]G denote
Q =−v1v2v3 +v2g+1
1 +v2g+1
2 +v2g+1
3 .
The following is a variant of Seidel’s [93, Lemma 4.1], whose proof we follow closely.
Lemma 5.28. Pick constants (λ,µ 1,µ 2,µ 3)∈ (C∗)4. Let p(·) be a polynomial of degree 4≤
deg(p)≤ 2g + 1, with vanishing coeﬃcients of the monomials v2g+1
i . The A∞-structure deﬁned
by any Z2g+1-invariant Maurer-Cartan pair (W, 0) with
W =λv1v2v3 +p(v1,v 2,v 3) +µ1v2g+1
1 +µ2v2g+1
2 +µ3v2g+1
3 +O(2g + 2)
is A∞-isomorphic to the structure deﬁned by (Q, 0).
66 IV AN SMITH
Proof. To be maximally explicit, we suppose ﬁrst g = 2, so p(·) = 0, and explain the mod-
iﬁcations for the general case at the end. Let Wµ denote the degree ≤ 5 = 2 g + 1 part of
the given formal function W . Letting I denote the ideal generated by the partial derivatives
I =⟨∂1Wµ,∂ 2Wµ,∂ 3Wµ⟩, one checks that:
• vivj∈I +O(4)
• v6
i∈I·O(2) +O(8).
Explicitly, to check the second claim, one starts from ∂1Wµ∈I and writes
5µ1v4
1∈I +µ0v2v3 ⇒ v6
1∈I·O(2) + C·v2
1v2v3
and then substitutes
v2
1v2v3 = ( v1v2)· (v1v3)∈ (I− Cv4
3)· (I− Cv4
2).
Given any n, direct manipulation now yields a co-ordinate transformation exp(g1) (which can be
averaged to be G-equivariant) for which
exp(g1)· (W ) = Wµ +O(n).
Explicitly, if W =Wµ +O(6) is Z5-equivariant, it contains no monomials vt
i fort = 6, 7, 8. Then
W−Wµ is a sum of terms vj.vk.(·) and terms of order ≥ 9, hence W−Wµ∈I·O(≥ 4) +O(≥ 9).
For a suitable change of variables
v′
j =vj +f4,j(v); f4,j∈O(4)
one sees W (v′
1,v ′
2,v ′
3) is given by
W (v1,v 2,v 3) +
∑
j
f4,j∂jW +··· +O(9)
which we write as:
W +
∑
j
f4,j∂jWµ +
∑
j
f4,j(∂jW−∂jWµ) +O(9)
Now using the bullet point above, one can choose the f4,j so that the ﬁrst two terms give exactly
the part of W−Wµ in I·O(4), and all the other Taylor co-eﬃcients are O(9), so we have
improvedn from 6 to 9. Iterating the procedure, one can increase n arbitrarily. Since Wµ has an
isolated singularity at the origin, the general ﬁnite determinacy the orem from singularity theory
[63] implies that, once n is large enough, there is a formal change of variables exp(h1) for which
exp(h1)·W = Wµ.
Recall that A∞-structures on Λ( V ) ⋊G are invariant under G-equivariant linear transformations
in GL(V ). In our situation they are invariant under arbitrary invertible linea r rescalings of the
vi. This brings any polynomial Wµ of the given form into the shape tv1v2v3 +v5
1 +v5
2 +v5
3.
A further linear co-ordinate change will bring this into the form −ǫv1v2v3 +ǫ3(v5
1 +v5
2 +v5
3),
for some ǫ∈ C∗. One now uses the existence of a canonical C∗-action (again not by gauge
transformations, but nonetheless by A∞-isomorphisms) on the space of A∞-structures, where
ǫ∈ C∗ acts by rescaling µj byǫj−2, to reduce to the desired polynomial Q. This completes the
argument when g = 2.
The general case, when g >2, is similar. The polynomial p actually lies in O(d) for some d> 4,
for invariance reasons, and contains no monomial terms vj
i (the only invariant monomial terms
of degree < 2g + 2 are v2g+1
i , for which p has vanishing coeﬃcients by hypothesis). Therefore,
its lowest degree d piece can be written (not necessarily uniquely) as
pd(v1,v 2,v 3) = v1v2q3 +v2v3q1 +v3v1q2
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 67
for G-invariant homogeneous polynomials qi∈O(d− 2) of degree > 2. There is an inﬁnitesimal
gauge transformation
vi↦→v′
i =vi−qi = vi + [−qiξi,v i]
associated to the 1-form − ∑ qiξi, and since qi ∈ O(2), this exponentiates to a gauge trans-
formation which takes the given W to a polynomial W ′ of the same shape, but for which the
polynomial p has larger degree:
W ′ =λv′
1v′
2v′
3 + ˜p(v′
1,v ′
2,v ′
3) +µ1(v′
1)2g+1 +µ2(v′
2)2g+1 +µ3(v′
3)2g+1 +O(2g + 2)
withdeg(˜p)≥d + 1, because all the higher order terms in the exponentiated adjoin t action (5.9)
have larger polynomial degree. Iterating (ﬁnitely often, so there are no convergence issues), one
reduces to the case when p∈O(2g + 2), so without loss of generality we can take p≡ 0 in the
statement of the Lemma. Now vivj∈I +O(2g), and explicit formal changes of variables as in the
g = 2 case iteratively kill the O(2g + 2)-part of W , cf. [29, Lemma 3.1]. Finally, the coeﬃcients
µj are adjusted using GL(V )-invariance and the canonical C∗-action on A∞-structures. □
Note that Lemma 5.26 veriﬁes that in the only non-excluded case, th e Hochschild cohomology
does have the anticipated rank. Combining our knowledge of quantu m cohomology, Corollary
5.6, with Lemma 5.27, one ﬁnds that the A∞-structure on F(Z) satisﬁes the conditions of Lemma
5.28. Since this singles out a unique quasi-isomorphism class, one conc ludes that the generalised
pentagram spheres in Z deﬁne an equivalent structure to the corresponding curves in the genus
g surface. Since on the genus g curve these Lagrangians split-generate, this proves that
DπF(Σ g)֒→DπF(Z).
Lemma 5.5 and Lemma 4.44 together show that this embedding has the same image, up to
quasi-isomorphism, as the embedding DπF(Q0∩Q1)֒→DπF(Z) of Lemma 4.38.
Corollary 5.29. The embedding of categories DπF(Σ g)֒→DπF(Z) is compatible with the nat-
ural weak actions of the pointed hyperelliptic mapping clas s group.
Corollary 5.29 has precisely the same proof as Corollary 4.45, but invo king Lemma 5.5 in place
of Lemma 4.44. Together, these results imply Addendum 1.2 from the Introduction.
Remark 5.30. The ﬁnite group H 1(Σ g; Z2)∋ξ has a natural weak action on F(Σ g), tensoring by
ﬂat line bundles ξ, and on F(Q0∩Q1; 0), by symplectic involutions ιξ of Remark 4.11, and one can
ask if the equivalence Υ : DπF(Σ g)≃DπF(Q0∩Q1; 0) we have constructed also entwines that
action. We shall not prove this, but the relevant cohomological evid ence is provided by Remark
3.22 and Remark 2.5. Presumably, just as Υ( γ)≃V¯γ, also Υ( ξ→γ)≃ιξV¯γ. If true, one could
compute the Hochschild cohomology of the autoequivalence ⊗ξ∈Auteq(F(Σ)) in terms of the
ﬁxed point Floer cohomology HF (ιξ) on Q0∩Q1.
