#!/usr/bin/env python3
"""Measure the effective bond dimension χ_eff(k) of the atom-braid Markov trace.

Decisive gate (direction 1) of the atom-braid program (PR #2389): does the atom
braid populate ≪ p(3k) intermediate partitions at each strand-cut (→ a restricted
MPS could beat the p(3A) wall), or all p(3k) (→ the wall is intrinsic)?

Reports, per nucleon-level k:
  - p(3k)                     (total Wedderburn sectors / partition labels)
  - #partitions reached       (structural Bratteli support, bratteli_state_sizes)
  - Σ running-multiplicity    (full Bratteli-path count — what the partition basis
                               collapses away)
and, for small A, the NUMERICAL nonzero-χ^λ count (no accidental zeros at q₀).

Verdict (see docs/audits/2026-06-16-bond-dimension-verdict-p3A-wall-intrinsic.md):
χ_eff(k) = p(3k) exactly → no support reduction → the transfer is already minimal →
exact ¹⁶O is out of reach; heavy nuclei stay on the A→∞ q-CLT extrapolation.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from chi_atom_transfer import bratteli_state_sizes  # noqa: E402
from chi_monotone_transfer import chi_all_lambda  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from lr_coefficients import partitions_of  # noqa: E402
import mpmath as mp  # noqa: E402


def structural(max_A: int = 8) -> None:
    print("STRUCTURAL bond dimension (Bratteli reachability):")
    print(f"  {'k':>3} {'3k':>4} {'p(3k)':>8} {'#reached':>10} {'Σ paths':>16}  full?")
    for A in range(1, max_A + 1):
        k, nreach, nstates = bratteli_state_sizes(A)[-1]
        p3k = len(partitions_of(3 * k))
        print(f"  {k:>3} {3*k:>4} {p3k:>8} {nreach:>10} {nstates:>16}  "
              f"{'YES' if nreach == p3k else 'no'}")


def numerical(atoms=(("D", 1, 1), ("3He", 2, 1), ("4He", 2, 2)), dps: int = 40) -> None:
    mp.mp.dps = dps
    print(f"\nNUMERICAL support (nonzero χ^λ at q₀, dps={dps}):")
    for lbl, Z, N in atoms:
        n = 3 * (Z + N)
        chi = chi_all_lambda(atom_braid_word_3A(Z, N), n, dps=dps)
        nz = sum(1 for v in chi.values() if abs(v) > mp.mpf("1e-30"))
        p3a = len(partitions_of(n))
        flag = "= p(3A)" if nz == p3a else f"≠ p(3A)={p3a}"
        print(f"  {lbl:<4} n={n:<3} nonzero χ^λ = {nz:>4}  ({flag})")


def row_tail(atoms=(("D", 1, 1), ("3He", 2, 1), ("4He", 2, 2)), dps: int = 40) -> None:
    """SU_q(3) question: contribution of >row-r sectors to tr_M (atom + free).

    🛑 THIS LEG'S PREMISE IS FALSE UNDER CONVENTION D.  Re-measured 2026-08-29.

    The paragraph below used to open "y_λ is the Wenzl PRINCIPAL Schur specialization
    (canonical Jones–Markov trace, NONZERO FOR ALL λ)".  Under the canonical trace
    convention D (`z = q^3/(q^2+1)`, owner ruling 2026-08-15) the Wenzl level is
    `r = 2`, so `y_λ = 0` EXACTLY for every partition with three or more rows
    (`QOU.…wenzlLevel_conventionD` + `schurPrincipal_eq_zero_iff`, both sorry-free).
    Measured at the proton pin: `max|y_λ|` over the ℓ≥3 stratum is **0.0** at n=6 and
    n=9, against 0.115 and 0.0221 over all λ.

    AND THIS FUNCTION HAS NEVER RUN.  `y_lambda_at` is not imported anywhere in this
    module — not at module scope, not locally — so `row_tail` raised
    `NameError: name 'y_lambda_at' is not defined` at its first atom, on `main()`'s
    every invocation, for as long as the call has been there.  So the 0.2–3.4 %
    figures below are not merely convention-C: nothing in the tree reproduces them.
    (A `NameError` is a defect, not one of this corpus's designed refusals — no
    guard the cone defines raises it.)  Import added 2026-08-29.

    The figures below were therefore measured in a standalone harness reproducing
    this function's arithmetic, and then confirmed by running the repaired file.
    Since the truncations differ only in terms with `len(l) >= 3`, all carrying
    `y_λ = 0`:

        atom   ≤2 miss   ≤3 miss   ≤4 miss      (measured 2026-08-29, D, proton pin)
        D          0.0       0.0       0.0
        ³He        0.0       0.0       0.0

    identical at float64 and at 50-dps, so this is exact, not a precision artifact.

    WHAT THAT DOES TO THE TWO CLAIMS, scoped separately because they fare differently:

    * "the ≤3-row SU_q(3) restriction is a DIFFERENT trace, a 0.2–3.4 % error growing
      with A, invalid at the 1-ppQ floor" — the 0.2–3.4 % figures are CONVENTION-C
      measurements and are kept here as that.  Under D the ≤2-row truncation is
      already exact, so this measurement supports no error and no invalidity verdict.
      The verdict may still be true on other grounds; it does not follow from here.
    * "the free reference also carries >3-row content (≥ the atom's), refuting
      'binding lives in >3-row sectors'" — the CONCLUSION survives and is in fact
      stronger under D (those sectors carry no weight at all), but the EVIDENCE
      given for it is now false: neither the atom nor the free reference carries any
      >3-row content, so "≥ the atom's" is comparing two zeros.  Do not cite this
      function as the measurement behind that refutation.

    UNAFFECTED: `structural()` and `numerical()`, and with them the headline verdict
    `χ_eff(k) = p(3k)` / the p(3A) wall is intrinsic.  Neither calls `y_lambda_at` —
    one counts Bratteli support, the other counts nonzero χ^λ — so the verdict in
    docs/audits/2026-06-16-bond-dimension-verdict-p3A-wall-intrinsic.md stands, and
    that document does not carry the row-tail figures (checked).

    THREE DEFECTS, then, in one leg: a premise convention D falsifies, a `float(Q0)`
    cast feeding float64 into a computation, and a missing import that made the whole
    function unrunnable.  The last one is why the first two survived — a function that
    always crashes is never read for its numbers.

    Bean qou-5wng.  Found via the witnessless-consumer list in
    computations/audits/ylambda_threerow_frame_audit.py: this file emits no witness,
    so no numeric or dating layer could have reached it.
    """
    # `y_lambda_at` was NEVER imported, at module scope or here, so this function
    # raised NameError at its first atom on every run. Added 2026-08-29; see the
    # docstring's third defect.
    from wedderburn_jones_markov import y_lambda_at  # noqa: E402
    from q_parameter import Q_MP as Q0  # noqa: E402

    def ymp(v):
        return mp.mpc(v) if isinstance(v, complex) else mp.mpf(str(v))

    mp.mp.dps = dps
    print(f"\nROW-TAIL (>r-row contribution to |tr_M|, dps={dps}):")
    print(f"  {'atom':<5} {'≤2 miss':>10} {'≤3 miss':>10} {'≤4 miss':>10}   free ≤3 miss")
    for lbl, Z, N in atoms:
        n = 3 * (Z + N)
        # Full-precision q0, NOT float(Q0): the cast dropped the pin at digit 17
        # (1.1099785827513808 against 1.109978582751380807591669...), feeding a
        # float64 into a computation rather than a display. NO-FLOAT64 applies to
        # probes exactly as to producers.
        y = y_lambda_at(n, Q0)
        chA = chi_all_lambda(atom_braid_word_3A(Z, N, include_inter=True), n, dps=dps)
        chF = chi_all_lambda(atom_braid_word_3A(Z, N, include_inter=False), n, dps=dps)

        def tr(ch, mr=99):
            return sum(ymp(y[l]) * ch[l] for l in ch if len(l) <= mr)

        Af = abs(tr(chA))
        miss = [float(abs(tr(chA) - tr(chA, mr)) / Af) for mr in (2, 3, 4)]
        free_miss3 = float(abs(tr(chF) - tr(chF, 3)) / abs(tr(chF)))
        print(f"  {lbl:<5} {miss[0]:>10.3e} {miss[1]:>10.3e} {miss[2]:>10.3e}"
              f"   {free_miss3:.3e}")


def main() -> int:
    structural(8)
    numerical()
    row_tail()
    print("\nχ_eff(k) = p(3k) exactly → no support reduction → p(3A) wall is intrinsic.")
    print("y_λ = principal specialization. Under convention D the Wenzl level is r=2,")
    print("so y_λ = 0 exactly for ℓ≥3 and every row-tail miss above is 0.0 — see the")
    print("row_tail docstring: the 0.2–3.4 % figures were convention C, and the")
    print("'free nuclei need >3-row too' evidence is comparing two zeros. The")
    print("χ_eff = p(3A) verdict is unaffected; it never used y_λ.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
