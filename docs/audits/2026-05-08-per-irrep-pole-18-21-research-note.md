# Per-irrep pole derivation of `18Z + 21N + 1` — research-grade follow-up

**Date:** 2026-05-08
**Status:** **Research-grade.** Documented here as the next open
question after PR #572's q-Hecke character closure
([`docs/audits/2026-05-08-q-hecke-character-gap-closure.md`](2026-05-08-q-hecke-character-gap-closure.md)).
Not blocking PR #572.

## Background

`prop:per-nucleon-shift-additive-linearity` (already on `main`)
proves that the canonical `pppnnn` atomic-braid Markov-trace
denominator $D(u) = 2^{2A+1} \cdot u^{18Z + 21N + 1} \cdot (1 + u^2)^{3A-1}$ has
shift exponent

$$\mathrm{shift}_{\mathrm{NF}}(\beta_{\mathrm{atomic}}(Z, N)) \;=\; 18 Z + 21 N + 1.$$

The constants `18, 21, 1` decompose (per
[`docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md`](2026-05-08-crystal-r-matrix-sublemma-2-1.md)
Step 5) as

| Coefficient | Per-component pole order | Provenance |
|---:|---|---|
| 18 | per-new-proton: $\mathrm{ord}_{q=0}^{(-)} \chi^{\mu_p^*}(\beta_p)$ | AXKIA commit `2f186ebc9` (empirical); cited as input |
| 21 | per-new-neutron: $\mathrm{ord}_{q=0}^{(-)} \chi^{\nu_n^*}(\beta_n)$ | same |
| 1 | inter-nucleon interface: $\alpha_{\mathrm{shift}}(T_{(2,1)}) = 1 \cdot (2 - 1)$ | derived from `prop:alpha-shift-torus-knot` + crystal-R-matrix audit |

The interface contribution `1` is **derived** from
[`prop:q-hecke-seminormal-character-closure`](../../content/quantum-observable-universe/braids-and-knots/q-hecke-seminormal-character-closure.md)
infrastructure (Hoefsmit χ^λ_q on the canonical word includes the
$\sigma_{n_1} - \frac{h}{2} \cdot 1$ interface; Crystal-R-matrix
Step 2 gives pole order $1$ when $\rho_T(j) \le -1$).

The per-nucleon `18` and `21` are currently **empirical inputs**
from AXKIA — derived from numerical pole-order analysis of the
canonical proton and neutron braid words at the LR-maximizer
partitions $\mu_p^*$ and $\nu_n^*$.

## What's open

A first-principles categorical derivation of `18` and `21` from
the substrate parameter $q$ and the canonical proton/neutron
braid-word structures. Three paths:

### Path A: direct seminormal pole-order analysis

For each of $\lambda \in \{(3), (2, 1), (1, 1, 1)\}$ at $H_3$:

- Compute the Hoefsmit seminormal action of the proton's
  canonical 11-crossing word $\beta_p$ in the $\lambda$-irrep.
- Find the maximum pole order at $q = 0$ of the matrix entries.
- Identify the maximizer $\mu_p^*$ and report
  $\mathrm{ord}_{q=0}^{(-)} \chi^{\mu_p^*}(\beta_p)$.

The infrastructure exists (`hoefsmit_symbolic.chi_lambda_symbolic`
+ `canonical_braid_crossings.atom_canonical_crossings(1, 0)`).
The pole-order computation requires symbolic expansion of the
trace and tracking the leading $q$-coefficient sign across all
matrix-product steps.

**Estimated effort:** 1–2 days. The proton case alone exercises
the technique; the neutron is symmetric.

### Path B: q-ribbon-tableau weights

The Wenzl-style q-ribbon-tableau formulation expresses
$\chi^\lambda_q$ on cycle types as a sum over q-ribbon tableaux,
each weighted by $q^{\mathrm{spin}}$. For the canonical pppnnn
braid, the cycle-type permutation is computable; the
ribbon-tableau enumeration gives an explicit closed form for
$\chi^\lambda_q(\beta_p)$ at every $\lambda \vdash 3$.

Pole-order analysis on the closed form recovers `18` directly.

**Estimated effort:** 1 week. Q-ribbon-tableau enumeration is a
standard combinatorial technique (Stanley §7.17, Mathas §3.5);
the canonical-braid cycle type makes it tractable for $H_3$.

### Path C: KLR / categorification bypass

Per [`conj:crystal-graph-realization`](../../content/quantum-observable-universe/braids-and-knots/crystal-graph-realization.md)
(merged on `main`), the Brundan–Kleshchev iso connects
$H_n(R, q)$ to KLR cyclotomic quotients with explicit grading.
The q=0 pole order of $\chi^\lambda_q$ corresponds to a graded
Euler characteristic of an indecomposable graded module.

