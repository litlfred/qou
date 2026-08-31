---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-005-41-a-connection-between-young-lattice-and-gross
section_title: "A connection between Young lattice and Gross-Witten-Wadia model"
section_number: 4.1
pages: 13-15
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
---
The Gross-Witten-Wadia model is a well studied unitary matrix model in physics. The partition
function for this model is deﬁned over an ensemble of N× N unitary matrices with a real potential
TrU + TrU†, where the trace is taken over fundamental representations. The partition function of
GWW model is given by
ZGWW =
∫
[dU] e
N
λ (TrU+TrU†), λ ≥ 0. (4.4)
Gross and Witten [13] (and independently, Wadia [14]) studied this matrix model in the context
of lattice QCD and observed that the system undergoes a third order phase transition at λ = 2.
Diﬀerent phases of this model are characterised by the topology of distribution of eigenvalues of
the unitary matrix U on a unit circle. The strong coupling phase (λ> 2) corresponds to a gap-less
13
distribution of eigenvalues whereas weak coupling phase (λ <2) shows a ﬁnite gap in eigenvalue
distribution.
A close cousin of GWW model [40, 41] is given by
Zc =
∫
[dU] eaTrUTrU†
. (4.5)
The phase structure and eigenvalue distributions of this model are similar to those of GWW up
to a redeﬁnition of parameters : a⟨TrU⟩ = N/λ [17]. Expanding the exponential in (4.5) we get
Zc =
∫
[dU]
∞∑
k=0
ak
k! (TrU)k(TrU†)k. (4.6)
Using Frobenius formula for the characters of symmetric group we can write
(TrU)k =
∑
R
χR(1k)TrRU, and (Tr U†)k =
∑
R
χR(1k)TrRU† (4.7)
where the sum is over representations ofU(N) (or S U(N)) andχR(1k) is the character of conjugacy
class (1k) of symmetric group S k in representation R. Finally using the normalization condition
for the characters of unitary group
∫
[dU]TrRUTrR′U† =δRR′ (4.8)
we arrive at the ﬁnal expression for Zc written in terms of sum over representations of U(N)
[7]
Zc =
∞∑
k=0
ak
∑
R
(χR(1k))2
k! . (4.9)
It is well known that the character of the conjugacy class (1 k) of symmetric group S k in represen-
tation R is equal to the dimension of the representation [24]
χR(1k) = dimR. (4.10)
Representations of U(N) can be expressed in terms of Young diagrams. Since χR(1k) is non-zero
only when total number of boxes in the Young diagram is k we have
Zc =
∞∑
k=0
ak
∑
λk
(dimλk)2
k! δ(k−|λk|). (4.11)
Thus we see that the partition function for (cousin of) GWW model is same as that of a Young
lattice with the coupling constant a playing the role of fugacity. The rank of the gauge group
S U(N) in GWW model plays the role of the cut-oﬀ N in (4.3).
14
