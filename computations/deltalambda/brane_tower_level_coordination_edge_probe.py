#!/usr/bin/env python3
"""brane_tower_level_coordination_edge_probe.py — GAP-A-4 DERIVE-OR-WALL for the
A=3 Δ_λ 3-body MAGNITUDE from the coordination-graph EDGE structure (jet-filtration
depth), NOT the tower LEVEL.

The gap (recap)
---------------
#4364 lifted the A=3 Borromean 3-body cluster to the H₉ joint-trace level via
width-3 cabling of the word (Δ_A·Δ_B⁻¹)³ → c₃ = +0.297 MeV = 0.63× μ₃
(μ₃ = +0.4708, AdditiveResidualSimplex #4320): a ~1.6× NEAR-MISS. Every LEVEL/WIDTH
route is closed (three-walls audit 2026-07-26): geometric W_λ overshoots ~30×,
derived color width w=3 IS #4364's near-miss, the n★ level rule is a refuted
overshoot. So the missing r* = μ₃/0.297 = 1.585× is NOT any derived LEVEL.

The structural observation (this probe)
---------------------------------------
#4364's word (Δ_A·Δ_B⁻¹)³ uses only TWO of the three cable-pairs: Δ_A bonds cables
{0,1}, Δ_B bonds cables {1,2}. The non-adjacent bond {0,2} is ABSENT. A braid
LINEARLY ORDERS its strands, so the coordination graph realizable by ADJACENT
block-transpositions is the PATH P₃ (2 edges), NOT the physical triton's complete
K₃ (3 edges, every nucleon pair bonded). The forward-derived edge ratio is
|E(K₃)|/|E(P₃)| = 3/2 = 1.5.

The 0-fit forward question: does adding the third (wraparound) bond Δ_C in a
symmetric way SCALE the amplitude by ~3/2 while PRESERVING the O(h⁴) Brunnian
order-suppression (→ NEAR-MISS/DERIVATION), or does it break the order and
overshoot (→ WALL: the edge count is a graph fact that does NOT translate to an
amplitude scaling, because braid Brunnian-ness is fragile)?

The reference channel deficits (borromean_h9_magnitude_lift_probe.py) already show
each SINGLE channel is large/non-Brunnian ((Δ_A)³=−0.125, (Δ_B⁻¹)³=+0.973); only
the specific combination (Δ_A·Δ_B⁻¹)³=+0.049 is the small O(h⁴) value. So the
prediction is that a naive third bond breaks Brunnian-ness. We MEASURE it.

Discipline (STRICT anti-fit)
----------------------------
q₀ + canonical Borromean cabling only, 0 fit. μ₃=+0.4708 enters ONLY as the
target. Δ_C is built by the standard adjacent-transposition decomposition
(0 2)=(1 2)(0 1)(1 2) — a principled convention, stated, not tuned. NO word chosen
to hit +0.4708. Nothing wired.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_COMP = _Path(__file__).resolve().parent.parent
for _d in ("hecke", "habiro", "substrate"):
    _p = str(_COMP / _d)
    if _p not in _sys.path:
        _sys.path.insert(0, _p)
_sys.path.insert(0, str(_COMP))
import _path_bridge  # noqa: E402, F401

import json  # noqa: E402
from datetime import datetime, timezone  # noqa: E402

import mpmath as mp  # noqa: E402
import pyhecke_native  # noqa: E402

from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps(30)
HERE = _Path(__file__).resolve().parent
q0 = mp.mpf(str(Q0))
q0f = float(Q0)
H = q0 - 1 / q0
E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))     # SAME E₀ ρ_F uses
_Y9 = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
       for k, v in y_lambda_at(9, q0).items()}


def _perblock(word):
    """ρ_F perblock trace g(word)=Σ_{λ⊢9} y_λ·|χ_λ(word)| (byte-identical to
    three_body_joint_trace_a3._perblock; gen index 1-based)."""
    factors = [(float(c), float(d), int(g) + 1) for (c, d, g) in word]
    cp = pyhecke_native.chi_q_atomic_all_partitions(9, factors, q0f)
    return sum(_Y9[tuple(s)] * abs(mp.mpf(repr(chi)))
               for s, chi in cp if tuple(s) in _Y9)


def _perblock_at(word, qv):
    yv = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
          for k, v in y_lambda_at(9, qv).items()}
    factors = [(float(c), float(d), int(g) + 1) for (c, d, g) in word]
    cp = pyhecke_native.chi_q_atomic_all_partitions(9, factors, float(qv))
    return sum(yv[tuple(s)] * abs(mp.mpf(repr(chi)))
               for s, chi in cp if tuple(s) in yv)


# ── block-transposition generator words (0-based σ gens) ──────────────────────
def _block_transposition(a: int, w: int = 3):
    """Descending-run cabling word swapping the ADJACENT cable blocks
    [a..a+w-1] and [a+w..a+2w-1]. For a=0: (σ2σ1σ0)(σ3σ2σ1)(σ4σ3σ2)."""
    gens = []
    for r in range(w):
        for g in range(a + w - 1 + r, a - 1 + r, -1):
            gens.append(g)
    return gens


def _pos(gens, h=None):
    return [(1.0, 0.0, g) for g in gens]


def _neg(gens, h=None):
    hh = H if h is None else h
    return [(1.0, float(-hh), g) for g in reversed(gens)]


# adjacent cable-block swaps
DA = _block_transposition(0)    # cables {0,1} : gens 0..4
DB = _block_transposition(3)    # cables {1,2} : gens 3..7


def dC_word():
    """The wraparound bond Δ_C (swap cables 0 and 2), built by the standard
    adjacent-transposition decomposition (0 2) = (1 2)(0 1)(1 2) at cable level
    ⇒ Δ_C_word = Δ_B · Δ_A · Δ_B. A principled realization of the third
    (non-adjacent) coordination edge in the linearly-ordered braid; convention
    stated, not tuned."""
    return DB + DA + DB


def _word_pos(gens, h=None):
    return [(1.0, 0.0, g) for g in gens]


def _word_neg(gens, h=None):
    hh = H if h is None else h
    return [(1.0, float(-hh), g) for g in reversed(gens)]


# ── candidate inter words (all 0-fit; h override for the h-order diagnostic) ──
def path_word(h=None):
    """#4364 baseline: (Δ_A · Δ_B⁻¹)³ — the 2-edge PATH P₃."""
    w = []
    for _ in range(3):
        w += _word_pos(DA, h) + _word_neg(DB, h)
    return w


