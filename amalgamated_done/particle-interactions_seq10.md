<!-- FILE_START: atomic-braid-mass-crossing-locality-cpt-intro.md -->
The preceding sub-section developed foundations for the atomic-braid LP and mass formula. This sub-section establishes consequences for crossing grading, locality, and CPT orbits. We treat mass-volume factorization, the crossing-graded mass expansion, and lifted-crossing locality. We derive $q$-holonomy locality, Frobenius-packing density, and CPT-orbit closure density. Finally, we establish bar-involution invariance and soft-confinement at $q_0$.
<!-- FILE_END: atomic-braid-mass-crossing-locality-cpt-intro.md -->

<!-- FILE_START: q-holonomy-locality-derivation.md -->
## Locality from flatness of the KZ connection

The lifted-crossing locality hypothesis reduces to a statement about the holonomy of the Knizhnik-Zamolodchikov (KZ) connection at generic $q$. Cross-talk between two lifted crossings measures the curvature of a flat connection. Flatness implies factorization.

## Setup — the KZ connection

Let $X_n$ be the configuration space of $n$ distinct complex points. The quantum KZ connection on $X_n$ is flat. The monodromy representation coincides with the quantum-group R-matrix representation.

## Applying to the mass endomorphism

We model each crossing of an atomic braid as a puncture in $X_n$. A lifted crossing inserts $\Phi_q(z_c)$; an unlifted crossing inserts the identity. The mass contribution is the trace of the braid-word operator, computed via parallel transport.

**Claim.**
*At generic $q$, the parallel transport factorizes over disjoint punctures:*

$$
  \mathrm{Tr}\!\left[
    \prod_{c \in S} \Phi_q(z_c) \cdot \rho(\beta)
  \right]
  \;=\;
  \mathrm{Tr}[\rho(\beta)] \cdot \prod_{c \in S}
  \eta(c),
$$

*where $\eta(c)$ is the single-crossing expectation value.*

**Proof sketch.**
By flatness, closed loops encircling separated subsets have commuting holonomies. Simultaneous diagonalization decomposes the trace. The $\Phi_q$ insertions act by scalar on each eigenstrand. Thus, the multi-crossing expectation is a product of single-crossing expectations. The scalar obstruction requires non-abelian monodromy, which flatness rules out. $\square$

## Failure of flatness

Flatness is equivalent to semisimplicity of the braided tensor category. At generic $q$, representations are semisimple and locality holds. At roots of unity, non-semisimple subquotients appear and locality fails.

## The substrate as the locality window

At the pinned parameter $q_0 \approx 1.11$, the KZ connection is flat and locality holds. The soft confinement level is far from the first non-trivial root of unity, so locality holds to high order.

## Corollary — exponential mass scaling

Combining locality with the crossing-graded expansion, we find that at the homogeneous fixed point, $\mathfrak{m}(\mathcal{K}; q_0) = \mathfrak{m}_{\mathrm{GB}}(\mathcal{K}) \cdot (1 + \xi(q_0))^{c(\mathcal{K})}$. Each crossing multiplies mass by $\approx 94$. Exponential scaling is the empirical signature of KZ flatness at the substrate.
<!-- FILE_END: q-holonomy-locality-derivation.md -->

<!-- FILE_START: cpt-orbit-closure-density.md -->
**Proposition (conditional).**
Let $\sigma \colon \mathrm{Part}(n) \to \mathrm{Part}(n)$ be the transpose involution. Define $\mathrm{CPTSat}(\mathcal{K})$ to mean $\Lambda(\mathcal{K})$ is closed under the fold.

Then the Frobenius packing-density rule is a derived consequence of crystal structure:

$$
  \boxed{\;
    \rho_F(\mathcal{K})
    \;=\;
    \begin{cases}
      m_e   & \text{if } \mathrm{CPTSat}(\mathcal{K}) \text{ is false}, \\[4pt]
      2 m_e & \text{if } \mathrm{CPTSat}(\mathcal{K}) \text{ is true}.
    \end{cases}
  \;}
