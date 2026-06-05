# GAP-A-4 L1 retrospective — per-atom Path B λ(K) is not a substrate transplant

**Date:** 2026-06-05
**Audit type:** post-L1 retrospective + next-probe identification
**Status:** clean negative consolidation; sharpens the open question for the next concrete probe.
**Owners:** PR chain — #1816 → #1841 → #1850 → #1853 → #1860 → #1822 → #1864 → #1868 → #1870 → #1872 → #1874 (L1 light-series probe, OPEN).

---

## §1. What L1 was supposed to do

GAP-A-4's scope ([`2026-06-04-gap-a4-path-b-lambda-K-scope.md`](./2026-06-04-gap-a4-path-b-lambda-K-scope.md) §4) proposed three closed-form candidates for the per-atom Path B `λ(K)`:

- **L1a** — uniform `linking_weight_family_a(q₀) ≈ 2.533`
- **L1b** — Phase-4 amplitude re-expressed in Path B coordinates
- **L1c** — Phase-4 carriers `[3]_q^{2(Z-1)} · (q^{1/2}+q^{-1/2})^{4N}` scaled by `lw(q₀)`

Each candidate was parameter-free, designed to **pass** the Δ_λ-gate "no 7th fit" discipline review.

## §2. What [PR #1874](https://github.com/litlfred/qou/pull/1874) actually showed

All three REFUTED across the light series; the **only** positive structural signal was the proton-row sanity assertion (L1a recovers the documented +2.89 % gap to 0.07 %).

| atom | `λ_emp` | L1a (lw) | L1b (Phase-4 re-expr) | L1c (carriers) |
|---|---:|---:|---:|---:|
| p | 2.460 | +2.96 % | -99.67 % | +2.96 % |
| n | 2.463 | +2.82 % | -99.43 % | +78.55 % |
| D | 2.820 | -10.20 % | -86.06 % | +1344.66 % |
| T | 4.224 | -40.04 % | +49.78 % | +15418.57 % |
| **³He** | **4.298** | **-41.07 %** | **-18.15 %** ⭐ | **+8683.01 %** |
| ⁴He | 5.704 | -55.60 % | +892.09 % | +106358.50 % |

**The L1b ³He row sits at -18.15 % — the only single-atom row in the entire grid that lands within 25 %.** This is a partial structural signal, not a derivation, but it's the most informative data point of the probe.

## §3. Three structural observations from the L1 grid

### O1. λ_emp grows monotonically with A — uniform multipliers are dead

`λ_emp` ranges from 2.46 at the proton to 5.70 at ⁴He — a 2.32× swing. **No single substrate constant can be the per-atom λ(K)**; the carrier framework must encode an A-dependent ladder. L1a (uniform `lw ≈ 2.53`) catches p/n by construction and breaks monotonically with A, as expected.

### O2. The Phase-4 carriers are dominant, not corrections

L1c's worst-rel of `+106358.50 %` at ⁴He says the `[3]_q^{2(Z-1)} · (q^{1/2}+q^{-1/2})^{4N}` carriers are **multiplicative powers in the binding-energy amplitude**, not small perturbations on Path B's mass multiplier. Direct transplant to Path B is structurally wrong; the Phase-4 carriers belong on the `B(K)` side of the `m(K) = Z·m_p + N·m_n − B(K)` decomposition, not in `λ(K)` directly.

### O3. The L1b ³He -18.15 % NEAR-MATCH is the lead

L1b's corrected form `λ_L1b(K) = A_Phase-4(K) · Vol_hyp(K)/Vol(𝓑₃) · ℏ_q²` lands within 25 % at ³He but at no other atom (closest neighbour: T at +49.78 %). What's special about ³He?

- Z=2, N=1, A=3 — the smallest two-proton nucleus.
- Vol_Phase-4(³He) = 12.554, identical to ⁴He's, distinct from D/T's 12.776.
- It's the first row where the Phase-4 color carrier `[3]_q^2` is non-trivial (Z=2) and the Phase-4 spin carrier `(q^{1/2}+q^{-1/2})^4` is the same as D's (N=1).

