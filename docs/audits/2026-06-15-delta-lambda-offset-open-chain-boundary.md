# The Δ_λ exponent offset is the open-chain boundary — keystone reduced to one number (2026-06-15)

**Branch:** `claude/vigilant-brown-x0tzat` (PR #2325)
**Owner ask:** *"chase the offset"* (the `−5` in `10A−5`; the `−3` crossing-vs-site puzzle).
**Result:** the offset is **derived** (open-chain boundary, pure algebra); the keystone
collapses to a **single** conjectural number — the per-site q-power `5` (Bring quintic).
Gate-respecting (no fit). **Not wired.**

## The offset dissolves under the chain-site reading

The canonical residual exponent factors exactly:

```
10A − 5  =  5 · (2A − 1)  =  5 · [  A   +  (A − 1) ]
                                  nucleons   bonds        (an OPEN A-chain)
```

- **Slope `10`/nucleon is forced.** Each nucleon adds 2 chain-sites (itself + one
  bond), so per-nucleon q-power `= 2 × 5 = 10` — independently matching the
  crossing slope `σ+σ⁻¹ = 10A−2` (A-only; `delta_lambda_exponent_from_crossings.py`).
- **The `−5` offset is the open-chain boundary, not a fit.** An open A-chain has
  `2A−1` sites — one fewer bond (`A−1`) than nucleons (`A`). The missing terminal
  bond is exactly `−1` site `= −5` q-power. A *closed* chain (A bonds) would give
  `5·2A = 10A`; the open chain gives `10A − 5`. Verified A=1..12
  ([`qlommel_offset_open_chain_site_law.py`](../../computations/qbeta/qlommel_offset_open_chain_site_law.py), 3 green).

## The "−3 puzzle" was a category error

Earlier framings compared the q-POWER `10A−5` with the crossing COUNT
`σ+σ⁻¹ = 10A−2` and called the difference `3` an unexplained offset. But a crossing
*count* and a q-graded *power* are different quantities; there is no reason they
should be equal, and their constant difference carries no q-power meaning. The
q-power is `5(2A−1)` directly (site law); the crossing count `10A−2` is a separate
combinatorial identity. No `−3` mystery survives.

## What remains open — exactly one number

The **sole** residual unknown is the per-site q-power magnitude `5` — the
**Bring-quintic conjecture** (Bring's surface `𝒳₅`, Aut `= S₅`; the same `5` as the
Weinberg cosh-ratio `(5,7)`). Confirming it needs the **q-graded Markov trace** of
the single-site sub-braid (the Rust hecke engine), which is out of scope in this
sandbox (the refactor moved the engine out of the content repo).

## Where this leaves the keystone

Combining this session's three results, the keystone `Δ_λ ≈ q₀^(10A−5)` is now:

| piece | status |
|---|---|
| recurrence `Δ_{A+1}=b·Δ_A−Δ_{A−1}` | **Lean-proved** (`two_root_geometric`, `two_seed_unique`) |
| `b = q₀¹⁰+q₀⁻¹⁰` from the slope | **derived** (`first_kind_geometric_b`; slope verified A=2..12) |
| slope `10`/nucleon | **derived** (`σ+σ⁻¹=10A−2`, 2 sites × 5) |
| offset `−5` | **derived** (open-chain boundary) |
| per-site `5` | **conjecture** (Bring quintic; needs q-graded trace) |

So the entire keystone reduces to proving **one** equality: per-chain-site q-power
`= 5`. That is the cleanest statement of what's left — a single number, with a named
mechanism and a concrete (trace-engine) test, not an open-ended "derive 10A−5 from
crossings." **Still near-match tier, NOT wired**: the binding *production* formula
remains gated on this number and on the +2.89% nucleon-mass gap.
