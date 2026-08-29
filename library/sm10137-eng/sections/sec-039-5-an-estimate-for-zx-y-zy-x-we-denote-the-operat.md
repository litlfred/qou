---
doc_id: sm10137-eng
doc_title: "Sbornik: Mathematics 215:12 1607–1632 Matematicheski˘ı Sbornik 215:12 30–55 Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel "
section_id: sec-039-5-an-estimate-for-zx-y-zy-x-we-denote-the-operat
section_title: "An estimate for Z(x, y) + Z(y, x). We denote the operator induced by this"
section_number: 5
pages: 19-23
source_pdf: sm10137_eng.pdf
source_sha256: afd51b0231f4dc41
doc_brief: "Sbornik: Mathematics 215:12 1607–1632 Matematicheski˘ı Sbornik 215:12 30–55 Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel S. M. Gorbunov — We"
---
kernel by eZ. Integration of the kernel by parts yields
eZ(x, y) = Z(x, y) + Z(y, x) = Aν
r
2
π
Z ∞
0
b0(t)
xyt
d
dt(sin(xt −ϕν) sin(yt −ϕν)) dt
= −Aν
r
2
π
b′(0)
xy sin2(ϕν)
−Aν
r
2
π
1
xy
Z ∞
0
d
dt
b0(t)
t

sin(xt −ϕν) sin(yt −ϕν) dt.
1626
S. M. Gorbunov
The first term induces the one-dimensional projector h1(x)⟨h2(y), −⟩L2 with trace
norm bounded by ∥h1∥L2∥h2∥L2. By Lemma 5, for the trace norm of the corres-
ponding operator on L2[R, ∞) we have |Aνb′(0)|/R ⩽|Aν|∥b∥˙B/R.
We apply Proposition 4 to the second term. This results in the estimate
∥χ[R,∞) eZχ[R,∞)∥J1 ⩽|Aν|∥b∥˙B
R
+ |Aν|
R
Z ∞
0

d
dt
b0(t)
t


 dt.
The integral over [0, 1] is estimated as follows in view of (7.19):
Z 1
0

d
dt
b0(t)
t


 dt ⩽∥b∥˙H2.
The integral over [1, ∞) is estimated using (7.16) and the Cauchy–Bunyakovsky–
Schwarz inequality:
Z ∞
1

d
dt
b0(t)
t


 dt ⩽
Z ∞
1
|b′(t)|
t
+ ∥b∥˙H1
t3/2

