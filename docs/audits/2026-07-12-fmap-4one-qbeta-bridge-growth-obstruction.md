# The 4₁↔Q_β bridge, precisely: exact both-channel fibre objects, cosh/sinh unification, and the growth-class obstruction

**Date:** 2026-07-12 · **Axis:** z→c_k f-map keystone (the 4₁↔Q_β bridge) · **Tier:**
scope-(b) structural (growth-class obstruction, cited invariant) + map synthesis ·
**Discipline:** no fit, no c_k value wired, nothing closed, no tier change. Builds on
the merged κ₁ (#3606) and the exact higher rungs (#3628).

## Why this document

The bridge from the **4₁ resurgence action** (even channel) to the **physical Q_β
observable** (odd channel) is the standing open keystone. Two recent results change
what is *known* about it, so the open gap can now be stated precisely:

1. **Even channel is exact** (#3606/#3628): `log J_N(4₁) = (3/2)logN + N·Vol/2π + A₀
   + Σ κ_n/N^n` with `κ_n ∈ ℚ(√3)·π^n` — `κ₁=(11/108)√3π`, `κ₂=(2/27)π²`,
   `κ₃=(1081/21870)√3π³`, `κ₄=(98/729)π⁴` (Ohtsuki figure-eight, 2-loop numerator 11).
2. **Odd channel is exact** (KC18–KC20): the Q_β `c₃` bar-odd carrier is the
   irreducible Hopf cubic `(h/4)·C(y)`, `C=y³−6y²+10y−6`, disc −76, prime-19, with
   real-q/quadratic closures Lean-excluded (`QBetaZeta4ResidueRefutation.lean`).

Both *fibre-level* objects are pinned exactly. This document states (a) the exact
structural skeleton that unifies them, (b) the precise reason a naive term-by-term
bridge is impossible, and (c) where the genuine open gap lives.

## (a) The skeleton — both channels are cosh/sinh of one η = log q (already proved)

The bar-even / bar-odd split *is* the cosh/sinh split of `η = log q`:

- even generator `[2]_q = q + q⁻¹ = 2 cosh η` (`bracket_two_eq_two_cosh`) — the
  4₁ / m_π / CAL-3 face (amphichiral, `J_{4₁}(q)=J_{4₁}(q⁻¹)`);
- odd generator `h = q − q⁻¹ = 2 sinh η` (`hecke_h_eq_two_sinh`) — the Q_β / Hopf /
  CAL-2 face (chiral).

They are linked by the Pythagorean identity, **already sorry-free** as
`reeb_growth_hyperbola : cosh²η − sinh²η = 1`
([`ReebTowerJacobiAnger.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/ReebTowerJacobiAnger.lean)),
i.e. `[2]_q² − h² = 4`. So the even (4₁) and odd (Q_β) channels are not independent
constructions — they are the two bar-parity halves of the *same* `η`. The bridge is
therefore not "relate two unrelated objects" but "relate the cosh-sector expansion
(exact κ_n) to the sinh-sector expansion (exact `C(y)`) of one `η`."

## (b) The growth-class obstruction — the bridge is NOT term-by-term (scope-(b))

The two channels are expanded in *different* variables — the even channel in
`ℏ = 2πi/N = η` (the `N→∞` volume-conjecture limit), the odd channel in
`u = b·ℏ_q²` (the substrate deformation, `ℏ_q = 1−1/q₀`). The exact κ_n now expose a
**growth-class dichotomy** that no change of variables can remove:

| | even channel (κ_n, exact) | odd channel (Q_β ladder c_k) |
|---|---|---|
| successive ratio | `κ₂/κ₁, κ₃/κ₂, κ₄/κ₃ = 1.32, 3.63, 4.93` — **rising without bound** | `c_{k+1}/c_k → 1/u = 117.41` — **constant** (KC8) |
| growth class | **Gevrey-1 divergent** (`κ_n ~ C·Γ(n+β)/A^n`, ratio `~ n/A → ∞`) | **convergent**, simple pole at `u_substrate` |
| resummation | asymptotic; needs Borel / median | already summable inside `\|u\| < u_substrate` |

