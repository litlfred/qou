---
doc_id: arxiv-math-0005038v1
doc_title: "BRAID GROUPS ARE LINEAR STEPHEN J. BIGELOW"
section_id: sec-004-13-notation-if-α-and-β-are-arcs-in-d-p-such-αs-β
section_title: "Notation. If α and β are arcs in D \ P such α(s) ⁄= β(s) for all s ∈ I then"
section_number: 1.3
pages: 2-4
source_pdf: 0005038v1.pdf
source_sha256: db0b9b7a8534f161
doc_brief: "BRAID GROUPS ARE LINEAR STEPHEN J. BIGELOW — The braid groups Bn can be deﬁned as the mapping class group of the n-punctured disc."
---
we deﬁne {α, β} to be the arc in C given by
{α, β}(s) = {α(s), β(s)}.
If y is a point in D \ P and α is an arc in D \ (P ∪ {y}) then we deﬁne {α, y} to be
the arc in C given by
{α, y}(s) = {α(s), y}.
The same arc can be denoted by {y, α}.
If x and y are elements of a group then we use the notation
xy = y−1xy
BRAID GROUPS ARE LINEAR 3
T (F )
F
T (F ′)
F ′
d1 d2
Figure 1. A fork F and a parallel copy F ′.
and
[x, y] = x−1y−1xy.
Throughout this paper, I will denote the interval [0 , 1]. Braids compose from right
to left. Arcs compose from left to right.
2. Forks and Noodles
In this section we deﬁne forks and noodles and a pairing between the m. The
idea of using a fork to represent an element of H2( ˜C) is due to Krammer [Kra].
A fork is an embedded tree F ⊂ D with four vertices d1, pi, pj and z such that
F ∩ ∂D = {d1}, F ∩ P = {pi, pj}, and all three edges have z as a vertex. The edge
containing d1 is called the handle of F . The union of the other two edges is a single
edge, which we call the tine edge of F and denote by T (F ).
For a given fork F we can deﬁne a parallel copy of F to be an embedded tree F ′
as shown in Figure 1. The ﬁve punctures at the top of the ﬁgure may be replaced by
any number, and any orientation-preserving self-homeomorphism may be applied
to the entire ﬁgure. The tine edge T (F ′) of F ′ is deﬁned analogously to that of F .
For any fork F , we deﬁne a surface ˜Σ( F ) in ˜C as follows. Let F ′ be a parallel
copy of F . Let z be the vertex contained in all three edges of F , and let z′ be the
vertex contained in all three edges of F ′. We deﬁne the surface Σ( F ) to be the set
of points in C which can be written in the form {x, y}, where x ∈ T (F ) \ P and
y ∈ T (F ′) \ P . Let β1 be an arc from d1 to z along the handle of F and let β2 be
an arc from d2 to z′ along the handle of F ′. Let ˜β be the lift of {β1, β2} to ˜C which
starts at ˜c0. Let ˜Σ( F ) be the lift of Σ( F ) to ˜C which contains ˜β(1).
A noodle is an embedded edge N ⊂ D \ P with endpoints d1 and d2. For a given
noodle N we deﬁne the surface Σ( N ) to be the set of points {x, y} ∈ C such that x
and y are distinct points in N . Let ˜Σ( N ) be the lift of Σ( N ) to ˜C which contains
˜c0.
Let F be a fork and let N be a noodle. We deﬁne ⟨N, F ⟩ ∈ Λ as follows.
⟨N, F ⟩ =
∑
a,b ∈Z
qatb(qatb ˜Σ( N ), ˜Σ( F )).
Here qatb ˜Σ( N ) denotes the image of ˜Σ( N ) under the covering transformation qatb,
and (qatb ˜Σ( N ), ˜Σ( F )) denotes the algebraic intersection number of the two surfaces
in ˜C.
