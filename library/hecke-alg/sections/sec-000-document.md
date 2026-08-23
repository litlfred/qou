---
doc_id: hecke-alg
doc_title: "Hecke algebras and Schur algebras of the symmetric group"
section_id: sec-000-document
section_title: "Document"
section_number: null
pages: 1-78
source_pdf: hecke_alg.pdf
source_sha256: 4ac08dfd165fb366
doc_brief: "Hecke algebras and Schur algebras of the symmetric group — 1 sections: Document"
---
Hec k e algebras and Sc h ur algebras of the
symmetric group
Andrew Mathas
Author address/:
School of Ma thema tics F/0/7/, University of Sydney/, Sydney NSW
/2/0/0/6/. A ustralia
E/-mail addr ess /: mathas/@maths/.usyd/.e du/.au
/1/9/9/1 Mathematics Subje ct Classi/c ation/. Primary /2/0C/3/0/, /1/6G/9/9/;
Secondary /2/0G/0/5/, /2/0C/2/0/.
The author gratefully ac kno wledges the supp ort of the
Sonderforsc h ungsb ereic h /3/4/3 at the Univ ersit/ at Bielefeld/.
Abstra ct/. These notes giv e a fully self/{con taine d in tro duction to the /(mo du/-
lar/) represen tati on theory of the Iw ahori/{Hec k e algebras and the q /{Sc h ur alge/-
bras of the symmetric groups/. The cen tral aim of this w ork is to giv e a concise/,
but complete/, and an elegan t/, y et quic k/, treatmen t of the classi/cation of the
simple mo dules and of the blo c ks of these t w o imp ortan t classes of algebras/.
Our approac h is com binatori al in nature and is based up on the construction
of /(cellular/) bases whic h are particularly w ell adapted to the represen tatio n
theory /.
Con ten ts
In tro duction iv
Chapter /1/. The Iw ahori/{Hec k e algebra of the Symmetric Group /1
/1/. The Symmetric group /1
/2/. The Iw ahori/{Hec k e algebra /3
/3/. The /0/{Hec k e algebra /6
Notes on Chapter /1 /7
Chapter /2/. Cellular algebras /9
/1/. Cellular bases /9
/2/. Simple mo dules in a cellular algebra /1/2
Notes on Chapter /2 /1/6
Chapter /3/. The Mo dular represen tation theory of H /1/7
/1/. The com binatorics of tableaux /1/7
/2/. The Murph y basis /2/0
/3/. Sp ec h t mo dules and Jucys/{Murph y elemen ts /2/6
/4/. The irreducible H /{mo dules /3/1
Notes on Chapter /3 /3/4
Chapter /4/. The q /{Sc h ur Algebra /3/6
/1/. Semistandard tableaux /3/6
/2/. A Sp ec h t series for M
/
/3/9
/3/. The semistandard basis theorem /4/0
Notes on Chapter /4 /4/4
Chapter /5/. The Jan tzen/{Sc hap er theorem /4/6
/1/. The Gram determinan t of W
/
/4/6
/2/. The Jan tzen sum form ula /5/7
/3/. The blo c ks of S /( d/; n /) and H /6/0
/4/. Irreducible Sp ec h t mo dules and W eyl mo dules /6/3
Notes on Chapter /5 /6/5
Notational Index /6/7
Bibliograph y /7/1
Index /7/3
iii
Ke ep it simple/; as simple as p ossible/, but no simpler/.
Alb ert Einstein
In tro duction
Iw ahori/{Hec k e algebras /rst app eared in the w ork of Iw ahori /[ /3/4 /] and no w
ha v e applications in sub jects ranging from the ordinary and mo dular represen tation
theory of Co xeter groups and the groups of Lie t yp e/, to knot theory /, quan tum
groups and statistical mec hanics /(see /[ /5/2 /] and the references there/)/. Sc h ur algebras
w ere in tro duced b y Sc h ur /[ /6/1 /] who used them to classify the ordinary irreducible
p olynomial represen tations of GL
n
/( C /)/; their /\quan tum analogues/,/" the q /{Sc h ur
algebras/, also determine the represen tation theory of the /nite general linear groups
in non/{de/ning c haracteristic /[ /1/5 /]/.
These notes aim to giv e a clear and concise treatmen t of the mo dular repre/-
sen tation theory of the Iw ahori/{Hec k e algebras of the symmetric groups and of the
q /{Sc h ur algebras/. Both of these theories w ere pioneered b y Dipp er and James in a
series of landmark pap ers /[ /1/3 /{ /1/6 /]/. T aking full adv an tage of recen t adv ances/, these
notes recast this theory with a primary goal of classifying and constructing the sim/-
ple mo dules and the blo c ks of these algebras/. Apart from some basic represen tation
theory /, these notes are en tirely self/{con tained/.
One of the cen tral themes of these notes is to view the Iw ahori/{Hec k e algebras
and q /{Sc h ur algebras as c el lular algebr as /, a class of algebras in tro duced b y Graham
and Lehrer /[ /2/6 /]/. This amoun ts to constructing a basis whic h is extremely w ell
adapted to the represen tation theory of the algebra/. F or example/, giv en a cellular
basis one can immedia tely construct all of the simple mo dules of the algebra/.
The cellular basis of the Iw ahori/{Hec k e algebra whic h w e concen trate up on
is the so/{called Murphy b asis /[ /5/5 /]/; this is a v ery natural basis indexed b y pairs
of standar d table aux /. Apart from b eing cellular/, the Murph y basis has another
marv elous prop ert y in that it is v ery easy to /\lift/" this basis to giv e a cellular basis
for the q /{Sc h ur algebra/, whic h is indexed b y pairs of semistandar d table aux /. In this
w a y /, one obtains a v ery clean and v ery elegan t construction of the simple mo dules
of b oth the Iw ahori/{Hec k e algebras and the q /{Sc h ur algebras/.
In order to classify the blo c ks of the our algebras w e pro v e an analogue of
Jantzen /'s sum formula for the Weyl mo dules of the q /{Sc h ur algebras/. Key to our
pro of of this result are generalizations of the Jucys/{Murphy elements from the
represen tation theory of the symmetric groups/. Using these elemen ts w e are able
to construct orthogonal bases for the W eyl mo dules /(when the q /{Sc h ur algebras are
semisimple/)/, whic h then allo w us to compute the Gram determinan t of the cellular
basis of the W eyl mo dules/. Essen tially some highest w eigh t theory then allo ws us
to deduce the sum form ula and so classify b oth the blo c ks of the q /{Sc h ur algebras
and Iw ahori/{Hec k e algebras/.
Brie/
y /, the structure of these notes is as follo ws/. Chapter /1 b egins b y pro ving
some basic facts ab out the symmetric group and its Iw ahori/{Hec k e algebra H /. In
fact/, this is really a c hapter Co xeter groups and general Iw ahori/{Hec k e algebras
INTR ODUCTION v
in disguise b ecause ev erything generalises to this more general con text/. Chapter /2
dev elops Graham and Lehrer/'s theory of cellular algebras/, culminating with the
construction of the simple mo dules in this setting/.
In Chapter /3 these notes b egin in earnest/. The com binatorics of tableaux are
in tro duced and Murph y/'s basis theorem is pro v ed in the /rst t w o sections/. Using
Chapter /2 this yields the simple H /{mo dules/. The third section uses the Jucys/{
Murph y elemen ts to construct the q /{analogue of Y oung/'s seminormal form for the
Sp ec h t mo dules of H in the semisimple case/. The fourth section classi/es the
simple H /{mo dules/.
Chapter /4 sho ws ho w the Murph y basis of H can b e /\lifted/" to giv e a cel/-
lular basis of the q /{Sc h ur algebra/. This in v olv es the in tro duction of semistandard
tableaux whic h corresp ond to orbits of the standard tableaux whic h index Murph y/'s
basis/. The simple mo dules for the q /{Sc h ur algebras are constructed and classi/ed
using the results of Chapter /2/. F or free/, w e obtain the fact that the q /{Sc h ur algebras
are quasi/{hereditary /.
Chapter /5 is dev oted to pro ving the Jan tzen/{Sc hap er theorem and classifying
the blo c ks of these algebras/. Here w e follo w the pap er of James and the author /[ /3/9 /]/,
using impro v emen ts from /[ /4/0 /]/. This is b y far the most tec hnical part of these notes/.
The k ey idea is to /rst construct an orthogonal basis of the W eyl mo dules of S /( d/; n /)
in a /\mo dular system/"/; it is here that generalizations of the Jucys/{Murph y elemen ts
pla y their most crucial role/.
The most ob vious omission from these notes is an y men tion of the b eautiful
result of Dipp er and James /[ /1/5 /] whic h sa ys that the represen tation theory of the
general linear groups in non/{de/ning c haracteristic is completely determined b y
the q /{Sc h ur algebras/. It w ould also ha v e b een go o d to include the Kleshc hev/{
Brundan branc hing rules /[ /4 /] and the w ork of Ariki /[ /2 /]/, Gro jno wski /[ /3/0 /] and Lascoux/,
Leclerc and Thib on /[ /5/1 /] connecting quan tum groups and decomp osition matrices
of Iw ahori/{Hec k e algebras o v er /eld of c haracteristic zero/. These matters w ould
ha v e more than doubled the size of these notes so instead w e refer the in terested
reader to the literature and/, in time/, to Brundan/'s forthcoming b o ok /[ /5 /]/.
These notes are based up on a series of lectures I ga v e at the Univ ersit/ at Biele/-
feld in /1/9/9/7 and it is a pleasure to thank the mem b ers of the Sonderforsc h ungsb ere/-
ic h /3/4/3/, and in particular Ste/en K/ onig and Claus Ringel/, for their encouragemen t
and supp ort/. A t times these notes dra w hea vily up on m y pap ers /[ /3/9 /, /4/0 /] with Gor/-
don James/, and our pap er /[ /1/7 /] with Ric hard Dipp er/, so in addition I w ould lik e to
thank m y coauthors for their con tributions to this do cumen t/.
Finally /, I thank Jon Brundan and Ste/en K/ onig for n umerous suggestions and
commen ts on an earlier v ersion of this man uscript/.
CHAPTER /1
The Iw ahori/{Hec k e algebra of the
Symmetric Group
In this c hapter w e b egin b y pro ving some fundamen tal results ab out the sym/-
metric group and then de/ne the asso ciated Iw ahori/{Hec k e algebra/. Ev erything
in this c hapter/, including the pro ofs/, generalises to the case of arbitrary Co xeter
groups and Iw ahori/{Hec k e algebras/.
/1/. The Symmetric group
Throughout these notes w e /x an in teger n / /1/.
/1/./1 Let S
n
b e the symmetric group acting on /1 /; /2 /; /: /: /: /; n from the right /. F or
i /= /1 /; /2 /; /: /: /: /; n /? /1 let s
i
b e the basic transp osition /( i/; i /+ /1/) and let S /. As a Co xeter
group/, S
n
is generated b y s
/1
/; s
/2
/; /: /: /: /; s
n /? /1
/, sub ject to the relations
s
/2
i
/= /1 /; for i /= /1 /; /2 /; /: /: /: /; n /? /1 /;
s
i
s
j
/= s
j
s
i
/; for /1 / i /< j /? /1 / n /? /2 /;
s
i
s
i /+/1
s
i
/= s
i /+/1
s
i
s
i /+/1
/; for i /= /1 /; /2 /; /: /: /: /; n /? /2 /:
The reader is in vited to pro v e that this do es indeed giv e a presen tation of S
n
/. /(Hin t/:
f /1 /; s
n /? /1
/; s
n /? /2
s
n /? /1
/; /: /: /: /; s
/1
s
/2
/: /: /: s
n /? /1
g is a complete set of righ t coset represen tativ es
of S
n /? /1
in S
n
/./) The second and third relations are the b raid relations of S
n
/.
Supp ose that w is an elemen t of S
n
and write w /= s
i
/1
/: /: /: s
i
k
for some i
/1
/; /: /: /: /; i
k
in f /1 /; /2 /; /: /: /: /; n /? /1 g /. If k is minim al then w e de/ne the length /, /` /( w /)/, of w to b e k
and w e will call b oth s
i
/1
/: /: /: s
i
k
and /( i
/1
/; /: /: /: /; i
k
/) a reduced exp ression for w /.
The sign rep resentation of S
n
is the one dimensional represen tation /" determined
b y /" /( s /) /= /? /1 for all s /2 S /. Th us/, /" /( w /) /= /( /? /1/)
/` /( w /)
for all w /2 S
n
/. Consequen tly /, if
w /2 S
n
and s /2 S then /` /( sw /) /= /` /( w /) / /1/.
W e w ould lik e to kno w when /` /( sw /) /= /` /( w /) /+ /1 and for this w e need another
description of the length function/. F or w /2 S
n
let
N /( w /) /= f /( j/; k /) /2 S
n
j /1 / j /< k / n and j w /> k w g /:
So/, for example/, N /(/1/) /= /? and N /( s /) /= f s g for all s /2 S /.
Giv en sets A and B let A
/_
/+ B /= /( A /[ B /) n /( A /\ B /) b e their symmetric di/erence/.
/1/./2 Lemma /(Dy er/) Supp ose that v /; w /2 S
n
/. Then N /( v w /) /= N /( v /)
/_
/+ v N /( w /) v
/? /1
/.
Pro of/. If s /2 S and /( j/; k /) /2 S
n
then s /( j/; k /) s /= /( j s/; k s /) so N /( sw /) /= N /( s /)
/_
/+ sN /( w /) s
for an y w /2 S
n
/; so the Lemma holds when /` /( v /) /= /1/. If /` /( v /) /> /1 then v /= su for
some s /2 S and u /2 S
n
and with /` /( u /) /= /` /( v /) /? /1/. Therefore/, b y induction on the
length of v /,
N /( v w /) /= N /( suw /) /= N /( s /)
/_
/+ sN /( uw /) s /= N /( s /)
/_
/+ sN /( u /) s
/_
/+ suN /( w /) u
/? /1
s
/= N /( v /)
/_
/+ v N /( w /) v
/? /1
/1
/2 /1/. THE IW AHORI/{HECKE ALGEBRA OF THE SYMMETRIC GR OUP
as required/.
F or con v enience let T /= f /( i/; j /) /2 S
n
g /=
S
w /2 S
n
w S w
/? /1
/. Then T is the set of
re/
ections in S
n
/(considering S
n
as a Co xeter group/)/, and N /( w /) / T /.
/1/./3 Prop ositio n Supp ose that w /2 S
n
/. Then
/(i/) /` /( w /) /= j N /( w /) j /; and/,
/(ii/) N /( w /) /= f t /2 T j /` /( tw /) /< /` /( w /) g /.
Pro of/. Supp ose that s
i
/1
/: /: /: s
i
k
is a reduced expression for w and/, for a /= /1 /; /: /: /: /; k /,
let t
a
/= s
i
/1
/: /: /: s
i
a /? /1
s
i
a
s
i
a /? /1
/: /: /: s
i
/1
/. Then t
a
/2 T for all a and/, b y Lemma /1/./2/,
N /( w /) /= N /( s
i
/1
/: /: /: s
i
k
/) /= f t
/1
g
/_
/+ / / /
/_
/+ f t
k
g /. W e claim that t
a
/6/= t
b
for a /6/= b /. By w a y
of con tradiction/, supp ose that t
a
/= t
b
for some a /< b /. Then
w /= t
a
t
b
w /= s
i
/1
/: /: /: s
i
a /? /1
s
i
a
s
i
a /? /1
/: /: /: s
i
/1
s
i
/1
/: /: /: s
i
b /? /1
s
i
b
s
i
b /? /1
/: /: /: s
i
/1
w
/= s
i
/1
/: /: /: bs
i
a
/: /: /: bs
i
b
/: /: /: s
i
k
/;
where bs
j
indicates that the transp osition s
j
is omitted/. Ho w ev er/, this con tradicts
the assumption that w has length k so t
/1
/; /: /: /: /; t
k
m ust all b e distinct/. Hence/,
N /( w /) /= f t
/1
/; /: /: /: /; t
k
g and /` /( w /) /= j N /( w /) j pro ving /(i/)/.
No w t
a
w /= s
i
/1
/: /: /: bs
i
a
/: /: /: s
i
k
for a /= /1 /; /: /: /: /; k so N /( w /) / f t /2 T j /` /( tw /) /< /` /( w /) g /.
Con v ersely /, b y what w e ha v e already sho wn/, if t /2 T then t /2 N /( t /)/. F urthermore/,
N /( tw /) /= N /( t /)
/_
/+ tN /( w /) t b y Lemma /1/./2/; so if t /=/2 N /( w /) then t /2 N /( tw /) and /` /( w /) /=
/` /( ttw /) /< /` /( tw /) b y /(i/)/. This pro v es /(ii/)/.
As a sp ecial case of the Prop osition w e ha v e the follo wing/.
/1/./4 Corollary Supp ose that w /2 S
n
and that s
i
/2 S /. Then
/` /( s
i
w /) /=
/(
/` /( w /) /+ /1 /; if iw /< /( i /+ /1/) w /;
/` /( w /) /? /1 /; if iw /> /( i /? /1/) w /:
/1/./5 Theorem /(The Strong Exc hange Condition/) Supp ose that s
i
/1
/; /: /: /: /; s
i
k
ar e
elements of S /, t /2 T and that /` /( ts
i
/1
/: /: /: s
i
k
/) /< /` /( s
i
/1
/: /: /: s
i
k
/) /. Then
ts
i
/1
/: /: /: s
i
k
/= s
i
/1
/: /: /: bs
i
a
/: /: /: s
i
k
for some a /. F urthermor e/, t /= s
i
/1
/: /: /: s
i
a /? /1
s
i
a
s
i
a /? /1
/: /: /: s
i
/1
/.
Pro of/. Let w /= s
i
/1
/: /: /: s
i
k
and/, for /1 / a / k /, de/ne t
a
as in the pro of of the
Prop osition /1/./3/. Then N /( w /) /= f t
/1
g
/_
/+ / / /
/_
/+ f t
k
g b y Lemma /1/./2 and t /2 N /( w /) b y
Prop osition /1/./3/(ii/)/. Therefore/, t /= t
a
for some a and the result follo ws/.
Note that in the statemen t of the strong exc hange condition w e do not require
that s
i
/1
/: /: /: s
i
k
b e reduced/. The exc hange condition also has an equiv alen t righ t
hand analogue/.
/1/./6 Corollary Supp ose that w /2 S
n
and s /2 S /. Then
/(i/) /` /( sw /) /< /` /( w /) if and only if w has a r e duc e d expr ession b e ginning with s /;
/(ii/) /` /( w s /) /< /` /( w /) if and only if w has a r e duc e d expr ession ending with s /.
Pro of/. Because /` /( sw /) /= /` /( w
/? /1
s /)/, parts /(i/) and /(ii/) are equiv alen t and it su/ces
to consider /(i/)/. Supp ose then that /` /( sw /) /< /` /( w /) and let s
i
/1
/: /: /: s
i
k
b e a reduced
expression for w /. By the exc hange condition there exists an in teger a suc h that
/2/. THE IW AHORI/{HECKE ALGEBRA /3
sw /= s
i
/1
/: /: /: bs
i
a
/: /: /: s
i
k
/. Therefore/, w /= ss
i
/1
/: /: /: bs
i
a
/: /: /: s
i
k
and this expression is
reduced/. The con v erse is clear/.
/1/./7 Corollary /(The Deletion Condition/) Supp ose that w /2 S
n
/, /` /( w /) /< k and
that w /= s
i
/1
/: /: /: s
i
k
for some s
i
j
/2 S /.
/(i/) Ther e exist inte gers /1 / a /< b / k such that w /= s
i
/1
/: /: /: bs
i
a
/: /: /: bs
i
b
/: /: /: s
i
k
/:
/(ii/) A r e duc e d expr ession for w c an b e obtaine d by deleting an even numb er of the
s
i
a
fr om s
i
/1
/: /: /: s
i
k
/.
Pro of/. Since /` /( w /) /< k there exists an in teger a with /1 / a /< k suc h that
/` /( s
i
a
/: /: /: s
i
k
/) /< /` /( s
i
a /+/1
/: /: /: s
i
k
/)/. Hence/, b y the exc hange condition s
i
a
/: /: /: s
i
k
/=
s
i
a /+/1
/: /: /: bs
i
b
/: /: /: s
i
k
for some b with a /< b / k /. Th us/, w /= s
i
/1
/: /: /: bs
i
a
/: /: /: bs
i
b
/: /: /: s
i
k
pro ving /(i/)/. P art /(ii/) is no w immediate/.
W e can no w pro v e the main result w e need from this section/. Giv en t w o reduced
expressions /( i
/1
/; /: /: /: /; i
k
/) and /( j
/1
/; /: /: /: /; j
k
/) write /( i
/1
/; /: /: /: /; i
k
/) /
b
/( j
/1
/; /: /: /: /; j
k
/) if one ex/-
pression can b e transformed in to the other using only the braid relations/. Th us/, /
b
is the equiv alence relation on k /{tuples generated b y /( /: /: /: /; i/; j/; /: /: /: /) /
b
/( /: /: /: /; j/; i/; /: /: /: /)/,
when j i /? j j /> /1/, and /( /: /: /: /; i/; i /+ /1 /; i/; /: /: /: /) /
b
/( /: /: /: /; i /+ /1 /; i/; i /+ /1 /; /: /: /: /)/.
/1/./8 Theorem /(Matsumoto/) Supp ose w /2 S
n
and let /( i
/1
/; /: /: /: /; i
k
/) and /( j
/1
/; /: /: /: /; j
k
/)
b e two r e duc e d expr essions for w /. Then /( i
/1
/; /: /: /: /; i
k
/) /
b
/( j
/1
/; /: /: /: /; j
k
/) /.
Pro of/. W e argue b y induction on k /= /` /( w /)/. If k / /1 there is nothing to pro v e
so supp ose that k /> /1/. By assumption s
i
/1
/: /: /: s
i
k
/= w /= s
j
/1
/: /: /: s
j
k
and these ex/-
pressions are b oth reduced/. Consequen tly /, s
i
/1
s
j
/1
/: /: /: s
j
k
is not a reduced expression
and s
i
/1
s
j
/1
/: /: /: s
j
k
/= s
j
/1
/: /: /: bs
j
a
/: /: /: s
j
k
for some in teger a b y the exc hange condition/.
Therefore/, /(i/) s
i
/2
/: /: /: s
i
k
/= s
j
/1
/: /: /: bs
j
a
/: /: /: s
j
k
and /(ii/) s
i
/1
s
j
/1
/: /: /: s
j
a /? /1
/= s
j
/1
/: /: /: s
j
a
and
all four of these expressions are all reduced/.
If a /6/= k then all of the reduced expressions in /(i/) and /(ii/) ha v e length strictly
less than k /. Therefore/, using induction and /(i/) and /(ii/) in turn/,
/( i
/1
/; i
/2
/; /: /: /: /; i
k
/) /
b
/( i
/1
/; j
/1
/; /: /: /: /; j
a /? /1
/; j
a /+/1
/; /: /: /: /; j
k
/) /
b
/( j
/1
/; /: /: /: /; j
a
/; j
a /+/1
/; /: /: /: /; j
k
/)
as required/.
If a /= k only expressions in /(i/) ha v e length less than k /, so w e deduce that
/( i
/2
/; /: /: /: /; i
k
/) /
b
/( j
/1
/; /: /: /: /; j
k /? /1
/)/; b y symmetry w e ma y also assume that /( j
/2
/; /: /: /: /; j
k
/) /
b
/( i
/1
/; /: /: /: /; i
k /? /1
/)/. Hence/, /( i
/1
/; i
/2
/; /: /: /: /; i
k
/) /
b
/( i
/1
/; j
/1
/; /: /: /: /; j
k /? /1
/) and /( j
/1
/; j
/2
/; /: /: /: /; j
k
/) /
b
/( j
/1
/; i
/1
/; /: /: /: /; i
k /? /1
/)/; so it su/ces to sho w that /( i
/1
/; j
/1
/; /: /: /: /; j
k /? /1
/) /
b
/( j
/1
/; i
/1
/; /: /: /: /; i
k /? /1
/)/.
If j i
/1
/? j
/1
j /> /1 then /( i
/1
/; j
/1
/) /
b
/( j
/1
/; i
/1
/) is a braid relation of length /2 so w e need
only sho w that /( i
/2
/; /: /: /: /; i
k /? /1
/) /
b
/( j
/2
/; /: /: /: /; j
k /? /1
/) whic h follo ws b y induction/. If
j i
/1
/? j
/1
j /= /1 then b y reapplying the argumen t of the /rst paragraph w e are re/-
duced to sho wing that /( i
/1
/; j
/1
/; i
/1
/; i
/2
/; /: /: /: /; i
k /? /2
/) /
b
/( j
/1
/; i
/1
/; j
/1
/; j
/2
/; /: /: /: /; j
k /? /2
/)/. Ho w ev er/,
/( i
/1
/; j
/1
/; i
/1
/) /
b
/( j
/1
/; i
/1
/; j
/1
/) is a braid relation of length /3/, so it is su/cien t to sho w that
/( i
/2
/; /: /: /: /; i
k /? /2
/) /
b
/( j
/2
/; /: /: /: /; j
k /? /2
/) whic h again follo ws b y induction/.
/2/. The Iw ahori/{Hec k e algebra
/1/./9 Let R b e a comm utativ e in tegral domain with /1 and let q b e an arbitrary
elemen t of R /. The Iw aho ri/{Heck e algeb ra H /= H
R/;q
/( S
n
/) of S
n
is the unital
/4 /1/. THE IW AHORI/{HECKE ALGEBRA OF THE SYMMETRIC GR OUP
asso ciativ e R /{algebra with generators T
/1
/; T
/2
/; /: /: /: /; T
n /? /1
whic h are sub ject to the
relations
/( T
i
/? q /)/( T
i
/+ /1/) /= /0 /; for i /= /1 /; /2 /; /: /: /: /; n /? /1 /;
T
i
T
j
/= T
j
T
i
/; for /1 / i /< j /? /1 / n /? /2 /;
T
i
T
i /+/1
T
i
/= T
i /+/1
T
i
T
i /+/1
/; for i /= /1 /; /2 /; /: /: /: /; n /? /2 /:
Notice that when q /= /1 the /rst relation reduces to T
/2
i
/= /1/; th us/, b y /(/1/./1/)/, H
is isomorphic to the group ring R S
n
of the symmetric group in this case/. When
q /6/= /1 this ma y seem a strange algebra to consider but/, in fact/, H arises naturally
in the represen tation theory of the general linear groups /(see Note /4 on page /7/)/.
Our /rst aim is to pro duce a basis of H /. Supp ose that w /2 S
n
and let
/( i
/1
/; /: /: /: /; i
k
/) b e a reduced expression for w /. W e de/ne
/1 /: /1/0 T
w
/= T
i
/1
/: /: /: T
i
k
/:
By Theorem /1/./8/, T
w
is indep enden t of the c hoice of reduced expression for w /. If w
is the iden tit y elemen t of S
n
w e iden tify T
w
with /1/, the iden tit y elemen t of R /.
/1/./1/1 Theorem The Iwahori/{He cke algebr a H /= H
R/;q
/( S
n
/) is fr e e as an R /{
mo dule with b asis f T
w
j w /2 S
n
g /. Mor e over/, the multiplic ation in H is determine d
by the formulae
T
w
T
s
/=
/(
T
w s
/; if /` /( w s /) /> /` /( w /) /;
q T
w s
/+ /( q /? /1/) T
w
/; otherwise /:
for al l w /2 S
n
and s /2 S /.
Pro of/. By Corollary /1/./6/(ii/)/, if w /2 S
n
and s /2 S then /` /( w s /) /< /` /( w /) if and only
if w has a reduced expression ending in s /; so the m ultiplicati on form ulae follo w
from the de/nition of T
w
and the relation T
/2
s
/= /( q /? /1/) T
s
/+ q /.
By the relations in H the set f T
w
j w /2 S
n
g certainly spans H /. Th us/, it
remains to sho w that f T
w
j w /2 S
n
g is linearly indep enden t/.
Let /^q b e an indeterminate o v er Z /. Then R b ecomes a Z /[ /^ q /]/{mo dule via the
homomo rphism /' /: Z /[ /^ q /] /? /! R determined b y /' /(/1/) /= /1 and /' /( /^ q /) /= q /. The generators
T
i
/
 /1 of the R /{algebra H
/0
/= H
Z /[ /^ q /] /; /^q
/( S
n
/) /
Z /[ /^ q /]
R satisfy the relations in H so
there is a surjection / /: H / H
/0
/. Therefore/, it is enough to sho w that H
Z /[ /^ q /] /; /^q
/( S
n
/)
is free as a Z /[ /^ q /]/{mo dule with basis f T
w
j w /2 S
n
g b ecause then H
/0
is R /{free with
basis f T
w
/
 /1 j w /2 S
n
g and/, consequen tly /, / m ust b e an isomorphism/.
Supp ose then that H /= H
Z /[ /^ q /] /; /^q
/( S
n
/)/. If f T
w
j w /2 S
n
g w ere not linearly
indep enden t then there w ould exist p olynomials a
w
/( /^ q /) /2 Z /[ /^ q /]/, not all zero/, suc h
that
P
w
a
w
/( /^ q /) T
w
/= /0 in H /. Without loss of generalit y /, the greatest common
divisor of the p olynomial s f a
w
/( /^ q /) j w /2 S
n
g is /1/. Consider Z as a Z /[ /^ q /]/{mo dule b y
letting /^q act as /1/. Then H /
Z /[ /^ q /]
Z
/
/=
Z S
n
and f T
w
/
 /1 j w /2 S
n
g maps to the
natural basis f w j w /2 S
n
g of Z S
n
under this isomorphism/. Hence/, w e obtain the
relation
P
w
a
w
/(/1/) w /= /0 in Z S
n
/; this forces a
w
/(/1/) /= /0 for all w /2 S
n
/. Therefore/,
for all w /2 S
n
the p olynomial a
w
/( /^ q /) b elongs to /( /^ q /? /1/) Z /[ /^ q /]/, con tradicting our
assumption that the a
w
/( /^ q /) ha v e greatest common divisor /1/. Hence/, f T
w
j w /2 S
n
g
is a basis of H
Z /[ /^ q /] /; /^q
/( S
n
/) and the Theorem follo ws/.
No w that w e ha v e established that H is free o v er R /, the argumen t from the
second paragraph of the pro of generalizes to yield the follo wing result/. /(In the
/2/. THE IW AHORI/{HECKE ALGEBRA /5
tensor pro duct of the Corollary w e consider R as an
/^
R /{mo dule with /^ r /2
/^
R acting
on R as /' /( /^ r /)/./)
/1/./1/2 Corollary Supp ose that /' /:
/^
R /? /! R is a ring homomorphism with /' /( /^ q /) /= q
for some /^q /2
/^
R /. Then H
R/;q
/( S
n
/) and H
/^
R
/; /^q
/( S
n
/) /
/^
R
R ar e c anonic al ly isomorphic
algebr as/.
In the situation of Corollary /1/./1/2/, w e sa y that H
R/;q
/( S
n
/) is a sp ecialization of
H
/^
R/; /^q
/( S
n
/)/; the tensor pro duct map H
/^
R/; /^q
/( S
n
/) /? /! H
/^
R /; /^q
/( S
n
/) is called a sp ecializa/-
tion homomo rphism /.
Let Z /= Z /[ /^ q /; /^q
/? /1
/]/, where /^q is an indeterminate o v er Z /. Then H
R/;q
/( S
n
/) is a
sp ecialization of H
Z
/= H
Z /; /^q
/( S
n
/) whenev er q is a non/{zero elemen t of R /. As w e
are most in terested in the case where q /6/= /0/, w e call H
Z
the generic Iw aho ri/{Heck e
algeb ra of S
n
/.
/1/./1/3 Corollary The Iwahori/{He cke algebr a has two one dimensional r epr esenta/-
tions /1
H
and /"
H
which ar e the R /{line ar maps determine d by
/1
H
/( T
w
/) /= q
/` /( w /)
and /"
H
/( T
w
/) /= /( /? /1/)
/` /( w /)
for al l w /2 S
n
/.
Pro of/. It is su/cien t to c hec k that these maps preserv e the relations in H and
this is clear/.
The represen tation /1
H
is the Iw ahori/{Hec k e algebras analogue of the trivial
represen tation of S
n
and that /"
H
is its analogue of the sign represen tation/.
De/ne an R /{bilinear map /( /; /) /: H / H /? /! R b y setting /( h
/1
/; h
/2
/) equal to the
co e/cien t of /1 in h
/1
h
/2
for all h
/1
/; h
/2
/2 H /. In particular/, this form is asso ciativ e/;
that is/, /( h
/1
h
/2
/; h
/3
/) /= /( h
/1
/; h
/2
h
/3
/) for all h
/1
/; h
/2
/; h
/3
/2 H /.
/1/./1/4 Prop ositi on Supp ose that x and y ar e elements of S
n
/. Then
/( T
x
/; T
y
/) /=
/(
q
/` /( x /)
/; if x /= y
/? /1
/;
/0 /; otherwise /:
In p articular/, if q is invertible then /( /; /) is a non/{de gener ate asso ciative symmetric
biline ar form/.
Pro of/. Let x/; y /2 S
n
/. The Prop osition will follo w if w e sho w that there exists an
in teger m and a
z
/2 R /, for z /2 S
n
/, suc h that a
z
/= /0 unless /` /( z /) / /` /( xy /) and
T
x
T
y
/= q
m
T
xy
/+
X
z /2 S
n
a
z
T
z
/:
T o pro v e this w e argue b y induction on the length of x /. When /` /( x /) /= /0 then
x /= /1 and there is nothing to pro v e/. If /` /( x /) /> /0 then there exists s /2 S suc h that
/` /( xs /) /< /` /( x /)/. Then T
x
T
y
/= T
xs
/( T
s
T
y
/) and the claim follo ws easily b y induction
using Theorem /1/./1/1/.
Giv en an y represen tation of H /, its cha racter is de/ned in the usual w a y b y
taking traces/. By Theorem /1/./1/1 the c haracters of H are R /{linear maps whic h are
determined b y their v alues on the basis elemen ts T
w
/, for w /2 S
n
/. Unlik e in the
case of /nite groups/, if / is a c haracter and x and y are conjugate elemen ts of
S
n
it is not necessarily true that / /( T
x
/) /= / /( T
y
/)/; for example/, consider the trivial
/6 /1/. THE IW AHORI/{HECKE ALGEBRA OF THE SYMMETRIC GR OUP
represen tation /1
H
of H /. Nonetheless/, there is an analogue of the orthogonalit y
relations when H is semisimple/.
Let W
n
/( /^ q /) /=
P
w /2 S
n
/^q
/` /( w /)
b e the P oincar / e p olynomial of S
n
/; this p olynomial
arises naturally in the in v arian t theory of the symmetric group /(see/, for example/,
/[ /3/3 /, x /3/./1/5/]/)/. Because f /1 /; s
n /? /1
/; s
n /? /1
s
n /? /2
/; /: /: /: /; s
n /? /1
/: /: /: s
/1
g is a set of righ t coset
represen tativ es for S
n /? /1
in S
n
/, it follo ws that
W
n
/( /^ q /) /= /(/1 /+ /^ q /)/(/1 /+ /^ q /+ /^ q
/2
/) /: /: /: /(/1 /+ /^ q /+ / / / /+ /^ q
n /? /1
/)/;
th us/, W
n
/( /^ q /) /= /[ /^ q /]
/!
n
in the notation of /(/3/./2/8/)/. Finally /, note that if /^q /= /1 then
W
n
/(/1/) /= n /! /= j S
n
j /.
/1/./1/5 Corollary Supp ose that K /= C /( /^ q /) and let H
K
/= H
K /; /^q
/( S
n
/) /. Then H
K
is
semisimple/. Mor e over/, if / and / ar e irr e ducible char acters of H
K
then
/1
W
n
/( /^ q /)
X
w /2 S
n
/^q
/? /` /( w /)
/ /( T
w
/) / /( T
w
/? /1 /) /= /
// 
D
/
/( /^ q /) /;
for some r ational function D
/
/( /^ q /) in K /.
Pro of/. By Prop osition /1/./1/4/, H
K
is a symmetric algebra with dual bases f T
w
g and
f /^q
/? /` /( w /)
T
w
/? /1 g /, so the orthogonalit y relation will follo w from the theory of symmetric
algebras /(see /[ /1/1 /, x /9A/]/) once w e sho w that H
K
is semisimple/.
Supp ose that H
K
is not semisimple/. Then w e can /nd a non/{zero elemen t h
in the radical of H
K
/. Without loss of generalit y w e ma y assume that h /2 H
Z
and
h /=/2 /( /^ q /? /1/) H
Z
/. Let /' /: H
Z
/? /! C S
n
b e the sp ecialization homomorphism sending
/^q to /1 /2 C /. Then for an y a
xy
/2 C w e ha v e
X
x/;y /2 S
n
a
xy
x/' /( h /) y /= /'
/?
X
x/;y /2 S
n
a
xy
T
x
hT
y
/
/:
No w h is nilp oten t so /' /( h /) is also nilp oten t/; ho w ev er/, C S
n
is semisimple so w e
m ust ha v e /' /( h /) /= /0/. Therefore/, h /2 k er /' /= /( /^ q /? /1/) H
Z
whic h con tradicts our
assumptions on h /.
W e shall see in Corollary /3/./2/2 b elo w that the Hec k e algebra H
K
is split semisim/-
ple and that/, as an algebra/, it is isomorphic to K S
n
/.
The rational functions D
/
/( /^ q /) of Corollary /1/./1/5 are the so/{called generic de gr e es
of S
n
/; they are all explicitly kno wn /(see /[ /6 /, p/. /4/4/6/]/) and turn out to b e p olyno/-
mials in Z /[ q /]/. Therefore/, giv en the remark of the last paragraph/, the equation
de/ning D
/
/( /^ q /) in Corollary /1/./1/5 can b e ev aluated at /^ q /= /1 where it b ecomes one of
the orthogonalit y relations for the ordinary irreducible c haracters if the symmetric
group/. It follo ws that D
/
/(/1/) is the dimension of an irreducible complex represen ta/-
tion of S
n
/. What is more/, when q is a prime p o w er the D
/
/( q /) giv e the dimensions
of the principal series represen tations of GL
n
/( q /)/; see /[ /6 /] and Note /4 b elo w/.
/3/. The /0 /{Hec k e algebra
After this section w e will assume that q is in v ertible/. F or completeness w e no w
describ e the simple H /{mo dules when q /= /0/.
/1/./1/6 Theorem /(Norton/) Supp ose that R is a /eld and that q /= /0 /. Then every
irr e ducible H /{mo dule is one dimensional/.
NOTES ON CHAPTER /1 /7
Pro of/. Fix a total ordering w
/1
/> w
/2
/> / / / /> w
n /!
/= /1 on S
n
suc h that w
a
/> w
b
whenev er /` /( w
a
/) /> /` /( w
b
/)/. De/ne H
a
to the R /{mo dule with basis f T
w
b
j b / a g and
let H
/0
/= /0/. Then /0 /= H
/0
/ H
/1
/ H
/2
/ / / / / H
n /!
/= H /.
No w/, if w /2 S
n
and s /2 S then b ecause q /= /0
T
w
T
s
/=
/(
T
w s
/; if /` /( w s /) /> /` /( w /) /;
/? T
w
/; if /` /( w s /) /< /` /( w /) /;
b y Theorem /1/./1/1/. Consequen tly /, for eac h a / /1 the R /{mo dule H
a
is a righ t
H /{mo dule /(in fact it is an ideal/)/. Therefore/, H
a
/= H
a /+/1
is a one dimensional H /{
mo dule/; in particular/, H
a
/= H
a /+/1
is simple/. Since these mo dules giv e a /ltration of
H /, ev ery irreducible H /{mo dule is of the form H
a
/= H
a /+/1
for some a with /1 / a /
n /! /. The Theorem follo ws/.
Norton /[ /5/7 /] explicitly constructs the principal indecomp osable mo dules of H
when q /= /0/. She sho ws that/, up to isomorphism/, the irreducible represen tations
of H are lab elled b y the subsets of S /. If I / S the corresp onding irreducible
represen tation /'
I
/: H /? /! R is the unique homomorphism suc h that
/'
I
/( T
i
/) /=
/(
/1 /; if i /2 I /;
/0 /; otherwise /;
for i /= /1 /; /2 /; /: /: /: /; n /? /1/. F urthermore/, the decomp osition matrices and Cartan ma/-
trices of the /0/{Hec k e algebra of S
n
are all explicitly kno wn /[ /7 /] /(in t yp e A only/)/.
Notes on Chapter /1
/1/. The elegan t pro of of the exc hange condition giv en in Section /1 is due to Matthew
Dy er /[ /2/2 /, /2/3 /]/. Dy er calls the function N a r e/
e ction c o cycle and he sho ws that
a group W generated a set S of in v olutions is a Co xeter group if and only if
W p ossesses a map N suc h that /(i/) N /( s /) /= f s g for all s /2 S and /(ii/) for all
elemen ts v and w in W /, N /( v w /) /= N /( v /)
/_
/+ v N /( w /) v
/? /1
/; cf/. Lemma /1/./2/.
/2/. Theorem /1/./8 is a sp ecial case of Matsumoto/'s monid lemma /[ /1/1 /, /6/4/./2/0/]/, whic h is
really a result ab out the corresp onding braid group/. It is the k ey result of the
/rst section b ecause it sho ws that the T /{basis is w ell/{de/ned/.
/3/. Theorem /1/./1/1 is often tak en as the de/nition of H /. In this case/, it is necessary to
pro v e that an algebra exists satisfying Theorem /1/./1/1/; this is done b y w orking in
the endomorphism ring of the R /{mo dule H /; see/, for example/, /[ /3/3 /, Chapter /7/]/.
/4/. Let G /= GL
n
/( q /)/, where q is a prime p o w er/, and let B b e the subgroup of upp er
triangular matrices in G /(a Bor el sub gr oup /)/. Let e
B
/=
/1
j B j
P
b /2 B
b /; then e
B
is
idemp oten t and Iw ahori /[ /3/4 /] sho w ed that H
C /;q
/
/=
e
B
C Ge
B
/. This is one of the
main reasons wh y these algebras are in teresting and imp ortan t/. /(Note that S
n
is
the W eyl group of GL
n
/( q /)/./) The principal series represen tations of G are just the
irreducible constituen ts of C Ge
B
/; this b egins to explain wh y the dimensions of
the principal series represen tations are giv en b y sp ecializing the generic degrees/.
Pro ofs and more complete details can b e found in /[ /1/1 /, x /6/7/-/6/8/]/.
/5/. The pro of that H
K
is semisimple in Corollary /1/./1/5 is due to Gy o ja and Uno /[ /3/1 /]/.
/6/. In the literature/, a He cke algebr a is an y algebra of the form eAe
/
/=
End
A
/( eA /)
where A is an algebra and e is an idemp oten t in A /. Suc h algebras w ere /rst
studied b y Hec k e/; this is wh y Iw ahori called H a Hec k e algebra/.
/8 /1/. THE IW AHORI/{HECKE ALGEBRA OF THE SYMMETRIC GR OUP
/7/. Ev en though the c haracters of H
K
are not class functions/, there is a w ell b e/-
ha v ed notion of char acter table whic h is de/ned b y the v alues of the irreducible
c haracters on minimal length conjugacy class represen tativ es/. These c haracters
w ere /rst calculated b y Ram /[ /5/9 /]/; see also /[ /2/4 /]/.
CHAPTER /2
Cellular algebras
Cellular algebras w ere in tro duced b y Graham and Lehrer in /[ /2/5 /, /2/6 /]/. Although
it is p ossible to giv e a basis/{free approac h to the theory of cellular algebras /[ /5/0 /]/,
our p ersp ectiv e is that a cellular algebra is an algebra whic h has a basis whic h is
particularly w ell/{adapted to its represen tation theory /.
This Chapter describ es the simple mo dules and blo c ks of a cellular algebra/;
in Chapters /3 and /4 this theory is applied to the Iw ahori/{Hec k e algebras of the
symmetric groups and the q /{Sc h ur algebras/.
/1/. Cellular bases
Let R b e a comm utativ e in tegral domain with /1 and A an asso ciativ e unital
R /{algebra/.
/2/./1 Supp ose that /(/ /; / /) is a /(/nite/) p oset and that for eac h / /2 / w e ha v e a /nite
set T /( / /) and elemen ts c
/
st
/2 A for all s /; t /2 T /( / /) suc h that
C /= f c
/
st
j / /2 / and s/; t /2 T /( / /) g
is a basis of A /. F or eac h / /2 / let
/
A
/
b e the R /{submo dule of A with basis
f c
/
uv
j / /2 / /; / /> / and u /; v /2 T /( / /) g /. The pair /( C /; //) is a cellula r basis of A if
/(i/) the R /{linear map / /: A /? /! A determined b y c
/
st
/
/= c
/
ts
/, for all / /2 / and all s
and t in T /( / /)/, is an algebra an ti/{isomorphism of A /; and/,
/(ii/) for an y / /2 //, t /2 T /( / /) and a /2 A there exist r
v
/2 R suc h that for all s /2 T /( / /)
c
/
st
a /
X
v /2T /( / /)
r
v
c
/
sv
mo d
/
A
/
/:
If A has a cellular basis w e sa y that A is a cellula r algeb ra /.
It should b e emphasized that a cellular algebra ma y ha v e more than one cellular
basis /(up to an automorphism of A /)/.
/2/./2 Examples /(i/) First an easy example whic h illustrates some of the prop erties
of cellular algebras/. Let A /= R /[ x /]/, where x is in indeterminate o v er R /, and tak e
/ to b e the non/{negativ e in tegers with their natural ordering/. F or eac h n /2 / let
T /( n /) /= f/g and set c
n
//
/= x
n
/. It is easy to c hec k that f x
n
j n / /0 g is a cellular basis
of A /. Here
/
A
n
is the set of p olynomials of degree greater than n and
/
A
n
/=
/
A
n /+/1
/
/=
R
is simple for all n /.
/(ii/) Let H /= H
R/;q
/( S
/3
/) and let / /= f /(/3/) /; /(/2 /; /1/) /; /(/1
/3
/) g /, the set of partitions of /3
ordered lexicographically /. Let s /=
/1 /2 /3
/, t /=
/1 /2
/3
/, u /=
/1 /3
/2
and v /=
/1
/2
/3
and set
/9
/1/0 /2/. CELLULAR ALGEBRAS
T /(/3/) /= f s g /, T /(/2 /; /1/) /= f t /; u g and T /(/1
/3
/) /= f v g /. Then
c
/(/3/)
ss
/= /1 /+ T
/1
/+ T
/2
/+ T
/1
T
/2
/+ T
/2
T
/1
/+ T
/1
T
/2
T
/1
c
/(/2 /; /1/)
tt
/= /(/1 /+ T
/1
/) c
/(/2 /; /1/)
ut
/= T
/2
/(/1 /+ T
/1
/)
c
/(/2 /; /1/)
tu
/= /(/1 /+ T
/1
/) T
/2
c
/(/2 /; /1/)
uu
/= T
/2
/(/1 /+ T
/1
/) T
/2
c
/(/1
/3
/)
vv
/= /1 /:
is a cellular basis of H /(c hec k/!/)/. Note that u /= t s
/2
and c
/(/2 /; /1/)
tu
/= c
/(/2 /; /1/)
tt
T
/2
/. W e
generalize this example in the next c hapter/.
Throughout this Chapter w e assume that C /= f c
/
st
g is a /xed cellular basis
of the algebra A /. W e b egin our study of cellular algebras b y noting four easy
consequences of the de/nition/.
F or / /2 / let A
/
b e the R /{mo dule with basis the set of c
/
uv
where / /2 //, / / /
and u /; v /2 T /( / /)/. Th us/,
/
A
/
/ A
/
and A
/
/=
/
A
/
has basis c
/
st
/+
/
A
/
where s /; t /2 T /( / /)/.
/2/./3 Corollary L et / b e an element of / /.
/(i/) Supp ose that s /2 T /( / /) and a /2 A /. Then for al l t /2 T /( / /)
a
/
c
/
st
/=
X
u /2T /( / /)
r
u
c
/
ut
mo d
/
A
/
wher e for e ach u /, r
u
is the element of R determine d by /(/2/./1/)/(ii/) /.
/(ii/) The R /{mo dules A
/
and
/
A
/
ar e two/{side d ide als of A /.
/(iii/) Supp ose that //; / /2 / /, / /6/ / and x /2 A
/
/. Then ax/; xa /2
/
A
/
for al l a /2 A
/
/.
/(iv/) Supp ose that s and t ar e elements of T /( / /) /. Then ther e exists an element r
st
of R such that for any u /; v /2 T /( / /)
c
/
us
c
/
tv
/= r
st
c
/
uv
mo d
/
A
/
/:
Pro of/. Applying the an ti/{isomorphism / to /(/2/./1/)/(ii/) pro v es /(i/)/. The remaining
statemen ts no w follo w directly from part /(i/) and /(/2/./1/)/(ii/)/.
Corollary /2/./3/(iv/) is the k ey whic h unlo c ks the irreducible mo dules of a cellular
algebra/. F or eac h / /2 / the /(righ t/) cell mo dule C
/
is the righ t A /{mo dule whic h is
free as an R /{mo dule with basis f c
/
t
j t /2 T /( / /) g and where for eac h a /2 A
/2 /: /4 c
/
t
a /=
X
v /2T /( / /)
r
v
c
/
v
where r
v
is the elemen t of R determined b y /(/2/./1/)/(ii/)/. By /(/2/./1/)/(ii/) these de/nitions
mak e C
/
in to an A /{mo dule/. Similarly /, abusing notation de/ne the left cell mo dule
C
/ /
to b e the free R /{mo dule with basis f c
/
t
j t /2 T /( / /) g and A /{action giv en b y
/2 /: /5 a
/
c
/
t
/=
X
v /2T /( / /)
r
v
c
/
v
for all a /2 A and where/, once again/, r
v
is giv en b y /(/2/./1/)/(ii/)/. Then the ideals A
/
/=
/
A
/
and C
/ /
/
R
C
/
are canonically isomorphic via c
/
st
/+
/
A
/
/7/? /! c
/
s
/
 c
/
t
for s /; t /2 T /( / /)/.
By Corollary /2/./3/(iv/) w e can de/ne a bilinear form h /; i /: C
/
/ C
/
/? /! R to b e
the unique bilinear map suc h that/, for an y s /, t /2 T /( / /)/,
/2 /: /6 c
/
us
c
/
tv
/= h c
/
s
/; c
/
t
i c
/
uv
mo d
/
A
/
/;
where u and v are an y elemen ts of T /( / /)/. The next result sho ws that h /; i is b oth
symmetric and asso ciativ e/.
/1/. CELLULAR BASES /1/1
/2/./7 Prop ositio n Supp ose that / /2 / and let x/; y /2 C
/
/. Then
/(i/) h x/; y i /= h y /; x i /.
/(ii/) h xa/; y i /= h x/; y a
/
i for al l a /2 A /.
/(iii/) xc
/
uv
/= h x/; c
/
u
i c
/
v
for al l u /; v /2 T /( / /) /.
Pro of/. Because h /; i is bilinear it is su/cien t to consider the case where x /= c
/
s
and y /= c
/
t
for some s /; t /2 T /( / /)/. Let u and v b e an y elemen ts of T /( / /)/. Then/, b y
de/nition/,
h c
/
s
/; c
/
t
i c
/
uv
/ c
/
us
c
/
tv
/= /( c
/
vt
c
/
su
/)
/
/ /( h c
/
t
/; c
/
s
i c
/
vu
/)
/
/= h c
/
t
/; c
/
s
i c
/
uv
mo d
/
A
/
/;
pro ving /(i/)/. Similarl y for /(ii/)/,
h c
/
s
a/; c
/
t
i c
/
uv
/ /( c
/
us
a /) c
/
tv
/= c
/
us
/( ac
/
tv
/) / h c
/
s
/; c
/
t
a
/
i c
/
uv
mo d
/
A
/
/:
Finally /, when x /= c
/
s
/, part /(iii/) is precisely the de/nition of h /; i /.
/2/./8 Let rad C
/
/= f x /2 C
/
j h x/; y i /= /0 for all y /2 C
/
g /. Then b y Prop osition /2/./7/(ii/)/,
rad C
/
is an A /{submo dule of C
/
/. Accordingly /, w e de/ne D
/
/= C
/
/= rad C
/
/.
Although w e ha v e y et to do an ything di/cult/, w e can no w exhibit some irre/-
ducible A /{mo dules/. Recall that the Jacobson radical of a mo dule is the smallest
submo dule with a semisimple quotien t/; it is also the in tersection of all of the max/-
imal ideal in the mo dule/.
/2/./9 Prop ositio n Supp ose that R is a /eld and let / b e any element of / such
that D
/
/6/= /0 /.
/(i/) The right A /{mo dule D
/
is absolutely irr e ducible/.
/(ii/) The Jac obson r adic al of C
/
is e qual to rad C
/
/.
Pro of/. Let x b e an y non/{zero elemen t of C
/
n rad C
/
/. Then h x/; y i /6 /= /0 for some
y /2 C
/
and/, b ecause R is a /eld/, w e ma y assume that h x/; y i /= /1/. No w y /=
P
s /2T /( / /)
r
s
c
/
s
for some r
s
/2 R /; so/, for eac h t /2 T /( / /)/, de/ne y
t
/=
P
s /2 /
r
s
c
/
st
/2 A /.
Then/, b y Prop osition /2/./7/(iii/)/,
xy
t
/=
X
s /2T /( / /)
r
s
xc
/
st
/=
X
s /2T /( / /)
r
s
h x/; c
/
s
i c
/
t
/= h x/; y i c
/
t
/= c
/
t
/:
Consequen tly /, x generates C
/
/. This argumen t applies to an y elemen t of C
/
whic h
do es not b elong to the radical/; consequen tly /, D
/
is irreducible and rad C
/
is the
unique maxim al prop er submo dule of C
/
/, pro ving /(ii/)/. By the same argumen t/, D
/
is irreducible for an y extension /eld of R so in fact D
/
is absolutely irreducible/.
/2/./1/0 Prop ositi on Supp ose that R is a /eld and let / and / b e elements of / such
that D
/
/6/= /0 and let M b e a pr op er submo dule of C
/
/.
/(i/) If / /: C
/
/? /! C
/
/= M is a non/{zer o homomorphism then / / / /.
/(ii/) Supp ose that / /= / /. Then Hom
A
/( C
/
/; C
/
/= M /)
/
/=
R /.
Pro of/. De/ne elemen ts x/; y and y
t
/=
P
s
r
s
c
/
st
as in the pro of of Prop osition /2/./9/,
where t /2 T /( / /) and let / /: C
/
/? /! C
/
/= M b e an A /{mo dule homom orphism /. Then
there exists some a
/
/2 C
/
suc h that / /( x /) /= M /+ a
/
/. Therefore/, / /( c
/
t
/) /= / /( xy
t
/) /=
/ /( x /) y
t
/= M /+ a
/
y
t
for all t /2 T /( / /)/. By Corollary /2/./3/(iii/) and /(/2/./4/)/, if / /6/ / then
a
/
y
t
/= /0 so / /( c
/
t
/) /= /0 for all t /. Consequen tly /, if / /6/= /0 then / / / /, pro ving /(i/)/.
/1/2 /2/. CELLULAR ALGEBRAS
No w supp ose that / /= / /. Then b y Prop osition /2/./7/(iii/) w e /nd that
/ /( c
/
t
/) /= M /+ a
/
y
t
/= M /+
X
s /2T /( / /)
r
s
a
/
c
/
st
/= M /+ c
/
t
h a
/
/; y i /:
Hence/, / is just the natural pro jection C
/
/! C
/
/= M comp osed with m ultiplicati on
b y h a
/
/; y i /.
/2/./1/1 Corollary Supp ose that R is a /eld and let / and / b e elements of / such
that D
/
/6/= /0 and D
/
/
/=
D
/
/. Then / /= / /.
Pro of/. By assumption there exists a non/{zero homomorphism / /: C
/
/? /! D
/
/;
whence / / / b y /(i/)/. By symmetry /, / / / /. Th us / /= / as required/.
/2/. Simple mo dules in a cellular algebra
In this section w e sho w that ev ery irreducible A /{mo dule is isomorphic to some
D
/
/, for some / /2 //, and w e describ e the decomp osition matrix of A /. Throughout/,
w e assume that the p oset / is /nite/; th us A is a /nite dimensional algebra/.
/2/./1/2 Lemma Supp ose that / is a minimal element of / /. Then rad C
/
/= /0 /; c on/-
se quently/, C
/
/= D
/
/.
Pro of/. By w a y of con tradiction/, supp ose that rad C
/
/6/= /0/; then there exists some
x /2 C
/
suc h that h x/; y i /= /0 for all y /2 C
/
/. W rite x /=
P
t
r
t
c
/
t
and consider
/^x /=
P
t
r
t
c
/
tt
/. By Prop osition /2/./7/(iii/)/, if u /; v /2 T /( / /) then /^xc
/
uv
/2
/
A
/
/. Therefore/, b y
the minim al it y of / and Corollary /2/./3/(iii/)/, /^x a /2
/
A
/
for all a in A /. In particular/,
/^x /= /^ x / /1 b elongs to
/
A
/
/, yielding the promised con tradiction/.
/2/./1/3 Theorem /(Graham/{Lehrer/) Supp ose that R is a /eld and that / is //-
nite/. Then f D
/
j / /2 / and D
/
/6/= /0 g is a c omplete set of p airwise ine quivalent
irr e ducible A /{mo dules/.
Pro of/. By Prop osition /2/./9 if D
/
/6/= /0 then D
/
is irreducible and b y Corollary /2/./1/1
D
/
/6
/
/=
D
/
whenev er / /2 / and / /6/= / /. It remains to sho w that ev ery irreducible
A /{mo dule is isomorphic to one of the non/{zero mo dules D
/
with / /2 //.
By the de/nition/, an y total ordering of / giv es rise to a /ltration of A in whic h
eac h comp osition factor is isomorphic to a cell mo dule of A /. Consequen tly /, to pro v e
Theorem it su/ces to sho w that if / /2 / then ev ery irreducible comp osition factor
of C
/
is isomorphic to D
/
for some / /2 //. T o pro v e this w e argue b y induction on
/ /.
If / is a minim al elemen t of / then C
/
/= D
/
b y Lemma /2/./1/2 and there is
nothing to pro v e/.
No w supp ose that / is not minimal and let D b e an irreducible comp osition
factor of C
/
/. Then either D /= D
/
or D is a comp osition factor of rad C
/
/. Let x
b e an elemen t of rad C
/
and let
/
A
/
b e the R /{mo dule spanned b y
f c
/
uv
j / /2 / /; / /6/> / and u /; v /2 T /( / /) g /:
Then
/
A
/
is a t w o/{sided ideal of A /, b y /(/2/./1/)/(i/) and Corollary /2/./3/(i/)/, and x
/
A
/
/= /0
b y Corollary /2/./3/(iii/)/. Therefore/, an y comp osition factor of rad C
/
is a comp osition
factor of A/=
/
A
/
/. Ho w ev er/, b y construction/, A/=
/
A
/
has a comp osition series with
comp osition factors isomorphic to cell mo dules C
/
with / /2 / and / /> / /. By
/2/. SIMPLE MODULES IN A CELLULAR ALGEBRA /1/3
induction/, if / /> / then ev ery irreducible comp osition factor of C
/
is isomorphic
to D
/
for some / /2 //. This completes the pro of/.
Let /
/+
/= f / /2 / j D
/
/6/= /0 g /. Then / /2 /
/+
if and only if the bilinear form
h /; i on C
/
is non/{degenerate/. In principle/, Theorem /2/./1/3 classi/es the simple
A /{mo dules/; ho w ev er/, in practice/, it is often di/cult to determine the set /
/+
/.
If / /2 /
/+
and / /2 / let d
//
b e the comp osition m ultipli cit y of the irreducible
mo dule D
/
in C
/
/; b y the Jordan/{H/ older Theorem /[ /1/0 /]/, d
//
is w ell/{de/ned/. The
matrix D /= /( d
//
/)/, where / /2 / and / /2 /
/+
/, is the so/{called decomp osition matrix of
A /. The next result could also ha v e b een deduced during the pro of of Theorem /2/./1/3/.
/2/./1/4 Corollary Supp ose that R is a /eld/. Then the de c omp osition matrix D of
A is unitriangular/; that is/, if / /2 /
/+
and / /2 / then d
//
/= /1 and d
//
/6/= /0 only
if / / / /.
Pro of/. The decomp osition n um b er d
//
is non/{zero if and only if there exists
a submo dule M of C
/
and a homom orphism / /: C
/
/? /! C
/
/= M with the image
of / isomorphic to D
/
/. Therefore/, if d
//
/6/= /0 then / / / b y Prop osition /2/./1/0/(i/)/.
F urthermore/, if / /= / then C
/
/= k er / is simple if and only if k er / /= rad C
/
b y
Prop osition /2/./9/(ii/)/, so d
//
/= /1/.
Next w e describ e the Cartan in v arian ts of A /. F or eac h elemen t / /2 /
/+
w e
ha v e a simple mo dule D
/
and a pro jectiv e indecomp osable mo dule P
/
/, uniquely
determined up to isomorphism b y the prop ert y that it has simple head D
/
/. In fact/,
since D
/ /
/
R
D
/
is a simple ideal w e ha v e A
/
/=
L
/ /2 /
/+
D
/ /
/
R
P
/
/.
If / /2 /
/+
let c
//
b e the comp osition m ultiplicit y of D
/
in P
/
/. Then C /= /( c
//
/)/,
where //; / /2 /
/+
/, is the Ca rtan matrix of A /.
In order to compute C w e need t w o Lemmas and some more notation/.
/2/./1/5 Lemma Supp ose that R is a /eld/, / /2 /
/+
and / /2 / /. Then
d
/ /
/= dim
R
Hom
A
/( P
/
/; C
/
/) /= dim
R
P
/
/
A
C
/ /
/:
Pro of/. If / /2 / then d
/ /
is non/{zero only if there exists a submo dule M of C
/
together with a surjectiv e homom orphism / /: M /? /! D
/
/. Since P
/
is pro jectiv e/, /
lifts uniquely to a homomo rphism
/^
/ /: P
/
/? /! M and the inclusion M /, /! C
/
pro duces
an A /{homomorphism P
/
/? /! C
/
/. Th us/, d
/ /
/= dim
R
Hom
A
/( P
/
/; C
/
/) as required/.
A subset /? of / a p oset ideal if / /2 /? whenev er / /2 /? and / /> / /. If /? is a
p oset ideal let A /(/?/) b e the R /{submo dule of A with basis f c
/
uv
g where / /2 /? and
u /; v /2 T /( / /)/. Then A /(/?/) is a t w o/{sided ideal of A b y /(/2/./1/)/(ii/) and Corollary /2/./3/(i/)/.
/2/./1/6 Lemma Supp ose that P is a pr oje ctive A /{mo dule/. Then P has a /ltr ation
/? /= P
/0
/ / / / / P
k
/= P with c omp osition factors P
i
/=P
i /? /1
isomorphic to the
/( non/{zer o /) mo dules P /
A
/( C
/ /
/
R
C
/
/) /, with e ach / /2 / o c curring exactly onc e/.
Pro of/. Let /? b e a p oset ideal and supp ose that /? /[ f / g is also an ideal for some
/ /2 / n /?/. Then /0 /! A /(/?/) /! A /(/? /[ f / g /) /! A /(/?/) /= A /(/? /[ f / g /) /! /0 is a short exact
sequence of /( A/; A /)/{bimo dules and A /(/? /[ f / g /) /= A /(/?/)
/
/=
C
/ /
/
R
C
/
/. Because P is
pro jectiv e/, w e can tensor this sequence with P to obtain an exact sequence
/0 /! P /
A
A /(/?/) /! P /
A
A /(/? /[ f / g /) /! P /
A
A /(/? /[ f / g /) /= A /(/?/) /! /0 /:
/1/4 /2/. CELLULAR ALGEBRAS
Consequen tly /, P /
A
A /(/? /[ f / g /) /=P /
A
A /(/?/)
/
/=
P /
A
/( C
/ /
/
R
C
/
/)/.
No w supp ose that /? /= /?
/0
/ /?
/1
/ / / / / /?
k
/= /? is a maxima l c hain of ideals
in //. Then/, for i /= /1 /; /2 /; /: /: /: /; k /, w e ha v e /?
i
/= /?
i /? /1
/[ f /
i
g for some /
i
/2 /?/. Therefore/,
/0 /= A /(/?
/0
/) /, /! A /(/?
/1
/) /, /! / / / /, /! A /(/?
k
/) /= A is a /ltration of A /. T ensoring with P
giv es a /ltration of P with comp osition factors/, b y the last paragraph/, precisely the
non/{zero mo dules P /
A
/( C
/ /
/
R
C
/
/) for / /2 //.
Noting that P /
A
/( C
/ /
/
R
C
/
/)
/
/=
/( P /
A
C
/ /
/) /
R
C
/
/
/=
/(dim P /
A
C
/ /
/) C
/
/,
w e see that ev ery pro jectiv e A /{mo dule P has a cell mo dule /ltration/; that is a
/ltration in whic h ev ery comp osition factor is isomorphic to a cell mo dule/.
In the next result/, D
t
denotes the transp ose of D /.
/2/./1/7 Theorem /(Graham/{Lehrer/) Supp ose that R is a /eld and that / is /nite/.
Then C /= D
t
D /. In p articular/, the Cartan matrix of A is symmetric/.
Pro of/. Let / and / b e elemen ts of /
/+
and tak e P /= P
/
/. By Lemma /2/./1/6/, P
/
has a /ltration with comp osition factors the non/{zero mo dules P
/
/
A
/( C
/ /
/
R
C
/
/)/,
and where eac h / /2 / o ccurs at most once/. Therefore/, b y Lemma /2/./1/5/,
c
//
/= /[ P
/
/: D
/
/] /=
X
/ /2 /
/[/( P
/
/
A
C
/ /
/) /
R
C
/
/: D
/
/]
/=
X
/ /2 /
dim
R
/( P
/
/
A
C
/ /
/)/[ C
/
/: D
/
/]
/=
X
/ /2 /
d
/ /
d
/ /
/:
Hence/, C /= D
t
D as claimed/.
/2/./1/8 Corollary Supp ose that R is a /eld/. Then the fol lowing ar e e quivalent/.
/(i/) A is /( split /) semisimple/.
/(ii/) C
/
/= D
/
for al l / /2 / /.
/(iii/) rad C
/
/= /0 for al l / /2 / /.
/(iv/) d
//
/= /
//
for al l / and / in / /.
Pro of/. First w e note that if A is semisimple then R is a splitting /eld for A
since eac h D
/
is absolutely irreducible b y Prop osition /2/./9/. Th us/, the algebra A is
semisimple if and only if it is split semisimple/.
No w supp ose that A is semisimple/. Then P
/
/= D
/
for all / /2 /
/+
/; consequen tly /,
C
/
/= D
/
b y Theorem /2/./1/7/. F urthermore/, b ecause A is semisimple/,
dim
R
A /=
X
/ /2 /
/+
dim
R
/( C
/
/)
/2
/=
X
/ /2 /
/+
jT /( / /) j
/2
/:
Ho w ev er/, dim
R
A /=
P
/ /2 /
jT /( / /) j
/2
/, so w e m ust ha v e / /= /
/+
/. Hence/, /(i/) implies /(ii/)/.
Certainly /(ii/) and /(iii/) are b oth equiv alen t and they b oth imply /(iv/)/, so assume
that /(iv/) holds/. In particular/, /(iv/) implies that / /= /
/+
and/, using Theorem /2/./1/7
again/, that P
/
/= C
/
/= D
/
/. Therefore/, A is a direct sum of simple /(pro jectiv e/)
mo dules/; that is to sa y it is semisimple/.
The next result connects the theory of quasi/{hereditary algebras and cellular
algebras/. Quasi/{hereditary algebras are v ery a imp ortan t class of algebras/; ho w ev er/,
/2/. SIMPLE MODULES IN A CELLULAR ALGEBRA /1/5
as w e do not need an y results from their theory /, w e refer the in terested reader to /[ /8 /]
for the de/nition/.
/2/./1/9 Corollary Supp ose that R is a /eld/. Then the fol lowing ar e e quivalent/.
/(i/) / /= /
/+
/.
/(ii/) The de c omp osition matrix D is a squar e unitriangular matrix/.
Mor e over/, if either of these c onditions is satis/e d then A is quasi/{her e ditary/.
Pro of/. That /(i/) and /(ii/) are equiv alen t is clear from Corollary /2/./1/4/. If /(i/) holds
then it follo ws directly from the de/nitions in /[ /8 /] that A is quasi/{hereditary /.
Implicitly /, part /(ii/) pla ys a role in the pro of of the Jan tzen sum form ula in
Chapter /5/; this criterion indicates that b eing quasi/{hereditary is a non/{degeneracy
prop ert y /.
Finally /, w e consider blo c ks of a cellular algebra/. Supp ose that R is a /eld /(and
that / is /nite/)/. Then A can b e decomp osed as a direct sum of indecomp osable t w o/{
sided ideals/; sa y A /= B
/1
/ / / / / B
k
/. The ideals B
/1
/; /: /: /: /; B
k
are uniquely determined
and are called the blo ck ideals of A /. F urthermore/, for eac h i /, there exists a /(unique/)
primitiv e cen tral idemp oten t e
i
suc h that B
i
/= e
i
A /= e
i
Ae
i
/= Ae
i
/. It follo ws that
/1 /= e
/1
/+ / / / /+ e
k
and that e
i
e
j
/= /
ij
e
i
/; th us/, B
i
is an R /{algebra with iden tit y e
i
/.
Pro ofs of these general facts can b e found in /[ /1/0 /, Chapter VI I I/]/.
Tw o A /{mo dules are said to b elong to the same blo ck if all of their irreducible
comp osition factors lie in the same blo c k/. In particular/, b ecause e
i
e
j
/= /
ij
for
/1 / i/; j / k /, a righ t A /{mo dule N b elongs to the same blo c k as B
i
if and only if
N e
i
/= N and N e
j
/= /0 if i /6/= j /.
/2/./2/0 Lemma Supp ose that e and f ar e idemp otents in A /. Then Hom
A
/( eA/; f A /)
and f Ae ar e c anonic al ly isomorphic as R /{mo dules/. Mor e over/, if e /= f then
End
A
/( eA /) and eAe ar e isomorphic as algebr as/.
Pro of/. If /' /2 Hom
A
/( eA/; f A /) then /' is completely determined b y /' /( e /)/. Certainly /,
/' /( e /) /2 f A and/, b ecause e is idemp oten t/, /' /( e /) /= /' /( e
/2
/) /= /' /( e /) e /2 f Ae /. Hence/, the
map /' /7/? /! /' /( e /) is an isomorphism/.
Finally /, supp ose that e /= f /. F or homomorphism s /' and / in End
A
/( eA /)/,
write /' /( e /) /= ea
/'
e and / /( e /) /= ea
/ 
e for some a
/'
/; a
/ 
/2 A /. Then /' /( e /) / /( e /) /=
/( ea
/'
e /)/( ea
/ 
e /) /= /( ea
/'
e /) a
/ 
e /= /( /'/ /)/( e /)/. Hence/, End
A
/( eA /) and eAe are isomorphic
algebras/.
In particular/, if /1 / i/; j / k then Hom
A
/( B
i
/; B
j
/)
/
/=
e
j
Ae
i
/= e
j
e
i
A /= /
ij
B
i
/.
Sa y that / and / in / are link ed if there exist / /= /
/0
/; /
/1
/; /: /: /: /; /
k
/= / in /
suc h that C
/
i /? /1
and C
/
i
ha v e a common irreducible comp osition factor for i /=
/1 /; /2 /; /: /: /: /; k /. This de/nes an equiv alence relation on //; imp ortan tly /, if / /2 /
/+
then
d
//
/6/= /0 only if / and / are link ed/.
/2/./2/1 Theorem Supp ose that R is a /eld and that / is /nite/. L et / and / b e
elements of / /. Then / and / ar e linke d if and only if C
/
and C
/
ar e in the same
blo ck/.
Pro of/. As a righ t A /{mo dule eac h blo c k B
i
decomp oses in to a direct sum of prin/-
cipal indecomp osable mo dules/. This giv es a partition /
/+
/= /
/+
/1
t /: /: /: t /
/+
k
of /
/+
suc h
that B
i
/
/=
L
/ /2 /
/+
i
D
/ /
/
R
P
/
for i /= /1 /; /2 /; /: /: /: /; k /. F urthermore/, b y Lemma /2/./1/6/,
eac h indecomp osable P
/
has a cell mo dule /ltration/; th us/, to pro v e the Theorem
it su/ces to sho w that //; / /2 /
/+
are link ed if and only if //; / /2 /
/+
i
for some i /.
/1/6 /2/. CELLULAR ALGEBRAS
Supp ose /rst that / and / are in /
/+
and that D
/
is a comp osition factor of P
/
/.
Then/, as in the pro of of Lemma /2/./1/5/, Hom
A
/( P
/
/; P
/
/) /6/= /0/. Consequen tly P
/
and
P
/
m ust b e con tained in the same blo c k since Hom
A
/( B
i
/; B
j
/) /= /0 if i /6/= j /. Hence/,
if / and / in / are link ed then C
/
and C
/
are in the same blo c k/.
Con v ersely /, supp ose that there exists an in teger i /, with /1 / i / k /, and / and /
in /
/+
i
suc h that C
/
and C
/
are not link ed/. Then P
/
and P
/
ha v e no comp osition
factor in common so Hom
A
/( P
/
/; P
/
/) /= /0/. Let /
/+
i /1
b e the set of / /2 /
/+
i
whic h are
link ed to / and let /
/+
i /2
/= /
/+
i
n /
/+
i /1
/. F or a /= /1 /; /2 let B
ia
/=
L
/ /2 /
/+
ia
D
/ /
/
 P
/
/. Then/,
b y Lemma /2/./2/0 and the remark follo wing it/,
B
i
/
/=
End
A
/( B
i
/) /= End
A
/( B
i /1
/ B
i /2
/) /= End
A
/( B
i /1
/) / End
A
/( B
i /2
/) /;
con tradicting the fact that B
i
is an indecomp osable blo c k ideal of A /.
Notes on Chapter /2
/1/. All of the results in this Chapter are due to Graham and Lehrer and can b e
found in /[ /2/5 /, /2/6 /]/.
/2/. The in tro duction of cellular algebras w as largely motiv ated b y the Kazhdan/{
Lusztig /[ /4/6 /] bases of the Iw ahori/{Hec k e algebras of t yp e A /. Man y more exam/-
ples of cellular algebras can b e found in /[ /2/5 /, /2/6 /]/. F or example/, /(generalized/)
T emp erley/-Lieb algebras/, Jones/' ann ular algebra/, Ariki/{Koik e algebras/, and the
cyclotomic q /{Sc h ur algebras of /[ /1/7 /] are all cellular/.
/3/. A ring theoretic de/nition of cellular algebras has b een K/ onig and Xi /[ /5/0 /]/; in
particular/, their approac h is indep enden t of a c hoice of basis/. They ha v e also
in v estigated cellular algebras under Morita equiv alence /[ /4/8 /] and sho wn that the
p oset / is not/, in an y sense/, an in v arian t of a cellular algebra /[ /4/9 /]/.
/4/. If A is also a symmetric algebra then Graham /[ /2/5 /, /4/./1/2/] has sho wn that the dual
basis of a cellular basis of A is again cellular/, pro viding that the trace form on A
comm utes with the / /{automorphism /.
/5/. Du and Rui /[ /2/0 /] ha v e pro v ed a con v erse to Corollary /2/./1/9/; they sho w ed that an y
quasi/-hereditary algebra p ossessing a certain t yp e of in v olution is cellular/.
CHAPTER /3
The Mo dular represen tation theory of H
In this c hapter w e construct Murph y/'s basis of the Iw ahori/{Hec k e algebra H /.
Murph y/'s pap ers /[ /5/5 /, /5/6 /]app eared b efore the theory of cellular algebras/: nev erthe/-
less/, his basis is cellular/.
F or the rest of these notes w e assume that q is an in v ertible elemen t of R /.
In particular/, this implies that T
i
is in v ertible with T
/? /1
i
/= q
/? /1
/( T
i
/? q /+ /1/) for
i /= /1 /; /2 /; /: /: /: /; n /? /1/. Consequen tly if w /2 S
n
and s
i
/1
/: /: /: s
i
k
is a reduced expression
for w then T
/? /1
w
/= T
/? /1
i
k
/: /: /: T
/? /1
i
/1
/.
/1/. The com binatori cs of tableaux
Let m b e a p ositiv e in teger/. A comp osition of m is a sequence / /= /( /
/1
/; /
/2
/; /: /: /: /)
of non/{negativ e in tegers suc h that j / j /=
P
i
/
i
/= m /. The in tegers /
i
/, i / /1/, are the
p arts of / /; if /
i
/= /0 for i /> k w e iden tify / with /( /
/1
/; /: /: /: /; /
k
/)/. A comp osition / is
a pa rtition if /
i
/ /
i /+/1
for all i / /1/.
The diagram of a comp osition / is the subset
/[ / /] /= f /( i/; j /) j /1 / j / /
i
and i / /1 g /:
of N / N /. The elemen ts of /[ / /] are called the no des of / /; more generally /, a no de
is an y elemen t of N / N /. It will b e con v enien t to represen t the diagram of / as an
arra y of b o xes in the plane/. F or example/, if / /= /(/2 /; /3/) then /[ / /] /= /.
If / is a comp osition of n then a / /{ tableau is a bijection t /: /[ / /] /? /! f /1 /; /2 /; /: /: /: /; n g /;
w e sa y that t has shap er / and write Shap e/( t /) /= / /. Notice that a tableau t
corresp onds to a lab elled diagram/; for example/, if / /= /(/2 /; /3/) then
/1 /2
/3 /4 /5
and
/4 /2
/3 /1 /5
are t w o / /{tableaux/. Accordingly /, w e will sp eak of the ro ws and columns of tableaux/.
W e distinguish t w o particular t yp es of / /{tableaux/. A / /{tableau t is ro w stan/-
da rd if the en tries in t increase from left to righ t in eac h ro w/; t is standa rd if /(i/)
/ is a partition and /(ii/) the en tries in t increase from left to righ t in eac h ro w and
from top to b ottom in eac h column/. If / is a partition let Std/( / /) denote the set of
standard / /{tableaux/.
Of the t w o tableaux ab o v e/, only the /rst is ro w standard/; neither is standard
b ecause /(/2 /; /3/) is not a partition/. If / /= /(/3 /; /2/) then
/1 /3 /4
/2 /5
is a standard / /{tableau/.
Giv en an y comp osition / let t
/
b e the ro w standard / /{tableau in whic h the
in tegers /1 /; /2 /; /: /: /: /; n are en tered in increasing order from left to righ t along the ro ws
of /[ / /]/. F or example/, if / /= /(/2 /; /3/) then t
/
/=
/1 /2
/3 /4 /5
/.
If / /= /( /
/1
/; /: /: /: /; /
k
/) is a comp osition of n then the symmetric group S
n
acts
from the righ t up on the set of / /{tableaux b y p erm uting the en tries inside a giv en
tableau/. F or example/, if t /=
/1 /3
/2 /4 /5
then t /(/2 /; /4 /; /5 /; /3/) /=
/1 /2
/4 /5 /3
/.
Let S
/
b e the subgroup of S
n
whic h stabilizes the ro ws of t
/
and let H /( S
/
/)
b e the subalgebra of H spanned b y f T
w
j w /2 S
/
g /. Then S
/
/= S
/
/1
/ / / / / S
/
k
/1/7
/1/8 /3/. THE MODULAR REPRESENT A TION THEOR Y OF H
and H /( S
/
/) is isomorphic to H /( S
/
/1
/) / / / / / H /( S
/
k
/)/, the Iw ahori/{Hec k e of S
/
/.
It follo ws that S
/
is generated b y S /\ S
/
and that H /( S
/
/) is generated b y
f T
s
j s /2 S /\ S
/
g /. Finally /, w e let m
/
/=
P
w /2 S
/
T
w
and de/ne M
/
to b e the
righ t ideal m
/
H /.
/3/./1 Example Let / /= /(/2 /; /3/)/. Then t
/
/=
/1 /2
/3 /4 /5
/, S
/
/= S
/2
/ S
/3
/= h s
/1
/; s
/3
/; s
/4
i and
m
/
/= /(/1 /+ T
/1
/)/(/1 /+ T
/3
/+ T
/4
/+ T
/3
T
/4
/+ T
/4
T
/3
/+ T
/3
T
/4
T
/3
/)/.
/3/./2 Lemma Supp ose that / is a c omp osition of n and let w b e an element of S
/
/.
Then m
/
T
w
/= q
/` /( w /)
m
/
/.
Pro of/. It su/ces to sho w that if s /2 S /\ S
/
then m
/
T
s
/= q m
/
/. W e ha v e
m
/
T
s
/=
X
w /2 S
/
T
w
T
s
/=
X
w /2 S
/
/` /( w s /) />/` /( w /)
T
w
T
s
/+
X
w /2 S
/
/` /( w s /) /</` /( w /)
T
w
T
s
/=
X
w /2 S
/
/` /( w s /) />/` /( w /)
T
w s
/+
X
w /2 S
/
/` /( w s /) /</` /( w /)
/?
/( q /? /1/) T
w
/+ q T
w s
/
/= q m
/
/;
where the last line follo ws b y the m ultiplicatio n form ulae of Theorem /1/./1/1/.
Comparing Lemma /3/./2 and Corollary /1/./1/3 w e see that m
/
H /( S
/
/) /= Rm
/
a/ords the trivial represen tation of H /( S
/
/) and/, moreo v er/, that as an H /{mo dule
M
/
/
/=
m
/
H /( S
/
/) /
H /( S
/
/)
H /. Th us/, M
/
is the Iw ahori/{Hec k e algebra analogue
of the induced represen tation Ind
S
n
S
/
/(/1/)/.
T o giv e a basis of M
/
w e need a set of coset represen tativ es for S
/
in S
n
/.
/3/./3 Prop ositio n Supp ose that / is a c omp osition of n and let
D
/
/= f d /2 S
n
j t
/
d is r ow standar d g /:
Then D
/
is a c omplete set of right c oset r epr esentatives of S
/
in S
n
/. Mor e over/, if
w /2 S
/
and d /2 D
/
then /` /( w d /) /= /` /( w /) /+ /` /( d /) and T
w d
/= T
w
T
d
/.
Pro of/. If S
/
w /= S
/
v then the tableaux t
/
w and t
/
v agree up to a reordering of
the en tries in eac h ro w/; therefore/, D
/
is a complete set of righ t coset represen tativ es
of S
/
in S
n
/.
It remains to sho w that if w /2 S
/
and d /2 D
/
then /` /( w d /) /= /` /( w /) /+ /` /( d /)/.
First note that if i /< j /, where i and j are in the same ro w of t
/
/, then id /< j d /. In
particular/, if i and i /+/1 are in the same ro w of t
/
then id /< /( i /+/1/) d so /` /( s
i
d /) /= /1/+ /` /( d /)
whenev er s
i
/2 S /\ S
/
b y Corollary /1/./4/.
No w supp ose that w /2 S
/
and that /` /( w /) /> /1/. Then w /= s
i
v and /` /( w /) /= /1 /+ /` /( v /)
for some s
i
/2 S
/
/\ S and v /2 S
/
/; therefore/, iv /< /( i /+ /1/) v b y Corollary /1/./4/. No w iv
and /( i /+ /1/) v b elong to the same ro w of t
/
/, so iv d /< /( i /+ /1/) v d b y the last paragraph/;
whence/, /` /( s
i
v d /) /= /1 /+ /` /( v d /) b y Corollary /1/./4 again/. Consequen tly /, b y induction on
the length of v w e /nd that
/` /( w d /) /= /` /( s
i
v d /) /= /1 /+ /` /( v d /) /= /1 /+ /` /( v /) /+ /` /( d /) /= /` /( w /) /+ /` /( d /)
as required/.
Th us eac h ro w standard / /{tableau corresp onds to a righ t coset of S
/
in S
n
/.
If t is a ro w standard / /{tableau let d /( t /) b e the unique elemen t of S
n
suc h that
t /= t
/
d /( t /)/. By Prop osition /3/./3 d /( t /) is the unique elemen t of minim al length in the
coset S
/
d /( t /)/; suc h coset represen tativ es are called distinguished coset rep resentatives /.
/1/. THE COMBINA TORICS OF T ABLEA UX /1/9
/3/./4 Corollary L et / b e a c omp osition of n /. Then M
/
is a fr e e R /{mo dule with
b asis f m
/
T
d /( t /)
j t a r ow standar d / /{table au g /. Mor e over/, if t is r ow standar d and
s /= t s
i
/, for some /1 / i /< n /, then
m
/
T
d /( t /)
T
i
/=
/8
/<
/:
q m
/
T
d /( t /)
/; if s is not r ow standar d/,
m
/
T
d /( s /)
/; if s is r ow standar d and /` /( d /( s /)/) /> /` /( d /( t /)/) /,
q m
/
T
d /( s /)
/+ /( q /? /1/) m
/
T
d /( t /)
/; if s is r ow standar d and /` /( d /( s /)/) /< /` /( d /( t /)/) /.
Pro of/. That M
/
is a free R /{mo dule with the basis sho wn follo ws directly from
Theorem /1/./1/1/, Lemma /3/./2 and Prop osition /3/./3/. It remains to v erify the m ultipli /-
cation form ulae/.
Let w /= d /( t /) s
i
/; then s /= t
/
w /. No w/, s is not ro w standard if and only if i
and i /+ /1 are in the same ro w of t /, in whic h case w and d /( t /) are in the same righ t
coset of S
/
/. Therefore/, w /= sd /( t /) for some s /2 S
/
and /` /( w /) /= /` /( d /( t /)/) /+ /1 b y
Prop osition /3/./3/; hence/, m
/
T
d /( t /)
T
i
/= m
/
T
s
T
d /( t /)
/= q m
/
T
d /( t /)
b y Lemma /3/./2/.
Finally /, if i and i /+ /1 are not in the same ro w of s then s is ro w standard/; th us/,
d /( s /) /2 D
/
and the remaining statemen ts follo w from the m ultiplication form ulae of
Theorem /1/./1/1/.
/3/./5 T o conclude this section w e in tro duce t w o partial orders/. Let / and / b e
comp ositions/. Then / D / if
i
X
j /=/1
/
j
/
i
X
j /=/1
/
j
for all i / /1 /:
If / D / w e sa y that / dominates / /. If / /6/= / w e write / B / /.
Next/, giv en a ro w standard tableau t and an in teger m / n let t /# m b e the
tableau obtained from t b y deleting all of the en tries greater than m /. Note that
t /# m is a ro w standard tableau for some comp osition of m /. Giv en ro w standard
/ /{tableaux s and t write s D t if Shap e/( s /# m /) D Shap e/( t /# m /) for m /= /1 /; /2 /: /: /: /; n /.
Similarly /, w e write s B t when s D t and s /6/= t /.
/3/./6 Example /(i/) Let / b e a partition of n and let t b e an y ro w standard / /{
tableau/. Then t
/
D t /.
/(ii/) Let s /=
/1 /3 /4
/2 /5
and t /=
/2 /3 /5
/1 /4
/. Then the follo wing table sho ws that s B t /.
m /1 /2 /3 /4 /5
s /# m
/1
/?
/1
/2
/1 /3
/2
/1 /3 /4
/2
/1 /2 /4
/3 /5
t /# m
/?
/1
/2
/1
/2 /3
/1
/2 /3
/1 /4
/2 /3 /5
/1 /4
Supp ose that r
/1
/: /: /: r
k
is a not necessarily reduced expression for some elemen t
of S
n
/, where r
/1
/; /: /: /: /; r
k
/2 S /. A sub exp ression of r
/1
/: /: /: r
k
is an y expression of the
form r
i
/1
/: /: /: r
i
l
where /1 / i
/1
/< / / / /< i
l
/ k /.
Giv en t w o elemen ts v and w in S
n
write v D w if v has a reduced expression
whic h is a sub expression of some reduced expression of w /. F or example/, /1 D w for
all w /2 S
n
/. By the strong exc hange condition /(/1/./5/)/, v D w if and only if there exist
re/
ections t
i
/; /: /: /: /; t
k
/2 T suc h that w /= v t
/1
/; /: /: /: t
k
and /` /( v t
/1
/: /: /: t
j /? /1
/) /< /` /( v t
/1
/: /: /: t
j
/)
for j /= /1 /; /2 /; /: /: /: /; k /. /(In fact/, one can sho w that v D w if and only if there exist
/2/0 /3/. THE MODULAR REPRESENT A TION THEOR Y OF H
re/
ections t
i
/; /: /: /: /; t
k
/2 T suc h that w /= v t
/1
/; /: /: /: t
k
and /` /( v t
/1
/: /: /: t
j
/) /= /` /( v /) /+ j for
j /= /1 /; /2 /; /: /: /: /; k /./) In particular/, this sho ws that D is a partial order on S
n
/.
The partial order D on S
n
is the ubiquitous Bruhat/{Chevalley o rder /. P erhaps
surprisingly /, it agrees with the dominance ordering on ro w standard / /{tableaux
/(when restricted to D
/
/)/.
/3/./7 Prop ositio n /(Dipp er/{James /) L et / b e a c omp osition of n and supp ose that s
and t ar e r ow standar d / /{table aux/. Then s D t if and only if d /( s /) D d /( t /) /.
Pro of/. First supp ose that s B t and c ho ose r minim al suc h that ro w r of s and
ro w r of t are di/eren t/. Let a b e the smallest n um b er whic h is in ro w r of s but
not in ro w r of t /; similarly /, let b b e the smallest n um b er whic h is in ro w r of t but
not in ro w r of s /. Then a /< b since s B t /. Therefore/, if v /= t /( a/; b /) then v B t and
d /( v /) B d /( t /)/. F urther/, if a is in ro w t of t and b is in ro w s of s then t /> r and t / s /;
so/, either v /= s or s B v /. Therefore/, b y induction/, d /( s /) D d /( v /)/; so d /( s /) B d /( t /) as
required/.
T o pro v e the con v erse it is su/cien t to consider the case where d /( t /) /= d /( s /) t for
some t /2 T suc h that /` /( d /( t /)/) /= /` /( d /( s /)/) /+ /1/. Ho w ev er/, in this case it is easy to see
from the de/nitions that s B t /.
The Prop osition has a tec hnical Corollary whic h will b e used man y times b elo w/.
/3/./8 Corollary Supp ose that / /, g and t ar e r ow standar d / /{table aux such that / B g
and d /( t /) /= d /( g /) w for some w /2 S
n
with /` /( d /( t /)/) /= /` /( d /( g /)/) /+ /` /( w /) /. Then ther e exist
r
s
/2 R such that m
/
T
d /( / /)
T
w
/=
P
s
r
s
m
/
T
d /( s /)
and wher e r
s
/6/= /0 only if s B t /.
Pro of/. It follo ws from Theorem /1/./1/1 that there exist elemen ts r
x
/2 R suc h that
T
d /( / /)
T
w
/=
P
r
x
T
x
where the sum is o v er elemen ts x /2 S
n
whic h ha v e a reduced
expression whic h is a sub expression of d /( / /) w /; that is/, r
x
/6/= /0 only if x D d /( / /) w /.
Consequen tly /, b y Corollary /3/./4/, m
/
T
d /( / /)
T
w
/=
P
s
r
s
m
/
T
d /( s /)
where the sum is o v er
ro w standard / /{tableaux s suc h that r
s
/6/= /0 only if d /( s /) D d /( / /) w /. By assump/-
tion d /( / /) is a prop er sub expression of d /( g /) and /` /( d /( g /) w /) /= /` /( d /( g /)/) /+ /` /( w /)/; so d /( / /) w
is a prop er sub expression of d /( t /) /= d /( g /) w /. Th us/, if r
s
/6/= /0 then s D d /( / /) w B d /( t /)/,
giving the result/.
/2/. The Murph y basis
In Corollary /3/./4 w e sa w that the p erm utation mo dules M
/
ha v e a basis indexed
b y ro w standard tableaux/; in this section w e sho w that H /= M
/(/1
n
/)
has a cellular
basis indexed b y pairs of standard tableaux of the same shap e/.
Let / b e the R /{linear an tiautomorphism of H determined b y T
/
i
/= T
i
for
i /= /1 /; /2 /; /: /: /: /; n /? /1/. Then T
/
w
/= T
w
/? /1
for all w /2 S
n
/.
Let / b e a comp osition of n and let s and t b e ro w standard / /{tableaux/.
De/ne m
st
i /= T
/
d /( s /)
m
/
T
d /( t /)
/( cf/. Example /2/./2/(ii/)/)/. In particular/, m
/
st
/= m
ts
for all
ro w standard tableaux s and t of the same shap e/.
If / /= /(/1
n
/) then/, as R /{mo dules/, M
/
/= H so the elemen ts f m
st
g certainly
span H b y Corollary /3/./4/. First w e sho w that w e need only those elemen ts m
st
/,
where the shap e of s and t is a partition /(not just a comp osition/)/.
/3/./9 Lemma L et / b e a c omp osition of n and let / b e the p artition obtaine d fr om
/ by r e or dering its p arts/. Supp ose that s and t ar e r ow standar d / /{table aux/. Then
/2/. THE MURPHY BASIS /2/1
m
st
is an R /{line ar c ombination of terms of the form m
uv
wher e u and v ar e r ow
standar d / /{table aux/.
Pro of/. Cho ose an elemen t d /2 S
n
suc h that S
/
/= d S
/
d
/? /1
and suc h that t
/
d and
t
/
d
/? /1
are b oth ro w standard /( d and d
/? /1
p erm ute the ro ws of t
/
and t
/
resp ectiv ely/;
see Example /3/./1/0/)/. Then S
/
d /= d S
/
/, d /2 D
/
and d
/? /1
/2 D
/
/; so m
/
T
d
/= T
d
m
/
b y
Prop osition /3/./3/. Consequen tly /, m
/
/= T
/? /1
d
m
/
T
d
can b e written as a linear com bi/-
nation of terms m
uv
where u and v are ro w standard / /{tableaux b y Corollary /3/./4
and its left/{handed analogue/. The general case follo ws from this and Corollary /3/./4
since m
st
/= T
/
d /( s /)
m
/
T
d /( t /)
/= T
/
d /( s /)
T
/
d
m
/
T
d
T
d /( t /)
/.
/3/./1/0 Example Supp ose that / /= /(/2 /; /1 /; /3 /; /3/)/. Then/, using the notation of Lemma /3/./9/,
/ /= /(/3 /; /3 /; /2 /; /1/) and
t
/
/=
/1 /2
/3
/4 /5 /6
/7 /8 /9
and t
/
/=
/1 /2 /3
/4 /5 /6
/7 /8
/9
/:
Th us w e ma y tak e d /= /(/1 /; /4 /; /7/)/(/2 /; /5 /; /8/)/(/3 /; /6 /; /9/)/, in whic h case
t
/
d
/? /1
/=
/7 /8
/9
/1 /2 /3
/4 /5 /6
and t
/
d /=
/4 /5 /6
/7 /8 /9
/1 /2
/3
/:
Note/, ho w ev er/, that d is not unique/; w e could also let d /= /(/1 /; /7/)/(/2 /; /8/)/(/3 /; /9/)/, then
t
/
d
/? /1
/=
/7 /8
/9
/4 /5 /6
/1 /2 /3
and t
/
d /=
/7 /8 /9
/4 /5 /6
/1 /2
/3
are again ro w standard/. Ho w ev er/, for b oth c hoices of d w e ha v e S
/
/= d S
/
d
/? /1
/.
Let / b e a partition and supp ose that s and t are ro w standard / /{tableaux/. W e
need to sho w that m
st
can b e written as a linear com bination of terms m
uv
where
u and v are standard tableaux of the same shap e/. W e b egin with a sp ecial case/.
Supp ose that /( i/; j /) /2 /[ / /] where /
i /+/1
/ j and let a /= t
/
/( i/; j /) and b /= t
/
/( i /+ /1 /; j /)/.
The /( i/; j /)th Ga rnir tableau of shap e / is the ro w standard / /{tableau g /= g
ij
in whic h
all n um b ers less than a or greater than b o ccup y the same p ositions in t
/
and g /,
and where the n um b ers a/; a /+ /1 /; /: /: /: /; b are inserted in increasing order from left to
righ t/, /rst along ro w i /+ /1 and then along ro w i /, in to the remaining p ositions/.
/3/./1/1 Example Let / /= /(/3 /; /3/) then g
/1/1
/=
/2 /3 /4
/1 /5 /6
/, g
/1/2
/=
/1 /4 /5
/2 /3 /6
and g
/1/3
/=
/1 /2 /6
/3 /4 /5
/. Let
g /= g
/1/1
and / /= /(/4 /; /2/)/. In this case/, the pro of of the Lemma /3/./1/2 b elo w reduces to
the /(easily v eri/ed/) coset iden tit y
/2 /3 /4
/1 /5 /6
/+
/1 /3 /4
/2 /5 /6
/+
/1 /2 /4
/3 /5 /6
/+
/1 /2 /3
/4 /5 /6
/=
/1 /2 /3 /6
/4 /5
/+
/1 /2 /3 /5
/4 /6
/+
/1 /2 /3 /4
/5 /6
where/, for this example/, a tableau t on the left hand side is iden ti/ed with m
/
T
d /( t /)
and a tableau v on the righ t hand side is iden ti/ed with T
/
d /( v /)
m
/
/.
F or the next few Lemmas w e need another ordering on the set of partitions/.
Giv en partitions / and / w e write / /> / if / is greater than / in the lexicographic
o rdering /. That is/, there exists an in teger j / /1 suc h that /
i
/= /
i
for /1 / i /< j and
/
j
/> /
j
/. Similarl y w e write / / / if either / /= / or / /> / /. Note that if / B /
then / /> / /.
/2/2 /3/. THE MODULAR REPRESENT A TION THEOR Y OF H
/3/./1/2 Lemma L et / b e a p artition of n and supp ose that g is a Garnir table au/.
Then ther e exists a p artition / of n such that / /> / and
m
t
/
g
/= h /?
X
/ /2 Std/( / /)
/ B g
m
t
/
/
wher e h is a line ar c ombination of terms m
uv
such that u and v ar e r ow standar d
/ /{table aux/.
Pro of/. W rite / /= /( /
/1
/; /: /: /: /; /
k
/) and supp ose that g /= g
ij
is the /( i/; j /)th Garnir
tableau/. Set / /= /( /
/1
/; /: /: /: /; /
i /? /1
/; j /? /1 /; /
i
/+ /1 /; /
i /+/1
/? j/; /
i /+/2
/; /: /: /: /; /
k
/)/, a comp osition
of n /, and let X /= f v w j v /2 S
/
and w /2 S
/
g /. Then/, b y Prop osition /3/./3/,
X
w /2 S
/
/\ D
/
m
/
T
w
/=
X
x /2 X
T
x
/=
X
v /2 S
/
/\ D
/
T
/
v
m
/
/( cf/. Example /3/./1/1/)/. No w f t
/
w j w /2 S
/
/\ D
/
g /= f g g /[ f / /2 Std/( / /) j / B g g /, so
rearranging this equation w e obtain
m
t
/
g
/=
X
d /( v /) /2 S
/
/\ D
/
m
vt
/
/?
X
/ /2 Std/( / /)
/ B g
m
t
/
/
/:
In order to complete the pro of w e need to sho w that h /=
P
v
m
vt
/
has the required
form/. Let / b e the partition obtained from / b y reordering its parts/. Then / /> /
so the result follo ws from Lemma /3/./9/.
/3/./1/3 Lemma Supp ose that t is a r ow standar d / /{table au which is not standar d/.
Then ther e exists a Garnir table au g and w /2 S
n
such that t /= g w and /` /( d /( t /)/) /=
/` /( d /( g /)/) /+ /` /( w /) /.
Pro of/. Because t is not standard there exists a no de /( i/; j /) in /[ / /] suc h that t /( i/; j /) />
t /( i /+ /1 /; j /)/. If t is the /( i/; j /)th Garnir tableau w e ma y tak e w /= /1 and there is nothing
to pro v e/; otherwise/, there exists an s /2 S suc h that t
/0
/= t s is ro w standard/,
t
/0
/( i/; j /) /> t
/0
/( i /+ /1 /; j /) and t
/0
B t /. Let g b e the /( i/; j /)th Garnir tableau/; b y induction
w e ma y assume that there exists a p erm utation w
/0
/2 S
n
suc h that t
/0
/= g w
/0
and
/` /( d /( t
/0
/)/) /= /` /( d /( g /)/) /+ /` /( w
/0
/)/. Therefore/, if w e set w /= w
/0
s then t /= g w and
/` /( d /( t /)/) /= /` /( d /( t
/0
/)/) /+ /1 /= /` /( d /( g /)/) /+ /` /( w
/0
/) /+ /1 /= /` /( d /( g /)/) /+ /` /( w /)
as required/.
/3/./1/4 Lemma L et / b e a p artition of n and supp ose that s and t ar e r ow standar d
/ /{table aux/. Then m
st
c an b e written as a line ar c ombination of elements m
uv
wher e
u and v ar e standar d / /{table au for some p artition / of n such that either /(i/) / /> / /,
or /(ii/) / /= / and u D s and v D t /.
Pro of/. First supp ose that t is ro w standard but not standard/. By Lemma /3/./1/3/,
m
st
/= m
sg
T
w
for some Garnir tableau g and some w /2 S
n
/. Consequen tly /, b y
Lemma /3/./1/2 there exists an elemen t h /=
P
r
uv
m
uv
/, where u and v are ro w standard
/ /{tableaux with / /> / /, suc h that
m
st
/= T
/
d /( s /)
m
t
/
g
T
w
/= T
/
d /( s /)
/
h /?
X
/ B g
m
t
/
/
/
T
w
/= T
/
d /( s /)
hT
w
/?
X
v B t
r
v
m
sv
/;
/2/. THE MURPHY BASIS /2/3
for some r
v
/2 R and where the last equalit y uses Corollary /3/./8/. By Corollary /3/./4
and induction on / /, T
/
d /( s /)
hT
w
can b e written in the required form/. F urthermore/, b y
induction on t /, the terms m
sv
can b e written as a linear com bination of terms m
uv
/0
where u and v
/0
are / /{tableaux suc h that / D / and u is ro w standard and v
/0
is
standard/. Since m
uv
/0
/= m
/
v
/0
u
w e can rep eat the argumen t to replace the left hand
tableaux with standard tableaux of the required form/, and so deduce the result/.
W e will often need an imp ortan t sp ecial case of Lemma /3/./1/4 whic h can b e
gleaned from a careful scrutin y of its pro of/.
/3/./1/5 Corollary Supp ose that t is a standar d / /{table au such that i and i /+ /1 ar e
in the same c olumn of t for some i /. Then/, for any standar d / /{table au s /,
m
st
T
i
/= /? m
st
/+
X
r
uv
m
uv
wher e r
uv
/2 R and the sum is over p airs /( u /; v /) of r ow standar d / /{table au such that
either /(i/) / /> / /, or /(ii/) / /= / /, u /= s and v B t /.
Pro of/. By assumption/, t s
i
is not standard so w e ma y write t s
i
/= g w for some
Garnir tableau g and w /2 S
n
b y Lemma /3/./1/3/. No w/, there is a unique standard
tableau / suc h that g /= / s for some s /2 S /; moreo v er/, /` /( d /( g /)/) /= /` /( d /( / /)/) /+ /1 and
if v is an y /(standard/) tableau with v B g then v D / /. Consequen tly /, in this case
Lemma /3/./1/2 sa ys that
m
sg
/= /? m
s /
/+
X
r
uv
m
uv
where r
uv
/2 R and the sum is o v er pairs /( u /; v /) of standard / /{tableau suc h that either
/(i/) / /> / /, or /(ii/) / /= / /, u /= s and v B / /. Finally /, b ecause /` /( d /( t /)/) /= /` /( d /( / /)/) /+ /` /( w /)
and t /= / w /, b y m ultiplying the equation w e ha v e obtained for m
sg
on the righ t b y
T
w
and using Corollary /3/./8 w e obtain the result/.
Let M /= f m
st
j s /; t /2 Std/( / /) for some partition / of n g /: Then Lemma /3/./9
and Lemma /3/./1/4 sho w that M spans H /. By Theorem /1/./1/1 w e kno w that H is a
free R /{mo dule of rank n /!/. Ho w ev er/, jMj /=
P
/
j Std/( / /) j
/2
and it is w ell/{kno wn that
this sum is equal to n /! /(for example/, use the Robinson/{Sc hensted corresp ondence/;
see /[ /4/7 /]/)/. Th us/, M is a basis of H /. W e call M the Murphy basis of H /.
If w e let /
lex
b e the set of partitions of n ordered lexicographically w e ha v e
sho wn that /( M /; /
lex
/) is a cellular basis of H /. In order to pro v e the stronger
result that the set of partitions can b e ordered b y dominance w e need the follo wing
imp ortan t Prop osition/.
If h /2 H w e ma y write h /=
P
r
st
m
st
where r
st
/2 R and m
st
/2 M /. W e sa y
that m
st
is involved in h if r
st
/6/= /0/. Recall that H
Z
/= H
Z /; /^q
where Z /= Z /[ /^ q /; /^q
/? /1
/]/.
/3/./1/6 Prop ositi on L et i b e an inte ger with /1 / i /< n and supp ose that h /2 M
/
wher e / is the c omp osition of n such that m
/
/= /(/1 /+ T
i
/) /. Supp ose that h /=
P
r
st
m
st
/,
wher e r
st
/2 R and m
st
/2 M /. Then r
st
/= /0 whenever i and i /+ /1 b elong to the same
c olumn of s /.
Pro of/. First supp ose that H /= H
Z
and write M
/
Z
/= m
/
H
Z
/. Let / b e minim al
in the lexicographic order suc h that m
uv
is in v olv ed in h for some / /{tableaux u
and v /. Cho ose a pair /( u /; v /) of standard / /{tableaux suc h that /(i/) m
uv
is in v olv ed
in h /, and /(ii/) whenev er /( s /; t /) is another pair of standard / /{tableaux suc h that u D s
and v D t then m
st
is not in v olv ed in h /.
/2/4 /3/. THE MODULAR REPRESENT A TION THEOR Y OF H
Supp ose that i and i /+ /1 are in the same column of u /. Then/, b y Corollary /3/./1/5
and our c hoice of /( u /; v /)/,
T
i
h /= /( h
/
T
i
/)
/
/= /? r
uv
m
uv
/+
X
a
st
m
st
for some a
st
/2 R suc h that whenev er u D s and v D t then a
st
/= /0/. Ho w ev er/,
T
i
m
/
/= /^ q m
/
b y Lemma /3/./2/, so T
i
h /= /^ q h and this forces r
uv
/= /0/, a con tradiction/.
Consequen tly /, i and i /+ /1 do not b elong to the same column of u /.
Next let u
/0
/= u /( i/; i /+ /1/)/. If u
/0
B u then T
i
m
uv
/= m
u
/0
v
so m
u
/0
v
is in v olv ed in h
since /^q
/? /1
T
i
h /= h /; ho w ev er/, this con tradicts our assumption /(ii/) so/, in fact/, u B u
/0
/.
Therefore/, m
uv
/+ m
u
/0
v
/= m
/
m
uv
is an elemen t of M
/
Z
and h
/0
/= h /? r
uv
/( m
uv
/+ m
u
/0
v
/)
is an elemen t of M
/
Z
whic h do es not in v olv e m
uv
/. Applying the same argumen t to h
/0
it follo ws that i and i /+ /1 are nev er in the same column of s if m
st
is in v olv ed in h /.
This completes the pro of when H /= H
Z
/.
No w supp ose that R is an arbitrary ring/. By Corollary /3/./4/, f m
/
T
d
j d /2 D
/
g
is a basis of M
/
/. By what w e ha v e sho wn/, inside H
Z
w e can write eac h ro w
standard basis elemen t m
/
T
d
as a Z /{linear com bination of Murph y basis elemen ts
of the required form/. The sp ecialization homom orphism from H
Z
to H maps the
Murph y basis of H
Z
to the Murph y basis of H /. It also maps the ro w standard
basis of M
/
Z
to that of M
/
/. Hence/, in H eac h basis elemen t m
/
T
d
can b e written
as an R /{linear com bination of Murph y basis elemen ts of the required form/.
As in the last c hapter/, w e de/ne H
/
to b e the R /{mo dule with basis
n
m
uv
/
/
/
u /; v /2 Std/( / /) for some partition
/ of n suc h that / D /
o
/:
Similarly /, w e de/ne
/
H
/
to b e the R /{mo dule with basis m
st
where s and t are
standard / /{tableaux and / B / /.
/3/./1/7 Corollary Supp ose that / is a p artition/. Then
/
H
/
and H
/
ar e two/{side d
ide als of H /.
Pro of/. Let s and t b e standard / /{tableaux and w /2 S
n
/. Because
/
H
/
/=
P
/ B /
H
/
/, it is enough to sho w that m
st
T
w
/2 H
/
/. W e pro v e this b y induction
on / /, the case / /= /( n /) b eing a consequence of Lemma /3/./2/.
First note that b y Lemma /3/./1/4 there exist r
uv
/2 R suc h that m
t
/
t
T
w
/=
P
r
uv
m
uv
where the sum is o v er pairs /( u /; v /) of standard / /{tableaux with / / / /.
Supp ose that r
uv
/6/= /0 for some / /{tableaux u and v /. By Prop osition /3/./1/6/, if i and
i /+ /1 are in the same ro w of t
/
then they cannot b e in the same column of u /. It
follo ws that /1 /; /2 /: /: /: /; /
/1
m ust all b e in the /rst ro w of u /; so /
/1
/ /
/1
/. Consideration
of the second ro w sho ws that /
/1
/+ /
/2
/ /
/1
/+ /
/2
/, and so on/. Hence/, / D / whenev er
r
uv
/6/= /0/.
Because m
st
/= T
/
d /( s /)
m
t
/
t
/, the general case follo ws b y induction on / using the
left handed v ersion of Lemma /3/./1/4/, together with Corollary /3/./4/.
W e can no w pro v e the main result of this section/. Let / b e the set of partitions
of n ordered b y dominance/. Recall that / /: H /? /! H is the unique R /{linear an ti/{
isomorphism of H suc h that T
/
w
/= T
w
/? /1
for all w /2 S
n
/.
/2/. THE MURPHY BASIS /2/5
/3/./1/8 The Murph y Basis Theorem /(Murph y/) The He cke algebr a H is a fr e e
R /{mo dule with b asis
M /=
n
m
st
/
/
/
s /; t /2 Std /( / /) for some p artition / of n
o
/:
Mor e over/,
/(i/) m
/
st
/= m
ts
for al l / /2 / and al l s /; t /2 Std /( / /) /.
/(ii/) Supp ose that h /2 H and that t /2 Std/( / /) /. Then ther e exist r
v
/2 R such that
for al l s /2 Std/( / /)
m
st
h /
X
v /2 Std /( / /)
r
v
m
sv
mo d
/
H
/
/:
Conse quently/, /( M /; //) is a c el lular b asis of H /.
Pro of/. W e ha v e already seen that M is a basis of H and/, from the de/nitions/,
it is immediate that m
/
st
/= m
ts
/. Hence/, it remains to pro v e /(ii/)/.
Let N
/
b e the R /{mo dule spanned b y
/
H
/
and f m
t
/
t
j t /2 Std /( / /) g /. The ar/-
gumen t of Corollary /3/./1/7 sho ws that N
/
is a righ t ideal of H /. Therefore/, for an y
standard tableau t /2 Std /( / /) and h /2 H there exists r
v
/2 R suc h that
m
t
/
t
h /
X
v /2 Std /( / /)
r
v
m
t
/
v
mo d
/
H
/
/:
Multiplying this expression on the left b y T
/
d /( s /)
pro v es /(ii/) and hence the Theorem/.
F or future use/, w e note the follo wing strengthening of Corollary /3/./1/5/.
/3/./1/9 Corollary Supp ose s and t ar e standar d / /{table au such that i and i /+ /1 ar e
in the same c olumn of t for some i /. Then/, for al l s /2 Std/( / /) /,
m
st
T
i
/ /? m
st
/+
X
v B t
r
v
m
sv
mo d
/
A
/
/:
for some r
v
/2 R /.
W e can no w use the theory of cellular algebras from Chapter /2 to construct all
of the irreducible H /{mo dules/. The cell mo dules of H are called Sp ec h t mo dules/.
Let / b e a partition of n /. Rather than the abstract de/nition of Chapter /2
w e de/ne the Sp echt mo dule S
/
to b e the righ t H /{mo dule /(
/
H
/
/+ m
/
/) H /. Note
that
/
H
/
/+ m
/
is an elemen t of the H /{mo dule H /=
/
H
/
so that S
/
is a submo dule
of H /=
/
H
/
/.
W arning The Sp ec h t mo dule S
/
/, as w e ha v e de/ned it/, is isomorphic to the dual
of the Sp ec h t mo dule whic h Dipp er/{James /[ /1/3 /] index b y /
/0
/, the partition whic h is
conjugate to / /. Because of this/, when comparing the results in these notes with
those from the represen tation theory of the symmetric groups /( q /= /1/)/, or with the
pap ers of Dipp er and James/, the Sp ec h t mo dule S
/
m ust b e replaced with S
/
/0
/
/. In
the literature our Sp ec h t mo dules are sometimes called dual Sp ec h t mo dules/.
Giv en a standard / /{tableau t let m
t
/=
/
H
/
/+ m
t
/
t
/. Then Theorem /3/./1/8 giv es
us the follo wing basis of S
/
/(and sho ws that S
/
is isomorphic to the cell mo dule as
de/ned in Chapter /2/)/.
/3/./2/0 Prop ositi on Supp ose that / is a p artition of n /. Then the Sp e cht mo dule S
/
is a fr e e R /{mo dule with b asis f m
t
j t /2 Std/( / /) g /.
/2/6 /3/. THE MODULAR REPRESENT A TION THEOR Y OF H
W e call the basis of Prop osition /3/./2/0 the Murphy basis of S
/
/. T ranslating the
notation from /(/2/./6/)/, the bilinear form h /; i on S
/
is the unique R /{bilinear map
from S
/
/ S
/
in to R suc h that
h m
s
/; m
t
i m
/
/ m
t
/
s
m
tt
/ mo d H
/
/:
for all standard / /{tableaux s and t /. By Prop osition /2/./7/, this form is asso ciativ e and
symmetric so rad S
/
/= f x /2 S
/
j h x/; y i /= /0 for all y /2 S
/
g is an H /-submo dule
of S
/
/. As in /(/2/./8/)/, for eac h partition / of n w e de/ne D
/
to b e the righ t H /{
mo dule S
/
/= rad S
/
/. Th us b y Theorem /2/./1/3 w e ha v e the follo wing result/.
/3/./2/1 Theorem /(Dipp er/{James/) Supp ose that R is a /eld/. Then
f D
/
j / a p artition of n such that D
/
/6/= /0 g
is a c omplete set of non/{isomorphic irr e ducible H /{mo dules/.
W e will classify the partitions / suc h that D
/
/6/= /0 in Section /4/. F or no w w e
note that b y Corollary /2/./1/8 and Corollary /1/./1/5 w e ha v e the follo wing/.
Recall that H
K
/= H
C /( /^ q /) /; /^q
/( S
n
/)/.
/3/./2/2 Corollary /(Ho efsmit/) The Iwahori/{He cke algebr a H
K
is a split semisim/-
ple algebr a and f S
/
j / a p artition of n g is a c omplete set of non/{isomorphic irr e/-
ducible H
K
/{mo dules/.
In particular/, this sho ws that H
K
and K S
n
are isomorphic as K /{algebras/.
/3/. Sp ec h t mo dules and Jucys/{Murph y elemen ts
In this section w e study the action of the follo wing op erators up on the Sp ec h t
mo dules and use them to construct an orthogonal basis for S
/
/. F or k /= /1 /; /2 /; /: /: /: /; n
let
L
k
/= q
/? /1
T
/( k /? /1 /;k /)
/+ q
/? /2
L
/( k /? /2 /;k /)
/+ / / / /+ q
/1 /? k
T
/(/1 /;k /)
/:
The elemen ts L
/1
/; /: /: /: /; L
n
are the Jucys/{Murphy elements of H /.
/3/./2/3 Example If n /= /4 then the four Jucys/{Murph y elemen ts are L
/1
/= /0/, L
/2
/=
q
/? /1
T
/(/1 /; /2/)
/, L
/3
/= q
/? /1
T
/(/2 /; /3/)
/+ q
/? /2
T
/(/1 /; /3/)
/, and L
/4
/= q
/? /1
T
/(/3 /; /4/)
/+ q
/? /2
T
/(/2 /; /4/)
/+ q
/? /3
T
/(/1 /; /4/)
/.
/3/./2/4 Prop ositi on L et i and k b e inte gers with /1 / i /< n and /1 / k / n /.
/(i/) T
i
and L
k
c ommute if i /6/= k /? /1 /; k /.
/(ii/) T
i
L
i /+/1
/= /( q /? /1/) L
i /+/1
/+ /1 /+ L
i
T
i
and T
i
L
i
/= T
i
L
i /+/1
/? /1 /? /( q /? /1/) L
i /+/1
/.
/(iii/) T
i
c ommutes with L
i
L
i /+/1
and L
i
/+ L
i /+/1
/.
/(iv/) L
i
and L
k
c ommute/.
Pro of/. The pro ofs of all of these statemen ts follo w easily using the relations in
H /, so w e pro v e only /(i/)/. Because L
/1
/= /0 there is nothing to pro v e when k /= /1/, so
assume that k /> /1/. Then/, b y de/nition/, L
k
/= q
/? /1
/( T
k
/+ T
k
L
k /? /1
T
k
/)/, so if j i /? k j /> /1
then T
i
L
k
/= q
/? /1
/( T
i
T
k
/+ T
i
T
k
L
k /? /1
T
k
/) /= q
/? /1
/( T
k
T
i
/+ T
k
T
i
L
k /? /1
T
k
/)/; so T
i
L
k
/= L
k
T
i
b y induction/. Finally /, it remains to consider the case when i /= k /+ /1/; ho w ev er/, this
is easy b ecause T
k /+/1
comm utes with T
/( j/;k /)
for j /= /1 /; /: /: /: /; k /.
/3/./2/5 Corollary A ny symmetric p olynomial in L
/1
/; /: /: /: /; L
n
b elongs to the c entr e
of H /.
The Corollary indicates wh y the Jucys/{Murph y elemen ts are so useful/. The idea
is that L
/1
/; /: /: /: /; L
n
generate a large ab elian subalgebra of H /| whic h is kno wn to
b e maxim al when H is semisimple /| and consequen tly these elemen ts can b e used
/3/. SPECHT MODULES AND JUCYS/{MURPHY ELEMENTS /2/7
to distinguish b et w een the blo c ks and irreducible represen tations of H /, m uc h lik e
the Cartan subalgebra of a Lie algebra/.
In the Lemma b elo w w e write S
/
R
to indicate that the Sp ec h t mo dule is de/ned
o v er R /. Recall that K /= C /( /^ q /) and Z /= Z /[ /^ q /; /^q
/? /1
/]/.
/3/./2/6 Lemma L et / b e a p artition of n /. Then ther e exists / /2 R such that
m
t
/( L
/1
/+ / / / /+ L
n
/) /= /m
t
for al l standar d / /{table au t /.
Pro of/. First supp ose that H /= H
K
/. By Corollary /3/./2/5/, the symmetric p oly/-
nomial L
/1
/+ / / / /+ L
n
is cen tral in H and S
/
K
is an irreducible H
K
/{mo dule b y
Corollary /3/./2/2/. Therefore/, b y Sc h ur/'s Lemma L
/1
/+ / / / /+ L
n
acts as a scalar/, sa y /^/ /,
on S
/
K
/. In particular/, if t is a standard / /{tableau then m
t
/( L
/1
/+ / / / /+ L
n
/) /= /^ /m
t
/. By
Corollary /3/./4 the left hand side of this equation is con tained in H
Z
/; consequen tly /,
/^/ /2 Z /.
No w supp ose that R is an arbitrary ring/. Then/, as in Corollary /1/./1/2/, w e can
consider R as a Z /{mo dule b y sp ecifying that /^q acts as m ultiplicatio n b y q on R /.
Then S
/
R
/
/=
S
/
Z
/
 R as R /{mo dules and the Murph y basis of S
/
Z
is mapp ed to the
Murph y basis of S
/
R
b y the sp ecialization homom orphism /. It follo ws that if /^/ acts
on R as m ultiplication b y / /2 R then m
t
/( L
/1
/+ /: /: /: /+ L
n
/) /= /m
t
for all t /2 Std/( / /)/.
The precise v alue of / can b e computed from Theorem /3/./3/0 b elo w/; the next
Lemma is the inductiv e step in pro ving this result/.
/3/./2/7 Lemma L et / b e a p artition of n and let s and t b e standar d / /{table aux such
that s B t and t /= s /( i/; i /+ /1/) for some i with /1 / i /< n /. F or k /= /1 /; /2 /; /: /: /: /; n /, supp ose
that ther e exist r
s
/( k /) /2 R such that
m
s
L
k
/= r
s
/( k /) m
s
/+
X
v /2 Std /( / /)
v B s
a
v
m
v
for some a
v
/2 R /. Then/, for k /= /1 /; /2 /; /: /: /: /; n /, ther e exist b
v
/2 R such that
m
t
L
k
/= r
t
/( k /) m
t
/+
X
v /2 Std /( / /)
v B t
b
v
m
v
wher e r
t
/( k /) /= r
s
/( k /) if k /6/= i/; i /+ /1 /, r
t
/( i /) /= r
s
/( i /+ /1/) and r
t
/( i /+ /1/) /= r
s
/( i /) /.
Pro of/. First w e note that m
t
/= m
s
T
i
b y Theorem /1/./1/1 b ecause s B t /. Therefore/,
b y Prop osition /3/./2/4/(i/)/, if k /6/= i/; i /+ /1 then
m
t
L
k
/= m
s
T
i
L
k
/= m
s
L
k
T
i
/= r
s
/( k /) m
s
T
i
/+
X
v /2 Std /( / /)
v B s
a
v
m
v
T
i
/;
and the result follo ws b y Corollary /3/./8/. If k /= i /+ /1 then/, using Prop osition /3/./2/4/(ii/)
and Corollary /3/./8/,
m
t
L
i /+/1
/= m
s
T
i
L
i /+/1
/= m
s
/
L
i
T
i
/+ /1 /+ /( q /? /1/) L
i /+/1
/	
/= r
s
/( i /) m
s
T
i
/+
/
/1 /+ /( q /? /1/) r
s
/( i /+ /1/)
/	
m
s
/+
X
v B s
b
v
m
v
/= r
s
/( i /) m
t
/+
X
v B t
b
v
m
v
/:
/2/8 /3/. THE MODULAR REPRESENT A TION THEOR Y OF H
The case k /= i is similar/.
Giv en an in teger m let /[ m /]
q
/= /1 /+ q /+ / / / /+ q
m /? /1
if m / /0 and /[ /? m /]
q
/=
/? q
/? m
/[ m /]
q
otherwise/; then /[ m /]
q
/=
q
m
/? /1
q /? /1
when q /6/= /1/. If m / /0 w e also de/ne
/[ m /]
/!
q
/= /[/1/]
q
/[/2/]
q
/: /: /: /[ m /]
q
/. These are the so/{called quan tum in tegers and quan tum
factorials resp ectiv ely/; this is b ecause /[ m /]
/1
/= m and /[ m /]
/!
/1
/= m /! for all m /2 Z /.
/3/./2/8 De/ne e to b e the smallest p ositiv e in teger suc h that /[ e /]
q
/= /0/; set e /= /1 if no
suc h in teger exists/. In other w ords/, either q /= /1 and e is equal to the c haracteristic
of R /, or q is a primitiv e e th ro ot of unit y /. As w e shall see/, the in teger e b eha v es
v ery m uc h lik e the c haracteristic of the /eld in the represen tation theory of /nite
groups/.
Supp ose that x /= /( i/; j /) is a no de in /[ / /]/. The e /{residue of x is the in teger
res /( x /) /= j /? i mo d e /. If t is a / /{tableau and k an in teger with /1 / k / n then the
e /{residue of k in t is res
t
/( k /) /= res /( x /) where x is the unique no de in /[ / /] suc h that
t /( x /) /= k /.
/3/./2/9 Example Supp ose that e /= /3/, / /= /(/4 /; /2/) and t /=
/1 /3 /4 /6
/2 /5
/. Then the e /{
residues in /[ / /] are
/0 /1 /2 /0
/2 /0
/. So/, for example/, /[res
t
/(/3/)/]
q
/= /[/1/]
q
and /[res
t
/(/4/)/]
q
/= /[/4/]
q
/.
/3/./3/0 Theorem /(Dipp er/{James/) Supp ose that / is a p artition of n and let t b e
a standar d / /{table au/. L et k b e any inte ger such that /1 / k / n /. Then ther e exist
a
v
/2 R such that
m
t
L
k
/= /[res
t
/( k /)/]
q
m
t
/+
X
v /2 Std /( / /)
v B t
a
v
m
v
/:
Pro of/. By Lemma /3/./2/7 it is su/cien t to sho w that m
t
/ L
k
/= /[res
t
/ /( k /)/]
q
m
t
/ for
k /= /1 /; /2 /; /: /: /: /; n /. When n /= /1 there is nothing to pro v e so b y induction w e can
assume that the Theorem is kno wn for smaller v alues of n /. W e no w pro ceed b y
induction on k /, the case k /= /1 b eing trivial b ecause L
/1
/= /0 and /[res
t
/(/1/)/]
q
/= /[/0/]
q
/= /0/.
Supp ose /rst that k is in ro w r of t
/
where /
r /+/1
/6/= /0/. Let / /= /( /
/1
/; /: /: /: /; /
r
/)/.
Then j / j /< n and m
t
/ /= H
/
/+ m
/
h / m
/
h /, where h is some elemen t of the
subalgebra of H generated b y T
k /+/1
/; /: /: /: /; T
n /? /1
/. Consequen tly /, m
/
L
k
/2 H /( S
j / j
/)
and h and L
k
comm ute b y Prop osition /3/./2/4/(i/)/. Hence/, w orking mo dulo H
/
and
arguing b y induction on n /,
m
t
/
L
k
/ m
/
hL
k
/= m
/
L
k
h / /[res
t
/
/( k /)/]
q
m
/
h / /[res
t
/
/( k /)/]
q
m
t
/
/:
Th us w e ma y assume that k is in the last ro w of t
/
/.
Next/, supp ose that k is not in the /rst column of t
/
i and that w e kno w the result
for smaller k /. No w s
k /? /1
is an elemen t of S
/
so m
/
T
k /? /1
/= q m
/
b y Lemma /3/./2/; so/,
m
t
/ L
k
/= q
/? /1
m
t
/ /( T
k /? /1
L
k /? /1
T
k /? /1
/+ T
k /? /1
/) /= m
t
/ /(/1 /+ L
k /? /1
T
k /? /1
/)
/= /(/1 /+ q /[res
t
/ /( k /? /1/)/]
q
/) m
t
/ /= /[res
t
/ /( k /)/]
q
m
t
/
b y induction on k /.
This reduces us to the case where k is the n um b er in the last ro w and the /rst
column of t
/
/. W rite / /= /( /
/1
/; /: /: /: /; /
r /+/1
/) where /
r /+/1
/> /0/. Then m
/
/= hm
/( /
/1
/;/:/:/: /;/
r
/; /1/)
for some h /2 H /( S
n
/) and m
/( /
/1
/;/:/:/: /;/
r
/; /1/)
/2 H /( S
k
/)/. Therefore/, if k /< n w e can again
deduce the result b y induction/. Finally then/, it remains then to consider the case
where k /= n and / /= /( /
/1
/; /: /: /: /
r
/; /1/)/.
/3/. SPECHT MODULES AND JUCYS/{MURPHY ELEMENTS /2/9
Let i b e the /rst n um b er in ro w r of t
/
and let t b e the standard / /{tableau
t
/
s
n /? /1
/: /: /: s
i /+/1
/. Then the second last ro w of t con tains the n um b ers i/; i /+ /2 /; /: /: /: /; n
and the last ro w of t consists of the single en try i /+ /1/.
So far w e ha v e sho wn that m
t
/ L
k
/= /[res
t
/ /( k /)/]
q
m
t
/ for /1 / k /< n /. W e also
kno w that m
t
/ /( L
/1
/+ / / / /+ L
n
/) /= /m
t
/ for some / /2 R b y Lemma /3/./2/6/; consequen tly /,
m
t
/ L
n
/= r
n
m
t
/ for some r
n
/2 R /. Therefore/, m
t
L
i
/= /[res
t
/ /( i /)/]
q
m
t
/+
P
s B t
a
s
m
s
and m
t
L
i /+/1
/= r
n
m
t
/+
P
s B t
b
s
m
s
b y Lemma /3/./2/7/.
The k ey p oin t no w is that t s
i
is a Garnir tableau/; b ecause of this w e can /nd
elemen ts c
s
in R suc h that m
t
T
i
/= /? m
t
/+
P
s B t
c
s
m
s
b y Corollary /3/./1/9/. This allo ws
us to compute m
t
L
i /+/1
in another w a y/; namely /, b y Corollary /3/./8 and Lemma /3/./1/2
there exist a
/0
s
and d
s
/2 R /, resp ectiv ely /, suc h that
m
t
L
i /+/1
/= q
/? /1
m
t
/( T
i
L
i
T
i
/+ T
i
/)
/= /? q
/? /1
n
m
t
/+
X
s B t
c
s
m
s
o
/( L
i
T
i
/+ /1/)
/= /? q
/? /1
m
t
/(/[res
t
/ /( i /)/]
q
T
i
/+ /1/) /+
X
s B t
a
/0
s
m
s
T
i
/= q
/? /1
/(/[res
t
/ /( i /)/]
q
/? /1/) m
t
/+
X
s B t
d
s
m
s
/= /[res
t
/ /( n /)/]
q
m
t
/+
X
s B t
d
s
m
s
/:
Consequen tly /, r
n
/= /[res
t
/( n /)/]
q
as required/.
/3/./3/1 F or the remainder of this section w e assume that R is a /eld and that e /> n
/(see /(/3/./2/8/)/)/. Let t b e a standard / /{tableau and de/ne
F
t
/=
n
Y
k /=/1
Y
s /2 Std /( / /)
/[res
s
/( k /)/]
q
/6/=/[res
t
/( k /)/]
q
L
k
/? /[res
s
/( k /)/]
q
/[res
t
/( k /)/]
q
/? /[res
s
/( k /)/]
q
and let f
t
/= m
t
F
t
/.
Note that all of the factors in F
t
comm ute so there is no need to sp ecify an
ordering in the pro duct/. In practice man y of the factors in the de/nition of f
t
are
redundan t/; ho w ev er/, the ab o v e de/nition is con v enien t/. The elemen ts F
t
are de/ned
whether or not e /< n /; it is the next Lemma where w e need this assumption/.
If / is a partition then a no de x /2 /[ / /] is removable if /[ / /] n f x g is the diagram of
a partition/.
/3/./3/2 Lemma Supp ose that R is a /eld/, e /> n and let / b e a p artition of n /. L et s
and t b e standar d / /{table aux/.
/(i/) Supp ose that /[res
s
/( k /)/]
q
/= /[res
t
/( k /)/]
q
for k /= /1 /; /: /: /: /; n /. Then s /= t /.
/(ii/) Supp ose that /[res
s
/( k /)/]
q
/= /[res
t
/( k /)/]
q
for /1 / k / n and k /6/= i/; i /+ /1 for some i /.
Then either s /= t or s /= t /( i/; i /+ /1/) /.
Pro of/. Note that b ecause e /> n the no des with the same e /{residue o ccur in
diagonal lines in the diagram of / /; consequen tly /, distinct remo v able no des ha v e
distinct e /{residues/. Therefore/, b y successiv ely remo ving n/; n /? /1 /; /: /: /: /; /1 from s w e
see that t is completely determined b y the sequence /[res
t
/(/1/)/]
q
/; /: /: /: /; /[res
t
/( n /)/]
q
/. Both
parts of the Lemma no w follo w/.
/3/0 /3/. THE MODULAR REPRESENT A TION THEOR Y OF H
/3/./3/3 Prop ositi on Supp ose that R is a /eld and that e /> n /. Supp ose that / is a
p artition of n and let t b e a standar d / /{table au/.
/(i/) Ther e exist a
s
/2 R such that f
t
/= m
t
/+
X
s B t
a
s
m
s
/.
/(ii/) If s B t then m
s
F
t
/= /0 /.
/(iii/) F or k /= /1 /; /: /: /: /; n /, f
t
L
k
/= /[res
t
/( k /)/]
q
f
t
/.
/(iv/) If s /2 Std /( / /) then f
t
F
s
/= /
st
f
t
/.
Pro of/. Let N /= j Std/( / /) j and for an y s /2 Std/( / /) let f
/0
s
/= m
s
F
N
s
/. W e will /rst
pro v e analogues of /(i/)/|/(iv/) for f
/0
s
and then sho w that f
s
/= f
/0
s
/.
W e kno w from Theorem /3/./3/0 that m
t
L
k
/= /[res
t
/( k /)/]
q
m
t
/+
P
s B t
b
s
m
s
/, for some
b
s
/2 R /. Therefore/, f
/0
t
/= m
t
/+
P
s B t
a
s
m
s
for some a
s
/2 R /. Call this statemen t /(i/)
/0
/.
Next supp ose that s is a standard / /{tableau suc h that s B t /. By Lemma /3/./3/2/(i/)
w e can /nd an in teger k suc h that /[res
t
/( k /)/]
q
/6/= /[res
s
/( k /)/]
q
/. Then
/?
L
k
/? /[res
s
/( k /)/]
q
/
is a factor of F
t
so m
s
F
t
/=
P
v B s
c
v
m
v
for some c
v
/2 R b y Theorem /3/./3/0/. No w if
c
v
/6/= /0 then v B t and/, as b efore/, w e can /nd k
/0
suc h that /[res
t
/( k
/0
/)/]
q
/6/= /[res
v
/( k
/0
/)/]
q
/;
therefore/, m
s
F
/2
t
/=
P
v
/0
c
/0
v
/0
m
/0
v
where c
/0
v
/0
/6/= /0 only if there exists v with v
/0
B v B t /.
Con tin uing in this w a y sho ws that m
s
F
N
t
/= /0 whenev er s B t /.
Next w e claim that /(iii/)
/0
holds/; that is/, f
/0
t
L
k
/= /[res
t
/( k /)/]
q
f
/0
t
for all k with
/1 / k / n /. This no w follo ws b ecause b y the last paragraph and Theorem /3/./3/0
f
/0
t
L
k
/= m
t
F
N
t
L
k
/= m
t
L
k
F
N
t
/=
/?
/[res
t
/( k /)/]
q
m
t
/+
X
s B t
b
s
m
s
/
F
N
t
/= /[res
t
/( k /)/]
q
f
/0
t
/:
Using /(iii/)
/0
and the de/nitions w e disco v er that f
/0
t
is /xed b y ev ery factor of F
t
/;
th us/, f
/0
t
F
t
/= f
/0
t
/. F urthermore/, if s /6/= t then b y Lemma /3/./3/2/(i/) there exists an in teger
k suc h that /[res
s
/( k /)/]
q
/6/= /[res
t
/( k /)/]
q
/. Ho w ev er/, /(iii/)
/0
sho ws that
/?
L
k
/? res
t
/( k /)
/
kills
f
/0
t
/; so f
/0
t
F
s
/= /0 b ecause
/?
L
k
/? res
t
/( k /)
/
is a factor of F
s
/. Therefore/, f
/0
t
F
s
/= /
st
f
/0
t
/;
call this statemen t /(iv/)
/0
/.
Finally w e can sho w that f
t
/= f
/0
t
/. Supp ose that s is a standard / /{tableau
suc h that s D t /; then b y /(i/)
/0
there exist d
v
/2 R suc h that m
s
/= f
/0
s
/+
P
v B s
d
v
f
/0
v
/.
Therefore/, using /(iv/)
/0
/,
m
s
F
t
/=
/?
f
/0
s
/+
X
v B s
d
v
f
/0
v
/
F
t
/= /
st
f
/0
t
/:
In particular/, f
t
/= m
t
F
t
/= f
/0
t
and w e ha v e pro v ed all that w e set out to pro v e /(note
that the previous line includes /(ii/)/)/.
W e can no w pro v e the q /{analogue of Y oung/'s seminormal form for H /.
/3/./3/4 Theorem /(Dipp er/{James/) Supp ose that R is a /eld and that e /> n /. L et
/ b e a p artition of n /.
/(i/) f f
t
j t /2 Std/( / /) g is an ortho gonal b asis of S
/
/.
/(ii/) L et s b e a standar d / /{table au/, t /= s /( i/; i /+ /1/) and / /= res
s
/( i /) /? res
t
/( i /) /. Then
f
s
T
i
/=
/8
/>
/>
/>
/>
/>
/<
/>
/>
/>
/>
/>
/:
q f
s
/; if i and i /+ /1 ar e in the same r ow of s /,
/? f
s
/; if i and i /+ /1 ar e in the same c olumn of s /.
/?
/1
/[ / /]
q
f
s
/+ f
t
/; if t /2 Std/( / /) and s B t /,
q
/
/[ / /]
q
f
s
/+
/[ / /+/1/]
q
/[ / /? /1/]
q
/[ / /]
/2
q
f
t
/; if t /2 Std/( / /) and t B s /.
/4/. THE IRREDUCIBLE H /{MODULES /3/1
Pro of/. /(i/) By Prop osition /3/./3/3/(i/) the transition matrix b et w een the standard basis
of S
/
and f f
t
j t /2 Std/( / /) g is unitriangular so this set is a basis of S
/
/. Moreo v er/,
if s and t are standard / /{tableaux then
h f
s
/; f
t
i /= h f
s
F
s
/; f
t
i /= h f
s
/; f
t
F
/
s
i /= h f
s
/; f
t
F
s
i /= /
st
h f
s
/; f
s
i
b y Prop osition /2/./7/(ii/) and Prop osition /3/./3/3/(iv/)/. Th us/, f f
t
j t /2 Std/( / /) g is an or/-
thogonal basis of S
/
/.
/(ii/) By part /(i/) w e ma y write f
s
T
i
/=
P
v
c
v
f
v
for some c
v
/2 R where v /2 Std/( / /)/.
Let k b e an y in teger suc h that k /6/= i/; i /+ /1 /(note that there is nothing to pro v e
when n / /2/)/. Then T
i
and L
k
comm ute so f
s
T
i
L
k
/= f
s
L
k
T
i
/= /[res
s
/( k /)/]
q
f
s
T
i
b y
Prop osition /3/./3/3/(iii/)/. On the other hand/,
f
s
T
i
L
k
/=
X
v
c
v
f
v
L
k
/=
X
v
c
v
/[res
v
/( k /)/]
q
f
v
/:
Equating co e/cien ts/, c
v
/[res
v
/( k /)/]
q
/= c
v
/[res
s
/( k /)/]
q
for all k /6/= i/; i /+ /1/. Therefore/, b y
Lemma /3/./3/2/(ii/)/, c
v
/= /0 unless v /= s /, or v /= t and t is standard/.
Supp ose /rst that t is not standard/; then w e ha v e sho wn that f
s
T
i
/= c
s
f
s
for
some c
s
/2 R /. By Prop osition /3/./3/3/(i/)/, f
s
/= m
s
/+
P
v B s
a
v
m
v
for some a
v
/2 R /.
Because t is not standard/, either i and i /+ /1 are in the same ro w of s or they
are in the same column/. In the /rst case/, m
s
T
i
/= q m
s
b y Corollary /3/./4/; in the
second/, m
s
T
i
/= /? m
s
/+
P
v B s
b
v
for some b
v
/2 R b y Corollary /3/./1/9/. Therefore/, b y
Prop osition /3/./3/3/(i/) again/, f
s
T
i
equals q f
s
or /? f
s
resp ectiv ely /.
No w assume that t is standard/. W e ha v e sho wn that f
s
T
i
/= c
s
f
s
/+ c
t
f
t
for some
c
s
/; c
t
/2 R /. First supp ose that s B t /. Then m
s
T
i
/= m
t
/; so/, f
s
T
i
/= m
t
/+
P
u B t
b
u
m
u
for some b
u
/2 R /. Therefore/, as in the last paragraph/, c
t
/= /1/; that is/, f
s
T
i
/= c
s
f
s
/+ f
t
/.
No w res
s
/( i /) /= res
t
/( i /+ /1/) and res
s
/( i /+ /1/) /= res
t
/( i /)/. Therefore/, using Theorem /3/./3/0
and Prop osition /3/./2/4/(ii/)/, w e /nd that
c
s
/[res
t
/( i /)/]
q
f
s
/+ /[res
s
/( i /)/] f
t
/= /( c
s
f
s
/+ f
t
/
L
i /+/1
/= f
s
T
i
L
i /+/1
/= f
s
/
/( q /? /1/) L
i /+/1
/+ /1 /+ L
i
T
i
/	
/=
/
/( q /? /1/)/[res
t
/( i /)/]
q
/+ /1 /+ c
s
/[res
s
/( i /)/]
q
/	
f
s
/+ /[res
s
/( i /)/]
q
f
t
/:
Consequen tly /, remem b ering that /[ m /]
q
/= /( q
m
/? /1/) /= /( q /? /1/) /(when q /6/= /1/)/,
c
s
/=
/( q /? /1/)/[res
t
/( i /)/]
q
/+ /1
/[res
t
/( i /)/]
q
/? /[res
s
/( i /)/]
q
/= q
res
t
/( i /)
/( q /? /1/)
q
res
t
/( i /)
/? q
res
s
/( i /)
/= /?
/1
/[ / /]
q
as claimed/.
The form ula for f
t
T
i
/(or/, equiv alen tly /, for f
s
T
i
when t is standard and t B s /)
can no w b e obtained b y expanding f
s
T
/2
i
/= f
t
T
i
/? /1 /= /[ / /]
q
f
s
T
i
/.
W e will see in the next section that H is semisimple if and only if e /> n /; so
the last few results ha v e really b een ab out the semisimple case/. Ev en so/, our main
applications of these results will b e in the case where H is not semisimple/.
/4/. The irreducibl e H /{mo dules
In this section w e giv e necessary and su/cien t conditions for the mo dule D
/
to
b e non/{zero/; b y Theorem /3/./2/1 this will classify the simple H /{mo dules/. Throughout
this section w e assume that R is a /eld/.
Recall that e is the smallest p ositiv e in teger suc h that /[ e /]
q
/= /0 /(or e /= /1 /)/.
/3/2 /3/. THE MODULAR REPRESENT A TION THEOR Y OF H
Supp ose that / /= /( /
/1
/; /
/2
/; /: /: /: /)/. Then / is e /{restricted if /
i
/? /
i /+/1
/< e for all
i / /1/. In addition/, w e sa y that a standard / /{tableau s is e /{restricted if whenev er
/ B / and t /2 Std/( / /) then /[res
s
/( k /)/]
q
/6/= /[res
t
/( k /)/]
q
for some k /. Let Std
e
/( / /) b e the
set of e /{restricted tableaux/.
W e will sho w that / is e /{restricted if and only if there exists an e /{restricted / /{
tableau/. The next t w o Lemmas pro v e one direction/. Before the reader gets excited/,
w e remark that the lo w er b ound giv en for dim D
/
in the next Lemma is rarely
sharp/.
/3/./3/5 Lemma L et / b e a p artition of n /. Then dim D
/
/ j Std
e
/( / /) j /.
Pro of/. Let L b e the subalgebra of H generated b y L
/1
/; L
/2
/; /: /: /: /; L
n
and let / b e
a partition of n /. Supp ose that t
/1
/; t
/2
/; /: /: /: /; t
k
are the standard / /{tableaux/, ordered
so that i /> j whenev er t
i
B t
j
/. F or i /= /0 /; /1 /: /: /: /; k let S
/
i
b e the R /{mo dule spanned
b y f m
t
j
j /1 / j / i g and let S
/
/( t
i
/) /= S
/
i
/=S
/
i /? /1
/. By Theorem /3/./3/0 the R /{mo dules
S
/
i
and S
/
/( t
i
/) are L /{mo dules and/, up to isomorphism/, S
/
i
/( t
i
/) dep ends only up on
the sequence /(/[res
t
i
/(/1/)/]
q
/; /: /: /: /; /[res
t
i
/( n /)/]
q
/]/)/. Th us/, S
/
/= S
/
/1
/> S
/
/2
/> / / / /> S
/
k
/> /0 is
an L /{mo dule comp osition series of S
/
with simple comp osition factors/.
No w supp ose that s is an e /{restricted / /{tableau and let / b e a partition of n
with D
/
/6/= /0/. By Corollary /2/./1/4/, D
/
is a comp osition factor of S
/
only if / D / /;
ho w ev er/, b y assumption/, the L /{mo dule S
/
/( s /) is not an L /{comp osition factor
of S
/
/| and hence D
/
/| if / B / /. Therefore/, S
/
/( s /) is an L /{comp osition factor
of D
/
/. This pro v es the Lemma/.
Next/, w e de/ne the ladder numb er of a no de /( i/; j /) /2 N / N to b e the in teger
l
e
/( i/; j /) /= i /? j /+ ej /? e /. Th us/, t w o no des ha v e the ladder n um b er only if they ha v e
the same e /{residue/. F or example/, if / /= /(/4 /; /3/) and e /= /3 then the ladder n um b ers
in /[ / /] are
/0 /1 /2 /3
/2 /3 /4
and w e reduce these mo dulo /3 to obtain the e /{residues
/0 /1 /2 /0
/2 /0 /1
/.
Let / b e a partition of n /. The ladder tableau l
/
e
is de/ned inductiv ely as follo ws/.
If n /= /1 set l
/
e
/= t
/
/. When n /> /1 let /( i/; j /) b e the unique no de in /[ / /] suc h that
/(i/) l
e
/( i/; j /) / l
e
/( k /; l /) for all /( k /; l /) /2 /[ / /]/, and /(ii/)/, if l
e
/( i/; j /) /= l
e
/( k /; l /) then i / k /. Let
/ b e the partition of n /? /1 with diagram /[ / /] n f /( i/; j /) g and de/ne l
/
e
to b e unique
/ /{tableau suc h that l
/
e
/# /( n /? /1/) /= l
/
e
/; that is/,
/3 /: /3/6 l
/
e
/( k /; l /) /=
/(
l
/
e
/( k /; l /) /; if /( k /; l /) /6/= /( i/; j /) /;
n/; if /( k /; l /) /= /( i/; j /) /:
By construction l
/
e
is a standard / /{tableau/.
F or example/, if / /= /(/4 /; /3/) and e /= /3/, as ab o v e/, then l
/
e
/=
/1 /2 /4 /6
/3 /5 /7
/.
/3/./3/7 Lemma Supp ose that / is an e /{r estricte d p artition of n /. Then the ladder
table au l
/
e
is e /{r estricte d/.
Pro of/. W e pro v e this b y induction on n /, the result b eing clear when n /= /1/.
Let /( i/; j /) and / as in /(/3/./3/6/)/. W e claim that the partition / is e /{restricted/. If
not then either /(i/) /
i
/? /
i /+/1
/= e /, or /(ii/) i /> /1 and /
i /? /1
/? /
i
/= e /. The /rst case
cannot happ en b ecause then /
i
/? /
i /+/1
/> e whic h con tradicts our assumption that
/ is e /{restricted/. In the second scenario/, ro w /( i /? /1/) of / w ould con tain a no de with
higher ladder n um b er con tradicting our c hoice of /( i/; j /)/. Hence/, / is e /{restricted as
claimed/.
Let / b e a partition and supp ose that / D / and that there exists a / /{tableau t
with /[res
t
/( k /)/]
q
/= /[res
l
/
e
/( k /) for k /= /1 /; /: /: /: /; n /. In particular/, /[res
t
/( n /)/]
q
/= /[res
l
/
e
/( n /)/]
q
/,
/4/. THE IRREDUCIBLE H /{MODULES /3/3
so / D Shap e/( t /# /( n /? /1/)/) since /( i/; j /) is the lo w est no de with e /{residue /[res
l
/
e
/( n /)/]
q
whic h ma y b e added to /[ / /] to giv e the diagram of a partition/. By induction on n
the tableau l
/
e
is e /{restricted/, so this forces t /# /( n /? /1/) /= l
/
e
/. Ho w ev er/, if t /( k /; l /) /= n
then k / i b ecause / D / /. Therefore/, /( k /; l /) /= /( i/; j /)/, t /= l
/
e
and / /= / /; hence/, l
/
e
is
e /{restricted as required/.
Com bining the last t w o results w e see that if / is e /{restricted then D
/
is non/{
zero/. T o pro v e the con v erse w e need some more notation/.
If / /= /( /
/1
/; /: /: /: /; /
k
/) is a partition and i an in teger with /1 / i / k let /
i
/=
/( /
i
/; /
i /+/1
/; /: /: /: /; /
k
/) and / /= /( /
/1
/? /
/2
/; /
/2
/? /
/3
/; /: /: /: /)/. Let g
i
b e the greatest common
divisor of /[ /
 /]
/!
q
/, where /
 runs o v er all partitions of /
i
suc h that /
 B /
i
/. Finally /, w e
de/ne g
/
/= g
/1
g
/2
/: /: /: g
k
/.
/3/./3/8 Lemma Supp ose that / /= /( /
/1
/; /: /: /: /; /
k
/) is a p artition of n and let s and t b e
standar d / /{table aux/. Then g
/
is a factor of h m
s
/; m
t
i /.
Pro of/. By de/nition/, h m
s
/; m
t
i m
/
/ m
t
/
s
m
tt
/ mo d H
/
/; ho w ev er/, b y Corol/-
lary /3/./4/, m
t
/
s
m
tt
/ is a linear com bination of terms m
/
T
d /( v /)
m
/
where v is a ro w
standard / /{tableau/. So/, c hanging notation/, it is su/cien t to sho w that if t is a ro w
standard / /{tableau then m
/
T
d /( t /)
m
/
/ r g
/
m
/
for some r /2 R /.
De/ne / /= /( /
/1
/; /: /: /: /; /
k
/) to b e the comp osition of /
/1
suc h that /
i
is equal to the
n um b er of en tries in ro w i of t whic h are less than or equal to /
/1
/. Abusing notation/,
write m
/
/= m
/
/1
/: /: /: m
/
k
where S
/
/= S
/
/1
/ / / / / S
/
k
and m
/
i
/=
P
x /2 S
/
i
T
x
for
/1 / i / k /.
W e /rst consider m
t
/
t
m
/
/1
/. Let u b e the ro w standard / /{tableau whic h agrees
with t on all en tries greater than /
/1
and where /1 /; /2 /; /: /: /: /; /
/1
are inserted in increasing
order from left to righ t and then top to b ottom in to the remaining p ositions/. Then
t /= u w for some w /2 S
/
/1
suc h that /` /( d /( t /)/) /= /` /( d /( u /)/) /+ /` /( w /)/; so m
t
/
t
/= m
t
/
u
T
w
/.
Therefore/, b y Lemma /3/./2 and Corollary /3/./4/,
m
t
/
t
m
/
/1
/= m
t
/
u
T
w
m
/
/1
/= q
/` /( w /)
m
t
/
u
m
/
/1
/= q
/` /( w /)
/[ / /]
/!
q
m
t
/
u
h
for some h /2 H /( S
/
/1
/.Consequen tly /, m
t
/
u
m
/
/1
is an elemen t of H m
/
where / is the
comp osition /( /
/1
/; /
/1
/? /
/1
/; /: /: /: /; /
k
/? /
k
/)/.
Supp ose that / /6D / /. Then / /6D / where / is the partition obtained from / b y
reordering its parts/; therefore/, m
t
/
t
m
/
/1
/2 H
/
/\ H m
/
/
/
H
/
b y Corollary /2/./3/(iii/)/.
Th us/, m
t
/
t
m
/
/1
/ /0 mo d
/
H
/
and/, in particular/, our claim is correct in this case/.
On the other hand/, if / D / then /( /
/1
/; /
/2
/; /: /: /: /; /
k
/) D /( /
/1
/; /
/1
/? /
/1
/; /: /: /: /; /
/1
/? /
k
/)/;
equiv alen tly /, / D /
/1
/= /( /
/1
/? /
/2
/; /: /: /: /; /
k /? /1
/? /
k
/)/. No w/, g
/1
is a factor of /[ / /]
/!
q
/, so b y
Theorem /3/./1/8 there exist r
v
/2 R suc h that
m
t
/
t
m
/
/1
/= q
/` /( w /)
/[ / /]
/!
q
m
t
/
u
h / g
/1
X
v /2 Std /( / /)
r
v
m
t
/
v
mo d
/
H
/
/:
Moreo v er/, b y the righ t handed v ersion of Prop osition /3/./1/6/, r
v
/6/= /0 only if the
in tegers /1 /; /2 /; /: /: /: /; /
/1
all app ear in the /rst ro w of v /; that is to sa y that r
v
/6/= /0
only if v and t
/
ha v e the same /rst ro w/. Rep eating this argumen t w e /nd that for
i /= /1 /; /2 /: /: /: /; k there exist r
v
/2 R suc h that
m
t
m
/
/1
/: /: /: m
/
i
/= g
/1
/: /: /: g
i
X
v /2 Std /( / /)
r
v
m
v
/3/4 /3/. THE MODULAR REPRESENT A TION THEOR Y OF H
and r
v
/6/= /0 only if the tableaux v and t
/
agree on the /rst i ro ws/. T aking i /= k
pro v es the Lemma/.
Let d
//
/= /[ S
/
/: D
/
/] b e the comp osition m ultiplicit y of D
/
in S
/
/. W e can no w
pro v e the follo wing k ey result of Dipp er and James/.
/3/./3/9 Theorem /(Dipp er/{James/) Supp ose that R is a /eld/.
/(i/) f D
/
j / an e /{r estricte d p artition of n g is a c omplete set of non/{isomorphic
irr e ducible H /{mo dules/.
/(ii/) Supp ose that / is an e /{r estricte d p artition of n and that / is a p artition of n /.
Then d
//
/= /1 and d
//
/6/= /0 only if / D / /.
Pro of/. Ev erything will follo w from Theorem /2/./1/3 and Corollary /2/./1/4 once w e sho w
that D
/
/6/= /0 if and only if / is e /{restricted/. That D
/
/6/= /0 when / is e /{restricted is
immedia te from Lemmas /3/./3/7 and /3/./3/5/.
Con v ersely /, if / is not e /{restricted then /
i
/? /
i /+/1
/ e for some in teger i / /1/;
consequen tly /, /[ e /]
/!
q
is a factor of g
/
since /[ e /]
/!
q
divides g
i
/. Ho w ev er/, /[ e /]
/!
q
/= /0 so g
/
m ust also b e /0/. Therefore/, h m
s
/; m
t
i /= /0 for an y s /; t /2 Std /( / /) b y Lemma /3/./3/8/; th us/,
rad S
/
/= S
/
and D
/
/= /0/.
In particular/, w e see that S
/
/= D
/
for all / if and only if e /> n /. Hence/, b y
Corollary /2/./1/8 w e ha v e an easy w a y of determining whether or not H is semisimple/.
More precisely /, w e ha v e the follo wing/.
/3/./4/0 Corollary Supp ose that R is a /eld/. Then the fol lowing ar e e quivalent/.
/(i/) H is a split semisimple algebr a/;
/(ii/) S
/
/= D
/
for al l p artitions / of n /; and/,
/(iii/) e /> n /.
Note that e is equal to the c haracteristic of R in the case where q /= /1/. Conse/-
quen tly /, as they m ust/, these results agree with the corresp onding results from the
represen tation theory of the symmetric group /(see /[ /3/6 /] and Note /3 b elo w/)/.
Theorem /3/./3/9 com bined with Lemma /3/./3/5 also giv es us the follo wing com bina/-
torial result /(a more direct pro of can b e extracted from /[ /3/5 /, Theorem A/]/)/.
/3/./4/1 Corollary L et / b e a p artition of n /. Then / is e /{r estricte d if and only if
ther e exists an e /{r estricte d / /{table au/.
Notes on Chapter /3
/1/. The pro of of Prop osition /3/./7 comes from /[ /1/3 /]/. Although this result m ust ha v e
b een kno wn for some time/, this is the only place where I ha v e seen it in the
literature/.
/2/. In his thesis /[ /3/2 /]/, Ho efsmit classi/ed the irreducible H
K
/{mo dules b y using
Y oung/'s seminormal form /(Theorem /3/./3/4/) as the de/nition of the Sp ec h t mo dules/.
Later Dipp er and James /[ /1/3 /] constructed the Sp ec h t mo dules as submo dules of
H and hence classi/ed the irreducible H /{mo dules o v er an arbitrary /eld/. The
approac h that w e ha v e tak en here is based up on w ork of Murph y /[ /5/5 /, /5/6 /]/.
/3/. Let /# b e the R /{linear automorphism of H determined b y T
/#
w
/= /( /? q /)
/` /( w /)
T
/? /1
w
/? /1
for all w /2 S
n
/. Then S
/ /#
is isomorphic to the dual of Dipp er and James/' Sp ec h t
mo dule whic h is indexed b y the partition conjugate to / /(see /[ /5/6 /, Theorem
/5/./2/] and the w arning on page /2/5/)/. This is also wh y the simple H /{mo dules
NOTES ON CHAPTER /3 /3/5
in Theorem /3/./3/9 are indexed b y e /{restricted partitions rather than e /{regular
partitions /(a partition is e /{regular if its conjugate is e /{restricted/)/.
/4/. If / is a partition let n
/
/=
P
w /2 S
/
/( /? q /)
/? /` /( w /)
T
w
and for s /; t /2 Std /( / /) de/ne
n
st
/= T
/
d /( s /)
n
/
T
d /( t /)
/. Then
N /= f n
st
j s /; t /2 Std /( / /) for some partition / of n g
is a basis of H /. It is easy to c hec k that m
/#
/
/= q
a
n
/
for some in teger a /; since
the automorphism s / and /# comm ute this sho ws that /( N /; //) is a cellular basis/.
/5/. In the represen tation theory of the symmetric groups the elemen ts L
k
w ere in/-
tro duced indep enden tly b y Jucys /[ /4/5 /] and Murph y /[ /5/4 /]/. Dipp er and James /[ /1/4 /]
/rst studied their analogues in the represen tation theory of H /.
/6/. Let L
/0
k
/= q
/1 /? k
T
k /? /1
/: /: /: T
/1
T
/1
/: /: /: T
k /? /1
for /1 / k / n /. An easy argumen t sho ws
that L
/0
k
/= /( q /? /1/) L
k
/+ /1/; accordingly /, man y authors prefer to use these elemen ts
b ecause they are easier to w ork with/. Unfortunately /, when q /= /1/, whic h is the
case of the symmetric group/, L
/0
k
/= /1 for all k /. Rather that ha ving to treat this
imp ortan t sp ecial case separately w e use the elemen ts L
k
throughout/.
/7/. Lemma /3/./3/5 is essen tially Prop osition /5/./9/(i/) of /[ /2/6 /]/. Lemma /3/./3/7 is motiv ated
b y the w ork of Lascoux/, Leclerc and Thib on /[ /5/1 /] who/, in turn/, w ere inspired
b y James /[ /3/5 /]/. The argumen t of Lemma /3/./3/8 is due to Murph y /[ /5/6 /] /(cf/. /[ /1/3 /,
Theorem /6/./8/]/)/.
/8/. The pro of of Lemma /3/./3/5 actually sho ws that d
//
/ k where k is maxima l suc h
that Std/( / /) /= X
/0
t X
/1
t /: /: /: t X
k
/(disjoin t union/) where for i /= /1 /; /2 /: /: /: /; k there
exists a bijection /
i
/: X
i
/? /! Std
e
/( / /) suc h that /[res
t
/( k /)/]
q
/= /[res
/
i
/( t /)
/( k /)/]
q
for all
t /2 X
i
and all k with /1 / k / n /.
/9/. The rank of the Sp ec h t mo dule S
/
is explicitly kno wn /(see /[ /3/6 /]/)/; it is equal
to n /! /=
Q
h
/
ij
where the pro duct if o v er the no des /( i/; j /) /2 /[ / /] and h
/
ij
is the /( i/; j /)th
ho ok length /(see page /5/5/)/. Except in some v ery sp ecial cases/, the dimension
of D
/
is not kno wn/.
CHAPTER /4
The q /{Sc h ur Algebra
The q /{Sc h ur algebra w as in tro duced b y Dipp er and James /[ /1/5 /] who sho w ed
that this algebra completely determines the decomp osition matrices of the /nite
general linear groups in non/{de/ning c haracteristic/. The q /{Sc h ur algebras also
ha v e applications to the represen tation theory of the general linear groups o v er
other /elds/. W e do not explore these connections here/. Instead/, in this Chapter w e
/`lift/' the Murph y basis of H to giv e a cellular basis of the q /{Sc h ur algebra/.
/1/. Semistandard tableaux
/4/./1 Let//( d/; n /) b e a set of comp ositions of n with a most d non/{zero parts/. The
q /{Schur algeb ra is the endomorphism algebra
S /( d/; n /) /= End
H
/
M
/ /2 //( d/;n /)
M
/
/
/:
Note that the q /{Sc h ur algebra/, lik e H /, is dep enden t up on the c hoices of R and q /.
By de/nition/, S /( d/; n /)
/
/=
L
//;/ /2 //( d/;n /)
Hom
H
/( M
/
/; M
/
/)/; accordingly /, m uc h of
this Chapter is dev oted to understanding the ideals M
/
and the homomorphism s
b et w een them/. T o this end w e no w in tro duce another kind a tableaux/.
/4/./2 Let / and / b e comp ositions of n /. A / /{tableau of t yp e indextableau/!t yp e / is
a map T /: /[ / /] /? /! N suc h that /
i
/= /# f x /2 /[ / /] j T /( x /) /= i g for i / /1/. Again w e write
Shap e/( T /) /= / /.
F or example/, if /! /= /(/1
n
/) then the tableaux of Chapter /3 are precisely the
tableaux of t yp e /! /. W e con tin ue to use lo w er case letters for tableaux of t yp e /! /;
tableaux of arbitrary t yp e will b e denoted b y upp er case letters/.
A / /{tableau T is ro w semistanda rd if the en tries in eac h ro w of T are non/{
decreasing/; T is semistanda rd if /(i/) / is a partition/, and /(ii/) T is ro w semistandard
and the en tries in eac h column of T are strictly increasing/. Let T /( //; / /) b e the set
of ro w semistandard / /{tableaux of t yp e / and i T
/0
/( //; / /) b e the set of semistandard
/ /{tableaux of t yp e / /.
/4/./3 Examples Supp ose that / is a comp osition of n /.
/(i/) Let T
/
b e the tableau of t yp e / suc h that T
/
/( ij /) /= i for all /( i/; j /) /2 /[ / /]/. Then
T
/
is the unique semistandard / /{tableau T
/
of t yp e / /. F or example/, if / /= /(/3 /; /2 /; /1/)
then T
/
/=
/1 /1 /1
/2 /2
/3
/.
/(ii/) All of the semistandard tableaux of t yp e / can b e obtained from T
/
b y
/`mo ving no des up/' in T
/
/. Con tin uing example /(i/)/, the other semistandard tableaux
of t yp e /(/3 /; /2 /; /1/) are
/1 /1 /1 /2
/2
/3
/,
/1 /1 /1
/2 /2 /3
/,
/1 /1 /1 /2
/2 /3
/,
/1 /1 /1 /3
/2 /2
/,
/1 /1 /1 /2 /2
/3
/,
/1 /1 /1 /2 /3
/2
and
/1 /1 /1 /2 /2 /3
/.
Next w e describ e a w a y of con v erting tableaux of t yp e /! in to tableaux of t yp e / /.
Let t b e a tableau of t yp e /! and let / b e a comp osition/. Then / /( t /) the tableau of
/3/6
/1/. SEMIST AND ARD T ABLEA UX /3/7
t yp e / obtained from t b y replacing eac h en try i in t b y r if i app ears in ro w r of
t
/
/.
/4/./4 Examples /(i/) If t is a ro w standard / /{tableau then / /( t /) is ro w semistandard/.
/(ii/) Supp ose that t /=
/1 /3 /4 /5
/2 /6
and let / /= /(/3 /; /2 /; /1/)/. Then / /=
/1 /2 /3
/4 /5
/6
so w e ha v e
/ /( t /) /=
/1 /1 /2 /2
/1 /3
/.
/(iii/) If / is a comp osition then T
/
/= / /( t
/
/)/.
Let / and / b e comp ositions and supp ose d /2 D
/
/. Then t
/
d is ro w standard
and the subgroup d
/? /1
S
/
d is just the ro w stabilizer of t
/
d /. Therefore/, d
/? /1
S
/
d /\ S
/
is generated b y S /\ d
/? /1
S
/
d /\ S
/
and so d
/? /1
S
/
d /\ S
/
/= S
/
for some comp osition /
of n /. W e write / /= /d /\ / /.
W e can no w generalize Prop osition /3/./3 to describ e the /( S
/
/; S
/
/)/{double cosets/.
/4/./5 Prop ositio n Supp ose that / and / ar e c omp ositions of n and let
D
//
/=
n
d /2 S
n
/
/
/
/ /( t
/
d /) is r ow semistandar d and t
/
d D t whenever t
is a r ow standar d table au such that / /( t /) /= / /( t
/
d /)
o
/:
Then D
//
is a c omplete set of /( S
/
/; S
/
/) /{double c oset r epr esentatives in S
n
/. In
addition/, the fol lowing hold/.
/(i/) Every element w of S
n
c an b e written uniquely in the form w /= v du wher e
v /2 S
/
/, d /2 D
//
and u /2 D
/d /\ /
/\ S
/
/. F urthermor e/, /` /( w /) /= /` /( v /) /+ /` /( d /) /+ /` /( u /) /.
/(ii/) D
//
/= D
/
/\ D
/? /1
/
/.
/(iii/) The map d /7/? /! / /( t
/
d /) gives a one/{to/{one c orr esp ondenc e b etwe en the elements
of D
//
and the set of r ow semistandar d / /{table aux of typ e / /.
Pro of/. By Prop osition /3/./3/, the righ t cosets of S
/
are indexed b y ro w standard
/ /{tableau/. Therefore/, the
/?
S
/
/; S
/
/)/{double cosets are indexed b y S
/
/{orbits of ro w
standard / /{tableaux/. F urthermore/, t w o ro w standard tableaux s and t are in the
same S
/
/{orbit if and only if / /( s /) /= / /( t /)/; that is/, if d and d
/0
are elemen ts of D
/
then S
/
d S
/
/= S
/
d
/0
S
/
if and only if / /( t
/
d /) /= / /( t
/
d
/0
/)/.
Let O b e a S
/
/{orbit of ro w standard / /{tableaux/. Then O con tains a unique
tableau t suc h that whenev er i and i /+ /1 are in the same ro w of t
/
then either i and
i /+ /1 are in the same ro w of t or t B t /( i/; i /+ /1/)/. Let d /= d /( t /)/. Then O is precisely
the set of ro w standard tableau of the form t
/
du where u /2 S
/
/(and du /2 D
/
/)/.
No w t
/
du /= t u is ro w standard if and only if iu /< j u for all in tegers i /< j whic h
are in the same ro w of t
/
d /. Therefore/, u /2 D
/d /\ /
and /` /( du /) /= /` /( d /) /+ /` /( u /) b y
Prop osition /3/./3/. Hence/, an y w in the double coset S
/
d S
/
is uniquely expressible
in the form v du for some v /2 S
/
and u /2 D
/d /\ /
/. Moreo v er/, b y Prop osition /3/./3
again/, /` /( w /) /= /` /( v /) /+ /` /( du /) since du /2 D
/
/; th us/, /` /( w /) /= /` /( v /) /+ /` /( d /) /+ /` /( u /)/, pro ving /(i/)/.
F or /(ii/) note that b y /(i/) if d /2 D
//
then d is the unique elemen t of minim al
length in S
/
d S
/
/. In particular/, d is the unique elemen t of minim al length in S
/
d
and also in d S
/
/; so D
//
/ D
/
/\ D
/? /1
/
b y Prop osition /3/./3/. Con v ersely /, an y elemen t
of D
/
/\ D
/? /1
/
m ust b e an elemen t of minim al length in its double coset and hence
b elongs to D
//
/.
Finally /, for /(iii/) if T is a ro w semistandard / /{tableau of t yp e / then w e can easily
/nd a ro w standard tableau t suc h that / /( t /) /= T /, so T corresp onds to a /( S
/
/; S
/
/)/{
double set/. W e ha v e already observ ed the con v erse/, so the pro of is complete/.
The elemen ts of D
//
are called distinguished double coset rep resentatives of S
n
/.
/3/8 /4/. THE q /{SCHUR ALGEBRA
Let T b e a ro w semistandard / /{tableau of t yp e / and de/ne /rst /( T /) to
b e the unique ro w standard / /{tableau suc h that / /(/rst/( T /)/) /= T and /rst /( T /) D t
whenev er t is a ro w standard tableau suc h that / /( t /) /= T /. It is also easy to see that
there exists a unique ro w standard tableau last /( T /) suc h that / /(last /( T /)/) /= T and
t D last/( T /) whenev er t is another ro w standard tableau suc h that / /( t /) /= T /.
/4/./6 Example Supp ose that / /= /(/4 /; /4/) and let T b e the / /{tableau
/1 /1 /3 /4
/2 /3 /3 /4
/. Then T is
of t yp e / /= /(/2 /; /1 /; /3 /; /2/)/, /rst/( T /) /=
/1 /2 /4 /7
/3 /5 /6 /8
and last/( T /) /=
/1 /2 /6 /8
/3 /4 /5 /7
/. Let d /= d /(/rst/( T /)/)/;
then /d /\ / /= /(/2 /; /1 /; /1 /; /2 /; /1 /; /1/) since S
/d /\ /
is the in tersection of S
/
with the ro w
stabilizer of /rst /( T /)/.
Let d /2 D
//
and let T /= / /( t
/
d /) and S /= / /( t
/
d
/? /1
/)/. Then w e ha v e sho wn that S
and T are b oth ro w semistandard and that
/4 /: /7
X
y /2 D
/
/ /( t
/
y /)/= S
T
/
y
m
/
/=
X
w /2 S
/
d S
/
T
w
/=
X
x /2 D
/
/ /( t
/
x /)/= T
m
/
T
x
/:
The elemen t d also determines an H /{mo dule homomorphism /'
d
//
/: M
/
/? /! M
/
giv en b y
/'
d
//
/( m
/
h /) /=
X
w /2 S
/
d S
/
T
w
h/; for all h /2 H /:
In fact/, these elemen ts giv e a basis of Hom
H
/( M
/
/; M
/
/)/.
/4/./8 Theorem L et / and / b e c omp ositions of n /. Then Hom
H
/( M
/
/; M
/
/) is fr e e as
an R /{mo dule with b asis f /'
d
//
j d /2 D
//
g /.
Pro of/. Supp ose that /' /2 Hom
H
/( M
/
/; M
/
/)/. Then/, for all h /2 H /, w e ha v e that
/' /( m
/
h /) /= /' /( m
/
/) h /; hence/, /' is completely determined b y /' /( m
/
/)/. By Corollary /3/./4
there exist r
d
/2 R suc h that
/' /( m
/
/) /=
X
d /2 D
/
r
d
m
/
T
d
/:
Cho ose x /2 D
/
of minim al length suc h that r
x
/6/= /0/. If x /=/2 D
//
then b y Prop o/-
sition /4/./5 there exists s /2 S /\ S
/
suc h that /` /( xs /) /= /` /( x /) /? /1/. Then xs /2 D
/
and
/' /( m
/
/) /= q
/? /1
/' /( m
/
T
s
/) /= q
/? /1
X
d /2 D
/
r
d
m
/
T
d
T
s
/= r
x
m
/
T
xs
/+
X
d /2 D
/
b
d
m
/
T
d
for some b
d
/2 R suc h that b
xs
/= /0/. In particular/, this sho ws that m
/
T
xs
is
in v olv ed in /' /( m
/
/) con trary to our assumption that x is an elemen t of minim al
length with r
x
/6/= /0/. Therefore/, x /2 D
//
and/, consequen tly /, /'
/0
/= /' /? a
x
/' b elongs to
Hom
H
/( M
/
/; M
/
/)/. F urthermore/, /'
/0
/( m
/
/) is a linear com bination of a terms of the
form m
/
T
d
where d /2 D
/
and d /6/= x /. In fact/, the ab o v e argumen t sho ws that m
/
T
d
is not in v olv ed in /'
/0
/( m
/
/) whenev er S
/
d S
/
/= S
/
x S
/
/. Hence/, w e can rep eat this
argumen t to write /' as linear com bination of maps /'
x
//
with x /2 D
//
as required/.
Finally /, it remains to c hec k that f /'
d
//
j d /2 D
//
g is linearly indep enden t/. This
follo ws b ecause f /'
d
//
/( m
/
/) j d /2 D
//
g is a linearly indep enden t subset of M
/
/(b eing
sums o v er distinct /( S
/
/; S
/
/)/{double cosets b y /(/4/./7/)/)/.
/4/./9 Corollary L et / and / b e c omp ositions of n /. Then Hom
H
/( M
/
/; M
/
/) and
M
/
/\ M
/ /
ar e c anonic al ly isomorphic as R /{mo dules/.
/2/. A SPECHT SERIES F OR M
/
/3/9
Pro of/. Ev ery homom orphism /' in Hom
H
/( M
/
/; M
/
/) is determined b y /' /( m
/
/) and/,
moreo v er/, /' /( m
/
/) /2 M
/
/\ M
/ /
b y Theorem /4/./8/. Con v ersely /, v ery elemen t of M
/
/\
M
/ /
determines a homom orphism in Hom
H
/( M
/
/; M
/
/)/. Consequen tly /, the map
Hom
H
/( M
/
/; M
/
/) /! M
/
/\ M
/ /
giv en b y /' /7/? /! /' /( m
/
/) is an isomorphism of R /{
mo dules/.
There are t w o p oin ts w orth noting from Theorem /4/./8/. First/, b y Prop osition /4/./5
w e could ha v e indexed the basis f /'
d
//
j d /2 D
//
g of Hom
H
/( M
/
/; M
/
/) b y ro w semi/-
standard / /{tableau of t yp e / /(or b y ro w semistandard / /{tableaux of t yp e / /)/. Th us/,
this basis is the analogue of the ro w standard basis of M
/
giv en b y Corollary /3/./4/.
Secondly /, b y extending the maps /'
d
//
to elemen ts of S /( d/; n /) w e obtain a basis
of the q /{Sc h ur algebra whic h is indep enden t of R and q /.
/2/. A Sp ec h t series for M
/
In Theorem /4/./8 w e sa w that Hom
H
/( M
/
/; M
/
/) has a basis indexed b y ro w
semistandard tableaux/. As in Chapter /3/, w e w an t to replace this basis with a
cellular basis whic h is indexed b y pairs of semistandard tableaux/. Rather than
pro ving this directly /, w e /rst giv e another basis of M
/
whic h is compatible with
the Murph y basis of H /.
Let / b e a partition of n and / a comp osition of n /. Let S b e a semistandard
/ /{tableaux of t yp e / and let t b e a standard / /{tableau/. W e de/ne
m
S t
/=/=
X
s /2 Std /( / /)
/ /( s /)/= S
m
st
and let m
t S
/= m
/
S t
/.
/4/./1/0 Theorem /(Murph y/) L et / b e a c omp osition of n /. Then M
/
is fr e e as an
R /{mo dule with b asis
n
m
S t
/
/
/
S /2 T
/0
/( //; / /) /, t /2 Std/( / /) for some p artition / of n
o
/:
Pro of/. Supp ose that S /2 T
/0
/( //; / /)/, t /2 Std/( / /) and let d
/? /1
/= /rst /( S /)/. By /(/4/./7/)
m
S t
/=
X
s /2 Std /( / /)
/ /( s /)/= S
T
/
d /( s /)
m
/
T
d /( t /)
/=
X
w /2 S
/
d S
/
T
w
T
d /( t /)
/:
In particular/, m
S t
/2 M
/
/.
No w supp ose that h is an arbitrary non/{zero elemen t of M
/
/. By Theorem /3/./1/8
there exist r
st
/2 R suc h that h /=
P
r
st
m
st
where m
st
/2 M /. Supp ose that m
st
is in v olv ed in h /. By de/nition/, S /= / /( s /) is alw a ys ro w standard/; therefore/, S is
semistandard b y Prop osition /3/./1/6/. If s /6/= /rst /( S /) then there exists s
i
/2 S
/
suc h
that if s
/0
/= s s
i
then / /( s
/0
/) /= S and s
/0
B s /. Then T
i
m
st
/= /( q /? /1/) m
st
/+ q m
s
/0
t
b y Corollary /3/./4 and T
i
h /= q h b y Lemma /3/./2/; hence/, m
s
/0
t
is also in v olv ed in h /.
Consequen tly /, w e ma y as w ell assume that s /= /rst/( S /)/. No w let
h
/0
/= h /?
X
/ /` n
X
S /2T
/0
/( //;/ /)
X
s /; t /2 Std /( / /)
s /=/rst/( S /)
r
st
m
S t
/:
Then h
/0
is an elemen t of M
/
/; ho w ev er/, h in v olv es no term m
st
with s /= /rst /( / /( s /)/)/.
Therefore/, h
/0
/= /0 and w e ha v e written h as a linear com bination of the required
/4/0 /4/. THE q /{SCHUR ALGEBRA
form/.
This allo ws us to giv e a Sp echt series for M
/
/; that is/, a /ltration of M
/
with
eac h comp osition factor isomorphic to a Sp ec h t mo dule/.
/4/./1/1 Corollary L et / b e a c omp osition of n /. Then/, as an H /{mo dule/, M
/
has a
/ltr ation M
/
/= M
/1
/> M
/2
/> / / / /> M
k /+/1
/= /0 such that for i /= /1 /; /2 /; /: /: /: /; k ther e
exists a p artition /
i
of n with M
i
/= M
i /+/1
/
/=
S
/
i
/. Mor e over/, for e ach p artition / the
numb er of /
i
e qual to / is the numb er of semistandar d / /{table aux of typ e / /.
Pro of/. Let f S
/1
/; /: /: /: /; S
k
g b e the set of semistandard tableaux of t yp e / where
S
i
/2 T
/0
/( /
i
/; / /) and /
i
D /
j
whenev er i /> j /. F or i /= /1 /; /2 /; /: /: /: /; k /+ /1 let M
i
b e the
R /{mo dule of M
/
with basis f m
S
j
t
j i / j / k and t /2 Std/( /
j
g /. Then
M
/
/= M
/1
/> M
/2
/> / / / /> M
k
/> M
k /+/1
/= /0
and b y Theorem /3/./1/8 eac h M
i
is a righ t H /{mo dule/.
Fix an in teger i with /1 / i / k /. Then M
i
/\
/
H
/
i
/ M
i /+/1
/. Consequen tly /,
there is a w ell/{de/ned homomorphism / /: S
/
i
/? /! M
i
/= M
i /+/1
of H /{mo dules giv en b y
/ /( m
t
/) /= m
S
i
t
/+ M
i /+/1
for all t /2 Std/( / /)/. The map / is certainly surjectiv e/; moreo v er/,
b oth mo dules ha v e the same rank/, so / is an isomorphism/.
The last result in this section requires some more notation/. Let / b e a partition
of n and let / and / b e comp ositions of n /. Supp ose that S /2 T
/0
/( //; / /) and T /2
T
/0
/( //; / /)/. No w de/ne
m
ST
/=
X
s /; t
m
st
where the sum is o v er all pairs /( s /; t /) of standard / /{tableaux suc h that / /( s /) /= S and
/ /( t /) /= T /. Then/, b y /(/4/./7/)/, m
ST
/2 M
/
/\ M
/ /
/. This allo ws us to pro v e the follo wing
result whose imp ortance deriv es from Corollary /4/./9/.
/4/./1/2 Corollary Supp ose that / and / ar e c omp ositions of n /. Then M
/
/\ M
/ /
is
fr e e as an R /{mo dule with b asis
n
m
ST
/
/
/
S /2 T
/0
/( //; / /) and T /2 T
/0
/( //; / /)
for some p artition / of n
o
/:
Pro of/. Supp ose that h is a non/{zero elemen t of M
/
/\ M
/ /
/. Then/, with resp ect to
the Murph y basis of H w e ma y write h /=
P
r
st
m
st
for some r
st
/2 R /. No w h /2 M
/
/,
so b y Theorem /4/./1/0 if r
st
/6/= /0 then / /( s /) is semistandard and r
st
/= r
s
/0
t
whenev er
/ /( s /) /= / /( s
/0
/)/. Similarly /, b ecause h /2 M
/ /
if r
st
/6/= /0 then / /( t /) is semistandard and
r
st
/= r
st
/0
whenev er / /( t /) /= / /( t
/0
/)/. Consequen tly /, if / /( s /) /= / /( s
/0
/) and / /( t /) /= / /( t
/0
/)
then r
st
/= r
s
/0
t
/= r
s
/0
t
/0
/. The result follo ws/.
/3/. The semistandard basis theorem
W e are no w ready to pro v e that the q /{Sc h ur algebras are cellular/. In fact/, w e
shall see that they are quasi/{hereditary /.
Recall that //( d/; n /) is the set of comp ositions and let /
/+
/( d/; n /) b e the set of
partitions con tained in //( d/; n /)/. Supp ose that / /2 /
/+
/( d/; n /)/, //; / /2 //( d/; n /) and that
/3/. THE SEMIST AND ARD BASIS THEOREM /4/1
S /2 T
/0
/( //; / /) and T /2 T
/0
/( //; / /)/. By Corollary /4/./1/2/, m
ST
/2 M
/
/\ M
/ /
so w e can de/ne
/'
ST
to b e the elemen t of S /( d/; n /) giv en b y
/4 /: /1/3 /'
ST
/( m
/
h /) /= /
//
m
ST
h for all / /2 //( d/; n /) and h /2 H /:
F or an y partition / /2 /
/+
/( d/; n /) let T
/0
/( / /) /=
S
/ /2 //( d/;n /)
T
/0
/( //; / /) and de/ne
/
S
/
/( d/; n /) to b e the R /{submo dule of S /( d/; n /) spanned b y the homomorphism s /'
ST
where S /; T /2 T
/0
/( / /) for some / /2 /
/+
/( d/; n /) suc h that / B / /. Similarly /, S
/
/( d/; n /) is
the R /{submo dule spanned b y the maps /'
ST
where S /; T /2 T
/0
/( / /) and / D / /.
/4/./1/4 The Semistandard Basis Theorem /(R/. Green/) The q /{Schur algebr a is
fr e e as an R /{mo dule with b asis
/ /=
n
/'
ST
/
/
/
/ /2 /
/+
/( d/; n /) and S /; T /2 T
/0
/( / /)
o
/:
Mor e over/,
/(i/) The R /{line ar map / /: S /( d/; n /) /? /! S /( d/; n /) determine d by /'
/
ST
/= /'
TS
/, for al l
S /; T /2 T
/0
/( / /) and al l / /2 /
/+
/( d/; n /) /, is an anti/{isomorphism of S /( d/; n /) /.
/(ii/) Supp ose that / /2 /
/+
/( d/; n /) and that T is a semistandar d / /{table au/. Then for
al l /' /2 S /( d/; n /) ther e exist r
V
/2 R such that for al l S /2 T
/0
/( / /)
/'
ST
/' /
X
V /2T
/0
/( / /)
r
V
/'
SV
mo d
/
S
/
/( d/; n /) /:
Conse quently/, /(/ /; /
/+
/( d/; n /)/) is a c el lular b asis of S /( d/; n /) /.
Pro of/. Com bining Corollary /4/./9 and Corollary /4/./1/2 sho ws that S /( d/; n /) is free as
an R /{mo dule with basis //. It remains to v erify /(i/) and /(ii/)/.
Let / b e a partition in /
/+
/( d/; n /) and supp ose that S /2 T
/0
/( //; / /) and T /2 T
/0
/( //; / /)/.
Then /'
/
ST
/( m
/
/) /= m
/
ST
/= m
TS
/=
/?
/'
TS
/( m
/
/)
/
/
/. No w supp ose that / /2 /
/+
/( d/; n /)/, U /2
T
/0
/( //; / /) and V /2 T
/0
/( //; / /)/. W e ma y assume that / /= / since otherwise /'
ST
/'
UV
/= /0/.
W rite m
ST
/= h
S
m
/
and m
UV
/= h
U
m
/
for h
S
/; h
U
/2 H /. Then
/( /'
ST
/'
UV
/)
/
/( m
/
/) /=
/?
/'
ST
/'
UV
/( m
/
/)
/
/
/=
/?
h
S
h
U
m
/
/)
/
/= m
/
h
/
U
h
/
S
/= /'
VU
/( m
/
/) h
/
S
/= /'
VU
/( m
/
h
/
S
/) /= /'
VU
/'
TS
/( m
/
/) /:
Hence/, /( /'
ST
/'
UV
/)
/
/= /'
/
UV
/'
/
ST
and / is an an ti/{isomorphism /, pro ving /(i/)/.
No w consider /(ii/)/. W e ma y assume that /' /2 Hom
H
/( M
/
/; M
/
/) for some / /2
//( d/; n /)/. By Corollary /4/./9 there exists an h /2 H suc h that /' /( m
/
/) /= m
/
h /; so/,
/'
ST
/' /( m
/
/) /= m
ST
h /. No w m
ST
h is an elemen t of M
/
/\ M
/
/
so b y Theorem /4/./1/0
w e ma y write m
ST
h /=
P
r
UV
m
UV
where r
UV
/2 R and the sum is o v er pairs /( U /; V /)
of semistandard / /{tableaux where / /2 /
/+
/( d/; n /)/. Therefore/, b y Theorem /3/./1/8/(ii/)/,
there exist r
V
/; r
U
/0
V
/0
/2 R suc h that
m
ST
h /=
X
V /2T
/0
/( //;/ /)
r
V
m
SV
/+
X
/ /2 /
/+
/( d/;n /)
/ B /
X
U
/0
/2T
/0
/( //;/ /)
V
/0
/2T
/0
/( //;/ /)
r
U
/0
V
/0
m
U
/0
V
/0
/:
Hence/, /'
ST
/' /
X
V /2T
/0
/( //;/ /)
r
V
/'
SV
mo d
/
S
/
/( d/; n /)/, whic h pro v es /(ii/)/.
W e call / the semistanda rd basis of S /( d/; n /) /.
No w that w e ha v e a cellular basis of the q /{Sc h ur algebra w e can describ e its
irreducible represen tations o v er a /eld/. T raditionally /, the cell mo dules of S /( d/; n /)
are called W eyl mo dules/.
/4/2 /4/. THE q /{SCHUR ALGEBRA
Let / /2 /
/+
/( d/; n /) b e a partition and recall that T
/
/= / /( t
/
/) is the unique
semistandard / /{tableau of t yp e / /. F rom the de/nitions one sees that /'
T
/
T
/
restricts
to the iden tit y map on M
/
/.
The W eyl mo dule W
/
is the righ t S /( d/; n /) /{mo dule /(
/
S
/
/( d/; n /) /+ /'
T
/
T
/ /) S /( d/; n /)/.
Th us/, W
/
is a submo dule of S /( d/; n /) /=
/
S
/
/( d/; n /) and whic h/, as an R /{mo dule/, is free
with basis f
/
S
/
/( d/; n /) /+ /'
T
/
T
j T /2 T
/0
/( / /) g /.
There is another description of W
/
whic h is more con v enien t for our purp oses/.
Giv en a semistandard / /{tableau T of t yp e / let m
T
/=
P
t
m
t
/, where the sum
is o v er those standard tableau t suc h that / /( t /) /= T /. Then m
T
/2 S
/
/. De/ne
/'
T
to b e homomorphism in Hom
H
/( M
/
/; S
/
/) giv en b y /'
T
/( m
/
/) /= m
T
/. Note that
Hom
H
/( M
/
/; S
/
/) b ecomes a righ t S /( d/; n /)/{mo dule under comp osition of maps/.
/4/./1/5 Prop ositi on L et / /2 /
/+
/( d/; n /) b e a p artition of n /. Then ther e is a c anonic al
isomorphism of S /( d/; n /) /{mo dules
W
/
/
/=
M
/ /2 //( d/;n /)
Hom
H
/( M
/
/; S
/
/) given by
/
S
/
/( d/; n /) /+ /'
T
/
T
/7/? /! /'
T
/;
for al l T /2 T
/0
/( / /) /.
Pro of/. Let M /=
L
/ /2 //( d/;n /)
M
/
and
/
M
/
/=
L
/ /2 //( d/;n /)
/
H
/
/\ M
/
/. Eac h homo/-
morphism /' in
/
S
/
/( d/; n /) maps M in to
/
M
/
/; so w e ma y regard S /( d/; n /) /=
/
S
/
/( d/; n /) as
a set of maps from M in to M /=
/
M
/
/. In this w a y /, if T is a semistandard / /{tableau
then the homomorphi sm
/
S
/
/( d/; n /) /+ /'
T
/
T
can b e regarded as the map from M
/
in to M /=
/
M
/
whic h sends m
/
to
/
M
/
/+ m
T
/
T
/. By the third isomorphism theorem/,
/(
/
M
/
/+ M
/
/) /=
/
M
/
/
/=
M
/
/= /(
/
M
/
/\ H
/
/) /= M
/
/= /(
/
H
/
/\ M
/
/)
/
/=
/(
/
H
/
/+ M
/
/) /=
/
H
/
/:
Ho w ev er/, /(
/
H
/
/+ M
/
/) /=
/
H
/
/= S
/
so this sho ws that
/
S
/
/( d/; n /) /+ /'
T
/
T
can b e iden/-
ti/ed with the homom orphism /'
T
as claimed/. Consequen tly /, the map giv en in the
statemen t of the Prop osition is an S /( d/; n /) /{mo dule isomorphism from W
/
in to the
R /{mo dule spanned b y f /'
T
j T /2 T
/0
/( / /) g /. Con v ersely /, giv en /' /2 Hom
H
/( M
/
/; S
/
/)/,
the ab o v e iden ti/cations sho w that w e can de/ne an elemen t /^/' of W
/
b y requiring
that /^/' /( m
/
h /) /= /' /( m
/
/) h for all h /2 H /. Hence/, f /'
T
j T /2 T
/0
/( / /) g m ust span the
S /( d/; n /) /{mo dule
L
/
Hom
H
/( M
/
/; S
/
/)/. The Prop osition follo ws/.
Hereafter/, w e iden tify W
/
and
L
/
Hom
H
/( M
/
/; S
/
/)/. In particular/, w e will call
f /'
T
j T /2 T
/0
/( / /) g the semistanda rd basis of W
/
/.
As in Chapter /2/, the W eyl mo dule W
/
p ossesses an asso ciativ e symmetric
bilinear form whic h is completely determined b y the equation
h /'
S
/; /'
T
i /'
T
/
T
/ / /'
T
/
S
/'
TT
/ mo d
/
S
/
/( d/; n /)
for all S /; T /2 T
/0
/( / /)/. In particular/, h /'
S
/; /'
T
i /= /0 unless S and T are semistandard
tableaux of the same t yp e/.
Let L
/
/= W
/
/= rad W
/
where/, once again/, rad W
/
is the set of elemen ts x /2 W
/
suc h that h x/; y g /= /0 for all y /2 W
/
/.
/4/./1/6 Theorem /(Dipp er/{James/) Supp ose that R is a /eld/.
/(i/) L et / b e a p artition in /
/+
/( d/; n /) /. Then L
/
is an absolutely irr e ducible S /( d/; n /) /{
mo dule/.
/(ii/) f L
/
j / /2 /
/+
/( d/; n /) g is a c omplete set of non/{isomorphic irr e ducible S /( d/; n /) /{
mo dules/.
/3/. THE SEMIST AND ARD BASIS THEOREM /4/3
Pro of/. W e ha v e already remark ed that /'
T
/
T
/ is the iden tit y map on M
/
/. There/-
fore/, w e compute that
h /'
T
/ /; /'
T
/ i /'
T
/
T
/ / /'
T
/
T
/ /'
T
/
T
/ /= /'
T
/
T
/ mo d
/
S
/
/( d/; n /)/;
so h /'
T
/ /; /'
T
/ i /= /1/. In particular/, L
/
/6/= /0/. P arts /(i/) and /(ii/) no w follo w from
Theorem /2/./1/3/.
/4/./1/7 Corollary /(P arshall/{W ang/) Supp ose that R is a /eld/. Then S /( d/; n /) is
quasi/{her e ditary/.
Pro of/. This is immediate from Theorem /4/./1/6/(ii/) and Corollary /2/./1/9/.
Giv en t w o partitions / and / in //( d/; n /) let d
//
/= /[ W
/
/: L
/
/] b e the comp osition
m ultiplicit y of the simple mo dule L
/
in W
/
/. Corollary /2/./1/4 yields the next result/.
/4/./1/8 Corollary Supp ose that R is a /eld and let / and / b e p artitions in /
/+
/( d/; n /) /.
Then d
//
/= /1 and if d
//
/> /0 then / B / /.
In Chapter /3 w e de/ned d
//
to b e the decomp osition m ultiplicit y /[ S
/
/: D
/
/]/;
w e close this c hapter b y in v estigating more closely the links b et w een the Iw ahori/{
Hec k e algebras and the q /{Sc h ur algebras when d / n /. In particular/, w e sho w that
if / is e /{restricted then /[ S
/
/: D
/
/] /= /[ W
/
/: L
/
/]/; th us/, the notation d
//
is consisten t
in this case/. /(If these t w o sets of decomp osition n um b ers b eing equal w orries y ou/,
reread the w arning on page /2/5/./)
F or the remainder of this section w e assume that /! /2 /
/+
/( d/; n /)/; or equiv alen tly /,
that d / n /. In this case/, Hom
H
/( H /; H /) is an R /{submo dule of S /( d/; n /)/. F urther/-
more/, there is a canonical isomorphism of R /{mo dules H
/
/=
Hom
H
/( H /; H /) giv en
b y h /7/? /! /
h
where /
h
is the homom orphism giv en b y left m ultiplicati on b y h /. In
fact/, H
/
/=
/'
T
/!
T
/!
S /( d/; n /) /'
T
/!
T
/!
since giv en standard / /{tableaux S /2 T
/0
/( //; / /) and
T /2 T
/0
/( //; / /) w e ha v e that /'
T
/!
T
/!
/'
ST
/'
T
/!
T
/!
/= /
/! /
/
/ /!
/'
ST
/.
Noting that /'
T
/!
T
/!
is idemp oten t in S /( d/; n /) /, w e can de/ne a functor from the
category of righ t S /( d/; n /) /{mo dules to the category of righ t H /{mo dules/; the Schur
functo r is the functor whic h sends a righ t S /( d/; n /) /{mo dule M to M /'
T
/!
T
/!
/.
/4/./1/9 Prop ositi on Supp ose that R is a /eld and that d / n /. L et / b e a p artition
of n /. Then/, as right H /{mo dules/,
/(i/) W
/
/'
T
/!
T
/!
/
/=
S
/
/;
/(ii/) L
/
/'
T
/!
T
/!
/
/=
D
/
/.
F urthermor e/, if / is an e /{r estricte d p artition of n then /[ W
/
/: L
/
/] /= /[ S
/
/: D
/
/] /.
Pro of/. Supp ose that T is a standard / /{tableau of t yp e / /. Then /'
T
/'
T
/!
T
/!
/= /0
unless / /= /! and/, if / /= /! /, then T /= t is a standard / /{tableau and /'
T
/'
T
/!
T
/!
/= /'
t
/.
Consequen tly /, W
/
/'
T
/!
T
/!
is free as an R /{mo dule with basis f /'
t
j t /2 Std/( / /) g and
the map W
/
/'
T
/!
T
/!
/! S
/
whic h sends /'
t
to /'
t
/( m
/!
/) /= m
t
is an isomorphism /(cf/.
Prop osition /4/./1/5/)/.
P art /(ii/) of the Prop osition no ws follo ws from Theorem /3/./3/9/(ii/) and Corol/-
lary /4/./1/8/. In particular/, this sho ws that if L
/
/'
T
/!
T
/!
/6/= /0 then / is e /{restricted/.
Finally /, let W
/
/= W
/1
/> / / / /> W
k
/> /0 b e a comp osition series for W
/
/.
Then S
/
/
/=
W
/1
/'
T
/!
T
/!
/ / / / / W
k
/'
T
/!
T
/!
/ /0 giv es an H /{mo dule /ltration
of S
/
with quotien ts W
i
/'
T
/!
T
/!
/=W
i /+/1
/'
T
/!
T
/!
/
/=
/( W
i
/=W
i /+/1
/) /'
T
/!
T
/!
/
/=
L
/
i
/'
T
/!
T
/!
for
some partitions /
i
/. By the last paragraph/, L
/
i
/'
T
/!
T
/!
is simple when /
i
is e /{
restricted and zero otherwise/. Therefore/, b y omitting the mo dules W
i
/'
T
/!
T
/!
suc h
/4/4 /4/. THE q /{SCHUR ALGEBRA
that W
i
/'
T
/!
T
/!
/
/=
W
i /+/1
/'
T
/!
T
/!
w e obtain a comp osition series for S
/
whic h has the
required m ultipli cities/. This pro v es /(iii/)/.
Finally /, let M /=
L
/ /2 //( d/;n /)
M
/
/. Then M is naturally a left S /( d/; n /) /{mo dule
with action /' / m /= /' /( m /) for all /' /2 S /( d/; n /) and all m /2 M /. Of course/, M is also
a righ t H /{mo dule and it is clear that the actions of S /( d/; n /) and H comm ute/.
/4/./2/0 Theorem /(The double cen tralizer prop ert y/) Supp ose that d / n /. Then
S /( d/; n /)
/
/=
End
H
/
M
/ /2 //( d/;n /)
M
/
/
and H
/
/=
End
S /( d/;n /)
/
M
/ /2 //( d/;n /)
M
/
/
/:
Pro of/. The /rst isomorphism is just the de/nition of the q /{Sc h ur algebra/, so there
is nothing to pro v e here/. F or the second isomorphism/, notice that b y Corollary /4/./9
for an y comp osition / w e ha v e M
/
/= M
/
/\ H
/
/
/=
Hom /( H /; M
/
/)/. In fact/, w e claim
that as H /{mo dules /'
T
/
T
/
S /( d/; n /) /'
T
/!
T
/!
/
/=
M
/
/. T o see this /rst notice that b y
Theorem /4/./1/4/, the R /{mo dule /'
T
/
T
/
S /( d/; n /) /'
T
/!
T
/!
has basis f /'
S t
g where S /2 T
/0
/( //; / /)
and t /2 Std/( / /) for some / /2 /
/+
/( d/; n /)/. Hence/, the R /{linear map determined b y
/'
S t
/7/? /! /'
S t
/( m
/
/) is an isomorphism b y Theorem /4/./1/0/. Consequen tly /,
M
/ /2 //( d/;n /)
M
/
/
/=
M
/ /2 //( d/;n /)
Hom
H
/( H /; M
/
/)
/
/=
M
/ /2 //( d/;n /)
/'
T
/
T
/
S /( d/; n /) /'
T
/!
T
/!
/:
Ho w ev er/,
P
/
/'
T
/
T
/
is the iden tit y elemen t of the q /{Sc h ur algebra so/, as an S /( d/; n /) /{
mo dule/,
L
/
M
/
/
/=
S /( d/; n /) /'
T
/!
T
/!
/. Therefore/, as algebras/,
End
S /( d/;n /)
/
M
/
M
/
/
/
/=
End
S /( d/;n /)
/
S /( d/; n /) /'
T
/!
T
/!
/
/
/=
/'
T
/!
T
/!
S /( d/; n /) /'
T
/!
T
/!
/;
the last isomorphism coming from Lemma /2/./2/0/. Since H and /'
T
/!
T
/!
S /( d/; n /) /'
T
/!
T
/!
are canonically isomorphic/, the Theorem follo ws/.
In fact/, the argumen t sho ws that the isomorphism s in the Theorem are canon/-
ical/.
Notes on Chapter /4
/1/. The q /{Sc h ur algebra w as in tro duced b y Dipp er and James in /[ /1/5 /] where they
sho w ed that it completely determined the represen tation theory of the /nite
general linear groups in non/{de/ning c haracteristic/. This mirrors the classical
theory /, for whic h the reader is referred to Green/'s excellen t b o ok /[ /2/7 /]/.
/2/. Beilinson/, Lusztig and MacPherson /[ /3 /] ha v e de/ned the q /{Sc h ur algebra using
the geometry of the general linear groups /(that these de/nitions coincide sho wn
b y Du /[ /1/9 /]/) and sho w ed that there is a natural surjection from the quan tum
general linear group U
q
/( g l
d
/) on to S /( d/; n /) /. Latter P arshall and W ang /[ /5/8 /] /(see
also Dipp er and Donkin /[ /1/2 /]/) sho w ed ho w to construct U
q
/( g l
d
/) from the q /{Sc h ur
algebras/. F or details consult Brundan /[ /5 /] and Donkin /[ /1/8 /]/.
/3/. A semistandard basis theorem for the W eyl mo dules of the q /{Sc h ur algebra w as
/rst pro v ed b y Dipp er and James /[ /1/6 /]/; the treatmen t here is considerably easier
and is based on /[ /1/7 /]/.
NOTES ON CHAPTER /4 /4/5
/4/. In a di/eren t guise/, the semistandard basis of the Sc h ur algebra /(i/.e/. the case
q /= /1/)/, /rst app eared as J/. A/. Green/'s /[ /2/8 /] co determinan t basis/; shortly after/-
w ards/, W o o dco c k /[ /6/2 /] ga v e a more direct pro of/. Ric hard Green /[ /2/9 /] generalized
W o o dco c ks argumen t to giv e a q /{analogue of the co determinan t basis/; it turns
out that this basis is the semistandard basis of Theorem /4/./1/4/. The construction
of the semistandard basis giv en here is based /[ /1/7 /] and is v ery di/eren t from
Green/'s/; that the semistandard basis and the Murph y basis are related w as /rst
observ ed b y Du and Scott /[ /2/1 /]/.
/5/. In /[ /1/8 /] Donkin parameterizes the irreducible mo dules of the /0/{Sc h ur algebra
o v er a /eld and also giv es an explicit c haracter form ula for the simple mo dules/.
As one migh t exp ect/, the /0/{Sc h ur algebra is not quasi/{hereditary/; surprisingly /,
ho w ev er/, it is a quasi/{F rob enius algebra /(at least when d / n /)/.
/6/. It is sho wn in /[ /1/0 /, /6/1/./2/] that whenev er A is a quasi/{F rob enius algebra/, a /2 A
and J is an ideal of A then Hom
A
/( J /; aA /)
/
/=
J /\ aA /. By Prop osition /1/./1/4/, H is
quasi/{F rob enius so this giv es another pro of of Corollary /4/./9/. /(See also /[ /1/7 /, x /5/]/./)
/7/. P arshall and W ang /[ /5/8 /] /rst sho w ed that the q /{Sc h ur algebra is quasi/{hereditary /.
In particular/, this implies that the q /{Sc h ur algebras ha v e /nite global dimension/;
this dimension has b een explicitly calculated b y Donkin /[ /1/8 /] when d / n /.
/8/. The double cen tralizer prop ert y /(/4/./2/0/) is normally phrased in terms of actions
of S /( d/; n /) and H up on /\ q /{tensor space/"/; see /[ /5 /, /1/6 /]/.
CHAPTER /5
The Jan tzen/{Sc hap er theorem
In this c hapter w e pro v e an analogue of the Jan tzen sum form ula for the q /{
Sc h ur algebra/. This is a strong result describing the structure of W eyl mo dules/;
ho w ev er/, its pro of follo ws from the calculation of Gram determinan ts/. As our main
application of this result w e classify the blo c ks of H /.
/1/. The Gram determinan t of W
/
Throughout this section w e /x a partition / /2 /
/+
/( d/; n /) and a comp osition / /2
//( d/; n /)/. The / /{ w eight space of the W eyl mo dule W
/
is W
/
/
/= W
/
/'
T
/
T
/
/; it is the free
R /{submo dule of S /( d/; n /) with basis f /'
T
j T /2 T
/0
/( //; / /) g and/, b y Prop osition /4/./1/5/,
W
/
/
/
/=
Hom
H
/( M
/
/; S
/
/)/. The aim of this section is to compute the Gram determinant
G
/
/
/= det
/?
h /'
S
/; /'
T
i
/
of W
/
/
/, where and S and T run o v er T
/0
/( //; / /) in some /xed order/.
Supp ose that k is an in teger with /1 / k / d and let x/; x /+ /1 /; /: /: /: /; y b e the
en tries in ro w k of t
/
/. Prop osition /3/./2/4/(iii/) sho ws that
/5 /: /1 /( L
x
/+ L
x /+/1
/+ / / / L
y
/) m
/
/= m
/
/( L
x
/+ L
x /+/1
/+ / / / L
y
/) /:
Hence/, w e can de/ne a map L
/
i
/: M
/
/? /! M
/
b y sp ecifying that
L
/
k
/( m
/
h /) /= /( L
x
/+ L
x /+/1
/+ / / / /+ L
y
/) m
/
h/;
for all h /2 H /. Note that L
/!
k
is just left m ultiplication b y L
k
/, so these elemen ts
are a generalization of the Jucys/{Murph y elemen ts of Chapter /2/. F urthermore/, L
/
k
and L
/
j
comm ute for all j and k b y Prop osition /3/./2/4/(iv/)/.
Let T /2 T
/0
/( //; / /)/. As in /(/3/./5/)/, if k is an in teger let T /# k b e the tableau obtained
from T b y deleting all en tries greater than k /. Then/, extending the dominance
ordering on tableaux of t yp e /! w e write S D T if Shap e /( S /# k /) D Shap e /( T /# k /) for
k /= /1 /; /2 /; /: /: /: /; n /. It follo ws from Prop osition /3/./3 and Prop osition /4/./5 that S D T if
and only if d /(/rst/( S /)/) D d /(/rst/( T /)/.
Finally /, let /[res
T
/( k /)/]
q
/=
X
x /2 /[ / /]
/[res
T
/( x /)/]
q
/; where the sum is o v er those no des x
suc h that T /( x /) /= k /(see /(/3/./2/8/)/)/.
/5/./2 Example Supp ose that e /= /3 and let / /= /(/3 /; /2/) and / /= /(/2
/2
/; /1/)/. Then
T
/0
/( //; / /) /= f S /; T g where S /=
/1 /1 /2
/2 /3
and T /=
/1 /1 /3
/2 /2
/. F rom the de/nitions/, S B T /,
/[res
S
/(/1/)/]
q
/= /[/0/]
q
/+ /[/1/]
q
/, /[res
S
/(/2/)/]
q
/= /[/2/]
q
/+ /[/2/]
q
and /[res
S
/(/3/)/]
q
/= /[/0/]
q
/.
/5/./3 Theorem /(James/{Mathas/) Supp ose that T /2 T
/0
/( //; / /) and let k b e an inte ger
with /1 / k / d /. Then
/'
T
L
/
k
/= /[res
T
/( k /)/]
q
/'
T
/+
X
S B T
r
S
/'
S
/;
for some r
S
/2 R /.
/4/6
/1/. THE GRAM DETERMINANT OF W
/
/4/7
Pro of/. Let t /= last/( T /)/; then m
T
/= m
t
/+
P
s B t
m
s
where the sum is o v er those
standard / /{tableaux suc h that / /( s /) /= T /. Therefore/, b y Theorem /3/./3/0/,
/'
T
L
/
k
/( m
/
/) /= m
T
/( L
x
/+ / / / /+ L
y
/)
/=
/
m
t
/+
X
s B t /: / /( s /)/= T
m
s
/
/( L
x
/+ / / / /+ L
y
/)
/= /[res
T
/( k /)/]
q
m
t
/+
X
s B t
b
s
m
s
/;
for some b
s
/2 R /. Ho w ev er/, /'
T
/
T
L
/
k
/( m
/
/) /2 M
/
/\ M
/ /
so b y Corollary /4/./1/2 there
exist b
S
/2 R suc h that
/'
T
L
/
k
/( m
/
/) /= /[res
T
/( k /)/]
q
m
T
/+
X
S B T
b
S
m
S
/:
Hence/, /'
T
L
/
k
/= /[res
T
/( k /)/]
q
/'
T
/+
P
S B T
b
S
/'
S
pro ving the Theorem/.
Recall that e is the smallest p ositiv e in teger /(or e /= /1 /) suc h that /[ e /]
q
/= /0/.
Just as in section /3 of Chapter /3/, un til further notice w e assume that R is a /eld
and that e /> n /. An argumen t similar to that of Lemma /3/./3/2 pro v es the follo wing/.
/5/./4 Lemma Supp ose that R is a /eld and that e /> n /. L et S and T b e two semi/-
standar d / /{table aux of typ e / /. Then /[res
S
/( k /)/]
q
/6/= /[res
T
/( k /)/]
q
for some inte ger k /.
Exactly as in /(/3/./3/1/)/, for an y semistandard / /{tableau T of t yp e / let
F
T
/=
Y
k / /1
Y
S /2T
/0
/( //;/ /)
/[res
S
/( k /)/]
q
/6/=/[res
T
/( k /)/]
q
L
/
k
/? /[res
S
/( k /)/]
q
/[res
S
/( k /)/]
q
/? /[res
T
/( k /)/]
q
and de/ne / 
T
/= /'
T
F
T
/.
Because of Theorem /5/./3 and Lemma /5/./4 the pro of of Prop osition /3/./3/3 can no w
b e rep eated/, w ord for w ord/, to pro v e the follo wing result/.
/5/./5 Prop ositio n Supp ose that R is a /eld and that e /> n /. L et T b e a semistandar d
/ /{table au of typ e / /. Then
/(i/) Ther e exist a
S
/2 R such that / 
T
/= /'
T
/+
P
S B T
a
S
/'
S
/.
/(ii/) If S B T then /'
S
/ 
T
/= /0 /.
/(iii/) F or k /= /1 /; /: /: /: /; n /, / 
T
L
k
/= /[res
T
/( k /)/]
q
/ 
T
/.
/(iv/) F or any S /2 Std /( / /) /, / 
T
F
S
/= /
ST
/ 
T
/.
/5/./6 Corollary f / 
T
j T /2 T
/0
/( //; / /) g is an ortho gonal b asis of W
/
/
/.
Pro of/. That f / 
T
j T /2 T
/0
/( //; / /) g is a basis of W
/
/
is imm ediate from part /(i/) of
the Prop osition/. Using part /(iv/) w e /nd that for an y semistandard / /{tableaux S
and T of t yp e / w e ha v e h / 
S
/; / 
T
i /= h /'
S
F
S
/; / 
T
i /= h /'
S
/; / 
T
F
S
i /= /
ST
h /'
S
/; / 
S
i /; pro ving
the Corollary /.
In order to compute the Gram determinan t G
/
/
of W
/
/
w e determine the inner
pro ducts h / 
T
/; / 
T
i for all T /2 T
/0
/( //; / /)/. F or this w e need some com binatorics/.
Let T b e a semistandard / /{tableau of t yp e / /. F or eac h no de /( i/; j /) /2 /[ / /] let
/?
T
/( i/; j /) /= f /( k /; l /) /2 /[ / /] j l /< j/; T /( k /; l /) /< T /( i/; j /) and T /( k
/0
/; l /) /> T /( i/; j /) for all k
/0
/> k g
/4/8 /5/. THE JANTZEN/{SCHAPER THEOREM
and let
/
T
/( q /) /=
Y
/( i/;j /) /2 /[ / /]
Y
/( k /;l /) /2 /?
T
/( i/;j /)
/[ j /? i /+ k /? l /+ /1/]
q
/[ j /? i /+ k /? l /]
q
/:
Most of the time w e omit the q and simply write /
T
/.
Supp ose that is t is a standard / /{tableau and let x /= /( i/; j /) and y /= /( k /; l /)/. Then
res
t
/( x /) /? res
t
/( y /) /= j /? i /+ l /? k is the /\axial distance/" from x to y in the diagram
of / /.
/5/./7 Example Supp ose that / /= /(/3 /; /2/) and let t /=
/1 /2 /4
/3 /5
/, S /=
/1 /1 /2
/2 /3
and T /=
/1 /1 /3
/2 /2
/.
Then
/
t
/=
/[/2/]
q
/[/1/]
q
/
/[/2/]
q
/[/1/]
q
/[/4/]
q
/[/3/]
q
/
/[/2/]
q
/[/1/]
q
/; /
S
/=
/[/2/]
q
/[/1/]
q
/[/2/]
q
/[/1/]
q
and /
T
/=
/[/3/]
q
/[/2/]
q
/[/4/]
q
/[/3/]
q
/:
Notice that if / /= /(/2
/2
/; /1/) then T
/0
/( //; / /) /= f S /; T g and /
S
/
T
/= /[/2/]
q
/[/4/]
q
/, so /
S
/
T
/2 Z /[ q /]/.
Recall that /[ m /]
/!
q
/= /[/1/]
q
/: /: /: /[ m /]
q
/. F or an y partition / /= /( /
/1
/; /: /: /: /; /
k
/) w e also
let /[ / /]
/!
q
/= /[ /
/1
/]
/!
q
/: /: /: /[ /
k
/]
/!
q
/.
/5/./8 Lemma L et / /2 /
/+
/( d/; n /) /. Then /
t
/ /= /[ / /]
/!
q
/.
Pro of/. When n /= /1 then / /= /(/1/) and /
t
/ /= /1 so the Lemma is correct/. No w
supp ose that n /> /1 and let / /= /( /
/1
/; /: /: /: /; /
r
/)/, where /
r
/> /0/, and let / b e the
partition /( /
/1
/; /: /: /: /; /
r
/? /1/)/. By induction/, /
t
/
/= /[ / /]
/!
q
/. Consequen tly /,
/
t
/
/= /
t
/
/
/[/2/]
q
/[/1/]
q
/ / /
/[ /
r
/]
q
/[ /
r
/? /1/]
q
/= /[ / /]
/!
q
/[ /
r
/]
q
/= /[ / /]
/!
q
/;
completing the pro of/.
/5/./9 Lemma Supp ose that s and t ar e standar d / /{table au such that s B t and
s /= t /( i/; i /+ /1/) for some inte ger i with /1 / i /< n /. Then /
t
/= q
/? /1
/( q /+ / /)/(/1 /? / /) /
s
wher e /
/? /1
/= /[res
s
/( i /) /? res
t
/( i /)/]
q
/.
Pro of/. By de/nition/, if /( a/; b /) /2 /[ / /] then the sets /?
s
/( a/; b /) and /?
t
/( a/; b /) are equal
unless s /( a/; b /) /= i /. F urthermore/, if s /( a/; b /) /= i and s /( c/; d /) /= i /+ /1 then a /> c and
d /< b so /?
s
/( a/; b /) /[ f /( c /? /1 /; d /) g /= /?
t
/( a/; b /) /[ f /( c/; d /) g /; where b oth unions are disjoin t/.
It follo ws that
/
t
/=
/[res
s
/( i /) /? res
t
/( i /) /+ /1/]
q
/[res
s
/( i /) /? res
t
/( i /)/]
q
/
/[res
s
/( i /) /? res
t
/( i /) /? /1/]
q
/[res
s
/( i /) /? res
t
/( i /)/]
q
/ /
s
/= q
/? /1
/( q /+ / /)/(/1 /? / /) /
s
as required/.
/5/./1/0 Prop ositi on L et t b e a standar d / /{table aux/. Then h / 
t
/; / 
t
i /= q
/` /( d /( t /)/)
/
t
/.
Pro of/. Supp ose /rst that t /= t
/
/; then / 
t
/ /= /'
t
/ b y Prop osition /5/./5/(i/)/. By
de/nition/, h / 
t
/ /; / 
t
/ i /'
T
/
T
/ / /'
T
/
t
/ /'
t
/
T
/ mo d
/
S
/
/( d/; n /)/, and
/'
T
/
t
/
/'
t
/
T
/
/( m
/
/) /= /'
T
/
t
/
/( m
/
/) /= /'
T
/
t
/
/(/1/) m
/
/= m
/
m
/
/= /[ / /]
/!
q
m
/
b y Lemma /3/./2/. Th us/, h / 
t
/ /; / 
t
/ i /= /
t
/ b y Lemma /5/./8/.
No w supp ose that t /6/= t
/
/. Then there exists a standard / /{tableau s suc h that
s B t and s /= t /( i/; i /+ /1/) for some i /. F urthermore/, b y Theorem /3/./3/4/, f
s
T
i
/= f
t
/? /f
s
/,
/1/. THE GRAM DETERMINANT OF W
/
/4/9
where /
/? /1
/= /[res
s
/( i /) /? res
t
/( i /)/]
q
/. Therefore/, / 
t
/= / 
s
T
i
/+ // 
s
since / 
v
/(/1/) /= f
v
for
all v /2 Std/( / /)/; consequen tly /,
h / 
t
/; / 
t
i /= h / 
s
T
i
/+ // 
s
/; / 
s
T
i
/+ // 
s
i
/= h / 
s
T
i
/; / 
s
T
i
i /+ /2 / h / 
s
T
i
/; / 
s
i /+ /
/2
h / 
s
/; / 
s
i
/= h / 
s
T
/2
i
/; / 
s
i /+ /2 / h / 
s
T
i
/; / 
s
i /+ /
/2
h / 
s
/; / 
s
i
/= /(/2 / /+ q /? /1/) h / 
s
T
i
/; / 
s
i /+ /( q /+ /
/2
/) h / 
s
/; / 
s
i
/= /(/2 / /+ q /? /1/) h / 
t
/? // 
s
/; / 
s
i /+ /( q /+ /
/2
/) h / 
s
/; / 
s
i
/= /( q /+ / /)/(/1 /? / /) h / 
s
/; / 
s
i /;
where for the last equalit y w e ha v e used Corollary /5/./6/. Ho w ev er/, b y induction
on dominance/, h / 
s
/; / 
s
i /= q
/` /( d /( s /)/)
/
s
/; so/, b y Lemma /5/./9/, h / 
t
/; / 
t
i /= q
/1/+ /` /( d /( s /)/)
/
t
/=
q
/` /( d /( t /)/)
/
t
as required/.
/5/./1/1 Corollary Supp ose that t is a standar d / /{table aux/. Then h f
t
/; f
t
i /= q
/` /( d /( t /)/)
/
t
/.
Conse quently/, the Gr am determinant of the Sp e cht mo dule S
/
is e qual to
G
/!
/( / /) /=
Y
t /2 Std /( / /)
q
/` /( d /( t /)/)
/
t
/:
No w w e turn to tableaux of arbitrary t yp e/. T o do this w e need to compare
/'
T
/!
T
/
/'
t
and /'
T
when T /= / /( t /)/; this will b e accomplished b y the next de/nition/.
Let t b e a standard / /{tableau suc h that T /= / /( t /) is semistandard/. F or eac h no de
/( i/; j /) /2 /[ / /] let
P
/
t
/( i/; j /) /= f /( k /; l /) /2 /[ / /] j l /< j/; t /( k /; l /) /< t /( i/; j /) and T /( i/; j /) /= T /( k /; l /) g
and
/
/
t
/=
Y
/( i/;j /) /2 /[ / /]
Y
/( k /;l /) /2 P
/
t
/( i/;j /)
/[ j /? i /+ k /? l /+ /1/]
q
/[ j /? i /+ k /? l /]
q
/:
/5/./1/2 Example Supp ose that / /= /(/3 /; /2/) and / /= /(/2
/2
/; /1/)/. Then T /=
/1 /1 /2
/2 /3
is a
standard / /{tableau of t yp e / and s /= /rst /( T /) /=
/1 /2 /3
/4 /5
and t /= last/( T /) /=
/1 /1 /4
/3 /5
/.
Therefore/,
/
/
s
/=
/[/2/]
q
/[/1/]
q
and /
/
t
/=
/[/2/]
q
/[/1/]
q
/[/4/]
q
/[/3/]
q
/:
Notice that /
t
/= /
/
t
/
T
b y Example /5/./7/.
Let d /2 D
//
and recall from Prop osition /4/./5 that / /= /d /\ / is the comp osition
of n suc h that S
/
/= d
/? /1
S
/
d /\ S
/
/.
/5/./1/3 Lemma L et T b e a semistandar d / /{table au of typ e / /.
/(i/) L et t /= /rst/( T /) and let d /= d /( t /) /. Then /
/
t
/= /[ / /]
/!
q
wher e / /= /d /\ / /.
/(ii/) L et t /= last /( T /) /. Then /
t
/= /
/
t
/
T
/.
Pro of/. Let t /= /rst /( T /) and supp ose that /( i/; j /) /2 /[ / /]/. Then
P
/
t
/( i/; j /) /= f /( k /; l /) /2 /[ / /] j l /< j and T /( i/; j /) /= T /( k /; l /) g /:
Therefore/, if p
/
ij
/= j P
/
t
/( i/; j /) j then
Y
/( k /;l /) /2 /[ / /]
/[ j /? i /+ k /? l /+ /1/]
q
/[ j /? i /+ k /? l /]
q
/=
/[/2/]
q
/[/1/]
q
/ / /
/[ p
/
ij
/+ /1/]
q
/[ p
/
ij
/]
q
/= /[ p
/
ij
/+ /1/]
q
/:
/5/0 /5/. THE JANTZEN/{SCHAPER THEOREM
Consequen tly /, /
/
t
/=
Q
/( i/;j /) /2 /[ / /]
/[ p
/
ij
/+ /1/]
q
/=
Q
r / /1
Q
n
k /=/1
f c
r k
/( t /) g
q
where c
r k
/( t /) is equal
to the n um b er of en tries in ro w r of T whic h are equal to k /. Ho w ev er/, the parts of /
are precisely the n um b ers c
r k
/( t /) as r and k v ary /(cf/. Example /4/./6/)/, so this pro v es
part /(i/)/.
P art /(ii/) follo ws b y comparing the de/nitions of /
t
and /
/
t
/.
/5/./1/4 Lemma Supp ose that t is a standar d / /{table au/, T /= / /( t /) and s /= /rst/( T /) /.
/(i/) If T is semistandar d then /'
t
/'
T
/!
T
/
/= q
/` /( w /)
/
/
s
/'
T
wher e / /= /d /\ / and w is the
element of S
/
such that d /( t /) /= d /( s /) w /.
/(ii/) If T is not semistandar d then ther e exist c
S
/2 R such that /'
t
/'
T
/!
T
/
/=
X
S B T
c
S
/'
S
/.
Pro of/. Applying the de/nitions w e /nd that
/'
t
/'
T
/!
T
/
/( m
/
/) /= /'
t
/( m
/
/) /= /'
t
/(/1/) m
/
/= m
t
m
/
/:
Therefore/, if T /= / /( t /) is semistandard then m
s
m
/
/= /[ / /]
/!
q
m
T
b y Prop osition /4/./5/(i/)
and Lemma /3/./2/; consequen tly /, m
s
m
/
/= /
/
s
/'
T
b y Lemma /5/./1/3/(i/)/. Moreo v er/, d /( t /) /=
d /( s /) w /, for some w /2 S
n
/, and m
t
m
/
/= m
s
T
w
m
/
/= q
/` /( w /)
m
s
m
/
/= q
/` /( w /)
/
/
s
m
T
b y
Lemma /3/./2/. This pro v es /(i/)/.
When T is not semistandard the argumen t is a little bit ugly /. First consider
the case where H /= H
Z
/. Because T is not semistandard there exists an in teger i
suc h that s
i
/2 S
/
and i and i /+ /1 are in the same column of t /. As a result/, b y
Corollary /3/./1/9/, there exist r
v
/2 Z suc h that
/(/1 /+ /^ q /) m
t
m
/
/= m
t
/(/1 /+ T
i
/) m
/
/=
X
v B t
r
v
m
v
m
/
/:
By induction on v w e can write m
v
m
/
as a Z /{linear com bination of terms m
S
for
whic h S D / /( v /) B T /. Therefore/, there exist /^c
S
/2 Z suc h that /(/1 /+ /^ q /) m
t
m
/
/=
P
S
/^c
S
m
s
with /^ c
S
/6/= /0 only if S B T /. Ho w ev er/, f m
S
j S /2 T
/0
/( //; / /) g is a Z /{basis of
M
/
Z
/\ M
/ /
Z
/, and the structure constan ts lie in Z /, so it follo ws that eac h of /^c
S
is
divisible b y /(/1 /+ /^ q /)/. Hence/, w e can divide b y /1 /+ /^ q and then sp ecialize /^q to deduce
the result/.
/5/./1/5 Lemma Supp ose that s and t ar e semistandar d / /{table aux of typ e / such that
/ /( s /) /= / /( t /) /, s B t and s /= t /( i/; i /+ /1/) for some inte ger i /. Then /
/
t
/= /( q /+ / /) /
/
s
wher e
/
/? /1
/= /[res
s
/( i /) /? res
t
/( i /)/]
q
/.
Pro of/. Let /( a/; b /) and /( c/; d /) b e the no des in /[ / /] suc h that t /( a/; b /) /= i and t /( c/; d /) /=
i /+ /1/; then s /( a/; b /) /= i /+ /1 and s /( c/; d /) /= i and b /< d since s B t /. Therefore/,
P
/
t
/( a/; b /) /= P
/
s
/( a/; b /) /[ f /( c/; d /) g and P
/
t
/( x /) /= P
/
s
/( x /) for all no des x /6/= /( a/; b /) in /[ / /]/.
Hence/, /
/
t
/= /[ b /? a /+ c /? d /+ /1/]
q
/= /[ b /? a /+ c /? d /]
q
/
/
s
/= /( q /+ / /) /
/
s
/.
/5/./1/6 Lemma Supp ose that t is a standar d / /{table au such that T /= / /( t /) is semis/-
tandar d/. Then / 
t
/'
T
/
T
/!
/= /
/
t
/ 
T
/.
Pro of/. Supp ose that t is a standard / /{tableau suc h that / /( t /) /= T /. W e /rst sho w
that / 
t
/'
T
/
T
/!
/= r
t
/'
T
for some r
t
/2 R /. Let k b e an in teger with /1 / k / d and let
x/; x /+ /1 /; /: /: /: /; y b e the en tries in ro w k of t
/
/. Then/, b y /(/5/./1/) and Prop osition /5/./5/(iii/)/,
/ 
t
/'
T
/
T
/!
L
/
k
/= / 
t
/( L
/!
x
/+ L
/!
x /+/1
/+ / / / /+ L
/!
y
/) /'
T
/
T
/!
/= /[res
T
/( k /)/]
q
/ 
t
/'
T
/
T
/!
/:
/1/. THE GRAM DETERMINANT OF W
/
/5/1
Ho w ev er/, / 
t
/'
T
/
T
/!
L
/
k
/2 W
/
/
and f /'
S
j S /2 T
/0
/( //; / /) g is a basis of W
/
/
b y Corol/-
lary /5/./6/; so it follo ws that there exist r
t
/2 R suc h that / 
t
/'
T
/
T
/!
/= r
t
/ 
T
from
Prop osition /5/./5/(iv/)/. It remains to sho w that r
t
/= /
/
t
for all t /.
Supp ose that t /= /rst/( T /)/. Then /'
T
/= /
/
t
/'
t
/'
T
/!
T
/
b y Lemma /5/./1/3/(i/) and
Lemma /5/./1/4/(i/)/. F urthermore/, b y Prop osition /5/./5/(i/)/, there exist a
s
/2 R suc h that
/ 
t
/= /'
t
/+
P
s B t
a
s
/'
s
/. Therefore/, b y Lemma /5/./1/4/,
/ 
t
/'
T
/!
T
/
/= /'
t
/'
T
/!
T
/
/+
X
s B t
a
s
/'
s
/'
T
/!
T
/
/= /
/
t
/'
T
/+
X
S B T
b
S
/'
S
for some b
S
/2 R /. Ho w ev er/, / 
t
/'
T
/!
T
/
is a m ultiple of /'
T
so / 
t
/'
T
/!
T
/
/= /
/
t
/'
T
b y
Prop osition /5/./5/(i/)/, and w e are done in this case/.
Finally supp ose that t /6/= /rst /( T /)/. Then there exists a standard / /{tableau s
suc h that / /( s /) /= T /, s B t and s /= t /( i/; i /+ /1/) for some in teger i with /( i/; i /+ /1/) /2 S
/
/.
No w /'
T
/!
T
/
T
i
/= q /'
T
/!
T
/
b y Lemma /3/./2 and / 
t
/= / 
s
T
i
/+ // 
s
/, where /
/? /1
/= /[res
s
/( i /) /?
res
t
/( i /)/]
q
/, b y Theorem /3/./3/4/. Therefore/, b y induction/,
/ 
t
/'
T
/!
T
/
/= / 
s
/( T
i
/+ / /) /'
T
/!
T
/
/= /( q /+ / /) / 
s
/'
T
/!
T
/
/= /( q /+ / /) /
/
s
/ 
T
/= /
/
t
/ 
T
/;
the last equalit y coming from Lemma /5/./1/5/.
/5/./1/7 Lemma Supp ose that T is a semistandar d / /{table au of typ e / and let t /=
last/( T /) /. Then ther e exist b
s
/2 R such that
/ 
T
/'
T
/
T
/!
/= / 
t
/+
X
s B t
b
s
/ 
s
/:
Pro of/. By Prop osition /4/./5/, m
T
/= m
t
/+
P
m
s
where the sum is o v er those standard
/ /{tableaux s suc h that s B t and / /( s /) /= T /. Therefore/, b y Prop osition /5/./5/(i/) there
exist a
S
/2 R suc h that
/ 
T
/'
T
/
T
/!
/(/1/) /= / 
T
/( m
/
/) /= /'
T
/( m
/
/) /+
X
S B T
a
S
/'
S
/( m
/
/) /= m
T
/+
X
S B T
a
S
m
S
/= m
t
/+
X
s B t
b
/0
s
/:
Hence/, / 
T
/'
T
/
T
/!
/= /'
t
/+
P
s B t
b
/0
s
/'
s
/. No w apply Prop osition /5/./5/(i/) once more/.
/5/./1/8 Theorem Supp ose that R is a /eld and that e /> n /. L et T b e a semistandar d
/ /{table au of typ e / /. Then h / 
T
/; / 
T
i /= q
/` /( d /( t /)/)
/
T
wher e t /= last/( T /) /.
Pro of/. Let t /= last/( T /)/; then / 
t
/'
T
/!
T
/
/= /
/
t
/ 
T
b y Lemma /5/./1/7/. Consequen tly /,
/
/
t
h / 
T
/; / 
T
i /= h / 
t
/'
T
/!
T
/
/; / 
T
i /= h / 
t
/; / 
T
/'
/
T
/!
T
/
i /= h / 
t
/; / 
T
/'
T
/
T
/!
i /;
the second last equalit y coming from Prop osition /2/./7/(ii/)/. By Lemma /5/./1/7 there
exist b
s
/2 R suc h that / 
T
/'
T
/
T
/!
/= / 
t
/+
P
s B t
b
s
/ 
s
/, so
/
/
t
h / 
T
/; / 
T
i /= h / 
t
/; / 
T
/'
T
/
T
/!
i /= h / 
t
/; / 
t
i /+
X
s B t
b
s
h / 
t
/; / 
s
i /= h / 
t
/; / 
t
i /= q
/` /( d /( t /)/)
/
t
/;
b y Corollary /5/./6 and Prop osition /5/./1/0/. Ho w ev er/, /
/
t
/
T
/= /
t
b y Lemma /5/./1/3/(ii/) so
w e/'re done/.
Let /^q b e an indeterminan t o v er Z and de/ne g
/
/
/( /^ q /) /=
Q
T
/
T
/( /^ q /)/. F or the re/-
mainder of this section w e /x N /=
P
T
/` /( d /(last/( T /)/)/) where the sum is o v er the
semistandard / /{tableaux T of t yp e / /.
/5/2 /5/. THE JANTZEN/{SCHAPER THEOREM
/5/./1/9 Corollary Supp ose that R is an inte gr al domain and let / /2 /
/+
/( d/; n /) and
/ /2 //( d/; n /) /. Then G
/
/
/= q
N
g
/
/
/, c onsidering g
/
/
as an element of R /.
Pro of/. Supp ose /rst that R /= Q /( /^ q /) where /^q is an indeterminan t o v er Q /. By
Prop osition /5/./5/(i/) the transition matrix b et w een the semistandard basis of W
/
/
and
its orthogonal basis is unitriangular so b y Theorem /5/./1/8
G
/
/
/( /^ q /) /= /^ q
N
Y
T /2T
/0
/( //;/ /)
/
T
/( /^ q /) /= /^ q
N
g
/
/
/( /^ q /) /:
Ho w ev er/, b y de/nition/, G
/
/
/( /^ q /) /2 Z /[ /^ q /] so it follo ws that g
/
/
/( /^ q /) /2 Z /[ /^ q /]/. /(This is quite
astounding giv en the de/nition of the rational functions /
T
/( /^ q /)/!/)
No w supp ose that R is an arbitrary in tegral domain and let q b e an in v ertible
elemen t of R /. Consider R /[ /^ q /] as a Z /[ /^ q /]/{mo dule via the homomorphism / /: Z /[ /^ q /] /? /! R
whic h maps /^q to q /. Then / sends an inner pro duct h /'
S
/; /'
T
i in S
Z /[ /^ q /] /; /^q
/( d/; n /) to
the corresp onding inner pro duct in S
R/;q
/( d/; n /) /. Hence/, g
/
/
/( q /) /= /
/?
g
/
/
/( /^ q /)
/
can b e
considered as an elemen t of R and the Gram determinan t G
/
/
/( q /) of the R /{mo dule
W
/
/
is equal to q
N
g
/
/
/( q /)/.
/5/./2/0 Example Let / /= /(/3 /; /2/) and / /= /(/2
/2
/; /1/)/. Then T
/0
/( //; / /) /= f S /; T g where
S /=
/1 /1 /2
/2 /3
and T /=
/1 /1 /3
/2 /2
/. Therefore/, G
/
/
/= q /[/2/]
q
/[/4/]
q
b y Example /5/./7/.
No w that w e ha v e form ula for G
/
/
w e pull some con tortionists/' tric ks to rewrite
the pro duct g
/
/
in a more usable form/.
Let / b e a partition of n and let /
/0
b e its conjugate pa rtition /; that is/, /
/0
/=
/( /
/0
/1
/; /
/0
/2
/; /: /: /: /) where /
/0
i
is equal for the n um b er of no des in column i of /[ / /] for eac h
i / /1/.
F or /1 / i / n let /
i
/= n /? i /+ /
/0
i
/; then / /= /( /
/1
/; /: /: /: /; /
n
/) is the sequence of b eta
numb ers for / /. Notice that /
/1
/> /
/2
/> / / / /> /
n
/ /0/. F or example/, if / /= /( n /) then
/
/0
/= /(/1
n
/) and /( n/; n /? /1 /; /: /: /: /; /1/) is the sequence of b eta n um b ers for / /; if / /= /(/1
n
/)
then /
/0
/= /( n /) and / /= /(/2 n /? /1 /; n /? /2 /; /: /: /: /; /1 /; /0/)/.
/5/./2/1 Let / /= /( /
/1
/; /: /: /: /; /
n
/) b e an y sequence of in tegers and let / /= /( /
/1
/; /: /: /: /; /
n
/) b e
the sequence obtained b y putting the terms in / in to non/{increasing order/. Then
/ is the sequence of b eta n um b ers for some partition if and only if /
c
/ /0 for
c /= /1 /; /: /: /: /; n and /
b
/6/= /
c
if b /6/= c /.
Supp ose that / is a sequence of b eta n um b ers for some partition / /2 /
/+
/( d/; n /)/.
Then there exists a unique elemen t w in S
n
suc h that /
c
/= /
cw
for c /= /1 /; /: /: /: /; n /.
F or an y comp osition / let d
/
/( / /) /= /( /? /1/)
/` /( w /)
jT
/0
/( //; / /) j /; so d
/
/( / /) /= / dim W
/
/
/.
If / is not the sequence of b eta n um b ers for an y partition in /
/+
/( d/; n /) then w e
set d
/
/( / /) /= /0/.
No w w e return rewriting our form ula for G
/
/
/. Let / /= /( /
/1
/; /: /: /: /; /
n
/) b e the
sequence of / n um b ers for / and supp ose that Z is the largest in teger suc h that
/
Z
/6/= /0/. Let z /= /
Z
/; then ev ery tableau T in T
/0
/( //; / /) has z exactly en tries equal to
Z and these o ccur at the feet of distinct columns/, sa y columns c
/1
/< c
/1
/< / / / /< c
z
/.
Let T
C
b e the tableau obtained from T b y deleting all of the en tries lab elled Z and
let /
C
/= /( /
C
/1
/; /: /: /: /; /
C
n
/) b e sequence of in tegers giv en b y
/
C
b
/=
/(
/
b
/? /1 /; if b /2 C /;
/
b
/; if b /= /2 C /;
/1/. THE GRAM DETERMINANT OF W
/
/5/3
where C /= f c
/1
/; /: /: /: /; c
z
g /. Let /
C
b e the partition of n /? z whose sequence of
b eta n um b ers is /
C
/. Then T
C
is a semistandard /
C
/{tableau of t yp e / where
/ /= /( /
/1
/; /: /: /: /; /
Z /? /1
/; /0/)/. Consequen tly /, b y the con v en tions of /(/5/./2/1/)/,
d
/
/( / /) /= jT
/0
/( //; / /) j /=
X
C /f /1 /; /2 /;/:/:/: /;n g
j C j /= z
d
/
/( /
C
/) /:
More generally /, for an y sequence / /= /( /
/1
/; /: /: /: /; /
n
/) of in tegers w e ha v e
/5 /: /2/2 d
/
/( / /) /=
X
C /f /1 /; /2 /;/:/:/: /;n g
j C j /= z
d
/
/( /
C
/) /;
where the sequence /
C
is de/ned in exactly the same w a y as the sequence /
C
/.
F or con v enience let n /= f /1 /; /2 /; /: /: /: /; n g /. In the next Lemma/, if C / n and /
C
is not a sequence of b eta n um b ers of a partition in /
/+
/( d/; n /) then w e adopt that
con v en tion that g
/
C
/
/= /1 and T
/0
/( /
C
/; / /) /= /? /.
/5/./2/3 Lemma L et / /= /( /
/1
/; /: /: /: /; /
n
/) b e the se quenc e of b eta numb ers for / /. Then
g
/
/
/( /^ q /) /= B
/2
B
/3
Y
C / n
j C j /= z
g
/
C
/
/( /^ q /)
wher e B
/2
/=
Y
h / /1
Y
C / n
j C j /= z /? /1
Y
b/;c /= /2 C
/
C
b
/? /
C
c
/+/1/= h
/[ h /]
/? d
/
/( /
C
/1
/;/:/:/: /;/
C
b
/? h/;/:/:/: /;/
C
c
/? /1/+ h/;/:/:/: /;/
C
n
/)
/^q
and B
/3
/=
Y
h / /1
Y
C / n
j C j /= z /? /1
Y
b/;c /= /2 C
/
C
b
/? /
C
c
/= h
/[ h /]
d
/
/( /
C
/1
/;/:/:/: /;/
C
b
/? /1 /? h/;/:/:/: /;/
C
c
/+ h/;/:/:/: /;/
C
n
/)
/^q
/.
Pro of/. By de/nition
g
/
/
/( /^ q /) /=
Y
T /2T
/0
/( //;/ /)
/
T
/( /^ q /) /=
Y
T /2T
/0
/( //;/ /)
Y
/( i/;j /) /2 /[ / /]
Y
/( k /;l /) /2 P
/
/( i/;j /)
/[ j /? i /+ k /? l /+ /1/]
/^q
/[ j /? i /+ k /? l /]
/^q
/:
The discussion of /(/5/./2/1/) sho ws that deleting all of the no des lab elled Z from a
tableau giv es a bijectiv e corresp ondence b et w een the sets T
/0
/( //; / /) and
S
C
T
/0
/( /
C
/; / /)/,
where C runs through the subsets of n of size z /. Therefore/,
Y
T /2T
/0
/( //;/ /)
Y
/( i/;j /) /2 /[ / /]
T /( i/;j /) /6/= Z
Y
/( k /;l /) /2 P
/
/( i/;j /)
/[ j /? i /+ k /? l /+ /1/]
/^q
/[ j /? i /+ k /? l /]
/^q
/=
Y
C / n
j C j /= z
g
/
C
/
/( /^ q /) /:
Next supp ose that /( i/; j /) /2 /[ / /] and T /( i/; j /) /= Z /. Then /( i/; j /) is at the fo ot of some
column in /[ / /] and if /( k /; l /) /2 P
/
/( i/; j /) then T /( k /; l /) /< Z and l /< j /; therefore/, /
l
/? /
j
/=
/5/4 /5/. THE JANTZEN/{SCHAPER THEOREM
j /? i /+ k /? l /. Hence/,
Y
T /2T
/0
/( //;/ /)
Y
/( i/;j /) /2 /[ / /]
T /( i/;j /)/= Z
Y
/( k /;l /) /2 P
/
/( i/;j /)
/[ j /? i /+ k /? l /+ /1/]
/^q
/[ j /? i /+ k /? l /]
/^q
/=
Y
C / n
j C j /= z
/
Y
b/<c
c /2 C
b /= /2 C
/[ /
b
/? /
c
/+ /1/]
/^q
/[ /
b
/? /
c
/]
/^q
/
d
/
/( /
C
/)
/=
Y
h / /1
Y
C / n
j C j /= z
Y
b /= /2 C/;c /2 C
/
b
/? /
c
/+/1/= h
/[ h /]
d
/
/( /
C
/1
/;/:/:/: /;/
C
b /? /1
/;/
b
/;/
C
b /+/1
/;/:/:/: /;/
C
c /? /1
/;/
c
/? /1 /;/
C
c /+/1
/;/:/:/: /;/
C
n
/)
/^q
Y
b /= /2 C/;c /2 C
/
b
/? /
c
/= h
/[ h /]
d
/
/( /
C
/1
/;/:/:/: /;/
C
b /? /1
/;/
b
/;/
C
b /+/1
/;/:/:/: /;/
C
c /? /1
/;/
c
/? /1 /;/
C
c /+/1
/;/:/:/: /;/
C
n
/)
/^q
/=
Y
h / /1
Y
C / n
j C j /= z /? /1
Y
b/;c /= /2 C
/
C
b
/? /
C
c
/+/1/= h
/[ h /]
/? d
/
/( /
C
/1
/;/:/:/: /;/
C
b /? /1
/;/
C
c
/? /1 /;/
C
b /+/1
/;/:/:/: /;/
C
c /? /1
/;/
C
b
/;/
C
c /+/1
/;/:/:/: /;/
C
n
/)
/^q
Y
b/;c /= /2 C
/
C
b
/? /
C
c
/= h
/[ h /]
/? d
/
/( /
C
/1
/;/:/:/: /;/
C
b /? /1
/;/
C
c
/? /1 /;/
C
b /+/1
/;/:/:/: /;/
C
c /? /1
/;/
C
b
/;/
C
c /+/1
/;/:/:/: /;/
C
n
/)
/^q
/=
Y
h / /1
Y
C / n
j C j /= z /? /1
Y
b/;c /= /2 C
/
C
b
/? /
C
c
/+/1/= h
/[ h /]
/? d
/
/( /
C
/1
/;/:/:/: /;/
C
b /? /1
/;/
C
b
/? h/;/
C
b /+/1
/;/:/:/: /;/
C
c /? /1
/;/
C
c
/? /1/+ h/;/
C
c /+/1
/;/:/:/: /;/
C
n
/)
/^q
Y
b/;c /= /2 C
/
C
b
/? /
C
c
/= h
/[ h /]
/? d
/
/( /
C
/1
/;/:/:/: /;/
C
b /? /1
/;/
C
b
/? /1 /? h/;/
C
b /+/1
/;/:/:/: /;/
C
c /? /1
/;/
C
c
/+ h/;/
C
c /+/1
/;/:/:/: /;/
C
n
/)
/^q
/;
where the last equation follo ws using the relation /
C
b
/? /
C
c
/+ /1 /= h /, in the n umerator/,
and /
C
b
/? /
C
c
/= h /, in the denominator/. Com bining the ab o v e equations pro v es the
Lemma/.
In the next result /(and similarly in the de/nition of B
/2
and B
/3
ab o v e/)/, the only
restriction on b and c is that /
b
/< /
c
/+ h /; in particular/, w e do not require that b /< c
as migh t b e inferred from the notation/.
/5/./2/4 Prop ositi on Supp ose that R is an inte gr al domain/. L et / /2 /
/+
/( d/; n /) and
/ /2 //( d/; n /) and supp ose that / /= /( /
/1
/; /: /: /: /; /
n
/) is the se quenc e of b eta numb ers for
/ /. Then
g
/
/
/=
Y
h / /1
Y
c /2 n
Y
b /2 n
/
b
/>/
c
/? h
/[ h /]
/? d
/
/( /
/1
/;/:/:/: /;/
b
/+ h/;/:/:/: /;/
c
/? h/;/:/:/: /;/
n
/)
q
/;
r e gar de d as an element of R /.
Pro of/. As in the pro of of Corollary /5/./1/9 it is su/cien t to consider the case where
R /= Z /[ /^ q /]/. W e no w argue b y induction on n /. When n /= /1 b oth g
/
/
and the
righ t hand side are equal to /1/, so w e ma y assume that n /> /1/. By induction/,
Q
C
g
/
C
/
/= G
/1
G
/2
G
/3
G
/4
where/, in the pro duct/, C runs o v er all subsets of n whic h
/1/. THE GRAM DETERMINANT OF W
/
/5/5
ha v e z elemen ts and
G
/1
/=
Y
h / /1
Y
C / n
j C j /= z
Y
c /= /2 C
Y
b /2 n n C
/
C
b
/>/
C
c
/? h
/[ h /]
/? d
/
/( /
C
/1
/;/:/:/: /;/
C
b
/+ h/;/:/:/: /;/
C
c
/? h/;/:/:/: /;/
C
n
/)
/^q
/;
G
/2
/=
Y
h / /1
Y
C / n
j C j /= z /? /1
Y
c /= /2 C
Y
b /= /2 C
/
C
b
/>/
C
c
/? /1/+ h
/[ h /]
/? d
/
/( /
C
/1
/;/:/:/: /;/
C
b
/+ h/;/:/:/: /;/
C
c
/? /1/+ h/;/:/:/: /;/
C
n
/)
/^q
/;
G
/3
/=
Y
h / /1
Y
C / n
j C j /= z /? /1
Y
c /= /2 C
Y
b /= /2 C
/
C
b
/+/1 />/
C
c
/? h
/[ h /]
/? d
/
/( /
C
/1
/;/:/:/: /;/
C
b
/+/1 /? h/;/:/:/: /;/
C
c
/? h/;/:/:/: /;/
C
n
/)
/^q
/;
and
G
/4
/=
Y
h / /1
Y
C / n
j C j /= z /? /2
Y
c /= /2 C
Y
b /= /2 C
/
C
b
/>/
C
c
/? h
/[ h /]
/? d
/
/( /
C
/1
/;/:/:/: /;/
C
b
/+/1 /? h/;/:/:/: /;/
C
c
/? h /? /1 /;/:/:/: /;/
C
n
/)
/^q
/:
Let B
/2
and B
/3
b e as in Lemma /5/./2/3/. Then
B
/2
G
/2
/=
Y
h / /1
Y
C / n
j C j /= z /? /1
Y
c /= /2 C
Y
b /= /2 C
/
C
b
/>/
C
c
/? h
/[ h /]
/? d
/
/( /
C
/1
/;/:/:/: /;/
C
b
/+ h/;/:/:/: /;/
C
c
/? /1/+ h/;/:/:/: /;/
C
n
/)
/^q
/;
and
B
/3
G
/3
/=
Y
h / /1
Y
C / n
j C j /= z /? /1
Y
c /= /2 C
Y
b /= /2 C
/
C
b
/>/
C
c
/? h
/[ h /]
/? d
/
/( /
C
/1
/;/:/:/: /;/
C
b
/+/1 /? h/;/:/:/: /;/
C
c
/? h/;/:/:/: /;/
C
n
/)
/^q
/:
By Lemma /5/./2/3 again/, g
/
/
/= G
/1
/( B
/2
G
/2
/)/( B
/3
G
/3
/) B
/4
/, so com bining the last three
equations and using /(/5/./2/2/) completes the pro of/.
/5/./2/5 Example As in Example /5/./2/0/, let / /= /(/3 /; /2/) and / /= /(/2
/2
/; /1/)/. The sequence
of b eta n um b ers for / is / /= /(/6 /; /5 /; /3 /; /1 /; /0/) so
G
/
/
/= q /[/2/]
/? d
/
/(/4 /; /7 /; /3 /; /1 /; /0/)
q
/[/3/]
/? d
/
/(/9 /; /2 /; /3 /; /1 /; /0/)
q
/[/4/]
/? d
/
/(/2 /; /5 /; /7 /; /1 /; /0/) /? d
/
/(/2 /; /9 /; /3 /; /1 /; /0/)
q
/= q /[/2/]
jT
/0
/(/(/3 /; /1
/2
/) /;/ /) j
q
/[/3/]
jT
/0
/(/(/1
/5
/) /;/ /) j
q
/[/4/]
jT
/0
/(/(/2
/2
/; /1/) /;/ /) j/?jT
/0
/(/(/1
/5
/) /;/ /) j
q
/:
Because jT
/0
/(/(/1
/5
/) /; / /) j /= /0 and jT
/0
/(/(/2
/2
/; /1/) /; / /) j /= jT
/0
/(/(/3 /; /1
/2
/) /; / /) j /= /1/, this agrees with
the answ er obtained for G
/
/
in Example /5/./2/0/.
Prop osition /5/./2/4 giv es a closed form ula for G
/
/
/. A more com binatorial statemen t
is p ossible/; this requires a /nal piece of notation and a Lemma/.
Let /( a/; b /) b e a no de in the diagram of / /. Then /( a/; b /)th ho ok of / is the set
H
/
ab
/= f /( a/; c /) /2 /[ / /] j c / b g /[ f /( d/; b /) /2 /[ / /] j d / a g /;
that is/, /( a/; b /)th ho ok is the set of no des in /[ / /] whic h are either in the same ro w and
to the righ t of /( a/; b /)/, or in the same column and b elo w /( a/; b /) /{ including /( a/; b /)/. Let
h
/
ab
/= j H
/
ab
j /= /
a
/+ /
/0
b
/? a /? b /+ /1 b e the /( a/; b /)th ho ok length /. The leg length of H
/
ab
is l
/
ab
/= /
/0
b
/? a /+ /1/; that is/, l
/
ab
is equal to the n um b er of no des in H
/
ab
whic h are
con tained in column b of /[ / /]/.
/5/6 /5/. THE JANTZEN/{SCHAPER THEOREM
Similarl y /, the /( a/; b /)th rim ho ok R
/
ab
is the collection of no des along the rim of /[ / /]
from ro w a to column b /. This is b est illustrated b y an example/; let / /= /(/6 /; /4 /; /3/)
then
H
/
/1/2
/=
/ / / / /
/
/
and R
/
/1/2
/=
/ / /
/ /
/ /
/:
Th us/, there is a one/{to/{one corresp ondence b et w een ho oks and rim ho oks and
j R
/
ab
j /= h
/
ab
/. Imp ortan tly /, if / is a partition of n then /[ / /] n R
/
ab
is the diagram of a
partition of n /? h
/
ab
/. F or example/, when / /= /(/6 /; /4 /; /3/) then /[ / /] n R
/
/1/2
/= /[/(/3 /; /2 /; /1/)/]/.
If /[ / /] n R
/
ab
/= /[ / /] w e sa y that / can b e obtained from / b y wrapping on the rim
ho ok R
/
ab
/; alternativ ely /, / can b e obtained from / b y unwrapping R
/
ab
/.
/5/./2/6 Lemma L et / /= /( /
/1
/; /: /: /: /; /
n
/) b e the se quenc e of b eta numb ers for / and let b
and h b e inte gers with /1 / b / n and h / /1 /. Then ther e exists a c omp osition /
such that d
/
/( /
/1
/; /: /: /: /; /
b
/? h/; /: /: /: /; /
n
/) /6/= /0 only if h /= h
/
ab
for some /( a/; b /) /2 /[ / /] /. In
this c ase/,
d
/
/( /
/1
/; /: /: /: /; /
b
/? h/; /: /: /: /; /
n
/) /= /( /? /1/)
h /? l
/
ab
d
/
/( /
/1
/; /: /: /: /; /
n
/)
wher e /( /
/1
/; /: /: /: /; /
n
/) is the se quenc e of b eta numb ers for the p artition / which is
obtaine d by unwr apping the rim ho ok R
/
ab
fr om / /.
Pro of/. There exists a comp osition / suc h that d
/
/( /
/1
/; /: /: /: /; /
b
/? h/; /: /: /: /; /
n
/) /6/= /0
only if /
b
/? h /6/= /
c
for all in tegers c suc h that b /< c / n and /
b
/? h / /0/.
Supp ose that /
b
/? h / /0 and that there exists an in teger c suc h that b / c / n
and /
c
/> /
b
/? h /> /
c /+/1
/(setting /
n /+/1
/= /? /1 if necessary/)/. Then w e can remo v e h
no des from along the rim of / /, starting with the last no de in column b and ending in
column c so as the lea v e the diagram of a partition / /. If the last no de is in ro w a then
h /= h
/
ab
and /[ / /] /= /[ / /] n R
/
ab
/. Finally /, the sign attac hed to d
/
/( /
/1
/; /: /: /: /; /
b
/? h/; /: /: /: /; /
n
/)
is /( /? /1/)
b /? c
/= /( /? /1/)
h /? l
where l /= l
/
ab
/.
/5/./2/7 Theorem /(James/{Mathas/) Supp ose that R is an inte gr al domain and let
/ /= /( /
/1
/; /: /: /: /; /
n
/) b e the se quenc e of b eta numb ers for / /. Then
G
/
/
/= q
N
Y
/( a/;b /) /2 /[ / /]
/( a/;c /) /2 /[ / /]
b/<c
/
/[ h
/
ab
/]
q
/[ h
/
ac
/]
q
/
d
/
/( /
/1
/;/:/:/: /;/
b
/+ h
/
ab
/;/:/:/: /;/
c
/? h
/
ab
/;/:/:/: /;/
n
/) /:
Pro of/. By Corollary /5/./1/9/, G
/
/
/= q
N
g
/
/
/; th us/, b y Prop osition /5/./2/4 and Lemma /5/./2/6/,
G
/
/
/= q
N
Y
/( a/;b /) /2 /[ / /]
Y
c /2 n
/
b
/>/
c
/? h
/
ab
/[ h
/
ab
/]
/? d
/
/( /
/1
/;/:/:/: /;/
b
/+ h
/
ab
/;/:/:/: /;/
c
/? h
/
ab
/;/:/:/: /;/
n
/)
q
/= q
N
Y
/( a/;b /) /2 /[ / /]
Y
b/<c /2 n
/
b
/>/
c
/? h
/
ab
/[ h
/
ab
/]
/? d
/
/( /
/1
/;/:/:/: /;/
b
/+ h
/
ab
/;/:/:/: /;/
c
/? h
/
ab
/;/:/:/: /;/
n
/)
q
/
Y
/( a/;b /) /2 /[ / /]
Y
b/>c /2 n
/
b
/>/
c
/? h
/
ab
/[ h
/
ab
/]
/? d
/
/( /
/1
/;/:/:/: /;/
c
/? h
/
ab
/;/:/:/: /;/
b
/+ h
/
ab
/;/:/:/: /;/
n
/)
q
No w if c /> b and /
b
/> /
c
/? h
/
ab
then /? d
/
/( /
/1
/; /: /: /: /; /
c
/? h
/
ab
/; /: /: /: /; /
b
/+ h
/
ab
/; /: /: /: /; /
n
/) /=
d
/
/( /
/1
/; /: /: /: /; /
b
/+ h
/
ab
/; /: /: /: /; /
c
/? h
/
ab
/; /: /: /: /; /
n
/)/; moreo v er/, b y Lemma /5/./2/6 this is equal
/2/. THE JANTZEN SUM F ORMULA /5/7
to zero unless /( a/; c /) /2 /[ / /] since /
b
/? h
/
ab
/= /
c
/? h
/
ac
if /( a/; c /) /2 /[ / /]/. On the hand/, if
c /< b then /( a/; c /) /2 /[ / /]/. Com bining these facts pro v es the Theorem/.
By Lemma /5/./2/6 the exp onen t d
/
/( /
/1
/; /: /: /: /; /
b
/+ h
/
ab
/; /: /: /: /; /
c
/? h
/
ac
/; /: /: /: /; /
n
/) has
a com binatorial in terpretation whic h mak es Theorem /5/./2/7 easy to apply /. Namely /,
supp ose that the partition / is obtained b y un wrapping the /( a/; c /)th rim ho ok R
/
ac
from /[ / /] and then wrapping it bac k on in suc h a w a y that its lo w est no de is in
column b /; then/, d
/
/( /
/1
/; /: /: /: /; /
b
/+ h
/
ab
/; /: /: /: /; /
c
/? h
/
ac
/; /: /: /: /; /
n
/) /= /( /? /1/)
l
/
ab
/+ l
/
ac
jT
/0
/( //; / /) j /:
/5/./2/8 Example Supp ose that / /= /(/3 /; /2/)/. In the diagrams b elo w/, using the notation
of Theorem /5/./2/7/, w e lab el the no des /( a/; b /) and /( a/; c /) b y b and c resp ectiv ely and
w e mark the other no des in the v arious rim ho oks with a cross/; in the righ t hand
column w e giv e the con tribution of eac h pair of no des to G
/
/
/.
b c
/!
b
/
con tributing /1
b c
/!
b
/
con tributing
/
/[/4/]
q
/[/1/]
q
/
jT
/0
/(/(/2
/2
/; /1/) /;/ /) j
b c /
/
/!
b
/
/
/
con tributing
/
/[/4/]
q
/[/3/]
q
/
/?jT
/0
/(/(/1
/5
/) /;/ /) j
b c
/!
b
/
con tributing
/
/[/2/]
q
/[/1/]
q
/
jT
/0
/(/(/3 /; /1
/2
/) /;/ /) j
Therefore/, G
/
/
/= /[/2/]
jT
/0
/(/(/3 /; /1
/2
/) /;/ /) j
q
/[/3/]
jT
/0
/(/(/1
/5
/) /;/ /) j
q
/[/4/]
jT
/0
/(/(/2
/2
/; /1/) /;/ /) j/?jT
/0
/(/(/1
/5
/) /;/ /) j
q
/; agreeing with
the answ er obtained in Example /5/./2/5/.
/2/. The Jan tzen sum form ula
So far this Chapter has b een dev oted to calculating determinan ts/. Using a
tec hnique due to Jan tzen w e no w transform these results in to strong statemen ts
ab out the structure of W eyl mo dules and Sp ec h t mo dules/.
Throughout this section R will b e a principal ideal domain and p a prime in R /.
Let F /= R/= p R b e the residue /eld of /( R/; p /) and /
p
/: R
/
/? /! N the p /{adic v aluation
map/; that is/, if r /2 R and r /6/= /0 then /
p
/( r /) /= i if i is the largest in teger suc h that r
is an elemen t of p
i
R /.
Supp ose that M is a free /nite dimensional R /{mo dule whic h is equipp ed with
a symmetric bilinear form h /; i /: M / M /? /! R /. F or eac h in teger k / /1 let
M /( k /) /= f e /2 M j h e/; f i /2 p
k
R for all f /2 M g /;
and let M
F
/( k /) /= M /
R
F b e the reduction of M /( k /) mo dulo p /. Because M
F
/= M /
R
F
is a /nite dimensional F /{mo dule/, there exists an in teger z / /1 suc h that M
F
/( k /) /= /0
whenev er k / z /. The /ltration
M
F
/= M
F
/(/0/) / M
F
/(/1/) / / / / / M
F
/( z /) /> /0
is so/{called Jantzen /ltration of M
F
/. Observ e that M
F
/(/1/) /= rad M
F
/.
Let e
/1
/; /: /: /: /; e
d
b e a basis for M and let G /= det/( h e
i
/; e
j
i /) b e the Gram determi/-
nan t of the bilinear form with resp ect to this basis/. Note that G b elongs to R /.
/5/./2/9 Lemma /(Jan tzen/) L et R b e a princip al ide al domain and supp ose that the
biline ar form h /; i is non/{de gener ate/. Then /
p
/( G /) /=
P
i/> /0
dim
F
M
F
/( i /) /.
/5/8 /5/. THE JANTZEN/{SCHAPER THEOREM
Pro of/. Because R is a principal ideal domain/, w e can /nd a basis f f
/1
/; /: /: /: /; f
d
g of
M suc h that there exist r
i
/2 R
/
with h e
i
/; f
j
i /= /
ij
r
i
for /1 / i/; j / d /. F urthermore/,
the Gram determinan t G /=
Q
z
i /=/1
h e
i
/; f
i
i /=
Q
d
i /=/1
r
i
/, so /
p
/( G /) /=
P
d
i /=/1
/
p
/( r
i
/)/.
No w/, m /=
P
i
a
i
f
i
/, for a
i
/2 R /, is an elemen t of M /( k /) if and only if a
i
r
i
is an
elemen t of p
k
R for i /= /1 /; /: /: /: /; d /; that is/, /
p
/( a
i
r
i
/) / k for all i /. Therefore/, M /( k /) is
the free R /{submo dule of M with basis
f f
i
j /
p
/( r
i
/) / k g /[ f p
k /? /
p
/( r
i
/)
f
i
j /
p
/( r
i
/) /< k g /:
Accordingly /, M
F
/( k /) has basis f f
i
/
 /1 j /
p
/( r
i
/) / k g and so
X
k /> /0
dim
F
M
F
/( k /) /=
z
X
i /=/1
/
p
/( r
i
/) /= /
p
/( G /) /;
as w e wished to sho w/.
W e are going to apply this Lemma in the case where M /= W
/
R
/'
T
/
T
/
/; b efore w e
can do this ho w ev er/, w e need some preparation/.
Let /^ q b e an elemen t of R suc h that /[ n /]
/!
/^q
/6/= /0/; b y Theorem /5/./2/7 this ensures that
G
/
/
/( /^ q /) /6/= /0 for all / /2 /
/+
/( d/; n /) and / /2 //( d/; n /)/. Let q /= /^ q /+ p R and consider F as
an R /{mo dule in the natural w a y /. Then S
F /;q
/( d/; n /)
/
/=
S
R/; /^q
/( d/; n /) /
R
F /.
Supp ose that M
F
is a righ t S
F /;q
/( d/; n /)/{mo dule and let f a
/
j / /2 /
/+
/( d/; n /) g b e
a set of in tegers/. W rite M
F
/ /!
P
/
a
/
W
/
F
if
M
F
/
M
a
/
/< /0
/( /? a
/
/) W
/
F
and
M
a
/
/> /0
a
/
W
/
F
ha v e the same comp osition factors/. Th us/, M
F
and the virtual mo dule
P
/
a
/
W
/
F
ha v e the same images in the Grothendiec k group of S
F /;q
/( d/; n /) /.
/5/./3/0 Lemma L et M
F
b e a right S
F /; q
/( d/; n /) /{mo dule and supp ose that ther e exist
inte gers f a
/
j / /2 /
/+
/( d/; n /) g such that
dim
F
M
F
/'
T
/
T
/
/=
X
/ /2 /
/+
/( d/;n /)
a
/
dim W
/
F
/'
T
/
T
/
for al l / /2 /
/+
/( d/; n /) /. Then M
F
/ /!
X
/
a
/
W
/
F
/.
Pro of/. By Theorem /4/./1/6 there exist in tegers c
/
suc h that M
F
/=
P
/
c
/
W
/
F
/. There/-
fore/,
/0 /=
X
/ /2 /
/+
/( d/;n /)
/( c
/
/? a
/
/) dim
F
W
/
F
/'
T
/
T
/
/=
X
/ /2 /
/+
/( d/;n /)
/( c
/
/? a
/
/) / jT
/0
/( //; / /) j /:
Ho w ev er/, T
/0
/( //; / /) /= f T
/
g and T
/0
/( //; / /) /= /? unless / D / so the matrix
/?
jT
/0
/( //; / /) j
/
is unitriangular/, where //; / /2 /
/+
/( d/; n /)/. Hence/, the equations ab o v e ha v e a unique
solution/; namely /, c
/
/= a
/
for all / /2 /
/+
/( d/; n /)/.
Giv en a sequence / /= /( /
/1
/; /: /: /: /; /
n
/) of in tegers recall that / is the sequence
obtained b y reordering the terms in / so that they are in non/{increasing order/.
Let w /2 S
n
b e a p erm utation suc h that /
i
/= /
iw
/. If / is the sequence of b eta
n um b ers for a partition / /2 /
/+
/( d/; n /) then w is uniquely determined /(see /5/./2/1/) and
w e de/ne W
/
F
to b e the /(virtual/) S
F /; q
/( d/; n /) /{mo dule /( /? /1/)
/` /( w /)
W
/
F
/. Similarl y /, let
/2/. THE JANTZEN SUM F ORMULA /5/9
S
/
F
/= /( /? /1/)
/` /( w /)
S
/
F
/, a virtual H
F /;q
/{mo dule/. If / is not the sequence of b eta n um b ers
for an y partition in /
/+
/( d/; n /) w e set W
/
F
/= /0 and S
/
F
/= /0/.
/5/./3/1 The Jan tzen Sum F orm ula /( /[ /1 /, /3/9 /] /) Supp ose that /[ n /]
/!
/^q
/6/= /0 in R and let /
b e a p artition in /
/+
/( d/; n /) /. Then
X
i/> /0
W
/
F
/( i /) / /!
X
/( a/;b /) /2 /[ / /]
/( a/;c /) /2 /[ / /]
b/<c
/
/
p
/(/[ h
/
ab
/]
/^q
/) /? /
p
/(/[ h
/
ac
/]
/^q
/)
/
W
/( /
/1
/;/:/:/: /;/
b
/+ h
/
ab
/;/:/:/: /;/
c
/? h
/
ac
/;/:/:/: /;/
n
/)
F
/:
Pro of/. Let / /2 /
/+
/( d/; n /) and consider the R /{mo dule W
/
/
/= W
/
R
/'
T
/
T
/
/. Let / /=
/( /
/1
/; /: /: /: /; /
n
/) b e the sequence of b eta n um b ers for / /. No w /[ n /]
/!
/^q
is non/{zero/, so
G
/
/
/6/= /0/. Therefore/, b y Jan tzen/'s Lemma /(/5/./2/9/)/, /
p
/( G
/
/
/) /=
P
i/> /0
dim
F
W
/
F
/'
T
/
T
/
/.
On the other hand/, b y Theorem /5/./2/7/,
/
p
/( G
/
/
/) /=
X
/( a/;b /) /2 /[ / /]
/( a/;c /) /2 /[ / /]
b/<c
/
/
p
/(/[ h
/
ab
/]
/^q
/) /? /
p
/(/[ h
/
ac
/]
/^q
/)
/
d
/
/( /
/1
/; /: /: /: /; /
b
/+ h
/
ab
/; /: /: /: /; /
c
/? h
/
ac
/; /: /: /: /; /
n
/)
/=
X
/( a/;b /) /2 /[ / /]
/( a/;c /) /2 /[ / /]
b/<c
/
/
p
/(/[ h
/
ab
/]
/^q
/) /? /
p
/(/[ h
/
ac
/]
/^q
/)
/
dim W
/( /
/1
/;/:/:/: /;/
b
/+ h
/
ab
/;/:/:/: /;/
c
/? h
/
ac
/;/:/:/: /;/
n
/)
F
/'
T
/
T
/
/:
The last equation holds for all partitions / /2 /
/+
/( d/; n /)/, so the Theorem no w follo ws
b y applying Lemma /5/./3/0/.
The Jan tzen Sum form ula is imp ortan t b ecause W
/
F
/(/1/) /= rad W
/
F
/; consequen tly /,
if / /6/= / then L
/
F
is a comp osition factor of W
/
F
if and only if L
/
F
is a comp osition
factor of
P
i/> /0
W
/
F
/( i /)/. In general/, the comp osition m ultiplicit y of L
/
F
in
P
i/> /0
W
/
F
/( i /)
will b e m uc h higher than the comp osition m ultiplicit y of L
/
F
in W
/
F
/; ho w ev er/, this
m ultiplicit y is an upp er b ound on d
//
/.
Applying the Sc h ur functor of Prop osition /4/./1/9 giv es the analogue of the sum
form ula for H
F /;q
/.
/5/./3/2 Corollary /(The q /{Sc hap er Theorem/) Supp ose that /[ n /]
/!
/^q
/6/= /0 in R and let
/ b e a p artition in /
/+
/( d/; n /) /. Then
X
i/> /0
S
/
F
/( i /) / /!
X
/( a/;b /) /2 /[ / /]
/( a/;c /) /2 /[ / /]
b/<c
/
/
p
/(/[ h
/
ab
/]
/^q
/) /? /
p
/(/[ h
/
ac
/]
/^q
/)
/
S
/( /
/1
/;/:/:/: /;/
b
/+ h
/
ab
/;/:/:/: /;/
c
/? h
/
ac
/;/:/:/: /;/
n
/)
F
/:
/5/./3/3 Example Supp ose that R /= C /[ /^ q /] and that p /= /[ m /]
/^q
is a cyclotomic p olyno/-
mial in R for some in teger m / /2/. If / /= /(/3 /; /2/) then/, b y Example /5/./2/8/,
X
i/> /0
W
/
F
/( i /) / /! /
p
/(/[/2/]
/^q
/) W
/(/3 /; /1
/2
/)
F
/+
/
/
p
/(/[/3/]
/^q
/) /? /
p
/(/[/4/]
/^q
/)
/
W
/(/1
/5
/)
F
/+ /
p
/(/[/4/]
/^q
/) W
/(/2
/2
/; /1/)
/:
No w/, /
p
/(/[ k /]
/^q
/) /= /1 if m divides k and /
p
/(/[ k /]
/^q
/) /= /0 otherwise/. Recall that e is the
smallest p ositiv e in teger suc h that /[ e /]
q
/= /0 /(in F /)/; therefore/, W
/
F
is irreducible /(that
is W
/
F
/= L
/
F
/)/, if and only if e /> /4/.
/6/0 /5/. THE JANTZEN/{SCHAPER THEOREM
Next assume that p /= /1 /+ /^ q /; then F /= C and q /= /? /1/, so e /= /2/. Therefore/,
/
p
/(/[/2/]
/^q
/) /= /
p
/(/[/4/]
/^q
/) /= /1 and /
p
/(/[/3/]
/^q
/) /= /0/. Consequen tly /,
X
i/> /0
W
/(/3 /; /2/)
F
/( i /) / /! W
/(/3 /; /1
/2
/)
F
/+ W
/(/2
/2
/; /1/)
F
/? W
/(/1
/5
/)
F
/:
F urther applications of the sum form ula sho ws that W
/(/1
/5
/)
F
/= L
/(/1
/5
/)
F
/, W
/(/2
/2
/; /1/)
F
/= L
/(/2
/2
/; /1/)
F
and W
/(/3 /; /1
/2
/)
F
/ /! L
/(/3 /; /1
/2
/)
F
/+ L
/(/1
/5
/)
F
/+ L
/(/2
/2
/; /1/)
/. The comp osition factors of W
/(/3 /; /1
/2
/)
F
are
completely determined here b ecause the m ultiplicities giv en b y the sum form ula
are /0 or /1/. Com bining these facts sho ws that
P
i/> /0
W
/(/3 /; /2/)
F
/ /! L
/(/3 /; /1
/2
/)
F
/+ /2 L
/(/2
/2
/; /1/)
F
/;
consequen tly /, d
/(/3 /; /2/)/(/3 /; /1
/2
/)
/= /1 and d
/(/3 /; /2/)/(/2
/2
/; /1/)
is either /1 or /2/.
Next consider the Sp ec h t mo dule S
/
F
/; as b efore w e ha v e
X
i/> /0
S
/
F
/( i /) / /! /
p
/(/[/2/]
/^q
/) S
/(/3 /; /1
/2
/)
F
/+
/
/
p
/(/[/3/]
/^q
/) /? /
p
/(/[/4/]
/^q
/)
/
S
/(/1
/5
/)
F
/+ /
p
/(/[/4/]
/^q
/) S
/(/2
/2
/; /1/)
/:
Supp ose once more that p /= /1 /+ q /. A calculation similar to the ab o v e sho ws that
P
i/> /0
S
/(/3 /; /2/)
F
/( i /) / /! /2 D
/(/2
/2
/; /1/)
F
/. Therefore/, S
/(/3 /; /2/)
F
/
/=
D
/(/2
/2
/; /1/)
F
b y coun ting dimensions/;
hence/, d
/(/3 /; /2/)/(/2
/2
/; /1/)
/= /1 b y Prop osition /4/./1/9/(iii/)/.
A t this p oin t w e ha v e calculated all but the last t w o ro ws of the decomp osition
matrix of S
C /; /? /1
/( d/; /5/) where d / /5/. Tw o further applications of the sum form ula
giv e the remaining en tries/; the full matrix is as follo ws/.
/1
/5
/1
/2 /; /1
/3
/: /1
/2
/2
/; /1 /: /: /1
/3 /; /1
/2
/1 /: /1 /1
/3 /; /2 /: /: /1 /1 /1
/4 /; /1 /: /1 /: /: /: /1
/5 /1 /: /: /1 /: /: /1
By Prop osition /4/./1/9/, the submatrix of b old faced en tries is the decomp osition matrix
of H
C /; /? /1
/.
Notice that di/erence b et w een these calculations for W eyl and Sp ec h t mo dules
arises b ecause D
/
F
/= /0 whenev er the partition / is not e /{restricted /(in particular/,
the partition /(/3 /; /2/) is not /2/{restricted/)/.
/3/. The blo c ks of S /( d/; n /) and H
Throughout this section w e assume that d / n /. In this case/, w e use the sum
form ula /(/5/./3/1/) to classify the blo c ks of the q /{Sc h ur algebras S /( d/; n /) and/, from this/,
classify the blo c ks of H /. In order to classify the blo c ks w e /rst de/ne the e /{core
of a partition/.
Recall the de/nition of rim ho ok from the previous section/. W e call a rim ho ok
R
/
ij
an e /{rim ho ok if it is a rim ho ok of length e /; that is if l
/
ij
/= e /.
Let / b e a partition of n /. If the diagram of / con tains an e /{rim ho ok let /
/1
b e
the partition of n /? e obtained b y un wrapping this rim ho ok/. Similarly /, let /
/2
b e the
partition obtained from /
/1
b y un wrapping an e /{rim ho ok/, if p ossible/. Con tin uing
in this w a y w e obtain a sequence of partitions / /= /
/0
/; /
/1
/; /: /: /: /; /
w
with w / /0 and
suc h that the diagram of /
w
con tains no e /{rim ho ok and the partition /
i
is obtained
from /
i /? /1
b y un wrapping an e /{rim ho ok for i /= /1 /; /: /: /: /; w /. The partition /
w
is the
e /{co re of / /; it is a partition of n /? w e /.
/3/. THE BLOCKS OF S /( d/; n /) AND H /6/1
F or example/, if / /= /(/4 /; /3 /; /2 /; /1/) then one sequence of partitions leading to the
/3/{core of / is the follo wing/.
/ /
/
/!
/ /
/
/!
/
/ /
/! /;
so the /3/{core of / is the partition /(/1/)/. It is not at all clear that the e /{core do es
not dep end up on the order in whic h the rim ho oks are remo v ed/. The next Lemma
sho ws that this is not the case/.
/5/./3/4 Lemma The e /{c or e of a p artition is wel l de/ne d/.
Pro of/. Let / /= /( /
/1
/; /: /: /: /; /
n
/) b e the sequence of b eta n um b ers for the partition / /.
Think of the b eta n um b ers as b eing arranged on an ab acus with e /{runners/, where
the b ead p ositions on the abacus are n um b ered from left to righ t as /0 /; /1 /; /: /: /: /; e /? /1 in
the /rst ro w/, e/; e /+ /1 /; /: /: /: /; /2 e /? /1 in the second ro w and so on/. F or example/, if e /= /3
and / /= /(/4 /; /3 /; /2 /; /1/) as ab o v e then / /= /(/1/3 /; /1/1 /; /9 /; /7 /; /5 /; /4 /; /3 /; /2 /; /1 /; /0/) is the sequence of
b eta n um b ers for / and they are represen ted on an abacus as follo ws/.
/ / /
/ / /
/ / /
/ / /
/ / /
/ / /
By Lemma /5/./2/6/, un wrapping an e /{ho ok from / corresp onds to decreasing some
b eta n um b er /
i
b y e /; this is the same as mo ving a b ead one ro w higher in some
column of the abacus/. Consequen tly /, the e /{core of / corresp onds to pushing all of
the b eads up to their highest p ossible p ositions in eac h column of the abacus/. In
particular/, the e /{core is indep enden t of the sequence of rim ho oks remo v ed/.
/5/./3/5 Lemma L et M b e an S
F /;q
/( d/; n /) /{mo dule and supp ose that al l of the c omp o/-
sition factors of M b elong to the same blo ck and that M / /!
P
/
a
/
W
/
F
for some
inte gers a
/
/, / /2 /
/+
/( d/; n /) /. Then W
/
F
and M lie in the same blo ck whenever a
/
/6/= /0 /.
Pro of/. By Lemma /5/./3/0 a virtual mo dule
P
/
a
/
W
/
F
/ /! /0 if and only if a
/
/= /0
for all / /2 /
/+
/( d/; n /)/. Hence/, the Lemma follo ws b y applying a suitable sum of blo c k
idemp oten ts/.
/5/./3/6 Theorem Supp ose that F is a /eld and that d / n /. Then the Weyl mo dules
W
/
F
and W
/
F
b elong to the same blo ck if and only if / and / have the same e /{c or e/.
Pro of/. By Theorem /5/./3/1 the comp osition factors of W
/
F
/, apart from L
/
F
itself/, are
of the form L
/
F
where the partition / is obtained b y un wrapping a rim ho ok from
/ and wrapping it bac k on lo w er do wn in the resulting diagram/. Supp ose that W
/
F
app ears with non/{zero co e/cien t in the Jan tzen sum form ula for W
/
F
/. Then there
exist no des /( a/; b /) and /( a/; c /) in the diagram of / suc h that /
p
/(/[ h
/
ab
/]
/^q
/) /6/= /
p
/(/[ h
/
ac
/]
/^q
/)
and / can b e obtained from / b y un wrapping the rim ho ok R
/
ac
and wrapping it
bac k on lo w er do wn/. No w/, if h is an in teger and /
p
/(/[ h /]
/^q
/) /6/= /0 then /[ h /]
/^q
/2 p
i
R /;
therefore/, /[ h /]
q
/= /0 in F and/, consequen tly /, e divides h /. It follo ws that e m ust divide
/6/2 /5/. THE JANTZEN/{SCHAPER THEOREM
at least one of h
/
ab
and h
/
ac
/. If e j h
/
ac
then / is obtained from / b y mo ving a n um b er
of e /{ho oks and so / and / ha v e the same e /{core/. If e do es not divide h
/
ac
then e
divides h
/
ab
and it is easy to see that / can b e obtained from / b y /\sliding/" the
/( a/; b /)/{rim ho ok/; th us again/, / and / ha v e the same e /{core/. Consequen tly /, if W
/
F
and W
/
F
are in the same blo c k then / and / ha v e the same e /{core/.
No w supp ose that / is an e /{core of some partition of n /; then j / j /= n /? ew for
some w / /0/. Let /
 /= /( /
/1
/; /
/2
/; /: /: /: /) b e the partition of r for whic h /
/1
/= /
/1
/+ w e and
/
i
/= /
i
for i /> /1/. Then /
 has e /{core / /.
Assume that / /` r and that / has e /{core / /. T o pro v e the theorem it su/ces
to sho w that W
/
F
and W
/
F
are in the same blo c k/. Supp ose that / /6/= /
 /. Then/, for
some /( a/; b /) the rim ho ok R
/
ab
of /[ / /] has length e and its lo w est no de is in a ro w
later than the /rst ro w/. Remo v e this rim ho ok from /[ / /] and add it bac k at the
end of the /rst ro w of /[ / /]/, to obtain the diagram /[ / /]/, sa y /. Then W
/
F
app ears with
non/{zero m ultiplicit y in
P
i/> /0
W
/
F
/( i /) b y Theorem /5/./3/1/; therefore/, W
/
F
and W
/
F
are
in the same blo c k b y Lemma /5/./3/5/. This pro v es the Theorem b ecause/, b y induction/,
W
/
F
and W
/
F
are already in the same blo c k/.
W e can no w classify the blo c ks of H /. A t /rst sigh t/, it is p ossible that there
could exist W eyl mo dules W
/
F
and W
/
F
whic h are in the same blo c k of S /( d/; n /) and
suc h that the Sp ec h t mo dules S
/
F
and S
/
F
are in di/eren t blo c ks of H /; for example/,
the W eyl mo dules W
/
F
and W
/
F
could b e link ed via an irreducible mo dule L
/
in
S /( d/; n /) where / is partition whic h is not e /{restricted/. The next result sho ws that
this do es not happ en/.
/5/./3/7 Corollary /(Dipp er/{James/, James/{Mathas/) Supp ose that / and / ar e
p artitions of r /. Then the H
F
/( S
r
/) /{mo dules S
/
F
and S
/
F
b elong to the same blo ck if
and only if / and / have the same e /{c or e/.
Pro of/. By Prop osition /4/./1/9 and Theorem /5/./3/6/, S
/
F
and S
/
F
are in the same blo c k
only if / and / ha v e the same e /{core/. Th us/, to complete the pro of it su/ces to
sho w that S /( d/; n /) has at least as man y blo c ks as H /.
Let M /=
L
/
M
/
/; then S /( d/; n /)
/
/=
End
H
/( M /)/. W rite H /= B
/1
/ / / / / B
k
as
a direct sum of blo c k ideals/. Since M con tains H as a submo dule/, M B
i
/6/= /0 for
i /= /1 /; /2 /; /: /: /: /; k /; moreo v er/, if i /6/= j then M B
i
/\ M B
j
/= /0/. Therefore/, M /= M H /=
M /( B
/1
/ / / / / B
k
/) /= M B
/1
/ / / / / M B
k
and so
End
H
/( M /) /= End
H
/( M B
/1
/ / / / / M B
k
/) /= End
B
/1
/( M B
/1
/) / / / / / End
B
k
/( M B
k
/) /;
since if i /6/= j then Hom
H
/( B
i
/; B
j
/) /= /0 b ecause B
i
and B
j
ha v e no common ir/-
reducible consituen ts b y Theorem /2/./2/1/. Therefore/, the n um b er of blo c k ideals
con tained in S /( d/; n /) is at least as great the n um b er of blo c ks in H /. The Corollary
follo ws/.
Supp ose that / is a partition of n with e /{core / /. Then / is a partition of k for
some k / n and k /+ w e for some w / /0/. W e sa y that / is a partition of e /{w eight
w /.
If / has e /{w eigh t /0 then / is an e /{core and / is the only partition in its blo c k/;
th us/, P
/
F
/= W
/
F
/= L
/
F
is irreducible and pro jectiv e/. The structure of the W eyl
mo dules indexed b y partitions of e /{w eigh t /1 are also easy to describ e/.
/5/./3/8 Prop ositi on /(James/) Supp ose that n /= m /+ e and let / b e a p artition of m
which is an e /{c or e/. Then ther e exist pr e cisely e p artitions /
/1
B /
/2
B / / / B /
e
of n
/4/. IRREDUCIBLE SPECHT MODULES AND WEYL MODULES /6/3
whose e /{c or e is / /. F urthermor e/, if / /6/= /
k
is a p artition of n then d
//
k /= /
//
k /+/1
for k /= /1 /; /: /: /: /; e /? /1 /.
Pro of/. The en umeration of the w eigh t /1 partitions is easy /(for example/, think of
the abaci of Lemma /5/./3/4/)/. Hence/, for k /= /1 /; /2 /; /: /: /: /; e
X
i/> /0
W
/
k
F
/( i /) / /!
X
j />k
/( /? /1/)
j /? k /+/1
W
/
j
F
b y the Jan tzen sum form ula /(/5/./3/1/)/. In particular/, W
/
e
F
/= L
/
e
F
is reducible/. If
/1 / k /< e it no w follo ws easily b y induction that W
/
k
F
/ /! L
/
k
F
/+ L
/
k /+/1
F
as w e
wished to sho w/.
/4/. Irreducibl e Sp ec h t mo dules and W eyl mo dules
In the last section of these notes w e classify the irreducible W eyl mo dules and
the irreducible Sp ec h t mo dules whic h are indexed b y e /{restricted partitions/. The
/rst t w o results dep end up on the c hoice of Jan tzen /ltration/; our /nal result will
dep end only up on the /eld and on q /.
As in Section /2 w e /x a principal ideal domain R /, an in v ertible elemen t /^ q /2 R
and a prime p in R and let F /= R/= p and q /= /^ q /+ p R /.
/5/./3/9 Theorem Supp ose that / /2 /
/+
/( d/; n /) and that /[ n /]
/!
/^q
/6/= /0 in R /. Then the Weyl
mo dule W
/
F
is irr e ducible if and only if /
p
/(/[ h
/
ab
/]
/^q
/) /= /
p
/(/[ h
/
ac
/]
/^q
/) for al l /( a/; b /) and
/( a/; c /) in /[ / /] /.
Pro of/. If /
p
/(/[ h
/
ab
/]
/^q
/) /= /
p
/(/[ h
/
ac
/]
/^q
/) for all /( a/; b /) and /( a/; c /) /2 /[ / /] then
P
i/> /0
W
/
F
/( i /) /= /0
b y Theorem /5/./3/1/; in particular/, Lemma /5/./3/0 no w sho ws that rad W
/
F
/= /0/, so W
/
F
is irreducible/.
Con v ersely /, supp ose that /
p
/(/[ h
/
ab
/]
/^q
/) /6/= /
p
/(/[ h
/
ac
/]
/^q
/) for some no des /( a/; b /) and /( a/; c /)
in /[ / /]/. Cho ose a/; b and c so that the partition / whose sequence of b eta n um b ers
is /( /
/1
/; /: /: /: /; /
b
/+ h
/
ab
/; /: /: /: /; /
c
/? h
/
ac
/; /: /: /: /; /
n
/) is minima l in the dominance ordering
among all the partitions app earing on the righ t hand side of the equation in The/-
orem /5/./3/1/. Then / B / and L
/
F
is a comp osition factor of
P
i/> /0
W
/
F
/( i /)/. Hence/, L
/
F
is a comp osition factor of W
/
F
and W
/
F
is not irreducible/.
The irreduciblit y of the Sp ec h t mo dules is more subtle/; indeed/, the classi/cation
of the irreducible Sp ec h t mo dules ev en in the case of the symmetric groups is an
op en problem /(except in c haracteristic /2/; see /[ /4/1 /]/)/. Ho w ev er/, as the next result
sho ws/, the answ er is kno wn when / is e /{restricted/.
/5/./4/0 Theorem Supp ose that /[ n /]
/!
/^q
/6/= /0 in R and let / b e an e /{r estricte d p artition
of n /. Then S
/
F
is an irr e ducible H /{mo dule if and only if /
p
/(/[ h
ab
/]
/^q
/) /= /
p
/(/[ h
ac
/]
/^q
/)
for al l no des /( a/; b /) and /( a/; c /) in /[ / /] /.
Pro of/. First supp ose that S
/
F
/= D
/
F
/. Then the Gram matrix of the S
/
F
with
resp ect to its standard basis f m
t
g is non/{zero/. By Corollary /5/./1/1 and Theorem /5/./2/7
this determinan t is equal to
G
/
/!
/= q
N
Y
/( a/;b /) /2 /[ / /]
/( a/;c /) /2 /[ / /]
b/<c
/
/[ h
/
ab
/]
q
/[ h
/
ac
/]
q
/
d
/!
/( /
/1
/;/:/:/: /;/
b
/+ h
/
ab
/;/:/:/: /;/
c
/? h
/
ab
/;/:/:/: /;/
n
/)
/;
/6/4 /5/. THE JANTZEN/{SCHAPER THEOREM
for some N /2 N /. Supp ose that d / n /. Then / /2 /
/+
/( d/; n /) and the S
F /;q
/( d/; n /) /{
mo dule W
/
F
is irreducible if and only if its Gram matrix G
/
is non/{zero/. By
Theorem /5/./2/7 again/,
G
/
/=
Y
/ /2 //( d/;n /)
G
/
/
/= q
M
Y
/ /2 //( d/;n /)
Y
/( a/;b /) /2 /[ / /]
/( a/;c /) /2 /[ / /]
b/<c
/
/[ h
/
ab
/]
q
/[ h
/
ac
/]
q
/
d
/
/( /
/1
/;/:/:/: /;/
b
/+ h
/
ab
/;/:/:/: /;/
c
/? h
/
ab
/;/:/:/: /;/
n
/)
for some M /2 N /. Moreo v er/, d
/
/( /
/1
/; /: /: /: /; /
n
/) is non/{zero only if d
/!
/( /
/1
/; /: /: /: /; /
n
/) /6/=
/0 for an y partition / /. Therefore/, if S
/
F
/= D
/
F
then W
/
F
is irreducible/; whence/,
/
p
/(/[ h
ab
/]
/^q
/) /= /
p
/(/[ h
ac
/]
/^q
/) for all no des /( a/; b /) and /( a/; c /) in /[ / /] b y Theorem /5/./3/9/.
The con v erse is m uc h easier b ecause S
/
F
/ /! D
/
F
/+ rad S
/
F
and D
/
F
/6/= /0 since
/ is e /{restricted/. Therefore/, S
/
F
/= D
/
F
if /
p
/(/[ h
ab
/]
/^q
/) /= /
p
/(/[ h
ac
/]
/^q
/) for all no des /( a/; b /)
and /( a/; c /) in /[ / /] b y Corollary /5/./3/2/.
The last t w o results dep ended up on the c hoice of R /, /^q and p /, and not directly
up on F and q /; our /nal Theorem remo v es this restriction/.
Fix a /eld F and a non/{zero elemen t q in F /. Let /^q b e an determinan t o v er F
and let R /= F /[ /^ q /] and p /= /^q /? q /. Then R is a principal ideal domain/, p is a prime
and /[ n /]
/!
/^q
/6/= /0/. F urthermore/, F
/
/=
R/= p R and S
F /;q
/( d/; n /)
/
/=
S
R/; /^q
/( d/; n /) /
R
F so w e are
in a situation where all of the results of this section apply /.
Recall that e is the smallest p ositiv e in teger suc h that /[ e /]
q
/= /0/. Notice that
/[ k /]
q
/= /0 if and only if /[ k /]
/^q
/2 p R /. If F is a /eld of c haracteristic /0 set p /= /1 /;
otherwise/, let p b e the c haracteristic of F /. De/ne /
p
to b e the usual p /{adic v aluation
on N /. /(If p /= /1 then/, b y con v en tion/, /
p
/( k /) /= /0 for all k /2 N /./)
/5/./4/1 Lemma L et a and b b e inte gers with /1 / a / n and /1 / b / n /. Then
/
p
/(/[ a /]
/^q
/) /= /
p
/(/[ b /]
/^q
/) if and only if either
/(i/) e /- a and e /- b /; or/,
/(ii/) e j a and e j b and /
p
/( a /) /= /
p
/( b /) /.
Pro of/. W e ha v e already observ ed that e is the smallest p ositiv e in teger suc h that
p divides /[ e /]
/^q
/. Therefore/, if k /2 N then p divides /[ k /]
/^q
if and only if e divides k /. It
follo ws that /
p
/(/[ a /]
/^q
/) /= /
p
/(/[ b /]
/^q
/) only if either /(i/) e /- a and e /- b /, or /(ii/) e j a and e j b /.
If e /- a and e /- b then /
p
/(/[ a /]
/^q
/) /= /
p
/(/[ b /]
/^q
/) /= /0 and there is nothing to pro v e/.
Hence w e ma y assume that e j a and e j b /.
First consider the case where p /= /1 /. If k /2 N then /[ k e /]
/^q
/= /[ e /]
/^q
/[ k /]
/^q
e
and
/[ k /]
/^q
e
/ k /1
R
mo d p since p divides /^q
e
/? /1/. Therefore/, /
p
/(/[ k e /]
/^q
/) /= /
p
/(/[ e /]
/^q
/) since
p /- k /1
R
/. Hence/, /
p
/(/[ a /]
/^q
/) /= /
p
/(/[ b /]
/^q
/) /= /
p
/(/[ e /]
/^q
/) and the Lemma holds in this case/.
No w consider the case where F is a /eld of p ositiv e c haracteristic/. W rite a /=
eup
x
and b /= ev p
y
where p do es not divide u or v /. Then
/
p
/(/[ a /]
/^q
/) /= /
p
/(/[ b /]
/^q
/) /( /) /
p
/( /^ q
a
/? /1
R
/) /= /
p
/( /^ q
b
/? /1
R
/)
/( /) /
p
/?
/( /^ q
ep
x
/? /1
R
/)/[ u /]
/^q
ep
x
/
/= /
p
/?
/( /^ q
ep
y
/? /1
R
/)/[ v /]
/^q
ep
y
/
/( /) /
p
/( /^ q
ep
x
/? /1
R
/) /= /
p
/( /^ q
ep
y
/? /1
R
/) /;
the last line follo wing b ecause /[ u /]
/^q
ep
x
/ u /1
R
mo d p /, since p divides /^q
e
/? /1
R
/, and
u /1
R
/6/ /0 mo d p /(and similarly for /[ v /]
/^q
ep
y
/)/. No w/, if y /> x then /^q
ep
y
/? /1
R
/=
/( /^ q
ep
x
/? /1
R
/)/[ p
y /? x
/]
/^q
ep
x
/. Ho w ev er/, /[ p
y /? x
/]
/^q
ep
x
/ p
y /? x
/1
R
/ /0 mo d p /, so this forces
NOTES ON CHAPTER /5 /6/5
/
p
/( /^ q
ep
y
/? /1
R
/) /> /
p
/( /^ q
ep
x
/? /1
R
/)/. Therefore/,
/
p
/(/[ a /]
/^q
/) /= /
p
/(/[ b /]
/^q
/) /( /) /
p
/( a /) /= /
p
/( b /) /;
completing the pro of of the Lemma/.
Giv en partitions / /= /( /
/1
/; /
/2
/; /: /: /: /) and / /= /( /
/1
/; /
/2
/; /: /: /: /) and m /2 N /, w e de/ne / /+
/ to b e the partition /( /
/1
/+ /
/1
/; /
/2
/+ /
/2
/; /: /: /: /) and m/ to b e the partition /( m/
/1
/; m/
/2
/; /: /: /: /)/.
Recall that /
/0
is the partition whic h is conjugate to / /.
/5/./4/2 Theorem /(James/{Mathas/) Supp ose that F is a /eld of char acteristic p
and let / b e an e /{r e gular p artition of r /. Then the S
/
F
is irr e ducible if and only if
ther e exist p artitions /
/(/1/)
/; /
/(/2/)
/; /: /: /: and /
/(/1/)
/; /
/(/2/)
/; /: /: /: such that
/(i/) /
/0
/= /
/(/1/)
/+ e/
/(/1/)
/, /
/(/1/)
is an e /{c or e/, and /
/(/1/)
i
/= /
/(/1/)
i /? /1
/+ e /? /1 for al l i with
/
/(/1/)
i
/6/= /0 /; and
/(ii/) for al l j / /1 /, /
/( j /)
/= /
/( j /+/1/)
/+ p/
/( j /+/1/)
/, /
/( j /+/1/)
is a p /{c or e/, and /
/( j /+/1/)
i
/= /
/( j /+/1/)
i /? /1
/+
p /? /1 for al l i with /
/( j /+/1/)
i
/6/= /0 /.
Pro of/. If e /= /1 /, then S
/
F
is alw a ys irreducible/; in this case tak e /
/(/1/)
/= / and let
the partitions /
/(/2/)
/; /: /: /: /; /
/(/1/)
/; /
/(/2/)
/; /: /: /: b e partitions of /0/. Th us/, w e ma y assume that
e /6/= /1 /.
By Theorem /5/./4/0 and Lemma /5/./4/1/, S
/
F
is irreducible if and only if for all no des
/( a/; b /) and /( a/; c /) in /[ / /] either e /- h
/
ab
and e /- h
/
ac
/, or e j h
/
ab
and e j h
/
ac
and
/
p
/( h
/
ab
/) /= /
p
/( h
/
ac
/)/. W e sho w that this condition is equiv alen t to /(i/) and /(ii/) ab o v e/.
Dra w the diagram /[ /
/0
/] and circle those no des whic h ha v e ho ok lengths divisible
b y e /, as in Example /5/./4/3 b elo w/. The condition that for all /( a/; b /) and /( a/; c /) /2 /[ / /]
either e /- h
/
ab
and e /- h
/
ac
/, or e j h
/
ab
and e j h
/
ac
amoun ts to sa ying that in eac h
column of /[ /
/0
/] either no no de is circled or ev ery no de is circled/. By remo ving an
e /{rim ho ok from the righ tmost column whic h con tains a circled no de and using
induction this is equiv alen t to /(i/)/. Assume therefore that condition /(i/) holds/.
Supp ose that the /( a/; b /)/{no de of /[ / /] is circled /(ie/. e divides h
/
ab
/)/, and that /( a/; b /)
lies in the r /{th column of circled no des in /[ /
/0
/]/. Then h
/
ab
/= eh
/
/(/1/)
r b
/. Therefore/,
/
p
/( h
/
ab
/) /= /
p
/( h
/
ac
/) for all c with /( a/; c /) /2 /[ / /] if and only if /
p
/( h
/
/(/1/)
r b
/) /= /
p
/( h
/
/(/1/)
r c
/) for
all c with /( r /; c /) /2 /[ /
/(/1/)
/]/. Replace / b y /
/(/1/)
/0
/, e b y p and iterate this argumen t to
complete the pro of/.
/5/./4/3 Example Supp ose that / /= /(/4 /; /3
/3
/; /2
/5
/; /1
/2
/) and e /= /3/. W e illustrate /[ /
/0
/]/,
marking those no des in the e /{core b y / and circling those no des whic h ha v e ho ok
lengths divisible b y e /.
/[ /
/0
/] /=
/ /
 / / / /
/ /
 / /
/ /
/
Therefore/, b y Theorem /5/./4/0/, S
/
F
is irreducible when F is a /eld of c haracteristic /0/. In
this case/, the decomp osition of /
/0
giv en b y Theorem /5/./4/2 is /
/0
/= /(/5 /; /3 /; /1
/2
/) /+ /3/(/2
/2
/; /1/)/.
If F is a /eld of c haracteristic /3 then the analogous diagram for /
/(/1/)
is
/ /
/
/; so S
/
F
is not irreducible when p /= /3/.
Notes on Chapter /5
/1/. The b eta n um b ers used in the pro of of Theorem /5/./2/7 w ere in tro duced b y Little/-
w o o d /[ /5/3 /]/. The abaci of Lemma /5/./3/4 are due to James /[ /3/7 /]/.
/6/6 /5/. THE JANTZEN/{SCHAPER THEOREM
/2/. The com binatorics underpinning the pro of of Theorem /5/./2/7 w ere in tro duced
b y James and Murph y /[ /4/2 /] /(see also /[ /5/4 /]/)/; they consider the corresp onding
result in the represen tation theory of the symmetric group /(ie/. when q /= /1
and / /= /! /)/. The extension of this argumen t to the q /{Sc h ur algebras is due to
James and Mathas /[ /3/9 /]/; w e ha v e basically follo w ed their argumen t adding some
impro v em en ts from /[ /4/0 /]/.
/3/. The W eyl mo dules W
/
of the q /{Sc h ur algebra can also view ed as W eyl mo dules
for the quan tum general linear groups /(see/, for example/, /[ /1/2 /, Theorem /3/./3/./2/]/)/.
Using a geometric argumen t Andersen/, P olo and W en /[ /1 /] pro v ed a sum form ula
for the W eyl mo dules of quan tum groups/; Theorem /5/./3/1 can b e deduced from
their result using the argumen t of Sc hap er/'s thesis /[ /6/0 /]/.
/4/. Jan tzen /[ /4/3 /] pro v ed his sum form ula /rst for the W eyl mo dules of the general
linear groups and later /[ /4/4 /] extended the sum form ula to W eyl mo dules of other
t yp es/. In Jan tzen/'s w ork the sum form ula is expressed in terms of the dot
action of an a/ne W eyl group up on the w eigh t lattice/. Starting with Jan tzen/'s
result/, and guided b y /[ /4/2 /]/, Sc hap er /[ /6/0 /] deduced the com binatorial statemen t of
Corollary /5/./3/2 in the case of the symmetric groups/.
/5/. Necessary and su/cien t conditions for t w o Sp ec h t mo dules of H to b elong to
the same blo c k w ere pro v ed in /[ /1/4 /] and /[ /3/9 /] resp ectiv ely /.
/6/. In the represen tation theory of the symmetric group/, Corollary /5/./3/7 is kno wn as
the Nak a y ama conjecture /(ev en though it has b een pro v ed for a long time/)/. The
elegan t idea of using the double cen tralizer prop ert y to classify the blo c ks of H
is due to K/ onig/.
/7/. Theorem /5/./3/6 classi/es the blo c ks for the q /{Sc h ur algebras when d / n /; when
d /< n the blo c ks of S /( d/; n /) ha v e b een classi/ed b y Co x /[ /9 /]/.
/8/. Prop osition /5/./3/8 /rst app eared in /[ /3/8 /]/. In this pap er James also giv es a series
of /\rules/" whic h partially determine the decomp osition matrices of the q /{Sc h ur
algebras together with tables of decomp osition n um b ers when n / /1/0/.
Notational Index
Chapter /1/.
/1/./1 S
n
The symmetric group on f /1 /; /2 /; /: /: /: /; n g
s
i
The simple transp osition /( i/; i /+ /1/)
S The set f s
/1
/; /: /: /: /; s
n /? /1
g of Co xeter generators for
S
n
/` /( w /) The length of w /2 S
n
/" The sign represen tation of S
n
T The set of re/
ections in S
n
/1/./2 H /= H
R/;q
/( S
n
/) The Iw ahori/{Hec k e algebra of S
n
T
i
/; T
s
The generators T
/1
/; /: /: /: /; T
n /? /1
of H
T
w
A standard basis elemen t of H /, w /2 S
n
Z Z /[ /^ q /; /^q
/? /1
/]/, where /^q is an indeterminate o v er Z
H
Z
The generic Iw ahori/{Hec k e algebra H
Z /; /^q
/( S
n
/)
Chapter /2/.
/2/./1 /(/ /; / /) The p oset indexing the cellular basis
T /( / /) An indexing set for the cellular basis
/
A
/
The span of the c
/
uv
where / /> /
/ The automorphism of A giv en b y c
/
st
/
/= c
/
ts
A
/
The span of the c
/
uv
where / / /
C
/
A /(righ t/) cell mo dule
C
/ /
A left cell mo dule
D
/
C
/
/= rad C
/
/2/./2 d
//
The comp osition m ultiplicit y of D
/
in C
/
Chapter /3/.
/3/./1 /[ / /] The diagram f /( i/; j /) j /1 / j / /
i
and i / /1 g of /
Shap e /( t /) The shap e of the tableau t
s /; t /; /: /: /: /(Standard/) tableau /(of t yp e /! /)
Std/( / /) The set of standard / /{tableaux
t
/
The standard / /-tableau with f /1 /; /2 /; /: /: /: /; n g en/-
tered along its ro ws/.
S
/
The Y oung subgroup S
/
/1
/ S
/
/2
/ / / /
/6/7
/6/8 NOT A TIONAL INDEX
H /( S
/
/) The Iw ahori/{Hec k e algebra of S
n
m
/
P
w /2 S
/
T
w
M
/
The /\p erm utation mo dule/" m
/
H
D
/
The distinguished coset represen tativ es of S
/
in
S
n
d /( t /) The elemen t of S
n
suc h that t /= t
/
d /( t /)
D /; B The dominance order on the set of comp ositions
t /# m The subtableau of t con taining the en tries
/1 /; /2 /; /: /: /: /; m
/3/./2 / The R /{linear an tiautomorphism of H deter/-
mined b y T
/
w
/= T
w
/?
/1
for all w /2 S
n
m
st
T
/
d /( s /)
m
/
T
d /( t /)
M The Murph y basis f m
st
g of H
H
/
The ideal of H with basis the set of m
uv
where
u and v are standard / /{tableau with / D /
/
H
/
The ideal of H with basis the set of m
uv
where
u and v are standard / /{tableau with / B /
/ The set of partitions of n
S
/
The Sp ec h t mo dule indexed b y /
m
t
A Murph y basis elemen t of a Sp ec h t mo dule
D
/
A simple H /{mo dule/; D
/
/= S
/
/= rad S
/
/3/./3 L
k
q
/? /1
T
/( k /? /1 /;k /)
/+ q
/? /2
L
/( k /? /2 /;k /)
/+ / / / /+ q
/1 /? k
T
/(/1 /;k /)
/[ m /]
q
The /\quan tum in teger/" /1 /+ q /+ / / / /+ q
m /? /1
/[ m /]
/!
q
The /\quan tum factorial/" /[/1/]
q
/[/2/]
q
/: /: /: /[ m /]
q
e The smallest p ositiv e in teger suc h that /[ e /]
q
/= /0
res /( x /) The e /{residue of the no de x
f
t
An orthogonal basis elemen t of a simple Sp ec h t
mo dule
/3/./4 d
//
/= /[ S
/
/: D
/
/] The comp osition m ultiplicit y of D
/
in S
/
Chapter /4/.
/4/./1 //( d/; n /) The set of comp ositions of n with at most d parts
S /( d/; n /) The q /{Sc h ur algebra
/! The partition /(/1
n
/)
S /; T /; /: /: /: /(Semistandard/) tableaux of t yp e /
T
/0
/( //; / /) The set of semistandard / /{tableaux of t yp e /
T
/
The unique semistandard / /-tableau of t yp e /
/ /( t /) The tableau of t yp e / obtained from t b y replac/-
ing eac h en try in t b y its ro w index in t
/
/d /\ / The comp osition / suc h that S
/
/= d
/? /1
S
/
d /\ S
/
D
//
The set of distinguished /( S
/
/; S
/
/)/{double coset
represen tativ es
/rst/( T /) See page /3/8
NOT A TIONAL INDEX /6/9
last/( T /) See page /3/8
/4/./2 m
S t
P
s
m
st
where / /( s /) /= S
m
ST
P
s /; t
m
st
where / /( s /) /= S and / /( t /) /= T
/4/./3 /
/+
/( d/; n /) The set of partitions in //( d/; n /)
/'
ST
The map in Hom
H
/( M
/
/; M
/
/) giv en b y /'
ST
/( m
/
/) /=
m
ST
T
/0
/( / /)
S
/ /2 //( d/;n /)
T
/0
/( //; / /)
/
S
/
/( d/; n /) The ideal of S /( d/; n /) with basis the /'
ST
where
S /; T /2 T
/0
/( / /) where / B /
S
/
/( d/; n /) The ideal of S /( d/; n /) with basis the /'
ST
where
S /; T /2 T
/0
/( / /) where / D /
/ The automorphism of S /( d/; n /) determined b y
/'
/
ST
/= /'
TS
W
/
The W eyl mo dule indexed b y /
m
T
P
t
m
t
where / /( t /) /= T
/'
T
The map in Hom
H
/( M
/
/; S
/
/) giv en b y /'
T
/( m
/
/) /=
m
T
L
/
W
/
/= rad W
/
d
//
The comp osition m ultiplicit y of L
/
in W
/
Chapter /5/.
/5/./1 W
/
/
The / /{w eigh t space of W
/
G
/
/
The Gram determinan t of W
/
/
L
/
i
The elemen t of End
H
/( M
/
/) giv en b y L
/
k
/( m
/
/) /=
m
/
/( L
x
/+ L
x /+/1
/+ / / / /+ L
y
/) where x/; /: /: /: /; y are the
en tries in ro w i of t
/
/[res
T
/( k /)/]
q
P
x /: T /( x /)/= k
/[res
T
/( x /)/]
q
/
T
/( q /) See page /4/8/.
/[ / /]
/!
q
/[ /
/1
/]
/!
q
/: /: /: /[ /
k
/]
/!
q
/
/
t
See page /4/9
g
/
/
/( /^ q /)
Q
T
/
T
/( /^ q /)
N
P
T
/` /( d /(last/( T /)/)/)
//; / Sequences of in tegers /(b eta n um b ers/)
d
/
/( / /) See /(/5/./2/1/)
Z The largest in teger with /
Z
/6/= /0
/ The comp osition /( /
/1
/; /: /: /: /; /
Z /? /1
/)
z /
Z
/
C
A sequence of b eta n um b ers/; see page /5/3
n f /1 /; /2 /; /: /: /: /; n g
l
/
ab
The leg length of the a/; b /)th ho ok in /
/5/./2 W
/
F
The /(virtual/) W eyl mo dule corresp onding to the
sequence / of b eta n um b ers
/7/0 NOT A TIONAL INDEX
S
/
F
/(virtual/) Sp ec h t mo dule corresp onding to the se/-
quence / of b eta n um b ers
W
/
F
/( i /) The i th mo dule in the Jan tzen /ltration of W
/
F
Bibliograph y
/[/1/] H/. Andersen/, P/. Polo/, and K/. Wen /, R epr esentations of quantum algebr as /, In v en t/. Math/./,
/1/0/4 /(/1/9/9/1/)/, /1/{/5/9/.
/[/2/] S/. Ariki /, On the de c omp osition numb ers of the He cke algebr a of G /( m/; /1 /; n /)/, J/. Math/. Ky oto
Univ/./, /3/6 /(/1/9/9/6/)/.
/[/3/] A/. Beilinson/, G/. Lusztig/, and R/. Ma cPherson /, A ge ometric setting for the quantum
deformation of GLn /. /, Duk e Matj/. J/./, /6/1 /(/1/9/9/0/)/, /6/5/5/{/6/7/7/.
/[/4/] J/. Br und an /, Mo dular br anching rules for quantum GL
n
and the He cke algebr a of typ e A /,
Pro c/. Lond/. Math/. So c/. /(/3/)/, to app ear/.
/[/5/] /, Quantum line ar gr oups /, CUP /, in preparatio n/.
/[/6/] R/. W/. Car ter /, Finite Gr oups of Lie T yp e /, John Wiley /, New Y ork/, /1/9/8/5/.
/[/7/] /, R epr esentation the ory of the /0/{He cke algebr a /, J/. Algebra/, /1/0/4 /(/1/9/8/6/)/, /8/9/{/1/0/3/.
/[/8/] E/. Cline/, B/. P arshall/, and L/. Scott /, Finite dimensional algebr as and highest weight
c ate gories /, Math/. Ann/./, /2/5/9 /(/1/9/8/2/)/, /1/5/3/{/1/9/9/.
/[/9/] A/. Co x /, The blo cks of the q /{Schur algebr a /, J/. Algebra/, /(to app ear/)/.
/[/1/0/] C/. W/. Cur tis and I/. Reiner /, R epr esentation the ory of /nite gr oups and asso ciative algebr as /,
In terscience/, /1/9/6/2/.
/[/1/1/] /, Metho ds of R epr esentation The ory /, V ols/. I and I I/, John Wiley /, New Y ork/, /1/9/8/7/.
/[/1/2/] R/. Dipper and S/. Donkin /, Quantum GL
n
/, Pro c/. London Math/. So c/. /(/3/)/, /6/3 /(/1/9/9/1/)/, /1/6/5/{/2/1/1/.
/[/1/3/] R/. Dipper and G/. James /, R epr esentations of He cke algebr as of gener al line ar gr oups /, Pro c/.
London Math/. So c/. /(/3/)/, /5/2 /(/1/9/8/6/)/, /2/0/{/5/2/.
/[/1/4/] /, Blo cks and idemp otents of He cke algebr as of gener al line ar gr oups /, Pro c/. London
Math/. So c/. /(/3/)/, /5/4 /(/1/9/8/7/)/, /5/7/{/8/2/.
/[/1/5/] /, The q /{Schur algebr a /, Pro c/. London Math/. So c/. /(/3/)/, /5/9 /(/1/9/8/9/)/, /2/3/{/5/0/.
/[/1/6/] /, q /{T ensor sp ac e and q /{Weyl mo dules /, T rans/. AMS/, /3/2/7 /(/1/9/9/1/)/, /2/5/1/{/2/8/2/.
/[/1/7/] R/. Dipper/, G/. James/, and A/. Ma thas /, Cyclotomic q /{Schur algebr as /, Math/. Zeit/./, to app ear/.
/[/1/8/] S/. Donkin /, The q /{Schur algebr a /, LMS Lecture Notes/, CUP /, /1/9/9/8/.
/[/1/9/] J/. Du /, A note on quantize d Weyl r e cipr o city at r o ots of unity /, Alg/. Collo q/./, /2 /(/1/9/9/5/)/, /3/6/3/{/3/7/2/.
/[/2/0/] J/. Du and H/. R ui /, Base d algebr as and standar d b ases for quasi/{her e ditary algebr as /, T rans/.
AMS/./, /(to app ear/)/.
/[/2/1/] J/. Du and L/. Scott /, The q /{Schur
/2
algebr a /, T rans/. AMS/, /(to app ear/)/.
/[/2/2/] M/. J/. D yer /, R e/
e ctions in Coxter gr oups /, PhD thesis/, Univ ersit y of Sydney /, /1/9/8/7/.
/[/2/3/] M/. J/. D yer /, R e/
e ction sub gr oups of Coxeter systems /, J/. Algebra/, /1/3/5 /(/1/9/9/0/)/, /5/7/{/7/3/.
/[/2/4/] M/. Geck and G/. Pfeiffer /, On the irr e ducible char acters of He cke algebr as /, Adv ances/, /1/0/2
/(/1/9/9/3/)/, /7/9/{/9/4/.
/[/2/5/] J/. J/. Graham /, Mo dular r epr esentations of He cke algebr as and r elate d algebr as /, PhD thesis/,
Univ ersit y of Sydney /, /1/9/9/5/.
/[/2/6/] J/. J/. Graham and G/. I/. Lehrer /, Cel lular algebr as /, In v en t/. Math/./, /1/2/3 /(/1/9/9/6/)/, /1/{/3/4/.
/[/2/7/] J/. A/. Green /, Polynomial r epr esentations of GL
n
/, SLN/, /8/3/0 /, Springer/{V erla g/, New Y ork/,
/1/9/8/0/.
/[/2/8/] /, Combinatorics and the Schur algebr a /, J/. Pure Appl/. Algebra/, /8/8 /(/1/9/9/3/)/, /8/9/{/1/0/6/.
/[/2/9/] R/. Green /, q /{Schur algebr as and quantize d enveloping algebr as /, PhD thesis/, Univ ersit y of
W arwic k/, /1/9/9/5/.
/[/3/0/] I/. Gr ojno wski /, R epr esentations of a/ne He cke algebr as /(and a/ne quantum GL
n
/) at r o ots
of unity /, Math/. Researc h Notes/, /(/1/9/9/4/)/, /2/1/5/{/2/1/7/.
/[/3/1/] A/. Gyoja and K/. Uno /, On the semisimplicity of He cke algebr as /, J/. Math/. So c/. Japan/, /4/1
/(/1/9/8/9/)/, /7/5/{/7/9/.
/7/1
/7/2 BIBLIOGRAPHY
/[/3/2/] P/. N/. Hoefsmit /, R epr esentations of He cke algebr as of /nite gr oups with B N /{p airs of classic al
typ e /, PhD thesis/, Univ ersit y of British Colum bia/, /1/9/7/9/.
/[/3/3/] J/. E/. Humphreys /, R e/
e ction Gr oups and Coxeter Gr oups /, Cam bridge Univ ersit y Press/, Cam/-
bridge/, /1/9/9/0/.
/[/3/4/] N/. Iw ahori /, On the structur e of the He cke ring of a Cheval ley gr oup over a /nite /eld /, J/.
F ac/. Sci/. U/. T oky o/, /1/0 /(/1/9/6/4/)/, /2/1/4/{/2/3/6/.
/[/3/5/] G/. D/. James /, On the de c omp osition matric es of the symmetric gr oups II /, J/. Algebra/, /4/3
/(/1/9/7/6/)/, /4/5/{/5/4/.
/[/3/6/] /, The r epr esentation the ory of the symmetric gr oups /, SLN/, /6/8/2 /, Springer/{V erla g/, New
Y ork/, /1/9/7/8/.
/[/3/7/] /, Some c ombinatorial r esults involving Y oung diagr ams /, Pro c/. Cam b/. Phil/. So c/./, /8/3
/(/1/9/7/8/)/, /1/{/1/0/.
/[/3/8/] G/. D/. James /, The de c omp osition matric es of GL
n
/( q /) for n / /1/0/, Pro c/. London Math/. So c/.
/(/3/)/, /6/0 /(/1/9/9/0/)/, /2/2/5/{/2/6/4/.
/[/3/9/] G/. D/. James and A/. Ma thas /, A q /{analo gue of the Jantzen/{Schap er the or em /, Pro c/. London
Math/. So c/. /(/3/)/, /7/4 /(/1/9/9/7/)/, /2/4/1/{/2/7/4/.
/[/4/0/] /, The cyclotomic Jantzen/{Schap er the or em /, preprin t/, /(/1/9/9/8/)/.
/[/4/1/] /, The irr e ducible Sp e cht mo dules in char acteristic /2/, preprin t/, /(/1/9/9/8/)/.
/[/4/2/] G/. D/. James and G/. E/. Murphy /, The determinant of the Gr am matrix for a Sp e cht mo dule /,
J/. Algebra/, /5/9 /(/1/9/7/9/)/, /2/2/2/{/2/3/5/.
/[/4/3/] J/. C/. Jantzen /, Darstel lungen halb einfacher algebr aischer Grupp en und zuge or dnete kon/-
tr avariante F ormen /, Bonner Math/. Sc h/./, /6/7 /(/1/9/7/3/)/.
/[/4/4/] /, Weyl mo dules for gr oups of Lie typ e /, in Finite Simple Groups I I/: Pro c/. LMS Symp o/-
sium/, Durham /1/9/7/8/, M/. Collins/, ed/./, Academic Press/, /1/9/8/0/.
/[/4/5/] A/. A/. Jucys /, On the Y oung op er ators of the symmetric gr oups /, Lith uanian Ph ys/. J/./, /1/1
/(/1/9/7/1/)/, /1/{/1/0/.
/[/4/6/] D/. Kazhd an and G/. Lusztig /, R epr esentations of Coxeter gr oups and He cke algebr as /, In v en t/.
Math/./, /5/3 /(/1/9/7/9/)/, /1/6/5/{/1/8/4/.
/[/4/7/] D/. Knuth /, The A rt of Computer Pr o gr amming /, v ol/. /3 /, Addison/{W esley /, Massac h usetts/,
/1/9/7/3/.
/[/4/8/] S/. K
/
onig and C/. Xi /, Cel lular algebr as/: in/
ations and morita e quivalenc e s /, preprin t/, /(/1/9/9/8/)/.
/[/4/9/] /, On the numb er of c el ls of a c el lular algebr a /, preprin t/, /(/1/9/9/8/)/.
/[/5/0/] /, On the structur e of c el lular algebr as /, Pro ceedings of ICRA VI I I/, AMS/, to app ear/.
/[/5/1/] A/. Lascoux/, B/. Lecler c/, and J/./-Y/. Thibon /, He cke algebr as at r o ots of unity and crystal
b ases of quantum a/ne algebr as /, Comm/. Math/. Ph ys/./, /1/8/1 /(/1/9/9/6/)/, /2/0/5/{/2/6/3/.
/[/5/2/] G/. I/. Lehrer /, A survey of He cke algebr as and A rtin br aid gr oups /, Con/. Math/./, /7/8 /(/1/9/8/8/)/,
/3/6/5/{/3/8/5/.
/[/5/3/] D/. E/. Littlew ood /, Mo dular r epr esentations of symmetric gr oups /, Pro c/. Ro y al So c/. A/, /2/0/9
/(/1/9/5/1/)/, /3/3/3/{/3/5/2/.
/[/5/4/] G/. E/. Murphy /, A new c onstruction of Y oung/'s semi/{normal r epr esentation of the symmetric
gr oups /, J/. Algebra/, /6/9 /(/1/9/8/1/)/, /2/8/7/{/2/9/7/.
/[/5/5/] /, On the r epr esentation the ory of the symmetric gr oups and asso ciate d He cke algebr as /,
J/. Algebra/, /1/5/2 /(/1/9/8/2/)/, /4/9/2/{/5/1/3/.
/[/5/6/] /, The r epr esentations of He cke algebr as of typ e A
n
/, J/. Algebra/, /1/7/3 /(/1/9/9/5/)/, /9/7/{/1/2/1/.
/[/5/7/] P/. N/. Nor ton /, /0/{He cke algebr as /, J/. Austral/. Math/. So c/./, /2/7 /(/1/9/7/9/)/, /3/3/7/{/3/5/7/.
/[/5/8/] B/. P arshall and J/. p/. W ang /, Quantum gener al line ar gr oups /, Memoirs A/.M/.S/./, /4/3/9 /(/1/9/9/1/)/.
/[/5/9/] A/. Ram /, A F r ob enius formula for the char acters of the He cke algebr a /, In v en t/. Math/./, /1/0/6
/(/1/9/9/1/)/, /4/6/1/{/4/8/8/.
/[/6/0/] K/./-D/. Schaper /, Char akterformeln f/ ur Weyl/{Mo duln und Sp e cht/{Mo duln in Primchar acter/-
istik /, Diplomarb e it/, Bonn/, /1/9/8/1/.
/[/6/1/] I/. Schur /,
/
Ub er eine Klasse von Matrizen/, die sich einer ge geb enen Matrix zuor dnen lassen /,
Gesammelte Abhandlungen I/, Springer/-V erlag /, Berlin/, /1/9/0/1/.
/[/6/2/] D/. W oodcock /, Str aightening c o determinants /, J/. Pure Appl/. Algebra/, /8/8 /(/1/9/9/3/)/, /3/1/7/{/3/2/0/.
Index
b eta n um b ers/, /5/2/, /5/4
blo c ks/, /1/5/, /6/1/, /6/2
braid relations/, /1
Bruhat/{Chev all ey order/, /2/0
dominance order/, /2/0
Cartan matrix/, /1/3
cell mo dule/, /1/0
cellular algebra/, /9
cellular basis/, /9
c haracter/, /5/, /8
comp osition /, /1/7
core/, /6/0
decomp osit ion matrix/, /1/3/, /3/4/, /4/3/, /5/9
diagram/, /1/7
distinguishe d coset represen tativ es/, /1/8
double/, /3/7
dominance order
Bruhat/{Chev alle y order/, /2/0
partitions/, /1/9
tableau/, /1/9/, /4/6
exc hange condition/, /2
Garnir tableau/, /2/1
generic degree/, /6
generic Iw ahori/{Hec k e algebra/, /5
Gram determinan t /, /4/6
ho ok/, /5/5
ho ok length/, /3/5/, /5/5
induced represen tatio n/, /1/8
in v olv ed in/, /2/3
Iw ahori/{Hec k e algebra/, /3
Jan tzen /ltration/, /5/7
Janzten /ltration/, /5/9
Jucys/{Murph y elemen ts/, /2/6/, /2/8/, /4/6
left cell mo dule/, /1/0
leg length/, /5/5
length/, /1
lexicograph ic ordering/, /2/1
link ed/, /1/5
Murph y basis/, /2/3/, /2/6/, /3/9/, /4/1
Nak a y ama conjecture/, /6/2
no de/, /1/7
partition/, /1/7
conjugate partition/, /5/2
core/, /6/0
diagram/, /1/7
parts/, /1/7
restricted/, /3/2/, /3/4
w eigh t/, /6/2
q /{Sc h ur algebra/, /3/6
reduced expression/, /1
residue/, /2/8/, /4/6
rim ho ok/, /5/6
ro w standard/, /1/7
Sc h ur functor/, /4/3/, /5/9
semistandar d basis/, /4/1/, /4/2
sign represen tation /, /1/, /5
Sp ec h t mo dule/, /2/5/, /3/4
dual Sp ec h t mo dule/, /2/5
Sp ec h t series/, /4/0
sp ecializati on/, /5
sp ecializati on homomorphis m/, /5
standard basis/, se e Murph y basis
sub expressio n/, /1/9
tableau/, /1/7
ro w semistandar d/, /3/6
restricted/, /3/2/, /3/4
ro w standard/, /1/7
semistandard /, /3/6
shap e/, /1/7/, /3/6
standard/, /1/7
trivial represen tat ion /, /5
un wrapping/, /5/6
w eigh t space/, /4/6
W eyl mo dule/, /4/2
wrapping/, /5/6
Y oung/'s seminormal form/, /3/0/, /3/4
/7/3
