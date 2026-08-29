---
doc_id: arxiv-1105.0091v1
doc_title: "E-mail: meliot@phare.normalesup.org"
section_id: sec-005-7-jones-ocneanu-traces-of-hecke-algebras-and-qt
section_title: "Jones-Ocneanu traces of Hecke algebras and (q,t)-Plancherel measures"
section_number: 7
pages: 57-70
source_pdf: 1105.0091v1.pdf
source_sha256: 7d6f72e016b25027
doc_brief: "E-mail: meliot@phare.normalesup.org — In this paper, we review the representation theory of the inﬁnite symmetric group, and we extend the works of Kerov and Vershik by proving that the irreducible"
---
measures
In this last section, we return to the “algebraic” study of the probability
measures Pn,ω, and we introduce new observables in O related to the rep-
resentation theory of the Hecke algebras H (Sn), that are deformations of
the symmetric group algebrasCSn. We then determine their asymptotic be-
haviour under the probability measuresPn,ω, thereby proving aq-analog of
Theorem 17. Finally, we study the systems of coherent measures coming from
the Jones-Ocneanu traces of the Hecke algebras (cf. §7.2); they form a(q,t )-
deformation of the system of Plancherel measures described on page 11, see
§7.3.
7.1 Hecke algebras of the symmetric groups
Let us ﬁx a non-negative integern. We recall that the (generic)Iwahori-
Hecke algebraof the symmetric groupSn is the C(q)-algebra H (Sn) gen-
erated by elementsT1,T 2,...,T n−1, with presentation:



