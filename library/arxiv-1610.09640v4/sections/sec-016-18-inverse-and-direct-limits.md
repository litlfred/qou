---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-016-18-inverse-and-direct-limits
section_title: "Inverse and Direct Limits"
section_number: 1.8
pages: 30-33
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
limits indexed by the ordered setN. For a general discussion see [101] or [75].
Let C be a category. Recall that anN-indexed direct systemin C is data
(
{Ck}k∈N,{µk}k∈N
{
,
where Ck are objects of C, and µk : Ck →Ck+1 are morphisms, that we call
transitions. A direct limitof this system is data
(
C,{ϵk}k∈N
{
, whereC∈C, and
ϵk : Ck →C are morphisms, that we callabutments, such that ϵk+1◦µk = ϵk
for allk. The universal property required is this: if
(
C′,{ϵ′
k}k∈N
{
is another pair
such thatϵ′
k+1◦µk = ϵ′
k, then there is a unique morphismϵ: C→C′such that
ϵ′
k = ϵ◦ϵk. If a direct limitC exists, then of course it is unique, up to a unique
isomorphism. We then write limk→Ck := C, and call this the direct limit of the
system{Ck}k∈N, keeping the transitions and the abutments implicit. Sometimes
we look at the morphisms
µk0,k1 :=µk1−1◦···◦µk0 :Ck0→Ck1
for k0 <k 1, andµk,k := idCk.
By anN-indexed inverse systemin the categoryC we mean data
(
{Ck}k∈N,{µk}k∈N
{
,
where{Ck}k∈N is a collection of objects, andµk : Ck+1 →Ck are morphisms,
also called transitions. Aninverse limitof this system is data
(
C,{ϵk}k∈N
{
, where
C∈C, andϵk : C→Ck are morphisms, that we also call abutments, such that
µk◦ϵk+1 =ϵk. These satisfy an analogous universal property. If an inverse limitC
exists, then it is unique, up to a unique isomorphism. We then writelim←kCk :=C,
and we call this the inverse limit of the system{Ck}k∈N. We deﬁne the morphisms
µk0,k1 :=µk0◦···◦µk1−1 :Ck1→Ck0
for k0 <k 1, andµk,k := idCk.
Exercise 1.8.1. We can view the ordered setN as a category, with a single mor-
phism k→l when k≤l, and no morphisms otherwise.
30
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(1) InterpretN-indexed direct and inverse systems inC as functorsF :N→C
and G :Nop→C respectively.
(2) Let ¯N := N∪{∞}. Interpret the direct and inverse limits of F and G
respectively as functors ¯F : ¯N→C and ¯G : ¯Nop→C, extendingF and G,
with suitable universal properties.
Exercise 1.8.2. Prove thatN-indexed direct and inverse limits exist in the cate-
gories Set and ModA, for any ringA. Give explicit formulas.
Example1.8.3. Let Mbethe categoryof ﬁnite abelian groups. The inverse system
{Mk}k∈N, whereMk :=Z/(2k), andthetransition µk :Mk+1→Mk isthecanonical
surjection, does not have an inverse limit inM. We can also make{Mk}k∈N into a
direct system, in which the transitionνk :Mk→Mk+1 is multiplication by2. The
direct limit does not exist inM.
If{Ck}k∈N is a direct system inC, andD∈C is any object, then there is an
induced inverse system
{
HomC(Ck,D )}k∈N in Set, and it has a limit. If C :=
limk→Ck exists, then the abutmentsϵk :Ck→C induce a morphism
(1.8.4) HomC(C,D )→lim
←k
HomC(Ck,D )
in Set.
Similarly, if{Ck}k∈N is an inverse system inC, andD∈C is any object, then
there is an induced inverse system
{
HomC(D,Ck)}k∈N in Set, and it has a limit. If
C := lim←kCk exists, then the abutmentsϵk :C→Ck induce a morphism
(1.8.5) HomC(D,C )→lim
←k
HomC(D,Ck),
in Set.
Proposition 1.8.6. Let C be a category.
(1) Let{Ck}k∈N be a direct system inC, and let
(
C,{ϵk}k∈N
{
be data as in the
deﬁnition of a direct limit. ThenC = limk→Ck if and only if for every
objectD∈C, the function(1.8.4) is bijective.
(2) Let{Ck}k∈N be an inverse system inC, and let
(
C,{ϵk}k∈N
{
be data as in
the deﬁnition of an inverse limit. ThenC = lim←kCk if and only if for
every objectD∈C, the function(1.8.5) is bijective.
Exercise 1.8.7. Prove Proposition 1.8.6.
Remark 1.8.8. In many cases inverse and direct limits do not exist inC because
“its objects are too small”. This happens in the categorySetﬁn of ﬁnite sets, and
also in the categoryAbﬁn of ﬁnite abelian groups (see Example 1.8.3 above).
There is a very eﬀective method to enlargeC just enough so that the bigger
category will have the desired limits. This is done by means of the categories
Ind(C) and Pro(C) of ind-objects and pro-objectsof C, respectively. See [KaSc1, Sec
1.11] and [KaSc2, Sec 6.1] for detailed discussions.
Here are two examples. ForC = Setﬁn, the category Ind(Setﬁn) is (canonically
equivalent to)Set. The categoryPro(Setﬁn) is the category of totally disconnected
compact Hausdorﬀ topological spaces, whose morphisms are the continuous func-
tions.
For C = Abﬁn, the categoryInd(Abﬁn) of ind-objects is the categoryAb of abelian
groups. The category Pro(Abﬁn) of pro-objects is the category of proﬁnite abelian
groups, whose morphisms are the continuous group homomorphisms.
31
Derived Categories | Amnon Yekutieli | 14 Apr 2019
