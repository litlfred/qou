#!/usr/bin/env python3
"""Triage AME-literal → codata_constants registry routes: SAFE (byte-exact) vs UNSAFE.

Bean fvxq ("route remaining inline mass literals through the codata_constants
registry"). The atomic-mass registry exports landed on main (PR-#539b82f125:
`M_*_ATOMIC_MEV_VALIDATION`, `AME_B_*_MEV_VALIDATION`). The remaining inline-literal
tail is NOT a uniform mechanical sweep: the registry's canonical value strings differ
at the last digit(s) from many corpus literals. Routing a mismatched literal would
SILENTLY CHANGE the value — a value-preservation violation.

  ⚠ THE REGISTRY MOVED AGAIN AFTER THIS SCRIPT WAS WRITTEN. This docstring used to
  cite `AME_B_HE4 = 28.295673` and deuteron `2.224566`. Commit 03c25e8db ("the
  canonical binding reference was hand-typed and 7 of 11 were wrong", owner: "ame
  data is in corpus") switched `_ame_binding_mev` from `binding_energy_total_keV`
  — derived, and computed in float64 by vendor_ame2020.py — to the quoted
  `binding_energy_per_A_keV` column. The canonical values today are
  `AME_B_HE4 = 28.2956624` and deuteron `2.2245662`, so the corpus literals that
  were byte-exact BEFORE that commit are now in the UNSAFE class. The SAFE/UNSAFE
  split below is computed from `dir(codata_constants)` at runtime and is therefore
  always current; only this prose had gone stale.

This script classifies every AME-range decimal literal in `computations/*.py`
(excluding `_deprecated/` and the registry module itself) as:

  • SAFE   — the literal STRING exactly equals a registry value string ⇒ routing is
             value-preserving (`mp.mpf("8.481798")` → `AME_B_TRITIUM_MEV_VALIDATION`).
  • UNSAFE — within ~5e-6 relative of a registry value but NOT byte-exact ⇒ routing
             would change the value; needs a value-reconciliation decision (is the
             registry value canonical, or is the corpus literal? owner/sibling call),
             NOT a mechanical route.

Pure string/value comparison — no compute deps, runs anywhere. This is the routing
roadmap for the fvxq tail; the SAFE list is the value-preserving work, the UNSAFE
list is the decisions that must precede routing.

Output: ame-registry-routing-triage.witness.json
"""
from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "substrate"))
import codata_constants as c  # noqa: E402

# Registry value-string → export-name (atomic masses + AME binding energies).
REG = {}
for nm in dir(c):
    if nm.endswith("_VALIDATION") and ("ATOMIC" in nm or "AME_B" in nm):
        try:
            REG[str(c.__dict__[nm])] = nm
        except Exception:
            pass

# Fraction bounded at 15 digits ON PURPOSE. A hand-typed AME literal is at
# most ~12 significant figures (the widest registry value is
# 938.78307479441, 11 decimals). An unbounded pattern also matched
# witness_float64_padding_audit.py's own self-test fixture --
#   "8.4817962000000015621026250300928950309753417968750000000000"
# -- which is a padded-float64 EXAMPLE, not a literal anyone typed. The
# triage then wrote it into its own witness, where the padding audit
# correctly flagged it: a roadmap reporting the example of a bug as an
# instance of a different bug.
_NUMONLY = re.compile(r'^\d{1,5}\.\d{3,15}$')


