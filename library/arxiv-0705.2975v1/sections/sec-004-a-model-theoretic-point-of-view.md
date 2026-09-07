---
doc_id: arxiv-0705.2975v1
doc_title: "On the Definitions of Difference Galois Groups"
section_id: sec-004-a-model-theoretic-point-of-view
section_title: "A Model-Theoretic Point of View"
section_number: null
pages: 15-18
source_pdf: 0705.2975v1.pdf
source_sha256: 683d6bd44cea6704
doc_brief: "On the Definitions of Difference Galois Groups — We compare several deﬁnitions of the Galois group of a linear diﬀerence equation that have arisen in algebra, analysis and model theory and sh ow"
---
4.1 Preliminary model-theoretic deﬁnitions and results
Deﬁnition 4.1 LetK be a diﬀerence ﬁeld with automorphism σ.
1. K is generic iﬀ
15
(∗) every ﬁnite system of diﬀerence equations with coeﬃcients in K and
which has a solution in a diﬀerence ﬁeld containing K, already has a solu-
tion in K.
2. A ﬁnite σ-stable extension M ofK is a ﬁnite separably algebraic extension of K such
that σ(M) = M.
3. The core of L over K, denoted by Core(L/K), is the union of all ﬁnite σ-stable
extensions of K which are contained in L.
One of the diﬃculties with diﬀerence ﬁelds, is that there are usually se veral non-isomorphic
ways of extending the automorphism to the algebraic closure of the ﬁeld. An important
result of Babbitt (see [5]) says that once we know the behaviour of σ on Core(K/K ), then
we know how σ behaves on the algebraic closure K of K.
Fix an inﬁnite cardinal κ which is larger than all the cardinals of structures considered
(e.g., in our case, we may take κ = |C|+ = (2 ℵ0)+). In what follows we will work in a
generic diﬀerence ﬁeld U, which we will assume suﬃciently saturated , i.e., which has the
following properties:
(i) ( ∗) above holds for every system of diﬀerence equations of size < κ (in inﬁnitely
many variables).
(ii) (1.5 in [4]) If f is an isomorphism between two algebraically closed diﬀeren ce subﬁelds
of U which are of cardinality <κ , then f extends to an automorphism of U.
(iii) Let K ⊂L be diﬀerence ﬁelds of cardinality < κ, and assume that K ⊂ U . If every
ﬁnite σ-stable extension of K which is contained in L K-embeds in U, then there is
a K-embedding of L in U.
Note that the hypotheses of (iii) are always veriﬁed if K is an algebraically closed subﬁeld
of U. If K is a diﬀerence ﬁeld containing the algebraic closure Q of Q, then K will embed
into U, if and only if the diﬀerence subﬁeld Q of K and the diﬀerence subﬁeld Q of U are
isomorphic. This might not always be the case. However, every diﬀer ence ﬁeld embeds into
some suﬃciently saturated generic diﬀerence ﬁeld.
Let us also recall the following result (1.12 in [4]): Let n be a positive integer, and
consider the ﬁeld U with the automorphism σn. Then ( U,σ n) is a generic diﬀerence ﬁeld,
and satisﬁes the saturation properties required of ( U,σ ).
Notation. We use the following notation. Let R be a diﬀerence ring. Then, as in the
previous sections, CR denotes the ﬁeld of “constants” of R, i.e., CR = {a ∈R |σ(a) = a}.
We let DR = {a ∈R | σm(a) = a for some m ⁄= 0}. Then DR is a diﬀerence subring of R,
and if R is a ﬁeld, DR is the relative algebraic closure of CR in R. We let D′
R denote the
diﬀerence ring with same underlying ring as DR and on which σ acts trivially. Thus CU is
16
a pseudo-ﬁnite ﬁeld (see 1.2 in [4]), and DU is its algebraic closure (with the action of σ),
D′
U the algebraic closure of CU on which σ acts trivially.
Later we will work with powers of σ, and will write Fix (σn)(R) for {a ∈R |σn(a) = a}
so that no confusion arises. If R = U, we will simply write Fix (σn). Here are some
additional properties of U that we will use.
Let K ⊂M be diﬀerence subﬁelds of U, with M algebraically closed, and let a be a tuple
of U. By 1.7 in [4]:
(iv) If the orbit of a under Aut(U/K) is ﬁnite, then a ∈K (the algebraic closure of K).
We already know that every element of Aut( M/KC M ) extends to an automorphism of U.
More is true: using 1.4, 1.11 and Lemma 1 in the appendix of [4]:
(v) every element of Aut( M/KC M ) lifts to an element of Aut( U/KC U ).
Recall that a deﬁnable subset S of U n is stably embedded if whenever R ⊂ U nm is deﬁnable
with parameters from U, then R ∩Sm is deﬁnable using parameters from S. An important
result ([4] 1.11)) shows that CU is stably embedded. Let d ≥ 1. Then, adding parameters
from Fix (σd), there is a deﬁnable isomorphism between Fix (σd) and C d
U . Hence,
(vi) for every d> 0, Fix (σd) is stably embedded, and
(vii) if θ deﬁnes an automorphism of DU which is the identity on DM , then θ extends
to an automorphism of U which is the identity on M.
We also need the following lemma. The proof is rather model-theoretic and we refer to
the Appendix of [4] for the deﬁnitions and results. Recall that if K is a diﬀerence subﬁeld
of U, then its deﬁnable closure, dcl( K), is the subﬁeld of U ﬁxed by Aut( U/K). It is an
algebraic extension of K, and is the subﬁeld of the algebraic closure K ofK which is ﬁxed
by the subgroup {τ ∈ Gal(K/K ) |σ−1τσ =τ }.
Lemma 4.2 LetK be a diﬀerence ﬁeld, and M be a ﬁnite σ-stable extension of KC U . Then
M ⊂KD U , i.e., there is some ﬁnite σ-stable extension M0 of K such that M ⊂M0DU .
Proof. Fix an integer d ≥ 1. Then, in the diﬀerence ﬁeld ( U,σ d), Fix (σd) is stably
embedded, dcl(K) = K and dcl(Fix (σd)) = Fix (σd). Denoting types in ( U,σ d) by tpd,
this implies
tpd(K/K ∩Fix (σd)) ⊢tpd(K/Fix (σd)). (♯)
Assume by way of contradiction that KC U has a ﬁnite σ-stable extension M which is
not contained in KD U . We may assume that M is Galois over KC U (see Thm 7.16.V in
[5]), with Galois group G. Choose d large enough so that σd commutes with all elements
of G, and M = M0DU , where M0 is Galois over KFix (σd). Then there are several non-
isomorphic ways of extending σd to M. As tpd(K/Fix (σd)) describes in particular the
KFix (σd)-isomorphism type of the σd-diﬀerence ﬁeld M, this contradicts (♯) (see Lemmas
2.6 and 2.9 in [4]).
17
