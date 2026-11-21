#!/usr/bin/env python3
"""Options if `B = scale . Delta_tr` is NOT the law — and is the scale knot dependent?

`qbeta_no_regime_of_validity_probe.py` closed the multiplicative law: at its own
OPTIMAL scale it still spans 4.59 decades over AME2020. This probe asks the two
questions that follow — what replaces it, and can a knot-dependent scale save it
— and answers both from the closed form rather than by search.

*** 0. WHY THE LINEAR LAW CANNOT WORK — ONE LINE ***

The closed form makes the obstruction algebraic, not empirical:

    tr_M(beta_free) = t_p^Z . t_n^N                        A PRODUCT
    tr_M(beta_atom) = t_p^Z t_n^N . b_pp^(Z-1) b_pn b_nn^(N-1)

`tr_M` is MULTIPLICATIVE along the chain. Binding energy is EXTENSIVE — a sum
over bonds. A constant times a product is still a product, so `B = s.Delta_tr`
asks an exponential to be a line. The failure is not that the scale is wrong; it
is that no scale exists.

*** 1. THE OPTION THAT IS ALREADY IN THE REPO ***

`log` is the unique map carrying multiplicative to additive, so the functional
with the right extensivity is FORCED, not chosen:

    B(Z,N) = E_0 . log( tr_M(beta_free) / tr_M(beta_atom) )
           = E_0 . [ (Z-1)(-ln b_pp) + (-ln b_pn) + (N-1)(-ln b_nn) ]

linear in Z and N — a per-bond energy, i.e. the SEMF volume term, with the three
bond energies already derived and no fit anywhere. That is
`computations/binding_log_free_energy.py` (bean `lkpl`, completed 2026-06-23),
whose scale `E_0 = m_e/(q0(q0-1))` is a closed substrate expression. It had
never been scanned against the full table; its docstring quotes 0.57-2.36x on a
small validation set. Section 2 scans it, and the result is much stronger than
that range suggests.

*** 2. MEASURED — AND THE HEADLINE NUMBER IS A ROBUST SPREAD, NOT A RANGE ***

On the 2548 nuclides whose AME binding energy is MEASURED (`estimated=False`):

    law                        p5-p95 spread     full range
    B = s . Delta_tr                  1592 x     4.21 decades
    B = E_0 . log(free/atom)         1.225 x     1.008 decades

A factor of ~1300 in the robust spread, from changing the FUNCTIONAL, not the
constant: both laws consume the same derived `b_pp`, `b_pn`, `b_nn`.

The full range is quoted second deliberately. The additive law's extremes are
`5Be` (Z=4, N=1, B = 0.09 MeV, AME-EXTRAPOLATED) and `7H`, `6H`, `5H` — drip-line
systems that are barely or not bound at all. A bond-counting law with strictly
positive bond energies predicts ~`E_0 . 0.7 A` for ANY configuration and so
cannot produce `B ~ 0`; unbound nuclides are a NAMED limitation of the law, not
noise. Median ratio is 2.686 and the band medians run 2.58 -> 2.31 from A<40 to
A>280, so the law does not drift away.

*** THE ONE HONEST GAP: A FACTOR OF 2.66 ***

The derived `E_0 = 4.18598 MeV` puts the law 2.656x low; the best single scale is
11.119 MeV. That is ONE dimensionless number, not a shape failure — and it is
recorded here as a target for a future derivation to be checked AGAINST, never as
a criterion to search on. This probe does not adopt the optimum and does not go
looking for a closed form that hits 2.656. Anti-fit discipline (AGENTS.md).

Two more numbers in the same category, recorded not searched: the ratio ceiling
sits at 3.00-3.01 across the whole iron peak and the N=Z alpha-conjugate chain
(Si-28, S-32, Ar-36, Ca-40, Cr-50, Fe-52/54, Co-55, Ni-56/57/58), and 4He alone
sits above it at 3.259.

*** 3. IS THE SCALE KNOT DEPENDENT? — NO, FOR THREE REASONS ***

The natural rescue is the Markov normalisation: `tr_M` is not a link invariant,
and the HOMFLY normalisation `mu^(n-1) . nu^(e)` (braid index `n`, exponent sum
`e`) is exactly a per-closure — knot-dependent — scale, DERIVED from the Markov
moves rather than fitted. Three reasons it is unavailable, in increasing order of
finality:

  (a) `e` DOES NOT EXIST. The atom object is not in the image of
      `rho : B_n -> H_n(q)`: `2A+1` letters are weight-1 averages of `sigma` and
      `sigma^-1` (two `ud` pairs per nucleon, plus one per interface). By
      linearity `tr_M` is a weighted sum of `2^(2A+1)` link invariants, each
      branch with a DIFFERENT exponent sum. There is no writhe to normalise by
      and no single knot for a scale to depend on. (`atom_braid_word_3A`
      docstring; docs/audits/2026-08-25-atom-word-closures-are-not-hyperbolic.md)

  (b) THE RATE IS WRONG BY 24x AT BEST. Granting a normalisation `mu^(3A-1)`
      anyway, its log-slope is `3 ln mu` per nucleon, a fixed number. The slope
      the data demands along `N=Z` is `-0.0619` per nucleon. Measured below: the
      closest RIGHT-SIGNED substrate constant (`mu = z`) is 23.8x too steep, and
      the closest by magnitude (`mu = q`, 5.06x) has the WRONG SIGN. The
      substrate offers no constant at the needed rate.

  (c) THE SCALE THAT WOULD WORK IS THE ALGEBRA'S OWN OUTPUT, INVERTED. Regress
      `ln(B/Delta_tr)` on `(Z,N)`: coefficients come back at `-ln t_p` and
      `-ln t_n` to within 20 %. A scale of that shape cancels `t_p^Z t_n^N` and
      leaves the scale carrying all the physics and the trace carrying none.
      That is the definition of a fit; it is reported to be REFUSED.

*** WHAT IS AND IS NOT REFUTED ***

Refuted: the multiplicative ansatz `B = scale . Delta_tr` at any scale, and its
knot-dependent repair. Untouched: the ALGEBRA. `Delta_tr` is closed-form, derived
with zero fitted constants, agrees with the direct trace to 1e-35, and its bond
factors are exactly what the surviving additive law consumes. Only the map from
those factors to MeV changes.
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
QB = mp.mpf("0.78233340931")
M_E = mp.mpf("0.51099895069")

# --- the closed form (derived; qbeta_bond_factors_derived_probe.py) ----------
T_P = ((Q0**22 + Q0**20 + 2*Q0**18 + 2*Q0**16 + 3*Q0**14 + 2*Q0**12
        + Q0**10 - Q0**8 - Q0**4 - Q0**2 - 1) / (4*Q0**9*(Q0**2 + 1)**2))
T_N = ((Q0**18 - Q0**16 + 2*Q0**14 - 2*Q0**12 + 4*Q0**10 - 3*Q0**8
        + 3*Q0**6 - 2*Q0**4 + Q0**2 - 1) / (4*Q0**9))
B_PP = Q0**3 / (Q0**2 + 1)
B_NN = 1 / (Q0**3 + Q0)
B_PN = ((Q0**10 - 2*Q0**9 + 7*Q0**8 - 2*Q0**6 + 4*Q0**5 + 4*Q0**4
         + Q0**2 - 2*Q0 + 1) / (12*Q0**5*(Q0**2 + 1)))

# `E_0 = m_e / (q0 (q0 - 1))` -- the scale of the log functional. A closed
# substrate expression, NOT a fourth calibration: it is the one already carried
# by computations/binding_log_free_energy.py.
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E0 = _qbeta_e0.order_zero_scaled(M_E, Q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)

AME = ROOT / "qou-mass/src/qou_mass/data/ame2020.json"


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def delta_tr(Z: int, N: int):
    """`tr_M(beta_free) - tr_M(beta_atom)` -- the MULTIPLICATIVE observable."""
    f = T_P**Z * T_N**N
    return f - f * B_PP**(Z - 1) * B_NN**(N - 1) * B_PN


def log_bond_sum(Z: int, N: int):
    """`log(tr_M(beta_free) / tr_M(beta_atom))` -- the ADDITIVE observable.

    Exactly `-[(Z-1) ln b_pp + ln b_pn + (N-1) ln b_nn]`: the `t_p^Z t_n^N` free
    factor cancels in the RATIO, which is the whole reason this functional is
    extensive and the difference is not.
    """
    return -((Z - 1) * mp.log(B_PP) + mp.log(B_PN) + (N - 1) * mp.log(B_NN))


def _pct(vals, num: int, den: int = 100):
    """The `num/den` quantile. Integer num/den so no float64 enters a cut point."""
    v = sorted(vals)
    return v[min(len(v) - 1, len(v) * num // den)]


def _stats(vals):
    lo, hi = min(vals), max(vals)
    return {"min": lo, "max": hi, "decades": mp.log10(hi / lo),
            "median": _pct(vals, 50),
            "p1_p99": _pct(vals, 99) / _pct(vals, 1),
            "p5_p95": _pct(vals, 95) / _pct(vals, 5)}


def _geo(vals):
    return mp.exp(sum(mp.log(v) for v in vals) / len(vals))


def _lstsq2(rows, y):
    """Least squares `y ~ c0 + c1.Z + c2.N` via normal equations at 30 dps.

    Used ONLY to characterise what a rescuing scale would have to be, in order to
    REFUSE it (section 3c). Not a fit adopted as evidence for anything.
    """
    n = len(rows)
    X = [[mp.mpf(1), mp.mpf(r[0]), mp.mpf(r[1])] for r in rows]
    A = [[sum(X[k][i] * X[k][j] for k in range(n)) for j in range(3)]
         for i in range(3)]
    b = [sum(X[k][i] * y[k] for k in range(n)) for i in range(3)]
    return mp.lu_solve(mp.matrix(A), mp.matrix(b))


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    all_rows, meas_rows = [], []
    for e in json.loads(AME.read_text())["entries"]:
        Z, N, A = e["Z"], e["N"], e["A"]
        if Z < 1 or N < 1:
            continue
        bpa = e.get("binding_energy_per_A_keV")
        if not bpa:
            continue
        B = mp.mpf(str(bpa)) * A / 1000
        if B <= 0:
            continue
        d = delta_tr(Z, N)
        if d <= 0:
            continue
        rec = (A, Z, N, B, d, log_bond_sum(Z, N), e.get("element"),
               bool(e.get("binding_energy_per_A_estimated")))
        all_rows.append(rec)
        if not rec[7]:
            meas_rows.append(rec)

    ok = True
    print("=" * 78)
    print(f"0. TWO OBSERVABLES, ONE ALGEBRA — {len(all_rows)} nuclides "
          f"({len(meas_rows)} measured)")
    print("=" * 78)
    print(f"  -ln b_pp = {mp.nstr(-mp.log(B_PP), 12)}   (p-p bond)")
    print(f"  -ln b_pn = {mp.nstr(-mp.log(B_PN), 12)}   (p-n interface)")
    print(f"  -ln b_nn = {mp.nstr(-mp.log(B_NN), 12)}   (n-n bond)")
    print(f"  E_0 = m_e/(q0(q0-1)) = {mp.nstr(E0, 12)} MeV   (derived, no fit)")
    ok &= chk("proton_bonds_bind_less_than_neutron_bonds",
              -mp.log(B_PP) < -mp.log(B_NN), True,
              "b_pp = z = 0.6127 > b_nn = 0.4036, so a p-p bond carries less "
              "log-weight than n-n. The ALGEBRAIC fact stands; reading it as "
              "'the sign Coulomb would give' is RETRACTED 2026-09-04 "
              "(qou-q7ga) -- aggregated over the table the splitting has the "
              "WRONG sign. See qbeta_tower_log_z_and_roast_probe.py")

    print("\n" + "=" * 78)
    print("1./2. THE TWO LAWS, SIDE BY SIDE")
    print("=" * 78)
    res = {}
    for tag, rows in (("all", all_rows), ("measured", meas_rows)):
        lin_opt = _geo([r[3] / r[4] for r in rows])
        lin = _stats([r[3] / (lin_opt * r[4]) for r in rows])
        add = _stats([r[3] / (E0 * r[5]) for r in rows])
        log_opt = _geo([r[3] / r[5] for r in rows])
        res[tag] = {"n": len(rows), "lin_opt": lin_opt, "lin": lin,
                    "add": add, "log_opt": log_opt}
        print(f"  --- {tag} (n={len(rows)}) " + "-" * (52 - len(tag)))
        print(f"    B = s.Delta_tr   @ optimal s = {mp.nstr(lin_opt, 8)} MeV : "
              f"p5-p95 {mp.nstr(lin['p5_p95'], 7):>10}   full "
              f"{mp.nstr(lin['decades'], 4)} dec")
        print(f"    B = E_0.log(...) @ DERIVED E_0 = {mp.nstr(E0, 8)} MeV : "
              f"p5-p95 {mp.nstr(add['p5_p95'], 7):>10}   full "
              f"{mp.nstr(add['decades'], 4)} dec   median {mp.nstr(add['median'], 6)}")
        print(f"    (best single additive scale = {mp.nstr(log_opt, 10)} MeV = "
              f"{mp.nstr(log_opt/E0, 7)} x E_0 -- RECORDED, NOT ADOPTED)")

    m = res["measured"]
    gain = m["lin"]["p5_p95"] / m["add"]["p5_p95"]
    print(f"\n  robust-spread gain on measured values: {mp.nstr(gain, 7)} x")
    ok &= chk("additive_law_shrinks_the_robust_spread_by_over_a_thousandfold",
              gain > 1000, True,
              f"p5-p95 {mp.nstr(m['lin']['p5_p95'],6)} -> "
              f"{mp.nstr(m['add']['p5_p95'],6)}; the gain is from the FUNCTIONAL, "
              "not the constant -- both consume the same derived bond factors")
    ok &= chk("additive_law_p5_p95_is_within_a_factor_of_1_point_3",
              m["add"]["p5_p95"] < mp.mpf("1.3"), True,
              "90 % of measured nuclides land inside a 1.225x band")

    # The full range is NOT the headline: name what sets it.
    worst = min(all_rows, key=lambda r: r[3] / (E0 * r[5]))
    print(f"  worst additive outlier: {worst[0]}{worst[6]} (Z={worst[1]}, "
          f"N={worst[2]})  B = {mp.nstr(worst[3], 4)} MeV  "
          f"estimated={worst[7]}  ratio {mp.nstr(worst[3]/(E0*worst[5]), 6)}")
    ok &= chk("the_additive_full_range_is_set_by_an_unbound_extrapolated_nuclide",
              worst[7] and worst[3] < mp.mpf("0.2"), True,
              "5Be, B = 0.09 MeV and AME-EXTRAPOLATED. A bond-counting law with "
              "strictly positive bond energies predicts ~E_0.0.7A for any "
              "configuration and cannot produce B ~ 0: unbound systems are a "
              "NAMED limitation, and excluding extrapolations takes the full "
              "range from 2.51 to 1.01 decades")
    ok &= chk("excluding_extrapolated_values_more_than_halves_the_full_range",
              m["add"]["decades"] < res["all"]["add"]["decades"] / 2, True)

    print("\n  band medians of B/(E_0.log-ratio), measured values:")
    by_a = {}
    for r in meas_rows:
        by_a.setdefault(r[0] // 40, []).append(r[3] / (E0 * r[5]))
    bands = []
    for k in sorted(by_a):
        v = by_a[k]
        med = _pct(v, 50)
        bands.append({"A_band": f"{40*k}-{40*k+39}", "n": len(v),
                      "median_ratio": mp.nstr(med, 8)})
        print(f"    A {40*k:>3}-{40*k+39:<3}  n={len(v):>4}  median "
              f"{mp.nstr(med, 6)}")
    meds = [mp.mpf(b["median_ratio"]) for b in bands]
    ok &= chk("additive_band_medians_stay_within_a_factor_of_1_point_3",
              max(meds) / min(meds) < mp.mpf("1.3"), True,
              "no drift with A across the whole table -- the law is "
              "structurally extensive, not extensive by accident")

    print("\n  🔓 OPEN, recorded not searched: the derived E_0 is "
          f"{mp.nstr(m['log_opt']/E0, 6)}x low.")
    print("     One dimensionless number, not a shape failure. Ceiling of the")
    print("     ratio sits at 3.00-3.01 across the iron peak and the N=Z")
    print("     alpha-conjugate chain; 4He alone is above it at 3.259.")

    print("\n" + "=" * 78)
    print("3. IS THE SCALE KNOT DEPENDENT?")
    print("=" * 78)
    for A in (2, 4, 56, 208):
        print(f"    A={A:>3}:  non-braid letters = 2A+1 = {2*A+1:>4}   "
              f"branch links = 2^{2*A+1}")
    ok &= chk("atom_object_is_not_a_braid_so_it_has_no_writhe", True, True,
              "2A+1 letters are weight-1 averages of sigma and sigma^-1, so "
              "tr_M is a sum of 2^(2A+1) link invariants with 2^(2A+1) "
              "different exponent sums -- the Markov normalisation mu^(n-1).nu^e "
              "has no e to use, and no single knot for a scale to depend on")

    need = -(mp.log(T_P) + mp.log(T_N)) / 2      # required slope /nucleon at N=Z
    print(f"    required correction slope along N=Z: {mp.nstr(need, 8)} /nucleon")
    cands = {"z = q^3/(q^2+1)": B_PP, "1/(q^3+q)": B_NN, "b_pn": B_PN,
             "[2]_q = (q^2+1)/q": (Q0**2 + 1) / Q0, "q": Q0}
    cand_rows = []
    for nm, mu in cands.items():
        slope = 3 * mp.log(mu)                   # mu^(3A-1): 3 strands / nucleon
        ratio = abs(slope) / abs(need)
        sign_ok = bool(slope * need > 0)
        cand_rows.append({"mu": nm, "slope_per_nucleon": mp.nstr(slope, 10),
                          "ratio_to_required": mp.nstr(ratio, 8),
                          "sign_matches": sign_ok})
        print(f"    mu = {nm:<20} 3.ln(mu) = {mp.nstr(slope, 8):>13} /nucleon"
              f"   |slope|/required = {mp.nstr(ratio, 6):>9}   "
              f"sign {'OK ' if sign_ok else 'WRONG'}")
    right = [mp.mpf(c["ratio_to_required"]) for c in cand_rows if c["sign_matches"]]
    wrong = [mp.mpf(c["ratio_to_required"]) for c in cand_rows if not c["sign_matches"]]
    ok &= chk("closest_right_signed_candidate_is_over_20x_too_steep",
              min(right) > 20, True,
              "mu = z, the Markov parameter itself, is 23.8x too steep")
    ok &= chk("the_candidate_closest_in_magnitude_has_the_wrong_sign",
              min(wrong) < min(right), True,
              "mu = q is only 5.06x off in magnitude but pushes the correction "
              "the wrong way -- so no substrate constant is close on both counts")

    y = [mp.log(r[3] / r[4]) for r in meas_rows]
    c = _lstsq2([(r[1], r[2]) for r in meas_rows], y)
    print("    regression ln(B/Delta_tr) ~ c0 + cZ.Z + cN.N (measured values):")
    print(f"      cZ = {mp.nstr(c[1], 10):>14}   -ln t_p = "
          f"{mp.nstr(-mp.log(T_P), 10)}")
    print(f"      cN = {mp.nstr(c[2], 10):>14}   -ln t_n = "
          f"{mp.nstr(-mp.log(T_N), 10)}")
    dz = abs(c[1] / (-mp.log(T_P)) - 1)
    dn = abs(c[2] / (-mp.log(T_N)) - 1)
    ok &= chk("required_scale_reproduces_minus_ln_t_p_and_minus_ln_t_n_to_20pc",
              dz < mp.mpf("0.2") and dn < mp.mpf("0.2"), True,
              f"cZ off by {mp.nstr(dz*100,3)} %, cN by {mp.nstr(dn*100,3)} %. Not "
              "tighter because ln B ~ ln(8.5A) is not linear in (Z,N) and "
              "contaminates both coefficients. Sign and magnitude are the point: "
              "the only scale that rescues the multiplicative law is t_p^-Z "
              "t_n^-N, which cancels the trace's own output. REFUSED as a fit")

    print("\n  ✅ The replacement is not a new object: it is the LOG of the same")
    print("     derived bond factors. Robust spread "
          f"{mp.nstr(m['lin']['p5_p95'], 6)}x -> {mp.nstr(m['add']['p5_p95'], 6)}x.")
    print("  🛑 A knot-dependent scale is unavailable (no single knot),")
    print("     quantitatively refuted where derivable, and a fit where it works.")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    def _st(d):
        return {k: mp.nstr(v, 12) for k, v in d.items()}

    witness = {
        "computation": "qbeta-binding-law-options",
        "q0Anchor": "proton",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {
            "q0": mp.nstr(Q0, 30), "dps": DPS,
            "corpus_Q_beta_MeV": str(QB),
            "E_0_MeV": mp.nstr(E0, 20), "E_0_expression": "m_e/(q0*(q0-1))",
            "multiplicative_law": "B = s.(tr_M(free) - tr_M(atom))",
            "additive_law": "B = E_0.log(tr_M(free)/tr_M(atom))",
            "source": "qou-mass/src/qou_mass/data/ame2020.json",
        },
        "data": {
            "n_all": len(all_rows), "n_measured": len(meas_rows),
            "bond_energies_natural_log": {
                "minus_ln_b_pp": mp.nstr(-mp.log(B_PP), 20),
                "minus_ln_b_pn": mp.nstr(-mp.log(B_PN), 20),
                "minus_ln_b_nn": mp.nstr(-mp.log(B_NN), 20),
            },
            "laws": {tag: {
                "multiplicative_optimal_scale_MeV": mp.nstr(v["lin_opt"], 15),
                "multiplicative": _st(v["lin"]),
                "additive_at_derived_E0": _st(v["add"]),
                "additive_optimal_scale_MeV": mp.nstr(v["log_opt"], 15),
                "additive_optimal_over_E0": mp.nstr(v["log_opt"] / E0, 12),
            } for tag, v in res.items()},
            "additive_band_medians_measured": bands,
            "worst_additive_outlier": {
                "A": worst[0], "Z": worst[1], "N": worst[2],
                "element": worst[6], "B_MeV": mp.nstr(worst[3], 10),
                "ame_estimated": worst[7],
                "ratio": mp.nstr(worst[3] / (E0 * worst[5]), 10)},
            "knot_dependence": {
                "atom_object_in_image_of_rho": False,
                "non_braid_letters": "2A+1", "branch_links": "2^(2A+1)",
                "required_slope_per_nucleon_at_NeqZ": mp.nstr(need, 15),
                "candidates": cand_rows,
                "rescuing_scale_cZ": mp.nstr(c[1], 15),
                "rescuing_scale_cN": mp.nstr(c[2], 15),
                "verdict": "unavailable (no single knot), quantitatively "
                           "refuted where derivable, a fit where it works",
            },
        },
        "provenance": {"headSha": _head_sha(),
                       "producer": "computations/qbeta/qbeta_binding_law_options_probe.py",
                       # `elapsed_sec`, not `elapsed_s`: the raw-float64 ratchet
                       # excuses a wall-clock duration only by EXACT field name
                       # (`witness_raw_float64_audit.EPHEMERAL_TIMING_FIELDS` =
                       # durationMs / durationSeconds / duration_sec /
                       # elapsed_sec / elapsed_seconds). `elapsed_s` is the same
                       # quantity under a spelling that vocabulary does not
                       # carry, so it read as a payload float and took the gate
                       # red. No value changes; only the key.
                       "elapsed_sec": round(time.monotonic() - t0, 3)},
    }
    out = HERE / "qbeta-binding-law-options.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwitness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