def _literals(txt: str):
    """Yield every AME-range literal that is CODE, via tokenize.

    The regex this replaced scanned raw text, so a value written in a comment
    or a docstring counted as a routable site. That inflates both halves of
    the roadmap: prose is not work. tokenize separates them exactly --
      COMMENT           -> skip, always prose
      STRING            -> keep ONLY if the whole string is the number, which
                           is the `mp.mpf("8.4817962")` form; anything else is
                           prose that happens to contain digits
      NUMBER            -> keep, a bare literal
    """
    import io
    import tokenize as _tk
    try:
        toks = list(_tk.generate_tokens(io.StringIO(txt).readline))
    except (_tk.TokenError, IndentationError, SyntaxError):
        return
    for t in toks:
        if t.type == _tk.COMMENT:
            continue
        if t.type == _tk.STRING:
            body = t.string.strip("\"'")
            if _NUMONLY.match(body):
                yield body, t.start[0]
        elif t.type == _tk.NUMBER:
            if _NUMONLY.match(t.string):
                yield t.string, t.start[0]




def _is_rounding(lit: str, reg: str) -> bool:
    """Is `lit` the registry value written to fewer digits, or a DIFFERENT number?

    This is the split that makes the UNSAFE tail workable. Both halves are
    "near a registry value and not byte-exact", but they need opposite handling:

      2.224566   vs 2.2245662     -- the registry value at 6dp. Same number,
                                     written short. Routing is a precision gain.
      8.481821   vs 8.4817962     -- disagrees at the 6th decimal, a digit it
                                     does print. A different measurement, near
                                     certainly an older AME evaluation. Routing
                                     silently updates the data, which is a
                                     provenance decision, not a refactor.

    Rounding the registry value to the literal's own decimal count answers it
    exactly, with no tolerance to tune.
    """
    from decimal import Decimal, InvalidOperation
    try:
        d_lit, d_reg = Decimal(lit), Decimal(reg)
    except InvalidOperation:
        return False
    nd = -d_lit.as_tuple().exponent
    if nd < 0:
        return False
    return d_reg.quantize(Decimal(1).scaleb(-nd)) == d_lit

def _fixture_lines(txt: str) -> set[int]:
    """Line numbers inside a self-test, where routing needs its own ruling.

    A byte-exact string match says routing preserves the VALUE. It does not say
    routing is CORRECT, and inside a test the answer splits two ways:

      • `registry_witness_pin_validator.self_test()` builds two synthetic mass
        tables -- one healthy, one reproducing the 2026-06-22 incident where
        `rows[2]` silently became 3He. Routing those would make the validator
        check the registry against itself, and would let the incident
        reproduction drift the moment a registry value moved. Never route.
      • `delta_lambda_shape_probe._test_option_e_delta_lambda()` just holds the
        real AME values as comparison targets. Routing is defensible there.

    This function does not try to tell the two apart -- it only stops them being
    counted as ordinary REVIEW work, since both need a ruling a reader must make.
    """
    import ast as _ast
    try:
        tree = _ast.parse(txt)
    except SyntaxError:
        return set()
    out: set[int] = set()
    for n in _ast.walk(tree):
        if isinstance(n, (_ast.FunctionDef, _ast.AsyncFunctionDef)) and (
                n.name == "self_test" or n.name.startswith("test_")
                or n.name.startswith("_test_")):
            lo = n.lineno
            hi = max((getattr(c, "lineno", lo) for c in _ast.walk(n)), default=lo)
            out.update(range(lo, hi + 1))
    return out

# ── Role classification: which UNSAFE sites may be routed AT ALL ────────
#
# SAFE/UNSAFE answers "would routing change the value". It does NOT answer
# the question bean fvxq raises, which gates the whole migration: routing a
# `_VALIDATION` constant into a PREDICTION INPUT violates the 3-cal
# discipline. Those constants are comparison targets; feeding one into the
# quantity being validated is fitting on the answer. So an UNSAFE site is not
# a unit of work until its ROLE is known, and until now nothing measured it.
#
# The discriminator is what the AME-bound name FLOWS INTO:
#
#   TARGET  every assignment it reaches names an error/comparison quantity
#           (err, miss, residual, pct, ratio, deviation, gap, delta_*). The
#           value is only ever compared against, never built from.
#   INPUT   it reaches a scale/calibration name (alpha, scale, calib, norm,
#           E0, coeff) or a predicted quantity (B_pred, M_pred). This is the
#           3-cal shape: derive a scale FROM the measurement, then multiply it
#           back into a prediction of that same measurement.
#   REVIEW  neither, or it escapes into a call whose role we cannot see.
#
# Deliberately conservative: a site is INPUT if ANY use looks like one, and
# REVIEW rather than TARGET when unsure. The failure mode to avoid is calling
# a calibration site routable.
_TARGET_RE = re.compile(r'err|miss|resid|pct|ratio|deviat|gap|diff|delta|'
                        r'compare|vs_|_vs|overshoot|undershoot|closure|'
                        r'^tgt$|target', re.I)
