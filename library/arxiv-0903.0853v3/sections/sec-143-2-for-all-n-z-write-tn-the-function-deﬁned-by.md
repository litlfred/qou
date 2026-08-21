---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-143-2-for-all-n-z-write-tn-the-function-deﬁned-by
section_title: "For all n∈ Z, write Tn the function deﬁned by:"
section_number: 2
pages: 89-92
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
---
Tn :=θΛ ,n(z) =
∑
ℓ≤n
βℓ zℓ .
84 CHAPTER 5. SUMMATION AND ASYMPTOTIC THEORY
If j∈{ 1,...,m }, one has:
(5.28) Kn,j := sup
z∈[λj]
⏐
⏐z−n Tn(z)
⏐
⏐< +∞ .
Proof. — From the fundamental relation θ(qz) =qzθ(z), one draws:
θΛ (qz) =L zν θΛ (z), L :=
m∏
j=1
(
− q
λj
) νj
,
whence, for all k∈ Z:
θΛ (qkz) =Lk zkν qk(k−1)ν/2 θΛ (z) .
The relation (5.27) follows immediately.
Sincez−n Tn(z) represents an analytic function over C∗∪{∞} , one obtains
(5.28) by noticing that, if z∈ [λj], then:
Tn(z) =−
∑
ℓ>n
βℓ zℓ ,
which implies that z−n Tn(z) tends to zero as z tends 0 along the half-spiral
λiq−N.
Consider a q-Gevrey series ˆf = ∑
n≥0
anzn∈ C[[z]]q;1/ν with order 1/ν and,
for all ℓ∈ Z, put cℓ := ∑
n≥0
anβℓ−n. Set ℓ :=kν +r withk∈ Z andr∈ Z, and
write:
cℓ =
ν−1∑
j=0
∑
m≥0
amν+jβ(k−m)ν+(r−j).
As we shall see now, the above inﬁnie series converges when th e integer−ℓ is
large enough. Indeed, using relation (5.27), one gets:
β(k−m)ν+(r−j) = (Lq−r)kq−k(k+1)ν/2qkj
(qr−j+kν
L
) m
q−m(m−1)ν/2.
Since ˆf has q-Gevrey order 1/ν, there exists C1 > 0, A1 > 0 such that|an|≤
C1An
1|q|n(n−1)/(2ν) for all n∈ N. One has:
⏐
⏐amν+jβ(k−m)ν+(r−j)
⏐
⏐≤
C1(|L||q|−r)k|q|−k(k+1)ν/2 (|q|kA1)j|q|j(j−1)/(2ν)
(
|q|r+kν+(ν−1)/2
|L|A−ν
1
) m
.
5.3. q-GEVREY THEOREM OF BOREL-RITT AND FLAT FUNCTIONS 85
Therefore, if we set:
C2 :=
ν−1∑
j=0
Aj
1|q|j(j−1)/(2ν),
then we ﬁnd (ℓ =kν +r):
|cℓ|≤ C1C2 (|Lq−r|)k|q|−k(k−1)ν/2∑
m≥0
(
|q|ℓ+(ν−1)/2
|L|A−ν
1
) m
.
It is easy to see that the last series converges if|q|ℓ+(ν−1)/2 <|L|A−ν
1 ; moreover,
when ℓ→−∞ , the sequence (cℓ) is q-Gevrey of level (−ν).
Proposition 5.3.2. — Let ˆf := ∑
n≥0
anzn∈ C[[z]]q;1/ν and let N0 be a neg-
ative integer such that any series deﬁning cℓ converges for ℓ ≤ N0. Let
F(z) := ∑
ℓ≤N0
cℓzℓ. Then, F∈EΛ
0 .
Proof. — Since ( cℓ) is a q-Gevrey sequence of order (−1/ν) for ℓ→−∞ , the
sumF represents an analytic function in C∗∪{∞}, withq-exponential growth
of order ν at zero.
We are left to estimate F(z) and its derivatives along the spirals [ λj] be-
longing to the divisor Λ. Taking in account relation (5.27), one has:
T−n−kν(z) = (Lzν)−k q−k(k−1)ν/2 T−n(qkz).
Therefore, when z∈ [λj], relation (5.28) allows writing F(z) in the following
form:
F(z) =
∑
k≥0
ν−1∑
n=0
akν+n zkν+n TN0−kν−n(z),
and also:
(5.29) F(z) =
ν−1∑
n=0
zn∑
k≥0
L−kakν+n q−k(k−1)ν/2 TN0−n(qkz).
One deduces that F has moderate growth when z → 0 along spirals [ λj]
belonging to the divisor Λ.
As for the derivatives F (ℓ), along each spiral [ λj], with ℓ < νj, one may
proceed all the same: the function T (ℓ)
n is indeed bounded over [ λj] for all
ℓ<ν j and one checks that relation (5.29) remains true up to order ℓ, that is,
86 CHAPTER 5. SUMMATION AND ASYMPTOTIC THEORY
if z∈ [λj]:
F (ℓ)(z) =
ν−1∑
n=0
∑
k≥0
L−kakν+n q−k(k−1)ν/2[
zn TN0−n(qkz)
] (ℓ).
