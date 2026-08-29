#!/usr/bin/env python3
"""s5so3_geometric_wlambda_borromean_lift_probe.py — the GENUINE geometric (Beasley–
Witten / WRT(S³/2I)) keystone W_λ = d_q²/D² re-weight of the A=3 Borromean H₉ cluster.

Distinct angle on Route 1 vs the sibling s5so3_wlambda_borromean_lift_probe.py
-----------------------------------------------------------------------------
The sibling re-weighted with the q-Plancherel PROXY  W_raw = d_q(λ)²/[n]_q!  and got
r_raw = c₃(W_raw)/c₃(y_λ) = 52.62 (33× overshoot, WALL).  But at q₀ > 1 (growth regime)
  Σ_λ d_q²/[n]_q! = D²/[n]_q! = 1.1109 ≠ 1  — so d_q²/[n]_q! is NOT a probability measure.

The corpus's own WLambdaMTCLocalizationObligation.lean states the genuine Beasley–Witten
/ RT localization weight on S³/2I is
  W_geom = d_q(λ)² / D²,   D² = Σ_{λ⊢n} d_q(λ)²   (⇒ Σ_λ W_geom = 1, the C1 normalization,
  "the genuine Plancherel normaliser, NOT [n]_q!").
i.e. W_geom = W_raw / S with S = D²/[n]_q!.  Since the cluster is LINEAR in the weight,
  r_geom = r_raw / S.

This probe forward-evaluates ALL THREE weightings (production y_λ, sibling W_raw, genuine
W_geom) on the IDENTICAL #4364 cabled-Borromean word (Δ_A·Δ_B⁻¹)³, SAME E₀, SAME |χ_λ|.
Only the weight system changes.  0 free parameters; μ₃/AME/CODATA never inverted.

STRICT anti-fit
---------------
W_geom is fixed by q₀ + hook-lengths (0 fit).  μ₃ = +0.4708 enters ONLY as the target.
The probe ALSO records the DECLINED fit-trap: Σ y_λ = 0.0318 ≠ 1, so rescaling y_λ to
Σ=1 (c ≈ 31.5) lands r near 1.585 — that rescale is a μ₃-inverted free parameter = a FIT,
declined.  If the genuine r_geom lands ≈1.585 0-fit → DERIVATION lead; else → honest WALL.
Nothing wired.  "No seventh fit-based ansatz" + PROBE-4 KL-prune stand.
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
H = q0 - 1 / q0
E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))       # SAME E₀ as ρ_F / #4364


# ── block weights ─────────────────────────────────────────────────────────────
def _q_int(m: int, q: mp.mpf) -> mp.mpf:
    return (q ** m - q ** (-m)) / (q - 1 / q)


def _hook_lengths(lam: tuple) -> list[int]:
    conj = [sum(1 for row in lam if row > j) for j in range(lam[0])]
    hooks = []
    for i, row in enumerate(lam):
        for j in range(row):
            hooks.append((row - 1 - j) + (conj[j] - 1 - i) + 1)
    return hooks


def _dq(lam: tuple, q: mp.mpf) -> mp.mpf:
    """q-hook-length quantum dimension d_q(λ) = [n]_q!/∏_cells [hook]_q (balanced)."""
    n = sum(lam)
    qfact = mp.mpf(1)
    for m in range(1, n + 1):
        qfact *= _q_int(m, q)
    ph = mp.mpf(1)
    for h in _hook_lengths(lam):
        ph *= _q_int(h, q)
    return qfact / ph


_Y9 = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
       for k, v in y_lambda_at(9, q0).items()}
_DQSQ9 = {sh: _dq(sh, q0) ** 2 for sh in _Y9}

_QFACT9 = mp.mpf(1)
for _m in range(1, 10):
    _QFACT9 *= _q_int(_m, q0)
_D2 = sum(_DQSQ9.values())                          # D² = Σ_λ d_q²  (genuine normaliser)

_W_RAW9 = {sh: _DQSQ9[sh] / _QFACT9 for sh in _Y9}          # sibling  d_q²/[n]_q!  (Σ=1.111)
_W_GEOM9 = {sh: _DQSQ9[sh] / _D2 for sh in _Y9}            # genuine BW  d_q²/D²   (Σ=1)

_S_RAW = sum(_W_RAW9.values())                       # = D²/[n]_q!  (the correction factor)
_S_GEOM = sum(_W_GEOM9.values())                     # = 1 (guard)
_S_Y = sum(_Y9.values())                             # Σ y_λ (= 0.0318, NOT 1)


def _characters(word):
    factors = [(float(c), float(d), int(g) + 1) for (c, d, g) in word]
    cp = pyhecke_native.chi_q_atomic_all_partitions(9, factors, q0f)
    return {tuple(s): mp.mpf(repr(chi)) for s, chi in cp}


def _perblock(word, weight):
    chars = _characters(word)
    return sum(weight[s] * abs(chi) for s, chi in chars.items() if s in weight)


# ── canonical width-3 cabled Borromean inter word (verbatim from #4364) ────────
def _block_transposition(a: int, w: int = 3):
    gens = []
    for r in range(w):
        for g in range(a + w - 1 + r, a - 1 + r, -1):
            gens.append(g)
    return gens


def borromean_inter_word():
    dA = _block_transposition(0)
    dB = _block_transposition(3)
    dB_inv = [g for g in reversed(dB)]
    word = []
    for _ in range(3):
        word += [(1.0, 0.0, g) for g in dA]
        word += [(1.0, float(-H), g) for g in dB_inv]
    return word


def _cluster(weight):
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
    print("=" * 90)
    print("GENUINE geometric W_λ = d_q²/D² (Beasley–Witten / WRT(S³/2I)) re-weight — A=3 H₉")
    print(f"  q₀={float(q0):.8f}  h={float(H):.6f}  E₀={float(E0):.6f} MeV")
    print(f"  Σ y_λ = {mp.nstr(_S_Y,8)} (NOT 1)   Σ d_q²/[n]_q! = {mp.nstr(_S_RAW,10)} (sibling, NOT 1)"
          f"   Σ d_q²/D² = {mp.nstr(_S_GEOM,10)} (genuine → 1)")
    print(f"  D² = Σd_q² = {mp.nstr(_D2,8)}   [9]_q! = {mp.nstr(_QFACT9,8)}   "
          f"D²/[9]_q! = {mp.nstr(_D2/_QFACT9,10)}")
    print("=" * 90)

    MU3 = mp.mpf("0.4708")

    c3_y, per_y = _cluster(_Y9)
    c3_raw, per_raw = _cluster(_W_RAW9)
    c3_geom, per_geom = _cluster(_W_GEOM9)

    r_raw = c3_raw / c3_y
    r_geom = c3_geom / c3_y
    r_needed = MU3 / c3_y
    # normalization guard: r_geom should equal r_raw / S_RAW
    r_geom_via_S = r_raw / _S_RAW

    print(f"\n  c₃(y_λ  production, Σ={mp.nstr(_S_Y,4)}) = {mp.nstr(c3_y,6)} MeV = {mp.nstr(c3_y/MU3,4)}× μ₃")
    print(f"  c₃(d_q²/[n]_q!  sibling, Σ={mp.nstr(_S_RAW,5)}) = {mp.nstr(c3_raw,6)} MeV = {mp.nstr(c3_raw/MU3,4)}× μ₃")
    print(f"  c₃(d_q²/D²  GENUINE BW, Σ=1) = {mp.nstr(c3_geom,6)} MeV = {mp.nstr(c3_geom/MU3,4)}× μ₃")
    print(f"\n  r_raw  = c₃(sibling)/c₃(y_λ) = {mp.nstr(r_raw,6)}")
    print(f"  r_geom = c₃(genuine)/c₃(y_λ) = {mp.nstr(r_geom,6)}   (= r_raw/S = {mp.nstr(r_geom_via_S,6)}, guard)")
    print(f"  r*needed = μ₃/c₃(y_λ)        = {mp.nstr(r_needed,6)}")

    # ── declined fit-trap: put BOTH weights on Σ=1 (normalize y_λ up by 1/Σy_λ) ──
    #    r_both = c₃(geom,Σ=1)/c₃(y/Σy_λ) = r_geom·Σy_λ.  Reaches 1.506 (5% miss), and is
    #    a normalization-convention choice ρ_F does not make (it uses raw y_λ) ⇒ NOT a derivation.
    r_both_normalized = r_geom * _S_Y
    c_normalize_y = 1 / _S_Y
    c_exact_close = MU3 / (r_geom * c3_y)   # the c that would close EXACTLY (μ₃-inverted ⇒ FIT)
    print(f"\n  [declined fit-trap] both-Σ=1 ratio r_both = r_geom·Σy_λ = {mp.nstr(r_both_normalized,6)}"
          f"  ({mp.nstr((r_needed - r_both_normalized)/r_needed*100,3)}% short of r*={mp.nstr(r_needed,5)})")
    print(f"     needs normalizing y_λ up by 1/Σy_λ = {mp.nstr(c_normalize_y,6)} — a convention ρ_F does NOT use;")
    print(f"     exact closure needs c = μ₃/(r_geom·c₃_y) = {mp.nstr(c_exact_close,6)} (μ₃-inverted ⇒ FIT). DECLINED.")

    lands = mp.mpf("0.42") < c3_geom < mp.mpf("0.52")
    near = mp.mpf("0.20") < c3_geom < mp.mpf("0.80")
    if lands:
        verdict = "DERIVATION LEAD — genuine geometric W_λ closes the A=3 Δ_λ residual 0-fit"
    elif near:
        verdict = "WALL(scope-a) — genuine geometric W_λ same order as y_λ, not closing (0-fit)"
    else:
        verdict = "WALL(scope-a) — genuine geometric W_λ (d_q²/D²) ≠ target order (overshoots); A=3 magnitude source open (0-fit)"

    print("\n" + "=" * 90)
    print(f"VERDICT: {verdict}")
    print("  W_geom fixed by q₀ + hook-lengths — 0 fit; μ₃ never inverted; nothing wired.")
    print("  No OTHER geometric W_λ to try: self-duality S⁴=1 (2026-07-17) + framing-collapse")
    print("  (2026-07-12) ⇒ d_q²/D² IS the geometric measure; the route converges on this wall.")

    witness = {
        "schema": "witness/v1",
        "producer": "computations/deltalambda/s5so3_geometric_wlambda_borromean_lift_probe.py",
        "computation": "s5so3-geometric-wlambda-borromean-lift",
        "description": (
            "GENUINE geometric (Beasley-Witten / WRT(S3/2I)) keystone W_lambda = d_q^2/D^2 "
            "re-weight of the A=3 Borromean H9 cluster (distinct angle on Route 1 vs sibling "
            "d_q^2/[n]_q!). D^2 = Sum_lambda d_q^2 is the genuine Plancherel normaliser "
            "(WLambdaMTCLocalizationObligation.lean: 'NOT [n]_q!'); Sum_lambda d_q^2/D^2 = 1 "
            "exactly (C1), whereas the sibling's d_q^2/[n]_q! sums to 1.1109 (not a probability "
            "measure). Forward-evaluated on the IDENTICAL #4364 cabled-Borromean word "
            "(Delta_A*Delta_B^-1)^3, same E0, same |chi_lambda|; only the weight system changes. "
            f"Result: c3(genuine) = {mp.nstr(c3_geom,6)} MeV = {mp.nstr(c3_geom/MU3,4)}x mu3; "
            f"r_geom = {mp.nstr(r_geom,6)} = r_raw/S ({mp.nstr(r_raw,6)}/{mp.nstr(_S_RAW,6)}), vs "
            f"needed r* = {mp.nstr(r_needed,6)}. The correct normaliser (D^2 not [n]_q!) shifts "
            "the number 11% but not the verdict. VERDICT: " + verdict + ". 0 free params; W_geom "
            "+ y_lambda fixed by q0 + hook-lengths; mu3 target only, never inverted; nothing wired. "
            "Declined fit-trap: rescaling y_lambda to Sum=1 (c~31.5) lands r~1.585 but is a "
            "mu3-inverted free parameter = a FIT, declined."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "free_parameters": 0,
            "q0": str(q0), "h": str(H), "E0_MeV": str(E0),
            "level": "H9 perblock Sum_{lambda|-9} weight_lambda*|chi_lambda|, three width-3 cables",
            "inter_word": "(Delta_A*Delta_B^-1)^3 cabled Borromean (identical to #4364)",
            "D2_sum_dq2": str(_D2),
            "qfact_9": str(_QFACT9),
            "sum_y_lambda": str(_S_Y),
            "sum_dq2_over_qfact_sibling": str(_S_RAW),
            "sum_dq2_over_D2_genuine": str(_S_GEOM),
            "note": "mu3=+0.4708 target only; SAME E0+word+characters as #4364; ONLY weight changes; 0 fit.",
        },
        "results": {
            "y_lambda_cluster": {
                "c3_T_MeV": str(per_y["T"]), "c3_3He_MeV": str(per_y["3He"]),
                "c3_mean_MeV": str(c3_y), "c3_over_mu3": str(c3_y / MU3),
            },
            "sibling_raw_cluster_dq2_over_qfact": {
                "c3_mean_MeV": str(c3_raw), "c3_over_mu3": str(c3_raw / MU3),
                "r_over_y": str(r_raw),
            },
            "genuine_geometric_cluster_dq2_over_D2": {
                "c3_T_MeV": str(per_geom["T"]), "c3_3He_MeV": str(per_geom["3He"]),
                "c3_mean_MeV": str(c3_geom), "sign": "+" if c3_geom > 0 else "-",
                "c3_over_mu3": str(c3_geom / MU3),
            },
            "reweight_ratio": {
                "r_geom_derived": str(r_geom),
                "r_geom_via_S_guard": str(r_geom_via_S),
                "r_raw_sibling": str(r_raw),
                "S_correction_factor": str(_S_RAW),
                "r_needed_mu3_over_cY": str(r_needed),
                "closes": bool(lands),
                "right_order": bool(near),
            },
            "declined_fit_trap": {
                "r_both_normalized_r_geom_times_sum_y": str(r_both_normalized),
                "pct_short_of_needed": str((r_needed - r_both_normalized) / r_needed * 100),
                "one_over_sum_y_lambda": str(c_normalize_y),
                "c_exact_close_mu3_inverted": str(c_exact_close),
                "is_fit": True, "declined": True,
                "reason": "both-Sigma=1 ratio r_geom*Sum_y = 1.506 is a 5% miss AND a normalization "
                          "convention rho_F does not make (rho_F uses raw y_lambda); exact closure needs "
                          "a mu3-inverted rescale = a FIT. Neither is a derivation.",
            },
            "verdict": {
                "classification": verdict,
                "is_fit": False, "wired": False, "free_param_count": 0, "mu3_inverted": False,
                "corrects_sibling": "r_raw=52.62 used d_q^2/[n]_q! (Sum=1.111, not a measure); "
                                    "genuine d_q^2/D^2 (Sum=1) gives r_geom=47.37 — verdict unchanged (WALL)",
                "no_other_geometric_wlambda": "self-duality S^4=1 (2026-07-17) + framing-collapse "
                                              "(2026-07-12) => d_q^2/D^2 IS the geometric measure; route converges on this wall",
                "anti_fit": "W_geom + y_lambda derived from q0 + hook-lengths; only the weight system "
                            "changed (level/word/E0/characters identical to #4364); mu3 never inverted; nothing wired.",
            },
        },
        "scriptCommitSha": "uncommitted",
    }
    out = HERE / "s5so3-geometric-wlambda-borromean-lift.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False))
    print(f"\nwitness → {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
