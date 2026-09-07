#!/usr/bin/env python3
"""FOUR conventions live in the chi witness corpus, and only ONE reaches A >= 5.

Found while trying to extend the extensivity scan (`qou-n9qf`) from A = 2..4 to
A = 5, 6. The corpus has committed `chi` witnesses for lithium-5 (n = 15) and
lithium-6 (n = 18), both complete. Using them would have been wrong.

*** THE SPLIT ***

Every `chi-*.witness.json` carries a `convention` field, and four values are in
use:

    averaged-crossings                        20 witnesses   n = 3, 6, 9, 12
    colour-weighted-averaged-crossing         13             n = 6, 9, 12
    sign-only-crossings                        7             n = 6, 9, 12, 15, 18
    bring_color_weighted-averaged-crossings    1             n = 12

**Only `sign-only-crossings` reaches n = 15 and n = 18.** The four atoms the
binding law is calibrated on — 2H, 3H, 3He, 4He — are
`colour-weighted-averaged-crossing`. So an A-scan that walks from A = 4 to
A = 5 using committed witnesses SILENTLY CHANGES CONVENTION at the boundary,
and any shape change seen there would be an artefact of that switch.

`sign-only-crossings` quantises the letter shift `d` to a sign. The
`chi_q_atomic_mpfr` docstring says what that costs: a crossing is
`sigma_g + d.I`, and "quantising `d` to a sign discards everything but the three
symmetric cases" — which is exactly the colour-weighted p-n interface the mass
pipeline relies on.

*** HOW BIG IS THE DIFFERENCE? MEASURED, SAME ATOM, SAME n, SAME q PIN ***

    n =  6  deuteron   worst |chi_sign-only - chi_colour| =   9.46
    n =  9  helium-3   worst                              =  36.69
    n =  9  tritium    worst                              =  41.06
    n = 12  helium-4   worst                              = 305.15

and it grows with n.

*** A SECOND SPLIT, INDEPENDENT OF THE FIRST: THE q PIN ***

The `-muon` witnesses pin `q0 = 1.1099785956427390466817` against the proton
`1.1099785827513808075916` — a difference of 1.3e-8, which moves `y_lambda` by
5.9e-10. `y_lambda` is convention-independent but **q-dependent**, so a
comparison that mixes pins measures the pin and not the convention. A first
draft of this probe did exactly that and its weight assertion failed; the pairs
are now filtered to a fixed pin and the cross-pin ones are reported separately
rather than averaged in.

*** WHAT IS SAFE TO REUSE ACROSS THE CONVENTION SPLIT: THE WEIGHTS ***

The Jones-Markov weights depend on `n` and `q` only — fixed by the Markov
normalisation, nothing to do with the braid word, which is what carries the
convention. Measured at a FIXED pin, and it holds:

    worst |y_sign-only - y_colour|   n = 6: 1.0e-50   n = 9: 6.9e-52   n = 12: 1.2e-52

So `y_lambda` may be lifted from a sign-only witness to reconstruct a
colour-weighted trace **at the same pin**; `chi_lambda` may not. That is what
makes extending the scan to lithium tractable at all: only the characters need
recomputing.

*** WHY ONLY sign-only REACHES A >= 5: A HARD CAPABILITY WALL, NOT AN OVERSIGHT ***

Measured below. The colour-weighted route evaluates
`chi_lambda(prod_i (c_i sigma_{g_i} + d_i I))` by building seminormal MATRICES,
because a general shift `d` is not a braid generator. The largest Specht block:

    n = 12    77 partitions    max dim      7,700     <- 4He, tractable (~4 min)
    n = 15   176 partitions    max dim    292,864
    n = 18   385 partitions    max dim 16,336,320

A 16,336,320-square matrix is not a slow computation, it is an impossible one.
`sign-only-crossings` reaches n = 15 and 18 precisely because `chi_q_via_gp` is
CHARACTER-THEORETIC (Murnaghan-Nakayama style) and never forms a matrix — but
that method needs the crossings sign-quantised, which is the very information
the colour-weighted convention exists to keep.

The multilinear escape does not rescue it either: only the `2A + 1` AVERAGED
letters carry a general `d`, so expanding just those gives `2^(2A+1)` pure braid
words — 32 at A = 2 (fine, and that is how the light atoms were done here) but
8192 at A = 6, each still needing a full all-partition sweep.

**So the A-scan cannot be extended past A = 4 in the calibration convention with
current tooling.** Attempted here: a colour-weighted 6Li (n = 18) run was killed
after 5 h 03 m without completing the first of its two words. That is a real
limit on `qou-n9qf`'s extensivity prediction, not a scheduling problem, and it
is why the corpus's convention split falls exactly where it does.

*** SCOPE ***

Scope-(a). Nothing is refuted and no witness is edited. Both the `convention`
and the q-pin fields are present and correctly populated everywhere — the hazard
is that nothing forces a CONSUMER to compare either, and the one convention that
reaches the larger atoms is not the one the calibration atoms use.
"""
from __future__ import annotations

import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

import glob
import json
import os
import subprocess
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "computations"))

