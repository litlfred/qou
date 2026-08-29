---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-030-75-the-characterization-of-bi-negligible-amplitu
section_title: "The characterization of bi-negligible amplitudes. We need to ﬁnd the bianalytic ana-"
section_number: 7.5
pages: 23-25
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
logue of Proposition 6.2, so that we can tell when we have a bi-negligible amplitude. To
formulate the criterion, we ﬁrst need to deﬁne the operator N. We note that a function f ∈R2
has a unique decomposition f(z, w) = f1(z, w) + ¯zf2(z, w), where f1 and f2 are holomorphic in in
z and C∞-smooth in w (near the diagonal z = w). For such f ∈R2, we put
N[f](z, w) := f1(z, w) −f1(w, w)
z −w
+ ¯z f2(z, w) −f2(w, w)
z −w
.
Then NMz−w is the identity operator. Second, we need the (formal) operator S′ given by
(7.5.1)
S′ := SM−1
¯∂wθS−1NS.
Proposition 7.2. Fix an integer k = 1, 2, 3, . . .. Suppose a has an asymptotic expansion a ∼m2a0 +
ma1 + a2 + m−1a3 + . . ., where the functions aj ∈R2 are all independent of m. Then the following are
equivalent:
(i) There exist two ﬁnite asymptotic expansions α = m2α0 + mα1 + α2 + · · · + m−k+1αk+1 and α′ =
m2α′
0+mα′
1+α′
2+· · ·+m−k+1α′
k+1, where each αj, α′
j ∈R2 is independent of m, such that [Sa]⟨k⟩= Mz−wα
and [S′a]⟨k⟩= Mz−wα′(z, w).
(ii) There exists an asymptotic expansion A ∼A0 + m−1A1 + m−2A2 + . . ., with Aj ∈R2 independent
of m, such that
a⟨k⟩= [∇M ¯∂wθ∇A]⟨k⟩.
Proof. We ﬁrst show the implication (i) ⇒(ii). We recall the abschnitt properties (6.5.5) and
(6.5.6), which will be used repeatedly. We put β := [S−1α]⟨k⟩, to obtain
(7.5.2)
[Sa]⟨k⟩= Mz−wα = [Mz−wSβ]⟨k⟩,
and, consequently, by (6.5.8), we have
(7.5.3)
a⟨k⟩= [S−1Mz−wSβ]⟨k⟩= [(2m)−1∇β]⟨k⟩.
Moreover, we see from (7.5.2) and the deﬁnition (7.5.1) of S′ that
(7.5.4)
[S′a]⟨k⟩= [SM−1
¯∂wθS−1NSa]⟨k⟩= [SM−1
¯∂wθS−1NMz−wSβ]⟨k⟩= [SM−1
¯∂wθβ]⟨k⟩,
where we used that NMz−w is the identity. Next, we put β′ := [S−1α′]⟨k⟩, so that α′ = [Sβ′]⟨k⟩, so
that in view of the second condition in (i) and (7.5.4), we get that
Mz−w[Sβ′]⟨k⟩= Mz−wα′ = [S′a]⟨k⟩= [SM−1
¯∂wθβ]⟨k⟩.
We solve for β, using (6.5.8):
(7.5.5)
β = [M ¯∂wθS−1Mz−wSβ′]⟨k⟩= [(2m)−1M ¯∂wθ∇β′]⟨k⟩.
By putting the relations (7.5.3) and (7.5.5) together, we now see that
a⟨k⟩= [(2m)−2∇M ¯∂wθ∇β′]⟨k⟩,
which means that (ii) holds with A⟨k+2⟩= (2m)−2β′.
24
ANTTI HAIMI AND HAAKAN HEDENMALM
Finally, we turn to the reverse implication (ii) ⇒(i). This time we have A, and just need
to ﬁnd α and α′ with the given properties. Inspired by the calculations we carried out for the
forward implication, we put α′ := [(2m)2SA]⟨k⟩and α := [2mSM ¯∂wθ∇A]⟨k⟩. It remains to verify
that (i) holds with these choices α and α′. We ﬁrst check with the help of (6.5.8) and (ii) that
Mz−wα = [2mMz−wSM ¯∂wθ∇A]⟨k⟩= [S∇M ¯∂wθ∇A]⟨k⟩= [Sa]⟨k⟩,
so the ﬁrst relation in (i) holds. Second, we check using (ii), (7.5.1), and (6.5.8), that
[S′a]⟨k⟩= [S′∇M ¯∂wθ∇A]⟨k⟩= [SM−1
¯∂wθS−1NS∇M ¯∂wθ∇A]⟨k⟩
= [2mSM−1
¯∂wθS−1NMz−wSM ¯∂wθ∇A]⟨k⟩= [2mSM−1
¯∂wθM ¯∂wθ∇A]⟨k⟩
= [2mS∇A]⟨k⟩= [(2m)2Mz−wSA]⟨k⟩= Mz−wα′,
and the second relation in (i) holds as well. Note that in the above calculation we used that
NMz−w is the identity. The proof is complete.
□
Remark 7.3. (a) It is clear that a bi-negligible amplitude is automatically a negligible amplitude,
since ∇M−1
¯∂wθ∇A = ∇B, with B := M−1
¯∂wθ∇A. The ﬁrst part of condition (i) of Proposition 7.2
captures this observation. But it is of course harder for amplitude to be bi-negligible than to
be negligible. The second part of condition (i), which involves S′, expresses that diﬀerence.
(b) In the context of the proof of Proposition 7.2, the relation
A⟨k+2⟩= (2m)−2β′ = (2m)−2[S−1α′]⟨k⟩= (2m)−2[S−1NS′a]⟨k⟩
tells us how to obtain A⟨k+2⟩starting from a given a⟨k⟩.
(c) Proposition 7.2 is stated for bi-negligible amplitudes (i.e., where q = 2). However, it is
rather clear how to formulate the corresponding result for general q. In (i), we get q operators
S, . . ., S(q−1) instead of S, S′, and in (ii), we get a product of q copies of the operator ∇interlaced
with q −1 copies of the multiplication operator M ¯∂wθ.
7.6. The local uniqueness criterion for bianalytic kernels. For F(z, w) holomorphic in (z, ¯w)
near the diagonal z = w in C2, it is well-known that the diagonal is a set of uniqueness. In
particular, the assumption F ∈Mz−wR1 implies that F(z, w) ≡0 holds near the diagonal. We
need the analogous criterion for functions biholomorphic in each of the variables (z, ¯w).
Lemma 7.4. Suppose F ∈R2, so that F(z, w) is biholomorphic in z and C∞-smooth in w near the
diagonal z = w. If F(z, w) ∈M2
z−wR2, and in addition, F(z, w) is biholomorphic in ¯w, then F(z, w) ≡0
holds near the diagonal.
Proof. We ﬁrst decompose F = F0 + ¯zF1 + wF2 + ¯zwF3, where each Fj is holomorphic in (z, ¯w)
near the diagonal. Since F is biholomorphic in z, the function ¯∂z∂wF = F3 is holomorphic in
(z, ¯w), and the assumption F ∈M2
z−wR2 leads to ¯∂z∂wF = F3 ∈Mz−wR1. But the diagonal is a set
of uniqueness for F3, and we ﬁnd that F3(z, w) ≡0. So F = F0 + ¯zF1 + wF2, and, consequently,
¯∂zF = F1 ∈M2
z−wR1 is holomorphic in (z, ¯w). Again the diagonal is a set of uniqueness for F1,
which implies that F1(z, w) ≡0. What remains of the decomposition is now F = F0 + wF2. From
F ∈M2
z−wR2 we get that ∂wF = F2 ∈Mz−wR2, and analogously we obtain that F2(z, w) ≡0. The
ﬁnal step, to show that F vanishes if F = F0 ∈M2
z−wR2 is holomorphic in (z, ¯w), is trivial.
□
Remark 7.5. In the context of the lemma, it is not possible to weaken the assumption that
F ∈M2
z−wR2 to just F ∈Mz−wR2, as is clear from the example F(z, w) := z −w.
ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS
25
