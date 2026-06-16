# Complex c_3 fibre probe — diagnostic findings (2026-06-01)

**Date:** 2026-06-01
**PR:** TBD (claude/qbeta-complex-c3-fibre-probe-2026-06-01)
**Status:** DIAGNOSTIC — refutes specific complex-c_3 candidates;
flags cross-anchor test as under-diagnostic at current anchor spacing.

## TL;DR

User-raised question (2026-06-01): "are we maybe missing an Im part
that's not directly observable?" — referencing the Im(q) fibre vs
observable framing from PR #1616.

Tested 4 specific complex-c_3 candidates:
- Candidate 1: `c_3(q) = -2 + i·δ(q)`, δ real — INCONCLUSIVE due to anchor proximity
- Candidate 2: `c_3(q) = J_Hopf(q)` at complex q — N/A (substrate Im(q_0) = 0 per Lusztig)
- Candidate 3: bar-decomposition sym/antisym = Re/Im of complex Δtr_M — **REFUTED**
- Candidate 4: Re-projection `Re[c_3] = -2` exactly with Im residual — **REFUTED**

Key finding: **the cross-anchor test (q_proton vs q_muon) is under-
diagnostic** at the current anchor spacing (|q_proton − q_muon| ≈ 1e-8).
The empirical c_3 swing is dominated by extraction-precision noise, NOT
by structural q-dependence.

The complex-c_3 framing remains structurally plausible per PR #1616 but
cannot be discriminated from real-c_3 with current data.

## Detailed candidate analysis

### Candidate 1: c_3(q) = -2 + i·δ(q)

```
δ(q_proton) = -0.0693
δ(q_muon)   = -0.0097
δ_proton / δ_muon = 7.13
ℏ_q(q_proton) / ℏ_q(q_muon) = 1.000000115
(ℏ_q ratio)² = 1.000000230
```

The 7× ratio in δ doesn't match any small power of ℏ_q. Two interpretations:

- **(a)** δ is NOT a simple power of ℏ_q — substrate structure is more complex
- **(b)** The cross-anchor δ values are dominated by extraction noise — the "swing" isn't structural

Without an independent third anchor (e.g., m_e-pin or m_He-pin separated more), can't discriminate (a) vs (b). **INCONCLUSIVE.**

### Candidate 3: bar-decomposition = Re/Im of complex Δtr_M

If `Δtr_M_complex(q) = sym(q) + i·antisym(q)`, then:

```
|Δtr_M_complex|² = sym² + antisym² = 1.733 × 10⁻²
|Δtr_M|² (real)  = (sym + antisym)² = 2.019 × 10⁻²
ratio            = 0.858 ≠ 1
```

**REFUTED.** The bar-decomposition is NOT a Re/Im split. It is the
eigenspace decomposition under the bar-involution `t ↔ 1/t` acting on
a REAL function — different from complex conjugation.

This is structurally meaningful: bar-involution and complex conjugation
are *different operations*. PR #1620's clean Hecke-natural form
`sym = -[2]_{q^(1/2)} · h̃² / 2` is a real eigenvalue of a real
involution, not the real part of a complex object.

### Candidate 4: Re[c_3] = -2 exactly, residual is Im at higher order

If `c_3 = -2 + i·δ` and the u^3 projection takes Re part only, then
empirical c_3 at u^3 order should be `-2` exactly. But:

```
empirical c_3 at q_proton = -2.0693 (NOT -2)
```

The deviation of -0.0693 IS at u^3 order — so it cannot be the Im-part
contribution that lives at u^6 in the magnitude expansion
`|1 + c_3·u^3|² = 1 + 2Re·u^3 + (Re² + Im²)·u^6`.

**REFUTED** — the deviation is at the wrong order for the Re-projection
model.

## Why the cross-anchor test is under-diagnostic

The two production q-anchors are:
- `q_proton` from m_p/m_e CODATA: 1.10997858275138...
- `q_muon` from m_μ/m_e CODATA:   1.10997859555418... (cross-check only post-2026-05-29 re-pin)

|q_proton − q_muon| ≈ 1.28 × 10⁻⁸.

At this anchor proximity:
- ℏ_q ratios are 1 ± O(10⁻⁸)
- Any "structural" q-dependence of c_3 = f(q) would produce
  δ(q_proton)/δ(q_muon) = 1 ± O(10⁻⁸)
- But empirical ratio is **7.13** — orders of magnitude away from the
  expected ratio for a structural q-dependence

**Conclusion:** the empirical "cross-anchor swing" of c_3 is dominated
by **extraction precision** in the residual / u³ division, NOT by
structural q-dependence. The discipline of "must match at both anchors"
is correct, but the THRESHOLD for "match" should be the extraction
precision (currently ~10⁻²), not absolute compute precision (10⁻⁵⁰).

## Implication for CAL-1/2/3 + fibre framing

Per CLAUDE.md §Canonical chain (PR #1616): CAL inputs measure
ARCHIMEDEAN observables only — they constrain Re[q_0] and Im[q_0] = 0
but give no information about the fibre Im structure of the Habiro
element.

**This probe's specific finding:** even if the fibre Habiro element has
Im components, the current cross-anchor test cannot detect them. The
c_k flip-flop pattern remains under-constrained by current data.

**What would discriminate complex-c_3 from real-c_3:**

1. **Wider-spaced q-anchors** — derive a third q from a different
   observable with sufficient precision (e.g., m_e/m_K if precise
   enough, or a non-mass observable).
2. **Direct Habiro q-difference equation analysis** — examine the
   structural equation `(1 − σ_q)F(q) = δ(q;q)_∞` per `d6b6e0483`
   audit for Im content rather than relying on numerical c_3
   extraction.
3. **Higher-precision Q_β data** — currently Q_β is measured to
   ~7.8 ppb experimentally. Improving by 10× would let cross-anchor
   tests at 1e-9 anchor spacing become diagnostic.

## What this audit does NOT do

- ❌ Does NOT propose a 7th c_k candidate to wire
- ❌ Does NOT claim complex-c_3 is the right framing — it's plausible
  per fibre/observable but not yet supported by data
- ❌ Does NOT modify any production wiring

## Anti-pattern guard

Per CLAUDE.md no-7th-ansatz discipline:

- ❌ Do NOT wire `c_3 = -2 + i·δ` for any specific δ form — refuted at q^3 order
- ❌ Do NOT promote the bar-decomposition (PR #1620) to Re/Im of a complex object — that interpretation is refuted (sum-of-squares mismatch)
- ❌ Do NOT search for an Im(c_3) function matching the 7× anchor ratio numerically — that's the 8th-ansatz trap

## Witness + cross-refs

- `computations/probes/qbeta-complex-c3-fibre-probe.witness.json`
- `computations/probes/qbeta_complex_c3_fibre_probe.py`
- PR #1616 — Im(q) fibre/observable framing in CLAUDE.md
- PR #1620 — bar-decomposition Hecke-natural form (the REAL bar-involution
  eigenspaces, not complex Re/Im)
- `docs/audits/2026-05-31-qbeta-bridge-narrowing.md` — 7 mechanisms ruled out
- `docs/audits/2026-05-30-qbeta-recursive-pair-rules-and-habiro-pde.md` — q-difference equation framing
- `todos/research-queue.json` — `research-qbeta-habiro-element-search`
  remains the keystone; this probe refines its scope
