---
doc_id: du-fu-quantum-gln-qschur-survey
doc_title: "QUANTUM gln, q-SCHUR ALGEBRAS AND THEIR"
section_id: page-002
section_title: "Page 2"
section_number: null
pages: 2-2
source_pdf: du-fu-quantum-gln-qschur-survey.pdf
source_sha256: 6852134eaffb3137
toc_source: undetermined
doc_brief: "Quantum gl_n, q-Schur algebras and their infinite/infinitesimal counterparts — We present a survey of recent developments of the Beilinson–Lusztig–MacPherson approach in the study of quantum gln"
---
2
JIE DU AND QIANG FU
Parallel to the inﬁnitesimal theory for quantum gln, little q-Schur algebras are discussed
in §7.
For the rest of the paper, we focus on the case when η = Z.
In §8, we discuss
presentations of the algebras U(∞, r). Inﬁnite q-Schur algebras S(∞, r) are introduced and
the relations between S(∞, r) and quantum gl∞are discussed in §9. In particular, we show
that U(∞, r) is a proper subalgebra of S(∞, r). We end the paper by discussions on the
representation theory of quantum gl∞. We discuss the highest weight representations in §10
and their polynomial type representations in §11.
Acknowledgement. The ﬁrst author would like to thank the organizers for the oppor-
tunity to attend the conference and for the ﬁnancial support.
2. Quantum glη, infinitesimal quantum glη, and q-Schur algebras
Let η ⊆Z be a consecutive segment of Z. In other words, η is a subset of the form
[m, n] := {i ∈Z | m ⩽i ⩽n} or one of the sets (∞, m], [n, ∞) and Z, where m, n ∈Z, Let
η⊣= η\{max(η)} if η is bounded above, and η⊣= η otherwise. We also denote by Mη(R)
(resp. Rη) the set of all matrices (ai,j)i,j∈η (resp. all sequences (ai)i∈η) with all entries in
a set R of numbers, and will always abbreviate the sub-/supscript η by n if η = [1, n], and
by ∞if η = Z. Moreover, we also assume that, if η is inﬁnite, then the elements in Mη(R)
(resp., Rη) have ﬁnite support, i. e., all ai,j = 0 (resp. ai = 0) but ﬁnitely many of them.
Let U(η) := Uv(glη) be quantum glη deﬁned over Q(v). Then, U(η) is the algebra over
Q(υ) presented by generators
Ei, Fi
(i ∈η⊣), Kj, K−1
j
(j ∈η)
and relations
(a) KiKj = KjKi, KiK−1
i
= 1;
(b) KiEj = υδi,j−δi,j+1EjKi;
(c) KiFj = υδi,j+1−δi,jFjKi;
(d) EiEj = EjEi, FiFj = FjFi when |i −j| > 1;
(e) EiFj −FjEi = δi,j
e
Ki−e
K−1
i
υ−υ−1 , where eKi = KiK−1
i+1;
(f) E2
i Ej −(υ + υ−1)EiEjEi + EjE2
i = 0 when |i −j| = 1;
(g) F 2
i Fj −(υ + υ−1)FiFjFi + FjF 2
i = 0 when |i −j| = 1.
When η is an inﬁnite segment, U(η) can be regarded as the quantum enveloping algebra
associated with an ∞× ∞Cartan matrix.
We also set U(η) =
(
U(n),
if η = [1, n];
U(∞),
if η = Z.
Clearly, we have natural algebra embedding
U([−n, n]) ⊆U([−n −1, n + 1]) for all n ⩾0. Hence, obtain an algebra isomorphism
(2.0.1)
U(∞) ∼= lim
−→
n
U([−n, n])
We will see in §4 that U(η) can be reconstructed as a vector space together with a given
basis and certain explicit multiplication formulas between basis elements and generators.
