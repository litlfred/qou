---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-043-141-the-connes-unitary-cocycle-radon-nikodym-the
section_title: "The Connes unitary cocycle Radon-Nikodym theorem."
section_number: 14.1
pages: 105-109
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
theorem.
This result will allow us to extract information from the modular group of a
state which is independent of the state.
Theorem 14.1.1. Let φ and ψ be faithful normal states on a von Neumann
algebra M. Then there is a strongly continous map t →ut from R to the
unitary group of M so that
σφ
t = Adutσψ
t
∀t ∈R.
Morevoer ut satisﬁes the cocycle condition utσψ
t (us) = ut+s.
Proof. We deﬁne the faithful normal state Φ on M ⊗M2(C) by Φ((x)ij) =
1
2(φ(x11) + ψ(x22)). The projection p = ( 1 0
0 0 ) is ﬁxed by σΦ by 13.4.4. So σΦ
deﬁnes a one parameter automorphism group of pM ⊗M2(C)p which satisﬁes
the KMS condition for φ.
Hence σΦ
t (x ⊗e11) = σφ
t (x) ⊗e11.
Similarly
σΦ
t (x ⊗e22) = σψ
t (x) ⊗e22.
Let Vt = σΦ
t (1 ⊗e21).
Then VtV ∗
t
= ( 0 0
0 1 )
and V ∗
t Vt = ( 1 0
0 0 ). Hence Vt = ( 0 0
vt 0 ) for some unitary vt ∈M. Routine
computations give the rest.
Corollary 14.1.2. If M is a factor and σφ
t is outer for any φ and t then M
is of type III.
Proof. By the previous result it suﬃces to exhibit a single faithful normal
state on a type II factor with inner modular group. In the II1 case use the
trace and in the II∞case choose a faithful normal state φ on B(H) and use
tr⊗φ, using the KMS condition (if necessary) to very that the modular group
for the tensor product is the tensor product of the modular groups.
105
Corollary 14.1.3. The subgroup of all t ∈R for which σφ
t is inner is inde-
pendent of the faithful normal state φ.
Deﬁnition 14.1.4. The subgroup of the previous corollary, which is an in-
variant of M, is called T(M).
We shall now calculate T(M) for the Powers factor Rλ where this refers
to the ITPFI factor with all nk = 2 and all states having the same density
matrix h =

1
1+λ
0
0
λ
1+λ

.
Theorem 14.1.5.
T(Rλ) =
2π
log λZ
.
Proof. By the formula for the modular group σφ
2π
log λ = id so
2π
log λZ ⊆T(Rλ).
For the other direction it suﬃces to show that an automorphism α of the
form
α = ⊗∞
k=1Adu
is outer whenever the unitary u is not a scalar.
For this ﬁrst deﬁne uk = ⊗k
1u and observe that if α = Adv then (uk ⊗
1)−1v = id on the matrix algebra Ak = ⊗k
1M2(C). By exercise 4.3.3 this
means that v = uk ⊗w. Now it is clear from our basis that we can choose
⊗p
j=1xi ⊗1Ωwith non-zero inner procuct with vΩ. But then ﬁxing p and
letting k tend to inﬁnity we see that
⟨(⊗p
j=1xi ⊗1)Ω, vΩ⟩=
p
Y
j=1
⟨xi, u⟩⟨1, u⟩k−p⟨1, w⟩.
The left hand side does not depend on k and |⟨1, w⟩| ≤1 so we must have
|⟨1, u⟩| = 1 which means that u is a scalar multiple of 1 by the Cauchy-
Schwarz inequality.
We conclude that the Powers factors Rλ are type III factors, mutually
non-isomorphic for diﬀerent values of λ.
14.2
Type IIIλ.
The spectrum of the modular operator ∆is easy to calculate for an ITPFI
factor. It is simply the closure of the set of all ratios
µi
µj as µ varies over
all the density matrices deﬁning the product state. Apart from being closed
106
under the inverse operation this set of non-negative real numbers has no
particular structure and can be altered easily by making changes in ﬁnitely
many density matrices which of course do not change the factor.
Deﬁnition 14.2.1. If M is a von Neumann algebra the invariant S(M)
is the intersection over all faithful normal states φ of the spectra of their
corresponding modular operators ∆φ.
Theorem 14.2.2. A factor M is of type III iﬀ0 ∈S(M).
Theorem 14.2.3. (Connes-van Daele) S(M) \ {0} is a closed subgroup of
the positive real numbers.
There are only three kinds of closed subgroups of R+.
Deﬁnition 14.2.4. A factor M is called type IIIλ for 0 ≤λ ≤1 if
λ = 0
:
S(M) = {0} ∪{1}
0 < λ < 1
:
S(M) = {0} ∪{λn : n ∈Z}
λ = 1
:
S(M) = {0} ∪R+
Theorem 14.2.5. The Powers factor Rλ is of type IIIλ.
In his thesis, Connes showed that every type IIIλ factor for 0 < λ < 1 is
Connes thesis
canonically isomorphic to the crossed product of a type II∞factor with an
action of Z whose generator scales the trace by λ.
If A is a locally compact abelian group with an action α on a von Neumann
algebra M, there is an action ˆα of the Pontryagin dual ˆA on the crossed
product M ⋊α A satisfying
ˆαa(x)
=
x
for x ∈M
ˆαˆa(ua)
=
ˆa(a)ua
if ua are the unitaries deﬁning the crossed product.
The existence of the so-called “dual action” ˆα is trivial proved since it is
implemented by the obvious unitary representation of ˆA on L2(A).
Exercise 14.2.6. If A is ﬁnite consider the projection p = P
a ua ∈M ⋊A.
Show that pM ⋊Ap = M Ap and thus show that (M ⋊α A)⋊ˆα ˆA is isomorphic
to M ⊗M|A|(C).
107
Observe that the crossed product of a von Neumann algebra M on H by
the modular group σφ does not depend, up to isomorphism, on the faithful
normal state φ. This follows from theorem 14.1.1 by deﬁning the unitary V
on L2(R, H) by
V f(t) = utf(t)
where ψ is another faithful normal state with unitary one-cocycle ut. Conju-
gating the operators that generate M⋊σφR by V one obtains the generators
of M ⋊σψ R.
Theorem 14.2.7. The crossed product of M by the modular group admits a
trace satisfying the properties of 9.1.9
Deﬁnition 14.2.8. The action of ˆR on Z(M ⋊σφ R) is called the “ﬂow of
weights” of M.
Theorem 14.2.9. (Takesaki duality) The crossed product
(M ⋊σφ R) ⋊c
σφ ˆR
is isomorphic to the tensor product M ⊗B(H) for H = L2(R).
Thus if M is a factor the ﬂow of weights is ergodic.
Theorem 14.2.10. If M is a factor of type IIIλ the ﬂow of weights is
III1:
The trivial ﬂow on a one point set if M is III1.
IIIλ:
The transitive ﬂow on the circle with period 2π
λ if M is of type IIIλ,
0 < λ < 1.
III0:
Ergodic non-transitive if M is of type III0.
Moreover any ergodic non-transitive ﬂow arises as the ﬂow of weights for
some type III0 factor.
108
Chapter 15
Hyperﬁniteness
Deﬁnition 15.0.11. A von Neumann algebra M on a separable Hilbert space
is called hyperﬁnite if there is an increasing sequence An of ﬁnite dimensional
*-subalgebras of M which generates M as a von Neumann algebra.
