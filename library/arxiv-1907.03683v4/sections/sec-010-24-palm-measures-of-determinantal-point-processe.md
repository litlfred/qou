---
doc_id: arxiv-1907.03683v4
doc_title: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND"
section_id: sec-010-24-palm-measures-of-determinantal-point-processe
section_title: "Palm measures of determinantal point processes. We here give a probabilistic"
section_number: 2.4
pages: 10-11
source_pdf: 1907.03683v4.pdf
source_sha256: eb8cc2ddfc8c0739
doc_brief: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND — Christoﬀel deformation of a measure on the real line consists of multipying this measure by a squared polynomial having its roots in R."
---
interpretation of Christoﬀel deformations of orthogonal polynomial ensembles in the case
when the points u1, ..., uk belong to the support of the measure ω. We ﬁrst recall the basics
on Palm distributions of a general point process P on a discrete space E, see for instance
[21], [32] or [15] and references therein for a more general treatment.
Deﬁnition 2.5. Let P be a point process on the discrete set E. For pairwise distinct points
u1, ..., uk ∈E such that P(u1, ..., uk ∈X) > 0, the Palm measure ˆPu1,...,uk of P at u1, ..., uk is
the point process P on E conditionned to have particles at u1, ..., uk,
ˆPu1,...,uk(B) = P(B ∩{u1, ..., uk ∈X})
P(u1, ..., uk ∈X)
,
for any borel set B ⊂Conf(E). The reduced Palm measure Pu1,...,uk is then deﬁned as the
pushforward of the Palm measure ˆPu1,...,uk under the map
Conf(E) →Conf(E)
X 7→X \ {u1, ..., uk}.
In particular, if the point process P has N + k particles, i.e. P(|X| = N + k) = 1, then its
reduced Palm measure Pu1,...,uk has N particles.
We also recall the following Proposition from [32].
Proposition 2.6. If P is a determinantal point process with kernel K such that P(u1, ..., uk ∈
X) > 0, then, its reduced Palm measure at u1, ..., uk is a determinantal point process with
kernel
Ku1,...,uk(x, y) = (det(K(ui, uj))−1
1≤i,j≤k det




K(x, y)
K(x, u1)
. . .
K(x, uk)
K(u1, y)
K(u1, u1)
. . .
K(u1, uk)
...
...
...
K(uk, y)
. . .
. . .
K(uk, uk)



.
acting on l2(E).
We now consider a measure ω as before, with an inﬁnite support lying in a discrete count-
able subset E of R. For n ∈N, we denote by Pn the corresponding orthogonal polynomial
ensemble. Let u1, ..., uk ∈supp(ω) be pairwise distinct, and, as before, denote by Pk
n the
Christoﬀel deformation of Pn at u1, ..., uk. The next Proposition formally establishes the fact
that the study of Christoﬀel deformations of orthogonal polynomial ensembles contains the
study of their Palm measures.
Proposition 2.7. For any natural N ∈N, we have the equality between point processes
Pu1,...,uk
N+k
= Pk
N.
Proof. We know from [32] (see also [15]) that, for a determinantal point process with a
kernel that is a kernel of an orthogonal projection onto a closed subspace L ⊂l2(E), its
10
reduced Palm measure at points u1, ..., uk is a determinantal point process with the kernel
of orthogonal projection onto
Lk := {f ∈L, f(u1) = ... = f(uk) = 0}.
Specializing this fact to the subspace
L := {
p
ω(x)p(x), p ∈RN+k−1[x]},
one obtains the statement of the Proposition.
□
