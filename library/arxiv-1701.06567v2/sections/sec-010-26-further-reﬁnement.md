---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-010-26-further-reﬁnement
section_title: "Further reﬁnement"
section_number: 2.6
pages: 19-20
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
As we discussed above, for Seifert 3-manifolds the theory T [M3] has an extra U(1)β ﬂavor
symmetry. In particular, this is the case for M3 =L(p, 1), which will serve as an important
example to us later. This ﬂavor symmetry in T [M3] results in the presence of an extra Z-
grading in homological invariants HD2 andHS2 considered in the previous sections and a
possibility to consider the corresponding reﬁned indices (equivariant Euler characteristics):
ˆZa(q;t) =
∑
i∈Z+∆a,
j,𝓁∈Z
qit𝓁(−1)j dimHi,j;𝓁
a , (2.35)
and
I(q;t) =
∑
i,j,𝓁∈Z
qit𝓁(−1)j dimHi,j;𝓁
S2 . (2.36)
19For reasons similar to the ones described at the end of the previous section, in general a negative power
of 2 can appear as an overall factor. We omit it in some generic formulas to avoid clutter and instead focus
attention on the conceptual structure. As mentioned earlier and as we shall see in examples, the eﬀect of such
fractions on categoriﬁcation can typically be traced to the existence of bosonic modes with zero q-grading.
20For a generic 3-manifold M3, the analytic continuation of the series ˆZa(q)∈ Z[[q]] convergent in|q| < 1
may not exist outside|q| = 1, at least in the standard way. However, one possible way to deﬁne it for general
M3 is
ˆZa(q−1) ≡ ˆZa(q)
⏐⏐⏐
M3→M 3
, (2.34)
where M3 denotes M3 with the reversed orientation. Note that therefore I(q), unlike ˆZa(q), is insensetive to
the orientation.
– 18 –
where, from the physics point of view, 𝓁 is the U(1)β charge. The reﬁned indices obviously
provide more information about the underlying vector spaces and, as we will see in examples,
can be used sometimes to compute (conjecturally) the full homological invariants via the
“homological-ﬂavor locking” phenomenon that we will explain later.
The reﬁned version of the factorization formula ( 2.33) reads
I(q;t) =
∑
a∈ TorH1(M3,Z)/Z2
|Wa|ˆZa(q;t)ˆZa(q−1;t−1). (2.37)
