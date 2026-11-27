---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-021-a2-3--qutrit-code-and-4-qutrit-state
section_title: "A.2 3 -qutrit code and 4-qutrit state"
section_number: null
pages: 45-46
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
One of the simplest examples of perfect tensors is given by the three qutrit code. This
stabilizer code allows encoding one logical qutrit onto three physical qutrits in a way
that it may be recovered even after erasure of any single physical qutrit. The reason
for providing this additional example at this point is that we believe that this family of
perfect tensors may naturally be suited to generalizations leading to a continuum type
limit.
The code states for this code can be given as follows.
√
3|˜0⟩ =|000⟩ +|111⟩ +|222⟩
√
3|˜1⟩ =|012⟩ +|120⟩ +|201⟩
√
3|˜2⟩ =|021⟩ +|102⟩ +|210⟩.
Correspondingly, the perfect state can be given explicitly as
3|[[4, 0, 3]]3⟩ =|0000⟩ +|1110⟩ +|2220⟩
+|0121⟩ +|1201⟩ +|2011⟩
+|0212⟩ +|1022⟩ +|2102⟩.
The [[4, 0, 3]]3 state is determined by the following stabilizer group
S =⟨ZZZI,ZZ −1IZ,XXXI,XX −1IX⟩, (A.9)
– 43 –
where we have omitted the three tensor product operator ⊗ between the qutrit Pauli
operators
I =


1 0 0
0 1 0
0 0 1

 X =


0 1 0
0 0 1
1 0 0

 Z =


1 0 0
0 ω 0
0 0 ω2

 ω =e2iπ/3. (A.10)
From this presentation of the stabilizer group, it becomes clear that this perfect state
corresponds to a self dual CSS code. 8 This separation of X and Z type operators,
and treating them on similar footing may potentially allow generalization to continuum
variable where position and momentum conjugate variables play a similar role.
Like any other maximally entangled stabilizer state, given a bipartition, the [[4, 0, 3]]3
perfect state may be interpreted as a unitary gate belonging to the generalized Cliﬀord
group. A second reason for presenting this code is that we can provide a simple and
explicit presentation of the corresponding Cliﬀord circuit. In the case of the [[4 , 0, 3]]3,
the corresponding Cliﬀord is composed to two controlled adder gates which are run in
opposite directions one after the other.
U[[4,0,3]]3 =|x1,x 2⟩→| 2x1 +x2,x 1 +x2⟩ =
 (A.11)
