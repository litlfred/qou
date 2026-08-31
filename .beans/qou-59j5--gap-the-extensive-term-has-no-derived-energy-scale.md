---
# qou-59j5
title: 'GAP: the extensive term has no derived energy scale -- m_e vs E_0 moves it 8.19x'
status: todo
type: task
priority: high
created_at: 2026-08-31T04:13:26Z
updated_at: 2026-08-31T04:13:26Z
---


## The finding

The Markov normaliser `Z(n) = (1+q₀²)ⁿ` is a **dimensionless** partition
function. Turning `log Z` into MeV needs an energy, and **the framework does not
derive one**. Two different scales are in current corpus use and they differ by

    E₀ / m_e  =  1 / (q₀(q₀ − 1))  =  8.1917611722

| scale | value | used by |
|---|---|---|
| `m_e` | 0.51100 MeV | my three extensive-term probes, this session |
| `E₀ = m_e/(q₀(q₀−1))` | 4.18598 MeV | `computations/b_over_a_evaluator.py` ("Hadronic energy unit", the scale of every B/A prediction there); the `B_sym` linear chain, where `α = E₀` is CAL-1; the ROAST's own `E₀ log N` |

Every "the extensive term is short by ~7×" statement in this lane is **that
ratio**, not a measurement. `m_e` is the outlier and it is mine — I never gave a
reason for it. `E₀` is the corpus's, but it is CAL-1, a *calibration*, not a
derivation. So neither side is pinned, and until one is, no `N×` claim about the
extensive term means anything.

This is the ROAST's own §A1 complaint — "choosing the member that lands on the
target IS a fit" — one level up, applied to the units rather than to the
normalisation convention. I made exactly the error I was auditing.

⚠ **`E₀` is an overloaded name.** `computations/atom_mass_derived.py` defines
`E0_MEV = m_p / tr_M(proton) = 1662.7295 MeV`, a factor **397.21** away and a
different object entirely (it belongs to the absolute-mass chain excised
2026-08-11, bean `qou-exam`). Say which `E₀` you mean.

## The numbers, corrected

Probe: `computations/probes/extensive_term_energy_scale_reconciliation_probe.py`
(4 assertions, all passing).

At `E₀`, 3 strands/nucleon, over the normaliser convention family:

    8.722 … 11.597 MeV/nucleon      (at m_e it was 1.065 … 1.416)
    vs B/A plateau 8.5   →  1.03× … 1.36×  OVER      (was 6.0–8.0× short)
    vs a_V 15.8          →  1.36× … 1.81×  short     (was 11–15× short)
    family span          →  1.33×,  the SAME SIZE as the deficit

## Two verdicts this overturns

* **`qou-78pt` — WITHDRAWN.** "A1 REFUTED" rested on span 1.33× being two orders
  of magnitude smaller than a 6–15× deficit. Corrected, span ≈ deficit, which is
  exactly the condition that makes choosing a member a fit. **A1 reverts to
  "unfalsifiable as written"** and the ROAST was right the first time: pinning
  the convention from the axioms is the actual work. Probe docstring, witness
  and verdict all annotated in place; the original text is kept so the
  retraction has something to point at.
* **`extensive_counter_family_probe`** — its `no_family_member_reaches_plateau`
  assertion is renamed `..._AT_THE_m_e_SCALE` and is **false** at `E₀` (family
  max 46.39 MeV/nucleon). The conclusion "the missing factor is neither a
  normalisation nor a counter" is withdrawn.

**`qou-imcd` survives.** Its exponent test is scale-free — a constant multiplier
cannot change a log–log slope — so `log Z(3A)` is still exactly linear in `A`
and the braid→nucleus map is still not the defective step. Only its `6.906×`
residual figure is withdrawn.

## The unreconciled ROAST number, resolved

`markov_normalisation_convention_span_probe` logged an open discrepancy: the
ROAST's "~2.91 MeV/strand" against my 0.355–0.472, with "the ROAST does not show
its construction". It does, one sentence earlier — *"the extensive coefficient is
`E₀ log N`"* — and

    2.91 / E₀ = 0.695176   vs   ln 2 = 0.693147     (0.3 %)

while at `m_e` the figure is **unreachable**: it would need a normaliser with
`log = 5.695`, against a family whose logs span 0.694–0.923. Failing to
reproduce it was the tell, and I filed it as "unreconciled" instead of chasing
it. That is the lesson worth keeping from this bean.

*(Not fully determined: `E₀·ln 2 = 2.9015`, and the ROAST wrote `2.91`, which is
also exactly the `B_sym` chain's per-bond constant `b_pp = 2.91` — same `α = E₀`.
The documents do not distinguish the two, and it does not matter here: both are
`E₀`-scaled. If it was `b_pp`, the ROAST also mislabelled a **per-bond** constant
as **per-strand** and then multiplied by 3 strands/nucleon.)*

## What would actually close this

A derivation of the energy scale from the axioms, not a calibration. Candidates
to test, in order of how much structure they would need:

1. **Is `E₀ = m_e/(q₀(q₀−1))` derivable?** It is currently CAL-1. `q₀(q₀−1)` is
   not an obvious partition-function quantity; find out whether it is one.
2. **Does the scale cancel in a ratio?** Every L2 *ratio* observable (`m_μ/m_e`,
   `m_K/m_π`) is scale-free by construction, which is why they were never
   affected. If the extensive term can be phrased as a ratio to something else
   extensive, the question dissolves. `B/A` against `a_V` is not such a ratio —
   both carry MeV.
3. **The `B_sym` per-bond route as the cross-check.** `b_pp/b_pn/b_nn =
   2.91/3.89/5.18` (log form) and `2.38/2.49/2.53` (signed form) are two
   different functors of the same trace agreeing on the chain structure. They
   use the same `α = E₀`, so they do **not** independently pin the scale — but
   the ratio `b_nn/b_pp = 1.78` is scale-free and is a real prediction.

Do **not** report another "N× short" figure for the extensive term until (1) is
settled either way.
