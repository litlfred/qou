#!/usr/bin/env python3
"""photon_chiral_ports_probe.py — the four-term chiral photon in place of the single-crossing photon.

Owner ruling (Carl, 2026-11-18, confirmed 2026-11-20; bean qou-99qc): def:photon is
    gamma(phi) = 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^-1,
and owner 2026-11-20 16:34: "make sure using the correct four-term photon that has the chirality part".
The 2026-11-17 photon-usage audit lists producers that model one photon as a single crossing
(conflicts C5, C6, C7, C9) and the gamma-gamma word probes that build on the bare vertex
V = s0 s1^-1. This probe recomputes each of their photon claims with the four-term photon, exactly
over Q(q) (h = q - q^-1 symbolic), then evaluates at the proton q0 (70 dps).

Colour weights. Only corpus-derived weights are evaluated: the eigenvalue pair
gamma_+ = gamma(0, 0, q h), gamma_- = gamma(0, 0, -q^-1 h) of
mass-theory/borromean-two-photon-factorisation (V^3 = gamma_+ gamma_-). Everything else is kept
symbolic in phi, psi. The Breit-Wheeler numbers 0.0487 / 0.0978 are labelled FITS (audit C2/C5) and are
reported only as a labelled comparison. Nothing is fitted, selected or wired.

Sections
  A  knot-operator-table.py key table  gamma . T . gamma    (record: s0 . T . s0)
  B  gram-matrix-dual.py photon / photon-pair rows         (record: 3-term fits, bare pair s0^2)
  C  gamma_gamma_pair_production_decomposition.py          (record: three gamma-gammabar events)
  D  breit_wheeler_filtration_chain_probe.py               (record: one photon = one generator)
  E  sdp_gamma_gamma_to_qqbar.py                            (record: photon = H_2 slot s0)
  F  the gamma-gamma unit gamma(phi) gamma(psi) on which every V-word probe is built

-- Ref: [leitner2026] def:photon; prop:gamma-gamma-generates-particles;
   mass-theory/borromean-two-photon-factorisation; bean qou-99qc
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import h3_photon as H  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

set_compute_dps()
Q0 = q_at(70)                       # proton pin (package default; AGENTS.md R2)
q = H.q
f0, f1, f01, p0, p1, p01 = sp.symbols("phi0 phi1 phi01 psi0 psi1 psi01")
GPH, GPS = H.gamma(f0, f1, f01), H.gamma(p0, p1, p01)
GP, GM = H.GAMMA_PLUS, H.GAMMA_MINUS
CHECKS = []


def at_q0(expr):
    e = sp.sympify(expr)
    return mp.mpf(0) if e == 0 else sp.lambdify(q, e, modules="mpmath")(Q0)


def ex(a):
    """Exact NF as strings, plus 70-dps values at the proton q0."""
    return {H.NAMES[w]: {"exact": str(c), "q0": fmt(at_q0(c))} for w, c in a.items()}


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}")


def tr_q0(a):
    t = H.trace(a)
    return {"exact": str(t), "q0": fmt(at_q0(t))}


# ---------------------------------------------------------------- A
# σ₀σ₁σ₀ closes to the Hopf link and (σ₀σ₁)²σ₀ to the T(2,4) link (both in B_3);
# keyed T_{2,3} / T_{2,5} until 2026-11-21. Labels only, words unchanged.
KNOT_OPERATORS = {"T_{1,0}": (), "T_{2,1}": (0,), "T_{2,2}": (0, 0), "T_{2,2}^{(3)}": (0, 1, 0),
                  "T_{2,4}^{(3)}": (0, 1, 0, 1, 0)}


def elem(w):
    out = H.ONE
    for s in w:
        out = H.mul(out, H.S0 if s == 0 else H.S1)
    return out


def section_a():
    print("A  key table gamma . T . gamma")
    rows = {}
    for name, w in KNOT_OPERATORS.items():
        T = elem(w)
        old = H.mul(H.mul(H.S0, T), H.S0)
        new_pm = H.mul(H.mul(GP, T), GM)
        new_mp = H.mul(H.mul(GM, T), GP)
        sym = H.mul(H.mul(GPH, T), GPS)
        e_sym = sp.factor(sym.get((0, 1, 0), 0))
        rows[name] = {
            "record_s0_T_s0": {"nf": ex(old), "e_minus": (0, 1, 0) in old, "tr_M": tr_q0(old)},
            "gamma_plus_T_gamma_minus": {"nf": ex(new_pm), "e_minus": (0, 1, 0) in new_pm, "tr_M": tr_q0(new_pm)},
            "gamma_minus_T_gamma_plus": {"nf": ex(new_mp), "e_minus": (0, 1, 0) in new_mp, "tr_M": tr_q0(new_mp)},
            "symbolic_e_minus_coefficient": str(e_sym),
        }
        print(f"    {name}: e- record {(0,1,0) in old}, gamma+Tgamma- {(0,1,0) in new_pm}, "
              f"tr_M record {rows[name]['record_s0_T_s0']['tr_M']['q0'][:14]} -> "
              f"{rows[name]['gamma_plus_T_gamma_minus']['tr_M']['q0'][:14]}")
    return rows


# ---------------------------------------------------------------- B
def section_b():
    print("B  gram-matrix-dual photon rows")
    out = {}
    out["photon_nf_chiral"] = {H.NAMES[w]: str(c) for w, c in GPH.items()}
    out["photon_nf_straight_chart"] = {H.NAMES[w]: str(c) for w, c in
                                       H.gamma_straight(f0 - H.h * f01, f1, f01).items()}
    # labelled fits: 3-term (phi01 = 0) specialisations; identical in both charts
    fits = {"linear_fit_0.0487": ("0.0487", "0.0487", "0"), "circular_fit_0.0978_a": ("0.0978", "0", "0"),
            "circular_fit_0.0978_b": ("0", "0.0978", "0")}
    for k, (a, b, c) in fits.items():
        a, b, c = sp.Rational(a), sp.Rational(b), sp.Rational(c)
        same = H.add(H.gamma(a, b, c), H.scale(-1, H.gamma_straight(a, b, c))) == {}
        out[k] = {"LABEL": "FIT (audit 2026-11-17 C2/C5) -- comparison only, not a derived weight",
                  "phi01": "0", "same_in_both_charts": same}
        check(f"B_{k}_unchanged_by_ruling", same)
    bare_pair_record = H.mul(H.S0, H.S0)
    bare_pair = H.mul(H.gamma(0, 0, 0), H.gamma(0, 0, 0))
    pair = H.mul(GP, GM)
    out["pair_record_s0_squared"] = {"nf": ex(bare_pair_record), "tr_M": tr_q0(bare_pair_record)}
    out["pair_bare_photons"] = {"nf": ex(bare_pair), "tr_M": tr_q0(bare_pair)}
    out["pair_eigenvalue_pair_equals_V3"] = {"nf": ex(pair), "tr_M": tr_q0(pair),
                                             "chi": {lam: str(H.chi(pair, lam)) for lam in ("sym", "std", "alt")}}
    check("B_bare_photon_pair_is_identity", bare_pair == {(): 1})
    return out


# ---------------------------------------------------------------- C
def section_c():
    print("C  Borromean braid as photons")
    V3 = H.mul(H.mul(H.V, H.V), H.V)
    ok = H.add(V3, H.scale(-1, H.mul(GP, GM))) == {}
    comm = H.add(H.mul(GP, GM), H.scale(-1, H.mul(GM, GP))) == {}
    check("C_V3_equals_gamma_plus_gamma_minus", ok)
    check("C_factors_commute", comm)
    return {"V3_nf": ex(V3), "tr_M_V3": tr_q0(V3),
            "record": "three gamma-gammabar events, photon = s0, anti-photon = s1^-1",
            "under_ruling": "two four-term photons gamma(0,0,qh) gamma(0,0,-q^-1 h); V = s0 s1^-1 is one photon's fourth term",
            "V_letters": 3, "four_term_photons": 2, "tr_M_unchanged": True}


# ---------------------------------------------------------------- D
def section_d():
    print("D  Breit-Wheeler promote / split under the four-term photon")
    single = {"gamma_0_0_phi01": H.grades(H.gamma(0, 0, f01)), "V_alone": H.grades(H.V)}
    par = H.mul(H.gamma(f0, 0, 0), H.gamma(p0, 0, 0))
    perp = H.mul(H.gamma(f0, 0, 0), H.gamma(0, p1, 0))
    full = H.mul(GPH, GPS)
    pair = H.mul(GP, GM)
    e_full = sp.factor(full.get((0, 1, 0), 0))
    out = {
        "single_photon_grades": single,
        "parallel_s0_terms_grades": H.grades(par),
        "perpendicular_s0_s1_terms_grades": H.grades(perp),
        "full_product_grades": H.grades(full),
        "full_product_e_minus_coefficient": str(e_full),
        "eigenvalue_pair_product_grades": H.grades(pair),
        "eigenvalue_pair_e_minus_coefficient": str(pair.get((0, 1, 0), 0)),
    }
    check("D_e_minus_coefficient_is_phi01_psi0_plus_phi1_psi01",
          sp.simplify(e_full - (f01 * p0 + f1 * p01)) == 0, f"got {e_full}")
    check("D_single_vertex_photon_is_not_grade_homogeneous", single["gamma_0_0_phi01"] == [0, 1, 2])
    print(f"    grades: single gamma(0,0,phi01) {single['gamma_0_0_phi01']}; full product {out['full_product_grades']};"
          f" eigenvalue pair {out['eigenvalue_pair_product_grades']}; e- coeff {e_full}")
    return out


# ---------------------------------------------------------------- E
def section_e():
    print("E  Wedderburn blocks (sdp_gamma_gamma_to_qqbar): H_3 photon, PSD at q0")
    out = {"record": "H_2 scaffold: photon = slot s0; the chiral vertex needs s1, so a four-term photon lives in H_3"}
    for nm, el in (("gamma_plus", GP), ("gamma_minus", GM), ("gamma_plus_gamma_minus", H.mul(GP, GM))):
        row = {}
        for lam in ("sym", "std", "alt"):
            B = H.block(el, lam)
            Bs = (B + B.T) / 2
            ev = [at_q0(e) for e in Bs.eigenvals(multiple=True)]
            row[lam] = {"block": str(B), "sym_part_eigs_q0": [fmt(mp.re(e)) for e in ev],
                        "chi_q0": fmt(at_q0(B.trace())), "psd_sym_part": all(mp.re(e) >= 0 for e in ev)}
        out[nm] = row
        print(f"    {nm}: chi sym {row['sym']['chi_q0'][:12]} std {row['std']['chi_q0'][:12]} alt {row['alt']['chi_q0'][:12]}; "
              f"PSD(sym part) {[row[l]['psd_sym_part'] for l in ('sym','std','alt')]}")
    return out


# ---------------------------------------------------------------- F
def section_f():
    print("F  the gamma-gamma unit: characters (reading 3 needs chi >= 0 on sym and std under D)")
    full = H.mul(GPH, GPS)
    out = {"chi_symbolic": {lam: str(H.chi(full, lam)) for lam in ("sym", "std", "alt")},
           "tr_M_symbolic": str(H.trace(full))}
    vw = H.mul(H.mul(H.V, H.V), H.V)
    pure = H.mul(H.gamma(0, 0, f01), H.gamma(0, 0, p01))
    out["chi_pure_vertex_photons"] = {lam: str(H.chi(pure, lam)) for lam in ("sym", "std", "alt")}
    out["chi_V3_q0"] = {lam: fmt(at_q0(H.chi(vw, lam))) for lam in ("sym", "std", "alt")}
    # first-order sensitivity of the eigenvalue-pair unit to the chiral single-crossing part
    sens = {}
    for var in (f0, f1, p0, p1):
        sub = {f0: 0, f1: 0, p0: 0, p1: 0, f01: q * H.h, p01: -H.h / q}
        sens[str(var)] = {lam: fmt(at_q0(sp.diff(H.chi(full, lam), var).subs(sub)))
                          for lam in ("sym", "std", "alt")}
    out["d_chi_d_chiral_part_at_eigenvalue_pair_q0"] = sens
    out["d_trM_d_chiral_part_at_eigenvalue_pair_q0"] = {
        str(var): fmt(at_q0(sp.diff(H.trace(full), var).subs(
            {f0: 0, f1: 0, p0: 0, p1: 0, f01: q * H.h, p01: -H.h / q}))) for var in (f0, f1, p0, p1)}
    eqv = all(sp.simplify(H.chi(full, lam).subs({f0: 0, f1: 0, p0: 0, p1: 0}) - H.chi(pure, lam)) == 0
              for lam in ("sym", "std", "alt"))
    check("F_V_words_are_the_phi0_phi1_zero_specialisation", eqv)
    print(f"    d chi / d(chiral part) at the eigenvalue pair: {sens}")
    return out


# ---------------------------------------------------------------- G
TABLE_RECORD = {"1": "1.005", "s0": "0.099", "s1": "0.099", "L+": "0.043", "L-": "0.003", "e-": "0.002"}


def section_g():
    """tbl:four-term-pair-nucleon-table1-data has no recorded producer or weights. The six rounded
    entries are reproduced by gamma_straight(a, a, b)^2 with a = 0.0487 (the Breit-Wheeler linear
    FIT) and b = 0.02 (unsourced). Recompute the same weights with the ruled photon."""
    print("G  tbl:four-term-pair-nucleon-table1-data reconstruction")
    a, b = sp.Rational("0.0487"), sp.Rational("0.02")
    old = H.mul(H.gamma_straight(a, a, b), H.gamma_straight(a, a, b))
    new = H.mul(H.gamma(a, a, b), H.gamma(a, a, b))
    row_old = {H.NAMES[w]: fmt(at_q0(old.get(w, 0))) for w in H.WORDS}
    row_new = {H.NAMES[w]: fmt(at_q0(new.get(w, 0))) for w in H.WORDS}
    repro = all(abs(mp.mpf(row_old[k]) - mp.mpf(v)) <= mp.mpf("0.0005") for k, v in TABLE_RECORD.items())
    check("G_record_reproduced_by_straight_0.0487_0.02_to_rounding", repro)
    for k in TABLE_RECORD:
        print(f"    {k:>3}: record {TABLE_RECORD[k]}  straight {row_old[k][:9]}  ruled {row_new[k][:9]}")
    return {"LABEL": "weights reconstructed, not recorded: a = 0.0487 is a labelled FIT, b = 0.02 unsourced",
            "record_rounded": TABLE_RECORD, "straight_chart_q0": row_old, "ruled_photon_q0": row_new,
            "tr_M_straight": tr_q0(old), "tr_M_ruled": tr_q0(new)}


def main() -> int:
    res = {"A_knot_operator_key_table": section_a(), "B_gram_matrix_dual": section_b(),
           "C_borromean_as_photons": section_c(), "D_breit_wheeler_filtration": section_d(),
           "E_sdp_wedderburn_blocks": section_e(), "F_gamma_gamma_unit": section_f(),
           "G_four_term_pair_nucleon_table": section_g()}
    wb = WitnessBuilder("photon-chiral-ports", engine="sympy+mpmath", output_dir=HERE)
    for n, ok, d in CHECKS:
        wb.add_assertion(n, computed="1" if ok else "0", expected="1", source=d or "exact Q(q)")
    wb.save({"q0Anchor": "proton", "q0AnchorReason": "qou_substrate.constants.q_at(70), package default",
             "markov_convention": "D, z = q^3/(q^2+1)",
             "description": "PROBE (bean qou-99qc): four-term chiral photon gamma = 1 + phi0 s0 + phi1 s1 + "
                            "phi01 s0 s1^-1 in place of the single-crossing photon of audit 2026-11-17 C5/C6/C7/C9; "
                            "only corpus-derived weights (eigenvalue pair) evaluated; 0.0487/0.0978 labelled fits.",
             "results": res})
    return 0 if all(ok for _, ok, _ in CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
