---
doc_id: aif-2009-59-1-347-0
doc_title: "On q-summation and confluence"
section_id: sec-004-12-confluence
section_title: "Confluence"
section_number: 1.2
pages: 10-14
source_pdf: AIF_2009__59_1_347_0.pdf
source_sha256: 35b8422990e24888
toc_source: outline
---
355
In the present article, we will denote by ep(x) and eq(x) the functions
obtained by replacing n! by [n]!
p and [n]!
q, respectively, in the Tarlor ex-
pansion at zero of the exponential function ex. Since Euler, one knows that
(q(1 −q)x; q)∞coincides with the analytic function at 0:
ep(−qx) :=
X
n⩾0
(−qx)n
[n]!p
,
so that Equation (1.4) takes the more familiar shape:
Eq(x) =
Z
x
1−q
0
ep(−qt/x)
t + 1
dqt,
that so closely reminds the Euler integral:
E(x) =
Z +∞
0
e−t
x
t + 1dt.
The analytic function E(x) can be continued to C∖R−, it is asymptotic at
zero to the Euler series P
n⩾0(−1)nn!xn+1 and is solution of the diﬀerential
equation x2y′ + y = x. In the following subsection we are going to study
the behavior of Eq(x) with respect to E(x) when q →1−.
1.2. Conﬂuence
Let us denote by E(x) the analytic continuation to C \ (−∞, 0] of the
Borel sum of ˆE(x) in the direction R+:
E(x) =
Z +∞
0
e−t
x
t + 1dt,
ℜx > 0,
and by log x the analytic continuation to C \ (−∞, 0] of log x.
Theorem 1.4. — If q →1−, the analytic continuation of Eq(x) con-
verges to E(x) for any x ∈C ∖(−∞, 0] and the convergence is uniform on
the compacts of C ∖(−∞, 0].
The proof of the theorem above relies on the following result (cf. §B.2
below for the proof):
Proposition 1.5. — The following identity holds, for any x ∈C∗\q−N:
(1.5)
X
n⩾0
(q; q)nxn+1 = −

−qxθ′(−qx)
θ(−qx) + 1 + A(q)
  q
x; q

∞
+
X
n⩾1
an
(q; q)n
qn(n+1)/2

−1
x
n
,
TOME 59 (2009), FASCICULE 1
356
Lucia DI VIZIO & Changgui ZHANG
where
θ(x) = θ(q, x) =
X
n∈Z
qn(n−1)/2xn,
A(q) =
X
n⩾0
qn+1
qn+1 −1
and
an+1 =
n
X
k=0
1
qk+1 −1,
n ⩾0.
Our strategy for the proof of Theorem 1.4 is based on the fact that (1.5)
is a “deformation” of the following classical formula:
(1.6)
E(x) = (log x −γ)e
1
x +
X
n⩾1
P
1⩽k⩽n
1
k
n!
 1
x
n
,
where γ is the Euler constant:
γ = lim
n→∞
 n
X
k=1
1
k −ln(n)
!
.
In fact, taking the logarithmic derivative of the functional equation θ(x) =
xθ(qx), one proves that the meromorphic function (q −1)z θ′(−z)
θ(−z) veriﬁes
the equation y(qx) −y(x) = q −1 or equivalently dqy(x) = 1
x, therefore it
“deforms” the logarithm. On the other hand we have:
(q −1)A(q) =
X
n⩾0
qn+1
[n + 1]q
,
whose link to the Euler constant is intuitive. The proof of Theorem 1.4 is
a formalization of these ideas.
Proof of Theorem 1.4. — If we perform the variable change x →
x
q−1 in
(1.6) and remember that
ep (q/x) =
−q(1 −q)
x
; q

∞
,
then we obtain the expression
(1.7)
Eq(x) =(1 −q)

ℓq
 qx
q −1

+ 1 + A(q)

ep
 q
x

