---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems"
section_id: sec-020-9-comments-on-universality
section_title: "Comments on universality"
section_number: 9
pages: 12-13
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
toc_source: outline
doc_brief: "KPZ limit theorems — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
Comments on universality
KPZ limit theorems are proved for many isolated examples of integrable models. In this ﬁnal section, we
discuss a few instances that universality is proved.
9.1
Thin DLPP
The universality should hold for the last passage time L(n, k) as n, k →∞. It is easy to prove it for thin
rectangles. Recall from Subsection 2.3 that ws denotes the random variable at site s ∈Z, representing the
passage time through the site.
Theorem 9.1 ( [16,21]). Suppose that ws is an arbitrary random variable which has all moments. Assume
that the mean is zero and the variance is one. Then, for every x,
lim
n,k→∞P
L(n, k) −2
√
nk
n
1
2 k−1
6
≤x

= FTW(x)
for k = [na]
with any 0 < a < 3/7.
The restriction a < 3/7 is technical. If we assume only ﬁnite p moments for p > 2, then the result holds
for thinner rectangles satisfying 0 < a < 3(p−2)
7p
.
For the case of ﬁxed k and large n, a directed path looks like the one in Figure 13. Since the sum of ws
on each row converges to a Brownian motion, Donsker’s theorem implies that
L(n, k)
√n
⇒Dk
where Dk =
sup
0=t0≤t1≤···≤tk=1
k
X
i=1
(Bi(ti) −Bi(ti−1))
and Bi(t), i = 1, · · · , k, are independent Brownian motions. On the other hand, it is known [19] that
lim
k→∞P((Dk −2
√
k)k1/6 ≤x) = FTW(x).
12
This limit is a consequence of an explicit formula of the exponential DLPP by letting n →∞ﬁrst and
then taking k →∞. We prove Theorem 9.1 by showing that if n, k →∞but k grows slowly enough, we
can take n →∞ﬁrst and k →∞later. This argument is achieved by the Skorohod embedding or the
Koml´os–Major–Tusn´ady embedding. However, the proof breaks down if α ≥3/7 since we cannot ignore the
upward parts of the paths anymore. For k = O(n), limit theorems are proved only for a few examples.
