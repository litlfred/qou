---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-035-b-proof-of-the-gamma-factor-and-by-hidetoshi-awa
section_title: "Proof of the gamma factor () and (), by Hidetoshi Awata"
section_number: B
pages: 75-79
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
doc_brief: "Volume Conjecture: Reﬁned and Categoriﬁed — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebraic curve, the zero"
---
Let PR
h
c 1−L
1−q2
i
be the Macdonald function PR(x; q1, q2) with the specialization pn := P∞
i=1 xn
i =
cn 1−Ln
1−qn
2 . The Pieri formula [51](Ch. VI.6) gives
PSr(x; q1, q2)PSr(x; q1, q2) =
r
X
ℓ=0
N Sr+ℓ,r−ℓ
SrSr
PSr+ℓ,r−ℓ(x; q1, q2),
(B1)
PΛr(x; q1, q2)PΛr(x; q1, q2) =
r
X
ℓ=0
N Λr+ℓ,r−ℓ
ΛrΛr
PΛr+ℓ,r−ℓ(x; q1, q2)
(B2)
with
N Sr+ℓ,r−ℓ
SrSr
:=
r−ℓ
Y
j=1
1 −qj−1
1
q2
1 −qj
1
·
r+ℓ
Y
j=2ℓ+1
1 −qj−1
1
q2
2
1 −qj
1q2
·
r
Y
j=ℓ+1
 
1 −qj
1
1 −qj−1
1
q2
!2
,
(B3)
N Λr+ℓ,r−ℓ
ΛrΛr
:=
ℓ
Y
i=1
1 −q1qi−1
2
1 −qi
2
·
2ℓ
Y
i=ℓ+1
1 −qi
2
1 −q1qi−1
2
.
(B4)
Note that above N Sr+ℓ,r−ℓ
SrSr
and N Λr+ℓ,r−ℓ
ΛrΛr
are invariant under the transformation q1 →q−1
1
and q2 →q−1
2 . The specialization formula [51](Ch. VI.6)
PR

c 1 −L
1 −q2

= cr
Y
(i,j)∈R
qi−1
2
−qj−1
1
L
1 −qRi−j
1
q
Rt
j−i+1
2
(B5)
yields
PSr+ℓ,r−ℓ
h
c 1−L
1−q2
i
PSr
h
c 1−L
1−q2
i
= cr
Qr−ℓ
j=1(q2 −qj−1
1
L) · Qr+ℓ
j=r+1(1 −qj−1
1
L) · Qr
j=r−ℓ+1(1 −qj−1
1
q2)
Q2ℓ
j=1(1 −qj−1
1
q2) · Qr+ℓ
j=2ℓ+1(1 −qj−1
1
q2
2)
,
PΛr+ℓ,n−ℓ
h
c 1−L
1−q2
i
PΛr
h
c 1−L
1−q2
i
= cr
Qr−ℓ
i=1(qi−1
2
−q1L) · Qr+ℓ
i=r+1(qi−1
2
−L) · Qr
i=r−ℓ+1(1 −qi
2)
Q2ℓ
i=1(1 −qi
2) · Qr+ℓ
i=2ℓ+1(1 −q1qi
2)
.
Let
gℓ:= c−r
r
Y
j=ℓ+1
1 −qj−1
1
q2
1 −q−j
1
,
(B6)
g′
ℓ:= c−r
r
Y
i=1
q1−i
2
·
ℓ
Y
i=1
1 −qi
2
1 −q−1
1 q1−i
2
,
(B7)
– 74 –
then we have
Proposition.
PSr

c 1 −L
1 −q2

=
r
X
ℓ=0
gℓN Sr+ℓ,r−ℓ
SrSr
PSr+ℓ,r−ℓ

c 1 −L
1 −q2

,
(B8)
PΛr

c 1 −L
1 −q2

=
r
X
ℓ=0
g′
ℓN Λr+ℓ,r−ℓ
ΛrΛr
PΛr+ℓ,r−ℓ

c 1 −L
1 −q2

