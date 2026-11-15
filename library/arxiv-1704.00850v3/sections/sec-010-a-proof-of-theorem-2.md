---
doc_id: arxiv-1704.00850v3
doc_title: "Estimating the spectral gap of a trace-class Markov operator"
section_id: sec-010-a-proof-of-theorem-2
section_title: "A Proof of Theorem 2"
section_number: null
pages: 26-30
source_pdf: 1704.00850v3.pdf
source_sha256: 09dd9c99453ba251
toc_source: outline
doc_brief: "Estimating the spectral gap of a trace-class Markov operator — The utility of a Markov chain Monte Carlo algorithm is, in large part, determined by the size of the spectral gap of the corresponding"
---
Proof of Theorem 2
Theorem 2. The DA operator P is trace-class if and only if
Z
SU
p(u, u) µ(du) < ∞.
(4)
If (4) holds, then for any positive integer k,
sk :=
κ
X
i=0
λk
i =
Z
SU
p(k)(u, u) µ(du) < ∞.
(5)
Proof. Note that P is self-adjoint and non-negative. Let {gi}∞
i=0 be an orthonormal basis of L2(πU). The
operator P is deﬁned to be trace-class if (see e.g. Conway, 2000)
∞
X
i=0
⟨Pgi, gi⟩πU < ∞.
(24)
This condition is equivalent to P being compact with summable eigenvalues. To show that P being trace-
class is equivalent to (4), we will prove a stronger result, namely
∞
X
i=0
⟨Pgi, gi⟩πU =
Z
SU
p(u, u)µ(du).
(25)
We begin by deﬁning two new Hilbert spaces. Let L2(πV ) be the Hilbert space consisting of functions
that are square integrable with respect to the weight function πV (·). For f, g ∈L2(πV ), their inner product
is deﬁned, as usual, by
⟨f, g⟩πV =
Z
SV
f(v)g(v)πV (v) ν(dv).
Let L2(πU × πV ) be the Hilbert space of functions on SU × SV that are square integrable with respect to the
weight function πU(·)πV (·). For f, g ∈L2(πU × πV ), their inner product is
⟨f, g⟩πU×πV =
Z
SU×SV
f(u, v)g(u, v)πU(u)πV (v) µ(du) ν(dv).
Note that L2(πV ) is separable. Let {hj}∞
j=0 be an orthonormal basis of L2(πV ). It can be shown that
{gihj}(i,j)∈Z2
+ is an orthonormal basis of L2(πU × πV ). Of course, gihj denotes the function given by
(gihj)(u, v) = gi(u)hj(v).
The inequality (4) is equivalent to
Z
SU×SV
 πU,V (u, v)
πU(u)πV (v)
2
πU(u)πV (v) µ(du) ν(dv) < ∞,
which holds if and only if the function ϕ : SU × SV →R given by
ϕ(u, v) = πU,V (u, v)
πU(u)πV (v)
is in L2(πU × πV ). Suppose (4) holds. Then by Parseval’s identity,
Z
SU
p(u, u) µ(du) = ⟨ϕ, ϕ⟩πU×πV
=
X
(i,j)∈Z2
+
|⟨ϕ, gihj⟩πU×πV |2
=
X
(i,j)∈Z2
+

Z
SU×SV
gi(u)hj(v)πU,V (u, v) µ(du) ν(dv)

2
=
∞
X
i=0
∞
X
j=0

Z
SV
 Z
SU
gi(u)πU|V (u|v) µ(du)

hj(v)πV (v) ν(dv)

2
.
Again by Parseval’s identity, this time applied to the function on SV (and in fact, in L2(πV ) by Jensen’s
inequality) given by
ϕi(v) =
Z
SU
gi(u)πU|V (u|v) µ(du),
we have
Z
SU
p(u, u) µ(du) =
∞
X
i=0
∞
X
j=0
|⟨ϕi, hj⟩πV |2
=
∞
X
i=0
⟨ϕi, ϕi⟩πV
=
∞
X
i=0
Z
SV

Z
SU
gi(u)πU|V (u|v) µ(du)

2
πV (v) ν(dv)
=
∞
X
i=0
Z
SV
Z
SU
 Z
SU
gi(u′)πU|V (u′|v)πV |U(v|u) µ(du′)

gi(u)πU(u) µ(du) ν(dv)
=
∞
X
i=0
Z
SU
 Z
SU
p(u, u′)gi(u′) µ(du′)

