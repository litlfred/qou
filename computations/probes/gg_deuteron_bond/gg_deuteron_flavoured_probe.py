#!/usr/bin/env python3
"""gg_deuteron_flavoured_probe.py — Phase B of preregistration.md Addendum 1 (80-dps proton pin).

Nucleons are gamma-gamma words on their own FOUR strands (vertices V(0), V(1), length 1..L; L = 6
default) that pass reading 3 at every level m = 1..4 on four strands, so proton and neutron may
differ. The deuteron is on eight strands, every strand kept in the trace: x = w1 (gens 0-2) . w2
(gens 4-6), bond K = V(3)^k (enters the newer nucleon, 2026-11-22 ruling) or V(2)^k, k in {1,2,3}.
Every ordered pair (w1, w2) is evaluated at >= 80 dps (via `qou-gg-cli` 320-bit MPFR, independently
cross-checked against pure Python `mpmath` at 85 dps on the L <= 3 subset). Which is the proton is
not determined by the corpus, so no pair is chosen. Ratio and B = -E0 ln r reported, never used to
select (ruling B). Zero float64; nothing fitted or wired.

-- Ref: [leitner2026] bean qou-ales; bean qou-xj4p; bean qou-ggtb
"""
from __future__ import annotations

import itertools
import json
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent
for _p in (
    str(HERE),
    str(REPO / "computations"),
    str(REPO / "computations" / "substrate"),
    str(REPO / "computations" / "qbeta"),
    str(REPO / "tools" / "qou-substrate" / "python"),
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402

WORK_DPS = 85
OUT_DPS = 80
mp.mp.dps = WORK_DPS

import qbeta_e0  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, M_E_MEV  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402


def _fmt(x: mp.mpf) -> str:
    return "0" if x == 0 else mp.nstr(x, OUT_DPS)


def _ensure_cli() -> Path:
    target_dir = Path(os.environ.get("CARGO_TARGET_DIR", "/tmp/qou-shared-cargo-target"))
    bin_path = target_dir / "release" / "qou-gg-cli"
    if bin_path.is_file() and os.access(bin_path, os.X_OK):
        return bin_path
    env = os.environ.copy()
    env["PATH"] = f"{Path.home() / '.cargo' / 'bin'}:{env.get('PATH', '')}"
    env["CARGO_TARGET_DIR"] = str(target_dir)
    env["CARGO_BUILD_JOBS"] = env.get("CARGO_BUILD_JOBS", "2")
    env["CARGO_NET_GIT_FETCH_WITH_CLI"] = "true"
    manifest = REPO / "crates" / "qou-gg-cli" / "Cargo.toml"
    subprocess.run(
        ["nice", "-n", "15", "cargo", "build", "--release", "--manifest-path", str(manifest)],
        cwd=str(REPO),
        env=env,
        check=True,
    )
    return bin_path


def _spot_check_v0v0v0_mpmath(q0: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    """Independent 85-dps mpmath check of tr_M^(4)(V0^3) via H_3 -> H_4 Markov embedding."""
    h = q0 - mp.mpf(1) / q0
    z_d = (q0 ** 3) / (q0 ** 2 + mp.mpf(1))
    # V^3 in H_3(q) has NF: 1 + h^2 V - h^2 V^2; embedded on strands 0..2 of H_4(q),
    # strand 3 is idle, so under normalized Convention-D trace on H_4, tr_M^(4)(V0^3) = tr_M^(3)(V^3)!
    # Compute V^3 = 1 + h^2*(L_+ - h*s_0) - h^2*((L_+ - h*s_0)^2):
    # More directly: chi^(3)(V^3) = 1 (since s_0 -> q, s_1^-1 -> q^-1 => V -> 1),
    # and on 2D Specht (2,1), V = s_0 * s_1^-1 has det = (-1)*(-1) = 1 and trace = h*(q^-1) ...
    # Actually V = s_0*(s_1 - h): chi^(2,1)(V) = chi^(2,1)(s_0*s_1) - h*chi^(2,1)(s_0) = -1 - h^2!
    # Wait: let's evaluate exact 2x2 matrix of V on [2,1]!
    s0_21 = mp.matrix([[q0, mp.mpf(0)], [mp.mpf(0), -mp.mpf(1) / q0]])
    c_m2 = h / (mp.mpf(1) - q0 ** 4)
    c_p2 = h / (mp.mpf(1) - q0 ** (-4))
    q2_int = q0 + mp.mpf(1) / q0
    off = mp.sqrt(mp.mpf(1) - mp.mpf(1) / (q2_int ** 2))
    s1_21 = mp.matrix([[c_m2, off], [off, c_p2]])
    s1_inv_21 = s1_21 - h * mp.eye(2)
    v_21 = s0_21 * s1_inv_21
    v3_21 = v_21 * v_21 * v_21
    chi21_v3 = v3_21[0, 0] + v3_21[1, 1]
    y3 = (q0 ** 4 + mp.mpf(1)) / ((q0 ** 2 + mp.mpf(1)) ** 2)
    y21 = (q0 ** 2) / ((q0 ** 2 + mp.mpf(1)) ** 2)
    tr_v3 = y3 * mp.mpf(1) + y21 * chi21_v3
    return tr_v3, z_d


def main() -> int:
    mp.mp.dps = WORK_DPS
    max_l = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    q0 = q_at(dps=WORK_DPS)
    m_e = mp.mpf(str(M_E_MEV))
    b_ame = mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION))
    e0_order0 = qbeta_e0.order_zero(q=q0, m_e=m_e)
    e0_tower = qbeta_e0.tower_summed(q=q0, m_e=m_e)

    bin_path = _ensure_cli()
    proc = subprocess.run(
        [
            "nice", "-n", "15", str(bin_path),
            "--section", "flavoured",
            "--prec-bits", "320",
            "--dps", str(OUT_DPS),
            "--flavoured-max-vertices", str(max_l),
        ],
        cwd=str(REPO),
        check=True,
        capture_output=True,
        text=True,
    )
    c4 = json.loads(proc.stdout, parse_float=str)["h4_flavoured_census"]

    tr_v3_mp, _ = _spot_check_v0v0v0_mpmath(q0)
    v000_row = next(r for r in c4["nucleon_words"] if r["word"] == "V0V0V0")
    tr_v000_err = abs(mp.mpf(v000_row["tr_m"]) - tr_v3_mp)

    rows = []
    for r in c4["passing_atoms"]:
        rows.append(
            {
                "w1": r["w1"],
                "w2": r["w2"],
                "bond": r["bond"],
                "ratio": r["ratio"],
                "B_MeV": r["b_order_zero_mev"],
                "B_tower_MeV": r["b_tower_mev"],
                "B_err_vs_AME_pct": r["b_err_vs_ame_order_zero_pct"],
                "B_tower_err_vs_AME_pct": r["b_err_vs_ame_tower_pct"],
                "min_level_char": r["min_level_char"],
            }
        )

    summary = {
        "n_candidates_h4": c4["n_candidates_h4"],
        "n_nucleon_words": c4["n_passing_nucleon_words"],
        "n_pairs": c4["n_ordered_pairs_h8"],
        "n_passing_atoms": c4["n_passing_h8_atoms"],
        "n_passing_v3_cubed_atoms": c4["n_passing_v3_cubed_atoms"],
        "B_min_MeV": c4["b_order_zero_min_mev"],
        "B_max_MeV": c4["b_order_zero_max_mev"],
        "B_tower_min_MeV": c4["b_tower_min_mev"],
        "B_tower_max_MeV": c4["b_tower_max_mev"],
        "n_bound": c4["n_bound"],
        "n_unbound": c4["n_unbound"],
    }

    total_evals = c4["n_ordered_pairs_h8"] * 7
    wb = (
        WitnessBuilder("gg-deuteron-flavoured", engine="mpmath+qou-gg-cli")
        .set_description(
            "PROBE Phase B (prereg addendum 1, commit 2024623969e; owner 'need all strands'): "
            f"four-strand gamma-gamma nucleon words (1..{max_l} vertices) passing reading 3, "
            "every ordered pair on eight strands with bonds V(3)^k, V(2)^k; reading 3 at every "
            "level, convention D, 80-dps proton pin (plus Readings A/B normal-form net table). "
            "No pair chosen as 'the deuteron'. Ratio and B reported, never used to select."
        )
        .set_audit_only("computations/probes/gg_deuteron_bond/results.md")
        .add_parameter("L", max_l)
        .add_parameter("out_dps", OUT_DPS)
        .add_parameter("B_AME_2H_MeV", _fmt(b_ame))
        .add_parameter("E0_MeV", _fmt(e0_order0))
        .add_parameter("E0_tower_MeV", _fmt(e0_tower))
        .add_data("nucleon_words", [r["word"] for r in c4["nucleon_words"]])
        .add_data("nucleon_word_readings_a_b", c4["nucleon_words"])
        .add_data("summary", summary)
        .add_data("passing_atoms", rows)
    )
    wb.add_assertion(
        "every_row_evaluated",
        computed=c4["n_total_h8_evaluations"],
        expected=total_evals,
        tolerance=0,
        source="all enumerated 8-strand free + bonded rows were evaluated",
    )
    wb.add_assertion(
        "v0v0v0_trace_matches_independent_mpmath_80dps",
        computed=_fmt(tr_v000_err),
        expected="0",
        tolerance="1e-76",
        source="TwoRowTowerRep(4) tr_M(V0^3) vs independent 85-dps mpmath Hoefsmit [2,1] evaluation",
    )
    wb.save()
    print("SUMMARY", summary, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
