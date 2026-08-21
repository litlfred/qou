---
doc_id: arxiv-gr-qc-0407052v1
doc_title: "Black hole entropy in loop quantum gravity"
section_id: sec-000-abstract
section_title: "Abstract"
section_number: null
pages: 1-9
source_pdf: 0407052v1.pdf
source_sha256: 4624ea2fb4d318ad
doc_brief: "Black hole entropy in loop quantum gravity — We calculate the black hole entropy in Loop Quantum Gravity a s a function of the horizon area and provide the exact formula fo r the leading and"
---
We calculate the black hole entropy in Loop Quantum Gravity a s a
function of the horizon area and provide the exact formula fo r the
leading and sub-leading terms. By comparison with the Beken stein–
Hawking formula we uniquely ﬁx the value of the ’quantum of ar ea’
in the theory.
The Bekenstein–Hawking formula gives the leading term in th e entropy
of the black hole in the form
S = 1
4
A
l2
P
(1)
where lP is the Planck length and A is the black hole horizon area. According
to the common belief, the entropy is always connected with th e logarithm of
the number of microscopic states realizing a given macrosco pic state. The
fact that the entropy in (1) is proportional to the area (and not as is usual to
the volume) has led to the formulation of the so called holographic principle.
It was however diﬃcult to ﬁnd the microscopic states that cou ld account for
such an entropy.
The problem was attacked in two diﬀerent approaches – in stri ng theory
[1]-[5] and in Loop Quantum Gravity [6]-[10] (see also the re view [11]). The
latter approach is based on a quantum theory of geometry. The basic ge-
ometric operators were introduced in [12, 13] and a detailed description of
the quantum horizon geometry was introduced using the U(1) Chern-Simons
theory in [10] where one can ﬁnd the detailed discussion of th e states on the
horizon of the black hole (see also [14]). However, the proce dure introduced
in [10] for state counting contained a spurious constraint o n admissible se-
quences and the number of the relevant horizon states is unde restimated.
The correct method of counting was proposed in [14] but that a nalysis pro-
vides only lower and upper bounds on the number of states. The purpose
of this paper is to rectify this situation. We will provide th e correct value
1
of the Barbero-Immirzi parameter that is needed to obtain ag reement with
the Hawking-Bekenstein formula for large black holes. Furthermore, since we
are able to calculate the number of states to suﬃcient accura cy, we also rig-
orously obtain the precise sub-leading quantum correction to the Hawking-
Bekenstein formula. The physical aspects of this result wil l be discussed
elsewhere [15].
As it was shown in [14] the proper counting of states is given b y all
sequences (of arbitrary length) of mi ∈ Z/ 2, m i ⁄= 0 such that
∑
i
√
|mi|(|mi| + 1) < a (2)
where
a = A
8πγl 2
P
(3)
and γ is a parameter introduced in [16]. Addditionally we have to i mpose
the condition ∑
i
mi = 0. (4)
It is our task to calculate the number of sequences satisfyin g (2) and (4).
We start with the sequences without (4) imposed. If we denote by N(a)
the number of sequences satisfying (2) then we can split the c ounting into
the ﬁrst number m1 and the rest and write the recurrence relation
N(a) = θ (a −
√
3/ 2)
(
2N(a −
√
3/ 2) + 2N(a −
√
2) + . . .
+2N(a −
√
|mi|(|mi| + 1) + . . . + 2
[ √
4a2 + 1 − 1
])
(5)
where the symbol [ . . . ] denotes the integer part. The ﬁrst term on the RHS
corresponds to sequences with at least two elements and m1 = ±1/ 2, the
second to sequences with at least two elements and m1 = ±1 and so on and
the last term to sequences consisting of just m1 and nothing else.
We now assume (we will later prove that it is indeed the case) t hat the
leading part of the solution of the recurrence relation (5) i s for large a given
by
N(a) = Ce 2πγ M a (6)
where γ M is a constant to be determined.
2
Plugging the form (6) into (5) we get
1 =
∞∑
k=1
2 e−2πγ M
√
k(k+2)/ 4 (7)
where we neglected terms vanishing in the limit a → ∞. The solution to this
equation can be found numerically and reads
γ M = 0. 23753295796592 . . . (8)
We see that the coeﬃcient of growth γ M is between the lower and upper
bounds given in [14] i.e. ln 2
π < γ M < ln 3
π . It seems that γ M deﬁned by
(7) cannot be calculated analytically or given as a solution of any “simpler”
equation. In the present paper we will also use ˜γ where
˜γ M := 2πγ = 1. 492463591462379 . . . (9)
Since the condition (4) (as we will later prove) gives only po wer-like cor-
rections to N(a) therefore for large a we have from (6)
S = lnN(a) = γ M
4γ
A
l2
P
+ O(lnA). (10)
The comparison with the Bekenstein–Hawking formula (1) giv es therefore
the unambiguous result
γ = γ M (11)
so this physical requirement uniquely ﬁxes the value of γ and hence the
’quantum of area’ in the theory.
One may note that the exponential ansatz (6) works in many oth er cases
for example if the number of states for a given spin j was (2j + 1) instead of
2 one would have in (7) ( k + 1) instead of 2 in front of the exponential and
the appropriate γ M would be equal to 0 . 273985635 . . . .
We now prove that the assumption (6) is actually correct and a t the end
we add the condition (4) – the ﬁnal result will not modify (11)and will enable
us to ﬁnd the sub–leading (logarithmic) correction to the formula for entropy
(10).
We introduce the Laplace transform of N(a):
P (s) :=
∫ ∞
0
da N(a) e−sa. (12)
3
The transform is well deﬁned since we know thatN(a) is piecewise continuous
and of exponential order i.e. it is bounded by Ke −βa for some K and β ([14]).
Integrating the relation (5) over a from 0 to ∞ we get an exact result
P (s) = 2∑ ∞
k=1 e−s
√
k(k+2)/ 4
s
(
1 − 2∑ ∞
k=1 e−s
√
k(k+2)/ 4
) . (13)
If all the poles of the Laplace transform are distinct and of ﬁ nite order then
we can make analytical continuation to the complex half-pla ne Re( s) > 0,
excluding positions of the poles, i.e. beyond the region all owed by the def-
inition (12). We now use the well known fact that the growth of N(a) is
determined by the poles of P (s) i.e.
N(a) =
∑
si, Re(si)>0
ressiesia + O(an) (14)
(we assumed here that all the poles are simple – otherwise we w ould have to
add some powers of a in front of the exponentials). Therefore our problem
boils down to determination of such complex si that satisfy
G(si) − 1
2 = 0 (15)
where we deﬁned
G(s) :=
∞∑
k=1
e−s
√
k(k+1)/ 4. (16)
It is important to analyze the distribution of zeroes of ( G(s) − 1
2) in more
detail. Since G(s) is complex analytic in the open domain Re( s) > 0 all the
zeroes are distinct, of ﬁnite order and there is no point of ac cumulation of
zeroes inside this domain. Therefore we have to analyze the d omain’s border
i.e. the imaginary line Re( s) = 0. To analyze the limit when Re( s) ց 0
deﬁne a new function Gr(s) by subtracting two analytic (for Re( s) > 0)
functions
Gr(s) := G(s) −
∞∑
k=1
e−s(k+1)/ 2 − s
4
∞∑
k=1
e−s(k+1)/ 2
k (17)
The function Gr(s) is well deﬁned in the whole domain Re(s) ≥ 0, continuous
and doesn’t have any singularities in this domain. On the oth er hand two
4
subtracted functions have a well deﬁned limit when Re( s) ց 0 so we can
write
G(s) = Gr(s) + e−s/ 2
es/ 2 − 1 − se−s/ 2
4 ln
(
1 − e−s/ 2)
. (18)
We see that apart from singularities at s = 4 π in, the function G(s) has
a well deﬁned limit when Re( s) ց 0 and in the domain Re( s) > 0 it is
complex analytic so in the whole domain Re( s) ≥ 0 there can be no points
of accumulation of zeroes – therefore all zeroes of the funct ion G(s) − 1
2 in
the whole domain Re( s) ≥ 0 must be distinct and of ﬁnite order.
The only real zero is given by (9):
s = ˜γ M . (19)
Close to this zero the function P (s) behaves as
P (s) ∼ CM
s − ˜γ M
(20)
where
CM = − 1
2˜γ M G′(˜γ M) = 0. 509202564 . . . (21)
Therefore the leading behaviour for large a is given by
N(a) = CM e˜γ M a (22)
as was to be shown.
The complex zeroes of the function G(s) − 1
2 for Re(s) > 1. and |Im(s)| <
100 are listed below:
Re(s) Im(s)
1.49246359. . . 0
1.22393017. . . ± 22.1530069. . .
1.41016352. . . ± 35.9362749. . .
1.30363023. . . ± 58.0472739. . .
1.18587535. . . ± 71.8281531. . .
1.17654302. . . ± 79.9673974. . .
1.07191106. . . ± 87.4120423. . .
1.21660746. . . ± 93.9713059. . .
5
It is easy to prove that all the complex zeroes (i.e. poles of P (s)) with nonva-
nishing imaginary part must have smaller real part than ˜γ M so in comparison
to the leading behaviour (22) they give exponentially small (and rapidly os-
cillating) contribution to N(a).
To illustrate the method in the cases where the number of sequ ences is
explicitly known let us give two examples. For sequences of h alf-integers
with the condition ∑ |mi| < a the number of sequences is 3 [2a] − 1 and by
the method described above we get
P (s) = 2
s (es/ 2 − 3) (23)
and indeed the real pole is equal to 2 ln 3. For sequences of half-integers with
the condition∑ (|mi|+ 1/ 2) < a the number of sequences is 1
3(2[2a]+1 ±1) −1
(where + is for even and − for odd [2 a]) and
P (s) = 2
s (es − es/ 2 − 2) (24)
and indeed the positive real pole is equal to 2 ln 2. The actual numbers
of sequences in both cases indeed show that the leading behav iour is given
precisely by the largest positive real pole of P (s).
It can be useful to discuss how diﬀerent ways of deﬁning the se quences
are reﬂected in the properties of P (s). We have essentially three diﬀerent
“statistics”.
• Boltzmann statistics (used in this paper): all sequences sa tisfying the
condition are allowed and are treated as diﬀerent. Therefor e P (s) is
given by eq. (13):
P (s) = 2∑ ∞
k=1 e−s
√
k(k+2)/ 4
s
(
1 − 2∑ ∞
k=1 e−s
√
k(k+2)/ 4
) (25)
which has the largest positive real pole equal to γ M.
• the intermediate statistics (between Boltzmann and Bose): it requires
that |mi+1| ≥ | mi| but treats for example (+ 1
2, − 1
2, + 1
2, . . . ) as diﬀerent
from (− 1
2 , + 1
2, + 1
2, . . . ) – then we have
P (s) =
∞∏
k=1
1(
1 − 2e−s
√
k(k+2)/ 4
) (26)
6
which has the largest positive real pole given by k = 1: s = 2ln 2√
3 .
• Bose statistics: it requires not only that |mi+1| ≥ | mi| but treats for
example (+ 1
2, − 1
2, + 1
2, . . . ) as the same as ( − 1
2 , + 1
2, + 1
2, . . . ) i.e. the
allowed sequences have the form (1
2, . . . , − 1
2 , . . . , +1, . . . , −1, . . . ). Then
we have
P (s) =
∞∏
k=1
1(
1 − e−s
√
k(k+2)/ 4
) 2 (27)
and this P (s) does not have a pole with Re( s) > 0 at all so N(a) must
have milder growth than ec′a. However when s → 0 the function P (s)
behaves as P (s) ∼ e
2ζ (2)
s where ζ (s) is the Riemann’s zeta function.
Hence we have accumulation of zeroes at s = 0 and the inverse Laplace
transform gives the exponential growth with √a:
N(a) ∼ ac e
√
8ζ (2)a (28)
(this type of statistics and therefore similar formula give s for example
the degeneracy of states in string theory).
At the end we impose the condition (4) i.e. ∑ mi = 0. We introduce
N(a, p ) as the number of sequences satisfying
∑
i
√
|mi|(|mi + 1) < a (29)
and ∑
i
mi = p (30)
where p ∈ Z/ 2 and a ≥
√
|p|(|p| + 1). We can write the recurrence relation
as
N(a, p ) = θ (a −
√
3/ 2)θ (a −
√
|p|(|p| + 1)) ×(
N(a −
√
3/ 2, p − 1/ 2) + (N(a −
√
3/ 2, p + 1/ 2)+
+N(a −
√
2, p − 1) + N(a −
√
2, p + 1) + . . . + 1
)
. (31)
where the ﬁrst term inside the brackets on the RHS corresponds to sequences
with at least two elements and m1 = + 1
2, the second to sequences with at
7
least two elements and m1 = − 1
2 and so on and the last term to sequences
consisting of just m1 (which must be equal to p).
Next we deﬁne P (s, ω ) as the Fourier transform with respect to p and
Laplace transform with respect to a of N(a, p ):
P (s, ω ) :=
∑
p∈Z/ 2
∫ ∞
0
da N(a, p ) eiωp e−sa. (32)
Then summing and integrating eq. (31) we get
P (s, ω ) = 2
s
∞∑
k=1
e−s
√
k(k+2)/ 4
(
1 − 2
∞∑
k=1
e−s
√
k(k+2)/ 4 cos(kω/ 2)
) −1
(33)
where we neglected some contributions from the endpoints ( p ∼ a) what will
be justiﬁed a posteriori. Therefore we have to ﬁnd the zeroes of the function
inside the bracket on the RHS of (33). With ω = 0 we know that the only
real zero (i.e. the one that gives the leading behaviour) is e qual to s = ˜γ M.
Expanding around s = ˜γ M we get
1 − 2
∞∑
k=1
e−˜γ M
√
k(k+2)/ 4
(
1 − (s − ˜γ M)
√
k(k + 2)/ 4 − k2ω 2/ 8 + O(ω 4)
)
= 0.
(34)
Hence the pole of P (s, ω ) is given by
s = ˜γ M − β M ω 2 + O(ω 4) (35)
where
β M = −
∑ ∞
k=1 k2e−˜γ M
√
k(k+2)/ 4
8G′(˜γ M) = 0. 475841255 . . . (36)
Therefore the leading behaviour of N(a, p ) is given by
N(a, p ) = CM
2π
∫
dω e −iωp e˜γ M a−β M ω 2a = CM√4πβ M a e2πγ M a e−p2/ (4β M a). (37)
As we see the endpointsp ∼ a are exponentially small justifying (33). Also we
see a posteriori that the terms O(ω 4) from (35) would give in (37) corrections
of relative size 1 /a so for large a we can neglect them.
8
Note that the gaussian distribution with respect to p in (37) with the
mean square deviation of the order of √a can be expected by the analogy
with the random walk where the average distance is zero and the mean square
deviation is of the order of square root of the number of steps .
Imposing the condition p = 0 we get the ﬁnal result
N(a, 0) = CM√4πβ M a e2πγ M a. (38)
Therefore the entropy is given by
S = lnN(a, 0) = γ M
4γ
A
l2
P
− ln(A/l 2
P )
2 + O(1) (39)
so for large A/l 2
P we conﬁrm (10) as the leading behaviour and we can un-
ambiguously both get the physical value of γ equal to γ M (given in (8))
and resolve the controversy (summarized in [17]) about the c oeﬃcient of the
logarithmic term ﬁxing it to − 1
2.
Acknowledgement The author would like to acknowledge valuable dis-
cussions with Abhay Ashtekar and Jerzy Lewandowski and than k Hermann
Nicolai for the invitation to the Albert Einstein Institute in Golm where part
of this work was done. The work partially supported by the Polish KBN grant
2P03B 001 25 and the European Programme HPRN–CT–2000–00152 .