_INPUT_RE = re.compile(r'^(alpha|scale|calib|norm|coeff|e0|b_pred|m_pred|'
                       r'pred|fit|anchor|pin)\b|_pred$|^b_sym', re.I)


def _binding_names(tree, lits: set) -> set:
    """Names bound to an assignment whose value contains an AME literal."""
    out = set()
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        val = node.value
        if val is None:
            continue
        src = ast.dump(val)
        if not any(("'" + L + "'") in src or ("=" + L) in src or L in src for L in lits):
            continue
        tgts = node.targets if isinstance(node, ast.Assign) else [node.target]
        for t in tgts:
            for n in ast.walk(t):
                if isinstance(n, ast.Name):
                    out.add(n.id)
    return out


def _is_alias(val, tainted: set) -> bool:
    """Is `val` still THE AME value, or a quantity DERIVED from it?

    An alias is the bare name, a trivial numeric/string wrapper of it
    (`mp.mpf(x)`, `float(x)`, `D(str(x))`), or a subscript of a tainted AME
    table (`B_AME["D"]`). Anything containing an operator is a DERIVED
    quantity, and the name that lands on is exactly the role signal this
    classifier reads -- propagating taint through arithmetic would erase the
    signal and make everything REVIEW again.
    """
    if any(isinstance(n, (ast.BinOp, ast.UnaryOp, ast.Compare, ast.BoolOp))
           for n in ast.walk(val)):
        return False
    used = {n.id for n in ast.walk(val) if isinstance(n, ast.Name)}
    return bool(used & tainted)


def _ame_slot(tree, fornode, lits: set):
    """The single loop variable that receives the AME literal, when knowable.

    Only fires for the shape the corpus actually uses: a module-level name bound
    to a list/tuple of same-length tuples, iterated with a tuple target. Returns
    the ast.Name for the slot whose column contains an AME literal, or None.
    """
    if not isinstance(fornode.target, ast.Tuple):
        return None
    names = [n for n in fornode.target.elts if isinstance(n, ast.Name)]
    if len(names) != len(fornode.target.elts):
        return None
    if not isinstance(fornode.iter, ast.Name):
        return None
    rows = None
    for nd in ast.walk(tree):
        if isinstance(nd, ast.Assign) and any(
                isinstance(tg, ast.Name) and tg.id == fornode.iter.id for tg in nd.targets):
            if isinstance(nd.value, (ast.List, ast.Tuple)):
                rows = nd.value.elts
            break
    if not rows:
        return None
    hits = set()
    for r in rows:
        if not isinstance(r, ast.Tuple) or len(r.elts) != len(names):
            return None
        for i, e in enumerate(r.elts):
            src = ast.dump(e)
            if any(L in src for L in lits):
                hits.add(i)
    return names[hits.pop()] if len(hits) == 1 else None


