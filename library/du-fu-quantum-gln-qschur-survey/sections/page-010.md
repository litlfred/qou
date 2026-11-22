---
doc_id: du-fu-quantum-gln-qschur-survey
doc_title: "QUANTUM gln, q-SCHUR ALGEBRAS AND THEIR"
section_id: page-010
section_title: "Page 10"
section_number: null
pages: 10-10
source_pdf: du-fu-quantum-gln-qschur-survey.pdf
source_sha256: 6852134eaffb3137
toc_source: undetermined
doc_brief: "Quantum gl_n, q-Schur algebras and their infinite/infinitesimal counterparts — We present a survey of recent developments of the Beilinson–Lusztig–MacPherson approach in the study of quantum gln"
---
10
JIE DU AND QIANG FU
(2) There is an algebra epimorphism ϕ : ˜uk(η) ։ W satisfying Eh 7→Eh,h+1(¯0), Fh 7→
Eh+1,h(¯0), Kj 7→0(¯ej).
(3) If l′ is even, ϕ is an isomorphism and, if l′ is odd, then ϕ induces isomorphism
¯ϕ : uk(η)
∼
→W.
Corollary 5.4 ([1]). If l′ = l is odd, then we have an algebra isomorphism uk(η) ∼= k′(η).
6. Bases for q-Schur algebras
In this section, we ﬁrst describe the Drinfeld–Jimbo type presentations for q-Schur algebras
at η = [1, n], and then we introduce several resulting bases.
Theorem 6.1. The q-Schur algebra U(n, r) over Q(υ) has the following presentations with
(1) ([4]) generators
ei, fi (1 ⩽i ⩽n −1), kj (1 ⩽j ⩽n)
and relations:
(S1) kikj = kjki;
(S2) kiej = υδi,j−δi,j+1ejki, kifj = υδi,j+1−δi,jfjki;
(S3) eiej = ejei, fifj = fjfi when |i −j| > 1;
(S4) e2
i ej −(υ + υ−1)eiejei + eje2
i = 0 when |i −j| = 1;
(S5) f2
i fj −(υ + υ−1)fifjfi + fjf2
i = 0 when |i −j| = 1;
(S6) eifj −fjei = δij
eki−eki
−1
υ−υ−1 , where eki = kik−1
i+1;
(S7) k1 · · · kn = vr and, for all 1 ⩽i ⩽n, (ki −1)(ki −v) · · · (ki −vr) = 0.
(2) ([9]) generators
ei, fi, kj (1 ⩽i ⩽n −1)
and relations (S1)–(S6) together with
(S0) [k1; t1]![k2; t2]! · · · [kn−1; tn−1]! = 0 for ti ∈N such that t1 + · · · + tn−1 = r + 1,
where [X; t]! = (X −1)(X −v) · · · (X −vt−1), and kn = υrk−1
1 · · · k−1
n−1 in (S6).
Proof. Let eU(n, r) be the algebra with either of the described presentations. Then there
exist an algebra epimorphism
˜ζr : U(n) ։ eU(n, r).
The algebra epimorphism ζr : U(n) ։ V(n, r) = U(n, r) given by
Eh 7→Eh,h+1(0, r), Ki 7→0(ei, r), Fh 7→Eh+1,h(0, r),
where ei = (. . . , 0, 1
(i), 0 . . .), induces an epimorphism eU(n, r) ։ U(n, r). Thus, the result
follows if we could prove that dim eU(n, r) ⩽dim U(n, r).
We prove this inequality by constructing some integral monomial bases below.
□
We ﬁrst display an integral monomial basis for U(n). For A = A+ + A−∈Ξ±(n), where
A+ ∈Ξ+(n) and A−∈Ξ−(n), and j ∈Zn let
M (A,j) = E(A+) · K(j) · F (A−) ∈U(n)
