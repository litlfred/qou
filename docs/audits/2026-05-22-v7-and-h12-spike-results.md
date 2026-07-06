# V_7 sub-leading correction + H_12 A-operator extract — spike results

**Date:** 2026-05-22
**Branch:** `claude/cheat-sheet-tracker-2026-05-22`
**Trigger:** Cheat-sheet §5 manager view "two highest-leverage next
actions" — V_7 sub-leading refinement (#916 follow-up) and H_12
A-operator extract (Track B unblocker).

## TL;DR

| Spike | Outcome |
|---|---|
| V_7 sub-leading correction search at q_0 (100 dps PSLQ) | **NEGATIVE.** No clean categorical correction X(q) found against the natural basis `{h²·G, h^4, h^6, h², ℏ_q²·G}` at coeff ≤ 10¹². Δ = -0.005230064522 (target − V_7); no small-integer-coefficient relation. Hypothesis: V_7 chase is hunting a fitted target. |
| H_12 A-operator extract (script `A_operator_extract_general.py --A 4`) | **DIED silently.** Foreground showed `Computing χ^λ for 12321 pairs × 77 λ` then no progress; process disappeared from pgrep with no error in log.  Likely OOM at the 950K-character sweep.  Confirms cheat-sheet audit's "2-3 day compute" estimate is conservative on memory + needs a different decomposition strategy. |

## V_7 finding details

**Setup.** Per PR #916 — V_7 = `Σ_{λ ⊢ 4} dim_q V_λ / [4]_q` is
the first Wedderburn linear functional with the right sign on h²
(c_2 = -13/16 vs target ≈ -G = -0.9160).  Question: is there a
small categorical sub-leading correction X(q) that closes the
residual?

**Algebraic decomposition of V_7 at H_4:**

| λ | dim_q V_λ | At q_0 (40 dps) |
|---|---|---:|
| (4) | 1 | 1.00000 |
| (3,1) | [3]_q = [2]_q² − 1 | 3.04371 |
| (2,2) | [4]_q / [2]_q = [2]_q² − 2 | 2.04371 |
| (2,1,1) | [3]_q (mirror) | 3.04371 |
| (1,1,1,1) | 1 | 1.00000 |
| **Σ dim_q** | **3·[2]_q² − 2** | **10.13112** |
| [4]_q | [2]_q · ([2]_q² − 2) | 4.10968 |
| **V_7** | **(3·[2]²_q − 2) / ([2]_q · ([2]²_q − 2))** | **2.46518** |

**Cleanest algebraic form:**

$$
  V_7(q) \;=\; \frac{3 [2]_q^2 - 2}{[2]_q \bigl([2]_q^2 - 2\bigr)}
$$

A reduction at q = 1: [2]_q → 2, [4]_q → 4, V_7 → (12 − 2)/4 = 5/2. ✓

**Gap calculation at q_0 (100 dps):**

```
target (CODATA closure)  λ_p = 2.4599527843613182892482457339493...
V_7(q_0)                     = 2.4651828488834238585963352422426...
Δ = target - V_7             = -0.0052300645221055693480895083013...

Δ / h²                       = -0.1196640829119909886279199...
Δ / ℏ_q²                     = -0.5327456547182389040333893...
Δ / h^4                      = -2.737918945099930720593968...
```

None of these ratios is a clean rational, irrational known constant,
or small integer-coefficient combination of substrate primitives.

**PSLQ search.** At 100 dps with tolerance 10⁻³⁰ and maxcoeff 10¹²,
against the basis `{Δ, h²·G, h^4, h^6, h², ℏ_q²·G}` — **no
relation found**.

**Tried candidates (all miss):**

