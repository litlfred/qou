---
doc_id: aif-2009-59-1-347-0
doc_title: "On q-summation and confluence"
section_id: sec-024-44-the-functional-space-h-in-the-borel-plane
section_title: "The functional space H in the Borel plane"
section_number: 4.4
pages: 42-45
source_pdf: AIF_2009__59_1_347_0.pdf
source_sha256: 35b8422990e24888
toc_source: outline
doc_brief: "On q-summation and confluence — 28 sections: Front matter; Introduction; Part 1. Convergent q-Borel and q-L"
---
We recall that the q-Borel transform Bq associates to a power series ˆf =
P
n⩾0 anxn+1 ∈C[[x]] the power series φ = P
n⩾0 anq−n(n−1)/2ξn ∈C[[ξ]].
As we have already pointed out, the q-Borel transform of a generic q-Gevrey
series admits a positif radius of convergence and can be continued to an
analytic function in the whole complex plane minus a ﬁnite number of sets
of the form λqN (cf. [20] and [23]).
In this section we want to prove that every generic q-Gevrey series can be
expressed by means of “modiﬁed Tschakaloﬀseries”. Our strategy consists
in proving that the q-Borel transform of any generic q-Gevrey series ad-
mits an elementary decomposition, by studying the q-convolution product
of suitable entire functions by a rational functions. This leads to the con-
struction of a functional space which is somehow spanned by the q-Borel
transforms of the modiﬁed Tschakaloﬀseries.
Definition 4.17. — We call q-convolution product the following bilin-
ear operator:
∗q :
C{ξ} × C{ξ}
−→
ξC{ξ}
ξn ∗q ξm
7−→
q−(nm+n+m+1)ξn+m+1 .
A direct calculation shows that
1. If φ = P
n⩾0 φnξn ∈C{ξ} and ψ ∈C{ξ}, then ([12, 1.4.3, where s = 1)])
φ ∗q ψ(ξ) =
X
⩾0
φ0q−n−1ξn+1ψ(q−n−1ξ).
TOME 59 (2009), FASCICULE 1
388
Lucia DI VIZIO & Changgui ZHANG
2. Bq( ˆfˆg) = Bq( ˆf) ∗q Bq(ˆg).
Let K be the set of rational functions bounded at zero and let Eq be
the set of all entire functions admitting at most a q-exponential growth of
order 1 at the inﬁnity. We know that K ∩Eq = C[ξ] and Eq = Bq(xC{x})
(cf. [Ram92]). Notice that the formula Bq( ˆfˆg) = Bq( ˆf) ∗q Bq(ˆg) identiﬁes
(Eq, ∗q) to a commutatif sub-ring of (C{ξ}, ∗q).
Definition 4.18. — We deﬁne the functional space H := ∪n⩾0Hn in
the following way:
H−1 = {1},
H0 = K,
H1 = Eq ∗q K := {φ ∗q r : φ ∈Eq, r ∈K}
and, for any integer n ⩾1,
H2n = KH2n−1 := {ru : r ∈K, u ∈H2n−1},
H2n+1 = Eq ∗q H2n := {φ ∗q u : φ ∈Eq, u ∈H2n}.
Proposition 4.19. — For any (r, φ, u) ∈K ×Eq ×H, we have (ru, φ∗q
u) ∈H × H. In other words, the functional space H is a (K, Eq)-bimodule.
Proof. — It follows immediately from the deﬁnition of H. Indeed, if n ⩽
m, then Hn ⊂Hm. So, we can suppose that (r, φ, u) ∈K × Eq × Hn and
hence, (ru, φ ∗q u) ∈Hn+2 × Hn+2 ⊂H × H.
□
Theorem 4.20. — For any u ∈H, there exist φ0, φ1, . . . , φn ∈Eq and
r0, r1, . . . , rn ∈K such that
u = φ0 + r0 + φ1 ∗q r1 + ... + φn ∗q rn.
Moreover, we can suppose that r1, ..., rn are rational functions of the form
1
(ξ−λi)νi , where ci, λi ∈C∗and νi ∈N.
Proof. — Since Hm ⊂Hm+1, for any u ∈H there exists m ∈N such
that u ∈Hm. So we can prove the theorem by induction on m. The cases
m = 0 and m = 1 are trivial. Suppose that u ∈Hm+1. Then there exists
(r, v, φ) ∈K × Hm × Eq such that on of the following two cases occurs:
(1) u = rv,
(2) u = φ ∗v,
and, by inductional hypothesis, v = φ0 + r0 + Pm
j=1 φj ∗q rj. The proof in
the case (2) is straightforward, since φ ∗q (φj ∗q rj) = (φ ∗q φj) ∗q rj. In the
case (1), we need the following elementary lemma.
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE
389
Lemma 4.21. — For any (a, b, ℓ, n) ∈C∗× C∗× N × N such that a̸ = b,
the following decomposition holds:
1
(x −a)ℓ
1
(x −b)n =
ℓ−1
X
k=0
(n + k)!
(a −b)n+kk!
(−1)k
(x −a)ℓ−k
+
n−1
X
k=0
(ℓ+ k)!
(b −a)ℓ+kk!
(−1)k
(x −b)n−k .
Proof. — It enough to take the (ℓ−1)-th derivative with respect to a
and the n −1-th derivative with respect to b in the formula
1
x −a
1
x −b =
1
a −b

1
x −a −
1
x −b

.
□
Let us go back to the proof of the Theorem 4.20. By linearity, it enough
to consider a product of the form r(φ ∗q r′), with r =
1
(ξ−λ)ℓ, r′ =
1
(ξ−µ)n)
and φ = P
k⩾0 φkξk ∈Eq. Since
r′ ∗q φ(ξ) =
X
k⩾0
φkq−k−1
ξk+1
(q−k−1ξ −µ)n ,
the decomposition follows from the lemma above.
□
Corollary 4.22. — For any u ∈H, there exist λ1, . . . , λn ∈C∗such
that u is analytic on the domain C\(∪m
i=1λiqN) and the function U deﬁned
by
U(ξ) = u(ξ)
n
Y
i=1
Y
m⩾0

1 −
ξ
λiqm

can be continued to an entire function that has at most a q-exponential
growth of order n + 1 at the inﬁnity.
The corollary results from the combination of the theorem above and the
following lemma:
Lemma 4.23. — Let φ ∈Eq, r =
1
(ξ−λ)n , n ⩾1 and λ ∈C∗. Then φ∗q r
admits λqN as set of poles and there exist C > 0, m > 0 such that, for any
ϵ > 0,
|ξq−n −λ| > ϵ
=⇒
|φ ∗q r(ξ)| < C
ϵn |ξ|m|e
(log x)2
2 ln q |.
Proof. — Let φ = P
k⩾0 φnξk. Since φ ∈Eq, there exist A, B > 0 such
that
∀k ∈N,
|φk| < ABnq−n(n+1)/2.
TOME 59 (2009), FASCICULE 1
390
Lucia DI VIZIO & Changgui ZHANG
On the other hand,
φ ∗q r =
X
k⩾0
φkq−k−1ξk+1r(q−k−1ξ),
which implies directly the lemma.
□
