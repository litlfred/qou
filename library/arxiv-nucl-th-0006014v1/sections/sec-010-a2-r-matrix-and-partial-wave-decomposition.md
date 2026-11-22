---
doc_id: arxiv-nucl-th-0006014v1
doc_title: "The high-precision, charge-dependent Bonn nucleon-nucleon potential (CD-Bonn)"
section_id: sec-010-a2-r-matrix-and-partial-wave-decomposition
section_title: "R-matrix and partial wave decomposition"
section_number: A.2
pages: 18-21
source_pdf: 0006014v1.pdf
source_sha256: 208c7a6aaf628b30
toc_source: inferred
doc_brief: "The high-precision, charge-dependent Bonn nucleon-nucleon potential (CD-Bonn) — 56 sections: Front matter; Introduction; The model"
---
In solving the scattering equation, it is more convenient to deal with real quantities. We
shall therefore introduce the real R-matrix (better known as ‘K-matrix’) deﬁned by
T = R −iπRδ(E −H0)T
(A19)
The equation for the real R-matrix corresponding to the complex T-matrix of Eq. (A18) is
R(q′, q) = V (q′, q) + P
Z
d3k V (q′, k)
M
q2 −k2 R(k, q)
(A20)
where P denotes the principal value.
Now, we need to also include the spin of the nucleons. Relativistic scattering of particles
with spin is treated most conveniently in the helicity formalism [99]. Therefore, we will use
a helicity state basis in our further formal developments. Our presentation will be relatively
brief; a more detailed derivation is given in Appendix C of Ref. [1] which is based upon
Refs. [99,100].
The helicity λi of particle i (with i = 1 or 2) is the eigenvalue of the helicity operator
1
2σi · pi/|pi| which is ±1
2.
Using helicity states, the R-matrix equation reads, after partial wave decomposition,
⟨λ′
1λ′
2|RJ(q′, q)|λ1λ2⟩= ⟨λ′
1λ′
2|V J(q′, q)|λ1λ2⟩
+
X
h1,h2
P
Z ∞
0
dk k2
M
q2 −k2⟨λ′
1λ′
2|V J(q′, k)|h1h2⟩
× ⟨h1h2|RJ(k, q)|λ1λ2⟩
(A21)
where J denotes the total angular momentum of the two nucleons. Here we are changing
our notation for momenta: in the above equation and throughout the rest of Appendix
A, momenta denoted by non-bold letters are the magnitude of three-momenta, e. g. q ≡
|q|, k ≡|k|, etc.; h1 and h2 are the helicities in intermediate states for nucleon 1 and 2,
respectively. Equation (A21) is a system of coupled integral equations which needs to be
solved to obtain the desired matrix elements of RJ.
Ignoring anti-particles, there are 4 × 4 = 16 helicity amplitudes for RJ. However, time-
reversal invariance, parity conservation, and the fact that we are dealing with two identical
fermions imply that only six amplitudes are independent.
For these six amplitudes, we
choose the following set:
RJ
1(q′, q) ≡⟨+ + |RJ(q′, q)| + +⟩
RJ
2(q′, q) ≡⟨+ + |RJ(q′, q)| −−⟩
RJ
3(q′, q) ≡⟨+ −|RJ(q′, q)| + −⟩
RJ
4(q′, q) ≡⟨+ −|RJ(q′, q)| −+⟩
(A22)
RJ
5(q′, q) ≡⟨+ + |RJ(q′, q)| + −⟩
RJ
6(q′, q) ≡⟨+ −|RJ(q′, q)| + +⟩
where ± stands for ±1
2. Notice that
RJ
5(q′, q) = RJ
6(q, q′).
(A23)
We have now six coupled equations. To partially decouple this system, it is usefull to
introduce the following linear combinations of helicity amplitudes:
0RJ ≡RJ
1 −RJ
2
1RJ ≡RJ
3 −RJ
4
12RJ ≡RJ
1 + RJ
2
(A24)
34RJ ≡RJ
3 + RJ
4
55RJ ≡2RJ
5
66RJ ≡2RJ
6
We also introduce corresponding deﬁnitions for V J.
Using these deﬁnitions, Eq. (A21)
decouples into the following three sub-systems of integral equations:
Spin singlet
0RJ(q′, q) = 0V J(q′, q) + P
Z ∞
0
dk k2
M
q2 −k2
0V J(q′, k) 0RJ(k, q) .
(A25)
Uncoupled spin triplet
1RJ(q′, q) = 1V J(q′, q) + P
Z ∞
0
dk k2
M
q2 −k2
1V J(q′, k) 1RJ(k, q) .
(A26)
Coupled triplet states
12RJ(q′, q) = 12V J(q′, q) + P
Z ∞
0
dk k2
M
q2 −k2[ 12V J(q′, k) 12RJ(k, q)
+ 55V J(q′, k) 66RJ(k, q)]
34RJ(q′, q) = 34V J(q′, q) + P
Z ∞
0
dk k2
M
q2 −k2[ 34V J(q′, k) 34RJ(k, q)
+ 66V J(q′, k) 55RJ(k, q)]
55RJ(q′, q) = 55V J(q′, q) + P
Z ∞
0
dk k2
M
q2 −k2[ 12V J(q′, k) 55RJ(k, q)
+ 55V J(q′, k) 34RJ(k, q)]
66RJ(q′, q) = 66V J(q′, q) + P
Z ∞
0
dk k2
M
q2 −k2[ 34V J(q′, k) 66RJ(k, q)
+ 66V J(q′, k) 12RJ(k, q)] .
(A27)
More common in nuclear physics is the representation of two-nucleon states in terms of
an |LSJM⟩basis, where S denotes the total spin, L the total orbital angular momentum,
and J the total angular momentum with projection M. In this basis, we will denote the R
matrix elements by RJS
L′,L ≡⟨L′SJM|R|LSJM⟩. These are obtained from the helicity state
matrix elements by the following unitary transformation:
Spin singlet
RJ0
J,J = 0RJ .
(A28)
Uncoupled spin triplet
RJ1
J,J = 1RJ .
(A29)
Coupled triplet states
RJ1
J−1,J−1 =
1
2J + 1

