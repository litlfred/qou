---
doc_id: arxiv-2312.00624v1
doc_title: "On the structure of wave functions in complex Chern–Simons theory"
section_id: sec-016-conclusions
section_title: "Conclusions"
section_number: null
pages: 36-38
source_pdf: 2312.00624v1.pdf
source_sha256: bda867f7b84f69c3
doc_brief: "On the structure of wave functions in complex Chern–Simons theory — We study the structure of wave functions in complex Chern–Simons theory on the complement of a hyperbolic knot, emphasizing the"
---
In this paper, we have made various observations on the structure of the wave functions in CS theory
with gauge group SL(2, C) on the complement of a hyperbolic knot in the three-sphere. We have first
conjectured explicit integrality properties for the resummed WKB expansion of the wave function,
which can be tested directly using the decomposition into holomorphic/anti-holomorphic blocks.
Our integrality conjecture guarantees that the singularities appearing in the holomorphic blocks
at rational values of ℏ get canceled against those occurring in the corresponding anti-holomorphic
blocks. We have then developed various techniques to compute the wave function in the rational
case effectively. In particular, we have analyzed the quantum A-polynomial at rational points by
exploiting the underlying quasi-periodic structure, and we have solved the associated q-dfference
equation in closed form in the general cases of order two and three. The calculation methods we
have introduced have been applied to the examples of the figure-eight and the three-twist knots, and
our conjectural statements have been verified. Finally, we have performed a direct evaluation of the
Andersen–Kashaev state integral of the figure-eight knot at rational values, which gave us further
insights into the properties of the exact wave functions. All computational approaches have yielded
compatible results.
Our investigation raises two main questions. The first one concerns the interpretation of the
integrality structure of the resummed WKB expansion of the wave function in terms of an enumer-
ative problem, or a BPS counting problem, in the dual supersymmetric theory [42]. The second
one concerns the shape of the wave function obtained by directly evaluating the state integral. As
highlighted in Section 5, this is enticingly similar to the functional profiles of the ground state wave
functions computed in the context of the TS/ST correspondence [10, 11]. This observation raises the
issue of understanding the AJ conjecture from a purely quantum mechanical point of view. The AJ
conjecture can be explained, a priori , as a consequence of the quantization of the classical moduli
space described by theA-polynomial, as pointed out in [5] and briefly recalled in Section 2. However,
the precise details of this quantization procedure still need to be fully understood from a physical
perspective. We know that the quantization is non-trivial and cannot be obtained by simply pro-
moting the classical variables X,P to Weyl operators. In addition, the classical phase space is not
compact, which carries various problems concerning its appropriate quantization. From a quantum
mechanical angle, in such a situation, we would generically expect to have at most metastable states
with complex energies. We are, therefore, tempted to conjecture that the observed non-trivial quan-
tization of the A-polynomial is required to obtain a normalizable wave function with precisely zero
energy. We hope to address this question in the near future.
– 35 –
Acknowledgements
We want to thank Stavros Garoufalidis, Jie Gu, and Sergei Gukov for valuable discussions. We are
particularly grateful to Szabolcs Zakany for initial collaboration on this subject some years ago. This
research is supported in part by the ERC-SyG project “Recursive and Exact New Quantum Theory”
(ReNewQuantum), which received funding from the European Research Council (ERC) under the
European Union’s Horizon 2020 research and innovation program, grant agreement No. 810573.
A Computing the ϵ-expansions
For completeness, we include here the details of the computations performed in Section 3.2. We
observe that, as a consequence of Eqs. (3.3), (3.7), the coefficient functions ˆa±n(q) satisfy the relation
ˆa±n(q)q−σ±n =
X
k|n
kD±k

q
n
k

q−n
kσ±k
k−1X
j=0
q
n
kj, n ∈ Z>0, (A.1)
and we write the Z-polynomials D±k(q) explicitly as
D±k(q) =
degD±kX
ℓ=0
D±k,ℓ qℓ, k ∈ Z>0, (A.2)
where D±k,ℓ is an integer and deg D±k denotes the degree of the polynomial. Let us now take
q = e2πiP
Q, P,Q ∈ Z>0 coprime, (A.3)
while we introduce
qϵ = eiℏϵ, ℏϵ = 2πP
Q +ϵ, 0<ϵ ≪ 1, (A.4)
and consider the limit ϵ→ 0. In the case n =sQ, s∈ Z>0, we have the ϵ-expansions
D±k

q
sQ
k
ϵ

=

1 + iϵq ∂
∂q

D±k

q
sQ
k

+O(ϵ2), (A.5a)
k−1X
j=0
q
sQ
k (j−σ±k)
ϵ =

1 + iϵq ∂
∂q
k−1X
j=0
q
sQ
k (j−σ±k) +O(ϵ2), (A.5b)
and therefore also
ˆa±sQ(qϵ)q−σ±sQ
ϵ =

1 + iϵq ∂
∂q

ˆa±sQ(q)q−σ±sQ +O(ϵ2). (A.6)
We now observe that
1
qsQ
ϵ − 1
=− i
sQϵ− 1
2 +O(ϵ), (A.7)
and, combining Eqs. (A.6), (A.7), we finally obtain the NLO ϵ-expansion in Eq. (3.22a). On the
dual side, we consider
qD =q
Q2
P 2 = e2πiQ
P , q ϵ,D = e
4π2i
ℏϵ , (A.8)
– 36 –
and take again the limit ϵ→ 0. It follows that
qϵ,D =qD e−ϵQ2
P 2 +O(ϵ2). (A.9)
Similarly to the case above, when n =sP , s∈ Z>0, we have the ϵ-expansions
D±k

q
sP
k
ϵ,D

=

1− iϵQ2
P 2 qD
∂
∂qD

D±k

q
sP
k
D

+O(ϵ2), (A.10a)
k−1X
j=0
q
sP
k (j−σ±k)
ϵ,D =

1− iϵQ2
P 2 qD
∂
∂qD
k−1X
j=0
q
sP
k (j−σ±k)
D +O(ϵ2), (A.10b)
and therefore also
ˆa±sP (qϵ,D)q−σ±sP
ϵ,D =

1− iϵQ2
P 2 qD
∂
∂qD

ˆa±sP (qD)q−σ±sP
D +O(ϵ2). (A.11)
Finally, we note that
1
qsP
ϵ,D− 1 = iP
sQ2ϵ− 1
2 + i
2πsQ +O(ϵ), (A.12)
and, combining Eqs. (A.11), (A.12), we obtain the NLO ϵ-expansion in Eq. (3.22b).
