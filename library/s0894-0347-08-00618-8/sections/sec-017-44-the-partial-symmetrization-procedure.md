---
doc_id: s0894-0347-08-00618-8
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8"
section_id: sec-017-44-the-partial-symmetrization-procedure
section_title: "The partial symmetrization procedure"
section_number: 4.4
pages: 29-31
source_pdf: S0894-0347-08-00618-8.pdf
source_sha256: 7c0b2ca41992b21c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8 — 24 sections: Front matter; Introduction; A plethora of negative dependence"
---
symmetrization of (complex) measures on 2[n] deﬁned in (3), and Deﬁnition 2.9.
The main result of this section is the following theorem.
Theorem 4.20. Let µ be a complex measure on 2[n] with a (complex) stable gener-
ating polynomial. Then for any transposition τ ∈Sn and θ ∈[0, 1] the generating
polynomial of the partial symmetrization µτ,θ = θµ+(1−θ)τ(µ) is (complex) stable.
In particular, Theorem 4.20 implies that the class of strongly Rayleigh measures
on 2[n] is invariant under the partial symmetrization procedure. Clearly, the latter
result is real stable in nature. However, in order to establish it we have to consider
the (wider) complex stable context (cf. Deﬁnition 2.9), as in the above theorem.
For the proof of Theorem 4.20 we need a multivariate generalization of the clas-
sical Obreschkoﬀtheorem that was obtained in [9].
Theorem 4.21 (Multivariate Obreschkoﬀtheorem). Let f, g ∈R[z1, . . . zn]. Then
all non-zero polynomials in the space {αf + βg : α, β ∈R} are stable if and only if
either f + ig or f −ig is stable or f = g ≡0.
550
J. BORCEA, P. BR¨AND´EN, AND T. M. LIGGETT
Remark 4.4. There are now elementary proofs of Theorem 4.20 that avoid the mul-
tivariate Obresckoﬀtheorem; see [10, 56]. Also, the referee sketched an elementary
proof similar to those given in [10, 56].
Proof of Theorem 4.20. Let f ∈C[z1, . . . , zn] be the generating polynomial of µ.
Hence f is stable and multi-aﬃne. Assuming, as we may, that i = 1 and j = 2, we
need to prove that
θf(ξ1, ξ2, . . . , ξn) + (1 −θ)f(ξ2, ξ1, . . . , ξn)̸ = 0
whenever ξ1, . . . , ξn ∈{z : Im(z) > 0} (cf. Deﬁnition 2.9). By ﬁxing ξ3, . . . , ξn
arbitrarily in the open upper half-plane and considering the multi-aﬃne polynomial
in variables z1, z2 given by
(z1, z2) 
→g(z1, z2) := f(z1, z2, ξ3, . . . , ξn),
we see that the problem reduces to proving that the linear operator Tθ on multi-
aﬃne polynomials in two variables deﬁned by
Tθ(h)(z1, z2) = θh(z1, z2) + (1 −θ)h(z2, z1)
preserves stability. Let us ﬁrst show that Tθ preserves real stability. For this let
f(z1, z2) = a00 + a01z2 + a10z1 + a11z1z2 ∈R[z1, z2] \ {0}
be real stable and set Df = a00a11 −a01a10. By Theorem 4.1 we know that f is
real stable if and only if Df ≤0. Since
DTθ(f) = Df −θ(1 −θ)(a01 −a10)2 ≤Df,
it follows that Tθ(f) is also real stable, as required. To deal with the (non-real)
stable case ﬁrst let h = g + if ∈C[z1, z2] be strictly stable and multi-aﬃne. This
means that h(z1, z2)̸ = 0 whenever Im(z1) ≥0 and Im(z2) ≥0. By the multivariate
Obreschkoﬀtheorem we have that αg + βf is real stable or zero for all α, β ∈R.
Hence, by the above, we also have that αTθ(f)+βTθ(g) is real stable or zero for all
α, β ∈R. By the multivariate Obreschkoﬀtheorem again this gives that Tθ(g + if)
or Tθ(g −if) is stable. However, one has
Tθ(h)(z, z) = h(z, z) = g(z, z) + if(z, z),
which is strictly stable by assumption. If Tθ(g −if) is stable, then g(z, z)−if(z, z)
is stable and g(z, z) + if(z, z) is strictly stable, which is impossible since it would
imply that all zeros of (the strictly stable polynomial) g(z, z) + if(z, z) were real.
Hence Tθ(g + if) is stable.
Now if ϵ > 0 and p ∈C[z1, z2] is stable, then clearly p(z1 + iϵ, z2 + iϵ) is strictly
stable (in the sense deﬁned above), and thus any stable polynomial is the uniform
limit on compact sets of strictly stable polynomials. By the multivariate version of
Hurwitz’ classical theorem on the “continuity of zeros” (see, e.g., [8, Theorem 2.3]
and [19, Footnote 3, p. 96]) this proves that Tθ preserves stability.
□
Remark 4.5. From Theorem 4.20 it follows that the symmetrization µs of a strongly
Rayleigh measure µ is also strongly Rayleigh. A diﬀerent proof is as follows. If µ is a
strongly Rayleigh measure on 2[n], then (2) implies that the diagonal specialization
∆(gµs)(t) = ∆(gµ)(t) (cf. Deﬁnition 2.8) is a real-rooted univariate polynomial and
by the Grace-Walsh-Szeg¨o theorem we conclude that the symmetrization µs of µ is
also strongly Rayleigh.
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS
551
