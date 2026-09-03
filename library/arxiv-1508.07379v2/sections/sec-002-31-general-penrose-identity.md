---
doc_id: arxiv-1508.07379v2
doc_title: "Convergence of Mayer and Virial expansions and the Penrose t ree-graph identity"
section_id: sec-002-31-general-penrose-identity
section_title: "General Penrose identity"
section_number: 3.1
pages: 7-8
source_pdf: 1508.07379v2.pdf
source_sha256: c3dbf93d1cac198e
doc_brief: "Convergence of Mayer and Virial expansions and the Penrose t ree-graph identity — We establish new lower bounds for the convergence radius of the Ma yer series and the Virial series of a continuous"
---
Penrose identity is a rewriting of the Ursell functions
Φ T (x1, . . . , x n) =
∑
g∈Gn
∏
{i,j }∈Eg
[
e−βV (xi−xj) − 1
]
based on the existence of a map ( partition scheme ) from the set Tn of the trees with vertex set [ n]
to the set Gn of the connected graphs with vertex set [ n].
Deﬁnition 3 A map M : Tn → G n is called a partition scheme in the set of the connected graph s
Gn if, for all τ ∈ T n, τ ⊂ M (τ) (i.e. τ is subgraph of M (τ)) and Gn = ⨄
τ∈Tn[τ, M (τ)] where ⨄
means disjoint union and [τ, M (τ)] = {g ∈ G n : τ ⊂ g ⊂ M (τ)} is an interval in Gn (with respect
to the set-inclusion).
Once a partition scheme in Gn has been given, we have the following identity
Theorem 2 (General Penrose identity) Let V (x) be a pair potential. Let n ≥ 2. Let M :
Tn → G n be a partition scheme in Gn. Then, for any (x1, . . . , x n) ∈ Rdn the following identity holds
∑
g∈Gn
∏
{i,j }∈Eg
[
e−βV (xi−xj) − 1
]
=
∑
τ∈Tn

 ∏
{i,j }∈Eτ
(
e−βV (xi−xj ) − 1
)

 e
−β ∑
{i,j }∈EM (τ )\Eτ
V (xi−xj )
(3.1)
Proof . Let us pose shortly Vij = βV (xi − xj). Since Gn is the disjoint union Gn = ⨄
τ∈Tn[τ, M (τ)]
we can write
∑
g∈Gn
∏
{i,j }∈Eg
(
e−Vij − 1
)
=
∑
τ∈Tn
∑
g∈[τ, M (τ)]
∏
{i,j }∈Eg
(
e−Vij − 1
)
=
=
∑
τ∈Tn
∏
{i,j }∈Eτ
(
e−Vij − 1
) ∑
g∈Gn
Eτ ⊂Eg ⊂EM (τ )
∏
{i,j }∈Eg\Eτ
(
e−Vij − 1
)
=
=
∑
τ∈Tn
∏
{i,j }∈Eτ
(
e−Vij − 1
) ∑
E⊂EM (τ )\Eτ
∏
{i,j }∈E
(
e−Vij − 1
)
=
=
∑
τ∈Tn

 ∏
{i,j }∈Eτ
(
e−Vij − 1
)

 ∏
{i,j }∈EM (τ )\Eτ
[(
e−Vij − 1
)
+ 1
]
=
=
∑
τ∈Tn

 ∏
{i,j }∈Eτ
(
e−Vij − 1
)

 ∏
{i,j }∈EM (τ )\Eτ
e−Vij □
From Theorem 2 the corollary below easily follows.
7
Corollary 1 Let V (x) be a pair potential. Let n ≥ 2. Let M : Tn → G n be a partition scheme in
Gn. Then, for any (x1, . . . , x n) ∈ Rdn the following inequality holds
⏐⏐⏐⏐⏐⏐
∑
g∈Gn
∏
{i,j }∈Eg
[
e−βV (xi−xj ) − 1
]
⏐⏐⏐⏐⏐⏐
≤
∑
τ∈Tn
e
−β ∑
{i,j }∈EM (τ )\E+τ
V (xi−xj ) ∏
{i,j }∈Eτ
(
1 − e−β |V (xi−xj)|
)
(3.2)
where E+
τ denotes the set of edges of the tree τ with non-negative energy. That is,
E+
τ = {{i, j } ∈ Eτ : V (xi − xj) ≥ 0} (3.3)
Proof. Let us pose once again Vij = βV (xi − xj). By Theorem 2 we have that
⏐⏐⏐⏐⏐⏐
∑
g∈Gn
∏
{i,j }∈Eg
(
e−Vij − 1
)
⏐⏐⏐⏐⏐⏐
≤
∑
τ∈Tn
∏
{i,j }∈Eτ
⏐⏐e−Vij − 1
⏐⏐e
− ∑
{i,j }∈EM (τ )\Eτ Vij
(3.4)
Using now the trick proposed in [17] we observe that, for any τ ∈ T n
∏
{i,j }∈Eτ
|e−Vij − 1| =
[ ∏
{i,j }∈Eτ
(1 − e−|Vij |)
]
e
− ∑
{i,j }∈Eτ \E+τ
Vij
so that

 ∏
{i,j }∈Eτ
⏐⏐e−Vij − 1
⏐⏐

 e
− ∑
{i,j }∈EM (τ )\Eτ Vij
=

 ∏
{i,j }∈Eτ
(1 − e−|Vij |)

 e
− ∑
{i,j }∈EM (τ )\E+τ
Vij
(3.5)
Inserting now (3.5) into (3.4) we get (3.2). □
