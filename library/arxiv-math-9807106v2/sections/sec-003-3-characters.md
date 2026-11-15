---
doc_id: arxiv-math-9807106v2
doc_title: "An Extension of the Character Ring of sl(3) and Its Quantisation P. Furlan∗,†"
section_id: sec-003-3-characters
section_title: "Characters."
section_number: 3
pages: 10-17
source_pdf: 9807106v2.pdf
source_sha256: e3cd089e3df5d71f
toc_source: inferred
doc_brief: "An Extension of the Character Ring of sl(3) and Its Quantisation P. Furlan∗,† — We construct a commutative ring with identity which extends the ring of characters of ﬁnite dimensional representations"
---
Let us start by recalling the supports and characters of ordinary Verma and ﬁnite
dimensional modules of g. The latter characters are elements of the group ring Z[tP ] of
the group of translations by the weight lattice. Keeping with tradition, the translations
t−λ from the previous section will be written as formal exponentials e−κλ ; κ = −1 recovers
the standard notation, see, e.g., [3] for standard deﬁnitions. The character of the Verma
module Vλ of highest weight λ is given by
ch(Vλ) =
X
µ∈λ−Q+
K
λ
µe−κµ = e−κλ X
β∈Q+
Kβeκβ = e−κλ
Y
α∈∆+
(1 −eκα)−1 = e−κ(λ+ρ) dκ ,
(3.1)
where the multiplicity K
λ
µ of an weight µ is expressed via the Kostant partition function
K
λ
µ := Kλ−µ ∈Z≥0 , while dκ is a W invariant (up to a sign) quantity w(dκ) = det(w) dκ
for w(eκβ) := eκw(β). The support of a module is the set of weights µ of nonzero multi-
plicity K
λ
µ, thus suppVλ = λ −Q+.
The irreducible ﬁnite dimensional modules can be resolved in terms of Verma modules,
i.e., each Verma module Vw·λ, with w ∈W and λ ∈P+, contains submodules of weight
Vw′·λ for all w′ > w in the Bruhat ordering of W (in a convention in which 1 is the smallest
element) and grading W by the reduced length of words the Verma module inclusions
organize in a BGG (Bernstein–Gelfand–Gelfand) resolution. For the characters χλ , λ ∈P+
of irreducible ﬁnite dimensional modules the BGG resolution gives immediately the Weyl
character formula
χλ =
X
w∈W
det(w) ch(Vw·λ) = dκ
X
w∈W
det(w) e−κw(λ+ρ) =
X
µ∈P
mλ
µ e−κµ ,
mλ
µ =
X
w∈W
det(w) Kw·λ−µ ,
(3.2)
and from χ1 = 1 the factor dκ is expressed as 1/dκ = P
w∈W det(w) e−κw(ρ). The support
(weight diagram) is Γλ = {µ ∈P | mλ
µ̸ = 0}. From (3.2) it follows that
w(χλ) = χλ ,
mλ
w(µ) = mλ
µ ,
(3.3)
and, extending the ﬁrst line of (3.2) to λ ∈P,
χw·λ = det(w) χλ .
(3.4)
10
The map ι introduced in (2.6) establishes a correspondence between (highest weights of)
Verma modules of the aﬃne algebra g and of the horizontal subalgebra g, with identical
reducibility structure. Now we shall introduce another class of ‘Verma modules’ Vy (of
yet unknown ﬁnite dimensional algebra) described through its supports, i.e., weights and
their multiplicities. The supports are parametrised by elements of aW ⊂˜W (for a ﬁxed
a ∈A) and mapped by ι into subsets of supports of g Verma modules. Motivated by
the intertwining property (2.10) we shall call such a module reducible if its ι image is
a reducible Verma module. In particular the maximally reducible ‘Verma modules’ have
highest weights Λ = y·kΛ0 , y ∈˜
W(+) , whence the name ‘dominant chamber’ for the latter
subset of ˜W. Furthermore in full analogy with the representation theory of g we shall
introduce ‘ﬁnite dimensional modules’ obtained factorising maximal ‘Verma submodules’
of reducible ‘Verma modules’ by an analog of the BGG resolution in which the role of W is
replaced by the action of the KW group, equivalent according to (2.3) to the right action
of W on ˜W. We have already explained on the example of g = sl(3) this construction in
[9] on the level of multiplicities of weights, here we add a realisation of the characters of
these ‘Verma- and ﬁnite dimensional modules’. It recovers the prescribed multiplicities but
furthermore allows to consider a tensor product of ‘ﬁnite dimensional modules’ realised by
a multiplication of their characters. The result is a new commutative ring which extends
the ring of g characters. It will be used in sections 6,7 as a basis for the construction of
quantised ‘q’-characters which realise the fusion rules of the admissible representations at
rational level.
We can describe the analogs of the multiplicities in (3.1) via the map ι, so what remains
to be done is to generalise the formal exponentials entering (3.1). The naive extension of
the map ι to the characters, thus leading to ordinary formal exponentials with arguments
involving the weights ι(y) (or the horizontal projections ¯Λ = h(y) ∈¯h∗) is possible but is
not consistent (except in the case g = sl(2)) since in general a sum of such weights goes
beyond the image of ι. (This is in agreement with the fact that there is no nontrivial
subset of the n-ality zero representations of g closed under tensor products). So our main
idea is, instead of exponentials (elements of the group algebra of the group of translations
tP ) assigned to weights, to consider the elements w e−κλ = y ∈˜W , i.e., the generating
elements of the group algebra of the group ˜W (the extension of tP over W). (We shall
use the same notation for both interpretations denoting as before sometimes the aﬃne
11
translations by formal exponentials.)1
Unlike the formal exponentials these generating
elements do not commute any more (rather satisfy the multiplication rules of ˜W in (2.2),
but nevertheless the ‘ﬁnite dimensional module’ characters we obtain, do commute and
multiply according to the rules conjectured in our previous paper.
Now we introduce the supports, Vu and Gu, and characters, ch(Vu) and χu, of,
respectively, ‘Verma’ and ‘ﬁnite dimensional modules’. The supports are certain inﬁnite
or ﬁnite subsets of the extended aﬃne Weyl group ˜W while the characters are certain
(formal) series or ﬁnite sums with integer coeﬃcients of elements of ˜W.
Let Λ = y · kΛ0 , y ∈aW , a ∈A . We deﬁne
Vy := {z ∈aW| ι(z) ∈ι(y) −Q+} = {xy | x ∈W , ι(x) ∈−y(Q+)} .
(3.5)
Alternatively, using that any ν ∈Q+ can be represented uniquely as ν = nβ + λ , with
some β ∈Q+ and λ ∈Q+/nQ+ = {Pn−1
i=1 kiαi | 0 ≤ki ≤n −1}, we can bring Vy into the
form
Vy = T y y tQ+ = {tuy(β) uy | u ∈T y , β ∈Q+} .
(3.6)
Here the ﬁnite subsets T y ⊂W, which project horizontally to W , are subject to the
condition
T y = {u ∈W | −¯y−1(ι(u)) ∈Q+/nQ+} .
(3.7)
E.g., if an element u ∈T y projects to a reﬂection wα ∈W , α ∈∆+ then it equals u = wα ,
or u = wα t−α = wδ−α if y−1(α) ∈∆+ , or y−1(−α) ∈∆+ , respectively.
Thus the support Vy in (3.5) naturally generalises the support of a g Verma module,
being deﬁned as a collection of |W| “positive” (for a choice of a set of simple roots)
root lattice cones tu y(Q+) applied to u y ∈T y y . The two descriptions of Vy reﬂected in
(3.6) and in (3.5) – as a collection of supports of ordinary g modules of highest weights
h(u y) = uy · kΛ0, or as the support of g module of highest weight ι(y) with some ‘excluded’
points, will be both useful in what follows. Next we deﬁne the multiplicity of an weight z
through its ι image,
Ky
z := Kι(y)−ι(z)
or Ky
xy = K−y−1(ι(x)) ,
(3.8)
1
From now on w eκλ will stand for the multiplication of two elements in the group ring Z[ ˜
W]
; accordingly the standard notation for the action of the (horizontal) Weyl group on the formal
exponentials, w(e−κλ) = e−κw(λ) , will be replaced by e−κw(λ) = we−κλw−1, cf. (2.2).
12
where Kβ is the Kostant partition function in (3.1). Then the characters generalising (3.1)
are deﬁned according to
ch(Vy) :=
X
z ∈˜W , zy−1 ∈W
ι(z) ∈ι(y) −Q+
z Ky
z =
X
x ∈W ,
ι(x) ∈−y(Q+)
xy K−y−1(ι(x)) .
(3.9)
Equivalently, using that −¯y−1(ι(x)) = −¯y−1(ι(u)) + nβ for xy = uytβ , and denoting
Pr e−κρ dκ :=
X
β∈Q+
Knβ+r eκ β ,
(3.10)
we rewrite (3.9) as
ch(Vy) =
X
u∈T y
uy P−¯y−1(ι(u)) e−κρ dκ .
(3.11)
Multiplying both sides of (3.10) by e
κ
n r , summing over r ∈Q+/nQ+ and making a change
of variables nβ + r = β′ , we recover in the r.h.s. the factor e−κ
n ρ dκ/n, cf. (3.1). Thus
Pr are polynomials of translations in Q+ determined through the quotient of the standard
denominators, dκ/n and dκ.
X
r∈Q+/nQ+
Pr e
κ
n r = e−κ
n ρ dκ/n
e−κρ dκ
=
Y
α>0
n−1
X
kα=0
e
κ
n kα α =
X
µ∈Q+
(n)Kµ e
κ µ
n ,
(3.12)
Pr =
X
ν∈Q+
(n)Kr+nν eκ ν .
(3.13)
The partition function (n)Kµ deﬁned through the last equality in (3.12) is apparently
nonzero for a ﬁnite subset of Q+, i.e., the summation in (3.13) is ﬁnite. The relations
(3.10), (3.13) imply
Knβ+r =
X
ν∈Q+
(n)Knν+r Kβ−ν .
(3.14)
We have the symmetry properties
ch(Va y) = a ch(Vy) ,
a−1 T ay a = T y ,
P−(ay)−1(ι(aua−1)) = P−¯y−1(ι(u)) ,
(3.15)
using that ι(a) = 0 , ι(a−1xa) = ¯a−1(ι(x)) for a ∈A .
Now consider Λ = y · kΛ0 ∈P+ , y ∈
˜
W(+) , hence ι(y) ∈P+. According to our
deﬁnition Vy is reducible with submodules Vyw , w ∈W , since Vι(y) is reducible with
13
submodules Vw−1·ι(y) . In parallel with (3.2) we deﬁne the characters of ‘ﬁnite dimensional
modules’ by a ‘resolution’ formula with respect to the KW Weyl group
χy :=
X
w′∈W
[Λ]
det( ¯w′) ch(Vw′ y) =
X
w∈W
det(w) ch(Vy w) =
X
z∈˜
W , zy−1∈W
my
z z .
(3.16)
We extend this deﬁnition to the whole ˜W, i.e.,
χyw = det(w) χy ,
y ∈˜
W(+) , w ∈W .
(3.17)
Using (3.8) and the intertwining property (2.10) of the map ι (3.16) gives for the multi-
plicities my
z (cf. (3.2) )
my
z =
X
w∈W
det(w) Kyw
z
=
X
w∈W
det(w) Kι(yw)−ι(z) =
X
w∈W
det(w) Kw·ι(y)−ι(z) = mι(y)
ι(z) .
(3.18)
Having an explicit description for the multiplicities we can introduce the supports
Gy of ‘ﬁnite dimensional modules’ as Gy = {z ∈˜W | my
z̸ = 0}. From (3.18) and from
the deﬁnition of the map ι it follows that these ‘generalised weight diagrams’ have the
structure of n-ality zero sl(n) weight diagrams Γι(y) with the points µ̸ ∈Im(ι) excluded.
An sl(3) example is illustrated on ﬁg. 4, see [9] for more examples. Let us point out some
symmetry properties of the generalised weight diagrams. We have from (3.15)
χa y = a χy ,
a ∈A ,
(3.19)
which implies that may
az = my
z. The invariance of the g multiplicities mι(y)
¯a(ι(z)) = mι(y)
ι(z) =
mι(y)
ι(a z a−1) ) implies
my
a−1 z a = my
z ,
a ∈A
(3.20)
and hence a χy a−1 = χy . For z = a t−µ , a ∈A , the symmetry property (3.20) extends to
my
a t−w(µ) = my
a t−µ ,
w ∈W ,
(3.21)
using once again (2.7) to obtain ι(aw a−1 z w−1) = w(ι(z)) as well as the invariance of the
g multiplicities mι(y)
w(ι(z)) = mι(y)
ι(z) for any w ∈W.
Now we examine the case g = sl(3) in details. The 6 element sets T y are T ¯a =
a W a−1 , while T ¯awθ = a T wθ a−1 , and T wθ = {1 , w010 , w020 , w10 , w20 , w0} , see ﬁgs. 5,6,
where the two basic supports are ‘visualized’ as certain subgraphs of the Cayley graph of
14
W . The set of polynomials P−¯y−1(ι(u)) in (3.11) associated with T y and the corresponding
characters for y = 1 , wθ read
ch(Vt−λ) =
X
w∈W
w P−ι(w) e−κ(λ+ρ) dκ
=

