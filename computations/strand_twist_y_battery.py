#!/usr/bin/env python3
"""Strand-twist hypercharge battery — EXPLORATORY enumeration probe.

Scope (honest): this is a *candidate-space feasibility* battery for the
per-strand framing datum (``def:strand-twist-datum``), NOT a framework
derivation. It enumerates helon-style twist assignments (three strands
per first-generation fermion, per-strand twists in {-1, 0, +1}; Bilson-
Thompson precedent) and asks which assignments make the candidate

    Y_t(f) = 2 * (Q_twist(f) - I3(f)),   Q_twist = totalTwist / 3

reproduce the Standard Model first-generation hypercharge spectrum, the
Baez-Huerta Z6 compatibility (tau/3 + w/2 + Y/2 integral), and the
nucleon-doublet Gell-Mann-Nishijima consistency. Surviving assignments
are reported IN FULL (no cherry-picking); uniqueness or its failure is
part of the result.

What this probe does NOT do: it does not derive the twist values from
the framework's own braid words (the corpus carries no per-chiral-
fermion framed braid words yet — that gap is recorded in the witness),
and nothing here is wired to production. The open content remains
``conj:sm-hypercharge-invariant``.

Exact rational arithmetic throughout (fractions.Fraction); no floats,
no fitted parameters. The normalisation 1/3 is the colour-tube charge
quantum, fixed once structurally — not tuned.
"""

from __future__ import annotations

import itertools
from fractions import Fraction as Fr

import _path_bridge  # noqa: F401  (canonical sys.path bridge)
from witness_base import WitnessBuilder  # noqa: E402

# ---------------------------------------------------------------- SM data
# First-generation chiral fermions: (flavour, chirality) with SM
# (I3, Y, Q), colour triality tau (quarks 1, leptons 0), weak parity w
# (SU(2) doublet 1, singlet 0). Q = I3 + Y/2 throughout (SM input).
SM = {
    ("u", "L"): dict(I3=Fr(1, 2), Y=Fr(1, 3), tau=1, w=1),
    ("d", "L"): dict(I3=Fr(-1, 2), Y=Fr(1, 3), tau=1, w=1),
    ("nu", "L"): dict(I3=Fr(1, 2), Y=Fr(-1), tau=0, w=1),
    ("e", "L"): dict(I3=Fr(-1, 2), Y=Fr(-1), tau=0, w=1),
    ("u", "R"): dict(I3=Fr(0), Y=Fr(4, 3), tau=1, w=0),
    ("d", "R"): dict(I3=Fr(0), Y=Fr(-2, 3), tau=1, w=0),
    ("nu", "R"): dict(I3=Fr(0), Y=Fr(0), tau=0, w=0),
    ("e", "R"): dict(I3=Fr(0), Y=Fr(-2), tau=0, w=0),
}
FLAVOURS = ["u", "d", "nu", "e"]


def q_of(state: dict) -> Fr:
    return state["I3"] + state["Y"] / 2


def z6_ok(state: dict) -> bool:
    """Baez-Huerta Z6 compatibility: tau/3 + w/2 + Y/2 must be integral."""
    val = Fr(state["tau"], 3) + Fr(state["w"], 2) + state["Y"] / 2
    return val.denominator == 1


# ------------------------------------------------- twist assignment space
# One twist multiset (3 strands, entries in {-1,0,1}) per FLAVOUR; both
# chiralities of a flavour share it (same Q => same required total).
MULTISETS = sorted(
    {tuple(sorted(c)) for c in itertools.product((-1, 0, 1), repeat=3)}
)


def battery(assign: dict[str, tuple[int, int, int]]) -> dict:
    """Run all batteries for one assignment; return per-check results."""
    spectrum_ok = True
    per_state = {}
    for (fl, ch), st in SM.items():
        T = sum(assign[fl])
        q_twist = Fr(T, 3)
        y_t = 2 * (q_twist - st["I3"])
        ok = y_t == st["Y"]
        spectrum_ok &= ok
        per_state[f"{fl}_{ch}"] = dict(
            total_twist=T,
            Y_candidate=str(y_t),
            Y_SM=str(st["Y"]),
            match=ok,
        )
    # Nucleon doublet GMN: p = uud, n = udd; derived Q(p)=+1, Q(n)=0,
    # writhe-derived I3(p)=+1/2, I3(n)=-1/2 (appendix inputs).
    Tp = 2 * sum(assign["u"]) + sum(assign["d"])
    Tn = sum(assign["u"]) + 2 * sum(assign["d"])
    p_ok = Fr(Tp, 3) == Fr(1) and 2 * (Fr(Tp, 3) - Fr(1, 2)) == Fr(1)
    n_ok = Fr(Tn, 3) == Fr(0) and 2 * (Fr(Tn, 3) + Fr(1, 2)) == Fr(1)
    return dict(
        spectrum_ok=spectrum_ok,
        nucleon_ok=p_ok and n_ok,
        per_state=per_state,
        nucleon=dict(T_p=Tp, T_n=Tn, p_ok=p_ok, n_ok=n_ok),
    )


