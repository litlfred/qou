#!/usr/bin/env python3
"""The D-frame k=2 residual with the D-frame N=1 factor — the measurement the
convention-sensitivity probe could not make.

Bean `qou-cds1`, entry 17.  Scope (a).  Measures; proposes nothing.

## The gap this closes

The bean's convention table reports, for the D column, `c_3 ~ -974` and "no rung
convergence", from `qbeta_c3_ladder_trace_convention_sensitivity_probe`.  That
probe varies **only `z`**: its line 126 is

    q_n1 = q_a * mp.cos(alpha - b * hbar ** 2 / 2)

for BOTH conventions.  That cosine is the **convention-C** N=1 factor.  So the
recorded D column is a **HYBRID** — convention-D `z` inside a convention-C N=1
factor — not the D-frame ladder.  The bean says as much about the number
("a sensitivity measurement, not a proposed value ... what the *current
extractor* returns when fed `z_D`"); what it does not say is that the extractor
is C-framed in a second place besides `z`.

Entry 10 settled what the D-frame N=1 factor has to be, and it is not that one.
Under C the phase `a_C = (z_C - 1)h/2` is **bar-odd**, so `cos` is already
bar-invariant and the bar rule is vacuous.  Under D the phase carries a defect

    bar(a_D) + a_D = h^2 / 2                    (control, asserted below)

so `cos(a_D)` is NOT bar-invariant, and bar acts as reflection about `h^2/4`.
`QOU.QBeta.N1FactorUniqueness` (sorry-free) then forces the centre:

    barMidpoint_eq   (cos a + cos(bar a))/2 = cos(a - d/2) * cos(d/2)
    const_free       the centre d/2 is bar-invariant for ANY amplitude K
    phase_forced     for K != 0, bar-invariance holds IFF c = d/2 - k*pi
    uncentred_fails  the C-style uncentred phase FAILS under D

so the D-frame N=1 factor is `cos(a_D - h^2/4) * cos(h^2/4)`.

## What is computed

Three N=1 factors against the same `Q_A`, `u`, and the same structural
`c_2 = -1`, at the proton pin:

    C        z_C, cos(a_C - b*hbar^2/2)          the published baseline
    HYBRID   z_D, cos(a_D - b*hbar^2/2)          what the D column actually is
    D        z_D, cos(a_D - h^2/4)*cos(h^2/4)    the entry-10 forced form

and for each: the N=1 residual against CODATA `Q_beta`, the N=2 residual after
the structural rung, their ratio (does the rung help?), and the `c_3` an
extractor WOULD return.

## What this does NOT do

**No `c_3` is proposed, adopted, extracted into a cache, or wired.**  The `c_3`
column is reported for the same reason the sensitivity probe reports it — to
show what the machine would say — and every one of them is labelled.  The
convention-D refusal in `qbeta_ck_cache.py` is untouched and this file does not
call it.  `c_2 = -1` is used as the structural rung it is (no fit, no CODATA, no
q_0); nothing here re-derives or re-fits it.

Precision: mpmath at 60 dps end to end; `float()` appears nowhere.
Pin: proton, per the owner directive of 2026-08-07.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 60

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))


def l2_target_ppb() -> mp.mpf:
    """The canonical L2 target for Q_beta, from the dashboard — never a literal.

    Hard-won: the entry-9 probe took a ROUNDED 7.8e-7 out of a PSLQ probe's
    witness and reported a threshold 0.038 % off, then I "corrected" the right
    figure to the wrong one. Read the authoritative row or refuse.
    """
    dash = json.loads((ROOT / "per-observable-100x-status.witness.json").read_text())

    def find(o):
        if isinstance(o, dict):
            if o.get("obs") == "Q_beta" and "target_100x_ppb" in o:
                return o
            for v in o.values():
                r = find(v)
                if r:
                    return r
        elif isinstance(o, list):
            for v in o:
                r = find(v)
                if r:
                    return r
        return None

    row = find(dash)
    if row is None:
        raise SystemExit("REFUSING: no Q_beta row in per-observable-100x-status; "
                         "the L2 target must not be guessed or hardcoded")
    return mp.mpf(str(row["target_100x_ppb"]))


def frames(q: mp.mpf) -> dict:
    """The three N=1 framings against one substrate amplitude."""
    h = q - 1 / q
    hbar = (q - 1) / q
    b = mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar ** 2
    z_c = mp.sqrt(q) / (1 + q)
    z_d = q ** 3 / (q ** 2 + 1)
    a_c = (z_c - 1) * h / 2
    a_d = (z_d - 1) * h / 2
    q_a = ME * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)

    n1 = {
        # published baseline: C phase in the C-frame cosine
        "C": mp.cos(a_c - b * hbar ** 2 / 2),
        # what the sensitivity probe's D column actually computes
        "HYBRID": mp.cos(a_d - b * hbar ** 2 / 2),
        # entry 10's forced form: centred on the bar-midpoint h^2/4
        "D": mp.cos(a_d - h ** 2 / 4) * mp.cos(h ** 2 / 4),
    }
    out = {"h": h, "hbar": hbar, "b": b, "u": u, "z_C": z_c, "z_D": z_d,
           "a_C": a_c, "a_D": a_d, "Q_A": q_a, "rows": {}}
    for name, f in n1.items():
        qn1 = q_a * f
        qn2 = qn1 * (1 - u ** 2)                      # the structural c_2 = -1
        r1 = QCOD / qn1 - 1
        r2 = QCOD / qn2 - 1
        out["rows"][name] = {
            "N1_factor": f, "Q_N1": qn1, "Q_N2": qn2,
            "n1_res_ppb": r1 * mp.mpf(10) ** 9,
            "n2_res_ppb": r2 * mp.mpf(10) ** 9,
            "rung_gain": abs(r1 / r2) if r2 != 0 else mp.inf,
            "c3_extractor_would_return": r2 / u ** 3,
        }
    return out


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    def chk(name: str, ok: bool, why: str = "") -> None:
        checks.append((name, bool(ok), why))

    q0 = mp.mpf(q_at(55))
    F = frames(q0)
    u, h = F["u"], F["h"]
    target = l2_target_ppb()

    # ---- control: the entry-10 bar defect, re-derived symbolically here ----
    qs = sp.symbols("q", positive=True)
    hs = qs - 1 / qs
    zd_s = qs ** 3 / (qs ** 2 + 1)
    zc_s = sp.sqrt(qs) / (qs + 1)
    ad_s = (zd_s - 1) * hs / 2
    ac_s = (zc_s - 1) * hs / 2
    bar = lambda e: sp.simplify(sp.powsimp(sp.radsimp(e.subs(qs, 1 / qs)), force=True))  # noqa: E731
    chk("control_C_phase_is_bar_odd", sp.simplify(bar(ac_s) + ac_s) == 0,
        "bar(a_C) + a_C = 0 — cos is even, so the bar rule is VACUOUS under C; "
        "this is why the C-frame N=1 factor needs no centring")
    chk("control_D_defect_is_h_sq_over_2",
        sp.simplify(sp.simplify(bar(ad_s) + ad_s) - hs ** 2 / 2) == 0,
        "bar(a_D) + a_D = h^2/2 — so bar reflects about h^2/4 and the D-frame "
        "N=1 factor must be centred there (QOU.QBeta.N1FactorUniqueness)")

    # ---- the claim this probe exists to make ----
    hyb = F["rows"]["HYBRID"]["N1_factor"]
    dfr = F["rows"]["D"]["N1_factor"]
    chk("D_frame_N1_DIFFERS_from_the_hybrid_the_bean_measured",
        abs(hyb - dfr) / abs(dfr) > mp.mpf("1e-12"),
        f"HYBRID N1 = {mp.nstr(hyb, 16)} vs D-frame N1 = {mp.nstr(dfr, 16)}, "
        f"rel {mp.nstr(abs(hyb - dfr) / abs(dfr), 6)} — the sensitivity probe's D "
        "column varies only z and keeps the C-frame cosine, so it is NOT the "
        "D-frame ladder")

    rows = F["rows"]
    chk("C_frame_rung_HELPS", rows["C"]["rung_gain"] > 10,
        f"C: N1 {mp.nstr(rows['C']['n1_res_ppb'], 8)} ppb -> N2 "
        f"{mp.nstr(rows['C']['n2_res_ppb'], 8)} ppb, gain "
        f"{mp.nstr(rows['C']['rung_gain'], 6)}x — the ladder is C-built")

    # Does the entry-10 centring rescue convergence under D? Reported either way.
    d_gain = rows["D"]["rung_gain"]
    hyb_gain = rows["HYBRID"]["rung_gain"]
    chk("D_frame_rung_gain_MEASURED", True,
        f"D-frame (entry-10 centred): N1 {mp.nstr(rows['D']['n1_res_ppb'], 8)} ppb "
        f"-> N2 {mp.nstr(rows['D']['n2_res_ppb'], 8)} ppb, gain "
        f"{mp.nstr(d_gain, 6)}x   [HYBRID for comparison: {mp.nstr(hyb_gain, 6)}x]")
    chk("centring_does_NOT_rescue_C_like_convergence", d_gain < rows["C"]["rung_gain"],
        f"D-frame gain {mp.nstr(d_gain, 6)}x vs C-frame {mp.nstr(rows['C']['rung_gain'], 6)}x "
        "— the entry-10 centring is the RIGHT N=1 factor and still does not make the "
        "C-frame rung structure work under D. The ladder needs re-derivation, which "
        "is what qou-cds1 says; this measures it with the correct N=1 for the first time")

    # the c_3 an extractor would return — LABELLED, never adopted
    c3_d = rows["D"]["c3_extractor_would_return"]
    c3_h = rows["HYBRID"]["c3_extractor_would_return"]
    chk("c3_under_D_is_NOT_order_unity", abs(c3_d) > 100,
        f"an extractor fed the D-frame N=1 would return c_3 = {mp.nstr(c3_d, 10)} "
        f"(HYBRID gives {mp.nstr(c3_h, 10)}). NOT a proposed value and NOT wired — "
        "both are far outside the order-unity range the C-frame c_3 = -2.069 sits in, "
        "so 'one derived rung closes the gap' is a C-frame statement, as entry 9 scoped it")
    chk("the_two_D_numbers_are_NOT_the_same_measurement",
        abs(c3_d - c3_h) / abs(c3_h) > mp.mpf("1e-9"),
        f"the bean's recorded D column is the HYBRID {mp.nstr(c3_h, 10)}; with the "
        f"entry-10 N=1 factor it is {mp.nstr(c3_d, 10)}, differing by "
        f"{mp.nstr(abs(c3_d - c3_h) / abs(c3_h) * 100, 6)} %. Do not quote one for the other")

    # the threshold is convention-independent; restated here as the anchor
    thr = target / (u ** 4 * mp.mpf(10) ** 9)
    chk("entry9_threshold_is_unchanged_by_the_N1_framing",
        abs(thr - mp.mpf("1.4816")) < mp.mpf("0.001"),
        f"|c_4| <= target/u^4 = {mp.nstr(thr, 8)} regardless of which N=1 factor is "
        "used — u = b*hbar^2 carries no Markov parameter and no phase. Only the "
        "'can one rung close it' reading is frame-dependent")

    npass = sum(1 for _, ok, _ in checks if ok)
    print("=" * 78)
    print("  D-frame k=2 residual with the D-frame N=1 factor (qou-cds1 entry 17)")
    print("=" * 78)
    print(f"\n  q0 (proton) = {mp.nstr(q0, 20)}")
    print(f"  u           = {mp.nstr(u, 20)}")
    print(f"  h^2/4       = {mp.nstr(h ** 2 / 4, 16)}   (the bar-midpoint centre)")
    print(f"  L2 target   = {mp.nstr(target, 6)} ppb")
    print(f"\n  {'frame':<8} {'N1 factor':>20} {'N1 res ppb':>16} {'N2 res ppb':>16} "
          f"{'gain':>10} {'c_3 would-be':>16}")
    for nm in ("C", "HYBRID", "D"):
        r = rows[nm]
        print(f"  {nm:<8} {mp.nstr(r['N1_factor'], 16):>20} "
              f"{mp.nstr(r['n1_res_ppb'], 8):>16} {mp.nstr(r['n2_res_ppb'], 8):>16} "
              f"{mp.nstr(r['rung_gain'], 5):>10} "
              f"{mp.nstr(r['c3_extractor_would_return'], 10):>16}")
    print("\n  HYBRID = convention-D z inside the convention-C cosine — what the")
    print("  sensitivity probe's D column measures. D = entry-10's forced centring.\n")
    for n, ok, why in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {n}\n         {why}")
    print(f"\n  {npass}/{len(checks)} assertions passed\n")

    w = WitnessBuilder("qbeta-d-frame-n1-ladder-residual", engine="python+mpmath",
                       output_dir=HERE, _script_path=__file__)
    w.set_description(
        "The D-frame k=2 ladder residual computed with the D-frame N=1 factor. The "
        "convention-sensitivity probe's D column varies only z and keeps the C-frame "
        "cosine cos(a - b*hbar^2/2), so the c_3 ~ -974 recorded in qou-cds1's table is "
        "a HYBRID (D-frame z, C-frame N=1). Entry 10 forces the D-frame N=1 to be "
        "cos(a_D - h^2/4)*cos(h^2/4), since bar(a_D) + a_D = h^2/2 makes bar a "
        "reflection about h^2/4 (QOU.QBeta.N1FactorUniqueness, sorry-free). Measured "
        "with the correct N=1, the C-frame rung structure still does not transfer, "
        "confirming qou-cds1's 're-derive, do not re-evaluate' from the N=1 side as "
        "well as the z side. Scope (a): no c_k proposed, adopted or wired; the "
        "convention-D refusal in qbeta_ck_cache is untouched. The entry-9 threshold "
        "|c_4| <= target/u^4 is unaffected by the N=1 framing.")
    w.set_content_block("prop:q-beta-cos-resummation")
    w.add_parameter("q0_anchor", "proton (physical_proton pin)")
    w.add_parameter("q0", mp.nstr(q0, 50))
    w.add_data("l2_target_ppb", mp.nstr(target, 10))
    w.add_data("bar_midpoint_centre_h2_over_4", mp.nstr(h ** 2 / 4, 30))
    w.add_data("u_substrate", mp.nstr(u, 30))
    for nm in ("C", "HYBRID", "D"):
        r = rows[nm]
        w.add_data(f"{nm}_N1_factor", mp.nstr(r["N1_factor"], 30))
        w.add_data(f"{nm}_n1_res_ppb", mp.nstr(r["n1_res_ppb"], 20))
        w.add_data(f"{nm}_n2_res_ppb", mp.nstr(r["n2_res_ppb"], 20))
        w.add_data(f"{nm}_rung_gain", mp.nstr(r["rung_gain"], 20))
        w.add_data(f"{nm}_c3_extractor_would_return_NOT_ADOPTED",
                   mp.nstr(r["c3_extractor_would_return"], 20))
    w.add_data("assertions_passed", npass)
    w.add_data("assertions_total", len(checks))
    w.add_data("checks", [{"name": n, "pass": ok, "why": why} for n, ok, why in checks])
    w.add_data("scope", (
        "Scope (a). No c_k proposed, adopted, extracted into a cache or wired; both "
        "c_3 figures are what an extractor WOULD return and are labelled as such. "
        "qbeta_ck_cache's convention-D refusal is untouched and is not called. "
        "c_2 = -1 is used as the structural rung it is."))
    for n, ok, _ in checks:
        w.add_assertion(n, "pass" if ok else "fail", "pass")
    # save(), not build(): build() returns the dict WITHOUT writing. The first
    # version of this file called build() and then printed a success line
    # unconditionally, so it announced a witness that was never created. A print
    # is not evidence that a file exists -- hence the check below.
    out = w.save()
    if not Path(out).exists():
        raise SystemExit(f"REFUSING: witness was not written to {out}")
    print(f"\u2713 Witness: {Path(out).name}  ({len(checks)} assertions, "
          f"{npass} passed)")
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
