---
doc_id: arxiv-q-alg-9702017v2
doc_title: "Idempotents of Hecke algebras of type A"
section_id: sec-005-6-connections-with-the-quantum-group-invariants
section_title: "Connections with the quantum group invariants"
section_number: 6
pages: 25-40
source_pdf: 9702017v2.pdf
source_sha256: 282c911abb2a54e9
toc_source: outline
doc_brief: "Idempotents of Hecke algebras of type A — We use a skein-theoretic version of the Hecke algebras of type A to present three-dimensional diagrammatic views of Gyoja’s idempotent el- ements, based"
---
ants
Here we discuss brieﬂy the relationship between the Homﬂy polynomial and the
SU(N)q–invariants and the bearing the idempotent elements of Sect. 4 have on
this relationship. For more details, the reader is referred to [2] and [15].
Let Qλ denotes the closure of (1/αλ) eλ in the Homﬂy skein of the annulus,
or equally of (1/αλ) Eλ in the skein of D2 × S1.
Theorem 6.1 ([20]) The quantum invariant J(L; V✷, · · ·, V✷) of the link L with
each component decorated by the fundamental representation is given as a function
of s by the framed Homﬂy polynomial X (L), evaluated at x = s−1/N and v = s−N.
We will denote this evaluation of X by XN.
Every element of S(Rn
n) determines an endomorphism of the n-fold tensor
product of the fundamental representation, V ⊗n
✷. Let Φ denote the map which
takes an (n, n) tangle to this endomorphism.
Jimbo [9] showed that Φ is a
surjective ring homomorphism.
Proposition 6.2 ([2]) For every Young diagram λ with n cells, the endomor-
phism of V ⊗n
✷
determined by Φ(eλ) is a scalar multiple of the projection map onto
a single copy of the irreducible SU(N)q–module Vλ.
Theorem 6.3 ([2]) Let C be a framed knot coloured by the irreducible represen-
tation Vλ. Let S be the satellite knot C ∗Qλ with companion C and pattern Qλ.
Then
J(C; Vλ) = XN(S) .
The result also holds for links where each component coloured by Vλ is replaced
by its satellite, with pattern Qλ.
Idempotents of the Hecke algebra.
26
It is not diﬃcult to show that the elements Qλ form a linear basis for the
skein of the annulus, by expressing them in terms of Turaev’s basis, as discussed
in Sect. 2. There is no nice skein theory proof that the expression for QλQµ
in terms of this basis is identical to that for the decomposition of the tensor
product of the irreducible representations Vλ ⊗Vµ. It can, however, be proved
more circuitously that
QλQµ =
X
ν∈λµ
aλµνQν ,
where the aλµν are the Littlewood-Richardson coeﬃcients.
Theorem 6.3 has been used to calculate the quantum dimensions of represen-
tations of SU(N)q. The details are discussed in [1], where the following formula
is proved skein theoretically;
X (beλ) =
Y
(i,j)∈λ
sj−i(v−1sj−i −vsi−j)
(s −s−1)
.
Making the substitutions prescribed by Theorem 6.1, we obtain the formula for
the quantum dimension XN(Qλ), which was originally established by Reshetikhin
[18],
XN(Qλ) =
Y
(i,j)∈λ
[N + j −i]
[λi + λ∨
j −i −j + 1].
The classical dimension is given by the same formula but with integers in the
place of quantum integers.
References
[1] A. K. Aiston.
A skein theoretic proof of the hook formula for quantum
dimension. ArXiv:q-alg/9711019.
[2] A. K. Aiston.
Skein theoretic idempotents of Hecke algebras and quan-
tum group invariants.
PhD thesis,
University
of Liverpool,
1996.
https://livrepository.liverpool.ac.uk/7155/
[3] T. Deguchi,
Y. Akutsu,
and M. Wadati.
Exactly solvable mod-
els and new link polynomials. III. Two-variable topological invariants.
J. Phys. Soc. Japan, 57:757–776, 1988.
[4] T. Deguchi, M. Wadati, and Y. Akutsu.
Exactly solvable models and
new link polynomials. V. Yang-Baxter operator and braid-monoid algebra.
J. Phys. Soc. Japan, 57:1905–1923, 1988.
[5] R Dipper and G. D. James. Blocks and idempotents of Hecke algebras of
general linear groups. Proc. London Math. Soc., 54:57–82, 1987.
Idempotents of the Hecke algebra.
27
[6] E. A. Elrifai and H. R. Morton. Algorithms for positive braids. Quart. J.
Math. Oxford (2), 45:479–497, 1994.
[7] W. Fulton and J. Harris. Representation theory – a ﬁrst course. G.T.M.
Springer Verlag, 1991.
[8] A. Gyoja. A q-analogue of Young symmetriser. Osaka J. Math., 23:841–852,
1986.
[9] M. Jimbo. A q-analogue of U(gl(n + 1)), Hecke algebra and Yang Baxter
equation. Lett. Math. Phys., 11:247–252, 1986.
[10] H. F. Jones. Groups, representations and physics. Adams Hilger, 1990.
[11] V. F. R. Jones.
Hecke algebra representations of braid groups and link
polynomials. Ann. Math., 126:335–388, 1987.
[12] J. Katriel, B. Abdesselam, and A. Chakrabarti. The fundamental invariant
of the Hecke algebra Hn(q) characterizes the representations of Hn(q), Sn,
SUq(N) and SU(N). J. Math. Phys., 36:5139–5158, 1995.
[13] H. R. Morton. Invariants of links and 3-manifolds from skein theory and from
quantum groups. In M. Bozh¨uy¨uk, editor, Topics in knot theory. N.A.T.O.
A.S.I. series C 399, pages 107–156. Kluwer, 1993.
[14] H. R. Morton. Quantum invariants given by evaluation of knot polynomials.
J. Knot Theory Ramif., 2:195–209, 1993.
[15] H. R. Morton and A. K. Aiston. Young diagrams, the Homﬂy skein of the
annulus and unitary invariants. In S. Suzuki, editor, Knots 96, pages 31–45.
World Scientiﬁc, 1997.
[16] H. R. Morton and P. Traczyk. Knots and algebras. In E. Martin-Peinador
and A Rodez Usan, editors, Contribuciones Matematicas en homenaje al
profesor D. Antonio Plans Sanz de Bremond., pages 201–220. University of
Zaragoza, 1990.
[17] A. Ocneanu. A new polynomial invariant for knots: a combinatorial and
algebraic approach. preprint, MSRI, 1985.
[18] N. Y. Reshetikhin.
Quantized universal enveloping algebras, the Yang-
Baxter equation and invariants of links I and II. preprint, E–4–87 E–17–87,
LOMI, 1987.
[19] V. G. Turaev. The Conway and Kauﬀman modules of the solid torus with
an appendix on the operator invariants of tangles. LOMI preprints, E-6-88,
1988.
Idempotents of the Hecke algebra.
28
[20] V. G. Turaev. The Yang Baxter equation and invariants of links. Invent.
Math., 92:527–553, 1988.
[21] A. J. Wasserman. Coactions and Yang-Baxter equations for ergodic actions
and subfactors. London Math. Soc. Lecture Notes, 136:203–236, 1993.
[22] H. Wenzl. Hecke algebras of type An and subfactors. Invent. Math., 92:349–
383, 1988.
[23] H. Wenzl. Quantum groups and subfactors of type B, C and D. Commun.
Math. Phys., 133(2):383–432, 1990.
[24] H. Wenzl. Unitary braid representations. In proceedings of the RIMS Re-
search Project “Inﬁnite Analysis” 1991. Int. J. Modern Physics A, 7 Suppl.
1B:985–1006, 1992.
[25] H. Weyl.
The classical groups and their invariants and representations.
Princeton University Press, 1946.
[26] Y. Yokota. Skeins and quantum SU(N) invariants of 3-manifolds. Math.
Ann., 307:109–138, 1997.
. . .
. . .
m
( )
a λ l
i
a
-
σj
σ
b
-
j
µ
b
(j )
p
ω π
]
1] [N+2] [N+3]
[1]
[6]
[3]
[1]
[2
[4]
5
1
7
4
3
2 6
S
T
...
...
...
...
µ
b
(j )
p
( )
a λ l
i
π
ω
i
b
a
-
-
j
σ
σ
Q
Q
.
. .
.
1
2
ρ
ω
m
2
ρ
ω
aλ 1
aλ 2
λk
.  .  .
bλ2*
bλ*m
.  .  .
.  .  .
.  .  .
a
bλ 1*
ω π λ
2
2
ω ρ
k
1
ρ
ω
2
1
ρ
ω
ω ρ 11
