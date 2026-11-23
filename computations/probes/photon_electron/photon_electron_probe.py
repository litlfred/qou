#!/usr/bin/env python3
"""photon_electron_probe.py — one photon on γγ electron candidates: single-crossing terms and the four-term arm.

Scope note (2026-11-20). The pre-registered rows read "one photon" as a single crossing sigma_g^{+-1}.
Under def:photon (gamma = 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^-1, owner ruling 2026-11-18, confirmed
2026-11-20) those rows are the phi0 / phi1 terms of one photon. `four_term_arm` adds the full photon.

Pre-registered in preregistration.md (4ba00ecab5b). Bean qou-a1hh, PR #7741. mpmath, convention D, proton q₀.
Nothing fitted, selected or wired.
-- Ref: [manuscript] bean qou-a1hh; bean qou-ales
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
mp.mp.dps = max(mp.mp.dps, 40)  # the h2_one_rule base works at 40 dps; stated here so this
                                # probe does not rely on an import side effect two modules away

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
sys.path.insert(0, str(HERE.parent / "gg_symmetry"))
import h2_gg_atom_probe as ga  # noqa: E402
import gg_symmetry_probe as gs  # noqa: E402

base, log, TOL = ga.base, ga.log, ga.TOL
ONE, ZERO, H = base.ONE, base.ZERO, base.H
from qou_substrate.witness import WitnessBuilder  # noqa: E402

V = [(ONE, ZERO, 0), (ONE, -H, 1)]
VB = [(ONE, -H, 0), (ONE, ZERO, 1)]
CANDS = {"V^0": [], **{f"V^{k}": V * k for k in (3, 6, 9)}, **{f"Vbar^{k}": VB * k for k in (3, 6, 9)}}


def s(g, e):
    return (ONE, ZERO, g) if e > 0 else (ONE, -H, g)


def chars(w):
    return gs.chars(w)


def fmt(c):
    return {f"{m}:{mu}": mp.nstr(v, 15) for (m, mu), v in sorted(c.items())}


# ---- four-term chiral photon arm (added 2026-11-20) ------------------------------------------
# def:photon is gamma(phi) = 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^-1 (owner ruling 2026-11-18,
# confirmed 2026-11-20, bean qou-99qc). The single-crossing rows above are the phi0 / phi1
# TERMS of one photon, not a photon. Characters are linear in the element (checked: P1), so
# chi(E gamma) = chi(E) + phi0 chi(E s0) + phi1 chi(E s1) + phi01 chi(E V). The four per-term
# characters are recorded (phi stays symbolic), and the photon is evaluated only at the
# corpus-derived colour weights: the eigenvalue pair gamma_+ = gamma(0, 0, q h),
# gamma_- = gamma(0, 0, -q^-1 h) of mass-theory/borromean-two-photon-factorisation. No phi
# is fitted. Note those weights have phi0 = phi1 = 0.
PHOTON_TERMS = {"1": [], "s0": [s(0, 1)], "s1": [s(1, 1)], "V": [s(0, 1), s(1, -1)]}


def _comb(parts, wts):
    return {k: sum(w * parts[t][k] for t, w in wts.items()) for k in parts["1"]}


def four_term_arm():
    qv = base.Q
    hv = qv - 1 / qv
    pair = {"gamma_plus": {"1": ONE, "V": qv * hv}, "gamma_minus": {"1": ONE, "V": -hv / qv}}
    lin_worst = mp.mpf(0)
    out = {"definition": "gamma(phi) = 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^-1",
           "weights": "eigenvalue pair phi01 = q h, -q^-1 h (phi0 = phi1 = 0); per-term chars give any phi"}
    for name, w in CANDS.items():
        # linearity check: chi(w s0^-1) = chi(w s0) - h chi(w)
        a, b, c = chars(w + [s(0, -1)]), chars(w + [s(0, 1)]), chars(w)
        lin_worst = max(lin_worst, max(abs(a[k] - (b[k] - hv * c[k])) for k in a))
        row = {}
        for side in ("absorb", "emit"):
            parts = {t: chars(w + tw if side == "absorb" else tw + w) for t, tw in PHOTON_TERMS.items()}
            row[f"{side}_per_term"] = {t: fmt(v) for t, v in parts.items()}
            for pn, wts in pair.items():
                cc = _comb(parts, wts)
                row[f"{side}_{pn}"] = {"passes": all(v >= -TOL for v in cc.values()), "chars": fmt(cc)}
        pa = {t: chars(w + tw) for t, tw in PHOTON_TERMS.items()}
        cp, cm = _comb(pa, pair["gamma_plus"]), _comb(pa, pair["gamma_minus"])
        R = {k: cp[k] - cm[k] for k in cp}
        row["R_pair"] = fmt(R)
        row["DeltaR_pair_level2"] = mp.nstr(R[(2, (1, 1))] - R[(2, (2,))], 15)
        out[name] = row
        log(f"[four-term] {name}: absorb gamma+ passes {row['absorb_gamma_plus']['passes']}, "
            f"gamma- passes {row['absorb_gamma_minus']['passes']}; DeltaR_pair {row['DeltaR_pair_level2']}")
    return out, lin_worst


def main() -> int:
    worst = mp.mpf(0)
    hval = mp.mpf(H) if not isinstance(H, tuple) else None
    out = {}
    for name, w in CANDS.items():
        row = {"E": fmt(chars(w))}
        cE = chars(w)
        for g in (0, 1):
            for e in (1, -1):
                for kind, word in (("absorb", w + [s(g, e)]), ("emit", [s(g, e)] + w),
                                   ("compton", [s(g, e)] + w + [s(g, -e)])):
                    c = chars(word)
                    row[f"{kind}_g{g}_{'+' if e > 0 else '-'}"] = {
                        "passes": all(v >= -TOL for v in c.values()), "chars": fmt(c)}
            cp, cm = chars(w + [s(g, 1)]), chars(w + [s(g, -1)])
            R = {k: cp[k] - cm[k] for k in cp}
            row[f"R_g{g}"] = fmt(R)
            for lam in ((3,), (2, 1)):
                worst = max(worst, abs(R[(3, lam)] - hval * cE[(3, lam)]))
        out[name] = row
        log(f"{name}: R_g0 level2 (2)={row['R_g0']['2:(2,)']} (1,1)={row['R_g0']['2:(1, 1)']}; "
            f"absorb passes " + str({k: v['passes'] for k, v in row.items() if k.startswith('absorb')}))
    ok = worst < mp.mpf("1e-30")
    log(f"[{'PASS' if ok else 'FAIL'}] P0_level3_response_is_h_chi: worst {mp.nstr(worst, 5)}")
    four, lin_worst = four_term_arm()
    lin_ok = lin_worst < mp.mpf("1e-30")
    log(f"[{'PASS' if lin_ok else 'FAIL'}] P1_chars_linear_in_the_element: worst {mp.nstr(lin_worst, 5)}")
    wb = WitnessBuilder("photon-electron", engine="mpmath", output_dir=HERE)
    wb.add_assertion("P0_level3_response_is_h_chi", computed="1" if ok else "0", expected="1",
                     source=f"worst {mp.nstr(worst, 5)}")
    wb.add_assertion("P1_chars_linear_in_the_element", computed="1" if lin_ok else "0", expected="1",
                     source=f"chi(w s^-1) = chi(w s) - h chi(w); worst {mp.nstr(lin_worst, 5)}")
    wb.save({"q0Anchor": "proton", "q0AnchorReason": "via h2_gg_atom (cf.Q, proton pin)",
             "description": "PROBE (bean qou-a1hh): one photon sigma_g^{+-1} absorbed/emitted/Compton-scattered on "
                            "gamma-gamma electron candidates on 3 strands; reading 3 levels 1-3 and photon response. "
                            "Pre-registered. Nothing fitted or wired.",
             "weight_family": "markov_y_lambda_convention_D", "results": out,
             "four_term_photon_arm": four})
    return 0 if (ok and lin_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
