# Transcendental-conjecture surreal-narrowing ledger

**Date:** 2026-06-08 · **Branch:** `claude/vigilant-fermat-SROph` · **PR:** #1995
**Status:** living ledger. Realizes the owner's directive — *"even if we can
narrow the transcendental conjectures to a statement on surreals in QOU, that is
worthwhile even if not able to prove the last bit; take the approach wherever
appropriate."*

## The approach (one line)

For each QOU transcendental conjecture, use the **surreal / iterated-integral
depth grading** to factor it into

```
   [ surreal-graded narrowing — provable / structural in QOU ]
                       +
   [ open residue — a NAMED external transcendence input ]
```

The narrowing is the worthwhile product even when the residue stays open. This
mirrors the keystone, which is already a *reduction* device (depth-2 theorem;
depth-≥3 reduced to Goncharov), not a proof engine.

## Classification axis (from the rank-2 probe)

Each narrowing is tagged by whether surreals are **essential** or **language**:

- **L (language):** the narrowing is single-axis / rank-1 (`ε`-powers only); the
  surreal statement re-describes an ordinary real asymptotic. Surreals are
  convenient, not necessary.
- **E? (essential candidate):** the narrowing involves `ε^ℓ` with `ℓ → ω`
  (infinitesimal to an infinite power) or an independent geometric divergence —
  an infinite-value-group object the `ε`-adic `ℝ` line cannot express. Surreals
  may be necessary. Decided by the finite-page-vs-perpetual check
  ([rank-2 probe](../audits/2026-06-08-surreal-rank2-nonabelian-stokes-quadratic-probe.md)).

## The ledger (period / volume cluster — pass 1)

| # | Conjecture | Surreal-graded narrowing (the worthwhile part) | Open residue (named external input) | Surreal? |
|---|---|---|---|---|
| 1 | [`gb-depth-period-correspondence`](../../content/quantum-observable-universe/mass-theory/gb-depth-period-correspondence.md) (keystone) | `τ_arch(G^(n)(ℋ_q)) ⊆ 𝒫_n`, sharp. **Depth-2 = THEOREM** (Bloch–Suslin). | Goncharov motivic (depth≥3); Beilinson (depth≥4) | L (proof is K-theoretic) |
| 2 | [`depth-2-identification-bloch-suslin`](../../content/quantum-observable-universe/appendix-surreals/depth-2-identification-bloch-suslin.md) | `G^(2)/𝒫_1 ≅ K_3^ind(F)⊗ℚ` via Bloch group + Suslin + Borel | — (proved at depth 2) | L |
| 3 | [`qou-infra-discharges-goncharov-zeta5`](../../content/quantum-observable-universe/appendix-surreals/qou-infra-discharges-goncharov-zeta5.md) | 22-term relation at `ζ₅` = Markov trace of an explicit Hecke `β`, NF-reduces mod depth-2 ⇒ discharges Goncharov at `ℚ(ζ₅)` | the P2 specialization-commutes lemma + the pruned β-search ([Avenue B scaffold](../workplans/2026-06-08-zeta5-goncharov-avenue-b-scaffold.md)) | L |
| 4 | [`kashaev-surreal`](../../content/quantum-observable-universe/appendix-surreals/kashaev-surreal.md) | `std`-part identity separating the algebraic (`tr_M`) from the transcendental (`Vol`) part of the volume conjecture | Volume Conjecture (open) | **L** (`q=e^{2πi/N}` ties the scales → rank-1) |
| 5 | `hyperbolic-volume-transcendence` (jet-order tower) | **Narrowed to finite-base-order by [PR #1990](https://github.com/litlfred/qou/pull/1990)** (jacobian rank = 3 at every `N≥3` via rank-monotonicity) — residual = surreal-bridge inputs I2/I3 only | I2 holonomy-shadow + I3 monodromy-shadow (physical, conjectural) | **L** — finite-page degeneration ⇒ rank-1 (a *worked instance* of the probe's rank-1 side) |
| 6 | [`two-filtration-bridge`](../../content/quantum-observable-universe/stochastic-mechanics/two-filtration-bridge-small-cases.md) | bar-class ⇒ depth: self-conjugate `λ`→depth 2 (`CS=0`), chiral pair→depth 3 (`CS≠0`); verified `n≤4` | general `n≥5` Vol/CS dictionary | L |

## The one essential candidate (not yet in a single conjecture block)

**The GS-tower compounding of the non-abelian-Stokes quadratic term.** The gauge
term `∫tr(F∧_q⋆_qF)` → Hecke-quadratic events `(q−q⁻¹)≈2ε` → `ε^ℓ`, `ℓ=ℓ(K)→ω`.
This is **E?** — the value group acquires an infinite generator, which the
`ε`-adic `ℝ` line cannot express. It is *not* currently stated as a transcendental
conjecture; the probe's next step is to check whether the **`motivic-perpetual-obstruction`**
/ GS spectral-sequence carries a perpetual `ε^ω` tail (⇒ surreal-essential, and a
new ledger row) or degenerates at a finite page (⇒ L, like row 5).

## Reading of the ledger (for the keep/purge decision)

- **By the owner's narrowing criterion, surreals already pass** (rows 1–6 are
  genuine reductions of open transcendental problems to named residues — the
  worthwhile product). ⇒ **keep, re-scoped as this ledger**, not as
  "millennium-problem bounds."
- **Surreal *necessity* (E?) is still undecided** and rides entirely on the one
  candidate above. If it resolves to L, the ledger is the *language* in which the
  narrowings are written (still worthwhile); if E?, surreals are load-bearing.
- **Either way the speculative `*-surreal-bound` millennium framing is the part
  to retire** — replace each with its ledger row (narrowing + named residue).

## Next passes (wherever appropriate — to fold in)

`observables-algebraic-independence`, `cs-evaluation-faithfulness`,
`bring-trilog-imaginary-tate-rational`, `cl3-zeta5-*`, `dilogarithm-archimedean-limit`
(keystone). Each gets a row: narrowing + named residue + L/E? tag. Do **not**
fabricate a residue — read the block first (corpus-grep discipline).
