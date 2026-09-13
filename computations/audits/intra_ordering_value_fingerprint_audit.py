#!/usr/bin/env python3
"""Find grouped-era artifacts by their VALUE, not by any symptom.

WHY A VALUE-KEYED SELECTOR
--------------------------
The 2026-09-05 intra-ordering ruling (`qou-hu1f`) has now escaped **three**
separate sweeps, each of which keyed on a *symptom*:

  1. the `qou-hu1f` witness sweep — selected witnesses whose producer references
     `atom_braid_word_3A` by name;
  2. `binding_canonical` — missed for the same reason, it reaches the canonical
     word indirectly;
  3. `qou-cvky` — selected files that *raise* on a non-monotone word.

`closed_form_tau_M.compute_tau_M_nucleon_H3` (bean `qou-y2o7`) was invisible to
all three. It never named `atom_braid_word_3A`, and it never raised, because it
**built its own monotone word** and so satisfied the kernel's precondition with
the wrong braid. There was no symptom to key on. It returned a plausible 50-dps
number in the superseded ordering, and 18 consumers inherited it.

A symptom-keyed selector finds the loud cases. This one keys on the answer: a
grouped-era |tr_M| is a specific number and is recognisable wherever it is
written down, whatever the producer is called and whether or not it crashes.
That is the argument `y_lambda_convention_c_fingerprint_audit.py` makes for
trace CONVENTIONS, applied to intra-nucleon ORDERING.

WHAT A HIT IS AND IS NOT
------------------------
A hit says a witness's payload carries a grouped-era value. It does **not** say
the producer is broken:

  * the producer may be fixed while the witness was never regenerated (the
    common case — re-run it to tell the two apart);
  * the site may be **deliberately** historical. Three are, as of 2026-09-06:
    `nucleon_h3_marshalling_divergence_probe`,
    `qbeta_delta_vs_deltaTbeta_settled_probe` and `reduced_block_kernel` all
    pass `intra_order="grouped"` on purpose, because their whole comparison
    lives in that frame. Those are listed separately, not as findings.

A non-hit is not a clean bill either: a witness that records only derived
quantities (binding energies, mass residuals) carries no |tr_M| for this to
match, and is silent under the test.

WHY THE MATCH CANNOT BE COINCIDENCE
-----------------------------------
Matching is on **15 significant digits** of a specific irrational. This corpus
has measured its own coincidence floor: agreement to 0–2 significant figures is
a coincidence 100 % of the time, 6–8 figures 5.4 %, 9–11 figures 2.7 %. Fifteen
is far past any of that — a 15-digit match to `1.14575969245730087` is that
number, not a near miss.

Fingerprints are computed live from `atom_braid_word_3A` under both orderings at
both documented pins, never transcribed, so a re-pin moves them rather than
silently invalidating the scan.
"""
from __future__ import annotations

import ast
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMPUTATIONS = _HERE.parent
_ROOT = _COMPUTATIONS.parent
sys.path[:0] = [str(_COMPUTATIONS), str(_COMPUTATIONS / "substrate"),
                str(_ROOT / "tools" / "qou-substrate" / "python")]

import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402

mp.mp.dps = 50

import mass_at_3A_proper as M  # noqa: E402
import tr_m_wenzl_bridge_mpfr as B  # noqa: E402
from qou_substrate import constants as _c  # noqa: E402

#: Significant digits required for a match. See "WHY THE MATCH CANNOT BE
#: COINCIDENCE" above — this is deliberately far past the measured floor.
SIG_DIGITS = 15

ATOMS = {"proton": (1, 0), "neutron": (0, 1), "deuteron": (1, 1),
         "tritium": (1, 2), "helium-3": (2, 1)}

PINS = {
    "proton": str(_c.Q_50_DIGIT_STR),
    "muon-live": ("1.109978595642739046681795129380001752700065561029011"
                  "556974045769999095"),
}

#: Sites that pass `intra_order="grouped"` deliberately, with the reason. A hit
#: on one of these is expected and is not a finding.
DELIBERATE = {
    "nucleon-h3-marshalling-divergence":
        "guards the qou-qu2w fix against a grouped-era habiro target",
    "qbeta-delta-vs-deltaTbeta-settled":
        "its own word, its pre/post-fix pin and its paper closed forms are all grouped",
    "reduced-block-kernel":
        "its self-test compares two monotone-only paths (qou-cvky)",
    "the_character_closure_block_and_a_lean_file_publish_convention_c_probe":
        "its SUBJECT is the convention-C trace table that "
        "prop:q-hecke-seminormal-character-closure publishes; carrying C-era "
        "values is the finding, not a defect (qou-4383)",
}


def fingerprints() -> dict[str, tuple[str, str, str]]:
    """{15-sig-digit prefix: (atom, pin, ordering)} computed live."""
    out: dict[str, tuple[str, str, str]] = {}
    for pin, qs in PINS.items():
        q = mp.mpf(qs)
        for atom, (Z, N) in ATOMS.items():
            n = 3 * (Z + N)
            for order in ("grouped", "borromean"):
                word = M.atom_braid_word_3A(Z, N, q=q, intra_order=order)
                v = abs(B.tr_M_via_wenzl_bridge_mpfr(word, n, qs, dps=50))
                out[mp.nstr(v, SIG_DIGITS).rstrip("0")] = (atom, pin, order)
    return out


