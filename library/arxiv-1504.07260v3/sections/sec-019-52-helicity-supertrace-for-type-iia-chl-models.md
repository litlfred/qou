---
doc_id: arxiv-1504.07260v3
doc_title: "Fricke S-duality in CHL models"
section_id: sec-019-52-helicity-supertrace-for-type-iia-chl-models
section_title: "Helicity supertrace for type IIA CHL models"
section_number: 5.2
pages: 32-33
source_pdf: 1504.07260v3.pdf
source_sha256: 707cb014400a3f05
doc_brief: "Fricke S-duality in CHL models — We consider four dimensional CHL models with sixteen spacetime supersym- metries obtained from orbifolds of type IIA superstring on K3×T 2 by aZN symmetry acting"
---
Let us now generalize the previous analysis to CHL models in type IIA string theory. We
are interested in the case where the orbifold groupG is cyclic of orderˆN, with generatorˆg
acting by a shiftδ of a 1/ ˆN period along one of the cycles ofT 2 and by a symmetryg of
the K3 sigma model. Then, the generating functionZIIA
CHL[ˆg] is obtained from (5.4) by the
usual orbifold formula
ZIIA
CHL[ˆg](υ, ¯υ) = ϑ1(υ/2)2 ¯ϑ1(¯υ/2)2
η6¯η6τ2
ξ(υ)¯ξ(¯υ) 1
| ˆN|
ˆN∑
r,s=1
Cgr,gs(υ/2, ¯υ/2)ΘΓ2,2
[r
s
]
, (5.7)
where
ΘΓ2,2
[r
s
]
:=
∑
(pL,pR)∈rδ+Γ2,2
e2πisδ·(pL,pR)q
p2
L
2 ¯q
p2
R
2 . (5.8)
Here we used the fact that the orbifold group acts only on the winding-momenta alongT 2
and on the internal K3 sigma model. The fourth helicity trace is then evaluated to
BCHL[ˆg]
4 = 3
2τ2
1
ˆN
ˆN∑
r,s=1
Cgr,gs(0, 0)ΘΓ2,2
[r
s
]
. (5.9)
We have
Cgr,gs(0, 0) = Tr24(ggcd(r,s,N)) , (5.10)
where 24 denotes the 24 dimensional representation of R-R ground states in the K3 sigma
model. Therefore, ifg has Frame shape∏
a|Nam(a), we obtain
Tr24(gd) =
∑
a|d
m(a)a (5.11)
for alld| ˆN. Assembling the pieces we ﬁnd that the fourth helicity supertrace of the CHL
model becomes
BCHL[ˆg]
4 = 3
2τ2
1
ˆN
∑
d| ˆN
Tr24(gd)
ˆN/d∑
r,s=1
gcd(r,s, ˆN/d)=1
ΘΓ2,2
[dr
ds
]
(5.12)
= 3
2τ2
1
ˆN
∑
d| ˆN
Tr24(gd)
∑
l| ˆN
d
µ(l)
ˆN/ld∑
r,s=1
ΘΓ2,2
[ldr
lds
]
(5.13)
n:=ld= 3
2τ2
1
ˆN
∑
n| ˆN
(∑
d|n
Tr24(gd)µ(n/d)
) ˆN/n∑
r,s=1
ΘΓ2,2
[nr
ns
]
(5.14)
= 3
2τ2
1
ˆN
∑
n| ˆN
(∑
d|n
µ(n/d)
∑
a|d
m(a)a
) ˆN/n∑
r,s=1
ΘΓ2,2
[nr
ns
]
(5.15)
– 31 –
where µ is the Möbius function. Using the property
∑
x|y
µ(x) =
{
1 if y = 1 ,
0 otherwise ,
(5.16)
the divisor sum simpliﬁes:
∑
d|n
µ(n/d)
∑
a|d
m(a)a
t:=n/d
=
∑
a|n
m(a)a
∑
t|n
a
µ(t) =m(n)n (5.17)
so that
BCHL[ˆg]
4 = 3
2τ2
∑
n| ˆN
m(n)n
ˆN
ˆN/n∑
r,s=1
ΘΓ2,2
[nr
ns
]
(5.18)
Finally, we note that, ifT,U are the Kähler and complex moduli ofT 2 in the original
(unorbifolded) model, then
n
ˆN
ˆN/n∑
r,s=1
ΘΓ2,2
[nr
ns
]
(T,U ) = ΘΓ2,2(Tn/ ˆN,Un/ ˆN) , (5.19)
because the LHS is simply (up to a factor1/|η|4) the partition function for a bosonic sigma
model on a torusT 2 with moduli (T,U ), orbifolded by a shift of orderˆN/n along one of
the cycles; this orbifold is again a sigma model onT 2, with theT andU moduli divided by
ˆN/n. Notice that, in our conventions the Kähler and complex structure moduliTIIA and
UIIA of T 2 in the CHL model are related toT,U via
TIIA≡ T
ˆN
UIIA≡ U
ˆN
. (5.20)
Therefore the ﬁnal result for the helicity supertrace is
BCHL[ˆg]
4 = 3
2τ2
∑
n| ˆN
m(n)ΘΓ2,2(nTIIA,nU IIA). (5.21)
