#!/usr/bin/env python3
"""PROBE 2b — the GENUINE Schur-Weyl [1^4]-flavour-projected 12-strand Markov
trace at A=4 (⁴He), replacing the Mayer-cluster stand-in of PROBE 2
(``su4_connected_1111_magnitude_probe.py``).

WHAT CHANGED vs PROBE 2.  PROBE 2 approximated the connected 4-body [1^4]
supermultiplet operator by the irreducible connected (Ursell/Mayer) cluster
``b_A^c`` of the interface graph — a pairwise-derived stand-in whose scale
depended on a ``Σg`` normalisation (a Rule-14 hidden DOF).  This probe computes
the *genuine* categorical object named by the scoping note
(``docs/scope/2026-07-05-gap-a4-interface-operator-attack-scoping.md`` §3 Lever 1)
and the Lean gate (``QOU.MassTheory.SU4SupermultipletGate``):

  the ANTISYMMETRIC SU(4) plethysm  e_A[h_3]  of the A three-quark nucleons,
  realised as a y_λ-normalised sum over the 3A-strand Hecke Markov trace.

CANONICAL CONSTRUCTION (zero fit).  Wigner's SU(4) supermultiplet treats each
nucleon as a 4-flavour unit (p↑,p↓,n↑,n↓) with the 3 quarks in the internal
complete-homogeneous channel h_3.  The fully-antisymmetric [1^A] combination of
A nucleons is the outer-elementary plethysm  e_A[h_3]  (degree 3A).  Its
Schur expansion

    e_A[h_3]  =  Σ_{λ ⊢ 3A}  m_λ · s_λ ,   m_λ = ⟨ e_A[h_3], s_λ ⟩ ,

is computed EXACTLY here (power-sum plethysm  p_k↦p_k[h_3]  +
Murnaghan-Nakayama  ⟨p_ρ,s_λ⟩ = χ^λ(ρ)).  The [1^A]-flavour-projected Markov
trace of the canonical 3A-strand atom braid β_K is then the y_λ-weighted sum
over exactly those λ:

    T_[1^A](K)  =  C(4,A) · Σ_{λ ⊢ 3A}  m_λ · y_λ(q) · χ_λ(β_K) ,

with y_λ the Wenzl bridge weight (``y_lambda_wenzl_bridge``, the SAME weights
that give the Markov closure  tr_M(β) = Σ_λ y_λ χ_λ(β)) and χ_λ the exact
Hoefsmit seminormal character (``mass_at_3A_proper.chi_lambda_of_word`` on the
canonical ``atom_braid_word_3A``).  The SU(4) gate C(4,A) (Lean-proved: dim of
the [1^A] flavour irrep, = # A-subsets of 4 flavours) multiplies the whole
object — **exactly 1 at A=4, exactly 0 at A>4** (no [1^5]/[1^6]).

  • A=4 (⁴He): C(4,4)=1, e_4[h_3] = 10 partitions of 12 (all mult 1,
    dim-check Σ m_λ f^λ = 15400 = 12!/(6^4·24)).  T_[1^4] is the genuine
    connected value.
  • A=6 (⁶Li): C(4,6)=0 ⟹ T_[1^6] ≡ 0 EXACTLY — the α-shell-closure
    locality, supplied by the PROVED gate (as in PROBE 2, the gate is
    load-bearing; the internal plethysm e_6[h_3] of ℓ≤4 partitions of 18 is
    itself non-zero, so the vanishing is the flavour C(4,6)=0, not the trace).

VERDICT DISCIPLINE.  A units-mismatched near-match must NOT be wired
(AGENTS.md §Before declaring refuted; PROBE 2 already flagged this trap).  The
[1^4] channel supplies a super-pairwise enhancement only if a *scale-free*
(no normalisation DOF) ratio built from the y_λ-normalised traces lands at the
measured ×2.093 — reported below with every natural denominator made explicit.

`-- Ref:` Wigner 1937 (SU(4) supermultiplet); Littlewood (plethysm);
Wenzl 1988 (Markov trace); scoping §3 Lever 1;
QOU.MassTheory.SU4SupermultipletGate (Lean gate, sorry-free).
"""
from __future__ import annotations

import sys as _sys
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke")):
    if _p not in _sys.path:
        _sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402
import math  # noqa: E402

