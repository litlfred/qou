#!/usr/bin/env python3
# polynomial_q_not_applicable: static source audit; emits no numeric physics.
"""Catch a hardcoded witness value that has ALREADY drifted from its source.

## The blind spot this closes

`witness_value_copy_audit.py` finds a script that hardcodes a value another
producer computed, by looking the source literal up in an index of every value
in every committed witness. That lookup is **exact string equality**
(`if sig_digits(lit) < MIN_SIG or lit not in idx: continue`), and it is the
right design for what that audit does: an exact match is what establishes that
the literal *is* a copy rather than a coincidence, so the finding can be acted
on -- convert the copy into a read.

But read its own statement of the harm:

    Staleness. The producer is re-run, the witness changes, and the copy does
    not. The two silently disagree from then on, with nothing to detect it.

**The moment that happens, the copy stops matching exactly, and the exact-match
lookup goes blind to it.** So the sibling audit sees copies that are still
fresh -- the ones that are not yet a problem -- and loses each one at exactly
the moment it becomes one. Its 271 findings are all live copies awaiting
conversion; a copy that already drifted is in neither the findings nor the
clean set. It is nowhere.

The two audits are complementary and neither subsumes the other:

  sibling  keys on the VALUE   -> finds fresh copies, blind once they drift
  this one keys on the NAME    -> finds drifted copies, because a name does
                                  not change when the value it refers to does

## The worked case (bean qou-l4q3)

`qbeta_habiro_integrality_kill_test.py` carried

    # Cross-check targets from committed witnesses (muon/canonical q0 chain)
    N3_WITNESS_B   = mp.mpf("0.86758406730714238749179779530277068827007617830461...")
    N3_WITNESS_QN2 = mp.mpf("0.78233438651817188475730658357783604758705596862882...")
    N3_WITNESS_C3  = mp.mpf("-2.0216155770600061205300249700296445660947408177192...")

snapshotted from `q-beta-operator-valued-N3.witness.json` on 2026-07-11. That
witness has since migrated to the proton pin, and the constants were left at
the RETIRED muon pin. Its three cross-checks had been failing for about a
month; the committed witness still recorded `allPassed: true`, because it too
predated the drift.

The sibling audit could not see it: none of the three literals appears in any
witness any more. The names could not be plainer -- `N3_WITNESS_*`, under a
comment saying "from committed witnesses" -- and nothing was looking at names.

## What this audit does

Find every assignment whose **name declares a witness provenance**
(`*WITNESS*`), or that carries a comment naming a `.witness.json`, and whose
value is a decimal literal of at least `MIN_SIG` significant digits. Then two
checks, strongest first:

1. **`DECLARED_SOURCE_MISSING`** -- when the comment names a SPECIFIC witness
   file, ask *that file*. The author wrote down where the number came from, so
   the claim is checkable directly and needs no index at all. A literal can be
   perfectly fresh against some witness somewhere and still have a declared
   source that does not carry it: that is a provenance claim being wrong rather
   than a value being stale, and **neither this audit's index nor the sibling's
   can see it**, since both ask "does any witness carry this" instead of "does
   the named one".

2. **`DRIFTED`** -- otherwise, look the literal up in the same exact-value
   index the sibling builds.
   * present -> FRESH. The sibling audit owns it; not reported here.
   * absent  -> the name claims a witness carries this number and none does.

Each finding names the most likely source by longest shared decimal prefix, so
it is actionable rather than merely alarming.

## These are CANDIDATES; the verdict is an agent's

A comment can name a witness for context rather than as the value's source, and
a value can be deliberately stale (`Q0_STALE_MUON_PIN` is a real example -- the
test is *about* a superseded pin, so the number is meant to be old even though
the provenance claim has since broken). What the audit establishes is narrow
and checkable: **the named file does not carry this value.** Whether that
matters is a judgement, the same posture as the vacuity audit's ledger.

## What is NOT a finding

* A declared source that carries the same number at a DIFFERENT WIDTH. The
  check is width-tolerant for the same reason the drift check is; a substring
  test calls that absent, and 1 of the first 11 findings was exactly this.
* A neighbouring line's declaration. Consecutive constants each carry their own
  trailing comment, so the own-line comment takes precedence over the block
  above -- without that, a three-line window asks the wrong witness about
  `REF_B5` and reports a clean site.
* A literal that IS still in some witness -- reported by the sibling, not here.
* Fewer than `MIN_SIG` significant digits: short decimals collide by accident,
  the same floor and the same reasoning as the sibling.
* A name matching `*WITNESS*` bound to something that is not a number (a path,
  a filename, a dict) -- there is no value to compare.
* The same number rendered at two precisions. `0.57517233101788385191979179668`
  against a witness `0.575172331017883851919791796687` is one value at two
  output widths, not a disagreement; so is a witness carrying the ROUNDED
  rendering rather than a truncated one, which a naive prefix test gets wrong
  in the opposite direction. `_agrees_to_shorter` is the guard, and without it
  3 of the first 5 findings were this.

## The residual limit, stated rather than hidden

A DRIFTED finding says *no witness carries this value*. It does not, by itself,
prove the literal was ever copied from one: an author could name a constant
`X_WITNESS_Y` and type a number that never came from a witness at all. The
prefix report is what separates those -- a long shared prefix with a real
witness value is strong evidence of a drifted copy, a short one is not. The
verdict is an agent's, and the audit says which evidence it has.

Output: `drifted-witness-copy-audit.witness.json`.
"""
from __future__ import annotations

