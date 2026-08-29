#!/usr/bin/env python3
"""The state space DOES contain a 3-dimensional object. The Sym^2 gate is
exactly what rejects it.  (bean qou-8p1i / qou-8p1x)

The question
------------
"Is the state space not just made up of fibres?"  Yes -- and that is the point.
`feynman-eigenbasis.md` builds the physical state space as

    V_phys = direct limit of V^{tensor n},

decomposed into irreducible summands labelled by knot types.  So every object
in the framework's state space -- including every object of the gauge action
groupoid (`def:gauge-action-groupoid`), whose objects are the topological
states -- is built from tensor powers of the ONE fibre `V`, with `dim V = 2` by
the Descartes condition.

So the natural follow-up is: the tensor powers of a 2-dimensional `V` contain
summands of many dimensions.  **Does one of them have dimension 3?**  If so, is
the "missing 3-dimensional fibre" already sitting in the state space?

The answer, and why it does not close the gap
----------------------------------------------
**Yes, there is a 3.**  For `dim V = 2`,

    V tensor V  =  Sym^2(V)  +  Lambda^2(V)  =  3  +  1,

so `Sym^2(V)` is a 3-dimensional object living natively in `V^{tensor 2}` -- it
is the `SU(2)` adjoint, spin 1.  Nothing has to be constructed or imported.

**And it fails the Sym^2 gate.**  T3a's gate (`schur-weyl-eightfold.md`) demands
that a candidate `W` be non-self-dual, tested as: `Sym^2(W)` must contain no
singlet.  The relevant general fact is that

    W tensor W  contains a singlet  <==>  W is self-dual,

and the Frobenius-Schur indicator says which half it lands in: `+1` puts the
singlet in `Sym^2`, `-1` puts it in `Lambda^2`.  So:

  * `V` itself (spin 1/2, dim 2): FS = -1, symplectic.  The singlet sits in
    `Lambda^2(V)`, so `Sym^2(V)` is singlet-free -- `V` would pass the gate,
    but it is 2-dimensional, which is the whole problem.
  * `W = Sym^2(V)` (spin 1, dim 3): FS = +1, orthogonal.  The singlet sits in
    `Sym^2(W)`:  `Sym^2(3) = 5 + 1`.  **Fails.**
  * `SU(3)` fundamental `3`: not self-dual (`3bar` is a different
    representation), so `3 tensor 3` has no singlet at all and
    `Sym^2(3) = 6` is irreducible.  **Passes.**

Both candidates have `dim Sym^2 = 6`.  They are separated purely by whether
that 6 is irreducible or splits as `5 + 1` -- which is exactly self-duality.

So the gate is not an arbitrary filter.  It is precisely the condition that
rejects the 3 the state space hands you for free, because an `SU(2)` adjoint
carries an invariant symmetric form (the Killing form / `delta_ij`) and a
colour triplet must not.

Consequence for qou-8p1i
-------------------------
This closes the cheapest hope for the multi-fibre groupoid route: one cannot
take the 3-dimensional object already present in `V^{tensor 2}` and call it the
colour (or flavour) triplet.  Any `W` satisfying the gate must be **non-self-
dual**, and every summand of `V^{tensor n}` for `SU(2)`-fibre `V` is self-dual,
because every `SU(2)` representation is self-dual.

That last sentence is the real obstruction, and it is stronger than "we have not
found a construction":

    **No summand of any tensor power of a 2-dimensional fibre can pass the
    Sym^2 gate**, because all `SU(2)` representations are self-dual.

So T3b's "inequivalent fibre objects" cannot mean "different summands of
`V^{tensor n}`".  It must mean genuinely inequivalent fibres -- several
non-isomorphic `V`s, i.e. a Tannakian gerbe / multi-fibre-functor situation --
which is what `qou-dwsh` §2b was reaching for and what remains unconstructed.

What is verified here (exact integer arithmetic)
------------------------------------------------
  C1  For `SU(2)`: `V tensor V = 3 + 1`, so a 3-dimensional summand exists.
  C2  `Sym^2(spin 1) = spin 2 + spin 0` -- dimension `6 = 5 + 1`, singlet
      present, gate FAILED.
  C3  `Sym^2(spin 1/2) = spin 1` -- dimension 3, no singlet (the singlet is in
      `Lambda^2`), consistent with FS = -1.
  C4  Every `SU(2)` irrep is self-dual: the weight multiset of each irrep is
      symmetric under negation, so `chi` is real and `W = W*`.  Checked for
      spins 1/2 through 6.
  C5  The `SU(3)` contrast: `3 tensor 3 = 6 + 3bar` carries no singlet, since
      `3` is not self-dual -- its weight multiset is NOT negation-symmetric.
  C6  **The parity split** (added 2026-08-07 as a correction, see below):
      self-duality alone does NOT decide the gate.  For the `SU(2)` irrep of
      dimension `d = 2j+1` the Frobenius-Schur indicator is `(-1)^{2j}
      = (-1)^{d-1}`, so the invariant form is symmetric for odd `d` and
      antisymmetric for even `d`.  The singlet therefore sits in `Sym^2` only
      when `d` is odd.  Checked for `d = 2..9`.

CORRECTION (2026-08-07)
-----------------------
An earlier version of this module inferred from C4 that "EVERY summand of every
`V^{tensor n}` is self-dual, so none of them can pass the gate".  **That
inference is invalid.**  Self-duality splits by Frobenius-Schur:

  * `FS = +1` (orthogonal): the invariant form is symmetric, lives in `Sym^2`,
    so `Sym^2(W)` carries a singlet -- gate FAILS;
  * `FS = -1` (symplectic): the invariant form is antisymmetric, lives in
    `Lambda^2`, so `Sym^2(W)` has NO singlet -- gate PASSES.

C3 of this very module is a counterexample to the generalisation it was used to
support: the 2-dimensional fundamental is self-dual with `FS = -1`, its singlet
sits in `Lambda^2`, and it **passes** the `Sym^2` gate.

What survives is the odd-dimensional case, which is the one the colour question
actually needs: **no odd-dimensional `SU(2)` irrep passes the gate, in
particular none of dimension 3.**  The conclusion drawn downstream is therefore
unaffected -- a 3-dimensional triplet cannot be found among the summands of
`V^{tensor n}` -- but the stated generality was wrong and is corrected here.

Scope
-----
**scope-(b)** for the claim "some **odd-dimensional** summand of
`V^{tensor n}`, `dim V = 2`, passes the Sym^2 gate" -- excluded by the
Frobenius-Schur parity computation (C6), *not* by self-duality alone.

**NOT excluded:** even-dimensional summands, which are symplectic and do pass
the gate.  They are simply the wrong dimension for a colour triplet.

NOT claimed: that no 3-dimensional fibre exists anywhere in the framework; only
that it cannot be found inside the tensor powers of the existing 2-dimensional
one.  Nor anything about how to construct inequivalent fibres.

Exact integer arithmetic on weight multisets; no floating point.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
_OUT = HERE / "state-space-natural-three-sym2-gate.witness.json"


# ---------------------------------------------------------------------------
# SU(2): an irrep of spin j is indexed by its dimension d = 2j+1.  Use DOUBLED
# weights so everything is an integer: weights are d-1, d-3, ..., -(d-1).
# ---------------------------------------------------------------------------
def su2_weights(d: int) -> list[int]:
    return [d - 1 - 2 * k for k in range(d)]


def decompose_su2(weights) -> list[int]:
    """Peel highest-weight strings off a weight multiset -> list of dims."""
    c = Counter(weights)
    dims = []
    while any(v > 0 for v in c.values()):
        top = max(w for w, v in c.items() if v > 0)
        d = top + 1                      # doubled highest weight -> dim
        for w in su2_weights(d):
            c[w] -= 1
            if c[w] < 0:
                raise RuntimeError("not a valid SU(2) rep multiset")
        dims.append(d)
    return sorted(dims, reverse=True)


def tensor_weights(a, b):
    return [x + y for x in a for y in b]


def sym2_weights(w):
    """Weights of Sym^2 of a rep: unordered pairs WITH repetition (i <= j)."""
    return [w[i] + w[j] for i in range(len(w)) for j in range(i, len(w))]


def alt2_weights(w):
    """Weights of Lambda^2: strictly i < j."""
    return [w[i] + w[j] for i in range(len(w)) for j in range(i + 1, len(w))]


def main() -> int:
    print("=" * 74)
    print("Does the state space already contain a usable 3?  (qou-8p1i)")
    print("=" * 74)

    checks: dict[str, bool] = {}

    V = su2_weights(2)          # the fibre: spin 1/2, dim 2
    # -- C1 : V (x) V = 3 + 1 -------------------------------------------
    vv = decompose_su2(tensor_weights(V, V))
    checks["C1_VtensorV_is_3_plus_1"] = vv == [3, 1]
    print(f"\nC1  V (x) V decomposes as {vv}  (want [3, 1])")
    print("    => a 3-dimensional object EXISTS natively: Sym^2(V), the SU(2) adjoint")

    # -- C2 : Sym^2 of the 3 contains a singlet -> gate FAILS -------------
    W = su2_weights(3)          # spin 1, dim 3
    s2W = decompose_su2(sym2_weights(W))
    checks["C2_sym2_of_3_has_singlet"] = (s2W == [5, 1])
    print(f"\nC2  Sym^2(3) decomposes as {s2W}  (dim {sum(s2W)})")
    print(f"    singlet present : {1 in s2W}  =>  Sym^2 GATE FAILED")

    # -- C3 : Sym^2(V) has no singlet (FS = -1, singlet is in Lambda^2) ---
    s2V = decompose_su2(sym2_weights(V))
    a2V = decompose_su2(alt2_weights(V))
    checks["C3_sym2_of_V_no_singlet"] = (1 not in s2V)
    checks["C3_alt2_of_V_is_singlet"] = (a2V == [1])
    print(f"\nC3  Sym^2(V) = {s2V}, Lambda^2(V) = {a2V}")
    print("    the singlet sits in Lambda^2, i.e. Frobenius-Schur = -1 (symplectic)")

    # -- C4 : every SU(2) irrep is self-dual -----------------------------
    c4 = True
    for d in range(2, 14):
        w = su2_weights(d)
        c4 &= (Counter(w) == Counter(-x for x in w))
    checks["C4_all_su2_irreps_self_dual"] = c4
    print(f"\nC4  every SU(2) irrep has a negation-symmetric weight multiset")
    print(f"    (i.e. is self-dual), dims 2..13 : {c4}")
    print("    => every summand of every V^(tensor n) is self-dual")
    print("    NOTE: self-duality alone does NOT decide the gate -- see C6.")

    # -- C5 : the SU(3) contrast ------------------------------------------
    # Fundamental 3 of SU(3): weights in the standard basis, as integer
    # triples summing to 0 -- (2,-1,-1), (-1,2,-1), (-1,-1,2) up to scale.
    su3_fund = [(2, -1, -1), (-1, 2, -1), (-1, -1, 2)]
    neg = [tuple(-x for x in w) for w in su3_fund]
    not_self_dual = Counter(su3_fund) != Counter(neg)
    checks["C5_su3_fund_not_self_dual"] = not_self_dual
    # singlet in 3 (x) 3 would need a zero weight arising from w + w'
    tensor33 = Counter(tuple(a + b for a, b in zip(x, y))
                       for x in su3_fund for y in su3_fund)
    zero_wt = tensor33[(0, 0, 0)]
    checks["C5_no_zero_weight_in_3x3"] = (zero_wt == 0)
    print(f"\nC5  SU(3) fundamental is self-dual? {not not_self_dual}  (want False)")
    print(f"    zero-weight multiplicity in 3 (x) 3 : {zero_wt}  (want 0)")
    print("    => no singlet in 3 (x) 3; Sym^2(3) = 6 irreducible, GATE PASSED")

    # -- C6 : the parity split (CORRECTION, 2026-08-07) --------------------
    # Self-duality alone does not decide the gate.  For the SU(2) irrep of
    # dimension d = 2j+1 the singlet in W (x) W sits in Sym^2 iff 2j is even,
    # i.e. iff d is odd.  Verified by dimension bookkeeping, independent of
    # the Frobenius-Schur formula it confirms.
    print("\nC6  parity split -- does self-duality decide the gate?  NO")
    print("    %-4s %-6s %-10s %-12s %s" % ("d", "2j", "dimSym^2", "singlet in", "gate"))
    c6 = True
    parity_rows = []
    for d in range(2, 10):
        twoj = d - 1
        # W (x) W = sum_{k=0}^{2j} V_k ; Sym^2 collects k = 2j, 2j-2, ...
        sym_ks = list(range(twoj, -1, -2))
        dsym_from_ks = sum(2 * k + 1 for k in sym_ks)
        c6 &= (dsym_from_ks == d * (d + 1) // 2)          # bookkeeping check
        singlet_in_sym = (0 in sym_ks)
        c6 &= (singlet_in_sym == (d % 2 == 1))            # odd d <=> singlet in Sym^2
        gate = "FAILS" if singlet_in_sym else "PASSES"
        print("    %-4d %-6d %-10d %-12s %s" % (d, twoj, dsym_from_ks,
                                                "Sym^2" if singlet_in_sym else "Lambda^2",
                                                gate))
        parity_rows.append({"d": d, "singlet_in": "Sym^2" if singlet_in_sym else "Lambda^2",
                            "gate": gate})
    checks["C6_parity_decides_gate_not_self_duality"] = c6
    print("    => odd d (integer spin, FS=+1)  : singlet in Sym^2   -> FAILS")
    print("    => even d (half-int spin, FS=-1): singlet in Lambda^2 -> PASSES")
    print("    The 2-dim fundamental PASSES. Self-duality does NOT imply failure.")

    all_ok = all(checks.values())
    print("\n" + "=" * 74)
    print(f"ALL CHECKS PASS : {all_ok}")
    print("=" * 74)
    print("""
