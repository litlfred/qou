---
doc_id: arxiv-math-9805023v1
doc_title: "q-Laguerre polynomials and big q-Bessel functions and their orthogonality relations"
section_id: sec-005-6-proof-of-the-dual-orthogonality-relations
section_title: "Proof of the dual orthogonality relations."
section_number: 6
pages: 13-20
source_pdf: 9805023v1.pdf
source_sha256: ea8758b2a2bf9d85
toc_source: inferred
doc_brief: "q-Laguerre polynomials and big q-Bessel functions and their orthogonality relations — The q-Laguerre polynomials correspond to an indetermined moment problem."
---
In this section we prove the dual orthogonality relations of Corollary 4.3 by using a
rigorous limit transition from the big q-Jacobi polynomials to the q-Bessel functions under
consideration, which we will call now big q-Bessel functions. The orthogonality relations
for the big q-Jacobi polynomials tend to the dual orthogonality relations given in Corollary
4.3. This then gives, together with the analytic proofs of the previous section a complete
alternative analytic proof of Theorem 4.1.
For α > −1, c > 0, k ∈Z, x ∈R put
J c
α,k(x; q) := 1ϕ1
 x−1
qα+1 ; q, −c−1xqk+α+2

(6.1)
= (−c−1qk+1; q)∞2ϕ1
qα+1x, 0
qα+1
; q, −c−1qk+1

.
(6.2)
13
Here we used for the second identity the tranformation
1ϕ1
a
c ; q, x

= (ax/c; q)∞2ϕ1
c/a, 0
c
; q, ax/c

,
which is a limit case of Heine’s transformation formula [7, (1.4.6)]. Then formulas (4.1)
and (4.2) can be rewritten as
(6.3)
L(α)
n (c−1qk+1; q) = (qα+1; q)n
(q; q)n
J c
α,k(qn; q)
(n ∈Z≥0),
respectively
(6.4)
M (α;c−1)
p
(c−1qk+1; q) =
(qα+1; q)∞
(q, −c−1qα+1; q)∞
J c
α,k(−cqp−α; q)
(p ∈Z).
The (dual) orthogonality relations in Corollary 4.3 can be rewritten by substitution
of (4.5), (6.3) and (6.1). We obtain for k, l ∈Z:
(6.5)
∞
X
n=0
(J c
α,kJ c
α,l)(qn; q) qn (qn+1; q)∞
(qn+α+1; q)∞
+
∞
X
p=−∞
(J c
α,kJ c
α,l)(−cqp−α−1; q) cqp−α−1 (−cqp−α; q)∞
(−cqp; q)∞
= δk,lq−k(α+1)
(q; q)2
∞
(qα+1; q)2∞
(−cq−α−1, −qα+2c−1, −qk+1c−1; q)∞
(−c, −qc−1; q)∞
.
We will show that the orthogonality relations (6.5) can be rigorously obtained as a limit
case of the orthogonality relations for big q-Jacobi polynomials.
Let 0 < a < q−1, b > −q−1, c > 0. Big q-Jacobi polynomials are deﬁned by
(6.6)
Pk(x; a, b, −c; q) := 3ϕ2
q−k, abqk+1, x
aq, −cq
; q, q

