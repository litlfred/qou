---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-029-321-single-bead-sampling
section_title: "Single-Bead Sampling"
section_number: 3.2.1
pages: 66-69
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
FromR ={R0,...,R K,...,R N}, we can propose to move just one bead, bead K,
we moveRK to R′
K, thenR′ ={R0,...,R′
K,...,R N}. This is single bead sampling.
For theK = 0 or N case, the gF (R′) in Eq.(2.96) becomes,
gF (R′)|R0→R′
0 =Gf
0′,1
N−1∏
I=1
Gf
I,I +1, (3.22)
gF (R′)|RN→R′
N =Gf
N−1,N′
N−2∏
I=0
Gf
I,I +1, (3.23)
whereGf
0′1 andGf
N−1,N′ are as deﬁned in Eq.(2.98) and can be calculated by Eq.(2.69),
Gf
0′,1 =⟨R′
0|e−T ∆τ|R1⟩ =
( m
2π∆τ ℏ2
) 3A
2
e
−
(R′
0−R1)2
2∆τ ℏ2
m , (3.24)
Gf
N−1,N′ =⟨RN−1|e−T ∆τ|R′
N⟩ =
( m
2π∆τ ℏ2
) 3A
2
e
−
(RN−1−R′
N )2
2∆τ ℏ2
m . (3.25)
56
We can just set the proposed transition probability as,
Tl′r′(R→R ′)|R0→R′
0 =Gf
0′,1, (3.26)
Tl′r′(R→R ′)|RN→R′
N =Gf
N−1,N′, (3.27)
and then Eq.(3.12) becomes Eq.(3.20) and we use Eq.(3.21) to judge if we accept R′
K
and thusR′ or not.
For theK⁄= 0 or N case, the corresponding gF (R′) becomes,
gF (R′) =Gf
K−1,K′Gf
K′,K+1
K−2∏
I=0
Gf
I,I +1
N−1∏
I=K+2
Gf
I,I +1, (3.28)
where Gf
K−1,K′ and Gf
K′,K+1 are the free propagators calculated by Eq.(2.98) or
Eq.(2.69).
In order to proceed, we introduce a useful relation in our calculation. For any
coeﬃcients a and b and any conﬁguration RM, RN and RL,
a(RM−RN)2+b(RN−RL)2 =(a +b)
(
RN−aRM +bRL
a+b
)2
+ ab
a+b(RM−RL)2, (3.29)
where each square can be calculated by using Eq.(2.70). In particular, if a =b = 1,
Eq.(3.29) just becomes,
(RM−RN)2 + (RN−RL)2 = 2
(
RN− RM +RL
2
)2
+ (RM−RL)2
2 . (3.30)
By using Eq.(3.30), the product of the two free particle propagatorsGf
K−1,K′Gf
K′,K+1
in Eq.(3.28) becomes,
Gf
K−1,K′Gf
K′,K+1 =
( m
2π∆τ ℏ2
)3A
e
−
(
R′
K−
RK−1+RK+ 1
2
)2
∆τ ℏ2
m e
− (RK−1−RK+ 1)2
4∆τ ℏ2
m . (3.31)
We set the proposed transition probability Tl′r′(R→R ′) from Eq.(3.31) as,
Tl′r′(R→R ′) =
( m
π∆τ ℏ2
) 3A
2
e
−
(
R′
K−
RK−1+RK+ 1
2
)2
∆τ ℏ2
m . (3.32)
57
The corresponding reverse transition probability Tlr(R′→R ) can be written as,
Tlr(R′→R ) =
( m
π∆τ ℏ2
) 3A
2
e
−
(
RK−
RK−1+RK+ 1
2
)2
∆τ ℏ2
m . (3.33)
Now we can see that gF (R′)Tlr(R′→R ) = gF (R)Tl′r′(R→R ′), so Eq.(3.12)
becomes Eq.(3.20) and we use Eq.(3.21) to judge if we accept R′
K and thusR′ or not.
For particle i at bead K, we deﬁne its spatial coordinates as rK
i ≡ (xK
i ,yK
i ,zK
i ),
and its new proposed coordinates as r′K
i ≡ (x′K
i ,y′K
i ,z′K
i ). So for the A-nucleon nuclei,
RK = (rK
1 ,rK
2 ,...,rK
A ) and R′
K = (r′K
1 ,r′K
2 ,...,r′K
A ). We also deﬁne a 3 dimensional
vectorgi for particle i,
gi = (gix,giy,giz), (3.34)
where gix,giy,giz are all independent gaussian random numbers with average value 0
and variance 1.
The basic procedures of the algorithm is described as follows.
Step 1 Randomly pick an integer K from 0 to N.
Step 2 For particlei at bead K,
1. if K = 0, according to Eq.(3.26), propose its new coordinates r′0
i according
tor1
i at bead 1,
r′0
i =r1
i +gi
√
∆τ ℏ2
m, (3.35)
2. IfK =N, according to Eq.(3.27), propose its new coordinatesr′N
i according
torN−1
i at bead N− 1,
r′N
i =rN−1
i +gi
√
∆τ ℏ2
m, (3.36)
3. If K ⁄= 0,N , according to Eq.(3.32), propose its new coordinates r′K
i
according torK−1
i at bead K− 1 andrK+1
i at bead K + 1,
r′K
i =rK−1
i +rK+1
i
2 +gi
√
∆τ ℏ2
2m, (3.37)
58
Step 3 Loop over step 2 for all the particles, i from 1 to A. Then we have the new
conﬁguration R′
K.
Step 4 Use Eq.(3.21) to judge if we accept the proposed conﬁgurations R′ or not.
Then go to step 1 and continue.
In the program, we store all the probability amplitudes φr
M(R,S ) in Eq.(2.103)
andφl
M(R,S ) in Eq.(2.104) for M from 0 to N. Once any R′
K is accepted, we need to
update all the φr
M(R′,S ) forK≤M≤N andφl
M(R′,S ) for 0≤M≤K. This means
we need to do about N updates for just one accepted R′
K (which is not economical),
and therefore totally about N 2 updates for all the beads if they are accepted. Besides,
single bead sampling usually has a very high acceptance rate, this indicates that the
beads may not be moved far enough in the conﬁguration space. Therefore it should
not be used often in the program. It is however simple, and can be used as a check for
more complicated algorithms.
