#!/usr/bin/env python3
"""s5so3_wlambda_borromean_lift_probe.py — Route-1 DERIVE-OR-WALL for the A=3
Δ_λ residual 1.6× via the s5-so3 keystone W_λ re-weight.

The gap #4364 left
------------------
#4364 (`borromean_h9_magnitude_lift_probe.py`, `BorromeanMagnitudeLift.lean`)
lifted the DERIVED A=3 Borromean 3-body cluster to the H₉ joint-trace level via
faithful width-3 cabling and reached v_y = +0.297 MeV = 0.63× μ₃ (μ₃ = +0.4708),
measured O(h⁴), 0 fit — a ~1.6× NEAR-MISS.  Its `lift_is_coefficient_ratio`
theorem proves a level lift is a pure coefficient rescale (the shared h⁴
cancels), so the residual 1.6× is a COEFFICIENT question.

The Route-1 hypothesis (this probe)
-----------------------------------
The H₉ joint trace ρ_F normalizes the Wedderburn blocks λ⊢9 with the PRODUCTION
weight y_λ (Wenzl principal specialization s_λ(1,q,q²,…), `y_lambda_at`).  The
s5-so3 keystone (docs/coordination/s5-so3-keystone.md) posits a DIFFERENT,
geometrically-derived block weight — the Ocneanu / q-Plancherel measure

    W_λ = d_q(λ)² / [n]_q!   (balanced [m]_q = (q^m−q^−m)/(q−q^−1),  Σ_{λ⊢n} W_λ = 1),

via the hook-length form  W_λ = [n]_q! / ∏_cells [hook]_q²  (identical:
d_q(λ) = [n]_q!/∏[hook]_q, the q-hook-length formula).

Re-weighting the SAME cabled-Borromean cluster y_λ → W_λ is — by the same
argument as `lift_is_coefficient_ratio` — a COEFFICIENT rescale r = κ_W/κ_y of
the O(h⁴) cluster.  Route 1 closes iff the DERIVED ratio r = c₃(W_λ)/c₃(y_λ)
equals the needed μ₃/v_y ≈ 1.585.

STRICT anti-fit
---------------
W_λ is fixed by q₀ + the partition hook-lengths — 0 free parameters, NEVER
inverted from μ₃/AME/CODATA.  μ₃ = +0.4708 enters ONLY as the target.  Same E₀,
same characters |χ_λ|, same cabled Borromean word (Δ_A·Δ_B⁻¹)³ as #4364 — the
ONLY change is the block-weight system y_λ → W_λ.  If the derived r lands ≈1.585
0-fit → DERIVATION lead; if not → honest WALL (residual stays a coefficient
question; NOT tuned to μ₃).  "No seventh fit-based ansatz" + PROBE-4 KL-prune
stand.  Nothing wired.
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

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps(30)
HERE = _Path(__file__).resolve().parent
q0 = mp.mpf(str(Q0))
q0f = float(Q0)
H = q0 - 1 / q0                                   # Hecke h = q − q⁻¹
E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))       # SAME E₀ as ρ_F / #4364

# ── block weights: production y_λ (control) and keystone W_λ (Route 1) ─────────
_Y9 = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
       for k, v in y_lambda_at(9, q0).items()}


def _q_int(m: int, q: mp.mpf) -> mp.mpf:
    """Balanced quantum integer [m]_q = (q^m − q^−m)/(q − q^−1)."""
    return (q ** m - q ** (-m)) / (q - 1 / q)


def _hook_lengths(lam: tuple) -> list[int]:
    conj = [sum(1 for row in lam if row > j) for j in range(lam[0])]
    hooks = []
    for i, row in enumerate(lam):
        for j in range(row):
            hooks.append((row - 1 - j) + (conj[j] - 1 - i) + 1)
    return hooks


def _W_lambda(lam: tuple, q: mp.mpf) -> mp.mpf:
    """Ocneanu / q-Plancherel weight  W_λ = [n]_q! / ∏_cells [hook]_q²
    = d_q(λ)²/[n]_q!  (balanced q-integers).  0 free parameters."""
    n = sum(lam)
    qfact = mp.mpf(1)
    for m in range(1, n + 1):
        qfact *= _q_int(m, q)
    prod_hooks_sq = mp.mpf(1)
    for h in _hook_lengths(lam):
        prod_hooks_sq *= _q_int(h, q) ** 2
    return qfact / prod_hooks_sq


_W9 = {sh: _W_lambda(sh, q0) for sh in _Y9}
# q-Plancherel normalization self-check (Σ_λ W_λ = 1) — a derivation guard.
_W9_SUM = sum(_W9.values())


def _characters(word):
    """The per-block characters χ_λ(word) for all λ⊢9 — the SAME machinery
    #4364 uses (`chi_q_atomic_all_partitions`, kernel gen index 1-based)."""
    factors = [(float(c), float(d), int(g) + 1) for (c, d, g) in word]
    cp = pyhecke_native.chi_q_atomic_all_partitions(9, factors, q0f)
    return {tuple(s): mp.mpf(str(chi)) for s, chi in cp}


