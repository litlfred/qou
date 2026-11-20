#!/usr/bin/env python3
"""bsym_residual_sign_form_dependence_probe.py
================================================

**Does the MIXED-SIGN premise of the #5812 scope-(b) exclusion survive a change
of binding form?**

`docs/audits/2026-08-26-faddeev-niemi-qh34-verdict.md` states the strongest
result in the low-isotope binding arc:

    "The residual the class would have to supply is mixed-sign: the corpus's
     B_sym overshoots at 2H, giving R(2H) = -0.6074 MeV against
     R(4He) = +19.6157 MeV. A non-negative functional cannot equal a
     sign-changing target -- no choice of c, no choice of Q_H, no
     reparametrisation."

That is licensed as scope-(b) on the same shape as the Option-E PROBE-4
KL-positivity prune: a non-negative weight cannot produce a mixed-sign target.

**The exclusion is only as strong as the mixed-sign premise, and that premise is
stated against ONE binding form.** This probe asks whether `sign R(2H) != sign
R(4He)` is a property of the physics or of the choice of `B_sym`. The question
is not idle: the same audit's F1 records that `B_AME(2H)` sits INSIDE the
convention-D band `[1.5598, 4.2887]`, and that an older 2H impossibility claim
was a **convention-C artifact** that did not survive R1. A sign that was once a
convention artifact deserves a second look.

METHOD
------
`R(iso) := B_AME(iso) - B_form(iso)` for each committed binding form, and the
sign pattern reported per form. Forms:

  B_sym    alpha[(Z-1)L_pp + L_pn + (N-1)L_nn]  -- the bond-chain form the
           exclusion is stated against. L re-formed in mpf here rather than
           taken from `mass_binding_dashboard._bond_type_L`, which casts to
           float at the return (recorded in the cluster-substructure verdict's
           discipline notes).
  B_lin    the production linear truncation (`binding_canonical`), read from
           `low-isotopes-binding-sweep.witness.json`. It is the LINEARIZATION
           of B_sym.
  B_law    B_lin * q0^(10A-5) -- the Delta_lambda-law near-match.
  B_magic  2*m_e*A*8G (Catalan) -- the flat magic-A form.

PRECISION
---------
mpmath end to end at 60 dps; no float64 in any arithmetic. `float()` appears
only inside display f-strings. The sign margins here are O(0.1-30 MeV) against
a float64 resolution of ~1e-16, so the SIGN verdict does not rest on the
arithmetic; the digits are carried so the magnitudes can be quoted.

WHAT THIS PROBE DOES NOT CLAIM
------------------------------
It does not claim `B_sym` is the wrong baseline, that the exclusion is void, or
that any non-negative correction now works. It measures ONE thing: whether the
mixed-sign premise is form-invariant. Establishing which form the exclusion
*ought* to be stated against is a separate judgement and is left open.
"""
from __future__ import annotations

# Bootstrap BEFORE importing the bridge: a script in a cluster subdir has
# sys.path[0] set to its own directory, and `_path_bridge` lives in
# computations/. Importing it first fails unless PYTHONPATH is already
# set — the defect class AGENTS.md records as bean `qou-0e1t`.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import pathlib
import time

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

set_compute_dps()
HERE = pathlib.Path(__file__).resolve().parent
COMP = HERE.parent

ISOTOPES = [("D", 1, 2), ("T", 1, 3), ("3He", 2, 3), ("4He", 2, 4),
            ("6Li", 3, 6), ("7Li", 3, 7), ("7Be", 4, 7)]


def bond_L_mpf(q0):
    """L_XY = -ln(z + d_XY) - (delta_e/2)*ln(1-h), convention D, in mpf.

    Re-forms `mass_binding_dashboard._bond_type_L` exactly. That accessor
    casts to float at the return, so it must not be used for arithmetic.
    """
    z = q0 ** 3 / (q0 ** 2 + 1)              # convention D
    h = q0 - 1 / q0
    delta = (q0 - 1) ** 2 * (1 - q0 ** -4) / 3   # flavour split, leading term
    d = {"pp": mp.mpf(0),
         "pn": -h * (mp.mpf(1) / 2 - delta / 4),
         "nn": -h}
    de = {"pp": mp.mpf(1), "nn": mp.mpf(-1),
          "pn": 2 * (mp.mpf(1) / 2 - delta / 4) - 1}
    lw = mp.log(1 - h)
    return {k: -mp.log(z + v) - de[k] / 2 * lw for k, v in d.items()}


