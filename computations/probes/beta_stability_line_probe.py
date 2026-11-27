#!/usr/bin/env python3
"""
beta_stability_line_probe.py -- accuracy epic qou-myts, vector 8 follow-up.
Owner card 2026-11-27 ("Which derivation should this thread take on next?"):
"Stability line Z*(A)".

PRE-REGISTRATION (written before the first run; nothing below is tuned)
-----------------------------------------------------------------------
Model Q-value for beta-minus of (Z, N), from the mass table's ruled-law masses:
    Q_model(Z, N) = m_ruled(Z, N) - m_ruled(Z+1, N-1) - m_e
m_ruled already carries whatever binding terms production has wired on top of
the ruled log law (T(T+1) twist, Coulomb E_EM). This probe adds NO term itself.

SCORE 1 -- decay direction, two-sided. Over EVERY measured (non-estimated) AME2020
beta-minus Q-value with |Q_exp| > 10 keV, count sign(Q_model) == sign(Q_exp).
Scorecard Table 3.4b keeps only Q_exp > 0.01 MeV, so it can never see a model
that calls every nucleus beta-minus unstable. This score is the two-sided check.

SCORE 2 -- the line itself. For each A, Z*_model(A) is the Z where Q_model changes
sign from + to - going up in Z along the isobar (the model's most stable isobar
member); Z*_exp(A) is the same from Q_exp. Report mean |Z*_model - Z*_exp| over
the A where both exist and each has exactly one sign change.

Comparison data (AME2020) are used ONLY for the reported scores, never as input.
Scope (a): a statement about the current production construction.

Closed form, for reading the result (not used in the computation):
with B_twist = -kappa*T(T+1), T = |N-Z|/2, and E_EM = eps*Z(Z-1)/2, one
beta-minus step at d = N - Z >= 2 gives Q = (m_n-m_p) - m_e + kappa*d - eps*Z,
so the line is d* = (eps*Z - (m_n-m_p) + m_e)/kappa.
"""
from __future__ import annotations

import collections
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
from _precision import set_compute_dps  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
except ImportError:  # pragma: no cover
    WitnessBuilder = None

set_compute_dps()
M_E = mp.mpf("0.51099895069")
THRESH = mp.mpf("0.010")  # MeV


# Most complete ruled-law mass first: + Coulomb (PR #9691, conditional on the
# CAL-3 length r_rms = sqrt(3/5)*lambda_pi*A^(1/3)), then the ruled law alone.
MASS_KEYS = ("m_ruled_em_MeV", "m_ruled_MeV", "m_symbolic_MeV")


def _mass_key(row):
    for k in MASS_KEYS:
        if row.get(k):
            return k
    return None


