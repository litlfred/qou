---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere Chris Li"
section_id: sec-006-local-models-of-excellent-morse-failures
section_title: "Local Models of Excellent Morse Failures"
section_number: null
pages: 38-46
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere Chris Li — We give two presentations for bordisms ofS 2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
Proposition 3.2.2 gives the existence of commutative Frobenius relations among CF
generators. We would like to know if they are sufficient– namely, are there other
necessary relations if one wants to give a presentation of the category Cob(3) S2,CF ?
This section introduces a tool which we calllocal models of failures, which the next
section uses alongside theorem 3.3.6 to prove sufficiency.
Definition 3.4.1.(Local Model) Letf:M→Rbe a Morse function. A local model
of critical points and indices ((m j,ij))n
j=1 is a connected submanifoldU⊂Malong
with a Morse decomposition induced byf| U:
U∼=U1∪X1U2∪X2∪···∪ Xn−1Un⊂M.
such that eachU j is an elementary cobordism with critical pointm j∈U j of indexi j
satisfying
f(m 1)≤f(m 2)≤···≤f(m n).
If it is clear from context which critical points (m j) and which submanifoldUare
being considered, we say the local model is of (i j) onU. Note that a local model onU
by definition is equipped with a inducing Morse function defined on at leastU.
We say two local modelsU ∼=∪i∈IUi,V ∼=∪i∈IVi are diffeomorphic if there exists a
diffeomorphismh:U→Vsuch thath(U j) =V j preserves each boundary components
(as a set, not necessarily acting as the identity on each boundary component) andh
sends critical points to corresponding critical points.
Conventions 3.4.2.This is a subtle convention. Given two local modelsU i,U′
i of the
same critical points onM, we assume that they are two Morse decompositions of the
same underlying connected submanifoldU⊂M. This is so that we can speak of a
path of functions between two local models: it is a path of functions on a submanifold
Ubetween the two Morse functions inducing the two local modelsU i andU ′
i.
38
Definition 3.4.3.(Path of functions between two local models) Letf 0,f 1 :M→R
be Morse functions inducing two different local models on a connected submanifold
U⊂M. A path of functions between local models ofUis a pathf t :I×U→Rfrom
f0|U tof 1|U. Note we do not require thatf t be defined on all of the ambient manifold
M.
Example 2.For the associativity relation ofS 2, figure 3.2-(a) gives two local models
forU=Mand there exists an evident path of local models of (1,1). This path is
described by smoothly moving the two index 2 critical points towards each other in
height, and their critical values ultimately coincide and cross. In this case this path
of local models is the same as a path of Morse functions on the wholeM, which
exchanges the critical values of the two critical points. Note that the local models are
notdiffeomorphic: it exchanges boundary components.
Example 3.Consider the two torus Σ 1 =S 1×S 1 withUthe shaded region in figure
3.8. Equip the torus on the left with the standard height function. In figure (a),U
has no critical points, so it is itself a trivial local model. In figure (b),Uhas an index
1 critical point and an index 2 critical point. In order to induce this on the same
Σ1, the Morse function on Σ 1 is no longer the height function in figure b. However
standard Cerf theory shows there is a pathf t between the height function and the
Morse function inducing figure (b). When restricted toU, this path gives a pathf t|U
of functions between the trivial local model ofUand the local model of indices (1,2)
ofU.
(a) (b)
U U
Figure 3.8: A local model of the birth of a pair of critical points.
Notations 3.4.4.Letf 0,f 1 be two admissible excellent Morse functions onM, and
γ: [0,1]→C ∞(M) a path fromf 0 tof 1. Letf t =γ(t). Then standard Cerf theory
applies andft is admissible excellent Morse for all but finitely manyt, say at{t 1,...t n}.
1. We sayf ti is of failure type (j,j+ 1) B or (j,j+ 1) D if two critical points of index
j,j+ 1 were created or destroyed at timet i.
2. We sayf ti is of failure type (k,l) X if two critical points of indexk,lhave the
same critical value atf ti. The ordering is such thatf ti−ϵ(xk)<f ti−ϵ(xj) ifx k is
the critical point of indexk.
39
3. We sayf ti is of local failure type (j,j+ 1) B,D if it is of failure type (j,j+ 1) B,D.
4. We sayf ti is of local failure type (k,l) X,M,M′ if it is of failure type (k,l) X and
M,M′ are local models of (k,l) before and after the exchange.
5. We sayf ti is of trivial local failure type (k,l) X if it is of local failure type
(k,l)X,M,M′ whereM,M ′ are diffeomorphic local models of (k,l).
In this language, arelationbetween two (non-cylindrical) cobordism generators is
either a local failure type (j,j+ 1) B,D or a non-trivial local failure type (k,l) X,M,M′,
whereM,M ′ are not the same (i.e. diffeomorphic) local models. To classify relations
between CF generators, we want the local models before and after a failure to have
only spherical boundaries.
Remark3.4.5.The need to distinguish failure and local failure is because even though
birth/death is purely local, exchanges of critical values are not. However the purpose
of introducing local models is so we can isolate a local region and treat the whole region
as a whole. Although this is not usually a focal issue in standard Cerf theory or in
Cob(3)S2,CF , presently it is necessary to distinguish (1,1) X exchanges in Cob(2) by
their local models, as illustrated in the following example.
Example 4.Consider the standard height function on the two-torusT= Σ 1∼=S1×S1,
embedded inR 3 as in figure 3.9. Consider rotating the torus byθ(t) about thex-axis,
whereθ(t) =πt. Then there is a path of maps parametrized byt
ft :T= Σ 1∼=S1×S 1,→R 3 Rx(θ(t))
−→R 3 projz
−↠R.
such that atθ(0) = 0 one recovers the standard height function. As one increasest, the
critical values of the two index 1 critical points move towards each other, ultimately
coinciding at someθ c(tc). For a timet=t c +ϵslightly aftert c, the critical values
become distinct again.
Note however thatf tc is of trivial local failure type (1,1) X– the local models of
(1,1), before and after the exchange of critical values, are diffeomorphic– both are of
the form
pants∪S1⊔S1 copants.
Therefore in this tilting torus example, the exchange of the critical values of the
two index 1 critical points do not constitute a relation.
Example 5.By remark 3.2.3, the birth of the pair of critical points of index (1,2) is
not a relation between CF generators because the local model after the birth has torus
boundaries.
Example 6.If dim(M) = 2, the possible failure types are
{(0,1)B,(0,1) D,(1,2) B,(1,2) D,(1,1) X}.
The possible relations, aka non-trivial local failure types are
{(0,1)B,(0,1) D,(1,2) B,(1,2) D,(1,1) X,assoc,(1,1) X,coassoc,(1,1) X,Frobenius}.
where the pairs of local models are the evident ones.
40
0
1
1
2
2
0
1,1
Figure 3.9: The tilting torus. The figure on the left is the standard embedding of the 2-torus.
As one rotates the torus, the critical values of the index 1 critical points move towards each
other, ultimately coinciding as depicted in the right figure. The critical level set is depicted
as the two dashed circles wedged together at two points. For a better visualization, we
encourage the reader to cut a few donuts or bagles like so in real life.
Example 7.If dim(M) = 3, the possible failure types are
{(0,1)B,(0,1) D,(2,3) B,(2,3) D,(1,1) X,(2,2) X,(1,2) X}.
The possible relations, aka non-trivial local failure types are
{(0,1)B,(0,1) D,(2,3) B,(2,3) D,(1,1) X,assoc,(2,2) X,coassoc,(1,2) X,Frobenius}.
where the pairs of local models are the evident ones.
3.5 Sufficiency of Commutative Frobenius Re-
lations Among CF Generators
Recall that there is asilly functordefined in 3.3.5,
S: Cob(2)→Cob(3) S2,CF
sending disjoint unions ofn-copies ofS 1 to disjoint unions ofn-copies ofS 2, and the
genusgbordism
[Σg\int(⊔ninc+noutD2)] :⊔ nincS1→⊔ noutS1
to the bordism
[#g(S2×S 1)\int(⊔ ninc+noutD3)] :⊔ nincS2→⊔ noutS2.
41
Let’s examine what this functor does to local failure models. Unsurprisingly, it
maps Cob(2) non-trivial local failure types, to Cob(3) S2,CF relations by
(0,1)B,D7→(0,1) B,D
(1,2)B,D7→(2,3) B,D
(1,1)X,assoc7→(1,1) X,assoc
(1,1)X,coassoc7→(2,2) X,coassoc
(1,1)X,Frobenius7→(1,2) X,Frobenius
It also behaves well with the associated Morse data: note thatS([M]◦[N]) =
S([M])◦S([N]) andS([Σ g]) = [# gS2×S 1]. In particular, ifMis a representative
of [M] with Morse functionfinducing decompositionM=M 1∪···∪M n, then
there exists a manifoldNa representative ofS([M]) with Morse functionFinducing
decompositionN=N 1∪···∪N n such that the Morse decompositions are mapped to
each other:
S([Mi]) = [Ni],∀i= 1,...,n.
See figure 3.10 for a simple example. Note that there are infinitely many choices
of suchFonN, and, by composing with suitable monotonically increasing functions,
in fact infinitely manyFthat additionally has the same as critical values as those of
f. Therefore WLOG we impose the condition thatFhas the same critical values as
those off.
Notations 3.5.1.For simplicity and abusing the notations, we refer to any repre-
sentativeN∈S([M]) asS(M), and any Morse functionF:N→R, with the same
critical values asfand inducingN=N 1∪...N n such thatS([M i]) = [Ni], asS(f).
Naively, when one is given a morphism [M] in Cob(2) and two different compositions
related by a single 2-dimensional commutative Frobenius relation, one may use the silly
functorSon [M] and its two compositions to get a morphismS([M]) in Cob(3) S2,CF
with two compositions related by a 3-dimensional commutative Frobenius relation.
Because the silly functorS: Cob(2)→Cob(3) S2,CF is an isomorphism, this also
works the other way around: given a morphism [N] in Cob(3) S2,CF and two distinct
compositions related by a single commutative Frobenius relation, one can use the in-
verse silly functor to getS −1([N]) in Cob(2) and two compositions related by a single
commutative Frobenius relations.
The next proposition 3.5.2 says that this process is repeatable, and in fact has a
Cerf-theoretic lift: given two Morse functionsf 0,f 1 :M→Rand a pathf t between
them, one can construct a pathF t betweenF 0,F 1 :S(M)→R, whereS(M) is a
representative ofS([M]), andF 0,1 is induced byf 0,1. Along this path except with at
finitely many isolated singularities, the function is not only admissible excellent Morse,
but importantly also spherical. The isolated singularities also match those (non-trivial)
singularities off t in the sense that they are theS-image of local failures.
The strategy of the proof is simple: to constructF t :S(M)→R, followf t :M→
Rand use it as a blueprint. More specifically, whenever one encounters a specific
singularity alongf t, isolates a local regionUof the manifoldMwhere the topology
change occurs, and consider its imageS(U) inS(M). All the commutative Frobenius
relations in Cob(3)S2,CF can be described by some basic paths ˜Ft, so we declare that
overS(U) the path of functions takes the form ˜Ft, and outsideUthe path of functions
42
1
2
1
11
0
2
3
2
11
0
M∈[M] S([M])∋S(M)
f
 S(f)
S
M1
M2
M3
M4
N1
N2
N3
N4
Figure 3.10: The behavior of Morse data under the isomorphismS: Cob(2)→Cob(3) S2.
S(f) :S(M)→Ris any Morse function such that it has the same critical values asf, and
induces decompositionS(M) =N 1∪···∪N n such thatS([M i]) = [Ni].
is constant. Then we can glue the two paths of functions together with a bump function
over a collared neighbourhood of∂S(U).
The reader is warned that the wording of the proposition and technical aspects of
the proof may obscure the intuition and the proof strategy outlined above.
Proposition 3.5.2.Let[M]be a morphism inCob(2)andf 0,f 1 :M→Rtwo admissi-
ble excellent Morse functions. Letf t be a path fromf 0 tof 1 whereft fails to be excellent
Morse at time{t 1<t 2<···<t n}of non-trivial local failure type{T 1,T 2,...,T n}, and
possibly of trivial local failure type(1,1) X at other times
bt1<···< btm
	
. Then there
exists a pathF t connectingS(f 0),S(f 1) :S(M)→Rwhich fails to be admissible excel-
lent spherical Morse only at time{t 1,...,t n}of local failure type{S(T 1),...,S(T n)}.
Proof.WLOG we can choose the critical values ofF 0 andF 1 to be the same as those
off 0,f 1. Indeed, for any{x 1<...x k}and{y 1<···<y k}, there exists a monotoni-
cally increasing smooth function mappingx i toy i, and we can always take a smooth
interpolation from the identity to this function.
Take a strict total ordering of all the times thatf t fails to be excellent Morse:
{τ1,τ 2,...,τ n+m}such that eachτ j is either in{t 1,...,t n}or
bt1,..., btm
	
, corre-
sponding to non-trivial local failures or trivial ones. Letϵ >0 be small enough such
that∩ m+n
j=1 (τj−ϵ,τ j +ϵ) =∅, or equivalently
∩n
i=1(ti−ϵ,t i +ϵ)∩ m
j=1 (btj−ϵ,btj +ϵ) =∅.
We shall construct the pathF t :I×M→RfromF 0 =S(f 0) toF 1 =S(f 1)
satisfying the desired property. First we split the pathf t inton+m+ 1 segments:
(0,τ 1−ϵ),(τ 1 +ϵ,τ 2−ϵ),...,(τ n+m +ϵ,1).
43
Over any such segment,f t is excellent good Morse and the Morse data are diffeo-
morphic. For the “base case”, letF τ1−ϵ have the same critical values asf τ1−ϵ, and let
Ft be the smooth interpolation fromF 0 toF τ1−ϵ.
SupposeF t is defined up to and includingτ i−ϵ, we will constructF t up to and
includingτ i+1−ϵ. Over the interval (τi−ϵ,τ i +ϵ),f t fails to be excellent Morse exactly
once atτ i. There are three possible cases:
1. the failure is of trivial local failure type (1,1) X.
The Morse data before and after the failure are diffeomorphic, meaningf τi−ϵ and
fτi+ϵ have diffeomorphic Morse decompositions. Therefore we letF t be a smooth
interpolation fromF τi−ϵ toF τi+1−ϵ, whereF τi+1−ϵ =S(f τi+1−ϵ) has the same
critical values asf τi+1−ϵ.
2. the failure is of non-trivial local failure type (j,j+ 1) B or (j,j+ 1) D.
We will constructF t over the time interval (τi−ϵ,τ i +ϵ) such thatF t is of local
failure typeS((j,j+ 1) B,D) att=τ i.
The birth or death of a pair of critical points of indices (S(j),S(j)+1) is described
locally by a path ˜Ft provided by standard Cerf theory. LetU⊂S(M) be a
neighbourhood over which ˜Ft is defined. Outside ofU⊂S(M), we can take
˜Gt : (τi−ϵ,τ i +ϵ)×U c→Rto be the same asF τi−ϵ|Uc for allt∈(τ i−ϵ,τ i +ϵ).
We then glue ˜Fand ˜Gtogether using a bump function, and set the result to be
the desiredFt over the interval (τi−ϵ,τi+ϵ). We then take a smooth interpolation
fromF τi+ϵ toF τi+1−ϵ =S(f τi+1−ϵ).
3. the failure is of non-trivial local failure type (j,k) X,w,w′ wherew,w ′ are local
models of (j,k) before and after the exchange.
We will constructF t over the time interval (τi−ϵ,τ i +ϵ) such thatF t is of local
failure typeS((j,k) X,w,w′) att=τ i. We use a similar approach to the birth-death
type of failure, except instead of gluing a path defined on a neighbourhood, we
glue a path defined on the relevant local model.
First note that for any pairs of local models associated with theS-image of a
non-trivial local failure type, our settings are simple enough that there exists an
evident path of functions on the local model between the two inducing Morse
functions. So letU⊂S(M) be a local model induced byF τi−ϵ of the pair
of critical points of indexS(j),S(k) whose critical values are being exchanged,
namelyUis the underlying submanifold of the local modelS(w). Choose any
local model∪ lUl onUdiffeomorphic toS(w ′), then there exists a path of functions
˜Ft : (τi−ϵ,τ i +ϵ)×U→RfromF τi−ϵ|U to the Morse function inducing∪ lUl,
such that it is of the desired failure type att=τ i. OutsideU, we can take
˜Gt : (τi−ϵ,τ i +ϵ)×U c→Rto be the same asF τi−ϵ|Uc. Glue ˜Fand ˜Gtogether
to get the desiredF t : (τi−ϵ,τ i +ϵ) and take a smooth interpolation toS(f τi+1−ϵ)
at timeτ i+1−ϵ.
Since there are only finitely manytsuch thatf t fails to be excellent Morse, this
process eventually must terminate and all the smooth interpolations are taken from the
constructedF τi+ϵ toS(f 1). Also sinceF 0 is spherical, smooth interpolations preserves
spherical-ness, and all local failures are spherical except at the singular point, we have
that the constructed pathF t is admissible excellent spherical Morse at all but time
{t1,...,t n}.
44
The power of proposition 3.5.2 is that it allows a Cerf-path in Cob(2) to lift to a
spherical Cerf-path in Cob(3) S2,CF . Together with the silly functorS, we can show
that there is always a spherical Cerf-path between any admissible excellent spherical
Morse functions onN, a representative of a morphism [N] in Cob(3) S2,CF .
Proposition 3.5.3.Let[N]be a morphism inCob(3) S2,CF andF 0,F 1 :N→Rtwo
admissible excellent spherical Morse functions. Then there exists a pathF t inC ∞(N)
fromF 0 toF 1 which is admissible excellent spherical Morse at all but finitely manyt.
Moreover, the types of failure are of CF type.
Proof.Considerf 0 =S −1(F0) andf 1 =S −1(F1), both of which are Morse functions
onMa representative ofS −1([N]). Letf t be any path of functions fromf 0 tof 1 on
M. Then by proposition 3.5.2, there exists a pathF t fromS(f 0) =S(S −1(F0)) =F 0
toS(f 1) =S(S −1(F1)) =F 1 which fails to be admissible excellent spherical Morse at
finitely many times, and the types of failure are of commutative Frobenius type.
Corollary 3.5.4.CF bordism generators satisfy no more relations.
Remark3.5.5.Proposition 3.5.3 and corollary 3.5.4 addresses the major subtlety of the
isomorphism between Cob(2) and Cob(3) S2,CF : while two compositions of the same
morphism [N] in Cob(3)S2,CF are always induced by two Morse functionsF 0,F 1 :N→
R, a pathF !
t fromF 0 toF 1 may fail to be spherical. An example is example 1, where
F0 =F 1 :S 2×S 1→Rare both pants decompositions, but the pathF !
t has a segment
which is the Heegaard splitting, in particular not spherical.
However by proposition 3.5.3 and corollary 3.5.4, we now know that there is always a
pathFt fromF 0 toF 1 that is spherical all the way except at singularities of commutative
Frobenius type. So any two compositions of the same morphisms [N] in Cob(3) S2,CF
can always be turned into each other using only commutative Frobenius relations.
45
Chapter 4