def triangle_word(h=None):
    """Naive 3-edge K₃: (Δ_A · Δ_B⁻¹ · Δ_C)³ — cube of the triangle product,
    all three coordination edges included symmetrically once per period."""
    DC = dC_word()
    w = []
    for _ in range(3):
        w += _word_pos(DA, h) + _word_neg(DB, h) + _word_pos(DC, h)
    return w


def cyclic_word(h=None):
    """3-cycle of PATH words — the S₃-symmetric Borromean analog:
    (Δ_A·Δ_B⁻¹)(Δ_B·Δ_C⁻¹)(Δ_C·Δ_A⁻¹). Each of the three edges appears once
    positive and once negative (bar-balanced), the natural symmetrization of
    #4364's single path period."""
    DC = dC_word()
    return (_word_pos(DA, h) + _word_neg(DB, h)
            + _word_pos(DB, h) + _word_neg(DC, h)
            + _word_pos(DC, h) + _word_neg(DA, h))


def _measure(name, wordfn):
    """deficit, c₃, and log-log h-order for a candidate word."""
    g0 = _perblock([])
    gW = _perblock(wordfn())
    deficit = 1 - gW / g0
    c3 = E0 * (g0 - gW)
    # h-order via a q-grid
    grid = ["1.02", "1.04", "1.08"]
    defs = []
    for qv in grid:
        qm = mp.mpf(qv)
        hv = qm - 1 / qm
        d = 1 - _perblock_at(wordfn(h=hv), qm) / _perblock_at([], qm)
        defs.append(d)
    (d1, d2) = defs[0], defs[-1]
    h1 = mp.mpf("1.02") - 1 / mp.mpf("1.02")
    h2 = mp.mpf("1.08") - 1 / mp.mpf("1.08")
    order = mp.log(abs(d2 / d1)) / mp.log(h2 / h1) if d1 != 0 else mp.nan
    return {"deficit": deficit, "c3": c3, "order": order,
            "grid_defs": [str(x) for x in defs]}


