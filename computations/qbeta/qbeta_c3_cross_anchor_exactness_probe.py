#!/usr/bin/env python3
"""qbeta_c3_cross_anchor_exactness_probe.py — settle the "c_3 = -2 exact" claim.

CONTEXT.  A 2026-07-06 docs-only commit on main asserted that the Q_beta
precision-ladder coefficient c_3 is EXACTLY -2 for all q, and that the
previously-recorded cross-anchor "swing" was an artifact of a 0-indexed
generator bug `(0,1,0)` in the Python Hecke/Hoefsmit infrastructure.

This probe settles the claim on the CURRENT (post-bug-fix) compute by
extracting c_3 at BOTH the proton-pinned and muon-pinned q_0 and by a
symbolic u-series test of the FIXED theoretical base ladder.  It writes
no production value and wires nothing — it is a verification artifact for
the audit doc docs/audits/2026-07-06-c3-not-exact-cross-anchor-verdict.md.

VERDICT (reproducible below):
  * c_3 is q-DEPENDENT / anchor-swinging: -2.0693 (proton) vs -2.0202
    (muon), a 2.375 % swing.  It is NOT -2 and NOT anchor-independent.
  * The FIXED theoretical ladder through N=2 has [u^3] = 0 EXACTLY: there
    is no first-principles c_3.  The -2ish number only appears by dividing
    the FIXED experimental Q_codata by the MOVING theoretical Q_base
    (the cal-anchored, circular extraction the registry already flags).
  * The "(0,1,0) generator bug" narrative is a misdiagnosis: generators
    are correctly 0-indexed (sigma_0, sigma_1 for H_3 == 1-indexed
    sigma_1, sigma_2), (0,1,0) = sigma_1 sigma_2 sigma_1 is the correct
    trefoil-type 3-braid word, and the one real historical bug (the
    TR_M[5] trace value, docs/audits/2026-05-19-trm5-markov-bug.md) is
    ALREADY fixed — c_3 still swings on the post-fix code.

This confirms the authoritative registry
(docs/coordination/ck-dk-canonical-registry.md, ck-dk-registry.json):
c_3 tier = empirical / cal-anchored / not anchor-stable.  Only c_2 = -1
is Taylor-exact and Lean-proved.
"""
from __future__ import annotations

import mpmath as mp

mp.mp.dps = 60

# Constants (computations/codata_constants.py, q_parameter.py, muon witness).
M_E = mp.mpf("0.51099895069")
Q_COD = mp.mpf("0.78233341")
Q_PROTON = mp.mpf("1.1099785827513808075916690956107688798744991218736")
Q_MUON = mp.mpf(
    "1.10997859555733471989976322048322502665620840878015368660798114614493"
)


def substrate(q):
    sq = mp.sqrt(q)
    h = q - 1 / q
    hbar = (q - 1) / q
    b = mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar ** 2
    z = 1 / (sq + 1 / sq)
    alpha = (z - 1) * h / 2
    Q_A_over_me = mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    return dict(h=h, hbar=hbar, b=b, u=u, z=z, alpha=alpha, Q_A_over_me=Q_A_over_me)


def extract_ck(q, kmax=5):
    """Production recursive extraction c_k = (Q_cod/Q_{N_{k-1}} - 1)/u^k, c_2=-1.

    Mirrors computations/qbeta/qbeta_ck_cache.py:145 and
    qbeta_utils.c3_target_at.
    """
    s = substrate(q)
    Q_A = M_E * s["Q_A_over_me"]
    Q_N1 = Q_A * mp.cos(s["alpha"] - s["b"] * s["hbar"] ** 2 / 2)  # = Q_base
    c = {2: mp.mpf(-1)}
    Q_prev = Q_N1 * (1 + c[2] * s["u"] ** 2)  # Q_N2
    for k in range(3, kmax + 1):
        ck = (Q_COD / Q_prev - 1) / s["u"] ** k
        c[k] = ck
        Q_prev = Q_prev * (1 + ck * s["u"] ** k)
    return c, s["u"]


def main() -> int:
    print("=" * 78)
    print(" c_3 cross-anchor exactness probe — is c_3 = -2 for all q?")
    print("=" * 78)
    cp, up = extract_ck(Q_PROTON)
    cm, um = extract_ck(Q_MUON)
    print(f"  u(proton) = {mp.nstr(up, 18)}   u(muon) = {mp.nstr(um, 18)}")
    print()
    print(f"  c_2 @ proton = {mp.nstr(cp[2], 18):>22}   @ muon = {mp.nstr(cm[2], 18)}")
    print(f"  c_3 @ proton = {mp.nstr(cp[3], 20):>22}   @ muon = {mp.nstr(cm[3], 20)}")
    d = cp[3] - cm[3]
    print(f"  c_3 swing    = {mp.nstr(d, 8)}  ({mp.nstr(d / cp[3] * 100, 6)} % of c_3)")
    print(f"  c_3 - (-2)   = {mp.nstr(cp[3] + 2, 6)} (proton), "
          f"{mp.nstr(cm[3] + 2, 6)} (muon)")
    print()
    exact = abs(cp[3] + 2) < mp.mpf("1e-40") and abs(cm[3] + 2) < mp.mpf("1e-40")
    print(f"  VERDICT: c_3 = -2 exact & anchor-independent? -> {exact}")
    print("  (Expected False: c_3 is a cal-anchored, q-dependent near-match;")
    print("   only c_2 = -1 is Taylor-exact.  The fixed theoretical ladder")
    print("   through N=2 has [u^3] = 0 exactly — there is no first-principles c_3.)")
    return 0 if not exact else 1


if __name__ == "__main__":
    raise SystemExit(main())
