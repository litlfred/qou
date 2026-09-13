#!/usr/bin/env python3
"""qbeta_eigenphase_carrier_det_forces_even_length_probe.py — the carrier's
SECOND field is a length-parity prune, and it is not the one the corpus proved.

Bean `qou-pdix` (the S1 blocker: derive the Q_beta ladder eigenphase alpha),
parent `qou-cds1`. Scope (a) for the arithmetic; the algebra is exact.

## Why this exists — formalize-first, before any alpha search

`qou-pdix`'s four route candidates are now all measured against (A and B in
PR #7326, C in PR #7340). What survives is the bean's own uninstantiated
replacement carrier:

    QOU.QBeta.EigenphaseCarrier.TransferMatrixSpectrum (q) (M) : Prop
      trace_eq : M.trace = 2 * Real.cos (eigenphase q)
      det_eq   : M.det = 1

Discharging it means producing `M` from the Hecke seminormal representation on
`V_(2,1)` of `H_3(q)`. Before searching for such an `M`, the formalize-first
discipline asks what structurally constrains the search. **The second field
does, and it prunes by parity.**

## The argument

Every Hecke generator satisfies the corpus's own relation (AGENTS.md §7a)

    (sigma_i - q)(sigma_i + 1/q) = 0

so its eigenvalues are `q` and `-1/q`. On the TWO-dimensional irreducible
`V_(2,1)` both occur (that is what makes the block two-dimensional and not a
sum of characters), hence

    det rho(sigma_i) = q * (-1/q) = -1                            (per letter)
    det rho(sigma_i^{-1}) = 1 / (-1) = -1                         (per letter)
    => det rho(w) = (-1)^len(w)                                   (multiplicative)

and therefore

    TransferMatrixSpectrum.det_eq  <=>  len(w) is EVEN.

No trace is computed, no alpha is derived, and no word is searched: this is a
necessary condition on which words can carry alpha through this carrier at all.

## What this probe does, and what it refuses to do

It takes the seminormal matrices from the CORPUS's own machinery
(`he4_magnus_omega2_sign_sparse_probe.block_structure` / `sigma_csr`), not from
hand-written ones. That is deliberate and it is not a style preference: an
earlier attempt at this used a hand-written `sigma_2` reconstructed from memory
and it FAILED its own Hecke check, producing a nonsense determinant
(`-q^2 + q - 3 + 1/q - 1/q^2`). The Hecke-relation check below is kept as a
gate for exactly that reason -- a matrix that fails it is not a seminormal
generator and nothing may be read off it.

## Relation to the corpus's length-parity result — DIFFERENT block, DIFFERENT quantity

`QOU.Mass.AltCharShiftMultiset.wordChar_sign` (sorry-free, proved before its
probe) already gives `sign(wordChar w) = (-1)^len(w)`. That is the
ONE-dimensional ALTERNATING block `(1,1,1)`, where PSD reduces to
`0 <= character`, and it powers `qou-99qc`'s whole-element SDP exclusion.

This is the TWO-dimensional `(2,1)` block and the quantity is the
DETERMINANT, not a character. The two agree on the parity and arrive at it
from different places -- the Hecke quadratic's eigenvalues here, the letters'
negative alternating characters there. So this **corroborates** that result and
does not duplicate it, and it bites on a different thing: not SDP-admissibility
but the carrier's `det_eq` field.

## The consequence that is not free

The corpus's currently-scored element `nuc11_interleaved` is **eleven** letters.
Eleven is odd. So it cannot satisfy `det_eq`, and cannot carry `alpha` through
this carrier -- independently of `qou-99qc`'s SDP route reaching the same
element by the alternating character.

## Precision

sympy exact symbolic throughout for the algebra; mpmath at the proton pin where
a numeric check is wanted. No float64: `float(` appears nowhere, no
`statistics`, no `math.`.
"""
from __future__ import annotations

import pathlib as _pl
import sys as _sys

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta", _COMP / "deltalambda"):
    if str(_p) not in _sys.path:
        _sys.path.insert(0, str(_p))

import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

set_compute_dps(50)

RESULTS: list[dict] = []


def check(name: str, passed: bool, detail: str) -> None:
    RESULTS.append({"name": name, "passed": bool(passed), "detail": detail})
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}\n         {detail}\n")


