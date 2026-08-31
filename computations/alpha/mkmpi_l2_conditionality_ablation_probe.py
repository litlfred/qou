#!/usr/bin/env python3
"""m_K/m_pi's L2 pass is NOT conditional on the Witten-kappa `sorry`. Measured.

AGENTS.md states the framework's single scoreable L2 win is "truncation-fitted +
alpha_em-`sorry`-conditional", and concludes the count of unconditional
parameter-free sub-100x predictions is 0/5. This probe tests both halves of that
claim against the live stack. One half is STALE and the other is MIS-STATED --
but a third criticism, which AGENTS.md also makes, SURVIVES intact.

HALF ONE -- "truncation-fitted" -- IS STALE. The 2026-08-22 red team measured a
shipped 3-term truncation (3q^2-1)/(2q^2) at 23.45 ppb beating the untruncated
resummation 1+log(1+hbar_q) at 51.5 ppb, and called the truncation order
data-selected. That truncation has since been RETIRED: the live dashboard row
reports 51.48 ppb and its own source_witness field says "EM factor is the FULL
series". This probe reproduces both numbers so the retirement is checkable.

HALF TWO -- "sorry-conditional" -- CONFLATES TWO CLAIMS. It is true that alpha_em
as a FRAMEWORK-DERIVED quantity rests on an open Witten-kappa `sorry`. It does
NOT follow that the L2 VERDICT rests on it. Substituting the independently
measured CODATA alpha_em for the derived one moves the result

    51.4754 ppb  ->  51.428 ppb        (0.09 %)

and both pass the 263.6 ppb target by ~5.1x. So the pass survives the `sorry`
being unprovable: it does not depend on the derivation, only on alpha_em having
roughly its measured value.

WHAT SURVIVES, AND IT IS NOT SMALL. alpha_em's PRESENCE is entirely load-bearing
even though its VALUE is not: setting alpha_em := 0 gives 101553 ppb, 385x the
target. So the EM correction does real work. And using CODATA alpha_em makes this
a FOUR-input prediction rather than a three-calibration one, which is the
DOF-accounting criticism AGENTS.md also makes -- that one stands untouched, and
it is the honest residual objection to crediting this row.

NOT CLAIMED, explicitly:
  * That alpha_em's derivation is proved. The Witten-kappa `sorry` is open and
    this probe does not touch it.
  * That the DOF objection is answered. It is not; see above.
  * That the strong core alone suffices. It does not -- that is the 385x row.
  * Anything about the other four scoreable observables.

Scope (a): a measurement of what the L2 verdict is and is not contingent on.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
for p in (HERE.parent, HERE.parent / "substrate"):
    sys.path.insert(0, str(p))

import mpmath as mp

from meson_em_sinh_closed_form import alpha_em_inv_derived
from q_parameter import Q_50_DIGIT_STR

TARGET_PPB = mp.mpf("263.6")          # sigma_exp/100 for m_K/m_pi
ALPHA_CODATA = mp.mpf("0.0072973525693")   # CODATA 2018, an independent measurement

_results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    _results.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} — {detail}")


def main() -> int:
    mp.mp.dps = 60
    q = mp.mpf(Q_50_DIGIT_STR)
    h = 1 - 1 / q
    br = lambda n: (q**n - q ** (-n)) / (q - 1 / q)
    strong = br(3) * br(4)
    em_full = 1 + mp.log(1 + h)
    em_trunc = (3 * q**2 - 1) / (2 * q**2)
    pdg = mp.mpf("493.677") / mp.mpf("139.57039")

    a_der = 1 / alpha_em_inv_derived(q)
    ratio = lambda a, em: mp.sqrt(strong + (a / mp.pi) * em)
    ppb = lambda r: abs(r - pdg) / pdg * mp.mpf(10) ** 9

    print("=" * 72)
    print("  m_K/m_pi — what the L2 pass IS and IS NOT contingent on")
    print("=" * 72)

    shipped = ppb(ratio(a_der, em_full))
    codata = ppb(ratio(ALPHA_CODATA, em_full))
    noem = ppb(ratio(mp.mpf(0), em_full))
    trunc = ppb(ratio(a_der, em_trunc))

    print(f"\n  {'variant':<40} {'err_ppb':>12}")
    for lbl, v in (("FULL series, DERIVED alpha [SHIPPED]", shipped),
                   ("FULL series, CODATA alpha", codata),
                   ("FULL series, alpha_em := 0", noem),
                   ("3-term truncation [RETIRED]", trunc)):
        print(f"  {lbl:<40} {mp.nstr(v, 6):>12}")
    print(f"\n  100x target = {TARGET_PPB} ppb")

    print("\n-- the shipped formula is the FULL series, not the retired truncation")
    check("shipped_matches_dashboard_row",
          abs(shipped - mp.mpf("51.48")) < mp.mpf("0.01"),
          f"{mp.nstr(shipped, 6)} ppb vs the dashboard's 51.48 — the untruncated form")
    check("retired_truncation_is_a_different_number",
          abs(trunc - shipped) > mp.mpf("20"),
          f"the truncation gives {mp.nstr(trunc, 6)} ppb; it is not what ships")

    print("\n-- the VERDICT does not depend on which alpha_em is used")
    rel = abs(shipped - codata) / shipped
    check("derived_vs_codata_alpha_barely_moves_it",
          rel < mp.mpf("0.01"),
          f"{mp.nstr(shipped, 6)} -> {mp.nstr(codata, 6)} ppb, {mp.nstr(rel * 100, 3)} %")
    check("both_alphas_pass_the_100x_target",
          shipped < TARGET_PPB and codata < TARGET_PPB,
          f"by {mp.nstr(TARGET_PPB / shipped, 4)}x and {mp.nstr(TARGET_PPB / codata, 4)}x — "
          "so the pass survives the Witten-kappa sorry being unprovable")

    print("\n-- but alpha_em's PRESENCE is entirely load-bearing (the surviving criticism)")
    check("removing_the_EM_term_fails_by_a_wide_margin",
          noem > TARGET_PPB * 100,
          f"alpha_em := 0 gives {mp.nstr(noem, 6)} ppb = {mp.nstr(noem / TARGET_PPB, 4)}x "
          "the target — the strong core alone does not clear it")

    n_pass = sum(1 for _, ok, _ in _results if ok)
    print("\n" + "=" * 72)
    print(f"  {n_pass}/{len(_results)} assertions passed")
    print("  The L2 pass is NOT conditional on the Witten-kappa sorry: swapping the")
    print("  derived alpha_em for the measured one changes the answer by 0.09 % and")
    print("  it still passes by 5.1x. 'Truncation-fitted' is STALE — the truncation")
    print("  was retired and the full series ships. What SURVIVES is the DOF")
    print("  objection: with CODATA alpha_em this is a four-input prediction, not a")
    print("  three-calibration one. That is a real criticism and is untouched here.")
    print("  Scope (a). No value changed; nothing wired.")
    print("=" * 72)
    return 0 if n_pass == len(_results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
