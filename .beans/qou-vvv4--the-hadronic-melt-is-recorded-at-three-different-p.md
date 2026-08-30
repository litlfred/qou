---
# qou-vvv4
title: The hadronic melt is recorded at three different points, and two of them are in sibling blocks that contradict each other
status: in-progress
type: task
priority: normal
created_at: 2026-08-30T14:42:14Z
updated_at: 2026-08-30T15:14:43Z
---

## Measured 2026-08-30 — the mechanism, and what it does to the melt

PR #6270. Probe `computations/hecke/h3_gram_degeneracy_is_wedderburn_weight_vanishing.py` (19/19),
Lean `QOU/Hecke/WedderburnWeightDegeneracy{,Real}.lean` (13 theorems, sorry-free, axioms clean).

**The Gram determinant IS the Wedderburn product.** Measured, not assumed:

    det G(u) / (y_(3) * y_(2,1)^4 * y_(1^3))|_{z=z_C}
      = -(u^4+1)^2 (u^2-u+1)^6 (u^2+u+1)^6 (u^4-u^2+1)^6 / u^28

no positive real zero, no positive real pole. So on u>0 every degeneracy of the
corpus Gram is a weight vanishing, and the recorded factorisation is explained:
`(u^3+u-1)^5` is `z_C = q` (kills y_(2,1) at d^2=4, plus y_(1^3) at 1);
`(u^3+u^2+1)^5` is `z_C = -1/q` (y_(2,1) at 4, plus y_(3) at 1). Multiplicity 5
is d^2 bookkeeping — 5 of the 6 dimensions of the regular representation.

**Under convention D there is no degeneracy at any real q.**
`y_(2,1)(z_D) = q^2/(q^2+1)^2 > 0`; `y_(1^3)(z_D) = 0` identically (the D
radical, = `gramMatrixD_det_eq_zero`); `y_(3)(z_D) = (q^4+1)/(q^2+1)^2`; sum = 1.
Scope-(b) with the invariant cited. Scope-(a) for "no hadronic melt" generally —
this excludes the Wedderburn/Gram route only.

**The two sibling blocks disagree, and the theorem block is the right one.**
`spectrahedral-phase-collapse-melt.md` says threshold `q = psi ~ 1.4655` and
"heated past"; the theorem + its sorry-free Lean give `u = 1/psi` with
`u = sqrt(q)`, so `q = 1/psi^2 ~ 0.4656`, and the melt hypothesis is
`u^3+u-1 < 0`, i.e. BELOW. Measured: y_(2,1)(z_C) < 0 for u < 1/psi, > 0 above,
= 0.2809 at the proton pin. NOT FIXED — needs an author decision about what the
melt block was trying to say. No `content/` touched.

**Three "supergolden" points, not one.** `u = 1/psi` (Gram, convention C);
`q = psi` (z_D = 1, tr_M collapses onto the counit); `u = -psi` (detFactor4,
outside the regime). I hypothesised the first two were the same point and
checked; they are not. Recorded as refuted rather than dropped.

**Strengthening of an existing corpus claim.** `qbeta-counit-closed-form.md`
says the trivial loop value "is never attained on the substrate" — about q_0.
Measured: `z_C = u/(u^2+1) <= 1/2` for ALL u>0, so under C eps = tr_M is
unreachable at EVERY q.

**Cross-check gained for free:** the derived `y_(1^3)(z)` reproduces the
2026-08-26 audit's form exactly, though that audit solved for it from the
descent condition and this solves the character-table system.

### Wrong turns, recorded

1. First det-vs-Wedderburn run declared `u` without `positive=True`, so
   `sqrt(u^2)` never simplified and the ratio came back carrying spurious
   `(u^3+u-1)^5` and `(u-1)` — it LOOKED like the prediction had failed.
2. Started from the hypothesis that `z_D = 1` (q = psi) was the same point as
   the Gram collapse (u = 1/psi). It is not; refuted before it was written down.

### Still open

- The melt block's location + direction: author decision, untouched here.
- Whether any convention-D transition exists by a NON-Wedderburn mechanism
  (SDP feasibility boundary not driven by weight vanishing, higher-n block,
  archimedean bound). Nothing here bears on it.
