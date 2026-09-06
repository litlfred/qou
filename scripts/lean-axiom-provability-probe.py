#!/usr/bin/env python3
"""Try to PROVE each Lean `axiom`.  An axiom Lean can close is not an axiom.

Why this exists
---------------
`lean-axiom-degenerate-risk-audit.py` ranks axioms by the *shape* that made
five SDP uniqueness axioms false.  It is a triage aid and it scores on syntax,
so it is structurally blind to the opposite failure: an axiom that is not false
but **vacuously true** -- one Lean would discharge outright if anyone asked it.

Two such were found by hand on 2026-09-06 and neither scored above threshold:

  * `chart_glue_from_spectrum : ∃ κ : R, κ = ↑bed.lam_sym⁻¹`
        -- an existential whose witness is named in its own body; `⟨_, rfl⟩`.
        Its docstring called it "the wall -- the categorical model of
        `O_q(P¹)` is not in Mathlib".
  * `su2_emergence : ∃ sd : SpinDecomposition …, sd.fundamentalObj = …`
        -- `SpinDecomposition` has three free fields and two equations
        satisfiable by a constant `simpleObj`; the whole thing closes by `rfl`.

A false axiom announces itself the moment somebody looks for a counterexample.
A vacuous one can stand indefinitely, cited as Tannaka-Krein reconstruction,
asserting only that a record with free fields can be filled in.  Nothing
unsound follows from it -- which is exactly why nothing surfaces it.

Method
------
For each axiom: copy its file, rewrite that one declaration from `axiom` to
`theorem … := by <tactics>`, and compile.  Exit 0 means Lean proved it and the
axiom should be a theorem.  One axiom per run, so a hit is attributable.

This is a **sound** detector in the direction that matters: a PASS is a proof,
not a heuristic.  A FAIL is not evidence of anything -- the tactic list is
short by design (a long one would spend hours proving real theorems, which is
not the question being asked).

Self-test
---------
`--selftest` reconstructs the two axioms above from git and requires both to
be provable.  Aborts if either stops being found, so a future narrowing of the
tactic list cannot silently report a clean tree.
"""
from __future__ import annotations
import argparse, os, pathlib, re, shutil, subprocess, sys, tempfile

sys.path.insert(0, str(pathlib.Path(__file__).parent))
_risk = __import__("lean-axiom-degenerate-risk-audit".replace("-", "_")) if False else None

AXIOM_RE = re.compile(r"^axiom\s+([A-Za-z_][A-Za-z0-9_.'!?]*)")
DECL_START = re.compile(
    r"^(axiom|theorem|lemma|def|abbrev|instance|structure|class|example|opaque|"
    r"noncomputable|@\[|/--|/-!|namespace|end|section|variable|open|import|"
    r"universe|set_option)\b")

# Deliberately short.  The question is "is this axiom free?", not "can this be
# proved with effort" -- a long list turns the probe into a proof search whose
# failures say nothing and whose runtime is unbounded.
TACTICS = [
    "rfl",
    "trivial",
    "exact ⟨_, rfl⟩",
    "exact ⟨_, rfl, rfl⟩",
    "simp",
    "decide",
    "constructor <;> rfl",
    "exact ⟨_, by rfl⟩",
]
TACTIC_BLOCK = " := by\n  first\n" + "\n".join(f"  | {t}" for t in TACTICS) + "\n"


def strip_block_comments(text: str) -> str:
    out, i, depth = [], 0, 0
    for line in text.split("\n"):
        keep, j, buf = True, 0, []
        while j < len(line):
            if depth == 0 and line.startswith("/-", j):
                depth += 1; j += 2; continue
            if depth > 0 and line.startswith("-/", j):
                depth -= 1; j += 2; continue
            if depth == 0:
                buf.append(line[j])
            j += 1
        out.append("".join(buf) if depth == 0 or buf else "")
    return "\n".join(out)


def axioms_in(text: str):
    lines_raw = text.split("\n")
    lines = strip_block_comments(text).split("\n")
    out, i = [], 0
    while i < len(lines):
        m = AXIOM_RE.match(lines[i])
        if not m:
            i += 1
            continue
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            if nxt.strip() == "":
                k = j
                while k < len(lines) and lines[k].strip() == "":
                    k += 1
                if k < len(lines) and lines[k].startswith((" ", "\t")) \
                        and not DECL_START.match(lines[k].lstrip()):
                    j = k + 1; continue
                break
            if not nxt.startswith((" ", "\t")):
                break
            j += 1
        out.append((m.group(1), i, j))   # [i, j) in ORIGINAL line coordinates
        i = j
    return out


