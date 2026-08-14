#!/usr/bin/env python3
"""Every live consumer must handle every ctype the classifier can emit.

Why this exists
---------------
`canonical_braid_crossings.classify_crossing` gained a fourth label,
`averaged_weighted`, for the colour-weighted p-n interface. Four live
consumers carried their own `{sigma, sigma_inv, averaged}` tables and had no
idea, so `canonical_tr_m_via_rust.canonical_word_for` raised `KeyError` for
**every** `Z >= 1, N >= 1` nuclide -- deuteron, He-4, all of them -- while
the proton and neutron paths kept working, because a single-species word
carries no p-n interface. That asymmetry is why it reached `main`: the
proton path is the one most probes exercise (bean `qou-8zjd`).

It was the sixth instance of one pattern in this arc: *a private copy cannot
learn what the canonical one learns*. Three inline `d`-maps, two
`WITNESS_REF` regexes, two structural detectors -- each found by hand, after
the fact. Hand-finding does not scale to a seventh, so this test asks the
question mechanically:

  Part A -- for each known consumer, does it accept all of `CTYPES`?
  Part B -- does any file carry a *private* ctype vocabulary at all?

Part B is the one that generalises. Part A only knows the consumers it was
told about, which is the very failure mode being tested for.

Run: `python3 computations/test_ctype_consumer_coverage.py`
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "markov"))

from canonical_braid_crossings import CTYPES, d_for_ctype, sign_for_ctype  # noqa: E402

CANONICAL_MODULE = "canonical_braid_crossings"

# ── Part B baseline ────────────────────────────────────────────────────────
# Files that mention the ctype vocabulary without importing it. Each entry
# needs a reason. Per AGENTS.md the ratchet drains and never grows: do NOT
# add a file here to make this test pass -- import from the canonical module
# instead. An entry is removable the moment its file is repointed.
# Triaged 2026-08-14. Each of these NAMES the vocabulary in prose or counts
# label occurrences; none maps a label to a `d`, a sign, or a matrix, so none
# can substitute a wrong value the way the four repaired consumers did. The
# three that DID map values -- atom_level_wedderburn_tower (private `d_for`
# dict), audits/term5_aK_audit (private classifier), and
# theta_mn_linearchain_vs_allpairs (a regex whose closing quote made
# 'averaged' fail to match 'averaged_weighted', dropping the one interface
# crossing it exists to count) -- were repaired rather than baselined.
PRIVATE_VOCAB_BASELINE: dict[str, str] = {
    "audits/braid_encoding_audit.py": "prose table; counts '½' glyphs, not labels",
    "bk_crossing_coordination.py": "comment only",
    "delta_lambda_exponent_from_crossings.py": "prose derivation of the exponent slope",
    "free-neutron-decay.py": "prose table of quark-channel Hecke elements",
    "probes/charge_symmetry_bond_probe.py": "docstring naming the interface crossing",
    "probes/interface_factor_categorical_derivation_probe.py":
        "audits the module's own interface_factor('averaged') against z-h/2; "
        "the literal is the thing under test",
    "probes/qbeta_half_fill_probe.py": "prose; counts n_avg from a supplied tally",
    "qbeta/qlommel_b_ladder_slope_derivation.py": "emits a 'non_averaged' output key",
}

failures: list[str] = []
notes: list[str] = []


# ── Part A: registered consumers accept every ctype ────────────────────────
def _check(name, fn):
    """Call `fn(ctype)` for every ctype; record which ones it rejects."""
    bad = []
    for ct in CTYPES:
        try:
            fn(ct)
        except Exception as exc:  # noqa: BLE001 -- any rejection is a failure
            bad.append(f"{ct} ({type(exc).__name__})")
    if bad:
        failures.append(f"{name} rejects: {', '.join(bad)}")
    else:
        notes.append(f"  ok   {name}")


def part_a() -> None:
    print(f"Part A -- consumers vs CTYPES = {CTYPES}")

    _check("canonical_braid_crossings.d_for_ctype", lambda ct: d_for_ctype(ct, 0.2))
    _check("canonical_braid_crossings.sign_for_ctype", sign_for_ctype)

    import canonical_tr_m_via_rust as ctr
    _check("canonical_tr_m_via_rust.CTYPE_TO_SIGN", lambda ct: ctr.CTYPE_TO_SIGN[ct])

    import importlib
    wlr = importlib.import_module("markov.markov_trace_via_wenzl_lr")
    _check("markov_trace_via_wenzl_lr.CTYPE_TO_SIGN", lambda ct: wlr.CTYPE_TO_SIGN[ct])

    from markov import markov_peel
    _check("markov_peel.crossing_element", lambda ct: markov_peel.crossing_element(0, ct))

    import sympy as sp
    import tau_M_proton_closed_form_phase5l1 as t5
    _check("tau_M_proton_closed_form_phase5l1._cross_to_cd",
           lambda ct: t5._cross_to_cd(ct, sp.Symbol("q")))

    import chi_sym_alt_closed_form as csa
    _check("chi_sym_alt_closed_form.count_factor_types_from_crossings",
           lambda ct: csa.count_factor_types_from_crossings([(0, ct)]))

    import atom_level_wedderburn_tower as alwt  # noqa: F401 -- import-time check
    notes.append("  ok   atom_level_wedderburn_tower imports (private d_for removed)")

    # The marshallers are exercised through real words rather than raw
    # labels, since they take (c, d, gen) triples.
    from canonical_braid_marshalling import (
        marshal_to_chi_lambda_braid, marshal_to_symbolic_braid,
    )
    from hecke_core import h as h_val
    from mass_at_3A_proper import atom_braid_word_3A
    for Z, N, label in [(1, 0, "p"), (0, 1, "n"), (1, 1, "D"), (2, 2, "4He")]:
        word = atom_braid_word_3A(Z, N, include_inter=True)
        for fname, fn in [("marshal_to_symbolic_braid", marshal_to_symbolic_braid),
                          ("marshal_to_chi_lambda_braid", marshal_to_chi_lambda_braid)]:
            try:
                fn(word, h_val)
                notes.append(f"  ok   {fname}({label})")
            except Exception as exc:  # noqa: BLE001
                failures.append(f"{fname}({label}): {type(exc).__name__}: {exc}")


# ── Part A2: the classifier and the marshaller must not disagree ───────────
def part_a2() -> None:
    """A second classifier is only safe if it agrees with the first.

    This is the check that pins the silent half of the defect: the private
    classifier did not crash, it returned a *different label*, and the label
    resolved to a `d` that was wrong by 6.88e-4.
    """
    print("\nPart A2 -- marshalled classification == canonical classification")
    from canonical_braid_crossings import classify_crossing
    from canonical_braid_marshalling import marshal_to_symbolic_braid
    from hecke_core import h as h_val
    from mass_at_3A_proper import atom_braid_word_3A

    for Z, N, label in [(1, 0, "p"), (0, 1, "n"), (1, 1, "D"),
                        (1, 2, "T"), (2, 1, "3He"), (2, 2, "4He")]:
        word = atom_braid_word_3A(Z, N, include_inter=True)
        canon = [classify_crossing(float(c), float(d), h_val) for (c, d, _g) in word]
        marsh = [t for (_g, t) in marshal_to_symbolic_braid(word, h_val)]
        dis = [(i, a, b) for i, (a, b) in enumerate(zip(canon, marsh)) if a != b]
        if dis:
            i, a, b = dis[0]
            failures.append(
                f"{label}: {len(dis)}/{len(word)} classification disagreements; "
                f"first at crossing {i}: canonical {a!r} vs marshalled {b!r}"
            )
        else:
            notes.append(f"  ok   {label}: {len(word)} crossings agree")


# ── Part B: no new private vocabularies ────────────────────────────────────
def part_b() -> None:
    """Flag any file that names the ctype vocabulary without importing it.

    Heuristic, deliberately: it looks for a file that mentions BOTH
    `sigma_inv` and `averaged` (i.e. is doing something vocabulary-shaped)
    while not importing `canonical_braid_crossings`. High recall, and the
    baseline above carries the triaged exceptions.
    """
    print("\nPart B -- private ctype vocabularies")
    found: list[str] = []
    for path in sorted(HERE.rglob("*.py")):
        rel = path.relative_to(HERE).as_posix()
        if "_deprecated/" in rel or rel == "canonical_braid_crossings.py":
            continue
        if rel == Path(__file__).name:
            continue
        try:
            src = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if "sigma_inv" not in src or "averaged" not in src:
            continue
        if re.search(rf"\b{CANONICAL_MODULE}\b", src):
            continue
        found.append(rel)

    new = [f for f in found if f not in PRIVATE_VOCAB_BASELINE]
    stale = [f for f in PRIVATE_VOCAB_BASELINE if f not in found]

    for f in new:
        failures.append(
            f"NEW private ctype vocabulary in {f} -- import from "
            f"{CANONICAL_MODULE} instead of re-listing the labels"
        )
    for f in stale:
        notes.append(f"  note baseline entry no longer needed, drop it: {f}")
    if not new:
        notes.append(f"  ok   no new private vocabularies ({len(found)} baselined)")


# ── Part C: the blind spot Part B leaves open ──────────────────────────────
# Part B exits early on `if re.search(CANONICAL_MODULE, src): continue` --
# importing the canonical module buys a file a total exemption. That is
# backwards. A file that has never heard of the module is mostly harmless:
# nothing feeds it canonical crossings. The dangerous file is the one that
# calls `atom_canonical_crossings(...)` and THEN maps the labels with a table
# of its own, because it receives the new ctype and answers for it privately.
#
# Every defect the qou-uzk0 sweep found was in that exempted population --
# 14 files, all importing the module, all keeping a private table:
# four silent (spectral_coordinates_all_atoms substituted the IDENTITY for the
# interface, 199% on the affected generator; per_irrep_pole_atom miscounted;
# build_atomic_braid_recipe_d_chain asserted a false DERIVED breakdown;
# hoefsmit_symbolic's self-test reapplied the previous crossing) and ten
# raising, one of which (per_nucleon_shift_derivation) died at import.
# habiro_coefficients_interpolate managed both at once: it applied the
# COLOUR-WEIGHTED value under the colour-BLIND key.
#
# So Part B was blind to precisely the population it exists to protect. This
# part closes that: it looks for value-mapping shapes in importers.
_VALUE_MAP_PATTERNS = (
    # dict literal keyed by a ctype label: {"sigma": ..., "averaged": ...}
    re.compile(r"""\{\s*["']sigma["']\s*:"""),
    # if/elif dispatch: ctype == "averaged"
    re.compile(r"""==\s*["'](?:sigma|sigma_inv|averaged)["']"""),
    # membership set: {"sigma", "sigma_inv", "averaged"}
    re.compile(r"""\{\s*["']sigma["']\s*,"""),
)
#: Importers allowed to keep a value-shaped literal. Same ratchet discipline
#: as Part B: drains, never grows. Fix the file rather than adding a row.
#: Triaged 2026-08-14 (qou-uzk0). Two of the nine hits were real and were
#: repaired rather than listed: d_u_closed_form_proof (n_avg_inter counted
#: only `averaged`, so it was identically 0 for every Z>=1,N>=1 atom) and
#: probes/homflypt_operator_valued_probe (an informative "not representable"
#: refusal degraded into "unknown crossing type"). The seven below all treat
#: the two averaged kinds identically ALREADY, via an `else` or by excluding
#: both, so none can substitute a wrong value.
IMPORTER_VALUE_MAP_BASELINE: dict[str, str] = {
    "audits/term5_aK_audit.py":
        "`else` catches both averaged kinds and treats them as self-inverse",
    # The d-chain is no longer listed: it now names `averaged_weighted` and
    # passes on its own. These two are correct only because a single nucleon
    # has no p-n bond — neither is cross-checked against
    # `atom_canonical_crossings`, which is exactly how the d-chain carried a
    # wrong `averaged: 5` under trust_basis=DERIVED until this sweep. The
    # cross-check is bean qou-nmva.
    "build_atomic_braid_recipe_n_chain.py":
        "recipe DATA literal, not dispatch; correct (neutron has no p-n "
        "bond) but unverified — bean qou-nmva",
    "build_atomic_braid_recipe_p_chain.py":
        "recipe DATA literal, not dispatch; correct (proton has no p-n "
        "bond) but unverified — bean qou-nmva",
    "deltalambda/c_knot_nonuniversal_pinned_weight_probe.py":
        "counts writhe (sigma vs sigma_inv) only; excludes both averaged "
        "kinds by construction",
    "deltalambda/he4_binding_k_presentation_correction_probe.py":
        "dict of human-readable descriptions keyed by ctype, not values",
    "deltalambda/vol_t_he3_snappy_probe.py":
        "`else` catches both averaged kinds — neither is a topological "
        "crossing, which is the only distinction this probe makes",
}


def part_c() -> None:
    print("\nPart C -- importers that still map ctype labels privately")
    found: list[str] = []
    for path in sorted(HERE.rglob("*.py")):
        rel = path.relative_to(HERE).as_posix()
        if "_deprecated/" in rel or rel == "canonical_braid_crossings.py":
            continue
        try:
            src = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        # only importers -- the exact population Part B waves through
        if not re.search(rf"\b{CANONICAL_MODULE}\b", src):
            continue
        # Two ways to be fine, and the second matters: resolving through the
        # canonical helpers, OR naming `averaged_weighted` explicitly. The
        # second is not a loophole — comparing against ctype labels is often
        # correct (converting to a signed word, counting writhe), and what
        # made every defect in this class silent was that the label was never
        # mentioned at all. Requiring the mention is what drains: an author
        # who writes it has had to decide what the interface does.
        if re.search(r"\b(d_for_ctype|sign_for_ctype|CTYPES)\b", src):
            continue
        if "averaged_weighted" in src:
            continue
        if any(p.search(src) for p in _VALUE_MAP_PATTERNS):
            found.append(rel)

    new = [f for f in found if f not in IMPORTER_VALUE_MAP_BASELINE]
    stale = [f for f in IMPORTER_VALUE_MAP_BASELINE if f not in found]
    for f in new:
        failures.append(
            f"{f} calls into {CANONICAL_MODULE} and still maps ctype labels "
            f"with a private table -- use d_for_ctype / sign_for_ctype / "
            f"CTYPES so a new ctype cannot be answered for privately"
        )
    for f in stale:
        notes.append(f"  note Part C baseline entry no longer needed: {f}")
    if not new:
        notes.append(
            f"  ok   no importer maps ctypes privately "
            f"({len(found)} baselined)"
        )


def main() -> int:
    part_a()
    part_a2()
    part_b()
    part_c()
    print("\n".join(notes))
    if failures:
        print(f"\nFAIL ({len(failures)}):")
        for f in failures:
            print(f"  ✗ {f}")
        return 1
    print("\nPASS -- every consumer covers every ctype")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
