#!/usr/bin/env python3
"""s013 redirect (ii) grounding — the value-map target is COMPACT SU_q(2)
quantum-dimension data (Laurent polynomials in q₀), so the non-compact q-Bessel
search is chasing the wrong function class; and the uploaded Murakami paper
supplies no colored blocks.

Context. After the compact-modular routes were exhausted (Σ(2,3,5) D=2 golden,
2026-07-02; Σ(3,4,5) D=6, 2026-07-04 PR #3290), the surviving lead was
redirect (ii): the non-compact q-Bessel / E_q(2) vacuum row, motivated by the
NON-compact SU_q(2)→E_q(2) contraction and the owner-uploaded Murakami paper
`library/arxiv-2205.01282v2/2205.01282v2.pdf` ("colored blocks"). This probe grounds two facts
that together show redirect (ii) is not disciplined-actionable from the in-repo
sources, and locates where its genuine (literature-gated) content lives.

FACT 1 (machine-verified here). The keystone target bwS0(λ) = d_q(λ)/D at n=5 is
EXACTLY the normalized SU_q(2)/Hecke quantum-dimension vector — three SINGLE
balanced q-integers with the natural Hecke labels {1,4,5} plus one product:

    d_q(5)     = [1]_q            = 1
    d_q(4,1)   = [4]_q            ≈ 4.110
    d_q(3,2)   = [5]_q            ≈ 5.220
    d_q(3,1,1) = [4]_q[3]_q/[2]_q ≈ 6.220   (self-conjugate; the sole product)

Each is a LAURENT POLYNOMIAL in q₀ (a finite sum q^{k}+…+q^{-k}) — the character
of a finite-dimensional SU_q(2)/Hecke module. This is the COMPACT quantum
dimension, i.e. the Verlinde ratio S_{0λ}/S_{00} of the Hecke modular category.

FACT 2 (source scan, library/arxiv-2205.01282v2/2205.01282v2.pdf). Murakami's paper proves the
Gukov–Pei–Putrov–Vafa conjecture (WRT = radial limit of the homological block
Ẑ) for plumbed homology spheres. Text scan: 0 occurrences of
color/colour/decorat/wilson/refined/equivariant; the homological block is the
UNDECORATED false theta. For Σ(2,3,5) that block is the Lawrence–Zagier D=2
false theta — the very golden-row object already refuted. The paper contributes
no colored/decorated block that could carry a 4-class family.

STRUCTURAL CONSEQUENCE (type mismatch, made precise). The target values are
Laurent polynomials in q₀ (compact, finite, algebraic). The Hahn–Exton q-Bessel
J_ν(x;q) that a non-compact E_q(2) vacuum row is built from is a NON-TERMINATING
q-hypergeometric (₁φ₁) series in x — a transcendental function whose value at a
generic radial argument is not a q-integer. So a non-compact q-Bessel row can hit
the compact target only by TUNING its radial argument(s) to land a transcendental
function on algebraic q-integer values:

  * the disciplined SINGLE-argument (1-dof, overdetermined) form was already
    refuted (2026-07-02 qbessel-gate §4: best 13% off, E₈-exponent order);
  * a MULTI-argument form assigns each of the 4 channels its own radial argument
    ⇒ ≥ 4 free reals for 4 targets ⇒ UNFALSIFIABLE fit (dof ≥ constraints), unless
    the arguments are FIXED by the E_q(2) Plancherel measure — which requires the
    Koelink–Swarttouw q-Hankel kernel, a source NOT in library/.

So redirect (ii) is not disciplined-actionable in-repo: Murakami supplies no
colored block, and the only falsifiable q-Bessel form is refuted while the
falsifiable-multi-argument form needs the (un-uploaded) Plancherel kernel.
Meanwhile FACT 1 says the target IS the compact Verlinde/Hecke datum
S_{0λ}/S_{00} = d_q — which is exactly redirect (iii) (`BWVacuumRowIsHecke`),
near-definitional.

No fit; no q-Bessel formula is written here (fabrication-avoidance); the only
computed quantities are the exact compact quantum dimensions. Nothing wired.

Output: keystone-valuemap-target-is-compact-hecke.witness.json

# Ref: [murakami2022wrt] arXiv:2205.01282 (library/arxiv-2205.01282v2/2205.01282v2.pdf; GPPV proof,
#      undecorated homological blocks)
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 50
Q0 = mpf("1.1099785955541805")
MURAKAMI_PDF = ROOT.parent / "library" / "arxiv-2205.01282v2" / "2205.01282v2.pdf"


def qint(m, q=Q0):
    return (q ** m - q ** (-m)) / (q - q ** (-1))


def laurent_poly_check(m):
    """[m]_q = Σ_{j=0}^{m-1} q^{m-1-2j} — verify the q-integer is a balanced
    Laurent polynomial (finite, algebraic; the compact character)."""
    direct = qint(m)
    poly = mp.fsum(Q0 ** (m - 1 - 2 * j) for j in range(m))
    return abs(direct - poly) < mpf("1e-45")


def scan_murakami():
    """FACT 2: count colored/decorated terms in the uploaded Murakami PDF."""
    try:
        import fitz  # pymupdf
        if not MURAKAMI_PDF.exists():
            return {"available": False}
        d = fitz.open(str(MURAKAMI_PDF))
        txt = "\n".join(d[i].get_text() for i in range(d.page_count)).lower()
        terms = ["color", "colour", "decorat", "wilson", "refined", "equivariant"]
        counts = {t: txt.count(t) for t in terms}
        # "knot" appears only in a bibliography title (FIMT21) — record for honesty
        counts["knot_total"] = txt.count("knot")
        counts["homological_block"] = txt.count("homological block")
        counts["false_theta"] = txt.count("false theta")
        return {"available": True, "pages": d.page_count, "counts": counts,
                "any_colored_block": any(counts[t] for t in terms)}
    except Exception:  # noqa: BLE001 — missing/corrupt PDF or absent pymupdf: degrade gracefully
        return {"available": False}


def run():
    out = {"q0": float(Q0)}

    # FACT 1 — the target IS the compact Hecke quantum-dimension vector
    dq = {
        "(5)": (mpf(1), "[1]_q"),
        "(4,1)": (qint(4), "[4]_q"),
        "(3,2)": (qint(5), "[5]_q"),
        "(3,1,1)": (qint(4) * qint(3) / qint(2), "[4]_q[3]_q/[2]_q"),
    }
    out["bwS0_targets"] = {k: {"value": mp.nstr(v, 15), "hecke_label": lbl}
                           for k, (v, lbl) in dq.items()}
    # match the merged screen-probe figures (1, 4.110, 5.220, 6.220)
    ref = {"(5)": mpf("1"), "(4,1)": mpf("4.10968"),
           "(3,2)": mpf("5.22044"), "(3,1,1)": mpf("6.22044")}
    out["targets_match_screen_probe"] = bool(
        all(abs(dq[k][0] - ref[k]) < mpf("1e-4") for k in ref))
    # each single q-integer is a balanced Laurent polynomial (compact character)
    out["q_integers_are_laurent_polynomials"] = bool(
        laurent_poly_check(1) and laurent_poly_check(4) and laurent_poly_check(5)
        and laurent_poly_check(3) and laurent_poly_check(2))
    # the self-conjugate block is the sole non-monomial-q-integer (a product)
    out["self_conjugate_is_sole_product"] = "(3,1,1) = [4][3]/[2]"

    # FACT 2 — the uploaded Murakami paper has no colored blocks
    out["murakami_scan"] = scan_murakami()

    matched = out["targets_match_screen_probe"] and \
        out["q_integers_are_laurent_polynomials"]
    no_colored = (not out["murakami_scan"].get("any_colored_block", True)) \
        if out["murakami_scan"].get("available") else None
    out["value_target_is_compact_hecke"] = bool(matched)
    out["murakami_supplies_colored_block"] = (
        out["murakami_scan"].get("any_colored_block")
        if out["murakami_scan"].get("available") else "pdf-unavailable")

    out["verdict"] = (
        "GROUNDED: (1) bwS0=d_q/D is exactly the compact SU_q(2)/Hecke "
        "quantum-dimension vector — 3 balanced q-integers [1],[4],[5] (Laurent "
        "polynomials) + the product [4][3]/[2]; = Verlinde S_{0λ}/S_{00}. "
        "(2) The uploaded Murakami paper (GPPV proof) has no colored/decorated "
        "block; its Σ(2,3,5) block is the undecorated D=2 false theta (golden, "
        "refuted). Consequence: the non-compact q-Bessel search (redirect ii) "
        "targets a transcendental function class to hit a compact-algebraic "
        "target; the single-argument (falsifiable) form is refuted (qbessel-gate "
        "§4) and the multi-argument form is an unfalsifiable ≥4-dof fit without "
        "the (un-uploaded) Koelink–Swarttouw Plancherel kernel. The honest "
        "resolution is redirect (iii): the compact Verlinde/Hecke identity "
        "S_{0λ}/S_{00}=d_q (BWVacuumRowIsHecke), near-definitional. Scope (a) on "
        "the tested q-Bessel forms; no structural exclusion of a Plancherel-fixed "
        "row asserted.")
    return out


def report(res):
    print("# s013 redirect (ii) grounding — target is compact Hecke; Murakami has no colored block\n")
    print("## FACT 1 — bwS0 = d_q/D is the compact SU_q(2)/Hecke quantum dimension\n")
    for k, d in res["bwS0_targets"].items():
        print(f"  d_q{k:8s} = {d['hecke_label']:18s} = {d['value']}")
    print(f"- targets match merged screen probe (1,4.110,5.220,6.220): "
          f"**{res['targets_match_screen_probe']}**")
    print(f"- q-integers are balanced Laurent polynomials (compact characters): "
          f"**{res['q_integers_are_laurent_polynomials']}**\n")
    print("## FACT 2 — uploaded Murakami 2205.01282 scan\n")
    sc = res["murakami_scan"]
    if sc.get("available"):
        print(f"- pages {sc['pages']}; colored/decorated term counts: {sc['counts']}")
        print(f"- supplies a colored/decorated block: **{sc['any_colored_block']}**\n")
    else:
        print("- (pymupdf unavailable; scan skipped)\n")
    print(f"**VERDICT:** {res['verdict']}")


def main():
    res = run()
    report(res)
    wb = WitnessBuilder("keystone-valuemap-target-is-compact-hecke",
                        engine="mpmath", output_dir=HERE)
    wb.set_description(
        "s013 redirect (ii) grounding: the value-map target bwS0=d_q/D is the "
        "compact SU_q(2)/Hecke quantum-dimension vector (Laurent polynomials, "
        "= Verlinde S_0λ/S_00), and the uploaded Murakami GPPV paper has no "
        "colored/decorated block (its Σ(2,3,5) block is the undecorated D=2 "
        "golden false theta). So the non-compact q-Bessel search chases the "
        "wrong function class; single-arg form refuted, multi-arg is an "
        "unfalsifiable fit without the un-uploaded Koelink–Swarttouw kernel. "
        "No fit; no q-Bessel formula written; nothing wired.")
    for k, v in res.items():
        wb.add_data(k, v)
    wb.add_assertion("value_target_is_compact_hecke",
                     str(res["value_target_is_compact_hecke"]), "True",
                     source="the 4 targets equal exact compact q-integers/products "
                            "matching the merged screen probe")
    # FACT 2 is a HARD gate: the Murakami PDF is committed under library/, so a
    # run that cannot read it (missing pymupdf / missing-or-corrupt file) must
    # FAIL loudly rather than emit allPassed:true with a vacuous
    # "pdf-unavailable" — the assertion is emitted unconditionally.
    scan_available = bool(res["murakami_scan"].get("available"))
    wb.add_assertion("murakami_scan_ran", str(scan_available), "True",
                     source="the committed library/arxiv-2205.01282v2/2205.01282v2.pdf must be "
                            "readable (pymupdf present, file intact); a skipped "
                            "scan is a failure, not a silent pass")
    wb.add_assertion("murakami_supplies_colored_block",
                     str(res["murakami_supplies_colored_block"])
                     if scan_available else "pdf-unavailable", "False",
                     source="the uploaded GPPV paper has no colored/decorated "
                            "block term (source scan)")
    path = wb.save()
    print(f"\nwitness: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
