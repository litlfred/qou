---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-019-72-monodromic-hecke-categories
section_title: "Monodromic Hecke categories"
section_number: 7.2
pages: 40-41
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — W e apply the ideas of derived algebraic geometry and topolog ical ﬁeld theory to the representation theory of reductive groups."
---
stacks where X has smooth diagonal δ :X→X×X. Suppose given AX∈D (X) a commutative
algebra object.
Let j :X×Y X→X×X be the natural map, introduce the commutative algebra object
A(2)
X =j!(AX ⊠AX )∈D (X×Y X)
and the resulting Hecke category of bimonodromic D-modules
DA(2)
X
(X×Y X) = Mod A(2)
X
(D(X×Y X))
More generally, we have similar constructions for repeated ﬁber pr oducts.
There is a natural monoidal structure on the bimonodromic Hecke c ategory ˜H =DA(2)
X
(X×Y X)
with product given by
M⋆AX N = ˜p13∗(˜p!
12(M)⊗A(3)
X
˜p!
23(N))
Here the functors are the ringed-space variants of the usual pu llback, tensor and pushforward func-
tors. Namely, the !-pullbacks denote the composition of the usual !- pullbacks and then tensoring up
with the free AX -module on the remaining factor. The tensor product denotes the tensor product
ofA(3)
X -modules. The ∗-pushforward denotes the composition of the usual ∗-pushforward and then
forgetting the AX -module structure on the middle factor. The monoidal unit 1 ˜H is the diagonal
bimodule u∗AX arising from the map u : X→ X×Y X. Standard identities produce the higher
constraints of the monoidal structure.
40
In the case where AX =π∗π∗ωX∈D (X) for a smooth map π : ˜X→X as discussed above, the
monodromic Hecke category is a full subcategory
˜H =DA(2)
X
(X×Y X)/d31 /d127 /d47/d47D( ˜X×Y ˜X)
Moreover, the latter category is naturally monoidal with respect t o convolution and the above
inclusion is monoidal.
Example 7.3. If ˜X =B→X =BB→Y =BG are the natural projections of classifying stacks for
a Borel subgroup B⊂G and its unipotent radical N⊂B, then a bimonodromic D-module in the
above sense is equivalent to a traditional unipotent bimonodromic D-module on N\G/N.
We have the following algebraic observation extending Theorems 6.2, 6.3.
Theorem 7.4. Suppose X is a stack with smooth diagonal, Y is a stack, and X→Y is a proper
representable map. Suppose AX∈D (X) is a commutative algebra object whose underlying object is
compact.
Then the monodromic Hecke category ˜H =DA(2)
X
(X×YX) is semi-rigid (hence 2-dualizable) with
a canonical Calabi-Yau structure.
Proof. For compact objects M∈H , objects of the form A(2)
X ⊗ M∈ ˜H are compact and generate.
Recall from the proof of Theorem 6.2 that ι(M)∈H is the left and right monoidal dual of such
compact objects M∈H .
Recall the natural map j :X×Y X→X×X, and introduce the A(2)
X -modules
A(2)
X
′ =j!(AX ⊠A∨
X )∈D (X×Y X) ′A(2)
X =j!(A∨
X ⊠AX )∈D (X×Y X)
It is simple to check that A(2)
X
′⊗ι(M)∈ ˜H (respectively, ′A(2)
X ⊗ι(M)∈ ˜H) is the right (respec-
tively, left) monoidal dual of A(2)
X ⊗ M∈ ˜H.
Finally, for the Calabi-Yau structure, one can directly repeat the p roof of Theorem 6.3 with the
functorsq∗ andp! replaced by their respective monodromic versions ˜q∗ and ˜p! as in the construction
of the monoidal structure on ˜H. Namely, they are given by the ringed-space variants where ˜ q∗ is
the composition of the usual ∗-pushforward and then forgetting the module structure, and ˜ p! is the
composition of the usual !-pullback and then tensoring up with the fr ee module. □
