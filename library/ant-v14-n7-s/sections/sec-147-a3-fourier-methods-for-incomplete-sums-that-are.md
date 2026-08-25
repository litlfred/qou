---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-147-a3-fourier-methods-for-incomplete-sums-that-are
section_title: "A.3. Fourier methods for incomplete sums that are not short"
section_number: null
pages: 282-283
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
appears as a natural constraint of the ranges for which our main results hold. This is not a deﬁcit, for
recall that on the other side of this threshold, different methods, which also rely on Weil bounds, become
feasible, for appropriate F. To bound S(F; N, H) in cases where Hi≫ q1/2, an advantageous strategy is
to “complete the sum,” writing
S(F; N, H)=
∑
a=(a1,...,an)
ai (mod q)
χ( F(a))
∑
x∈Zn
xi∈(Ni,Ni+Hi]
1x≡a(mod q).
Burgess bounds for short character sums evaluated at forms 1949
One then expands the sum over x using
1x≡a(mod q)= 1
qn
∑
k(mod q)
eq(k·(x− a))
so that
S(F; N, H)= 1
qn
∑
k(mod q)
∑
a(mod q)
χ( F(a))eq(−k· a)41(a1/q)··· 4n(an/q),
in which4(α)= min{Hi,‖α‖−1}, where‖α‖ denotes the distance fromα to the nearest integer. One then
aims to show that under appropriate assumptions on the smoothness of F∈ Fq[x1,..., xn], for generic k
a Weil bound applies so that the internal sum over a is O(qn/2). (Note that this does require the deep
input of a Weil-strength bound for a multi-dimensional mixed character sum; see, e.g., [Katz 2006].) The
resulting sum over k is then expected to be roughly on the order of O(q−n/2‖H‖+ qn/2(log q)n), which is
o(‖H‖) in the case that Hi≫ q1/2 log q for each i= 1,..., n, that is, the setting that is complementary to
that of this paper. In a hybrid case, in which some Hi are smaller than q1/2 and some are larger, one could
adopt a hybrid strategy; this regime is closely related to [Pierce 2006; Heath-Brown and Pierce 2012].
