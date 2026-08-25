---
doc_id: aif-2009-59-1-347-0
doc_title: "On q-summation and confluence"
section_id: sec-011-3-the-divergent-q-euler-series
section_title: "The divergent q-Euler series"
section_number: 3
pages: 29-31
source_pdf: AIF_2009__59_1_347_0.pdf
source_sha256: 35b8422990e24888
doc_brief: "On q-summation and confluence — 18 sections: Introduction; Part 1. Convergent q-Borel and q-L; Convergent q-Euler series"
---
Since q >1, the q-Euler series
ˆEq(x) =
∑
n/greaterorequalslant0
(−1)n[n]!
qxn+1
is obviously divergent for anyx ∈ C∗, as the Euler series∑
n/greaterorequalslant0(−1)nn!xn+1.
The corresponding q-diﬀerence equation is
x2dqy +y =x.
3.1. Deﬁnition of diﬀerent sums of the q-Euler series
Let us consider the q-Borel transforms of ˆEq(x) (for the general deﬁni-
tion,cf. §4.1):
ψ(ξ) := 1
1 +ξ and φ(ξ) := Ep(ξ).
In the following, we will identify Ep(ξ) to its analytic continuation on C \
((p − 1)qN). For any d ∈ (−π,π ) and λ /∈ −pZ, we set:
(3.1) E d
q (x) = q − 1
lnq
∫ eid∞
0
ψ(ξ)
eq(q ξ
x )
dξ, argx ∈ (d −π,d +π);
(3.2) E [λ]
q (x) = q
1 −p
∫
λpZ
ψ
(
ξ
1−p
)
eq
(
q ξ
(1−p)x
)dpξ, x /∈ (p − 1)λqZ;
(3.3) Ed
q (x) = q
lnq
∫ eid∞
0
φ(ξ)
θp(q ξ
x )
dξ, argx ∈ (d −π,d +π);
(3.4) E[λ]
q (x) = q
1 −p
∫
λpZ
φ(ξ)
θp(q ξ
x )
dpξ, x /∈ (p − 1)λqZ;
Proposition 3.1. — (1) The functions E d
q and Ed
q can be analytically
continued on the sector {| argx| < 2π} of the Riemann surface of the
logarithm.
(2) The functions E [λ]
q andE[λ]
q are analytic on C∗ \(−(1−p)λqZ), the point
−(1 −p)λqn being a simple pole for any integer n ∈ Z.
Proof. — The functions E d
q andEd
q are a priori deﬁned for | argx−d|<π
and d varies in (−π,π ). The second assertion is straightforward. □
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE 375
We will denote by Eq and Eq the analytic continuation of E d
q and Ed
q ,
respectively, on the open sector V (−2π, 2π) := {x ∈ ˜C∗ : | argx|< 2π} on
the Riemann surface of the logarithm. We recall the following result:
Proposition 3.2 ([15, Thm. 2.1] and [ 23, Thm. 1.3.2]) . — The func-
tion Eq(x) (resp. E [λ]
q ) admits ˆEq(x) as q-Gevrey asymptotic expansion at
x = 0 in the sector {argx < 3π/2}. In particular they are solution of
x2dqy +y =x.
The following theorem is about the comparison between the four sum-
mations of ˆEq we have just introduced:
Theorem 3.3. — Eq(x) = Eq(x) and E [λ]
q (x) = E[λ]
q (x).
First, we need to prove the following two lemmas.
Lemma 3.4. — For any x ∈ C such that argx ∈ (−2π, 0) we have:
(3.5) Eq(xe2πi) − Eq(x) = Eq(xe2πi) −Eq(x) = −2πiq − 1
lnq
1
eq(− q
x ).
In particular: Eq(xe2πi) −Eq(xe2πi) = Eq(x) −Eq(x).
Proof. — A variable change in the integral deﬁning E d
q (resp.Ed
q ) shows
that E d
q (xe2πi) = E d−2π
q (x) (resp. Ed
q (xe2πi) = Ed−2π
q (x)). We are reduced
to calculate E d−2π
q (x) − E d
q (x) and hence to calculate a residue at ξ = −1.
In an analogous way, using formula ( 1.1), we obtain
Ed
q (xe2πi) −Ed
q (x) = −q2πi
lnq
∑
n/greaterorequalslant0
Resξ=(p−1)qn

 Ep(ξ)
θp
(
q ξ
x
)


= −q(p − 1)2πi
lnq
∑
n/greaterorequalslant0
qn(pn+1;p)∞
θp
(
q (p−1)qn
x
)
= q(p − 1)2πi
lnq
(p;p)∞
θp
( 1−q
x
)
∑
n/greaterorequalslant0
pn(n−1)/2
(p;p)n
= −q(p − 1)2πi
lnq
(
p, − x
q−1 ;p
)
∞
θp
( 1−q
x
) .
The Jacobi triple product formula for θp immediately allows to conclude.
□
Lemma 3.5. — Let us consider the homogenous q-diﬀerence equation
(3.6) x2dqy =y.
TOME 59 (2009), F ASCICULE 1
376 Lucia DI VIZIO & Changgui ZHANG
Let y0 be a meromorphic solution of (3.6) on the domain Ω = {0< |x|<
R}. Suppose that one of the following hypotheses is veriﬁed:
• the function y0 is analytic on Ω;
• there exists µ ∈ C∗ such that µ /∈ (1 −p)pN and such that the
function y0 has only simple poles contained in the set µpN;
then y0 is identically zero.
Proof. — Notice that 1/ep(q/x) is a uniform solution to ( 3.6). Hence,
there exists a q-invariant function K(x) such that y0(x) = K(x)/ep(q/x).
Identifying K(x) to an elliptic function, one ends the proof noticing that
(1 −p)pZ is the only spiral of poles of ep(q/x). □
Proof of Theorem 3.3. — Lemma 3.4 implies thathd(x) := Ed
q (x)−E d
q (x)
is an analytic solution of ( 3.6) on C∗. We deduce from Lemma 3.5 that
hd ≡ 0.
The diﬀerence E[λ]
q (x) − E [λ]
q (x) has only simple poles on −λ(1 −p)qZ.
Since λ /∈ −pZ we conclude applying Lemma 3.5. □
