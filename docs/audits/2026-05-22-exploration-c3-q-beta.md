# Q_β c_3 sub-leading search — exploration spike

**Date:** 2026-05-22
**Branch:** `claude/cheat-sheet-tracker-2026-05-22`
**Trigger:** Manager view notes Q_β at **11.13 ppb miss-factor 1.4×**
is the closest Subgoal-1 100× target.  This spike investigates
whether the gap closes categorically.

## Setup

Q_β prediction chain in `per_observable_100x_status.py`:

```
Q_N3 = Q_N2 · (1 + c_3 · b³ · ℏ_q^6)
```

with `c_3_categorical = -2 = J_Hopf(q=1)` (Hopf algebra, proved
in `prop:tau-M-asymptotic-rep-theory` per the N3 witness).

The `q-beta-operator-valued-N3.witness.json` also reports
`c_3_empirical_additive = -2.0097397609790...` — the value that
makes Q_N3 match CODATA exactly (a fit).

Gap on c_3:

| | value |
|---|---:|
| c_3 categorical (Hopf, proved) | -2 |
| c_3 empirical (CODATA fit) | -2.0097397610 |
| Δc_3 | **-0.0097397610** |

## PSLQ at 100 dps

Searched against the natural-substrate basis
`{h², h²·G, h^4, h^4·G, h^6, ℏ_q², ℏ_q²·G, ℏ_q^4, ℏ_q^3}` at
maxcoeff 10¹⁵, tolerance 10⁻²⁵:

**No relation found.**

Best candidate near-coincidences (all 2-3 % off):

| Form | Value | Fit |
|---|---:|---:|
| `-1/100` | -0.01 | 2.67 % off |
| `-h²·G/4` | -0.01001 | 2.76 % off |
| `-h²/4` | -0.01093 | 12.18 % off |

After subtracting either of the leading candidates, the residual
(~+2.6 × 10⁻⁴) **also has no clean PSLQ relation** in extended
basis `{h^4, h^4·G, h^6, h^6·G, ℏ_q^4, ℏ_q^4·G, ℏ_q²·G, h²·G², 1/q²}`
at maxcoeff 10¹².

## Findings

1. **Q_β at 11.13 ppb (with c_3 = -2 categorical) IS the
   framework's honest prediction at the current closure layer.**
   The 7.8 ppb 100× target requires either:
   - A different PROVED categorical c_3 value (open research), or
   - A different N=3 formula structure (operator-valued tower
     beyond Hopf — open research).

2. **The "closure value" c_3_empirical = -2.0097397610 is a fitted
   value**, in the same sense as λ_p = 2.4599527869.  It exists in
   the cheat-sheet's mental model as a "target to derive" but
   shares the same now-cumulative empirical-search refutation as
   the λ_p ladder:

| Search target | Status |
|---|---|
| λ_p Bring-Bloch hyperbolic-knot basis (PR #888 + #904) | NEG, 6 tiers |
| λ_p substrate-natural q-dilog (PR #923) | NEG, 80 dps |
| λ_p V̂_S + ℚ(ζ_60) + tier-0 vols (PR #928) | NEG, 80 dps |
| V_7 sub-leading (this session) | NEG, 100 dps |
| **c_3 Q_β sub-leading (this exploration)** | **NEG, 100 dps** |

   Five independent searches; five negatives.  Position 2
   (categorical theory is internally consistent but does not
   reach CODATA-target precision via small-coefficient extensions)
   is now the consensus across multiple observables.

## Manager-view impact

Q_β's 1.4× miss on the 100× target is **structurally similar to
m_p's 3 % miss**: both are bounded by the framework's actual
PROVED categorical predictions (Hopf c_3 = -2; Family A
λ_A = 5/2 + 3h²/4), not by a missing categorical refinement we
haven't found yet.

The closure targets

  | observable | target | framework | gap |
  |---|---|---|---|
  | Q_β 100× | 7.8 ppb | 11.13 ppb | **1.4× miss** |
  | m_p 100× | 3 ppt | 3 % (29 605 ppm) | 10¹⁰× miss |

are both fit-derived.  The framework's PROVED accuracy at each
layer is the *honest* prediction we should report, and the cheat-
sheet §5 #1 / Subgoal-1 plan should be reframed accordingly:

- **Subgoal-1-achievable items**: m_e (anchor), m_μ (0.06 ppb ✓),
  Δ_pn (after flavor_split_subleading wires).
- **Subgoal-1-bounded items**: Q_β (11.13 ppb is the framework
  bound, not a closure target), m_p / m_n (3 % is the framework
  bound).

This is a research-direction finding, not a code fix.  Nothing
to ship today; the audit doc records it for the manager ledger.

## Recommendation

Update the manager ledger Q_β row from "1.4× miss" to "framework-
bounded at 11.13 ppb" — the wording matters for future agents
who would otherwise spend time on the same negative-result
search this spike just completed.
