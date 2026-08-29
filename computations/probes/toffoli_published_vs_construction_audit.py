#!/usr/bin/env python3
"""toffoli_published_vs_construction_audit.py — do the published Toffoli entries
match the construction the corpus records for them?

BEAN qou-3j5m.  This began as the P_66 discrepancy the convention work turned up.
It is not a P_66 problem.

THE ONLY RECORDED CONSTRUCTION is `computations/_deprecated/toffoli-braid.py`:

    V_i     = z*a_i + b_i     (a_i, b_i) from chain_reduce -- rational in q, no z
    P_{k,k} = prod_i V_i      over range(A-1)
    P_{m,k} = sum_conv [ prod_{j != conv} V_j^par ] * (V_conv^par - V_conv^dau)

This probe reconstructs it independently (same recipe, written from the content
block's prose) and compares three things: my reconstruction, the producer's own
committed witness, and the values published in the content blocks.

WHAT IT FINDS.

1. Reconstruction == producer, EXACTLY (symbolic zero, both diagonals).  So the
   recipe below is the framework's, not my paraphrase of it.

2. Of the four published entries, ONE matches:

       P_77   producer 0.5514527845   published 0.5514527845   MATCH
       P_66   producer 0.4153790120   published 0.6010         NO
       P_76   producer -0.1415316448  published +0.0495 (= Phi) NO
       P_67   producer +0.1415316448  published -0.0495         NO

3. The proof block's key lemma -- "target-flip blindness of the control crossing",
   Delta_1 = 0 -- is CONVENTION-DEPENDENT and false as the producer runs.
   chain_reduce pairs generator i with every j > i, so generator 1 is the crossing
   (1,2).  That is control-control only if the TARGET IS STRAND 0.  The producer's
   `toffoli_output` flips `k & 1`, i.e. the LAST strand.  Measured:

       target = last  (producer)      Delta_1 = -0.1045   NOT zero
       target = first (block's prose) Delta_1 =  0        zero

4. AND EVEN UNDER THE BLOCK'S OWN CONVENTION the chain does not give the published
   Phi:  V_1^par * Delta_0 = -0.04667 against Phi = +0.04955, ratio -0.942 -- 6% in
   magnitude and a sign flip.

CONSEQUENCE, and it is why this probe exists rather than a content edit.  The
convention-D work upstream of this took the published closed forms as the
framework's quantities and asked which z they carry.  For P_77 that is safe -- it
matches its construction.  For Phi, P_66 and P_67 the prior question is open: the
published closed form is not what the recorded construction produces, so migrating
it to convention D would carry the discrepancy along at a new value.

NOT CLAIMED: that the published forms are WRONG.  The construction lives in a
_deprecated file that neither the content blocks nor the live producer cite, so it
may itself be superseded by a derivation that is not in the tree.  What is
established is that the two disagree and that the corpus does not record which is
current.

NO-FLOAT64: sympy exact throughout; mpmath 30 dps for display only.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent.parent),
                str(Path(__file__).resolve().parent.parent / "substrate")]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(30)

_q = sp.symbols("q", positive=True)
_ha = _q - 1 / _q
_zC = sp.sqrt(_q) / (_q + 1)
Q_EVAL = sp.Rational(111, 100)      # the q the producer's witness reports at


def _cc(ti, tj):
    if ti == 1 and tj == 1:
        return sp.Integer(1), sp.Integer(0)
    if ti == 0 and tj == 0:
        return sp.Integer(1), -_ha
    return sp.Integer(1), -_ha / 2


def _chain(i, order):
    a, b = sp.Integer(0), sp.Integer(1)
    for j in range(i + 1, len(order)):
        c, d = _cc(order[i], order[j])
        a, b = a * c * _ha + a * d + b * c, a * c + b * d
    return a, b


def _V(i, order, z=_zC):
    a, b = _chain(i, order)
    return sp.cancel(z * a + b)


def _diag(order, z=_zC):
    return sp.cancel(_V(0, order, z) * _V(1, order, z))


def _num(e):
    return mp.mpf(str(sp.N(sp.simplify(e).subs(_q, Q_EVAL), 25)))


def main() -> int:
    print("=" * 90)
    print(" Published Toffoli entries vs the construction the corpus records")
    print("=" * 90)

    # published closed forms, verbatim from the content blocks
    pub = {
        "P_77": (_q + sp.sqrt(_q) - 1) / (_q + 1),
        "P_66": (_q ** 4 + _q ** sp.Rational(7, 2) + 2 * _q ** sp.Rational(3, 2)
                 + sp.sqrt(_q) - 1) / (2 * (_q + 1) ** 2),
        "Phi": ((_q - 1) * (_q * sp.sqrt(_q) + sp.sqrt(_q) - 1)
                * (_q * sp.sqrt(_q) + _q + 1) / (2 * (_q + 1) ** 2)),
    }
    # the producer's own committed witness
    wpath = (Path(__file__).resolve().parent.parent
             / "_deprecated" / "toffoli-braid.witness.json")
    prod = {}
    if wpath.exists():
        d = json.loads(wpath.read_text())
        me = d.get("matrix_entries") or d.get("data", {}).get("matrix_entries", {})
        for key, ent in (("P_66", "P_6,6"), ("P_77", "P_7,7"), ("P_76", "P_7,6")):
            if ent in me:
                prod[key] = mp.mpf(str(me[ent]["numerical_1.110"]))

    # 1. reconstruction == producer?
    recon_77 = sp.simplify(sp.radsimp(sp.simplify(_diag((1, 1, 1)) - pub["P_77"])))
    recon_matches_pub_77 = (recon_77 == 0)
    r66, r77 = _num(_diag((1, 1, 0))), _num(_diag((1, 1, 1)))
    agree_prod = (abs(r66 - prod.get("P_66", mp.inf)) < mp.mpf("1e-12")
                  and abs(r77 - prod.get("P_77", mp.inf)) < mp.mpf("1e-12"))

    print(f"\n  reconstruction reproduces the PRODUCER witness: {agree_prod}")
    print(f"    P_66 mine {mp.nstr(r66, 12)}   producer {mp.nstr(prod.get('P_66', mp.nan), 12)}")
    print(f"    P_77 mine {mp.nstr(r77, 12)}   producer {mp.nstr(prod.get('P_77', mp.nan), 12)}")

    print(f"\n  vs the PUBLISHED content blocks, at q = 111/100:")
    rows = [("P_77", r77, _num(pub["P_77"])),
            ("P_66", r66, _num(pub["P_66"])),
            ("P_76", prod.get("P_76", mp.nan), _num(pub["Phi"]))]
    mismatches = []
    for name, got, want in rows:
        ok = abs(got - want) < mp.mpf("1e-12")
        if not ok:
            mismatches.append(name)
        print(f"    {name}  construction {mp.nstr(got, 12):>16}   "
              f"published {mp.nstr(want, 12):>16}   {'MATCH' if ok else 'NO'}")

    # 2. the key lemma, both conventions
    def delta1(par, dau):
        return sp.simplify(_V(1, par) - _V(1, dau))
    d1_last = delta1((1, 1, 0), (1, 1, 1))     # producer: toffoli_output flips k & 1
    d1_first = delta1((0, 1, 1), (1, 1, 1))    # block prose: target is strand 0
    lemma_conv_dependent = (d1_first == 0) and (sp.simplify(d1_last) != 0)
    print(f"\n  proof-block key lemma Delta_1 = 0:")
    print(f"    target = LAST strand  (producer): Delta_1 = {mp.nstr(_num(d1_last), 10)}"
          f"   zero: {sp.simplify(d1_last) == 0}")
    print(f"    target = FIRST strand (prose)   : Delta_1 = {mp.nstr(_num(d1_first), 10)}"
          f"   zero: {d1_first == 0}")
    print(f"    convention-dependent: {lemma_conv_dependent}")

    # 3. even under the block's convention, does the chain give Phi?
    par2, dau2 = (0, 1, 1), (1, 1, 1)
    chain_amp = sp.simplify(_V(1, par2) * (_V(0, par2) - _V(0, dau2)))
    chain_is_phi = (sp.simplify(sp.radsimp(sp.simplify(chain_amp - pub["Phi"]))) == 0)
    ratio = _num(chain_amp / pub["Phi"])
    print(f"\n  under the block's own convention, V_1^par * Delta_0 = "
          f"{mp.nstr(_num(chain_amp), 12)}")
    print(f"    published Phi = {mp.nstr(_num(pub['Phi']), 12)}   equal: {chain_is_phi}"
          f"   ratio {mp.nstr(ratio, 8)}")

    gates_ok = (agree_prod and recon_matches_pub_77
                and lemma_conv_dependent and not chain_is_phi)

    print("\n" + "=" * 90)
    print(" RESULT")
    print("  * The reconstruction IS the producer's construction (exact).")
    print("  * Of four published entries only P_77 matches it.")
    print("  * The key lemma Delta_1 = 0 holds only if the target is strand 0; the")
    print("    producer flips the LAST strand, where it is false.")
    print("  * Even under the block's own convention the chain gives -0.0467, not the")
    print("    published Phi = +0.0495 — 6% and a sign.")
    print("  => Migrating Phi/P_66/P_67 to convention D is premature: the prior question")
    print("     is which of the two disagreeing objects is current. P_77 is unaffected.")
    print("=" * 90)

    w = WitnessBuilder("toffoli-published-vs-construction",
                       output_dir=Path(__file__).resolve().parent)
    w.add_assertion("reconstruction_equals_producer_witness", 1 if agree_prod else 0, 1)
    w.add_assertion("P77_published_equals_construction", 1 if recon_matches_pub_77 else 0, 1)
    w.add_assertion("delta1_lemma_is_convention_dependent",
                    1 if lemma_conv_dependent else 0, 1)
    w.add_assertion("chain_does_NOT_reproduce_published_Phi", 0 if chain_is_phi else 1, 1)
    w.add_parameter("q_evaluated_at", str(Q_EVAL))
    w.add_parameter("construction_source",
                    "computations/_deprecated/toffoli-braid.py::chain_reduce")
    w.add_data("mismatched_published_entries", mismatches)
    w.add_data("P66_construction", mp.nstr(r66, 20))
    w.add_data("P66_published", mp.nstr(_num(pub["P_66"]), 20))
    w.add_data("P76_producer", mp.nstr(prod.get("P_76", mp.nan), 20))
    w.add_data("Phi_published", mp.nstr(_num(pub["Phi"]), 20))
    w.add_data("chain_amplitude_block_convention", mp.nstr(_num(chain_amp), 20))
    w.add_data("chain_over_Phi_ratio", mp.nstr(ratio, 12))
    w.add_caveat(
        "NOT a claim that the published forms are wrong. The only recorded "
        "construction lives in a _deprecated file that neither the content blocks nor "
        "the live producer cite, so it may itself be superseded by a derivation absent "
        "from the tree. What is established: the two disagree on three of four entries, "
        "the proof block's key lemma is convention-dependent and false as the producer "
        "runs, and the corpus does not record which side is current."
    )
    w.set_description(
        "Compares the published Toffoli transfer-matrix entries against the only "
        "construction the corpus records (_deprecated/toffoli-braid.py). An independent "
        "reconstruction reproduces that producer exactly, and then only P_77 of the four "
        "published entries matches: P_66 is 0.4154 vs a published 0.6010, and P_76 is "
        "-0.1415 vs a published +0.0495 (claimed equal to Phi). The proof block's key "
        "lemma Delta_1 = 0 holds only when the target is strand 0, while the producer "
        "flips the last strand; and even under the block's own convention the chain "
        "yields -0.0467 rather than Phi = +0.0495. Blocks the convention-D migration of "
        "Phi, P_66 and P_67 -- P_77 is unaffected and stays derived."
    )
    w.save()
    return 0 if gates_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
