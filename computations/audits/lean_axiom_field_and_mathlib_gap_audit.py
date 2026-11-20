#!/usr/bin/env python3
"""Axiom-field audit: which Prop-carrying `class`/`structure` carriers have an inhabitant.

WHY THIS EXISTS
---------------
Epic `qou-dxbw` and its eight child features quote counts (1803 carriers, 1336
"uninstantiated", per-carrier "Top Priority" tables) from a script at this path
and a witness beside it. Neither was ever committed (GAP bean `qou-dx7g`,
measured 2026-11-20). This is a rewrite rather than a recovery: the definitions
below are stated explicitly so a reviewer can check them, and the numbers it
prints are NOT expected to match the epic's.

DEFINITIONS (all syntactic; this is a text scanner, not Lean elaboration)
-------------------------------------------------------------------------
* **carrier** — a `class` or `structure` declaration in a tracked `.lean` file
  under `folio/` that has at least one **Prop field**. A field is Prop if the
  carrier is declared `: Prop`, or the field's type contains a propositional
  connective or relation (`=`, `≠`, `≤`, `<`, `≥`, `>`, `↔`, `∀`, `∃`, `∧`, `∨`,
  `¬`, `∈`, `⊆`, `Prop`) at the top of its text. Pure-data structures are not
  carriers.
* **inhabited** — some declaration ANYWHERE in the scanned tree (not only in the
  carrier's own file) is an `instance`, `def`, `abbrev`, `noncomputable def`,
  `example` or `theorem` whose RESULT TYPE head is the carrier's name (short or
  qualified). The result type is the text after the last depth-0 `:` of the
  declaration header (the header ends at `:=` or a trailing `where`).
  A result type `Nonempty (X ...)` also counts: such a declaration is proved
  by exhibiting a term. Universe annotations (`X.{0, 0}`) are stripped.
* **toy-only** — inhabited, but every inhabiting header names `Unit`, `PUnit`,
  `Fin 1`, `Empty` or `PEmpty` as an argument.
* **consumer** — a declaration header (in any file) that mentions the carrier
  name as a binder: `[X`, `[_ : X`, `(h : X`, `{h : X`.

KNOWN LIMITS (do not read the counts past these)
------------------------------------------------
* No elaboration: an inhabitant built by a tactic proof of `Nonempty X`, or an
  instance found by unification through `extends`, is invisible. So
  "uninhabited" is an UPPER bound and "inhabited" is a lower bound.
* Short-name matching: two carriers with the same last component in different
  namespaces share evidence. Collisions are counted and reported.
* No satisfiability judgement: a parameter bundle such as
  `UGB...HeckeParams` (`q : ℝ`, `0 < q`, `q ≠ 1`) is trivially inhabitable at
  `q = 2` yet reads "uninhabited" because no closed term is written down. Such
  bundles are hypotheses, not axiom-fields, and they dominate the top of the
  consumer ranking. Separating them needs a per-carrier agent verdict.
* `--selftest` asserts four calibration verdicts that were checked by hand and
  FAILS if any of them comes out wrong. An audit whose calibration cannot fail
  cannot find its own blind spot (detector-blindness taxonomy, row 45).

Usage:
    python3 computations/audits/lean_axiom_field_and_mathlib_gap_audit.py [--json OUT] [--top N] [--selftest]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                      text=True, cwd=os.path.dirname(os.path.abspath(__file__))).stdout.strip()

PROP_MARK = re.compile(r"(=|≠|≤|<|≥|>|↔|∀|∃|∧|∨|¬|∈|⊆|\bProp\b|\bTrue\b|\bFalse\b)")
DECL_KW = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+|scoped\s+)*"
    r"(class|structure|instance|def|abbrev|theorem|lemma|example)\b(.*)$")
NS_OPEN = re.compile(r"^\s*namespace\s+([\w.'’]+)")
NS_END = re.compile(r"^\s*end\s+([\w.'’]+)\s*$")
TOY = re.compile(r"\b(PUnit|Unit|PEmpty|Empty)\b|\bFin\s+1\b")
IDENT = re.compile(r"[A-Za-z_Ͱ-Ͽᴀ-ᶿ][\w.'’Ͱ-Ͽ₀-₉]*")

# hand-checked calibration verdicts (2026-11-20, main 3411686c48e + this file)
CALIBRATION = {
    # QDimension is NOT here on purpose: its one field `dq` is data, so it is not a
    # carrier at all -- the epic's "TOY_ONLY, 11 consumers" row counted a data class.
    "QOU.MathlibExt.QPlancherel.HasPartitionFunction": "inhabited",  # partitionPartitionFunction
    "QOU.Archimedean.UpstreamAdditions.Cl_2_DoubleAngle": "inhabited",  # instCl_2_DoubleAngle
    "QOU.MathlibExt.QPlancherel.HasQPlancherelCLT": "uninhabited",  # no instance anywhere
    "QOU.BraidKnot.YoungTableauStandard.SkewStandardYoungTableau": "inhabited",  # SkewSYTBranchingBijection
    # the two blind spots the 2026-11-20 top-80 triage found:
    "QOU.AppendixSurreals.SurrealField": "inhabited",   # def ... : SurrealField.{0, 0} R*
    "QOU.Torsion.VacuumState": "inhabited",             # vacuum_state_exists : Nonempty ...
}


def lean_files() -> list[str]:
    out = subprocess.run(["git", "ls-files", "--full-name", "folio"], capture_output=True,
                         text=True, cwd=ROOT).stdout.split()
    files = [os.path.join(ROOT, p) for p in out if p.endswith(".lean") and "/.lake/" not in p]
    if not files:
        sys.exit("no tracked .lean files found -- refusing to report an empty corpus as clean")
    return files


def strip_comments(text: str) -> str:
    text = re.sub(r"/-.*?-/", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    return re.sub(r"--[^\n]*", "", text)


def header_of(lines: list[str], i: int) -> str:
    """Declaration header from line i: up to `:=` or a trailing `where` (max 40 lines)."""
    buf = []
    for j in range(i, min(i + 40, len(lines))):
        ln = lines[j]
        if ":=" in ln:
            buf.append(ln.split(":=", 1)[0])
            break
        if re.search(r"\bwhere\s*$", ln):
            buf.append(re.sub(r"\bwhere\s*$", "", ln))
            break
        buf.append(ln)
        if j > i and DECL_KW.match(lines[j + 1] if j + 1 < len(lines) else ""):
            break
    return " ".join(buf)


def result_type(header: str) -> str:
    depth, last = 0, -1
    for k, ch in enumerate(header):
        if ch in "([{⟨":
            depth += 1
        elif ch in ")]}⟩":
            depth -= 1
        elif ch == ":" and depth == 0 and header[k + 1:k + 2] != "=":
            last = k
    return header[last + 1:].strip() if last >= 0 else ""


def scan():
    carriers: dict[str, dict] = {}
    evidence: dict[str, list] = defaultdict(list)     # short name -> inhabiting headers
    consumer_hits: Counter = Counter()
    standalone = Counter()
    headers_all = []
    for path in lean_files():
        rel = os.path.relpath(path, ROOT)
        try:
            raw = open(path, encoding="utf-8").read()
        except OSError:
            continue
        lines = strip_comments(raw).split("\n")
        ns: list[str] = []
        for i, ln in enumerate(lines):
            if m := NS_OPEN.match(ln):
                ns.extend(m.group(1).split("."))
                continue
            if m := NS_END.match(ln):
                parts = m.group(1).split(".")
                if ns[-len(parts):] == parts:
                    del ns[-len(parts):]
                continue
            if re.match(r"^\s*axiom\b", ln):
                standalone["axiom"] += 1
            if re.match(r"^\s*(?:noncomputable\s+)?opaque\b", ln):
                standalone["opaque"] += 1
            if re.search(r"\bsorry\b", ln):
                standalone["sorry"] += 1
            m = DECL_KW.match(ln)
            if not m:
                continue
            kw, rest = m.group(1), m.group(2)
            hdr = header_of(lines, i)
            headers_all.append((rel, i + 1, hdr))
            if kw in ("class", "structure"):
                nm = IDENT.match(rest.strip())
                if not nm:
                    continue
                short = nm.group(0)
                full = ".".join(ns + [short])
                is_prop_carrier = bool(re.search(r":\s*Prop\b", hdr))
                fields, n_prop = [], 0
                for j in range(i + 1, min(i + 200, len(lines))):
                    fl = lines[j]
                    if DECL_KW.match(fl) or NS_END.match(fl) or NS_OPEN.match(fl):
                        break
                    fm = re.match(r"^\s{2,}([\w'’₀-₉]+)\s*(?:\{[^}]*\}|\([^)]*\)|\[[^\]]*\]|\s)*:\s*(.*)$", fl)
                    if fm and fm.group(1) not in ("extends", "mk"):
                        is_p = is_prop_carrier or bool(PROP_MARK.search(fm.group(2)))
                        fields.append(fm.group(1))
                        n_prop += is_p
                if n_prop == 0:
                    continue
                carriers[full] = {"name": full, "short": short, "kind": kw, "file": rel,
                                  "line": i + 1, "prop_fields": n_prop, "fields": len(fields)}
            elif kw in ("instance", "def", "abbrev", "theorem", "lemma", "example"):
                rt = result_type(hdr)
                # `Nonempty (X ...)` proved by construction is inhabitation evidence
                # (blind spot 2, found by the 2026-11-20 top-80 triage).
                nm2 = re.match(r"Nonempty\s*\(?\s*", rt)
                if nm2:
                    rt = rt[nm2.end():]
                hm = IDENT.match(rt)
                if hm:
                    # strip a trailing `.` left by a universe annotation such as
                    # `SurrealField.{0, 0}` (blind spot 1).
                    head = hm.group(0).rstrip(".")
                    evidence[head.split(".")[-1]].append(
                        {"file": rel, "line": i + 1, "toy": bool(TOY.search(rt)), "head": head})
    for rel, line, hdr in headers_all:
        for nm in set(re.findall(r"[\[(\{]\s*(?:[\w'’]+\s*:\s*)?([A-Za-z_][\w.'’]*)", hdr)):
            consumer_hits[nm.split(".")[-1]] += 1
    shorts = Counter(c["short"] for c in carriers.values())
    for c in carriers.values():
        ev = [e for e in evidence.get(c["short"], [])
              if e["head"] == c["short"] or c["name"].endswith(e["head"])]
        c["collision"] = shorts[c["short"]] > 1
        c["consumers"] = consumer_hits.get(c["short"], 0)
        if not ev:
            c["status"] = "uninhabited"
        elif all(e["toy"] for e in ev):
            c["status"] = "toy_only"
        else:
            c["status"] = "inhabited"
        c["evidence"] = [f'{e["file"]}:{e["line"]}' for e in ev[:3]]
    return carriers, standalone


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    carriers, standalone = scan()
    st = Counter(c["status"] for c in carriers.values())
    print(f"carriers (class/structure with >=1 Prop field): {len(carriers)}")
    for k in ("uninhabited", "toy_only", "inhabited"):
        print(f"  {k:12s} {st[k]}")
    print(f"  short-name collisions: {sum(c['collision'] for c in carriers.values())}")
    print(f"standalone: axiom {standalone['axiom']}, opaque {standalone['opaque']}, "
          f"lines with sorry {standalone['sorry']}")
    ranked = sorted((c for c in carriers.values() if c["status"] != "inhabited"),
                    key=lambda c: (-c["consumers"], c["name"]))
    print(f"\ntop {a.top} uninhabited/toy carriers by consumer count:")
    for c in ranked[:a.top]:
        print(f'  {c["consumers"]:4d}  {c["status"]:11s} {c["name"]}  ({c["file"]}:{c["line"]})')
    fails = []
    for name, want in CALIBRATION.items():
        got = carriers.get(name, {}).get("status", "MISSING")
        ok = got == want
        print(f'calibration {"PASS" if ok else "FAIL"}: {name}: want {want}, got {got}')
        if not ok:
            fails.append(name)
    if a.json:
        head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True,
                              cwd=ROOT).stdout.strip()
        with open(a.json, "w", encoding="utf-8") as fh:
            json.dump({"description": "Axiom-field audit (qou-dx7g); syntactic, see script docstring",
                       "commitSha": head, "counts": dict(st), "carriers_total": len(carriers),
                       "standalone": dict(standalone), "calibration_failures": fails,
                       "carriers": sorted(carriers.values(), key=lambda c: c["name"])},
                      fh, ensure_ascii=False, indent=1)
    if a.selftest and fails:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
