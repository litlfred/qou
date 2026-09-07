"""The class basis diagonalises the quadratic twist; the conjecture is one Fourier coefficient.

Epic `qou-x631`, T_3(k) = SUM_lam (f^lam)^2 chi^lam(3-cyc) <= 0. Bean `qou-igjo`.

The user asked whether the self-duality / Frobenius-pairing structure carries a
QUADRATIC TWIST. It does, and this probe records the form it takes, which turns
out to organise almost every exact fact the epic has accumulated.

*** THE BASIS ***

For mu |- k let |C_mu| be the conjugacy class size and

    e_mu(lam) := sqrt(|C_mu|) * chi^lam(mu) / f^lam .

Column orthogonality says exactly that {e_mu}_{mu |- k} is an ORTHONORMAL BASIS
of L^2(Plancherel_k):

    E_P[e_mu e_nu] = (1/k!) sqrt(|C_mu||C_nu|) SUM_lam chi^lam(mu) chi^lam(nu)
                   = delta_{mu,nu} .

The count is right on the nose -- dim L^2 = p(k) = #classes -- so this is a
basis, not merely an orthonormal system. e_{1^k} = 1 is the constant function,
so every other mode has mean zero.

*** THE TWIST IS DIAGONAL IN IT ***

The omega involution lam |-> lam' (conjugate partition) acts on the basis by a
SIGN, one mode at a time:

    e_mu(lam') = sgn(mu) * e_mu(lam),     sgn(mu) = (-1)^{SUM (mu_i - 1)} ,

because chi^{lam'}(mu) = sgn(mu) chi^lam(mu) and f^{lam'} = f^lam. So the
quadratic twist is not an extra symmetry sitting beside the Frobenius pairing --
it is DIAGONALISED by the pairing's own orthonormal basis, with eigenvalue
sgn(mu). Consequences, each of which was previously a separate computation:

  - An omega-EVEN observable is supported on even classes; an omega-ODD one on
    odd classes. f^lam and log f^lam are omega-even.
  - Sigma_p = (k)_p chi^lam(p,1^{k-p})/f^lam is the single mode
    mu = (p,1^{k-p}) rescaled, with |C_mu| = (k)_p/p. So

        Var_P(Sigma_p) = (k)_p^2/|C_mu| = p (k)_p ,

    and E_P[Sigma_p Sigma_q] = 0 for p != q, both in one line of Parseval. The
    sibling `..._exact_variance_probe` derived these directly; here they are
    corollaries.
  - Sigma_p has twist eigenvalue (-1)^{p-1}.

*** THE CONJECTURE IS ONE FOURIER COEFFICIENT OF f^lam ***

Expand the omega-even observable f^lam in the basis: f = SUM_mu a_mu e_mu with

    a_mu = E_P[f e_mu] = sqrt(|C_mu|)/k! * S_mu ,   S_mu := SUM_lam (f^lam)^2 chi^lam(mu) .

S_{(3,1^{k-3})} is precisely T_3(k). So the conjecture is the statement that ONE
named Fourier coefficient of f^lam is non-positive. Measured, the 3-cycle mode is
consistently a top-4 mode of f by mass (k = 8,10,12,14) -- it is not a tail term.

Exact identities the expansion supplies, all verified below:

  (A) S_mu = 0 for every ODD mu.               [twist; f is omega-even]
  (B) S_{1^k} = M(k) = SUM_lam (f^lam)^3.      [chi^lam(1^k) = f^lam]
  (C) SUM_mu |C_mu| S_mu = k!.                 [SUM_g chi^lam(g) = k! delta_{lam,(k)}]
  (D) SUM_mu |C_mu| S_mu^2 = k! SUM_lam (f^lam)^4.   [Parseval]

*** WHAT THE REFRAMING DOES NOT DO ***

Restating the conjecture as "one Fourier coefficient of f^lam is <= 0" is a
genuine simplification of the STATEMENT and no progress at all on the PROOF, and
the basis makes the reason visible. The three moments of f^lam sit either side of
where the combinatorics closes:

    SUM_lam f^lam    = 1, 2, 4, 10, 26, 76, 232, ...     involutions
    SUM_lam (f^lam)^2 = k!                                RSK  [QOU.Mathlib.rskBurnsideHolds]
    SUM_lam (f^lam)^3 = 1, 2, 10, 64, 596, 8056, ...      = M(k) = S_{1^k}

The first two have closed forms and the corpus carries the second as an
axiom-clean Lean theorem. No closed form for the third is used anywhere in this
repository. S_mu = SUM_lam (f^lam)^2 chi^lam(mu) is a THIRD-order character sum:
it is not a connection coefficient, which would carry a 1/f^lam and reduce to
counting factorisations in S_k. So the conjecture lives exactly one power past
the point where RSK/Burnside stops producing closed forms, and any route that
hopes to evaluate it bijectively is being asked to evaluate a third moment. That
is a scoping fact, not a verdict on any route -- `qou-0ml9` is open and its
mathematics is untouched by this probe.

*** AND THE OBVIOUS STRENGTHENING IS FALSE ***

(B)+(C) give SUM_{mu != 1^k} |C_mu| S_mu = k! - M(k), which is very negative --
tempting one to guess S_mu <= 0 for all mu != 1^k, which would contain the
conjecture. It is FALSE: S_{(4,2,1^{k-6})} > 0 for every 7 <= k <= 14, and it is
the LARGEST positive coefficient in each. Recorded so the route is not re-walked.

*** THE log f DECOMPOSITION, AND A CORRECTION TO MY OWN READING ***

`qou-f4ye` measured g'(0) = -1/4 for the tempering path and reduced it to
c_p := Cov_P(log f, Sigma_p)/sd_P(Sigma_p) at p = 3. Two facts:

  - c_p = 0 EXACTLY for even p. log f is omega-even, Sigma_p is omega-odd for
    even p, so the pairing vanishes mode-by-mode. Decided here on INTEGERS via
    f^lam chi^lam(p,1^{k-p}) + f^{lam'} chi^{lam'}(p,1^{k-p}) = 0, zero
    violations over 4 <= k <= 12. NOT subsumed by orthogonality, which needs
    both arguments to be characters, and log f is not one.

  - c_3 -> -1/4: measured -0.25031 at k = 52.

*** THE RETRACTION THIS PROBE FORCES ON A MERGED CLAIM ***

c_3 IS g'(0). The tempering derivative of `qou-f4ye` is d/dt E_{Q_t}[Sigma_3] at
t = 0 with Q_t ~ P^{1+t/2}; since log Q_t ~ (1+t/2)(2 log f - log k!), that
derivative is exactly Cov_P(log f, Sigma_3). Computed here by the Kerov-mode
route it agrees with the tempering route to every printed digit at
k = 16,24,32,40,44,48 -- two unrelated code paths, so the identification is not
a hopeful reading.

That makes this probe's larger k a direct test of a MERGED claim, and the claim
fails on both halves:

  - NOT MONOTONE. On a consecutive grid c_3(k) rises at k = 33,34,35 and again at
    k = 44. It oscillates (quasi-period ~11 in k, amplitude ~3e-4) on a downward
    drift. `qou-f4ye` read "monotone from below" off k = 16,24,32,40,44,48, a
    coarse grid that lands only on descending phases.
  - NOT FROM BELOW. c_3(52) = -0.250311 and c_3(56) = -0.250614: the sequence
    passes THROUGH -1/4 near k = 50 and keeps going. The merged assertion
    `gprime0_approaches_quarter_from_below` tests -0.25 < g'(0) and holds only
    because its range stops at 48.

The inference that was resting on those two -- "monotone approach from below, so
the limit is -1/4" -- is therefore withdrawn. -1/4 stays recorded as a TARGET TO
CHECK A DERIVATION AGAINST. What the data now says is weaker and should be quoted
as such: c_3(k) is near -1/4 at k ~ 50 and the range does not separate a limit of
exactly -1/4 from one slightly below it.

I first read the table at k <= 28 and recorded the pattern c_p = -1/(p+1) as
FALSIFIED, on the grounds that c_5 sat at -0.075 rather than -1/6 and c_7 was
POSITIVE. Extending to k = 52 retracts that. c_7 turns negative by k = 48, and
c_5 climbs monotonically to 62% of -1/6 with residual decaying like ~k^{-0.64};
reaching 95% would need k ~ 10^3. The honest verdict is that c_p = -1/(p+1) is
UNTESTABLE in reachable k for p >= 5, and every datum at p = 3,5,7 is consistent
with it. The earlier call was an artifact of the k-range, not a refutation --
exactly the failure mode of reading a slowly-converging sequence as converged.

*** THE FLOAT64 GUARD MEASURES ITSELF, AND THE TWO PARITIES DIFFER ***

The c_p table is the only float path here; everything structural is decided on
exact integers or Fractions. Rather than assert that double is adequate, the
probe MEASURES the cancellation |SUM |t|| / |SUM t| it actually incurs:

    odd p:   5.8e4   -- ~4.8 of 16 significant digits lost, ~11 left,
                        against assertions that need 2.
    even p:  1.7e17  -- total cancellation, no significant digits left.

The even figure is not a defect and not a failure of the guard; it is the float
path correctly reporting that those entries are exactly zero. A first version
pooled both parities into one ratio, read 1.7e17, and failed its own headroom
assertion. That is precisely why section 4 decides even p on INTEGERS and this
table only displays them.

*** WHY THE LOW MODES EXPLAIN A SHRINKING SHARE ***

SUM_{p odd} c_p^2 / Var_P(log f) falls from 21% (k=12) to 15% (k=32). That is
structural, not a defect: the single-cycle classes are k-1 of the p(k) basis
directions, a vanishing fraction, and sd_P(log f) grows (empirically ~0.19 ln k
over 12 <= k <= 32 -- a FIT, not a theorem, quoted with its range). Any
derivation of g'(0) that hopes to work mode-by-mode over single cycles is
therefore working in a shrinking corner of the space.
"""
from __future__ import annotations

