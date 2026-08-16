---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkaidˆo lectures in Arithmetic Geometry Yves Andr´ e (with appendices by F. Kato and N. Tsuzuki)"
section_id: sec-307-1-ssπtemp
section_title: "(S,s)→πtemp"
section_number: 1
pages: 135-137
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp Tôhoku-Hokkaidô lectures in Arithmetic Geometry Yves André (with appendices by F. Kato and N. Tsuzuki) — 580 sections: INTRODUCTION; INTRODUCTI"
---
1 (S,s)).
Theorem 2.1.11. Assume that K is algebraically closed of characteristic
zero. Let S be a (paracompact strictly) normal connectedK-analytic spaceS,
and let Z be a closed analytic subset such that S :=S\Z is smooth. Assume
that for any point s of S, there is a covering (in the sense of 1.2.3) from a
K-manifold onto a neighborhood U (s) of s which is ´ etale aboveU (s)∩S.
Then any temperate ´ etale covering S′→S extends to a (possibly ramiﬁed)
coveringS
′
→S, in the sense of 1.2.3: any point x has an open neighborhood
U (x) such that S′×SU (x) is a disjoint union of ﬁnite (ramiﬁed) coverings
Vj of U (x). Moreover, one may assume that the Vj are normal; such an
extension S
′
→S is then unique.
Furthermore, if Z has codimension≥ 2 and S is smooth, any temperate
´ etale coveringS′→S extends to a unique temperate covering S
′
→S.
Proof. We start with the statement about unicity. Since it is local o nS, it
is enough to establish it in the case of ﬁnite coverings (by de ﬁnition 1.2.3).
LetS
′
andS
′′
be two connected ﬁnite coverings of S which coincide over S.
The diagonal ∆ is a connected component of S′×SS′′. Its closure ∆ in the
normalization of S
′
×S S
′′
is again a connected component (using [ Ber99,
3.3.16]). The projections ∆ →S
′
, ∆ →S
′′
are ﬁnite, and their restrictions
to ∆ are isomorphisms; hence they are themselves isomorphis ms if S
′
and
S
′′
are normal.
Let us turn to the existence of the extension (with the normal ity prop-
erty). By unicity, this is a local question; we may and shall a ssume that Z is
a hypersurface, and that S is (strictly) aﬃnoid, and that there exists a ﬁnite
coveringT→S by a rigid-analytically smooth aﬃnoid T , which restricts to
a ﬁnite ´ etale covering T→S.
Let us ﬁrst show that any quotient of a temperate covering S′→S which
has the extension property inherits this extension propert y: by unicity, the
question is again local on S; by deﬁnition of coverings, this reduces the
question to the case when S′→S is ﬁnite. By glueing ( cf. [Ber93, 1.3.3]),
it is again enough to treat the aﬃnoid (normal) case. The argu ment is
similar to the above one for unicity and left to the reader.
132 III. p-ADIC ORBIFOLDS AND MONODROMY.
This remark allows us to assume that S′→S is a topological covering of
a ﬁnite ´ etale covering of S. Let us ﬁrst treat the case of a ﬁnite ´ etale cover-
ing. In this case, the extension property is proved in Gabber -L¨ utkebohmert
[L¨ ut93].
The crucial case is the case of a punctured disk S = D∗ which is worth
stating separately:
Lemma 2.1.12 (Gabber, L¨ utkebohmert). Any ﬁnite ´ etale covering of D∗
becomes a ﬁnite disjoint union of Kummer coverings on a small er concentric
punctured disk.
(Here the assumption that K is of characteristic zero is essential). From
there, one draws the extension property, in the product case , when
S is a
polydisk and Z a union of axes ( cf. loc. cit. , 3.3). By Kiehl’s theorem on the
existence of tubular neighborhoods [ Kie67b], the statement also holds if Z
is a strict normal crossing divisor in S. In the general case, one can invoke
embedded resolution for Z, cf. [Sch99] (note that [ L¨ ut93,§4] proposes an
alternative strategy which uses embedded resolution only i n dimension 2).
It remains to deal at last with the case of a topological cover ingS′→S.
In order to avoid problems of singularities, we consider a ﬁn ite etale covering
T→S as above,T being a rigid-analytically smooth aﬃnoid. It will be more
convenient to replace S′ byS′×ST (of which S′ is a quotient) so that the
new S′ is a topological covering of T itself a ﬁnite ´ etale covering of S. By
1.1.4, S′ extends to a topological covering S
′
→ T , and composition with
T→S provides the desired extension of S′/S to a covering S
′
/S.
The last statement of the theorem follows from the Nagata-Za riski pu-
rity theorem (which becomes easy in the case of a ﬁnite morphi sm of one-
dimensional aﬃnoids).
Remark. This extension property of temperate coverings does not hol d for
arbitrary ´ etale coverings.
Indeed, one can show that the logarithmic covering of the aﬃn e line does
not extend to a (ramiﬁed) covering of the projective line.
The previous theorem is completed by the following result, w hich is
proven as in the complex case [ SGA 1 , exp. XII, 5.3]:
Proposition 2.1.13. Let
S be a normal analytic space, and let Z be a
closed analytic subset such that S :=S\Z is dense in S. Then the functor
which attaches to any ﬁnite normal covering of S its restriction to S is fully
faithful.
It follows that in 2.1.11, the extension of coverings from te mperate cov-
erings of S to ‘normal’ coverings of S ‘is’ a fully faithful functor.
