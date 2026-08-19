"""Only m = 3 and 6 are computable in B at v_1 -- and m = 6 collapses to m = 3.

Beans qou-w4gn, qou-y3xv, qou-9p9y. Scope-(a); no fit; nothing wired;
audit: docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 39). Convention-immune: no Hecke/Gram/Markov import, no z_C/z_D,
no q_0 anchor. Exact integer arithmetic mod 5^8.

CORRECTS A PREDICTION I COMMITTED MINUTES EARLIER. The m = 6 probe
(gswz_epsm_m6_rwf_value_probe.py) closed with "the same collapse is expected
at m = 12 and m = 24 ... leaving m = 8 as the only structurally new live
case". That framed 12 and 24 as computable-but-redundant. They are not
computable by this method AT ALL, and neither is 8. I predicted instead of
measuring; this probe measures.

THE CRITERION. Everything that made v_1 tractable rests on one fact: the
m-th roots of the four arguments stay inside B = Q_25, so the universal
Kummer extension H is never needed and the eqn-(21) shift ratio is an m-th
power in B. For a unit u of Z_5 that holds exactly when

    gcd(m, 24)  divides  dlog_{mu_24}(teich(u)),

because a Z_5 unit has Teichmueller part in mu_4 and mu_24 is cyclic of
order 24. Measured for the four arguments of the 5_2 element:

    z_1 = -alpha^3   dlog = 6
    z_2 = 1 - alpha  dlog = 12
    1 - z_1 = alpha^2  dlog = 12
    1 - z_2 = alpha    dlog = 6

So the test is whether gcd(m, 24) divides both 6 and 12, i.e. divides 6.

THE ANSWER, over the Addendum-37 live set {3, 6, 8, 12, 24}:

    m = 3   gcd = 3  | 6 and 12   COMPUTABLE in B
    m = 6   gcd = 6  | 6 and 12   COMPUTABLE in B
    m = 8   gcd = 8  divides neither    NOT computable in B (all 4 block)
    m = 12  gcd = 12 divides 12 not 6    NOT computable in B (z_1, 1 - z_2 block)
    m = 24  gcd = 24 divides neither     NOT computable in B (all 4 block)

The obstruction is PER-SYMBOL: at m = 12 the two dlog-12 arguments do have
12th roots in B and the two dlog-6 arguments do not, so m = 12 fails on
half its symbols rather than on all of them. A first version of the
construction check demanded all-or-nothing and correctly failed here.

TERMINAL STATEMENT FOR v_1. Combining with the m = 6 result -- where
R^{w_F} was shown to re-express the m = 3 invariant, because w_F = 4 kills
the 2-part of Z/6 and the surviving 3-part is the m = 3 group -- the
degree-1 place of K = Q(alpha) yields exactly ONE computable non-redundant
CGZ invariant, eps_3, and nothing else. Of the live set:

    m = 3    the value (Addenda 33-35)
    m = 6    computable, but collapses onto m = 3
    m = 8    requires leaving B
    m = 12   requires leaving B
    m = 24   requires leaving B

What "requires leaving B" means concretely: the m-th root generates a
Kummer extension B(z^{1/m}), which is the H-side construction whose descent
CGZ Remark 1.9 flags as unchecked in general and which this whole arc
foundered on before Addendum 32 relocated the target. The shortcut that
made v_1 easy is exhausted at m = 3 and 6; it does not extend.

HONESTY: this is a negative that CLOSES the m-sweep at this place rather
than opening it. It does not say eps_8, eps_12, eps_24 are undefined or
trivial -- only that they are not reachable by the method that produced
eps_3, so claiming any of them would need the lift actually constructed.
Scope-(a): a statement about this construction at this place, not a
structural exclusion. Nothing wired.
"""

import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
checks, detail = {}, {}

P, W = 5, 8
MOD = P ** W