def _tainted_names(tree, lits: set) -> set:
    """`_binding_names` closed transitively over ALIASES.

    `_binding_names` alone stops at the first name. The corpus almost never
    stops there: it writes `B_AME = 2.224566`, then `b_exp = B_AME`, then
    `err_pct = (pred - b_exp) / b_exp`. One level of tainting sees `b_exp` as a
    sink with no role signal and gives up -- which is why 383 of the 389 REVIEW
    sites were "bound, but no signal". Closing over aliases follows the value to
    where its role is actually named.
    """
    t = set(_binding_names(tree, lits))
    for _ in range(10):
        grew = False
        for node in ast.walk(tree):
            # (i) alias assignment
            if isinstance(node, (ast.Assign, ast.AnnAssign)):
                if node.value is None or not _is_alias(node.value, t):
                    continue
                tgts = node.targets if isinstance(node, ast.Assign) else [node.target]
            # (ii) UNPACKING a tainted table. The corpus keeps AME values in
            #      row tuples --
            #          ISOTOPES = [("D", 1, 1, 2.22456612, ...), ...]
            #          for label, Z, N, B_AME, formula, leading in ISOTOPES:
            #              leading_err_pct = (leading - B_AME) / B_AME * 100
            #      -- and without this the taint stops at ISOTOPES, which is
            #      never itself in arithmetic. That file then looks like a value
            #      that is merely recorded, when it is the comparison target of
            #      the whole probe. Bind every loop variable: which slot holds
            #      the AME value is not knowable here, and over-tainting costs
            #      a REVIEW, while under-tainting costs a misclassification.
            elif isinstance(node, (ast.For, ast.AsyncFor)):
                if not ({n.id for n in ast.walk(node.iter) if isinstance(n, ast.Name)} & t):
                    continue
                # Prefer the POSITIONAL slot. `for label, Z, N, B_AME, ... in
                # ISOTOPES` over rows of literal tuples: only one slot holds the
                # AME value, and tainting `Z` and `N` as well floods the sink
                # census with loop-counter names and can manufacture a false
                # INPUT out of a variable that merely happens to be called
                # `scale`. When the rows are statically readable, taint that one
                # slot; otherwise fall back to the whole target.
                slot = _ame_slot(tree, node, lits)
                tgts = [slot] if slot is not None else [node.target]
            elif isinstance(node, ast.comprehension):
                if not ({n.id for n in ast.walk(node.iter) if isinstance(n, ast.Name)} & t):
                    continue
                tgts = [node.target]
            else:
                continue
            for tg in tgts:
                for n in ast.walk(tg):
                    if isinstance(n, ast.Name) and n.id not in t:
                        t.add(n.id)
                        grew = True
        if not grew:
            break
    return t


def _role_for(txt: str, lits: set) -> str:
    try:
        tree = ast.parse(txt)
    except SyntaxError:
        return "REVIEW"
    names = _tainted_names(tree, lits)
    if not names:
        return "REVIEW"
    saw_target = False
    for node in ast.walk(tree):
        # (a) assignment targets: `err_pct = (pred - AME) / AME`
        if isinstance(node, ast.Assign):
            # PAIRWISE for a tuple-to-tuple assignment. `pred, obs =
            # mp.mpf(mpred), mp.mpf(mobs)` taints only `obs`; reading the whole
            # statement as one unit hands the AME value to `pred` as well and
            # reports a prediction built from the measurement where the file
            # merely stores the two side by side.
            pairs = []
            if (len(node.targets) == 1 and isinstance(node.targets[0], ast.Tuple)
                    and isinstance(node.value, ast.Tuple)
                    and len(node.targets[0].elts) == len(node.value.elts)):
                pairs = list(zip(node.targets[0].elts, node.value.elts))
            if pairs:
                for tg, val in pairs:
                    if not ({n.id for n in ast.walk(val) if isinstance(n, ast.Name)} & names):
                        continue
                    for tn in ast.walk(tg):
                        if not isinstance(tn, ast.Name):
                            continue
                        if _INPUT_RE.search(tn.id):
                            return "INPUT"
                        if _TARGET_RE.search(tn.id):
                            saw_target = True
                continue
            used = {n.id for n in ast.walk(node.value) if isinstance(n, ast.Name)}
            if used & names:
                for t in node.targets:
                    for tn in ast.walk(t):
                        if not isinstance(tn, ast.Name):
                            continue
                        if _INPUT_RE.search(tn.id):
                            return "INPUT"
                        if _TARGET_RE.search(tn.id):
                            saw_target = True
        # (b) DICT-LITERAL KEYS. Most of this corpus records results as
        #     {"err_pct": (B_base - B_AME[n]) / B_AME[n], ...}
        #     which is the clearest target signal there is, and is invisible to
        #     (a) because the key is not an assignment target. Missing this put
        #     87% of the tail in REVIEW on the first pass.
        elif isinstance(node, ast.Dict):
            for k, v in zip(node.keys, node.values):
                if not isinstance(k, ast.Constant) or not isinstance(k.value, str):
                    continue
                used = {n.id for n in ast.walk(v) if isinstance(n, ast.Name)}
                if not (used & names):
                    continue
                if _INPUT_RE.search(k.value):
                    return "INPUT"
                if _TARGET_RE.search(k.value):
                    saw_target = True
    return "TARGET" if saw_target else "REVIEW"


