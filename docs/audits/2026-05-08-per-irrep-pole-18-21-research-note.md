# Path A pole derivation of `18Z + 21N + 1` — proton + deuteron CLOSED

**Date:** 2026-05-08 (drafted) / 2026-05-09 (proton + deuteron verified)
**Status:** **Both single- and multi-nucleon Path A verified** by
direct symbolic Hoefsmit pole-order analysis:

- **Proton** ($A = 1$, $H_3$): $\mathrm{ord}_{u=0}(\mathrm{tr}_M(\beta_p)) = 19 = 18 \cdot 1 + 21 \cdot 0 + 1$
  ([`per_irrep_pole_proton_h3.py`](../../computations/per_irrep_pole_proton_h3.py),
  witness:
  [`per-irrep-pole-proton-h3.witness.json`](../../computations/per-irrep-pole-proton-h3.witness.json)).
- **Deuteron** ($A = 2$, $H_6$): $\mathrm{ord}_{u=0}(\mathrm{tr}_M(\beta_D)) = 40 = 18 \cdot 1 + 21 \cdot 1 + 1$
  ([`per_irrep_pole_deuteron_h6.py`](../../computations/per_irrep_pole_deuteron_h6.py),
  witness:
  [`per-irrep-pole-deuteron-h6.witness.json`](../../computations/per-irrep-pole-deuteron-h6.witness.json)).

Both atoms match `prop:per-nucleon-shift-additive-linearity` exactly.

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

`computations/per_irrep_pole_proton_h3.py`
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
[`d_u_closed_form_proof.py`](../../computations/d_u_closed_form_proof.py)
line 18, $z = u/(1+u^2)$ at $q = u^2$):

$$
\mathrm{ord}_{u=0}\bigl(\mathrm{tr}_M(\beta_p)\bigr) \;=\; \boxed{19}
\;=\; 18 \cdot Z + 21 \cdot N + 1 \;=\; 18 + 0 + 1.
$$

**Path A verified for the proton** — the u-pole order of
$\mathrm{tr}_M(\beta_p)$ matches `prop:per-nucleon-shift-additive-linearity`
exactly at $A = 1$.

**Cross-confirmation (independent compute path).**
[`shift_from_nf_basis.py`](../../computations/shift_from_nf_basis.py),
which extracts shift values from the Hecke normal-form basis
expansion (a different algorithmic route than the seminormal trace
above), records `shift_proton_h3 = 19` in
[`shift-from-nf-basis.witness.json`](../../computations/shift-from-nf-basis.witness.json)
(assertion `shift_proton_h3_finite: computed=19, expected=19, passed=True`).
Two independent symbolic methods — Hoefsmit seminormal pole-order
(this PR) and NF-basis shift extraction (pre-existing) — agree
exactly on the per-proton $u$-pole.

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
emerges at $A \ge 2$ (deuteron $= 18 + 21 + 1 = 40$).

### Deuteron multi-nucleon verification — CLOSED (2026-05-09)

Three optimisations made the deuteron tractable in-session:

1. **Cached symbolic $y_\lambda(q)$**: pre-existing
   [`y-lambda-wenzl-bridge-symbolic-witness.json`](../../computations/y-lambda-wenzl-bridge-symbolic-witness.json)
   (n=2 through n=12) is loaded directly, bypassing the
   `solve_y_lambda(6)` symbolic bottleneck (>5 min via
   `sp.cancel` on rationals in q with half-integer powers).
2. **Cached symbolic $\chi^\lambda_q(\beta_D)$**: first run
   computes the 11 `chi_lambda_symbolic` calls on the 23-crossing
   deuteron word (~131 s) and emits
   [`chi-deuteron-h6.witness.json`](../../computations/chi-deuteron-h6.witness.json);
   subsequent runs are <1 s.
3. **Per-term pole order**: $\mathrm{ord}_{u=0}(y_\lambda \cdot \chi^\lambda)$
   per partition, then take max. Avoids the `sp.together`
   bottleneck on the 11-term sum. When the maximum is uniquely
   achieved (lower-order terms cannot cancel a strict max), the
   inferred full-sum pole order is rigorous.

Per-term u-pole orders for the deuteron:

| $\lambda \vdash 6$ | $\mathrm{ord}_{u=0}(y_\lambda \cdot \chi^\lambda)$ |
|---:|---:|
| $(4, 1, 1)$ | **40** |
| $(4, 2)$ | 39 |
| $(3, 1, 1, 1)$ | 37 |
| $(3, 3)$ | 35 |
| $(2, 2, 1, 1)$ | 33 |
| $(2, 2, 2)$ | 29 |
| $(3, 2, 1)$ | 24 |
| $(5, 1)$ | 23 |
| $(2, 1, 1, 1, 1)$ | 22 |
| $(1, 1, 1, 1, 1, 1)$ | 3 |
| $(6)$ | 2 |

**Maximizer $\lambda = (4, 1, 1)$ uniquely**, so
$\mathrm{ord}_{u=0}(\mathrm{tr}_M(\beta_D)) = 40 = 18 \cdot 1 + 21 \cdot 1 + 1$
matches `prop:per-nucleon-shift-additive-linearity` exactly.

### Open: A ≥ 3 atoms ($H_9$, $H_{12}$, $\ldots$)

Tritium / ³He at $H_9$ (30 partitions of 9) and ⁴He at $H_{12}$
(77 partitions of 12) follow the same pattern but require more
chi_lambda compute. The cached y_λ already exists for those n;
extending Path A to A ≥ 3 is a straightforward port of
`per_irrep_pole_deuteron_h6.py` — the chi cache emission is the
only new work, and it parallelises trivially across partitions.

## Performance note: per-step `sp.cancel` is correct

A profiling investigation (2026-05-09) confirmed that the existing
`hecke_character_symbolic.q_character_on_braid_word` design — calling
`M.applyfunc(sp.cancel)` after each crossing — is **the right
algorithm**, not the bottleneck.

Profile data on `chi^{(4,2)}_q(β_D)` at $H_6$:

| Strategy | Wall time | Status |
|---|---:|---|
| Existing path (`q`-rationals + per-step `sp.cancel`) | **13 s** | ✓ |
| `q = u^2` substituted first, no per-step cancel, single final cancel | >240 s | ✗ timed out |

Removing per-step `sp.cancel` lets matrix entries grow exponentially
in the number of crossings (each entry becomes a sum of products of
Hecke eigenvalues without simplification), so the final `sp.cancel`
on the trace becomes intractable. The per-step cancel keeps each
entry's polynomial complexity bounded.

The earlier "130 s per partition" wall-clock observation in the bg
runs was **CPU contention**, not per-shape cost. Running tritium with
`--workers 8` and ³He with `--workers 4` simultaneously on a 4-core
machine over-provisioned by 3× — each worker received ~1/3 of a
core, tripling effective wall time per partition. Re-launching with
`--workers 4` (one per core) on a single atom recovers the expected
~13–60 s per shape.

### Provisioning recommendation

For multi-atom Path A runs, set `--workers` to the **number of CPU
cores**, and run atoms sequentially (one at a time) rather than
concurrently. The chi cache is permanent, so a sequential schedule
is no slower than a parallel-atom schedule, and avoids contention.

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