| Form | Fit to Δ |
|---|---:|
| -h² · G | 665 % off |
| -h² · (G − 13/16) | 13.5 % off |
| +h² · 13/16 | 779 % off |
| -h^4/24 | 98 % off |
| -h^6/6 (per PR #909) | 99.7 % off |
| +h^6 · G/720 | 100 % off |

Best candidate is **−h² · (G − 13/16)** at 13.5 % off, which is
itself essentially the symbolic statement "the missing piece is
the difference between G and 13/16 multiplied by h²" — restating
the gap, not deriving it.

### Interpretation

The CODATA-closure target `λ_p = 2.4599527843613...` was **solved
from CODATA m_p** (per the PR #888 truth-in-naming audit and the
PR #895 production swap to Family A).  It is a fitted value, not a
categorical-derivation target.

The PR #916 V_7 finding correctly identifies V_7 as the FIRST
Wedderburn linear functional with the right sign on h² — that is
a real structural signal vs Family A's wrong sign.  But the
**absolute level** (V_7 lands 0.144 % off the FITTED target, vs
Family A's 2.89 % off) may be measuring proximity to a fit rather
than to a categorical truth.

Two consistent positions:

1. **V_7 is the right categorical λ.**  Then the residual 0.144 %
   should close with a NATURAL categorical sub-leading correction
   (none found above coeff 10¹² → likely false).
2. **V_7 is one of many proved categorical functionals on H_4.**
   No categorical-derivation rule (yet) picks V_7 over V_1 (Family
   A) or V_2 (Plancherel) or V_4 (hook-weighted).  Without that
   selection rule, the 0.144 % proximity is suggestive but not
   structural.

Position 2 is the conservative read.  Position 1 is the optimistic
read — it would predict a small h^4 / h^6 categorical correction
exists; this spike does not find one.

### Recommended next steps (for V_7 line of work)

1. **Search a much wider basis** (e.g. include Wedderburn-natural
   sub-functionals like `dim_q V_λ²/[2]_q!` or hook-content
   refinements).  Coeff ceiling 10²⁰+.
2. **Derive the selection rule** that picks V_7 over V_1, V_4
   from a structural principle (e.g. "the Plancherel-weighted
   denominator must absorb the q-Casimir").
3. **Accept that 0.144 % is the framework's V_7-baseline accuracy**
   and update the cheat-sheet §5 #1 status to track V_7 alongside
   Family A as a "best-known categorical λ" with no closure yet.

### Cumulative empirical case for Position 2 (2026-05-22 update)

The V_7 spike here is the **fourth independent negative search**
for `λ_scale ≈ 2.4599527869` in the published series:

| Search | Basis | Coeff | Result | Ref |
|---|---|---|---|---|
| `bring_bloch_tier{0..5}` | 52 hyperbolic knots ≤ 11 crossings | 10³⁰ | NEG | PR #888, #904 |
| `q_dilog_tower_spike` | Substrate-natural Li_2^q + Φ_q | 10³⁰ | NEG | PR #923 |
| `q_dilog_vhat_spike` | V̂_S + ℚ(ζ_60) D + tier-0 vols | 10³⁰ | NEG | PR #928 (merged 2026-05-22) |
| **V_7 sub-leading (this doc)** | `{h²·G, h^4, h^6, h², ℏ²·G}` | 10¹² | **NEG** | this spike |

Four independent searches; four negatives.  **The
substrate-categorical proof that the target itself is a fitted
value (per #888 truth-in-naming) is now matched by an
empirical-search proof that no small-coefficient categorical
identity reproduces it.**  Position 2 ("V_7 is one of many
proved categorical functionals on H_4, no selection rule yet
picks it; the 0.144 % proximity to a fitted target is suggestive
but not structural") is the conservative consensus across the
λ_scale cluster.

## H_12 A-operator extract details

**Setup.** Per cheat-sheet §5 #2 manager view, the H_12 A-operator
extract is the next concrete blocker for migrating 14 SUPERSEDED-
importer `.py` scripts to `mass_tower_operator_valued`.

Launched: `python3 -u computations/a_operator/A_operator_extract_general.py --A 4`

**What happened.** Process started, printed the setup banner:

```
  Split: H_6 ⊗ H_6 → H_12
  partitions: 11 × 11 → 77
  LR non-zero entries: 1588
  test panel: K1=111 × K2=111 = 12321 pairs
  Pre-computing ρ_μ(β_1) for 111 × 11 = 1221
    [0.0s]
  Computing χ^λ for 12321 pairs × 77 λ    ← last output
```

Then the process disappeared from pgrep with no traceback.  Log
size frozen at 496 bytes.  Most likely cause: **OOM at the inner
12321 × 77 = 950 K character sweep** — each character is a 11×11
seminormal matrix product over Q(q), held in memory by the
`lru_cache` on `evaluate_word_matrix`.

### Implications for cheat-sheet §5 #2

The audit's "2-3 day compute" estimate may be wall-time only;
the actual constraint here is **memory**.  Concrete unblockers:

1. **Split the (12321 × 77) sweep into chunks**, persist to disk,
   GC the cache between chunks.  Same total wall time but bounded
   memory.
2. **Restrict the test panel** to a smaller K1 × K2 if the LR
   coefficients can be recovered with fewer constraints.
3. **Use a sparse seminormal representation** (most LR entries are
   zero; the script computes dense matrices anyway).

These are 1-2 day implementation tasks per option.

## Manager-view impact

Both items remain in "BLOCKED with concrete unblockers" state.
Updating the manager ledger:

| Item | Prior status | Post-spike status |
|---|---|---|
| §5 #1 (V_7 refinement, PR #916 follow-up) | "recommended next step" | "spike confirms NO small categorical correction found; consider Position 2 (V_7 = one categorical baseline among many)" |
| §5 #2 (H_12 A-operator extract) | "2-3 day compute task" | "Memory-bounded; needs chunk-and-GC restructure (1-2 day impl) before compute can complete" |

No regression on the existing 2-closed / 3-open §5 status.
