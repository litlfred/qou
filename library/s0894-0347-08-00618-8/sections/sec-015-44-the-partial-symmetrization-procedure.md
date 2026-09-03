---
doc_id: s0894-0347-08-00618-8
doc_title: "AMERICAN MATHEMATICAL SOCIETY"
section_id: sec-015-44-the-partial-symmetrization-procedure
section_title: "The partial symmetrization procedure"
section_number: 4.4
pages: 29-33
source_pdf: S0894-0347-08-00618-8.pdf
source_sha256: 7c0b2ca41992b21c
---
symmetrization of (complex) measures on 2 [n] deﬁned in (3), and Deﬁnition 2.9.
The main result of this section is the following theorem.
Theorem 4.20. Let µ be a complex measure on2[n] with a (complex) stable gener-
ating polynomial. Then for any transposition τ ∈ Sn and θ ∈ [0, 1] the generating
polynomial of the partial symmetrizationµτ,θ = θµ+(1 −θ)τ(µ) is (complex) stable.
In particular, Theorem 4.20 implies that the class of strongly Rayleigh measures
on 2[n] is invariant under the partial symmetrization procedure. Clearly, the latter
result is real stable in nature. However, in order to establish it we have to consider
the (wider) complex stable context (cf. Deﬁnition 2.9), as in the above theorem.
For the proof of Theorem 4.20 we need a multivariate generalization of the clas-
sical Obreschkoﬀ theorem that was obtained in [9].
Theorem 4.21 (Multivariate Obreschkoﬀ theorem). Let f,g ∈ R[z1,...z n].T h e n
all non-zero polynomials in the space {αf + βg : α, β ∈ R} a r es t a b l ei fa n do n l yi f
either f + ig or f − ig is stable or f = g ≡ 0.
5 5 0 J .B O R C E A ,P .B R ¨AND ´EN, AND T. M. LIGGETT
Remark 4.4. There are now elementary proofs of Theorem 4.20 that avoid the mul-
tivariate Obresckoﬀ theorem; see [10, 56]. Also, the referee sketched an elementary
proof similar to those given in [10, 56].
Proof of Theorem 4.20. Let f ∈ C[z1,...,z n] be the generating polynomial of µ.
Hence f is stable and multi-aﬃne. Assuming, as we may, that i =1a n d j =2 ,w e
need to prove that
θf(ξ1,ξ 2,...,ξ n)+( 1 − θ)f(ξ2,ξ 1,...,ξ n) ⁄=0
whenever ξ1,...,ξ n ∈{ z : Im(z) > 0} (cf. Deﬁnition 2.9). By ﬁxing ξ3,...,ξ n
arbitrarily in the open upper half-plane and considering the multi-aﬃne polynomial
in variables z1,z 2 given by
(z1,z 2) ↦→ g(z1,z 2): = f(z1,z 2,ξ 3,...,ξ n),
we see that the problem reduces to proving that the linear operator Tθ on multi-
aﬃne polynomials in two variables deﬁned by
Tθ(h)(z1,z 2)= θh(z1,z 2)+( 1 − θ)h(z2,z 1)
preserves stability. Let us ﬁrst show that Tθ preserves real stability. For this let
f(z1,z 2)= a00 + a01z2 + a10z1 + a11z1z2 ∈ R[z1,z 2] \{ 0}
be real stable and set Df = a00a11 − a01a10. By Theorem 4.1 we know that f is
real stable if and only if Df ≤ 0. Since
DTθ (f ) = Df − θ(1 − θ)(a01 − a10)2 ≤ Df ,
it follows that Tθ(f) is also real stable, as required. To deal with the (non-real)
stable case ﬁrst let h = g + if ∈ C[z1,z 2]b e strictly stable and multi-aﬃne. This
means that h(z1,z 2) ⁄= 0 wheneverIm(z1) ≥ 0a n dIm(z2) ≥ 0. By the multivariate
Obreschkoﬀ theorem we have that αg + βf is real stable or zero for all α, β ∈ R.
H e n c e ,b yt h ea b o v e ,w ea l s oh a v et h a tαTθ(f)+ βTθ(g) is real stable or zero for all
α, β ∈ R. By the multivariate Obreschkoﬀ theorem again this gives thatTθ(g + if)
or Tθ(g − if) is stable. However, one has
Tθ(h)(z,z )= h(z,z )= g(z,z )+ if(z,z ),
which is strictly stable by assumption. IfTθ(g −if) is stable, then g(z,z ) −if(z,z )
is stable and g(z,z )+ if(z,z ) is strictly stable, which is impossible since it would
imply that all zeros of (the strictly stable polynomial) g(z,z )+ if(z,z ) were real.
Hence Tθ(g + if)i ss t a b l e .
Now if ϵ> 0a n dp ∈ C[z1,z 2] is stable, then clearly p(z1 + iϵ, z2 + iϵ) is strictly
stable (in the sense deﬁned above), and thus any stable polynomial is the uniform
limit on compact sets of strictly stable polynomials. By the multivariate version of
Hurwitz’ classical theorem on the “continuity of zeros” (see, e.g., [8, Theorem 2.3]
and [19, Footnote 3, p. 96]) this proves that Tθ preserves stability. □
Remark 4.5. From Theorem 4.20 it follows that the symmetrizationµs of a strongly
Rayleigh measureµ is also strongly Rayleigh. A diﬀerent proof is as follows. Ifµ is a
strongly Rayleigh measure on 2[n], then (2) implies that the diagonal specialization
∆(gµs )(t)=∆ ( gµ)(t) (cf. Deﬁnition 2.8) is a real-rooted univariate polynomial and
by the Grace-Walsh-Szeg¨o theorem we conclude that the symmetrizationµs of µ is
also strongly Rayleigh.
NEGATIVE DEPENDENCE AND THE GEOMETR Y OF POL YNOMIALS 551
5. Preservation of negative dependence
by symmetric exclusion processes
In this section we study some consequences of the results in §4 for symmetric
exclusion processes and provide an answer to the problem of ﬁnding a natural
negative dependence property that is preserved by such evolutions (Problem 3.5).
Let us ﬁrst describe these processes in more detail. A conﬁguration of particles
on a countable set S is a point η on the Boolean lattice 2S, which we identify with
{0, 1}S,s o η(i) = 1 means that site i is occupied, while η(i) = 0 means that it is
vacant. One is given a non-negative symmetric kernel Q =( qi,j)i,j∈S satisfying
(16) sup
i
∑
j
qi,j < ∞.
The corresponding exclusion process ηt is the Markov process on {0, 1}S in which
η → τi,j(η)a tr a t eqi,j,w h e r eτi,j is the transposition that interchanges the coordi-
nates η(i)a n dη(j). Note that if η(i)= η(j) (i.e., the two sites are both occupied or
both empty), this transposition has no eﬀect, while ifη(i) ⁄= η(j), the transposition
has the eﬀect of moving the particle from the occupied site to the vacant site. In the
language of semigroups and generators, the semigroup T(t)o n C({0, 1}S) deﬁned
by T(t)F(η)= EηF(ηt) has a generator
LF(η)= 1
2
∑
i,j
qi,j[F(τi,j(η)) − F(η)]
for functions F that depend on ﬁnitely many coordinates. Condition (16) guaran-
tees that the process is well deﬁned and uniquely determined by Q.
One can give a more probabilistic description of the symmetric exclusion process
in terms of Poisson processes. Recall that a Poisson process N(t)w i t hr a t eλ> 0
is a random increasing step function with jumps of size one, in which the times
between jumps are independent exponentially distributed random variablesτk with
parameter λ: P(τk >t )= e−λt. Now take a collection Ni,j(t) of independent
Poisson processes indexed by unordered pairs i, j (Ni,j(t)w i t hr a t eqi,j) and apply
the transposition τi,j to η at the jump times ofNi,j(t). We will denote probabilities
for the process with initial conﬁguration η by Pη.
Negative correlation inequalities have played an important role in the develop-
ment of the theory of symmetric exclusion processes. For example, Proposition 1.7
of [52, Chap. VIII] implies that
(17) Pη(ηt ≡ 1o n A) ≤
∏
i∈A
Pη(ηt(i)=1 ) ,A ⊆ S.
This inequality was used in an essential way in the characterization of stationary
distributions of the process; see Theorem 1.44 inop. cit. and the end of this section.
Inequality (17) was generalized by Andjel in [2] to
Pη(ηt ≡ 1o n A ∪ B) ≤ Pη(ηt ≡ 1o n A)Pη(ηt ≡ 1o n B),
A, B ⊆ S, A ∩ B = ∅,(18)
and used to prove an ergodic theorem. For further applications of correlation in-
equalities in this setting; see the references and discussion in [55].
5 5 2 J .B O R C E A ,P .B R ¨AND ´EN, AND T. M. LIGGETT
In that paper, one of us conjectured that the distribution of ηt at time t with
deterministic initial conﬁguration η is negatively associated. Even the special case
Pη(ηt ≡ 1o n A, ηt ≡ 0o n B) ≥ Pη(ηt ≡ 1o n A)Pη(ηt ≡ 0o n B),
A, B ⊆ S, A ∩ B = ∅(19)
remained open (note that in (19), one of the events is increasing while the other is
decreasing). Surprisingly, despite the similarity between (18) and (19), neither the
proof of (18) in [2], nor a somewhat diﬀerent one given in [55], extends to prove
(19). We are now able to prove this conjecture; see Theorem 5.2 below. The latter
is actually a consequence of a yet stronger property for ﬁnite symmetric exclusion
processes that we will now establish.
Proposition 5.1. Suppose that S is ﬁnite and the initial distribution η0 of a sym-
metric exclusion process on{0, 1}S is strongly Rayleigh. Then so is the distribution
of ηt for all t> 0.
Proof. First, we observe that it suﬃces to prove the statement in case qi,j ⁄=0f o r
only one pairi, j. To see this, supposeT1(t)a n dT2(t) are semigroups for ﬁnite state
Markov chains on the same state space with generatorsL1 and L2 respectively, and
let T(t) be the semigroup with generator L1 + L2. The Trotter product formula
(see [27, p. 33]) gives
T(t) = lim
n→∞
[
T1(t/n)T2(t/n)
]n
.
It follows that if a closed set of probability measures M on the state space has the
property that µ ∈M implies µTi(t) ∈M for i =1 , 2a n d t> 0, then µ ∈M
implies µT(t) ∈M for t> 0. Now write the generator of the symmetric exclusion
process as the following sum, corresponding to transitions at individual pairs of
sites:
L =
∑
i,j
Li,j,
where
Li,jF(η)= 1
2qi,j[F(τi,j(η)) − F(η)].
Repeated application of the preceding observation withM = the set of probability
measures on {0, 1}S with stable generating polynomials, implies that the statement
of the proposition is correct for the process with generator L if it is correct for the
process with generator Li,j for each i, j.
In the case of a single non-zeroqi,j, the generating polynomial of the distribution
of ηt is given by αf(z)+( 1 − α)f(τi,j(z)), where α = P(Ni,j(t)i se v e n )a n df is
the generating polynomial for the initial distribution. Therefore, the result follows
from Theorem 4.20. □
Recall from §2.4 that if S is a countably inﬁnite set, a probability measure on
{0, 1}S is strongly Rayleigh if every projection onto a ﬁnite subset of S is strongly
Rayleigh. Note that this property is preserved by weak convergence of measures.
Theorem 5.2. Suppose that S is countable and the initial distribution η0 of a
symmetric exclusion process on {0, 1}S is strongly Rayleigh. Then the distribution
of ηt is strongly Rayleigh, and hence CNA+, for all t> 0.
NEGATIVE DEPENDENCE AND THE GEOMETR Y OF POL YNOMIALS 553
Proof. Since stability (the strongly Rayleigh property) implies negative association
by Theorem 4.9, the result follows from Proposition 5.1 whenS is ﬁnite. For general
S, approximate the exclusion process on S by processes on ﬁnite subsets Sn of S
that increase to S, by taking the transposition rates for the process on Sn to be
qi,j if i, j ∈ Sn and zero otherwise. By the Trotter-Kurtz semigroup convergence
theorem (see [27, p. 28]), the processes on Sn converge to the process on S,s ot h e
result holds on S as well. (See [52, §I.3] for details.) □
Remark 5.1. In particular, Theorem 5.2 proves Conjecture 2.2 and shows that its
conclusion remains valid if the initial conﬁguration is a product measure (since any
such measure is obviously strongly Rayleigh; cf. Deﬁnition 2.11 and §2.4).
We conclude this section with an application of Theorem 5.2 to the extremal sta-
tionary distributions for an irreducible symmetric exclusion process. Theorem 1.44
of [52, Chap. VIII] states that these are exactly {µα : α ∈H },w h e r e
(a) H =
{
α : S → [0, 1] :∑
j qi,j[α(j) − α(i)] = 0 for each i
}
are the harmonic
functions for Q with values in [0, 1], and
(b) µα = limt→∞ ναT(t), where να is the product measure on{0, 1}S satisfying
να{η : η ≡ 1o n A} =
∏
i∈A
α(i),A ⊆ S.
Very little is known about µα other than
(I) µα = να if and only if α is constant, and
(II) µα{η : η(i)=1 } = α(i)f o re a c hi ∈ S.
As a consequence of Theorem 5.2, we can now add
(III) µα is negatively associated for each α ∈H .
Remark 5.2. If S is ﬁnite and qi,j > 0 for all i, j,t h e na sw en o t e di n§3.5 the
limiting distribution ofηt as t →∞ is the symmetrization of the initial distribution.
In §7 we construct examples of measures in Pn, n ≥ 20, that are CNA+ but do
not have ULC rank sequences. By Theorem 3.7 in §3.5, these counterexamples to
Conjectures 2.3–2.5 show that none of the properties NLC, h-NLC, Rayleigh/h-
NLC+, CNA, or CNA+ is preserved by the symmetrization procedure (2), and by
[55, Theorem 3.2], the same can be said about the NA property. Therefore, the
analog of Proposition 5.1 fails for all the aforementioned properties.
Remark 5.3. The analog of Theorem 5.2 for asymmetric exclusion processes is false.
A simple example is obtained by taking S = {1, 2} in which only transitions from
state 1 to state 2 are allowed. If the initial distribution gives probability 1
4 to each
of the conﬁgurations in {0, 1}S, then the limiting distribution ast →∞ is given by
µ({11})= µ({00})= 1
4 , µ({10}) = 0, and µ({01})= 1
2 . This measure is not NA.
