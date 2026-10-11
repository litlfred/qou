#!/usr/bin/env python3
"""interface_knot_markov_z_convention_d_probe.py — re-run of the
interface-knot full / constituent Markov-trace table at convention D.

Bean ``qou-7xpx``. The table in
``folio/quantum-observable-universe/mass-theory/interface-knot-markov-z-proof.md``
was measured with the excised convention-C weight ``z = sqrt(q)/(q+1)``
by ``computations/delta_lambda_fr_identity_phase5c.py``. This probe
re-measures it under convention D, ``z = q^3/(q^2+1)``, at the proton
pin, with no float64 anywhere on the value path.

Route (independent of the old producer):

    tr_M(x) = sum_lambda  y_lambda^D(q0) * chi_lambda(x)

  * ``y_lambda^D`` from ``y_lambda_su_n(n, q, 2)`` (SU(2)/TL weights,
    convention D; zero on every shape with a third row);
  * ``chi_lambda`` from ``pyhecke_native.chi_lambdas_braid_mpfr``
    (Hoefsmit seminormal characters in MPFR, q passed as a string).

The route is validated before use (``validate_route``): tr(1) = 1,
tr(s1) = z_D, tr(s1^-1) = z_D - h, tr(s1 s2) = z_D^2, tr(s1^2) = h z_D + 1,
and agreement with the independent Rust Markov-ascent
``pyhecke_native.tr_m_atomic_mpfr`` (exact BigInt Laurent coefficients)
on a mixed-sign word.

Averaged letters.  ``atom_braid_word_3A`` returns Hecke ELEMENTS
``c*sigma_g + d*1``. A letter with ``d`` in {0, -h} is sigma / sigma^-1;
any other ``d`` (the two averaged intra letters per nucleon and the
colour-weighted p-n interface) is expanded by LINEARITY into a sigma
branch (weight c) and an identity branch (weight d). The old producer
instead marshalled every averaged letter as a bare sigma (see its
``compute_tr_M_decomposition``), i.e. it traced a different element.

Three word variants are measured, because the proof block's census and
the live canonical word disagree on the p-n interface:

  ``pn_sigma``       p-n interface = sigma (the census printed in the
                     proof block: "D: 1 positive (p-n)");
  ``canonical``      the live default, bring_color_weighted:
                     sigma - h(1/2 - delta/4);
  ``strict_averaged``  sigma - h/2 (colour-blind).

For each, the factorisation (star) predicts
``tr(full)/tr(constit) = prod_interfaces (z + d_i)``.

Also measured: the per-Z constituent step
``tr(constit(Z+1,N))/tr(constit(Z,N))`` against the C-era conjecture
``2q - 1``, and the full per-Z step against ``z_D (2q - 1)``.
"""
from __future__ import annotations

import json
import os
import sys
import time
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

set_compute_dps(70)

import pyhecke_native as phn  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402  (proton pin)
from y_lambda_su_n import y_lambda_su_n  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402

DPS = 70
Q_STR = str(Q_50_DIGIT_STR)
Q = mp.mpf(Q_STR)
H = Q - 1 / Q
Z_D = Q ** 3 / (Q ** 2 + 1)
T0 = time.time()

ATOMS = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]

_Y_CACHE: dict = {}


def log(msg: str) -> None:
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def y_weights(n: int):
    if n not in _Y_CACHE:
        y = y_lambda_su_n(n, Q, 2)
        _Y_CACHE[n] = [(sh, y[sh]) for sh in y if y[sh] != 0]
    return _Y_CACHE[n]


def tr_signed(word_1idx, n: int) -> mp.mpf:
    """tr_M^D of a signed braid word [(sign, gen_1indexed), ...] in H_n."""
    ys = y_weights(n)
    chis = phn.chi_lambdas_braid_mpfr([list(sh) for sh, _ in ys],
                                      list(word_1idx), Q_STR, DPS)
    return mp.fsum(y * mp.mpf(c) for (_, y), c in zip(ys, chis))


