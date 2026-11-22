---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-029-31-metropolis-algorithm
section_title: "Metropolis Algorithm"
section_number: 3.1
pages: 61-64
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.994
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#MarkovChian label="MarkovChian"}

In general, for a normalized probability distribution $\pi(s)$ such that $\sum_s \pi(s)=1$, $\langle F \rangle$ the expectation value of function $F(s)$ is, $$\langle F \rangle = \sum_s F(s) \pi(s),
\label{Fave}$$ where the letter $s$ means a set of variables which can describe a state. In the Monte Carlo method, if we can sample $n$ states which effectively explore the state space of $\pi(s)$ and are distributed according to $\pi(s)$, denoting those states as $\{s_0,s_1,s_2...,s_n\} \in s$, then the expectation value $\langle F \rangle$ can be calculated by, $$\langle F \rangle = \frac{\sum_{i=0}^n F(s_i) }{n} .
\label{FaveMC}$$

So it is clear that we need to make a process which can continuously generate a series of states {$s_0,s_1,s_2,s_3$\...} such that they distributed according to a target distribution $\pi(s)$. In order to do so, we need a transition probability $\mathcal{P}(s\rightarrow s')$ which is the probability for state $s$ to transit to $s'$. Once this process reaches its equilibrium status, it must satisfy, $$\sum_s \pi(s) \mathcal{P}(s\rightarrow s')=\pi(s').
\label{equilibriumeq}$$

We can require the number of states that make transition from any $s$ to $s'$ equals that transit from $s'$ back to $s$, $$\pi(s) \mathcal{P}(s\rightarrow s')=\pi(s') \mathcal{P}(s'\rightarrow s).
\label{detailbalance}$$ Eq.([\[detailbalance\]](#detailbalance){reference-type="ref" reference="detailbalance"}) is the detailed balance condition ([@Ceperley95a]). Note that $\sum_{s'} \mathcal{P}(s\rightarrow s')=\sum_{s} \mathcal{P}(s'\rightarrow s)=1$, so once we reach the detailed balance, Eq.([\[equilibriumeq\]](#equilibriumeq){reference-type="ref" reference="equilibriumeq"}) the equilibrium status will automatically become valid and therefore the states we generated will indeed be distributed according to $\pi(s)$.

The transition probability can be written as, $$\mathcal{P}(s\rightarrow s')=T(s\rightarrow s') A(s\rightarrow s'),
\label{PeqTA}$$ where $T(s\rightarrow s')$ is a proposed transition probability and $A(s\rightarrow s')$ is the acceptance probability which will be used to judge if the proposed transition is accepted or not. With Eq.([\[PeqTA\]](#PeqTA){reference-type="ref" reference="PeqTA"}), the detailed balance equation Eq.([\[detailbalance\]](#detailbalance){reference-type="ref" reference="detailbalance"}) can be further written as, $$\frac{A(s\rightarrow s')}{A(s'\rightarrow s)}=\frac{\pi(s')T(s'\rightarrow s)}{\pi(s) T(s\rightarrow s') } .
\label{detailbalanceAoA}$$

A common choice of the acceptance probability $A(s\rightarrow s')$ which can satisfy Eq.([\[detailbalanceAoA\]](#detailbalanceAoA){reference-type="ref" reference="detailbalanceAoA"}) and thus the detailed balance condition is ([@Kalos1986a]), $$A(s\rightarrow s')=
\min \left[  1, \frac{\pi(s')T(s'\rightarrow s)}{\pi(s) T(s\rightarrow s')} \right] .
\label{Accptequation}$$

As we can see, the normalization factors in $\pi(s)$ and $\pi(s')$ and that in $T(s \rightarrow s')$ and $T(s'\rightarrow s)$ will be canceled out in Eqs.([\[detailbalanceAoA\]](#detailbalanceAoA){reference-type="ref" reference="detailbalanceAoA"},[\[Accptequation\]](#Accptequation){reference-type="ref" reference="Accptequation"}) so those factors are irrelevant in calculating $A$. In order to make the value of $A(s\rightarrow s')$ larger, we can try to make $T(s'\rightarrow s)$ similar with $\pi(s)$, and $T(s'\rightarrow s)$ similar with $\pi(s')$, such that the numerator and denominator in Eq.([\[Accptequation\]](#Accptequation){reference-type="ref" reference="Accptequation"}) can largely cancel. That will usually make the calculation efficient. In the ideal case, if we can make $T(s'\rightarrow s)=\pi(s)$ and $T(s'\rightarrow s')=\pi(s')$, then $A(s\rightarrow s')=1$ so we just need to always accept the new proposed states, but this is normally not possible, and if possible the Metropolis method would be unnecessary.

The basic procedure for the Monte Carlo method is described as follows.

Step 1

:   For the current state $s$, propose a new state $s'$ according to the proposed transition probability $T(s\rightarrow s')$.

Step 2

:   For the proposed new state $s'$, use Eq.([\[Accptequation\]](#Accptequation){reference-type="ref" reference="Accptequation"}) to calculate the acceptance rate $A(s\rightarrow s')$.

Step 3

:   Generate a uniform random number $a$ which ranges from 0 to 1. If $a \leq A(s\rightarrow s')$, the new state $s'$ is accepted, so set the accepted state $s'$ as the current state $s$, namely $s = s'$, and keep $s'$ as a sample, then go to step 1 and continue. Else, the new state $s'$ is rejected which means the state $s$ is accepted and kept as the sample, so set the accepted state $s$ as our current state $s$, then go to step 1 and continue.

After looping over the procedure for enough times, all those 'current state' $s$ in step 1 will eventually be distributed according to the desired distribution $\pi(s)$.

Note that the choice of $T$ and therefore $A$ are not unique. In order to make the algorithm more robust, we usually include different types of moves with correspondingly proposed transition probability $T$, and acceptance rate $A$, and this will still lead to the target distribution $\pi(s)$, as long as the detailed balance condition Eq.([\[detailbalanceAoA\]](#detailbalanceAoA){reference-type="ref" reference="detailbalanceAoA"}) holds for each type of move. Any such choice that has transitions between any two allowed states by a series of moves and has some rejections will converge to samples of $\pi(s)$. Also, the choice of $T$ determines how efficient the Monte Carlo procedure is. A poorly chosen $T$ can make the code run for a very long time but still not able to form $\pi(s)$. So $T$ is crucial in the algorithm, we will discuss our choice of $T$ in the next section.
