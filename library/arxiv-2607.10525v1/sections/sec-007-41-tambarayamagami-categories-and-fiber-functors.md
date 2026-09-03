---
doc_id: arxiv-2607.10525v1
doc_title: "FIBER FUNCTORS OF EQUIVARIANTIZATIONS OF FINITE TENSOR CATEGORIES"
section_id: sec-007-41-tambarayamagami-categories-and-fiber-functors
section_title: "Tambara–Yamagami categories and fiber functors"
section_number: 4.1
pages: 12-18
source_pdf: 2607.10525v1.pdf
source_sha256: b893cb4c87ea1d66
doc_brief: "FIBER FUNCTORS OF EQUIVARIANTIZATIONS OF FINITE TENSOR CATEGORIES — LetGbe a finite group acting on a finite tensor categoryC."
---
groupA, a nondegenerate symmetric bicharacterχ, andτ 2 =|A| −1, the category
TY(A,χ,τ)has simple objectsA∪{m}and fusion rules
a⊗b=a+b, a⊗m=m⊗a=m, m⊗m=
M
a∈A
a;
its associator is determined by(χ,τ)[TY98]. In particular,FPdim(m) =
p
|A|and
FPdim(TY(A,χ,τ)) = 2|A|.
The formχishyperbolicifA=L×L ′ withχtrivial onL×Land onL ′×L′;
otherwise it iselliptic. For|A|odd, Tambara’s classification states thatTY(A,χ,τ)
admits a fiber functor exactly whenτ−1 is a positive integer andχis hyperbolic. Its
fiber functors are then parametrized by the ordered decompositions(L,L′)of this
type [Tam00, Propositions 4.1 and 4.2].
4.2.The Hopf algebrasH p.Letpbe an odd prime,A p =C p×C p, and choose a
primitivepth root of unityξ∈k. We identifyF p-valued bilinear forms with bichar-
acters by exponentiating withξ, and use the convention
Alt(µ)(x,y) =µ(y,x)µ(x,y) −1, J=

0 1
−1 0

.
Set
χp((x1,x 2),(y 1,y 2)) =ξ x1y2+y1x2,C p = TY(Ap,χp,p−1).
The only Lagrangian subgroups of(Ap,χp)areL 1 =C p×{0}andL 2 ={0}×C p.
HenceC p has two fiber functors, represented by the ordered decompositions(L1,L 2)
and(L 2,L 1).
The involutiont(x,y) = (y,x)preservesχ p and induces a strictC 2-action onC p
withT t(a) =t(a)andT t(m) =m[Nik08, Proposition 2.10]. Nikshych’s Hopf algebra
Hp is characterized by
Rep(Hp)≃C C2
p ;
see [CM17, Theorem 1] for an explicit construction.
FIBER FUNCTORS OF EQUIV ARIANTIZATIONS 13
4.3.Classification of fiber functors forRep(H p).The only subgroups in Theo-
rem 3.6 areJ={e}andJ=C 2. The first gives theC2-orbits of fiber functors onCp.
In the second, Corollary 3.7 requires an indecomposable rank-twoCp-module category
with a free transitiveC2-action on its simples.
Lemma 4.1.TheT t-invariant indecomposable rank-twoCp-module categories are as
follows. Ifp≡3 (mod 4), there are none. Ifp≡1 (mod 4), there is exactly one
equivalence class.
Proof.With the convention fixed above, the map[µ]7→Alt(µ)identifiesH 2(Ap,k×)
with the alternating bicharacters onA p. Tambara uses the reciprocal convention
in [Tam00, Proposition 2.6], which gives the same parametrization.
By [Nik08, Lemma 4.3], every indecomposable rank-twoCp-module category is of
the form
Nµ = ModCp(R(Ap,µ)),
where[µ]̸= 0inH 2(Ap,k×). SinceA p has dimension two, every non-zero alternating
form onAp is nondegenerate. Thus there is a uniqueλ∈F×
p such that
Alt(µ) =λJ.
We first determine the equivalence class ofNµ. By [Nik08, Remark 4.5], restriction
to the pointed subcategory gives
Nµ|VecAp≃M(A p,µ)⊕M(A p,µ′),
where, ifSisthematrixofthesymmetricbicharacterχ p, theautomorphismιµ defined
in that remark satisfies
λJι µ =S, µ ′(x,y) =µ −1(ιµ(x),ιµ(y)).
Sinceι µ =−λ−1JSandS TJS= det(S)J, we obtain
Alt(µ′) =ι T
µ(−λJ)ιµ =− det(S)
λ J.
This is also the specialization of the translate formula in [MM12, Lemma 9.1]. For
the hyperbolic formχp,
S=

