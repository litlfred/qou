---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-017-24-wave-function
section_title: "Wave Function"
section_number: 2.4
pages: 35-42
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
From Eq.(2.1) we know that an initial trial wave function Ψ T is needed. Like all
QMC calculations, the closer the trial wave function Ψ T is to the ground state, the
faster and the lower variance the calculation will become. In fact, obtaining a high
quality trial wave function is always an important task for QMC.
The state of the trial wave function |ΨT⟩ in this work takes the following form
(Carlson et al. (2015)),
|ΨT⟩ =F|Φ⟩, (2.37)
where|Φ⟩ is the model state, and F is the correlation operator.
Since nucleons are fermions, the model state |Φ⟩ has to be antisymmetric under
the exchange of the labels between any of the two particles. For A≤ 4 it can be
decomposed as a spatial part and a spin isospin part,
|Φ⟩ =|ΦR⟩⊗| ΦS⟩. (2.38)
The spatial part|ΦR⟩ is symmetrized which can be chosen as,
|ΦR⟩ =
∫
dR|R⟩, (2.39)
such that
⟨R′|ΦR⟩ =
∫
dR⟨R′|R⟩ =
∫
dRδ(R′−R) = 1. (2.40)
Since the spatial part is symmetric, the spin-isospin part |ΦS⟩ has to be antisym-
metric under the exchanges of labels between any of the two particles. For light nuclei
with A ≦ 4, we can pick a basis state |S′⟩≡| s′
1
1⟩⊗| s′
2
2⟩⊗ ..⊗|s′
A
A⟩≡| s′
1
1s′
2
2...s′
A
A⟩
25
from any one of the NS =
(A
Z
)
× 2A spin-isospin basis|S⟩, then construct|ΦS⟩ using
A byA Slater determinant of single particle states in such a form,
|ΦS⟩=A|s′
1
1s′
2
2..s′
A
A⟩ =
NS∑
N=1
φN|N⟩, (2.41)
where the number φN is either -1, 1 or 0 depends on whether a certain spin-isospin
state|N⟩ from the NS states|S⟩ has odd permutation (exchanging the particle labels
between two particles), even permutation or any overlap with the chosen |S′⟩ under
any permutation or not.
The projection of|ΦS⟩ on state|S⟩≡| s1
1s2
2s3
3s4
4⟩ is the amplitude⟨S|ΦS⟩ which is
calculated by,
⟨S|ΦS⟩ =
⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐
⟨s1
1|s′1
1⟩ ⟨ s2
2|s′2
1⟩ ... ⟨sA−1
A−1|s′A−1
1 ⟩ ⟨sA
A|s′A
1⟩
⟨s1
1|s′1
2⟩ ⟨ s2
2|s′2
2⟩ ... ⟨sA−1
A−1|sA−1
2 ⟩ ⟨ sA
A|sA
2⟩
... ... ... ... ...
⟨s1
1|s1
A−1⟩ ⟨s2
2|s′2
A−1⟩ ... ⟨sA−1
A−1|sA−1
A−1⟩ ⟨sA
A|sA
A−1⟩
⟨s1
1|s1
A⟩ ⟨ s2
2|s′2
A⟩ ... ⟨sA−1
A−1|sA−1
A ⟩ ⟨ sA
A|sA
A⟩
⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐
=φS, (2.42)
where the overlap between the spin-isospin state |s′N
j⟩ of particle N and|s′M
j ⟩ of
particle M is,
⟨sM
i |s′N
j⟩ =⟨si|s′
j⟩δMN =δsi,s′jδMN. (2.43)
Note that⟨S|ΦS⟩ is a fermion wave function and it is antisymmetric under the
particle label exchange between two particles. If|S′′⟩ is obtained from|S⟩ by exchanging
the i and j particle labels, then⟨S′′|ΦS⟩ is the determinant in Eq.(2.42) with i and j
columns exchanged, which obviously becomes−⟨S|ΦS⟩.
By using Eqs.(2.40–2.42), the wave function ⟨RS|Φ⟩ is calculated as,
⟨RS|Φ⟩ =⟨R|ΦR⟩⟨S|ΦS⟩ =
NS∑
N=1
φN⟨S|N⟩ =φS. (2.44)
26
Again, take 4He as an example, we can pick any one of the states from the 96
basis, and then antisymmetrize it to form the spin isospin part |ΦS⟩ which will then
be a linear combination of 4! = 24 non-zero basis states. We can pick a basis state
|S′⟩ =|n↑1n↓2p↑3p↓4⟩ from the basis, then antisymmetrize it to form |ΦS⟩ of 4He,
|ΦS⟩ =
96∑
N=1
|N⟩⟨N|ΦS⟩ =
96∑
N=1
φN|N⟩, (2.45)
whereφN =⟨N|ΦN⟩ is either−1 or 1 depending on the antisymmetrization for each
of the 24 basis states, and 0 for the rest 72 basis states. For example, using Eq.(2.42)
one can ﬁnd if|N⟩ =|n↑1n↓2p↑3p↓4⟩ then φN is 1, if|N⟩ =|n↑2n↓1p↑3p↓4⟩ then
φN is -1, if|N⟩ =|n↑2n↓1p↑3p↑4⟩ then φN is 0, etc.
The correlation operatorF is represented by the products of two-body correlation
operators Fij,
F =S
∏
i<j
Fij, (2.46)
whereS is the symmetrization operator, and Fij is,
Fij =
6∑
p=1
fp
ijOp
ij, (2.47)
where Op
ij are the same AV6’ operators, and fp
ij is the corresponding correlation
function operator (Lomnitz-Adler et al. (1981)). After operating on |R⟩, fp
ij will
become a function fp
ij(rij) which only depends on the distance rij between particle i
and j.
By using Eqs.(2.33–2.47), the trial wave function ⟨RS|ΨT⟩ is calculated as,
⟨RS|ΨT⟩=⟨R|⊗⟨ S|F|ΦR⟩⊗| ΦS⟩=
⟨
S
⏐⏐⏐⏐⏐S
∏
i<j
[ 6∑
p=1
fp
ij(rij)Op
ij
] NS∑
N=1
φN
⏐⏐⏐⏐⏐N
⟩
. (2.48)
The trial wave function ⟨RS|ΨT⟩ with correlation operators Eq.(2.47) enriches
the structure of the wave function, especially, it has the important tensor structure
(Carlson et al. (2015)), and thus is an improvement over those without Op
ij operators.
27
However, such a trial wave function is usually expensive to calculate. Even if Op
are just 1, it will take at least 96 × 6 = 576 operations for a given pair. And we have
4 particles so 6 pairs, so 576× 6 = 3456 operations. Then there is a symmetrizer S
which contribute another factor of 6! = 720. So totally at least 3456 ∗ 720 = 2488320
operations for computing just one ⟨RS|ΨT⟩. In general, for a nuclei, without further
simplifying⟨RS|ΨT⟩, brute force calculation for AV6’ can take at least
(A
Z
)
× 2A× 6×
[A(A−1)/2]×[A(A−1)/2]! operations. This is computationally too expensive. Because
of that, in this work, as well as in most other QMC methods like AFDMC (Schmidt
and Fantoni (1999)), it is sampled instead of summing over all the [A(A− 1)/2]!
symmetrized terms.
In our calculation, we use ‘l’ to denote a sampled order ⟨Ψl
T| from⟨ΨT|, and use
‘r’ to denote a sampled order |Ψr
T⟩ from|ΨT⟩. So, it is,
⟨ΨT| =
∑
l
⟨Ψl
T|, (2.49)
|ΨT⟩ =
∑
r
|Ψr
T⟩. (2.50)
We can write⟨ΨT|RS⟩ and⟨RS|ΨT⟩ as,
⟨ΨT|RS⟩ =
∑
l
⟨Ψl
T|RS⟩, (2.51)
⟨RS|ΨT⟩ =
∑
r
⟨RS|Ψr
T⟩, (2.52)
and⟨RS|Ψr
T⟩ and⟨Ψl
T|RS⟩ are,
⟨RS|Ψr
T⟩ =
⟨
S
⏐⏐⏐⏐⏐
∏r
i<j
[ 6∑
p=1
fp
ij(rij)Op
ij
] 96∑
N=1
φN
⏐⏐⏐⏐⏐N
⟩
, (2.53)
⟨Ψl
T|RS⟩ =
96∑
N=1
⟨
N
⏐⏐⏐⏐⏐φ∗
N
∏l
i<j
[ 6∑
p=1
fp
ij
∗(rij)Op
ij
]⏐⏐⏐⏐⏐S
⟩
, (2.54)
where we use symbols
∏r
i<j
and
∏l
i<j
to denote a particular chosen ‘ r’ and ‘l’
order fromS∏
i<j. This l and r order sampling totally reduces the cost by the factor
28
of{[A(A− 1)/2]!}2. For 4He that is (6!)2 = 518400. Since the operator commutators
are relatively small, so all the [A(A− 1)/2]! terms from either⟨Ψl
T| or|Ψr
T⟩ are almost
the same, therefore the variance increase from sampling this operator order is also
small.
It needs to be pointed that, |ΦS⟩ (and therefore |Φ⟩) does not have to be just
one Slater determinant, it can be (sometime it better be) a linear combination of
several diﬀerent Slater determinants formed from diﬀerent antisymmetrized basis states.
Overall, that is to say, using a linear combination of Slater determinant to form |Φ⟩
may be required to obtain the correct quantum numbers for a nucleus. To say the
least, the deuteron ground state must have J =S = 1 (Siemens and Jensen (2018)).
For theA >4 system, merely the four spin-isospin states |n↑⟩,|n↓⟩,|p↑⟩ and
|p↓⟩ are not enough to form the antisymmetric state |Ψ⟩ in Eq.(2.37). If we were to
use single-particle states to form |Ψ⟩ by Slater determinants, they have to contain
some orbital quantum number information. For example we can use single particle
orbital (Zeng (2013); Xu (2009)) inspired from shell model (Mayer (1964)).
We can mark such a shell-model-like single-particle state as|sK
i⟩nljmj as illustrated
in Fig. 2.3. The symbol K means it is the state of particle K. Letter i can be from
0 to 4 and they denote spin-isospin state n↑, n↓, p↑, n↓ accordingly. Quantum
numbern is the radial quantum number, l is the orbit angular momentum quantum
number,j is the total angular momentum quantum number and mj is the j projection
quantum number. For simplicity, we can use|φK
α⟩ to denote|sK
i⟩nljmj,
|φK
α⟩≡| sK
i⟩nljmj, (2.55)
where symbol α contains all the spin-isospin information si and orbital information
nljmj,
α ={si,nljm j}. (2.56)
29
Figure 2.3: Single-particle orbital states|sK
i⟩nljmj.
and the amplitude between|φK
α⟩ and particle M’s basis|rM
j sM
j ⟩ is⟨rM
j sM
j |φK
α⟩ which
can be written as,
⟨rM
j sM
j |φK
α⟩ =φα(rj,sj)δsj,siδMK. (2.57)
The function φα(rj,sj) is usually called an orbital and it can be written as,
φα(rj,sj) =Rnl(rj)Y
jmj
l , (2.58)
whereRnl(r) is a radial function which can be found from the solution of some central
potential such as Woods-Saxon potential (Lonardoni et al. (2018b)), and Y
jmj
l is
a simultaneous eigenfunction of l2,s2 andj2 called spin-angular function (Sakurai
(1993)). Y jm
l is a spin spherical harmonic Ym
l multiplied by some coeﬃcients which
are functions of l, j and mj. ,
Assuming there arenφ ways to pickA suitable single-particle states|φK
α⟩ which can
produce the correct total angular momentum J, parity π and total isospin quantum
30
numberT of a give A-nucleon nucleus, and the state |Φ⟩ can be written as a linear
combination of nφ Slater determinants|Dq
Φ⟩,
|Φ⟩ =
nφ∑
q=1
cq|Dq
Φ⟩, (2.59)
where cq is some coeﬃcient and the amplitude ⟨RS|Dq
Φ⟩ can be calculated by using
Eq.(2.57) as,
⟨RS|Dq
Φ⟩ =
⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐
⟨r1
1s1
1|φ1
1⟩ ... ⟨rA
AsA
A|φA
1⟩
... ... ...
⟨r1
1s1
1|φ1
A⟩ ... ⟨rA
AsA
A|φA
A⟩
⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐
=
⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐
φ1(r1s1) ... φ 1(rAsA)
... ... ...
φA(r1s1)⟩ ... φ A(rAsA)
⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐
. (2.60)
Figure 2.4: Single-particle orbital states of 16O(0+, 0)
For example, consider 16O(0+, 0) whose total angular momentum quantum number
and parity is Jπ = 0+ and isospin quantum number is T = 0. From the knowledge of
shell model, as illustrated in Fig. 2.4, we know that 16O(0+, 0) is a closed shell nucleus.
31
All the 16 particles fully occupy the N = 1 and N = 2 shells. Among them, 4 occupy
the 1S1/2 states, 4 occupy the 1P1/2 states and 8 occupy the 1P3/2 states. So totally 16
particles occupy 16 diﬀerent orbital. So we can form one 16 by 16 Slater determinant
to describe the wave function of 16O.
However, for open-shell nuclei, there are more single-particle orbital states than
the number of nucleons A. Therefore in order to form the |Φ⟩ in Eq.(2.59), all the
possible orbital states may need to be picked to form the accordingly total number of
nφ Slater determinants. E.g., 6He(0+, 1) needs 9 Slater determinants, 6Li(1+, 0) needs
32 and 12C(0+, 0) needs 119 (Lonardoni et al. (2018b)). Also, considering each Slater
determinants needs to be operated by the correlation operator F in Eq.(2.46) in order
to form|ΨT⟩ in Eq.(2.37), the computational cost of calculating open-shell nuclei is
much higher than closed-shell nuclei.
Last but not least, it needs to be pointed out that, the wave function does not
have to be formed by the Slater determinants using single-particle orbital. We can
also use paired states to form the antisymmetrized fermion wave functions in the
Pfaﬃan form (Bouchaud et al. (1988); Bajdich et al. (2006)). In fact, making the wave
function relatively cheap to calculate while making it containing as much of ground
state information as possible is one of the most important tasks in QMC calculations.