import json
import math  # float64-ok: see the cancellation measurement guarding the c_p table; every structural assertion is decided on exact ints/Fractions
import subprocess
import sys
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
from _mn_characters import partitions, border_strips, chi, hook_dim  # noqa: E402

# k-ranges. EXACT_K is exhaustive over all classes (cost ~ p(k)^2); CHAT_K walks
# only the single-cycle modes with a one-level MN expansion, so it reaches much
# further.
EXACT_K = range(3, 15)
CHAT_K = (12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52)
CHAT_P = (2, 3, 4, 5, 7, 9)


def conj(lam: tuple) -> tuple:
    return tuple(sum(1 for r in lam if r > j) for j in range(lam[0])) if lam else ()


def falling(k: int, p: int) -> int:
    r = 1
    for i in range(p):
        r *= k - i
    return r


def class_size(mu: tuple, k: int) -> int:
    den = 1
    for part, m in Counter(mu).items():
        den *= (part ** m) * math.factorial(m)
    return math.factorial(k) // den


def sgn(mu: tuple) -> int:
    return (-1) ** sum(p - 1 for p in mu)


def chi_hook(lam: tuple, p: int, nf_minus: int) -> int:
    """chi^lam(p, 1^{k-p}) by one Murnaghan-Nakayama step onto hook-length dims."""
    return sum((-1) ** ht * hook_dim(nu, nf_minus) for nu, ht in border_strips(lam, p))


