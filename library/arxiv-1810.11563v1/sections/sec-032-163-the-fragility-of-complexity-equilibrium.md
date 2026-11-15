---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-032-163-the-fragility-of-complexity-equilibrium
section_title: "The Fragility of Complexity Equilibrium"
section_number: 16.3
pages: 63-64
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.982
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
Let's  take the default position: If there is no reason to believe that  firewalls don't occur when the complexity stops increasing, then they probably do occur.
 How stable would such a firewall be? The naive answer is that equilibrium is  stable and not likely to be significantly disturbed by butterflies. 
 That is true for ordinary thermal equilibrium, say of a gas of $N$ classical molecules. 
 
 Thermal equilibrium is a state of maximum entropy in which the entropy is proportional to the number of molecules,
 \be 
 S_{max}\sim N.
 \ee
Now lets perturb the state by adding a single molecule. The result will be that the maximum entropy will be increased by one bit,
\be 
S_{max} \to N+1.
\ee

Although initially out of equilibrium, the new molecule will  come to equilibrium with the new entropy being $\sim N+1.$ This will typically take a very short time.

Let's compare this with what happens if we add a single qubit to a system of $K$ qubits in complexity equilibrium. The maximum complexity of the original $K$ qubit system is $2^K.$ Adding a qubit brings the maximum complexity to $2^{(K+1)}= 2\times 2^K$. This means that the new state is far out of complexity equilibrium; the complexity can increase for an additional amount $\sim 2^K.$
  
Now let's return to the black hole in complexity equilibrium at maximal complexity. If we drop in a single thermal photon the entropy increases by one bit, but the maximal complexity doubles.
The system has been kicked far out of complexity equilibrium by the addition of a thermal photon.
To return to equilibrium a minimum of $2^K$ gates must act, and this will take an exponential time. By dropping in the thermal photon we buy an additional exponential time during which the complexity increases. Complexity equilibrium is evidently very fragile. 


There is another way to think about this. If indeed a black hole in complexity equilibrium has a firewall at its horizon, throwing in a thermal photon will   have the same effect as in section \ref{Sec: fragile FW}. The photon will kick the shock wave  and push it into the singularity. The horizon will be clear and the wormhole will be free to grow again for another exponential time.

\bn