Hypothesis: L1b's `Vol_hyp/Vol(𝓑₃) · ℏ_q²` rescaling absorbs the *dominant* per-(Z, N) scaling at A=3, Z=2 specifically, but fails to capture the A-dependent ladder that drives the ⁴He / ³He growth ratio (5.70 / 4.30 = 1.33×, vs L1b's 56.59 / 3.52 = 16.1× overshoot). Something *additional* in ⁴He breaks the L1b form — N=2 doubling the spin carrier power isn't matched by an equivalent doubling of `λ_emp`.

## §4. What the next probe should look like

Given O1-O3, the next GAP-A-4 probe should:

1. **Drop the direct-transplant assumption.** Phase-4's carriers are amplitude-of-binding-energy carriers, not λ(K)-of-mass carriers. The two should NOT have the same `[3]_q^{2(Z-1)} · (q^{1/2}+q^{-1/2})^{4N}` form.

2. **Test an additive form**, not multiplicative. Per Path B's actual formula `m(K) = m_e · Vol(K)/ℏ_q² · λ(K) + S(K)`, the sub-leading `S(K)` term is exactly the thing that should absorb the A-dependent ladder. Re-derive `S(K)` candidates from Phase-4's A-decomposition and test whether `λ(K)` reduces to a near-constant (proton-anchored value ≈ 2.46) once `S(K)` is included.

3. **Investigate the L1b ³He coincidence**. Compute L1b's per-(Z, N) contributions at the ³He row in isolation; see whether the -18.15 % residual factors as a clean substrate quantity (e.g. q-deformed mass-ratio correction). If yes, that's the structural lead.

4. **Re-examine the per-knot Vol(K) convention** for compound atoms. The Phase-4 SnapPy JSJ values (12.776 for Z=1; 12.554 for Z=2) cluster by Z, suggesting they're not the genuine Path B `Vol(K)`. A re-derivation from the canonical atomic braid closure under the production convention may give different values that align L1 candidates better.

## §5. Net for the framework's open math

- **Phase-4 per-atom amplitude `A(K)`** is substrate-derived to ≤ 2.5 % and confirmed at deuteron to 0.07 %.
- **Per-partition `Δ_λ(K)` family** is closed: 17 no-fit ansätze refuted across 8 sessions (#1860 + #1870 + the gate-doc's 6 + L1's 3).
- **Per-atom Path B `λ(K)` direct-substrate-form** is closed: L1a/L1b/L1c refuted across the light series.
- **Productive remaining direction**: the additive `S(K)` sub-leading term in Path B (per §4 item 2), or the per-knot Vol(K) re-derivation (§4 item 4) — whichever the framework finds more tractable to formalize first.

The recommended one-line framing for downstream content: *"Phase-4 substrate-derives the per-atom binding-energy amplitude; the per-atom mass multiplier λ(K) is sub-leading-controlled rather than directly carrier-derived."*

## §6. Discipline

- **EXPLORATORY** — doc-only retrospective consolidation; no production code, no Lean, no witnesses changed.
- **Builds on**: the 17 no-fit closures + Phase-4's per-atom success + L1b's ³He partial-finding.
- **No 7th fit ansatz** — every candidate in §4 is a closed-form substrate quantity or a Path-B re-derivation; no fitted scalars.

## §7. Cross-references

- [`2026-06-04-three-paths-refuted-roadmap-update.md`](./2026-06-04-three-paths-refuted-roadmap-update.md) — the 3-path-refuted consolidation (#1864)
- [`2026-06-04-gap-a3-brane-tower-level-selection-scope.md`](./2026-06-04-gap-a3-brane-tower-level-selection-scope.md) — GAP-A-3 scope (#1868)
- [`2026-06-04-gap-a4-path-b-lambda-K-scope.md`](./2026-06-04-gap-a4-path-b-lambda-K-scope.md) — GAP-A-4 scope (#1872; L1 plan)
- [`2026-05-19-delta-lambda-phase4-z4N-closure.md`](./2026-05-19-delta-lambda-phase4-z4N-closure.md) — Phase-4 amplitude (the substrate-derived per-atom result)
- [`2026-05-18-delta-lambda-gating-context.md`](./2026-05-18-delta-lambda-gating-context.md) — the original Δ_λ gate doc + Path B/D framing
- PRs #1870 (P_λ probe) + #1874 (L1 probe) — the two probe-side closures of this session's chain
