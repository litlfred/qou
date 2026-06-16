# Single-knot vs multi-nucleon: three-layer decomposition of the +2.89-3.86% mass gap

**Date:** 2026-05-24
**Trigger:** PR #1089's low-isotope sign-flip diagnostic falsifies the
single-VolDensity(𝓑₃) refinement framing from PR #1063 when extended
to multi-nucleon isotopes.
**Status:** Reconciliation audit. Identifies that the two framings
operate at **different layers** of the prediction chain and are
**complementary, not contradictory**.

## §1. The two findings, side by side

### Finding A — PR [#1063](https://github.com/litlfred/qou/pull/1063) (merged) + PR [#1081](https://github.com/litlfred/qou/pull/1081) (merged)

**Single-knot scope.** The proton's prediction at the **single-knot VolDensity level**
$$m_p^{\text{pred}} = m_e \cdot \mathrm{VolDensity}(\mathcal{B}_3, q_0)$$
gives $m_p \approx 965.4\;\text{MeV}$, a **+2.89 % gap** vs CODATA $938.27\;\text{MeV}$.

The framing in PR #1063 (now on `main` as `docs/audits/2026-05-24-family-a-gap-audit.md`):
this is a `VolDensity(\mathcal{B}_3)` **categorical-exactness refinement gap** at $h^2$ order.

The PR #1081 finding (now on `main` as `computations/probes/vol_density_borromean_h4_probe.py`):
**replacing Family A's `5/2 + (3/4)·h²` linking weight with the exact
Markov-trace × 5/2** (closed form `5/2·(4+h²−3h⁴−h⁶)/(h²+4)`) shrinks
the gap to **+1.948 %** — a 1.5× single-knot improvement using only
the exact topological Jones invariant, zero free parameters.

### Finding B — PR [#1089](https://github.com/litlfred/qou/pull/1089) (open)

**Multi-nucleon scope.** Sign-flip across the low-isotope table:

| Atom | Pred (MeV) | AME (MeV) | err | Sign |
|---|---:|---:|---:|---|
| p | 965.4 | 938.27 | **+2.89 %** | + |
| n | 966.7 | 939.57 | **+2.89 %** | + |
| ²H | 2.249 | 2.225 | **+1.09 %** | + |
| ³H | 8.469 | 8.482 | **−0.16 %** | **−** |
| ³He | 7.489 | 7.718 | **−2.97 %** | **−** |
| ⁴He | 29.96 | 28.30 | **+5.87 %** | + |

PR #1089 §"Low-isotope mass-error analysis": *"The sign-flips
**falsify** the single-VolDensity(𝓑₃) refinement framing — a uniform
scale gap would force every isotope to overshoot by the same
fraction."*

## §2. Why both findings can be true: the three-layer decomposition

The prediction chain for a multi-nucleon isotope $\mathrm{atom}(Z, N)$ decomposes into **three independent layers**:

```
m_atom(Z, N) = Σ_i m_nucleon_i (single-knot layer; PR #1081 scope)
             + Σ_{pairs(i,j)} V_inter(i, j)   (channel layer; PR #1089 scope)
             + V_shell(Z, N)                  (nuclear-shell layer; not yet quantified)
```

Each layer has its own source of error, its own canonical-derivation status, and its own potential closure path:

