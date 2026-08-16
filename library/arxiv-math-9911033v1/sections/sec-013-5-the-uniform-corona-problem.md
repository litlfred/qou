---
doc_id: arxiv-math-9911033v1
doc_title: "ON THE LOWER BOUND ESTIMA TES OF SECTIONS OF THE CANONICAL BUNDLES OVER A RIEMANN SURF ACE ZHIQIN LU Contents 1. Introductions 1 2. A lower bound estimate 4 3. A counterexample 11 "
section_id: sec-013-5-the-uniform-corona-problem
section_title: "The uniform corona problem"
section_number: 5
pages: 24-28
source_pdf: 9911033v1.pdf
source_sha256: 196c05d2e3419565
doc_brief: "ON THE LOWER BOUND ESTIMATES OF SECTIONS OF THE CANONICAL BUNDLES OVER A RIEMANN SURFACE ZHIQIN LU Contents 1. Introductions 1 2. A lower bound estimate 4 3. A counterexample 11 4. Partial uniform est"
---
Let M be a Riemann surface of genus g ≥ 2. It is well known that the
coordinate ring ⊕∞
m=0H 0(M,K m
M ) is ﬁnitely generated. That is, there is an
m0> 0 such that for any m> 0 and S ∈H 0(M,K m
M ),S can be represented
by
S =
d∑
i=1
UiTi,(5.1)
where Ui ∈ H 0(M,K m0
M ) and Ti ∈ H 0(M,K m−m0
M ) for i = 1 , · · ·,d =
dimH 0(M,K m0
M ). Finding a suitable set of {Ti}i=1, ··· ,d is called the corona
problem(cf. [4]).
We need to consider the case where M approaches to the boundary of
the moduli space in the Teichm¨ uller theory. So in addition t o the existence
24
of Ui and Ti, we need some uniform estimates. In this section, we give the
uniform estimate for the corona problem on Riemann surfaces .
Theorem 5.1. LetM be a Riemann surface of genus g and constant cur-
vature (−1). Then there is an m0 > 0 such that for any m > m0 and
S ∈H 0(M,K m
M ), there is a decomposition
S =
d∑
i=1
Si
of Si ∈H 0(M,K m
M )(i = 1, · · ·,d ) such that
||Si||L2 ≤C(m,m 0,g )||S||L2
||Si||L∞ ≤C(m,m 0,g )||S||L∞
(5.2)
for i = 1, · · ·d, and
Si =TiUi
for a basis U1, · · ·,U d of H 0(M,K m0
M ) and T1, · · ·,T d ∈H 0(M,K m−m0
M ).
Remark 5.1. An estimate on Ti(i = 1, · · ·,d ) alone is not expected because
of the counterexample in §3, where ∑ ||Ui||2 can be arbitrarily small.
Throughout this section, we will use the notation D1,D 2, · · · to denote
the constants depending only on m0 and the genus g. We also use A ≤∼B
to mean that there is a positive constant C =C(m0,g ), depending only on
m0 and g such that A ≤CB . Likewise, we use A ≥∼B to denote the fact
A ≥CB for some constant C =C(m0,g ).
The idea of the proof is that, if the injective radius of M is greater than an
absolute constant, then ∑ ||Ui||2 has a lower bound by an absolute positive
constant. In this case, we can solve the corona problem exact ly using the
method in [4]. So we just need to prove the theorem in the case w hereinj(M )
is arbitrarily small. By the collar theorem, we know that in t his case, there
are ﬁnite many collars Cδ1, · · ·,C δs (with maxδi small) embedded in M and
they do not intersect each other. By Proposition 4.1, outsid e the collars, the
injective radius has an absolute lower bound. Special care m ust be taken
for the sections over these collars. In order to take care of t he collars to get
the estimates, we ﬁrst ﬁx a collar Cδ embedded in M with the parameter δ
small. We will use all the notations about collars in § 3. For any ˜R> 0, let
Cδ( ˜R) = {x||ρ| ≤ ˜R}.
In particular, Cδ =Cδ(R) with δ sinhR =ε1.
We choose and ﬁx a number m0 > 0 such that K m0
M is very ample. Let ˜η
be the cut-oﬀ function of M deﬁned as
˜η =



