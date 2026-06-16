# Chain 4 mixed chains — Wenzl × Kashaev × Kashiwara (plan)

**Date:** 2026-06-04
**PR:** (this branch — `claude/qbeta-mixed-chains-2026-06-04`)
**Status:** PLAN (compute pending)
**Predecessor:** [PR #1787 audit — n=5 + Demazure NEGATIVE](./2026-06-04-qbeta-chain4-n5-demazure-verdict.md)

## Why this direction

Every **single-chain** family in the residue-A categorical-ID search
is now TIERED-NEGATIVE:

| Family | Probed in | Verdict |
|---|---|---|
| n ≤ 4 partition Kashiwara crystal | PR #1772 | NEGATIVE |
| n = 5 partition Kashiwara crystal | PR #1787 | NEGATIVE |
| Demazure chars at ω_j of sl_n (n ∈ {3,4,5}) | PR #1787 (real D_i) | NEGATIVE |
| q-binomial / [k]_q monomials | PR #1772 + #1787 | NEAR-FUZZY artifact only |
| ℏ_q^N / b^N·ℏ_q^M / Q_β·ε (38 cands) | residue-A probe | NEGATIVE |

The 1ppQ ledger (cont. 5) lists **mixed chains** as the only
genuinely-unprobed legitimate direction: *products* combining a
Wenzl (Hecke/Markov-trace) invariant, a Kashaev (quantum-dilog)
evaluation, and a Kashiwara (partition / crystal) invariant.

## Target (carried forward verbatim)

| Quantity | Value |
|---|---|
| Residue A | `1.804e-15` (PR #1727; simple pole, fibre-level, anchor-independent) |
| ℏ_q formula | `ℏ_q = (q − 1) / q` — **NEVER hard-code** (predecessor h_q-bug burned 4 h) |
| Proton-pinned q₀ | `1.10997858275138080759166909561` |
| Muon-pinned q₀ | `1.10997868769193107842185960213` |
| ℏ_q at proton | ≈ 0.09908 |
| **Target prefactor** | `A / ℏ_q^15 ≈ 2.072` at proton anchor |

## The three component layers

### Wenzl (Hecke / Markov-trace per λ-block)

H_n(q) decomposes via Wenzl idempotents into matrix blocks indexed by
partitions λ ⊢ n. The per-block Markov-trace weight / quantum
dimension is the natural "Wenzl trace" value. Computed here via the
**closed-form hook-length principal specialisation**

```
q-dim(λ)(q) = q^{n(λ)} · [n]_q! / ∏_{c∈λ} [hook(c)]_q
```

plus the genuine Markov-trace block weight

```
w_λ(q, z) = z^{n−1} · q-dim(λ),   Markov parameter z = 1/(√q + 1/√q)
```

both pure-mpmath (the native `hecke-engine` is not built in this
sandbox; the hook formula is the canonical closed form pyhecke would
otherwise compute, cross-checked by Σ_λ (f^λ)² = n! and the q→1
limit).

### Kashaev (quantum dilogarithm)

At real q₀ ≈ 1.11 the Faddeev non-compact Φ_b (|q|=1) does **not**
apply. The meaningful objects on the real-q fibre are the **Rogers
q-dilogarithm** and the **q-exponential / q-Pochhammer**:

```
Li_2^q(x) = Σ_{m≥1} x^m / (m·(1 − q^{-m}))      (base q^{-1} < 1)
(x; p)_∞  = ∏_{m≥0} (1 − x p^m),   p = q^{−1} < 1 for convergence
```

Evaluated at the ρ-shifted Kashiwara lowest-weight argument
`z_λ = q^{−(n(λ)+1)} ∈ (0,1)` (the +1 ρ-shift keeps `z_λ` strictly
inside the unit disk, off the quantum-dilog pole at `x = 1`) and at
`x = ℏ_q`.

### Kashiwara (partition / crystal invariant)

Reuse the partition / SYT / Demazure machinery from PR #1787:
f^λ, maj-sum, q-dim, n(λ).

## Mixed candidate space

For each λ ⊢ n (n ∈ {3,4,5}):

- Wenzl value `W_λ ∈ {q-dim(λ), w_λ, f^λ}`
- Kashaev value `K_λ ∈ {Li_2^q(z_λ), (z_λ;q⁻¹)_∞, exp(Li_2^q), ...}`
- Mixed candidate `W_λ · K_λ`, plus ratios `W_λ / K_λ`, conjugate-pair
  products `W_λ · W_{λ'}`, and ℏ_q-normalised forms.

Total ≈ 100–200 candidates per n — manageable in one PR.

## Anti-pattern guards (STRICT — CLAUDE.md compliance)

- **TIERED reporting only**: NEAR-1PPM / NEAR-0.1PCT / NEAR-1PCT /
  NEAR-FUZZY / NEAR-CLOSE / MISS / ZERO. No ansatz at NEAR-FUZZY or
  coarser.
- **Cross-anchor BEFORE structural claim**: any NEAR-1PCT at proton
  anchor is immediately checked at muon anchor; swing > 1% (the c_3
  flip-flop pattern) ⇒ anchor-dependent fibre object, NOT a
  categorical invariant. STOP and surface to author before any
  closure claim.
- **ℏ_q from `(q − 1)/q`**, never hard-coded.
- **No production wiring** — this script is diagnostic-only.
- **No λ_scale re-framing** (absorbed into VolDensity 2026-05-23).
- **No Δ_λ closure claim** without the 4-grep checklist + the gating
  audit.
- **4-grep checklist** before declaring "open": done at verdict time.

## Deliverables

```
docs/audits/
  2026-06-04-qbeta-mixed-chains-plan.md      # this file
  2026-06-04-qbeta-mixed-chains-verdict.md   # final TIERED verdict
computations/qbeta/
  qbeta_chain4_mixed_wenzl_kashaev_kashiwara.py
  qbeta-chain4-mixed-wenzl-kashaev-kashiwara.witness.json  # auto-emitted
```

Witness emits BOTH proton + muon prefactor targets; `top10`
tier-sorted; `witness_safe()` strips `*_num` keys before JSON.
