#!/usr/bin/env python3
"""Shared source normalisation: strip what DESCRIBES code from what IS code.

WHY THIS EXISTS
    A scanner that matches raw file text convicts the files that are most
    careful, because this corpus documents q₀, CODATA literals and anchor
    conventions *precisely where the code avoids them*. Measured instances
    (bean `qou-5li4`):

      * `hardcoded_literal_audit` files `canonical_tower.py`'s note reading
        "this module does NOT use the β-decay Q-value 0.78233341 MeV as E_0"
        as an `i9_violation` of that exact value, `rel_err: 0.0`.
      * `q0_consistency_audit` convicts pin RECOGNIZERS and an anti-straddle
        GUARD — text that identifies or defends a pin, read as text that
        hardcodes one.
      * `q0_muon_population_partition` EXEMPTS a direct pinner because its
        docstring says it computes at muon *regardless of* `q_parameter`.
        The sentence denying the routing is read as proof of it.

    Before this module the corpus carried FOUR independent correct
    implementations of the same blanking pass — in `float64_leak_audit`,
    `q0_hardcoded_pin_audit`, `scripts/real-sorry-scan.py`, and
    `q0_independence_checker` — and shared none of them. Every other scanner
    re-derived it privately or failed to.

WHAT THIS IS NOT
    **Raw-text matching is not itself the defect**, and reaching for this
    module is not always the right fix. Measured counter-example:
    `convention_frame_staleness_audit` reads raw text with no AST pass and is
    *clean* — 212 raw matches, 212 code-only, zero prose-only — because its
    pattern is `^`-anchored and assignment-shaped, which a `#` comment cannot
    satisfy.

    So: a BARE-TOKEN pattern (a literal, a module name, a symbol) matches
    anywhere and needs `code_only`. An ASSIGNMENT-SHAPED, anchored pattern is
    already immune, and re-shaping the pattern is cheaper than normalising the
    input. Choose deliberately.

LINE AND COLUMN ARE PRESERVED, WHICH IS THE POINT
    `hardcoded_literal_audit` strips docstrings with
    `re.sub(r'\"\"\".*?\"\"\"', "", text, flags=DOTALL)`, which DELETES the
    newlines. Every line number after the first docstring is then wrong — its
    witness reports 476 for a string at 647, off by 171. Blanking in place
    keeps every offset intact, so a reported line still points at the code.
"""
from __future__ import annotations

import ast
import io
import re
import tokenize
from typing import Iterable, Optional

__all__ = [
    "code_only",
    "code_and_numeric_strings_only",
    "identifiers_only",
    "blank_declaration_prose",
    "blank_message_strings",
    "code_only_ast",
]

_NUM_STR_RX = re.compile(r"^[+-]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][+-]?\d+)?$")
_FSTRING_MIDDLE = getattr(tokenize, "FSTRING_MIDDLE", None)

#: Calls whose string argument DOES the thing rather than describes it. A
#: filename inside `open(...)`/`witness_path(...)` is a real read; the same
#: filename inside `raise SystemExit(f"...")` is a warning about one. This
#: carve-out is the load-bearing half of `blank_message_strings` — without it
#: the pass blanks genuine reads. Contributed from PR #5810, which measured the
#: failure it prevents: `qbeta_habiro_residual_probe` raises a guard naming
#: `q-pinning-50-digit.witness.json`, and a classifier read that guard's own
#: warning as evidence the producer reads the muon pin.
OPERATIVE_CALLS = frozenset({
    "open", "Path", "read_text", "read_bytes", "mpf", "mpmath", "Decimal",
    "load", "loads", "witness_path", "joinpath", "with_suffix", "glob",
})

#: Calls whose string arguments are MESSAGES — prose aimed at a human.
MESSAGE_CALLS = frozenset({
    "print", "warn", "warning", "log", "info", "debug", "error", "critical",
    "SystemExit", "RuntimeError", "ValueError", "AssertionError", "format",
})


