---
doc_id: arxiv-1909.06744v1
doc_title: "Springer correspondence for symmetric spaces"
section_id: sec-002-2-springer-correspondence-for-gln
section_title: "§2. Springer correspondence for GLn"
section_number: null
pages: 2-3
source_pdf: 1909.06744v1.pdf
source_sha256: 82e3980da78c07da
toc_source: inferred
doc_brief: "Springer correspondence for symmetric spaces — This is a survey on the Springer correspondence for symmetric spaces."
---
Throughout the paper, we assume that k is an algebraically closed ﬁeld of char-
acteristic p ≥0, and we consider ¯Ql-sheaves, where ¯Ql is an algebraic closure of the
l-adic number ﬁeld Ql with l̸ = p. Note that if p = 0, one can replace k by the com-
plex number ﬁeld C, and ¯Ql-sheaves by ordinary C-sheaves. All the representations
of ﬁnite groups are considered over ¯Ql ≃C. For a ﬁnite group Γ, we denote by Γ ∧
the set of isomorphism classes of irreducible representations of Γ.
We will start from the simplest example. Let G = GLn(k), B a Borel subgroup
of G containing a maximal torus T. Let W = NG(T)/T be the Weyl group of G.
Hence W is isomorphic to the symmetric group Sn of degree n. Let Pn be the set
of partitions λ = (λ1, . . . , λk) such that P
i λi = n. It is well-known that there is a
bijection
(2.1)
S∧
n ≃Pn,
(Vλ ↔λ)
where we normalize this so that Vλ is the identity (resp. the sign) representation if
λ = (n) (resp. λ = (1n)).
On the other hand, let Guni be set of unipotent elements in G, called the unipo-
tent variety of G. G acts on Guni by the conjugation, and Guni is a union of unipo-
tent classes of G. We denote by Guni/∼G the set of unipotent classes in G. It is also
well-known, via the Jordan normal form, that
(2.2)
Guni/∼G ≃Pn,
(Oλ ↔λ).
It follows from (2.1) and (2.2) that there exists a bijection S∧
n ≃Guni/∼G by
Vλ ↔Oλ. But this is nothing more than the parametrization of two sets, S∧
n and
Guni/∼G, coincides each other, by accident. It would be more interesting, form a
mathematical point of view, to show that there exists a “canonical” bijection between
S∧
n and Guni/∼G, independent from the parametrization. Actually, this assertion
was achieved by the discovery of the Springer correspondence, as explained below.
Let B = G/B be the ﬂag variety of G. Consider the variety
3
(2.3)
eGuni = {(x, gB) ∈Guni × B | g−1xg ∈B}
and a map π : eGuni →Guni, (x, gB) 7→x. Then eGuni is smooth, irreducible, and
π is proper. In fact, π gives a resolution of singularities of Guni, and is called the
Springer resolution of Guni. For x ∈Guni, we deﬁne a closed set Bx of B by
(2.4)
π−1(x) ≃Bx = {gB ∈B | g−1xg ∈B}.
Bx is called the Springer ﬁbre of x. Bx is not smooth, nor irreducible, but
it is an interesting variety. We consider the cohomology group Hi(Bx, ¯Ql). Then
Hi(Bx, ¯Ql) = 0 if i > 2dx, where dx = dim Bx. Thus H2dx(Bx, ¯Ql) is the top
cohomology. The following result holds.
Theorem 2.1 (Springer). Let x ∈Guni.
(i) Hi(Bx, ¯Ql) has a structure of Sn-module, called the Springer representa-
tion of Sn.
(ii) H2dx(Bx, ¯Ql) is an irreducible Sn-module.
(iii) The map x 7→H2dx(Bx, ¯Ql) induces a “canonical” bijection
Guni/∼G ∼
−→S∧
n.
(iv) For x ∈Oλ, H2dx(Bx, ¯Ql) ≃Vλ as Sn-modules. Hence we obtain the corre-
spondence Oλ ↔Vλ.
The bijective correspondence in (iii) is called the Springer correspondence.
