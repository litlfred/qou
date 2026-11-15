#!/usr/bin/env python3
"""Write the two-row tower probe's convention-D traces into the certificates.

v9 fills `tr_markov_d` itself only when its build kept every word (A <= 8).
For every other certificate whose nucleus the tower probe has computed, this
fills the field from `computations/probes/markov-trace-two-row-tower.witness.json`
and records the method. The pn count is checked against the certificate's own
`pn_count` where it has one, so a value cannot land on the wrong normalisation.

Rows the Python probe lacks (A = 17..20) come from the Rust port's witness,
markov-trace-two-row-tower-rust.witness.json.

Usage: attach_tower_trace.py [--check]
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CERTS = ROOT / "tools/hecke-engine"
WIT = ROOT / "computations/probes/markov-trace-two-row-tower.witness.json"
RUST_WIT = ROOT / "computations/probes/markov-trace-two-row-tower-rust.witness.json"
Q0 = "1.1099785827513808075916690956107688798744991218736"
V9_METHOD = "v9: Ocneanu recursion on the strip-free T_w expansion"
TOWER_METHOD = ("two-row seminormal characters up the Hecke tower "
                "(computations/probes/markov_trace_two_row_tower_probe.py); "
                "agrees with the v9 method to 60 digits on the 12 nuclei both compute")
RUST_METHOD = ("two-row seminormal characters up the Hecke tower, diagonal-only "
               "(hecke-tower-trace, MPFR at 80 and 70 digits); agrees with the "
               "Python tower probe to >= 59 digits on all 63 isotopes both compute")


ORDER = ["computed", "value", "exact_z_t", "reason", "method", "z", "q0", "normalisation"]


def base():
    return {"computed": False, "z": "q^3/(q^2+1)", "q0": Q0,
            "normalisation": "divided by 2^pn_count, like the *_f64 fields"}


def ordered(t):
    """Field order as certificate.rs serialises MarkovTraceD."""
    return {k: t[k] for k in ORDER if k in t}


def splice(text, t):
    """Replace (or append) the tr_markov_d block textually, so that every
    other byte of the certificate -- f64 spellings included -- is kept."""
    block = json.dumps(ordered(t), indent=2, ensure_ascii=False).replace("\n", "\n  ")
    key = '"tr_markov_d": '
    i = text.find(key)
    if i >= 0:
        j = text.index("{", i)
        depth = 0
        for k in range(j, len(text)):
            if text[k] in "[{":
                depth += 1
            elif text[k] in "]}":
                depth -= 1
                if depth == 0:
                    return text[:j] + block + text[k + 1:]
        raise ValueError("unbalanced tr_markov_d block")
    end = text.rstrip().rindex("}")
    head = text[:end].rstrip()
    return head + ",\n  " + key + block + "\n" + text[end:]


def main():
    check = "--check" in sys.argv
    w = json.load(open(WIT))
    assert w["q0"] == Q0
    rows = {(r["z"], r["n"]): {**r, "method": TOWER_METHOD} for r in w["rows"]}
    rw = json.load(open(RUST_WIT))
    assert rw["q0"] == Q0 and rw["q0_anchor"] == "proton"
    for r in rw["rows"]:
        rows.setdefault((r["z"], r["n"]), {**r, "method": RUST_METHOD})
    changed = []
    for f in sorted(CERTS.glob("certificate-*.json")):
        d = json.load(open(f))
        iso = d.get("isotope")
        if not isinstance(iso, dict) or "z" not in iso or f.name.endswith("-crt.json"):
            continue  # residue-only certificate (4he-crt)
        key = (iso["z"], iso["n"])
        old = json.dumps(d.get("tr_markov_d"), sort_keys=True)
        t = d.get("tr_markov_d") or base()
        if t.get("computed") and t.get("method") in (None, V9_METHOD) and "exact_z_t" in t:
            t["method"] = V9_METHOD
        elif key in rows:
            r = rows[key]
            if "pn_count" in d:
                assert d["pn_count"] == r["pn"], (f.name, d["pn_count"], r["pn"])
            t = {**base(), "computed": True, "value": r["tr_markov_d"], "method": r["method"]}
        elif iso["a"] > 20:
            t = {**base(), "reason": "A > 20: beyond the two-row tower computations so far, "
                                     "and v9's build was stripped mid-construction"}
        else:
            continue
        if json.dumps(t, sort_keys=True) != old:
            changed.append(f.name)
            if not check:
                new = splice(f.read_text(), t)
                assert json.loads(new)["tr_markov_d"] == ordered(t), f.name
                f.write_text(new)
    print(len(changed), "certificates", "would change" if check else "changed")
    for c in changed:
        print(" ", c)
    return 1 if (check and changed) else 0


if __name__ == "__main__":
    sys.exit(main())
