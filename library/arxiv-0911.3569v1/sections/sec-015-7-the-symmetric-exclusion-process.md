---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-015-7-the-symmetric-exclusion-process
section_title: "The symmetric exclusion process."
section_number: 7
pages: 19-19
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
---
This section summarizes an application of stable polynomials to probability and
statistical mechanics from a 2009 paper of Borcea, Br¨ and´ en and Liggett [7].
Let Λ be a set of sites. A symmetric exclusion process (SEP) is a type of Markov
chain with state space a subset of {0, 1}Λ. In a state S : Λ→{ 0, 1}, the sites in
S−1(1) are occupied and the sites in S−1(0) are vacant. This is meant to model
a physical system of particles interacting by means of hard-core exclusions. Such
models come in many varieties – to avoid technicalities we discuss only the case
of a ﬁnite system Λ and continuous time t. (The results of this section extend to
countable Λ under a reasonable ﬁniteness condition on the interaction rates.) Sym-
metry of the interactions turns out to be crucial, but particle number conservation
is unimportant.
Let E be a set of two-element subsets of Λ. For each {i,j}∈ E, let λij > 0 be
a positive real, and let τij : Λ→ Λ be the permutation that exchanges i and j and
ﬁxes all other sites. Our SEP Markov chain M proceeds as follows. Each{i,j}∈ E
has a Poisson process “clock” of rateλij, and these are independent of one another.
With probability one, no two clocks ever ring at the same time. When the clock
of{i,j} rings, the current state S is updated to the new state S◦τij. In other
words, when the{i,j} clock rings, if exactly one of the sites {i,j} is occupied then
a particle hops from the occupied to the vacant of these two sites.
Let Λ = [m] and Ω ={0, 1}Λ, let ϕ0 be an initial probability distribution on Ω,
and let ϕt be the distribution of the state of M, starting at ϕ0, after evolving for
time t≥ 0. We are concerned with properties of the distribution ϕt that hold for
all t≥ 0.
