---
# qou-bzj5
title: 'CHECK THEN REMARK at thm:buchberger: does LC in R^x buy back the field case over a commutative ground ring?'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T18:29:20Z
updated_at: 2026-10-04T15:16:54Z
parent: qou-q4oa
---

[bokutchen2015pbw] section 1 (pp. 2-3) notes that Groebner-Shirshov theory over a
commutative algebra K needs the double-free algebra M_{k[Y]}(X), with
lcm(u_Y u_X, v_Y v_X) = lcm(u_Y, v_Y) lcm(u_X, v_X). A composition relative to a
trivial lcm(u_X, v_X) is automatically trivial over a FIELD but not over a
commutative algebra when lcm(u_Y, v_Y) != u_Y v_Y, so a pair s1, s2 generally
admits infinitely many compositions.

The folio's Buchberger criterion (`thm:buchberger` / `thm:ugb-buchberger`) is
stated over a commutative R with A free as an R-module, and its S-polynomial
machinery requires unit leading coefficients (LC(f_i) in R^x, lambda in R^*;
see s-polynomial.md and s-polynomial-decomposition.md).

DO THE CHECK FIRST: do those unit conditions genuinely exclude the non-trivial
trivial-lcm compositions, or do they merely make them unreachable in the worked
examples? If they exclude them, write a one-line remark saying why the
commutative ground ring costs this chapter nothing, and cite section 1. If they
do not, that is a defect in thm:buchberger and needs its own bean. Do NOT write
the remark before the check.
