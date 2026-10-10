#!/usr/bin/env python3
"""
stale_audit_discriminator.py — turn the qou-5pgl CANDIDATE list into VERDICTS.

The confirmed defect (bean qou-5pgl; and the CORRECTED 2026-09-05 block in
docs/audits/2026-08-08-borromean-trace-convention-forcing.md):

    c1a3299434  2026-08-16  "markov_peel: the docstring said convention C;
                             the live path is D"

Every number measured through markov_peel.word_to_element BEFORE that date is a
convention-C measurement wearing no C label.  z_C = sqrt(q)/(q+1) ~ 0.4993203342
at the proton q0; z_D = q^3/(q^2+1) ~ 0.6126880371.  Owner ruled D canonical
2026-08-15.

METHOD.  A stale doc usually NAMES the probe or producer that produced its
figures; that script is usually still on disk and still runnable.  Re-run it,
diff its stdout decimals against the doc's quoted decimals, and the question is
decided mechanically.  That is how the one confirmed instance was caught.

NO-FLOAT64 (AGENTS.md, STRICT — probes are NOT exempt).  No float arithmetic
anywhere in this file.  Decimal literals from docs and from producer stdout are
kept as STRINGS and compared by significant-digit prefix; where a numeric value
is genuinely needed it is an exact fractions.Fraction.  The builtin float
coercion appears in no executable line.

(This sentence deliberately avoids naming that builtin with its parenthesis.
The first draft asserted its own absence in a form that a grep for the
coercion matched, so the file refuted its own claim to any checker cheap
enough to run -- and the same slip was made independently in
computations/probes/atom_intra_block_is_not_a_braid_probe.py the same hour.
Detector-blindness taxonomy: docs/audits/2026-08-15-detector-blindness-taxonomy.md.)

RE-RUN SAFETY — every guard here was bought by a failure, do not remove them:
  * ONE script per doc (the "primary"), never every script a doc mentions.  An
    audit doc that tabulates 49 producers is not citing 49 sources for its
    figures, and running them all is what fills the disk.
  * A free-disk floor checked BEFORE each run.  A single producer run in this
    container took free space from 350M to 5M and made every subsequent
    command fail, including the `rm` that would fix it.
  * PROBE-PREFERRED ranking.  A script that constructs a WitnessBuilder or
    writes a *.witness.json is a PRODUCER: expensive, and it dirties the tree
    (producers write SIBLING witnesses, AGENTS.md).  Probes are preferred even
    when the cost heuristic likes the producer.
  * --dry-run prints exactly what would be executed and runs nothing.

USAGE
    python3 -u stale_audit_discriminator.py                  # scan + worklist
    python3 -u stale_audit_discriminator.py --reconcile      # vs the bean's counts
    python3 -u stale_audit_discriminator.py --json
    python3 -u stale_audit_discriminator.py --rerun 3 --dry-run
    python3 -u stale_audit_discriminator.py --rerun 3
    python3 -u stale_audit_discriminator.py --rerun-doc <path>

It writes NOTHING into the repo itself.  Producers it runs may write sibling
witnesses; the re-run phase prints `git status --short` before and after and
names the NEW dirt so the caller can `git checkout --` it.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

# ---------------------------------------------------------------------------
# constants of the problem
# ---------------------------------------------------------------------------

MIGRATION_COMMIT = "c1a3299434"
MIGRATION_DATE = "2026-08-16"          # ISO -> string compare is date order
SIGFIG_MIN = 10
MIN_FREE_BYTES = 2 * 1024 ** 3          # refuse to launch a producer under 2 GiB

REPO = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                           capture_output=True, text=True,
                           check=True).stdout.strip())

TREES = {
    "docs/audits": REPO / "docs" / "audits",
    "docs/coordination": REPO / "docs" / "coordination",
    "beans/defs": REPO / "beans/defs",
}

# (a) topic.  Bare `peel` is far too common in prose, so it counts only in a
# Markov-trace context on the same line.
TOPIC_STRONG = re.compile(
    r"markov_peel|tr_M_atomic|word_to_element|tr_m_atom(?![a-z])", re.I)
TOPIC_NARROW = re.compile(r"markov_peel|tr_M_atomic")   # the bean's own wording
TOPIC_PEEL_CTX = re.compile(
    r"(?=.*\bpeel\b)(?=.*(markov|tr_M|trace|braid|hecke))", re.I)

# (c) a decimal with >= SIGFIG_MIN significant digits.  The lookarounds reject
# dotted versions, dates and IPs.
DECIMAL_RE = re.compile(r"(?<![\w.])(-?\d+\.\d+)(?:[eE]([+-]?\d+))?(?![\w.])")

SCRIPT_PATTERNS = [
    re.compile(r"(?<![\w/])((?:computations|scripts|tools|content)/[\w./-]+\.py)"),
    re.compile(r"`([\w./-]+\.py)`"),
    re.compile(r"\]\(([\w./-]+\.py)\)"),
    re.compile(r"\b([a-z][a-z0-9_]{4,})\.py\b"),
]

# Cost markers.  AGENTS.md records tr_M_atomic at A>=4 in tens of minutes and
# hadron_knot_table at >50 min for ONE bound atom.  These are TEXT matches, not
# runtime measurements -- see KNOWN WEAKNESSES in the module docstring section.
EXPENSIVE_MARKERS = [
    ("hadron_knot_table", 120), ("low_isotope_mass_table", 120),
    ("mass_table", 60), ("atom_braid_word_3A", 40), ("binding_energy(", 40),
    ("tr_M_atomic", 25), ("tr_m_atomic", 25), ("pslq", 40), ("findpoly", 40),
    ("solve_psd", 25), ("sdp", 15), ("simplify(", 15), ("sympy.simplify", 15),
    ("for A in range", 25), ("ISOTOPES", 25), ("sweep", 20), ("nsolve", 20),
    ("findroot", 15), ("Matrix(", 10),
]

# A script that builds a witness is a PRODUCER: slower, and it dirties the tree.
PRODUCER_MARKERS = re.compile(
    r"WitnessBuilder|witness\.json|save_witness|write_witness|\.witness\b", re.I)

# the strong discriminator: does the doc's script actually travel the migrated
# path, so its numbers MOVED on 2026-08-16?
CONE_MARKERS = re.compile(
    r"markov_peel|word_to_element|tr_M_element|tr_M_atomic|markov_trace_canonical",
    re.I)

STDLIB_SKIP = {"os", "sys", "re", "json", "math", "mpmath", "sympy", "numpy",
               "itertools", "argparse", "pathlib", "collections", "decimal",
               "fractions", "typing", "functools", "dataclasses", "time",
               "subprocess", "textwrap", "warnings", "scipy"}


# ---------------------------------------------------------------------------
# string / exact-rational helpers  (no float)
# ---------------------------------------------------------------------------

def sigfigs(mantissa: str) -> int:
    """Significant digits of a decimal mantissa STRING.

    '0.998366622585715967' -> 18; '1.145759692457300870' -> 19;
    '0.0685558643198896'   -> 15; '3.14' -> 3.
    Leading zeros are not significant; trailing zeros after the point are.
    """
    s = mantissa.lstrip("-")
    ip, _, fp = s.partition(".")
    ip = ip.lstrip("0")
    return len(ip) + len(fp) if ip else len(fp.lstrip("0"))


def exact(mantissa: str, exponent: str | None) -> Fraction:
    """Exact rational value of a decimal literal.  Never a float."""
    f = Fraction(mantissa)
    return f * (Fraction(10) ** int(exponent)) if exponent else f


def sig_digits(lit: str) -> str:
    s = lit.lstrip("-").split("e")[0].split("E")[0]
    ip, _, fp = s.partition(".")
    ip = ip.lstrip("0")
    return (ip + fp) if ip else fp.lstrip("0")


def prefix_match(doc_lit: str, run_lit: str, min_digits: int = SIGFIG_MIN) -> bool:
    """Significant-digit prefix agreement.  Pure string work: no float parse,
    and it tolerates the doc quoting fewer digits than the producer prints."""
    a, b = sig_digits(doc_lit), sig_digits(run_lit)
    n = min(len(a), len(b), 18)
    if n < min_digits:
        return False
    if a[:n] == b[:n]:
        return True
    # allow one ulp of last-digit rounding
    return a[:n - 1] == b[:n - 1] and abs(int(a[n - 1]) - int(b[n - 1])) <= 1


def git(cmd, timeout=120):
    return subprocess.run(["git"] + cmd, cwd=str(REPO), capture_output=True,
                          text=True, timeout=timeout)


def free_bytes() -> int:
    return shutil.disk_usage(str(REPO)).free


# ---------------------------------------------------------------------------
# dating
# ---------------------------------------------------------------------------

FNAME_DATE = re.compile(r"^(20\d{2}-\d{2}-\d{2})-")
FM_CREATED = re.compile(r"^created_at:\s*(\d{4}-\d{2}-\d{2})", re.M)
FM_UPDATED = re.compile(r"^updated_at:\s*(\d{4}-\d{2}-\d{2})", re.M)


def date_of(path: Path, text: str):
    """(first_date, last_date, method).  The method is REPORTED, never mixed.

    'filename'    docs convention YYYY-MM-DD-slug.md — what the doc is ABOUT.
    'frontmatter' beans carry created_at / updated_at.
    'git'         `git log --diff-filter=A`, fallback only.  This is a SHALLOW
                  clone (boundary 2026-08-02), so anything older dates AT the
                  boundary.  Harmless HERE because the boundary precedes the
                  migration (2026-08-16): a clamped date still lands on the
                  correct side of the cut.  It would NOT be harmless for a cut
                  earlier than 2026-08-02.  (bean qou-5pgl retracted a whole
                  narrative for reading that boundary as a landing.)
    """
    m = FNAME_DATE.match(path.name)
    if m:
        return m.group(1), None, "filename"
    c = FM_CREATED.search(text[:800])
    if c:
        u = FM_UPDATED.search(text[:800])
        return c.group(1), (u.group(1) if u else None), "frontmatter"
    return None, None, "git-needed"


def git_add_date(rel: str):
    r = git(["log", "--diff-filter=A", "--date=short", "--format=%ad", "--", rel])
    lines = [x for x in r.stdout.splitlines() if x.strip()]
    return lines[-1] if lines else None


# ---------------------------------------------------------------------------
# extraction
# ---------------------------------------------------------------------------

# The corpus writes its mathematics in GREEK.  An ASCII-only keyword list
# silently drops the very lines that carry the figures: the confirmed instance's
# table row reads "| `(sigma..)^3` -- true \u03b2_Bor | 0.998562... |", which
# matches none of tr_M/trace/markov/hecke/braid.  Measured: with ASCII only,
# 1 of 3 table figures was scored; with these added, all 3 are.
NEAR_RE = re.compile(
    r"tr_M|trace|markov|beta_Bor|\u03b2_?Bor|z_[CD]|peel|hecke|braid|"
    r"[\u03c3\u03b2\u03c4]|\u2192\s*[\d.]|Vol\(|q0|q_0", re.I)

# A doc CORRECTED IN PLACE quotes its own superseded figures as a record.  Those
# must not count against it -- the confirmed instance carries both its live table
# and, inside a "CORRECTED 2026-09-05" blockquote, the three figures it replaced.
# Without this, correcting a doc makes it look PARTIALLY STALE forever.
CORRECTION_MARKER = re.compile(
    r"CORRECTED|RETRACT|SUPERSED|superseded|as first written|as published|"
    r"previously read|used to read|this (?:line|read|figure|table) (?:read|said)|"
    r"do not quote|stale|was wrong|\bOLD\b|before the (?:migration|fix)", re.I)
CORRECTION_WINDOW = 15


def extract_decimals(text: str):
    out = []
    lines_all = text.splitlines()
    for ln, line in enumerate(lines_all, 1):
        lo = max(0, ln - 1 - CORRECTION_WINDOW)
        historical = bool(CORRECTION_MARKER.search(
            "\n".join(lines_all[lo:ln])))
        for m in DECIMAL_RE.finditer(line):
            mant, expo = m.group(1), m.group(2)
            sf = sigfigs(mant)
            if sf < SIGFIG_MIN:
                continue
            out.append({
                "literal": mant + (f"e{expo}" if expo else ""),
                "sigfigs": sf, "line_no": ln, "line": line.strip()[:200],
                "near_markov": bool(NEAR_RE.search(line)),
                "historical": historical,
            })
    return out


def extract_scripts(text: str):
    hits = {}
    for pat in SCRIPT_PATTERNS:
        for m in pat.finditer(text):
            ref = m.group(1)
            ref = ref[2:] if ref.startswith("./") else ref
            e = hits.setdefault(ref, {"n": 0, "explicit": "/" in ref})
            e["n"] += 1
    return hits


_resolve_cache: dict[str, str | None] = {}


def resolve_script(ref: str):
    if ref in _resolve_cache:
        return _resolve_cache[ref]
    p = REPO / ref
    if p.is_file():
        _resolve_cache[ref] = p.relative_to(REPO).as_posix()
        return _resolve_cache[ref]
    stem = Path(ref).name
    for root in ("computations", "scripts", "tools"):
        base = REPO / root
        if base.is_dir():
            for cand in base.rglob(stem):
                if cand.is_file():
                    _resolve_cache[ref] = cand.relative_to(REPO).as_posix()
                    return _resolve_cache[ref]
    _resolve_cache[ref] = None
    return None


# ---------------------------------------------------------------------------
# script classification
# ---------------------------------------------------------------------------

_script_cache: dict[str, dict] = {}


def classify_script(rel: str) -> dict:
    if rel in _script_cache:
        return _script_cache[rel]
    p = REPO / rel
    try:
        src = p.read_text(errors="replace")
    except OSError:
        _script_cache[rel] = {"exists": False}
        return _script_cache[rel]

    lines = src.count("\n") + 1
    required_pos = [m.group(1) for m in
                    re.finditer(r"add_argument\(\s*[\"']([A-Za-z][\w-]*)[\"']", src)]
    uses_argv = bool(re.search(r"sys\.argv\[[1-9]", src)) and \
        not re.search(r"len\(sys\.argv\)", src)

    cost, reasons = 1, []
    for marker, mins in EXPENSIVE_MARKERS:
        if marker in src:
            if mins > cost:
                cost, reasons = mins, [marker]
            elif mins == cost:
                reasons.append(marker)
    if lines > 600:
        cost = max(cost, 10)
        reasons.append(f"{lines}L")

    is_producer = bool(PRODUCER_MARKERS.search(src))
    if is_producer:
        cost = max(cost, 10)          # producers are never "1 minute" here
        reasons.append("writes-witness")

    direct = bool(CONE_MARKERS.search(src))
    hop = []
    if not direct:
        for m in re.finditer(r"^\s*(?:from\s+([\w.]+)\s+import|import\s+([\w.]+))",
                             src, re.M):
            mod = (m.group(1) or m.group(2) or "").split(".")[0]
            if not mod or mod in STDLIB_SKIP:
                continue
            for root in ("computations", "computations/markov",
                         "computations/qbeta", "computations/probes"):
                cand = REPO / root / (mod + ".py")
                if cand.is_file():
                    try:
                        if CONE_MARKERS.search(cand.read_text(errors="replace")):
                            hop.append(cand.relative_to(REPO).as_posix())
                    except OSError:
                        pass
                    break

    info = {
        "exists": True, "path": rel, "lines": lines,
        "required_positional": required_pos, "uses_argv": uses_argv,
        "runnable_bare": not required_pos and not uses_argv,
        "is_producer": is_producer,
        "is_probe": ("probe" in rel or "probes/" in rel) and not is_producer,
        "cost_minutes_est": cost, "cost_reasons": sorted(set(reasons))[:4],
        "in_migrated_cone_direct": direct,
        "in_migrated_cone_onehop": sorted(set(hop)),
    }
    _script_cache[rel] = info
    return info


# ---------------------------------------------------------------------------
# scan
# ---------------------------------------------------------------------------

def scan():
    result = {"trees": {}, "candidates": []}
    for tree_name, tree_path in TREES.items():
        stats = {"md_files": 0, "topic_hits": 0, "topic_and_predated": 0,
                 "candidates": 0, "undated": 0}
        if not tree_path.is_dir():
            result["trees"][tree_name] = stats
            continue
        for path in sorted(tree_path.rglob("*.md")):
            stats["md_files"] += 1
            try:
                text = path.read_text(errors="replace")
            except OSError:
                continue
            if TOPIC_STRONG.search(text):
                topic = "strong"
            elif any(TOPIC_PEEL_CTX.search(l) for l in text.splitlines()):
                topic = "peel-in-context"
            else:
                continue
            stats["topic_hits"] += 1

            rel = path.relative_to(REPO).as_posix()
            first, last, method = date_of(path, text)
            if method == "git-needed":
                first, method = git_add_date(rel), "git"
                if first is None:
                    stats["undated"] += 1
                    continue
            if not (first < MIGRATION_DATE):
                continue
            stats["topic_and_predated"] += 1

            decs = extract_decimals(text)
            if not decs:
                continue
            stats["candidates"] += 1

            cited = []
            seen = {}
            for ref, meta in extract_scripts(text).items():
                r = resolve_script(ref)
                if r is None:
                    cited.append({"ref": ref, "resolved": None, "exists": False,
                                  "mentions": meta["n"]})
                    continue
                if r in seen:
                    seen[r]["mentions"] += meta["n"]
                    seen[r]["explicit_path_ref"] |= meta["explicit"]
                    continue
                info = dict(classify_script(r))
                info.update(resolved=r, ref=ref, mentions=meta["n"],
                            explicit_path_ref=meta["explicit"])
                seen[r] = info
                cited.append(info)

            result["candidates"].append({
                "tree": tree_name, "path": rel, "date": first,
                "date_method": method, "last_touched": last, "topic": topic,
                "n_decimals": len(decs),
                "n_decimals_near_markov": sum(1 for d in decs if d["near_markov"]),
                "max_sigfigs": max(d["sigfigs"] for d in decs),
                "decimals": decs, "cited_scripts": cited,
            })
        result["trees"][tree_name] = stats
    result["candidates"] = rank(result["candidates"])
    return result


def rank(cands):
    """Rank by decidable-now x cheap x probe-preferred."""
    for c in cands:
        runnable = [s for s in c["cited_scripts"]
                    if s.get("exists") and s.get("runnable_bare")]
        cone = [s for s in runnable if s.get("in_migrated_cone_direct")
                or s.get("in_migrated_cone_onehop")]
        c["n_scripts_cited"] = len(c["cited_scripts"])
        c["n_scripts_on_disk"] = sum(1 for s in c["cited_scripts"] if s.get("exists"))
        c["n_scripts_runnable"] = len(runnable)
        c["n_scripts_in_cone"] = len(cone)

        # PRIMARY = the one script we would actually run.  Probes before
        # producers, cheap before dear, explicit path-cite before bare stem,
        # then most-mentioned.  A doc listing 49 producers is not citing 49
        # sources for its own figures.
        prim = sorted(cone, key=lambda s: (
            not s.get("is_probe"), s.get("is_producer", False),
            s["cost_minutes_est"], not s.get("explicit_path_ref"),
            -s.get("mentions", 0), s["resolved"]))
        c["primary_script"] = prim[0]["resolved"] if prim else None
        c["primary_cost"] = prim[0]["cost_minutes_est"] if prim else 999
        c["primary_is_probe"] = bool(prim and prim[0].get("is_probe"))
        c["primary_is_producer"] = bool(prim and prim[0].get("is_producer"))
        c["primary_explicit"] = bool(prim and prim[0].get("explicit_path_ref"))

        if cone:
            c["decidability"] = "DECIDABLE-NOW"
        elif runnable:
            c["decidability"] = "RUNNABLE-BUT-OFF-CONE"
        elif c["n_scripts_on_disk"]:
            c["decidability"] = "SCRIPT-NEEDS-ARGS"
        elif c["n_scripts_cited"]:
            c["decidability"] = "SCRIPT-GONE"
        else:
            c["decidability"] = "NO-SCRIPT-CITED"

        tier = {"DECIDABLE-NOW": 0, "RUNNABLE-BUT-OFF-CONE": 1,
                "SCRIPT-NEEDS-ARGS": 2, "SCRIPT-GONE": 3,
                "NO-SCRIPT-CITED": 4}[c["decidability"]]
        c["_sort"] = (tier, not c["primary_is_probe"], c["primary_cost"],
                      not c["primary_explicit"], -c["n_decimals_near_markov"],
                      c["path"])
    cands.sort(key=lambda c: c["_sort"])
    for c in cands:
        c.pop("_sort", None)
    return cands


# ---------------------------------------------------------------------------
# re-run
# ---------------------------------------------------------------------------

def build_env():
    env = dict(os.environ)
    extra = [str(REPO / "computations"), str(REPO / "computations" / "markov"),
             str(REPO)]
    prev = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = os.pathsep.join(extra + ([prev] if prev else []))
    return env


TRACEBACK_RE = re.compile(r"^Traceback \(most recent call last\):", re.M)
# A refusal implemented as a raised DOMAIN exception is not a crash
# (AGENTS.md: qbeta_habiro_phase5q_dn / AmDifferenceInvalid).
GUARD_RE = re.compile(
    r"AmDifferenceInvalid|Refusing|refuses|precision would|must run under|"
    r"anchor guard|would publish laundered", re.I)


def rerun_script(rel: str, timeout: int, logdir: Path | None):
    """Run one script, cwd=<producer dir> then cwd=<repo root>.

    AGENTS.md: capture STDOUT as well as stderr (by-design refusals explain
    themselves on stdout), decide on a TRACEBACK not on the exit code, and try
    both cwds because several producers use repo-root-relative paths.
    """
    p = REPO / rel
    env = build_env()
    attempts = []
    for label, cwd in (("cwd=producer-dir", p.parent), ("cwd=repo-root", REPO)):
        rec = {"cwd": label, "returncode": None, "timed_out": False,
               "stdout": "", "stderr": ""}
        try:
            r = subprocess.run([sys.executable, "-u", str(p)], cwd=str(cwd),
                               capture_output=True, text=True, timeout=timeout,
                               env=env)
            rec.update(returncode=r.returncode, stdout=r.stdout or "",
                       stderr=r.stderr or "")
        except subprocess.TimeoutExpired as e:
            def dec(x):
                return x.decode("utf-8", "replace") if isinstance(x, bytes) else (x or "")
            rec.update(timed_out=True, stdout=dec(e.stdout), stderr=dec(e.stderr))
        except MemoryError:
            rec.update(stderr="MemoryError in harness")
        blob = rec["stdout"] + "\n" + rec["stderr"]
        rec["has_traceback"] = bool(TRACEBACK_RE.search(blob))
        rec["looks_like_guard"] = bool(GUARD_RE.search(blob))
        attempts.append(rec)
        if rec["stdout"].strip() and not rec["has_traceback"] and not rec["timed_out"]:
            break
    if logdir:
        logdir.mkdir(parents=True, exist_ok=True)
        (logdir / (Path(rel).stem + ".log")).write_text("\n\n".join(
            f"=== {a['cwd']} rc={a['returncode']} timeout={a['timed_out']} "
            f"tb={a['has_traceback']} ===\n--- stdout ---\n{a['stdout'][:200000]}"
            f"\n--- stderr ---\n{a['stderr'][:40000]}" for a in attempts))
    return attempts


def decimals_in_output(text: str):
    out = {}
    for line in text.splitlines():
        for m in DECIMAL_RE.finditer(line):
            if sigfigs(m.group(1)) < SIGFIG_MIN:
                continue
            lit = m.group(1) + (f"e{m.group(2)}" if m.group(2) else "")
            out.setdefault(lit, line.strip()[:160])
    return out


def verdict_for(cand, run_lits, drop_historical=True):
    doc = [d for d in cand["decimals"] if d["near_markov"]] or cand["decimals"]
    n_hist = sum(1 for d in doc if d["historical"])
    if drop_historical:
        doc = [d for d in doc if not d["historical"]] or doc
    matched = [d for d in doc if any(prefix_match(d["literal"], r) for r in run_lits)]
    unmatched = [d for d in doc if d not in matched]
    hist_note = f" [{n_hist} figure(s) excluded as quoted-inside-a-correction]" \
        if (drop_historical and n_hist) else ""
    if not run_lits:
        return ("UNDECIDED", matched, unmatched,
                "the script printed no >=10-sf decimal - nothing to diff against" + hist_note)
    if matched and not unmatched:
        return ("CONFIRMED-CURRENT", matched, unmatched,
                "every markov-adjacent figure the doc quotes is reproduced today" + hist_note)
    if matched and unmatched:
        return ("PARTIAL-STALE", matched, unmatched,
                f"{len(matched)} of {len(doc)} reproduced; the rest are not" + hist_note)
    return ("UNDECIDED-LEANS-STALE", matched, unmatched,
            "no quoted figure reproduced — consistent with staleness, but ALSO "
            "with the doc quoting numbers this particular script never prints; "
            "needs an eyeball before it becomes a verdict" + hist_note)


def dirt():
    r = git(["status", "--short"])
    return [l for l in r.stdout.splitlines() if l.strip()]


# ---------------------------------------------------------------------------
# reporting
# ---------------------------------------------------------------------------

def print_report(res, top):
    print("=" * 78)
    print("STALE-AUDIT DISCRIMINATOR — markov_peel convention C->D "
          f"({MIGRATION_COMMIT}, {MIGRATION_DATE})")
    print("=" * 78)
    print(f"repo {REPO}   free {free_bytes() // 1024**3} GiB")
    print(f"filters: (a) topic  (b) dated < {MIGRATION_DATE}  "
          f"(c) >= {SIGFIG_MIN} sig-fig decimal\n")

    print("--- MEASURED CANDIDATE COUNTS PER TREE (rglob, wide topic regex) ---")
    print(f"{'tree':20} {'.md':>7} {'(a)':>7} {'(a)+(b)':>9} "
          f"{'(a)(b)(c)':>10} {'undated':>8}")
    for t, s in res["trees"].items():
        print(f"{t:20} {s['md_files']:>7} {s['topic_hits']:>7} "
              f"{s['topic_and_predated']:>9} {s['candidates']:>10} {s['undated']:>8}")
    print()

    print("--- DECIDABILITY SPLIT ---")
    split = {}
    for c in res["candidates"]:
        split[c["decidability"]] = split.get(c["decidability"], 0) + 1
    total = len(res["candidates"]) or 1
    for k in ("DECIDABLE-NOW", "RUNNABLE-BUT-OFF-CONE", "SCRIPT-NEEDS-ARGS",
              "SCRIPT-GONE", "NO-SCRIPT-CITED"):
        n = split.get(k, 0)
        print(f"  {k:24} {n:>4}   {100 * n // total:>3}%")
    print(f"  {'TOTAL':24} {len(res['candidates']):>4}")
    print()

    if top <= 0:
        return
    print(f"--- RANKED WORKLIST (top {top}; probe-preferred, cheapest first) ---")
    print(f"{'#':>2} {'cost':>5} {'kind':>8} {'nearM':>6} {'cone':>5}  doc")
    print("-" * 78)
    for i, c in enumerate(res["candidates"][:top], 1):
        kind = "probe" if c["primary_is_probe"] else (
            "producer" if c["primary_is_producer"] else "script")
        print(f"{i:>2} {c['primary_cost']:>4}m {kind:>8} "
              f"{c['n_decimals_near_markov']:>6} {c['n_scripts_in_cone']:>5}  {c['path']}")
        prim = next((s for s in c["cited_scripts"]
                     if s.get("resolved") == c["primary_script"]), None)
        if prim:
            cone = "direct-cone" if prim["in_migrated_cone_direct"] else \
                "1hop:" + ",".join(Path(x).stem
                                   for x in prim["in_migrated_cone_onehop"][:2])
            print(f"      RUN  PYTHONPATH=computations python3 -u {prim['resolved']}")
            print(f"           [{cone}; ~{prim['cost_minutes_est']}m; {prim['lines']}L; "
                  f"{'explicit-path-cite' if prim['explicit_path_ref'] else 'bare-stem-cite'}"
                  f"; {prim['mentions']} mention(s)]")
        if c["n_scripts_in_cone"] > 1:
            print(f"           (doc also names {c['n_scripts_in_cone'] - 1} other "
                  f"cone script(s) — NOT run; see RE-RUN SAFETY)")
    print()


def reconcile():
    """Counts under the bean's OWN definition alongside mine.

    Bean qou-5pgl quotes 75 / 34 / 7.  Those are right UNDER ITS OWN DEFINITION:
    narrow topic regex (the two names it lists), audits dated by FILENAME and
    globbed at top level only, beans dated by `updated_at` ("last touched").
    Widening the regex to the migrated function itself (word_to_element), or
    dating beans by created_at, or rglobbing subdirectories, each moves the
    number up.  Neither definition is wrong; they answer different questions.
    """
    import glob
    print("RECONCILIATION — the bean's counts vs this scan's\n")
    print(f"{'topic definition':52} {'audits':>7} {'+10sf':>7} "
          f"{'beansU':>7} {'+10sf':>7} {'beansC':>7} {'+10sf':>7}")
    for name, pat in (("NARROW  markov_peel|tr_M_atomic  (the bean's)", TOPIC_NARROW),
                      ("WIDE    + word_to_element, tr_m_atom (mine)", TOPIC_STRONG)):
        a = []
        for f in sorted(glob.glob(str(REPO / "docs/audits/*.md"))):
            m = FNAME_DATE.match(Path(f).name)
            if not m or not (m.group(1) < MIGRATION_DATE):
                continue
            t = Path(f).read_text(errors="replace")
            if pat.search(t):
                a.append(t)
        a10 = [t for t in a if extract_decimals(t)]
        bu = bu10 = bc = bc10 = 0
        for f in sorted(glob.glob(str(REPO / "beans/defs/*.md"))):
            t = Path(f).read_text(errors="replace")
            if not pat.search(t):
                continue
            has = bool(extract_decimals(t))
            u, c = FM_UPDATED.search(t[:800]), FM_CREATED.search(t[:800])
            if u and u.group(1) < MIGRATION_DATE:
                bu += 1
                bu10 += has
            if c and c.group(1) < MIGRATION_DATE:
                bc += 1
                bc10 += has
        print(f"{name:52} {len(a):>7} {len(a10):>7} {bu:>7} {bu10:>7} "
              f"{bc:>7} {bc10:>7}")
    print("\nbeansU = dated by updated_at (the bean's basis); "
          "beansC = dated by created_at.")
    print("audits: top-level *.md only here; the main scan rglobs subdirs, "
          "which adds ~27 more.")


# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--top", type=int, default=12)
    ap.add_argument("--reconcile", action="store_true")
    ap.add_argument("--rerun", type=int, default=0)
    ap.add_argument("--rerun-doc", default=None)
    ap.add_argument("--timeout", type=int, default=180)
    ap.add_argument("--logdir", default=None)
    ap.add_argument("--dry-run", action="store_true",
                    help="print the exact commands and run nothing")
    args = ap.parse_args()

    if args.reconcile:
        reconcile()
        return

    res = scan()
    if args.json:
        print(json.dumps(res, indent=2))
        return
    print_report(res, args.top)

    todo = []
    if args.rerun_doc:
        todo = [c for c in res["candidates"] if c["path"] == args.rerun_doc]
        if not todo:
            print(f"!! {args.rerun_doc} is not in the candidate set")
    elif args.rerun:
        todo = [c for c in res["candidates"]
                if c["decidability"] == "DECIDABLE-NOW"][:args.rerun]
    if not todo:
        return

    logdir = Path(args.logdir) if args.logdir else None
    print("=" * 78)
    print("RE-RUN PHASE" + ("  [DRY RUN]" if args.dry_run else ""))
    print("=" * 78)
    before = dirt()
    print(f"git status --short BEFORE: {len(before)} entries (pre-existing)")

    for c in todo:
        print("\n" + "-" * 78)
        print(f"DOC  {c['path']}  ({c['date']} via {c['date_method']})")
        prim = c["primary_script"]
        if not prim:
            print("  VERDICT: UNDECIDED (no runnable in-cone script cited)")
            continue
        print(f"  ONE script only: {prim}")
        if args.dry_run:
            print(f"  WOULD RUN: PYTHONPATH=computations python3 -u {prim}")
            continue
        fb = free_bytes()
        if fb < MIN_FREE_BYTES:
            print(f"  ABORT: only {fb // 1024**2} MiB free (floor "
                  f"{MIN_FREE_BYTES // 1024**3} GiB). Refusing to launch.")
            continue
        print(f"  RUN (timeout {args.timeout}s, {fb // 1024**3} GiB free)")
        attempts = rerun_script(prim, args.timeout, logdir)
        run_lits = {}
        for a in attempts:
            print(f"    [{a['cwd']}] rc={a['returncode']} timeout={a['timed_out']} "
                  f"traceback={a['has_traceback']} stdout={len(a['stdout'])}B "
                  f"stderr={len(a['stderr'])}B")
            if a["has_traceback"]:
                tb = [l for l in a["stderr"].splitlines() if l.strip()]
                print("      stderr tail:", tb[-1][:150] if tb else "")
                if a["looks_like_guard"]:
                    print("      NOTE looks like a BY-DESIGN guard raised as a "
                          "domain exception, not a crash")
            elif a["returncode"] not in (0, None):
                print("      NOTE non-zero exit WITHOUT traceback — by-design "
                      "refusal is likely; read stdout, not the exit code")
            if a["stdout"].strip() and not a["timed_out"]:
                run_lits.update(decimals_in_output(a["stdout"]))

        if not run_lits and all(not a["stdout"].strip() for a in attempts):
            print("  VERDICT: UNDECIDED (script produced no usable stdout)")
            continue
        v, matched, unmatched, why = verdict_for(c, list(run_lits))
        vraw, _, _, _ = verdict_for(c, list(run_lits), drop_historical=False)
        print(f"  script emitted {len(run_lits)} distinct >= {SIGFIG_MIN}-sf decimals")
        print(f"  VERDICT: {v} - {why}")
        if vraw != v:
            print(f"  (raw verdict without the correction-block filter: {vraw})")
        for d in matched[:6]:
            print(f"    MATCH   {d['literal']:24} L{d['line_no']}: {d['line'][:70]}")
        for d in unmatched[:6]:
            print(f"    NOMATCH {d['literal']:24} L{d['line_no']}: {d['line'][:70]}")
        print("  script output (first 10):")
        for lit, ctx in list(run_lits.items())[:10]:
            print(f"    {lit:26} | {ctx[:68]}")

    after = dirt()
    new = [l for l in after if l not in before]
    print("\n" + "=" * 78)
    print(f"git status --short AFTER: {len(after)} entries")
    if new:
        print("NEW DIRT — revert with `git checkout -- <path>`:")
        for l in new:
            print("   ", l)
    else:
        print("tree unchanged by the re-run phase")
    print(f"free space now: {free_bytes() // 1024**3} GiB")


if __name__ == "__main__":
    main()
