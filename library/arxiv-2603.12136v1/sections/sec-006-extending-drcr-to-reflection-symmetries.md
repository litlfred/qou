---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-006-extending-drcr-to-reflection-symmetries
section_title: "Extending DRCR to reflection symmetries"
section_number: null
pages: 10-13
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
As mentioned in the introduction, the DRCR algorithm presented in [11] only detects
automorphisms that arise from permutation matrices, whereas the theory they for-
mulate supports more general linear symmetries of the constraint matrix. In [4] it is
shown that for linear programs the projection to the fixed space of the symmetry
group works for any linear group, rather than just the symmetries arising from
permutation matrices. The algorithm presented in [4] uses reflection symmetries gen-
erated by the signed permutation group to solve highly symmetric integer programs.
Reflection symmetries generalize permutation symmetries to signed permutations
and additionally take the action of complementing a variablextou−xinto account,
whereuis its upper bound.
Most MILP solvers and LP solvers only perform symmetry handling for permu-
tation symmetries. SCIP is a notable exception, as it handles reflection symmetries
since version 9.0 [40]. More information on how reflection symmetries are detected
and handled in SCIP can be found in [2]. As far as we are aware, the only other
work that treats reflection symmetries computationally for MILP solvers is by
Christophel, Güzelsoy and Pólik [41] and explores how reflection symmetries may be
used in primal heuristics. Reflection symmetries that are not permutation symme-
tries are somewhat uncommon in Mixed Integer Programs; Hojny [2] reports that
10
they were detected for only 60 out of 1055 tested MIPLIB 2017 instances and 6 out
of 486 tested MINLPLIB instances, and that handling of reflection symmetries for
mixed-integer linear programs does not produce large speedups. In fact, the default
settings for symmetry handling in SCIP 9.0 disable the detection and handling of
reflection symmetries. This can perhaps be explained by the interesting result by
Geyer, Bulutoglu and Ryan [37], who show that for feasible linear programs that are
full-dimensional and do not contain redundant inequalities, permutation symmetries
can be used to detect the complete linear symmetry group of the linear program. To
do so, they first normalize the linear program using a singular-value decomposition
and then formulate a complicated algorithm to detect the full symmetry group. They
also detect reflection symmetries and exploit them in an enumeration procedure for
an integer linear program used for classifying orthogonal arrays.
As our first contribution, we will show that DRCR can be extended to detect
reductions that take the complements of every variable into account. We will con-
sider the original linear program given byF(A,b,ℓ,u,c), and transform it to obtain
a representation where DRCR is more effective. Our approach somewhat resembles
the detection strategies in [2, 41], which both reduce the problem of finding reflection
symmetries to finding permutation symmetries by adding both the original and the
complemented variables to the auxilliary graph used for symmetry detection. We will
use two transformations to achieve something similar using DRCR. First, the origin
is moved to the center of the variable domains using an affine transformation, so that
ℓ≤x≤uis transformed into−ν≤x ′≤ν, whereν= u−ℓ
2 . Then, each variablex′
w
forw∈Wis split into two variablesx ′+
w andx′−
w such thatx′
w =x′+
w −x′−
w holds,
where0≤x ′+≤νand0≤x ′−≤νhold. Crucially, we show that by computing
an equitable partition on this linear program withx′+ andx′−, one can recover the
best equitable partition possible for the original linear program under the operation
of complementing the variables.
We illustrate the main ideas of our method with an example linear program given
in (3).
minx 1−x 2 (3a)

2 1 1
−1−2−1
−1 1 0




x1
x2
x3

≤


5
−3
1

 (3b)
0≤x i≤2∀i∈{1,2,3}(3c)
The polyhedron that defines the feasible region of (3) has two reflection symme-
tries, one reflection in the hyperplanex1 +x 2 = 2and one reflection in the hyperplane
x3 = 1. We will show how both symmetries can be projected out by considering a
reformulation of (3). First, we apply an affine transformation to (3) that yields vari-
ables that have identical negative and positive domain sizes by substitutingx=x′+1.
Furthermore, we add the slack variablessto turn the inequalities into equalities.
11
minx′
1−x′
2 (4a)


