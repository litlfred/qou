---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-000-1-preface
section_title: "Preface"
section_number: 1
pages: 3-5
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
19 Negentropy 67
20 Uncomplexity 68
20.1 The Auxiliary System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
20.2 Combining Auxiliary Systems . . . . . . . . . . . . . . . . . . . . . . . . . 69
21 Uncomplexity as a Resource 71
22 The Power of One Clean Qubit 72
22.1 The Protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
22.2 Expending Uncomplexity and Negentropy . . . . . . . . . . . . . . . . . . 74
23 Spacetime and Uncomplexity 75
23.1 CA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
2
23.2 Geometric Interpretation of Uncomplexity . . . . . . . . . . . . . . . . . . 76
IV Conclusion 79
Part I
Lecture I: Hilbert Space is Huge
1 Preface
These lectures are a tale of two metrics on the same space—the space of states of a quantum
system ofK qubits. One metric is familiar to you and the other probably very unfamiliar.
They are extremely diﬀerent measures of the distance between quantum states and they
have diﬀerent purposes.
The two metrics are totally dissimilar. One, the inner product metric, is small in the
sense that no two points are more distant thatπ/2. The other, relative complexity, is huge;
almost all points are separated by a distance exponential inK. The inner product metric is
positively curved like a sphere. The geometry of relative complexity is negatively curved,
with the radius of curvature being much smaller than the maximum distance between
points (the diameter of the space). Both are compact and homogeneous.
Although they both represent the distance between quantum states they are in a sense
incommensurate: The distance between two points can be very small in one metric and
exponentially large in the other. They represent very diﬀerent relations between states.
Relative complexity should be of interest in quantum-computer science but has not
been of much use in the study of ordinary quantum systems, not even black holes if we
are interested in the region outside the horizon. It is only when we ask about the interior
of a black hole, the region behind the horizon, that relative complexity takes its place as
an essential quantity.
You might ask why put so much eﬀort into understanding what in practice can never be
seen, i.e., the black hole interior. The answer is two-fold: First Einstein’s general theory of
relativity predicts and describes the region behind the horizon and if we want to understand
quantum gravity we have to take account of this fact. We will not have understood how
the full geometry of GR emerges from quantum mechanics without following space into
the black hole interior.
3
The second point is that in a de Sitter cosmology like ours everyone is behind someone
else’s horizon. We won’t understand anything without understanding horizons.
These three lectures cover a certain aspect of complexity and black holes that I ﬁnd
most interesting, namely the relation to the second law of thermodynamics. Quantum com-
plexity is not entropy, but there are deﬁnite parallels between the two. In fact complexity
is the entropy of an “auxiliary” classical system (called A) which has an exponentially
large number of degrees of freedom. The system A actually represents the motion of the
state vector in Hilbert space. If the number of qubits describing the quantum system is K
then the number of classical degrees of freedom describing A is 4K. The auxiliary system
is chaotic has its own statistical thermodynamics, including a “second law of complex-
ity.” This second law plays the central role in the emergence of the spacetime behind the
horizon, and is the main subject of these lectures.
Because of the limitations of time I have had to sacriﬁce two important subjects which
I would like to have covered. The action of a Wheeler DeWitt patch is probably our best
bet for a precise geometric quantity to relate to complexity. I describe it very brieﬂy in
Lecture III. On the pure quantum side our best bet for a deﬁnition of complexity may come
from Nielsen’s approach, in which the geometry of Hilbert space is modiﬁed to a right-
invariant Riemannian metric space. I mention the Nielsen approach in the conclusion but
only brieﬂy. Had I more time, these are the two things I would have included.