def validate_route() -> dict:
    checks = {
        "tr(1)": (tr_signed([], 6), mp.mpf(1)),
        "tr(s1)": (tr_signed([(1, 1)], 6), Z_D),
        "tr(s1^-1)": (tr_signed([(-1, 1)], 6), Z_D - H),
        "tr(s1 s2)": (tr_signed([(1, 1), (1, 2)], 6), Z_D ** 2),
        "tr(s1^2)": (tr_signed([(1, 1), (1, 1)], 6), H * Z_D + 1),
    }
    w = [(1, 1), (-1, 2), (1, 1), (-1, 2), (1, 3), (-1, 4)]
    rust = mp.mpf(phn.tr_m_atomic_mpfr([(s, g - 1) for s, g in w], 6, Q_STR, DPS))
    checks["Rust Markov ascent, (s1 s2^-1)^2 s3 s4^-1"] = (tr_signed(w, 6), rust)
    out = {}
    for k, (a, b) in checks.items():
        err = abs(a - b)
        assert err < mp.mpf(10) ** -45, (k, a, b)
        out[k] = mp.nstr(err, 3)
    return out


def classify(word, pn_mode: str):
    """Return (letters, interface_offsets).

    letters: list of (gen_0idx, kind, d) with kind in {'+', '-', 'avg'}.
    Interface letters are those on generator 3k+2.
    """
    letters, inter = [], []
    tol = mp.mpf(10) ** -50
    for c, d, g in word:
        c, d = mp.mpf(c), mp.mpf(d)
        assert abs(c - 1) < tol
        is_inter = (g % 3 == 2)
        if abs(d) < tol:
            kind = "+"
        elif abs(d + H) < tol:
            kind = "-"
        else:
            kind = "avg"
        if is_inter and kind == "avg" and pn_mode == "pn_sigma":
            kind, d = "+", mp.mpf(0)
        letters.append((g, kind, d))
        if is_inter:
            inter.append(mp.mpf(0) if kind == "+" else (-H if kind == "-" else d))
    return letters, inter


def tr_element(letters, n: int) -> tuple:
    """tr_M^D of a product of (c*sigma + d*1) letters, by linearity."""
    avg_idx = [i for i, (_, k, _) in enumerate(letters) if k == "avg"]
    total = mp.mpf(0)
    for choice in product((0, 1), repeat=len(avg_idx)):
        pick = dict(zip(avg_idx, choice))
        w, weight = [], mp.mpf(1)
        for i, (g, k, d) in enumerate(letters):
            if k == "+":
                w.append((1, g + 1))
            elif k == "-":
                w.append((-1, g + 1))
            elif pick[i] == 0:
                w.append((1, g + 1))      # sigma branch, weight c = 1
            else:
                weight *= d               # identity branch, weight d
        total += weight * tr_signed(w, n)
    return total, len(avg_idx)


def word_for(Z, N, include_inter, mode):
    conv = "strict_averaged" if mode == "strict_averaged" else "bring_color_weighted"
    return atom_braid_word_3A(Z, N, include_inter=include_inter, pn_convention=conv)