def rewrite(lines, start, end):
    """Turn the axiom occupying [start, end) into a theorem with a tactic block."""
    body = lines[start:end]
    body[0] = re.sub(r"^axiom\b", "theorem", body[0])
    # Trailing `:` continuation lines are fine; append the tactic block at the end.
    return lines[:start] + body + [TACTIC_BLOCK] + lines[end:]


def probe(path: pathlib.Path, name: str, start: int, end: int,
          lean: str, lean_path: str, timeout: int) -> tuple[bool, str]:
    lines = path.read_text().split("\n")
    new = rewrite(lines, start, end)
    with tempfile.NamedTemporaryFile("w", suffix=".lean", delete=False,
                                     dir=path.parent) as fh:
        fh.write("\n".join(new))
        tmp = pathlib.Path(fh.name)
    try:
        env = dict(os.environ, LEAN_PATH=lean_path)
        r = subprocess.run([lean, "-DautoImplicit=false", "-s", "65536", str(tmp)],
                           capture_output=True, text=True, timeout=timeout, env=env)
        return r.returncode == 0, (r.stdout + r.stderr)[:400]
    except subprocess.TimeoutExpired:
        return False, "TIMEOUT"
    finally:
        tmp.unlink(missing_ok=True)


# Both were converted to theorems on 2026-09-06, so they are read from the
# commit before that.  They are listed SEPARATELY because the probe catches one
# and not the other, and that asymmetry is the point.
# Each row pins an IMMUTABLE COMMIT SHA, never a moving ref.
#
# The first version of this self-test read its fixtures from
# `--selftest-rev`, defaulting to whatever the caller passed -- and that is
# exactly the defect this branch had already fixed, hours earlier, in
# `lean-axiom-degenerate-risk-audit.py`, whose self-test read the five
# known-false SDP axioms from `origin/main` and went red the moment the merge
# deleting them landed.  The same mistake was rebuilt here and surfaced the
# same way (`SELFTEST FAIL: ... not parsed at <rev>`) as soon as the fixtures'
# own axioms were converted.
#
# A pinned sha cannot rot: the axiom is in that commit forever.  The residual
# risk is a shallow clone lacking the object, which reports SELFTEST ERROR
# rather than silently passing.
SELFTEST_PROVABLE = [
    ("e6233b20bb~1",
     "content/quantum-observable-universe/quantum-observable-universes/"
     "spectral-chart-correspondence.lean", "chart_glue_from_spectrum"),
]

