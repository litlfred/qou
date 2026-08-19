---
doc_id: gambaudo-ghys-braids-signatures-2005
doc_title: "Bull. Soc. math. France 133 (4), 2005, p. 541–579"
section_id: sec-010-31-signature-of-4-manifolds-recall-that-the-sign
section_title: "Signature of 4-manifolds. — Recall that the signature σ (M ) of an"
section_number: 3.1
pages: 14-17
source_pdf: gambaudo-ghys-braids-signatures-2005.pdf
source_sha256: 647f4c28cab7428d
doc_brief: "Bull. Soc. math. France 133 (4), 2005, p. 541–579 — 62 sections: Introduction; (v1) −v1 =v2 −γ 2(v2) and deﬁne; (α,β ) which is a 2-fold branched"
---
oriented compact 4-manifold is the signature of the interse ction form on the
second homology group H2(M ; R). Note that this intersection form can be
degenerate if the boundary of M is not empty: a class in H2(∂M ; R) maps
in H2(M ; R) to an element of the kernel of this form.
The signature of an oriented link can be seen as the signature of a 4-manifold
as follows. Consider an oriented link λ ⊂ S3 and a Seifert surface Sλ embedded
in S3 which can be considered as the boundary of the 4-dimensional ball D4.
Let us push the Seifert surface in D4 keeping its boundary ﬁxed on S3 to get a
surfaceS′
λ which intersects the boundary S3 only along its boundary. Consider
the 2-fold cover V 4
2 of D4 branched along S′
λ . It is a 4-dimensional manifold
tome 133 – 2005 – n o 4
BRAIDS AND SIGNATURES 555
whose boundary ∂V 4
2 is a 2-fold cover over S3 branched along λ . It turns out
(see for instance [7]) that:
sign(λ ) = σ (V 4
2 ).
In the general case of a root of unity ω which is diﬀerent from −1, we shall see
in 3.4 that there is a similar interpretation of the ω -signature of an oriented
link in terms of signatures of 4-manifolds.
Remark. — Ramiﬁed Z/k Z-cyclic coverings are omnipresent in this paper.
Recall that such a covering is completely determined by a ramiﬁcation locus
(which is a codimension 2 submanifold) and a homomorphism fr om the fun-
damental group of its complement to Z/k Z. In the previous cases that we
considered, the homomorphism was implicit. In the case of th e ramiﬁed 2-fold
cover of the disc, it was the unique homomorphism which is equ al to 1 on small
simple positive loops going once around the x0
i ’s. In case of the 2-fold cover
of S3 ramiﬁed on an oriented link, it was the reduction modulo 2 of t he linking
number. In the case of the cover of D4 branched along S′
λ , it was also given by
a linking number: a curve in the complement of S′
λ bounds a disc in D4 and
one considers the reduction modulo 2 of the intersection num ber of this disc
with S′
λ .
An important tool in our proof will be Novikov additivity theorem that we
recall brieﬂy now (see for instance [7] for a proof):
Theorem 3.1 (Novikov). — LetM be an oriented 4-manifold obtained by glu-
ing two 4-manifolds M1 and M2 along some components of their boundaries.
Then the signature is additive:
σ (M ) = σ (M1) +σ (M2).
(The orientations on M1 and M2 are of course induced by the orientation
on M.)
In the proof of Theorem A, we shall need a more general situati on where one
glues manifolds with corners. Consider two oriented 4-mani folds M1 and M2
with boundary. In the boundaries ∂M 1,∂M 2, choose submanifolds, V1 andV2,
of dimension 3, possibly with boundary, and assume that we ar e given some
homeomorphism h from V1 to V2 reversing the orientations. Then one can
glue M1 and M2 along V1 and V2 using h. This produces a new oriented
4-manifoldM with boundary.
The Novikov additivity theorem does not apply in this situation: however
one can write
σ (M ) = σ (M1) +σ (M2) +δ
where the “defect” δ is not diﬃcult to analyze. Denote by X the union of
the boundaries of M1 and M2 in M . It consists of three 3-manifolds with
boundaries having a common boundary: the closures of ∂M 1 \V1 and∂M 2 \V2
BULLETIN DE LA SOCI ´ET´E MATH ´EMATIQUE DE FRANCE
556 GAMBAUDO (J.-M.) & GHYS (E.)
∂M 1 \ V1 ∂M 2 \ V2
Σ
~X
M
M1 M2
V1 = V2
Figure 8. Gluing manifolds with corners
(contained in the boundary of M ) and V1 (which is identiﬁed with V2 in M ).
One can describe M as the union of three 4-manifolds with boundary: M1,M2,
and ~X, where ~X denotes a regular neighborhood of X in M . If follows from
Novikov additivity theorem that δ is the signature of the oriented 4-manifold ~X
(see Figure 8). This means in particular that the defect only depends on the
topology of X, i.e. on the boundaries of M1 and M2 and the gluing map. Let
us make this defect more explicit.
Recall the notion of ternary Maslov index . Consider a real vector space E
equipped with a symplectic form Ω, and three Lagrangian subs pacesL1,L 2,L 3
(i.e. maximal isotropic subspaces). In the direct sum L1
⨁ L2
⨁ L3 consider
the subspace of triples ( x1,x 2,x 3) whose sum is zero in E. On this subspace,
one deﬁnes a symmetric bilinear form f by
f
(
(x1,x 2,x 3), (y1,y 2,y 3)
)
= Ω( x1,y 3) = Ω( x2,y 1) = Ω( x3,y 2)
= Ω( y1,x 3) = Ω( y2,x 1) = Ω( y3,x 2).
The Maslov index τ (L1,L 2,L 3) is by deﬁnition the signature of f (see
for instance [16] for a background). Note that this index is b ounded
by 3 dim L = 3
2 dimE (the better bound 1
2 dimE is possible but this will
be enough for our needs).
The index τ (L1,L 2,L 3) is a skew symmetric function of its three arguments
and is a cocycle in the sense that for any four Lagrangian subspaces, one has
τ (L1,L 2,L 3) −τ (L1,L 2,L 4) +τ (L1,L 3,L 4) −τ (L2,L 3,L 4) = 0.
In our situation, X consists of three oriented 3-manifolds with a common
boundary surface Σ. The ﬁrst homology group H1(Σ , R) is a symplectic vec-
tor space (using intersection) as soon as one chooses an orie ntation on Σ:
let us choose the orientation that comes from the orientatio n of ∂M 1 \V1
(which in turn comes from the orientation of M1). In the symplectic vector
spaceH1(Σ , R), one has three natural Lagrangian subspaces L1,L 2,L 3, corre-
sponding to those homology classes in Σ which are trivial whe n one maps them
in the homology of ∂M 1 \V1,∂M 2 \V2 and V1 (≃ V2) respectively (these sub-
spaces are Lagrangian as follows from Poincar´ e duality). I n [17], Wall proves
that the defect δ is equal to the ternary Maslov index of these three Lagrangia n
tome 133 – 2005 – n o 4
BRAIDS AND SIGNATURES 557
subspaces. This follows from a simple application of Mayer-Vietoris e xact se-
quence which enables an identiﬁcation of the intersection f orm in H2( ~X, R)
(modulo subspaces contained in the kernel) to the quadratic formf associated
to L1,L 2,L 3. We shall call this result the Novikov-Wall additivity theorem .
