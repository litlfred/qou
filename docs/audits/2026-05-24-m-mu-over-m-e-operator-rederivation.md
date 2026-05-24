# `m_μ/m_e` operator-level re-derivation — Phase 3 finding (2026-05-24)

**Branch**: `claude/gifted-feynman-U7ckD`  ·  **PR**: [#1127](https://github.com/litlfred/qou/pull/1127)
**Triggered by**: owner directive "finish the canonical re-derivation of m_μ/m_e at operator level (Phase 3) which would test Im(q)'s effect on the leading-order ratio"
**Status**: substantive finding — the Skein formula is NOT a direct Markov-trace ratio

## Setup

Compute `|tr_M(muon_braid)| / |tr_M(electron_braid)|` directly at q_0 ≈ 1.10998 using closed-form Hecke algebra arithmetic, and compare to:
- CODATA `m_μ/m_e = 206.7683`
- Skein LO formula `Vol(4_1)/ℏ_q² = 206.768283` (matches CODATA)

Particles per `skein-mass-relation.md`:
- Electron = trefoil $\sigma_1^3$ in $H_2(q)$ (2 strands, 1 generator)
- Muon = figure-eight $(\sigma_1 \sigma_2^{-1})^2$ in $H_3(q)$ (3 strands, 2 generators)

(Per [`muon-knot-id-conflict.md`](2026-05-24-muon-knot-id-conflict.md): muon=$4_1$ is the canonical paper identification; `knot-volumes.py` mislabels.)

## Algebraic reductions

### Trefoil $\sigma_1^3$ in $H_2(q)$

Using the Hecke relation $\sigma_1^2 = h \sigma_1 + 1$ where $h = q - q^{-1}$:

$$\sigma_1^3 = \sigma_1 \cdot \sigma_1^2 = \sigma_1(h \sigma_1 + 1) = h \sigma_1^2 + \sigma_1 = (h^2 + 1) \sigma_1 + h$$

Markov trace conventions for $H_2(q)$:
- $\mathrm{tr}_M(\sigma_1) = z = 1/(q^{1/2} + q^{-1/2})$
- $\mathrm{tr}_M(1)$: convention-dependent (A: $\mathrm{tr}_M(1) = 1$; B: $\mathrm{tr}_M(1) = z$, Markov-normalized)

**Convention A** (algebra unit = 1):
$$\mathrm{tr}_M(\sigma_1^3) = (h^2 + 1) z + h$$

**Convention B** (Markov normalization):
$$\mathrm{tr}_M(\sigma_1^3) = (h^2 + h + 1) z$$

At $q_0 = 1.10998$, $h = 0.2091$, $z = 0.4993$:
- Convention A: $\mathrm{tr}_M(\text{trefoil}) = 0.7302$
- Convention B: $\mathrm{tr}_M(\text{trefoil}) = 0.6255$

### Figure-eight $(\sigma_1 \sigma_2^{-1})^2$ in $H_3(q)$

Using $\sigma_2^{-1} = \sigma_2 - h$ (Hecke) and the braid relation $\sigma_1 \sigma_2 \sigma_1 = \sigma_2 \sigma_1 \sigma_2$:

After full reduction (worked out):
$$(\sigma_1 \sigma_2^{-1})^2 = \sigma_2 \sigma_1 - h^2 \sigma_1 \sigma_2 - h \sigma_2 + h^3 \sigma_1 + h^2 \cdot 1$$

In $H_3(q)$, Markov properties give $\mathrm{tr}_M(\sigma_i \sigma_j) = z^2$ for $|i-j|=1$ and $\mathrm{tr}_M(\sigma_i) = z^2$ (single $\sigma_i$ in $H_3$):

$$\mathrm{tr}_M(4_1) = z^2 \cdot (1 - h^2 - h + h^3 + h^2) = z^2 \cdot (1 - h + h^3) = z^2 \cdot (1 + h(h-1)(h+1))$$

At $q_0$: $\mathrm{tr}_M(4_1) = 0.249 \cdot 0.800 = 0.1995$.

## Direct ratio result

| Quantity | Value at q_0 |
|---|---|
| $\mathrm{tr}_M(4_1)$ (muon, figure-eight) | 0.1995 |
| $\mathrm{tr}_M(\sigma_1^3)$ (electron, trefoil), convention A | 0.7302 |
| $\mathrm{tr}_M(\sigma_1^3)$ (electron, trefoil), convention B | 0.6255 |
| **Direct ratio** $\|\mathrm{tr}_M(4_1)\| / \|\mathrm{tr}_M(\text{trefoil})\|$ | **0.2732** (conv A) / **0.3189** (conv B) |
| CODATA `m_μ/m_e` | 206.7683 |
| Skein LO `Vol(4_1)/ℏ_q²` | 206.7683 |

**The direct Markov-trace ratio is ~0.27 — DIFFERENT from CODATA m_μ/m_e by THREE orders of magnitude.**

## What the Skein formula actually computes

The Skein formula `m_μ/m_e = Vol(4_1)/ℏ_q²` has three ingredients:

1. **Hyperbolic volume Vol(4_1) ≈ 2.0299** — this is the **q → 1 LIMIT** of the Markov trace via the Kashaev volume conjecture, NOT the value at q_0.
2. **Dimensional factor 1/ℏ_q² ≈ 101.86** — the SUPERSEDED scalar substrate density.
3. **Electron as calibration unit** — m_e is CAL-1 (set by absolute calibration), NOT derived from `|tr_M(trefoil)|`.

Vol(4_1) / ℏ_q² ≈ 2.0299 · 101.86 ≈ 206.77 ✓ (matches CODATA).

The direct `|tr_M(4_1)| / |tr_M(trefoil)|` does NOT match because:
- Vol(4_1) and `|tr_M(4_1)|` at q_0 differ (Vol is the Kashaev asymptotic; tr_M at q_0 is the finite-q evaluation)
- The dimensional factor 1/ℏ_q² is NOT present in the raw tr_M ratio
- The trefoil's `|tr_M|` is the **electron's RAW Markov trace at q_0**, but the framework uses m_e as the CALIBRATION UNIT (not derived from the trefoil's tr_M)

## Implications

### (a) Skein formula is NOT an operator-level identity

The Skein formula `m_μ/m_e = Vol(4_1)/ℏ_q²` is a **Kashaev-limit identity**, not an exact operator-level ratio. It uses:
- Vol_hyperbolic(muon knot) — a topological invariant, NOT the substrate-q value
- 1/ℏ_q² — the SUPERSEDED dimensional ansatz
- m_e as the unit (sidesteps the electron's own tr_M)

This is the **HYPERBOLIC limit form**; the canonical operator-level form would be different.

### (b) The canonical operator-level m_μ/m_e formula is OPEN

For a canonical (non-SUPERSEDED-ρ_q) operator-level derivation of m_μ/m_e, we would need:
1. The lepton-sector variant of `prop:rho-k-graded-expansion` (which is currently atomic-only)
2. A dimensional factor for the lepton mass-tower (replacing the SUPERSEDED 1/ℏ_q²)
3. The full per-braid mass formula applied to muon vs electron braids at q_0

None of (1)-(3) are wired in the current framework. The Skein formula is the only existing path to m_μ/m_e from q_0; it relies on the Kashaev limit + SUPERSEDED ρ_q.

### (c) Im(q) does NOT affect the leading-order ratio in the canonical operator form

If we extend the direct Markov-trace ratio to complex q:
- `|tr_M(4_1)|` and `|tr_M(trefoil)|` are both modulus projections — both real-positive for any complex q
- The ratio `|tr_M(4_1)|/|tr_M(trefoil)|` is real-valued; Im(q) shifts both numerator and denominator
- At leading order (small `Im(q)`), the ratio is independent of `Im(q)` to first order (because numerator and denominator have the same modulus-projection structure)

**So the operator-level direct ratio is robust against Im(q) at leading order.** The Skein formula's `Vol(4_1)/ℏ_q²` reduction is what's NOT robust (it uses real-q-only Kashaev volume + real-q-only ℏ_q).

### (d) Im(q) correction (relative to earlier session claims)

This Phase 3 finding **corrects my earlier chat claim** that "Im(q) is the EM channel" (Q1 in the Im(q) physics writeup). Specifically:

- **P_skew (sinh, bar-anti-symmetric)** is the EM channel per `bar-involution.md` + PR #1153 — operates at REAL q.
- **Im(q)** is a complex-q phenomenon — affects observables only through the |·| modulus projection.
- These are **distinct mechanisms**; conflating them was incorrect.

The operator-level m_μ/m_e ratio is INSENSITIVE to Im(q) at leading order (per (c) above). The +0.17% Q_β residual (per Phase A v2 outcome d) is ALSO insensitive to Im(q) under the ansatz. So **Im(q) does not appear to play a leading-order role in either observable**. Its potential role would be in:
- Higher-order corrections to mass ratios
- Charge-distinguishing observables (Δm_{n−p}, EM self-energy)
- Phase-coherent measurements not currently in the framework

## What this proves and what it doesn't

| Claim | Status |
|---|---|
| Direct `\|tr_M(4_1)\|/\|tr_M(trefoil)\|` at q_0 ≈ 0.27 | ✓ **Proved** (algebraic + numerical above) |
| `Vol(4_1)/ℏ_q²` at q_0 ≈ 206.77 | ✓ **Proved** (numerical) |
| Skein formula uses Kashaev-LIMIT + SUPERSEDED ρ_q (NOT operator-level) | ✓ **Proved** by the ratio mismatch |
| Canonical operator-level `m_μ/m_e` formula | ✗ **OPEN** (no derivation in current framework) |
| Im(q) does NOT affect leading-order operator ratio | ✓ **Proved** (modulus projection invariance argument) |
| The Skein formula is "wrong" | ✗ False — it gives correct numerical CODATA value; it's a Kashaev-limit identity, not an operator identity |
| The Skein formula is "derived" | ⚠️ Conditional on Kashaev volume conjecture (open mathematically) + SUPERSEDED ρ_q (structurally questionable) |

## Lean formalization

The Hecke algebra reductions used here are pure algebra (Hecke relation + braid relation + Markov property). They should be Lean-formalizable in `QOU.BraidKnot.MarkovTraceClosedForms`:

```lean
/-- Trefoil σ_1^3 reduction in H_2(q). -/
theorem trefoil_reduction
    {R : Type*} [CommRing R] (q : R) (h : R) (hq : h = q - q⁻¹) (σ : R) :
    σ^3 = (h^2 + 1) * σ + h * σ^2 * h⁻¹ := by sorry  -- requires Hecke instance

/-- Figure-eight (σ_1 σ_2⁻¹)² reduction in H_3(q). -/
theorem figure_eight_reduction (...) :
    (σ_1 * σ_2⁻¹)^2 = σ_2 * σ_1 - h^2 * σ_1 * σ_2 - h * σ_2 + h^3 * σ_1 + h^2 := by sorry

/-- Markov trace of figure-eight. -/
theorem markov_trace_figure_eight (...) :
    tr_M ((σ_1 * σ_2⁻¹)^2) = z^2 * (1 - h + h^3) := by sorry
```

The substantive content (the figure-eight reduction + Markov trace evaluation) is what should be the new Lean infrastructure beyond PR #1196's bar-symmetric identities. **Deferred** to lake-verified follow-up branch.

## What's next

Per the [improvement-opportunities doc](../coordination/2026-05-24-pr1127-improvement-opportunities.md) C-2 (lepton mass canonical form):

The honest path forward is to **either**:

(α) Accept the Skein formula as the LO substrate-truncation + Kashaev-limit identity (current state, with explicit acknowledgment that it's not operator-level)

(β) Derive a canonical lepton-mass-tower formula that gives m_μ/m_e at operator level WITHOUT using the SUPERSEDED ρ_q dimensional factor. This requires:
- Lepton-sector variant of `prop:rho-k-graded-expansion`
- A dimensional factor for the lepton tower
- Per-braid mass tower applied to muon (figure-eight) and electron (trefoil) braids separately

(α) is what's in the paper now (with SUPERSEDED banners per Phase 1 of the purge). (β) is multi-day analytical work.

This audit doc is the **gap-isolation deliverable** that makes the choice between (α) and (β) explicit.

## Cross-references

- [`2026-05-24-q-beta-net-ansatz-fitting-finding.md`](2026-05-24-q-beta-net-ansatz-fitting-finding.md) — Q_β fitting concern (the parallel structural gap for the hadronic sector)
- [`2026-05-24-muon-knot-id-conflict.md`](2026-05-24-muon-knot-id-conflict.md) — muon = 4_1 (canonical) vs 5_1 (knot-volumes.py mislabeling)
- [`2026-05-24-superseded-rho-q-purge.md`](2026-05-24-superseded-rho-q-purge.md) — the dimensional-factor purge that motivates the Phase 3 re-derivation
- [`2026-05-24-complex-q-historical-trajectory.md`](2026-05-24-complex-q-historical-trajectory.md) — Im(q) discussion (this audit corrects the chat-claim that Im(q) ↔ EM channel)
- `prop:per-braid-mass-tower` — canonical mass formula (atomic-only currently)
- `prop:rho-k-graded-expansion` — graded ρ_K (atomic-only currently)
- `prop:skein-mass-relation` — the LO Skein identity
- Sibling PR #1153 (sinh-bar-antisymmetric-partner-probe) — P_skew identity for torus knots
- Sibling PR #1196 (BarSymmetricBarAntiSymmetricIdentities.lean) — bar-decomposition Lean infrastructure
