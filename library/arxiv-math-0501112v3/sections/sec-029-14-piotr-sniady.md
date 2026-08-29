---
doc_id: arxiv-math-0501112v3
doc_title: "GAUSSIAN FLUCTUATIONS OF CHARACTERS OF"
section_id: sec-029-14-piotr-sniady
section_title: "PIOTR ´SNIADY"
section_number: 14
pages: 14-16
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
doc_brief: "GAUSSIAN FLUCTUATIONS OF CHARACTERS OF — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
Some asymptotic results for this representation were prove d by Biane
[Bia01].
Example 3.6 (Irreducible representations). Let c > 0 be a constant and let
(λq ) be a sequence of Young diagrams. We assume thatλq has q boxes and
it has at most c√
q rows and columns. Suppose that the shapes of rescaled
Young diagrams q− 1
2 λq converge to some limit. The convergence of the
shapes of Young diagrams implies convergence of the free cum ulants and
it follows (condition (3.4)) that the sequence (ρλ q) of the corresponding
irreducible representations has the characters factorization property.
In this example the cumulants (3.3) and (3.4) vanish for n ≥ 2 since the
Young diagrams are non-random and the corresponding limits for n = 1
are determined by the limit of the shape of the Young diagrams.
The above three examples are the building blocks from which o ne can
construct some more complex representations with the help o f the opera-
tions on representations presented below.
Theorem 3.7 (Restriction of representations). Suppose that the sequence of
representations (ρq ) has the character factorization property. Let a se-
quence of integers (rq ) be given, such that rq ≥ q and the limit p =
limq →∞
q 
rq
exists.
Let ρ ′
q denote the restriction of the representation ρrq to the subgroup
Sq ⊆ Srq. Then the sequence (ρ ′
q ) has the factorization property of char-
acters. The ﬂuctuations of the free cumulants are determined by
(3.11)
c ′
l+1 := lim
q →∞
E(R ′
l+1)q− l+1
2 = p
l− 1
2 lim
q →∞
E(Rl+1)q− l+1
2 = p
l− 1
2 cl+1,
(3.12) lim
q →∞
Cov(R ′
l1+1, R ′
l2+1)q− l1 +l2
2 =
p
l1 +l2
2
[
lim
q →∞
Cov(Rl1+1, R l2+1)q− l1 +l2
2 − l1l2cl1 +1cl2+1
(
p− 1 − 1
)
+
∑
r≥1
∑
a1,...,a r≥1
a1+···+ar=l1
∑
b1 ,...,b r ≥1
b1 +···+br =l2
l1l2
r ca1+b1 · · · car+br (p− r − 1)
]
for all l, l 1, l 2 ≥ 1, where the quantities R ′
i, c ′
i concern the representations
(ρ ′
q ) while Ri, c i concern the representations (ρq ).
In particular, for p = 0 we recover the ﬂuctuations of the Plancherel
measure.
Proof. Notice that for any permutations σ 1, . . . , σ n the value of the cumu-
lant k(σ 1, . . . , σ n) is the same for the representation ρ ′
q of Sq and for the
GAUSSIAN FLUCTUATIONS OF CHARACTERS OF SYMMETRIC GROUPS 15
representation ρrq of Srq. It follows that
lim
q →∞
kρ ′q (σ 1, . . . , σ n)q
|σ 1 |+···+|σ n |+2(n− 1)
2 =
p
|σ 1 |+···+|σ n |+2(n− 1)
2 lim
q →∞
kρ rq (σ 1, . . . , σ n)(rq )
|σ 1|+···+|σ n |+2(n− 1)
2
Since the original representations (ρq ) fulﬁll condition (3.1) hence re-
stricted representations (ρ ′
q ) fulﬁll (3.1) as well. Equations (3.11) and
(3.12) follow as special cases for n = 1, 2 . □
Remark. Please notice that the above theorem concerns restrictions of the
form ρrq

↓ Srq
Sq
while it is even more interesting to ask about the asymptotics
of the restrictions of the form ρ ′′
q = ρrq

↓ Srq
Sq ×Srq − q
. A typical question is the
following one: let [λ(1)] × [λ(2)] be a random irreducible component of ρ ′′
q ;
is it true that the joint distribution of the free cumulants
(
Ri(λ(r))
)
r∈{1,2 };i≥2
converges after appropriate rescaling to a family of Gaussian variables? The
answer for this question is positive and the Reader may easily prove it using
the methods presented in Section 4.
Such representations are no longer representations of symm etric groups
(but products of such groups) and the original deﬁnition of r epresentations
with the approximate factorization property does not ﬁt into this setup. Nev-
ertheless
In the work of Pittel and Romik [PR04] some interesting results concern-
ing restrictions of irreducible representations correspo nding to rectangular
Young diagrams were proved.
Theorem 3.8 (Outer product of representations). Suppose that for i ∈ {1, 2 }
the sequence of representations (ρ(i)
q ) has the character factorization prop-
erty. Let sequences of positive integersr(i)
q be given, such thatr(1)
q +r(2)
q = q
and the limits p(i) := limq →∞
r(i)
q exist.
Let ρ ′
q = ρ(1)
r(1)
q
◦ ρ(2)
r(2)
q
denote the outer product of representations. Then
the sequence (ρ ′
q ) has the factorization property of characters with
(3.13) c ′
l+1 := lim
q →∞
E(R ′
l+1)q− l+1
2 =
(
p(1)) l+1
2 c(1)
l+1 +
(
p(2)) l+1
2 c(2)
l+1,
