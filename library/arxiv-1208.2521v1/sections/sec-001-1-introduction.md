---
doc_id: arxiv-1208.2521v1
doc_title: "On q-analogues of the Fourier and Hankel transforms"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 1208.2521v1.pdf
source_sha256: 8d0281aa84043865
doc_brief: "On q-analogues of the Fourier and Hankel transforms — For the third q-Bessel function (ﬁrst introduced by F. H. Jackson, later rediscovered by W. Hahn in a special case and by H."
---
Several possible q-analogues of the Bessel function
(1.1) Jα (x) :=
∞∑
k=0
(−1)k (x/ 2)α +2k
k! Γ( α + k + 1)
have been considered in the literature. Best known are two re lated q-Bessel func-
tions denoted J (1)
α (x; q) and J (2)
α (x; q) by Ismail [10], but ﬁrst introduced by Jackson
in a series of papers during the years 1903–1905 (see the refe rences in [10]) and also
studied by Hahn [7]. A third q-Bessel function was introduced by Hahn [8] (in a
special case; we thank G. Gasper for this reference) and by Ex ton [3], [4, (5.3.1.11)]
(in full). In Exton’s notation:
(1.2) Cα (q; x) := (1 − q)α
(q; q)∞
∞∑
k=0
qk(k− 1)/ 2 (qα +k+1; q)∞ (−x(1 − q)2)k
(q; q)k
,
1991 Mathematics Subject Classiﬁcation . Primary 33A40, 33A30; Secondary 42A38, 42C05.
This paper appeared in Trans. Amer. Math. Soc. 333 (1992), 445–4 61. In the present version
the statement and proof of Proposition 4.2 and the proof of Propos ition A.1 have been corrected.
Typeset by AMS-TEX
1
2 TOM H. KOORNWINDER AND REN ´E F. SW ARTTOUW
where the q-shifted factorials are deﬁned by
(1.3) ( a; q)k :=
k− 1∏
j=0
(1 − aqj), k = 1, 2, . . . ; ( a; q)0 := 1;
(a; q)∞ := lim
k→∞
(a; q)k, |q| < 1.
Hahn [8] considered the case α = 0 of (1.2). They obtained these functions as
the solutions of a special basic Sturm-Liouville equation, by which they could also
derive the following q-analogue of the Fourier-Bessel orthogonality relations:
∫ 1
0
xα Cα (q; µ iqx) Cα (q; µ jqx) dqx = 0, i ⁄= j, α > −1,
where µ 1, µ 2, . . . are the roots of the equation Cα (q; µ ) = 0, and where the q-integral
is deﬁned by ∫ 1
0
f (x) dqx := (1 − q)
∞∑
k=0
f (qk) qk.
By specialization to α = ±1/ 2, Exton obtained similar orthogonalities for q-
analogues of the sines and cosines. So some of the harmonic an alysis involving
Bessel functions, sines and cosines has been extended to the q-case. However, q-
analogues of the Fourier-cosine, Fourier-sine and Hankel t ransforms were missing
until now (except for a q-Laplace transform with inversion formula, cf. Hahn [7, §9]
and Feinsilver [5]).
Exton [4, (5.3.3.1)] also generalized the generating funct ion
(1.4) ez(t− t− 1)/ 2 =
∞∑
k=−∞
tk Jk(z)
(cf. Watson [15, §2.1 (1)]) to the case of his q-Bessel functions (1.2):
(1.5) eq((1 − q)t) Eq(−(1 − q)t− 1x) =
∞∑
n=−∞
tn Cn(q; x),
where
(1.6) eq(z) :=
∞∑
k=0
zk
(q; q)k
= 1
(z; q)∞
, |z| < 1,
and
(1.7) Eq(z) :=
∞∑
k=0
qk(k− 1)/ 2 zk
(q; q)k
= (−z; q)∞
ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS 3
are q-analogues of the exponential function (cf. Gasper and Rahm an [6, (1.3.15),
(1.3.16)]).
Recently, Vaksman and Korogodski ˘ ı [14] gave an interpretation of the q-Bessel
functions (1.2) as matrix elements of irreducible represen tations of the quantum
group of plane motions. Their paper, which does not contain p roofs, implicitly
contains some new orthogonality relations for the function s (1.2). In particular,
the unitariness of the representations implies a q-analogue of the Hansen-Lommel
orthogonality relations
(1.8) δnm =
∞∑
k=−∞
Jk+n(x) Jk+m(x), n, m ∈ Z
(cf. [15, §2.5 (3),(4)]). Furthermore, the Schur type orthogonality r elations for
matrix elements of irreducible unitary representations wh ich are square integrable
with respect to a suitable Haar functional, yield a q-analogue of Hankel’s Fourier-
Bessel integral
(1.9) f (x) =
∫ ∞
0
Jα (xt)
( ∫ ∞
0
Jα (ty) f (y) y dy
)
t dt,
cf. [15, §14.3].
It is the purpose of the present note to state these two types o f orthogonality
relations for the functions (1.2) explicitly, to show that t he ﬁrst type is immediately
implied by the generating function (1.5), and to rewrite the ﬁrst type as the second
type by use of a simple, but possibly new, symmetry for the fun ctions (1.2). This
will be done in §2. In §3 we will show that the second type of orthogonality is, on the
one hand, a limit case of the orthogonality for the little q-Jacobi polynomials, and,
on the other hand, allows the Hankel transform inversion for mula as a limit case
for q ↑ 1. In §4 we will generalize the two orthogonality relations to two e quivalent
formulas, which are respectively the q-analogues of Graf’s addition formula and the
Weber-Schafheitlin discontinuous integral. The special c ases of the q-Fourier-cosine
and sine transforms will be the topic of §5. No material from §4 is needed in this
section. Finally, Appendix A will contain rigorous proofs o f two limit results.
In a recent paper by Rahman [13], where a q-analogue of the Fourier-Bessel
orthogonality for Jackson’s q-Bessel functions is discussed, the author states in his
concluding remarks that Jackson’s q-Bessel functions have probably nicer properties
than those of Exton. However, the results obtained in [14] an d in the present
paper might suggest that the Hahn-Exton functions are more s uitable for harmonic
analysis, both within and without the context of quantum gro ups. Future research
will help to clarify the merits of the various types of q-Bessel functions.
In this paper we will not preserve Exton’s notation Cα (q; x) in (1.2), but state
the results in terms of the q-hypergeometric function
(1.10) 1φ 1(0; w; q, z ) :=
∞∑
k=0
(−1)k qk(k− 1)/ 2 zk
(w; q)k (q; q)k
.
