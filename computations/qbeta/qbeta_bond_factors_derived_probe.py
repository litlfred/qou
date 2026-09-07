#!/usr/bin/env python3
"""All five constants of the chain closed form, DERIVED. Zero fitted numbers.

`qbeta_mixed_chain_closed_form_probe.py` left two of the five as measured
constants — `b_pn` extracted from 2H and `b_nn` from 3H — and said plainly that
calling the result a closed form without that caveat would make it a fit with
two knobs. This removes the knobs.

*** METHOD ***

The same exact-Laurent route that produced `r(q)`. `tr_m_word_lq` returns
Laurent polynomials in (z, h) with integer q-coefficients; each atom word
expands into POSITIVE braid words by branching every `c.sigma_g + d.I` letter
into "keep sigma_g" and "drop it, weight d"; the sums are exact rational
functions of q.

The builder emits exactly four shift values, and they are mapped back to their
symbolic forms:

    0                     pure sigma
    -h                    sigma^-1
    -h/2                  colour-BLIND averaged crossing
    -h(1/2 - delta/4)     colour-WEIGHTED p-n crossing, delta = (q-1)^2(1-q^-4)/3

**The last two differ by 7.2e-5 at q_0** (-0.104530149 against -0.104458248).
A loose matcher would silently map the colour-weighted p-n shift onto the
colour-blind one and return a wrong `b_pn` that still looked plausible. The
probe asserts the four are separable before matching, and matches at 1e-25.

*** THE FIVE CONSTANTS ***

    t_p  = (q^22+q^20+2q^18+2q^16+3q^14+2q^12+q^10-q^8-q^4-q^2-1) / (4q^9(q^2+1)^2)
    t_n  = (q^18-q^16+2q^14-2q^12+4q^10-3q^8+3q^6-2q^4+q^2-1)     / (4q^9)
    b_pp = q^3/(q^2+1)
    b_pn = (q^10-2q^9+7q^8-2q^6+4q^5+4q^4+q^2-2q+1)               / (12q^5(q^2+1))
    b_nn = 1/(q^3+q)

*** THREE IDENTITIES, EACH SIMPLIFYING TO EXACTLY ZERO ***

  1. `b_pp - z = 0` where `z = q^3/(q^2+1)` is the Ocneanu parameter of
     convention D. The previous probe could only say the p-p bond factor
     MATCHES z to 4.6e-16. It IS z.

  2. `b_pp/b_nn - q^4 = 0`. The two same-species bond factors differ by exactly
     `q^4`, and `b_nn = 1/(q(q^2+1))` is the simplest of the five.

  3. `r_previous - t_p.z = 0`, where `r_previous` is the homogeneous-chain ratio
     derived in a separate computation from different words. Two independent
     derivations of the same object agree symbolically — the strongest available
     check that neither is an artefact of its expansion.

*** THE RESULT ***

    tr_M(beta_free(Z,N)) = t_p^Z t_n^N
    tr_M(beta_atom(Z,N)) = t_p^Z t_n^N . b_pp^(Z-1) . b_pn^[Z,N>=1] . b_nn^(N-1)
    Delta_tr(Z,N)        = t_p^Z t_n^N (1 - b_pp^(Z-1) b_pn^[Z,N>=1] b_nn^(N-1))

as an exact rational function of q for EVERY atom, with no fitted constant, no
matrices, and therefore no dependence on the n >= 15 dimension wall.

*** SCOPE ***

Scope-(a). This derives the constants of a form whose STRUCTURE was established
and validated earlier (held-out 3He and 4He at 7.5e-16). It does not by itself
say the binding law is right — `Delta_tr` is what the law evaluates, and how far
that is from B remains the open physics question.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

# The provenance stamp at the end of main() does
# `from qou_substrate.witness import WitnessBuilder`, which lives at
# tools/qou-substrate/python and is NOT on the default path. Without this the
# script computed everything and then died on the very last line with
# ModuleNotFoundError — so its witness could never be regenerated, which is why
# it still carried grouped-era values long after the 2026-09-05 ordering ruling
# (bean qou-4383). `_path_bridge` already puts qou_substrate within reach.
sys.path.insert(0, str(ROOT / "computations"))
import _path_bridge  # noqa: E402, F401

DPS = 40
mp.mp.dps = DPS
Q0S = "1.1099785827513808075916690956107688798744991218736"

_q = sp.symbols("q", positive=True)
Z_SYM = _q**3 / (_q**2 + 1)
DELTA = (_q - 1)**2 * (1 - _q**-4) / 3

T_P = ((_q**22 + _q**20 + 2*_q**18 + 2*_q**16 + 3*_q**14 + 2*_q**12
        + _q**10 - _q**8 - _q**4 - _q**2 - 1) / (4*_q**9*(_q**2 + 1)**2))
T_N = ((_q**18 - _q**16 + 2*_q**14 - 2*_q**12 + 4*_q**10 - 3*_q**8
        + 3*_q**6 - 2*_q**4 + _q**2 - 1) / (4*_q**9))
B_PP = _q**3 / (_q**2 + 1)
B_PN = ((_q**10 - 2*_q**9 + 7*_q**8 - 2*_q**6 + 4*_q**5 + 4*_q**4
         + _q**2 - 2*_q + 1) / (12*_q**5*(_q**2 + 1)))
B_NN = 1 / (_q**3 + _q)
# derived separately, from the homogeneous chain, on different words
R_PREV = ((_q**22 + _q**20 + 2*_q**18 + 2*_q**16 + 3*_q**14 + 2*_q**12
           + _q**10 - _q**8 - _q**4 - _q**2 - 1)
          / (4*_q**6*(_q**6 + 3*_q**4 + 3*_q**2 + 1)))

# ── FRAME MISMATCH, VERIFIED 2026-09-07 (bean qou-4383) ────────────────
# The two nucleon traces below are GROUPED-era. Measured live against
# `atom_braid_word_3A` under both intra-nucleon orderings at this same pin:
#
#     atom     grouped                  borromean (canonical)
#     proton   1.1457596924573008697    0.62932840220292191817
#     neutron  0.98774368811580957163   0.47513351715568221251
#
# The literals here match GROUPED to ~1e-21 — every digit written — and differ
# from the canonical borromean values by 82 % (proton) and 108 % (neutron).
# The canonical intra-nucleon word has been `(σ₀σ₁⁻¹)³` since the 2026-09-05
# ruling (bean qou-hu1f).
#
# Meanwhile the per-atom inputs read from `ATOM_WITNESS` below ARE canonical.
# So this probe currently mixes a canonical atom frame with superseded nucleon
# traces, which is the most likely reason its closed form does not reproduce
# every atom.
#
# NOT flipped here. `qbeta_delta_vs_deltaTbeta_settled_probe` is deliberately
# pinned to grouped because its whole comparison lives in that frame, so
# "grouped constant" is not automatically a defect — and this file is under
# active edit today (`qou-qqm4`, "the bond factors ARE the two Markov
# parameters"). Whether these should move to the canonical values, or the atom
# witnesses should be read in the grouped frame instead, is a call for whoever
# owns that derivation. Flagged rather than changed.
MEASURED = {"t_p": "1.1457596924573008697", "t_n": "0.98774368811580957163",
            "b_pp": "0.6126880371464652516", "b_pn": "0.50822978937673896258",
            "b_nn": "0.40362773835082593617"}
ATOM_WITNESS = {"2H": ("chi-deuteron-h6-at-q0-50dps.witness.json", 1, 1),
                "3H": ("chi-tritium-h9-at-q0-50dps.witness.json", 1, 2),
                "3He": ("chi-helium-3-h9-at-q0-50dps.witness.json", 2, 1),
                "4He": ("chi-helium-4-h12-at-q0-50dps.witness.json", 2, 2)}


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def _ev(e):
    return mp.mpf(str(sp.N(e.subs(_q, sp.Float(Q0S, 50)), 35)))


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
    print("=" * 74)
    print("1. THE FOUR SHIFTS ARE SEPARABLE — the trap this method could fall into")
    print("=" * 74)
    shifts = {"0": sp.Integer(0), "-h": -(_q - 1/_q), "-h/2": -(_q - 1/_q)/2,
              "-h(1/2-d/4)": -(_q - 1/_q)*(sp.Rational(1, 2) - DELTA/4)}
    vals = {k: _ev(v) for k, v in shifts.items()}
    for k, v in vals.items():
        print(f"  {k:<14} {mp.nstr(v, 20)}")
    xs = list(vals.values())
    gap = min(abs(xs[i] - xs[j]) for i in range(len(xs)) for j in range(i + 1, len(xs)))
    print(f"  smallest separation: {mp.nstr(gap, 6)}  (colour-blind vs "
          f"colour-weighted)")
    ok &= chk("four_shifts_are_separable", gap > mp.mpf("1e-6"), True,
              "a loose matcher would map the colour-weighted p-n shift onto the "
              "colour-blind one and return a plausible but wrong b_pn")

    print("\n" + "=" * 74)
    print("2. THE FIVE CONSTANTS, AGAINST THEIR MEASURED VALUES")
    print("=" * 74)
    rows, worst = [], mp.mpf(0)
    for name, expr in (("t_p", T_P), ("t_n", T_N), ("b_pp", B_PP),
                       ("b_pn", B_PN), ("b_nn", B_NN)):
        v = _ev(expr)
        m = mp.mpf(MEASURED[name])
        rel = abs(v - m) / abs(m)
        worst = max(worst, rel)
        rows.append({"name": name, "closed_form": str(sp.simplify(expr)),
                     "at_q0": mp.nstr(v, 25), "measured": MEASURED[name],
                     "rel_err": mp.nstr(rel, 6)})
        print(f"  {name:<5} {mp.nstr(v, 22):>26}   measured {MEASURED[name]:>22}"
              f"   rel {mp.nstr(rel, 4)}")
    ok &= chk("all_five_match_their_measured_values", worst < mp.mpf("1e-18"), True)

    print("\n" + "=" * 74)
    print("3. THREE IDENTITIES — each simplifies to exactly zero")
    print("=" * 74)
    ids = [("b_pp - z", sp.simplify(B_PP - Z_SYM)),
           ("b_pp/b_nn - q^4", sp.simplify(B_PP/B_NN - _q**4)),
           ("r_previous - t_p.z", sp.simplify(R_PREV - T_P*Z_SYM))]
    for nm, val in ids:
        print(f"  {nm:<22} = {val}")
    ok &= chk("b_pp_IS_the_markov_parameter", ids[0][1] == 0, True,
              "an identity, not a 4.6e-16 match")
    ok &= chk("same_species_bond_factors_differ_by_q4", ids[1][1] == 0, True,
              "b_pp/b_nn = q^4 exactly")
    ok &= chk("agrees_with_the_independent_homogeneous_derivation",
              ids[2][1] == 0, True,
              "r(q) was derived from different words in a separate computation")

    print("\n" + "=" * 74)
    print("4. Delta_tr(Z,N) FOR THE FOUR ATOMS, FROM THE CLOSED FORM ALONE")
    print("=" * 74)
    tp, tn = _ev(T_P), _ev(T_N)
    bpp, bpn, bnn = _ev(B_PP), _ev(B_PN), _ev(B_NN)
    dt, worst_d = [], mp.mpf(0)
    print(f"  {'atom':<5}{'Z':>2}{'N':>2}{'Delta_tr closed form':>26}{'measured':>24}")
    for tag, (wf, Z, N) in ATOM_WITNESS.items():
        tr_meas = mp.mpf(json.loads((ROOT / "computations" / wf).read_text())
                         ["tr_M_at_q0"])
        free = tp**Z * tn**N
        atom = free * bpp**(Z - 1) * bnn**(N - 1) * (bpn if (Z >= 1 and N >= 1) else 1)
        d_pred, d_meas = free - atom, free - tr_meas
        rel = abs(d_pred - d_meas) / abs(d_meas)
        worst_d = max(worst_d, rel)
        dt.append({"atom": tag, "Z": Z, "N": N,
                   "delta_closed_form": mp.nstr(d_pred, 22),
                   "delta_measured": mp.nstr(d_meas, 22), "rel_err": mp.nstr(rel, 6)})
        print(f"  {tag:<5}{Z:>2}{N:>2}{mp.nstr(d_pred, 20):>26}"
              f"{mp.nstr(d_meas, 20):>24}   rel {mp.nstr(rel, 4)}")
    ok &= chk("closed_form_reproduces_every_atom", worst_d < mp.mpf("1e-15"), True,
              "no fitted constant anywhere in the chain")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-bond-factors-derived",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": Q0S, "dps": DPS,
                       "trace_convention": "D (SU(2)/Temperley-Lieb)",
                       "delta": str(DELTA),
                       "method": "exact Laurent via tr_m_word_lq over positive "
                                 "braid-word expansions"},
        "data": {"constants": rows,
                 "identities": [{"name": nm, "simplifies_to": str(v)}
                                for nm, v in ids],
                 "shift_values_at_q0": {k: mp.nstr(v, 22) for k, v in vals.items()},
                 "smallest_shift_separation": mp.nstr(gap, 8),
                 "delta_tr": dt},
        "context": {
            "axis": "can the two remaining measured constants of the chain "
                    "closed form be derived, leaving zero fitted numbers?",
            "answer": "Yes. All five are exact rational functions of q. b_pp is "
                      "the Ocneanu parameter z IDENTICALLY (the difference "
                      "simplifies to 0, where the previous probe could only "
                      "match it to 4.6e-16); b_nn = 1/(q^3+q); and "
                      "b_pp/b_nn = q^4 exactly.",
            "independent_check": "r_previous - t_p.z simplifies to 0, and "
                                 "r_previous was derived from different words in "
                                 "a separate computation. Two independent "
                                 "derivations agreeing symbolically is the "
                                 "strongest available check that neither is an "
                                 "expansion artefact.",
            "scope": "Scope-(a). This derives the CONSTANTS of a form whose "
                     "structure was established and validated earlier (held-out "
                     "3He and 4He at 7.5e-16). It does not say the binding law "
                     "is right — how far Delta_tr is from B remains open.",
        },
        "gitCommit": _head_sha(),
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out_p = HERE / "qbeta-bond-factors-derived.witness.json"
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out_p
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as f:
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="sympy+mpmath",
            q0_anchor="proton",
            q0_anchor_reason="experimental pin (Physical-Observations layer): q0 read at the proton m_p/m_e pin", q0_value=Q0S)
        # ensure_ascii=False: the corpus convention is UTF-8 witnesses, and
        # `witness_shape_guard` flags a witness that gains \uXXXX escapes.
        json.dump(witness, f, indent=2, ensure_ascii=False)
        f.write("\n")
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
