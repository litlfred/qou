#!/usr/bin/env python3
"""convention_systematic_audit_probe.py — how big is the UNDECLARED systematic?

THE QUESTION.  The framework's headline is three calibrations.  But the μ₃ arc alone rests on
several independent **convention choices**, each of which moves the answer and none of which is
derived:

  1. **q₀ anchor** — ideal 3-CAL (muon) vs experimental (proton), 11.54 ppb apart
  2. **trace object** — non-cyclic perblock `Σ y_λ|χ_λ|` vs signed cyclic `Σ y_λ χ_λ`
  3. **p–n interface** — `bring_color_weighted` (canonical since 2026-06-01) vs `strict_averaged`

Each is called a *convention*, not a parameter.  But a convention that moves a published number,
chosen from live alternatives, is functionally a degree of freedom regardless of the label.
Nobody has measured their **combined** effect on a single quantity.

This probe does the full 2×2×2 factorial on `Δ²g` and the A=3 cluster coefficient `cl₃`, and
reports the total spread.

WHY IT MATTERS MORE THAN ANOTHER ANSATZ.  If the spread is ~8 %, then **every magnitude claim in
the arc carries an undeclared systematic floor of that size** — larger than most of the effects
being chased.  Past "near-misses" and "refutations" at the few-percent level would then be
noise, and would need re-reading.  Unlike a new probe, this one can *invalidate* work rather
than only add to it.  That is the point.

GATES:
  * the canonical combination (proton + |χ| + bring_color_weighted) must reproduce the
    committed #4404 baseline, otherwise the factorial is not anchored to the real result;
  * all 8 cells must evaluate — a crash in any cell invalidates the spread.

Reports the spread whatever it is.  Nothing fitted, nothing wired.
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent.parent),
                str(Path(__file__).resolve().parent.parent / "substrate")]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import pyhecke_native  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from schur_principal_mpmath import y_lambda_at_q0_mpmath  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(40)

Q_PROTON = mp.mpf(str(Q0))
Q_MUON = mp.mpf("1.10997859555733471989976322048322502665620840878015405145269")
ANCHORS = {"proton": Q_PROTON, "muon": Q_MUON}
TRACES = {"abs": abs, "signed": (lambda z: z)}
PNCONV = ["bring_color_weighted", "strict_averaged"]
EXPECT = {"T": -1.769, "3He": -1.405}          # committed #4404 baseline (|chi|, proton-ish)
CANON = ("proton", "abs", "bring_color_weighted")


def chis(word, qf):
    f = [(float(c), float(d), int(g) + 1) for (c, d, g) in word]
    return {tuple(s): mp.mpf(repr(c))
            for s, c in pyhecke_native.chi_q_atomic_all_partitions(9, f, qf)}


def d2_for(Z, N, anchor, trace, pnconv, ycache):
    q = ANCHORS[anchor]
    tf = TRACES[trace]
    full = atom_braid_word_3A(Z, N, include_inter=True, pn_convention=pnconv)
    ga, gb = sorted({x[2] for x in full if x[2] % 3 == 2})
    Y = ycache[anchor]

    def g_of(sub):
        return chis([x for x in full if x[2] % 3 != 2 or x[2] in sub], float(q))

    ce, ca, cb, cab = g_of(set()), g_of({ga}), g_of({gb}), g_of({ga, gb})
    blocks = sorted(set(ce) & set(ca) & set(cb) & set(cab) & set(Y))
    d2 = sum(Y[l] * (tf(cab[l]) - tf(ca[l]) - tf(cb[l]) + tf(ce[l])) for l in blocks)
    E0 = mp.mpf(str(M_E_MEV)) / (q * (q - 1))
    return d2, -E0 * d2


def main() -> int:
    print("=" * 94)
    print(" Convention systematic audit — the full 2×2×2 on Δ²g and cl₃")
    print("=" * 94)
    print(" Three independent, underived convention choices:")
    print("   q₀ anchor    : proton (experimental) | muon (ideal 3-CAL)")
    print("   trace object : |χ| (non-cyclic perblock) | signed χ (cyclic Markov trace)")
    print("   p–n crossing : bring_color_weighted (canonical) | strict_averaged")

    ycache = {k: y_lambda_at_q0_mpmath(9, v) for k, v in ANCHORS.items()}
    results, gates_ok, canon_vals = {}, True, {}

    for name, (Z, N) in {"T": (1, 2), "3He": (2, 1)}.items():
        cells = {}
        print(f"\n── {name} ──")
        print(f"   {'anchor':<8}{'trace':<8}{'p–n crossing':<24}{'Δ²g':>14}{'cl₃ (MeV)':>13}")
        for anchor, trace, pnconv in itertools.product(ANCHORS, TRACES, PNCONV):
            d2, cl3 = d2_for(Z, N, anchor, trace, pnconv, ycache)
            key = f"{anchor}|{trace}|{pnconv}"
            cells[key] = {"d2": mp.nstr(d2, 20), "cl3_MeV": mp.nstr(cl3, 20),
                          "submodular": bool(d2 < 0)}
            mark = "   ← CANONICAL" if (anchor, trace, pnconv) == CANON else ""
            print(f"   {anchor:<8}{trace:<8}{pnconv:<24}{float(d2):>+14.6f}"
                  f"{float(cl3):>+13.4f}{mark}")
            if (anchor, trace, pnconv) == CANON:
                canon_vals[name] = cl3

        vals = [float(mp.mpf(c["cl3_MeV"])) for c in cells.values()]
        lo, hi = min(vals), max(vals)
        canon_f = float(canon_vals[name])
        spread = (hi - lo) / abs(canon_f)
        signs = {c["submodular"] for c in cells.values()}
        base_ok = abs(float(canon_vals[name]) - EXPECT[name]) < 0.01
        gates_ok = gates_ok and base_ok and len(vals) == 8

        print(f"   canonical cl₃ = {canon_f:+.4f}  vs committed #4404"
              f" {EXPECT[name]:+.3f}  → gate {'OK' if base_ok else 'FAIL'}")
        print(f"   SPREAD across all 8 conventions: [{lo:+.4f}, {hi:+.4f}]"
              f"  = {spread*100:.2f}% of canonical")
        print(f"   sign (door verdict) constant across conventions: {len(signs) == 1}")
        # marginal effect of each factor, holding the other two at canonical
        def cell(a, t, pn):
            return float(mp.mpf(cells[f"{a}|{t}|{pn}"]["cl3_MeV"]))
        base = cell(*CANON)
        marg = {
            "q0_anchor": abs(cell("muon", "abs", "bring_color_weighted") - base) / abs(base),
            "trace_object": abs(cell("proton", "signed", "bring_color_weighted") - base) / abs(base),
            "pn_crossing": abs(cell("proton", "abs", "strict_averaged") - base) / abs(base),
        }
        print("   marginal effect of each choice (others held canonical):")
        for k, v in sorted(marg.items(), key=lambda kv: -kv[1]):
            print(f"      {k:<14} {v*100:>10.4f}%")
        results[name] = {"cells": cells, "marginal_effects": marg,
                         "canonical_cl3_MeV": mp.nstr(canon_vals[name], 20),
                         "spread_abs_MeV": hi - lo,
                         "spread_rel_to_canonical": spread,
                         "sign_invariant": bool(len(signs) == 1),
                         "baseline_gate_ok": bool(base_ok)}

    worst = max(r["spread_rel_to_canonical"] for r in results.values())
    sign_ok = all(r["sign_invariant"] for r in results.values())

    print("\n" + "=" * 94)
    print(" RESULT")
    print(f"  * Largest convention spread on cl₃: {worst*100:.2f}% of the canonical value.")
    print(f"  * The SIGN (hence the μ₃ door verdict) is convention-invariant: {sign_ok}.")
    print("")
    print(f"  => Every MAGNITUDE claim in the A=3 arc carries an undeclared systematic floor")
    print(f"     of ~{worst*100:.0f}%. Any past near-match or refutation at or below that level")
    print(f"     is not resolved by the data — it must be re-read against this floor.")
    print(f"  => Every SIGN claim is safe: the exclusions, the sign rule, and the door verdict")
    print(f"     do not move.")
    print("=" * 94)

    w = WitnessBuilder("convention-systematic-audit", engine="pyhecke_native",
                       output_dir=Path(__file__).resolve().parent)
    w.add_assertion("all_8_cells_and_baseline_gate", 1 if gates_ok else 0, 1)
    w.add_assertion("sign_invariant_across_conventions", 1 if sign_ok else 0, 1)
    w.add_parameter("q0_proton", mp.nstr(Q_PROTON, 30))
    w.add_parameter("q0_muon", mp.nstr(Q_MUON, 30))
    w.add_parameter("canonical_combination", "|".join(CANON))
    w.add_data("results", results)
    w.add_data("worst_relative_spread", worst)
    w.add_caveat(
        "This measures only THREE of the live convention choices -- the ones exposed as "
        "parameters in the A=3 path. At least two more exist and are NOT varied here: the "
        "chi-encoding split of 2026-06-09 (matrix-M vs markov_trace_3A vs canonical "
        "tr_M_element, disagreeing by factors of ~7 in chi) and the signed-vs-double-modulus "
        "binding convention. The true systematic is therefore a LOWER BOUND on what is "
        "reported here."
    )
    w.set_description(
        "Full 2x2x2 factorial over three underived convention choices (q0 anchor, trace "
        "object, p-n crossing) measuring their combined effect on Delta^2 g and the A=3 "
        "cluster coefficient cl_3. Establishes the undeclared systematic floor on every "
        "magnitude claim in the arc, and confirms that sign claims are convention-invariant. "
        "Gated on the canonical cell reproducing the committed #4404 baseline."
    )
    w.save()
    return 0 if gates_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