from hecke_characters import partitions_of, standard_young_tableaux  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from _precision import fmt, str_at_true_precision  # noqa: E402
import mass_at_3A_proper as m3  # noqa: E402
from hecke_characters import build_seminormal_matrices  # noqa: E402, F401
from hoefsmit_mpmath import (  # noqa: E402
    BlockCacheMP,
    chi_lambda_of_word_sparse_mp,
    seminormal_matrices_mp,
)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# One cache for every partition: BlockCacheMP memoises the Hoefsmit block
# values, which depend only on q, so rebuilding it per irrep would recompute
# the same square roots ten times. Bound at module scope for the same reason
# `set_compute_dps()` is -- both must be in force before any mpf arithmetic.
_BLOCK_CACHE_MP = BlockCacheMP(mp.mpf(Q_50_DIGIT_STR))

# AME2020 total nuclear binding (MeV) — same anchors as PROBE 2.
AME = {"D": mp.mpf("2.224566"), "4He": mp.mpf("28.295673"), "6Li": mp.mpf("31.994564")}


# ══════════════════════════════════════════════════════════════════════
# §1  Plethysm e_A[h_3] → Schur multiplicities m_λ (exact, rational)
# ══════════════════════════════════════════════════════════════════════
def _pmul(a, b):
    out = defaultdict(F)
    for pa, ca in a.items():
        for pb, cb in b.items():
            out[tuple(sorted(pa + pb, reverse=True))] += ca * cb
    return dict(out)


def _pscale(a, s):
    return {k: v * s for k, v in a.items()}


def _padd(*terms):
    out = defaultdict(F)
    for t in terms:
        for k, v in t.items():
            out[k] += v
    return {k: v for k, v in out.items() if v != 0}


def _Pk(k):
    """p_k[h_3] = (p_k^3 + 3 p_k p_{2k} + 2 p_{3k})/6."""
    return _pscale(_padd({(k, k, k): F(1)},
                         {tuple(sorted((k, 2 * k), reverse=True)): F(3)},
                         {(3 * k,): F(2)}), F(1, 6))


def _e_powersum(A):
    """e_A in the power-sum basis as {partition: Fraction}. e_A = Σ_{ρ⊢A}
    ε_ρ p_ρ / z_ρ,  ε_ρ = (-1)^{A-ℓ(ρ)},  z_ρ = ∏ i^{m_i} m_i!."""
    out = {}
    for rho in partitions_of(A):
        rho = tuple(rho)
        ell = len(rho)
        cnt = defaultdict(int)
        for r in rho:
            cnt[r] += 1
        z = 1
        for r, mult in cnt.items():
            z *= (r ** mult) * math.factorial(mult)
        out[rho] = F((-1) ** (A - ell), z)
    return out


def plethysm_e_A_h3(A):
    """e_A[h_3] in the power-sum basis: substitute p_k ↦ p_k[h_3] into the
    power-sum expansion of e_A, then multiply out."""
    e_ps = _e_powersum(A)
    Pcache = {}
    total = {}
    for rho, coeff in e_ps.items():
        term = {(): F(1)}
        for k in rho:
            if k not in Pcache:
                Pcache[k] = _Pk(k)
            term = _pmul(term, Pcache[k])
        total = _padd(total, _pscale(term, coeff))
    return total


def _mn(lam, rho):
    """Murnaghan–Nakayama χ^λ(ρ) via border-strip removal (beta-numbers)."""
    lam = tuple(x for x in lam if x > 0)
    if not rho:
        return 1 if sum(lam) == 0 else 0
    r = rho[0]
    rest = rho[1:]
    lam = list(lam)
    n = len(lam)
    beta = [lam[i] + (n - 1 - i) for i in range(n)]
    bset = set(beta)
    total = 0
    for b in beta:
        if b - r >= 0 and (b - r) not in bset:
            newb = sorted([x for x in beta if x != b] + [b - r], reverse=True)
            ht = sum(1 for x in beta if b - r < x < b)
            newlam = [newb[i] - (n - 1 - i) for i in range(n)]
            newlam = tuple(sorted((x for x in newlam if x > 0), reverse=True))
            total += ((-1) ** ht) * _mn(newlam, rest)
    return total


def schur_multiplicities(A):
    """m_λ = ⟨e_A[h_3], s_λ⟩ = Σ_ρ c_ρ χ^λ(ρ) for λ ⊢ 3A. Returns {λ: int}."""
    ps = plethysm_e_A_h3(A)
    out = {}
    for lam in partitions_of(3 * A):
        lam = tuple(lam)
        val = F(0)
        for rho, c in ps.items():
            if rho == ():
                continue
            val += c * _mn(lam, rho)
        if val != 0:
            assert val.denominator == 1, f"non-integer multiplicity {val} at {lam}"
            out[lam] = int(val)
    return out


