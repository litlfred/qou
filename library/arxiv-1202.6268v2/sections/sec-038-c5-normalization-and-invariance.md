---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-038-c5-normalization-and-invariance
section_title: "C.5. Normalization and invariance"
section_number: null
pages: 44-46
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
has always been a subtle issue. For the integral of [
Dim], ambiguities in the normalization
come from two sources: the projectivity of the Weil representat ion, and the incomplete
invariance of the integral (even formally) under a change of “quad type” and a 2–3 move.
Let us consider the Weil representation ﬁrst. We will assume that a ll symplectic matrices
are in Sp(2N, Z), and that all shifts involve integers (like ν and νP ) times iπ + ℏ
2 . This as-
sumption (which, again, is only an observed property) allows us to imp rove on the estimates
of [ Dim] ( cf. Eqn.(6.6) there). The Weil representation becomes a projective u nitary repre-
sentation of ISp(2N, Z)≃ Sp(2N, Z) ⋉
[(
iπ + ℏ
2
)
Z
] 2N
onL2(RN ), for ℏ pure imaginary. Our
Hilbert spaceH⊗2N
∆ is very close to L2(RN ), so we may hope that the Weil representation is
also unitary projective there. The most severe projective ambigu ity arises from a violation of
THE QUANTUM CONTENT OF THE GLUING EQUATIONS 45
expected commutation relations between shifts and T -type transformations such as ( C.19).
This leads to projective factors of the form
(C.24) exp
[ 1
2ℏ
(
iπ + ℏ
2
) 2
a
]
= exp
[(
− π2
2ℏ + iπ
2 + ℏ2
8
)
a
]
, a ∈ Z.
With the exception of factors like this, unitarity with respect to the norm
||f||2 =
∫ dNZ
(±2πiℏ)N/ 2|f (Z)|2
may be used to normalize Weil transformations. For example, the fa ctor
[
(2πiℏ)N det B
] −1/ 2
in ( C.20) follows easily from formal manipulations on the integral transform ation to demon-
strate unitarity.
The lack of complete invariance under a change of quad type (cyclic p ermutation invari-
ance) and a 2–3 move can also ruin the normalization of the state inte gral. The change
of quad type was analyzed, formally, in Section 6.2.1 of [ Dim]. A cyclic permutation of a
tetrahedron is accomplished by an aﬃne version of the element ST∈ Sp(2N; Z), under the
Weil representation. The single-tetrahedron wavefunction tran sforms as
(C.25) ψℏ(Z) ↦→
∫ dZ√
2πiℏ
e
1
2ℏ
(
Z 2+2ZZ ′−(2πi +ℏ)Z
)
ψℏ(Z) = e
π 2
6ℏ ± iπ
4 − ℏ
24ψℏ(Z ′).
The last equality follows from the Fourier transform of the quantum dilogarithm [ FKV01,
PT01]. This shows that the tetrahedron wavefunction is invariant under permutations, up
to a factor
(C.26) exp
[( π2
6ℏ± iπ
4 − ℏ
24
)
a
]
, a ∈ Z.
The analysis of the 2–3 move is slightly more involved. It was done in ter ms of operator
algebra in [ Dim], and then explained in terms of wavefunctions in Section 6.2 of [ DGG]. The
main idea is that a 2–3 move can be done locally during the gluing procedu re, by performing
a formal, “local” transformation on the state integral. The crucial property involved is the
Ramanujan-like identity for the quantum dilogarithm [ FKV01, PT01], which expresses three
quantum dilogarithms as an integral of two; for example,
ψℏ(W ′
1)ψℏ(W ′
2)ψℏ(W ′
3)
⏐
⏐
W ′
1+W ′
2+W ′
3=2πi +ℏ
∼
∫ dZ
√
2πiℏ
e
1
2ℏ
(
Z 2+2W ′
2Z−(2πi +ℏ)(W ′
1+W ′
2+Z)
)
ψℏ(−Z)ψℏ(Z−W ′
1)(C.27)
which holds up to a factor that is again of the type (
C.26).
Putting together all three eﬀects, we ﬁnd that we might be able to c ontrol the overall
normalization of the state integral up to a factor of the form
(C.28) exp
[ π2
6ℏa + iπ
4 b + ℏ
24c
]
, a,b,c ∈ Z.
46 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
