---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-012-comparison-with-reflection-symmetries
section_title: "Comparison with reflection symmetries"
section_number: null
pages: 32-34
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
Next, we will show that reflection reductions generalize reflection symmetries. First
let us define reflection symmetries more formally. Apermutation matrixBis a square
binary matrix with exactly one nonzero element with value1in each row and column.
ItiswellknownthattheinverseB −1 isagainapermutationmatrix,whichcorresponds
to the inverse permutation of the permutation given byB. Asigned permutation
matrixis a square{−1,0,1}-matrix with exactly one nonzero element in each row and
column. Note that each signed permutation matrixBcan be decomposed asdiag(s)C
orCdiag(s ′)whereCis the nonzero support ofB, which is a permutation matrix,
andsands ′ are suitably chosen{−1,1}vectors. In this section, we do not allow for
arbitrary reordering of matrix columns and rows. In order to clarify the effect of the
permutation symmetries, we denote each permutation explicitly using a permutation
matrix.
Definition22Consider a linear programF(A,b,ℓ,u,c), withA∈R V×W . Letγ∈{−1,1} V,
λ∈ {−1,1}W and defineΓ := diag(γ)andΛ := diag(λ), and letC∈ {0,1} V×V and
32
D∈ {0,1}W×W be permutation matrices. Then,(γ,λ,C,D)is areflection symmetry of
F(A,b,ℓ,u,c)if the following hold:
(i)CΓAΛD=A
(ii)CΓb=b
(iii)D −1λc=c
(iv)−D −1bs(ℓ,u,−λ) =ℓandD −1bs(u,ℓ,λ) =u
Furthermore, we say that(C,D)is apermutation symmetryofF(A,b,ℓ,u,c)if(1,1,C,D)
is a reflection symmetry ofF(A,b,ℓ,u,c).
Theorem 23Every reflection symmetry ofF(A,b,ℓ,u,c)induces a permutation symmetry
ofF S(A,b,ℓ,u,c).
ProofLet(γ,λ,C,D)be a reflection symmetry ofF(A,b,ℓ,u,c). Then, consider the split
reformulationF S(A,b,ℓ,u,c). We argued earlier that for the split permutation there exist
permutation matrices bC1 and bD1 whose application toFS(A,b,ℓ,u,c)yields the following
linear program, see e.g. (7). Here,bC1 corresponds to the permutation that swapsv+ andv−
ifγ v =−1holds, and bD1 corresponds to the permutation that swapsw+ andw− ifλ w =−1
holds.
min(Λc)⊺bxλ−(Λc) ⊺bx−λ (11a)
 ΓAΛ−ΓAΛ
−ΓAΛ ΓAΛ
 bxλ
bx−λ

=
 Γb
−Γb

(11b)
O≤
bxλ
bx−λ

≤
 bs(ℓ,u,λ)
bs(ℓ,u,−λ)

(11c)
Then, we define permutation matricesbC2 :=
CO
OC

and bD2 :=
DO
OD

and apply them
to (11). Doing so, we obtain the linear program:
min(D−1Λc)⊺bxλ−(D−1Λc)⊺bx−λ (12a)
 CΓAΛD−CΓAΛD
−CΓAΛD CΓAΛD
 bxλ
bx−λ

=
 CΓb
−CΓb

(12b)
O≤
bxλ
bx−λ

≤
 D−1bs(ℓ,u,λ)
D−1bs(ℓ,u,−λ)

(12c)
Then, since(γ,λ,C,D)is a reflection symmetry, it follows by substitution thatCΓAΛD=
A,CΓb=b,D −1bs(ℓ,u,λ) =u,D −1bs(ℓ,u,−λ) =−ℓ. Using these substitutions, (12) is
identical toFS(A,b,ℓ,u,c,), without reordering the indices. Thus, the permutation matrices
bC := bC2bC1 and bD := bD1bD2 form a permutation symmetry(bC, bD)ofF S(A,b,ℓ,u,c).□
By Theorem 23, the reflection symmetries of a linear program are captured
completely by the permutation symmetries of its split reformulation. In section 7.2
in [11], it is argued that for any linear program, performing the reduction from
Proposition 3 using equitable partitions generalizes the projection to the fixed space
of the symmetry group formed by the permutation symmetries. Although we do
not show it formally, the permutation symmetries that we exhibit in the proof
33
of Theorem 23 are bound-respecting, as they act similarly on the positive and nega-
tive variables of the split reformulation. As a consequence, the symmetry subgroup
of the split reformulation corresponding to any permutation symmetries derived
from reflection symmetries generates a bound-respecting equitable partition of the
split reformulation. Thus, by computing bound-respecting equitable partitions of the
split reformulation, our approach generalizes the projection to the fixed space of the
symmetry group formed by reflections symmetries.
As is also remarked in [11], equitable partitions may also occur even if there is no
symmetry. Next, we show an example where this occurs for the split reformulation of
a general class of matrices that does not necessarily contain symmetries.
Example 24LetA∈{0,1} m×n be a matrix with two non-zero entries in each row. The
matrixAdoes not necessarily contain any symmetries, and we can consider the following
linear program with no objective.
Ax=1
O≤x≤1
Then, centering the linear program usingδw := 1
2 for allw∈Wyields the following linear
program.
Ax=O
−1
2≤xw≤ 1
2 ∀w∈W
Its split reformulation is given by
Ax+−Ax− =O
−Ax+ +Ax− =O
0≤x +
w≤ 1
2 ∀w∈W
0≤x −
w≤ 1
2 ∀w∈W
Then, since the objective and right-hand sides are all zero and the variable bounds are
identical, the coarsest equitable partition of this linear program has a single bipolar variable
part and a single bipolar row part, even though the original LP does not in general contain
any symmetries.
