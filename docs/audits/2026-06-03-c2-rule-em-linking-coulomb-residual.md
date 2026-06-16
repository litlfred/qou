# c=2 selection-rule × T-³He Coulomb-residual probe — a 0.1 %-level lead

**Date:** 2026-06-03
**Probe:** [`computations/probes/c2_rule_em_linking_residual.py`](../../computations/probes/c2_rule_em_linking_residual.py)
**Witness:** `c2-rule-em-linking-residual.witness.json`
**Branch:** `claude/habiro-per-knot-lambda-derivation-2026-06-03` (PR #1765 follow-up)
**Status:** EXPLORATORY. Suggestive lead at 0.1 % — **NOT** a derivation. No production wiring, no fit.

## What this tests

PR #1775 / [`docs/audits/2026-06-03-charge-coulomb-tn3he-derived.md`](2026-06-03-charge-coulomb-tn3he-derived.md) derives the categorical pp-Coulomb piece of the T-vs-³He AME binding split:

```
derived_Coulomb_dHe · [open EM-linking invariant] = AME split
   0.2377 MeV      ·    REMAINING_FACTOR 3.2137× = 0.7638 MeV
```

The 3.2137× is the open derivation target on **PR #1777** ("Derive the two-like-charge EM-linking invariant"). PR #1765 ships a zero-parameter per-component selection rule

```
lw(L; c=2) = (1/3) · Σ_{λ⊢3} dim_q V_λ = (q+1)² / (3q)
```

— the natural per-link scalar for the two-proton 2-component-link case. Question: does it fit the slot?

## Result

| object | value at q₀ | notes |
|---|---|---|
| `lw_c2(q₀) = (q+1)²/(3q)` | **1.336966** | zero-parameter selection rule |
| target factor | **3.213697** | exact from charge-coulomb witness |
| measured residual = target / lw_c2 | **2.403725** | what the EM-linking slot still needs |
| **candidate (a):** `12/5 = dim H_4 / I(4)` at q=1 | 2.400000 | −0.155 % off residual |
| candidate (b): `Σ dim_q² / Σ dim_q` at H_4, q₀ | 2.438529 | +1.448 % off residual |

Best factorization:

```
predicted_split = derived_Coulomb · lw_c2(q₀) · (12/5)
                = 0.2377  ·  1.336966  ·  2.4
                = 0.762616 MeV   vs AME 0.7638 MeV   →  −0.155 % off
```

## Honest framing — suggestive lead, not a derivation

**Why it's interesting:**

- The c=2 selection rule lands the residual within **0.155 %** of the *classical-limit* Wedderburn ratio `dim H_4 / I(4) = 24/10 = 12/5`.
- `12/5` carries a clean structural reading: regular-rep dimension over Gelfand-rep dimension at the proton's Wedderburn rank H_4 — exactly **one rank above** c=2's H_3, the same `n → n+1` jump my selection rule's open mechanism (lepton-fibre adjunction) hypothesizes.
- The full prediction reproduces the AME T-³He split to 0.155 %.
- **Zero free parameters.** The selection rule is fixed (anchored exact at muon c=1, proton c=3) and 12/5 is a categorical integer ratio.

**Why it's NOT a derivation:**

- 0.155 % is **NOT** derivation-tight. Δ_λ-gate / 1ppQ-level work requires ppm or better; this is ppt.
- The factorization mixes a **q-deformed** lw_c2(q₀) with the **classical-limit** 12/5. The natural fully-q-deformed analogue (candidate b: `Σ dim_q² / Σ dim_q` at H_4, q₀) lands **worse** (1.45 % off). There is no a-priori categorical reason for the un-q-deformation in the 12/5 piece.
- Could easily be coincidence at this precision — Wedderburn integer ratios at low n are not numerous enough to rule out chance.

**What would close it:**

1. A categorical reason for why `dim H_4 / I(4) = 12/5` enters un-q-deformed alongside the q-deformed lw_c2(q₀). E.g., maybe 12/5 lives in the **classical-limit projector** that selects the lepton-adjunction direction at the H_3 → H_4 boundary, while lw_c2(q₀) is the q-active Wedderburn weight inside that boundary.
2. OR: a different residual identification that lands at ≤ ppm. (Plausible candidates not yet tried: `(q+1)²/q + integer`, `[2]_q · ratio_classical_(H_5)`, etc.)
3. OR: the open derivation of PR #1777 lands by a different route entirely, and this 0.155 % near-match is recorded as a curious coincidence.

## Q-usage discipline

All symbolic work at fibre level (formal q). q₀ enters only at the final archimedean evaluation (Im(q₀) = 0). 12/5 is the **classical** limit at q = 1 — also a legitimate archimedean point. No |q| = 1 step. CLAUDE.md §7c compliant.

## Coordination

- **PR #1765** (selection rule home): this probe sits as a downstream consumer artefact, not a wiring change to the selection-rule probe itself.
- **PR #1777** (EM-linking invariant open derivation): concrete numerical candidate posted as a comment alongside this audit. The slot now has a falsifiable target shape: any derivation of the EM-linking invariant should either reproduce `lw_c2 · (12/5)` (or its q-deformed analogue) to ≤ ppm, or it gives a structurally different answer.
- **PR #1775** (parent Coulomb work): inputs sourced from its witness (provenance inlined in the probe).

## Update 2026-06-03: steps B + A run

### Step B (PSLQ scan for alternative residual identifications) — clean NEGATIVE

Probe: [`probes/c2_residual_pslq_scan.py`](../../computations/probes/c2_residual_pslq_scan.py)

PSLQ at tol `1e-30`, maxcoeff up to `10000`, against bases:

- `(residual, 1, h², h⁴)`
- `(residual, 1, h², h⁴, h⁶)`
- `(residual − 12/5, h², h⁴, h⁶)`

**No low-norm integer relation found** in any basis. Direct ratio scans (`residual / element` vs `p/q` with `|p|,|q| ≤ 30`) also produce no clean match within `1e-5`. Trial fits like `12/5 · (1 + h²/28)` land at 0.0009 % but the denominators have no structural justification — they are *fits*, not derivations.

**Conclusion (B):** the residual is **NOT** a low-height polynomial-in-h² over ℚ. The 12/5 stays the cleanest available identification, with the 0.155 % gap lying outside the polynomial basis.

### Step A (H_3 → H_4 categorical derivation) — PARTIAL SUCCESS

Probe: [`probes/c2_h3_h4_pieri_branching_derivation.py`](../../computations/probes/c2_h3_h4_pieri_branching_derivation.py)

Direct computation: the Frobenius-reciprocity branching trace of `H_3 → H_4` (Pieri rule, multiplicity 1 per addable box) gives

```
B(q) := Σ_{λ⊢3} dim_q(V_λ) · Σ_{µ⊢4, µ⊃λ} dim_q(V_µ)
B(1) = 1·(1+3) + 2·(3+2+3) + 1·(3+1) = 24 = dim H_4
```

Normalised by Gelfand dim:

```
B(1) / I(4) = 24 / 10 = 12/5    EXACTLY
```

**So 12/5 has a categorical home: it is the Frobenius-reciprocity branching trace from H_3 to H_4, normalized by the Gelfand dimension at the upper rank** — derived, not numerologically fit. This is the candidate categorical machinery for PR #1765's selection-rule open `n = c + 1` mechanism: the Pieri "+1 box" IS the "lepton-fibre adjunction" the selection rule hypothesized.

**But the q-deformed version makes it WORSE, not better.** At q₀:

```
B(q₀) / Gelfand_H_4(q₀) = 2.41220   →  +0.352 % vs residual
B(1)  / I(4) = 12/5 = 2.40000       →  −0.155 % vs residual  ← cleaner
```

The classical-q version is *closer*. This is the structural subtlety: if the categorical identification were exact, the fully q-deformed object should hit the q₀ residual to ≤ ppm, but it lands 0.35 % away. The classical-q version landing closer suggests an inconsistent factorisation — `lw_c2(q₀)` (q-deformed) × `B(1)/I(4)` (classical) has no a-priori categorical justification.

### Net verdict after A + B

- **12/5 IS a real categorical object** (Pieri-branching trace per Gelfand dim, derived at q=1). The selection rule's open mechanism has a candidate identification.
- **The 0.155 % residual gap at q₀ does NOT close** via either q-deformation (Step A: q-deformed lands further away) or h-polynomial corrections (Step B: PSLQ-negative).
- **Two remaining interpretations for the gap:**
  - **(i)** The 12/5 categorical identification is correct, and the 0.155 % is a **categorical Lobachevsky / transcendental** correction outside the polynomial basis — or a precision-noise artifact inside the source `derived_Coulomb_dHe = 0.23767...` value itself.
  - **(ii)** The c=2 selection rule is *almost but not* the right object — close enough that the H_3↓H_4 Pieri trace surfaces, but missing a small piece that makes the factorisation un-clean at q ≠ 1.

## Next on the queue

- **(C)** Hand off to PR #1777 — categorical lead recorded; the precision gap is now well-localized to a specific question (the un-clean q-deformation step), best pursued by someone with the framework's α_EM / KLR / SDP toolkit at hand.
- **(D)** Inspect whether the `derived_Coulomb_dHe` derivation in PR #1775 has its own 0.1 %-level corrections (e.g. higher-order pp-Coulomb terms) that would shift the residual.
- **(E)** Probe whether the 0.155 % is structural — try a different evaluation point (q=1 vs q=q₀ vs q=√q₀) or a different normalisation of the branching trace.
