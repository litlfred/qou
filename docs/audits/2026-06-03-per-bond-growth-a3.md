# Per-bond growth confirmed — embedded A=3 bonds are +16–20% stronger

**Status:** FINDING (reproducible, no fit). The C(A,2) multiplicity bond sum
closes A=3 to −15% (PR #1754); the residual is **per-bond growth** — bonds
inside the dense A-nucleon braid being stronger than the isolated 2-nucleon
bond. This probe measures it directly via the Rust kernel.

Probe: [`per_bond_growth_a3.py`](../../computations/per_bond_growth_a3.py)
(witness `per-bond-growth-a3.witness.json`).

## Method (no fit)

For each chain interface `I_b` in the H₉ atom, the **embedded** bond is the
per-block marginal of adding just that interface to the 3-nucleon free braid
(the other nucleon present as a spectator):

`B_b^emb = E_0·( perblock(W_free) − perblock(W_free + I_b) )`

vs the isolated H₆ bond `B_b^iso`. χ at H₉ via `pyhecke_native` on custom
`(c,d,gen)` words. Growth = `B_b^emb / B_b^iso`.

## Result

| nucleus | bond (position) | B_emb | B_iso | growth |
|---|---|---|---|---|
| T | pn (gen 2, early) | 2.320 | 2.305 | 1.007× |
| T | **nn (gen 5, deep)** | 2.701 | 2.250 | **1.201×** |
| ³He | pp (gen 2, early) | 2.200 | 2.286 | 0.962× |
| ³He | **pn (gen 5, deep)** | 2.672 | 2.305 | **1.159×** |

## Verdict

- **Per-bond growth is real and position-dependent.** The deeper chain bond
  (more spectator strands before it) is **+16–20%** stronger than isolated —
  precisely the scale of the −15% A=3 residual. The early bond barely moves
  (≈0%); the early pp even shrinks slightly. So the enhancement scales with
  **embedding depth** (how many strands the bond is braided through).
- This is the missing mechanism behind the −15% residual: the isolated-bond
  multiplicity sum undercounts because real bonds sit *inside* the dense
  braid and are strengthened by it.

## Toward closure (still open, no fit)

Exact A=3 closure needs **both** the full C(A,2)=3 pair multiplicity **and**
each bond's embedding growth — but the canonical braid is a **chain** (A−1=2
adjacent interfaces; the 1-3 pair is absent), so the chain gives only 2
embedded bonds (sum 5.0 MeV for T, −41%, worse than the 3 isolated bonds).
The clean closure is an **embedded all-pairs (C(A,2)) sum** with
position-derived growth — i.e. combine this session's two confirmed pieces
(multiplicity + per-bond growth) into one operator-valued combiner over all
pairs at their embedding depths. That combiner is the next concrete step;
the magnitude is now bounded (growth ≈ 1.16–1.20 on deep bonds), so it is a
derivation, not a fit.