(x ∈R, k ∈Z≥0).
Formally we have
(6.7)
lim
r→∞Pr−k(qα+1x; qα, b, −cq−r−1; q) =
1
(−c−1qk+1; q)∞
Jk(x; α, c; q).
(Substitute (6.6) and (6.2) and take termwise limits in the 3ϕ2.) The orthogonality rela-
tions for big q-Jacobi polynomials are given by
(6.8)
Z aq
−cq
(PkPl)(x; a, b, −c; q) (x/a, −x/c; q)∞
(x, −bx/c; q)∞
dqx
= δk,l M
1 −abq
1 −abq2k+1
(q, bq, −abq/c; q)k
(abq, aq, −cq; q)k
(acq2)k qk(k−1)/2,
14
where
M := (1 −q) aq (q, −c/a, −aq/c, abq2; q)∞
(aq, bq, −cq, −abq/c; q)∞
,
see [7, (7.3.12)–(7.3.14)]. (Note the error on the right-hand side of [7, (7.3.13)]: the factor
(−ac)n must be replaced by (−acq2)−n.)
Formally the orthogonality relations (6.5) can be obtained as a limit case of the or-
thogonality relations (6.8) for big q-Jacobi polynomials. In (6.8) just replace k by r −k,
l by r −l, c by cqr−1, and a by qα, and let r →∞. Because of these limit results we call
the functions x 7→Jk(x; α, c; q) big q-Besel functions.
For b = 0 we can transform the right-hand side of (6.6) by the transformation formula
[7, Exercise 1.15(i)]:
(6.9)
ePk(x; a, 0, −c; q) := (−c−1q−k; q)k Pk(x; a, 0, −c; q) = 2ϕ1
q−k, aq/x
aq
; q, −x/c

.
Formula (6.7) for b = 0 can also be obtained as a formal termwise limit by substituting
(6.9) and (6.1) and by taking termwise limits in the 2ϕ1.
Fix α > −1, c > 0, and let r ∈Z≥0. From (6.8) we get orthogonality relations for the
functions x 7→ePr−k(qα+1x; qα, 0, −cq−r−1; q)
(k = r, r −1, . . .):
(6.10)
∞
X
n=0
( ePr−k ePr−l)(qn+α+1; qα, 0, −cq−r−1; q) qn (qn+1, −c−1qα+n+r+2; q)∞
(qα+n+1; q)∞
+
∞
X
p=−r
( ePr−k ePr−l)(−cqp; qα, 0, −cq−r−1; q) cqp−α−1 (−cqp−α, qp+r+1; q)∞
(−cqp; q)∞
= δk,l
(q, −cq−r−α−1, −qα+r+2/c; q)∞
(qα+1, −cq−r; q)∞
(q, −c−1qk+1; q)r−k
(qα+1; q)r−k
q(α+1)(r−k).
Here k, l = r, r −1, . . . . Note that the orthogonality relations (6.10) and (6.5) have the
same structure. We want to show that we can take a rigorous limit for r →∞of (6.10)
which yields (6.5) preserving this structure.
Proposition 6.1. Fix α > −1, c > 0, k ∈Z. Then, for each x ∈R we have the pointwise
limit
(6.11)
lim
r→∞
ePr−k(qα+1x; qα, 0, −cq−r−1; q) = J c
α,k(x; q).
Furthermore, if M > 0 then
(6.12)

 ePr−k(qα+1x; qα, 0, −cq−r−1; q)

J c
α,k(x; q)

)
≤1φ1
−M −1
qα+1 ; q, −qα+k+2M
c

for |x| ≤M and r = k, k + 1, . . . .
15
Proof. Write
ePr−k(qα+1x; qα, 0, −cq−r−1; q) = 2φ1
q−r+k, x−1
qα+1
; q, −qα+r+2x
c

=
∞
X
j=0
tr(j, x)
with
tr(j, x) := (q−r+k, x−1; q)j
(qα+1, q; q)j
(−c−1qα+r+2x)j
(vanishing if j > r −k).
Also write
J c
α,k(x; q) = 1φ1
 x−1
qα+1 ; q, −c−1xqk+α+2

=
∞
X
j=0
t(j, x)
with
t(j, x) :=
(x−1; q)j
(qα+1, q; q)j
q
1
2 j(j−1) (c−1xqk+α+2)j.
Then
(6.13)
lim
r→∞tr(j, x) = t(j, x)
and
(6.14)
|tr(j, x)| ≤T(j, M)
for r ≥k and |x| ≤M,
where
T(j, M) := (−M −1; q)j
(qα+1, q; q)j
q
1
2 j(j−1) (c−1Mqk+α+2)j
and
∞
X
j=0
T(j, M) = 1φ1
−M −1
qα+1 ; q, −c−1Mqk+α+2

