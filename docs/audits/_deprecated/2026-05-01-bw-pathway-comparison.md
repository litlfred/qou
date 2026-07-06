> **DEPRECATED on 2026-05-24.** Workplan / status snapshot / investigation result / closure-attempt that has been integrated into main or superseded by a later resolution. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) for the tranche rationale.

# BW pathway comparison — ladder vs Wenzl bridge vs LP shadow-price

**Workplan task**: P3.6.
**Pair**:
[`2026-05-01-math-framework-workplan.md`](2026-05-01-math-framework-workplan.md),
[`2026-05-01-math-framework-deep-audit.md`](2026-05-01-math-framework-deep-audit.md)
§2·C (BW-8, BW-11).
**Status**: scoping / inventory.

## Why this matters

The 11 extended Bethe-Weizsäcker coefficients in
[`prop:q-integer-mass-formula`](../../content/quantum-observable-universe/particle-interactions/q-integer-mass-formula.md)
are derivable through three distinct algebraic pathways, each
exposing a different structural feature of the Hecke algebra. The
audit's BW-8 / BW-11 closure (P1.2 / P1.3) currently picks any one
pathway as canonical; the repo-owner directive is to either:

1. **Prove** the three give pairwise-identical symbolic outputs in
   $\mathbb{Z}[q^{\pm 1}]$ on every BW coefficient, or
2. **Document** the regimes in which each is preferred and keep all
   three as parallel canonical pathways.

Picking one without the equivalence proof loses information.

## The three pathways

### Pathway A — direct BW skein ladder

**Formula** (per-isotope):
$$
B_{\text{pred}} = B_{\text{leading}} + \alpha \cdot m_e \cdot |(q; q)_r|
$$
where $|(q; q)_r| = \prod_{k=1}^{r} (1 - q^k)$ is the truncated
$q$-Pochhammer and $(\alpha, r)$ are partition-by-partition
parameters of the binding ladder.

**Compute**:
[`computations/binding_ladder_catalog.py`](../../computations/binding_ladder_catalog.py).

**What it exposes**: per-partition contribution structure
(D / T / ³He / ⁴He / ⁶Li / ⁷Li receive distinct ladder corrections).
The ladder is the natural object on the **enumerative-combinatorial**
side of the Skein resolution tree.

**Drawback**: the per-isotope $(\alpha, r)$ values look like fits;
in fact they are projections of a single symbolic ladder, but
displaying them as a list per isotope obscures the unified origin.

### Pathway B — Wenzl bridge (Schur principal-specialization)

**Formula** (Markov-trace central coefficient at partition
$\lambda \vdash n$):
$$
y_\lambda \;=\; \frac{s_\lambda(1, Q, Q^2, \ldots, Q^{r-1})}
                    {\sum_{\mu \,\vdash\, n} d_\mu \cdot s_\mu(1, Q, Q^2, \ldots, Q^{r-1})}
$$
with $Q = q^2$, $d_\mu = f^\mu$ the classical $S_n$-irrep dimension,
$s_\lambda$ the principal-specialization Schur polynomial in $r$
variables, and $r$ the unique solution of
$q \cdot z = Q^r (1 - Q) / (1 - Q^r)$.

**Source**:
[`prop:y-lambda-closed-form-wenzl-bridge`](../../content/quantum-observable-universe/braids-and-knots/y-lambda-closed-form-wenzl-bridge.md),
[`prop:wenzl-bridge-applicability-qou`](../../content/quantum-observable-universe/braids-and-knots/wenzl-bridge-applicability-qou.md).

**Compute**:
[`y_lambda_wenzl_bridge_extended.py`](../../computations/y_lambda_wenzl_bridge_extended.py),
extending to $n = 12$ via $O(p(n) \cdot \max\text{hooks})$
specialization rather than $O(p(n)^3)$ linear-system solve.

**What it exposes**: a single closed-form ratio of Schur
polynomials. The "ladder cabling" of the Hecke algebra (Wenzl's
projector tower) is implicit in the principal specialization;
recovering the per-partition BW coefficients from $y_\lambda$ is
mechanical.

**Drawback**: looks transcendental (Schur polynomial); does not
expose the LP-dual structure.

### Pathway C — LP shadow-price (Schrijver / Wigner-2)

**Formula** (self-conjugate $\lambda$ at Hecke level $k$):
$$
C_\lambda \;=\; w_\lambda \cdot h / 2,
\qquad h = q - q^{-1}
$$
where $w_\lambda$ is the optimal LP-dual variable of the Frobenius
positivity constraint $\langle \Phi, \pi_\lambda \rangle_F \geq 0$
in the operator-selection LP. For self-conjugate partitions, the
trace-per-dim identity (Wigner-2) gives the direct closed form.

**Source**:
[`prop:mass-coefficient-shadow-price`](../../content/quantum-observable-universe/braids-and-knots/mass-coefficient-shadow-price.md),
[`prop:wigner-coefficient-derivation`](../../content/quantum-observable-universe/braids-and-knots/wigner-coefficient-derivation.md).

**Compute**:
[`shadow_price_c_321_q0.py`](../../computations/shadow_price_c_321_q0.py),
[`paper_six_term_shadow_price_sweep.py`](../../computations/sweeps/paper_six_term_shadow_price_sweep.py).

**What it exposes**: the BW coefficients as **shadow prices** —
i.e., what would change in the optimal LP value per unit relaxation
of the Frobenius constraint. This connects directly to the
operator-selection LP and gives a physical "price of positivity"
interpretation.

**Drawback**: does not extend trivially to non-self-conjugate
partitions; the conjugate-pair coefficients (BW-10, BW-11) need
additional structure to fit this template.

