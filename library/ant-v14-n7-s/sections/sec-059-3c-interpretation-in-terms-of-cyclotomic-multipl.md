---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-059-3c-interpretation-in-terms-of-cyclotomic-multipl
section_title: "3C. Interpretation in terms of cyclotomic multiple harmonic sums viewed as functions of the upper bound of their domain of summation"
section_number: null
pages: 71-73
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
bound of their domain of summation. The main result above gives a description of harq˜α as a function
of q˜α (and˜α) regarded as a p-adic integer. Let us extend the question and consider the study of harm as a
function of m, for any m∈ N∗ regarded as a p-adic integer. We are going to remove the factor mweight in
harm, i.e., consider the (nonweighted) cyclotomic multiple harmonic sums hm((ni)d;(ξi)d+1) of (0-2).
Intuitively, hm is a highly discontinuous function of m, but we have proved by the main theorem
that harq˜α has a power series expansion in terms of q˜α. The goal of the next proposition is to write a
decomposition of hm in a way which explains the relation between these two phenomena, by using the
q-adic expansion of m, in order to clarify the dependence of har m in m.
Below we use the following deﬁnition: an increasing connected partition of a subset of N is a partition
of that set into sets Ji of consecutive integers, such that each element of Ji is less than each element of
Ji′ when i< i′.
Proposition 3C.1. (i) Let m∈ N∗, and let its q-adic expansion be
m= ayd′ q yd′+ ayd′−1q yd′−1+···+ ay1q y1,
with yd′>··· > y1, and ayd′,..., ay1∈{ 1,..., q− 1}. Let
ν j′= ayd′ q yd′+···+ ayd′− j′+1q yd′− j′+1
1738 David Jarossay
for j′∈{ 1,..., d′}. We have
hm((ni)d;(ξi)d+1)=
∑
n={ν j′′
1
,...,ν j′′
d′′}⊂{ν1,...,νd′}
:n↪→{1,...,d} injective
J0∐···∐Jd′={1,...,d}−( n), satisfying(∗)
d′′
∏
j′′=1
1
ν
n(ν j′′)
j′′
d′
∏
j′=0
∑
l jmax
j′ ,...,l jmin
j′
>0
( j max
j′
∏
u= j min
j′
(−nu
lu
))(d′− j′+1∑
l=d′
ayl q yl
)∑ jmax
j′
u= jmin
j′
lu
× hayd′− j′ q
yd′− j′((n j+ l j) j j′,min< j< j j′,max;(ξ) jmin< j< jmax+1), (3-6)
where(∗) is that J0∐···∐ Jd′ is an increasing connected partition of{1,..., d}−( n), such that each
J(ν j′′)∐···∐ J(ν j′′+1)−1, j′′= 1,..., d′′, is an increasing connected partition of({1,..., d}−( n))∩
](ν j′′),(ν j′′+1)[.
(ii) Let n∈ N∗, whose decomposition in base q is of the form aq y, with a∈{ 1,..., q− 1} and y∈ N∗.
Letν j′= j′q y for j′∈{ 1,..., a− 1}. We have
haq y((ni)d;(ξi)d+1)=
∑
n={ν j′′
1
,...,ν j′′
d′′}⊂{ν1,...,νd′}
:n↪→{1,...,d} injective
J0∐···∐Jd′={1,...,d}−( n), satisfying(∗)
d′′
∏
j′′=1
1
ν
n(ν j′′)
j′′
d′
∏
j′=0
∑
l jmax
j′ ,...,l jmin
j′
>0
( j max
j′
∏
u= j min
j′
(−nu
lu
))
×( j′q y)
∑ jmax
j′
u= jmin
j′
lu
hq
yd′− j′((n j j′+ l j j′) jmin< j′< jmax;(ξ j j′) jmin< j′< jmax+1). (3-7)
Proof. (i) and (ii) We apply the “formula of splitting” of multiple harmonic sums of [Jarossay 2015,
Section 3] at{ν1,...,ν r}; this gives
hm((ni)d;(ξi)d+1)=
∑
n={ν j1,...,ν jd′′}⊂{ν1,...,νd′}
:n↪→{1,...,d} injective
J0∐···∐Jd′={1,...,d}\( n), satisfying(∗)
d′′
∏
j′′=1
1
n
n(ν j′′)
(ν j′′)
d′
∏
j′=0
hν j′,ν j′+1(w|J j′)
and we express each factor hν j′,ν j′+1(w|J j′) in terms of hν j′+1−ν j′ by the p-adic formula of shifting of
multiple harmonic sums of [Jarossay 2015, Section 4.1] writing J j′=[ j min
j′ , j max
j′ ]. □
Example 3C.2 (N= 1 and d= 1). For all n∈ N∗, we have
hm(n)=
hayd′+1(n)
(pyd′)n +
d′−1∑
i=1
∑
l>0
hayi+1(n+ l)
(pyi)n+l
(−n
l
)
(ayd′ pyd′+···+ ayi+1 pyi+1)l
+
∑
1⩽ j⩽d′
0⩽a′
y j⩽ay j−1
∑
l>0
(−n
l
)
hy j(n+ l)
( d′
∑
m= j+1
aym pym+ a′
j py j
)l
. (3-8)
Pro-unipotent harmonic actions and dynamical properties of p -adic cyclotomic multiple zeta values 1739
In the formulas of the proposition, there are terms which are analytic functions of a power of q by the
main theorem, and certain factors which are “polar” in function of the q-adic expansion of m. This sheds
light on the dependence of hm on m.
The reason why studying hm as a function of m is a natural comes from [Jarossay 2019], in which this
question appeared implicitly. We have studied the map sending m to the coefﬁcient of degree m in the
power series expansion at 0 of the overconvergent p-adic multiple polylogarithm Li†
p,α[w], forw any
word on e0∪µN . We have proved that it can be extended to a locally analytic map on Z(N)
p = lim←−−Z/N puZ
[loc. cit., Section 3]. This map is a linear combination of multiple harmonic sums over the ring generated
by p-adic cyclotomic multiple zeta values. Thus we can interpret them as a “regularization” of multiple
harmonic sums. See also Appendix A of [loc. cit.].
