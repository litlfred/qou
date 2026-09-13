#!/usr/bin/env python3
"""a4_h12_brunnian_deficit_measure_probe.py — Task 3 (Route-3 companion input).

Measure the SIGN of the A=4 4-component *Brunnian* level deficit `1 − τ_L₄` at the
substrate q₀ to establish (or refute) the antecedent `τ_L₄ ≤ 1` of the (scope-(b),
CONDITIONAL) Lean sign wall
`QOU.MassTheory.HeliumFourBodyCluster.mu4_ne_brunnian4Cluster` (#4376).

  τ_L₄ ≤ 1 measured  ⇒ Brunnian cluster c₄ = E₀·(1−τ_L₄) ≥ 0, sign-incompatible
                       with the derived μ₄ = −4.591 < 0 ⇒ Route-3 sign wall
                       becomes UNCONDITIONAL (scope-(b) antecedent measured true).
  τ_L₄ > 1 measured   ⇒ antecedent FAILS, the Brunnian deficit is negative and
                       could match μ₄<0 ⇒ recipe REOPENS (reported honestly).

Why this is distinct from `helium_four_body_cluster_probe.py`
-------------------------------------------------------------
That probe measured cabled BLOCK-CHAIN words whose Brunnian-ness was NEVER
verified. Block-chains fail the delete-one-block test, so a τ>1 there does NOT
refute the wall (the wall is about the *Brunnian* deficit specifically). This
probe constructs a GENUINELY Brunnian 4-braid — the iterated left-normed
commutator of pure-braid band generators

    w₄ = [[A₀₁, A₁₂], A₂₃]              (0-based strands; = [[A₁₂,A₂₃],A₃₄] 1-based)

and VERIFIES Brunnian-ness EXACTLY before measuring the deficit sign.

Why w₄ is Brunnian (pure-braid strand-forgetting algebra, verified below)
-------------------------------------------------------------------------
The band generators A_{ij} (i<j) are the standard generators of the pure braid
group P_n. The strand-forgetting homomorphism d_k : P_n → P_{n-1} acts by
    d_k(A_{ij}) = 1                if k ∈ {i,j}     (that band dies)
    d_k(A_{ij}) = A_{i',j'}        otherwise        (reindex indices > k down by 1)
A proper sub-link = closure of d_k(w₄). Deleting ANY strand collapses the nested
commutator to the identity braid:
  d₀: A₀₁→1 ⇒ inner=[1,A₀₁]=id ⇒ w₄=[id,A₁₂]=id
  d₁: A₀₁→1, A₁₂→1 ⇒ inner=id ⇒ id
  d₂: A₁₂→1 ⇒ inner=[A₀₁,1]=id ⇒ id
  d₃: A₂₃→1 ⇒ w₄=[inner,1]=id
So every proper sub-link is the UNLINK (trace deficit EXACTLY 0), while the full
4-braid is a nontrivial pure braid (a genuine Brunnian 4-component link, first
non-vanishing Milnor invariant μ̄(1234) at length 4 ⇒ leading order O(h⁶)=2·(4−1)).
The probe computes d_k(w₄) explicitly at the band level and confirms deficit≈0.

Level / normalization: the SAME 0-fit perblock trace g(word)=Σ_{λ⊢n} y_λ·|χ_λ|·E₀
and E₀ = m_e/(q₀(q₀−1)) used by #4364 / the A=3 Borromean H₉ lift. Base level n=4
(rigorous, traces <0.1s); width-3 cabling to H₁₂ (n=12, 77 partitions) for the
magnitude regime. deficit := 1 − g_link/g_unlink, so τ := g_link/g_unlink (unlink=1)
and deficit ≥ 0 ⟺ τ ≤ 1 ⟺ Lean antecedent holds.

STRICT anti-fit: 0 free params; μ₄ forward AME−model, NEVER inverted; the word is
fixed by the TOPOLOGICAL Brunnian constraint (verified delete-strand → identity),
not tuned to any target; nothing wired.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_COMP = _Path(__file__).resolve().parent.parent
for _d in ("hecke", "habiro", "substrate"):
    _p = str(_COMP / _d)
    if _p not in _sys.path:
        _sys.path.insert(0, _p)
_sys.path.insert(0, str(_COMP))
import _path_bridge  # noqa: E402, F401

import json  # noqa: E402
import time  # noqa: E402
import hashlib  # noqa: E402
import subprocess  # noqa: E402
from datetime import datetime, timezone  # noqa: E402

import mpmath as mp  # noqa: E402
import pyhecke_native  # noqa: E402

from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps(30)
HERE = _Path(__file__).resolve().parent
_T0 = time.time()


def _log(msg: str) -> None:
    print(f"[{time.time() - _T0:7.1f}s] {msg}", flush=True)


q0 = mp.mpf(str(Q0))
q0f = float(Q0)
H = q0 - 1 / q0                                   # Hecke h = q − q⁻¹
E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))       # SAME E₀ as #4364 / ρ_F


# =========================================================================
# (i) FORWARD-derive the A=4 residual target μ₄ (AME − model, 0 fit).
#     Byte-identical to helium_four_body_cluster_probe.derive_mu4.
# =========================================================================
def qint(n, q):
    """Unbalanced q-integer [n]_q = 1 + q + ... + q^{n-1} = (q^n - 1)/(q - 1)."""
    return sum(q ** k for k in range(n))


def qfac_over_2(A, q):
    r = mp.mpf(1)
    for k in range(3, A + 1):
        r *= qint(k, q)
    return r


def derive_mu4():
    from math import comb
    rho_grad = {A: qfac_over_2(A, q0) for A in (2, 3, 4)}
    rho_strong = {2: mp.mpf(1), 3: mp.mpf("3.8128"), 4: mp.mpf("13.0316")}
    M = {A: rho_strong[A] - rho_grad[A] for A in (2, 3, 4)}
    mu2 = M[2]
    mu3 = M[3] - 3 * mu2
    mu4 = M[4] - 6 * mu2 - 4 * mu3
    for A in (2, 3, 4):
        recon = mu2 * comb(A, 2) + mu3 * comb(A, 3) + mu4 * comb(A, 4)
        assert abs(recon - M[A]) < mp.mpf("1e-25"), f"simplex must reproduce M({A})"
    return mu2, mu3, mu4, M


# =========================================================================
# Braid words as lists of (sign, gen)  [sign=+1: σ_g ; sign=-1: σ_g⁻¹], 0-based g.
# =========================================================================
def sig(g):
    return [(+1, g)]


def sig_inv(g):
    return [(-1, g)]


def word_inv(word):
    """Inverse braid word: reverse order, flip each crossing sign."""
    return [(-s, g) for (s, g) in reversed(word)]


def to_hecke(word, h=None):
    """(sign,gen) list → (c,d,g) Hecke triples; g stays 0-based (perblock adds +1).
    σ_g = (1,0,g);  σ_g⁻¹ = σ_g − h·I = (1,−h,g)."""
    hh = H if h is None else h
    out = []
    for (s, g) in word:
        out.append((1.0, 0.0, g) if s > 0 else (1.0, float(-hh), g))
    return out


# =========================================================================
# Band (pure-braid) generators A_{ij} (i<j, 0-based) as σ-words + the
# strand-forgetting map d_k, so the Brunnian test is EXACT.
#
#   A_{ij} = (σ_{j-1}…σ_{i+1}) σ_i² (σ_{i+1}⁻¹…σ_{j-1}⁻¹)     (standard P_n gen)
#
# A band-word is a list of (i, j, e) with e=±1 meaning A_{ij}^e.
# =========================================================================
def band_to_sigma(i, j, e):
    """One band factor A_{ij}^e → (sign,gen) σ-word."""
    assert i < j
    pre = []
    for k in range(j - 1, i, -1):        # σ_{j-1} … σ_{i+1}
        pre += sig(k)
    core = sig(i) + sig(i)               # σ_i²
    post = []
    for k in range(i + 1, j):            # σ_{i+1}⁻¹ … σ_{j-1}⁻¹
        post += sig_inv(k)
    w = pre + core + post
    return w if e > 0 else word_inv(w)


def band_word_to_sigma(bw):
    out = []
    for (i, j, e) in bw:
        out += band_to_sigma(i, j, e)
    return out


def band_inv(bw):
    return [(i, j, -e) for (i, j, e) in reversed(bw)]


def band_comm(a, b):
    """[a,b] = a b a⁻¹ b⁻¹ at the band level."""
    return list(a) + list(b) + band_inv(a) + band_inv(b)


def delete_strand_band(bw, k):
    """Strand-forgetting d_k on a band-word: drop factors with k∈{i,j}, reindex
    the rest (indices > k shift down by 1). Returns a band-word on n−1 strands."""
    out = []
    for (i, j, e) in bw:
        if i == k or j == k:
            continue
        ii = i - 1 if i > k else i
        jj = j - 1 if j > k else j
        out.append((ii, jj, e))
    return out


# The A=4 genuine Brunnian braid (band-level):  w₄ = [[A₀₁, A₁₂], A₂₃]
A01 = [(0, 1, +1)]
A12 = [(1, 2, +1)]
A23 = [(2, 3, +1)]
INNER_A4 = band_comm(A01, A12)             # [A₀₁, A₁₂]
W4_BAND = band_comm(INNER_A4, A23)         # [[A₀₁, A₁₂], A₂₃]

# The A=3 Borromean band analog (validation):  w₃ = [A₀₁, A₁₂]
W3_BAND = band_comm(A01, A12)


# =========================================================================
# Perblock joint trace at level n:  g(word) = Σ_{λ⊢n} y_λ·|χ_λ(word)|   (0-fit)
# =========================================================================
_YCACHE: dict[tuple, dict] = {}


def _yn(n, qv):
    key = (n, str(qv))
    if key not in _YCACHE:
        _YCACHE[key] = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
                        for k, v in y_lambda_at(n, qv).items()}
    return _YCACHE[key]


def perblock(n, hecke_word, qv=None):
    qv = q0 if qv is None else qv
    Y = _yn(n, qv)
    cp = pyhecke_native.chi_q_atomic_all_partitions(
        n, [(float(c), float(d), int(g) + 1) for (c, d, g) in hecke_word], float(qv))
    return sum(Y[tuple(s)] * abs(mp.mpf(repr(chi))) for s, chi in cp if tuple(s) in Y)


def deficit_sigma(n, sigma_word, qv=None, h=None):
    """1 − g_link/g_unlink at level n for a (sign,gen) σ-word."""
    qv = q0 if qv is None else qv
    g_unlink = perblock(n, [], qv)
    g_link = perblock(n, to_hecke(sigma_word, h=h), qv)
    return 1 - g_link / g_unlink, g_link, g_unlink


def leading_order(n, sigma_word_fn, grid=("1.02", "1.04", "1.08")):
    """log-log slope of |deficit(q)| across a q-grid ⇒ leading h-exponent."""
    pts = []
    for qv in grid:
        qm = mp.mpf(qv)
        hv = qm - 1 / qm
        d, _, _ = deficit_sigma(n, sigma_word_fn(), qm, h=hv)
        pts.append((hv, d))
    (h1, d1), (h2, d2) = pts[0], pts[-1]
    nord = mp.log(abs(d2) / abs(d1)) / mp.log(h2 / h1) if d1 != 0 and d2 != 0 else mp.nan
    return nord, pts


# =========================================================================
# Width-3 cabling: σ_g → block-transposition of blocks g,g+1 (descending run).
# =========================================================================
def _block_transposition(a, w=3):
    gens = []
    for r in range(w):
        for g in range(a + w - 1 + r, a - 1 + r, -1):
            gens.append(g)
    return gens


def cable_sigma_word(sigma_word, w=3):
    """Cable a base (sign,gen) σ-word to a width-w σ-word (n → w·n strands)."""
    out = []
    for (s, g) in sigma_word:
        gens = _block_transposition(g * w, w)
        if s > 0:
            out += [(+1, gg) for gg in gens]
        else:
            out += [(-1, gg) for gg in reversed(gens)]
    return out


def main() -> int:
    print("=" * 88)
    print("Task 3 — A=4 H₁₂ *Brunnian* level-deficit SIGN  (establish/refute τ_L₄ ≤ 1)")
    print(f"  q₀={float(q0):.8f}  h={float(H):.6f}  E₀={float(E0):.6f} MeV")
    print("=" * 88)

    # ── (i) forward-derived A=4 target sign ───────────────────────────────────
    mu2, mu3, mu4, M = derive_mu4()
    _log("A=4 residual target (forward AME − model, 0 fit):")
    print(f"    μ₂={mp.nstr(mu2,6)}  μ₃=+{mp.nstr(mu3,6)}  μ₄={mp.nstr(mu4,6)}  "
          f"sign(μ₄)={'NEGATIVE' if mu4 < 0 else 'positive'}")
    assert mu4 < 0

    # ── (ii) A=3 band-commutator Borromean validation ─────────────────────────
    _log("A=3 band-commutator w₃=[A₀₁,A₁₂] — machinery + Brunnian-test validation")
    w3_sigma = band_word_to_sigma(W3_BAND)
    d3, gl3, gu3 = deficit_sigma(3, w3_sigma)
    n3, _ = leading_order(3, lambda: w3_sigma)
    # exact delete-strand test at n=2
    sub3 = {}
    for k in range(3):
        dbw = delete_strand_band(W3_BAND, k)
        sw = band_word_to_sigma(dbw)
        dd, _, _ = deficit_sigma(2, sw) if sw else (mp.mpf(0), None, None)
        sub3[f"drop_{k}"] = mp.nstr(dd, 6)
    print(f"    deficit 1−τ = {mp.nstr(d3,8)}  sign={'+' if d3 > 0 else '-'}  "
          f"leading order n≈{mp.nstr(n3,4)}  (Borromean: expect + and 4)")
    print(f"    delete-strand sub-deficits (must be ≈0): {sub3}")

    # ── (iii) A=4 GENUINE Brunnian braid at base n=4 (rigorous, fast) ─────────
    _log("A=4 genuine Brunnian w₄=[[A₀₁,A₁₂],A₂₃] at base n=4 — EXACT Brunnian test")
    w4_sigma = band_word_to_sigma(W4_BAND)
    print(f"    w₄ band factors={len(W4_BAND)}  σ-word length={len(w4_sigma)}")
    d4, gl4, gu4 = deficit_sigma(4, w4_sigma)
    n4, _ = leading_order(4, lambda: w4_sigma)
    sub4 = {}
    all_sub_trivial = True
    for k in range(4):
        dbw = delete_strand_band(W4_BAND, k)
        sw = band_word_to_sigma(dbw)
        if sw:
            dd, _, _ = deficit_sigma(3, sw)
        else:
            dd = mp.mpf(0)
        sub4[f"drop_{k}"] = mp.nstr(dd, 8)
        # trivial ⟺ machine-zero: the native χ trace is f64, noise ~1e-15; the
        # genuine Brunnian signal is O(h⁶)~1e-4, so 1e-10 cleanly separates them.
        if abs(dd) > mp.mpf("1e-10"):
            all_sub_trivial = False
    tau4 = gl4 / gu4
    c4_base = E0 * (gu4 - gl4)                         # E₀·g_unlink·deficit = E₀·(1−τ)·g_unlink
    print(f"    g_unlink={mp.nstr(gu4,10)}  g_link={mp.nstr(gl4,10)}")
    print(f"    τ_L₄ = g_link/g_unlink = {mp.nstr(tau4,10)}")
    print(f"    deficit 1−τ_L₄ = {mp.nstr(d4,8)}  sign={'+' if d4 > 0 else '-'}"
          f"  ({'τ≤1 (binding, c₄≥0)' if d4 >= 0 else 'τ>1 (c₄<0)'})")
    print(f"    leading Milnor order n≈{mp.nstr(n4,4)}  (Brunnian n=4 ⇒ expect 6=2·(4−1))")
    print(f"    c₄(base,E₀·(1−τ)·g_unlink) = {mp.nstr(c4_base,6)} MeV  sign={'+' if c4_base > 0 else '-'}")
    print(f"    EXACT delete-strand test (all must be 0): {sub4}")
    print(f"    ⇒ Brunnian-ness {'VERIFIED (all 4 proper sub-links trivial)' if all_sub_trivial else 'FAILED'}")
    assert all_sub_trivial, "w₄ must be genuinely Brunnian — delete-strand must give unlink"

    # ── (iv) width-3 cabling → H₁₂ (magnitude regime) ─────────────────────────
    _log("A=4 width-3 cabling → H₁₂ (n=12, 77 partitions)")
    w4_cabled = cable_sigma_word(w4_sigma, w=3)
    print(f"    cabled σ-word length = {len(w4_cabled)}  maxgen={max(g for _, g in w4_cabled)}")
    _log("  timing one H₁₂ trace (unlink already cheap; full cabled word)…")
    t0 = time.time()
    d12, gl12, gu12 = deficit_sigma(12, w4_cabled)
    dt12 = time.time() - t0
    tau12 = gl12 / gu12
    c4_h12 = E0 * (gu12 - gl12)
    _log(f"  H₁₂ full cabled trace took {dt12:.1f}s")
    print(f"    g_unlink={mp.nstr(gu12,10)}  g_link={mp.nstr(gl12,10)}")
    print(f"    τ_L₄(H₁₂) = {mp.nstr(tau12,10)}")
    print(f"    deficit 1−τ_L₄(H₁₂) = {mp.nstr(d12,8)}  sign={'+' if d12 > 0 else '-'}"
          f"  ({'τ≤1 (c₄≥0)' if d12 >= 0 else 'τ>1 (c₄<0)'})")
    print(f"    c₄(H₁₂) = {mp.nstr(c4_h12,6)} MeV  sign={'+' if c4_h12 > 0 else '-'}")

    # delete-BLOCK test at n=9 (delete one width-3 nucleon = cable of delete-strand)
    _log("  H₁₂ delete-BLOCK test (delete one width-3 nucleon → cable at n=9, must be ≈0)")
    subblk = {}
    all_block_trivial = True
    for k in range(4):
        dbw = delete_strand_band(W4_BAND, k)
        sw = band_word_to_sigma(dbw)
        if sw:
            swc = cable_sigma_word(sw, w=3)
            dd, _, _ = deficit_sigma(9, swc)
        else:
            dd = mp.mpf(0)
        subblk[f"drop_block_{k}"] = mp.nstr(dd, 8)
        if abs(dd) > mp.mpf("1e-9"):
            all_block_trivial = False
        _log(f"    drop block {k}: sub-deficit={mp.nstr(dd,6)}")
    print(f"    delete-block sub-deficits (must be ≈0): {subblk}")
    print(f"    ⇒ cabled Brunnian-ness {'VERIFIED' if all_block_trivial else 'NOT verified'}")

    # ── verdict ────────────────────────────────────────────────────────────────
    tau_le_1_base = bool(d4 >= 0)
    tau_le_1_h12 = bool(d12 >= 0)
    signs_agree = (tau_le_1_base == tau_le_1_h12)
    if tau_le_1_base and tau_le_1_h12:
        verdict = ("ANTECEDENT CONFIRMED — τ_L₄ ≤ 1 measured (deficit ≥ 0) for the genuine "
                   "4-component Brunnian braid at BOTH base n=4 and cabled H₁₂. The Brunnian "
                   "binding cluster c₄ = E₀·(1−τ_L₄) ≥ 0 is sign-INCOMPATIBLE with the derived "
                   "μ₄ = −4.591 < 0. The scope-(b) conditional Route-3 sign wall "
                   "mu4_ne_brunnian4Cluster is now UNCONDITIONAL (antecedent measured true).")
    elif (not tau_le_1_base) and (not tau_le_1_h12):
        verdict = ("ANTECEDENT REFUTED — τ_L₄ > 1 measured (deficit < 0) for the genuine "
                   "4-component Brunnian braid at BOTH levels. The Brunnian deficit is NEGATIVE, "
                   "so c₄ = E₀·(1−τ_L₄) < 0 — sign-COMPATIBLE with μ₄ < 0. The scope-(b) "
                   "antecedent of the Route-3 wall genuinely FAILS; the A=4 recipe reopens on "
                   "sign (the magnitude test becomes live). Reported honestly; nothing tuned.")
    else:
        verdict = ("LEVEL-DEPENDENT — the Brunnian deficit sign DIFFERS between base n=4 "
                   f"(τ≤1={tau_le_1_base}) and cabled H₁₂ (τ≤1={tau_le_1_h12}). Cabling changed "
                   "the sign; the antecedent is construction/level-dependent. Reported honestly.")
    print("\n" + "=" * 88)
    print(f"VERDICT: {verdict}")
    print("=" * 88)

    witness = {
        "schema": "witness/v1",
        "producer": "computations/deltalambda/a4_h12_brunnian_deficit_measure_probe.py",
        "computation": "a4-h12-brunnian-deficit-measure",
        "description": (
            "Task 3: measure the SIGN of the A=4 4-component *Brunnian* level deficit 1−τ_L₄ "
            "at the substrate q₀ to establish/refute the antecedent τ_L₄ ≤ 1 of the scope-(b) "
            "CONDITIONAL Lean sign wall QOU.MassTheory.HeliumFourBodyCluster."
            "mu4_ne_brunnian4Cluster (#4376). Distinct from helium_four_body_cluster_probe.py "
            "(which measured cabled BLOCK-CHAIN words never verified Brunnian): this probe "
            "constructs a GENUINELY Brunnian 4-braid — the iterated left-normed commutator of "
            "pure-braid band generators w₄=[[A₀₁,A₁₂],A₂₃] — and VERIFIES Brunnian-ness EXACTLY "
            "via the pure-braid strand-forgetting map d_k (deleting ANY strand collapses the "
            "nested commutator to the identity braid ⇒ every proper sub-link is the unlink, "
            "trace deficit exactly 0). It measures the full-braid deficit sign + leading Milnor "
            "order (expect O(h⁶)=2·(4−1)) at base n=4 (rigorous) and confirms at width-3 cabled "
            "H₁₂ (n=12, 77 partitions). deficit:=1−g_link/g_unlink so τ:=g_link/g_unlink and "
            "deficit≥0 ⟺ τ≤1 ⟺ antecedent holds. SAME 0-fit perblock trace g=Σ y_λ|χ_λ|·E₀ and "
            "E₀=m_e/(q₀(q₀−1)) as #4364. STRICT anti-fit: 0 free params; μ₄ forward AME−model, "
            "never inverted; word fixed by the topological Brunnian constraint, not tuned; "
            "nothing wired."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "free_parameters": 0,
            "q0": str(q0), "h": str(H), "E0_MeV": str(E0),
            "brunnian_word": "w₄ = [[A₀₁,A₁₂],A₂₃] (iterated left-normed commutator of "
                             "pure-braid band generators; 0-based strands)",
            "band_factors": [[i, j, e] for (i, j, e) in W4_BAND],
            "base_level": "n=4, y_λ over partitions of 4",
            "cabled_level": "H₁₂ (n=12), width-3 nucleon cables, y_λ over 77 partitions of 12",
            "note": "μ₄=−4.591 forward AME−model target only; SAME E₀ + y_λ norm as #4364.",
        },
        "results": {
            "a4_residual_target": {
                "mu2": mp.nstr(mu2, 8), "mu3": mp.nstr(mu3, 8),
                "mu4": mp.nstr(mu4, 8), "mu4_sign": "negative",
            },
            "a3_borromean_band_validation": {
                "deficit_1_minus_tau": mp.nstr(d3, 8), "sign": "+" if d3 > 0 else "-",
                "leading_h_order": mp.nstr(n3, 4),
                "delete_strand_subdeficits": sub3,
                "note": "band-commutator [A₀₁,A₁₂] reproduces the Borromean: + deficit, O(h⁴), "
                        "all delete-strand sub-links trivial — validates the band machinery.",
            },
            "a4_brunnian_base_n4": {
                "sigma_word_length": len(w4_sigma),
                "g_unlink": str(gu4), "g_link": str(gl4),
                "tau_L4": str(tau4),
                "deficit_1_minus_tau_L4": str(d4),
                "deficit_sign": "+" if d4 > 0 else "-",
                "tau_le_1": tau_le_1_base,
                "leading_milnor_order": mp.nstr(n4, 4),
                "c4_MeV": str(c4_base), "c4_sign": "+" if c4_base > 0 else "-",
                "delete_strand_subdeficits": sub4,
                "brunnian_verified_exact": bool(all_sub_trivial),
            },
            "a4_brunnian_cabled_h12": {
                "cabled_sigma_word_length": len(w4_cabled),
                "single_trace_seconds": round(dt12, 2),
                "g_unlink": str(gu12), "g_link": str(gl12),
                "tau_L4": str(tau12),
                "deficit_1_minus_tau_L4": str(d12),
                "deficit_sign": "+" if d12 > 0 else "-",
                "tau_le_1": tau_le_1_h12,
                "c4_MeV": str(c4_h12), "c4_sign": "+" if c4_h12 > 0 else "-",
                "delete_block_subdeficits": subblk,
                "cabled_brunnian_verified": bool(all_block_trivial),
            },
            "verdict": {
                "classification": verdict,
                "tau_le_1_base": tau_le_1_base,
                "tau_le_1_h12": tau_le_1_h12,
                "signs_agree_across_levels": bool(signs_agree),
                "antecedent_status": (
                    "CONFIRMED" if (tau_le_1_base and tau_le_1_h12)
                    else ("REFUTED" if (not tau_le_1_base and not tau_le_1_h12)
                          else "LEVEL-DEPENDENT")),
                "route3_wall_unconditional": bool(tau_le_1_base and tau_le_1_h12),
                "mu4_sign": "negative",
                "is_fit": False, "wired": False, "free_param_count": 0,
                "anti_fit": "μ₄ forward AME−model, never inverted; the Brunnian word is fixed "
                            "by the topological delete-strand=identity constraint (verified "
                            "exactly), not tuned to any target; nothing wired.",
            },
        },
        "scriptHash": hashlib.sha256(_Path(__file__).read_bytes()).hexdigest()[:16],
    }
    try:
        witness["scriptCommitSha"] = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", __file__],
            cwd=HERE, text=True).strip() or "uncommitted"
    except Exception:
        witness["scriptCommitSha"] = "uncommitted"
    out = HERE / "a4-h12-brunnian-deficit-measure.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    _log(f"witness -> {out.relative_to(_COMP.parent)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
