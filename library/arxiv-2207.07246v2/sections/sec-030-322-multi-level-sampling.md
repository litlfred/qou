---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-030-322-multi-level-sampling
section_title: "Multi-level Sampling"
section_number: 3.2.2
pages: 69-77
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
Due to the disadvantage of single bead sampling, for a given amount of computation
time, we have to sample multiple beads at a time instead of just one in order to make
the sampling eﬃcient. For example, if we propose to move u portion of the N beads,
so about uN beads will be proposed to move at a time, and the acceptance rate is
a. Then in order for all the N beads to be moved, we need at least 1 /(ua) trials. For
each trial, in order to calculate acceptance rate A(s→s′), we need to do uN updates
for either φr
M(R,S ) in Eq.(2.103) or φl
M(R,S ) in Eq.(2.104) with accordingly range
of M. So for the proposed moves there are uN/(ua) =N/a updates. Besides, among
all the 1/(ua) trials, only about a/(ua) = 1/u are accepted, for those accepted moves,
we need to update some beads for the φr
M(R,S ) and some for the φl
M(R,S ). This will
59
actually results in updating about N beads. So for the accepted moved, there will
be N/u updates. So totally, there will be N/u +N/a =N(1/u + 1/a) updates. And
the factor (1/u + 1/a) is usually much smaller than N, for example, N=500, when
u = 1/3, a could be around 0.1 so 10%, so (1/u + 1/a)≈ 13 which is much smaller
thanN = 500. So N(1/u + 1/a) updates much more cheaper than N 2 updates needed
for the single beads sampling.
In order to ﬁnd some ways to sample multiple beads at a time, we need to make full
use of Eq.(3.30). From the totalN +1 beads on the time line from bead 0 to beadN, we
randomly pick 2n +1 contingent beads from beadI to beadI +2n, wheren is a positive
integer. To make the notations easier, here we temporarily mark the conﬁgurations
from bead I to bead I + 2n as R0 to R2n, and we mark their conﬁgurations as,
R ={R0,R 1,R 2,...,R 2n−1,R 2n}. (3.38)
The conﬁgurations R0 to R2n in Eq.(3.38) are just the relabeling of the original RI to
RI+2n among the total N + 1 beads on the path.
The product of the free particle propagators gF (R) can be written as,
gF (R) =
2n−1∏
I=0
Gf
I,I +1. (3.39)
We can group the 2n + 1 beads{R0,R 1,...,R 2n} inR inton levels as the following,
Level 0 : R0,R 2n. (2 beads) Ln
0(R)
Level 1 : R 1
2 2n. (1 bead) Ln
1(R)
Level 2 : R 1
4 2n,R 3
4 2n. (2 beads) Ln
2(R)
... ... ... ...
Levelk : R 1
2k 2n,R 3
2k 2n,R 5
2k 2n,...,R 2k−1
2k 2n. (2k−1 beads) Ln
k(R)
... ... ... ...
Leveln : R1,R 3,R 5,R 7,...,R 2n−1. (2n−1 beads) Ln
n(R)
60
We can then use Eq.(3.31) to rearrange Eq.(3.39) level by level and Eq.(3.39)
becomes,
gF (R) =
n∏
k=0
Ln
k(R), (3.40)
where Ln
k(R) is deﬁned as the product of gaussian functions at level k,
Ln
k(R) =