def code_only(src: str) -> str:
    """`src` with comments and docstring-style strings blanked, offsets intact.

    Blanks COMMENT tokens and triple-quoted STRING tokens by overwriting their
    characters with spaces, leaving newlines alone. The result has the same
    length, the same line count, and the same column positions as the input, so
    a match's `lineno` is still true of the original file.

    Ordinary single-quoted strings are DELIBERATELY left intact: they carry
    real values a scanner often needs to see (an f-string with a precision
    literal, a path, a declared constant). Use `blank_declaration_prose` when
    the prose you must exclude lives in a string VALUE.

    An unparseable file is returned unchanged — the caller keeps whatever
    behaviour it had rather than silently seeing an empty file.
    """
    out = list(src)
    lines = src.splitlines(keepends=True)
    starts = [0] * (len(lines) + 1)
    for i, ln in enumerate(lines):
        starts[i + 1] = starts[i] + len(ln)

    def offset(row: int, col: int) -> int:
        if row - 1 >= len(starts):
            return len(out)
        return min(starts[row - 1] + col, len(out))

    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            is_comment = tok.type == tokenize.COMMENT
            is_docstr = (tok.type == tokenize.STRING
                         and tok.string.lstrip("rRbBuUfF")[:3] in ('"""', "'''"))
            if not (is_comment or is_docstr):
                continue
            beg, end = offset(*tok.start), offset(*tok.end)
            for i in range(beg, end):
                if out[i] != "\n":
                    out[i] = " "
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return src
    return "".join(out)


def code_and_numeric_strings_only(src: str) -> str:
    """`code_only(src)` with non-numeric prose strings blanked in place.

    Preserves exact byte length, line count, and column offsets. Single- or
    double-quoted string literals whose stripped interior is a pure numeric
    constant (e.g. `mp.mpf("0.78233341")` or `Q_STR = "1.109978582751"`)
    survive intact; English sentences and format-string prose (e.g.
    `"this module does NOT use the β-decay Q-value 0.78233341 MeV as E_0"` or
    `f"with e^2 = 1.43996 MeV.fm: {x}"`) are overwritten with spaces.
    """
    s = code_only(src)
    out = list(s)
    lines = s.splitlines(keepends=True)
    starts = [0] * (len(lines) + 1)
    for i, ln in enumerate(lines):
        starts[i + 1] = starts[i] + len(ln)

    def offset(row: int, col: int) -> int:
        if row - 1 >= len(starts):
            return len(out)
        return min(starts[row - 1] + col, len(out))

    try:
        for tok in tokenize.generate_tokens(io.StringIO(s).readline):
            if tok.type == tokenize.STRING:
                inner = tok.string.lstrip("rRbBuUfF")
                if len(inner) >= 2 and inner[0] in ('"', "'") and inner[-1] == inner[0]:
                    if _NUM_STR_RX.match(inner[1:-1].strip()):
                        continue
            elif _FSTRING_MIDDLE is not None and tok.type == _FSTRING_MIDDLE:
                if _NUM_STR_RX.match(tok.string.strip()):
                    continue
            else:
                continue
            beg, end = offset(*tok.start), offset(*tok.end)
            for i in range(beg, end):
                if out[i] != "\n":
                    out[i] = " "
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return s
    return "".join(out)


def identifiers_only(src: str) -> str:
    """`src` with ALL comments and string literals blanked, offsets intact.

    Use when scanning for Python identifiers (`M_P_MEV`, `Q_beta`, `Vol_hyp`)
    that must never match inside a comment, docstring, or string literal.
    """
    out = list(src)
    lines = src.splitlines(keepends=True)
    starts = [0] * (len(lines) + 1)
    for i, ln in enumerate(lines):
        starts[i + 1] = starts[i] + len(ln)

    def offset(row: int, col: int) -> int:
        if row - 1 >= len(starts):
            return len(out)
        return min(starts[row - 1] + col, len(out))

    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            is_str_or_comment = (
                tok.type in (tokenize.COMMENT, tokenize.STRING)
                or (_FSTRING_MIDDLE is not None and tok.type == _FSTRING_MIDDLE)
            )
            if not is_str_or_comment:
                continue
            beg, end = offset(*tok.start), offset(*tok.end)
            for i in range(beg, end):
                if out[i] != "\n":
                    out[i] = " "
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return code_only(src)
    return "".join(out)


