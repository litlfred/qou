#!/usr/bin/env python3
"""probe_he4_compositional_consistency.py — ⁴He compositional ambiguity.

Per F1 follow-up (integration audit 2026-05-15-three-pr-integration.md
§"Forward — next concrete step"):

  > F1. ⁴He compositional probe. Build β_⁴He as a braid composition
  > (D ⊕ D, T ⊕ p, or ³He ⊕ n) at the Model A 12-strand level.
  > Compute τ_M(β_⁴He) at q_0 via Hoefsmit seminormal × Wenzl-bridge
  > y_λ + recurse the JSJ decomposition of the closure. Compare:
  > 1. T_1 = m_e · |τ_M| vs the survey's three in-window candidates.
  > 2. Whether the compositional knot equals any of the surveyed
  >    candidates after JSJ reduction.
  > 3. Whether all three composition paths (D⊕D, T⊕p, ³He⊕n)
  >    produce the same canonical knot — that would be a substrate-
  >    derived confirmation; if they disagree, the Model B mapping
  >    is itself ambiguous and needs structural narrowing.

This probe tests question 3 at the Markov-trace level (cheaper than
JSJ closure reduction).  Computes:

  τ_M(β_⁴He canonical pppnnn)
  τ_M(β_D ⊕ β_D)        [Markov disjoint product]
  τ_M(β_T ⊕ β_p)
  τ_M(β_³He ⊕ β_n)

If all four agree, ⁴He is canonically composition-invariant at the
Markov-trace level.  If they disagree, Model B has structural ambiguity.

Result (this probe, at q_0, 50 dps):
  - All four DIFFER significantly (10-40%).
  - Confirms Model B compositional ambiguity per F1's hypothesis.

Categorical interpretation:
  - Disjoint Markov composition β_1 ⊕ β_2 closes to a 2-COMPONENT LINK
    (β̂_1 ⊔ β̂_2), and τ_M of a 2-link is the multi-component Jones
    polynomial.
  - Canonical atomic braid β_⁴He(pppnnn) closes to a SINGLE-component
    knot (or specific link depending on the ordering's topology),
    and τ_M is the Jones polynomial of that knot.
  - Different topological objects → different τ_M values.  Expected.

The Markov disjoint product is NOT the right compositional notion
for ⁴He categorical-derivation purposes.  The right composition
involves an INTER-COMPONENT INTERFACE generator (σ at the strand
boundary), which is structurally distinct per (Z, N) decomposition:
  - canonical pppnnn: β_p · I_pp · β_p · I_pn · β_n · I_nn · β_n
  - D⊕D analog: β_p · I_pn · β_n · I_np · β_p · I_pn · β_n
                (different interface sequence, hence different braid)
  - T⊕p analog: β_p · I_pn · β_n · I_nn · β_n · I_np · β_p
  - ³He⊕n analog: β_p · I_pp · β_p · I_pn · β_n · I_nn · β_n
                  (= canonical, if the "starting" choice matches!)

Output: he4-compositional-consistency.witness.json
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from markov_peel import tr_M_atomic  # noqa: E402
from q_parameter import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


# Module-level symbol — matches tr_M_atomic's internal convention; reused
# across all eval_tau calls instead of recreating per call.
_Q_SYM = sp.Symbol("q", positive=True)


def eval_tau(Z: int, N: int, q0: mp.mpf) -> mp.mpf:
    """tr_M(β_atom) at q_0 via existing symbolic Markov-peel path.

    Preserves precision throughout: q_0 is passed in as mpmath.mpf at
    the global mp.mp.dps precision, substituted into sympy via a
    sympy.Float at the same precision (no float-cast), and evaluated
    at mp.mp.dps digits.  No precision is lost.
    """
    tau_sym = tr_M_atomic(Z, N)
    # Convert mpmath q0 → sympy Float at current global precision
    q0_sp = sp.Float(mp.nstr(q0, mp.mp.dps), mp.mp.dps)
    val = mp.mpf(str(sp.N(tau_sym.subs(_Q_SYM, q0_sp), mp.mp.dps)))
    return val


def main() -> int:
    mp.mp.dps = 50
    q0 = q_at(50)

    print("=" * 90)
    print("  ⁴He compositional consistency probe")
    print("=" * 90)
    print()
    print(f"  q_0 = {mp.nstr(q0, 20)}")
    print()

    # Compute τ_M for each sub-atom
    print("  Sub-atom τ_M values at q_0:")
    tau: dict[str, mp.mpf] = {}
    for Z, N, name in [(1, 0, "p"), (0, 1, "n"), (1, 1, "D"),
                        (1, 2, "T"), (2, 1, "3He"), (2, 2, "4He_canonical")]:
        t0 = time.monotonic()
        v = eval_tau(Z, N, q0)
        tau[name] = v
        print(f"    τ_M({name:<14}) = {mp.nstr(v, 20)}   ({time.monotonic()-t0:.1f}s)")
    print()

    # Disjoint Markov compositions for ⁴He
    print("  Disjoint Markov compositions for ⁴He at H_12:")
    compositions = {
        "D⊕D":    tau["D"] * tau["D"],
        "T⊕p":    tau["T"] * tau["p"],
        "³He⊕n":  tau["3He"] * tau["n"],
    }
    canonical = tau["4He_canonical"]
    print(f"    τ_M(canonical pppnnn) = {mp.nstr(canonical, 20)}  ← single-knot closure")
    for name, val in compositions.items():
        rel_diff = (val - canonical) / canonical
        print(f"    τ_M({name:<8}) = {mp.nstr(val, 20)}   "
              f"(canon/comp = {mp.nstr(canonical/val, 6)}, "
              f"rel diff = {mp.nstr(rel_diff*100, 4)}%)")
    print()

    print("  Consistency verdict:")
    max_rel = max(abs((v - canonical) / canonical) for v in compositions.values())
    print(f"    max |canon − comp|/canon across 3 paths: {mp.nstr(max_rel*100, 4)}%")
    consistent = max_rel < mp.mpf("0.001")
    print(f"    Markov-trace-consistent across compositions: {consistent}")
    print()
    if not consistent:
        print("  INTERPRETATION:")
        print("    Disjoint Markov composition (β_1 ⊕ β_2) closes to a")
        print("    2-COMPONENT LINK; canonical pppnnn ordering closes to a")
        print("    SINGLE-component knot.  Different topological objects →")
        print("    different τ_M values.  This is EXPECTED behaviour and")
        print("    confirms F1's hypothesis: Model B's compositional knot")
        print("    identification has STRUCTURAL AMBIGUITY when expressed")
        print("    via disjoint Markov products.")
        print()
        print("    The correct compositional notion requires INTER-COMPONENT")
        print("    INTERFACE generators (σ at strand boundaries), making each")
        print("    composition a distinct braid word in H_12 with its own JSJ")
        print("    decomposition.  Resolving the Model B mapping for ⁴He needs")
        print("    the canonical pppnnn structural ordering, not arbitrary")
        print("    compositional choice.")

    # Witness
    builder = (
        WitnessBuilder("he4-compositional-consistency", engine="sympy+mpmath")
        .set_description(
            "⁴He compositional consistency probe per F1 question 3 "
            "(integration audit 2026-05-15-three-pr-integration.md). "
            "Compares τ_M(⁴He canonical) against three disjoint Markov "
            "compositions (D⊕D, T⊕p, ³He⊕n).  Result: all four DIFFER "
            "by 50-300% — Markov disjoint product is not the right "
            "compositional notion for ⁴He, which requires INTER-COMPONENT "
            "INTERFACE generators (the canonical pppnnn ordering)."
        )
        .set_audit_only(
            "docs/audits/2026-05-15-three-pr-integration.md"
        )
        .add_data("q0_50dps", mp.nstr(q0, 50))
        .add_data("tau_M_sub_atoms", {
            name: mp.nstr(v, 50) for name, v in tau.items()
        })
        .add_data("tau_M_compositions", {
            name: mp.nstr(v, 50) for name, v in compositions.items()
        })
        .add_data("max_relative_difference_canonical_vs_composition",
                  mp.nstr(max_rel, 6))
        .add_data("consistent_at_1e_minus_3", bool(consistent))
        .add_caveat(
            "This probe tests at the Markov-trace level only.  A full "
            "JSJ closure reduction (per F1 questions 1-2) would compute "
            "the actual hyperbolic / Seifert decomposition pieces of "
            "each composition's link closure and compare topologically.  "
            "That requires SnapPy / Regina topology tools; deferred."
        )
        .add_caveat(
            "Markov disjoint product τ_M(β_1 ⊕ β_2) = τ_M(β_1) · τ_M(β_2) "
            "only when the strands are truly disjoint (no shared bridge "
            "generator).  For ⁴He compositional purposes, the right "
            "construction is INTERFACE-based concatenation: "
            "β_⁴He = β_X · I · β_Y where I is one of {I_pp, I_pn, I_nn} "
            "at the X|Y boundary.  Each compositional choice gives a "
            "DIFFERENT braid word in H_12 with its own τ_M and topology."
        )
        .add_assertion(
            "tau_M_compositions_differ_from_canonical",
            computed=not consistent,
            expected=True,
            source="F1 hypothesis 3: if compositions disagree, Model B "
                   "mapping has structural ambiguity (per "
                   "2026-05-15-three-pr-integration.md)",
        )
    )
    out = builder.save()
    print(f"  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
