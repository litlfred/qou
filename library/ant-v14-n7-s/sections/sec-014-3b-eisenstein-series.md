---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-014-3b-eisenstein-series
section_title: "3B. Eisenstein series"
section_number: null
pages: 17-18
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
in the de Rham cohomology. In the next section, we’ll exhibit a canonical system of modular units – the
Siegel units – whose de Rham realisations can be written down very explicitly in terms of the following
Eisenstein series.
Deﬁnition 3.3 (compare [Kato 2004, §3]). Let τ∈ H, k an integer> 2, and β∈ Q/Z, with β⁄= 0 if
k= 2. Deﬁne
F(k)
β (τ):= (k− 1)!
(−2πi)k
∑′
(m,n)∈Z2
e2πiβm
(mτ+ n)k,
where the prime denotes that the term (m, n)=(0, 0) is omitted. This is a modular form of weight k and
level01(N), for any N such that Nβ= 0.
(Kato deﬁnes a slightly more general class of Eisenstein series F(k)
α,β; we shall only use the case α= 0,
so we drop it from the notation.)
For the L-value calculations in the Appendix, we shall need to use the fact that this series is a
specialisation of a real-analytic family. Forℜ(s)> 1− 1
2k, we deﬁne
E(k)
β (τ, s):= 0(s+ k)
(−2πi)kπ s
∑′
(m,n)∈Z2
Im(τ) s
(mτ+ n+β)k|mτ+ n+β|2s, (3-1)
where the prime denotes that the term (m, n)=(0, 0) is omitted ifβ= 0 (but included otherwise). This
has analytic continuation to all s∈ C, and we have
F(k)
β (τ)= E(k)
β (τ, 1− k).
(See, e.g., [Lei et al. 2014, 4.2.2(iv)].)
1684 David Loeﬄer and Chris Williams
