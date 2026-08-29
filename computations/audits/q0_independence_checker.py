#!/usr/bin/env python3
"""Mechanise `q0Anchor: "independent"` — the one anchor label nothing could check.

WHY THIS EXISTS
    `witness.py` defines five `q0Anchor` values. Four are checkable: `muon` and
    `proton` each assert one pin and can be matched against the payload's own
    q₀; `ambiguous` and `comparison` are about a producer spanning layers. The
    fifth, `independent` — "the compute NEVER READS q₀" — is producer-declared
    only. `witness.py` says so in its own header:

        `independent` asserts something about an import cone and can only be
        trusted [...] and has no way to check it without re-deriving the
        import cone.

    This re-derives the import cone. A producer that declares `independent`
    while demonstrably reading q₀ is asserting a layer-independence its code
    does not have, and until now nothing in the repo could tell.

THE ASYMMETRY, WHICH IS THE WHOLE DESIGN
    Static analysis proves a POSITIVE ("this cone reads q₀") far more reliably
    than a NEGATIVE ("this cone does not"). A read is witnessed by a specific
    line in a specific module; an absence is only as good as the analysis's
    reach. So the two directions are NOT symmetric and must not be reported as
    if they were:

      VIOLATION  (blocking)  declared `independent`, and the cone reads q₀.
                             Positive evidence; a named module and line.
      CANDIDATE  (advisory)  no read found anywhere in a FULLY RESOLVED cone.
                             A suggestion for a human/producer to adopt — never
                             auto-applied, because `independent` is a claim
                             about intent as well as about code.
      UNKNOWN    (neither)   the cone contains an escape hatch this cannot
                             follow (`__import__`, `importlib`, `exec`, `eval`,
                             `getattr`-dispatch) or a module that will not
                             parse. Reported separately, never silently folded
                             into CANDIDATE — that fold is how a checker starts
                             lying about its own coverage.

MEASURE CODE, NOT FILE TEXT
    Every module is normalised through `ast.unparse` with docstrings stripped
    before matching. A previous version of this scan matched
    `from q_parameter import Q` inside `_path_bridge`'s USAGE DOCSTRING and
    attributed a q₀ read to 431 producers that have none — inverting the
    majority verdict of the whole population from two lines of prose in one
    helper. Comments and docstrings are not code.

THE CONE IS TRANSITIVE
    One hop is not enough: `A -> B -> q_parameter` reads q₀ just as surely as
    `A -> q_parameter`. This walks to a fixpoint and reports the full chain, so
    a violation names the path, not just the endpoint.

Pure static inspection — `ast`, `json`, `re`. No arithmetic, so the NO-FLOAT64
discipline is satisfied vacuously.

Usage
-----
    python3 computations/audits/q0_independence_checker.py              # summary
    python3 computations/audits/q0_independence_checker.py --verify     # exit 1 on violations
    python3 computations/audits/q0_independence_checker.py --propose    # candidates
"""
from __future__ import annotations

import argparse
import ast
import collections
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _source_normalise import code_only  # noqa: E402  (shared, PR #5818)

# A q₀ read, in CODE. Each alternative is a way the corpus actually reaches q₀.
# A q₀ read, in CODE, after two false-positive classes were measured and closed:
#
#   1. THE DECLARATION'S OWN PROSE. `q0AnchorReason` is where an author explains
#      why a compute is q₀-independent, and that prose naturally says
#      "q-pinning-50-digit" or quotes the pin. `ast.unparse` preserves string
#      constants, so the explanation was being matched as evidence against
#      itself. Measured: 3 of the first 4 violations inspected were nothing but
#      their own reason string. `_blank_declaration_prose` removes it.
#
#   2. `from q_parameter import <non-q₀ symbol>`. That module also exports
#      CODATA ratios; `knot-volumes.py` imports `MASS_RATIO_MU_E` from it and
#      reads no q₀ at all. A bare module-name match cannot tell the two apart,
#      so imports are matched on the SYMBOL, not the module.
Q0_SYMBOLS = (
    "Q", "Q_MP", "Q_MUON", "Q_50_DIGIT_STR", "Q_SYM", "HA_MP",
    "q_at", "q_muon_at", "load_q_50dps", "_q0_value_for_anchor",
)
_SYMS = "|".join(re.escape(s) for s in Q0_SYMBOLS)
READ = re.compile(rf"""(
      from\s+q_parameter\s+import\s+[^\n]*\b({_SYMS})\b
    | from\s+qou_substrate\.constants\s+import\s+[^\n]*\b({_SYMS})\b
    | \bq_at\s*\(  | \bq_muon_at\s*\(  | \bload_q_50dps\s*\(
    | \b(Q_50_DIGIT_STR|Q_MUON|Q_MP|HA_MP)\b
    | _q0_value_for_anchor
    | q-pinning-50-digit
    | 1\.109978595
)""", re.X)


