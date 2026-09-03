#!/usr/bin/env python3
"""Validate ck-dk-registry.json — internally, AND against its markdown twin.

The registry (docs/coordination/ck-dk-canonical-registry.md + its JSON
twin ck-dk-registry.json) is the single source of truth for the
canonical-vs-empirical status of the Q_β c_k ladder and the m_p d_k
tower.

PART 1 — JSON-internal (the original checks, §8 flip-flop guard):

  1. Any WIRED rung must be tier `canonical` (anchor-stable, derived).
     (No empirical/near-match/fit/refuted rung may be wired.)
  2. Every rung's tier must be one of the declared tiers.
  3. production.qbeta_wired_rungs must match the rungs marked wired=true.

PART 2 — TWIN COMPARISON (`--twin`, added 2026-08-29, bean `qou-kt8o`).

WHY. The JSON's own `meta.description` says "Tiers and wiring MUST agree
between the two", and until now *nothing checked that*. Part 1 opens one
file. The consequence is on the record: the `dc_3/dq ≈ 4.6×10⁶ → 3.84×10⁶`
correction landed in the `.md` on 2026-08-25 (PR #5765) with the reasoning
written out in full, and the JSON still said `4.6e6` four days later. Every
check passed the whole time, because no check read both files.

The divergence is not one-directional, which is the argument for a
mechanical check rather than care. Measured when this was written: the
`.md` had the CORRECTED slope and the STALE `−2.88%` swing; the JSON (after
PR #5942) had the corrected slope and the live `−2.375%` swing. Each file
was ahead of the other on a different number in the same table row.

WHAT IT COMPARES, and why only these. A twin check is only as good as the
facts it can key on, so this keys on four that are structural or explicitly
pinned, and deliberately does NOT diff prose:

  T1  rung coverage   — every JSON rung has a `.md` row and vice versa
  T2  tier agreement  — JSON `tier` vs the `.md` status cell's tier word
  T3  wired agreement — JSON wired rungs vs the §6 authoritative statement
  T4  pinned figures  — named quantities quoted in BOTH files (currently
                        `dc_3/dq` and the c_3 cross-anchor swing), compared
                        numerically

PART 3 — TWIN-vs-SOURCE (`--twin`; the check the twin comparison cannot be).

**Twin agreement is necessary but not sufficient, and this registry is a
live example.** Both files state the L2 dashboard as "2/7 beats-100×",
citing `summary.beats_100x_count = 2`. They agree, so T1–T4 pass them. They
are also both wrong in the way AGENTS.md §"Precision goals" rules out
explicitly: `beats_100x_count` counts the CALIBRATION INPUTS `m_e` and `m_p`
alongside predictions, and `m_e`'s error is not measured but *defined* zero
(it is the CAL-1 input that fixes the MeV unit). The canonical count is
`beats_100x_scoreable` / `scoreable_total` = 1/5, and AGENTS.md says bare
`beats_100x_count` "must not be quoted as an accuracy result".

So T5 checks both twins against the WITNESS, not against each other:

  T5  dashboard counts — both files' quoted dashboard figures vs the live
                         `per-observable-100x-status.witness.json`, using the
                         mandated `beats_100x_scoreable`/`scoreable_total`

Exit 0 if consistent; exit 1 with a report otherwise. No external deps.

Usage:
  python3 docs/coordination/ck_dk_registry_validate.py            # part 1
  python3 docs/coordination/ck_dk_registry_validate.py --twin     # all parts
  python3 docs/coordination/ck_dk_registry_validate.py --selftest # prove the
                                                                  # checks fire
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTRY = HERE / "ck-dk-registry.json"
TWIN = HERE / "ck-dk-canonical-registry.md"
REPO = HERE.parent.parent
DASHBOARD = REPO / "computations" / "per-observable-100x-status.witness.json"


# --------------------------------------------------------------------------
# Twin comparison (part 2) + twin-vs-source (part 3)
# --------------------------------------------------------------------------
#
# A NOTE ON PARSER FAILURE, which is the whole reason this is written the way
# it is. A markdown scraper that cannot find its table has two options: report
# "no divergences" or report that it could not look. The first is how a green
# result gets produced by a scan that never ran — the exact failure this
# session hit twice, most sharply when a hand-written scan of an audit witness
# guessed key names, found zero flips, and would have reported a clean tree.
# So every extractor below raises `TwinParseError` rather than returning empty,
# and `--selftest` asserts each check FIRES on a synthetic divergence.

class TwinParseError(RuntimeError):
    """The `.md` twin did not have the shape this validator needs.

    Raised — never swallowed into an empty result — so a structural change to
    the document is reported as "cannot check", not as "nothing wrong".
    """


# JSON tier -> the word(s) that may carry it in the `.md` status cell.
# The `.md` uses a coarser vocabulary than the JSON (both `empirical_fit` and
# `empirical_near_match` surface as "EMPIRICAL"), so this is a MANY-TO-ONE map
# and the check is "the .md word is an accepted rendering of the JSON tier",
# not string equality.
_TIER_WORDS = {
    "canonical": {"CANONICAL"},
    "empirical_near_match": {"EMPIRICAL"},
    "empirical_fit": {"EMPIRICAL"},
    "artifact": {"EMPIRICAL", "ARTIFACT"},
    "conjecture": {"CONJECTURE"},
    "refuted": {"REFUTED", "EMPIRICAL"},
    "tbd": {"TBD"},
    "open": {"OPEN"},
}


def _md_section(md: str, heading_re: str) -> str:
    """Slice one `## n. ...` section out of the twin, exclusive of the next."""
    m = re.search(heading_re, md, re.M)
    if not m:
        raise TwinParseError(f"twin has no section matching {heading_re!r}")
    start = m.end()
    nxt = re.search(r"^## \d+\.", md[start:], re.M)
    return md[start:start + nxt.start()] if nxt else md[start:]


def _md_rungs(section: str, prefix: str) -> dict[str, str]:
    """Map rung id -> status cell, from a `| rung | status | ...` table.

    The rung cell is bolded and may name several rungs at once
    (`**c_6, c_7**`), matching the JSON's range form (`"6-7"`). Both sides are
    normalised to a sorted tuple of bare digits so `c_6, c_7` and `6-7` compare
    equal without either file having to change how it writes them.
    """
    rows: dict[str, str] = {}
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        ids = re.findall(rf"{prefix}_(\d+)", cells[0])
        if not ids:
            continue
        rows["-".join(str(i) for i in sorted(int(x) for x in ids))] = cells[1]
    if not rows:
        raise TwinParseError(
            f"no `{prefix}_k` table rows found — the twin's table shape changed"
        )
    return rows


def _md_status_word(cell: str) -> str:
    """The VERDICT token of a status cell — its first bold run, upper-cased.

    Matching tier words against the whole cell is far too loose, and this
    validator's own selftest caught it doing so: setting c_2's JSON tier to
    `refuted` did NOT fire T2, because c_2's cell discusses "the implied
    empirical c₂ under convention D" further along, and `"EMPIRICAL" in cell`
    matched that prose. These cells are paragraphs — they cite other tiers,
    other rungs and superseded verdicts by name — so only the leading
    `**...**` run is the row's own verdict. Same detector-blindness class the
    corpus documents elsewhere: a pattern that matches the discussion of a
    thing as readily as the thing.
    """
    m = re.search(r"\*\*(.+?)\*\*", cell, re.S)
    return (m.group(1) if m else cell).upper()


def _norm_rung(rung: str) -> str:
    """JSON rung id -> the same sorted digit tuple `_md_rungs` produces.

    A hyphen in the JSON means an INCLUSIVE RANGE (`meta.schema_version_note`:
    "ranges carry a hyphen ('6-7','8-10')"), so it must be EXPANDED, not just
    split. Splitting gives `8-10` -> {8,10} while the `.md` writes the same
    rungs out as `**c_8, c_9, c_10**` -> {8,9,10}, and the two never match —
    which is exactly what this validator's own selftest caught: a spurious
    "in the JSON, no matching row" against a row sitting right there.
    """
    parts = [int(p) for p in re.findall(r"\d+", str(rung))]
    if "-" in str(rung) and len(parts) == 2:
        parts = list(range(parts[0], parts[1] + 1))
    return "-".join(str(p) for p in sorted(parts))


def _figure(text: str, label_re: str, what: str) -> float:
    """Pull ONE number quoted next to a named label.

    Free-form number extraction over a 1000-line document is a false-positive
    machine (measured this session: an unguarded `0.0596` grep ran 66 false to
    12 true). So each pinned figure is extracted by an explicit label pattern
    and every match must agree, rather than trusting the first hit.
    """
    hits = re.findall(label_re, text)
    if not hits:
        raise TwinParseError(f"no {what} figure found (pattern {label_re!r})")
    vals = {_to_float(h) for h in hits}
    if len(vals) > 1:
        raise TwinParseError(
            f"{what}: the SAME file quotes several values {sorted(vals)} — "
            f"resolve the internal disagreement before comparing twins"
        )
    return vals.pop()


def _to_float(tok: str) -> float:
    """`3.84e6`, `3.84×10⁶`, `4.6e6`, `2.375` -> float."""
    t = tok.replace("−", "-").replace(",", "").strip()
    m = re.match(r"^(-?[\d.]+)\s*[×x*]\s*10\^?\{?(-?\d+)\}?", t)
    if m:
        return float(m.group(1)) * 10 ** int(m.group(2))
    m = re.match(r"^(-?[\d.]+)\s*[×x*]\s*10([⁰¹²³⁴⁵⁶⁷⁸⁹]+)", t)
    if m:
        sup = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
        return float(m.group(1)) * 10 ** int(m.group(2).translate(sup))
    return float(t)


# Pinned cross-file figures. Each entry: (label, json-side pattern, md-side
# pattern, relative tolerance). Tolerance is relative because these are quoted
# to differing precision on the two sides by design (`3.84e6` vs `3.839e6`);
# the check is "the same quantity", not "the same rendering".
_SLOPE = r"dc_?3\s*/\s*dq\s*[~≈]\s*(-?[\d.]+\s*(?:e6|[×x]\s*10[\^⁰¹²³⁴⁵⁶⁷⁸⁹]*6?))"
_SWING = r"swings?\s*[−-]([\d.]+)\s*%\s*to\s*muon"

PINNED = [
    ("dc_3/dq slope", _SLOPE, _SLOPE, 0.02),
    ("c_3 cross-anchor swing", _SWING, _SWING, 0.02),
]


def twin_checks(d: dict) -> list[str]:
    """T1-T4: compare the JSON against its markdown twin."""
    errors: list[str] = []
    md = TWIN.read_text(encoding="utf-8")

    ck_sec = _md_section(md, r"^## 3\. .*per-rung registry")
    dk_sec = _md_section(md, r"^## 4\. .*per-rung registry")

    for family, section, prefix, key in (
        ("Q_β c_k", ck_sec, "c", "qbeta_ck_ladder"),
        ("m_p d_k", dk_sec, "d", "mp_dk_tower"),
    ):
        md_rows = _md_rungs(section, prefix)
        js_rows = {_norm_rung(r["rung"]): r for r in d[key]["rungs"]}

        # T1 — coverage, both directions.
        for only_js in sorted(set(js_rows) - set(md_rows)):
            errors.append(
                f"T1 {family} rung {only_js}: in the JSON, no matching row in "
                f"the .md twin"
            )
        for only_md in sorted(set(md_rows) - set(js_rows)):
            errors.append(
                f"T1 {family} rung {only_md}: a row in the .md twin, absent "
                f"from the JSON"
            )

        # T2 — tier agreement on the rungs both carry.
        for rid in sorted(set(js_rows) & set(md_rows)):
            tier = js_rows[rid].get("tier")
            allowed = _TIER_WORDS.get(tier, set())
            verdict = _md_status_word(md_rows[rid])
            if not any(w in verdict for w in allowed):
                errors.append(
                    f"T2 {family} rung {rid}: JSON tier {tier!r} expects one of "
                    f"{sorted(allowed)} in the .md status cell, whose verdict "
                    f"token reads {verdict!r}"
                )

    # T3 — wired agreement. §6 is the twin's "ONE authoritative statement".
    sec6 = _md_section(md, r"^## 6\. Production wiring")
    js_wired = sorted(str(r) for r in d["production"]["qbeta_wired_rungs"])
    md_wired = sorted(set(re.findall(r"c_(\d+)\s+only", sec6)))
    if js_wired != md_wired:
        errors.append(
            f"T3 wired: JSON production.qbeta_wired_rungs {js_wired} != the .md "
            f"§6 statement {md_wired or '<none parsed>'}"
        )
    if "m_p: bare" not in sec6 and d["production"]["mp_wired_rungs"]:
        errors.append("T3 wired: JSON wires an m_p d_k but §6 still says bare")

    # T4 — pinned figures quoted in both files.
    js_text = REGISTRY.read_text(encoding="utf-8")
    for label, js_pat, md_pat, tol in PINNED:
        try:
            a, b = _figure(js_text, js_pat, f"JSON {label}"), _figure(md, md_pat, f".md {label}")
        except TwinParseError as e:
            errors.append(f"T4 {label}: {e}")
            continue
        if abs(a - b) > tol * max(abs(a), abs(b)):
            errors.append(
                f"T4 {label}: JSON says {a:g}, .md twin says {b:g} "
                f"(>{tol:.0%} apart — one of them is stale)"
            )
    return errors


def dashboard_checks(d: dict) -> list[str]:
    """T5: check BOTH twins against the witness, not against each other.

    This is the check a twin comparison structurally cannot be. Both files
    currently agree on "2/7", and both are wrong the same way.
    """
    errors: list[str] = []
    if not DASHBOARD.exists():
        return [f"T5: dashboard witness not found at {DASHBOARD}"]
    w = json.loads(DASHBOARD.read_text(encoding="utf-8"))
    s = w.get("data", {}).get("summary", {})
    scoreable = s.get("beats_100x_scoreable")
    total = s.get("scoreable_total")
    if scoreable is None or total is None:
        return [
            "T5: witness has no beats_100x_scoreable/scoreable_total — the "
            "dashboard producer changed shape; re-check before trusting any "
            "count quoted in the registry"
        ]

    js_beats = d["production"].get("dashboard_beats_100x")
    js_total = d["production"].get("dashboard_total")
    if (js_beats, js_total) != (scoreable, total):
        errors.append(
            f"T5 JSON: production.dashboard_{{beats_100x,total}} = "
            f"{js_beats}/{js_total}, but the witness scores "
            f"{scoreable}/{total} (beats_100x_scoreable/scoreable_total). "
            f"AGENTS.md §Precision goals: beats_100x_count counts the "
            f"CALIBRATION INPUTS m_e and m_p and 'must not be quoted as an "
            f"accuracy result'"
        )

    md = TWIN.read_text(encoding="utf-8")
    sec6 = _md_section(md, r"^## 6\. Production wiring")
    for a, b in re.findall(r"dashboard:\s*\*\*(\d+)/(\d+)\*\*", sec6):
        if (int(a), int(b)) != (scoreable, total):
            errors.append(
                f"T5 .md §6: quotes {a}/{b} beats-100×, witness scores "
                f"{scoreable}/{total}"
            )
    if "beats_100x_count" in _assertive(sec6):
        errors.append(
            "T5 .md §6: cites `beats_100x_count` as the source of its figure, "
            "which AGENTS.md forbids quoting as an accuracy result — use "
            "beats_100x_scoreable"
        )
    return errors


def _assertive(section: str) -> str:
    """Drop blockquoted lines — the document's annotation register.

    A checker for "does this document cite the forbidden field" must not fire
    on the passage EXPLAINING that the field is forbidden. This validator did
    exactly that on its first run: the §6 correction note names
    `beats_100x_count` in order to say it must not be quoted, and a plain
    substring test flagged it.

    That is a known and expensive failure mode in this repo, not a one-off —
    PR #5923 rebuilt a c_3 wiring tripwire for the identical reason, where the
    only two hits were inside a docstring stating that c_3 is refuted and NOT
    wired. Writing the correct thing down was enough to fail the check that
    the thing had not been done.

    In this document `>` blocks are corrections, caveats and history; the
    unquoted bullets are the authoritative statement. So the assertive text is
    what is left after the blockquotes are removed. `--selftest` pins BOTH
    directions: the check must still fire on an unquoted citation, and must
    stay silent on a blockquoted one.
    """
    return "\n".join(
        ln for ln in section.splitlines() if not ln.lstrip().startswith(">")
    )


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    d = json.loads(REGISTRY.read_text(encoding="utf-8"))
    tiers = set(d["meta"]["tiers"].keys())
    errors: list[str] = []

    def check_rungs(family_key: str, rungs: list[dict]) -> list:
        wired = []
        for r in rungs:
            rung = r.get("rung")
            tier = r.get("tier")
            if tier not in tiers:
                errors.append(f"{family_key} rung {rung}: unknown tier {tier!r}")
            if r.get("wired"):
                wired.append(rung)
                if tier != "canonical":
                    errors.append(
                        f"{family_key} rung {rung}: WIRED but tier={tier!r} "
                        f"(flip-flop guard: only `canonical` may be wired)"
                    )
        return wired

    ck_wired = check_rungs("qbeta_ck", d["qbeta_ck_ladder"]["rungs"])
    dk_wired = check_rungs("mp_dk", d["mp_dk_tower"]["rungs"])

    prod = d["production"]

    # Normalize every rung identifier to its canonical string form before
    # comparing, so the check is robust whether a rung is authored as an
    # int (legacy) or a string (current schema v2). Single rungs are bare
    # digits ("2".."6"); ranges carry a hyphen ("6-7", "8-10"). Only single
    # rungs may be wired, so ranges are filtered out on the canonical form.
    def _rung_id(rung) -> str:
        return str(rung)

    def _is_single(rung) -> bool:
        return "-" not in _rung_id(rung)

    def _wired_ids(wired: list) -> list[str]:
        return sorted(_rung_id(x) for x in wired if _is_single(x))

    def _prod_ids(prod_rungs: list) -> list[str]:
        return sorted(_rung_id(x) for x in prod_rungs)

    if _wired_ids(ck_wired) != _prod_ids(prod["qbeta_wired_rungs"]):
        errors.append(
            f"production.qbeta_wired_rungs {prod['qbeta_wired_rungs']} "
            f"!= rungs marked wired {ck_wired}"
        )
    if _wired_ids(dk_wired) != _prod_ids(prod["mp_wired_rungs"]):
        errors.append(
            f"production.mp_wired_rungs {prod['mp_wired_rungs']} "
            f"!= rungs marked wired {dk_wired}"
        )

    twin = "--twin" in sys.argv
    if twin:
        try:
            errors += twin_checks(d)
        except TwinParseError as e:
            # Reported as a failure, never as a pass. See the note above
            # TwinParseError: "could not look" and "nothing wrong" must not
            # produce the same exit code.
            errors.append(f"TWIN PARSE: {e}")
        errors += dashboard_checks(d)

    if errors:
        print("ck-dk-registry.json: FAIL")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("ck-dk-registry.json: OK")
    print(f"  Q_β c_k wired rungs: {ck_wired or 'none'} "
          f"(canonical only — flip-flop guard satisfied)")
    print(f"  m_p d_k wired rungs: {dk_wired or 'none'}")
    # Deliberately NOT printing production.dashboard_beats_100x here. It used
    # to, which made this validator a propagation route for the `2/7` framing
    # AGENTS.md forbids quoting as an accuracy result. Under --twin, T5 checks
    # that field against the witness instead.
    if twin:
        print("  twin (.md) agreement: T1 coverage, T2 tiers, T3 wiring, "
              "T4 pinned figures — all consistent")
        print("  twin-vs-witness: T5 dashboard counts consistent")
    else:
        print("  (JSON-internal only — pass --twin to compare the .md twin)")
    return 0


# --------------------------------------------------------------------------
# Self-test
# --------------------------------------------------------------------------
#
# A checker that has never been shown to fail is a checker you cannot read a
# green run from. Each case below perturbs ONE fact and asserts the matching
# check fires; the last asserts a structural change is reported as "cannot
# check" rather than as a pass.

def _expect(name: str, errs: list[str], token: str) -> bool:
    hit = any(token in e for e in errs)
    print(f"  {'PASS' if hit else 'FAIL'}  {name}")
    if not hit:
        print(f"        expected an error containing {token!r}, got: {errs}")
    return hit


def selftest() -> int:
    import copy
    print("ck_dk_registry_validate --selftest")
    d0 = json.loads(REGISTRY.read_text(encoding="utf-8"))
    ok = True

    # T2 — flip one rung's tier away from what the .md says.
    d = copy.deepcopy(d0)
    d["qbeta_ck_ladder"]["rungs"][0]["tier"] = "refuted"   # c_2 is CANONICAL
    ok &= _expect("T2 fires on a tier that disagrees with the .md",
                  twin_checks(d), "T2")

    # T1 — add a rung the .md has no row for.
    d = copy.deepcopy(d0)
    d["qbeta_ck_ladder"]["rungs"].append(
        {"rung": "99", "tier": "open", "wired": False})
    ok &= _expect("T1 fires on a JSON rung with no .md row",
                  twin_checks(d), "T1")

    # T3 — claim a wiring §6 does not state.
    d = copy.deepcopy(d0)
    d["production"]["qbeta_wired_rungs"] = ["2", "3"]
    ok &= _expect("T3 fires on a wiring the .md §6 does not state",
                  twin_checks(d), "T3")

    # T5 — quote a dashboard count the witness does not support.
    d = copy.deepcopy(d0)
    d["production"]["dashboard_beats_100x"] = 99
    ok &= _expect("T5 fires on a dashboard count the witness contradicts",
                  dashboard_checks(d), "T5 JSON")

    # T4 — the case this was written for: the real 4.6e6 -> 3.84e6 drift.
    # Exercised on the extractor directly, since it is the JSON *text* that
    # carries the figure.
    try:
        a = _figure("dc_3/dq ~ 4.6e6", _SLOPE, "x")
        b = _figure("dc_3/dq ≈ 3.84×10⁶", _SLOPE, "x")
        hit = abs(a - b) > 0.02 * max(a, b)
        print(f"  {'PASS' if hit else 'FAIL'}  T4 separates 4.6e6 from 3.84e6 "
              f"({a:g} vs {b:g})")
        ok &= hit
    except TwinParseError as e:
        print(f"  FAIL  T4 extractor: {e}")
        ok = False

    # The forbidden-field check must distinguish CITING the field from
    # EXPLAINING that it must not be cited. Both directions, because getting
    # only one right is how the #5923 tripwire shipped.
    fires = "beats_100x_count" in _assertive(
        "- L2 dashboard: **2/7** (`summary.beats_100x_count = 2`)")
    quiet = "beats_100x_count" not in _assertive(
        "> Corrected: it cited `beats_100x_count`, which AGENTS.md forbids.")
    print(f"  {'PASS' if fires else 'FAIL'}  forbidden-field check fires on an "
          f"authoritative citation")
    print(f"  {'PASS' if quiet else 'FAIL'}  ...and stays silent on the note "
          f"explaining the ban")
    ok &= fires and quiet

    # Parser failure must be loud. A twin whose table shape changed has to
    # report "cannot check", not an empty (green) result.
    try:
        _md_rungs("no table here at all", "c")
        print("  FAIL  parser returns empty instead of raising")
        ok = False
    except TwinParseError:
        print("  PASS  a shape change raises rather than reporting zero")

    print("selftest:", "OK" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
