---
doc_id: s0025-5718-07-02027-3
doc_title: "MA THEMA TICS OF COMPUT A TION"
section_id: sec-005-7-the-algorithm
section_title: "The algorithm"
section_number: 7
pages: 14-24
source_pdf: S0025-5718-07-02027-3.pdf
source_sha256: 080b5ac8542ff19c
doc_brief: "MATHEMATICS OF COMPUTATION — We describe an algorithm for computing Coleman’s p-adic poly- logarithms up to a given precision."
---
In this section we use the material from the previous sections in order to give
an algorithm for computing Lin(z)f o rn ≥ 2a n dz ⁄= 1 up to a given precision and
analyze its eﬃciency.
First of all we formalize the notion of “up to a given precision”.
Deﬁnition 7.1. (1) For any numberα in Cp we say that we knowα up to precision
N if we have β in Cp such that vp(α − β) >N .
(2) We say that we knowα ⁄=0i n Cp up to relative precision N if we have β in
Cp such that vp(β/α − 1) >N .
Remark 7.2. (1) Note that those notions are absolute; even if α is in a ﬁnite
extension of Qp they do not take the ramiﬁcation of this extension into account.
(2) For α and β as in the ﬁrst part of the deﬁnition we shall refer to β as an
approximation of α up to precision N.
(3) If we knowα ⁄= 0 up to precisionN, then we knowα up to relative precision
N − vp(α), and conversely.
(4) If z ⁄= 0 is known up to relative precisionN ≥ 0, then so is 1/z.I np a r t i c u l a r ,
if we know z ⁄= 0 up to precisionN>v p(z), then we knowz and 1/z up to relative
precision N − vp(z), and 1/z up to precision N − 2vp(z).
We assume that we want to compute Lin(z) up to precision N> 0f o rz ⁄=1i n
a complete subﬁeld F of Cp.I f z in F does not lie in U0, U1 or U∞, then it lies in
Uζ for some Teichm¨uller representative ζ ⁄=1 . S i n c eF is complete one sees as in
the proof of Proposition 4.1 that ζ lies in F.
We shall also assume that we know z up to precision N ′ >v p(z)s ot h a tw e
can at least decide in which residue disc z lies and, in fact, we know vp(z). In
Algorithm 7.10 we will also give a value of N ′that suﬃces for the computation of
Lin(z) up to precison N.
Li(p) -SER VICE? AN ALGORITHM FOR p-ADIC POLYLOGARITHMS 1119
Remark 7.3. For the algorithm it is not necessary to assume that F is a ﬁnite
extension of Qp, but with that assumption it is possible to give universal estimates
(see Remark 8.1) and to quantify its eﬃciency (see Theorem 8.2). If we want to
know Lin(z) up to precision N for arbitrary z in Cp, then from the algorithm we
can determine N ′such that for an approximation ˜z of z up to precision N ′,L in(˜z)
is an approximation of Lin(z) up to precision N.B yt a k i n gt h i s˜z in
 Qp we reduce
