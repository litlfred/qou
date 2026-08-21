---
doc_id: afst-2007-6-16-3-665-0
doc_title: "Galois theory of q-difference equations"
section_id: sec-004-13-the-slope-ﬁltration
section_title: "The slope ﬁltration"
section_number: 1.3
pages: 6-7
source_pdf: AFST_2007_6_16_3_665_0.pdf
source_sha256: 402b61574e561f86
doc_brief: "Galois theory of q-difference equations (van der Put–Reversat, Ann. Fac. Sci. Toulouse XVI:3, 2007, 665–718) — Galois-theoretic framework for q-difference equations."
---
We describe here the slope ﬁltration and give references for more details
and proofs. It is well known that any diﬀerence moduleM overK contains
acyclicvector.Thismeansthatthereexistsanelement e ∈M suchthatthe
homomorphismK[Φ,Φ−1] →M,givenby ∑ anΦn ↦→∑ anΦn(e),issurjec-
tive(compareLemma4.1).Thus M isisomorphicto K[Φ,Φ−1]/K[Φ,Φ−1]L
for someLof the form Φd+ad−1Φd−1+··· +a0, with allai ∈K anda0 ⁄=0 .
The diﬀerence operatorL has a Newton polygon. For completeness we re-
call its deﬁnition. Letord : ˆK → Z ∪{ +∞} denote the order function
on ˆK∗ extended byord( 0 )=+∞.I n R2 one considers the convex hull of⋃d
i=0{(i, −ord(ai)+ x2)| x2 ⩽ 0}. The ﬁnite part of the boundary of this
convex set is the Newton polygon ofL.
The moduleM (overK or over ˆK) is calledpureif this Newton polygon
has only one slope. As in the case of diﬀerential operators, one can factorize
L, viewed as an element ofˆK[Φ,Φ
−1], according to the slopes in any order
that one chooses. This gives a unique decomposition ofˆK ⊗K M as direct
sum N1 ⊕N2 ⊕· · ·⊕ Nr of pure diﬀerence modules over ˆK with slopes
λ1 <λ 2 < ··· <λr. The rule Φzn = qnznΦ and |q| < 1 imply that the
slope factorizationL1 ·L2 ··· Lr ofL whereLi has slopeλi fori =1,...,r
is convergent, i.e., allLi are inK[Φ,Φ−1].
One deduces from this the ascendingslope ﬁltrationof M by submod-
ules 0 =M0 ⊂ M1 ⊂ M2 ⊂· · ·⊂ Mr = M such that eachMi/Mi−1 is
pure of slopeλi and moreover ˆK ⊗Mi/Mi−1 ∼=Ni. The slope ﬁltration is
unique. The graded modulegr(M) associated toM is ⊕r
i=1Mi/Mi−1.W e
note that the above facts on slope ﬁltration are already present in the work
of G.D. Birkhoﬀ, P.E. Guenther and C.R. Adams, see [Bir]. A modern proof
is provided in [Sau3]. The diﬀerence moduleM overK is calledsplit ifM is
isomorphic togr(M) (in other words,M is a direct sum of pure modules).
Fix a direct sumA= ⊕
r
i=1Ai of pure modules with slopesλ1 < ··· <λr.I n
section 3 we will construct a ﬁne moduli space for the equivalence classes of
the pairs (M,f ), consisting of a diﬀerence module overK and an isomor-
phismf :gr(M) →A.
– 669 –
Marius van der Put, Marc Reversat
