---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-091-a-general-setting-of-the-problem
section_title: "General setting of the problem"
section_number: A
pages: 137-140
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
Let C a commutative ring and C an abelian C-linear category. We ﬁx a
ﬁnitely graded object:
P = P1 ⊕· · · ⊕Pk,
and intend to classify pairs (M, u) made up of a ﬁnitely ﬁltered object:
M = (0 = M0 ⊂M1 ⊂· · · ⊂Mk = M),
and of an isomorphism from grM to P:
u = (ui : Mi/Mi−1 ≃Pi)1≤i≤k.
As easily checked, it amounts to the same as giving k exact sequences:
0 →Mi−1
wi
→Mi
vi→Pi →0.
1. This is all the more necessary since the work [40] by the ﬁrst two authors strongly
relies on this explicit description.
132
APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFERENCE MODULES
The pairs (M, u) and (M′, u′) are said to be equivalent if (with obvious no-
tations) there exists a morphism from M to M′ which is compatible with the
ﬁltrations and with the structural isomorphisms, that is, making the following
diagram commutative:
grM
u
!❈
❈
❈
❈
❈
❈
❈
❈
grf
/ grM′
u′
|③③③③③③③③
P
In the description by exact sequences, the equivalence relation translates as
follows: there should exist morphisms fi : Mi →M′
i making the following
diagrams commutative:
0 −−−−→Mi−1
wi
−−−−→Mi
vi
−−−−→Pi −−−−→0
yfi−1
yfi
yIdPi
0 −−−−→M′
i−1
w′
i
−−−−→M′
i
v′
i
−−−−→Pi −−−−→0
Note that such a morphism (if it exists) is automatically strict and an iso-
morphism.
We write F(P1, . . . , Pk) the set (2) of equivalence classes of pairs (M, u).
A.1.1. Small values of k. — For k = 1, the set F(P1) is a singleton. For
k = 2, the set F(P1, P2) has a natural identiﬁcation with the set Ext(P2, P1)
of classes of extensions of P2 by P1, which carries a structure of C-module (3).
The identiﬁcation generalizes the one that was described in proposition 2.3.9
and can be obtained as follows. To give a ﬁltered module M = (0 = M0 ⊂
M1 ⊂M2 = M) endowed with an isomorphism from grM to P1 ⊕P2 amounts
to give an isomorphism from M1 to P1 and an isomorphism from M/M1 to
P2, that is, a monomorphism i from P1 to M and an epimorphism p from M
to P2 with kernel i(P1), that is, an exact sequence:
0 →P1
i→M
p→P2 →0,
2. We admit that F(P1, . . . , Pk) is indeed a set; from the devissage arguments that follow,
(see A.1.2), it easily seen to be true if all the Ext spaces are sets, e.g. in the category of left
modules over a ring.
3. Note however that the latter comes by identifying Ext with Ext1, and that there
are two opposite such identiﬁcations, see for instance [15], exercice 1, p. 308.
We shall
systematically use the conventions of [12] and, from now on, make no diﬀerence between
Ext and Ext1.
A.1. GENERAL SETTING OF THE PROBLEM
133
that is, an extension of P2 by P1. One then checks easily that our equivalence
relation thereby corresponds with the usual isomorphism of extensions.
When k = 3, the description of F(P1, P2, P3) amounts to the classiﬁ-
cation of blended extensions (“extensions panach´ees”).
These were intro-
duced by Grothendieck in [25].
We refer to the studies [5, 6] by Daniel
Bertrand (4), whose conventions we use. Start from a representative of a class
in F(P1, P2, P3), in the form of three exact sequences:
0 →M0
w1
→M1
v1
→P1 →0,
0 →M1
w2
→M2
v2
→P2 →0,
0 →M2
w3
→M3
v3
→P3 →0.
Also recall that M0 = 0 and M3 = M. These give rise to two further exact
sequences; ﬁrst:
0
/ P1
w2◦v−1
1 / M2
v2
/ P2
/ 0
Indeed, v1 : M1 →P1 is an isomorphism, so that v−1
1
: P1 →M1 is well deﬁned;
and the exactness is easy to check. To describe the second exact sequence,
note that v2 : M2 →P2 induces an isomorphism v2 : M2/w2(M1) →P2,
whence (v2)−1 : P2 →M2/w2(M1); then w3 : M2 →M3 = M induces a
morphism w3 : M2/w2(M1) →M′, where we put M′ := M/w3 ◦w2(M1), and,
by composition, a morphism w3 ◦(v2)−1 : P2 →M′; last, v3 : M3 →P3 is
trivial on w3(M2), therefore on w3 ◦w2(M1), so that it induces a morphism
v3 : M′ →P3. Now we get the sequence:
0
/ P2
w3◦(v2)−1
/ M′
v3
/ P3
/ 0
We leave for the reader to verify the exactness of this sequence. These two
sequences can be blended (“panach´ees”) to give the following commutative
4. Also see the revised version “Extensions panach´ees autoduales”, to be found on
http://www.math.jussieu.fr/ bertrand/Recherche/recherche.html.
134
APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFERENCE MODULES
diagram of exact sequences:
0

0

0
/ P1
w2◦v−1
1
/ M2
v2
/
w3

P2
/
w3◦(v2)−1

0
0
/ P1
w3◦w2◦v−1
1
/ M
can /
v3

M′
/
v3

0
P3

P3

0
0
(We call can the canonical projection from M to M′.) Conversely, starting
from such a diagram of blended extensions, we recover a representative (M, u)
of a class in F(P1, P2, P3) as follows. The module M is the one sitting at the
center of the diagram. The submodule M1 is the image of P1 by the monomor-
phism w3 ◦w2 ◦v−1
1 . Then, M2 is the preimage by can of the submodule of M′
deﬁned as the image of P2 by w3 ◦(v2)−1. Of course, M0 := {0} and M3 := M.
The structural morphisms ui, i = 1, 2, 3, are easy to deﬁne. It can then be
proven that one thus gets a bijective mapping from F(P1, P2, P3) to the set of
equivalence classes of diagrams of blended extensions. (Note however that, in
loc. cit., D. Bertrand is interested by a slightly diﬀerent equivalence relation.)
Actually, one can even deﬁne a category on both sides of this correspondence
and get an equivalence of these categories, see [52].