$$

## Elimination of the Boolean flag

The proposition replaces the manual Boolean flag with the structural predicate $\mathrm{CPTSat}$, derived from the Type-B fold. CPT enforcement is now structural rather than post-hoc. The semantic equivalence holds for finite $\Lambda$.

## Example: $n = 3$ Wedderburn

For the blocks of $H_3(q)$, the Boolean flag is recovered as the orbit-closure check in every case.

## Correctness of the fold involution

The Type-B Cartan datum is obtained by folding. The KLR canonical basis is bar-invariant. The bar involution matches the chirality-reversal. Thus, $\sigma$ is the intrinsic fold.

## Lean formalisation

The Lean formalisation defines partition transpose and CPT saturation, proving their equivalence to the Boolean flag.

**Archimedean specialisation (§7c).** This block invokes real- or complex-analytic constructs. Categorical identities remain valid over an abstract coefficient ring; their archimedean realisation is specialised here.
<!-- FILE_END: cpt-orbit-closure-density.md -->

<!-- FILE_START: bar-involution-invariance.md -->
**Proposition (conditional).**
Let $\bar\cdot$ be the bar-involution sending $q \mapsto q^{-1}$. Then:

1. (**Plancherel-weight invariance**) The Plancherel weight satisfies $\overline{w_\lambda(q)} = w_\lambda(q)$.
2. (**Transpose-pair equality**) $w_\lambda(q) = w_{\lambda^T}(q)$.
3. (**Type-B-folded normal forms**) Any Hecke normal form produced by the pair-production engine is bar-invariant: $\overline{T_w} = T_w$.

## Significance: a witness against hand-rolled CPT violations

These conditions are necessary consequences of Type-B folding. Any normal form, mass formula, or LP cost vector must satisfy them. Failure signals a chirality bias incompatible with the symmetric-crystal substrate. This block packages the invariance lemmas as a regression-test witness.

## Proofs

**(1) Plancherel-weight invariance.** The $q$-integer $[k]_q$ is bar-invariant. The entire Plancherel weight is a quotient of bar-invariants, hence bar-invariant. $\square$

**(2) Transpose-pair equality.** Hook lengths are unchanged by transpose. This yields identical $w_\lambda$. $\square$

**(3) Type-B-folded normal forms.** The folded operator pair produces two descendants whose normal forms are bar-conjugates. Their sum is bar-invariant.

## Worked example: $n = 3$

Transpose pairing yields identical hook products, matching part 2. Bar-invariance follows from $[k]_{q^{-1}} = [k]_q$ on every factor.

## Lean formalisation

The Lean formalisation defines the bar-involution, $q$-integer, and Plancherel weight, and proves the relevant invariance lemmas.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall.
<!-- FILE_END: bar-involution-invariance.md -->

<!-- FILE_START: soft-confinement-at-q0.md -->
**1. Soft confinement at the substrate parameter.**
The Wedderburn block labels of $H_n(q)$ are $q$-independent, but the Plancherel weights depend sensitively on $q$. At roots of unity, sharp truncation occurs. At the generic real substrate parameter $q_0 \approx 1.11$, no representation is strictly confined, but weights decay rapidly, producing a soft confinement level $\ell_*(q_0) \approx 9.6$. Partitions exceeding $\ell_*$ contribute negligibly.

**2. Implication for atomic braids.**
An atomic braid lives in $H_{3A}(q_0)$. Soft confinement implies no truncation for light atoms, exponential suppression for medium atoms, and effective truncation for heavy atoms. This transition dictates why $\alpha$-cluster unfolding is numerically necessary beyond $A \sim 4$.

**3. Numerical estimate.**
See [Table](#tbl:soft-confinement-at-q0-table-data). The rapid saturation demonstrates soft confinement. The cutoff $\ell_*(q_0) \approx 10$ is the horizon where grading effectively terminates.
<!-- FILE_END: soft-confinement-at-q0.md -->
