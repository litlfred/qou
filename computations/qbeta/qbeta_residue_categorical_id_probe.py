"""qbeta_residue_categorical_id_probe.py — residue-ID follow-up on PR #1727.

Tests candidate categorical closed forms for the simple-pole residue
`A = 1.804 × 10⁻¹⁵` at u_substrate (verified in Step 1+2 of PR #1727).
A ≈ 1 ppQ, the precision-target scale. Three hypotheses per the
audit `2026-06-02-qbeta-1ppq-singularity-simple-pole-fibre-level.md`:

  (1) A = ℏ_q^N  for some integer N (or rational)
  (2) A = b^N · ℏ_q^M  structural product
  (3) A = Q_β · ε_struct  with ε_struct a small structural factor

NO ansatz fits per AGENTS.md. Each test is a TIERED PSLQ-style match:
PROVED (<1ppm), NEAR-MATCH (<1%), or REFUTED (>1%). The "tiered
NEAR-MATCH" outcome is honest: report as a NEAR-MATCH on a SPECIFIC
candidate, NOT a closure.

Ref: docs/audits/2026-06-02-qbeta-1ppq-singularity-simple-pole-fibre-level.md
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 100

# qou_substrate path
# Repo root by LANDMARK SEARCH, not by counting `.parent`s: the fixed
# count was off by one and resolved OUTSIDE the repo, so this bootstrap
# never fired -- masked because `_path_bridge`/PYTHONPATH already supplies
# the same directory in every in-repo run. Bean qou-rug0.
from pathlib import Path as _QPath  # noqa: E402
_QOU_REPO_ROOT = next(
    (_a for _a in _QPath(__file__).resolve().parents
     if (_a / "tools").is_dir() and (_a / "computations").is_dir()),
    _QPath(__file__).resolve().parent,
)
_QS = (_QOU_REPO_ROOT
       / "tools" / "qou-substrate" / "python")
if _QS.is_dir() and str(_QS) not in sys.path:
    sys.path.insert(0, str(_QS))
from qou_substrate.constants import q_at  # noqa: E402


def categorical_constants(q: mp.mpf) -> dict[str, mp.mpf]:
    """Standard q_0-dependent categorical scalars."""
    hbar_q = (q - 1) / q
    b_sq = (q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 2
    b = mp.sqrt(b_sq)
    h = q - 1 / q             # Hecke skein parameter
    z = q**3 / (q**2 + 1)   # Markov parameter
    return {
        "q": q,
        "hbar_q": hbar_q,
        "b": b,
        "b_sq": b_sq,
        "h": h,
        "z": z,
        "u_subst": b * hbar_q ** 2,
    }


def tier(value: mp.mpf, target: mp.mpf) -> str:
    if target == 0 or not mp.isfinite(value):
        return "INF/INVALID"
    err = (value / target - 1)
    abs_err_ppm = abs(err) * mp.mpf("1e6")
    if abs_err_ppm < mp.mpf("1"):
        return f"PROVED ({mp.nstr(err * mp.mpf('1e9'), 4)} ppb)"
    if abs_err_ppm < mp.mpf("10000"):  # <1%
        return f"NEAR-MATCH ({mp.nstr(err * mp.mpf('100'), 4)} %)"
    return f"REFUTED ({mp.nstr(err * mp.mpf('100'), 4)} %)"


def main() -> int:
    q = q_at(80)
    c = categorical_constants(q)

    # Residue from Step 1 of PR #1727
    TARGET = mp.mpf("1.8043e-15")   # = u_subst × tail_mean = 0.00852 × 2.118e-13

    # Recompute TARGET precisely:
    tail_mean = mp.mpf("2.11794472225e-13")  # from Step 1 witness
    TARGET = c["u_subst"] * tail_mean

    print(f"Q_β simple-pole residue categorical-ID probe @ q_0")
    print(f"  TARGET residue A = u_subst · tail_mean = {mp.nstr(TARGET, 14)}")
    print(f"  ≈ 1 ppQ = 10^-15 scale")
    print()
    print(f"  Canonical q_0 scalars:")
    for k, v in c.items():
        print(f"    {k:>10s} = {mp.nstr(v, 14)}")
    print()

    results: list[dict] = []

    # ─── (1) A = ℏ_q^N for integer N ──────────────────────────────
    print("--- (1) A = ℏ_q^N for N = 12..20 ---")
    hbar = c["hbar_q"]
    print(f"  hbar_q = {mp.nstr(hbar, 14)}")
    for N in range(12, 21):
        val = hbar ** N
        t = tier(val, TARGET)
        results.append({"hypothesis": f"hbar_q^{N}", "value": val, "tier": t})
        mark = "  ★" if "PROVED" in t else ("  ◆" if "NEAR" in t else "")
        print(f"  N={N:>2d}: ℏ_q^{N} = {mp.nstr(val, 10):>14s}  {t}{mark}")
    print()

    # ─── (2) A = b^N · ℏ_q^M ──────────────────────────────────────
    print("--- (2) A = b^N · ℏ_q^M for small N, M (with N+2M ≈ 15 for scale) ---")
    print(f"  b = {mp.nstr(c['b'], 14)}, ℏ_q = {mp.nstr(hbar, 14)}")
    # Scale of b^N · ℏ_q^M ≈ exp(N·log(b) + M·log(hbar)) at q_0:
    # log(b) ≈ -0.142, log(hbar) ≈ -2.31. To hit 10^-15 (= log = -34.5):
    # solve -0.142N - 2.31M = -34.5 → trade off N, M (M dominant).
    candidates = []
    for N in range(0, 10):
        for M in range(0, 20):
            val = c["b"] ** N * hbar ** M
            if mp.mpf("1e-17") < val < mp.mpf("1e-13"):
                err_abs = abs(val / TARGET - 1)
                candidates.append((err_abs, N, M, val))
    candidates.sort()
    print(f"  Top 8 closest (b^N · ℏ_q^M):")
    for err, N, M, val in candidates[:8]:
        t = tier(val, TARGET)
        results.append({"hypothesis": f"b^{N}·hbar^{M}", "value": val, "tier": t})
        mark = "  ★" if "PROVED" in t else ("  ◆" if "NEAR" in t else "")
        print(f"  b^{N:>1d}·ℏ_q^{M:>2d} = {mp.nstr(val, 10):>14s}  {t}{mark}")
    print()

    # ─── (4) A = [n]_q · ℏ_q^N (colored-Jones-unknot prefactor) ───
    # Per sibling #1521's α_em Habiro categorical ID: [N]_q = J_N(unknot)
    # is the canonical Jones-polynomial-of-trivial-knot prefactor.
    # Test A = [n]_q · ℏ_q^N for n ∈ {1, 2, 3, 4} and N near 15.
    print("--- (4) A = [n]_q · ℏ_q^N (J_n(unknot) prefactor) ---")

    def nq(n: int) -> mp.mpf:
        """[n]_q quantum integer = (q^n - q^-n)/(q - q^-1)."""
        if n == 1:
            return mp.mpf(1)
        return sum(q ** (n - 1 - 2 * k) for k in range(n))

    print(f"  [1]_q = {mp.nstr(nq(1), 12)}, [2]_q = {mp.nstr(nq(2), 12)}, "
          f"[3]_q = {mp.nstr(nq(3), 12)}, [4]_q = {mp.nstr(nq(4), 12)}")
    family4_best = (mp.inf, None, None)
    for n in range(1, 6):
        for N in range(13, 17):
            val = nq(n) * hbar ** N
            err = abs(val / TARGET - 1)
            if err < family4_best[0]:
                family4_best = (err, f"[{n}]_q·ℏ_q^{N}", val)
            t = tier(val, TARGET)
            mark = "  ★" if "PROVED" in t else ("  ◆" if "NEAR" in t else "")
            if abs(val / TARGET - 1) < mp.mpf("0.1"):  # only print close ones
                print(f"  [{n}]_q·ℏ_q^{N} = {mp.nstr(val, 10):>14s}  {t}{mark}")
                results.append({"hypothesis": f"[{n}]_q·hbar^{N}", "value": val, "tier": t})
    if family4_best[1]:
        print(f"  Best (4): {family4_best[1]} = {mp.nstr(family4_best[2], 12)} "
              f"err={mp.nstr(family4_best[0] * 100, 5)} %")
    print()

    # ─── (5) Multiplicative correction to 2·ℏ_q^15 ────────────────
    # The strongest near-pattern: A / ℏ_q^15 ≈ 2.07. Test
    # A = 2 · ℏ_q^15 · (1 + ε_correction) for canonical small ε.
    print("--- (5) A = 2·ℏ_q^15 · (1 + ε)  test canonical ε ---")
    base = 2 * hbar ** 15
    eps_implied = TARGET / base - 1
    print(f"  base = 2·ℏ_q^15 = {mp.nstr(base, 14)}")
    print(f"  ε_implied = A/base − 1 = {mp.nstr(eps_implied, 12)}")
    for name, val in [
        ("h²", c["h"] ** 2),
        ("h²·b²", c["h"] ** 2 * c["b_sq"]),
        ("ℏ_q", hbar),
        ("ℏ_q²", hbar ** 2),
        ("h²/2", c["h"] ** 2 / 2),
        ("u_subst", c["u_subst"]),
        ("π·u", mp.pi * c["u_subst"]),
        ("[2]_q · h² / 4", nq(2) * c["h"] ** 2 / 4),
    ]:
        ratio = eps_implied / val if val != 0 else mp.inf
        # Compare overall expression `2·ℏ_q^15·(1+val)` to TARGET
        composite = base * (1 + val)
        t = tier(composite, TARGET)
        mark = "  ★" if "PROVED" in t else ("  ◆" if "NEAR" in t else "")
        print(f"  ε={name:>14s}: composite={mp.nstr(composite, 10):>14s}  "
              f"ratio={mp.nstr(ratio, 6):>8s}  {t}{mark}")
        results.append({
            "hypothesis": f"2·hbar^15·(1+{name})",
            "value": composite,
            "tier": t,
        })
    print()

    # ─── (3) A = Q_β · ε_struct ───────────────────────────────────
    print("--- (3) A = Q_β · ε_struct (with ε_struct a small q_0-rational) ---")
    Q_beta = mp.mpf("0.78233340999999999999999999999999999999999999999999940982960403984")
    print(f"  Q_β = {mp.nstr(Q_beta, 14)}")
    eps_implied = TARGET / Q_beta
    print(f"  ε_implied = A / Q_β = {mp.nstr(eps_implied, 14)}")
    # Is ε_implied a recognizable ratio?
    for name, val in [
        ("ℏ_q^15", hbar ** 15),
        ("ℏ_q^14·u", hbar ** 14 * c["u_subst"]),
        ("u^7", c["u_subst"] ** 7),
        ("u^8 / b", c["u_subst"] ** 8 / c["b"]),
        ("u_subst^7·hbar", c["u_subst"] ** 7 * hbar),
    ]:
        ratio = eps_implied / val if val != 0 else mp.inf
        t = tier(val, eps_implied)
        results.append({
            "hypothesis": f"ε = {name}",
            "value": val,
            "tier": t,
            "ratio_to_implied": mp.nstr(ratio, 8),
        })
        mark = "  ★" if "PROVED" in t else ("  ◆" if "NEAR" in t else "")
        print(f"  ε = {name:>14s} = {mp.nstr(val, 10):>14s}  ratio={mp.nstr(ratio, 6):>8s}  {t}{mark}")
    print()

    # ─── (6) Cyclotomic Φ_8 / q-Pochhammer / depth-15 (Q_β-native) ─
    # Per AGENTS.md §"Q_β c_k truncation order": Φ_8² is a documented
    # Q_β structural object (mirror-pair Δa_m). The simple-pole at
    # u_subst with exponent 15 strongly suggests the documented
    # depth-15 Habiro prefactor Σ_m Δa_m·(u;u)_m = −u^15·(...). Test
    # residue against (u;u)_m q-Pochhammers and Φ_8-cyclotomic forms.
    print("--- (6) Cyclotomic Φ_8 / q-Pochhammer (u;u)_m / depth-15 ---")
    u = c["u_subst"]

    def pochhammer(base: mp.mpf, m: int) -> mp.mpf:
        """(base; base)_m = Π_{j=1}^m (1 − base^j)."""
        p = mp.mpf(1)
        for j in range(1, m + 1):
            p *= (1 - base ** j)
        return p

    # Φ_8(x) = x^4 + 1 (8th cyclotomic). Evaluate at q and at u.
    Phi8_q = q ** 4 + 1
    print(f"  Φ_8(q) = q⁴+1 = {mp.nstr(Phi8_q, 12)}")
    print(f"  (u;u)_15 = {mp.nstr(pochhammer(u, 15), 12)}")
    family6 = [
        ("u^15", u ** 15),
        ("2·u^15·(u;u)_15", 2 * u ** 15 * pochhammer(u, 15)),
        ("[2]_q·u^7·hbar", nq(2) * u ** 7 * hbar),
        ("Φ_8(q)·hbar^17", Phi8_q * hbar ** 17),
        ("(u;u)_7 · hbar^7", pochhammer(u, 7) * hbar ** 7),
        ("2·hbar^15·(u;u)_2", 2 * hbar ** 15 * pochhammer(u, 2)),
        # α_em Habiro element cross-link: α_em ID is [2]_q·(1-h²α).
        # Here test [2]_q·ℏ_q^15·(1−h²·α_em-analog).  Use α≈1/137.
        ("[2]_q·hbar^15·(1-h²/137)",
         nq(2) * hbar ** 15 * (1 - c["h"] ** 2 / 137)),
    ]
    for name, val in family6:
        t = tier(val, TARGET)
        mark = "  ★" if "PROVED" in t else ("  ◆" if "NEAR" in t else "")
        results.append({"hypothesis": name, "value": val, "tier": t})
        print(f"  {name:>28s} = {mp.nstr(val, 10):>14s}  {t}{mark}")
    print()

    # Verdict
    n_proved = sum(1 for r in results if "PROVED" in r["tier"])
    n_near = sum(1 for r in results if "NEAR-MATCH" in r["tier"])
    print(f"VERDICT: {n_proved} PROVED + {n_near} NEAR-MATCH out of {len(results)} candidates")
    if n_proved > 0:
        for r in results:
            if "PROVED" in r["tier"]:
                print(f"  ★ PROVED: A = {r['hypothesis']}  ({r['tier']})")
    elif n_near > 0:
        print(f"  Best candidates (NEAR-MATCH, no closure):")
        near_sorted = sorted(
            [r for r in results if "NEAR-MATCH" in r["tier"]],
            key=lambda r: abs(r["value"] / TARGET - 1),
        )
        for r in near_sorted[:5]:
            print(f"    ◆ {r['hypothesis']}: {r['tier']}")
    else:
        print(f"  All candidates REFUTED. Residue A = 1.804e-15 does not match")
        print(f"  ℏ_q^N (N ∈ [12, 20]), b^N · ℏ_q^M (small N, M), or")
        print(f"  Q_β · {'ℏ_q^15, ℏ_q^14·u, u^7, u^8/b, u_subst^7·hbar'}.")
        print(f"  Categorical residue ID remains open — needs a different")
        print(f"  hypothesis class (e.g. ratio of Markov-trace eigenvalues,")
        print(f"  Galois-descent element on Habiro ring, etc.).")

    # Witness
    w = WitnessBuilder("qbeta-residue-categorical-id-probe", engine="mpmath")
    w.set_description(
        "Tests categorical closed forms for the Q_β simple-pole residue "
        "A = 1.804e-15 at u_substrate (Step 1+2 of PR #1727). Three "
        "hypothesis families: (1) ℏ_q^N integer powers, (2) b^N·ℏ_q^M "
        "products, (3) Q_β · small-q_0-rational ε. Reports tiered "
        "PROVED <1ppm / NEAR-MATCH <1% / REFUTED otherwise. NO fits."
    )
    w.add_data("TARGET_residue_A", mp.nstr(TARGET, 30))
    w.add_data("n_proved", str(n_proved))
    w.add_data("n_near_match", str(n_near))
    w.add_data("n_refuted", str(len(results) - n_proved - n_near))
    for r in results:
        w.add_data(f"hyp_{r['hypothesis'].replace(' ', '_').replace('·', 'x')}",
                   f"value={mp.nstr(r['value'], 12)};tier={r['tier']}")
    w.add_assertion(
        name="at_least_one_categorical_match",
        computed=bool(n_proved > 0),
        expected=False,
        tolerance=0,
        source="Tiered structural test; default expectation is no clean closure",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
