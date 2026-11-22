---
doc_id: invariant-eigendistributions-2
doc_title: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups"
section_id: sec-008-6-characters-and-characteristic-cycles
section_title: "Characters and characteristic cycles."
section_number: 6
pages: 10-12
source_pdf: Invariant_eigendistributions_2.pdf
source_sha256: ee43c3ebeff95265
toc_source: inferred
doc_brief: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups — 18 sections: Front matter; Contents; Introduction."
---
As a ﬁrst and immediate application of Theorem 5.1 we derive a formula for the global character of a
(g, K)-module as a contour integral over the characteristic cycle of the corresponding (D, K)-module.
We start with some general remarks about global characters. A (g, K)-module M with inﬁnitesimal
character λ ∈h is the Harish-Chandra module of an admissible representation of Go, whose global
character is an invariant eigendistribution Θ = ch(M) on Go. It follows from results of Harish-Chandra
[1965] that one has an identity of distributions in a neighbourhood of 0 in go :
Θ(exp x) = j(x)−1θ(x)
(1)
where θ is an invariant eigendistribution on go with inﬁnitesimal character λ and
j(x) = det1/2(eadx/2 −e−adx/2
adx
) = ∆(x)
π(x)
on ho.
Here π = 
α∈∆+ α as before, and
∆=

α∈∆+
(eα/2 −e−α/2)
is the Weyl denominator. The products are over the roots α of ho in bo
⊥. If λ ∈h∗is regular, as we shall
now assume, the Integral Formula allows us to write θ = θΓ (λ) for a unique Γ ∈H2n(S). We shall call
this homology class Γ, or any 2n-cycle representing it, the character contour
of the (g, K)-module M,
and denote it C(M). It should be noted that C(M) depends on the choice of the element λ in the W-orbit
in h∗determined by the inﬁnitesimal character of M and on the Borel subalgebra s1 used to deﬁne the
map pλ.
Recall the Beilinson-Bernstein [1981] correspondence between (g, K)-modules and (D, K)-modules.
We consider only the case of regular integral inﬁnitesimal character; one may as well assume (as we now
do) that the inﬁnitesimal character is represented by −ρ where ρ = (ρo, ρo) is half the sum of the roots
of h in z1 = bo × bo.
The Beilinson-Bernstein correspondence based on the data (z1, −ρ) associates to each (g, K)-module
M with inﬁnitesimal character -ρ the (D, K)-module M = D⊗M. (D is the sheaf of diﬀerential operators
on B as in [Beilinson-Bernstein]; the tensor product is over U(g) as explained there.) This correspondence
is an equivalence of categories.
For each K-orbit Zy = K ·y−1z1 there is an induced D-module which we shall denote Iy. Write Iy
for the corresponding (g, K)-module. It is known that Iy is an induced (principal series) (g, K)-module.
The corresponding representation of Go has global character
REPRESENTATIONS OF WEYL GROUPS
11
1
∆

w∈W
e−(yw)−1ρ.
(T hisisaspecialcaseoftherelationbetweentwoofthethreeclassificationsof(
g,K)-modules, ofHecht −Miliˇci´c −Schmid −Wolf[1986].)
Under the correspondence (1) between invariant eigendistributions on Go and on go the global
character corresponds to the distribution
1
π

w∈W
e−(yw)−1ρ.
(2)
In analogy with the data (z1, −ρ) for the Beilinson-Bernstein correspondence it seems natural to base
the character contours on the data (s1, −σ) which correspond to (z1, −ρ) under the automorphism ι
interchanging k and go : s1 = bo × ¯bo and σ = (ρo, −ρo). We therefore write (2) as
1
π

w∈W
e−(wιyw)−1σ = ϕw1y(−σ)
(3)
where wι ∈W is the Weyl group element with wιρ = σ.
It follows from Theorem 5.1 that the character contour of the (g, K)-module Iy (based on the data
(s1, −σ) is
C(Iy) = wιy · S1
(4)
On the other hand, to a (D, K)-module M one can associate a characteristic cycle; this is an algebraic
cycle of complex dimension n on B∗which is known to lie on the conormal variety Z of the K-action
on B for these modules M. It determines therefore a homology class in H2n(Z), denoted Ch(M). By a
result of Tanisaki [1985] (or by the corresponding result of Kasihwara-Tanisaki [1984] for (D, B)-modules,
which amounts to essentially the same thing when go itself is complex, as here) the characteristic cycle of
the induced D-module Iy is
Ch(Iy) = y · Z1.
(5)
Since the Iy and Iy form bases for the respective K-groups one ﬁnds by comparing (4) and (5) :
6.1 Theorem. The character contour C(M) of a (g, K)-module M and the characteristic variety
Ch(M) of the corresponding D-module M are related by:
Ch(M) = wι · ιC(M).
(6)
In this equation ι denotes the map from the conormal variety of K-action of B to the conormal variety of
the Go-action induced by the involutionι of g which interchanges k and go and induces the W-isomorphism
of the homology groups of the conormal varieties. It is further understood that the data (z1, −ρ) entering
into the Beilinson-Bernstein correspondence and the data (s1, −σ) entering into the deﬁnition of character
REPRESENTATIONS OF WEYL GROUPS
12
contours are related by this automorphism ι. Explicitly, (6) says that the global character ch(M) of M is
given by the formula
ch(M)(exp x) = j(x)−1

p−σιwι−1Ch(M)
exσ−σσ.
