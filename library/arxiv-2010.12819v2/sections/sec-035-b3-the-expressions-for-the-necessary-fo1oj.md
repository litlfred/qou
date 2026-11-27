---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-035-b3-the-expressions-for-the-necessary-fo1oj
section_title: "B.3 The expressions for the necessary FO1,…,Oj"
section_number: null
pages: 40-42
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
In what follows we shall use the notation {λ} to refer to the set of Bethe roots λ1,...,λ n, while{λ}a denotes
the set with the a’th root removed. We use Sn({µ},{λ}) to refer to scalar products ⟨{µ}|{λ}⟩; these scalar
products are given explicitly below.
Note: As when ﬁnding the Bethe roots, we must again keep in mind the modiﬁed eigenvalue d(λ)→eiφd(λ).
For the norm squared above any overall phase is ignored in the ﬁnal normalization. Below, however, the phases
eiφ do matter. We obtain relative phases between the diﬀerent terms, and also overall phases that we must keep
in mind when we take conjugates as discussed in Section 4.3.1.
B.3.1 Fz,Fzz,F−+
F−+ is taken directly from [58], up to minor changes in notation. For the other two we have chosen to write
in terms of D, as it has somewhat nicer commutation relations. Fz,Fzz are given from FD,FDD in accordance
40
with (159). We have:
FD = −
n∑
a=1
ϕ(η)
ϕ(ξm−λa)
n∏
k=1,k⁄=a
ϕ(λa−λk +η)
ϕ(λa−λk) eiφd(λa)Sn({µ}|ξm,{λ}a), (164a)
FDD =
n∑
a,b=1,b⁄=a
ϕ(η)2
ϕ(ξm+1−λa)ϕ(ξm−λb)
n∏
k=1,k⁄=a
ϕ(λa−λk +η)
ϕ(λa−λk) eiφd(λa)ϕ(λb−ξm+1 +η)
ϕ(λb−ξm+1) (164b)
×
n∏
k=1,k⁄=a,b
ϕ(λb−λk +η)
ϕ(λb−λk) eiφd(λb)Sn({µ}|ξm,ξm+1,{λ}a,b).
ForF−+ we need FBC:
FBC =
n∑
a=1
Ma(ξm+1)Sn({µ}|ξm,{λ}a) +
n∑
b=1,b⁄=a
Mab(ξm+1)Sn({µ}|ξm,ξm+1,{λ}a,b). (165)
For all these we can safely let ξm,ξm+1→η/2, as long as we write the scalar products involving multiple η/2
as shown in section B.3.3.
B.3.2 Fz−+, F−z+
ForFz−+ we will need FDBC :
FDBC =−
n∑
a=1
Ma(ξm+2)
n∑
b=1,b⁄=a
ϕ(η)
ϕ(ξm−λb)
ϕ(λb−ξm+1 +η)
ϕ(λb−ξm+1)
n∏
k=1,k⁄=a,b
ϕ(λb−λk +η)
ϕ(λb−λk) eiφd(λb)
×Sn({µ}|ξm,ξm+1,{λ}a,b)
−
∑
a⁄=b
Mab(ξm+2)
n∑
c=1,c⁄=a,b
ϕ(η)
ϕ(ξm−λc)
ϕ(λc−ξm+1 +η)
ϕ(λc−ξm+1)
ϕ(λc−ξm+2 +η)
ϕ(λc−ξm+2)
n∏
k=1,k⁄=a,b,c
ϕ(λc−λk +η)
ϕ(λc−λk) eiφd(λc)
×Sn({µ}|ξm,ξm+1,ξm+2,{λ}a,b,c),
(166)
where we can again safely let ξm,ξm+1,ξm+2→η/2.
ForF−z+ we need both FBDC and FBAC:
FBDC =−
n∑
a=1
Ma(ξm+2)
n∑
b=1,b⁄=a
ϕ(η)
ϕ(ξm+1−λb)
n∏
k=1,k⁄=a,b
ϕ(λb−λk +η)
ϕ(λb−λk) eiφd(λb)Sn({µ}|ξm,ξm+1,{λ}a,b)
−
∑
a⁄=b
Mab(ξm+2)
n∑
c=1,c⁄=a,b
ϕ(η)
ϕ(ξm+1−λc)
ϕ(λc−ξm+2 +η)
ϕ(λc−ξm+2)
n∏
k=1,k⁄=a,b,c
ϕ(λc−λk +η)
ϕ(λc−λk) eiφd(λc)
×Sn({µ}|ξm,ξm+1,ξm+2,{λ}a,b,c),
(167)
FBAC =
n∑
a=1
Ma(ξm+2)
n∏
k=1,k⁄=a
ϕ(λk−ξm+1 +η)
ϕ(λk−ξm+1) Sn({µ}|ξm,{λ}a)
−
n∑
a=1
Ma(ξm+2)
n∑
b=1,b⁄=a
ϕ(η)
ϕ(λb−ξm+1)
n∏
k=1,k⁄=a,b
ϕ(λk−λb +η)
ϕ(λk−λb) Sn({µ}|ξm,ξm+1,{λ}a,b)
+
∑
a⁄=b
Mab(ξm+2)ϕ(ξm+2−ξm+1 +η)
ϕ(ξm+2−ξm+1)
n∏
k=1,k⁄=a,b
ϕ(λk−ξm+1 +η)
ϕ(λk−ξm+1) Sn({µ}|ξm,ξm+2,{λ}a,b)
−
∑
a⁄=b
Mab(ξm+2) ϕ(η)
ϕ(ξm+2−ξm+1)
n∏
k=1,k⁄=a,b
ϕ(λk−ξm+2 +η)
ϕ(λk−ξm+2) Sn({µ}|ξm,ξm+1,{λ}a,b)
−
∑
a⁄=b
Mab(ξm+2)
n∑
c=1,c⁄=a,b
ϕ(η)
ϕ(λc−ξm+1)
ϕ(ξm+2−λc +η)
ϕ(ξm+2−λc)
n∏
k=1,k⁄=a,b,c
ϕ(λk−λc +η)
ϕ(λk−λc)
×Sn({µ}|ξm,ξm+1,ξm+2,{λ}a,b,c).
(168)
41
In the latter expression, the third and fourth terms are divergent on their own if we take the homogeneous limit.
They will, however, combine into a derivative. Let ξm+1 = η/2, ξm+2 = η/2 +x. We have a common factor
Mab(ξm+2) that causes no problem, and for the rest we can write
1
ϕ(x) [third− fourth]−−−→
x→0
∂x
(
ϕ(η +x)Sn({µ}|η/2 +x,η/ 2,{λ}ab)
)⏐⏐⏐⏐⏐
x=0
∏ϕ(λk +η/2)
ϕ(λk−η/2)
−
(
ϕ(η)Sn({µ}|η/2,η/ 2,{λ}ab)
)
∂x
∏ϕ(λk−x +η/2)
ϕ(λk−x−η/2)
⏐⏐⏐⏐⏐
x=0
. (169)
