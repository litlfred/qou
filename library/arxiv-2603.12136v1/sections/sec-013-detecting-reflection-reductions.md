---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-013-detecting-reflection-reductions
section_title: "Detecting reflection reductions"
section_number: null
pages: 34-37
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
In order to detect reflection reductions, it suffices to compute symmetric equitable
partitions of the split reformulation form by Theorem 19. Thus, we can directly reuse
the algorithm formulated in [11], which relies on the fast color refinement algorithm
by Paige and Tarjan [35]. Since the split reformulation consists of four copies of the
constraint matrix, we can detect symmetric equitable partitions, and thus reflection
reductions, in identical asymptotic worst-case time and space complexity as in [11].
34
Theorem 25For a linear programF(A,b,ℓ,u,c)withA∈R V×W , letmbe the total
bitlength of the entries of


ℓ⊺ 0
u⊺ 0
c⊺ 0
A b

 and letn=|V|+|W|. Forδwith total bitlength
O(m), a reflection reduction(P,Q,γ,λ,δ,V U,WU)ofF(A,b,ℓ,u,c)can be determined in
O((n+m) logn)time andO(n+m)space.
ProofWe assume that the constraint matrix is given in a sparse format such as the CSR
and/or CSC format. First,F(A,b−Aδ,ℓ−δ,u−δ,c)can be computed inO(n+m)time
and space and has bitlengthO(m), where we use thatδhas bitlength of orderO(m). Then,
the split reformulationFS(A,b−Aδ,ℓ−δ,u−δ,c)can also be computed inO(n+m)time
and space and has bitlength of orderO(m). The initial symmetric equitable partition can be
determined in andO(n+m)time andO(n+m)space by using standard hashing techniques.
Then, computing the coarsest symmetric equitable partition of the split reformulation takes
O((n+m) logn)time andO(n+m)space [11, Theorem 3.1]. Using the symmetric equitable
partition, we can directly derive a reflection reduction inO(n+m)time and space. Summing
up all steps, we obtain a worst-case time complexity ofO((n+m) logn)time and a worst-case
space complexity ofO(n+m).□
In Theorem 25, we assumed that the offsetδhas bitlength that is of the same
order asF(A,b,ℓ,u,c). This is a reasonable choice, as bothδC andδS have encoding
lengths bounded by the encoding length ofℓanduby their definition.
Although the running time is asymptotically equivalent to the ‘ordinary’ equitable
partition algorithm presented in [11], computing equitable partitions of the split
reformulation, which has 4 times as many nonzero entries, may still be undesirable
in practice. To reduce the running time by a constant factor one can exploit the
structure of symmetric equitable partitions. We formulate a refinement algorithm
that computesγandλthat runs on the original matrix but models the refinement
algorithm that computes a symmetric partition on the split reformulation. This
closely follows the argumentation presented in Lemma 12 and Lemma 13. The core
idea to achieve this constant-factor improvement is to refine unipolar part pairs at
the same time, as is also done in the proof of Lemma 13. The implemented algo-
rithm is very similar to that in [11], who use the algorithm in [42] which provides a
thorough description of the fast color refinement algorithm. Since the algorithm we
present does not have a better asymptotic running time, we outline the main changes
and adaptations compared to the description in [11] here without proof.
For the data structures, we add arrays to trackλ,γand the type (unipolar or
bipolar) of each part, which takesO(n)space. The signsλw andγ w are used during
the computation of the column and row sums for equitability. Then,λandγare
determined whenever a bipolar partPis turned into a unipolar one or at initialization.
Initially, we compute the affine transformation given byδ C. Then, we com-
pute an initial symmetric bound-respecting partition of the split reformulation as in
Lemma 12, which can be achieved in linear time by using hashing techniques. For a
rowv∈V, we initialize it to be bipolar ifbv = 0holds. Otherwise, the row is marked
35
as unipolar and grouped with other rows based on the absolute values|bv|of the
right-hand side.
For a variablew∈W, we initialize them it to be bipolar ifcw = 0and−ℓ w =u w
hold. Otherwise, we let them be unipolar, and compute signsλw that so that variables
whose objective and bounds can be mapped to each other by negation are put into
the same initial part.
For the subsequent refinement of the constraint matrix we change the behavior
slightly based on the type of each part. The changes are similar to those described in
the proof of Lemma 13. When refined, unipolar parts retain their type, but bipolar
parts may be refined into smaller parts that may be either unipolar or bipolar. When
a bipolar part is refined into a unipolar part, the signsλorγare determined from its
elements based on the column or row sums. In our refinement algorithm, we partition
the columns (rows) of a bipolar part based on the absolute value of the sums, rather
than the sums directly as in the refinement algorithm in [11]. Then, we set the signs
λw so that the column sums are all positive when multiplied byλw. Finally, one
improvement that is directly suggested by Corollary 10 is that ifPis a bipolar type,
that then cMP,Q is an equitable block for anyQ∈Q. Thus, we do not need to add
bipolar parts to the search stack, since checking them for refinements is pointless.
There are two cases where one needs to be careful with the adapation of the color
refinement algorithm to the reduced matrix size. First, if a bipolar part contains row
or columns sums with identical but nonzero values, then it must be converted to a
unipolar part and added to the search stack. Second, we note that one has to be careful
with the ‘leave largest refined part out’-rule that is used in most color refinement
algorithms and is key to the fast running time of color refinement [36]. This rule
pushes all but the largest part obtained by a refinement of a part to the stack of parts
for which refinements need to be checked. Since we are modeling the refinement of
symmetric partitions of the split reformulation, we cannot leave out a unipolar part
in the algorithm that runs on the original matrix since it represents two parts in the
split reformulation, and leaving out both parts would break correctness. Luckily, this
does not lead to a slower running time, since the running time is still guaranteed
by Theorem 25 as we maintain the invariant that our partition models a symmetric
partition of the split reformulation.
Choosingγ,λandδ
One detail that is important for a practical implementation is the choice ofδ. Ifδhas
many nonzero entries and the matrixAhas large values, then the productAδthat
appears in the right-hand side of the reflection reduced model can become very large
and lead to numerical issues.
Recall that theγandλvectors that were generated by the symmetric equitable
partition were not unique, and could be optionally negated for each partP∈PU and
Q∈Q U. In order to minimize the number of complemented rows, we chooseγso that
for eachP∈P U at least|P|
2 rowsv∈Phave valueγ v = 1. Similarly, we minimize
the number of complemented variables by pickingλsuch that for eachQ∈Q U at
least |Q|
2 variablesw∈Qhave valueλ w = 1.
36
As a starting point for ourδvector we considerδ S as defined in Corollary 21.
However, this vector may still not be very sparse due to theℓw andu w values. By
Theorem 20, we may modifyδS toδ :=δS +(Λν,O)for anyQ U-equitable vectorν. In
our implementation, we chooseνso thatδbecomes sparse. For every partQ∈QU, we
compute how often the valueλwδS
w appears for allw∈Qand setν Q to be the negative
of the most frequently appearing value. This way, most variablesw∈Qsatisfy
δw =δS
w +λwνw =δS
w +λw(−λwδS
w) =δS
w−δS
w = 0.
Thus, the resultingδvector is typically quite sparse. Furthermore, we remark that for
a unipolar variablew∈Wwith integral bounds,δ S
w is also integral. One important
consequence is that if all variables in some partQ∈QU have integral bounds, then
δQ is also integral. Although we cannot modifyδS
w for variableswin bipolar parts,
these values do not lead to numerical issues as fixing the corresponding values does
not affect the right-hand sides since the corresponding parts have zero sums due to
bipolarity.
