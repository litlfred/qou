#!/usr/bin/env python3
"""Anatomy of the z_D Q_beta gap: what the 257x IS, and the three un-done migrations.

# Ref: .beans/qou-99qc--...md          (OWNER RULING 2026-09-08: eps := tr at z_D)
# Ref: docs/audits/2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md
# Ref: computations/qbeta/qbeta-zd-rescore-price.witness.json   (the re-score price)

WHY THIS EXISTS.  The 2026-09-12 re-score moved the dashboard Q_beta row from
1279 ppb to 4.316e+8 ppb, and the owner asked the right question: is that real,
or is some other migration missing?  This answers it by decomposition rather
than by assertion.  It changes nothing.

WHAT IT ESTABLISHES, in order of how much it should change a reader's mind:

1. THE 337,429x IS TWO FACTORS AND ONLY ONE IS THE CONVENTION.  1312x is the
   MISSING c_k LADDER (z=1 base -> z=1 published); 257x is the functional
   (z=1 base -> z_D base).  Base to base, convention D costs 257x.
   Quoting 1279 ppb against 4.316e+8 ppb compares a post-ladder number with a
   base -- the comparison AGENTS.md's own admissibility note forbids, and which
   the re-score PR's table made anyway (corrected).

2. THE GAP IS STRUCTURAL, NOT A BOTCHED SUBSTITUTION.  tr^z(Delta_S) rewrites
   EXACTLY as  h^2/2 - z*h  with h = q - 1/q.  The z term dominates the constant
   by 5.86x, so Q_beta is nearly PROPORTIONAL to z.  Inverting for CODATA gives
   z* = 0.99850 -- 0.15 % from z = 1.  The admissible roots sit +11.17 % and
   -38.64 % away.  So the published 0.168 % was reachable ONLY within 0.15 % of
   z = 1, the coordinate sum, which ConventionDAdmissibleRoots.lean (sorry-free)
   excludes.  The old agreement was a property of an inadmissible functional.

3. THE NORMALISATION IS NOT THE BUG.  Sum_lam y_lam * f^lam = 1 exactly under D
   at n = 3, 6, 9, 12.  A z-dependent missing normalisation was the leading
   alternative hypothesis and it is refuted here.

4. WHERE IT ENTERS BINDING.  z is not a separate knob -- it IS the y_lam, at
   step 6 of the canonical chain (the Frobenius pairing tr_M = Sum y_lam chi_lam).
   Binding is the SAME pairing, B(K) = m_e * Sum_lam y_lam chi^lam Delta_lam over
   partitions of n = 3A, so D's two-row truncation (y_lam = 0 for len >= 3) lands
   directly on it: at A = 4 it keeps 7 of 77 blocks and 0.043 % of the dimension.

5. E_0 HAS TWO LIVE FORMS, differing by 1/(1 - hbar_q^2) = +0.9915 %.  Not the
   answer to the 257x, and a real inconsistency.  Unified per owner instruction
   2026-09-12 -- see qbeta_e0.py.

NOT ESTABLISHED HERE, and left to the beans: whether Delta_S is the canonical
element at all (qou-99qc / PR #7212 -- the gamma-gamma ruling says braid words
are gamma-gamma-selected, not census-selected), and whether the binding channel
has been migrated off convention C at all (it has not -- qou-46ys).
"""
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import sys, pathlib, math

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / p) for p in
                ("computations", "computations/substrate", "tools/qou-substrate/python")]
from mpmath import mp, mpf, nstr

mp.dps = 70
ASSERTS: list[tuple[str, bool, str]] = []
failures = []

def check(label, ok, detail=""):
    print(f"  {'ok  ' if ok else 'FAIL'} {label}" + (f"   {detail}" if detail else ""))
    ASSERTS.append((label, bool(ok), detail))
    if not ok:
        failures.append(label)

import qou_substrate.constants as C
q = mpf(C.Q_50_DIGIT_STR)
me = mpf(str(C.M_E_MEV))
QEXP = mpf(str(C.Q_NEUTRON_MEV))
h = q - 1 / q
hbar = 1 - 1 / q
E0 = _qbeta_e0.order_zero_scaled(me, q)
PPB = mpf(10) ** 9