0 1
1 0

,det(S) =−1,
and hence
Alt(µ′) =λ−1J.
Consequently, the restriction ofNµ is encoded by the unordered pair
{λ,λ−1}.
This unordered pair is a complete invariant. Indeed, an equivalence ofCp-module cat-
egories restricts to an equivalence ofVecAp-module categories and therefore identifies
the two indecomposable summands, possibly after interchanging them. Conversely,
letx,ybe the two simple objects ofNµ, withEnd(x)≃R(A p,µ). The restriction for-
mula identifies the neutral part ofEnd(y)withR(A p,µ′). The fusion rules in [Nik08,
14 C. GALINDO, C. GALLEGO, AND Y. MORALES
Lemma 4.3] givem⊗y≃px, so the non-trivial graded component ofEnd(y)vanishes.
Therefore
End(y)≃R(A p,µ′).
Internal-Hom reconstruction [Nik08, Section 2.1] now gives
Nµ≃ModCp(R(Ap,µ′)) =N µ′.
Since the cohomology class of a cocycle onAp is determined by its alternating form,
the unordered pair is both necessary and sufficient. Thus the equivalence classes are
parametrized by
{λ,λ−1}, λ∈F ×
p.
The autoequivalenceTt, induced byt(x,y) = (y,x), sendsN µ toN tµ. Since
tTJt=−J,
it sendsλto−λ. HenceN µ isT t-invariant if and only if
{λ,λ−1}={−λ,−λ −1}.
Aspis odd andλ̸= 0, this is equivalent to
λ=−λ −1,or equivalentlyλ 2 =−1.
Ifp≡3 (mod 4), there is no solution. Ifp≡1 (mod 4), the two solutionsiand
−idetermine the same unordered pair becausei−1 =−i. Hence there is exactly one
Tt-invariant equivalence class.□
Lemma 4.2.Letsdenote the non-trivial element of the acting groupC 2; it acts on
Cp byT t. In the semidirect productD=C p ⋊C 2, let
em= [m,s],E ∆ =⟨[a,e] (a∈A p),em⟩.
ThenE ∆ is a Tambara–Yamagami fusion subcategory
E∆≃TY(A p,eχp,p−1),eχ p(a,b) =χ p(a,t(b)).
In coordinates,
eχp((x1,x 2),(y 1,y 2)) =ξ x1y1+x2y2.
Thuseχp is hyperbolic if and only ifp≡1 (mod 4).
Proof.Using the strict semidirect-product convention[X,g]⊗[Y,h] = [X⊗g ∗(Y),gh],
we obtain 
a,e

⊗[b,e] = [a+b,e],

a,e

