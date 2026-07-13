<!-- FILE_START: intro-hecke-chi-closed-forms.md -->
The Hecke algebra carries two natural coordinate systems. The Markov $u$-coordinate adapts to braid-trace identities. The $\chi$-character coordinate adapts to representation-theoretic decomposition. This section derives the closed-form transformation between the two. We identify the substrate parameter as the deformation knob that interpolates the two coordinate charts. Finally, we tabulate the explicit closed forms for the characters required by the binding-energy computations.

The analysis proceeds in three stages. First, we reduce the $u$-coordinate identities to a small set of generating discharge moves (the $u$-coordinate discharges). We then express the $\chi$-character as a polynomial in $u$ and the substrate parameter. The middle blocks establish the closed-form $\chi$ values at the small partitions ($\lambda = (1)$, $(2)$, $(1,1)$, $(2,1)$, $\dots$) that drive the early-shell binding-energy formulas. The closing blocks tie the $\chi$-closed forms to the Markov-axiom recursive ascent used downstream by the Plancherel sum.

The output provides the $\chi$-character table indexed by partitions. The subsequent section's Markov-axioms-braid-link enumeration consumes this table as its primary input. Readers focused on the binding-energy applications can take the closed forms on faith. The substrate-parameter dependence remains uniform across partitions and does not interact with the enumeration.
<!-- FILE_END: intro-hecke-chi-closed-forms.md -->

<!-- FILE_START: u-coordinate-discharges.md -->
**Macdonald coordinate $u = q^2$ substantive discharges for $H_3 / V_{(2,1)}$ scalar invariants.**