print("PART 1 - the 337,429x decomposes into ladder x functional")
base_z1 = abs(h**2 / 2 - 1 * h) * E0
base_zD = abs(h**2 / 2 - (q**3 / (q**2 + 1)) * h) * E0
e_base_z1 = abs(base_z1 - QEXP) / QEXP * PPB
e_base_zD = abs(base_zD - QEXP) / QEXP * PPB
pub_z1 = mpf("1279")                       # the laddered figure the dashboard published
ladder = e_base_z1 / pub_z1
functional = e_base_zD / e_base_z1
print(f"       z=1 base      {nstr(e_base_z1,8):>14} ppb")
print(f"       z=1 published {nstr(pub_z1,8):>14} ppb   -> ladder bought {nstr(ladder,6)}x")
print(f"       z_D base      {nstr(e_base_zD,8):>14} ppb   -> functional cost {nstr(functional,6)}x")
check("ladder factor x functional factor reproduces the total",
      abs(ladder * functional / (e_base_zD / pub_z1) - 1) < mpf("1e-6"),
      f"{nstr(ladder,6)} x {nstr(functional,6)} = {nstr(ladder*functional,7)}")
check("the MISSING LADDER is the larger factor", ladder > functional,
      f"ladder {nstr(ladder,6)}x > functional {nstr(functional,6)}x -- so most of the "
      "degradation is 'no ladder yet', not convention D")

print("\nPART 2 - tr^z(Delta_S) = h^2/2 - z*h, exactly; the z term dominates")
for lab, z in (("z=1 (INADMISSIBLE)", mpf(1)), ("z=q (augmentation)", q),
               ("z_D (RULED)", q**3 / (q**2 + 1))):
    tr = h**2 / 2 - z * h
    print(f"       {lab:22} z={nstr(z,9):12} tr={nstr(tr,9):13} "
          f"Q={nstr(abs(tr)*E0,9):12} err={nstr((abs(tr)*E0-QEXP)/QEXP*100,6)}%")
# the exact rewriting, verified against the audit's affine form
aff = lambda z: q**2/2 - q*z - 1 + z/q + 1/(2*q**2)
check("h^2/2 - z*h equals the audit's affine trace form, at both admissible roots",
      all(abs(aff(z) - (h**2/2 - z*h)) < mpf("1e-60")
          for z in (mpf(1), q, q**3/(q**2+1))))
dom = (q**3/(q**2+1)) * h / (h**2/2)
check("the z term dominates the z-independent term", dom > 5,
      f"|z_D*h| / |h^2/2| = {nstr(dom,6)}x -- so Q_beta is nearly proportional to z")

print("\nPART 3 - which z reproduces CODATA, and how far the admissible roots are")
z_star = (h**2 / 2 + QEXP / E0) / h
print(f"       z* = {nstr(z_star,14)}")
for lab, z in (("z = 1 (published)", mpf(1)), ("z = q", q), ("z_D", q**3/(q**2+1))):
    print(f"       {lab:18} {nstr(z,12):14} distance from z*: {nstr((z/z_star-1)*100,6)} %")
check("z* is within 0.2% of the INADMISSIBLE z = 1", abs(z_star - 1) < mpf("0.002"),
      f"z* = {nstr(z_star,10)}, i.e. {nstr((1/z_star-1)*100,4)}% from z=1 -- the published "
      "0.168% was a property of an inadmissible functional, not of the framework")
check("NEITHER admissible root is near z*",
      min(abs(q/z_star - 1), abs((q**3/(q**2+1))/z_star - 1)) > mpf("0.10"),
      f"z=q is {nstr((q/z_star-1)*100,5)}%, z_D is "
      f"{nstr(((q**3/(q**2+1))/z_star-1)*100,5)}% away -- with THIS element no admissible "
      "functional reproduces CODATA (the bean's '20 required levels, zero admissible')")

