# 2026-06-28 — Brane-tower m_can: formalize-first plan (single pipeline, conventions derived)

**Branch:** `claude/deuteron-m-sym-error-rf9i4u` · **PR:** #3016 · **Bean:** `km42`

Owner directives (this turn): **single pipeline, no special-casing** (no
`m_e·Vol(𝓑₃)`, no magic-A); **derive the conventions from the formalism**
(Frobenius pairing / categorical action), not numerically; **formalize-first**
(prove the convergence bound before the wide build). This doc records the
derivations and the Lean gates that must close before any A≥3 compute.

## 1. The single pipeline = the unified curvature-rank mass formula

No special-casing means one functional for every nucleus:

    𝔪_q,𝒦(𝒯) = Σ_{k=0}^{n-1} α_k · Φ_k(𝒦, 𝒯)      (prop:unified-curvature-rank-mass-formula)

with `α_{k≥4} = m_e·8G` **uniform** (`prop:plancherel-term-7-formulation`).
`m_can⁰ = m_unbnd,can − E₀·Δtr` (shipped, PR #3016) is the **k=0 descended
term** of this formula. The per-braid brane tower (`prop:per-braid-mass-tower`)
is the explicit jet-stratified content of the same Σ_k.

**No-special-casing corollary (the deep target).** A true single pipeline emits
the *nucleon* masses from the SAME functional — i.e. `m_p, m_n` as the k=0 term
on their own braids, not via the `canonical_mass` muon-anchored facade. That
requires the absolute-mass normaliser (`F_Bor = |tr_M|·[3]_q!/q³`) to be the
brane tower's own k≥1 content rather than a separate factor — this is exactly
bean **`ovud`** ("wire Li₂^q brane-tower into production F_Bor, replace /q³").
Until `ovud` lands, `m_can⁰` uses the facade nucleon masses; flagged here as the
one remaining special-case to excise for a literal single pipeline.

## 2. Convention Q2 (Li₂^q sign) — DERIVED from the categorical action

`bar-parity-split.md` (`prop:bar-parity-split`, Lean `QOU.Mass.evenPart_*`,
sorry-free): the bar-involution σ (q↦q⁻¹) splits every element; **binding is the
bar-EVEN (cosh) part**, β-decay the bar-odd (sinh) part.

- `Li₂^q(z) = Σ zⁿ/(n[n]_q)` is **bar-symmetric** (`[n]_q` is q↦q⁻¹-invariant),
  so it already lies in the binding (bar-even) channel. ✓
- The **argument sign** is the Hecke **antisymmetric eigenvalue −q⁻¹** (antipode
  `S(σᵢ)=σᵢ⁻¹`; Hecke `(σ−q)(σ+q⁻¹)=0`). The antisymmetric channel carries −q⁻¹,
  so the canonical brane-tower term is

      g(x) = −Li₂^q(−x)         (= `_li_2_q_util` doc lines 34–41)

The bare `+Li₂^q(+x)` (`compute_t2_t3_from_vols`) is an unnormalised helper, **not**
the binding projection. **Q2 resolved: `g = −Li₂^q(−x)`.**

## 3. Convention Q1 (A=2 pair stratum) — DERIVED from the strata

Per-braid strata: ℓ=0 = {W} (descended, functional `|tr_M(W)|`); ℓ=2 = pairs
(functional `z²·g(|tr_M(ξξ')|)`). For A=2 the single pair *braid* coincides with
W, but the two **functionals** differ (`|·|` vs `z²·g(·)`). The prop's
double-count carve-out forbids repeating the **descended product** `|tr_M|` per
jet level — it does **not** forbid the dilog pair term. **Q1 resolved: the A=2
pair IS included.** Consequence (honest): the deuteron tower is `+33%`
(`g=−Li₂^q(−·)`), worse than the `+12%` k=0 term — the tower **adds** binding;
it does not close the over-bound deuteron (that gap is not a truncation error).

## 4. Convention Q3 (formalize-first gate) — the ambient convergence bound

Before any A≥3 wide build, prove the prop's standing claim

    |tr_M(ξ)| < q₀   for every sub-braid stratum ξ evaluated via the
                     ambient H_{3A} Schur–Weyl path

(`prop:per-braid-mass-tower` §"All sub-braid Markov traces … |tr_M(ξ)| < q").
This is the gate that the naive H₆ product violates (`tr_p² ≈ 1.134 > q₀`) and
that caused the superseded per-generator form to diverge. **Lean target:** a
`QOU.Mass.ambient_subbraid_trace_lt_q` lemma (or §3b-cond class) bounding the
ambient Markov trace by `q₀`. Only after it closes is the A≥3 ambient-pair
compute (helps the under-bound ⁴He/⁶Li/⁷Li) authorised.

## 5. Status / gates

| Item | State |
|---|---|
| `m_can⁰ = m_unbnd,can − E₀·Δtr` (k=0) | ✅ shipped (PR #3016) |
| Q2 sign `g = −Li₂^q(−x)` | ✅ derived (§2), locked in `per_braid_tower.py` |
| Q1 A=2 pair inclusion | ✅ derived (§3), deuteron tower `+33%` (honest) |
| Q3 ambient bound `|tr_M(ξ)|<q₀` | ⬜ **Lean gate** — blocks A≥3 build |
| Single-pipeline nucleon masses (excise facade) | ⬜ gated on bean `ovud` (F_Bor brane tower) |

**Next action:** author the Q3 Lean lemma; on close, build the ambient-pair
tower as the k≥2 content of the single Σ_k pipeline (no special-casing).
