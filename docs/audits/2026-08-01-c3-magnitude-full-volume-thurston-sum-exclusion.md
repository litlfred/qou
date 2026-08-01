# c₃ magnitude: the multi-winding sum diverges for the FULL 𝔙₄₁ too — scope-(b) via Thurston (2026-08-01)

**Axis:** Q_β c₃ bar-odd `S` — the **magnitude** ratio `|S_p/S_m| ≈ 4.075`
(`qou-82w7` / `qou-dtd3`). **No c_k wired; no fit; registry untouched; no
`SDeformedVolumeChannel` instance fabricated.** This doc **upgrades** the #4501
multi-winding-sum divergence from scope-(a) to **scope-(b)** and definitively
closes the sum sub-branch.

## The open lever this closes

PR #4501 showed the multi-winding even-channel bridge sum `Σ_{m,ℓ} e^{−Re𝔙/ℏ_q}`
diverges in the **leading quadratic** NZ truncation, and flagged (scope-(a)) that a
**full, non-truncated 𝔙₄₁** *might* restore convergence (its large-`|u|` growth). This
was the single untested lever. It fails — and for a sharp geometric reason.

Probe: [`qbeta_c3_magnitude_full_volume_thurston_probe.py`](../../computations/qbeta/qbeta_c3_magnitude_full_volume_thurston_probe.py)
(exit 0), witness
[`qbeta-c3-magnitude-full-volume-thurston.witness.json`](../../computations/qbeta/qbeta-c3-magnitude-full-volume-thurston.witness.json).

## The argument (geometric, not the closed form of 𝔙₄₁)

Each cusp winding/slope `(m,ℓ) ∈ ℤ²` is a **Dehn filling** of the figure-eight
complement. Thurston's hyperbolic Dehn-surgery theorem bounds the filled volume:

```
0 < Re 𝔙₄₁(u_{m,ℓ}) ≤ Vol(4₁) ≈ 2.0299 ,   and  Re 𝔙₄₁(u_{m,ℓ}) → Vol(4₁) as |(m,ℓ)| → ∞
```

(filling volumes increase to the cusped volume from below; Neumann–Zagier give the
leading `−(τ/4)u²` correction). The even-channel bridge term `e^{−Re𝔙/ℏ_q}` is
**decreasing** in `Re𝔙`, so the bound gives a **positive floor**:

```
e^{−Re𝔙(u_{m,ℓ})/ℏ_q} ≥ e^{−Vol(4₁)/ℏ_q} = ε₀ ≈ 1.267×10⁻⁹ > 0   for every slope,
```

and moreover the terms **→ ε₀ (not 0)** as `|(m,ℓ)| → ∞` (volumes → Vol(4₁)). The
**necessary condition for convergence — terms → 0 — fails**. There are infinitely many
slopes, each contributing `≥ ε₀ > 0`, so

```
Σ_{m,ℓ} e^{−Re𝔙(u_{m,ℓ})/ℏ_q}   DIVERGES   (for the exact 𝔙₄₁, not just the truncation).
```

The probe demonstrates the shape-independence: any monotone saturating model
`Re𝔙(r) = Vol(4₁)(1−e^{−r})` (→ Vol(4₁)) already has `term → ε₀` (`r=32`: `1.2666×10⁻⁹`).

## Scope-(b) structural exclusion (cited invariant)

The multi-winding even-channel exponential-bridge **sum** cannot be the c₃ magnitude
source, for **any** potential respecting the Thurston bound — which the true `𝔙₄₁`
does. **Cited invariant: Thurston's Dehn-surgery volume bound** (`Re𝔙 ≤ Vol(4₁)`). Per
the (a)/(b) discipline this is a legitimate scope-(b) exclusion: the divergence is
**structural**, not a truncation artifact, and is backed by a named theorem.

The elementary consequence — *a real sequence bounded below by `ε₀ > 0` on an infinite
index set is not summable* (term test / `Summable.tendsto_cofinite_zero`) — is a clean
Lean-formalizable lemma; the deep input (the volume bound) is cited to Thurston, not
re-proved. (Lean lemma deferred as a follow-up; the scope-(b) backing is the citation.)

## Net — the sum branch is closed; only the argument map survives

The even-channel exponential bridge is now negative **four ways**:
1. single canonical pair — ~3.9× short (#4497);
2. multi-winding sum, leading truncation — diverges scope-(a) (#4501);
3. resurgent one-instanton ratio — circular (#4501);
4. **multi-winding sum, full 𝔙₄₁ — diverges scope-(b) via Thurston (this doc).**

So the c₃ magnitude does **not** come from a lattice sum of any kind. The sole
surviving route is a **single geometric structure** `u(q₀)` — the open argument map
(`qou-82w7`). **Do not route a c₃ magnitude closure through any multi-winding
even-channel sum** — it is structurally divergent.

-- Ref: [thurston1978] The geometry and topology of three-manifolds (Dehn-surgery volume bound)
-- Ref: [manuscript] docs/audits/2026-08-01-c3-magnitude-multiwinding-and-resurgent-obstructions.md (#4501)
-- Ref: [manuscript] docs/audits/2026-08-01-c3-magnitude-exp-bridge-canonical-windings-miss.md (#4497)
-- Ref: [manuscript] docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md (qou-82w7)