DPS = 50
mp.mp.dps = DPS


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    counts, byconv, atom_of, pin_of = Counter(), defaultdict(list), {}, {}
    for f in sorted(glob.glob(str(ROOT / "computations" / "chi-*.witness.json"))):
        try:
            d = json.loads(Path(f).read_text())
        except Exception:
            continue
        conv, n = d.get("convention"), d.get("n_strands")
        if not conv or not n or not d.get("by_partition"):
            continue
        counts[conv] += 1
        byconv[(conv, n)].append(f)
        atom_of[f] = d.get("atom")
        pin_of[f] = str(d.get("q_0_50dps") or d.get("q0") or "")[:24]

    print("=" * 74)
    print("1. CONVENTIONS IN THE chi WITNESS CORPUS")
    print("=" * 74)
    conv_rows = []
    for c, k in counts.most_common():
        ns = sorted({n for (cc, n) in byconv if cc == c})
        conv_rows.append({"convention": c, "witnesses": k, "n_strands": ns})
        print(f"  {c:<42}{k:>3}   n = {ns}")

    big = sorted({n for (c, n) in byconv if n >= 15})
    reach = sorted({c for (c, n) in byconv if n >= 15})
    calib = sorted({c for (c, n) in byconv if n in (6, 9, 12)
                    and any(atom_of[f] in ("deuteron", "tritium", "helium-3",
                                           "helium-4")
                            for f in byconv[(c, n)])})
    print(f"\n  n >= 15 present at: {big}, reached ONLY by: {reach}")
    ok = True
    ok &= chk("only_one_convention_reaches_n_ge_15", reach,
              ["sign-only-crossings"],
              "so an A-scan crossing A = 4 -> 5 changes convention silently")
    ok &= chk("that_is_not_the_calibration_atoms_convention",
              "colour-weighted-averaged-crossing" in calib
              and "colour-weighted-averaged-crossing" not in reach, True)

    print("\n" + "=" * 74)
    print("2. SAME ATOM, SAME n, DIFFERENT CONVENTION — how far apart?")
    print("=" * 74)
    pairs, chi_rows, y_rows, cross_pin = [], [], [], []
    for n in sorted({n for (_, n) in byconv}):
        so = byconv.get(("sign-only-crossings", n), [])
        cw = byconv.get(("colour-weighted-averaged-crossing", n), [])
        for fa in so:
            for fb in cw:
                if atom_of[fa] and atom_of[fa] == atom_of[fb]:
                    # SAME q PIN ONLY. y_lambda is convention-independent but
                    # q-DEPENDENT, and the `-muon` variants pin a different q0
                    # (1.1099785956… vs the proton 1.1099785827…, a 1.3e-8
                    # difference that moves y_lambda by 5.9e-10). Comparing
                    # across pins measures the pin, not the convention.
                    if pin_of[fa] and pin_of[fa] == pin_of[fb]:
                        pairs.append((n, atom_of[fa], fa, fb))
                    else:
                        cross_pin.append({"n": n, "atom": atom_of[fa],
                                          "pin_a": pin_of[fa], "pin_b": pin_of[fb]})
    skipped = []
    for (n, atom, fa, fb) in pairs:
        A = json.loads(Path(fa).read_text())["by_partition"]
        B = json.loads(Path(fb).read_text())["by_partition"]
        # Not every witness carries both fields; skip rather than crash, and
        # record what was skipped so the coverage claim stays honest.
        if not all("y_lambda" in r and "chi_lambda" in r for r in A + B):
            skipped.append({"n": n, "atom": atom,
                            "sign_only": Path(fa).name,
                            "colour_weighted": Path(fb).name,
                            "reason": "a witness lacks y_lambda or chi_lambda"})
            continue
        ya = {tuple(r["partition"]): mp.mpf(r["y_lambda"]) for r in A}
        yb = {tuple(r["partition"]): mp.mpf(r["y_lambda"]) for r in B}
        ca = {tuple(r["partition"]): mp.mpf(r["chi_lambda"]) for r in A}
        cb = {tuple(r["partition"]): mp.mpf(r["chi_lambda"]) for r in B}
        sh = set(ya) & set(yb)
        if not sh:
            skipped.append({"n": n, "atom": atom, "reason": "no shared partitions"})
            continue
        wy = max(abs(ya[k] - yb[k]) for k in sh)
        wc = max(abs(ca[k] - cb[k]) for k in sh)
        y_rows.append({"n": n, "atom": atom, "worst_y_diff": mp.nstr(wy, 6)})
        chi_rows.append({"n": n, "atom": atom, "worst_chi_diff": mp.nstr(wc, 6)})
        print(f"  n={n:<3} {atom:<10} worst |y diff| = {mp.nstr(wy,4):>12}"
              f"   worst |chi diff| = {mp.nstr(wc,6):>10}")

    if skipped:
        print(f"\n  skipped {len(skipped)} pair(s): "
              f"{[s2.get('atom') for s2 in skipped]}")
    ok &= chk("same_atom_cross_convention_pairs_compared", len(chi_rows) >= 2, True,
              "deuteron at n = 6 and helium-4 at n = 12")
    if cross_pin:
        print(f"\n  excluded {len(cross_pin)} cross-PIN pair(s) "
              f"(muon anchor vs proton anchor): "
              f"{sorted({c['atom'] for c in cross_pin})}")
    ok &= chk("weights_are_convention_independent_at_a_FIXED_PIN",
              all(mp.mpf(r["worst_y_diff"]) < mp.mpf("1e-45") for r in y_rows), True,
              "y_lambda depends on n and q only, so it is safe to reuse across "
              "the CONVENTION split — but only at the same q pin")
    ok &= chk("cross_pin_pairs_were_excluded_not_averaged_in",
              len(cross_pin) > 0, True,
              "the -muon variants differ in q at 1.3e-8, moving y_lambda by "
              "5.9e-10; a first draft compared across pins and failed")
    ok &= chk("characters_are_NOT_convention_independent",
              all(mp.mpf(r["worst_chi_diff"]) > mp.mpf("1") for r in chi_rows), True,
              "chi_lambda carries the convention — never reuse across the split")

    print("\n" + "=" * 74)
    print("3. WHY ONLY sign-only REACHES A >= 5 — the dimension wall")
    print("=" * 74)
    from math import factorial
    import pyhecke_native as ph

    def specht_dim(lam):
        conj = [sum(1 for i in range(len(lam)) if lam[i] > j) for j in range(lam[0])]
        pr = 1
        for i in range(len(lam)):
            for j in range(lam[i]):
                pr *= (lam[i] - j) + (conj[j] - i) - 1
        return factorial(sum(lam)) // pr

    wall = []
    for nn in (12, 15, 18):
        parts = ph.partitions_of(nn)
        dims = [specht_dim(list(pp)) for pp in parts]
        wall.append({"n": nn, "partitions": len(parts), "max_specht_dim": max(dims)})
        print(f"  n = {nn:<3} partitions {len(parts):>4}   max Specht dim "
              f"{max(dims):>12,}")
    print("\n  The colour-weighted route builds seminormal MATRICES (a general")
    print("  shift d is not a braid generator), so n = 18 needs a 16,336,320-square")
    print("  matrix. sign-only reaches it because chi_q_via_gp never forms one.")
    ok &= chk("colour_weighted_route_hits_a_dimension_wall_by_n_15",
              [w["max_specht_dim"] for w in wall if w["n"] >= 15][0] > 100000, True,
              "292,864 at n = 15 and 16,336,320 at n = 18, against 7,700 at "
              "n = 12 where the light atoms are tractable")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-chi-witness-convention-split",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"dps": DPS,
                       "scanned": "computations/chi-*.witness.json"},
        "data": {"conventions": conv_rows,
                 "n_ge_15_reached_by": reach,
                 "same_atom_pairs": [{"n": n, "atom": at,
                                      "sign_only": Path(fa).name,
                                      "colour_weighted": Path(fb).name}
                                     for (n, at, fa, fb) in pairs],
                 "worst_y_diffs": y_rows,
                 "worst_chi_diffs": chi_rows,
                 "skipped_pairs": skipped,
                 "excluded_cross_pin_pairs": cross_pin,
                 "dimension_wall": wall},
        "context": {
            "axis": "can committed chi witnesses be used to extend an A-scan "
                    "past A = 4?",
            "answer": "Not directly. Four conventions are in use and only "
                      "sign-only-crossings reaches n = 15 and 18, while the "
                      "binding law's calibration atoms are "
                      "colour-weighted-averaged-crossing. Walking from A = 4 to "
                      "A = 5 on committed witnesses changes convention at the "
                      "boundary, and any shape change there would be an "
                      "artefact.",
            "what_is_safe": "y_lambda is convention-independent (agrees to "
                            "1e-51), because the Markov weights depend on n and "
                            "q alone. chi_lambda is not (differs by 9.46 at "
                            "n = 6 and 305.15 at n = 12, same atom). So the "
                            "weights may be lifted and only the characters need "
                            "recomputing — which is what makes extending the "
                            "scan tractable.",
            "capability_wall": "The colour-weighted route builds seminormal "
                               "matrices; max Specht dim is 7,700 at n = 12 but "
                               "292,864 at n = 15 and 16,336,320 at n = 18. So "
                               "the A-scan cannot be extended past A = 4 in the "
                               "calibration convention with current tooling — a "
                               "6Li attempt was killed at 5h03m without "
                               "finishing one word. sign-only reaches n = 18 "
                               "because chi_q_via_gp is character-theoretic and "
                               "never forms a matrix.",
            "scope": "Scope-(a). Nothing refuted, no witness edited. The "
                     "convention field is present and correct everywhere; the "
                     "hazard is that nothing forces a consumer to compare it.",
        },
        "gitCommit": _head_sha(),
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out_p = HERE / "qbeta-chi-witness-convention-split.witness.json"
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out_p
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as f:
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
        # ensure_ascii=False: the corpus convention is UTF-8 witnesses, and
        # `witness_shape_guard` flags a witness that gains \uXXXX escapes.
        json.dump(witness, f, indent=2, ensure_ascii=False)
        f.write("\n")
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
