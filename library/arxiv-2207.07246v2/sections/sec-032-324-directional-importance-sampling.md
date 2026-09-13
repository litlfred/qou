---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-032-324-directional-importance-sampling
section_title: "Directional Importance Sampling"
section_number: 3.2.4
pages: 80-87
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
In this section, we discuss a special case of the importance sampling method.
Sometimes, the proposed transition probability T (s→ s′) has a certain symmetry
along n directions in the state space, so there are always n unique states s′
1,s′
2,...,s′
n
which share the same proposed transition probability T (s→s′
i),
T (s→s′
1) =T (s→s′
2) =... =T (s→s′
n). (3.65)
So, from the current state s, there is the same chance of proposing any of the states
froms′
1 tos′
n. Similarly, for a given state s′, there can be several states s1,...,s n which
have the same proposed transition probability T (s′→si). For the reverse proposed
transition probability we have,
T (s′→s1) =T (s′→s2) =... =T (s′→sn). (3.66)
The summation of the proposed transition probability alone each direction is the same,
∑
s′
i
T (s→s′
i) =
∑
si
T (s′→si) = 1
n. (3.67)
The total summation of the proposed transition probability is,
∑
s′
T (s→s′) =
∑
i
∑
s′
i
T (s→s′
i) =
∑
s
T (s′→s) =
∑
i
∑
si
T (s′→si) = 1. (3.68)
For example, Fig. 3.2 is an illustration for n = 8 case. In this case, in the conﬁgu-
ration space, a particle located at r = (x,y,z ) can be described as in state s. We can
propose to move it to a new state s′ with r′ = (x′,y′,z′) according to,
T (s→s′) =
( 1√
2πσ2
)3
e− (x′−x)2
2σ2 e− (y′−y)2
2σ2 e− (z′−z)2
2σ2 . (3.69)
On each axis there are 2 choices which correspond to the same value of T (s→ s′).
They are x′ and x′′ = 2x−x′, y′ and y′′ = 2y−y′, z′ and z′′ = 2z−z′. That means
70
Figure 3.2: Illustration of a state space with 8-direction symmetry.
there are in total n = 23 = 8 directions and unique states correspond to the same
T (s→ s′). We can label these 8 states from s′
1 to s′
8. E.g., set s′
1 as the (x′,y′,z′)
state, and if x′ >x , y′ >y and z′ >z , we can simply denote s′
1≡ (+ + +). Sets′
2 as
the (x′′,y′,z′) state, we can denote s′
2≡ (− + +), etc. Finally set s′
8 as the (x′′,y′′,z′′)
state, we can denote s′
8≡ (−−− ). So now, s′
1 to s′
8 simply mean the n = 8 unique
directions in the state space. Similarly, for each of the 8 possible s′ withr′ = (x′,y′,z′),
there are 8 possible s (denoted by the light circles for each s′). Their coordinates are
x and x− = 2x′−x, y and y− = 2y′−y, z and z− = 2z′−z.
For the summations over s′
i, we have ∑
s′
i
T (s→ s′
i) = 1 /8. For example, the
summation over all the s′
1 = (+ + +) states is,
∑
s′
1
T (s→s′
1) =
∫ +∞
x dx′∫ +∞
y dy′∫ +∞
z dz′e− (x′−x)2
2σ2 e− (y′−y)2
2σ2 e− (z′−z)2
2σ2
(√
2πσ2
)3 = 1
8. (3.70)
71
The summation over all the s′
2 = (− + +) states is ∑
s′
2
T (s→ s′
2) which has the
same integrand as Eq.(3.70) but with a diﬀerent integral range
∫x
−∞dx
∫ +∞
y dy
∫ +∞
z dz,
and∑
s′
2
T (s→ s′
2) is also 1/8. The summation over all the s′
8 = (−−− ) states is
∑
s′
8
T (s→s′
8) which has the same integrand as Eq.(3.70) and again with a diﬀerent
integral range
∫x
−∞dx
∫y
−∞dy
∫z
−∞dz, and∑
s′
8
T (s→s′
8) is 1/8, too. The summation
for all the other states are similar and ∑
s′
i
T (s→s′
i) are all 1/8. Therefore Eq.(3.67)
and Eq.(3.68) are valid.
If T (s→ s′) has directional symmetry, we can mark the current state s as si
because it implicitly carries the directional notation i. When we proposed a new state
s′ from such a T (s→s′), then we can temporarily mark s′ as s′
1. However, we do not
immediately pick this state s′
1 as the new trial state. Because from T (s→s′), each
of the s′
1 to s′
n states has the same chance to be picked, we want to further pick the
‘best’ state from s′
1 to s′
n. We can pick a state s′
j according to ˜π(s′
j) such that,
˜π(s′
j) = π(s′
j)∑n
k=1π(s′
k). (3.71)
This can be called directional importance sampling. In this way, the correspondingly
proposed transition probability for directional importance sampling T imp(si→s′
j) can
be written as,
T imp(si→s′
j) =
[ n∑
j=1
T (si→s′
j)
]
˜π(s′
j) = nT (si→s′
j)π(s′
j)∑n
k=1π(s′
k) . (3.72)
The reverse directional importance sampling transition probability T imp(s′
j→si) can
be similarly written as,
T imp(s′
j→si) = nT (s′
j→si)π(si)∑n
i=1π(si) , (3.73)
where states s1 to sn all have the same proposed transition probability T (s′
j→si) 1 .
1Note that T imp(s→s′
i) is a valid proposed transition probability. Because for Eq.(3.73), with
72
Therefore after picking s′
1 from T (s→s′) we further pick s′
j by Eq.(3.71). Finally
we judge if s′
j is accepted or not by the acceptance probability A(si→s′
j),
A(si→s′
j) = min
[
1,π(s′
j)T imp(s′
j→si)
π(si)T imp(si→s′
j)
]
= min

