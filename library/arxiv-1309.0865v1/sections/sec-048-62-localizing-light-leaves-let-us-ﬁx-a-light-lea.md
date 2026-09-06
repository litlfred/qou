---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-048-62-localizing-light-leaves-let-us-ﬁx-a-light-lea
section_title: "Localizing light leaves. Let us ﬁx a light leaves map LLx,e, with e expressing"
section_number: 6.2
pages: 60-62
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
w. Let w be the target of the map. Now consider what happens after the p assage
D → Kar(DQ). The target Bw splits up into standard summands, with a unique
summand isomorphic to Qw. For each subsequence f of x which also expresses w
we have a summand Qf
⊕
⊂ Bw isomorphic to Qw, and this is sent by LLw,e into the
unique summand Qw
⊕
⊂ Bw with some coefﬁcient pe
f ∈ Q. For the conventions used
to calculate this coefﬁcient, see section 5.5. A priori this coefﬁcient depends on the
choices made in the construction of LLw,e.
Proposition 6.6 (Path Dominance Upper-triangularity) . If pe
f ⁄= 0 then f ≤ e in the
path dominance order. Moreover,pe
e is non-zero, and is a product of roots independent of the
choice ofLLx,e.
Proof. Let us use the same notation as the previous section, so that wk is the element
expressed by (w≤k, e≤k). We write vk for the corresponding element with e replaced
by f.
Remember thatLLw,e is deﬁned inductively , beginning with LLk =LLw≤k,e≤k ⊗ /BD .
The target of LLk is wk, a rex for wk, which only has standard summands corre-
sponding to elements u ≤ wk. Therefore LLk will clearly act as zero on Qf≤k unless
vk ≤ wk. Thus LLw,e will act as zero on Qf unless vk ≤ wk for every k, which is
exactly the condition for f ≤ e in the path dominance order. The upper-triangularity
now follows.
We now turn to an explicit formula for pe
e. For each k ≤ ℓ(x) deﬁne a root αk as
follows:
αk
def=



wk−1(αxk) if ek is U0,
−wk−1(αxk) if ek is D1,
1 otherwise.
Note that wk−1(αxk) is the coefﬁcient one obtains if one places αxk in the region just
before wk, as an element of Qe, and pulls it to the far left region. We claim that
pe
e = ∏ l(x)
k=1αk.
SOERGEL CALCULUS 61
FIGURE 3. Calculating pe
e
U0
D0
=
α
β
γ
D1
= −
αα
ββ
Consider what happens at the k-th step, when one includes from either /BD or Qs
intoBs, and then follows φk, the inductive part of an LL map (see ﬁgure 6.2). First
let us take care of all the cases when ek is 0. If ek is U0 then φk is a dot and the
inclusion from R is a dot, leaving us with a factor of αs in that spot, which we drag
left to obtain αk. If ek is D0 then φk is a trivalent vertex; the dot from the inclusion
pulls into the trivalent vertex, leaving nothing behind. Wh at remains is an LL map
with all 0’s removed (with a coefﬁcient), so it is enough to ch eck the formula when e
consists only of 1’s.
Remember that bivalent vertices “pull through” rex moves, a s in relation (5.28).
All that remains of the LL map is rex moves and caps. If ek is U1 then one has a
bivalent vertex as the inclusion map, which will eventually pull through braids and
run into either a D1 or the top of the diagram. If it runs into th e top, it will precisely
cancel the projection map on top, leaving no coefﬁcient. If ek is D1 then the bivalent
vertex meets a bivalent vertex from an earlier U1, and using r elation (5.25) we obtain
a factor of −αs, which pulls left to become αk, as in ﬁgure 6.2.
What we obtain is precisely the standard diagram representi ng the only map from
Qe toQw, with a polynomial on the left equal to ∏ l(w)
k=1αk. □
Remark 6.7. Do not believe that just because pe
e did not depend on the choice of rex
moves in the construction of LLw,e, that no coefﬁcients do. When f < e, pe
f does
depend on the rex moves chosen. Here is an example, where w = (s,t,s,s,t,s ) in
typeA2, e = (1, 1, 1, 1, 1, 1) and f = (0, 0, 0, 0, 0, 0).
= =α 2
bα r α bα r(α b +α r)
However, it is a priori clear that all coefﬁcients pe
f are either products ofW -conjugates
of simple roots, or are zero.
Corollary 6.8. Fix an expression x and let LLx,w be a set consisting of one light leaves
map LLx,e : Bx → Bw for each subexpression e expressing w. Now consider the maps
Bx,Q →Qw in Kar(DQ) obtained by postcomposing LLx,e with the projection Bw,Q →Qw.
62 BEN ELIAS AND GEORDIE WILLIAMSON
These maps form a basis for Hom(Bw,Q,Q w). Moreover, the original set LLx,w is linearly
independent overR as a subset of Hom(Bx,B w).
Proof. The morphism space Bw,Q → Qw is the direct sum, for each f expressing
w, of the morphism space Qf → Qw. The basis result now follows from upper-
triangularity , and the invertibility of the diagonal inQ. Linear independence follows
immediately . □
This corollary is essentially Libedinsky’s theorem [Lib08 ], and we have now pre-
sented a diagrammatic proof for it, entirely within the cont ext of D and Dstd (i.e.
without ever using bimodules). As soon as one knows that the d imensions of Hom
spaces is given by the standard pairing (as is the case for Soe rgel bimodules by 3.15)
it follows by counting dimensions that the set LLw,e gives a basis of Hom(Bw,R ).
