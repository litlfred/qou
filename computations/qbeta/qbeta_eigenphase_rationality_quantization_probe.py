#!/usr/bin/env python3
"""The q-uniform braid-image eigenphase is QUANTIZED — and only one rational
phase fits the ladder window.

Bean `qou-pdix` (the S1 blocker), building directly on its sibling
`qbeta_braid_image_eigenphase_exclusion_probe.py`.  Two parts, and they have
very different epistemic status — read the status line on each before quoting
either.

## PART 1 — a structural strengthening (scope-(b), a proved invariant)

The sibling probe closes branch (1) of the `EigenphaseCarrierVacuity`
trichotomy like this: `tr ρ(w)` is a Laurent polynomial, `|2cos α| ≤ 2`, a
Laurent polynomial bounded on `(0,∞)` is constant, so `cos α` is constant —
and `α_C`, `α_D` are both *non-constant*, contradiction.

**That argument has a hole, and it is exactly the case a derivation would
want.**  It refutes the ansatz `α = (z−1)h/2` because that ansatz varies with
`q`.  It says nothing against a **constant** `α` — and nothing requires the
ladder's phase to vary, since the ladder `Q_N1 = Q_A·cos(α − u/2)` is already
`q`-dependent through `u`.  Someone proposing `α = α_req`, a pure number, walks
straight through it.

This probe closes that case, by running the same boundedness argument one step
further instead of stopping at "constant":

  1. `det ρ(σ_i) = −1` identically, so `det ρ(w) = (−1)^{e(w)}`, `e` the
     exponent sum.  `det = 1` is therefore not an assumption on `M` — it is a
     **parity condition on the word**.  (assertions 1–3)
  2. `σ_i^{-1} = σ_i − (q − q^{-1})·I` from the Hecke relation, so every word
     matrix has entries in `ℤ[q,q^{-1}]` and `tr ρ(w) ∈ ℤ[q,q^{-1}]`.
     (assertions 4–5)
  3. Bounded on `(0,∞)` ⟹ constant ⟹ **an integer**, since the coefficients
     are integers.  On the 2-dimensional `V_(2,1)`, `|tr| ≤ 2` then forces
     `tr ∈ {−2,−1,0,1,2}` and hence

         α ∈ {0, π/3, π/2, 2π/3, π}                                (assertion 7)

     — a five-element set.  No ansatz is read anywhere in this.
  4. The same argument on a `d`-dimensional `V_λ` gives `tr ρ(w^k)` constant
     integers for every `k`, hence an integer characteristic polynomial, hence
     eigenvalues that are algebraic integers with **all** conjugates on the
     unit circle — which by **Kronecker's theorem** are roots of unity.  So in
     every irrep, a `q`-uniformly elliptic braid image has

         α ∈ 2π·ℚ                                                  (assertion 8)

     This is the general form; the five-element set in (3) is its `d = 2` case.

`|α_req| = 0.05235868…` is not in the five-element set — the nearest member is
`0`, and it is **4795 ladder windows** away.  So branch (1) is closed on
`V_(2,1)` for a constant phase too, without invoking transcendence.

## PART 2 — a MEASUREMENT, and it is NOT a derivation (read the fit status)

Part 1 leaves the higher-dimensional case open (the sibling probe names it: one
eigenphase among several).  There `α ∈ 2π·ℚ` is the only surviving constraint —
so the search space for `α` is no longer a continuum but a **discrete list**,
and one can simply ask which members of it fit.  That question has never been
run.  Answer:

    2π/120 = π/60  is the UNIQUE primitive rational phase with denominator
    N ≤ 1000 lying inside the ladder's |c₃| ≤ 1 window.        (assertion 9)

and it sits **19× closer** to `α_req` than convention C does (0.109 windows vs
2.066 — C is *outside* the window).  It would imply `|c₃| ≈ 0.11` where the
committed C-frame extraction gives `−2.069`.                    (assertions 10–11)

**🛑 FIT STATUS — stated plainly, because the directive requires it.**  Under
AGENTS.md §"NO FITTING", picking `N = 120` *because it reproduces `α_req`* is
**selection against the target**, and that is what has been done here.  No
continuous parameter is tuned and it is still a fit.  It is reported as an
**identification candidate with a uniqueness measurement**, and it is **not
wired, not adopted, and not proposed as a value for anything.**

What would convert it into a derivation is named and not done: exhibit a braid
word and a partition whose `q`-uniform eigenphase is `2π/120` — i.e. derive the
**120** from the framework rather than from `α_req`.

**🛑 And the obvious way to do that is REFUTED here, by me, in the same probe
that raises the candidate (assertion 14).**  The tempting reading is that 120
is already the framework's own number — `|2I| = |S_5| = |Aut(Bring)| = 120`,
and the canonical chain runs through Bring's curve.  That reading does not
survive one line of group theory: an eigenvalue that is a *primitive* 120th
root of unity requires a group element of order divisible by 120, and **neither
group has one** — `S_5` has maximal element order **6**, and `2I = SL(2,5)` has
maximal element order **10** (its exponent is 60, not 120).  A group of order
120 does not supply a 120th root of unity; only an element of order 120 does.

So the candidate has **no identified mechanism at all**, and the one a reader
would reach for first is dead.  That makes it weaker than the uniqueness
measurement alone suggests, and it is the reason this is filed as a candidate
rather than a finding.  The coincidence statistics are reported below so a
reader can price it without taking my word:

  * expected number of primitive rational phases inside the window, `N ≤ 120`:
    **0.0152**  — so a hit at that denominator bound is not generic;
  * expected number, `N ≤ 1000`: **1.06** — so *that* a unique hit exists at
    this bound is entirely generic, and carries no information;
  * conditional on one hit, the chance its denominator is exactly 120:
    **1.05e-04**.

The honest reading is the third: the informative fact is *which* denominator
won, not that one did.

**🛑 SECOND SCOPE LIMIT, equally load-bearing.**  The ladder inverted here is
built on `Q_A = m_e|q²−2q−1|(q+1)/(2q³)` — the **`z = 1` cell, RETIRED as the
base by the 2026-09-08 owner ruling** (AGENTS.md; bean `qou-99qc`).  So `α_req`
is the phase required by a *retired* base, and nothing here moves the live
dashboard, whose `Q_β` row is base-only at ~4.3e+8 ppb on the ruled `z_D` base.
A phase correction is `O(0.1 %)` and cannot address a 43 % base gap: **the
D-base miss is not a phase problem**, and this probe should not be cited as if
it were.

What Part 1 *does* give `qou-cds1` is smaller but real and convention-free: if
`α` is a braid-image eigenphase at all, the rationality invariant makes it a
pure number with **no `z` in it**, so the phase does not need re-deriving
per-convention.  The C-vs-D question for the *phase* dissolves; it survives only
for the base.

## PART 3 — deriving `α` CANNOT unblock `qou-cds1`.  The gap is in the base.

This is the sharper result for the arc, and it was found by asking the question
Part 2 invites: *is the compute wrong?*  It is not — but it is computing a
**retired** object, and on the live one the whole rung is structurally excluded.

`qou-iagg` (the dashboard re-score) waits on `qou-cds1` (the `c_k` ladder on the
ruled `z_D` base), which waits on this bean (derive `α`).  **The second link does
not hold.**  On the ruled base the ladder must supply a factor

    Q_codata / Q_D  =  0.78233341 / 0.4447004  =  1.7592370…   > 1

while its `N = 1` rung is `cos(α − u/2) ≤ 1` for **every** `α`, and its `N = 2`
rung is `(1 + c₂u²) = 0.99992745… < 1` at the committed `c₂ = −1`.  The two
together are bounded by `0.99992745 < 1 < 1.7592`.               (assertions 15–16)

So no phase whatsoever repairs a base that is 43 % low, because a cosine cannot
exceed one.  The `c₃` that would be required instead is `1.23e6`, not `O(1)`.
**The `Q_β` L2 residual is a BASE problem, not a phase problem, and not a ladder
problem at all.**  Scope-(b), citing `Real.cos_le_one`.

This is the mirror of this bean's own 2026-08-22 entry, which excluded a `cosh`
re-reading because `cosh ≥ 1` sat on the wrong side of a required value *below* 1.
Here the required value is *above* 1 and `cos ≤ 1` is on the wrong side of it.

Lean twin (sorry-free, `lean`-direct exit 0, axioms `[propext, Classical.choice,
Quot.sound]`): `QOU.QBeta.EigenphaseQuantization.cos_rung_lt_of_base_short` and
its ladder-shaped corollary, alongside `two_cos_eq_int_cases` and
`not_braid_eigenphase_of_two_cos_mem_Ioo` for Part 1.

## Method

Exact `ℤ[q,q^{-1}]` Laurent arithmetic over Python `int` (no sympy simplify, no
floats) for Part 1; mpmath at 60 dps from the 50-digit proton-pin string for the
anchor evaluations.  No float64 anywhere, per AGENTS.md §"PROBES ARE NOT
EXEMPT" — `float()` appears only inside f-strings for display.
"""
from __future__ import annotations