1,
T (s′
j→si)
n∑
k=1
π(s′
k)
T (si→s′
j)
n∑
j=1
π(sj)

. (3.75)
If T (si→s′
j) =T (s′
j→si), Eq.(3.75) simply becomes,
A(si→s′
j) = min
[
1,
∑n
j=1π(s′
j)∑n
i=1π(si)
]
. (3.76)
If there are s′
j with bigger π(s′
j) than the π(s′
1) from the initially chosen s′
1 by
T (si→s′
1), then the directional importance sampling acceptance rate of Eq.(3.76) can
be higher than acceptance rate from gaussian sampling of Eq.(3.21) or regular sample
of Eq.(3.18). In other words, with this additional importance sampling, we can move
more beads in gaussian sampling with a larger step size in regular sampling than those
without importance sampling, with the same acceptance rate as without importance
sampling. Adding importance sampling can enable us to explore the conﬁguration
space more eﬃciently. The tradeoﬀ is that we need to evaluate all the relevant π(s′
j)
and π(si) which can be time-consuming.
the help of Eq.(3.65) and Eq.(3.67), we can see that,
∑
s′
T imp(s→s′) =
n∑
i=1
∑
s′
i
T imp(s→s′
i)
=n
n∑
i=1
∑
s′
i
T (s→s′
i)π(s′
i)∑n
j=1π(s′
j)
=n
∑
s′
i
T (s→s′
i)
∑n
i=1π(s′
i)∑n
j=1π(s′
j)
=n
∑
s′
i
T (s→s′
i)
= 1. (3.74)
SoT imp(s→s′
i) based on the importance sampling algorithm is a valid proposed transition probability
because it is non-negative and its summation over all the possible states is 1. Actually Eq.(3.74)
may not really need to be required. As long as the normalization factors of T imp can be canceled in
acceptance rate A(s→s′) it will be correct.
73
As long as the number n is an even number, and each state s′
i can ﬁnd its opposite
direction among the n directions, it can be reduced to a simple 2-directional case. We
can pick n/2 directions and combine them into one generalized direction, and combine
the rest n/2 opposite directions into the other generalized direction. Once we picked
s′
1 from one direction, there is always a state s′
2 in exactly the opposite direction. For
example, in the n = 8 case illustrated by Fig. 3.2, as indicated by the red arrows and
lines, we can denote s ass1, and we group s′
1 tos′
4 into one generalized direction. And,
since s′
5 is at the opposite direction of s′
4, s′
6 is the opposite of s′
3, s′
7 is the opposite
of s′
2, and s′
8 is the opposite of s′
1, so we group s′
5 to s′
8 into the other generalized
direction. By doing this, we reduced the n = 8 case into an n = 2 case. Every time we
proposeds′
1, we takes′
2 in the opposite direction of s′
1 as the only alternative state. We
can just mark s′
2 as s′
1−. For the chosen s′
1 or s′
2, there is a corresponding s2 such that
T (s′
i→s1) =T (s′
i→s2). In our PIMC, usually one can ﬁnd an ‘opposite direction’
ofR′ which can be marked asR′′ such that Tl′r′(R→R ′) =Tl′r′(R→R ′′), and then
we can use directional importance sampling to further pick either R′ orR′′.
As a concrete example, we can apply the n = 2 importance sampling to the single
bead sampling in Sections 3.2.1. The algorithm is described as follows.
Step 1 For the current state s, randomly pick bead K, we propose to move its conﬁg-
uration from RK to R′
K according to Eq.(3.32).
Step 2 It is 3 dimensional space and the particle number is A, each particle along one
dimension has 2 diﬀerent choices of coordinates, so there are 2 3A diﬀerentR′
K
which give the same value of Eq.(3.32). For any proposedR′
K = RK−1+RK+1
2 +∆R,
we only pickR′
K− = RK−1+RK+1
2 −∆R =RK−1 +RK+1−R′
K, because it not only
corresponds to the same value of Eq.(3.32) but also the opposite direction of
R′
K. Call the state with total conﬁguration R′ ={R1,..,R′
K,...,R N} as s′
1, and
74
call the state withR′− ={R1,..,R′
K−,...,R N} as s′
2 or s′
1−. We now calculate,
π(s′
1)
π(s′
1) +π(s′
1−) = fV
l′r′(R′)gF (R′)
fV
l′r′(R′)gF (R′) +fV
l′r′(R′
−)gF (R′
−)
= fV
l′r′(R′)
fV
l′r′(R′) +fV
l′r′(R′
−). (3.77)
Generate a random number a ranging uniformly from 0 to 1. If a≤ Eq.(3.77)
we choose R′
K which means s′
1, otherwise we choose R′
K− which means s′
2.
Step 3 Denote the original state s as s1. According to Eq.(3.33), no matter which
s′
i is selected, there are only two choices for s1 and s2. Since we denote the
original state s with RK as s1, s2 must include a another choice of RK call
it RK− such that
(
RK− RK−1+RK+ 1
2
)2
=
(
RK−− RK−1+RK+ 1
2
)2
. Similar with
R′
K−, we have RK− RK−1+RK+1
2 = RK−1+RK+1
2 − RK− for RK−. We denote
RK− = RK−1 +RK+1−RK as the opposite position of RK, and we denote
R− ={R1,..,R K−,...,R N} as s2 or s1−. The left part of Fig. 3.3 illustrates the
RK,RK−,R′
K−, andR′
K−. For the picked new states′
i, use Eq.(3.75) to calculate
the acceptance probability A(si→s′
i) and we ﬁnd that
A(s1→s′
i)=min

