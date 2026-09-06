#!/usr/bin/env python3
# polynomial_q_not_applicable: static classifier over witness diffs.
"""Classify what a witness regeneration actually changed.

Owner directive: NO FLOAT64 — this is the guard that decides whether a
regenerated witness may be committed.

## Why a classifier and not a diff

Re-running a producer changes a witness for several distinct reasons, and they
carry opposite verdicts:

| verdict | meaning | commit? |
|---|---|---|
| `DECLARED` | `upstream_witness_hashes` appeared; nothing else but metadata moved | yes |
| `ANCHOR_MIGRATION` | the witness's own q₀ moved muon → proton, and every other change is bounded | yes |
| `ANCHOR_MIGRATION_INFERRED` | no q₀ field exists to flip, but the producer re-anchors to proton and every move is inside the bound | **review** |
| `VALUES` | something moved that neither of the above explains | **no** |
| `NOCHANGE` | ran, nothing new | n/a |

`ANCHOR_MIGRATION` exists because of a measurement: 650 witnesses carry a
muon-anchored q₀ against 379 proton, and producers read `Q` from
`q_parameter`, which is proton-anchored. **Re-running a producer therefore
re-anchors it automatically** — observed in `braid-encoding-audit`, whose 87
moved fields were all one substitution, `-h/2` at the muon anchor
(`-0.10453016099779683`) to `-h/2` at the proton anchor
(`-0.10453014939781968`).

A classifier without this verdict reverts that as drift, which is what the
first version of this guard did: it would have discarded a correct migration
and quietly held the corpus on a retired anchor.

## The bound, and why it is evidence-gated

Anchor migration is only accepted when the witness itself shows the flip — a
q₀-valued field going from the muon prefix to the proton prefix. Small
movement alone is never enough. That matters because a *different* 1e-4-scale
change exists in this corpus and must not be waved through: the
colour-weighted vs colour-blind crossing convention moves `tr_M(4He)` by
182 ppm with no anchor change at all. Requiring positive evidence of the flip
separates them; a bound alone would not.

## Where the evidence gate cannot fire, and what replaces it

Measured (P50 in `docs/audits/2026-08-07-producer-repadding-empirical-sweep.md`,
then re-measured over the fuller producer set once witness-to-producer matching
stopped relying on the filename stem): of **159 declaring producers, 78 have a
witness carrying no q₀-valued field at all** — 49%. There is nothing there to
flip, so a genuine re-anchoring can only ever classify `VALUES` and be
reverted; the verdict added to stop the guard discarding correct migrations
still discards them for half the corpus.

The fuller measurement is what makes that a finding rather than a sampling
artefact. P50 measured the stem-matchable producers only, and a stem rule is
exactly the kind of sample that could have been biased — producers whose
witness is named after the script might plausibly differ from those whose is
not. Resolving the remainder moved the ratio from 51% to 49%, i.e. not at all.
The gate's blindness is a property of the corpus, not of how it was counted.

And it is structural rather than transient: `WitnessBuilder.save` carries a
recorded pin forward but never invents one, so a witness with no pin does not
acquire one by being re-run. Measured on the 42 witnesses the first full wave
kept — 18 of them carry no q₀ field before regeneration and still carry none
after.

`ANCHOR_MIGRATION_INFERRED` covers exactly that population, on two pieces of
circumstantial evidence in place of the missing direct one:

1. `resolve_q0_anchor(<producer>)` reports **proton**, so `q_parameter` hands
   the producer the proton pin and a re-run re-anchors it; and
2. every moved field is numeric and inside the same 1e-5 collateral bound.

The magnitudes are what make (2) load-bearing rather than decorative: an anchor
migration moves ~1e-7 relative, the crossing-convention change moves 1.8e-4,
and the bound sits at 1e-5 — an order of magnitude clear of each. That is the
same separation the strict path relies on for its collateral, applied here to
the whole diff.

**It is deliberately a weaker claim, and it is deliberately a separate verdict.**
Folding it into `ANCHOR_MIGRATION` would launder circumstantial evidence into
direct evidence and auto-commit the result. It is not in `witness_regen_wave`'s
`KEEP` set, so the driver reverts these like any other reject — the verdict's
whole job is to say *why* it was reverted, so a human can look at a named,
bounded, anchor-shaped population instead of an undifferentiated `VALUES` pile.
For the same reason the CLI exits non-zero on it.

A witness that *does* carry a q₀-valued field never reaches this path — if the
evidence could be there and is not, its absence is itself informative, and the
strict verdict stands.

**It is direction-blind, and that is the reason it can never be promoted into
`KEEP`.** The strict path reads direction off the flip and rejects a
proton → muon reverse. With no q₀ field there is no direction to read, so a
migration and its revert are the same diff to this verdict — measured on
99561ee6, a revert commit, which classifies as inferred exactly like a forward
re-anchoring would. A human looking at the named file can tell; the classifier
cannot.

Usage:
    python3 computations/witness_regen_classify.py <witness.json> [--base REF]
    python3 computations/witness_regen_classify.py --self-test
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# Stamped every run; never evidence of a real change.
#
# THE PRINCIPLE, so this stays a rule and not a list that grows until the
# light turns green: a field belongs here when it describes *how, when or by
# what* the computation ran — never *what it computed*. `description` is prose
# about the method; `engine`, `scriptFile`, `_provenance` are provenance;
# `computedAt` is a timestamp. None of them can make a number right or wrong.
# `convention` fails the test and is deliberately excluded: it changes what the
# numbers MEAN, worth 182 ppm in tr_M(4He).
#
# Two entries earned their place the hard way and are worth naming:
#
# `engine` — leaving it out made the classifier reject a genuine deuteron
# ANCHOR_MIGRATION because a string moved: the numerics were inside the bound
# and the q₀ flip was present, but the engine label changed from the fallback
# path to the native one. Exactly the provenance churn a regeneration produces.
#
# `scriptFile` — metadata here by separation of concerns, not indifference.
# `witness_provenance_audit` polices whether a scriptFile claim is *true* (it
# found five false ones); this classifier only asks whether a VALUE moved.
META = {
    "computedAt", "commitSha", "scriptHash", "scriptCommitSha", "scriptFile",
    "durationMs", "description",
    "engineVersion", "engine", "environment", "generatedAt", "timestamp",
    "upstream_witness_hashes", "precisionMetadata", "compute_time_sec",
    "compute_time_sec_so_far", "_provenance", "convention_inferred_by",
    # Wall-clock, by the PRINCIPLE above and not to make a light turn green:
    # each says how LONG the computation ran, never what it computed. They
    # were missing while `compute_time_sec` and `durationMs` were present, so
    # the rule was already established and these four were simply the spellings
    # nobody had hit yet. Counts in the corpus: elapsed_s 127, elapsed_sec 64,
    # time_sec 42, wall_sec 37.
    #
    # Not cosmetic. A timing field re-times on every run and moves by O(1)
    # relative, so one of them anywhere in a diff pushes the whole witness past
    # any numeric bound — `binding-canonical` was rejected on
    # `data.results[atom=3He].wall_sec` while its 27 real fields had moved only
    # at the float64 floor.
    "wall_sec", "elapsed_s", "elapsed_sec", "time_sec",
}

MUON_PREFIX = "1.109978595"
PROTON_PREFIX = "1.109978582"

# Ceiling on collateral movement in an accepted anchor migration. The q₀ shift
# is ~1.15e-8 relative; amplification through a producer is bounded well under
# this. Deliberately BELOW the 1.8e-4 crossing-convention shift, so that
# convention change can never be mistaken for an anchor migration.
ANCHOR_COLLATERAL_MAX = 1e-5

# A move at or below this is not physics — it is the float64 -> 50-dps upgrade.
#
# Sized by what it must separate, not by taste. An f64 substrate constant
# carries ~17 significant digits, so replacing it with the exact 50-dps value
# moves any derived quantity by ~1e-16 relative times its sensitivity. The
# smallest thing that is a REAL change here is a discrete one — a partition
# index, an assertion count, an argmax — and those move by O(1) relative when
# they move at all. Four orders above f64 noise and eleven below a discrete
# flip leaves no plausible physics in the gap.
#
# Deliberately NOT reusing ANCHOR_COLLATERAL_MAX (1e-5): that bound is sized
# for anchor collateral, which is 1e-7-ish, and would wave through changes
# nine orders larger than anything this verdict is meant to describe.
SUBFLOAT_MAX = 1e-12


# Keys that identify a record within a list, tried in order. A list of dicts
# each carrying one of these is addressed by identity rather than position.
IDENTITY_KEYS = ("partition", "lambda", "name", "id", "atom", "key", "label")


def _identity(v) -> str | None:
    """Stable identity for a record in a list, or None to fall back to index."""
    if not isinstance(v, dict):
        return None
    for k in IDENTITY_KEYS:
        if k in v:
            iv = v[k]
            return f"{k}={iv}" if not isinstance(iv, list) else f"{k}={tuple(iv)}"
    return None


def flatten(obj, path="", out=None) -> dict:
    """Flatten a witness to path -> scalar, addressing list records by identity.

    **Index addressing was a real defect, not a nicety.** The ⁴He rebuild
    reorders `by_partition` and gives each entry a new `dim` key. Under
    positional addressing that misaligns all 77 entries at once, so a clean
    anchor migration reported 560 moved fields and was rejected on
    `by_partition[0].dim` — the verdict honest about what it saw and wrong
    about what happened. Any producer that merely reorders its output would
    read the same way.

    So a list whose records carry an identity key is keyed by it:
    `by_partition[partition=(7, 4, 1)].chi_lambda` compares like with like
    however the list is ordered. Lists without one keep index addressing, which
    is correct for genuinely positional data.

    Falls back to index if identities are not unique — a repeated identity
    would silently collapse entries, and losing a field is worse than
    misaligning one.
    """
    out = {} if out is None else out
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in META:
                continue
            flatten(v, f"{path}.{k}" if path else k, out)
    elif isinstance(obj, list):
        ids = [_identity(v) for v in obj]
        keyed = all(i is not None for i in ids) and len(set(ids)) == len(ids)
        for i, v in enumerate(obj):
            flatten(v, f"{path}[{ids[i] if keyed else i}]", out)
    else:
        out[path] = obj
    return out


def _num(v):
    try:
        return float(str(v).strip())
    except (TypeError, ValueError):
        return None


# Literal anchor labels. `q0Anchor` carries these directly, and a witness
# saying "muon" -> "proton" is the strongest evidence of a migration there is —
# stronger than inferring it from a numeric prefix. Rejecting it as "a
# non-numeric field moved" is exactly backwards, and did reject a genuine
# deuteron migration until this was added.
_MUON_LABELS = {"muon", "ideal_muon", "ideal-muon"}
_PROTON_LABELS = {"proton"}
# Labels meaning "not established". A witness moving from one of these TO a
# definite anchor is a provenance *resolution*, not a value change — and it is
# what stamping `q0Anchor` properly produces where the old file only ever had
# "ambiguous". Accepted only when a numeric q₀ flip is independently present;
# the reverse (definite -> unknown) is a loss and stays rejected.
_UNKNOWN_LABELS = {"ambiguous", "unknown", "none", ""}


def _is_unknown_label(v) -> bool:
    return str(v).strip().lower() in _UNKNOWN_LABELS or v is None


def _resolve_anchor(script) -> str | None:
    """Which q₀ pin `q_parameter` would hand this producer, or None.

    Imported lazily and defensively. This module is otherwise dependency-free
    and runs as a bare guard in contexts where `qou_substrate` is not on the
    path; an import error there must degrade to "cannot infer" (⇒ `VALUES`),
    never to a crash and never to a permissive default.

    The in-repo substrate is added to `sys.path` as a fallback because the
    degrade is *silent* — `VALUES` is also the honest answer for a genuine
    value change, so a missing import looks exactly like the verdict correctly
    declining, and the whole population goes quietly unclassified. That is not
    hypothetical: `witness_regen_wave` builds a PYTHONPATH for the producer
    subprocesses but calls `classify` in its own process, which puts only
    `computations/` on the path. Measured before this fallback existed: with
    `qou_substrate` off the path the resolver returns None for every producer
    and the verdict never fires at all.
    """
    for attempt in (0, 1):
        try:
            from qou_substrate.witness import resolve_q0_anchor  # noqa: PLC0415
            return resolve_q0_anchor(script)[0]
        except Exception:  # noqa: BLE001
            if attempt:
                return None
            p = str(ROOT / "tools/qou-substrate/python")
            if p in sys.path:
                return None
            sys.path.append(p)
    return None


def _script_of(old: dict, new: dict) -> str | None:
    """The producer named by the witness pair, preferring the new one.

    `scriptFile` is a bare basename in this corpus, which is all
    `resolve_q0_anchor` needs (it keys on the stem). It is also a claim the
    witness makes about itself, and `witness_provenance_audit` has found false
    ones — tolerable here only because this verdict is not auto-kept. A
    mislabelled producer yields a wrong INFERRED tag on something a human is
    already being asked to look at, not a bad commit.
    """
    for src in (new, old):
        v = (src or {}).get("scriptFile")
        if isinstance(v, str) and v.strip():
            return v.strip()
    return None


def _anchor_of(v) -> str | None:
    s = str(v).strip()
    if s in _MUON_LABELS:
        return "muon"
    if s in _PROTON_LABELS:
        return "proton"
    if s.startswith(MUON_PREFIX):
        return "muon"
    if s.startswith(PROTON_PREFIX):
        return "proton"
    return None


def _subfloat_move(a: dict, b: dict, moved: list) -> dict | None:
    """`SUBFLOAT_MOVE` when every move is below the float64 floor.

    Named for what is MEASURED, not for what is intended. It was
    `PRECISION_GAIN` until the padding-stripping fixture landed here: that diff
    goes the other way — "2.029883212819307392038581383530981838703155517578125"
    (a float64's exact expansion, printed as if it were 50 dps) becoming the
    honest "2.0298832128193074". Both directions move the stored decimal by
    ~1e-17 and neither changes any physics, so a bound on magnitude cannot tell
    them apart and a name claiming "gain" would have been asserting a direction
    it never checked.

    The float64 sweep (bean qou-tj98) replaced f64 substrate constants with
    their exact 50-dps partners across ~120 producers. Re-running those
    producers moves values by ~1e-16 relative — a strict improvement, and not
    an anchor migration, so without this verdict every one of them classified
    as VALUES and was REVERTED. The first regeneration wave did exactly that:
    22 witnesses rejected under "a q0-valued field exists but did not flip",
    each of them a witness whose q0 had simply gained its missing 33 digits.

    Bounded rather than trusted. A discrete change — a partition index, an
    argmax, an assertion count — moves by O(1) relative and is excluded, which
    matters: the same wave surfaced `per_n.13.argmax_shape[1]` flipping, where
    a near-degenerate tie had been decided by float noise. That is a genuine
    finding and must stay VALUES for a human to read, not be absorbed as
    "precision".

    Non-numeric moves are excluded outright: text has no magnitude to bound.

    Compared in `Decimal`, not through `_num`. `_num` goes via `float()`, and
    the whole point of this diff is digits BEYOND float64 — "1.1099785827513808"
    and "1.1099785827513808075916690956107688798744991218736" are the same
    float64, so a float comparison reports the move as exactly zero and the
    change becomes invisible to the very verdict meant to describe it.
    Measuring a precision gain with the precision that was gained does not work.
    """
    from decimal import Decimal, InvalidOperation, localcontext
    worst = Decimal(0)
    with localcontext() as ctx:
        ctx.prec = 80
        for k in moved:
            try:
                x, y = Decimal(str(a.get(k)).strip()), Decimal(str(b.get(k)).strip())
            except (InvalidOperation, TypeError, ValueError):
                return {"_declined": f"non-numeric move at {k}"}
            rel = abs(y - x) / (abs(x) if x else Decimal(1))
            if rel > Decimal(repr(SUBFLOAT_MAX)):
                return {"_declined": f"{k} moved {float(rel):.3g}, above the "
                                     f"{SUBFLOAT_MAX:g} sub-float64 floor"}
            worst = max(worst, rel)
    if worst <= 0:
        return {"_declined": "no value moved"}
    worst = float(worst)
    return {"verdict": "SUBFLOAT_MOVE", "moved": len(moved), "flips": 0,
            "worst": worst,
            "reason": (f"every move <= {SUBFLOAT_MAX:g} relative "
                       f"(worst {worst:.3g}) — the f64 -> 50-dps upgrade"),
            "sample": moved[:5]}


def _infer_migration(a: dict, b: dict, moved: list, old: dict, new: dict,
                     script, resolve) -> dict | None:
    """`ANCHOR_MIGRATION_INFERRED`, or `{"_declined": <why>}` when not that.

    Every gate below is a *reason not to infer*. None of them may be relaxed
    into "probably fine": the whole verdict exists because direct evidence is
    unavailable, so the circumstantial substitutes have to be exact.

    Each declines with the reason it declined for, and `classify` carries that
    string onto the VALUES verdict it falls back to. Returning a bare None was
    measurably worse than useless: the 51 VALUES of wave 3 then all reported
    the caller's default, "no q0-valued field flipped muon -> proton", which is
    the *outer* condition every one of them satisfies and names no gate at all.
    A population that large reported under one indistinguishable label is a
    population nobody can triage, and it had to be re-run to find out why.
    """
    # 1. Only where the strict gate is structurally unable to fire. A witness
    #    carrying any q0-valued field — on either side, flipped or not — could
    #    have shown the migration and did not, and that silence is evidence.
    if any(_anchor_of(v) is not None for v in (*a.values(), *b.values())):
        return {"_declined": "a q0-valued field exists but did not flip"}

    # 2. The producer must be one a re-run actually re-anchors. `ideal_muon`
    #    producers (257 of them in the manifest) keep the muon pin, so movement
    #    in their output is not an anchor migration by any reading.
    #
    #    Measured caveat, pinned at 13ff8207: this gate currently rejects
    #    nothing it is ever asked about. Of 163 declaring producers, 13 resolve
    #    to muon and all 13 have a witness carrying a q0 field, so they are
    #    already stopped by gate 1. Every producer that reaches here resolves
    #    to proton. It is kept because the manifest is editable and the
    #    condition is the one the verdict actually claims — but the numeric
    #    gates below, not this one, are doing the discriminating today. Do not
    #    read a passing gate 2 as independent corroboration.
    script = script or _script_of(old, new)
    if not script:
        return {"_declined": "witness names no producer"}
    anchor = (resolve or _resolve_anchor)(script)
    if anchor != "proton":
        return {"_declined": f"{script} resolves to "
                             f"{anchor or 'no'} anchor, not proton"}

    # 3. Every move numeric and inside the collateral bound. A non-numeric
    #    change has no magnitude to compare against 1e-5, so it can never be
    #    excluded by it — `convention` flipping colour-blind to colour-weighted
    #    is exactly that, and must not slip through as "small".
    worst, worst_at = 0.0, None
    for k in moved:
        x, y = _num(a.get(k)), _num(b.get(k))
        if x is None or y is None:
            return {"_declined": f"non-numeric move at {k}"}
        rel = abs(y - x) / (abs(x) if x else 1.0)
        if rel > ANCHOR_COLLATERAL_MAX:
            return {"_declined": f"{k} moved {rel:.3g}, above the "
                                 f"{ANCHOR_COLLATERAL_MAX:g} anchor bound"}
        if rel > worst:
            worst, worst_at = rel, k

    # 4. Something must actually have moved. Fields can differ as text and be
    #    numerically identical — stripping float64 padding rewrites
    #    "2.029883212819307392038581383530981838703155517578125" as
    #    "2.0298832128193074", and commit 0de68792 ("strip float64 padding …
    #    no value moved") did that to 58 witnesses at once. An anchor migration
    #    moves values; a diff whose largest move is exactly zero moved none, so
    #    there is nothing here to attribute to an anchor. Measured: without
    #    this gate, 24 of that commit's 58 files classified as inferred
    #    migrations. They are re-serialisations.
    if worst <= 0.0:
        return {"_declined": "text differs but no value moved; a "
                             "re-serialisation, not a migration"}

    return {"verdict": "ANCHOR_MIGRATION_INFERRED", "moved": len(moved),
            "flips": 0, "worst": worst, "worst_at": worst_at,
            "reason": (f"no q0-valued field to flip; {script} resolves to the "
                       f"proton anchor and the largest move is {worst:.3g} "
                       f"at {worst_at}, inside the "
                       f"{ANCHOR_COLLATERAL_MAX:g} bound"),
            "sample": moved[:5]}


def classify(old: dict, new: dict, script=None, resolve=None) -> dict:
    """Classify a witness regeneration.

    `script` / `resolve` override how the producer's q₀ anchor is looked up —
    the seam the self-tests use so the verdict policy stays testable without a
    manifest on disk. Both default to reading the witness's own `scriptFile`
    and `qou_substrate.witness.resolve_q0_anchor`, so the two-argument call the
    driver makes is unchanged.
    """
    a, b = flatten(old), flatten(new)
    moved = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
    gained = bool((new.get("data") or {}).get("upstream_witness_hashes")) and \
        not bool((old.get("data") or {}).get("upstream_witness_hashes"))

    if not moved:
        return {"verdict": "DECLARED" if gained else "NOCHANGE",
                "moved": 0, "flips": 0}

    # A diff that only ADDS fields moved no value — nothing that existed
    # changed. This is what restoring the fields a rebuild used to drop looks
    # like (`producer`, `n_partitions_total`, `partial`), and lumping it in
    # with VALUES would report a strict provenance gain as drift.
    #
    # Reported, not auto-kept: an added field could still carry a wrong new
    # value, and this verdict only certifies that nothing OLD moved. Removals
    # are not covered — those stay rejections, since losing a field is the
    # defect this pair of rules exists to tell apart from gaining one.
    if all(k not in a for k in moved):
        return {"verdict": "SCHEMA_GAIN", "moved": len(moved), "flips": 0,
                "added": sorted(moved)[:8]}

    # Positive evidence: a q0-valued field flipped muon -> proton.
    flips = [k for k in moved
             if _anchor_of(a.get(k)) == "muon" and _anchor_of(b.get(k)) == "proton"]
    if not flips:
        precise = _subfloat_move(a, b, moved)
        if "_declined" not in precise:
            return precise
        inferred = _infer_migration(a, b, moved, old, new, script, resolve)
        if "_declined" not in inferred:
            return inferred
        # Prefer the sub-float64 gate's reason when the inference gate only
        # declined on the outer "a q0-valued field exists" condition: the
        # former names the field and magnitude that actually blocked, the
        # latter names a property most of this population shares.
        if inferred["_declined"].startswith("a q0-valued field exists"):
            inferred = precise
        # Report the gate that declined, not the outer condition. "No flip"
        # is true of every witness that reaches here and so distinguishes none
        # of them; the gate is what a reader can act on.
        return {"verdict": "VALUES", "moved": len(moved), "flips": 0,
                "reason": inferred["_declined"], "sample": moved[:5]}

    # Every other movement must be bounded, and none may go the wrong way.
    for k in moved:
        if _anchor_of(a.get(k)) == "proton" and _anchor_of(b.get(k)) == "muon":
            return {"verdict": "VALUES", "moved": len(moved), "flips": len(flips),
                    "reason": f"reverse flip at {k}", "sample": [k]}
        # A label resolving from "ambiguous"/absent to the proton anchor is a
        # provenance gain, not movement. Only in this direction.
        if _is_unknown_label(a.get(k)) and _anchor_of(b.get(k)) == "proton":
            continue
        if _anchor_of(a.get(k)) == "proton" and _is_unknown_label(b.get(k)):
            return {"verdict": "VALUES", "moved": len(moved), "flips": len(flips),
                    "reason": f"anchor label lost at {k}", "sample": [k]}
        # A field that did not exist cannot have MOVED. Adding one is a schema
        # gain — `by_partition[…].dim` on the 4He rebuild — and vetoing on it
        # rejects clean migrations for enriching their own output.
        if k not in a:
            continue
        # Removing one is the opposite: a loss, and losses are never waved
        # through. The 4He rebuild drops `producer`, `tr_M_markov_peel_xref`,
        # `tr_M_dual_path_rel_gap`, `n_partitions_total` and `partial` that
        # HEAD carried, and that should surface rather than pass as churn.
        if k not in b:
            return {"verdict": "VALUES", "moved": len(moved), "flips": len(flips),
                    "reason": f"field removed at {k}", "sample": [k]}
        x, y = _num(a.get(k)), _num(b.get(k))
        if x is None or y is None:
            if a.get(k) != b.get(k) and k not in flips:
                return {"verdict": "VALUES", "moved": len(moved),
                        "flips": len(flips),
                        "reason": f"non-numeric change at {k}", "sample": [k]}
            continue
        denom = abs(x) if x else 1.0
        if abs(y - x) / denom > ANCHOR_COLLATERAL_MAX:
            return {"verdict": "VALUES", "moved": len(moved), "flips": len(flips),
                    "reason": (f"{k} moved {abs(y - x) / denom:.3g}, above the "
                               f"{ANCHOR_COLLATERAL_MAX:g} anchor bound"),
                    "sample": [k]}
    return {"verdict": "ANCHOR_MIGRATION", "moved": len(moved),
            "flips": len(flips)}


# witness-copy-intentional: these are this classifier's own self-test
# INPUTS, not values read from anywhere. Each pair reproduces a shape
# observed on a real witness (the braid-encoding-audit -h/2 flip, the
# deuteron engine-label case) so the verdict logic is pinned against it.
# Loading them from a witness would delete what the test tests.
CASES = [
    ("declaration only", {}, {}, True, "DECLARED"),
    ("nothing at all", {"a": 1}, {"a": 1}, False, "NOCHANGE"),
    ("clean anchor migration",
     {"q0": "1.1099785955573347", "x": 0.20906032199559366},
     {"q0": "1.1099785827513808", "x": 0.20906029879563937}, False,
     "ANCHOR_MIGRATION"),
    # The real braid-encoding-audit shape: -h/2 either side of the flip.
    ("braid-encoding-audit shape",
     {"q0": "1.1099785955573347", "d": -0.10453016099779683},
     {"q0": "1.1099785827513808", "d": -0.10453014939781968}, False,
     "ANCHOR_MIGRATION"),
    ("movement with NO anchor flip is never waved through",
     {"x": 0.05534834587669884}, {"x": 0.055358426266783106}, False, "VALUES"),
    # 182 ppm crossing-convention change, WITH a flip present: still rejected,
    # because it exceeds the collateral bound. This is the case the bound is
    # sized for.
    ("crossing-convention shift is not an anchor migration",
     {"q0": "1.1099785955573347", "tr_M": 0.05534834587669884},
     {"q0": "1.1099785827513808", "tr_M": 0.055358426266783106}, False,
     "VALUES"),
    ("reverse flip (proton -> muon) is rejected",
     {"q0": "1.1099785827513808"}, {"q0": "1.1099785955573347"}, False, "VALUES"),
    ("string field changing alongside a flip is rejected",
     {"q0": "1.1099785955573347", "note": "a"},
     {"q0": "1.1099785827513808", "note": "b"}, False, "VALUES"),
    # The deuteron case: a real anchor migration that the classifier rejected
    # because `engine` moved from the fallback label to the native one.
    ("engine label moving does not veto an anchor migration",
     {"q0": "1.1099785955573347", "engine": "python", "x": 0.20906032199559366},
     {"q0": "1.1099785827513808", "engine": "pyhecke_native",
      "x": 0.20906029879563937}, False, "ANCHOR_MIGRATION"),
    # ...but a convention change still must not.
    ("convention change is never an anchor migration",
     {"q0": "1.1099785955573347", "convention": "averaged-crossings"},
     {"q0": "1.1099785827513808",
      "convention": "colour-weighted-averaged-crossing"}, False, "VALUES"),
    ("q0Anchor label muon -> proton is evidence, not a veto",
     {"q0Anchor": "muon", "x": 0.20906032199559366},
     {"q0Anchor": "proton", "x": 0.20906029879563937}, False,
     "ANCHOR_MIGRATION"),
    ("q0Anchor proton -> muon is a reverse flip",
     {"q0Anchor": "proton"}, {"q0Anchor": "muon"}, False, "VALUES"),
    ("q0Anchor resolving ambiguous -> proton is a gain, not movement",
     {"q0": "1.1099785955573347", "q0Anchor": "ambiguous",
      "x": 0.20906032199559366},
     {"q0": "1.1099785827513808", "q0Anchor": "proton",
      "x": 0.20906029879563937}, False, "ANCHOR_MIGRATION"),
    ("losing a definite anchor label is rejected",
     {"q0": "1.1099785955573347", "q0Anchor": "proton"},
     {"q0": "1.1099785827513808", "q0Anchor": "ambiguous"}, False, "VALUES"),
    # The 4He shape: by_partition reordered and each entry gains `dim`.
    # Positional addressing misaligned all entries and vetoed on
    # by_partition[0].dim; identity addressing compares like with like.
    ("reordered list of records is not movement",
     {"q0": "1.1099785955573347",
      "by_partition": [{"partition": [2], "chi": 1.0},
                       {"partition": [1, 1], "chi": 2.0}]},
     {"q0": "1.1099785827513808",
      "by_partition": [{"partition": [1, 1], "chi": 2.0, "dim": 1},
                       {"partition": [2], "chi": 1.0, "dim": 1}]},
     False, "ANCHOR_MIGRATION"),
    # ...but a real move inside a reordered list must still be caught.
    ("reordered list hiding a real move is still caught",
     {"q0": "1.1099785955573347",
      "by_partition": [{"partition": [2], "chi": 1.0},
                       {"partition": [1, 1], "chi": 2.0}]},
     {"q0": "1.1099785827513808",
      "by_partition": [{"partition": [1, 1], "chi": 2.5},
                       {"partition": [2], "chi": 1.0}]},
     False, "VALUES"),
    # Duplicate identities fall back to index: collapsing entries would lose a
    # field, which is worse than misaligning one.
    ("pure additions are a schema gain, not movement",
     {"x": 1.0}, {"x": 1.0, "producer": "p.py", "n_partitions_total": 11},
     False, "SCHEMA_GAIN"),
    ("an addition alongside a real move is still VALUES",
     {"x": 1.0}, {"x": 2.0, "producer": "p.py"}, False, "VALUES"),
    ("prose changing is not a value change",
     {"q0": "1.1099785955573347", "description": "old prose",
      "x": 0.20906032199559366},
     {"q0": "1.1099785827513808", "description": "new prose",
      "x": 0.20906029879563937}, False, "ANCHOR_MIGRATION"),
    ("but convention changing still is",
     {"q0": "1.1099785955573347", "convention": "averaged-crossings"},
     {"q0": "1.1099785827513808",
      "convention": "colour-weighted-averaged-crossing"}, False, "VALUES"),
    ("a removed field is a loss, not churn",
     {"q0": "1.1099785955573347", "producer": "p.py", "x": 0.20906032199559366},
     {"q0": "1.1099785827513808", "x": 0.20906029879563937}, False, "VALUES"),
    ("duplicate identities fall back to index addressing",
     {"rows": [{"name": "a", "v": 1}, {"name": "a", "v": 2}]},
     {"rows": [{"name": "a", "v": 1}, {"name": "a", "v": 2}]},
     False, "NOCHANGE"),
    ("metadata-only churn is not movement",
     {"computedAt": "x", "durationMs": 1, "v": 2},
     {"computedAt": "y", "durationMs": 9, "v": 2}, False, "NOCHANGE"),
]


def _anchor_stub(anchor):
    """Stand in for `resolve_q0_anchor` so the policy is testable on its own.

    The real resolver reads `q0_anchor_manifest.json` off disk; pinning its
    answer here keeps these cases about the verdict rather than about the
    manifest's current contents.
    """
    return lambda _script: anchor


# `ANCHOR_MIGRATION_INFERRED`: (label, old, new, resolver, want).
#
# `scriptFile` is metadata, so it never counts as a moved field — it is present
# in these fixtures only because it is where the producer name comes from.
#
# The magnitudes are the real ones. 1.11e-7 is the q₀ shift as it lands in a
# derived value (`-h/2`, from the braid-encoding-audit migration); 1.82e-4 is
# the measured colour-blind → colour-weighted move in `tr_M`. The bound at 1e-5
# sits between them, and the two boundary cases check it is actually enforced
# there rather than approximately.
# witness-copy-intentional: as CASES above — this classifier's own
# self-test inputs, each reproducing a real observed magnitude so the
# 1e-5 bound is pinned between them.
INFERRED_CASES = [
    ("no q0 field + proton producer + anchor-sized move is INFERRED",
     {"scriptFile": "p.py", "x": 0.20906032199559366},
     {"scriptFile": "p.py", "x": 0.20906029879563937},
     _anchor_stub("proton"), "ANCHOR_MIGRATION_INFERRED"),
    # The negative the bound exists for: same shape, convention magnitude.
    ("a convention-sized move (1.8e-4) is NOT inferred",
     {"scriptFile": "p.py", "tr_M": 0.05534834587669884},
     {"scriptFile": "p.py", "tr_M": 0.055358426266783106},
     _anchor_stub("proton"), "VALUES"),
    # The negative that keeps the strict path strict: evidence could have been
    # there. It is not, and its absence is not an invitation to infer.
    ("a witness WITH a q0 field still takes the strict path",
     {"scriptFile": "p.py", "q0": "1.1099785827513808",
      "x": 0.20906032199559366},
     {"scriptFile": "p.py", "q0": "1.1099785827513808",
      "x": 0.20906029879563937},
     _anchor_stub("proton"), "VALUES",
     # Still the strict path (no inferred migration) -- but the reason now
     # comes from the sub-float64 gate, which names the field and magnitude
     # that actually blocked rather than a condition most of this population
     # shares.
     "x moved 1.11e-07, above the 1e-12 sub-float64 floor"),
    ("a q0 field that moves the WRONG way is not rescued by inference",
     {"scriptFile": "p.py", "q0": "1.1099785827513808"},
     {"scriptFile": "p.py", "q0": "1.1099785955573347"},
     _anchor_stub("proton"), "VALUES"),
    # An ideal_muon producer keeps the muon pin, so a re-run re-anchors nothing.
    ("a muon-anchored producer is never an inferred migration",
     {"scriptFile": "p.py", "x": 0.20906032199559366},
     {"scriptFile": "p.py", "x": 0.20906029879563937},
     _anchor_stub("muon"), "VALUES",
     "p.py resolves to muon anchor, not proton"),
    ("an ambiguous producer is never an inferred migration",
     {"scriptFile": "p.py", "x": 0.20906032199559366},
     {"scriptFile": "p.py", "x": 0.20906029879563937},
     _anchor_stub("ambiguous"), "VALUES"),
    # Degrading to VALUES is the required failure mode when the resolver is
    # unavailable (no qou_substrate on the path) or the witness names no
    # producer. Never a permissive default.
    ("an unresolvable anchor degrades to VALUES",
     {"scriptFile": "p.py", "x": 0.20906032199559366},
     {"scriptFile": "p.py", "x": 0.20906029879563937},
     _anchor_stub(None), "VALUES",
     "p.py resolves to no anchor, not proton"),
    ("a witness naming no producer cannot be inferred",
     {"x": 0.20906032199559366}, {"x": 0.20906029879563937},
     _anchor_stub("proton"), "VALUES", "witness names no producer"),
    # A non-numeric move has no magnitude, so the bound cannot exclude it.
    ("a non-numeric move alongside a bounded one is not inferred",
     {"scriptFile": "p.py", "x": 0.20906032199559366, "note": "a"},
     {"scriptFile": "p.py", "x": 0.20906029879563937, "note": "b"},
     _anchor_stub("proton"), "VALUES", "non-numeric move at note"),
    ("a convention flip with no q0 field is not inferred",
     {"scriptFile": "p.py", "convention": "colour-blind"},
     {"scriptFile": "p.py", "convention": "colour-weighted"},
     _anchor_stub("proton"), "VALUES"),
    ("just inside the collateral bound is inferred",
     {"scriptFile": "p.py", "x": 1.0}, {"scriptFile": "p.py", "x": 1.000009},
     _anchor_stub("proton"), "ANCHOR_MIGRATION_INFERRED"),
    # The decline must name the bound gate it actually failed, NOT the outer
    # "no flip" condition — the distinction that made wave 3's 50 VALUES
    # unreadable and forced a second run to recover.
    ("just outside the collateral bound is not",
     {"scriptFile": "p.py", "x": 1.0}, {"scriptFile": "p.py", "x": 1.00002},
     _anchor_stub("proton"), "VALUES",
     "x moved 2e-05, above the 1e-05 anchor bound"),
    # One field inside the bound must not carry another that is outside it.
    ("one out-of-bound field vetoes the whole diff",
     {"scriptFile": "p.py", "x": 1.0, "y": 1.0},
     {"scriptFile": "p.py", "x": 1.000009, "y": 1.01},
     _anchor_stub("proton"), "VALUES"),
    # Metadata-only churn stays NOCHANGE; inference must not manufacture a
    # verdict out of a diff that has no moved fields at all.
    ("metadata-only churn is not inferred into a migration",
     {"scriptFile": "p.py", "computedAt": "x", "v": 2},
     {"scriptFile": "p.py", "computedAt": "y", "v": 2},
     _anchor_stub("proton"), "NOCHANGE"),
    # The real shape from 0de68792: differs as text, identical as a number.
    # Was pinned to VALUES; now SUBFLOAT_MOVE, and the test's actual intent —
    # "not an inferred migration" — still holds. The diff is a float64's exact
    # expansion being replaced by the honest 17 digits, which is a sub-float64
    # move by construction.
    ("stripping float64 padding is a sub-float64 move, not a migration",
     {"scriptFile": "p.py",
      "v": "2.029883212819307392038581383530981838703155517578125"},
     {"scriptFile": "p.py", "v": "2.0298832128193074"},
     _anchor_stub("proton"), "SUBFLOAT_MOVE"),
    # ── PRECISION_GAIN: the f64 -> 50-dps upgrade ───────────────────────────
    ("q0 gaining its missing digits is a sub-float64 move",
     {"scriptFile": "p.py", "constants.q_0": "1.1099785827513808"},
     {"scriptFile": "p.py",
      "constants.q_0": "1.1099785827513808075916690956107688798744991218736"},
     _anchor_stub("proton"), "SUBFLOAT_MOVE"),
    ("a derived value moving at the f64 floor is a sub-float64 move",
     {"scriptFile": "p.py", "x": 1.0}, {"scriptFile": "p.py", "x": 1.0000000000001},
     _anchor_stub("proton"), "SUBFLOAT_MOVE"),
    # The case this bound exists to EXCLUDE. A near-degenerate argmax decided
    # by float noise flipped when the noise was removed -- a real finding, and
    # it must reach a human as VALUES rather than be absorbed as "precision".
    ("an argmax flipping is NOT sub-float64, it is a finding",
     {"scriptFile": "p.py", "per_n.13.argmax_shape[1]": 3},
     {"scriptFile": "p.py", "per_n.13.argmax_shape[1]": 4},
     _anchor_stub("proton"), "VALUES"),
    ("an anchor-sized move is far too big to be sub-float64",
     {"scriptFile": "p.py", "q0": "1.1099785827513808", "x": 0.20906032199559366},
     {"scriptFile": "p.py", "q0": "1.1099785827513808", "x": 0.20906029879563937},
     _anchor_stub("proton"), "VALUES"),
    ("a non-numeric move has no magnitude, so never sub-float64",
     {"scriptFile": "p.py", "note": "a"}, {"scriptFile": "p.py", "note": "b"},
     _anchor_stub("proton"), "VALUES"),
    ("text differing with no value moved stays a re-serialisation",
     {"scriptFile": "p.py", "n": "3"}, {"scriptFile": "p.py", "n": "3.0"},
     _anchor_stub("proton"), "VALUES"),
    ("a reserialised number is not an inferred migration",
     {"scriptFile": "p.py", "n": "3"}, {"scriptFile": "p.py", "n": "3.0"},
     _anchor_stub("proton"), "VALUES",
     "text differs but no value moved; a re-serialisation, not a migration"),
]


def self_test() -> int:
    fails = 0
    for label, old, new, gained, want in CASES:
        o = dict(old)
        n = dict(new)
        if gained:
            n["data"] = {"upstream_witness_hashes": [{"path": "u.witness.json"}]}
        got = classify(o, n)["verdict"]
        ok = got == want
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}   (want {want}, got {got})")

    # A 6th element pins the decline reason. Every VALUES case here declines at
    # some gate, and pinning the text is what stops the reason regressing to a
    # single uninformative label again.
    for case in INFERRED_CASES:
        label, old, new, resolve, want = case[:5]
        want_reason = case[5] if len(case) > 5 else None
        out = classify(dict(old), dict(new), resolve=resolve)
        got = out["verdict"]
        ok = got == want
        detail = f"want {want}, got {got}"
        if want_reason is not None:
            reason = out.get("reason", "")
            ok = ok and reason == want_reason
            detail = f"want reason {want_reason!r}, got {reason!r}"
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}   ({detail})")

    # The verdict is only safe because the driver does not auto-keep it. Pin
    # both halves of that here: it must stay a distinct string, and it must not
    # collide with either name `witness_regen_wave.KEEP` holds. Asserted by
    # value rather than by importing the driver, which imports this module.
    auto_kept = {"DECLARED", "ANCHOR_MIGRATION"}
    ok = ("ANCHOR_MIGRATION_INFERRED" not in auto_kept
          and classify({"scriptFile": "p.py", "x": 1.0},
                       {"scriptFile": "p.py", "x": 1.000009},
                       resolve=_anchor_stub("proton"))["verdict"] not in auto_kept)
    fails += not ok
    print(f"  {'ok  ' if ok else 'FAIL'}  the inferred verdict is not one the "
          f"driver auto-keeps")

    total = len(CASES) + len(INFERRED_CASES) + 1
    print(f"\n{total - fails}/{total} passed")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("witness", nargs="?")
    ap.add_argument("--base", default="HEAD")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not a.witness:
        ap.error("a witness path is required unless --self-test")
    p = Path(a.witness)
    rel = p.resolve().relative_to(ROOT).as_posix()
    old_raw = subprocess.run(["git", "show", f"{a.base}:{rel}"], cwd=ROOT,
                             capture_output=True, text=True).stdout
    if not old_raw:
        print(f"NEW  {rel}  (no {a.base} version)")
        return 0
    r = classify(json.loads(old_raw), json.loads(p.read_text(encoding="utf-8")))
    print(f"{r['verdict']}  {rel}")
    for k in ("moved", "flips", "reason", "sample"):
        if r.get(k) not in (None, 0, []):
            print(f"    {k}: {r[k]}")
    if r["verdict"] == "ANCHOR_MIGRATION_INFERRED":
        print("    NOT auto-kept: circumstantial evidence only, needs review")
    # INFERRED exits non-zero with the rest of the rejects, by design.
    return 0 if r["verdict"] in {"DECLARED", "ANCHOR_MIGRATION", "NOCHANGE"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
