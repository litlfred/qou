---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-044-52-positive-links-37
section_title: "Positive links 37"
section_number: 5.2
pages: 37-38
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Lemma 5.9 If
D = D[n] = ˆ (σk1
1 σk2
2 . . .σkn
1 δ2)
with n ≥ 1 odd, k1,kn ≥ 1 and ki ≥ 2 when i = 2, . . . ,n − 1, then mindega Λ(D) = −1. Writing k = (k1, . . . ,kn) and
˜w(k) = ( k1 − 1) +
n
∑
l=2
(kl − 2) ,
we have maxdegz[Λ(D)]a−1 = ˜w(k).
Proof. If n = 1 we check directly (we have a reduced diagram of the (2,k1)-torus link), so let n ≥ 3.
Consider ﬁrst three special forms of k.
If k = (12∗1) (with 2∗ being a sequence of ‘2’), thenD is regularly isotopic to a trivial 2-component link diagram . If
k = (12∗) or (2∗1), then D is regularly isotopic to an unknot diagram with one positive kink. In both situations the
claims follow directly.
Now let k = (2∗). We orient D so as to become negative. Then D depicts the (2,−n − 1)-torus link. We can evaluateΛ
on L from F(L) by normalization. For its mirror image !L, we can use theorem 5.4 to conclude that mindega F(!L) = n.
Now it is also known that spana F(!L) = c(!L), and c(!L) = n + 1, so
maxdeg a F(!L) = mindeg a F(!L) +spana F(!L) = n + (n + 1) = 2n + 1 .
Thus mindeg a F(L) = −1 − 2n, and since w(D) = −2n, we have
mindeg a Λ(D) = −w(D) +mindega F(D) = −(−2n) − 1 − 2n = −1 .
That maxdeg z[Λ(D)]a−1 = 1 can also be obtained by direct calculation.
If k is not of these special types, then kl ≥ 3 for some 1 ≤ l ≤ n. We resolve a positive crossing in σkl
j . We have (with
D = D+)
Λ(D+) = zΛ(D0) + zΛ(D∞ ) − Λ(D−) .(40)
Here D0 has ˜w by one less and comes with az-factor, so it is enough to show thatΛ(D−) and Λ(D∞ ) do not contribute.
If kl > 3, then D− is of the required form and has ˜w by two less, so by induction Λ(D−) has too small z-degree in
[Λ]a−1.
Now consider kl = 3. As in the proof of lemma 5.2 of [St4] we can move by braid rela tions (regular isotopy) a σ1 in
σ1σ2σ1 until we get a σiσ−1
i (and then cancel). Here we replaced σ−1
i by δi, so that such σi right before a δi becomes
a kink, which is negative. By repeating this transformation , we obtain a form that has no σiσi±1σi (i.e. ki > 1 for
1 < i < n) and a certain non-zero number of negative kinks collected at both ends. The negative kinks shift the degree
in a of Λ up, so by induction D− has no contribution to [Λ]a−1.
It remains to deal with the term of D∞ in (40). It is the connected sum D[n1]#D[n2] with n1 + n2 = n − 1, and with
kl − 1 > 1 negative kinks. So by induction mindeg a Λ(D∞ ) = kl − 1 + (−1) + (−1) > −1, and Λ(D∞ ) gives no
contribution to [Λ(D+)]a−1. ✷
Theorem 5.5 If a 3-braid link is positive, then it is the closure of a posit ive or almost positive 3-braid. Along these
links the non-ﬁbered ones are exactly the (1,p,q,r)-pretzel links.
Proof. Consider the ﬁrst claim. Since L is positive, it is strongly quasi-positive, and so has a posi tive 3-braid band
representation β by theorem 1.1. So β is of Xu’s formR or (21)kR (with k > 0) up to extensions. If β contains σ1σ2σ1
or σ2σ1σ2 we can reduce it as before, until (a) it becomes positive, or (b) it still has a positive band representation, but
it does not contain σ1σ2σ1 or σ2σ1σ2. In case (a) we are done. In case (b) we observe that β is of the form (39), apply
lemma 5.8, and conclude that l ≤ 1.
It remains to argue which links are not ﬁbered. Positive brai ds are always ﬁbered, and by direct observation for an
almost positive braid we have Xu’s form R or (21)kR depending on whether in (39) (with l = 1) we have n1 = 3 or
n1 > 3. We proved in theorem 3.2 that the forms (21)kR (for k > 0) give ﬁbered closure links. For n1 = 3 we have as
before the (1,p,q,r)-pretzel links. ✷
