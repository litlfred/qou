---
doc_id: arxiv-1608.02961v3
doc_title: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Tudor Dimofte"
section_id: sec-003-3-complex-chern-simons-theory-as-a-tqft
section_title: "Complex Chern-Simons theory as a TQFT?"
section_number: 3
pages: 10-12
source_pdf: 1608.02961v3.pdf
source_sha256: ef3805c23133b8f2
doc_brief: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Tudor Dimofte — We present an elementary review of some aspects of Chern-Simons theory with complex gauge group SL(N, C)."
---
Now, having seen very explicitly that complex Chern-Simons Hilbert spaces are inﬁnite-
dimensional (and exactly how they’re inﬁnite-dimensional), let us think a bit about the
properties of partition functions.
For a closed three-manifold M, it is expected that the complex Chern-Simons partition
function takes the form
Z[M]k,s =
∑
ﬂat α
1
|Stab(α)|Bα(q
1
2 )~Bα(˜q
1
2 ). (3.1)
The sum here is over ﬂat complex connections α on M, which are the critical points of the
Chern-Simons path integral; andBα, ~Bα are holomorphic and antiholomorphic contributions
to the path integral from quantum ﬂuctuations around the critical point, with q, ˜q deﬁned
by (2.13). The prefactor |Stab(α)| is the volume of the stabilizer of α, i.e. the volume of the
subgroup of the gauge group that preserves a particular ﬂat connection.
One certainly expects such a formula to be valid perturbatively, due to standard proper-
ties of path integrals in quantum ﬁeld theory. (The perturbative version of (3.1) formed the
basis for the physical explanation of the Volume Conjecture in [25].) It was argued in [28],
however, that the formula is actually valid non-perturbatively as well. Roughly, one should
think of (3.1) as expanding the integration cycle in the Chern-Simons path integral into a
sum of integration cycles Γ α deﬁned by gradient ﬂow oﬀ of each critical point with respect
to the Chern-Simons action. The Γ α can further be written as products 3 of cycles γα×~γα
in the space of (holomorphic)×(anti-holomorphic) connections, leading to the factorization
Bα(q
1
2 )~Bα(˜q
1
2 ). 4
For a three-manifold with boundary Σ, the same type of formula holds after properly ac-
counting for boundary conditions. In particular, the sum is over ﬂat connections with a ﬁxed
behavior at Σ, and each summand becomes a wavefunction inH[Σ]k,s. For example if Σ =T 2
3In general, there could be a nontrivial matrix nαβ connecting holomorphic and anti-holomorphic sectors.
However, when one considers unitary Chern-Simons theory with an integration contour Γ along which A is
honestly the conjugate of A, the matrix is just the identity.
4The 3d-3d correspondence relates holomorphic-antiholomorphic factorization in complex Chern-Simons
theory to a rather nontrivial statement about lens-space partition functions of 3d N = 2 theories T [M] [57].
10
is a torus, we would ﬁx A-cycle holonomy eigenvalues x, ¯x of a ﬂat connection as in Section
2, and the individual wavefunctions would have the factorized form Bα(x,q
1
2 )~Bα(¯x, ˜q
1
2 ).
What can we learn from (3.1)? In the best-case scenario, there is a ﬁnite number of ﬂat
connections on M, and all the ﬂat connections have ﬁnite-volume stabilizers. This would
lead to a ﬁnite, well-deﬁned (in principle) Z[M]k,s. In contrast:
• If a ﬂat connection α is isolated but its stabilizer has inﬁnite volume, its contribution
to (3.1) vanishes.
• If ﬂat connections come in a continuous family on which the Chern-Simons action is
constant, then the contribution to (3.1) can be inﬁnite.
Unfortunately, the best-case scenario never holds, and both of these potentially bad situations
can arise. We consider some examples.
If M is hyperbolic (meaning that it admits a hyperbolic metric), it is expected that
there are a ﬁnite number of SL(2, C) ﬂat connections on M. Intuitively, for hyperbolic M
the fundamental group π1(M) is suﬃciently complicated that the representations π1(M)→
SL(2, C) are isolated. 5 Then the partition function is ﬁnite. As we discuss in Section 4.2,
the partition function can actually be computed. However, there is always at least one ﬂat
connection αabel whose holonomies belong to the maximal torus GL(1, C)⊂SL(2, C). The
stabilizer of αabel contains constant GL(1, C)-valued gauge transformations; since GL(1, C)
has inﬁnite volume, αabel does not contribute at all to the partition function. This becomes
hugely problematic when trying to formulate complex Chern-Simons as a TQFT, as all ﬂat
connections must be accounted for during cutting and gluing [44].
There are some simple manifolds whose fundamental group π1(M) is abelian. For exam-
ple, if M is a lens space L(p,r )≃ S3/Zp, the fundamental group is Zp. In this case, every
single ﬂat connection has holonomy in the maximal torus of the gauge group, the volume of
the stabilizer is always inﬁnite, and Z[M] vanishes identically.
In the opposite extreme are manifolds M on which the ﬂat connections are not isolated.
In this case, we expect that Z[M] diverges. For example, consider M = Σ×S1. Then
Mﬂat(GC,M ) =Mﬂat(GC, Σ)×TC (where TC is the maximal torus of GC). The partition
function is
Z[M]k,s = TrH[M]k,s1 1 = dimH[M]k,s =∞. (3.2)
Both the zeroes and inﬁnities appearing here obstruct the deﬁnition of consistent cutting
and gluing rules needed to make Chern-Simons theory a TQFT. The zeroes and inﬁnities
have to be regularized. While no systematic approach to regularization has been formulated
so far, there are exist several promising and exciting proposals. Almost all of them are
motivated by string/M-theory and the 3d-3d correspondence.
5On hyperbolic M, one particular ﬂat SL(2, C) connection — the one corresponding to the global hyper-
bolic metric — is well known to be isolated [58, 59]. Computational experiments suggest that in fact all ﬂat
connections SL(2, C) are isolated, but there exists no general proof of this statement.
11
