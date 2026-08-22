---
doc_id: zagier-the-dilogarithm-function
doc_title: "The dilogarithm function"
section_id: sec-050-2-an2bnc
section_title: "An2+Bn+C)"
section_number: 2
pages: 51-52
source_pdf: zagier-the-dilogarithm-function.pdf
source_sha256: 05079cf525c6ba0f
doc_brief: "The dilogarithm function — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
---
= −Aε
2
( log(1/Q)
ε −ν
) 2
− Bε
( log(1/Q)
ε −ν
)
= −log(Q) log(1−Q)
2ε +
(
B−νA) logQ +
(
−Aν2
2 +Bν
)
ε,
w h e r ew eh a v eu s e dAlog(Q) = log(1 −Q). Together with the lemma this
gives
log
( q
1
2 An2+Bn+C
(q)n
)
= L(1)−L(Q)
ε − 1
2 log 2π
ε + log QB
√1−Q
−
( ∆
1−Q
ν2
2 −
(
B + 1
2
Q
1−Q
)
ν + 1
24
1+Q
1−Q
)
ε−
∞∑
r=3
Br(ν)L i2−r(Q)εr−1
r!
54 Don Zagier
with ∆ = A +Q−AQ as before. If we write this as log ϕ(ν) where ϕ is
a smooth function of rapid decay, then FA,B(q) equals ∑
ν≡ν0 (mod 1) ϕ(ν),
which by the Poisson summation formula can be written as∑
r∈Z~ϕ(r)e2πirν0
where~ϕ is the Fourier transform of ϕ. The smoothness of ϕ implies that all
terms except r = 0 give contributions which are O( εN ) for all N> 0a s
ε→ 0. We therefore obtain the asymptotic expansion
FA,B
(
e−ε)
= QB
√
∆
· exp
( L(1)−L(Q)
ε − 1+Q
1−Q
ε
24
)
·I
[
exp
((
B + 1
2
Q
1−Q
)
uε−
∞∑
r=3
Br(u)L i2−r(Q)εr−1
r!
)]( 1−Q
∆ε
)
,
where I
[]
is the functional deﬁned formally by the integral transform
I
[
H(u)
](
t
)
= 1√
2πt
∫∞
−∞
e−u2/2tH(u)du, (39)
and explicitly at the level of power series by
I
[ ∞∑
n=0
cnun
](
t
)
∼
∞∑
n=0
(2n− 1)!!c2n tn , (40)
where (2n−1)!! = (2n)!/2nn! as usual. It is not immediately obvious why this
expansion makes sense, since the argument of the functional grows like 1/ε as
ε→ 0, but the power series to which it is applied has the property that the
coeﬃcient ofun is O(ε2n/3) for every n≥ 0, and since the functionalI
[]
has
the scaling property I
[
H(λu)
]
(t)= I
[
H(u)
]
(λ2t), the ﬁnal expression does
indeed involve only positive powers ofε. (Choose λ =εc with 1
2 <c< 2
3 .)
(c) The third method, which is based on a clever application of Cauchy’s
theorem going back originally to an old paper of Meinardus [26], was ﬁrst
used in this context by Nahm, Recknagel and Terhoeven [31] and is also the
one used in Nahm’s paper [30] in this volume, so that we will only indicate
the main idea of the method here. We writeFa,b(q)a s
FA,B(q)= Cx0
[( ∞∑
n=−∞
q
1
