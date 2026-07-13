# The S₃-equivariant link-level EM coupling functional on L6a4: defined; S2 closed (the 1/3 multiplicity is derived), S3 re-scoped to one scalar — still open

**Date:** 2026-07-13 · **Branch:** `claude/mass-binding-errors-9zqpal` ·
**Type:** FINDING (reproducible, no fit). The S3 attack requested by
[`2026-07-13-mirror-split-one-third-mechanism-probe.md`](2026-07-13-mirror-split-one-third-mechanism-probe.md)
§"What would close it": define the link-level EM coupling functional (its item 1),
attempt to derive its magnitude (item 2). Outcome: **item 1 done — the functional
is defined and its S₃-equivariance derives the equal 1/3 per-pair-channel weight,
closing S2. Item 2 is not closed** — everything structural reduces the freedom to
**one scalar** κ, whose near-match value 1/3 rests on an underived
"unit-capacity sum rule" and would have to supersede the derived pairwise
`tanh(ln q₀)`.

Probe: [`computations/deltalambda/mirror_split_s3_em_functional_probe.py`](../../computations/deltalambda/mirror_split_s3_em_functional_probe.py)
(witness [`mirror-split-s3-em-functional.witness.json`](../../computations/deltalambda/mirror-split-s3-em-functional.witness.json),
5/5 assertions pass, mpmath at the production floor, exit 0).

## Corpus-grep results consumed first (nothing here was open-declared blind)

- **Cusp-geometry route (candidate b): already scope-(b) excluded** as a
  magnitude source —
  [`2026-07-04-em-linking-cusp-geometry-excluded.md`](2026-07-04-em-linking-cusp-geometry-excluded.md):
  L6a4's three cusps are geometrically **identical** (shape `2i`, meridian `√2`,
  longitude `2√2`; SnapPy-verified), so within-link cusp data carry no
  proton-vs-neutron distinction; cross-link (8_11 vs L6a4) ratios miss the
  3.213× gate (best 4.3%). **Reused here with the sign flipped:** the very
  S₃ symmetry that kills the cusp *magnitude* route is the *premise* the
  equivariance derivation needs. Exact geometric data in corpus: complement =
  two ideal regular octahedra, `Vol(L6a4) = 8G` (Catalan) —
  [`2026-06-16-he4-magic-8G-is-borromean-volume-derived.md`](2026-06-16-he4-magic-8G-is-borromean-volume-derived.md);
  cusp shapes baked in
  [`em-linking-cusp-geometry-probe.witness.json`](../../computations/em-linking-cusp-geometry-probe.witness.json).
- **Flavor cannot reach cusp holonomy**
  ([`2026-06-01-flavor-dependent-cusp-shape.md`](2026-06-01-flavor-dependent-cusp-shape.md)) —
  consistent: this construction puts the charge asymmetry in the **labels**
  (`q_i q_j`), not the geometry.
