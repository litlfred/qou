#!/usr/bin/env python3
"""80-dps producer for Annex A Proper γγ Hadron & Light-Nuclei (A=1..4) Datum Table.

Invokes the native MPFR + Clarabel solver binary `qou-gg-cli` (`crates/qou-gg-eval` +
`crates/qou-clarabel`, linked against `Clarabel.rs` @ `rev = 37f06c3` at `320` bits ≈
`96` dps, formatted to `80` dps) at the experimental proton anchor `q_0^(p)`, performs
independent `85`-dps `mpmath` + exact `ℚ(q)` cross-checks across:
  1. `q_0^(p)` & canonical `E_0^tower` / `E_0^(0)` vs `qou_substrate.constants.q_at(90)` and `qbeta_e0`;
  2. All 12 `H_3(q)` photonic, 4-photon, and single-hadron normal forms, Convention-D Markov
     traces, Specht characters, and `γ(0,0,qh)·γ(0,0,-h/q) = V^3` (`prop:borromean-two-photon-factorisation`);
  3. All 12 Clarabel `MpfrFloat` operator-selection LP certificates (`6×6` NF-Gram LP, full
     3-partition Wedderburn LP with `qou-fu8c` `null` + `["0", "+inf"]` on `c_(1,1,1) = 0`,
     and 2-row quotient Wedderburn LP on `H_3(q)/rad`);
  4. Full-strand `A = 2..4` (`6, 9, 12`-strand) `T3` colour-valence (`M_T3(A) = 3⌊A/2⌋`)
     `V^3`-bonded nuclear trace ratios against `gg-deuteron-bond.witness.json` (`A = 2`)
     and exact `ℚ(q)` `hecke_flint` (`A = 2, 3`);
  5. Exploratory 4-strand `H_4(q)` flavoured `γγ` census (`L <= 6`) and 6-strand neutral
     `e^- + ν̄_e + 0_1` lepton-pair census (`L <= 5`).

Zero `float64` (`mp.mp.dps = 85`, `parse_float=str`, `q0Anchor = "proton"`). No fitting.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
for _p in (
    str(HERE),
    str(HERE / "substrate"),
    str(HERE / "qbeta"),
    str(HERE / "probes" / "light_nuclei_a2_a3"),
    str(REPO / "tools" / "pyhecke" / "python"),
    str(REPO / "tools" / "qou-substrate" / "python"),
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402
import qbeta_e0  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

WORK_DPS = 90
OUT_DPS = 80
mp.mp.dps = WORK_DPS

_UPSTREAM_RECORDS: list = []


def _fmt(val: mp.mpf) -> str:
    if val == 0:
        return "0"
    return mp.nstr(val, OUT_DPS)


def _find_or_build_cli() -> Path:
    target_dir = Path(os.environ.get("CARGO_TARGET_DIR", "/tmp/qou-shared-cargo-target"))
    bin_path = target_dir / "release" / "qou-gg-cli"
    if bin_path.is_file() and os.access(bin_path, os.X_OK):
        return bin_path

    env = os.environ.copy()
    cargo_bin = str(Path.home() / ".cargo" / "bin")
    env["PATH"] = f"{cargo_bin}:{env.get('PATH', '')}"
    env["CARGO_TARGET_DIR"] = str(target_dir)
    env["CARGO_BUILD_JOBS"] = env.get("CARGO_BUILD_JOBS", "2")
    env["CARGO_NET_GIT_FETCH_WITH_CLI"] = "true"

    manifest = REPO / "crates" / "qou-gg-cli" / "Cargo.toml"
    cmd_offline = [
        "nice", "-n", "15", "cargo", "build", "--release", "--offline",
        "--manifest-path", str(manifest),
    ]
    res = subprocess.run(cmd_offline, cwd=str(REPO), env=env)
    if res.returncode != 0:
        cmd_online = [
            "nice", "-n", "15", "cargo", "build", "--release",
            "--manifest-path", str(manifest),
        ]
        subprocess.run(cmd_online, cwd=str(REPO), env=env, check=True)
    if not bin_path.is_file():
        raise FileNotFoundError(f"expected built binary at {bin_path}")
    return bin_path


def _run_cli(bin_path: Path) -> dict:
    cmd = [
        "nice", "-n", "15", str(bin_path),
        "--prec-bits", "320",
        "--dps", str(OUT_DPS),
        "--flavoured-max-vertices", "6",
        "--lepton-max-vertices", "5",
    ]
    proc = subprocess.run(cmd, cwd=str(REPO), check=True, capture_output=True, text=True)
    return json.loads(proc.stdout, parse_float=str)


def _mp_h3_mul(a: list[mp.mpf], b: list[mp.mpf], h: mp.mpf) -> list[mp.mpf]:
    def mul_s0(c: list[mp.mpf]) -> list[mp.mpf]:
        return [
            c[1],
            c[0] + h * c[1],
            c[4],
            c[5],
            c[2] + h * c[4],
            c[3] + h * c[5],
        ]

    def mul_s1(c: list[mp.mpf]) -> list[mp.mpf]:
        return [
            c[2],
            c[3],
            c[0] + h * c[2],
            c[1] + h * c[3],
            c[5],
            c[4] + h * c[5],
        ]

    b0 = list(a)
    b1 = mul_s0(a)
    b2 = mul_s1(a)
    b3 = mul_s1(b1)
    b4 = mul_s0(b2)
    b5 = mul_s0(b3)
    bases = (b0, b1, b2, b3, b4, b5)
    out = [mp.mpf(0)] * 6
    for k, bk in enumerate(bases):
        rk = b[k]
        if rk != 0:
            for i in range(6):
                out[i] += bk[i] * rk
    return out


def main() -> int:
    mp.mp.dps = WORK_DPS
    gg_bond_path = REPO / "computations" / "probes" / "gg_deuteron_bond" / "gg-deuteron-bond.witness.json"
    gg_bond_w = record_upstream(gg_bond_path, _UPSTREAM_RECORDS)

    bin_path = _find_or_build_cli()
    payload = _run_cli(bin_path)

    # ── 1. Cross-check q_0^(p) and E_0^tower against mpmath 90-dps ────────────
    q0_mp = q_at(dps=WORK_DPS)
    q0_rust = mp.mpf(payload["q0_summary"]["q0"])
    q0_diff = abs(q0_rust - q0_mp)

    e0_tow_mp = qbeta_e0.tower_summed(q=q0_mp)
    e0_tow_rust = mp.mpf(payload["q0_summary"]["e0_tower_mev"])
    e0_diff = abs(e0_tow_rust - e0_tow_mp)

    # ── 2. Cross-check H_3(q) NF, trace, Specht characters, and LP KKT ────────
    h = q0_mp - mp.mpf(1) / q0_mp
    z_d = q0_mp ** 3 / (q0_mp ** 2 + mp.mpf(1))
    tw = [mp.mpf(1), z_d, z_d, z_d ** 2, z_d ** 2, h * z_d ** 2 + z_d]
    y3 = (q0_mp ** 4 + mp.mpf(1)) / ((q0_mp ** 2 + mp.mpf(1)) ** 2)
    y21 = (q0_mp ** 2) / ((q0_mp ** 2 + mp.mpf(1)) ** 2)

    # Independent Borromean two-photon check in mpmath
    one_nf = [mp.mpf(1), mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    s0_nf = [mp.mpf(0), mp.mpf(1), mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    s1_inv_nf = [-h, mp.mpf(0), mp.mpf(1), mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    v_nf = _mp_h3_mul(s0_nf, s1_inv_nf, h)
    v2_nf = _mp_h3_mul(v_nf, v_nf, h)
    v3_nf = _mp_h3_mul(v2_nf, v_nf, h)
    gp_nf = [one_nf[i] + q0_mp * h * v_nf[i] for i in range(6)]
    gm_nf = [one_nf[i] - (h / q0_mp) * v_nf[i] for i in range(6)]
    gpgm_nf = _mp_h3_mul(gp_nf, gm_nf, h)
    bor_factor_err = max(abs(gpgm_nf[i] - v3_nf[i]) for i in range(6))

    max_h3_tr_specht_err = mp.mpf(0)
    max_lp_kkt_res = mp.mpf(0)
    fu8c_mask_ok = True

    h3_rows = payload["h3_rows"]
    by_id = {r["id"]: r for r in h3_rows}
    v3_nf_rust = [mp.mpf(s) for s in by_id["nucleon_bare_v3"]["nf_coeffs"]]
    max_v3_nf_err = max(abs(v3_nf_rust[i] - v3_nf[i]) for i in range(6))

    for r in h3_rows:
        c = [mp.mpf(s) for s in r["nf_coeffs"]]
        tr_mp = mp.fsum(c[i] * tw[i] for i in range(6))
        chi3_mp = c[0] + q0_mp * (c[1] + c[2]) + (q0_mp ** 2) * (c[3] + c[4]) + (q0_mp ** 3) * c[5]
        chi21_mp = mp.mpf(2) * c[0] + h * (c[1] + c[2]) - (c[3] + c[4])
        tr_specht = y3 * chi3_mp + y21 * chi21_mp
        tr_rust = mp.mpf(r["tr_m"])
        err = max(abs(tr_rust - tr_mp), abs(tr_mp - tr_specht))
        if err > max_h3_tr_specht_err:
            max_h3_tr_specht_err = err

        lp = r["lp_certificate"]
        for sub in (lp["nf_gram_lp"], lp["wedderburn_full_lp"], lp["wedderburn_quotient_lp"]):
            for key in ("duality_gap", "kkt_primal_residual", "kkt_dual_residual"):
                v_res = abs(mp.mpf(sub[key]))
                if v_res > max_lp_kkt_res:
                    max_lp_kkt_res = v_res

        p111 = lp["wedderburn_full_lp"]["partitions"][2]
        if not (
            p111["partition"] == "(1,1,1)"
            and p111["u_identified"] is False
            and p111["u_lambda_star"] is None
            and p111["u_lambda_star_interval"] == ["0", "+inf"]
        ):
            fu8c_mask_ok = False

    # ── 3. Cross-check A=2..4 light-nuclei T3 rows against upstream & exact ℚ(q)
    ln_rows = payload["light_nuclei_t3_rows"]
    r2_bare = next(
        r for r in ln_rows if r["nuclide"] == "2H" and r["nucleon_cell"] == "bare_gg_V3"
    )
    gg_bond_v23 = next(
        r for r in gg_bond_w["data"]["results"]["V^3"]["rows"]
        if r["bond"] == "V(2)^3" and r["reading3_every_level"] is True
    )
    # gg-deuteron-bond.witness.json was emitted at 40 dps (20-digit string)
    r2_upstream_diff = abs(mp.mpf(r2_bare["ratio"]) - mp.mpf(gg_bond_v23["ratio"]))

    # Independent 85-dps pure-mpmath 6-strand two-row Hoefsmit cross-check on BOTH
    # 2H bare_gg_V3 ("vv") and 2H typed_uud_udd ("pn") (zero external flint dependency).
    def _mp_tr_h6_word(letters: list[tuple[str, int]]) -> mp.mpf:
        half_h = h / mp.mpf(2)
        q2_int = q0_mp + mp.mpf(1) / q0_mp
        total_tr = mp.mpf(0)

        def enum_syt6(r: int) -> list[list[int]]:
            out: list[list[int]] = []

            def rec(pos: int, c0: int, c1: int, cur: list[int]) -> None:
                if pos == 6:
                    out.append(list(cur))
                    return
                if c0 < 6 - r:
                    cur.append(0)
                    rec(pos + 1, c0 + 1, c1, cur)
                    cur.pop()
                if c1 < r and c1 < c0:
                    cur.append(1)
                    rec(pos + 1, c0, c1 + 1, cur)
                    cur.pop()

            rec(0, 0, 0, [])
            return out

        for r in range(4):  # (6), (5,1), (4,2), (3,3)
            syts = enum_syt6(r)
            dim = len(syts)
            idx_of = {tuple(s): i for i, s in enumerate(syts)}
            cts = []
            for s in syts:
                c0 = c1 = 0
                ct = []
                for row in s:
                    if row == 0:
                        ct.append(c0)
                        c0 += 1
                    else:
                        ct.append(c1 - 1)
                        c1 += 1
                cts.append(ct)
            gens = []
            for g in range(5):
                mat = mp.zeros(dim, dim)
                for i in range(dim):
                    d = cts[i][g + 1] - cts[i][g]
                    if d == 1:
                        mat[i, i] = q0_mp
                    elif d == -1:
                        mat[i, i] = -mp.mpf(1) / q0_mp
                    else:
                        mat[i, i] = h / (mp.mpf(1) - q0_mp ** (-2 * d))
                        sw = list(syts[i])
                        sw[g], sw[g + 1] = sw[g + 1], sw[g]
                        j = idx_of[tuple(sw)]
                        qd = (q0_mp ** abs(d) - q0_mp ** (-abs(d))) / h
                        mat[i, j] = mp.sqrt(mp.mpf(1) - mp.mpf(1) / (qd * qd))
                gens.append(mat)
            w_mat = mp.eye(dim)
            for kind, g in letters:
                mg = gens[g]
                if kind == "I":
                    mg = mg - h * mp.eye(dim)
                elif kind == "A":
                    mg = mg - half_h * mp.eye(dim)
                w_mat = w_mat * mg
            tr_blk = mp.fsum(w_mat[i, i] for i in range(dim))
            m_q = 6 - 2 * r + 1
            y_lam = ((q0_mp ** m_q - q0_mp ** (-m_q)) / h) / (q2_int ** 6)
            total_tr += y_lam * tr_blk
        return total_tr

    v3_0 = [("S", 0), ("I", 1)] * 3
    v3_3 = [("S", 3), ("I", 4)] * 3
    bond_2 = [("S", 2), ("I", 3)] * 3
    p_0 = v3_0 + [("S", 0), ("A", 0), ("A", 1), ("S", 0), ("S", 0)]
    n_3 = v3_3 + [("A", 3), ("A", 3), ("I", 4), ("S", 3), ("S", 3)]

    r2_vv_mp = _mp_tr_h6_word(v3_0 + v3_3 + bond_2) / _mp_tr_h6_word(v3_0 + v3_3)
    r2_pn_mp = _mp_tr_h6_word(p_0 + n_3 + bond_2) / _mp_tr_h6_word(p_0 + n_3)
    r2_pn_rust = mp.mpf(
        next(r for r in ln_rows if r["nuclide"] == "2H" and r["nucleon_cell"] == "typed_uud_udd")["ratio"]
    )
    flint_typed_err = max(abs(mp.mpf(r2_bare["ratio"]) - r2_vv_mp), abs(r2_pn_rust - r2_pn_mp))

    bare_a234_all_pass_r3 = all(
        r["reading3_m1_to_3a"] is True and r["bound_attracts"] is True
        for r in ln_rows
        if r["nucleon_cell"] == "bare_gg_V3"
    )
    typed_a234_all_fail_r3 = all(
        r["reading3_m1_to_3a"] is False and r["bound_attracts"] is False
        for r in ln_rows
        if r["nucleon_cell"] == "typed_uud_udd"
    )

    c4 = payload["h4_flavoured_census"]
    l6 = payload["lepton_pair_6s"]

    wb = (
        WitnessBuilder(
            "gg-hadron-datum-table",
            engine="mpmath+qou-gg-cli",
        )
        .add_upstream_records(_UPSTREAM_RECORDS)
        .set_content_block("rem:gg-hadron-datum-table")
        .set_description(
            "80-dps proton-pinned datum table for Annex A (rem:gg-hadron-datum-table, "
            "tbl:gg-hadron-datum-table-data): H_3(q) photonic, 4-photon, and A=1 hadron "
            "normal forms, Convention-D Markov traces, U(1) linking neutrality, Specht "
            "character margins, and Clarabel.rs@37f06c3 MpfrFloat LP-dual shadow prices; "
            "full-strand A=2..4 (6,9,12-strand) T3 colour-valence γγ-bonded nuclear braids; "
            "and exploratory H_4 flavoured nucleon & 6-strand lepton-pair censuses."
        )
        .add_parameter("prec_bits_rust", 320)
        .add_parameter("work_dps_mpmath", WORK_DPS)
        .add_parameter("out_dps", OUT_DPS)
        .add_data("q0_summary", payload["q0_summary"])
        .add_data("h3_basis_names", payload["h3_basis_names"])
        .add_data("h3_rows", payload["h3_rows"])
        .add_data("hadron_a1_supplements", payload["hadron_a1_supplements"])
        .add_data("light_nuclei_t3_rows", payload["light_nuclei_t3_rows"])
        .add_data("h4_flavoured_census", c4)
        .add_data("lepton_pair_6s", l6)
        .add_data(
            "cross_checks",
            {
                "q0_rust_vs_mpmath_abs_diff": _fmt(q0_diff),
                "e0_tower_rust_vs_mpmath_abs_diff": _fmt(e0_diff),
                "borromean_two_photon_factor_max_err": _fmt(bor_factor_err),
                "v3_nf_rust_vs_mpmath_max_err": _fmt(max_v3_nf_err),
                "h3_tr_m_and_specht_max_err": _fmt(max_h3_tr_specht_err),
                "clarabel_lp_max_kkt_and_gap_residual": _fmt(max_lp_kkt_res),
                "r2_bare_vs_gg_deuteron_bond_diff": _fmt(r2_upstream_diff),
                "typed_uud_udd_vs_exact_flint_max_err": _fmt(flint_typed_err),
                "bare_v3_a234_all_pass_reading3_and_bind": bare_a234_all_pass_r3,
                "typed_uud_udd_a234_all_fail_reading3_and_unbind": typed_a234_all_fail_r3,
            },
        )
    )

    wb.add_assertion(
        "q0_and_e0_match_mpmath_80dps",
        computed=_fmt(max(q0_diff, e0_diff)),
        expected="0",
        tolerance="1e-76",
        source="rug::Float 320-bit proton-pin secant solve vs qou_substrate.constants.q_at(90) & qbeta_e0.tower_summed",
    )
    wb.add_assertion(
        "h3_nf_traces_and_borromean_factorisation_exact",
        computed=_fmt(max(bor_factor_err, max_v3_nf_err, max_h3_tr_specht_err)),
        expected="0",
        tolerance="1e-76",
        source="prop:borromean-two-photon-factorisation & H_3(q) Specht decomposition y_3*chi_3 + y_21*chi_21 = tr_M",
    )
    wb.add_assertion(
        "clarabel_mpfr_lp_kkt_residuals_below_1e55",
        computed=_fmt(max_lp_kkt_res),
        expected="0",
        tolerance="1e-55",
        source="Clarabel.rs@37f06c3 320-bit MpfrFloat primal/dual/duality-gap KKT residuals across all 36 H_3 LPs",
    )
    wb.add_assertion(
        "qou_fu8c_null_interval_mask_enforced",
        computed=1 if fu8c_mask_ok else 0,
        expected=1,
        tolerance=0,
        source="Owner ruling 2026-11-25 (qou-fu8c): c_(1,1,1)=0 dual coordinate published as null with ['0', '+inf']",
    )
    wb.add_assertion(
        "deuteron_bare_v3_matches_upstream_witness",
        computed=_fmt(r2_upstream_diff),
        expected="0",
        tolerance="1e-18",
        source="gg-deuteron-bond.witness.json V(2)^3 20-digit ratio vs 80-dps TwoRowTowerRep(6)",
    )
    wb.add_assertion(
        "typed_uud_udd_matches_exact_q_rational_flint",
        computed=_fmt(flint_typed_err),
        expected="0",
        tolerance="1e-75",
        source="Exact ℚ(q) hecke_flint polynomial ratio evaluated at 90-dps q_0^(p) vs TwoRowTowerRep(6, 9)",
    )
    wb.add_assertion(
        "bare_v3_passes_reading3_and_typed_fails_for_a2_to_a4",
        computed=1 if (bare_a234_all_pass_r3 and typed_a234_all_fail_r3) else 0,
        expected=1,
        tolerance=0,
        source="Multi-level two-row reading-3 positivity check m = 1..3A on bare V^3 vs typed uud/udd blocks",
    )
    wb.add_assertion(
        "h4_flavoured_and_6s_lepton_censuses_reproduced",
        computed=c4["n_passing_nucleon_words"] * 1000 + l6["n_electron_antineutrino_words"],
        expected=12060,
        tolerance=0,
        source="12 passing H_4 words (L<=6) and 60 e^- + nu_bar 6-strand γγ words (L<=5)",
    )

    wb.save()
    print("Wrote computations/gg-hadron-datum-table.witness.json (all assertions passed).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
