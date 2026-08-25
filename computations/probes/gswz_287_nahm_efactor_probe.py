"""The (287) mismatch vs the Nahm-argument E-factor — third hypothesis class tested, scope-(a) refuted; the (1+x)^a structure and the h^3 residual pinned.

Bean qou-xx9f (third narrowing) + qou-9p9y. Scope-(a); no fit; nothing
wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 20).

CONTEXT. The (287) division mismatch (gswz_psi_section_division_probe)
has the GZ E-factor SIGNATURE (h^1 present, h^2 determined by h^1 —
the B_3 = 0 slot — h^3 residual; Addendum 15). Two argument-classes
were already refuted on the digits: the (275) roots of unity under a
uniform Bernoulli shift, and any parallel 5-unit scalar (Addendum 16;
bean xx9f second narrowing). The surviving idea was that the E-tail
arguments are the NAHM z-data of the (281) bracket
f_1^{5_2} = <e^w psi_{0,z,1}(w,x)^3>_{3a-2}/sqrt(delta).

NEW EXACT INPUT (this probe): the 5_2 Nahm/saddle variable of the
cube-potential state integral satisfies (1-z)^3 = z^2, i.e.
z^3 - 2z^2 + 3z - 1 = 0 (discriminant -23, same cubic field), and its
K-rational root IS the tetrahedron shape z_1 = 1 - alpha^2 (verified
exactly here). So the Nahm-argument set is {zeta_6^t z_1, zeta_6^t
z_2} (z_2 the second shape; zeta_6 = the GZ Z-shift e(-5/6) = zeta_6
at c = 1), with structural weights from the psi^3 / shape
multiplicities.

WHAT THIS PROBE ESTABLISHES (all exact, (Z/5^8)[alpha] arithmetic):

1. RECONSTRUCTION: e_1, e_2, e_3 of the multiplicative mismatch
   printed = (1 + e_1 x + e_2 x^2 + e_3 x^3) * computed, from the
   printed (287) digits and the Psi-division quotient, with the digit
   caps inherited from the printed (274) coefficients (x^1/x^2 mod 25
   with const mod 5; x^3 mod 5).
2. STRUCTURE CONFIRMED: e_2 == a(a-1)/2 with a = e_1 EXACTLY on all
   available digits — the mismatch is (1+x)^a * (1 + b x^3 + ...) to
   this order, the exponential/E-factor shape with an empty h^2 slot
   (B_3 = 0). This re-derives the Addendum-16 "x^2 confirmed mod 25"
   through an independent reconstruction.
3. RESIDUAL PINNED: b = mu_3 = e_3 - a(a-1)(a-2)/6 is NONZERO mod 5
   (digits recorded) — the normalization is a genuine series, not a
   single power (1+x)^a.
4. SCANNER SENSITIVITY CONTROL: a synthetic mismatch built from a
   known Nahm candidate (weights (2,1), t = 0, sign +) is planted and
   the scanner must find EXACTLY that candidate — an always-empty
   scanner cannot masquerade as a refutation.
5. THE TEST: C_1 = +-(n_1 Li_0(zeta_6^t z_1) + n_2 Li_0(zeta_6^t z_2))
   over t in 0..5, weights (n_1,n_2) in {(3,0),(2,1),(1,2),(0,3),
   (1,0),(0,1),(1,1)}, both signs — 84 zero-free-parameter candidates;
   the E-factor implies a = -C_1/12. RESULT: NO candidate matches the
   e_1 digits. Scope-(a): the Nahm-argument shifted-tail E-factor,
   with these Li_0 arguments and structural weights, ALONE and AS-IS,
   does not reproduce the (287) mismatch. (Any h^1 survivor would then
   have faced -C_3 == 720 mu_3 at h^3 with the SAME weights — the
   falsifier stage, unreachable this run.)

WHAT REMAINS (honest scope): three argument-classes are now excluded
on digits — (275) roots of unity, parallel scalars, and Nahm z-data
under Li_0 with structural weights. Remaining candidates: the m = 5
fibre reading of the printed subscript (f_5 vs f_1, awaiting the
owner's pdf eyeball), or an E-factor with Bernoulli-polynomial-
weighted MIXED arguments (GZ (8.7) at c > 1) which requires the
unprinted higher-fibre data to constrain without fitting.
"""