def _fdim(lam):
    syt, _, _ = standard_young_tableaux(list(lam))
    return len(syt)


# ══════════════════════════════════════════════════════════════════════
# §2  y_λ-normalised Markov trace of the atom braid, projected onto e_A[h_3]
# ══════════════════════════════════════════════════════════════════════
class ExactCharacterInfeasible(RuntimeError):
    """Raised when χ_λ cannot be computed at the required precision.

    A guard, not a crash. See `_chi` for the measurement behind it.
    """


def _chi(lam, word, n_gens):
    """χ_λ(β_K) in exact mpmath arithmetic.

    THIS PROBE USED TO REFUSE HERE, AND THE REFUSAL IS NOW LIFTED.
    `atom_braid_word_3A` carries exact `mpf` offsets by default
    (`allow_float64=False`), and `mass_at_3A_proper.chi_lambda_of_word`
    multiplies them into `scipy.sparse` matrices, which reject `dtype
    object` -- so those two halves are precision-incompatible. Measured on
    the A=4 word: 25 of its 47 crossings carry an `mpf` coefficient.

    The exact route EXISTS -- `hoefsmit_mpmath.chi_lambda_of_word_mp`, dense
    mpmath, same accumulation order -- and is correct. It is also unaffordable,
    measured at the canonical working precision (dps = 70):

        dim = 132   ((6,6), the SMALLEST of the ten irreps)   81.2 s
        dim = 4158  ((5,3,3,1), the largest)   ~705 h by cubic scaling
        all ten irreps                         ~1135 h

    CORRECTED: an earlier version of this note said 65.7 s / ~571 h. That was
    measured at `mp.dps = 15` -- mpmath's DEFAULT, which `_precision`'s own
    docstring warns about in as many words: "IMPORTING THIS MODULE DOES NOT
    SET mp.dps ... the number reads as measured while carrying ~15 significant
    digits". Neither this file nor `hoefsmit_mpmath` raises it, so a harness
    that forgets `set_compute_dps()` silently benchmarks float64-grade
    arithmetic. The old figures understated the cost.

    THE TEMPTING FIX IS BANNED. Casting `float(c)` makes this exit 0 in
    0.01 s and produce numbers that look entirely plausible. It is exactly
    the shortcut AGENTS.md §"PROBES ARE NOT EXEMPT" was made STRICT to stop,
    and "note it as a limitation and ship" is named there as the wrong move.

    RETRACTED, THEN RE-MEASURED, and the pair is the lesson. This note used to
    say "the float64 character agrees to 15 digits against the 50-dps
    reference, so the word is well conditioned there". BOTH SIDES of that
    comparison were at dps = 15, so the agreement was the FLOOR OF THE
    ARITHMETIC ON BOTH SIDES -- the invalid form AGENTS.md names.

    Redone against a reference that is actually exact (the sparse route below,
    dps = 70, cross-validated against dense mpmath to 7e-71):

        shape          dim    float64 relative error   digits
        (6,6)          132          2.779e-16            15
        (9,1,1,1)      165          4.073e-16            15
        (3,3,3,3)      462          5.715e-17            16
        (8,3,1)        891          2.999e-15            14

    So float64 holds 14-16 digits across a 6.7x range of dim, degrading mildly.
    Extrapolating that trend to dim = 4158 suggests ~13, but it was NOT
    measured there.

    The point worth keeping: the retracted claim was APPROXIMATELY RIGHT and
    entirely UNSUPPORTED. Being close to the truth is not the same as having
    evidence for it, and the fix is to get the evidence rather than to keep the
    guess. Note also what this does and does not license -- it says the
    CHARACTER PRODUCT is well conditioned; it says nothing about the probe's
    verdict, which also depends on the y_lambda weights and the ratios built
    from them, and AGENTS.md's rule is about carriage through the whole
    analysis, not one number.

    THE FIX IS BUILT (bean `qou-fmoi`), and this function now routes to it:
    `hoefsmit_mpmath.chi_lambda_of_word_sparse_mp`. Neither cast nor dense-mpmath: the
    seminormal `sigma_i` carry at most 2 nonzeros per row, so the trace can be
    taken by propagating ONE ROW AT A TIME through the 47 factors, never
    materialising the product. Cost falls from `dim^3 * len(word)` to
    `dim^2 * len(word) * nnz_per_row`. Validated at dim=132, dps=70, against
    the dense routine:

        dense   20.472734309881028753   ~80 s
        sparse  20.472734309881028753    ~1 s      (80-85x over two runs)
        relative difference  7.077e-71  -- exact agreement at the working
                                           precision, NOT a float64 floor

    THE VALUE ABOVE IS AT THE CANONICAL 50-DIGIT q. An earlier version of this
    note quoted 20.472734309881024467, which came from `mpf(str(q_parameter.Q))`
    -- and `q_parameter.Q` is a Python FLOAT, so that pins the substrate to 16
    digits. The dense-vs-sparse agreement was unaffected (same q on both sides),
    but the character itself was a float64-q character, differing from the
    probe's at ~1e-16 for a reason having nothing to do with either routine.

        extrapolated, all ten irreps:  ~36 min (nnz/row = 1, as at dim=132)
                                       ~73 min (nnz/row = 2, the 2x2 blocks
                                                that larger irreps carry)

    So the A=4 [1^4] object is roughly an hour of exact compute, not 1135
    hours. Cross-checked against the dense routine by
    `computations/hoefsmit_sparse_character_test.py`.

    NOTE the matrices come from `seminormal_matrices_mp`, NOT from
    `hecke_characters.build_seminormal_matrices` -- the latter is the float64
    builder whose `BlockCache` uses `math.sqrt` against a 1e-15 degeneracy
    threshold, so feeding its output to an exact character routine would carry
    float64 blocks through an exact product and advertise a precision the
    numbers do not have.
    """
    sig, dim, _ = seminormal_matrices_mp(tuple(lam), cache=_BLOCK_CACHE_MP)
    if dim == 0:
        return mp.mpf(0)
    return chi_lambda_of_word_sparse_mp(sig, dim, word, n_gens)