+
X
n⩾1
(q −1)an
[n]!q
qn(n−1)/2  q
x
n
,
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE
357
in which we have set
ℓq(x) := −xθ′(−x)
θ(−x) .
We are going to analyze (1.7) term by term.
First of all the constant A(q) can be expressed in terms of the logarithmic
derivative Ψq(x) =
Γ′
q(x)
Γq(x) (see (B.5), where Ω(q) = A(q)):
(1.8)
A(q) = −1
ln q (Ψq(1) + ln(1 −q)) .
The following result says how the q-logarithm ℓq tends to the usual log-
arithm.
□
Lemma 1.6. — Let ϵ ∈(0, π) and consider the sector Vϵ = {x ∈C∗:
| arg x| ⩽π−ϵ}. Then the following uniform estimate holds for any (q, x) ∈
(0, 1) × Vϵ:
(1.9)
| ln q ℓq(−√qx) + log x| ⩽
4πe
2π
ln q ϵ
(1 −e
4π2
ln q )(1 −e
2π
ln q ϵ)
.
Proof. — The lemma is a consequence of the following classical func-
tional relation for θ(x) (cf. [19, §21.51, p. 475], where ϑ3(z|τ) = θ(√qe2πiz)
with q = e2πiτ):
(1.10)
θ(√qx) =
s
2π
ln(1/q)e−log2 x
2 ln q θ∗(√q∗x∗),
where we have written
x∗= e−2πi
ln q log x,
q∗= e
4π2
ln q
and denoted by θ∗the Theta function obtained by replacing q by q∗. In-
deed, if we take the logarithmic derivative w.r.t. the variable x in (1.10)
and observe that ln q xdx∗= −2πix∗dx, then we obtain the following ex-
pression:
(1.11)
ln q ℓq(−√qx) + log x = −2πiℓq∗(−√q∗x∗),
so that we only need to examine ℓq∗(−√q∗x∗). The key point of the proof
is the fact that q∗→0+ when q →1−.
For ϵ ∈(0, π) we set:
rϵ = e
2π
ln q ϵ ∈(√q∗, 1),
V ∗
ϵ = {x ∈C :
√q∗
rϵ
⩽|x| ⩽
rϵ
√q∗}.
It’s obvious that for any x ∈Vϵ, we have x∗∈V ∗
ϵ , so that
(1.12)
q∗< q∗
rϵ
⩽|√q∗x∗| ⩽rϵ < 1.
TOME 59 (2009), FASCICULE 1
358
Lucia DI VIZIO & Changgui ZHANG
On the other hand, the following identity, consequence of the Jacobi triple
product,
X θ∗′(X)
θ∗(X) =
X
n⩾0

q∗nX
1 + q∗nX −
q∗n+1
X + q∗n+1

,
combined with the inequalities:
|1 + Xq∗n| ⩾1 −|X|,
|X + q∗n+1| ⩾|X| −q∗, for q∗< |X| < 1,
implies that:
(1.13)
sup
q∗
rϵ ⩽|X|⩽rϵ
|ℓq∗(−X)| ⩽
rϵ
1 −q∗
1
1 −rϵ
+
q∗
1 −q∗
1
q∗
rϵ −q∗⩽
2rϵ
(1 −rϵ)(1 −qϵ).
We get (1.9) and hence Lemma 1.6 by combing (1.11) and (1.13).
□
End of the proof of Theorem 1.4. — By replacing x by √qx/(1 −q) in
Lemma 1.6, we have:
ℓq
 qx
q −1

= −1
ln q

log x + ln
 √q
1 −q

+ O

e2πϵ/ ln q
.
Therefore, we deduce from (1.8) that:
(1.14)
ℓq
 qx
q −1

+ 1 + A(q) = −1
ln q

log x + Ψq(1) + ln q
2
+ O(e2πϵ/ ln q)

,
where Ψq denotes the logarithmic derivative of Γq. As q →1−, the function
Γq(x) converges uniformly to Γ(x) on any compact of C\(−N) (cf. [22]), so
Ψq(x) converges to the logarithmic derivative Ψ(x) of the Γ function. From
the classical relation Ψ(1) = −γ, one deduces that Ψq(1) = −γ + o(1). In
other words, (1.14) implies the following estimate:
(1.15)
(q −1)

ℓq
 qx
q −1

+ 1 + A(q)

= −log x + γ + o(1)
where o(1) denotes a quantity converging to 0 as q →1−, uniformly on any
compact of C \ (−∞, 0].
Notice that the exponential function e
1
x is the uniform limit on any
domain {|x| > R > 0} of the p-exponential ep(q/x), since
ep
 1
x

=
X
n⩾0
qn(n−1)/2
[n]!q
 q
x
n
.
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE
359
In the same time, the dominated convergence Theorem implies that
X
n⩾1
(q −1)anqn(n−1)/2
[n]!q
 q
x
n
→
X
n⩾1
Pn
k=1
1
k
n!
 1
x
n
,
when q →1−, uniformly for |x| > R > 0. We conclude combining (1.7)
with (1.15).
□
2. Conﬂuence of the convergent q-analogue of
Borel-Laplace summation
Let q be a real number in the open interval (0, 1). We want to general-
ize, under convenient reasonable assumptions, the results of the previous
section.