< ∞.
Then the limit (6.11) follows from (6.13) and (6.14) by dominated convergence.
For the proof of (6.14) we have used that, for i = 0, 1, . . . , r −k −1 and |x| ≤M:

(1 −q−r+k+i)(1 −x−1qi)qr−kx

 =

(qi −qr−k)(x −qi)

≤qi(M + qi) = (1 + M −1qi)qiM.
□
For ePr−k(−cqp; qα, 0, −cq−r−1; q) as −r ≤p ≤−k, r →∞we need a more reﬁned
estimate in order to be able to take limits in (6.10).
16
Proposition 6.2. Fix α > −1, c > 0, k ∈Z, Let r ∈{k, k + 1, . . .}. Then, for p ∈
{−k, −k −1, . . .} we have
(6.15)
ePr−k(−cqp; qα, 0, −cq−r−1; q) = (q; q)r−k
(−cqp; q)−k−p
(qα+1, q; q)−k−p
(−c−1qα−p+1)−k−p
× 2φ2

q−r−p, −cq−k
qα+1−k−p, q−k−p+1 ; q, −c−1qα−k−p+r+2

and
(6.16)
J c
α,k(−cqp−α−1; α, c; q) = (q; q)∞
(−cqp; q)−p−k
(qα+1; q; q)−p−k
(−c−1q−p+α+1)−p−k
× 1φ2

−cq−k
q−p−k+1, qα+1−p−k ; q, −c−1q−2p−k+α+2

= lim
r→∞
ePr−k(−cqp; qα, 0, −cq−r−1; q).
Furthermore,
(6.17)

 ePr−k(−cqp; qα, 0, −cq−r−1; q)

J c
α,k(−cqp−α−1; α, c; q)

)
≤
(−cqp; q)−k−p
(qα+1, q; q)−k−p
(c−1qα−p+1)−k−p
× 1φ2
 −cq−k
qα+1, q ; q, c−1qk+α+2

for r ∈{k, k + 1, . . .} and p ∈{−k, −k −1, . . .}.
Proof. By Jackson’s tranformation formula [7, (1.5.4)] we have
2φ1
a, b
c ; q, z

= (az; q)∞
(z; q)∞
2φ2
a, c/b
c, az ; q, bz

=
1
(z; q)∞
∞
X
j=0
(a, c/b; q)j (azqj; q)∞
(c, q; q)j
q
1
2 j(j−1)(−bz)j.
Put z := q−s+1a−1, where s ∈Z≥0. Then (azqj; q)∞= (q−s+j+1; q)∞, so in the last sum
the summation will start at j = s. Replace the summation index j by j + s and write the
resulting sum again as a 2φ2. Then we obtain for s ∈Z≥0:
2φ1
a, b
c ; q, a−1q−s+1

= (q; q)∞(c/b; q)s bs
(qa−1; q)∞(c; q)s
2φ2
aqs, cqs/b
cqs, qs+1 ; q, qa−1b

.
This yields (6.15) (here s = −k −p).
The ﬁrst identity in (6.16) can be derived in a similar way by starting with
1φ1
a
c ; q, z

=
1
(c; q)∞
∞
X
j=0
(az/c; q)j (qjz; q)∞
(q; q)j
q
1
2 j(j−1) (−c)j
17
(this is (3.5) with the right-hand side expanded) and then putting z := q−s+1 (s ∈Z≥0).
Expand the right-hand side of (6.15). So
ePr−k(−cqp; qα, 0, −cq−r−1; q) =
∞
X
j=0
tr(j; p)
with
tr(j, p) := (q; q)r−k
(−cqp; q)−k−p
(qα+1, q; q)−k−p
(−c−1qα−p+1)−k−p
×
(q−r−p, −cq−k; q)j
(qα+1−k−p, q−k−p+1, q; q)j
q
1
2 j(j−1) (c−1qα−k−p+r+2)j
(vanishing if j > r + p).
Then
(6.18)
|tr(j, p)| ≤T(j, p)
for r ∈{k, k + 1, . . .} and p ∈{−k, −k −1, . . .},
where
T(j, p) :=
(−cqp; q)−k−p
(qα+1, q; q)−k−p
(c−1qα−p+1)−k−p
(−cq−k; q)j
(qα+1, q, q; q)j
qj(j−1) (c−1qk+α+2)j
and P∞
j=0 T(j, p) equals the right-hand side of (6.17).
For the proof of (6.18) we have used that, for i = 0, 1, . . . , r + p −1,

