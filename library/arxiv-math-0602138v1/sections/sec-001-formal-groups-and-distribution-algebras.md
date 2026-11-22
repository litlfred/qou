---
doc_id: arxiv-math-0602138v1
doc_title: "Non-Commutative Formal Groups in Positive Characteristic"
section_id: sec-001-formal-groups-and-distribution-algebras
section_title: "Formal Groups and Distribution Algebras"
section_number: null
pages: 12-16
source_pdf: 0602138v1.pdf
source_sha256: ed9ade66a774c93e
toc_source: outline
doc_brief: "Non-Commutative Formal Groups in Positive Characteristic — We describe geometric non-commutative formal groups in ter ms of a ge- ometric commutative formal group with a Poisson structure o n its"
---
We wish to apply the results of §1 in order to give a description of non-
commutative formal groups over a ﬁeld k of characteristic p > 0. We establish
some notation and conventions for general rings R. We say that G is a formal
group (over R) if it is a group object in the category of smooth formal varieties
over R. We denote its dimension by n < ∞.
We recall some basic results of such formal groups (c.f [2], [3], [7], [8], a nd
[10]). Given a formal group G over R, one can look at the ring of formal
functions R[ [G] ] whose maximal ideal of functions we denote m. One can form
the continuous linear dual of R[ [G] ] with respect to the m-adic topology which we
denote by Dist(G). We denote by ⟨ , ⟩ the natural pairing between Dist(G)
and R[ [G] ]. One knows that Dist(G) has an algebra structure given by dualizing
the co-multiplication map m of R[ [G] ]. The non-commutativity of G is reﬂected
equally in the non-commutativity of the algebra structure of Dist(G) and the
non-co-commutativity of the co-multiplication m. One knows further that one
may dualize the multiplication of R[ [G] ] to give a co-multiplication map ∆ on
Dist(G). The algebra and co-algebra structure of Dist(G), and also those of
R[ [G] ], are compatible so that we in fact have a bi-algebra structure. Th e m-adic
topology on R[ [G] ] yields a ﬁltration of Dist(G) by sub-co-algebras:
Dist(G) =
⋃
n≥0
Dist(n)(G)
Dist(n)(G) := R ⊕ Dist(n)
+ (G)
Dist(n)
+ (G) := HomR(m/ mn+1, R ).
A choice of coordinate system x = {x1, · · · , x n} on G gives an identiﬁcation
R[ [G] ] =R[ [x1, · · · , x n] ]. If one chooses an ordering on the xi’s, sayx1 < · · · < xn,
then then one is working in the category of formal group laws. Any c hoice
of a coordinate system, without any speciﬁed ordering, gives the c hoice of an
additional structure on Dist(G), namely that of a DVPS-bi-algebra. By this
12
we mean there is a choice of a basis δxI of Dist(G) where J = (J1, · · · , J n) ∈ Zn
≥0
is a multi-index such that the co-multiplication law satisﬁes:
∆( δxJ ) =
∑
A+B=J
δxA ⊗ δxB .
The speciﬁc basis that the choice of x is the basis given by the maps:
δxJ (xK) :=
{ 1 J = K
0 J ⁄= K
where for the multi-index K we have deﬁned xK := xK1
1 · · ·xKn
n ∈ R[ [G] ]. We
will call such a basis an additive basis . The existence of the additive basis
means that one can recognize the dual of Dist(G) with multiplication given by
dualizing ∆ as a ring of power series. There is a ﬁnal structure on Dist(G)
which is the anti-pode or inverse Dist(G)
inv✲ Dist(G) which gives Dist(G)
the structure of a Hopf algebra. The existence and uniqueness is a utomatic in
the situations we will consider below.
Example 2.1.
2.1.1. Let G be a smooth (analytic, algebraic,..) group deﬁned over R. Then
we denote the completion of its ring of functions at the identity by R[ [G] ],
which we identify as the ring of formal functions of a formal group. Denote
by g the Lie algebra of G. If R is a Q-algebra, then Ug is canonically
isomorphic to Dist(G).
2.1.2. If k is a ﬁeld of characteristic p > 0, or more generally R is an Fp-algebra,
then one has that Dist(G) is ﬁltered by sub-bi-algebras:
Dist(G) =
⋃
r≥0
Dist(pr −1)(G).
Let us now assume that R = k is a ﬁeld of characteristic p > 0. In order to
make use of the results of §1, we will need to make use of a second basis:
Lemma/Deﬁnition 2.2. Let G be a formal group over a ﬁeld k of character-
istic p > 0. Let x< = {x1 < · · · < x n} be the choice of an ordered coordinate
system for G. Then Dist(G) has a k-basis, the multiplicative basis, given for
multi-indices J as the ordered products:
δJ
x<
= δ
J1
x1 · · ·δ
Jn
xn
where:
δ
Jj
xj := δJj,0
xp0
j
· · · δJj,r
xpr
j
.
Here, the δxps
j
’s are as in the additive basis above, and the Jj,t ’s are given by
the p-adic expansions of the Jj’s:
Jj = Jj, 0p0 + Jj, 1p1 + · · · + Jj,r pr.
13
When the choice of an ordered coordinate system x< is understood, we will drop
the subscripts and simply write δJ := δJ
x<
.
Remark 2.3.
2.3.1. The fact that this is indeed a basis is in [3]. Deﬁning:
X := {δpr
xj | 1 ≤ j ≤ n r ≥ 0}
one has at once an induced R-linear map ιx< given by:
Dist(G) ⊂
ιx< ✲ TX
δI ✲ δI .
We deﬁne for η, ζ ∈ X ⊆ Dist(G):
˜πx<(η, ζ ) := ιx<(ηζ − ζη) = ιx< ◦ πc(η, ζ )
gx<,η,ζ := ιx<(η)ιx<(ζ) − ιx<(ζ)ιx<(η) − ˜πx< (η, ζ )
Fx<(η) := ιx<(ηp)
fx<,η := ιx<(η)p − Fx<(η).
The extension of ˜πx< by the bi-derivation law to TX will also be denoted
by ˜πx< . If we take the choice x< as understood we shall write ˜ π = ˜πx<.
We may also identify X ⊆ Dist(G) and Dist(G) with their images in TX
via ιx< . Thus we may write more succinctly:
gη,ζ = ηζ − ζη − ˜π (η, ζ )
fη = ηp − F (η)
2.3.2. We have the following important ﬁltration properties of the F (η) and
πc(η, ζ ):
F (δxpr
i
) ∈ Dist(pr+1−1)(G)
π (δxps
j
, δ xpr
i
) ∈ Dist(pr+ps−1)(G).
2.3.3. There is an analogue to the multiplicative basis in the characteristic z ero
situation of g as above. For simplicity, let us assume that g is abelian and
arises as the Lie algebra of the formal group G = Gn
a . Let us choose a coor-
dinate yi for each of the Ga’s such that we may write the co-multiplication
map of G as:
m(yi) = yi ⊗ 1 + 1 ⊗ yi.
Let us denote the corresponding basis of g by g = ⟨Yi⟩1≤i≤n where Yi(yj) =
δi,j is the Kronecker delta product. Then, in this setting the, “multiplica -
tive basis” of Ug = Sg = Dist(G) is given by the elements:
Y I = Y I1
1 · · · Y In
n .
14
We may compute:
δyiδyk
i
=
∑
J
⟨m(yJ ), δ yi ⊗ δk
yi⟩δyJ
=
∑
j
⟨(yi ⊗ 1 + 1 ⊗ yi)j, δ yi ⊗ δk
yi⟩δyj
i
= ( k + 1)δyk+1
i
so that identifying Yi = δyi the additive and multiplicative basis are related
by:
Y I = δI
y = I!δyI
where I! := I1! · · · In!.
We may have also chosen the coordinates xi = exp(yi) − 1 for G, so that:
m(xi) = xi ⊗ 1 + 1 ⊗ xi + xi ⊗ xi
which is the group law for Gm the multiplicative group as well as its formal
completion Gm. Then as we have that:
δxi · δxk
i
= (k + 1)δxk+1
i
+ kδxk
i
one sees that the change of basis between the multiplicative and add itive
bases can be expressed in terms of the Sterling numbers of the ﬁrs t kind:
δxn
i = 1
n! δxi(δxi − 1)(δxi − 2) · · · (δxi − (n − 1)).
2.3.4. The impossibility of inverting I! and the fact that Ga and Gm are not
isomorphic in positive characteristic is the essential source of all th e com-
plications. Let us deﬁne for n ∈ Z ≥ 0:
n!p := n0!n1! · · · nr!
where n = n0 + n1p + · · ·nrpr is the p-adic expansion of n. We make a
similar deﬁnition for a multi-index I. Then one know that for a formal
group G we have:
δxI = 1
I!p
δI
x<
+ Lower Order Terms
In the case of G = Ga with coordinate y as above, we have, in fact, that:
δyn = 1
n!p
δn
y .
For G = Gm, with coordinate x as above, we have “Sterling numbers
modulo p”. Indeed, we may compute:
δxpr δxm = (mr + 1)δxm+1 + mrδxm
15
where m = m0 + · · · + mrpr is the p-adic expansion of m and we assume
mr < p − 1. From this it follows that we have:
δxm = 1
m!p
r∏
t=0
δxpt (δxpt − 1)(δxpt − 2) · · ·(δxpt − (mt − 1)).
Proposition 2.4. Let G be a formal group over a ﬁeld k of characteristic p > 0.
Let x< be the choice of an ordered coordinate system. Let us adopt th e notation
as in (Rmk. 2.3.1). Deﬁne deg(δpr
xi ) := pr and take:
δxps
j
> δxpr
i
if j > i or if j = i and s > r . Let I be the two-sided ideal of TX :
I = R + ˜J≪
R = ( fη | η ∈ X )
˜J≪ = ( gη,ζ | η > ζ ∈ X ) .
Imposing the graded lexicographic ordering on TX , the set:
{fη , g η,ζ |η > ζ ∈ X }
is a Gr¨ obner basis for the ideal I. In particular, Dist(G) is isomorphic as an
algebra to TX / I.
Proof. Due to the monomial ordering indicated and by (Rmk. 2.3.2) we see
that we having the following leading monomials:
LM(fη ) = ηp
LM(gη,ζ ) = ηζ.
The result follows as otherwise we would not have the existence of a m ultiplica-
tive basis.
