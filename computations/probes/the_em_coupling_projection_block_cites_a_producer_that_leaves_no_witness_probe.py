#!/usr/bin/env python3
"""`prop:em-coupling-projection` is CORRECT; its `contentBlock` pointer is aimed
at the wrong producer, and the claiming witness carries two wrong labels.

WHY THIS EXISTS
---------------
`scripts/witness-block-agreement.py` flagged this block hardest of any: **6 of 7
published figures absent from the single witness declaring it.** A near-total
miss is the signature of a misdirected pointer rather than a stale table, so it
was worth checking before reading it as a defect.

**The block is right.** Every figure reproduces at the proton pin from
`computations/alpha/alpha_em_form_comparison_probe.py` — the producer the table
names *in its own prose* — and the table's claim that "all rows are evaluated at
the proton pin" is accurate.

THE ACTUAL FINDING: THE POINTER IS ON THE WRONG PRODUCER
--------------------------------------------------------
    em_coupling_projection_probe.py     declares contentBlock, computes 1 of 7 rows
    alpha_em_form_comparison_probe.py   computes the other 6, emits NO witness at all

So the block's machine-readable provenance covers **14 %** of it, and the
producer of the rest leaves no record for any tool to find. This is the mirror
image of what the checker was built to catch: not a block drifting from its
witness, but a block whose witness was never the right one.

TWO LABEL DEFECTS IN THE CLAIMING WITNESS — NUMBERS UNTOUCHED
--------------------------------------------------------------
1. **"muon-anchored" on a proton-pinned computation.** `q0Value` is the proton
   pin and `q0Anchor` is `proton` — both correct — while `q0_source`, the
   description and the assertion `source` all say "the canonical muon-anchored
   substrate q₀". Three prose sites against two correct structured fields.

2. **`CODATA_ALPHA_INV` is not CODATA.** `137.035999206` is the **Morel et al.
   (2020) Rb-87 recoil** measurement, cited under exactly that name in
   `sec:fine-structure-data`. It is a legitimate and well-sourced number; four
   sites in the producer call it CODATA. The block's table compares against
   CODATA 2022 = `137.035999177(21)`, a different quantity.

**Both are numerically inert, which is why they survived.** Rb-87 differs from
CODATA 2022 by `2.1e-10` relative, against an assertion tolerance of `5e-3` and a
measured error of `1.55e-3`. Nothing about the verdict moves. The defect is
provenance only — the same shape as `df13e845cee`'s "*the defect was the label*".

A THIRD FINDING, CROSS-BLOCK: ONE QUANTITY, TWO PINS
-----------------------------------------------------
`q[9]_q[10]_q` is published by two blocks at two different `q₀`, and one of them
is a retired vintage:

    prop:em-coupling-projection      136.823209      proton   (136.823208853583)
    prop:em-coupling-bring-zero-mode 136.823219654   RETIRED  (136.823219654561)
                                                     live muon: 136.823219729273

`qou-i229` already found the retired pin in `bring-zero-mode`. New here is that a
**sibling block publishes the same quantity at the production pin**, so the two
disagree on one number in the eleventh digit. That sharpens the refresh case: it
is not only stale against the substrate, it is inconsistent across the corpus.

WHAT IS NOT CLAIMED
-------------------
Nothing about whether the Chern-Simons dressing is the right model of `α_EM`;
`rem:em-coupling-chern-simons` is explicitly open, `κ` is still a `sorry`, and
the producer's own output records that the smallest residual belongs to a
RULED-OUT (PSLQ-empirical) form. Nothing about which pin either block *should*
take — that is the owner ruling `qou-i229` holds. No figure is changed.
"""
from __future__ import annotations

import json
import re
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

BLOCK = ROOT / ("folio/quantum-observable-universe/predicted-spectra/"
                "em-coupling-projection-table1-data.md")
CLAIMANT = COMP / "probes/em_coupling_projection_probe.py"
CLAIM_WIT = COMP / "probes/em-coupling-projection-probe.witness.json"
REAL = COMP / "alpha/alpha_em_form_comparison_probe.py"

#: The three registered `q0` values this block's quantity can distinguish.
PROTON = mp.mpf("1.1099785827513808075916690956107688798744991218736")
MUON = mp.mpf("1.109978595642739046681795129380001752700065561029011556974045769999095")
RETIRED = mp.mpf("1.1099785955541805752815940796095093779932822799587")