def blank_declaration_prose(
    tree: ast.AST, keys: Iterable[str] = ("q0Anchor", "q0AnchorReason", "q0Values"),
) -> ast.AST:
    """Empty string values held under `keys` so a REASON cannot indict its claim.

    `q0AnchorReason` is where an author explains why a compute is
    q₀-independent, so it naturally quotes the pin it does not use. Since
    `ast.unparse` preserves string constants, that explanation matched as
    evidence against itself: three of the first four violations inspected in
    `q0_independence_checker` were nothing but their own reason string.

    Mutates and returns `tree`.

    Do NOT pass a key whose value a caller reads back out of the same
    normalised source — blanking `Q0_ROLE` this way silently disabled an
    auditor carve-out (exempt 3 → 0) because the marker was matched against the
    blanked text.
    """
    wanted = set(keys)
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        for k, v in zip(node.keys, node.values):
            if (isinstance(k, ast.Constant) and k.value in wanted
                    and isinstance(v, ast.Constant)
                    and isinstance(v.value, str)):
                v.value = ""
    return tree


def blank_message_strings(tree: ast.AST) -> ast.AST:
    """Empty MESSAGE strings — f-strings, `raise`, `print`/`warn`/`log` args.

    `code_only` deliberately leaves single-quoted strings intact because they
    carry declared values (`VAR = "1.1099785827..."`). That correctly keeps real
    data visible and incorrectly keeps *messages* visible, and a message naming
    a thing is the canonical shape of this whole defect class:

        raise SystemExit(f"ANCHOR STRADDLE in q-pinning-50-digit.witness.json: ...")

    A guard that exists to PREVENT reading the muon pin, read as evidence that
    it does. Blanking it is safe only because of `OPERATIVE_CALLS`: a string
    that is an argument to `open`/`witness_path`/`mpf`/`json.load` is preserved
    even inside a message context, because those calls act on it.

    Mutates and returns `tree`. Compose with `blank_declaration_prose`, which is
    orthogonal — that one keys on dict KEYS, this one on call CONTEXT.
    """
    protected: set[int] = set()

    def _call_name(node: ast.Call) -> str:
        f = node.func
        return getattr(f, "attr", None) or getattr(f, "id", None) or ""

    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and _call_name(node) in OPERATIVE_CALLS:
            for a in list(node.args) + [k.value for k in node.keywords]:
                for sub in ast.walk(a):
                    if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
                        protected.add(id(sub))

    def _blank_within(node: ast.AST) -> None:
        for sub in ast.walk(node):
            if (isinstance(sub, ast.Constant) and isinstance(sub.value, str)
                    and id(sub) not in protected):
                sub.value = ""

    for node in ast.walk(tree):
        if isinstance(node, ast.JoinedStr):
            _blank_within(node)
        elif isinstance(node, ast.Raise):
            _blank_within(node)
        elif isinstance(node, ast.Call) and _call_name(node) in MESSAGE_CALLS:
            for a in list(node.args) + [k.value for k in node.keywords]:
                _blank_within(a)
    return tree


def code_only_ast(src: str, *, strip_docstrings: bool = True,
                  blank_keys: Optional[Iterable[str]] = None,
                  blank_messages: bool = False) -> Optional[str]:
    """AST round-trip: docstrings dropped, declaration prose optionally blanked.

    Returns `None` when `src` will not parse, so a caller can distinguish
    "no match" from "could not look" rather than treating both as clean.

    NOTE this does NOT preserve line numbers — `ast.unparse` reformats. Use it
    for presence questions ("does this module read q₀?"), and `code_only` when
    a reported position must stay true of the file.
    """
    try:
        tree = ast.parse(src)
    except (SyntaxError, ValueError):
        return None
    if strip_docstrings:
        for node in ast.walk(tree):
            if isinstance(node, (ast.Module, ast.FunctionDef,
                                 ast.AsyncFunctionDef, ast.ClassDef)):
                body = getattr(node, "body", None)
                if (body and isinstance(body[0], ast.Expr)
                        and isinstance(body[0].value, ast.Constant)
                        and isinstance(body[0].value.value, str)):
                    body.pop(0)
    if blank_keys is not None:
        blank_declaration_prose(tree, blank_keys)
    if blank_messages:
        blank_message_strings(tree)
    return ast.unparse(tree)


