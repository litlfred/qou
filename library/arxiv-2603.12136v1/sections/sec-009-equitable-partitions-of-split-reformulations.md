---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-009-equitable-partitions-of-split-reformulations
section_title: "Equitable partitions of split reformulations"
section_number: null
pages: 15-22
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
15
3.3 Equitable partitions of split reformulations
Throughout this section, we investigate the structure of equitable partitions of the
split reformulationFS(A,b,ℓ,u,c)for an arbitrary linear programF(A,b,ℓ,u,c)with
ℓ≤Oandu≥O.
Recall that for a split reformulation, its variable index setscW= cW +∪cW− and
bV= bV +∪ bV− correspond to the original and negated variables and constraints,
respectively. Forx∈ {−1,1}, we will use the synonyms bVx :=
(bV + ifx= 1
bV− ifx=−1
and cWx :=
(cW + ifx= 1
cW− ifx=−1 to denote the corresponding signed sets and for
v∈V(w∈W) we similarly usev x (wx) to indicate thatvlies in bVx (cWx). For
anyP⊆Vandγ∈{−1,1} P, and, we useP γ :={v γv ∈ bVγv |v∈P}to denote
the signed set of indices corresponding in bV + (ifγ v = 1)and bV− (ifγ v =−1).
For example, forP={v 1,v 2,v 3}andγ :=
γv1 γv2 γv3

=

1−1−1

, we would
have thatP γ ={v +
1,v−
2,v−
3}and thatP −γ ={v−
1,v +
2,v +
3}, wherev +
1,v +
2,v +
3 ∈ bV +
2
andv −
1,v−
2,v−
3 ∈ bV−
2 . Similarly, for anyQ⊆Wandλ∈ {−1,1} Q, we define
Qλ :={w λw∈cWλw|w∈Q}.
Then, we consider the structure of equitable partitions(bP, bQ)ofF S(A,b,ℓ,u,c)
in further detail. These equitable partitions have many symmetries that are a result
of the redundancies introduced by the split reformulation. One property that will be
important in this context, is thepolarityof parts bP∈ bP. If for somev∈V, both
v+∈ bPandv −∈ bPhold then bPis said to bebipolar. If bP⊆ bVis not bipolar, then
|bP∩{v +,v−}|≤1holds for allv∈Vand we say it isunipolar. Note that for each
unipolar part bPthere exists a partP⊆Vandγ∈{−1,1} V such that bP=P γ
holds. Similarly,bQ⊆ cWisbipolarif there exists somew∈Wsuch thatw +∈ bQand
w−∈Qhold, and bQis said to beunipolarif| bQ∩{w +,w−}|≤1holds for allw∈W.
If bQis unipolar, then there existsQ⊆Wandλ∈{−1,1} W such that bQ=Q λ
holds. In Definition 8, we define the symmetric structure of equitable partitions of the
split reformulationFS(A,b,ℓ,u,c)of any linear programF(A,b,ℓ,u,c)with row and
column indicesVandW, respectively. The sets bVand cWare the row and column
indices ofFS(A,b,ℓ,u,c)as defined in Definition 6.
Definition 8Let( bP, bQ)be a partition of bV× cW. We say that(bP, bQ)issymmetricif the
following hold.
(i) for every unipolar partP∈ bPsuch thatP=P γ holds,P −γ∈ bPholds too.
(ii) for every bipolar partP∈ bPand anyv∈V,Peither contains bothv + andv− or none.
(iii) for every unipolar partQ∈ bQsuch thatQ=Q λ holds,Q−λ∈ bQholds too.
(iv) for every bipolar partQ∈ bQand anyw∈W,Qeither contains bothw + andw− or
none.
16
For a symmetric equitable partition(bP, bQ)ofF S(A,b,ℓ,u,c), we use bPB :={P∈
bP|Pis bipolar}and bPU :={P∈ bP|Pis unipolar}and note that bPU and bPB are
a disjoint partition of bP. Similarly, we define that bQB :={Q∈ bQ|Qis bipolar}
and bQU :={Q∈ bQ|Qis unipolar}, which also partitions bQ. Furthermore, we use
bVU := S
P∈bPU
P, bVB := S
P∈bPB
P, cWU := S
Q∈bQU
Qand cWB := S
Q∈bQB
Qfor the
corresponding partitioned subsets ofbVand cW. To denote the corresponding sets in
VandWwe useV U :={v∈V|{v +,v−}∩ bVU̸=∅},V B :={v∈V|{v +,v−}⊆ bVB},
WU :={w∈W|{w +,w−}∩ cWU̸=∅}andW B :={w∈W|{w +,w−}⊆ cWB}.
The notion of bipolar and unipolar parts in Definition 8 is very similar to an
observation by Bödi, Herr and Joswig [4], who show that the orbits of reflection
symmetry groups are either unipolar or bipolar, where bipolar orbits must consist of
only pairsw +,w− for some subset ofW. Similarly, we will show that the equitable
partitions ofFS(A,b,ℓ,u,c), that the associated equitable partitions are indeed sym-
metric and satisfy Definition 8.
Next, we show one important property of symmetric partitions: bipolar parts
correspond to zero row and column sums.
Lemma 9Let( bP, bQ)be any partition ofF S(A,b,ℓ,u,c)and let(P ′,Q′)∈ bP× bQ. Then,
the following hold:
(i) IfP ′ =P 1 ∪P−1 holds for some setP⊆V, then P
v∈P′cMv,w = 0holds for allw∈W.
(ii) IfQ′ =Q 1 ∪Q−1 holds for some setQ⊆W, thenP
w∈Q′cMv,w = 0holds for allv∈V.
ProofTo prove (i), consider anyw∈W. Then, we have that
X
v∈P′
cMv,w =
X
v+∈P 1
cMv+,w +
X
v−∈P−1
cMv−,w =
X
v∈P
Av,w +
X
v∈P
−Av,w = 0,
wherethefirstequalityisgivenbythecondition.Thesecondequalitycanbeobservedthrough
case distinction whetherw∈W + orw∈W − holds. Ifw∈W + holds then by definition of
cMwe have cMv+,w =A v,w and cMv−,w =−A v,w. Forw∈W − we havecMv+,w =−A v,w
and cMv−,w =Av,w. In both cases, the equality follows.
The proof for (ii) is similar, where we have for allv∈Vthat:
X
w∈Q′
cMv,w =
X
w+∈Q1
cMv,w+ +
X
w−∈Q−1
cMv,w− =
X
w∈Q
Av,w +
X
w∈Q
−Av,w = 0.
□
Corollary 10Let( bP, bQ)be any symmetric equitable partition ofF S(A,b,ℓ,u,c)and let
(P,Q)∈( bP, bQ). If at least one ofPandQis bipolar, then P
v∈P cMv,w = 0holds for all
w∈Qand P
w∈QcMv,w = 0holds for allv∈P.
17
ProofWe haveP
v∈P
P
w∈QcMv,w =P
w∈Q
P
v∈P cMv,w = 0, where the final equality holds
by Lemma 9, since bipolarity of eitherQorPimplies that P
w∈QcMv,w = 0holds for all
v∈Por P
v∈P cMv,w = 0holds for allw∈Q. By equitability of the block(P,Q), the row and
column sums are identical, and it follows thatP
w∈QcMv,w = 1
|P|
P
v′∈P
P
w∈QcMv′,w = 0
holds for allv∈Pand P
v∈P cMv,w = 1
|Q|
P
w′∈Q
P
v∈P cMv,w′ = 0holds for allw′∈Q.□
In order to investigate symmetric equitable partitions of split reformulations, we
need a key assumption that limits the structure of the equitable partitions for the
split reformulation. One disadvantage of the split reformulation is that thex+- and
x−-variables may interact in non-identical ways, which makes it tough to interpret
the computed partition of bVand cWin the context of the original linear program
F(A,b,ℓ,u,c). For example, for variablesw 1,w 2∈W, it may be the case that there
exists a part{w+
1,w−
1,w +
2}which acts identically on the whole domain ofw1 but only
on the positive domain ofw2. To avoid such issues, we consider only partitions of the
split reformulation such that for each partQ∈ bQ, the associated variables inQof
the linear programF(A,b,ℓ,u,c)have identical variable bounds.
Definition 11A partition( bP, bQ)of bV× cWis said to bebound-respectingif for allQ∈ bQ
and anyws1
1 ,ws2
2 ∈Qwe have:
(i)ℓ w1 =ℓw2 andu w1 =uw2 ifs 1 =s 2 holds
(ii)ℓ w1 =−uw2 andu w1 =−ℓw2 ifs 1̸=s 2 holds
Then, we show that the split reformulationFS(A,b,ℓ,u,c)admits a symmetric
equitable partition in two steps. First, we show in Lemma 12 that the initial coarsest
bound-respecting equitable partition is symmetric. Second, we show in Lemma 13
that any refinements of the initial partition from the constraint matrix preserve the
symmetry of the partition.
Lemma 12Let( bP, bQ)be the coarsest bound-respecting partition ofFS(A,b,ℓ,u,c)such that
bPis equitable for bb :=

b−b

and bQis equitable for thebc :=

c−c
⊺ andbu :=

u−ℓ
⊺.
Then,( bP, bQ)is symmetric. Moreover,bv = 0holds for allv∈ bVB andc w = 0andu w =−ℓw
hold for allw∈W B.
ProofFirst, consider the coarsest equitable partitionbPof the right-hand sidebb∈R bV +∪bV−
.
Consider any bipolar partP∈ bPsuch that for somev∈V,{v +,v−}⊆Pholds. Then, since
bPis an equitable partition ofbb, it follows thatbv =bbv+ =bbv− =−b v holds, which implies
thatb v = 0. As this holds for allv∈Vwithb v = 0, it follows that the blockPin the
coarsest equitable partition is exactly formed by those rows ofbthat have right-hand side
0, i.e.P={v +,v−|such thatb v = 0forv∈V}is the only bipolar part in bP. Clearly,P
satisfies Definition 8(ii).
For any unipolar part bP∈ bPholds such that bP=P γ for suitableP⊆Vand
γ∈ {−1,1}V, it follows from equitability ofbPfor bbthat for allv γ
1,vγ
2 ∈ bPthat bbvγ
1
=
γv1bv1 =γ v2bv2 = bbvγ
2
holds. However, this directly implies for the setP−γ ⊆ bVthat
18
bbv−γ
1
=−γ v1bv1 =−γ v2bv2 =bbv−γ
1
holds, which shows thatP−γ is also an equitable block.
Thus, bPcan only be the coarsest equitable partition ofbbif there exists some blockbP′ such
thatP −γ ⊆ bP′. One can show using a similar argument thatP−γ = bP′ holds: existence
of anyv−γ ∈ bP′\P−γ contradicts that bPis the coarsest equitable partition ofbbas then
the part containingvγ can be merged withbPto form a coarser partition. Since the above
reasoning holds for all unipolar blocks, it follows that Definition 8(i) is satisfied.
Second, we consider the coarsest bound-respecting equitable partitionbQofbcandbu. Then,
for anyQ∈ bQwe have forbw1,bw2∈Qthatbc bw1 =bcbw2 andbubw1 =bubw2 hold. First, consider
the case whereQ∈ bQis bipolar, and letw 1∈Wbe some index such that{w +
1,w−
1}⊆Q
holds. Then, it follows from equitability forbcthatcw1 =bcw+
1
=bcw−
1
=−c w1 holds, which
implies thatcw1 = 0. Furthermore, equitability forbuimplies thatuw1 =buw+
1
=buw−
1
=−ℓw1
holds. Then, assume for the sake of contradiction that there exists anyw2∈Wsuch that
|{w+
2,w−
2}∩Q|= 1holds. Ifw +
2 ∈Qholds, thenbuw−
2
=−ℓw2 =−ℓw1 =buw−
1
=buw+
2
shows
thatw−
2 has the same bound forbu, where the second equality follows sincebQis a bound-
respecting partition andw +
2 andw +
1 are both included inQ. Similarly, ifw−
2 ∈Qholds,
thenbuw+
2
=u w2 =u w1 =buw+
1
=buw−
2
holds since bQis a bound-respecting partition andQ
contains bothw−
1 andw−
2 . In either case, it follows thatbuw+
2
=buw−
2
holds. As one ofw+
2
andw−
2 is inQ, it follows thatbcw+
2
=bcw−
2
=c w2 = 0also holds, which contradicts that bQ
is the coarsest bound-respecting partition as then bothw+
2 andw−
2 may be included inQ.
Thus, bipolar parts must always contain pairs of variables and Definition 8(iv) follows.
Finally, consider the case wherebQ∈ bQis unipolar and given bybQ=Q λ withQ⊆Wand
λ∈{−1,1} W. By equitability ofbQ, we must have for allwλ
1,wλ
2∈Q λ thatbcwλ
1
=bcwλ
2
and
buwλ
1
=buwλ
2
hold. Then, considerQ−λ⊆cW. First of all, note that for anyw−λ
1 ,w−λ
2 ∈Q−λ
that we have:bcw−λ
1
=−bcwλ
1
=−bcwλ
2
=bcw−λ
2
, where the first and last equalities follow by
definition ofbcand the second equality follows sincewλ
1 andw λ
2 lie in the equitable partQλ.
Now, let us show that for the boundsbuw−λ
1
=buw−λ
2
holds too:
buw−λ
1
=
(
−ℓw1 ifλ w1 = 1
uw1 ifλ w1 =−1 =



−ℓw1 ifλ w1 = 1andλ w2 = 1
−ℓw1 ifλ w1 = 1andλ w2 =−1
uw1 ifλ w1 =−1andλ w2 = 1
uw1 ifλ w1 =−1andλ w2 =−1
(a)
=



−ℓw2 ifλ w1 = 1andλ w2 = 1
uw2 ifλ w1 = 1andλ w2 =−1
−ℓw2 ifλ w1 =−1andλ w2 = 1
uw2 ifλ w1 =−1andλ w2 =−1
=
(
−ℓw2 ifλ w2 = 1
uw2 ifλ w2 =−1 =buw−λ
2
.
Here, (a) follows since bQis a bound-respecting partition andw λ
1 andw λ
2 are inQ∈ bQ.
ThusQ−λ⊆Q′ must hold for someQ′∈ bQ. Using a similar argument, one can show that
existence of anyw−λx ∈Q′\Q−λ shows that the part containingwλx can be merged with
Qλ, which contradicts thatbQis the coarsest partition. ThusQ−λ belongs tobQ, which shows
that Definition 8(iii) is satisfied.□
Note in Lemma 12 that the lower bounds of variablesx+ andx− are not considered
as they are all zero and thus do not affect the equitable partition ofcW. Next, let
us show that refinement of symmetric partitions through the constraint matrix again
yields a symmetric partition.
19
Lemma 13Consider the split reformulationF S(A,b,ℓ,u,c)of a linear program, where the
constraint matrix ofFS(A,b,ℓ,u,c)is given by cM=
 A−A
−A A

, and let(bP0, bQ0)be a sym-
metric partition ofF(A,b,ℓ,u,c). Then, the coarsest equitable partition(bP∞, bQ∞)that refines
(bP0, bQ0)with respect tocMis symmetric.
ProofBy Theorem 2 in [35], the coarsest equitable partition is unique. Thus, it suffices to
show that there exists a sequence of refinements such that the coarsest equitable partition
is symmetric. We prove the statement by showing that there exists a refinement algorithm
that maintains a symmetric partition at every step. In particular, we assume that(bPi, bQi)
is symmetric, and show that existence of any refinement of( bPi, bQi)implies that there
exists a refinement into a partition(bPi+1, bQi+1)that is symmetric. The result then follows
inductively, where the base case is satisfied by assumption.
Then, assume that( bPi, bQi)is a symmetric partition ofF S(A,b,ℓ,u,c)such that there
exists some(P ′,Q′)∈( bPi, bQi)such that cMP′,Q′ is not an equitable block. We consider
the case wherecMP′,Q′ does not satisfy (1) for somev,v′∈P ′ such thatP
w∈Q′cMv,w ̸=
P
w∈Q′cMv′,w, and show that thenbPi can be refined symmetrically so that(bPi+1, bQi)is a
symmetric partition that refines(bPi, bQi). The argumentation for the case wherecMP′,Q′ does
not satisfy (2) is identical up to transposition.
First, note that ifQ′ is bipolar, that then it follows by symmetry ofbPi and Lemma 9 thatP
v,wcMv,w = 0holds for allv∈P ′. Hence (1) is satisfied in this case, and it is sufficient to
consider the case whereQ′ is unipolar in the following. We letQ′ =Q λ for someQ⊆W
andλ∈{−1,1} W and useQ + :={w∈Q|w +∈Q λ}andQ − :={w∈Q|w −∈Q λ}to
denote the positive and negative variables inQ, respectively. Next, we show that refinement
of the block cMP′,Q′ always produces a symmetric partition. To do so, we distinguish the
cases whetherP′ is bipolar or unipolar.
Case 1:P′ is bipolar.
IfP′ is bipolar, then there existsP⊆Vsuch thatP ′ =P 1 ∪P−1 . Then, sinceQ′ is unipolar,
we have that:
cMP′,Q′ = cMP′,Qλ =
" cMP 1 ,Qλ∩W +
2
cMP 1 ,Qλ∩W−
2
cMP−1 ,Qλ∩W +
2
cMP−1 ,Qλ∩W−
2
#
=
 AP,Q+ −AP,Q−
−AP,Q+ AP,Q−

=
 G
−G

,
whereG :=
AP,Q+ −AP,Q−

. Then, consider the refinement ofbPi into bPi+1 obtained by
splittingP ′ intokdifferent classes based on the different row sums of cMP′,Q′. LetP ′
j for
j= 1,···,kdenote these parts, where we have for allv,v ′ ∈P ′
j that P
w∈Q′cMv,w =
P
w∈Q′cMv′,w, and define bPi+1 := ( bPi\{P ′})∪ Sk
j=1P′
j. We show that (i) and (ii) in
Definition 8 are satisfied for allP′
j, which is sufficient since they are satisfied by assumption
for allP′′∈ bPi\{P′}.
First,considerthecasewhereP ′
j isbipolar.SinceP ′
j containsatleastonepairv +,v−∈P′
j
for somev∈V 2, we can deduce thatP
w∈Q′Gv,w = P
w∈Q′cMv,w = P
w∈Q′cMv′,w =P
w∈Q′−Gv,w = 0holds. Then, note that for anyγ∈{−1,1}such thatv γ∈P ′
j, the rows
ofv γ andv−γ both sum to zero, which implies that alsov−γ∈P′
j holds by definition ofP′
j,
where we use the assumption that Definition 8(ii) holds forbPi to infer thatv−γ∈P′ holds.
Thus, this shows that Definition 8(ii) is satisfied bybPi+1 in the case whereP′ is bipolar.
20
IfP ′
j is unipolar, then there exists someγ∈{−1,1} V andP⊆Vsuch thatP ′
j =P γ,
and we have for allv∈P ′
j thatP
w∈Q′cMv,w =γ v
P
w∈Q′Gv,w =αfor someα∈R\{0},
where we can excludeα= 0because this corresponds to the bipolar parts treated above.
SinceP ′
i satisfies Definition 8(ii) by assumption, all elements ofP−γ are also contained in
P′, and must be partitioned according to their sums. Then we have for allv∈P−γ thatP
w∈Q′cMv,w =−γ v
P
w∈Q′Gv,w =−α, which shows that there exists somej′ such that
P′
j′ =P−γ. Thus, we have shown that Definition 8(i) holds forbPi+1 in the case whereP′ is
bipolar. Thus, we have shown that(bPi+1, bQi)is symmetric and refines(bPi, bQi).
Case 2:P′ is unipolar.
IfP ′ is unipolar, then there existsP⊆Vandγ∈{−1,1} V such thatP ′ =P γ holds.
By the assumption thatbPi is symmetric, it also holds thatP−γ∈ bPi. Then, we show that
forP γ andP −γ the corresponding blocks cMPγ,Q′ and cMP−γ,Q′ can be simultaneously
refined to preserve symmetry inbPi+1. Forx∈{γ,−γ}, letP x
+ :={v∈P|v +∈P x}and
Px
− :={v∈P|v − ∈P x}denote the positive and negative variables associated toP x,
respectively. Note thatPγ
+ =P−γ
− andP γ
− =P−γ
+ hold. Then, for the considered blocksPγ
andP −γ, we have that:
"
cMPγ,Q′
cMP−γ,Q′
#
=
" cMPγ,Qλ
cMP−γ,Qλ
#
=


APγ
+,Q+ −APγ
+,Q−
−APγ
−,Q+ APγ
−,Q−
−AP−γ
− ,Q+ AP−γ
− ,Q−
AP−γ
+ ,Q+ AP−γ
+ ,Q−


=


APγ
+,Q+ −APγ
+,Q−
−APγ
−,Q+ APγ
−,Q−
−APγ
+,Q+ APγ
+,Q−
APγ
−,Q+ APγ
−,Q−

 =
 G
−G

,
whereG= cMPγ,Q′ =
"
APγ
+,Q+ −APγ
+,Q−
−APγ
−,Q+ APγ
−,Q−
#
. Thus, the block corresponding to(P−γ,Q′)
is the negated block of(Pγ,Q′).
Forj= 1,...,k, letP j denote the partition ofPintoP j so that the row sums of all
v∈P γ
j are identical, and forj̸=j ′ andv∈P j andv∈P j′, the row sums ofvandv′ differ.
Then, we similarly define the partitionP−γ
j forj= 1,...,k. Forv,v ′∈P−γ, note that
X
w∈Q′
cMv,w =
X
w∈Q′
−Gv,w =−
X
w∈Q′
Gv,w
(a)
=−
X
w∈Q′
Gv′,w =
X
w∈Q′
−Gv′,w =
X
w∈Q′
cMv′,w
where (a) holds becauseP γ
j has the same row sums by definition. Thus, the partitions
Pγ
j andP −γ
j are both valid refinements. Note that for eachj= 1,···,k, the pair
Pγ
j andP −γ
j is a unipolar pair as in Definition 8(i). Then, the partition defined by
bPi+1 := bPi\{P γ,P−γ}∪Sk
j=1(Pγ
j ∪P−γ
j )satisfies Definition 8(i), and (ii) follows since we
did not alter any bipolar part inbPi. Thus,(bPi+1, bQi)is symmetric and refines(bPi, bQi).
Thus, we have shown that there exists a symmetric refinement(bPi+1, bQi+1)in all cases,
where bQi+1 = bQi holds. Using essentially the same proof, one can show that there exists a
symmetric refinement( bPi+1, bQi+1)with bPi = bPi+1 if there exists some(P′,Q′)∈ bPi× bQi
such that (2) is not satisfied forcM. This completes the proof.□
Theorem 14The coarsest bound-respecting and equitable partition(bP, bQ)ofF S(A,b,ℓ,u,c)
is symmetric.
21
ProofLemma 12 shows that the initial partition is symmetric, and it follows from Lemma 13
showsthatapplyingcolorrefinementontheconstraintmatrixproducesasymmetricequitable
partition, given the symmetric initial partition.□
Theorem 14 shows that symmetric equitable partitions of split reformulations
can be obtained by using the assumption that the partition is bound-respecting.
Although this assumption seems a bit arbitrary for now, we will motivate it in further
detail later on.
A simple but crucial observation for symmetric partitions is that symmetric par-
tition of the split reformulation induce partitions and signings for the original linear
program.
Proposition 15Consider any symmetric partition( bP, bQ). For its unipolar partsbPU and
bQU, there existγ∈{−1,1} VU and a partitionPU ofV U such that bPU =S
P∈P{Pγ,P−γ},
and there existsλ∈{−1,1} WU and a partitionQU ofWU such thatbQU =S
Q∈Q{Qλ,Q−λ}.
For its bipolar partsbPB and bQB, there exist partitionsPB ofV B andQ B ofW B such that
bPB ={P 1 ∪P−1 |P∈P B}and bQB ={Q 1 ∪Q−1 |Q∈Q B}hold.
ProofConsider any unipolar part bP∈ bP. By unipolarity, there existsP⊆Vsuch that
bP=P γ. Then, since(bP, bQ)is symmetric, Definition 8(i) holds and showsP−γ∈ bPholds
too. Since this holds for all elements andbPis a partition, it follows thatbPconsists of pairs
Pγ,P −γ. Then,PU is generated by all suchPandγis defined by picking a representative
part for each pairPγ,P −γ. A similar argument using Definition 8(iii)shows the result forλ
andQ U. For the bipolar parts, the statement follows directly from Definition 8(ii)(iv).□
For anyγ∈ {−1,1} VU,λ∈ {−1,1} WU,P :=P U∪P B andQ :=Q U∪Q B
such as those in Proposition 15 we say that they aregenerated by(bP, bQ). We use
bPγ
U :={P γ|P∈P U}and bQλ
U :={Q λ|Q∈Q U}, and definebP−γ
U and bQ−λ
U similarly.
Note that the choice forγis not unique as for eachP∈PU we can exchangePγ and
P−γ by negatingγv for allv∈P, i.e. by usingγ ′ := (−γP,γV\P ). Similarly, one can
also choose for eachQ∈Qto simultaneously negateλ w for allw∈Q. We note that
these actions only affect the signsγandλand not the setsP U andQ U.
