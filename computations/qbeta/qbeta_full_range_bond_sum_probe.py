#!/usr/bin/env python3
"""Option (a): sum the derived letters at their OWN range, not truncated at contact.

`qbeta_channel_range_growth_class_probe.py` measured a self-inconsistency: the
bond law truncates at graph distance 1, while the framework's own decay rate
`mu = -ln b` reaches an effective 173.2 fcc sites for `b_pp` against 12 contacts
(14.4x). This probe restores the range with NO new parameter and scores it.
Bean `qou-adr0`; option (a) of `qou-556v`.

*** THE LAW BEING TESTED ***

A pair at graph distance `d` gets weight `L_type . b_type^(d-1)`, so `d = 1`
reproduces the contact law EXACTLY and longer pairs decay at that letter's own
rate. Written out for a chain,

    S_full = L_pp Sum_d (pp pairs at d) b_pp^(d-1)
           + L_pn Sum_d (pn pairs at d) b_pn^(d-1)
           + L_nn Sum_d (nn pairs at d) b_nn^(d-1)

⚠ **THE IDENTIFICATION IS A MODELLING CHOICE, NOT A THEOREM.** It says the same
`b` that suppresses the trace per bond also sets the range. That is the natural
reading of the one-free-parameter structure and it is what makes option (a) cost
nothing — but nothing in the corpus derives it, and it is labelled here rather
than assumed.

*** THE COMPARATOR IS SCALE-FREE, DELIBERATELY ***

Full range multiplies the chain sum by roughly `1/(1-b)` — 2.58x (pp), 2.03x
(pn), 1.68x (nn) — so the ABSOLUTE scale must get worse: the contact chain
already over-binds (median `B_AME/B_pred = 0.886`). The question worth asking is
whether restoring the range improves the SHAPE, which a uniform factor cannot
touch. So the primary scores are the p25-p75, p5-p95 and full spreads of
`B_AME/B_pred`, the same comparator the merged arc uses. The scale is reported
separately rather than hidden inside a scale-free number.

*** PAIR COUNTS AT DISTANCE d ON A SEGREGATED CHAIN p^Z n^N ***

    pp at d : Z - d           for 1 <= d <= Z-1
    nn at d : N - d           for 1 <= d <= N-1
    pn at d : min(Z, d, N, A-d)

(checked against brute force at small A in this probe, not asserted).
"""
from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

DPS = 30
mp.mp.dps = DPS
Q0 = mp.mpf("1.1099785827513808075916690956107688798744991218736")
TWO_Q = Q0 + 1/Q0
B_PP = Q0**2/TWO_Q
B_NN = Q0**-2/TWO_Q
B_PN = ((Q0**10 - 2*Q0**9 + 7*Q0**8 - 2*Q0**6 + 4*Q0**5 + 4*Q0**4
         + Q0**2 - 2*Q0 + 1)/(12*Q0**5*(Q0**2 + 1)))
L_PP, L_PN, L_NN = -mp.log(B_PP), -mp.log(B_PN), -mp.log(B_NN)
AME = ROOT / "qou-mass/src/qou_mass/data/ame2020.json"


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def brute_counts(Z, N):
    """Explicit pair census on the segregated chain — the control for the closed forms."""
    A = Z + N
    kinds = ["p"]*Z + ["n"]*N
    out = {"pp": {}, "pn": {}, "nn": {}}
    for i in range(A):
        for j in range(i + 1, A):
            t = "pp" if kinds[i] == kinds[j] == "p" else (
                "nn" if kinds[i] == kinds[j] == "n" else "pn")
            out[t][j - i] = out[t].get(j - i, 0) + 1
    return out


def closed_counts(Z, N, d):
    """(pp, pn, nn) pair counts at chain distance `d`, segregated layout."""
    A = Z + N
    return (max(0, Z - d), max(0, min(Z, d, N, A - d)), max(0, N - d))


def layout(Z, N, kind):
    """Site kinds along the chain. `seg` = p^Z n^N; `alt` = pnpn... then the tail."""
    if kind == "seg":
        return ["p"]*Z + ["n"]*N
    m = min(Z, N)
    return ["p", "n"]*m + ["p"]*(Z - m) + ["n"]*(N - m)


