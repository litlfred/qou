---
doc_id: arxiv-2205.01282v2
doc_title: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES YUYA MURAKAMI"
section_id: sec-008-4-expressions-of-homological-blocks-as-false-the
section_title: "Expressions of homological blocks as false theta functions"
section_number: 4
pages: 9-11
source_pdf: 2205.01282v2.pdf
source_sha256: 00f656afa60db838
doc_brief: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES YUYA MURAKAMI — In this paper, we prove a conjecture by Gukov–Pei–Putrov–Vafa for a wide class of plumbed"
---
In this section, we represent the homological block of M(Γ) as a false theta function.
For the plumbed homology sphere M(Γ), the homological block bZΓ(q) is defined as follows.
Definition 4.1 ([GPPV20, Subsection 3.4]). The homological block of the plumbed homology sphere
M(Γ) is defined as
bZΓ(q) = 2−|V|q−P
v∈V (wv+3)/4p.v.
Z
|zv|=1,v∈V
Θ−W,δ(q;z)
Y
v∈V
(zv− 1/zv)2−deg(v) dzv
2π√−1zv
,
where p.v. is the Cauchy principal value defined as
p.v.
Z
|z|=1
:= lim
ε→+0
 Z
|z|=1+ε
+
Z
|z|=1−ε
!
,
δ := (deg(v))v∈V∈ ZV , and
Θ−W,δ(q;z) :=
X
l∈2ZV +δ
q−tlW−1l/4Y
v∈V
zlv
v
10 Y. MURAKAMI
is the theta function.
Here we remark that our definition of the Cauchy principal value is half of the previous definition
in [GPPV20] ([GPPV20, p.55]). However, our definition of the homological block bZΓ(q) is the same
as [GPPV20] since we multiply it by 2−|V|.
Our main result in this section is the following.
Proposition 4.2. It holds
bZΓ(q) = (−1)|V1|2−|V≥3|q−(P
v∈V (wv+3)+P
i∈V1 1/wi)/4
X
e∈{±1}V≥3

 Y
v∈V≥3
edeg(v)+|v|
v

X
α∈S
ε(α)
X
n∈ZV≥3
P (n)qQ(e(n+α)),
where P (n) is the polynomial defined in (2.2), Q(x) := txSx and ex := ((xv)v∈V2, (evxv)v∈V≥3) for
x∈ ZV≥2 and e∈{± 1}V≥3.
To prove this proposition, we need the following lemma.
Lemma 4.3 ([AM22, p. 743]) . Ford∈ Z>0 and l∈ Z, it holds that
p.v.
Z
|z|=1
zl−1
(z− 1/z)d−2
dz
2π√−1 =



−2l d = 1,l∈{± 1},
2 d = 2,l = 0,
sgn(l)d
m +d− 3
d− 3

d≥ 3,±l∈d− 2 + 2m for some m∈ Z≥0,
0 otherwise.
Proof of Proposition 4.2. By definition, we have
2|V|q
P
v∈V (wv+3)/4bZΓ(q)
=
X
l∈2ZV +δ
q−tlW−1l/4Y
v∈V
p.v.
Z
|zv|=1
zlv−1
v
(zv− 1/zv)deg(v)−2
dzv
2π√−1.
By Lemma 4.3, this is equal to
X
l=(l1,l2,l≥3),
l1∈{±1}V1,l 2=0,
±l≥3∈2Z
V≥3
≥−1+δ≥3
q−tlW−1l/4

Y
i∈V1
(−2li)

 2|V2|
Y
v∈V≥3
sgn(lv)deg(v)
(|lv|− deg(v) + 2)/2 + deg(v)− 3
deg(v)− 3

,
where δ≥3 := (deg(v))v∈V≥3∈ ZV≥3. For l = t(ε1,l 2,l≥3) with l2 = 0, we have
−tlW−1l =Q(l≥3 +tTl 1)−
X
i∈V1
l2
i
wi
by Proposition 2.2 (i). By letting
li =evεi, l v =ev(nv + deg(v)− 2), e v,εi∈{± 1}, n v∈ Z≥0
for v∈V≥3 and i∈v, we obtain
(−1)|V1|2|V≥3|q(P
v∈V (wv+3)+P
i∈V1 1/wi)/4bZΓ(q)
=
X
e∈{±1}V≥3

 Y
v∈V≥3
edeg(v)
v

 X
ε∈{±1}V1

 Y
v∈V≥3
Y
i∈v
evεi


X
n∈Z
V≥3
≥0
qQ(e(n+δ≥3/2+tTε/ 2−(1,...,1))) Y
v∈V≥3
nv + deg(v)− 3
nv

.
WRT INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES 11
Since W−1∈ Aut(ZV ), every matrix entries of StT is integers by Proposition 2.2 (i). Thus, for any
ε∈{± 1}V1, we have tTε/ 2∈ (2S)−1(ZV≥2). Since
1
2
tTε =
 X
i∈v
εi
2wi
!
v∈V≥2
by the definition of T in Section 2.2, the map
{±1}V1 −→ S
ε 7−→ δ≥3/2 +tTε/ 2− (1,..., 1)
is bijective by Lemma 2.7 (ii). Thus, the claim follows by letting α =δ≥3/2 +tTε/ 2− (1,..., 1). □
