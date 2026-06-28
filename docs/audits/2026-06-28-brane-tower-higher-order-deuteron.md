# 2026-06-28 — Higher-order brane tower for nuclear binding: deuteron result + the A≥3 ambient-trace gap

**Branch:** `claude/deuteron-m-sym-error-rf9i4u` · **PR:** #3016 · **Bean:** `km42`

Follow-on to the deuteron `m_sym` error investigation. Owner ask: headline a
canonically-derived mass `m_can` (pure Markov trace, zero AME/CODATA beyond
CAL-1 m_e + CAL-2 q₀), use the **full brane tower**, build the higher orders,
and fix the divergent implementation.

## 1. The implemented "full tower" diverges — it is the superseded per-generator form

`mass_at_3A_proper.binding_3A_tower` (via `mass_from_tower`) gives, for the
deuteron, **B ≈ 6,926,226 MeV** (`m_free ≈ 4.7e7`, `m_atom ≈ 3.9e7`). This is
the `prop:mass-endomorphism-tower` **per-generator** form

    𝔪_per-gen = |Π_i V̂ᵢ| + Σ_i Φ_q(|V̂ᵢ|) + z²·Σ Φ_q(|V̂ᵢV̂ⱼ|),

whose per-generator product `Π V̂ᵢ` compounds past the Φ_q convergence radius
`|z| < q`. It is **explicitly superseded** by `prop:per-braid-mass-tower`
(per-braid-mass-tower.md §"Supersession of the per-generator form").

## 2. The convergent per-braid form

    𝔪(W) = |tr_M(W)| + Σ_{ξ∈S₁} g(|tr_M(ξ)|) + z²·Σ_{(ξ,ξ')∈S₂} g(|tr_M(ξξ')|) + …

with sub-braid (not per-generator) traces, `g = −Li_2^q(−·)` the **symmetric**
(bar-invariant) Rogers dilogarithm (binding context, `_li_2_q_util.py` +
cheat-sheet §4), `z = 1/(q^{1/2}+q^{-1/2})`. Geometric `ℏ_q²`-suppressed tail
(`prop:jet-tower-convergence`), `ℏ_q² ≈ 0.0098` per jet level.

**Binding = `E₀·(𝔪_free − 𝔪_atom)`** → the per-nucleon **singleton terms cancel**
(nucleons unchanged bound-vs-free). Survivors: the descended `Δtr_M` (= level 0,
`B_can⁰`) and the **pair** terms.

## 3. Deuteron result (exact — the single pair IS the whole atom)

`computations/per_braid_tower.py` (50 dps):

| form | B(²H) | err = B_AME/B |
|---|--:|--:|
| `B_can⁰ = E₀·Δtr` (level 0) | 2.491 | 0.893 (**+12.0 %**) |
| `B_tower` (+ n=0 pair, `g=−Li_2^q(−·)`) | 2.967 | 0.750 (+33.4 %) |
| `B_tower` (+ n=0 pair, `g=+Li_2^q(+·)`) | 3.625 | 0.614 (+63.0 %) |

**The n=0 pair term ADDS binding under both sign conventions.** The deuteron is
already *over*-bound at level 0 (+12 %), so the higher tower makes it **worse**,
not better. Higher jet levels (`n≥1`) are `ℏ_q²≈1 %`-suppressed and cannot
reverse a +0.48 MeV correction.

**Implication (corrects the working hypothesis "the full tower closes the
deuteron"):** the brane tower adds binding, so it *helps the under-bound A≥3
nuclei* (level-0 `E₀·Δtr` under-binds ⁴He by 7.4×) and *hurts the over-bound
deuteron*. The deuteron's sub-percent number (`m_e·Vol(𝓑₃)·Δtr`, +0.19 %, cheat
sheet) comes from the **Vol(𝓑₃)=8G scale**, not from tower orders.

## 4. The A≥3 open item — ambient sub-braid traces

The prop requires each sub-braid trace via the proper H_{3A} Schur–Weyl path so
`|tr_M(ξ)| < q₀`. Computing a nucleon-PAIR trace naively as an isolated H₆ trace
gives the **free pp-pair** value `tr_p² ≈ 1.134 > q₀ ≈ 1.110` → `Li_2^q = ∞`
(the same divergence class as §1). The A≥3 pair terms must be evaluated as
`χ^λ(ξ)` for `λ ⊢ 3A` in the **ambient** algebra (the sub-braid embedded in the
full 3A-strand transfer), not in its own H₆. That ambient-pair build is the
remaining work; the deuteron (A=2, pair = whole atom) is the one exact case.

## 5. Two disambiguations needed (paper-level, not inferable from code)

1. **Does A=2 carry the pair term?** Its only pair coincides with the whole-atom
   descended stratum. Reading A (degenerate → exclude): `m_can(D)=m_can⁰`, +12 %.
   Reading B (distinct functional → include): +33 %. The reference
   `per_braid_tower.py` cited in the prop was never merged to `main`, so the
   intended convention is not recoverable from the corpus.
2. **Li_2^q sign convention**: `_li_2_q_util.py` carries BOTH `−Li_2^q(−x)`
   (doc lines 34–41) and `+Li_2^q(+x)` (impl line 141). They differ by 2× on the
   deuteron pair term.

## Status

- **Shipped (PR #3016):** `m_can⁰ = m_unbnd,can − E₀·Δtr` headline (deuteron
  mass error 6× better than the log `m_sym`).
- **This doc + `per_braid_tower.py`:** convergent tower, deuteron exact, the
  A≥3 ambient-trace gap + the two conventions stated.
- **Open:** A≥3 ambient-pair traces (helps heavy nuclei); owner ruling on the
  two §5 conventions.