def _selftest() -> int:
    """Fail loudly if a future narrowing breaks the properties that matter."""
    src = (
        '"""Module doc mentioning 0.78233341 and q-pinning-50-digit."""\n'
        "import os  # trailing comment with 1.10997859555733471\n"
        "\n"
        "# a full-line comment naming Q_50_DIGIT_STR\n"
        "REAL = 0.78233341\n"
        'W = {"q0Anchor": "independent",\n'
        '     "q0AnchorReason": "reads no q-pinning-50-digit anchor"}\n'
        'KEEP = "0.51099895069"\n'
    )
    out = code_only(src)
    fails = []
    if len(out) != len(src):
        fails.append("length changed — offsets no longer valid")
    if out.count("\n") != src.count("\n"):
        fails.append("newline count changed — LINE NUMBERS CORRUPTED")
    for line_no, needle, want in [
        (1, "0.78233341", False),   # module docstring
        (2, "1.10997859", False),   # trailing comment
        (4, "Q_50_DIGIT_STR", False),  # full-line comment
        (5, "0.78233341", True),    # real assignment survives
        (8, "0.51099895069", True),  # single-quoted value survives
    ]:
        got = needle in out.splitlines()[line_no - 1]
        if got != want:
            fails.append(f"line {line_no}: {needle!r} present={got}, want={want}")
    # the declaration's own reason must not indict it
    kept = code_only_ast(src, blank_keys=("q0Anchor", "q0AnchorReason"))
    if kept is None or "q-pinning-50-digit" in kept:
        fails.append("blank_declaration_prose left the reason string matchable")
    if code_only_ast("def broken(:\n") is not None:
        fails.append("unparseable source did not return None")
    if code_only("def broken(:\n") != "def broken(:\n":
        fails.append("code_only did not pass through unparseable source")

    # message-string blanking, with the operative-call carve-out that makes it
    # safe. Both halves are checked: the guard must vanish, the read must not.
    msg_src = (
        'import json\n'
        'from _pb import witness_path\n'
        'def f(p):\n'
        '    q = json.load(open("q-pinning-50-digit.witness.json"))\n'
        '    w = witness_path("q-pinning-50-digit.witness.json")\n'
        '    if bad:\n'
        '        raise SystemExit(f"ANCHOR STRADDLE in q-pinning-50-digit.witness.json")\n'
        '    print("reading q-pinning-50-digit.witness.json now")\n'
    )
    got = code_only_ast(msg_src, blank_messages=True)
    if got is None:
        fails.append("message selftest source did not parse")
    else:
        if got.count("q-pinning-50-digit") != 2:
            fails.append(
                "operative-call carve-out wrong: expected exactly the 2 real "
                f"reads to survive, saw {got.count('q-pinning-50-digit')}")
        if "ANCHOR STRADDLE" in got:
            fails.append("raise-guard message was not blanked")
        if "reading q-pinning" in got:
            fails.append("print message was not blanked")

    prose_lit_src = (
        'note = "this module does NOT use the β-decay Q-value 0.78233341 MeV as E_0"\n'
        'val = mp.mpf("0.78233341")\n'
        'msg = f"with e^2 = 1.43996 MeV.fm: {mp.mpf(\'137.0359991\')}"\n'
    )
    cn = code_and_numeric_strings_only(prose_lit_src)
    if len(cn) != len(prose_lit_src) or cn.count("\n") != prose_lit_src.count("\n"):
        fails.append("code_and_numeric_strings_only corrupted length or newlines")
    cn_lines = cn.splitlines()
    if "0.78233341" in cn_lines[0]:
        fails.append("code_and_numeric_strings_only left prose denial literal matchable")
    if "0.78233341" not in cn_lines[1]:
        fails.append("code_and_numeric_strings_only blanked real mpf numeric string")
    if "1.43996" in cn_lines[2] or "137.0359991" not in cn_lines[2]:
        fails.append("code_and_numeric_strings_only f-string split failed")

    id_only = identifiers_only('s = "Q_beta is not used"\nx = Q_beta\n')
    id_lines = id_only.splitlines()
    if "Q_beta" in id_lines[0] or "Q_beta" not in id_lines[1]:
        fails.append("identifiers_only failed to separate string from identifier")
    for f in fails:
        print(f"  FAIL {f}")
    print("selftest:", "PASS" if not fails else f"{len(fails)} FAILURE(S)")
    return 1 if fails else 0


if __name__ == "__main__":
    import sys
    sys.exit(_selftest())