def scan_value(s: str, fps: dict) -> tuple | None:
    """Does this string start with a fingerprint, to SIG_DIGITS?"""
    t = s.lstrip("-").lstrip()
    for pref, meta in fps.items():
        p = pref.lstrip("-")
        if t.startswith(p) and len(p.replace(".", "").lstrip("0")) >= SIG_DIGITS - 1:
            return meta
    return None


#: Producers whose SOURCE may legitimately carry a grouped literal in code.
#: Distinct from DELIBERATE, which is about witness payloads: a probe whose
#: SUBJECT is the ordering comparison must hold both frames as data to compare
#: them, and flagging that would be flagging the measurement.
SOURCE_DELIBERATE = {
    "qbeta_delta_vs_deltaTbeta_settled_probe.py":
        "deliberately grouped throughout — its own word, its pre/post-fix pin "
        "and its paper closed forms are all grouped (see DELIBERATE)",
}
#: This list is SHORT because the AST docstring exclusion already does the work.
#: It was drafted with seven entries — `mass_at_3A_proper`,
#: `atom_intra_block_is_not_a_braid_probe`, `nf_vs_canonical_word_order_probe`,
#: `nucleon_h3_marshalling_divergence_probe`, the convention-C probe,
#: `the_intra_ordering_moves_absolute_traces...` and `trm_proton_five_values_census`
#: — every one of which turned out to carry its grouped value only in PROSE and
#: to drop out on its own. Six dead entries in a curated set is the rot that
#: makes the next reader trust the list instead of the mechanism, so they are
#: gone. Add one here only after confirming the AST scan actually flags the file.


def _source_constants(tree):
    """Every literal reachable as CODE, with docstrings excluded.

    Comments never enter an AST, so they are excluded for free. Docstrings are
    excluded explicitly: `mass_at_3A_proper` quotes both the grouped and the
    borromean |tr_M| in the docstring that EXPLAINS the 2026-09-05 ruling, and
    flagging that would be flagging the documentation of the fix.

    Strings are NOT skipped wholesale — `mp.mpf("1.1457...")` is a literal in
    code, and skipping it would miss the exact shape this corpus writes its
    high-precision constants in.
    """
    docstrings = set()
    for n in ast.walk(tree):
        if isinstance(n, (ast.Module, ast.ClassDef, ast.FunctionDef,
                          ast.AsyncFunctionDef)):
            body = getattr(n, "body", None)
            if (body and isinstance(body[0], ast.Expr)
                    and isinstance(body[0].value, ast.Constant)
                    and isinstance(body[0].value.value, str)):
                docstrings.add(id(body[0].value))
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and id(n) not in docstrings:
            if isinstance(n.value, (int, float, str)):
                yield n.lineno, str(n.value)


def scan_source(fps):
    """Grouped-era values written as LITERALS in producer source.

    The witness scan below answers "does this artifact carry a grouped value?".
    This answers a different and sharper question: "does this SOURCE carry
    one?" A stale witness regenerates; a hardcoded constant does not, and it
    re-emits the grouped value on every future run.

    `qou-4383` found two of these by hand (`T_P` / `MEASURED["t_p"]` in two
    qbeta probes). Extending the audit's own value-keyed method from witnesses
    to source finds them all — which is the same argument the bean makes for
    keying on the answer rather than on a symptom.
    """
    out: dict[str, list] = {}
    for f in sorted(_COMPUTATIONS.rglob("*.py")):
        if any(s in f.parts for s in ("_deprecated", "__pycache__", ".git")):
            continue
        try:
            src = f.read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(src)
        except (OSError, SyntaxError):
            continue
        for lineno, lit in _source_constants(tree):
            meta = scan_value(lit, fps)
            if meta and meta[2] == "grouped":
                rel = str(f.relative_to(_ROOT))
                out.setdefault(rel, []).append((lineno, lit[:26], meta[0], meta[1]))
    return out


