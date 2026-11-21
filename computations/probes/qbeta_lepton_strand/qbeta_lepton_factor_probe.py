#!/usr/bin/env python3
"""qbeta_lepton_factor_probe — how a disjoint electron enters the ruled Q_β functional.

Issue #8833 (owner card 2026-11-21: "Derive the lepton factor rule"). Lean first:
QOU/QBeta/ElectronHalfTwistBlock.lean (sector_trace_halfTwist, sector_sum_eq_markov_zD).

D1 (ruled 2026-11-20): ε_p = q·tr_{W_p}(X)/[2]³, ε_n = q⁻¹·tr_{W_n}(X)/[2]³ (the quantum
trace Tr(K^{⊗3}·)/[2]³ on the two nucleon weight sectors), ε_flavour = ε_n − ε_p.

Checks (exact sympy over Q(q), Jimbo braiding on (C²)^{⊗3})
  F1  tr_{L_b}(Δ) = q³ on every electron weight sector b = 0..3 (Δ = σ₀σ₁σ₀).
  F2  Σ_b q^{3−2b}·q³/[2]³ = q³(q⁴+1)/(q²+1)²: the full electron quantum trace is its
      convention-D Markov value.
  F3  for the scored base V³, ε_n = ε_p / q² exactly.
  F4  the candidate table (factor f on the n side or the p side, f = Markov value or a single
      sector q^{6−2b}/[2]³) spans the needed value, so choosing among them by Q_β would be
      a fit. Reported; NONE is selected.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

import qbeta_e0  # noqa: E402
from codata_2022_source import Q_BETA_MEV_AME  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = 60
mp.mp.dps = DPS
_FS = _ROOT / "computations/probes/qbeta_flavour_weight_split/qbeta_flavour_weight_split_probe.py"
_spec = importlib.util.spec_from_file_location("_flavour_split", _FS)
fs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fs)
q, h, D2 = fs.q, fs.h, fs.D2
Q0 = sp.Rational(Q_50_DIGIT_STR)

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}\n")


def mpv(e) -> mp.mpf:
    return mp.mpf(str(sp.N(sp.sympify(e).subs(q, Q0), DPS + 5)))


R2 = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
S0 = sp.kronecker_product(R2, sp.eye(2))
S1 = sp.kronecker_product(sp.eye(2), R2)


def main() -> int:
    Delta = S0 * S1 * S0
    tr_b = []
    for b in range(4):
        idx = [i for i in range(8) if bin(i).count("1") == b]
        tr_b.append(sp.simplify(Delta.extract(idx, idx).trace()))
    check("F1_every_electron_sector_has_trace_q_cubed",
          all(sp.simplify(t - q ** 3) == 0 for t in tr_b),
          f"tr_(L_b)(Delta) for b = 0..3: {tr_b}. The V_(2,1) copies are traceless "
          "(Lean trace_halfTwist), so each sector carries only the V_(3) line q^3.")

    total = sum(q ** (3 - 2 * b) * tr_b[b] for b in range(4)) / D2 ** 3
    markov = q ** 3 * (q ** 4 + 1) / (q ** 2 + 1) ** 2
    check("F2_sector_sum_is_the_convention_D_markov_value",
          sp.simplify(total - markov) == 0,
          f"sum_b q^(3-2b) tr_(L_b)(Delta)/[2]^3 = {sp.factor(total)} = z_D(h z_D + 1) "
          f"(Lean sector_sum_eq_markov_zD) = {mp.nstr(mpv(markov), 15)} at q0.")

    Mp = (fs.A1 * fs.A2.inv()) ** 3
    Mn = (fs.B1 * fs.B2.inv()) ** 3
    ep = sp.simplify(q * Mp.trace() / D2 ** 3)
    en = sp.simplify(Mn.trace() / q / D2 ** 3)
    check("F3_eps_n_is_eps_p_over_q_squared", sp.simplify(en - ep / q ** 2) == 0,
          f"eps_p(V^3) = {sp.factor(ep)}; eps_n = eps_p / q^2 exactly. At q0 eps_p = "
          f"{mp.nstr(mpv(ep), 15)}, eps_n = {mp.nstr(mpv(en), 15)}: the scored difference "
          "is a 19 % cancellation, so a factor on one side only moves Q_beta a lot.")

    E0 = mp.mpf(qbeta_e0.canonical())
    P, N = mpv(ep), mpv(en)
    QB = mp.mpf(str(Q_BETA_MEV_AME))
    cands = [("Markov (all sectors)", mpv(markov))] + \
        [(f"sector b={b}", mpv(q ** (6 - 2 * b) / D2 ** 3)) for b in range(4)]
    rows, vals = [], []
    print("  factor              f          side   Q_beta (MeV)    vs CODATA")
    for nm, f in cands:
        for side in ("p (final state)", "n (initial state)"):
            val = (N - f * P) if side.startswith("p") else (f * N - P)
            Qx = abs(val) * E0
            vals.append(Qx)
            pct = (Qx / QB - 1) * 100
            rows.append({"factor": nm, "f": mp.nstr(f, 20), "side": side,
                         "Q_beta_MeV": mp.nstr(Qx, 20), "vs_codata_pct": mp.nstr(pct, 8)})
            print(f"  {nm:<19} {mp.nstr(f, 8):>10}  {side[0]}    {mp.nstr(Qx, 10):>12}   "
                  f"{mp.nstr(pct, 5):>8} %")
    print()
    spans = min(vals) < QB < max(vals)
    check("F4_candidates_span_the_target_so_none_is_selected", spans,
          f"the {len(rows)} candidates run from {mp.nstr(min(vals), 6)} to "
          f"{mp.nstr(max(vals), 6)} MeV and bracket the measured value, so picking one by its "
          "Q_beta would be selection against the target. Which side the electron sits on, and "
          "which sector (premise L, #8673), are not derived here. None is selected.")

    # F5: the q -> 1 order. The scored difference eps_n - eps_p = eps_p (q^-2 - 1) is O(h);
    # a factor f on one side leaves eps_p(1)(1 - f(1)), which is O(1) unless f(1) = 1.
    base1 = sp.limit(en - ep, q, 1)
    ep1 = sp.limit(ep, q, 1)
    f1 = {nm: sp.limit(fx, q, 1) for nm, fx in
          [("Markov", markov)] + [(f"b={b}", q ** (6 - 2 * b) / D2 ** 3) for b in range(4)]}
    one_sided = {nm: ep1 * (1 - v) for nm, v in f1.items()}
    check("F5_one_sided_factor_survives_q_to_1",
          base1 == 0 and all(v != 0 for v in one_sided.values()),
          f"at q -> 1: eps_n - eps_p -> {base1} (the scored cell is O(h)); eps_p -> {ep1}; "
          f"f(1) = {f1}; so eps_p(1)(1 - f(1)) = {one_sided}, all nonzero. A one-sided lepton "
          "factor changes the q -> 1 order of the cell from O(h) to O(1). A factor shared by "
          "both sides (f on n and p) cannot: it multiplies an O(h) quantity.")

    # F6: the O(h) corrections of each lepton factor (the eigenphase thread's half of the
    # split with #8868, which owns the q = 1 coefficient). Exact series in h = q - 1/q.
    hh = sp.Symbol("hh", positive=True)
    qh = (hh + sp.sqrt(hh ** 2 + 4)) / 2
    hseries, ratio_q0 = {}, {}
    for nm, fx in [("Markov", markov)] + [(f"b={b}", q ** (6 - 2 * b) / D2 ** 3)
                                           for b in range(4)]:
        ser = sp.series(sp.simplify(fx.subs(q, qh)), hh, 0, 4).removeO()
        hseries[nm] = str(sp.expand(ser))
        ratio_q0[nm] = mp.nstr(mpv(fx) / mp.mpf(str(f1[nm])), 20)
    ok6 = sp.expand(sp.series(sp.simplify(markov.subs(q, qh)), hh, 0, 2).removeO()) == \
        sp.Rational(1, 2) + sp.Rational(3, 4) * hh
    check("F6_lepton_factor_O_h_corrections", ok6,
          f"exact series in h to O(h^3): {hseries}. Ratio f(q0)/f(1) (the size of the O(h) "
          f"tail at the proton pin): {ratio_q0}. The b=3 sector has no O(h) term. These are "
          "kept regardless of size (owner 2026-11-21); which one applies waits on the q = 1 "
          "coefficient of the interaction (#8868).")

    allp = all(ok for _, ok, _ in RESULTS)
    print(f"  {sum(ok for _, ok, _ in RESULTS)}/{len(RESULTS)} checks passed")
    wb = WitnessBuilder("qbeta-lepton-factor", engine="mpmath")
    for nm, ok, det in RESULTS:
        wb.add_assertion(nm, computed="PASS" if ok else "FAIL", expected="PASS",
                         tolerance="exact", source=det)
    wb.save({
        "description": ("Disjoint electron Delta = s0 s1 s0 under the ruled D1 quantum-trace "
                        "functional: per-sector factor, full-trace factor, and the candidate "
                        "table. Nothing selected or scored."),
        "beans": ["qou-cds1", "qou-pdix", "qou-99qc"],
        "q0Anchor": "proton",
        "q0Value": Q_50_DIGIT_STR,
        "lean": "QOU/QBeta/ElectronHalfTwistBlock.lean",
        "eps_p_V3": str(sp.factor(ep)),
        "eps_n_V3": str(sp.factor(en)),
        "candidates_not_selected": rows,
        "q_to_1": {"base": str(base1), "eps_p": str(ep1),
                   "f": {k: str(v) for k, v in f1.items()},
                   "one_sided_p": {k: str(v) for k, v in one_sided.items()}},
        "h_series": hseries,
        "ratio_f_q0_over_f_1": ratio_q0,
        "scope": "(a): disjoint electron only; linked words are in qbeta-lepton-strand.",
    })
    return 0 if allp else 1


if __name__ == "__main__":
    raise SystemExit(main())
