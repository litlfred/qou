---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal a nd other strong Rayleigh measures"
section_id: sec-009-52-exclusion-measures
section_title: "Exclusion measures"
section_number: 5.2
pages: 16-18
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
---
The symmetric group Sn acts on Bn by permuting the coordinates. Suppose a nonnegative rate
r(τ ) is given for each transposition τ ∈ S n. Deﬁne a random evolution on Bn by letting each pair
of coordinates ( i,j ) transpose independently at rate r(τij ). In other words, we have a continuous
time chain on Bn which jumps from x to τ (x) at rate r(τ ) for each transposition τ . This process is
known as the symmetric exclusion process.
Borcea, Branden and Liggett [BBL09, Proposition 5.1] prove that t he strong Rayleigh property
is preserved under this evolution. In particular, because the point mass at a single state is always
strong Rayleigh, it follows that the time t distribution of a symmetric exclusion process started from
a deterministic state is strong Rayleigh. The stochastic covering pr operty follows, as do PHR and
negative association. Interestingly, before the publication of [BBL 09], all that was known about this
model was negative cylinder dependence [Lig77, Lemma 2.3.4]).
Recently, it was shown by [Wag11] that one can add birth and death t o the exclusion dynamics
and still preserve the strong Rayleigh property. More speciﬁcally, let {αi,β i : 1 ≤ i ≤ n} be
positive real numbers and let ωi change to one at rate αi and to zero at rate βi, along with the
exclusion dynamics. Then the evolution preserves the strong Rayle igh property and in particular, if
the starting state is deterministic, all time t marginals are strong Rayleigh.
Corollary 5.5. Let P be the law on Bn resulting from running an exclusion process for a ﬁxed time,
starting from a deterministic state with k sites occupied. Then
P(f − Ef ≥a) ≤e−a2/(8k).
Example 5.6. Let n > 0 be even and populate a n ×n square of the integer lattice in Z2 (with
torus boundary conditions) by ﬁlling all sites in the left ha lf and leaving empty all sites in the right
half. Run the symmetric exclusion process for time t with rate 1 on each edge. Let ft(ω) denote the
number of edges at time t with exactly one endpoint occupied. The mean of ft starts at n at time
0 and approaches its limiting value of n2 −O(1) as t → ∞ . Once t = Θ( n2), the variance of ft
15
becomes Θ(n2) and the concentration inequality
P(f − Ef ≥a) ≤e−a2/(4n2),
which holds for all t, becomes a meaningful Gaussian tail bound (here k =n2/2).
5.3 Determinantal measures on a ﬁnite Boolean lattice
We say that a probability measure P on Bn is determinantal (in the general sense) if there is an
n ×n real or complex matrix K such that that for every S ⊆ {1,...,n },
E
∏
j∈S
Xj = detKS (5.1)
whereKS is the submatrix of K obtained by choosing only those rows and columns whose index is in
S. In this deﬁnition, the phrase “general sense” refers to the lack of further assumptions on K. An
important subclass is the Hermitian determinantal measures, for which the matrix K is Hermitian.
In this paper we will be interested only in the Hermitian case and will use the term determinantal
hereafter to refer only to the case where K is Hermitian. Determinantal measures are known to
be negatively associated [Lyo03, Theorem 6.5]. In fact they are str ong Rayleigh [BBL09, proof of
Theorem 3.4] and therefore satisfy the stochastic covering prop erty.
Example 5.7 (uniform or weighted spanning tree) . As previously remarked, the uniform or weighted
random spanning tree is a determinantal measure.
In the next section we will extend the notion of a determinantal mea sure to the continuous
setting. The extension to a countably inﬁnite set of variables is more straightforward: the kernel K
is now indexed by a countably inﬁnite set, but (5.1) may be interprete d as holding for all ﬁnite sets
S. The following example of a determinantal process on Z appeared ﬁrst in [Joh03].
Example 5.8 (positions of non-colliding R W’s) . Let {Y (k) : 1 ≤ k ≤ n} be n independent time
homogeneous nearest neighbor random walks on Z. Begin the walks at locations y1,...,y n and
suppose the event that the walks are all at their starting pos itions at time 2n and have not intersected
has positive probability. Conditional on this event, the po sitions at time n form a determinantal
measure. That is, the indicator functions {Xj} have a determinantal law, where Xj = 1 if some
Y (k) is at position j at time n, and zero otherwise.
Remark. The positions of non-colliding random walks are given by a determinant under more general
conditions (see [KM59]). The present situation is arranged so as to m ake the kernel Hermitian.
16
