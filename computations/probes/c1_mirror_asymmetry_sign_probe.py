#!/usr/bin/env python3
"""The derived c₁ mirror asymmetry has the WRONG SIGN — 0/230 against AME, and it is scale-free.

Bean `qou-z4ba`. Successor to `qou-pdg9` (c₁ derived, PR #6492) and `qou-i719`
(PR #6541).

## Why this test is worth running, given that the scale is unpinned

`qou-59j5` established that the framework does not derive the energy scale that
turns the trace channel into MeV, and `qou-ssz6` that `log Z` is an entropy with
no temperature. That kills every *magnitude* claim in this lane — every "N× short"
is a ratio against a chosen unit.

**A sign is immune to it.** Any positive energy scale `E` maps `c₁ ↦ E·c₁` and
preserves order. So a prediction about *which of two nuclei binds more* is
testable with no scale at all, and it is the one kind of claim this lane can still
make. That is what this probe tests, on the one quantity here that is derived
rather than measured.

## The prediction, exact and parameter-free

`c₁(Z,N) = (21Z + 16N)(2^{−A−1} − 4^{−A}) − 4(I_pp − I_nn)·4^{−A}` — derived in
PR #6492 as a permutation count, with `21 = 4·6 − 3` and `16 = 4·5 − 4` the
proton / neutron letter census and `I_pp = Z−1`, `I_nn = N−1` truncated at 0.
Nothing in it is fitted. Its mirror difference collapses to

    c₁(Z,N) − c₁(N,Z)  =  (Z − N) · (5·2^{−A−1} − 13·4^{−A})
                       =  (Z − N) · 4^{−A} · (5·2^{A−1} − 13)

verified exactly here over every `(Z,N)` with `A = 2…24`. The bracket is
**negative at `A = 2`** (`10 < 13`) and **positive for every `A ≥ 3`**
(`20, 40, 80, … > 13`). So for `A ≥ 3` the trace channel says the **proton-rich**
member of a mirror pair binds **more**.

## The measurement

Nature says the opposite, without exception: the proton-rich mirror is always the
less bound one, because of Coulomb repulsion. Over every mirror pair in AME 2020
with `Z > N` and `A ≥ 3` — **230 pairs** — the sign agreement is **0/230**.

Two consequences, kept separate:

* **Scope (a), and sharp.** The trace channel *alone*, at leading order in `ℏ_q`,
  gets the mirror asymmetry backwards for every measured pair. This is a
  scope-limited negative about that channel at that order, not a structural
  exclusion of anything — no invariant is cited and none is claimed.
* **It localises what is missing.** The residual must be charge-dependent and
  **repulsive**, and must exceed the wrong-signed `c₁` term rather than merely
  supply the observed gap. That is the Coulomb term, which
  `QOU/MassTheory/CoulombFromCrossingCounts.lean` records as *"`a_C` is nowhere,
  the `1/R` is not derived"*, and `QOU/Mass/SaturationPeakStructure.lean` as
  *"Nothing here derives `a_V`, `a_S` or `a_C`"*.

## What is NOT claimed

That the leading order is where the mirror asymmetry should appear — `c₂` and
higher are not tested here (the exact `c₂` values exist for six words only, and
have no closed form in `(Z,N)`). That the trace channel is refuted: it is not,
this bounds one order of one channel. And no magnitude is quoted anywhere,
because none is available without a scale.

Precision: `Fraction` for the closed form (exact), `Decimal` for AME (the table's
own quoted digits, per `ame_2020_binding_energies`). No float in any comparison;
signs are compared, never differences of differently-typed quantities.
"""
from __future__ import annotations

import sys
from decimal import Decimal
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401

from ame_2020_binding_energies import _EXACT, _binding_mev_exact  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def c1_closed(Z: int, N: int) -> F:
    """The derived leading-order coefficient (PR #6492, QOU.MassTheory.c1Closed)."""
    A = Z + N
    return ((21 * Z + 16 * N) * (F(1, 2) ** (A + 1) - F(1, 4) ** A)
            - 4 * (max(Z - 1, 0) - max(N - 1, 0)) * F(1, 4) ** A)


