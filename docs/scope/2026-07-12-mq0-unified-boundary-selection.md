# The u ≠ 0 boundary condition and the N-selection — one discrete question

**Date:** 2026-07-12 · **Axis:** c₃ bar-odd S geometric instantiation
(continuation of [`2026-07-12-mq0-literature-candidates.md`](2026-07-12-mq0-literature-candidates.md);
owner-picked items 1+2). · **Tier:** formalize-first scoping — derivations
of the *matching structure* only; no candidate evaluated, nothing wired.

## 1. The three candidate families are one parametrization

Hikami's boundary-parametrized state integral (math/0604094 eq 4.2, meridian
`m = e^u` external), Gukov's parametrized VC (`u = Nℏ` fixed), and
Murakami's RoU-deviation evaluation (`q_eval = e^{(u+2πi)/N}`) all present
the **same** deformation datum: the boundary/meridian log-holonomy `u`, fed
to the identical `𝔙(u) = Vol(u) + i·CS(u)` on the 4₁ character variety.
The differences are only in *how `u` is produced from the evaluation data*.

## 2. Substrate matching forces the form of u — and makes it complex

The substrate evaluation point is **real**, `q₀ = e^t`. Matching Murakami's
evaluation `q_eval = e^{(u+2πi)/N}` to `q₀` exactly:

    (u + 2πi)/N = t  (mod 2πi/N)   ⇒   **u(N, k) = N·t − 2πi·k**,  k ∈ ℤ₊

with `k = 1` the principal (nearest-RoU) branch. Three structural facts,
each *derived*, not assumed:

- **u is complex by construction** — real substrate offset `N·t` plus the
  winding `−2πi·k`. `e^u = q₀^N` is real, but `𝔙` lives on the *covering*
  of the character variety (the CS term sees the winding), so
  `Im 𝔙(u) ≠ 0` genuinely. This is exactly #3543's "phase accumulates like
  a root of unity", now with the mechanism explicit.
- **G2 (feasibility floor) is passed automatically**: `|u| ≥ 2πk ≥ 2π`,
  far above the 0.2135 floor — the first candidate family in five rounds
  that clears G2 structurally rather than failing it. *[Corrected in §6:
  this was a misframing — G2 is a magnitude* match, *not a one-sided
  floor; `|u| ≥ 2π` lands 1–2 orders* above *the `|u| ≈ 0.21` that the
  measured `|S|` demands, so the lattice overshoots rather than passes.]*
- **The continuous mystery m(q₀) collapses to a DISCRETE selection**: which
  integers `(N, k)` does the categorical action assign? A color and a
  winding — not a function to fit. This is the entire remaining freedom.

## 3. The gates become selection equations for (N, k)

- **G4 (zero at q*)**: `u(N, k, q*) = N·t* − 2πi·k` must lie on the
  `Im 𝔙 = 0` locus of the covering sheet — a **quantization condition**
  tying `N·t*` to a real-volume period. Order-of-magnitude:
  `N ~ 2π/t* ≈ 60.2`.
- **Named categorical N-candidates to check first** (named BEFORE any
  evaluation, per the anti-fitting discipline; the coincidence of scale is
  flagged, not claimed): `N = 60 = |A₅|` and `N = 120 = |2I|` — the
  icosahedral orders of the Bring-curve/s5-so3 substrate — plus the
  strand-data candidates `N ∈ {3, 6}` (H₃ / doubled). Any other N would
  need its own categorical derivation before being tested.
- **G3 (derivative gate)**: `d/dq[Im 𝔙(u(N,k,q))] = (N/q)·∂_u Im 𝔙` — the
  lever demands `N·|∂_u Im 𝔙| ≈ 3.84×10⁶·u³`-unlevered ≈ 2.37; with
  `N ~ 60`, `|∂_u Im 𝔙| ~ 0.04` at the evaluation point — an O(1)-testable
  requirement on the covering-sheet geometry (no blow-up needed: the
  winding sheet supplies the offset, the slope stays smooth — consistent
  with the "static amplification" law of #3621).
- **G1 (two values)** then has zero remaining freedom.

## 4. Why this dissolves the C3 branch blocker

The stage-0 branch ambiguity (periodic vs quasi-period continuation,
winding factor O(e^{2π²/t})) is the SAME winding datum as `k`: choosing the
state-integral contour sheet ⇔ choosing `k`. In the u ≠ 0 parametrization
the choice is explicit and discrete instead of hidden in a contour
deformation — the honest home for the decision.

## 5. Next compute (deferred; needs the uploaded source, not conventions)

Implement `𝔙(u)` for 4₁ from Murakami's explicit formulas
(`library/arxiv-math-0401084v3/0401084v3.pdf`, theorem-grade; cross-check against the merged
Newton solver on the real slice and Hikami's NZ series
`2v = −2πi + 4√3iu + …`), then evaluate the NAMED candidates
`(N, k) ∈ {3, 6, 60, 120} × {1, 2}` at both anchors against all four gates.
Discrete menu of 8 — no fit, every member pre-named with a categorical
pedigree. A kit-pass would be a near-match-tier candidate requiring
independent-method confirmation; 0/8 would be a clean scope-(a) negative
narrowing to other (N, k) derivations.

## 6. Postscript (2026-07-12, same day) — the §5 compute ran: 0/8

The deferred compute was executed in [PR #3704](https://github.com/litlfred/qou/pull/3704)
(`computations/qbeta/qbeta_c3_mq0_nk_scan.py`: branch-tracked
`𝔙(u)` for 4₁ from Murakami–Yokota math/0401084, machinery validated 5/5
— `u = 0 ⇒ Vol(4₁)`, NZ slope `2√−3`, gluing residual 1e−20). Verdict on
the named 8-member menu: **0/8, a clean scope-(a) negative**, exactly the
second branch anticipated above. The least-bad candidate `(N,k) = (120,2)`
still overshoots `|S_proton|` by ~40×; the six large-`|Im|` members by
1e2–1e4×. Root cause: the winding lattice forces `|u| ≥ 2π`, off the 4₁
geometric component and 1–2 orders above the `|u| ≈ 0.21` the measured
`|S|` magnitude demands — the §2 "G2 passed automatically" reading was a
misframing (corrected in place). Scope note: this excludes the *named
`(N,k)` menu as-is*, not winding per se.

Independently, the decisive resolution of the odd-S origin landed on
`main` while this memo was in flight: the Ohtsuki tower at the *small
imaginary* substrate parameter `2πb² = i·t` (`|·| ≈ 0.10`), with the
Lean-proved bar-parity selection rule and Borel–Padé `Im 𝔙 ≈ 0.055` —
see [`rem:ohtsuki-tower-bar-parity`](../../content/quantum-observable-universe/mass-theory/rem-ohtsuki-tower-bar-parity.md).
The small-parameter route supersedes the large-`|u|` winding route this
memo proposed; the `1/u³` ladder is that smooth object's representation,
per #3704's reconciliation.

## Cross-references

- Kit + exclusions: `QOU.QBeta.BarOddLadderShape` (PR #3660), #3562/#3596/#3621 witnesses.
- Winding diagnosis: #3543; static-amplification law: #3621; q*: the 2026-07-12 q* probes.
- s5-so3 keystone (icosahedral orders): [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md).
