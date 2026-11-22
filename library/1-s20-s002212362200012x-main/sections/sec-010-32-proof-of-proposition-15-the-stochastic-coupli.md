---
doc_id: 1-s20-s002212362200012x-main
doc_title: "Journal of Functional Analysis Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-010-32-proof-of-proposition-15-the-stochastic-coupli
section_title: "Proof of Proposition 15: the stochastic coupling"
section_number: 3.2
pages: 15-19
source_pdf: 1-s2.0-S002212362200012X-main.pdf
source_sha256: 6fc7d28c8d40bf42
toc_source: outline
doc_brief: "Journal of Functional Analysis Log concavity and concentration of Lipschitz functions on the Boolean hypercube — V Article history: Received 17 December 2020 Accepted 13 January 2022 Available online"
---
Proposition 15 will be proven via a coupling argument laid out below, which is a 
variant of the standard reﬂection coupling of Brownian motions. Let v ∈Rn and consider 
the process
w0 = v,
dwt = dBt + aν(wt)dt.
(21)
According to Proposition 11, we have that limt→∞aν(wt) ∼τvν. This gives rise to 
the following coupling. Let Ut be a process adapted to Ft such that for all t, Ut is an 
orthogonal matrix. Let ε > 0 and θ ∈Sn−1, and consider the additional process deﬁned 
by the equation
u0 = v + εθ,
dut = UtdBt + aν(ut)dt.
(22)
The existence and uniqueness of the solution will be justiﬁed at the end of the section. 
Similarly to the above, we have limt→∞aν(ut) ∼τv+εθν, and therefore
W1(τvν, τv+εθν) =
sup
˜ϕ∈Lip(Cn)
E
	
˜ϕ

lim
t→∞aν(wt)

−E
	
˜ϕ

lim
t→∞aν(ut)


≤E
 lim
t→∞aν(wt) −lim
t→∞aν(ut)

1

≤√nE
 lim
t→∞aν(wt) −lim
t→∞aν(ut)

2

.
Consider the stopping time
τ := inf{t;
ut = wt}
and the event E := {τ ≤1}. By setting Ut = In for all t ≥τ, we get that aν(wt) = aν(ut)
for all t ≥τ almost surely, and therefore
E holds
⇒
lim
t→∞|aν(wt) −aν(ut)| = 0.
Moreover, since aν(wt) is a martingale (as follows from part 2 of Proposition 10), we 
have
16
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
E
	aν(wt) −lim
s→∞aν(ws)

 Ft

≤

E
aν(wt) −lim
s→∞aν(ws)

2 Ft

=

Tr

Cov(τwtν)

=

Tr(Aν(wt)),
where the ﬁrst equality uses the fact that lims→∞aν(ws)|Ft has the law τwtν, which 
follows from Proposition 11. Combining the above displays and using the triangle in-
equality, we conclude that for all t ≥1,
W1(τvν, τv+εθν) ≤√nE

1EC
 lim
t→∞aν(wt) −lim
t→∞aν(ut)

2

≤√nE
	
|aν(wt) −aν(ut)|

+ E
	
1EC

nTr(Aν(wt)) +

nTr(Aν(ut))

.
(23)
We estimate every term on the right hand side separately, beginning with the ﬁrst one. 
According to equation (9), we have almost surely,
|aν(ut) −aν(wt)| ≤β|ut −wt|.
(24)
Using equation (21) and (22), and by Itô’s formula, we have
d|ut −wt|2 = 2⟨ut −wt, dut −dwt⟩+ Tr

(Ut −In)2
dt
= 2⟨ut −wt, (Ut −In)dBt⟩+ 2⟨ut −wt, aν(ut) −aν(wt)⟩dt
+ Tr

(Ut −In)2
dt.
(25)
Set
Wt =
t

0

 ut −wt
|ut −wt|, dBt

,
∀t ≤τ.
Observe that Wt is a standard Wiener process up to the time τ. Finally, for all t < τ, 
choose
Ut = In −2
 wt −ut
|wt −ut|
 ⊗2
,
the reﬂection about the axis spanned by wt −ut. We have, by deﬁnition,
⟨wt −ut, (In −Ut)dBt⟩= 2|ut −wt|dWt.
Consequently, equation (25) can be written
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
17
d|ut −wt|2 = 4|ut −wt|dWt + 4dt + Stdt
where
St = 2⟨ut −wt, aν(ut) −aν(wt)⟩
(24)
≤2β|ut −wt|2.
Now deﬁne Yt = |ut −wt|. Invoking Itô’s formula again, we have that up to time τ, one 
has
dYt = d