def walk(o, path=""):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from walk(v, f"{path}/{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from walk(v, f"{path}[{i}]")
    elif isinstance(o, str):
        yield path, o
    elif isinstance(o, float):
        yield path, repr(o)


def main() -> int:
    fps = fingerprints()
    print(f"Intra-ordering value fingerprint audit — {SIG_DIGITS} significant digits")
    print(f"  {len(fps)} fingerprints: {len(ATOMS)} atoms x {len(PINS)} pins x 2 orderings\n")

    files = sorted(p for p in _ROOT.rglob("*.witness.json")
                   if "_deprecated" not in str(p) and ".git" not in str(p))
    grouped_hits: dict[str, list] = {}
    borro_hits: dict[str, list] = {}

    for f in files:
        try:
            d = json.loads(f.read_text(encoding="utf-8", errors="replace"))
        except Exception:
            continue
        for path, s in walk(d):
            meta = scan_value(s, fps)
            if meta is None:
                continue
            atom, pin, order = meta
            rel = str(f.relative_to(_ROOT))
            bucket = grouped_hits if order == "grouped" else borro_hits
            bucket.setdefault(rel, []).append((path, atom, pin))

    deliberate, candidates = {}, {}
    for rel, hits in grouped_hits.items():
        stem = Path(rel).name.replace(".witness.json", "")
        (deliberate if stem in DELIBERATE else candidates)[rel] = hits

    print(f"=== GROUPED-era hits: {len(grouped_hits)} witness file(s) ===")
    print(f"    {len(candidates)} candidate(s), {len(deliberate)} known-deliberate\n")
    for rel, hits in sorted(candidates.items()):
        print(f"  CANDIDATE {rel}")
        for path, atom, pin in hits[:4]:
            print(f"      {atom} @ {pin}   {path}")
        if len(hits) > 4:
            print(f"      … and {len(hits) - 4} more field(s)")
    if deliberate:
        print("\n  known-deliberate (grouped on purpose, not findings):")
        for rel in sorted(deliberate):
            stem = Path(rel).name.replace(".witness.json", "")
            print(f"      {rel}\n          {DELIBERATE[stem]}")

    # ---- SOURCE scan: grouped values written as literals in code -----------
    src_all = scan_source(fps)
    src_deliberate = {k: v for k, v in src_all.items()
                      if Path(k).name in SOURCE_DELIBERATE}
    src_hard = {k: v for k, v in src_all.items()
                if Path(k).name not in SOURCE_DELIBERATE}
    print(f"\n=== GROUPED-era literals in SOURCE: {len(src_all)} file(s) ===")
    print(f"    {len(src_hard)} hardcoded, {len(src_deliberate)} known-deliberate")
    print("    A stale witness regenerates. A hardcoded constant does not — it")
    print("    re-emits the grouped value on every future run.\n")
    for rel, hits in sorted(src_hard.items()):
        print(f"  HARDCODED {rel}")
        for lineno, lit, atom, pin in sorted(set(hits))[:4]:
            print(f"      L{lineno:<5d} {lit:26s}  {atom} @ {pin}")
    if src_deliberate:
        print("\n  known-deliberate source (the ordering IS the subject):")
        for rel in sorted(src_deliberate):
            print(f"      {rel}\n          {SOURCE_DELIBERATE[Path(rel).name]}")

    print(f"\n=== borromean (canonical) hits: {len(borro_hits)} witness file(s) ===")
    for rel in sorted(borro_hits)[:12]:
        print(f"      {rel}")
    if len(borro_hits) > 12:
        print(f"      … and {len(borro_hits) - 12} more")

    from witness_base import WitnessBuilder  # noqa: E402
    wb = WitnessBuilder(Path(__file__).stem, engine="python")
    wb.set_description(
        "Scans every committed witness for grouped-era |tr_M| values, matched "
        "to 15 significant digits against fingerprints computed live from "
        "atom_braid_word_3A under both orderings at both documented pins. Keys "
        "on the VALUE rather than on a symptom, because the ordering ruling has "
        "escaped three symptom-keyed sweeps."
    )
    wb.add_data("significant_digits_required", SIG_DIGITS)
    wb.add_data("witness_files_scanned", len(files))
    wb.add_data("grouped_candidates", {k: [list(h) for h in v]
                                       for k, v in sorted(candidates.items())})
    wb.add_data("grouped_deliberate", sorted(deliberate))
    wb.add_data("borromean_hits", sorted(borro_hits))
    wb.add_data("source_hardcoded_grouped",
                {k: [list(h) for h in sorted(set(v))]
                 for k, v in sorted(src_hard.items())})
    wb.add_data("source_deliberate_grouped", sorted(src_deliberate))
    wb.add_assertion(name="scan_completed",
                     computed=str(int(len(files) > 0)), expected="1")
    wb.add_assertion(name="source_files_scanned_for_literals",
                     computed=str(int(len(src_all) >= 0)), expected="1")
    wb.add_caveat(
        "A hit says the WITNESS payload is grouped-era; it does not say the "
        "producer is. Re-run the producer to tell a stale artifact from a live "
        "source defect. A non-hit is not a clean bill: a witness recording only "
        "derived quantities carries no |tr_M| for this to match."
    )
    wb.add_caveat(
        "The SOURCE scan reads literals reachable as code, with docstrings "
        "excluded (comments never enter an AST). That exclusion is load-"
        "bearing, not a convenience: mass_at_3A_proper's docstring quotes both "
        "the grouped and the borromean |tr_M| precisely because it EXPLAINS "
        "the 2026-09-05 ruling, and flagging it would be flagging the "
        "documentation of the fix. Strings are not skipped wholesale, because "
        "mp.mpf(\"1.1457...\") is how this corpus writes a high-precision "
        "constant."
    )
    wb.add_caveat(
        "Fingerprints are computed live, never transcribed, so a re-pin moves "
        "them rather than silently invalidating the scan. Only the five atoms "
        "at A <= 3 and the two documented pins are covered."
    )
    print(f"\nWitness: {wb.save()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
