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
  * all 8 cells must evaluate — a crash in any cell invalidates the spread;
  * the sign of Δ²g must be reported as measured, whatever it is.

  The #4404 numeric reproduction is deliberately NOT a gate: see the convention note
  on `EXPECT_C` below.

MEASURED ANSWER (convention D, canonical since the owner ruling of 2026-08-15).
The combined spread over all eight cells is **0.01 %**, and all of it is the p–n
crossing convention:

    q0_anchor     0.0000 %      (proton vs muon: 11.5 ppb in, ~2e-7 out)
    trace_object  0.0000 %      (|χ| vs signed χ — see below)
    pn_crossing   0.0146 %      (bring_color_weighted vs strict_averaged)

**The trace-object choice contributes exactly zero, and that is a consequence of
convention D rather than a coincidence.**  Under D the Wenzl level relation
collapses to r = 2 (`wenzlLevel_conventionD`) and `y_λ = 0 ⟺ ℓ(λ) > r`
(`schurPrincipal_eq_zero_iff`, sorry-free, all n and all r), so every partition with
three or more rows carries y_λ = 0 — 25 of the 30 partitions of 9.  Both are already
established on main; `two_row_support_recount.py` measures what the truncation removes.
The ten partitions whose weights were *negative* under convention C are all inside
that zeroed set, so |χ| and signed χ now agree term by term.

Under the excised convention C the same probe measured a **7.7 %** spread (T; 5.5 %
for ³He), entirely from that |χ|-vs-signed choice.  That number is a
convention-C artifact and must not be quoted as a systematic on current main.

So the arc's undeclared systematic floor from these three choices is ~0.01 %, not
percent-level.  This narrows rather than widens the alarm — but see the caveat: two
further convention choices are not varied here, so 0.01 % is a LOWER bound.

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
from q_parameter import Q_MP as Q0_MP, q_muon_at  # noqa: E402 — the mpf, NOT the float64 `Q`
from codata_constants import M_E_MEV  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.witness import q0_comparison  # noqa: E402

set_compute_dps(40)

