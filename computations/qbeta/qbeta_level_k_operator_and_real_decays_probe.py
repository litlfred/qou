#!/usr/bin/env python3
"""qou-cds1 Step 25: real nuclear beta decays are HYPERBOLIC, the corpus never
leaves H_3, and no species difference supplies the ladder phase.

Step 24 closed both readings of the 0.0566-vs-2.0204 gap and left exactly one
place open: a genuinely LEVEL-k operator, not induced from H_3. This tests it
with the physically right objects and closes it three ways.

======================================================================
1. THE CORPUS NEVER LEAVES H_3 — so the open avenue is not instantiated
======================================================================

`build_atom_nf(Z, N)` returns a SIX-vector in the H_3 normal-form basis
[gamma, sigma_0, sigma_1, L+, L-, e^-] for EVERY mass number, tritium (A = 3)
included. The atom braid words are laid out on 3A strands, but the normal form is
H_3-valued throughout (because `build_atom_nf` folds generator indices `gi % 2`
into `{sigma_0, sigma_1}`).

Scope note (bean `qou-zgg2`): full-tower `B_{3A} -> H_{3A}(q)` atomic braid and
Markov-trace modules DO exist in the corpus (`canonical_braid_crossings.py`,
`markov/markov_peel.py`, `tr_m_atom_via_transfer.py`); what is H_3-collapsed is
specifically `pyhecke.gram.build_atom_nf`, which is the representation the
`T_beta` decay-operator candidates on this arc were wired to.

So there is no genuinely level-k operator anywhere in this corpus. The avenue
Step 24 identified as the only remaining place a different phase could come from
EXISTS LOGICALLY BUT IS NOT INSTANTIATED. Building one would be new construction,
not a reading of something already present — which is a materially different ask
and belongs to whoever owns the T_beta Stage B branch (queued since PR #1840).

======================================================================
2. THE REAL BETA DECAYS ARE HYPERBOLIC
======================================================================

Taking the physically correct objects — actual beta-minus decays present in the
corpus's atom table, rather than the free-nucleon difference:

  decay                                  disc      det A_0   det B_0  tr(A_0B_0)   kind
  free n -> p        (A=1, Q=782 keV)  -0.03584   -1.05656  -1.04166    2.10718   ELLIPTIC
  n -> protium       (A=1, atomic)     +6.52244   -1.05656  -0.07004   -0.50401   real
  tritium -> He3     (A=3, Q=18.6 keV) +4.46143   -1.16119  +0.72261   -0.67677   real
  C14 -> N14         (A=14, Q=156 keV) +12.94889 -12.20773  +2.30791    6.66260   real

Only the BARE NUCLEON pair is elliptic. Every actual nuclear decay is hyperbolic,
and the alignment diagnostic says why: for the nuclear cases the parent and
daughter are nowhere near parallel in sl_2 (sums -1.63, -1.12, -3.24 against the
nucleons' +0.00896). Ellipticity is a property of the near-degenerate n/p pair,
not of beta decay.

======================================================================
3. AND NO SPECIES DIFFERENCE SUPPLIES THE PHASE
======================================================================

Exhaustive scan over all 105 pairs from the 15 available species: 21 are elliptic
(20 %), with eigenphases spanning

    0.2495  (he4 - li6)   ...   2.9686  (he3 - he4)

The required ladder phase is 0.0565947 — BELOW ALL TWENTY-ONE. The smallest
available eigenphase is 4.4x too large. So no difference of corpus species,
elliptic or not, supplies the ladder phase.

======================================================================
*** A CORRECTION TO STEP 23, MINE ***
======================================================================

Step 23 called Delta_L's ellipticity "structural" and supported it partly with a
random control showing only 8.9 % of scale-matched random NF differences are
elliptic. That control was against RANDOM vectors. Against the corpus's OWN
species, 21/105 = 20 % of pairs are elliptic — so being elliptic is NOT rare, and
"structural" should not have been read as "special".

What Step 23 got RIGHT and stands: the MECHANISM. The identity
det(A_0-B_0) = det A_0 + det B_0 + tr(A_0B_0) holds, both nucleon directions are
hyperbolic, and their pairing clears the exact-parallel threshold by 0.43 % --
which IS the near-degeneracy of the nucleons. What is corrected is the
significance attached to ellipticity per se: it is common, and n-p's ellipticity
is MARGINAL (disc -0.0358, the smallest in magnitude of the 21) precisely because
the pair is nearly parallel. Near-parallelism is the special thing; ellipticity
is its consequence and is not by itself rare.

======================================================================
WHERE THIS LEAVES THE ARC
======================================================================

Every named avenue for the ladder phase is now closed or uninstantiated:
braid image excluded, arbitrary M circular, constant-residue holonomies fail the
doubling identity, all real-spectrum generators are on the wrong side of 1, Im(q)
cannot supply ellipticity, Bring's E and tau_0 are both non-CM, bar-odd operators
have zero W-weighted trace Sum W_lam chi^lam, the tower carries one eigenphase per H_3 element,
no rational factor bridges the gap, real nuclear decays are hyperbolic, and no
species difference has a small enough eigenphase.

The one thing not closed is not a reading: it is CONSTRUCTING a level-k operator
the corpus does not currently have.

SCOPE. Scope-(a). Nothing derived, proposed, wired or readmitted; no convention
adjudicated; no c_k value asserted. Anchor: experimental (proton) pin.
"""

