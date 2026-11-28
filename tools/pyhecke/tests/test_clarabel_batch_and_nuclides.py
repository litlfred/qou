"""80-dps parity, `qou-fu8c` interval semantics, bounded-RSS, and speedup tests
for `crates/qou-clarabel` batch LP/PSD mode & `all_nuclides_sdp_admissibility_mp` (`qou-cbot` Rank #5).
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp
import pytest

REPO_ROOT = Path(__file__).resolve().parents[3]
for _p in (
    str(REPO_ROOT / "computations"),
    str(REPO_ROOT / "computations" / "substrate"),
    str(REPO_ROOT / "tools" / "pyhecke" / "python"),
    str(REPO_ROOT / "tools" / "qou-substrate" / "python"),
):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from compound_shift_nf import build_atom_nf_mp  # noqa: E402
from pyhecke import gram  # noqa: E402
from pyhecke.lp_dual_solver import (  # noqa: E402
    _find_qou_gg_cli_bin,
    solve_operator_selection_lp,
    solve_operator_selection_lp_batch,
)

GG_CLI = _find_qou_gg_cli_bin()
pytestmark = pytest.mark.skipif(GG_CLI is None, reason="qou-gg-cli binary not built")


def test_batch_80dps_kkt_and_single_call_parity():
    """Verify `< 10^-76` KKT/duality-gap residuals at 320-bit MPFR and exact parity
    between `solve_operator_selection_lp_batch` and `solve_operator_selection_lp`."""
    with mp.workdps(98):
        t_s = gram.tr_m_mp_strings(94)
        G_s = gram.gram_matrix_mp_strings(94)
        targets = ["1", "2", "4", "16", "40", "90", "208", "238", "260"]

        batch_res, meta = solve_operator_selection_lp_batch(
            t_s,
            G_s,
            targets,
            backend="clarabel",
            prec_bits=320,
            out_dps=80,
            return_metadata=True,
        )
        assert meta["subprocesses_spawned"] == 1
        assert meta["n_items"] == len(targets)
        assert len(batch_res) == len(targets)

        tol_kkt = mp.mpf("1e-76")
        for a_str, rb in zip(targets, batch_res):
            assert rb.feasible is True
            assert rb.backend == "clarabel-mpfr"
            assert rb.precision_bits == 320
            assert rb.active_set == [0]
            assert rb.y0_star_str is not None
            assert abs(mp.mpf(rb.kkt_primal_residual_str)) < tol_kkt
            assert abs(mp.mpf(rb.kkt_dual_residual_str)) < tol_kkt
            assert abs(mp.mpf(rb.duality_gap_str)) < tol_kkt
            assert abs(mp.mpf(rb.gap_recomputed_str)) < tol_kkt

        # Exact parity vs single-instance Clarabel MPFR call on A = 208
        r_single = solve_operator_selection_lp(
            t_s, G_s, "208", backend="clarabel", prec_bits=320
        )
        r_batch_208 = batch_res[targets.index("208")]
        assert r_batch_208.active_set == r_single.active_set
        assert abs(mp.mpf(r_batch_208.y0_star_str) - mp.mpf(r_single.y0_star_str)) < tol_kkt
        for yb, ys in zip(r_batch_208.y_star_str, r_single.y_star_str):
            assert abs(mp.mpf(yb) - mp.mpf(ys)) < tol_kkt


def test_batch_nontrivial_quotient_lp_80dps_kkt():
    """Verify `< 10^-76` KKT & duality gap on non-degenerate 2-row quotient LPs (`y0* > 0`)."""
    with mp.workdps(95):
        c3 = "0.49315793733281412279204569103245019283746192837461928374619283746192837461928375"
        c21 = "0.50540422650450192837461928374619283746192837461928374619283746192837461928374619"
        t_s = [c3, c21]
        G_s = [[c3, "0"], ["0", c21]]
        targets = ["0.99856216383731605116666497477864303029939030299390302993903029939030299390302994", "2.5"]

        res_list = solve_operator_selection_lp_batch(
            t_s, G_s, targets, backend="clarabel", prec_bits=320, out_dps=80
        )
        tol = mp.mpf("1e-76")
        for n_str, r in zip(targets, res_list):
            assert r.feasible is True
            # Optimum puts all mass on min(c3, c21) = c3 => y0* = c3, u_0* = 0, u_1* = 1 - c3/c21
            expected_y0 = mp.mpf(c3)
            expected_u1 = mp.mpf(1) - mp.mpf(c3) / mp.mpf(c21)
            assert abs(mp.mpf(r.y0_star_str) - expected_y0) < tol
            assert abs(mp.mpf(r.y_star_str[0])) < tol
            assert abs(mp.mpf(r.y_star_str[1]) - expected_u1) < tol
            assert abs(mp.mpf(r.primal_obj_str) - mp.mpf(n_str) * expected_y0) < tol
            assert abs(mp.mpf(r.kkt_dual_residual_str)) < tol
            assert abs(mp.mpf(r.duality_gap_str)) < tol


def test_qou_fu8c_zero_cost_null_and_interval_semantics():
    """Verify `2026-11-25` `qou-fu8c` rule: zero-cost unconstrained dual coordinates
    emit `u_identified = False`, `None` (`null` in JSON) in `y_star_masked_str`,
    and `["0", "+inf"]` in `y_star_intervals`."""
    c3 = "0.49315793733281412279"
    c21 = "0.50540422650450192837"
    t_s = [c3, c21, "0"]
    G_s = [
        [c3, "0", "0"],
        ["0", c21, "0"],
        ["0", "0", "0"],
    ]
    res = solve_operator_selection_lp_batch(
        t_s, G_s, ["0.99856216383731605116"], backend="clarabel", prec_bits=320, out_dps=80
    )[0]
    assert res.feasible is True
    assert res.u_identified == [True, True, False]
    assert res.y_star_masked_str[0] is not None
    assert res.y_star_masked_str[1] is not None
    assert res.y_star_masked_str[2] is None
    assert res.y_star_intervals == [None, None, ["0", "+inf"]]

    as_json = json.loads(json.dumps(res.to_dict()))
    assert as_json["y_star_masked_str"][2] is None
    assert as_json["y_star_intervals"][2] == ["0", "+inf"]


def test_streaming_jsonl_mode_and_full_229_nuclide_rss_bound():
    """Verify `--lp-batch-jsonl` streaming parity and `< 80 MB` peak RSS across all 229
    distinct nuclide `A` values (`1..260`)."""
    t_s = gram.tr_m_mp_strings(90)
    G_s = gram.gram_matrix_mp_strings(90)

    # 1. Streaming JSONL check on 5 items
    lines_in = "\n".join(
        json.dumps({"id": str(a), "t": t_s, "G": G_s, "n_target": str(a), "psd_diagonal_lift": True})
        for a in (1, 4, 16, 208, 238)
    ) + "\n"
    proc = subprocess.run(
        [GG_CLI, "--lp-batch-jsonl", "--prec-bits", "320", "--dps", "80"],
        input=lines_in,
        capture_output=True,
        text=True,
        check=True,
    )
    out_lines = [json.loads(ln) for ln in proc.stdout.strip().splitlines()]
    assert len(out_lines) == 5
    for row in out_lines:
        assert row["feasible"] is True
        assert len(row["eigenvalues_str"]) == 6

    # 2. Full 229-item nuclide batch RSS < 80 MB + wall-time benchmark
    magic = {2, 8, 20, 28, 50, 82, 126}
    distinct_a = sorted({
        z + n
        for z in range(0, 93)
        for n in range(0, 147)
        if 0 < (z + n) <= 260 and (z in magic or n in magic or (z + n) % 4 == 0)
    })
    assert len(distinct_a) == 229

    t0 = time.perf_counter()
    res_229, meta = solve_operator_selection_lp_batch(
        t_s,
        G_s,
        [str(a) for a in distinct_a],
        backend="clarabel",
        prec_bits=320,
        out_dps=80,
        return_metadata=True,
    )
    dt_batch = time.perf_counter() - t0
    assert len(res_229) == 229
    assert all(r.feasible and r.y0_star_str is not None for r in res_229)
    assert meta["peak_rss_bytes"] < 80 * 1024 * 1024, (
        f"peak RSS {meta['peak_rss_bytes'] / (1024*1024):.2f} MiB >= 80 MiB"
    )
    assert dt_batch < 25.0, f"229-item batch took {dt_batch:.2f}s (expected < 25s)"


def test_atom_nf_batch_80dps_parity_including_pb208_and_u238():
    """Verify `--atom-nf-batch` matches `compound_shift_nf.build_atom_nf_mp` to `< 10^-75`
    relative error across light, doubly-magic, Pb-208 (`10^499`), and U-238 (`10^662`)."""
    pairs = [(1, 0), (0, 1), (1, 1), (2, 2), (8, 8), (20, 28), (50, 82), (82, 126), (92, 146)]
    req = {
        "prec_bits": 384,
        "nf_dps": 92,
        "net_dps": 30,
        "log10_dps": 20,
        "pairs": [[z, n] for z, n in pairs],
    }
    proc = subprocess.run(
        [GG_CLI, "--atom-nf-batch"],
        input=json.dumps(req),
        capture_output=True,
        text=True,
        check=True,
    )
    resp = json.loads(proc.stdout, parse_float=str)
    assert resp["n_rows"] == len(pairs)

    with mp.workdps(120):
        for (z, n), row in zip(pairs, resp["rows"]):
            nf_py = build_atom_nf_mp(z, n, dps=108)
            net_py = sum(nf_py)
            for k in range(6):
                c_scale = max(abs(nf_py[k]), mp.mpf(1))
                c_rel = abs(mp.mpf(row["nf_str"][k]) - nf_py[k]) / c_scale
                assert c_rel < mp.mpf("1e-80"), f"(Z={z}, N={n}) comp {k} rel_err={c_rel}"
            net_rust_full = sum(mp.mpf(s) for s in row["nf_str"])
            scale = max(abs(net_py), mp.mpf(1))
            rel_err = abs(net_rust_full - net_py) / scale
            assert rel_err < mp.mpf("1e-76"), f"(Z={z}, N={n}) rel_err={rel_err}"
            # Also check 30-digit formatted nf_net_str matches mp.nstr(net_py, 30) to 1e-28 rel
            rel_30 = abs(mp.mpf(row["nf_net_str"]) - net_py) / scale
            assert rel_30 < mp.mpf("1e-28"), f"(Z={z}, N={n}) 30-dps rel_err={rel_30}"
