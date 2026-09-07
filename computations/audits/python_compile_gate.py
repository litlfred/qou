#!/usr/bin/env python3
"""python_compile_gate.py — every tracked .py must survive `compile()`.

Bean `qou-sidu`. Not `ast.parse` — that is the whole point.

WHY A SECOND SYNTAX CHECK, WHEN THE CORPUS ALREADY HAS SEVERAL
--------------------------------------------------------------
`ast.parse` and `compile` disagree, and the gap is a real one this repo
paid for. Future-statement placement is enforced at COMPILE time, not at
parse time:

    import os as _os_sidu
    \"\"\"module docstring\"\"\"
    from __future__ import annotations

`ast.parse` accepts that. `compile` rejects it with

    SyntaxError: from __future__ imports must occur at the beginning of the file

and so does the interpreter, so the file cannot be imported OR run.

On 2026-09-07 the qou-sidu atomic-write transform inserted its
`import os as _os_sidu` as LINE 1 — above the module docstring — in 35
files, and **12 of them could not be compiled at all**:

    alpha_em/alpha_em_b2_canonical_scale_ratio_probe
    h4_markov_character_decomposition
    probe_option_e_phase2_crystal_vertex_candidates
    probes/qbeta_habiro_integrality_kill_test
    probes/symbolic_nf_q_degree_magic_probe
    qbeta/qbeta_chi_witness_convention_split_probe
    qbeta/qbeta_computable_observables_vs_row_cap_probe
    qbeta/qbeta_derived_w_overdetermined_test_probe
    qbeta/qbeta_l1_ceiling_is_one_point_of_a_family_probe
    qbeta/qbeta_row_cap_sweep_of_physical_numbers_probe
    qbeta/tl_quotient_gram_determinant_general_n_probe
    witness_import_cone_staleness_audit

Every static audit here validates with `ast.parse`, so all of them
reported those files as fine. They were found by RUNNING one, weeks
later. In the meantime one of the twelve
(`qbeta-row-cap-sweep-of-physical-numbers`) kept a committed
`allPassed: true` while the corpus moved 435 commits underneath it —
a witness that had not lied so much as become impossible to ask.

WHY NOT THE IMPORTABILITY AUDIT
-------------------------------
`computations/audits/producer_importability_audit.py` imports each
producer and would in principle have caught all twelve. Two reasons it
did not, and neither is fixable by pointing at it harder:

* It is **wired into no gate array.** `scripts/precision-gates.sh`
  mentions it only inside a comment. Same shape AGENTS.md records for
  `witness_hollowness_audit.py`: a gate wired nowhere is a gate nobody
  runs.
* Importing is environment-dependent and noisy — its own baseline
  carries 13 `ModuleNotFoundError` findings that are its RESULT, and
  its docstring records an earlier pass that reported 24 bogus
  SyntaxErrors. A check with a known false-positive history is one
  people learn to skim.

This gate executes nothing, imports nothing, and reads no environment.
`compile()` failing IS the defect: the interpreter cannot run the file.
There is no judgement in it and therefore no false positives, which is
why it can be blocking at zero rather than baselined.

THE CONTRACT IS ZERO, NOT A RATCHET
-----------------------------------
Measured 2026-09-07 over 5183 tracked `.py`: **0 failures**, and 0 files
where `ast.parse` and `compile` disagree. A baseline would only record
permission to break it. Any finding is a file Python cannot load.

    python3 computations/audits/python_compile_gate.py            # report
    python3 computations/audits/python_compile_gate.py --strict   # exit 1 on any
    python3 computations/audits/python_compile_gate.py --self-test
"""
from __future__ import annotations

import argparse
import ast
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent

#: Excluded because they are not part of the runnable corpus. `_deprecated`
#: is retired code the repo keeps for provenance; the vendored tree is
#: generated and is checked at its source instead.
SKIP_DIRS = {"_deprecated", "node_modules", ".git"}


def check_source(src: str, filename: str = "<src>") -> str | None:
    """None if `compile` accepts it, else the SyntaxError message.

    `ast.parse` is deliberately NOT the test. Kept alongside only so the
    report can name the disagreement, which is the interesting case.
    """
    try:
        compile(src, filename, "exec")
    except (SyntaxError, ValueError) as exc:      # ValueError: NUL bytes
        return f"{type(exc).__name__}: {exc.args[0] if exc.args else exc}"
    return None


def parses_but_will_not_compile(src: str, filename: str = "<src>") -> bool:
    """The blind spot itself: accepted by `ast.parse`, rejected by `compile`."""
    try:
        ast.parse(src)
    except (SyntaxError, ValueError):
        return False
    return check_source(src, filename) is not None