η(ρ − (R − 1)) ρ ≥ 0 and x ∈Cδ,
η(−ρ − (R − 1)) ρ< 0 and x ∈Cδ,
0 otherwise,
(5.3)
25
where the function η is deﬁned in (2.10). Let
u1 = 1√
δ
˜η(dz)m0(5.4)
be a section of K m0
M overM using this cut-oﬀ function, where dz is deﬁned
in (3.3). We can check that
{
||
∂u 1||2 ≤ 4
δ(cosh ρ)2m0 R − 1 ≤ |ρ| ≤ R,
∂u 1 = 0 otherwise.
Thus∫
M
||∂u 1||2 ≤ 2
∫ R
R−1
4
δ(coshρ)2m0
coshρδdρ ≤ 8
(cosh(R − 1))2m0−1.
By Proposition 2.1, there is a section u of K m0
M such that
∂u =∂u 1
with ∫
M
||u||2 ≤ 1
m0 − 1
∫
M
||∂u 1||2 ≤ 8
(m0 − 1)(cosh(R − 1))2m0−1.
By using (4.1), we see that ∫
M
||u||2 ≤∼δ2m0−1.(5.5)
Let
U ′ =u1 −u.(5.6)
Then
∂U ′ = 0.
Lemma 5.1. LetU ′′ be a holomorphic section of K m0
M on Cδ(R) such that
(U ′′,u 1)Cδ (R−2) = 0. That is,
∫
Cδ (R−2)
<U ′′,u 1 >= 0,(5.7)
whereu1 is the section deﬁned in (5.4). Then there is an absolute constant
ε6 > 0 such that
||U ′′|| ≤∼ e−ε6eR−| ρ |+m0(R−|ρ|)||U ′′||L2(Cδ ),(5.8)
and
||∇U ′′|| ≤∼ e−ε6eR−| ρ |+(m0+1)(R−|ρ|)||U ′′||L2(Cδ ).(5.9)
We use the notation in § 3. Let
w1 =e
2π √
− 1
δ θ− 4π
δ (arctan eρ −arctan e− (R− 2)),
w2 =e− 2π √ − 1
δ θ+ 4π
δ (arctan eρ −arctan eR− 2).
Let
U ′′ = (g1(w1) +a +g3(w2))(dz)m0
26
be the decomposition similar to that in (3.4) where g1(w1) and g2(w2) are
holomorphic functions of w1 and w2 respectively,g1(0) = g2(0) = 0, a is a
constant, and dz is deﬁned in (3.3).
Using (5.7), we see that a = 0. By the Schwartz Lemma, we have
|g1(w1)| ≤ |w1| max
|w1|=1
|g1(w1)|.(5.10)
At each point of {|w1| = 1 } or {ρ = R − 2}, by the collar theorem, there
is an absolute lower bound for the injective radius. Thus by t he Cauchy
integral formula, we have
max
|w1|=1
||g1(dz)m0 || ≤∼ ||g1(dz)m0 ||L2(Cδ ).(5.11)
Using (5.10) and (5.11), we have
||g1(dz)m0 || ≤ e− 4π
δ (arctan eρ −arctan e− (R− 2)) (coshR)m0
(coshρ)m0
||g1(dz)m0 ||L2(Cδ ).
(5.12)
It is elementary to check that there is an absolute constant ε6 > 0 such that
e− 4π
δ (arctan eρ −arctan e− (R− 2)) ≤e−ε6eR−| ρ |
.(5.13)
Combining (5.12) and (5.13),
||g1(dz)m0 || ≤∼ e−ε6eR−| ρ |+m0(R−|ρ|)||g1(dz)m0 ||L2(Cδ ).(5.14)
Similarly, we have
||g2(dz)m0 || ≤∼ e−ε6eR−| ρ |+m0(R−|ρ|)||g2(dz)m0 ||L2(Cδ ).(5.15)
(5.14) and (5.15) give the inequality (5.8).
On the other hand, a straightforward computations gives
∇U ′′ = ( 2π √
−1
δ (w1g′
1 +w2g′
2)
− 1
2m0
√
−1 sinhρ(g1 +g2))(dz)m0 ⊗dz.
(5.16)
Using the same argument as above, we get (5.9).
Lemma 5.2. With the notations as above, there is a constant r > 2, de-
pending only on m0 and the genus g, such that U ′ ⁄= 0 on Cδ(R −r), where
U ′ is deﬁned in (5.6).
Proof. By (5.6), we know that u is holomorphic on Cδ(R − 2). Let
u =u′ +αu 1(5.17)
be the decomposition of u such that (u′,u 1)Cδ (R−2) = 0 and α is a constant.
Then ∫
M
||u||2 ≥
∫
Cδ (R−2)
||u′||2 +
∫
Cδ (R−2)
|α |2||u1||2.(5.18)
27
In particular
∫
Cδ (R−2)
||u||2 ≥ |α |2
∫ R−2
−(R−2)
1
(coshρ)2m0−1dρ.(5.19)
By (5.5) and (5.19), we have
|α | ≤∼ δm0− 1
2.(5.20)
On the other hand, by Lemma 5.1,
||u′|| ≤∼ e−ε6eR−| ρ |+m0(R−|ρ|)δm0− 1
2.(5.21)
Thus by (5.4), (5.20) and (5.21), there are constants D1 and D2 such that
||U ′(x)|| ≥ 1
√
δ(coshρ)m0
(1 −D1δm0− 1
2 )
−D2e−ε6eR−| ρ |+m0(R−|ρ|)δm0− 1
2
(5.22)
for |ρ| < R− 3. If r is large enough, then ||U ′(x)|| > 0 for |ρ| < R−r. In
particular U ′ ⁄= 0 on Cδ(R −r). This completes the proof of the lemma.
Now we assume the general case. Let Cδ1, · · ·,C δs be the collars of param-
eters δ1, · · ·,δ s respectively embedded into M . We assume that Cδi, (i =
1, · · ·,s ) do not intersect each other. By Lemma 5.2, there are Ri, (i =
1, · · ·,s ) such that we can ﬁnd U ′
i ∈ H 0(M,K m0
m ), (i = 1 , · · ·,s ) with
U ′
i|Cδi (Ri) ⁄= 0. Let ρi,dz i, (i = 1, · · ·,s ) be deﬁned in § 3 coresponding
to Cδi(i = 1, · · ·,s ), respectively. Let
ηi =



η(ρi − (Ri − 1)) ρi ≥ 0 and x ∈Cδi
η(−ρi − (Ri − 1)) ρi ≤ 0 and x ∈Cδi
0 otherwise
be the cut-oﬀ functions for i = 1, · · ·,s . Assume that max δi is small enough.
Then by Lemma 5.2, U ′
1, · · ·,U ′
s ∈H 0(M,K m0
M ) have the following proper-
ties
1. ||U ′
i || ≥∼ 1
√δi
e−m0|ρi| on Cδi(Ri) for i = 1, · · ·,s (by (5.22));
