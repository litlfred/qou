---
doc_id: s0025-5718-07-02027-3
doc_title: "Li(p)-service? An algorithm for computing p-adic polylogarithms"
section_id: sec-003-3-method-of-computation-on-u0-and-u
section_title: "Method of computation on U0 and U"
section_number: 3
pages: 5-6
source_pdf: S0025-5718-07-02027-3.pdf
source_sha256: 080b5ac8542ff19c
toc_source: outline
doc_brief: "Li(p)-service? An algorithm for computing p-adic polylogarithms — We describe an algorithm for computing Coleman’s p-adic poly- logarithms up to a given precision."
---
On U0 we can use the standard expansion in (1.1),
(3.1)
Lin(t) =
∞

k=1
tk
kn ,
which we shall denote by Fn,0(t).
Remark 3.2. As an immediate consequence of the power series expansion of Lin(z)
on U0 and the deﬁnition of Li(p)
n (z) in (2.5) we see that on U0
(3.3)
Li(p)
n (z) =

k≥1
′ zk
kn ,
where the prime indicates that we only sum over those k for which p̸| k. We can
collect terms zk/kn in Lin(z) = 
k≥1
zk
kn for which vp(k) = m and ﬁnd that
(3.4)
Lin(z) =

m≥0
Li(p)
n (zpm)
pmn
as well.
1110
AMNON BESSER AND ROB DE JEU
For the disc U∞we use that
Lin(z) + (−1)nLin(1/z) = −1
n! logn(z)
as in part (2) of Proposition 2.10. This reduces the calculation of Lin(z) to that of
Lin(1/z), with 1/z in U0, and that of log(z).
