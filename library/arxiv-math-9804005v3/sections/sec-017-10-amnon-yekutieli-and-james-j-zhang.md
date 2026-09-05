---
doc_id: arxiv-math-9804005v3
doc_title: "RINGS WITH AUSLANDER DUALIZING COMPLEXES"
section_id: sec-017-10-amnon-yekutieli-and-james-j-zhang
section_title: "AMNON YEKUTIELI AND JAMES J. ZHANG"
section_number: 10
pages: 10-11
source_pdf: 9804005v3.pdf
source_sha256: 62d069533bb97a00
doc_brief: "RINGS WITH AUSLANDER DUALIZING COMPLEXES — A ring with an Auslander dualizing complex is a generalizati on of an Auslander-Gorenstein ring."
---
Example 1.17. Let A be the non-catenary noetherian commutative local ring of
[Na] Appendix, p. 203 Example 2. Then again there is no dualizing comple x in
Db(Mod(A ⊗B◦)) for any right noetherian k-algebra B.
2. Auslander Dualizing Complexes
The basic ideas in this section already appear in [Ye2] Section 1 (which t reats
graded algebras).
Assume R ∈ Db(Mod(A ⊗B◦)) is a dualizing complex. Let M be a ﬁnitely
generated A-module. The grade of M with respect to R is
jR;A(M ) := inf {q | Extq
A(M,R ) ⁄= 0} ∈ Z ∪ {∞}.
Similarly deﬁne jR;B◦ for a B◦-module.
We are ready to deﬁne the notion appearing in the title of the paper.
Deﬁnition 2.1. Let A and B be k-algebras, with A left noetherian and B right
noetherian, and let R ∈ D(Mod(A ⊗B◦)) be a dualizing complex. We say that R
has the Auslander property, or that R is an Auslander dualizing complex , if
(i) for every ﬁnitely generated A-module M , integer q and B◦-submodule N ⊂
Extq
A(M,R ), one has jR;B◦ (N ) ≥q.
(ii) the same holds after exchanging A and B◦.
Note that the role of the algebras A andB◦ is symmetric. Also note that if R is
an Auslander dualizing complex, then any shift R[n] is also an Auslander dualizing
complex (the shift cancels out in the double dual).
Example 2.2. Let A be a commutative k-algebra and R a central dualizing com-
plex over it. From Proposition 1.12 it is clear that R is Auslander. For a prime
ideal p one has jR;A(A/p) = d(p).
Example 2.3. (a) If A is Gorenstein, i.e. the bimodule A has ﬁnite injective di-
mension on both sides, then R = A is a dualizing complex over A. If A is an
Auslander-Gorenstein ring in the sense of [Bj], then R =A is an Auslander dualiz-
ing complex.
(b) IfA is a ﬁnite k-algebra, i.e. rankkA< ∞, then the bimodule A∗ := Homk(A,k )
is injective on both sides, and R = A∗ is an Auslander dualizing complex over A.
Clearly jR;A(M ) = 0 for all M .
(c) Let A be the matrix algebra
( k V
0 k
)
where V is a ﬁnite rank k-module. Since A
is hereditary it is also Gorenstein, so both A and A∗ are dualizing complexes, and
if V ⁄= 0 they are non-isomorphic. According to [ASZ] Example 5.4, the dua lizing
complex A is Auslander iﬀ rank kV ≤ 1. See also [Ye3] Section 3.
More examples of algebras with Auslander dualizing complexes are in Ex amples
6.11-6.15.
The next deﬁnition is taken from [MR] Section 6.8.4 (with a slight modiﬁca tion
– we allow negative dimensions).
Deﬁnition 2.4. An exact dimension function is a function dim which assigns to
each module M ∈ ModfA a value dim M in an ordered set containing −∞, R and
some inﬁnite ordinals, and satisﬁes the following axioms:
(i) dim 0 = −∞.
RINGS WITH AUSLANDER DUALIZING COMPLEXES 11
(ii) For every short exact sequence 0 →M ′ →M →M ′′ → 0 one has dim M =
max{dimM ′, dimM ′′}.
(iii) If pM = 0 for some prime ideal p, and M is a torsion A/p-module, then
dimRM ≤ dimRA/p − 1.
Familiar examples of exact dimension functions are the Krull dimension Kdim
and (sometimes) the Gelfand-Kirillov dimension GKdim.
Lemma 2.5. A function dim deﬁned on ModfA and satisfying axioms (i)-(ii)
(resp. axioms (i)-(iii)) extends uniquely to a function on ModA, satisfying axioms
(i)-(ii) ( resp. axioms (i)-(iii)) and the axiom
(iv) dim M = sup{dimM ′ |M ′ ⊂M ﬁnitely generated }.
The proof of the lemma is standard.
Usually we will have a pair of dimension functions, one on ModA and the other
on ModB◦; when necessary we shall distinguish between them by writing dim A and
dimB◦ respectively.
Deﬁnition 2.6. An exact dimension function dim is called ﬁnitely partitive if given
a ﬁnitely generated module M there is a number l0, such that for every chain of
submodules M =M0 ⫌ M1 · · · ⫌ Ml with dimMi/Mi+1 = dimM one has l ≤l0.
In the next two deﬁnitions (taken from [ASZ] and [Ye2]) dim denotes a function
on ModA satisfying axioms (i), (ii) and (iv).
Deﬁnition 2.7. 1. A module M is called dim -pure if dimM ′ = dimM for every
nonzero submodule M ′ ⊂M .
