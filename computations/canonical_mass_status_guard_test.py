#!/usr/bin/env python3
"""Both-directions regression for the canonical-mass status guard.

The guard's filters are tuned AGAINST the live tree, so a test that scans the
live tree proves nothing — it would pass by construction and keep passing after
a change that silences a real defect. Every case here drives
`docstring_hits()` with a fixture instead.

The controls that matter:

  * CATCHES — the pre-fix `mass_table_comprehensive.py` docstring, verbatim.
    This is the defect the .py pass was built for (PR #4822). Two of the three
    guard designs tried during that work failed exactly here: the naive
    per-line version buried it among 34 hits, and the whole-docstring-negation
    version silenced it outright. Any future change to SUMMARY_SCOPE,
    NAMES_THE_GAP, NEGATION_WINDOW or the regexes must keep this red.
  * CLEARS — one fixture per rule added during the qou-efcv triage, each taken
    from the real docstring that motivated it.

Run: python3 computations/canonical_mass_status_guard_test.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import canonical_mass_status_guard as G  # noqa: E402


def hits(doc: str) -> list[tuple[str, int, str]]:
    """Run the docstring pass over a fixture, as `scan()` would."""
    return G.docstring_hits("fixture.py", 1, doc.splitlines())


# ── The control: the real pre-fix docstring (git 4f760bad^) ──────────────────
# Its summary carries NO scope marker ("full mass/binding table at current
# production tier"), the formula line names no gap, and the nearby
# "KNOT ATLAS" / "not-computed" text must NOT negate it — the missing leading
# word boundary in `NOT\b` matching the NOT inside KNOT is what hid this hit.
STALE_MASS_TABLE = '''"""mass_table_comprehensive.py — full mass/binding table at current production tier.

