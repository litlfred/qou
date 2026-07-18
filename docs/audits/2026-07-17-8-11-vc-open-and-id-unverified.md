# 8₁₁ (³H) — the volume-conjecture instance is open, and the knot *assignment* is itself unverified

**Date:** 2026-07-17
**Branch:** `claude/mass-binding-close-2026-07-17`
**Context:** "What next to close the derivation of the pinned mass and binding
formula" — the binding-scale identity `B(K) = m_e · 2·Vol(K)` is conditional on
the volume conjecture *per link*. Three of the four load-bearing instances are
now on **proven** ground; ³H is the lone hold-out. This note records the honest
status of that hold-out after a targeted hunt for a closable instance, so a
later agent does not re-open the search believing a citation or SnapPy match is
one grep away.

Companion to
[`docs/coordination/binding-scale-is-hyperbolic-volume.md`](../coordination/binding-scale-is-hyperbolic-volume.md)
(the load-bearing claim + per-link proven/open table).

## The per-link volume-conjecture ledger (recap)

| Instance | Role | VC status |
|---|---|---|
| **4₁** | muon anchor `Vol(4₁)` | **proven** (Ekholm; Andersen–Hansen) |
| **L6a4 = Borromean rings** | ³He scale `2·Vol(L6a4)` | **proven** — a Whitehead chain (R. van der Veen, *Proof of the volume conjecture for Whitehead chains*, [arXiv:math/0611181](https://arxiv.org/abs/math/0611181), Acta Math. Vietnam. 2008; the family explicitly contains the Borromean rings) |
| **𝓑₃** | deuteron / single-nucleon Borromean scale | derived via `m_e·Vol(𝓑₃)·Δtr` (+0.19 %) |
| **8₁₁** | ³H scale `2·Vol(8₁₁)` | **open** — this note |

## Finding 1 — the 8₁₁ volume-conjecture instance is genuinely open

The volume conjecture is proven only for specific families and small cases
(figure-eight and its cables; torus knots in the appropriate asymptotic sense;
Whitehead chains via van der Veen 2008; the Borromean rings as a member of that
family; a handful of individually-verified hyperbolic knots in the
Ohtsuki-school asymptotic-expansion literature). **8₁₁ is an 8-crossing
hyperbolic knot and lies in none of these covered families.** No published
result establishes VC for it, and it is beyond the individually-verified
frontier.

Per the corpus-grep + "no fabricated citation" discipline: **there is no
reference to add.** Writing `8₁₁` as "proven modulo a citation" would be
laundering an open instance. The correct status remains **conditional on the
volume conjecture (open instance)**, exactly as the coordination table already
records it.

## Finding 2 — the 8₁₁ = ³H *assignment* is itself unverified

Distinct from (and logically prior to) the VC gap: the identification of the
tritium nucleus with the knot **8₁₁** is a `manual-historical-volume-match` — it
was chosen because `m_e·2·Vol(8₁₁) = 8.47 MeV` sits −0.16 % from the AME ³H
binding energy, **not** because the canonical SDP knot-ID pipeline (the
Wedderburn-block / Markov-trace selection that assigns a braid to a nucleus)
returned 8₁₁ for A=3, Z=1. So even a future proof of VC-for-8₁₁ would close only
*half* the gap: it would make `Vol(8₁₁)` a theorem, but leave open whether 8₁₁ is
the physically-correct ³H knot.

This is the same trap the ⁴He `Vol₄` probe fell into and closed out honestly on
2026-07-13 (`he4_vol4_prediction_test_probe.py` + audit): a residual-implied
volume with **no in-advance-named** structural knot/link carrier is a post-hoc
match, not a derivation.

## The real closure path (recorded, not executed here)

The honest route to closing ³H is **not** "find a VC proof for 8₁₁." It is the
same route the ⁴He audit named: run the **canonical SDP knot-ID at H₉** for the
true A=3, Z=1 link. Two outcomes, both progress:

1. **The SDP returns a Whitehead-chain / arithmetic link** whose VC is *already*
   proven (the way L6a4 = Borromean was closed by van der Veen 2008). Then ³H is
   closed on proven ground, and 8₁₁ was simply the wrong historical guess.
2. **The SDP returns 8₁₁** (or another non-covered knot). Then the assignment is
   *derived* (Finding 2 closed), and only the VC instance stays open (Finding 1),
   which is an honest, well-scoped open problem to state.

Either way the deliverable is a *derived* assignment, replacing the
`manual-historical-volume-match`. That SDP re-ID is the next concrete unit of
work; it is not done in this note.

## Scope discipline

Per "before declaring refuted / ruled out": nothing here is refuted.

- **8₁₁ VC** — scope-(a) open (no proof known), *not* a structural exclusion.
- **8₁₁ = ³H** — unverified assignment, *not* a disproven one; the −0.16 %
  numerical agreement is real and is exactly the kind of near-match the SDP
  re-ID would either derive or displace.

The Lean-proved pieces are untouched: bond-count `M_n = n−1`
(`DeltaLambdaExponentKeystone` family) and the A=3 multiplicity results stay
valid; this note constrains only the *volume-instance* leg and the *assignment*
leg of the ³H scale, not the algebra around them.
