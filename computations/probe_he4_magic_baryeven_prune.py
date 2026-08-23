#!/usr/bin/env python3
"""EXPLORATORY structural pruning (per .claude/skills/local/production-vs-exploratory-discipline.md).

Formalize-first PRUNING — does NOT propose a closed form (Δ_λ gate: no 7th
fit-ansatz) and does NOT promote any near-match. It excludes published
magic-factor candidates by a symmetry (bar-involution) argument.

PROBE — the ⁴He magic-closure factor must be BAR-EVEN (q ↦ q⁻¹ invariant)
=======================================================================

w5tg's open "magic-α" blocker: the ⁴He doubly-magic shell-closure factor
    f(⁴He)/Z·N ≈ 2.0715
(the +47% super-additive enhancement over the Z·N inter-nucleon pair count;
a567 workplan, witness binding-factor-f-sequence) has no derived closed form.
a567 tested the two best near-misses `1+q` (+1.86%) and `2√q` (+1.72%) and
recorded them as "not close enough to claim, not far enough to rule out."

STRUCTURAL CONSTRAINT (formalize-first). The bar-involution q ↦ q⁻¹ is the
chirality / mirror operation. Per Lever-3 (thb7, A=3 mirror): the bar-ODD
(sinh) channel carries the p↔n (n−p) isospin asymmetry; the bar-EVEN (cosh)
channel is mirror-symmetric. ⁴He has N = Z = 2, so it is SELF-MIRROR under
p↔n ⇒ its binding has ZERO bar-odd component ⇒ the magic-closure factor must
be a BAR-EVEN function of q (invariant under q ↦ q⁻¹), i.e. a function of
[2]_q = q + q⁻¹ alone. (The atomic trace Δtr(⁴He, q) is itself bar-even
because the self-mirror word maps to itself under the bar involution; the
extracted f therefore inherits bar-evenness.)

  Adjacent, NOT the same: z2bn just proved the binding-kernel COEFFICIENT
  τ is bar-even in [2]_q (`tau_bar_even`, PR #2774). τ is the depth-2
  recurrence trace; the magic FACTOR here is a distinct 4-body object. This
  probe is the orthogonal magic-factor leg of the bar-even structure.

CONSEQUENCE — the two published near-misses are STRUCTURALLY EXCLUDED:
    1+q   not bar-even (1 + q⁻¹ ≠ 1 + q)      ⇒ cannot be the magic factor
    2√q   not bar-even (2√(q⁻¹) ≠ 2√q)        ⇒ cannot be the magic factor
Their numerical proximity is a coincidence of the FORBIDDEN (bar-odd) family,
not a lead — the q-locality / selection-bias trap (production-vs-exploratory
§Antipattern 2) made structural.

DISCIPLINE — no promotion. Bar-even forms DO sit near the target (e.g.
[2]_q + (q−q⁻¹)² ≈ 2.055, −0.82%). This probe does NOT promote any of them:
a sub-1% bar-even near-match selected by AME-match is the selection-bias form
of fitting, not a derivation. The CLOSURE of the magic factor stays the open
Demazure crystal-closure / operator-valued LR-branching problem (a567's
nominated mechanism). This probe only PRUNES: remove the bar-odd candidates,
constrain the survivors to the bar-even (= [2]_q-functional) family.

Usage:
    python3 probe_he4_magic_baryeven_prune.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))  # for witness_base
set_compute_dps()

# Canonical muon-pinned substrate q₀ (computations/q_parameter.py::Q); the
# bar-symmetry argument is q-independent, so the exact value is only used for
# the illustrative numerics below.
Q0 = mp.mpf("1.1099785955573347")
# a567 witnessed magic factor f(⁴He)/Z·N (binding-factor-f-sequence.witness.json).
TARGET = mp.mpf("2.0715")
BAR_EVEN_TOL = mp.mpf("1e-18")


def is_bar_even(f) -> bool:
    """True iff f(q) == f(q⁻¹) at q₀ (necessary condition for the magic factor)."""
    return abs(f(Q0) - f(1 / Q0)) < BAR_EVEN_TOL


# (label, f, published?) — the two a567 near-misses + bar-even substrate forms.
CANDIDATES = [
    ("1+q                (a567)", lambda x: 1 + x, True),
    ("2*sqrt(q)          (a567)", lambda x: 2 * mp.sqrt(x), True),
    ("[2]_q = q+q^-1",          lambda x: x + 1 / x, False),
    ("1+(q+q^-1)/2",            lambda x: 1 + (x + 1 / x) / 2, False),
    ("[2]_q + (q-q^-1)^2",      lambda x: (x + 1 / x) + (x - 1 / x) ** 2, False),
    ("cosh(2 ln q) + 1",        lambda x: mp.cosh(2 * mp.log(x)) + 1, False),
]


def main() -> None:
    print("=" * 74)
    print("PROBE — ⁴He magic-closure factor must be BAR-EVEN (q ↦ q⁻¹ invariant)")
    print("=" * 74)
    print(f"q₀ = {mp.nstr(Q0, 12)}   target f(⁴He)/Z·N = {mp.nstr(TARGET, 8)}")
    print("⁴He is self-mirror (N=Z=2) ⇒ zero bar-odd ⇒ magic factor is bar-even.")
    print()
    print(f"{'candidate':<26}{'value@q₀':>10}{'err':>9}{'bar-even?':>11}  verdict")
    excluded, survivors = [], []
    for label, f, published in CANDIDATES:
        v = f(Q0)
        err = (v - TARGET) / TARGET
        even = is_bar_even(f)
        if published and not even:
            verdict = "EXCLUDED (bar-odd — cannot be the factor)"
            excluded.append(label)
        elif even:
            verdict = "admissible (bar-even) — NOT promoted"
            survivors.append((label, float(err)))
        else:
            verdict = "bar-odd (not a candidate)"
        print(f"{label:<26}{float(v):>10.4f}{float(err)*100:>8.2f}%"
              f"{str(even):>11}  {verdict}")
    print()
    print("-" * 74)
    print("RESULT")
    print("-" * 74)
    print(f"  • STRUCTURALLY EXCLUDED (bar-odd, published near-misses): "
          f"{', '.join(e.split()[0] for e in excluded)}")
    print("    Their +1.7–1.9% proximity is a coincidence of the forbidden")
    print("    (chirality-odd) family — not a lead.")
    closest_lab, closest_err = min(survivors, key=lambda s: abs(s[1]))
    print(f"  • Admissible survivors lie in the bar-even (= [2]_q-functional)")
    print(f"    family; the closest illustrative one is "
          f"'{closest_lab.strip()}' ({abs(closest_err)*100:.2f}%) — DELIBERATELY NOT")
    print("    promoted (a sub-1% AME-selected near-match is fitting, not a")
    print("    derivation; Δ_λ gate). Closure stays the open Demazure /")
    print("    operator-valued LR-branching problem (a567 nominated mechanism).")
    print()
    print("  ⇒ NET (scope-(b) structural exclusion via a parity invariant): the")
    print("    correct ⁴He magic factor is bar-even; the two published")
    print("    substrate-constant near-misses are ruled OUT, narrowing w5tg's")
    print("    search to the bar-even/Demazure family.")
    print("=" * 74)

    _emit_witness(excluded, survivors)


def _emit_witness(excluded, survivors) -> None:
    try:
        import _path_bridge  # noqa: F401 — Phase-6 substrate path shim
        from witness_base import WitnessBuilder
    except Exception as e:  # pragma: no cover — keep probe runnable standalone
        print(f"[witness skipped: {e}]")
        return
    w = WitnessBuilder("probe-he4-magic-baryeven-prune", engine="mpmath")
    w.set_description(
        "EXPLORATORY structural pruning: the ⁴He magic-closure factor must be "
        "bar-even (q↦q⁻¹ invariant) because ⁴He is self-mirror (N=Z=2); this "
        "structurally excludes the published near-misses 1+q and 2√q (bar-odd). "
        "No closed form proposed; no near-match promoted (Δ_λ gate).")
    w.add_parameter("q0", mp.nstr(Q0, 30))
    w.add_parameter("target_f_he4_over_ZN", mp.nstr(TARGET, 8))
    w.add_data("excluded_bar_odd", excluded)
    w.add_data("bar_even_survivors_not_promoted",
               {lab: f"{err*100:+.2f}%" for lab, err in survivors})
    # assert-the-refutation: allPassed=true on the EXPECTED outcome (the two
    # published near-misses are bar-odd ⇒ structurally excluded).
    both_excluded = int(len(excluded) == 2)
    w.add_assertion(
        "published_near_misses_1plusq_2sqrtq_are_bar_odd_excluded",
        computed=both_excluded, expected=1, tolerance=None,
        source="bar-involution q↦q⁻¹; ⁴He self-mirror ⇒ magic factor bar-even")
    w.set_audit_only(
        "docs/audits/2026-06-25-he4-magic-factor-bar-even-pruning.md")
    out = w.save({"q0Anchor": "independent",
         "q0AnchorReason": (
            'Reads no substrate value. PROVED by running this producer'
            'under QOU_Q0_ANCHOR=muon and =proton and diffing the emitted'
            'witness: the only non-ephemeral leaves that differ are'
            'q0Anchor and q0Value THEMSELVES -- every substantive field is'
            'byte-identical, so the pin changes the label and nothing else.'
            'Its previous `muon` label was therefore a false claim that'
            'this producer computed at that anchor. `independent` is the'
            'honest disposition; a q0_anchor_manifest entry would be the'
            'WRONG fix, promoting a false claim into a declared one. Bean'
            'qou-o922, class (ii).'
         )})
    print(f"[witness → {out}]")


if __name__ == "__main__":
    main()
