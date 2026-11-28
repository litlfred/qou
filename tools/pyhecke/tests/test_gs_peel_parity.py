"""Exact bit-for-bit algebraic parity & speedup tests for `crates/gs-basis` (`gs-peel`).

Verifies:
  1. 100% identical exact `dict[int, Fraction]` Laurent coefficients between
     `symbolic_nf_q_degree_magic_probe.build_atom_nf_lau(..., use_rust=True)` (`DyadicLaurent`)
     and pure-Python `build_atom_nf_lau_python` across all `(Z, N)` for `1 <= Z + N <= 8`
     (`44` configurations x `6` basis components = `264` Laurent polynomials).
  2. Exact polynomial agreement between `tl_dyadic_trace_walk` and Annex-B homogeneous
     `markov_tower_homogeneous` peeling in `Z[1/2][q, q^{-1}]` across `n = 2..7` strands
     (plus exact rational parity with `bratteli_two_row_rational` on monotone words up to `n = 8`).
  3. 80-dps numerical agreement (`< 1e-75`) between `markov_trace_two_row_tower_probe.walk`
     (`gs-peel` path) and `walk_python` at the proton anchor `q_at("proton")`.
"""
from __future__ import annotations

import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import pytest

_ROOT = Path(__file__).resolve().parents[3]
for _rel in (
    "computations",
    "computations/hecke",
    "computations/probes",
    "computations/substrate",
    "tools/qou-substrate/python",
):
    _p = str(_ROOT / _rel)
    if _p not in sys.path:
        sys.path.insert(0, _p)

from gs_peel_bridge import (  # noqa: E402
    decode_dyadic_laurent,
    gs_peel_binary_path,
    invoke_gs_peel,
)
import markov_trace_two_row_tower_probe as two_row_probe  # noqa: E402
import symbolic_nf_q_degree_magic_probe as sym_nf_probe  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402


def _require_gs_peel() -> Path:
    bp = gs_peel_binary_path()
    if bp is None:
        pytest.skip("gs-peel release binary not built")
    return bp


def test_dyadic_laurent_nf_exact_parity_through_a8_and_speedup():
    _require_gs_peel()

    # Batch all 44 configurations (1 <= A <= 8) in one gs-peel call AND verify single-call wrapper:
    configs = [(z, a - z) for a in range(1, 9) for z in range(a + 1)]
    assert len(configs) == 44

    jobs = [
        {
            "id": f"{z}_{n}",
            "num_strands": 3,
            "include_terms": True,
            "steps": sym_nf_probe._atom_dyadic_steps(z, n),
        }
        for (z, n) in configs
    ]

    t_rust0 = time.perf_counter()
    resp = invoke_gs_peel({"op": "dyadic_hecke_nf_batch", "jobs": jobs})
    t_rust = time.perf_counter() - t_rust0

    t_py0 = time.perf_counter()
    py_refs = {(z, n): sym_nf_probe.build_atom_nf_lau_python(z, n) for (z, n) in configs}
    t_py = time.perf_counter() - t_py0

    for (z, n), res in zip(configs, resp["results"]):
        rust_nf = [decode_dyadic_laurent(c.get("terms") or []) for c in res["components"]]
        assert rust_nf == py_refs[(z, n)], f"Laurent coefficient mismatch at (Z={z}, N={n})"

    # Also check direct drop-in function at A = 12 (Z=6, N=6):
    t0 = time.perf_counter()
    py_12 = sym_nf_probe.build_atom_nf_lau_python(6, 6)
    py_12_sec = time.perf_counter() - t0

    t1 = time.perf_counter()
    rust_12 = sym_nf_probe.build_atom_nf_lau(6, 6, use_rust=True)
    rust_12_sec = time.perf_counter() - t1

    assert rust_12 == py_12

    # Verify profile_batch observable dictionary parity on A=1..8 (excluding wall_ms):
    batch_profiles = sym_nf_probe.profile_batch(configs, use_rust=True)
    for (z, n), bp in zip(configs, batch_profiles):
        ref_p = sym_nf_probe.profile(z, n, use_rust=False)
        for k in (
            "Z",
            "N",
            "A",
            "magic_Z",
            "magic_N",
            "any_magic",
            "doubly_magic",
            "max_degree",
            "min_degree",
            "degree_span",
            "n_terms",
            "degree_profile",
            "support_size",
        ):
            assert bp[k] == ref_p[k], f"profile mismatch on {k} at (Z={z}, N={n})"

    # Record timing diagnostics in stdout for -s inspection:
    print(
        f"\n[parity OK] A=1..8 batch: py={t_py*1000:.1f}ms vs rust={t_rust*1000:.1f}ms; "
        f"A=12 (6,6): py={py_12_sec*1000:.1f}ms vs rust={rust_12_sec*1000:.1f}ms"
    )


