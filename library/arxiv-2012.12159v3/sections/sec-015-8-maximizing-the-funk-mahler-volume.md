---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-015-8-maximizing-the-funk-mahler-volume
section_title: "Maximizing the Funk-Mahler volume"
section_number: 8
pages: 26-34
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
doc_brief: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME — We explore connections furnished by the Funk metric, a relative of the Hilbert metric, between projective geometry, billiards"
---
Let us introduce for convenience ρ = 1−e−r, and the modiﬁed Funk-Mahler
volumes
~Mρ(K,q ) :=rnMr(K,q ) =
∫
z∈q+ρ(K−q)
|Kz|dz, ~Mρ(K) = inf
q∈int(K)
~Mρ(K,q ).
Lemma 8.1. LetB⊂ Rn be an ellipsoid. Then
~Mρ(B) =nω2
n
∫ ρ
0
tn−1dt
(1−t2)
n+1
2
.
Proof. By Lemmas 7.1 and 7.4,
~Mρ(B) = ~Mρ(Bn, 0) =
∫
ρB
|Bz|dz =ωn
∫
ρB
dz
(1−|z|2)
n+1
2
=nω2
n
∫ ρ
0
tn−1dt
(1−t2)
n+1
2
.
□
In light of the discussion in section 7, and inspired by the Blaschke-Santal´ o
and the centro-aﬃne isoperimetric inequalities, we propose a uniﬁed inequality
containing both of the above as limiting cases.
Conjecture 8.2. Fix any 0≤ρ< 1, and let K∈K (Rn) have 0 as its centroid.
i) ~Mρ(K, 0)≤ ~Mρ(Bn).
ii) If ~Mρ(K, 0) = ~Mρ(Bn) then K is an ellipsoid.
This is not to say that ~Mρ(K) = ~Mρ(K, 0): as ρ→ 0, ~Mρ(K,q ) attains its
minimum close to the Santal´ o point ofK, which generally diﬀers from the centroid.
We will prove the conjecture in the restricted class of unconditional convex bod-
ies. To this end, we must expand our discussion to include log-concave functions.
We writefq(•) =f(q +•).
27 A Funk perspective on billiards, projective geometry and Mahler volume
Deﬁnition 8.3. Forf : Rn→ R+ a Borel function, put φ(x) =− logf(x) : Rn→
R∪{ +∞}. Deﬁne for ρ∈ C the Funk-Mahler volumes around 0
~Mρ(f, 0) := 1
n!
∫
z∈Rn
e−φ(z
ρ )
∫
ξ∈Rn
e−Lφz(ξ)dξdz
= 1
n!ρn
∫
Rn×Rn
e−φ(x)−Lφ(ξ)+ρ⟨x,ξ⟩dxdξ,
whenever the integral converges. Deﬁne also
~Mρ(f,q ) := ~Mρ(fq, 0), ~Mρ(f) := inf
q∈Rn
~Mρ(f,q ).
As ρ→ 0,
~Mρ(f, 0)∼ 1
n!ρn
∫
Rn×Rn
e−φ(z)−Lφ(ξ)dxdξ,
which is the functional Mahler product.
Lemma 8.4. It holds that ~Mρ(f, 0) = ~Mρ(λf◦A, 0) for anyλ> 0 andA∈ GLn(R).
Furthermore,~Mρ(f,q ) is a convex function of q, and strictly convex where ﬁnite.
Proof. The ﬁrst statement is immediate from deﬁnition by the GL-equivariance of
the Legendre transform, and since L(φ +c) =Lφ−c.
For the second, observe that
~Mρ(f,q ) = 1
n!
∫
Rn×Rn
e−φ(w
ρ )+⟨ξ,w⟩−Lφ(ξ)e(1−ρ)⟨ξ,q⟩dwdξ,
and note that t↦→e(1−ρ)t is strictly convex. □
The functional Funk-Mahler volumes generalize those previously introduced for
convex bodies, as follows.
Lemma 8.5. ~Mρ(1 K, 0) = ~Mρ(K, 0).
Proof. Recall thatL(− log 1 K)(ξ) =hK(ξ) =‖ξ‖Ko. Thus
~Mρ(1 K, 0) = 1
n!
∫
ρK×Rn
e−‖ξ‖Kz
dzdξ = 1
n!
∫
ρK
dz
∫ ∞
0
rn−1e−rdr
∫
∂Kz
dµKz,
where dξ =rn−1drdµKz. Thus
~Mρ(1 K, 0) = 1
n!(n− 1)!n
∫
ρK
|Kz|dz = ~Mρ(K, 0). □
Using this representation, let us exhibit a curious property of the Funk-Mahler
volume of a convex body, which at present we only formally establish for zonoids.
Proposition 8.6. Assume 0∈ int(K). There is then a continuous extension of
~Mρ(K, 0) to ρ∈ [0, 1)×iR, which is analytic in (0, 1)×iR.
Furthermore if K is a zonoid, then
lim
t→±∞
~Mit(K, 0) =in (2π)n
n! .
Proof. For the ﬁrst statement, put ρ =s +it, write
~Mρ(K, 0) = ~Mρ(1 K, 0) = (s +it)n
n!
∫
K×Rn
e−hK(ξ)+s⟨x,ξ⟩+it⟨x,ξ⟩dxdξ,
28 A Funk perspective on billiards, projective geometry and Mahler volume
and note that
1
n!
∫
K×Rn
e−hK(ξ)+s⟨x,ξ⟩dxdξ = 1
sn
~Ms(K, 0)<∞
for 0≤s< 1.
For the second statement, letF(f)(y) =
∫
Rnf(x)e−i⟨x,y⟩dx be the Fourier trans-
form. Write
~Mit(K, 0) = in
n!tn
∫
Rn×Rn
1 K(x)e−hK(ξ)eit⟨x,ξ⟩dxdξ
= in
n!
∫
Rn
1 K(x
t )F(e−hK)(−x)dx
= in
n!
∫
Rn
e−hK(ξ)
∫
tK
ei⟨x,ξ⟩dxdξ,
and note thatF(e−hK)∈L1(Rn) when K is a zonoid. Thus as t→±∞ ,
~Mit(K, 0)→ in
n!
∫
Rn
F(e−hK) = in
n!(2π)ne−hK(0) =in (2π)n
n! .
□
Motivated by Conjecture 8.2, and inspired by the results of [19], we boldly put
forward the following
Conjecture 8.7. Consider two Borel functions φ,ψ : Rn→ R∪{ +∞} such that
for all x,ξ∈ Rn one has φ(x) +ψ(ξ)≥⟨x,ξ⟩. Assume also
∫
xe−φ(x)dx = 0. Then
for all 0≤ρ< 1,∫
Rn×Rn
e−φ(x)−ψ(ξ)+ρ⟨x,ξ⟩dxdξ≤ (2π)n(1−ρ2)−n
2. (7)
Equality is attained uniquely, up to equality a.e., by the pairs of functions
φ(x) = 1
2⟨Ax,x⟩ +c, ψ (ξ) =Lφ(ξ) = 1
2⟨A−1x,x⟩− c, (8)
for some A> 0 and c∈ R.
We remark that here and in the following, one may restrict attention to dual
pairs of convex functions φ,ψ =Lφ, without loss of generality. In all that follows,
we take a.e.-uniqueness to mean uniqueness up to equality a.e.
Let us check the trivial statement in the conjecture.
Lemma 8.8. Pairs φ,ψ as in (8) give equality in (7).
Proof. Takingq(x) = 1
2|x|2,
Lqz(ξ) =|ξ|2
2 −⟨ξ,z⟩,
and so∫
Rn×Rn
e−|z|2
2ρ2−|ξ|2
2 +⟨ξ,z⟩dξdz =ρn
∫
e− 1
2 (|w|2+|ξ|2−2ρ⟨w,ξ⟩)dξdw
=ρn
∫
e− 1
2 (|w−ρξ|2+(1−ρ2)|ξ|2)dξdw =
∫
e− 1
2|w|2
dw
∫
e− 1
2 (1−ρ2)|ξ|2
dξ
= (2π)nρn(1−ρ2)−n
2.
29 A Funk perspective on billiards, projective geometry and Mahler volume
By Lemma 8.4, we get equality for all pairs as claimed.
□
An immediate corollary is a functional version of Conjecture 8.2, as follows.
Conjecture 8.9. Let f : Rn→ R+ be an integrable Borel function, and assume
also that
∫
xf(x)dx = 0. Then for all 0≤ρ< 1,
~Mρ(f, 0)≤ 1
n!(2π)nρn(1−ρ2)−n
2.
Equality is attained uniquely by multiples of gaussians: f(x) =λe− 1
2⟨Ax,x⟩.
Remark 8.10. Note that the implication Conjecture 8.7 ⇒ Conjecture 8.9 is valid
separately for each n, and also separately for any family of functions with certain
symmetry, such as even or unconditional functions.
We now prove Conjecture 8.7 under the extra assumption of unconditionality.
Recall that φ is unconditional if φ(x1,...,x n) =φ(|x1|,..., |xn|).
Theorem 8.11. Consider two unconditional Borel functionsφ,ψ : Rn→ R∪{+∞}
such that for all x,ξ∈ Rn one has φ(x) +ψ(ξ)≥⟨x,ξ⟩. Then for all 0≤ρ< 1,∫
Rn×Rn
e−φ(x)−ψ(ξ)+ρ⟨x,ξ⟩dxdξ≤ (2π)n(1−ρ2)−n
2.
Equality is attained a.e.-uniquely by Legendre-dual pairs
φ(x) = 1
2⟨Ax,x⟩ +c, ψ (ξ) =Lφ(ξ) = 1
2⟨A−1x,x⟩− c.
Proof. Since φ(x) =φ(−x), the claimed inequality is equivalent to
I :=
∫
Rn×Rn
e−φ(x)−ψ(ξ) cosh(ρ⟨x,ξ⟩)dξdx≤ (2π)n(1−ρ2)−n/2. (9)
The left hand side can be rewritten as
J =
∞∑
j=0
ρ2j
(2j)!
∫
Rn×Rn
e−φ(x)−ψ(ξ)⟨x,ξ⟩2jdxdξ
=
∞∑
j=0
ρ2j
(2j)!
∑
|I|=2j
(2j
I
)∫
Rn
xIe−φ(x)dx
∫
Rn
ξIe−ψ(ξ)dξ,
where the last sum is over alln-tuplesI = (i1,...,i n) of non-negative integers such
that|I| :=∑n
ν=1iν = 2j, and we use the notation xI :=∏n
ν=1xiν
ν , and
(2j
I
)
:= (2j)!
i1!··· in!
for the multinomial coeﬃcient.
Observe that by unconditionality, if I contains an odd index then the corre-
sponding integrals vanish. Therefore,
J =
∞∑
j=0
ρ2j
(2j)!
∑
|I|=j
(2j
2I
)∫
Rn
x2Ie−φ(x)dx
∫
Rn
ξ2Ie−ψ(ξ)dξ (10)
= 4n
∞∑
j=0
ρ2j
(2j)!
∑
|I|=j
(2j
2I
)∫
Rn
+
x2Ie−φ(x)dx
∫
Rn
+
ξ2Ie−ψ(ξ)dξ.
30 A Funk perspective on billiards, projective geometry and Mahler volume
Making the change of coordinates x = eu := (eui)n
i=1, ξ = ev = (evi), we may
write ∫
Rn
+
e−φ(x)x2Idx
∫
Rn
+
e−ψ(ξ)ξ2Idξ =
∫
Rn
f(u)du
∫
Rn
g(v)dv, (11)
where f(u) =e−φ(eu)e⟨2I+1,u⟩, g(v) =e−ψ(ev)e⟨2I+1,v⟩, and I +c := (iν +c)n
ν=1.
Denote
h(w) =e− 1
2|ew|2
e⟨2I+1,w⟩, w ∈ Rn,
where|ew| =
√∑n
i=1e2wi. Since φ(x) +ψ(ξ)≥⟨x,ξ⟩, we immediately ﬁnd that
f(u)g(v)≤h
(u +v
2
)2
,
and by the Prekopa-Leindler inequality we have
∫
Rn
f
∫
Rn
g≤
(∫
Rn
h
)2
=
(∫ ∞
0
e−|p|2
2 p2Idp
)2
=
n∏
ν=1
(∫ ∞
0
e−t2
2 t2iνdt
)2
=
(√
2π
2
)2n n∏
ν=1
((2iν− 1)!!)2 = (2π)n
4n
n∏
ν=1
((2iν− 1)!!)2.
Combined with (9), (10), (11), it remains to verify that
∞∑
j=0
ρ2j
(2j)!
∑
|I|=j
(2j
2I
) n∏
ν=1
((2iν− 1)!!)2 = (1−ρ2)−n/2,
or equivalently
∞∑
j=0
ρ2j ∑
|I|=j
(2j
2I
) n∏
ν=1
(2iν− 1)!!
(2iν)!! = (1−ρ2)−n/2.
By Newton’s binomial formula,
(1−ρ2)− 1
2 =
∞∑
i=0
(−1/2
i
)
(−1)iρ2i =
∞∑
i=0
(2i− 1)!!
2ii! ρ2i =
∞∑
i=0
(2i− 1)!!
(2i)!! ρ2i,
and it remains to raise both sides to power n.
For equality, we must have an equality at each application of Prekopa-Leindler,
which is characterized in [12]. Namely for each I, one has a.e. equalities f =
λh(• +C), g = λ−1h(•− C). Already for a single multi-index I this forces the
existence of a diagonal matrix A and c∈ R such that a.e. one has
φ(x) = 1
2⟨Ax,x⟩ +c, ψ (ξ) = 1
2⟨A−1x,x⟩− c.
□
By the previous discussion, we immediately get
Corollary 8.12. For all unconditional Borel functions f : Rn→ R+ it holds that
~Mρ(f, 0)≤ 1
n!(2π)nρn(1−ρ2)−n
2,
with equality attained a.e.-uniquely byf(x) =λe− 1
2⟨Ax,x⟩ with some diagonal matrix
A> 0 and scalar λ> 0.
31 A Funk perspective on billiards, projective geometry and Mahler volume
Proof. Follows directly from Theorem 8.11, since ~Mρ(f, 0) = ~Mρ(f) by uncondi-
tionality and the second part of Lemma 8.4. □
In particular, we proved a functional inequality of independent interest.
Corollary 8.13. Consider an unconditional Borel function f = e−φ : Rn→ R+.
Then
I2j(f) :=
∫
Rn×Rn
⟨x,ξ⟩2je−φ(x)−Lφ(ξ)dxdξ≤ (2π)n (n− 2 + 2j)!!
(n− 2)!!(2j− 1)!!.
Equality is attained a.e.-uniquely by multiples of gaussians f(x) = λe− 1
2⟨Ax,x⟩, for
some diagonal A> 0 and scalar λ> 0.
The case of j = 0 is the Blaschke-Santal´ o inequality for unconditional functions.
The case of j = 1 was established previously in [17].
Proof. Denote ψ =Lφ. In the proof of Theorem 8.11, we have seen that I2j(e−φ)
is maximized a.e.-uniquely by multiples of gaussians. The maximal value I2j(G)
can be computed directly, or alternatively it can be deduced from Theorem 8.11 as
follows. We have
∞∑
j=0
ρ2j
(2j)!I2j(G) = (2π)n(1−ρ2)−n/2,
and by Newton’s binomial
(1−ρ2)−n
2 =
∞∑
j=0
(−n/2
j
)
(−1)jρ2j =
∞∑
i=0
(n + 2j− 2)!!
(n− 2)!!(2j)!!ρ2j.
Consequently,
I2j(G) = (2π)n(2j)! (n + 2j− 2)!!
(n− 2)!!(2j)!! = (2π)n (n− 2 + 2j)!!
(n− 2)!!(2j− 1)!!.
□
We can now deduce the corresponding inequalities for unconditional convex bod-
ies. Deﬁne
I2j(K) :=
∫
K×Ko
⟨x,ξ⟩2jdxdξ.
First, we prove two simple relations.
Lemma 8.14. For any convex body K∈K 0(Rn),
I2j(K) = 1
((n + 2j)!!)2
( 2
π
) 1
2 (1−(−1)n)
I2j(e− 1
2‖x‖2
K). (12)
If K =−K then
~Mρ(K) =
∞∑
j=0
(n + 2j
n
)
I2j(K)ρn+2j. (13)
Proof. We will use the change of variables x =tp, ξ =sη, with p∈∂K,η ∈∂Ko.
We havedx =rn−1drdµK(p),dξ =sn−1dsdµKo(η).
We may write
32 A Funk perspective on billiards, projective geometry and Mahler volume
I2j(e− 1
2‖x‖2
K) =
∫
Rn×Rn
⟨x,ξ⟩2je−
‖x‖2
K
2 e−
‖ξ‖2
Ko
2 dxdξ
=
∫
[0,∞)2
e−r2
2−s2
2 rn+2j−1sn+2j−1drds
∫
∂K×∂Ko
⟨p,η⟩2jdµK(p)dµKo(η)
=
(∫ ∞
0
rn+2j−1e−r2/2dr
)2∫
∂K×∂Ko
⟨p,η⟩2jdµK(p)dµKo(η)
= 2n+2j−2Γ(n
2 +j)2
∫
∂K×∂Ko
⟨p,η⟩2jdµK(p)dµKo(η).
On the other hand,
I2j(K) =
∫
K×Ko
⟨x,ξ⟩2jdxdξ
=
∫
∂K×∂Ko
⟨p,η⟩2jdµK(p)dµKo(η)
∫
[0,1]2
rn+2j−1sn+2j−1drds
= 1
(n + 2j)2
∫
∂K×∂Ko
⟨p,η⟩2jdµK(p)dµKo(η),
and it remains to combine the two equalities to ﬁnd
I2j(K) = 1
2n+2j−2(n + 2j)2Γ(n
2 +j)2I2j(e− 1
2‖x‖2
K)
= 1
((n + 2j)!!)2
( 2
π
) 1
2 (1−(−1)n)
I2j(e− 1
2‖x‖2
K).
Now assume K =−K. By Lemmas 8.5 and 7.1,
~Mρ(K) = ~Mρ(K, 0) = ~Mρ(1 K, 0) =ρn
n!
∫
K×Rn
e−‖ξ‖Ko+ρ⟨x,ξ⟩dxdξ
= ρn
n!
∫
K×Rn
e−‖ξ‖Ko
cosh(ρ⟨x,ξ⟩)dxdξ
=
∞∑
j=0
1
n!(2j)!ρn+2j
∫
K×Rn
⟨x,ξ⟩2je−‖ξ‖Ko
dxdξ.
We may write
I2j(K) =
∫
K×Ko
⟨x,ξ⟩2jdxdξ =
∫
K×∂Ko
⟨x,η⟩2jdxdµKo(η)
∫ 1
0
s2j+n−1ds
= 1
n + 2j
∫
K×∂Ko
⟨x,η⟩2jdxdµKo(η).
Therefore,
∫
K×Rn
⟨x,ξ⟩2je−‖ξ‖Ko
dxdξ =
∫
K×[0,∞)×∂Ko
s2j+n−1e−s⟨x,η⟩2jdxdsdµKo(η)
= (2j +n− 1)!
∫
K×∂Ko
⟨x,η⟩2jdxdµKo(η)
= (2j +n)!I2j(K),
33 A Funk perspective on billiards, projective geometry and Mahler volume
and so
~Mρ(K) =
∞∑
j=0
(n + 2j)!
n!(2j)! ρn+2jI2j(K).
□
Corollary 8.15. ForK⊂ Rn convex and unconditional,
I2j(K) :=
∫
K×Ko
⟨x,ξ⟩2jdxdξ≤ (2π)n
n + 2j
1
(n + 2j)!!(n− 2)!!(2j− 1)!!
( 2
π
) 1−(−1)n
2
.
Equality is attained uniquely by ellipsoids.
Proof. We apply Corollary 8.13 tof(x) =e−φ(x) =e− 1
2‖x‖2
K. By eq. (12), I2j(K) is
uniquely maximized by ellipsoids, and the maximal value is readily computed. □
Corollary 8.16. For any 0≤ r <∞, and K ⊂ Rn convex and unconditional,
Mr(K)≤Mr(Bn). Equality is attained uniquely by ellipsoids.
Proof. We only need to note that by Corollary 8.15, each summand of (13) is
uniquely maximized by ellipsoids. □
Proof of Corollary 3. Since dH = 1
2(dF +dRF )≥ 1
2dF , it follows thatBH
r (q,K )⊂
BF
2r(q,K ). Write cn for a constant depending only on n which may change between
occurrences. By Proposition 7.6 we have vol F (BF
R(q,Bn))≤ cne
n−1
2 R. Using the
Rogers-Shephard inequality as in the proof of Corollary 3.12, and applying Corollary
8.16, we ﬁnd
volH
K(BH
r (q,K ))≤cn volF
K(BH
r (q,K ))≤cn volF
K(BF
2r(q,K ))≤cn volF
K(BF
2r(q,Bn))
≤cne
n−1
2 2r =cne(n−1)r,
completing the proof. □
Using the same methods as before, we can also show the following.
Theorem 8.17. Letf =e−φ : Rn
+→ R+ be a Borel function. Then
• For all j≥ 0,
I+
j (f) :=
∫
Rn
+×Rn
+
⟨x,ξ⟩je−φ(x)−Lφ(ξ)dxdξ≤I+
j (e−|x|2
2 ).
• If n = 1,
I+
2j+1(f) =
∫ ∞
0
x2j+1e−φ(x)dx
∫ ∞
0
ξ2j+1e−Lφ(ξ)dξ≤ (2j)!!2.
• For all 0≤ρ< 1,∫
R+×R+
e−φ(x)−Lφ(ξ) sinh(ρxξ)dxdξ≤ 1√
1−ρ2 arctan ρ√
1−ρ2.
Equality in all cases is a.e.-uniquely attained by λe− 1
2⟨Ax,x⟩, where A > 0 is
diagonal and λ> 0.
Proof. The ﬁrst two inequalities can be obtained by trivially adjusting the proof of
Theorem 8.11. For the last inequality, we should show that
∞∑
j=0
(2j)!!2
(2j + 1)!ρ2j+1 =
∞∑
j=0
(2j)!!
(2j + 1)!!ρ2j+1 = 1√
1−ρ2 arctan ρ√
1−ρ2.
34 A Funk perspective on billiards, projective geometry and Mahler volume
This can be done by observing that
(2j)!!
(2j + 1)!! =
∫ π/2
0
sin2jtdt,
and so
∞∑
j=0
(2j)!!
(2j + 1)!!ρ2j+1 =
∫ π
2
0
(ρ sint)2j+1dt =
∫ π
2
0
ρ sint
1−ρ2 sin2tdt
=
∫ 1
0
2ρds
s2 + 2(1− 2ρ2)s + 1
= 1√
1−ρ2
(
arctan
√
1−ρ2
ρ − arctan 1− 2ρ2
2ρ
√
1−ρ2
)
= 1√
1−ρ2 arctan ρ√
1−ρ2.
Equality cases are settled using [12] as in Theorem 8.11. □
As a sidenote, the discussion above suggests an extension of the centro-aﬃne
surface area to functions.
Deﬁnition 8.18. Letf : Rn→ [0,∞) be a Borel function. Its centro-aﬃne surface
area is
Ωn(f) := 1
n! lim sup
ρ→1−
(1−ρ2)n/2
∫
Rn×Rn
e−φ(x)−Lφ(ξ)+ρ⟨x,ξ⟩dxdξ.
Evidently, Ωn(f) = Ωn(λf◦A) for any λ> 0 and A∈ GLn(R).