(1 + 2eκθ) + w12(2 + eκα1) + w21(2 + eκα2)
+ w1(1 + eκθ + eκα2) + w2(1 + eκθ + eκα1) + 3wθ

e−κ(λ+ρ) dκ ,
(3.22)
ch(Vwθ t−λ ) =
X
u∈T wθ
u wθ P−θ−1(ι(u)) e−κ(λ+ρ) dκ
=

w0 wθ (2 + eκθ) + w010 wθ (1 + 2eκα2) + w020 wθ (1 + 2eκα1)
(3.23)
+ w20 wθ (2 + eκα1) + w10 wθ (2 + eκα2) + wθ (1 + 2eκθ)

e−κ(λ+ρ) dκ .
Now we rewrite the ‘ﬁnite dimensional module’ characters (3.16) expressing them in
terms of the ordinary sl(3) characters, the elements of A and the ‘class’ element
F ≡
X
a∈A
a w0 a−1 = w0 + w1 + w2 .
(3.24)
Proposition 3.1 For any x = x t−λ = t−ν x ∈˜
W(+) , ν = x(λ) we have
χx = det(x)

χν + γ χν−2Λ1 + γ−1 χν−2Λ2 + (F + 2)
 χν−ρ + γ χν−Λ2 + γ−1 χν−Λ1

