#!/usr/bin/env python3
# polynomial_q_not_applicable: round 25 is a representation-theory grounding of
# the (2,2)=EM channel.  All computation is EXACT finite character theory of S_4
# (rational arithmetic) + partition-conjugate (transpose) combinatorics. No
# q-deformation, no mpmath, no sympy required (the q-dimension of (2,2) is
# [4]_q/[2]_q = q^2+q^-2, already in EHartreeTraceRatio.lean; not recomputed here).
"""
conj:e-hartree-categorical-derivation — ROUND 25 (why the EM channel is (2,2)).

THE DEEP (2,2)=EM PUSH.  Rounds 19-24 *posit* that the molecular electromagnetic
exchange between the two covalent electrons lives in the self-transpose (2,2)
scalar Wedderburn block of H_4(q) (the "(2,2)=EM identification", the conjecture's
core conditional).  The corpus justifies the choice as "(2,2) is the unique
self-transpose partition of 4, Schur-Weyl dual of the 2-dim slot space".  This
probe gives a COMPLEMENTARY, physically-grounded derivation that connects (2,2)
to the covalent-PAIR structure via standard induction — it does NOT close the
conjecture, it grounds the channel choice.

THE ARGUMENT (standard representation theory, not fitted).
  * The 2-strand EM coupling is the SINGLET idempotent e_- = Lambda^2 A, i.e. the
    SIGN representation sgn of S_2 (prop:em-coupling-projection: the unique scalar
    exchange channel, |tr_tau(e_-)|^2 = q^-1).
  * A covalent single bond shares exactly TWO electrons (Pauli-2), each carrying
    one EM singlet exchange => the pair sits in sgn (x) sgn on S_2 x S_2.
  * Inducing to the 4-strand molecular braid (S_4):
        Ind_{S_2 x S_2}^{S_4}(sgn (x) sgn) = (2,2) (+) (2,1,1) (+) (1,1,1,1)
    each with multiplicity 1 (verified here by Frobenius reciprocity against the
    S_4 character table).  Equivalently s_{1,1} * s_{1,1} = s_{2,2}+s_{2,1,1}+s_{1^4}.
  * The three summands have a clean physical reading:
        (2,2)     -- the UNIQUE self-transpose summand = the parity-symmetric,
                     Frobenius-self-dual (antipode-closed) BOUND-STATE channel,
        (2,1,1)   -- transpose of (3,1); the FORCE-CARRIER channel that
                     conj:force-carrier-intertwining-correspondence assigns to
                     T_{2,9} on a 4-strand braid (corroboration, not used as input),
        (1,1,1,1) -- fully antisymmetric = the DECOUPLED / separated-atom channel.
  * A covalent bound state has definite (symmetric) parity, hence is closed under
    the Hopf antipode S: V_lambda -> V_{lambda^T}; so its channel must be
    self-transpose.  Among the induced summands ONLY (2,2) is self-transpose.
    => the EM bound-state channel is FORCED to (2,2).

WHAT THIS DELIVERS vs WHAT REMAINS (honest, critical-distance).
  ADVANCES: the (2,2)=EM channel is no longer an isolated "unique self-transpose
  of 4" assertion -- it is the self-dual summand of the induced DOUBLED EM singlet
  (sgn (x) sgn), tying it to the covalent-pair (Pauli-2) physics and the 2-strand
  EM singlet of em-coupling-projection.  The decomposition's other two summands
  match the force-carrier (2,1,1) and decoupled (1^4) channels -- a consistency
  check.
  REMAINS (does NOT close the conjecture): (i) the physical input "covalent bond
  = two EM singlets (sgn (x) sgn)"; (ii) the round-20 alpha^2 ALGEBRA landing the
  magnitude on (2,2) (separate); (iii) the m_e c^2 CAL-1 unit.  This is a grounding
  of the core (2,2)=EM conditional, not its elimination.

NON-CIRCULARITY.  prop:em-coupling-projection (sgn = EM singlet) is upstream of
conj:e-hartree (no circularity).  conj:force-carrier-intertwining-correspondence
is itself e-hartree-conditional, so the (2,1,1)=force-carrier coincidence is
recorded only as CORROBORATION, never used to prove anything.

Refs: prop:em-coupling-projection (sgn = the EM singlet e_-); rounds 19-24
((2,2)=EM identification + the alpha^2 algebra); prop:force-carrier-intertwining-
correspondence ((2,1,1) force-carrier channel, conditional -- corroboration only).
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from fractions import Fraction
from itertools import permutations
from pathlib import Path

_HERE = Path(__file__).resolve().parent


# ---- S_4 by brute force (exact; no external deps) ------------------------------
_S4 = list(permutations(range(4)))


def _compose(p, q):
    return tuple(p[q[i]] for i in range(4))


def _inv(p):
    r = [0] * 4
    for i, pi in enumerate(p):
        r[pi] = i
    return tuple(r)


# subgroup H = S_2{0,1} x S_2{2,3}
_E = (0, 1, 2, 3)
_H = [(0, 1, 2, 3), (1, 0, 2, 3), (0, 1, 3, 2), (1, 0, 3, 2)]


def _psi(h):
    """sgn (x) sgn on S_2 x S_2."""
    s1 = -1 if (h[0], h[1]) == (1, 0) else 1
    s2 = -1 if (h[2], h[3]) == (3, 2) else 1
    return s1 * s2


def _chi_ind(g):
    """Induced character Ind_H^{S_4}(psi) at g (standard summation formula)."""
    tot = 0
    for x in _S4:
        c = _compose(_compose(_inv(x), g), x)
        if c in _H:
            tot += _psi(c)
    return Fraction(tot, len(_H))


# S_4 irreducible character table, by class representative.
_REPS = {"e": _E, "(01)": (1, 0, 2, 3), "(01)(23)": (1, 0, 3, 2),
         "(012)": (1, 2, 0, 3), "(0123)": (1, 2, 3, 0)}
_SIZES = {"e": 1, "(01)": 6, "(01)(23)": 3, "(012)": 8, "(0123)": 6}
_CHARTAB = {
    "(4)":       {"e": 1, "(01)": 1,  "(01)(23)": 1,  "(012)": 1,  "(0123)": 1},
    "(3,1)":     {"e": 3, "(01)": 1,  "(01)(23)": -1, "(012)": 0,  "(0123)": -1},
    "(2,2)":     {"e": 2, "(01)": 0,  "(01)(23)": 2,  "(012)": -1, "(0123)": 0},
    "(2,1,1)":   {"e": 3, "(01)": -1, "(01)(23)": -1, "(012)": 0,  "(0123)": 1},
    "(1,1,1,1)": {"e": 1, "(01)": -1, "(01)(23)": 1,  "(012)": 1,  "(0123)": -1},
}


def induced_decomposition():
    """Return {lambda: multiplicity} of Ind_{S_2 x S_2}(sgn (x) sgn) in S_4."""
    indv = {k: _chi_ind(v) for k, v in _REPS.items()}
    out = {}
    for lam, ch in _CHARTAB.items():
        ip = sum(Fraction(_SIZES[k]) * indv[k] * ch[k] for k in _REPS) / 24
        out[lam] = ip
    return out


# ---- partition conjugate (transpose) -------------------------------------------
def conj(lam: tuple[int, ...]) -> tuple[int, ...]:
    if not lam:
        return ()
    return tuple(sum(1 for p in lam if p >= i) for i in range(1, lam[0] + 1))


def main() -> None:
    decomp = induced_decomposition()
    induced = [lam for lam, m in decomp.items() if m != 0]
    mults_ok = (decomp["(2,2)"] == 1 and decomp["(2,1,1)"] == 1
                and decomp["(1,1,1,1)"] == 1 and decomp["(4)"] == 0
                and decomp["(3,1)"] == 0)

    summands = {"(2,2)": (2, 2), "(2,1,1)": (2, 1, 1), "(1,1,1,1)": (1, 1, 1, 1)}
    transposes = {name: conj(p) for name, p in summands.items()}
    self_T = [name for name, p in summands.items() if conj(p) == p]
    em_unique = self_T == ["(2,2)"]

    # all partitions of 4 — (2,2) is the UNIQUE self-conjugate one
    parts4 = {"(4)": (4,), "(3,1)": (3, 1), "(2,2)": (2, 2),
              "(2,1,1)": (2, 1, 1), "(1,1,1,1)": (1, 1, 1, 1)}
    self_T_all = [n for n, p in parts4.items() if conj(p) == p]
    unique_in_4 = self_T_all == ["(2,2)"]

    assertions = [
        {
            "name": "Ind_{S_2 x S_2}^{S_4}(sgn (x) sgn) = (2,2)+(2,1,1)+(1^4), "
            "each multiplicity 1 (Frobenius reciprocity vs S_4 char table)",
            "computed": bool(mults_ok),
            "expected": True,
            "passed": bool(mults_ok),
            "source": "induced doubled EM singlet; s_{1,1}*s_{1,1}="
            "s_{2,2}+s_{2,1,1}+s_{1^4}",
        },
        {
            "name": "(2,2) is the UNIQUE self-transpose summand of the induced "
            "doubled singlet => the parity-symmetric covalent EM bound-state "
            "channel is FORCED to (2,2)",
            "computed": bool(em_unique),
            "expected": True,
            "passed": bool(em_unique),
            "source": "(2,2)^T=(2,2); (2,1,1)^T=(3,1); (1^4)^T=(4); antipode-closed "
            "bound state must be self-transpose",
        },
        {
            "name": "(2,2) is the unique self-conjugate partition of 4 "
            "(corpus assertion, here re-derived)",
            "computed": bool(unique_in_4),
            "expected": True,
            "passed": bool(unique_in_4),
            "source": "transpose involution on partitions of 4",
        },
    ]
    all_passed = all(a["passed"] for a in assertions)

    script_path = Path(__file__).resolve()
    script_hash = hashlib.sha256(script_path.read_bytes()).hexdigest()[:12]

    witness = {
        "engine": "python",
        "engineVersion": f"python {sys.version.split()[0]}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "commitSha": "unknown",
        "assertions": assertions,
        "allPassed": all_passed,
        "computation": "e-hartree-round25-em-channel-induction",
        "scriptFile": script_path.name,
        "scriptHash": script_hash,
        "scriptCommitSha": "unknown",
        "precisionMetadata": {
            "method": "exact finite character theory of S_4 (Fraction) + "
            "partition-conjugate combinatorics",
            "stdlib_only": True,
        },
        "environment": {
            "python": sys.version.split()[0],
            "stdlib_only": True,
            "note": "no sympy/mpmath/qou_substrate (brute-force S_4 + rational "
            "character inner products)",
        },
        "description": (
            "conj:e-hartree round 25 (the deep (2,2)=EM push): grounds the core "
            "(2,2)=EM channel identification via standard induction, WITHOUT "
            "closing the conjecture.  The 2-strand EM coupling is the sign rep "
            "of S_2 (e_- singlet, prop:em-coupling-projection); a covalent bond "
            "is two such singlets (Pauli-2), i.e. sgn (x) sgn on S_2 x S_2; "
            "inducing to S_4 gives (2,2)+(2,1,1)+(1^4) (mult 1 each, verified by "
            "Frobenius reciprocity).  (2,2) is the UNIQUE self-transpose summand "
            "= the parity-symmetric, antipode-closed bound-state channel, so the "
            "covalent EM channel is forced to (2,2); (2,1,1) matches the "
            "force-carrier channel (intertwining-correspondence, corroboration "
            "only -- it is e-hartree-conditional, not used as input) and (1^4) is "
            "the decoupled channel.  ADVANCES the grounding; does NOT close: still "
            "rests on the 'covalent = two EM singlets' input + the round-20 alpha^2 "
            "algebra + the m_e c^2 CAL-1 unit.  No fit, no experimental number."
        ),
        "contentBlock": "conj:e-hartree-categorical-derivation",
        "data": {
            "induced_decomposition": {k: str(v) for k, v in decomp.items()},
            "induced_summands": induced,
            "summand_transposes": {k: list(v) for k, v in transposes.items()},
            "self_transpose_summands": self_T,
            "unique_self_conjugate_partition_of_4": self_T_all,
            "finding": (
                "Ind_{S_2 x S_2}^{S_4}(sgn (x) sgn) = (2,2)+(2,1,1)+(1^4); (2,2) "
                "is the unique self-transpose summand, forcing the parity-symmetric "
                "covalent EM bound-state channel to (2,2).  (2,1,1)=force-carrier "
                "(corroboration), (1^4)=decoupled.  Grounds the (2,2)=EM core "
                "conditional in covalent-pair physics; does not eliminate it."
            ),
        },
    }

    out_path = _HERE / "e-hartree-round25-em-channel-induction.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    out_path.write_text(json.dumps(witness, indent=2) + "\n")

    print("=" * 74)
    print("conj:e-hartree ROUND 25 — why the EM channel is (2,2)")
    print("=" * 74)
    print(f"  Ind_(S2xS2)^S4(sgn(x)sgn) decomposition: "
          f"{ {k: str(v) for k, v in decomp.items() if v != 0} }")
    print(f"  summand transposes: {transposes}")
    print(f"  unique self-transpose summand: {self_T}  (EM bound-state channel)")
    print(f"  unique self-conjugate partition of 4: {self_T_all}")
    print(f"  allPassed={all_passed}")
    print(f"\nWitness saved -> {out_path.name}")


if __name__ == "__main__":
    main()
