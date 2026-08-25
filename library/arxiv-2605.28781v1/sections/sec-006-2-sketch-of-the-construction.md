---
doc_id: arxiv-2605.28781v1
doc_title: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS"
section_id: sec-006-2-sketch-of-the-construction
section_title: "Sketch of the construction"
section_number: 2
pages: 5-6
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
doc_brief: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily largeA⊂R(whose elements are algebraic integers in a number"
---
In this section we give a sketch of the construction which is used to prove The-
orem 1.2. The construction is a high-dimensional version of the standard Balog–
Wooley example first introduced in [4]. In its simplest one-dimensional form, one
takes
A=GP,
whereGis a short geometric progression andPis an interval. The multiplicative
structure ofGgives 1
|GG|≪|G|,
while the additive structure ofPkeepsGP+GPinside a relatively short interval.
This gives examples for which both|A+A|and|AA|are smaller than the trivial
bound|A| 2, but only by a logarithmic factor in|A|. This example was used by
Balog and Wooley [4] to show that the natural additive energy variant of the sum-
product conjecture is false, yet it falls short of being a counterexample to the
original conjecture since the geometric progression is exponentially sparse, which
allowsA+Ato still have size≥|A| 2−o(1).
The point of the present construction is to transform this example, replacing the
geometric progression with a much denser multiplicatively structured set, and the
arithmetic progression with a high-dimensional lattice embedded inR. Instead of
working inZ, we work in the ring of integersO K of a totally real number fieldK
of large degreed. Thedreal embeddings
σ1,...,σ d :K ,→R
allow us to viewO K as a lattice of full rank inR d. We will use two different lattice
structures inO K: the additive lattice of algebraic integers and the multiplicative
logarithmic lattice of units.
The additive part of the construction is a box of algebraic integers. We choose
a large parameterX, and takeP⊂O K so that every embedding of everyp∈P
lies in a short interval aroundX, say
σi(p)∈[X−cX,X+cX] (1≤i≤d)
for some small constantc>0. The geometry of numbers gives
|P|≫X d∆−1/2
K ,
up to harmless constants. Thus, provided the discriminant ∆ K is bounded above
byO(1) d,Pbehaves like ad-dimensional additive box of size≫X d.
The multiplicative part is a box in the unit lattice. By Dirichlet’s unit theorem,
the logarithms of the absolute values of the embeddings of units form a lattice of
rankd−1 in the hyperplane defined by the equationx 1 +···+x d = 0. We choose
G={u∈O ×
K :|log|σ i(u)||≤Yfor alli}.
The regulator of the number field controls the covolume of this unit lattice, and
hence, provided the regulator is at mostO(1) d, there are≫Y d−1 many such units.
Moreover, sinceGGis contained in the same logarithmic lattice box withYreplaced
by 2Y, we have a small-doubling estimate of the form
|GG|≤O(1) d|G|.
1In this section we will make free use of the Vinogradov notation≪and≫, both of which
indicate the relevant inequality holds up to some absolute constant.
6 THOMAS F. BLOOM, WILL SA WIN, CARL SCHILDKRAUT, AND DMITRII ZHELEZOV
This is the high-dimensional analogue of the fact that a geometric progression has
small product set.
We then take
A=GP={up:u∈G, p∈P}.
Importantly, providedXandYare chosen suitably, this product is direct in the
sense that|A|=|G||P|. This is because, ifu 1p1 =u 2p2 withu i∈Gandp i∈P,
thenp 1/p2 is a unit. Provided the short interval aroundXin the definition ofP
is sufficiently short, we haveσ i(p1/p2)∈[1−ϵ,1 +ϵ] for all 1≤i≤dand any
small absolute constantϵ >0. By a result of Schinzel, however, ifu̸= 1 is a unit
then there exists 1≤i≤dsuch that|σ i(u)−1|> ϵ, whereϵ >0 is an absolute
constant independent ofKandd. Therefore the only solutions tou 1p1 =u 2p2 are
those withu 1 =u 2.
To control the size ofA+A, the key point is that multiplication by units inG
expands each embedding by at moste Y . Therefore every element ofAlies, in all
real embeddings, inside a box of side lengthO(Xe Y ). Consequently
A+A⊆{α∈O K :|σ i(α)|≪Xe Y for alli}.