.
(B9)
Proof. First, let
fℓ:= gℓN Sr+ℓ,r−ℓ
SrSr
PSr+ℓ,r−ℓ
h
c 1−L
1−q2
i
PSr
h
c 1−L
1−q2
i
= (1 −q2ℓ
1 q2)
Qr
j=ℓ+1(−qj
1)(1 −qj
1) · Qr−ℓ
j=1(q2 −qj−1
1
L) · Qr+ℓ
j=r+1(1 −qj−1
1
L)
Qr−ℓ
j=1(1 −qj
1) · Qr+ℓ
j=ℓ(1 −qj
1q2)
, (B10)
f ′
ℓ:= g′
ℓN Λr+ℓ,r−ℓ
ΛrΛr
PΛr+ℓ,r−ℓ
h
c 1−L
1−q2
i
PΛr
h
c 1−L
1−q2
i
= (−q1)ℓ(1 −q1q2ℓ
2 )
r
Y
i=ℓ+1
q1−i
2
×
Qr
i=r−ℓ+1(1 −qi
2) · Qr−ℓ
i=1(qi−1
2
−q1L) · Qr+ℓ
i=r+1(qi−1
2
−L)
Qℓ
i=1(1 −qi
2) · Qr+ℓ
i=ℓ(1 −q1qi
2)
.
(B11)
The residues of fℓand f ′
ℓat q2 = q−k
1
and q1 = q−k
2
(ℓ≤k ≤ℓ+ r), respectively, are
−qk
1Resq2=qk
1fℓ= q−kr
1
(q−ℓ
1
−qℓ−k
1
)q(k+1)ℓ
1
ℓ
Y
j=1
(−q−j
1 ) ·
k−ℓ
Y
j=1
(−qj
1)
×
Qr
j=1(−qj
1)(1 −qj
1)
Qℓ
j=1(1 −qj
1) · Qk−ℓ
j=1(1 −qj
1)
·
Qr+k−ℓ
j=k+1(1 −qj−1
1
L) · Qr+ℓ
j=r+1(1 −qj−1
1
L)
Qr−ℓ
j=1(1 −qj
1) · Qr+ℓ−k
j=1
(1 −qj
1)
,
(B12)
−qk
2Resq1=qk
2f ′
ℓ= q−kr
2
(q−ℓ
2
−qℓ−k
2
)
ℓY
i=1
(−qi
2) ·
k−ℓ
Y
i=1
(−qi
2)
×
Qr
i=1 q1−i
2
(1 −qi
2)
Qℓ
i=1(1 −qi
2) · Qk−ℓ
i=1(1 −qi
2)
·
Qr+k−ℓ
i=k+1(qi−1
2
−L) · Qr+ℓ
i=r+1(qi−1
2
−L)
Qr−ℓ
i=1(1 −qi
2) · Qr+ℓ−k
i=1
(1 −qi
2)
.
(B13)
Note that each second line (i.e. (B12) and (B13)) of the above two equations is symmetric
under the replacement ℓ↔k −ℓ. Thus one can show that
Resq2=q−k
1 (fℓ+ fk−ℓ) = Resq1=q−k
2 (f ′
ℓ+ f ′
k−ℓ) = 0.
(B14)
– 75 –
Next, let
f :=
r
X
ℓ=0
fℓ,
f ′ :=
r
X
ℓ=0
f ′
ℓ.
(B15)
The residue of f at q2 = q−k
1
is
Resq2=q−k
1 f =
min(k,r)
X
ℓ=max(0,k−r)
Resq2=q−k
1 fℓ
=


⌊k
2 ⌋
X
ℓ=max(0,k−r)
+
min(k,r)
X
ℓ=⌈k
2 ⌉

Resq2=q−k
1 fℓ
=
⌊k
2 ⌋
X
ℓ=max(0,k−r)
Resq2=q−k
1 (fℓ+ fk−ℓ) = 0,
(B16)
and also Resq=t−kf ′ = 0. Here the ﬂoor function ⌊x⌋denotes the largest integer not greater
than x and the ceiling function ⌈x⌉denotes the smallest integer not less than x. Furthermore
limq2→∞f, limq1→∞f ′ < ∞. Therefore f and f ′ are constant in q2 and q1, respectively. But
lim
q2→0 f = lim
q2→0 f0 = 1,
lim
q1→∞f ′ = lim
q1→∞f ′
0 = 1.
(B17)
Therefore f = f ′ = 1.
Substituting c := (q2/L)
1
2 into (B8) and (B9) yields
PSr

L
1
2 −L−1
2
q
1
2
2 −q
−1
2
2

=
r
X
ℓ=0
gℓN Sr+ℓ,r−ℓ
SrSr
PSr+ℓ,r−ℓ

L
1
2 −L−1
2
q
1
2
2 −q
−1
2
2

,
(B18)
PΛr

L
1
2 −L−1
2
q
1
2
2 −q
−1
2
2

=
r
X
ℓ=0
g′
ℓN Λr+ℓ,r−ℓ
ΛrΛr
PΛr+ℓ,r−ℓ

L
1
2 −L−1
2
q
1
2
2 −q
−1
2
2

,
(B19)
where gℓ= γℓλℓand g′
ℓ= γ′
ℓλ′
ℓwith
λℓ:= (L/q2)
r
2
r
Y
j=ℓ+1
(−q
j−1
2
1
q
1
2
2 ),
γℓ:=
r
Y
j=ℓ+1
q
j−1
2
1
q
1
2
2 −q
1−j
2
1
q
−1
2
2
q
j
2
1 −q
−j
2
1
,
(B20)
λ′
ℓ:= (L/qr
2)
r
2
ℓY
i=1
(−q
i−1
2
2
q
1
2
1 ),
γ′
ℓ:=
ℓ
Y
i=1
q
i
2
2 −q
−i
2
2
q
i−1
2
2
q
1
2
1 −q
1−i
2
2
q
−1
2
1
.
(B21)
– 76 –
Note that γℓ= γSr+ℓ,r−ℓ
SrSr
, γ′
ℓ= γΛr+ℓ,r−ℓ
ΛrΛr
. If we set L := qN
2 , then PR
"
L
1
2 −L−1
2
q
1
2
2 −q
−1
2
2
#
= MR(q̺2; q1, q2),
λℓ= λ(+)
Sr+ℓ,r−ℓ(Sr, Sr) and λ′
ℓ= λ(+)
Λr+ℓ,r−ℓ(Λr, Λr). Hence we obtain
MSr(q̺2) =
r
X
ℓ=0
γSr+ℓ,r−ℓ
SrSr
λ(+)
Sr+ℓ,r−ℓ(Sr, Sr)N Sr+ℓ,r−ℓ
SrSr
MSr+ℓ,r−ℓ(q̺2; q1, q2),
(B22)
MΛr(q̺2; q1, q2) =
r
X
ℓ=0
γΛr+ℓ,r−ℓ
ΛrΛr
λ(+)
Λr+ℓ,r−ℓ(Λr, Λr)N Λr+ℓ,r−ℓ
ΛrΛr
MΛr+ℓ,r−ℓ(q̺2; q1, q2).
(B23)
– 77 –
