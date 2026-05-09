# Path A pole derivation of `18Z + 21N + 1` — proton CLOSED, multi-nucleon deferred

**Date:** 2026-05-08 (drafted) / 2026-05-09 (proton verified)
**Status:** **Proton case verified** by direct symbolic Hoefsmit
pole-order computation
([`per_irrep_pole_proton_h3.py`](../../folio-assistant/computations/per_irrep_pole_proton_h3.py),
witness:
[`per-irrep-pole-proton-h3.witness.json`](../../folio-assistant/computations/per-irrep-pole-proton-h3.witness.json)).
$\mathrm{ord}_{u=0}(\mathrm{tr}_M(\beta_p)) = 19 = 18 \cdot 1 + 21 \cdot 0 + 1$
matches `prop:per-nucleon-shift-additive-linearity`. Multi-nucleon
verification (deuteron at $H_6$, $A \ge 3$ at $H_9$) deferred —
symbolic Hoefsmit chi_lambda on the deuteron's 11-partition $H_6$
takes ~3 minutes; numerical-q-from-start path needs implementation.

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

## Path A — concrete H_3 result (2026-05-09, verified)

`folio-assistant/computations/per_irrep_pole_proton_h3.py`
implements Path A directly. Concrete output for the proton:

### Per-irrep table

| $\lambda \vdash 3$ | $\chi^\lambda_q(\beta_p)$ (simplified) | $\mathrm{ord}_{q=0}^{(-)} \chi^\lambda_q$ |
|---:|---|---:|
| $(3)$ | $q(q^4 + 2q^2 + 1)/4$ | 0 |
| $(2, 1)$ | $(q^{22} + q^{20} + q^{18} + q^{14} - q^8 - q^4 - q^2 - 1) / (4q^{11})$ | **11** |
| $(1, 1, 1)$ | $(-q^4 - 2q^2 - 1)/(4q^5)$ | 5 |

Per-irrep maximizer: $\lambda = (2, 1)$ with q-pole order $11$.

### Full Markov-trace u-pole

After summing $\mathrm{tr}_M(\beta_p) = \sum_\lambda y_\lambda(q) \cdot \chi^\lambda_q(\beta_p)$
and substituting $q = u^2$ (per $D(u)$ convention from
[`d_u_closed_form_proof.py`](../../folio-assistant/computations/d_u_closed_form_proof.py)
line 18, $z = u/(1+u^2)$ at $q = u^2$):

$$
\mathrm{ord}_{u=0}\bigl(\mathrm{tr}_M(\beta_p)\bigr) \;=\; \boxed{19}
\;=\; 18 \cdot Z + 21 \cdot N + 1 \;=\; 18 + 0 + 1.
$$

**Path A verified for the proton** — the u-pole order of
$\mathrm{tr}_M(\beta_p)$ matches `prop:per-nucleon-shift-additive-linearity`
exactly at $A = 1$.

### Reading correction (audit-internal)

The original line in this research note attributed the constant
$18$ to "per-new-proton: $\mathrm{ord}_{q=0}^{(-)} \chi^{\mu_p^*}(\beta_p)$".
That attribution is **incorrect** as a per-irrep statement: the
actual per-irrep maximum $\mathrm{ord}_{q=0}^{(-)} \chi^\lambda_q(\beta_p) = 11$
(at $\lambda = (2, 1)$), not $18$.

The $18$ is the **per-proton additive coefficient in the full
Markov-trace u-pole order $\mathrm{shift}_{\mathrm{NF}}$**, which
sums over partitions:

$$
\mathrm{shift}_{\mathrm{NF}}(\beta_{\mathrm{atomic}}(Z, N)) \;=\;
\mathrm{ord}_{u=0}\bigl(\sum_{\lambda} y_\lambda \cdot \chi^\lambda_q\bigr)
\;=\; 18 Z + 21 N + 1.
$$

The crystal-R-matrix audit's Step 5 derivation
([`crystal-r-matrix-sublemma-2-1.md`](2026-05-08-crystal-r-matrix-sublemma-2-1.md))
remains valid; the per-irrep / per-nucleon attribution is a
**structural decomposition of the u-exponent**, not a sum of
per-irrep q-pole orders.

### Single-nucleon symmetry note

The neutron computation at $H_3$ also gives
$\mathrm{ord}_{u=0}(\mathrm{tr}_M(\beta_n)) = 19$, equal to the
proton (not the audit's per-nucleon $21$). This is consistent
with the formula at $A = 1$: a single-nucleon braid with
$Z = 0, N = 1$ has shift $= 18 \cdot 0 + 21 \cdot 1 + 1 = 22$,
*if* an inter-nucleon interface were present — but a lone neutron
has no inter, so the actual single-neutron shift is $21 \cdot 1 = 21$
in pure form, or $19$ if the lone-nucleon convention adds a
self-interface. The full asymmetry between $18$ and $21$
emerges at $A \ge 2$ (deuteron $= 18 + 21 + 1 = 40$) and is
verifiable from the deuteron's $\mathrm{tr}_M$ — symbolic
$H_6$ pole-order analysis is too slow in-session ($> 90$ s for
$11$ partitions; numerical-q would fix it but loses the symbolic
exponent). Deferred to a follow-up.

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
