#!/usr/bin/env python3
"""DERIVED: what fixes the linking number of a bonded pair — and why it is not uniform.

THE QUESTION. `bonded_pair_linking_inconsistency_probe.py` (bean qou-zbgu)
established that the corpus assigns two incompatible link values to the same
relation: the 4He mu-bar exclusion (qou-klgu, merged) needs every bonded pair
to have lk = 1, while binding_mn_milnor_linking.py models the TRITON -- whose
three pairs are all bonded -- as BORROMEAN with pairwise lk = [0,0,0]. It left
the question open: WHAT FIXES THE LINKING NUMBER OF A BONDED PAIR?

THE ANSWER, AND IT IS A DERIVATION, NOT A CHOICE. The canonical braid word
fixes it. `mass_at_3A_proper.atom_braid_word_3A(Z, N)` is the corpus's source
of truth for the atomic braid, and the owner's Option-A ruling (2026-08-29)
makes the canonical braid closure the nucleus's knot. Reading the
inter-nucleon interfaces straight out of it -- the crossings that
`include_inter=True` contributes and `include_inter=False` drops -- gives, per
nucleus, the table printed below.

WHAT IT SAYS, IN THREE PARTS.

(1) The interfaces are NOT a single crossing type. 4He's three interfaces are
    `sigma` (+1), `averaged_weighted` (no sign), and `sigma_inv` (-1). So
    "bonded => lk = 1" is not merely unestablished, as qou-zbgu concluded --
    it is FALSE, derived from the canonical object. That strengthens the
    retraction of qou-klgu from "premise not established" to "premise false".

(2) "bonded => lk = 0" is ALSO false. Two of 4He's three interfaces are
    genuine signed braid generators. So the triton BORROMEAN model's uniform
    lk = 0 does not describe the canonical braid either. NEITHER branch of the
    qou-zbgu dichotomy is what the corpus's own canonical word contains.

(3) The p-n interface HAS NO CLASSICAL LINKING NUMBER AT ALL. It is
    `averaged_weighted` = `sigma_g - h(1/2 - delta/4) . 1`, a Hecke-algebra
    element that is NOT in the braid group: `sigma` has d = 0 and
    `sigma_inv` has d = -h (since sigma^2 = h.sigma + 1), while this sits
    strictly between them. A linking number is an invariant of a LINK; this
    interface is a linear combination of an over- and an under-crossing, so
    promoting it to a classical link requires CHOOSING a representative.

    That choice is the unforced one qou-zbgu was looking for. It is not that
    the corpus picked the wrong value -- it is that the canonical object is
    not a link, and every mu-bar count in the tower silently classicalises it.

A FOURTH THING, FOUND ON THE WAY, AND IT IS LARGER. The canonical braid is a
CHAIN: it carries A-1 inter-nucleon interfaces (D 1, T 2, 4He 3, at generator
indices 2, 5, 8 -- exactly the boundaries between consecutive 3-strand nucleon
blocks). The max-contact contact-graph model used throughout the M_n(K)
programme asserts C(A,2) bonded pairs (D 1, T 3, 4He 6). These agree ONLY at
A = 2. So the clique-counting programme and the canonical braid word disagree
about WHICH PAIRS ARE BONDED, before any linking number is assigned.

SCOPE. scope-(a) on the interface reading: it reports what the canonical word
contains and what follows for the two uniform link models. The (3) claim --
that no classical lk is defined for the p-n interface -- is structural and
cites the algebra (the element is not in the braid group), but it excludes no
ingredient: a derivation that FIXES a classical representative would define one,
and nothing here says such a derivation cannot exist. No fit, no witness,
nothing wired.

Beans qou-k12x; answers qou-zbgu; bears on qou-klgu, qou-izah, qou-ooqh.
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import canonical_braid_crossings as C  # noqa: E402

# `h` is imported inside main() rather than at module level. NOTE, because a
# reviewer suggested taking it from "a lighter substrate shim" to avoid heavy
# deps: that would not help. `canonical_braid_crossings.atom_canonical_crossings`
# does `from hecke_core import h as h_val` INTERNALLY (line 159), and this probe
# cannot avoid calling it -- the canonical word IS its subject. So the
# dependency is unavoidable here; only the failure POINT moves.

ISO = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]


def main() -> int:
    from hecke_core import h as h_val  # see the note above the imports

    print("== the four interface elements, as Hecke elements sigma_g + d.1 ==")
    for t in ("sigma", "sigma_inv", "averaged", "averaged_weighted"):
        d = C.d_for_ctype(t, h_val)
        inbraid = t in ("sigma", "sigma_inv")
        print(f"  {t:18s} d = {float(d):+.12f}  sign = {C.sign_for_ctype(t):+d}"
              f"  {'braid generator' if inbraid else 'NOT in the braid group'}")
    print(f"  h = {float(h_val):.12f};  sigma has d=0, sigma_inv has d=-h.")
    assert C.d_for_ctype("sigma", h_val) == 0
    assert C.d_for_ctype("sigma_inv", h_val) == -h_val

    print()
    print("== inter-nucleon interfaces of the canonical braid word ==")
    print("   (what include_inter=True adds and include_inter=False drops)")
    for lab, Z, N in ISO:
        a = Counter(C.atom_canonical_crossings(Z, N, include_inter=True))
        b = Counter(C.atom_canonical_crossings(Z, N, include_inter=False))
        added = sorted((a - b).elements())
        A = Z + N
        desc = ", ".join(f"gen{g}:{t}({C.sign_for_ctype(t):+d})" for g, t in added)
        print(f"  {lab:4s} A={A}  interfaces={len(added)}  {desc}")
        assert len(added) == A - 1, f"{lab}: expected a chain of A-1 interfaces"

    print()
    print("== (1)+(2) both uniform link models are refuted by the word ==")
    a4 = Counter(C.atom_canonical_crossings(2, 2, include_inter=True))
    b4 = Counter(C.atom_canonical_crossings(2, 2, include_inter=False))
    types4 = sorted(t for _g, t in (a4 - b4).elements())
    print(f"  4He interface ctypes: {types4}")
    print("  -> not all positive crossings, so 'bonded => lk = 1' is FALSE")
    print("  -> not all unsigned,          so 'bonded => lk = 0' is FALSE")
    assert "sigma" in types4 and "sigma_inv" in types4, "need both signs present"
    assert "averaged_weighted" in types4, "need the unsigned p-n interface"

    print()
    print("== (4) the bond SET disagrees too, before any lk is assigned ==")
    print(f"  {'iso':5s} {'A':>2s} {'braid interfaces (A-1)':>22s} {'contact-graph C(A,2)':>21s}")
    for lab, Z, N in ISO:
        A = Z + N
        print(f"  {lab:5s} {A:2d} {A-1:22d} {A*(A-1)//2:21d}")
    print("  They agree only at A = 2. The clique-counting M_n programme and")
    print("  the canonical braid word disagree about WHICH PAIRS ARE BONDED.")

    print()
    print("== VERDICT ==")
    print("  The canonical braid word FIXES the bonded-pair linking data, and")
    print("  it fixes it NON-UNIFORMLY: +1, -1, and one interface with no")
    print("  classical linking number at all.")
    print()
    print("  The p-n interface is sigma_g - h(1/2 - delta/4).1, strictly")
    print("  between sigma (d=0) and sigma_inv (d=-h), hence not in the braid")
    print("  group. A linking number is an invariant of a LINK; this is a")
    print("  linear combination of an over- and an under-crossing. Promoting it")
    print("  to a classical link requires CHOOSING a representative -- and that")
    print("  choice, not a wrong value, is the unforced step qou-zbgu found.")
    print()
    print("  So qou-klgu's premise is FALSE (not merely unestablished), the")
    print("  triton's uniform lk=0 is also not the canonical word, and every")
    print("  mu-bar count in the M_n tower silently classicalises a Hecke")
    print("  element. scope-(a) on the reading; the not-in-the-braid-group")
    print("  claim is structural and excludes nothing -- a derivation that")
    print("  FIXES a representative would define an lk, and nothing here says")
    print("  one cannot exist. That is the next question, and it is sharper")
    print("  than the one this answers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