J 12RJ + (J + 1) 34RJ +
q
J(J + 1)( 55RJ + 66RJ)

RJ1
J+1,J+1 =
1
2J + 1

(J + 1) 12RJ + J 34RJ −
q
J(J + 1)( 55RJ + 66RJ)

RJ1
J−1,J+1 =
1
2J + 1
q
J(J + 1)( 12RJ −34RJ) −J 55RJ + (J + 1) 66RJ)

RJ1
J+1,J−1 =
1
2J + 1
q
J(J + 1)( 12RJ −34RJ) + (J + 1) 55RJ −J 66RJ)

.
(A30)
Similar notation and transformations apply to V .
One way to proceed is to solve the system of equations (A27) and then apply the trans-
formation (A30). Alternatively, one may apply the transformation (A30) directly in (A27)
to obtain the system of four coupled integral equations in LSJ representation,
RJ1
++(q′, q) = V J1
++(q′, q) + P
Z ∞
0
dk k2
M
q2 −k2[ V J1
++(q′, k) RJ1
++(k, q)
+ V J1
+−(q′, k) RJ1
−+(k, q)]
RJ1
−−(q′, q) = V J1
−−(q′, q) + P
Z ∞
0
dk k2
M
q2 −k2[ V J1
−−(q′, k) RJ1
−−(k, q)
+ V J1
−+(q′, k) RJ1
+−(k, q)]
RJ1
+−(q′, q) = V J1
+−(q′, q) + P
Z ∞
0
dk k2
M
q2 −k2[ V J1
++(q′, k) RJ1
+−(k, q)
+ V J1
+−(q′, k) RJ1
−−(k, q)]
RJ1
−+(q′, q) = V J1
−+(q′, q) + P
Z ∞
0
dk k2
M
q2 −k2[ V J1
−−(q′, k) RJ1
−+(k, q)
+ V J1
−+(q′, k) RJ1
++(k, q)]
(A31)
where we used the abbreviations RJ1
++
≡
RJ1
J+1,J+1,
RJ1
−−
≡
RJ1
J−1,J−1,
RJ1
+−
≡
RJ1
J+1,J−1, RJ1
−+ ≡RJ1
J−1,J+1; and similarly for V .
The above integral equations can be solved numerically by the matrix inversion
method [101]. The method is explained in detail in Ref [102] where also a computer code is
provided.
Each two-nucleon state carries a well-deﬁned total isospin T (which is either 0 or 1) that
is ﬁxed by
(−1)L+S+T = −1 .
(A32)
