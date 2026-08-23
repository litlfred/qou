---
doc_id: stateintegralsqseries
doc_title: "FROM STATE INTEGRALS TO q-SERIES"
section_id: sec-007-25-some-auxiliary-power-series
section_title: "Some auxiliary power series"
section_number: 2.5
pages: 10-12
source_pdf: state.integrals.qseries.pdf
source_sha256: a5e86443f35e21c0
doc_brief: "FROM STATE INTEGRALS TO q-SERIES — It is well-known to the experts that multi-dimensional state integra ls of prod- ucts of Faddeev’s quantum dilogarithm which arise in Quantum Topolog y can be"
duplicate_of: "arxiv-1304.2705v1"
---
(36) 1
aex− 1 =
∞∑
n=0
pn(a)xn
where
pn(a) =− a
n!(1−a)n+1
n−1∑
m=0
An,mam p0(a) =− 1
1−a
and An,m are Euler triangular numbers (sequence A008292 in the online encyclopedia of
integer sequences [Slo]) that satisfy the recursion
An,m = (n−m)An−1,m−1 + (m + 1)An−1,m
and also given by the sum
An,m =
m∑
k=0
(−1)k
(n + 1
k
)
(m + 1−k)n.
For a detailed discussion on this subject, see [FS70]. A table of the ﬁrst few numbers An,m
is given by
n\m 0 1 2 3 4 5 6 7 8
1 1
2 1 1
3 1 4 1
4 1 11 11 1
5 1 26 66 26 1
6 1 57 302 302 57 1
7 1 120 1191 2416 1191 120 1
8 1 247 4293 15619 15619 4293 247 1
9 1 502 14608 88234 156190 88234 14608 502 1
FROM STATE INTEGRALS TO q-SERIES 11
Lemma 2.4. Forl≥ 1, we have:
(37) dl
dxl log(1−qkebx)|x=0 =blpl−1(qk) +bδl,1
Proof. It follows from
d
dx log(1−qkebx) =b
(
1 + 1
qkebx− 1
)
and Equation (36). □
For positive natural numbers l, r with l≥r and m consider the q-series E(m)
l,r (q) deﬁned
by
E(m)
l,r (q) =
∞∑
k=m+1
qkr
(1−qk)l(38)
Lemma 2.5. (a) We have
(39) E(m)
l,r (q) =
∞∑
s=r
al,s
qs(m+1)
1−qs
where
xr
(1−x)l =
∞∑
s=r
al,sxs
(b) It follows that
(40)
l−1∑
r=0
Al−1,rE(m)
l,r+1(q) =E(m)
l (q)
Proof. For (a), interchangek and s summation:
E(m)
l,r (q) =
∞∑
k=m+1
∞∑
s=r
al,sqsk =
∞∑
s=r
∞∑
k=m+1
al,sqsk =
∞∑
s=r
q(m+1)s
∞∑
k=0
al,sqsk =
∞∑
s=r
al,s
q(m+1)s
1−qs
(b) follows from (a) and the fact that
∑l−1
r=0Al−1,rxr
(1−x)l =
∞∑
s=1
sl−1xs.
□
Lemma 2.6. We have:
φm(x) = exp
(
−
∞∑
l=1
1
l!
l−1∑
r=0
Al−1,rE(m)
l,r+1(q)xl
)
(41)
Proof. It follows from Lemma 2.4 combined with
log(φm(x)) = log
((qm+1ex;q)∞
(qm+1;q)∞
)
=
∞∑
l=m+1
(
log(1−qlex)− log(1−ql)
)
□
12 STA VROS GAROUF ALIDIS AND RINAT KASHAEV
