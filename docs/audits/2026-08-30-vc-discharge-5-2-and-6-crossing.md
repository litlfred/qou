# The 5₂ and 6-crossing volume-conjecture instances were already proven, and the papers were already in `library/`

**Date:** 2026-08-30 · **Bean:** `qou-ckbv`

## What changed

Four per-knot volume-conjecture instances move from open/partial to **proven**:

| Knot | was | now |
|---|---|---|
| 5₂ | "partial — case treated by Ohtsuki (numerical, not full proof)" | proven, `[ohtsuki2016-52]` |
| 6₁ | "partial / numerical only" | proven, `[ohtsuki-yokota-6crossings]` §3 |
| 6₂ | **open** | proven, same paper §4 |
| 6₃ | **open** | proven, same paper §5 |

**6₂ is the canonical ²H (deuteron) knot closure** in
`computations/substrate/knot_volumes.py`, so this is a load-bearing instance,
not a bookkeeping row.

## This was a reading gap, not a literature gap

Both papers were in `library/` the entire time:

- `library/104171-qt-83/` (published) and `library/ki52/` (preprint) — Ohtsuki
  on 5₂.
- `library/ki6c/` — Ohtsuki–Yokota on the 6-crossing knots.

`ki6c` was **already cited by the corpus**, in
`QOU/QBeta/GZThirdKnotRankGrading.lean`, for its saddle-point data and gluing
quartic — by an agent who used the paper's machinery without noticing that its
headline result discharges the volume conjecture for the knots it treats.

Meanwhile `b1-hyperbolic-rows-theorem-table2-data` recorded 6₂ and 6₃ as open
and 5₂ as "numerical, not full proof". That is not a stale status; it is the
opposite of what the papers say. Ohtsuki–Yokota's abstract reads: "In
particular, **we show the volume conjecture for these knots**, which states that
the leading terms of the expansions present the hyperbolic volume and the
Chern–Simons invariant of the complements of the knots." Sections 3, 4 and 5 are
each headed "Proof of Theorem 1.1 for the 6ₓ knot". The method is the saddle
point method plus the Poisson summation formula — asymptotic-expansion theorems,
not numerics.

The lesson for the corpus's citation discipline: `check-citation-keys.py` and
the no-fabricated-citation rule both police citations that are *missing or
wrong*. Neither can detect a citation that is present, filed, correct, and
**unread** — which is how a proven result sat next to a table calling it open.

## What did NOT change

- **8₁₁ (³H) is unaffected** and remains the load-bearing open instance. It is
  an 8-crossing knot and lies outside every family above; the 2026-07-17 audit
  ([`8-11-vc-open-and-id-unverified`](2026-07-17-8-11-vc-open-and-id-unverified.md))
  stands unmodified, as does its second open leg (the 8₁₁ = ³H assignment).
- **The chiral hyperbolic rows are still conditional**, but now for a different
  reason. Their VC leg is discharged; what remains open is the **depth-3
  Chern–Simons partner**, per
  [`prop:b1-figure-8-row-theorem`](../../content/quantum-observable-universe/appendix-surreals/b1-figure-8-row-theorem.md).
  Discharging VC does not by itself promote those rows to theorems, and the
  status table now says which leg is which.
- **7-crossing knots stay open here.** A seven-crossing sequel exists
  (*Internat. J. Math.* **28**(13), 2017) and was verified by web search, but it
  is not in `library/` and its authorship is not settled from the sources
  reachable in-sandbox (some list Ohtsuki alone, some Ohtsuki–Yokota). Under the
  no-fabricated-citation discipline a status upgrade should rest on a filed,
  read paper. **Follow-up: obtain it and re-run this check** — it would cover
  7₂, 7₃, 7₄ and the rest of the 7ₓ family, several of which sit in the Tier-1
  PSLQ basis.

## Scope note on the PSLQ basis

The KVC discharge survey's finding that "8₁₁ is the one genuinely open case"
holds for the four load-bearing mass/binding instances. It does **not** hold for
the Tier-1/Tier-2 PSLQ basis in
`computations/tier_{1,2}_hyperbolic_*_pslq.py`, which also contains 8₅, 8₁₀,
8₁₅, 8₁₆, 8₁₇, 8₁₈ — all open, all 8-crossing. After this change the basis
splits: 4₁, 5₂, 6₁, 6₂, 6₃ and the Borromean/Whitehead links are proven; every
8-crossing member is open. Worth stating explicitly before any Tier-3 extension
is read as resting on proven ground.
