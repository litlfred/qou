#!/usr/bin/env python3
"""`prop:q-hecke-seminormal-character-closure` publishes the **convention-C**
trace table, and a live Lean file repeats the false "matches the bridge" claim
that `qou-46ab` already disproved in `computations/`.

WHY THIS EXISTS
---------------
`scripts/witness-block-agreement.py` flagged this block 5/5. Its three
top-scoring candidate producers were all wrong, in three different ways, which is
the case the checker's docstring warns coverage scoring cannot settle:

    laurentq-a5-ceiling-measure         5/5   a WALLTIME BENCHMARK; computes the
                                              traces only to time them
    rho-k-leading-order-verification    5/5   scriptFile is literally
                                              "(deferred -- producer not in
                                              computations/ tree)"
    witness-float64-padding-audit       5/5   an AGGREGATOR that scrapes other
                                              witnesses for fake precision

Reading beat scoring, and what it found is larger than a pointer problem.

FINDING 1 — THE DECLARING WITNESS CANNOT CARRY THIS TABLE
----------------------------------------------------------
`q_hecke_seminormal_character_closure_probe.py` verifies the character-closure
identity on **five abstract braids in B_3** — identity, `s1`, the Coxeter
element, the figure-8, and the full twist. No nucleons appear in it. It is a
correct structural verifier and it is not, and cannot be, the producer of a table
of nucleon traces. Fourth block in a row where the `contentBlock` pointer sits on
a verifier.

FINDING 2 — THE TABLE IS CONVENTION C, BY 7 % TO 120 %
-------------------------------------------------------
The canonical Hoefsmit + Wenzl bridge witness computes exactly these five atoms
by exactly the block's stated method (`sum_lambda y_lambda * chi_lambda`). It
agrees with **none** of them:

    atom       block publishes    canonical bridge witness      D/block
    proton     1.06530622859      1.14575969245730087           1.0755
    neutron    0.92323329717      0.987743688115809572          1.0699
    deuteron   0.38828647155      0.575172243917771871          1.4813
    tritium    0.10405211868      0.229310102104556507          2.2038
    3He        0.20654085856      0.40376703685142817           1.9549

The proton ratio is the signature. `qou-46ab` proved to 50 digits, via
`computations/audits/he4_witness_convention_attribution_probe.py`:

    C-frame  1.0653062286131670594     D-frame  1.1457597822878355047
    |D - C| / C = 0.0755215

Measured here as `|D - C| / D = 0.0702185`, the same fact under the other
normalisation (`0.0755215 / 1.0755215 = 0.0702185`). **The block's table is the
C frame.**

The block's own "Relative error ~1e-15" column is therefore an agreement between
**two C-frame paths**, not agreement with the production convention. Two paths
agreeing tells you nothing about which convention they are both in.

FINDING 3 — THE SAME FALSE CLAIM IS LIVE IN LEAN
--------------------------------------------------
`QOU/Interactions/MarkovPeelH3.lean` states

    tr_M(proton)|q0 = +1.065306228592389333...  (matches Hoefsmit + Wenzl
    bridge witness `atomic-tr-m-mpfr-50dps.witness.json` to ~4e-16)

That named witness gives `1.1457597823152389404`. The gap is `7.02e-2`, not
`4e-16` — **wrong by fourteen orders of magnitude.** It is word-for-word the
class `qou-46ab` found and fixed at
`canonical_tr_m_three_path_comparison.py:104` (*"matches bridge to all digits"*
-> *"now provably FALSE"*).

WHY qou-46ab's SWEEP COULD NOT SEE EITHER OF THEM
---------------------------------------------------
That bean scanned for the literal `1.06530622861316` and found 31 files. This
block renders the same quantity as `1.06530622859` and the Lean file as
`1.065306228592389333`. **A literal scan cannot match a different rendering of
the same number**, so zero content files and zero Lean files appeared in a sweep
whose whole purpose was to find them. This is the rounding lesson `qou-i229`
opened with, arriving from the other direction: there it inflated a count
fourfold, here it silently zeroed one.

WHAT IS NOT CLAIMED
-------------------
**Nothing is recomputed.** Migrating this table to convention D is `qou-46ab`'s
scoped job, it moves five published figures by 7-120 %, and it needs the Lean
declaration moved in the same pass or the two diverge further. The block and the
Lean comment are **labelled**, which is the precedent `df13e845cee` set.

No claim about the 11th-digit residual between the block's `1.06530622859` and
`qou-46ab`'s C-frame `1.06530622861`; that is `2e-11`, a separate and much
smaller question than the 7.55 % convention gap, and it is not diagnosed here.

No claim that the character-closure identity is wrong. It is not — the declaring
probe verifies it correctly on abstract braids, and it holds in either
convention.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

mp.mp.dps = 50

BLOCK = ROOT / ("folio/quantum-observable-universe/mass-endomorphism/"
                "q-hecke-seminormal-character-closure.md")
LEAN = ROOT / ("folio/quantum-observable-universe/lean/QOU/Interactions/"
               "MarkovPeelH3.lean")
DECLARING = COMP / "probes/q-hecke-seminormal-character-closure-probe.witness.json"
BRIDGE = COMP / "atomic-tr-m-mpfr-50dps.witness.json"
BRIDGE_P = COMP / "atomic-tr-m-mpfr-50dps-proton.witness.json"

#: The block's published table.
PUBLISHED = {"proton": "1.06530622859", "neutron": "0.92323329717",
             "deuteron": "0.38828647155", "tritium": "0.10405211868",
             "helium-3": "0.20654085856"}

#: qou-46ab's 50-digit attribution, via he4_witness_convention_attribution_probe.
C_FRAME_PROTON = "1.0653062286131670594"
D_FRAME_PROTON = "1.1457597822878355047"

#: The literal that bean scanned for, and the renderings that defeated it.
SCANNED_LITERAL = "1.06530622861316"
BLOCK_RENDERING = "1.06530622859"
LEAN_RENDERING = "1.065306228592389333"


def bridge_values(path: Path) -> dict[str, mp.mpf]:
    d = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    return {r["atom"]: mp.mpf(r["tr_M_at_q0_50dps"])
            for r in d.get("results", []) if "tr_M_at_q0_50dps" in r}


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])

    print("\n" + "=" * 78)
    print("§1  THE DECLARING WITNESS TESTS ABSTRACT BRAIDS, NOT NUCLEONS")
    print("=" * 78)
    dw = json.loads(DECLARING.read_text(encoding="utf-8", errors="replace"))
    labels = [r["label"] for r in dw["data"]["per_test_results"]]
    for lab in labels:
        print(f"    {lab}")
    check("the declaring probe's five tests are abstract B_3 braids — no nucleon "
          "appears, so it structurally cannot carry the block's table",
          len(labels) == 5
          and not any(a in " ".join(labels).lower()
                      for a in ("proton", "neutron", "deuteron", "tritium",
                                "helium", "3he")))

    print("\n" + "=" * 78)
    print("§2  THE TABLE IS CONVENTION C — 7 % TO 120 % FROM THE BRIDGE")
    print("=" * 78)
    bv = bridge_values(BRIDGE_P)
    print(f"    {'atom':<10} {'block':>16} {'canonical bridge':>26} {'D/block':>9}")
    ratios = {}
    for atom, pub in PUBLISHED.items():
        if atom not in bv:
            continue
        r = bv[atom] / mp.mpf(pub)
        ratios[atom] = r
        print(f"    {atom:<10} {pub:>16} {mp.nstr(bv[atom], 18):>26} "
              f"{mp.nstr(r, 6):>9}")
    check("the canonical bridge — which computes these five atoms by the block's "
          "OWN stated method, sum_lambda y_lambda chi_lambda — agrees with none "
          "of them", all(abs(r - 1) > mp.mpf("0.05") for r in ratios.values()))

    c, d = mp.mpf(C_FRAME_PROTON), mp.mpf(D_FRAME_PROTON)
    print(f"\n    qou-46ab's 50-digit attribution:")
    print(f"      C-frame proton   {C_FRAME_PROTON}")
    print(f"      D-frame proton   {D_FRAME_PROTON}")
    print(f"      |D-C|/C = {mp.nstr((d - c) / c, 7)}   (the bean's 0.0755215)")
    print(f"      |D-C|/D = {mp.nstr((d - c) / d, 7)}   (the same fact, other "
          f"normalisation)")
    check("the block's proton ratio matches qou-46ab's measured C-to-D gap, so "
          "the table is the C frame",
          abs(ratios["proton"] - d / c) < mp.mpf("1e-6"))

    print("\n    The block's own 'relative error ~1e-15' column is agreement")
    print("    between TWO C-FRAME PATHS. Two paths agreeing says nothing about")
    print("    which convention they are both in.")

    print("\n" + "=" * 78)
    print("§3  THE SAME FALSE CLAIM IS LIVE IN LEAN")
    print("=" * 78)
    lean_txt = LEAN.read_text(encoding="utf-8", errors="replace")
    bp = bridge_values(BRIDGE)["proton"]
    lv = mp.mpf(LEAN_RENDERING)
    gap = abs(bp - lv) / bp
    print(f"    Lean states       {LEAN_RENDERING}")
    print(f"    and claims it matches {BRIDGE.name} to ~4e-16")
    print(f"    that witness gives    {mp.nstr(bp, 20)}")
    print(f"    actual gap            {mp.nstr(gap, 6)}"
          f"   — wrong by 14 orders of magnitude")
    check("the Lean file carries the C-frame value and claims 4e-16 agreement "
          "with a witness it is 7e-2 from", LEAN_RENDERING in lean_txt
          and gap > mp.mpf("0.05"))

    print("\n" + "=" * 78)
    print("§4  WHY qou-46ab's LITERAL SCAN COULD NOT SEE EITHER")
    print("=" * 78)
    # The durable, self-contained form of this check. An earlier version counted
    # content files containing SCANNED_LITERAL and asserted zero -- which broke
    # the moment the correction box added to the block quoted that literal to
    # explain the miss. An assertion that a labelling pass can falsify was
    # testing the wrong thing; what matters is that the two strings differ while
    # denoting the same quantity, which is why a literal scan cannot bridge them.
    block_txt = BLOCK.read_text(encoding="utf-8", errors="replace")
    table_line = next(ln for ln in block_txt.splitlines()
                      if ln.startswith("| Proton"))
    same_quantity = (abs(mp.mpf(BLOCK_RENDERING) - mp.mpf(C_FRAME_PROTON))
                     < mp.mpf("1e-9"))
    print(f"    bean scanned for       {SCANNED_LITERAL}")
    print(f"    block's table row      {table_line.strip()[:60]}")
    print(f"    Lean renders it as     ...{LEAN_RENDERING[-12:]}")
    print(f"    the two strings differ but denote the same C-frame quantity "
          f"(within {mp.nstr(abs(mp.mpf(BLOCK_RENDERING) - mp.mpf(C_FRAME_PROTON)), 3)})")
    check("the block's table and the scanned literal are different strings for "
          "the same C-frame quantity, so no literal scan can bridge them — which "
          "is why a sweep aimed at exactly these sites returned zero",
          SCANNED_LITERAL not in table_line
          and BLOCK_RENDERING in table_line
          and same_quantity)

    print("\n" + "=" * 78)
    print("§S  VERDICT")
    print("=" * 78)
    print("  Not a pointer problem. The block publishes an excised convention,")
    print("  a live Lean file repeats a false agreement claim that qou-46ab")
    print("  already disproved in computations/, and that bean's literal scan")
    print("  could not see either because they render the number differently.")
    print("  NOTHING RECOMPUTED — the migration is qou-46ab's and it moves five")
    print("  published figures by 7-120 %. Both sites are labelled.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_content_block("prop:q-hecke-seminormal-character-closure")
        wb.set_description(
            "prop:q-hecke-seminormal-character-closure publishes a five-nucleon "
            "trace table in the EXCISED convention C. The canonical Hoefsmit+Wenzl "
            "bridge witness computes those same five atoms by the block's own stated "
            "method (sum_lambda y_lambda chi_lambda) and agrees with none of them: "
            "proton 1.0755x, neutron 1.0699x, deuteron 1.4813x, tritium 2.2038x, "
            "3He 1.9549x. The proton ratio is the signature qou-46ab proved to 50 "
            "digits (C-frame 1.0653062286131670594, D-frame 1.1457597822878355047, "
            "|D-C|/C = 0.0755215). The block's own 'relative error ~1e-15' column is "
            "agreement between two C-frame paths, which says nothing about which "
            "convention both are in. The same C value is live in "
            "QOU/Interactions/MarkovPeelH3.lean, claiming it 'matches Hoefsmit + "
            "Wenzl bridge witness atomic-tr-m-mpfr-50dps.witness.json to ~4e-16' when "
            "that witness gives 1.1457597823152389404 -- a 7.02e-2 gap, wrong by 14 "
            "orders of magnitude, and word-for-word the class qou-46ab fixed at "
            "canonical_tr_m_three_path_comparison.py:104. qou-46ab's sweep could not "
            "see either site: three renderings of one C-frame quantity share the prefix "
            "1.0653062286 and diverge after it (scanned ...61316, block ...59, Lean "
            "...592389333), and a literal scan matches none of the others -- so a sweep "
            "whose purpose was to find these returned zero for content and Lean. The "
            "block's declaring witness is a structural verifier over five ABSTRACT "
            "B_3 braids and cannot carry a nucleon table. NOTHING IS RECOMPUTED: the "
            "migration belongs to qou-46ab and moves five published figures by "
            "7-120 %. qou-i229.")
        # The block's own published figures are DELIBERATELY NOT transcribed
        # here. Recording them would make a witness that declares this block
        # "carry" them and close the checker's row -- the transcription weakness
        # documented in scripts/witness-block-agreement.py. These five figures
        # have no live producer (they are convention C, which is excised) and
        # the checker must keep saying so until qou-46ab migrates them. The
        # canonical D values and the ratios are recorded; the C figures stay
        # where they are published.
        wb.add_data("canonical_bridge_vs_block_ratio", {
            atom: {"canonical_bridge_D": mp.nstr(bv[atom], 20),
                   "ratio_D_over_published_C": mp.nstr(ratios[atom], 8)}
            for atom in ratios})
        wb.add_data("convention_attribution", {
            "c_frame_proton": C_FRAME_PROTON,
            "d_frame_proton": D_FRAME_PROTON,
            "gap_over_C": mp.nstr((d - c) / c, 8),
            "gap_over_D": mp.nstr((d - c) / d, 8),
            "source": "qou-46ab via he4_witness_convention_attribution_probe.py",
        })
        wb.add_data("lean_false_agreement_claim", {
            "file": "QOU/Interactions/MarkovPeelH3.lean",
            # By suffix: the full literal rounds to the block's published
            # proton figure and would close its row by transcription.
            "states_suffix_after_1.0653062286": LEAN_RENDERING[len("1.0653062286"):],
            "claims_agreement_with": BRIDGE.name,
            "claimed_gap": "4e-16",
            "actual_gap": mp.nstr(gap, 8),
        })
        # Renderings given by their DIFFERING SUFFIX, not in full: writing the
        # block's literal here would close its checker row by transcription.
        # The suffixes carry the whole finding -- the strings diverge from the
        # 9th decimal on, so no literal scan bridges them.
        wb.add_data("why_the_literal_scan_missed_it", {
            "common_prefix": "1.0653062286",
            "scanned_suffix": SCANNED_LITERAL[len("1.0653062286"):],
            "block_suffix": BLOCK_RENDERING[len("1.0653062286"):],
            "lean_suffix": LEAN_RENDERING[len("1.0653062286"):],
            "note": ("same C-frame quantity, three renderings; a literal scan "
                     "matches none of the others"),
        })
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "NOTHING IS RECOMPUTED. Migrating this table to convention D is "
            "qou-46ab's scoped job; it moves five published figures by 7-120 % and "
            "needs the Lean declaration moved in the same pass or the two diverge "
            "further. Both sites are LABELLED, the precedent df13e845cee set.")
        wb.add_caveat(
            "No claim about the 11th-digit residual between the block's rendering "
            "(...59) and qou-46ab's C-frame (...61) -- that is 2e-11, a "
            "separate and much smaller question than the 7.55 % convention gap, and "
            "it is not diagnosed here.")
        wb.add_caveat(
            "No claim that the character-closure identity is wrong. It is not; the "
            "declaring probe verifies it correctly on abstract braids and it holds "
            "in either convention.")
        print(f"\nWitness: {wb.save(extra={"q0Anchor": "ambiguous", "q0AnchorReason": 'compares figures across pins on purpose: reads the proton bridge (atomic-tr-m-mpfr-50dps-proton) and the muon bridge (atomic-tr-m-mpfr-50dps) witnesses and hardcoded proton-pin C/D-frame values, to attribute published renderings'})}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