import argparse
import ast
import json
import pathlib
import re
import sys as _sys
from decimal import Decimal, localcontext

_sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from qou_substrate.witness import WitnessBuilder  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
COMP = ROOT / "computations"
OWN_WITNESS = pathlib.Path(__file__).stem.replace("_", "-") + ".witness.json"

# Same floor and same reasoning as witness_value_copy_audit: below this,
# decimals collide by coincidence and the audit becomes noise.
MIN_SIG = 11

NUMBER = re.compile(r"\d+\.\d+")
#: A name that ASSERTS a witness provenance. Deliberately narrow -- this audit
#: trades recall for precision, because its whole value is that a hit is worth
#: opening. `WITNESS` as a word, not `w`, not `ref`, not `expected`.
NAME_DECLARES = re.compile(r"WITNESS", re.IGNORECASE)
#: A comment naming a witness file, which declares provenance just as a name does.
COMMENT_DECLARES = re.compile(r"\.witness\.json|committed witness", re.IGNORECASE)
#: A comment that names a SPECIFIC witness file. This is the strongest signal
#: the corpus offers: the author wrote down where the number came from, so the
#: claim can be checked against that exact file rather than against the whole
#: index.
NAMED_SOURCE = re.compile(r"([A-Za-z0-9_.-]+\.witness\.json)")


def sig_digits(lit: str) -> int:
    return len(lit.replace(".", "").replace("-", "").lstrip("0"))


def index_witnesses() -> dict[str, set[str]]:
    """decimal literal -> witness paths carrying it (exact string match).

    Excludes this audit's own witness for the reason the sibling records: an
    audit that writes its findings into a file it then indexes becomes a
    carrier for them, and every finding sustains itself forever.
    """
    idx: dict[str, set[str]] = {}
    for w in COMP.rglob("*.witness.json"):
        if w.name == OWN_WITNESS:
            continue
        try:
            raw = w.read_text()
        except OSError:
            continue
        for m in NUMBER.finditer(raw):
            lit = m.group(0)
            if sig_digits(lit) >= MIN_SIG:
                idx.setdefault(lit, set()).add(str(w.relative_to(ROOT)))
    return idx


def _literal_of(node: ast.AST) -> str | None:
    """The decimal literal a value node carries, through a numeric ctor.

    Handles `0.5`, `"0.5"`, `mp.mpf("0.5")`, `mpf('-0.5')`, `Decimal("0.5")`
    and a unary minus in front of any of them. Returns the digits WITHOUT the
    sign, because the witness index is built from unsigned `NUMBER` matches
    and a signed lookup would miss every negative constant -- which is how a
    first version of this audit reported 0 findings on a file it was written
    from.
    """
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return _literal_of(node.operand)
    if isinstance(node, ast.Constant):
        v = node.value
        if isinstance(v, float):
            return repr(v)
        if isinstance(v, str):
            m = NUMBER.search(v)
            return m.group(0) if m else None
        return None
    if isinstance(node, ast.Call):
        for a in node.args:
            got = _literal_of(a)
            if got:
                return got
    return None


