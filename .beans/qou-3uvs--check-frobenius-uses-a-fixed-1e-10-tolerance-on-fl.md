---
# qou-3uvs
title: check_frobenius uses a FIXED -1e-10 tolerance on float64 values reaching 1e31 — the LP_stable verdict for ca40/fe56 is below its own noise floor
status: todo
type: task
created_at: 2026-09-05T06:46:39Z
updated_at: 2026-09-05T06:46:39Z
---


Found while working `qou-uiut`'s float64 excision. It bears directly on that
bean's headline result — the four `LP_stable` failures in
`hadron-knot-table.witness.json` — so read them together.

## The test

`tools/pyhecke/python/pyhecke/atom.py:279`

    def check_frobenius(nf):
        x = np.array(nf)
        Gx = G @ x
        violations = [(NF_NAMES[i], Gx[i]) for i in range(6) if Gx[i] < -1e-10]
        return len(violations) == 0, Gx, violations

Two problems, and they compound: the product is **float64** (`np.array` of an
already-float64 NF — see `qou-ejuy`), and the tolerance is a **fixed absolute
-1e-10** applied to values whose magnitude spans thirty orders.

## Measured, from the committed witness

    atom   stable  tr_M       max|nf|    float64 ulp at that scale
    ---------------------------------------------------------------
    o16    True    1.900e+01  1.540e+01  3.39e-15   far below 1e-10
    ne20   False   2.241e+02  3.541e+02  7.79e-14   below 1e-10
    si28   False   1.838e+06  4.166e+06  9.17e-10   COMPARABLE to 1e-10
    ca40   False   1.500e+15  3.805e+15  8.37e-01   10 orders ABOVE
    fe56   False   4.392e+30  1.149e+31  2.53e+15   25 orders ABOVE

For ca40 and fe56 the threshold sits far below float64's own resolution at
that magnitude. A `Gx[i]` whose true value is exactly 0 can compute as
±1e+15 from cancellation alone, and `-1e+15 < -1e-10` registers as a
violation. si28 is on the boundary.

## What this does and does not establish

It does NOT show the verdicts are wrong. If a violation is genuinely large and
negative — say Gx = -1e+30 — the answer is right regardless of the tolerance.

It shows the TEST CANNOT TELL THE TWO APART for ca40 and fe56. "Not
Frobenius-stable" is not established by this predicate at those scales; it is
only established where the ulp is below the threshold, which is up to ne20.

And the witness cannot settle it either, which is the second half of this bean:

    fe56 row keys: A, B_MeV, N, V_per_gen, Z, cross_channel_sum,
                   delta_xchan_MeV, frobenius_stable, knot_type, ln_abs_tr,
                   n_terms, name, net, nf, ordering, tr_M

`check_frobenius` RETURNS `(stable, Gx, violations)` and `hadron_knot_table`
unpacks all three — `stable, Gx, violations = check_frobenius(nf)` — then
records only the boolean. The evidence is computed and thrown away, so no
reader can check a False verdict without re-running the table. That is the
same shape as the `atom_frobenius_norm_sq` defect in `qou-8w8v`: the right
value is produced and the caller drops it.

## Scope

1. Record `Gx` and `violations` in the witness row. Cheap, no recompute
   needed beyond the next regeneration, and it makes every future verdict
   auditable. Do this first — it is what tells us whether 2 is urgent.
2. Make the tolerance SCALE-AWARE: compare against `-tol * max(1, ||Gx||_inf)`
   or similar, rather than a bare `-1e-10`. An absolute tolerance is simply
   the wrong shape for a quantity ranging over 1e1 to 1e31.
3. The float64 product itself is `qou-ejuy`. Fixing that removes the noise
   floor but NOT the tolerance-shape problem — an mpf `Gx` at 1e31 still needs
   a relative test.

## Correction this forces

`qou-uiut` and my session summary reported the four LP_stable failures as a
substantive finding, and said the trace growth "is intrinsic to the model".

The TRACE GROWTH claim stands: tr_M runs 19.0 (o16) -> 4.39e+30 (fe56), and
the braid-fix ratios (0.9070 / 0.8796 / 0.8770 / 0.8714) are reliable, because
a ratio of two float64 values of the same magnitude keeps ~16 digits.

The STABILITY VERDICT claim does not, for ca40 and fe56. It should have been
stated as "the predicate reports unstable, at a scale where the predicate
cannot resolve its own threshold".
