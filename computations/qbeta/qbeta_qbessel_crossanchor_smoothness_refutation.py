#!/usr/bin/env python3
"""qbeta_qbessel_crossanchor_smoothness_refutation.py
====================================================

Close the one open gate PR #2279 left on the q-Bessel `c_3` program: whether a
**substrate-fixed real amplitude `x`** in the bar-odd Hahn–Exton / Jacobi–Anger
object `sinh(x·sinh η)` (`η = log q₀`) can reproduce the `c_3` residue-A
**cross-anchor swing**. **Verdict: REFUTED for any real `x`** — by the same
smoothness bound that killed the real-q `c_3` family (PR #1821) and the fixed-ℓ
`sinh(ℓη)/u^k` f-map (PR #1887 swing-lock).

## The structural argument (formalize-first; no scan, no fit)

The proton-pinned and muon-pinned substrate anchors are the *same* `q₀` to seven
significant figures — they differ only in the 8th decimal:

    q₀_proton = 1.10997858275138…      q₀_muon = 1.10997859555418…
    Δq₀ = 1.2803e-8   (relative 1.15e-8)

yet the CAL-anchored `c_3` differs by ~2.9 %:

    c_3(proton) = −2.0693            c_3(muon) = −2.0097      (eigenphase, authoritative)

So the empirical slope is

    dc_3/dq₀ ≈ 4.66e6 .

Any candidate of the form `c_3(η) = K · sinh(x·sinh η)` with a **fixed** real `x`
is a *smooth* real function of `η = log q₀`. Its cross-anchor relative swing is

    Δc_3/c_3  ≈  coth(x·sinh η) · x · cosh η · (Δq₀/q₀)        (★)

which is bounded by `x · cosh η · (Δq₀/q₀)` for `x·sinh η ≳ 1`. Pinning `x` at any
physical brane-tower scale — `x ∈ {1, 1/√u, 1/u} ≈ {1, 10.8, 117.4}`, where
`u = b·ℏ_q² ≈ 0.00852` is the ladder step (`1/u ≈ 117.4` is the q-difference pole
the q-Bessel recurrence reproduces, `qbeta_qbessel_contiguity_cfinite.py`) — gives
a predicted swing of `≤ 1.4e-6`, i.e. **at least 2×10⁴ too small** to be the
observed `2.9e-2`.

Equivalently (the dual): solving (★) for the `x` that *would* match the observed
slope gives `x ≈ 2.5e6`, so the Jacobi–Anger argument `x·sinh η ≈ 2.6e5` — deep in
the asymptotic-oscillatory regime where the "first few `J_{2m+1}`" truncation that
PR #2279 uses is meaningless, and `x` is five orders of magnitude past the
`O(117)` tower scale. Physically absurd.

## What this does and does NOT say

- It does **not** contradict PR #2279. #2279 identifies the home-grown Reeb-phase
  objects as the q-special functions of `SU_q(2)` (Hahn–Exton q-Bessel =
  `E_q(2)` matrix coefficients; Vaksman–Korogodsky 1989, Koelink 1994) **at the
  fibre / formal-`q` level**, and explicitly claims no `c_3` closure. This probe
  *confirms* that caution: the q-Bessel is the right **language** (a fibre object
  at formal `q`), not a real closed form `c_3(q₀)`.
- It is the forward complement of the CLAUDE.md Im(q) rule: the resolution lives
  in the **fibre** (a Habiro element evaluated per-anchor), where Im(q) is
  unconstrained, not in a real archimedean `f(q₀_real)`. A real-`x` q-Bessel is an
  archimedean object and inherits the #1821 smoothness obstruction.
- Net for the program: this **retires the speculative `c_3`-via-real-q-Bessel
  upside**, parallel to how PR #2294 retired the q-Bessel binding upside, leaving
  #2279 as clean exposition + fibre structure. The productive `c_3` direction
  remains the **fibre-level Q_β Habiro element** (the α_EM `[2]_q·(1−h²α)`
  template), per `docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`.

## Discipline

Three-calibration; **no 7th fit** (zero free parameters — `x` is *pinned*, `K`
cancels in the ratio); derive-or-refute; report TIERED; `c_3` stays cal-anchored;
nothing wired to production.

The q-Bessel object refuted here is defined and cited (Vaksman–Korogodsky 1989,
Koelink 1994, Gasper–Rahman 2004) in PR #2279; this probe is a self-contained
smoothness bound and adds no bibliography.
"""
from __future__ import annotations

import json
import pathlib

from mpmath import mp, mpf, log, sinh, cosh, coth, findroot

mp.dps = 50

