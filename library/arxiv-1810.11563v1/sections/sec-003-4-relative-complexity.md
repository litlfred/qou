---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-003-4-relative-complexity
section_title: "Relative Complexity"
section_number: 4
pages: 7-9
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
The enormity of the space of states of quantum systems begs the question of how to
measure the distance between states. Are some states close to each other and others
enormously far? The usual metric in state space (by which I mean CP (N)) is the inner-
product metric. It’s also called the Fubini-Study (FS) metric. The FS distance between
two vectors|A⟩ and|B⟩ is,
dfs(A,B ) = arccos|⟨A|B⟩|. (4.8)
It varies from dfs = 0 when |A⟩ =|B⟩ to π/2 when |A⟩ and|B⟩ are orthogonal. The
space with the FS metric is “small” in the sense that the furthest distance between points
is π/2.
The FS metric has its purposes but it fails to capture something important. Imagine
an intricate piece of machinery with a microscopic switch—a control qubit—that can be
6
ﬂipped on or oﬀ. Compare the distance between these two states,
|on⟩ | oﬀ⟩
with the distance between two other states: a brand new machine, and a pile of rust,
|new⟩ | rust pile⟩
The FS distance between states |new⟩ and|rust pile⟩ is exactly the same as the
distance between|on⟩ and|oﬀ⟩, namely π/2. If the only criterion was the FS distance it
would be just as easy to:
1. Make a transition from |new⟩ to|rust pile⟩ as to make a transition from |on⟩ to
|oﬀ⟩.
2. Create a coherent superposition of|new⟩ and|rust pile⟩, or a coherent superposition
of|on⟩ and|oﬀ⟩.
3. Do a measurement that would be sensitive to the relative phases of such superposi-
tions in the two cases.
But of course this is not true. It is much easier make a superposition of |on⟩ and
|oﬀ⟩ (it just involves superposing two single-qubit states) than of |new⟩ and|rust pile⟩.
Evidently the FS metric fails to capture the diﬀerence between these two cases.
If it were equally possible to physically apply any operator to a system, then it would
be no harder to superpose the machine and the rust pile, than the on-oﬀ states. But in the
real world an operator that takes a machine to a rust pile is much more complex than an
operator that ﬂips a qubit. In practice, and maybe in principle, we carry out very complex
operations as sequences of simple operations. Once a set of “allowable” simple operations
has been identiﬁed, a new measure of distance between states becomes possible. It can be
deﬁned as:
The minimal number of simple operations needed to go from |A⟩ to|B⟩.
In (quantum)information theory the simple operations are called gates and new distance
measure is called relative complexity:
The relative complexity of |A⟩ and|B⟩ is the minimum number of gates required to go
from|A⟩ to|B⟩.
7
One might object that relative complexity is a somewhat subjective idea since it depends
on a choice of simple operations. But in a qubit context a simple operation is one that
involves a small number of qubits. For example we might allow all one and two-qubit gates
as simple operations. Relative complexity would then be fairly well deﬁned 1 But then a
skeptic may say: Yes, but what happens to your deﬁnition of complexity if I decide to
allow three qubit gates?
I expect (but cannot prove) that the answer is: Not much happens at least for large
complexity. There are two kinds of ambiguities to worry about—additive and multiplica-
tive. The additive ambiguities are associated with precision—how close do we have to get
to the target to declare success? If we are required to get within inner-product distance ϵ,
then there is an additive term in the complexity, logarithmic in ϵ. It is closely related to
the logarithmic ambiguity in 3.7.
There is also a multiplicative ambiguity when we go from allowing only one and two
qubit gates to allowing three qubit gates. That is because a three qubit gate can be ap-
proximated by some number of one and two qubit gates. That ambiguity can be accounted
for as long as the complexity is not too small.
A basic assumption is that there a set of deﬁnitions of quantum complexity that exhibit
a universal behavior up to additive and multiplicative ambiguities. The important rule is
that the allowable gates must be restricted to be k-local with k much smaller than the
number of qubits comprising the system. What k-local means is that the gate involves no
more than k qubits.
We’ll have more to say about relative complexity but let’s ﬁrst discuss the dual role of
unitary operators.
