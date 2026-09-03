---
doc_id: arxiv-1704.00850v3
doc_title: "Estimating the spectral gap of a trace-class Markov operator"
section_id: sec-009-a-proof-of-theorem-2
section_title: "A Proof of Theorem 2"
section_number: null
pages: 26-30
source_pdf: 1704.00850v3.pdf
source_sha256: 09dd9c99453ba251
doc_brief: "Estimating the spectral gap of a trace-class Markov operator — The utility of a Markov chain Monte Carlo algorithm is, in large part, determined by the size of the spectral gap of the corresponding"
---
Theorem 2. The DA operatorP is trace-class if and only if
∫
SU
p(u,u )µ(du)<∞. (4)
If (4) holds, then for any positive integerk,
sk :=
κ∑
i=0
λk
i =
∫
SU
p(k)(u,u )µ(du)<∞. (5)
26
Proof. Note that P is self-adjoint and non-negative. Let {gi}∞
i=0 be an orthonormal basis of L2(πU). The
operatorP is deﬁned to be trace-class if (see e.g. Conway, 2000)
∞∑
i=0
⟨Pgi,gi⟩πU <∞. (24)
This condition is equivalent to P being compact with summable eigenvalues. To show that P being trace-
class is equivalent to (4), we will prove a stronger result, namely
∞∑
i=0
⟨Pgi,gi⟩πU =
∫
SU
p(u,u )µ(du). (25)
We begin by deﬁning two new Hilbert spaces. Let L2(πV ) be the Hilbert space consisting of functions
that are square integrable with respect to the weight function πV (·). Forf,g ∈L2(πV ), their inner product
is deﬁned, as usual, by
⟨f,g⟩πV =
∫
SV
f(v)g(v)πV (v)ν(dv).
LetL2(πU×πV ) be the Hilbert space of functions onSU×SV that are square integrable with respect to the
weight functionπU(·)πV (·). Forf,g ∈L2(πU×πV ), their inner product is
⟨f,g⟩πU×πV =
∫
SU×SV
f(u,v )g(u,v )πU(u)πV (v)µ(du)ν(dv).
Note that L2(πV ) is separable. Let {hj}∞
j=0 be an orthonormal basis of L2(πV ). It can be shown that
{gihj}(i,j)∈Z2
+
is an orthonormal basis of L2(πU×πV ). Of course, gihj denotes the function given by
(gihj)(u,v ) =gi(u)hj(v).
The inequality (4) is equivalent to
∫
SU×SV
( πU,V (u,v )
πU(u)πV (v)
)2
πU(u)πV (v)µ(du)ν(dv)<∞,
which holds if and only if the functionϕ :SU×SV→ R given by
ϕ(u,v ) = πU,V (u,v )
πU(u)πV (v)
is inL2(πU×πV ). Suppose (4) holds. Then by Parseval’s identity,
∫
SU
p(u,u )µ(du) =⟨ϕ,ϕ⟩πU×πV
=
∑
(i,j)∈Z2
+
|⟨ϕ,gihj⟩πU×πV|2
=
∑
(i,j)∈Z2
+
⏐⏐⏐
∫
SU×SV
gi(u)hj(v)πU,V (u,v )µ(du)ν(dv)
⏐⏐⏐
2
=
∞∑
i=0
∞∑
j=0
⏐⏐⏐
∫
SV
(∫
SU
gi(u)πU|V (u|v)µ(du)
)
hj(v)πV (v)ν(dv)
⏐⏐⏐
2
.
27
Again by Parseval’s identity, this time applied to the function on SV (and in fact, in L2(πV ) by Jensen’s
inequality) given by
ϕi(v) =
∫
SU
gi(u)πU|V (u|v)µ(du),
we have
∫
SU
p(u,u )µ(du) =
∞∑
i=0
∞∑
j=0
|⟨ϕi,hj⟩πV|2
=
∞∑
i=0
⟨ϕi,ϕi⟩πV
=
∞∑
i=0
∫
SV
⏐⏐⏐
∫
SU
gi(u)πU|V (u|v)µ(du)
⏐⏐⏐
2
πV (v)ν(dv)
=
∞∑
i=0
∫
SV
∫
SU
(∫
SU
gi(u′)πU|V (u′|v)πV|U(v|u)µ(du′)
)
gi(u)πU(u)µ(du)ν(dv)
=
∞∑
i=0
∫
SU
(∫
SU
p(u,u′)gi(u′)µ(du′)
)
gi(u)πU(u)µ(du).
(26)
Note that the use of Fubini’s theorem in the last equality can be easily justiﬁed by noting that gi∈L2(πU),
and making use of Jensen’s inequality. But the right hand side of (26) is precisely∑∞
i=0⟨Pgi,gi⟩πU. Hence,
(25) holds when
∫
SU
p(u,u )µ(du) is ﬁnite.
To ﬁnish our proof of (25), we’ll show (24) implies (4). Assume that (24) holds. Tracing backwards
along (26) yields
∑
(i,j)∈Z2
+
|⟨ϕi,hj⟩πV|2<∞.
This implies that the function
˜ϕ :=
∑
(i,j)∈Z2
+
⟨ϕi,hj⟩πVgihj
is inL2(πU×πV ). Recall that (4) is equivalent toϕ being inL2(πU×πV ). Hence, it sufﬁces to show that
˜ϕ(u,v ) =ϕ(u,v ) almost everywhere. Deﬁne a linear transformation T :L2(πU)→L2(πV ) by
Tf (v) =
∫
SU
f(u)πU|V (u|v)µ(du), ∀f∈L2(πU).
By Jensen’s inequality,T is bounded, and thus, continuous. For any g = ∑∞
i=0αigi∈ L2(πU) andh =
28
∑∞
j=0βjhj∈L2(πV ),
∫
SV
∫
SU
ϕ(u,v )g(u)h(v)πU(u)πV (v)µ(du)ν(dv)
=⟨Tg,h⟩πV
=
∞∑
i=0
∞∑
j=0
αiβj⟨Tgi,hj⟩πV
=
∞∑
i=0
∞∑
j=0
αiβj⟨ϕi,hj⟩πV
=⟨ ˜ϕ,gh⟩πU×πV
=
∫
SV
∫
SU
˜ϕ(u,v )g(u)h(v)πU(u)πV (v)µ(du)ν(dv),
whereg∈ L2(πV ) is given by g(u) := g(u), andgi is deﬁned similarly for i∈ Z+. This implies that for
anyC1∈U andC2∈V ,
∫
C1×C2
ϕ(u,v )πU(u)πV (v)µ(du)ν(dv) =
∫
C1×C2
˜ϕ(u,v )πU(u)πV (v)µ(du)ν(dv).
Note that ∫
SU×SV
| ˜ϕ(u,v )|πU(u)πV (v)µ(du)ν(dv)≤⟨ ˜ϕ, ˜ϕ⟩1/2
πU×πV <∞. (27)
By (27) and the dominated convergence theorem, one can show that
A :=
{
C∈U×V
⏐⏐⏐
∫
C
ϕ(u,v )πU(u)πV (v)µ(du)ν(dv) =
∫
C
˜ϕ(u,v )πU(u)πV (v)µ(du)ν(dv)
}
is a λ system. An application of Dynkin’s π-λ theorem reveals that U×V ⊂A . Therefore, ˜ϕ(u,v ) =
ϕ(u,v ) almost everywhere, and (4) follows.
For the rest of the proof, assume that P is trace-class. This implies that P is compact, and thus admits
the spectral decomposition (see e.g. Helmberg, 2014,§28 Corollary 2.1) given by
Pf =
κ∑
i=0
λi⟨f,fi⟩πUfi, f ∈L2(πU) (28)
wherefi, i= 0, 1,...,κ, is the normalized eigenfunction corresponding toλi. By Parseval’s identity,
∞∑
i=0
⟨Pgi,gi⟩πU =
∞∑
i=0
κ∑
j=0
λj|⟨gi,fj⟩πU|2
=
κ∑
j=0
λj⟨fj,fj⟩πU
=
κ∑
j=0
λj.
29
This equality is in fact a trivial case of Lidskii’s theorem (see e.g. Erd ¨os, 1974; Gohberg et al., 2012). It
follows that (5) holds fork = 1.
We now consider the case wherek≥ 2. By (28) and a simple induction, we have the following decom-
position forPk.
Pkf =
κ∑
i=0
λk
i⟨f,fi⟩πUfi, f ∈L2(πU).
HencePk is trace-class with ordered positive eigenvalues{λk
i}κ
i=0. Note thatPk is a Markov operator whose
Mtd isp(k)(u,·), u∈ SU. Thus, in order to show that (5) holds for k≥ 2, it sufﬁces to verify Pk is a DA
operator, for then we can treat Pk asP and repeat our argument for the k = 1 case. To be speciﬁc, we’ll
show that there exists a random variable˜V taking values onS ˜V, where (S ˜V, ˜V, ˜ν) is aσ-ﬁnite measure space
and ˜V is countably generated, such that foru∈SU,
p(k)(u,·) =
∫
S ˜V
πU| ˜V (·|v)π ˜V|U(v|u) ˜ν(dv), (29)
whereπ ˜V (·),πU| ˜V (·|·), andπ ˜V|U(·|·) have the apparent meanings.
Let (Uk,Vk)∞
k=0 be a Markov chain. Suppose thatU0 has pdfπU(·), and for any non-negative integerk,
letVk|Uk = u have pdfπV|U(·|u), and let Uk+1|Vk = v have pdfπU|V (·|v). It’s easy to see{Uk}∞
k=0 is a
stationary DA chain with Mtdp(u,·). Supposek is even. The pdf ofUk|U0 =u is
p(k)(u,·) =
∫
SU
p(k/2)(u,u′)p(k/2)(u′,·)µ(du).
Meanwhile, since the chain is reversible and starts from the stationary distribution, U0|Uk/2 = u has the
same distribution as Uk/2|U0 = u, which is just p(k/2)(u,·). Thus, (29) holds with ˜V = Uk/2. A similar
argument shows that whenk is odd, (29) holds with ˜V =V(k−1)/2.