# ── the row-count prune ────────────────────────────────────────────────
#
# `y_lambda_wenzl_bridge_numeric` is the SU(2) Wenzl weight, and the quantum
# dimension of a partition with more than N rows vanishes in SU(N). At N=2
# that means y_lambda is EXACTLY zero -- `y == 0` is True, not merely small --
# for every lambda with three or more rows.
#
# MEASURED on e_4[h_3], the ten partitions of 12 that carry the A=4 [1^4]
# object: NINE have >= 3 rows and weight exactly 0. The whole projected trace
# is carried by (6,6), the ONLY two-row partition, at dim=132.
#
#     (5,3,3,1) f=4158   (6,4,2) f=2673   (7,3,1,1) f=2376   (6,3,3) f=1650
#     (5,5,1,1) f=1485   (7,4,1) f=1408   (8,3,1)   f= 891   (3,3,3,3) f=462
#     (9,1,1,1) f= 165   -- all y_lambda = 0
#     (6,6)     f= 132   -- y_lambda = 0.00022872963188107212307
#
# So computing chi_lambda for the nine is multiplying an expensive number by
# zero. Checking `y` FIRST turns this probe from ~an hour into seconds, and it
# is not an optimisation detail -- it is the structural fact that the [1^4]
# channel at this weight is a ONE-TERM sum. AGENTS.md's formalize-first probe
# discipline is exactly this: ask whether a structural claim prunes the class
# before running the wide search. Recorded in bean `qou-fmoi`.
# ── anchor identification ──────────────────────────────────────────────
_PROTON_Q0 = "1.1099785827513808"    # experimental / Physical-Observations pin
_MUON_Q0 = "1.1099785955573347"      # ideal CAL-2 pin


def _anchor_of(q_val) -> str:
    """Name the pin `q_val` actually is, or refuse.

    The two pins agree to 8 digits and differ only past the 9th, so this
    compares a 16-digit prefix -- enough to separate them, loose enough to
    survive a re-derivation that moves the last recorded digits.

    Refusing beats guessing: a witness whose `q0Anchor` disagrees with its
    `q0Value` is worse than one with no anchor at all, because
    `q0_anchor_consistency_audit` scores the first as a FLIP and the second
    as a benign MISSING.
    """
    head = mp.nstr(q_val, 17, strip_zeros=False)[:18]
    for name, ref in (("proton", _PROTON_Q0), ("muon", _MUON_Q0)):
        if head.startswith(ref[:17]):
            return name
    raise ValueError(
        f"q0 = {mp.nstr(q_val, 20)} matches neither the proton pin "
        f"({_PROTON_Q0}...) nor the muon pin ({_MUON_Q0}...). Refusing to "
        f"stamp an anchor that would not describe the value.")


def _weight_is_zero(lam) -> bool:
    """True when the SU(2) Wenzl weight vanishes identically for `lam`."""
    return len(tuple(lam)) > 2