VERDICT (qou-8p1i)
------------------
The state space DOES already contain a 3-dimensional object -- Sym^2(V), the
SU(2) adjoint, sitting inside V (x) V. It is not the triplet we need, and the
Sym^2 gate is precisely the condition that rejects it: Sym^2(3) = 5 + 1 carries
a singlet because the SU(2) adjoint is self-dual (it has an invariant symmetric
form), whereas the SU(3) fundamental has Sym^2(3) = 6 irreducible because 3bar
is a different representation.

HOW FAR THE OBSTRUCTION GENERALISES -- CORRECTED 2026-08-07. An earlier version
of this verdict said: "every SU(2) rep is self-dual (C4), so EVERY summand of
EVERY tensor power is self-dual, so none of them can pass the gate". That
inference is INVALID, and C3 of this same module is the counterexample: the
2-dimensional fundamental is self-dual with FS = -1, its singlet sits in
Lambda^2, and it PASSES the gate.

Self-duality splits (C6). For the SU(2) irrep of dimension d the invariant form
is symmetric when d is odd (FS = +1, singlet in Sym^2, gate FAILS) and
antisymmetric when d is even (FS = -1, singlet in Lambda^2, gate PASSES).

What survives is the odd-dimensional case -- which is the one the colour
question needs: NO ODD-DIMENSIONAL SU(2) IRREP PASSES THE GATE, in particular
none of dimension 3. scope-(b) for that statement, on the parity computation,
not on self-duality alone. Even-dimensional summands are symplectic and do pass
the gate; they are simply the wrong dimension for a triplet.

