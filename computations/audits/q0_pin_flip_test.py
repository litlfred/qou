#!/usr/bin/env python3
"""Dynamic pin-flip test: does a producer's OUTPUT move when the anchor moves?

Run:  python3 computations/audits/q0_pin_flip_test.py

The third check for a `q0Anchor: independent` verdict. The other two are
STATIC and both can pass on a producer that is nonetheless pin-dependent:

  * the import-cone trace sees q0 reached through `q_parameter` /
    `qou_substrate.constants`, and nothing else;
  * `producer_baked_pin_audit.py` sees a q0-VALUED literal in the source.

Neither sees a dependence that arrives through what the producer computes
*with*. Recommended by the sibling working #6519 (`qou-9ugp`) after measuring
exactly that: two probes declaring themselves pin-independent whose own
`_q0`-named fields moved **428.7 ppb** and 3.4 ppb under a re-pin -- 37x the
pin move itself in the first case.

The converse also holds and is worth knowing: a producer can READ q0 and still
not move. Both controls here read it; one of them records it and little else.
"Reads q0" and "depends on q0" are different properties, and only this test
separates them.

METHOD. q_parameter resolves the anchor by the running producer's stem:
`if _stem in _man.get("ideal_muon", [])` -> muon, else proton. So temporarily
adding a stem to `ideal_muon` flips its pin. Re-run, diff the payload with
volatile provenance masked, restore.

POSITIVE CONTROL IS MANDATORY. A producer that genuinely never reads q0 will
show no move -- and so will a broken harness. Controls are producers KNOWN to
read q0 (cone trace says so); if they do not move, the null result on the
subjects means nothing and the run is void.
"""
import json, os, re, subprocess, sys, pathlib, shutil

ROOT = pathlib.Path("/home/user/qou")
MAN = ROOT / "computations/q0_anchor_manifest.json"
ENV = {**os.environ, "PYTHONPATH":
       "/home/user/qou/computations/substrate:/home/user/qou/computations:"
       "/home/user/qou/tools/qou-substrate/python"}

VOL = {"computedAt","commitSha","scriptHash","scriptCommitSha","durationMs","ms",
       "wall","seconds","elapsed_seconds","build_s","build_seconds","measured_at",
       "timestamp","start_time_monotonic","pyhecke_native_build","q0Anchor",
       "q0AnchorReason","q0Value","q0_anchor","q0_pin","environment","invocation"}
T = re.compile(r'\b\d+(?:\.\d+)?\s*s\b')
def norm(o):
    if isinstance(o, dict): return {k: norm(v) for k, v in o.items() if k not in VOL}
    if isinstance(o, list): return [norm(x) for x in o]
    if isinstance(o, str):  return T.sub("<T>", o)
    return o

CONTROLS = [  # KNOWN to read q0 (cone trace); must MOVE or the run is void
    ("computations/probes/coulomb_from_crossing_counts_probe.py",
     "computations/probes/coulomb-from-crossing-counts.witness.json", []),
    ("computations/probes/arc_count_diagnostic_degeneracy_probe.py",
     "computations/probes/arc-count-diagnostic-degeneracy.witness.json", []),
]
SUBJECTS = [  # my 7 `independent` verdicts; must NOT move
    ("computations/probes/aggregator_convexity_divided_difference_probe.py",
     "computations/probes/aggregator-convexity-divided-difference.witness.json", []),
    ("computations/probes/aggregator_family_exclusion_probe.py",
     "computations/probes/aggregator-family-exclusion.witness.json", []),
    ("computations/probes/pair_locality_shortfall_probe.py",
     "computations/probes/pair-locality-shortfall.witness.json", []),
    ("computations/probes/carrier_crossing_quantisation_probe.py",
     "computations/probes/carrier-crossing-quantisation.witness.json", []),
    ("computations/em_linking_fh_mirror_split_charge_blindness.py",
     "computations/em-linking-fh-mirror-split-charge-blindness.witness.json", []),
    ("computations/em_linking_upper_bound_precision_budget.py",
     "computations/em-linking-upper-bound-precision-budget.witness.json", []),
    ("computations/deltalambda/wlambda_covariance_epic_M1_edge_ratio_decomposition.py",
     "computations/deltalambda/m1-edge-ratio-decomposition.witness.json", ["46"]),
]

