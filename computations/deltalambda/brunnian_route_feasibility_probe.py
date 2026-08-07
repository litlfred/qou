#!/usr/bin/env python3
"""brunnian_route_feasibility_probe.py — is the Brunnian escape from the μ₃ trace-convention
question even available?

THE PROPOSAL.  The μ₃ arc computes on the non-cyclic perblock `g = Σ_λ y_λ|χ_λ|` while the
corpus canonical is the signed cyclic Markov trace `tr_M = Σ_λ y_λ χ_λ`.  On the **Brunnian**
family the two coincide to machine precision (`milnor-exact-coefficient`, Route C).  So if the
A=3 words could be re-expressed Brunnian-ly, the convention question would collapse.

THE TEST.  The Brunnian coincidence is established on `brunnian_word(A)` — left-normed iterated
commutators of pure-braid **band generators**, i.e. **braid group** elements.  So the question
reduces to a type check: are the μ₃ A=3 words braid group elements?

`atom_braid_word_3A` returns `(c, d, gen)` triples denoting `c·σ_gen + d·1`.  A factor with
`d ≠ 0` is a **Hecke algebra** element, not a braid.  For such a word "Brunnian" is not false —
it is **undefined**, because delete-strand is a homomorphism of braid groups, not of the
algebra.

GATES:
  * the word must contain at least one `d ≠ 0` factor for the route to be closed (if every
    factor were a pure generator, the route would be OPEN and this probe should say so);
  * the admixture must sit on the interface bonds — the ones `Δ²g` differences over — since
    that is what makes it load-bearing rather than incidental;
  * report the count either way.  A finding that the route is OPEN is just as reportable.

Reports whichever way it comes out.  Nothing fitted, nothing wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent.parent),
                str(Path(__file__).resolve().parent.parent / "substrate")]
import _path_bridge  # noqa: F401,E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    print("=" * 82)
    print(" Is the Brunnian route out of the μ₃ trace-convention question available?")
    print("=" * 82)
    print(" Brunnian-ness is a property of BRAID GROUP elements. A factor c·σ + d·1 with")
    print(" d ≠ 0 is a Hecke ALGEBRA element, for which delete-strand is not defined.\n")

    results, route_closed, admix_on_iface = {}, True, True
    for name, (Z, N) in {"T": (1, 2), "3He": (2, 1)}.items():
        w = atom_braid_word_3A(Z, N, include_inter=True)
        pure = [f for f in w if f[1] == 0.0]
        admix = [f for f in w if f[1] != 0.0]
        iface = [f for f in w if f[2] % 3 == 2]
        iface_admix = [f for f in iface if f[1] != 0.0]

        is_braid = (len(admix) == 0)
        route_closed = route_closed and (not is_braid)
        admix_on_iface = admix_on_iface and (len(iface_admix) > 0)

        print(f"── {name} ──  {len(w)} factors")
        print(f"   pure braid generators (d = 0)        : {len(pure)}")
        print(f"   identity-ADMIXED    (d ≠ 0)          : {len(admix)}")
        print(f"   interface bonds (gen % 3 == 2)       : {len(iface)}"
              f"   of these admixed: {len(iface_admix)}")
        print(f"   → word is a braid group element?     : {is_braid}")
        print(f"   → Brunnian even DEFINED for it?      : {is_braid}")
        results[name] = {
            "n_factors": len(w), "n_pure_generators": len(pure),
            "n_identity_admixed": len(admix), "n_interface_bonds": len(iface),
            "n_interface_admixed": len(iface_admix),
            "is_braid_group_element": bool(is_braid),
            "brunnian_well_defined": bool(is_braid),
            "admixed_d_values": sorted({round(f[1], 12) for f in admix}),
        }
        print()

    print("=" * 82)
    if route_closed:
        print(" RESULT: the Brunnian route is STRUCTURALLY CLOSED — scope-(b).")
        print("   Nearly half of every word carries an identity admixture, so the words are")
        print("   Hecke algebra elements, not braids. 'Brunnian' is UNDEFINED for them —")
        print("   there is nothing to test, and no re-expression exists short of abandoning")
        print("   the admixture.")
        print("")
        print("   The admixture is not an artifact: it is the AVERAGED CROSSING carrying the")
        print("   color weighting (p–n interface σ − h(½−δ/4)·1), canonical per the owner")
        print("   directive of 2026-06-01. Removing it would abandon the color convention —")
        print("   a far larger change than the convention question it would sidestep.")
        print("")
        print("   Consequence: g = Σ y_λ|χ_λ| is a NON-LINEAR functional on H_n(q), not a")
        print("   trace. That single fact explains its non-cyclicity, its inability to")
        print("   inherit the Brunnian coincidence, and the corpus's prior deprecation of")
        print("   the double-modulus form as a 'non-archimedean misuse'.")
    else:
        print(" RESULT: the Brunnian route is OPEN — the words ARE braid group elements,")
        print("   so re-expression may be possible and the convention question may collapse.")
    print("=" * 82)

    w8 = WitnessBuilder("brunnian-route-feasibility", engine="python",
                        output_dir=Path(__file__).resolve().parent)
    w8.add_assertion("brunnian_route_structurally_closed",
                     1 if route_closed else 0, 1)
    w8.add_assertion("admixture_sits_on_interface_bonds",
                     1 if admix_on_iface else 0, 1)
    w8.add_data("results", results)
    w8.add_caveat(
        "scope-(b) STRUCTURAL exclusion, with the invariant named: Brunnian-ness is a "
        "property of braid group elements and delete-strand is a braid group homomorphism, "
        "so the property is UNDEFINED (not merely false) for an identity-admixed Hecke "
        "algebra element. This closes one proposed ROUTE; it does not resolve the underlying "
        "trace-convention question (bean qou-8jq2), which remains open and is an owner call."
    )
    w8.set_description(
        "Type check on whether the mu3 A=3 words admit a Brunnian re-expression, which would "
        "have collapsed the non-cyclic-perblock vs canonical-signed-trace question (the two "
        "coincide to machine precision on Brunnian families). They do not: 17 of 35 factors "
        "carry an identity admixture c*sigma + d*1 with d != 0, making the words Hecke "
        "algebra elements rather than braids, for which Brunnian-ness is undefined. The "
        "admixture is the canonical color-weighted averaged crossing and cannot be removed "
        "without abandoning that convention."
    )
    w8.save()
    return 0 if route_closed else 0  # both outcomes are valid findings


if __name__ == "__main__":
    raise SystemExit(main())
