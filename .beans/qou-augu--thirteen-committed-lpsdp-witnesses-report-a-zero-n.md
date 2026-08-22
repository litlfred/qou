---
# qou-augu
title: Thirteen committed LP/SDP witnesses report a zero net-constraint dual — mechanism confirmed for none of them
status: todo
type: task
priority: normal
created_at: 2026-08-22T12:19:51Z
updated_at: 2026-08-22T12:20:18Z
---


Split out of `qou/8na1`, which asked only whether the `a_K` chain divides by a
dual now known to be zero. It does not — all four divisions in the corpus are
guarded. The sweep that answered that question turned up something wider.

## The sweep

Every `computations/**/*.witness.json` carrying a `y0_star` field, flagged when
`max|y₀*| ≤ 1e-12`. **Thirteen** hit, of which `8na1` knew about two:

```
confinement-lp                              lp-duality-check
a-K-via-lp-dual-full            (known)     a-K-via-lp-dual-hecke-basis  (known)
all-nuclides-sdp-admissibility              co-bond-order-active-set
he3-pairknot-composite-lp                   molecular-frobenius-lp
pn-alpha-lp-dual                            frobenius-repose
qbeta-confinement-sdp-offset-homogeneity    qbeta-c3-barodd-binding-sdp-dual
qbeta-symbolic-sdp-strict-complementarity   wedderburn-pair-volumes
```

## What is NOT claimed

That these share `8na1`'s mechanism. `y_0_eq_zero_of_radical` needs three
things — a radical `v` with `Gv = 0`, a cost vector with `⟨t,v⟩ = 0`, and
`Σⱼvⱼ ≠ 0`. None of the thirteen has been checked against them.

Nine of the eleven producing scripts build a trace-form / Gram object, which is
where the mechanism lives. Two — `all_nuclides_sdp_admissibility.py`,
`co_bond_order_active_set.py` — mention neither `tr_M` nor a Gram, so **at
least two of the thirteen have a different cause**, whatever it is.

`qou/pin3` is the standing reason to be careful: it was filed as the same
degeneracy seen from the numerics, and it was not — `alpha_5_lp_dual_crystal.py`
builds `G = diag(|weight_λ|)`, has no radical at all, and its real problem was
a solver tolerance amplified by dividing by `|w| ~ 1e-06`. A shared symptom is
not a shared cause, and this bean exists to check rather than to assume.

The control that shows this is not "every LP in the corpus":
`rho-k-h3a-lp-dual` reports **`y₀* = 8.671`**. A real `scipy.linprog` solve
over a Wedderburn refinement with a Plancherel or Frobenius cost —
trace-adjacent, and not degenerate.

## Second finding: the guard threshold is below the band

The four divisions by a dual all guard at `1e-12`:

- `aK_via_lp_dual_full.py:198`, `aK_via_lp_dual_hecke_basis.py:191`,
  `probes/ak_lp_dual_quotient_probe.py:189` — each returns `None`
- `aK_via_lp_dual.py:185` divides by `|tr_M|`, not a dual

Two committed witnesses report a net-constraint dual **between** the guard and
any plausible physical scale:

- `borromean-axial-coupling` — `y₀* = 1.076e-10`
- `habiro-correction-shadow-price-test` — `5.949e-08`
  (`nucleus-real-sdp-he4`, `5.933e-08`)

Neither divides by it, so nothing is wrong today. But `1e-12` would **pass** on
`1.08e-10` and hand back a quotient inflated by ~1e10 with no signal. The guard
is calibrated to floating-point zero rather than to the scale at which these
solves actually report a vanishing dual — and `pin3` is the precedent for a
small denominator producing a large wrong number that reads as a result.

## Next

- [ ] For each of the nine trace-form scripts: does its `G` have a radical, and
      is its `t` orthogonal to it? That is the actual test, and the Lean lemma
      `y_0_eq_zero_of_radical` states the hypotheses to check.
- [ ] The two non-trace scripts: find the separate cause.
- [ ] Re-calibrate the four guards, or justify `1e-12` against the observed
      `1e-10`/`1e-8` band.