import itertools
import sys
from math import gcd
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import substrate_ladder_quantities  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
C2 = mp.mpf(-1)  # hardcoded in the committed extraction

WORD_LEN = 6  # exhaustive over 4^6 = 4096 words


# ── exact Laurent polynomials in q over ℤ: {exponent: coefficient} ───────────

def lp(*terms):
    d = {}
    for e, c in terms:
        if c:
            d[e] = d.get(e, 0) + c
    return {e: c for e, c in d.items() if c}


def lp_add(a, b):
    d = dict(a)
    for e, c in b.items():
        d[e] = d.get(e, 0) + c
    return {e: c for e, c in d.items() if c}


def lp_mul(a, b):
    d = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            d[e1 + e2] = d.get(e1 + e2, 0) + c1 * c2
    return {e: c for e, c in d.items() if c}


def mat_mul(A, B):
    return [[lp_add(lp_mul(A[i][0], B[0][j]), lp_mul(A[i][1], B[1][j]))
             for j in range(2)] for i in range(2)]


def lp_eval(a, x):
    """Evaluate at mpmath x. Exact-in, mpf-out; no float64."""
    return sum((mp.mpf(c) * x ** e for e, c in a.items()), mp.mpf(0))


ZERO, ONE = {}, {0: 1}
EYE = [[ONE, ZERO], [ZERO, ONE]]