For the proton's word, the graded character of the relevant KLR
module is computable from the diagrammatic side of the BK
isomorphism. **`18` would then be a degree shift in a graded
Euler-characteristic computation.**

**Estimated effort:** research-grade. Requires the full KLR
diagrammatic apparatus (Khovanov–Lauda 2009).

## Path A — concrete H_3 result (2026-05-09)

`folio-assistant/computations/per_irrep_pole_proton_h3.py` now
implements Path A directly. Concrete output:

| λ ⊢ 3 | $\chi^\lambda_q(\beta_p)$ (simplified) | $\mathrm{ord}_{q=0}^{(-)}$ |
|---:|---|---:|
| $(3)$ | $q(q^4 + 2q^2 + 1)/4$ | 0 |
| $(2, 1)$ | $(q^{22} + q^{20} + q^{18} + q^{14} - q^8 - q^4 - q^2 - 1) / (4q^{11})$ | **11** |
| $(1, 1, 1)$ | $(-q^4 - 2q^2 - 1)/(4q^5)$ | 5 |

**Maximizer is $(2, 1)$, not $(1, 1, 1)$**, and the q-pole order
is $11$, not the empirical AXKIA $18$.

This is a substantive finding: either

1. the $18$ in $D(u) = 2^{2A+1} \cdot u^{18Z + 21N + 1} \cdot (1+u^2)^{3A-1}$
   is the **u-pole** order, related to the q-pole order by a
   non-trivial substrate map $u \leftrightarrow q$ (e.g. $u = h = q - q^{-1}$
   gives $u \to \infty$ as $q \to 0$, so the q-pole structure does
   not lift cleanly to a u-pole structure of the same order), or
2. the $18$ refers to the **full atomic-braid Markov-trace
   denominator** $D(u)$, not the per-irrep $\chi^\lambda_q(\beta_p)$
   pole order.

The `prop:per-nucleon-shift-additive-linearity` derivation cites
the audit
[`crystal-r-matrix-sublemma-2-1.md`](2026-05-08-crystal-r-matrix-sublemma-2-1.md)
Step 5 as the source of the `18, 21` decomposition. That audit
attributes both constants to $\mathrm{ord}_{q=0}^{(-)} \chi^{\mu_p^*}(\beta_p)$
and $\mathrm{ord}_{q=0}^{(-)} \chi^{\nu_n^*}(\beta_n)$ respectively.
The H_3 computation above demonstrates that **`18` is not the
q-pole order at H_3** under the obvious reading.

**Open question:** which of the two interpretations is correct?
The right next step is to inspect the AXKIA commit `2f186ebc9`
linked in the original empirical input to see exactly what
quantity was numerically computed; reconcile the convention with
either (a) the substrate u-pole map, or (b) the full D(u) shift
exponent. The Path-A scaffold is now in place — the discrepancy
isolation reduces this from research-grade to a concrete reading
exercise.

## Original recommendation (preserved for reference)

Path A — the seminormal pole-order analysis. Pre-existing
infrastructure (`hoefsmit_symbolic`, `canonical_braid_crossings`)
makes it tractable. If the proton case yields `18` cleanly, the
neutron `21` follows.

A focused PR: `claude/per-irrep-pole-18-21` would extend
[`prop:per-nucleon-shift-additive-linearity`](../../content/quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md)
with a §"Categorical derivation of 18, 21" showing the seminormal
pole order matches the AXKIA empirical input. This closes the
"AXKIA inputs cited but not derived" gap explicitly.

## Out of scope for #572

This PR (#572) **does not** open Path A — the q-Hecke character
closure is a separate deliverable. The infrastructure landed in
#572 (`canonical_braid_crossings` + `wedderburn_jones_markov`)
makes Path A tractable in a follow-up; this audit doc captures
the open question + the path.

## Cross-references

- [`prop:per-nucleon-shift-additive-linearity`](../../content/quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md)
  — the master `shift(Z, N) = 18Z + 21N + 1` claim
- [`prop:alpha-shift-torus-knot`](../../content/quantum-observable-universe/braids-and-knots/alpha-shift-torus-knot.md)
  — proves $\alpha_{\mathrm{shift}}(T_{(p, k)}) = k(p - 1)$
- [`docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md`](2026-05-08-crystal-r-matrix-sublemma-2-1.md)
  — Step 5 explicitly cites `18, 21` as AXKIA inputs
- [`docs/audits/2026-05-08-q-hecke-character-gap-closure.md`](2026-05-08-q-hecke-character-gap-closure.md)
  — closure that makes Path A tractable
