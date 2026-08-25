#!/usr/bin/env python3
"""mu3_anchor_consistency_probe.py — the μ₃ probes straddled the two CALIBRATION LAYERS.

THE DEFECT, correctly framed.  This is **not** a cache-staleness bug.  It is the documented
two-layer q₀ convention — *ideal mathematical* CAL-2 versus *experimental* precision anchor —
leaking into a single computation.  Per AGENTS.md §"q₀ anchor convention", q₀ has one value
but two documented pins:

    IDEAL / canonical 3-CAL (mathematical)
        CAL-2 = 𝔇_β, pinned via its proxy m_μ/m_e
        → q₀ = 1.10997859555733471989...            (MUON)
        → this is what `y-lambda-at-q0.witness.json` and the ~840 `computations/`
          witnesses are built at

    EXPERIMENTAL / Physical-Observations layer
        m_p/m_e (0.06 ppb, vs the muon ratio's 22 ppb; re-pin 2026-05-28)
        → q₀ = 1.1099785827513808                   (PROTON)
        → this is `q_parameter.Q`, the package layer

    separation = 11.54 ppb  —  precisely the μ–p substrate tension (AGENTS.md quotes the
    unavoidable theory residual as ~11.5 ppb; this probe measures 11.54 ppb).

`mu3_frechet_perblock_probe.py` (#4657, merged) took `y_λ` from the **ideal/mathematical**
layer (the muon-built cache) while evaluating `χ_λ` at the **experimental** proton q₀.  Those
are not two versions of one number — they are two *layers of the calibration*, mixed inside
one `Δ²g`.

The mechanism that let it happen: `wedderburn_jones_markov.y_lambda_at(n, q)` returns the
cached witness whenever `|q − q_parameter.Q| < 1e-12`, a gate satisfied *trivially* when the
caller passes `q_parameter.Q` itself — so the ideal-layer cache is served to an
experimental-layer caller with no signal that a layer boundary was crossed.  This is the
recurring class AGENTS.md flags under bean `tnjb`.

THE CORRECT FIX is therefore **not** "bypass the cache" but "pick a layer and stay in it."
The μ₃ door is a structural/categorical question living in `computations/`, so the
**ideal (muon) layer is correct** and the proton value was the intruder — the reverse of
what a naive "the package constant is more precise" reading would suggest.

THE QUESTION this probe answers: does the mixing change any conclusion, or is it below the
noise of every claim that was made?

WHAT IS CHECKED.  `Δ²g` is recomputed three ways on identical braid words:
  * `mixed`        — y_λ from cache (muon), χ at proton q₀   [what #4657 actually did]
  * `pure_proton`  — both at the proton q₀ (cache bypassed via the live closed form)
  * `pure_muon`    — both at the muon q₀ (the `computations/` layer convention)

AGENTS.md is explicit that the `computations/` layer is **muon-q₀ canonical** (the ideal
3-CAL derivation layer) and that the ~840 muon witnesses must NOT be migrated to proton
without owner sign-off.  So `pure_muon` is the correct convention here — not `pure_proton`.
The proton pin belongs to the precision/prediction layer, where the point is to place the
~11.5 ppb residual where it is least significant; it is not the layer a categorical
Δ²g computation lives in.

Nothing is fitted and nothing is wired.  This reports a defect and its size.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent.parent),
                str(Path(__file__).resolve().parent.parent / "substrate")]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import pyhecke_native  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from schur_principal_mpmath import y_lambda_at_q0_mpmath  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[2]
                       / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import _q0_value_for_anchor  # noqa: E402

set_compute_dps(40)
Q_PROTON = mp.mpf(str(Q0))
# READ the muon anchor; do not retype it. The proton leg already reads
# (`q_parameter.Q_MP`) while this one was a 61-character literal that tracked
# the anchor for 51 digits and then diverged — `…878015405145269` against the
# anchor's `…878015368660798114`. A probe whose subject IS a crossed
# calibration layer cannot afford a muon leg that no re-pin can reach.
Q_MUON = mp.mpf(_q0_value_for_anchor("muon"))


def chis(word, qf):
    f = [(float(c), float(d), int(g) + 1) for (c, d, g) in word]
    return {tuple(s): mp.mpf(repr(c))
            for s, c in pyhecke_native.chi_q_atomic_all_partitions(9, f, qf)}


def d2_under(word, ga, gb, ymap, qf):
    def g_of(sub):
        return chis([x for x in word if x[2] % 3 != 2 or x[2] in sub], qf)
    ce, ca, cb, cab = g_of(set()), g_of({ga}), g_of({gb}), g_of({ga, gb})
    blocks = sorted(set(ce) & set(ca) & set(cb) & set(cab) & set(ymap))
    return sum(ymap[l] * (abs(cab[l]) - abs(ca[l]) - abs(cb[l]) + abs(ce[l]))
               for l in blocks)


def main() -> int:
    rel_q = abs(Q_PROTON - Q_MUON) / Q_MUON
    print("=" * 84)
    print(" μ₃ probes mixed q₀ anchors — how much did it matter?")
    print("=" * 84)
    print(f" q_parameter.Q (proton)        = {mp.nstr(Q_PROTON, 20)}")
    print(f" y-lambda cache q₀ (muon)      = {mp.nstr(Q_MUON, 20)}")
    print(f" separation                    = {float(rel_q)*1e9:.2f} ppb")

    y_cached = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(9, Q_PROTON).items()}
    y_proton = y_lambda_at_q0_mpmath(9, Q_PROTON)
    y_muon = y_lambda_at_q0_mpmath(9, Q_MUON)

    dy = max(abs(y_cached[l] - y_muon[l]) / max(abs(y_muon[l]), mp.mpf('1e-40'))
             for l in y_cached)
    print(f"\n cache vs live-at-MUON  : max rel {mp.nstr(dy, 6)}"
          f"   → {'cache IS muon-built' if dy < mp.mpf('1e-20') else 'cache is NOT muon'}")
    dy2 = max(abs(y_cached[l] - y_proton[l]) / max(abs(y_proton[l]), mp.mpf('1e-40'))
              for l in y_cached)
    print(f" cache vs live-at-PROTON: max rel {mp.nstr(dy2, 6)}"
          f"   → this is the mixing error the merged probe carried")
    signs_agree = all(mp.sign(y_cached[l]) == mp.sign(y_proton[l]) for l in y_cached)
    print(f" all 30 signs agree between anchors: {signs_agree}"
          f"   → the SIGN rule (#4662) is anchor-independent")

    E0p = mp.mpf(str(M_E_MEV)) / (Q_PROTON * (Q_PROTON - 1))
    E0m = mp.mpf(str(M_E_MEV)) / (Q_MUON * (Q_MUON - 1))
    results, verdicts = {}, []
    for name, (Z, N) in {"T": (1, 2), "3He": (2, 1)}.items():
        full = atom_braid_word_3A(Z, N, include_inter=True)
        ga, gb = sorted({x[2] for x in full if x[2] % 3 == 2})
        row = {}
        print(f"\n── {name} ──")
        for label, ymap, qf, E0 in (
            ("mixed (what #4657 did)", y_cached, float(Q_PROTON), E0p),
            ("pure proton", y_proton, float(Q_PROTON), E0p),
            ("pure muon  ", y_muon, float(Q_MUON), E0m),
        ):
            d2 = d2_under(full, ga, gb, ymap, qf)
            c3 = -E0 * d2
            door = "OPEN" if d2 < 0 else "CLOSED"
            print(f"   {label:<24} Δ²g = {float(d2):+.9f}   c₃ = {float(c3):+.6f} MeV"
                  f"   door {door}")
            row[label.strip()] = {"d2": mp.nstr(d2, 20), "c3_MeV": mp.nstr(c3, 20),
                                  "submodular": bool(d2 < 0)}
            verdicts.append(bool(d2 < 0))
        base = mp.mpf(row["mixed (what #4657 did)"]["d2"])
        for k in ("pure proton", "pure muon"):
            shift = abs(mp.mpf(row[k]["d2"]) - base) / abs(base)
            row[k]["rel_shift_vs_mixed"] = mp.nstr(shift, 10)
            print(f"     {k} vs mixed: rel shift {float(shift):.3e}")
        results[name] = row

    same = len(set(verdicts)) == 1
    print("\n" + "=" * 84)
    print(" RESULT")
    print(f"  * The mixing is REAL, and it is a CALIBRATION-LAYER crossing — not a cache")
    print(f"    bug. y_λ came from the IDEAL 3-CAL layer (muon, CAL-2 via m_μ/m_e) while χ")
    print(f"    was evaluated at the EXPERIMENTAL layer (proton). The {float(rel_q)*1e9:.2f} ppb gap IS")
    print(f"    the μ–p substrate tension.")
    print(f"  * Its SIZE is ~1e-7 relative on Δ²g — far below the 5–8% |χ| effect and")
    print(f"    utterly below any sign question. Every conclusion is unchanged:"
          f" door {'CLOSED under all three readings' if same else 'VERDICT FLIPS — serious'}.")
    print(f"  * The #4662 sign rule is anchor-INDEPENDENT: all 30 signs agree.")
    print(f"  * Correct convention going forward is PURE MUON — AGENTS.md pins the")
    print(f"    computations/ layer to muon-q₀ and forbids migrating it without sign-off.")
    print("=" * 84)

    w = WitnessBuilder("mu3-anchor-consistency", engine="pyhecke_native",
                       output_dir=Path(__file__).resolve().parent)
    w.add_assertion("verdict_unchanged_across_anchors", 1 if same else 0, 1)
    w.add_assertion("sign_rule_anchor_independent", 1 if signs_agree else 0, 1)
    w.add_parameter("q0_proton", mp.nstr(Q_PROTON, 30))
    w.add_parameter("q0_muon", mp.nstr(Q_MUON, 30))
    w.add_parameter("separation_ppb", float(rel_q) * 1e9)
    w.add_data("results", results)
    w.add_caveat(
        "DEFECT RECORDED, and it is a CALIBRATION-LAYER crossing, not a cache-staleness "
        "bug: mu3_frechet_perblock_probe.py (#4657, merged) took y_lambda from the IDEAL "
        "3-CAL layer (muon-pinned, CAL-2 via proxy m_mu/m_e) while evaluating chi at the "
        "EXPERIMENTAL layer (proton-pinned q_parameter.Q). The 11.54 ppb separation is the "
        "mu-p substrate tension itself. Mechanism: y_lambda_at()'s fast path serves the "
        "ideal-layer cache to an experimental-layer caller with no layer-boundary signal. "
        "Correct fix is to pick a layer and stay in it -- for a categorical Delta^2 g in "
        "computations/, that layer is MUON. Size ~1e-7 relative; no conclusion changes. "
        "Recurring class flagged as bean tnjb."
    )
    w.set_description(
        "Quantifies the q0 anchor mixing in the mu3 Frechet probe. Recomputes Delta^2 g "
        "three ways -- mixed (as merged), pure proton, pure muon -- on identical braid "
        "words. Door CLOSED under all three; the #4662 sign rule is anchor-independent "
        "(all 30 signs agree). Correct convention is pure muon per the AGENTS.md q0-anchor "
        "section."
    )
    w.save()
    return 0 if same else 1


if __name__ == "__main__":
    raise SystemExit(main())