import json
import os
import sys
import tempfile

import itertools

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- run the Psi-division probe in-process for its validated
# machinery + quotient coefficients (cwd redirected so its witness
# lands in a temp dir, not over the committed one) --------------------
ns = {"__name__": "psi_probe"}
src = open(os.path.join(HERE, "gswz_psi_section_division_probe.py")).read()
_cwd = os.getcwd()
_tmp = tempfile.mkdtemp(prefix="psi287_")
os.makedirs(os.path.join(_tmp, "computations", "probes"), exist_ok=True)
os.chdir(_tmp)
try:
    exec(compile(src, "gswz_psi_section_division_probe.py", "exec"), ns)
except SystemExit:
    pass
finally:
    os.chdir(_cwd)

MOD = ns["MOD"]
T1, T2, T3 = ns["T1"], ns["T2"], ns["T3"]
mul, add, sub, smul, pw, rat = (
    ns["mul"], ns["add"], ns["sub"], ns["smul"], ns["pw"], ns["rat"]
)
Z24 = ns["Z24"]

checks = {}
detail = {}
checks["psi_probe_green_and_T3_available"] = (
    all(ns["checks"].values()) and T3 is not None
)

one = [1, 0, 0]
alpha = [0, 1, 0]


def inv_ring(u):
    """Inverse in (Z/5^8)[alpha]/(alpha^3-alpha^2+1) by Gaussian
    elimination on the multiplication matrix (unit iff det is a
    5-unit; asserts via pivot search)."""
    cols = []
    for i in range(3):
        e = [0, 0, 0]
        e[i] = 1
        cols.append(mul(u, e))
    A = [[cols[j][i] % MOD for j in range(3)] + [1 if i == 0 else 0]
         for i in range(3)]
    for c in range(3):
        piv = next(r for r in range(c, 3) if A[r][c] % 5 != 0)
        A[c], A[piv] = A[piv], A[c]
        iv = pow(A[c][c], -1, MOD)
        A[c] = [(x * iv) % MOD for x in A[c]]
        for r in range(3):
            if r != c and A[r][c]:
                f = A[r][c]
                A[r] = [(x - f * y) % MOD for x, y in zip(A[r], A[c])]
    return [A[0][3], A[1][3], A[2][3]]


def li0(w):
    return mul(w, inv_ring(sub(one, w)))


def lim2(w):
    return mul(mul(w, add(one, w)), pw(inv_ring(sub(one, w)), 3))


# ---- Nahm data: (1-z)^3 = z^2 and z = z_1 exactly --------------------
z1 = sub(one, mul(alpha, alpha))
z2 = add(sub(mul(z1, z1), z1), [2, 0, 0])
nahm_lhs = pw(sub(one, z1), 3)
nahm_rhs = mul(z1, z1)
checks["nahm_saddle_z1_exact"] = nahm_lhs == nahm_rhs
zeta6 = pw(Z24, 4)

# ---- mismatch reconstruction ----------------------------------------
printed = [ns["printed_x1"], ns["printed_x2"], ns["printed_x3"]]


def p_val(pr):
    f = lambda d: sum(x * 5**i for i, x in enumerate(d))
    return [f(pr["const"]), f(pr["alpha"]), f(pr["alpha2"])]


P1, P2, P3 = map(p_val, printed)
e1 = sub(P1, T1)
e2 = sub(sub(P2, T2), mul(e1, T1))
e3 = sub(sub(sub(P3, T3), mul(e1, T2)), mul(e2, T1))

CAP1 = (1, 2, 2)   # const digit cap 1 (single printed digit), alpha/alpha2 cap 2
CAP2 = (2, 2, 2)
CAP3 = (1, 1, 1)


def capred(v, caps):
    return [x % (5**c) for x, c in zip(v, caps)]


