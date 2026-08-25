---
# qou-iav7
title: threerow_isospin_parity_probe has the same C/D straddle as qou-qdtk, and emits NO witness
status: todo
type: task
priority: normal
created_at: 2026-08-25T19:29:30Z
updated_at: 2026-08-25T19:30:09Z
---

FOUND 2026-08-25 while draining `qou-qdtk` (PR for that is in flight). Not previously
identified by the #5762 audit or by `qou-qdtk`'s own diagnosis — it is a FOURTH
instance of the class, reached by grepping for the symbols `qou-qdtk` removed.

## The defect — identical straddle, independently hardcoded

`computations/deltalambda/threerow_isospin_parity_probe.py`:

```
  82  U_STAR = mp.findroot(lambda u: -u**6 - u**4 + u**3 + u**2 + 1, mp.mpf("1.13"))
  83  Q_STAR = U_STAR ** 2                          <- convention C's pole
 101      Q, QR = _wenzl_constants(q)               <- convention D, r = 2
 159      print(f" real-level branch (1, q*), q* = ...; ray (q*, 4] is DIAGNOSTIC")
 198      br  = scan(f, Q_LO, Q_STAR * (1 - 1e-5), ...)
 199      ray = scan(f, Q_STAR * (1 + 1e-5), Q_RAY_MAX, ...)
```

It does NOT import these from `threerow_qcross_trend_probe` — it is an independent
copy of the same convention-C constant. So fixing that probe does not fix this one,
and a grep for importers finds nothing.

Its object is again the ≥3-row sign crossing, which convention D sets to zero
(`schurPrincipal_eq_zero_iff`, `wenzlLevel_conventionD`). Under D there is no pole, so
the "real-level branch (1, q*)" and the "DIAGNOSTIC ray (q*, 4]" are a partition of
`q > 0` into two halves either side of a point with no significance — and the crossings
being scanned for are round-off in an identically-zero object.

## Why this one is WORSE than qou-qdtk, and should not just be copied over

**It emits no witness.** `find computations -name "*isospin-parity*"` returns nothing.
Per AGENTS.md's probe discipline, that is the more dangerous case, not the safer one:
*"a witness is a number that gets re-derived; a probe conclusion is an ARGUMENT that
gets written into a bean, an audit doc, a PR body and a content block, where nothing
re-derives it."* So there is no green-but-vacuous witness to correct here — the damage,
if any, is already downstream in prose. **Whoever takes this must first grep for where
its conclusions landed** (bean `qou-prjo`, #4832, and any audit doc citing an
isospin-dependent crossing) rather than starting from the file.

## Its own thesis may be independently sound — check before retiring

Unlike `qou-qdtk`, this probe's headline argument is a *confound* argument: that among
{D(1,1), T(1,2), ³He(2,1), ⁴He(2,2)} isospin and strand count move together, so the
four points cannot separate "Z=N" from "n an even multiple of 6". That reasoning is
combinatorial and does not depend on the convention at all — it may survive intact even
though the numerical crossing scan beneath it does not. Retiring the whole file would
discard it. Read the two apart.

Its cost table (Σ_λ (dim V_λ)² = n! exactly; n=18 ≈ 14 years/grid point) is likewise
convention-independent and worth keeping.

## Not attempted here

`qou-qdtk`'s PR rewrites one probe; this is a second full rewrite with a different
thesis, so it is recorded rather than bundled. Scope-(a), about this probe.