CONSEQUENCE (unaffected by the correction): T3b's "inequivalent fibre objects"
cannot mean "different summands
of V^(tensor n)". It must mean genuinely non-isomorphic fibres -- a Tannakian
gerbe / multi-fibre-functor situation, which is what qou-dwsh section 2b was
reaching for and what remains unconstructed. The state space being "made of
fibres" is true but does not help: it is made of tensor powers of ONE fibre,
and the gate sees through that.
""")

    payload = {
        "schema": "witness/v1",
        "description": (
            "The state space already contains a 3-dimensional object, Sym^2(V), "
            "but it fails the Sym^2 gate because all SU(2) reps are self-dual; "
            "hence no summand of any V^(tensor n) can pass. Bean qou-8p1i."
        ),
        "computation": {
            "script": "computations/state_space_natural_three_sym2_gate.py",
            "arithmetic": "exact integer weight multisets; no floating point",
        },
        "data": {
            "V_tensor_V": vv,
            "sym2_of_adjoint": s2W,
            "sym2_of_V": s2V,
            "alt2_of_V": a2V,
            "su3_fundamental_self_dual": not not_self_dual,
            "zero_weight_multiplicity_in_3x3": zero_wt,
            "verdict": (
                "a 3-dimensional object exists natively (Sym^2(V), the SU(2) "
                "adjoint) but fails the Sym^2 gate: Sym^2(3) = 5+1 has a "
                "singlet because the adjoint is self-dual, whereas SU(3)'s "
                "Sym^2(3) = 6 is irreducible"
            ),
            "generalisation": (
                "CORRECTED 2026-08-07. Self-duality alone does NOT decide the "
                "gate: for the SU(2) irrep of dimension d the invariant form is "
                "symmetric when d is odd (singlet in Sym^2, gate fails) and "
                "antisymmetric when d is even (singlet in Lambda^2, gate "
                "passes). What holds is: no ODD-dimensional SU(2) irrep passes "
                "the gate, in particular none of dimension 3"
            ),
            "parity_split": parity_rows,
            "superseded_claim": (
                "an earlier version asserted 'every summand of every tensor "
                "power is self-dual, so none can pass the gate'. That is FALSE "
                "-- the 2-dimensional fundamental is self-dual with FS = -1 and "
                "PASSES the gate (C3 of this module is the counterexample to "
                "the generalisation it was used to support). The downstream "
                "conclusion is unaffected because it only needs dimension 3"
            ),
            "scope": (
                "scope-(b) for 'some ODD-DIMENSIONAL summand of V^(tensor n) "
                "with dim V = 2 passes the Sym^2 gate', excluded by the "
                "Frobenius-Schur parity computation (C6), NOT by self-duality "
                "alone. Even-dimensional summands are symplectic and do pass "
                "the gate; they are the wrong dimension for a triplet"
            ),
            "consequence_for_T3b": (
                "'inequivalent fibre objects' cannot mean different summands of "
                "V^(tensor n); it must mean genuinely non-isomorphic fibres, a "
                "Tannakian gerbe / multi-fibre-functor situation"
            ),
            "not_claimed": [
                "that no 3-dimensional fibre exists anywhere in the framework -- "
                "only that it is not inside the tensor powers of the existing "
                "2-dimensional one",
                "anything about how to construct inequivalent fibres",
            ],
            "all_checks_pass": all_ok,
            "checks": checks,
        },
    }
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    payload.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        payload, script_path=__file__, engine=None, q0_anchor=False)
    _OUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {_OUT.name}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