# ASSERTED BLIND SPOT.  `su2_emergence` is vacuous -- provable by hand in one
# line -- and this probe does NOT find it, because closing it needs a witness
# RECORD built field by field:
#
#     ⟨{ simpleObj := fun _ => data.qou.fundamentalObj
#        fundamentalObj := data.qou.fundamentalObj
#        fundamental_is_half := rfl
#        adjointObj := data.qou.fundamentalObj
#        adjoint_is_one := rfl }, rfl⟩
#
# No generic tactic supplies that: after `⟨?sd, rfl⟩` the metavariable is a
# whole structure and unification cannot invent one.  The honest response is to
# state the miss rather than pad TACTICS until it happens to land -- a tactic
# list tuned to its own fixtures measures itself.
#
# The self-test asserts this one STAYS unprovable.  If a future tactic addition
# catches it, the test fails and tells you to move the row up, so coverage can
# never grow silently.
# ASSERTED BLIND SPOTS, now TWO and of DIFFERENT KINDS.  Both are vacuous --
# provable by hand in one line -- and this probe finds neither.
#
#  * `su2_emergence` needs a witness RECORD built field by field: after
#    `⟨?sd, rfl⟩` the metavariable is a whole structure and unification cannot
#    invent one.  `categorical_jet_prolongation` was later found by hand to be
#    a second instance of that shape, so it recurs.
#
#  * `antipode_anti_hom` needs CASE-SPECIFIC UNFOLDING.  On its file's
#    scalar-coefficient model `antipodeS = id` and `heckeMul` is real
#    multiplication, so the anti-homomorphism identity collapses to
#    `mul_comm` -- but both are plain `def`s with no `@[simp]`, so nothing
#    unfolds them without being told which.  MEASURED on a minimal
#    reproduction: `rfl`, `trivial`, `simp`, `simp_all`, `simp [mul_comm]`,
#    `constructor <;> ring`, `decide` and `aesop` ALL fail, `aesop` reporting
#    "made no progress".  Those tactics were added and then reverted: they
#    cost runtime and caught nothing.  Knowing which definitions to unfold is
#    case-specific, so this class is out of reach of a fixed tactic list
#    rather than one tactic away.
SELFTEST_KNOWN_MISS = [
    ("e6233b20bb~1",
     "content/quantum-observable-universe/quantum-observable-universes/"
     "su2-emergence.lean", "su2_emergence"),
    ("24c6710ad5",
     "content/quantum-observable-universe/braids-and-knots/"
     "frobenius-antipode-lean-stub.lean", "antipode_anti_hom"),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="content")
    ap.add_argument("--timeout", type=int, default=180)
    ap.add_argument("--filter", default="")
    ap.add_argument("--selftest", action="store_true", default=True,
                    help="run the pinned-sha self-test first (default on); "
                         "the probe aborts unless every fixture matches its "
                         "recorded provable / blind-spot verdict")
    args = ap.parse_args()

    lean = shutil.which("lean")
    if not lean:
        print("provability-probe: no `lean` on PATH -- source "
              "scripts/lean-direct-env.sh first", file=sys.stderr)
        return 2
    lean_path = os.environ.get("LEAN_PATH", "")
    if not lean_path:
        print("provability-probe: LEAN_PATH unset -- source "
              "scripts/lean-direct-env.sh first", file=sys.stderr)
        return 2

    if args.selftest:
        ok = True
        for rev, rel, name, want in (
                [(v, r, n, True) for v, r, n in SELFTEST_PROVABLE]
                + [(v, r, n, False) for v, r, n in SELFTEST_KNOWN_MISS]):
            src = subprocess.run(["git", "show", f"{rev}:{rel}"],
                                 capture_output=True, text=True)
            if src.returncode != 0:
                print(f"  SELFTEST ERROR: cannot read {rel}@{rev}",
                      file=sys.stderr); ok = False; continue
            tmpdir = pathlib.Path(rel).parent
            tf = tmpdir / f".selftest-{name}.lean"
            tf.write_text(src.stdout)
            found = [a for a in axioms_in(src.stdout) if a[0] == name]
            if not found:
                print(f"  SELFTEST FAIL: {name} not parsed at {rev}",
                      file=sys.stderr); ok = False; tf.unlink(); continue
            n, s, e = found[0]
            good, _ = probe(tf, n, s, e, lean, lean_path, args.timeout)
            tf.unlink(missing_ok=True)
            match = (good == want)
            label = "provable" if want else "known blind spot (must stay unprovable)"
            print(f"  {'ok  ' if match else 'FAIL'} {name:<32} {label}",
                  file=sys.stderr)
            if not match and not want:
                print(f"       -> it is now PROVABLE. Move it to "
                      f"SELFTEST_PROVABLE and say what closed it.",
                      file=sys.stderr)
            ok = ok and match
        if not ok:
            print("\nSELF-TEST FAILED -- the probe no longer proves axioms it is "
                  "known to prove. Aborting.", file=sys.stderr)
            return 3
        print("self-test passed\n", file=sys.stderr)

    hits, scanned = [], 0
    for path in sorted(pathlib.Path(args.root).rglob("*.lean")):
        if ".lake" in path.parts:
            continue
        try:
            text = path.read_text()
        except UnicodeDecodeError:
            continue
        axs = axioms_in(text)
        for name, s, e in axs:
            if args.filter and args.filter not in name:
                continue
            scanned += 1
            good, out = probe(path, name, s, e, lean, lean_path, args.timeout)
            if good:
                hits.append((name, path, s + 1))
                print(f"PROVABLE  {name}\n          {path}:{s + 1}", flush=True)

    print(f"\naxioms probed : {scanned}")
    print(f"provable      : {len(hits)}")
    if hits:
        print("\nEach of these is an axiom Lean closes on its own. An axiom that\n"
              "asserts what its own statement already gives is not a gap in the\n"
              "formalisation -- it is a claim that no gap was crossed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
