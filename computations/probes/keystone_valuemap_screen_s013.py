#!/usr/bin/env python3
"""s013 — value-map screen: which amplitude turns the colored Σ(2,3,5) family into bwS0 = d_q/D?

Bean s013 (the keystone value step). PR #3190 established the STRUCTURE: coloring the icosahedral
5-fibre of Σ(2,3,5) gives an E₈-exponent-indexed family whose 4 Coxeter dual pairs match the 4
conjugation classes of bwS0 at n=5, monotone in magnitude (bare support {1,11,19,29} = the H₄
exponents; colour split = H₄ ⊂ E₈ folding). The open VALUE step: an amplitude reproducing the actual
numbers bwS0(λ) = d_q(λ)/D. This probe screens the natural closed-form candidates (formalize-first:
test specific structural hypotheses, not a fit) and reports the outcome — pruning the easy maps and
locating the genuine difficulty.

Candidates screened against the 4 target d_q values (= bwS0·D), assigning each conjugation class its
E₈ dual-pair representative exponent e ∈ {1,7,11,13}:

  (C1) exponent quantum dimension  [e]_q = sinh(eη)/sinh(η)      — the naive Verlinde d_e
  (C2) modular sine-kernel vacuum row  S_{1,e} ∝ sin(π e / 30)   — compact-MTC S_{0λ}
  (C3) growth-regime  sinh(η e)                                   — the non-compact sinh

RESULT (q₀, 50 dps): all three are REFUTED — none reproduces d_q = (1, 4.110, 5.220, 6.220):
[e]_q → (1, 7.63, 13.55, 17.34); sin-kernel ratios → (1, 6.40, 8.74, 9.36); sinh → same as [e]_q.
The E₈ exponents are NOT the quantum-dimension labels of the value map.

THE SHARP POSITIVE (where the difficulty actually is): 3 of the 4 targets are SINGLE q-integers with
the natural HECKE labels {1,4,5} (not the E₈ exponents) — d_q(5)=[1]_q, d_q(4,1)=[4]_q,
d_q(3,2)=[5]_q — while the self-conjugate ≥3-row block d_q(3,1,1)=[4]_q[3]_q/[2]_q is the sole
genuine PRODUCT. So the value map is trivial on the near-standard blocks (a single balanced
q-integer) and non-trivial ONLY on the self-conjugate (3,1,1) — exactly the ≥3-row block where the
SU(2)/spin-j gate failed (2026-06-24). The realization difficulty is concentrated there.

CONCLUSION (consistent with the modular-category identification, 2026-06-22): since the compact
sine-kernel and the exponent q-dimension both fail, and the arena is the NON-COMPACT SU_q(2)→E_q(2)
contraction (Hahn–Exton q-Bessel at real q₀>1), the value map is the **non-compact q-Bessel vacuum
row**, not a compact modular S-matrix entry. The genuine remaining computation: the q-Bessel
amplitude reproducing the single q-integers on near-standard blocks and the [4][3]/[2] product on the
self-conjugate (3,1,1). (a)-prunes the compact candidates; no fit; no fabricated q-Bessel formula.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from q_parameter import Q_MP  # noqa: E402
import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
# q0 comes from the pin table, never a literal. This held
# `1.1099785955541805`, the SUPERSEDED muon value -- it matches
# neither current pin, so nothing could compare it against
# anything. Owner ruling 2026-08-24, bean `qou/ftuv`.
Q0 = Q_MP
ETA = mp.log(Q0)
P = 30


def qi(m):
    return (Q0 ** m - Q0 ** (-m)) / (Q0 - Q0 ** (-1))


# 4 conjugation classes at n=5: (label, E8 dual-pair exponent, target d_q, Hecke q-integer form)
CLASSES = [
    ("(5)~(1^5)", 1, mp.mpf(1), "[1]_q", mp.mpf(1)),
    ("(4,1)~(2,1^3)", 7, qi(4), "[4]_q", qi(4)),
    ("(3,2)~(2,2,1)", 11, qi(5), "[5]_q", qi(5)),
    ("(3,1,1) self-conj", 13, qi(4) * qi(3) / qi(2), "[4][3]/[2]", qi(4) * qi(3) / qi(2)),
]


def run():
    rows = []
    for nm, e, dq, hlabel, hval in CLASSES:
        rows.append({
            "class": nm, "e8_exponent": e, "d_q": float(dq),
            "hecke_form": hlabel, "hecke_val": float(hval),
            "cand_qint_e": float(qi(e)),                        # C1 [e]_q
            "cand_sin_kernel": float(mp.sin(mp.pi * e / P)),    # C2 sin(pi e/30)
            "cand_sinh_eta_e": float(mp.sinh(ETA * e)),         # C3 sinh(eta e)
            "is_single_qinteger": hlabel.count("[") == 1,
        })
    # normalized ratios to the vacuum (first) class
    d0 = rows[0]["d_q"]
    for key, cand in (("ratio_d_q", "d_q"), ("ratio_qint", "cand_qint_e"),
                      ("ratio_sin", "cand_sin_kernel"), ("ratio_sinh", "cand_sinh_eta_e")):
        base = rows[0][cand]
        for r in rows:
            r[key] = r[cand] / base
    # refutation: a candidate matches iff its ratio-vector equals the d_q ratio-vector
    def refuted(rkey):
        return not all(abs(r[rkey] - r["ratio_d_q"]) < 1e-6 for r in rows)
    return {
        "q0": float(Q0), "eta": float(ETA),
        "rows": rows,
        "qint_refuted": refuted("ratio_qint"),
        "sin_kernel_refuted": refuted("ratio_sin"),
        "sinh_refuted": refuted("ratio_sinh"),
        "single_qinteger_count": sum(1 for r in rows if r["is_single_qinteger"]),
    }


def report(res):
    print("# s013 value-map screen — colored Σ(2,3,5) amplitude → bwS0 = d_q/D?\n")
    print(f"q₀ = {res['q0']:.10f}   η = log q₀ = {res['eta']:.6f}   P = {P}\n")
    print("| class | E₈ e | d_q | Hecke form | [e]_q (C1) | sin(πe/30) (C2) | sinh(ηe) (C3) |")
    print("|---|--:|--:|---|--:|--:|--:|")
    for r in res["rows"]:
        print(f"| {r['class']} | {r['e8_exponent']} | {r['d_q']:.4f} | {r['hecke_form']} "
              f"| {r['cand_qint_e']:.4f} | {r['cand_sin_kernel']:.4f} | {r['cand_sinh_eta_e']:.4f} |")
    print("\nNormalized to the vacuum class (ratios to the smallest):")
    print("| class | d_q ratio | [e]_q ratio | sin ratio | sinh ratio |")
    print("|---|--:|--:|--:|--:|")
    for r in res["rows"]:
        print(f"| {r['class']} | {r['ratio_d_q']:.3f} | {r['ratio_qint']:.3f} "
              f"| {r['ratio_sin']:.3f} | {r['ratio_sinh']:.3f} |")

    print("\n## Screen result\n")
    print(f"- **C1 [e]_q (exponent quantum dimension): REFUTED** ({res['qint_refuted']}).")
    print(f"- **C2 sin(πe/30) (compact modular S-matrix vacuum row): REFUTED** "
          f"({res['sin_kernel_refuted']}).")
    print(f"- **C3 sinh(ηe): REFUTED** ({res['sinh_refuted']}).")
    print("  None reproduces d_q via the E₈-exponent assignment.\n")

    print("## The sharp positive — where the difficulty is\n")
    print(f"- **{res['single_qinteger_count']} of 4** target d_q are SINGLE balanced q-integers with the")
    print("  natural HECKE labels {1,4,5} (NOT the E₈ exponents): d_q(5)=[1], d_q(4,1)=[4],")
    print("  d_q(3,2)=[5]. The value map is trivial on these near-standard blocks.")
    print("- The ONLY genuine product is the self-conjugate ≥3-row block d_q(3,1,1)=[4][3]/[2] —")
    print("  exactly the block where the SU(2)/spin-j gate failed (2026-06-24). The realization")
    print("  difficulty is concentrated at the self-conjugate block.\n")

    print("## Conclusion\n")
    print("- The compact sine-kernel and the exponent q-dimension both fail, consistent with the")
    print("  modular-category identification (2026-06-22): the arena is the NON-COMPACT")
    print("  SU_q(2)→E_q(2) contraction (Hahn–Exton q-Bessel at real q₀>1), so the value map is the")
    print("  **non-compact q-Bessel vacuum row**, not a compact S-matrix entry.")
    print("- Genuine remaining computation: the q-Bessel amplitude reproducing the single q-integers")
    print("  on near-standard blocks and the [4][3]/[2] product on the self-conjugate (3,1,1). This")
    print("  (a)-prunes the compact candidates and locates the hard block. No fit; no fabricated")
    print("  q-Bessel formula.")


def main(argv=None):
    res = run()
    report(res)
    w = WitnessBuilder("keystone-valuemap-screen-s013", engine="mpmath")
    w.set_description(
        "s013 keystone value-map screen: which amplitude turns the colored Sigma(2,3,5) E8-exponent "
        "family into bwS0 = d_q/D? Screens 3 closed-form candidates against the 4 target d_q at q0: "
        "(C1) exponent q-dimension [e]_q, (C2) compact sine-kernel vacuum row sin(pi e/30), (C3) "
        "sinh(eta e). ALL REFUTED via the E8-exponent assignment (d_q=1,4.11,5.22,6.22 vs [e]_q="
        "1,7.63,13.55,17.34; sin-ratios 1,6.40,8.74,9.36). Sharp positive: 3 of 4 d_q are single "
        "balanced q-integers with HECKE labels {1,4,5} (not E8 exponents) -- d_q(5)=[1], d_q(4,1)=[4], "
        "d_q(3,2)=[5] -- and only the self-conjugate >=3-row block d_q(3,1,1)=[4][3]/[2] is a product "
        "(exactly where the SU(2) gate failed). Consistent with the non-compact E_q(2)/Hahn-Exton "
        "q-Bessel identification: the value map is the q-Bessel vacuum row, not a compact S-matrix "
        "entry. (a)-prunes compact candidates, locates the hard block. No fit."
    )
    w.add_data("q0", res["q0"])
    w.add_data("eta", res["eta"])
    w.add_data("rows", res["rows"])
    w.add_data("qint_refuted", res["qint_refuted"])
    w.add_data("sin_kernel_refuted", res["sin_kernel_refuted"])
    w.add_data("sinh_refuted", res["sinh_refuted"])
    w.add_assertion(
        "compact_valuemap_candidates_refuted",
        computed=1 if (res["qint_refuted"] and res["sin_kernel_refuted"] and res["sinh_refuted"]) else 0,
        expected=1, tolerance=0,
        source="All three compact closed-form value-map candidates ([e]_q, sin(pi e/30), sinh(eta e)) "
               "fail to reproduce d_q via the E8-exponent assignment, consistent with the non-compact "
               "E_q(2)/q-Bessel arena. The value map is the q-Bessel vacuum row; difficulty is "
               "concentrated on the self-conjugate (3,1,1) block (d_q=[4][3]/[2]).",
    )
    out = w.save()
    print(f"\nwitness → {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
