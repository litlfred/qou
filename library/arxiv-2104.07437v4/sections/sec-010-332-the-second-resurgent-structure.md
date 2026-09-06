---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-010-332-the-second-resurgent-structure
section_title: "The second resurgent structure"
section_number: 3.3.2
pages: 30-34
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
doc_brief: "Peacock patterns and new integer invariants in topological string theory — Topological string theory near the conifold point of a Calabi–Yau threefold gives rise to factorially divergent power series"
---
We can use the conifold free energies to construct the formal power series Φ 0;2(gs) at N = 2.
Instead we will consider the following normalised series 10
Φ′
0;2(gs) = 1 + 8π2gs
9
√
3
Φ0;2(gs)
Φ0;1(gs)2 =
∑
n≥0
angn
s
= 1 + 8π2gs
9
√
3 + 16π4g2
s
81 + 64π6g3
s
729
√
3− 64π8g4
s
19683 +...
(3.121)
10The fact that the normalised series has no exponential factor indicates that the leading contribution to
Φ0;2(gs)∼Z2(ℏ) is indeed exp(2VP2/gs) as predicted by (3.8).
– 29 –
ϕ0;2(gs)
Figure 9. The singularities in the Borel plane for the series ϕ0;2(gs)
Up to normalisation, this is the power series associated to the normalised second trace
Tr′ρ2
P2 := Trρ2
P2
(TrρP2)2 = 1− 2Z2(ℏ)
Z1(ℏ)2. (3.122)
As we will see, the advantage of working with this series is that its resurgent structure is simpler.
In the remainder of this section and the following sections we will drop the prime and always
refer to the normalised series (3.121) when we use the symbol Φ 0;2(gs). We will refer to BΦ0;2 as
the second resurgent structure of local P2.
The resurgent structure associated to Φ 0;2(gs) is quite interesting. The Borel transform
ˆΦ0;2(ζ) has one family of inﬁnitely many singularities in the ﬁrst and the fourth quadrants as
illustrated in Fig. 9, and they are located at
3VP2 + in, n ∈ 1
2 + Z. (3.123)
This indicates that there exists a second family of asymptotic series, which we denote by
Φ1,n;2(gs) = Φ1;2(gs)e−n i
gs, n ∈ 1
2 + Z. (3.124)
Note that here we have generalized the convention (2.32) in Section 2.3 in order to emphasize
the reﬂection symmetry of the singularities in the Borel plane. In (3.124),
Φ1;2(gs) = e−
3VP2
gs ϕ1;2(gs), (3.125)
and we assume ϕ1;2(gs) has the general form
ϕ1;2(gs) = (−gs)−ν
∞∑
n=0
an,1gn
s. (3.126)
To uncover the nature of the series ϕ1;2(gs), we focus on the two nearest singularities
ζ1 := 3VP2 + i
2, ζ ∗
1 = 3VP2− i
2, (3.127)
– 30 –
which are conjugate to each other. It follows from standard resurgent analysis that the perturba-
tive seriesϕ1;2(gs) at these two singular points control the large order behavior of the coeﬃcients
an of the series Φ 0,2(gs), albeit in a more complicated form
an∼ S01,0;2
π
∞∑
k=0
|ζ1|k−n−νΓ(n +ν−k)|ak,1| sin(θk− (n +ν−k)θ). (3.128)
Here,
θ = argζ1, θ k = argak,1. (3.129)
Therefore, it should be possible to extract the coeﬃcients ak,1 from the large order behavior of
the series an. Since the asymptotics is oscillatory, one can not apply the standard Richardson
transform which is often used in resurgent analysis. It turns out that, for this type of oscillatory
behavior, there is a numerical algorithm due to Hunter and Guerrieri [87] which makes it possible
to extract the coeﬃcients ak,1 (see Appendix C for an explanation of this algorithm). By using
this algorithm, we ﬁnd
S01,0;2ϕ1;2(gs) =−21/239/4π−1/2g−1/2
s exp
(π2gs
2
√
3− 4π6g3
s
405
√
3 +...
)
, (3.130)
which turns out to be proportional to Φ 0;1(gs)−3. We choose the normalisation S01,0;2 = 1 so
that the second asymptotic series associated to the normalised second trace reads
Φ1;2(gs) =−21/239/4π−1/2g−1/2
s Φ0;1(gs)−3. (3.131)
Since by Stokes automorphism Φ 0;1(gs), and hence Φ 1;2(gs), transforms back to itself, the two
families of power series{Φ0,n;2(gs), Φ1,n;2(gs)} form a minimal resurgent structure. The complete
set of Borel singularities of this minimal resurgent structure is illustrated in Fig. 10. Stokes rays
passing through these singular points divide the complex plane into inﬁnitely many sectors in
the ﬁrst and the fourth quadrants. As usual we denote the sectors bordering the positive real
axis in the ﬁrst and the fourth quadrants as I,IV and sometimes refer to the second and the
third quadrants as sectors II,III .
Following the pattern of Stokes rays we can collect all the Stokes constants in the 2 × 2
Stokes matrix
S2(q) =
(0 S01;2(q)
0 S11;2(q)
)
, (3.132)
and then decompose it as
S2(q) = S+
2 (q) + S−
2 (q), (3.133)
where S+
2 (q) and S−
2 (q) are respectively q- and q−1-series encoding Stokes constants in the upper
and lower half planes. Here we choose for q the same convention as in the previous subsection
q = e2πib2
= e3iℏ = e− 3i
gs, (3.134)
so that the entries of S2(q) are
S01;2(q) =q
1
6
∞∑
n=0
S01,n;2q
n
3, S11;2(q) =
∞∑
n=1
S11,n;2q
n
3. (3.135)
– 31 –
III
III IV
Figure 10. Stokes rays and sectors in the gs-plane for the series ϕ0;2(gs),ϕ 1;2(gs) in the second resurgent
structure of local P2.
Since under complex conjugation
Φ−;2(gs)∗ = Φ−;2(g∗
s), (3.136)
it follows that
S−
2 (q) = (1 + S+
2 (q−1))−1− 1, (3.137)
and we only have to compute S+
2 (q). The component S+
11;2(q) can be immediately identiﬁed
S+
11;2(q) = (1+ S+
1 (q))−3−1 =−9q1/3+45q2/3−165q+486q4/3−1197q5/3+2517q2+.... (3.138)
The ﬁrst term of S+
01;2(q) is q1/6 by our normalisation. More terms of S+
01;2(q) can again be
computed by using the TS/ST correspondence and radial asymptotic analysis, to which we will
momentarily turn. We end this subsection by recording the results here
S+
01;2(q) =q1/6(1− 3q1/3 + 10q2/3− 29q + 72q4/3− 155q5/3 + 291q2− 474q7/3 + 660q8/3− 760q3
+ 663q10/3− 309q11/3− 193q4 +... ). (3.139)
Using (3.137) we can write down the following Stokes constants in the lower half plane as well:
S−
11;2(q) =(1 + S+
1 (q−1))3− 1 = 9q−1/3 + 36q−2/3 + 84q−1 + 135q−4/3 + 198q−5/3 + 327q−2 +...,
S−
01;2(q) =− S+
01;2(q−1)/(1 + S+
11;2(q−1))
=−q−1/6(1 + 6q−1/3 + 19q−2/3 + 37q−1 + 54q−4/3 + 82q−5/3 + 135q−2 + 174q−7/3
+ 171q−8/3 + 234q−3 + 399q−10/3 + 406q−11/3 + 273q−4 +... ). (3.140)
The diagonal Stokes constants in the series S11;2(q) are responsible for the automorphism of
Φ1;2(gs) back to itself and they are similar to Stokes constants in S00;1(q) which are illustrated
in Fig. 8. The oﬀ-diagonal Stokes constants in the series S01;2(q) are illustrated in Fig. 11.
– 32 –
ϕ0;2(gs)
1
−3
10
−29
−1
−6
Figure 11. Oﬀ-diagonal Stokes constants for the second resurgent structure of local P2.
