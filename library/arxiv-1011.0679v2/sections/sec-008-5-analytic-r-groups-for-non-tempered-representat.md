---
doc_id: arxiv-1011.0679v2
doc_title: "A FORMULA OF ARTHUR AND AFFINE HECKE ALGEBRAS"
section_id: sec-008-5-analytic-r-groups-for-non-tempered-representat
section_title: "Analytic R-groups for non-tempered representations"
section_number: 5
pages: 20-21
source_pdf: 1011.0679v2.pdf
source_sha256: 6fa4bbcf4e908373
doc_brief: "A FORMULA OF ARTHUR AND AFFINE HECKE ALGEBRAS — Let π, π ′ be tempered representations of an aﬃne Hecke algebra with positive parameters."
---
In this section we extend the deﬁnitions and results from Sec tion 1.4 (which stem
from [DeOp2]) to non-tempered induction data ξ ∈ Ξ \ Ξ un. One approach would
be to deﬁne the R-group of ξ = (P,δ,t ) to be that of ξun = (P,δ,t |t|−1). This works
out well in most cases, but it is unsatisfactory if the isotro py group Wξun is strictly
larger than Wξ.
The problem is that t |t|−1 is not always a generic point of ( T P )Wξ . To overcome
this, we deﬁne Mξ to be the collection of mirrors M ∈ M P,δ that contain not
onlyt |t|−1, but the entire connected component of t|t|−1 in (T P
un)Wξ . Notice that all
components of (T P )Wξ are cosets of a complex subtorus of T P . Since t |t|r ∈ (T P )Wξ
for all r ∈ R, Mξ is precisely the collection of mirrors whose complexiﬁcati on
containst.
Now we deﬁne Rξ,R +
ξ and Rξ as in (28) and (29). We note that Rξ may diﬀer
from Rξun, but that Rξ =RP,δ,t′ for almost all t′ ∈ (T P
un)Wξ . For positive induction
data there is an analogue of Theorem 1.5:
Theorem 5.1. Letξ = (P,δ,t ) ∈ Ξ +.
(a) Forw ∈ W ξ the intertwiner π(w,ξ ) is scalar if and only if w ∈W (Rξ).
(b) There exists a 2-cocycle κξ of Rξ such that EndH(π(ξ)) is isomorphic to the
twisted group algebra C[Rξ,κ ξ].
(c) There exists a unique bijection
Irr(C[Rξ,κ ξ]) → IrrWξ(H) : ρ ↦→πρ,
and there exist indecomposable direct summands ~πρ of π(ξ), such that πρ is a
quotient of ~πρ and π(ξ) ∼=
⨁
ρ ~πρ ⊗ρ as H ⊗ C[Rξ,κ ξ]-modules.
Remark 5.2. Part (a) also holds for general ξ ∈ Ξ . Part (d) of Theorem 1.5
does not admit a nice generalization to ξ ∈ Ξ +. One problem is that the category
Modf (C[Rξ,κ ξ]) is semisimple, while π(ξ) is not always completely reducible. One
can try to consider the category of H-representations all whose irreducible subquo-
tients lie in Irrξ(H), but then one does not get a nice formula for the functor Eξ.
Proof. (a) and (b) Since ξ is positive, the operators π(w,ξ ) with w ∈ W ξ span
EndH(π(ξ)) [Sol3, Theorem 3.3.1]. Let v ∈W (Rξ). The intertwiner π(v,P,δ,t ′) is
rational in t′ and by Theorem 1.5.a it is scalar for all t′ in a Zariski-dense subset of
(T P
un)Wξ . Hence π(v,P,δ,t ′) is scalar for all t′ ∈ (T P )Wξ , which together with (29)
and (17) implies that
EndH(π(ξ)) = span {π(w,ξ ) : w ∈ Rξ}.
All the intertwiners π(w,P,δ,t ′) depend continuously on t′, so the type of π(P,δ,t ′)
as a projective Rξ-representation is constant on connected components of ( T P )Wξ .
Again by Theorem 1.5.a {π(w,ξ ) : w ∈ Rξ} is linearly independent for generic
t′ ∈ (T P
un)Wξ , so it is in fact linearly independent for all t′ ∈ (T P )Wξ . Now the mul-
tiplication rules for intertwining operators (17) show tha t End H(π(ξ)) is isomorphic
to a twisted group algebra of Rξ.
(c) Let A = End C[Rξ,κξ] be the bicommutant of π(ξ, H) in End C(H). There is a
canonical bijection
Irr(C[Rξ,κ ξ]) → Irr(A) : ρ ↦→~πρ
A FORMULA OF ARTHUR AND AFFINE HECKE ALGEBRAS 21
such thatπ(ξ) ∼=
⨁
ρ ~πρ⊗ρ asA⊗C[Rξ,κ ξ]-modules. By construction the irreducible
A-subrepresentations ofπ(ξ) are precisely the indecomposable H-subrepresentations
of π(ξ). By [Sol3, Proposition 3.1.4] every ~πρ has a unique irreducible quotient H-
representation, say πρ, and πρ ∼= πρ′ if and only if ~πρ ∼= ~πρ′ as H-representations.
Thus ρ ↦→πρ sets up a bijection between Irr( C[Rξ,κ ξ]) and the equivalence classes
of irreducible quotients of π(ξ). By Theorem 1.2 the latter collection is none other
than Irr Wξ(H). ✷