def main() -> int:
    print("=" * 88)
    print("GAP-A-4: A=3 Δ_λ magnitude from the COORDINATION-EDGE structure "
          "(not the tower level)")
    print(f"  q₀={float(q0):.8f}  h={float(H):.6f}  E₀={float(E0):.6f} MeV")
    print(f"  edge ratio |E(K₃)|/|E(P₃)| = C(3,2)/(3-1) = 3/2 = 1.500  (forward, 0-fit)")
    print(f"  needed r* = μ₃/c₃(path) = 0.4708/0.297 = {0.4708/0.297:.4f}")
    print("=" * 88)

    MU3 = mp.mpf("0.4708")
    C3_PATH_REF = mp.mpf("0.297")   # #4364 published H₉ path value

    cands = {"path_P3_2edge": path_word,
             "triangle_K3_3edge": triangle_word,
             "cyclic_S3_symmetric": cyclic_word}
    res = {}
    for name, fn in cands.items():
        m = _measure(name, fn)
        res[name] = m
        ratio_vs_path = m["c3"] / C3_PATH_REF if C3_PATH_REF != 0 else mp.nan
        print(f"\n[{name}]")
        print(f"  deficit        = {mp.nstr(m['deficit'], 8)}")
        print(f"  c₃             = {mp.nstr(m['c3'], 6)} MeV")
        print(f"  measured h-order = {mp.nstr(m['order'], 4)}   "
              f"(#4364 path is O(h⁴); Brunnian ⇒ 4)")
        print(f"  c₃ / c₃(path #4364=0.297) = {mp.nstr(ratio_vs_path, 5)}")
        print(f"  c₃ / μ₃        = {mp.nstr(m['c3'] / MU3, 5)}")

    # ── the edge-count HYPOTHESIS test: does the third bond give ~3/2 at O(h⁴)? ──
    c3_path = res["path_P3_2edge"]["c3"]
    c3_tri = res["triangle_K3_3edge"]["c3"]
    c3_cyc = res["cyclic_S3_symmetric"]["c3"]
    ord_tri = res["triangle_K3_3edge"]["order"]
    ord_cyc = res["cyclic_S3_symmetric"]["order"]

    # edge-count PREDICTION (if b₃ ∝ #edges, and Brunnian preserved):
    edge_pred = (mp.mpf(3) / 2) * c3_path
    print("\n" + "=" * 88)
    print("EDGE-COUNT HYPOTHESIS  (b₃ ∝ #edges ⇒ K₃/P₃ = 3/2 scaling)")
    print(f"  path P₃ (2 edges)      c₃ = {mp.nstr(c3_path,6)} MeV   "
          f"(reproduces #4364 0.297? {abs(c3_path-C3_PATH_REF)<mp.mpf('0.03')})")
    print(f"  3/2 × path (predicted) c₃ = {mp.nstr(edge_pred,6)} MeV   "
          f"vs μ₃={mp.nstr(MU3,5)}  ({mp.nstr(100*(edge_pred-MU3)/MU3,3)}%)")
    print(f"  triangle K₃ (measured) c₃ = {mp.nstr(c3_tri,6)} MeV  order={mp.nstr(ord_tri,4)}")
    print(f"  cyclic  S₃ (measured)  c₃ = {mp.nstr(c3_cyc,6)} MeV  order={mp.nstr(ord_cyc,4)}")

    tri_brunnian = abs(ord_tri - 4) < mp.mpf("0.6")
    cyc_brunnian = abs(ord_cyc - 4) < mp.mpf("0.6")
    tri_matches_edge = abs(c3_tri - edge_pred) / abs(edge_pred) < mp.mpf("0.1") if edge_pred != 0 else False
    cyc_matches_edge = abs(c3_cyc - edge_pred) / abs(edge_pred) < mp.mpf("0.1") if edge_pred != 0 else False

    print("\n  Brunnian order preserved by third bond?  "
          f"triangle: {tri_brunnian} (order {mp.nstr(ord_tri,3)})   "
          f"cyclic: {cyc_brunnian} (order {mp.nstr(ord_cyc,3)})")
    print(f"  measured c₃ matches the 3/2 edge prediction?  "
          f"triangle: {tri_matches_edge}   cyclic: {cyc_matches_edge}")

    # ── verdict ──────────────────────────────────────────────────────────────
    # DERIVATION only if a symmetric word preserves O(h⁴) AND lands ~μ₃ (0-fit).
    lands = [nm for nm, m in res.items()
             if mp.mpf("0.42") < m["c3"] < mp.mpf("0.52")
             and abs(m["order"] - 4) < mp.mpf("0.6")]
    if lands:
        verdict = f"DERIVATION — {lands} lands μ₃ at O(h⁴), 0 fit"
    elif tri_brunnian or cyc_brunnian:
        # a symmetric word stayed Brunnian; check if 3/2 held
        verdict = ("NEAR-MISS(scope-a) — a symmetric 3-edge word preserves O(h⁴) but "
                   "does not land μ₃ (edge-count factor ≠ exact r*)")
    else:
        verdict = ("WALL(scope-a) — adding the third coordination bond BREAKS the "
                   "Brunnian O(h⁴) order-suppression (order drops toward 2), so the "
                   "3/2 edge count does NOT translate to a 3/2 amplitude; braid "
                   "Brunnian-ness is fragile, the coordination-edge reading walls")
    print("\n" + "=" * 88)
    print(f"VERDICT: {verdict}")
    print("  0 free parameters; μ₃ never inverted; nothing wired.")

    witness = {
        "schema": "witness/v1",
        "producer": "computations/deltalambda/brane_tower_level_coordination_edge_probe.py",
        "computation": "brane-tower-level-coordination-edge",
        "description": (
            "GAP-A-4 DERIVE-OR-WALL for the A=3 Δ_λ 3-body magnitude from the "
            "coordination-graph EDGE structure (jet-filtration depth), not the tower "
            "LEVEL. #4364's H₉ word (Δ_A·Δ_B⁻¹)³ uses only 2 of 3 cable-pairs = the "
            "path P₃ (2 edges); the physical triton is K₃ (3 edges). Forward edge ratio "
            "3/2. This probe adds the third (wraparound) bond Δ_C=(1 2)(0 1)(1 2) and "
            "measures whether a symmetric 3-edge word scales the amplitude by ~3/2 at "
            "O(h⁴) (DERIVATION/NEAR-MISS) or breaks the Brunnian order-suppression and "
            "overshoots (WALL). 0 fit; μ₃ only a target; nothing wired. "
            "Verdict: " + verdict
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "free_parameters": 0,
            "q0": str(q0), "h": str(H), "E0_MeV": str(E0),
            "edge_ratio_K3_over_P3": "3/2",
            "needed_r_star": str(MU3 / C3_PATH_REF),
            "dC_convention": "(0 2)=(1 2)(0 1)(1 2) ⇒ Δ_C=Δ_B·Δ_A·Δ_B",
            "note": "μ₃=+0.4708 target only; SAME E₀+y_λ normalization as ρ_F; 0 fit.",
        },
        "results": {
            "candidates": {nm: {"deficit": str(m["deficit"]), "c3_MeV": str(m["c3"]),
                                "measured_h_order": str(m["order"]),
                                "c3_over_mu3": str(m["c3"] / MU3),
                                "grid_deficits": m["grid_defs"]}
                           for nm, m in res.items()},
            "edge_count_hypothesis": {
                "path_c3_MeV": str(c3_path),
                "path_reproduces_4364": bool(abs(c3_path - C3_PATH_REF) < mp.mpf("0.03")),
                "three_halves_prediction_MeV": str(edge_pred),
                "three_halves_pct_vs_mu3": str(100 * (edge_pred - MU3) / MU3),
                "triangle_c3_MeV": str(c3_tri), "triangle_order": str(ord_tri),
                "triangle_brunnian_preserved": bool(tri_brunnian),
                "triangle_matches_3half_pred": bool(tri_matches_edge),
                "cyclic_c3_MeV": str(c3_cyc), "cyclic_order": str(ord_cyc),
                "cyclic_brunnian_preserved": bool(cyc_brunnian),
                "cyclic_matches_3half_pred": bool(cyc_matches_edge),
            },
            "verdict": {
                "classification": verdict,
                "is_fit": False, "wired": False, "free_param_count": 0,
                "mu3_inverted": False,
            },
        },
        "scriptCommitSha": "uncommitted",
    }
    out = HERE / "brane-tower-level-coordination-edge.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=2))
    print(f"\nwitness -> {out.relative_to(_COMP.parent)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
