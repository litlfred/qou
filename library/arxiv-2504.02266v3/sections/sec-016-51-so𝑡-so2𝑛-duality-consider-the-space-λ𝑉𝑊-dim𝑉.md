---
doc_id: arxiv-2504.02266v3
doc_title: "Knizhnik-Zamolodchikov equations in Deligne categories"
section_id: sec-016-51-so𝑡-so2𝑛-duality-consider-the-space-λ𝑉𝑊-dim𝑉
section_title: "(so𝑡, so2𝑛) duality. Consider the space Λ∙(𝑉⊗𝑊), dim(𝑉) = 𝑡, dim(𝑊) = 𝑛. We"
section_number: 5.1
pages: 14-20
source_pdf: 2504.02266v3.pdf
source_sha256: a12193f740b6ee53
toc_source: inferred
---
fix the following notations from [3]. Let so2𝑛be the orthogonal Lie algebra preserving the
form (𝑣𝑖, 𝑣𝑗) = 𝛿𝑖,−𝑗on a space C2𝑛with the basis 𝑣𝑖, 𝑖∈{−𝑛, . . . , −1, 1, . . . , 𝑛}. Let
𝑀𝑖,𝑗:= 𝐸𝑖,𝑗−𝐸−𝑗,−𝑖.
(5.4)
The space Λ∙(𝑉⊗𝑊) admits an action of so2𝑛via
𝑀(𝑘)
𝑖,𝑗= 𝑥𝑘𝑖𝜕𝑘𝑗−𝜕𝑘𝑗𝑥𝑘𝑖
2
,
𝑀(𝑘)
−𝑖,𝑗= 𝜕𝑘𝑖𝜕𝑘𝑗−𝜕𝑘𝑗𝜕𝑘𝑖
2
,
𝑀(𝑘)
𝑖,−𝑗= 𝑥𝑘𝑖𝑥𝑘𝑗−𝑥𝑘𝑗𝑥𝑘𝑖
2
,
𝑖, 𝑗> 0.
(5.5)
We have the following equality in terms of the Clifford algebra
Ω𝑎,𝑏= 1
2
∑︁
1≤𝑖<𝑗≤𝑡
(𝑥𝑖𝑎𝜕𝑗𝑎−𝑥𝑗𝑎𝜕𝑖𝑎)(𝑥𝑗𝑏𝜕𝑖𝑏−𝑥𝑖𝑎𝜕𝑗𝑏) =
(5.6)
= 1
2
∑︁
𝑖<𝑗
(−𝑥𝑖𝑎𝜕𝑖𝑏𝑥𝑗𝑏𝜕𝑗𝑎+ 𝑥𝑗𝑎𝑥𝑗𝑏𝜕𝑖𝑎𝜕𝑖𝑏+ 𝑥𝑖𝑎𝑥𝑖𝑏𝜕𝑗𝑎𝜕𝑗𝑏−𝑥𝑗𝑎𝜕𝑗𝑏𝑥𝑖𝑏𝜕𝑖𝑎) =
(5.7)
= 1
2
∑︁
𝑖<𝑗
(−𝑀(𝑖)
𝑎,𝑏𝑀(𝑗)
𝑏,𝑎−𝑀(𝑖)
𝑏,𝑎𝑀(𝑗)
𝑎,𝑏+ 𝑀(𝑖)
−𝑎,𝑏𝑀(𝑗)
𝑎,−𝑏+ 𝑀(𝑖)
𝑎,−𝑏𝑀(𝑗)
−𝑎,𝑏) =
(5.8)
= −1
2
∑︁
𝑖̸=𝑗
(𝑀(𝑖)
𝑎,𝑏𝑀(𝑗)
𝑏,𝑎−𝑀(𝑖)
−𝑎,𝑏𝑀(𝑗)
𝑎,−𝑏) = −1
2(𝑀𝑎,𝑏𝑀𝑏,𝑎+ 𝑀−𝑎,𝑏𝑀𝑏,−𝑎)+
(5.9)
+ 1
2
∑︁
1≤𝑖≤𝑡
(𝑀𝑎,𝑏𝑀𝑏,𝑎+ 𝑀−𝑎,𝑏𝑀𝑏,−𝑎)(𝑖)
(5.10)
where the last term is a sum of quadratic elements acting on 𝑖th gl(𝑊) tensor component.
Note that the space Λ∙(𝑉⊗𝑊) still retains decomposition
Λ∙(𝑉⊗𝑊) =
⨁︁
𝜆
Λ𝜆1𝑊⊗· · · ⊗Λ𝜆𝑡𝑊.
(5.11)
KNIZHNIK-ZAMOLODCHIKOV EQUATIONS IN DELIGNE CATEGORIES
15
We may identify the space (5.3) with the space of so(𝑉)-singular (under some choice
of Borel subalgebra) vectors of weight 𝜆and of so2𝑛weight 𝛽:= (1 −𝑡
2, . . . , 1 −𝑡
2) in the
highest weight so2𝑛-module of weight 𝛾⊤:= (𝜆′
1 −𝑡
2, . . . , 𝜆′
𝑛−𝑡
2) where 𝜆′ is the usual
transposition of a partition (note that now the notation 𝛾⊤differs from the one given in
Section 3). Let us deal with the last term in (5.6).
(𝑀𝑎,𝑏𝑀𝑏,𝑎+ 𝑀−𝑎,𝑏𝑀𝑏,−𝑎)(𝑖) = 𝑥𝑖𝑎𝜕𝑖𝑏𝑥𝑖𝑏𝜕𝑖𝑎+ 𝜕𝑖𝑎𝜕𝑖𝑏𝑥𝑖𝑏𝑥𝑖𝑎=
(5.12)
= 𝑥𝑖𝑎𝜕𝑖𝑎(1 −𝑥𝑖𝑏𝜕𝑖𝑏) + (1 −𝑥𝑖𝑎𝜕𝑖𝑎)(1 −𝑥𝑖𝑏𝜕𝑖𝑏) = 1 −𝑥𝑖𝑏𝜕𝑖𝑏= 1
2 −𝑀(𝑖)
𝑏𝑏,
(5.13)
so
𝑡
∑︁
𝑖=1
(𝑀𝑎,𝑏𝑀𝑏,𝑎+ 𝑀−𝑎,𝑏𝑀𝑏,−𝑎)(𝑖) = 𝑡
2 −𝑀𝑏𝑏.
(5.14)
This allows us to rewrite the KZ connection (5.1) as follows:
∇𝐾𝑍= 𝑑+ℏ
2
∑︁
1≤𝑎<𝑏≤𝑛
𝑑𝑧𝑎−𝑑𝑧𝑏
𝑧𝑎−𝑧𝑏
(𝑀𝑏,𝑎𝑀𝑎,𝑏+ 𝑀𝑎,𝑎−𝑀𝑏,𝑏+ 𝑀−𝑎,𝑏𝑀𝑏,−𝑎−𝑡
2 + 𝑀𝑏,𝑏) =
(5.15)
= 𝑑+ ℏ
∑︁
1≤𝑎<𝑏≤𝑛
𝑑𝑧𝑎−𝑑𝑧𝑏
𝑧𝑎−𝑧𝑏
(𝑒𝜖𝑏−𝜖𝑎𝑒𝜖𝑎−𝜖𝑏+ 𝑒−𝜖𝑎−𝜖𝑏𝑒𝜖𝑎+𝜖𝑏−𝑡
4 + 𝑀𝑎,𝑎
2
).
(5.16)
Here, 𝑒𝛼, 𝛼∈𝑅are the normalized root elements and 𝜖𝑎are the standard diagonal el-
ements of the dual space to the Cartan subalgebra of so2𝑛. After the restriction to the
weight space in question we will get
𝑑+ ℏ
∑︁
1≤𝑎<𝑏≤𝑛
𝑑𝑧𝑎−𝑑𝑧𝑏
𝑧𝑎−𝑧𝑏
(𝑒𝜖𝑏−𝜖𝑎𝑒𝜖𝑎−𝜖𝑏+ 𝑒−𝜖𝑎−𝜖𝑏𝑒𝜖𝑎+𝜖𝑏+ 1 −𝑡
2
).
(5.17)
Let us fix a so𝑡⊕so2𝑛weight space 𝑀𝜆,𝜇in Λ∙(𝑉⊗𝑊) with weight (𝜆, 𝜇). We obtain
the following.
Theorem 5.1. A function 𝑓: {(𝑧1, · · · , 𝑧𝑛) ∈C𝑛| 𝑧𝑖̸ = 𝑧𝑗} →𝑀𝜆,𝜇is a flat section of
the KZ connection (5.1) if and only if the function
𝑔= 𝑓· [
∏︁
𝑎<𝑏
(𝑧𝑎−𝑧𝑏)]ℏ1−𝑡
2
(5.18)
is a flat section of the dual flat connection
𝑑+ ℏ
∑︁
1≤𝑎<𝑏≤𝑛
𝑑𝑧𝑎−𝑑𝑧𝑏
𝑧𝑎−𝑧𝑏
(𝑒𝜖𝑏−𝜖𝑎𝑒𝜖𝑎−𝜖𝑏+ 𝑒−𝜖𝑎−𝜖𝑏𝑒𝜖𝑎+𝜖𝑏)
(5.19)
In particular, the connection (5.19) is flat.
Example 5.2. Consider an isomorphism of Lie algebras so(6) ∼= sl(4) sending 𝑀12,
𝑀23,𝑀2,−3 to 𝐸23, 𝐸34 and 𝐸12 respectively. Under this isomorphism the connection (5.19)
can be presented as
𝑑+ ℏ
2
(︁𝑑(𝑧1 −𝑧2)
𝑧1 −𝑧2
(𝐸3,2𝐸2,3 + 𝐸4,1𝐸1,4)+
(5.20)
+𝑑(𝑧1 −𝑧3)
𝑧1 −𝑧3
(𝐸4,2𝐸2,4 + 𝐸3,1𝐸1,3)+𝑑(𝑧2 −𝑧3)
𝑧2 −𝑧3
(𝐸4,3𝐸3,4 + 𝐸2,1𝐸1,2)
)︁
,
(5.21)
where 𝑥is a residue of an integer 𝑥modulo 3.
16
P. Etingof ⋆, I. Motorin*, A. Varchenko♢, and I. Zhu†
Recall the definition of the boundary Casimir connection (see [3])
∇bCas := 𝑑−ℏ
2
∑︁
𝑎,𝑏∈𝐼,𝑎̸=𝑏
𝑑(𝑧𝑎−𝑧𝑏)
𝑧𝑎−𝑧𝑏
𝐵2
𝑎,𝑏,
𝐼= {−𝑛, . . . , −1, 1, . . . , 𝑛}
(5.22)
where 𝐵𝑎,𝑏:= 𝐸𝑎,𝑏−𝐸𝑏,𝑎and assume that it acts on the trivial vector bundle with fiber
Λ∙(𝑉⊗𝑈) and the base space {(𝑧−𝑛, . . . , 𝑧−1, 𝑧1, · · · , 𝑧𝑛) ∈C2𝑛| 𝑧𝑖̸ = 𝑧𝑗} where 𝑈is the
tautological representation for so(2𝑛). Note that Λ∙𝑊⊗Λ∙𝑊contains the representation
Λ𝑙𝑈of so(2𝑛) for any 𝑙. We can relate ∇bCas and (5.19) as follows.
Theorem 5.3. Consider the pair of embeddings of an 𝑂(𝑉) × so(𝑈)-module
Λ∙(𝑉⊕2 ⊗𝑊)
𝑖1
←˒ Λ𝑙1𝑈⊗· · · ⊗Λ𝑙𝑡𝑈
𝑖2
˓→Λ∙(𝑉⊗𝑈)
(5.23)
for some non-negative integers 𝑙1, . . . , 𝑙𝑡. The fiber restriction of ∇bCas with respect to the
map 𝑖2 is gauge equivalent to the residue connection
∇′
bCas := 𝑑−ℏ
2
∑︁
1≤𝑎<𝑏≤𝑛
𝑑𝑧𝑎−𝑑𝑧𝑏
𝑧𝑎−𝑧𝑏
(𝐵2
𝑎,𝑏+ 𝐵2
𝑎,−𝑏+ 𝐵2
−𝑎,𝑏+ 𝐵2
−𝑎,−𝑏)
(5.24)
with 𝑧𝑎= 𝑧−𝑎∀𝑎. The fiber restriction of (5.19) with respect to the map 𝑖2 is gauge
equivalent to ∇′
bCas.
Proof. Consider an isomorphism of two so(2𝑛) algebras preserving nondegenerate diagonal
and antidiagonal symmetric forms given by
𝑒𝑗↦→𝑒𝑗+ 𝑒−𝑗
√
2
, 𝑒−𝑗↦→i𝑒−𝑗−𝑒𝑗
√
2
.
(5.25)
Since 𝐺𝐿(𝑈) acts on Λ𝑙1𝑈⊗· · · ⊗Λ𝑙𝑡𝑈, the restriction of the dual connection (5.19)
transforms under this isomorphism into
−1
2
(︀
𝐵2
𝑎,𝑏+ 𝐵2
𝑎,−𝑏+ 𝐵2
−𝑎,𝑏+ 𝐵2
−𝑎,−𝑏−2i𝐵𝑏,−𝑏
)︀
(5.26)
where 𝐵𝑎,𝑏:= 𝐸𝑎,𝑏−𝐸𝑏,𝑎. Here, we can remove the last term by an appropriate gauge
transformation (as it comes from an element of the Cartan subalgebra of so(2𝑛) before
the isomorphism).
Now, take the connection ∇bCas acting on Λ∙(𝑉⊗𝑈) and substitute a change of variables
𝑧−𝑖= 𝜖𝑖+ 𝑧𝑖. Then it can be rewritten as follows
∇bCas = 𝑑−ℏ
2
∑︁
1≤𝑎<𝑏≤𝑛
(︁
𝐵2
𝑎,𝑏𝑑log(𝑧𝑎−𝑧𝑏) + 𝐵2
−𝑎,𝑏𝑑log(𝑧𝑎−𝑧𝑏+ 𝜖𝑎) + 𝐵2
𝑏,−𝑏𝑑log(𝜖𝑏)+
(5.27)
+ 𝐵2
𝑎,−𝑏𝑑log(𝑧𝑎−𝑧𝑏−𝜖𝑏) + 𝐵2
−𝑎,−𝑏𝑑log(𝑧𝑎−𝑧𝑏+ 𝜖𝑎−𝜖𝑏) + 𝐵2
𝑎,−𝑎𝑑log(𝜖𝑎)
)︁
.
(5.28)
The gauge transformation of ∇bCas given by
Ψ = exp
(︃
−ℏ(𝑛−1)
2
𝑛
∑︁
𝑎=1
log(𝜖𝑎)𝐵2
𝑎,−𝑎
)︃
(5.29)
removes all singular terms of ∇bCas with respect to 𝜖𝑎, so we can extend the conjugated
connection to the space 𝜖𝑎= 0, 𝑧𝑎̸ = 𝑧𝑏if 𝑎̸ = 𝑏. Such restriction in the base clearly gives
us the connection ∇′
bCas.
□
We also have the analogues of Lemma 3.5 and Theorem 3.7.
KNIZHNIK-ZAMOLODCHIKOV EQUATIONS IN DELIGNE CATEGORIES
17
Lemma 5.4. For all non-integer and large enough integer 𝑡we have an isomorphism
𝜑: HomRep(𝑂𝑡)(𝑉[𝜆], 𝑉⊗𝑛) ∼= 𝑊𝛾⊤[𝛽],
(5.30)
where 𝑊𝛾⊤is the irreducible so2𝑛-module of the highest weight 𝛾⊤.
Proof. The proof of this lemma is similar to Lemma 3.5, since we know that the joint
highest weight vectors for 𝑂𝑡× 𝑆𝑂2𝑛in Λ∙(𝑉⊗𝑊) are necessarily joint highest weight
vectors for 𝐺𝐿𝑡× 𝐺𝐿𝑚([18][Section 4.3.5]). From this we see that these highest weight
vectors and the relations on their descendants are independent of 𝑡, because we may
embed a joint highest weight vector and its descendants into
⨁︁
𝑖1,...,𝑖𝑙(𝜆)≥0
Λ𝛾1−2𝑖1𝑊⊗· · · ⊗Λ𝛾𝑙(𝜆)−2𝑖𝑙(𝜆)𝑊⊗C · 1 ⊗C · 1 ⊗. . .
(5.31)
for a certain partition 𝛾, but (5.31) is still a finite-dimensional vector space. The choice
of basis in HomRep(𝑂𝑡)(𝑉[𝜆], 𝑉⊗𝑛) is repeated verbatim.
□
Theorem 5.5. The isomorphism 𝜑identifies the connection (5.19) on 𝑊𝛾⊤[𝛽] and the
KZ connection (5.1) on HomRep(𝑂𝑡)(𝑉[𝜆], 𝑉⊗𝑛). The flat sections of both connections are
related as in Theorem 5.1.
Proof. Similar to Theorem 3.7.
□
The usual methods of [17] for finding integral solutions can not be applied directly for
∇𝑏𝐶𝑎𝑠for two reasons. Firstly, the poles of ∇𝑏𝐶𝑎𝑠differ from the root hyperplanes of h*
so2𝑛.
Lastly, there does not seem to be a canonical lift of the connection formula to the level
of universal enveloping algebra 𝑈(̃︀n−⊕h ⊕̃︀n+) wherẽ︀n± are free Lie algebras generated
by 𝑓𝑖, 𝑒𝑖respectively.
Problem 5.6. An interesting problem would be to find integral formulas for solutions to
(5.19) or ∇bCas.
6. Drinfeld-Kohno theorem in Deligne categories.
Let 𝑡∈C ∖Z and Rep(𝐺𝐿𝑡) be the corresponding symmetric Deligne category. Let
𝑉1, ..., 𝑉𝑛, 𝑌be arbitrary objects of Rep(𝐺𝐿𝑡). Let ℏ∈C, and consider the KZ equations
𝜕𝐹
𝜕𝑧𝑖
= ℏ
∑︁
𝑗̸=𝑖
Ω𝑖𝑗
𝑧𝑖−𝑧𝑗
𝐹
(6.1)
where Ω𝑖𝑗are the Casimir endomorphisms and 𝐹is a locally holomorphic solution in
variables 𝑧1, ..., 𝑧𝑛(defined locally in some simply connected region of C𝑛where 𝑧𝑖̸ = 𝑧𝑗
and extended analytically) with values in the space HomRep(𝐺𝐿𝑡)(𝑌, 𝑉1 ⊗... ⊗𝑉𝑛). Let
𝜌(ℏ) be the monodromy representation of the pure braid group 𝐵𝑛(for some base point)
defined by this equation, when without loss of generality 𝑉1 = 𝑉2 = · · · = 𝑉𝑛= 𝑉. Thus,
𝜌(ℏ) is well defined up to an isomorphism.
On the other hand, assume that ℏ/∈Q.
Let 𝑞= 𝑒𝜋𝑖ℏand consider the quantum
Deligne category Rep𝑞(𝐺𝐿𝑡) – the Skein category with parameters 𝑞and 𝑎:= 𝑞𝑡=
𝑒𝜋𝑖ℏ𝑡. Furthermore, assume that 𝑞, 𝑎are multiplicatively independent, so the category
Rep𝑞(𝐺𝐿𝑡) is semisimple and naturally equivalent to Rep(𝐺𝐿𝑡) as an abelian category
(i.e., simple objects of both categories are labeled by the same set - pairs of partitions). Let
𝑋𝑞∈Rep𝑞(𝐺𝐿𝑡) be the 𝑞-analog of the object 𝑋∈Rep(𝐺𝐿𝑡). The category Rep𝑞(𝐺𝐿𝑡) is
braided, so we have a braid group representation 𝜌𝑞: 𝐵𝑛→Aut(HomRep𝑞(𝐺𝐿𝑡)(𝑌𝑞, 𝑉⊗𝑛
𝑞
)).
Theorem 6.1. The representations 𝜌(ℏ) and 𝜌𝑞are isomorphic.
18
P. Etingof ⋆, I. Motorin*, A. Varchenko♢, and I. Zhu†
Proof. Following Drinfeld ([9, 10]), define a new braided tensor structure on Rep(𝐺𝐿𝑡)
using the KZ equations. Namely, consider the KZ equation for 𝑛= 3 with 𝑧1 = 0, 𝑧2 =
𝑧, 𝑧3 = 1. We then get
𝐹′(𝑧) = ℏ
(︂Ω12
𝑧
+ Ω23
𝑧−1
)︂
𝐹(𝑧)
where 𝐹(𝑧) ∈HomRep(𝐺𝐿𝑡)(𝑌, 𝑉1 ⊗𝑉2 ⊗𝑉3). Define the associativity isomorphism
Φ𝑉1𝑉2𝑉3 : (𝑉1 ⊗𝑉2) ⊗𝑉3 →𝑉1 ⊗(𝑉2 ⊗𝑉3)
as the suitably renormalized monodromy operator from 0 to 1 of this KZ equation for
arbitrary 𝑌, and define the braiding by 𝛽:= 𝑒
ℏΩ
2 . Denote this new braided tensor cate-
gory by Rep(𝐺𝐿𝑡)(ℏ). In this category, the braid group action on HomRep(𝐺𝐿𝑡)(ℏ)(𝑌, 𝑉⊗𝑛)
is given, up to isomorphism, by the monodromy of the KZ equation.
Thus we have two braided tensor structures on the same semisimple abelian category.
We can further endow both categories with the ribbon structure by letting the balancing
morphism act by 𝑞−⟨𝜆+2𝜌,𝜆⟩on simple objects of weight 𝜆. The category Rep𝑞(𝐺𝐿𝑡) has
a universal property: braided tensor functors from Rep𝑞(𝐺𝐿𝑡) to a ribbon category 𝒞
correspond to (rigid) objects 𝑋in 𝒞of quantum dimension [𝑡]𝑞, where [𝑡]𝑞:= 𝑞𝑡−𝑞−𝑡
𝑞−𝑞−1 such
that the braiding 𝛽𝑋𝑋: 𝑋⊗𝑋→𝑋⊗𝑋satisfies the Hecke relation (𝛽−𝑞)(𝛽+𝑞−1) = 0.
So we have a braided tensor functor Rep𝑞(𝐺𝐿𝑡) →Rep(𝐺𝐿𝑡)(ℏ) sending the tautological
object 𝑋𝑞to 𝑋, which is clearly an equivalence. The Drinfeld-Kohno theorem follows.
□
Consider analogous representation of the braid group
𝜌𝑂(ℏ) : 𝐵𝑛→Aut(HomRep(𝑂𝑡)(𝑌, 𝑉⊗𝑛))
(6.2)
where 𝑌∈Rep(𝑂𝑡) and 𝑉is the defining object. And let
𝜌𝑂,𝑞: 𝐵𝑛→Aut(HomRep(𝑂𝑡)(𝑌𝑞, 𝑉⊗𝑛
𝑞
))
(6.3)
be a similar representation for the BWM category. Then assuming 𝑞and 𝑞𝑡are multi-
plicatively independent, we have the following.
Theorem 6.2. The representations 𝜌𝑂(ℏ) and 𝜌𝑂,𝑞are isomorphic.
Proof. The same as for Rep(𝐺𝐿𝑡).
□
Appendix A. Hypergeometric solutions for 𝜆, 𝜇= 0 and 𝑚= 𝑛= 2
In this appendix we will describe explicit solutions of the KZ equations as in (3.5) in
terms of hypergeometric functions for the special case when 𝜆, 𝜇= 0 and 𝑚= 𝑛= 2.
In this case we are working in the space HomRep(𝐺𝐿𝑡)(1, 𝑉*⊗2 ⊗𝑉⊗2) ∼= C[𝑆2], and the
Casimirs Ω𝑖𝑗act as in (3.5). Then letting 𝑒, (12) be the two permutations in C[𝑆2] we can
express a KZ section as 𝜑(𝑧1, 𝑧2, 𝑧3, 𝑧4) = 𝑓(𝑧1, 𝑧2, 𝑧3, 𝑧4) · 𝑒+ 𝑔(𝑧1, 𝑧2, 𝑧3, 𝑧4) · (12), and the
KZ equations read
{︃
ℏ−1𝜕1𝑓
=
𝑔
𝑧12 −𝑡𝑓+𝑔
𝑧13
ℏ−1𝜕1𝑔
=
𝑓
𝑧12 −𝑓+𝑡𝑔
𝑧14
and symm. eqs. for 𝑧𝑖↦→𝑧𝜋(𝑖), 𝜋∈{(12)(34), (13)(24), (14)(23)}
(A.1)
KNIZHNIK-ZAMOLODCHIKOV EQUATIONS IN DELIGNE CATEGORIES
19
where for brevity we denote 𝑧𝑖𝑗:= 𝑧𝑖−𝑧𝑗and 𝜕𝑖:= 𝜕𝑧𝑖. Also, denote Δ := 𝑡ℏ. Then it is
straightforward to check that the equations (A.1) are solved by
𝑓(𝑧1, 𝑧2, 𝑧3, 𝑧4) = 𝐴(𝑧1, 𝑧2, 𝑧3, 𝑧4)
𝑧Δ
13𝑧Δ
24
(A.2)
𝑔(𝑧1, 𝑧2, 𝑧3, 𝑧4) = 𝐵(𝑧1, 𝑧2, 𝑧3, 𝑧4)
𝑧Δ
14𝑧Δ
23
.
(A.3)
where 𝐴, 𝐵are functions depending on two parameters 𝑐1, 𝑐2 ∈C:
𝐴:= 𝑐1 ·
(︂𝑧14𝑧32
𝑧12𝑧34
)︂1−Δ
2𝐹1
(︂
1 −ℏ−Δ, 1 + ℏ−Δ; 2 −Δ; 𝑧14𝑧32
𝑧12𝑧34
)︂
(A.4)
+ 𝑐2 · 2𝐹1
(︂
−ℏ, ℏ; Δ; 𝑧14𝑧32
𝑧12𝑧34
)︂
(A.5)
𝐵:= ℏ−1𝑧Δ
14𝑧Δ−1
23
𝑧−Δ+1
13
𝑧−Δ
24 𝑧12(𝜕1𝐴).
(A.6)
Note that these solutions involve one integration (in the hypergeometric functions). For
comparison, Theorem 3.4 and Theorem 4.3 give us the formula for solutions in this case
as explained below.
Let us fix two integration cycles Γ𝑙𝑖, 𝑖= 1, 2 for 𝑙−1
1
: (1, 2, 3, 4) →(2, 3, 1, 4) and
𝑙−1
2
: (1, 2, 3, 4) →(2, 1, 4, 3). Note that 𝑓𝑐(𝜎)𝑣is not zero only in the case if 𝑐(𝜎(4)) is
2. One can see that the vectors 𝑓2𝑓1𝑓3𝑓2𝑣= 𝑓2𝑓3𝑓1𝑓2𝑣both correspond to 𝑒∈C[𝑆2].
Analogously we have the following correspondence
𝑓1𝑓3𝑓2𝑓2𝑣= 𝑓3𝑓1𝑓2𝑓2𝑣∼2𝑒+ 2(12),
(A.7)
𝑓1𝑓2𝑓3𝑓2𝑣∼𝑒+ (12),
(A.8)
𝑓3𝑓2𝑓1𝑓2𝑣∼𝑒+ (12).
(A.9)
This allows us to compute 𝜔:
𝜔=
(︂2𝑡1𝑡4 −(𝑡1 + 𝑡4)(𝑡2 + 𝑡3) + 𝑡2
2 + 𝑡2
3
𝑡2𝑡3(𝑡4 −𝑡2)(𝑡4 −𝑡3)(𝑡1 −𝑡2)(𝑡1 −𝑡3)𝑒+
2𝑡1𝑡4 −(𝑡1 + 𝑡4)(𝑡2 + 𝑡3) + 2𝑡2𝑡3
𝑡2𝑡3(𝑡4 −𝑡2)(𝑡4 −𝑡3)(𝑡1 −𝑡2)(𝑡1 −𝑡3)(12)
)︂
·
· 𝑑𝑡1 ∧𝑑𝑡2 ∧𝑑𝑡3 ∧𝑑𝑡4.
(A.10)
Then we’ll have the solutions given by
∫︁
Γ𝑙𝑖
exp (ℏ(𝑧12𝑡1 + 𝑧23(𝑡2 + 𝑡3) + 𝑧34𝑡4))
(︂
(𝑡2 −𝑡3)2
(𝑡1 −𝑡2)(𝑡1 −𝑡3)(𝑡2 −𝑡4)(𝑡3 −𝑡4)
)︂−ℏ
·
· 𝜔· 𝑧𝑡−1
12 𝑧13𝑧14𝑧23𝑧24𝑧34
(A.11)
Data sharing not applicable to this article as no datasets were generated or analysed
during the current study. All authors declare that they have no conflicts of interest.
References
[1] Y. Andr´e. 𝐺-functions and geometry, volume E13 of Aspects of Mathematics. Friedr. Vieweg & Sohn,
Braunschweig, 1989.
[2] S. Barbier, Diagram categories of Brauer type, arXiv:2406.18436v1 [math.RT], 26 Jun 2024.
[3] E. Bodish and A. Kalmykov, Orthogonal Howe duality and dynamical (split) symmetric pairs,
arXiv:2405.08126v2 [math.RT], 19 Aug 2024.
[4] E. Bombieri, On G-functions, Recent Progress in Analytic Number Theory, Vol. 2, Acad. Press,
1981, pp. 1–67.
[5] J. Brundan, Representations of the oriented skein category, arXiv:1712.08953v1 [math.RT], 24 Dec
2017.
20
P. Etingof ⋆, I. Motorin*, A. Varchenko♢, and I. Zhu†
[6] J. Comes and B. Wilson, Deligne’s category 𝑅𝑒𝑝(𝐺𝐿𝛿) and representations of general linear super-
groups, Representation Theory, 16 (2012), 568–609.
[7] P. Deligne, Cat´egories tannakiennes, in P. Cartier, N. M. Katz, Y. I. Manin, L. Illusie, G. Laumon,
and K. A. Ribet (eds.), The Grothendieck Festschrift, Modern Birkh¨auser Classics, Birkh¨auser,
Boston, MA, 2007.
[8] P. Deligne and J. S. Milne, Tannakian Categories, in Hodge Cycles, Motives, and Shimura Varieties,
Lecture Notes in Mathematics, vol. 900, Springer, Berlin, Heidelberg, 1982.
[9] V. G. Drinfeld, Quasi-Hopf algebras, Algebra i Analiz, 1:6 (1989), 114–148; Leningrad Math. J., 1:6
(1990), 1419–1457.
[10] V. G. Drinfeld, On quasitriangular quasi-Hopf algebras and on a group that is closely connected with
Gal(¯Q/Q), Algebra i Analiz, 2:4 (1990), 149–181; Leningrad Math. J., 2:4 (1991), 829–860.
[11] B. Dwork, G. Gerotto, and F.J. Sullivan, An introduction to 𝐺-functions, Vol. 133 of Ann. Math.
Studies, Princeton Univ. Press, 1994.
[12] P. I. Etingof, S. Gelaki, D. Nikshych, and V. Ostrik, Tensor Categories, Mathematical Surveys and
Monographs, American Mathematical Society, 2015.
[13] P. Etingof and O. Schiffmann, Representation theory in complex rank, II, Transformation Groups,
22(4) (2017), 935–964.
[14] P. Etingof and D. Kazhdan, Quantization of Lie Bialgebras, Part VI: Quantization of Generalized
Kac–Moody Algebras, Transformation Groups, 13 (2008), 527–539. DOI: 10.1007/s00031-008-9029-6.
[15] P.
Etingof
and
A.
Varchenko,
Periodic
and
quasi-motivic
pencils
of
flat
connections,
arXiv:2401.00636v2 [math.AG], 4 May 2024.
[16] B. Feigin, L. Rybnikov, and F. Uvarov, Gaudin model and Deligne’s category, Letters in Mathemat-
ical Physics, 114(1) (2023), Article 3. DOI: 10.1007/s11005-023-01747-y.
[17] G. Felder, Y. Markov, V. Tarasov, and A. Varchenko, Differential Equations Compatible with KZ
Equations, arXiv:math/0001184v1 [math.QA], 31 Jan 2000.
[18] R. Howe, Perspectives on invariant theory: Schur duality, multiplicity-free actions and beyond, in
The Schur Lectures (1992) (Tel Aviv), Israel Math. Conf. Proc., vol. 8, Bar-Ilan Univ., Ramat Gan,
1995, pp. 1–182.
[19] V. Kac, Infinite Dimensional Lie Algebras, Cambridge University Press, 1990.
[20] G. I. Lehrer and R. Zhang, The Brauer category and invariant theory, J. Eur. Math. Soc., 17(9)
(2015), 2311–2351.
[21] E. Mukhin and A. Varchenko, Norm of a Bethe Vector and the Hessian of the Master Function,
Compositio Mathematica, 141(5) (2005), 1462–1475. DOI: 10.1112/S0010437X05001651.
[22] N. Reshetikhin and A. Varchenko, Quasiclassical asymptotics of solutions to the KZ equations, in
Geometry, Topology and Physics for R. Bott, Intern. Press, 1995, pp. 293–322.
[23] V. Schechtman and A. Varchenko, Arrangements of hyperplanes and Lie algebra homology, Invent.
Math., 106 (1991), 139–194.
[24] C. Simpson, Higgs bundles and local systems, Publ. math. de l’I.H.E.S, 75 (1992), 5–95.
[25] V. Tarasov and A. Varchenko, Dynamical Differential Equations Compatible with Rational qKZ
Equations, Letters in Mathematical Physics, 71 (2005), 101–108. DOI: 10.1007/s11005-004-6363-z.
[26] V. Tarasov and A. Varchenko, Identities for Hypergeometric Integrals of Different Dimensions, Let-
ters in Mathematical Physics, 71 (2005), 89–99. DOI: 10.1007/s11005-004-6364-y.
[27] V. Toledano-Laredo, A Kohno-Drinfeld theorem for quantum Weyl groups, Duke Math. J., 112(3)
(2002), 421–451. arXiv:math/0009181.
♢Department of Mathematics, University of North Carolina, Chapel Hill, NC 27599 –
3250, USA
⋆, *, † Department of Mathematics, MIT, Cambridge, MA 02139, USA
Email address:
⋆etingof@math.mit.edu,
* ivanm597@mit.edu,
♢anv@email.unc.edu,
† isaaczhu@mit.edu.
