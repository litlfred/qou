# Exotic-signed Lusztig escape — N4: the |Σ|~40 requirement is a divisor artifact (owner-authorized)

**Date:** 2026-07-07 · **Bean:** `8z8k` · **Owner-authorized:** 2026-07-07 ("1 2" — pursue the last c_3 escape)
· **Axis:** Q_β c_3 / z→c_k f-map keystone · **Tier:** structural-exact · **Verdict:** N4 NARROWING (scope-(a))

## Context

The exotic-signed Demazure-Lusztig variant of the Composite-1 ansatz is the last
open item on the cont.9 KLR menu — the only theoretical escape from the c_3
CAL-3-anchoring, flagged "research-grade, specifying a convention is itself a
research task"
([scope doc](../scope/2026-06-06-qbeta-klr-exotic-signed-lusztig-bounded-magnitude-scope.md),
narrowings N1 magnitude / N2 saturation / N3 cross-anchor rigidity). The owner
authorized pursuing it. Rather than scan exotic conventions (open-ended), this
tranche applies formalize-first pruning — find the invariant that closes the
escape at physical rank.

## N4 — the magnitude requirement is an artifact of the wrong mechanism

The Composite-1 ansatz `F(u) = Σ_w D_w(λ)·(q;q)_{ℓ(w)}·u^{ℓ(w)}` reads `c_2` off
the `u²` rung: `c_2 = (q;q)_2 · Σ_{ℓ(w)=2} D_w`. Since `(q;q)_2 ≈ 0.0255` at q₀,
matching `c_2 = −1` demands `Σ D_w ≈ −39.4`. **That large target is an artifact
of routing `c_2` through the tiny `(q;q)_2` divisor** — precisely the `u`-series
re-expansion mechanism that **KC17** (the B3-U obstruction) showed does not carry
fibre parity to the `c_k`. And `c_2 = −1` is *already proved* by an independent,
non-`u`-series mechanism (Kashiwara f̃₁², `q-beta-c-2-eq-neg-one-structural.lean`;
re-derived via the eval-map counit decomposition **KC18**), which carries no such
divisor pathology.

**The magnitude bound closes the escape at physical rank.** The Demazure-Lusztig
operator `T_i` has eigenvalues `{q, −1/q}` (Hecke relation `T_i² = h·T_i + 1`,
`h = q − q⁻¹` — the *same* `h` that carries the KC18 odd channel; the
eigenvalue-sum is exactly `h`). A length-2 signed character is a product of two
eigenvalues, so `|D_w| ≤ q₀² ≈ 1.23`. Reaching `|Σ| ≈ 40` by summing `O(1)` terms
needs `~32` length-2 Weyl elements:

| rank | #(length-2 elements of Sₙ) |
|---|---|
| S₃ | 2 |
| S₄ | 5 |
| S₅ | 9 |
| S₆ | 14 |
| S₇ | 20 |
| S₈ | 27 |
| **S₉** | **≥ 32** |

So the escape requires **rank n ≥ 9** — physically absurd for a nucleon, which
lives in `H₃/H₄` Hecke (rank 3–4). Probe
[`qbeta_exotic_lusztig_magnitude_preflight.py`](../../computations/qbeta/qbeta_exotic_lusztig_magnitude_preflight.py)
→ [witness](../../computations/qbeta/qbeta-exotic-lusztig-magnitude-preflight.witness.json)
(4/4, exact).

## Verdict and scope (honest classification)

**Scope-(a), not scope-(b).** This does **not** prove that *no* exotic convention
works — an unphysical-rank (`n ≥ 9`) or unnaturally-large-magnitude convention
could in principle reach the target. What it establishes: the
**physically-motivated Demazure-Lusztig family does not escape** N1–N3, and the
`|Σ|~40` requirement it would need is an artifact of the `u`-series divisor that
the proved eval-map mechanism (KC18) does not share. So the escape is not a route
to a `c_2`/`c_3` the eval-map lacks; it is categorically unmotivated at physical
rank and, per KC18, unnecessary.

Combined tally on the cont.9 menu: **Option A (c_3 CAL-3-anchored permanently)**
is now backed by **3 corpus closures + 4 preflight refutations + 4 structural
narrowings (N1–N4)** + Lusztig 1990 positivity. The exotic-Lusztig escape remains
*formally* open only for unphysical-rank / non-categorical conventions — a
research curiosity, not a path to the nucleon's `c_3`.

## Discipline

No fit, no `c_k` value, nothing wired, no tier change. The owner-authorized
investigation reached a decisive formalize-first outcome without entering the
saturated convention-scan space — consistent with the anti-laundering rule
(§"Axiomatization is NOT a Proof") and the formalize-first probe discipline.

## Cross-references

- Scope + N1–N3: [`2026-06-06-qbeta-klr-exotic-signed-lusztig-bounded-magnitude-scope.md`](../scope/2026-06-06-qbeta-klr-exotic-signed-lusztig-bounded-magnitude-scope.md)
- KC17 (u-re-expansion obstruction): [`2026-07-07-z-ck-fmap-b3u-uside-transfer-obstruction.md`](2026-07-07-z-ck-fmap-b3u-uside-transfer-obstruction.md)
- KC18 (eval-map, `c_2` without the divisor): [`2026-07-07-z-ck-fmap-eval-map-bar-decomposition.md`](2026-07-07-z-ck-fmap-eval-map-bar-decomposition.md)
- `c_2 = −1` proved: `content/quantum-observable-universe/mass-theory/q-beta-c-2-eq-neg-one-structural.lean`
- Menu state: [`1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) cont.18
