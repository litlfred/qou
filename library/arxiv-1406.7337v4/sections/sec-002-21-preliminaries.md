---
doc_id: arxiv-1406.7337v4
doc_title: "Semi-Adequate Closed Braids and Volume Adam Giambrone Alma College giambroneaj@alma.edu"
section_id: sec-002-21-preliminaries
section_title: "Preliminaries"
section_number: 2.1
pages: 2-3
source_pdf: 1406.7337v4 (1).pdf
source_sha256: 5bae8237742733b9
doc_brief: "Semi-Adequate Closed Braids and Volume Adam Giambrone Alma College giambroneaj@alma.edu — In this paper, we show that the volumes for a family of A-adequate closed braids can be bounded above and"
---
Let D(K)⊆ S2 denote a diagram of a link K⊆ S3. To smooth a crossing of the link diagram D(K), we
may either A-resolve or B-resolve this crossing according to Figure 1. By A-resolving each crossing of D(K)
we form the all-A state ofD(K), which is denoted by HA and consists of a disjoint collection of all-A circles
and a disjoint collection of dotted line segments, called A-segments, that are used record the locations of
crossing resolutions. We will adopt the convention throughout this paper that any unlabeled segments are
assumed to be A-segments. We call a link diagram D(K) A-adequate ifHA does not contain any A-segments
that join an all-A circle to itself, and we call a link K A-adequate if it has a diagram that is A-adequate.
2
D(K) HA GA G′
A
Figure 2: A link diagram D(K), its all-A resolution HA, its all-A graph GA, and its reduced all-A graph G′
A.
long resolution short resolution
A A
Figure 3: The long and short resolutions of a twist region of D(K).
While we will focus exclusively on A-adequate links, our results can easily be extended to semi-adequate
links by reﬂecting the link diagram D(K) and obtaining the corresponding results for B-adequate links.
From HA we may form the all-A graph , denoted GA, by contracting the all-A circles to vertices and
reinterpreting the A-segments as edges. From this graph we can form the reduced all-A graph, denoted G′
A,
by replacing parallel edges with a single edge. For an example of a diagram D(K), its all-A resolution HA,
its all-A graph GA, and its reduced all-A graph G′
A, see Figure 2. Let v(G) and e(G) denote the number
of vertices and edges, respectively, in a graph G. Let −χ(G) = e(G)−v(G) denote the negative Euler
characteristic of G.
Deﬁnition 2.1. Deﬁne a twist region of D(K) to be a longest possible string of bigons in the projection
graph of D(K). Denote the number of twist regions in D(K) by t(D) and call t(D) the twist number of
D(K). Note that it is possible for a twist region to consist of a single crossing of D(K). If a given twist
region contains two or more crossings, then the A-resolution of a left-handed twist region will be called a
long resolution and the A-resolution of a right-handed twist region will be called a short resolution. See
Figure 3 for depictions of these resolutions. We will call a twist region long if its A-resolution is long and
short if its A-resolution is short.
Deﬁnition 2.2. A link diagram D(K) satisﬁes the two-edge loop condition (TELC) if, whenever two all-A
circles share a pair of A-segments, these segments correspond to crossings from the same short twist region
of D(K). (See the right side of Figure 3.)
Recall that v8 = 3.6638... denotes the volume of a regular ideal octahedron and v3 = 1.0149... denotes
the volume of a regular ideal tetrahedron. By combining results from [6], [8], and [13], we get the following
key result.
Theorem 2.1 (Corollary 1.4 of [6], Theorem from Appendix of [13]) . Let D(K) be a connected, prime,
A-adequate link diagram that satisﬁes the TELC and contains t(D)≥ 2 twist regions. Then K is hyperbolic
and
−v8·χ(G′
A)≤ vol(S3\K)< 10v3· (t(D)− 1).
