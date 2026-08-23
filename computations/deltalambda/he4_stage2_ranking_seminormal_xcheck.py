#!/usr/bin/env python3
"""Fast seminormal-f64 ranking cross-check for the ⁴He stage-2 dominant
binding channel λ*(K).

Companion to the full `he4_binding_k_stage2_probe.py` (both Wedderburn
legs, ~1 h at 50 dps). This script runs ONLY the channel ranking —
χ_λ(K) for all 77 blocks of H₁₂ via the seminormal-f64 engine
(`pyhecke_native.chi_lambda_all_partitions_f64`), ranked by |y_λ·χ_λ(K)| —
in under a minute. It exists to answer, cheaply and independently of the
buggy GP kernel (see `docs/audits/2026-07-14-gp-kernel-bug-and-he4-stage2.md`),
the question the 2026-07-14 audit left open: *does the committed
GP-legged dominant channel λ*(K) = (9, 3) survive the engine fix?*

Engine independence: the committed stage-2 witness ranked λ*(K) on the
GP character path (`chi_lambdas_via_gp`, found to return wrong χ on some
plain braid words). This script uses the **seminormal** path instead —
the same family the full probe's Leg A now uses — so agreement between
this f64 ranking and the full probe's 50-dps Leg A is an f64-vs-mpfr
precision cross-check, and disagreement of either with the committed
(9, 3) would flag a GP-bug artifact in the ranking.

Scope-(a); audit-only; no fit; nothing wired. tr_M(K) here is the
f64-precision value — the 50-dps authoritative value comes from the full
probe's witness.
"""
from __future__ import annotations
import datetime
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
for p in ["computations", "computations/deltalambda", "computations/substrate",
          "tools/qou-substrate/python", "tools/pyhecke/python"]:
    sys.path.insert(0, str(REPO / p))

import mpmath as mp  # noqa: E402

# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

import pyhecke_native as pn  # noqa: E402
import hecke_core  # noqa: E402
from canonical_braid_crossings import _avg_color_delta  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402

N = 12
COMP = REPO / "computations"


def load_canonical_q() -> str:
    d = json.loads((COMP / "q-pinning-50-digit.witness.json").read_text())
    q = d["derived_50_digit"]["q"]
    assert q.startswith("1.109978595557"), q
    return q


def classify(triples, h_f64):
    """Map (c, d, gen) factor triples to seminormal factor kinds
    (verbatim from he4_binding_k_stage2_probe.py)."""
    dcw = float(_avg_color_delta())
    out = []
    for (c, d, g0) in triples:
        assert abs(float(c) - 1.0) < 1e-12
        df = float(d)
        if abs(df) < 1e-12:
            out.append(("s", g0))
        elif abs(df + h_f64) < 1e-9:
            out.append(("i", g0))
        elif abs(df + h_f64 / 2) < 1e-9:
            out.append(("a", g0))
        else:
            assert abs(df + h_f64 * (0.5 - dcw / 4)) < 1e-9, d
            out.append(("cw", g0))
    return out


def shifted_nucleon_kinds(Z1, N1, off, h_f64):
    return [(k, g0 + off)
            for (k, g0) in classify(atom_braid_word_3A(Z1, N1), h_f64)]


