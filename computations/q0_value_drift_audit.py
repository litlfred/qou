#!/usr/bin/env python3
# polynomial_q_not_applicable: static value audit; emits no numeric physics.
"""q0-value drift audit — catch stale substrate anchors, and RATCHET.

Bean: follow-up to `qou-ny4j` (the 73.6 ppQ stale `z`), which turned out to
be one instance of a corpus-wide class.

**The problem.** A witness or table that embeds `q_0` freezes whatever value
the producer had at the time. When the canonical pinning is re-solved, every
frozen copy silently goes stale. Nothing downstream notices, because a
q0-derived number has no independent check (see
`docs/audits/2026-08-06-markov-loop-value-rank-audit.md` §1).

**What this does.** Scans `*.witness.json` for q0-bearing fields, compares
each against the documented anchors at 65 dps, and classifies:

| class | meaning |
|---|---|
| `canonical` | matches the CAL-2 muon pin — the `computations/` layer convention |
| `proton-pin` | ~11.54 ppb below canonical: the documented physical-observations layer (`AGENTS.md` §q₀ anchor convention). **Legitimate, not drift.** |
| `STALE` | close to canonical but matching no documented pin |
| `unknown` | far from every anchor — needs a human look |

**Ratchet, not big-bang.** The existing backlog is large (203 live witnesses
at the time of writing). Demanding it drain before the gate turns on would
mean the gate never turns on, so instead:

* `--strict` fails only on stale values **not already in the baseline**
  (`q0-drift-baseline.json`). New staleness is blocked immediately; the
  historical backlog is recorded, not ignored.
* `--rebaseline` regenerates the baseline. Use it **only** when draining
  (the count must go DOWN); it is not a way to silence a new failure.

Two things this deliberately does NOT do:

* It does not rewrite witnesses. A stale witness is fixed by **re-running
  its producer**, never by hand-editing the number — the same discipline
  applied when fixing `q-beta-spectral-bridge-table-data.md`.
* It does not treat the proton pin as drift. Both layers are documented and
  intentional; conflating them would be the exact mistake `AGENTS.md`
  §"Recurring bug to watch (bean `tnjb`)" warns about.

Output: `q0-value-drift-audit.witness.json`.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    from mpmath import mp, mpf
except ImportError:  # pragma: no cover
    print("mpmath required", file=sys.stderr)
    raise

mp.dps = 65

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
BASELINE = HERE / "q0-drift-baseline.json"

# Documented anchors. Canonical is the CAL-2 muon pin carried by
# q-pinning-50-digit.witness.json; the proton pin is the physical-
# observations layer (AGENTS.md §q₀ anchor convention).
#
# BOTH ARE RESOLVED LIVE.  They used to be transcribed literals here:
#
#     Q_CANONICAL    = mpf("1.10997859555733471989...")   # the frozen anchor
#     PROTON_PIN_PPB = mpf("-11.5371")                    # measured against it
#
# and that is a defect of exactly the kind this audit exists to detect.  A
# drift detector whose reference is a transcription cannot see the reference
# drift.  Concretely, under the 2026-08-22 owner ruling ("A --> CODATA 2022")
# the anchor moves +0.0769 ppb, and a transcribed Q_CANONICAL would then have
# classified every CORRECTLY migrated witness as STALE while calling the
# superseded value canonical -- the ratchet inverted, pointing at the fix
# instead of the defect.  It was already doing so on the migration branch: it
# reported the re-derived anchor witness as the single NEW stale entry.
#
# PROTON_PIN_PPB moves with it.  It is an OFFSET measured against the muon
# anchor, so re-pinning the anchor changes it too (-11.5371 vs A becomes
# -11.6140 vs C); freezing the offset while the reference moves would drag
# every proton-pinned witness across the PIN_TOL_PPB window.  Deriving it
# from the two resolved pins keeps the pair consistent by construction.
#
# `_q0_value_for_anchor` is the anchor-LABEL resolver in qou_substrate --
# the same function that decides what gets stamped `muon` -- so this audit
# and the stamps it checks now read one source instead of two.
from qou_substrate.witness import _q0_value_for_anchor as _pin
# `q_parameter` lives in computations/substrate/ and is reachable only through
# _path_bridge, which this file did not import -- `qou_substrate` above
# resolves for an unrelated reason (the editable .pth in the dev image), so the
# two are not evidence for each other. This is bean qou-ya1e's defect met head
# on while fixing something else; the bootstrap is that bean's, verified under
# a bare-container simulation.
import sys as _sys, pathlib as _pl  # noqa: E402 -- bean qou-ya1e
for _anc in _pl.Path(__file__).resolve().parents:
    if (_anc / '_path_bridge.py').exists():
        _sys.path.insert(0, str(_anc)); break
import _path_bridge  # noqa: F401,E402 -- adds the substrate path
from q_parameter import Q_MUON_50_DIGIT_STR   # noqa: E402 -- pin A, 50 digits


def _resolved(anchor: str) -> mpf:
    v = _pin(anchor)
    if not v:
        raise SystemExit(
            f"q0_value_drift_audit: cannot resolve the {anchor} pin. "
            "Refusing to fall back to a transcribed literal -- a drift audit "
            "measuring against a guess is worse than no drift audit."
        )
    return mpf(v)


Q_CANONICAL = _resolved("muon")
_Q_PROTON = _resolved("proton")
# Offset of the proton-pinned value, in ppb, DERIVED rather than transcribed.
PROTON_PIN_PPB = (_Q_PROTON - Q_CANONICAL) / Q_CANONICAL * mpf(10) ** 9
PIN_TOL_PPB = mpf("0.5")             # how close to a named pin counts as that pin

# Field names that carry a substrate anchor. `q_star` / `qstar` are a
# DIFFERENT parameter (the decay-sector q*) and are deliberately excluded.
Q0_FIELD = re.compile(r"^(q_?0|q_?0_\d+dps|q0Value|q_zero|substrate_q)$", re.I)
EXCLUDE_FIELD = re.compile(r"star|\*|anchor$|err|sigma|unit", re.I)

# Only values in this neighbourhood are substrate anchors at all.
Q_LO, Q_HI = mpf("1.1"), mpf("1.12")


# ── DECLARED historical pins ─────────────────────────────────────────────
#
# Some witnesses record a retired pin ON PURPOSE. `two_blocks_publish_the_two
# _sides_of_one_identity_at_different_pins_probe` evaluates one identity at
# several pins and reports their separation: the retired values ARE its
# measurement, not drift in it. Without a way to say so they are permanently
# NEW on this gate, and the two obvious cures both delete the gate instead of
# draining it (measured 2026-09-14, bean `qou-zru5`):
#
#   * adding these values to the anchor set reclassifies 201 of the 206 STALE
#     rows, because ~all of the backlog IS the pre-ruling pin;
#   * excluding `_deprecated/` drops 179 of the 329 BASELINED keys.
#
# So the carve-out is per FIELD and, unlike a bare `precision_tier` assertion,
# it is CHECKED: the producer names WHICH pin, and the value must match that
# pin. Declaring `B` on something that is not B still reports — as
# DECLARATION-MISMATCH, which blocks. A declaration cannot launder a value.
#
# WHAT A, B AND C ARE (`audits/muon_pin_three_values_probe.py`, PR #5434):
#
#   A  1.1099785955573347…    the self-certified anomaly. Inverted it gives
#                             m_mu/m_e = 206.768282989315, matching NO
#                             published figure, so it is not that derivation
#                             at any CODATA vintage and CANNOT be derived.
#   B  Vol(4_1)/206.7682830   the lepton-tower derivation at CODATA 2018
#   C  Vol(4_1)/206.7682827   ...and at CODATA 2022 — today's canonical muon
#                             pin, which is `Q_CANONICAL` resolved live above.
#
# B and C are DERIVED for the reason the header gives for the live anchors: a
# transcribed reference cannot be seen to drift. A is the one exception the
# evidence forces, and it is safe for the reason that makes it an exception —
# A is retired and not reproducible from anything, so it cannot move.
#
# MEASURED against the live canonical: A -0.076942 ppb, B -0.079784 ppb. Those
# are exactly the two buckets this gate's STALE population falls into (199
# rows at B, 2 at A), which is how the registry was checked rather than
# assumed.
_VOL_4_1 = 2 * mp.clsin(2, mp.pi / 3)


def _q0_from_muon_ratio(ratio: str) -> mpf:
    """The lepton-tower inversion: hbar_q^2 = Vol(4_1)/(m_mu/m_e)."""
    return 1 / (1 - mp.sqrt(_VOL_4_1 / mpf(ratio)))


HISTORICAL_PINS = {
    # A is IMPORTED, not retyped. "Not derivable" (above) means no published
    # muon ratio reproduces it; it is still a NAMED CONSTANT, and typing it by
    # hand gave a 17-digit truncation of a 50-digit value. The reference-
    # literal ratchet caught that as a NEW finding, correctly.
    "A": mpf(Q_MUON_50_DIGIT_STR),
    "B": _q0_from_muon_ratio("206.7682830"),  # CODATA 2018
    "C": Q_CANONICAL,                         # CODATA 2022 == live canonical
}

#: The key a producer writes NEXT TO a q0 field to declare it historical.
#: Deliberately not matched by `Q0_FIELD`, so it can never be read as a value.
DECL_KEY = "q0_historical_pin"

#: A and B are only 2.842e-12 apart in relative terms, so the tolerance has to
#: sit well inside that or a declaration could not tell them apart. 1e-13 is
#: 28x tighter than the gap and still far looser than any truncation in the
#: corpus (the shortest stored form, A at 17 digits, is exact).
DECL_TOL = mpf("1e-13")


def classify_declared(x: mpf, label: object) -> tuple[str, mpf]:
    """Classify a value whose field DECLARED which historical pin it records."""
    pin = HISTORICAL_PINS.get(str(label))
    if pin is None:
        return "DECLARATION-UNKNOWN", _ppb(x)
    if abs(x - pin) / pin < DECL_TOL:
        return "declared-historical", _ppb(x)
    return "DECLARATION-MISMATCH", _ppb(x)


def _ppb(x: mpf) -> mpf:
    return (x - Q_CANONICAL) / Q_CANONICAL * mpf(10) ** 9


def classify(x: mpf) -> tuple[str, mpf]:
    d = _ppb(x)
    if abs(d) < mpf("1e-6"):
        return "canonical", d
    if abs(d - PROTON_PIN_PPB) < PIN_TOL_PPB:
        return "proton-pin", d
    if abs(d) < mpf("100"):
        return "STALE", d
    return "unknown", d


def _walk(obj, path: str, out: list) -> None:
    if isinstance(obj, dict):
        # Read once per dict: a declaration applies to the q0 field beside it,
        # which is the narrowest scope that can express "this one is a pin".
        declared = obj.get(DECL_KEY)
        for k, v in obj.items():
            p = f"{path}.{k}" if path else k
            if isinstance(v, (str, float, int)) and Q0_FIELD.match(k) and not EXCLUDE_FIELD.search(k):
                try:
                    x = mpf(str(v))
                except Exception:
                    continue
                if Q_LO < x < Q_HI:
                    cls, d = (classify_declared(x, declared) if declared is not None
                              else classify(x))
                    row = {"field": p, "value": str(v), "class": cls,
                           "ppb_vs_canonical": float(d)}
                    if declared is not None:
                        row["declared_pin"] = str(declared)
                    out.append(row)
            else:
                _walk(v, p, out)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            _walk(v, f"{path}[{i}]", out)


def scan() -> list[dict]:
    rows: list[dict] = []
    for p in sorted(HERE.rglob("*.witness.json")):
        rel = p.relative_to(ROOT).as_posix()
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        found: list = []
        _walk(data, "", found)
        for f in found:
            rows.append({"file": rel, **f})
    return rows


def layer_mismatches(canonical_rows: list) -> list:
    """`canonical`-classed values whose PRODUCER is no longer in the muon layer.

    `canonical` here means "matches the CAL-2 muon pin", which the header table
    defines as *the `computations/` layer convention* — not as the framework's
    canonical anchor.

    The class definition does not follow manifest membership, and `canonical` is
    the one class that can never be `STALE`. So a witness written by a
    proton-layer producer, still carrying the muon pin, is invisible to this
    audit's staleness test. That is the gap this function reports.

    CORRECTED 2026-08-23. This docstring previously said `_migration_2026_08_19`
    moved 255 producers out of `ideal_muon` "on owner authorisation, leaving 3",
    and that acting on the result would move ~162 witnesses into `STALE` and fail
    a blocking gate. **Both figures were artefacts.** `ideal_muon` held 3 because
    `q0_anchor_manifest.json`'s producer lookup was root-only and never read the
    ~700 witnesses whose producers live in `probes/`, `qbeta/`, `substrate/` etc
    (fixed in `8b4825920`). The manifest now holds 110 / 513 / 22, and
    `_migration_2026_08_19` no longer exists in it.

    Re-measured 2026-08-23 against the fixed manifest: 156 canonical-classed
    witness files = 66 mismatch + 76 legitimately muon-layer + 14 unresolved.
    The 66 are 50 producers simply **undeclared** in the manifest (a declaration
    gap, not a stale value), 9 `physical_proton` and 7 `ambiguous`. Current
    `STALE` is 292 against a 329-key baseline, so NEW = 0 and `--strict` exits 0.

    Diagnostic only: printed, never written to the witness, and it cannot change
    the exit code. Bean `qou-fd0e`.
    """
    try:
        man = json.loads((HERE / "q0_anchor_manifest.json").read_text())
    except Exception as exc:  # noqa: BLE001 — reported, never silently empty
        return [{"error": f"manifest unreadable: {exc}"}]
    ideal = set(man.get("ideal_muon", []))
    repo = HERE.parent
    out, legit, unresolved, seen = [], [], [], set()
    for r in canonical_rows:
        f = r.get("file")
        if not f or f in seen:
            continue
        seen.add(f)
        # Resolve relative to the repo, not the process cwd.
        cand = Path(f) if Path(f).is_absolute() else (repo / f)
        if not cand.exists():
            hits = list(repo.rglob(Path(f).name))
            if not hits:
                unresolved.append({"witness": f, "why": "file not found"})
                continue
            cand = hits[0]
        try:
            sf = json.loads(cand.read_text()).get("scriptFile") or ""
        except Exception as exc:  # noqa: BLE001
            unresolved.append({"witness": f, "why": f"unreadable ({type(exc).__name__})"})
            continue
        stem = Path(str(sf)).stem
        if not stem:
            unresolved.append({"witness": f, "why": "no scriptFile"})
        elif stem in ideal:
            legit.append({"witness": f, "producer": stem})
        else:
            out.append({"witness": f, "producer": stem})
    # Three explicit classes. An UNRESOLVED witness is not evidence of either
    # verdict — reporting it by subtraction would count "could not check" as
    # "legitimately muon", which is the exact defect this session has been
    # cataloguing (beans qou-0uqm, qou-i5jy).
    return {"mismatch": out, "legit": legit, "unresolved": unresolved}


def is_retired(row: dict) -> bool:
    """True for a witness under `_deprecated/` — excised, never re-run."""
    return "_deprecated" in str(row.get("file", "")).split("/")


def _selftest() -> int:
    """Both directions. A carve-out that cannot be shown to REFUSE is a hole."""
    B = HISTORICAL_PINS["B"]
    A = HISTORICAL_PINS["A"]
    cases = [
        # (containing dict, expected class, why)
        ({"q_0": mp.nstr(B, 30)}, "STALE",
         "the backlog case: pin B, undeclared, is drift — 199 rows look like this"),
        ({"q_0": mp.nstr(B, 30), DECL_KEY: "B"}, "declared-historical",
         "...and the SAME value declared as B is the probe's measurement"),
        ({"q_0": mp.nstr(B, 30), DECL_KEY: "A"}, "DECLARATION-MISMATCH",
         "A DECLARATION CANNOT LAUNDER A VALUE: B declared as A still reports"),
        ({"q_0": mp.nstr(A, 20), DECL_KEY: "A"}, "declared-historical",
         "A is carried as a literal because it is not derivable from any "
         "published muon ratio; it still has to MATCH"),
        ({"q_0": mp.nstr(B, 30), DECL_KEY: "Z"}, "DECLARATION-UNKNOWN",
         "an unresolvable label is a blocking failure, never a silent pass"),
        ({"q_0": mp.nstr(Q_CANONICAL, 30)}, "canonical",
         "the live canonical muon pin, undeclared"),
        ({"q_0": mp.nstr(_Q_PROTON, 30)}, "proton-pin",
         "the documented physical-observations layer, undeclared"),
        ({"q_0": mp.nstr(B + B * mpf("1e-12"), 30), DECL_KEY: "B"},
         "DECLARATION-MISMATCH",
         "TOLERANCE: 1e-12 off B is refused — it has to be, because A and B "
         "are only 2.842e-12 apart and a looser window could not tell them "
         "apart"),
        ({"q_0": mp.nstr(B + B * mpf("1e-15"), 30), DECL_KEY: "B"},
         "declared-historical",
         "...while a truncation-scale difference is accepted"),
    ]
    bad = 0
    for obj, want, why in cases:
        out = []
        _walk(obj, "", out)
        got = out[0]["class"] if out else "NO-ROW"
        ok = got == want
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'} want={want:22s} got={got:22s} {why}")

    # the declaration key must never itself read as a q0 value
    out = []
    _walk({DECL_KEY: "B"}, "", out)
    ok = not out
    bad += not ok
    print(f"  {'ok  ' if ok else 'FAIL'} want={'(no row)':22s} "
          f"got={('(no row)' if ok else out[0]['class']):22s} "
          "the declaration key is not matched by Q0_FIELD, so it cannot be "
          "read as a value")

    # retired predicate, both ways
    for f, want in (("computations/_deprecated/x.witness.json", True),
                    ("computations/probes/x.witness.json", False),
                    ("computations/not_deprecated_really/x.witness.json", False)):
        got = is_retired({"file": f})
        ok = got == want
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'} is_retired({f.split('/')[1][:22]:24s}) "
              f"-> {got}  (want {want})")

    print(f"\nselftest: {len(cases) + 4 - bad}/{len(cases) + 4} passed")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", "--selftest", action="store_true",
                    dest="selftest",
                    help="prove the detector fires AND refuses, then exit")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on stale values NOT already in the baseline")
    ap.add_argument("--rebaseline", action="store_true",
                    help="regenerate the baseline (only when draining — count must go DOWN)")
    ap.add_argument("--layer-check", action="store_true",
                    help="report `canonical`-classed values whose producer is no "
                         "longer in the manifest's ideal_muon layer. Diagnostic: "
                         "printed, not written to the witness, cannot change the "
                         "exit code.")
    args = ap.parse_args()
    if args.selftest:
        return _selftest()

    rows = scan()
    by = {}
    for r in rows:
        by.setdefault(r["class"], []).append(r)
    stale = by.get("STALE", [])
    unknown = by.get("unknown", [])

    print("=" * 74)
    print("q0-VALUE DRIFT AUDIT")
    print("=" * 74)
    for cls in ("canonical", "proton-pin", "declared-historical", "STALE",
                "unknown", "DECLARATION-MISMATCH", "DECLARATION-UNKNOWN"):
        n = len(by.get(cls, []))
        if n == 0 and cls.startswith("DECLARATION"):
            continue
        note = {"proton-pin": "  (documented physical-observations layer — legitimate)",
                "canonical": "  (CAL-2 muon pin — the computations/ convention)",
                "declared-historical": "  (field DECLARES which retired pin it records, and matches it)",
                "DECLARATION-MISMATCH": "  (BLOCKING — declared a pin it does not match)",
                "DECLARATION-UNKNOWN": "  (BLOCKING — declared a pin this audit cannot resolve)",
                }.get(cls, "")
        print(f"  {cls:<20} {n:>5}{note}")
    print(f"  {'TOTAL':<12} {len(rows):>5} q0-bearing fields in *.witness.json")

    prior = []
    if BASELINE.exists():
        prior = json.loads(BASELINE.read_text())["stale_keys"]
    key = lambda r: f"{r['file']}::{r['field']}"
    _prior = set(prior)
    # A retired witness cannot REGRESS: nobody re-runs a producer that has been
    # excised, so a NEW finding under `_deprecated/` is always the anchor moving
    # beneath a frozen file rather than anyone's change — unfixable by the very
    # remedy the banner prescribes ("fix by RE-RUNNING THE PRODUCER").
    #
    # THIS IS NOT THE `_deprecated` EXCLUSION THAT WOULD BE A DRAIN. It applies
    # to the NEW check only. The census, the `stale total` and the baseline are
    # untouched, so 179 of the 329 baselined keys stay counted exactly as they
    # were and no number goes down. Retired arrivals are reported on their own
    # line instead of vanishing.
    unbaselined = [r for r in stale if key(r) not in _prior]
    new_stale = [r for r in unbaselined if not is_retired(r)]
    new_retired = [r for r in unbaselined if is_retired(r)]

    if stale:
        print(f"\n  stale total: {len(stale)}   baseline: {len(prior)}   NEW: {len(new_stale)}")
        if new_stale:
            print("\n  NEW stale (not in baseline) — fix by RE-RUNNING THE PRODUCER,")
            print("  never by hand-editing the number:")
            for r in new_stale[:25]:
                print(f"    {r['file']}  {r['field']}  ({r['ppb_vs_canonical']:+.3g} ppb)")
            if len(new_stale) > 25:
                print(f"    ... and {len(new_stale) - 25} more")
        if new_retired:
            print(f"\n  {len(new_retired)} unbaselined stale field(s) under "
                  "_deprecated/ — REPORTED, not gating:")
            for r in new_retired[:10]:
                print(f"    {r['file']}  {r['field']}  ({r['ppb_vs_canonical']:+.3g} ppb)")
            print("    Their producers are excised, so re-running them — the only "
                  "fix this\n    gate prescribes — is not available. Still counted "
                  "in `stale total`.")
    if unknown:
        print(f"\n  ⚠ {len(unknown)} value(s) matching no anchor — needs a human look:")
        for r in unknown[:10]:
            print(f"    {r['file']}  {r['field']} = {r['value']}")

    if args.rebaseline:
        # Provenance stamp (bean qou-f1rs): the witness dict was built
        # INLINE at the write below, so there was nothing to stamp. It
        # is bound to a name here so this producer records which script
        # wrote it -- a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        import os as _os  # noqa: E402 -- provenance stamp
        from qou_substrate.witness import WitnessBuilder as _WB
        _prov_payload_1 = {"note": "Known-stale q0 fields. Regenerate ONLY when draining; "
                     "the count must go DOWN. Not a way to silence a new failure.",
             "count": len(stale),
             "stale_keys": sorted(key(r) for r in stale)}
        _prov_payload_1.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            _prov_payload_1, script_path=__file__, engine=None, q0_anchor=False)
        BASELINE.write_text(json.dumps(
            _prov_payload_1, indent=2) + "\n")
        print(f"\nRebaselined: {len(stale)} stale keys recorded.")

    out = HERE / "q0-value-drift-audit.witness.json"
    # Provenance stamp (bean qou-f1rs): the witness dict was built
    # INLINE at the write below, so there was nothing to stamp. It
    # is bound to a name here so this producer records which script
    # wrote it -- a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    _prov_payload_2 = {
        "schema": "witness/v1",
        "name": "q0-value-drift-audit",
        "description": "Substrate-anchor drift across witness JSONs. proton-pin is "
                       "legitimate (documented layer); STALE matches no documented pin.",
        "data": {"counts": {k: len(v) for k, v in by.items()},
                 "stale_total": len(stale), "new_stale": len(new_stale),
                 "rows": rows},
    }
    _prov_payload_2.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        _prov_payload_2, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(_prov_payload_2, indent=2) + "\n")
    print(f"\nWrote {out.name}")

    if args.layer_check:
        mism = layer_mismatches(by.get("canonical", []))
        print("\n" + "=" * 66)
        print("  producer-layer check (--layer-check, diagnostic only)")
        print("=" * 66)
        if isinstance(mism, list) and mism and "error" in mism[0]:
            print(f"  {mism[0]['error']}")
        else:
            n_canon_files = len({r["file"] for r in by.get("canonical", [])})
            bad, ok, unk = mism["mismatch"], mism["legit"], mism["unresolved"]
            print(f"  canonical-classed witness files            : {n_canon_files}")
            print(f"  producer NOT in ideal_muon (blind to STALE): {len(bad)}")
            print(f"  legitimately muon-layer                    : {len(ok)}")
            print(f"  UNRESOLVED (not evidence either way)       : {len(unk)}")
            mism = bad
            for m in mism[:20]:
                print(f"    {m['witness'][:52]:54} <- {m['producer']}")
            if len(mism) > 20:
                print(f"    … and {len(mism) - 20} more")
        print("\n  Exit code unchanged — `new_stale` remains the only gate.")

    # A declaration that does not check out is a HARDER failure than stale
    # drift: stale is a backlog with a known remedy, a false declaration is an
    # attempt to carve out a value that is not what it claims. It blocks under
    # --strict regardless of any baseline, and there is no baseline for it.
    bad_decl = by.get("DECLARATION-MISMATCH", []) + by.get("DECLARATION-UNKNOWN", [])
    if bad_decl:
        print(f"\n  ✗ {len(bad_decl)} DECLARATION failure(s) — a field named a "
              "historical pin it does not match,\n    or one this audit cannot "
              "resolve. Fix the declaration or the value; there is no\n    baseline "
              "for these and adding one is not the remedy.")
        for r in bad_decl[:10]:
            print(f"    {r['file']}  {r['field']}  declared={r.get('declared_pin')!r}"
                  f"  ({r['ppb_vs_canonical']:+.3g} ppb)")

    return 1 if (args.strict and (new_stale or bad_decl)) else 0


if __name__ == "__main__":
    sys.exit(main())
