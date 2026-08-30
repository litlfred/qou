---
doc_id: arxiv-2412.04241v2
doc_title: "THE HABIRO RING OF A NUMBER FIELD"
section_id: sec-021-33-proof-of-the-main-theorems
section_title: "Proof of the main theorems"
section_number: 3.3
pages: 43-45
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
doc_brief: "THE HABIRO RING OF A NUMBER FIELD — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
Proof of Theorem 2 of Section 1.5. Firstly, we see that HR⊆H R,0 as f(q) = 1 is a global
invertible L(0)-section. For all p prime to ∆, the constant collection 1 is an invertible
Lp(0)-section. Therefore, from Corollary 3.7 of Section 3.2 and the gluing condition (24) of
Definition 1.4, if f∈H R,0, then f∈H R∧p . Varying over all primes shows that f∈H R. This
completes the proof thatHR,0 =HR. The second statement follows from the fact that εm is
multiplicative while Dp is additive and that the conditions equation (24) and equation (21)
are multiplicative as a consequence. The final statement follows from the combination of the
previous two. □
Proof of Theorem 5 of Section 1.7. Firstly, we show that the constant term of fA,z,m(x) is
εm(ξ)1/m times an element of K[ζm]. For m prime to ∆ (where ∆ includes the primes 2 and
3 and finitely many other primes that depend only on the number field K), this follows from
Theorem 1.6 and equation (14) of [10, Thm.1.6] combined with Hutchinson [31].
Secondly, we will prove that for a system of q-difference equations associated to the com-
bination in equation (24) there is a unique solution in formal power series in t. We will
explicitly describe the case when N = 1. (We again omit the case when N > 1, since it
completely analogous but notationally heavier.) To do this, we will use standard methods
in the study of q-holonomic modules. Recall the q-difference equation (33) and define
ψA,µ(t,q ) = FA(qµt,q ). (211)
Fix γ∈ Z>0 and consider the function
(µ,ν,t )7→ψ(γ)
A,µ,ν(t,q ) = ψA,µ1(t,qγ)··· ψA,µγ(t,qγ)ψA,ν(t,q−1), (212)
where µ = ( µ1,...,µ γ)∈ Zγ and ν∈ Z. It satisfies γ + 2 equations, corresponding to the
number of variables:
ψ(γ)
A,µ,ν(t,q )−ψ(γ)
A,µ+δi,ν(t,q ) = ( −1)AqAγtψ(γ)
A,µ+Aδi,ν(t,q ) ( i = 1,··· ,γ ),
ψ(γ)
A,µ,ν(t,q )−ψ(γ)
A,µ,ν+1(t,q ) = ( −1)Aq−Atψ(γ)
A,µ,ν+A(t,q ),
ψ(γ)
A,µ(qt,q ) = ψ(γ)
A,µ+1,ν−1(t,q ).
(213)
44 STA VROS GAROUF ALIDIS, PETER SCHOLZE, CAMPBELL WHEELER, AND DON ZAGIER
These equations have a unique solution for power series in t of the form 1 + O( t). This
follows from the fact that the first two equations imply that the coefficient of tk in ψ(γ) is
constant in µ,ν modulo coefficients of smaller powers of t. Assuming this, the last equation
implies that this coefficient multiplied by qk− 1 is given entirely by combinations of lower
order terms. Therefore, everything is determined by the coefficient of t0.
From the explicit formulas of equation (117) and equation (118), Theorem 8 of Sec-
tion 2.7, Theorem 4 of Section 1.7, and Galois invariance under z1/m 7→ ζmz1/m; we see
thatψ(γ)
A,µ,ν(t1/m,ζm +x)∈S(m)
p [ [x] ], for all primesp prime to ∆ andm prime toγ. Therefore,
ψ(γ)
A,µ,ν(t1/m,ζm + x) ∈ S(m)[ [x] ]. Moreover, since there is a unique solution to the equa-
tions (213), if we p-complete and re-expand by x7→ x +ζpm−ζm then we must find an
equality after applying a Frobenius, which maps t7→ tp. Therefore, these equalities persist
when we specialise t = 1. This proves that fA,z satisfies equation (24).
For the rest of the proof, we fix a positive integer m, a prime p with (m,p ) = 1 and a
congruence class k∈ (Z/mZ)N. Theorems 4 of Section 1.7 and 8 of Section 2.7 imply that
each term Ω FGI
A,m,k(t,x ) of equation (126), specialised to t = 1, satisfies equation (39), which
is an essentially equation (21) restricted to a disc. Summing up using (117) and (126), we
obtain that
f FGI
A,m(1,x ) =
X
k∈(Z/mZ)N
(−1)diag(A)·kq
1
2 (ktAk+diag(A)·k)
(q;q)k1··· (q;q)kN
ΩFGI
A,m,k(1,q ), q = ζm +x. (214)
It follows that f FGI
A (1,q ) gives an element of the module HR[δ−1/2]∧p [ζm,z1/m],ξ for q-restricted
to the disc around ζm. Finally, from the invariance under z1/m7→ζmz1/m from Lemma 2.12
of Section 2.5, we see that fA,z(q) descends to an element ofHR[δ−1/2]∧p,ξ restricted to the disc
around ζm.
Varying over all m prime to ∆ and combining this with the previous result that equa-
tion (24) is satisfied, we conclude that fA,z(q)∈H R[δ−1/2],ξ|∆. □
Proof of Corollary 1.11 of Section 1.7. This would immediately follow from Theorem 5 of
Section 1.7, Theorem 2 of Section 1.5, and Proposition 1.5 of Section 1.5; if we did not have
the technical assumption on the order of roots of unity being prime to ∆.
However, equation (44) does immediately follow from the proof of Theorem 5 of Section 1.7
that showed fA,z satisfies equation (24), which in particular holds when γ = 1.
For part (b), a weaker statement asserting that fA,z(q)r∈H R[1/
√
δ]|∆ follows from Theo-
rem 5 of Section 1.7 and Theorem 2 of Section 1.5. To replace HR[1/
√
δ]|∆ byHR[1/
√
δ], note
the surjective map K3(K)→ B(K) of Suslin (see e.g., [52, Eqn.(1.1)]). Hence, if rξ = 0,
then the image of ξ in the Bloch group can be written as a sum of 5-term relations in the
Bloch group. Then the identity of [34] that was used in [10] shows that the constant term
at ζm is in S(m). □
Remark 3.11. In fact, the specialisation t = qν for ν∈ ZN (i.e., tj = qνj for integers νj)
defines an element fA,z,ν(q)∈H R[1/
√
δ],ξ|∆. The proof is identical to the proof of Theorem 5
of Section 1.7 and is omitted.
THE HABIRO RING OF A NUMBER FIELD 45
Proof of Proposition 1.5 of Section 1.5. The proofs of the proposition are all elementary and
outlined as follows:
• Property (a) and (d) follow from the χ−1 equivariance of ε.
• Property (b) follows from Theorem 2 of Section 1.5.
• Property (c) is trivial and follows from the definition of γ∗ just prior to the proposi-
tion.
• Property (e) this property follows from the fact that, varying overγ,γ′, the collections
f(qγ1)··· f(qγn)f(q−γ′
1)··· f(q−γ′
n′), where P
kγ−1
k −P
kγ′−1
k = 0 determine f(q).
Alternatively, one could use the remark of Section 3.2 to connect various roots of
unity.
• Property (f) follows from the fact that the constants fm(0)∈R∧
p [ζm,ε 1/m
m ] for all m
and p with (mp, ∆) = 1.
□
An immediate corollary of part (f) is the following result, which even in very simple
instances like the 4 1-knot seems very difficult to prove directly.
Corollary 3.12. For m prime to ∆, the constants U FGI
m (1) from equation (121) are ∆-
integral.
