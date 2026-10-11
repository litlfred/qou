#!/usr/bin/env python3
"""Attach the convention-D Markov trace to regenerated v9 certificates.

v9's own `tr_markov_f64` weights each normal-form word by z^len(w) with the
excised convention-C z = 1/(t + 1/t). That is not a Markov trace in any
convention (tr(s0 s1 s0) = h z^2 + z, not z^3). The genuine Ocneanu trace at
convention D, z = q^3/(q^2+1), is computed exactly by
computations/probes/v9_markov_trace_convention_d_probe.py for the nuclei whose
full product fits in memory with no mid-construction strip. This script copies
those values into the matching certificates as `tr_markov_conventionD` (a
60-digit decimal string, divided by 2^pn like the other fields). Certificates
the probe does not cover get no field; their `tr_markov_f64` stays as v9 wrote
it. Bean qou-m7py.

The probe traces the FULL crossing product. v9 strips words mid-construction
once the element grows past its threshold, and did so for 10B and 10Be, so for
those two the attached value is the trace of a different (larger) element than
the one the certificate's other fields describe. Each attached record says
which: `same_element_as_certificate` is true only where v9's dumped element
(V9_DUMP_ELEM, before the final strip) was checked equal to the probe's build
and v9 did no mid-construction strip. Verified 2026-10-11 for 4H, 5He, 5Li, 8Be
and 8Li.

Usage: python3 tools/hecke-engine/scripts/attach_convention_d_trace.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
WIT = ROOT / "computations/probes/v9-markov-trace-convention-d.witness.json"
CERTS = ROOT / "tools/hecke-engine"
# v9 element == probe's full product (dump compared word by word, no
# mid-construction strip). 10B and 10Be were stripped mid-construction.
SAME_ELEMENT = {"4H", "5He", "5Li", "8Be", "8Li"}


def main():
    w = json.loads(WIT.read_text())
    for row in w["data"]["rows"]:
        name = "certificate-%s.json" % row["nucleus"].lower()
        path = CERTS / name
        cert = json.loads(path.read_text())
        assert cert["pn_count"] == row["pn_count"], name
        cert["tr_markov_conventionD"] = {
            "value": row["tr_markov_D"],
            "z": "q^3/(q^2+1)",
            "q0": w["parameters"]["q0"],
            "object": "full crossing product, before any strip",
            "same_element_as_certificate": row["nucleus"] in SAME_ELEMENT,
            "source": "computations/probes/v9-markov-trace-convention-d.witness.json",
        }
        path.write_text(json.dumps(cert, indent=2, ensure_ascii=False) + "\n")
        print(name, row["tr_markov_D"][:22])


if __name__ == "__main__":
    main()
