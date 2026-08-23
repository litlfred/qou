---
# qou-c1ya
title: y_lambda orphan family inherits a 17-digit q0 that is 2.84e-12 off the muon pin
status: todo
type: task
priority: normal
created_at: 2026-08-23T19:52:19Z
updated_at: 2026-08-23T19:53:04Z
---

## What was found

Surfaced while draining tier C of the derivation-chain gap (`dgpc`): the
`wenzl-y-lambda-h9/h12` witnesses record

    parameters.q0 = 1.10997859555418057528159407960950937799328227995870

which is **not** the canonical ideal-CAL-2 (muon) pin

    1.10997859555733471989976322048322502665620840878015368660798114614493

They agree to 12 significant digits and then diverge: `…5955 5418…` vs
`…5955 5733…`. Relative separation **2.84e-12**.

## Get the units right — this is a PRECISION defect, not a LAYER defect

My first framing of this was wrong and is not repeated here: 2.84e-12
relative is **0.00284 ppb**, so it is roughly **4000× SMALLER** than the
11.5 ppb μ–p substrate tension, not larger. Nobody confused the muon layer
for the proton layer. What it *is*:

| against | ratio |
|---|---|
| μ–p substrate tension (11.5 ppb) | 0.00025× — invisible beside it |
| L1 compute-precision target (1 ppQ = 1e-15) | **2840×** — well above |

So the physics conclusions do not move; the corpus's own precision claim
does. Confirmed by pushing it through the anchor equation
`m_μ/m_e = Vol(4₁)/ℏ_q²`: the bad pin implies `206.768283` against the
canonical `206.768282989315`, a 5.2e-11 relative difference in the ratio
(≈18× amplification of the q₀ separation). Not a CODATA-vintage difference
either — those are ~1e-8 in the ratio.

## Where it comes from — NOT from the convention-D regeneration

`git log` on the witness shows the value predates
`1ab204f8ed` ("bring the orphan y_lambda witnesses to convention D"). The
regeneration producer preserved it **correctly**, per its own documented
policy of using each file's own pin so that only the convention moves and
the ideal/experimental layer is left alone. The bad value is inherited from
the **producerless original** — which is exactly the hazard `qou-rohl`
described: a witness nothing writes is a permanent upstream, and here it
carried a stale pin as well as a stale convention.

One 17-significant-digit ancestor `1.1099785955541805` sits under all of it.
Each file pads it to 50 digits with a *different* float64 noise tail —
h9/h12 end `…7528159407960950937799328227995870`, the wenzl-bridge file ends
`…1695830018898879867637876138498395` — and the tails diverge at digit 18,
which is precisely where float64 runs out.

## What was fixed here (PR on `claude/derivation-chain-c-tier-drain-2026-08-23`)

The producer had canonised the ancestor as a module constant,
`MUON_Q0 = "1.1099785955541805"`, used as the fallback for any target file
that states no q₀ of its own. That fallback is **exercised**, and by the
larger share of the corpus:

| target | q₀ source | weights |
|---|---|---|
| `y-lambda-wenzl-witness.json` | **fallback** | 28627 |
| `y-lambda-symbolic-witness.json` | **fallback** | 20 |
| `wenzl-y-lambda-h9` / `h12` | own field | 30 / 77 |
| `y-lambda-wenzl-bridge-numeric` | own field | 3190 |

Replaced with the canonical 50-digit muon string and regenerated. Measured
effect: **254 nonzero weights moved**, max **5.22e-11** relative at λ=(30)
— the rest of the 28627 are the `ℓ(λ) ≥ 3` exact zeros convention D forces,
unchanged. `y-lambda-symbolic-witness.json` did not move at all, being
symbolic. `Σ_λ dim_λ·y_λ = 1` re-verified on every rewritten table by the
producer's own gate; `scripts/precision-gates.sh --changed` green.

## What is left OPEN — the three files that state their own pin

`wenzl-y-lambda-h9`, `wenzl-y-lambda-h12` and
`y-lambda-wenzl-bridge-numeric` still carry the inherited 17-digit pin,
because the producer honours a file's own q₀ and that rule is the right one
for a convention migration. Correcting them means **overriding** it.

Deliberately not done as a drive-by:

- It changes committed `y_λ` values that **six live nuclear consumers**
  read (`nucleus_real_sdp.py`, `probes/frobenius_gram_delta_lambda_probe.py`,
  the two `habiro/habiro_h9_*`, the two `deltalambda/he4_binding_k_*`) —
  tritium and ³He at H₉, ⁴He at H₁₂. Binding energies, not a side probe.
- Three sibling PRs are live on q₀ pinning right now (#5500, #5519, #5573).
- Both h9/h12 entries are currently suppressed in
  `computations/q0-drift-baseline.json::parameters.q0`. **Those two
  baseline lines are the drain target** — AGENTS.md is explicit that
  baselines drain and never grow, so the close condition is removing them
  because the value is right, never because the check was widened.

Suggested shape: an explicit `--upgrade-q0-precision` flag on the producer,
run once, with the six consumers' outputs diffed before and after so the
~5e-11 movement is recorded rather than discovered.

## Close condition

All three remaining files carry the canonical 50-digit muon pin, their two
`q0-drift-baseline.json` entries are **removed** (not re-baselined), and the
consumer-side movement is measured and recorded.
