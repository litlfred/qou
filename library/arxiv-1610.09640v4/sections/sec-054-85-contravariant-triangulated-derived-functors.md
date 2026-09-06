---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-054-85-contravariant-triangulated-derived-functors
section_title: "Contravariant Triangulated Derived Functors"
section_number: 8.5
pages: 162-165
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
is a ﬁxed nonzero commutative base ringK, and all categories and functors here
areK-linear. The next setup is assumed.
Setup 8.5.1.We are given a DG ringA, an abelian categoryM, and a full additive
subcategory K⊆K(A, M) s.t. Kop⊆K(A, M)op is triangulated. We write S :=
K∩S(A, M), the set of quasi-isomorphisms inK, and Dop := (Kop)Sop, the derived
category of Kop.
As explained in Subsections 5.6 and 7.6, the categoriesKop and Dop have canon-
ical triangulated structures, and the localization functorQop : Kop→Dop is trian-
gulated.
Deﬁnition 8.5.2.Let E be a triangulated category, and letF : Kop→E be a
triangulated functor. A triangulated right derived functorof F is a triangulated
right derived functor(RF,ηR) : Dop→E of F with respect toSop, in the sense of
Deﬁnition 8.4.7.
Likewise:
Deﬁnition 8.5.3.Let E be a triangulated category, and let F : Kop →E be
a triangulated functor. A triangulated left derived functorof F is a triangulated
left derived functor (LF,ηL) : Dop→E of F with respect to Sop, in the sense of
Deﬁnition 8.4.21.
Theuniquenessresults(Propositions8.4.8and8.4.22)andexistenceresults(The-
orems 8.4.9 and 8.4.23) apply in the contravariant case as well. We shall return to
the existence question the end of Section 10, when we talk aboutresolving subcat-
egories; this will make matters more concrete. For now we give one example.
Example 8.5.4. Let M and N be abelian categories, and letF 0 : M→N be a
contravariant additive functor. This is the same as an additive functorF 0◦Op :
Mop→N. As in Theorem 3.9.13,F 0 gives rise to a contravariant DG functor
C−(F 0) : C−(M)→C+(N).
This means, according to Proposition 3.9.3, that we have a DG functor
C−(F 0)◦Op : C−(M)op→C+(N).
Passingtohomotopycategories, andusingTheorem5.6.10, weobtainatriangulated
functor
Ho
(
C−(F 0)◦Op
{
: K−(M)op→K+(N)
(with a translation isomorphism¯τthat we ignore now). Composing this with the
localization functor QN we have a triangulated functor
(8.5.5) F := QN◦Ho
(
C−(F 0)◦Op
{
: K−(M)op→D+(N).
162
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Similarly there is a triangulated functor
(8.5.6) F ﬂip := QN◦Ho
(
C+(F 0◦Op)
{
: K+(Mop)→D+(N).
Observe that this triangulated functor is of the same sort as the one we had in
(8.4.18). The functors (8.5.5) and (8.5.6) ﬁt into the the following commutative
diagram of triangulated functors
K−(M)op F //
Flip ∼=

D+(N)
K+(Mop)
F ﬂip
77
where Flip is the isomorphism of triangulated categories from (5.6.3).
The triangulated right derived functor
(8.5.7) R−F : D−(M)op→D+(N)
of the functorF from (8.5.5) would sit inside this diagram of triangulated functors,
which is commutative up to a unique isomorphism:
D−(M)op R−F //
Flip ∼=

D+(N)
D+(Mop)
R+F ﬂip
77
Like in Example 8.4.17, to show existence ofR+F ﬂip using Theorem 8.4.9, and
to calculate it, we would need a full triangulated subcategoryJ⊆K+(Mop), such
that every M ∈K+(Mop) admits a quasi-isomorphismM →I with I ∈J; and
every quasi-isomorphismψin J goes to an isomorphismF ﬂip(ψ) in D+(N). This
translates, by the ﬂip, to a full triangulated subcategoryP⊆K−(M) such that
J = Flip(P). The conditions on P are these: each M ∈K−(M) admits a quasi-
isomorphism P →M with P ∈P; and each quasi-isomorphism φin P goes to
an isomorphismF (φ) in D+(N). For instance, if M has enough projectives, then
according to Corollary 11.3.19, the category P of bounded above complexes of
projectives satisﬁes these conditions.
To calculate the derived functorR−F in equation (8.5.7) we choose a system
of left P-resolutions in K−(M), as in Deﬁnition 8.3.32. Thus for everyM we have
a chosen quasi-isomorphismρM : P (M)→M in K−(M). We take R−F (M) :=
F (P (M))∈D+(N). The morphism η−
M : F (M)→R−F (M) is η−
M := F (ρM) :
F (M)→F (P (M)).
The story is very similar for the triangulated left derived functor
L+F : D+(M)op→D−(N)
of
F := QN◦Ho
(
C+(F 0)◦Op
{
: K+(M)op→D−(N),
so we won’t tell it.
In later parts of the book we shall use the same symbolF to denote also the
functors F 0, F 0◦Op and C⋆(F 0)◦Op from the example above. This will simplify
our notation.
Though indirectly deﬁned (in Deﬁnition 5.6.4), the translation functorTop of
K(A, M)op is known to have some useful properties. Note that the objects of
K(A, M)op are the same as those ofK(A, M).
163
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proposition 8.5.8. For every objectM∈K(A, M)op there are canonical isomor-
phisms Top(M)i∼=Mi−1 and Hi(Top(M))∼= Hi−1(M) in M.
Proof. This is immediate from Theorem 3.9.16 and Deﬁnition 5.6.4. □
Here are several useful properties of the triangulated structure onD(A, M)op.
Proposition 8.5.9. Suppose
0→L
φ
− →M
ψ
− →N→0
is an exact sequence inCstr(A, M)op. Then there is a distinguished triangle
L
Qop(φ)
−−−−→M
Qop(ψ)
−−−−→N
θ
− →Top(L)
in D(A, M)op.
Proof. Apply the functorFlip to the given exact sequence. By Theorem 3.9.16(3)
we obtain a short exact sequence
0→Flip(L)
Flip(φ)
−−−−→Flip(M)
Flip(ψ)
− −−−− →Flip(N)→0
in Cstr(Aop, Mop). According to Proposition 7.3.5 there is a distinguished triangle
Flip(L)
Qﬂip(Flip(φ))
−−−−−−−−→Flip(M)
Qﬂip(Flip(ψ))
−−−−−−−−−→Flip(N)
θ′
−→Tﬂip(Flip(L))
in D(Aop, Mop). Take the morphism
θ:= Flip−1(θ′) :N→Flip−1(Tﬂip(Flip(L))) = Top(L)
in D(A, M)op. Since Flip−1(Qﬂip(Flip(φ))) = Q op(φ), and likewise forψ, we have
the desired distinguished triangle. □
Recall from Proposition 7.3.8 that ifA is a nonpositive DG ring, then for any
M∈C(A, M) and integeri the smart truncationssmt≥i(M), smt≤i(M)∈C(A, M)
exist.
Proposition 8.5.10. Assume A is a nonpositive DG ring. For every objectM∈
C(A, M) there is a distinguished triangle
smt≥i+1(M)→M→smt≤i(M)→Top(smt≥i+1(M))
in D(A, M)op. The truncations are performed inC(A, M) as above.
Proof. Let N := Flip(M)∈D(Aop, Mop). By Proposition 7.3.10 there is a distin-
guished triangle
smt≤i(N)− →N− →smt≥i+1(N)− →Tﬂip(smt≤i(N))
in D(Aop, Mop), where now the truncations are done inC(Aop, Mop). The formulas
deﬁning the ﬂip functor in the proof of Theorem 3.9.16 show that
Flip−1(smt≤i(N)) = smt≥i+1(M) and Flip−1(smt≥i+1(N)) = smt≤i(M). □
164
Derived Categories | Amnon Yekutieli | 14 Apr 2019