#: Morel et al. 2020 Rb-87 recoil, and the two CODATA adjustments it is not.
RB87_2020 = "137.035999206"
CODATA_2022 = "137.035999177"
CODATA_2018 = "137.035999084"


def qint(n, q):
    """Balanced quantum integer `[n]_q = (q^n - q^-n)/(q - q^-1)`."""
    return (q ** n - q ** (-n)) / (q - 1 / q)


def bare(q):
    """`q [9]_q [10]_q`, the undressed inverse coupling."""
    return q * qint(9, q) * qint(10, q)


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])

    print("\n" + "=" * 78)
    print("§1  THE BLOCK'S FIGURES REPRODUCE AT THE PROTON PIN")
    print("=" * 78)
    q = PROTON
    hbar2 = ((q - 1) / q) ** 2
    two_half = (q + 1 / q) / 2
    rows = [("q [9]_q [10]_q", bare(q), "136.823209"),
            ("hbar_q^2", hbar2, "0.00981719"),
            ("[2]_q / 2", two_half, "1.005448")]
    ok = True
    for name, val, pub in rows:
        k = len(pub.split(".")[1])
        agree = mp.nstr(val, 30)[:1] and abs(val - mp.mpf(pub)) < mp.mpf(10) ** (-k) / 2 * mp.mpf("1.000001")
        ok &= bool(agree)
        print(f"    {name:<18} = {mp.nstr(val, 14):<20} published {pub:<14}"
              f" {'match' if agree else 'MISMATCH'}")
    check("the table's directly-recomputable rows reproduce at the PROTON pin, "
          "as the table's own prose states", ok)

    print("\n" + "=" * 78)
    print("§2  THE POINTER IS ON THE PRODUCER THAT COMPUTES ONE ROW OF SEVEN")
    print("=" * 78)
    claim_src = CLAIMANT.read_text(encoding="utf-8", errors="replace")
    real_src = REAL.read_text(encoding="utf-8", errors="replace")
    wit = json.loads(CLAIM_WIT.read_text(encoding="utf-8", errors="replace"))

    check("the claiming producer declares this block",
          'set_content_block("prop:em-coupling-projection")' in claim_src)
    wit_s = json.dumps(wit)
    check("the claiming witness carries the BARE form only — the dressed value, "
          "delta_CS and kappa are all absent",
          "136.82320885358258431" in wit_s
          and "137.035935" not in wit_s
          and "delta_CS" not in wit_s and "kappa" not in wit_s)
    check("the producer the TABLE names emits no witness at all, so six of the "
          "seven rows have no machine-readable provenance",
          "WitnessBuilder" not in real_src
          and not list((COMP / "alpha").glob("alpha-em-form-comparison*.witness.json")))
    print(f"    claimant : {CLAIMANT.relative_to(ROOT)}   (1 of 7 rows)")
    print(f"    named    : {REAL.relative_to(ROOT)}   (6 of 7, no witness)")

    print("\n" + "=" * 78)
    print("§3  LABEL DEFECT A — 'muon-anchored' on a proton-pinned computation")
    print("=" * 78)
    q0v = mp.mpf(wit["q0Value"])
    print(f"    witness q0Anchor           = {wit['q0Anchor']}")
    print(f"    witness q0Value            = {mp.nstr(q0v, 20)}")
    print(f"    proton pin                 = {mp.nstr(PROTON, 20)}")
    print(f"    muon pin (live)            = {mp.nstr(MUON, 20)}")
    check("the STRUCTURED fields are correct: q0Anchor says proton and q0Value "
          "is the proton pin",
          wit["q0Anchor"] == "proton" and abs(q0v - PROTON) < mp.mpf("1e-40"))
    prose = sum(1 for _ in re.finditer("muon-anchored", claim_src))
    prose_wit = sum(1 for _ in re.finditer("muon-anchored", wit_s))
    print(f"    'muon-anchored' in producer = {prose} site(s); in witness = "
          f"{prose_wit} site(s)   (was 4 and 3 before this change)")
    # REGRESSION GUARD, not a defect assertion. The defect was four prose sites
    # in the producer and three in its witness saying "muon-anchored" over a
    # proton-pinned computation; it is fixed in the same change that found it.
    # Asserting the DEFECT would leave a probe that goes red the moment the fix
    # lands -- the exact failure this bean already recorded for
    # muon_pin_three_values_probe.py. So assert the invariant instead.
    check("no site now calls this proton-pinned computation muon-anchored — the "
          "prose agrees with the structured fields (was 4 sites + 3 in the "
          "witness)", prose == 0 and prose_wit == 0)

    print("\n" + "=" * 78)
    print("§4  LABEL DEFECT B — `CODATA_ALPHA_INV` holds an Rb-87 measurement")
    print("=" * 78)
    rb, c22, c18 = (mp.mpf(RB87_2020), mp.mpf(CODATA_2022), mp.mpf(CODATA_2018))
    print(f"    producer's constant        = {RB87_2020}"
          f"   (Morel et al. 2020, Rb-87 recoil)")
    print(f"    CODATA 2022                = {CODATA_2022}")
    print(f"    CODATA 2018                = {CODATA_2018}")
    check("the producer's constant is neither CODATA adjustment",
          rb != c22 and rb != c18)
    check("it is the Rb-87 value, cited under that name in sec:fine-structure-data",
          "137.035999206" in (ROOT / "folio/quantum-observable-universe/"
                              "observations/fine-structure-data.md").read_text(
                                  encoding="utf-8", errors="replace"))
    # Same regression-guard shape as §3: the producer said "CODATA
    # α_EM = 1/137.035999206" in four places. Fixed in this change; the
    # constant's VALUE is untouched, only what it is called. The identifier
    # CODATA_ALPHA_INV is kept for callers and now carries a comment saying
    # what it actually holds.
    mislabel = sum(1 for _ in re.finditer(r"CODATA α_EM = 1/137\.035999206",
                                          claim_src))
    print(f"    producer sites still calling 137.035999206 'CODATA' = {mislabel}"  # noqa: P31 — names the mislabel it counts
          f"   (was 4)")
    check("no site now presents the Rb-87 value as a CODATA adjustment; the "
          "constant's value is unchanged", mislabel == 0)
    check("the producer now names Morel et al. 2020 explicitly",
          "Morel" in claim_src)
    rel = abs(rb - c22) / c22
    print(f"    Rb-87 vs CODATA 2022, relative = {mp.nstr(rel, 4)}"
          f"   (tolerance 5e-3, measured error 1.55e-3)")
    check("the mislabel is NUMERICALLY INERT — it cannot move the verdict, which "
          "is why it survived", rel < mp.mpf("1e-8"))

    print("\n" + "=" * 78)
    print("§5  CROSS-BLOCK: ONE QUANTITY, TWO PINS, ONE OF THEM RETIRED")
    print("=" * 78)
    bp, bm, br = bare(PROTON), bare(MUON), bare(RETIRED)
    print(f"    q[9][10] at proton         = {mp.nstr(bp, 15)}"
          f"   <- em-coupling-projection publishes 136.823209")
    print(f"    q[9][10] at muon (live)    = {mp.nstr(bm, 15)}")
    print(f"    q[9][10] at RETIRED        = {mp.nstr(br, 15)}"
          f"   <- em-coupling-bring-zero-mode publishes 136.823219654")
    check("this block's figure is the proton pin",
          abs(bp - mp.mpf("136.823209")) < mp.mpf("5e-7"))
    sib = mp.mpf("136.823219654")
    near = min(("proton", bp), ("muon_live", bm), ("retired", br),
               key=lambda kv: abs(kv[1] - sib))
    print(f"    sibling's 136.823219654 is nearest the {near[0].upper()} pin"
          f"   (|d| = {mp.nstr(abs(near[1] - sib), 4)})")
    check("the sibling block's figure is nearest the RETIRED pin — the two "
          "blocks disagree on the same quantity in the 11th digit",
          near[0] == "retired")

    # The sibling figure is a TRUNCATION of the retired value, not a rounding:
    # 136.823219654561 rounds to ...655. It misses a half-ulp acceptance window
    # by 1.12 half-ulps, so any rounding-based matcher (including
    # scripts/witness-block-agreement.py) rejects it even against its own
    # producer. Measured across the whole report, truncation explains 0 of the
    # 58 asserted-unmatched figures, so the checker is NOT widened for it: a
    # window that rescues nothing while admitting false negatives is a net loss.
    half_ulp = mp.mpf("5e-10")
    check("that figure is a TRUNCATION of the retired value, not a rounding — it "
          "misses a half-ulp window by 1.12 half-ulps, a documented hazard for "
          "any rounding-based matcher",
          br > sib and (br - sib) < mp.mpf("1e-9")
          and abs(br - sib) > half_ulp)

    print("\n" + "=" * 78)
    print("§S  TRIAGE VERDICT")
    print("=" * 78)
    print("  The BLOCK is correct and the checker's 6/7 row is a false positive of")
    print("  the documented class: a block's producer need not be the witness")
    print("  naming it. What the row genuinely points at is that the contentBlock")
    print("  pointer is on the wrong producer, and the right one emits no witness.")
    print("  Two label defects found en route, both numerically inert, neither")
    print("  touching a figure. No number changed by this probe.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_content_block("prop:em-coupling-projection")
        wb.set_description(
            "Triages the witness-block-agreement checker's hardest row (6 of 7 "
            "published figures absent from the single witness declaring "
            "prop:em-coupling-projection). The BLOCK IS CORRECT: every figure "
            "reproduces at the proton pin from alpha_em_form_comparison_probe.py, "
            "the producer the table names in its own prose, and the table's claim "
            "that all rows use the proton pin is accurate. The real finding is that "
            "the contentBlock pointer is on the wrong producer -- "
            "em_coupling_projection_probe.py claims the block and computes 1 of 7 "
            "rows, while the producer of the other 6 emits no witness at all, so "
            "the block's machine-readable provenance covers 14 percent of it. Two "
            "label defects in the claiming witness, numbers untouched: (a) q0Value "
            "and q0Anchor correctly say proton while three prose sites say "
            "'muon-anchored'; (b) CODATA_ALPHA_INV holds 137.035999206, which is "
            "the Morel et al. 2020 Rb-87 recoil measurement cited under that name "
            "in sec:fine-structure-data, not a CODATA adjustment. Both are "
            "numerically inert (Rb-87 vs CODATA 2022 is 2.1e-10 relative against a "
            "5e-3 tolerance), which is why they survived. Third finding, "
            "cross-block: q[9]_q[10]_q is published at 136.823209 (proton) here and "
            "136.823219654 (RETIRED vintage) in prop:em-coupling-bring-zero-mode, "
            "so two blocks disagree on one quantity in the 11th digit.")
        wb.add_data("block_rows_at_proton_pin", {
            "q_dq9_dq10": mp.nstr(bare(PROTON), 20),
            "hbar_q_sq": mp.nstr(hbar2, 20),
            "two_q_over_2": mp.nstr(two_half, 20),
        })
        wb.add_data("pointer", {
            "claiming_producer": str(CLAIMANT.relative_to(ROOT)),
            "claiming_producer_rows_covered": "1 of 7",
            "producer_named_by_the_table": str(REAL.relative_to(ROOT)),
            "producer_named_by_the_table_emits_witness": "no",
        })
        wb.add_data("label_defects", {
            "q0_prose_says": "muon-anchored",
            "q0_structured_says": wit["q0Anchor"],
            "alpha_constant": RB87_2020,
            "alpha_constant_actually": "Morel et al. 2020, Rb-87 recoil",
            "alpha_constant_labelled": "CODATA",
            "rb87_vs_codata2022_relative": mp.nstr(rel, 6),
        })
        wb.add_data("cross_block_q_dq9_dq10", {
            "proton": mp.nstr(bp, 18),
            "muon_live": mp.nstr(bm, 18),
            "retired": mp.nstr(br, 18),
            "em_coupling_projection_publishes": "136.823209",
            "em_coupling_bring_zero_mode_publishes": "136.823219654",
        })
        for name, ok_ in checks:
            wb.add_assertion(name=name, computed=str(int(ok_)), expected="1")
        wb.add_caveat(
            "Says nothing about whether the Chern-Simons dressing is the right model "
            "of alpha_EM. rem:em-coupling-chern-simons is open, kappa is still a "
            "sorry, and the named producer's own output records that the smallest "
            "residual belongs to a RULED-OUT PSLQ-empirical form -- the signature of "
            "a fit, not evidence for one.")
        wb.add_caveat(
            "Says nothing about which pin either block SHOULD take. That is the owner "
            "ruling qou-i229 holds. No published figure is changed here.")
        print(f"\nWitness: {wb.save(extra={"q0Anchor": "ambiguous", "q0AnchorReason": (
            "comparison by design: evaluates the block's quantity q[9]_q[10]_q at three registered pins (proton 1.10997858275138..., live CODATA-2022 muon 1.10997859564273..., retired CODATA-2018 muon 1.10997859555418...) to find which one the published figures come from")})}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok_ in checks if not ok_]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