= χλ+x−1·0 + γ χλ+x−1·(−2Λ1) + γ−1 χλ+x−1·(−2Λ2)
+ (F + 2)
 χλ+x−1·(−ρ) + γ χλ+x−1·(−Λ2) + γ−1 χλ+x−1·(−Λ1)

.
(3.25)
Proof:
First the ‘Verma module’ characters (3.22), (3.23) can be rewritten for any x =
x t−µ ∈˜W as (recall that γ = w12 e−κΛ2)
ch(Vx) =

(1 + γeκx−1(2Λ1) + γ−1eκx−1(2Λ2))
+ (F + 2)(eκx−1(ρ) + γeκx−1(Λ2) + γ−1eκx−1(Λ1))

dκe−κ(µ+x−1(ρ)) .
(3.26)
Next apply the ‘resolution’ formula (3.16) in the form
χx =
X
w′∈W
[x]
det( ¯w′) ch(Vw′ x) =
X
w∈W
det(w) ch(Vxw t−w−1(λ))
15
= det(x)
X
w∈W
det(w) ch(Vw t−w−1(x(λ))) .
To obtain the second equality in (3.25), i.e., to express the characters in terms of sl(3)
characters χλ with λ ∈P+ , we have used (3.4), so that each term det(x) χν−νa turns into
χλ+x−1·(−νa) .
□
Taking into account the same property (3.4) (which in particular implies that χλ = 0
for weights on the shifted reﬂecting hyperplanes, i.e., wα · λ = λ for some α ∈∆+) some
terms in the general expression (3.25) may vanish or compensate each other for some
‘boundary’ weights.
The character formula (3.25) can be also rewritten as a decomposition over W , or U
χy = P
w∈W w B(w)
y
= P
u∈U u C(u)
y
with some coeﬃcients B(w)
y
(C(u)
y
) given by linear
combinations of sl(3) characters and formal exponentials. From this decomposition the
multiplicity my
z in (3.18) can be rewritten as a sum of sl(3) multiplicities. E.g., rewrite
(3.25) for the character χx ,
χx =
X
µ∈P
P λ
µ e−κµ :=
X
a∈A ,µ∈P

