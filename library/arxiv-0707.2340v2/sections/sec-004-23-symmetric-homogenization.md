---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-004-23-symmetric-homogenization
section_title: "Symmetric Homogenization"
section_number: 2.3
pages: 10-13
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
---
tion procedure for arbitrary measures in Pn. This natural construction proves to
be quite useful for studying strongly Rayleigh measures ( §4.1).
Deﬁnition 2.12. Given a measure µ ∈ Pn deﬁne a new measure µsh ∈ P2n called
the symmetric homogenization of µ by
µsh(S) =
{
µ(S ∩ [n])
( n
|S∩[n]|
)−1
if |S| = n,
0 otherwise.
Note that the generating polynomial of µsh may be written as
gµsh(z1, . . . , zn, zn+1, . . . , z2n) =
∑
S⊆[n]
µ(S)
( n
|S|
)−1
zSen−|S|(zn+1, . . . , z2n),
where z = ( z1, . . . , zn) and ek, 0 ≤ k ≤ n, denotes the k-th elementary symmetric
function. Clearly, gµsh is symmetric in the variables zn+1, . . . , z2n and µsh projects
to µ, that is, gµsh(z1, . . . , zn, 1, . . . ,1) = gµ(z1, . . . , zn). It is not diﬃcult to show
that gµsh is actually the unique polynomial in P2n of total degree n that is symmet-
ric in zn+1, . . . , z2n and satisﬁes the latter identity. Therefore, µsh is canonically
determined by the aforementioned conditions.
2.4. Measures on countably inﬁnite sets. In §5 we will need to extend some
of the notions of negative dependence to probability measures on 2 E, where E is a
countably inﬁnite set. This is canonically done as follows.
Deﬁnition 2.13. Let µ be a probability measure on 2 E, where E is a countably
inﬁnite set satisfying
(A): for all x ∈ E the set
{
T ∈ 2E : x ∈ T
}
is measurable.
Let P be a property deﬁned for measures on power-sets of ﬁnite sets. We say that
µ has property P provided that the projection of µ to all ﬁnite subsets of E has
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS 11
property P. (Note that condition (A) is necessary for projections on ﬁnite se ts to
be well-deﬁned.)
2.5. T owards a Theory of Negative Dependence: Problems and Solut ions.
A series of problems and conjectures was proposed by several au thors as natural
steps toward building as general a theory of negative dependence as possible. In
[65, §III] Pemantle pointed out that although they are desirable, the ma ny nega-
tive dependence properties listed in §2.1 might not be mutually satisﬁable, and he
suggested a problem that may be formulated as follows.
Problem 2.1. Find a natural and useful class of “negatively dependent mea sures”.
Note that there may well exist several such classes, if indeed any, depending on
the applications that one has in mind. We show that the class of stron gly Rayleigh
measures introduced in §2.2 enjoys all the negative dependence properties deﬁned
in §2.1 as well as other properties, which provides an answer to Problem 2.1.
The problem of describing natural negative dependence propertie s that are pre-
served by symmetric exclusion evolutions has attracted some atte ntion in the theory
of interacting particle systems and Markov processes [52, 54, 55], see Problem 3.5
in §3.5 and the discussion therein. In particular, the following conjectu re was im-
plicitly made in [65, p. 1374] and [55, p. 551].
Conjecture 2.2. If the initial conﬁguration of a symmetric exclusion proces s is
non-random/deterministic, then the distribution at time t is NA for all t > 0.
In §5 we prove a stronger form of this conjecture using the results on strongly
Rayleigh measures obtained in §4.
There are several conjectures, ﬁrst published in [65] but appare ntly of obscure
folklore origin (cf. [72]), stating that various negative dependent p roperties give rise
to ULC rank sequences. The strongest form of these is contained in the ﬁrst part
of Conjecture 4 in Pemantle’s paper [65] (see also [72, Conjecture 3.9]) and reads
as follows.
Conjecture 2.3. If µ ∈ Pn is NA then it is ULC.
Inspired by Conjecture 2.3 and motivated by Mason’s long-standing conjecture
in enumerative graph/matroid theory [62], Wagner made the following conjecture
in [72, Conjecture 3.4] and baptized it “The Big Conjecture” since – if true – it
would prove the validity of Mason’s conjecture for a large class of ma troids.
Conjecture 2.4. Any Rayleigh measure µ ∈ Pn is ULC.
Since we now know that the Rayleigh and h-NLC+ properties are equiv alent
(Proposition 2.2), Conjecture 2.4 is actually already contained in the second part
of Conjecture 4 in Pemantle’s paper [65]. The weakest form of the lat ter conjecture
is the one stated below.
Conjecture 2.5. If µ ∈ Pn is CNA + then it is ULC.
In §7 we construct examples of measures in Pn for any n ≥ 20 that disprove
all these three conjectures (for the strongest of these, name ly Conjecture 2.3, we
can actually ﬁnd counterexamples already in P3 and P4, see Remark 7.2). In fact,
our examples show that the strongest negative association prope rty (CNA+) need
not even give rise to an SLC rank sequence (Deﬁnition 2.8), thus inva lidating a
12 J. BORCEA, P. BR ¨AND ´EN, AND T. M. LIGGETT
still weaker version of Conjecture 2.5. Moreover, these same exa mples show that
neither the PHR property (Deﬁnition 2.6) nor indeed any of the prop erties weaker
than strongly Rayleigh implies the ULC property, and also that Conje cture 2.5
fails even under extra assumptions like those suggested in [12, Prob lem 6]. This
conﬁrms once again the delicate nature of negative dependence.
The FKG theorem [30] is a powerful tool that allows one to establish ( global) pos-
itive correlation inequalities and limit theorems from a local (usually eas ier to check)
condition, namely the positive lattice condition PLC. By contrast, th ere is as yet
no general and practical local-to-global device for negative depe ndence/association.
The NLC property is not closed under projections and implies neither the NA nor
the (weaker) p-NC property, so the negative version of the FKG t heorem fails. As a
potential remedy to this situation, in [65, Conjecture 2] Pemantle c onjectured that
the implications CNA ⇒ h-NLC and CNA+ ⇒ Rayleigh/h-NLC+ (established in
[65], cf. Remark 2.4) are actually equivalences:
Conjecture 2.6. h-NLC ⇒ CNA and Rayleigh/h-NLC+ ⇒ CNA+.
We prove Conjecture 2.6 for almost symmetric measures (cf. Deﬁn ition 2.1).
Since PHR measures are CNA+ (Theorem 4.10), we are naturally led to consider
the following related problem.
Problem 2.7. Is PHR = Rayleigh/h-NLC+?
Note that if true, this would prove the second part of Conjecture 2.6. In §7
we show that the answer to Problem 2.7 is negative, and that in fact t he class of
PHR measures is strictly contained in the class of CNA+ measures. Th e question
whether Conjecture 2.6 is true in full generality therefore remains open.
We summarize the implications between the various notions of negativ e depen-
dence discussed so far in Fig. 1 below. Compared with the one in [65, §II.B], this
diagram contains ﬁve extra classes – three “old” (ULC, p-NC, NLC) and two “new”
(strongly Rayleigh, PHR) – and disregards the classes called JNRD, J NRD+ in [65].
As we already noted, the above examples and those in the next sect ions show
that the left horizontal, down left, and all vertical implications in Fig. 1 are strict,
while the question whether the right horizontal implications are also s trict is open
(cf. Conjecture 2.6). Note also that there is no arrow pointing tow ards ULC from
anything “below” strongly Rayleigh.
In [65, §I.B & §III.C] it was pointed out that the notions of stochastic domination
and truncation are also useful when studying (positive or) negativ e dependence.
Deﬁnition 2.14. If µ, ν ∈ Pn are such that µ(A) ≥ ν(A) for any increasing event
A on 2 [n] one says that µ stochastically dominates ν, written µ ≽ ν or ν ≼ µ.
Deﬁnition 2.15. Let µ ∈ Pn and 1 ≤ p ≤ q ≤ n. The truncation of µ to [ p, q] is
the conditional measure
µp,q :=
(
µ
⏐⏐⏐⏐p ≤
n∑
i=1
Xi ≤ q
)
∈ Pn,
which is well deﬁned provided that µ
({
S ∈ 2[n] : p ≤ |S| ≤ q
})
⁄= 0. The generating
polynomial of µp,q is thus given by
gµp,q (z1, . . . , zn) = gp,q(z1, . . . , zn)
gp,q(1, . . . ,1) ∈ P n,
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS 13
ULC Strongly
Rayleigh/d111/d111
/d15/d15
PHR
/d15/d15
CNA+
/d15/d15
/d47/d47 Rayleigh
(h-NLC+)
/d15/d15
CNA
/d15/d15
/d47/d47 h-NLC
/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127
/d15/d15
NA
/d15/d15
NLC
p-NC
Figure 1. Subordination relations between negative dependence properties .
where gp,q(z) =∑
p≤|S|≤q aSzS and∑
S⊆[n] aSzS = gµ(z).
For simplicity, we let µk = µk,k, 0 ≤ k ≤ n. In [45, 65] and references therein
it has been discussed whether truncations of measures are opera tions that preserve
negative dependence properties. Question 10 of [65] asks the follo wing.
Problem 2.8. Under what hypotheses on µ can one prove that µk ≼ µk+1?
Moreover, the next conjecture was made in [65, Conjecture 8].
Conjecture 2.9. Suppose that µ is CNA + and that
µ({S ∈ 2[n] : |S| = k})µ({S ∈ 2[n] : |S| = k + 1}) > 0.
Then µk ≼ µk+1.
To underline the relevance of these questions, in [65, §III.C] Pemantle argued that
a combination of positive answers to Problem 2.8 and Conjecture 2.9 ( for Rayleigh
measures) would imply Conjecture 2.6. In §4.3 we give an answer to Problem 2.8
and prove that its conclusion (hence also that of Conjecture 2.9) h olds for strongly
Rayleigh measures, while in §7 we disprove Conjecture 2.9 in its full generality.
