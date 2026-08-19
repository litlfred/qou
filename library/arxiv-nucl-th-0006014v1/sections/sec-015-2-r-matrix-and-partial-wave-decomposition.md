---
doc_id: arxiv-nucl-th-0006014v1
doc_title: "The high-precision, charge-dependent Bonn nucleon-nucle on potential (CD-Bonn) R. Machleidt ∗"
section_id: sec-015-2-r-matrix-and-partial-wave-decomposition
section_title: "R-matrix and partial wave decomposition"
section_number: 2
pages: 18-19
source_pdf: 0006014v1.pdf
source_sha256: 208c7a6aaf628b30
doc_brief: "The high-precision, charge-dependent Bonn nucleon-nucle on potential (CD-Bonn) R. Machleidt ∗ — 35 sections: Scattering equation . . . . . . . ; R-matrix and partial wave decompos; Phase shifts . . ."
---
In solving the scattering equation, it is more convenient to deal with real quantities. We
shall therefore introduce the real R-matrix (better known as ‘ K-matrix’) deﬁned by
T =R −iπRδ(E −H0)T (A19)
The equation for the real R-matrix corresponding to the complex T -matrix of Eq. (A18) is
R(q′, q) = V (q′, q) + P
∫
d3kV (q′, k) M
q2 − k2 R(k, q) (A20)
where P denotes the principal value.
Now, we need to also include the spin of the nucleons. Relativ istic scattering of particles
with spin is treated most conveniently in the helicity forma lism [99]. Therefore, we will use
a helicity state basis in our further formal developments. O ur presentation will be relatively
brief; a more detailed derivation is given in Appendix C of Re f. [1] which is based upon
Refs. [99,100].
The helicity λi of particle i (with i = 1 or 2) is the eigenvalue of the helicity operator
1
2σ i · pi/|pi| which is ± 1
2 .
Using helicity states, the R-matrix equation reads, after partial wave decomposition,
⟨λ′
1λ′
2|RJ(q′,q )|λ1λ2⟩= ⟨λ′
1λ′
2|V J (q′,q )|λ1λ2⟩
+
∑
h1,h 2
P
∫ ∞
0
dkk 2 M
q2 −k2 ⟨λ′
1λ′
2|V J (q′,k )|h1h2⟩
× ⟨h1h2|RJ(k,q )|λ1λ2⟩ (A21)
where J denotes the total angular momentum of the two nucleons. Here we are changing
our notation for momenta: in the above equation and througho ut the rest of Appendix
A, momenta denoted by non-bold letters are the magnitude of t hree-momenta, e. g. q ≡
|q|, k ≡ | k|, etc.; h1 and h2 are the helicities in intermediate states for nucleon 1 and 2 ,
18
respectively. Equation (A21) is a system of coupled integra l equations which needs to be
solved to obtain the desired matrix elements of RJ .
Ignoring anti-particles, there are 4 × 4 = 16 helicity amplitudes for RJ . However, time-
reversal invariance, parity conservation, and the fact tha t we are dealing with two identical
fermions imply that only six amplitudes are independent. Fo r these six amplitudes, we
choose the following set:
RJ
