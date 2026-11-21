---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-013-91-hamiltonian-evolution
section_title: "Hamiltonian Evolution"
section_number: 9.1
pages: 30-32
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.647
latex_coverage_ratio: 0.96
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
In the live lectures at PiTP I ran out of time before I had a chance to discuss how complexity evolves when a system's dynamics is governed by a time independent \kl \ Hamiltonian. In that case the constraint of energy conservation restricts the motion of $U(t)$ to lie on a relatively low dimensional subspace of \Suk. Let's write $U(t)$ in the form,
\bea
U(t) \eq e^{\-iHt}  \cr \cr
\eq \sum_{i=1}^{2^K} |E_i\ra \la E_i| e^{-iE_i t}
\eea
For a given Hamiltonian the motion is restricted to a torus defined by the set of $2^K$ phases,
\be 
e^{i\theta_i} = e^{-iE_i t}.
\ee
In other words $U(t)$ moves on a $2^K$-dimensional torus embedded in the $(4^K-1)$-dimensional group \Suk. Although in itself a very large space the torus can only cover a tiny fraction of the full \Suk \ space. 

The first question is whether $U(t)$ fills the torus? Typically the answer is yes. If the energy levels are incommensurate, as will be the case if the system is chaotic, then the motion will be ergodic on the torus. The recurrence time for $U$ to return to the neighborhood of the identity  is the time for all the phases to get simultaneously close to $1$, and that takes time,
\be 
t_{recur}\sim \exp{2^K}.
\ee
This is in contrast to the recurrence time $\sim \exp{4^K}$  random (Brownian) circuits which fill the entire $4^K$-dimensional unitary group. Therefore it is not possible for $U(t)$ to visit any but an infinitesimal  fraction of the  maximally complex unitaries with $\CC\sim 4^K.$ 

On the other hand the unitaries of complexity $\leq 2^K$ comprise a set with volume comparable to the torus. It is therefore likely that for a Hamiltonian system the growth of complexity in figure \ref{2nd-law}  reaches $2^K$.

\bn

This raises an interesting question: In equation \ref{N=expC} I estimated the volume of the portion of \Suk \ with complexity $\CC$ and got,
$$e^{\CC \log{K}}.$$  That was the basis for the connection between complexity and the entropy of the auxiliary system, \ref{CsimS},
$$
S_{\CA} \approx \CC \log{K}.
$$

A similar question can be formulated for motion restricted to the torus: What is the volume of the torus occupied by unitaries of complexity $\CC?$ I expect that the answer is exponential,
$e^{ \alpha \CC}$,
 but with $\alpha$ parametrically smaller than $ \log {K}$. My guess is that $\alpha$ is independent of $K.$ In that case \ref{CsimS} would be replaced by,
 \be 
 S_{\CA} \approx \CC.
 \ee




\bn

This concludes lecture I. In the next lecture I will explain what   complexity and its second law has to do with black holes.










\rightline{}
\bigskip
\bigskip\bigskip\bigskip\bigskip
\bigskip








 









\part{Lecture II: Black Holes and the Second Law of Complexity}


\section{Preface}
When a star collapses a horizon forms and its area grows until it reaches its final value.  This is visible from outside the horizon and is known to be a manifestation of a statisitcal law, the second law of thermodynamics: Entropy increases until thermal equilibrium is reached.

There is another similar but less well-known phenomenon: the growth
of the spatial  volume behind the horizon of the black hole. 
At first sight this could  be another example of the increase of entropy, but more careful thought shows that this is not so. The growth of the interior continues long past the time when the black hole has come to thermal equilibrium. Something else---not entropy---increases. What that something else is should have been one of the deepest mysteries of black hole physics---if anyone had ever thought to ask about it.

Complexity is of course that something. Although complexity is most emphatically not ordinary entropy, the theory of complexity has a very strong thermodynamic flavor, as I began to explain in the last lecture. In this lecture we will see how another statistical law, ``The Second Law of Complexity" controls physics  behind the horizon in a manner very similar to the way the second law of thermodynamics controls the the dynamics of the horizon as seen from outside the black hole.
