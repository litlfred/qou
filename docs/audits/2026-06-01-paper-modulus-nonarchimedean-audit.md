# Paper `|...|` audit — non-archimedean misuse (2026-06-01)

**Date:** 2026-06-01
**PR:** TBD (claude/phi-q-modulus-audit-and-reframe-2026-06-01)
**Status:** AUDIT — identifies misuse sites; refactor proposal pending.
**Triggered by:** user 2026-06-01: *"more general statements (even if
char p) should be in paper; specialize only when needed for
archimedean."*

## TL;DR

**212 total `|...|` math sites** in the paper. **34 classified as
NON-ARCH-MISUSE** — `|...|` appearing in categorical / pre-τ contexts
where it should not.

| Classification | Count | Meaning |
|---|---|---|
| ARCHIMEDEAN-OK | 74 | `|...|` in explicit archimedean context |
| **NON-ARCH-MISUSE** | **34** | **`|...|` in categorical context — should be removed** |
| BOTH-SIGNALS | 27 | Mixed context — needs human classification |
| AMBIGUOUS | 77 | Context too short to classify automatically |

**By directory (NON-ARCH-MISUSE):**
- `mass-theory/` — **24 sites**
- `mass-endomorphism/` — 4
- `braids-and-knots/` — 3
- `predicted-spectra/` — 2
- `observations/` — 1

## Worst offenders (priority fix list)

### Tier 1 — Self-contradictory

**`conj:im-q-physical-role`** (line 5):
```
𝔪_{q,𝓚} = |tr_M|
```
A conjecture ABOUT Im(q)'s physical role that USES modulus (which
strips any Im content). The conjecture is logically self-contradictory
as stated. Highest-priority refactor.

### Tier 2 — Flagship categorical formulas with `|tr_M|`

| File | Line | Statement |
|------|------|-----------|
| `atom-knot-mass-derivation.md` | 66 | `M(𝔥) := ν_SDP·m(𝔥) = ν_SDP·[|tr_M(T_w)| + tower + tr_M(C_dim_q)]` — flagship categorical definition |
| `atom-knot-mass-derivation.md` | 72 | `|tr_M(T_w)|` defined as "the descended Markov trace" |
| `brane-tower-z-habiro.md` | 122, 172, 217 | `B = m_e·ρ·(|tr_M(T_w)| + tower^(k) + σ_3A)` — categorical binding formula |
| `conj-canonical-knot-id-sdp.md` | 20, 99 | Flagship single-term `B = m_e·ρ·|tr_M(T_w)|` |
| `calibration-inputs.md` | 147 | `𝔪(ϱ) = |tr_M(ρ(β))|` — mass DEFINITION |
| `feynman-categorical-trace.md` | 41 | `|tr_M(ρ(β))|` in feynman-categorical statement |
| `deuterium-derived-binding.md` | 131-132 | `Δtr = |tr_M(free)| − |tr_M(atom)|` — TWO redundant `|...|` in a difference |
| `descended-level-zero.md` | 194 | "The single-level mass is `|tr_M(ρ(β))|`" |
| `np-discrepancy-resolution.md` | 70-71 | Term 1 "descended `|tr_M|`": `|tr_M(𝓑_p)|·1.065 > |tr_M(𝓑_n)|·0.923` — `|...|` no-op (both positive) but categorically wrong |
| `borromean-markov-trace-closed-form.md` | 175, 177 | `F_Bor = |tr_M|·[3]_q!/q³` |

### Tier 3 — Categorical (probability / measure) contexts

| File | Line | Statement |
|------|------|-----------|
| `markov-disambiguation.md` | 17-18 | `p_{w→w'} = |tr_M(ρ(w'))|² / Σ|tr_M(ρ(w''))|²` — Markov probability defined via |·|² |
| `atom-mass-full-hecke.md` | 44 | `𝔪_vert = |tr_M^full(Φ_mass)|` |
| `proton-mass-substrate-identity.md` | 14 | `|tr_M(β_Bor, q)|` |
| `rem-im-q-vs-p-skew.md` | 33 | `𝔪_{q,𝓚} = |tr_M(ρ(β_𝓚))|` |

## Recommended refactor

**Per the user's framing (paper-level discipline parallel to CLAUDE.md §7c):**

1. **Categorical / pre-τ statements** should use signed `tr_M`, `χ_λ`, etc. — these are bar-asymmetric objects per `prop:li2q-phiq-bar-symmetrization` and should respect that asymmetry at the categorical level.

2. **Archimedean specializations** add `|...|` ONLY where convergence requires it (e.g., `|v| < q` for Φ_q radius) AND where positivity is required by the OBSERVABLE (e.g., mass = positive real).

3. **Standard form should be:**
   - Categorical theorem: `𝔪(ϱ) = tr_M(ρ(β))` (signed, in the Habiro ring / categorical sense)
   - Archimedean specialization: "Evaluating at q_0 ∈ ℝ via τ_arch, the observable mass is `|tr_M(ρ(β))(q_0)|` for positivity."

4. **Q-difference / Habiro contexts** stay signed throughout — they live in the fibre.

5. **Markov-trace probability** (`p_{w→w'} = |tr_M(ρ(w'))|²`) uses `|...|²` ≡ tr_M · conj(tr_M) which IS a categorical operation (related to bar-involution), so this is borderline OK — but should be rewritten as `tr_M · \bar{tr_M}` to make the bar-involution explicit.

## Scope of refactor

- Tier 1 (1 site): immediate fix — replace `|tr_M|` with signed `tr_M` in the conjecture about Im(q). Edit `conj-im-q-physical-role.md`.
- Tier 2 (10+ sites): substantial refactor — many flagship formulas. Each requires a careful read to determine whether the `|...|` is masking a bar-asymmetric content or genuinely needed for the observable.
- Tier 3 (4 sites): probability / measure contexts — needs separate audit (some `|...|²` might be `tr_M·\bar{tr_M}` in disguise).

**Total refactor effort:** estimate 15–20 file edits, 1–2 sessions. Out of scope for this PR.

## What this PR does NOT do

- ❌ Does NOT refactor any paper content. Audit only.
- ❌ Does NOT modify production wiring.
- ❌ Does NOT pick a side on whether `|...|` is "correct" in any specific context — flags the issue for human/author review.

## Files

- `computations/paper_modulus_audit_nonarchimedean.py`
- `computations/paper-modulus-audit-nonarchimedean.witness.json`
- `docs/audits/2026-06-01-paper-modulus-nonarchimedean-audit.md` (this file)

## Methodology limitations

- Regex-based classification with 5-line context window. Subject to:
  - **False positives**: some categorical statements DO need `|...|` if positivity is the categorical content (e.g., norms, measures)
  - **False negatives**: some categorical misuses may classify as "AMBIGUOUS" if section header lacks clear keyword
- The 77 AMBIGUOUS sites warrant individual review
- The 27 BOTH-SIGNALS sites might be archimedean specializations correctly applied — needs case-by-case classification

## Cross-refs

- PR #1641 — sister diagnostic showing Φ_q(signed) vs Φ_q(|...|) up to 92% per-term divergence
- PR #1626 — complex c_3 fibre diagnostic
- PR #1616 — Im(q) fibre/observable framing in CLAUDE.md
- `prop:li2q-phiq-bar-symmetrization` — the bar-asymmetric Φ_q vs bar-symmetric Li_2^q split
- CLAUDE.md §7c — base ring convention (generic R vs archimedean ℝ); analogous paper-level discipline