def _tracked_py() -> list[str]:
    out = subprocess.run(["git", "ls-files", "*.py"], cwd=ROOT,
                         capture_output=True, text=True).stdout.split()
    return [f for f in out if not any(d in f.split("/") for d in SKIP_DIRS)]


def _selftest() -> int:
    cases = [
        # (source, expect_compile_failure, expect_blind_spot)
        ("x = 1\n", False, False),
        ('"""doc."""\nfrom __future__ import annotations\nx = 1\n', False, False),
        # the qou-sidu shape: an import hoisted above the docstring
        ('import os as _o\n"""doc."""\nfrom __future__ import annotations\n',
         True, True),
        # __future__ after a plain statement, no docstring involved
        ("import os\nfrom __future__ import annotations\n", True, True),
        # ordinary syntax error: both agree, so it is NOT the blind spot
        ("def f(:\n    pass\n", True, False),
        # a docstring alone before __future__ is fine
        ('"""a"""\n"""b"""\nfrom __future__ import annotations\n', True, True),
        # __future__ first is always fine
        ("from __future__ import annotations\nimport os\n", False, False),
        # comments and blank lines before the docstring are fine
        ('#!/usr/bin/env python3\n# c\n\n"""d."""\n'
         'from __future__ import annotations\n', False, False),
        # no __future__ at all: a hoisted import is legal, just docstring-losing
        ('import os as _o\n"""doc."""\nx = 1\n', False, False),
    ]
    ok = 0
    for i, (src, want_fail, want_blind) in enumerate(cases):
        got_fail = check_source(src, f"<case{i}>") is not None
        got_blind = parses_but_will_not_compile(src, f"<case{i}>")
        if got_fail == want_fail and got_blind == want_blind:
            ok += 1
        else:
            print(f"  FAIL case {i}: compile_fails={got_fail} "
                  f"(want {want_fail}), blind_spot={got_blind} "
                  f"(want {want_blind})\n    {src!r}")
    # The docstring-demotion case is worth pinning separately: legal Python,
    # so this gate must NOT claim it, even though qou-sidu caused both.
    demoted = 'import os as _o\n"""doc."""\nx = 1\n'
    tree = ast.parse(demoted)
    if ast.get_docstring(tree) is None and check_source(demoted) is None:
        ok += 1
    else:
        print("  FAIL: docstring-demotion must be legal and unclaimed here")
    total = len(cases) + 1
    print(f"self-test: {ok}/{total}")
    return 0 if ok == total else 1


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    # BOTH spellings: `scripts/precision-gates.sh` calls `--self-test` while
    # `.github/workflows/word-provenance-gate.yml` calls `--selftest`, and a
    # script offering only one fails its gate on arrival for a reason that
    # has nothing to do with what it detects.
    ap.add_argument("--self-test", "--selftest", action="store_true",
                    dest="selftest")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on ANY finding (the contract is zero)")
    ap.add_argument("paths", nargs="*")
    a = ap.parse_args(argv)
    if a.selftest:
        return _selftest()

    files = a.paths or _tracked_py()
    findings, blind = [], []
    for f in files:
        p = pathlib.Path(f)
        if not p.is_absolute():
            p = ROOT / f
        try:
            src = p.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        err = check_source(src, str(f))
        if err is None:
            continue
        findings.append({"file": str(f), "error": err})
        if parses_but_will_not_compile(src, str(f)):
            blind.append(str(f))

    if a.json:
        print(json.dumps({"scanned": len(files), "findings": findings,
                          "ast_parse_disagrees": blind}, indent=2))
        return 1 if (findings and a.strict) else 0

    print("=" * 78)
    print("tracked .py that `compile()` REJECTS — the interpreter cannot load them")
    print("=" * 78)
    print(f"  scanned                     : {len(files)} tracked .py")
    print(f"  FINDINGS                    : {len(findings)}")
    print(f"  of which ast.parse ACCEPTS  : {len(blind)}   <- invisible to every "
          f"ast.parse-based audit here")
    for x in findings:
        mark = "  [ast.parse says fine]" if x["file"] in blind else ""
        print(f"\n  {x['file']}{mark}\n      {x['error']}")
    if findings:
        print("\n  Fix the file. There is no baseline: a file that does not "
              "compile\n  cannot be imported or run, so there is no state in "
              "which this is\n  acceptable to record rather than repair.")
    return 1 if (findings and a.strict) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