# ── Anchors + CAL-anchored c_3 (sources cited inline) ────────────────────────
# q₀ values: qbeta_chain4_kashiwara_step3_cross_anchor.py (Q_PROTON / Q_MUON).
Q0_PROTON = mpf("1.10997858275138080759166909561")
Q0_MUON = mpf("1.10997859555418057528159407961")
# c_3 targets: qbeta_eigenphase_taylor_in_u.py (C3_EMP_MP / C3_EMP_MUON) — the
# authoritative both-anchor pair. (The scope doc's Φ₂ reconciliation quotes a
# slightly different muon value −2.0202; the verdict is robust to either, so we
# report both as a sensitivity check.)
C3_PROTON = mpf("-2.0693")
C3_MUON_AUTH = mpf("-2.0097")  # eigenphase probe (authoritative)
C3_MUON_SCOPE = mpf("-2.0202")  # scope-doc Φ₂ reconciliation (sensitivity)

# Substrate ladder step u = b·ℏ_q² ≈ 0.00852 (qbeta_ck_truncation_bias_correction_probe.py);
# 1/u ≈ 117.4 is the q-difference pole reproduced by the q-Bessel tail ratio
# (qbeta_qbessel_contiguity_cfinite.py).
U_SUBST = mpf("0.00852")
INV_U = 1 / U_SUBST

results: dict = {}
asserts: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    asserts.append((name, bool(ok)))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}")


# ── (1) The anchors are the same substrate to 7 sig figs ─────────────────────
print("(1) Anchors are the same q₀ to 7 sig figs")
dq = Q0_MUON - Q0_PROTON
rel_dq = dq / Q0_PROTON
eta = log(Q0_PROTON)
se, ce = sinh(eta), cosh(eta)
print(f"    q0_proton = {mp.nstr(Q0_PROTON, 18)}")
print(f"    q0_muon   = {mp.nstr(Q0_MUON, 18)}")
print(f"    Δq0       = {mp.nstr(dq, 6)}  (rel {mp.nstr(rel_dq, 4)})")
print(f"    η=log q0  = {mp.nstr(eta, 8)}   sinh η = {mp.nstr(se, 6)}")
results["anchors"] = {
    "q0_proton": mp.nstr(Q0_PROTON, 30),
    "q0_muon": mp.nstr(Q0_MUON, 30),
    "delta_q0": mp.nstr(dq, 8),
    "rel_delta_q0": mp.nstr(rel_dq, 8),
    "eta": mp.nstr(eta, 12),
}
check("anchors differ by < 1e-7 (same substrate to 7 sig figs)", abs(rel_dq) < mpf("1e-7"))


# ── (2) The empirical c_3 slope is the #1821 ≈4.6e6 smoothness wall ───────────
print("\n(2) Empirical cross-anchor slope dc_3/dq₀")
slope_table = {}
for tag, c3m in [("authoritative", C3_MUON_AUTH), ("scope_phi2", C3_MUON_SCOPE)]:
    dc3 = c3m - C3_PROTON
    rel_swing = abs(dc3 / C3_PROTON)
    slope = dc3 / dq
    print(
        f"    [{tag:13s}] c_3: {mp.nstr(C3_PROTON,6)} → {mp.nstr(c3m,6)}   "
        f"|Δc_3/c_3| = {mp.nstr(rel_swing,4)}   dc_3/dq₀ = {mp.nstr(slope,5)}"
    )
    slope_table[tag] = {
        "c3_muon": mp.nstr(c3m, 8),
        "rel_swing": mp.nstr(rel_swing, 8),
        "dc3_dq0": mp.nstr(slope, 8),
    }
results["empirical_slope"] = slope_table
# Both variants land in the millions (the #1821 wall): assert > 1e6.
check(
    "dc_3/dq₀ > 1e6 for both muon variants (the PR #1821 ≈4.6e6 smoothness wall)",
    abs((C3_MUON_AUTH - C3_PROTON) / dq) > mpf("1e6")
    and abs((C3_MUON_SCOPE - C3_PROTON) / dq) > mpf("1e6"),
)
# Authoritative variant reproduces ≈4.6e6 specifically.
slope_auth = abs((C3_MUON_AUTH - C3_PROTON) / dq)
check(
    "authoritative dc_3/dq₀ ≈ 4.6e6 (matches CLAUDE.md / PR #1821 figure within 10%)",
    abs(slope_auth - mpf("4.6e6")) / mpf("4.6e6") < mpf("0.10"),
)