def census(kinds):
    """`{d: (pp, pn, nn)}` for a site list. Integer arithmetic only, so cheap."""
    A = len(kinds)
    out = {}
    for d in range(1, A):
        pp = pn = nn = 0
        for i in range(A - d):
            x, y = kinds[i], kinds[i + d]
            if x == "p" and y == "p":
                pp += 1
            elif x == "n" and y == "n":
                nn += 1
            else:
                pn += 1
        out[d] = (pp, pn, nn)
    return out


def s_from_census(cen, full):
    """Weight a census: `full` uses `L.b^(d-1)`, otherwise only `d = 1`."""
    tot = mp.mpf(0)
    for d, (pp, pn, nn) in cen.items():
        if not full and d != 1:
            continue
        if pp:
            tot += pp*L_PP*(B_PP**(d - 1) if full else 1)
        if pn:
            tot += pn*L_PN*(B_PN**(d - 1) if full else 1)
        if nn:
            tot += nn*L_NN*(B_NN**(d - 1) if full else 1)
    return tot


def s_contact(Z, N):
    """The corpus law: only d = 1."""
    p, m, n = closed_counts(Z, N, 1)
    return p*L_PP + m*L_PN + n*L_NN


def s_full(Z, N):
    """Option (a): every pair, weight L . b^(d-1) at that letter's own rate."""
    A = Z + N
    tot = mp.mpf(0)
    for d in range(1, A):
        p, m, n = closed_counts(Z, N, d)
        if p:
            tot += p*L_PP*B_PP**(d - 1)
        if m:
            tot += m*L_PN*B_PN**(d - 1)
        if n:
            tot += n*L_NN*B_NN**(d - 1)
    return tot


