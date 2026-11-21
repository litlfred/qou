---
doc_id: s0894-0347-08-00618-8
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8"
section_id: sec-006-25-towards-a-theory-of-negative-dependence-probl
section_title: "Towards a theory of negative dependence: Problems and solutions"
section_number: 2.5
pages: 11-13
source_pdf: S0894-0347-08-00618-8.pdf
source_sha256: 7c0b2ca41992b21c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8 — 24 sections: Front matter; Introduction; A plethora of negative dependence"
---
A series of problems and conjectures was proposed by several authors as natural
steps toward building as general a theory of negative dependence as possible. In
[65, §III] Pemantle pointed out that although they are desirable, the many nega-
tive dependence properties listed in §2.1 might not be mutually satisﬁable, and he
suggested a problem that may be formulated as follows.
Problem 2.1. Find a natural and useful class of “negatively dependent measures”.
Note that there may well exist several such classes, if indeed any, depending on
the applications that one has in mind. We show that the class of strongly Rayleigh
measures introduced in §2.2 enjoys all the negative dependence properties deﬁned
in §2.1 as well as other properties, which provides an answer to Problem 2.1.
The problem of describing natural negative dependence properties that are pre-
served by symmetric exclusion evolutions has attracted some attention in the theory
of interacting particle systems and Markov processes [52, 54, 55]; see Problem 3.5
in §3.5 and the discussion therein. In particular, the following conjecture was im-
plicitly made in [65, p. 1374] and [55, p. 551].
Conjecture 2.2. If the initial conﬁguration of a symmetric exclusion process is
non-random/deterministic, then the distribution at time t is NA for all t > 0.
In §5 we prove a stronger form of this conjecture using the results on strongly
Rayleigh measures obtained in §4.
There are several conjectures, ﬁrst published in [65] but apparently of obscure
folklore origin (cf. [72]), stating that various negative dependent properties give rise
to ULC rank sequences. The strongest form of these is contained in the ﬁrst part
of Conjecture 4 in Pemantle’s paper [65] (see also [72, Conjecture 3.9]) and reads
as follows.
Conjecture 2.3. If µ ∈Pn is NA, then it is ULC.
Inspired by Conjecture 2.3 and motivated by Mason’s long-standing conjecture
in enumerative graph/matroid theory [62], Wagner made the following conjecture
in [72, Conjecture 3.4] and baptized it “The Big Conjecture” since – if true – it
would prove the validity of Mason’s conjecture for a large class of matroids.
Conjecture 2.4. Any Rayleigh measure µ ∈Pn is ULC.
Since we now know that the Rayleigh and h-NLC+ properties are equivalent
(Proposition 2.2), Conjecture 2.4 is actually already contained in the second part
of Conjecture 4 in Pemantle’s paper [65]. The weakest form of the latter conjecture
is the one stated below.
Conjecture 2.5. If µ ∈Pn is CNA+, then it is ULC.
532
J. BORCEA, P. BR¨AND´EN, AND T. M. LIGGETT
In §7 we construct examples of measures in Pn for any n ≥20 that disprove
all these three conjectures (for the strongest of these, namely Conjecture 2.3, we
can actually ﬁnd counterexamples already in P3 and P4; see Remark 7.2). In fact,
our examples show that the strongest negative association property (CNA+) need
not even give rise to an SLC rank sequence (Deﬁnition 2.8), thus invalidating a
still weaker version of Conjecture 2.5. Moreover, these same examples show that
neither the PHR property (Deﬁnition 2.6) nor indeed any of the properties weaker
than strongly Rayleigh implies the ULC property, and also that Conjecture 2.5
fails even under extra assumptions like those suggested in [12, Problem 6]. This
conﬁrms once again the delicate nature of negative dependence.
The FKG theorem [30] is a powerful tool that allows one to establish (global) pos-
itive correlation inequalities and limit theorems from a local (usually easier to check)
condition, namely the positive lattice condition PLC. By contrast, there is as yet
no general and practical local-to-global device for negative dependence/association.
The NLC property is not closed under projections and implies neither the NA nor
the (weaker) p-NC property, so the negative version of the FKG theorem fails. As a
potential remedy to this situation, in [65, Conjecture 2] Pemantle conjectured that
the implications CNA ⇒h-NLC and CNA+ ⇒Rayleigh/h-NLC+ (established in
[65]; cf. Remark 2.4) are actually equivalences:
Conjecture 2.6. h-NLC ⇒CNA and Rayleigh/h-NLC+ ⇒CNA+.
We prove Conjecture 2.6 for almost symmetric measures (cf. Deﬁnition 2.1).
Since PHR measures are CNA+ (Theorem 4.10), we are naturally led to consider
the following related problem.
Problem 2.7. Is PHR = Rayleigh/h-NLC+?
Note that if true, this would prove the second part of Conjecture 2.6. In §7
we show that the answer to Problem 2.7 is negative, and that in fact the class of
PHR measures is strictly contained in the class of CNA+ measures. The question
whether Conjecture 2.6 is true in full generality therefore remains open.
We summarize the implications between the various notions of negative depen-
dence discussed so far in Figure 1. Compared with the one in [65, §II.B], this dia-
gram contains ﬁve extra classes – three “old” (ULC, p-NC, NLC) and two “new”
(strongly Rayleigh, PHR) – and disregards the classes called JNRD, JNRD+ in
[65].
As we already noted, the above examples and those in the next sections show
that the left horizontal, down left, and all vertical implications in Figure 1 are strict,
while the question as to whether the right horizontal implications are also strict is
open (cf. Conjecture 2.6). Note also that there is no arrow pointing towards ULC
from anything “below” strongly Rayleigh.
In [65, §I.B & §III.C] it was pointed out that the notions of stochastic domination
and truncation are also useful when studying (positive or) negative dependence.
Deﬁnition 2.14. If µ, ν ∈Pn are such that µ(A) ≥ν(A) for any increasing event
A on 2[n], one says that µ stochastically dominates ν, written µ ≽ν or ν ≼µ.
Deﬁnition 2.15. Let µ ∈Pn and 1 ≤p ≤q ≤n. The truncation of µ to [p, q] is
the conditional measure
µp,q :=

