---
doc_id: arxiv-math-0006051v1
doc_title: "Finite and p-adic polylogarithms"
section_id: sec-002-2-the-proof
section_title: "The proof"
section_number: 2
pages: 2-4
source_pdf: 0006051v1.pdf
source_sha256: 10483e75bd3655ea
doc_brief: "Finite and p-adic polylogarithms — 8 sections: AMNON BESSER; Introduction; The proof"
---
The connection between p-adic and ﬁnite polylogarithms is made by the following
Proposition 2.1. Let Li(p)
n (z) := Li n(z) − Lin(zp)/p n. Then Li(p)
n (X) ⊂ W and
the function Li(p)
n reduces modulo p to (1 − zp)− 1 lin(z).
Proof. According to [Col82], the function Li (p)
n (z) can be computed as
Li(p)
n (z) =
∫
Z×
p
x− ndµ z(x) ,
where µ z is the measure on Zp deﬁned by
µ z(a + pmZp) = za1 − zpm a = 0, 1, . . . , p m − 1 .
Since for z ∈ X µ z takes integral values, this shows the ﬁrst statement. Reducing
modulo p we may replace the function x ↦→x− k by the function x ↦→a− k if x ≡ a
(mod p), which is congruent to it modulo p on Z×
p . This implies that Li (p)
n (z) is
congruent modulo p to
p− 1∑
a=1
a− nµ z(a + pZp) =
p− 1∑
a=1
a− n za
1 − zp .
Corollary 2.2. Let α ∈ X be a root of unity. Then we have Lin(α ) ∈ pnW and
p− n Lin(α ) ≡ − lin(σ (α ))/ (1 − α ) (mod p).
Proof. Since α ∈ X ⊂ W the order of α is prime to p and we have α pk
= α for
some k. By using the deﬁnition of Li (p)
n repeatedly we ﬁnd
Lin(α ) = Li (p)
n (α ) + p− n Lin(α p)
= Li (p)
n (α ) + p− n Li(p)
n (α p) + p− 2n Lin(α p2
)
· · · =
k− 1∑
i=0
p− in Li(p)
n (α pi
) + p− kn Lin(α pk
) .
FINITE AND p-ADIC POLYLOGARITHMS 3
Since α pk
= α we may move the last term to the left hand side of the equation and
obtain
Lin(α ) = 1
1 − p− kn
k− 1∑
i=0
p− in Li(p)
n (α pi
)
= pn
pkn − 1
k− 1∑
i=0
p(k− 1− i)n Li(p)
n (α pi
) ∈ pnW ,
and dividing by pn and reducing modulo p we obtain using the proposition
− Li(p)
n (α pk− 1
) ≡ (1 − (α pk− 1
)p)− 1 lin(α pk− 1
) ≡ − lin(σ (α ))/ (1 − α ) (mod p) .
Proposition 2.3. Let α be a root of unity in X. Set ~Lin(α ) = p− n Lin(α ). Then
for w ∈ W we have
p− n Lin(α (1 + pw)) ≡
n∑
k=0
~Lin− k(α ) wk
k! (mod p) .
Proof. Let gn(w) = p− n Lin(α (1 + pw)). Then one ﬁnds
g0(w) = α (1 + pw)
1 − α (1 + pw) = α
1 − α
1 + pw
1 − α
1− α pw = ~Li0(α ) +
∞∑
k=1
bk(pw)k
with bn ∈ W . Write
gn(w) = ~Lin(α ) +
∞∑
k=1
dn
k wk .
It is easy to verify that
d
dw gn(w) = gn− 1(w) 1
1 + pw = gn− 1(w)(1 +
∞∑
k=1
ck(pw)k) ,
with ck ∈ W . To ﬁnd the coeﬃcients dn
k modulo p for k < p one can simply reduce
the above equations modulo p and one easily ﬁnds that
dn
k ≡
{ ~ Lin− k(α )
k! when k ≤ n
0 when n < k < p .
It thus remains to show that also for k ≥ p the coeﬃcient dn
k is divisible by p.
For this it is easier to consider the function fn(u) = Li n(α + u) which satisﬁes
f0(u) ∈ W [[u]], d/duf n+1(u) = g(u)fn(u) with g(u) ∈ W [[u]] and fn(0) ∈ W .
Lemma 2.4. In the situation above we have vp(ak) ≥ − vp(k!), where vp is the
p-adic valuation and ak is the k-th coeﬃcient in the power series expansion with
respect to u of any of the functions fn.
Proof. Let ak(h) be the k-th coeﬃcient of h for any power series h. We have
vp(ak(fng)) ≥ min
l≤ k
[vp(al(fn))] .
