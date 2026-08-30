#!/usr/bin/env python3
"""The 2026-05-19 TR_M[5] Markov-trace fix never reached `computations/` — five
live producers still carry `z**3`, and the wrong value MASKS the D-frame Gram
singularity.

`docs/audits/2026-05-19-trm5-markov-bug.md` corrected
`tools/pyhecke/python/pyhecke/gram.py`: on the Grobner-Shirshov normal-form
basis of H_3(q), the sixth weight is

    tr_M(sigma_0 sigma_1 sigma_0) = h*z^2 + z ,   h = q - 1/q

and NOT `z^3`. The derivation is three lines of the Markov axioms and is
reproduced in check 1 below. `pyhecke.gram.TR_M` carries the fix. Five
`computations/` producers on the SAME basis do not.

## Why this is not a cosmetic drift

The wrong weight is off by a factor of ~3 at the proton anchor under D, and
~4.4 under C -- not a precision issue, a different number.

More consequential: `pyhecke/gram.py`'s own banner records that the crate's
Rust mirror kept `z*z*z` and notes exactly what that buys --

    "This is what keeps the crate's Gram non-singular, so it has no radical
     and no quotient -- hence the trace fix and the quotient must land
     together (fixing the trace alone drops a singular Gram into a path with
     nothing to handle it)."

Check 3 below measures that on a live producer. `compound_shift_nf.gram_mp`
builds G[i][j] = tr_M(b_i b_j) and feeds it to an LP. With the committed
`z^3` it is rank 6 under BOTH conventions, so the file looks like a clean
z-swap candidate. With the CORRECT weight it is rank 6 under C and **rank 5
under D** -- the singularity that bean qou-cds2 tracks. The trace bug is
what hides it.

Check 4 is the cross-check that ties the two files together: with the correct
weight under C, `compound_shift_nf`'s determinant equals
`gram_h3_det_factorization`'s in magnitude to every digit. They are the same
Gram; they disagreed only because one carries the bug.

## Scope

This is a scope-(a) finding about five named files, not a claim that every
`z**3` in the corpus is wrong -- `z^3` is the correct weight for other
objects, and 14 further hits live under `computations/_deprecated/` and are
out of scope. Each site below was confirmed to use the SAME six-element NF
basis `[(), (0,), (1,), (0,1), (1,0), (0,1,0)]` before being listed.

Run:  PYTHONPATH=computations python3 -u computations/probes/trm5_zcubed_live_producer_audit.py
"""
from __future__ import annotations

