---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-017-detecting-drcr-for-mixed-integer-linear-programs
section_title: "Detecting DRCR for mixed-integer linear programs"
section_number: null
pages: 48-55
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
Next, let us formulate an algorithm to detect the reductions described in Theorem 26.
To achieve such a reduction, we need to balance two conditions: we would like the
partitionQto be as coarse as possible, but (13) must also hold. These two objec-
tives naturally conflict with each other, as a coarse partition of the integer variables
requires us to find an affine TU decomposition with fewer integrality constraints.
Although one could consider the coarsest possible partition and simply try to detect
an affine TU decomposition and apply Theorem 33 and Theorem 32, it is unlikely
that (13) holds, either by the structure of the problem or by additional symmetries.
For the example of the generalized assignment problem in Section 4.2, if two bins
have identical capacities then the symmetries that permute the two bins imply that
48
(13) is not satisfied for the coarsest equitable partition.
In order to detect an affine TU decomposition that we can use, we attempt
to detect the structure of Theorem 33 whereTis given by(Π ⊺
QΛxWU )Q′,⋆, where
Q′⊆{Q∈Q I||Q|>1}. Note that the columns ofTconsist of unit vectors, which
may have been negated. Forw∈W 2 we have for its column inTthatT ⋆,w =λ we Q
holds forQ∈Q ′ such thatw∈Q, wheree Q is a unit vector. Then it follows that
B⋆,w = (S+UT) ⋆,w =S ⋆,w +UT ⋆,w =S ⋆,w +λwU⋆,Q holds. Since we wantSto be
part of the totally unimodular matrix, its entries are±1values. Thus, if a column
B⋆,w contains large entries these must come from theU ⋆,Q vector. Furthermore,
note that for all columns in the blockQ, its entries must differ by at most1from
λwU⋆,Q. Thus, columns inB ⋆,Q must differ by at most1up to±1scaling. For
example, ifQcontains some block(P,Q)∈P×Qsuch thatB P,Q =

3 0
0 3