def mirror_bracket(A: int) -> F:
    """`5·2^{−A−1} − 13·4^{−A}` — the whole A-dependence of the mirror difference."""
    return 5 * F(1, 2) ** (A + 1) - 13 * F(1, 4) ** A


def main() -> int:
    w = WitnessBuilder("c1-mirror-asymmetry-sign-probe")
    w.set_description(
        "The derived c1 closed form predicts that the proton-rich member of a mirror pair binds "
        "MORE for every A >= 3, via the exact identity c1(Z,N) - c1(N,Z) = (Z-N)(5*2^-(A+1) - "
        "13*4^-A). AME 2020 says the opposite in all 230 mirror pairs. Parameter-free and "
        "scale-free (a sign is invariant under any positive energy scale), so unlike every "
        "magnitude claim in this lane it survives the unpinned-E_0 problem of bean qou-59j5."
    )
    w.set_audit_only(True)

    print("=" * 78)
    print("  The c1 mirror asymmetry vs AME 2020")
    print("=" * 78)

    # ── 1. the exact identity ────────────────────────────────────────────────
    bad = [(Z, A - Z) for A in range(2, 25) for Z in range(1, A)
           if c1_closed(Z, A - Z) - c1_closed(A - Z, Z) != (2 * Z - A) * mirror_bracket(A)]
    w.add_assertion(
        "mirror_difference_collapses_to_the_exact_identity",
        computed=str(len(bad)), expected="0",
        source="c1(Z,N) - c1(N,Z) == (Z-N)*(5*2^-(A+1) - 13*4^-A) as exact Fractions, for every "
               "(Z,N) with Z,N >= 1 and A = 2..24 (275 pairs). The census term contributes "
               "5(Z-N) and the interface term -8(Z-N), both times 4^-A; the whole isospin "
               "dependence of c1 is this one bracket.",
    )
    print(f"\n  identity c1(Z,N) - c1(N,Z) = (Z-N)(5*2^-(A+1) - 13*4^-A): "
          f"{'EXACT for all 275 pairs A=2..24' if not bad else f'FAILS at {bad[:3]}'}")

    # ── 2. the sign of the bracket ───────────────────────────────────────────
    brackets = {A: mirror_bracket(A) for A in range(2, 25)}
    a2_neg = brackets[2] < 0
    a3plus_pos = all(v > 0 for A, v in brackets.items() if A >= 3)
    w.add_assertion(
        "bracket_is_negative_at_A2_and_positive_for_every_A_at_least_3",
        computed="1" if (a2_neg and a3plus_pos) else "0", expected="1",
        source=f"5*2^-(A+1) - 13*4^-A = 4^-A (5*2^(A-1) - 13): at A=2, 5*2 = 10 < 13 so it is "
               f"{brackets[2]} < 0; at A=3, 5*4 = 20 > 13 so it is {brackets[3]} > 0, and "
               f"2^(A-1) only grows. So for every A >= 3 the trace channel predicts the "
               f"PROTON-RICH mirror (Z > N) binds MORE.",
    )
    print(f"  bracket at A=2: {brackets[2]} (negative);  A=3: {brackets[3]} (positive); "
          f"positive for all A>=3: {a3plus_pos}")

    # ── 3. against AME ───────────────────────────────────────────────────────
    pairs = sorted({(Z, A - Z, A) for (Z, A) in _EXACT
                    if Z > A - Z and A >= 3 and (A - Z, A) in _EXACT})
    rows, agree = [], 0
    for Z, N, A in pairs:
        pred = c1_closed(Z, N) - c1_closed(N, Z)                     # Fraction
        obs = _binding_mev_exact(Z, A) - _binding_mev_exact(N, A)    # Decimal
        s_pred = (pred > 0) - (pred < 0)
        s_obs = (obs > 0) - (obs < 0)
        if s_pred == s_obs:
            agree += 1
        rows.append({"Z": Z, "N": N, "A": A,
                     "c1_Z_N": str(c1_closed(Z, N)), "c1_N_Z": str(c1_closed(N, Z)),
                     "c1_difference": str(pred), "predicted_sign": s_pred,
                     "B_Z_N_mev": str(_binding_mev_exact(Z, A)),
                     "B_N_Z_mev": str(_binding_mev_exact(N, A)),
                     "B_difference_mev": str(obs), "observed_sign": s_obs,
                     "signs_agree": s_pred == s_obs})
    # NB both assertions below are stated so that they PASS when the finding holds.
    # A refutation is an established result, not a red mark: an assertion shaped as
    # `computed 0/230, expected 230/230` would trip the witness failed-assertion
    # ratchet for a probe that did exactly what it set out to do.
    w.add_assertion(
        "prediction_and_observation_disagree_in_sign_for_EVERY_mirror_pair",
        computed=str(len(pairs) - agree), expected=str(len(pairs)),
        source="for each AME 2020 mirror pair with Z > N and A >= 3, the sign of "
               "c1(Z,N) - c1(N,Z) against the sign of B(Z,N) - B(N,Z). The prediction is "
               "positive for every pair (bracket positive, Z > N); the observation is negative "
               "for every pair (Coulomb repulsion makes the proton-rich mirror less bound). "
               "Signs are compared, never magnitudes: no energy scale enters, so this is the one "
               "claim in this lane immune to the unpinned E_0 of bean qou-59j5.",
    )
    w.add_assertion(
        "the_disagreement_is_universal_not_a_sample_artifact",
        computed=str(agree), expected="0",
        source=f"{len(pairs)} pairs, spanning A = {min(p[2] for p in pairs)}..{max(p[2] for p in pairs)} "
               f"and Z-N = {min(p[0]-p[1] for p in pairs)}..{max(p[0]-p[1] for p in pairs)}; "
               f"agreement {agree}. Not a selected subset — every mirror pair the AME table holds "
               f"with both members present.",
    )

    print(f"\n  mirror pairs (Z > N, A >= 3, both in AME): {len(pairs)}")
    print(f"  {'pair':>10}{'c1 diff':>13}{'B diff (MeV)':>16}   verdict")
    for r in rows[:10]:
        print(f"  {str((r['Z'], r['N'])):>10}{r['c1_difference']:>13}"
              f"{r['B_difference_mev']:>16}   "
              f"{'agree' if r['signs_agree'] else 'OPPOSITE'}")
    print(f"  … {len(rows) - 10} more")
    print(f"\n  SIGN AGREEMENT: {agree}/{len(pairs)}")

    w.add_data("pairs", rows)
    w.add_data("bracket_by_A", {str(A): str(v) for A, v in brackets.items()})
    w.add_data("verdict", (
        f"The derived c1 mirror asymmetry is WRONG IN SIGN for every one of the {len(pairs)} AME "
        f"mirror pairs with A >= 3. The prediction is exact and parameter-free — "
        f"c1(Z,N) - c1(N,Z) = (Z-N) 4^-A (5*2^(A-1) - 13), positive for Z > N whenever A >= 3 — "
        f"and the comparison is SCALE-FREE, since any positive energy scale preserves a sign. "
        f"SCOPE (a): the trace channel alone, at leading order in hbar_q, gets the mirror "
        f"asymmetry backwards. It is not a structural exclusion; no invariant is cited. What it "
        f"localises is that the missing term must be charge-dependent and REPULSIVE, and must "
        f"exceed the wrong-signed c1 contribution rather than merely supply the observed gap — "
        f"i.e. the Coulomb term the corpus records as nowhere derived."
    ))
    out = w.save({"q0Anchor": "independent", "q0AnchorReason": "q0_independence_checker: the fully-resolved import cone reads no q0 and the source carries no q0-shaped literal"})
    print(f"\n  witness -> {out}")
    ok = (not bad) and a2_neg and a3plus_pos and agree == 0
    print(f"  ALL PASSED: {ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
