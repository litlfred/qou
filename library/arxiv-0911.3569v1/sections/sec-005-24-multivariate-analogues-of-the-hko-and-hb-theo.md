---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-005-24-multivariate-analogues-of-the-hko-and-hb-theo
section_title: "Multivariate analogues of the HKO and HB Theorems."
section_number: 2.4
pages: 6-8
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
with the univariate HB Theorem, polynomials f,g ∈ R[x] are said to be in proper
position, denoted by f≪g, when g + if∈ S[x]. (As will be seen, this implies that
f,g ∈ SR[x].) Thus, the multivariate analogue of Hermite-Biehler is a deﬁnition ,
not a theorem.
Proposition 2.7 (Lemma 1.8 and Remark 1.3 of [5]) . Letf,g ∈ C[x].
(a) If f,g ∈ R[x] then f≪g if and only if g +yf∈ SR[x,y ].
(b) If 0⁄≡f∈ S[x] then g +yf∈ S[x,y ] if and only if for all z∈ Hm,
Im
(g(z)
f(z)
)
≥ 0.
Proof. If g +yf ∈ SR[x,y ] then g + if ∈ S[x], by specialization. Conversely,
assume that h = g + if∈ S[x] with f,g ∈ R[x], and let z = a + ib with a,b ∈ R
and b> 0. By Lemma 2.3, for all a, b∈ Rm with b> 0 we haveh(a + bt)∈ S[t].
By HB, ˆf(t) = f(a + bt) and ˆg(t) = g(a + bt) are such that ˆf ≪ ˆg. By HKO,
cˆf +dˆg∈ SR[t] for all c,d∈ R. By HKO again, the roots of bˆf and of ˆg +aˆf are
interlaced. Since W [bˆf,ˆg +aˆf] = bW [ˆf,ˆg]≤ 0 on R, it follows that bˆf≪ˆg +aˆf.
Finally, by HB again, ˆg + (a + ib)ˆf∈ S[t]. Since this holds for all a, b∈ Rm with
b> 0, Lemma 2.3 implies that g +(a+ib)f∈ S[x]. Since this holds for all a,b∈ R
with b> 0, g +yf∈ S[x,y ]. This proves part (a).
For part (b), ﬁrst letg +yf be stable. By specialization, g is also stable. If g≡ 0
then there is nothing to prove. Otherwise, consider any z∈ Hm, so that f(z)⁄= 0
and g(z)⁄= 0. There is a unique solution z∈ C to g(z) +zf (z) = 0, and since
g +yf is stable, Im(z)≤ 0. Hence, Im( g(z)/f(z)) = Im(−z)≥ 0. This argument
can be reversed to prove the converse implication. □
Exercise 2.8 (Corollary 2.4 of [4]) . S[x] ={g + if : f,g ∈ SR[x] and f≪g}.
Here is the multivariate HKO Theorem of Borcea and Br¨ and´ en.
Theorem 2.9 (Theorem 1.6 of [4]). Letf,g ∈ R[x]. Then af +bg∈ SR[x] for all
a,b∈ R if and only if f,g ∈ SR[x] and either f≪g or g≪f.
Proof. First assume that f ≪ g, and let a,b ∈ R with b > 0. By Proposition
2.7(a), g +yf∈ SR[x,y ]. By scaling and specialization, bg + (a + i)f∈ S[x]. By
Proposition 2.7(a) again, f≪ (af +bg). Thus af +bg∈ SR[x] for all a,b ∈ R.
The case that g≪f is similar.
Conversely, assume that af +bg∈ SR[x] for all a,b ∈ R. Let a, b∈ Rm with
b> 0, and let ˆf(t) =f(a+bt) andˆg(t) =g(a+bt). By Lemma 2.3, aˆf +bˆg∈ SR[t]
for all a,b∈ R. By HKO, for each a, b∈ Rm with b> 0, either ˆf≪ˆg orˆg≪ ˆf.
If ˆf≪ˆg for all a, b∈ Rm with b> 0, then by HB,ˆg+iˆf∈ S[t] for all a, b∈ Rm
with b > 0. Thus g + if∈ S[x] by Lemma 2.3, which is to say that f≪ g (by
deﬁnition). Similarly, if ˆg≪ ˆf for all a, b∈ Rm with b> 0 then g≪f.
It remains to consider the case that f(a0 + b0t)≪g(a0 + b0t) for some a0, b0∈
Rm with b0 > 0, and g(a1 + b1t)≪ f(a1 + b1t) for another a1, b1∈ Rm with
b1 > 0. For 0≤λ≤ 1, let aλ = (1−λ)a0 +λa1 and bλ = (1−λ)b0 +λb1. Since
roots of polynomials move continuously as the coeﬃcients are varied continuously,
there is a value 0 ≤λ≤ 1 for which both f(aλ + bλt)≪g(aλ + bλt) and g(aλ +
bλt)≪f(aλ +bλt). From Exercise 2.6, it follows that cf(aλ +bλt) =dg(aλ +bλt)
MULTIVARIATE STABLE POLYNOMIALS 7
for some c,d∈ R not both zero. Now h =cf−dg∈ S[x] by hypothesis, and since
h(aλ + bλt)≡ 0 identically, it follows that h(aλ + ibλ) = 0. Since bλ > 0 and h is
stable, this implies that h≡ 0, so that cf =dg in S[x]. In this case, both f≪g
and g≪f hold. □
Forf,g ∈ C[x] and i∈ [m], let Wi[f,g ] =∂if·g−f·∂ig be the i-th Wronskian
of the pair (f,g ).
Corollary 2.10 (Theorem 1.9 of [5]). Letf,g ∈ R[x]. The following are equivalent:
(a) g + if is stable in S[x], that is f≪g;
(b) g +yf is real stable in SR[x,y ];
(c)af +bg∈ SR[x] for all a,b∈ R, and Wi[f,g ](a)≤ 0 for all i∈ [m] and a∈ Rm.
Proof. Proposition 2.7(a) shows that (a) and (b) are equivalent.
If (a) holds then Theorem 2.9 implies that af +bg∈ SR[x] for all a,b∈ R. To
prove the rest of (c), let i∈ [m] and a∈ Rm, and let δi∈ Rm be the unit vector
with a one in the i-th position. Since f≪g, for any b∈ Rm with b> 0 we have
f(a + (b +δi)t)≪g(a + (b +δi)t) in SR[t], from Proposition 2.7(a) and Lemma
2.3. By the Wronskian condition for univariate polynomials in proper position,
W[f(a + (b +δi)t),g (a + (b +δi)t)]≤ 0
for all t∈ R. Taking the limit as b→ 0 and evaluating at t = 0 yields
Wi[f,g ](a) = W[f(a +δit),g (a +δit)]|t=0≤ 0,
by continuity. Thus (a) implies (c).
To prove that (c) implies (b), let a, b∈ Rm with b = (b1,...,b m) > 0, and let
a,b ∈ R with b >0. By Lemma 2.3, to show that g +yf∈ SR[x,y ] it suﬃces to
show that g(a + bt) + (a + ib)f(a + bt)∈ S[t]. From (c) it follows that p =g +af
andq =bf are such that αp +βq∈ SR[x] for all α,β ∈ R. By Theorem 2.9, either
p≪q or q≪p. Now
W[q(a + bt),p (a + bt)] = bW[f(a + bt),g (a + bt)]
= b
m∑
i=1
biWi[f,g ](a + bt)≤ 0,
by the Wronskian condition in part (c). Thus q(a + bt)≪ p(a + bt), so that
p(a+bt)+iq(a+bt)∈ S[t]. Since p+iq =g +(a+ib)f, this shows that (c) implies
(b). □
Exercise 2.11 (Corollary 1.10 of [5]). Letf,g ∈ SR[x] be real stable. Then f≪g
and g≪f if and only if cf =dg for some c,d∈ R not both zero.
Proposition 2.12 (Lemma 3.2 of [5]). LetV be a K-vector subspace of K[x], with
either K = R or K = C.
(a) If K = R and V ⊆ SR[x] then dimRV ≤ 2.
(b) If K = C and V ⊆ S[x] then dimCV ≤ 1.
Proof. For part (a), suppose to the contrary that f,g,h ∈V are linearly indepen-
dent over R (and hence not identically zero). By Theorem 2.9, either f ≪ g or
g≪f, and similarly for the other pairs {f,h} and{g,h}. Renaming these polyno-
mials as necessary, we may assume thatf≪h andh≪g. Now, for all λ∈ [0, 1] let
pλ = (1−λ)f +λg, and note that each pλ⁄≡ 0. By Theorem 2.9, for each λ∈ [0, 1]
either h≪ pλ or pλ≪ h. Since p0 = f≪ h and h≪ g = p1, by continuity of
8 DAVID G. WAGNER
the roots of {pλ : λ∈ [0, 1]} there is a λ∈ [0, 1] such that h≪ pλ and pλ≪ h.
But then, by Exercise 2.11, either {f,g} is linearly dependent or h is in the span
of{f,g}, contradicting the supposition.
For part (b), let Re(V ) ={Re(h) : h∈ V}. Then Re( V ) is a real subspace of
SR[x], so that dim R Re(V )≤ 2 by part (a). If dim R Re(V )≤ 1 then dim CV ≤ 1.
In the remaining case let {p,q} be a basis of Re( V ) with f = p + iq∈ V . By
Corollary 2.10, Wi[q,p ](a)≤ 0 for all i∈ [m] and a∈ Rm. Since p and q are not
linearly dependent, there is an index k∈ [m] such that Wk[q,p ]⁄≡ 0.
Consider any g∈V . There are reals a,b,c,d ∈ R such that
g = (ap +bq) + i(cp +dq).
Sinceg is stable, Wk[cp +dq,ap +bq](a) = (ad−bc)Wk[q,p ](a)≤ 0 for all a∈ Rm.
Since Wk[q,p ]⁄≡ 0, it follows that ad−bc≥ 0. Now, for any v,w ∈ R,g + (v + iw)f
is in V . Since
g + (v + iw)f = (a +v)p + (b−w)q + i((c +w)p + (d +v)q),
this argument shows that H = (a +v)(d +v)− (b−w)(c +w)≥ 0 for all v,w ∈ R.
But
4H = (2v +a +d)2 + (2w +c−b)2− (a−d)2− (b +c)2,
so that H≥ 0 for all v,w ∈ R if and only if a =d and b =−c. This implies that
g = (a + ic)f, so that dim CV = 1. □
