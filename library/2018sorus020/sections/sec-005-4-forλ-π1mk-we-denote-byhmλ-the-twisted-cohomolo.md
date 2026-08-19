---
doc_id: 2018sorus020
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-005-4-forλ-π1mk-we-denote-byhmλ-the-twisted-cohomolo
section_title: "Forλ :π1(M)→k∗, we denote byH∗(M,λ ) the twisted cohomology groups"
section_number: 4
pages: 9-11
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "HAL Id: tel-02108892 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 78 sections: Introduction"
---
with action ofλ by multiplication on the ﬁeldk. Of course, whenλ is constant
equal to 1, we keep the notationH∗(M,k ).
The torsion of twisted cohomological complexes by a representationρ : π1(M)→
SL2(C) for M a hyperbolic 3-manifold has been studied for a long time. Let us
mention the seminal work of Joan Porti in his PhD dissertation [Por97] (see the
survey [Por15] too) for the adjoint torsion, and of Teruaki Kitano [Kit94, Kit96]
for the standard torsion and the relation with the twisted Alexander polynomial.
Many other authors have substantially contributed to the topic in the past ten
years, including Jérome Dubois, Nathan Dunﬁeld, Stefan Friedl, Takahiro Kitayama,
Yoshikazu Yamaguchi.
In the ﬁrst chapter of this thesis, we give the main deﬁnitions that will be used in
the rest of this work. In particular we discuss various reﬁnements of the character
varieties theory, its relations with incompressible surfaces in 3-manifolds via the
Culler-Shalen theory, and deﬁne the Reidemeister torsion in a general setting. In the
second chapter, we study the adjoint torsion on the character variety, we deﬁne it as
a rational diﬀerential form, and we study its poles and zeros. In the third chapter,
8
we focus on the standard torsion function, and prove that under mild hypothesis on
M the torsion is not constant.
The adjoint torsion
In Chapter 2, we focus on the adjoint torsion, and present the results of the article
[Ben16].
The Reidemeister adjoint torsion is a topological invarianttor(M, Ad◦ρ) that we
may interpret as a volume element in the twisted cohomology, that is an element in
Det(H∗(M, Ad◦ρ)) =
3⨂
i=0
Det(Hi(M, Ad◦ρ))(−1)i
.
Moreover as soon as ρ and ρ′ are conjugated representations, there is a natural
isomorphism Det(H∗(M, Ad◦ρ))≃ Det(H∗(M, Ad◦ρ′)) that preserves the torsion.
Hence it is natural to deﬁne the Reidemeister adjoint torsion as a section of some
line bundle over the character variety.
In his Phd thesis [Por97], Joan Porti deﬁned the torsion as an analytic function
on a Zariski open subset of the character variety depending on a choice of a boun-
dary curve. Many computations have been performed by J. Dubois and al. [Dub06],
[DHY09] and the torsion has been extended to the whole character variety in [DG16].
We will follow in this article the approach of [Mar15], where the Reidemeister tor-
sion of any 3-manifold with boundary is interpreted as a rational volume form on
the character variety. More precisely, if the boundary ofM is a torus, the torsion
is a rational volume form on theaugmented character varietywhich is the following
2-fold covering of the character variety :
¯X(M) ={(ρ :π1(M)→ SL2(C),λ :π1(∂M )→ C∗), Trρ|π1(∂M ) =λ+λ−1}//SL2(C).
In this thesis we assume thatX(M) is 1-dimensional andreduced, in the sense of
schemes. The ﬁrst assumption is guaranteed by the assumption thatM is small,
that is without closed incompressible oriented surfaces not parallel to the boundary.
Let X¯ be an irreducible component of ¯X(M) containing the character of an irre-
ducible representation and letY be its smooth projective model. It is a smooth
compact curve obtained from X¯ by desingularizing and adding a ﬁnite number of
points at inﬁnity : we call the latter points ideal points ofY and the others are ﬁnite
points. We denote byv an element ofY that can be viewed as a valuation on the
9
function ﬁeldC(Y ) = C(X¯ ). Its local ring atv will be denoted byOv. The torsion
will be denoted bytor(M, Ad◦ρ) and seen as an element ofΩC(Y )/C. The ﬁrst result
is the following theorem :
Theorem (Theorem 2.0.1). Letv be a ﬁnite point ofY, thentor(M, Ad◦ρ) has no
pole atv. More precisely