**Cited invariant (makes this scope-(b), not a scope-(a) numerical miss):** the
even-channel series is the asymptotic expansion of a *hyperbolic* knot's quantum
invariant, hence Gevrey-1 with a nonzero Borel singularity (the resurgence action
`A`, the sub-dominant saddle); the Q_β ladder is convergent with a simple pole
(KC8, corroborated independently by the `c_{k+1}/c_k` plateau at 117.41). A
factorially-divergent series and a convergent one **cannot** be equated
term-by-term under any reparametrisation `ℏ ↔ u`. Therefore the bridge map is
necessarily the **Borel / median resummation** of the even-channel series — i.e.
the Faddeev `Φ_b` state integral at real `q₀` (off `|q|=1`), exactly the object the
live frontier (#3544/#3596) is constructing. This closes off the naive "identify
κ_n with c_k" route as a proved dead end, not a failed probe.

## (c) The precise open gap + a decisive necessary condition

The gap is **not** the fibre objects (both exact) — it is the **archimedean
(Rogers↔Faddeev) evaluation map** `E` carrying the fibre data to the observable
`c_k` at substrate `q₀`. Post-#3628, `E` is squeezed from both sides: its input on
the even side is exactly `Σ κ_n/N^n` (Gevrey-1, Borel singularity `A`); its output
on the odd side is the convergent ladder (pole `1/u = 117.41`).

**Necessary condition (a decisive, honest check — not a fit):** the Borel median
resummation sends the even-channel singularity at `ℏ = A` to a singularity of the
observable in the `u`-plane. Under `u = b·ℏ_q²` with `ℏ_q ≈ ℏ` near `q=1`, the
even Borel singularity lands at `u ≈ b·A²`. The bridge *requires*
`b·A² = u_substrate = 1/117.41` (the ladder pole). With the documented `A ≈ 0.688`
and the substrate `b`, this is a one-line falsifiable test: a pass is a genuine
structural signal for the bridge; a fail bounds the change-of-variables and
localises the missing analytic ingredient. **This test needs `A` to more digits
than 4 exact κ_n give** (the κ_n ratios estimate `A ≈ 0.7`, consistent with 0.688
but not yet sharp); extracting `κ₅, κ₆` (research-grade, lower precision) sharpens
`A` and makes the necessary-condition test conclusive. That extraction is the
concrete next compute; it is *not* a closure of the bridge.

## Honest scope (anti-laundering)

Nothing here closes the bridge or wires a `c_k`. The even κ_n and the odd `C(y)` are
**4₁-Kashaev / Ohtsuki topological facts**; the cosh/sinh link is elementary and
already proved. The one *new* structural claim — the growth-class obstruction — is a
scope-(b) *negative* (it rules the naive bridge out), with its invariant cited. The
positive bridge (the `E` map) remains open and is the Φ_b state-integral frontier.
**No fit; no c_k value wired; no tier change.**

## Cross-references

- Even channel exact: [`2026-07-12-ohtsuki-higher-rungs-exact.md`](2026-07-12-ohtsuki-higher-rungs-exact.md), [`2026-07-11-fmap-action-qsqrt3-saddle-lean.md`](2026-07-11-fmap-action-qsqrt3-saddle-lean.md)
- Odd channel cubic (KC18–KC20): [`2026-07-11-qbeta-c3-kc19-kc20-consistency.md`](2026-07-11-qbeta-c3-kc19-kc20-consistency.md), [`2026-07-07-qbeta-net-bar-odd-projection-equals-kc20-cubic.md`](2026-07-07-qbeta-net-bar-odd-projection-equals-kc20-cubic.md)
- Growth tension (KC8) + Φ_b frontier: [`2026-07-11-qbeta-ck-untested-avenues-and-literature.md`](2026-07-11-qbeta-ck-untested-avenues-and-literature.md) §3.B; live on PRs #3544/#3596
- cosh/sinh channel link (proved): [`CoherentCollapseSinhCosh.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/CoherentCollapseSinhCosh.lean), [`ReebTowerJacobiAnger.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/ReebTowerJacobiAnger.lean)
- Registry (per-rung tiers): [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
