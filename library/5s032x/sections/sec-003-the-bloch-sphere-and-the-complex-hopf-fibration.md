---
doc_id: 5s032x
doc_title: "The standard model symmetry and qubit entanglement"
section_id: sec-003-the-bloch-sphere-and-the-complex-hopf-fibration
section_title: "The Bloch Sphere and the Complex Hopf Fibration"
section_number: null
pages: 6-7
source_pdf: 5S032X.pdf
source_sha256: 17761383781f7bdc
doc_brief: "The standard model symmetry and qubit entanglement — quantum description."
---
Above, we have already introduced the Bloch sphere representation of single qubits. The normalization condition
|c0|2 +|c1|2 = 1 implies that the Hilbert space of a single qubit is the 3-sphere S3. However, quantum states are
properly represented by rays in Hilbert space, and hence, only unique up to an overall U(1) phase factor exp (iϕ).
Taking account of this, each qubit can be represented in the projective Hilbert space S2 =S3/U(1) =S3/S1. Hence,
there must be a map taking elements of S3 to S2. This is the complex Hopf map, and can be explicitly written as
the composition of a map h1 taking points of S3 defined by complex coordinates ( c0,c 1) to points on the extended
complex plane C∪{∞} ,
hc
1 : S3 −→ C∪{∞}
(c0,c 1) −→ c0c−1
1
, (12)
and a map h2 corresponding to an inverse stereographic projection from C to S2
hc
2 : C∪{∞} −→ S2
c0c−1
1 −→ (x1,x 2,x 3), (13)
such thatx2
1+x2
2+x2
3 = 1. As discussed above, this is of course just the map taking a quantum state|ψ⟩ =c0|0⟩+c1|1⟩
to its Bloch vector representation, yielding for each coordinate [52]
xi =⟨σi⟩ψ
= (c∗
0,c∗
1)σi

c0
c1

,
7
where it is obvious that each xi is defined only up to an U(1) ambiguity.
This provides a realization of the single-qubit Hilbert space in terms of the complex Hopf fibration
S3 S1
−→S2, (14)
which is the simplest example of a nontrivial fibre bundle, meaning that S3̸=S2×S1. Physically, this nontriviality
implies the impossibility of assigning a consistent phase to every point on the Bloch sphere.
It is at this point that the necessity of the division algebra property enters into the picture: without it, there is
no way to define c0c−1
1 , and thus, to formulate the Hopf map unambiguously. This explains why there are precisely
four such constructions, corresponding to the four division algebras R, C, H and O. Consequently, the construction
presented here has a natural endpoint at the octonionic level.
