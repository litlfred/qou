#!/usr/bin/env python3
"""Is the binding residual c_λ = B_AME/E_gate a parameter-free function of partition shape?

Context (session 2026-06-30). The SU(4)-occupancy binding E_gate = E₀·ln(1/W_λ) gets the
magic/mid-mass SCALE right (⁴He 6%) where the production B_sym misses by ~2.1×. The entire
remaining error is one factor
    c_λ = B_AME / E_gate
which runs 0.24 → 0.94 (⁴He, the doubly-magic rectangular (3,3,3,3)) → 1.46. "Fixing" binding
= deriving c_λ. The Δ_λ gate forbids FITTING c_λ; this probe instead TESTS whether c_λ is a
parameter-free function of partition-shape invariants — formalize-first hypothesis screening,
NOT a fit. A clean no-tuned-constant relationship would be a lead; its absence confirms the full
keystone W_λ match is required.

Shape invariants of the SU(4) ground partition λ (all parameter-free, dimensionless where noted):
  • imbalance   I_rect = 1 − n/(m·λ_max)   (0 ⟺ rectangular/magic; the ⁴He anchor)
  • contentVar  Σ_c c(c)² / n²             (the keystone Identity-I object, normalised)
  • aspect      λ_max / m                   (row length / row count)
  • nDistinct   #distinct row lengths / m   (shape complexity)

Key control: ³H and ³He share the SAME SU(4) partition (3,2,2,2) but have DIFFERENT c_λ
(0.534 vs 0.486). So if c_λ depended on λ alone, they'd be equal — they are not. The probe
surfaces this split explicitly: it is the signature of a charge/Coulomb (Z-dependent) component
that no shape invariant of λ can carry. Reported, not fitted.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
import mass_binding_dashboard as mbd  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def shape_invariants(lam):
    """Parameter-free shape invariants of partition λ (tuple of row lengths)."""
    rows = [r for r in lam if r > 0]
    n = sum(rows)
    m = len(rows)
    lam_max = max(rows)
    I_rect = 1.0 - n / (m * lam_max)
    # content c(i,j) = j − i over cells (0-indexed)
    content_sq = sum((j - i) ** 2 for i, r in enumerate(rows) for j in range(r))
    contentVar = content_sq / (n * n)
    aspect = lam_max / m
    nDistinct = len(set(rows)) / m
    return {
        "n": n, "m": m, "I_rect": I_rect, "contentVar": contentVar,
        "aspect": aspect, "nDistinct": nDistinct, "content_sq": content_sq,
    }


def _pearson(xs, ys):
    nn = len(xs)
    mx = sum(xs) / nn; my = sum(ys) / nn
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sxx = sum((x - mx) ** 2 for x in xs)
    syy = sum((y - my) ** 2 for y in ys)
    if sxx <= 0 or syy <= 0:
        return None
    return sxy / math.sqrt(sxx * syy)


def run():
    me, q0, E0 = mbd._constants()
    ame = mbd._ame_table()
    Lbond = mbd._bond_type_L()
    nucleon_msym = mbd._nucleon_msym(E0)
    rows = []
    # Use the dashboard's own low-group isotope list so NUCLEAR_SPINS (keyed on those
    # names) resolves — wrong names default spin to 0, impossible for odd-quark nuclei.
    for (nm, Z, N) in mbd.GROUPS["low"]:
        r = mbd._row(nm, Z, N, E0, me, Lbond, nucleon_msym, ame, max_strands=0)
        lam = r["su4_partition"]
        if lam is None or not r["B_AME"] or not r["E_gate"]:
            continue
        inv = shape_invariants(lam)
        c_lam = r["B_AME"] / r["E_gate"]
        rows.append({
            "iso": nm, "Z": Z, "N": N, "A": Z + N, "lambda": list(lam),
            "B_AME": r["B_AME"], "W_lam": r["W_lam"], "E_gate": r["E_gate"], "c_lam": c_lam,
            **inv,
        })
    return {"q0": q0, "E0": E0, "rows": rows}


INVARIANTS = ["I_rect", "contentVar", "aspect", "nDistinct"]


def report(res):
    rows = res["rows"]
    print("# Is c_λ a parameter-free function of partition shape?")
    print(f"E₀ = {res['E0']:.4f} MeV   q₀ = {res['q0']:.6f}\n")
    print("| iso | A | λ (SU(4)) | B_AME | E_gate | c_λ | I_rect | contentVar | aspect | nDistinct |")
    print("|---|--:|---|--:|--:|--:|--:|--:|--:|--:|")
    for r in rows:
        lam = ",".join(map(str, r["lambda"]))
        print(f"| {r['iso']} | {r['A']} | ({lam}) | {r['B_AME']:.2f} | {r['E_gate']:.2f} "
              f"| {r['c_lam']:.3f} | {r['I_rect']:.3f} | {r['contentVar']:.3f} "
              f"| {r['aspect']:.2f} | {r['nDistinct']:.2f} |")

    print("\n## c_λ vs each shape invariant (Pearson r over the 6 isotopes)\n")
    print("| invariant | Pearson r |")
    print("|---|--:|")
    cs = [r["c_lam"] for r in rows]
    corr = {}
    for inv in INVARIANTS:
        xs = [r[inv] for r in rows]
        rr = _pearson(xs, cs)
        corr[inv] = rr
        print(f"| {inv} | {(f'{rr:+.3f}' if rr is not None else '—')} |")

    # The 3H/3He control: same λ, different c_λ
    th = next((r for r in rows if r["iso"] == "3H"), None)
    he = next((r for r in rows if r["iso"] == "3He"), None)
    print("\n## Control — ³H vs ³He (mirror nuclei, SAME SU(4) partition)\n")
    if th and he:
        print(f"- ³H  λ=({','.join(map(str,th['lambda']))}) Z=1  c_λ={th['c_lam']:.3f}")
        print(f"- ³He λ=({','.join(map(str,he['lambda']))}) Z=2  c_λ={he['c_lam']:.3f}")
        print(f"- Δc_λ = {abs(th['c_lam']-he['c_lam']):.3f} with IDENTICAL λ ⇒ c_λ is NOT a")
        print(f"  function of the SU(4) partition alone: a charge/Coulomb (Z-dependent) component")
        print(f"  is present that no shape invariant of λ can carry.")

    print("\n## Verdict\n")
    best = max(corr.items(), key=lambda kv: abs(kv[1]) if kv[1] is not None else 0)
    print(f"- Strongest single-invariant correlation: {best[0]} (r={best[1]:+.3f}) — but the SU(4)")
    print(f"  partition always has m=4 rows, so aspect = λ_max/4 ≈ SIZE: this largely re-encodes")
    print(f"  the known A-trend, not a new shape law. The size-normalised contentVar (r≈−0.75, the")
    print(f"  keystone Identity-I object) is the more shape-specific (weaker) signal.")
    print(f"- ⁴He (rectangular (3,3,3,3), I_rect=0) anchors c_λ≈0.94≈1 — consistent with the")
    print(f"  magic/rectangular = saturated reading.")
    print(f"- The ³H/³He split proves c_λ ≠ f(λ) alone: a Z-dependent (Coulomb) term is needed")
    print(f"  beyond any partition-shape function. So a clean parameter-free c_λ=f(shape) does")
    print(f"  NOT close the binding by itself — the full keystone W_λ match + a charge term is")
    print(f"  required. This SCREENS the hypothesis (no fit); it does not fit c_λ.")
    return corr


def main(argv=None):
    res = run()
    corr = report(res)
    w = WitnessBuilder("clambda-shape-invariant-probe", engine="python")
    w.set_description(
        "Screens whether the binding residual c_lambda = B_AME/E_gate (E_gate = E0*ln(1/W_lambda)) "
        "is a parameter-free function of SU(4)-partition shape invariants (I_rect, contentVar, "
        "aspect, nDistinct) over 2H/3H/3He/4He/6Li/7Li. Formalize-first hypothesis screening, NOT a "
        "fit. Key control: 3H and 3He share the SAME partition (3,2,2,2) but differ in c_lambda "
        "(0.534 vs 0.486) -> c_lambda is NOT a function of lambda alone; a charge/Coulomb (Z) term "
        "is present. 4He (rectangular, I_rect=0) anchors c_lambda~1. Conclusion: a clean shape-only "
        "c_lambda does not close binding; the full keystone W_lambda match + a charge term is needed."
    )
    w.add_data("q0", res["q0"])
    w.add_data("E0_MeV", res["E0"])
    w.add_data("rows", res["rows"])
    w.add_data("pearson_c_lambda_vs_invariant", corr)
    th = next((r for r in res["rows"] if r["iso"] == "3H"), None)
    he = next((r for r in res["rows"] if r["iso"] == "3He"), None)
    if th and he:
        w.add_data("mirror_split_3H_3He_c_lambda", round(abs(th["c_lam"] - he["c_lam"]), 4))
    he4 = next((r for r in res["rows"] if r["iso"] == "4He"), None)
    w.add_assertion(
        "he4_rectangular_anchor_c_lambda_near_one",
        computed=round(he4["c_lam"], 3) if he4 else 0.0,
        expected=1.0, tolerance=0.10,
        source="At the doubly-magic, RECTANGULAR SU(4) partition (3,3,3,3) (I_rect=0), "
               "c_lambda = B_AME/E_gate ~ 0.94 ~ 1 — the magic/rectangular = saturated anchor "
               "the shape hypothesis predicts.",
    )
    out = w.save()
    print(f"\nwitness → {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
