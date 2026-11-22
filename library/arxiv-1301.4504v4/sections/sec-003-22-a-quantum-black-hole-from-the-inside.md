---
doc_id: arxiv-1301.4504v4
doc_title: "Quantum Computation vs. Firewalls"
section_id: sec-003-22-a-quantum-black-hole-from-the-inside
section_title: "A Quantum Black Hole from the Inside"
section_number: 2.2
pages: 11-13
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.986
doc_brief: "Quantum Computation vs. Firewalls — In this paper we discuss quantum computational restrictions on the types of thought experiments recently used by Almheiri, Marolf, Polchinski, and Sully to argue"
---
We now consider Alice the infalling observer's point of view. As mentioned in the introduction, it may be possible to "embed" Alice's quantum mechanics into Charlie's via some sort of nontrivial operator mapping. We will discuss this eventually but for the moment will just treat Alice's theory as an independent construction. Here are the basic assumptions about it:

-   Although Alice eventually hits the singularity, we imagine that well before that she has an approximately quantum mechanical description of her experiences in terms of a quantum state on a time slice like the one shown in figure [1](#alice){reference-type="ref" reference="alice"}. We will not insist that the state be pure.

-   Alice's Hilbert space also has a roughly semiclassical factorization of the form $$\mathcal{H}_{inside}=\mathcal{H}_A\otimes\mathcal{H}_B\otimes\mathcal{H}_R\otimes\mathcal{H}_{H'}.$$ Here $\mathcal{H}_B$ and $\mathcal{H}_R$ are factors shared with Charlie, since they are outside the black hole horizon and are causally accessible to both Charlie and Alice. $\mathcal{H}_A$ are the field theory modes just inside the horizon, say with support over $GM<r<2GM-\epsilon$. $\mathcal{H}_{H'}$ are the remaining degrees of freedom having to do with Alice's horizon (which is distinct from the black hole horizon). $\mathcal{H}_H$ is absent; the region $2GM-\epsilon<r<2GM+\epsilon$ is passed through by Alice in an extremely short period of time and does not have any operational meaning to her. Of course, at times long before she falls in, the black hole horizon is indistinguishable from her horizon, and $\mathcal{H}_H$ is roughly part of $\mathcal{H}_{H'}$. We emphasize however that the details of this accounting don't matter.

-   Because $\mathcal{H}_B$ and $\mathcal{H}_R$ are shared with Charlie, we must have $\rho^{\{Alice\}}_{BR}=\rho^{\{Charlie\}}_{BR}$. This is sometimes called the overlap rule, and it is designed to prevent contradictions where Alice and Charlie disagree about the results of experiments they can communicate about.

<figure id="alice">
<div class="center">
<embed src="acpic.pdf" style="height:8cm" />
</div>
<figcaption>Alice’s quantum mechanics, compared to Charlie’s. The world inside her horizon is drawn in blue and the time slice she quantizes on is in red. For reference Charlie’s world is in yellow, and the overlap is green. We’ve chosen Charlie’s black slice to coincide closely with Alice’s near <span class="math inline"><em>B</em></span> and <span class="math inline"><em>R</em></span>.</figcaption>
</figure>

With these assumptions, one can now argue following AMPS that Alice must not see a smooth vacuum at the horizon. Recall that the modes in $\mathcal{H}_B$ and $\mathcal{H}_A$ are basically Rindler modes on two different sides of a Rindler horizon. In the Minkowski vacuum state such modes are close to maximally entangled: $$\label{smoothvac}
|vac\rangle\sim\sum_\omega e^{-\frac{\beta\omega}{2}}|\omega\rangle_A|\omega\rangle_B,$$ where $\beta\omega$ is the dimensionless Rindler energy; here it is just the ratio of Schwarzschild energy to the black hole temperature. This however is problematic from our discussion of Charlie. We argued that for an old black hole Charlie should see $B$ being close to maximally entangled with $R_B$, and by the third assumption about Alice this must also be true for her. But entanglement in quantum mechanics is monogamous: such entanglement prevents $B$ from also being entangled with $A$ as in [\[smoothvac\]](#smoothvac){reference-type="eqref" reference="smoothvac"}. One way to see this more precisely, again following AMPS, who themselves were motivated by a similar argument due to Mathur [@Mathur:2009hf], is to note that strong subadditivity [@lieb1973proof] requires $$\label{strongsub}
S_{ABR_B}+S_B\leq S_{AB}+S_{BR_B}.$$ By construction we have $S_{BR_B}=0$, which also implies (for example by the Araki-Lieb triangle inequality) that $S_{ABR_B}=S_A$. For [\[strongsub\]](#strongsub){reference-type="eqref" reference="strongsub"} to be consistent with the subadditivity inequality $S_A+S_B\geq S_{AB}$ we then must have $$I_{AB}\equiv S_A+S_B-S_{AB}=0.$$ $I_{AB}$ is called the *mutual information* between $A$ and $B$, and it is zero if and only if the density matrix $\rho_{AB}$ is actually a product $\rho_A\otimes \rho_B$. This is clearly inconsistent with $A$ and $B$ being close to the highly entangled state [\[smoothvac\]](#smoothvac){reference-type="eqref" reference="smoothvac"}. This concludes the AMPS argument; one possible interpretation is that the resolution of the contradiction is that there is a "firewall" of high energy quanta at the horizon of an old black hole which annihilates any infalling observer.
