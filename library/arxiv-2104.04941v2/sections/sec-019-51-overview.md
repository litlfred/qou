---
doc_id: arxiv-2104.04941v2
doc_title: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES"
section_id: sec-019-51-overview
section_title: "Overview"
section_number: 5.1
pages: 23-24
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
doc_brief: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES — Fock and Goncharov [FG06b] introduced cluster ensembles, p roviding a framework for coordi- nates on varieties of surface"
---
The quiver Q will be divided into an interior and three edges. Coordinate s at each vertex will be assigned
generalized minors of elements in the canonical form (h1,h 2,h 3,u ) of an element of Conf ∗
3. Each edge should
contain information for some hi, and the interior should contain information for u.
One minor for each simple root determines an element of H; the coordinates on an edge will be of the
form ∆ ωj (hi). Accordingly, the edges of the triangle will be quivers of Dy nkin type. The interior vertices
will be given by generalized minors of the form ∆ wkωik (u). Laying these out to satisfy [FZ99, Theorem 1.17]
follows the algorithm of [BFZ05, Section 2]. This, together with our choice of presentation for w0, means
the interior will be a rectangular grid of vertices. Recall t hat these take the names A•, B•, C•, and vi,j by
Deﬁnition 4.13.
The algorithm of Fomin–Zelevinsky describes a rectangle. T wo of the rectangle’s edges will be edges in
the triangle. We call this Q0. The chief diﬃculty of constructing Q is introducing the third edge to Q0. To
do this, we look ahead to µrot. Since that quiver mutation must rotate Q, and Q and Q0 share a mutable
23
portion, we can rotate Q0. And since Q0 already has two of Q’s three edges, the third edge of Q can be
deduced from the action of µrot on Q0.
The ﬂip mutation µﬂip is built in the same way that µrot is: repeated application of [FZ99, Theorem 1.17].
We need a bit of compensation before and after because the ama lgamation does not quite line up the quivers
as necessary.
Remark 5.1. Our construction will produce µrot andµﬂip as compositions of smaller mutations. They contain
smaller mutations (µrotTw and µﬂipTw ) which may be more useful for certain applications. See Sect ion 5.7.
Finally, the map M is the generalized minors, as described above, together wit h a monomial compensation.
At each step of µrot and µﬂip , [FZ99, Theorem 1.17] takes the form described in Section 3. 2
(initial) · (ﬁnal ) = ( left) · (right) +
∏
j⁄=ik
(in same column ).
However, at the edges of Q, when j is very low or very high, the left or right elements might be tr ivially 1
according to the theorem. In our quivers, however, these ele ments are non-trivial, given by frozen vertices.
Therefore, we have to balance the equation of the theorem. To do so, we treat the edge coordinates in
the mutation relation as “Extra” information, and include t his extra information in our deﬁnition of interior
coordinates. Then the quiver mutations take forms similar t o the following:
Extra · (initial) · (ﬁnal ) =
left/bracehtipdownleft/bracehtipupright/bracehtipupleft/bracehtipdownright
(Extra · 1) ·(right) + Extra ·
∏
j⁄=ik
(in same column ).
Since the extraneous factors appear in every term, the desir ed result still holds by the theorem. This is the
eﬀect of the monomial map m in M.
Example 5.2. Based on the Dynkin diagram for F4, the following is a well-rooted tree-like
Dynkin quiver (following Deﬁnition 4.11) for F4:
1 2 3 4
Remark 5.3. By Deﬁnition 4.8, the nodes with higher weight in the quiver c orrespond to the nodes which
are “smaller” in the Dynkin diagram.
With this, we are ready to begin the construction. Let D be a well-rooted tree-like quiver of Dykin type
forG. Let c = {c1,c 2,...,c n } be the induced Coxeter element as in Deﬁnition 4.9, and let w0 be the longest
word, with presentation via Fact 2.10.
Remark 5.4. We will abuse notation slightly by writing si1si2 · · ·sin as {i1,i 2,...,i n }.
