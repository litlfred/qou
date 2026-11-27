---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-010-32-bosonization-and-expected-results
section_title: "Bosonization and expected results"
section_number: 3.2
pages: 12-15
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
Many algebraic aspects of the continuum limit of Temperley-Lieb based models can be understood using
bosonization of the underlying XXZ spin chain and its relation with the free-ﬁeld (Dotsenko-Fateev) descrip-
tion [31] of c <1 CFTs. We start with some basic results here, concerning in particular the identiﬁcation of
the stress-energy tensor and its “twisted” version, the role of vertex operators, and the nature of corrections to
scaling. These results will be useful later to formulate conjectures about the continuum limit of modules.
The free ﬁeld (FF) representation starts with a pair of (chiral and anti-chiral) bosonic ﬁelds ϕ, ¯ϕ with the
stress-energy tensors
TFF = −1
4 :(∂ϕ)2:, (46a)
¯TFF = −1
4 :(¯∂ ¯ϕ)2:, (46b)
12
where :−: denotes normal order. The Hamiltonian is
HFF =−
∫ dσ
2π (TFF + ¯TFF), (47)
and the propagators are
⟨ϕ(z)ϕ(z′)⟩ = −2 ln(z−z′), (48a)
⟨ ¯ϕ(¯z) ¯ϕ(¯z′)⟩ = −2 ln(¯z− ¯z′). (48b)
Here z = σ +iτ, where σ is the space coordinate and τ the imaginary time coordinate.
To further analyse this free-ﬁeld problem we deﬁne the vertex operators
Vα(e,m),¯α(e,m) = :exp
(
ie
2α+Φ−im
2α−Θ
)
:, (49)
expressed here in terms of the non-chiral components
Φ ≡ ϕ + ¯ϕ, (50a)
Θ ≡ ϕ− ¯ϕ. (50b)
The integerse,m∈ Z can be interpreted as electric and magnetic charges in the Coulomb gas formalism [38,39],
and in terms of those we have
α(e,m ) = 1
2 (eα+−mα−) , (51a)
¯α(e,m ) = 1
2 (eα+ +mα−) , (51b)
whereα± are coupling constants related with the compactiﬁcation radius of the boson. The conformal weights
of the vertex operators (49) are then
hFF = [ α(e,m )]2, (52a)
¯hFF = [¯α(e,m )]2. (52b)
We consider speciﬁcally low-energy excitations over the ground state of the antiferromagnetic Hamiltonian
(19), which are described by (47), with
α+ ≡
√
x + 1
x , (53a)
α− ≡ −
√ x
x + 1 (53b)
in the parametrization (1).
Deﬁning
fj =−σ−
j σ+
j+1−σ+
j σ−
j+1− cosγ
2 σz
jσz
j+1 + cosγ
2 (54)
we note that we can equivalently write the Hamiltonian (19) as
H =− γ
π sinγ
N∑
j=1
(fj−f∞), (55)
wheref∞ =e∞. Let us now consider the scaling limit of each individual term. We use the basic formulae from
the literature (see, e.g., [40])
σz
j = aα+
2π
dΦ
dσ + (−1)jCz
1ad1,0 sinα+Φ
2 (σ) +... , (56a)
σ±
j = exp
(
±iα−
2 Θ
)
(σ)
[
ad0,1C±
0 +ad1,1C±
1 (−1)j cosα+Φ
2 (σ) +...
]
, (56b)
where a is the cutoﬀ (lattice spacing) and the physical coordinate σ = ja. The Cz
1,C±
0 ,C±
1 are (known)
constants that depend only on x. The numbers de,m are the physical dimensions of the operators (49), namely
de,m≡hFF + ¯hFF.
13
Using these formulae, one can write a similar expansion for the elementary Hamiltonians [40]
fj−f∞ =a2 sinγ
2γ (TFF + ¯TFF)(σ) +C1(−1)jad1,0 cosα+Φ
2 (σ) +... . (57)
The important quantity is the dimension
d1,0 = α2
+
2 = x + 1
2x . (58)
In the regime we are interested in, γ∈ [0,π ], whence x∈ [0,∞). The leading contribution to (57) comes from
the ﬁrst term only when d1,0 > 2, that is 1 − γ
π < 1
4, or γ∈] 3
4,π ]. Equivalently, the anisotropy parameter
∆∈ [−1,−
√
2
2 ] from (20), or the conformal parameter x < 1
3 from (1). For values inside this interval, we can
thus safely write, as a→ 0:
− γ
a2π sinγ (fj−f∞)≈− 1
2π (TFF + ¯TFF). (59)
Outside this interval—i.e. for x> 1
3 (including x integer)—the second term dominates. A very important fact
however is that the second term comes with a (−1)j alternating prefactor, i.e., it only contributes to excitations
at lattice momentum near π. As a result, for all Virasoro generators Ln at ﬁnite n—and thus at momentum of
order 1/N—the alternating term is eﬀectively scaling with a dimension d1,0 + 2. For instance, for L0 we have
fj−1 +fj+1 + 2fj = 4a2 sinγ
2γ (TFF + ¯TFF)(σ) +C1(−1)jad1,0+2 d2
dσ2 cosα+Φ
2 (σ) +... , (60)
and we see that all corrections are irrelevant.
The same analysis can now be carried out for the Temperley-Lieb generators ej. Comparing (54) and (18)
we see that
ej =fj−isinγ
2
(
σz
j−σz
j+1
)
, (61)
for which we get the continuum limit
− γ
a2π sinγ (ej−e∞) =− 1
2π (TFF + ¯TFF)(σ) +i γ
(2π)2α+
d2Φ
dσ2 . (62)
Since in the models we study, the Temperley-Lieb generators are the fundamental Hamiltonian densities, we
must interpret the right-hand side of this equation as a modiﬁed or “improved” stress-energy tensor, which is
the sum of its free ﬁeld analog TFF + ¯TFF and a new “deformation” term. In terms of the parameter x, the
“twist term” multipliying the second derivative of Φ is
1
2π× 1
2(x + 1)
√
x + 1
x ≡ 1
2πα0, (63)
where we have introduced the so-called background chargeα0, deﬁned as in (6), familiar from the Coulomb-gas
analysis [31]. Using that ∂2
σΦ =∂2ϕ+( ¯∂)2 ¯ϕ, we ﬁnally get the expressions for the modiﬁed stress-energy tensor
T = −1
4 :(∂ϕ)2: +iα0∂2ϕ, (64a)
¯T = −1
4 :(¯∂ ¯ϕ)2: +iα0 ¯∂2 ¯ϕ. (64b)
This is the well known “twisted” stress-energy tensor studied in [31, 41, 42]. It is this modiﬁed stress-energy
tensor—rather than the free-ﬁeld version TFF, ¯TFF of (46)—that is relevant for a lattice discretization based
on the Temperley-Lieb algebra. We shall henceforth consider T, ¯T throughout almost all the paper, except in
Appendix G where we shall give an alternative construction based on the untwisted stress-energy tensor.
With respect to this stress-energy tensor, the vertex operators Vα,¯α get the modiﬁed conformal weights
h = α2− 2αα0, (65a)
¯h = ¯α2− 2¯αα0, (65b)
to be compared to the previous free-ﬁeld expressions (51).
14
The eigenvalues of H and P only allow one to determine the conformal weights, not the value of the charges.
For a given conformal weight, two values are possible in general, α and 2α0−α. Recalling the notation in (4)
we now state the result, ﬁrst shown in [1], which we will justify in detail below:
In the XXZ spin chain with twisted boundary conditions parametrized by φ = 2πeφ, the scaling states in the
sector of magnetization Sz correspond in the scaling limit to primary states Vα,¯α with charges on the form
α = α−(e−eφ),Sz = 1
2(e−eφ)α+ +α0− 1
2Szα− (66a)
¯α = α−(e−eφ),−Sz = 1
2(e−eφ)α+ +α0 + 1
2Szα−, (66b)
wheree is an integer, and their descendants. The conformal weights are given by (65).
The precise correspondence, including the proper identiﬁcation of the integers e, will be discussed in Section 4,
as well as the exact meaning of the words scaling states and scaling limit.
We conclude this section by some remarks about corrections to scaling. The leading corrections to ej look
a bit diﬀerent from (57). We have
(ej−e∞) =a2 sinγ
2γ (T + ¯T )(σ)−iα+a2 sinγ
4π
d2Φ
dσ2 +(−1)jad1,0
(
Cz
1 sinα+Φ
2 (σ) + 2iC1 cosα+Φ
2 (σ)
)
+... . (67)
Meanwhile, it is expected that the leading correction should now be given by the operator Φ 2,1 with conformal
weightsh = ¯h =h2,1 = x+3
4x in the twisted theory. Under twisting, we expect in general the ﬁeld
:exp(niαΦ): with α = α+
2 (68)
to get the weight
h =α2− 2αα0 =h1−n,1. (69)
This means the term exp( iα+Φ/2) should disappear from the combination in (67), leading to a relationship
between the two constants
Cz
1 = 2C1. (70)
While (70) can be checked to hold in some cases using results in [43, 44], we are not aware of a general proof:
more investigation of this question would be very interesting, but it outside the scope of this paper.