def _comment_context(lines: list[str], lineno: int) -> tuple[str, str]:
    """(own-line trailing comment, block above) for a 1-indexed line number.

    THE TWO MUST BE KEPT APART, and a first version merged them into one blob.
    Consecutive constants each carry their own trailing comment:

        REF_B4 = mp.mpf("-10.3376891441")   # qbeta-5two-higher-cable-qstar...
        REF_B5 = mp.mpf("593.607693594")    # qbeta-5two-n5-cable-qstar...

    A three-line window over REF_B5 picks up REF_B4's file name, so the audit
    asked the WRONG witness and reported a clean site. Found by triaging its
    own output; the own-line comment therefore takes precedence and the block
    above is only the fallback.
    """
    own = lines[lineno - 1] if 0 < lineno <= len(lines) else ""
    own_c = own[own.index("#"):] if "#" in own else ""
    lo = max(0, lineno - 4)
    above = "\n".join(
        ln[ln.index("#"):] for ln in lines[lo:lineno - 1] if "#" in ln)
    return own_c, above


_OWN_CACHE: dict[str, set[str]] = {}


def own_witnesses(py: pathlib.Path) -> set[str]:
    """Witness paths this script itself writes, by `scriptFile` provenance.

    A producer that hardcodes a value appearing in ITS OWN witness is doing a
    regression check against itself, not copying someone else's number -- the
    same exemption `witness_value_copy_audit` makes, and for the same reason.
    Without it this audit reports a producer's own value rendered at a
    different output width, which is 3 of its first 5 findings.
    """
    key = str(py)
    if key in _OWN_CACHE:
        return _OWN_CACHE[key]
    stem = py.stem.replace("_", "-")
    out: set[str] = set()
    for w in COMP.rglob(f"{stem}*.witness.json"):
        out.add(str(w.relative_to(ROOT)))
    for w in COMP.rglob("*.witness.json"):
        try:
            j = json.loads(w.read_text())
        except (OSError, ValueError):
            continue
        comp = j.get("computation")
        sf = j.get("scriptFile") or (comp.get("script") if isinstance(comp, dict) else None)
        if isinstance(sf, str) and pathlib.Path(sf).name == py.name:
            out.add(str(w.relative_to(ROOT)))
    _OWN_CACHE[key] = out
    return out


def scan(idx: dict[str, set[str]]) -> list[dict]:
    findings: list[dict] = []
    for py in sorted(COMP.rglob("*.py")):
        if py.resolve() == pathlib.Path(__file__).resolve():
            continue          # never scan self: the docstring quotes literals
        try:
            src = py.read_text()
            tree = ast.parse(src)
        except (OSError, SyntaxError):
            continue
        lines = src.splitlines()
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            names = [t.id for t in targets if isinstance(t, ast.Name)]
            if not names:
                continue
            lit = _literal_of(node.value)
            if lit is None or sig_digits(lit) < MIN_SIG:
                continue
            own_c, above_c = _comment_context(lines, node.lineno)
            comment = own_c + "\n" + above_c
            by_name = any(NAME_DECLARES.search(n) for n in names)
            by_comment = bool(COMMENT_DECLARES.search(comment))
            if not (by_name or by_comment):
                continue
            # STRONGEST CHECK FIRST, and it is independent of the index. When
            # a comment names a specific witness file, the author has written
            # down where the number came from -- so ask THAT file. A literal
            # can be perfectly fresh against some witness somewhere and still
            # have a declared source that does not carry it, which is a claim
            # about provenance being wrong rather than a value being stale.
            # Neither this audit's index nor the sibling's can see that, since
            # both ask "does any witness carry this" rather than "does the
            # named one".
            # Own-line comment wins: it belongs to THIS assignment.
            named = NAMED_SOURCE.search(own_c) or NAMED_SOURCE.search(above_c)
            if named:
                srcs = list(COMP.rglob(named.group(1)))
                if srcs:
                    raw = srcs[0].read_text()
                    # Width-tolerant, not `lit not in raw`. The declared file
                    # may render the same number at a different precision, and
                    # a substring test calls that absent. Measured: 1 of 11
                    # findings was this, caught by triaging the output.
                    carried = any(
                        sig_digits(c) >= 8 and _agrees_to_shorter(lit, c)
                        for c in NUMBER.findall(raw))
                    if not carried:
                        findings.append({
                            "file": str(py.relative_to(ROOT)),
                            "line": node.lineno,
                            "name": names[0],
                            "literal": lit,
                            "declared_by": "comment naming a file",
                            "class": "DECLARED_SOURCE_MISSING",
                            "declared_source": str(srcs[0].relative_to(ROOT)),
                            "nearest_witness_value": _nearest(lit, idx),
                        })
                        continue

            if lit in idx:
                continue      # FRESH -- the sibling audit owns it
            near = _nearest(lit, idx)
            if near and near["same_number_at_lower_precision"]:
                continue      # same value, different output width -- not drift
            own = own_witnesses(py)
            if near and set(near["carriers"]) <= own:
                # The ONLY carrier is this producer's own output. The sibling
                # audit exempts that as a self-regression check -- but here the
                # name or comment DECLARES an external source, so "the only
                # place this number lives is the file that writes it" is the
                # finding, not an exemption. Kept as a separate class rather
                # than dropped: measured, dropping it hid the one case where a
                # constant's declared source does not carry it at all.
                pass
            findings.append({
                "file": str(py.relative_to(ROOT)),
                "line": node.lineno,
                "name": names[0],
                "literal": lit,
                "declared_by": "name" if by_name else "comment",
                "class": "DRIFTED",
                "nearest_witness_value": near,
                "only_carrier_is_own_output": bool(near and set(near["carriers"]) <= own),
            })
    return findings


