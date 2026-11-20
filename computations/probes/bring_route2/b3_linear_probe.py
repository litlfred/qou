#!/usr/bin/env python3
"""Route 2, Part B option B3 (recipe: preregistration-b3b4.md, committed 132dd4894f before this run).

Evaluate the nucleon ELEMENT (a weighted sum of braids) in a 2x2 linear representation and
report trace, determinant and the translation length of the projective action. Two
normalisations are computed and reported side by side; neither is chosen by its numbers:

  N-H  rho_2(s_i) = -q0^-1 * S_i(q0^2)   (the 2-dim irreducible of H_3(q0), where the element lives)
  N-B  rho(s_i)   = S_i(-q0), unscaled   (the owner-ruled R-q point for single braid words)

No ranking, no selection, no Q_beta / CODATA / mass input. mpmath 60 dps throughout.
"""
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import signed_candidates_probe as SC  # noqa: E402  (also puts the repo packages on sys.path)
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 60
TOL = mp.mpf(10) ** -25


def S(i, t):
    return mp.matrix([[-t, 1], [0, 1]]) if i == 0 else mp.matrix([[1, 0], [t, -t]])


def classify(M):
    d = mp.det(M)
    tr = M[0, 0] + M[1, 1]
    out = {"trace": tr, "det": d}
    if abs(d) < mp.mpf(10) ** -40:
        out.update(type="degenerate (det = 0), no length")
        return out
    x = abs(tr) / mp.sqrt(abs(d))
    out["x"] = x
    if d < 0:
        out.update(type="glide reflection", ell=2 * mp.asinh(x / 2))
    elif abs(x - 2) < TOL:
        out.update(type="parabolic", ell=mp.mpf(0))
    elif x > 2:
        out.update(type="hyperbolic", ell=2 * mp.acosh(x / 2))
    else:
        out.update(type="elliptic", ell=mp.mpf(0), theta=2 * mp.acos(x / 2))
    return out


def word_mat(w, gens):
    M = mp.eye(2)
    for g, e in w:
        M = M * (gens[g] if e == 1 else gens[g] ** -1)
    return M


def element_mat(terms, gens):
    M = mp.zeros(2, 2)
    for w in terms.values():
        M += word_mat(w, gens) / 4
    return M


def ser(o):
    if isinstance(o, dict):
        return {k: ser(v) for k, v in o.items()}
    if isinstance(o, mp.mpf):
        return mp.nstr(o, 25)
    return o


def main():
    q = Q_MP
    h = q - 1 / q
    NH = {i: -S(i, q ** 2) / q for i in (0, 1)}
    NB = {i: S(i, -q) for i in (0, 1)}
    pt, nt = SC.proton_terms(), SC.neutron_terms()
    checks = {}

    # check 1: Hecke and braid relations for N-H
    e1 = max(mp.mnorm(NH[i] ** 2 - h * NH[i] - mp.eye(2), 1) for i in (0, 1))
    e2 = mp.mnorm(NH[0] * NH[1] * NH[0] - NH[1] * NH[0] * NH[1], 1)
    checks["NH_hecke_and_braid_relations"] = bool(e1 < mp.mpf(10) ** -40 and e2 < mp.mpf(10) ** -40)

    # check 2 and 3: N-H matrix from the builder's normal form; character chi_(2,1)
    from pyhecke import atom as A
    basis = [mp.eye(2), NH[0], NH[1], NH[1] * NH[0], NH[0] * NH[1], NH[0] * NH[1] * NH[0]]
    chi21 = [mp.mpf(2), h, h, mp.mpf(-1), mp.mpf(-1), mp.mpf(0)]
    ok2 = ok3 = True
    for quarks, terms in (("uud", pt), ("udd", nt)):
        nf = A.build_nucleon_nf_mp(list(quarks), 60)
        from_nf = mp.zeros(2, 2)
        for c, B in zip(nf, basis):
            from_nf += c * B
        ok2 &= mp.mnorm(from_nf - element_mat(terms, NH), 1) < mp.mpf(10) ** -40
        chi = sum(c * x for c, x in zip(nf, chi21))
        ok3 &= abs(chi - (from_nf[0, 0] + from_nf[1, 1])) < mp.mpf(10) ** -40
    checks["NH_term_sum_equals_builder_normal_form"] = bool(ok2)
    checks["NH_trace_equals_chi_21_of_builder"] = bool(ok3)

    # check 4: N-B at t = -1 reproduces the SL(2,Z) traces of results_signed.json
    stored = json.loads((HERE / "results_signed.json").read_text())["proton_terms"]
    cl = {i: S(i, mp.mpf(-1)) for i in (0, 1)}
    ok4 = True
    for k, w in {**pt, **nt}.items():
        M = word_mat(w, cl)
        ok4 &= abs(M[0, 0] + M[1, 1] - stored[k]["trace"]) < mp.mpf(10) ** -40
    checks["NB_classical_limit_matches_sl2z"] = bool(ok4)

    out = {"recipe": "preregistration-b3b4.md (132dd4894f)", "q0": Q_50_DIGIT_STR, "checks": checks}
    for name, gens in (("N-H", NH), ("N-B", NB)):
        sec = {"proton element": classify(element_mat(pt, gens)),
               "neutron element": classify(element_mat(nt, gens)),
               "gamma-gamma core": classify(word_mat(SC.CORE, gens))}
        for k, w in {**pt, **nt}.items():
            sec[k] = classify(word_mat(w, gens))
        out[name] = sec
    out = ser(out)
    for name in ("N-H", "N-B"):
        for k, v in out[name].items():
            print(name, k, v["type"], v.get("x"), v.get("ell"), v["det"])
    print(json.dumps(checks))
    (HERE / "results_b3.json").write_text(json.dumps(out, indent=1) + "\n")
    sys.exit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
