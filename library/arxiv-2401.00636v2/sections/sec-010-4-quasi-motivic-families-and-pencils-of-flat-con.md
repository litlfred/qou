---
doc_id: arxiv-2401.00636v2
doc_title: "PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS"
section_id: sec-010-4-quasi-motivic-families-and-pencils-of-flat-con
section_title: "Quasi-motivic families and pencils of flat connections"
section_number: 4
pages: 10-11
source_pdf: 2401.00636v2.pdf
source_sha256: 35e372d04cedf234
toc_source: outline
---
4.1. Quasi-motivic families. It is often hard to prove directly that a given family ∇of
ﬂat connections is periodic, as the operators Aj may be diﬃcult to compute. However, if
k = C and ∇has regular singularities, there is an approach to checking this property using
the monodromy of ∇. This approach is based on the following theorem.
Theorem 4.1. A family ∇of ﬂat connections with regular singularities on a complex variety
X has periodic monodromy if and only if it is periodic.
Proof. Any periodic family has periodic monodromy, so we just need to prove the “only if”
direction.
Consider the family of ﬂat connections ∇(j)(s) := ∇(s + ej) ⊗∇(s)∗. Thus ∇(j)(s) has
monodromy representation ρs+ej ⊗ρ∗
s.
By assumption, the periodicity condition for index j holds for s belonging to some subset
Sj ⊂Cn which is not contained in a countable union of proper Zariski closed subsets. For
a ﬁxed j and s ∈Sj ﬁx an isomorphism ψs : ρs ∼= ρs+ej. There exists a ﬂat holomorphic
section Aj(s) of ∇(j)(s) such that Aj(s, x0) = ψs; in particular, Aj(s, x) ∈GL(V ) for all
x ∈X.
Fix a smooth compactiﬁcation X of X such that X \ X is a normal crossing divisor (it
exists by Hironaka’s theorem). Since ∇(j)(s) has regular singularities, the functions Aj(s, x)
have at worst power growth near X \X. Hence they are meromorphic functions on X. Thus
Aj(s, x) are rational functions, i.e., Aj(s) ∈GL(V )(C[X]).
Fix a basis {fi, i ∈Z≥1} of C[X]. For M ∈N let Sj(M) ⊂Sj be the set of s ∈S for which
Aj(s, x) =
M
X
l=1
Ajl(s)fl(x).
for suitable matrices Ajl(s). It is clear that Sj(M) ⊂Sj(M + 1) and ∪MSj(M) = Sj. Since
Sj is not contained in a countable union of proper Zariski closed subsets, there exists M for
which Sj(M) is Zariski dense in Cn. The property that Aj(s, x) is a ﬂat section of ∇(j)(s)
is then a system of homogeneous linear equations on the matrices Ajl(s), l = 1, ..., M, over
C(s). By Chevalley’s elimination of quantiﬁers, since this system has an invertible solution
for s ∈Sj(M), it must have one over C(s), where s is a collection of variables, as claimed.
□
Remark 4.2. If ∇has irregular singularities, then it can have periodic monodromy without
being periodic, for example, ∇(s) = d −s on X = A1 (the monodromy is trivial for all
s since X is simply connected). We expect, however, that Theorem 4.1 can be extended
to the irregular case (at least when dim X = 1) if the condition of periodic monodromy is
replaced by “periodic monodromy and Stokes data”. We hope that this can be done using
the techniques of [Ka].
Theorem 4.1 motivates the following deﬁnition.
Deﬁnition 4.3. We say that a family ∇of ﬂat connections over an algebraically closed ﬁeld
k of characteristic zero is quasi-motivic if
(i) ∇(s) has regular singularities for all s ∈kn, and
(ii) ∇is periodic.
By Theorem 4.1, if k = C then ∇is quasi-motivic if and only if it has regular singularities
and periodic monodromy.
PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS
11
