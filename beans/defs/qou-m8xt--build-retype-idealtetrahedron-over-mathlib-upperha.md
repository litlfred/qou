---
# qou-m8xt
title: 'BUILD: retype IdealTetrahedron over Mathlib UpperHalfPlane (ℍ) — 62 QOU files hand-roll 0 < im, zero use ℍ'
status: todo
type: task
priority: normal
created_at: 2026-09-04T09:08:08Z
updated_at: 2026-09-04T09:08:08Z
parent: qou-8lxd
---

**BUILD.** `QOU/MathlibExt/IdealTriangulation.lean:66-70` is

    structure IdealTetrahedron where
      shape : ℂ
      im_pos : 0 < shape.im

That is `Mathlib.Analysis.Complex.UpperHalfPlane.ℍ`, spelled out.

**Measured 2026-09-04** (mathlib `f897ebcf72c`, `grep -rn 'UpperHalfPlane' QOU/`):
`UpperHalfPlane` occurs in **2** QOU files and in **zero** QOU declarations — both hits
are audit prose (`Archimedean/HyperbolicVolumeMeasure.lean:9`,
`Eightfold/HyperbolicVolumeFormType.lean:137`). Meanwhile **62** QOU files carry a
hand-rolled `im_pos` / `0 < _.im`.

**What retyping over `ℍ` buys**, all present at the pin:
* `UpperHalfPlane.im_pos`, `ne_zero`, `normSq_pos`, `re_add_im`, `ext'`;
* the `positivity` extensions `evalUpperHalfPlaneIm` / `evalUpperHalfPlaneCoe`, so
  `0 < z.im` side goals discharge automatically;
* the `{x : ℝ // 0 < x}` scaling and `ℝ`-translation actions (`posRealAction`,
  `AddAction ℝ ℍ`);
* `MoebiusAction.lean` (389 lines) — the `GL(2,ℝ)⁺` and `SL(2,R)` Möbius actions, the
  natural home for the shape-parameter cycle `z ↦ 1/(1−z) ↦ 1 − 1/z`;
* `Metric.lean` (341 lines) — the hyperbolic distance on ℍ², `Dist ℍ`, `dist_eq`,
  `cosh_dist`, and isometries including `ModularGroup.S`.

**Size: small-to-medium.** Mechanically it is a retype plus `.coe` insertions, but it
touches a load-bearing structure (`IdealTetrahedron.volume`, `volume_rotate`, the
gluing equations, `ManifoldVolumeBridge`, `ManifoldVolumePositive`) so it needs a real
`lean`-direct pass, not a sed.

**Sequence:** do the `BlochWigner_unit_circle` build first — it is ~5 lines and free.

**Scope note:** this is ℍ², i.e. the 2-dimensional layer only. It does **not** touch
the ℍ³ gap (`qou-5gai`), which is real and unaffected.

Source: `docs/audits/2026-09-04-mathlib-infrastructure-inventory.md` §B4, §H1.
