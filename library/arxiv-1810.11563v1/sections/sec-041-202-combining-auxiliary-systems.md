---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-041-202-combining-auxiliary-systems
section_title: "Combining Auxiliary Systems"
section_number: 20.2
pages: 70-72
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.992
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
In thermodynamics it is important to understand how systems combine, as for example, when we combined two boxes of gas.  The question arises: What does it mean to combine two auxiliary systems? For example suppose $\CA$ is the auxiliary system corresponding to some quantum system $\CQ$. Is there a quantum system whose auxiliary is two copies of $\CA$? The first thing that comes to mind is to simply double the quantum system from $\CQ$ to two copies $\CQ \cup \CQ.$
However the number of coordinates describing the Auxiliary system for $\CQ \cup \CQ$ is not twice the number describing the original system $\CQ$. It is the square of that number.
Evidently doubling the quantum system is not doubling the auxiliary system.

In fact the right thing to do if we want to double the number of components in \ref{psi} is to add just one qubit. Let the computational basis for the additional qubit be $|0\ra, |1\ra.$
Any state can be written in the  form,
\be 
|\Psi\ra = |0\ra |\psi_0\ra + |1\ra |\psi_1\ra .
\ee
This obviously doubles the number of components in \ref{psi},
\be 
|\Psi\ra \to (\alpha_1, \alpha_2,......\alpha_{2^K}, \beta_1, \beta_2,......\beta_{2^K}),
\ee
Thus doubling the number of coordinates describing the auxiliary system.
If we think of the coefficients as coordinates of fictitious particles, then the number of particles is doubled by adding
the extra qubit!

With this in mind let us build an analogy with the two boxes of gas in the previous section. First consider a state,
\be 
|\Psi\ra = |0\ra|max_0\ra + |1\ra|max_1\ra
\label{Psi1}
\ee
where $|\max_{0,1}\ra$ are maximally complex states of $K$ qubits. Furthermore  assume that $|\max_{0}\ra$ and $|\max_{1}\ra$ have maximal relative complexity (see lecture I). This latter condition is the anolog of the two gasses in figure \ref{2box-uncor} being completely uncorrelated.

The maximum complexity of states $|\Psi \ra$ is $2^{K+1} = 2\times 2^K$. It is also true that if the relative complexity of $|\max_{0}\ra $ and $|\max_{1}\ra$ is maximal then the actual complexity of $|\Psi\ra$ is maximal, i.e., $2^{K+1}$. It follows that the uncomplexity of \ref{Psi1} is zero. If indeed uncomplexity is a necessary resource for some purpose, then the state \ref{Psi1} is useless for that purpose.


\bn

Next consider a similar state except that $|\max_1\ra$ and $|\max_2\ra$ are identical. In this case the single qubit is unentangled with the other $K$ qubits: it is said to be  ``clean." 
The $\alpha_i$ and $\beta_i$ are equal to each other and we have a situation which is analogous to  the one in figure \ref{2box-cor} where the two boxes were in identical microstates. 
Each box of gas in figure \ref{2box-cor} was in equilibrium, but the combined system was far from equilibrium. 

It is very easy to see that if $|max_1\ra = |max_2\ra$ then the complexity of the combined system of $(K+1)$ qubits is the same as the complexity of either component, i.e., $2^K$. 
Evidently, by adding a  single qubit to a maximally complex state we have doubled the maximal complexity but have not changed the actual complexity. Thus the addition of  a single clean qubit  restores the uncomplexity to the same value that one box of gas would have if it were in a simple unentangled state.
