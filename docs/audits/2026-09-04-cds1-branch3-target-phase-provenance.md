# The branch-3 target phase is experimentally anchored — but the quoted number is the form's

**Bean:** `qou-cds1` / `qou-pdix` route 5.
**Probe:** [`computations/qbeta/qbeta_required_phase_target_provenance_probe.py`](../../computations/qbeta/qbeta_required_phase_target_provenance_probe.py) (4/4).
**Scope: (a).**

## Why this was asked, and the answer I expected

Branch 3 of the eigenphase trichotomy scores every candidate generator against a
required eigenphase, quoted by
[`HolonomySpectrumSignObstruction`](../../content/quantum-observable-universe/lean/QOU/QBeta/HolonomySpectrumSignObstruction.lean)
as `θ = 0.0565947` rad (required correction factor `0.998399`). The arc's own
discipline is explicit that a number may be *checked against* but never
*searched on* unless it is independently anchored — see the `c₃(muon)`
coincidence note in
[`qbeta_decay_operator_elliptic_spectrum_probe.py`](../../computations/qbeta/qbeta_decay_operator_elliptic_spectrum_probe.py).

I came to this **expecting circularity**: that `0.0565947` was read off the
ladder's own `cos(α − u/2)`, whose form `α = (z−1)h/2` has no derivation
([`2026-09-04-cds1-ladder-phase-has-no-derivation.md`](2026-09-04-cds1-ladder-phase-has-no-derivation.md)).
If so, every branch-3 candidate would be scored against a fit.

**That expectation was wrong.** Recorded as wrong, because someone else will
arrive at the same worry.

## The target is genuinely experimental

The N=1 factor the experiment requires, from inputs independent of the phase
form:

```
Q_A      = m_e·|q²−2q−1|(q+1)/(2q³)      prop:neutron-qvalue-symbolic
c_2      = −1                             structural — no fit, no CODATA, no q₀
required = Q_exp / (Q_A·(1 − u²))        = 0.99839766871925519
```

Nothing in it reads `z`, `α`, or any fitted `c_k`. So branch 3 has a legitimate
criterion to search on, and the circularity worry is unfounded.

## The defect that is there

`arccos(required) = 0.0566173`. The quoted target is `0.0565947`, and that
number is `|α − u/2|` — **the form's own phase** — matching it to `6.6e-7`
relative while matching the experimental value only to `4.0e-4`.

| quantity | value | matches quoted to |
|---|---|---|
| quoted target | 0.0565947 | — |
| `\|α − u/2\|`, convention C (the **form**) | 0.056594737543 | 6.6e-7 |
| `arccos(required)` (the **experiment**) | 0.056617300794 | 4.0e-4 |

So the branch is scored against what the current form produces, where it should
be scored against what the experiment requires. That is precisely the
"target versus criterion" distinction the arc's own discipline turns on, applied
one level up — to the target itself.

**Correct target for branch 3: `θ_required = 0.0566173`, not `0.0565947`.**

**This changes no verdict on record.** The correction is 0.0399 %, and the one
elliptic candidate on record (`Δ_L = NF(n) − NF(p)`, `θ = 2.0204`) misses by a
factor of 35.7. It matters only for a future candidate landing inside 4e-4 — but
that is exactly the regime in which a branch-3 result would be declared, so the
number should be right before then.

## A convention note, and what it is not

The C form sits `1.28e-6` from the experimental requirement; the D form sits
`6.02e-4`, about 470× further. That is consistent with the ladder having been
built in convention C and is **not** evidence for C, which is excised. It is
recorded only so that a reader comparing the two does not mistake the gap for a
physical statement.

## Scope

**(a)**. About the provenance of the target number, not about any candidate
generator, and not about whether a phase is derivable. Nothing is wired, no
`c_k` moves, no convention is adjudicated.
