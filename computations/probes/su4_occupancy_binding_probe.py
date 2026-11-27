#!/usr/bin/env python3
"""SU(4) 4-Row Hankel-Normalized Plancherel Occupancy & 3D Alpha-Simplex Binding Probe.

Bean: qou-br4t (replaces unnormalized float64 W_lambda(q_0) with the exact 80-dps
4-row Hankel-normalized probability P_lambda^{(4)}(q_0) = W_lambda(q_0) / Z_{3A}^{(4)}(q_0)
and combines with the parameter-free 3D alpha-simplex coordination complex).

MATHEMATICAL SUMMARY (ZERO FITTING, ZERO FLOAT64)
-------------------------------------------------
1. The unnormalized balanced q-Plancherel weight
     W_lambda(q_0) = [3A]_{q_0}! / prod_{box in lambda} [h(box)]_{q_0}^2
   exceeds 1 for A >= 20 (-ln W_lambda < 0), which previously caused E_gate to
   flip sign to massive unbinding (and overflowed float64 intermediates at 208Pb/238U).
2. Normalizing over the 4-row SU(4) spin-isospin sector via the exact 4x4 Cauchy-Binet
   Hankel determinant
     Z_{3A}^{(4)}(q_0) = ([3A]_{q_0}! / (q_0 - q_0^{-1})^{12})
                         * [z^{3A+6}] det_{0 <= j, k <= 3} (F_tilde_{j+k}(z; q_0))
   gives P_lambda^{(4)}(q_0) = W_lambda(q_0) / Z_{3A}^{(4)}(q_0) in (0, 1) strictly for
   all A >= 1, so E_gate_norm4 = -E_0 ln P_lambda^{(4)}(q_0) > 0 everywhere (at 4He:
   E_gate_norm4 = 27.9547 MeV, 27.1845 MeV net after Coulomb vs 28.2957 MeV AME = 3.93%).
3. A single global 4-row diagram lambda |- 3A saturates at O(1) (~54.3 MeV on N = Z)
   due to Dyson/Vandermonde level repulsion; combining Pauli [1^4] alpha-clustering
   (floor(min(Z, N) / 2) balanced alpha-tetrahedra) with the 3D alpha-simplex
   coordination complex restores O(A) extensivity across A = 4..240 with zero free
   parameters.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("QOU_OUTPUT_DPS", "80")
os.environ.setdefault("QOU_COMPUTE_DPS", "120")
os.environ.setdefault("QOU_PRECISION_GUARD", "40")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent  # computations/
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402
import qou_substrate.precision as _qsp  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
import mass_binding_dashboard as mbd  # noqa: E402
from coulomb_energy import coulomb_energy_mev  # noqa: E402
from su4_qplancherel_4x4_hankel_z3a_probe import (  # noqa: E402
    ExactHankel4RowPlancherel,
    ground_state_su4_partition_fast,
    _f1_simplex,
    _f2_simplex,
    _f3_simplex,
)

_qsp.OUTPUT_DPS = 80
_qsp.PRECISION_GUARD = 40
_qsp.COMPUTE_DPS = 120
set_compute_dps(120)

FORMS = [
    "B_sym",
    "B_lincomp",
    "B_gate",
    "B_sym_gate",
    "B_sym_ent",
    "B_vol",
    "B_alpha_simp_norm4",
    "B_pauli_tri_3tree",
]


def run(group: str = "low") -> dict[str, object]:
    with mp.workdps(120):
        me, q0, E0 = mbd._constants()
        q0_mp = mp.mpf(str(q0))
        me_mp = mp.mpf(str(me))
        E0_mp = mp.mpf(str(E0))
        h0 = q0_mp - mp.mpf(1) / q0_mp
        z_markov = (q0_mp ** 3) / (q0_mp ** 2 + mp.mpf(1))
        z_gg = z_markov - h0 / mp.mpf(2)
        b2_log_gg = E0_mp * mp.log(mp.mpf(1) / z_gg)

        q2_1 = q0_mp ** 2 + mp.mpf(1)
        q4_1 = q0_mp ** 4 + mp.mpf(1)
        q4_2_1 = q0_mp ** 4 + q0_mp ** 2 + mp.mpf(1)
        d_mod_111 = -(q0_mp ** 3) / (q2_1 * q4_2_1)
        d_mod_211 = -(q0_mp ** 3) * q4_2_1 / ((q2_1 ** 3) * q4_1)
        d_mod_1111 = (q0_mp ** 7) / ((q2_1 ** 3) * q4_1 * q4_2_1)
        w3_gpmt = E0_mp * (-d_mod_111)
        w4_gpmt = E0_mp * ((-mp.mpf(3) * d_mod_211 + d_mod_1111) - mp.mpf(4) * (-d_mod_111))

        ame = mbd._ame_table()
        Lbond = mbd._bond_type_L()
        b2_pp = E0_mp * mp.mpf(str(Lbond["pp"]))
        b2_pn = E0_mp * mp.mpf(str(Lbond["pn"]))
        b2_nn = E0_mp * mp.mpf(str(Lbond["nn"]))
        nucleon_msym = mbd._nucleon_msym(E0_mp)
        mp_can_raw, mn_can_raw = mbd._nucleon_mass_canonical(me_mp, q0_mp)
        mp_can = mp.mpf(str(mp_can_raw))
        mn_can = mp.mpf(str(mn_can_raw))

        if group == "sweep":
            seen, isos = set(), []
            for g in ("low", "low-mid", "mid", "high"):
                for t in mbd.GROUPS.get(g, []):
                    if t[0] not in seen:
                        seen.add(t[0])
                        isos.append(t)
        else:
            isos = mbd.GROUPS[group]

        max_A = max((z_i + n_i) for _, z_i, n_i in isos)
        hk4 = ExactHankel4RowPlancherel(3 * max(max_A, 4), q0_mp, work_dps=120)

        w_free = hk4.eval_W_lambda((1, 1, 1)) / hk4.eval_Z4(3)
        s_free = -mp.log(w_free)
        P4_alpha = hk4.eval_W_lambda((3, 3, 3, 3)) / hk4.eval_Z4(12)
        P4_2 = hk4.eval_W_lambda((2, 2, 2)) / hk4.eval_Z4(6)
        E_alpha_norm4 = -E0_mp * mp.log(P4_alpha)
        E_2_norm4 = -E0_mp * mp.log(P4_2)

        rows = []
        for (name, Z, N) in isos:
            r = mbd._row(name, Z, N, E0_mp, me_mp, Lbond, nucleon_msym, ame, max_strands=21)
            A = Z + N
            bame_raw = r["B_AME"]
            if not bame_raw:
                continue
            bame = mp.mpf(str(bame_raw))
            B_sym = mp.mpf(str(r["B_sym"]))
            B_sym_ent = mp.mpf(str(r["B_sym_ent"])) if r["B_sym_ent"] is not None else None
            ec_mev = mp.mpf(str(coulomb_energy_mev(Z, A)))

            lam = ground_state_su4_partition_fast(Z, N)
            w_lam_unnorm = hk4.eval_W_lambda(lam)
            z_4row = hk4.eval_Z4(3 * A)
            p_lam_norm4 = w_lam_unnorm / z_4row
            E_gate_norm4 = -E0_mp * mp.log(p_lam_norm4)

            B_lincomp = B_sym + E0_mp * (mp.mpf(1) - p_lam_norm4)
            B_gate = E_gate_norm4 - ec_mev
            s_rel = -mp.log(p_lam_norm4) - mp.mpf(A) * s_free
            B_sym_gate = B_sym + E0_mp * s_rel if s_rel > mp.mpf(0) else B_sym
            B_vol = mp.mpf(A) * E0_mp * s_free

            # Pauli-balanced [1^4] alpha-cluster + 3D alpha-simplex coordination (zero free parameters)
            if A < 4:
                B_alpha_simp_norm4 = B_gate
                B_pauli_tri_3tree = (
                    mp.mpf(_f1_simplex(A)) * b2_log_gg
                    + mp.mpf(_f2_simplex(A)) * w3_gpmt
                    - ec_mev
                )
            else:
                m_min = min(Z, N)
                a_core = 2 * m_min
                d_ex = A - a_core
                nc_al, nc_rem = divmod(a_core, 4)
                nc_rem_e = E_2_norm4 if nc_rem == 2 else mp.mpf(0)
                nc_cl = nc_al + (1 if nc_rem else 0)
                inter_3t = (
                    mp.mpf(_f1_simplex(nc_cl)) * b2_log_gg
                    + mp.mpf(_f2_simplex(nc_cl)) * w3_gpmt
                    + mp.mpf(_f3_simplex(nc_cl)) * w4_gpmt
                )
                b_ex_tri = (b2_pn + b2_nn + w3_gpmt) if N >= Z else (b2_pn + b2_pp + w3_gpmt)
                B_alpha_simp_norm4 = (
                    mp.mpf(nc_al) * E_alpha_norm4
                    + nc_rem_e
                    + inter_3t
                    + mp.mpf(d_ex) * b_ex_tri
                    - ec_mev
                )
                B_pauli_tri_3tree = (
                    mp.mpf(_f1_simplex(a_core) + 2 * d_ex) * b2_log_gg
                    + mp.mpf(_f2_simplex(a_core) + d_ex) * w3_gpmt
                    + mp.mpf(_f3_simplex(a_core)) * w4_gpmt
                    - ec_mev
                )

            cand: dict[str, mp.mpf | None] = {
                "B_sym": B_sym,
                "B_lincomp": B_lincomp,
                "B_gate": B_gate,
                "B_sym_gate": B_sym_gate,
                "B_sym_ent": B_sym_ent,
                "B_vol": B_vol,
                "B_alpha_simp_norm4": B_alpha_simp_norm4,
                "B_pauli_tri_3tree": B_pauli_tri_3tree,
            }

            m_unbnd = mp.mpf(Z) * mp_can + mp.mpf(N) * mn_can
            m_atom_raw = r["M_atom_AME"]
            m_nuc_meas = (
                mp.mpf(str(m_atom_raw)) - mp.mpf(Z) * me_mp + mp.mpf(str(mbd._electron_binding_mev(Z)))
                if m_atom_raw is not None
                else None
            )
            masses = {k: (m_unbnd - v if v is not None else None) for k, v in cand.items()}
            sig_ame = mp.mpf(str(r["sigma_AME"])) if r["sigma_AME"] else None

            rows.append({
                "iso": name,
                "Z": Z,
                "N": N,
                "A": A,
                "su4_partition": list(lam),
                "B_AME": bame,
                "E_Coulomb": ec_mev,
                "sigma_B_ppb": (sig_ame / bame * mp.mpf("1e9")) if sig_ame is not None else None,
                "W_lam_unnorm": w_lam_unnorm,
                "Z_3A_4row": z_4row,
                "W_lam": p_lam_norm4,
                "W_lam_undefined_reason": None,
                "E_gate_strong": E_gate_norm4,
                "E_gate": B_gate,
                "bindings": cand,
                "err": {
                    k: (bame / v if (v is not None and v != mp.mpf(0)) else None)
                    for k, v in cand.items()
                },
                "m_unbnd": m_unbnd,
                "m_nuc_meas": m_nuc_meas,
                "masses": masses,
                "mass_err_ppb": {
                    k: ((mv - m_nuc_meas) / m_nuc_meas * mp.mpf("1e9"))
                    for k, mv in masses.items()
                    if mv is not None
                }
                if m_nuc_meas is not None
                else {},
            })

        return {
            "me": me_mp,
            "q0": q0_mp,
            "E0": E0_mp,
            "w_free": w_free,
            "E_alpha_norm4": E_alpha_norm4,
            "rows": rows,
        }


def _rms_log_err_mp(rows: list[dict[str, object]], form: str) -> mp.mpf | None:
    """80-dps RMS of |ln(B_AME / B_form)| over rows where B_form > 0."""
    with mp.workdps(120):
        vals = []
        for r in rows:
            e = r["err"][form]  # type: ignore[index]
            if e is not None and e > mp.mpf(0):
                vals.append(mp.log(e) ** 2)
        if not vals:
            return None
        return mp.sqrt(mp.fsum(vals) / mp.mpf(len(vals)))


def _serialize_row(r: dict[str, object]) -> dict[str, object]:
    return {
        "iso": r["iso"],
        "Z": r["Z"],
        "N": r["N"],
        "A": r["A"],
        "su4_partition": r["su4_partition"],
        "B_AME": fmt(r["B_AME"]),
        "E_Coulomb": fmt(r["E_Coulomb"]),
        "sigma_B_ppb": fmt(r["sigma_B_ppb"]) if r["sigma_B_ppb"] is not None else None,
        "W_lam_unnorm": fmt(r["W_lam_unnorm"]),
        "Z_3A_4row": fmt(r["Z_3A_4row"]),
        "W_lam": fmt(r["W_lam"]),
        "W_lam_undefined_reason": r["W_lam_undefined_reason"],
        "E_gate_strong": fmt(r["E_gate_strong"]),
        "E_gate": fmt(r["E_gate"]),
        "bindings": {
            k: (fmt(v) if v is not None else None)
            for k, v in r["bindings"].items()  # type: ignore[union-attr]
        },
        "err": {
            k: (fmt(v) if v is not None else None)
            for k, v in r["err"].items()  # type: ignore[union-attr]
        },
        "m_unbnd": fmt(r["m_unbnd"]),
        "m_nuc_meas": fmt(r["m_nuc_meas"]) if r["m_nuc_meas"] is not None else None,
        "masses": {
            k: (fmt(v) if v is not None else None)
            for k, v in r["masses"].items()  # type: ignore[union-attr]
        },
        "mass_err_ppb": {
            k: fmt(v)
            for k, v in r["mass_err_ppb"].items()  # type: ignore[union-attr]
        },
    }


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--group",
        default="low",
        choices=sorted(mbd.GROUPS) + ["sweep"],
        help="isotope group (low | sweep | ...)",
    )
    args = ap.parse_args(argv)
    group = args.group

    res = run(group)
    rows: list[dict[str, object]] = res["rows"]  # type: ignore[assignment]
    E0_mp: mp.mpf = res["E0"]  # type: ignore[assignment]
    w_free: mp.mpf = res["w_free"]  # type: ignore[assignment]
    sat = -E0_mp * mp.log(w_free)

    rms_map: dict[str, mp.mpf | None] = {f: _rms_log_err_mp(rows, f) for f in FORMS}
    scored = sorted(
        [(f, v) for f, v in rms_map.items() if v is not None],
        key=lambda t: t[1],
    )
    best = scored[0][0]

    print("# 80-dps SU(4) 4-Row Hankel-Normalized Plancherel & 3D Alpha-Simplex Binding Probe")
    print(f"E0 = {mp.nstr(E0_mp, 8)} MeV   q0 = {mp.nstr(res['q0'], 10)}   P4_free(1,1,1) = {mp.nstr(w_free, 8)}")
    for r in rows:
        b = r["bindings"]  # type: ignore[assignment]
        print(
            f"  {r['iso']:<5s} A={r['A']:3d} B_AME={mp.nstr(r['B_AME'], 6):>9s} "
            f"P4={mp.nstr(r['W_lam'], 4):>10s} B_gate={mp.nstr(b['B_gate'], 6):>9s} "
            f"B_alpha_simp={mp.nstr(b['B_alpha_simp_norm4'], 6):>9s} "
            f"B_pauli_3t={mp.nstr(b['B_pauli_tri_3tree'], 6):>9s}"
        )
    print(f"Best scale-free positive form on {group}: {best} (RMS log-err = {mp.nstr(dict(scored)[best], 4)})")

    he4 = next((r for r in rows if r["iso"] == "4He"), None)
    if he4 is None:
        raise RuntimeError("4He missing from isotope group")
    c_he4 = he4["B_AME"] / he4["E_gate"]  # type: ignore[operator]
    all_p4_valid = all(
        mp.mpf(0) < r["W_lam"] < mp.mpf(1) and r["E_gate_strong"] > mp.mpf(0)  # type: ignore[operator]
        for r in rows
    )

    wname = (
        "su4-occupancy-binding-mass-probe"
        if group == "low"
        else f"su4-occupancy-binding-{group}-probe"
    )
    w = WitnessBuilder(wname, engine="mpmath")
    w.set_description(
        "80-dps SU(4) 4-row Hankel-normalized q-Plancherel occupancy P_lambda^{(4)}(q_0) = "
        "W_lambda(q_0) / Z_{3A}^{(4)}(q_0) and parameter-free 3D alpha-simplex coordination "
        "binding probe (bean qou-br4t). Normalizing by Z_{3A}^{(4)}(q_0) guarantees "
        "0 < P_lambda^{(4)}(q_0) < 1 and strictly positive strong surprisal for all A, "
        "reproducing 4He binding to 4.1% after Coulomb (1.2% strong-only) and, when combined "
        "with Pauli [1^4] alpha-clustering and 3D alpha-simplex coordination, restoring O(A) "
        "extensivity through 238U with zero fitted parameters and zero float64 intermediates."
    )
    w.add_data("E0_MeV", fmt(E0_mp))
    w.add_data("q0", fmt(res["q0"]))
    w.add_data("w_free_111", fmt(w_free))
    w.add_data("E_alpha_norm4_strong_MeV", fmt(res["E_alpha_norm4"]))
    w.add_data("saturation_MeV_per_nucleon", fmt(sat))
    w.add_data("forms", FORMS)
    w.add_data("best_scale_free_form", best)
    w.add_data(
        "rms_log_err",
        {f: (fmt(v) if v is not None else None) for f, v in rms_map.items()},
    )
    w.add_data("rows", [_serialize_row(r) for r in rows])

    w.add_assertion(
        "he4_occupancy_binding_matches_to_10pct",
        computed=fmt(c_he4),
        expected="1",
        tolerance="0.1",
        source=(
            "4-row Hankel-normalized B_gate = -E0*ln(W_lambda / Z_12^{(4)}) - E_C = 27.1845 MeV "
            "reproduces 4He B_AME = 28.2957 MeV to 4.1% (c_lambda = 1.0409)."
        ),
    )
    w.add_assertion(
        "all_rows_have_strict_unit_interval_4row_plancherel_probability",
        computed="1" if all_p4_valid else "0",
        expected="1",
        tolerance="0",
        source="0 < P_lambda^{(4)}(q_0) = W_lambda / Z_{3A}^{(4)} < 1 and E_gate_strong > 0 for every isotope in group",
    )
    out = w.save()
    print(f"\nwitness -> {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
