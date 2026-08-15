---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-139-6c-a-dyadic-decomposition
section_title: "6C. A dyadic decomposition"
section_number: null
pages: 270-271
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
is a power of 2, say Ki= 2ti , in which case we naturally havet1≤ t2≤···≤ tn, under the hypotheses of the
proposition. We ﬁx m and suppose that S(F; m, k) assumes its maximum for k≤ K at k=(k1,..., kn),
and for each i we decompose
ki=
∑
δi∈Di
2ti−δi,
where Di is a set of distinct nonnegative integersδi≤ ti. Let δ=(δ1,...,δ n) denote a tuple withδi∈ Di
for each i. Let t=(t1,..., tn) and deﬁne the notation 2t−δ=(2t1−δ1,..., 2tn−δn). Given a tuple v, we
deﬁne 2t−δ◦v=(2t1−δ1v1,..., 2tn−δnvn). Furthermore let Vm,δ be an n-tuple deﬁned such that the i-th
entry is(Vm,δ)i= 2ti−δivm,δ,i, where
vm,δ,i=
∑
ei∈Di,ei<δi
2δi−ei < 2δi.
Then we may express
S(F; m, k)=
∑
δ,δi∈Di
S(F; m+ Vm,δ, 2t−δ).
Burgess bounds for short character sums evaluated at forms 1937
After taking absolute values, we can obtain an upper bound by increasing the sum to run over all tuples δ
withδi≤ ti. We get
|S(F; m, k)|≤
∑
δ
0≤δi≤ti
|S(F; m+ Vm,δ, 2t−δ)|.
Then by Hölder’s inequality,
|S(F; m, k)|2r≤
( n∏
i=1
(ti+ 1)
)2r−1 ∑
δ
0≤δi≤ti
∑
v
0≤vi<2δi
|S(F; m+ 2t−δ◦v, 2t−δ)|2r,
where we have possibly enlarged the right-hand side by summing over all possible values forvm,δ,i up to 2δi .
Recalling that for eachm we chose k above to be the length at which the maximum is attained, we then have
∑
m
|mi|≤2q
max
k≤K
|S(F; m, k)|2r≤ T 2r−1 ∑
δ
0≤δi≤ti
∑
v
0≤vi<2δi
∑
m
|mi|≤2q
|S(F; m+ 2t−δ◦v, 2t−δ)|2r
≪ T 2r−1 ∑
δ
0≤δi≤ti
‖2δ‖
∑
m(mod q)
|S(F; m, 2t−δ)|2r,
where T:=∏n
i=1(ti+ 1). Now we perform the key step that accommodates the fact that we only achieve
a saving in the smallest direction of the box.