- **μ̄-as-length-scale a-priori exclusion** (2026-07-04: "μ̄ is dimensionless,
  the gap is dimensionful") does **not** apply here: the magnitude below is a
  dimensionless coefficient in `B_pp` units, not a length scale. μ̄ serves as
  topological support only.
- Milnor machinery: the validated integer-Magnus `mu()` of
  [`binding_mn_milnor_linking.py`](../../computations/binding_mn_milnor_linking.py)
  (imported, not re-derived).

## The functional (definition)

$$E(L, c) \;=\; \sum_{i<j} w_{ij}(L)\, q_i q_j$$

for a 3-component link $L$ with charge labeling $c = (q_1,q_2,q_3)$, with axioms:

| axiom | statement | justification |
|---|---|---|
| **A1** | bilinear in charges, **no self-term** $a\sum q_i^2$ | **derived**, not assumed: per-component EM self-energy lives in the free-nucleon masses $m_p, m_n$, and binding $B = Z m_p + N m_n - M$ subtracts them identically. Self-terms cancel in $B$ by definition. |
| **A2** | S₃-equivariance: $E(g\cdot L, g\cdot c) = E(L,c)$ | component relabeling is a gauge choice (functoriality) |
| **A3** | topological support: $w_{ij}(L)$ is built from link invariants of $L$ | for L6a4 all pairwise $\mathrm{lk}_{ij}=0$ (S1, proved exact), so a nonzero $w_{ij}$ is mediated by the first non-vanishing invariant $\bar\mu(123)=\pm 1$ — the triple channel, consistent with S1 |

## Derived consequences

**D1 — equal weights (S2 CLOSED).** $\mathrm{Sym}(L6a4) \supseteq S_3$ acts
transitively on components (geometric fact, SnapPy-verified identical cusps).
A2 with $g \in \mathrm{Sym}(L)$ gives $w_{g(i)g(j)} = w_{ij}$; transitivity on
unordered pairs forces $w_{12}=w_{13}=w_{23}=:w$. Hence, exactly:

- $E(^3\mathrm{He}, (1,1,0)) = w\cdot(1{+}0{+}0) = w$;
- $E(^3\mathrm{H}, (1,0,0)) = 0$ **for any link** (every pair product vanishes —
  that ³H's link is 8_11 rather than Borromean is immaterial);
- predicted split $= w$; and in orbit-average form $E = 3w\,\langle q_iq_j\rangle$
  with $\langle q_iq_j\rangle_{^3\mathrm{He}} = 1/3$ exactly. **The equal 1/3
  per-pair-channel multiplicity is derived** — the object the predecessor audit's
  S2 was conditional on now exists.

**D2 — sign-representation obstruction (new).** Verified exactly (integer
Magnus, all 6 permutations): $\bar\mu(g(1)g(2)g(3)) = \mathrm{sgn}(g)\cdot\bar\mu(123)$
— **μ̄ spans the sign rep of S₃.** The pair-channel space $\mathbb{R}^3$
decomposes as trivial ⊕ standard; the sign rep does not occur, so by Schur's
lemma any equivariant coupling **linear in μ̄** to the charge bilinear vanishes
identically. The coupling must enter through $|\bar\mu|$ (equivalently
$\bar\mu^2$). Consequences: (i) the functional is **mirror-insensitive** (the
mirror of L6a4 has $\bar\mu = -1$, same $E$) — the EM split does not see link
chirality; (ii) the sign of the effect comes from the charge bilinear alone
(repulsive: reduces ³He binding). This obstruction was not in the predecessor
audits.

**D3 — the magnitude (S3, re-scoped, NOT closed).** A1–A3 + D1 + D2 fix the
functional up to **one scalar**: $w = \kappa\cdot|\bar\mu(123)|\cdot B_{pp}$.

## Numbers (probe output; nothing hardcoded, nothing tuned)

| quantity | value | provenance |
|---|---|---|
| $B_{pp}$ (per-block H₆ diproton) | 2.286088 MeV | imported from the predecessor probe's exact code path ([`mirror_split_milnor_one_third_probe.per_block`](../../computations/deltalambda/mirror_split_milnor_one_third_probe.py), itself the `charge_coulomb_tn3he_derived.py` path) |
| AME split $B(^3\mathrm{H})-B(^3\mathrm{He})$ | 0.763755 MeV | AME2020 via `codata_constants` |
| **N1** prediction ($\kappa = 1/3$, unit-capacity sum rule) | **0.762029 MeV** | **error vs AME: −0.226%** |
| **N2** prediction ($\kappa = \tanh(\ln q_0) = 0.103964$, derived pairwise coefficient) | 0.237670 MeV unshared (31.1%); 0.079223 MeV shared (10.4%) | `def:coulomb-charge` |
| N1 + N2 coverage if additive | 130.9% | **competing, not additive** |

**N1, stated precisely.** "The link carries $|\bar\mu| = 1$ unit of topological
coupling capacity in strong-bond units, shared over the 3 equal channels:
$\sum_{i<j} w_{ij} = |\bar\mu|\cdot B_{pp}$, hence $\kappa = 1/3$." Anchor
consistency: the Hopf/diproton $M_2$ unit ($\mathrm{lk}=1$, one pair channel)
gives $w = B_{pp}$ — exactly the per-block bond. **But the $M_2$ anchor cannot
distinguish the sum rule from per-channel normalization** (they differ only at
$n\ge 3$), so the sum rule is **underived**; and the deeper sub-step — why the
*strong* per-block bond $B_{pp}$ sets the EM channel unit at coefficient 1
rather than the *derived* pairwise Coulomb/strong ratio $\tanh(\ln q_0)$ — is
exactly the predecessor's S3 gate, unchanged. This is where laundering would
happen, and it is not done here.

**The tanh tension, addressed explicitly (replaces vs coexists).** N1 and the
derived tanh route are **competing** (sum 130.9% > 100%); a closure via N1 must
**replace** $\tanh(\ln q_0)$ at the triple channel — i.e. show that the
μ̄-mediated coupling is not a Coulomb *crossing insertion* (which carries the
per-crossing ratio $\tanh(\ln q_0) = (q_0-q_0^{-1})/(q_0+q_0^{-1})$ from
`def:coulomb-charge`) but a charge-gated full strong channel. No such
derivation exists; conversely, transplanting the derived tanh coefficient into
this functional gives 31.1% (unshared) or 10.4% (capacity-shared) — the
derived coefficient with the wrong magnitude at the triple channel. They
cannot both stand; **this audit resolves neither in favor of the other.**

## Classification (anti-fit discipline, STRICT)

**(ii) PARTIAL — S2 closed, S3 open and re-scoped to one scalar.**

- **Derived, each step cited:** the functional form with $a=0$ (definition of
  binding energy); equal per-pair weights $w_{ij}\equiv w$ (S₃ equivariance +
  transitivity of $\mathrm{Sym}(L6a4)$, SnapPy-verified) — **S2 of
  [`2026-07-13-mirror-split-one-third-mechanism-probe.md`](2026-07-13-mirror-split-one-third-mechanism-probe.md)
  is closed**; support through $|\bar\mu|$ only (sign-rep Schur obstruction,
  D2, new); $E(^3\mathrm{H}) = 0$ independent of the ³H link.
- **Not derived (scope-(a) phrasing):** the unit-capacity sum rule, *alone,
  as stated*, does not derive $\kappa = 1/3$ — the $M_2$ anchor cannot separate
  it from the per-channel alternative ($\kappa = 1$, which would overshoot the
  split 3×), and the $B_{pp}$-unit-at-coefficient-1 step remains the same open
  gate as before, now sharpened: **the entire remaining freedom of the
  triple-channel EM coupling is one number** $\kappa$, with the guarded datum
  $\kappa_{\mathrm{AME}} = \mathrm{split}/B_{pp} = 0.334088$.
- Nothing was tuned to 0.7638 MeV; the −0.226% is the same guarded near-match
  as the predecessor's datum, now attached to a defined functional rather than
  a bare ratio. Not derived ⇒ not wired: no production change, no tier change,
  no content-block edit.

## What would close S3 (for the next agent)

1. **Derive the sum rule** $\sum_{i<j} w_{ij} = |\bar\mu|\cdot(\text{unit})$
   from the Massey-product / lower-central-series structure (one μ̄ invariant =
   one channel of capacity), *or* find an independent anchor where sum-rule and
   per-channel normalizations differ and the corpus already fixes the answer —
   e.g. an A=4 link with two EM-active pairs among $\binom{4}{2}=6$ channels
   (⁴He charge bilinear = 1, same as ³He: the per-isotope $\mathcal{B}_K$ link
   assignment is the model input gating this test).
2. **Derive the unit**: show the triple-channel coupling is charge-gated strong
   bonding (coefficient 1 on $B_{pp}$) rather than a Coulomb crossing insertion
   (coefficient $\tanh(\ln q_0)$) — this must simultaneously explain why the
   derived pairwise tanh is superseded at the triple channel. Until then the
   31%-vs-99.8% tension stands as recorded.
3. The numerology-guard items ($\tanh(\ln\sqrt2) = 1/3$ exactly, $\sqrt2 = 1/x^*$)
   remain guarded, unchanged from the predecessor audit.

## Files

- probe: [`computations/deltalambda/mirror_split_s3_em_functional_probe.py`](../../computations/deltalambda/mirror_split_s3_em_functional_probe.py) (new)
- witness: [`computations/deltalambda/mirror-split-s3-em-functional.witness.json`](../../computations/deltalambda/mirror-split-s3-em-functional.witness.json) (new, audit-only, 5/5 pass)
- this audit: `docs/audits/2026-07-13-mirror-split-s3-em-functional-attempt.md`
- context consumed (unchanged):
  [`2026-07-13-mirror-split-one-third-mechanism-probe.md`](2026-07-13-mirror-split-one-third-mechanism-probe.md),
  [`2026-07-13-a3-split-borromean-redirect-and-deuteron-coupling.md`](2026-07-13-a3-split-borromean-redirect-and-deuteron-coupling.md),
  [`2026-06-03-charge-coulomb-tn3he-derived.md`](2026-06-03-charge-coulomb-tn3he-derived.md),
  [`2026-07-04-em-linking-cusp-geometry-excluded.md`](2026-07-04-em-linking-cusp-geometry-excluded.md),
  [`2026-06-01-flavor-dependent-cusp-shape.md`](2026-06-01-flavor-dependent-cusp-shape.md),
  [`computations/binding_mn_milnor_linking.py`](../../computations/binding_mn_milnor_linking.py),
  [`computations/deltalambda/mirror_split_milnor_one_third_probe.py`](../../computations/deltalambda/mirror_split_milnor_one_third_probe.py),
  [`computations/em_linking_cusp_geometry_probe.py`](../../computations/em_linking_cusp_geometry_probe.py)