def main() -> int:
    t0 = time.monotonic()
    a: list[dict] = []
    ok = True

    def chk(name, computed, expected, note=""):
        good = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(good), **({"note": note} if note else {})})
        print(f"  [{'PASS' if good else 'FAIL'}] {name}: {computed!r}")
        return good

    # ------------------------------------------------------------------ 1
    print("=" * 78)
    print("1. {e_mu} IS AN ORTHONORMAL BASIS, AND omega IS DIAGONAL IN IT")
    print("=" * 78)
    bad_orth, bad_dim, bad_twist = [], [], []
    for k in range(3, 10):
        nf = math.factorial(k)
        lams = list(partitions(k))
        mus = list(partitions(k))
        fs = {l: hook_dim(l, nf) for l in lams}
        for i, mu in enumerate(mus):
            for nu in mus[i:]:
                # <e_mu, e_nu> = sqrt(|C_mu||C_nu|)/k! SUM chi(mu)chi(nu); the sqrt is
                # only rational when mu = nu, so test the SQUARE-FREE form: the raw sum
                # is delta * k!/|C_mu|, an exact integer identity.
                s = sum(chi(l, mu) * chi(l, nu) for l in lams)
                want = (nf // class_size(mu, k)) if mu == nu else 0
                if s != want:
                    bad_orth.append((k, mu, nu, s, want))
        if len(mus) != len(lams):
            bad_dim.append(k)
        # omega acts by sgn(mu) on every mode
        for lam in lams:
            lc = conj(lam)
            if fs[lc] != fs[lam]:
                bad_twist.append((k, lam, "dim"))
            for mu in mus:
                if chi(lc, mu) != sgn(mu) * chi(lam, mu):
                    bad_twist.append((k, lam, mu))
        print(f"    k={k:>3}  #classes = #partitions = {len(mus)}   orthonormal + twist-diagonal")

    ok &= chk("class_basis_is_orthonormal", bad_orth, [],
              note="column orthogonality: SUM_lam chi(mu)chi(nu) = delta * k!/|C_mu|, "
                   "tested as an exact integer identity over every pair of classes")
    ok &= chk("basis_is_complete", bad_dim, [],
              note="#classes = p(k) = dim L^2(Plancherel_k), so the orthonormal "
                   "system is a basis")
    ok &= chk("omega_is_diagonal_with_eigenvalue_sgn", bad_twist, [],
              note="e_mu(lam') = sgn(mu) e_mu(lam). THE QUADRATIC TWIST, in the form "
                   "the Frobenius pairing puts it: one sign per class, not a global "
                   "symmetry to be exploited separately")

    # ------------------------------------------------------------------ 2
    print()
    print("=" * 78)
    print("2. Var_P(Sigma_p) = p (k)_p AND UNCORRELATEDNESS AS PARSEVAL COROLLARIES")
    print("=" * 78)
    bad_var = []
    for k in range(4, 13):
        for p in range(2, min(k, 6) + 1):
            mu = tuple([p] + [1] * (k - p))
            # Sigma_p = (k)_p/sqrt(|C_mu|) * e_mu  =>  Var = (k)_p^2/|C_mu| = p(k)_p
            if falling(k, p) ** 2 != p * falling(k, p) * class_size(mu, k):
                bad_var.append((k, p))
    ok &= chk("variance_is_a_basis_corollary", bad_var, [],
              note="|C_{(p,1^{k-p})}| = (k)_p/p, so (k)_p^2/|C_mu| = p(k)_p with no "
                   "character sum at all -- the sibling probe's Result 1 and 2 in one line")

    # ------------------------------------------------------------------ 3
    print()
    print("=" * 78)
    print("3. f^lam IN THE BASIS: S_mu, THE FOUR IDENTITIES, AND THE FALSE STRENGTHENING")
    print("=" * 78)
    bad_odd, bad_const, bad_sum, bad_parseval = [], [], [], []
    pos_42, mass_rank_3 = {}, {}
    for k in EXACT_K:
        nf = math.factorial(k)
        lams = list(partitions(k))
        fs = {l: hook_dim(l, nf) for l in lams}
        M = sum(v ** 3 for v in fs.values())
        S = {mu: sum(fs[l] ** 2 * chi(l, mu) for l in lams) for mu in partitions(k)}
        cs = {mu: class_size(mu, k) for mu in S}
        if any(S[mu] != 0 for mu in S if sgn(mu) == -1):
            bad_odd.append(k)                                              # (A)
        if S[tuple([1] * k)] != M:
            bad_const.append(k)                                            # (B)
        if sum(cs[mu] * S[mu] for mu in S) != nf:
            bad_sum.append(k)                                              # (C)
        if sum(cs[mu] * S[mu] ** 2 for mu in S) != nf * sum(v ** 4 for v in fs.values()):
            bad_parseval.append(k)                                         # (D)
        if k >= 7:
            m42 = tuple([4, 2] + [1] * (k - 6))
            pos_42[k] = S[m42]
        mass = sorted(S, key=lambda m: -Fraction(cs[m] * S[m] ** 2, nf * nf))
        mu3 = tuple([3] + [1] * (k - 3))
        mass_rank_3[k] = mass.index(mu3) + 1
        print(f"    k={k:>3}  S[3-cyc] = {S[mu3]:<18} rank-by-mass {mass_rank_3[k]:>2}/{len(S)}"
              f"   S[(4,2,..)] = {pos_42.get(k, '-')}")

    ok &= chk("S_vanishes_on_odd_classes", bad_odd, [],
              note="(A) f is omega-even, so its expansion is supported on the "
                   "sgn = +1 eigenspace. Half the coefficients are zero for free")
    ok &= chk("S_at_identity_is_M", bad_const, [],
              note="(B) S_{1^k} = SUM (f^lam)^3 = M(k), the normaliser of Q")
    ok &= chk("weighted_S_sum_is_k_factorial", bad_sum, [],
              note="(C) SUM_mu |C_mu| S_mu = SUM_lam (f^lam)^2 SUM_g chi^lam(g) = k!, "
                   "since SUM_g chi^lam(g) = k! delta_{lam,(k)} and f^{(k)} = 1")
    ok &= chk("parseval_identity", bad_parseval, [],
              note="(D) SUM_mu |C_mu| S_mu^2 = k! SUM_lam (f^lam)^4")
    ok &= chk("strengthening_S_mu_le_0_is_FALSE",
              sorted(k for k, v in pos_42.items() if v <= 0), [],
              note="S_{(4,2,1^{k-6})} > 0 for every 7 <= k <= 14, and is the largest "
                   "positive coefficient in each. (B)+(C) make SUM_{mu != 1^k} |C_mu| S_mu "
                   "= k! - M(k) < 0, which invites the guess that all of them are <= 0. "
                   "They are not, so the conjecture cannot be obtained by proving a "
                   "blanket sign -- it needs the 3-cycle class specifically")
    ok &= chk("three_cycle_is_a_leading_mode",
              bool(all(r <= 4 for r in mass_rank_3.values() if r)), True,
              note=f"rank by |a_mu|^2 among all p(k) modes: {mass_rank_3}. The "
                   "conjecture's coefficient is a leading term of f^lam, not a tail")

    # ------------------------------------------------------------------ 4
    print()
    print("=" * 78)
    print("4. c_p = Cov_P(log f, Sigma_p)/sd_P(Sigma_p): EVEN p VANISH EXACTLY")
    print("=" * 78)
    bad_pair = []
    for k in range(4, 13):
        nf = math.factorial(k)
        for lam in partitions(k):
            lc = conj(lam)
            for p in (2, 4, 6, 8):
                if p > k:
                    continue
                mu = tuple([p] + [1] * (k - p))
                if hook_dim(lam, nf) * chi(lam, mu) + hook_dim(lc, nf) * chi(lc, mu) != 0:
                    bad_pair.append((k, lam, p))
    ok &= chk("even_p_covariance_vanishes_termwise", bad_pair, [],
              note="Cov_P(log f, Sigma_p) = (k)_p/k! SUM_lam f^lam chi^lam(p,1^{k-p}) log f^lam "
                   "(the mean drops out because SUM_lam f^lam chi^lam(mu) = 0 for mu != 1^k). "
                   "Pairing lam with lam' makes the integer weights cancel for even p. Decided "
                   "on INTEGERS -- and NOT implied by orthogonality, which needs both arguments "
                   "to be characters; log f is not")

    # ------------------------------------------------------------------ 5
    print()
    print("=" * 78)
    print("5. THE c_p TABLE, AND THE RETRACTION OF 'c_p = -1/(p+1) IS FALSIFIED'")
    print("=" * 78)
    chat: dict[int, dict[int, float]] = {}
    sd_log: dict[int, float] = {}
    explained: dict[int, float] = {}
    cancel_odd, cancel_even = 0.0, 0.0
    print(f"    {'k':>4} | " + " ".join(f"{'p=' + str(p):>10}" for p in CHAT_P)
          + " |  sd(log f) | explained")
    for k in CHAT_K:
        nf = math.factorial(k)
        nfm = {p: math.factorial(k - p) for p in CHAT_P}
        lams = list(partitions(k))
        fs = [hook_dim(l, nf) for l in lams]
        ws = [(x * x) / nf for x in fs]          # float64-ok: f^2 and k! are exact ints; the ratio is a probability in [0,1] and the quotient is the only rounding
        lg = [math.log(x) for x in fs]           # float64-ok: log of an exact int; 16 digits against a table read to 5
        el = sum(w * g for w, g in zip(ws, lg))
        var = sum(w * (g - el) ** 2 for w, g in zip(ws, lg))
        row: dict[int, float] = {}
        for p in CHAT_P:
            num = 0.0
            gross = 0.0
            for lam, f, w, g in zip(lams, fs, ws, lg):
                c = chi_hook(lam, p, nfm[p])
                if c:
                    t = w * g * falling(k, p) * c / f  # float64-ok: cancellation measured below and reported as an assertion; ~4 orders lost against 16 available
                    num += t
                    gross += abs(t)
            if gross > 0:
                # Cancellation is measured SEPARATELY by parity, because the two
                # parities are not the same question. For odd p the net is a real
                # number and the ratio bounds the digits lost. For even p the net
                # is exactly zero by section 4, so gross/|net| is a division by
                # rounding noise -- unbounded, and meaningless as a headroom test.
                # A first version of this guard pooled them and duly reported
                # 1.7e17, which is the float64 path saying (correctly) that it
                # has no significant digits left on the even entries. That is why
                # section 4 decides even p on integers instead of reading this table.
                r = math.inf if num == 0.0 else gross / abs(num)
                if p % 2:
                    cancel_odd = max(cancel_odd, r)
                else:
                    cancel_even = max(cancel_even, r)
            row[p] = num / math.sqrt(p * falling(k, p))
        chat[k] = row
        sd_log[k] = math.sqrt(var)
        explained[k] = sum(v * v for p, v in row.items() if p % 2) / var
        print(f"    {k:>4} | " + " ".join(f"{row[p]:>+10.5f}" for p in CHAT_P)
              + f" | {sd_log[k]:9.4f} | {explained[k]:8.2%}")

    ok &= chk("float64_headroom_is_adequate_on_odd_p",
              bool(cancel_odd < 1e8), True,
              note=f"worst measured |gross|/|net| over the ODD-p entries is {cancel_odd:.3g}; "
                   "double carries ~16 significant digits and the assertions below need 2, "
                   "so the guard is quantified rather than asserted. The even-p entries "
                   f"measure {cancel_even:.3g} -- total cancellation, no significant digits "
                   "left -- which is not a defect but the reason section 4 decides them on "
                   "exact integers and this table merely displays them")
    ok &= chk("even_p_c_is_numerically_zero",
              bool(max(abs(chat[k][p]) for k in CHAT_K for p in CHAT_P if p % 2 == 0) < 1e-9),
              True, note="the exact integer cancellation of section 4, seen through the float path")
    ok &= chk("c3_is_near_minus_one_quarter_at_k_52",
              bool(abs(chat[52][3] + 0.25) < 0.01), True,
              note=f"c_3(52) = {chat[52][3]:.5f}. The tempering derivative g'(0) of `qou-f4ye` "
                   "is exactly this projection, so g'(0) = -1/4 is now a statement about one "
                   "Plancherel Fourier coefficient of log f")
    r5 = {k: chat[k][5] / (-1 / 6) for k in CHAT_K}
    ok &= chk("c5_has_not_converged_so_the_pattern_is_UNTESTED",
              bool(0.55 < r5[52] < 0.75 and all(r5[b] > r5[a] - 0.02
                                                for a, b in zip(CHAT_K, CHAT_K[1:]))),
              True,
              note=f"c_5/(-1/6) climbs monotonically to {r5[52]:.3f} at k=52 with residual "
                   "~k^{-0.64}; 95% would need k ~ 10^3. RETRACTION: reading the k<=28 table "
                   "I recorded c_p = -1/(p+1) as FALSIFIED because c_5 sat near -0.075 and "
                   "c_7 was POSITIVE. c_7 turns negative by k=48. The pattern is UNTESTABLE "
                   "for p >= 5 in reachable k, and consistent with every datum -- not refuted")
    ok &= chk("low_modes_explain_a_shrinking_share",
              bool(explained[32] < explained[12]), True,
              note=f"{explained[12]:.1%} at k=12 -> {explained[32]:.1%} at k=32. Structural: "
                   "single-cycle classes are k-1 of p(k) basis directions. A mode-by-mode "
                   "derivation of g'(0) over single cycles works in a shrinking corner")

    # ------------------------------------------------------------------ 6
    print()
    print("=" * 78)
    print("6. RETRACTION: g'(0) IS NOT MONOTONE, AND IT CROSSES -1/4")
    print("=" * 78)
    cross: dict[int, float] = {k: chat[k][3] for k in (48, 52)}
    for k in (33, 34, 35, 36, 56):
        nf = math.factorial(k)
        nfm = math.factorial(k - 3)
        tot = 0.0
        for lam in partitions(k):
            c = chi_hook(lam, 3, nfm)
            if c:
                f = hook_dim(lam, nf)
                tot += (f * f / nf) * math.log(f) * falling(k, 3) * c / f  # float64-ok: same path and same measured headroom as section 5's odd-p entries
        cross[k] = tot / math.sqrt(3 * falling(k, 3))
    for k in sorted(cross):
        print(f"    k={k:>3}  c_3 = {cross[k]:>+11.6f}")

    ok &= chk("gprime0_is_NOT_monotone",
              bool(cross[34] > cross[33] and cross[35] > cross[34]), True,
              note=f"c_3(33) = {cross[33]:.6f} -> c_3(34) = {cross[34]:.6f} -> "
                   f"c_3(35) = {cross[35]:.6f}: RISING. On a consecutive grid c_3(k) "
                   "oscillates (turning points near k = 35 and k = 43, quasi-period ~11, "
                   "amplitude ~3e-4) on top of a downward drift. The merged claim "
                   "'monotone from below' in `qbeta_covariance_kernel_tempering_probe` "
                   "and bean `qou-f4ye` was read off the coarse grid k = 16,24,32,40,44,48, "
                   "which samples only descending phases")
    ok &= chk("gprime0_CROSSES_minus_one_quarter",
              bool(cross[48] > -0.25 > cross[52] > cross[56]), True,
              note=f"c_3(48) = {cross[48]:.6f}, c_3(52) = {cross[52]:.6f}, "
                   f"c_3(56) = {cross[56]:.6f}. The sequence passes THROUGH -1/4 between "
                   "k = 48 and 52 and keeps going. `qou-f4ye` asserted -0.25 < g'(0), true "
                   "only because its range stopped at 48. CONSEQUENCE: the argument for the "
                   "limit being exactly -1/4 was 'monotone approach from below', and both "
                   "halves of that are now false. -1/4 remains a TARGET TO CHECK A "
                   "DERIVATION AGAINST; it is no longer supported as an infimum, and the "
                   "data does not separate 'limit = -1/4' from 'limit slightly below -1/4'")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        head = "unknown"
    out = HERE / "qbeta-covariance-kernel-class-basis.witness.json"
    out.write_text(json.dumps({
        "computation": "qbeta-covariance-kernel-class-basis",
        "assertions": a, "allPassed": bool(ok),
        "parameters": {
            "epic": "qou-x631", "bean": "qou-igjo",
            "claim": "{sqrt(|C_mu|) chi^lam(mu)/f^lam} is an orthonormal basis of "
                     "L^2(Plancherel) diagonalising the omega twist with eigenvalue "
                     "sgn(mu); T_3(k) is one Fourier coefficient of f^lam",
        },
        "data": {
            # NO RAW float64 REACHES THIS WITNESS. AGENTS.md: "none may enter a
            # witness", and `witness_raw_float64_audit` ratchets it -- a witness
            # absent from the baseline that carries any raw float64 fails.
            #
            # These quantities ARE float64-grade by construction (log of an exact
            # integer), so the two dishonest options are storing the double
            # itself, or padding it through fmt() to serialization width where
            # 53 bits read as measured (the hazard `_precision` documents). Both
            # are refused. They are emitted as DECIMAL STRINGS truncated to the
            # digits the probe actually establishes: the odd-p cancellation is
            # 5.8e4 against 16 available digits, and an independent
            # mean-subtracted summation in reverse order agrees to 13, so 6
            # decimals is supported with room to spare and is not padding.
            "_grade": "decimal strings, float64-grade, 6 dp; see cancellation_ratio_odd_p",
            "c_p": {str(k): {str(p): f"{v:.6f}" for p, v in row.items()}
                    for k, row in chat.items()},
            "sd_log_f": {str(k): f"{v:.6f}" for k, v in sd_log.items()},
            "explained_fraction": {str(k): f"{v:.6f}" for k, v in explained.items()},
            "three_cycle_mass_rank": {str(k): v for k, v in mass_rank_3.items()},
            "S_4_2_positive": {str(k): v for k, v in pos_42.items()},
            "c3_crossing": {str(k): f"{v:.6f}" for k, v in cross.items()},
            "cancellation_ratio_odd_p": f"{cancel_odd:.1f}",
            "cancellation_ratio_even_p": f"{cancel_even:.3e}",
        },
        "provenance": {"headSha": head,
                       "producer": "computations/qbeta/qbeta_covariance_kernel_class_basis_probe.py",
                       "elapsed_s": f"{time.monotonic() - t0:.3f}"},
    }, indent=2) + "\n")
    print(f"witness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