def main() -> None:
    # Sanity: SM table itself satisfies GMN + Z6 (input validation).
    assert all(q_of(s) == s["I3"] + s["Y"] / 2 for s in SM.values())
    z6_table = {f"{fl}_{ch}": z6_ok(s) for (fl, ch), s in SM.items()}
    assert all(z6_table.values()), "SM Z6 sanity failed"

    survivors = []
    n_total = 0
    for combo in itertools.product(MULTISETS, repeat=len(FLAVOURS)):
        n_total += 1
        assign = dict(zip(FLAVOURS, combo))
        res = battery(assign)
        if res["spectrum_ok"] and res["nucleon_ok"]:
            survivors.append(dict(assignment=assign, **res))

    # Per-flavour ambiguity: which multisets appear among survivors.
    per_flavour = {
        fl: sorted({tuple(s["assignment"][fl]) for s in survivors})
        for fl in FLAVOURS
    }

    wb = WitnessBuilder("strand-twist-y-battery", engine="python-fractions")
    wb.set_description(
        "EXPLORATORY strand-twist hypercharge battery (def:strand-twist-"
        "datum steps b/c, beans qou-4tul/qou-q377): helon-style candidate-"
        "space enumeration for Y = 2(T/3 - I3) against the SM first-"
        "generation spectrum, Baez-Huerta Z6 compatibility, and nucleon-"
        "doublet GMN. Candidate-space feasibility only — NOT wired, NOT a "
        "derivation; conj:sm-hypercharge-invariant stays open.")
    wb.add_data("search_space", {
        "multisets_per_flavour": len(MULTISETS),
        "assignments_enumerated": n_total,
        "twist_range": [-1, 0, 1],
        "strands_per_fermion": 3,
        "normalisation": ("Q_twist = totalTwist/3 (colour-tube charge "
                          "quantum; fixed structurally, not tuned)"),
    })
    wb.add_data("z6", {
        "condition": "tau/3 + w/2 + Y/2 integral (Baez-Huerta)",
        "sm_table_ok": z6_table,
    })
    wb.add_data("survivors", {
        "count": len(survivors),
        "per_flavour_multisets": {
            k: [list(m) for m in v] for k, v in per_flavour.items()
        },
        "full": [
            {
                "assignment": {k: list(v) for k, v in s["assignment"].items()},
                "nucleon": s["nucleon"],
            }
            for s in survivors
        ],
    })
    wb.add_data("bar_negation_note", (
        "Antiparticle consistency Y(fbar) = -Y(f) holds identically for "
        "Y = 2(T/3 - I3) under (T, I3) -> (-T, -I3); a structural property "
        "of the candidate form, not scored as a battery outcome."))
    wb.add_data("honest_gap", (
        "Candidate-space feasibility only. The framework carries no "
        "per-chiral-fermion framed braid words; deriving the twist "
        "multisets from framework states (rather than enumerating them) "
        "is the open content of conj:sm-hypercharge-invariant. "
        "Q_twist == crossing-derived Q was checked only on the nucleon "
        "doublet composites, where the appendix records derived Q and I3."))
    wb.add_assertion(
        name="survivors_count",
        computed=len(survivors), expected=4, tolerance=0, unit="count",
        source=("Exact enumeration of all 10^4 helon-style assignments; "
                "4 survive the spectrum + nucleon-GMN battery."))
    wb.add_assertion(
        name="u_multiset_unique",
        computed=len(per_flavour["u"]), expected=1, tolerance=0, unit="count",
        source="The u-quark twist multiset {0,1,1} is uniquely determined.")
    wb.add_assertion(
        name="e_multiset_unique",
        computed=len(per_flavour["e"]), expected=1, tolerance=0, unit="count",
        source="The electron twist multiset {-1,-1,-1} is uniquely determined.")
    out = wb.save()

    print(f"assignments enumerated: {n_total}")
    print(f"survivors (spectrum + nucleon GMN): {len(survivors)}")
    for fl in FLAVOURS:
        print(f"  {fl}: surviving multisets {per_flavour[fl]}")
    print(f"Z6 SM sanity: all pass = {all(z6_table.values())}")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
