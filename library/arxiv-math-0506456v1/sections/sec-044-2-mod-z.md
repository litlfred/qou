---
doc_id: arxiv-math-0506456v1
doc_title: "Journal of Knot Theory and Its Ramiﬁcations c© W orld Scientiﬁc Publishing Company ASYMPTOTICS OF THE QUANTUM INV ARIANTS FOR SURGERIES ON THE FIGURE 8 KNOT JØRGEN ELLEGAARD ANDERS"
section_id: sec-044-2-mod-z
section_title: "(mod Z)"
section_number: 2
pages: 50-52
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
Here
2
∫ θ0
1/6
βε(t)dt = 2fε(θ0)
(
θ0 − 1
6
)
+ 1
πi
∫ θ0
θ1
Log(Lε(θ))dθ,
so
Ψ 0,b
n (2θ0,y ) − CS(¯ρθ0,ε) = 1
πi
(∫ θ0
1/6
Log(Lε(θ))dθ −
∫ θ0
θ1
Log(Lε(θ))dθ
)
+ 1
6 + 2eε(θ0)θ1 − 1
3fε(θ0) + b(θ0)
2 −θ1 (mod Z).
The subcase θ0 ∈]1/6, 1/4[. Here we have θ1 = 1/6 and b(θ0) = 0 so the result
follows by the fact that eε(θ) = fε(θ) for θ ∈]1/6, 1/4[.
The subcase θ0 ∈]1/4, 1/3[. In this case we have b(θ0) = 1 and θ1 = 1/3 so
Ψ 0,b
n (2θ0,y ) − CS(¯ρθ0,ε) = 1
πi
(∫ θ0
1/6
Log(Lε(θ))dθ −
∫ θ0
1/3
Log(Lε(θ))dθ
)
+ 1
3 + 2
3eε(θ0) − 1
3fε(θ0) (mod Z).
By (5.91) we get
∫ θ0
1/3
Log(L±(t))dt =
∫ 1
2 −θ0
1/3
Log(L±(t))dt = −
∫ θ0
1/6
Log(L±
(1
2 −t
)
)dt.
By (5.89) and (5.90) we then have
∫ θ0
1/3
Log(L±(t))dt =
∫ θ0
1/6
Log(L±(t))dt,
so
Ψ 0,b
n (2θ0,y ) − CS(¯ρθ0,ε) = 1
3 + 2
3eε(θ0) − 1
3fε(θ0) (mod Z),
and this is zero by Lemma 8, (5.72) and (5.73).
Asymptotics of the quantum invariants for the ﬁgure 8 knot 51
Remark 7. If u± = u±(v) are the two solutions to φ(v2,u ) = 0 for v ∈ C∗ ﬁxed,
then λ11(v,u −) = λ11(v,u +)−1 by Lemma 9. By the proof of Theorem 7 we there-
fore conclude that (v, 1 +uε),ε ∈ {±} , is a solution to (4.41) and (4.42) if and only
if (v, 1 +u−ε) is a solution to (4.42) and
vp =
(w −v2
1 −v2w
) q
. (5.92)
If we work with the invariants τr instead of the invariants ¯τr, then by (2.16) we
have to change p/q to −p/q everywhere in the above. The equation (4.42) will be
the same but (4.41) will change to (5.92). If ( v,u ) ∈ ˜N then we ﬁnd as in the proof
of Theorem 7 that ( v,w ) = (v,u + 1) is a solution to (5.92) if and only if ( v,u ) is a
solution to
vp =λ11(v,u )q,
which is the “wrong” equation. This is one of the main reasons for wor king with ¯τr
instead of τr. Another reason is that one would get a minus sign in (5.78).
Let us end this section by some futher results on the Chern–Simons invariants
of ﬂat irreducible SU(2)–connections on Mp/q. By (5.90) ¯ρθ,ε extends to a SU(2)–
representation of π1(Mp/q) if and only if ¯ ρθ,−ε extends to a SU(2)–representation
of π1(M−p/q). In that case we ﬁnd that
CS(¯ρθ,−ε) = −CS(¯ρθ,ε)
by using (5.74).
If p is even then e2πip(1/2−θ) = e2πipθ. Since Lε(1/2 −θ) = Lε(θ)−1 by (5.89)
and (5.90) and since q is odd it follows that ¯ρθ,ε extends to a SU(2)–representation
of π1(Mp/q) if and only if ¯ ρ1/2−θ,ε extends to such a representation, see (5.65).
Assuming that ¯ρθ,ε extends to such a representation we get
CS(¯ρ 1
2 −θ,ε) = CS(¯ρθ,ε) − 1
2
p
2 (mod Z)
by using (5.91) and (5.74).
By (5.70) and (5.65) we ﬁnd that ¯ ρ1/6,− = ¯ρ1/6,+ is a SU(2)–representation of
π1(Mp/q) if and only if p = 6m + 3, m ∈ Z, and q is odd. In that case
CS(¯ρ1/6,ε) = −cp
36 − dq
4 − 1
2d (mod Z).
By (5.70) and (5.65) we also have that ¯ρ1/3,− = ¯ρ1/3,+ is a SU(2)–representation of
π1(Mp/q) if and only if p = 6m + 3, m ∈ Z, and q is even. In that case
CS(¯ρ1/3,ε) = 1
2 − cp
9 − dq
4 (mod Z).
52 Asymptotics of the quantum invariants for the ﬁgure 8 knot
Finally, by (5.70) and (5.65), ρ1/4,− and ρ1/4,+ are SU(2)–representations of
π1(Mp/q) if and only if 4 divides p. In that case we ﬁnd that
CS(¯ρ1/4,+) = 1
5 − cp
