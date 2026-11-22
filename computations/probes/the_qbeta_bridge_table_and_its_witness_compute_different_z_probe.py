#!/usr/bin/env python3
"""`tbl:q-beta-spectral-bridge-table-data` and the witness it cites compute
**different `z`** — under the same name — and differ by 21 % (`qou-i229`).

AND IT RETRACTS A CLAIM OF MINE
-------------------------------
I recorded this table as "already internally inconsistent: its `h` is at pin A
and its `h^2` at pin B, so `h^2 != (h)^2` as published". **That is wrong and is
withdrawn.** Measured:

    h  published                 0.2090603219955937
    (h published)^2              0.043706218232901319
    h^2 published                0.04370621823290131      differ by 9.0e-18

The table closes on itself exactly. I reached the wrong conclusion by matching
`h^2` against closed forms at three candidate `q0` values and reading which
bucket it fell in; at `h^2` the pin-A and pin-B values differ around the tenth
digit and my significant-figure bucketing could not separate them. Same lossy
metric that tied `log(1 + q_0)` earlier the same day — second instance, and the
first one should have taught me to check the simpler explanation (`h^2` is just
`h` squared) before reaching for a cross-pin story.

THE REAL DEFECT IS LARGER, AND IT RUNS THE OTHER WAY
-----------------------------------------------------
The block ends with

    "Values are the displayed digits of the 50-dps witness
     q-beta-spectral-bridge.witness.json, regenerated from the canonical CAL-2
     pinning q-pinning-50-digit.witness.json."

**Every clause of that is false.** The witness contains none of the table's
values, and declares `q0Anchor: proton` rather than the canonical CAL-2 (muon)
pinning. The two are different computations:

                          block (published)        witness (producer)
    q0                    1.109978595557335        1.1099785827513808...   proton
    z                     0.4993203340335613       0.6126880371464652...
    h                     0.2090603219955937       0.2090602987956393...
    ln(1 + z h)           0.09929139859972778      0.1205248238414840...
    1/z + (z-1)h/(2z)     1.897907634269324        1.5660730493910099...

Each side reproduces its own numbers exactly from its own `z` and pin. The
divergence is **21 %** on the bridge ratio — not a vintage, a different formula.

WHICH SIDE IS STALE — AND IT IS NOT THE ONE I EXPECTED
--------------------------------------------------------
`conj:q-beta-spectral-bridge` **defines**

    z := 1 / (sqrt q + 1/sqrt q)

so the published table agrees with its own proposition, and the **producer**
does not: `q_beta_spectral_bridge_witness.py` computes `q^3/(q^2+1)`, the
Markov trace parameter. The usual failure this arc keeps finding is content
lagging compute; here the compute has diverged from the stated definition.

**The mechanism that hid it is a name collision.** The proposition calls
`1/(sqrt q + 1/sqrt q)` "the Markov-Jones parameter", and the witness's field
holding `q^3/(q^2+1)` is named `z_markov_jones`. Same name, different formula,
so nothing that greps the name sees a disagreement.

**And CI is green throughout.** The witness's two assertions
(`bridge_residual_within_O_h_squared`, `Q_beta_form_a_form_b_agree_...`) both
PASS, because they are internally consistent — a producer checking itself
against itself cannot see that it has drifted from the block it declares in
`contentBlock`.

WHAT THIS PROBE DOES NOT DO
---------------------------
It does not rule on which `z` is correct. The proposition defines one and the
producer computes the other; deciding whether the definition or the compute
moved is an authoring question about `conj:q-beta-spectral-bridge`, and both
readings have a live consequence (the `Q_beta` MeV figures differ by ~0.05 MeV).
It does not touch the producer, the proposition, or the table's values. It does
correct the block's provenance sentence, which is false under either reading.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

mp.mp.dps = 50

#: The block's own quoted pin, and the proposition's own `z`.
Q_BLOCK = "1.109978595557335"
#: The witness's declared pin.
Q_WITNESS = "1.1099785827513808075916690956107688798744991218736"
WITNESS = COMP / "q-beta-spectral-bridge.witness.json"

#: `(label, published-in-block, key-in-witness)`.
ROWS = (("h", "0.2090603219955937", "h"),
        ("z", "0.4993203340335613", "z_markov_jones"),
        ("ln(1 + z h)", "0.09929139859972778", "form_b_log_one_plus_zh"),
        ("1/z + (z-1)h/(2z)", "1.897907634269324", "predicted_bridge_ratio"),
        ("h^2", "0.04370621823290131", "h_squared_tolerance"))


def z_prop(q):
    """`conj:q-beta-spectral-bridge`'s definition: `1/(sqrt q + 1/sqrt q)`."""
    return 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))