Gf
0,2n, k = 0.
2k−1
∏
I=1
Gf
2I−1
2k 2n; 2I−2
2k 2n, 2I
2k 2n, k ⁄= 0.
(3.41)
For any non negative integer J,K,L,M,N, the Gf
J,K is calculated by Eq.(2.97), and
the Gf
M;L,N in Eq.(3.41) is,
Gf
M;L,N =
( 2m
π|N−L|∆τ ℏ2
) 3A
2
e
−(RM−RL+RN2 )
2
2×|N−L|
2 ∆τ ℏ2
2m . (3.42)
Given Eqs.(3.41) and (3.42), we can propose to move multiple beads, from bead 1 to
2n− 1 such that the new conﬁguration is
R′ ={R′
0,R′
1,R′
2,...,R′
2n−1,R′
2n}, (3.43)
where R0 and R2n remain the same although they are marked as R′
0 and R′
2n in
Eq.(3.43). The product of the new free particle propagators gF (R′) can be written as,
gF (R′) =
n∏
k=0
Ln
k(R′). (3.44)
We can set the proposed transition probability Tl′r′(R→R ′) as,
Tl′r′(R→R ′) =gF (R′) =
n∏
k=0
Ln
k(R′). (3.45)
Eq.(3.45) means that we can set the proposed transition probability at each level k as
Tn
k (R′) such that
Tn
k (R′) =Ln
k(R′), (3.46)
61
and Tl′r′(R→R ′) can be just written as
Tl′r′(R→R ′) =
n∏
k=0
Tn
k (R′). (3.47)
The reverse transition probability Tlr(R′→R ) can be written as,
Tlr(R′→R ) =
n∏
k=0
Tn
k (R). (3.48)
We can call this multi-level or n-level sampling, because we can propose to move
the beads level by level from level 0 to level n, by using Tn
k (R′) at each level. By doing
proposed moves in this way, we implement Eq.(3.47). This makesgF (R′)Tlr(R′→R) =
gF (R)Tl′r′(R→R ′) and it enables Eq.(3.12) to become Eq.(3.20), and we can use
Eq.(3.21) to judge if accept R′ or not. Fig. 3.1 is the illustration of 3-level sampling.
Level 0 
Level 3 
Level 2 
Level 1 
0 54321 6 7 8
0 1’ 3’ 5’ 7’ 2’ 6’ 4’ 8
0,1 
fG 1,2 
fG 2,3 
fG 3,4 
fG 4,5 
fG 5,6 
fG 6,7 
fG 7,8 
fG
4';0,8 
fG
2';0,4' 
fG 4';0,8 
fG
6';4',8 
fG
4';0,8 
fG
2';0,4' 
fG 6';4',8 
fG
1';0,2' 
fG 3';2',4' 
fG 5';4',6' 
fG 7 ';6',8 
fG
I I+2 I+1 I+3 I+7 I+6 I+5 I+4 I+8 0 N
I I+1 I+2 I+3 I+4 I+5 I+6 I+7 I+8 
I I+2 I+1 I+3 I+7 I+6 I+5 I+4 I+8 0 N
I I+1 I+2 I+3 I+4 I+5 I+6 I+7 I+8 
Figure 3.1: Illustration of a 3-level sampling algorithm.
The algorithm can be described as follows.
Step 1 For the totalN + 1 beads on the time line as shown in Fig. 2.5, select a proper
integern, randomly pick 2n + 1 contingent beads from RI to RI+2n (note that
62
in the program, n does not need to be a ﬁxed number, we can pick diﬀerent
n each time when we are at step 1). For notational convenience, temporarily
call them R0 to R2n instead of RI to RI+2n, and we useR to denote the group,
R ={R0,R 1,R 2,...,R 2n−1,R 2n}.
For example, in Fig. 3.1, it is n = 3 so 2n = 8. We randomly pick RI to RI+8
beads from the total N + 1 beads, we temporarily mark them as R0 to R8.
Step 2 1. If we keep R0 and R2n unchanged, this can be taken as a ‘fake’ level 0
move, so R′
0 =R0 and R′
2n =R2n. In this case, Ln
0(R′) =Ln
0(R), we set
Tl′r′(R→R ′) =
n∏
k=1
Ln
k(R′), (3.49)
and it can still make Eq.(3.12) become Eq.(3.20). And we go to step 3.
2. Else, if we keep R2n unchanged and just propose R′
0 (so R′
2n =R2n), then
according to Eq.(3.41), Ln
0(R′) = exp
[
− (R′
0−R2n)2
2×2n∆τ ℏ2
m
]
, we propose
r′0
i =r2n
i +gi
√
2n∆τ ℏ2
m, (3.50)
for i from 1 to A, and we have R′
0 and go to step 3 for the rest Ln
k(R′).
3. Else, if we keep R0 unchanged and just propose R′
2n (so R′
0 = R0), then
according to Eq.(3.41), Ln
0(R′) = exp
[
−
(R0−R′
2n)2
2×2n∆τ ℏ2
m
]
, we propose
r′2n
i =r0
i +gi
√
2n∆τ ℏ2
m, (3.51)
for i from 1 to A, and we have R′
2n and go to step 3 for the rest Ln
k(R′).
4. Else, we can also use the one bead sampling algorithm described in section
3.2.1, propose R′
0 according to R1 and R′
2n according to R2n−1 and then
judge and go to step 1.
For example, in Fig. 3.1, we keepR0 andR8 unchanged, soR′
0 =R0 andR′
8 =R8.
63
Step 3 According to the product of gaussian functions of Ln
k(R) in Eq.(3.41), we
propose the moves level by level, so k from 1 to n. At level k, 2k−1 beads
need be to moved, which means from I = 1 to 2k−1, each R 2I−1
2k 2n need to be
proposed to a new conﬁguration R′
2I−1
2k 2n. And we propose R′
2I−1
2k 2n according to
the Gf
( 2I−1
2k 2n)
′
;( 2I−2
2k 2n)
′
,( 2I
2k 2n)
′ in Ln
k(R′) in Eq.(3.45), such that r′(2I−1)2n−k
i (the
new coordinates of particle i) in R 2I−1
2k 2n is proposed according to,
r′
2I−1
2k 2n
i =r′
2I−2
2k 2n
i +r′
2I
2k 2n
i
2 +gi
√
2n
2k ∆τ ℏ2
2m. (3.52)
Fori from 1 to A, we propose to move particle i according to Eq.(3.52) in each
conﬁguration in each level.
Note that the level k beads are only proposed based on the beads of previous
levels, so this allow us to propose the new beads level by level. After we propose
the new conﬁgurations level by level, we have R′ ={R′
0,R′
1,R′
2,...,R′
2n−1,R′
2n}.
For example, in Fig. 3.1, level 1, 2 and 3 are,
Level 1 k = 1, 21−1 = 1, I = 1, each [(2I− 1)23−1]th bead needs to be moved,
so R4 is the only bead that needs to be moved, and we propose R′
4 based
on R′
0 and R′
8 according to Eq.(3.52), and each particle is moved as
r′4
i =r′0
i +r′8
i
2 +gi
√
4∆τ ℏ2
2m. (3.53)
After looping over all the particles, go to level 2.
Level 2 k = 2, 22−1 = 2, soI = 1, 2, each [(2I−1)23−2]th bead needs to be moved,
so R2 and R6 are the two beads that need to be moved, and according to
Eq.(3.52), we propose R′
2 based on R′
0 R′
4, and R′
6 based on R′
4 and R′
8.
E.g., each particle in R′
2 is moved as
r′2
i =r′0
i +r′4
i
2 +gi
√
2∆τ ℏ2
2m, (3.54)
64
and that in R′
6 is moved as
r′6
i =r′4
i +r′8
i
2 +gi
√
2∆τ ℏ2
2m. (3.55)
After looping over all the particles, go to level 3.
Level 3 k = 3, 23−1 = 4, so I = 1, 2, 3, 4, each [(2I− 1)23−3]th beads need to be
moved, and so R′
1, R′
3,R′
5, R′
7 need to be proposed according to Eq.(3.52)
similarly as described before.
Step 4 Now we need to look at the whole set of N + 1 beads on the time line, and
use consistent notations in the work. The {R′
0,R′
1,R′
2,...,R′
2n−1,R′
2n} in step 3
are in fact as mentioned in step 1, really {R′
I,R′
I+1,R′
I+2,...,R′
I+2n−1,R′
I+2n} on
the time line. So overall, the proposed conﬁguration R′ is,
R′ ={R0,R 1,...,R′
I,R′
I+1,...,R′
I+2n,...,R N}. (3.56)
The original conﬁgurationR is just Eq.(2.88) for the whole N + 1 original beads.
For example, in Fig. 3.1, once we have the new {R′
0,R′
1,...,R′
8}, we change their
labels to the original ones {R′
I,R′
I+1,...,R′
I+8}. So ﬁnallyR′ is the same asR
except that RI to RI+8 are replaced by R′
I to R′
I+8.
Step 5 Use Eq.(3.21) to judge if we accept the proposed conﬁgurations R′ or not.
Then go to step 1 and continue.
For example, in Fig. 3.1, we use Eq.(3.21) to judge if we accept the proposed
conﬁgurationsR′ or not.
It should be pointed out that, the proposed trial moves at each level in the multi-
level sampling are the same as in the bisection method (Ceperley (1995)). But the
two are not the same. We propose all the n-level new conﬁgurations and then do an
65
overall acceptance or rejection. However in the bisection method, we accept or reject
at each level, and if the proposed conﬁguration is rejected at level k, then the whole
proposed conﬁgurations from level 1 to k will be completely rejected and discarded.
In the bisection method, the lower the level, the less time consuming it is to do
the rejection. In other words, ‘if you want to reject, reject early.’ It works best if the
ﬁrst level’s acceptance rate is highly distinct from the rest levels’.
For example, consider a 3-level bisection, if the ﬁrst level acceptance rate is 30%,
the second and third levels’ are 80% and 90%, then the total acceptance rate is 21.6%.
But since the ﬁrst level acceptance rate is signiﬁcantly lower than the rest, actually
most trial moves are quickly rejected at the ﬁrst level and there is no need to spend
time to go to 2 nd and 3rd level, and those trial moves which get to the 2 nd and 3rd
level are mostly be accepted. Therefore, not much time is wasted at the 2 nd and 3rd
levels. In this case, bisection method will be faster than multi-level sampling simply
because it can reject early. Bisection works well for systems with potentials with highly
repulsive cores where core overlap can be deleted early and rejected.
However, if the three levels’ acceptance rate are similar, then the bisection method
does not have an advantage over multi-level sampling. If the 1 st, 2nd and 3rd level’s
acceptance rate are 50%, 60% and 70%, then the total acceptance is still similarly 21%.
Nonetheless, more moves will go to level 2 and 3 and be judged and then be rejected.
This slows down the bisection method. We have tested the bisection method and ﬁnd
it lack of eﬃciency in our calculations. In the bisection method we need to accept
or reject using an eﬀective Eq.(3.21) at each level which involves the calculation of
an eﬀective fV
l′r′(R′) and fV
lr (R). They contain the sum over all the spin and isospin
states. This is diﬀerent from the situations in most bisection method calculations
which mostly deal with central interaction which does not have spin isospin structure.
This spin and isospin sum makes each level’s acceptance rate not too much diﬀerent
66
from each other, just like the 50%, 60% and 70% example above.
Therefore, we ﬁnd the bisection method does not have a computational advantage
over multi-level sampling. As expected, multi-level sampling has a slightly higher
acceptance rate than bisection method. This is because the bisection method can reject
early. For example, say the total acceptance rate is a = 20% for a 2-level sampling.
In bisection method it decomposes the acceptance rate a in to a1 for level 1 and a2
for level 2, and theoretically a =a1a2. If a1 and a2 are both less than 100% then the
acceptance rate of bisection and 2-level sampling are the same, both are a = 20%. But,
in bisection it sometimes happens that a1 = 10% and a2 = 200% (when it is bigger
than 100% it simply means always accepting the moves), so theoretically a1a2 is still
20%, but actually since a1 = 10%, 90% of the moves have already been rejected at
the 1st level. The real total acceptance is around 10% instead of the 20% for 2-level
sampling. We use multi-level sampling in our calculations, because it allows us to take
more samples of new conﬁgurations per unit time.
