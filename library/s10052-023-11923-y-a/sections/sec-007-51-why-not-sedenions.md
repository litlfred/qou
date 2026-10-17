---
doc_id: s10052-023-11923-y-a
doc_title: "Three generations of colored fermions with S 3 family symmetry from Cayley–Dickson sedenions"
section_id: sec-007-51-why-not-sedenions
section_title: "Why not sedenions?"
section_number: 5.1
pages: 7-9
source_pdf: s10052-023-11923-y_a.pdf
source_sha256: 73d1a03532d62ef7
toc_source: outline
doc_brief: "Three generations of colored fermions with S 3 family symmetry from Cayley-Dickson sedenions — An algebraic representation of three generations of fermions with SU(3)C color symmetry based on the"
duplicate_of: "arxiv-2306.13098v2"
---
Since one generation of electrocolor states are efﬁciently rep-
resented starting from C ⊗O, one might ask if S (or rather
C ⊗S) is an appropriate larger algebraic structure capable
of describing three generations. Not being a division algebra
is not grounds to disqualify S, for we point out that neither
123
747
Page 8 of 13
Eur. Phys. J. C (2023) 83 :747
C⊗O nor Cℓ(6) generated as the left multiplication algebra
are themselves division algebras. Furthermore, the algebra
R ⊗C ⊗H ⊗O is, like S, not even alternative. In fact, the
construction of invariant subspaces (minimal ideals) relies
explicitly on the use of projectors (and nilpotents), which
altogether do not exist in division algebras.
There are several natural reasons to suspect that S exhibits
the algebraic structure necessary to describe three full gen-
erations:
1. Aut(S) = Aut(O) × S3, and one ﬁnds a threefold mul-
tiplicity of the symmetries associated with O,
2. The process in Sect. 4 shows how to naturally isolate thee
O subalgebras within S, which could perhaps be used to
construct three generations,
3. The group Spin(8) generated from Cℓ(8) admits a trial-
ity, which has on occasion been suggested as a potential
source of three generations [32,44]. The group of outer-
automorphisms of Spin(8) is precisely S3.
One approach to construct three generations with SU(3)C
symmetry is to use each of the three C ⊗Oi ⊂S to generate
(via its left action on itself, but not as a left action of C⊗S!) a
Cℓ(6) algebra, and subsequently representing three genera-
tions in terms of the minimal left ideals of these three Cℓ(6).
This approach was considered in [34], as a generalization
of the construction three generations of leptons from three
H ⊂O developed in [36].
There are several drawbacks to this approach however.
Each generation requires its own copy of SU(3) resulting in
three generations of gluons. Finally, the physical interpre-
tation of the S3 automorphisms remains obscured, because
these automorphisms stabilize the (non-principle) octonion
subalgebras in S.
Theapproachpursuedhereisdifferentandseekstoresolve
these shortcomings. We instead use each C⊗Oi ⊂S to con-
struct a pair or fermionic ladder operators that each generate
Cℓ(2), via their left multiplication action on all of C ⊗S
(instead of just C ⊗Oi). The three pairs of ladder operators
are independent of one another and hence we identify a single
copy of Cℓ(6) ∼= Cℓ(2) ˆ⊗Cℓ(2) ˆ⊗Cℓ(2), corresponding to a
subalgebra of Cℓ(8). Thus, we will employ all three Oi ⊂S
in order to construct a single generation of states. This corre-
sponds to a direct generalization of the construction reviewed
in Sect. 3 where three H subalgebras of O are used to con-
struct a single generation of color states. Subsequently, the
order three S3 automorphism of S will be used to generate
two additional generations. This construction will therefore
provide a clear interpretation of the new S3 automorphism ψ.
All three generations constructed in this manner transform
as required under a single copy of the gauge group SU(3)C,
thereby avoiding introducing three generations of gluons.
5.2 One generation of electrocolor states from C ⊗S
We proceed by ﬁrst constructing a single generation with
unbroken SU(3)C × U(1) symmetry from C ⊗S. Consider-
ing the three octonion subalgebras O1, O2, O3 of S deﬁned
above:
O1 : {e0, e1, e4, e5, e8, e9, e12, e13},
O2 : {e0, e2, e4, e6, e8, e10, e12, e14},
O3 : {e0, e3, e4, e7, e8, e11, e12, e15}.
For each Oi subalgebra, we deﬁne a single pair of raising
and lowering operators as follows:
A†
1 ≡
1
2
√
2
(e1 + ie5 + e9 + ie13),
(30)
A1 ≡
1
2
√
2
(−e1 + ie5 −e9 + ie13),
(31)
A†
2 ≡
1
2
√
2
(e2 + ie6 + e10 + ie14),
(32)
A2 ≡
1
2
√
2
(−e2 + ie6 −e10 + ie14),
(33)
A†
3 ≡
1
2
√
2
(e3 + ie7 + e11 + ie15),
(34)
A3 ≡
1
2
√
2
(−e3 + ie7 −e11 + ie15).
(35)
It is readily checked that Ai(Aiw) = A†
i (A†
i w) = 0 and
Ai(A jw) = −A j(Aiw), ∀w ∈C ⊗S, and therefore these
ladder operators satisfy (as left actions on a general w ∈S)
the usual anticommutation relations:
{Ai, A j}w = {A†
i , A†
j}w = 0,
(36)
{Ai, A†
j}w = δi jw, ∀w ∈C ⊗S.
(37)
Each Ai ∈Oi ⊂S corresponds to a generalization of αi ∈
Hi ⊂O where now each ladder operators consists of four
terms instead of just two.
Subsequently we can proceed to construct two minimal
left ideals, in a manner identical as in Sect. 3. These ideals
are identical to Su and Sd above, and (as will be demonstrated
shortly) preserved by the same unitary symmetries, but with
both the states and symmetry generators written in terms of
the generalised ladder operators Ai and A†
i .
Su
1 = νeω1ω†
1 + dr A†
1ω1ω†
1 + dg A†
2ω1ω†
1 + db A†
3ω1ω†
1
+ur A†
3A†
2ω1ω†
1 + ug A†
1A†
3ω1ω†
1 + ub A†
2 A†
1ω1ω†
1
+e+ A†
3A†
2 A†
1ω1ω†
1,
Sd
1 = νeω†
1ω1 + dr A1ω†
1ω1 + dg A2ω†
1ω1 + db A3ω†
1ω1
+ur A3A2ω†
1ω1 + ug A1A3ω†
1ω1 + ub A2 A1ω†
1ω1
+e−A3A2 A1ω†
1ω1,
where ω1 := A1A2 A3.
123
Eur. Phys. J. C (2023) 83 :747
Page 9 of 13
747
The SU(3)C generators are now a direct generalization of
those in Sect. 3, with αi replaced by Ai:
Λ1 = −A†
2 A1 −A†
1A2,
Λ2 = i A†
2 A1 −i A†
1A2,
Λ3 = A†
2 A2 −A†
1A,
Λ4 = −A†
1 A3 −A†
3A1,
Λ5 = −i A†
1 A3 + i A†
3 A1,
Λ6 = −A†
3 A2 −A†
2 A3,
Λ7 = i A†
3A2 −i A†
2 A3,
Λ8 = −1
√
3
(A†
1A1 + A†
2 A2 −2A†
3 A3)
Furthermore, the number generator can again be used to
deﬁne a U(1) generator that (together with −Q∗) assigns
the correct electric charges to all the states:
Q = N
3 = 1
3(A†
1A1 + A†
2 A2 + A†
3A3).
(38)
