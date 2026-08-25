---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-020-73-face-degenerate-edge-sets
section_title: "Face-degenerate edge sets"
section_number: 7.3
pages: 18-19
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety forSL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
Deﬁnition 7.12.LetT′ be a triangulation whose edge set contains that ofT . Adescendant of
E∈ T(T ) is an elementE′∈ T(T′) such thatE′ agrees withE on the edges ofT . IfE′∈ T(T′)
is a descendent ofE∈ T(T ) we writeE′
|T =E.
Lemma 7.13.LetE∈ T(T ) be face-degenerate and suppose that there arek degenerate faces.
IfT′ is the triangulation obtained fromT by performing a 2-3 move at each degenerate face
then E has 2k descendants each of which is edge-degenerate.
Proof. Performing a 2-3 move adds an edge which can be either zero or nonzero without violating
transitivity. In either case, none of the new faces are degenerate (see Figure 13). This concludes
the proof. □
TRIANGULATION INDEPENDENT PTOLEMY V ARIETIES 19
0 0
0
⁄= 0
⁄= 0
⁄= 0
⁄= 0⁄= 0
⁄= 0
0 0
0
0
0
⁄= 0
⁄= 0⁄= 0
0
Figure 13. A 2-3 move, face-
degenerate edge set.
Figure 14. A 2-3 move,
simplex-degenerate edge set.
Deﬁnition 7.14.Let E∈ T(T ) be face-degenerate and letT′ be the triangulation obtained
fromT by performing 2-3 moves between all degenerate faces. Deﬁne
(7.7) P (T,E ) =
⋃
E′
|T =E
P (T′,E′),
where the (clearly disjoint) union is taken insideA(V (M)) or the ﬁnite-dimensionalA(W ) where
W is the union of allV (T′). We deﬁnePσ(T,E ) andEP (T,E ) similiarly.
Theorem 7.15. The one-to-one correspondences(7.2), (7.3), and (7.4) still hold ifE is face-
degenerate.
Proof. IfT′ is a decoration with edge set containingT , the set of decorations of typeE∈ T(T )
is the disjoint union, over the descendantsE′ of E, of the sets of decorations of typeE′. The
result now follows from Theorem 7.4. □
