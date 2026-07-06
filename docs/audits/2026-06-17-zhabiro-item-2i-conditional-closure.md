# z-Habiro item 2(i): conditional closure + the pinned c_n

**Date:** 2026-06-17
**Branch:** `claude/zhabiro-cn-coords-exist-2026-06-17` (PR #2447)
**Status:** item 2(i) of `conj:brane-tower-z-habiro` **conditionally closed**;
one `tprod`-reindex step **pending full-build verification** (see §Verification).

## What closed

The "which family / which base ring" half of item 2(i) — pinning the cyclotomic
coefficients `c_n` of the analytic `Φ_q` — is now reduced to a single analytic
input (the functional equation) and a chain of machine-checked algebra:

```
analytic Φ_q  ──(1−z)·Φ_q(qz)=Φ_q(z)──▶  its coeffs obey the q-difference recurrence
   [quantumDilog_functional_eq]                     │
                                                     ▼  eulerCoeff_unique ✅
                       coeffs = eulerCoeff  (the localised Euler family) ✅
                                                     ▼  zHabiroLimit_eq_euler ✅
              the z-Habiro Cauchy limit  zHabiroLimit qinv eulerCoeff  IS Φ_q's
```

| Lean declaration (`QOU.MassEndomorphism.*`) | content | status |
|---|---|---|
| `ZHabiroCauchy.eulerCoeff` (+ `_zero`, `_succ`) | Euler `b_n = q^{-n}/∏(1-q^{-j})` in `S^{-1}ℤ[q^±1]`, `S=⟨1-q^{-j}⟩` | ✅ #2442 |
| `ZHabiroCauchy.braneMonic_coords_unique` | cyclotomic coordinates unique | ✅ #2442 |
| `ZHabiroCauchy.braneMonic_coords_exist` | monic basis spans `R[X]_{≤n}` | ✅ #2447 |
| `ZHabiroCauchy.eulerCoeff_unique` | the q-difference recurrence has a unique solution | ✅ #2447 |
| `ZHabiroCauchy.zHabiroLimit_eq_euler` | **conditional closure**: recurrence ⇒ limit = localised-Euler element | ✅ #2447 |
| `PhiQConvergence.quantumDilog_functional_eq` | `(1−z)·Φ_q(qz)=Φ_q(z)` | ⚠️ pending (§Verification) |

The "couple of generic points determine it" mechanism (owner, 2026-06-17): `Φ_q`
is the unique solution of a **first-order** q-difference equation with the single
normalisation `Φ_q(0)=1`; the value at the one generic point `z=0` plus the
functional equation (relating `z` and `qz`) pins every coefficient. In
coordinates this is exactly `eulerCoeff_succ`, whose unique solution is
`eulerCoeff`.

## Verification (STRICT — pending item)

All declarations **except** `quantumDilog_functional_eq` are verified sorry-free
by `lean`-direct in the web sandbox (full Mathlib context, oleans restored from
`lake-cache/qou-v4-24-0`).

`quantumDilog_functional_eq` is a `tprod` reindex via
`Multipliable.tprod_eq_zero_mul`. Its **arithmetic core** (`hstep`, `htail`,
`hhead`, the domain bounds) is verified sorry-free; the single
`tprod_eq_zero_mul` step **could not be verified in the sandbox** because that
lemma whnf-times-out at 4·10⁵ heartbeats **even on a trivial `g : ℕ → ℝ`** — an
artifact of the restored-olean environment, not a defect of this proof (the
lemma is standard and instant in a real build). `maxHeartbeats` raised to 10⁶.

- **Independent math check:** `computations/probes/z_habiro_increment_probe.py`
  confirms (exact symbolic) that the functional equation holds coeff-wise and
  the recurrence reproduces the Euler coefficients.
- **Owner directive (2026-06-17):** proceed assuming `quantumDilog_functional_eq`
  compiles; full-build (`lake build`) confirmation is **still pending** (overnight
  laptop run). This note is the record of that pending item. If a full build
  fails, the fix is tactic-orchestration (beta/`tprod_congr` matching), not a
  math gap.

## Cross-references

- `content/quantum-observable-universe/lean/QOU/MassEndomorphism/ZHabiroCauchy.lean`
- `content/quantum-observable-universe/lean/QOU/MassEndomorphism/PhiQConvergence.lean`
- `content/quantum-observable-universe/mass-theory/brane-tower-z-habiro.md` (conjecture)
- `computations/probes/z_habiro_increment_probe.py` (symbolic check)
- PRs #2442, #2447