## Per-coefficient pathway map

Status flags from
[`computations/DERIVATION-STATUS.md`](../../computations/DERIVATION-STATUS.md)
lines 45–55. Pathway columns mark which derivation has been
explicitly worked out for that term (✓), partial (~), or absent (·).

| # | Term | Partition | Ladder (A) | Wenzl (B) | LP-dual (C) | Status |
|---|------|-----------|:-:|:-:|:-:|--------|
| 1 | Volume | $[2,1]\,h^0$ | ✓ | ✓ | ✓ | DERIVED |
| 2 | Surface | $[2,1]\,h^2$ boundary | ✓ | ✓ | ✓ | DERIVED |
| 3 | Coulomb | $[2,1]\,$pp excess | ✓ | ✓ | ✓ | DERIVED |
| 4 | Asymmetry | $[2,1]\,h^1$ Casimir | ✓ | ✓ | ✓ | DERIVED |
| 5 | Pairing | $[3]+[1^3]$ descent | ✓ | ✓ | ~ | DERIVED |
| 6 | Exchange | $[2,1]\,h^3$ boundary | ✓ | ✓ | ✓ | DERIVED |
| 7 | Shell | $[3,1]$ branching | ✓ | ✓ | ✓ | DERIVED |
| 8 | Hook | $[2,2]$ self-conj | ✓ | ~ | ~ | **DERIVED (coeff ad hoc)** |
| 9 | Wigner | $[3,1,1]$ Frob reciprocity | ✓ | ✓ | ✓ | DERIVED |
| 10 | Form factor | $[3,2]\oplus[2,2,1]$ conj pair | ✓ | ~ | · | DERIVED |
| 11 | pn corr | $[4,1]\oplus[2,1,1,1]$ conj pair | ✓ | ~ | · | **DERIVED (coeff approx)** |

The two non-derived coefficients (BW-8 Hook, BW-11 pn corr) are
exactly the cases where the LP-dual pathway (C) is partial or
absent. Closing them via Wenzl-bridge or via dual-LP extension
(handling conjugate pairs) discharges P1.2 / P1.3 *and* gives the
first non-trivial test of pathway equivalence.

## Known equivalences

- **A ≡ B** at $n = 3, 4$: verified at floating-point precision in
  [`y_lambda_wenzl_bridge_extended.py`](../../computations/y_lambda_wenzl_bridge_extended.py)
  ("at $n = 3, 4$, the Wenzl-bridge values agree with the
  y-lambda-symbolic-witness.json values to floating-point
  precision").
- **B ≡ C** for self-conjugate $\lambda$ at $n \leq 6$: implicit in
  [`prop:wigner-2-coefficient`](../../content/quantum-observable-universe/braids-and-knots/wigner-2-coefficient.md);
  the Wigner-2 result $C_\lambda = w_\lambda \cdot h / 2$ matches
  the principal-specialization ratio for self-conjugate $\lambda$
  by direct symbolic comparison.

The triangle (A ≡ B ≡ C) is **not yet** closed across all 11 BW
terms. The remaining gaps are concentrated on conjugate-pair
coefficients (BW-10, BW-11) and the Hook self-conjugate (BW-8).

## Proposed equivalence test (BW-11 as the canonical case)

The pn correction term BW-11 is the natural test case:

- Self-flagged "approx" — needs closure regardless.
- Lives on the conjugate pair $[4, 1] \oplus [2, 1^3]$, exactly
  where pathway C (LP-dual self-conjugate) is incomplete.
- The Wenzl bridge gives $y_{[4,1]}$ and $y_{[2,1^3]}$ via
  pathway B; pathway A gives the per-isotope ladder; pathway C
  needs the conjugate-pair extension.

**Test plan**:

1. Compute $y_{[4,1]} + y_{[2,1^3]}$ symbolically via pathway B
   (Wenzl bridge) at $n = 5$; reduce to $\mathbb{Z}[q^{\pm 1}]$.
2. Compute the ladder coefficient via pathway A (extract from
   `binding_ladder_catalog.py` or analogue).
3. Solve the LP-dual at $n = 5$ for the conjugate pair (extend
   pathway C to handle $\lambda + \lambda'$ together).
4. Compare the three symbolic outputs.

If they agree identically → the triangle closes for BW-11, and
the "approx" tag in DERIVATION-STATUS.md drops to "DERIVED".
If they agree only at $q_0$ → the regimes diverge; document each
pathway's domain of validity and keep all three.

## Recommendation

**Keep all three pathways.** The ladder (A) is not redundant — it
exposes the per-partition enumerative structure that the LP dual
collapses. The Wenzl bridge (B) is the single closed-form. The
LP-dual (C) is the connection to operator-selection physics.
Picking any one as canonical loses one of these features.

**Add a `pathway:` field** to BW-coefficient blocks indicating
which derivation produced each entry. Track pairwise-equivalence
status (proven ✓ / numerical ~ / open ·) per coefficient in this
audit doc until the triangle closes uniformly.

## Open questions for follow-up

1. Does the conjugate-pair extension of pathway C (LP-dual on
   $\lambda + \lambda'$) admit a closed form analogous to the
   self-conjugate Wigner-2 result?
2. Is the ladder $|(q;q)_r|$ identifiable as a Schur principal-
   specialization (i.e., is pathway A literally a re-parametrisation
   of pathway B)?
3. Beyond $n = 12$ (current Wenzl-bridge ceiling), do all three
   pathways extend or do they branch? CRT polynomial reconstruction
   (per workplan §P2.2) would be needed to test.

---

*Generated as the scoping document for P3.6; tracked on branch
`claude/tier3-math-audit-B0wyO`.*
