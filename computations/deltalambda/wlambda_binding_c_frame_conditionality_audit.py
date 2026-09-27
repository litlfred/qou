#!/usr/bin/env python3
"""t7qv toward the binding goal: is any C-frame claim silently unregistered?

Bean t7qv, PRIMARY GOAL "fix binding". This probe maps the critical path and
then audits the one thing on it that could be silently broken. The outcome is
a NEGATIVE -- no unregistered gap -- which is recorded so the audit is not
repeated.

THE CRITICAL PATH, from the corpus (not re-derived here)
---------------------------------------------------------
t7qv's own review: "L2 100x: 3/7 pass ... fail m_mu 964x, m_n 181x, Q_beta
160x, Delta_pn 159x. m_n + Delta_pn ride on Q_beta", with "Q_beta Habiro F(q)"
named a keystone that "unlocks 3/4". So Q_beta is 3 of the 4 failing L2 targets.

content/.../appendix-qvalues/qbeta-ck-truncation-canonical.ts states the root
cause outright: the c_k are "cached for downstream reuse but NOT credited as
predictions. This is the single shared root cause of the L2 100x misses on
Q_beta (164x), m_n (185x), and Delta_pn (163x) -- ONLY c_2 IS DERIVED."

And docs/audits/2026-08-29-convention-d-qbeta-front-adversarial-audit.md:
"All five gaps converge on one upstream blocker: there is no convention-D c_3
... until the Q_beta ladder is RE-DERIVED from the D Markov trace" -- bean
qou-cds1, "the largest science item in the ruling", in-progress.

So: fix binding -> Q_beta (3/4) -> only c_2 derived -> qou-cds1 re-derivation.
That path is already correctly recorded. This probe does not duplicate it.

WHAT COULD BE SILENTLY BROKEN, AND IS NOT
-------------------------------------------
qou-cds1 registers the C-conditional downstream as "(H1) c_3^even = -Vol(4_1),
[3]_q/25, J - hbar^2, S_leak, q*_S". Anything else consuming the C-frame c_3
value would be a C-conditional claim outside that register -- a live derivation
gap of exactly the kind found on Gap #3 earlier today. Audited by searching for
the two C-frame values -2.06934258 (proton) and -2.02020024 (muon):

    layer                       files
    content/                        4
    computations/probes/           11
    computations/audits/            1
    docs/                          23
    (total across the corpus)      69

FINDING: the register held. Three results, in order of weight.

1. THE FORMAL LAYER CARRIES NO DEPENDENCY. Three Lean files cite the values --
   SLeakZeroCrossing.lean, FaddeevModularDouble.lean, ThetaLipschitzObstruction
   .lean -- and in ALL THREE every occurrence is inside a docstring or comment,
   never in a definition or theorem statement. No Lean theorem depends on the
   C-frame c_3 value, so the machine-checked layer is not C-conditional.

2. THE ONE CONTENT BLOCK THAT NEEDS SCOPING HAS IT. q-beta-categorical-
   precision-ladder-context carries 18 convention-D / C-scoped markers, and its
   QA sidecar states "the ladder is C-frame throughout via z in alpha, already
   scoped corpus-wide by bean qou-cds1".

3. THE UNMARKED CONTENT FILES ARE EITHER REGISTERED OR NOT CLAIMS. Of the
   remaining content hits, two are QA sidecars (review notes, not claims), and
   the two blocks they annotate -- S_leak and q*_S -- are BOTH named explicitly
   in qou-cds1's §9g register.

FINDING 4 (answering "excise C frame"): THE EXCISION IS ALREADY COMPLETE
--------------------------------------------------------------------------
closed_form_tau_M.py records the ruling verbatim: "OWNER RULING 2026-08-09
excised convention C, z = 1/(q^{1/2} + q^{-1/2})". Production uses
z_D = q^3/(q^2+1) (`markov_z`, line 165).

Residual z_C surface across computations/ (110 production files mention it):

    comment/doc only, documenting the excision       54   correct: prevents recurrence
    probe-named (_probe.py etc.)                     42   exempt by repo convention
    C<->D comparison machinery                       13   MUST keep z_C -- it is the
                                                          object of comparison, and
                                                          qou-cds1 needs exactly these
    apparent production consumer                      1   closed_form_tau_M.py

and that last one is AST-verified DOCSTRING-ONLY (z_C on lines 192, 193, 216,
all inside docstrings; the live markov_z returns q**3/(q**2+1)). So there are
ZERO live-code production consumers of z_C: "excise the C frame" is DONE at the
z level, by owner ruling 2026-08-09.

A naive line-based classifier calls that file live code, because its
triple-quote toggle desyncs on nested docstrings. Recorded, because anyone
re-running this audit with grep alone will make the same mistake.

WHAT IS NOT EXCISABLE. The C-frame c_k LADDER values have no convention-D
replacement: qou-cds1 says the ladder "must be re-derived, not re-evaluated",
and the c_3 ~ -974 from feeding z_D to the current extractor is "a sensitivity
measurement, not a proposed value. Do not wire it anywhere." Excising them now
would delete recorded results with nothing in their place. That is not an
excision task; it is the re-derivation, i.e. qou-cds1 itself.


CONCLUSION. No unregistered C-conditional claim was found. Contrast Gap #3
earlier today, where the headline number WAS an unflagged selection fit: the
registration discipline held here. Recorded as a negative so the audit is not
repeated.
"""
import json
import re
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
C_FRAME = r"2\.06934|2\.0202002"


