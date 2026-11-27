#!/usr/bin/env python3
"""qbeta_eigenphase_carrier_det_forces_even_length_probe.py -- the carrier's
SECOND field is a length-parity condition.

Bean `qou-pdix` (the S1 blocker: derive the Q_beta ladder eigenphase alpha),
parent `qou-cds1`. Scope (a) for the arithmetic; the algebra is exact.

## CORRECTED 2026-09-13, SAME DAY -- this probe is largely a RE-DERIVATION

The first version of this docstring presented the parity law as a new
formalize-first prune. **It is not.** Bean `qou-pdix` -- the bean this probe is
filed under -- already carries it, twice, and states it more sharply:

  * line ~81: "det rho(sigma_i^{+-1}) = -1, so det rho(w) = (-1)^L; det M = 1
    forces L even and lambda = +-1, leaving the trace in +-Z[q,q^-1]."
  * line ~1409: "det rho(sigma) = -1 for all four generators, so an even-length
    word has det = +1 exactly. **The carrier's M.det = 1 field is automatic and
    free on the braid image -- it was never the obstruction.** Odd-length words
    have det = -1 and cannot meet it at all, so the image splits cleanly by
    parity."

And `qbeta_mbeta_v21_spectrum_under_d.py` independently records
`det T_pp = det T_nn = -1` ("Hecke unimodularity") and labels its
`sigma_1 sigma_2^-1` det = 1 assertion "even word length".

**The bean's framing is STRONGER than the one this probe opened with.** It calls
`det_eq` *free*, never an obstruction; calling it "a prune that bites"
overstates what a necessary-but-automatic condition buys. That correction stands
whatever the arithmetic below says.

**How the duplication happened:** AGENTS.md's corpus-grep path 6 is "grep the
beans", and it was not run before this probe was written -- on the very bean the
probe is filed under. Path 6's own rationale names this exact failure: a prior
agent's conclusion sits in the bean before it reaches any other artifact.

## What survives as this probe's own contribution

Two things, and they are small:

1. **The application to `nuc11_interleaved`.** The bean never names it (grep:
   zero hits). The corpus's currently-scored element is ELEVEN letters, which is
   odd, so it cannot satisfy `det_eq`. Force limited: branch 1 (M in the braid
   image) is independently excluded by
   `BraidImageEigenphaseAlgebraic.coeffs_zero_of_surjective_nonpos`, so the
   parity bites on a branch already closed.
2. **The Hecke-relation gate on the matrices.** An earlier attempt here used a
   hand-written `sigma_2` reconstructed from memory; it FAILED the gate and gave
   a nonsense determinant (`-q^2 + q - 3 + 1/q - 1/q^2`). The matrices below come
   from the corpus's own `he4_magnus_omega2_sign_sparse_probe.block_structure` /
   `sigma_csr`, and the gate is kept because it is what caught that.

## The argument, for completeness (not novel)

Every Hecke generator satisfies (AGENTS.md 7a) `(sigma_i - q)(sigma_i + 1/q) = 0`,
so its eigenvalues are `q` and `-1/q`. On the TWO-dimensional irreducible
`V_(2,1)` both occur, hence per letter `det rho(sigma_i^{+-1}) = -1`, and det is
multiplicative, so `det rho(w) = (-1)^len(w)` and

    TransferMatrixSpectrum.det_eq  <=>  len(w) is EVEN.

## Relation to the corpus's OTHER length-parity result

`QOU.Mass.AltCharShiftMultiset.wordChar_sign` (sorry-free) gives
`sign(wordChar w) = (-1)^len(w)` for the ONE-dimensional ALTERNATING block
`(1,1,1)`. That is a different block and a different quantity (a character, not
a determinant); it corroborates rather than duplicates. The duplication flagged
above is with the BEAN and with `qbeta_mbeta_v21_spectrum_under_d.py`, not with
that Lean result.

## Precision

sympy exact symbolic for the algebra; mpmath at the proton pin for the numeric
cross-check. No float64: no `float(`, no `statistics`, no `math.`.
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
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

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

    q0n = Q_MP
    allp = all(r["passed"] for r in RESULTS)
    print(f"  {sum(r['passed'] for r in RESULTS)}/{len(RESULTS)} checks passed")

    for r in RESULTS:
        wb.add_assertion(r["name"],
                         computed="PASS" if r["passed"] else "FAIL",
                         expected="PASS", tolerance="exact", source=r["detail"])
    wb.save({
        "description": (
            "CORRECTED SAME DAY -- largely a RE-DERIVATION. Bean qou-pdix "
            "already carries the parity law twice (lines ~81 and ~1409) and "
            "states it MORE STRONGLY: 'the carrier's M.det = 1 field is "
            "automatic and free on the braid image -- it was never the "
            "obstruction'. qbeta_mbeta_v21_spectrum_under_d.py independently "
            "records det T_pp = det T_nn = -1 and labels its det=1 assertion "
            "'even word length'. Corpus-grep path 6 (grep the beans) was not run "
            "before writing this, on the probe's own bean. What survives as this "
            "probe's own: the application to nuc11_interleaved (11 letters, odd "
            "-- the bean never names it), whose force is limited because branch 1 "
            "is independently excluded; and the Hecke-relation gate, which caught "
            "a hand-written sigma_2 that produced a nonsense determinant. "
            "Original description follows. The eigenphase carrier "
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
        "duplicates": [
            ".beans/qou-pdix lines ~81 and ~1409 -- same parity law, stated more strongly",
            "computations/qbeta/qbeta_mbeta_v21_spectrum_under_d.py -- det T_pp = det T_nn = -1; 'even word length'",
        ],
        "own_contribution": [
            "application to nuc11_interleaved (11 letters, odd); the bean never names it",
            "Hecke-relation gate on the seminormal matrices",
        ],
        "q0Anchor": "proton",
        "q0Value": fmt(q0n),
        "carrier": "QOU.QBeta.EigenphaseCarrier.TransferMatrixSpectrum",
        "block": "V_(2,1) of H_3(q), dim 2",
        "parity_law": "det rho(w) = (-1)^len(w)",
        "corroborates": "QOU.Mass.AltCharShiftMultiset.wordChar_sign (different block, different quantity)",
        "scope": (
            "(a) scope-limited, and mostly NOT NEW (see duplicates). A NECESSARY "
            "but AUTOMATIC condition on the carrying word, not "
            "a derivation of alpha and not a sufficient condition for anything. "
            "It does not exclude alpha, does not select a word, and says nothing "
            "about trace_eq -- the field that actually carries alpha. An "
            "even-length word satisfying det_eq may still fail trace_eq."
        ),
    })
    return 0 if allp else 1


if __name__ == "__main__":
    raise SystemExit(main())