a = e1
checks["h2_consistency_1px_pow_a"] = capred(
    sub(e2, mul(mul(rat(1, 2), a), sub(a, one))), CAP2
) == [0, 0, 0]
mu3 = sub(e3, mul(mul(mul(rat(1, 6), a), sub(a, one)), sub(a, [2, 0, 0])))
checks["mu3_residual_nonzero_mod5"] = capred(mu3, CAP3) != [0, 0, 0]
detail["e1_digits_capped"] = capred(e1, CAP1)
detail["mu3_digits_mod5"] = capred(mu3, CAP3)

# ---- the scan --------------------------------------------------------
WEIGHTS = [(3, 0), (2, 1), (1, 2), (0, 3), (1, 0), (0, 1), (1, 1)]


def scan(target_e1, cap):
    surv = []
    for t in range(6):
        tw = pw(zeta6, t) if t else one
        w1, w2 = mul(tw, z1), mul(tw, z2)
        L0 = (li0(w1), li0(w2))
        for (n1, n2), s in itertools.product(WEIGHTS, (1, -1)):
            C1 = smul(s, add(smul(n1, L0[0]), smul(n2, L0[1])))
            E1 = mul(rat(-1, 12), C1)
            if capred(sub(E1, target_e1), cap) == [0, 0, 0]:
                surv.append((t, (n1, n2), s))
    return surv


# (4) sensitivity control: plant a known candidate, scanner must find it
planted = mul(rat(-1, 12), add(smul(2, li0(z1)), smul(1, li0(z2))))
found = scan(planted, CAP1)
checks["scanner_finds_planted_candidate"] = (0, (2, 1), 1) in found
detail["planted_scan_hits"] = [f"t={t} n={n} s={s}" for t, n, s in found]

# (5) the real scan
surv = scan(e1, CAP1)
checks["nahm_grid_no_h1_survivor"] = surv == []
detail["real_scan_hits"] = [f"t={t} n={n} s={s}" for t, n, s in surv]
detail["grid_size"] = 6 * len(WEIGHTS) * 2
# had there been survivors, each would face -C_3 == 720*mu_3 (same
# weights, Li_{-2}) — recorded for the next argument-class attempt
detail["h3_falsifier"] = "-C_3 == 720*mu_3 mod 25 with Li_-2, same (t,n,s)"

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

import subprocess

_sha = subprocess.run(
    ["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=HERE
).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_287_nahm_efactor_probe",
    "engine": "python3-int-exact",
    "scriptFile": "gswz_287_nahm_efactor_probe.py",
    "commitSha": _sha,
    "beans": ["qou-xx9f", "qou-9p9y"],
    "source": (
        "GSWZ arXiv:2412.04241v2 eqns (270), (281), (287) "
        "(library/arxiv-2412.04241v2/2412.04241v2.pdf); GZ SIGMA 20 (2024) 055 §8.1-8.2 "
        "eqns (8.7)-(8.8) (library/arxiv-2111.06645v3/2111.06645v3.pdf)"
    ),
    "checks": checks,
    "result": detail,
    "scope": (
        "scope-(a): the Nahm-argument shifted-tail E-factor (Li_0 on "
        "{zeta_6^t z_1, zeta_6^t z_2}, structural weights, both signs) "
        "ALONE and AS-IS does not reproduce the (287) h^1 mismatch — "
        "third argument-class excluded on digits, with a planted-"
        "candidate sensitivity control proving the scanner detects "
        "true matches. POSITIVE results: the Nahm saddle (1-z)^3 = z^2 "
        "has K-rational root exactly z_1 = 1-alpha^2; the mismatch has "
        "the exact (1+x)^a structure at h^2 (B_3 = 0 E-signature); the "
        "h^3 residual mu_3 is pinned mod 5. Remaining candidates: the "
        "f_5 fibre reading, or Bernoulli-weighted mixed arguments "
        "(GZ (8.7) c > 1) needing unprinted data"
    ),
}
with open(
    os.path.join(HERE, "gswz_287_nahm_efactor.witness.json"), "w"
) as f:
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
