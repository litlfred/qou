---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-047-61-diagrammatics-for-light-leaves-fix-a-rex-w-we
section_title: "Diagrammatics for light leaves. Fix a rex w. We want to ﬁnd a basis of dia-"
section_number: 6.1
pages: 57-60
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
grams for the space of morphisms Bx → Bw modulo “lower terms.” Here, lower
terms are morphisms which induce the zero map to the unique st andard summand
Qw
⊕
⊂ Bw after localization. This basis will be parametrized by subs equences e ofx
which expressw. Libedinsky associates a morphism LLw,e to e, although this choice
is not canonical. In fact, there are many valid choices for wh at each LLw,e can be,
and selecting one morphism for each e will give a basis modulo lower terms. Thus
we will give a general rubric for selecting LLw,e, which does not specify a single map
but a set of maps, any of which will sufﬁce. See Remark 6.3 belo w on how to be more
speciﬁc.
Recall that a rex move is a morphism constructed from 2m-valent vertices which
corresponds to a path in the reduced expression graph of some elementw ∈W . Rex
moves have degree 0. When the realization is unbalanced, there is an ambiguity
when deﬁning the rex move associated to a path, which amounts to an invertible
scalar. This scalar will be irrelevant for our discussion be low: a rescaled basis is
a basis still. However, we use the convention that rex moves a lways preserve the
1-tensor.
Construction 6.1. For every (x, e) expressingw and everyk ≤ℓ(x), we let (x≤k, e≤k)
be the ﬁrst k terms, expressing an element wk, and let x>k denote the remaining
terms. When x is the empty set and e its unique subsequence, the map LLw,e is
the empty diagram. Suppose that, by induction, we have alrea dy chosen a map
LLk−1
def= LLx≤k−1,e≤k−1 : Bx≤k−1 →Bwk−1 for some rex wk−1 ofwk−1. Suppose that the
next index xk is s. By placing a vertical line /BD
s next to LLx≤k−1,e≤k−1 we get a map
fromBx≤k →Bwk−1 ⊗Bs. We will now choose a map φk : Bwk−1 ⊗Bs →Bwk for some
rexwk ofwk. The composition will be LLk
def= LLx≤k,e≤k.
58 BEN ELIAS AND GEORDIE WILLIAMSON
FIGURE 2. The Four Maps
The Wise Map D1
α
β
The Wicked Map D0
α
β
The Simple Map U0
α
The Map Who Does
Not Know To Ask  U1
α
It follows that LLw,e is a composition φℓ(w) ◦φℓ(w)−1 ⊗ /BD ◦ · · · ◦φ1 ⊗ /BD , where at the
k-th step /BD denotes the identity map of Bw>k. The composition of the ﬁrst k terms is
LLk ⊗ /BD
Bw>k
.
(6.1) = LLkLLk−1
wk−1
wk
φ k
s
There are four possibilities for the map φk, depending on ek. To obtain φk follow
these three steps (see also ﬁgure 2):
• If ek is either U1 or U0, do nothing. If ek is either D0 or D1, then s is in the
right descent set of wk−1. Apply β ⊗ /BD
Bs, whereβ is some rex move fromwk−1
to a rex with s on the right. Now the top has Bs ⊗Bs on the far right.
• If ek is U1 do nothing. If ek is U0, apply a dot to the rightmost Bs. If ek is D1,
apply a cap to the ﬁnal Bs ⊗Bs. If ek is D0, apply a merging trivalent vertex
to the ﬁnal Bs ⊗Bs.
• We have now reached some reduced expression for wk. Now apply some rex
moveα to get to the desired rex wk.
As expected, the degree of the morphism LLw,e is +1 for each U0 and −1 for each
D0 and hence agrees with defect of e. Note also that the width (i.e. number of
strands) always weakly decreases from bottom to top in an LL map.
Example 6.2. Here is a possible map LLw,e forw =rbrgbrr withmbr = 3 andmbg =
mgr = 2, and for e = 1111010.
Remark 6.3. Clearly there are many choices in this construction. The ﬁrs t important
choice is which rex w is the ﬁnal target. If one is to compare LLx,e with LLx,f for
two subsequences e, f both expressing w, then they should have the same target w,
and this is generally assumed. However, at each step in the in ductive construction
one needs to choose a rex wk, and there is no particular need to be consistent with
this choice. For instance, the intermediate map LLk in the construction of LLx,e
SOERGEL CALCULUS 59
need not equal the map we constructed for LLx≤k,e≤k. There is even no need for
the intermediate rex wk to agree with the ﬁnal target for the chosen map LLx≤k,e≤k.
When ek is D0 or D1, one has a free hand to choose which rex with s on the right
will be factored through, and which rex move β will take us there. The rex move α
is also freely chosen, and by no means does it have to be the sho rtest or easiest way
to traverse the reduced expression graph Γ w.
To be absolutely precise, i.e. to make the above constructio n into an algorithm,
one should ﬁx once and for all the following data:
(1) For each w ∈W , a rex w.
(2) For each w ∈ W and each index s ∈ S in the right descent set of w, a rex ws
which ends in s.
(3) For any two rexes w1 andw2 in forw, a rex move from w1 tow2.
This is not the only way to make the algorithm precise.
The more precise one is, the more annoying certain statement s get. Flexibility will
be more useful. However, at some point (in the ﬁnal chapter) w e will have to show
how one set of choices “spans” all the other possible choices .
Remark 6.4. When e = (1, 1,..., 1), it is a sequence of all U1 precisely when w is a
reduced expression. If so, the set of possible LLw,e is precisely the set of rex moves.
The most convenient choice is for LLw,e to be the identity map.
Now suppose that (w, e) has length k, and the ﬁrst k − 1 terms are all U1, a rex
forwk−1. In the construction of LLw,e we may choose LLk−1 to be the identity map,
meaning that LLw,e = φk. Thus for any sequence (w, e) the map φk is a valid choice
forLLw′,e′, wherew′ =wk−1s and e′ = (1, 1, 1,..., 1, ek). This observation gives us a
different inductive way to look at light leaves:
= 1 1
LLk
LLk+n
LLn+l(wk)
One should think of the top of an LL map as being a rex labelled with all U1’s, for
the purpose of further LL maps.
We will write LLx,w to indicate a set consisting of one ﬁxed choice of LLx,e for
each subexpression e of x expressing w. When we speak of the “span” of LLx,w,
we mean all morphisms obtained as linear combinations of LL maps, with polyno-
mials appearing in the left-most region. Note that LL maps themselves never have
polynomials in any region.
Remark 6.5. Not every diagram is in the light leaves basis. Here is a diagr am which
is not in the light leaves basis, and a description of it as an R-linear combination of
LL maps.
= + −
0 1 1 1 1 0 1 0 1
60 BEN ELIAS AND GEORDIE WILLIAMSON
Here is a diagram which is not in the span of LL maps at all, because it factors
through “lower terms.”
However, when viewed under adjunction as a map to ∅, it is an LL map.
1 0 0 0 0 1
Note that ∅ has no lower terms, so that LLx,e should genuinely form a basis for
HomD(Bx, /BD ).
