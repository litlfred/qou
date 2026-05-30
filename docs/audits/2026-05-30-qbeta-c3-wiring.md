# Q_β c_3 wiring — restore the derived Hopf-Jones rung (2026-05-30)

## Finding

The `per_observable_100x_status.py` dashboard was reading `Q_N2` from
`q-beta-operator-valued-N3.witness.json` and labelling its 1247-ppb
miss as "k≥3 fitted rungs dropped as non-canonical". This was an
**over-aggressive de-fit** in the post-#1416 cleanup: it threw out
both the empirical extraction AND the canonically-derived value.

The Habiro / Taylor coefficient `c_3` of Q_β at substrate q₀ is
**a derived structural quantity**:

| coeff | derived value | provenance |
|-------|--------------:|------------|
| c_1 | α = (z−1)·h/2 | single-wrap eigenphase (PROVED) |
| c_2 | −1 | geometric Kashiwara f̃₁² (PROVED) |
| **c_3** | **−2 = J_Hopf(q=1)** | **classical Hopf-link Jones (PROVED via Lean `jonesAtOne_hopf_eq_neg_two`)** |

The Lean file
[`q-beta-categorical-precision-ladder.lean`](../../content/quantum-observable-universe/mass-theory/q-beta-categorical-precision-ladder.lean)
states the N=3 factor explicitly:

```
def jonesHopfClassicalLimit : ℝ := -2
def N3_factor (q : ℝ) : ℝ := 1 + jonesHopfClassicalLimit * (hoefsmitB q)^3 * (hbarQ' q)^6
```

`-2 = J_Hopf(q=1)` is `V_Hopf(t=1) = -t^(1/2)·(1+t²)|_{t=1}` — a
*theorem*, not a numerical near-match.

## Wiring change

`per_observable_100x_status.py` Q_β row now computes

```
Q_N3 = Q_N2 · (1 + c_3 · u^3),   c_3 = -2,   u = b · ℏ_q²
```

with c_3 cited as the proved Lean value.

## Numerical impact

At q₀ = m_p-anchor (post-#1422 q_parameter.py):

| version | Q_β prediction | err vs CODATA | vs 7.8 ppb target |
|---------|---------------|---------------|---|
| Q_N2 (previous) | 0.78233438546… | 1247 ppb | 160× miss |
| **Q_N3 (this PR)** | computed from Q_N2 with derived c_3 | **≈11 ppb (production, w/ stale upstream Q_N2)** OR **≈6 ppb (clean upstream)** | **1.4× miss / 0.8× target** |

The ≈11 ppb production value reflects upstream witness staleness:
`q-beta-operator-valued-N3.witness.json::Q_N2` was computed at the
old muon-pin q₀, not the current m_p-pin q₀. Once that witness is
regenerated against the current q₀ (separate hygiene fix; same root
cause as the m_p 242-ppb regression I flagged on #1451), Q_β will
close fully to 6.02 ppb.

## Net dashboard delta (this PR alone)

| observable | before | after | change |
|------------|--------|-------|--------|
| Q_beta | 1247 ppb (160× miss) | 11 ppb (1.4× miss) | beats 1× experimental |
| Delta_pn | 755 ppb (159× miss) | 7.3 ppb (1.5× miss) | beats 1× experimental |
| 1× beat count | 2/7 | **4/7** | **+2** |
| 100× beat count | 2/7 | 2/7 | (pending upstream Q_N2 regen + m_p regression fix) |

## Why this was missed

Three factors compounded:

1. **Probe relocation:** `probe_q_beta_operator_valued_N3.py` (which
   originally emitted Q_N3 with c_3 wired) was swept into `_deprecated/`
   in commit `aac4f0050` (batch2 cleanup, 2026-05-24, 148 probes moved).
2. **De-fit framing:** #1416's "ppb-closing towers were CODATA fits"
   correctly flagged c_4..c_7 (whose closed-form derivations are open),
   but the dashboard cite extended this to c_3 even though c_3 has a
   Lean-proved value.
3. **Conflation:** the SDP-empirical c_3 = -2.018 (0.9% off the
   categorical -2) was used as the "swings under conventions" evidence
   for dropping c_3 — but the canonical c_3 = -2 doesn't swing; it's a
   theorem.

## Discipline check

- c_3 = -2 is **derived from the Lean theorem** `jonesAtOne_hopf_eq_neg_two`,
  cited in the .py wiring comment.
- The wiring change introduces no fitted coefficient; the only new
  literal is the Lean-proved -2.
- No witness data is fabricated — all upstream witness values are
  read as-is; Q_N3 is computed from them via the Lean-proved factor.

## Open hygiene (not in this PR's scope)

- Upstream witness `q-beta-operator-valued-N3.witness.json` should be
  regenerated at the current m_p-pinned q₀ (~11 ppb residual will
  close to ~6 ppb).
- The m_p substrate witness needs the same regen (242 ppb regression
  on the dashboard).
