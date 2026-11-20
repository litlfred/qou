#!/usr/bin/env python3
"""qbeta_constant_residue_character_doubling_probe.py -- the hyperbolic branch
route 5 just re-opened is itself closed for CONSTANT residues, by the cosh
doubling identity; and the cross-anchor prune that would have been the obvious
test CANNOT work here, for a measured reason.

Beans `qou-pdix` / `qou-cds1`, route 5.  Scope-(b) for the constant-residue
exclusion, citing a proved identity (`QOU/QBeta/CharacterDoubling.lean`,
sorry-free); scope-(a) for every number.  Reports one FAILED prune as a failure.

## Where this picks up

`qbeta_ruled_base_inverts_the_route5_obstruction_probe` (same PR) measured that
step 18's exclusion of a real-spectrum holonomy carries the hypothesis
`kappa < 1`, and that on the owner-ruled base `kappa > 1` -- so the hyperbolic
branch re-opens.  Re-opening a branch is not a result; the branch has to be
worked.  This works it.

## 1. The prune that FAILED, and why it could never have worked

The obvious test is cross-anchor rigidity, which this corpus uses elsewhere:
solve for the constant and see whether the proton and muon pins agree.  It is
**useless here**, and the reason is sensitivity rather than luck.  Measured,
with the two pins 11.6141 ppb apart:

    quantity                     rel swing     AMPLIFICATION (swing / rel dq)
    c  (z_D order-zero)         9.71466e-8                      8.36
    c  (dashboard, LIVE)         1.1122e-7                      9.58
    c_3 (recorded)               0.0239121                  2.05889e+6

`c_3` is amplified ~2.06e6 because it is extracted through `1/u^3`; `c` has no
such magnifier and is amplified ~10.  The ratio is **2.15e5**, so a test that
separates `c_3` across these anchors cannot separate `c` at all.  **Do not read
the agreement as evidence that `c` is anchor-independent** -- it is evidence
that this test has no power here.  Reported as a failed prune, not a finding.

(The proton `c_3` is the canonical extraction `qbeta_ck_cache.py` performs,
recomputed via `qbeta_utils.c3_proton_extracted` -- dividing by the N=2 ladder
value, not the bare base; my own first re-derivation divided by the bare base and
gave -2710.  The muon `c_3` is AGENTS.md's recorded CODATA-2022 extraction.  The
swing reproduces the recorded 2.3912 %.)

## 2. The prune that WORKS: the cosh doubling identity

Kohno-Drinfeld fixes `hbar = 2 ln q`, so a constant-residue generator eigenvalue
is `c * ln q`.  `PhaseFailsLogFunctionalEquation` excludes this on the ELLIPTIC
reading via `ln(q^2) = 2 ln q`.  The hyperbolic reading observes the *character*
rather than the angle, so the analogue is the cosh double-angle law:

    chi(q^2) = 2 chi(q)^2 - 1        for EVERY c at once

Measured, the requirement function `kappa(q) = Q_codata / (Q_base(q)(1-u^2))`
misses it by 59-70 % at `q in {q0, 1.5, 2, 3}` -- against a genuine character,
which satisfies it to 1e-61.

## 3. The check my own argument needed, and it survives it

The identity is **not scale-invariant**, and `kappa` carries the experimental
`Q_codata` as an overall scale -- so a rescaling might have rescued it.  It does
not: solving `2 lam^2 kappa(q)^2 - lam kappa(q^2) - 1 = 0` gives a `lam(q)` that
spreads **28.86 %** over five points, against `lam == 1` exactly for a genuine
character.  One constant cannot do it.

## Scope, and what stays open

Scope-(b) applies to *"as a FUNCTION of q"* only.  **At a point the exclusion
does not hold**: at `q0` alone the free `c` reaches any `kappa >= 1`, so a
pointwise match is always available and carries no information.  What survives
is exactly what survives the elliptic sibling -- a q-DEPENDENT residue, a
non-flat construction, or a genuinely q-dependent-parameter transcendental
object.  Step 18 claimed to close all three "by a sign argument that never reads
the residues"; that argument is the one the ruled base voids.

## Discipline

`c` at the live cell is 5.96832, which is 0.5281 % from 6.  Recorded as a
check-AGAINST and **not pursued**: per NO FITTING a near-integer found by
solving against the target is selection against the target, and the cell is
provisional besides -- the 2026-09-13 owner ruling records that its element
`nuc11_interleaved` FAILS the confinement SDP on `(2,1)` and `(1,1,1)`, so `c`
moves when the element is replaced.  No search was run for a reason `c` should
be 6, and none should be until something independent selects one.

## Precision

mpmath at 60 dps; `q_0` from `q_at` (proton pin, canonical) with `q_muon_at`
used only for the explicit two-pin comparison of section 1 (exception E1 of the
2026-08-30 owner ruling).  No float64: no `float(` outside display, no
`statistics`, no `math.`.
"""
from __future__ import annotations

