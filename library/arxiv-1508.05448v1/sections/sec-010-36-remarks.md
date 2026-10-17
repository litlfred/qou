---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-010-36-remarks
section_title: "Remarks"
section_number: 3.6
pages: 55-59
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.981
---
By generalizing this method introduced by Chatterjee and Ledoux, we are able to show concentration of measure of the empirical spectral distribution not only for operator compressions via $SO(n)$ but also for operators that are \"compressed\" by conjugation with a Gaussian matrix. It is likely that this method could be applied to a much wider range of Markov chains, given that the chain does not change too many entries at once, has an appropriate invariant distribution, and for which the spectral gap is known. It is possible that better bounds for the Gaussian compression could be obtained by adapting the method to use the \"second\" spectral gap or the exponential decay rate in relative entropy found in [@BLV].

It is worth noting that Talagrand's isoperimetric inequality [@Talagrand] gives concentration of measure for the length of the longest increasing subsequence for random permutations, but it cannot be used in the context of this ASEP random walk, as it requires independence. Using Chatterjee and Ledoux's method, independence is not needed. We only need a spectral gap bound for the Markov chain.\
\

# Mixed Matrix Moments and Eigenvector Overlap Functions of the Ginibre Ensemble

The purpose of this section is to make some observations about the mixed matrix moments for non-Hermitian random matrices. The results in this chapter can be found in [@MWSS]. Let $\operatorname{Mat}_n(\mathbb{C})$ denote the set of $n\times n$ matrices with complex entries. We use this notation here because we will use $M_n$ for something else later.

The model we will focus on most is the complex Ginibre ensemble, given by $$A_n \in \operatorname{Mat}_n(\mathbb{C})\, ,\quad A_n = (a_n(j,k))_{j,k=1}^{n}\, ,\quad
a_n(j,k)\, =\, \frac{X(j,k)+iY(j,k)}{\sqrt{2n}}\, ,$$ where $(X(j,k))_{j,k=1}^{\infty}$, $(Y(j,k))_{j,k=1}^{\infty}$ are IID, $\mathcal{N}(0,1)$ real random variables.

Much of what we will say has already been explored by Chalker and Mehlig in a pair of papers [@CM; @MC], in particular, in their definition of expected overlap functions. There are other models of interest which were explored by Fyodorov and coauthors [@FY1; @FY2], for which one can obtain more explicit formulas for the expected overlap functions. Our main emphasis will be to relate Chalker and Mehlig's formulas for the overlap functions of the complex Ginibre ensemble to the mixed matrix moments.

Our motivation in considering this problem is the following. There is a rough analogy between mean-field spin glasses and random matrices, as far as the mathematical methods are concerned. We indicate this in the table in Figure [1.1](#fig:1){reference-type="ref" reference="fig:1"}. We will give more details and references in a later discussion, but we would like to point out some of the analogies now. This analogy leads to a method to calculate moments, but there is still the question about how to relate the moments to the spectral information for the matrix.  

<figure id="fig:1">
<div class="center">

</div>
<figcaption>Some analogous elements in random matrix and spin glass theory. (Proofs may differ considerably.) <span id="fig:1" label="fig:1"></span></figcaption>
</figure>

Although the main subject of this subject is random matrices, we will give a very brief introduction to spin glasses, just to motivate our analogy. Spin glasses are physical objects. We will not say much about the physics behind them, as the subject of this paper is mathematics. However, we will give a quote from Daniel Mattis's book [@Mattis] in his discussion of dilute magnetic alloys. He says :\
\
*\"If the impurity atom does possess a magnetic moment this polarizes the conduction electrons in its vicinity by means of the exchange interaction and thereby influences the spin orientation of a second magnetic atom at some distance. Owing to quantum oscillations in the conduction electrons' spin polarization the resulting effective interaction between two magnetic impurities at some distance apart can be ferromagnetic (tending to align their spins) or antiferromagnetic (tending to align them in opposite directions). Thus a given magnetic impurity is subject to a variety of ferromagnetic and antiferromagnetic interactions with the various neighboring impurities. What is the state of lowest energy of such a system? This is the topic of an active field of studies entitled "spin glasses," the magnetic analog to an amorphous solid.\"* [@Mattis] (p. 48)\
\
Since this is a mathematics paper, we will consider a spin glass as a probabilistic model. We can consider a system $$\Sigma_N=\{-1,1\}^N$$ for a large integer $n$. We call an element $\sigma\in \Sigma_n$ a configuration. The components of $\sigma$ are called spins (and can each take the value either $\pm 1$). The energy of the system in a configuration $\sigma$ is called the Hamiltonian, which is usually denoted $H_N(\sigma)$. Given a parameter $\beta$ (the inverse temperature), we can define the Gibbs measure by $$G_N(\{\sigma\})=\frac{\exp(-\beta H_N(\sigma))}{Z_N}$$ where $Z_N$ is a normalizing factor, called the partition function. The Gibbs measure is a probability measure which represents the probability of observing the configuration $\sigma$ after the system has reached equilibrium in a heat bath at temperature $1/\beta$. $H_N(\sigma)$ relates to the interactions between the spins. In the models that are often considered, the $H_N(\sigma)$ are random variables. For a given $H_N(\sigma)$, the main problem is to understand the Gibbs measure. See [@Talagrandbook] for a more in depth discussion of the probabilistic aspect of spin glasses.

We will depart from our discussion of spin glasses now, to begin the discussion of random matrices. The analogies between the two topics will be discussed more in depth later.

We will start by briefly recalling the formula for the mixed matrix moments of the complex Ginibre ensemble, and we will emphasize the relation to spin glass techniques. This formula is already known and we will give references.

In later sections, we will describe the relationship between the mixed matrix moments and the expected overlap functions of Chalker and Mehlig. This leads to some new problems.