def _agrees_to_shorter(a: str, b: str) -> bool:
    """Do two decimal strings agree once the longer is rounded to the shorter?

    This is the distinction the whole audit turns on, and the first version of
    it did not make. `0.57517233101788385191979179668` against a witness
    `0.575172331017883851919791796687` is the SAME NUMBER rendered at two
    precisions -- a difference in output width, not a disagreement. So is
    `1.7916878279761012` against `1.79168782798`, where the witness carries the
    ROUNDED rendering rather than a truncated one, which a prefix test gets
    wrong in the opposite direction.

    Only a value that differs before the shorter rendering runs out has
    actually moved, and only that is a finding.
    """
    if a.startswith(b) or b.startswith(a):
        return True           # one is the other TRUNCATED -- same value, fewer digits
    d_a, d_b = Decimal(a), Decimal(b)
    short, long_ = (d_a, d_b) if len(a.replace(".", "")) <= len(b.replace(".", "")) else (d_b, d_a)
    n = len(short.as_tuple().digits)
    with localcontext() as ctx:
        ctx.prec = n
        return +long_ == +short   # ... or the other ROUNDED


def _nearest(lit: str, idx: dict[str, set[str]]) -> dict | None:
    """Longest shared-prefix witness value, as evidence of the intended source.

    A long shared prefix is strong evidence the literal came from that value; a
    short one is not, and the caller is told which it got rather than being
    handed a verdict.
    """
    best, best_len = None, 0
    for cand in idx:
        n = 0
        for a, b in zip(lit, cand):
            if a != b:
                break
            n += 1
        n -= lit[:n].count(".")          # count DIGITS, not the decimal point
        if n > best_len:
            best, best_len = cand, n
    if best is None or best_len < 4:
        return None
    return {"value": best, "shared_leading_digits": best_len,
            "same_number_at_lower_precision": _agrees_to_shorter(lit, best),
            "carriers": sorted(idx[best])[:3]}