import pathlib as _pl
import sys as _sys

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    if str(_p) not in _sys.path:
        _sys.path.insert(0, str(_p))

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from q_parameter import q_at, q_muon_at  # noqa: E402
from qbeta_utils import c3_proton_extracted  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = 60
_EXPECTED_PREFIX = "0.651856310060"

# Proton c_3: recomputed by the canonical extraction inside main() (a typed copy
# carried here until 2026-10-13 is reproduced by no producer). Muon: AGENTS.md's
# recorded CODATA-2022 extraction (see docstring section 1).
C3_MUON_2022 = "-2.01986031"

def _dashboard_qbeta_mev():
    """Read the scored Q_beta cell from the dashboard witness, at FULL precision.

    Hardcoding the 12-digit truncation silently loses ~5e-13 and, worse, goes
    stale without saying so -- the exact defect this arc keeps documenting. The
    witness carries 60 digits; reading it turns a staleness hazard into a
    failing assertion. `_EXPECTED_PREFIX` is the value this probe's prose was
    written against, so a dashboard move is LOUD rather than invisible.
    """
    import json
    w = _COMP / "per-observable-100x-status.witness.json"
    if not w.exists():
        raise SystemExit(f"dashboard witness missing: {w}")
    d = json.loads(w.read_text())
    v = d.get("data", {}).get("qbeta_ruled_base", {}).get("Q_beta_MeV")
    if v is None:
        for r in d.get("data", {}).get("rows", []) or d.get("rows", []):
            if r.get("obs") == "Q_beta":
                v = r.get("pred_MeV")
                break
    if v is None:
        raise SystemExit("dashboard witness carries no Q_beta cell")
    if not str(v).startswith(_EXPECTED_PREFIX):
        raise SystemExit(
            f"DASHBOARD MOVED: witness Q_beta = {v}, this probe's prose was "
            f"written against {_EXPECTED_PREFIX}. Re-read the prose before "
            f"re-running -- do not just update the literal."
        )
    return str(v)

RESULTS: list[dict] = []


def check(name: str, passed: bool, detail: str) -> None:
    RESULTS.append({"name": name, "passed": bool(passed), "detail": detail})
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}\n         {detail}\n")