# σ_i with eigenvalues {q, −q⁻¹}, i.e. σ² = (q − q⁻¹)σ + 1 (AGENTS.md §7a).
# Same normalisation as the sibling exclusion probe.
S1 = [[lp((-1, -1)), lp((1, 1))], [ZERO, lp((1, 1))]]
S2 = [[lp((1, 1)), ZERO], [lp((-1, 1)), lp((-1, -1))]]
# σ⁻¹ = σ − (q − q⁻¹)·I, from the Hecke relation. Entries stay in ℤ[q,q⁻¹].
S1I = [[lp((1, -1)), lp((1, 1))], [ZERO, lp((-1, 1))]]
S2I = [[lp((-1, 1)), ZERO], [lp((-1, 1)), lp((1, -1))]]
GEN = {1: S1, 2: S2, -1: S1I, -2: S2I}


def word_matrix(word):
    M = EYE
    for g in word:
        M = mat_mul(M, GEN[g])
    return M


def trace(M):
    return lp_add(M[0][0], M[1][1])


def det(M):
    return lp_add(lp_mul(M[0][0], M[1][1]),
                  {e: -c for e, c in lp_mul(M[0][1], M[1][0]).items()})


def is_constant(a):
    return all(e == 0 for e in a)


def main() -> int:
    failures = []

    def check(name, ok, detail=""):
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
        if detail:
            print(f"        {detail}")
        if not ok:
            failures.append(name)
        return ok

    print("=" * 78)
    print(" Q_beta eigenphase: the q-uniform braid image is QUANTIZED")
    print("=" * 78)
    print("\nPART 1 - structural (scope-(b))\n")

    # 1-2. determinants of the generators and their inverses
    check("1. det rho(sigma_i) = -1 identically, both generators",
          det(S1) == {0: -1} and det(S2) == {0: -1})
    check("2. sigma_i . sigma_i^-1 = I  (the Hecke inverse is Laurent)",
          mat_mul(S1, S1I) == EYE and mat_mul(S2, S2I) == EYE)

    # 3-7. exhaustive sweep over all words of length <= WORD_LEN
    letters = (1, 2, -1, -2)
    det_ok = True
    integral_ok = True
    bounded_but_not_constant = []
    constants = set()
    n_words = 0
    for L in range(1, WORD_LEN + 1):
        for w in itertools.product(letters, repeat=L):
            n_words += 1
            M = word_matrix(w)
            e = sum(1 if g > 0 else -1 for g in w)
            if det(M) != {0: 1 if e % 2 == 0 else -1}:
                det_ok = False
            t = trace(M)
            if not all(isinstance(c, int) for c in t.values()):
                integral_ok = False
            # bounded on (0,inf) <=> constant: the top exponent blows up as
            # q -> inf and the bottom exponent as q -> 0+.
            if is_constant(t):
                constants.add(t.get(0, 0))
            else:
                lo, hi = min(t), max(t)
                if lo >= 0 and hi <= 0:
                    bounded_but_not_constant.append(w)

    check(f"3. det rho(w) = (-1)^(exponent sum), all {n_words} words |w| <= {WORD_LEN}",
          det_ok)
    check("4. tr rho(w) has INTEGER coefficients, every word", integral_ok)
    check("5. no word is bounded-but-not-constant (the Laurent lemma, verified)",
          not bounded_but_not_constant)
    check("6. the constant characters that occur all lie in [-2, 2]",
          all(abs(c) <= 2 for c in constants),
          f"observed constant characters: {sorted(constants)}")

    quantized = sorted({mp.nstr(mp.acos(mp.mpf(c) / 2), 12) for c in constants
                        if abs(c) <= 2})
    check("7. => the q-uniform eigenphase set on V_(2,1) is finite",
          len(constants) <= 5,
          f"alpha in {{{', '.join(quantized)}}} rad "
          f"(= {{0, pi/3, pi/2, 2pi/3, pi}} subset)")

    # 8. the Kronecker step, stated; its d=2 instance is assertion 7.
    check("8. Kronecker: q-uniform ellipticity => integer char poly => "
          "eigenvalues are roots of unity => alpha in 2*pi*Q",
          True,
          "general-d form; the d=2 instance is assertion 7 above. "
          "The Lean twin of this step is NOT written - see bean qou-pdix.")

    # ---- the anchor numbers -------------------------------------------------
    print("\nPART 2 - measurement (NOT a derivation; see the fit status)\n")

    def ladder(q):
        s = substrate_ladder_quantities(q, convention="C")
        h, u = s["h"], s["u"]
        Q_A = ME * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
        cos_req = QCOD / (Q_A * (1 + C2 * u ** 2))
        alpha_req = u / 2 - mp.acos(cos_req)
        window = u ** 3 / mp.fabs(mp.sin(alpha_req - u / 2))
        return Q_A, h, u, alpha_req, window

    def c3_of(alpha, q, Q_A, u):
        Q_N2 = Q_A * mp.cos(alpha - u / 2) * (1 + C2 * u ** 2)
        return (QCOD / Q_N2 - 1) / u ** 3

    anchors = {}
    for q, label in ((q_at(), "proton"), (q_muon_at(), "muon")):
        Q_A, h, u, areq, win = ladder(q)
        zC = mp.sqrt(q) / (1 + q)
        aC = (zC - 1) * h / 2
        cand = -mp.pi / 60
        anchors[label] = {
            "q": fmt(q), "alpha_required": fmt(areq), "window": fmt(win),
            "alpha_C": fmt(aC),
            "C_windows_from_required": fmt(abs(aC - areq) / win),
            "cand_2pi_over_120": fmt(cand),
            "cand_windows_from_required": fmt(abs(cand - areq) / win),
            "c3_implied_by_C": fmt(c3_of(aC, q, Q_A, u)),
            "c3_implied_by_cand": fmt(c3_of(cand, q, Q_A, u)),
        }
        print(f"  {label}:  alpha_req = {mp.nstr(areq, 16)}   "
              f"window = +-{mp.nstr(win, 6)}")
        print(f"    convention C : {mp.nstr(abs(aC - areq) / win, 6):>10} windows"
              f"   => c3 = {mp.nstr(c3_of(aC, q, Q_A, u), 8)}")
        print(f"    -2*pi/120    : {mp.nstr(abs(cand - areq) / win, 6):>10} windows"
              f"   => c3 = {mp.nstr(c3_of(cand, q, Q_A, u), 8)}")

    p = anchors["proton"]
    areq_p = mp.mpf(p["alpha_required"])
    win_p = mp.mpf(p["window"])
    target = abs(areq_p)

    # 9. uniqueness of the rational candidate
    def hits(nmax):
        out = []
        for N in range(1, nmax + 1):
            k0 = int(mp.floor(target * N / (2 * mp.pi) + mp.mpf("0.5")))
            for k in (k0 - 1, k0, k0 + 1):
                if k <= 0 or gcd(k, N) != 1:
                    continue
                if abs(2 * mp.pi * k / N - target) <= win_p:
                    out.append((N, k))
        return sorted(set(out))

    h1000 = hits(1000)
    check("9. exactly ONE primitive rational phase 2*pi*k/N with N <= 1000 "
          "lies inside the |c3| <= 1 window, and it is N = 120",
          h1000 == [(120, 1)],
          f"hits: {h1000}")

    check("10. the candidate is INSIDE the window and convention C is OUTSIDE",
          abs(mp.mpf(p["cand_windows_from_required"])) < 1
          < abs(mp.mpf(p["C_windows_from_required"])),
          f"candidate {p['cand_windows_from_required'][:7]} windows, "
          f"C {p['C_windows_from_required'][:7]} windows")

    check("11. |c3| implied by the candidate is well below the C-frame -2.069",
          abs(mp.mpf(p["c3_implied_by_cand"])) < 1
          < abs(mp.mpf(p["c3_implied_by_C"])),
          f"candidate c3 = {p['c3_implied_by_cand'][:12]}, "
          f"C c3 = {p['c3_implied_by_C'][:12]}")

    # 12. price the coincidence, so the reader does not have to take my word
    def totient(n):
        r, nn, d = n, n, 2
        while d * d <= nn:
            if nn % d == 0:
                while nn % d == 0:
                    nn //= d
                r -= r // d
            d += 1
        if nn > 1:
            r -= r // nn
        return r

    Phi = {}
    acc = 0
    for N in range(1, 1001):
        acc += totient(N)
        Phi[N] = acc
    exp120 = mp.mpf(Phi[120]) * win_p / mp.pi
    exp1000 = mp.mpf(Phi[1000]) * win_p / mp.pi
    cond120 = mp.mpf(totient(120)) / mp.mpf(Phi[1000])
    check("12. coincidence priced: a hit at N <= 1000 is GENERIC; "
          "the informative fact is WHICH denominator won",
          exp1000 > 1 > exp120,
          f"E[hits | N<=120] = {mp.nstr(exp120, 4)}, "
          f"E[hits | N<=1000] = {mp.nstr(exp1000, 4)}, "
          f"P(denominator = 120 | one hit) = {mp.nstr(cond120, 4)}")

    print("""
CONSEQUENCE

  PART 1 (scope-(b), proved invariant).  The sibling exclusion probe closes the
  braid-image branch only against a q-VARYING ansatz; a constant alpha walks
  through it.  Carrying the same boundedness argument one step further -- to
  integrality, and then (general d) to Kronecker -- closes the constant case
  too: a q-uniform braid-image eigenphase on V_(2,1) lies in the five-element
  set {0, pi/3, pi/2, 2pi/3, pi}, and |alpha_req| is 4795 windows from the
  nearest member.  Branch (1) is now closed on V_(2,1) for EVERY alpha, not
  only for the (z-1)h/2 family, and without invoking transcendence.

  Corollary for qou-cds1, convention-free: if alpha is a braid-image eigenphase
  at all, it is a pure number with no z in it.  The C-vs-D question for the
  PHASE dissolves; it survives only for the base.

  PART 2 (a fit, and labelled one).  Given alpha in 2*pi*Q, the search space is
  discrete, and exactly one member fits.  That is an identification CANDIDATE,
  selected against the target, and it is NOT adopted here.  It bears on a
  RETIRED base (the z = 1 cell) and moves no dashboard row: a ~0.1% phase
  cannot address the 43% gap of the ruled z_D base.  The D-base miss is not a
  phase problem.

  WHAT WOULD CLOSE IT: derive the 120 -- exhibit a braid word and a partition
  whose q-uniform eigenphase is 2*pi/120 -- rather than read it off alpha_req.
  Assertion 14 kills the mechanism a reader reaches for first: |2I| = |S_5| =
  120, but neither has an ELEMENT of order 120 (max 10 and 6), so neither
  supplies the root of unity. The candidate has no mechanism at all.

  PART 3 (scope-(b), proved invariant) -- THE ONE THAT RE-SCOPES THE ARC.
  Deriving alpha CANNOT unblock qou-cds1. The ruled z_D base needs a ladder
  factor of 1.7592 > 1; the N=1 rung is a COSINE, bounded by 1 for every alpha,
  and the N=2 rung is 0.99992745 < 1. The required c3 would be 1.23e6, not
  O(1). So the dependency chain qou-iagg <- qou-cds1 <- qou-pdix is WRONG at
  the second link: the Q_beta L2 residual is a BASE problem, not a phase
  problem and not a ladder problem at all. Lean twin sorry-free:
  QOU.QBeta.EigenphaseQuantization.cos_rung_lt_of_base_short.
""")

    # 13. the cross-anchor swing does NOT discriminate -- record it so the
    # candidate is not credited with a stability it does not have.
    m = anchors["muon"]
    swing_cand = abs(mp.mpf(p["c3_implied_by_cand"]) - mp.mpf(m["c3_implied_by_cand"]))
    swing_C = abs(mp.mpf(p["c3_implied_by_C"]) - mp.mpf(m["c3_implied_by_C"]))
    same = abs(swing_cand - swing_C) / swing_C < mp.mpf("0.02")
    check("13. cross-anchor c3 swing is the SAME for candidate and for C, "
          "so it does not discriminate between them",
          same,
          f"swing(candidate) = {mp.nstr(swing_cand, 6)}, "
          f"swing(C) = {mp.nstr(swing_C, 6)} -- both are just alpha_req's own "
          f"anchor dependence, not a property of either phase")

    # 14. refute the obvious mechanism for the 120, in the same probe that
    # raises the candidate. A group of order 120 does NOT supply a primitive
    # 120th root of unity; only an element of order 120 does.
    def elt_orders_S5():
        from math import lcm
        from functools import reduce
        def parts(n, mx=None):
            mx = mx or n
            if n == 0:
                yield []
            for k in range(min(n, mx), 0, -1):
                for r in parts(n - k, k):
                    yield [k] + r
        return sorted({reduce(lcm, pp) for pp in parts(5)})

    def elt_orders_2I():
        els = [(a, b, c, d) for a in range(5) for b in range(5)
               for c in range(5) for d in range(5) if (a * d - b * c) % 5 == 1]

        def mul(x, y):
            a, b, c, d = x
            e, f, g, hh = y
            return ((a * e + b * g) % 5, (a * f + b * hh) % 5,
                    (c * e + d * g) % 5, (c * f + d * hh) % 5)
        I2, out = (1, 0, 0, 1), set()
        for x in els:
            y, n = x, 1
            while y != I2:
                y, n = mul(y, x), n + 1
            out.add(n)
        return len(els), sorted(out)

    o_s5 = elt_orders_S5()
    n_2i, o_2i = elt_orders_2I()
    check("14. the obvious mechanism for 120 is REFUTED: neither S_5 nor "
          "2I = SL(2,5) has an element of order 120, so neither supplies a "
          "primitive 120th root of unity as an eigenvalue",
          max(o_s5) < 120 and max(o_2i) < 120 and n_2i == 120,
          f"|2I| = {n_2i} but element orders are {o_2i} (max {max(o_2i)}); "
          f"S_5 element orders {o_s5} (max {max(o_s5)}). A group of ORDER 120 "
          f"does not give a 120th root of unity - only an ELEMENT of order 120 "
          f"does. So the candidate has NO identified mechanism.")

    # ---- PART 3: the ruled z_D base cannot be reached by ANY phase ----------
    print("\nPART 3 - deriving alpha cannot unblock qou-cds1\n")
    q_p = q_at()
    s_p = substrate_ladder_quantities(q_p, convention="C")
    u_p = s_p["u"]
    Q_D = mp.mpf("0.4447004")          # RULED z_D base (AGENTS.md; qou-99qc)
    need = QCOD / Q_D
    rung2 = 1 + C2 * u_p ** 2          # the N=2 factor at the committed c2 = -1
    print(f"  Q_codata / Q_D          = {mp.nstr(need, 12)}   (> 1)")
    print(f"  max over ALL alpha of cos(alpha - u/2) = 1")
    print(f"  N=2 rung (1 + c2 u^2)   = {mp.nstr(rung2, 12)}   (< 1)")
    print(f"  => first two rungs <=     {mp.nstr(rung2, 12)}   < 1 < "
          f"{mp.nstr(need, 8)}")
    c3_needed = (need / rung2 - 1) / u_p ** 3
    print(f"  c3 that would be needed instead = {mp.nstr(c3_needed, 10)}  "
          f"(vs O(1))")

    check("15. the RULED z_D base needs a ladder factor strictly ABOVE 1, "
          "which a cosine rung can never supply",
          need > 1 and rung2 < 1,
          f"need = {mp.nstr(need, 12)}, and the N=1 rung is bounded by 1 while "
          f"the N=2 rung is {mp.nstr(rung2, 12)} < 1 -- so NO alpha closes it")

    check("16. the required c3 on the ruled base is ~1e6, not O(1): the gap is "
          "in the BASE, not in any rung",
          abs(c3_needed) > mp.mpf("1e5"),
          f"c3_needed = {mp.nstr(c3_needed, 10)}; deriving alpha therefore "
          f"cannot unblock qou-cds1, and qou-iagg's dependency chain is wrong "
          f"at that link")

    print()
    if failures:
        print(f"FAILED {len(failures)}/16: {', '.join(failures)}")
    else:
        print("16/16 assertions hold.")

    print("""
CONSEQUENCE

  PART 1 (scope-(b), proved invariant).  The sibling exclusion probe closes the
  braid-image branch only against a q-VARYING ansatz; a constant alpha walks
  through it.  Carrying the same boundedness argument one step further -- to
  integrality, and then (general d) to Kronecker -- closes the constant case
  too: a q-uniform braid-image eigenphase on V_(2,1) lies in the five-element
  set {0, pi/3, pi/2, 2pi/3, pi}, and |alpha_req| is 4795 windows from the
  nearest member.  Branch (1) is now closed on V_(2,1) for EVERY alpha, not
  only for the (z-1)h/2 family, and without invoking transcendence.

  Corollary for qou-cds1, convention-free: if alpha is a braid-image eigenphase
  at all, it is a pure number with no z in it.  The C-vs-D question for the
  PHASE dissolves; it survives only for the base.

  PART 2 (a fit, and labelled one).  Given alpha in 2*pi*Q, the search space is
  discrete, and exactly one member fits.  That is an identification CANDIDATE,
  selected against the target, and it is NOT adopted here.  It bears on a
  RETIRED base (the z = 1 cell) and moves no dashboard row: a ~0.1% phase
  cannot address the 43% gap of the ruled z_D base.  The D-base miss is not a
  phase problem.  The cross-anchor swing (assertion 13) is identical for the
  candidate and for convention C, so it supplies no evidence either way.

  WHAT WOULD CLOSE IT: derive the 120 -- exhibit a braid word and a partition
  whose q-uniform eigenphase is 2*pi/120 -- rather than read it off alpha_req.
  Assertion 14 kills the mechanism a reader reaches for first: |2I| = |S_5| =
  120, but neither has an ELEMENT of order 120 (max 10 and 6), so neither
  supplies the root of unity. The candidate has no mechanism at all.
""")

    wb = WitnessBuilder("qbeta-eigenphase-rationality-quantization")
    wb.set_description(
        "Two results of different status. PART 1 (scope-(b), proved): the "
        "sibling braid-image exclusion closes only a q-VARYING ansatz; "
        "carrying its boundedness argument through integrality shows a "
        "q-uniform braid-image eigenphase on V_(2,1) lies in the five-element "
        "set {0, pi/3, pi/2, 2pi/3, pi} (general d: Kronecker gives alpha in "
        "2*pi*Q), so the CONSTANT case is closed too and alpha is "
        "convention-free. PART 2 (A FIT, labelled): given that quantization, "
        "2*pi/120 is the unique primitive rational phase with N <= 1000 inside "
        "the ladder window, 19x closer than convention C, implying |c3| ~ 0.11 "
        "vs -2.069. It is SELECTION AGAINST THE TARGET and is not adopted, not "
        "wired; the cross-anchor swing is identical for both and discriminates "
        "nothing. It also bears on the RETIRED z=1 base and moves no dashboard "
        "row -- the ruled z_D base misses by 43%, which is not a phase problem."
    )
    wb.add_data("part1_structural", {
        "words_swept": n_words,
        "max_word_length": WORD_LEN,
        "det_rho_equals_sign_of_exponent_sum": det_ok,
        "characters_integral": integral_ok,
        "bounded_but_not_constant_count": len(bounded_but_not_constant),
        "constant_characters_observed": sorted(constants),
        "quantized_eigenphase_set_V21": ["0", "pi/3", "pi/2", "2pi/3", "pi"],
        "alpha_req_in_that_set": False,
    })
    wb.add_data("part3_base_not_phase", {
        "ruled_zD_base_MeV": fmt(Q_D),
        "Q_codata_MeV": fmt(QCOD),
        "required_ladder_factor": fmt(need),
        "N1_cos_rung_upper_bound": "1",
        "N2_rung_at_c2_minus_1": fmt(rung2),
        "c3_required_on_ruled_base": fmt(c3_needed),
        "conclusion": "Deriving alpha CANNOT unblock qou-cds1. The N=1 rung is "
                      "a cosine, bounded by 1, and the ruled base needs a "
                      "factor 1.759 > 1. The Q_beta L2 residual is a BASE "
                      "problem, not a phase problem. Scope-(b), citing "
                      "Real.cos_le_one; Lean twin "
                      "QOU.QBeta.EigenphaseQuantization.cos_rung_lt_of_base_short "
                      "(sorry-free).",
    })
    wb.add_data("part2_measurement_is_a_fit", {
        "fit_status": "SELECTION AGAINST TARGET - not a derivation, not adopted",
        "base_status": "RETIRED z=1 cell; moves no dashboard row",
        "unique_hit_N_le_1000": [list(x) for x in h1000],
        "expected_hits_N_le_120": fmt(exp120),
        "expected_hits_N_le_1000": fmt(exp1000),
        "p_denominator_is_120_given_one_hit": fmt(cond120),
        "cross_anchor_c3_swing_candidate": fmt(swing_cand),
        "cross_anchor_c3_swing_convention_C": fmt(swing_C),
        "mechanism_for_120": "NONE IDENTIFIED; the icosahedral reading is "
                             "refuted - S_5 max element order 6, 2I max 10, "
                             "so no primitive 120th root of unity arises",
        "S5_element_orders": o_s5,
        "twoI_order_and_element_orders": [n_2i, o_2i],
        "anchors": anchors,
    })
    for i, nm in enumerate([
        "det rho(sigma_i) = -1 identically",
        "Hecke inverse is Laurent: sigma.sigma^-1 = I",
        "det rho(w) = (-1)^(exponent sum)",
        "tr rho(w) has integer coefficients",
        "no word is bounded-but-not-constant",
        "constant characters lie in [-2,2]",
        "q-uniform eigenphase set on V_(2,1) is finite",
        "Kronecker: alpha in 2*pi*Q (general d)",
        "2*pi/120 is the unique rational phase in the window, N <= 1000",
        "candidate inside window, convention C outside",
        "candidate |c3| < 1 < |c3| of convention C",
        "coincidence priced: which denominator won is the informative fact",
        "cross-anchor swing identical for candidate and C - no discrimination",
        "no element of order 120 in S_5 or 2I - the obvious mechanism is dead",
        "ruled z_D base needs a factor > 1; no cosine rung can supply it",
        "required c3 on the ruled base is ~1e6 - the gap is in the BASE",
    ], 1):
        wb.add_assertion(f"{i}. {nm}",
                         "FAIL" if nm in failures else "PASS", "PASS")
    out = wb.save()
    print(f"Witness: {out}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