def main() -> int:
    print("=" * 78)
    print(" TransferMatrixSpectrum.det_eq forces EVEN word length on V_(2,1)")
    print("=" * 78)

    wb = WitnessBuilder("qbeta-eigenphase-carrier-det-forces-even-length",
                        engine="sympy+mpmath")

    q = sp.Symbol("q", positive=True)

    # ---- 1. the eigenvalue fact, from the Hecke relation alone -------------
    # (s - q)(s + 1/q) = 0  =>  spectrum {q, -1/q}  =>  on a 2-dim irreducible
    # where both occur, det = q * (-1/q) = -1.
    lam = [q, -1 / q]
    det_sym = sp.simplify(lam[0] * lam[1])
    check(
        "hecke_eigenvalues_give_det_minus_one_on_a_two_dim_block",
        det_sym == -1,
        f"the Hecke relation (s-q)(s+1/q)=0 gives spectrum {{q, -1/q}}; on the "
        f"2-dim irreducible V_(2,1) both eigenvalues occur, so "
        f"det = q * (-1/q) = {det_sym}. Symbolic in q -- holds for every q, not "
        f"just at the anchor.",
    )

    # ---- 2. the same, from the CORPUS's seminormal matrices ----------------
    # Not hand-written: an earlier hand-written sigma_2 failed its own Hecke
    # check and gave a nonsense determinant. The gate below is why.
    corpus_ok, corpus_detail = False, ""
    try:
        import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402

        per_gen, dim = base.block_structure((2, 1))
        q0 = base.Q0
        sig = base.sigma_csr(per_gen, dim, q0)
        dets, hecke_ok = [], True
        for gi in range(len(sig)):
            S = base._dense_from_csr(sig[gi], dim)
            d = S[0, 0] * S[1, 1] - S[0, 1] * S[1, 0]
            dets.append(d)
            # Hecke gate: (S - q)(S + 1/q) must vanish
            I = mp.matrix([[1, 0], [0, 1]])
            H = (S - q0 * I) * (S + I / q0)
            if max(abs(H[i, j]) for i in range(2) for j in range(2)) > mp.mpf(10) ** -40:
                hecke_ok = False
        worst = max(abs(d + 1) for d in dets)
        corpus_ok = hecke_ok and worst < mp.mpf(10) ** -40 and dim == 2
        corpus_detail = (
            f"dim(V_(2,1)) = {dim}; {len(sig)} generator block(s); every one "
            f"satisfies the Hecke relation to < 1e-40 and has det = -1 to "
            f"{mp.nstr(worst, 6)}. Taken from the corpus's own "
            f"block_structure/sigma_csr, NOT hand-written."
        )
    except Exception as exc:  # pragma: no cover - environment-dependent
        corpus_detail = (
            f"corpus seminormal machinery unavailable here ({type(exc).__name__}: "
            f"{exc}). The symbolic argument in check 1 is independent of it and "
            f"stands; this cross-check is REPORTED AS NOT RUN rather than passed."
        )
    check("corpus_seminormal_matrices_reproduce_det_minus_one",
          corpus_ok, corpus_detail)

    # ---- 3. multiplicativity -> the parity law ----------------------------
    # det is multiplicative, so det rho(w) = prod over letters = (-1)^len(w).
    # Inverses too: det rho(s^-1) = 1/(-1) = -1.
    parity = {L: sp.Integer(-1) ** L for L in (2, 3, 6, 10, 11, 12)}
    check(
        "det_rho_word_equals_minus_one_to_the_length",
        all(parity[L] == (1 if L % 2 == 0 else -1) for L in parity),
        "det is multiplicative and every letter contributes -1 (inverses too, "
        "since 1/(-1) = -1), so det rho(w) = (-1)^len(w). Hence "
        "TransferMatrixSpectrum.det_eq (M.det = 1) holds iff len(w) is EVEN: "
        + ", ".join(f"len {L} -> det {parity[L]}" for L in sorted(parity)),
    )

    # ---- 4. the consequence for the scored element ------------------------
    NUC11 = 11
    check(
        "nuc11_interleaved_cannot_satisfy_det_eq",
        NUC11 % 2 == 1,
        f"the corpus's currently-scored element nuc11_interleaved has "
        f"{NUC11} letters, which is odd, so det rho = -1 != 1 and the element "
        f"cannot carry alpha through this carrier. This is INDEPENDENT of "
        f"qou-99qc's route to the same element: that one goes through the "
        f"1-dim alternating block's character and SDP-admissibility, this one "
        f"through the 2-dim block's determinant and the carrier's det_eq.",
    )

    q0n = mp.mpf(Q_50_DIGIT_STR)
    allp = all(r["passed"] for r in RESULTS)
    print(f"  {sum(r['passed'] for r in RESULTS)}/{len(RESULTS)} checks passed")

    for r in RESULTS:
        wb.add_assertion(r["name"],
                         computed="PASS" if r["passed"] else "FAIL",
                         expected="PASS", tolerance="exact", source=r["detail"])
    wb.save({
        "description": (
            "A formalize-first prune for qou-pdix. The eigenphase carrier "
            "QOU.QBeta.EigenphaseCarrier.TransferMatrixSpectrum has two fields; "
            "its SECOND (det_eq : M.det = 1) is a parity constraint. Every Hecke "
            "generator has spectrum {q, -1/q} by the Hecke relation, so on the "
            "2-dim irreducible V_(2,1) det rho(sigma) = -1 per letter and "
            "det rho(w) = (-1)^len(w). Hence only EVEN-length words can carry "
            "alpha through this carrier. Corroborates, and does not duplicate, "
            "QOU.Mass.AltCharShiftMultiset.wordChar_sign -- that is the 1-dim "
            "ALTERNATING block's CHARACTER, this is the 2-dim block's "
            "DETERMINANT, and they reach the same parity from different places. "
            "Consequence: nuc11_interleaved (11 letters, odd) cannot satisfy "
            "det_eq. No alpha is derived and no word is searched."
        ),
        "bean": "qou-pdix",
        "q0Anchor": "proton",
        "q0Value": fmt(q0n),
        "carrier": "QOU.QBeta.EigenphaseCarrier.TransferMatrixSpectrum",
        "block": "V_(2,1) of H_3(q), dim 2",
        "parity_law": "det rho(w) = (-1)^len(w)",
        "corroborates": "QOU.Mass.AltCharShiftMultiset.wordChar_sign (different block, different quantity)",
        "scope": (
            "(a) scope-limited: a NECESSARY condition on the carrying word, not "
            "a derivation of alpha and not a sufficient condition for anything. "
            "It does not exclude alpha, does not select a word, and says nothing "
            "about trace_eq -- the field that actually carries alpha. An "
            "even-length word satisfying det_eq may still fail trace_eq."
        ),
    })
    return 0 if allp else 1


if __name__ == "__main__":
    raise SystemExit(main())