def main() -> int:
    log(f"proton pin q0 = {Q_STR}; z_D = {mp.nstr(Z_D, 20)}; h = {mp.nstr(H, 20)}")
    validation = validate_route()
    log(f"route validated: {validation}")

    results: dict = {}
    constit: dict = {}
    for name, Z, N in ATOMS:
        n = 3 * (Z + N)
        lt, _ = classify(word_for(Z, N, False, "canonical"), "canonical")
        c_val, nb = tr_element(lt, n)
        constit[name] = c_val
        log(f"{name} H{n} constit tr = {mp.nstr(c_val, 25)} ({2**nb} branches)")

    for mode in ("pn_sigma", "canonical", "strict_averaged"):
        results[mode] = {}
        for name, Z, N in ATOMS:
            n = 3 * (Z + N)
            lf, inter = classify(word_for(Z, N, True, mode), mode)
            f_val, nb = tr_element(lf, n)
            ratio = f_val / constit[name]
            pred = mp.fprod([Z_D + d for d in inter])
            rel = abs(ratio - pred) / abs(pred)
            results[mode][name] = {
                "n": n, "full": f_val, "constit": constit[name], "ratio": ratio,
                "predicted": pred, "rel_err": rel,
                "interface_offsets_over_h": [mp.nstr(d / H, 15) for d in inter],
                "branches": 2 ** nb,
            }
            log(f"{mode:16s} {name:4s} H{n}: ratio {mp.nstr(ratio, 20)} "
                f"pred {mp.nstr(pred, 20)} rel {mp.nstr(rel, 3)} ({2**nb} br)")

    # per-Z steps (add one proton): D -> 3He, T -> 4He
    two_q_m1 = 2 * Q - 1
    steps = {}
    for lo, hi in (("D", "3He"), ("T", "4He")):
        cs = constit[hi] / constit[lo]
        fs = {m: results[m][hi]["full"] / results[m][lo]["full"] for m in results}
        steps[f"{lo}->{hi}"] = {
            "constit_step": cs,
            "constit_rel_vs_2q_minus_1": abs(cs - two_q_m1) / two_q_m1,
            "full_step": fs,
            "full_rel_vs_zD_2q_minus_1": {
                m: abs(v - Z_D * two_q_m1) / (Z_D * two_q_m1) for m, v in fs.items()},
        }
        log(f"step {lo}->{hi}: constit {mp.nstr(cs, 15)} vs 2q-1 {mp.nstr(two_q_m1, 15)}"
            f" (rel {mp.nstr(steps[f'{lo}->{hi}']['constit_rel_vs_2q_minus_1'], 4)});"
            f" full[canonical] {mp.nstr(fs['canonical'], 15)} vs z_D(2q-1) "
            f"{mp.nstr(Z_D * two_q_m1, 15)}")

    # single-nucleon traces (constit multiplicativity check)
    lp, _ = classify(atom_braid_word_3A(1, 0, include_inter=False), "canonical")
    ln, _ = classify(atom_braid_word_3A(0, 1, include_inter=False), "canonical")
    tp, _ = tr_element(lp, 3)
    tn, _ = tr_element(ln, 3)
    mult = {name: abs(constit[name] - tp ** Z * tn ** N) / abs(constit[name])
            for name, Z, N in ATOMS}
    log(f"tr(proton) = {mp.nstr(tp, 20)}, tr(neutron) = {mp.nstr(tn, 20)}; "
        f"constit = tr_p^Z tr_n^N rel err max {mp.nstr(max(mult.values()), 3)}")

    s = lambda v: mp.nstr(v, 40)  # noqa: E731
    witness = {
        "description": ("qou-7xpx: interface-knot full/constit Markov trace "
                        "re-measured at convention D, proton pin, MPFR route."),
        "convention": "D: z = q^3/(q^2+1)",
        "q0": Q_STR, "z_D": s(Z_D), "h": s(H), "dps": DPS,
        "route_validation_abs_err": validation,
        "tr_proton": s(tp), "tr_neutron": s(tn),
        "constit_multiplicativity_rel_err": {k: mp.nstr(v, 3) for k, v in mult.items()},
        "results": {m: {a: {k: (s(v) if isinstance(v, mp.mpf) else v)
                            for k, v in r.items()} for a, r in rm.items()}
                    for m, rm in results.items()},
        "per_Z_steps": {k: {
            "constit_step": s(v["constit_step"]),
            "constit_rel_vs_2q_minus_1": mp.nstr(v["constit_rel_vs_2q_minus_1"], 6),
            "full_step": {m: s(x) for m, x in v["full_step"].items()},
            "full_rel_vs_zD_2q_minus_1": {m: mp.nstr(x, 6) for m, x in
                                          v["full_rel_vs_zD_2q_minus_1"].items()},
        } for k, v in steps.items()},
        "two_q_minus_1": s(two_q_m1), "zD_two_q_minus_1": s(Z_D * two_q_m1),
        "wall_seconds": round(time.time() - T0, 1),
    }
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", os.path.basename(__file__))
    _WB.stamp_staleness_metadata(witness, script_path=__file__, engine=None,
                                 q0_anchor="proton")
    out = HERE / "interface-knot-markov-z-convention-d.witness.json"
    out.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    log(f"witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
