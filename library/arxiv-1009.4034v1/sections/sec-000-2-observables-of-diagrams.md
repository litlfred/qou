---
doc_id: arxiv-1009.4034v1
doc_title: "KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES OF PARAMETER α = 1/2 PIERRE-LOÏC MÉLIOT"
section_id: sec-000-2-observables-of-diagrams
section_title: "Observables of diagrams"
section_number: 2
pages: 6-12
source_pdf: 1009.4034v1.pdf
source_sha256: 8f8d6d786b60c279
doc_brief: "KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES OF PARAMETER α = 1/2 PIERRE-LOÏC MÉLIOT — In this article, we show that Kerov’s central limit theorem related to the ﬂuctuations of Young"
---
given by the formula
z−1Gλ(z−1) = 1 +
∞∑
n=1
~hn(λ)zn = exp
(∞∑
n=1
~pn(λ)
n zn
)
.
For a true Young diagramλ, ~pn(λ) = ∑v
i=1(xi)n−∑v−1
i=1 (yi)n is the n-th moment of the interlacing
coordinates, whereas for a continuous diagram, one can give the following formula:
~pn(ω) =
∫
R
σ′′(s)snds = 1
(n + 1)(n + 2)
∫
R
σ(s)sn+2ds
Notice that~h1(λ) =~p1(λ) = 0 for any (continuous) diagramλ; on the other hand, one can show that the
other coeﬃcients are algebraically independant (viewed as functions on diagrams). So,
O = C [~h2,~h3,... ] = C [~p2,~p3,... ],
see [IO02, §2]. Theweight grading on this algebra is then deﬁned by settingwt(~pk≥2) = k, and it
provides a ﬁltration of algebra onO that is well-behaved with respect to scaling of continuous diagrams.
More precisely, ifω is a continuous diagram and ifωt is the scaled diagram deﬁned by
ωt(s) = ω(st)
t
(see ﬁgure 6), then for any homogeneous observablef of weightk, f(ωt) =tkf(ω). In particular, ifλ is
a true Young diagram and ifλ∗ =λ1/
√
|λ| =λ1/√n, thenf(λ∗) =n−k
2 f(λ).
6 PIERRE-LOÏC MÉLIOT
Given a (continuous) diagram λ,t h ec o eﬃcients ~hn(λ) of the power serie z−1Gλ(z−1) generate an algebra
O of observables of diagrams .O n e m a y a l s o c o n s i d e r a s a n a l g e b r a i c b a s i s f o rO the coe ﬃcients ~pn(λ)
given by the formula
z−1Gλ(z−1)=1+
∞∑
n=1
~hn(λ) zn =e x p
( ∞∑
n=1
~pn(λ)
n zn
)
.
For a true Young diagram λ, ~pn(λ)= ∑ v
i=1(xi)n − ∑ v−1
i=1 (yi)n is the n-th moment of the interlacing
coordinates, whereas for a continuous diagram, one can give the following formula:
~pn(ω)=
∫
σ′′(s) sn ds = 1
(n +1 ) (n +2 )
∫
σ(s) sn+2 ds
Notice that ~h1(λ)= ~p1(λ)=0 for any (continuous) diagram λ;o nt h eo t h e rh a n d ,o n ec a ns h o wt h a tt h e
other coe ﬃcients are algebraically independant (viewed as functions on diagrams). So,
O =
 [~h2, ~h3,... ]=
 [~p2, ~p3,... ],
see [IO02, §2]. The weight grading on this algebra is then deﬁned by setting wt(~pk≥2)= k,a n di t
provides a ﬁltration of algebra on O that is well-behaved with respect to scaling of continuous d iagrams.
More precisely, if ω is a continuous diagram and if ωt is the scaled diagram deﬁned by
ωt(s)= ω(st)
t
(see ﬁgure 6), then for any homogeneous observable f of weight k, f (ωt)= tk f (ω). In particular, if λ is
at r u eY o u n gd i a g r a ma n di fλ∗ = λ1/
√
|λ| = λ1/√
 n,t h e nf (λ∗)= n− k