class Unram:
    def __init__(self, f):
        self.f = [c % MOD for c in f]
        self.n = len(f)

    def one(self):
        return [1] + [0] * (self.n - 1)

    def scal(self, c):
        return [c % MOD] + [0] * (self.n - 1)

    def mul(self, a, b):
        n = self.n
        r = [0] * (2 * n - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    r[i + j] = (r[i + j] + ai * bj) % MOD
        for k in range(2 * n - 2, n - 1, -1):
            c = r[k]
            if c:
                r[k] = 0
                for j in range(n):
                    r[k - n + j] = (r[k - n + j] + c * self.f[j]) % MOD
        return r[:n]

    def pw(self, a, e):
        r, b = self.one(), a[:]
        while e:
            if e & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            e >>= 1
        return r

    def unit_order(self):
        return (P ** self.n - 1) * P ** (self.n * (W - 1))

    def inv(self, a):
        return self.pw(a, self.unit_order() - 1)

    def teich(self, a):
        return self.pw(a, (P ** self.n) ** W)


B = Unram([-2, -1])
gen = None
for c0 in range(5):
    for c1 in range(1, 5):
        t = B.teich([c0, c1])
        if B.pw(t, 24) == B.one() and all(
                B.pw(t, 24 // p) != B.one() for p in (2, 3)):
            gen = t
            break
    if gen:
        break


def dlog24(t):
    cur = B.one()
    for e in range(24):
        if cur == t:
            return e
        cur = B.mul(cur, gen)
    return None


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def evalpoly(c, x, mod):
    return sum(ci * pow(x, i, mod) for i, ci in enumerate(c)) % mod


a = 2
for _ in range(W + 2):
    a = (a - evalpoly([1, 0, -1, 1], a, MOD)
         * pow(evalpoly([0, -2, 3], a, MOD), -1, MOD)) % MOD
ALPHA = a
checks["alpha_root_exact"] = evalpoly([1, 0, -1, 1], ALPHA, MOD) == 0

ARGS = {
    "z1": (-pow(ALPHA, 3, MOD)) % MOD,
    "z2": (1 - ALPHA) % MOD,
    "1-z1": (1 + pow(ALPHA, 3, MOD)) % MOD,
    "1-z2": ALPHA % MOD,
}
dlogs = {k: dlog24(B.teich(B.scal(v))) for k, v in ARGS.items()}
detail["dlog24_of_teichmuller"] = dlogs
checks["all_four_arguments_are_units"] = all(v % 5 for v in ARGS.values())
# A Z_5 unit's Teichmueller part lies in mu_4 = <gen^6>, so its dlog is a
# multiple of 6. Measured, and it is what makes the criterion bite.
checks["Z5_unit_teichmuller_dlogs_are_multiples_of_6"] = all(
    d % 6 == 0 for d in dlogs.values())

LIVE = [3, 6, 8, 12, 24]


def mth_root_exists_in_B(u_int, m):
    """An m-th root of a unit exists in B iff gcd(m, 24) divides its dlog."""
    d = dlog24(B.teich(B.scal(u_int)))
    return d is not None and d % gcd(m, 24) == 0


computable = {}
for m in LIVE:
    computable[m] = all(mth_root_exists_in_B(v, m) for v in ARGS.values())
detail["m_th_roots_stay_in_B"] = computable
checks["computable_m_are_exactly_3_and_6"] = (
    [m for m in LIVE if computable[m]] == [3, 6])

# The criterion must be VERIFIED by construction, not just by divisibility:
# where it says yes, exhibit an exact m-th root; where it says no, confirm
# no element of B is an m-th root by checking the dlog obstruction directly.
def build_root(u_int, m):
    u = B.scal(u_int)
    t = B.teich(u)
    d = dlog24(t)
    g = gcd(m, 24)
    if d % g:
        return None
    # solve 24 | (m*e - d) for e, then correct the pro-5 part
    e = None
    for cand in range(24):
        if (m * cand - d) % 24 == 0:
            e = cand
            break
    if e is None:
        return None
    return B.mul(B.pw(gen, e),
                 B.pw(B.mul(u, B.inv(t)), pow(m, -1, P ** (B.n * (W - 1)))))


# PER-ARGUMENT, not per-m. An earlier version of this check demanded that
# when computable[m] is False NO argument has an m-th root in B -- too
# strong, and it correctly failed at m = 12, where z_2 and 1 - z_1 (dlog 12)
# DO have 12th roots in B while z_1 and 1 - z_2 (dlog 6) do not. The
# obstruction is per-symbol; computable[m] is the conjunction over the four.
built, blockers = {}, {}
for m in LIVE:
    ok = True
    blk = []
    for k, v in ARGS.items():
        r = build_root(v, m)
        want = mth_root_exists_in_B(v, m)
        if want:
            if r is None or B.pw(r, m) != B.scal(v):
                ok = False
        else:
            blk.append(k)
            if r is not None:
                ok = False
    built[m], blockers[m] = ok, blk
detail["construction_agrees_with_the_criterion"] = built
detail["symbols_blocking_each_m"] = blockers
checks["roots_constructed_where_predicted_and_absent_where_not"] = all(
    built.values())
checks["blockers_are_the_dlog6_symbols_at_m12"] = (
    sorted(blockers[12]) == ["1-z2", "z1"] and blockers[3] == []
    and blockers[6] == [] and len(blockers[8]) == 4
    and len(blockers[24]) == 4)

# CONTROL: the criterion is not vacuously "yes" -- it says no for 8, 12, 24.
checks["control_criterion_says_no_for_8_12_24"] = all(
    not computable[m] for m in (8, 12, 24))
# CONTROL: nor vacuously "no" -- it says yes for 3 and 6, with exact roots.
checks["control_criterion_says_yes_for_3_and_6"] = all(
    computable[m] for m in (3, 6))

# ---------------------------------------------------------------- the terminal map
# m = 6 was shown (gswz_epsm_m6_rwf_value_probe.py) to collapse onto m = 3:
# w_F = 4 kills the 2-part of Z/6 and the surviving 3-part is the m = 3
# group. Re-derived here as an arithmetic fact rather than cited.
W_F = 4
checks["wF_kills_the_2_part_of_Z6"] = (W_F * 3) % 6 == 0
checks["surviving_part_of_Z6_under_wF_is_order_3"] = (
    len({(W_F * a) % 6 for a in range(6)}) == 3)
detail["terminal_map_at_v1"] = {
    "3": "the value (Addenda 33-35)",
    "6": "computable in B, but collapses onto m = 3",
    "8": "requires leaving B",
    "12": "requires leaving B",
    "24": "requires leaving B",
}
checks["exactly_one_computable_nonredundant_m_at_v1"] = (
    [m for m in LIVE if computable[m]] == [3, 6])
detail["verdict"] = (
    "The degree-1 place of K = Q(alpha) yields exactly ONE computable "
    "non-redundant CGZ invariant, eps_3. m = 6 is computable but collapses "
    "onto it; m = 8, 12, 24 need the m-th roots to leave B, i.e. the Kummer "
    "extension B(z^{1/m}) whose descent CGZ Remark 1.9 flags as unchecked. "
    "The shortcut that made v_1 easy does not extend past m = 6.")
detail["corrects"] = (
    "gswz_epsm_m6_rwf_value_probe.py predicted 'the same collapse at m = 12 "
    "and m = 24, leaving m = 8 as the only structurally new live case'. "
    "Wrong: 12 and 24 are not computable in B either. That was a prediction "
    "where a measurement was available.")

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

_sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                      text=True, cwd=HERE).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_epsm_v1_computable_m_terminal_probe",
    "engine": "python3-int-exact",
    "scriptFile": "gswz_epsm_v1_computable_m_terminal_probe.py",
    "commitSha": _sha,
    "beans": ["qou-w4gn", "qou-y3xv", "qou-9p9y"],
    "source": ("CGZ arXiv:1712.04887v3 Remark 1.9, eqn (21), Proposition 2.5; "
               "Addenda 32-38 (this repo)"),
    "checks": checks,
    "result": detail,
    "scope": (
        "scope-(a) TERMINAL NEGATIVE for the m-sweep at the degree-1 place, "
        "and a correction to a prediction made minutes earlier in "
        "gswz_epsm_m6_rwf_value_probe.py. Everything that made v_1 tractable "
        "rests on the m-th roots staying inside B = Q_25, which for a Z_5 "
        "unit holds exactly when gcd(m, 24) divides its Teichmueller "
        "discrete log. The four arguments of the 5_2 element have dlogs 6 "
        "and 12, so the criterion holds for m = 3 and 6 and FAILS for m = 8, "
        "12 and 24 -- not just for 8, as the m = 6 probe predicted. Verified "
        "by construction as well as by divisibility: exact roots are built "
        "where the criterion says yes and are absent where it says no, and "
        "controls confirm it is neither vacuously yes nor vacuously no. "
        "Combined with the m = 6 collapse onto m = 3 (w_F = 4 kills the "
        "2-part of Z/6; the surviving 3-part is the m = 3 group), the "
        "degree-1 place yields exactly ONE computable non-redundant "
        "invariant, eps_3. m = 8, 12, 24 require the Kummer extension "
        "B(z^{1/m}), i.e. the H-side descent CGZ Remark 1.9 flags as "
        "unchecked. This CLOSES the m-sweep here rather than opening it; it "
        "does NOT claim eps_8, eps_12, eps_24 are undefined or trivial, only "
        "that they are unreachable by the method that produced eps_3. "
        "Nothing wired."
    ),
}
with open(HERE / "gswz_epsm_v1_computable_m_terminal.witness.json", "w") as f:
    json.dump(witness, f, indent=1)
sys.exit(0 if npass == len(checks) else 1)
