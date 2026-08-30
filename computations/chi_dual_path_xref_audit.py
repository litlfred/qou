#!/usr/bin/env python3
# polynomial_q_not_applicable: read-only audit; pairs cached values, writes no witness.
"""Cross-check each χ cache against the markov-peel scalar — and say which
anchor every leg of that comparison is standing on.

## The capability this restores

`_b0vf_complete_he4_witness.py` guarded its ⁴He write with GATE B: the Wenzl
Frobenius pairing Σ_λ y_λ χ_λ and the markov-peel scalar are two independent
implementations of the SAME canonical Markov trace, so they must agree. It
recorded the result in the witness as `tr_M_markov_peel_xref` and
`tr_M_dual_path_rel_gap`.

That producer was a one-off at the muon pin. The proton-anchored rebuild
(4fb4ac54) went through the canonical producer, which never computed the
cross-check, so both fields left the corpus and no χ cache carries a dual-path
check today. This audit is that check, read-only and over every atom instead of
one — the capability, not the two stale numbers.

## What running it found

The comparison has three legs, and they are no longer on the same anchor:

    χ tables        MIXED — deuteron/⁴He/proton proton-pinned,
                    tritium/helium-3/neutron still muon-pinned
    y_λ weights     muon   (`y-lambda-mpfr-witness.json`)
    markov-peel     muon   (`markov/markov-peel-atomic-tr-m.witness.json`)

Measured relative gap Σyχ vs peel, per atom:

    proton     proton χ     2.221e-50      neutron     muon χ     1.237e-51
    tritium      muon χ     9.111e-20      helium-3    muon χ     9.111e-20
    deuteron   proton χ     1.704e-07      helium-4  proton χ     3.261e-07

Same pin throughout agrees to ~1e-19 — which is also what the peel producer's
own header claims ("peel agrees with the chi-cache leg at ~1e-19"). Cross-pin
lands at 1e-7, twelve orders worse. ⁴He is the controlled experiment: the same
77-partition table scored 9.111e-20 before the rebuild and 3.261e-07 after,
with nothing but the anchor changed.

Two things in that table are observations, not conclusions, and are recorded
rather than smoothed over:

- **`proton` is cross-pinned yet agrees to 2.221e-50.** Both A=1 atoms are
  insensitive to the split, so the single-nucleon comparison is not testing the
  anchor at all. Whether that is a cancellation at n=3 or the peel row for A=1
  being derived from the same inputs (which would make it circular) is not
  established here. It is still reported ANCHOR_SPLIT: agreement reached by
  comparing two different pins is not evidence, however small the number.
- **The same-pin floor moves with n** — 1e-50 at n=3, 9.111e-20 at both n=9 and
  n=12. Tritium and helium-3 landing on the *identical* 9.111e-20 points at a
  shared input (most likely the y_λ table's precision at that n) rather than
  anything atom-specific. Nothing above n=12 has been measured, so the floor is
  characterised only over the range this corpus covers.

## Why this is worse than a failing gate

GATE B's tolerance is `10·B_D`, where B_D is the deuteron's own dual-path gap.
The deuteron is cross-pinned too, so B_D inflated to 1.704e-07 along with
everything else, and 10·B_D = 1.7e-06 now comfortably admits ⁴He's 3.261e-07.
**The gate still passes.** Its bound floats up with the contamination it exists
to detect, so it has silently stopped discriminating rather than gone red.

That also retires the premise in that gate's docstring — an "intrinsic
two-implementation gap" of ~4.8e-8 which the deuteron supposedly proved
unavoidable. Three complete same-pin atoms agree to 9.111e-20. The 4.8e-8 was
never intrinsic; it was the deuteron's anchor mismatch, measured and then
promoted to a constant of nature.

## This is the documented "layer straddle", not staleness

**Corrected 2026-08-08.** An earlier version of this header called the two muon
legs stale and predicted they would re-anchor on their next run. That was
wrong, and running them disproved it: `q_pinning_50_digit` and
`atomic_tr_m_mpfr_50dps` are both in `q0_anchor_manifest.json` `ideal_muon`
(257 entries), so they are muon **by design** and regenerate muon. The wave
rejected both, correctly.

What the table above actually measures is the defect AGENTS.md §"q₀ anchor
convention" (STRICT) already names:

> **Never straddle the two layers inside one quantity.** Mixing an ideal-layer
> input with an experimental-layer input in a single computed number is a
> defect regardless of its size. … the μ₃ Fréchet probe took `y_λ` from the
> muon-built cache while evaluating `χ_λ` at the proton `q₀` — an 11.54 ppb
> layer separation … ~1e-7 relative on the result.

That is this measurement, arrived at independently: proton χ against muon y_λ,
~1e-7 relative. The 11.54 ppb is the μ–p substrate tension itself. So the
number is real and the diagnosis is settled — it is a layer boundary being
crossed, not a witness lagging its producer.

**The fix is therefore NOT to re-pin the shared y_λ cache.** That cache is the
ideal-layer artifact and 257 ideal_muon producers read it; flipping it to
proton straddles the ideal layer in the other direction. Measured: with y_λ on
the proton pin, `atomic_tr_m_mpfr_50dps` (ideal_muon) moved 49 fields. AGENTS.md
gives the intended route for experimental-anchor compute — call the live closed
form `schur_principal_mpmath.y_lambda_at_q0_mpmath(n, q)`.

It used to add that `wedderburn_jones_markov.y_lambda_at(n, q)` serves a
muon-built cache whenever `|q − q_parameter.Q| < 1e-12`, a gate a caller passing
`q_parameter.Q` satisfies trivially. CORRECTED 2026-08-29: that mechanism is dead. `y_lambda_at`'s live body reads no file at all -- it delegates to `y_lambda_su_n` at whatever q it is handed. The `1e-12` cache gate survives only inside `_y_lambda_at_convention_C_HISTORICAL` (dead, convention C, excised 2026-08-09), and the cache FILE was re-derived to convention D and re-pinned to proton in the same cascade. Verified by reading the body, not inferred. This file's CHOICE is unaffected; only the reason was stale. The μ₃ straddle described
above is real history and is unaffected — only its mechanism is obsolete.

Which anchor the χ family should carry is **owner-gated** (AGENTS.md; bean
`tnjb`), so this audit reports the split and does not resolve it.

## Why the anchors sit where they do

`q_parameter` is **anchor-adaptive**, which is why one function answered two
ways during this investigation. `Q_50_DIGIT_STR` / `Q_MP` are proton
(`1.1099785827513808…`) by default, but under `QOU_Q0_ANCHOR=ideal` — or when
the running producer's stem is in `q0_anchor_manifest.json` `ideal_muon` —
`q_at`/`q_str` rebind to the muon string. So the same `q_at` call returns
proton from a plain shell and muon from inside `q_pinning_50_digit.py`. Read a
q₀ without knowing which of those you are in and you will misattribute the
result, as the first cut of this header did.

Chain, measured rather than assumed:

    q_pinning_50_digit.py        ideal_muon   -> q-pinning-50-digit.witness.json
    atomic_tr_m_mpfr_50dps.py    ideal_muon   -> atomic-tr-m-mpfr-50dps.witness.json
    markov_peel_atomic_witness.py  unlisted   -> reads the bridge above
    regenerate_y_lambda_mpfr.py    unlisted   -> y-lambda-mpfr-witness.json

The bridge is where the peel gets its q₀ — not from `q_parameter` — so the peel
inherits the ideal layer through it.

Bean **`qou-n1c4`** tracks the open decision. It is not a regeneration wave:
regenerating changes nothing, because the muon legs are already emitting what
their manifest class says they should.

Verdicts: `AGREES` (one pin, gap at the intrinsic floor), `DISAGREES` (one pin,
gap above it — a real χ defect), `ANCHOR_SPLIT` (legs on different pins, so the
number measures the split and not the χ), `INCOMPLETE` (partial χ table, so Σ
is not the full trace), `SKIPPED`.

Read-only. Runs no producer and writes no witness, so it is safe beside other
work.

Usage:
    python3 computations/chi_dual_path_xref_audit.py
    python3 computations/chi_dual_path_xref_audit.py --atom helium-4
    python3 computations/chi_dual_path_xref_audit.py --self-test
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

PEEL_WITNESS = HERE / "markov" / "markov-peel-atomic-tr-m.witness.json"
Y_LAMBDA_WITNESS = HERE / "y-lambda-mpfr-witness.json"

PROTON_PREFIX = "1.10997858275"
MUON_PREFIX = "1.10997859555"

# Measured floor for two same-pin implementations of one Markov trace: three
# complete atoms (tritium, helium-3, and ⁴He before its rebuild) all land at
# 9.111e-20, and the peel producer's own header independently claims ~1e-19.
# The bound sits three orders above that floor and eight below the 1e-7 of a
# cross-pin comparison, so it separates the two decisively without being tuned
# to either. It is NOT derived from a measured witness gap the way `10·B_D`
# was — that is exactly how the old gate came to scale with its own defect.
INTRINSIC_MAX = 1e-15

ATOMS = {"proton": (1, 0), "neutron": (0, 1), "deuteron": (1, 1),
         "tritium": (1, 2), "helium-3": (2, 1), "helium-4": (2, 2)}


def anchor_of(q) -> str | None:
    """'proton' / 'muon' / None, from a q₀ decimal string."""
    if q is None:
        return None
    s = str(q).strip()
    if s.startswith(PROTON_PREFIX):
        return "proton"
    if s.startswith(MUON_PREFIX):
        return "muon"
    return None


def verdict(gap, anchors, n_chi: int, n_parts: int) -> str:
    """Judge one atom. Pure — self-tested below.

    `anchors` is the pin of each leg (χ, y_λ, peel); None means unrecognised.
    Order of the checks is the point of the function:

    1. No measurement at all -> SKIPPED.
    2. A partial χ table -> INCOMPLETE. Σ over a subset is not the trace, so
       the gap is meaningless before the anchors are even considered.
    3. Legs on different pins -> ANCHOR_SPLIT, *whatever the gap is*. This
       precedes the numeric verdict deliberately: a cross-pin comparison that
       happens to land under the bound is not a passing check, it is a check
       that did not happen. Ordering it after the bound is precisely the bug
       GATE B has.
    """
    if gap is None:
        return "SKIPPED"
    if n_parts and n_chi != n_parts:
        return "INCOMPLETE"
    known = [a for a in anchors if a is not None]
    if len(known) != len(anchors) or len(set(known)) > 1:
        return "ANCHOR_SPLIT"
    return "AGREES" if gap <= INTRINSIC_MAX else "DISAGREES"


def _measure(atom: str, Z: int, N: int):
    """(gap, anchors, n_chi, n_parts) for one atom. Import-heavy; lazy."""
    import _path_bridge  # noqa: F401
    import mpmath as mp
    from tr_m_wenzl_bridge_mpfr import load_y_lambda_for_q0

    n = 3 * (Z + N)
    chi_path = HERE / f"chi-{atom}-h{n}-at-q0-50dps.witness.json"
    if not chi_path.exists():
        return None, (None, None, None), 0, 0

    mp.mp.dps = 60
    cw = json.loads(chi_path.read_text(encoding="utf-8"))
    chi = {tuple(e["partition"]): mp.mpf(e["chi_lambda"])
           for e in cw.get("by_partition", []) if "chi_lambda" in e}
    if not chi:
        return None, (None, None, None), 0, 0

    pw = json.loads(PEEL_WITNESS.read_text(encoding="utf-8"))
    # Pair each χ with y_λ at ITS OWN pin rather than with one shared cache.
    # The accessor refuses to cross the boundary, so a missing counterpart
    # surfaces as a raise here instead of as a silent ~1e-7 error downstream.
    chi_q0 = cw.get("q_0_50dps")
    y = load_y_lambda_for_q0(n, chi_q0)
    y_anchor = anchor_of(chi_q0)
    anchors = (anchor_of(chi_q0), y_anchor,
               anchor_of((pw.get("parameters") or {}).get("q0")))
    peel = None
    for r in pw["data"]["results"]:
        if r["Z"] == Z and r["N"] == N:
            peel = mp.mpf(r["tr_M_at_q0"])
            break
    if peel is None or peel == 0:
        return None, anchors, len(chi), len(y)

    s = sum(mp.mpf(str(y[lam])) * c for lam, c in chi.items() if lam in y)
    return float(abs(s - peel) / abs(peel)), anchors, len(chi), len(y)


P, M = "proton", "muon"
CASES = [
    # The floor, measured on tritium / helium-3 / pre-rebuild ⁴He.
    ("one pin, gap at the intrinsic floor", 9.111e-20, (M, M, M), 30, 30,
     "AGREES"),
    ("one pin, gap above the floor is a real defect", 1e-7, (P, P, P), 11, 11,
     "DISAGREES"),
    # ⁴He today: the number is the anchor split, not a χ measurement.
    ("proton chi against muon upstreams", 3.261e-07, (P, M, M), 77, 77,
     "ANCHOR_SPLIT"),
    # The failure mode GATE B has: cross-pin, but small enough to slip a bound.
    # Ordering ANCHOR_SPLIT after the numeric test would call this AGREES.
    ("a cross-pin gap UNDER the bound is still not a check", 1e-20,
     (P, M, M), 11, 11, "ANCHOR_SPLIT"),
    ("all three legs must match, not just chi and peel", 9.111e-20,
     (P, M, P), 11, 11, "ANCHOR_SPLIT"),
    # An unrecognised q0 is not evidence of agreement.
    ("an unreadable anchor is never waved through", 9.111e-20, (P, P, None),
     11, 11, "ANCHOR_SPLIT"),
    # Incompleteness outranks the anchors: Σ over a subset is not the trace,
    # and calling it AGREES because the pins line up would be worse than the
    # cross-pin case — it would be a positive result off a partial sum.
    ("a partial chi table cannot be cross-checked", 1e-20, (M, M, M), 27, 77,
     "INCOMPLETE"),
    ("incompleteness outranks a matching anchor set", 9.111e-20, (M, M, M),
     76, 77, "INCOMPLETE"),
    ("nothing measured", None, (None, None, None), 0, 0, "SKIPPED"),
]


def self_test() -> int:
    fails = 0
    for label, gap, anchors, n_chi, n_parts, want in CASES:
        got = verdict(gap, anchors, n_chi, n_parts)
        ok = got == want
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}   (want {want}, got {got})")

    # The bound must not be derived from a witness. `10·B_D` was, and inflated
    # with the very contamination it was meant to catch; pin the constant so a
    # future edit cannot quietly reintroduce a floating tolerance.
    ok = INTRINSIC_MAX == 1e-15
    fails += not ok
    print(f"  {'ok  ' if ok else 'FAIL'}  the tolerance is a fixed constant, "
          f"not a measured gap")

    total = len(CASES) + 1
    print(f"\n{total - fails}/{total} passed")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--atom", action="append", help="restrict to these atoms")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()

    atoms = a.atom or list(ATOMS)
    print(f"{'atom':<11} {'chi':<7} {'y_lam':<7} {'peel':<7} {'parts':>7} "
          f"{'rel gap':>11}  verdict")
    bad = 0
    for atom in atoms:
        if atom not in ATOMS:
            print(f"{atom:<11} not a known atom")
            continue
        Z, N = ATOMS[atom]
        try:
            gap, anchors, n_chi, n_parts = _measure(atom, Z, N)
        except Exception as exc:  # noqa: BLE001
            print(f"{atom:<11} MEASURE FAILED: {type(exc).__name__}: {exc}")
            bad += 1
            continue
        v = verdict(gap, anchors, n_chi, n_parts)
        bad += v in {"DISAGREES", "ANCHOR_SPLIT"}
        ca, ya, pa = (x or "?" for x in anchors)
        fg = "n/a" if gap is None else f"{gap:.3e}"
        print(f"{atom:<11} {ca:<7} {ya:<7} {pa:<7} {n_chi:>3}/{n_parts:<3} "
              f"{fg:>11}  {v}")
    print("\nANCHOR_SPLIT is not a weak result, it is the absence of one: the "
          "two legs\nwere never compared at the same q0. This is the layer "
          "straddle AGENTS.md\nforbids (ideal-layer y_lambda against an "
          "experimental-layer chi), not stale\nwitnesses — the muon legs are "
          "`ideal_muon` in q0_anchor_manifest.json and\nregenerate muon by "
          "design. Re-running them changes nothing; re-pinning the\nshared "
          "y_lambda cache only straddles the ideal layer instead. Owner-gated: "
          "see\nbean qou-n1c4.")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
