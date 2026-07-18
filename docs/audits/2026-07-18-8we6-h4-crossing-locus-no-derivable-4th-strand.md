# 8we6 option-2: no derivable constant-coupling 4th strand passes the c₄ gate

**Date:** 2026-07-18 · **Branch:** `claude/pr-3660-merge-pipeline-ephmw4` (PR #3833) ·
**Bean:** `8we6` (genuine c₄ rungs → Casoratian W₃), session `qou-tti3` ·
**Probe:** [`qbeta_h4_crossing_locus_probe.py`](../../computations/qbeta/qbeta_h4_crossing_locus_probe.py) (+ witness) ·
**Tier:** exact (sympy s-series + resultant; no float in the algebra; no fit) ·
**Scope:** (a) — a negative on the **constant-coupling** 4th-strand family, with the
gate invariant cited; **not** a scope-(b) exclusion of all H₄ objects.

## The move (formalize-first, not a tenth candidate)

The 07-13 gate-fail audit executed nine hand-built H₄ constructions (three
Route-A framings + six mid-word screens), all `GATE-FAIL`, and warned that a
tenth hand-arranged candidate would be "tuning — the fit trap." The
screen those negatives rest on was independently **verified sound** the same
session ([`2026-07-17-8we6-h4-screen-calibration-verified.md`](2026-07-17-8we6-h4-screen-calibration-verified.md)).

This probe asks the *structural* question instead of guessing again: **does
*any* 4th-strand crossing rule pass the decoupling gate?** The 4th strand's
categorical content is exactly its two crossing couplings — `α = ` (b–u
crossing), `β = ` (b–d crossing) — each of the form `σ_gen + w·1` with
`w = −ℏ_q·θ` (`ℏ_q = q−q⁻¹`), the shape **every** existing crossing rule takes
(`θ ∈ {0, ½, 1}` for u–u / u–d / d–d). Regularizability (`Δ(net)₄(q=1)=0`) is
automatic for all `(α,β)` of this form. We then compute the screen coefficients
`φ₄(α,β), φ₆(α,β)` exactly and ask whether the gate `φ₄ = φ₆ = 0` has any
**derivable** (nameable-categorical) solution.

## Result

- **`φ₄, φ₆` are exact rational functions** with denominators
  `8(α−β+1)⁴` and `24(α−β+1)⁶` — the leading net coefficient is `p₀ ∝ (α−β+1)`,
  so the object degenerates only on the line `β = α+1`.
- **Categorical grid (7×7 nameable couplings, `θ ∈ {0,±½,±1,±2}`): none zero
  both `φ₄` and `φ₆`.** In particular the existing rules `(0,−½,−1)²` do not
  pass — consistent with, and explaining, the nine-candidate negatives.
- **Full locus (resultant `Res_β(N₄,N₆)`, degree 72 in α): exactly one rational
  α-root, giving `(α,β) = (−3/2, −1/2)` — a spurious pole degeneration, not a
  gate pass** (see below). Every other locus point is irrational (a tuned value,
  the fit-trap).

**Verdict:** no derivable constant-coupling 4th-strand crossing rule passes the
c₄ decoupling gate. A passer would require a **q-dependent** coupling
`θ(q)` (higher-Taylor) — which carries unbounded free coefficients and is
therefore a fit, not a derivation. This lifts the nine-candidate scope-(a)
negative to the whole constant-coupling family.

## Critical-eye record — two self-caught probe artifacts

Per the owner's "some probes may be inaccurate — keep critical eye," two
false signals from *this probe's own tooling* were caught and corrected before
any verdict was recorded:

1. **Vandermonde conditioning (screen-verify probe, qou-tti3).** The first
   independent φ engine solved an order-8 Vandermonde on clustered points
   `s = 1e-3…8e-3` — catastrophically ill-conditioned — and spuriously reported
   `engines_agree = False` for all candidates. Replaced by a Cauchy contour
   integral (`mpmath.taylor` quad); agreement collapsed to ~1e-48.
2. **Resultant pole-locus extraneous root (this probe).** The resultant's sole
   rational root `(−3/2,−1/2)` satisfies `N₄ = N₆ = 0` and was first flagged
   `derivable=True`. But `α−β+1 = 0` there — it lies on the **denominator's**
   zero locus. Direct limits give `φ₄ → −∞` (not a finite zero): a `0/0`
   degeneration where the 4-strand net loses its leading term. The classifier
   now excludes pole-locus points and requires `φ₄ = φ₆ = 0` as **finite**
   zeros; the corrected verdict matches the grid.

## Scope discipline (STRICT (a)/(b))

This is a **scope-(a)** negative: *the constant-coupling 4th-strand family, as
parametrized, does not pass the gate.* The invariant cited is the decoupling
gate itself (`φ₄=φ₆=0`, i.e. lower-rung exactness) plus the exact locus
computation. It is **not** a scope-(b) structural exclusion — untested and
still open:

- **q-dependent couplings** `θ(q)` (the named escape hatch; a derivation would
  have to *derive* `θ(q)`, not fit it);
- **non-net-route** constructions (subtracted / connected objects whose
  low-order cancellation is *derived*, per the gate-fail audit);
- objects outside the `σ_gen + w·1` two-term crossing ansatz.

## Disposition

- Bean `8we6` item 1 stays **open by an honest wall**, now sharpened: the wall
  is the whole constant-coupling family, not just nine unlucky constructions.
- No `c_k` wired; no tier change; registry untouched (no rung produced).

## Cross-references

- Screen verified: [`2026-07-17-8we6-h4-screen-calibration-verified.md`](2026-07-17-8we6-h4-screen-calibration-verified.md)
- Nine-negatives + gate: [`2026-07-13-8we6-h4-route-a-three-framings-gate-fail.md`](2026-07-13-8we6-h4-route-a-three-framings-gate-fail.md)
- Route-B prune: [`2026-07-03-8we6-h4-route-b-structural-prune.md`](2026-07-03-8we6-h4-route-b-structural-prune.md)
- Casoratian W₃ endpoint: [`2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md`](2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md)