def atom_traces(Z, N, q, *, projected_only=True, verbose=False):
    """Return dict with the full Markov trace tr_M(β_K)=Σ_λ y_λ χ_λ and the
    [1^A]-projected trace T_[1^A]=C(4,A)·Σ_{m_λ≠0} m_λ y_λ χ_λ."""
    A = Z + N
    n = 3 * A
    n_gens = n - 1
    word = m3.atom_braid_word_3A(Z, N)
    mult = schur_multiplicities(A)
    gate = math.comb(4, A)

    proj = mp.mpf(0)
    proj_rows = []
    for lam, mlam in sorted(mult.items(), key=lambda kv: -_fdim(kv[0])):
        y = y_lambda_wenzl_bridge_numeric(list(lam), q, dps=50)
        # Skip the character when the weight is identically zero. Not a
        # tolerance test -- `_weight_is_zero` is the row-count criterion, and
        # the numeric `y` is exactly 0 for those, so the product is 0 whatever
        # chi is. Asserted rather than assumed, so a change in the weight
        # convention (SU(2) -> SU(N)) fails loudly instead of silently pruning
        # terms that now contribute.
        if _weight_is_zero(lam):
            assert y == 0, (
                f"{tuple(lam)} has {len(tuple(lam))} rows so the SU(2) Wenzl "
                f"weight should vanish, but y = {mp.nstr(y, 12)}. The weight "
                f"convention changed; the row-count prune is no longer valid.")
            chi = None
            contrib = mp.mpf(0)
        else:
            chi = _chi(lam, word, n_gens)
            contrib = mlam * y * chi
        proj += contrib
        proj_rows.append({"lam": lam, "m": mlam, "f": _fdim(lam),
                          "y": y, "chi": chi, "contrib": contrib})
        if verbose:
            print(f"    {str(lam):>20} m={mlam} f={_fdim(lam):>5} "
                  f"y={mp.nstr(y,6):>12} "
                  f"chi={'(skipped: y=0)' if chi is None else mp.nstr(chi,8):>14} "
                  f"contrib={mp.nstr(contrib,8):>14}")
    T_proj = gate * proj

    full = None
    if not projected_only:
        full = mp.mpf(0)
        for lam in partitions_of(n):
            y = y_lambda_wenzl_bridge_numeric(list(lam), q, dps=50)
            if _weight_is_zero(lam):
                assert y == 0, f"{tuple(lam)}: weight convention changed"
                continue
            full += y * _chi(lam, word, n_gens)

    return {"A": A, "n_strands": n, "gate_C4A": gate,
            "T_proj": T_proj, "proj_sum": proj, "proj_rows": proj_rows,
            "full_trM": full, "n_surviving": len(mult)}


def nucleon_H3_trace(nucleon, q):
    """tr_M^3(β_nucleon) = Σ_{λ⊢3} y_λ χ_λ(intra-word) — for the multiplicativity
    cross-check of the full 12-strand trace."""
    Z, N = (1, 0) if nucleon == "p" else (0, 1)
    word = m3.atom_braid_word_3A(Z, N, include_inter=False)
    tot = mp.mpf(0)
    for lam in partitions_of(3):
        y = y_lambda_wenzl_bridge_numeric(list(lam), q, dps=50)
        chi = _chi(lam, word, 2)
        tot += y * chi
    return tot


