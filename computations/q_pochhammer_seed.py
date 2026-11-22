"""
q-Pochhammer denominator zeros as Newton-Raphson seeds for the
Thurston gluing equations.

Computes Φ_n(x; q_0) at several depths n, extracts the n simple roots
of its denominator (x; q_0)_n = ∏_{k=0..n-1}(1 - x q_0^k), and compares
them to the discriminant roots of the color-tube cubic computed by
picard_lefschetz_thimble.py.

Manuscript references:
  - def:q-pochhammer-partial-product
  - conj:shared-denominator-cusp-holonomy
  - `denominator-zeros-as-sw-critical-points`  [no carrier]
  - `pl-jsj-mass-integration-equivalence`          [REMOVED -- see below]
  (The two labels marked [no carrier] were blocks in the removed
   `descartes-universe/` chapter; no file in the tree defines them.
   See bean qou-3kni.)

The witness records:
  - The n algebraic denominator zeros for each tested n
  - The PL discriminant roots from picard_lefschetz_thimble
  - The pairing distance between the two sets (a candidate
    Newton-Raphson seed and its target SW critical point)

This script is a *static* witness for the seeding rule. It does not
yet drive a SnapPy Newton iteration; that is the next pipeline step.

*** NO-FLOAT64 (2026-09-13) ***

Every number here used to be float64 — not merely cast at the record, but
*computed* in float64 via `numpy` and Python `complex`, with the verdict read
back off it. Four separate defects, in increasing order of how much they
mattered:

1. `q0` came from `q_parameter.Q`, the **float64** q_0 (17 digits), so the
   algebraic seeds `q_0^{-k}` started with 17 digits of a 50-digit constant.
   Now `q_at()`, imported after `set_compute_dps()` so the module builds its
   constants at the live precision rather than at 53 bits.
2. The color-tube discriminant Δ(z) was built with `numpy.polynomial` over
   float coefficients and its roots taken by `numpy.polyroots`. **Δ's
   coefficients are exact integers** — `CUBIC_A/B/C/D` are integer lists and
   Δ = 18abcd − 4b³d + b²c² − 4ac³ − 27a²d² is an integer combination of their
   products — so they are computed with Python `int` arithmetic now (zero
   error, not merely small error) and the roots taken by `mp.polyroots` at the
   compute precision with `extraprec`.
3. 🛑 **`discriminant_derivative` was a CENTRAL FINITE DIFFERENCE with
   `h = 1e-7`.** In float64 that returns ~8 correct digits at best — the
   optimal central-difference step is `h ≈ ε^(1/3) ≈ 6e-6`, and 1e-7 sits
   inside the subtractive-cancellation regime. So the Newton *convergence
   rate*, which is this probe's entire measured claim, was limited by the
   difference quotient rather than by the mathematics. Δ is an explicit
   polynomial; its derivative is now taken **analytically** from the same
   exact integer coefficients.
4. The verdict ran on the shadow. `converged_at` / `converged` /
   `max_iterations_to_converge` are decided by `|Δ(z)| < tol`, and `Δ` is
   degree 6 — evaluating it in float64 near a root loses roughly half the
   available digits, so a `tol = 1e-12` test was being applied to a quantity
   known to ~1e-8 there. Same class as the Casimir-Macdonald and
   Δ-coupling probes (bean `qou-baye`).

`tol` is deliberately **kept at 1e-12**, and the loop still breaks on the
first iterate below it, so `iterations` and `converged_at` remain directly
comparable across the arithmetic change.  The precision-appropriate question
is asked in a separate `newton_deep_convergence` pass rather than by moving
the threshold.

*** WHAT THE DRAIN ACTUALLY CHANGED — it is not cosmetic ***

119 recorded fields moved by more than 1e-12 relative, and the pattern says
which defect did it:

    residual_trace[1]   73.80983470605896        ->  73.8098363816047...   2.27e-08
    residual_trace[8]    1.5295667703648856e-06  ->   1.5295935116521e-06  1.75e-05
    final_residual       2.997783086261874e-13   ->   2.1204641552487e-13  29.3 %

**The Newton iterates were wrong from the first step**, by 2.3e-8 — four
orders of magnitude worse than float64 rounding, and exactly the size of a
`h = 1e-7` central-difference error on Δ'.  Newton divides by that derivative,
so every subsequent iterate inherits and compounds it, reaching 29 % on the
final residual.  So the convergence trace this probe exists to report was good
to ~8 digits at best, and its final residuals were wrong by a third.

What did NOT change is the verdict *at the historical tolerance*: every
`converged_at` and every iteration count is identical, and inside the 16-step
loop `k=3` still stops at `|Δ_*| = 1.1893e+01` (against `1.1898e+01` float64).

🛑 **But the reading that `k=3` FAILS to converge is wrong, and the deep pass
shows it.**  With an exact derivative, `k=3` reaches `1e-40` at iteration
**23** — `|Δ_*| = 4.84e-42`.  The historical `max_iter = 16` simply cut it off.
So `k=3` converges more slowly than its siblings (23 steps against 11 / 13 /
12) rather than not at all, and the recorded `converged_at: null` is a budget
artefact, not a mathematical fact.

That distinction was **unavailable** to the float64 version in principle, not
merely in practice: with ~1e-8 error in each iterate the iteration stalls
around 1e-13 and can never reach 1e-40 at any step count, so "does this seed
eventually converge?" had no answer there.  This is the reason the deep pass
exists, and the reason it is worth its extra twenty lines.

(This paragraph first asserted the opposite — "that failure is therefore real"
— written from the historical loop's output before the deep pass had been run.
Corrected the same hour, by running the measurement it was added to make.)

Removal record for `pl-jsj-mass-integration-equivalence` (owner ruling
"a1", relayed 2026-10-10: the carrier stays REMOVED and citations point at the
record). Deleted in f86ea9d7ac, 2026-05-18, "content(thimble): demote the
`picard-lefschetz-thimble` definition + delete redundant bridges" (subject paraphrased; full label in docs/audits/2026-10-11-retired-label-records.md) -- Phase C of the
thimble simplification, on the stated ground that "PL is no longer rigorously
needed after Tier 1+2 (algebraic-residue swap on principal Galois orbit +
Moebius-from-binomials derivation)". It was a REDUNDANT bridge, not a lost one.
Its chapter `descartes-universe/` has since been removed entirely, so there is
no longer anywhere for it to live. Do NOT restore it.

Retired-label note: a block named above with a backticked stem and no
`prop:`/`conj:` prefix has NO carrier in folio/ — it was demoted to
_deprecated/ and is recorded in docs/audits/2026-10-11-retired-label-records.md §A,
with the statement it carried and the command to recover its content.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from _precision import set_compute_dps, fmt  # noqa: E402

# Raise the working precision BEFORE importing `q_parameter`: that module
# builds its `mpf` constants at import time, so importing it first freezes
# q_0 at 53 bits (measured: `q_at()` returns 1.1099785827513808 — the
# float64 value promoted — against the 50-digit
# 1.1099785827513808075916690956107688798744991218736).
set_compute_dps()

from mpmath import mp, mpf, mpc  # noqa: E402
from q_parameter import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Maximum truncation depth probed in the witness.  Bumping this gives
# more algebraic seed candidates per critical point, at the cost of
# extra polynomial multiplications in `q_pochhammer_denom_poly`.
MAX_DEPTH = 4

# Imaginary perturbation applied to real algebraic seeds q^{-k} to
# enter the complex plane for Newton-Raphson on Δ(z).  Shared with
# `snappy_cusp_seeding.py` so both witnesses use the same convention.
# An exact decimal, lifted at the live precision — not the float 0.1j,
# which is 0.1000000000000000055511151231257827.
IM_PERTURBATION_STR = "0.1"

# Coefficients of a, b, c, d in the color-tube cubic
#   F(z, c) = c^3 + (4z+1) c^2 + (6z^2+3z+1) c + (4z^3+3z^2+2z+1)
# expressed as polynomials in z (ascending powers).  Shared between
# the discriminant root-finder and the pointwise discriminant
# evaluator below.
#
# INTEGERS, not floats.  Δ(z) is an integer combination of products of
# these, so its coefficients are exact integers and the polynomial
# carries no error at all — see defect 2 in the module docstring.
CUBIC_A: list[int] = [1]                # 1
CUBIC_B: list[int] = [1, 4]             # 1 + 4z
CUBIC_C: list[int] = [1, 3, 6]          # 1 + 3z + 6z²
CUBIC_D: list[int] = [1, 2, 3, 4]       # 1 + 2z + 3z² + 4z³

# Newton tolerance.  Kept at the historical value on purpose — see the
# closing paragraph of the module docstring.
NEWTON_TOL_STR = "1e-12"
# A tolerance the arithmetic can actually resolve.  Used ONLY by the separate
# deep pass below, never inside `newton_iterate_from_seed` — that function's
# loop breaks at `NEWTON_TOL_STR`, so a tight threshold evaluated inside it
# could never fire and would publish a field that is structurally always null.
NEWTON_TOL_TIGHT_STR = "1e-40"
NEWTON_DEEP_MAX_ITER = 40


def _serialise(obj):
    """Render an `mpf`/`mpc`-bearing structure for the witness.

    Single point at which a number becomes text, and it becomes text via
    `_precision.fmt`.  Every numeric field in this witness used to be
    `float(...)`, which threw ~50 of the available digits away at the record
    boundary — and, worse, was read back to decide convergence.
    """
    if isinstance(obj, dict):
        return {k: _serialise(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_serialise(v) for v in obj]
    if isinstance(obj, mp.mpf):
        return fmt(obj)
    return obj


# ── exact integer / mpf polynomial helpers ──────────────────────

def _polymul(p: list, q: list) -> list:
    """Multiply two polynomials given in ASCENDING powers.

    Type-preserving: two `int` lists give an `int` list (exact), so the
    discriminant's coefficients below are exact integers.
    """
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a == 0:
            continue
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def _polyadd(p: list, q: list) -> list:
    n = max(len(p), len(q))
    return [
        (p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0)
        for i in range(n)
    ]


def _polyscale(p: list, s) -> list:
    return [s * c for c in p]


def _polypow(p: list, n: int) -> list:
    out = [1]
    for _ in range(n):
        out = _polymul(out, p)
    return out


def _polyderiv(p: list) -> list:
    """d/dz of an ascending-powers polynomial.  Exact for `int` input."""
    return [k * c for k, c in enumerate(p)][1:] or [0]


def _polyeval(p: list, z):
    """Horner evaluation at `z` (an `mpf`/`mpc`); no float64 anywhere."""
    out = z * 0
    for c in reversed(p):
        out = out * z + c
    return out


# ── q-Pochhammer denominator polynomial ─────────────────────────

def q_pochhammer_denom_roots(q, n: int) -> list:
    """Return the n simple roots of (x; q)_n = ∏_{k=0..n-1}(1 - x q^k).

    Each factor (1 - x q^k) has a single root at x = q^{-k}.  The roots
    are all real (since q is real); we return them as complex numbers
    so they line up with PL discriminant roots (which are complex).
    """
    return [mpc(q ** (-k), 0) for k in range(n)]


def q_pochhammer_denom_poly(q, n: int) -> list:
    """Coefficients of (x; q)_n in ASCENDING powers of x.

    Sanity check on the analytic root formula.  `mpf` throughout —
    `numpy.convolve` over float64 previously.
    """
    poly = [mpf(1)]
    for k in range(n):
        poly = _polymul(poly, [mpf(1), -(q ** k)])   # (1 - x q^k)
    return poly


# ── Discriminant of the color-tube cubic — EXACT integers ───────

def color_tube_discriminant_coeffs() -> list[int]:
    """Δ(z) = 18abcd − 4b³d + b²c² − 4ac³ − 27a²d², ASCENDING powers.

    Every coefficient is an exact Python `int`: `CUBIC_A/B/C/D` are integer
    lists and every operation above is an integer ring operation.  The
    previous implementation built this with `numpy.polynomial` over float64.
    """
    a, b, c, d = CUBIC_A, CUBIC_B, CUBIC_C, CUBIC_D
    t1 = _polyscale(_polymul(_polymul(_polymul(a, b), c), d), 18)
    t2 = _polyscale(_polymul(_polypow(b, 3), d), -4)
    t3 = _polymul(_polypow(b, 2), _polypow(c, 2))
    t4 = _polyscale(_polymul(a, _polypow(c, 3)), -4)
    t5 = _polyscale(_polymul(_polypow(a, 2), _polypow(d, 2)), -27)
    out = [0]
    for t in (t1, t2, t3, t4, t5):
        out = _polyadd(out, t)
    return out


DELTA_COEFFS: list[int] = color_tube_discriminant_coeffs()
DELTA_DERIV_COEFFS: list[int] = _polyderiv(DELTA_COEFFS)


def color_tube_discriminant_roots() -> list:
    """Roots of Δ(z) at the live compute precision.

    `mp.polyroots` wants DESCENDING coefficients; `DELTA_COEFFS` is ascending.
    `extraprec` is what makes a degree-6 root-find trustworthy — the previous
    `numpy.polyroots` had 53 bits and no option.
    """
    desc = list(reversed(DELTA_COEFFS))
    roots = mp.polyroots(
        [mpf(c) for c in desc],
        maxsteps=200,
        extraprec=4 * mp.prec,
    )
    return [mpc(r) for r in roots]


def discriminant_value(z):
    """Δ(z), evaluated by Horner over the exact integer coefficients."""
    return _polyeval(DELTA_COEFFS, z)


def discriminant_derivative(z):
    """Δ'(z) — ANALYTIC, from the exact integer coefficients.

    Was a central finite difference with `h = 1e-7` in float64, i.e. ~8
    correct digits of a quantity Newton divides by.  See defect 3 in the
    module docstring.  This is exact to the working precision.
    """
    return _polyeval(DELTA_DERIV_COEFFS, z)


# ── Pairing: nearest discriminant root for each algebraic seed ──

def pair_seeds_to_critical_points(seeds: list, critical_points: list) -> list[dict]:
    """For each algebraic seed, find the closest PL critical point
    and report the pairing distance.

    The conjecture (shared-denominator-cusp-holonomy) asserts that
    these distances vanish under τ_arch.  Since the algebraic seeds
    here are real and the discriminant roots are complex conjugate
    pairs, the raw distances are non-zero — they measure how far
    the algebraic seed sits from the matched SW critical point in
    the complex plane, before τ_arch is applied.  This is the
    "Newton-Raphson seed-to-target distance" recorded in the
    witness.

    `min` over `mpf` distances now; `numpy.argmin` over float64 before, so
    two nearly-equidistant critical points could be ordered by rounding.
    """
    if not critical_points:
        return []
    pairs = []
    for k, seed in enumerate(seeds):
        dists = [abs(seed - cp) for cp in critical_points]
        idx = min(range(len(dists)), key=lambda i: dists[i])
        pairs.append({
            "k": k,
            "seed_real": seed.real,
            "seed_imag": seed.imag,
            "matched_zc_real": critical_points[idx].real,
            "matched_zc_imag": critical_points[idx].imag,
            "pairing_distance": dists[idx],
            "matched_zc_index": idx,
        })
    return pairs


# ── Newton-Raphson driver from algebraic seeds ──────────────────

def newton_iterate_from_seed(seed, max_iter: int = 16) -> dict:
    """Drive Newton-Raphson on Δ(z) = 0 starting from `seed`.

    Returns a dict recording:
      - per-iteration residual |Δ(z_k)|
      - iterations to reach tol (or max_iter if not converged)
      - final z_k

    This is the empirical test of the
    `shared-denominator-cusp-holonomy` conjecture's prediction that
    algebraic seeds sit at SW critical points (Δ = 0). If the
    conjecture holds, the residual at iteration 0 is small and the
    solver converges in O(1) steps.

    The loop structure — `break` on the first iterate below `tol` — is
    unchanged from the float64 version, so `iterations` and `converged_at`
    remain directly comparable across the arithmetic change.  The
    precision-appropriate question is asked separately by
    `newton_deep_convergence`, because a tight threshold tested inside this
    loop can never fire: the loose `break` gets there first.
    """
    tol = mpf(NEWTON_TOL_STR)
    z = mpc(seed)
    residuals = [abs(discriminant_value(z))]
    converged_at = None
    stationary_at = None
    for it in range(1, max_iter + 1):
        d_val = discriminant_value(z)
        d_der = discriminant_derivative(z)
        if abs(d_der) < mpf("1e-30"):
            # Stationary point — abandon Newton step.
            stationary_at = it
            break
        z = z - d_val / d_der
        res = abs(discriminant_value(z))
        residuals.append(res)
        if res < tol and converged_at is None:
            converged_at = it
            break
    return {
        "seed_real": seed.real,
        "seed_imag": seed.imag,
        "final_real": z.real,
        "final_imag": z.imag,
        "iterations": len(residuals) - 1,
        "converged_at": converged_at,
        "stationary_at": stationary_at,
        "initial_residual": residuals[0],
        "final_residual": residuals[-1],
        "residual_trace": residuals,
    }


def newton_deep_convergence(seed) -> dict:
    """Run Newton to `NEWTON_TOL_TIGHT_STR` (or `NEWTON_DEEP_MAX_ITER`).

    This is the question the float64 version could not ask.  With the
    derivative taken by a 1e-7 central difference at 53 bits, the iterates
    themselves carried ~1e-8 relative error (measured: 2.27e-8 at the FIRST
    step, 1.75e-5 by step 8, and 29 % on the final residual), so "how many
    Newton steps to reach machine-irrelevant accuracy" was unanswerable —
    the iteration stalled at the difference quotient's floor long before it
    stalled at the mathematics.

    Recorded under its own key; it does not touch the historical fields.
    """
    tol = mpf(NEWTON_TOL_TIGHT_STR)
    z = mpc(seed)
    res = abs(discriminant_value(z))
    reached = None
    stationary_at = None
    for it in range(1, NEWTON_DEEP_MAX_ITER + 1):
        d_der = discriminant_derivative(z)
        if abs(d_der) < mpf("1e-30"):
            stationary_at = it
            break
        z = z - discriminant_value(z) / d_der
        res = abs(discriminant_value(z))
        if res < tol:
            reached = it
            break
    return {
        "reached_tight_at": reached,
        "stationary_at": stationary_at,
        "iterations": min(it, NEWTON_DEEP_MAX_ITER),
        "final_residual": res,
        "final_real": z.real,
        "final_imag": z.imag,
    }


# ── Main ────────────────────────────────────────────────────────

def main() -> None:
    q0 = q_at()
    print(f"q_0 = {mp.nstr(q0, 30)}   (mp.dps = {mp.dps})")
    print(f"Δ(z) exact integer coefficients (ascending): {DELTA_COEFFS}")
    print()

    # PL discriminant roots — one-time setup
    crit_pts = color_tube_discriminant_roots()
    print(f"PL discriminant: {len(crit_pts)} critical points")
    for i, zc in enumerate(crit_pts):
        sgn = "+" if zc.imag >= 0 else "-"
        # float() inside an f-string is display, not computation.
        print(f"  z_c[{i}] = {float(zc.real):+.8f} {sgn} "
              f"{float(abs(zc.imag)):.8f}i")
    print()

    # Algebraic seeds at depths n = 1, ..., MAX_DEPTH (smallest non-
    # trivial cases).
    im_pert = mpc(0, mpf(IM_PERTURBATION_STR))
    depth_results = []
    for n in range(1, MAX_DEPTH + 1):
        seeds = q_pochhammer_denom_roots(q0, n)
        pairs = pair_seeds_to_critical_points(seeds, crit_pts)
        print(f"depth n = {n}: {len(seeds)} algebraic seeds")
        for p in pairs:
            print(
                f"  k={p['k']} seed={float(p['seed_real']):+.8f} "
                f"-> z_c[{p['matched_zc_index']}] "
                f"({float(p['matched_zc_real']):+.8f}, "
                f"{float(p['matched_zc_imag']):+.8f}i)"
                f" |Δ| = {float(p['pairing_distance']):.6f}"
            )
        print()

        # Drive Newton-Raphson on Δ(z) = 0 from each seed.  Bumps the
        # real seed into the complex plane along the steepest-descent
        # direction; convergence to a critical point measures the
        # `shared-denominator-cusp-holonomy` conjecture's prediction.
        # Seed `q_0^0 = 1` is purposely perturbed off the real axis so
        # the Jacobian is invertible.
        newton_runs = []
        for k, seed in enumerate(seeds):
            perturbed = seed + im_pert     # enter the complex plane
            run = newton_iterate_from_seed(perturbed)
            run["k"] = k
            newton_runs.append(run)
            print(
                f"  k={k} Newton: "
                f"|Δ_0|={float(run['initial_residual']):.4e} "
                f"-> |Δ_*|={float(run['final_residual']):.4e} "
                f"in {run['iterations']} iter "
                f"(converged@{run['converged_at']})"
            )

        depth_results.append({
            "n": n,
            "seeds": [
                {"k": k, "seed_real": s.real, "seed_imag": s.imag}
                for k, s in enumerate(seeds)
            ],
            "pairings": pairs,
            "newton_runs": newton_runs,
            "denom_polynomial_coefficients": q_pochhammer_denom_poly(q0, n),
        })

    # Witness emission
    w = WitnessBuilder("q-pochhammer-seed", engine="mpmath")
    w.set_description(
        "q-Pochhammer denominator zeros at substrate q_0, paired against "
        "Picard-Lefschetz discriminant roots of the color-tube cubic. "
        "Provides the candidate Newton-Raphson seed values for the "
        "Thurston gluing equations on the active JSJ piece.  "
        "Arithmetic is mpmath end to end as of 2026-09-13: the "
        "discriminant's coefficients are exact integers, its derivative is "
        "taken analytically rather than by a 1e-7 central finite difference, "
        "and the roots come from mp.polyroots with extraprec instead of "
        "numpy.polyroots at 53 bits.  The per-depth newton_runs keep the "
        "historical loop and tol = 1e-12, so iterations and converged_at are "
        "directly comparable across the change; the precision-appropriate "
        "question (steps to tol = 1e-40) is asked separately in "
        "newton_deep_convergence.  MEASURED CONSEQUENCE: the float64 "
        "iterates were wrong from the first step — 2.27e-8 relative at "
        "residual_trace[1], 1.75e-5 by step 8, and 29 % on the final "
        "residual (2.998e-13 recorded against an exact 2.120e-13).  That is "
        "the 1e-7 central-difference derivative, not float64 rounding, and "
        "it means the convergence trace this probe exists to report carried "
        "~8 correct digits at best.  The converged_at verdicts and iteration "
        "counts are unchanged, so the verdict at the historical tolerance "
        "survives — but the reading that k=3 FAILS to converge does not: "
        "with an exact derivative it reaches 1e-40 at iteration 23 "
        "(|D_*| = 4.84e-42), so its recorded converged_at:null is an artefact "
        "of max_iter = 16, not a mathematical fact.  A float64 run could not "
        "have decided that at any step count: at ~1e-8 iterate error the "
        "iteration stalls near 1e-13 and never reaches 1e-40."
    )
    w.set_content_block("conj:shared-denominator-cusp-holonomy")
    w.add_parameter("q0", fmt(q0))
    w.add_parameter("max_depth", MAX_DEPTH)
    w.add_parameter("newton_tol", NEWTON_TOL_STR)
    w.add_parameter("newton_tol_tight", NEWTON_TOL_TIGHT_STR)
    w.add_parameter("im_perturbation", IM_PERTURBATION_STR)
    w.add_parameter("delta_coeffs_exact_integers", str(DELTA_COEFFS))

    w.add_data("pl_discriminant_roots", _serialise([
        {"index": i, "z_c_real": zc.real, "z_c_imag": zc.imag}
        for i, zc in enumerate(crit_pts)
    ]))
    w.add_data("depth_results", _serialise(depth_results))

    # The shared-denominator conjecture predicts that under τ_arch the
    # seeds map exactly onto a matched subset of the PL critical points.
    # Our raw seeds are real, while critical points are complex; the
    # pairing distance therefore measures the residual the SnapPy
    # Newton-Raphson solver has to drive to zero.
    all_dists = [p["pairing_distance"] for d in depth_results
                 for p in d["pairings"]]
    w.add_data("pairing_summary", {
        "min_distance": fmt(min(all_dists)),
        "max_distance": fmt(max(all_dists)),
    })

    w.add_caveat(
        "Algebraic seeds q_0^{-k} are real; PL discriminant roots are "
        "complex (three conjugate pairs). The pairing distance is the "
        "complex-plane distance from a real seed to its closest PL "
        "critical point; under τ_arch the seed acquires an imaginary "
        "part matching the critical point. The Newton-Raphson solver "
        "uses the real seed as initial guess and converges to the "
        "complex SW critical point via a few gradient-flow steps."
    )
    # Newton-Raphson convergence summary
    all_runs = [run for d in depth_results for run in d["newton_runs"]]
    converged_runs = [r for r in all_runs if r["converged_at"] is not None]
    initial = [r["initial_residual"] for r in all_runs]
    w.add_data("newton_summary", {
        "total_runs": len(all_runs),
        "converged": len(converged_runs),
        "max_iterations_to_converge": (
            max((r["converged_at"] for r in converged_runs), default=None)
        ),
        "min_initial_residual": fmt(min(initial)),
        "max_initial_residual": fmt(max(initial)),
    })

    # The precision-appropriate convergence question, asked separately so the
    # fields above stay comparable across the float64 -> mpmath change.
    deep = []
    print()
    print(f"deep pass (tol {NEWTON_TOL_TIGHT_STR}, max "
          f"{NEWTON_DEEP_MAX_ITER} iter):")
    for k in range(MAX_DEPTH):
        seed = mpc(q0 ** (-k), 0) + im_pert
        r = newton_deep_convergence(seed)
        r["k"] = k
        deep.append(r)
        print(f"  k={k} reached_tight@{r['reached_tight_at']} "
              f"in {r['iterations']} iter, "
              f"|Δ_*|={float(r['final_residual']):.4e}")
    w.add_data("newton_deep_convergence", _serialise(deep))

    w.add_caveat(
        "This script is a static seeding witness plus a Newton-Raphson "
        "driver on the color-tube discriminant Δ(z). It does not yet "
        "drive "
        "a SnapPy Newton iteration to verify O(1)-step convergence; "
        "that integration is the next pipeline step (cf. "
        "conj:shared-denominator-cusp-holonomy §implication)."
    )

    w.save()
    print("Witness written.")


if __name__ == "__main__":
    main()
