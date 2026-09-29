# Coordination ledger — λ_scale CAL-4 (consolidated)

**Status:** Acknowledged-CAL-4 as of 2026-05-23. Empirically
falsifiable prediction; no closed-form derivation from substrate
across 8 independent searches.

**Supersedes (for reference only):**
- `2026-05-18-lambda-scale-falsification.md` — original falsification ledger (PR #701)
- `2026-05-20-lambda-p-followons-ledger.md` — PR #852 bar-symmetrization / Bring-Bloch
- `2026-05-22-cal4-lambda-scale.md` — CAL-4 cluster (PRs #888–#904)
- `2026-05-22-lambda-scale-alts-strategy-d-ledger.md` — Strategy D alternatives (PR #916)
- `explore-q10.md` — q^10 selectivity (PR #951)

## Empirical record (8 negative searches)

| search | PR(s) | basis / method | result |
|---|---|---|---|
| Tiers 0–5 | #701, #843 | PSLQ over 52 hyperbolic-knot Bloch-Wigner values, 100 dps, coeff ≤ 10³⁰ | no integer relation |
| q-dilog substrate-natural | #923 | PSLQ over Li₂^q + Φ_q at substrate-natural arguments | no integer relation |
| V̂_S + ℚ(ζ_60) | #928 | PSLQ over V̂_S + ℚ(ζ_60) + Tier-0 knot volumes | no integer relation |
| Commutative Φ_q | #941 | non-linear commutative Φ_q functional eq + pentagon-like | no <1 ppb (best ≈ 4%) |
| Operator Φ_q | #943 | operator-theoretic Φ_q in truncated Heisenberg rep | 19 ppm near-match 1/(1 − h_q·q₀^10) |
| q-locality | #951 | sweep across q₀ ± 0.05 on all 4 known near-matches | all 4 non-smooth (slope ~10⁷ ppm/q) |
| Reframing | #957 | Strategy I pre-flight: λ_p(q) = C·ℏ_q² exactly; Tier 5 already searched C | structurally misaligned axis |
| Strategy J | #969 | proton/neutron tr_M ratio probe (20 candidates × 7 targets) | 0.45% best pure-substrate |

## Key insights

### 1. Q-locality diagnostic (PR #951)

All known near-matches are **residual zero-crossings** at substrate
q₀, not smooth structural identities. Residual slope ~−1.7×10⁷
ppm/q across the substrate window. Per standing discipline "q₀ not
special, just where we happen to be," these are coincidences.

### 2. Reframing (PR #957)

λ_p(q) = (m_p/m_e) · ℏ_q² / (8G) = **C · ℏ_q²** exactly, where
ℏ_q := (q−1)/q and C = (m_p/m_e)/(8G) ≈ 250.576.

- All prior near-matches used h_q = q − 1/q (NOT ℏ_q), giving the
  **wrong q-parametrization** (h_q = (q+1)·ℏ_q has varying
  coefficient vs q).
- The structural question is to derive the **constant C** from
  substrate, not to find F(q) ≈ λ_p(q).
- Tier 5's search for T = λ_p · 8G ≈ 18.03 as a ℤ-combination of
  knot volumes was equivalent (T = C · ℏ_q² · 8G), and was negative.

### 3. Archimedean-image table (PR #990 + this consolidation)

The functor τ: **C** → **Arch** maps algebraic structures to real
observables. HOMFLYPT P(K; a, z) is the highest-value unbuilt
infrastructure: it gives the full SU(N) family N=2,3,4,...,∞ in one
polynomial, where the current pipeline accesses only N=2 (Jones /
Markov trace). The polynomial COEFFICIENTS are integers
(q-independent) — they sit on the correct axis for structural
derivations of C.

See [`rem:archimedean-image-table`](../../folio/quantum-observable-universe/braids-and-knots/archimedean-image-table.md)
for the full 13-row catalog.

## Closure status

**Formally acknowledged-CAL-4** as of PR #969 (merged 2026-05-23).
Both conjecture blocks carry the empirical-exhaustion banner:

- [`conj:lambda-scale-bring-bloch-identity`](../../folio/quantum-observable-universe/braids-and-knots/lambda-scale-bring-bloch-identity.md) — 8-search tally + acknowledged-CAL-4 paragraph
- [`conj:lambda-scale-substrate-form`](../../folio/quantum-observable-universe/braids-and-knots/lambda-scale-substrate-form.md) — q-locality refutation + reframing + "empirical only" title (PR #982)

## Low-priority open directions (not committed)

| direction | cost | likelihood |
|---|---|---|
| Deeper Strategy K (Tier 6/7, 250 knots, 200 dps) | ~1 day mpmath | low (6 prior negatives) |
| Full HOMFLYPT skein recursion on β_p/β_n | ~2 days implementation | unknown (correct axis via coefficients) |
| HOMFLYPT SU(N) family evaluation at N=3,4,...,6 | hours (after HOMFLYPT engine) | unknown |

## Sibling PRs (active)

| PR | Branch | Topic | Coordination status |
|---|---|---|---|
| #909 | `keen-maxwell-jqdPU` | Strategy D stage-1 + ε residual | 4 comments posted (reframing, q-locality, gate cherry-pick) |
| #916 | `lambda-scale-alts-strategy-d-2026-05-22` | Strategy enumeration F–M | 3 comments posted (reframing, non-smooth) |
| #920 | `cheat-sheet-tracker-2026-05-22` | §5 manager tracker | 1 comment posted (entry needs acknowledged-CAL-4 update) |
| #990 | `homflypt-skein-engine-2026-05-23` | HOMFLYPT engine scaffold (WIP) | new infrastructure, no conflicts |

## Decision record

| date | decision | who |
|---|---|---|
| 2026-05-18 | Original falsification: Family A ≠ target (wrong sign) | agent (PR #701) |
| 2026-05-21 | Truth-in-naming: `LAMBDA_PROTON_FITTED_FROM_CODATA` | agent (PR #888) |
| 2026-05-22 | Demote both conjectures to `conj:` | agent (PRs #892, #904) |
| 2026-05-22 | 4-search PSLQ exhaustion (Tiers + q-dilog + V̂_S + Φ_q) | agent (PRs #923, #928, #941) |
| 2026-05-22 | Operator Φ_q 19 ppm near-match (q^10 balance point) | agent (PR #943) |
| 2026-05-23 | Q-locality refutes all 4 near-matches as coincidences | agent (PR #951) |
| 2026-05-23 | Reframing: λ_p = C·ℏ_q², Tier 5 already searched C | agent (PR #957) |
| 2026-05-23 | Strategy J negative; formal acknowledged-CAL-4 status | agent (PR #969) |
| 2026-05-23 | Sync substrate-form block to acknowledged-CAL-4 | agent (PR #982) |
| 2026-05-23 | HOMFLYPT engine scaffold + Archimedean-image table | agent (PR #990) |
| 2026-05-23 | Consolidated coordination doc (this file) | agent |
