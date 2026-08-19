---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic"
section_id: sec-018-ind-constructible-calabi-yau-categories-and-pote
section_title: "Ind-constructible Calabi-Yau categories and potentials"
section_number: null
pages: 53-56
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
tentials
Let k be a ﬁeld of characteristic zero. Recall that a Calabi-Yau ca tegory
of dimension d is a weakly unital k-linear triangulated A∞-categoryC (see
[41], [42], [65]), such that for any two objects E,F the Z-graded vector
space Hom•(E,F ) =⊕n∈Z Homn(E,F ) is ﬁnite-dimensional (hence the space
Ext•(E,F ) is also ﬁnite-dimensional) and moreover:
1) We are given a non-degenerate pairing
(•,•) : Hom•(E,F )⊗ Hom•(F,E )→ k[−d] ,
which is symmetric with respect to interchange of objects E and F ;
2) For any N /greaterorequalslant2 and a sequence of objects E1,E 2,...,E N we are given
a polylinear Z/NZ-invariant map
WN :⊗1≤i≤N (Hom•(Ei,Ei+1)[1])→ k[3−d] ,
where [1] means the shift in the category of Z-graded vector spaces, and we
set EN +1 =E1;
53
3) We have:
WN (a1,...,a N ) = (mN−1(a1,...,a N−1),aN ) ,
wheremn :⊗1≤i≤n Hom•(Ei,Ei+1)→ Hom•(E1,En+1)[2−n] are higher com-
position maps.
The collection (WN )N /greaterorequalslant2 is called the potential ofC. If d = 3 then for any
object E∈ Ob(C) we deﬁne a formal series Wtot
E at 0 ∈ Hom•(E,E )[1] by
the formula:
Wtot
E (α) =
∑
n/greaterorequalslant2
Wn(α,...,α )
n .
We callWtot
E the total (or full) potential of the object E. We call the potential
of E the restriction of Wtot
E to the subspace Hom 1(E,E ). We will denote it
byWE.
The notion of a Calabi-Yau category admits a natural general ization to
the ind-constructible case (the pairing is required to be a m orphism of con-
structible vector bundles). It follows from the Axiom A3) th at there exists a
decomposition of Ob(C)≃⊔ Si into the disjoint union of schemes such that
all Taylor components WN of the potential are symmetrizations of regular
sections of cyclic powers of algebraic vector bundles on sch emes Si. There-
fore we can treat the family of potentials WC = (WE)E∈Ob(C) as a function,
which is regular with respect to the variable E and formal in the direction
α∈ Hom1(E,E ) (or α∈ Ext1(E,E ) if our category is minimal on the diag-
onal). Also the potential WE considered as a function of E∈Sj becomes a
section of the pro-algebraic vector bundle∏
n/greaterorequalslant2Symn(HOM1
|Diag(Sj )⊂Sj×Sj )⋆,
where Diag denotes here the diagonal embedding.
Proposition 7 In the case of 3d Calabi-Yau categoryC consisting of one
object E the potential WE admits (after a formal change of coordinates) a
splitting:
WE =Wmin
E ⊕QE⊕NE ,
where Wmin
E is the potential of the minimal model Cmin (i.e. it is a for-
mal series on Ext1(E,E )), the quadratic form QE is deﬁned on the vector
space Hom1(E,E )/ Ker(m1 : Hom 1(E,E )→ Hom2(E,E )) by the formula
QE(α,α ) = m2(α,α)
2 , and NE is the zero function on the image of the map
m1 : Hom 0(E,E )→ Hom1(E,E ). In the above splitting formula we use the
notation (f⊕g)(x,y ) = f (x) +g(y) for the direct sum of formal functions f
and g.
54
The above Proposition follows from the minimal model theore m for Calabi-
Yau algebras (i.e. Calabi-Yau categories with only one obje ct). In its for-
mulation below we are going to use the language of formal non- commutative
geometry from [42]. We assume that the ground ﬁeld has charac teristic zero.
Theorem 5 a) Let (X,x 0,ω,d X) be a Z/2Z-graded non-commutative for-
mal pointed manifold (X,x 0) endowed with an odd symplectic form ω and
homological vector ﬁeld dX which preserves ω and vanishes at x0. Then it is
isomorphic to the product
(X′,x′
0,ω′,dX′)× (X′′,x′′
0,ω′′,dX′′) ,
where (X′,x′
0,ω′,dX′) is minimal in the sense that (LiedX′ )|Tx′
0X′ = 0 (i.e.
dX′ vanishes quadratically at x′
0), and the second factor satisﬁes the follow-
ing property: there exists a ﬁnite-dimensional super vecto r space V endowed
with an even non-degenerate quadratic form QV such that (X′′,x′′
0,ω′′,dX′′) is
isomorphic to the non-commutative formal pointed manifold associated with
V⊕ Π V∗ (here Π is the change of parity functor) endowed with a constant
symplectic formωV coming from the natural pairing between V and Π V∗, and
homological vector ﬁeld dV is the Hamiltonian vector ﬁeld associated with the
pull-back of QV under the natural projection V⊕ Π V∗→V .
b) In the Z-graded case when X corresponds to a 3d Calabi-Yau algebra
(i.e. ω has degree−1) a similar statement holds. In this case V is Z-graded
vector space, QV has degree 0, and the tangent space Tx′′
0X′′ isomorphic to
V⊕V∗[−1].
Proof. One can prove part a) similarly to the usual minimal model the -
orem for A∞-algebras or L∞-algebras (it is induction by the order of the
Taylor expansion, see e.g. [41]). Part b) is a Gm-equivariant version of part
a). ■
The Proposition follows from part b) of the Theorem, since we have a
decomposition Hom 1(E,E )≃ Ext1(E,E )⊕V 0⊕ (V 1)∗ where Vi,i∈ Z are
the graded components of V . The restriction of Wtot
E to Hom 1(E,E ) is the
direct sum of Wmin
E , the restriction of QV to V 0 (we identify QV with QE)
and the zero function on ( V 1)∗.
Corollary 2 The minimal model potential Wmin
E does not depend on a choice
of minimal model for End•(E), if considered up to a formal non-linear auto-
morphism of the bundleHOM1 restricted to the diagonalDiag(Sj)⊂Sj×Sj.
55
Proof. Change of the minimal model is a Z-graded change of coordinates.
It preserves the topological ideal generated by all coordin ates of non-zero
degrees. ■
We remark that there is a notion of Calabi-Yau category valid over a ﬁeld
k of arbitrary characteristic. In the case of a category with o ne object E let
us denote by A theA∞-algebra Hom•(E,E ). We assume that Ext •(E,E ) =
H•(A) is ﬁnite-dimensional. Then a Calabi-Yau structure of dime nsiond on
A is given by a functional Tr of degree−d on the cyclic homology HC•(A)
such that the induced functional on H•(A)/[H•(A),H•(A)] gives rise to a
non-degenerate bilinear form ( a,b )↦→Tr (ab), where a,b∈H•(A).
In the case of positive characteristic the notion of the pote ntial does
not exist in the conventional sense. This can be seen in the ex ample A =
F3⟨ξ⟩/(ξ4), degξ = +1. The potential should have the form W (ξ) = ξ3/3 +
... which does not make sense over the ﬁeld F3.
In general it seems that although the potential does not exis t, its diﬀer-
ential is well-deﬁned as a closed 1-form.
Remark 17 In the case of characteristic zero the cyclic homology HC•(A)
can be identiﬁed with the cohomology of the complex ⊕n/greaterorequalslant1Cycln(A[1]) of
cyclically invariant tensors (see [42]). Therefore the pot ential W becomes
a functional of degree 3−d on the latter complex, vanishing on the image
of the diﬀerential. Hence it deﬁnes a class [W ] in (HC•(A))∗. The latter
space is a k[[u]]-module, where u is a variable, degu = +2 (see loc. cit.).
The class [W ] is related to the functional Tr discussed above by the formula
[W ] = uTr . In the case of a Calabi-Yau algebra of dimension d = 2k + 1
it is natural to introduce a cyclic functional Wk with the corresponding class
[Wk] = ukTr . It can be thought of as a higher-dimensional Chern-Simons
action. In particular, it deﬁnes a formal power series W 0
k of degree zero such
that it vanishes with the ﬁrst k derivatives on the formal scheme of solutions
to the Maurer-Cartan equation.