⊗em≃em≃em⊗[a,e],
em⊗em≃
M
a∈Ap
[a,e].
Moreover,[a,e] ∗ = [−a,e]andem ∗≃em. ThusE ∆ has Tambara–Yamagami fusion
rules.
FIBER FUNCTORS OF EQUIV ARIANTIZATIONS 15
The action used to form the semidirect product is strict with identity tensor struc-
ture [Nik08, Proposition 2.10], so the relevant associators are inherited fromCp. For
a,b∈A p, they are
α [a,e],em,[b,e]=χ p(a,t(b)) id em,
α em,[a,e],em=
M
b∈Ap
χp(a,t(b)) id [b,e],
(α em,em,em)a,b =p−1χp(a,t(b))−1.
Here we used thattpreservesχ p. These are precisely the associativity data of
TY(Ap,eχp,p−1),eχ p(a,b) =χ p(a,t(b)).
In coordinates,
eχp((x1,x 2),(y 1,y 2)) =ξ x1y1+x2y2,
soeχp is represented by the identity matrix. It is hyperbolic precisely whenx2
1+x2
2 = 0
has a nonzero solution, or equivalently when−1is a square inFp. This is equivalent
top≡1 (mod 4); ifi 2 =−1, the two Lagrangian lines are⟨(1,i)⟩and⟨(1,−i)⟩.□
Proposition 4.3.Assume thatp≡1 (mod 4). The uniqueT t-invariant indecompos-
able rank-twoCp-module category admits aC2-equivariant structure whose non-trivial
element acts freely on its two simple objects. Moreover, the caseJ=C2 contributes
exactly one equivalence class of fiber functors onCC2
p .
Proof.Let
D=C p ⋊C 2.
We use the faithful grading
K:=Z/2Z×C 2,
where the first factor is the Tambara–Yamagami grading ofCp and the second is the
semidirect-product grading. Put
∆ ={(0,e),(1,s)}⊂K, γ= (0,s),
and let
E∆ =D (0,e)⊕D (1,s).
By Lemma 4.2,
E∆≃TY(A p,eχp,p−1),eχ p(a,b) =χ p(a,t(b)).
Sincep≡1 (mod 4), the formeχ p is hyperbolic. Ifi 2 =−1inF p, its two Lagrangian
lines are
L+ =⟨(1,i)⟩, L − =⟨(1,−i)⟩.
Tambara’s classification [Tam00, Propositions 4.1 and 4.2] therefore gives exactly
two rank-oneE ∆-module categories, denotedN + andN −, corresponding to the two
ordered decompositionsAp =L +×L− andA p =L−×L +. Fix either one and denote
it byN.
Consider the inducedD-module category
fM:= IndD
E∆(N) =D⊠ E∆N.
16 C. GALINDO, C. GALLEGO, AND Y. MORALES
By [Gal12, Propositions 3.5 and 3.7], the induced category is graded by the two right
cosets∆andγ∆. Accordingly, as a rightE ∆-module category,
D=E ∆⊕Dγ∆.
The object
u= [1,s]∈D γ
is invertible, and left tensoring byugives an equivalence of rightE∆-module categories
E∆−→Dγ∆, X7−→u⊗X.
Consequently,
fM≃N⊕N
as a semisimple category. In particular, fMhas exactly two simple objects, one in
each coset summand. The invertible objectuexchanges these two summands, sofM
is indecomposable as aD-module category.
Let
H=Z/2Z×{e}⊂K;D H =C p.
The homogeneous component of degree(1,e)sends the coset∆to(1,e)∆ =γ∆and
conversely. Hence the action of the non-zero object[m,e]∈D(1,e) sends either simple
object of fMto a non-zero multiple of the other. It follows that
ResD
Cp(fM)
is an indecomposable rank-twoCp-module category.
A module category overCp⋊C2 is equivalently aC2-equivariantCp-module category.
Thus the restricted module category isTt-invariant, and Lemma 4.1 identifies it with
the unique such rank-twoCp-module category. Moreover, the non-trivial element of
C2 acts throughu= [1,s], which exchanges the two simple objects. The action is
therefore free and transitive. SinceH 2(C2,k×) = 0, Corollary 3.7 shows that its
equivariantization has rank one, and hence defines a fiber functor onCC2
p .
It remains to prove uniqueness in the caseJ=C2. LetMbe anyC 2-equivariant
indecomposable rank-twoC p-module category whose non-trivial element acts freely
on simple objects, and regardMas aD-module category. Letx,ybe its two simple
objects. By the fusion-rule calculation in [Nik08, Lemma 4.3], everya∈A p fixes
bothxandy, whereas the non-invertible component ofC p interchanges them. Thus
the restriction ofMto
D(0,e) = VecAp
has two indecomposable rank-one summands, generated byxandy. The degree(1,e)
component interchanges these summands, and so does the degree(0,s)component
because the givenC 2-action is free. Their product degree(1,s)therefore stabilizes
each summand. Hence the stabilizer inKof eitherVecAp-summand is precisely∆.
The Clifford theorem for graded fusion categories [Gal12, Corollary 4.4] now gives
M≃D⊠ E∆N,
FIBER FUNCTORS OF EQUIV ARIANTIZATIONS 17
whereNis aE ∆-module category whose restriction toVecAp is one of the two rank-
one summands above. In particular,Nitself has rank one, so it is equivalent toN+
orN−.
Finally, the coset degreeγ= (0,s)normalizes∆. Conjugation byu= [1,s]acts
onE ∆ bytonA p and fixesem= [m,s]. Since
t(L+) =L−, t(L −) =L +,
the translated module category
Dγ∆ ⊠E∆N+
is equivalent toN− as anE ∆-module category. The equivalence criterion for induced
module categories [Gal12, Proposition 4.6] therefore implies
D⊠E∆N+≃D⊠ E∆N−.
Thus the caseJ=C 2 contributes exactly one equivalence class of fiber functors on
CC2
p . □
Theorem 4.4.Letpbe an odd prime, and letH p be Nikshych’s semisimple Hopf
algebra of dimension4p2, so that
Rep(Hp)≃C C2
p
as tensor categories. ThenRep(Hp)has one equivalence class of fiber functors ifp≡3
(mod 4), and two equivalence classes of fiber functors ifp≡1 (mod 4).
Proof.Since every subgroup ofC 2 is cyclic, its second cohomology with coefficients
ink× is trivial. Hence Corollary 3.7 applies.
We distinguish the two possible subgroupsJ⊆C2.
First letJ={e}. In this case the relevant data are the fiber functors ofC p,
modulo the action ofC2. By Tambara’s classification, the two fiber functors ofCp =
TY(Ap,χp,p−1)correspond to the two ordered Lagrangian decompositions
Ap =L 1×L 2 andA p =L 2×L 1.
The involutiont(x,y) = (y,x)exchangesL 1 andL 2, and hence exchanges these two
ordered decompositions. Therefore the caseJ={e}contributes one equivalence class
of fiber functors onCC2
p .
Now letJ=C 2. SinceH 2(C2,k×) = 0, the rank-one condition in Corollary 3.7
requires aC 2-equivariant indecomposableCp-module category whose non-trivial ele-
ment acts freely and transitively on its simple objects. Thus the underlyingCp-module
category must have rank two.
Ifp≡3 (mod 4), Lemma 4.1 shows that there is noT t-invariant indecomposable
rank-twoC p-module category. Hence the caseJ=C 2 contributes no fiber functor,
and the single class from the caseJ={e}is the whole list.
Ifp≡1 (mod 4), Proposition 4.3 shows that the uniqueT t-invariant indecompos-
able rank-twoCp-module category admits aC2-equivariant structure whose non-trivial
element acts freely on its two simple objects, and that the caseJ=C2 contributes
exactly one equivalence class of fiber functors.
18 C. GALINDO, C. GALLEGO, AND Y. MORALES
Finally, the two classes just obtained forp≡1 (mod 4)are not identified with each
other: they come from the subgroups{e}andC 2, respectively, and these subgroups
are not conjugate inC2. By Theorem 3.6, they therefore define distinct equivalence
classes. ThusRep(H p)≃C C2
p has one equivalence class of fiber functors ifp≡3
(mod 4), and two ifp≡1 (mod 4).□