Many scalar invariants in the Hecke and Wenzl-bridge algebras are rational in the Macdonald coordinate $u = q^2$, even when their defining formulas require `Real.sqrt` over $q$. We use this Macdonald substitution to eliminate square roots. This provides concrete, closed-form Lean identities that algebraically verify the explicit-residual discharges required in [`rem:ck-extraction-from-algebraic-rules`](#rem:ck-extraction-from-algebraic-rules) and related proofs.

## Substantive identities

See [Table](#tbl:u-coordinate-discharges-table-data).

We export each scalar identity as a Lean theorem. Because the substitution removes square roots, the `field_simp + ring` tactic closes every proof without opaque axioms.

## Significance

Previously, explicit-residual discharges at the class level (such as `⟨0, rfl⟩`) appeared abstractly trivial: the residual evaluates to $0$, but no concrete computation connects this to the underlying substrate arithmetic. The $u$-coordinate identities express the underlying scalars as rational functions in a single variable $u$. This enables `ring` and `field_simp` to verify the equalities mechanically.

For example, the abstract class field `HeckeQuadraticAllGenerators 3 q .hecke_quad_residual_eq_zero` mandates that the residual vanishes. The substantive reason for this vanishing lies in the identity `hecke_root_sum_times_q`: the relation $q \cdot (q - q^{-1}) = u - 1$ constitutes a non-trivial rational identity closed by `field_simp + ring`.

## Downstream dependencies

These $u$-coordinate identities act as the computational backing for several downstream files:

- `rem:ck-extraction-from-algebraic-rules` references these identities to justify its instances.
- `rem:h3-hecke-idempotents` links its `dimQ_V21^2` computation to `dimQ_V21_sq_in_u`.
- `prop:hoefsmit-V21-cos-symmetrization` establishes a no-sqrt closed form for the Hoefsmit coupling $b^2$ via `hoefsmit_b_sq_in_u`.
<!-- FILE_END: u-coordinate-discharges.md -->

<!-- FILE_START: multi-link-jones-q1-extension.md -->
**Multi-link Jones values at $q = 1$ — Lean infrastructure for the $c_5 / c_6$ candidate investigation.**

The $\mathfrak{Q}_\beta$ precision ladder ([`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder)) closed $c_1, c_2$ from Kashiwara ($b, b^2$), $c_3$ from $J_{\mathrm{Hopf}}(q{=}1) = -2$ at the 3-fold Markov closure, and $c_4$ from the mixed Kashiwara-plus-Hopf-half $b^2 + 1/2$. The simple alternating Kashiwara $\times$ Jones pattern at odd $k = 3$ suggests trying multi-link Jones values for $c_5, c_7, \ldots$ (e.g., Borromean rings, double-Hopf).

| coefficient | empirical | closest simple multi-link Jones candidate |
|:---:|---:|---:|
| $c_5$ | $\approx -395.4$ | $-J_{\mathrm{Borromean}} = +8$ (50$\times$ off in scale and sign) |
| $c_6$ | $\approx -45{,}485$ | $J_{\mathrm{Hopf}} \cdot J_{\mathrm{Borromean}} = 16$ (3000$\times$ off) |

## Contents of this block

This block provides **infrastructure, not closure**. The Lean module `QOU.BraidKnot.multi_link_jones_q1_extension` exports:

1. **Three new `Link` constructors** (extending the `Link` inductive in [`rem:braid-link-types`](#rem:braid-link-types)): `trefoil`, `borromean`, `doubleHopf`.
2. **Three new `jonesAtOne` cases**, each proved by `rfl`:

   | constructor | $J_L(q{=}1)$ | source |
   |---|---:|---|
   | `trefoil` | $+1$ | Jones 1985, $T(2,3)$ 1-component unnormalised |
   | `borromean` | $-8$ | Jones 1985 / Habiro 2002, 3-component Brunnian |
   | `doubleHopf` | $+4$ | $J_{\mathrm{Hopf}}^2$ by disjoint-union multiplicativity |

3. **Two combination values**: `jonesHopfTimesBorromean = 16`, `jonesBorromeanFlipped = 8`. Both candidates carry **explicit docstrings noting the empirical mismatch**. They are not closures.

## Failure of the simple multi-link pattern

We posit three structural hypotheses for the 50–3000$\times$ mismatch:

1. **Precision-ladder normalisation revision**: the $b^k$ factor multiplying $c_k$ beyond $k = 4$ may carry an extra Wedderburn-weight or coupling-constant prefactor not captured by the $(b \cdot \hbar_q^2)^k$ expansion ansatz.
2. **Sum-over-Wedderburn-blocks**: multi-link contributions enter via a non-trivial sum over $\lambda \vdash n$ rather than as a direct scalar multiple of a single Jones value. The $y_\lambda$ normalisation in the Wenzl bridge could redistribute weight in a way that magnifies single-Jones values into the empirical $c_5, c_6$ scale.
3. **New categorical input at $k \geq 5$**: a higher-rank irrep coupling, a Mostow rigidity gap correction, or a non-trivial Habiro residue contribution may enter only at orders $k \geq 5$.

We must test whether the per-Wedderburn-block contribution at $k = 5, 6$ matches the empirical values when properly weighted by the $q$-deformed dimensions $\dim_q(V_\lambda)$. This requires extending the Wenzl-bridge $y_\lambda$ infrastructure to $\varepsilon^{10}, \varepsilon^{12}$ evaluations of the $\tau_M$ expansion on $V_{(2,1)}, V_{(3)}, V_{(1,1,1)}$ separately.
<!-- FILE_END: multi-link-jones-q1-extension.md -->

<!-- FILE_START: hecke-algebra-type-scaffold.md -->
The Iwahori–Hecke algebra $H_n(R, q)$ is the unital associative algebra with generators $\sigma_0, \ldots, \sigma_{n-2}$ modulo three defining relations: the quadratic relation (R1), the far-commutation relation (R2), and the braid cubic relation (R3). Its full type-theoretic realization decomposes into four constructions: a free $R$-module on $B_n$, a multiplication structure, the quotient by the three relations, and the per-block Wedderburn decomposition (the $q$-deformed Schur–Weyl splitting $\sum_\lambda y_\lambda = 1$).

The Lean class scaffold (`HeckeGen n`, `HeckeWord n`, `HeckeRelations n q`, `HeckeWedderburn n q`) encodes the abstract generators, formal signed words, defining relations, and Plancherel completeness as class hypotheses. Downstream Lean theorems take `[HeckeRelations n q]` and `[HeckeWedderburn n q]` as hypotheses. The per-$n$ instances plug in when the relation-quotient and Murphy seminormal-form infrastructure land.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs: real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: hecke-algebra-type-scaffold.md -->

<!-- FILE_START: markov-trace-operator-construction.md -->
The Jones–Wenzl Markov trace $\tau_M : \mathbf{B}_\infty \to \mathbb{R}$ on the inductive limit of braid groups is uniquely characterised by the M1–M4 axioms (Jones 1985 / Wenzl 1988). We realise it as a single operator on the von Neumann inductive-limit hyperfinite $\mathrm{II}_1$ factor in five stages: a per-$n$ Hilbert representation, an inductive embedding $\iota_n : V_n \hookrightarrow V_{n+1}$, the inductive limit $V_\infty = \varinjlim V_n$, the trace state on $\bigcup_n H_n$, and the bicommutant closure $\mathcal{M} := (\bigcup_n H_n)''$. On $\mathcal{M}$, the trace $\tau_M$ provides the unique faithful normal trace up to scaling.

The Lean classes `HnHilbertRep n q`, `HnInductiveEmbedding n q`, and `MarkovTraceVNFactor q` encode the per-$n$ representation, the inductive embedding, and the GNS bicommutant factor hosting $\tau_M$. Downstream files import these classes as hypotheses. The operator-algebra steps—the GNS state and the bicommutant closure—supply the per-$n$ instances.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes analytic constructs: real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Generic categorical $q$-deformation identities remain valid over an abstract coefficient ring; we specialise only their archimedean realisation here.
<!-- FILE_END: markov-trace-operator-construction.md -->