def main() -> int:
    t0 = time.monotonic()
    q0 = Q_MP
    from experimental_constants import M_E_MEV
    m_e = mp.mpf(str(M_E_MEV))
    alpha = m_e / (q0 * (q0 - 1))
    L = bond_L_mpf(q0)

    # cross-check against the committed per-bond energies in the
    # cluster-substructure verdict (alpha*L_pp/pn/nn)
    xcheck = {k: alpha * v for k, v in L.items()}

    from ame_2020_binding_energies import _binding_mev_exact
    sweep = {r["atom"]: mp.mpf(r["B_pred_canonical_MeV"])
             for r in json.loads(
                 (COMP / "low-isotopes-binding-sweep.witness.json").read_text()
             )["data"]["rows"]}

    G = mp.catalan
    rows = []
    for name, Z, A in ISOTOPES:
        N = A - Z
        B_ame = mp.mpf(str(_binding_mev_exact(Z, A)))
        B_sym = alpha * ((Z - 1) * L["pp"] + L["pn"] + (N - 1) * L["nn"])
        B_lin = sweep[name]
        B_law = B_lin * q0 ** (10 * A - 5)
        B_magic = 2 * m_e * A * (8 * G)
        r = {"atom": name, "Z": Z, "N": N, "A": A, "B_AME_MeV": fmt(B_ame)}
        for label, B in (("sym", B_sym), ("lin", B_lin),
                         ("law", B_law), ("magic", B_magic)):
            R = B_ame - B
            r[f"B_{label}_MeV"] = fmt(B)
            r[f"R_{label}_MeV"] = fmt(R)
            r[f"sign_{label}"] = int(mp.sign(R))
        rows.append(r)

    patterns = {}
    for label in ("sym", "lin", "law", "magic"):
        signs = [r[f"sign_{label}"] for r in rows]
        patterns[label] = {
            "signs_by_isotope": {r["atom"]: r[f"sign_{label}"] for r in rows},
            "mixed_sign": len(set(signs)) > 1,
            "n_negative": sum(1 for s in signs if s < 0),
            "n_positive": sum(1 for s in signs if s > 0),
        }

    print(f"alpha = {mp.nstr(alpha, 12)} MeV")
    print("per-bond energies (cross-check vs cluster verdict "
          "2.541586 / 2.832825 / 3.306906):")
    for k in ("pp", "pn", "nn"):
        print(f"   alpha*L_{k} = {mp.nstr(xcheck[k], 10)}")
    print()
    hdr = f"{'iso':>5} {'A':>2} {'B_AME':>9}"
    for label in ("sym", "lin", "law", "magic"):
        hdr += f" | {'B_'+label:>10} {'R_'+label:>10}"
    print(hdr)
    for r in rows:
        line = (f"{r['atom']:>5} {r['A']:>2} "
                f"{float(mp.mpf(r['B_AME_MeV'])):>9.4f}")
        for label in ("sym", "lin", "law", "magic"):
            line += (f" | {float(mp.mpf(r['B_'+label+'_MeV'])):>10.4f} "
                     f"{float(mp.mpf(r['R_'+label+'_MeV'])):>+10.4f}")
        print(line)
    print()
    for label, p in patterns.items():
        print(f"  B_{label:<6} mixed_sign={str(p['mixed_sign']):>5}  "
              f"(neg {p['n_negative']}, pos {p['n_positive']})")

    w = WitnessBuilder("bsym-residual-sign-form-dependence", start_time=t0)
    w.set_description(
        "Does the mixed-sign premise of the #5812 scope-(b) exclusion survive "
        "a change of binding form? R = B_AME - B_form per committed form. "
        "Measures form-invariance of the sign pattern only; does not "
        "adjudicate which form the exclusion ought to be stated against.")
    w.add_data("alpha_MeV", fmt(alpha))
    w.add_data("per_bond_energy_MeV", {k: fmt(v) for k, v in xcheck.items()})
    w.add_data("rows", rows)
    w.add_data("sign_patterns", patterns)
    w.add_data("premise_is_form_invariant",
               all(p["mixed_sign"] for p in patterns.values())
               or not any(p["mixed_sign"] for p in patterns.values()))
    w.add_assertion("B_sym_is_mixed_sign", patterns["sym"]["mixed_sign"], True)
    w.save()
    print(f"\nwall {time.monotonic()-t0:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
