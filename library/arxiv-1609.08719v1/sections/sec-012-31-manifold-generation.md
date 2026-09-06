---
doc_id: arxiv-1609.08719v1
doc_title: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE"
section_id: sec-012-31-manifold-generation
section_title: "Manifold generation"
section_number: 3.1
pages: 10-11
source_pdf: 1609.08719v1.pdf
source_sha256: f61ff2111e9a97f9
doc_brief: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE — We use a large census of hyperbolic 3-manifolds to experimentally investigate a conjecture of Neumann regarding the Bloch Group."
---
can be found at https://github.com/s-gilles/maps-reu-code . We consid-
ered all orientable, cusped, hyperbolic manifolds which can be triangulated us-
ing 9 tetrahedra or less (the OrientableCuspedCensus within SnapPy at the time
of work), as well as all link complements using 3 crossings or more (a subset of
INVESTIGATION OF NEUMANN’S CONJECTURE 11
LinkExteriors). We also considered additional manifolds in the LinkExteriors
and HTLinkExteriors collections.
Of these manifolds, we performed Dehn surgery of type ( p,q ) over each of the
n cusps, with p∈ [0,L (n)] and q∈ [−L(n),L (n)], (and (p,q ) = 1) where L(n) is
given by ﬁgure 8.
L(n) 16 12 8 6 4 3 3 2
n 1 2 3 4 5 6 7 ≥ 8
Figure 8. L(n)
Of the resulting manifolds, we discarded those whose invariant trace ﬁeld re-
sulted in a polynomial with degree 9 or more (or if SnapPy or Snap were unable
to triangulate the result). For each remaining manifold, we we stored intermediate
information about the manifold. The resulting ﬁle, available athttp://www.curve.
unhyperbolic.org/linComb/finalized_data/volumes/all_volumes.csv, contains
over 790,000 manifolds, representing over 6,300 distinct invariant trace ﬁelds, with
volumes accurate to at least 50 decimal places. The work was performed on the
University of Maryland’s computation cluster.
3.2. Lattice matching. With the data stored inall volumes.csv, we have enough
data to conjecture partial lattice generators for 5,900 invariant trace ﬁelds. Of those,
for 312 invariant trace ﬁelds we have enough data to conjecture not only generating
volumes for the full lattice, but also representative manifolds associated to the in-
variant trace ﬁeld which exhibit those volumes. This data can be found at http://
www.curve.unhyperbolic.org/linComb/finalized_data/volume_spans.csv, and
the code we used for conjecturing lattice generators is available athttps://github.
com/s-gilles/maps-reu-code , an implementation of algorithm 1.
Sample data can be found in section 6.