def _in_range(v: float) -> bool:
    return (1.5 < v < 45) or (1800 < v < 12000)   # AME binding MeV or atomic-mass MeV



def _selftest() -> int:
    """Pin every role the classifier must be able to reach.

    A classifier that CANNOT return INPUT would report zero INPUT sites and
    look like good news. That is the failure this exists to make impossible:
    the zero below is only meaningful because these cases prove the path
    fires.
    """
    cases = [
        ("ALIAS CHAIN to a comparison: the corpus almost never names the "
         "literal and the residual with the same variable",
         'B_AME = 2.22452\nb_exp = B_AME\nerr_pct = (pred - b_exp) / b_exp\n',
         "TARGET"),
        ("TUPLE ASSIGNMENT is matched pairwise — storing a prediction beside "
         "the measurement is not building one from it",
         'ROWS = [(1, 2.0, 2.22452)]\n'
         'for Z, mpred, mobs in ROWS:\n'
         '    pred, obs = mp.mpf(mpred), mp.mpf(mobs)\n',
         "REVIEW"),
        ("UNPACKING a table of rows — the corpus keeps AME values in tuples "
         "and reads them out in a for-loop, so taint that cannot cross the "
         "unpack stops at a container that is never itself in arithmetic",
         'ISOTOPES = [("D", 2.22452, "vol")]\n'
         'for label, B_AME, formula in ISOTOPES:\n'
         '    err_pct = (leading - B_AME) / B_AME * 100\n',
         "TARGET"),
        ("ALIAS CHAIN to a calibration — the case that makes this closure "
         "load-bearing rather than cosmetic. Without it this reads REVIEW, "
         "and a REVIEW site that is really an INPUT is the one error this "
         "classifier exists to prevent.",
         'AME = {"D": 2.22452}\nb2 = AME["D"]\npred = comb(A, 2) * b2\n',
         "INPUT"),
        ("alias closure must NOT cross arithmetic: a derived quantity is not "
         "the AME value, and its name is the signal",
         'B_AME = 2.22452\ngap = B_AME - base\nscale = gap / ell\n',
         "TARGET"),
        ("calibration: a scale derived FROM the measurement, then multiplied "
         "back into a prediction of it",
         'B_AME = {"D": 2.22452}\nalpha = B_AME["D"] / ell\nB_pred = alpha * tr\n',
         "INPUT"),
        ("comparison, assignment target",
         'B_AME = {"D": 2.22452}\nerr_pct = (P - B_AME["D"]) / B_AME["D"]\n',
         "TARGET"),
        ("comparison, DICT KEY — the common shape in this corpus, and "
         "invisible to an assignment-target-only pass",
         'B_AME = {"D": 2.22452}\nrow = {"err_pct": (P - B_AME["D"]) / B_AME["D"]}\n',
         "TARGET"),
        ("opaque: escapes into a call, role unknowable statically",
         'B_AME = {"D": 2.22452}\nz = helper(B_AME["D"])\n',
         "REVIEW"),
    ]
    print("role-classifier self-test:")
    ok = True
    for name, src, want in cases:
        got = _role_for(src, {"2.22452"})
        good = got == want
        ok = ok and good
        print(f"  {'ok  ' if good else 'FAIL'}  {name}\n         got={got} want={want}")
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    if "--selftest" in sys.argv:
        return _selftest()
    # rglob, NOT glob. This used to scan `computations/*.py` only, with a
    # comment reasoning that substrate/ is a subdir and therefore excluded --
    # but that also hid probes/, deltalambda/, phase5/ and sweeps/, which is
    # where most of the tail actually lives. Same defect the q0 manifest had:
    # "the producer lookup was root-only, so half the corpus was invisible".
    files = [q for q in HERE.parent.rglob("*.py")
             if "_deprecated" not in q.parts and "_internal" not in q.parts
             and q.name != "codata_constants.py"]
    safe: dict[str, set] = {}
    unsafe: dict[str, set] = {}
    fixture: dict[str, set] = {}
    roles: dict[str, str] = {}
    site_roles: dict[str, str] = {}
    for p in files:
        fn = p.name
        txt = p.read_text(encoding="utf-8")
        fixlines = _fixture_lines(txt)
        for lit, lineno in _literals(txt):
            v = float(lit)
            if not _in_range(v):
                continue
            # A self-test line only matters if the literal is ACTUALLY an AME
            # value. _in_range is a numeric window, not a semantic test: without
            # the near-match gate this branch swallowed Euler's number
            # (2.718281828) and a beam eigenvalue (4.73124891) from
            # no_free_parameter_certificate, and four unrelated magnitudes from
            # witness_raw_float64_audit, reporting six sites of routing work
            # that never existed.
            # classifier arithmetic on decimal strings, mirroring the
            # near-match test below: this decides a BUCKET, not a quantity
            _near = lit in REG or any(abs(v - float(rs)) / float(rs) < 5e-6  # float64-ok: bucket decision, not a computed quantity
                                      for rs in REG)
            if lineno in fixlines and _near:
                fixture.setdefault(fn, set()).add((lit, REG.get(lit, "~near")))
            elif lineno in fixlines:
                pass
            elif lit in REG:
                safe.setdefault(fn, set()).add((lit, REG[lit]))
            else:
                for rs, nm in REG.items():
                    if abs(v - float(rs)) / float(rs) < 5e-6:
                        unsafe.setdefault(fn, set()).add((lit, nm, rs))
                        break
        if fn in unsafe and fn not in roles:
            roles[fn] = _role_for(txt, {l for l, _n, _r in unsafe[fn]})
            # PER-SITE roles as well. A file-level role cannot say WHICH literal
            # earns it, and acting on the file-level answer is how a 4He literal
            # feeding `B_pred` in low_isotope_binding_sweep got routed while two
            # files whose INPUT role came from entirely different literals were
            # held back. Route decisions are per site, so the role must be too.
            for _l, _n, _r in unsafe[fn]:
                site_roles[f"{fn}:{_l}"] = _role_for(txt, {_l})

    n_safe_routes = sum(len(v) for v in safe.values())
    n_unsafe = sum(len(v) for v in unsafe.values())
    print(f"AME-literal → registry routing triage")
    print(f"  registry value strings: {len(REG)}")
    n_fixture = sum(len(v) for v in fixture.values())
    print(f"  SAFE (byte-exact, value-preserving): {n_safe_routes} routes in {len(safe)} files")
    print(f"  IN-SELF-TEST (routing needs a per-test ruling): "
          f"{n_fixture} in {len(fixture)} files")
    print(f"  UNSAFE (near, value-change — decision needed): {n_unsafe} in {len(unsafe)} files")
    _rnd = {(f, l) for f, v in unsafe.items() for l, _n, r in v if _is_rounding(l, r)}
    _div = {(f, l) for f, v in unsafe.items() for l, _n, r in v if not _is_rounding(l, r)}
    print(f"    ROUNDING   {len(_rnd):>4} sites in {len({f for f, _ in _rnd}):>3} files   "
          f"the registry value at fewer digits — routing is a precision gain")
    print(f"    DIVERGENT  {len(_div):>4} sites in {len({f for f, _ in _div}):>3} files   "
          f"disagrees at a printed digit — a provenance ruling, not a refactor")

    # Role split. SAFE/UNSAFE says whether routing moves a VALUE; role says
    # whether the site may be routed AT ALL. A prediction INPUT must not be,
    # whatever its value does (bean fvxq, 3-cal).
    by_role: dict[str, list] = {"TARGET": [], "INPUT": [], "REVIEW": []}
    for fn in unsafe:
        by_role.setdefault(roles.get(fn, "REVIEW"), []).append(fn)
    print("  UNSAFE by role — what the AME-bound name flows into:")
    for r, why in (("TARGET", "only error/comparison names — routable once the value question is settled"),
                   ("INPUT",  "reaches a scale/calibration or predicted name — NEVER route (3-cal)"),
                   ("REVIEW", "neither, or escapes into a call — needs reading")):
        fns = sorted(by_role.get(r, []))
        n = sum(len(unsafe[f]) for f in fns)
        print(f"    {r:7} {n:4} sites in {len(fns):3} files   {why}")
    print(f"\n  SAFE files (route value-preservingly):")
    for fn in sorted(safe):
        print(f"    {fn:46} {sorted(l for l, _ in safe[fn])}")

    witness = {
        "computation": "ame-registry-routing-triage",
        "kind": "infrastructure-triage",
        "description": (
            "Classifies inline AME-range literals in computations/*.py as SAFE "
            "(byte-exact to a codata_constants registry export → value-preserving "
            "route) vs UNSAFE (near but not exact → routing changes the value). The "
            "registry's last-digit conventions differ from many corpus literals, so "
            "the fvxq tail is not a uniform sweep. SAFE = the routing work; UNSAFE = "
            "value-reconciliation decisions that must precede any route."
        ),
        "registry_value_strings": REG,
        # The INPUT role is the one classification that must NEVER be acted against:
        # it marks a name reaching a scale/calibration or predicted quantity, where
        # routing a _VALIDATION constant violates the 3-cal rule. It was printed but
        # not witnessed, so a consumer reading the roadmap could not see it.
        "roles": dict(sorted(roles.items())),
        "site_roles": dict(sorted(site_roles.items())),
        "rounding_sites": sorted(f"{f}:{l}" for f, l in _rnd),
        "divergent_sites": sorted(f"{f}:{l}" for f, l in _div),
        "fixture_sites": {k: sorted(v) for k, v in fixture.items()},
        "safe_routes": {fn: sorted([list(t) for t in v]) for fn, v in sorted(safe.items())},
        "unsafe_near_matches": {fn: sorted([list(t) for t in v]) for fn, v in sorted(unsafe.items())},
        "counts": {"safe_routes": n_safe_routes, "safe_files": len(safe),
                   "unsafe_near_matches": n_unsafe, "unsafe_files": len(unsafe)},
        "note": ("Routing + per-file run-verification (the fvxq value-preservation "
                 "discipline) is infra-gated in some sandboxes: many target files import "
                 "pyhecke_native (buildable, ~42s) or have pre-existing runtime errors. "
                 "This triage (pure string compare) runs anywhere and is the roadmap."),
        "bean": "fvxq", "sibling": "claude/fvxq-atomic-mass-registry-2026-06-21",
    }
    out = HERE.parent / "ame-registry-routing-triage.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
    witness["scriptFile"] = _os.path.basename(__file__)
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"\n  witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
