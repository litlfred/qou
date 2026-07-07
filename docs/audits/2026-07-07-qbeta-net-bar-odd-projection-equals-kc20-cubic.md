# The GS net's bar-ODD projection IS KC20's odd-channel cubic (independent derivation)

**Date:** 2026-07-07 · **Axis:** z→c_k f-map keystone, forward direction ·
**Follows:** the [W2 kill](2026-07-07-qbeta-gs-net-vs-cos-ladder-w2-kill.md)
(full GS net is cosh-like / bar-even dominated) · **Tier:** symbolic-exact ·
**No `c_k` value, no wiring** (registry §8 guard).

## Result

The W2 kill showed the *full* H₃ GS categorical net `Δ(net)` is cosh-like — its
**bar-even** part dominates and pushes Q_β away from the observable ladder. So the
decay carrier is the **bar-ODD projection**. Computing it exactly:

`Δ(net)_odd = ½(Δ(net)(q) − Δ(net)(1/q)) = (h/4)·C(q² + q⁻²)`,
  with `h = q − q⁻¹` and `C(y) = y³ − 4y² + 3y − 2`.

**`C(y)` is exactly the irreducible odd-channel cubic of KC20** — which the
sibling PR derived *independently* from the cyclotomic / Hopf-sector analysis of
the bar-odd carrier. Two independent categorical routes to the identical cubic.

Probe [`qbeta_net_bar_odd_projection_probe.py`](../../computations/qbeta/qbeta_net_bar_odd_projection_probe.py)
→ [witness](../../computations/qbeta/qbeta-net-bar-odd-projection.witness.json)
(7/7, sympy-exact):

| gate | result |
|---|---|
| W-odd-1 | `Δ(net)_odd = (h/4)·C(q²+q⁻²)` **exactly** |
| — | `Δ(net)_odd` is exactly bar-odd; vanishes at `q=1` (since `h(1)=0`) |
| W-odd-2 | `C = C_Hopf + C_unknot` (KC20 split): `C_Hopf = y³−6y²+10y−6`, `C_unknot = 2y²−7y+4` |
| W-odd-3 | `C`, `C_Hopf` irreducible over ℚ (no rational root) |
| W-odd-4 | no quadratic anchor is a root: `C(golden y=3) = −2`, `C(silver y=6) = 88`, `C(classical y=2) = −4` |

## Why it matters

- **Independent corroboration of KC20.** KC20 (registry §9, sibling) obtained
  `C(y)` from a cyclotomic/Hopf-sector route and concluded "real-q/quadratic
  `c_3` closures are structurally excluded; the open odd channel is the
  Hopf-sector cubic field via KC18/KC19 archimedean evaluation." This audit
  reaches the *same* cubic from a completely different object — the bar-odd
  projection of the H₃ GS augmentation `Δ(net)`. A degree-3 field arrived at by
  two independent categorical constructions is strong evidence it is the genuine
  odd-channel object, not an artifact of either derivation.
- **Resolves the W2 tension.** The full net is cosh-like *because* it is
  bar-mixed and even-dominated; the observable's bar-odd decay content is
  cleanly `(h/4)·C(y)`. The bar-even growth (W2) and the bar-odd cubic (here) are
  the two halves KC18 splits the evaluation map into — now both computed on the
  actual categorical net.
- **The `c_3` exclusion, doubly witnessed.** Since `C` is an irreducible cubic,
  its roots generate a degree-3 field; no quadratic anchor (golden/silver/
  classical `y`) lies in it. So a real-q/quadratic closed form for `c_3` cannot
  come from this channel — matching KC20 and the `dc_3/dq ≈ 4.6×10⁶` rigidity,
  now from the GS-net side too.

## Scope / next

Symbolic-exact, no fit, no anchor, no `c_k` value. The odd channel is now pinned
to `(h/4)·C(y)` on *both* the Hopf-sector (KC20) and GS-augmentation (here)
routes. The remaining open step is unchanged and sharpened: the **archimedean
(Rogers↔Faddeev) evaluation** of this irreducible cubic at the substrate anchor —
per KC18/KC19 — is where any `c_3` value would come from; a real-q/quadratic
route is excluded on both routes.

## Coordination

Suggested registry note on **KC20**: add "independently reproduced as the bar-odd
projection `(h/4)·C(q²+q⁻²)` of the H₃ GS categorical net (this audit)" — left
for coordination with the KC20 owner branch to avoid a cross-branch §9 edit;
flagged on the sibling PR.