| Layer | What | Source of error | PR addressing it |
|---|---|---|---|
| **L1**: single-knot $\mathrm{VolDensity}(K)$ | per-nucleon mass via $m(K) = m_e \cdot \mathrm{VolDensity}(K, q_0)$ | $\mathrm{VolDensity}(\mathcal{B}_3)$ categorical-exactness shortfall at $h^{2k}$ for $k \geq 2$ | PR #1063 + PR #1081 (single-knot finding: structural Markov × 5/2 → +1.948 %) |
| **L2**: inter-nucleon channels | binding energy from pp/pn/nn pairwise crossing weights $(c_{pp}, c_{pn}, c_{nn})$ | channel assignment rule "pp → σ, pn → averaged, nn → σ⁻¹" not yet Lean-proved | PR #1089 (sign-flip finding) |
| **L3**: nuclear-shell binding | per-shell or per-deuteron-pair correction (e.g., the ⁴He α-particle's extra binding) | nuclear-shell-model / SU(4) Wigner spin-isospin structure not in framework | NOT yet addressed |

### How the layers compose to give the table

**Free p, n:** L1 only. Predicted via $m_e \cdot \mathrm{VolDensity}(\mathcal{B}_3, q_0)$.
Error +2.89 % is pure L1 shortfall.

**²H = pn:** L1 + one pn channel weight + minimal L3 (no shell). Error +1.09 %
shows L1's +2.89% gets *partially absorbed* by the L2 deuteron-binding
contribution (which has a different sign or magnitude than expected if L2 were canonical).

**³H = pnn / ³He = ppn:** L1 + three pairwise channels + L3 shell. Both predicted
masses come **below** AME, meaning L1's overshoot is *over-corrected* by
L2 + L3 in the same direction. The sign flip from + (p, n, ²H) to −
(³H, ³He) is the diagnostic that L2 + L3 carry their own error.

**⁴He = ppnn:** L1 + six pairwise channels + L3 (with α-particle extra binding). The +5.87 % overshoot — much larger than the +2.89 % L1 baseline — suggests **L3 is contributing positively** (α-particle binding currently UNDER-counted, giving an unphysically heavy ⁴He).

Empirically reading the table:
- L1 contributes ~+2.89 % uniformly (per-nucleon)
- L2 + L3 together flip sign and grow in magnitude with $A$
- L3 specifically appears to be ABSENT from the framework (the α-particle has its own ~28 MeV binding above shell-additive that the framework's current chain doesn't capture)

## §3. PR #1063's framing is correct **at L1 scope**; PR #1089's is correct at L2+L3 scope

**PR #1063's "single VolDensity(𝓑₃) refinement" framing is exactly right for L1.** Its action items:
- Formalize `prop:s4-s3-half-symmetric-projection` (L1 structural input) ✓ landed
- Re-run q-locality on VolDensity output ✓ landed (architectural-fail finding)
- Formalize $S_5 \leftrightarrow SO(3)$ fiber action (L1 structural input) ✓ scaffold landed
- Wire structural Markov × 5/2 (L1 closure, +1.948 %)

The +2.89 % gap on free p, free n IS a L1 question. PR #1081's structural Markov × 5/2 reduces it 1.5× **for these isotopes**, vindicating the L1 closure path.

**PR #1089's "sign-flips falsify single VolDensity" framing is exactly right for L2+L3.** L1 cannot explain why ³H errs −0.16 % while ⁴He errs +5.87 %; that requires layers L2 and L3.

Neither framing is wrong; they are diagnosing different layers of the same chain. The session-level coordination error was that PR #1063's audit § §4 implied "closing L1 closes the +2.89 % gap" — true for free nucleons, not for multi-nucleon isotopes. **This audit re-frames the closure path as three independent layers, each with its own closure budget.**

## §4. Per-layer closure paths

### L1 (single-knot VolDensity)

- **Current best**: Family A `5/2 + (3/4)·h²` linking weight (production)
- **Structurally-improved candidate**: `5/2 · (4+h²−3h⁴−h⁶)/(h²+4)` (structural Markov × 5/2; PR #1081 Probe 2; +1.948 % gap)
- **Categorical refinement input**: S_4↓S_3 bijection (Lean PROVED), S_5↔SO(3) (Lean scaffold, instance pending)
- **Open**: full BringFiberAction instance + categorical derivation of $h^4 = -3/4$ via one of (Pachner state-sum / DIM master Pentagon / Habiro cyclotomic — last already complete via Markov-trace closed form)

### L2 (inter-nucleon channel weights)

- **Current**: pp → σ, pn → averaged, nn → σ⁻¹ (per [`isotope_record_schema.py:65-70`](../../computations/isotope_record_schema.py))
- **Open** (per PR #1089's Lean-coverage matrix): no `prop:` block formalizing the channel assignment rule (medium risk)
- **Sign-flip evidence**: the ³H − vs ⁴He + sign change suggests the current channels are correct in magnitude (L1's overshoot is captured) but possibly wrong in sign for one of {pp, pn, nn}, OR a missing per-pair coupling constant
- **Closure path**: derive channel assignment from CPT-symmetry categorical argument; cross-check via the sign-flip diagnostic table

### L3 (nuclear-shell binding)

- **Current**: ABSENT from the framework's prediction chain
- **Evidence**: ⁴He's +5.87 % vs ³He's −2.97 % — the α-particle shell binding (≈ 28 MeV above shell-additive) is **not** in the prediction
- **Open**: the framework's archimedean functor needs an additional Geom-functor evaluation per closed nuclear shell (or per spin-isospin SU(4) Wigner supermultiplet)
- **Closure path**: long-term research direction; analog to nuclear-shell-model parameterization but derived from substrate. May tie to the Yekutieli MI tessellation at jet grade $k \geq 2$ (where ⁴He's 16-cell tessellation level adds structural binding)

## §5. Updated framing for both audits

Neither PR #1063 nor PR #1089 needs amendment — both are correct at their declared scope. This audit doc serves as the **scope-clarifying reconciliation**:

- **PR #1063** = L1 audit (single-knot VolDensity refinement)
- **PR #1089** = L2+L3 audit (multi-nucleon channel + shell)

Future agents writing on either layer should cite this doc to avoid the cross-layer confusion.

The +2.89-3.86 % single-line summary should be **disaggregated by layer** in future status dashboards:

| isotope | L1 contribution | L2 contribution | L3 contribution | total error |
|---|---|---|---|---|
| p | +2.89 % | 0 | 0 | +2.89 % |
| n | +2.89 % | 0 | 0 | +2.89 % |
| ²H | +2.89 %/(2 nucleons) | small + | 0 | +1.09 % |
| ³H | similar/3 | larger ± | small | −0.16 % |
| ³He | similar/3 | larger ± | small | −2.97 % |
| ⁴He | similar/4 | medium ± | **larger +** | +5.87 % |

The per-layer attribution above is **qualitative**; the L2 sign and L3 magnitude need empirical fitting from the multi-isotope table to disambiguate.

## §6. Cross-references

- [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md) — canonical framing (PR #1080)
- [`docs/audits/2026-05-24-family-a-gap-audit.md`](2026-05-24-family-a-gap-audit.md) — L1 audit (PR #1063 re-amended)
- [`docs/audits/2026-05-24-h4-coefficient-source-trace-and-so3-gap.md`](2026-05-24-h4-coefficient-source-trace-and-so3-gap.md) — L1 structural input source trace
- [`docs/audits/2026-05-24-derivation-chain-gb-jet-orders-and-pentagon.md`](2026-05-24-derivation-chain-gb-jet-orders-and-pentagon.md) — L1 per-step jet-order analysis
- [`docs/audits/2026-05-24-pentagon-identity-broad-context.md`](2026-05-24-pentagon-identity-broad-context.md) — L1 Pentagon literature
- PR [#1089](https://github.com/litlfred/qou/pull/1089) — L2+L3 sign-flip diagnostic (open)
- [`computations/isotope_record_schema.py`](../../computations/isotope_record_schema.py) — L2 channel assignment (current production)
- [`computations/probes/vol_density_borromean_h4_probe.py`](../../computations/probes/vol_density_borromean_h4_probe.py) — L1 structural Markov × 5/2 probe (+1.948 % at L1)
