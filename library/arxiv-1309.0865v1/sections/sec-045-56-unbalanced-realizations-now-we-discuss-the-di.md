---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-045-56-unbalanced-realizations-now-we-discuss-the-di
section_title: "Unbalanced realizations. Now we discuss the diagrammatic alterations which"
section_number: 5.6
pages: 55-57
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
must be made to accommodate the case of non-balanced realiza tions. This was dis-
cussed for dihedral groups in the appendix to [Elib], where t wo separate diagram-
matic conventions are proposed to deal with the new bookkeep ing required. We
follow the second suggested convention from that appendix.
Fix a dihedral parabolic subgroup with m = mst < ∞. Relation (5.7) implies that
there is a close connection between 2m-valent vertices and two-colored Jones-Wenzl
projectors. However, this begs the question: which Jones-W enzl projector? After all,
the left-blue-aligned Jones-Wenzl projector is not equal to the rotation of the left-red-
aligned one. A careful examination of (5.7) and (5.16) shows that different choices of
Jones-Wenzl projector must be made, depending on the locati on of the dot and the
orientation of the 2m-valent vertex.
If some rescaling of (5.7) is to hold, for any positioning of t he dot and the 2m-
valent vertex, then the Jones-Wenzl projector must satisfy the death by pitchfork
property (5.17). In particular, JW m−1 must be negligible, and must have some rota-
tional eigenvalue. This is not possible when the realizatio n is even-unbalanced (see
[Elib] for more details). While one may be able to design a dia grammatic calculus
for even-unbalanced realizations, we will not attempt to do so. When m is even and
[m − 1] = 1 , all the two-color relations above hold as stated.
The 2m-valent vertex is supposed to correspond, under the functor F , to some
non-zero morphism between bimodules, living in a one-dimen sional space of mor-
phisms. Let w(s) denote the reduced expression ...tsts of length m ending in s, and
let w(t) denote the reduced expression ...stst of length m ending in t. There is a
unique bimodule map f(s) : BS (w(t)) → BS (w(s)) which sends the 1-tensor to the
1-tensor, and a unique map f(t) : BS (w(s)) → BS (w(t)) which does the same. How-
ever, when the realization is not balanced, these maps are no t rotations of each other
(by one strand), and this is the underlying issue. However, t hese maps are individ-
ually invariant under color-preserving rotations (just li keJW m−1, even in the odd-
unbalanced case), so we may draw each unambiguously as some k ind of 2m-valent
vertex. We label the vertices (s) or (t) to distinguish the two. (We only draw the case
whenm is odd, but nothing prevents drawing the even case too.)
The purple strand is meant to encode the appropriate sequenc e of alternating red
and blue strands. To reiterate, when the blue-centered 2m-valent vertex is oriented
such that its upper-right strand is blue (as in the picture ab ove), then it corresponds
under F to a morphism which preserves the 1-tensor. When the blue-ce ntered 2m-
valent vertex is oriented such that its upper-right strand i s red, one differs from this
map by an invertible scalar λ. In [Elib], this scalar λ = [ m − 1]y is discussed at
56 BEN ELIAS AND GEORDIE WILLIAMSON
additional length. Therefore, one has the rotational relat ion:
(5.30) = =λ λ −1
When we place a dot on a 2m-valent vertex, we obtain a relation similar to (5.7).
(5.31)
= =
= =
JW m−1 JW m−1
JW m−1 JW m−1
In each case, the version of the Jones-Wenzl projector used i s the one whose coef-
ﬁcient of the identity is 1, when color-aligned as above. By rotating these pictures,
one knows how to place a dot on any strand in either 2m-valent vertex. To check that
these relations make sense, observe that both sides send the 1-tensor to the 1-tensor.
To give the correct versions of (5.6) and (5.16), one should l abel the 2m-valent
vertices in such a way that both sides preserve the 1-tensor.
(5.32) = =
(5.33) = JW
There are additional, color-switched versions of each of th ese relations.
Finally , to give the correct version of the three-color rela tions, one should again
ensure that both sides preserve the 1-tensor. Here is the A3 relation.
(5.34) =
Note that, when working with these diagrams, there is a scala r ambiguity that
appears when deﬁning a rex move, determined by the choice of c entral color on
each 2m-valent vertex. Our convention is that one will always choos e a coloring so
that the 1-tensor is preserved by the rex move.
SOERGEL CALCULUS 57
For the remainder of this paper, we will work solely with the b alanced case, and
thus will not need the extra confusion of labeled 2m-valent vertices. In the rest of the
paper, it is roughly the case that diagrams are only importan t “up to scalar.” That
is, we will be asking whether certain morphisms span or are li nearly independent,
and these concepts are not affected by rescaling. It should n ot be hard to convince
oneself that the remainder of this paper applies equally wel l to the odd-unbalanced
case.
Part 3. Light leaves morphisms and proofs