1,
T (s′
i→s1)
2∑
j=1
π(s′
j)
T (s1→s′
i)
2∑
j=1
π(sj)


=min



1,e
−
(
RK−
RK−1+RK+ 1
2
)2
∆τ ℏ2
m
[
fV
l′r′(R′)gF (R′) +fV
l′r′(R′
−)gF (R′
−)
]
e
−
(
R′
K−
RK−1+RK+ 1
2
)2
∆τ ℏ2
m [fV
lr (R)gF (R) +fV
lr (R−)gF (R−)]



=min
{
1,fV
l′r′(R′) +fV
l′r′(R′
−)
fV
lr (R) +fV
lr (R−)
}
. (3.78)
Step 4 Generate a uniform random number b which ranges from 0 to 1. If b≤A(s1→
s′
i), the new state s′
i is accepted, so set it as the current state s, namely s =s′
i,
75
then go to step 1 and continue. Else, the new state s′
i is rejected (in other words
the new state s′
i is just the current state s), then go to step 1 and continue.
Figure 3.3: Illustration of 2-direction importance samplings. The left one is for single
bead sampling plus 2-direction importance sampling. The right one is for regular
sampling plus 2-direction importance sampling.
The importance sampling can also be applied on the regular single bead sampling in
sections 3.2.3. The algorithm is very similar. The diﬀerence is that, in step 1, we propose
a move for the selected beadK according to Eq.(3.63). In step 2,R′
K−RK =RK−R′
K−
so R′
K− = 2RK−R′
K, and denote the new state with R′
K as s′
1, with R′
K− as s′
2. In
step 3, denote the current state as s1, if s′
1 is chosen, RK−R′
K = R′
K−RK− so
RK− = 2R′
K−RK. If s′
2 is chosen, RK−R′
K− =R′
K−−RK− so RK− = 2R′
K−−RK.
Based on the chosens′
1 ors′
2, denote the correspondingRK− ass2. The right part of Fig.
3.3 illustrates the relevant states and the coordinates. Since T (s1→s′
i) =T (s′
i→s1),
the A(s1→s′
i) is simply Eq.(3.76) and we have,
A(s1→s′
i) = min

1,
2∑
j=1
π(s′
j)
2∑
j=1
π(sj)


= min
{
1,fV
l′r′(R′)gF (R′) +fV
l′r′(R′
−)gF (R′
−)
fV
lr (R)gF (R) +fV
lr (R−)gF (R−)
}
= min


1,
fV
l′r′(R′)Gf
K−1,K′Gf
K′,K+1 +fV
l′r′(R′
−)Gf
K−1,K′
−
Gf
K′
−,K+1
fV
lr (R)Gf
K−1,KGf
K,K+1 +fV
lr (R−)Gf
K−1,K−Gf
K−,K+1


.(3.79)
76
The K− or K′
− appear at the I or J subscript in Gf
I,J means RK− or RK
′
− in the
corresponding place in Eq.(2.97).