(1 −q−r−p+i)qr−p−k

 =

(qi −qr+p)q−2p−k

 ≤qiqk.
For ﬁxed p, the limit formula in (6.16) follows from (6.11), but it follows also by
taking a termwise limit for r →∞on the right-hand side of (6.15) and by using dominated
convergence in view of (6.18).
□
Proof of (6.5).
Suppose k ≥l (without loss of generality). As r →∞, the right-hand
side of (6.10) tends to the right-hand side of (6.5), and each term on the left-hand side of
(6.10) tends to the corresponding term on the left-hand side of (6.5) (because of (6.11)).
We will show that the left-hand side of (6.10) tends rigorously to the left-hand side of (6.5)
by splitting up the left-hand side of (6.10) as
∞
X
n=0
+
∞
X
p=−l+1
+
l
X
p=−k+1
+
−k
X
p=−∞
,
and by using dominated convergence for each of the three inﬁnite sums.
As for the ﬁrst sum, by (6.12) the nth term is bounded in absolute value by Cqn,
where C > 0 and independent of n. Similarly, the pth term in the second sum is bounded
in absolute value by Cqp.
18
By (6.17), the pth term in the fourth sum is bounded in absolute value by
C (−cqp; q)−k−p
(qα+1, q; q)−k−p
(−cqp; q)−l−p
(qα+1, q; q)−l−p
(c−1qα−p+1)−k−l−2pqp (−cqp−α; q)∞
(−cqp; q)∞
≤A qp2 Bp,
where A, B, C > 0 and independent of p.
□
Remark. As we said in the Introduction the limit transition (6.7) from big q-Jacobi poly-
nomials to big q-Bessel functions is inspired by what happens at a quantum group level.
The regular representation of the quantum group SUq(2) on Podle´s’ quantum spheres
naturally decomposes into irreducibles, generated by suitable spherical functions which
turn out to depend on a single variable. Such functions can thus be identiﬁed with ordinary
big q-Jacobi polynomials, see [22].
In the limit transition from SUq(2) to the Euclidean quantum group Eq(2), quantum
spheres are replaced by quantum hyperboloids, i.e., algebras in two generators z and ¯z
such that z¯z = q2¯zz + 1 −q2. The corresponding regular representation decomposes into
irreducibles, each of which has an ∞-dimensional basis consisting of certain formal power
series in 1 −¯zz, see [4]. This makes it possible to identify such power series with ordinary
functions, and more precisely with q-Bessel functions of the form J c
α,k(x; q).
More precisely, the paper [4] gives in (4.9) the basis elements of the irreducible rep-
resentation space as explicit formal power series J(q)
r .
After the substitution ¯zjzj =
(1 −¯zz; q−2)j (see their Remark (4.10) (ii)) one can identify the series J(q)
r
for E = −q2k
with J q2/(q2−1)2
r,k
(1 −¯zz; q2) as deﬁned by (6.1).
References
1. N.I. Akhiezer, The Classical Moment Problem and Some Related Questions in Analysis, Hafner, 1965.
2. J.M. Berezanski˘ı, Expansions in Eigenfunctions of Selfadjoint Operators, Transl. Math. Monographs
17, Amer. Math. Soc., 1968.
3. C. Berg, On some indeterminate moment problems for measures on a geometric progression, preprint
(1997).
4. F. Bonechi, N. Ciccoli, R. Giachetti, E. Sorace and M. Tarlini, Free q-Schr¨odinger equation from
quantum homogeneous spaces of the 2-dim Euclidean quantum group, Comm. Math. Phys. 175 (1996),
161–176.
5. Y. Cheng, M.E.H. Ismail and K.A. Muttalib, Asymptotics of basic Bessel functions and q-Laguerre
polynomials, J. Comp. Appl. Math. 54 (1994), 263–272.
6. N. Dunford and J.T. Schwartz, Linear Operators II: Spectral Theory, Interscience, 1963.
7. G. Gasper and M. Rahman, Basic Hypergeometric Series, Cambridge Univ. Press, 1990.
8. M.E.H. Ismail, The zeros of basic Bessel functions, the functions Jν+ax(x), and associated orthogonal
polynomials, J. Math. Anal. Appl. 86 (1982), 1–19.
9. M.E.H. Ismail, D.R. Masson and S.K. Suslov, The q-Bessel function on a q-quadratic grid, preprint
(1996).
10. M.E.H. Ismail and M. Rahman, The q-Laguerre polynomials and related moment problems, J. Math.
Anal. Appl. 218 (1998), 155–174.
11. T. Kakehi, Eigenfunction expansion associated with the Casimir operator on the quantum group
SUq(1, 1), Duke Math. J. 80 (1995), 535–573.
12. T. Kakehi, T. Masuda and K. Ueno, Spectral analysis of a q-diﬀerence operator which arises from the
quantum SU(1, 1) group, J. Operator Theory 33 (1995), 159–196.
19
13. H.T. Koelink, A basic analogue of Graf’s addition formula and related formulas, Integral Transforms
and Special Functions 1 (1993), 165–182.
14.
, The quantum group of plane motions and the Hahn-Exton q-Bessel function, Duke Math. J.
76 (1994), 483–508.
15.
, The quantum group of plane motions and basic Bessel functions, Indag. Mathem. N.S. 6
(1995), 197–211.
16. H.T. Koelink and J. Verding, Spectral analysis and the Haar functional on the quantum SU(2) group,
Comm. Math. Phys. 177 (1996), 399–415.
17. T.H. Koornwinder, Jacobi functions and analysis on noncompact semisimple Lie groups, Special Func-
tions: Group Theoretical Aspects and Applications (R.A. Askey, T.H. Koornwinder, W. Schempp,
eds.), Reidel, 1984, pp. 1–85.
18. T.H. Koornwinder and R.F. Swarttouw, On q-analogues of the Fourier and Hankel transforms, Trans.
Amer. Math. Soc. 333 (1992), 445–461.
19. D.R. Masson and J. Repka, Spectral theory of Jacobi matrices in ℓ2(Z) and the su(1, 1) Lie algebra,
SIAM J. Math. Anal. 22 (1991), 1131–1146.
20. T. Masuda, K. Mimachi, Y. Nakagami, M. Noumi, Y. Saburi and K. Ueno, Unitary representations
of the quantum group SUq(1, 1): II—Matrix elements of unitary representations and the basic hyper-
geometric functions, Lett. Math. Phys. 19 (1990), 195–204.
21. D.S. Moak, The q-analogue of the Laguerre polynomials, J. Math. Anal. Appl. 81 (1981), 20–47.
22. M. Noumi and K. Mimachi, Quantum 2-spheres and big q-Jacobi polynomials, Comm. Math. Phys.
128 (1990), 521–531.
23. L.L. Vaksman and L.I. Korogodski˘ı, An algebra of bounded functions on the quantum group of the
motions of the plane and q-analogues of Bessel functions, Soviet Math. Dokl. 9 (1989), 173-177.
Dipartimento di Matematica, Universit`a di Perugia, Via Vanvitelli 1, 06123 Perugia,
Italy
E-mail address: ciccoli@dipmat.unipg.it
Korteweg-de Vries Instituut, Universiteit van Amsterdam, Plantage Muidergracht 24,
1018 TV Amsterdam, The Netherlands
E-mail address: koelink@wins.uva.nl
thk@wins.uva.nl
20
