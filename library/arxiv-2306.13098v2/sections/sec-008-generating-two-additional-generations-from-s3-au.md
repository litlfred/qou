---
doc_id: arxiv-2306.13098v2
doc_title: "Three generations of colored fermions with S3 family symmetry from Cayley-Dickson sedenions"
section_id: sec-008-generating-two-additional-generations-from-s3-au
section_title: "Generating two additional generations from S3 automorphisms"
section_number: null
pages: 11-13
source_pdf: 2306.13098v2.pdf
source_sha256: edeb214d587bfca4
doc_brief: "Three generations of colored fermions with S3 family symmetry from Cayley-Dickson sedenions — An algebraic representation of three generations of fermions with SU (3)C color symmetry based on the"
---
Having constructed one generation of electrocolor states, we now proceed to apply ψ to the ladder operators
eqns. (59)-(61), and subsequently the basis states of the minimal left ideals, in order to generate two
additional generations.
The first thing to check is that the S3 automorphisms of S carry over the automorphisms of the left
multiplication algebra Cℓ(8). Given the generating basis e0,...,e 8 for Cℓ(8), it is readily verified that
ψ(ei)ψ(ei) =ψ(e2
i ) =−1, (64)
ψ(ei)ψ(ej) +ψ(ei)ψ(ej) = 0. (65)
Subsequently,ψ extends to an automorphism of the entire Cℓ(8) algebra (see Lemma 9.7 of [45]). A similar
argument holds for the order two S3 automorphism ϵ of S, which likewise extends to an automorphism of
Cℓ(8). It can furthermore be checked that:
ψ(ei+8)ψ(ei+8) =ψ(e2
i+8) =−1, (66)
ψ(ei+8)ψ(ej+8) =−ψ(ei+8)ψ(ej+8). (67)
Finally, one also find that
ψ2(ei) +ψ(ei) +ei = 0, (68)
ψ2(ei+8) +ψ(ei+8) +ei+8 = 0, (69)
indicating that ψ2(ei), ψ(ei) and ei (as well as ψ2(ei+8), ψ(ei+8) and ei+8) are not linearly independent.
These conditions however are not satisfied by more general Cℓ(8) multivectors (nor for e8, which is fixed by
ψ).
Since the action of ψ one1,...,e 15 as elements of Cℓ(8) is known, we can via linearity establish the action
11
of ψ on the ladder operators. This gives the three sets of ladder operators:
A†
i = 1
2
√
2(ei +iei+4 +ei+8 +iei+12), (70)
Ai = 1
2
√
2(−ei +iei+4−ei+8 +iei+12), (71)
ψ(A†
i) =B†
i = 1
2
√
2(aei +iaei+4 +bei+8 +ibei+12), (72)
ψ(Ai) =Bi = 1
2
√
2(−aei +iaei+4−bei+8 +ibei+12), (73)
ψ2(A†
i) =C†
i = 1
2
√
2(bei +ibei+4 +aei+8 +iaei+12), (74)
ψ2(Ai) =Ci = 1
2
√
2(−bei +ibei+4−aei+8 +iaei+12), (75)
where i = 1, 2, 3, and
a =
√
3− 1
2 , b =−
√
3− 1
2 , (76)
satisfying a2 +b2 = 2, a+b =−1, ab=−1/2.
The three sets of ladder operators are not linearly independent since
ψ2(A†
i) +ψ(A†
i) +A†
i = 0. (77)
The two additional sets of ladder operators {B†
i,Bi} and{C†,Ci} generated in this manner likewise
constitute Witt bases for Cℓ(6), satisfying the same anticommutation relations as {A†
i,Ai}, and we proceed
to construct an additional pair of minimal left ideals of Cℓ(6) for each of the two additional sets of ladder
operators{BiB†
i} and{Ci,C†
i}. We interpret these additional pairs of minimal ideals as representing the
second and third generation of electrocolor states:
Su
2 =νµω2ω†
2+
crB†
1ω2ω†
2+cgB†
2ω2ω†
2 +cbB†
3ω2ω†
2+
srB†
3B†
2ω2ω†
2+sgB†
1B†
3ω2ω†
2 +sbB†
2B†
1ω2ω†
2+
µ+B†
3B†
2B†
1ω2ω†
2
Sd
2 =νµω†
2ω2+
crB1ω†
2ω2+cgB2ω†
2ω2 +cbB3ω†
2ω2+
srB3B2ω†
2ω2+sgB1B3ω†
2ω2 +sbB2B1ω†
2ω2+
µ−B3B2B1ω†
2ω2
Su
3 =ντω3ω†
3+
brC†
1ω3ω†
3+bgC†
2ω3ω†
3 +bbC†
3ω3ω†
3+
trC†
3C†
2ω3ω†
3+tgC†
1C†
3ω3ω†
3 +tbC†
2C†
1ω3ω†
3+
τ +C†
3C†
2C†
1ω3ω†
3
Sd
3 =ντω†
3ω3+
brC1ω†
3ω3+bgC2ω†
3ω3 +bbC3ω†
3ω3+
trC3C2ω†
3ω3+tgC1C3ω†
3ω3 +tbC2C1ω†
3ω3+
τ−C3C2C1ω†
3ω3
Here, ω2 :=B1B2B3, ω3 :=C1C2C3.
That is the order three automorphism ψ of the finite group S3 can be used to construct exactly two
additional generations of color states. This automorphism then permutes between the three generations.
On the other hand, the order two automorphism ϵ does not generate transformations between the three
generations. Applying ϵ to the ladder operators Ai and A†
i generates an complementary set of ladder
operators satisfying the same anticommutation relations asAi andA†
i (sinceϵ is an automorphism of Cℓ(8)),
and hence can likewise be used to construct minimal ideals. The automorphism ϵ can then be used to
incorporate an additional degree of freedom (perhaps chirality, handedness, or spin). It is not immediately
clear at present however what the most natural physical interpretation for ϵ is.
12
5.4 SU (3)C color symmetries of three generations
The anticommutators between ladder operators belonging to different generations are not the standard
fermionic anticommutation relations. That is
{Ai,Bj}w̸= 0, {Bi,Cj}w̸= 0, {Ci,Aj}w̸= 0, wheneveri̸=j (78)
and likewise for the other anticommutation relations. Surprisingly however, it turns out that all three
generations of states transform correctly under a single copy of SU (3), which may be generated from any of
the three sets of Cℓ(6) ladder operators. We will here use the SU (3)C generators from Subsection 5.2. One
then finds for example that
h
Λ1,A 1ω†
1ω1
i
=A2ω†
1ω1,
h
Λ1,B 1ω†
1ω1
i
=B2ω†
1ω1,
h
Λ1,C 1ω†
1ω1
i
=C2ω†
1ω1. (79)
A single SU (3) generator thus correctly transforms the equivalent states of each generation
Λ1 :dr→dg, c r→cg, t r→tg. (80)
The same holds true for the otherSU (3) generators and states. Despite having three generations of fermions,
only one copy of SU (3), and hence one generation of gauge bosons is needed in the present construction.
On the other hand, one finds that the number operator only assigns the correct electric charge for one of
the generations. This same issue was encountered in [33]. Thus although the number operator can be used
to obtain the correct electric charge within the context of a single generation model, this approach fails to
work in a three generation model. A generalized action to obtain the correct electric charges is presented in
[35]. This approach, which makes extensive use of both left and right projectors would work for the present
model as well. However, it remains unclear why this action takes the particular form that it does, and so
this issue will be revisited at a later time once the weak (or electroweak) symmetry has been included within
the present sedenion model.
