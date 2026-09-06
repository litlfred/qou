---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-020-73-monodromic-hochschild-calculations
section_title: "Monodromic Hochschild calculations"
section_number: 7.3
pages: 41-42
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — W e apply the ideas of derived algebraic geometry and topolog ical ﬁeld theory to the representation theory of reductive groups."
---
the previous section, in particular Theorem 7.4. Thus suppose X is a stack with smooth diagonal, Y
is a stack, and X→Y is a proper representable map. Suppose AX∈D (X) is a commutative algebra
object whose underlying object is compact and hence dualizable with dual denoted byA∨
X∈D (X).
Return to the fundamental correspondence
LY =Y×Y ×Y Y LY×Y X =X×X×Y X
q/d111/d111 ǫ /d47/d47X×Y X.
where q is a base change of p, and ǫ is a base change δ.
Deﬁne the functor
˜F :DA(2)
X
(X×Y X) ˜ǫ!
/d47/d47DAX (LY×Y X)
˜q∗ /d47/d47D(LY )
where ˜ǫ! is the composition of the pullback ǫ! and then tensoring with the diagonal AX -module, and
˜q∗ is the composition of forgetting AX -module structure and then the pushforward q∗.
For simplicity, we will also assume given an equivalence of AX -modules of the form A∨
X≃A X [k],
for some ﬁxed k. This provides an identiﬁcation of the right adjoint of the pushforw ard ˜q∗ with a
shift of the pullback ˜q!. Thus we have the explicit continuous right adjoint
˜F r :D(LY )
˜q![k] /d47/d47DAX (LY×Y X)
˜ǫ∗[−2 dim X] /d47/d47DA(2)
X
(X×Y X)
41
where ˜q! is the composition of the pullback q! and then tensoring withAX , and ˜ǫ∗ is the composition
of forgetting to an A(2)
X -module structure and then the pushforward ǫ∗.
LetI( ˜F )⊂D (LY ) denote the cocompletion of the image of ˜F . It is naturally equivalent to the
left orthogonal ⊥K( ˜F r)⊂D (LY ) to the kernel of ˜F r.
Suppose in addition that tensoring with A∨
X is conservative so that ˜q! satisﬁes descent. Then
both of the above categories are naturally equivalent to the full su bcategory of D(LY ) of objects
whose image under ˜q! is in the cocompletion of the image of ˜ ǫ!.
Now repeating the arguments of Theorem 6.6 and Corollary 6.7 gives t he following extension.
Theorem 7.5. There are natural adjoint commutative diagrams
˜H
tr
/d119/d119♣♣♣♣♣♣♣♣♣♣♣♣♣
F
/d15/d15
Tr( ˜H) ∼ /d47/d47 ⊥K( ˜F r)≃I ( ˜F )
˜F r
/d79/d79
∼ /d47/d47 Z( ˜H)
z
/d102/d102◆◆◆◆◆◆◆◆◆◆◆◆◆
Proof. For notational convenience, set ˜A =DAX×Y X (X×YX) and ˜B =DAX (X), so that the center
is the totalization of the cosimplicial object
˜C• = Hom ˜B⊗ ˜Bop( ˜A⊗ ˜B•, ˜A)
Using Proposition 5.7 as in the proof of of Theorem 6.6, we have a level- wise fully faithful map
of cosimplicial diagrams
˜C• /d47/d47DA(•+1)
X
(X ×Y (•+1)×YLY )
where the cosimplicial structure maps on the latter are given by the composition of !-pullbacks
together with tensoring up with tensor powers of A∨
X .
Thus the center Z( A) is equivalent to the full subcategory of D(LY ) of objects whose image
under ˜q! is in the cocompletion of the image of ˜ ǫ!. □
Finally, there is a Morita-invariance between the original and now mon odromic calculations.
Proposition 7.6. The full subcategories K(F r),K( ˜F r)⊂D (LY ) deﬁned by the original and mon-
odromic fundamental correspondences coincide.
Proof. On underlying objects, we calculate via composition identities and the projection formula
that ˜F r(M)≃ F (M)⊗A ′
X×Y X . Since tensoring with A∨
X is conservative, so is tensoring with
A′
X×Y X , and hence K(F r) =K( ˜F r)⊂D (LY ). □