µ
 p ≤
n

i=1
Xi ≤q

∈Pn,
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS
533
ULC
Strongly
Rayleigh


PHR

CNA+

 Rayleigh
(h-NLC+)

CNA

 h-NLC


NA

NLC
p-NC
Figure 1. Subordination relations between negative dependence properties.
which is well deﬁned provided that µ


S ∈2[n] : p ≤|S| ≤q

	̸
= 0. The generating
polynomial of µp,q is thus given by
gµp,q(z1, . . . , zn) = gp,q(z1, . . . , zn)
gp,q(1, . . . , 1)
∈Pn,
where gp,q(z) = 
p≤|S|≤q aSzS and 
S⊆[n] aSzS = gµ(z).
For simplicity, we let µk = µk,k, 0 ≤k ≤n. In [45, 65] and the references therein
it has been discussed whether truncations of measures are operations that preserve
negative dependence properties. Question 10 of [65] asks the following.
Problem 2.8. Under what hypotheses on µ can one prove that µk ≼µk+1?
Moreover, the next conjecture was made in [65, Conjecture 8].
Conjecture 2.9. Suppose that µ is CNA+ and that
µ({S ∈2[n] : |S| = k})µ({S ∈2[n] : |S| = k + 1}) > 0.
Then µk ≼µk+1.
To underline the relevance of these questions, in [65, §III.C] Pemantle argued that
a combination of positive answers to Problem 2.8 and Conjecture 2.9 (for Rayleigh
measures) would imply Conjecture 2.6. In §4.3 we give an answer to Problem 2.8
and prove that its conclusion (hence also that of Conjecture 2.9) holds for strongly
Rayleigh measures, while in §7 we disprove Conjecture 2.9 in its full generality.
