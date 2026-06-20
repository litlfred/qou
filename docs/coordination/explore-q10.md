# Q^10 selectivity exploration — coordination ledger

**Goal:** Identify the categorical / structural reason why the
substrate-natural power `n = 10` is selectively picked out in
the recent finding `1 / (1 − h_q · q_0^{10}) ≈ λ_p` (PR #943).

**Owner branch:** `claude/iw-explore-q10-2026-05-23`
**Started:** 2026-05-23

## Background

PR #943 (merged 2026-05-22) established that the Faddeev
quantum-dilogarithm functional-equation form

```
1 / (1 − h_q · q_0^{10})  =  2.4599992316…
                          ≈  λ_p  =  2.4599527843…   (+19 ppm)
```

with `h_q := q − 1/q ≈ 0.20906`, `q_0 ≈ 1.10998`, lands within
**19 ppm** of the CODATA target. The integer power `n = 10` is
strikingly selective — adjacent powers `n = 9, 11` give 13% and
19% relative error.

## Structural connection found in existing content

**Source:** [`markov-trace-antipode-polynomial-symmetry.md`](../../content/quantum-observable-universe/braids-and-knots/markov-trace-antipode-polynomial-symmetry.md)

The proton braid `𝓑_p ∈ B_3` (the canonical braid used in
`prop:atomic-mass-gb-nf`) has closed-form Markov trace:

```
tr_M(𝓑_p)  =  p(q) / (12 · q^{10})
p(q)       =  q^{20} + q^{18} + 2 q^{12} − 2 q^{8} − q^{2} − 1
```

with the antipode-induced polynomial symmetry

```
q^{20} · p(1/q)  =  −p(q)
```

i.e. `p` is anti-self-reciprocal of degree 20, centered at `q^{10}`.

**The integer `10` is the antipode-balance center of the proton
braid's Markov trace polynomial.** It is not a fitted power — it
is dictated by the braid's degree-20 structure.

The composite `h_q · q^{10} = q^{11} − q^{9}` is the bilateral
excursion *adjacent* to this center, with `q^{11}` and `q^{9}`
sitting symmetrically about the q^{10} balance point.

## Sibling-PR scope map

| PR | Branch | Classification | Overlap | Coordination |
|---|---|---|---|---|
| #916 | `lambda-scale-alts-strategy-d-2026-05-22` | strategy enumeration | **strong** | [intent posted](https://github.com/litlfred/qou/pull/916#issuecomment-4525066386) |
| #909 | `keen-maxwell-jqdPU` | Strategy D stage-1 + ε residual | **strong** | [intent posted](https://github.com/litlfred/qou/pull/909#issuecomment-4525067011) |
| #917 | `per-observable-100x-refresh-2026-05-22` | 100× dashboard | weak (status pinning) | none |
| #920 | `cheat-sheet-tracker-2026-05-22` | §5 manager tracker | weak (status pinning) | none |
| #921 | `closed-form-tau-M-refactor-2026-05-22` | tr_M speed refactor | medium (uses `tr_M(𝓑_p)`) | watching |

## Hypotheses

1. **H1 (most likely):** The `n=10` selectivity is dictated by the
   proton braid's antipode-balance center (degree-20 polynomial
   symmetry). The 19 ppm residual is *not* a fit; it is a sub-leading
   correction in the Φ_q functional-equation expansion that is
   structural (Demazure-fibre / non-symmetric Macdonald) rather
   than empirical.

2. **H2:** The form `1/(1 − h_q · q^{10})` is the leading term of
   a `Φ_q` infinite product `Φ_q(h_q · q^{10}) / Φ_q(h_q · q^{11})`
   whose subsequent factors contribute the 19 ppm residual. If true,
   computing more factors should close the gap.

3. **H3 (null):** `q^{10}` happens to satisfy `h_q · q^{10} ≈ 1 −
   1/λ_p` numerically at substrate `q_0 ≈ 1.110` by coincidence —
   no categorical content. Falsifiable by checking smoothness of
   `1/(1 − h_q · q^{10}) − λ_p_codata(q)` across the substrate
   window `q ∈ [q_0 − ε, q_0 + ε]`.

## Plan (in priority order)

- [ ] **Q-locality sweep** — verify the 19 ppm residual is
  *not* a coincidence by checking smoothness across `q ∈
  [q_0 − 0.02, q_0 + 0.02]`. Per #909's discipline (`"q_0 not
  special"`), the residual `λ_p_codata(q) − 1/(1 − h_q · q^{10})`
  should be a smooth function of q across the window.

- [ ] **Φ_q tower expansion** — compute the FULL Φ_q expansion
  `Φ_q(h_q · q^{11}) / Φ_q(h_q · q^{10})` and identify the
  sub-leading correction. Distinguishes H1 vs H2 — if H1, the
  correction is structurally tied to the braid; if H2, it
  decays geometrically.

- [ ] **Adjacent-power probes** — test
  `1/(1 − h_q · q^{10}) − 1/(1 − h_q · q^{12})/c_{12} −
  1/(1 − h_q · q^{8})/c_{8}` with weights `c_{8}, c_{12}` from
  the `p(q)` polynomial coefficients `q^{12}` and `q^{8}`
  (from `2q^{12} − 2q^{8}`). Categorically natural composite.

- [ ] **Cross-check against tr_M(𝓑_p)** — verify that
  `tr_M(𝓑_p) · F(q_0) ≈ λ_p` for some structural `F` involving
  `1/(1 − h_q · q^{10})`. If yes, the connection is direct.

## Anti-patterns (do not)

- Do NOT fit a 7th-order ansatz to close the 19 ppm gap. Per
  AGENTS.md, `Δ_λ` gate fit-bans apply: any closed-form must
  carry categorical justification, not curve-fitting.
- Do NOT pivot to PSLQ over h-powers — PR #909 stage 2 owns
  that work. Coordinate via the comment on #909.
- Do NOT promote `1/(1 − h_q · q^{10})` to `proposition` or
  `definition` content-block status unless the 19 ppm residual
  closes structurally OR the residual is shown to be a clean
  Φ_q functional-equation tail.

## Resolution criteria

This investigation **closes positively** (i.e. opens a follow-up
content-block PR) iff:
- The q-locality sweep shows the residual is a smooth function of q
  (not a substrate-`q_0` accident), AND
- Either (a) the Φ_q functional-equation tail closes the residual
  to < 1 ppm at substrate, OR (b) a categorical composite
  involving `tr_M(𝓑_p)` and `1/(1 − h_q · q^{10})` closes to
  < 1 ppm.

This investigation **closes negatively** (i.e. records as
empirical exhaustion alongside PR #923/#928/#941/#943) iff:
- The residual is sensitive to small q perturbations (H3
  falsified the structural-connection hypothesis), OR
- The Φ_q tail does not close the 19 ppm gap AND no
  categorical composite closes it either.