def main() -> int:
    t_start = time.time()
    q_str = load_canonical_q()
    q0 = mp.mpf(q_str)
    two_q = q0 + 1 / q0
    h_f64 = float(hecke_core.h)
    delta = mp.mpf(float(_avg_color_delta()))
    a_cw, b_cw = mp.mpf(1) / 2 + delta / 4, mp.mpf(1) / 2 - delta / 4

    # ── K = T ++ reversed-inverted cp  (verbatim construction) ──
    T_kinds = classify(atom_braid_word_3A(2, 2), h_f64)
    cp_kinds = (shifted_nucleon_kinds(1, 0, 0, h_f64)
                + shifted_nucleon_kinds(1, 0, 3, h_f64)
                + shifted_nucleon_kinds(0, 1, 6, h_f64)
                + shifted_nucleon_kinds(0, 1, 9, h_f64))
    INV = {"s": "i", "i": "s", "a": "ia"}
    K_kinds = list(T_kinds) + [(INV[k], g0) for (k, g0) in reversed(cp_kinds)]
    n_ia = sum(1 for k, _ in K_kinds if k == "ia")
    n_cw = sum(1 for k, _ in K_kinds if k == "cw")
    assert n_cw == 1, n_cw
    scalar = (4 / two_q ** 2) ** n_ia
    print(f"K word: {len(K_kinds)} factors ({n_ia} averaged-inverse, "
          f"{n_cw} color-weighted)")

    def signed_letters(cw_branch):
        w = []
        for (k, g0) in K_kinds:
            g1 = g0 + 1
            w.append({"s": (1, g1), "i": (-1, g1), "a": (0, g1),
                      "ia": (0, g1), "cw": (cw_branch, g1)}[k])
        return w

    shapes = pn.partitions_of(N)
    y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(N, q0).items()}

    # ── seminormal-f64 χ_λ(K), both color-weighted branches ──
    t0 = time.time()
    branch = {}
    for br in (1, -1):
        branch[br] = {tuple(lam): mp.mpf(chi) for lam, chi in
                      pn.chi_lambda_all_partitions_f64(N, signed_letters(br),
                                                       float(q0))}
        print(f"  branch {br:+d} done at {time.time()-t0:.0f}s", flush=True)
    chi = {lam: scalar * (a_cw * branch[1][lam] + b_cw * branch[-1][lam])
           for lam in map(tuple, shapes)}

    rows = sorted(
        ({"lambda": list(lam), "chi_K": float(chi[lam]),
          "y_lambda": float(y[lam]),
          "y_chi_abs": float(abs(y[lam] * chi[lam]))}
         for lam in map(tuple, shapes)),
        key=lambda r: -r["y_chi_abs"])
    tr_M_K = sum(y[lam] * chi[lam] for lam in map(tuple, shapes))
    dominant = tuple(rows[0]["lambda"])
    runner = tuple(rows[1]["lambda"])
    margin = (rows[0]["y_chi_abs"] - rows[1]["y_chi_abs"]) / rows[0]["y_chi_abs"]

    print(f"tr_M(K) = {mp.nstr(tr_M_K, 16)} (f64 engine)")
    print("top 5 by |y_λ·χ_λ(K)|:")
    for r in rows[:5]:
        print(f"  λ={str(tuple(r['lambda'])):26s} |y·χ| = {r['y_chi_abs']:.8g}")
    print(f"dominant λ*(K) = {dominant}; runner-up {runner}; "
          f"relative margin {margin:.3%}")
    print(f"committed GP-legged dominant = (9, 3): "
          f"{'CONFIRMED' if dominant == (9, 3) else 'REPLACED'}")

    wit = {
        "computation": "he4-stage2-ranking-seminormal-xcheck",
        "description": "Fast seminormal-f64 dominant-channel ranking for the "
                       "A=4 stage-2 binding operator K(⁴He) = T·cp⁻¹ at "
                       "H12(q0); companion cross-check to the full "
                       "he4_binding_k_stage2_probe (both Wedderburn legs). "
                       "Confirms whether the committed GP-legged λ*(K)=(9,3) "
                       "survives the seminormal engine (GP kernel bug: "
                       "docs/audits/2026-07-14-gp-kernel-bug-and-he4-stage2.md).",
        "audit_only": True,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "pyhecke_native seminormal-f64 (chi_lambda_all_partitions_f64); "
                  "GP path NOT used. tr_M(K) is f64-precision; 50-dps "
                  "authoritative value from he4-binding-k-stage2.witness.json.",
        "q_pin": {"used": "canonical muon (QOU_Q0_ANCHOR=ideal)", "value": q_str},
        "dominant_lambda": list(dominant),
        "runner_up_lambda": list(runner),
        "dominant_margin_rel": margin,
        "tr_M_K_f64": mp.nstr(tr_M_K, 16),
        "per_lambda_top10": rows[:10],
        "elapsed_sec": round(time.time() - t_start, 1),
        "scope": "(a) — ranking cross-check only; no PSD certificate (see the "
                 "full probe); no AME input; no fit; nothing wired.",
        "assertions": [
            {"label": "dominant channel survives GP→seminormal (== committed (9,3))",
             "passed": dominant == (9, 3)},
            {"label": "all 77 blocks ranked",
             "passed": len(rows) == 77},
        ],
    }
    wit["allPassed"] = all(a["passed"] for a in wit["assertions"])
    # Provenance envelope. This producer writes its witness as raw JSON, so
    # nothing stamps `scriptHash` / `commitSha` / `computedAt` on it. That is
    # not cosmetic: a witness without `scriptHash` cannot be compared against
    # its producer, so it DROPS OUT of the self-staleness audit entirely and
    # reads as "not stale" forever. Regenerating one therefore looks like
    # progress while removing it from the count — a false drain. Measured
    # 2026-08-23: four such witnesses across one regeneration sweep, and 29
    # raw-JSON producers repo-wide that would do the same.
    #
    # `stamp_staleness_metadata` rather than `wrap_legacy().save()` on purpose:
    # it adds the fields in place and leaves the on-disk shape untouched, so no
    # consumer of this witness's legacy `assertions` records (which key on
    # `label`, not `name`) has to change. `engine` is passed back from the
    # payload because the helper overwrites that field, and this producer
    # writes a descriptive engine string worth keeping.
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        wit, script_path=__file__,
        engine=wit.get("engine", 'pyhecke_native'))
    out = HERE / "he4-stage2-ranking-seminormal-xcheck.witness.json"
    json.dump(wit, open(out, "w"), indent=1)
    print("witness ->", out.name, " allPassed:", wit["allPassed"],
          f" ({wit['elapsed_sec']}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