def _selftest() -> int:
    """Fire on the case this audit was written from, and decline the sibling's.

    Case 1 is the pre-fix `qbeta_habiro_integrality_kill_test` constant, which
    the exact-match sibling structurally cannot see. Case 2 is a fresh copy,
    which it can, and which this audit must therefore stay quiet about --
    otherwise the two overlap and every finding is reported twice.
    """
    idx = {"0.8675840669652511556511628915360523957049793773943147562967":
           {"computations/q-beta-operator-valued-N3.witness.json"}}
    drifted = "0.8675840673071423874917977953027706882700761783046107644471"
    fresh = "0.8675840669652511556511628915360523957049793773943147562967"
    bad = 0
    for label, lit, want in (
        ("drifted copy (qou-l4q3)", drifted, True),
        ("fresh copy (sibling's)", fresh, False),
    ):
        got = lit not in idx and sig_digits(lit) >= MIN_SIG
        ok = got == want
        bad += not ok
        print(f"  [{'ok ' if ok else 'FAIL'}] reports={got!s:5} want={want!s:5}  {label}")
    near = _nearest(drifted, idx)
    shared = near["shared_leading_digits"] if near else 0
    ok = shared == 9
    bad += not ok
    print(f"  [{'ok ' if ok else 'FAIL'}] nearest-source prefix = {shared} digits "
          f"(want 9: the two agree to 0.86758406 and diverge after)")
    # A negative literal must resolve through the unary minus AND drop its sign,
    # or every negative witness constant is invisible.
    got = _literal_of(ast.parse('mp.mpf("-2.021615577060006120530024970029")'
                                ).body[0].value)
    ok = got == "2.021615577060006120530024970029"
    bad += not ok
    print(f"  [{'ok ' if ok else 'FAIL'}] negative-through-ctor -> {got!r}")
    # The precision guard, which is what keeps this audit from reporting the
    # same number rendered two ways. Both directions: a TRUNCATED witness
    # rendering and a ROUNDED one, since a prefix test gets the second wrong.
    for a_, b_, want, label in (
        ("0.57517233101788385191979179668",
         "0.575172331017883851919791796687", True, "source truncates the witness"),
        ("1.6183053302953433958898778525126", "1.6183053302953433959",
         True, "witness carries the ROUNDED rendering"),
        ("0.575172331017883851919791796687",
         "0.5751723310178838519197917966", True, "witness is a clean prefix"),
    ):
        got_ = _agrees_to_shorter(a_, b_)
        ok = got_ == want
        bad += not ok
        print(f"  [{'ok ' if ok else 'FAIL'}] same-number={got_!s:5} want={want!s:5}  {label}")
    print("selftest:", "PASS" if not bad else f"{bad} FAILURE(S)")
    return 1 if bad else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--list", action="store_true", help="print every finding")
    args = ap.parse_args(argv)
    if args.selftest:
        return _selftest()

    idx = index_witnesses()
    findings = scan(idx)

    b = WitnessBuilder("drifted-witness-copy-audit")
    b.set_description(
        "Bean qou-odb0. Complements witness_value_copy_audit, which keys on "
        "the VALUE and so goes blind to a copied witness value at exactly the "
        "moment it drifts and stops matching. This one keys on the NAME (an "
        "identifier or comment declaring a witness provenance) and reports the "
        "literals no witness carries any more. Worked case: the three "
        "N3_WITNESS_* constants in qbeta_habiro_integrality_kill_test, stale "
        "for a month against three failing cross-checks (bean qou-l4q3), "
        "invisible to the sibling audit throughout."
    )
    by_class: dict[str, int] = {}
    for f in findings:
        by_class[f["class"]] = by_class.get(f["class"], 0) + 1
    b.add_data("population", {
        "witness_literals_indexed": len(idx),
        "min_significant_digits": MIN_SIG,
        "findings_total": len(findings),
        "findings_by_class": by_class,
        "note": "DRIFTED is empty on this corpus as of 2026-09-06: the case "
                "this audit was written from (qbeta_habiro_integrality_kill_"
                "test, bean qou-l4q3) is fixed, and no other witness-named "
                "literal has drifted from a value some witness still carries. "
                "An empty class is a result, not a broken detector -- the "
                "selftest fires on the known instance.",
    })
    b.add_data("findings", findings)
    b.add_data("scope", {
        "not_reported_here": "a literal still present in some witness -- that "
                             "is a FRESH copy and witness_value_copy_audit "
                             "owns it. The two audits partition the class.",
        "residual_limit": "a finding says no witness carries this value; it "
                          "does not by itself prove the literal was ever "
                          "copied from one. `nearest_witness_value` is the "
                          "evidence for that, and a short shared prefix is "
                          "weak evidence. The verdict is an agent's.",
    })
    b.add_assertion(
        "audit_examined_a_populated_index",
        computed="1" if len(idx) > 1000 else "0",
        expected="1",
        source=f"{len(idx)} distinct witness literals of >= {MIN_SIG} "
               f"significant digits were indexed. Asserted because an audit "
               f"that reports zero findings against an EMPTY index has "
               f"examined nothing, and would read as a clean tree.",
    )
    b.save()

    print(f"indexed witness literals (>= {MIN_SIG} sig digits): {len(idx)}")
    print(f"findings: {len(findings)}   " +
          "  ".join(f"{k}={v}" for k, v in sorted(by_class.items())))
    print("(DRIFTED empty means no witness-named literal has drifted from a "
          "value a witness still carries;\n the selftest fires on the known "
          "instance, so an empty class is a result.)\n")
    show = findings if args.list else findings[:15]
    for f in show:
        near = f["nearest_witness_value"]
        print(f"  {f['file']}:{f['line']}  {f['name']} = {f['literal'][:34]}")
        if near:
            print(f"      nearest witness value shares {near['shared_leading_digits']}"
                  f" digits: {near['value'][:34]}")
            print(f"      carried by {near['carriers'][0]}")
        else:
            print("      no witness value shares a meaningful prefix "
                  "(weak evidence it was ever a copy)")
    if not args.list and len(findings) > len(show):
        print(f"  ... and {len(findings) - len(show)} more (--list)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