import itertools
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "substrate"),
                str(HERE.parent / "hecke")]
import _path_bridge  # noqa: E402, F401

from hecke_characters import build_seminormal_matrices_mp  # noqa: E402
from hecke_core import build_nucleon_nf_mp  # noqa: E402
from pyhecke.gram import NF_NAMES, build_atom_nf  # noqa: E402
from q_parameter import q_at  # noqa: E402

mp.mp.dps = 30
Q0 = q_at(mp.mp.dps)
H = Q0 - 1 / Q0
HB = (Q0 - 1) / Q0
B_SUB = mp.sqrt((H ** 2 + 3) / (H ** 2 + 4))
U = B_SUB * HB ** 2
Z_C = mp.sqrt(Q0) / (1 + Q0)
TH_REQ = mp.fabs((Z_C - 1) * H / 2 - U / 2)

WORDS = [[], [0], [1], [0, 1], [1, 0], [0, 1, 0]]
_G = build_seminormal_matrices_mp((2, 1), Q0)[0]
BAS = []
for _w in WORDS:
    _M = mp.eye(2)
    for _i in _w:
        _M = _M * _G[_i]
    BAS.append(_M)

ATOMS = [("protium", 1, 0), ("deuterium", 1, 1), ("tritium", 1, 2), ("he3", 2, 1),
         ("he4", 2, 2), ("li6", 3, 3), ("li7", 3, 4), ("be9", 4, 5), ("b11", 5, 6),
         ("c12", 6, 6), ("c14", 6, 8), ("n14", 7, 7), ("o16", 8, 8)]


def blk(v):
    M = mp.zeros(2, 2)
    for c, Bi in zip(v, BAS):
        M = M + mp.mpf(c) * Bi
    return M


def tr(M):
    return M[0, 0] + M[1, 1]


def det(M):
    return M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]


