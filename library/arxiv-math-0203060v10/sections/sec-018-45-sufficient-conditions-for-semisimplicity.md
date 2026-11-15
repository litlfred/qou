---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-018-45-sufficient-conditions-for-semisimplicity
section_title: "Sufficient conditions for semisimplicity"
section_number: 4.5
pages: 17-18
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
toc_source: outline
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
ment of [N, Proposition 6.4] and is analogous to the Larson-Radford theorem [LR1]
for usual Hopf algebras which says that if A is a ﬁnite dimensional Hopf algebra
with Tr(S2|A)̸ = 0 then A is semisimple and cosemisimple.
Proposition 4.10. Let A be a ﬁnite dimensional weak Hopf algebra. If for every
primitive idempotent p in At ∩Z(A) there exist idempotents qp, q′
p in pAt such that
(20)
Tr(S2|qpAS(q′
p))̸ = 0,
then A is semisimple.
Proof. Let ℓand λ be a dual pair of non-degenerate left integrals in A and A∗re-
spectively. Then (ℓ(2) ⇀λ)⊗qpS−1(ℓ(1))S(q′
p) is the dual bases tensor for qpAS(q′
p),
cf. [N]. Therefore,
0̸
=
Tr(S2|qpAS(q′p))
=
⟨ℓ(2) ⇀λ, qpS(ℓ(1))S(q′
p) ⟩
=
⟨λ, qpεs(q′
pℓ) ⟩.
Therefore, yp := εs(q′
pℓ)̸ = 0. Next, we compute
ypℓ
=
S(ℓ(1))S(q′
p)ℓ(2)ℓ
=
S(ℓ(1))S(q′
p)εt(ℓ(2))ℓ
=
S(ℓ(1))εt(ℓ(2))S(q′
p)ℓ= S(ℓ)yp.
Let ξp be an element in A∗
t (here and below we write A∗
t := (A∗)t, A∗
s := (A∗)s)
such that ξp ⇀1 = yp. Then from the previous computation we have
(21)
ypℓ= (α ⇀ℓ)yp,
where α is a distinguished group-like element of A∗. Arguing as in [N, Proposition
6.4] one gets
(22)
ξp = S(ξp)α,
18
PAVEL ETINGOF, DMITRI NIKSHYCH, AND VIKTOR OSTRIK
whence α is trivial, i.e., α ∈A∗
min. This means that one can choose ℓin such a
way that α = ǫ, i.e., ℓ= S(ℓ). Hence, yp ∈As ∩Z(A) is a non-zero multiple of
p. We conclude that y := εs(ℓ) = P
p yp is an invertible central element of A.
Hence, ℓ′ = y−1ℓis a normalized right integral in A. By Maschke’s theorem, A is
semisimple.
□
Let q qnd q′ be idempotents in At, and let ρ = ǫ ↼q and ρ′ = ǫ ↼q′. Then ρ
and ρ′ are idempotents in A∗
t .
Lemma 4.11. The space ρA∗S(ρ′) may be identiﬁed, in an S2-invariant way, with
the dual space of qAS(q′).
Proof. It is easy to check that for all h ∈A and φ ∈A∗one has ⟨φ, qhS(q′) ⟩=
⟨ρφS(ρ′), h ⟩, whence the statement follows.
□
The next three corollaries reﬁne [N, Corollaries 6.5 - 6.7].
Corollary 4.12. Let A be a ﬁnite dimensional weak Hopf algebra. If for every
primitive idempotent π in A∗
t ∩A∗
s there exist idempotents ρπ, ρ′
π in πA∗
t such that
(23)
Tr(S2|ρπA∗S(ρ′π))̸ = 0,
then A is semisimple.
Proof. This immediately follows from Proposition 4.10 and Lemma 4.11, since the
latter implies Tr(S2|ρπA∗S(ρ′π)) = Tr(S2|qpAS(q′p)).
□
Corollary 4.13. Let A be a connected ﬁnite dimensional weak Hopf algebra. If
there exist idempotents q, q′ in At such that Tr(S2|qAS(q′))̸ = 0 then A is semi-
simple.
Corollary 4.14. Let A be a biconnected ﬁnite dimensional weak Hopf algebra. If
there exist idempotents q, q′ in At such that Tr(S2|qAS(q′))̸ = 0 then A and A∗are
semisimple.