def _perblock(word, weight):
    """g(word) = Σ_{λ⊢9} weight_λ · |χ_λ(word)|  for a given weight dict."""
    chars = _characters(word)
    return sum(weight[s] * abs(chi) for s, chi in chars.items() if s in weight)


# ── canonical width-3 cabled Borromean inter word (0 params) — copied verbatim
#    from #4364 borromean_h9_magnitude_lift_probe.py (level FIXED, no divergence)
def _block_transposition(a: int, w: int = 3):
    gens = []
    for r in range(w):
        for g in range(a + w - 1 + r, a - 1 + r, -1):
            gens.append(g)
    return gens


def borromean_inter_word():
    """inter_Borr = (Δ_A · Δ_B⁻¹)³ as (c,d,gen) triples (0 free params)."""
    dA = _block_transposition(0)          # cables 0,1 : gens 0..4
    dB = _block_transposition(3)          # cables 1,2 : gens 3..7
    dB_inv = [g for g in reversed(dB)]
    word = []
    for _ in range(3):
        word += [(1.0, 0.0, g) for g in dA]
        word += [(1.0, float(-H), g) for g in dB_inv]
    return word


def _cluster(weight):
    """The atom-dressed A=3 Borromean cluster c₃ = E₀·(g_intra − g_intra+Borr),
    mean over (T, ³He), at a given block weight.  SAME intra / inter as #4364."""
    inter = borromean_inter_word()
    per = {}
    for name, (Z, N) in {"T": (1, 2), "3He": (2, 1)}.items():
        full = atom_braid_word_3A(Z, N, include_inter=True)
        intra = [x for x in full if x[2] % 3 != 2]
        g0 = _perblock(intra, weight)
        gB = _perblock(intra + inter, weight)
        per[name] = E0 * (g0 - gB)
    mean = (per["T"] + per["3He"]) / 2
    return mean, per


