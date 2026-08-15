---
# qou-m9xp
title: 'q-pinning-50-digit witness self-contradicts: q0Anchor=muon but calibration_inputs.anchor=m_p/m_e'
status: todo
type: task
priority: normal
---

## The contradiction

`computations/q-pinning-50-digit.witness.json` states its anchor **both ways**:

| field | value |
|---|---|
| `.q0Anchor` | `muon` |
| `.q0Value` | `1.1099785955573347198997632…` ← the **muon** value |
| `.derived_50_digit.q` | `1.1099785955573347198997632…` ← the **muon** value |
| `.calibration_inputs.anchor` | **`m_p/m_e`** ← proton |
| `.physical_anchoring_bound.anchor` | **`m_p/m_e`** ← proton |

The *numbers* are muon throughout; two *metadata* fields say the calibration
input was the proton ratio. Both cannot be true. A reader checking the anchor
gets whichever answer they happen to grep for.

For reference the two pins differ by **11.54 ppb** — the μ–p substrate tension
itself:

    muon   q0 = 1.1099785955573347
    proton q0 = 1.1099785827513808
    relative  = 11.54 ppb

## Why it matters now

`computations/alpha/alpha_k_jones_markov_h12.py` reads this witness for its
substrate constants:

```python
Q_PIN  = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
q0_mpf = mp.mpf(record_upstream(Q_PIN, _UPSTREAM_RECORDS)["derived_50_digit"]["q"])
q0_f64 = float(q0_mpf)
h_f64  = float(q0_mpf - 1 / q0_mpf)
z_mark = q0_mpf**3 / (q0_mpf**2 + 1)
```

So `q0`, `h` and the Markov parameter `z` are all **muon**-pinned there, while
the owner directive of 2026-08-07 makes the **proton/experimental** pin the
default for all agents and all production code, and the rest of the surface
this producer sits in has moved: `y-lambda-at-q0.witness.json` now records
`parameters.q_0 = 1.10997858275138080759…`, i.e. **proton**.

`alpha-k-jones-markov-h12` is also one of the remaining convention-C
witnesses (`qou-lt8x`). Migrating its C→D convention **without** settling the
pin would produce a quantity that straddles: convention D evaluated at the
muon anchor, feeding a corpus that is proton elsewhere. AGENTS.md
§"q₀ anchor convention" is explicit that straddling is a defect regardless of
its size, and the measured cost of the last straddle was this same 11.54 ppb.

## Note for AGENTS.md currency

AGENTS.md §"q₀ anchor convention" rule 2 says the `computations/` layer
"historically carries **muon-q₀** witnesses:
`…/q-pinning-50-digit.witness.json` holds the muon value". That is still
accurate for *this* file — but the **companion claim is now stale for
`y-lambda-at-q0`**, which has been rebuilt at the proton pin. The straddle
hazard the rule describes (cache muon-built, caller passes proton `Q`)
therefore does **not** apply to the y_λ cache any more. Worth correcting when
someone next touches that section, so a reader does not avoid a hazard that
has already been removed — or, worse, assume the remaining muon files were
migrated too.

## To close

1. Decide which anchor this witness records, and make all five fields agree.
   The value is muon; the `calibration_inputs.anchor` / `physical_anchoring_bound.anchor`
   fields saying `m_p/m_e` are the ones that look wrong.
2. Decide whether `alpha_k_jones_markov_h12` should stay muon-pinned (it is an
   ideal-layer 3-CAL computation) or move to proton (the standing default for
   compute). Record the choice **in the producer**, not only here.
3. Only then migrate its convention C→D, so the result is not a straddle.

Found while answering a direct question about whether this session's work used
the correct pin. The work committed so far — `probe_1b_li6_orthogonality`, via
`y_lambda_at_q0_mpmath(18, q_parameter.Q)` — is **proton**, verified. This
producer is the next one on that list and is not.
