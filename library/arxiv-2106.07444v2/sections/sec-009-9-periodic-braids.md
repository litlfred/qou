---
doc_id: arxiv-2106.07444v2
doc_title: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS"
section_id: sec-009-9-periodic-braids
section_title: "Periodic Braids"
section_number: 9
pages: 61-64
source_pdf: 2106.07444v2.pdf
source_sha256: 5acca39c07bcdddd
doc_brief: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS — Let W be the W eyl group of a split semisimple group G. Its Hecke category HW can be built from pure perverse sheaves on the double ﬂag variety of G."
---
9.1. In this section and the next, we no longer assume that W is crystallographic.
Letw0 be the longest element of W with respect to the chosen Coxeter presentation
(see § A.1). The full twist of BrW is the positive braid
π =σ2
w0 ∈ Br +
W.
It is central in BrW [BM97, §2]. We say that a braid β ∈ BrW is periodic iﬀ
βn =πm
for some m
n ∈ Q, in which case we say that m
n is the slope of β.
Theorem 9.1.1 (Lee–Lee). If β ∈ BrW is periodic of slope m
n , then β =γm and
π =γn for some γ ∈ BrW .
Proof. Let d be the minimal positive exponent such that σd
w0 is central in BrW .
Either d = 1 or d = 2.
In [ LL], E.-K. Lee and S.-J. Lee say that an element γ ∈ BrW is primitive iﬀ,
wheneverγ =δℓ for some δ ∈ BrW , we have ℓ = ±1. Theorem 3.14 of ibid. implies
that if γ is primitive and periodic, then γ is a positive root of σd
w0 .
If β is periodic, then any root of β is also periodic. So it remains to check that
some root of β is primitive. Indeed, this follows from the well-ordering p rinciple,
because the writhe of β is an integer. □
Remark 9.1.2. In type A, where the elements of BrW represent topological braids,
Theorem 9.1.1 was ﬁrst shown in 1934 by Kerékjártó–Eilenberg [ E].
Remark 9.1.3. A result of Bessis implies that if an nth root of π exists, then the
nth roots of π form a single conjugacy class in BrW [Bes, Thm. 12.4(ii)].
9.2. The following result, an incarnation of Schur’s lemma, is [ GP, Thm. 9.4.3].
Theorem 9.2.1 (Springer). For all φ ∈ ˆW , the full twist acts on the underlying
HW -module of φq by the scalar qc(φ), where c(φ) is the content of φ (see § A.10).
In particular, φq(π) = qc(φ)φ(1).
The following corollary is a mild generalization of [ BM97, Prop. 9.2.8], but we
give the proof anyway. The proof is based on [ J, Lem. 9.4], which Jones used to
calculate the HOMFLY polynomials of torus knots.
Corollary 9.2.2. If φ ∈ ˆW and β ∈ BrW is periodic of slope ν ∈ Q, then
φq(β) = qνc(φ)φ(w),
wherew ∈W is the image of β under the surjection Br W ։W .
Proof. It suﬃces to prove the result when q
1
2 has been specialized to a generic
complex number q
1
2 . We set
HW [q
1
2 ] = HW ⊗Z[q±1/2] C,
62 MINH-TÂM QUANG TRINH
where Z[q± 1
2 ] → C sends q
1
2 ↦→q
1
2 , and
φq =φq|q1/2=q1/2.
Writeν = m
n in lowest terms. By the theorem, q−mc(φ)πm acts on the underlying
HW [q
1
2 ]-module of φq by the identity operator I. Since βn =πm, we deduce that
q−νc(φ)β acts by an nth root of I.
Recall that HW |q=1 = Z[W ]. Choose a generic path in the complex plane from
q to 1. Since the (diagonalizable) roots of I do not deform, the deformation of q
along this path shows that the following operators must have the same eigenvalue
spectrum:
• The action of q−νc(φ)β on the underlying H[q
1
2 ]-module of φq.
• The action of w on the underlying C[W ]-module of φ.
The result follows. □
9.3. Let V be a realization of W over C such that VW = 0. A vector of V is
regular with respect to W iﬀ its stabilizer in W is trivial, or equivalently, it avoids
the reﬂecting hyperplanes that generate the W -action. Suppose that an element
w ∈W admits a regular eigenvector in V with eigenvalue ζ ∈ C×. In this case, ζ
must be a root of unity. We say that ζ is regular with respect to W and that w
is a ζ-regular element ofW . The following results are parts (iv) and (v) of [ S74,
Thm. 4.2], respectively.
Theorem 9.3.1 (Springer). For any ζ ∈ C×, the set of ζ-regular elements of W
is either empty or forms a single conjugacy class.
Theorem 9.3.2 (Springer). If w ∈W is a ζ-regular element, then
φ(w) = Fegφ(ζ−1) = Fegφ(ζ)
for all φ ∈ ˆW , where Fegφ is the fake degree of φ (see § A.8).
Remark 9.3.3. In [ S74, 170], Springer claims that if n is a ﬁxed integer, then the
regular elements of W of order n form a single conjugacy class. This claim, which
is stronger than Theorem 9.3.1, fails when W is not crystallographic. For example,
letW be the Coxeter group of type I2(5) and let w be a Coxeter element. Then w
and w2 are both regular elements of order 5, but they are not conjuga te.
Regular elements of W are related to periodic elements of BrW by the following
results, which are respectively Proposition 3.11 and Théor ème 3.12 in [ BM97].
Proposition 9.3.4 (Broué–Michel). If w ∈W is regular of order n, then σn
w =π.
Theorem 9.3.5 (Broué–Michel). Ifγ ∈ Br +
W satisﬁes γn =π for some n, then its
image in W is a e
2πi
n -regular element.
Corollary 9.3.6. If β ∈ BrW is periodic of slope ν ∈ Q, then the image of β in
W is a e2πiν -regular element.
Proof. This is immediate from Theorem 9.3.5 whenβ is a root of π. Theorem 9.1.1
lets us bootstrap to the general case. □
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 63
Remark 9.3.7. We emphasize that Theorem 9.3.5 is deeper than Proposition 9.3.4:
Its proof relies on results used by Charney to prove the biaut omaticity of Artin
groups [ BM97, §3.19].
9.4. Theorem 10 states that if β ∈ BrW is periodic of slope ν ∈ Q, then its R(W )
trace is given by
⟨β⟩ q =
∑
ψ∈ ˆW
qνc(ψ)Degψ(ζ)ψ,
where ζ =e2πiν and Degφ is the unipotent degree of φ (see § A.8).
Proof of Theorem 10. By Corollary 9.3.6, the image ofβ inW is aζ-regular element.
Therefore, by Corollary 9.2.2 and Theorem 9.3.2,
φq(β) = qνc(φ)Fegφ(ζ).
Therefore, by Lemma-Postulate A.9.1(2) and Corollary A.10.4,
∑
φ∈ ˆW
{φ,ψ }φq(β) = qνc(ψ) ∑
φ∈ ˆW
{φ,ψ }Fegφ(ζ)
= qνc(ψ)Degψ(ζ),
as needed. □
64 MINH-TÂM QUANG TRINH