(mλ+x−1·(−νa)
µ
+ 2mλ+x−1·(−ν
′
a)
µ
) a + mλ+x−1·(−ν
′
a)
µ
F a

e−κµ
=
X
a∈A ,µ∈P
 mλ+x−1·(−νa)
µ
+ 2mλ+x−1·(−ν
′
a)
µ

a +
  X
b∈A
mλ+x−1·(−ν
′
b)
µ+µb,a

a w0

e−κµ
=
X
z = a t−µ
a ∈A , µ ∈P
mx
z a e−κµ +
X
z = a w0 t−µ
a ∈A , µ ∈P
mx
z a w0 e−κµ
(3.27)
where the weights νa , ν
′
a ∈P can be read from (3.25), and the polynomials P λ
µ = P λ
w(µ)
are invariant under the nonshifted action of W. The weights µb,a ∈P+ result from the
resummation of the ‘odd’ term in (3.25), setting wj a = bw0t−µa,b , b ∈A (since ˜W = U tP ),
which allows comparing the second and the third lines in (3.27) to get an expression for
the multiplicities mx
z in terms of the sl(3) ones.
Let us give some examples
χa = a ,
a ∈A ,
χw0 = 2 + w0 + w1 + w2 = 2 + F ,
χf ≡χt−¯
Λ1 = χ¯
Λ1 + (1 + F) γ−1 = χγ−1 χw20
= γ−1 (w20 + w12 + w01 + w0 + w1 + w2 + 1) ,
χf∗≡χt−¯
Λ2 = χ¯
Λ2 + (1 + F) γ = χγ χw10
= γ (w10 + w21 + w02 + w0 + w1 + w2 + 1) .
(3.28)
16
Finally we deﬁne dimensions of the ‘ﬁnite dimensional modules’ by setting in (3.16)
every (generating) element w e−κµ in Z[ ˜W] to 1, i.e., for y = ¯y t−λ ∈˜
W(+)
Dy =
X
z∈˜
W
my
z .
(3.29)
Using the decomposition formula (3.25) the dimension can be expressed as a sum of di-
mensions Dλ of sl(3) ﬁnite dimensional representations – the ﬁnal expression can be cast
into the form
Dy = 9
Y
α>0
⟨¯y(λ) + ρ
3 , ¯y(α)⟩+ det(¯y)
3
= 1
3
Y
α>0
⟨ι(y) + ρ , α⟩+ det(¯y)
3
= 2
3 Dι(y) + det(¯y)
3
.
(3.30)
Since ι(a) = 0 ,
a ∈A we have Dy = Da y . Here are the ﬁrst few numbers produced from
(3.30): 1 , 5 , 7 , 19 , 23 , 43 , 83 , 103 , . . ..
Remark.
In the case g = sl(2) we have ι(W) ≡Q = 2P and
˜
W(+) ≡A t−P+.
The
supports of the ‘Verma modules’ and the weight diagrams Gy are isomorphic to the supports
of g = sl(2) Verma modules Vι(y) and weight diagrams Γι(y), respectively. Alternatively
the map 1
2ι recovers the supports of modules of highest weight 1
2ι(a t−λ) = λ ∈P+ of the
superalgebra osp(1|2), with a = 1 , γ , labelling the two types of modules for a given λ .
One has χa t−λ = a(χλ + γ χλ−α/2) and we can replace γ simply by a sign ǫ = −1, thus
recovering the supercharacters of the ﬁnite dimensional representations of osp(1|2). The
formula (3.30) is replaced by Dy = ⟨ι(y) + ρ , α⟩= 2 ⟨λ + ρ
2 , α⟩, y = a t−λ .
