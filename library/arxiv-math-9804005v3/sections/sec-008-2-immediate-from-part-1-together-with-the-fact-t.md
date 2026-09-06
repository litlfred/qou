---
doc_id: arxiv-math-9804005v3
doc_title: "RINGS WITH AUSLANDER DUALIZING COMPLEXES"
section_id: sec-008-2-immediate-from-part-1-together-with-the-fact-t
section_title: "Immediate from part 1, together with the fact that M ∈ Db(ModA) implies"
section_number: 2
pages: 6-7
source_pdf: 9804005v3.pdf
source_sha256: 62d069533bb97a00
doc_brief: "RINGS WITH AUSLANDER DUALIZING COMPLEXES — A ring with an Auslander dualizing complex is a generalizati on of an Auslander-Gorenstein ring."
---
DM ∈ Db(ModB◦).
Remark 1.4. The noetherian hypothesis can be relaxed – dualizing complexes can
be deﬁned over any coherent algebra A (see [Ye1] or [Mi1]). The category of ﬁnitely
generated A-modules is then replaced by the category of coherent modules. Ma ny
deﬁnitions and results in our paper hold for coherent algebras, as c an be easily
checked.
Perhaps one can even work over an arbitrary algebra, using the ca tegory of
coherent complexes, as deﬁned by Illusie (see [SGA6] Expos´ e I).
Another direction to extend the theory is to allow k to be any commutative ring.
In this case the derived category of bimodules should be D(DGMod(A ⊗L
k B◦)),
where A ⊗L
k B◦ is a diﬀerential graded algebra. See [Ye3] Remark 1.12.
Remark 1.5. Miyachi proved a converse to Proposition 1.3(2): if there are con-
travariant triangle functors D(ModA) → D(ModB◦) and D(ModB◦) → D(ModA)
which send⨁ to∏ , preserve Db and induce duality on Db
f , then there is a dualizing
complex in D(Mod(A ⊗B◦)) (see [Mi2] Theorem 3.3).
Remark 1.6. There are examples of algebras A and B where there is a dualizing
complexR ∈ D(Mod(A ⊗B◦)), but there is no dualizing complex in D(ModAe); cf.
[WZ]. The algebras A and B are necessarily not derived Morita equivalent, since
given a tilting complex T ∈ D(Mod(B ⊗A◦)), the complex R ⊗L
B T ∈ D(ModAe)
would be dualizing (cf. [Ye3]).
There are Grothendieck spectral sequences for the isomorphism of functors
1Db
f (ModA) ∼=D◦D and 1Db
f (ModB◦) ∼=DD◦. For modules they take this form:
Proposition 1.7. Let R ∈ D(Mod(A ⊗B◦)) be a dualizing complex. Then there
are convergent double-Ext spectral sequences
Ep,q
2 := Extp
B◦ (Ext−q
A (M,R ),R ) ⇒M(1.8)
RINGS WITH AUSLANDER DUALIZING COMPLEXES 7
for all M ∈ ModfA, and
Ep,q
2 := Extp
A(Ext−q
B◦ (N,R ),R ) ⇒N(1.9)
for all N ∈ ModfB◦.
Proof. By symmetry it suﬃces to consider (1.8) only. We can assume R is a
bounded complex of bimodules with each Rq an injective module over A and B◦.
Given a nonzero ﬁnitely generated A-module M , deﬁne the complex
H := HomB◦(HomA(M,R ),R ).
Then the adjunction homomorphism M → H is a quasi-isomorphism. Pick a
positive integer d large enough so that Rq = 0 if |q|> d. Consider the decreasing
ﬁltration on H given by the subcomplexes
FpH := HomB◦ (HomA(M,R ),R ≥p).
Then F is an exhaustive ﬁltration, and it determines the convergent spect ral se-
quence (1.8).
Given M ∈ D+(ModA), there is a quasi-isomorphism M → I in D+(ModA),
where each Iq is injective and Ker( Iq →Iq+1) ⊂Iq is essential. Such I is unique
(up to a non-unique isomorphism), and it is called the minimal injective resolution
ofM (cf. [Ye1] Lemma 4.2). If M has ﬁnite injective dimension then I is bounded.
The next two results are straightforward generalizations of [ASZ] Lemma 2.2 and
Theorem 2.3, so the proofs are omitted.
Lemma 1.10. Let R ∈ D(Mod(A ⊗B◦)) be a dualizing complex, and let I be the
minimal injective resolution of R in Db(ModA). Let Zi := Ker(Ii →Ii+1) and let
M be a ﬁnitely generated left A-module. Then there exist f1,... ,f n ∈ Hom(M,Zi)
such that for every N ⊂⋂
j Ker(fj) the natural map Exti
A(M,R ) → Exti
A(N,R ) is
zero; or equivalently, the natural map Exti
A(M/N,R ) → Exti
A(M,R ) is surjective.
Theorem 1.11. Let R ∈ D(Mod(A ⊗B◦)) be a dualizing complex, let I be the
minimal injective resolution of R in Db(ModA), and let Zi := Ker(Ii → Ii+1).
Then:
