---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-126-5-periods-as-solutions-of-the-gauss-manin-connec
section_title: "PERIODS AS SOLUTIONS OF THE GAUSS-MANIN CONNECTION. 59"
section_number: 5
pages: 63-65
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp — 580 sections: INTRODUCTION; INTRODUCTION; INTRODUCTION"
---
• Let E = Q[
√
−d] and E′ = Q[
√
−d′] be two distinct subﬁelds of D (d,d′
squarefree; we do not exclude the case d =d′). According to [ Vig80, II 1.4],
E∩ D =OE, E′∩ D =OE′. The elements e =
√
−d∈E and e′ =
√
−d′∈
E′ generate the algebra D. We remark that ee′ +e′e commutes to e ande′,
hence is an integer m∈ Z (an even integer if d or d′≡ 3 (mod 4), which is
divisible by 4 if both d,d′≡ 3 (mod 4)). We have ( ee′−e′e)2 =m2− 4dd′.
Sinceee′−e′e anticommutes with e, it is not an integer, hence |m|< 2
√
dd′.
On the other hand, the images of e and e′ in D⊗ Fp commute (ee′−e′e
acts trivially on regular diﬀerentials in characteristic p), therefore p divides
4dd′−m2.
• On the other hand, there exists a unique symplectic basis of e igenvectors
fore in H 1
dR(A) of the form ( ω1,ω 2 +σω1), with σ∈k. We get the relation
ω22 +σω12 =~τ (ω21 +σω11), with~τ =−a−c
√
−d
b .
Let now E′ = Q[
√
−d′]⁄= E be another subﬁeld of D, and assume that
(γ1,γ 2) is a basis of eigenvectors for E′: e′.γ1 =
√
−d′γ1. We get ( ee′ +
e′e)γ1 = 2a
√
−d′
c γ1 =mγ1, so that
~τ
τ = m + 2
√
dd′
m− 2
√
dd′∈ Q[
√
dd′]
the sign of the square root being chosen in such a way that p| 2
√
dd′−m
(in the unramiﬁed case).
• The previous relations, together with det Ω = 1, show that the transcen-
dence degree over
Q of the entries of Ω is at most one in the CM case.
• We now describe the p-adic number ω11 modulo Q
×
, keeping the notation
of 4.6.2 and Theorem 4.6.3 ( ǫ is the Dirichlet character, w the number of
roots of unity, h the class number).
Theorem 5.3.9. In case p does not ramify in the ﬁeld of complex multipli-
cations Q[
√
−d] = End(A)⊗ Q, one has
ω11 ∼
∏
u∈(Z/d)×
(
Γ p
⟨
pu
d
⟩)−ǫ(u)w/8h
in Q
×
p/
Q
×
.
Examples. If A is the Legendre curve X1/2 (y2 = x(x− 1)(x− 1/2)) and
p≡ 3 (mod 4), we ﬁnd ω11∼ Γ p(1/4). Similarly, if End(A)⊗ Q = Q(√−3)
andp≡ 2 (mod 3), then ω11∼ Γ p(1/3)3/2.
Proof. We may assume that the number ﬁeld k (⊂ Qp) is Galois over
Q. We denote by k′ = k∩ Qp the subﬁeld of k ﬁxed by the local Galois
group Gal( Qp/Qp). Let us consider the Weil restriction B := Rk/k′(A)
(cf. [BLR90, 7.6]). This is an abelian variety over k′⊂ Qp, with good,
supersingular reduction at p (likeA), and we have Bk≃∏
τ∈Gal(k/k′)Aτ .
60 I. ANALYTIC ASPECTS OF p-ADIC PERIODS.
On the other hand, let ψ be any element of degree one in the Weil group
(i.e. any lifting of the Frobenius element in Gal( Qp/Qp)), and let Ψ Aτ (resp.
Ψ B) be the corresponding semilinear endomorphism of H 1
dR(Aτ/k)⊗
Qp
(resp. H1
dR(B/k′)⊗
Qp). If Φ B denotes the canonical linear action induced
by Fr Fp on H 1
crys(B0/Qp)⊗
Qp ≃ H1
dR(B)
Qp
, one has the formula Ψ B =
Φ B◦ (id⊗ψ) ( cf. [BeO83, 4]). Moreover, Ψ B =⨁ Ψ Aτ with respect to the
decomposition H 1
dR(B,
Qp)≃⨁
τ H1
dR(Aτ,
Qp).
If (ω1,ω 2) is any symplectic basis of eigenvectors for Q[
√
−d] in H 1
dR(A)
Q,
with ω1∈ Ω 1(A)Q, we can write Ψ A(ω1) = κ.ω2, where κ modulo Q
×
is
given by Ogus’ formula in Theorem 4.6.3
κ ∼
∏
u∈(Z/d)×
(
Γ p
⟨
pu
d
⟩)−ǫ(u)w/4h
in Q
×
p/
Q
×
.
Because the conjugates Aτ are isogenous to each other over k (and since iso-
genies preserve the regular diﬀerential forms), we derive t hat the constant κ,
resp. the “period” ω11, is the same modulo Q
×
for each of them. Therefore,
for any ω∈ Ω 1(B)⊂ H1
crys(B0/Qp), we can write Φ B(ω) = Ψ B(ω) = κ.η for
someη∈ H1
dR(B)
Q whose pairing with any element of H 1B(B, Q) belongs to
ω21.Q. Since ω−1
11ω∈ H1
B(B,
Q), ω−1
21η∈ H1
B(B,
Q), and since Φ B respects
H1B(B, Q), we get κ∼ ω11
ω21
∼ω2
11, whence the result.
Conjecture 5.3.10. Assume that A is a lifting of A0 deﬁned over Q, and
that p does not ramify End(A)⊗ Q (which is obviously the case if A does
not have complex multiplication). Then H1
dR(B)
Q⁄= H 1
1B(B,
Q).
In the absence of complex multiplication, this follows from the previous
conjecture. In the presence of complex multiplication, it a mounts to the
transcendence of ω11.
Taking into account 5.3.9, the conjecture would imply, for i nstance, the
transcendence of the adic numbers Γ 3(1/4), Γ 7(1/4), Γ 2(1/3), Γ 5(1/3) (note,
in contrast, that Γ 5(1/4) and Γ 7(1/3) are algebraic numbers, according to
the Gross-Koblitz formula (2.6.4)).
• Actually, it may happen, in the ramiﬁed CM case, that H 1
dR(A)
Q =
H1
1B(A,
Q).
Let us ﬁrst notice that the argument given in the proof of theo rem 5.3.9
still works in the ramiﬁed case, and allows to conclude that κ∼ ω2
11. The
computation of κ (mod Q
×
) (for p odd) according to Ogus-Coleman-Urfels
was explained in 4.6.4. In the example of an elliptic curve wi th complex
multiplication by Q[√−3], we have seen that κ∈ Q, hence ω11∈ Q and
H1
dR(A)
Q = H 1
1B(A,
Q).
This is also the case for an elliptic curve with complex multi plication
by Q[√−3n] if the Legendre symbol ( n
3 ) is 1, but probably not in general if
( n
3 ) =−1 (although this happens for n = 8, after the last example in 4.6.4).