def main() -> int:
    print("=" * 86)
    print("Route 1 — s5-so3 keystone W_λ re-weight of the A=3 Borromean H₉ cluster")
    print(f"  q₀={float(q0):.8f}  h={float(H):.6f}  E₀={float(E0):.6f} MeV   "
          f"Σ_λ W_λ = {mp.nstr(_W9_SUM, 12)}  (q-Plancherel guard → 1)")
    print("=" * 86)

    MU3 = mp.mpf("0.4708")
    V_Y_REF = mp.mpf("0.297")          # #4364 published y_λ cluster value

    # ── control: reproduce #4364 with production y_λ ──────────────────────────
    c3_y, per_y = _cluster(_Y9)
    print("\n(control) production y_λ weight  (should reproduce #4364 v_y ≈ 0.297)")
    print(f"  c₃(y_λ) T={mp.nstr(per_y['T'],6)}  ³He={mp.nstr(per_y['3He'],6)}  "
          f"mean = {mp.nstr(c3_y,6)} MeV")

    # ── Route 1: keystone W_λ = d_q²/[n]_q! q-Plancherel weight ────────────────
    c3_W, per_W = _cluster(_W9)
    print("\n(Route 1) keystone W_λ = d_q(λ)²/[n]_q! (Ocneanu / q-Plancherel) weight")
    print(f"  c₃(W_λ) T={mp.nstr(per_W['T'],6)}  ³He={mp.nstr(per_W['3He'],6)}  "
          f"mean = {mp.nstr(c3_W,6)} MeV  sign = {'+' if c3_W > 0 else '-'}")

    # ── the derived re-weight ratio r = c₃(W_λ)/c₃(y_λ) vs the needed 1.585 ────
    r_derived = c3_W / c3_y if c3_y != 0 else mp.inf
    r_needed = MU3 / c3_y if c3_y != 0 else mp.inf
    r_needed_ref = MU3 / V_Y_REF
    print("\n" + "=" * 86)
    print("DERIVED re-weight ratio  r = c₃(W_λ) / c₃(y_λ)   (0 free params)")
    print(f"  r_derived  = {mp.nstr(r_derived,6)}")
    print(f"  r_needed   = μ₃ / c₃(y_λ)          = {mp.nstr(r_needed,6)}")
    print(f"  r_needed   = μ₃ / v_y(#4364=0.297) = {mp.nstr(r_needed_ref,6)}")
    print(f"  c₃(W_λ)                            = {mp.nstr(c3_W,6)} MeV")
    print(f"  c₃(W_λ) / μ₃                       = {mp.nstr(c3_W/MU3,6)}   "
          f"(~{mp.nstr(MU3/c3_W if c3_W!=0 else mp.inf,4)}× "
          f"{'short of' if abs(c3_W)<MU3 else 'past'} +0.4708)")

    # ── verdict ───────────────────────────────────────────────────────────────
    lands = mp.mpf("0.42") < c3_W < mp.mpf("0.52")     # clean landing ±10%
    near = mp.mpf("0.20") < c3_W < mp.mpf("0.80")      # right order
    improves = abs(c3_W - MU3) < abs(c3_y - MU3)       # closer than y_λ?
    if lands:
        verdict = "DERIVATION LEAD — W_λ re-weight closes the A=3 Δ_λ residual 0-fit"
    elif near and improves:
        verdict = "PARTIAL LEAD — W_λ re-weight improves toward μ₃, does not close (0-fit)"
    elif near:
        verdict = "WALL(scope-a) — W_λ re-weight same order, no closer than y_λ (0-fit)"
    else:
        verdict = "WALL(scope-a) — W_λ re-weight ≠ target order; magnitude source open (0-fit)"
    print("\n" + "=" * 86)
    print(f"VERDICT: {verdict}")
    print(f"  y_λ cluster  = {mp.nstr(c3_y,5)} MeV = {mp.nstr(c3_y/MU3,4)}× μ₃")
    print(f"  W_λ cluster  = {mp.nstr(c3_W,5)} MeV = {mp.nstr(c3_W/MU3,4)}× μ₃")
    print(f"  needed ratio r* ≈ {mp.nstr(r_needed_ref,5)}   derived r = {mp.nstr(r_derived,5)}")
    print("  W_λ, y_λ both fixed by q₀ + hook-lengths — 0 fit, μ₃ never inverted, nothing wired.")

    witness = {
        "schema": "witness/v1",
        "producer": "computations/deltalambda/s5so3_wlambda_borromean_lift_probe.py",
        "computation": "s5so3-wlambda-borromean-lift-route1",
        "description": (
            "Route-1 DERIVE-OR-WALL for the A=3 Δ_λ residual 1.6× left by #4364. "
            "The H₉ joint trace ρ_F weights blocks λ⊢9 with production y_λ (Wenzl "
            "principal spec), giving the #4364 cabled-Borromean cluster c₃(y_λ) = "
            f"{mp.nstr(c3_y,6)} MeV = {mp.nstr(c3_y/MU3,4)}× μ₃. This probe forward-"
            "evaluates the s5-so3 keystone weight W_λ = d_q(λ)²/[n]_q! (Ocneanu / "
            "q-Plancherel, hook-length form [n]_q!/∏[hook]_q², balanced q-integers, "
            f"Σ_λ W_λ = {mp.nstr(_W9_SUM,10)}) as the block weight on the SAME cabled "
            "Borromean word (Δ_A·Δ_B⁻¹)³, SAME E₀, SAME |χ_λ|. Only the weight system "
            f"changes. Result: c₃(W_λ) = {mp.nstr(c3_W,6)} MeV = {mp.nstr(c3_W/MU3,4)}× "
            f"μ₃; derived re-weight ratio r = c₃(W_λ)/c₃(y_λ) = {mp.nstr(r_derived,5)} "
            f"vs the needed r* = μ₃/v_y ≈ {mp.nstr(r_needed_ref,5)}. VERDICT: {verdict}. "
            "0 free params; W_λ + y_λ both fixed by q₀ + hook-lengths; μ₃ target only, "
            "never inverted; nothing wired."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "free_parameters": 0,
            "q0": str(q0), "h": str(H), "E0_MeV": str(E0),
            "level": "H₉ perblock Σ_{λ⊢9} weight_λ·|χ_λ|, three width-3 nucleon cables",
            "inter_word": "(Δ_A·Δ_B⁻¹)³ cabled Borromean (identical to #4364)",
            "weights_compared": {
                "y_lambda": "Wenzl principal specialization s_λ(1,q,q²,…) — production ρ_F weight",
                "W_lambda": "Ocneanu / q-Plancherel d_q(λ)²/[n]_q! = [n]_q!/∏[hook]_q² — s5-so3 keystone",
            },
            "note": "μ₃=+0.4708 target only; SAME E₀+word+characters as #4364; ONLY weight changes; 0 fit.",
        },
        "results": {
            "q_plancherel_norm_sum": str(_W9_SUM),
            "y_lambda_cluster": {
                "c3_T_MeV": str(per_y["T"]), "c3_3He_MeV": str(per_y["3He"]),
                "c3_mean_MeV": str(c3_y), "c3_over_mu3": str(c3_y / MU3),
            },
            "W_lambda_cluster": {
                "c3_T_MeV": str(per_W["T"]), "c3_3He_MeV": str(per_W["3He"]),
                "c3_mean_MeV": str(c3_W), "sign": "+" if c3_W > 0 else "-",
                "c3_over_mu3": str(c3_W / MU3),
                "shortfall_factor_vs_mu3": str(MU3 / c3_W if c3_W != 0 else "inf"),
            },
            "reweight_ratio": {
                "r_derived_cW_over_cY": str(r_derived),
                "r_needed_mu3_over_cY": str(r_needed),
                "r_needed_mu3_over_vY_ref": str(r_needed_ref),
                "closes": bool(lands),
                "improves_over_y_lambda": bool(improves),
                "right_order": bool(near),
            },
            "verdict": {
                "classification": verdict,
                "is_fit": False,
                "wired": False,
                "free_param_count": 0,
                "mu3_inverted": False,
                "delta_lambda_status": (
                    "A=3 residual: W_λ re-weight forward-evaluated 0-fit; "
                    "closure per the classification above."
                ),
                "anti_fit": (
                    "W_λ + y_λ both derived from q₀ + hook-lengths; only the weight "
                    "system changed (level/word/E₀/characters identical to #4364); μ₃ "
                    "never inverted; no weight tuned to hit +0.4708; nothing wired."
                ),
            },
        },
        "scriptCommitSha": "uncommitted",
    }
    out = HERE / "s5so3-wlambda-borromean-lift.witness.json"
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
