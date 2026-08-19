---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-079-4-fωx1x-lxvq-nv2-a15
section_title: "Fω(x1,...,x L)|xv=q nv/2 (A.15)"
section_number: 4
pages: 70-71
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
where
Fω(x1,...,x L) =
∏
v∈ Vertices
(xv− 1/xv)∆v
{( 1
xv−ω/xv
)deg(v)−2+∆v
+
( 1
ωxv− 1/xv
)deg(v)−2+∆v
}
ω≈0=
∑
m≥0
∑
𝓁∈Im
Nm,𝓁
∏
v
x𝓁v
v ·ωm ∈ Z[x±1
1 ,...,x ±1
L ][[ω]] (A.16)
withIm being a ﬁnite set of elements from ZL. If, after expansion in ω one collects coeﬃcients
in front of powers of x, the expression has the following form:
Fω(x1,...,x L)
Formally
= = = =
∑
𝓁∈2ZL+δ
F𝓁
ω
∏
v
x𝓁v
v ∈ Z[ω][[x±1
1 ,...,x ±L
1 ]] (A.17)
where
F𝓁
ω =
∑
m:𝓁∈Im
Nm,𝓁ωm ∈ Z[ω] (A.18)
and
δ∈ ZL/2ZL, δ v≡ degv (mod 2). (A.19)
Note that F𝓁
1 =∑
mNm,𝓁∈ Z does not depend on the choice of ∆ ∈ ZL in (A.13). Formally,
F1(x1,...,x L) =
∑
𝓁∈2ZL+δ
F𝓁
1
∏
v
x𝓁v
v =
∏
v∈ Vertices
{
Expansion
at x→ 0
1
(xv− 1/xv)degv−2 + Expansion
at x→∞
1
(xv− 1/xv)degv−2
}
. (A.20)
– 69 –
Now let us assume that the quadratic form M : ZL× ZL→ Z is negative deﬁnite, 58i.e. σ =
−L). Then we can deﬁne the following q-series, convergent for|q|< 1:
ˆZb(q) Def= = 2−Lq− 3L+∑
vav
4
∑
𝓁∈2M ZL+b
F𝓁
1q− (𝓁,M−1𝓁)
4 ∈ 2−cq∆bZ[[q]] (A.21)
where
c∈ Z+, c ≤L, (A.22)
b∈ (2ZL +δ)/2M ZL/Z2∼= (2CokerM +δ)/Z2
Set∼= H1(M3, Z)/Z2, (A.23)
∆b =−3L +∑
vav
4 − max
𝓁∈2M ZL+b
(𝓁,M−1𝓁)
4 ∈ Q (A.24)
where Z2 acts as follows:
b→−b (A.25)
which is a symmetry of ( A.21).
Using relation ( A.15) and applying Gauss reciprocity formula ( A.8) we arrive at the
following expression for the WRT invariant:
τk[M3(Γ)] = e−πiσ
4 q − 3L+∑
vav
4