import re

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
COMP = REPO / "computations"
for _p in (str(COMP), str(COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from q_parameter import q_at  # noqa: E402 — proton pin (stem not in ideal_muon)
from witness_base import WitnessBuilder  # noqa: E402

#: (file, line, symbol) -- confirmed on the same NF basis, live (not _deprecated).
LIVE_SITES = [
    ("computations/compound_shift_nf.py", 257, "tr_m_weights_mp"),
    ("computations/electron_sigma_f_chain.py", 107, "TR_M"),
    ("computations/jet_knot_invariants.py", 56, "tr_basis"),
    ("computations/atom_mass_derived.py", 102, "TR_M_3"),
    ("computations/basis_knot_tables.py", 54, "TR_M"),
]

NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]


def check1_derivation() -> dict:
    """The Markov axioms give h*z^2 + z, symbolically, with z free."""
    q, z = sp.symbols("q z")
    h = q - 1 / q
    # tr(s0 s1 s0) = tr(s1 s0^2)          [cyclicity]
    #              = tr(s1 (h s0 + 1))    [Hecke: s^2 = h s + 1]
    #              = h tr(s1 s0) + tr(s1)
    #              = h z^2 + z            [Markov: tr(s_i x) = z tr(x)]
    derived = sp.expand(h * z**2 + z)
    return {
        "derived_symbolic": str(derived),
        "equals_z_cubed": bool(sp.simplify(derived - z**3) == 0),
        "difference": str(sp.simplify(sp.factor(z**3 - derived))),
    }


def check2_magnitude(q0) -> dict:
    h = q0 - 1 / q0
    out = {}
    for name, zv in (("C", 1 / (mp.sqrt(q0) + 1 / mp.sqrt(q0))),
                     ("D", q0**3 / (q0**2 + 1))):
        wrong, right = zv**3, h * zv**2 + zv
        out[name] = {
            "z": mp.nstr(zv, 20),
            "committed_z_cubed": mp.nstr(wrong, 20),
            "correct_h_z2_plus_z": mp.nstr(right, 20),
            "correct_over_committed": mp.nstr(right / wrong, 12),
            "committed_rel_error_pct": mp.nstr((wrong - right) / right * 100, 10),
        }
    return out


def check3_gram_rank(q0) -> dict:
    """The trace bug masks the D Gram singularity in a LIVE producer."""
    import compound_shift_nf as C
    h = q0 - 1 / q0
    zs = {"C": 1 / (mp.sqrt(q0) + 1 / mp.sqrt(q0)), "D": q0**3 / (q0**2 + 1)}
    orig = C.tr_m_weights_mp
    rows = {}
    try:
        for zn, zv in zs.items():
            for fixed in (False, True):
                w = [mp.mpf(1), zv, zv, zv**2, zv**2,
                     (h * zv**2 + zv) if fixed else zv**3]
                C.tr_m_weights_mp = lambda dps=50, _w=w: list(_w)
                G = C.gram_mp(50)
                M = mp.matrix([[G[i, j] for j in range(6)] for i in range(6)])
                sv = mp.svd_r(M, compute_uv=False)
                rank = sum(1 for s in sv if abs(s) > mp.mpf(10) ** -30)
                key = f"z_{zn}/{'correct' if fixed else 'committed'}"
                rows[key] = {
                    "det": mp.nstr(mp.det(M), 12),
                    "rank": rank,
                    "min_singular_value": mp.nstr(min(abs(s) for s in sv), 6),
                }
    finally:
        C.tr_m_weights_mp = orig
    return rows


def check4_same_gram(ranks: dict) -> dict:
    """With the CORRECT weight under C, compound_shift_nf's |det| matches the
    independent gram_h3_det_factorization value -- so they are one Gram."""
    u, qs = sp.symbols("u q", positive=True)
    det_u = (-(u - 1) * (u + 1) * (u**3 + u - 1) ** 5 * (u**3 + u**2 + 1) ** 5
             * (u**6 - u**5 + u**4 - u**3 + 2 * u**2 - u + 1)
             * (u**6 + u**5 + 2 * u**4 + u**3 + u**2 + u + 1)
             / (u**10 * (u**2 + 1) ** 12))
    q0s = sp.Float(str(q_at(40)), 40)
    indep = sp.N(det_u.subs(u, sp.sqrt(q0s)), 20)
    mine = mp.mpf(ranks["z_C/correct"]["det"])
    return {
        "gram_h3_det_factorization_at_q0": str(indep),
        "compound_shift_nf_correct_weight_at_q0": mp.nstr(mine, 12),
        "magnitudes_agree": bool(abs(abs(mp.mpf(str(indep))) - abs(mine))
                                 < mp.mpf(10) ** -9),
        "note": ("sign differs by a basis-ordering orientation; the magnitude "
                 "identity is the claim"),
    }



# A REAL corpus scan, added 2026-08-30 (bean qou-isu5).
#
# The regression guard below iterates LIVE_SITES, a hardcoded five-name list.
# On 2026-08-30 it printed "all five fixed: True" while SEVEN other files on
# the same H_3 NF basis still carried the bug -- five of them found by hand
# (hh-trefoil-corrected, ch-bond-writhe-lp, intermediate_knot_detection,
# photon_operator_table, and the CORE MODULE substrate/hecke_core_symbolic),
# and two more that no spelling in the guard could have matched:
# electron_shell_sdp_capacity (`z ** 3` inside np.array) and
# qbeta_c3_barodd_hs_matrix_resolvent_probe (`z * z * z`).
#
# The guard's own scope note was honest -- "not a claim about every z**3 in
# the corpus" -- but its printed headline is what a reader acts on. So the
# scan below keys on the SHAPE of the six-element vector rather than on a
# file list or on `z**3` alone (which is an ordinary polynomial term almost
# everywhere it appears).
_SIX_VEC = re.compile(
    r"\[\s*(?:1\.0|1|_?ONE|mp\.mpf\(1\)|sp\.Integer\(1\))\s*,"
    r"\s*z\s*,\s*z\s*,"          # entries 2,3 = z
    r"\s*z\s*(?:\*\*\s*2|\*\s*z)\s*,"   # entry 4 = z^2, either spelling
    r"\s*z\s*(?:\*\*\s*2|\*\s*z)\s*,"   # entry 5 = z^2
    r"\s*(?P<last>[^\]]+)\]"
)
# a sixth entry that is a CUBE of z and nothing else
_CUBE = re.compile(r"^\s*z\s*(?:\*\*\s*3|\*\s*z\s*\*\s*z)\s*$")


def scan_corpus_for_six_vectors(repo):
    """Every 6-element H_3-shaped trace vector in the tree, with its 6th entry.

    Returns (bad, ok). A hit is `bad` when the 6th entry is a bare cube of z.
    Deliberate side-by-side comparisons name themselves on the same line
    (`retired`, `OLD`, `bug`, `stale`, `historical`) and are not counted.
    """
    bad, ok = [], []
    for path in sorted(repo.rglob("*.py")):
        rel = str(path.relative_to(repo))
        if "/_deprecated/" in f"/{rel}" or ".lake" in rel:
            continue
        try:
            lines = path.read_text().splitlines()
        except (OSError, UnicodeDecodeError):
            continue
        for i, line in enumerate(lines, 1):
            m = _SIX_VEC.search(line)
            if not m:
                continue
            last = m.group("last")
            rec = {"file": rel, "line": i, "sixth_entry": last.strip()}
            if _CUBE.match(last):
                if re.search(r"retired|OLD\b|bug|stale|historical",
                             line, re.I):
                    rec["deliberate_comparison"] = True
                    ok.append(rec)
                else:
                    bad.append(rec)
            else:
                ok.append(rec)
    return bad, ok



def _selftest() -> int:
    """The scan must be shown able to REPORT a bug before its 0 means anything.

    Four spellings, all of which were live in this corpus at some point, plus
    two controls that must NOT be flagged.  Run with `--selftest`.
    """
    import pathlib
    import tempfile
    cases = {
        "np_array_pow": "TR_M = np.array([1.0, z, z, z * z, z * z, z ** 3])",
        "spaced_triple": "    TR_M = [mp.mpf(1), z, z, z * z, z * z, z * z * z]",
        "sympy_pow": "TR_M_SYM = [ONE, z, z, z**2, z**2, z**3]",
        "plain_pow": "tr_basis = [1, z, z, z**2, z**2, z**3]",
        # controls
        "CORRECT_ctl": "TR_M = [1.0, z, z, z**2, z**2, h * z**2 + z]",
        "DELIB_ctl": '  "OLD  (retired: e-=z^3)": [1, z, z, z**2, z**2, z**3],',
    }
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        for k, line in cases.items():
            (root / f"{k}.py").write_text(line + "\n")
        bad, ok = scan_corpus_for_six_vectors(root)
    flagged = {b["file"].replace(".py", "") for b in bad}
    seen = {o["file"].replace(".py", "") for o in ok}
    want = {"np_array_pow", "spaced_triple", "sympy_pow", "plain_pow"}
    checks = [
        ("all four bug spellings caught", flagged == want),
        ("correct weight not flagged",
         "CORRECT_ctl" not in flagged and "CORRECT_ctl" in seen),
        ("deliberate comparison not flagged",
         "DELIB_ctl" not in flagged and "DELIB_ctl" in seen),
    ]
    ok_all = True
    for name, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
        ok_all = ok_all and passed
    if not ok_all:
        print(f"    flagged={sorted(flagged)}  want={sorted(want)}")
    return 0 if ok_all else 1


def main() -> int:
    mp.mp.dps = 60
    q0 = q_at(55)

    c1 = check1_derivation()
    c2 = check2_magnitude(q0)
    c3 = check3_gram_rank(q0)
    c4 = check4_same_gram(c3)

    # REGRESSION GUARD, not a live-site scan.
    #
    # This probe was written to ESTABLISH the finding, while all five sites
    # still carried z^3. They were fixed later in the same PR, at which point
    # reading `text[line - 1]` started returning the FIXED lines (and, once
    # explanatory comments shifted the files, unrelated lines entirely) while
    # the payload still said "live sites still on z^3". The witness contradicted
    # itself. Caught when a rebase re-ran the probe.
    #
    # So it now checks what is actually worth checking going forward: that each
    # file carries the CORRECT weight and no longer carries the bug. Keyed on
    # content, not line numbers, so it cannot rot the same way twice.
    sites = []
    repo = HERE.parent.parent
    all_fixed = True
    for path, line, sym in LIVE_SITES:
        text = (repo / path).read_text()
        # the bug: a six-element trace vector ending in a cube of z
        has_bug = any(
            pat in text.replace(" ", "")
            for pat in ("z**2,z**2,z**3", "z*z,z*z,z**3", "z**2,z**2,z**3]")
        )
        has_fix = any(
            pat in text.replace(" ", "")
            for pat in ("h*z**2+z", "h*z*z+z", "h_trm*z**2+z", "_h_trm*z**2+z")
        )
        all_fixed = all_fixed and has_fix and not has_bug
        sites.append({
            "file": path, "symbol": sym,
            "historical_line": line,
            "still_carries_z_cubed": has_bug,
            "carries_h_z2_plus_z": has_fix,
        })

    bad_sites, ok_sites = scan_corpus_for_six_vectors(repo)
    print(f"  CORPUS SCAN  H_3-shaped six-vectors found : {len(bad_sites) + len(ok_sites)}")
    print(f"               still ending in a cube of z  : {len(bad_sites)}")
    for b in bad_sites:
        print(f"               [BUG] {b['file']}:{b['line']}  -> {b['sixth_entry']}")
    if not bad_sites:
        print("               (deliberate retired-variant comparisons excluded)")

    payload = {
        "description": (
            "The 2026-05-19 TR_M[5] fix (h*z^2 + z, NOT z^3) reached "
            "pyhecke/gram.py and never reached computations/. Five live "
            "producers on the same H_3 NF basis still carry z^3, and the "
            "wrong weight masks the convention-D Gram singularity."
        ),
        "nf_basis": [list(b) for b in NF_BASIS],
        "regression_guard": {
            "note": ("These five carried TR_M[5] = z^3 when this probe was "
                     "written; all five are fixed in the same PR. The check is "
                     "now that the fix HOLDS, keyed on content rather than line "
                     "numbers — the line-keyed version contradicted its own "
                     "payload as soon as the fix landed."),
            "all_five_fixed": all_fixed,
            "sites": sites,
        },
        "corpus_scan": {
            "note": ("Shape-keyed scan of the whole tree, not a file list. Added "
                     "after the five-name guard printed all-clear while seven "
                     "other files on the same basis still carried the bug -- two "
                     "of them in spellings (`z ** 3` inside np.array, `z * z * z`) "
                     "that no pattern in the guard could match."),
            "six_vectors_found": len(bad_sites) + len(ok_sites),
            "still_cubed": len(bad_sites),
            "bug_sites": bad_sites,
            "clean_sites": ok_sites,
        },
        "check1_markov_derivation": c1,
        "check2_magnitude_at_q0": c2,
        "check3_gram_rank_live_producer": c3,
        "check4_same_gram_as_gram_h3": c4,
        "sequencing_constraint": (
            "pyhecke/gram.py records that the trace fix and the Gram quotient "
            "must land together: fixing the trace alone drops a singular Gram "
            "into a path with nothing to handle it. Check 3 measures exactly "
            "that on compound_shift_nf."
        ),
        "context": {
            "prior_audit": "docs/audits/2026-05-19-trm5-markov-bug.md",
            "beans": ["qou-t9r1", "qou-pmkh", "qou-cds2"],
            "scope": ("Two claims, different scopes. The REGRESSION GUARD is "
                      "scope-limited to five named files. The CORPUS SCAN is "
                      "tree-wide but shape-limited: it sees six-element vectors "
                      "[1,z,z,z^2,z^2,*] on the H_3 NF basis, so a trace built "
                      "elementwise, in a loop, or on another basis is still "
                      "invisible to it. It is NOT a claim about every z**3."),
        },
        "q0Anchor": "proton",
        "q0Value": str(q0),
    }

    out = WitnessBuilder.wrap_legacy(
        "trm5-zcubed-live-producer-audit", payload,
        script_path=__file__, engine="python+mpmath+sympy",
    ).save()

    print("=== TR_M[5]: the 2026-05-19 fix never reached computations/ ===")
    print(f"  CHECK 1  Markov axioms give     : {c1['derived_symbolic']}")
    print(f"           equals z^3?            : {c1['equals_z_cubed']}   "
          f"(difference {c1['difference']})")
    for k, v in c2.items():
        print(f"  CHECK 2  z_{k}: committed {v['committed_z_cubed'][:12]}  "
              f"correct {v['correct_h_z2_plus_z'][:12]}  "
              f"off by {v['committed_rel_error_pct'][:8]}%")
    print("  CHECK 3  compound_shift_nf Gram (LIVE producer):")
    for k, v in c3.items():
        print(f"           {k:22s} det {v['det']:>16}  rank {v['rank']}/6")
    print(f"  CHECK 4  same Gram as gram_h3?  : {c4['magnitudes_agree']}")
    print(f"  REGRESSION GUARD — all five fixed : {all_fixed}")
    for st in sites:
        flag = "BUG" if st["still_carries_z_cubed"] else ("ok" if st["carries_h_z2_plus_z"] else "??")
        print(f"           [{flag}] {st['file']}  {st['symbol']}")
    print(f"\n  witness -> {out}")
    return 0


if __name__ == "__main__":
    import sys as _sys
    if "--selftest" in _sys.argv:
        raise SystemExit(_selftest())
    raise SystemExit(main())