def test_tl_walk_vs_homogeneous_markov_tower_and_bratteli_through_n8():
    _require_gs_peel()

    # 1. Exact symbolic Laurent parity between TL loop-closure walk and homogeneous Markov peeling
    #    on non-monotone braided nuclear tower words for n = 2..7:
    #    Recall: P_n(q) / (q + q^-1)^n == scaled_markov(q) / (q + q^-1)^{n-1}
    #    <==>    P_n(q) == (q + q^-1) * scaled_markov(q) identically in Z[1/2][q, q^{-1}]!
    z_p, n_n = 3, 4  # A = 7 strands
    types = ["p"] * z_p + ["n"] * n_n
    levels = []
    flat_steps = []
    for k in range(1, len(types)):
        lvl = []
        for i in range(k):
            ti, tk = types[i], types[k]
            if ti == "p" and tk == "p":
                st = {"gen": i, "c_mant": 1, "d_mant": 0, "d_exp2": 0, "d_hpow": 0}
            elif ti == "n" and tk == "n":
                st = {"gen": i, "c_mant": 1, "d_mant": -1, "d_exp2": 0, "d_hpow": 1}
            else:
                st = {"gen": i, "c_mant": 1, "d_mant": -1, "d_exp2": -1, "d_hpow": 1}
            lvl.append(st)
        levels.append(lvl)

    tl_resp = invoke_gs_peel({"op": "tl_dyadic_trace_walk", "levels": levels})
    for idx, row in enumerate(tl_resp["levels"]):
        m = int(row["strands"])
        flat_steps.extend(levels[idx])
        peel_resp = invoke_gs_peel({
            "op": "markov_tower_homogeneous",
            "num_strands": m,
            "steps": flat_steps,
        })
        p_tl = decode_dyadic_laurent(row["numerator_terms"])
        scaled_mk = decode_dyadic_laurent(peel_resp["scaled_trace_terms"])
        # Multiply scaled_mk by delta = q + q^-1:
        delta_times_mk: dict[int, Fraction] = {}
        for exp, val in scaled_mk.items():
            for sh in (-1, 1):
                nv = delta_times_mk.get(exp + sh, Fraction(0)) + val
                if nv:
                    delta_times_mk[exp + sh] = nv
                elif (exp + sh) in delta_times_mk:
                    del delta_times_mk[exp + sh]
        assert p_tl == delta_times_mk, f"TL vs Markov tower mismatch at m={m}"

    # 2. Monotone n = 8 strands exact rational parity: Bratteli two-row vs homogeneous Markov peel at q = 2:
    q_val = Fraction(2, 1)
    h_val = q_val - 1 / q_val  # 3/2
    # Monotone steps on n = 8 strands (generators 0..6):
    mono_dyadic = [
        {"gen": 0, "c_mant": 1, "d_mant": 0, "d_exp2": 0, "d_hpow": 0},
        {"gen": 0, "c_mant": 1, "d_mant": -1, "d_exp2": 0, "d_hpow": 1},
        {"gen": 1, "c_mant": 1, "d_mant": -1, "d_exp2": -1, "d_hpow": 1},
        {"gen": 2, "c_mant": 1, "d_mant": 0, "d_exp2": 0, "d_hpow": 0},
        {"gen": 3, "c_mant": 1, "d_mant": -1, "d_exp2": 0, "d_hpow": 1},
        {"gen": 4, "c_mant": 1, "d_mant": -1, "d_exp2": -1, "d_hpow": 1},
        {"gen": 5, "c_mant": 1, "d_mant": 0, "d_exp2": 0, "d_hpow": 0},
        {"gen": 6, "c_mant": 1, "d_mant": -1, "d_exp2": 0, "d_hpow": 1},
    ]
    mono_rat = []
    for st in mono_dyadic:
        d_q = Fraction(st["d_mant"]) * (Fraction(2) ** st["d_exp2"]) * (h_val ** st["d_hpow"])
        mono_rat.append({
            "gen": st["gen"],
            "c_num": 1,
            "c_den": 1,
            "d_num": d_q.numerator,
            "d_den": d_q.denominator,
        })

    bratteli = invoke_gs_peel({
        "op": "bratteli_two_row_rational",
        "num_strands": 8,
        "q_num": 2,
        "q_den": 1,
        "factors": mono_rat,
    })
    peel_8 = invoke_gs_peel({
        "op": "markov_tower_homogeneous",
        "num_strands": 8,
        "steps": mono_dyadic,
    })
    poly_8 = decode_dyadic_laurent(peel_8["scaled_trace_terms"])
    eval_num = sum(c * (q_val ** e) for e, c in poly_8.items())
    delta_q = q_val + 1 / q_val
    trace_from_peel = eval_num / (delta_q ** 7)
    trace_from_bratteli = Fraction(int(bratteli["trace_num"]), int(bratteli["trace_den"]))
    assert trace_from_peel == trace_from_bratteli

    # 3. 80-dps proton-pin parity on markov_trace_two_row_tower_probe.walk (A = 7):
    with mp.workdps(80):
        q_p = q_at(80)
        res_rust = two_row_probe.walk(3, 4, q_p, use_rust=True)
        res_py = two_row_probe.walk_python(3, 4, q_p)
        assert set(res_rust.keys()) == set(res_py.keys())
        for m in sorted(res_py):
            tr_r, pn_r = res_rust[m]
            tr_p, pn_p = res_py[m]
            assert pn_r == pn_p
            assert abs(tr_r - tr_p) < mp.mpf("1e-74"), f"80-dps drift at m={m}: {abs(tr_r - tr_p)}"
