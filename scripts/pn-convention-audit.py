#!/usr/bin/env python3
"""Audit which p-n interface convention each site uses.

The inter-nucleon (proton-neutron) bond carries a Markov factor

    f_pn = z - h * (1/2 - eps)

with `z = q^3/(q^2+1)` (convention D) and `h = q - 1/q`. Two values of
the weight offset `eps` are live in this corpus:

    strict_averaged       eps = 0        f_pn = z - h/2
    bring_color_weighted  eps = delta/4  f_pn = z - h*(1/2 - delta/4)

where `delta = (q-1)^2 (1 - q^-4)/3` is the substrate flavour split. The
owner ruling of 2026-08-15 (R3), reaffirmed 2026-08-26, makes
`bring_color_weighted` canonical. `strict_averaged` is the COLOUR-BLIND
one: it is the bar-symmetriser of `z`, correct as mathematics, wrong as
this framework's p-n bond.

At the proton pin the two differ by `h*delta/4 = 7.190163e-05`, a
relative 1.415e-04 -- about 1e11 times the float64 floor, so a recorded
value tells you unambiguously which convention produced it.

WHY BOTH A SOURCE SCAN AND A VALUE SCAN. A source scan keys on how the
convention was WRITTEN and is defeated by every re-spelling in
docs/audits/2026-08-15-detector-blindness-taxonomy.md. A value scan keys
on what the number IS and cannot be fooled by spelling -- but only
reaches witnesses that record the factor itself, not the ones that
record something downstream of it. Neither is complete; run both and
read them together.

Usage:
    python3 scripts/pn-convention-audit.py               # both scans
    python3 scripts/pn-convention-audit.py --source      # source only
    python3 scripts/pn-convention-audit.py --witness     # witnesses only
    python3 scripts/pn-convention-audit.py --json
    python3 scripts/pn-convention-audit.py --selftest
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ── the two reference values at the proton pin ───────────────────────────────
# Recomputed by --selftest from the live producers, never trusted from here.
# 50-dps values. An earlier revision of this file carried the evaluation at
# `q_parameter.Q`, which is a FLOAT64: identical to 17 significant digits
# and divergent after, so it looked right and was not. The committed
# witnesses record the 50-dps form.
BLIND_STR = "0.508157887748645593880406757381"
CANON_STR = "0.508229789376738962577995797656"
# 12 significant digits separates them by ~1e8 and survives f64 round-tripping.
# Unaffected by the q-precision correction above: the two forms agree to 17.
BLIND_KEY = "0.508157887748"
CANON_KEY = "0.508229789376"

# Trees that are not live source.
EXCLUDE_DIRS = (
    "/_deprecated/",
    "/node_modules/",
    "/.git/",
    "/.beans/",
    "/lake-packages/",
    "/.lake/",
)
# Generated mirror -- never hand-edit; sync from computations/ instead.
GENERATED = "/qou-mass/src/qou_mass/_internal/"


def _excluded(p: Path) -> bool:
    s = "/" + str(p.relative_to(ROOT)).replace("\\", "/")
    return any(d in s for d in EXCLUDE_DIRS)


# ── source scan ──────────────────────────────────────────────────────────────
# A p-n factor open-coded with eps = 0. Deliberately several spellings: the
# taxonomy's lesson is that one spelling is never the whole surface.
BLIND_SHAPES = (
    re.compile(r"-\s*(?:hecke_)?[hH](?:_q)?\s*/\s*2\b"),
    re.compile(r"-\s*0?\.5\s*\*\s*(?:hecke_)?[hH]\b"),
    re.compile(r"-\s*(?:hecke_)?[hH]\s*\*\s*0?\.5\b"),
    re.compile(r"\bz\s*-\s*(?:hecke_)?[hH]\s*/\s*2\b"),
    # Rust
    re.compile(r"-\s*\(\s*0\.5\s*\*\s*h\s*\)"),
    re.compile(r"StrictAveraged"),
)
# Evidence the site is canonical rather than blind.
CANON_MARKS = (
    "bring_color_weighted",
    "BringColorWeighted",
    "flavor_split_leading",
    "flavour_split_leading",
    "pn_interface_factor",
    "pn_offset",
    "delta_m_over_M",
    # A dual detector that computes the weighted offset in order to ACCEPT
    # both is canonical machinery, not a blind site.
    "_D_PN_WEIGHTED",
    "_pn_weighted_d",
)
# A COMPARISON site is one that computes BOTH conventions on purpose --
# never drain it. The test is that both NAMES appear, not that the file
# says something convention-ish: the first version accepted "CONVENTION
# CAVEAT" and "comparison" as marks, which misclassified
# mu4_rhoF_cluster_derivation_probe.py -- a genuinely blind site that a
# previous PR LABELLED rather than flipped. A label is not a comparison,
# and a classifier that cannot tell them apart hides exactly the sites a
# flip needs to find.
# A file may work in the colour-blind limit DELIBERATELY without ever naming
# a convention -- by declaring `delta -> 0`, "equal-weight", or "colour-blind"
# in its own prose. `bond_extensivity_equal_weight.py` says "(delta->0)" in its
# module docstring and is exactly right to use `z - h/2`; draining it on the
# strength of the shape alone would silently change what the probe measures.
# These are reported as DECLARED_BLIND, never as actionable.
DECLARED_BLIND_RE = re.compile(
    r"(\u03b4\s*(\u2192|->|=)\s*0|delta\s*(\u2192|->|=)\s*0"
    r"|delta-degenerate|\u03b4-degenerate|colou?r-blind"
    r"|no flavou?r split|equal[- ]weight)", re.I)

# TWO VOCABULARIES NAME THE SAME PAIR. The convention-level names are
# `strict_averaged` / `bring_color_weighted`; the ctype-level names, used by
# `d_for_ctype` and the seminormal machinery, are `averaged` /
# `averaged_weighted`. A file that builds BOTH interfaces using only the
# second vocabulary is just as deliberate a comparison as one using the
# first, and the initial list knew only the first -- so
# `rho_w_crystal_vertex_trace.py` read as BLIND while its own docstring says
# "Two interfaces, not one: the colour-blind `averaged` ... and the
# colour-weighted `averaged_weighted`".
BLIND_NAMES = ("strict_averaged", "StrictAveraged", '"averaged"', "'averaged'")
CANON_NAMES = ("bring_color_weighted", "BringColorWeighted",
               "averaged_weighted", "d_for_ctype",
               # A file that ALREADY accepts both offsets is a dual detector,
               # not a blind site: atom_braid_active_partitions.py matches
               # `d == -H_HALF or d == _D_PN_WEIGHTED` on purpose.
               "_D_PN_WEIGHTED", "_pn_weighted_d", "pn_interface_offset",
               "colour-blind z - h/2 was")

# The p-n bond has to actually be what the line is about.
# `\b` treats `_` as a word character, so `\bpn\b` does NOT match `V_pn_exact`,
# `f_pn`, `pn_d` or `d_pn` -- i.e. it missed the ordinary Python naming
# convention for this bond, which is the commonest way it appears. Explicit
# alphanumeric lookaround treats `_` as a delimiter, which is what was meant.
#
# Found by an ASSERTION, not by the detector: after the flip,
# confined_knot_binding's `V_pn = W_std*(z+d_pn)` check failed because
# `V_pn_exact = W_STD * (z - h/2)` two hundred lines earlier was still blind
# and invisible to this filter. Keep such assertions; they audit the auditor.
PN_CONTEXT = re.compile(
    r"(?<![A-Za-z0-9])p[-_]?n(?![A-Za-z0-9])|inter[-_]?nucleon|interface", re.I)

# `h/2` near the word "interface" is not automatically a p-n site. The
# SAME-FLAVOUR tag in delta_lambda_v_hat_z_transfer_phase5d_4.py matches
# `|V| == h/2` to label a p-p or n-n interface -- the p-n case there is the
# `V == 0` branch above it. Excluding on the site's own same-flavour wording
# is precise; widening PN_CONTEXT to demand a literal "pn" token would drop
# real sites that only say "interface".
# The quark-level u-d mixed crossing is a DIFFERENT BOND and keeps -h/2:
# nothing in this corpus establishes what convention a u-d crossing carries.
# It lives in the same function as the nucleon p-n branch (`build_atom_nf`),
# so enclosing-function context cannot separate them -- the site's OWN line
# can, because it says `ud -> sigma_0 mixed`.
UD_CROSSING = re.compile(r"\bu-?d\b|\bquark\b|\bud\s*(->|→)", re.I)

SAME_FLAVOUR = re.compile(r"same[-_ ]?flavou?r|\bp-p\b|\bn-n\b|\bpp\b.*\bnn\b",
                          re.I)


def _is_h_name(node) -> bool:
    """`h`, `H`, `h_q`, `hecke_h(...)`, `self.h` -- the Hecke h by any spelling."""
    if isinstance(node, ast.Name):
        return node.id in ("h", "H", "h_q", "H_q", "_h", "hf", "HA")
    if isinstance(node, ast.Attribute):
        return node.attr in ("h", "H", "h_q")
    if isinstance(node, ast.Call):
        f = node.func
        name = f.id if isinstance(f, ast.Name) else getattr(f, "attr", "")
        return name in ("hecke_h", "h_of_q")
    return False


def _const(node):
    """The numeric value of a literal (or a negated literal), else None."""
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        v = _const(node.operand)
        return None if v is None else -v
    return None


def _strip_neg(node) -> tuple[object, bool]:
    """Peel unary minus signs, returning (inner, negated)."""
    neg = False
    while isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        neg = not neg
        node = node.operand
    return node, neg


def _is_half_of_h(node) -> bool:
    """True for any spelling of +/- h/2 -- the eps = 0 p-n offset.

    Covers `h/2`, `-h/2`, `0.5*h`, `-0.5*h`, `h*0.5`, `(-h)/2`, `-(h/2)`.

    THE UNARY-MINUS CASE IS WHY THIS FUNCTION EXISTS IN THIS FORM. Python
    parses `-h / 2` as `(-h) / 2`, so the numerator is a UnaryOp and not a
    Name. The first version of this scan tested `_is_h_name(node.left)`
    directly and therefore matched `z - h / 2` while silently missing bare
    `-h / 2` -- which is the commoner spelling in this corpus. It reported
    15 sites against a true 23. That is the same detector-blind-spot class
    catalogued in docs/audits/2026-08-15-detector-blindness-taxonomy.md,
    and it was found only by noticing that a file the value scan flagged
    did not appear in the source scan. Cross-check your detectors against
    each other; a single one cannot tell you it has gone blind.
    """
    node, _ = _strip_neg(node)
    if not isinstance(node, ast.BinOp):
        return False
    left, _ = _strip_neg(node.left)
    right, _ = _strip_neg(node.right)
    if isinstance(node.op, ast.Div):
        return _is_h_name(left) and _const(node.right) in (2, -2)
    if isinstance(node.op, ast.Mult):
        lc, rc = _const(node.left), _const(node.right)
        return ((_is_h_name(left) and rc is not None and abs(rc) == 0.5)
                or (_is_h_name(right) and lc is not None and abs(lc) == 0.5))
    return False


def _enclosing_context(tree, lineno: int, lines: list[str]) -> str:
    """Source of the smallest function enclosing `lineno`, else a line window.

    A FIXED LINE WINDOW IS NOT ENOUGH. `wlambda_nuclear_braid_connected_probe`
    computes its p-n crossing in the `else:` branch of an if/elif that names
    `p` and `n` twelve lines above -- and an eight-line comment sits in
    between, pushing every p-n token out of a +/-3 window. The site was
    therefore invisible: not misclassified, not reported at all.

    The comment that hid it is one I added in PR #5769 to LABEL the site.
    Labelling it made it undetectable, which is the third distinct way a
    label has defeated this scanner.

    The enclosing function is the right unit: a crossing table's flavour
    branches are always in the same function as the offset they assign.
    """
    best = None
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            end = node.end_lineno or node.lineno
            if node.lineno <= lineno <= end:
                if best is None or (node.lineno > best.lineno):
                    best = node
    if best is not None:
        return "\n".join(lines[best.lineno - 1: (best.end_lineno or best.lineno)])
    return "\n".join(lines[max(0, lineno - 6): lineno + 5])


class _BlindVisitor(ast.NodeVisitor):
    """Collect `<expr> - h/2` and bare `-h/2` in REAL expressions only.

    Deliberately AST rather than regex: the first version of this scan
    stripped only `#` comments, so every docstring and print() that MENTIONS
    `z - h/2` counted as a live site. That reported 57 BLIND where the true
    live-code count is far smaller -- an over-count is as useless as a
    miss, because nobody drains a list they do not trust.
    """

    def __init__(self):
        self.hits: list[int] = []

    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Sub) and _is_half_of_h(node.right):
            self.hits.append(node.lineno)
        elif _is_half_of_h(node):
            self.hits.append(node.lineno)
        self.generic_visit(node)

    def visit_UnaryOp(self, node):
        if _is_half_of_h(node):
            self.hits.append(node.lineno)
        self.generic_visit(node)


RUST_BLIND = (
    re.compile(r"-\s*\(\s*0?\.5\s*\*\s*h\s*\)"),
    re.compile(r"-\s*0?\.5\s*\*\s*h\b"),
    re.compile(r"PnConvention::StrictAveraged"),
)


def _module_docstring(text: str) -> str:
    """The module docstring only, or "" if there is none.

    DECLARED_BLIND is scoped to this and not to the whole file, because a
    file mentions "colour-blind" for three different reasons and only one of
    them is a declaration:

      - it declares its own delta=0 regime  (bond_extensivity_equal_weight)
      - it says what it FIXED                ("was -h/2, the colour-blind form")
      - it says what the OTHER option is     ("two interfaces, not one: the
                                              colour-blind averaged, and ...")

    A whole-file search cannot tell them apart, and calling the second one a
    declaration marks an already-migrated file as deliberately blind -- which
    is the same defect as accepting "CONVENTION CAVEAT" as a comparison
    marker, made twice in one session.
    """
    try:
        return ast.get_docstring(ast.parse(text)) or ""
    except SyntaxError:
        return ""


def _code_only(text: str) -> str:
    """`text` with comments and docstrings removed.

    COMPARISON is decided on this, not on the raw source. Requiring both
    convention NAMES was meant to stop a label being read as a comparison,
    and it does not: a label that says "`strict_averaged`, NOT the canonical
    `bring_color_weighted`" contains both names, in prose. That is exactly
    the comment I added to `wlambda_nuclear_braid_connected_probe` in PR
    #5769, and it made a genuinely blind site read as deliberate.

    Third time a label has defeated this scanner, each time in a different
    way: as a marker string, as a whole-file phrase match, and now as a
    both-names match. The invariant that keeps holding is that PROSE ABOUT a
    convention is not USE of one -- so decide on code.
    """
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return text
    lines = text.splitlines()
    drop = set()
    for node in ast.walk(tree):
        if (isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant)
                and isinstance(node.value.value, str)):
            for ln in range(node.lineno, (node.end_lineno or node.lineno) + 1):
                drop.add(ln)
    out = []
    for i, line in enumerate(lines, 1):
        if i in drop:
            continue
        out.append(line.split("#", 1)[0])
    return "\n".join(out)


def _classify(text: str) -> tuple[str, str]:
    """Return (verdict, the evidence that produced it).

    An opaque verdict cannot be checked; every row carries the marker that
    decided it so a reader can disagree with the classifier rather than
    with the tool.
    """
    code = _code_only(text)
    has_blind_name = [n for n in BLIND_NAMES if n in code]
    has_canon_name = [n for n in CANON_NAMES if n in code]
    if has_blind_name and has_canon_name:
        return ("COMPARISON",
                f"CODE names both: {has_blind_name[0]} + {has_canon_name[0]}")
    canon_marks = [m for m in CANON_MARKS if m in code]
    if canon_marks:
        return "MIXED", f"canonical machinery present: {canon_marks[0]}"
    declared = DECLARED_BLIND_RE.search(_module_docstring(text))
    if declared:
        return ("DECLARED_BLIND",
                f"the MODULE DOCSTRING declares a colour-blind regime: "
                f"{declared.group(0)!r}")
    return "BLIND", "no canonical machinery, no second convention"


def scan_sources() -> list[dict]:
    out: list[dict] = []
    for path in sorted(ROOT.glob("computations/**/*.py")) + sorted(
            ROOT.glob("tools/**/*.py")) + sorted(ROOT.glob("qou-mass/**/*.py")):
        if _excluded(path):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(text)
        except (OSError, SyntaxError):
            continue
        v = _BlindVisitor()
        v.visit(tree)
        if not v.hits:
            continue
        lines = text.splitlines()
        verdict, why = _classify(text)
        for ln in sorted(set(v.hits)):
            window = _enclosing_context(tree, ln, lines)
            if not PN_CONTEXT.search(window):
                continue
            if SAME_FLAVOUR.search(window) and not re.search(r"\bp[-_]?n\b", window, re.I):
                continue
            # Judged on the SITE's own line, not the window: the u-d and the
            # p-n crossings share an enclosing function.
            if UD_CROSSING.search(lines[ln - 1]):
                continue
            out.append({
                "file": str(path.relative_to(ROOT)),
                "line": ln,
                "verdict": verdict,
                "why": why,
                "lang": "py",
                "generated": GENERATED in "/" + str(path.relative_to(ROOT)),
                "text": lines[ln - 1].strip()[:140],
            })

    for path in sorted(ROOT.glob("tools/**/*.rs")):
        if _excluded(path):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        lines = text.splitlines()
        verdict, why = _classify(text)
        for i, line in enumerate(lines, 1):
            code = line.split("//", 1)[0]
            if not any(s.search(code) for s in RUST_BLIND):
                continue
            window = "\n".join(lines[max(0, i - 4): i + 3])
            if not PN_CONTEXT.search(window):
                continue
            out.append({
                "file": str(path.relative_to(ROOT)),
                "line": i,
                "verdict": verdict,
                "why": why,
                "lang": "rs",
                "generated": False,
                "text": line.strip()[:140],
            })
    return out


# ── witness value scan ───────────────────────────────────────────────────────
def _walk(node, path=""):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from _walk(v, f"{path}.{k}" if path else str(k))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from _walk(v, f"{path}[{i}]")
    else:
        yield path, node


def _producer_is_declared_blind(witness: dict) -> bool:
    """True when the witness's own producer declares a colour-blind regime.

    Keyed on the witness's recorded ``scriptFile`` and the SAME docstring test
    the source scan uses, so the two scans cannot drift apart. A witness whose
    producer is missing, unreadable, or does not declare is left BLIND -- the
    conservative direction, since this function can only ever REMOVE rows from
    the actionable list.
    """
    stem = witness.get("scriptFile")
    if not isinstance(stem, str) or not stem:
        return False
    name = Path(stem).name
    for cand in ROOT.glob(f"computations/**/{name}"):
        try:
            text = cand.read_text(encoding="utf-8")
        except OSError:
            continue
        if DECLARED_BLIND_RE.search(_module_docstring(text)):
            return True
    return False


def scan_witnesses() -> list[dict]:
    out: list[dict] = []
    for path in sorted(ROOT.glob("computations/**/*.witness.json")):
        if _excluded(path):
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        blind_at, canon_at, labels = [], [], []
        for key, val in _walk(data):
            if isinstance(val, bool) or val is None:
                continue
            if isinstance(val, (int, float)):
                s = repr(float(val))
            elif isinstance(val, str):
                s = val
                lv = val.lower()
                if lv in ("strict_averaged", "bring_color_weighted"):
                    labels.append((key, val))
            else:
                continue
            if BLIND_KEY in s:
                blind_at.append(key)
            if CANON_KEY in s:
                canon_at.append(key)
        if not (blind_at or canon_at or labels):
            continue
        if blind_at and canon_at:
            verdict = "BOTH"          # deliberate comparison -- NEVER drain
        elif blind_at:
            verdict = "BLIND"
            # A witness INHERITS its producer's declared regime. The source scan
            # already carves out DECLARED_BLIND (a module docstring saying
            # 'equal-weight' / 'colour-blind'), but until now the witness scan
            # did not, so the OUTPUT of a deliberately colour-blind producer was
            # reported as an actionable BLIND witness -- an owner-scoped flip
            # decision made against an inflated count. Measured: 1 of 7
            # (bond-extensivity-equal-weight, whose producer
            # bond_extensivity_equal_weight.py:77 the source scan already lists
            # as DECLARED_BLIND).
            if _producer_is_declared_blind(data):
                verdict = "DECLARED_BLIND"
        elif canon_at:
            verdict = "CANONICAL"
        else:
            verdict = "LABEL_ONLY"
        out.append({
            "file": str(path.relative_to(ROOT)),
            "verdict": verdict,
            "blind_fields": blind_at[:6],
            "canon_fields": canon_at[:6],
            "labels": [f"{k}={v}" for k, v in labels][:6],
        })
    return out


# ── selftest ─────────────────────────────────────────────────────────────────
def selftest() -> int:
    """Fail unless the reference values reproduce AND the shapes still fire.

    A detector with no selftest reports a clean tree when it has gone blind;
    this repo has that happen four separate times (see the taxonomy audit).
    """
    ok = True

    sys.path.insert(0, str(ROOT / "computations"))
    sys.path.insert(0, str(ROOT / "computations" / "substrate"))
    try:
        from mpmath import mp  # noqa: E402
        mp.dps = 50
        from q_parameter import Q_50_DIGIT_STR  # noqa: E402
        from closed_form_tau_M import markov_z, hecke_h  # noqa: E402
        from _li_2_q_util import flavor_split_leading  # noqa: E402
        q = mp.mpf(Q_50_DIGIT_STR)
        z, h, d = markov_z(q), hecke_h(q), flavor_split_leading(q)
        blind = z - h / 2
        canon = z - h * (mp.mpf(1) / 2 - d / 4)
        for name, got, want in (("blind", blind, BLIND_STR),
                                ("canon", canon, CANON_STR)):
            gs = mp.nstr(got, 30)
            if gs[:14] != want[:14]:
                print(f"  FAIL {name}: producers give {gs}, constant says {want}")
                ok = False
            else:
                print(f"  ok   {name} reproduces: {gs}")
    except ImportError as exc:
        print(f"  SKIP value check: {exc} (mpmath / producers unavailable)")

    # Shape battery. Each must fire, or the scan has gone blind -- the
    # failure mode this repo has hit four separate times (see the
    # detector-blindness taxonomy). Both halves are covered: the Python AST
    # path and the Rust regex path.
    py_probes = [
        ('FAC = {"pp": Z, "nn": Z - H, "pn": Z - H / 2}', True),
        ("f_pn = z - h/2", True),
        ("f_pn = z - 0.5 * h", True),
        ("f_pn = z - h * 0.5", True),
        ("f_pn = z - hecke_h(q) / 2", True),
        # The unary-minus family. `-h / 2` parses as `(-h) / 2`; the first
        # version of this scan missed every one of these and under-reported
        # the surface by a third.
        ('pn = (mp.mpf(1), -h / 2)', True),
        ('pn = (1.0, -H / 2)', True),
        ("d = -0.5 * h", True),
        ("d = -(h / 2)", True),
        ("blocks = interface_blocks(lam, 9, 3, q_str, -h / 2, 50)", True),
        ("f_pn = z - h * (1/2 - delta/4)", False),   # canonical
        ("f_nn = z - h", False),                      # a different bond
        ("half = x / 2", False),                      # not h
        ("third = h / 3", False),                     # not a half
    ]
    for text, want in py_probes:
        tree = ast.parse(text)
        v = _BlindVisitor()
        v.visit(tree)
        got = bool(v.hits)
        if got != want:
            print(f"  FAIL py shape: {text!r} fired={got} expected={want}")
            ok = False
    else:
        if ok:
            print(f"  ok   {len(py_probes)} python AST probes")

    rs_probes = [
        ("PnConvention::StrictAveraged => -(0.5 * h),", True),
        ("let f = z - (0.5 * h);", True),
        ("PnConvention::BringColorWeighted => ...", False),
    ]
    for text, want in rs_probes:
        got = any(s.search(text.split("//", 1)[0]) for s in RUST_BLIND)
        if got != want:
            print(f"  FAIL rs shape: {text!r} fired={got} expected={want}")
            ok = False
    if ok:
        print(f"  ok   {len(rs_probes)} rust regex probes")

    print("SELFTEST", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", action="store_true")
    ap.add_argument("--witness", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    both = not (args.source or args.witness)
    src = scan_sources() if (both or args.source) else []
    wit = scan_witnesses() if (both or args.witness) else []

    if args.json:
        print(json.dumps({"source": src, "witness": wit}, indent=2))
        return 0

    if both or args.source:
        print(f"SOURCE SITES ({len(src)})")
        for v in ("BLIND", "DECLARED_BLIND", "MIXED", "COMPARISON"):
            rows = [r for r in src if r["verdict"] == v]
            note = ("  <- deliberate delta=0 regime, NOT actionable"
                    if v == "DECLARED_BLIND" else "")
            print(f"  {v}: {len(rows)}{note}")
            for r in rows:
                gen = "  [GENERATED - sync, do not hand-edit]" if r["generated"] else ""
                print(f"    {r['file']}:{r['line']}{gen}")
                print(f"        {r['text']}")
                print(f"        why: {r['why']}")
        print()

    if both or args.witness:
        print(f"WITNESSES CARRYING A p-n FACTOR VALUE ({len(wit)})")
        for v in ("BLIND", "DECLARED_BLIND", "CANONICAL", "BOTH", "LABEL_ONLY"):
            rows = [r for r in wit if r["verdict"] == v]
            note = ("  <- deliberate comparison, NEVER drain" if v == "BOTH"
                    else "  <- producer declares colour-blind, NOT actionable"
                    if v == "DECLARED_BLIND" else "")
            print(f"  {v}: {len(rows)}{note}")
            for r in rows:
                print(f"    {r['file']}")
                for f in r["blind_fields"]:
                    print(f"        blind @ {f}")
                for f in r["canon_fields"]:
                    print(f"        canon @ {f}")
                for l in r["labels"]:
                    print(f"        label   {l}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
