---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams"
section_id: sec-014-42-the-pivotal-indicators
section_title: "The pivotal indicators"
section_number: 4.2
pages: 21-24
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
toc_source: outline
doc_brief: "Fusion categories via string diagrams — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
The pivotal indicators
In this subsection we compute the paired dimensions explicitly and deﬁne the
pivotal indicators.
21
Let C be a fusion category, with representative simple objects Xi, i ∈I.
The right duality induces a map ∗: I →I with ∗∗= id. Choose for each i ∈I
a nonzero map ηi : 1 →Xi∗⊗Xi:
Deﬁne ˆηi : Xi∗⊗Xi →1 as the linear dual of ηi, so that
= 1
for all i ∈I. Deﬁne the complex numbers ai as the coeﬃcients appearing in the
associator expansion
= ai
+ other terms.
(26)
Similarly deﬁne bi as the coeﬃcients appearing in the inverse associator expan-
sion
= bi
+ other terms.
(27)
Clearly, these coeﬃcients are precisely the numbers appearing in
= ai
,
= bi
.
(28)
In particular, they are nonzero as C is rigid (if they were zero, it would be
impossible to choose counit maps satisfying the rigidity equations).
Example 4.4. In the Yang-Lee category, we read oﬀfrom (7) that aτ = −1
2(1+
√
5). In category E, we read oﬀfrom (10) that ax = 1 +
√
3; similarly ay = 1.
Lemma 4.5. bi = ai∗for all i ∈I.
Proof. Adapted from [1, Prop 5.3.13]. Consider evaluating the morphism
22
in two diﬀerent ways. On the one hand, by dragging the right-most ηi down-
wards, and then using (28a), it equals aiηi.
On the other hand, by drag-
ging the left-most ηi downwards, and then using (28b), it equals bi∗ηi. Hence
ai = bi∗.
For each i ∈I, deﬁne ϵi : Xi ⊗Xi∗→1 by
= 1
ai
.
We have just proved the following:
Lemma 4.6. For each i ∈I, (ηi, ϵi) satisfy the rigidity equations furnishing
Xi∗as a right dual of Xi.
Corollary 4.7. The paired dimensions compute as d{i,i∗} =
1
ai∗ai
.
Lemma 4.8. There exists a choice of basis of the ηi such that ai = ai∗for all
i ∈I.
Proof. If Xi is self-dual, then i = i∗so we are done. Partition the non self-
dual objects into ordered pairs (Xi, Xi∗). Scale the ηi by setting η′
i = ηi and
η′
i∗= λiηi∗where λi is a root of λ2
i = ai
ai∗. In this new basis we have a′
i = a′
i∗.
In such a basis we have a−2
i
= d{i,i∗} for all i ∈I. By Theorem 3.19, the
paired dimension d{i,i∗} is a positive real number, with the fusion dimension
di deﬁned as its positive square root. Hence ai = ± 1
di
. If Xi is not self-dual
and ai = −di, then we can remove this sign by setting η′
i = −ηi, η′
i∗= ηi∗,
after which we have a′
i = di. We call such a basis choice ηi ∈Hom(1, Xi∗⊗Xi)
satisfying ai > 0 for all non self-dual Xi a fair basis.
Note that if Xi is self-dual then this sign cannot be removed. We record this
as a deﬁnition.
Deﬁnition 4.9. Let C be a fusion category over C. The pivotal indicator p(Xi)
of a simple object Xi is deﬁned as follows. If Xi is not self-dual, p(Xi) = 1.
If Xi is self-dual, then p(Xi) is the sign of the coeﬃcient ai appearing in the
associator expansion
= ai
+ other terms.
where ηi : 1 →Xi ⊗Xi is some nonzero vector (the number ai is independent
of this choice).
Example 4.10. In the Yang-Lee category, we read oﬀfrom (7) that p(τ) = −1.
In category E, we read oﬀfrom (10) that p(x) = 1, similarly p(y) = 1.
23
Remark 4.11. As in Remark 4.3, the pivotal indicator p(Xi) of a self-dual
simple object is closely related, but not equal to, the 2nd Frobenius-Schur in-
dicator ν2(Xi) of a self-dual simple object, as deﬁned in [23]. The former is
deﬁned using only the underlying fusion category, while the latter depends on a
pivotal structure γ, whence we can write it as νγ
2 (Xi). The precise relationship
is
νγ
2 (Xi) = γip(Xi)
where γi = ±1 is the sign associated to the self-dual object Xi in the pivotal
structure γ (see Section 5.1).
