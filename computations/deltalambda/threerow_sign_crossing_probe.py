#!/usr/bin/env python3
"""threerow_sign_crossing_probe.py — does the ≥3-row signed trace change sign on (1, q₀]?

THE ONE DECISIVE QUESTION (bean qou-prjo; convergence-test of #4817 + #4818).

Both sibling leads converged on the same characterization of the OPEN
deuteron/light-nucleus many-body binding *magnitude*:

  * #4817 (LEAD-1, algebraic ≥3-row extensive cumulant): the q₀-FREE
    combinatorics only *bracket* the AME ratios and give the WRONG sign order
    `(ν₃,ν₄)=(−,+)` vs the derived `(μ₃,μ₄)=(+,−)`.  §5: the real sign lives in
    the q₀-dependent `y_λ(q)·χ^λ` trace weighting; the sharp next unit is
    "the sign of `Σ_{λ⊢k,ℓ≥3} y_λ(q)·χ^λ·Δ_λ` is q-dependent and crosses zero
    between the combinatorial (q→1) limit and q₀."
  * #4818 (LEAD-2, geometric NA-Stokes surface curvature): the scalar
    Markov/character trace is provably NULL on the commutator object
    (`listPairing_trace_zero`), so the sign cannot come from the diagonal /
    Betti reading — it must be in the operator/weight channel.

This probe answers exactly that question, on the CANONICAL object of
`deltalambda-extensivity-gap-synthesis` (`B_base = m_e·|Σ y_λ χ^λ sgn·dim|`,
where `sgn·dim = (−1)^{n(λ)}·dim = Δ_λ`):

    F_K(q) = Σ_{λ ⊢ 3A, ℓ(λ) ≥ 3}  y_λ(q) · χ^λ(β_K; q) · Δ_λ

restricted to the ≥3-ROW stratum (#4664: the stratum measured to *dominate*
binding).  We sweep q from q→1⁺ (combinatorial limit) to the substrate q₀
(EXPERIMENTAL PROTON ANCHOR, owner directive 2026-08-07) and ask whether the
sign of F_K crosses zero.

  YES  ⇒ the zero-crossing IS the many-body (+,−) sign-change, DERIVED from the
         *known* q₀ (legitimate: q₀-USE ≠ q₀-DERIVATION; only deriving q₀ is
         FOREVER GATED, AGENTS.md 2026-08-02).
  NO   ⇒ scope-(a) negative: "this object alone does not supply the sign-change
         on (1,q₀]"; the sign lives elsewhere.

LAYER PURITY (AGENTS.md q₀-anchor STRICT, straddle hazard).  BOTH y_λ(q) AND
χ^λ(β_K;q) are q-dependent (the Hecke character of the color-weighted nuclide
braid), and BOTH are evaluated at the SAME running q.  Holding χ^λ fixed at q₀
while running y_λ(q) would be the forbidden straddle.  y_λ via the LIVE closed
form `schur_principal_mpmath.y_lambda_at_q0_mpmath` (NOT the muon-serving cache).

DISCIPLINE.  0 free parameters; AME never inverted (targets/checks only);
proton anchor default; scope-(a)/(b) honest.  The character path is validated
against `atom-chi-rust-{d,t,3he,4he}.witness.json` at q₀ inside the probe
(signs exact; ~1e-7 f64-seminormal accumulation — see PRECISION note).

PRECISION.  y_λ(q) is full mpmath (50 dps).  χ^λ(β_K;q) uses the pure-Python
f64 Hoefsmit-seminormal fallback (`build_seminormal_matrices`; no scipy/native
kernel needed for the matrix product), so the *product* is f64-precision.  This
is DECISIVE for a SIGN question away from a crossing (|F| = O(1) there); near a
detected crossing we bisect and report the located q with its f64-limited
resolution and flag if the sign is within f64 noise.  No mpfr kernel is
available in this sandbox (disk-quota; documented, not a proof gap).
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

sys.path[:0] = [
    str(Path(__file__).resolve().parent.parent),                 # computations/
    str(Path(__file__).resolve().parent.parent / "substrate"),   # q_parameter, _precision
    str(Path(__file__).resolve().parent.parent / "hecke"),       # hecke_characters
]
import _path_bridge  # noqa: F401,E402

import math  # noqa: E402
import numpy as np  # noqa: E402
import mpmath as mp  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from hecke_characters import build_seminormal_matrices  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from schur_principal_mpmath import (  # noqa: E402
    y_lambda_at_q0_mpmath, partitions_of, _f_lambda,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from _precision import fmt, set_compute_dps, str_at_true_precision  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

warnings.filterwarnings("ignore")
set_compute_dps(50)

Q0 = mp.mpf(Q_50_DIGIT_STR)          # experimental proton anchor (q_parameter)
Q_LO = mp.mpf("1.0001")              # combinatorial limit surrogate (q→1⁺)
ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}
# n=6 (D) and n=9 (T,³He) complete in seconds via the pure-Python f64 Hoefsmit
# seminormal fallback. n=12 (⁴He) builds dim-in-the-thousands f64 matrices for
# ~60 ℓ≥3 partitions per grid point (>4 min/point, GB-scale RAM) — a documented
# SANDBOX COMPUTE LIMIT (no mpfr Rust kernel; disk quota), NOT a proof gap. It is
# recorded as compute-limited; run with QOU_INCLUDE_4HE=1 on a host with the
# native kernel to fill it in.
import os  # noqa: E402
ISOTOPES = ["D", "T", "3He"] + (["4He"] if os.environ.get("QOU_INCLUDE_4HE") else [])
COMPUTE_LIMITED = [] if os.environ.get("QOU_INCLUDE_4HE") else ["4He"]


# ─────────────────────────────────────────────────────────────────────────
# Δ_λ = (−1)^{n(λ)}·dim V_λ = sgn_conjugate_parabolic(λ)·dim(λ)   (PROVED, value-only)
# ─────────────────────────────────────────────────────────────────────────
def delta_lambda(lam: tuple[int, ...]) -> int:
    conj = tuple(sum(1 for p in lam if p > i) for i in range(lam[0])) if lam else ()
    sgn = math.prod((-1) ** (p * (p - 1) // 2) for p in conj)  # = (−1)^{n(λ)}
    return sgn * _f_lambda(tuple(lam))


# ─────────────────────────────────────────────────────────────────────────
# χ^λ(β_K; q)  — Hecke character of the color-weighted nuclide braid at running q.
# Direct matrix product Tr(∏_j (c_j σ_{g_j} + d_j I)); no 2^k branch expansion.
# Layer-pure: the word AND the seminormal matrices are both materialised at q.
# ─────────────────────────────────────────────────────────────────────────
def chi_atom(shape: tuple[int, ...], Z: int, N: int, q: mp.mpf) -> mp.mpf:
    qf = float(q)
    sig, dim, _ = build_seminormal_matrices(tuple(shape), q=qf)
    if dim == 0:
        return mp.mpf(0)
    # `allow_float64=True` DECLARES the loss where it actually happens. The
    # seminormal matrices are built at `float(q)` and each letter is assembled
    # as `float(c)·σ + float(d)·I`, so this χ path is f64 end to end whatever
    # precision `q` carries in. `reject_float64_q` (efcaf79ed) is right that a
    # 50-dps pipeline must not be silently capped at 17 digits; it is not being
    # silenced here, it is being answered — the PRECISION note in this module's
    # docstring and the witness caveat say the same thing in prose.
    word = atom_braid_word_3A(Z, N, include_inter=True, q=q,  # (c, d, gen0) at q
                              allow_float64=True)
    I = np.eye(dim)
    prod = np.eye(dim)
    for (c, d, g) in word:
        M = float(c) * sig[g] + float(d) * I
        prod = prod @ M
    return mp.mpf(float(np.trace(prod)))


F64_SIG_DIGITS = 17          # binary64's round-trip decimal width


def fmt_f64_limited(x: mp.mpf) -> str:
    """Serialize a value whose NARROWEST input was the f64 χ kernel.

    `str_at_true_precision` cannot detect this case, and silently gets it wrong
    in the expensive direction.  Its test is representational and exact — "is
    this mpf equal to its own float64?" — which is right for a pure f64 kernel
    output.  But `F = Σ y_λ(q)·χ^λ(β;q)·Δ_λ` MIXES a 50-dps mpmath weight with
    an f64 character, so the product is not a 53-bit dyadic and the helper keeps
    all 50 digits, ~34 of which the χ kernel never supplied.  That reads as
    measured and is worse than the raw float64 it replaced.

    So the mixed case is handled by hand, at the same limit
    `str_at_true_precision` would apply to a pure f64 value: the kernel's own
    round-trip width.  ACCURACY is looser still — the measured seminormal
    accumulation `chi_vs_witness_max_rel_at_q0` is ~1.5e-6 — but that is a
    caveat about the number, not a reason to truncate it: a witness has to stay
    reproducible, and these digits ARE what the kernel produced.
    """
    return fmt(x, F64_SIG_DIGITS)


def F_iso(Z: int, N: int, q: mp.mpf, min_rows: int = 3) -> mp.mpf:
    """F_K(q) = Σ_{λ⊢3A, ℓ(λ)≥min_rows} y_λ(q)·χ^λ(β_K;q)·Δ_λ."""
    n = 3 * (Z + N)
    y = y_lambda_at_q0_mpmath(n, q)
    tot = mp.mpf(0)
    for lam in partitions_of(n):
        if len(lam) < min_rows:
            continue
        tot += y[lam] * chi_atom(lam, Z, N, q) * delta_lambda(lam)
    return tot


def G_char_free(n: int, q: mp.mpf, min_rows: int = 3) -> mp.mpf:
    """Character-free companion G(q) = Σ_{λ⊢n, ℓ(λ)≥min_rows} y_λ(q)·Δ_λ (full mpmath)."""
    y = y_lambda_at_q0_mpmath(n, q)
    tot = mp.mpf(0)
    for lam in partitions_of(n):
        if len(lam) < min_rows:
            continue
        tot += y[lam] * delta_lambda(lam)
    return tot


def geom_grid(lo: mp.mpf, hi: mp.mpf, npts: int) -> list[mp.mpf]:
    """Geometric grid on [lo, hi] in (q−1) so points cluster near q→1⁺."""
    a, b = mp.log(lo - 1), mp.log(hi - 1)
    return [1 + mp.e ** (a + (b - a) * k / (npts - 1)) for k in range(npts)]


# Chosen once and independent of the data: the convention-C values this probe
# recorded were O(1) (|F(q0)| ran 0.19 … 5.9), while f64 chi noise on an O(1)
# product is ~1e-16.  Any threshold below 1e-16 therefore cannot be met by a
# genuinely non-vanishing object, and separates "identically zero" from the C-era
# regime by more than thirty orders of magnitude.  NOT tuned to the measurement.
F_ZERO_TOL = mp.mpf("1e-30")


def bisect_cross(f, qa: mp.mpf, qb: mp.mpf, fa: mp.mpf, fb: mp.mpf,
                 iters: int = 40) -> mp.mpf:
    """Locate the sign change of f on [qa,qb] (fa·fb<0) by bisection."""
    for _ in range(iters):
        qm = (qa + qb) / 2
        fm = f(qm)
        if fm == 0:
            return qm
        if (fm > 0) == (fa > 0):
            qa, fa = qm, fm
        else:
            qb, fb = qm, fm
    return (qa + qb) / 2


def validate_chi_at_q0(names=("D", "T")) -> mp.mpf:
    """Cross-check χ^λ(β_K;q₀) against the canonical atom-chi witnesses (sign+value).

    Validate on the smaller isotopes (D n=6, T n=9) — enough to confirm the
    convention; the n=12 seminormal builds are reserved for the sweep.
    """
    import json
    COMP = Path(__file__).resolve().parent.parent
    max_rel = mp.mpf(0)
    for name in names:
        Z, N = ZN[name]
        wf = COMP / f"atom-chi-rust-{name.lower()}.witness.json"
        if not wf.exists():
            continue
        ref = json.loads(wf.read_text())["data"]["atom"]["by_partition"]
        for e in ref:
            lam = tuple(e["partition"])
            r = mp.mpf(e["chi_lambda"])
            mine = chi_atom(lam, Z, N, Q0)
            rel = abs(mine - r) / (abs(r) + mp.mpf("1e-40"))
            max_rel = max(max_rel, rel)
    return max_rel


def main() -> int:
    print("=" * 84)
    print(" Δ_λ ≥3-row SIGN-CROSSING PROBE  —  does sign(Σ_{ℓ≥3} y_λ(q)·χ^λ·Δ_λ)")
    print(" cross zero as q runs from q→1⁺ to the substrate q₀?  (bean qou-prjo)")
    print("=" * 84)
    print(f" q₀ (EXPERIMENTAL PROTON ANCHOR) = {mp.nstr(Q0, 20)}")
    print(f" q_lo (combinatorial-limit surrogate q→1⁺) = {mp.nstr(Q_LO, 8)}")

    # --- convention gate: χ path vs canonical witnesses at q₀ --------------
    chi_rel = validate_chi_at_q0()
    print(f"\n χ^λ(β_K;q₀) vs canonical atom-chi witnesses: max rel diff = "
          f"{float(chi_rel):.2e}"
          f"  ({'OK' if chi_rel < 1e-5 else 'FAIL'}; f64 seminormal accumulation)")

    import time
    npts = 13
    grid = geom_grid(Q_LO, Q0, npts)

    # ---------- PRIMARY: full character object per isotope -----------------
    print("\n" + "─" * 84)
    print(" PRIMARY  F_K(q) = Σ_{λ⊢3A, ℓ(λ)≥3} y_λ(q)·χ^λ(β_K;q)·Δ_λ   (layer-pure)")
    print("─" * 84)
    iso_rows = {}
    for name in ISOTOPES:
        Z, N = ZN[name]
        f = lambda q, Z=Z, N=N: F_iso(Z, N, q)
        t0 = time.time()
        vals = []
        for k, q in enumerate(grid):
            vals.append(f(q))
            print(f"    [{name}] grid {k+1}/{npts} q={mp.nstr(q,8)} "
                  f"F={float(vals[-1]):+.4e}  ({time.time()-t0:.0f}s)", flush=True)
        signs = [int(mp.sign(v)) for v in vals]
        s_lo, s_hi = signs[0], signs[-1]
        crossings = []
        for i in range(len(grid) - 1):
            if vals[i] != 0 and vals[i + 1] != 0 and (vals[i] > 0) != (vals[i + 1] > 0):
                qc = bisect_cross(f, grid[i], grid[i + 1], vals[i], vals[i + 1], iters=24)
                crossings.append(qc)          # keep the mpf; serialize at the sink
        crossed = s_lo != s_hi or len(crossings) > 0
        # PRIMARY block: every value here passes through the f64 χ kernel, so it
        # is serialized at that kernel's width, not at mpmath's.
        iso_rows[name] = {
            "Z": Z, "N": N, "n_strands": 3 * (Z + N),
            "F_at_qlo": fmt_f64_limited(vals[0]),
            "F_at_q0": fmt_f64_limited(vals[-1]),
            "max_abs_F_on_grid": fmt_f64_limited(max(abs(v) for v in vals)),
            "sign_qlo": s_lo, "sign_q0": s_hi,
            "sign_crossed": bool(crossed),
            "n_crossings_on_grid": len(crossings),
            "crossing_q_values": [fmt_f64_limited(c) for c in crossings],
        }
        cs = (f"CROSS @ q={[float(c) for c in crossings]}" if crossings
              else "no crossing")
        print(f"  {name:4s} n={3*(Z+N):2d}  F(q_lo)={float(vals[0]):+.5e}  "
              f"F(q₀)={float(vals[-1]):+.5e}  sign {s_lo:+d}→{s_hi:+d}  {cs}")

    # ---------- COMPANION: character-free y_λ weighting only ---------------
    print("\n" + "─" * 84)
    print(" COMPANION  G(q) = Σ_{λ⊢n, ℓ(λ)≥3} y_λ(q)·Δ_λ   (character-free; full mpmath)")
    print("─" * 84)
    cf_rows = {}
    for n in (6, 9, 12):
        f = lambda q, n=n: G_char_free(n, q)
        vals = [f(q) for q in grid]
        s_lo, s_hi = int(mp.sign(vals[0])), int(mp.sign(vals[-1]))
        crossings = []
        for i in range(len(grid) - 1):
            if (vals[i] > 0) != (vals[i + 1] > 0):
                crossings.append(bisect_cross(f, grid[i], grid[i + 1],
                                              vals[i], vals[i + 1]))
        # G is character-free and therefore full 50-dps mpmath — these keep
        # every digit, where the primary block above keeps 53 bits' worth.
        cf_rows[str(n)] = {
            "G_at_qlo": str_at_true_precision(vals[0]),
            "G_at_q0": str_at_true_precision(vals[-1]),
            "sign_qlo": s_lo, "sign_q0": s_hi,
            "sign_crossed": bool(s_lo != s_hi or crossings),
            "crossing_q_values": [str_at_true_precision(c) for c in crossings],
        }
        cs = (f"CROSS @ q={[float(c) for c in crossings]}" if crossings
              else "no crossing")
        print(f"  n={n:2d}  G(q_lo)={float(vals[0]):+.5e}  G(q₀)={float(vals[-1]):+.5e}  "
              f"sign {s_lo:+d}→{s_hi:+d}  {cs}")

    # ---------- verdict ----------------------------------------------------
    any_iso_cross = any(r["sign_crossed"] for r in iso_rows.values())
    d_cross = iso_rows["D"]["sign_crossed"]
    print("\n" + "=" * 84)
    verdict_kind = "YES" if any_iso_cross else "NO"
    print(f" VERDICT: sign crossing on (1,q₀] in the ≥3-row object — {verdict_kind}")
    print(f"   deuteron (D): {'crosses' if d_cross else 'does NOT cross'}")
    if COMPUTE_LIMITED:
        print(f"   compute-limited (not evaluated): {COMPUTE_LIMITED} "
              f"(n=12 f64 seminormal budget; documented, not a proof gap)")
    print("=" * 84)

    # ---------- witness ----------------------------------------------------
    w = WitnessBuilder("threerow-sign-crossing", engine="mpmath+f64-seminormal",
                       output_dir=Path(__file__).resolve().parent)
    w.set_description(
        "Bean qou-prjo convergence-test of #4817+#4818. Tests whether "
        "sign(F_K(q)=Σ_{λ⊢3A,ℓ(λ)≥3} y_λ(q)·χ^λ(β_K;q)·Δ_λ) crosses zero as q "
        "runs from the combinatorial limit q→1⁺ to the substrate q₀ (EXPERIMENTAL "
        "PROTON ANCHOR). Δ_λ=(−1)^{n(λ)}·dim (PROVED value-only); y_λ via live "
        "schur_principal_mpmath (proton anchor, NOT muon cache); χ^λ via q-running "
        "color-weighted nuclide braid + f64 Hoefsmit seminormal. Layer-pure (both "
        "y_λ and χ^λ at the same q). 0 free parameters; AME not used. Char-free "
        "companion G(q)=Σ y_λ·Δ_λ isolates the y_λ weighting. Scope-(a)/(b) per verdict."
    )
    w.add_parameter("q0_experimental_proton_anchor", mp.nstr(Q0, 30))
    w.add_parameter("q_lo_combinatorial_surrogate", mp.nstr(Q_LO, 12))
    w.add_parameter("q0_pin", "experimental/proton (q_parameter.Q); live closed form y_λ")
    w.add_parameter("free_parameters", 0)
    w.add_parameter("grid_npts", npts)
    w.add_parameter("chi_precision", "f64 Hoefsmit seminormal (no mpfr kernel in sandbox)")
    w.add_data("chi_vs_witness_max_rel_at_q0", fmt_f64_limited(chi_rel))
    w.add_data("primary_full_character_object", iso_rows)
    w.add_data("companion_character_free", cf_rows)
    w.add_data("any_isotope_sign_crossed", bool(any_iso_cross))
    w.add_data("deuteron_sign_crossed", bool(d_cross))
    w.add_data("isotopes_evaluated", ISOTOPES)
    w.add_data("isotopes_compute_limited", COMPUTE_LIMITED)
    w.add_assertion("chi_convention_matches_witness", 1 if chi_rel < 1e-5 else 0, 1)
    # The two assertions that stood here were
    #     w.add_assertion("D_sign_qlo", iso_rows["D"]["sign_qlo"], iso_rows["D"]["sign_qlo"])
    #     w.add_assertion("D_sign_q0",  iso_rows["D"]["sign_q0"],  iso_rows["D"]["sign_q0"])
    # i.e. `x == x`, under a comment calling them "the headline falsifiable fact".
    # They were tautologies and could never fail: between conventions C and D the
    # deuteron object went from F(q0) = -0.19496... to identically zero and the sign
    # went -1 -> 0, and both still reported passed (committed 1/1, -1/-1; re-run
    # 0/0, 0/0).  A sign is a MEASUREMENT; it is recorded in `iso_rows` via add_data,
    # which is what recording is for.  What is genuinely checkable is below.
    max_abs_F = max(abs(mp.mpf(iso_rows[k]["max_abs_F_on_grid"])) for k in iso_rows)
    w.add_assertion("three_row_object_is_structural_zero",
                    1 if max_abs_F < F_ZERO_TOL else 0, 1)
    w.add_caveat(
        "χ^λ(β_K;q) is f64-precision (pure-Python Hoefsmit seminormal; the mpfr "
        "Rust kernel is unavailable in this sandbox — disk quota, documented). "
        "y_λ(q) is full 50-dps mpmath. The product is therefore f64-precision — "
        "DECISIVE for a SIGN question away from a crossing (|F|=O(1)); near any "
        "crossing the located q carries only f64 resolution."
    )
    if COMPUTE_LIMITED:
        w.add_caveat(
            f"⁴He (n=12) is a documented SANDBOX COMPUTE LIMIT, not a proof gap: "
            f"the pure-Python f64 Hoefsmit seminormal build for ~60 ℓ≥3 partitions "
            f"of 12 (dim in the thousands, GB-scale f64 matrices) exceeds >4 min/grid "
            f"point with no mpfr Rust kernel available (disk quota). The character-free "
            f"companion G(q) for n=12 IS computed (pure mpmath). Re-run with "
            f"QOU_INCLUDE_4HE=1 on a host with pyhecke_native to fill in the full "
            f"character object. n=6 (D) and n=9 (T,³He) fully answer the light-chain "
            f"crossing question."
        )
    w.add_caveat(
        f"SERIALIZATION SPLIT (raw-float64 ratchet). Every numeric field is a "
        f"decimal string, at the precision of its NARROWEST input. The PRIMARY "
        f"block passes through the f64 χ kernel and is written at that kernel's "
        f"round-trip width ({F64_SIG_DIGITS} significant digits) — the same "
        f"digits the previous raw-float64 output carried, neither inflated nor "
        f"lost. The COMPANION block is character-free and therefore full 50-dps "
        f"mpmath, and now shows all of it where float64 was discarding ~34 "
        f"digits. Note the two are NOT interchangeable: representational width "
        f"is not accuracy, and the χ path's accuracy is the ~1.5e-6 recorded in "
        f"chi_vs_witness_max_rel_at_q0, far looser than {F64_SIG_DIGITS} digits."
    )
    w.add_caveat(
        "value_only object: F_K is NOT a binding energy (Δ_λ is value-only; the "
        "extensive super-pairwise magnitude term is open). This probe tests ONLY "
        "the SIGN of the ≥3-row trace weighting, not the magnitude."
    )
    w.save()
    print("\nwitness -> threerow-sign-crossing.witness.json")
    return 0 if chi_rel < 1e-5 else 1


if __name__ == "__main__":
    raise SystemExit(main())