# ── (3) FORWARD (zero-parameter): pin x at substrate scales → tiny swing ──────
# Predicted cross-anchor relative swing of sinh(x·sinh η), K-independent:
#   Δc_3/c_3 = sinh(x·sinh η_muon)/sinh(x·sinh η_proton) − 1.
print("\n(3) FORWARD — pin x at physical brane-tower scales, predict the swing")
eta_m = log(Q0_MUON)
se_m = sinh(eta_m)
obs_swing = abs((C3_MUON_AUTH - C3_PROTON) / C3_PROTON)
pinned = {"x=1": mpf(1), "x=1/sqrt(u)≈10.8": 1 / mp.sqrt(U_SUBST), "x=1/u≈117.4": INV_U}
fwd = {}
worst_ratio = mpf(0)
for label, x in pinned.items():
    pred = abs(sinh(x * se_m) / sinh(x * se) - 1)
    ratio = obs_swing / pred
    worst_ratio = max(worst_ratio, ratio)
    print(
        f"    {label:18s}: predicted swing = {mp.nstr(pred,4)}   "
        f"observed/predicted = {mp.nstr(ratio,4)}×"
    )
    fwd[label] = {"x": mp.nstr(x, 8), "predicted_swing": mp.nstr(pred, 8),
                  "observed_over_predicted": mp.nstr(ratio, 8)}
results["forward_pinned_x"] = {"observed_swing": mp.nstr(obs_swing, 8), "cases": fwd}
check(
    "every physical-scale x under-predicts the swing by ≥ 1e4×",
    worst_ratio > mpf("1e4"),
)


# ── (4) DUAL (inverse): the x that WOULD match the slope is absurd ───────────
print("\n(4) DUAL — solve for the x that would match the observed slope")
inv = {}
x_req_auth = None  # cache the authoritative root for the assertion (findroot is costly)
for tag, c3m in [("authoritative", C3_MUON_AUTH), ("scope_phi2", C3_MUON_SCOPE)]:
    target = abs((c3m - C3_PROTON) / dq / C3_PROTON)  # |d ln c_3 / dq₀|
    x_req = findroot(lambda x: coth(x * se) * x * ce / Q0_PROTON - target, mpf("2e6"))
    if tag == "authoritative":
        x_req_auth = x_req
    arg = x_req * se
    print(
        f"    [{tag:13s}] required x = {mp.nstr(x_req,5)}   "
        f"→ Jacobi–Anger arg x·sinh η = {mp.nstr(arg,5)}"
    )
    inv[tag] = {"required_x": mp.nstr(x_req, 8), "jacobi_anger_arg": mp.nstr(arg, 8)}
results["inverse_required_x"] = inv
check(
    "required x > 1e6 (≥ 4 orders past the O(117) brane-tower scale) — absurd",
    x_req_auth > mpf("1e6"),
)


# ── Verdict + witness ────────────────────────────────────────────────────────
all_passed = all(ok for _, ok in asserts)
verdict = (
    "REFUTED (real x). A substrate-fixed real amplitude x in the bar-odd q-Bessel / "
    "Jacobi–Anger object sinh(x·sinh η) CANNOT reproduce the c_3 cross-anchor swing: "
    "the two anchors differ by Δq₀≈1.28e-8 while c_3 differs ~2.9%, so dc_3/dq₀≈4.66e6 "
    "— the PR #1821 smoothness wall. Pinning x at any physical brane-tower scale "
    "(1…117) under-predicts the swing by ≥2e4×; matching it needs x≈2.5e6 (argument "
    "≈2.6e5), physically absurd. This CONFIRMS PR #2279's stated caution (no c_3 "
    "closure claimed) and is consistent with PR #1887 (fixed-ℓ swing-lock) and the "
    "Im(q) fibre-vs-observable rule: the q-Bessel is the right FIBRE language, not a "
    "real closed form c_3(q₀). Productive direction stays the fibre-level Q_β Habiro "
    "element (α_EM [2]_q·(1−h²α) template). No fit; nothing wired; c_3 cal-anchored."
)
print("\n" + ("ALL PASSED" if all_passed else "SOME FAILED"))
print("VERDICT:", verdict)

witness = {
    "computation": "qbeta_qbessel_crossanchor_smoothness_refutation",
    "description": (
        "Formalize-first refutation of a substrate-fixed real-x q-Bessel "
        "sinh(x·sinh η) as a c_3 residue-A cross-anchor closed form. The "
        "proton/muon anchors differ by Δq₀≈1.28e-8 but c_3 differs ~2.9% "
        "(dc_3/dq₀≈4.66e6, the PR #1821 wall); any physical-scale x under-predicts "
        "the swing ≥2e4×, matching it needs x≈2.5e6. Closes the one open gate PR "
        "#2279 named; confirms its no-closure caution. "
        "docs/audits/2026-06-14-qbessel-c3-crossanchor-smoothness-refutation.md."
    ),
    "discipline": "no fit (x pinned, K cancels); derive-or-refute; TIERED; c_3 cal-anchored; nothing wired",
    "precision_dps": mp.dps,
    "results": results,
    "assertions": {name: ok for name, ok in asserts},
    "allPassed": all_passed,
    "verdict": verdict,
}
out = pathlib.Path(__file__).parent / "qbeta-qbessel-crossanchor-smoothness-refutation.witness.json"
out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
print(f"\nwitness → {out}")
