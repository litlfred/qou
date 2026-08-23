---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-040-33-the-thick-subcategory-of-negligible-objects-4
section_title: "The thick subcategory of negligible objects 47"
section_number: 3.3
pages: 55-57
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
LEMMA 3.4. For all K,M∈ D and χ∈ Π(X) one has the following
natural isomorphisms.
(a) Adjoint duality:
HomD(1,K∨∗∗ M)∼= HomD(K,M)∼= HomD(K∗! M∨,1).
(b) Character twists: (Kχ)∨∼= (K∨)χ,
(K∗! M)χ∼= Kχ∗! Mχ and (K∗∗ M)χ∼= Kχ∗∗ Mχ.
(c) Verdier duality:
D(K∗! M)∼= D(K)∗∗ D(M), D(K∗∗ M)∼= D(K)∗! D(M).
(d) K¨unneth formulae:
H•
c (X,K)⊗ΛH•
c (X,M) ∼−→ H•
c (X,K∗! M),
H•(X,K∗∗ M) ∼−→ H•(X,K)⊗ΛH•(X,M).
Proof. Part (a) follows from adjunction as in [41, p. 533]. In (b) the
ﬁrst identity comes fromRHom(Lχ,ΛX) = Lχ−1 and (−id)∗(Lχ−1) = Lχ,
and the other two follow as in proposition 2.1. Part(c) follows from the
compatibility of Verdier duality with exterior tensor products. Part(d) is
the K¨unneth isomorphism [7, exp. XVII.5.4] resp. its Verdier dual. □
3.3. The thick subcategory of negligible objects
In this and in the next section we always assume that for the abelian
varietyA = X/T the vanishing assumptionGV(A) of section 3.1 holds. We
have seen in theorem 3.1 thatGV(X) then holds as well. LetS(X)⊂ P(X)
be the full subcategory of all perverse sheaves of Euler characteristic zero,
and T(X)⊂ D(X) the full subcategory of all sheaf complexesK whose
perverse cohomology sheavespHn(K) lie inS(X) for all degreesn∈ Z. For
brevity we put
P = P(X), D = D(X), S = S(X) and T = T(X).
The following explains why we only use characters of the tame fundamental
group — we want the Euler characteristicχ(K) = ∑i∈ZdimΛ(Hi(X,K)) of
any complexK∈ D to be invariant under character twists.
LEMMA 3.5. Let K∈ D. Then χ(K) = χ(Kϕ) for allϕ∈ Π(X), hence
the following three conditions are equivalent:
(a) The complex K lies in the full subcategoryT.
(b) We have H•(X,Kϕ) =0 for genericϕ∈ Π(X).
(c) We have H•c (X,Kϕ) =0 for genericϕ∈ Π(X).
48 Chapter 3 – Perverse sheaves on semiabelian varieties
Proof.To prove the twist invariance of the Euler characteristic, we can
by d´evissage assume that the complexK is a constructible sheaf placed in
a single cohomology degree. Then [59, cor. 2.9] says that if j : X ↪→ ¯X
denotes a smooth compactiﬁcation, thenj!(K) and j!(Kϕ) have the same
Euler characteristic (the assumptions of the corollary are satisﬁed sinceχ is
a tame character, see sect. 2.6 of loc. cit.). Since for the Euler characteristic
it makes no difference whether we use compactly supported or ordinary
hypercohomology [70], it follows thatχ(K) = χ(Kϕ). The equivalence of
the three conditions(a) – (c) then follows via corollary 3.3. □
Recall that a full subcategory of an abelian category is said to be a Serre
subcategory if it is stable under the formation of arbitrary subquotients and
extensions. More generally, a full triangulated subcategory of a triangulated
category is called a thick subcategory if it has the following property: For
any morphismf : K→ L which factors over an object of the subcategory
and has its cone in the subcategory, the objectsK and L must both belong
to the subcategory as well.
COROLLARY 3.6. The subcategoryS⊂ P is Serre, andT⊂ D is thick.
Proof.Let 0−→P−→Q−→R−→0 be a short exact sequence in the
abelian categoryP. Theorem 3.1 says that for a generic characterχ∈ Π(X)
the hypercohomology of the perverse sheavesPχ, Qχ andRχ is concentrated
in degree zero so that the long exact sequence in hypercohomology reduces
to a short exact sequence
0−→H0(X,Pχ)−→H0(X,Qχ)−→H0(X,Rχ)−→0.
Therefore lemma 3.5 shows thatQ lies inS if and only if bothP and R are
in S. HenceS⊂ P is a Serre subcategory, and then the subcategoryT⊂ D
is thick by [41, prop. 3.6.1(i)]. □
In particular, localizing the abelian categoryP at the class of morphisms
whose kernel and cokernel lie in the Serre subcategoryS we can form the
abelian quotient categoryP = P/S in the sense of [42, chap. III]. Note that
the categoryP has the same objects asP and that for any objectsP1,P2
the elements ofHomP(P1,P2) can be represented by equivalence classes of
diagrams inP of the form
Qf1
zzuuuuuu f2
$$IIIIII
P1 P2
where the kernel and cokernel of the morphismf1 lie in S. In the same
way, localizing the triangulated categoryD at the class of morphisms whose
cone lies in the thick subcategoryT we can form the triangulated quotient
categoryD = D/T as described in [82, sect. 2.1].
