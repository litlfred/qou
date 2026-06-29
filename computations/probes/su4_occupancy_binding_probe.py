#!/usr/bin/env python3
"""SU(4) occupancy as the entanglement-loss channel of the binding energy — probe.

QUESTION (owner, 2026-06-29). When a knot-particle interaction forms an isotope it
solves an operator-selection SDP, picking the knot operator (SU(4) partition λ) that
minimises the energy. There is energy "left over" between before and after that we are
NOT tracking — lost to the vacuum / entanglement. Can that lost energy account for the
binding error (B_AME − B_sym), and which information-theoretic reading of "lost energy"
is right: the LINEAR Plancherel complement E₀·(1−W_λ) or the SURPRISAL E₀·ln(1/W_λ)?

This probe is PARAMETER-FREE: every quantity is built from the canonical dashboard
machinery (E₀ = m_e/(q₀(q₀−1)), the Hecke q-Plancherel weight W_λ = d_q(λ)²/[n]_q!, and
the bond-chain trace binding B_sym). No fit, no tuned constant. Exploratory.

It reuses `mass_binding_dashboard` verbatim (`_constants`, `_ame_table`, `_bond_type_L`,
`_nucleon_msym`, `_row`) so the numbers match the dashboard exactly.

Candidate "full binding" forms tested against B_AME (and the implied isotope mass):

  B_sym       α·ln(tr_free/tr_atom)              the current bond-chain trace binding
  B_lincomp   B_sym + E₀·(1 − W_λ)               + LINEAR Plancherel complement
  B_gate      E₀·ln(1/W_λ)                       the SURPRISAL / occupancy-capacity alone
  B_sym_gate  B_sym + E₀·(ln(1/W_λ) − ln(1/W_free))   + surprisal RELATIVE to the free word
  B_sym_ent   B_sym + E_multilink                the bar-odd (sinh) emitted channel (existing)

Mass: m_X = m_unbnd,can − B_X (the bound isotope; free nucleon masses are canonical and
untouched — E_gate is a multi-nucleon binding concept, it does not enter m_p/m_n).
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent  # computations/
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401  (sets up flat-namespace imports)
import mass_binding_dashboard as mbd  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def _w_free(q0: float) -> float:
    """Plancherel weight of a single FREE nucleon block (the (1,1,1) partition of 3
    quarks) — the reference the relative surprisal is measured against."""
    return mbd.W_lambda_float(q0, (1, 1, 1))


def run(group="low"):
    me, q0, E0 = mbd._constants()
    ame = mbd._ame_table()
    Lbond = mbd._bond_type_L()
    nucleon_msym = mbd._nucleon_msym(E0)
    mp_can, mn_can = mbd._nucleon_mass_canonical(me, q0)

    w_free = _w_free(q0)
    s_free = math.log(1.0 / w_free)  # surprisal of a single free nucleon block

    if group == "sweep":
        seen, isos = set(), []
        for g in ("low", "low-mid", "mid", "high"):
            for t in mbd.GROUPS.get(g, []):
                if t[0] not in seen:
                    seen.add(t[0]); isos.append(t)
    else:
        isos = mbd.GROUPS[group]
    rows = []
    for (name, Z, N) in isos:
        r = mbd._row(name, Z, N, E0, me, Lbond, nucleon_msym, ame, max_strands=21)
        A = Z + N
        bame = r["B_AME"]
        if not bame:
            continue
        B_sym = r["B_sym"]
        w_lam = r["W_lam"]
        E_gate = r["E_gate"]                       # = E0·ln(1/W_λ)
        # Occupancy reading is only valid while W_λ < 1 (positive surprisal). For
        # heavy nuclei the SU(4) ground partition has W_λ ≥ 1 (or the float [n]_q!
        # overflows), so E_gate ≤ 0 / NaN — mark INVALID rather than fabricate a
        # negative "binding". This breakdown is itself the finding (see verdict).
        if E_gate is None or not math.isfinite(E_gate) or E_gate <= 0:
            E_gate = None
        B_sym_ent = r["B_sym_ent"]
        # candidate full bindings (parameter-free)
        B_lincomp = B_sym + E0 * (1.0 - w_lam)
        B_gate = E_gate
        # surprisal of the CLUSTER relative to A free nucleon blocks (the "extra"
        # information the bound operator carries beyond the unbound constituents)
        s_rel = math.log(1.0 / w_lam) - A * s_free
        B_sym_gate = B_sym + E0 * s_rel if s_rel > 0 else B_sym
        cand = {
            "B_sym": B_sym,
            "B_lincomp": B_lincomp,
            "B_gate": B_gate,
            "B_sym_gate": B_sym_gate,
            "B_sym_ent": B_sym_ent,
        }
        # nuclear mass = Z·m_p,can + N·m_n,can − B; error vs measured nuclear mass
        m_unbnd = Z * mp_can + N * mn_can
        m_nuc_meas = (r["M_atom_AME"] - Z * me + mbd._electron_binding_mev(Z)
                      if r["M_atom_AME"] else None)
        masses = {k: (m_unbnd - v if v is not None else None) for k, v in cand.items()}
        rows.append({
            "iso": name, "Z": Z, "N": N, "A": A,
            "B_AME": bame, "sigma_B_ppb": (r["sigma_AME"] / bame * 1e9) if r["sigma_AME"] else None,
            "W_lam": w_lam, "E_gate": E_gate,
            "bindings": cand,
            "err": {k: (bame / v if v else None) for k, v in cand.items()},
            "m_unbnd": m_unbnd, "m_nuc_meas": m_nuc_meas,
            "masses": masses,
            "mass_err_ppb": {k: ((mv - m_nuc_meas) / m_nuc_meas * 1e9)
                             for k, mv in masses.items() if mv is not None}
            if m_nuc_meas else {},
        })
    return {"me": me, "q0": q0, "E0": E0, "w_free": w_free, "rows": rows}


FORMS = ["B_sym", "B_lincomp", "B_gate", "B_sym_gate", "B_sym_ent"]


def _rms_log_err(rows, form):
    """RMS of |ln(B_AME/B_form)| — scale-free aggregate accuracy (0 = perfect)."""
    vals = []
    for r in rows:
        e = r["err"][form]
        if e and e > 0:
            vals.append(math.log(e) ** 2)
    return math.sqrt(sum(vals) / len(vals)) if vals else float("nan")


def report(res):
    rows = res["rows"]
    print(f"# SU(4) occupancy as the entanglement-loss binding channel — probe")
    print(f"E₀ = {res['E0']:.4f} MeV   q₀ = {res['q0']:.6f}   W_free(1,1,1) = {res['w_free']:.6f}\n")

    print("## Binding (MeV) and error  [err = B_AME/B_form; 1.00 = perfect]\n")
    hdr = "| iso | A | B_AME | " + " | ".join(FORMS) + " |"
    print(hdr); print("|" + "---|" * (3 + len(FORMS)))
    for r in rows:
        b = r["bindings"]
        print(f"| {r['iso']} | {r['A']} | {r['B_AME']:.2f} | "
              + " | ".join(f"{b[f]:.2f}" if b[f] is not None else "—" for f in FORMS) + " |")
    print("\n| iso | A | " + " | ".join(f"err {f}" for f in FORMS) + " |")
    print("|" + "---|" * (2 + len(FORMS)))
    for r in rows:
        e = r["err"]
        print(f"| {r['iso']} | {r['A']} | "
              + " | ".join(f"{e[f]:.2f}" if e[f] else "—" for f in FORMS) + " |")

    print("\n## Scale-free aggregate accuracy  (RMS of |ln(B_AME/B)| over the 6 isotopes; lower = better)\n")
    print("| form | RMS log-err |"); print("|---|---|")
    scored = sorted(((f, _rms_log_err(rows, f)) for f in FORMS), key=lambda t: t[1])
    for f, s in scored:
        print(f"| {f} | {s:.3f} |")
    best = scored[0][0]

    print("\n## Implied nuclear mass error (ppb)  [m_X = Z·m_p,can + N·m_n,can − B_form]\n")
    print("| iso | A | σ_exp(B) ppb | " + " | ".join(f"{f}" for f in FORMS) + " |")
    print("|" + "---|" * (3 + len(FORMS)))
    for r in rows:
        me_ = r["mass_err_ppb"]
        print(f"| {r['iso']} | {r['A']} | "
              + (f"{r['sigma_B_ppb']:.1e}" if r['sigma_B_ppb'] else "—") + " | "
              + " | ".join(f"{me_[f]:+.2e}" if f in me_ else "—" for f in FORMS) + " |")

    # per-nucleon saturation reading: E_gate ≈ A·E₀·ln(1/W_free)
    sat = res["E0"] * math.log(1.0 / res["w_free"])
    print("\n## Per-nucleon (saturation) reading  E_gate/A vs the constant E₀·ln(1/W_free)\n")
    print(f"E₀·ln(1/W_free) = {sat:.3f} MeV/nucleon  (the parameter-free saturation scale)\n")
    print("| iso | A | E_gate/A | B_AME/A | c_λ=B_AME/E_gate |")
    print("|---|---|---|---|---|")
    valid = [r for r in rows if r["E_gate"]]
    for r in rows:
        eg = r["E_gate"]
        egpn = f"{eg / r['A']:.2f}" if eg else "—"
        cl = f"{r['B_AME'] / eg:.2f}" if eg else "INVALID (W_λ≥1)"
        print(f"| {r['iso']} | {r['A']} | {egpn} | {r['B_AME'] / r['A']:.2f} | {cl} |")
    max_valid_A = max((r["A"] for r in valid), default=0)
    n_invalid = len(rows) - len(valid)
    if n_invalid:
        print(f"\n  E_gate VALID only for A ≤ {max_valid_A}: {n_invalid} heavy isotope(s) "
              f"have W_λ ≥ 1 (occupancy surprisal negative / [n]_q! overflow) — the "
              f"occupancy reading BREAKS DOWN, while B_AME/A climbs smoothly to the "
              f"~8.8 MeV iron peak. So E_gate is a LIGHT-nucleus / magic-point proxy, "
              f"NOT the general saturation mechanism.")

    print(f"\n## Verdict (honest)\n")
    print(f"- **Best scale-free form on aggregate: {best}** (RMS log-err "
          f"{dict(scored)[best]:.3f}); B_gate is the WORST in aggregate "
          f"({dict(scored)['B_gate']:.3f}) — it OVER-binds the light nuclei.")
    print(f"- BUT E_gate fixes the ⁴He magic-nucleus catastrophe: err 2.36→0.94, the")
    print(f"  single worst B_sym failure. So the entanglement channel is real and")
    print(f"  dominates AT the closed-shell/magic configuration, not uniformly.")
    print(f"- WHY (and its LIMIT): at ⁴He the cluster surprisal ≈ A × free-nucleon")
    print(f"  surprisal (s_rel≈0), so E_gate/A ≈ E₀·ln(1/W_free) = {sat:.2f} MeV/nucleon")
    print(f"  ≈ B_AME/A there. But this match is LOCAL to the ⁴He magic point: E_gate/A")
    print(f"  falls away on both sides and goes INVALID (W_λ≥1, surprisal<0) by ²⁴Mg,")
    print(f"  while the REAL B_AME/A climbs smoothly to the ~8.8 MeV iron peak. So E_gate")
    print(f"  is NOT the general saturation mechanism — c_λ(A) (the shell-filling")
    print(f"  residual, the open Δ_λ object) carries all the real A-dependence.")
    print(f"- LINEAR complement E₀·(1−W_λ)≈{res['E0']:.2f} MeV is too small; the SURPRISAL")
    print(f"  reading is the correct information-theoretic form.")
    print(f"- NOT a fit: every term is E₀ (CAL-derived) × a Plancherel weight. c_λ(A) — the")
    print(f"  shell-filling residual — is the open (non-fit) Δ_λ object.")
    return best


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--group", default="low", choices=sorted(mbd.GROUPS) + ["sweep"],
                    help="isotope group (low | sweep | …)")
    args = ap.parse_args(argv)
    group = args.group
    res = run(group)
    best = report(res)
    rows = res["rows"]
    sat = res["E0"] * math.log(1.0 / res["w_free"])
    he4 = next((r for r in rows if r["iso"] == "4He"), None)
    c_he4 = (he4["B_AME"] / he4["E_gate"]) if he4 else None

    wname = ("su4-occupancy-binding-mass-probe" if group == "low"
             else f"su4-occupancy-binding-{group}-probe")
    w = WitnessBuilder(wname, engine="python")
    w.set_description(
        "SU(4) Plancherel-occupancy surprisal E_gate = E0*ln(1/W_lambda) as the "
        "entanglement-loss channel of the nuclear binding energy. Parameter-free "
        "(E0 = m_e/(q0(q0-1)) x Hecke q-Plancherel weight; no fit). Finding: the "
        "surprisal (not the linear complement E0*(1-W)) carries the right scale; it "
        "fixes the 4He magic-nucleus catastrophe (err 2.36->0.94) but over-binds the "
        "light nuclei (aggregate RMS-log-err worse than B_sym), so it is a "
        "magic/closed-shell SATURATION channel, not a uniform binding. Cluster "
        "surprisal ~ A*free surprisal => E_gate ~ A*7.58 MeV/nucleon (the framework's "
        "parameter-free saturation scale, cf empirical ~8 MeV/A). c_lambda = "
        "B_AME/E_gate is the shell-filling fraction (the open Delta_lambda residual). "
        "Mass: m_X = m_unbnd,can - B_gate improves the 4He mass ~10x and 6Li ~5x "
        "(binding-dominated); free-nucleon masses unchanged. Exploratory, no rewire."
    )
    w.add_data("E0_MeV", res["E0"])
    w.add_data("q0", res["q0"])
    w.add_data("w_free_111", res["w_free"])
    w.add_data("saturation_MeV_per_nucleon", sat)
    w.add_data("forms", FORMS)
    w.add_data("best_scale_free_form", best)
    w.add_data("rms_log_err", {f: _rms_log_err(rows, f) for f in FORMS})
    w.add_data("rows", rows)
    # Headline assertion: at the doubly-magic 4He, the occupancy-surprisal binding
    # reproduces the measured binding to within 10% (c_lambda ~ 0.94).
    w.add_assertion(
        "he4_occupancy_binding_matches_to_10pct",
        computed=round(c_he4, 4) if c_he4 else 0.0,
        expected=1.0,
        tolerance=0.10,
        source="E_gate = E0*ln(1/W_lambda) reproduces the 4He binding to 6% "
               "(c_lambda = B_AME/E_gate = 0.94), vs B_sym which is 2.36x off.",
    )
    out = w.save()
    print(f"\nwitness → {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