∀i≤n− 1, (Ti−q)(Ti + 1) = 0 ;
∀i≤n− 2, TiTi+1Ti =Ti+1TiTi+1 ;
∀i,j, |j−i|≥ 2⇒TiTj =TjTi.
Alinearbasisof H (Sn)consistsinthe Tσ =Ti1Ti2··· Ti𝓁(σ),where σ runsover
Sn and σ = si1si2··· si𝓁(σ) is any reduced decomposition ofσ in elementary
transpositions. Thus,H (Sn) is a quantization of the symmetric group algebra
CSn. In fact, it has the same representation theory: it is a semisimpleC(q)-
algebra,anditsirreduciblemodules Vλ(q)arelabelledbytheintegerpartitions
of sizen and have the same dimensions as the irreducible representationsVλ
58 Pierre-Loïc Méliot
of Sn, and the same branching rules (see [Mat99], and [GP00] for more details
on the Iwahori-Hecke algebras in the general setting of Coxeter groups).
As in the case of the symmetric groupSn, the character theory ofH (Sn)
can be encoded in the algebraSym of symmetric functions,cf. [Ram91]. A
normalized trace on H (Sn) is a functionτ : H (Sn)→ C(q) that satisﬁes
the two hypotheses:
1. τ is tracial:∀a,b, τ (ab) = τ (ba).
2. τ is normalized so thatτ (1) = 1.
The condition of positivity is a little more subtle than in the case of the sym-
metric group. First, for any value ofq∈ C, we denoteHq(Sn) = H (Sn)⊗C(q)
C the specialized Hecke algebra obtained by sending the variableq to its value.
This specialized Hecke algebra is a semisimple algebra isomorphic to CSn
(whence with the same representation theory) as soon asq⁄= 0 and q is not
a non-trivial root of unity; in particular, it is the case whenq∈ R∗
+. Then,
assuming q∈ R+∗, a positive normalized trace, or character onHq(Sn) is a
normalized trace Hq(Sn)→ C such that (see [KV89]):
3. For allσ1,...,σ r in Sn, (τ (TσiTσ−1
j
))1≤i,j≤r is hermitian and non-negative
deﬁnite.
As in the group case, any trace onH (Sn) is a C(q)-linear combination
of the irreducible charactersζλ(q) of the modulesVλ(q) of H (Sn); we shall
also denote byχλ(q) the normalized irreducible character ofVλ(q). A trace on
Hq(Sn) withq∈ R∗
+ is positive if and only if it is a positive linear combination
of theζλ(q). Ifµ = (µ1,...,µ r) is a partition inYn, let us denote
Tµ = (T1··· Tµ1−1)(Tµ1+1··· Tµ1+µ2−1)··· (Tµ1+···+µr−1+1··· Tµ1+···+µr−1).
Then, any elementh∈ H (Sn) is conjugated modulo[H (Sn), H (Sn)] to a
unique linear combination of elementsTµ,µ∈ Yn (cf. [GP00, §8.2] or [Ram91,
§5]). So, a traceτ : H (Sn)→ C(q) is entirely determined by the valuesτ (Tµ),
and the character theory ofH (Sn) is given by the character table
(
ζλ(q,µ ) = ζλ(q,Tµ)
)
λ,µ∈Yn
.
Now, using the notations introduced in §1.2, for any partitionµ, we set
qµ(q,X ) = hµ(qX−X)
(q− 1)𝓁(µ) ,
where hµ = ∏𝓁(µ)
i=1 sµi is the homogeneous symmetric function of type µ;
qµ(q,X ) is an element of Sym⊗C C(q). A generalization of the Frobenius
formula 1 reads as follows (see [Ram91, Theorem 4.14]):
A central limit theorem for the characters ofS∞ and H (S∞) 59
Proposition 27. For any partitionµ∈ Yn,
qµ(q,X ) =
∑
λ∈Yn
ζλ(q,µ )sλ(X).
Then, using exactly the same arguments as in the case ofS∞, we get the
q-analog of Thoma’s theorem 3:
Theorem 28. Supposeq∈ R∗
+. The set of extremal charactersX∗(Hq(S∞))
can be identiﬁed (homeomorphically) with the Thoma simplexΩ, and the char-
acter χω(q) corresponding to a pointω = (α,β )∈Ω writes as
χω(q,Tµ) = qµ(q,A−B +γE ).
The decomposition ofχω(q)|Hq(Sn) in irreducible characters is
χω(q) =
∑
λ∈Yn
Pn,ω[λ]χλ(q),
where Pn,ω[λ] = (dim λ)sλ(A−B +γE ) exactly as before.
This result provides “new” coherent systems of probability measures on
Y =⨆
n∈N Yn comingfromcharactersof Hq(S∞)insteadofcharactersof S∞.
Moreover, letting the parameterq vary in R∗
+, we will obtain one-parameter
families of coherent systems. In the following, we will investigate the (asymp-
totic) behaviour of certain families coming from the so-called Jones-Ocneanu
traces of H (S∞). The theory developed in the previous paragraphs holds
again; however, in the setting of the Hecke algebras, it seems more appriopri-
ate to enounce the algebraic central limit theorem 17 forq-characters instead
of characters. The end of this paragraph is devoted to this problem.
Forλ and µ partitions, we introduce as in §3.1 the symbol
Σµ(q,λ ) =
{
n(n− 1)... (n−|µ| + 1)χλ(q,µ⊔ 1n−|µ|) if n =|λ|≥| µ|,
0 otherwise.
At ﬁrst sight, it is not clear that the functionsΣµ(q) are observables of di-
agrams in the algebraO. However, one can expand the symmetric functions
qµ(q,X ) as combinations of power sumspµ(X), and therefore write theq-
characters as linear combinations of characters, see [Ram91, Theorem 5.4] and
[FM10, Proposition 10]:
∀λ,µ, (q− 1)𝓁(µ)ζλ(q,Tµ) =
∑
|ν|=|µ|
(qν− 1)⟨hµ|pν⟩
⟨pν|pν⟩ ζλ(ν)
60 Pierre-Loïc Méliot
Here, for a partitionν, qν− 1 is an abbreviation for∏𝓁(ν)
i=1 qνi− 1. From this,
one deduces that theΣµ(q) are indeed observables of diagrams, and that they
are related to theΣµ by the following relations (notice that the change of basis
is triangular):
(q− 1)𝓁(µ)Σµ(q) =
∑
|ν|=|µ|
(qν− 1)⟨hµ|pν⟩
⟨pν|pν⟩ Σν;
(qµ− 1)Σµ =
∑
|ν|=|µ|
(q− 1)𝓁(ν)⟨pµ|mν⟩ Σν(q).
Let us ﬁx a parameterω∈Ω. Theorem 17 ensures that the variables
∆n,ω(µ) =√n
(Σµ(λ)
n|µ| −pµ(ω)
)
with λ∼ Pn,ω converge jointly to a gaussian vector; since theΣµ(q)’s are
linear combinations of theΣµ’s, the same result holds for the variables
∆n,ω(q,µ ) =√n
(Σµ(q,λ )
n|µ| −qµ(q,ω )
)
.
We denote by∆∞,ω(q,µ ) the limiting gaussian variables; their covariances
k(∆∞,ω(q,µ (1)),∆∞,ω(q,µ (2))) are equal by bilinearity to
∑
|ν(i)|=|µ(i)|
Cµ(1),µ(2),ν(1),ν(2) (q) k(∆∞,ω(ν(1)),∆∞,ω(ν(2)))
=
∑
|ν(i)|=|µ(i)|
a∈ν(1),b∈ν(2)
ab Cµ(1),µ(2),ν(1),ν(2) (q)
( pa+b−1(ω)
pa(ω)pb(ω)− 1
)
,
where
Cµ(1),µ(2),ν(1),ν(2) (q) = (qν(1)⊔ν(2)
− 1)
(q− 1)𝓁(µ(1))+𝓁(µ(2))
⟨
hµ(1)
⏐⏐pν(1)
⟩⟨
hµ(2)
⏐⏐pν(2)
⟩
zν(1)zν(2)
.
Theorem 29. As n goes to inﬁnity, ifλ∼ Pn,ω, then the variables
√n
(
χλ(q,µ )−χω(q,ω )
)
converge jointly to a gaussian vector, whose covariance matrix is given by the
formula above.
In particular, whenµ(1) =l andµ(2) =m are partitions of length1, the scalar
products
⟨
hµ(i)
⏐⏐pν(i)
⟩
are all equal to 1 by Frobenius formula 1, and thus,
k(∆∞,ω(q,l ),∆∞,ω(q,m )) is equal to
1
(q− 1)2
∑
ν(1)∈Yl
ν(2)∈Ym
pν(1)⊔ν(2) (qω−ω)
zν(1)zν(2)


∑
a∈ν(1)
b∈ν(2)
ab
( pa+b−1(ω)
pa(ω)pb(ω)− 1
)

.
A central limit theorem for the characters ofS∞ and H (S∞) 61
In the general case, it does not seem possible to simplify this formula; however,
we obtained a simpliﬁcation in the case of theq-Plancherel measures, see
[FM10] and [Mél10].
7.2 Jones-Ocneanu traces and their weights
AMarkov trace(also-calledJones-Ocneanu trace, [Jon87]) onH (Sn)
is a normalized trace that satisﬁes the additional condition:
∀k∈ [ [1,n− 1] ], ∀a∈ H (Sk),τ (Tka) = τ (Tk)τ (a) = zτ (a).
If z is a ﬁxed parameter, there is a unique corresponding Markov trace on
H (Sn), characterized by the valuesτz(Tµ) = z|µ|−𝓁(µ).
Proposition 30. LetXq,z = [1−q+z]−[z]
1−[q] denote the formal alphabet that cor-
responds to the following specialization ofSym:
∀k≥ 1, pk(Xq,z ) = (1−q +z)k−zk
1−qk .
The decomposition ofτz in irreducibleq-characters is
τz =
∑
λ∈Yn
sλ(Xq,z )ζλ(q).
Proof. The result is due to Ocneanu (unpublished notes) and Wenzl (see
[Wen88]); we give here a very short proof. If Yq,z = qXq,z− Xq,z, then
pk(Yq,z ) = (qk− 1)pk(Xq,z ) = zk− (1−q +z)k. Consequently,
P (u) =
∞∑
k=1
pk(Yq,z )
k uk = log
( 1−u(1−q +z)
1−uz
)
H(u) =
∞∑
k=0
hk(Yq,z )uk = expP (u) = 1−u(1−q +z)
1−uz .
Hence, hk(Yq,z ) = (q− 1)zk−1, and
qµ(q,Xq,z ) = hµ(Yq,z )
(q− 1)𝓁(µ) =
𝓁(µ)∏
i=1
zµi−1 =z|µ|−𝓁(µ) =τz(Tµ).
Now, because of theq-Frobenius formula 27, for any partitionµ,
τz(Tµ) = qµ(q,Xq,z ) =
∑
λ∈Yn
sλ(Xq,z )ζλ(q,Tµ).
Since a trace is characterized by its values on theTµ’s, the result follows
immediately.
62 Pierre-Loïc Méliot
There is a hook length formula for the specializationssλ(Xq,z ) of the Schur
functions, see for instance [Mac95, §1.3]:
sλ(Xq,z ) = qn(λ) ∏
@∈λ
(1−q) +z(1−qc(@))
1−qh(@)
wheren(λ) =∑𝓁(λ)
i=1 (i− 1)λi, and if@ = (i,j ) is a box of the Young diagram of
λ,c(@) = i−j is thecontent of @. Now, let us make the change of variables:
z =−(1−q)(1−t).
Then, assuming thatq∈ R∗
+ and t∈ [0, 1], one sees thatsλ(Xq,z ) is positive,
because
sλ(Xq,z ) = qb(λ)
∏
@∈λ{h(@)}q
(∏
@∈λ
t + (1−t)qc(@)
)
with{i}q = 1−qi
1−q for any positive integeri. Another way to see thatsλ(Xq,z )
is positive in this situation is to notice that
Xq,z =A−B,
whereA andB are the alphabets associated to the point of the Thoma simplex
ωq,t = (αq,t,βq,t), with
αq,t = [t(1−q)]
1− [q] = (t(1−q),t (1−q)q,t (1−q)q2,... );
βq,t = [(1−t)(1−q)]
1− [q] = ((1−t)(1−q), (1−t)(1−q)q, (1−t)(1−q)q2,... ).
In particular:
Proposition 31. If z =−(1−q)(1−t) with t∈ [0, 1] and q∈ R∗
+, then the
Markov traceτz is an irreducible (positive) character ofHq(S∞), and it is
equal toχωq,t with ωq,t deﬁned by the formulas above.
Example. Suppose thatt = 1. Then,z = 0 and τ = τ0 is theregular trace
of Hq(S∞):
∀ω∈ S∞, τ (Tω) =
{
1 if ω = 1,
0 otherwise.
Although the deﬁnition of the regular does not seem to depend on the value
of q, the weights ofτ in its decomposition in irreducible characters vary with
q:
∀n, τ|Hq(Sn) = (1−q)n ∑
λ∈Yn
(dimλ)sλ(1,q,q 2,... )χλ(q).
The probability measures corresponding to this decomposition have been stud-
ied extensively in [FM10]. In the following, we generalize the results of this
paper by using the general theorems proved in Sections 4 and 5.
A central limit theorem for the characters ofS∞ and H (S∞) 63
7.3 (q,t )-Plancherel measures and their asymptotics
Forq∈ R∗
+ and t∈ [0, 1], we call(q,t)-Plancherel measureof sizen
the probability measure Pn,q,t on Yn corresponding to the decomposition of
the Markov traceτz withz =−(1−q)(1−t). In other words,Pn,q,t = Pn,ωq,t,
and
Pn,q,t[λ] = (1−q)n (dimλ) sλ
( [t]− [t− 1]
1− [q]
)
.
The (q,t )-Plancherel measures have the following symmetry:
Pn,q,t[λ] = Pn,q−1,t[λ′].
Hence, we shall always suppose thatq∈ ]0, 1[, the other case following by a
symmetry.
Remark. Whenq goes to1, one recovers the usual Plancherel measures deﬁned
on page 11
Pn,q=1,t[λ] = Pn[λ] = (dimλ)2
n! .
Hence, the(q,t )-Plancherel measures form a two-parameter deformation of the
coherent system of Plancherel measures. They are also a generalization of the
q-Plancherel measures deﬁned in [Ker92,Str08] and studied in [FM10].
Using the results of §2, one can interpret the(q,t )-Plancherel measures as
push-forwards of probability measures on the symmetric groups. Let us detail
a little bit these measures Qn,q,t such that Λ⋆Qn,q,t = Pn,q,t. We could of
course takeQn,q,t[σ] = Qn,ωq,t [σ], but it will be a little bit easier13 to describe
the probability measures
Qn,q,t[σ] = Qn,ωq,t [σ−1] = Fσ(ωq,t) = Lc(σ)(ωq,t).
Taking σ−1 instead of σ does not change the fact that Λ⋆Qn,q,t = Pn,q,t,
becausethebilateralKazhdan-Lusztigcells {σ∈ Sn| Λ(σ) = λ}arestabilized
by the inversionσ↦→ σ−1. Now, for any compositionc∈ Cn, if comaj(c) =∑
d∈D(c)n−d, then
∀q∈ ]0, 1[, Lc(1,q,q 2,... ) = qcomaj(c)
(1−q)(1−q2)··· (1−q)n,
13 In return, we lose the direct interpretation of the random permutations as generalized
shuﬄes.
64 Pierre-Loïc Méliot
see [Sta91, §7.19]. Using the deﬁnition of the specializationLc(ω) (cf. Para-
graph 2.2), one sees that:
Qn,q,t[σ] = Lc(σ)(ωq,t) =
n∑
i=0
Lc(σ)[ [1,i] ](αq,t)Lc(σ)[ [i+1,n] ]
(βq,t)
=
n∑
i=0
Lc(σ)[ [1,i] ](αq,t)Lc(σω0)[ [1,n−i] ](βq,t)
=
n∑
i=0
ti (1−t)n−i
{i!}q{n−i!}q
qcomaj(c(σ)[ [1,i] ])+comaj(c(σω0)[ [1,n−i] ]).
For w word of sizen, we set Qn,q[w] = qcomaj(w)
{n!}q
; for anyq∈ R∗
+, Qn,q is a
probability measure onSn.
Proposition 32. As t varies in [0, 1], the measuresQn,q,t provide an inter-
polation betweenQn,q[σ] and Qn,q[σω0]:
Qn,q,t[σ] =
n∑
i=0
ti (1−t)n−i Qi,q[σ[ [1,i] ]] Qn−i,q[(σω0)[ [1,n−i] ]]
whereσ[ [1,i] ]denotes the wordσ(1)σ(2)··· σ(i), and similarly for(σω0)[ [1,n−i] ].
It wasa priori a non trivial fact that these interpolations correspondvia
RSKtotheweightsoftheMarkovtraces τ−(1−q)(1−t).Ontheotherhand,letus
notice that the partsQi,q[σ[ [1,i] ]] Qn−i,q[(σω0)[ [1,n−i] ]] of Qn,q,t[σ] have a simple
geometric interpretation. Ifσ is a permutation, let us draw its corresponding
ribbon, see §2.1. We draw a line after thei-th box, and we deﬁnemi(σ) as the
sum of the following quantities:
–for each box ∨ before the line and with another box just under, the
distance between∨ and the line in the ribbon;
–for each box < after the line and with another box just at the left, the
distance between < and the line in the ribbon.
Then, the i-th weight is simply qmi (σ)
{i!}q{n−i!}q
; for instance, ifi = 5 and σ =
64182357, thenmi(σ) = (4 6 + 34 + 18) + (03 + 15 + 27) = 11.
6
4
1 8
2 3 5 7 =
∨
∨
∨
< < < .
A central limit theorem for the characters ofS∞ and H (S∞) 65
Now, let us describe the asymptotics of the (q,t )-Plancherel measures.
First, we give the algebraic central limit theorem, noticing that
pk(ωq,t) = (tk− (t− 1)k)(1−q)k
1−qk
for anyk≥ 1.
Proposition 33.Ifλ∼ Pn,q,t, then asn goes to inﬁnity, the random variables
√n
(
χλ(q,Tl)− (t− 1)l−1(1−q)l−1)
converge jointly to a gaussian vector(∆∞,q,t(q,l ))l≥1 with covariances
(1−q)−l−m+2k(∆∞,q,t(q,l ),∆∞,q,t(q,m ))
=
∑
ν(1)∈Yl
ν(2)∈Ym
a∈ν(1),b∈ν(2)
(t− 1)ν−tν
zν(1)zν(2)
( 1−ua+b−1
1−qa+b−1
1−u
1−q
1−qa
1−ua
1−qb
1−ub− 1
)
whereu = t−1
t , ν =ν(1)⊔ν(2), and (t− 1)ν−tν =∏𝓁(ν)
i=1 ((t− 1)νi−tνi ).
Remark. Whent = 1, this formula can be simpliﬁed by using a Möbius inver-
sion formula, and it becomes
k(∆∞,q,t(q,l ),∆∞,q,t(q,m )) = (q−q2)l+m−3 (1−q2){l− 1}q{m− 1}q
{l +m− 1}q{l +m− 2}q{l +m− 3}q
see [Mél10].
Now, let us give the geometric version of the central limit theorem. We
have drawn below a random Young diagram taken according to the(q,t )-
Plancherel measure of parametersn = 300, q = 1
2 and t = 2
3. Withq = 1
2,
{
λ =( 1 0 1↪ 49↪ 30↪ 14↪ 8↪... )
λ′ =( 5 4↪ 30↪ 17↪ 11↪ 8↪... )
10
Fig. 8 A random Young diagram under a(q,t )-Plancherel measure.
66 Pierre-Loïc Méliot
it is not hard to see that the ﬁrst rows and the ﬁrst columns seem to follow
geometric progressions of reason 1
2. Moreover, witht = 2
3, the ratio between
the ﬁrst row and the ﬁrst column seems to be close tot
1−t = 2. This is in
adequation with Theorems 15 and 19 that state the following (notice that we
are in the case of inequal coordinates):
Proposition 34. If λ∼ Pn,q,t, then
λi =nt (1−q)qi−1 +n1/2Xi +o(n1/2);
λ′
j =n (1−t)(1−q)qj−1 +n1/2Yj +o(n1/2),
where (Xi,Yj)i≥1,j≥1 is a gaussian vector with covariances
k(Xi,Xj) = δi,jt(1−q)qi−1−t2(1−q)2qi+j−2;
k(Yi,Yj) = δi,j (1−t)(1−q)qi−1− (1−t)2(1−q)2qi+j−2;
k(Xi,Yj) =−t(1−t)(1−q)2qi+j−2.
In particular, fort = 1, we recover Theorems 1 and 2 of [FM10]. Proposition 34
also gives the asymptotic behaviour of the length of a longest increasing or de-
creasing subword in a random permutation taken according to the probability
measure described in Proposition 32.
Conclusion
Let us summarize the results obtained in this paper:
1. To any irreducible character ofS∞ or of Hq(S∞) with q∈ R∗
+, we have
associated a pointω in the Thoma simplexΩ, and two random models:
a model (Qn,ω)n∈N of random permutations obtained by generalized riﬄe
shuﬄes, and a model(Pn,ω)n∈N of random partitions related to the restric-
tion of the irreducible character to the ﬁnite symmetric groups or their
Hecke algebras.
2. The computation of the probabilities of both models can be done using
specializations of combinatorial Hopf algebras: the Hopf algebraFQSym
for the permutations, and the Hopf algebraSym for the partitions. This
interpretation enabled us to see that the two models are related by the
RSK correspondence.
3. The model of random partitions satisﬁes a law of large numbers and a
central limit theorem. In both cases, the asymptotic result can be given an
algebraic ﬂavour (for the values of the characters), or a geometric ﬂavour
(for the ﬁrst rows and columns of the partitions). The geometric central
limit theorem is much more involved than the other results, and cannot
be proved by using only techniques of moments. Hence, one had to relate
random permutations and partitions to some conditioned random walks,
and to the behaviour of the eigenvalues of brownian hermitian matrices.
A central limit theorem for the characters ofS∞ and H (S∞) 67
Whenω = 0, our methods do not describe with suﬃcient precision the asymp-
totic behaviour of the random partitions; however, they can be adapted to this
purpose, see [IO02]. One obtains again a law of large numbers and a central
limit theorem, and this CLT seems to have a universality property;cf. [Mél11].
Hence, the next step in the asymptotic study of the models presented in this
article would be to understand what happens “in the neighbourhood” of the
point 0 of the Thoma simplex. More precisely, we would like to understand
what happens whenω varies withn and converges to0. Let us give a concrete
example — this is one of the two cases studied in [Mél11], and we refer also
to [Bia01]. Suppose that
ωn =
(( 1
N,..., 1
N, 0, 0,...
)
, (0, 0,... )
)
,
with N coordinates equal to 1
N, andcN≃√n. Then, there is a limit shape
for the random partitionsλ∼ Pn,ωn; it has been found by P. Biane in [Bia01],
and it is drawn on Figure 9 in the case whenc = 1.
11
Fig. 9 Random partition under the Schur-Weyl measure of parameterc = 1.
Now, the interesting fact is that the ﬂuctuations of the partitions under
these measures (calledSchur-Weyl measures) are described by a gaussian
free ﬁeld that does not depend onc (or, to be more precise, only by a trans-
lation of the ﬂuctuations on thex-axis). More generally, we conjecture the
following (the statement is willingly left unprecise):
68 Pierre-Loïc Méliot
Conjecture 35.This asymptotic behaviour is universal among models of ran-
dom partitions associated to parameters(ωn)n∈N converging to0 at speed1/√n
as n goes to inﬁnity.
There is one example whose study would be very interesting in order to
prove this conjecture — it has been suggested by M. Bożejko. In some sense,
the Schur-Weyl measures provide another one-parameter deformation of the
Plancherel measures: indeed, whenc goes to 0, the limit shape of the parti-
tions under Schur-Weyl measures converges to the one corresponding to the
Plancherel measures. On the other hand, the limit shapes under Schur-Weyl
measures correspond via the Markov-Krein correspondence (see [Ker98]) to
the Marčenko-Pastur measures, that are a one-parameter deformation of the
Wigner semicircle law (correspondingvia Markov-Krein to the limit shape of
the random partitions under Plancherel measures). Now, thefree Meixner
laws (see e.g. [BB06]) form a two-parameter deformation of the Wigner mea-
sure, and they generalize the Marčenko-Pastur laws. So it would be extremely
interesting to construct models of random partitions corresponding to these
laws, and to study their ﬂuctuations. One can hope that with two parame-
ters, the computations will be suﬃciently generic in order to understand the
behaviour of random partitions in the general situation of Conjecture 35. The
results of this paper have been obtained in a similar way: starting from the
q-Plancherel measures already studied in [FM10], we have gone to the case of
(q,t )-Plancherel measures, and we have then realized that our results hold in
fact for any model of random partitions associated to a point of the Thoma
simplex.
References
AGZ09. G. W. Anderson, A. Guionnet, and O. Zeitouni. An Introduction to Random
Matrices, volume 118 ofCambridge Studies in Advanced Mathematics. Cambridge
University Press, 2009.
AS05. M. Aguiar and F. Sottile. Structure of the Malvenuto-Reutenauer Hopf algebra of
permutations. Adv. Math., 191(2):225–275, 2005.
BB06. M. Bożejko and W. Bryc. On a class of free Lévy laws related to a regression
problem. J. Funct. Anal., pages 59–77, 2006.
BBO05. P. Biane, P. Bougerol, and N. O’Connell. Littelmann paths and brownian paths.
Duke Math. J., 130(1):127–167, 2005.
Bia01. P. Biane. Approximate factorization and concentration for characters of symmetric
groups. Internat. Math. Res. Notices, 4:179–192, 2001.
Bia09. P. Biane. From Pitman’s theorem to crystals.Advanced Studies in Pure Mathe-
matics, 55:1–13, 2009.
Bil69. P. Billingsley. Convergence of Probability Measures. Wiley, 1969.
Bri69. D. Brillinger. The calculation of cumulants via conditioning. Ann. Inst. Statist.
Math., 21:375–390, 1969.
DFŚ10. M. Dołega, V. Féray, and P. Śniady. Explicit combinatorial interpretation of Kerov
character polynomials as numbers of permutation factorizations. Adv. Math.,
225(1):81–120, 2010.
A central limit theorem for the characters ofS∞ and H (S∞) 69
DHT01. G. Duchamp, F. Hivert, and J.-Y. Thibon. Noncommutative symmetric functions
VI: Free quasi-symmetric functions and related algebras.arXiv:math/0105065v1,
2001.
Dys62. F. J. Dyson. A brownian-motion model for the eigenvalues of a random matrix.
J. Math. Phys., 3:1191–1198, 1962.
FM10. V. Féray and P.-L. Méliot. Asymptotics of q-Plancherel measures. To appear in
Probability Theory and Related Fields, arXiv:1001.2180v1 [math.RT] , 2010.
Ful97. W. Fulton. Young Tableaux with Applications to Representation Theory and Ge-
ometry, volume 35 ofLondon Mathematical Society Students Texts. Cambridge
University Press, 1997.
Ful02. J. Fulman. Applications of symmetric functions to cycle and increasing subse-
quence structure after shuﬄes.J. Alg. Combin., 16:165–194, 2002.
Ges94. I. M. Gessel. Multipartite P-partitions and inner products of skew Schur functions.
InCombinatorics and algebra (Boulder, Colo., 1983), pages 289–317. Amer. Math.
Soc., 1994.
GK10. R. Gohm and C. Köstler. Noncommutative independence from characters of the
inﬁnite symmetric groups∞. arXiv:1005.5726, 2010.
GP00. M. Geck and G. Pfeiﬀer.Characters of Finite Coxeter Groups and Iwahori-Hecke
Algebras, volume 21 ofLondon Mathematical Society Monographs. Oxford Uni-
versity Press, 2000.
IK99. V. Ivanov and S. Kerov. The algebra of conjugacy classes in symmetric groups, and
partial permutations. In Representation Theory, Dynamical Systems, Combina-
torial and Algorithmical Methods III, volume 256 ofZapiski Nauchnyh Seminarov
POMI, pages 95–120, 1999.
IO02. V. Ivanov and G. Olshanski. Kerov’s central limit theorem for the Plancherel mea-
sure on Young diagrams. InSymmetric Functions 2001: Surveys of Developments
and Perspectives, volume 74 ofNATO Science Series II. Mathematics, Physics
and Chemistry, pages 93–151, 2002.
JK81. G. D. James and A. Kerber. The Representation Theory of the Symmetric Group,
volume 16 ofEncyclopedia of Mathematics and its Applications. Addison-Wesley,
1981.
Jon87. V. F. R. Jones. Hecke algebra representations of braid groups and link polynomials.
Ann. of Math., 126(2):335–388, 1987.
Ker92. S. V. Kerov. q-analogue of the hook walk algorithm and random Young tableaux.
Funct. Anal. Appl., 26(3):179–187, 1992.
Ker93. S. V. Kerov. Gaussian limit for the Plancherel measure of the symmetric group.
Comptes Rendus Acad. Sci. Paris, Série I, 316:303–308, 1993.
Ker98. S. V. Kerov. Interlacing measures. Amer. Math. Soc. Transl., 181(2):35–83, 1998.
KO94. S. V. Kerov and G. Olshanski. Polynomial functions on the set of Young diagrams.
Comptes Rend. Acad. Sci. Paris, Série I, 319:121–126, 1994.
KOV04. S. V. Kerov, G. Olshanski, and A. M. Vershik. Harmonic analysis on the inﬁnite
symmetric group. Invent. Math., 158:551–642, 2004.
KV77. S. V. Kerov and A. M. Vershik. Asymptotics of the Plancherel measure of the
symmetric group and the limiting form of Young tableaux.Doklady AN SSSR,
233(6):1024–1027, 1977.
KV81a. S. V. Kerov and A. M. Vershik. Asymptotic theory of characters of the symmetric
group. Funct. Anal. Appl., 15(4):246–255, 1981.
KV81b. S. V. Kerov and A. M. Vershik. Characters and factor representations of the
inﬁnite symmetric group.Soviet Math. Doklady, 23:389–392, 1981.
KV84. S. V. Kerov and A. M. Vershik. Characters, factor representations and K-functor
of the inﬁnite symmetric group. InProc. Intern. Conf. on Operator Algebras and
Group Representations 1980, volume 2 ofMonographs and Studies in Mathemat-
ics, pages 23–32. Pitman, London, 1984.
KV89. S. V. Kerov and A. M. Vershik. Characters and realizations of representations of
an inﬁnite-dimensional Hecke algebra, and knot invariants.Soviet Math. Doklady,
38(1):134–137, 1989.
Lit95. P. Littelmann. Paths and root operators in representation theory. Ann. Math.,
142(3):499–525, 1995.
70 Pierre-Loïc Méliot
LLT02. A. Lascoux, B. Leclerc, and J.-Y. Thibon. The plactic monoid. In Algebraic
Combinatorics on Words. Cambridge University Press, 2002.
LS77. B. F. Logan and L. A. Shepp. A variational problem for random Young tableaux.
Adv. Math., 26:206–222, 1977.
Mac95. I. G. Macdonald. Symmetric functions and Hall polynomials. Oxford Mathemat-
ical Monographs. Oxford University Press, 2nd edition, 1995.
Mat99. A. Mathas. Iwahori-Hecke algebras and Schur algebras of the symmetric group,
volume 15 ofUniversity Lecture Series. Amer. Math. Soc., 1999.
Mél10. P.-L. Méliot. Gaussian concentration of the q-characters of the Hecke algebras of
type A. arXiv:1009.4288v1 [math.RT] , 2010.
Mél11. P.-L. Méliot. Kerov’s central limit theorem for Schur-Weyl and Gelfand measures.
Toappearintheproceedingsofthe23thInternationalConferenceonFormalPower
Series and Algebraic Combinatorics (Reykjavik), 2011.
MR95. C. Malvenuto and C. Reutenauer. Duality between quasi-symmetric functions and
Solomon descent algebra.J. Algebra, 177:967–982, 1995.
O’C03. N. O’Connell. A path-transformation for random walks and the Robinson-
Schensted correspondence. Trans. Amer. Math. Soc., 355:3669–3697, 2003.
Oko97. A. Okounkov. On representations of the inﬁnite symmetric group. Representa-
tion theory, dynamical systems, combinatorial and algorithmic methods II (A. M.
Vershik, ed.).Zapiski Seminarov POMI, 240:167–229, 1997.
OV04. A. Okounkov and A. M. Vershik. A new approach to the representation theory of
the symmetric groups, II.Zapiski Seminarov POMI, 307:57–98, 2004.
OY02. N. O’Connell and M. Yor. A representation for non-colliding random walks.Elec-
tron. Comm. Probab., 7:1–12, 2002.
Pit75. J.W.Pitman. One-dimensionalBrownianmotionandthethree-dimensionalBessel
process. Advances in Applied Probability, 7:511–526, 1975.
Ram91. A. Ram. A Frobenius formula for the characters of the Hecke algebras.Invent.
Math., 106:461–488, 1991.
Rob38. G. Robinson. On the representations of the symmetric group. Amer. J. Math.,
60(3):745–760, 1938.
RY91. D. Revuz and M. Yor.Continuous Martingales and Brownian Motion, volume 293
of Grundlehren der mathematischen Wissenschaften. Springer-Verlag, 3rd edition,
1991.
Sch61. C. Schensted. Longest increasing and decreasing subsequences.Canadian Journal
of Mathematics, 13:179–191, 1961.
Śni06a. P. Śniady. Asymptotics of characters of symmetric groups, genus expansion and
free probability.Discrete Math., 306(7):624–665, 2006.
Śni06b. P. Śniady. Gaussian ﬂuctuations of characters of symmetric groups and of Young
diagrams. Probability Theory and Related Fields, 136(2):263–297, 2006.
Sta91. R. P. Stanley. Enumerative combinatorics. Cambridge University Press, 1991.
Sta01. R. P. Stanley. A generalized riﬄe shuﬄe and quasisymmetric functions.Annals of
Combinatorics, 5:479–491, 2001.
Str08. E. Strahov. A diﬀerential model for the deformation of the Plancherel growth
process. Adv. Math, 217(6):2625–2663, 2008.
Tha87. D. H. Thang. Random operators in Banach spaces.Probability and Mathematical
Statistics, 8:155–167, 1987.
Tho64. E. Thoma. Die unzerlegbaren, positive-deﬁniten Klassenfunktionen der abzählbar
unendlichen symmetrischen Gruppe.Math. Zeitschrift, 85:40–61, 1964.
VV95. M. V. Velasco and A. R. Villena. A random Banach-Steinhaus theorem. Proc.
Amer. Math. Soc., 123(8):2489–2497, 1995.
Was81. A. J. Wassermann. Automorphic actions of compact groups on operator algebras.
Ph.D. Thesis, University of Pennsylvania, 1981.
Wen88. H. Wenzl. Hecke algebras of typeAn and subfactors. Invent. Math., 92:349–383,
1988.
Zel81. A. Zelevinsky. Representations of ﬁnite classical groups: A Hopf algebra approach,
volume 869 ofLecture Notes in Mathematics. Springer-Verlag, 1981.