Q_PROTON = Q0_MP
# The muon leg was the 60-digit literal
# "1.10997859555733471989976322048322502665620840878015405145269" -- the
# RETIRED self-certified muon pin A, superseded 2026-08-22 (fca08de7d2) by the
# live CODATA-2022 lepton-ratio derivation q_muon_at(), +0.0769 ppb. Reading it
# by name matters MORE here than in a sole-anchor probe, not less: the q0 anchor
# is axis 1 of this probe's 2x2x2 factorial, so a stale muon leg understates the
# very systematic being measured. This is an (E1) explicit mu-vs-p comparison, so
# it needs BOTH pins and belongs in NEITHER anchor list (bean qou-9ugp).
Q_MUON = q_muon_at(60)
ANCHORS = {"proton": Q_PROTON, "muon": Q_MUON}
TRACES = {"abs": abs, "signed": (lambda z: z)}
PNCONV = ["bring_color_weighted", "strict_averaged"]
# The #4404 committed baseline.  It was computed under trace convention **C**
# (z = 1/(√q + 1/√q)), which the owner ruling of 2026-08-15 excised.  Under the
# canonical convention **D** (z = q³/(q²+1)) the Wenzl level collapses to r = 2,
# so `schur_principal_mpmath` is the SU(2) two-row specialisation and every y_λ
# with ℓ(λ) ≥ 3 is exactly 0 — 25 of the 30 partitions of 9.  These values are
# therefore NOT reproducible on current main, and are kept as history, not as a
# gate.  See the C-vs-D block in the RESULT section below.
EXPECT_C = {"T": mp.mpf("-1.769"), "3He": mp.mpf("-1.405")}   # #4404 baseline, CONVENTION C
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
    results, gates_ok, canon_vals, spreads = {}, True, {}, {}

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

        # NO-FLOAT64: every quantity below is carried as mpmath.mpf end to end;
        # float() appears only inside f-strings, for display.
        vals = [mp.mpf(c["cl3_MeV"]) for c in cells.values()]
        lo, hi = min(vals), max(vals)
        canon_m = canon_vals[name]
        spread = (hi - lo) / abs(canon_m)
        signs = {c["submodular"] for c in cells.values()}
        # NOT a gate: the #4404 value is convention C, this run is convention D.
        delta_C = canon_m - EXPECT_C[name]
        gates_ok = gates_ok and len(vals) == 8

        print(f"   canonical cl₃ = {float(canon_m):+.4f}  (convention D)"
              f"   vs #4404 convention-C {float(EXPECT_C[name]):+.3f}"
              f"   Δ = {float(delta_C):+.4f}"
              f" ({float(delta_C / EXPECT_C[name])*100:+.1f}%)")
        print(f"   SPREAD across all 8 conventions: [{float(lo):+.4f}, {float(hi):+.4f}]"
              f"  = {float(spread)*100:.2f}% of canonical")
        print(f"   sign (door verdict) constant across conventions: {len(signs) == 1}")
        # marginal effect of each factor, holding the other two at canonical
        def cell(a, t, pn):
            return mp.mpf(cells[f"{a}|{t}|{pn}"]["cl3_MeV"])
        base = cell(*CANON)
        marg = {
            "q0_anchor": abs(cell("muon", "abs", "bring_color_weighted") - base) / abs(base),
            "trace_object": abs(cell("proton", "signed", "bring_color_weighted") - base) / abs(base),
            "pn_crossing": abs(cell("proton", "abs", "strict_averaged") - base) / abs(base),
        }
        print("   marginal effect of each choice (others held canonical):")
        for k, v in sorted(marg.items(), key=lambda kv: -kv[1]):
            print(f"      {k:<14} {float(v)*100:>10.4f}%")
        spreads[name] = spread
        results[name] = {"cells": cells,
                         "marginal_effects": {k: mp.nstr(v, 20)
                                              for k, v in marg.items()},
                         "canonical_cl3_MeV": mp.nstr(canon_vals[name], 20),
                         "spread_abs_MeV": mp.nstr(hi - lo, 20),
                         "spread_rel_to_canonical": mp.nstr(spread, 20),
                         "sign_invariant": bool(len(signs) == 1),
                         "convention_C_4404_baseline_MeV": mp.nstr(EXPECT_C[name], 20),
                         "delta_vs_convention_C_MeV": mp.nstr(delta_C, 20)}

    worst = max(spreads.values())
    sign_ok = all(r["sign_invariant"] for r in results.values())

    print("\n" + "=" * 94)
    print(" RESULT")
    print(f"  * Largest convention spread on cl₃: {float(worst)*100:.2f}% of the canonical value.")
    print(f"  * The SIGN (hence the μ₃ door verdict) is convention-invariant: {sign_ok}.")
    print("")
    print(f"  => Every MAGNITUDE claim in the A=3 arc carries an undeclared systematic floor")
    print(f"     of ~{float(worst)*100:.4f}% from THESE THREE choices. Under the excised convention C")
    print(f"     the same probe measured 7.7% — that figure is a C artifact (see module docstring).")
    print(f"  => Every SIGN claim is safe: the exclusions, the sign rule, and the door verdict")
    print(f"     do not move.")
    print("=" * 94)

    w = WitnessBuilder("convention-systematic-audit", engine="pyhecke_native",
                       output_dir=Path(__file__).resolve().parent)
    w.add_assertion("all_8_cells_evaluate", 1 if gates_ok else 0, 1)
    w.add_assertion("sign_invariant_across_conventions", 1 if sign_ok else 0, 1)
    w.add_parameter("q0_proton", mp.nstr(Q_PROTON, 30))
    w.add_parameter("q0_muon", mp.nstr(Q_MUON, 30))
    w.add_parameter("canonical_combination", "|".join(CANON))
    w.add_data("results", results)
    w.add_data("worst_relative_spread", mp.nstr(worst, 20))
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
        "cluster coefficient cl_3. Under the canonical trace convention D the combined "
        "floor is 0.0146%, ALL of it the p-n crossing: the q0 anchor and the |chi|-vs-signed "
        "trace object each contribute 0. The trace-object zero is structural under D -- the "
        "Wenzl level collapses to r=2, so every partition with three or more rows carries "
        "y_lambda = 0 and |chi| is a no-op. The 7.7% spread this probe measured under the "
        "excised convention C was that same choice, and is a C artifact. Sign claims are "
        "convention-invariant. The #4404 baseline is convention C, is recorded as history "
        "with its delta, and is deliberately NOT a gate."
    )
    _reason = (
        "Axis 1 of this probe's 2x2x2 factorial IS the q0 anchor: it evaluates "
        "Delta^2 g and cl_3 at BOTH the experimental (proton) and ideal-CAL-2 "
        "(muon) pins and publishes their relative separation as "
        "results.floors.q0_anchor. Both legs are read by name -- proton from "
        "q_parameter.Q_MP, muon from q_parameter.q_muon_at(60) -- so neither can "
        "go stale against the anchor. This is a comparison, not a layer straddle "
        "(bean qou-9ugp).")
    assert _reason.isascii(), "q0AnchorReason must be pure ASCII (json.dump ensure_ascii)"
    w.save(q0_comparison(muon=mp.nstr(Q_MUON, 50, strip_zeros=False),
                         proton=mp.nstr(Q_PROTON, 50, strip_zeros=False),
                         reason=_reason))
    return 0 if gates_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
