---
doc_id: arxiv-2106.07444v2
doc_title: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS"
section_id: sec-003-3-the-aw-trace
section_title: "The AW Trace"
section_number: 3
pages: 30-32
source_pdf: 2106.07444v2.pdf
source_sha256: 5acca39c07bcdddd
doc_brief: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS — Let W be the W eyl group of a split semisimple group G. Its Hecke category HW can be built from pure perverse sheaves on the double ﬂag variety of G."
---
3.1. If A is a Z-graded ¯Qℓ-algebra, then we write:
(1) Mod1(A) for the category of graded left A-modules in which the grading is
bounded below and each graded piece is ﬁnite-dimensional.
(2) Modb
2(A) for the category of left A-modulesM equipped with a Z2-grading
such that M ∈ Mod1(A) with respect to both gradings and the value of
i −j is uniformly bounded among the nonzero components Mi,j.
If R is an (ungraded) ¯Qℓ-algebra and A forms an R-module, then we write R ⋉A
for the vector space R ⊗A endowed with the ring structure where:
• R and A form subrings.
• The only relations between R andA are those of the form ra = (r ·a)r for
all r ∈R and a ∈A.
If the R-action on A preserves the grading, then we extend the grading on A to a
grading on R ⋉A in which R is placed in degree zero, so that R ⋉A forms a graded
A-algebra.
Recall that X is the character lattice in the root datum of G. We set
V = X ⊗ ¯Qℓ.
Let the symmetric algebra Sym( V) be endowed with the grading where Sym i(V)
is placed in degree 2 i, and let
AW = ¯Qℓ[W ] ⋉ Sym(V).
Below, we construct a contravariant, monoidal trace from th e Hecke category to
Modb
2(AW ).
3.2. Suppose that X0 is a G0-variety over F and that C(X0) is a full, additive
subcategory of Db
G,m(X0) stable under ⟨n⟩ for all n ∈ Z. Any object K ∈ C(X0)
gives rise to a graded ¯Qℓ-algebra:
AK =
⨁
n
HomC(X0)(K,K ⟨n⟩ ).
We write the multiplication in AK as right-to-left composition: g ·f =g ◦f . Then
we have additive functors
⨁
n
HomC(X0)(−,K ⟨n⟩ ) : C(X0)op → Mod1(AK),
⨁
n
HomC(X0)(K, (−)⟨n⟩ ) : C(X0) → Mod1(Aop
K ).
Above, the gradings are bounded below by Remark 1.2.1. These functors can be
respectively extended to
⨁
i,j
HomKb(C(X0))(−,K ⟨j⟩ [i −j]△) : Kb(C(X0))op → Modb
2(AK ),
⨁
i,j
HomKb(C(X0))(K, (−)⟨j⟩ [i −j]△) : Kb(C(X0)) → Modb
2(Aop
K ),
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 31
once we embed C(X0) into Kb(C(X0)) as the full subcategory of complexes concen-
trated in degree zero. Above, in either direct sum, the value of i −j is uniformly
bounded among the nonzero terms precisely because the objec ts of Kb(C(X0)) can
be represented by bounded complexes.
In the rest of this section, we only use the contravariant fun ctors; the covariant
ones will appear again in Section 6. The following lemma is a consequence of
Proposition 1.5.1.
Lemma 3.2.1. If C(X0) is Hom-pure, then we have a commutative diagram:
Kb(C(X0))op Kb(C(X0))op
Db
G,m(X0)op Modb
2(AK)
Kbκ
ρ
⨁
i,j Hom(−,K ⟨j⟩ [i −j]△)
⨁
i,j grw
j Homi(−,K )
3.3. We now set X0 = U0 and C(X0) = C(U0) as in Deﬁnition 2.9.1. Recall that
S ∈ C(U0) denotes the (mixed) Springer sheaf.
Theorem 3.3.1 (Lusztig). We have AW ≃ AS as graded ¯Qℓ-algebras.
Proof. By [ L88, Cor. 6.4], AW ≃ End∗(ξS). By Lemma 2.10.2 (or [ R, Lem. 5.4]),
we have Endi(ξS) ≃ Hom0(S, S⟨i⟩ ) for all i after we forget Frobenius. □
Remark 3.3.2. Although we will not use it, the proof of [ R, Prop. 6.5] implies that
the functor ⨁
i Hom(S, (−)⟨i⟩ ) induces a triangulated equivalence
Kb(C ˆW (U0)) ≃ Db(Mod1(AW )),
where the right-hand side is the bounded derived category of Mod1(AW ).
Deﬁnition 3.3.3. The AW trace on the Hecke category is the contravariant func-
tor
AH : Hop
W → Modb
2(AW )
deﬁned by the commutative diagram
(12)
Kb(C(B0 × B0))op Kb(C(U0))op Kb(C(U0))op
Db
G,m (B0 × B0)op Db
G,m (U0)op Modb
2(AW )
Kb(i∗⟨−r⟩ ◦ CH)
i∗⟨−r⟩ ◦ CH
Kbκ
ρ ρ
that we obtain by combining Remark 1.4.4, Lemma 2.10.2, Lemma 3.2.1, and The-
orem 3.3.1. Explicitly,
AHi,j = Hom Kb(C(U0))(Kb(κ ◦i∗⟨−r⟩ ◦ CH)(−), S⟨j⟩ [i −j]△)
≃ grw
j Homi((ρ ◦ Kb(i∗⟨−r⟩ ◦ CH))(−), S)
≃ grw
j Homi((i∗⟨−r⟩ ◦ CH ◦ρ)(−), S)
for all i,j . It is a monoidal trace in the sense of Lemma 2.7.1 because it factors
through CH.
32 MINH-TÂM QUANG TRINH
