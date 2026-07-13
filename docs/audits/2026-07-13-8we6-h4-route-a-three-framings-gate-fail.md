# 8we6 Route A executed: all three owner-authorized 4th-strand framings FAIL the decoupling gate

**Date:** 2026-07-13 · **Branch:** `claude/canonical-derivation-c-k-n00n2h` (PR #3769) ·
**Bean:** `8we6` (genuine c₄ rungs → Casoratian W₃ sign test) ·
**Probe:** [`qbeta_h4_route_a_gate_probe.py`](../../computations/qbeta/qbeta_h4_route_a_gate_probe.py)
(+ witness) · **Tier:** exact (sympy s-series, no floats in the ladder solve; no fit) ·
**Scope:** (a) — these three constructions, as built, fail the gate; NOT an
exclusion of every σ₂-support object.

## Context

The [2026-07-03 route-B prune](2026-07-03-8we6-h4-route-b-structural-prune.md)
left Route A as the only live H₄ path for a genuine `c₄^even` rung, gated on
two design choices the owner had to make ("owner call, NOT agent ansatz"):
the 4-strand object and the 4th-strand coupling rule. **The owner authorized
building all three candidate framings (2026-07-13, PR #3769 session)** and
letting the recorded decoupling gate decide: *the H₄ object's ladder must
reproduce the trusted H₃ rungs `c₂^even = −8.00641…`, `c₃^even = +86.66116…`
exactly; if lower rungs move, the object is wrong.*

## Build

The probe reproduces the `free-neutron-decay.py` machinery exactly (quiet
n-agnostic GB reducer — Hecke + far-comm + Yang-Baxter; identical crossing
rules) and validates: H₃ `Δ(net)` matches the committed witness at q₀
(−0.18829062), and the in-run H₃ ladder reproduces the 1jrh exact rungs.
Baseline H₃ `c₄`-order coefficient (s⁸, not a rung claim): −1819.74.

| framing | construction | Δ(net)₄(q=1) | c₂^even (shift) | c₃^even (shift) | gate |
|---|---|---|---|---|---|
| A1 brane/Hopf strand | pairwise loop extended to A=4; `(i,3)` pairs take the bare `σ_gen` else-branch | 0 ✓ | +3.99359 (**+12 exactly**) | −65.5027 (−152.164) | **FAIL** |
| A2 lepton strand | emitted-lepton word `e⁻ = σ₀σ₁σ₀` shifted to upper strands (`σ₁σ₂σ₁`), appended | 0 ✓ | −5.83974 (**+13/6 exactly**) | +114.951 (+28.290) | **FAIL** |
| A3 4-Brunnian core | `B₃ → B₄ = (σ₀σ₁⁻¹σ₂σ₁⁻¹)³` (candidate word; Brunnian property unverified), same quark crossings | 0 ✓ | −48.0064 (**−40 exactly**) | +555.213 (+468.55) | **FAIL** |

All three are `(q−1)`-regularizable (the ladder is defined) — and all three
move `c₂` and `c₃`, i.e. their σ₂ content enters the ladder at order `u²`,
not `u⁴`.

## The sharpened design criterion (what the fails teach)

The exact rational `c₂` shifts (+12, +13/6, −40) come from the ratio
`Δ(net)₄/Δ(net)₃` deviating from 1 already at `s²`. This gives a **checkable
a-priori criterion for any future Route-A candidate**, cheaper than the full
ladder:

> a candidate H₄ object with `Δ(net)₄ = g(q)·Δ(net)₃·(1 + O((q−1)^{2k}))`
> can contribute an independent rung first at `c_k`; a genuine `c₄`-only
> object needs `log(Δ(net)₄/Δ(net)₃) = O(u⁴)` — vanishing through `s⁶`.

None of the three natural constructions (append a coupling, extend the
pairwise loop, replace the core) comes close: appended/global modifications
dress the element at leading order. This mechanically corroborates the
Stage-B prescription that H₄ content must enter through *longer braid words
entangled mid-word* — constructions whose low-order ladder content cancels by
design — or through a *subtracted/connected* object built to cancel the
`u²`/`u³` dressing. Both are new design work, again owner-level framework
content.

## Disposition

- **Bean 8we6 item 1 (c₄^even via H₄):** the three authorized framings are
  executed and **negative** (gate-fail, exact shifts recorded). No `c₄^even`
  rung exists yet; W₃ stays gated (its conditional branch never fired).
- **Scope-(a):** the failure is of *these three constructions as built* —
  the invariant cited is the gate itself (lower-rung exactness), not a
  structural impossibility theorem. The `O(u⁴)`-dressing criterion above is
  the surviving constraint any future candidate must clear.
- No `c_k` wired; no tier change; registry untouched (no rung produced).

## Cross-references

- Route-B prune + gate definition: [`2026-07-03-8we6-h4-route-b-structural-prune.md`](2026-07-03-8we6-h4-route-b-structural-prune.md)
- Trusted rungs: [`2026-07-02-1jrh-c3even-exact-measurement.md`](2026-07-02-1jrh-c3even-exact-measurement.md) (+ witness `qbeta-c3even-exact-sseries.witness.json`)
- H₄ Hoefsmit/Ind machinery (prerequisite, landed 2026-07-13): `computations/probes/markov_reduction_h3_to_h4_verify.py`
- Why extracted c₄ can't substitute: the P4 entropy audit (registry §3, c₄ row)
