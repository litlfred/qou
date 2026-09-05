"""Turn the dps-floor scope scan into a regeneration queue (bean `qou-zbws`).

Maps each moving producer to the witness stem it writes, so the regeneration
phase is a list of commands rather than a research task. Static: reads source
and the scope audit's JSON, runs no producer.

Emits TWO artefacts from one scan, so they cannot drift apart:

    docs/audits/2026-09-03-dps-floor-regeneration-queue.md   human queue
    .work/dps-floor-regen-set.json                           machine set

The second is the input to

    scripts/regenerate-convention-c-witnesses.py --run \
        --from .work/dps-floor-regen-set.json \
        --journal .work/dps-floor-regen.jsonl

which is the harness that actually runs them: strictly serial, resumable,
process-grouped, and dependency-ordered so an upstream witness is rewritten
before its readers. Do not hand-roll a second runner.

## 2026-09-04 — why this file was rewritten

It used to read four files -- `tier1.txt`, `tier2.txt`, `tier1c.txt` and
`tier2c.txt` -- produced by hand from `q_parameter_dps_floor_scope.py --list`
and kept in a scratchpad directory. That directory is per-session and does not
survive a container reclaim, so the generator became unrunnable the moment the
container it was written in went away. That is exactly what happened, and the
queue could not be refreshed after merging `origin/main`.

It now takes the scope audit's own `--json` and derives every bucket from it.
One scan, no intermediate files, reproducible in a fresh container.

The counts in the generated prose are computed, not typed. The previous version
carried them as literals ("all 264 moving producers", "229 ... 35", "183 in
all", "813 of 3104") and every one was stale after the merge.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SCOPE = os.path.join(HERE, "q_parameter_dps_floor_scope.py")

#: `WitnessBuilder("stem")` and any literal `"foo.witness.json"`. Both forms
#: occur; keying on only the first misses producers that write through a
#: helper but name the file.
STEM = re.compile(r'WitnessBuilder\(\s*[\'"]([A-Za-z0-9._\-/]+)[\'"]')
LIT = re.compile(r'[\'"]([A-Za-z0-9._\-/]+)\.witness\.json[\'"]')

#: A producer that emits a witness at all. Guards the filename fallback below.
EMITS = re.compile(r"WitnessBuilder\s*\(|WitnessBuilder\.wrap_legacy\s*\(")
#: `WitnessBuilder.wrap_legacy("stem", ...)` -- the literal form above does not
#: match this, because the stem does not follow `WitnessBuilder(` directly.
WRAP = re.compile(r'WitnessBuilder\.wrap_legacy\(\s*[\'"]([A-Za-z0-9._\-/]+)[\'"]')
#: `{"name": "stem", ...}` in a wrap_legacy payload.
NAMEKEY = re.compile(r'[\'"]name[\'"]\s*:\s*[\'"]([A-Za-z0-9._\-/]+)[\'"]')

#: Trees whose witnesses are copies, not outputs: never attribute to a producer.
_SKIP_TREES = ("_deprecated", "qou-mass/")

_ONDISK = None


def _ondisk():
    """basename -> [repo-relative path] for every live witness."""
    global _ONDISK
    if _ONDISK is None:
        _ONDISK = {}
        for dirpath, _dirs, files in os.walk(ROOT):
            for fn in files:
                if not fn.endswith(".witness.json"):
                    continue
                rel = os.path.relpath(os.path.join(dirpath, fn), ROOT)
                if any(s in rel for s in _SKIP_TREES):
                    continue
                _ONDISK.setdefault(fn, []).append(rel)
    return _ONDISK


def _name_candidates(rel):
    """Witness basenames a producer's FILENAME could imply.

    Producers written as `WitnessBuilder(Path(__file__).stem, ...)` name their
    witness after themselves, with underscores usually but not always turned
    into dashes and a trailing `_probe`/`_test` usually but not always dropped.
    All variants are tried and only ones that EXIST are kept.
    """
    base = os.path.splitext(os.path.basename(rel))[0]
    out = set()
    for b in (base, base.replace("_probe", ""), base.replace("_test", "")):
        for v in (b, b.replace("_", "-")):
            out.add(v + ".witness.json")
    return out

#: Buckets whose producers move. `raises` already sets its own precision and
#: `no_mp` builds no mpmath values, so neither is in scope.
MOVING = ("moves_own_mp", "moves_via_helper")


def stems(rel):
    """Witness basenames `rel` writes, or [] when none can be established.

    Four routes, in decreasing directness. The first two are what the producer
    literally says; the last two are INFERENCES and are therefore accepted only
    when the file they name exists on disk.

    The filename fallback is gated on the producer actually constructing a
    WitnessBuilder, and that guard is load-bearing rather than tidy. Without it,
    `per_irrep_pole_deuteron_h6.py` -- which builds no witness of its own --
    matches `per-irrep-pole-deuteron-h6.witness.json` by name and gets credited
    with a file that `per_irrep_pole_atom.py` actually writes. Regenerating the
    wrong producer for a witness is worse than leaving the stem unresolved: the
    queue then reports coverage it does not have.
    """
    try:
        with open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace") as fh:
            src = fh.read()
    except OSError:
        return []
    out = []
    for s in STEM.findall(src):
        out.append(s if s.endswith(".witness.json") else s + ".witness.json")
    for s in LIT.findall(src):
        out.append(s + ".witness.json")
    if out:
        return list(dict.fromkeys(out))
    if not EMITS.search(src):
        return []                       # emits nothing: not a regeneration target
    disk = _ondisk()
    for s in WRAP.findall(src):
        n = s if s.endswith(".witness.json") else s + ".witness.json"
        out += disk.get(n, [])
    if not out:
        for s in NAMEKEY.findall(src):
            out += disk.get(s + ".witness.json", [])
    if not out:
        for c in _name_candidates(rel):
            out += disk.get(c, [])
    return [os.path.basename(p) for p in dict.fromkeys(out)]


def load_scope(path=None):
    """The scope audit's JSON. Runs the audit when no path is given.

    The scan walks ~4200 files and takes a couple of minutes, so a caller
    iterating on this file's OUTPUT should run the audit once, keep the JSON,
    and pass `--scope-json`.
    """
    if path:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    res = subprocess.run([sys.executable, SCOPE, "--json"],
                         capture_output=True, text=True, check=True)
    return json.loads(res.stdout)


def rows_from(scope):
    """[(tier_label, producer, stems, cone, bucket)] over both import cones."""
    out = []
    for cone_key, cone_label in (("cone_q_parameter", "q_parameter"),
                                 ("cone_constants_only", "constants_only")):
        for e in scope["detail"][cone_key]:
            if e["bucket"] not in MOVING:
                continue
            tier = "1-definite" if e["bucket"] == "moves_own_mp" else "2-probable"
            if cone_label == "constants_only":
                tier += " (constants-only cone)"
            out.append((tier, e["file"], stems(e["file"]), cone_label, e["bucket"]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scope-json", metavar="PATH",
                    help="output of q_parameter_dps_floor_scope.py --json; "
                         "the audit is run if omitted (~2 min)")
    a = ap.parse_args()

    scope = load_scope(a.scope_json)
    rows = rows_from(scope)
    with_w = [r for r in rows if r[2]]
    without = [r for r in rows if not r[2]]

    n_qp = sum(1 for r in rows if r[3] == "q_parameter")
    n_co = sum(1 for r in rows if r[3] == "constants_only")
    wb = scope["witnesses_by_bucket"]
    w_own, w_via = wb.get("moves_own_mp", 0), wb.get("moves_via_helper", 0)
    w_tot = wb.get("_witness_files_total", 0)
    w_orphan = wb.get("_no_producer_found", 0)

    print(f"moving producers: {len(rows)}  "
          f"(q_parameter cone {n_qp}, constants-only cone {n_co})")
    print(f"  witness stem resolved: {len(with_w)}   unresolved: {len(without)}")
    print(f"  witnesses attributed : {w_own + w_via}  "
          f"(tier 1 {w_own}, tier 2 {w_via})")

    out = [
        "# dps-floor regeneration queue (bean `qou-zbws`)",
        "",
        "Generated by `computations/audits/dps_floor_regeneration_queue.py`",
        "from `q_parameter_dps_floor_scope.py --json`. Static: it reads source",
        "and runs nothing. Every count below is computed by that generator, not",
        "typed — an earlier version carried them as literals and all of them",
        "were stale within a day.",
        "",
        "Landing the 50-dps floor moved these producers from mpmath's default 15",
        "dps to 50, so the numbers in the witnesses they emit change in their",
        "trailing digits. **Tier 1** build their own mpmath values and never raise",
        "dps — their numbers definitely move. **Tier 2** reach mpmath through a",
        "helper and probably move.",
        "",
        "## How to run this queue",
        "",
        "Do NOT work down the checkboxes by hand, and do not write a runner.",
        "`scripts/regenerate-convention-c-witnesses.py` already is one, and it",
        "handles the three things a hand-run gets wrong:",
        "",
        "```sh",
        "python3 scripts/regenerate-convention-c-witnesses.py --run \\",
        "    --from .work/dps-floor-regen-set.json \\",
        "    --journal .work/dps-floor-regen.jsonl --timeout 600",
        "```",
        "",
        "- **Serial.** Standing rule: never two producers at once in one",
        "  checkout. It takes a lock, and it runs each producer in its own",
        "  process group so killing the harness cannot orphan a producer that",
        "  then races the next one onto the same witness.",
        "- **Dependency-ordered.** Producers read each other's witnesses.",
        "  Alphabetical order regenerates downstream producers against STALE",
        "  upstream data and every one of them still reports success.",
        "- **Resumable.** One journal line per producer; a restart costs one",
        "  producer, not the run. The container is ephemeral.",
        "",
        "## What this queue does and does not cover",
        "",
        f"- **Both import cones, all {len(rows)} moving producers.** {n_qp} reach",
        "  `qou_substrate.constants` through the `q_parameter` shim; "
        f"{n_co} reach it",
        "  directly and are listed under the \"constants-only cone\" headings.",
        "  The other cone is not a residue to wave at: it was precisely the",
        "  argument for landing the floor in `constants.py` rather than in the",
        "  shim, so omitting it would have reintroduced the hole that placement",
        "  decision closed.",
        f"- **Not every producer here has a resolvable witness stem** "
        f"({len(without)} do not).",
        "  Those are listed in their own section: the stem is built dynamically,",
        "  written by a helper, or the producer emits none. Each needs a look,",
        "  not a guess.",
        "- **Witness counts, not producer counts, are what matters downstream.**",
        f"  The scope audit attributes {w_own} witnesses to tier 1 and {w_via} to",
        f"  tier 2, {w_own + w_via} in all — and could not attribute {w_orphan} of",
        f"  {w_tot} witnesses to any producer, so {w_own + w_via} is a LOWER bound",
        "  on what actually moves.",
        "- **Tier 2 is \"probably\", not \"definitely\".** A producer reaching mpmath",
        "  through a helper may or may not have its emitted numbers change. The",
        "  cheapest discriminator is to regenerate and diff, not to reason about",
        "  it.",
        "",
    ]
    for tier in ("1-definite", "2-probable",
                 "1-definite (constants-only cone)",
                 "2-probable (constants-only cone)"):
        sel = [r for r in with_w if r[0] == tier]
        out += [f"## Tier {tier} — {len(sel)} producers", ""]
        for _t, f, st, _c, _b in sorted(sel):
            out.append(f"- [ ] `{f}` -> "
                       + ", ".join("`" + s + "`" for s in st[:3]))
        out.append("")
    if without:
        out += [f"## No witness stem found by static scan — {len(without)}", "",
                "These are in the moving set but the scan could not name their",
                "witness (dynamic stem, helper-written, or they emit none).", ""]
        for _t, f, _st, _c, _b in sorted(without):
            out.append(f"- [ ] `{f}` — resolve stem by hand")
        out.append("")

    doc_path = os.path.join(
        ROOT, "docs/audits/2026-09-03-dps-floor-regeneration-queue.md")
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = doc_path
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print("wrote docs/audits/2026-09-03-dps-floor-regeneration-queue.md")

    # The machine set, in the harness's own schema, from the SAME scan.
    set_path = os.path.join(ROOT, ".work/dps-floor-regen-set.json")
    os.makedirs(os.path.dirname(set_path), exist_ok=True)
    payload = {
        "schema": "convention-d-blast-radius/v1",
        "note": "dps-floor regeneration set (bean qou-zbws), generated by "
                "computations/audits/dps_floor_regeneration_queue.py",
        "producers": [
            {"producer": f, "writes": st, "cone": cone,
             "tier": 1 if bucket == "moves_own_mp" else 2}
            for _t, f, st, cone, bucket in sorted(with_w)
        ],
    }
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = set_path
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(payload, indent=1))
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"wrote .work/dps-floor-regen-set.json "
          f"({len(payload['producers'])} producers, "
          f"{sum(len(p['writes']) for p in payload['producers'])} witnesses)")

    nostem_path = os.path.join(ROOT, ".work/dps-floor-regen-nostem.json")
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = nostem_path
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(
            [{"producer": f, "cone": cone,
              "tier": 1 if bucket == "moves_own_mp" else 2}
             for _t, f, _st, cone, bucket in sorted(without)], indent=1))
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"wrote .work/dps-floor-regen-nostem.json ({len(without)} producers)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