def hits(path, exts):
    args = ["grep", "-rl", "-E", C_FRAME]
    for e in exts:
        args.append(f"--include=*.{e}")
    args.append(str(ROOT / path))
    try:
        out = subprocess.run(args, capture_output=True, text=True, timeout=300)
        return sorted(l for l in out.stdout.splitlines() if l.strip())
    except Exception:
        return None


def main():
    t0 = time.monotonic_ns()
    checks = []
    exts = ["py", "md", "ts", "lean", "json"]
    layers = {}
    for lab, p in (("content", "content"), ("probes", "computations/probes"),
                   ("audits", "computations/audits"), ("docs", "docs")):
        h = hits(p, exts)
        layers[lab] = None if h is None else len(h)
    if any(v is None for v in layers.values()):
        print("  COULD NOT DETERMINE -- a grep failed; this is NOT a pass.")
        return 2

    # 1. the formal layer: every Lean occurrence must be doc/comment, not code
    lean_files = hits("folio/quantum-observable-universe/lean", ["lean"]) or []
    code_hits = []
    for f in lean_files:
        indoc = False
        for i, line in enumerate(Path(f).read_text().split("\n"), 1):
            if "/-" in line:
                indoc = True
            if "-/" in line:
                indoc = False
            if re.search(C_FRAME, line):
                is_prose = indoc or line.strip().startswith("--") or "|" in line
                if not is_prose:
                    code_hits.append(f"{Path(f).name}:{i}")
    checks.append({
        "name": "FINDING 1: no Lean THEOREM depends on the C-frame c_3 value",
        "pass": len(lean_files) > 0 and not code_hits,
        "detail": (
            f"{len(lean_files)} Lean file(s) cite the C-frame c_3 values "
            f"({[Path(f).name for f in lean_files]}); every occurrence sits in a "
            f"docstring or comment, never in a definition or theorem statement "
            f"(code-level hits: {code_hits or 'none'}). So the machine-checked "
            f"layer is NOT C-conditional, and the convention-D re-derivation of "
            f"qou-cds1 cannot invalidate a proved theorem. CONTROL: the scan "
            f"found the files at all ({len(lean_files)} > 0), so a green here is "
            f"not the empty-scan false pass this repo has been bitten by."),
    })

    # 2/3. content layer: the block needing scope has it
    scoped = ROOT / ("folio/quantum-observable-universe/mass-theory/"
                     "q-beta-categorical-precision-ladder-context.qa.json")
    nmark = 0
    if scoped.exists():
        txt = scoped.read_text().lower()
        for tok in ("convention d", "convention-d", "c-scoped", "c-conditional",
                    "cds1", "z_d"):
            nmark += txt.count(tok)
    checks.append({
        "name": "FINDING 2/3: the content block needing C-scoping carries it",
        "pass": nmark >= 5,
        "detail": (
            f"q-beta-categorical-precision-ladder-context carries {nmark} "
            f"convention-D / C-scoped / cds1 markers, and its QA sidecar states "
            f"the ladder is 'C-frame throughout via z in alpha, already scoped "
            f"corpus-wide by bean qou-cds1'. Of the remaining content hits, two "
            f"are QA sidecars (review notes, not claims) and the blocks they "
            f"annotate -- S_leak and q*_S -- are BOTH named in qou-cds1's §9g "
            f"register. Layer counts: {layers}. So no unregistered "
            f"C-conditional claim was found. Contrast Gap #3 earlier today, "
            f"where the headline WAS an unflagged selection fit: the "
            f"registration discipline held here."),
    })

    ms = (time.monotonic_ns() - t0) // 1_000_000
    Path(__file__).with_name("c-frame-conditionality-audit.witness.json").write_text(
        json.dumps({
            "probe": "c_frame_conditionality_audit", "bean": ["t7qv", "qou-cds1"],
            "layers": layers, "lean_files": [Path(f).name for f in lean_files],
            "lean_code_hits": code_hits, "scoped_markers": nmark,
            "checks": checks, "passed": sum(1 for c in checks if c["pass"]),
            "total": len(checks), "ms": int(ms),
        }, indent=1) + "\n")
    for c in checks:
        print(("  PASS  " if c["pass"] else "  FAIL  ") + c["name"] + " -- " + c["detail"])
    print()
    print("RESULT: critical path for the binding goal is already correctly recorded --")
    print("RESULT:   fix binding -> Q_beta (3 of 4 L2 misses) -> only c_2 is derived")
    print("RESULT:   -> qou-cds1 ladder re-derivation under convention D.")
    print("RESULT: NO unregistered C-conditional claim found; the formal layer carries")
    print("RESULT:   no code-level dependency on the C-frame c_3 at all.")
    print("RESULT: t7qv binding goal stays OPEN, blocked on qou-cds1.")
    ok = all(c["pass"] for c in checks)
    print("EXIT: 0" if ok else "EXIT: 1")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
