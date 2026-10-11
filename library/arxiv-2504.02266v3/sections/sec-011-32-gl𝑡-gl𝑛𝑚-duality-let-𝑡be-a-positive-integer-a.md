---
doc_id: arxiv-2504.02266v3
doc_title: "Knizhnik-Zamolodchikov equations in Deligne categories"
section_id: sec-011-32-gl𝑡-gl𝑛𝑚-duality-let-𝑡be-a-positive-integer-a
section_title: "(gl𝑡, gl𝑛+𝑚) duality. Let 𝑡be a positive integer and gl𝑡the corresponding general"
section_number: 3.2
pages: 6-10
source_pdf: 2504.02266v3.pdf
source_sha256: a12193f740b6ee53
toc_source: inferred
---
linear Lie algebra. In this section we derive a duality between the KZ equations for gl𝑡
and dynamical differential equations for gl𝑛+𝑚, via the joint action of gl𝑡and gl𝑛+𝑚on
the space Λ∙(𝑉⊗𝑊), where 𝑉, 𝑊are the tautological representations for gl𝑡and gl𝑛+𝑚
respectively. The derivation is similar to [27].
The space in (3.8) can be given the structure of a weight space of a gl(𝑛+ 𝑚)-module.
Namely, consider the space Λ∙(𝑉⊗𝑊), which inherits the action of gl(𝑉)⊕gl(𝑊). Recall
the following
Theorem 3.2 (Skew-Howe duality,[18]). As a gl(𝑉) ⊕gl(𝑊)-module
Λ∙(𝑉⊗𝑊) =
⨁︁
𝛿, 𝑙(𝛿)≤𝑡,𝑙(𝛿⊤)≤𝑛+𝑚
𝑉𝛿⊗𝑊𝛿⊤,
(3.9)
where 𝑉𝛿, 𝑊𝛿⊤are the irreducible representations of gl(𝑉) and gl(𝑊) of weights 𝛿and 𝛿⊤
respectively. In this section we define 𝛿⊤as the transpose of the partition 𝛿. The sum is
over all partitions 𝛿satisfying the conditions above.
From the action of the Cartan subalgebra of gl(𝑊) it follows that given the standard
weight basis for 𝑊, for any non-negative integer weight 𝛿= (𝛿1, . . . , 𝛿𝑛+𝑚) we have an
isomorphism of gl(𝑉)-module and gl(𝑊)-weight space of weight 𝛿:
Λ𝛿1𝑉⊗· · · ⊗Λ𝛿𝑛+𝑚𝑉∼= Λ∙(𝑉⊗𝑊)[𝛿].
(3.10)
In particular, we have an embedding (Λ𝑡−1𝑉)⊗𝑛⊗𝑉⊗𝑚˓→Λ∙(𝑉⊗𝑊) whose image is
the subspace of gl(𝑛+ 𝑚) weight
𝛽:= (𝑡−1, . . . , 𝑡−1
⏟
 ⏞
 
𝑛times
, 1, . . . , 1
⏟ ⏞ 
𝑚times
).
(3.11)
KNIZHNIK-ZAMOLODCHIKOV EQUATIONS IN DELIGNE CATEGORIES
7
Therefore, if 𝜇1 ≤𝑛, 𝜆1 ≤𝑚(otherwise the space (3.8) is 0) we have an embedding
Homgl𝑡(𝑉𝜆,𝜇⊗(Λ𝑡𝑉)⊗𝑛,(Λ𝑡−1𝑉)⊗𝑛⊗𝑉⊗𝑚)
∼= Homgl𝑡(𝑉𝜆,𝜇⊗(Λ𝑡𝑉)⊗𝑛, Λ∙(𝑉⊗𝑊)[𝛽]) ∼= 𝑊𝛾⊤[𝛽]
(3.12)
where 𝛾is the highest weight of the gl𝑡-module 𝑉𝜆,𝜇⊗(Λ𝑡𝑉)⊗𝑛,
𝛾:= (𝑛+ 𝜆1, 𝑛+ 𝜆2, . . . , 𝑛−𝜇2, 𝑛−𝜇1
⏟
 ⏞
 
𝑡entries
).
(3.13)
Let us take the standard bases 𝑣𝑎∈𝑉and 𝑤𝑖∈𝑊for 1 ≤𝑎≤𝑡, 1 ≤𝑖≤𝑛+ 𝑚and
form a basis 𝑥𝑎,𝑖= 𝑣𝑎⊗𝑤𝑖of 𝑉⊗𝑊. As a gl𝑡-module, the space Λ∙(𝑉⊗𝑊) is isomorphic
to
Λ∙[𝑥1,1, . . . , 𝑥𝑡,1] ⊗· · · ⊗Λ∙[𝑥1,𝑛+𝑚, . . . , 𝑥𝑡,𝑛+𝑚].
(3.14)
The gl𝑡Casimir operators Ω𝑖𝑗(as in (3.1)) act on this space as
Ω𝑖𝑗=
∑︁
𝑎
(𝑒𝑎)(𝑖)(𝑒𝑎)(𝑗)
(3.15)
where {𝑒𝑎}, {𝑒𝑎} are dual bases of gl𝑡, and the outside subscripts (𝑖) indicate action on the
𝑖-th factor of the tensor product. As Λ∙(𝑉⊗𝑊) is a gl𝑛+𝑚-module, it carries an action
by the operators 𝜅𝑖𝑗for 1 ≤𝑖, 𝑗≤𝑛+ 𝑚, 𝑖̸ = 𝑗defined by
𝜅𝑖𝑗:= 𝑒𝛼𝑒−𝛼+ 𝑒−𝛼𝑒𝛼
(3.16)
where 𝛼is the root 𝜃𝑖−𝜃𝑗of gl𝑛+𝑚and 𝑒±𝛼are the corresponding root vectors 𝐸𝑖𝑗, 𝐸𝑗𝑖
respectively from g±𝛼⊂gl𝑛+𝑚normalized by Tr(𝑒𝛼𝑒−𝛼) = 1.
Let 𝐸𝑖𝑗, 1 ≤𝑖, 𝑗≤𝑛+ 𝑚, be the standard basis of gl𝑛+𝑚.
Lemma 3.3. For any 1 ≤𝑖< 𝑗≤𝑛+ 𝑚, the equality
2Ω𝑖𝑗= −𝜅𝑖𝑗+ 𝐸𝑖𝑖+ 𝐸𝑗𝑗
(3.17)
holds as operators on Λ∙(𝑉⊗𝑊).
Proof. The action of Ω𝑖𝑗on Λ∙(𝑉⊗𝑊) can be written as
∑︁
1≤𝑎,𝑏≤𝑡
𝑥𝑎,𝑖𝜕𝑏,𝑖𝑥𝑏,𝑗𝜕𝑎,𝑗
(3.18)
where 𝑥𝑟,𝑐and 𝜕𝑟,𝑐are the operators of multiplication and differentiation by 𝑥𝑟,𝑐(with
appropriate powers of −1). Similarly, the action of 𝜅𝑖𝑗is
∑︁
1≤𝑎,𝑏≤𝑡
(𝑥𝑎,𝑖𝜕𝑎,𝑗𝑥𝑏,𝑗𝜕𝑏,𝑖+ 𝑥𝑏,𝑗𝜕𝑏,𝑖𝑥𝑎,𝑖𝜕𝑎,𝑗).
(3.19)
In view of the anticommutation relation 𝑥𝑎,𝑖𝜕𝑏,𝑗+ 𝑥𝑏,𝑗𝜕𝑎,𝑖= 𝛿𝑎,𝑏𝛿𝑖,𝑗, we have
𝜅𝑖𝑗=
∑︁
1≤𝑎,𝑏≤𝑡
𝑥𝑎,𝑖(−𝑥𝑏,𝑗𝜕𝑎,𝑗+ 𝛿𝑎,𝑏)𝜕𝑏,𝑖+ 𝑥𝑏,𝑗(−𝑥𝑎,𝑖𝜕𝑏,𝑖+ 𝛿𝑎,𝑏)𝜕𝑎,𝑗
(3.20)
= −2Ω𝑖𝑗+
∑︁
1≤𝑎≤𝑡
(𝑥𝑎,𝑖𝜕𝑎,𝑖+ 𝑥𝑎,𝑗𝜕𝑎,𝑗) = −2Ω𝑖𝑗+ 𝐸𝑖𝑖+ 𝐸𝑗𝑗
(3.21)
as desired.
□
For arbitrary weights 𝜆, 𝜇Let 𝑀𝜆,𝜇be the subspace of Λ∙(𝑉⊗𝑊) with gl𝑡-weight 𝜆and
gl𝑛+𝑚-weight 𝜇. As a consequence of the above lemma, we have the following theorem.
8
P. Etingof ⋆, I. Motorin*, A. Varchenko♢, and I. Zhu†
Theorem 3.4. A function 𝑓: {(𝑧1, · · · , 𝑧𝑛+𝑚) ∈C𝑛+𝑚| 𝑧𝑖̸ = 𝑧𝑗} →𝑀𝜆,𝜇is a flat section
of the KZ connection
∇𝐾𝑍= 𝑑−ℏ
∑︁
1≤𝑖<𝑗≤𝑛+𝑚
𝑑𝑧𝑖−𝑑𝑧𝑗
𝑧𝑖−𝑧𝑗
Ω𝑖𝑗
(3.22)
if and only if the function 𝑔= 𝑓· ∏︀
1≤𝑖<𝑗≤𝑛+𝑚(𝑧𝑖−𝑧𝑗)−(𝜇𝑖+𝜇𝑗)ℏ/2 is a flat section of the
connection
∇𝜅:= 𝑑+ ℏ
2
∑︁
1≤𝑖<𝑗≤𝑛+𝑚
𝑑𝑧𝑖−𝑑𝑧𝑗
𝑧𝑖−𝑧𝑗
𝜅𝑖𝑗.
(3.23)
Additionally, by using the gauge transformation ∇𝜅→ℎ∇𝜅ℎ−1 where
ℎ= exp
(︃
ℏ
2
∑︁
1≤𝑖<𝑗≤𝑛+𝑚
(𝜇𝑖−𝜇𝑗) log(𝑧𝑖−𝑧𝑗)
)︃
(3.24)
we can change the ∇𝜅connection to the dynamical connection ∇𝐷as in [17]:
∇𝐷= 𝑑+ ℏ
∑︁
1≤𝑖<𝑗≤𝑛+𝑚
𝑑𝑧𝑖−𝑑𝑧𝑗
𝑧𝑖−𝑧𝑗
𝐸𝑗𝑖𝐸𝑖𝑗.
(3.25)
Proof. A straightforward computation. For the second part, note that
𝑒𝛼𝑒−𝛼+ 𝑒−𝛼𝑒𝛼= 𝐸𝑖𝑗𝐸𝑗𝑖+ 𝐸𝑗𝑖𝐸𝑖𝑗= 2𝐸𝑗𝑖𝐸𝑖𝑗+ ℎ𝛼
(3.26)
and ℎ𝛼acts on 𝑀𝜆,𝜇by 𝜇𝑖−𝜇𝑗, where 𝛼= 𝜃𝑖−𝜃𝑗.
□
In the the following lemma we assume that 𝑡is either a non-integer or a large enough
integer number. However, in the actual proof we will only need to know it for large enough
integer numbers, because we can apply interpolation argument.
Lemma 3.5. For all non-integer and large enough integer 𝑡we have an isomorphism
𝜑: HomRep(𝐺𝐿𝑡)(𝑉[𝜆,𝜇], 𝑉*⊗𝑛⊗𝑉⊗𝑚) ∼= 𝑊𝛾⊤[𝛽],
(3.27)
where 𝑊𝛾⊤is the unique (infinite-dimensional for generic 𝑡) irreducible gl𝑛+𝑚-module of
the highest weight 𝛾⊤.
Proof. In this proof we will refer to the RHS or the LHS of the equation (3.27). Note that
for the specified 𝑡the dimension of the LHS is the same as the dimension of the same space
for some large enough integer 𝑡. The dimension of the RHS is constant due to the follow-
ing parabolic induction consideration. The module 𝑊𝛾⊤can be obtained by a quotient
of Indgl(𝑛+𝑚)
p
(𝑊𝛾⊤
𝑛⊗𝑊𝛾⊤
𝑚) where p is the block upper-triangular Lie subalgebra that con-
tains gl(𝑛)⊕gl(𝑚) and 𝑊𝛾⊤
𝑛or 𝑊𝛾⊤
𝑚are finite-dimensional irreducible gl(𝑛) or respectively
gl(𝑚) modules with highest weights 𝛾⊤
𝑛:= (𝛾⊤
1 , . . . , 𝛾⊤
𝑛) and 𝛾⊤
𝑚:= (𝛾⊤
𝑛+1, . . . , 𝛾⊤
𝑛+𝑚). The
action of the nilpotent part of p on 𝑊𝛾⊤
𝑛⊗𝑊𝛾⊤
𝑚is trivial.
For the choice of the LHS basis let us consider a projection
𝜋: HomRep(𝐺𝐿𝑡)(𝑉⊗|𝜆| ⊗𝑉*⊗|𝜇|, 𝑉*⊗𝑛⊗𝑉⊗𝑚) ↠HomRep(𝐺𝐿𝑡)(𝑉[𝜆,𝜇], 𝑉*⊗𝑛⊗𝑉⊗𝑚). (3.28)
Recall the set of spanning (𝑤, 𝑤′)−diagrams from the bigger space as in [6] for a variable
𝑇. Since C[𝑇] is a PID, it follows from the properties of the walled Brauer algebra that
the LHS in (3.27) admits a set of vectors polynomial in 𝑇such that it forms a basis after
taking a quotient 𝑇= 𝑡for 𝑡∈C ∖Z or for large enough integer 𝑡.
Let us fix a basis of the corresponding weight space from the PBW-spanning set on
the RHS. Note that the relations on the PBW vectors from the RHS are independent of
𝑡. Indeed, otherwise it would mean that we have a singular vector above 𝛽in the Verma
KNIZHNIK-ZAMOLODCHIKOV EQUATIONS IN DELIGNE CATEGORIES
9
module 𝑀𝛾⊤whose coefficients necessarily depend on 𝑡. This in turn would imply the
same fact for all large integer 𝑡, but with this assumption all the relations on the PBW
vectors are independent of 𝑡due to the consideration of the embedding below. In partic-
ular, it is clear that if a subset from the set of spanning PBW vectors is a basis for some 𝑡
as in the lemma, then it will also be a basis for the same weight space for all non-integer
or large enough integer 𝑡because the weights of the singular vectors of the corresponding
Verma module sitting above 𝛽are all the same for such 𝑡.
For a large integer 𝑡we may associate the space (3.8) with the space of gl(𝑉) highest
weight vectors of the gl(𝑉) ⊕gl(𝑊)-weight (𝛾, 𝛽) in Λ∙(𝑉⊗𝑊). We may embed both
spaces for a large integer 𝑡into the (𝛾, 𝛽)-weight space of Λ∙(𝑉⊗𝑊). In turn, it can be
viewed as the space
(Λ𝛾1𝑊⊗· · · ⊗Λ𝛾𝑡𝑊)[𝛽].
(3.29)
The highest weight vector of Λ𝛾1𝑊⊗· · · ⊗Λ𝛾𝑡𝑊is already gl(𝑉)-singular when it is
embedded back into Λ∙(𝑉⊗𝑊), so if we want to get the image of 𝜑from (3.27) in (3.29),
it is sufficient for us to apply chains of gl(𝑊) lowering operators to this vector, so that
we arrive in the correct weight space of weight 𝛽. The space in (3.29) has a spanning set
𝑤𝐽= 𝑓𝑗1
1 . . . 𝑓𝑗1
𝑘1𝑤1 ⊗· · · ⊗𝑓𝑖𝑡
1 . . . 𝑓𝑗𝑡
𝑘𝑡𝑤𝑡,
(3.30)
for various sequences 𝐽= (𝑗1
1, . . . , 𝑗1
𝑘1; . . . ; 𝑖𝑡
1, . . . , 𝑗𝑡
𝑘𝑡) and where 𝑤𝑖are the highest weight
vectors in Λ𝛾𝑖𝑊and
wt(𝑓𝑗1
1 . . . 𝑓𝑗1
𝑘1 . . . 𝑓𝑗𝑡
1 . . . 𝑓𝑗𝑡
𝑘𝑡) = 𝛾⊤−𝛽.
(3.31)
The coefficients in terms of (3.30) of the basis from the LHS will be rational in 𝑡and the
coefficients of the basis from the RHS will be constant. We want to produce the matrix
of the basis change from the RHS to the LHS. However, when 𝑡→+∞the image of the
LHS/RHS spaces lies in the subspace of a fixed (independent of 𝑡) finite dimension:
(Λ𝛾1𝑊⊗· · · Λ𝛾|𝜆|𝑊⊗(Λ𝑛𝑊⊗· · · ⊗Λ𝑛𝑊)𝑆𝑡−|𝜆|−|𝜇| ⊗Λ𝑡−|𝜇|+1𝑊⊗· · · ⊗Λ𝑡𝑊)[𝛽], (3.32)
where 𝑆𝑡−|𝜆|−|𝜇| acts by permutations of the tensor factors. Therefore, the matrix of the
basis change has fixed rational coefficients in 𝑡and we can identify the spaces from (3.27)
for 𝑡∈C ∖{−𝑀, . . . , −1, 0, 1, . . . , 𝑀} for some integer 𝑀.
□
Remark 3.6. Note that the weights 𝛽, 𝛾⊤are well defined for arbitrary 𝑡as opposed to the
weight 𝛾. Indeed, in order to obtain 𝛾⊤we only have to modify the weight (𝑡, . . . , 𝑡
⏟ ⏞ 
𝑛times
) by
adding or subtracting integer components of 𝜆⊤, 𝜇⊤at the respective parts of (𝑡𝑛). This
duality trick allows us to incorporate all 𝑡-dependence into 𝛽and 𝛾⊤.
We have the following consequence of Lemma 3.5.
Theorem 3.7. The isomorphism 𝜑in (3.27) identifies the dynamical connection on
𝑊𝛾⊤[𝛽] and the KZ connection on HomRep(𝐺𝐿𝑡)(𝑉[𝜆,𝜇], 𝑉*⊗𝑛⊗𝑉⊗𝑚). In particular, if
𝑓: {(𝑧1, · · · , 𝑧𝑛+𝑚) ∈C𝑛+𝑚| 𝑧𝑖̸ = 𝑧𝑗} →𝑊𝛾⊤[𝛽]
(3.33)
is a flat section of the dynamical connection, then
∏︁
1≤𝑖<𝑗≤𝑛+𝑚
(𝑧𝑖−𝑧𝑗)−(𝛽𝑖+𝛽𝑗)ℏ/2 · ℎ· 𝜑−1(𝑓) =
∏︁
1≤𝑖<𝑗≤𝑛+𝑚
(𝑧𝑖−𝑧𝑗)−𝛽𝑗ℏ· 𝜑−1(𝑓)
(3.34)
is a flat section of ∇𝐾𝑍.
Remark 3.8. According to this theorem, the KZ connection on HomRep(𝐺𝐿𝑡)(𝑉𝜆,𝜇, 𝑉*⊗𝑛⊗
𝑉⊗𝑚) in the Deligne category 𝐺𝐿𝑡corresponds to the dynamical connection on the gl𝑚+𝑛-
module 𝑊𝛾⊤whose highest weight is determined by the Deligne parameter 𝑡.
10
P. Etingof ⋆, I. Motorin*, A. Varchenko♢, and I. Zhu†
Proof. Since we know that 𝐸𝑗𝑖𝐸𝑖𝑗act as truncated Casimirs on 𝑊𝛾⊤[𝛽] for all sufficiently
large integers 𝑡and this action is polynomial in 𝑡(in terms of a PBW basis), it follows
that 𝐸𝑗𝑖𝐸𝑖𝑗will still act as truncated Casimirs for all non-integer and large enough integer
𝑡.
□
