#!/usr/bin/env python3
"""Probe whether a Lean context class can be inhabited with NO hypotheses.

WHY THIS EXISTS
---------------
`proof-no-self-assuming-projection` is a *syntactic* criterion: it flags a
theorem whose conclusion is character-identical to a class field it projects.
The ledger's recorded disposition for such a finding is *"construct a witness
instance and prove the property there"*.

That disposition is right only when a witness is hard to come by.  When the
context class can be inhabited by `Unit` and zero, constructing a witness is
not progress — it is the defect, and it is the same one the q-NS carriers in
`QOU/AlgebraicSubstrate/ConditionalClasses.lean` had before 2026-08-30: every
field was a statement about data the instance itself got to choose, so a `[C]`
hypothesis assumed nothing.  See
`docs/audits/2026-08-30-qns-carriers-are-refutable.lean` for that gate.

This script turns the syntactic criterion into a semantic one.  For each class
it generates the most trivial model it can — `Unit` for every `Type` field, `0`
(and, on a second pass, `1`) for every scalar, `fun _ => <default>` for every
function — and asks `lean` whether that model type-checks.

THE ASYMMETRY IS THE POINT, AND IT IS DELIBERATE
------------------------------------------------
- A **pass is decisive**: the class is inhabited with no hypotheses, so it
  constrains nothing and no downstream `[C]`-conditional result is conditional
  on anything.
- A **failure is inconclusive** and must never be reported as "has content".
  It means only that *this generator's* defaults did not satisfy the fields.
  A class whose claim is `weights_sum = 1` rejects the all-zero model and is
  still inhabited by the all-one model one line later; a class needing a
  bespoke structure value is skipped before it is ever compiled.

So the output is a LOWER BOUND on how many of these classes are vacuous.  Do
not quote the complement as a count of contentful ones.

USAGE
    python3 scripts/lean-context-class-inhabitation-probe.py            # all
    python3 scripts/lean-context-class-inhabitation-probe.py --only Foo,Bar
    python3 scripts/lean-context-class-inhabitation-probe.py --json out.json

Requires the olean cache to be restored (see AGENTS.md §"RESTORE -> build ->
SEED").  It runs `lean` directly and never `lake build`, which would evict a
restored cache.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEAN_LIB = ROOT / "folio/quantum-observable-universe/lean/.lake/build/lib/lean"
PKG_LIBS = sorted((ROOT / ".lake/packages").glob("*/.lake/build/lib/lean"))

# Unicode-aware: `Δ_K`, `μ`, `β`, `χ_λ` are field names in this corpus, and an
# ASCII-only pattern silently drops them -- which shows up as `Fields missing`
# from `lean`, i.e. as an inconclusive result rather than as a parser error.
IDENT = r"[^\W\d][\w'₀-₉]*"

# Types we know how to inhabit.  Anything else makes the class SKIPPED rather
# than FAILED -- the distinction matters, see the module docstring.
SCALARS = {"ℝ", "ℕ", "ℤ", "ℚ", "ℂ", "Real", "Nat", "Int", "Rat", "Complex"}

DISCHARGE = (
    "by first"
    " | rfl"
    " | trivial"
    " | norm_num"
    " | simp"
    " | (intro _; norm_num)"
    " | (intro _; simp)"
    " | (intro _ _; norm_num)"
    " | (intro _ _; simp)"
    " | (intro _ _ _; simp)"
    " | exact ⟨rfl, rfl, rfl⟩"
    " | exact ⟨rfl, rfl⟩"
    " | (refine ⟨?_, ?_⟩ <;> simp)"
    " | (refine ⟨?_, ?_, ?_⟩ <;> simp)"
    " | (constructor <;> norm_num)"
    " | (constructor <;> simp)"
    " | (intro _; exact ⟨rfl, rfl, rfl⟩)"
    " | (intro _; exact ⟨rfl, rfl⟩)"
    " | simp_all"
)


def lean_env() -> dict:
    env = dict(os.environ)
    env["LEAN_PATH"] = os.pathsep.join(
        [str(LEAN_LIB)] + [str(p) for p in PKG_LIBS]
    )
    env["PATH"] = f"{Path.home()}/.elan/bin:{env.get('PATH', '')}"
    return env


def module_of(path: Path) -> str | None:
    """Module name for a library file, or None for a content-block sibling."""
    s = str(path)
    marker = "/lean/QOU/"
    if marker not in s:
        return None
    return "QOU." + s.split(marker, 1)[1][:-5].replace("/", ".")


def namespace_at(text: str, offset: int) -> str:
    """Innermost `namespace` chain open at `offset`."""
    stack: list[str] = []
    for m in re.finditer(r"^(namespace\s+([\w.]+)|end\s+([\w.]+))", text[:offset], re.M):
        if m.group(2):
            stack.append(m.group(2))
        elif stack and stack[-1] == m.group(3):
            stack.pop()
    return ".".join(stack)


class Unsupported(Exception):
    pass


def default_for(ty: str, ring: str | None, zero: str,
                local_types: frozenset[str] = frozenset()) -> str:
    """A term of type `ty`, or raise Unsupported.

    `local_types` names this class's own `Type`-valued fields.  They matter
    more than they look: a class routinely declares `CategoricalObj : Type`
    and then types later fields by it (`mass : CategoricalObj → ℝ`), and
    `Finset Partition` is `Finset Unit` once `Partition` is instantiated.
    Without this the generator skips exactly the shape this corpus uses most,
    and -- worse -- reads `Finset Partition` as `∅`, turning a satisfiable
    `weights_sum = 1` into `0 = 1` and reporting a false `unproven`.
    """
    ty = ty.strip()
    if ty in local_types:
        return "()"
    while ty.startswith("(") and ty.endswith(")"):
        inner = ty[1:-1]
        if inner.count("(") == inner.count(")"):
            ty = inner.strip()
        else:
            break
    if ty in ("Type", "Type*", "Type _") or re.fullmatch(r"Type\s*[\w.*]*", ty):
        return "Unit"
    if ty == "Prop":
        return "True"
    if ty in SCALARS or (ring and ty == ring):
        return zero
    if ring and ty == f"{ring}ˣ":
        return "1"
    if ty.startswith("Option "):
        return "none"
    if ty.startswith("Finset "):
        arg = ty[len("Finset "):].strip()
        return "Finset.univ" if (arg == "Unit" or arg in local_types) else "∅"
    # top-level arrow?
    depth = 0
    for i in range(len(ty) - 1):
        c = ty[i]
        if c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        elif depth == 0 and ty[i] == "→":
            return f"fun _ => {default_for(ty[i + 1:], ring, zero, local_types)}"
    if "×" in ty and ty.count("×") == 1:
        a, b = ty.split("×")
        return f"({default_for(a, ring, zero, local_types)}, {default_for(b, ring, zero, local_types)})"
    raise Unsupported(ty)


def is_claim(ty: str) -> bool:
    return any(
        s in ty
        for s in ("=", "≤", "<", ">", "∀", "∃", "↔", "≠", "∈", "Nonempty",
                  "Tendsto", "IsOpen", "Subsingleton", "IsUnit")
    )


def parse_class(text: str, off: int):
    """Return (name, signature, [(field, type)]) for the class at `off`."""
    rest = text[off:]
    stop = re.search(
        r"\n(?=(?:/-!|/--|@\[|class |structure |theorem |lemma |def |abbrev "
        r"|instance |noncomputable |namespace |end |example ))",
        rest[1:],
    )
    blk = rest[: (stop.start() + 1 if stop else 4000)]
    wi = blk.find(" where")
    if wi == -1:
        raise Unsupported("no `where`")
    sig, body = blk[:wi], blk[wi + len(" where"):]
    nm = re.match(rf"\s*class\s+({IDENT})", sig)
    if nm is None:
        # The first ` where` in the block did not belong to this class header
        # (e.g. it sits inside a field type, or the declaration is not a plain
        # `class <ident>`). Skip rather than crash: an unparsed signature used
        # to raise AttributeError out of the worker thread and ABORT THE WHOLE
        # SWEEP, so a full-tree run stopped partway and the operator learned
        # about it only from a traceback in the log. Measured 2026-08-31: the
        # run died after 76 INHABITED verdicts with no summary.
        raise Unsupported(f"unparsed class signature: {sig.strip()[:80]!r}")
    name = nm.group(1)
    body = re.sub(r"/--.*?-/", "", body, flags=re.S)
    body = re.sub(r"--[^\n]*", "", body)
    fields = []
    for fm in re.finditer(
        rf"^  ({IDENT})\s*(\([^)]*\))?\s*:(.*?)(?=\n  {IDENT}|\Z)", body, re.S | re.M
    ):
        if fm.group(2):  # a field with its own binders; out of scope
            raise Unsupported(f"parameterised field {fm.group(1)}")
        fields.append((fm.group(1), " ".join(fm.group(3).split())))
    if not fields:
        raise Unsupported("no fields parsed")
    return name, sig, fields


def build_instance(name, sig, fields, ns, zero) -> str:
    if "extends" in sig:
        raise Unsupported("extends a parent class")
    ring = None
    args = []
    for bm in re.finditer(r"\(([^():]+):([^()]*)\)", sig[sig.index(name) + len(name):]):
        names, ty = bm.group(1).split(), bm.group(2).strip()
        if "Type" in ty or "Sort" in ty:
            ring = ring or names[0]
            args += ["ℚ"] * len(names)  # ℕ is neither a Field nor an AddCommGroup
        else:
            args += [default_for(ty, ring, zero, frozenset()) for _ in names]
    # Fields declared `: Type` are instantiated as `Unit`, so any later field
    # typed by one of them resolves too.
    local_types = frozenset(
        n for n, ty in fields if re.fullmatch(r"Type\s*[\w.*]*", ty.strip())
    )
    # `Prop`-valued data fields pair with a `_holds` witness; `True`/`trivial`.
    prop_fields = {n for n, ty in fields if ty.strip() == "Prop"}
    lines = []
    for n, ty in fields:
        if ty.strip() == "Prop":
            lines.append(f"  {n} := True")
        elif ty.strip() in prop_fields:
            lines.append(f"  {n} := trivial")
        elif is_claim(ty):
            base = re.sub(r"_holds$", "", n)
            lines.append(f"  {n} := {'trivial' if base in prop_fields else DISCHARGE}")
        else:
            lines.append(f"  {n} := {default_for(ty, ring, zero, local_types)}")
    head = f"{ns + '.' if ns else ''}{name}" + ("".join(f" ({a})" for a in args))
    return f"example : {head} where\n" + "\n".join(lines) + "\n"


def probe(name: str, path: Path, off: int) -> dict:
    text = path.read_text(errors="replace")
    ns = namespace_at(text, off)
    mod = module_of(path)
    try:
        cname, sig, fields = parse_class(text, off)
    except Unsupported as e:
        return {"class": name, "status": "skipped", "reason": str(e)}
    except Exception as e:  # noqa: BLE001 - one bad class must not kill the sweep
        # Belt and braces for the same failure mode as the `nm is None` guard
        # in `parse_class`: any unanticipated parser error is reported as a
        # skip for THIS class, never as an abort of the run. A partial sweep
        # that looks complete is worse than a sweep that names what it missed.
        return {"class": name, "status": "skipped",
                "reason": f"parser error: {type(e).__name__}: {e}"[:200]}
    last = None
    for zero in ("0", "1"):
        try:
            inst = build_instance(cname, sig, fields, ns, zero)
        except Unsupported as e:
            return {"class": name, "status": "skipped", "reason": f"type: {e}"}
        if mod:
            src = f"import {mod}\n\n{inst}"
        else:
            # Content-block sibling: no module, so probe against a copy of the
            # file.  `import Mathlib.Tactic` is PREPENDED because the copy
            # inherits the sibling's own imports, and most siblings import far
            # less than the tactic block below needs -- `linarith` came back
            # "unknown tactic" and `norm_num` could not close `0.99824 <= 10 *
            # 0.99824`.  Without this every one of the ~21 sibling classes was
            # judged against a crippled tactic set, and its `unproven` verdict
            # was a fact about the harness.  Measured on DirectionSanityGateClass:
            # unproven without the import, INHABITED with it.
            src = f"import Mathlib.Tactic\n{text}\n\n{inst}"
        with tempfile.NamedTemporaryFile("w", suffix=".lean", delete=False) as fh:
            fh.write(src)
            tmp = fh.name
        try:
            r = subprocess.run(
                ["lean", tmp], env=lean_env(), capture_output=True,
                text=True, timeout=300,
            )
        except subprocess.TimeoutExpired:
            return {"class": name, "status": "skipped", "reason": "lean timeout"}
        finally:
            os.unlink(tmp)
        if r.returncode == 0:
            return {"class": name, "status": "INHABITED", "model": zero,
                    "file": str(path.relative_to(ROOT))}
        last = (r.stdout or r.stderr).strip().split("\n")[:3]
    return {"class": name, "status": "unproven", "reason": " / ".join(last or [])[:300],
            "file": str(path.relative_to(ROOT))}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", help="comma-separated class names")
    ap.add_argument("--json", help="write the full result set here")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument(
        "--selftest", action="store_true",
        help="assert the five hand-verified classes still come back INHABITED",
    )
    args = ap.parse_args()

    if not LEAN_LIB.exists():
        print(f"error: no olean build at {LEAN_LIB}", file=sys.stderr)
        print("Restore the cache first (AGENTS.md §RESTORE -> build -> SEED).",
              file=sys.stderr)
        return 2

    # Five classes inhabited by hand on 2026-08-30, before this generator
    # existed (probe kept at docs/audits/).  They are the regression guard: the
    # first version of this script reported only 2 of them, because it could
    # not resolve a field whose TYPE was another field of the same class
    # (`mass : CategoricalObj → ℝ`) and so read `Finset Partition` as `∅`,
    # turning a satisfiable `Σ w = 1` into `0 = 1`.  Both showed up as
    # `unproven`/`skipped` -- i.e. as "no finding" -- which is exactly how a
    # detector reports a clean tree it never actually looked at.
    SELFTEST = [
        "SixTermMassFormulaContext",
        "JetPrefixGbFiltrationContext",
        "ReidemeisterMassInvarianceContext",
        "RMatrixBraidingContext",
        "KnotFactorSpectralContext",
    ]
    if args.selftest:
        args.only = ",".join(SELFTEST)

    wanted = set(args.only.split(",")) if args.only else None
    targets: dict[str, tuple[Path, int]] = {}
    for f in sorted((ROOT / "content").rglob("*.lean")):
        text = f.read_text(errors="replace")
        for m in re.finditer(rf"^\s*class\s+({IDENT})", text, re.M):
            n = m.group(1)
            if wanted and n not in wanted:
                continue
            targets.setdefault(n, (f, m.start()))

    print(f"probing {len(targets)} context classes with {args.jobs} workers\n")
    results = []
    with concurrent.futures.ThreadPoolExecutor(args.jobs) as pool:
        futs = {pool.submit(probe, n, p, o): n for n, (p, o) in targets.items()}
        for fut in concurrent.futures.as_completed(futs):
            res = fut.result()
            results.append(res)
            if res["status"] == "INHABITED":
                print(f"  INHABITED  {res['class']}  (model: all-{res['model']})")

    inh = [r for r in results if r["status"] == "INHABITED"]
    skip = [r for r in results if r["status"] == "skipped"]
    unp = [r for r in results if r["status"] == "unproven"]
    print(f"\n  INHABITED (proved vacuous) : {len(inh)}")
    print(f"  unproven  (INCONCLUSIVE)   : {len(unp)}")
    print(f"  skipped   (generator gap)  : {len(skip)}")
    print(f"  total                      : {len(results)}")
    print("\nA pass proves the class constrains nothing.  A failure proves"
          "\nNOTHING about the class -- only about this generator.  Do not"
          "\nquote `unproven` + `skipped` as a count of contentful classes.")

    if args.selftest:
        missed = sorted(set(SELFTEST) - {r["class"] for r in inh})
        if missed:
            print(f"\nSELFTEST FAILED: no longer detected as inhabited: {missed}")
            return 1
        print(f"\nSELFTEST PASSED: all {len(SELFTEST)} known-vacuous classes detected")
        return 0

    if args.json:
        Path(args.json).write_text(json.dumps(
            {"inhabited": inh, "unproven": unp, "skipped": skip}, indent=1,
            ensure_ascii=False))
        print(f"\nwrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