def main() -> int:
    set_compute_dps(DPS)
    mp.dps = DPS

    print("=" * 78)
    print(" constant-residue characters obey a doubling law; the requirement does not")
    print("=" * 78)

    m_e = mp.mpf(str(M_E_MEV))
    q_cod = mp.mpf(str(Q_BETA_MEV))
    q0 = q_at(DPS)
    q_mu = q_muon_at(DPS)

    def kappa_zD(q):
        """The requirement as a FUNCTION of q, on the z_D order-zero base."""
        h = q - 1 / q
        hbar = (q - 1) / q
        b = mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
        u = b * hbar ** 2
        z_d = q ** 3 / (q ** 2 + 1)
        import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
        E0 = _qbeta_e0.order_zero_scaled(m_e, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
        return (q_cod / (abs(h ** 2 / 2 - h * z_d) * E0)) / (1 - u ** 2)

    def kappa_dash(q):
        h = q - 1 / q
        hbar = (q - 1) / q
        b = mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
        u = b * hbar ** 2
        return (q_cod / mp.mpf(_dashboard_qbeta_mev())) / (1 - u ** 2)

    # ---- 1. the FAILED cross-anchor prune, and its measured reason ---------
    rel_dq = abs(q0 - q_mu) / q0
    amp_rows = []
    for nm, f in (("c (z_D order-zero)", kappa_zD), ("c (dashboard, LIVE)", kappa_dash)):
        cp = mp.acosh(f(q0)) / mp.log(q0)
        cm = mp.acosh(f(q_mu)) / mp.log(q_mu)
        rel = abs(cp - cm) / abs(cp)
        amp_rows.append({"quantity": nm, "proton": fmt(cp), "muon": fmt(cm),
                         "rel_swing": fmt(rel), "amplification": fmt(rel / rel_dq)})
    c3p, c3m = c3_proton_extracted(DPS), mp.mpf(C3_MUON_2022)
    rel_c3 = abs(c3p - c3m) / abs(c3p)
    amp_c3 = rel_c3 / rel_dq
    amp_rows.append({"quantity": "c_3 (recorded)", "proton": fmt(c3p),
                     "muon": C3_MUON_2022, "rel_swing": fmt(rel_c3),
                     "amplification": fmt(amp_c3)})

    print(f"  pins differ by {mp.nstr(rel_dq * 10 ** 9, 6)} ppb\n")
    print(f"    {'quantity':<22}{'rel swing':>16}{'amplification':>18}")
    for r in amp_rows:
        print(f"    {r['quantity']:<22}{mp.nstr(mp.mpf(r['rel_swing']), 6):>16}"
              f"{mp.nstr(mp.mpf(r['amplification']), 6):>18}")
    print()

    amp_c = rel_dq and (abs(mp.acosh(kappa_dash(q0)) / mp.log(q0)
                            - mp.acosh(kappa_dash(q_mu)) / mp.log(q_mu))
                        / abs(mp.acosh(kappa_dash(q0)) / mp.log(q0))) / rel_dq
    check(
        "cross_anchor_prune_FAILS_and_the_reason_is_sensitivity",
        amp_c3 / amp_c > mp.mpf(10) ** 4,
        f"c agrees across the two pins to ~1e-7 relative, and that is NOT "
        f"evidence of anchor-independence -- the test has no power here. "
        f"c_3 is amplified {mp.nstr(amp_c3, 6)}x (extracted through 1/u^3); c "
        f"is amplified {mp.nstr(amp_c, 6)}x (no magnifier). Ratio "
        f"{mp.nstr(amp_c3 / amp_c, 6)}x. Recorded as a FAILED prune. The c_3 "
        f"swing reproduces AGENTS.md's recorded 2.3912 % "
        f"({mp.nstr(rel_c3 * 100, 6)} %), which is the calibration.",
    )

    # ---- 2. the identity holds exactly for a genuine character ------------
    ctrl = []
    for c_str in ("0.5", "5.96831598119334", "11.1682695203772", "-3.2"):
        c = mp.mpf(c_str)
        chi = lambda x, c=c: (x ** c + x ** (-c)) / 2
        d = chi(q0 ** 2) - (2 * chi(q0) ** 2 - 1)
        ctrl.append({"c": c_str, "defect": fmt(d)})
    worst_ctrl = max(abs(mp.mpf(r["defect"])) for r in ctrl)
    check(
        "doubling_identity_is_exact_for_a_genuine_constant_residue_character",
        worst_ctrl < mp.mpf(10) ** -50,
        f"chi(q^2) - (2 chi(q)^2 - 1) is at most {mp.nstr(worst_ctrl, 4)} over "
        f"c in {{0.5, 5.968, 11.168, -3.2}} -- zero to the arithmetic's floor, "
        f"for every c. Proved in general by "
        f"QOU.QBeta.CharacterDoubling.char_doubling_of_constant_residue "
        f"(sorry-free), which is the hyperbolic analogue of ln(q^2) = 2 ln q.",
    )

    # ---- 3. the requirement function fails it, everywhere ------------------
    pts = [q0, mp.mpf("1.5"), mp.mpf("2"), mp.mpf("3")]
    fails = []
    print("    q            kappa(q^2)        2kappa(q)^2-1        rel defect")
    for x in pts:
        lhs = kappa_zD(x ** 2)
        rhs = 2 * kappa_zD(x) ** 2 - 1
        rel = abs(lhs - rhs) / abs(rhs)
        fails.append({"q": fmt(x), "lhs": fmt(lhs), "rhs": fmt(rhs),
                      "rel_defect": fmt(rel)})
        print(f"    {mp.nstr(x, 10):<13}{mp.nstr(lhs, 12):>14}{mp.nstr(rhs, 12):>20}"
              f"{mp.nstr(rel * 100, 6):>18} %")
    print()
    worst = min(mp.mpf(r["rel_defect"]) for r in fails)
    check(
        "requirement_function_fails_the_doubling_identity_at_every_point",
        worst > mp.mpf("0.5"),
        f"kappa(q) = Q_codata/(Q_base(q)(1-u^2)) on the z_D base misses "
        f"chi(q^2) = 2 chi(q)^2 - 1 by at least {mp.nstr(worst * 100, 5)} % "
        f"across q in {{q0, 1.5, 2, 3}} -- so it is the character of NO "
        f"constant-residue holonomy, for any c at once "
        f"(QOU.QBeta.CharacterDoubling."
        f"not_constant_residue_character_of_doubling_fails).",
    )

    # ---- 4. and no rescaling rescues it -----------------------------------
    def lam_at(q):
        A = 2 * kappa_zD(q) ** 2
        B = kappa_zD(q ** 2)
        return (B + mp.sqrt(B ** 2 + 4 * A)) / (2 * A)

    lams = [lam_at(x) for x in [q0, mp.mpf("1.2"), mp.mpf("1.5"), mp.mpf("2"), mp.mpf("3")]]
    spread = (max(lams) - min(lams)) / min(lams)
    c_ctrl = mp.mpf("5.96831598119334")
    kc = lambda x: (x ** c_ctrl + x ** (-c_ctrl)) / 2
    lam_ctrl = []
    for x in [q0, mp.mpf("1.5"), mp.mpf("2")]:
        A, B = 2 * kc(x) ** 2, kc(x ** 2)
        lam_ctrl.append((B + mp.sqrt(B ** 2 + 4 * A)) / (2 * A))
    ctrl_dev = max(abs(v - 1) for v in lam_ctrl)
    check(
        "no_rescaling_rescues_it_so_the_prune_is_not_a_normalisation_artifact",
        spread > mp.mpf("0.1") and ctrl_dev < mp.mpf(10) ** -40,
        f"The doubling identity is NOT scale-invariant and kappa carries the "
        f"experimental Q_codata as an overall scale, so a single lambda might "
        f"have rescued it. Solving 2 lam^2 kappa(q)^2 - lam kappa(q^2) - 1 = 0 "
        f"gives lam(q) spreading {mp.nstr(spread * 100, 6)} % over five points, "
        f"against |lam - 1| <= {mp.nstr(ctrl_dev, 4)} for a genuine character. "
        f"One constant cannot do it.",
    )

    # ---- 5. the exclusion is about the FUNCTION, never the point ----------
    c_dash = mp.acosh(kappa_dash(q0)) / mp.log(q0)
    pointwise_ok = abs(mp.cosh(c_dash * mp.log(q0)) - kappa_dash(q0))
    check(
        "at_a_point_the_exclusion_does_NOT_hold_and_that_is_the_scope",
        pointwise_ok < mp.mpf(10) ** -40,
        f"At q0 alone the free c reaches the requirement exactly: c = "
        f"{mp.nstr(c_dash, 15)} gives cosh(c ln q0) = kappa to "
        f"{mp.nstr(pointwise_ok, 4)}. So scope-(b) covers 'as a FUNCTION of q' "
        f"ONLY; a pointwise match is always available and carries no "
        f"information. Quoting this exclusion without that scope would be the "
        f"over-claim AGENTS.md's (a)/(b) rule exists to prevent.",
    )

    # ---- 6. the near-integer, recorded and NOT pursued --------------------
    near = mp.nint(c_dash)
    off = abs(c_dash - near) / abs(near)
    check(
        "the_near_integer_is_recorded_as_a_check_against_and_not_pursued",
        off > 0,
        f"c at the live cell is {mp.nstr(c_dash, 12)}, which is "
        f"{mp.nstr(off * 100, 4)} % from {int(near)}. Recorded as a "
        f"check-AGAINST and NOT pursued: a near-integer found by solving "
        f"against the target is selection against the target (NO FITTING), and "
        f"the cell is provisional besides -- the 2026-09-13 owner ruling "
        f"records that its element nuc11_interleaved FAILS the confinement SDP "
        f"on (2,1) and (1,1,1), so c moves when the element is replaced. No "
        f"search was run for a reason c should be {int(near)}.",
    )

    # ---- 7. the SECOND survivor is vacuous, not open ----------------------
    kap_scan = []
    worst_k = None
    for s in ("1.001", "1.01", "1.05", "1.1", "1.2", "1.5", "2", "3", "5", "10"):
        x = mp.mpf(s)
        kv = kappa_zD(x)
        kap_scan.append({"q": s, "kappa": fmt(kv), "ge_one": bool(kv >= 1)})
        worst_k = kv if worst_k is None or kv < worst_k else worst_k
    check(
        "the_q_dependent_residue_survivor_is_VACUOUS_not_open",
        worst_k >= 1,
        f"cosh is onto [1, inf), so wherever 1 <= kappa a q-dependent residue "
        f"reproducing it exists BY CONSTRUCTION -- one sets "
        f"a(q) := arcosh(kappa(q)), reading the residue off the answer. "
        f"Measured, kappa on the z_D base stays >= 1 throughout q in (1, 10] "
        f"(min {mp.nstr(worst_k, 12)} at the low end, rising to "
        f"{mp.nstr(kappa_zD(mp.mpf(10)), 12)} at q = 10), so the vacuity is not "
        f"conditional in the physical domain. Proved in general by "
        f"QOU.QBeta.CharacterDoubling.exists_q_dependent_residue_of_one_le. "
        f"Same disposition EigenphaseCarrierVacuity gives the elliptic "
        f"trichotomy's middle branch ('M arbitrary -- CIRCULAR'), reached "
        f"independently on the hyperbolic side. Only a residue whose "
        f"q-dependence is DERIVED can carry content.",
    )

    allp = all(r["passed"] for r in RESULTS)
    print(f"  {sum(r['passed'] for r in RESULTS)}/{len(RESULTS)} checks passed")

    wb = WitnessBuilder("qbeta-constant-residue-character-doubling", engine="mpmath")
    for r in RESULTS:
        wb.add_assertion(r["name"], computed="PASS" if r["passed"] else "FAIL",
                         expected="PASS", tolerance="exact", source=r["detail"])
    wb.save({
        "description": (
            "The hyperbolic branch that the ruled base re-opens for route 5 is "
            "itself closed for CONSTANT residues. Kohno-Drinfeld fixes "
            "hbar = 2 ln q, so a constant-residue generator eigenvalue is "
            "c*ln q and its character is cosh(c ln q), which satisfies "
            "chi(q^2) = 2 chi(q)^2 - 1 for EVERY c (the cosh double-angle law; "
            "the hyperbolic analogue of the ln(q^2) = 2 ln q identity that "
            "PhaseFailsLogFunctionalEquation uses to exclude the same holonomy "
            "on the elliptic reading). The requirement function "
            "kappa(q) = Q_codata/(Q_base(q)(1-u^2)) on the z_D base misses that "
            "identity by 59-70 % across q in {q0, 1.5, 2, 3}, and no rescaling "
            "rescues it (lambda(q) spreads 28.86 % against lambda == 1 for a "
            "genuine character). ALSO REPORTS A FAILED PRUNE: cross-anchor "
            "rigidity, the obvious test, has no power here -- c is amplified "
            "~9.6x across the two pins while c_3 is amplified ~2.06e6x through "
            "its 1/u^3 extraction, a ratio of 2.15e5, so the pins' agreement on "
            "c is evidence about the test and not about c. SCOPE: (b) for 'as a "
            "FUNCTION of q' only; at a single q0 the free c reaches any "
            "kappa >= 1 and the exclusion does NOT hold. What survives is what "
            "the elliptic sibling leaves open -- a q-dependent residue, a "
            "non-flat construction, or a q-dependent-parameter transcendental "
            "object."
        ),
        "bean": "qou-pdix",
        "also": "qou-cds1",
        "q0Anchor": "proton",
        "q0Value": fmt(q0),
        "cross_anchor_amplification": amp_rows,
        "doubling_control": ctrl,
        "doubling_defect_by_point": fails,
        "rescaling_lambda_spread": fmt(spread),
        "kappa_ge_one_scan": kap_scan,
        "invariant_cited": (
            "QOU.QBeta.CharacterDoubling (sorry-free, this PR): cosh_doubling, "
            "char_doubling_of_constant_residue, "
            "not_constant_residue_character_of_doubling_fails -- the last "
            "quantified over all c at once, exactly as its elliptic sibling "
            "QOU.QBeta.PhaseFailsLogFunctionalEquation is."
        ),
        "failed_prune_recorded": (
            "cross-anchor rigidity. Reported as a failure with its measured "
            "reason rather than omitted: the two pins are 11.6141 ppb apart and "
            "c carries no magnifier, so the test is 2.15e5 times less sensitive "
            "here than where the corpus uses it. An agent reading only the "
            "agreement would conclude c is anchor-independent, which this does "
            "NOT show."
        ),
        "not_pursued": (
            "c = 5.96832 at the live cell is 0.5281 % from 6. Check-AGAINST "
            "only. Selection against the target is forbidden (NO FITTING), and "
            "the cell is provisional -- its element nuc11_interleaved fails the "
            "confinement SDP per the 2026-09-13 owner ruling."
        ),
        "scope": (
            "(b) for the constant-residue exclusion AS A FUNCTION, citing a "
            "proved identity; (a) for every number; explicitly NOT an exclusion "
            "at a point. Derives no alpha, selects no base, wires nothing."
        ),
    })
    return 0 if allp else 1


if __name__ == "__main__":
    raise SystemExit(main())