def _blank_declaration_prose(tree: ast.AST) -> None:
    """Empty the q₀-declaration strings so a reason cannot indict its own claim."""
    # NOT Q0_ROLE: the auditor marker is read back out of this same normalised
    # source, so blanking it silently disables the carve-out (measured: exempt
    # 3 -> 0 the moment it was included here).
    DECL = {"q0Anchor", "q0AnchorReason", "q0Values"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            for k, v in zip(node.keys, node.values):
                if (isinstance(k, ast.Constant) and k.value in DECL
                        and isinstance(v, ast.Constant)
                        and isinstance(v.value, str)):
                    v.value = ""


# Dynamism this cannot follow. Presence anywhere in a cone => UNKNOWN, not clean.
OPAQUE = re.compile(r"(\b__import__\s*\(|\bimportlib\b|\bexec\s*\(|\beval\s*\()")

# An AUDITOR touches q₀ to REASON ABOUT it, not to compute at it. The two are
# statically indistinguishable and this was measured, not assumed:
# `hardcoded_q0_literal_families_audit.py` imports `_q0_value_for_anchor` — a
# signal as "strong" as any — purely to compare literals it is auditing. No
# pattern over imports or literals separates the two, because the auditor uses
# the same API for the opposite purpose.
#
# So the distinction is DECLARED, not inferred. A producer whose q₀ contact is
# audit tooling says so with a module-level marker:
#
#     Q0_ROLE = "auditor"   # reasons about q0; does not compute at it
#
# Absent the marker a q₀-reading cone is treated as computing at q₀ — the
# safe default, since a missing marker yields a reviewable flag while a
# guessed carve-out yields a silent exemption.
AUDITOR_MARKER = re.compile(r"""Q0_ROLE\s*=\s*['"]auditor['"]""")

IMPORT = re.compile(
    r"^\s*(?:from\s+([A-Za-z_][\w.]*)\s+import|import\s+([A-Za-z_][\w.]*))", re.M)

# Modules whose PURPOSE is to serve q₀. Their own source obviously reads q₀, so
# traversing into them makes every importer look like a q₀ consumer — including
# one that imports something else entirely. Measured: `knot-volumes.py` imports
# only `MASS_RATIO_MU_E` (a CODATA ratio) from `q_parameter` and reads no q₀,
# but the walk followed the import and indicted it on q_parameter's own code.
#
# So these are TERMINAL: whether an importer reads q₀ is decided at the import
# site by WHICH SYMBOL it binds (see Q0_SYMBOLS in READ), never by recursing.
Q0_PROVIDER_MODULES = {"q_parameter", "constants"}

STDLIB = {
    "os", "sys", "json", "re", "math", "pathlib", "typing", "collections",
    "itertools", "functools", "argparse", "subprocess", "dataclasses",
    "decimal", "fractions", "numpy", "scipy", "sympy", "mpmath", "time",
    "datetime", "textwrap", "warnings", "hashlib", "random", "copy", "csv",
    "traceback", "shutil", "tempfile", "glob", "pprint", "statistics",
}


def _tracked() -> list[str]:
    return subprocess.run(
        ["git", "ls-files", "computations", "tools"],
        cwd=ROOT, capture_output=True, text=True,
    ).stdout.split()


class Cone:
    """Transitive q₀-read analysis over locally-resolvable imports."""

    def __init__(self, py_files: list[str]) -> None:
        self.by_stem: dict[str, list[str]] = collections.defaultdict(list)
        for f in py_files:
            self.by_stem[pathlib.Path(f).stem].append(f)
        # prefer a live module over a _deprecated twin sharing its stem
        for k in self.by_stem:
            self.by_stem[k].sort(key=lambda p: ("_deprecated" in p, len(p)))
        self._code: dict[str, str | None] = {}

    def code(self, rel: str) -> str | None:
        """Docstring-stripped source, or None if it will not parse."""
        if rel not in self._code:
            try:
                tree = ast.parse((ROOT / rel).read_text(encoding="utf-8",
                                                        errors="replace"))
                for node in ast.walk(tree):
                    if isinstance(node, (ast.Module, ast.FunctionDef,
                                         ast.AsyncFunctionDef, ast.ClassDef)):
                        body = getattr(node, "body", None)
                        if (body and isinstance(body[0], ast.Expr)
                                and isinstance(body[0].value, ast.Constant)
                                and isinstance(body[0].value.value, str)):
                            body.pop(0)
                _blank_declaration_prose(tree)
                self._code[rel] = ast.unparse(tree)
            except Exception:            # noqa: BLE001 - unparseable => no claim
                self._code[rel] = None
        return self._code[rel]

    def analyse(self, entry: str) -> tuple[str, list[str]]:
        """('reads'|'clean'|'unknown', evidence chain)."""
        seen: set[str] = set()
        queue = [(entry, [entry])]
        opaque_at: list[str] | None = None
        while queue:
            mod, chain = queue.pop()
            if mod in seen:
                continue
            seen.add(mod)
            src = self.code(mod)
            if src is None:
                opaque_at = opaque_at or chain + ["<unparseable>"]
                continue
            if READ.search(src):
                return "reads", chain
            if OPAQUE.search(src):
                opaque_at = opaque_at or chain + ["<dynamic import/exec>"]
            for m in IMPORT.finditer(src):
                name = (m.group(1) or m.group(2) or "").split(".")[0]
                if not name or name in STDLIB or name in Q0_PROVIDER_MODULES:
                    continue
                for cand in self.by_stem.get(name, []):
                    if cand not in seen:
                        queue.append((cand, chain + [cand]))
        if opaque_at:
            return "unknown", opaque_at
        return "clean", [entry]


# ---------------------------------------------------------------------------
# IS THE ENV-FLIP EXPERIMENT EVEN VALID HERE?  (bean `qou-324i`)
#
# Most `independent` dispositions in this corpus are justified by one sentence,
# copy-pasted across five witnesses verbatim:
#
#     "PROVED by running this producer under QOU_Q0_ANCHOR=muon and =proton and
#      diffing the emitted witness: ... every substantive field is byte-identical"
#
# `QOU_Q0_ANCHOR` is read by `q_parameter` at import. It therefore reaches a q0
# ONLY when the q0 arrives through `q_parameter` / `qou_substrate.constants`.
# When it does not, byte-identity under the flip is guaranteed a priori and the
# experiment measures OVERRIDE-SENSITIVITY, not q0-independence -- so a producer
# can be hard-pinned to the muon layer and still "pass".
#
# Measured on this tree (2026-08-28): `probes/lambda_scale_substrate_probe.py`
# reads `q-pinning-50-digit.witness.json` directly -- the muon anchor-defining
# witness -- and the flip reports `clean`. That is the false negative, live.
#
# Three ways the override is defeated. Each is reported by NAME, because the
# correct repair differs: a literal is edited, a pin-witness read is rerouted
# through `q_parameter`, a peer import is chased to its provider.
FLIP_BLIND_LITERAL = "literal"
FLIP_BLIND_PIN_WITNESS = "pin-witness"
FLIP_BLIND_PEER_IMPORT = "peer-import"

# A q0-shaped decimal. Both basins: an `independent` claim is defeated by a
# hardcoded PROTON pin exactly as much as by a muon one -- the label says the
# producer reads no substrate value, and a literal is one.
_Q0_SHAPED = re.compile(r"\b1\.1099785\d{3,}")
_PIN_WITNESS = re.compile(r"q-pinning-50-digit")

# `sp.symbols('q')` is NOT a q0. This guard is not decoration: without it the
# peer-import scan indicts `probes/chi_content_eigenbasis_probe.py` and
# `probes/eigenbasis_structural_lemmas_probe.py`, which import `Q` from
# `hoefsmit_symbolic` -- where line 57 reads `Q = sp.symbols('q', positive=True)`.
# Both are correctly `independent`; a name-shaped detector calls them defects.
# The known TRUE positive is `chirality_topology_binding_probe`'s
# `from hecke_channel_binding_probe import Q0`, where `Q0 = Q_MP` is numeric
# (fixed on main in 0c772454cf); `--selftest` pins both directions.
_SYMBOLIC_RHS = re.compile(r"\b(symbols|Symbol|Dummy|Wild)\s*\(")

_PEER_Q0_NAMES = set(Q0_SYMBOLS) | {"Q0", "q0", "Q0_MP", "Q0_PROTON", "Q0_MUON",
                                    "q0_mp", "Q_PIN", "Q0_PIN"}


def _module_level_binding(cone: "Cone", stem: str, name: str) -> str | None:
    """The unparsed RHS of a module-level `name = ...` in module `stem`."""
    for rel in cone.by_stem.get(stem, []):
        try:
            tree = ast.parse((ROOT / rel).read_text(encoding="utf-8",
                                                    errors="replace"))
        except Exception:                # noqa: BLE001
            continue
        for node in tree.body:           # module level only, deliberately
            if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                    and isinstance(node.targets[0], ast.Name) \
                    and node.targets[0].id == name:
                return ast.unparse(node.value)
    return None


def flip_validity(producer: str, cone: "Cone") -> tuple[bool, list[str]]:
    """(the flip can see this producer's q0, reasons it cannot).

    A TRUE means only that the override reaches SOME q0 path here -- it is not
    a verdict that the producer is q0-dependent. A FALSE is the load-bearing
    direction: it says a byte-identical flip result is not evidence of anything.
    """
    try:
        raw = (ROOT / producer).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return True, []
    try:
        code = code_only(raw)            # comments + docstrings blanked IN PLACE
    except Exception:                    # noqa: BLE001 - unparseable: no claim
        code = raw

    blind: list[str] = []
    lits = sorted(set(_Q0_SHAPED.findall(code)))
    if lits:
        blind.append(f"{FLIP_BLIND_LITERAL}: {', '.join(lits[:3])}")
    if _PIN_WITNESS.search(code):
        blind.append(f"{FLIP_BLIND_PIN_WITNESS}: reads q-pinning-50-digit.witness.json")

    # Peer import: a q0-bearing name bound from another PRODUCER module. This is
    # the inheritance path `qou-1c4y` records as unaudited -- `inherited_q0_pin_
    # audit` follows witness FILES, not python imports, and the pin classifier
    # stops at a provider-terminal rule before it reaches the real source.
    try:
        tree = ast.parse(raw)
    except SyntaxError:
        return (not blind), blind
    for node in ast.walk(tree):
        if not isinstance(node, ast.ImportFrom) or not node.module:
            continue
        stem = node.module.split(".")[-1]
        if stem in Q0_PROVIDER_MODULES or stem not in cone.by_stem:
            continue
        for alias in node.names:
            if alias.name not in _PEER_Q0_NAMES:
                continue
            rhs = _module_level_binding(cone, stem, alias.name)
            if rhs is not None and _SYMBOLIC_RHS.search(rhs):
                continue                 # a sympy symbol is not a q0
            blind.append(
                f"{FLIP_BLIND_PEER_IMPORT}: {alias.name} from {node.module}"
                + (f" (= {rhs})" if rhs else ""))
    return (not blind), blind


CITES_FLIP = re.compile(
    r"QOU_Q0_ANCHOR\s*=\s*(muon|proton|ideal|physical)", re.I)


def _selftest_flip_validity(cone: "Cone") -> int:
    """Both directions of the sympy guard, pinned against real files.

    A narrowing that loses either one is the failure this file exists to make
    loud: over-reporting turns two correct dispositions into fake defects,
    under-reporting hands a hard muon pin a clean bill.
    """
    rc = 0
    ok, why = flip_validity("computations/probes/chi_content_eigenbasis_probe.py", cone)
    print(f"  chi_content_eigenbasis_probe  flip_visible={ok} blind={why}")
    if not ok:
        print("  SELFTEST FAILED - a sympy `Q` was read as a q0 (false positive).")
        rc = 1
    ok, why = flip_validity("computations/probes/lambda_scale_substrate_probe.py", cone)
    print(f"  lambda_scale_substrate_probe  flip_visible={ok} blind={why}")
    if ok or not any(FLIP_BLIND_PIN_WITNESS in w for w in why):
        print("  SELFTEST FAILED - the direct pin-witness read was not detected.")
        rc = 1
    ok, why = flip_validity(
        "computations/probes/chirality_topology_binding_probe.py", cone)
    print(f"  chirality_topology_binding_probe  flip_visible={ok} blind={why}")
    if ok or not any(FLIP_BLIND_PEER_IMPORT in w for w in why):
        print("  SELFTEST FAILED - the known peer-import positive "
              "(`Q0 = Q_MP` via hecke_channel_binding_probe) was not detected.")
        rc = 1
    if rc == 0:
        print("  selftest OK")
    return rc


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--verify", action="store_true",
                    help="exit 1 if any witness declares independent while its "
                         "cone reads q0")
    ap.add_argument("--propose", action="store_true",
                    help="list producers whose fully-resolved cone reads no q0")
    ap.add_argument("--flip-validity", action="store_true",
                    help="for every `independent` witness, report whether the "
                         "QOU_Q0_ANCHOR flip experiment can see its q0 at all "
                         "(bean qou-324i)")
    ap.add_argument("--selftest", action="store_true",
                    help="pin both directions of the peer-import sympy guard")
    args = ap.parse_args()

    tracked = _tracked()
    wits = [f for f in tracked
            if f.endswith(".witness.json") and "_deprecated" not in f]
    pys = [f for f in tracked if f.endswith(".py")]
    cone = Cone(pys)

    if args.selftest:
        return _selftest_flip_validity(cone)

    violations: list[tuple[str, str, list[str]]] = []
    declared_ok = 0
    auditor_exempt = 0
    verdicts: collections.Counter = collections.Counter()
    candidates: list[str] = []
    unknowns: list[tuple[str, list[str]]] = []
    flip_blind: list[tuple[str, str, list[str], bool]] = []

    for w in wits:
        try:
            d = json.loads((ROOT / w).read_text(encoding="utf-8"))
        except Exception:                # noqa: BLE001
            continue
        script = d.get("scriptFile") or ""
        stem = (pathlib.Path(script).stem if script
                else pathlib.Path(w).name[: -len(".witness.json")].replace("-", "_"))
        paths = cone.by_stem.get(stem)
        if not paths:
            verdicts["producer unresolved"] += 1
            continue
        producer = paths[0]
        state, chain = cone.analyse(producer)
        verdicts[state] += 1

        if d.get("q0Anchor") == "independent":
            reason = d.get("q0AnchorReason") or ""
            visible, blind = flip_validity(producer, cone)
            # An AUDITOR holds q0 literals as the DATA IT AUDITS, so the
            # override not reaching them is correct rather than a blind spot.
            # Same declared carve-out the VIOLATION path uses; measured cost of
            # omitting it here was 2 of 4 rows being audit tools.
            if not visible and not AUDITOR_MARKER.search(cone.code(producer) or ""):
                flip_blind.append((w, producer, blind,
                                   bool(CITES_FLIP.search(reason))))
            if state == "reads":
                src = cone.code(producer) or ""
                if AUDITOR_MARKER.search(src):
                    auditor_exempt += 1
                else:
                    violations.append((w, producer, chain))
            else:
                declared_ok += 1
        elif "q0Anchor" not in d and state == "clean":
            candidates.append(producer)
        if state == "unknown":
            unknowns.append((producer, chain))

    print("q0Anchor: \"independent\" — mechanised check")
    print("=" * 66)
    print(f"  witnesses examined            : {sum(verdicts.values())}")
    for k, v in sorted(verdicts.items()):
        print(f"    cone {k:22s}: {v}")
    print()
    print(f"  declared independent, upheld  : {declared_ok}")
    print(f"  auditor-marked, exempt        : {auditor_exempt}")
    print(f"  declared independent, VIOLATED: {len(violations)}")
    print(f"  candidates (clean, undeclared): {len(sorted(set(candidates)))} producers")
    print(f"  UNKNOWN cones (not candidates): {len(set(p for p, _ in unknowns))} producers")

    cited = [r for r in flip_blind if r[3]]
    print(f"  flip experiment CANNOT see q0 : {len(flip_blind)}"
          f"  (of which {len(cited)} cite that experiment as their proof)")

    if args.flip_validity:
        print("\nFLIP-BLIND — `independent` producers the QOU_Q0_ANCHOR override")
        print("  does not reach. A byte-identical flip here is guaranteed a")
        print("  priori and is NOT evidence of q0-independence (bean qou-324i).")
        for w, prod, blind, does_cite in flip_blind:
            print(f"  {w}")
            print(f"      producer {prod}")
            for b in blind:
                print(f"      blind    {b}")
            if does_cite:
                print("      🛑 its own q0AnchorReason cites the flip experiment "
                      "as proof — the proof does not apply")
        if not flip_blind:
            print("  (none)")

    if violations:
        print("\nVIOLATIONS — declares q0-independence, but the cone reads q0:")
        print("  (a producer whose q0 contact is audit tooling declares")
        print("   `Q0_ROLE = \"auditor\"` at module level rather than being")
        print("   carved out by a pattern here — see the AUDITOR_MARKER note.)")
        for w, prod, chain in violations:
            print(f"  {w}")
            print(f"      producer {prod}")
            print(f"      via      {' -> '.join(chain)}")

    if args.propose:
        print("\nCANDIDATES for q0Anchor: \"independent\" (ADVISORY — a claim about")
        print("intent as well as code; the producer must opt in, never a sweep):")
        for p in sorted(set(candidates))[:60]:
            print(f"   {p}")
        extra = len(set(candidates)) - 60
        if extra > 0:
            print(f"   ... and {extra} more (not truncated silently: this is the count)")

    if args.verify and violations:
        print(f"\nFAIL: {len(violations)} witness(es) assert q0-independence "
              f"their code does not have.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