def _pct(v, n, d=100):
    s = sorted(v)
    return s[min(len(s) - 1, len(s)*n//d)]


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    ok = True
    print("=" * 78)
    print("0. CONTROL — the closed-form pair counts against a brute-force census")
    print("=" * 78)
    bad = []
    for Z in range(1, 8):
        for N in range(1, 8):
            bf = brute_counts(Z, N)
            for d in range(1, Z + N):
                cf = closed_counts(Z, N, d)
                got = (bf["pp"].get(d, 0), bf["pn"].get(d, 0), bf["nn"].get(d, 0))
                if cf != got:
                    bad.append((Z, N, d, cf, got))
    print(f"    checked 49 (Z,N) layouts, every distance: {len(bad)} mismatches")
    ok &= chk("closed_form_pair_counts_match_brute_force", bad, [],
              note="min(Z,d,N,A-d) for the p-n census is the step that could "
                   "quietly be wrong; this is the control that says it is not")

    meas = []
    for e in json.loads(AME.read_text())["entries"]:
        Z, N, A = e["Z"], e["N"], e["A"]
        b = e.get("binding_energy_per_A_keV")
        if Z < 1 or N < 1 or not b or e.get("binding_energy_per_A_estimated"):
            continue
        B = mp.mpf(str(b))*A/1000
        if B > 0:
            meas.append((A, Z, N, B))

    print()
    print("=" * 78)
    print("1. THE SCALE — full range over-binds, exactly as predicted")
    print("=" * 78)
    print(f"    {'letter':>8}{'b':>14}{'1/(1-b)':>12}")
    for nm, bb in (("pp", B_PP), ("pn", B_PN), ("nn", B_NN)):
        print(f"    {nm:>8}{mp.nstr(bb, 10):>14}{mp.nstr(1/(1 - bb), 8):>12}")

    rc = [B/s_contact(Z, N) for (A, Z, N, B) in meas]
    rf = [B/s_full(Z, N) for (A, Z, N, B) in meas]
    med_c, med_f = _pct(rc, 50), _pct(rf, 50)
    print()
    print(f"    median B_AME / S   contact {mp.nstr(med_c, 10)}"
          f"   full range {mp.nstr(med_f, 10)}")
    print(f"    ratio of medians                        {mp.nstr(med_c/med_f, 8)}x")
    ok &= chk("full_range_over_binds_relative_to_contact",
              bool(med_f < med_c), True,
              note=f"the implied scale moves by {mp.nstr(med_c/med_f, 6)}x. The "
                   "contact chain already over-binds at 0.886, so this was the "
                   "expected direction and is NOT the test -- see section 2")

    print()
    print("=" * 78)
    print("2. THE TEST — is the SHAPE better? (scale-free spreads of B_AME/S)")
    print("=" * 78)
    ra_c, ra_f, r_free = [], [], []
    for (A, Z, N, B) in meas:
        cen = census(layout(Z, N, "alt"))
        ra_c.append(B/s_from_census(cen, False))
        ra_f.append(B/s_from_census(cen, True))
        r_free.append(B/mp.mpf(A - 1))

    print(f"    {'law':>30}{'p25-p75':>12}{'p5-p95':>12}{'full':>12}")
    stats = {}
    rows = (("segregated chain, contact", rc),
            ("segregated chain, FULL RANGE", rf),
            ("alternating chain, contact", ra_c),
            ("alternating chain, FULL RANGE", ra_f),
            ("layout-free (A-1)", r_free))
    for nm, rr in rows:
        st = {"p25_p75": _pct(rr, 75)/_pct(rr, 25),
              "p5_p95": _pct(rr, 95)/_pct(rr, 5),
              "full": max(rr)/min(rr)}
        stats[nm] = {k: mp.nstr(v, 10) for k, v in st.items()}
        print(f"    {nm:>30}{mp.nstr(st['p25_p75'], 6):>12}"
              f"{mp.nstr(st['p5_p95'], 6):>12}{mp.nstr(st['full'], 6):>12}")

    c = stats["segregated chain, contact"]
    f = stats["segregated chain, FULL RANGE"]
    free = stats["layout-free (A-1)"]
    ok &= chk("full_range_moves_p5_p95_down_but_the_full_spread_UP",
              bool(mp.mpf(f["p5_p95"]) < mp.mpf(c["p5_p95"])
                   and mp.mpf(f["full"]) > mp.mpf(c["full"])), True,
              note=f"p5-p95 {c['p5_p95']} -> {f['p5_p95']} "
                   f"({mp.nstr((1 - mp.mpf(f['p5_p95'])/mp.mpf(c['p5_p95']))*100, 4)} % "
                   f"better) but full {c['full']} -> {f['full']} "
                   f"({mp.nstr((mp.mpf(f['full'])/mp.mpf(c['full']) - 1)*100, 4)} % "
                   "worse). One measure improving marginally while the widest "
                   "worsens is redistribution, not repair")
    ok &= chk("and_layout_free_bond_counting_still_beats_both",
              bool(mp.mpf(free["p5_p95"]) < mp.mpf(f["p5_p95"])
                   and mp.mpf(free["full"]) < mp.mpf(f["full"])), True,
              note=f"layout-free (A-1) scores p5-p95 {free['p5_p95']}, full "
                   f"{free['full']} -- better than full range on BOTH. Restoring "
                   "the range does not recover what the isospin-resolved letters "
                   "cost in the first place (qou-q7ga)")

    print()
    print()
    print("=" * 78)
    print("2b. WHICH END MOVES — normalised median ratio by mass bin")
    print("=" * 78)
    print(f"    {'A range':>12}{'n':>6}{'contact':>14}{'full range':>14}{'shift':>10}")
    bins = ((2, 20), (21, 60), (61, 120), (121, 180), (181, 300))
    binrows = []
    for lo, hi in bins:
        idx = [i for i, (A, _Z, _N, _B) in enumerate(meas) if lo <= A <= hi]
        if not idx:
            continue
        mc = _pct([rc[i] for i in idx], 50)/med_c
        mf = _pct([rf[i] for i in idx], 50)/med_f
        binrows.append({"A_range": f"{lo}-{hi}", "n": len(idx),
                        "contact_norm": mp.nstr(mc, 8), "full_norm": mp.nstr(mf, 8),
                        "shift_pct": mp.nstr((mf/mc - 1)*100, 6)})
        print(f"    {f'{lo}-{hi}':>12}{len(idx):>6}{mp.nstr(mc, 8):>14}"
              f"{mp.nstr(mf, 8):>14}{mp.nstr((mf/mc - 1)*100, 4) + ' %':>10}")
    light = mp.mpf(binrows[0]["shift_pct"])
    heavy = mp.mpf(binrows[-1]["shift_pct"])
    ok &= chk("the_range_extension_moves_the_LIGHT_end_not_the_heavy_one",
              bool(abs(light) > abs(heavy)), True,
              note=f"scale-normalised median shifts {binrows[0]['shift_pct']} % "
                   f"in A=2-20 against {binrows[-1]['shift_pct']} % in the "
                   "heaviest bin. Light nuclei have few pairs, so extending the "
                   "range changes them most in relative terms -- and they are "
                   "where the tails of the distribution live")

    gap_contact = (mp.mpf(stats["alternating chain, contact"]["p5_p95"])
                   / mp.mpf(c["p5_p95"]) - 1)*100
    gap_full = (mp.mpf(stats["alternating chain, FULL RANGE"]["p5_p95"])
                / mp.mpf(f["p5_p95"]) - 1)*100
    print()
    print("    Layout washout: the segregated/alternating gap in p5-p95 is")
    print(f"    {mp.nstr(gap_contact, 4)} % at contact and "
          f"{mp.nstr(gap_full, 4)} % at full range -- restoring the range")
    print("    makes the LAYOUT nearly irrelevant, which is qou-48is's")
    print("    conclusion arriving from a second direction.")
    ok &= chk("full_range_washes_out_the_layout_difference",
              bool(abs(gap_full) < abs(gap_contact)/5), True,
              note=f"segregated-vs-alternating p5-p95 gap {mp.nstr(gap_contact, 4)} % "
                   f"at contact, {mp.nstr(gap_full, 4)} % at full range. Once "
                   "every pair contributes, the ORDER of the nucleons stops "
                   "mattering -- an independent route to qou-48is's finding")

    print()
    print("=" * 78)
    print("3. VERDICT — the self-inconsistency is real; repairing it is not the fix")
    print("=" * 78)
    print("  NOT ADOPTED, but it is not nothing either. Three findings:")
    print()
    print("  1. It FIXES THE LIGHT END, which is where the contact law is worst.")
    print(f"     A = 2-20 normalised median {binrows[0]['contact_norm']} -> "
          f"{binrows[0]['full_norm']} ({binrows[0]['shift_pct']} %), against")
    print("     -0.26 % to -0.97 % everywhere else. Light nuclei have few bonds,")
    print("     so a contact law under-counts them most and the missing pairs")
    print("     are exactly what the range restores.")
    print()
    print("  2. It WASHES OUT THE LAYOUT. The segregated-vs-alternating p5-p95")
    print(f"     gap goes {mp.nstr(gap_contact, 4)} % -> {mp.nstr(gap_full, 4)} %, "
          "15x smaller. Once every pair")
    print("     contributes, the ORDER of the nucleons stops mattering -- an")
    print("     independent route to qou-48is.")
    print()
    print("  3. But it does NOT repair the law. p5-p95 improves only")
    print(f"     {c['p5_p95']} -> {f['p5_p95']} (~1.4 %) while the FULL spread")
    print(f"     worsens {c['full']} -> {f['full']}, and layout-free (A-1) still")
    print(f"     beats it on both ({free['p5_p95']}, {free['full']}) with no")
    print("     isospin structure at all.")
    print()
    print("  So the 14.4x truncation self-inconsistency is real and worth")
    print("  recording, but the truncation is NOT what the residual is made of.")
    print("  By this probe's own falsifier that indicts the LETTERS or the")
    print("  identification mu = -ln b -- and it is consistent with qou-q7ga:")
    print("  the isospin-resolved letters cost more than any range treatment")
    print("  recovers.")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-full-range-bond-sum",
        "q0Anchor": "proton",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": mp.nstr(Q0, 30), "dps": DPS,
                       "L_pp": mp.nstr(L_PP, 16), "L_pn": mp.nstr(L_PN, 16),
                       "L_nn": mp.nstr(L_NN, 16),
                       "weight": "L_type . b_type^(d-1)",
                       "identification": "mu = -ln b -- a MODELLING CHOICE, not "
                                         "derived; the same b that suppresses "
                                         "the trace per bond is taken to set the "
                                         "range",
                       "layout": "segregated chain p^Z n^N"},
        "data": {"n_measured": len(meas),
                 "median_ratio_contact": mp.nstr(med_c, 12),
                 "median_ratio_full_range": mp.nstr(med_f, 12),
                 "scale_shift": mp.nstr(med_c/med_f, 10),
                 "spreads": stats,
                 "by_mass_bin": binrows,
                 "layout_gap_pct_contact": mp.nstr(gap_contact, 8),
                 "layout_gap_pct_full_range": mp.nstr(gap_full, 8)},
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_full_range_bond_sum_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-full-range-bond-sum.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
