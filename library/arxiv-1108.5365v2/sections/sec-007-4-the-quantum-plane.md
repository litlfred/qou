---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum"
section_id: sec-007-4-the-quantum-plane
section_title: "The quantum plane"
section_number: 4
pages: 22-23
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual ˆA as a von Neumann algebra."
---
In this section, we will deﬁne the main object of study in this paper, t he C∗-
algebraA of “functions vanishing at inﬁnity” on the quantum plane. Its Haar
functional is established, and we obtain the GNS construction of A on a Hilbert
spaceH≃ L2(R× R). Finally we construct the multiplicative unitary W , and show
that it is in fact manageable.
Note that in analogy to the classical semi-group with inverses absen t, in our
context we don’t have a well-deﬁned antipode S due to positivity. Hence we may
also call the object informally as a “quantum semigroup”. However, as we see in
Deﬁnition 4.6, there is instead a well-deﬁned unitary antipode R.
With the existence of the coproduct (Corollary 4.5), a left invariant faithful
KMS Haar functional (Theorem 4.7, Theorem 4.9, Corollary 4.15), a r ight invariant
Haar functional (Proposition 4.16) and the density condition (Theo rem 5.8), the
C∗-algebraA can be put in the context of “locally compact quantum group” in the
sense of [24, 25]. This allows us to apply the theory developed in those papers.
22
4.1 Motivations from classical ax + b group
Recall that the classical ax +b group is the group G of aﬃne transformations on
the real line R, where a> 0 and b∈ R, and they can be represented by a matrix of
the form (we use the transposed version):
g(a,b ) =
( a 0
b 1
)
, (4.1)
where the multiplication is given by
g(a1,b 1)g(a2,b 2) =
( a1a2 0
b1a2 +b2 1
)
. (4.2)
We can then talk about the space C∞(G) of functions on G vanishing at inﬁnity,
and a dense subspace of functions WG of the form
WG ={g(loga)f (b) : f,g ∈W⊂ L2(R)}, (4.3)
wheref,g ∈W are the rapidly decaying functions deﬁned in Deﬁnition 2.23. Then
C∞(G) is the sup-norm closure of WG.
In the study of quantum plane, it is necessary to consider the semig roup G+
of positive elements. Restricting f (a,b )∈W G to b > 0, we can use the Mellin
transform and express the functions as
f (a,b ) =
∫
R+i0
∫
R
F (s,t )aisbitdsdt. (4.4)
Since the function is continuous at b = 0, it has at most O(1) growth as b−→ 0+.
Hence from Theorem 2.2, we conclude that F (s,t ) is entire analytic with respect
to s, and holomorphic on Im( t)> 0. Furthermore, it has rapid decay in s,t along
the real direction, and can be analytically continued to Im( t) ≤ 0. Moreover,
since f (a,b ) is analytic at b = 0, the analytic structure of f (a,b ) on b is given
by∑ ∞
k=0Akbk for some constants Ak. Hence F (s,t ) has possible simple poles at
t =−in,n = 0, 1, 2,... .
Finally according to the Parseval’s Formula for Mellin transform, ther e is an L2
norm on functions of G+ given by
‖f (a,b )‖2 =
∫
R
∫
R
|F (s,t + 1
2i)|2dtds (4.5)
induced from the Haar measure da
a db. However, it is no longer left invariant due to
the lack of inverses.
