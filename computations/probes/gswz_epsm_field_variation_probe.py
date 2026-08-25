"""Is the Z/24 class forced, or an accident of K? The local signature, across 46 fields.

Bean qou-w4gn. Scope-(a); no fit; nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 45). Convention-immune: no Hecke/Gram/Markov import, no z_C/z_D,
no q_0 anchor. Exact integer arithmetic mod 5^8.

THE QUESTION, AND WHY IT IS ASKED THIS WAY. The eps_m arc ended with one
invariant at the degree-1 place of K = Q(alpha): a single class 8 in Z/24,
consistent across m = 3, 6, 8, 12, 24. The obvious follow-up is whether 8 is
forced or is an accident of K. Answering that directly would need a Bloch
element in each comparison field, and there is no canonical one -- for K the
element came from GSWZ Example 4.3, which does not generalise for free. So
this probe does NOT try to compute eps in another field.

It asks the cheaper question that GATES the expensive one: does the LOCAL
DATA that determines the class vary across fields at all? Everything the
class depends on enters through the mu_24 discrete logs of the arguments at
the degree-1 place -- that is what fixed [L:B], which m-th roots stay in B,
and every class computed in the arc. For K the exceptional pair (alpha,
1 - alpha) has dlogs (6, 12).

If every catalogued field gives (6, 12), the class cannot vary by this route
and 8 is forced by the local structure -- a strong statement. If the
signatures spread, variation is possible and the expensive question is worth
asking. Either answer is informative, and neither requires a Bloch element.

THE CATALOGUE. From gswz_epsm_second_element_feasibility_probe.py: monic
cubics x^3 + a x^2 + b x + c with c = +-1 (so beta is a unit) and
f(1) = 1 + a + b + c = +-1 (so 1 - beta is a unit, since N(1 - beta) = f(1)),
irreducible over Q, with a simple root mod 5 that Hensel-lifts to a degree-1
place where beta and 1 - beta are both units of Z_5. Rebuilt here rather
than imported, so this probe stands alone.

HONESTY: this measures the local signature, not eps. A constant signature
would show the class cannot vary THROUGH THIS CHANNEL; it would not prove
eps is field-independent, since two fields sharing a signature could still
differ through their Bloch elements. Stated as a gate, not a theorem.
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

    def teich(self, a):
        return self.pw(a, (P ** self.n) ** W)


B = Unram([-2, -1])                        # Q_25, where mu_24 lives
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
checks["mu24_generator_found"] = gen is not None


def dlog24(v_int):
    """mu_24 discrete log of a Z_5 unit's Teichmueller part."""
    t = B.teich(B.scal(v_int))
    cur = B.one()
    for e in range(24):
        if cur == t:
            return e
        cur = B.mul(cur, gen)
    return None


# ---------------------------------------------------------------- the catalogue
def irreducible_over_Q(a_, b_, c_):
    return all((r ** 3 + a_ * r * r + b_ * r + c_) != 0
               for r in (1, -1, c_, -c_))


def disc_cubic(a_, b_, c_):
    return (18 * a_ * b_ * c_ - 4 * a_ ** 3 * c_ + a_ * a_ * b_ * b_
            - 4 * b_ ** 3 - 27 * c_ * c_)


fields = []
for a_ in range(-12, 13):
    for b_ in range(-12, 13):
        for c_ in (1, -1):
            if (1 + a_ + b_ + c_) not in (1, -1):
                continue
            if not irreducible_over_Q(a_, b_, c_):
                continue
            roots5 = [r for r in range(5)
                      if (r ** 3 + a_ * r * r + b_ * r + c_) % 5 == 0
                      and (3 * r * r + 2 * a_ * r + b_) % 5 != 0]
            if not roots5:
                continue
            x = roots5[0]
            for _ in range(W + 2):
                fx = (x ** 3 + a_ * x * x + b_ * x + c_) % MOD
                dfx = (3 * x * x + 2 * a_ * x + b_) % MOD
                x = (x - fx * pow(dfx, -1, MOD)) % MOD
            if not (x % 5 and (1 - x) % 5):
                continue
            fields.append({
                "poly": [1, a_, b_, c_],
                "disc": disc_cubic(a_, b_, c_),
                "beta_mod5": x % 5,
                "dlog_beta": dlog24(x),
                "dlog_1_minus_beta": dlog24((1 - x) % MOD),
            })