def z_markov(q):
    """What the producer computes under the name `z_markov_jones`."""
    return q ** 3 / (q ** 2 + 1)


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name, ok):
        checks.append((name, bool(ok)))
        print(f"  [{'ok ' if ok else 'FAIL'}] {name}")

    print(__doc__.split("\n")[0])
    print(f"\nmpmath at {mp.mp.dps} dps")

    print("\n" + "=" * 78)
    print("§1  RETRACTION: the table DOES close on itself")
    print("=" * 78)
    h_pub = mp.mpf("0.2090603219955937")
    h2_pub = mp.mpf("0.04370621823290131")
    d = abs(h_pub ** 2 - h2_pub)
    print(f"    h published        {h_pub}")
    print(f"    (h published)^2    {mp.nstr(h_pub ** 2, 20)}")
    print(f"    h^2 published      {h2_pub}")
    print(f"    |difference|       {mp.nstr(d, 4)}")
    check("h^2 IS (h)^2 to 1e-16 — my 'already internally inconsistent, h^2 != "
          "(h)^2' claim is withdrawn", d < mp.mpf("1e-16"))

    print("\n" + "=" * 78)
    print("§2  THE BLOCK REPRODUCES FROM THE PROPOSITION'S z AT ITS OWN PIN")
    print("=" * 78)
    qb = mp.mpf(Q_BLOCK)
    hb, zb = qb - 1 / qb, z_prop(qb)
    got = {"h": hb, "z": zb, "ln(1 + z h)": mp.log(1 + zb * hb),
           "1/z + (z-1)h/(2z)": 1 / zb + (zb - 1) * hb / (2 * zb),
           "h^2": hb ** 2}
    ok_block = True
    for lbl, pub, _k in ROWS:
        v = got[lbl]
        rel = abs(v - mp.mpf(pub)) / abs(mp.mpf(pub))
        ok_block &= rel < mp.mpf("1e-14")
        print(f"    {lbl:>20} published {pub:>22}  computed "
              f"{mp.nstr(v, 17):>22}  rel {mp.nstr(rel, 3)}")
    check("every published value reproduces from q0 = 1.109978595557335 with "
          "the PROPOSITION's z = 1/(sqrt q + 1/sqrt q) — block and proposition "
          "agree", ok_block)

    print("\n" + "=" * 78)
    print("§3  THE WITNESS REPRODUCES FROM A DIFFERENT z AT A DIFFERENT PIN")
    print("=" * 78)
    if not WITNESS.exists():
        print(f"    (witness not found at {WITNESS})")
        check("witness present", False)
    else:
        w = json.loads(WITNESS.read_text())
        data = w.get("data", {})
        print(f"    witness q0Anchor = {w.get('q0Anchor')!r}   "
              f"contentBlock = {w.get('contentBlock')!r}")
        qw = mp.mpf(Q_WITNESS)
        hw, zw = qw - 1 / qw, z_markov(qw)
        gotw = {"h": hw, "z": zw, "ln(1 + z h)": mp.log(1 + zw * hw),
                "1/z + (z-1)h/(2z)": 1 / zw + (zw - 1) * hw / (2 * zw),
                "h^2": hw ** 2}
        ok_wit, ok_diff = True, True
        for lbl, pub, key in ROWS:
            wv = mp.mpf(data[key]) if key in data else None
            if wv is None:
                continue
            ok_wit &= abs(gotw[lbl] - wv) / abs(wv) < mp.mpf("1e-30")
            ok_diff &= abs(wv - mp.mpf(pub)) / abs(wv) > mp.mpf("1e-9")
            print(f"    {lbl:>20} witness {mp.nstr(wv, 20):>24}  block "
                  f"{pub:>22}")
        check("the witness reproduces exactly from the PROTON pin with the "
              "Markov z = q^3/(q^2+1) — it is internally consistent too",
              ok_wit)
        check("and every row differs from the block's — the two are different "
              "computations, not a rounding or a vintage", ok_diff)
        ratio = (mp.mpf("1.897907634269324")
                 / mp.mpf(data["predicted_bridge_ratio"]))
        print(f"\n    bridge ratio  block / witness = {mp.nstr(ratio, 8)}"
              f"   ({mp.nstr((ratio - 1) * 100, 3)} %)")
        check("the divergence is over 10 % — a different formula, not drift",
              abs(ratio - 1) > mp.mpf("0.1"))
        passed = [a.get("passed") for a in w.get("assertions", [])]
        print(f"    witness assertions: {passed}  (a producer checking itself "
              f"against itself cannot see this)")
        check("and the witness's own assertions all PASS, so nothing in CI is "
              "red while the published table and its producer differ by 21 %",
              all(passed))

    print("\n" + "=" * 78)
    print("§S  WHAT THIS SETTLES")
    print("=" * 78)
    print("  The block's provenance sentence is false: the values are not the")
    print("  witness's, and the witness declares q0Anchor 'proton', not the")
    print("  canonical CAL-2 pinning it names. Corrected in the block.")
    print()
    print("  Which z is right is NOT settled here. conj:q-beta-spectral-bridge")
    print("  DEFINES z = 1/(sqrt q + 1/sqrt q), which the table uses and the")
    print("  producer does not — so for once the compute has drifted from the")
    print("  stated definition rather than content lagging compute. A name")
    print("  collision hid it: the proposition calls its z 'the Markov-Jones")
    print("  parameter' and the producer's field for a DIFFERENT formula is")
    print("  named z_markov_jones.")

    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_description(
            "tbl:q-beta-spectral-bridge-table-data and the witness it cites compute "
            "different z under the same name and differ by 21 %. The block uses "
            "conj:q-beta-spectral-bridge's own definition z = 1/(sqrt q + 1/sqrt q) at "
            "q0 = 1.109978595557335 and reproduces every published value exactly; the "
            "producer q_beta_spectral_bridge_witness.py computes q^3/(q^2+1) at the "
            "PROTON pin, stores it in a field named z_markov_jones, and also reproduces "
            "its own values exactly. Both witness assertions PASS, so CI is green while "
            "publication and producer disagree. The block's claim that its values are "
            "the witness's digits, regenerated from the canonical CAL-2 pinning, is "
            "false on both counts (the witness declares q0Anchor: proton). Also "
            "RETRACTS this bean's earlier claim that the table was internally "
            "inconsistent with h^2 != (h)^2: h^2 is (h)^2 to 9.0e-18, and that claim "
            "came from significant-figure bucketing too coarse to separate pin A from "
            "pin B at h^2.")
        wb.add_data("block_q0", Q_BLOCK)
        wb.add_data("witness_q0_anchor", "proton")
        for lbl, pub, key in ROWS:
            wb.add_data(f"block_{key}", pub)
        for name, ok in checks:
            wb.add_assertion(name=name, computed=str(int(ok)), expected="1")
        wb.add_caveat(
            "Does NOT rule on which z is correct. The proposition defines one and the "
            "producer computes the other; whether the definition or the compute moved "
            "is an authoring question, and the Q_beta MeV figures differ by ~0.05 MeV "
            "between them.")
        wb.add_caveat(
            "Neither the producer, the proposition, nor the table's values are changed "
            "here — only the block's false provenance sentence.")
        print(f"\nWitness: {wb.save(extra={"q0Anchor": "ambiguous", "q0AnchorReason": (
            "comparison by design: tests the block's published values at the block's own quoted pin 1.109978595557335 (retired frozen muon pin A) against the witness's declared proton pin 1.10997858275138...")})}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    bad = [n for n, ok in checks if not ok]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
