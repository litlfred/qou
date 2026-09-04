#!/usr/bin/env python3
"""The deciding test: does an INTERFACE-supported `w` supply the binding
shortfall at every atom with one shared constant?

*** 🛑 A TEST, NOT A SEARCH ***

Chain so far. `qou-bmz8`: the ell-1 binding ceiling bounds exactly the CENTRE of
`H_n` (for central `z`, `chi^lambda(beta.z) = c_lambda.chi^lambda(beta)`, a
reweighting), leaving the NON-central part untouched. Then
`qbeta_derived_w_overdetermined_test_probe.py`: almost all of that freedom is
INERT on `Delta_bind` — `sigma_1`, the Jucys-Murphy `L_2` and both Lagrange
projectors of `sigma_1` each rescale by an ATOM-INDEPENDENT constant, so all
four give the same spread as `w = 1` (0.83903) and none can supply an
atom-dependent shortfall.

That probe's mechanism said which `w` CAN matter: those supported where the
atoms differ. `atom_braid_word_3A` adds exactly one letter per bond, at
generator `3j` (1-based), so the INTERFACE generators are the whole of the
difference. It could not finish the test — `tr_m_word_lq` raises Case C on
interface-suffixed words at `n = 9` — and one atom is fitted by construction.

This probe finishes it, on a route with no Case C.

  * Candidates FIXED IN ADVANCE and derived, not searched: the identity control,
    the interface crossing product, its inverse, the corpus's own AVERAGED
    interface crossing `(sigma + sigma^-1)/2`, and a single interface generator
    as a product-vs-single control.
  * OVERDETERMINED across FOUR atoms with ONE constant — three degrees of
    overdetermination. A single atom would be fitted by construction.
  * EVERY candidate reported with its spread. No winner is selected.
  * A small spread is A TARGET TO CHECK A FUTURE DERIVATION AGAINST, never a
    derivation.

*** THE ROUTE, AND WHY IT AVOIDS CASE C ***

Case C is a limitation of the Markov-trace RECURSION (`tr_m_word_lq`), not of
the character route. `chi_q_atomic_all_partitions_mpfr` evaluates
`chi_lambda(prod_i (c_i sigma_{g_i} + d_i I))` for every `lambda |- n` directly
from the `(c, d, g)` letters — no expansion into `2^k` signed words, no
recursion, no Case C — and `tr_M = sum_lambda y_lambda chi^lambda`.

**Generator indices are 1-BASED here** and 0-based in `tr_m_atomic_mpfr`. Mixing
them is silent at `n >= 4` (it just evaluates a different word) and only raises
at small `n`, so the convention is asserted below rather than assumed.

*** VALIDATION FIRST ***

For each atom the reconstruction `sum_lambda y_lambda chi^lambda(beta_atom)`
must reproduce the committed `tr_M_at_q0` in `chi-<atom>-h<n>-at-q0-50dps.
witness.json`, and every `chi^lambda` must match the committed value. Measured
at the deuteron while wiring this up: worst chi error 9.6e-50, `tr_M`
reproduced to all 25 quoted digits.

*** THE QUANTITY ***

`binding_canonical.py` computes `B = Q_beta(n).(tr_M(W_free) - tr_M(W_atom))`.
The dimensionless shortfall is `R_X = B_AME(X)/Q_beta - Delta_tr_X`, and a
candidate contributes `S_X(w) = tr_M(free_X . w) - tr_M(atom_X . w)`. The test
is whether `c_X = R_X/S_X(w)` is the same at every atom.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp
import pyhecke_native as ph

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "computations"))

DPS = 50
mp.mp.dps = DPS
Q0S = "1.1099785827513808075916690956107688798744991218736"
Q0 = mp.mpf(Q0S)
H = Q0 - 1 / Q0

ATOMS = {   # Z, N, B_AME (MeV), committed chi witness
    "2H":  (1, 1, "2.224566",  "chi-deuteron-h6-at-q0-50dps.witness.json"),
    "3H":  (1, 2, "8.481798",  "chi-tritium-h9-at-q0-50dps.witness.json"),
    "3He": (2, 1, "7.718043",  "chi-helium-3-h9-at-q0-50dps.witness.json"),
    "4He": (2, 2, "28.295673", "chi-helium-4-h12-at-q0-50dps.witness.json"),
}


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def _s(x) -> str:
    return mp.nstr(mp.mpf(x), DPS)


def interface_gens(A: int) -> list[int]:
    """1-based generator index of each nucleon-nucleon interface."""
    return [3 * j for j in range(1, A)]


def candidates(A: int):
    """Fixed in advance. name -> list of (c, d, gen_1based) letters."""
    ig = interface_gens(A)
    one, zero = mp.mpf(1), mp.mpf(0)
    return {
        "w = 1 (control)":            [],
        "interface sigma product":    [(one, zero, g) for g in ig],
        "interface sigma^-1 product": [(one, -H, g) for g in ig],
        # the corpus's own averaged crossing: (sigma + sigma^-1)/2
        "interface averaged product": [(one, -H / 2, g) for g in ig],
        "first interface only":       [(one, zero, ig[0])],
    }


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    from mass_at_3A_proper import atom_braid_word_3A
    from experimental_constants import Q_NEUTRON_MEV as _QB
    QB = mp.mpf(str(_QB))

    # Memoised: the n = 12 evaluation costs minutes, and `w = 1` is otherwise
    # recomputed three times per atom (validation, shortfall, control row).
    _chi_cache: dict = {}

    def chis(n, letters, suffix):
        fac = [(_s(c), _s(d), int(g) + 1) for (c, d, g) in letters] \
              + [(_s(c), _s(d), int(g)) for (c, d, g) in suffix]
        key = (n, tuple(fac))
        hit = _chi_cache.get(key)
        if hit is not None:
            return hit
        out = ph.chi_q_atomic_all_partitions_mpfr(n, fac, Q0S, DPS)
        res = {tuple(lam): mp.mpf(cs) for (lam, cs) in out}
        _chi_cache[key] = res
        return res

    print("=" * 74)
    print("1. VALIDATION — reconstruct each committed tr_M from chi and y")
    print("=" * 74)
    prep, worst_chi = {}, mp.mpf(0)
    ok = True
    for x, (Z, N, B, wf) in ATOMS.items():
        n, A = 3 * (Z + N), Z + N
        w = json.loads((ROOT / "computations" / wf).read_text())
        y = {tuple(r["partition"]): mp.mpf(r["y_lambda"]) for r in w["by_partition"]}
        wit = {tuple(r["partition"]): mp.mpf(r["chi_lambda"]) for r in w["by_partition"]}
        la = atom_braid_word_3A(Z, N, include_inter=True, q=Q0)
        lf = atom_braid_word_3A(Z, N, include_inter=False, q=Q0)
        ca = chis(n, la, [])
        we = max(abs(ca[l] - wit[l]) for l in wit)
        worst_chi = max(worst_chi, we)
        tr_a = sum(y[l] * ca[l] for l in y)
        err = abs(tr_a - mp.mpf(w["tr_M_at_q0"]))
        print(f"  {x:<5} n={n:<3} worst|chi-committed| {mp.nstr(we,4):>10}"
              f"   |tr_M - committed| {mp.nstr(err,4):>10}")
        prep[x] = {"n": n, "A": A, "y": y, "la": la, "lf": lf,
                   "B": mp.mpf(B), "tr_a": tr_a}
        ok &= err < mp.mpf("1e-40")
    ok &= chk("reproduces_every_committed_chi", worst_chi < mp.mpf("1e-40"), True)
    ok &= chk("reproduces_every_committed_tr_M", ok, True,
              "without this the rest is noise")

    print("\n" + "=" * 74)
    print("2. THE SHORTFALL")
    print("=" * 74)
    print(f"  {'atom':<5}{'dtr_pred':>16}{'dtr_req':>16}{'shortfall R':>16}{'supplied':>11}")
    per_atom = {}
    for x, p in prep.items():
        y, n = p["y"], p["n"]
        cf = chis(n, p["lf"], [])
        tr_f = sum(y[l] * cf[l] for l in y)
        d = tr_f - p["tr_a"]
        req = p["B"] / QB
        R = req - d
        p["dtr"], p["R"] = d, R
        per_atom[x] = {"n": n, "dtr_pred": mp.nstr(d, 16),
                       "dtr_required": mp.nstr(req, 16),
                       "shortfall_R": mp.nstr(R, 16),
                       "fraction_supplied": mp.nstr(d / req, 8)}
        print(f"  {x:<5}{mp.nstr(d,12):>16}{mp.nstr(req,12):>16}"
              f"{mp.nstr(R,12):>16}{mp.nstr(d/req,6):>11}")

    print("\n" + "=" * 74)
    print("3. THE DECIDING TEST — one constant c across FOUR atoms")
    print("=" * 74)
    atoms = list(prep)
    print(f"  {'candidate w':<28}" + "".join(f"{x:>13}" for x in atoms) + f"{'spread':>10}")
    print("  " + "-" * (28 + 13 * len(atoms) + 10))
    rows = []
    for cname in candidates(2):
        cs, ratios = {}, {}
        for x in atoms:
            p = prep[x]
            suf = candidates(p["A"])[cname]
            y, n = p["y"], p["n"]
            ca = chis(n, p["la"], suf)
            cf = chis(n, p["lf"], suf)
            s = sum(y[l] * (cf[l] - ca[l]) for l in y)
            ratios[x] = mp.nstr(s / p["dtr"], 16)
            cs[x] = None if abs(s) < mp.mpf("1e-30") else p["R"] / s
        vals = [v for v in cs.values() if v is not None]
        spread = ((max(vals) - min(vals)) / abs(sum(vals) / len(vals))
                  if len(vals) == len(atoms) else None)
        rows.append({"w": cname, "ratio_to_w1": ratios,
                     "c_per_atom": {k: (mp.nstr(v, 12) if v else None)
                                    for k, v in cs.items()},
                     "spread": (mp.nstr(spread, 8) if spread is not None else None)})
        cells = "".join(f"{(mp.nstr(cs[x],8) if cs[x] else '—'):>13}" for x in atoms)
        print(f"  {cname:<28}{cells}{(mp.nstr(spread,5) if spread else '—'):>10}")

    ctrl = next(r for r in rows if r["w"].startswith("w = 1"))
    tight = [r["w"] for r in rows
             if r["spread"] is not None and mp.mpf(r["spread"]) < mp.mpf("0.05")]
    beats = [r["w"] for r in rows
             if r["spread"] is not None and r["w"] != ctrl["w"]
             and mp.mpf(r["spread"]) < mp.mpf(ctrl["spread"]) * mp.mpf("0.5")]

    print("\n" + "=" * 74)
    print("VERDICT")
    print("=" * 74)
    print(f"  control (w = 1) spread                  : {ctrl['spread']}")
    print(f"  candidates with spread < 5 %            : {tight or 'NONE'}")
    print(f"  candidates beating the control by 2x    : {beats or 'NONE'}")
    print("\n  🛑 No candidate is put forward. A small spread would be a TARGET")
    print("     TO CHECK A FUTURE DERIVATION AGAINST, never a derivation.")

    ok &= chk("interface_candidates_evaluated_at_all_four_atoms",
              all(r["spread"] is not None for r in rows), True,
              "the Case C blocker that stopped the sibling probe is gone")
    ok &= chk("every_candidate_reported_with_its_spread",
              len(rows), len(candidates(2)))
    ok &= chk("no_candidate_reaches_5pct_spread", tight, [],
              "recorded as the measured outcome, whichever way it fell")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-interface-w-deciding-test",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": Q0S, "dps": DPS, "Q_beta_n_MeV": mp.nstr(QB, 20),
                       "binding_law": "B = Q_beta(n).(tr_M(W_free) - tr_M(W_atom))",
                       "route": "chi_q_atomic_all_partitions_mpfr (1-BASED "
                                "generators; no Case C)",
                       "atoms": atoms},
        "data": {"per_atom": per_atom, "deciding_test": rows,
                 "control_spread": ctrl["spread"],
                 "candidates_under_5pct": tight,
                 "candidates_beating_control_2x": beats,
                 "worst_chi_error_vs_committed": mp.nstr(worst_chi, 6)},
        "context": {
            "axis": "does an INTERFACE-supported w supply the binding shortfall "
                    "at every atom with one shared constant?",
            "method": "Candidates fixed in advance and derived (interface "
                      "crossing, its inverse, the corpus's averaged crossing, a "
                      "single interface generator). Four atoms, one constant: "
                      "three degrees of overdetermination.",
            "anti_fit": "No candidate is put forward and every one is reported "
                        "with its spread. A small spread is a target to check a "
                        "future derivation against, never a derivation.",
            "scope": "Scope-(a). No content block is edited here.",
        },
        "gitCommit": _head_sha(),
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out_p = HERE / "qbeta-interface-w-deciding-test.witness.json"
    with open(out_p, "w") as f:
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="mpmath+pyhecke_native",
            q0_anchor="proton",
            q0_anchor_reason="experimental pin (Physical-Observations layer): q0 read at the proton m_p/m_e pin", q0_value=Q0S)
        # ensure_ascii=False: the corpus convention is UTF-8 witnesses, and
        # `witness_shape_guard` flags a witness that gains \uXXXX escapes.
        json.dump(witness, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