print("\nPART 4 - the normalisation is NOT the bug: Sum y_lam f^lam = 1 under D")
def parts(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in parts(n - k, k):
            yield (k,) + rest
def f_lam(lam):
    n = sum(lam)
    conj = [sum(1 for p in lam if p > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= row - j + conj[j] - i - 1
    return math.factorial(n) // prod
qint = lambda m: (q**m - q**(-m)) / (q - 1/q)
def y_D(n, lam):
    if len(lam) >= 3:
        return mpf(0)
    k = lam[1] if len(lam) == 2 else 0
    return qint(n - 2*k + 1) / qint(2)**n
worst = max(abs(sum(y_D(3*A, l) * f_lam(l) for l in parts(3*A)) - 1) for A in (1, 2, 3, 4))
check("trace of the identity is 1 at n = 3, 6, 9, 12", worst < mpf("1e-50"),
      f"worst |Sum y_lam f^lam - 1| = {nstr(worst,4)} -- a z-dependent missing "
      "normalisation was the leading alternative hypothesis and is REFUTED")

print("\nPART 5 - where the convention enters BINDING: the two-row truncation")
print(f"       {'A':>2} {'n=3A':>5} {'parts':>6} {'<=2rows':>8} {'killed':>7} {'frac dim kept':>15}")
rows = {}
for A in (1, 2, 3, 4, 5):
    n = 3*A
    P = list(parts(n))
    keep = [l for l in P if len(l) <= 2]
    dk = sum(f_lam(l)**2 for l in keep)
    dt = sum(f_lam(l)**2 for l in P)
    rows[A] = {"n": n, "partitions": len(P), "two_row": len(keep),
               "killed": len(P)-len(keep), "frac_dim_kept": nstr(mpf(dk)/dt, 6)}
    print(f"       {A:>2} {n:>5} {len(P):>6} {len(keep):>8} {len(P)-len(keep):>7} "
          f"{nstr(mpf(dk)/dt,6):>15}")
check("D keeps under 1% of the Wedderburn dimension by A = 4",
      mpf(rows[4]["frac_dim_kept"]) < mpf("0.01"),
      f"A=4 keeps {rows[4]['two_row']} of {rows[4]['partitions']} blocks, "
      f"{rows[4]['frac_dim_kept']} of the dimension -- binding B(K) = m_e * "
      "Sum y_lam chi^lam Delta_lam is the SAME pairing, so this lands on it directly")

print("\nPART 6 - E_0 has two live forms (unified 2026-09-12 per owner instruction)")
ratio = 1 / (1 - hbar**2)
print(f"       E_0 order-zero  = m_e/(q(q-1))            = {nstr(E0,12)} MeV")
print(f"       E_0 tower-summed = that / (1 - hbar_q^2)   = {nstr(E0*ratio,12)} MeV")
print(f"       ratio {nstr(ratio,10)}  = +{nstr((ratio-1)*100,4)} %")
check("the E_0 discrepancy is real but cannot explain the 257x",
      ratio < mpf("1.02") and functional > 100,
      f"E_0 moves the row {nstr((ratio-1)*100,4)}%, the functional moves it "
      f"{nstr(functional,6)}x -- two different orders of magnitude")

print(f"\n=== {len(ASSERTS)-len(failures)}/{len(ASSERTS)} checks ok" if not failures
      else f"\n=== FAILURES: {failures}")

try:
    from witness_base import WitnessBuilder
except ImportError as e:
    print(f"witness skipped: {e}")
    WitnessBuilder = None
if WitnessBuilder is not None:
    w = WitnessBuilder("qbeta-zd-gap-anatomy")
    w.set_description(
        "Anatomy of the z_D Q_beta gap. Decomposes the 337,429x apparent degradation "
        "into 1312x MISSING LADDER and 257x FUNCTIONAL (base to base); shows "
        "tr^z(Delta_S) = h^2/2 - z*h so Q_beta is nearly proportional to z and the "
        "published 0.168% was reachable only within 0.15% of the INADMISSIBLE z = 1; "
        "refutes the missing-normalisation hypothesis (Sum y_lam f^lam = 1 exactly at "
        "n = 3..12); and measures what D's two-row truncation kills in the binding "
        "Frobenius sum (A=4 keeps 0.043% of the dimension). Measures only."
    )
    w.add_data("degradation_factors", {
        "missing_ck_ladder": nstr(ladder, 8), "functional_base_to_base": nstr(functional, 8),
        "product": nstr(ladder*functional, 8),
        "note": "1279 ppb is POST-ladder and 4.316e+8 ppb is a BASE; relating them "
                "directly is the comparison the corpus forbids.",
    })
    w.add_data("z_star_reproducing_codata", nstr(z_star, 16))
    w.add_data("distance_from_z_star_pct", {
        "z=1 (inadmissible)": nstr((1/z_star-1)*100, 8),
        "z=q (augmentation)": nstr((q/z_star-1)*100, 8),
        "z_D (ruled)": nstr(((q**3/(q**2+1))/z_star-1)*100, 8)})
    w.add_data("binding_two_row_truncation", rows)
    w.add_data("E0_forms", {"order_zero_MeV": nstr(E0, 14),
                            "tower_summed_MeV": nstr(E0*ratio, 14),
                            "ratio": nstr(ratio, 12)})
    w.add_data("undone_migrations", {
        "element_is_census_not_gamma_gamma": "qou-99qc / PR #7212",
        "binding_channel_still_convention_C": "qou-46ys",
        "E0_two_live_forms": "unified per owner 2026-09-12, qbeta_e0.py"})
    for label, ok, detail in ASSERTS:
        w.add_assertion(f"{label}{' -- ' + detail if detail else ''}",
                        computed="true" if ok else "false", expected="true")
    w.save()
    print("witness written")
sys.exit(1 if failures else 0)