gi(u)πU(u) µ(du).
(26)
Note that the use of Fubini’s theorem in the last equality can be easily justiﬁed by noting that gi ∈L2(πU),
and making use of Jensen’s inequality. But the right hand side of (26) is precisely P∞
i=0⟨Pgi, gi⟩πU . Hence,
(25) holds when
R
SU p(u, u) µ(du) is ﬁnite.
To ﬁnish our proof of (25), we’ll show (24) implies (4). Assume that (24) holds. Tracing backwards
along (26) yields
X
(i,j)∈Z2
+
|⟨ϕi, hj⟩πV |2 < ∞.
This implies that the function
˜ϕ :=
X
(i,j)∈Z2
+
⟨ϕi, hj⟩πV gihj
is in L2(πU × πV ). Recall that (4) is equivalent to ϕ being in L2(πU × πV ). Hence, it sufﬁces to show that
˜ϕ(u, v) = ϕ(u, v) almost everywhere. Deﬁne a linear transformation T : L2(πU) →L2(πV ) by
Tf(v) =
Z
SU
f(u)πU|V (u|v) µ(du),
∀f ∈L2(πU).
By Jensen’s inequality, T is bounded, and thus, continuous. For any g = P∞
i=0 αigi ∈L2(πU) and h =
P∞
j=0 βjhj ∈L2(πV ),
Z
SV
Z
SU
ϕ(u, v)g(u)h(v) πU(u)πV (v) µ(du) ν(dv)
= ⟨Tg, h⟩πV
=
∞
X
i=0
∞
X
j=0
αiβj⟨Tgi, hj⟩πV
=
∞
X
i=0
∞
X
j=0
αiβj⟨ϕi, hj⟩πV
= ⟨˜ϕ, gh⟩πU×πV
=
Z
SV
Z
SU
˜ϕ(u, v)g(u)h(v) πU(u)πV (v) µ(du) ν(dv),
where g ∈L2(πV ) is given by g(u) := g(u), and gi is deﬁned similarly for i ∈Z+. This implies that for
any C1 ∈U and C2 ∈V,
Z
C1×C2
ϕ(u, v) πU(u)πV (v) µ(du) ν(dv) =
Z
C1×C2
˜ϕ(u, v) πU(u)πV (v) µ(du) ν(dv).
Note that
Z
SU×SV
| ˜ϕ(u, v)| πU(u)πV (v) µ(du) ν(dv) ≤⟨˜ϕ, ˜ϕ⟩1/2
πU×πV < ∞.
(27)
By (27) and the dominated convergence theorem, one can show that
A :=
n
C ∈U × V

Z
C
ϕ(u, v) πU(u)πV (v) µ(du) ν(dv) =
Z
C
˜ϕ(u, v) πU(u)πV (v) µ(du) ν(dv)
o
is a λ system. An application of Dynkin’s π-λ theorem reveals that U × V ⊂A. Therefore, ˜ϕ(u, v) =
ϕ(u, v) almost everywhere, and (4) follows.
For the rest of the proof, assume that P is trace-class. This implies that P is compact, and thus admits
the spectral decomposition (see e.g. Helmberg, 2014, §28 Corollary 2.1) given by
Pf =
κ
X
i=0
λi⟨f, fi⟩πU fi,
f ∈L2(πU)
(28)
where fi, i = 0, 1, . . . , κ, is the normalized eigenfunction corresponding to λi. By Parseval’s identity,
∞
X
i=0
⟨Pgi, gi⟩πU =
∞
X
i=0
κ
X
j=0
λj|⟨gi, fj⟩πU |2
=
κ
X
j=0
λj⟨fj, fj⟩πU
=
κ
X
j=0
λj.
This equality is in fact a trivial case of Lidskii’s theorem (see e.g. Erd¨os, 1974; Gohberg et al., 2012). It
follows that (5) holds for k = 1.
We now consider the case where k ≥2. By (28) and a simple induction, we have the following decom-
position for P k.
P kf =
κ
X
i=0
λk
i ⟨f, fi⟩πU fi,
f ∈L2(πU) .
Hence P k is trace-class with ordered positive eigenvalues {λk
i }κ
i=0. Note that P k is a Markov operator whose
Mtd is p(k)(u, ·), u ∈SU. Thus, in order to show that (5) holds for k ≥2, it sufﬁces to verify P k is a DA
operator, for then we can treat P k as P and repeat our argument for the k = 1 case. To be speciﬁc, we’ll
show that there exists a random variable ˜V taking values on S ˜V , where (S ˜V , ˜V, ˜ν) is a σ-ﬁnite measure space
and ˜V is countably generated, such that for u ∈SU,
p(k)(u, ·) =
Z
S ˜V
πU| ˜V (·|v)π ˜V |U(v|u) ˜ν(dv),
(29)
where π ˜V (·), πU| ˜V (·|·), and π ˜V |U(·|·) have the apparent meanings.
Let (Uk, Vk)∞
k=0 be a Markov chain. Suppose that U0 has pdf πU(·), and for any non-negative integer k,
let Vk|Uk = u have pdf πV |U(·|u), and let Uk+1|Vk = v have pdf πU|V (·|v). It’s easy to see {Uk}∞
k=0 is a
stationary DA chain with Mtd p(u, ·). Suppose k is even. The pdf of Uk|U0 = u is
p(k)(u, ·) =
Z
SU
p(k/2)(u, u′)p(k/2)(u′, ·)µ(du).
Meanwhile, since the chain is reversible and starts from the stationary distribution, U0|Uk/2 = u has the
same distribution as Uk/2|U0 = u, which is just p(k/2)(u, ·). Thus, (29) holds with ˜V = Uk/2. A similar
argument shows that when k is odd, (29) holds with ˜V = V(k−1)/2.
