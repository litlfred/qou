---
doc_id: arxiv-1712.08953v1
doc_title: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY"
section_id: sec-029-26-j-brundan
section_title: "J. BRUNDAN"
section_number: 26
pages: 26-28
source_pdf: 1712.08953v1.pdf
source_sha256: 005e0b1ad63c173e
doc_brief: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY — The oriented skein category OS(z, t ) is a ribbon category which un- derpins the deﬁnition of the HOMFLY-PT invariant of an orien ted link, in the"
---
OS♭: The k -span of all ribbons with no components that are cups and in which pr op-
agating upward strands only cross underneath propagating down ward strands.
It is obvious that these are all locally unital subalgebras of OS. Also, OS is graded
as OS =⨁
d∈ZOS[d] with OS[d] spanned by all ribbons such that the total number
of cups minus the total number of caps equals d. This induces a grading on each
of the subalgebras above. Moreover, OS♯[0] = OS♭[0] = OS◦. We have already
introduced the right OS-module categories Mod- OS, lfdMod-OS and pMod-OS. We
adopt analogous notation for all of these other locally unital algebr as. Also let
fdMod-OS◦ =
∐
r,s≥0
fdMod-OS◦
r,s
be the category of (globally) ﬁnite-dimensional right OS◦-modules.
In the following lemma, we take tensor products of locally unital modu les over the
locally unital algebra K :=⨁
a∈⟨↑,↓⟩ k 1a < OS. In terms of the usual tensor product
⊗ over the ground ﬁeld k , we have that V⊗KW =⨁
a∈⟨↑,↓⟩V 1a⊗ 1aW .
Lemma 5.1. Multiplication deﬁne a vector space isomorphism
OS +⊗KOS◦⊗KOS− ∼
→OS.
Similarly, there are isomorphisms OS +⊗KOS◦ ∼
→OS♯ and OS◦⊗KOS− ∼
→OS♭.
Proof. We apply Theorem 1.2 to pick a basis for OS + consisting of cap-free generic
reduced lifts of matchings. Similarly, we pick a basis for OS−. Finally, we pick a basis
forOS◦ consisting of cup- and cap-free generic ribbons, all of whose right ward crossings
are positive and leftward crossings are negative. To prove the lemm a, it remains to
observe that the non-zero images of the pure tensors in these ba sis elements under the
multiplicationOS +⊗KOS◦⊗KOS−→OS give a basis for OS itself: it is just another
of the bases from Theorem 1.2 consisting of generic reduced lifts wit h all cups at the
top, all crossings of propagating strands in the middle, and all caps at the bottom of
the picture. □
Recall the Iwahori-Hecke algebras Hr from (3.6) and the homomorphism ır from
(3.7). Theorem 1.2 shows that this is an isomorphism. More generally, let
Hr,s :=Hr⊗Hs (5.1)
for any r,s≥ 0. Then there is an injective (but no longer surjective) homomorph ism
ır,s :Hr,s→ 1↓s↑rOS1↓s↑r (5.2)
sendingSi⊗ 1 to the positive crossing of the ith and (i + 1)th strands and 1 ⊗Sj
to the positive crossing of the (r +j)th and (r +j + 1)th strands, again numbering
strands from right to left.
Lemma 5.2. The map ır,s is an algebra isomorphism Hr,s
∼
→ 1↓s↑rOS◦
r,s1↓s↑r. More-
over, OS◦
r,s is isomorphic to the matrix algebra Mat(r+s
r )(Hr,s). Hence, the functor
Υ r,s :=?⊗Hr,s 1↓s↑rOS◦
r,s : Mod-Hr,s→ Mod-OS◦
r,s.
is an equivalence of categories, with quasi-inverse deﬁned by right multiplication by the
idempotent 1↓s↑r .
Proof. The ﬁrst statement follows from Theorem 1.2. To deduce the secon d statement,
let⟨↑,↓⟩r,s denote the
( r+s
r
)
diﬀerent words which have r letters↑ and s letters↓.
Note that OS◦
r,s =⨁
a,b∈⟨↑,↓⟩r,s 1aOS◦
r,s1b. For each a, b∈⟨↑,↓⟩r,s, let ea,b∈ 1aOS◦
r,s1b
ORIENTED SKEIN CATEGORY 27
be the unique (up to planar isotopy) reduced ( b, a)-ribbon which only involves pos-
itive rightward crossings and negative leftward crossings, and has no cups, caps or
upward/downward crossings. For example, ea,a = 1 a for each a. We have that
ea,beb′,c =δb,b′ea,c. Hence, the map
Hr,s→ 1aOS◦
r,s1b, f ↦→ea,↓s↑rır,s(f )e↓s↑r,b
is a bijection, and OS◦
r,s =⨁
a,b∈⟨↑,↓⟩r,sHr,sea,b is the matrix algebra as claimed. □
Next we are going to mimic the usual arguments of highest weight the ory for semi-
simple Lie algebras, with the role of “Borel subalgebra” being played b y OS♯, and the
role of “Cartan subalgebra” being played by OS◦. To parametrize the isomorphism
classes of irreducible representations of OS◦, we need some facts about the represen-
tation theory of the Iwahori-Hecke algebra Hr; e.g. see [DJ1].
The algebra Hr is semisimple if q is not a root of unity, with irreducible representa-
tions being the Specht modules S λ parametrized by partitions λ⊢r. To construct S λ
explicitly, recall the elementsxλ andyλ from (3.8). The right ideals xλHr andyλHr are
the permutation module Mλ and the signed permutation module Nλ, respectively. By
[DJ1, Theorem 3.3], the space Hom Hr (Mλ,Nλt) is one-dimensional. Then the Specht
module Sλ is the image of any non-zero homomorphism in this space.
The deﬁnition just given also makes sense when q is a root of unity (remembering
q2⁄= 1); the resulting Specht module S λ is related to the module S λ constructed in
[DJ1] by S λ∼= (Sλt
)#. In general, we deﬁne e to be the smallest positive integer such
that q2e = 1, setting e := 0 if q is not a root of unity. A partition λ is e-restricted if
either e = 0, or e >0 and λi−λi+1 < efor each i = 1, 2,... . For e-restricted λ⊢ r,
the Specht module S λ has irreducible head D λ, and these modules for all e-restricted
λ⊢r give a complete set of pairwise inequivalent irreducible right Hr-modules.
Let Yλ be a projective cover of D λ; since Hr is a symmetric algebra, this is also an
injective hull. If e = 0 we have simply that D λ = Sλ = Yλ, and they are all equal to
the right ideal eλHr where eλ is the Young symmetrizer from (3.9). In general, it is
known that Yλ has a ﬁnite ﬁltration 2 with sections Sµ, each appearing [S µ : Dλ] times.
Consequently,
[Yλ] =
∑
µ⊢r
[Sµ : Dλ][Sµ]
in the Grothendieck group K0(fdMod-Hr) of the Abelian category fdMod- Hr. We
refer to this decomposition as Brauer reciprocity; it may also be proved by lifting
idempotents.
Now let Bipr,s :={λ = (λ↑,λ↓)|λ⊢r,µ⊢s} be the set of bipartitions of (r,s ), and
lete-Bipr,s⊆ Bipr,s be the e-restricted ones. In particular, we denote the empty bipar-
tition (∅, ∅ ) by ∅∅∅ . From the previous paragraph, it follows that e-Bipr,s parametrizes
the irreducible Hr,s-modules. Applying Lemma 5.2, we get from them irreducible OS◦-
modules
D(λ ) := (Dλ↑⊠ Dλ↓ )⊗Hr,s 1↓s↑rOS◦
r,s. (5.3)
Deﬁne S( λ ) for λ ∈ Bipr,s and Y( λ ) for λ ∈ e-Bipr,s in similar ways, starting from
Sλ↑⊠ Sλ↓ or Y λ↑⊠ Yλ↓ , respectively. For λ ∈ e-Bipr,s, Y( λ ) is a projective cover
and an injective hull of D( λ ), and it has a ﬁltration with sections S( µ ) for µ∈ Bipr,s,
each appearing [S( µ ) : D( λ )] = [Sµ↑ : Dλ↑ ][Sµ↓ : Dλ↓ ] in the ﬁltration. Finally, we put
these modules all together: setting Bip := ∐
r,s≥0 Bipr,s and e-Bip := ∐
r,s≥0e-Bipr,s,
the modules{D(λ )| λ∈e-Bip} are a complete set of pairwise inequivalent irreducible
OS◦-modules.
2This is proved by applying the “Schur functor” to the analogo us result for the q-Schur algebra.
