---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal a nd other strong Rayleigh measures"
section_id: sec-006-41-the-classical-proofs
section_title: "The classical proofs"
section_number: 4.1
pages: 9-14
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
doc_brief: "Concentration of Lipschitz functionals of determinantal a nd other strong Rayleigh measures — Let {X1,...,X n} be a collection of binary valued random variables and let f : {0, 1}n → R be a Lipschitz"
---
To prove bounds such as (1.1), one obtains an upper bound for EeλSn , and then applies Markov’s
inequality, choosing λ optimally. Underlying the bounds on EeλSn are corresponding bounds for
compensated increments. Let ∆ denote a variable with mean zero. T hree classical exponential
bounds are as follows.
|∆ | ≤ 1 ⇒ Eeλ∆ ≤eλ2/2 (4.10)
∆ ∈ [r,s ] ⇒ Eeλ∆ ≤eλ2(s−r)2/8 (4.11)
∆ ∈ [r,s ] ⇒ Eeλ∆ ≤ exp
[
(eλ − 1 −λ) |rs|
]
, (4.12)
when |r −s| ≤ 1. These are used together with the following two special cases of M arkov’s inequality.
EeλX ≤ecλ2/2 =⇒ P(X ≥a) ≤e−a2/(2c) (4.13)
EeλX ≤eb (eλ−λ−1) =⇒ P(X >a) ≤ea
( b
a +b
) a+b
≤ exp
[
− a2
2(a +b)
]
(4.14)
These inequalities have appeared many times in the literature. Inequ alities (4.10) and (4.13)
8
constitute the classical Azuma-Hoeﬀding inequality and imply
Eeλ(Sn−µn) ≤ eλ2n/2 ; (4.15)
P(Sn −µn ≥a) ≤ e−a2/(2n). (4.16)
This is valid for any martingale with diﬀerences bounded by 1; an expos ition can be found in [AS08,
Theorem 7.2.1]. The improvement to (4.11) is present already in [Hoe63 ], though the exposition
in [McD89] is clearer (see Lemma 5.8 therein). When the increments of Sn −µn are compensated
Bernoullis, one may take b −a = 1 rather than 2, resulting in an improvement by a factor of 4 in
the exponent,
Eeλ(Sn−µn) ≤eλ2n/8. (4.17)
which together with (4.13) yields (1.1). Finally, (4.12) and induction yie ld
Eeλ(Sn−µn) ≤e(eλ−λ−1) Vn ≤e(eλ−λ−1) µn (4.18)
where Vn :=∑ n
k=1pk(1 −pk) is the variance of Sn; together with (4.14) this implies (1.3); these
results appear, for instance, in [Fre75, (1.3)–(1.6)].
To prove the generalization to Lipschitz functions, let
Mk := E (f (X1,...,X n) |X1,...,X k) − Ef (X1,...,X n).
It is immediate that {Mk} is a martingale and that conditional on X1,...,X k−1, the two possible
values of Mk diﬀer by at most 1. Hence, conditional on X1,...,X k−1, the increment ∆ k :=Mk −
Mk−1 is constrained to an interval of length at most 1. Applying (4.11) the n yields (1.4).
The extension of inequalities (1.1)–(1.2) to negatively cylinder depen dent random variables is
established by examining the power series for eλSn. This may be expanded into positive sums of
expectations of products of powers of the variables {Xj : 1 ≤j ≤n}. Negative cylinder dependence
implies that these are bounded from above by the corresponding pr oducts of expectations. There-
fore, (4.17) and (4.18) hold when the assumption of independence is replaced by negative cylinder
dependence, whence the probability inequalities (1.1) and (1.3) hold a s well. This and more is shown
in [PS97, Theorem 3.4], specializing their more general negative cylinde r property to λ = 1. We
remark that only the ﬁrst inequality (1.5) in the deﬁnition of negative cylinder dependence is used
to obtain bounds on EeλSn for λ >0, which suﬃces for the upper tail bounds. Lower tail bounds
require these inequalities for λ< 0, for which the second inequality (1.6) is required.
4.2 Proof of Theorems 3.1 and 3.4
Theorem 3.1 is a special case of Theorem 3.4. This is because any prob ability measure µ on Bn may
be viewed as the law of a point process on the n element set [n], where the random counting measure
9
Z(ω) is deﬁned by Z(ω)(S) =∑
j∈Sωj. Informally, the points of the process are the coordinates of
the ones in the sample ω. With this interpretation, the SCP on Bn is inherited from the SCP for
the point process Z, whence Theorem 3.4 with S = R (or any other standard Borel space containing
[n]) implies Theorem 3.1. It remains to prove Theorem 3.4.
Let (Ω , F, P) be a probability space on which is constructed the generalized samp ling scheme
described in Lemma 3.3. Let Fj :=σ(X1,...,X j) and let
Mj := E(f | Fj) − Ef. (4.19)
denote the martingale of sequential revelation. Applying the metho d of bounded diﬀerences is now
mostly a matter of bookkeeping. At a sample point where Xi =xi, 1 ≤i ≤k, the quantity Mj may
be written as the integral of f against the law of the point process
Zx1,...,xj +
j∑
i=1
δxi.
By the SCP, we have Zx1,...,xj ⊲ Zx1,...,xj+1 whence
d∞
(
Zx1,...,xj +
j∑
i=1
δxi , Zx1,...,xj+1 +
j+1∑
i=1
δxi
)
≤ 2.
By the Lipschitz assumption on f , it follows that |Mj+1 −Mj| ≤ 2. We now apply the basic
Azuma-Hoeﬀding inequality (4.16) to {Mj/2}1≤j≤k yielding
P(f − Ef ≥a) = P
( Mk
2 > a
2
)
≤ exp
(
−a2
8k
)
.
□
4.3 Proof of Theorem 3.2
In this section we assume P is the law of a strong Rayleigh measure on Bn with ﬁnite mean EN =µ.
We also let f denote an arbitrary but ﬁxed Lipschitz-1 function on conﬁguratio ns and deﬁne a
function φ on Z+ by
φ(k) := E(f |N =k).
Lemma 4.1. The variable N is distributed as the sum of independent Bernoullis.
Proof: In the deﬁnition of the strong Rayleigh property, setting the varia bles z1,...,z n equal
produces a univariate polynomial with no roots in the upper half plane . As pointed out at the
beginning of Section 3 of [BBL09], such a polynomial with real coeﬃcien ts must have all its roots
real. Since the coeﬃcients are nonnegative, this implies it is the gener ating function for a convolution
of Bernoullis. □
10
Lemma 4.2. The variable N satisﬁes
Eeλ(N −µ) ≤ exp
[
µ(eλ − 1 −λ)
]
and consequently for any a> 0,
P
(
N ≥µ + a
2
)
≤ exp
(
− (a/2)2
2(µ +a/2)
)
.
Proof: By Lemma 4.1 N is distributed as the sum of independent Bernoullis, which implies the
ﬁrst inequality; this implies the second inequality by (4.14). □
Lemma 4.3. The function φ is Lipschitz-1.
Proof: By Proposition 2.3 in the case of strong Rayleigh measures on Bn we know that Pk+1⊲ Pk.
By deﬁnition of the stochastic covering relation, ( φ(k + 1),φ (k)) may be written as E(f (η),f (ξ))
where d(η,ξ ) = 1 almost surely. The conclusion then follows from the fact that f is Lipschitz-1. □
Lemma 4.4. The random variable φ(N ) satisﬁes the concentration inequality
Eeλ(φ(N )−Eφ(N )) ≤eµ(eλ−1−λ).
Consequently, the upper tails of φ(N ) obey the bound
P(φ(N ) − Eφ(N )>t ) ≤e− t2
2(t+µ) .
Proof: Pursuant to Lemma 4.1, let {Yj} be a ﬁnite or countably inﬁnite collection of independent
Bernoulli variables whose sum has the same law as N ; we may therefore prove the statements with
N replaced by ∑
jYj. Write φ(∑
jYj) − Eφ(∑
jYj) as the ﬁnal term of a martingale {Mℓ} where
Mℓ := E(φ(∑
jYj) | Fℓ) − Eφ and Fℓ := σ(Y1,...,Y ℓ). If the number of Bernoullis is inﬁnite, the
ﬁnal term is a limit almost surely and in L2. The martingale {Mℓ} is a binary martingale, meaning
that conditional on Fℓ, the distribution of Mℓ+1 is concentrated on two values. In other words,
(Mℓ+1 | Fℓ) = pδr + (1 −p)δs
where p is the mean of the Bernoulli variable Yℓ+1. More importantly, r =
∫
fdµ and s =
∫
fdν
where µ is the conditional law of ∑
jYj given the values of Y1,...,Y ℓ (which are measurable with
respect to Fℓ) and given Yℓ+1 = 1, and ν is the conditional law of ∑
jYj given the values of Y1,...,Y ℓ
and givenYℓ+1 = 0. Clearly µ andν are probability measures on Z+ satisfyingd∞(µ,ν ) ≤ 1, whence
because φ is Lipschitz-1, we see that |r −s| ≤ 1. From (4.12) we then obtain
E
(
eλ(Mℓ+1−Mℓ) | Fℓ
)
≤ exp
(
p(1 −p)(eλ − 1 −λ)
)
.
The lemma follows by induction. □
11
Proof of Theorem 3.2 The event {f − Ef >a} is contained in the union of three events:
{
N >µ + a
2
}
∪
{
φ(N ) − Ef >a
2
}
∪
{
f −φ(N )> a
2, N≤µ + a
2
}
.
Thus P(f − Ef > a) is bounded above by the sum of the corresponding probabilities. Ea ch of the
ﬁrst two pieces is bounded above by exp[ −a2/(4(a + 2µ))]: the ﬁrst follows from Lemma 4.2 and
the second uses Lemma 4.4, noting that Eφ = E E (f |N ) = Ef . The last piece is bounded above
by exp[ −a2/(16(a + 2µ))]. To see this, observe that the measures Pk are all strong Rayleigh (this
is [BBL09, Corollary 4.18]). For any k ≤ µ +a/2, we can apply Theorem 3.1 to the homogeneous
measure Pk, obtaining
P
(
f −φ(N )> a
2 |N =k
)
≤ exp
(
− (a/2)2
8k
)
≤ exp
(
− a2
16(a + 2µ)
)
.
Reassembling these gives the upper bound
P
(
f −φ(N )> a
2, N≤µ + a
2
)
≤ exp
(
− a2
16(a + 2µ)
)
.
This last piece has the worst bound; using it for all three pieces gives the ﬁrst inequality of the
theorem; we remark that the better upper bound of 2 exp[ −a2/(4(a + 2µ))] + exp[−a2/(16(a + 2µ))]
is in fact valid.
For the two-sided bound, we need to consider two more events in ad dition to the three already
considered, namely the events {φ(N ) − Eφ(N )< −a/2} and {f −φ(N )< −a/2,N ≤µ +a/2}. The
arguments for these two extra events are exactly analogous to t wo of the three arguments we have
already seen, leading to a bound of exp[ −a2/(16(a + 2µ))] for each of the two new summands and
establishing the two-sided bounds. □
12
