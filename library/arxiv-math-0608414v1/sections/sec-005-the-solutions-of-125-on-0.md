---
doc_id: arxiv-math-0608414v1
doc_title: "Exponential Asymptotics, Transseries, and Generalized Borel Summation for Analytic, Nonlinear, Rank-One Systems of Ordinary Differential Equations"
section_id: sec-005-the-solutions-of-125-on-0
section_title: "The solutions of (1.25) on [0,)"
section_number: null
pages: 28-30
source_pdf: 0608414v1.pdf
source_sha256: bd9a8d48a6d66945
toc_source: outline
doc_brief: "Exponential Asymptotics, Transseries, and Generalized Borel Summation for Analytic, Nonlinear, Rank-One Systems of Ordinary Differential Equations — For analytic nonlinear systems of ordinary"
---
In this section we show that the leading asymptotic behavior of Yp as p →
1+ determines a unique solution of (1.25) in L1
loc(R+).
Furthermore, any
L1
loc solution of (1.25) is exponentially bounded at inﬁnity and thus Laplace
transformable. We also study some properties of these solutions and of their
Laplace transforms.
Let H be a solution of (1.25) on an interval [0, 1 + ǫ], which we extend to
R+ letting H(p) = 0 for p > 1 + ǫ. For a large enough b, deﬁne
SH := {f ∈L1
loc([0, ∞)) : f(p) = H(p) on [0, 1 + ǫ]}
(2.55)
and
S0 := {f ∈L1
loc([0, ∞)) : f(p) = 0 on [0, 1 + ǫ]}
(2.56)
We extend H to R+ by putting H(p) = 0 for p > 1 + ǫ; for p ≥1 + ǫ (1.25)
reads:
−p(H + h) = F0 −ˆΛ(H + h) −ˆB
Z p
0
(H + h)(s)ds + N (H + h)
(2.57)
with h ∈S0, or
h = −H + (ˆΛ −p)−1

F0 −ˆB
Z p
0
(H + h)(s)ds + N (H + h)

:= M(h)
(2.58)
For small φ0 > 0 and 0 ≤ρ1 < ρ2 ≤∞, consider the truncated sectors
S±
(ρ1,ρ2) := {z : z = ρe±iφ, ρ1 < ρ < ρ2; 0 ≤φ < φ0}
(2.59)
and the spaces of functions analytic in S±
(ρ1,ρ2) and continuous in its closure:
T ±
ρ1,ρ2 =
n
f : f ∈C(S(ρ1,ρ2)); f analytic in S±
(ρ1,ρ2)
o
(2.60)
which are Banach spaces with respect to ∥∥u on compact subsets of S(ρ1,ρ2).
28
Proposition 26 i) Given H, the equation (2.58) has a unique solution in
L1
loc[1 + ǫ, ∞). For large b, this solution is in L1
b([1 + ǫ, ∞)) and thus Laplace
transformable.
ii) Let Y0 be the solution deﬁned in Proposition 6. Then
Y±
0 (p) := lim
φ→±0 Y0(peiφ) ∈C(R+\{1}) ∩L1
loc(R+)
(2.61)
(and the limit exists pointwise on R+\{1} and in L1
loc(R+).)
Furthermore, Y±
0 are particular solutions of (1.25) and
Y±
0 (p)
=
(1 −p)β−1a±(p) + a±
1 (p) (β̸ = 1)
Y±
0 (p)
=
ln(1 −p) a±(p) + a±
1 (p) (β = 1)
(2.62)
where a± and a±
1 are in T ±
0,∞.
Proof
Note ﬁrst that by Proposition 13, M (eq. (2.58)) is well deﬁned on S0,
(eq.(2.56)). Moreover, since H is a solution of (1.25) on [0, 1 + ǫ), we have,
for h0 ∈S0, M(h) = 0 a.e. on [0, 1 + ǫ), i.e.,
M(S0) ⊂S0
Remark 27 For large b, M is a contraction in a small neighborhood of the
origin in ∥∥u,b.
Indeed, sup{∥(ˆΛ −p)−1∥Cn7→Cn : p ≥1 + ǫ} = O(ǫ−1) so that
∥M(h1) −M(h2)∥u,b ≤Const
ǫ
∥N (f + h) −N (f)∥u,b
(2.63)
The rest follows from (2.18) —Proposition 13 and Remark 10 applied to H.
The existence of a solution of (2.58) in S0 ∩L1
b([0, ∞)) for large enough b
is now immediate.
Uniqueness in L1
loc is tantamount to uniqueness in L1([1+ǫ, K]) = L1
b([1+
ǫ, K], for all K −1 −ǫ ∈R+. Now, assuming M had two ﬁxed points in
L1
b([1 + ǫ, K]), by Remark 10, we can choose b large enough so that these
solutions have arbitrarily small norm, in contradiction with Remark 27.
29
ii). For p < 1, Y±
0 (p) = Y0(p). For p ∈(1, 1 + ǫ) the result follows from
Lemma 20.
Noting that (in view of the estimate (2.15)) M(T ±1+ǫ,∞) ⊂
T ±1+ǫ,∞, the rest of the proof follows from the Remark 27 and Lemma 20.
Proposition 28 There is a one parameter family of solutions of equation
(1.25) in L1
loc[0, ∞), branching oﬀat p = 1 and in a neighborhood of p = 1
all solutions are of the form (2.43), (2.43’). The general solution of (1.25)
is Laplace transformable for large b and the Laplace transform is a solution
of the original diﬀerential equation in the half-space ℜ(x) > b.
Note: As of now, the correspondence (2.43), (2.43’) with the balanced
average (1.16) is proven only near p = 1; the complete correspondence is
established in Section 2.7.
Proof.
Let Y be any solution of (1.25). By Lemma 24 and Proposition 26, b
large implies that Y ∈L1
b([0, ∞)) (thus LY exists), that ∥Y∥b is small and,
in particular, that the sum deﬁning N in (1.22) is convergent in L1
b(R+).
By Remark 8,
L

X
|l|≥1
Gl ∗Y∗l +
X
|l|≥2
g0,lY∗l

(x) =
X
|l|≥1
(LGl)(LY)l(x) +
X
|l|≥2
g0,l (LY)l =
X
|l|≥1
gl(x)yl(x) = g(x, y(x))
(2.64)
(and g(x, y(x)) is analytic for ℜ(x) > b). The rest is straightforward.
