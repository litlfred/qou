---
doc_id: arxiv-math-0506456v1
doc_title: "Asymptotics of the quantum invariants for surgeries on the figure 8 knot"
section_id: sec-020-43-the-large-r-asymptotics-of-τrmpq
section_title: "The large r asymptotics of τr(Mp/q)"
section_number: 4.3
pages: 19-21
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
In Sec. 5 we will see that the signs of the phases in the asymptotics o f ¯τr(Mp/q) =
τr(Mp/q) agrees with the Chern–Simons values, hence we work with this conj ugate
invariant. Because of (2.16) we can always obtain the asymptotic ex pansion of
τr(Mp/q) by complex conjugation or by replacing either p by −p or q by −q. By
Lemma 2 we have
¯τr(Mp/q) = β1(r)
∑
n∈Z/|q|Z
∫
C 1r ×C 2r
cot(πrx) tan(πry) ¯fn,r(x,y )dxdy, (4.34)
where
β1(r) = isign(q)r
4
√
|q|
e
3πi
4 sign(pq) exp
(
−πi
2r
[
3sign(pq) − p
q + S
(p
q
)])
(4.35)
20 Asymptotics of the quantum invariants for the ﬁgure 8 knot
and
¯fn,r(x,y ) = sin
(π
q (x − 2nd)
)
e2πir
(
− dn2
q − p
4qx2+ n
qx−xy
)
Sγ(−π + 2π(x −y))
Sγ(−π + 2π(x +y)),
where γ =π/r as usual. Let for k,l ∈ Z
Ωk,l = { (x,y ) ∈ C2 | Re(x) + Re(y) ∈ [k,k + 1], Re(x) − Re(y) ∈ [−l, −l + 1] }.
For (x,y ) ∈ Ωk,l, we have by (3.18) and (4.23) that
¯fn,r(x,y ) = sin
(π
q (x − 2nd)
) (
1 +e2πi(x−y)r
) l(
1 +e2πi(x+y)r
) k
e2πirΦ n(x,y)
× exp (Iγ(−π + 2π(x −y +l)) −Iγ(−π + 2π(x +y −k))),
where
Φn(x,y ) = −dn2
q − p
4qx2 + n
qx −xy + 1
4π2
(
Li2(e2πi(x+y)) − Li2(e2πi(x−y))
)
.
We note that this expression and the above expression for ¯fn,r are only valid for
(x,y ) ∈ C2 satisfying the two conditions
(i) Re( x) + Re(y) /∈ Z ∨ Im(x) + Im(y) ≥ 0,
(ii) Re( x) − Re(y) /∈ Z ∨ Im(x) − Im(y) ≥ 0.
Observe that for k,l ∈ {0, 1}, which corresponds to the four diﬀerent Ω k,l inter-
secting C1
r ×C2
r , we have that
(
1 +e2πi(x−y)r
) l(
1 +e2πi(x+y)r
) k
=
∑
(a,b)∈Fk,l
e2πi(a(x+y)+b(x−y))r,
where Fk,l = {(a,b ) ∈ {0, 1}2 |a ≤k, b ≤l}. Hence, for such k,l we have
¯fn,r(x,y ) =
∑
(a,b)∈Fk,l
sin
(π
q (x − 2nd)
)
e2πirΦ a,b
n (x,y)
× exp (Iγ(−π + 2π(x −y +l)) −Iγ(−π + 2π(x +y −k)))
for (x,y ) ∈ Ωk,l, where
Φa,b
n (x,y ) = a(x +y) +b(x −y) + Φ n(x,y ). (4.36)
Let
Ωµ,ν
k,l = {(x,y ) ∈ Ωk,l |µIm(x) ≥ 0, ν Im(y) ≥ 0}.
