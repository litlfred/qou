# M1 mass table — combined mode + audit-trail fix

**Date:** 2026-05-12 (session 2)
**Branch:** `copilot/analyze-audit-reports-and-fix-calculations`
**Builds on:** [`2026-05-12-1ppb-implementation-plan.md`](2026-05-12-1ppb-implementation-plan.md), [`2026-05-11-model-b-mass-table.md`](2026-05-11-model-b-mass-table.md)

This is the M1 status snapshot after Phase 1 (P1.A, C, D) + Phase 2
(P2.A, P2.B) plumbing landed. M0 → M1 here is *purely the closure
infrastructure*; the underlying physics gap (Phase 3 closed-form
$\Delta_{\mathrm{coupling}}$ + ⁴He Model B knot) is unchanged.

## 1  Source

- Witness: `computations/sweeps/paper-six-term-isotope-sweep.witness.json`
- Generator: `paper_six_term_isotope_sweep.py` (run on this commit)
- Default `e0_mode = "substrate"` (P1.A, no calibration leak)
- Default `tower_mode` is iterated over all 8 modes; the row
  table below extracts the four canonical ones.

## 2  M1 table — substrate $E_0 \approx 4.186$ MeV/Hecke-unit (default)

`err_pct = (M_pred − M_CODATA) / M_CODATA × 100`; sign is signed.

| Atom | li2q (M0)   | habiro      | per-partition-k | combined (M1) | Sub-mode used by combined |
|------|------------:|------------:|----------------:|--------------:|---------------------------|
| p    | −97.600%    | −98.411%    | ERR (no cov.)   | −98.411%      | habiro                    |
| n    | −97.718%    | −98.476%    | ERR (no cov.)   | −98.476%      | habiro                    |
| D    | −98.148%    | −99.181%    | −99.012%        | −99.181%      | habiro                    |
| T    | −98.368%    | ERR (no cov.) | −99.908%       | −99.908%      | per-partition-k           |
| ³He  | −98.126%    | ERR (no cov.) | −99.320%       | −99.320%      | per-partition-k           |
| ⁴He  | −98.201%    | ERR (no cov.) | ERR (no cov.)  | −98.201%      | li2q                      |

**MAE on {p, n, D, T, ³He, ⁴He} under combined mode:** 98.749%.
**MAE on the same set under li2q (M0 default):** 98.027%.

### What this number means (audit-honest reading)

The substrate $E_0$ is the *anchor-discipline-respecting* energy
quantum: derived from CAL-1 ($m_e$) and CAL-2 ($q_0$) with no fit to
any mass observable. Multiplying it by the sum of the dimensionless
Hecke-units terms (T1+T2+T3+T4) gives a number that is structurally
~50× too small to reproduce nucleon mass scales. **This is expected
and intentional**:

- The mass scale at 1 GeV is set by **non-perturbative confinement**
  in the brane tower (Phase 3 closed-form $f$ for
  $\Delta_{\mathrm{coupling}}$).
- Substrate $E_0$ alone captures only the energy quantum per Hecke
  generator; bound-state binding is not yet folded in.
- The 98% gap is therefore the *honest closure target*, not a bug.

The previous M0 baseline doc (which showed −22% MAE) was reading
witnesses from the *proton-fit* calibration mode, which absorbs the
Phase-3-shaped $\Delta_{\mathrm{coupling}}$ into a fitted $E_0$. That
mode is still available (`QOU_E0_MODE=proton-fit` env var or
`run_sweep_for_mode(..., e0_mode="proton-fit")`) and stays useful for
order-of-magnitude sanity, but it is **not** anchor-discipline-clean.

## 3  Combined mode under proton-fit calibration is structurally invalid

If you re-run the sweep with `QOU_E0_MODE=proton-fit`, the per-mode
MAE table looks like this (excerpt from a manual run on this commit):

| Mode               | MAE     | Max err  | T − ³He pred | T − ³He CODATA |
|--------------------|--------:|---------:|-------------:|---------------:|
| li2q               | 21.33%  | 31.99%   | −283.49 MeV  | +0.019 MeV     |
| habiro             | 26.29%  | 48.46%   | —            | +0.019 MeV     |
| per-partition-k    | 99.41%  | 99.91%   | −16.52 MeV   | +0.019 MeV     |
| **combined**       | **43.43%** | **94.20%** | **−1039.07 MeV** | **+0.019 MeV** |

Combined under proton-fit is *worse* than li2q. The mechanism: $E_0$
is fit so the proton residual is exactly zero **under one specific
sub-mode** (here `habiro`, since combined routes proton to habiro).
But T and ³He are routed to `per-partition-k` whose tower numerics
have a different scale than habiro's; the habiro-fitted $E_0$ is
incompatible with them, so multiplying it by their (small) `total_hecke`
under-predicts their mass by ~99%.

**Recommendation in the production scripts:** combined mode must be
run only with `e0_mode="substrate"`. The script already auto-promotes
`per-partition-k` to substrate (line 757–761 of `paper_six_term_isotope_sweep.py`)
when proton-fit is requested but the sub-mode lacks proton coverage.
**Implemented in this session:** combined now does the same — when
called with `e0_mode="proton-fit"` it issues a `UserWarning` and
auto-promotes to `e0_mode="substrate"`, restoring coherent numbers
(combined under proton-fit no longer differs from combined under
substrate).

## 4  Audit-trail fix (this session)

Before this session, the `combined` branch in `paper_six_term_mass`
made a recursive call returning the sub-mode's row dict verbatim.
Result: a row in `all_modes["combined"].rows` would record
`tower_mode: "habiro"` (or "per-partition-k", "li2q"). An auditor
reading the witness would see "combined" in the section header and
"habiro" in the row — confusing and wrong.

Fix (commit on this session):

```python
result = paper_six_term_mass(..., tower_mode=sub_mode)  # recurse
result["tower_mode"] = "combined"     # outer label
result["sub_tower_mode"] = sub_mode   # which sub-mode actually ran
return result
```

The schema gains a uniform `sub_tower_mode` field on **every** row
(`None` on non-combined direct calls; the actual sub-mode on
combined). Witness consumers can rely on the field's presence.

Spot-check from the regenerated witness:

```
=== combined-mode rows: tower_mode + sub_tower_mode ===
   p   tower_mode=combined    sub_tower_mode=habiro
   n   tower_mode=combined    sub_tower_mode=habiro
   D   tower_mode=combined    sub_tower_mode=habiro
   T   tower_mode=combined    sub_tower_mode=per-partition-k
 ³He   tower_mode=combined    sub_tower_mode=per-partition-k
 ⁴He   tower_mode=combined    sub_tower_mode=li2q

=== sample non-combined row (li2q proton) ===
  tower_mode=li2q  sub_tower_mode=None
```

## 5  Forward path

1. **Phase 3 — closed-form $\Delta_{\mathrm{coupling}}$** is the
   only thing that can move the −98% gap. M1 is correct as a
   plumbing milestone; M2 (~0.1% on light) needs Phase 3.
2. **P1.B full backfill** ({n, D, T, ³He}) needs an environment with
   a higher CPU budget (each atom > 12 min in this sandbox); the
   per-atom CLI is in place.
3. **P1.B production wiring** of V1–V4 winner needs owner input on
   which mirror convention is canonical.
4. **P1.E ⁴He Model B knot** still needs owner input.
5. **Combined × proton-fit guard** — ✅ implemented this session (auto-promote with `UserWarning`).