2 1 1 1 0 0
−1−2−1 0 1 0
−1 1 0 0 0 1




x′
1
x′
2
x′
3
s1
s2
s3


=


1
1
1

 (4b)
−1≤x ′
i≤1∀i∈{1,2,3}(4c)
si≥0∀i∈{1,2,3}(4d)
Next, we introduce redundant variables and constraints in the following manner.
First, we split each variablex′
w usingx′
w =x′+
w−x′−
w forw∈{1,2,3}. After doing so,
we additionally add a negated copy of each equation. Then, the mappings defined by
x′
w←x′+
w−x′−
w and(x′+
w,x′−
w )←(max(x w,0),max(−x w,0))can be used to show that
feasibility and optimality are preserved. This yields the following equivalent linear
program, which we will call thesplit reformulationmore generally.
minx′+
1 −x′−
1 −x′+
2 +x′−
2 (5a)


2 1 1−2−1−1 1 0 0
−1−2−1 1 2 1 0 1 0
−1 1 0 1−1 0 0 0 1
−2−1−1 2 1 1−1 0 0
1 2 1−1−2−1 0−1 0
1−1 0−1 1 0 0 0−1




x′+
1
x′+
2
x′+
3
x′−
1
x′−
2
x′−
3
s1
s2
s3


=


1
1
1
−1
−1
−1


(5b)
0≤x ′j
i ≤1∀i∈{1,2,3},∀j∈{+,−}(5c)
si≥0∀i∈{1,2,3}(5d)
Next,wecomputetheequitablepartitionofthesplitreformulation (5).Wereorder
the variables to clarify the partition.
x′+
1 x′−
2 x′−
1 x′+
2 x′+
3 x′−
3 s1 s2 s3








2−1 −2 1 1−1 1 0 0 1
−1 2 1−2 −1 1 0 1 0 1
−1−1 1 1 0 0 0 0 1 1
−2 1 2−1 −1 1 −1 0 0−1
1−2 −1 2 1−1 0−1 0−1
1 1 −1−1 0 0 0 0 −1−1
12
Then, we apply Proposition 3 to the given equitable partition. Doing so aggregates
some of the positive and negative index variables with each other.
miny 1+,2−−y 1−,2+ (6a)


1−1 0 1 0
−1 1 0 0 1
−1 1 0−1 0
1−1 0 0−1




y1+,2−
y1−,2+
y3+,3−
s1,2
s3


=


2
1
−2
−1

 (6b)
0≤y 1+,2−,y 1−,2+,y 3+,3−≤2(6c)
s1,2,s 3≥0(6d)
(6e)
We can notice two things about (6). First of all, we note thaty3+,3− vanishes from
the given equations and thus any0≤y3+,3−≤2is always feasible, so we may remove
it from the Linear Program. This corresponds to removing the reflection symmetry
around the hyperplanex3 = 1, which implies thatx′
3+ andx′
3− are symmetric to each
other. Secondly, we can observe that the redundancy that we introduced by adding
negated variables and rows is still present in (6). By removing the duplicated rows
and settingz 1±,2∓ =y 1+,2−−y 1−,2+, we obtain the following one-dimensional linear
program.
minz 1±,2∓
z1±,2∓ +s 1,2 = 2
−z1±,2∓ +s 3 = 1
−2≤z 1±,2∓≤2
s1,2,s 3≥0
In this final linear program, we have additionally removed the reflection symmetry
around the hyperplanex 1 +x 2 = 2in the original problem. Finally, we can con-
clude that applying the equitable partition to the split reformulation was sufficient
to remove the reflection symmetries from our problem. In the next sections, we show
more formally that the illustrated procedure can be used to aggregate the reflection
symmetries of any linear program.
