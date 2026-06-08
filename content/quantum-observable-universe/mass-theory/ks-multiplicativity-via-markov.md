Kontsevich--Soibelman's Theorem 8 \cite{kontsevich-soibelman-2008}
states that the Donaldson--Thomas counting map
$\Phi \colon H(\mathbf{C}) \to R_\Gamma$ is a homomorphism of
$\Gamma$-graded algebras — *disjoint union maps to product*. Their
proof routes through the **motivic Hall algebra** (their Propositions
10--12): a stack-level integration whose foundations
(ind-constructibility, orientation data, the motivic quantum torus)
occupy most of the paper.

In the QOU setting the same multiplicativity is **two lines** — the
same reduction by which the Gröbner--Shirshov / Diamond-Lemma proof
of Poincaré--Birkhoff--Witt \cite{bergman1978} replaces the
analytic Lie-theoretic argument (the unital Gröbner-bases route to
PBW).

**Setup (two definitions).**

1. *The disjoint-union monoid of links.* Links form a commutative
   monoid $(\mathcal{L}, \sqcup)$ under split union; on braids this is
   the block inclusion
   $H_m(q) \otimes H_n(q) \hookrightarrow H_{m+n}(q)$.
2. *The Markov trace*
   $\mathrm{tr}_M \colon \mathcal{L} \to \mathbb{Z}[q^{\pm 1/2}]$.

**Two-line proof.** A split braid $\beta \sqcup \beta'$ has no
generator $\sigma_i$ linking the two blocks, so the right-to-left
Markov peel ([Markov-trace
factorization](#thm:markov-trace-factorization)) processes the two
blocks independently — peeling $\beta'$ never meets a generator of
$\beta$. Hence

$$
  \mathrm{tr}_M(\beta \sqcup \beta')
  \;=\;
  \mathrm{tr}_M(\beta)\,\mathrm{tr}_M(\beta'),
$$

i.e. $\mathrm{tr}_M$ is a **monoid homomorphism**
$(\mathcal{L}, \sqcup) \to (\mathbb{Z}[q^{\pm 1/2}], \cdot)$.
$\square$

This is the QOU avatar of KS Theorem 8 — the invariant is
multiplicative — with no Hall algebra, motivic measure, or
ind-constructibility: a known result given a prior heavy/motivic
proof, recovered here by an elementary algebraic one.

**Precision (what is and is not claimed).** The multiplicativity is
for the **monoidal** structure $\sqcup = \otimes$, *not* the internal
product:
$\mathrm{tr}_M(ab) \neq \mathrm{tr}_M(a)\,\mathrm{tr}_M(b)$ in
general (only the trace property
$\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$ holds). KS Theorem 8 is
likewise a statement about the counting/integration map on the
*disjoint-union* grading, not the internal multiplication. The
shortcut applies to that statement only — not to the wall-crossing
apparatus (KS Theorems 3--4), which is the archimedean locus the QOU
framework deliberately does not enter.
