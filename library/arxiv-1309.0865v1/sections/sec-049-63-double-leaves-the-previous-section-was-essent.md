---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-049-63-double-leaves-the-previous-section-was-essent
section_title: "Double leaves. The previous section was essentially a discussion of mapsBw →"
section_number: 6.3
pages: 62-64
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
Qw for somew. Let us use this to discuss maps Bw →By for arbitrary expressions w
andy.
Consider a light leaves map LLx,e : Bx →Bw wherew is a rex for w. Flipping this
diagram upside-down, we get a map LLx,e : Bw →Bx. By the results of the previous
section,LLw,e behaves nicely after localization, giving a nonzero map Qw →Qf only
when f ≤ e. The coefﬁcients appearing are not actually pe
f , because the polynomials
1
αs
should appear only in the projections maps from Bs,Q toQ orQs, not in the inclu-
sion maps. In the new formula for pe
e, U0 and U1 will not contribute, and D0 and D1
will contribute 1
αk
. We leave the reader to check the details. Regardless, the re sult is
still invertible in Q and the analogue of Corollary 6.8 holds.
Now let x and y be arbitrary sequences with subsequences e and f respectively ,
such that (x, e) and (y, f) both express w. Choose a rex w forw, and construct maps
LLw,e : Bw → Bw and LLy,f : Bw → By. We deﬁne the corresponding double leaves
map to be the composition
LLw,f ,e
def= LLy,f ◦LLx,e.
After localization, we obtain a coefﬁcient pf ,e
f ′,e′ given by the inclusion of each stan-
dard summand Qe′ of Bx and projection to each standard summand Qf ′ of y. We
know several facts about these coefﬁcients:
• pf ,e
f ′,e′ = 0 unless (x, e′) and (y, f ′) express the same element v.
• pf ,e
f ′,e′ = 0 unless both e′ ≤ e and f ′ ≤ f. In particular, this implies that the
commonly expressed element v must satisfy v ≤ w. We refer to this latter
phenomenon as Bruhat upper-triangularity , a special kind of path dominance
upper-triangularity .
• Whenv = w, e′ = e and f ′ = f, the coefﬁcient is nonzero and is a product of
roots, obeying a simple formula independent of the choice of LL maps.
SOERGEL CALCULUS 63
Proposition 6.9. Let LLw,y contain one map LLw,f ,e for each w ∈ W and each pair of
subsequences (x, e) and (y, f) expressingw. Then after localization, LLw,y forms a basis of
mapsBw →By. In particular, the set LLw,y is linearly independent.
Proof. After localization, the space of maps Bw →By is a direct sum of Hom(Qe,Q f )
for each pair of subsequences. These terms have a partial ord er, and the LL maps
satisfy upper-triangularity with respect to this partial o rder, with an invertible diag-
onal. □
Remark 6.10. In the deﬁnition of the double leaves basis we could have take n LL
maps and rotated them 180 degrees, instead of ﬂipping them. T his would avoid
some of the annoyances of the ﬁnal chapter, but would introdu ce its own annoy-
ances. Most notably , rotation takes a mapBw →By and returns a mapBω(y) →Bω(w),
whereω denotes reversing the order of a sequence. To deﬁne LL using a rotated map,
the target of the original map must be Bω(w), which is actually a rex for w−1, and this
requires additional bookkeeping. Rotation will be more obv iously useful in the ﬁnal
chapter. Note that both approaches are equally valid, altho ugh coming up with a
change of basis matrix between them would be a combinatorial nightmare. Also,
ﬂipping a diagram vertically is more natural in terms of the c ellular structure.
Let us now state some of our main results, which all assume Dem azure Surjectiv-
ity:
Theorem 6.11. The set LLx,y forms a free R-basis for Hom(Bx,B y) in D.
Proposition 6.12. The setLLx,e forms a free R-basis for Hom(Bx, /BD ) in D.
Corollary 6.13. Hom spaces in D are free gradedR-modules.
Remark 6.14. Proposition 6.12 is a special case of Theorem 6.11, because w heny = ∅
we must have w =e, andLLy is the empty diagram.
The ﬁnal chapter of this paper contains an elementary diagra mmatic (though un-
pleasant) proof of these results. Of course it is enough to sh ow that LL spans, as we
have already shown that this set is linearly independent ove rR. The reader is now
equipped to read that chapter, which does not use anything be yond this section.
We assume these three results for the rest of this chapter.
Because Theorem 6.11 did not depend on the particular LL maps chosen, this im-
plies that two different choices of LL are pairwise dependent. It does not imply
that two different choices of LLx,w are pairwise dependent, because the dependence
relations may require lower terms.
Example 6.15. Lets,t be the indices in type A2. There are two choices for the map
LLsts,111, as below. The difference between them is not an LL map, but it is an LL
map.
64 BEN ELIAS AND GEORDIE WILLIAMSON
1 0 0
− =
1 1 1 1 1 1
0 01
