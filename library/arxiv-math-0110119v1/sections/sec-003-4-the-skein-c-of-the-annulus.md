---
doc_id: arxiv-math-0110119v1
doc_title: "Idempotents of the Hecke algebra become Schur functions in the skein of the annulus"
section_id: sec-003-4-the-skein-c-of-the-annulus
section_title: "The skein C of the annulus"
section_number: 4
pages: 4-6
source_pdf: 0110119v1.pdf
source_sha256: 4904a86e8a340f59
toc_source: inferred
doc_brief: "Idempotents of the Hecke algebra become Schur functions in the skein of the annulus — The Hecke algebra Hn contains well known idempotents Eλ which are indexed by Young diagrams with n cells."
---
The skein C of the annulus
The skein of the annulus shall be denoted by C. Let D1 and D2 be two diagrams in
the annulus S1×[0, 1]. We can bring D1 into S1×[0, 1/2), and D2 into S1×(1/2, 1]
by regular isotopies. Then the product of D1 and D2 is deﬁned as the diagram
D1 ∪D2. An example is shown in ﬁgure 2. The product is commutative since
D1D2 and D2D1 diﬀer by regular isotopy. The empty diagram is the identity.
4
Γ
−→
Figure 4:
Encircling a diagram in the annulus.
Figure 3 depicts an annulus with a set of n oriented arcs.
A rectangle is
removed from the annulus so that we can insert a diagram from Rn
n with matching
orientations of the arcs. This factors to a map ∆n : Rn
n →C. This is a special case
of a wiring. We abbreviate ∆n by ∆if the index n is obvious from the context.
We denote by Cn the image of Rn
n under the closure map which is a submodule
of C. By C+ we denote the submodule of C spanned by all C0, C1, . . ..
We deﬁne Qλ to be the closure of the idempotent Eλ of Rn
n where n is the
number of cells of λ,
Qλ = ∆n(Eλ) ∈C.
By looking at the limit s →1 it is straightforward to verify that the Homﬂy
polynomial of Qλ as an element of the plane is non-zero and therefore Qλ is
non-zero in C (see [7]).
We deﬁne a linear map Γ from C+ to C+ that is the encircling of a diagram in
the annulus by a single loop with a speciﬁed orientation as shown in ﬁgure 4.
In Rn
n, one can write the identity braid on n strings with an encircling loop as
the linear combination of so-called Jucys-Murphy operators as explained in [10].
The skein calculations in [2] then immediately imply the following lemma.
Lemma 4.1 For any Young diagram λ we have Γ(Qλ) = cλQλ in C+ with the
scalar
cλ = v−1 −v
s −s−1 + vs−1
l(λ)
X
k=1
(s2(k−λk) −s2k).
Remark It is easy to conﬁrm that the eigenvalues cλ are pairwise diﬀerent for
all Young diagrams λ.
Lemma 4.2 The set {Qλ | λ has n cells } is a basis for Cn for any n ≥0.
5
Proof We deﬁne X+
i ∈Ci as the closure of the braid σi−1σi−2 · · · σ1 ∈Ri
i. The
weighted degree of a monomial (X+
i1)j1 · · · (X+
ik)jk is deﬁned as i1j1 + · · · + ikjk.
Any diagram in the annulus can be written inductively via the skein relations
as a linear combination of totally descending curves.
This means that Cn is
spanned linearly by the monomials in the X+
i of weighted degree n. Hence, the
dimension of Cn is at most π(n), by which we denote the number of partitions of
n.
On the other hand, Qλ lies in Cn provided that the Young diagram λ has n
cells. These elements are non-zero and they are linearly independent since they
have pairwise diﬀerent eigenvalues under the map Γ by lemma 4.1. By deﬁnition,
there are π(n) Young diagrams with n cells. Since the dimension of Cn is at most
π(n) by the above argument, the dimension of Cn is exactly π(n) and the set of
Qλ where λ has n cells is a basis.
⋄
Remark Lemma 4.2 implies that the elements X+
i , i ≥0, generate C+ freely as
a commutative algebra. This is a special case of Turaev’s result [11] that C is
generated freely as a commutative algebra by X+
i , X−
i for i ≥0 where X−
i derives
from X+
i by reversing the orientation.
