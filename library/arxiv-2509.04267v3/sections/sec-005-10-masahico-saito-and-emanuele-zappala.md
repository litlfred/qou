---
doc_id: arxiv-2509.04267v3
doc_title: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY"
section_id: sec-005-10-masahico-saito-and-emanuele-zappala
section_title: "MASAHICO SAITO AND EMANUELE ZAPPALA"
section_number: 10
pages: 10-12
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
doc_brief: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
The required equality is therefore seen to hold.
We now consider (6) and (7), i.e. we need to show the equalities
Tr2(ϕ(µ⊗µ)) + Tr 2(R(µ1⊗µ)) + Tr2(R(µ⊗µ 1)) =αβµ 1,
Tr2(ˆϕ(µ⊗µ)) + Tr 2(R−1(µ1⊗µ)) + Tr2(R−1(µ⊗µ 1)) =α −1βµ1,
where ˆϕ:=−R −1ϕR−1 is the infinitesimal component of the inverse of ˜R. Observe that
R−1ϕR−1 =R −1δ1
YB(f)R−1
=R −1R(f⊗1)R −1 +R−1R(1⊗f)R −1−R−1(f⊗1)RR −1 +R−1R(1⊗f)RR −1
= (f⊗1)R −1 + (1⊗f)R −1−R−1(f⊗1) +R −1R(1⊗f)
=−δ 1
R−1(f),
whereδ 1
R−1(f) is the first YB differential of the operatorR −1 applied tof.
Therefore, if (R,α,β,µ) is an EYBO, then we have that (R −1,α−1,β,µ) is also an EYBO.
Hence it is sufficient to prove (6), since (7) is equivalent to (6) for the EYBO (R−1,α−1,β,µ), with
ˆϕ=ℏδ 1
R−1(f) and ˜µ=µ+ℏµ 1. For the left-hand side of (6) we have
Tr2(ϕ(µ⊗µ)) + Tr 2(R(µ1⊗µ)) + Tr2(R(µ⊗µ 1))
= Tr 2[R(f⊗1)(µ⊗µ) +R(1⊗f)(µ⊗µ)−(f⊗1)R(µ⊗µ)−(1⊗f)R(µ⊗µ)
+R(µf⊗µ)−R(fµ⊗µ) +R(µ⊗µf)−R(µ⊗fµ)]
= Tr 2[R(f⊗1)(µ⊗µ) +R(1⊗f)(µ⊗µ)−(f⊗1)(µ⊗µ)R−(1⊗f)(µ⊗µ)R
+R(µf⊗µ)−R(fµ⊗µ) +R(µ⊗µf)−R(µ⊗fµ)]
=−Tr 2[(f⊗1)(µ⊗µ)R] + Tr 2[R(µ⊗µ)(f⊗1)]
−Tr2[(1⊗f)(µ⊗µ)R] + Tr 2[R(µ⊗µ)(1⊗f)]
=−fTr 2[(µ⊗µ)R] + Tr 2[R(µ⊗µ)]f−Tr 2[(1⊗f)(µ⊗µ)R] + Tr 2[R(µ⊗µ)(1⊗f)]
=−fαβµ+αβµf
=αβ[µf−fµ]
=αβµ 1,
where we have used (1) and (2) forRandµ, along with
−Tr2[(1⊗f)(µ⊗µ)R] + Tr 2[R(µ⊗µ)(1⊗f)] = 0,
by the cyclic property of the partial trace with respect to maps that factor as1⊗f, and
Tr2[(f⊗1)(µ⊗µ)R] =fTr 2((µ⊗µ)R),
Tr2[R(µ⊗µ)(f⊗1)] = Tr 2[R(µ⊗µ)]f.
This completes the proof.□
The following is an analogue, in our setting, of the result for quandle invariants that states that
the invariant of a coboundary is the number of quandle colorings, see [4].
Proposition 4.6.LetKbe a knot. Let(R,α,β,µ)be an EYBO, letϕ:=δ 2
YB(f)be a coboundary
for some1-cochainf, and setµ 1 =µf−fµ. Then, we haveΦ ϕ(K) = Φ0
ϕ(K). In other words, the
infinitesimal part of the quantum cocycle invariant vanishes,Φ 1
ϕ(K) = 0.
QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY 11
Proof.Applying Lemma 4.5, it follows that Φ ϕ(K) is well defined. Letb m denote a braid on
m-string whose closure isK. We show that
αw(bm)βmΦ1
ϕ(K) =
X
(i,j1,...,jm)∈Γm+1
Tr(Ψi
ϕ(bm)(µj1⊗···⊗µ jm)) = 0.
In this proof, we will refer to the arcs ofb m that are bounded by crossings (regardless of whether
the arc in question is an over or under arc at the end crossings), andexternalotherwise. External
arcs have at least one end at the top or bottom of the braid, and internal arcs do not. We claim
that the only terms in the operator Ψ 1
ϕ(bm) that do not vanish are those whereϕappears in a
position such that it has either external incoming arcs, or external outgoing arcs. In fact, if an arc
is internal, then it takes part in two consecutive crossings. The term Ψ 1
ϕ consists of the braidb m
where each crossing is replaced byR ±, except for one of the crossings whereϕappears. Moreover,
ϕappears exactly once in each position. If we consider an internal arc, then there are two terms
in the sum defining Ψ 1
ϕ whereϕappears, once in the top crossing and once in the bottom crossing.
There are three different types of configurations associated to this situation. Namely, we can have
bm =b′
mσ±
i σ±
i b′′
m, orb m =b′
mσ±
i σ±
i+1b′′
m, orb m =b′
mσ±
i+1σ±
i b′′
m.
R
φ R
φ R(1    f)
(f    1)R
Figure 7
First, we consider the case where all crossings are positive. We consider only the caseb m =
b′
mσiσi+1b′′
m, as the other two are substantially the same, and we show the fact that the contribution
to Ψ 1
ϕ(bm) vanishes for the terms whereϕappears in the position ofσ i, orσ i+1. These terms
correspond to the sum
Ψ0
ϕ(b′
m)◦(ϕ⊗1)(1⊗R)◦Ψ 0
ϕ(b′′
m) + Ψ0
ϕ(b′
m)◦(R⊗1)(1⊗ϕ)◦Ψ 0
ϕ(b′′
m),
which is part of the sum defining Ψ 1
ϕ(bm). In the left-hand side of Figure 7, these two terms are
depicted. Since
ϕ=δ 2
YB(f) =R(f⊗1) +R(1⊗f)−(f⊗1)R−(1⊗f)R,
we can pair the elements corresponding toR(f⊗1) associated to Ψ 0
ϕ(b′
m)◦(ϕ⊗1)(1⊗R)◦Ψ 0
ϕ(b′′
m),
and−(1⊗f)Rin Ψ 0
ϕ(b′
m)◦(R⊗1)(1⊗ϕ)◦Ψ 0
ϕ(b′′
m).These terms are seen to cancel. In the right-
hand side of Figure 7 these 1-cochains are depicted as circles on the corresponding edges. The
two terms represented by circles on the middle edge are the canceling pair. The cancelations of
1-cocycles on arcs are also seen in diagrams of Figure 3, where circles from a single YB 2-cocycle are
distributed to each adjacent edge, and two circles coming from crossings that bound each internal
arc represent canceling terms. This diagrammatic interpretation was also used in [4] for quandle
cocycle invariants.
Since, as shown in Lemma 4.5,ϕ −1 =δ 2
R−1(f), it follows that the computation is substantially
the same whenσ i is replaced byσ−1
i , upon changingRwithR −1. So, the same calculation as above
can be applied to the cases where a negative crossing appears, and we see that the terms all cancel.
We proceed in the same manner for each internal arc, therefore pairing all the terms arising from
each instance ofϕappearing in the positions of the crossings ofb m, and cancel all the terms where