_PATCHED = {"text": None}


def restore():
    """Revert witnesses AND re-apply the manifest patch.

    BUG THIS FIXES (caught by the positive control, which is why it exists):
    `computations/q0_anchor_manifest.json` lives UNDER `computations/`, so
    `git checkout -- computations/` reverts the pin patch along with the
    witnesses. In the first version, every producer after the first therefore
    ran at the UNFLIPPED pin and trivially showed "no move" -- a vacuous pass
    that would have been reported as seven confirmed verdicts. The second
    control read "no move" where it had to move, and that is what exposed it.
    """
    subprocess.run(["git", "checkout", "--", "computations/"], cwd=ROOT)
    if _PATCHED["text"] is not None:
        MAN.write_text(_PATCHED["text"])

def run_one(prod, wit, args):
    before = json.loads((ROOT / wit).read_text())
    d = (ROOT / prod).parent
    r = subprocess.run([sys.executable, "-u", pathlib.Path(prod).name, *args],
                       cwd=d, env=ENV, capture_output=True, text=True, timeout=900)
    after = json.loads((ROOT / wit).read_text())
    moved = norm(before) != norm(after)
    return moved, r.returncode

def main():
    man = json.loads(MAN.read_text())
    orig = MAN.read_text()
    stems = [pathlib.Path(p).stem for p, _, _ in CONTROLS + SUBJECTS]
    man["ideal_muon"] = sorted(set(man.get("ideal_muon", [])) | set(stems))
    MAN.write_text(json.dumps(man, indent=2) + "\n")
    _PATCHED["text"] = MAN.read_text()
    print(f"manifest patched: {len(stems)} stems forced to ideal_muon\n")
    results = {}
    try:
        for label, group in (("CONTROL", CONTROLS), ("SUBJECT", SUBJECTS)):
            for prod, wit, args in group:
                try:
                    moved, rc = run_one(prod, wit, args)
                except subprocess.TimeoutExpired:
                    moved, rc = None, "timeout"
                results[prod] = (label, moved, rc)
                mark = {True: "MOVED   ", False: "no move ", None: "TIMEOUT "}[moved]
                print(f"  {label:7s} {mark} rc={rc}  {pathlib.Path(prod).name}")
                restore()   # producers write SIBLING witnesses; restore after each
    finally:
        _PATCHED["text"] = None      # stop re-applying before the final restore
        restore()
        MAN.write_text(orig)
    print("\nmanifest and computations/ restored")
    ctl = [v[1] for v in results.values() if v[0] == "CONTROL"]
    sub = [(k, v[1]) for k, v in results.items() if v[0] == "SUBJECT"]
    print("\n" + "=" * 70)
    if not all(ctl):
        print(f"VOID — only {sum(1 for c in ctl if c)}/{len(ctl)} controls moved.")
        print("EVERY control must move: a control that does not is evidence the")
        print("pin was not flipped for it, and the subjects run under the same")
        print("harness. A partial pass here is exactly the bug this run had.")
        return 2
    print(f"controls moved: {len(ctl)}/{len(ctl)}  -> harness verified on every control")
    bad = [k for k, m in sub if m]
    if bad:
        print(f"\n*** {len(bad)} SUBJECT(S) MOVED — the `independent` verdict is WRONG for:")
        for b in bad: print("     ", b)
        return 1
    print(f"subjects moved: 0/{len(sub)}  -> all 7 `independent` verdicts hold")
    return 0

if __name__ == "__main__":
    sys.exit(main())