|ut −wt|2
2|ut −wt|
−d

|ut −wt|2
t
8|ut −wt|3
= 2dWt +
St + 4
2|ut −wt|dt −16|ut −wt|2
8|ut −wt|3 dt
= 2dWt +
St
2|ut −wt|dt.
Combining the two last displays, we learn that there exists an adapted process Zt such 
that
dYt = 2dWt + Ztdt,
∀t < τ
(26)
such that Zt ≤βYt almost surely for all t ≤τ. A ﬁnal application of Itô’s formula gives,
d(e−βtYt) = e−βtdYt −βe−βtYtdt = 2e−βtdWt + e−βt(Zt −βYt)dt.
(27)
Therefore, e−βtYt is a supermartingale, and by the optional stopping theorem, we have
E [Yt∧τ] ≤eβtE
	
e−β(t∧τ)Yt∧τ

= eβtY0 = eβtε.
It follows that
E
	
|aν(wt) −aν(ut))|

 (24)
≤βE
	
|wt −ut|

≤βeβtε.
(28)
It remains to bound the second summand in the right hand side of (23). To this end, 
recall that E is F1-measurable, so we have for all t ≥1,
E
	
1EC

nTr(Aν(wt))

≤P

EC
sup
v∈Rn E
	
nTr(Aν(wt))
 w1 = v

.
(29)
To give an upper bound for the right hand side, we will ﬁrst need the following lemma 
which is a simple variant of the reﬂection principle for random walks.
18
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
Lemma 16. Let ε > 0. Let Wt be a standard Brownian motion and let Xt, Qt be adapted 
to Wt, which satisfy
Xt = ε + Wt +
t

0
Qsds
and such that Qt ≤0, almost surely for all t. Let τ = inf{t; Xt = 0}. One has
P(τ ≥s) ≤
ε
√s,
∀s > 0.
Proof. By the reﬂection principle (see [12, Theorem 2.19]), we have
P

min
t∈[0,s] Xt ≤−ε
 
≥P

min
t∈[0,s] |Wt + ε| = 0
 
= 2P(Ws ≤−ε)
= 1 −2(P(Ws ∈[0, ε])
≥1 −
2ε
√
2πs.

Let t →T (t) be the unique increasing function satisfying
4
T (t)

0
e−2βsds = t,
∀0 ≤t ≤4
∞

0
e−2βsds.
According to (27),
[e−βtYt]T (s) = 4
T (s)

0
e−2βtdt = s
Since, as seen above, the process e−βtYt is a super-martingale, by applying a change of 
time we have that the process t →e−βT (t)YT (t) is also a super-martingale (with respect 
to the ﬁltration FT (t)). We may invoke the above lemma on this process and use the fact 
that 4 

 1
0 e−2βsds ≥1
β , to obtain
P

EC
= P(τ ≥1) ≤ε

β.
Finally, that by Equation (18) we have for all v ∈Rn that
E
	
nTr(Aν(wt))
 w1 = v

≤ne−(t−1)/16.
R. Eldan, O. Shamir / Journal of Functional Analysis 282 (2022) 109392
19
Combining the last two displays with equation (29), we have
E
	
1EC

nTr(Aν(wt))

≤ε

βne−(t−1)/16.
By a similar argument, the same bound holds with wt replaced by ut. Together with 
equations (23) and (28) this gives
W1(τvν, τv+εθν) ≤ε

β√neβt + 2

βne−(t−1)/16
,
∀t ≥1.
Choosing t = log(2n)
2β+ 1
8
ﬁnally gives
W1(τvν, τv+εθν) ≤4εβn1−1/(32β),
completing the proof of Proposition 15.
It remains to justify the existence and uniqueness of the solutions of the stochastic 
diﬀerential equation (21)-(22). We ﬁrst note that aν : Rn →Rn is C∞-smooth and 
Lipschitz. Remark also that we can write Ut = U(ut, wt) where
U(u, w) = In −2
 w −u
|w −u|
 ⊗2
.
Observe that for all δ > 0, the coeﬃcients of U(v, w) are C∞-smooth and Lipschitz 
on the set Aδ := {(u, v) ∈Rn × Rn; |u −v| ≥δ}. Consider the stopping times τk =
inf
!
t; (ut, wt) /∈A1/k
"
. By a standard existence theorem [10, Chapter 4] there exists a 
unique strong solution up to τk for all k. By continuity we have τ = limk→∞τk, meaning 
that there exists a solution up to time τ. For t > τ we can simply consider the solution of 
the equation (21) with initial condition wτ. This establishes the existence and uniqueness 
of a strong solution for any t > 0.
