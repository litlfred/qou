#!/usr/bin/env python3
"""four_term_pair_nucleon_table.py — producer for tbl:four-term-pair-nucleon-table1-data.

The table lists the H_3(q) normal form (basis 1, s0, s1, L+ = s0 s1, L- = s1 s0,
e- = s0 s1 s0) of one gamma-gamma product, gamma(phi) * gamma(phi).  Until this producer the
table had no recorded producer, witness or colour weights (PR #8583 caveat; PR #8595 §G).

Photon forms
  ruled  (def:photon, owner ruling 2026-11-18, confirmed 2026-11-20, bean qou-99qc):
         gamma(phi) = 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^{-1},   s1^{-1} = s1 - h
  old    (superseded straight form):  1 + phi0 s0 + phi1 s1 + phi01 s0 s1

Arms
  W  reconstructed weights phi = (a, a, b), a = 0.0487, b = 0.02.  These are NOT derived:
     a = 0.0487 is the Breit-Wheeler linear FIT (to 2 m_e); b = 0.02 has no source and was
     reconstructed by matching the six rounded record entries (#8595 §G).  The table under these
     weights is a worked illustration of the gamma-gamma NF, not a prediction.
     Step 1 recomputes the record with the OLD form and checks every entry against the record at
     the record's rounding; step 2 restates it with the ruled form at the same weights.
  E  the corpus-derived eigenvalue pair gamma_+ = gamma(0,0,q h), gamma_- = gamma(0,0,-q^-1 h)
     (mass-theory/borromean-two-photon-factorisation, V^3 = gamma_+ gamma_-).  A product of two
     DIFFERENT photons, not a square; reported as a labelled comparison arm.

Arithmetic: exact over Q(q) (sympy, h = q - q^-1 symbolic; decimal weights entered as exact
rationals), evaluated at the proton q0 (qou_substrate.constants.q_at, package default, AGENTS.md
R2) with mpmath at the package compute precision; serialised with qou_substrate.precision.fmt.
No floats.  Nothing is fitted here: the window scan in section W only MEASURES how loosely the
record pins the reconstructed weights.

-- Ref: [leitner2026] def:photon; prop:four-term-pair-nucleon; prop:confinement-universality;
   mass-theory/borromean-two-photon-factorisation; bean qou-99qc
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

set_compute_dps()
Q0 = q_at(70)

# ----------------------------------------------------------------- H_3(q) normal form
q = sp.Symbol("q", positive=True)
h = q - 1 / q
WORDS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NAMES = {(): "1", (0,): "s0", (1,): "s1", (0, 1): "L+", (1, 0): "L-", (0, 1, 0): "e-"}


def _canon(w):
    return (0, 1, 0) if w == (1, 0, 1) else w


def _gen_times(s, w):
    """s * w in the reduced-word basis, using s^2 = h s + 1 and the braid relation."""
    w = _canon(w)
    if len(w) == 3:                       # s * s0 s1 s0 (= s1 s0 s1)
        return {w: h, (1 - s, s): 1}
    if w and w[0] == s:
        return {w: h, w[1:]: 1}
    return {_canon((s,) + w): 1}


def _clean(a):
    out = {}
    for w, c in a.items():
        c = sp.factor(sp.simplify(c))
        if c != 0:
            out[w] = c
    return out


def mul(a, b):
    out = {}
    for wa, ca in a.items():
        for wb, cb in b.items():
            cur = {wb: ca * cb}
            for s in reversed(wa):
                nxt = {}
                for w, c in cur.items():
                    for w2, c2 in _gen_times(s, w).items():
                        nxt[w2] = nxt.get(w2, 0) + c * c2
                cur = nxt
            for w, c in cur.items():
                out[w] = out.get(w, 0) + c
    return _clean(out)


def lin(*terms):
    out = {}
    for c, x in terms:
        for w, v in x.items():
            out[w] = out.get(w, 0) + c * v
    return _clean(out)


ONE, S0, S1 = {(): 1}, {(0,): 1}, {(1,): 1}
S1INV = lin((1, S1), (-h, ONE))
V = mul(S0, S1INV)                 # chiral vertex s0 s1^{-1}
LP = {(0, 1): 1}                   # s0 s1, the superseded fourth term


def gamma_ruled(a0, a1, a01):
    return lin((1, ONE), (a0, S0), (a1, S1), (a01, V))


def gamma_old(a0, a1, a01):
    return lin((1, ONE), (a0, S0), (a1, S1), (a01, LP))


# ----------------------------------------------------------------- helpers
CHECKS: list[tuple[str, bool, str]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))


def at_q0(expr):
    e = sp.sympify(expr)
    return mp.mpf(0) if e == 0 else sp.lambdify(q, e, modules="mpmath")(Q0)


def row(a):
    return {NAMES[w]: at_q0(a.get(w, 0)) for w in WORDS}


def round3(x):
    """Round half away from zero to 3 decimals, as an exact decimal string."""
    n = int(mp.floor(abs(x) * 1000 + mp.mpf(1) / 2))
    return ("-" if x < 0 else "+") + f"{n // 1000}.{n % 1000:03d}"


# The record, as printed in the block before this producer (rounded to 3 decimals).
RECORD = {"1": "1.005", "s0": "0.099", "s1": "0.099", "L+": "0.043", "L-": "0.003", "e-": "0.002"}
A_FIT, B_UNSOURCED = sp.Rational("0.0487"), sp.Rational("0.02")


def nf_exact(a):
    return {NAMES[w]: str(c) for w, c in a.items()}


def nf_q0(a):
    return {k: fmt(v) for k, v in row(a).items()}


# ----------------------------------------------------------------- symbolic NF
def section_symbolic():
    print("S  gamma(phi) gamma(psi) NF, exact over Q(q, phi, psi)")
    f0, f1, f01, p0, p1, p01 = sp.symbols("phi0 phi1 phi01 psi0 psi1 psi01")
    ruled = mul(gamma_ruled(f0, f1, f01), gamma_ruled(p0, p1, p01))
    old = mul(gamma_old(f0, f1, f01), gamma_old(p0, p1, p01))
    # chart identity: ruled photon = old (straight) photon with phi0 -> phi0 - h phi01
    chart = lin((1, gamma_ruled(f0, f1, f01)), (-1, gamma_old(f0 - h * f01, f1, f01))) == {}
    check("S_ruled_equals_old_in_shifted_chart", chart, "gamma(f0,f1,f01) = gamma_old(f0 - h f01, f1, f01)")
    return {"ruled_gamma_phi_gamma_psi": nf_exact(ruled), "old_gamma_phi_gamma_psi": nf_exact(old),
            "chart_identity": "gamma_ruled(phi0, phi1, phi01) = gamma_old(phi0 - h*phi01, phi1, phi01), h = q - 1/q"}


# ----------------------------------------------------------------- arm W
def section_w():
    print("W  reconstructed weights phi = (0.0487, 0.0487, 0.02)  [FIT + UNSOURCED]")
    g_old = gamma_old(A_FIT, A_FIT, B_UNSOURCED)
    g_new = gamma_ruled(A_FIT, A_FIT, B_UNSOURCED)
    old = mul(g_old, g_old)
    new = mul(g_new, g_new)
    r_old, r_new = row(old), row(new)
    rounded_old = {k: round3(v) for k, v in r_old.items()}
    match = {k: rounded_old[k].lstrip("+") == RECORD[k] for k in RECORD}
    check("W1_old_form_reproduces_every_record_entry_at_3dp", all(match.values()),
          ", ".join(f"{k}:{rounded_old[k]}" for k in RECORD))
    delta = {k: r_new[k] - r_old[k] for k in RECORD}
    # ruled = old with phi0 -> phi0 - h phi01 (chart identity, section S), so the shift enters
    # through the s0 slot; check that s0 is the entry that moves most.
    big = max(delta, key=lambda k: abs(delta[k]))
    check("W2_largest_move_is_s0", big == "s0", f"largest |delta| at {big}: {mp.nstr(delta[big], 8)}")
    s_split = r_new["s0"] != r_new["s1"]
    check("W3_ruled_form_splits_s0_s1", s_split,
          f"s0 {mp.nstr(r_new['s0'], 9)} vs s1 {mp.nstr(r_new['s1'], 9)}")

    # How loosely does the record pin (a, b)?  Scan a grid of decimal weights; MEASUREMENT only.
    a_sym, b_sym = sp.symbols("a b")
    g = gamma_old(a_sym, a_sym, b_sym)
    sq = mul(g, g)
    exprs = {NAMES[w]: sp.lambdify((q, a_sym, b_sym), sp.sympify(sq.get(w, 0)), "mpmath") for w in WORDS}
    a_ok, b_ok, n_ok = [], [], 0
    for ia in range(450, 531):            # a in [0.0450, 0.0530], step 1e-4
        a = mp.mpf(ia) / 10000
        for ib in range(0, 61):           # b in [0.000, 0.060], step 1e-3
            b = mp.mpf(ib) / 1000
            ok = all(round3(exprs[k](Q0, a, b)).lstrip("+") == RECORD[k] for k in RECORD)
            if ok:
                n_ok += 1
                a_ok.append(ia)
                b_ok.append(ib)
    window = {"grid": "a in [0.0450, 0.0530] step 1e-4; b in [0.000, 0.060] step 1e-3",
              "points_reproducing_record": n_ok,
              "a_range": [str(sp.Rational(min(a_ok), 10000)), str(sp.Rational(max(a_ok), 10000))] if a_ok else None,
              "b_range": [str(sp.Rational(min(b_ok), 1000)), str(sp.Rational(max(b_ok), 1000))] if b_ok else None,
              "reading": "the six rounded entries constrain the weights only to this window; "
                         "(0.0487, 0.02) is one point in it, so the reconstruction is not unique"}
    check("W4_reconstructed_point_inside_window", n_ok > 0 and min(a_ok) <= 487 <= max(a_ok)
          and min(b_ok) <= 20 <= max(b_ok), f"{n_ok} grid points reproduce the record")
    print(f"    window: a {window['a_range']}, b {window['b_range']}, {n_ok} points")
    for k in RECORD:
        print(f"    {k:>3}: record {RECORD[k]}  old {mp.nstr(r_old[k], 8)}  ruled {mp.nstr(r_new[k], 8)}"
              f"  -> {round3(r_new[k])}")
    return {"LABEL": "WEIGHTS RECONSTRUCTED, NOT DERIVED. phi = (a, a, b); a = 0.0487 is the Breit-Wheeler "
                     "linear FIT (to 2 m_e); b = 0.02 is unsourced, reconstructed by matching the record. "
                     "Worked illustration of the gamma-gamma NF, not a prediction.",
            "weights": {"phi0": "0.0487", "phi1": "0.0487", "phi01": "0.02"},
            "record_rounded": RECORD,
            "old_form_nf_exact": nf_exact(old), "old_form_q0": nf_q0(old),
            "old_form_rounded_3dp": rounded_old, "old_form_matches_record": match,
            "ruled_form_nf_exact": nf_exact(new), "ruled_form_q0": nf_q0(new),
            "ruled_form_rounded_3dp": {k: round3(v) for k, v in r_new.items()},
            "delta_ruled_minus_old_q0": {k: fmt(v) for k, v in delta.items()},
            "record_pinning_window": window}


# ----------------------------------------------------------------- arm E
def section_e():
    print("E  corpus-derived eigenvalue pair gamma_+ gamma_- = V^3")
    gp, gm = gamma_ruled(0, 0, q * h), gamma_ruled(0, 0, -h / q)
    prod = mul(gp, gm)
    v3 = mul(mul(V, V), V)
    check("E1_gamma_plus_gamma_minus_equals_V3", lin((1, prod), (-1, v3)) == {})
    check("E2_no_e_minus_term", (0, 1, 0) not in prod)
    r = row(prod)
    for k, v in r.items():
        print(f"    {k:>3}: {mp.nstr(v, 10)}")
    return {"LABEL": "corpus-derived weights (borromean-two-photon-factorisation): gamma_+ = gamma(0,0,q h), "
                     "gamma_- = gamma(0,0,-q^-1 h). Product of two different photons, not a square; "
                     "comparison arm.",
            "nf_exact": nf_exact(prod), "nf_q0": nf_q0(prod),
            "rounded_3dp": {k: round3(v) for k, v in r.items()}}


# ----------------------------------------------------------------- nucleon nets
def section_n():
    print("N  nucleon nets 0.999 / 0.811 and the photon")
    # The nucleon NF is NF(B_3 * C(f1,f2;s0) C(f1,f3;s0) C(f2,f3;s1)) with flavours supplied as
    # input (prop:confinement-universality); no photon coefficient enters the confinement word.
    # This producer does not recompute the nets (no producer for them is on record); it records
    # that the gamma-gamma NF above is the only photon-dependent object in the block chain.
    return {"statement": "net(p) ~ 0.999, net(n) ~ 0.811 are photon-independent by construction "
                         "(prop:confinement-universality: the confinement word contains no photon "
                         "coefficient). Not recomputed here; no producer for the nets is on record.",
            "recomputed": False}


def main() -> int:
    res = {"S_symbolic": section_symbolic(), "W_reconstructed_weights": section_w(),
           "E_eigenvalue_pair": section_e(), "N_nucleon_nets": section_n()}
    wb = WitnessBuilder("four-term-pair-nucleon-table", engine="sympy+mpmath", output_dir=HERE)
    for n, ok, d in CHECKS:
        wb.add_assertion(n, computed="1" if ok else "0", expected="1", source=d or "exact Q(q)")
    wb.save({"q0Anchor": "proton", "q0AnchorReason": "qou_substrate.constants.q_at(70), package default",
             "q0Value": fmt(Q0),
             "block": "tbl:four-term-pair-nucleon-table1-data",
             "photon": "def:photon, gamma = 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^-1 (owner ruling 2026-11-18, "
                       "confirmed 2026-11-20, bean qou-99qc)",
             "description": "H_3(q) NF of gamma(phi) gamma(phi) for the pair-nucleon data table. Old (s0 s1) form "
                            "reproduces the record; ruled (s0 s1^-1) form restates it at the same reconstructed "
                            "weights (0.0487 = FIT to 2 m_e, Breit-Wheeler; 0.02 unsourced). Worked illustration, "
                            "not a prediction. Eigenvalue-pair arm at corpus-derived weights.",
             "results": res})
    ok = all(c for _, c, _ in CHECKS)
    print(f"{sum(c for _, c, _ in CHECKS)}/{len(CHECKS)} checks pass")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