, then
it is impossible to constructUandSsuch that we can getB=S+UT, since
BP,w1−BP,w2 /∈{−1,0,1}P implies that there exists no choice ofU⋆,Q such that we
can construct a totally unimodular matrixS.
For a matrixA∈R V×W , we define thenonternary maskntmask(A)∈R V×W
such thatntmask(A) v,w :=
(
0if|A v,w|= 1
Av,w otherwise holds for allv∈Vandw∈W.
Then, if two columns ofBhave the same nonternary mask up to±1scaling, they
are candidates to belong to the same partQ∈Q. In order to generate equitable
partitions which satisfy this condition, we change the initial partition that we pass to
the color refinement algorithm to only place two integer columnsw1 andw 2 in the
same initial partQ∈Q 0 ifntmask(A ⋆,w1) =±ntmask(A ⋆,w2)holds. Using standard
hashing techniques, this can be done in linear time, see [28] for further details. The
condition that the nonternary masks are equivalent requirement is a sufficient condi-
tion to ensure thatSis a ternary matrix, but not a necessary one. For example, we
have

3 2
2 3

=

1 0
0 1

+

2 2
⊺
1 1

where the
S T⊺
matrix is given by the totally
unimodular matrix

1 0 1
0 1 1
⊺
but the two nonternary masks of the original columns
differ.
Then, consider the second condition thatE=RTholds. Forv∈Vandw∈W
we haveEv,w = (RΠ⊺
Qλ)v,w =R v,Qλw forQsuch thatw∈Q, which only holds if the
columns inE⋆,Q are identical up to±1scaling. Thus, we require thatE⋆,w =±E ⋆,w′
holds for allw,w′∈Q.
Although totally unimodular matrices can be detected in polynomial time [49],
current implementations still have quintic time complexity [50], which is too slow for
practical purposes. Instead, we focus onnetwork matricesand their transposes, which
form large subclasses of totally unimodular matrices [33]. We use the fast column
augmentation algorithms by Bixby and Wagner for network matrices [31] and the
49
algorithm by van der Hulst and Walter for transposed network matrices [32]. For a
(transposed) network matrixM∈R V×W and a columnu∈R V, both algorithms are
given by a procedureAugmentNetwork(M,u)that returns whether the augmented
matrix
M u
is a (transposed) network matrix, growing the (transposed) network
matrix by one column. The operation ofaugmentinga column to a matrixMturns
Minto
M u
.
Then, we are ready to describe an algorithm that detects the conditions of
Theorem 26 by simultaneously computing a reflection reduction and an affine TU
decomposition of the MILP. The algorithm is described in Algorithm 1 and consists
of roughly five steps.
In the first step, we determine the row partition that is used for Theorem 33,
by partitioning the rows according to whether they contain non-integral entries or
right-hand side. Then, we determine for each of the the connected components of the
submatrix formed by the continuous columns that is in the integral part whether it
is (transposed) network. These components form theC-matrix in Theorem 33. This
step is identical to part of the algorithm described in [29] to detect implied integrality
using totally unimodular submatrices.
In the second step, we use the computed row partition for Theorem 33 to com-
pute an initial partition that we pass to the color refinement algorithm. As discussed
above, we put two columns in the same partition only if they are (up to±1scaling)
identical in the non-integral rows and if their nonternary masks are identical (up to
±1scaling) in the integral rows. In the third step, we compute a reflection reduction
given this initial partition.
For the fourth step, we consider the computed reflection reduction and
attempt to construct a matching affine TU decomposition using Theorem 33 that
extends the computed reduction to integer variables. For everyQ∈ Q ′, where
Q′ :={Q∈ Q I | |Q|>1}, we consider adding a columnuto theUmatrix of
the affine TU decomposition. For our approach in Algorithm 1, we simply check if
Av,Q =αλ Q holds for someα∈R\{0}. If so, then we setu v =α v. Then, we use
S⋆,Q =A ⋆,Q−u(Π ⊺
QΛ)⋆,Q This effectively cancels thev’th row ofA⋆,w by usingu. If
u=O, then we do not need the additional row ofΠ QΛto cancel any rows, and the
additional row in theTpart of the affine TU decomposition can only harm detection
of total unimodularity, as any submatrix of a TU matrix is TU. In this case, we
consider the partition of the subsetQ′\{Q}rather thanQ ′, which is sufficient by
Theorem 32, and we do not add the corresponding row to theTmatrix. Finally, we
ensure that for the affine TU decompositionE=RTholds by checking ifSVR,Q =O
holds, i.e. that all rows inVR are properly canceled.
50
Algorithm 1:Detecting DRCR for MILP using affine TU decompositions.
Algorithm:DRCR(A,b,ℓ,u,c,W I)
Input:Constraint matrixA∈R V×W , right-hand sideb∈R V, lower boundsℓ∈R W, upper
boundsu∈R W, objectivec∈R W and integer variablesWI⊆W
Output:A reflection reduction(P,Q,λ,γ,δ,V U,WU)such that the conditions of Theorem 26 hold.
1V R←{v∈V|b v /∈Zora v,w /∈Zfor somew∈W};
2LetKbe the set of connected components ofA V,W\WI;
3LetMdenote the (transposed) network matrix that is constructed;
4forK∈Kdo
5ifV R∩VK̸=∅then
6V R←VR∪VK;
7continue
8end
9isNetwork←True;
10forw∈W K do
11ifnotAugmentNetwork(M,A ⋆,w)then
12isNetwork←False;
13break
14elseAugmentMwithA ⋆,w ;
15end
16ifnotisNetworkthen
17V R←VR∪VK;
18Remove fromMany columns ofA ⋆,WK that were augmented;
19end
20end
21LetQ 0 be a partition ofWsuch thatQ∩W I =∅orQ⊆W I holds for allQ∈Q 0. Additionally,
we impose the condition that for allQ⊆WI,w,w ′∈Qholds if and only ifA VR,w =±AVR,w′
andntmask(A V\VR,w) =±ntmask(AV\VR,w′)hold;
22LetP 0←{V};
23(P 1,Q 1,λ,γ,δ,V 1
O,W 1
O)←ReflectionRefinement(P 0,Q 0,A,b,ℓ,u);
24SortQ 1 by descending size|Q|of its partsQ∈Q 1;
25forw∈W\W 1
O do
26ifnotAugmentNetwork(M,A ⋆,w)thenQ 1←Q 1∪{w};
27elseAugmentMwithA ⋆,w;
28end
29forQ∈Q 1 such thatQ⊆W I and|Q|>2do
30LetV cancel :={v∈V|A v,Q =αvλQ for someαv∈R\{0}}and letu∈R V be such that
uv =αv ifv∈V cancel andu v = 0otherwise.;
31LetS=A ⋆,Q−u(Π ⊺
QΛ)Q and letM′∈R (V∪Q 1 )×Q usingM ′←
 S
O |Q1|×Q

;
32ifS VR,⋆̸=Othen
33ModifyQ 1 by splittingQinto|Q|parts that contain its individual elements;
34continue
35end
36ifV cancel̸=∅thenUpdateM ′
Q1,Q←(Π ⊺
QΛ)Q ;
37isNetwork←True;
38forw∈Qdo
39ifnotAugmentNetwork(M,M ′
⋆,w)then
40isNetwork←False;
41break
42elseAugmentMwithM ′
⋆,w ;
43end
44ifnotisNetworkthen
45Remove fromMany column that was augmented fromM ′;
46ModifyQ 1 by splittingQinto|Q|parts that contain its individual elements;
47end
48end
49(P 2,Q 2,λ,γ,δ,V 2
O,W 2
O)←ReflectionRefinement(P 1,Q 1,A,b,ℓ,u);
50return(P 2,Q 2,λ,γ,δ,V 2
O,W 2
O);
51
In the fifth and final step, we consider allQ∈Qthat could not be added to the
affine TU decomposition. For each such a partQ, weindividualizeit by splittingQ
into|Q|parts where each element is in its own part of size1, and run the refine-
ment algorithm again. Note that this final refinement may refine ‘good’ parts that we
computed the affine TU decomposition for previously into several parts. This is unfor-
tunate, as it may adjust the requirements for theTmatrix, and break the affine TU
decomposition. An example of this phenomenon is shown in Example 34. However, we
show in Lemma 35 that, because the new partitionQis a refinement of the previous
partition, (13) is still satisfied and we can still recover solutions in polynomial time.
Example 34We consider a run of Algorithm 1 on the mixed-integer linear programconv({x∈
R6|Ax=b,x≥0}∩Z 6)where
A=


2 2 2 2 3 3
1 0 1 0 1 0
0 1 0 1 1 0
0 1 1 0 0 1
1 0 0 1 0 1
1 0 0 0 1 0
0 1 0 0 1 0
0 0 1 0 0 1
0 0 0 1 0 1


∈Z 9×6 andb=


8
2
2
2
2
1
1
1
1


∈Z 9.
We usev i to indicate thei’th row index andw j to indicate thej’th col-
umn index. The partition returned byReflectionReductionis given byP 1 =
{{v1},{v 2,v 3,v 4,v 5},{v 6,v 7,v 8,v 9}}andQ 1 ={{w 1,w 2,w 3,w 4},{w 5,w 6}}. ConsiderQ :=
{w1,w 2,w 3,w 4}, and note thatA ⋆,Q admits an affine TU decomposition usingA ⋆,Q =
 O 1×4
AV\{v 1},Q

+
 2
O 8×1

1 1 1 1

, where it can be verified that the matrix


O 1×4
AV\{v 1},Q
1 1×,4

 is
totally unimodular. Thus, initially, Algorithm 1 will reformulate the integrality constraints
onQ. Then, Algorithm 1 attempts to reformulate the integrality constraints for{w5,w 6}and
fails to do so. Thus, we refine{w5,w 6}into{w 5},{w 6}, and runReflectionReduction
again, which results in the partition given byP2 ={{v 1},{v 2,v 3},{v 4,v 5},{v 6,v 7},{v 8,v 9}}
andQ 2 ={{w 1,w 2},{w 3,w 4},{w 5},{w 6}}. Note forQ2 thatQis now split up into the two
parts{w 1,w 2}and{w 3,w 4}. However, this also affects the affine TU decomposition that
we previously computed, as the matrixΠ⊺
Q that represents theTmatrix in the affine TU
decomposition is refined fromΠ⊺
Q1
toΠ ⊺
Q2
, where the nonzero submatrix onQchanges from
1 1×4 to
1 1 0 0
0 0 1 1

. Unfortunately, the matrix


0 0 0 0
AV\{v 1},Q
1 1 0 0
0 0 1 1

 is not totally unimodular, which
invalidates the previously computed affine TU decomposition. Thus, it may be the case that
after a run of Algorithm 1 that the affine TU decomposition that is computed no longer
matches the equitable partition, due to the additional refinements that are computed in line
49 of Algorithm 1.
52
Lemma 35Let(P 1,Q 1,γ 1,λ 1,δ,V 1
O,W 1
O)be a reflection reduction ofG:=P(A,b,ℓ,u)and
let it be given that for somecQ1⊆Q 1
I thatH d :={x∈G|(Π ⊺
Q1Λ1xW 1
O
)cQ1 =d}is aW I-
integral polyhedron for alld∈Z
cQ1
. Consider any refinement(P 2,Q 2,λ 2,γ 2,δ,V 2
O,W 2
O)of
the given reflection reduction wherebQ2⊆Q 2 corresponds to the parts that were refined from
bQ1 such thatS
Q∈bQ2Q= S
Q∈bQ1Qholds. Then,(13)holds for the refined reduction, i.e. we
have:
conv(G∩MIWI ) = conv({x∈G|(Π ⊺
Q2Λ2xW 2
O
)Q2
I
∈ZQ2
I}) = conv({x∈G|(Π ⊺
Q2Λ2xW 2
O
)cQ2∈Z
cQ2
}),
ProofFirst,letusshowafewfactsabouttherefinedreduction(P 2,Q 2,λ,γ,δ,V 2
O,W 2
O).First
of all, note thatP2 andQ 2 must refineP1 andQ 1 respectively, and we must haveW1
O⊆W 2
O
since additional refinements can only turn bipolar variables into unipolar variables, but not
the other way around. Furthermore, note that additional refinements cannot change the value
ofλ 1w forw∈W 1
O, since the relative signs of unipolar parts are fixed. Thus,λ1 =λ 2
W 1
O
holds. By design of our algorithm,δis constant in both reductions. Then, we claim that the
following holds:
G∩MI WI⊆{x∈G|(Π ⊺
Q2Λ2xW 2
O
)cQ2∈Z
cQ2
}⊆{x∈G|(Π ⊺
Q1Λ1xW 1
O
)cQ1∈Z
cQ1
}.
Here, the first inclusion follows sinceΠ⊺
QΛ2 is an integral matrix. For the second inclusion,
consider anyx∈{x∈G|(Π ⊺
Q2Λ2xW 2
O
)cQ2∈Z
cQ2
}. Then, consider anyQ∈ cQ1. SinceQ 2
refinesQ 1, there exist partsQ′
i∈ cQ2 fori= 1,···,ksuch that Sk
i=1Q′
i =Qholds. Then,
we can derive that:
(Π⊺
Q1Λ1xW 1
O
)Q =
X
w∈Q
λ1
wxw =
kX
i=1
X
w∈Q′
i
λ1
wxw
(a)
=
kX
i=1
X
w∈Q′
i
λ2
wxw =
kX
i=1
(Π⊺
Q2Λ2xW 2
O
)Q′
i
,
where (a) holds sinceλ1 =λ 2
W 1
O
holds, and the final expression is integral by integrality of
(Π⊺
Q2Λ2xW 2
O
)Q′
i
, using thatQ′
i∈ cQ2.
Taking convex hulls, we note that by applying Lemma 31, usingWI-integrality ofHd, we
have equality throughout:
conv(G∩MIWI ) = conv({x∈G|(Π ⊺
Q2Λ2xW 2
O
)cQ2∈Z
cQ2
}) = conv({x∈G|(Π ⊺
Q1Λ1xW 1
O
)cQ1∈Z
cQ1
}).
Finally, we have the following inclusions:
G∩MI WI⊆{x∈G|(Π ⊺
Q2Λ2xW 1
O
)Q2
I
∈ZQ2
I}⊆{x∈G|(Π ⊺
Q2Λ2xW 2
O
)cQ2∈Z
cQ2
},
taking convex hulls and noting that the first and last sets are equal, we again have equality
throughout, which concludes the proof
conv(G∩MIWI ) = conv({x∈G|(Π ⊺
Q2Λ2xW 1
O
)Q2
I
∈ZQ2
I}) = conv({x∈G|(Π ⊺
Q2Λ2xW 2
O
)cQ2∈Z
cQ2
}),
□
It is not too difficult to see that finding a solution to the original problem can also
still be done in polynomial time by simply considering the fiberHd defined where
the affine subspaces are defined byΠ1
QΛ1xW 1
O
=d. In Example 34, this corresponds
to adding the equalityx 1 +x 2 +x 3 +x 4 =y 1,2 +y 3,4 in the postsolve procedure
53
rather than the two equalitiesx1 +x 2 =y 1,2 andx 3 +x 4 =y 3,4 which are shown to
be problematic in Example 34. Although the latter two equalities clearly imply the
former equality, adding them to the linear program breaks the integrality guarantee.
Next, let us consider the total runtime. As for linear programs, we assume that
the reflection reduction uses aδ-vector whose bitlength is of the same order in the
worst-case, which is reasonable as the choice forδthat is described in Corollary 21
satisfies this assumption.
Theorem 36For a mixed-integer linear programF(A,b,ℓ,u,c)withA∈R V×W and integer
variablesW I⊆W, letmbe the total bitlength of the entries of


ℓ0
u0
c0
A b

 and letn=|V|+|W|.
Assuming thatReflectionRefinementcomputes aδwith total bitlengthO(m), Algorithm 1
computes a reflection reduction(P,Q,γ,λ,δ,V U,WU)ofF(A,b,ℓ,u,c)such that(13)holds,
i.e.:
conv({x∈P(A,b,ℓ,u)|(Π ⊺
QΛx)QI∈ZQI}) = conv(P(A,b,ℓ,u)∩MI WI )
inO(n+m)space andO((n+m) logn)time using network matrices orO(n 2α(n,n) +
mlog(n))time using transposed network matrices.
ProofWe do not provide a complete proof of every step here, but instead emphasize the most
relevant parts of the correctness proof and the running time. First let us prove correctness.
In lines 1-20, we compute the connected components of the continuous variables that are
(transposed) network, which is necessary to compute our affine TU decomposition. Then, we
compute an initial reflection reduction in lines 21-23, whereQ1 satisfies the following for all
Q∈Q 1:
1. EitherQ∩W I orQ⊆W I holds.
2. IfQ⊆W I, thenAVR,w =±AVR,w′ andntmask(AV\VR,w) =±ntmask(AV\VR,w′)hold
for allw,w′∈Q.
In lines 24-48, we greedily construct an affine TU decomposition that satisfies the conditions
ofTheorem33wherewekeeptheinvariantthatTisequalto(Π ⊺
Q1Λ)Q forsomeQ ′⊆Q 1.The
construction uses condition 2. by testing if the vector
 AVR,w
ntmask(AV\VR,w)

, which is identical
up to±1scale for allw∈Qby construction, can be used to augment the (transposed)
network matrix in the affine TU decomposition. Our construction does not always add such
a column tou: we determine dynamically if this is necessary by checking ifV cancel ̸=∅
holds. If an additional column in theU-matrix is needed, we addQtoQ ′ and add the
row(Π ⊺
Q1Λ)Q toT. Otherwise, we leaveQ′ andTunchanged. By doing so for all columns,
we ensure thatT= Π ⊺
Q′Λholds. For anyQ∈Q 1 that can not added to the affine TU
decomposition, we simply split it into single-variable parts inQ1 to satisfy the conditions
of the affine TU decomposition. Then, it follows from Theorem 33 and Theorem 32 that for
Q1
I ={Q∈Q 1|Q⊆W I}we have:
conv({x∈P(A,b,ℓ,u)|(Π ⊺
Q1Λx)Q1
I
∈ZQ1
I}) = conv(P(A,b,ℓ,u)∩MI WI ).(19)
54
Finally, we refineQ1 toQ 2 in 49 to ensure thatQ2 corresponds to a reflection reduction. By
(19) and the fact thatQ2 refinesQ 1, Lemma 35 shows forQ2
I :={Q∈Q 2|Q⊆W I}that
conv({x∈P(A,b,ℓ,u)|(Π ⊺
Q2Λx)Q1
I
∈ZQ2
I}) = conv(P(A,b,ℓ,u)∩MI WI ).
Then, since(P 2,Q 2,λ,γ,δ,V 2
O,W 2
O)is a reflection reduction ofF(A,b,ℓ,u,c), it follows
that the conditions of Theorem 26 hold. Thus, we have shown correctness of Algorithm 1.
Next, let us consider the running time and space-complexity of Algorithm 1. First of all,
ReflectionRefinementruns inO((n+m) log(n))andO(n+m)space by Theorem 25 and
is called twice. Note that we use the fact thatδhas bitlength at mostO(m).
At the start of the Algorithm 1, we compute the connected components of the submatrix
formed by the continuous columns. This can be done inO(n)time and space by using a
depth-first search.
Computing the initial partitionQ0 can be done inO(n+m)time and space by using
standard hashing techniques. SortingQ1 can be done inO(nlog(n))time.
Finally, we note thatAugmentNetworkis called at most once for every column. The
matrixMhas size(|V|+|Q|)×|W|, which is of the orderO(n)×O(n). Moreover,MhasO(m)
nonzeros as it has fewer nonzeros thanA, since we only add the additional row of(Π⊺
QΛ)Q
for allQ∈Qif it can be used to cancel one or more rows fromA⋆,Q. We note that regardless
of the size of the nonzero entries, one can check in constant time if a nonzero has value±1.
For network matrices the column augmentation algorithm by Bixby and Wagner then runs in
O(mα(m,n))time, whereαis the inverse Ackermann function, which grows extremely slowly
and is dominated by the orderO((n+m) log(n))running time for the reflection reduction.
The transposed network algorithm by van der Hulst and Walter runs inO(n2α(n,n))time,
and dominates the total runtime in case it is used. Taking the bitlengthminto account, we
can simplify toO(n2α(n,n) +mlog(n))in this case.□
