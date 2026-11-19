A Turing machine computation of $N$ gates encodes as a braid $\beta$ on $n$ strands with $c = 3N$ crossings. Closing the braid yields a link $L = \hat{\beta}$. The Skein polynomial $P_L(q)$ forms the output of the computation.

**The Skein decomposition is the discrete path integral.**
At each crossing of $L$, the Skein relation resolves the link into three branches:
$$
  q L_+ - q^{-1} L_- = s L_0
$$
where $s = q^{1/2} - q^{-1/2}$. Each resolution replaces one crossing with a positive ($L_+$), negative ($L_-$), or smoothed ($L_0$) outcome. Iterating over all $c$ crossings constructs a resolution tree with $3^c$ leaves, each representing one discrete history. 

This constitutes the path integral at Planck resolution. Each resolution is exactly one Planck step. Each tree path is one discrete history. The Skein polynomial sums over all $3^c$ histories, weighted by their crossing signs, yielding the partition function of the computation.

| Path integral | Skein decomposition |
| ------------- | ------------------- |
| History | Resolution path through the tree |
| Action weight $e^{iS/\hbar}$ | Skein weight $q^{\pm 1}$ or $s$ per crossing |
| Partition function $Z$ | Skein polynomial $P_L(q) = \sum_{\text{paths}}(\text{weights})$ |
| Path integral measure | Markov trace $\mathrm{tr}_M$ |
| Planck time step | One crossing resolution |

**Information before and after the trace.**
Before the Markov trace, the braid word $\beta \in H_n(q)$ retains the full gate address fine structure: $O(N \log n)$ bits of exact generator wiring.

After the trace, the Skein polynomial $P_L(q)$ compresses from $3^c$ paths to $O(c)$ factors via $P_L(q) = \prod_{i=0}^{n-2} \hat{V}_i(q)$. This is the selective erasure of internal wiring. The discrete history the universe followed is irreversibly lost. What survives is the topological invariant: the computation's output. The Markov trace acts as observation, collapsing $3^c$ quantum paths into one polynomial.

**The backward flow.**
Starting from the output state $E \in \Gamma(M, \mathcal{S})$, each crossing resolves backward through the jet tower. After $3N$ resolutions, the braid unwinds completely to the Big Bang initial conditions $\mathcal{S}_0$. By descent, all branches flow back to $\mathcal{S}_0$. The initial conditions are the program; the braid is the computation; the Skein polynomial is the output.

**Quantum computations.**
A section $E$ that factors through a finite braid word is computable: it is reachable from $\mathcal{S}_0$ by a finite sequence of Toffoli gates. These sections form the computable fragment of the QOU. Sections requiring infinite crossing number are non-computable. They correspond to states of the universe unattainable from the Big Bang by any finite logic sequence. This distinction represents a topological property encoded by the finite degree of the Skein polynomial.