Computes absolute masses AND binding energies for all nuclei from
proton (A=1) through ¹²C (A=12), using the current production
infrastructure:

  ABSOLUTE MASS:
    m(K) = m_e · [Vol(𝓑₃)/ℏ_q²] · λ_A · (1 ± Δm/(2·M_N))

  where λ_A = Family A (PROVED), Δm/M_N = substrate-pure flavor-split
  (PROVED per PR #942). Proton gets −Δm/2, neutron gets +Δm/2.

  KNOT ATLAS CROSS-REFERENCE:
    Each entry carries the methodology tag from the recursive atom
    knot atlas — principled-derivation, magic-A-formula, or not-computed.
"""'''

# ── One fixture per clearing rule (all from real docstrings) ─────────────────
SUMMARY_EXPLORATORY = '''"""EXPLORATORY (UNPROVED — do not wire into production vol_density).
Top-down spectral-phase correction to the Borromean linking weight.

The leading VolDensity (Vol/ℏ² × lw_A) × m_e gives the AVERAGE
nucleon mass m_avg, and is +2.89 % high.  The correction is the
rotation angle of the Borromean braid.
"""'''

SUMMARY_COUNTERFACTUAL = '''"""The \'categorically-exact\' linking weight that would make
    m_p match CODATA exactly.

        m_p = m_e · (Vol(𝓑₃)/ℏ_q²) · linking_weight_exact
"""'''

ABSENCE_DISCLAIMER = '''"""borromean_binding_recompute.py — the SINGLE Borromean per-knot pipeline.

Complete nuclear-binding recompute through ONE pipeline (no special-casing,
no m_e·Vol(𝓑₃)): every nucleus AND every nucleon mass flows from the same
Borromean H_3 trace.
"""'''

NAMES_GAP = '''"""Per-block vs global wiring probe.

This script computes both readings, order-by-order in h = q − q⁻¹,
per knot (proton / neutron at H₃), and reports the recovered fraction
of the +2.89 % m_p gap — RAW.  No tuning to m_p or B_AME.
"""'''

# `m_p-pin` names the q₀ anchor, not a proton-mass value.
MP_PIN_ANCHOR = '''"""Q_β c_k truncation-order analysis.

  FACT B (discipline camp): c_3 = -2 is a q₀-dependent near-match
                            (-2.0097 at muon-pin q₀, -2.0693 at m_p-pin
                            q₀ — a 3.47% m_p-pin swing).
"""'''

# A summary marker about a DIFFERENT object must not grant blanket immunity:
# "derive or refute the 2.38× bridge" is about the bridge, and the docstring
# then labels the deprecated form "Production (m_p path)". Restricting the
# summary check to scope markers (not all of NEGATED) is what keeps this red.
SUMMARY_MARKER_IS_ABOUT_SOMETHING_ELSE = '''"""Yekutieli volume-join derivation — derive or refute the 2.38× bridge.

Task (2026-06-01, branch claude/yekutieli-volume-join-derivation):
Does the q-hyperbolic VOLUME evaluation (the Archimedean functor\'s action
in the Yekutieli non-abelian Stokes step) supply exactly the q-dependent
factor that maps the H₃ per-block Markov trace tr_M to the production
GLOBAL scalar linking_weight = (3q²+4+3q⁻²)/4, at ALL orders in
h = q − q⁻¹?

  Production (m_p path):   m = m_e · Vol(𝓑₃)/ℏ_q² · linking_weight
"""'''


CASES: list[tuple[str, str, bool]] = [
    ("pre-fix mass_table_comprehensive docstring", STALE_MASS_TABLE, True),
    ("summary marker about another object", SUMMARY_MARKER_IS_ABOUT_SOMETHING_ELSE, True),
    ("EXPLORATORY summary scope marker", SUMMARY_EXPLORATORY, False),
    ("counterfactual summary ('would make')", SUMMARY_COUNTERFACTUAL, False),
    ("absence disclaimer ('no m_e·Vol')", ABSENCE_DISCLAIMER, False),
    ("names the gap", NAMES_GAP, False),
    ("m_p-pin is a q₀ anchor", MP_PIN_ANCHOR, False),
]


def check_line_exemptions() -> list[str]:
    """A LINE_EXEMPTIONS entry must clear its line AND lapse when it is edited.

    The whole point of hashing the content rather than the path is that an
    exemption cannot outlive the sentence it was granted for.
    """
    problems: list[str] = []
    md = (Path(__file__).resolve().parent.parent / "docs" / "precision-goals.md")
    if not md.exists():
        return problems
    live = {G.hashlib.sha256(l.strip().encode()).hexdigest()[:12]
            for l in md.read_text(encoding="utf-8").splitlines()}
    for h, why in G.LINE_EXEMPTIONS.items():
        if h not in live:
            problems.append(f"exemption {h} ({why}) matches no line — the text changed; re-review it")
    for h in list(G.LINE_EXEMPTIONS)[:1]:
        sample = next(l for l in md.read_text(encoding="utf-8").splitlines()
                      if G.hashlib.sha256(l.strip().encode()).hexdigest()[:12] == h)
        if not G.is_exempt_line(sample):
            problems.append(f"exemption {h} does not clear its own line")
        if G.is_exempt_line(sample + " (edited)"):
            problems.append(f"exemption {h} survived an edit to its line — not content-addressed")
    return problems


def main() -> int:
    failures = 0
    for name, doc, want_hit in CASES:
        got = hits(doc)
        ok = bool(got) == want_hit
        verb = "flags" if want_hit else "clears"
        print(f"  {'PASS' if ok else 'FAIL'}  guard {verb}: {name}")
        if not ok:
            failures += 1
            print(f"        expected {'≥1 hit' if want_hit else 'no hits'}, got {got}")

    # The corrected docstring of the file that motivated the pass must be clean.
    live = Path(__file__).resolve().parent / "mass_table_comprehensive.py"
    if live.exists():
        live_hits = [h for h in G.scan(scan_py=True) if h[0].endswith("mass_table_comprehensive.py")]
        ok = not live_hits
        print(f"  {'PASS' if ok else 'FAIL'}  guard clears: corrected mass_table_comprehensive.py (live)")
        if not ok:
            failures += 1
            print(f"        got {live_hits}")

    exempt_problems = check_line_exemptions()
    print(f"  {'PASS' if not exempt_problems else 'FAIL'}  LINE_EXEMPTIONS are live and content-addressed")
    for p in exempt_problems:
        failures += 1
        print(f"        {p}")

    # --strict must be green: the guard is only usable as a gate if it is.
    strict_hits = G.scan(scan_py=True)
    ok = not strict_hits
    print(f"  {'PASS' if ok else 'FAIL'}  --strict is green on the live tree")
    if not ok:
        failures += 1
        for h in strict_hits:
            print(f"        {h[0]}:{h[1]}")

    print(f"\n{'OK' if not failures else str(failures) + ' FAILURE(S)'} — "
          f"{len(CASES) + 3} checks")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
