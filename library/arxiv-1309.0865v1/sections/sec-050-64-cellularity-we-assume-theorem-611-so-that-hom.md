---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-050-64-cellularity-we-assume-theorem-611-so-that-hom
section_title: "Cellularity. We assume Theorem 6.11, so that Hom spaces are free leftR-modules"
section_number: 6.4
pages: 64-65
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
and localization is injective on Hom spaces.
Claim 6.16. For anyw ∈W , let Xw be the set of maps in D which, after localization, induce
the zero map on every Qw summand of their source object. Then Xw is a 2-sided ideal in D.
Proof. Left to the reader. □
Claim 6.17. The light leaves map LLw,e,f will be in Xv for anyv ≰ w.
Proof. This follows from Bruhat upper-triangularity . □
For anyI ⊂W , let LLI denote the span of all LL maps which factor throughw ∈I.
Now letI ⊂W be an ideal with respect to the Bruhat order. In other words, i fw ∈I
andv ≤w thenv ∈I.
Claim 6.18. When I is an ideal, LLI is a 2-sided ideal in D. It is equal to XW \I, the
intersection of the ideals Xw for eachw /∈I.
Proof. We need only show that LLI is equal to XW \I, for the latter is clearly a 2-sided
ideal. The inclusion LLI ⊂ X W \I follows from the previous claim.
Now suppose that φ ∈ Hom(w,y ) is in XW \I, and write φ as a linear combination
of LL maps. Unless φ is zero, some LLw,f ,e has a non-zero coefﬁcient. Choose w, e,
and f successively such that each is maximal in the Bruhat/path do minance order
relative to the constraint that, with the previous choices, there is a nonzero coefﬁcient
for LLw,f ,e inφ. Because of upper triangularity , this is the only coefﬁcien t which can
possibly contribute to a map fromQe toQf , and it does contribute in a non-zero way .
Thereforeφ induces a nonzero map on Qe, implying that w ∈I. Since this is true for
each maximal choice of w, we see that φ ∈ LLI. □
It is clear that if w andw′ are rexes for w ∈W , then any two rex moves Bw →Bw′
are equal modulo LL<w. Both rex moves are in LL≤w, and induce the identity map
on the unique Qw summand after localization.
Now lety =x. Recall that LLw,f ,e =LLx,f ◦LLx,e, factoring through w in the mid-
dle. Suppose we compose them in the opposite order, to get an e ndomorphism of
Bw. We have an LL basis for endomorphisms ofBw as well, and there is a unique light
leaves morphism which induces a nonzero map on the unique sta ndard summand
Qw. This map can be any rex move, and though we often assume for co nvenience
that it is the identity , this assumption is not necessary . Le tψ(e, f) denote the coefﬁ-
cient of this light leaves morphism inside the composition LLw,e ◦LLw,f .
Claim 6.19. Letx,y,z be arbitrary. Fix w ∈W , and choose subsequences e ofx, f and g of
y, and h ofz which all express w. Then the composition LLh,gLLf ,e : Bx → Bz is equal to
ψ(g, f)LLh,e modulo LL<w.
SOERGEL CALCULUS 65
Proof. LLh,gLLf ,e is a composition of four maps, the inner ones being LLy,gLLy,f .
This composition is equal to ψ(g, f) times the identity of Bw, plus maps in LL<w.
Therefore the overall composition is equal to ψ(g, f)LLz,hLLw,e modulo LL<w, as
desired. □
Claim 6.20. Leta : By → Bz be an arbitrary morphism, and LLw,e,f be a light leaves map
Bx → By factoring through the rex Bw. Then aLLw,e,f = ∑
f ′ra(f, f ′)LLw,e,f ′ modulo
LL<w. The sum runs over subexpressions f ′ ofz expressingw. The coefﬁcients ra(f, f ′) do
not depend on e.
Proof. WriteaLLe,f = aLLy,fLLw,e, and consider aLLy,f as a map from Bw → Bz.
The space of maps Bw →Bz modulo LL<w is spanned by {LLz,f ′} over all f ′, so that
aLLy,f = ∑
f ′ra(f, f ′)LLz,f ′ modulo lower terms. Composing with LLx,e once more,
we get the desired result. □
Deﬁnition 6.21. Letι : D → D op denote the antiinvolution which preserves objects
and ﬂips diagrams upside-down.
Note that this reverses vertical composition, but not horiz ontal composition (ι is
monoidal and contravariant). Clearly ι(LLf ,e) = LLe,f .
For the deﬁnition and basic properties of cellular categori es, see [Wes09].
Proposition 6.22. The category D is cellular, with cellular basis LL (for any appropriate
choice of LL maps) and antiinvolution ι.
This proposition follows from the previous claim. The cells correspond to w ∈W
with the Bruhat order, and the set M(x,w ) consists of all subsequences of x express-
ingw. We do not know of any interesting interactions between the c ellular structure
and the monoidal structure.
