---
doc_id: 52036
doc_title: "Torus Knots Extremizing the M öbius Energy"
section_id: sec-007-references
section_title: "References"
section_number: null
pages: 1-9
source_pdf: 52036.pdf
source_sha256: ab02866e1f7191b7
doc_brief: "Torus Knots Extremizing the M öbius Energy — 9 sections: Front matter; Introduction; M ¨obius Invariance"
---
Software Availability
This w ork w as accomplished while the authors w ere at the
Institute for Adv anced Study /, and w as partly supp orted b y an
NSF P ostdo ctoral F ello wship/.
Using the principle of symmetric criticality [Palais 1979], we
construct torus knots and links that extremize the M ¨obius-
invariant energy introduced by O’Hara [1991] and Freedman,
He and Wang [1993]. The critical energies are explicitly com-
putable using the calculus of residues, a result obtained in
collaboration with Gil Stengle.
Experiments with a discretized version of the M ¨obius energy—
applicable to the study of arbitrary knots and links—are also
described, and conﬁrm the results of the analytic calculations.
1. INTRODUCTION
Recen tly F reedman/, He and W ang /[F reedman et
al/./]/, follo wing w ork of O/'Hara /[/1/9/9/1/]/, in tro duced
an energy E /(/BnZr/) for a simple closed curv e /BnZr / R
/3
/.
The functional E is con tin uous on eac h isotop y
class of curv es/, and tends to in/
nit y as /BnZr nears
self/-in tersection/. Moreo v er/, E is /\prop er/" on the
set of all isotop y classes/, in the sense that there are
only /
nitely man y knot t yp es b elo w a giv en energy
lev el/.
A useful geometric prop ert y of E is M/ obius in/-
v ariance/: if / is a M/ obius transformation of R
/3
/[ /1
and / /(/BnZr/) / R
/3
/, then E /( / /(/BnZr/)/) /= E /(/BnZr/)/. This can
b e used to pro v e /[F reedman et al/./] that eac h prime
knot class has an energy/-minimizing represen tativ e
/(of di/
eren tiabilit y class C
/1 /; /1
/: see de/
nition in the
b eginning of Section /2/)/, and that the round circle
is the unique energy minimizer among all curv es/,
with E /= /4/. It is also a non trivial result of /[F reed/-
man et al/./] that/, at least for C
/1 /; /1
curv es/, the func/-
tional E is su/cien tly smo oth to ha v e a /\gradien t/"
dE /(see Section /3/)/. Th us it b ecomes an in teresting
problem to /
nd E /-critical curv es/, that is/, solutions
to dE /= /0/.
c
/
 A K P eters/, Ltd/.
/1/0/5/8/-/6/4/5/8///9/6 /$/0/./5/0 p er page
2 Experimental Mathematics, Vol. 2 (1993), No. 1
In this article w e construct the /
rst explicit ex/-
amples of knotted curv es that are critical for E /.
Our basic observ ation is that the M/ obius/-in v arian t
energy E extends naturally to simple closed curv es
/BnZr / R
m
/(Section /2/)/. In particular/, if /BnZr is a simple
closed curv e in S
/3
/ R
/4
and / /: S
/3
/! R
/3
/[ /1
is stereographic pro jection/, then E /( / /(/BnZr/)/) /= E /(/BnZr/)
pro vided / /(/BnZr/) / R
/3
/. Then w e use the principle of
symmetric criticalit y /(Section /3/) to sho w that for
eac h relativ ely prime pair of in tegers /( p/; q /) there is
a /( p/; q /)/-torus knot /BnZr
p/;q
/ S
/3
critical for E /. This
curv e /BnZr
p/;q
is a principal orbit of an isometric action
of S
/1
on S
/3
/. In the same w a y /, w e construct crit/-
ical orbital links with more than one comp onen t
/(Section /4/)/.
The energies E /(/BnZr
p/;q
/) can b e computed explic/-
itly in terms of rational trigonometric in tegrals/.
This mak es them ideal b enc hmarks to c hec k the
accuracy of computer exp erimen ts with v arious dis/-
cretized energies/. One suc h discrete mo del is men/-
tioned in Section /5/. W e ha v e implemen ted sev/-
eral programs using this mo del/, run exp erimen ts/,
and tabulated some of the results/, but clearly more
w ork needs to b e done/. In this regard/, w e men tion
that sev eral Japanese mathematicians and/, inde/-
p enden tly /, Bryson /[Bryson et al/. /1/9/9/3/] ha v e also
conducted computer exp erimen ts to seek non triv/-
ial extrema/. In particular/, Bryson rep orts /
nd/-
ing a trefoil/|that is/, a /(/2 /; /3/)/-torus knot/|with en/-
ergy appro ximately equal to /7/4/, whic h is close to
the critical v alue of /7/4 /: /4/1/2/0 /(see T able /1 in Sec/-
tion /5/)/.
It is w ell/-kno wn /(see /[Sc h ub ert /1/9/5/3/, p/. /2/5/0/]/,
for example/) that torus knots are prime/, and it is
tempting to conjecture that the stereographic im/-
ages / /(/BnZr
p/;q
/) are the energy minimizers guaran teed
to exist b y /[F reedman et al/./]/. Ho w ev er/, w e exp ect
this to b e false when b oth p and q are large/, for
the follo wing reason/: W e can view /BnZr
p/;q
as a p /- or
q /-strand braid lying on the surface of a torus/, and
if b oth p and q are at least three/, energy can b e
sa v ed when /\extra strands/" of /BnZr
p/;q
depart from the
surface of the torus and push in to the in teriors of
the complemen tary solid tori/.
The righ t conjecture/, whic h is supp orted b y our
most recen t exp erimen ts /(Section /6/)/, app ears to
b e this/: /BnZr
p/;q
is a stable lo cal minim um for E when
p /= /2 or q /= /2/, but is not a minimizer otherwise/.
The general E /-stabilit y question will b e explored
elsewhere /[Kusner and Sulliv an/]/.
2. M ¨OBIUS INVARIANCE
Supp ose /BnZr / R
m
is a simple closed curv e of class
C
/1 /; /1
/, that is/, one that admits a parametrization
/BnZr /: S
/1
/, /! R
m
whose /
rst deriv ativ e /BnZr
/0
is Lipsc hitz/.
/(W eak er di/
eren tiabilit y assumptions are p ossible
/[F reedman et al/./, x /1/]/, but w e /
nd C
/1 /; /1
b est suited
to our purp oses/./) Let D /( x/; y /) denote the distance
b et w een /BnZr/( x /) and /BnZr/( y /) along /BnZr/, that is/,
D /( x/; y /) /= min
/
Z
y
x
j /BnZr
/0
/( z /) j dz /;
Z
x
y
j /BnZr
/0
/( z /) j dz
/
/:
Deﬁnition and Proposition. Given /BnZr as ab ove/, the
M/ obius ener gy
E /(/BnZr/) /=
Z Z
S
/1
/ S
/1
/
/1
j /BnZr/( x /) /BnZr /BnZr/( y /) j
/2
/BnZr
/1
D
/2
/( x/; y /)
/
/ j /BnZr
/0
/( x /) j j /BnZr
/0
/( y /) j dx dy
is /
nite and indep endent of the p ar ametrization of
/BnZr /. Mor e over/, if / is a M/ obius tr ansformation of
R
m
/[ /1 /, then E /( / /(/BnZr/)/) /= E /(/BnZr/) pr ovide d / /(/BnZr/) /
R
m
/.
Proof. The argumen ts/, with only formal mo di/
ca/-
tions to mo v e from /3 to m dimensions/, are essen/-
tially those of /[F reedman et al/./, xx /1 and /2/]/. In
particular/, concerning the M/ obius in v ariance/, the
/
rst term in the in tegrand is p oin t wise in v arian t/,
whereas the second term in the in tegral is /\in trin/-
sic/"/, in the sense that/, for an y /" /> /0/, the asymp/-
totic expansion
Z Z
j x /BnZr y j/ /"
j /BnZr
/0
/( x /) j j /BnZr
/0
/( y /) j
D
/2
/( x/; y /)
dx dy /=
/4 /
/"
/BnZr /4 /+ O /( /" /)
is in v arian t under all C
/1 /; /1
di/
eomorphisms of R
m
/,
not only M/ obius transformations/. /
Kim and Kusner: T orus Knots Extremizing the M ¨obius Energy 3
Note that the /4 / /=/" term here precisely cancels a
corresp onding singular term from the /
rst in te/-
gral/. This is the /\regularization/" of E in tro duced
in /[O/'Hara /1/9/9/1/]/.
Stereographic pro jection extends to a M/ obius
transformation of R
m /+/1
/[ /1 /, so w e deduce/:
Corollary. If /BnZr / S
m
/ R
m /+/1
is a C
/1 /; /1
simple
close d curve and / /: S
m
/! R
m
/[ /1 is ster e o/-
gr aphic pr oje ction/, then E /( / /(/BnZr/)/) /= E /(/BnZr/) pr ovide d
/ /(/BnZr/) / R
m
/.
3. TORUS KNOTS AND SYMMETRIC CRITICALITY
F or eac h pair /( p/; q /) of in tegers/, there is an isometric
action /

p/;q
of S
/1
on the unit sphere S
/3
/ R
/4
/= C
/2
/,
de/
ned b y
/

p/;q
/( e
i/
/) /:
/
z
w
/
/7/!
/
e
ip/
z
e
iq /
w
/
/:
This action is e/
ectiv e when p and q are relativ ely
prime/, an assumption w e mak e from no w on/.
The case /( p/; q /) /= /(/1 /; /1/) is the familiar Hopf ac/-
tion /, whose orbits are great circles in S
/3
/. In gen/-
eral/, the /

p/;q
/-orbits of the p oin ts
/BnZr
/1
/0
/
or
/BnZr
/0
/1
/
are
p /- or q /-fold co v erings of the z /- or w /-axis circles S
/1
z
or S
/1
w
/, resp ectiv ely /, while the remaining /

p/;q
/-orbits
are em b eddings S
/1
/! S
/3
/. These principal orbits
lie on tori
T
r
/=
/
/( z /; w /) /: j z j /=
r
p
/1 /+ r
/2
/; j w j /=
/1
p
/1 /+ r
/2
/
/;
for r /> /0/, where they ha v e homology /( p/; q /)/|that
is/, they are /( p/; q /)/-torus knots/. Eac h torus is foli/-
ated b y a circle/'s w orth of congruen t orbits/; w e can
parametrize this family of orbits b y asso ciating to
e
it
/2 S
/1
the orbit that go es through the p oin t
/0
B
/@
e
imt
r
p
/1 /+ r
/2
e
int
/1
p
/1 /+ r
/2
/1
C
A
/; (3.1)
where m and n are /
xed in tegers suc h that
det
/
m n
p q
/
/= / /1 /:
W e can think of /( r /; t /) as p olar co ordinates for the
orbit space S
p/;q
of the action/, whic h is an orbifold
homeomorphic to S
/2
/.
W e denote b y /BnZr
p/;q
/( r /) an orbit of /

p/;q
lying in
the torus T
r
/. F or de/
niteness/, w e tak e the orbit
corresp onding to t /= /0/, so that /BnZr
p/;q
/( r /) is the knot
e
i/
/7/!
/0
B
/@
e
ip/
r
p
/1 /+ r
/2
e
iq /
/1
p
/1 /+ r
/2
/1
C
A
/: (3.2)
The M/ obius energy of /BnZr
p/;q
/( r /)/, whic h w e denote
b y E /( r /)/, is a smo oth function of r /(see Figure /1/)/.
It turns out that w e can compute E /( r /) explicitly
using residue calculus /(see page /4/)/; ho w ev er/, the
results in this section do not dep end on that com/-
putation/.
Lemma. The knot /BnZr
p/;q
/( r /) is critic al for the M/ obius
ener gy E if and only if
/@
/@ r
E /( r /) /= /0 /:
Proof. The /\only if /" direction is clear/. The /\if /"
direction is a consequence of the principle of sym/-
metric critic ality /, whic h states roughly that/, for a
functional that is in v arian t under some group G of
symmetries/, the criticalit y of a G /-in v arian t func/-
tion need only b e c hec k ed as if the functional w ere
restricted to that part of its domain consisting of
all G /-in v arian t functions/. See /[P alais /1/9/7/9/]/, for ex/-
ample/, for a general discussion/.
More precisely /, consider a C
/1 /; /1
map V /: S
/1
/!
R
/4
/, though t of as a v ector /
eld along the knot
/BnZr /= /BnZr
p/;q
/( r /)/, and a v ariation /BnZr
/"
/= /BnZr /+ /"V of /BnZr/.
According to /[F reedman et al/./, Lemma /6/./1/]/, there
is a unique linear functional dE suc h that
dE /( V /) /=
d
d/"
E /(/BnZr
/"
/) j
/" /=/0
/;
for an y V as ab o v e/. /(More formally /, the Banac h
space of C
/1 /; /1
v ector /
elds along /BnZr is the tangen t
space to the Banac h manifold of C
/1 /; /1
curv es/, and
dE is the gradien t one/-form of E at /BnZr/. Sev eral
explicit form ulas for dE are giv en in /[F reedman et
4 Experimental Mathematics, Vol. 2 (1993), No. 1
Computing the M ¨obius Energy of Torus Knots by Residue Calculus
Rob Kusner and Gil Stengle
T o compute the M/ obius energy E /( r /) of the orbital torus knot /BnZr
p/;q
/( r /) of /(/3/./2/)/, w e /
rst rescale so the knot has
the parametrization /( r e
ipx
/; e
iq x
/)/, and then use the de/
nition of E /:
E /( r /) /=
Z
/2 /
/0
dy
Z
y /+ /
y /BnZr /
dx
/
r
/2
p
/2
/+ q
/2
r
/2
j e
ipx
/BnZr e
ipy
j
/2
/+ j e
iq x
/BnZr e
iq y
j
/2
/BnZr
/1
/( x /BnZr y /)
/2
/
/= /2 /
Z
/
/BnZr /
ds
/
r
/2
p
/2
/+ q
/2
r
/2
j e
ips
/BnZr /1 j
/2
/+ j e
iq s
/BnZr /1 j
/2
/BnZr
/1
s
/2
/
/;
where w e ha v e made the substitution s /= x /BnZr y /. In eac h of the cases /( p/; q /) /= /(/1 /; /0/)/, /(/0 /; /1/) or /(/1 /; /1/)/, the orbit
/BnZr
p/;q
/( r /) is a round circle/, and w e ha v e/, as already observ ed in /[F reedman et al/./]/,
E /( S
/1
/) /= /2 /
Z
/
/BnZr /
ds
/
/1
j e
is
/BnZr /1 j
/2
/BnZr
/1
s
/2
/
/= /2 /
Z
/ /= /2
/0
d/
/
/1
sin
/2
/
/BnZr
/1
/
/2
/
/= /2 /
/2
/
/= /4 /;
with / /=
/1
/2
s /. Subtracting the /
rst of these equalities from the second equalit y ab o v e for E /( r /)/, w e get
E /( r /) /BnZr E /( S
/1
/) /= /2 /
Z
/
/BnZr /
ds
/
r
/2
p
/2
/+ q
/2
r
/2
j e
ips
/BnZr /1 j
/2
/+ j e
iq s
/BnZr /1 j
/2
/BnZr
/1
j e
is
/BnZr /1 j
/2
/
/:
Using the iden tit y j e
ix
/BnZr /1 j
/2
/= /BnZr e
/BnZr ix
/( e
ix
/BnZr /1/)
/2
/, v alid for x real/, w e see that the in tegrand can b e extended to
a meromorphic di/
eren tial on C dep ending only on e
is
/; the substitution z /= e
is
/, ds /= /BnZr iz
/BnZr /1
dz then expresses
E /( r /) as a con tour in tegral along the unit circle/, to whic h w e can apply Cauc h y/'s residue form ula/:
E /( r /) /= /4 /+ /2 /
Z
/
/BnZr /
ds
/
/BnZr /( r
/2
p
/2
/+ q
/2
/)
r
/2
e
/BnZr ips
/( e
ips
/BnZr /1/)
/2
/+ e
/BnZr iq s
/( e
iq s
/BnZr /1/)
/2
/BnZr
/BnZr /1
e
/BnZr is
/( e
is
/BnZr /1/)
/2
/
/= /4 /+ /2 /
Z
j z j /=/1
dz
/
i /( r
/2
p
/2
/+ q
/2
/)
r
/2
z
/1 /BnZr p
/( z
p
/BnZr /1/)
/2
/+ z
/1 /BnZr q
/( z
q
/BnZr /1/)
/2
/BnZr
i
/( z /BnZr /1/)
/2
/
/= /4 /+ /4 /
/2
X
j z j /< /1
Res
/BnZr /( r
/2
p
/2
/+ q
/2
/)
r
/2
z
/1 /BnZr p
/( z
p
/BnZr /1/)
/2
/+ z
/1 /BnZr q
/( z
q
/BnZr /1/)
/2
/:
The last equalit y dep ends on the fact that the order/-t w o singularit y at z /= /1 of the /
rst term in the in tegral is
precisely cancelled b y the second term/. One can also c hec k that the set of p oles is in v arian t under conjugation
and in v ersion in S
/1
/. Moreo v er/, the residues o ccur in conjugate pairs and ha v e p ositiv e real part/, so that eac h
p ole inside the unit disk con tributes to E /.
A similar calculation sho ws that the energy cross/-term corresp onding to t w o /( p/; q /)/-torus knots/, with /\p olar
co ordinates/" /( r /; t /) and /( r /; t
/0
/) in the notation of Section /3/, is
/4 /
/2
Res
/BnZr /( r
/2
p
/2
/+ q
/2
/)
r
/2
z
/1 /BnZr p
e
/BnZr /2 / it
/( z
p
/BnZr e
/2 / it
/)
/2
/+ z
/1 /BnZr q
e
/BnZr /2 / it
/0
/( z
q
/BnZr e
/2 / it
/0
/)
/2
/: /( / /)
Th us/, the total energy of the torus link /BnZr
k p/;k q
/( r /)/, for p and q relativ ely prime /(see Section /4 for notation/)/, is
E /( r /) /= k
/
/4 /+ /4 /
/2
k /BnZr /1
X
j /=/0
X
j z j /< /1
Res
/BnZr /( r
/2
p
/2
/+ q
/2
/)
r
/2
z
/1 /BnZr p
e
/BnZr /2 / ij m
/( z
p
/BnZr e
/2 / ij m
/)
/2
/+ z
/1 /BnZr q
e
/BnZr /2 / ij n
/( z
q
/BnZr e
/BnZr /2 / ij n
/)
/2
/
/;
where m and n are /
xed in tegers suc h that det
/BnZr
m
p
n
q
/
/= / /1/.
Kim and Kusner: T orus Knots Extremizing the M ¨obius Energy 5
al/./, x /6/]/, but its linearit y is the only prop ert y w e
need here/./)
Supp ose that /BnZr is not critical/, so there exists a
/
eld V suc h that dE /( V /) /6/= /0/. Since /BnZr is an orbit of
the S
/1
/-action /
 /= /

p/;q
/, w e can a v erage the push/-
forw ard /( /
 /( e
i/
/)/)
/
V o v er S
/1
to obtain an /
 /-in v arian t
v ector /
eld
/~
V for whic h dE /(
/~
V /) /6/= /0 as w ell/.
No w
/~
V induces a v ariation through /
 /-orbits/, so
w e can view
/~
V as tangen t to the orbit space S /=
S
p/;q
at /BnZr/. But
dE j
S
/=
/@ E
/@ r
dr /+
/@ E
/@ t
dt /=
/@ E
/@ r
dr /;
b ecause knots with same t ha v e the same energy /.
Th us dE j
S
/(
/~
V /) /= dE /(
/~
V /) /6/= /0 implies /@ E /=/@ r /6/= /0/,
as required/. /
W e come next to our main result/.
Theorem 1. F or e ach r elatively prime p air of inte/-
gers p and q gr e ater than /1 /, ther e is a /( p/; q /) /-torus
knot /BnZr
p/;q
/ S
/3
that is critic al for the M/ obius en/-
er gy E /. The knot /BnZr
p/;q
is a princip al orbit of the
S
/1
/-action /

p/;q
de/
ne d ab ove/.
Proof. As already men tioned/, E /( r /) is a smo oth
function of r /. Because /BnZr
p/;q
/( r /) con v erges to either
a p /- or q /-fold co v ering of a round circle as r ap/-
proac hes /1 or /0/, and b ecause p/; q / /2/, w e ha v e
lim
r /# /0
E /( r /) /= lim
r /"/1
E /( r /) /= /+ /1 /:
Th us there is a /
nite v alue r
p/;q
/> /0 minimizing
E /( r /)/. By the previous lemma/, the principal orbit
/BnZr
p/;q
/= /BnZr
p/;q
/( r
p/;q
/) is critical for E /. /
In fact/, in all the examples w e examined/, there
app ears to b e exactly one minim um /(see Figure /1/)/.
4. TORUS LINKS
In /[F reedman et al/./] the M/ obius energy of a k /-
comp onen t link /(/BnZr
/1
/; /: /: /: /; /BnZr
k
/) is de/
ned as a natural
extension of the M/ obius energy of a knot/:
E /(/BnZr
/1
/; /: /: /: /; /BnZr
k
/) /=
X
/1 / i/;j / k
E /(/BnZr
i
/; /BnZr
j
/) /;
/0 /: /0/3 /0 /: /1 /0 /: /3 /1 /3 /1/0 /3/0 r
/3 /; /4
/5/0/0
/1/0/0/0
/1/5/0/0
/2/0/0/0
FIGURE 1. Graph of E /( r /) v ersus r /, for /(/3 /; /4/)/-torus
knots/, from the form ula on page /4/. Other v alues
of p and q yield a v ery similar shap e/.
where E /(/BnZr
i
/; /BnZr
i
/) /= E /(/BnZr
i
/) is as b efore/, and the cross/-
terms /( i /6/= j /) are
E /(/BnZr
i
/; /BnZr
j
/) /=
Z Z
S
/1
/ S
/1
j /BnZr
/0
i
/( x /) j j /BnZr
/0
j
/( y /) j
j /BnZr
i
/( x /) /BnZr /BnZr
j
/( y /) j
/2
dx dy /:
If w e consider links comp osed of orbits of the S
/1
/-
action /

p/;q
/, the principle of symmetric criticalit y
applies/: a k /-comp onen t orbital link is critical for
E among all links if and only if it corresp onds to an
E /-critical con/
guration of k distinct regular p oin ts
in the orbit space S /= S
p/;q
/, that is/, to a critical
p oin t of E restricted to S
k
n D /, where D is the big
diagonal of S
k
union the singular orbits/. But E is
a p ositiv e prop er function on S
k
n D /, so it has a
minim um/.
In fact/, it is easy to /
nd some critical links ex/-
plicitly /. If k /> /1/, denote b y /BnZr
k p/;k q
/( r /) the link con/-
sisting of k copies of the knot /BnZr
p/;q
/( r /)/, arranged
symmetrically around the torus T
r
/. In other w ords/,
/BnZr
k p/;k q
/( r /) is the union of the /

p/;q
/-orbits with param/-
eters /( r /; t /)/, with t /= /0 /; /2 / /=k /; /: /: /: /; /2 / /( k /BnZr /1/) /=k /. /(See
the b eginning of Section /3/, and esp ecially /(/3/./1/)/,
for the /( r /; t /) parametrization of the orbit space/./)
W e call /BnZr
k p/;k q
/( r /) a /( k p/; k q /) /-torus link /. Applying
the principle of symmetric criticalit y with resp ect
to the ob vious action of S
/1
/ C
k
/, where C
k
is the
cyclic group of order k /, w e conclude/:
6 Experimental Mathematics, Vol. 2 (1993), No. 1
Theorem 2. F or e ach r elatively prime p air of inte/-
gers p/; q / /1 and e ach k /> /1 /, ther e is a /( k p/; k q /) /-
torus link /BnZr
k p/;k q
which minimizes E among k /-c om/-
p onent links invariant under S
/1
/ C
k
/, and which is
ther efor e critic al for E /. In p articular/, ther e ar e in/-
/
nitely many E /-critic al links with any numb er of
c omp onents/.
A /( k /; k /)/-torus link is a particular case of a Hopf
link /, that is/, a link whose comp onen t curv es are
orbits of the Hopf action /

/1 /; /1
/. A Hopf link can
b e regarded as a collection of p oin ts in the orbit
space S
/1 /; /1
/= S
/2
/; the case of /BnZr
k /;k
/( r /) corresp onds
to k equidistan t p oin ts along a parallel of latitude
/(circle of constan t r /)/. All k /-comp onen t Hopf links
are isotopic/.
A direct calculation/, or an application of /( / /) on
page /4 /(with r /= /1 and /
 /= t /BnZr t
/0
/)/, sho ws that
the energy cross/-term arising from an ordered pair
of comp onen ts of a Hopf link equals /2 /
/2
csc /(
/1
/2
/
 /)/,
where /
 is the angular distance b et w een the cor/-
resp onding p oin ts in S
/2
/. In particular/, the total
energy of a k /-comp onen t Hopf link is/, up to a con/-
stan t/, simply the /\Coulom b energy/" for k p oin t
c harges in R
/3
constrained to lie on S
/2
/. /(This ob/-
serv ation w as made join tly with John Sulliv an/./)
Since the p oin ts of S
/2
corresp onding to /BnZr
k /;k
/( r /)
are furthest apart when they are on the equator/,
that is/, when r /= /1/, Theorem /2 has the follo wing
consequence/:
Corollary. F or any k /, the Hopf link /BnZr
k /;k
/(/1/) is E /-
critic al/.
In fact/, /BnZr
/2 /; /2
/(/1/)/, with energy /8 /+ /4 /
/2
/, is a min/-
imizer among all non trivial t w o/-comp onen t links
at least one comp onen t of whic h is a round cir/-
cle/; see /[F reedman et al/./, x /7/]/. One can also sho w
that /BnZr
/3 /; /3
/(/1/)/, with energy /1/2 /+ /8
p
/3 /
/2
/, is energy/-
minimizing among Hopf links with three comp o/-
nen ts/. In con trast/, /BnZr
/4 /; /4
/(/1/)/, with energy
/1/6 /+ /8/(/1 /+ /2
p
/2/) /
/2
/ /3/1/8 /: /2/8/0/5 /;
is not minimizing among Hopf links with four com/-
p onen ts/; the minimizing four/-comp onen t Hopf link
corresp onds to a tetrahedral/, rather than an equa/-
torial/, con/
guration of p oin ts on S
/2
/, and its energy
is /1/6 /+ /1/2
p
/6 /
/2
/ /3/0/6 /: /1/0/5/9 /(see Figure /2/)/. This
FIGURE 2. Tw o Hopf links critical for the energy functional E /: on the left/, the torus link /BnZr
/4 /; /4
/(/1/)/, whose
comp onen ts corresp ond /(in the quotien t space S
/2
of the Hopf /
bration/) to four p oin ts equally spaced along a
great circle/; on the righ t/, a link of less energy /, whose comp onen ts corresp ond to the v ertices of a tetrahedron/.
See the corollary ab o v e and the subsequen t paragraph/.
Kim and Kusner: T orus Knots Extremizing the M ¨obius Energy 7
phenomenon illustrates the conjectured b eha vior/,
discussed in Section /1/, of an E /-minimizing /( p/; q /)/-
torus knot for p and q large/. F urther results on
Hopf links are giv en in /[Kusner and Sulliv an/]/.
5. DISCRETIZATION AND COMPUTER EXPERIMENTS
Giv en a C
/1 /; /1
knot /BnZr /: S
/1
/= R /= /2 / Z /! R
m
/, and
a su/cien tly large in teger n /, the p olygon /
 with
v ertices /
 /( h /) /= /BnZr/(/2 / h/=n /)/, for /1 / h / n /, is a knot
isotopic to /BnZr/, whic h w e call a p olygonal appr oxima/-
tion to /BnZr/. One p ossible w a y to appro ximate E /(/BnZr/)
discretely w ould b e simply to use E /( /
 /)/, but this en/-
ergy unfortunately is in/
nite/! It can b e regularized/,
b y deleting the con tributions of adjacen t edges/, to
an energy E
/
/( /
 /) that has the adv an tage of an in/
/-
nite barrier to c hanging isotop y t yp e/, but the dis/-
adv an tage of b eing di/cult to compute/. Another
discrete energy e /( /
 /)/, de/
ned b elo w/, is m uc h easier
to compute/. It can b e sho wn that b oth E
/
/( /
 /) and
e /( /
 /) con v erge to E /(/BnZr/) as /
 approac hes /BnZr for n v ery
large/.
Deﬁnition. The discr ete ener gy of a p olygon with
v ertices /
 /: Z /=n Z /! R
m
is
e /( /
 /) /=
X X
/1 / i /6/= j / n
/
/1
j /
 /( i /) /BnZr /
 /( j /) j
/2
/BnZr
/1
d
/2
/( i/; j /)
/
/ j /
/0
/( i /) j j /
/0
/( j /) j /;
where
j /
/0
/( h /) j /=
/1
/2
/( j /
 /( h /BnZr /1/) /BnZr /
 /( h /) j /+ j /
 /( h /) /BnZr /
 /( h /+ /1/) j /)
and d /( i/; j /) is the distance b et w een /
 /( i /) and /
 /( j /)
along the p olygon/, that is/, the lesser of
P
i / h/<j
j /
 /( h /) /BnZr /
 /( h /+ /1/) j and
P
j / h/<i
j /
 /( h /) /BnZr /
 /( h /+ /1/) j /:
If /
 /= /
p/;q
is a p olygonal appro ximation to the
orbit /BnZr
p/;q
/ S
/3
/, w e can reduce the double sum
ab o v e /(b y setting h /= i /BnZr j /) to
e /( /
 /) /= n j /
/0
/(/1/) j
/2
X
/1 /<h / n
/
/1
j /
 /(/1/) /BnZr /
 /( h /) j
/2
/BnZr
/1
d
/2
/(/1 /; h /)
/
/:
Using this form ula w e wrote a simple F ortran
searc h routine/, torusknotenergy/.f /, to pro duce
appro ximate v alues for the M/ obius energies of crit/-
ical /( p/; q /)/-torus knots/. The results are v ery close to
those obtained from the analytic form ula on page /4/,
whic h w as implemen ted in a Mathematica program
tke/.m /[W olfram /1/9/9/1/]/: see T able /1/.
/( p/; q /) n / r
p/;q
energy
/(/1 /; /1/) /3/6/0 /1/./0 /| /3/./9/6/0/8
/7/2/0 /./5 /| /3/./9/8/0/4
/1/4/4/0 /./2/5 /| /3/./9/9/0/2
/2/8/8/0 /./1/2 /| /3/./9/9/5/1
/5/7/6/0 /./0/6 /| /3/./9/9/7/5
/1/1/5/2/0 /./0/3 /| /3/./9/9/8/7
extrap olation /| /3/./9/9/9/9
analytic v alue /| /4/./0/0/0/0/0
/(/2 /; /3/) /1/4/4/0 /./6/8 /1/./8/5 /7/4/./3/5/3
/2/8/8/0 /./3/4 /1/./8/5 /7/4/./3/8/3
/5/7/6/0 /./1/7 /1/./8/5/7 /7/4/./3/9/7
/1/1/5/2/0 /./0/9 /1/./8/5/7 /7/4/./4/0/5
extrap olation /1/./8/5/7 /7/4/./4/1/2
analytic v alues /1/./8/5/7/2/7/5 /7/4/./4/1/2/0/4
/(/2 /; /8/) /1/4/4/0 /./7/7 /5/./6/9 /2/1/5/./5/1/8
/2/8/8/0 /./3/8 /5/./6/9 /2/1/5/./6/4/6
/5/7/6/0 /./1/9 /5/./6/9/2 /2/1/5/./7/1/0
/1/1/5/2/0 /./1/0 /5/./6/9/3 /2/1/5/./7/4/2
extrap olation /5/./6/9/4 /2/1/5/./7/7/4
analytic v alues /5/./6/9/4/9/4/2 /2/1/5/./7/7/4/6/3
/(/3 /; /4/) /1/4/4/0 /./8/5 /1/./4/8 /2/0/4/./0/9/4
/2/8/8/0 /./4/2 /1/./4/8 /2/0/4/./1/5/6
/5/7/6/0 /./2/1 /1/./4/8/6 /2/0/4/./1/8/6
/1/1/5/2/0 /./1/1 /1/./4/8/6 /2/0/4/./2/0/1
extrap olation /1/./4/8/6 /2/0/4/./2/1/7
analytic v alues /1/./4/8/6/9/0/6 /2/0/4/./2/1/6/7/0
TABLE 1. Critical radii and energies obtained from
the discrete programs torusknotenergy/.f and
toruslinkenergy/.f /. Here n is the n um b er of seg/-
men ts in the discretization/, and / is the maxi/-
m um angle /(in degrees/) b et w een segmen ts/. The
last t w o lines in eac h blo c k sho w ho w extrap ola/-
tion of the program output as n /! /1 giv es results
v ery close to those predicted b y the analytic for/-
m ula on page /4/, whic h w ere computed with the
Mathematica programs tke/.m and tle/.m /.
8 Experimental Mathematics, Vol. 2 (1993), No. 1
These t w o programs are publicly a v ailable/, to/-
gether with their link coun terparts/, called tle/.m
and toruslinkenergy/.f /. F or details/, see /\Soft/-
w are Av ailabilit y/" at the end of the article/.
As a further c hec k/, w e compared the computed
v alues of E and r
p/;q
under an in terc hange of p and
q /. As exp ected/, E remains the same/, while r
p/;q
is
replaced b y its recipro cal/, to within the c hosen ac/-
curacy /. /(In the case of tke/.m /, the default accuracy
of the minim um searc h is six signi/
can t digits for r /,
but an y desired accuracy can b e sp eci/
ed/, sub ject
only to memory constrain ts/./)
6. FURTHER EXPERIMENTS
V ery recen tly /, the second author and John Sulliv an
computed the gradien t de of the discretized energy
e /( /
 /)/, and Ken Brakk e w as kind enough to incor/-
p orate it in to V ersion /1/./8/9 of his Surface Ev olv er
program /[Brakk e /1/9/9/2/]/. Because e and de are eac h
quadratic in n /, con v ergence of the negativ e gradi/-
en t /
o w to a critical knot or link is considerably
slo w er than in the program torusknotenergy/.f /,
whic h searc hes only among orbits/; the practical
size of n in the Ev olv er is limited accordingly /. Nev/-
ertheless/, w e w ere able to test the stabilit y of /BnZr
/2 /;q
for q small/. Moreo v er/, use of the Ev olv er allo ws
us to searc h among all knots/, not only those that
are in v arian t under the S
/1
action/. W e th us found
a non/-orbital /(/3 /; /4/)/-torus knot with energy appro x/-
imately /2/0/1/, less than the energy of /BnZr
/3 /; /4
/, whic h is
/2/0/4 /: /2/1/6/7/; see also the end of Section /1/.
W e hop e to rep ort further on this in future join t
w ork with Brakk e/, Sulliv an/, and a group of stu/-
den ts at the Fiv e Colleges Geometry Institute/.
ACKNOWLEDGEMENTS
W e thank the Sc ho ol of Mathematics at the Insti/-
tute for Adv anced Study /, the Cen ter for Geome/-
try /, Analysis/, Numerics and Graphics /(G/.A/.N/.G/./)
of the Univ ersit y of Massac h usetts at Amherst/, and
the Geometry Cen ter of the Univ ersit y of Min/-
nesota/, for the use of their computer facilities/; and
Ken Brakk e/, Bruce Kleiner and John Sulliv an/, for
their helpful commen ts/. Thanks also to Charlie
Gunn and P eter Norman for their in terest in this
pro ject/. W e are grateful to Dic k P alais and the
referee for suggesting a n um b er of impro v emen ts
to the text/, and to Mik e Da vis for p oin ting out the
reference /[Sc h ub ert /1/9/5/3/]/.
Finally /, w e w ould lik e to express our appreci/-
ation for Silvio Levy/'s sup erlativ e editing/, whic h
clari/
ed the exp osition/, and for his con tribution of
the program tle/.m /, whic h completed the circle of
ideas/.
REFERENCES
/[Brakk e /1/9/9/2/] K/. A/. Brakk e/, /\The Surface Ev olv er/"/,
Exp erimental Math/. /1 /(/1/9/9/2/)/, /1/4/1/{/1/6/5/.
/[Bryson et al/. /1/9/9/3/] S/. Bryson/, M/. H/. F reedman/, Z/.
X/. He and Z/. W ang/, /\M/ obius In v ariance of Knot
Energy/"/, Bul l/. A mer/. Math/. So c/. /2/8 /(/1/9/9/3/)/, /9/9/{/1/0/3/.
/[F reedman et al/./] M/. H/. F reedman/, Z/. X/. He and Z/.
W ang/, /\M/ obius energy of knots and unknots/"/, to
app ear in A nnals of Math/. Also a v ailable as /\On the
energy of knots and unknots/"/, Researc h Rep ort GCG
/4/0/, The Geometry Cen ter/, Univ ersit y of Minnesota/.
/[Kusner and Sulliv an/] R/. Kusner and J/. Sulliv an/,
/\A M/ obius in v arian t/, nonlo cal energy for em b edded
submanifolds/"/, in preparation/.
/[O/'Hara /1/9/9/1/] J/. O/'Hara/, /\Energy of a knot/"/, T op olo gy
/3/0 /(/1/9/9/1/)/, /2/4/1/{/2/4/7/.
/[P alais /1/9/7/9/] R/. P alais/, /\The principle of symmetric
criticalit y/"/, Comm/. Math/. Physics /6/9 /(/1/9/7/9/)/, /1/9/{/3/0/.
/[Sc h ub ert /1/9/5/3/] H/. Sc h ub ert/, /\Knoten und V ollringe/"/,
A cta Math/. /9/0 /(/1/9/5/3/)/, /1/3/1/{/2/8/6/.
/[W olfram /1/9/9/1/] S/. W olfram/, Mathematic a/: A Sys/-
tem for Doing Mathematics by Computer /, /2nd ed/./,
Addison/-W esley /, Reading/, MA/, /1/9/9/1/.
SOFTWARE AVAILABILITY
The Mathematica programs tke/.m and tle/.m /, as w ell as
the F ortran programs torusknotenergy/.f and torus /-
linkenergy/.f /, can b e found in the directory pub//knot
on the serv er polyphemus/.gang/.umass/.edu /.
Kim and Kusner: T orus Knots Extremizing the M ¨obius Energy 9
Denise Kim/, Departmen t of Ph ysics/, Univ ersit y of Massac h usetts/, Amherst/, MA /0/1/0/0/3 /(kim/@gang/.umass/.edu/)
Rob Kusner/, Departmen t of Mathematics/, Univ ersit y of Massac h usetts/, Amherst/, MA /0/1/0/0/3
/(kusner/@math/.umass/.edu/)
Gil Stengle/, Departmen t of Mathematics/, Lehigh Univ ersit y /, Bethlehem/, P A /1/8/0/1/5 /(gas/0/@lehigh/.edu/)
Receiv ed F ebruary /6/, /1/9/9/3/; accepted in revised form April /2/7
