**Conjecture.** At the physical non-torsion substrate parameter $q_0 \in \mathbb{G}_m^{\mathrm{nt}}(\mathbb{R})$, we have $\mathrm{P} \neq \mathrm{NP}$. Equivalently, the resolution-tree evaluation of the universal obstruction class $\chi(A)$ is non-vanishing:
$$
  \mathrm{res}_{\mathcal{R}}\!\bigl(\chi(A)\bigr)  \neq  0 \qquad\text{at } q = q_0.
$$

**Established complexity landscape (chippable kernel).** The concrete computational object attached to a link $L = \hat{\beta}$ is its Jones invariant $J_L(q) = \mathrm{tr}_M(\rho(\beta))$, and its complexity is a *theorem*, stratified by the arithmetic of $q$:

- **Exact evaluation is $\#\mathrm{P}$-hard** at all but finitely many $q$ (Jaeger--Vertigan--Welsh). The only classically poly-time points are the roots of unity of order $n \mid 6$ — the values $q \in \{1, -1, \pm i, e^{\pm i\pi/3}\}$.
- **Additive approximation is $\mathrm{BQP}$-complete** at a primitive root of unity of order $n \nmid 6$ (Aharonov--Jones--Landau; Freedman--Kitaev--Larsen--Wang).

This stratification is cited fact, not a QOU derivation. Crucially, $\#\mathrm{P}$-hardness of one invariant's exact evaluation **does not** separate $\mathrm{P}$ from $\mathrm{NP}$: it concerns counting, not decision, and no known reduction turns it into a $\mathrm{P} \neq \mathrm{NP}$ proof.

**The $\mathbb{G}_m$-torsion stratification (corrected).** Earlier drafts stated the torsion dichotomy backwards. The correct picture, matching the citations above:

| Regime | Value of $q$ | Jones complexity |
|--------|--------------|------------------|
| Classically transparent | torsion, order $n \mid 6$ | poly-time (JVW tractable set) |
| Quantum-hard | torsion, order $n \nmid 6$ | $\mathrm{BQP}$-complete additive approximation (AJL) |
| Counting-hard | non-torsion $q_0$ | $\#\mathrm{P}$-hard exact evaluation (JVW) |

At a torsion root of unity of order $n \mid 6$ the Iwahori--Hecke algebra degenerates just enough that the invariant collapses to a poly-time formula. This — not torsion in general — is the transparent regime. At other roots of unity the algebra supports the AJL quantum algorithm ($\mathrm{BQP}$). At the non-torsion substrate value $q_0$ the algebra is semisimple and exact evaluation is $\#\mathrm{P}$-hard.

**Kummer persistence.** The Kummer filtration yields $\kappa_c^{\mathrm{comp}} \bmod n = 0$ if and only if $n \mid 6$ — precisely the JVW classically-tractable set. Because $q_0$ is strictly non-torsion, no finite Kummer level applies: $q_0$ sits permanently outside the transparent set.

**What is conjectural (the irreducible gap).** The step from the *established* "$\#\mathrm{P}$-hard exact Jones evaluation at $q_0$" to the *asserted* "$\mathrm{P} \neq \mathrm{NP}$" is an **analogy, not a theorem**. Two things are unproven and constitute the single `sorry` on the Lean carrier [`QouPNeqNp`](../lean/QOU/Information/QouPNeqNp.lean):

1. that the resolution-tree residue $\mathrm{res}_{\mathcal{R}}(\chi(A))$ is a faithful invariant of the $\mathrm{P}$-vs-$\mathrm{NP}$ decision boundary, rather than of the (easier-to-obstruct) counting problem; and
2. that its non-vanishing at $q_0$ is *equivalent* to $\mathrm{P} \neq \mathrm{NP}$ rather than merely *implied by* it.

A concrete non-vanishing of $\chi(A)$ at generic $q_0$ is a Zariski-open (hence generically true, easy) condition; it therefore **cannot** by itself discharge the conjecture without collapsing the claimed equivalence. This genericity is itself Lean-proved, sorry-free, in the companion module [`ObstructionGenericity`](../lean/QOU/Information/ObstructionGenericity.lean): a nonzero polynomial obstruction vanishes at only finitely many parameter values (`obstruction_vanishing_locus_finite`), so its non-vanishing locus over an infinite domain is cofinite, hence infinite (`obstruction_nonvanishing_locus_infinite`) — stated over a generic integral domain, with no archimedean input. This is the chippable boundary: everything above the line is cited or provable; only the analogy remains open.

**The non-vanishing leg is itself an axiom consequence.** The corpus derives the scalar value $\chi(A) = -6$: the observability axiom kills $HH^0$, the Frobenius--Hopf self-duality induces the Yekutieli--Van den Bergh Poincaré duality on Hochschild cohomology so that $HH^2 \cong (HH^1)^\vee \cong k$ ([obstruction reduction](#prf:qou-obstruction-reduction)), and the Riemann--Roch / branch-point chain on Bring's surface pins the value ([the $\chi(A) = -6$ chain](#ex:chi-minus-six-derivation)). With $q_0$ strictly non-torsion, the Kummer filtration then yields $\mathrm{res}_{\mathcal{R}}(\chi(A)) \neq 0$ at $q_0$ — and no step of that chain refers to computational complexity. This sharpens the collapse observation above: were the asserted equivalence a theorem, $\mathrm{P} \neq \mathrm{NP}$ would follow from the QOU axioms by the eight-step chain alone. The conjecture's entire open content therefore lives in items 1--2 (faithfulness of the residue for the decision boundary), not in the non-vanishing.

**The fourth millennium evaluation.** The QOU obstruction reduction *conjectures* that all classical-limit obstructions map to the scalar class $\chi(A) \in HH^2 \cong k$, so that $\mathrm{P}$ vs $\mathrm{NP}$ becomes a fourth restriction of the same class alongside RH, NS, and BSD. The proportionality of the four evaluations is part of the conjecture, not a consequence of it.

**Corollary (conditional).** *If* the obstruction-class conjecture holds, resolving $\mathrm{P}$ vs $\mathrm{NP}$ constrains RH, NS, and BSD and vice versa, their evaluation maps differing but the underlying class remaining identical. The corollary inherits the conjectural status of its hypothesis.

**Parallel route.** This obstruction-class formulation is one of two independent attacks on the same separation. The Reeb--surreal route ([P vs NP in the QOU](#conj:p-vs-np-qou)) instead recovers $\mathrm{P} \neq \mathrm{NP}$ as the standard part of a strict $\mathbf{P} \subsetneq \mathrm{BQP}_q$ inclusion, via the surreal squeeze $\mathrm{ord}_\omega(\text{cost}) > \mathrm{ord}_\omega(\text{budget})$. The two carriers agree on the conclusion but neither is derived from the other; both remain open.
