# Q_β c₃ — KC19 ⇔ KC20 cross-consistency: same coordinate, disjoint singularities, joint exclusion

**Date:** 2026-07-11 · **Axis:** z→c_k f-map keystone (consistency of the two most-recent
narrowings) · **Tier:** symbolic-exact (sympy cross-check of two proved-lean constraints) ·
**No `c_k` value, no wiring, no tier change** (registry §8 flip-flop guard).

## Why this audit exists

Two independently-Lean-proved constraints landed on the Q_β c₃ bar-odd channel from
*different levels*:

- **KC19** ([#3473](https://github.com/litlfred/qou/pull/3473), `CrossingWeightAffine.lean`) —
  the **observable / eval-map** side: the archimedean evaluation `E(w)=h²/2−h·w` is affine, so
  the bar-odd ladder part is `K(q)·(w−w₀)` with the **anchor-rigid** kernel
  `K(q)=2h/(4w₀²−h²)`; the c₃ swing lives entirely in the crossing weight `w(q)`.
- **KC20** ([#3467](https://github.com/litlfred/qou/pull/3467), `QBetaZeta4ResidueRefutation.lean`) —
  the **fibre / 4₁-carrier** side: the bar-odd carrier `num=(q²−1)·R₁₂`, `R₁₂=q⁶·C(y)`,
  `C(y)=y³−4y²+3y−2` is a **degree-3 irreducible** cubic in `y=q²+q⁻²`, no quadratic anchor is
  a root ⇒ real-q/quadratic c₃ closures structurally excluded.

This audit is a formalize-first consistency cross-check of the two, not a closure attempt
(every discrete c₃ route is refuted, #3536/#3567; the surviving object is the analytic Φ_b
state-integral, worked on #3544/#3596).

> **Relation to the prior KC19×KC20 bridge (added 2026-07-12, corpus-grep correction).** A
> comprehensive KC19×KC20 reconciliation already exists —
> [`2026-07-07-hopf-cubic-vs-crossing-weight-shadow-bridge.md`](2026-07-07-hopf-cubic-vs-crossing-weight-shadow-bridge.md) —
> which this audit originally failed to cite. That bridge audit establishes the **shadow
> identity** `C_Hopf(2)=−2` (meaningful, `= J_Hopf(1)`), the **substrate rigidity** (`C_Hopf(y₀)`
> anchor-rigid ⇒ the c₃ swing is upstream in `w(q)`), and the **chirality-parity** table (even =
> unknot sector, disc `+17`, real; odd = Hopf sector, disc `−76`, complex/chiral). Read that
> audit for the substrate/chirality reconciliation. **What this audit adds that is genuinely new**
> and not in the bridge audit: (i) the exact identity **`4−h² = 6−y`** — KC19's eval-kernel
> denominator *is* KC20's carrier trace variable `y=q²+q⁻²` (§1); (ii) the **disjoint singular
> structure** — `K(q)`'s pole sits at the silver anchor `y=6` where the carrier is regular (§2).
> Section 4 below is **corrected** to distinguish the meaningful `C_Hopf(2)=−2` shadow from the
> separate coincidental total-`C(3)=−2` match (it originally discussed only the latter).

Probe [`qbeta_c3_kc19_kc20_consistency_probe.py`](../../computations/qbeta/qbeta_c3_kc19_kc20_consistency_probe.py)
→ [witness](../../computations/qbeta/qbeta-c3-kc19-kc20-consistency.witness.json) (5/5, sympy-exact).

## The four consistency facts

### 1. Same coordinate (the unstated bridge)

KC19's kernel denominator at the counit `w₀=1` is

`4w₀²−h² = 4−h² = 6−y`  exactly,  `y = q²+q⁻²`.

So KC19's eval kernel `K(q)=2h/(6−y)` and KC20's carrier `C(y)` are functions of the **same
bar-even trace variable** `y`. Neither audit states this; it is the structural reason both can
describe one channel.

### 2. Disjoint singular structure

`K(q)=2h/(6−y)` has its only pole at `y=6` (the **silver** anchor `1+√2`). The carrier is
regular there — `C(6)=88≠0` — and its real root is `y₀≈3.27`. So the eval map's singularity
and the carrier's degree-3 root are **disjoint**: the anchor-rigid evaluation contributes a
pole at silver, the fibre carrier its irreducible root elsewhere. Consistent, non-overlapping.

### 3. Joint (sharper) exclusion

Composing the three proved constraints —

- KC19: the c₃ swing lives in `w(q)` (eval map anchor-rigid);
- KC18 (the bridge): the carrier feeds `w` **affinely**;
- KC20: the carrier is degree-3 irreducible, no quadratic anchor —

gives the **unified** statement neither audit makes alone: `w(q)` (hence `c₃=[u³]w`) inherits
the degree-3 field, so **no quadratic / root-of-unity closed form for c₃ can exist**. KC20 §4
proves this exclusion at the *fibre carrier*; KC19 localizes the swing at the *observable*; the
affine bridge (KC18) joins them into one statement about `c₃` itself. The two constraints are
mutually consistent, and jointly stronger than either alone.

### 4. The *total*-`C(3)=−2` numerology is a wrong-anchor coincidence — but the *Hopf-sector* shadow `C_Hopf(2)=−2` is meaningful

> **Correction / cross-reference (2026-07-12).** This section, as originally written, addressed
> only the **total** carrier `C` and did not cite the pre-existing comprehensive KC19×KC20
> bridge audit
> [`2026-07-07-hopf-cubic-vs-crossing-weight-shadow-bridge.md`](2026-07-07-hopf-cubic-vs-crossing-weight-shadow-bridge.md)
> (a corpus-grep miss on my part). That audit establishes the **physically meaningful** shadow
> identity, which must **not** be conflated with the coincidence below. See the two-row split.

There are **two distinct** `−2`'s at play; keeping them separate is the point:

- **Meaningful (NOT a coincidence): `C_Hopf(2) = −2` at the classical anchor `y=2`.** The
  Hopf-sector cubic evaluated at the q=1 trace point equals the Hopf-link classical Jones
  `J_Hopf(1) = −2`, which **is** the known c₃→−2 q=1 shadow (KC10). This is the *right anchor*
  (`y=2` = q=1) and the *right object* (the Hopf sector, which KC20 §5 attributes the odd
  channel to). It is Lean-certified in the bridge audit — a carrier-side confirmation, not
  numerology.
- **Coincidental: total `C(3) = −2` at the golden anchor `y=3`.** This is the match KC20 §4
  flagged as numerology. Under the KC19 `y`-bridge the c₃ q=1 shadow lives at `y(q→1)=2`, where
  the **total** `C(2)=−4`, not `−2`; the total-`C` value `−2` only appears at the golden anchor
  `y=3`, a *different* point. So matching the shadow *value* via the *total* `C` requires the
  *wrong* anchor — the coincidence does not survive placing it at `y=2`. This confirms and
  sharpens KC20 §4's "coincidence" call (agrees, does not contradict).

| object | anchor | `y` | value | status |
|---|---|---|---|---|
| **`C_Hopf`** | q=1 (classical) | 2 | **−2** | **meaningful** — `= J_Hopf(1)` = c₃ shadow (bridge audit, Lean-certified) |
| total `C` | q=1 (classical) | 2 | −4 | the anchor that matches c₃'s q=1 shadow — total ≠ −2 here |
| total `C` | golden `φ` | 3 | −2 | KC20 §4 numerology: value matches, but **wrong anchor** |
| total `C` | silver `1+√2` | 6 | 88 | KC19's eval-kernel pole (disjoint from carrier) |

The lesson: the `−2`/c₃ connection is **not** globally coincidental — it is the meaningful
`C_Hopf(2)=−2` classical shadow. What *is* coincidental is the separate total-`C`-at-golden
match. My original section 4 debunked the latter without citing the former; both facts stand,
and they are about different (sector, anchor) pairs.

## What this buys, and what it does not

- **Buys:** confirmation that the two most-recent Lean-proved c₃ narrowings are **coherent**
  (same variable, disjoint singularities), a **unified** real-q/quadratic exclusion stronger
  than either alone, and the **closure of a flagged numerology**.
- **Does not buy:** a c₃ value or closure. The surviving open object is unchanged — the
  analytic Φ_b state-integral face at real q₀ (#3544/#3596). Any closure must supply the
  **cubic field of `C_Hopf`** (disc `−76`, the Hopf-sector `S₃` object) routed through the
  archimedean evaluation (KC18/KC19), not a quadratic anchor. Nothing wired; no tier change.

## Cross-references

- **Prior KC19×KC20 bridge (substrate rigidity + chirality parity):** [`2026-07-07-hopf-cubic-vs-crossing-weight-shadow-bridge.md`](2026-07-07-hopf-cubic-vs-crossing-weight-shadow-bridge.md)
- KC19 (affine eval map): [`2026-07-07-qbeta-crossing-weight-affine-narrowing.md`](2026-07-07-qbeta-crossing-weight-affine-narrowing.md)
- KC20 (degree-3 carrier): [`2026-07-07-zeta4-residue-lean-certificate-and-surviving-cubic.md`](2026-07-07-zeta4-residue-lean-certificate-and-surviving-cubic.md)
- KC18 (the affine bridge): [`2026-07-07-z-ck-fmap-eval-map-bar-decomposition.md`](2026-07-07-z-ck-fmap-eval-map-bar-decomposition.md)
- Registry: [`ck-dk-canonical-registry.md §9`](../coordination/ck-dk-canonical-registry.md) (KC18/KC19/KC20)
- Canonical framing (flip-flop guard): [`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