dt ⩽3∥b∥˙H1.
Therefore, we conclude that
∥χ[R,∞) eZχ[R,∞)∥J1 ⩽5|Aν|∥b∥˙B
R
.
This finishes the proof of Lemma 3.
§ 8. Proof of Theorems 1 and 2
Recall the Jacobi–Dodgson identity.
Proposition 7 ([23], Proposition 6.2.9). Let A be an invertible operator on a sep-
arable Hilbert space H and A −I ∈J1(H). Let P be an orthogonal projection in H
and Q = I −P . Then
det(PAP) = det(A) det(QA−1Q).
(8.1)
We use the following variation of this identity.
Corollary 2. Let P1 and P2 be two commuting orthogonal projections in a sepa-
rable Hilbert space H. Let Qi = I −Pi, i = 1, 2. Then
det(P1AP1)
det(Q1A−1Q1) =
det(P2AP2)
det(Q2A−1Q2),
(8.2)
if A is invertible, A −I ∈J2(H) and all Fredholm determinants are well defined.
Remark 3. It is not required that A −I ∈J1(H) in this statement.
Proof of Corollary 2. Let A = I + K, where K ∈J2(H).
We choose a joint
orthogonal basis {ei}i∈N of eigenvectors of P1 and P2. Let Rn be the orthogonal
projection onto span({ei}i∈1,...,n). We regard RnH as a separable Hilbert space.
Since the Pi and Qi commute with Rn, they remain orthogonal projections in RnH.
Rate of convergence in the central limit theorem
1627
Since K is compact, RnKRn →K in the operator norm. This implies that for
all sufficiently large n the operator I + RnKRn is invertible on RnH. Applying
Proposition 7 we have
det(RnP1AP1Rn)
det(Q1(RnARn)−1Q1) =
det(RnP2AP2Rn)
det(Q2(RnARn)−1Q2) = det(RnARn).
(8.3)
It remains to show that (RnARn)−1 −RnA−1Rn
J1(H)
−−−−→0 as n →∞. For the
above difference we have
(Rn + RnKRn)−1 −Rn(I + K)−1Rn
= (RnKRn)2(Rn + RnKRn)−1 −RnK2(I + K)−1Rn,
where (Rn + RnKRn)−1 →(I + K)−1 and Rn →I strongly, and (RnKRn)2 →K
and RnK2 →K2 in the trace norm since K ∈J2(H). Therefore, we have
lim
n→∞det(Qi(RnARn)−1Qi) = lim
n→∞det(RnQiA−1QiRn) = det(QiA−1Qi).
Equality (8.2) follows by taking limits in (8.3) as n →∞.
The corollary is proved.
Let us extend the definition (1.1) to all functions in L∞(R+). Recall that the
Hankel transform Hν on L2(R+) is defined by
Hνf(λ) =
Z ∞
0
√
λx Jν(λx)f(x) dx.
Similarly to the Fourier transform, it is an isometry of L1(R+)∩L2(R+) and extends
to L2(R+) by continuity. Also recall that H∗
ν = H−1
ν
= Hν. Now for b ∈L∞(R+)
we define the Bessel operator by
Bb = HνbHν.
(8.4)
This coincides with the definition (1.1) for b ∈L1(R+)∩L∞(R+), but from (8.4) it is
clear that B: f →Bf, L∞(R+) →B(L2(R+)) is a Banach algebra homomorphism
and, in particular, B−1
eb = Be−b.
Next we want to show that for b ∈B the operator Bb −Wb is Hilbert–Schmidt.
By Lemma 3 we have χ[1,∞)(Bb −Wb)χ[1,∞) ∈J1 and χ[0,1](Bb −Wb)χ[0,1] ∈J1 by
Theorem 4. The following statement, completing the argument, can be verified
directly.
Lemma 6 (see [3], Lemmas 3.1 and 3.2). For b ∈H1(R+) ∩L1(R+) the operators
χ[0,1]Bb and χ[0,1]Wb are Hilbert–Schmidt.
Proof of Lemma 2. For arbitrary R1, R2 > 0 we set P1 = χ[0,R1], P2 = χ[0,R2]
and A = We−b+BebWe−b−. By the first statement of Proposition 3 and the defi-
nition (8.4)
A is invertible and its inverse is Web−Be−bWeb+. In the notation of
Corollary 2 we also have Q1 = χ[R1,∞) and Q2 = χ[R2,∞). Using the second and
third assertions of Proposition 3 we can write
QiA−1Qi = χ[Ri,∞) + χ[Ri,∞)Web−χ[Ri,∞)Re−bχ[Ri,∞)Web+χ[Ri,∞),
(8.5)
1628
S. M. Gorbunov
where Rb = Bb−Wb. Hence by the assumptions and since Re−b is Hilbert–Schmidt,
we can apply Corollary 2 to obtain
det(χ[0,R1]We−b+BebWe−b−χ[0,R1])
det(χ[R1,∞)Web−Be−bWeb+χ[R1,∞)) = det(χ[0,R2]We−b+BebWe−b−χ[0,R2])
det(χ[R2,∞)Web−Be−bWeb+χ[R2,∞)) = Z(b),
(8.6)
where all Fredholm determinants are well defined.
Lemma 2 is proved.
Recall an asymptotic result due to Basor and Ehrhardt.
Theorem 6 ([3], Theorem 1.1). Suppose the function b ∈L1(R+) ∩L∞(R+) sat-
isfies the following conditions:
• b is continuous and piecewise C2-smooth on [0, ∞);
• limt→∞b(t) = 0;
• (1 + t)−1/2b′(t) ∈L1(R+), b′′(t) ∈L1(R+).
Then the following asymptotic formula holds as R →∞:
det(χ[0,R]Bebχ[0,R]) = exp(RcB
1 (b) + cB
2 (b) + cB
3 (b))QB
R(b),
QB
R(b) →1,
(8.7)
where the cB
i (b) are as in Theorem 1.
By Lemma 5 the functions in B satisfy the assumptions of Theorem 5.
The following lemma shows that for each b ∈B the function e−b satisfies the
assumption of Lemma 3.
Lemma 7. Let b ∈B. Then eb −1 ∈L1 ∩L∞. There exists a constant C such
that for any b ∈B we have
∥eb∥˙B ⩽C exp(∥b∥L∞)(1 + ∥xb′(x)∥2
L∞+ ∥b∥2
˙B)∥b∥˙B.
Proof. The first assertion follows directly from L∞being a Banach algebra with
pointwise multiplication and the inequality
∥eb −1∥L1 ⩽∥b∥L1

eb −1
b

L∞
.
For an estimate of the ˙B-seminorm, we have by definition
∥eb∥˙H1 ⩽exp(∥b∥L∞)∥b∥˙H1.
The third derivative of eb is
(eb)′′′ = eb(b′′′ + (b′)3 + 3b′b′′).
Observe that
∥b′∥L∞⩽∥λbb(λ)∥L1 ⩽∥b∥˙H1 + ∥b∥˙H2.
This yields the estimate
∥eb∥˙H3 ⩽exp(∥b∥L∞)(∥b∥˙H3 + ∥b∥2
˙B∥b∥˙H1 + 3∥b∥˙B∥b∥˙H2).
Rate of convergence in the central limit theorem
1629
Next we write out the second derivative of xeb(x):
(xeb(x))′′ = eb(x)((xb(x))′′ + x(b′(x))2).
Therefore,
∥xeb(x)∥˙H2 ⩽exp(∥b∥L∞)(∥xb(x)∥˙H2 + ∥xb′(x)∥L∞∥b∥˙H1).
Finally, the third derivative of x2eb(x) is as follows:
(x2eb(x))′′′ = eb(x)(6x(b′(x))2 + 3x2b′(x)b′′(x) + (x2b(x))′′′ + x2(b′(x))3).
This implies that
∥x2eb(x)∥˙H3 ⩽exp(∥b∥L∞)(3∥xb′(x)∥L∞∥xb(x)∥˙H2
+ ∥x2b(x)∥˙H3 + ∥xb′(x)∥2
L∞∥b∥˙H1).
The lemma is proved.
Proof of Theorem 1. Recall the inequality
| det(I + K) −1| ⩽∥K∥J1 exp(∥K∥J1).
Also recall that for any trace-class operator A and bounded B we have ∥AB∥J1 ⩽
∥A∥J1∥B∥. By the definition of Wiener–Hopf operators ∥Wb∥= ∥b∥L∞. These facts
and Lemmas 3 and 7, in combination with the expression (8.5), prove estimate (2.2).
By the above argument the denominator in (3.5) approaches 1. From Lemma 1
and Theorem 6, for the numerator in (3.5) we have
det(χ[0,R]We−b+BebWe−b−χ[0,R]) →exp(cB
2 (b) + cB
