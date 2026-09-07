---
doc_id: arxiv-2203.06568v4
doc_title: "Semidefinite programming bounds for binary codes from a split Terwilliger algebra"
section_id: sec-003-underlying-structure
section_title: "Underlying structure"
section_number: null
pages: 14-15
source_pdf: 2203.06568v4.pdf
source_sha256: 256fcfb588dac554
doc_brief: "Semidefinite programming bounds for binary codes from a split Terwilliger algebra — We study the upper bounds for A(n, d), the maximum size of codewords with length n and Hamming distance at least d."
---
Herein we describe a special structure for an association sc heme, which is inspired by the split method used in this paper .
Deﬁnition 27. (m-split property) Let S = ( X, {Ri}k
i=0) be an association scheme. We say that S is m-split for some
1 ≤ m ≤ | X| if there exist m association schemes S1 = ( X1, {R(1)
i }k1
i=0), . . . , Sm = ( Xm, {R(m)
i }km
i=0) and a collection of
maps {fi} such that fi : X − →Xi is surjective for each i and for (x, y) ∈ X × X, (x, y) ∈ Rj if and only if ∑ m
i=1 di = j,
where (fi(x), fi(y)) ∈ R(i)
di for each i.
Clearly, we have the following lemma.
Lemma 28. Every association scheme is 1-split.
For an m-split association scheme S, we can deﬁne an m-split Bose-Mesner algebra by ⨂ m
i=1 B(Si) and an m-split
Terwilliger algebra by ⨂ m
i=1 T (Si), where B(Si) is the Bose-Mesner algebra of Si and T (Si) is the Terwilliger algebra of
Si.
In our case of binary codes, S = H(n, 2) is the Hamming scheme of length n over F2 and each Si is H(ni, 2). Clearly,
S is m-split for 1 ≤ m ≤ n. We may observe that m-split Bose-Mesner algebras induce the m-split generalized Delsarte’s
inequalities and m-split Terwilliger algebras induce m-split triple distances SDP . Moreover, there are ascending chains for
algebras.
B1 ≤ B 2 ≤ · · · ≤ B n, (31)
T1 ≤ T2 ≤ · · · ≤ T n. (32)
In here, Bm is an m-split Bose-Mesner algebra of S, and Tm is an m-split Terwilliger algebra of S for m = 1 , . . . , n. The
chain (31) allows us to combine an l-split generalized Delsarte’s inequalities to an m-split generalized Delsarte’s inequalities
for l ≤ m by merging some partitions as the one. On the other hand, the c hain (32) allows us to add constraints in an l-split
triple distances SDP to an m-split triple distances SDP for some l ≤ m without increasing the number of variables.
VI. C ONCLUSION
In conclusion, we have derived generalized Schrijver semid eﬁnite constraints by considering the split of Terwilliger algebra.
Our split semideﬁnite constraints are a natural generaliza tion of Schrijver’s constraints since they also implied the generalized
Delsarte inequalities.
By implementing a 2-split SDP , we have improved the upper bounds for A(18, 4) and A(19, 4). The MA TLAB programs
of the SDPs in this paper can be found at:
https://github.com/PinChiehTseng/Split SDP solution
We have conﬁrmed that A(18, 4) ≤ 6551 by showing that an upper bound on the numerical error is small enough. As for
A(19, 4), we obtain A(19, 4) ≤ 13087.5 using n1 = 9. The currently best known bound for A(19, 4) is 13104. As for the error
estimate, we obtained an upper bound on the numerical error a s large as 215.7376. Since this estimate is over pessimistic, it
provides no information about out result. Since the solver n ormally returned without any warning, we believed this ﬁgur e is
correct. More accurate solvers could be considered.
Our split approach can be extended to other related problems . For example, one may consider an arbitrary ﬁnite ﬁeld or
k-distance SDP for arbitrary k. Notice that the method described in [GMS12] with |S| = 2 has been applied to improve upper
bounds for constant weight codes. Moreover, the algebra con sidered in [Pol19b] is of the form ⨂
i Ani with∑
i ni = n. The
constraint Rs for constant weight codes has been studied. We can have a simi lar application by adding the constraint R′
s,
which potentially opens a way to strengthen the upper bounds for constant weight codes. As for the upper bounds on the size
of a set with few distances or intersecting families of subse ts [MN11], [BM11], we may directly apply our method to those
problems. Moreover, as Schrijver’s SDP has been extended to the maximum size problem of a code in the fold of n-cube by
Hou et al. [HHGY20], we might have a similar extension. The id ea of isometry groups might be applied to spherical codes as
well.
As an example of association schemes, our method correspond s to a special case of the m-split property of the Hamming
scheme. Thus, our method may be extended to other associatio n schemes, which share this m-split property. It is an interesting
research direction.
Finally, it has been shown that certain polynomial symmetri c properties can be exploited to obtain additional matrix
inequalities and hence improve the semideﬁnite programmin g bounds for the kissing number problem [MdOF18]. It is unkno wn
whether a similar ideas could be applied to the case of binary codes to obtain better bounds for A(n, d).
15
ACKNOWLEDGEMENT
We would like to thank Dion Gijswijt, Alexander Schrijver, a nd Hajime Tanaka for helpful discussions. We would also like
to thank the anonymous referees for their valuable comments .
PCT and CYL were supported by the Ministry of Science and Tech nology (MOST) in Taiwan under Grant MOST110-2628-
E-A49-007. WHY was supported by MOST under Grant109-2628-M -008-002-MY4.