# ══════════════════════════════════════════════════════════════════════
# §3  Main
# ══════════════════════════════════════════════════════════════════════
def main() -> int:
    q = mp.mpf(Q_50_DIGIT_STR)
    # MISLABEL FIXED. This read "(canonical muon-q0 literal)" while printing
    # 1.1099785827513808..., which is the PROTON pin; the muon pin is
    # 1.1099785955573347... The VALUE was right -- `Q_50_DIGIT_STR` is
    # proton-pinned and proton is the standing default for all compute (owner
    # directive 2026-08-07) -- so nothing computed here was ever wrong. Only
    # the name was, which is the exact hazard AGENTS.md flags: "most survivors
    # compute the RIGHT value under the WRONG name". It matters because the
    # label is what a reader carries away, and calling a proton-pinned run
    # "muon" is a layer misattribution of the kind the mu-p straddle rules
    # exist to prevent. The two pins agree to 8 digits, so they can only be
    # told apart past the 9th -- never by eye.
    print(f"q0 = {mp.nstr(q,14)}  (canonical PROTON-q0 literal, "
          f"q_parameter.Q_50_DIGIT_STR)\n")

    # ── plethysm structure report (A=2,4 only; A=6 is gated to 0 by C(4,6),
    #    so its full Schur expansion is not needed for the verdict) ──
    for A in (2, 4):
        mult = schur_multiplicities(A)
        dimchk = sum(m * _fdim(l) for l, m in mult.items())
        induced = math.factorial(3 * A) // ((6 ** A) * math.factorial(A))
        print(f"e_{A}[h_3]: {len(mult)} partitions of {3*A}, "
              f"Σ m_λ f^λ = {dimchk} (= (3A)!/(6^A A!) = {induced})  "
              f"C(4,{A}) gate = {math.comb(4, A)}")
    print(f"e_6[h_3]: nonzero symmetric function of degree 18 (has ≤4-row "
          f"partitions); C(4,6) gate = {math.comb(4, 6)} ⟹ T_[1^6] ≡ 0.")
    print()

    # ── A=4 genuine projected trace (with full-trace cross-check) ──
    print("── ⁴He (A=4, 12-strand) — genuine [1^4]-projected Markov trace ──")
    he4 = atom_traces(2, 2, q, projected_only=False, verbose=True)
    print(f"  full tr_M(β_⁴He)  = {mp.nstr(he4['full_trM'],12)}")
    print(f"  Σ_λ m_λ y_λ χ_λ    = {mp.nstr(he4['proj_sum'],12)}")
    print(f"  T_[1^4]=C(4,4)·Σ  = {mp.nstr(he4['T_proj'],12)}  (gate={he4['gate_C4A']})")
    frac4 = he4["proj_sum"] / he4["full_trM"]
    print(f"  T_[1^4]/full       = {mp.nstr(frac4,10)}")

    # multiplicativity cross-check of the full 12-strand trace
    tp = nucleon_H3_trace("p", q)
    tn = nucleon_H3_trace("n", q)
    from closed_form_tau_M import closed_form_ratio
    iface = closed_form_ratio(2, 2, q)
    cf = (tp ** 2) * (tn ** 2) * iface
    print(f"  cross-check closed_form tr_M = tr_p²·tr_n²·∏f = {mp.nstr(cf,12)}")
    print(f"    (H12 direct − closed-form) rel = "
          f"{mp.nstr(abs(he4['full_trM']-cf)/abs(cf),4)}")

    # ── A=2 deuteron [1^2] projected (pairwise unit) ──
    print("\n── D (A=2, 6-strand) — [1^2]-projected pairwise unit ──")
    d = atom_traces(1, 1, q, projected_only=False, verbose=True)
    print(f"  full tr_M(β_D)     = {mp.nstr(d['full_trM'],12)}")
    print(f"  T_[1^2]=C(4,2)·Σ  = {mp.nstr(d['T_proj'],12)}  (gate={d['gate_C4A']})")
    fracD = d["proj_sum"] / d["full_trM"]

    # ── A=6 gated to zero ──
    li6_gate = math.comb(4, 6)
    print(f"\n── ⁶Li (A=6, 18-strand) — SU(4) gate C(4,6) = {li6_gate} ──")
    print(f"  T_[1^6] = C(4,6)·Σ = 0 EXACTLY (α-shell-closure locality; "
          f"the internal plethysm e_6[h_3] is itself non-zero, so the "
          f"vanishing is the PROVED flavour gate, not the trace).")

    # ══════════════════════════════════════════════════════════════════
    # §4  Honest enhancement metrics vs the measured ×2.093
    # ══════════════════════════════════════════════════════════════════
    need = mp.mpf("2.0925")   # measured super-pairwise excess (PROBE 2 table)
    print("\n── enhancement metrics vs measured super-pairwise ×2.093 ──")
    # Every metric below is a y_λ-normalised (scale-free at the level of a
    # single trace) ratio; the QUESTION is whether ANY is a *canonical*
    # (no free denominator) super-pairwise factor equal to 2.093.
    #
    # (m1) connected 4-body per pair, in units of the connected 2-body:
    #      |T_[1^4](⁴He)| / (n_pairs(4) · |T_[1^2](D)|),  n_pairs(4)=C(4,2)=6
    m1 = abs(he4["T_proj"]) / (6 * abs(d["T_proj"]))
    # (m2) connected 4-body vs connected 2-body directly (no pair count):
    m2 = abs(he4["T_proj"]) / abs(d["T_proj"])
    # (m3) super-pairwise lift on the full-trace fraction, PROBE-2 shape
    #      1 + |T_[1^4]|/|pairwise scale|, pairwise scale = (A-1)·|T_[1^2](D)|
    m3v = 1 + abs(he4["T_proj"]) / (3 * abs(d["T_proj"]))
    # (m4) fraction of the ⁴He trace in the [1^4] channel, relative to the
    #      D trace fraction in the [1^2] channel (dimensionless of dimensionless)
    m4 = frac4 / fracD
    for name, val, note in [
        ("m1  |T4|/(6|T2|)", m1, "connected-4b per pair / connected-2b"),
        ("m2  |T4|/|T2|", m2, "connected-4b / connected-2b (no pair count)"),
        ("m3  1+|T4|/(3|T2|)", m3v, "PROBE-2-shape lift over pairwise scale"),
        ("m4  frac4/fracD", m4, "channel-fraction ratio ⁴He:[1^4] vs D:[1^2]"),
    ]:
        # mpf / mpf -- `need` is mp.mpf("2.0925") and the metrics are mpf, so
        # the ratio stays exact. float() below is DISPLAY ONLY.
        r = val / need
        print(f"  {name:>22} = {float(val):8.4f}   "
              f"ratio/2.093 = {float(r):6.3f}   {note}")

    # ── verdict ──
    # These four ratios ARE the verdict -- `within5` and `order` below are
    # thresholded on them, and the witness stores them. They were built with
    # float(m)/float(need), which is arithmetic rather than display and is the
    # case AGENTS.md calls out: a probe's float64 corrupts the ANALYSIS, which
    # is the expensive kind of wrong. Both operands are mpf, so keep them mpf
    # and convert at the serialization boundary with `fmt`.
    ratios = {"m1": m1 / need, "m2": m2 / need,
              "m3": m3v / need, "m4": m4 / need}
    within5 = [k for k, r in ratios.items() if abs(r - 1) < 0.05]
    order = [k for k, r in ratios.items() if 0.5 < r < 2.0]
    verdict = ("CLOSES" if within5 and len(within5) >= 1 and
               # only CLOSES if a metric with NO free denominator matches;
               # all four carry a denominator convention → never auto-CLOSES
               False else
               "PARTIAL" if order else "DOES-NOT")
    print(f"\n  VERDICT: {verdict}")
    print(f"    within-5%-of-2.093 metrics: {within5 or 'none'}")
    print(f"    right-order (0.5–2×) metrics: {order or 'none'}")
    print("    NOTE: every metric carries a denominator convention (pair count,"
          " pairwise-scale definition) — a Rule-14 hidden DOF. No metric is a"
          " canonical no-free-parameter super-pairwise factor, so a within-5%"
          " hit is a units-mismatched near-match and must NOT be wired"
          " (same trap PROBE 2 flagged).")

    # ── witness ──
    import json
    import datetime
    witness = {
        "engine": "mpmath+numpy", "engineVersion": "mpmath50dps/f64-chi",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "computation": "su4-1111-markov-trace",
        "scriptFile": "su4_1111_markov_trace_probe.py",
        "description": (
            "PROBE 2b: GENUINE Schur-Weyl [1^4]-flavour-projected 3A-strand "
            "Markov trace. e_A[h_3] antisymmetric SU(4) plethysm (exact "
            "power-sum + Murnaghan-Nakayama) → Schur mult m_λ, y_λ-normalised "
            "(Wenzl bridge) sum of exact Hoefsmit characters χ_λ(β_atom), gated "
            "by C(4,A). Replaces the PROBE-2 Mayer-cluster stand-in. Audit-only, "
            "no fit, single canonical operator."),
        # AGENTS.md §4: "any new witness must record its q0 so a later reader
        # can tell which layer it belongs to without inferring it from a call
        # site." Q_50_DIGIT_STR is the PROTON pin (1.1099785827513808...), the
        # standing default for all compute; the muon pin is
        # 1.1099785955573347... and the two agree to 8 digits, so they cannot
        # be told apart by eye.
        #
        # TOP LEVEL, not inside "data". `q0_anchor_consistency_audit.py:134`
        # reads `body.get("q0Anchor")`, so an anchor nested one level down is
        # invisible to the checker while looking perfectly present to a human
        # -- which is how I first wrote it, and the audit is what caught it:
        # Q0_ANCHOR_MISSING went UP after I "added" the anchor.
        #
        # DERIVED from the value, not hardcoded. `qou-wee5` (8cdcf3865a8)
        # measured that the shim rebinds its whole derived q family to MUON
        # when the running process's argv stem is manifest-listed -- so the
        # same import can yield a different pin depending on who `__main__`
        # is. Measured for this probe: running it as `__main__` gives the
        # proton pin, so a hardcoded "proton" happens to be true today. It
        # would become a silent lie the moment this producer were added to
        # that manifest, and the witness would then claim an anchor it does
        # not have -- the straddle AGENTS.md forbids. `_anchor_of` reads the
        # value instead, and refuses rather than guessing.
        "q0Anchor": _anchor_of(q),
        "q0Value": str(q),
        "tier": "structural (exact plethysm + Wenzl y_λ + Hoefsmit χ_λ, all exact)",
        # Was "chi=f64 (magnitude verdict)". No longer true: chi now comes from
        # `hoefsmit_mpmath.chi_lambda_of_word_sparse_mp` in exact mpmath at the
        # module dps, via `seminormal_matrices_mp`. Leaving the old string
        # would have UNDERSTATED the witness's own precision -- the mirror of
        # the usual defect, but a mislabel either way.
        "precision": ("chi=mpfr_exact (sparse trace-only, cross-checked vs "
                      "dense at 7e-71); y_lambda=mpfr_50dps; "
                      "plethysm=exact rational"),
        "data": {
            "q0": str(q),
            "plethysm_A4_partitions": {str(l): m for l, m in
                                       schur_multiplicities(4).items()},
            "he4": {
                "full_trM": str(he4["full_trM"]),
                "proj_sum": str(he4["proj_sum"]),
                "T_1111": str(he4["T_proj"]),
                "gate_C44": he4["gate_C4A"],
                "T_over_full": str(frac4),
                "closed_form_trM": str(cf),
                "closed_form_rel_err": str(abs(he4["full_trM"] - cf) / abs(cf)),
                "per_partition": [
                    {"lambda": list(r["lam"]), "m": r["m"], "f": r["f"],
                     "y_lambda": str(r["y"]),
                     # chi comes from _chi(), which ends in
                     # mp.mpf(m3.chi_lambda_of_word(...)) — the f64
                     # seminormal kernel — so str(<mpf>) would print
                     # 50 dps of a 53-bit value.
                     "chi": str_at_true_precision(r["chi"]),
                     "contrib": str(r["contrib"])} for r in he4["proj_rows"]],
            },
            "deuteron": {
                "full_trM": str(d["full_trM"]),
                "T_11": str(d["T_proj"]), "gate_C42": d["gate_C4A"],
                "T_over_full": str(fracD)},
            "li6": {"gate_C46": li6_gate, "T_1111111": "0 (exact via gate)"},
            "enhancement_metrics": {k: fmt(v) for k, v in ratios.items()},
            "needed_super_pairwise": fmt(need),
            "verdict": verdict,
            "verdict_note": (
                "PARTIAL / scope-(a): the genuine e_A[h_3]-plethysm [1^4]-"
                "projected trace is right-KIND (categorical antisymmetric "
                "supermultiplet, not the pairwise-derived Mayer cluster) and "
                "right-LOCALITY (A=6 → 0 EXACTLY via the proved C(4,6)=0 gate; "
                "the internal plethysm e_6[h_3] is itself non-zero). It does NOT "
                "close the magnitude parameter-free: every enhancement metric vs "
                "2.093 carries a denominator convention (pair count / pairwise-"
                "scale) — a Rule-14 hidden DOF — so a within-5% hit is a units-"
                "mismatched near-match and must NOT be wired. Constrains the "
                "magnitude and confirms the ingredient KIND; does NOT exclude it."),
        },
        "assertions": [
            {"name": "plethysm_dimcheck_A4",
             "computed": str(sum(m * _fdim(l) for l, m in
                                 schur_multiplicities(4).items())),
             "expected": "15400", "passed":
             sum(m * _fdim(l) for l, m in schur_multiplicities(4).items()) == 15400},
            {"name": "a6_vanishes_via_gate", "computed": str(li6_gate),
             "expected": "0", "passed": li6_gate == 0},
            {"name": "full_trace_multiplicativity_crosscheck",
             "computed": str(float(abs(he4["full_trM"] - cf) / abs(cf))),
             "expected": "<1e-6",
             "passed": bool(abs(he4["full_trM"] - cf) / abs(cf) < mp.mpf("1e-6"))},
        ],
        "auditOnly": True,
        "context": {
            "axis": "GAP-A-4 class-D — A=4 [1^4] supermultiplet (Δ_λ magnitude leg)",
            "gate_lean": "qou:QOU.MassTheory.SU4SupermultipletGate",
            "supersedes_standin": "probes/su4-connected-1111-magnitude.witness.json",
            "scoping": "docs/scope/2026-07-05-gap-a4-interface-operator-attack-scoping.md §3",
        },
    }
    witness["allPassed"] = all(a["passed"] for a in witness["assertions"])
    out = _HERE / "su4-1111-markov-trace.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str), encoding="utf-8")
    print(f"\n  Witness: {out.name}  (allPassed={witness['allPassed']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
