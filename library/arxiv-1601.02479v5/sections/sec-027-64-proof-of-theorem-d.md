---
doc_id: arxiv-1601.02479v5
doc_title: "COHOMOLOGICAL DONALDSON–THOMAS THEORY OF A"
section_id: sec-027-64-proof-of-theorem-d
section_title: "Proof of Theorem D"
section_number: 6.4
pages: 60-63
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
doc_brief: "COHOMOLOGICAL DONALDSON–THOMAS THEORY OF A — This paper concerns the cohomological aspects of Donaldson – Thomas theory for Jacobi algebras and the associated cohomo logical Hall alge- bra"
---
bility condition ζ. By Corollary 4.11 there are canonical split inclusions
H(BC*)vir ⊗ BPSζ
W,µ → H
(
pζ
µ ,∗ICζ
W,µ
)
COHAS AND QUANTUM ENVELOPING ALGEBRAS 61
giving rise to canonical split inclusions H(B C*)vir⊗qζ
µ ,∗BPSζ
W,µ → qζ
µ ,∗ H
(
pζ
µ ,∗ICζ
W,µ
)
and thus split inclusions
ι′
µ : H(B C*)vir ⊗ qζ
µ ,∗BPSζ
W,µ֒H
(
qζ
µ ,∗pζ
µ ,∗ICζ
W,µ
)
by the decomposition theorem and properness of qζ
µ . Via the proof of Theorem 4.12
we can pick a right inverse ηµ ,∗ to the restriction map in cohomology
η∗
µ : H (pµ ,∗ICW,µ ) → H
(
qζ
µ ,∗pζ
µ ,∗ICζ
W,µ
)
for each µ . We set
ιµ =ηµ ,∗ι′
µ : H(B C*)vir ⊗ qζ
µ ,∗BPSζ
W,µ → H (pµ ,∗ICW,µ ) .
Theorem 6.12. Letζ be a generic stability condition, and consider the morphism
(104)
⊠tw
⊕,∞
µ
− →−∞
(
(τ )Sym⊠⊕
(
H(BC*)vir ⊗ qζ
µ ,∗BPSζ
W,µ
)) (¬ψ )H(˜∗W )
− − − − − − − → H(p∗ICW )
induced by the inclusions ιµ and the Hall algebra structure on H((ψ )AW ), where the
bracketed superscripts indicate that if we are not taking th e symmetrizing morphism
τ tw to deﬁne the functor τ Sym⊠⊕, then we take the ψ -twisted multiplication, for
ψ a bilinear form as in (16). Then (104) is an isomorphism.
Proof. We consider dual compactly supported cohomology, to match Theo rem 4.12.
In addition, we will assume that W = 0 to ease the notation a little — applying the
vanishing cycles functor to all of our arguments yields the general case by Lemma
5.3.
Let
d ∈ HNd be a Harder–Narasimhan type. Extending the notation Md′,d′′ ,
we let Md be the stack of all d-dimensional modules equipped with a ﬁltration by
submodules with the dimensions of successive subquotients given by d. We deﬁne
sd : Md → Md
to be the map of stacks given by forgetting the ﬁltration. In commo n with the map
sd′,d′′ of diagram (77), which corresponds to the special case d = (d′, d′′), the map
sd factors as a proper surjection and a closed inclusion, and is theref ore proper.
The Harder–Narasimhan type of the underlying d-dimensional module of a ﬁl-
tered module parametrised by a point of Md need not be d. On the other hand, by
the proof of [37, Prop.3.7], the proper map sd factors through the closed inclusion
of stacks
i≤d : Mζ
≤
d֒→Md.
By abuse of notation, for each dimension vector d we continue to denote by ηd,∗
the right inverse to the map
Dmon
M H (pd,!IC Md(Q)) → Dmon
M H
(
qζ
d,!pζ
d,!IC Mζ -ss
d
(Q)
)
deﬁned by the map already denoted ηd,∗. Given a stack N
r
− → Md over Md, we
denote by P(N) = Dmon
Md H(r!QN) the induced complex of mixed Hodge modules
62 BEN DA VISON AND SVEN MEINHARDT
on Md. Consider the commutative diagram
Mζ
≤
d
i≤d
/d38/d38▲▲▲▲▲▲▲▲▲▲▲▲
Mζ
d
rζ
d
/d15/d15
β
/d53/d53❧❧❧❧❧❧❧❧❧❧❧❧❧❧❧❧❧❧❧ γ /d47/d47 Md
α
/d79/d79
sd
/d47/d47
rd
/d15/d15
Md
Mζ -ss
d1 × . . . × Mζ -ss
ds
δ /d47/d47 Md1 × . . . × Mds
where the map α exists due to the comments above.
We consider the diagram of complexes of mixed Hodge modules
P(Mζ
≤
d)
β ∗
/d115/d115❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤
i≤d, ∗
/d41/d41❘❘❘❘❘❘❘❘❘❘❘❘❘❘❘❘
P(Mζ
d)
β ∗
/d50/d50
rζ
d, ∗
∼
=
/d15/d15
γ ∗
/d49/d49 P(Md)
α ∗
/d79/d79
γ ∗
/d111/d111
sd, ∗
/d47/d47
rd, ∗ ∼=
/d15/d15
P(Md)
L(d,d) ⊗ P (Mζ -ss
d1 × . . . × Mζ -ss
ds )
δ ∗
/d47/d47 L(d,d) ⊗ P (Md1 × . . . × Mds )δ ∗
/d111/d111
with ( d, d) deﬁned as in (73). The map δ∗ := L(d,d) ⊗
(
⊕∗(ηd1,∗ ⊠ . . . ⊠ηds,∗)
)
is
a right inverse to the natural restriction map δ∗. Then we deﬁne
γ ∗ := r−1
d,∗δ∗rζ
d,∗,
a right inverse toγ ∗. Then set β ∗ :=α ∗γ ∗. It can easily be veriﬁed that γ ∗ =β ∗α ∗,
and so β ∗ is a right inverse to β ∗.
The map ηd1,∗(H(Aζ
d1)) ⊠tw
⊕ . . . ⊠tw
⊕ ηds,∗(H(Aζ
d1 )) → H (Ad) has image in the
piece L(d,d)/2 ⊗P (Mζ
≤
d) of the ﬁltration of H(p∗IC0) by Harder–Narasimhan types.
By the commutativity of the above diagram, the resulting map
γ ∗
(
ηd1,∗(H(Aζ
d1 )) ⊠tw
⊕ . . . ⊠tw
⊕ ηds,∗(H(Aζ
d1 ))
)
→ L(d,d)/2 ⊗β ∗P(Mζ
≤
d)
is an isomorphism. Filtering the domain and the target of the map
Ψ : ⊠tw
⊕,∞
µ
− →−∞
(
ηµ ,∗(H(Aζ
µ ))
)
→ H(A)
by the ﬁltration indexed by the Harder–Narasimhan ﬁltration, it follo ws that the
associated graded morphism is an isomorphism between pure complex es of mixed
Hodge modules, and hence Ψ is an injection, and so an isomorphism, sin ce by
Theorem B the domain and image are isomorphic.
Sinceη∗
µ is a morphism of monoids, the diagram
η∗
µ
(τ )Sym⊠⊕
(
ηµ ,∗BPSζ
µ ⊗ H(BC*)vir
)
∼=
/d15/d15
/d47/d47η∗
µ H((¬ψ )Aµ )
∼
=
/d15/d15
(τ )Sym⊠⊕
(
BPSζ
µ ⊗ H(BC*)vir
)
/d47/d47
H((¬ψ )Aζ
µ )
commutes, with the horizontal maps deﬁned via the relative multiplica tions on
H((ψ )Aµ ) and H((ψ )Aζ
µ ) respectively. We deduce as above that the theorem is
true after passing to the associated graded with respect to the H arder–Narasimhan
COHAS AND QUANTUM ENVELOPING ALGEBRAS 63
ﬁltration, and so is injective, and hence an isomorphism since the dom ain and target
are isomorphic pure monodromic mixed Hodge modules by Theorems A a nd B. □
Corollary 6.13. For a generic stability conditionζ there exist embeddings BPSζ ,S
W,µ ⊗ H(BC*)vir ⊂
H((ψ )AW ) such that the induced morphism
⊠tw
⊕,∞
µ
− →−∞
(
(τ )Sym⊠+
(
BPSζ ,S
W,µ ⊗ H(BC*)vir
)) (¬ψ )H(˜∗W )
− − − − − − − →H(AS
W )
is an isomorphism.
The meaning of the bracketed superscripts is as in Theorem 6.12.
Proof. By Theorem 6.12 and Proposition 5.7, the corollary is true after repla cing
H(AS
W ) with the perverse associated graded Gr P(H(AS
W )) = H c(MS, dim! H(p∗ICW )).
Then for any lift of the embedding BPS ζ ,S
W,µ ⊗ H(BC*)vir ⊂ GrP(H(AS
W )) to an em-
bedding BPSζ ,S
W,µ ⊗ H(BC*)vir ⊂ H(AS
W ), the result follows. □