def main() -> int:
    rows = json.loads((COMP / "mass-table-comprehensive.witness.json").read_text())["data"]["rows"]
    by = {(r["Z"], r["N"]): r for r in rows}
    wired = sorted(k for k in ("B_twist_MeV", "E_EM_MeV") if any(k in r for r in rows[:50]))
    ame = json.loads((COMP / "data" / "ame2020.json").read_text())
    ame = ame if isinstance(ame, list) else next(v for v in ame.values() if isinstance(v, list))

    pairs = []  # (A, Z, q_model, q_exp)
    for e in ame:
        if e.get("beta_decay_energy_estimated") or e.get("beta_decay_energy_keV") is None:
            continue
        z, n = int(e["Z"]), int(e["N"])
        if n < 1:
            continue
        q_exp = mp.mpf(str(e["beta_decay_energy_keV"])) / 1000
        a, b = by.get((z, n)), by.get((z + 1, n - 1))
        if not a or not b:
            continue
        ka, kb = _mass_key(a), _mass_key(b)
        if ka is None or kb is None:
            continue
        q_model = mp.mpf(a[ka]) - mp.mpf(b[kb]) - M_E
        pairs.append((z + n, z, q_model, q_exp))

    # PREVIEW (clearly separate; NOT production): the two sibling terms as their
    # threads state them, added here only if m_ruled does not carry them yet.
    #   twist  B_twist = -kappa*T(T+1), kappa = 2*alpha*ln q, T = |N-Z|/2  (PR #9685)
    #   EM     E_EM = eps(A)*Z(Z-1)/2, eps(A) = 1.36749378*A^(-1/3) MeV    (PR #9691,
    #          conditional: CAL-3 length r_rms = sqrt(3/5)*lambda_pi*A^(1/3))
    from q_parameter import q_at
    q = q_at(60)
    alpha = M_E * 8 * mp.catalan
    kappa = 2 * alpha * mp.log(q)

    def t_t1(Z, N):
        T = mp.mpf(abs(N - Z)) / 2
        return T * (T + 1)

    def preview_shift(A, z):
        n = A - z
        sh = mp.mpf(0)
        if "B_twist_MeV" not in wired:  # Q = ... - B_parent + B_daughter
            sh += kappa * t_t1(z, n) - kappa * t_t1(z + 1, n - 1)
        if "E_EM_MeV" not in wired:
            eps = mp.mpf("1.36749378") * mp.power(A, mp.mpf(-1) / 3)
            sh += eps * z * (z - 1) / 2 - eps * (z + 1) * z / 2
        return sh

    preview = [(A, z, qm + preview_shift(A, z), qe) for A, z, qm, qe in pairs]

    def scores(pp):
        sc = [p for p in pp if abs(p[3]) > THRESH and p[0] > 1]
        po = [p for p in sc if p[3] > 0]
        ne = [p for p in sc if p[3] < 0]
        return (sum(1 for p in sc if (p[2] > 0) == (p[3] > 0)), len(sc),
                sum(1 for p in po if p[2] > 0), len(po), sum(1 for p in ne if p[2] < 0), len(ne))

    scored = [p for p in pairs if abs(p[3]) > THRESH and p[0] > 1]
    agree = sum(1 for _, _, qm, qe in scored if (qm > 0) == (qe > 0))
    pos = [p for p in scored if p[3] > 0]
    neg = [p for p in scored if p[3] < 0]
    agree_pos = sum(1 for p in pos if p[2] > 0)
    agree_neg = sum(1 for p in neg if p[2] < 0)

    by_a = collections.defaultdict(list)
    for A, z, qm, qe in pairs:
        if A > 1:
            by_a[A].append((z, qm, qe))

    def crossing(seq, idx):
        s = sorted(seq)
        flips = [s[i][0] + 1 for i in range(len(s) - 1)
                 if s[i][idx] > 0 and s[i + 1][idx] < 0]
        return flips[0] if len(flips) == 1 else None

    dz = []
    for A, seq in by_a.items():
        zm, ze = crossing(seq, 1), crossing(seq, 2)
        if zm is not None and ze is not None:
            dz.append(abs(zm - ze))

    print(f"wired terms detected in m_ruled: {wired or 'none (flat ruled law)'}")
    print(f"SCORE 1 direction: {agree}/{len(scored)} agree "
          f"(beta-minus side {agree_pos}/{len(pos)}, beta-plus/EC side {agree_neg}/{len(neg)})")
    if dz:
        print(f"SCORE 2 line: {len(dz)} isobars with one crossing in both; "
              f"mean |Z*_model - Z*_exp| = {mp.nstr(mp.fsum(dz) / len(dz), 4)}")
    else:
        print("SCORE 2 line: no isobar has a model sign change (Q_model has one sign everywhere)")

    pa = scores(preview)
    by_a_p = collections.defaultdict(list)
    for A, z, qm, qe in preview:
        if A > 1:
            by_a_p[A].append((z, qm, qe))
    dzp, sgn = [], []
    for A, seq in by_a_p.items():
        zm, ze = crossing(seq, 1), crossing(seq, 2)
        if zm is not None and ze is not None:
            dzp.append(abs(zm - ze)); sgn.append(zm - ze)
    print(f"PREVIEW (+twist +EM as stated by sibling threads, kappa = {mp.nstr(kappa, 6)} MeV):")
    print(f"  direction {pa[0]}/{pa[1]} (beta-minus {pa[2]}/{pa[3]}, beta-plus/EC {pa[4]}/{pa[5]})")
    if dzp:
        print(f"  line: {len(dzp)} isobars; mean |dZ*| = {mp.nstr(mp.fsum(dzp)/len(dzp), 4)}, "
              f"mean signed dZ* = {mp.nstr(mp.fsum(sgn)/len(sgn), 4)}")

    if WitnessBuilder is not None:
        wb = WitnessBuilder("beta-stability-line", engine="mpmath")
        wb.set_description(
            "Two-sided beta decay direction and stability line Z*(A) from the mass table's "
            "ruled-law masses (pre-registered; AME used only for scoring)."
        )
        wb.add_assertion("scored_rows_nonempty", computed=str(len(scored) > 0), expected="True", tolerance="0")
        for k, v in {
            "wired_terms": wired,
            "n_scored": len(scored), "n_agree": agree,
            "beta_minus_side": f"{agree_pos}/{len(pos)}",
            "beta_plus_side": f"{agree_neg}/{len(neg)}",
            "n_isobars_with_line": len(dz),
            "mean_abs_dZ": mp.nstr(mp.fsum(dz) / len(dz), 6) if dz else None,
            "preview_kappa_MeV": mp.nstr(kappa, 10),
            "preview_direction": f"{pa[0]}/{pa[1]}",
            "preview_beta_minus_side": f"{pa[2]}/{pa[3]}",
            "preview_beta_plus_side": f"{pa[4]}/{pa[5]}",
            "preview_n_isobars_with_line": len(dzp),
            "preview_mean_abs_dZ": mp.nstr(mp.fsum(dzp) / len(dzp), 6) if dzp else None,
            "preview_mean_signed_dZ": mp.nstr(mp.fsum(sgn) / len(sgn), 6) if sgn else None,
        }.items():
            wb.add_data(k, v)
        wb.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
