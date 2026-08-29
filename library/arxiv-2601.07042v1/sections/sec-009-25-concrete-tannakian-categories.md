---
doc_id: arxiv-2601.07042v1
doc_title: "A TANNAKIAN DESCRIPTION OF THE LOCAL KALETHA GERBE"
section_id: sec-009-25-concrete-tannakian-categories
section_title: "Concrete Tannakian categories"
section_number: 2.5
pages: 12-14
source_pdf: 2601.07042v1.pdf
source_sha256: c2f3e302624e7abb
doc_brief: "A TANNAKIAN DESCRIPTION OF THE LOCAL KALETHA GERBE — We construct, for ap-adic fieldF, an explicit semisimple Tannakian categoryRigIsoc F whose category of fiber functors recovers Kaletha’s Galois"
---
subsection in terms of a more concrete Tannakian category overF.
First we define the categoryI E{F,s for a fixedsPN; its objects are triplespV, ˜Φ,DqwhereVis a finite
dimensionalL E vector space, ˜Φis aΓ LE{F -semilinear action ofW LE{F onV, andDis a ś
ΓE{F
1
s Z-
grading ofV, such thatV paσ{sqσ has anL E-basis on whichf s
E PW LE{F acts by ś
σPΓE{F
σpϖEqaσ, and that
forxPΓ LE{F lifting¯xPΓ E{F , we have that ˜ΦpxqpVpaσqσq“V pa¯x´1σqσ. The categoryI E{F,s has a natural
tensor structure defined such thatpV, ˜ΦqbpV 1, ˜Φ1q“pVbV 1, ˜Φb ˜Φ1qwhere ˜Φˆ ˜Φ1 is given explicitly by
p˜Φb ˜Φ1qpσqpvbv 1q“ ˜Φpσqpvqb ˜Φ1pσqpv1q.
The identity object1ofI E{F consists of theLE vector spaceLE with ˜Φequal to the normal Galois action.
It is easy to check that the endomorphisms of1are in canonical bijection withF.
We now construct a functorT:W E{F,s ÑI E{F,s. Given an objectpX,X
fγ
ÝÑβγpXqqofW E{F,s, we
let the vector spaceVin theT-image ofpX,X
fγ
ÝÑβγpXqqbe the underlying vector space ofXand we
let the gradingDbe the grading onX. We define ˜Φas follows. For anyσPW LE{F we can write uniquely
σ“f n
EsEpγqfor someγPΓ E{F . Then we define
˜Φpσqpvq“Φ npf´1
γ pvb1qq.
We note thatf´1
γ issEpγqsemilinear onVby definition.
To show that ˜Φis indeed aΓ LE{F -action, we need to verify forσ 1,σ 2 PΓ LE{F that ˜Φpσ1q˝ ˜Φpσ2q “
˜Φpσ1σ2q. Explicitly, ifσi“f ni
EsEpγiq, then we must show that
pΦn1˝f ´1
γ1 q˝pΦ n2˝f ´1
γ2 q“Φ n1`n2`cEpγ1,γ2qf´1
γ1γ2.
By construction, we have
f´1
γ1γ2“f ´1
γ1 ˝f ´1
γ2 ˝Φ´cEpγ1,γ2q,
which implies the desired equality.
We also need to check that ˜Φacts on the grading correctly. LetγPΓ E{F . Then we have
˜ΦpsEpγqqpVpaσ{sqσq“f ´1
γ pVpaσ{sqσb1q“f ´1
γ pβγpVqpaγ´1σ{sqσq“V paγ´1σ{sqσ.
Finally,Tis a functor because morphisms ofW E{F,s must necessarily commute with theΦandf γ maps.
12
We now define a functorS:I E{F,s ÑW E{F,s, giving a quasi-inverse ofT. Given an objectpV, ˜Φ,Dq
ofI E{F,s, we define its image underSto have underlying vector space equal toVand ś
ΓE{F
1
s Z-gradingD.
We defineΦto be ˜ΦpfEq. Finally, for our fixed sections E : ΓE{F ÑW LE{F , we definef γ :VÑβ γpVq
by
fγ :vÞÑ ˜ΦpsEpγqq´1pvqb1.
There are many things we need to check in the above definition. First, we check thatfγ is an isomorphism
off E-spaces fromVtoβ γpVqfor a fixedγ. It is evidently an isomorphism of abelian groups, and isf E-
equivariant, since we have, forvPV, the identity
˜ΦpsEpγqq´1pfE¨vqb1“ ˜ΦpsEpγq´1qp˜ΦpfEqpvqqb1“ ˜ΦpsEpγq´1fEqpvqb1
“ ˜ΦpfEsEpγq´1qpvqb1“f E¨p ˜ΦpsEpγq´1qpvqqb1“f E¨p ˜ΦpsEpγqq´1pvqqb1,
where we have used thatf E is contained inZpW LE{Fq. We also haveL E-linearity due to the identity, for
ℓPL E, given by
˜ΦpsEpγq´1qpvbℓq“s Epγq´1pℓq˜ΦpsEpγq´1qpvqb1“ ˜ΦpsEpγq´1qpvqbℓ.
We now check that the mapsf γ satisfy the cocycle condition with respect toβ γ andµ γ1,γ stated in the
previous subsection. Recall that this condition is given by the equation
pµγ1,γqpXq˝f γ1γ“β γ1pfγq˝f γ1
for anyXPW E{F,s. In our setting, this equation is
˜ΦpcEpγ1,γq´1q˝ ˜ΦpsEpγ1γqq´1“ ˜ΦpsEpγqq´1˝ ˜ΦpsEpγ1qq´1,
which is trivial from the definition of the cocyclec E, since ˜Φis a group action. It follows that the above
functor gives a well-defined object ofWE{F,s. Any morphism inI E{F,s gives a morphism inWE{F,s, since
morphisms inIE{F,s preserve the grading by construction and commute with theWLE{F -action, and there-
fore with the mapsf γ. Both functorsSandTare evidentlyF-linear tensor functors. We thus immediately
obtain:
Corollary 2.10.The gerbe overpSch{Fq fpqc corresponding to the Tannakian categoryI E{F,s overFhas
band which is isomorphic as anF-group scheme to Res E{FpGmq.
It is not hard to see how this generalizes to give a more concrete interpretation of the categoryRWE{F,s.
Recall theW LE{F -action ˜ΦRE{F on the ringR E{F defined in the previous subsection. We now define the
categoryRI E{F,s, whose objects consist of tuplespV,D, ˜ΦqwhereVis anL E-vector space andDis aś
ΓE{F
1
s Z-grading onV. The graded vector spaceVis equipped with an action of the graded ringR E{F and
we require thatVis finitely generated as anR E{F -module. Finally, ˜Φis a semilinear action ofW LE{F on
Vsuch that ˜Φpγqprvq“ ˜ΦRE{Fpγqprq ˜ΦpγqpvqforrPR E{F , and such thatV pbσ{sqσ has anL E-basis upon
which ˜Φpfs
Eqacts by scaling by ś
σPΓE{F
σpϖEqbσ. To simplify notation, we will often denote˜Φpγqpvqsimply
byγ¨vorγv. The categoryRI E{F,s is Tannakian overFwith identity objectR E{F . An identical argument
to the one above proves that the functorsTandSmay be extended to inverse functors ˜S, ˜TbetweenRI E{F,s
andRW E{F,s, showing that the former is banded by theF-group scheme Res E{Fpµsq. By “extended," we
mean in the sense that the diagram of quotient functors
WE{F,s IE{F,s
RWE{F,s RIE{F,s,
13
where the left vertical arrow the quotient functor discussed in the previous subsection, and the right vertical
arrow is the functor which sends the objectpV,D, ˜Φqto the objectpVb LE RE{F,D1, ˜Φb ˜ΦRE{Fq, where
D1 is the grading induced by tensoring the grading ofVwith that ofR E{F . Fors 1{s, there is a clear tran-
sition functor fromI E{F,s toI E{F,s1, same forRI E{F,s, and one checks that the above equivalences with