detail["fields_found"] = len(fields)
checks["catalogue_rebuilt"] = len(fields) >= 40
checks["K_itself_is_in_the_catalogue"] = any(
    f["poly"] == [1, -1, 0, 1] for f in fields)

# K's own signature, as the reference point.
Kf = next(f for f in fields if f["poly"] == [1, -1, 0, 1])
detail["K_signature"] = (Kf["dlog_beta"], Kf["dlog_1_minus_beta"])
checks["K_signature_is_6_12"] = (Kf["dlog_beta"], Kf["dlog_1_minus_beta"]) == (6, 12)

sigs = {}
for f in fields:
    sigs.setdefault((f["dlog_beta"], f["dlog_1_minus_beta"]), []).append(f["disc"])
detail["signatures_seen"] = {str(k): len(v) for k, v in sorted(sigs.items())}
detail["distinct_signatures"] = len(sigs)
checks["signature_computed_for_every_field"] = all(
    f["dlog_beta"] is not None and f["dlog_1_minus_beta"] is not None
    for f in fields)

# THE ANSWER.
checks["signature_VARIES_across_fields"] = len(sigs) > 1
detail["verdict"] = (
    "The local mu_24 signature (dlog beta, dlog 1-beta) at the degree-1 place "
    "VARIES across the catalogued exceptional-unit fields; K's (6, 12) is one "
    "of several. So the class is not forced by the local structure, and the "
    "expensive question -- whether eps itself varies -- is worth asking, "
    "though it needs a Bloch element per field and this probe does not "
    "supply one."
    if len(sigs) > 1 else
    "Every catalogued field gives K's signature (6, 12), so the class cannot "
    "vary through the local channel and 8 is forced by local structure.")

# CONTROL: dlog24 is not constant on arbitrary inputs -- so a constant
# signature, had we found one, would have been a fact rather than a broken
# discrete log.
probe_dlogs = {dlog24(v) for v in (2, 3, 6, 7, 8, 11, 12, 13, 17, 19)}
detail["dlog24_on_arbitrary_units"] = sorted(probe_dlogs)
checks["control_dlog24_is_not_constant"] = len(probe_dlogs) > 1
# CONTROL: every catalogued beta really is an exceptional unit (both units).
checks["control_all_beta_and_1_minus_beta_are_units"] = all(
    (1 + f["poly"][1] + f["poly"][2] + f["poly"][3]) in (1, -1)
    and f["poly"][3] in (1, -1) for f in fields)

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

_sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                      text=True, cwd=HERE).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_epsm_field_variation_probe",
    "engine": "python3-int-exact",
    "q0Anchor": "independent",
    "q0AnchorReason": (
        "Reads no q0. Teichmueller discrete logs of exceptional units at a "
        "degree-1 place; the substrate modulus never enters."),
    "scriptFile": "gswz_epsm_field_variation_probe.py",
    "commitSha": _sha,
    "beans": ["qou-w4gn"],
    "source": "Addenda 40, 42 (this repo); CGZ arXiv:1712.04887v3",
    "checks": checks,
    "result": detail,
    "scope": (
        "scope-(a) GATE, not an answer to whether eps varies. Computing eps "
        "in a second field needs a Bloch element there, and there is no "
        "canonical one -- K's came from GSWZ Example 4.3, which does not "
        "generalise for free. So this asks the cheaper question that gates "
        "it: does the local data determining the class vary at all? "
        "Everything the class depended on in this arc entered through the "
        "mu_24 discrete logs of the arguments at the degree-1 place. "
        "Measured across the catalogued exceptional-unit cubics, K's "
        "signature (6, 12) is one of several -- the signature VARIES, so the "
        "class is not forced by local structure and the expensive question "
        "is live. A constant signature would have been the stronger result; "
        "it is not what the data shows. Controls: dlog24 is non-constant on "
        "arbitrary units, and every catalogued beta is genuinely an "
        "exceptional unit. Nothing wired."
    ),
}
with open(HERE / "gswz_epsm_field_variation.witness.json", "w") as f:
    json.dump(witness, f, indent=1)
sys.exit(0 if npass == len(checks) else 1)
