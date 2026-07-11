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

Nobody had checked that these two describe the **same** bar-odd object consistently. This
audit does — a formalize-first consistency cross-check, not a closure attempt (every discrete
c₃ route is refuted, #3536/#3567; the surviving object is the analytic Φ_b state-integral,
worked on #3544/#3596).

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

### 4. The `C(3)=−2` numerology is a wrong-anchor coincidence

KC20 §4 flags (numerology, not wired) that `C(3)=−2` matches the `c₃→−2` q=1 shadow. Under the
KC19 `y`-bridge, the c₃ q=1 shadow lives at `y(q→1)=q²+q⁻²→2`, where **`C(2)=−4`, not `−2`**.
The `−2` appears at `C(3)` — the **golden** anchor `y=3` — a *different* point. Matching the
shadow *value* requires the *wrong* anchor. So the coincidence does not survive placing it at
the anchor that actually corresponds to the q=1 shadow — confirming and sharpening the corpus
flag (this **agrees** with KC20 §4's "coincidence" call; it does not contradict it).

| anchor | `y=q²+q⁻²` | `C(y)` | note |
|---|---|---|---|
| golden `φ` | 3 | **−2** | the flagged coincidence (value matches, anchor wrong) |
| q=1 shadow | 2 | **−4** | the anchor that *actually* matches c₃'s q=1 shadow |
| silver `1+√2` | 6 | 88 | KC19's eval-kernel pole (disjoint from carrier) |

## What this buys, and what it does not

- **Buys:** confirmation that the two most-recent Lean-proved c₃ narrowings are **coherent**
  (same variable, disjoint singularities), a **unified** real-q/quadratic exclusion stronger
  than either alone, and the **closure of a flagged numerology**.
- **Does not buy:** a c₃ value or closure. The surviving open object is unchanged — the
  analytic Φ_b state-integral face at real q₀ (#3544/#3596). Any closure must supply the
  **cubic field of `C_Hopf`** (disc `−76`, the Hopf-sector `S₃` object) routed through the
  archimedean evaluation (KC18/KC19), not a quadratic anchor. Nothing wired; no tier change.

## Cross-references

- KC19 (affine eval map): [`2026-07-07-qbeta-crossing-weight-affine-narrowing.md`](2026-07-07-qbeta-crossing-weight-affine-narrowing.md)
- KC20 (degree-3 carrier): [`2026-07-07-zeta4-residue-lean-certificate-and-surviving-cubic.md`](2026-07-07-zeta4-residue-lean-certificate-and-surviving-cubic.md)
- KC18 (the affine bridge): [`2026-07-07-z-ck-fmap-eval-map-bar-decomposition.md`](2026-07-07-z-ck-fmap-eval-map-bar-decomposition.md)
- Registry: [`ck-dk-canonical-registry.md §9`](../coordination/ck-dk-canonical-registry.md) (KC18/KC19/KC20)
- Canonical framing (flip-flop guard): [`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