to calculations in Qp(˜z), a ﬁnite extension of Qp and a complete ﬁeld.
Remark 7.4. We shall now show that Li n(z)i si n F because F is complete, and
clarify how Lin(z) depends on the branch of the logarithm (see Deﬁnition 2.1 and
Remark 2.2). (The latter was also made explicit in [5, Proposition 2.6] by a diﬀerent
method.)
It is clear from (3.1) that F
n,0(t) lies in Q[[t]], so that Lin(z)f o rz in U0 lies in
F and is independent of the branch of the logarithm.
For z ⁄= ∞ in U∞ it follows from Proposition 2.10(2) that Lin(z)i si nF provided
we use a branch of the logarithm for which log(p)i si n F. The dependence on this
branch is also clear from this.
If z in Uζ,w h e r eζ ⁄=1i sa( pf − 1)-th root of unity for some f> 0, then by
Proposition 4.4 the coeﬃcients of Fn,ζ(t)a r ei nQp(ζ) ⊆ F so that Lin(z) lies in F.
Since the statements of Propositions 4.2, 4.3 and 4.4 do not depend on the branch
of the logarithm, neither does Li
n(z)f o rs u c hz.
For z ⁄=1i n U1 it is clear that Li 1(z)= − log(1 − z)i si n F if log(p)i s ,a n d
the dependence on the branch of the logarithm is clear as well. For n ≥ 2, we use
Propositions 5.6 and 5.8 to write Lin(z)= Hn(z −1) −logn−1(z)l o g ( 1−z)/(n −1)!.
From its deﬁnition and Proposition 5.5 we have that Hn(z − 1) is independent of
the branch of the logarithm. Moreover, from Proposition 5.8 we see that it is in
F.S o L in(z)i si n F if log(p) is, and the dependence of Li n(z) on the branch of
the logarithm is also explicit since only log(1 − z) depends on it. Finally, for z =1
and n ≥ 2 we deﬁned Lin(1) in Remark 5.7 as En(1) = Hn(0), which is in Qp by
Proposition 5.8 and is independent of the branch of the logarithm by Remark 5.7.
Before giving the algorithm, we describe two special cases that have to be dealt
with separately, namely z =0a n d z =1 .
Remark 7.5. Note that we can know z in Cp up to precision N ′>v p(z) only when
z ⁄= 0, which we shall assume in Algorithm 7.10 below. However, clearly Lin(0) = 0,
and if we know that |z| <p −N ′
≤ 1, then |Lin(z)| < maxm≥0{pmn−N ′pm
} by (3.4)
because |Li(p)
n (z)| = |z| when |z| < 1. If n ≤ N ′ln(p), then this maximum is
attained for m = 0 and equals p−N ′
, but if n>N ′ln(p), then it may be much
bigger.
For z = 1 the problem is of a diﬀerent nature. Although we deﬁned Li n(1) for
n ≥ 2 in Remark 5.7, in order to be able to bound Li n(z) − Lin(1) if z =1u pt o
its precision, we assume that F has ﬁnite ramiﬁcation index over Qp.
Remark 7.6. (1) For n ≥ 2w eh a v eL in(1) = 2 n−1Lin(−1)/(1 − 2n−1)( s e eR e -
mark 5.7 and Proposition 2.10(1)), which we can compute up to any desired preci-
sion using Algorithm 7.10 below. Of course, if n is even, then this value is zero by
Remark 5.12(1).
1120 AMNON BESSER AND ROB DE JEU
(2) If |z − 1| <p −N ′
≤ 1, z is in a subﬁeld of Cp of ﬁnite ramiﬁcation index e,
and n ≥ 2, then Lin(z)=L i n(1) up to precision
min{n logp(N ′/n), (n−1) logp(N ′)−vp((n−1)!)−vp(e)+min{vp(log(p)), − logp(e)}}.
If N ′ln(p) ≥ n, then this holds up to precision
min{N ′, (n − 1)N ′− vp((n − 1)!) − vp(e)+m i n{vp(log(p)), − logp(e)}} .
Namely, combining Propositions 5.6 and 5.8 we have, forz ⁄=1i n U1,
(7.7) Li n(z)= Hn(z − 1) − logn−1(z)l o g ( 1− z)
(n − 1)! ,
a n di nR e m a r k5 . 7w ep u tL in(1) = En(1) = Hn(0) . Thus we are really interested
in a lower bound for the p-adic valuation of
(7.8) Hn(t) − Hn(0) − logn−1(1 +t)l o g (−t)
(n − 1)!
when for t = z − 1w eh a v evp(t) >N ′≥ 0. By Proposition 6.11 we have
vp(Hn(t) − Hn(0)) > min
k≥1
{kN ′− n logp(k)} ,
and, similarly, vp(log(1 +t)) > mink≥1{kN ′− logp(k)}. By our assumption on the
ramiﬁcation, evp(t) is a positive integer a and
log(−t)=l o g (t)= e−1(a log(p)+l o g (t′))
with t′= te/pa having absolute value 1. Since log( η) = 0 for any root of unity η
we may assume t′ is in U1, hence satisﬁes vp(t′− 1) ≥ 1/e. T h e na ne s t i m a t ef o r
log(t′) similar to that for log(1 +t)g i v e s
vp(log(t)) ≥ min{vp(log(p)), min
k≥1
{ke−1 − logp(k)}} − vp(e) .
(For a slightly diﬀerent estimate for this see Remark 8.1.) Our statements then
follow from (7.8) by using the following lemma for the minima in our estimates.
Lemma 7.9. For p prime and C,c > 0, mink≥1{Ck − c logp(k)} >c logp(C/c).I f
C ln(p) ≥ c, then this minimum equals C.
Proof. Diﬀerentiating Ck −c logp(k) with respect tok we see that this function has
a unique minimum on the positive reals atk0 = c/(C ln(p)), and that ifk0 ≤ 1, then
our original minimum is at k = 1, hence equals C.I f k0 > 1, then the minimum
on the positive reals equals c
ln(p) (1 − ln(c)+l n (C)+l n ( l n (p))) >c logp(C/c)s i n c e
ln(ln(p)) > −1 for all primes p. □
We now give the algorithm for computing Lin(z) up to precision N for z ⁄=0 , 1,
while also giving a suﬃcient precision forz for this. The various steps, in which we
consider (approximations of) truncations of Fn,ζ(t), gn(v)a n dHn(t) by ignoring
terms of degree at least tsl, gsl and hsl respectively, will be justiﬁed afterwards. We
assume that the ﬁxed branch of the logarithm, log(z), is readily computable.
Algorithm 7.10. In order to compute Li n(z)f o rz ⁄=0 , 1i n F and n ≥ 2u pt o
precision N> 0 we ﬁrst determine in which residue disc z lies and then do the
following.
Li(p) -SER VICE? AN ALGORITHM FOR p-ADIC POLYLOGARITHMS 1121
(1) If z is in U0, then we ﬁndM ≥ 0 such thatpmvp(z)−mn > N for all m>M .
For eachm =0 ,...,M we ﬁnd tslm ≥ 1 such thatkpmvp(z)−mn > N for k ≥ tslm.
Working in F up to precision N + nM we then calculate
M∑
m=0
p−mn
tslm−1∑
k=1
′bk ˜zkpm
,
where the prime indicates that we sum only over k that are not divisible by p,˜z is
an approximation of z up to precision N +nM and bk is an approximation of 1/kn
up to the same precision.
(2) If z is in U∞,t h e nw ec a l c u l a t e(−1)n−1Lin(1/z) −logn(z)/n!. Here Lin(1/z)
is computed using (1), and it can be calculated up to precisionN if we knowz up to
precision max{N +nM +2vp(z),vp(z)} where M is such that −pmvp(z) −mn > N
for all m>M . We can calculate log n(z)/n! up to precision N by ﬁrst ﬁnding V
with | log(z)|≤ p−V and knowing z up to precision N ′>v p(z) satisfying
max{V,N + vp(n!) − (n − 1)V }≤ min
m≥0
{(N ′− vp(z))pm − m} .
(3) If z lies in Uζ with ζ ⁄=1i n F a root of unity of order dividing pf − 1, then
we proceed in several steps.
(a) We ﬁnd tsl ≥ 2 such that kvp(z − ζ) − n logp(k) >N for all k ≥ tsl.
(b) We ﬁnd gsl ≥ 2 with the property that
k
p − 1 − logp(k) >N − m + c(m, p)+( n − m)l o gp(tsl − 1)
for m =1 ,...,n and all k ≥ gsl,w h e r ec(m, p)i sa si nP r o p o s i t i o n6 . 1 .
(c) We calculate the classes of gm(v)i n Qp[[v]]/(vgsl)f o rm =1 ,...,n induc-
tively using Proposition 4.3, starting with the coeﬃcients of g0(v)u pt o
precision N + n logp(tsl − 1) +n
⌊
logp(gsl − 1)
⌋
.
(d) In Qp(ζ) we ﬁnd an approximation˜ζ of ζ with vp(˜ζ −ζ) >N +n logp(tsl−1).
Working in Qp(ζ) up to precision N +n logp(tsl −1) we compute Li(p)
m (ζpj
)
for j =0 ,...,f − 1a n d m =1 ,...,n up to precision N − m +( n −
m)l o gp(tsl − 1) by evaluating the terms of degree smaller thangsl in gm(v)
on 1/(1 − ˜ζpj
).
(e) Still working in Qp(ζ) up to precisionN +n logp(tsl−1) we calculate Lim(ζ)
up to precision N +( n − m)l o gp(tsl − 1) for m =1 ,...,n by using Propo-
sition 4.2, with the Li(p)
m (ζpj
)( j =0 ,...,f − 1) replaced with the approxi-
mations obtained in (d).
(f) Working in Qp(ζ)[[t]]/(ttsl) with coeﬃcients up to precisionN+n logp(tsl−1)
we use (4.5), (4.6) and (4.7), but with ζ replaced by ˜ζ and the Lim(ζ)r e -
placed by the approximations obtained in (e), in order to compute approx-
imations to the terms of degree less than tsl in F
n,ζ(t).
( g )W et h e ne v a l u a t et h et e r m so fd e g r e el e s st h a ntsl in the result on ˜z − ˜ζ
where ˜z is an approximation of z of precision N + n logp(tsl − 1), and we
work in F up to precision N + n logp(tsl − 1).
(4) If z ⁄= 1 lies in U1,t h e nw ec a l c u l a t eL in(z) up to precision N by calculating
both terms in (7.7) up to precision N, in several steps.
1122 AMNON BESSER AND ROB DE JEU
(a) We ﬁnd hsl ≥ 2 such thatkvp(z −1) >N +n logp(k) for allk ≥ hsl;i f p =2 ,
then we increase hsl if necessary to ensure that k>N − 1+ n logp(hsl − 1)
for all k ≥ hsl.
(b) If p = 2, then we compute the terms of degree less than hsl in
Hm(t)= bm,0 + bm,1t + bm,2t2 + ···
for m =2 ,...,n using (5.9) and (5.10), working in Q2[[t]]/(thsl)u pt op r e -
cision N + n log2(hsl − 1) for the coeﬃcients. At each stage we determine
an approximation ˜bm,0 of Hm(0) = bm,0, either as 0 if m is even, or as
2m−1(1 − 2m)−1 ∑ hsl−1
k=1
˜bm,k(−2)k if m is odd, where ˜bm,k is the approxi-
mation of bm,k.
If p ⁄=2 ,t h e nf o rm =2 ,...,n we put Hm(0) = 0 when m is even, and
compute
Hm(0) = 2m−1pmgm(1/2)/((1 − 2m−1)(pm − 1))
up to precisionN +(n−m)l o gp(hsl−1) when m is odd. For this we proceed
as in (3)(b)–(d), using gsl ≥ 2 such that
k
p − 1 − logp(k) >N − m + c(m, p)+ vp(1 − 2m−1)+( n − m)l o gp(hsl − 1)
for k ≥ gsl and m =2 ,...,n ,w h e r ec(m, p) is as in Proposition 6.1, and we
work up to precision
max
m=2,...,n
{N −m+vp(1 −2m−1)+( n −m)l o gp(hsl −1) +m⌊logp(gsl −1)⌋}
in Qp for the coeﬃcients of the gm(v)’s (m =0 ,...,n ). We then com-
pute the terms of degree less than hsl in Hn(t) by integration using (5.9)
and (5.10), but with the Hm(0) replaced by the approximations just ob-
tained and working up to precision N + n logp(hsl − 1) in Qp for the coeﬃ-
cients.
(c) We ﬁnd V and V1 with V ≤ vp(log(z)) and V1 ≤ vp(log(1 − z)) and put
~N =m a x{N + vp((n − 1)!),V 1 +( n − 1)V }.
( d ) W ec o m p u t el o gn−1(z) up to precision ~N − V1 as well as − log(1 − z)u pt o
precision ~N −(n−1)V and divide their product by (n−1)!. The calculation
of logn−1(z) up to the required precision can be done if we know z up to
precision N ′> 0 satisfying
max{V, ~N − V1 − (n − 2)V }≤ min
m≥0
{N ′pm − m} .
The calculation of − log(1 − z) can be done up to the required precision if
we know z up to precision N ′′>v p(1 − z) satisfying
~N − (n − 1)V ≤ min
m≥0
{(N ′′− vp(1 − z))pm − m} .
(e) Working in F up to precisionN +n logp(hsl−1) we evaluate the approxima-
tions of the terms of degree less thanhsl in Hn(t) as obtained in (b) on ˜z −1
where ˜z is an approximation of z of precision N + n logp(hsl − 1). We add
the result to the product obtained in (d), ﬁnding Lin(z) up to precision N.
Li(p) -SER VICE? AN ALGORITHM FOR p-ADIC POLYLOGARITHMS 1123
Remark 7.11. The conditions on tslm, tsl, gsl and hsl in (1), (3)(a), (3)(b), (4)(a)
and (4)(b) of the algorithm are of the formc1k −c2 ln(k) >c 3 for all k ≥ tslm,e t c . ,
with positive c1 and c2. Since the left-hand side is increasing for k>c 2/c1 it is
very easy to ﬁnd the minimum values for tslm,e t c .
We now justify the various steps in Algorithm 7.10. For (1) we use the next
proposition.
Proposition 7.12. Let N> 0 and let z ⁄=0 be in U0.I f M ≥ 0 is such that
pmvp(z) − mn > N for all m>M , ˜z is an approximation of z up to precision
N + nM,a n df o rm =0 ,...,M we choose tslm > 0 such that kpmvp(z) − mn > N
for k ≥ tslm,t h e n
M∑
m=0
p−mn
tslm −1∑
k=1
′˜zkpm
kn ,
where the prime indicates that we sum only overk that are not divisible by p,i sa n
approximation of Lin(z) up to precisionN. Moreover, we can replace each1/kn by
an approximation up to precision N + nM.
Proof. It is clear from (3.3) that|Li(p)
n (z)| = |z| when |z| < 1. Therefore, from (3.4)
we see that in order to compute Lin(z) up to precision N we only have to compute∑ M
m=0 p−mnLi(p)
n (zpm
)i f pmvp(z) − mn > N for all m>M . So we reduce to
the calculation of p−mnLi(p)
n (zpm
) up to precision N for m =0 ,...,M .I n t h e
corresponding power seriesp−mn ∑ ′∞
k=1 zkpm
/kn we can ignore terms with valuation
bigger than N, i.e., where kpmvp(z) − mn > N.
Finally, for each term p−mnzkpm
/kn that we compute we can replace z with an
approximation ˜z satisfying vp(z − ˜z) >N +mn and 1/kn with an approximationbk
satisfying vp(1/kn − bk) >N + mn, and obtain that term up to precision N.T h i s
follows from the identity zkpm
/kn − bk ˜zkpm
=( zkpm
− ˜zkpm
)/kn +( 1/kn − bk)˜zkpm
since vp(kn) = 0, and vp(z) > 0 implies that vp(zkpm
− ˜zkpm
) ≥ vp(z − ˜z)a n d
vp(˜zkpm
) > 0. □
I n( 2 )w eu s et h ef a c tt h a tL in(z)=( −1)n−1Lin(1/z) − logn(z)/n!b yP r o p o s i -
tion 2.10(2). For the term Lin(1/z) we use (1), and the corresponding precision of
z also follows from this part together with Remark 7.2(4) because we are assum-
ing that we know z up to positive relative precision. The term − logn(z)/n!c a n
be readily calculated using standard methods, so we only give estimates for the
precision of z that enables us to calculate it up to precision N.
Lemma 7.13. If y in Cp satisﬁes |y|≤ p−V and is known up to precisionN ′≥ V ,
then yn for n ≥ 1 is known up to precision N ′+( n − 1)V .
Proof. By assumption we know y + ε for some ε in Cp with |ε| <p −N ′
.T h e n
|(y + ε)n − yn| = |ε|·| yn−1 + εyn−2 + ··· + εn−2y + εn−1| <p −N ′
p−(n−1)V because
N ′≥ V . □
As for the logarithm we have the following result.
Lemma 7.14. If we knowz in C∗
p up to precisionN ′>v p(z), then we can calculate
log(z) up to precisionminm≥0{(N ′−vp(z))pm −m}.I f 1 ≤ (N ′−vp(z)) ln(p),t h e n
we can calculate log(z) up to precision N ′− vp(z).
1124 AMNON BESSER AND ROB DE JEU
Proof. Since we know z up to precision N ′ we know ˜z = z + ε with |ε| <p −N ′
.
Then log(˜z) −log(z)=l o g ( 1+ε/z)= −Li1(−ε/z). Since vp(ε/z) >N ′−vp(z) > 0
the estimates in Remark 7.5 apply. □
The last inequality in part (2) of the algorithm is then justiﬁed by the next
proposition. Note that Lemma 7.14 in practice allows us to bound | log(z)|,a si s
required here. (But see also Remark 8.1.)
Proposition 7.15. If, for z in C∗
p, | log(z)|≤ p−V and we know z up to precision
N ′>v p(z) satisfying
max{V,N + vp(n!) − (n − 1)V }≤ min
m≥0
{(N ′− vp(z))pm − m} ,
then we can compute logn(z)/n! up to precision N.
Proof. It suﬃces to calculate logn(z) up to precisionN +vp(n!). By Lemma 7.13 we
can do this if we know log(z) up to precision N ′′=m a x{V,N +vp(n!) −(n −1)V }.
In order to compute log(z) up to precision N ′′, it suﬃces by Lemma 7.14 to know
z up to precision N ′>v p(z) satisfying minm≥0{(N ′− vp(z))pm − m}≥ N ′′. □
For step (3) of the algorithm we need some more results.
Proposition 7.16. Let gn(v) be as in Proposition 4.3,a n dl e tc(n, k) be as in
Proposition 6.1. To compute gn(α) up to precision N ′ > 0 when vp(α)=0 it
suﬃces to know α up to precision N ′ and to evaluate the sum of the terms in
gn(v) of degree less than gsl′ on the approximation of α,w h e r egsl′ is such that
k
p−1 −logp(k)−c(n, p) >N ′for all k ≥ gsl′. In fact, it suﬃces to use approximations
up to precision N ′for the coeﬃcients of the terms of degree less thangsl′.
Similarly, in order to know Li(p)
n (ζ) up to precision N ′ > 0 for a root of unity
ζ ⁄=1 of order not divisible by p,i ts u ﬃ c e st ok n o wζ and the coeﬃcients of the
terms of gn(v) of degree less than gsl′up to precision N ′,w h e r egsl′is as before.
Proof. The ﬁrst statement follows from the estimates for the valuations of the
coeﬃcients of gn(v) as given in Proposition 6.1. It implies the second because
vp(1/(1 − ζ)) = 0, Li (p)
n (ζ)= gn(1/(1 − ζ)), and 1/(1 − ζ) is known to the same
precision as ζ by Remark 7.2(4). □
Remark 7.17. Computing the coeﬃcients of gn(v) as rational numbers is very in-
eﬃcient so, instead, we use coeﬃcients in Qp with ﬁnite precision. If gn(v)=
an,1v + an,2v2 + ··· ,t h e nkan+1,k = −(an,1 + an,2 + ··· + an,k) by Proposition 4.3.
Hence, if we knowan,k for 1 ≤ k ≤ gsl′−1 up to precision ~N, then we knowan+1,k
for 1 ≤ k ≤ gsl′− 1 up to precision ~N −
⌊
logp(gsl′− 1)
⌋
. In particular, using the
method of Proposition 4.3 we can computean,k for k =1 ,..., gsl′−1 up to precision
N ′if we know a0,k for k =1 ,..., gsl′− 1 up to precision N ′+ n
⌊
logp(gsl′− 1)
⌋
.
For the power series Fn,ζ(t) instead of gn(v), where ζ ⁄=1i sa( pf − 1)-th root
of unity, the corresponding statements in the next proposition are more involved.
Proposition 7.18. Assume that z lies in the residue discUζ for ζ ⁄=1 a (pf −1)-th
root of unity and let
Fn,ζ(t)= an,0 + an,1t + an,2t2 + ···
be the Taylor expansion of Lin(z) around ζ as in Proposition 4.4.L e t tsl′> 0 be
such that vp(an,k(z − ζ)k) >N for all k ≥ tsl′ and assume that the Lim(ζ) for
Li(p) -SER VICE? AN ALGORITHM FOR p-ADIC POLYLOGARITHMS 1125
m =1 ,...,n are known up to precision N +( n − m)l o gp(tsl′− 1).I f ζ and z
are known up to precision N + n logp(tsl′− 1), then we can compute Lin(z) up to
precision N by:
(1) ﬁnding the terms of degree less thantsl′in F0,ζ(t) as in (4.5) with ζ replaced
with its approximation;
(2) for m =1 ,...,n computing the terms of degree less than tsl′ in Fm,ζ(t)
up to precision N +( n − m)l o gp(tsl′− 1) via repeated integration of (4.6),
using the approximate values for ζ and Fm,ζ(0) = Lim(ζ);
(3) evaluating the terms of degree less thantsl′in the approximation of Fn,ζ(t)
on the diﬀerence of the approximations of z and ζ.
Proof. Note that tsl′as in the statement of the proposition exists by Proposition 6.7
or Remark 6.9. We can therefore compute Lin(z) up to precision N by computing
an,0 +an,1(z −ζ)+ ··· +an,tsl′−1(z −ζ)tsl′−1. Using an approximation ˜ζ of ζ in (4.5)
we have an approximation
~Fm,ζ(t)=˜am,0 +˜am,1t + ···
of Fm,ζ(t)f o rm =0 . W eu s e~Fm,ζ(t) instead of Fm,ζ(t)a n d˜ζ instead of ζ in (4.6)
in order to inductively obtain an approximation
~Fm+1,ζ(t)=˜am+1,0 +˜am+1,1t + ···
of Fm+1,ζ(t). Here k˜am+1,k = − ∑ k−1
j=0 (−˜ζ)j−k˜am,j for k =1 , 2,..., tsl′− 1, as
in (6.8). Inductively we may assume thatvp(˜am,j −am,j) >N +(n−m)l o gp(tsl′−1)
for j =0 ,..., tsl′− 1 since this holds for m = 0 by our assumption on vp(˜ζ − ζ),
Remark 7.2(4) and (4.5). Then for k =1 ,..., tsl′− 1 we have, as in the proof of
Proposition 6.7,
k(am+1,k − ˜am+1,k)=
k−1∑
j=0
(
(−˜ζ)j−k˜am,j − (−ζ)j−kam,j
)
=
k−1∑
j=0
(−1)j−k
[
˜ζj−k(˜am,j − am,j)+( ˜ζj−k − ζj−k)am,j
]
.
Since vp(˜ζj−k) ≥ 0a n dvp(˜ζj−k − ζj−k) >N + n logp(tsl′− 1) by our assumptions,
by Proposition 6.7 it follows as in the proof of that proposition that
vp(˜am+1,k − am+1,k) >N +( n − (m +1 ) )l o gp(tsl′− 1)
for k =1 ,..., tsl′−1. Finally, vp(˜am+1,0 −am+1,0) >N +(n −(m+1))log p(tsl′−1)
since we assume that we have such an approximation ˜am+1,0 for am+1,0 =L im+1(ζ).
Now we consider the terms an,j(z − ζ)j for j =0 ,..., tsl′− 1. For j =0w e
have vp(an,0 − ˜an,0) >N by assumption. For j> 0 this term is approximated by
˜an,j(˜z − ˜ζ)j with ˜z an approximation of z up to precision N + n logp(tsl′− 1) and
an,j(z − ζ)j − ˜an,j(˜z − ˜ζ)j =( an,j − ˜an,j)(z − ζ)j +˜an,j((z − ζ)j − (˜z − ˜ζ)j) .
We have just seen thatvp(an,j − ˜an,j) >N , and since vp(z − ζ) > 0 by assumption
the ﬁrst term in the right-hand side has valuation bigger thanN. The second term
has valuation at least vp(˜an,j)+ vp((z − ζ) − (˜z − ˜ζ)). Proposition 6.7 implies that
vp(˜an,j) ≥ min{vp(an,j − ˜an,j),vp(an,j)}≥− n logp(tsl′−1), so the valuation of the
second term is bigger than N by our assumptions on vp(z − ˜z)a n dvp(ζ − ˜ζ). □
1126 AMNON BESSER AND ROB DE JEU
We can now justify Algorithm 7.10(3). Remark 7.17 implies that (c) computes
the coeﬃcients of the terms of degree less than gsl in gm(v)( m =1 ,...,n )u pt o
precision N + n logp(tsl − 1) + (n − m)⌊logp(gsl − 1)⌋.I n( d ) ,f o rm =1 ,...,n let
N ′
m = N −m+(n−m)l o gp(tsl−1). If N ′
m > 0, then the indicated method calculates
Li(p)
m (ζpj
)= gm(1/(1 − ζpj
)) up to precision N ′
m by Proposition 7.16: vp(˜ζ − ζ) >
N ′
m so according to Remark 7.2(4) we have vp(1/(1 − ˜ζpj
) − 1/(1 − ζpj
)) >N ′
m;
k/(p−1)−logp(k)−c(m, k) >N ′
m for all k ≥ gsl by (b); and the relevant coeﬃcients
in gm(v)a r ek n o w nu pt op r e c i s i o nN ′
m from (c). If N ′
m ≤ 0, then we observe that
the valuation of the diﬀerence between what we calculate in (d) andgm(1/(1−ζpj
))
is bigger than N ′
m by Proposition 6.1 since vp(1/(1 − ˜ζpj
) − 1/(1 − ζpj
)) > 0a n d
k/(p − 1) − logp(k) − c(m, p) >N ′
m for k ≥ gsl by (b). (Note that we always
know the coeﬃcients of gm(v) that we compute up to precision N ′
m.) Now (e) is
immediate from (d), taking into account the valuations of the coeﬃcients of the
various contributions to Lim(ζpj
) when applying Proposition 4.2. Finally, (f) and
(g) then follow from Proposition 7.18 together with its proof by our choice of tsl
in (a) since vp(an,k) ≥− n logp(k) by Proposition 6.7.
We conclude this section by justifying Algorithm 7.10(4), dealing ﬁrst with the
term − logn−1(z)l o g ( 1− z)/(n − 1)! in (7.7), i.e., steps (c) and (d).
If for some α and β in Cp we have Vα ≤ vp(α)a n dVβ ≤ vp(β), then for the
calculation of αβ up to precision N it suﬃces to compute α up to precision N −Vβ
and β up to precision N − Vα,a tl e a s ti fN − Vα − Vβ ≥ 0. By increasing N if
necessary we may always assume the latter. For z ⁄=1i n U1 we let α =l o gn−1(z),
β = − log(1 − z) and replace N with N + vp((n − 1)!). Using Lemma 7.14 we ﬁnd
V and V1 with V ≤ vp(log(z)) and V1 ≤ vp(log(1 − z)). Then we let
~N =m a x{N + vp((n − 1)!),V 1 +( n − 1)V }
and compute logn−1(z) up to precision ~N −V1 as well as − log(1 −z) up to precision
~N −(n−1)V . We can do this by applying Proposition 7.15 and Lemma 7.14, taking
into account thatvp(z) = 0. This together with the estimates above gives (4)(c)–(d)
of Algorithm 7.10.
For the computation ofHn(z −1) up to precisionN, which corresponds to the re-
maining steps of (4), we use the following result and, ifp = 2, also Proposition 7.20.
Proposition 7.19. Assume z is in the residue disc U1 and, for n ≥ 2,l e t
Hn(t)= bn,0 + bn,1t + bn,2t2 + ···
be as in Propositions 5.8 and 6.11.L e thsl′> 0 be such that vp(bn,k(z − 1)k) >N
for all k ≥ hsl′ and assume that Hm(0) for m =2 ,...,n i sk n o w nu pt op r e c i s i o n
N+(n−m)l o gp(hsl′−1).I f z with |z|<1 is known up to precisionN+n logp(hsl′−1),
then we can compute Hn(z − 1) up to precision N by:
(1) ﬁnding the terms of degree less thanhsl′of G2(t) and H2(t) with coeﬃcients
up to precision N +( n − 2) logp(hsl′− 1);
(2) for m =3 ,...,n computing the terms of degree less thanhsl′in Gm(t) and
Hm(t) up to precision N +( n − m)l o gp(hsl′− 1) via repeated integration of
G′
n(t)= Gn−1(t)/(1 +t) and (5.10),u s i n gGm(0) = 0 and the approximate
values for Hm(0);
(3) evaluating the terms of degree less than hsl′in the approximation of Hn(t)
on the diﬀerence of the approximation of z and 1.
Li(p) -SER VICE? AN ALGORITHM FOR p-ADIC POLYLOGARITHMS 1127
Proof. Parts (1) and (2) are proved as in the proof of Proposition 7.18 by induction
on m starting with m = 2, but for Gm(t)a n dHm(t) simultaneously and with the
simpliﬁcation that we do not have to approximate 1. The estimate for (3) also goes
as in that proof, the estimates for the coeﬃcients ofHn(t) in Proposition 6.11 being
the same as for those of Fn,ζ(t) in Proposition 6.7. □
In order to apply this proposition we need to determine Hm(0) up to precision
N +(n −m)l o gp(hsl′−1) for m =2 ,...,n , and, according to Remark 5.12(1), only
for m odd.
When p ⁄=2w eh a v eHm(0) = 2m−1pmLi(p)
m (−1)/((1 − 2m−1)(pm − 1)) by Re-
mark 5.12(2), so we only have to calculate Li(p)
m (−1) up to precision
N +( n − m)l o gp(hsl′− 1) +vp(1 − 2m−1) − m
for m odd with 2 ≤ m ≤ n. In Algorithm 7.10(4)(b) we have done this along the
lines of (3)(b)–(d) of the algorithm. The justiﬁcation for this is similar to the one
given after Proposition 7.18, putting
N ′
m = N − m + vp(1 − 2m−1)+( n − m)l o gp(hsl − 1),
but with the simpliﬁcation that ζ = −1 is now known exactly, and using Proposi-
tion 6.11 instead of Proposition 6.7. Step (4)(e) is then immediate from the last
part of Proposition 7.19.
When p = 2 we use (5.11) in order to computeH
m(0), and for this we formulate
a supplement to Proposition 7.19. Note that we can always attain the condition on
hsl′below by increasing it if necessary, as stated in (4)(a) of the algorithm.
Proposition 7.20. Let p =2 and assume that hsl′in Proposition 7.19 also satisﬁes
k + vp(bm,k) >N − (m − 1) + (n − m)l o gp(hsl′− 1)
for all k ≥ hsl′ and all m =2 ,...,n . Then in the inductive procedure of Proposi-
tion 7.19 we can calculate Hm(0) for m =2 ,...,n up to the required precision as
2m−1(1 − 2m)−1 ∑ hsl′−1
k=1
˜bm,k where ˜bm,k is the approximation of bm,k.
Proof. We know from (5.11) thatHm(0) = 2m−1(Hm(−2) −Hm(0))/(1 −2m). The
extra condition on hsl′ means that for m =2 ,...,n we can compute Hm(−2) −
Hm(0) up to precision N − (m − 1) + (n − m)l o gp(hsl′− 1) using the non-constant
terms of degree less than hsl′in Hm(t). Inductively
vp(˜bm,k − bm,k) >N +( n − m)l o gp(hsl′− 1)
for k =1 ,..., hsl′− 1, so that
Hm(−2) − Hm(0) −
hsl′−1∑
k=1
˜bm,k(−2)k
has valuation at least N − (m − 1) + (n − m)l o gp(hsl′− 1). So the formula in the
proposition approximates Hm(0) up to precision N +( n − m)l o gp(hsl′− 1). □
Now Algorithm 7.10(4)(a), (b) and (e) for p = 2 follow from Propositions 7.19
and 7.20 combined with Proposition 6.11.
This ﬁnishes the justiﬁcation of Algorithm 7.10.
1128 AMNON BESSER AND ROB DE JEU
