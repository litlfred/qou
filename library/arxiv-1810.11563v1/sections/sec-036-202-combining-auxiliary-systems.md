---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes Leonard Susskind"
section_id: sec-036-202-combining-auxiliary-systems
section_title: "Combining Auxiliary Systems"
section_number: 20.2
pages: 70-72
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes Leonard Susskind — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to"
---
In thermodynamics it is important to understand how systems combine, as for example,
when we combined two boxes of gas. The question arises: What does it mean to combine
two auxiliary systems? For example suppose A is the auxiliary system corresponding to
some quantum systemQ. Is there a quantum system whose auxiliary is two copies of A?
The ﬁrst thing that comes to mind is to simply double the quantum system from Q to
69
two copiesQ∪Q . However the number of coordinates describing the Auxiliary system for
Q∪Q is not twice the number describing the original system Q. It is the square of that
number. Evidently doubling the quantum system is not doubling the auxiliary system.
In fact the right thing to do if we want to double the number of components in 20.84
is to add just one qubit. Let the computational basis for the additional qubit be |0⟩,|1⟩.
Any state can be written in the form,
|Ψ⟩ =|0⟩|ψ0⟩ +|1⟩|ψ1⟩. (20.86)
This obviously doubles the number of components in 20.84,
|Ψ⟩→ (α1,α 2,......α 2K,β 1,β 2,......β 2K), (20.87)
Thus doubling the number of coordinates describing the auxiliary system. If we think of
the coeﬃcients as coordinates of ﬁctitious particles, then the number of particles is doubled
by adding the extra qubit!
With this in mind let us build an analogy with the two boxes of gas in the previous
section. First consider a state,
|Ψ⟩ =|0⟩|max0⟩ +|1⟩|max1⟩ (20.88)
where| max0,1⟩ are maximally complex states of K qubits. Furthermore assume that
| max0⟩ and| max1⟩ have maximal relative complexity (see lecture I). This latter condition
is the anolog of the two gasses in ﬁgure 34 being completely uncorrelated.
The maximum complexity of states |Ψ⟩ is 2K+1 = 2 × 2K. It is also true that if
the relative complexity of | max0⟩ and| max1⟩ is maximal then the actual complexity of
|Ψ⟩ is maximal, i.e., 2 K+1. It follows that the uncomplexity of 20.88 is zero. If indeed
uncomplexity is a necessary resource for some purpose, then the state 20.88 is useless for
that purpose.
Next consider a similar state except that| max1⟩ and| max2⟩ are identical. In this case
the single qubit is unentangled with the other K qubits: it is said to be “clean.” The αi
and βi are equal to each other and we have a situation which is analogous to the one in
ﬁgure 35 where the two boxes were in identical microstates. Each box of gas in ﬁgure 35
was in equilibrium, but the combined system was far from equilibrium.
It is very easy to see that if |max1⟩ =|max2⟩ then the complexity of the combined
70
system of ( K + 1) qubits is the same as the complexity of either component, i.e., 2 K.
Evidently, by adding a single qubit to a maximally complex state we have doubled the
maximal complexity but have not changed the actual complexity. Thus the addition of a
single clean qubit restores the uncomplexity to the same value that one box of gas would
have if it were in a simple unentangled state.