2 f (λ).
ω
ω1/2
Figure 6. Ac o n t i n u o u sY o u n gd i a g r a mω and a rescaled version ωt.
Another algebraic basis of O consists in the free cumulants of the transition measures of the contin-
uous Young diagrams. First, if λ is a (continuous) Young diagram, we deﬁne its transition measure
µλ by
Gλ(z)=
∫
 µλ(s)
z − s .
In other words, the generating function of λ is the Stieltjes transform of the transition measure. Notic e
that the ~hn(λ)’s are precisely the moments of the compactly supported meas ure µλ.T h e n , t h e f r e e
cumulants of the measure µλ are the coe ﬃcients of the formal inverse Rλ of Gλ in a neighboorhood of
inﬁnity:
Rλ(Gλ(z)) = z for z big enough ; Rλ(z)= 1
z
(
1+
∞∑
n=1
Rn(µλ) zn
)
Figure 6. A continuous Young diagramω and a rescaled versionωt.
Another algebraic basis ofO consists in thefree cumulants of the transition measures of the contin-
uous Young diagrams. First, ifλ is a (continuous) Young diagram, we deﬁne itstransition measure
µλ by
Gλ(z) =
∫
R
µλ(s)
z−s.
In other words, the generating function ofλ is the Stieltjes transform of the transition measure. Notice
that the ~hn(λ)’s are precisely the moments of the compactly supported measureµλ. Then, the free
cumulants of the measureµλ are the coeﬃcients of the formal inverseRλ of Gλ in a neighboorhood of
inﬁnity:
Rλ(Gλ(z)) =z for z big enough ; Rλ(z) = 1
z
(
1 +
∞∑
n=1
Rn(µλ)zn
)
KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES 7
see [DNV92] for the uses of this notion in free probability. By Lagrange inversion, the free cumulants
also satisfy the formula
Rn+1(λ) =Rn+1(µλ) =− 1
n[z−1](Gλ(z))−n,
and Rn+1 is therefore an observable of diagrams that is homogeneous with weightn + 1. R. Speicher
has given a simple combinatorial interpretation of the change of basis formulas between the~h’s and the
R’s, see [NS06]. These formulas implie in particular that theRk≥2’s are algebraically independant, so
O = C [R2,R 3,... ].
Finally, another algebraic basis comes from the so-calledcentral characters, that allow to relie the
algebra O to the representation theory of the symmetric groups. Ifλ and µ are two partitions of same
size n, one denotes byχλ(µ) the value of the normalized irreducible character ofSn of label λ on a
permutation σµ of cycle typeµ. Then, ifλ and µ are two partitions of sizesn and k, one sets:
Σµ(λ) =
{
n↓kχλ(µ⊔ 1n−k) if n≥k,
0 otherwise.
Here, µ⊔ 1n−k is the completed partition obtained by adding parts of size1 to µ, andn↓k is the falling
factorial n(n− 1)··· (n−k + 1). It is true, although totally non trivial, that theΣµ’s are observables of
diagrams; cf. [IO02, §3-4]. More precisely,wt(Σµ) =|µ| +𝓁(µ), and the top homogeneous component of
Σµ is
Rµ+1 =Rµ1+1Rµ2+1··· Rµr+1,
see [Bia98] and [IO02, §10]. As a consequence,O = C [Σ1,Σ 2,... ] is freely generated by the central
characters of cycles, and one has a factorization property of characters in top homogeneous component:
Σµ1∗ Σµ2 =Σµ1⊔µ2 +
(
observable of weight less thanµ1 +µ2 +𝓁(µ1) +𝓁(µ2)− 2
)
In fact, there exists multivariate polynomials with non-negative integer coeﬃcientsKk such thatΣk =
Kk(Rk+1,Rk,...,R 2) for anyk≥ 1; these Kerov polynomials are studied for instance in [DFS08]. In
§5, we will rather have to exprime the~p’s as polynomials in theΣ’s. We refer to [IO02, Proposition 3.7]
for a proof of the following result:
Proposition 2 (Change of basis formula between~p’s andΣ’s). Fork≥ 2, ~pk is the top homogeneous
component of weightk of the observable
∑
µ=1m12m2···sms
|µ|+𝓁(µ)=k
k↓𝓁(µ)
∏
i≥1mi!
∏
i≥1
(Σi)mi.
Examples. Let us write the ﬁrst~pk’s in the linear basis of central characters(Σµ)µ∈⨆
n∈N Pn:
~p1 = 0 ; ~p2 = 2Σ1
~p3 = 3Σ2 ; ~p4 = 4Σ3 + 6Σ1,1 + 2Σ1
~p5 = 5Σ4 + 20Σ2,1 + 15Σ2
~p6 = 6Σ5 + 30Σ3,1 + 15Σ2,2 + 20Σ1,1,1 + 30Σ1,1 + 60Σ3 + 2Σ1
Hence, one sees for instance that~p6 is the top homogeneous component of6Σ5+30Σ3,1+15Σ2,2+20Σ1,1,1,
and if one uses the factorization property of the central characters, one sees that these formulas agree
with Proposition 2.
8 PIERRE-LOÏC MÉLIOT
3. Some computations around the limit shapes Ωc
By using observables of diagrams, it is very easy to prove Theorem 1; let us recall brieﬂy this proof.
If λ is a partition of sizen picked randomly according to a Schur-Weyl measure, then any observable of
diagram f∈ O yields a random variablef(λ). When f = Σµ, the expectation of the random variable
Σµ(λ) is easy to compute:
SWn,α,c[Σµ] =
{
n↓|µ| tr(C N)⊗n(σµ⊔1n−|µ|) if n≥|µ|,
0 otherwise,
≃n→∞ n|µ|N𝓁(µ)−|µ|≃c|µ|−𝓁(µ)n
|µ|+𝓁(µ)
2 ,
assuming thatα = 1/2 andc> 0. In particular,SWn,α,c[Σµ] is aO
(
n
wt(Σµ )
2
)
, and since theΣµ’s form a
linear basis ofO, one concludes that for any observablef,
SWn,α,c[f] =O
(
n
wt(f )
2
)
.
Now,Σµ and Rµ+1 have the same top homogeneous component, so ifRµ =Rµ1Rµ2··· Rµr, then
SWn,α,c[Rµ]≃c|µ|−2𝓁(µ)n
|µ|
2 ; SW n,α,c[Rµ(λ∗)]≃c|µ|−2𝓁(µ)
for any partitionµ without part of size1. It implies the convergence in probabilityRk(λ∗)→ ck−2 for
anyk≥ 2, whence the existence of limit shapesΩc with
RΩc(z) =Rc(z) = 1
z
(
1 +
∞∑
n=2
cn−2zn
)
= 1
z + z
1−cz
GΩc(z) =Gc(z) = c +z−
√
(z−c)2− 4
2(1 +cz) = 2
z +c +
√
(z−c)2− 4
where the holomorphic square root is deﬁned onC \ R − and chosen so that
√
1 = 1.
A careful analysis shows that these generating functions are indeed those of the continuous diagrams of
Theorem 1,cf. [Bia01, §3]. In the following, we are rather interested in the computation of the transition
measuresµc =µΩc and of the observables~hn(Ωc) and~pn(Ωc). Let us begin with the transition measures:
8 PIERRE-LOÏC MÉLIOT
3. Some computations around the limit shapes Ωc
By using observables of diagrams, it is very easy to prove The orem 1; let us recall brieﬂy this proof.
If λ is a partition of size n picked randomly according to a Schur-Weyl measure, then any observable of
diagram f ∈ O yields a random variable f (λ).W h e n f = Σ µ,t h ee x p e c t a t i o no ft h er a n d o mv a r i a b l e
Σ µ(λ) is easy to compute:
SWn,α ,c[Σ µ]=
{
n↓|µ| tr(
 N )⊗n (σµ⊔1n−|µ| ) if n ≥ |µ|,
0 otherwise,
≃n→∞ n|µ| N 𝓁(µ)−|µ| ≃ c|µ|−𝓁(µ) n
|µ|+𝓁(µ)
2 ,
assuming that α =1 /2 and c> 0. In particular, SWn,α ,c[Σ µ] is a O
(
n
wt(Σ µ )
2
)
,a n ds i n c et h eΣ µ’s form a
linear basis of O,o n ec o n c l u d e st h a tf o ra n yo b s e r v a b l ef ,
SWn,α ,c[f ]= O
(
n
wt(f )
2
)
.
Now, Σ µ and Rµ+1 have the same top homogeneous component, so if Rµ = Rµ1 Rµ2 ··· Rµr ,t h e n
SWn,α ,c[Rµ] ≃ c|µ|−2𝓁(µ) n
|µ|
2 ;S W n,α ,c[Rµ(λ∗)] ≃ c|µ|−2𝓁(µ)
for any partition µ without part of size 1.I t i m p l i e s t h e c o n v e r g e n c e i n p r o b a b i l i t yRk(λ∗) → ck−2 for
any k ≥ 2,w h e n c et h ee x i s t e n c eo fl i m i ts h a p e sΩc with
RΩc (z)= Rc(z)= 1
z
(
1+
∞∑
n=2
cn−2zn
)
= 1
z + z
1 − cz
GΩc (z)= Gc(z)= c + z −
√
(z − c)2 − 4
2(1 + cz) = 2
z + c +
√
(z − c)2 − 4
where the holomorphic square root is deﬁned on
 \
 − and chosen so that
√
1=1 .
Ac a r e f u la n a l y s i ss h o w st h a tt h e s eg e n e r a t i n gf u n c t i o n sa rei n d e e dt h o s eo ft h ec o n t i n u o u sd i a g r a m so f
Theorem 1, cf. [Bia01, §3]. In the following, we are rather interested in th ec o m p u t a t i o no ft h et r a n s i t i o n
measures µc = µΩc and of the observables ~hn(Ωc) and ~pn(Ωc).L e t u s b e g i n w i t h t h e t r a n s i t i o n m e a s u r e s :
c =0
c =1
c =1 /2
c =2
Figure 7. Deformations of the Wigner semicircle law corresponding to Schur-Weyl mea-
sures with parameters α =1 /2, c> 0.
Figure 7. Deformations of the Wigner semicircle law corresponding to Schur-Weyl mea-
sures with parametersα = 1/2, c> 0.
KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES 9
Proposition 3 (Limit shapes under Schur-Weyl measures and Marčenko-Pastur distributions). The tran-
sition measureµc is up to an homothetic transformation the Marčenko-Pastur distribution of parameter
c:
dµc≤1(s) = 1 s∈[c−2,c+2]
√
4− (s−c)2
2π(1 +cs) ds
dµc>1(s) = 1 s∈[c−2,c+2]
√
4− (s−c)2
2π(1 +cs) ds +
(
1− 1
c2
)
δ− 1
c
(s)
Notice that one recovers the Wigner semicircle law whenc = 0.
These Marčenko-Pastur distributions are in fact well-known, since they play the same role for Wishart
ensembles as the Wigner semicircle law for the GUE, see [MP67].
Proof. One uses the Perron-Stieltjes inversion formula:
dµc(s)
ds = lim
ε→0+
Gc(s− iε)−Gc(s + iε)
2iπ
which comes essentially from the calculus of residue. This formula holds for any real numbers such
that Gc stays bounded in the vicinity ofs. Suppose ﬁrst thatc <1. Then, the singularity ofGc(z) at
z =−1/c is removable, so the Perron-Stieltjes formula holds for anys. Ifs∈ ]c−2,c +2[, then(s−c)2−4
is a negative real number, so
lim
ε→0±
√
(s + iε)2− 4 =±i
√
4− (s−c)2.
The other terms inGc(z) are continuous atz =s, so
dµc(s∈ ]c− 2,c + 2[)
ds = (i
√
4− (s−c)2)− (−i
√
4− (s−c)2)
4iπ(1 +cs) =
√
4− (s−c)2
2π(1 +cs) .
If|s−c|≥ 2, then(s−c)2−4 is a non-negative real number, so the square root is continuous in a vicinity
of s. Consequently,
dµc(s /∈ ]c− 2,c + 2[)
ds = 0,
whence the formula forµc<1. Now, ifc≥ 1, then the Perron-Stieltjes formula do not hold anymore at
s =−1/c, and one has to add a Dirac to take account of the singularity ofGc(z) at this point. Since the
residue ofGc(z) at z =−1/c is
−1/c +c−
√
(c + 1/c)2− 4
2c =−(c− 1/c)−
√
(c− 1/c)2
2c =−
(
1− 1
c2
)
,
one obtains indeed the formula given by Proposition 3. □
Now, let us compute the observables~hn(Ωc) and ~pn(Ωc). Of course, it amounts to expand in power
series the functions
Hc(z) =z−1Gc(z−1) = 2
1 +cz +
√
(1−cz)2− 4z2
andPc(z) =zH′
c(z)/Hc(z), but the calculations are not at all trivial, and we shall need in particular the
following hypergeometric identity:
Lemma 4. For any non-negative integerm and k,
k∑
l=0
m∑
u=0
(2k + 2 +u− 2l) m + 2l + 2−u! 2k− 2l +u!
(m−u +l + 2)(m−u +l + 1)m−u!u!l!l + 1!k−l!k−l + 1! = m + 2k + 4
m +k + 2 × m + 2k + 2!
m!k!k + 2!.
10 PIERRE-LOÏC MÉLIOT
Proof. For such (multivariate) hypergeometric identities, one can use the theory of Wilf-Zeilberger, see
[PWZ97], [WZ92a] and [WZ92b]. More precisely, there is an algorithm that provides recurrence relations
satisﬁed by both sides of the identity, and on the other hand, it is easy to show that the identity holds
for certain values ofm and k. Consequently, the identity is indeed true for allm and k; we leave the
details of the computation of the recurrence relations to any computer algebra system. □
Proposition 5 (Observables of the limit shapes). The n-th moment of the lawµc is
~hn(Ωc) =µc(sn) =
⌊n
2⌋∑
k=1
n↓2k
(n−k + 1)(n−k)k!k− 1!cn−2k,
and then-th moment of interlacing coordinates is
~pn(Ωc) =
⌊n
2⌋∑
k=1
n↓2k
(n−k)k!k− 1!cn−2k.
Whenc = 0, one recovers the fact that the even moments of the semicircle law are the Catalan numbers:
~h2n(Ω0) =Cn.
Proof. The expansion of2/Hc(z) gives
2
Hc(z) = 1 +cz + (1−cz)
√
1− 4
( z
1−cz
)2
= 1 +cz + (1−cz)
(
1− 2
∞∑
m=0
Cm
( z
1−cz
)2(m+1))
= 2
(
1−
∞∑
m=0
Cm
z2m+2
(1−cz)2m+1
)
because∑∞
m=0Cmxm = 1−√1−4x
2x . Then,
Hc(z) = 1 +
∞∑
m=0
∞∑
r=1
{ ∑
m1+m2+···+mr=m
Cm1Cm2··· Cmr
}
z2m+2r
(1−cz)2m+r.
Let us denote byf(m,r ) the sum between brackets. One hasf(m, 0) = 0, f(m, 1) =Cm and f(m,r ) =
f(m + 1,r− 1)−f(m + 1,r− 2) because of the recurrence relation satisﬁed by Catalan numbers. Con-
sequently, one can show by induction that
f(m,r ) =r 2m +r− 1!
m!m +r! .
Finally, one can use the expansion 1
(1−cz)2m+r =∑∞
l=0
(2m+r+l−1
l
)
clzl to obtain:
Hc(z) = 1 +
∞∑
m=0
∞∑
r=1
∞∑
l=0
r 2m +r +l− 1!
l! 2m +r− 1!
2m +r− 1!
m!m +r! clz2m+2r+l
= 1 +
∞∑
n=2
zn



⌊n
2⌋∑
k=1
( k∑
r=1
r (n−r− 1)↓2k−r−1
k!k−r!
)
cn−2k



For any positive integersa, b and c,
( a+1
b+c+1
)
=∑
j≥1
(j
b
)(a−j
c
)
— this identity can be obtained combi-
natorially by grouping the parts of sizeb +c + 1 of [ [1,a + 1] ]according to the value of their(b + 1)-th
element. In particular,
∑
j≥1
j
(n−j− 1
n−k− 1
)
=
( n
n−k + 1
)
KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES 11
if one takesa =n− 1, b = 1 and c =n−k− 1. As a consequence, the term between parentheses in the
previous expression is just n↓2k
(n−k+1)(n−k)k!k−1!, whence the formula for the~hn(Ωc)’s.
As for the~pn(Ωc)’s, one can use Newton relations between the power sums and the complete homoge-
neous functions in the algebra of symmetric functions, or expand in power serie the functionPc(z) — it
leads to the same computations. First, one sees that:
Pc(z) =− z
1 +cz +
√
(1−cz)2− 4z2
(
c− c(1−cz) + 4z√
(1−cz)2− 4z2
)
= zHc(z)
2
(
c(1−cz) + 4z√
(1−cz)2− 4z2−c
)
= zHc(z)
2
(
c
∞∑
n=1
(2n
n
)( z
1−cz
)2n
+ 4
∞∑
n=0
(2n
n
)( z
1−cz
)2n+1)
= zHc(z)
2
(∞∑
n=0
∞∑
r=0
{
cz
(2n + 1 +r
r
)(2n + 2
n + 1
)
+ 4
(2n +r
r
)(2n
n
)}
crz2n+1+r
)
If n1≥ 2, then the coeﬃcient ofzn1 in zHc(z) is~hn−1(Ωc), that is to say:
⌊n1−1
2 ⌋∑
k=1
n1− 1!
(n1−k)(n1−k− 1)k!k− 1!n1− 1− 2k!cn1−2k−1
On the other hand, ifn2≥ 1, then the coeﬃcient ofzn2 in the second termTc(z) of the productPc(z) is:
⌊n2
2⌋−1∑
l=0
n2− 1!
n2− 2l− 2!l!l + 1!cn2−2l−1+ 2
⌊n2−1
2 ⌋∑
l=0
n2− 1!
n2− 2l− 1!l!l!cn2−2l−1 = 1
n2
⌊n2−1
2 ⌋∑
l=0
n2 + 1!
n2− 2l− 1!l!l + 1!cn2−2l−1
One also has to take account of the coeﬃcient ofz in zHc(z), that is equal to1. So, for n≥ 3, the
coeﬃcient ofzn in Pc(z) is equal to the sum of the following expressions:
A = 1
n− 1
⌊n
2⌋∑
k=1
n!
n− 2k!k!k− 1!cn−2k
B =
∑
n1+n2=n
n1≥2, n2≥1
2≤2k1≤n1−1
0≤2k2≤n2−1
(n2 + 1)n1− 1!n2− 1!n1−k1− 2!
n1−k1!k1!k1− 1!n1− 2k1− 1!n2− 2k2− 1!k2!k2 + 1!cn−2k1−2k2−2
=
∑
n1+n2=n−3
n1≥0, n2≥0
0≤2k1≤n1−1
0≤2k2≤n2
(n2 + 2)n1 + 1!n2!n1−k1− 1!
n1−k1 + 1!k1!k1 + 1!n1− 2k1− 1!n2− 2k2!k2!k2 + 1!cn−2k1−2k2−4
=
∑
0≤u≤n−4−2k
0≤k=k1+k2
f(k1,k 2,u,n )n− 2k2− 2−u! 2k2 +u!
n−u− 2k− 4!u!k1!k1 + 1!k2!k2 + 1!cn−2k−4
where f(k1,k 2,u,n ) = 2k2+2+u
(n−u−k1−2k2−2)(n−u−k1−2k2−3). Consequently,~pn(Ωc) is indeed a polynomial inc
with all terms of even degree or all terms of odd degree. The term of degreen− 2 comes exclusively from
A, and is
1
n− 1
n!
n− 2! =n = n↓2
n− 1 1! 0!,
12 PIERRE-LOÏC MÉLIOT
so the formula of Proposition 5 is true for the coeﬃcient ofcn−2. For the other coeﬃcients, one has to
show that ifk≥ 0 and n− 2k− 4≥ 0, then
∑
0≤u≤n−4−2k
k=k1+k2
f(k1,k 2,u,n )n− 2k2− 2−u! 2k2 +u!
n−u− 2k− 4!u!k1!k1 + 1!k2!k2 + 1! = n↓2k+4
(n−k− 2)(n− 1)k + 2!k!.
Indeed, the left-hand side comes fromB, and the right-hand side is the diﬀerence of the coeﬃcient in the
formula of Proposition 5 and of the coeﬃcient coming fromA. Up to a change of index, this last identity
is exactly Lemma 4. Finally, it is easy to verify that the formula for the moments~pn(Ωc) remains true
for n = 1, 2. □
These calculations are of course unessential, but we shall need the precise expression of the moments
~pn(Ωc) in our study of the ﬂuctuations∆λ,c(s) =λ∗(s)− Ωc(s).