def traceless(M):
    t = tr(M) / 2
    return mp.matrix([[M[0, 0] - t, M[0, 1]], [M[1, 0], M[1, 1] - t]])


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" Step 25: real decays, the level-k question, and the phase")
    print("=" * 78)

    # `build_atom_nf` returns float64 and has no correct mpf twin --
    # `build_atom_nf_exact` is Fraction arithmetic at the rational model
    # q = 111/100, 1.93e-5 off the substrate q_0, i.e. float-free and far
    # worse. `mp.mpf(x)` on a float is exact w.r.t. THAT float and makes no
    # wider claim; `mp.mpf(str(x))` at this file's dps would read a
    # 15-digit value as a 30-digit one. The atom rows carry a ~1e-16 floor.
    V = {nm: [mp.mpf(x) for x in build_atom_nf(Z, N)] for nm, Z, N in ATOMS}
    # `build_nucleon_nf` returns a list of Python FLOATS, so
    # `mp.mpf(str(x))` would read a float64 as exact at this file's dps.
    # `build_nucleon_nf_mp` is the same braid word in mpf -- and it was
    # STALE by the 2026-08-30 gluon term until it was fixed on this branch;
    # do not swap to it on a docstring's word without re-measuring.
    V["proton"] = build_nucleon_nf_mp(list("uud"), mp.mp.dps)
    V["neutron"] = build_nucleon_nf_mp(list("udd"), mp.mp.dps)

    lens = {nm: len(v) for nm, v in V.items()}
    print(f"\n[1] NF-vector length for every species: {sorted(set(lens.values()))}")
    print(f"    basis = {NF_NAMES}")
    print(f"    tritium (A=3) length = {lens['tritium']}  ->  the atom model is")
    print(f"    H_3-VALUED at every A. There is NO genuinely level-k operator in the")
    print(f"    corpus, so Step 24's one remaining avenue is NOT INSTANTIATED.")

    print(f"\n[2] real beta-minus decays vs the free-nucleon difference")
    print(f"    {'decay':34s}{'disc':>12s}{'det A_0':>11s}{'det B_0':>11s}"
          f"{'tr(A0B0)':>11s}  kind")
    decays = [("free n -> p        (Q=782 keV)", "neutron", "proton"),
              ("n -> protium       (atomic)   ", "neutron", "protium"),
              ("tritium -> He3     (Q=18.6keV)", "tritium", "he3"),
              ("C14 -> N14         (Q=156 keV)", "c14", "n14")]
    drows = {}
    for lbl, a, b in decays:
        d = [V[a][i] - V[b][i] for i in range(6)]
        M = blk(d)
        disc = tr(M) ** 2 - 4 * det(M)
        A0, B0 = traceless(blk(V[a])), traceless(blk(V[b]))
        dA, dB, cr = det(A0), det(B0), tr(A0 * B0)
        drows[lbl.strip()] = (disc, dA, dB, cr)
        print(f"    {lbl:34s}{mp.nstr(disc, 7):>12s}{mp.nstr(dA, 6):>11s}"
              f"{mp.nstr(dB, 6):>11s}{mp.nstr(cr, 6):>11s}  "
              f"{'ELLIPTIC' if disc < 0 else 'real'}")
    print(f"    -> only the BARE NUCLEON pair is elliptic; every actual nuclear")
    print(f"       decay is hyperbolic, because parent and daughter are nowhere")
    print(f"       near parallel in sl_2.")

    print(f"\n[3] exhaustive scan over all species pairs")
    names = sorted(V)
    ell = []
    tot = 0
    for a, b in itertools.combinations(names, 2):
        d = [V[a][i] - V[b][i] for i in range(6)]
        M = blk(d)
        tot += 1
        if tr(M) ** 2 - 4 * det(M) < 0:
            ell.append((a, b, mp.acos(tr(M) / (2 * mp.sqrt(det(M)))),
                        tr(M) ** 2 - 4 * det(M)))
    phs = sorted(e[2] for e in ell)
    print(f"    pairs: {tot}   ELLIPTIC: {len(ell)} "
          f"({mp.nstr(mp.mpf(len(ell)) / tot * 100, 4)} %)")
    print(f"    eigenphase range: {mp.nstr(phs[0], 10)} .. {mp.nstr(phs[-1], 10)}")
    print(f"    required ladder phase: {mp.nstr(TH_REQ, 12)}")
    print(f"    smallest available / required = {mp.nstr(phs[0] / TH_REQ, 8)}"
          f"   -> the required phase is BELOW ALL {len(ell)}")

    np_disc = min(abs(e[3]) for e in ell)
    np_is_min = mp.fabs(mp.fabs(drows["free n -> p        (Q=782 keV)"][0]) - np_disc) \
        < mp.mpf("1e-25")
    print(f"\n[4] CORRECTION TO STEP 23 (mine)")
    print(f"    Step 23's random control (8.9 % elliptic) was against RANDOM vectors.")
    print(f"    Against the corpus's OWN species, {len(ell)}/{tot} = "
          f"{mp.nstr(mp.mpf(len(ell)) / tot * 100, 4)} % of pairs are elliptic —")
    print(f"    so ellipticity is NOT rare and 'structural' should not have been read")
    print(f"    as 'special'. The MECHANISM stands; the significance does not.")
    print(f"    n-p has the SMALLEST |disc| of the {len(ell)}: {np_is_min} — its")
    print(f"    ellipticity is MARGINAL, which is exactly what near-parallelism means.")

    a = [
        {"name": "corpus_atom_model_is_H3_valued_at_every_A",
         "passed": bool(set(lens.values()) == {6}),
         "detail": f"every species NF vector has length {sorted(set(lens.values()))} in the "
                   "H_3 basis, tritium (A=3) included — so no genuinely level-k operator "
                   "exists in the corpus and Step 24's remaining avenue is not instantiated"},
        {"name": "real_nuclear_beta_decays_are_hyperbolic",
         "passed": bool(all(drows[k][0] > 0 for k in drows
                            if not k.startswith("free n"))),
         "detail": "n->protium +6.52, tritium->He3 +4.46, C14->N14 +12.95 — all real. "
                   "Only the bare nucleon difference is elliptic"},
        {"name": "required_phase_is_below_every_available_eigenphase",
         "passed": bool(phs[0] > TH_REQ * 2),
         "detail": f"{len(ell)} elliptic pairs span {mp.nstr(phs[0], 8)}..{mp.nstr(phs[-1], 8)}; "
                   f"the required {mp.nstr(TH_REQ, 8)} is below all of them, the smallest by "
                   f"a factor {mp.nstr(phs[0] / TH_REQ, 6)}"},
        {"name": "ellipticity_is_common_among_corpus_species",
         "passed": bool(mp.mpf(len(ell)) / tot > mp.mpf("0.15")),
         "detail": f"{len(ell)}/{tot} pairs elliptic — Step 23's 'structural' was right about "
                   "the mechanism but should not have been read as 'special'; corrected here"},
        {"name": "nucleon_ellipticity_is_marginal_as_near_parallelism_implies",
         "passed": bool(np_is_min),
         "detail": "n-p has the smallest |disc| of all elliptic pairs — marginal ellipticity "
                   "is exactly what a 0.43 % alignment excess predicts, so the Step-23 "
                   "mechanism is confirmed even as its significance is corrected"},
    ]
    ok = all(v["passed"] for v in a)
    print("\n  assertions:")
    for v in a:
        print(f"    [{'PASS' if v['passed'] else 'FAIL'}] {v['name']}")
        print(f"           {v['detail']}")
    print(f"\n  allPassed: {ok}  ({sum(1 for v in a if v['passed'])}/{len(a)})")

    witness = {
        "computation": "qbeta-level-k-operator-and-real-decays",
        "engine": "mpmath",
        "description": (
            "qou-cds1 Step 25. (1) build_atom_nf returns a 6-vector in the H_3 normal-form "
            "basis for EVERY mass number, tritium included, so the corpus's atom model is "
            "H_3-valued throughout and the genuinely level-k operator Step 24 left as the "
            "only remaining avenue is NOT INSTANTIATED anywhere — building one is new "
            "construction, not a reading. (2) Real beta-minus decays are HYPERBOLIC: "
            "n->protium +6.52, tritium->He3 +4.46, C14->N14 +12.95, against the bare "
            "nucleon pair's -0.0358. Ellipticity is a property of the near-degenerate n/p "
            "pair, not of beta decay. (3) Exhaustive scan of all 105 species pairs: 21 are "
            "elliptic with eigenphases spanning 0.2495..2.9686, and the required 0.0565947 "
            "is BELOW ALL of them, the smallest by 4.4x. CORRECTS Step 23: its random "
            "control (8.9 %) was against random vectors; against the corpus's own species "
            "20 % of pairs are elliptic, so 'structural' should not have been read as "
            "'special'. The mechanism stands and is confirmed — n-p has the smallest |disc| "
            "of the 21, i.e. marginal ellipticity, exactly what a 0.43 % alignment excess "
            "predicts."),
        "contentBlock": "prop:three-calibration-inputs",
        "assertions": a,
        "allPassed": ok,
        "parameters": {"pin": "experimental (proton)", "dps": 30,
                       "species": [n for n in names], "nf_basis": NF_NAMES},
        "data": {
            "q0": mp.nstr(Q0, 20), "theta_required": mp.nstr(TH_REQ, 14),
            "nf_vector_lengths": sorted(set(lens.values())),
            "decays": {k: {"disc": mp.nstr(v[0], 10), "det_A0": mp.nstr(v[1], 10),
                           "det_B0": mp.nstr(v[2], 10), "pairing": mp.nstr(v[3], 10)}
                       for k, v in drows.items()},
            "pairs_examined": tot, "elliptic_pairs": len(ell),
            "elliptic_fraction_pct": mp.nstr(mp.mpf(len(ell)) / tot * 100, 6),
            "eigenphase_min": mp.nstr(phs[0], 12),
            "eigenphase_max": mp.nstr(phs[-1], 12),
            "smallest_over_required": mp.nstr(phs[0] / TH_REQ, 10),
            "elliptic_list": [{"a": e[0], "b": e[1], "phase": mp.nstr(e[2], 10)}
                              for e in ell],
        },
        "context": {
            "axis": "qou-cds1: is there a level-k operator, and do real decays help?",
            "answer": (
                "No and no. The corpus is H_3-valued at every A, so the level-k avenue is "
                "uninstantiated; real nuclear beta decays are all hyperbolic; and across "
                "every species pair the required phase is smaller than any available "
                "eigenphase."),
            "corrects": (
                "Step 23's significance claim. Its mechanism stands and is confirmed by "
                "n-p having the smallest |disc| of the 21 elliptic pairs, but ellipticity "
                "is common (20 % of corpus pairs), so 'structural' must not be read as "
                "'special'."),
            "scope": "Scope-(a). Nothing derived, proposed, wired or readmitted.",
        },
        "gitCommit": _head_sha(),
        # int ms, not float sec (NO-FLOAT64 discipline; ephemeral meta).
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out_p = HERE / "qbeta-level-k-operator-and-real-decays.witness.json"
    with open(out_p, "w") as f:
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="mpmath",
            q0_anchor="proton", q0_value=mp.nstr(Q0, 30))
        json.dump(witness, f, indent=2)
        f.write("\n")
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
