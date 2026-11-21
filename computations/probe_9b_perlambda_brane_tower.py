#!/usr/bin/env python3
"""
probe_9b_perlambda_brane_tower.py — PROBE 4 (bean v292): per-λ (per
Wedderburn block) rerun of the single-pipeline Borromean brane tower.

The 2026-06-28 tower (computations/borromean_binding_recompute.py, per
docs/audits/2026-06-28-brane-tower-formalize-first-plan.md) applies
g(x) = −Li₂^q(−x) to the SCALAR Borromean trace
τ = |tr_M(β_Bor)| = (4+h²−3h⁴−h⁶)/(h²+4) ≈ 0.9986 < 1 — converges ∀Z,
right shape, but misses normalization (¹⁶O err 2.3×, under-binds
mid-mass, over-binds ⁵⁶Fe).  Diagnosis on record: the missing PER-λ
weight.  This probe carries (weight_λ, χ^λ(β_Bor)) for λ ⊢ 3 through g
PER BLOCK and collapses LAST (Markov-weighted sum AFTER the tower).

DISCIPLINE NOTE: this is NOT the refuted "Δ_λ per-block density"
ansatz (that refutation concerned multiplying an intensive scalar
density); here the per-λ weight rides an already-extensive tower, and
NO new constant is introduced — the weights are the Markov-trace
decomposition the scalar pipeline already collapses.  Derive-or-refute
only.

Structural findings encoded as assertions:

1.  The pipeline's closed-form τ is EXACTLY the SU(2)/Temperley–Lieb
    (Jones) Markov trace decomposition on H_3:
        τ = y₃ᴶ·χ^{(3)} + y₂₁ᴶ·χ^{(2,1)},
        y₃ᴶ = [4]_q/[2]_q³,  y₂₁ᴶ = 1/[2]_q²,  y_{(1³)}ᴶ = 0,
    with χ^{(3)} = χ^{(1³)} = 1 and χ^{(2,1)} = 2 − 3h⁴ − h⁶ (cheat
    sheet §2 step 3; verified here against the direct seminormal
    matrix product at 50 dps).  The corpus-canonical Wenzl z-trace
    (y_lambda_wenzl_bridge) gives a DIFFERENT scalar
    τ_W = Σ y_λ^W χ^λ ≈ 0.998367 — a 1.96e-4 trace-convention gap
    recorded as data (matters at B-precision, not at the 2.3× scale).

2.  RAW per-block tower (weights y_λ, arguments χ_λχ_μ) DIVERGES:
    χ^{(2,1)}² ≈ 3.977 > q₀ exceeds the Li₂^q convergence radius
    |z| < q (proved in _li_2_q_util.li_2_q).  Exclusion of the raw-χ
    variant is invariant-backed; the constructive alternative is the
    NORMALIZED per-block tower below.

3.  NORMALIZED per-block towers (collapse-last):  weights
    W_λ = y_λ·d_λ (Σ W_λ = 1 by Markov M3), block values r_λ = χ^λ/d_λ
    (all < q₀ ⇒ converges ∀Z), pair term
        Σ_{λ,μ} W_λ W_μ [g(r_λ r_μ) − g(r_λ r_μ f_b)]
    which reproduces the scalar pair term exactly at linear order in g
    (Σ W_λ r_λ = τ).  Run under BOTH weight conventions (Jones/TL and
    Wenzl), plus an AMBIENT-H_6 per-ν variant where the nucleon-pair
    block values are taken in H_6 via the classical Littlewood–
    Richardson rule (Mathas 1999 §3: χ^ν(x⊗y) = Σ c^ν_{λμ} χ^λ(x)χ^μ(y);
    c^ν_{λμ} computed from Murnaghan–Nakayama S_6/S_3 character tables
    and validated against Wenzl disjoint multiplicativity
    Σ_ν y_ν^{(6)} χ^ν(β⊗β) = τ_W²).

Level-0 (E₀·Δtr) stays scalar in every variant: it is LINEAR in the
trace, so collapse-first = collapse-last for it identically; the g
nonlinearity — the only place collapse order matters — lives in the
pair stratum.

Isotopes: full light series D … ⁵⁶Fe (all closed-form, cheap).
50 dps per computations/_precision.py; q₀ from the canonical 50-digit
pinning witness.  No fit constants; Δ_λ gate respected (no 7th ansatz —
no new per-λ constants are introduced anywhere).

Ref: docs/audits/2026-06-28-brane-tower-formalize-first-plan.md
Ref: docs/audits/2026-06-28-brane-tower-higher-order-deuteron.md
Ref: docs/audits/2026-07-02-9b-probes-alphak-perlambda-tower.md
Ref: computations/binding_reeb_phase_decomposition.py (per-λ vector emitter)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge
import json
import sys
from functools import lru_cache
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from _li_2_q_util import load_q_50dps, li_2_q  # noqa: E402
from closed_form_tau_M import markov_z as _markov_z  # noqa: E402 — canonical convention-D z
from y_lambda_wenzl_bridge import (  # noqa: E402
    y_lambda_wenzl_bridge_numeric,
    classical_dim,
    partitions_of,
)
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402  (AME registry)
from mpmath import nstr as _ame_nstr  # noqa: E402  (AME registry, string form)

# AME2020 totals (MeV) — comparison target only (same list as
# borromean_binding_recompute.py).
# AME binding energies as DECIMAL STRINGS, lifted to `mpf` at use below.
# They were float literals until 2026-09-13, which put an f64 rounding on the
# measured side of every `B_AME / B_tower` ratio this probe reports — the
# ratio is the comparison the probe exists to make, so the experimental input
# has no business arriving pre-rounded.  Strings also make the ordering
# against `set_compute_dps()` (line below) irrelevant for them rather than
# merely harmless.
ISO = [("2H", 1, 1, _ame_nstr(AME_B_DEUTERON_MEV_VALIDATION, 30)), ("3H", 1, 2, _ame_nstr(AME_B_TRITIUM_MEV_VALIDATION, 30)),
       ("3He", 2, 1, _ame_nstr(AME_B_HE3_MEV_VALIDATION, 30)), ("4He", 2, 2, _ame_nstr(AME_B_HE4_MEV_VALIDATION, 30)),
       ("6Li", 3, 3, "31.994564"), ("7Li", 3, 4, "39.244533"),
       ("12C", 6, 6, "92.161728"), ("16O", 8, 8, "127.619"),
       ("56Fe", 26, 30, "492.254")]

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

TOL_EXACT = mp.mpf("1e-40")
TOL_CROSS = mp.mpf("1e-25")


def _serialise(obj):
    """Render mpf leaves with `_precision.fmt`; leave everything else alone."""
    if isinstance(obj, dict):
        return {k: _serialise(v) for k, v in obj.items()
                if not k.startswith("_")}
    if isinstance(obj, list):
        return [_serialise(v) for v in obj]
    if isinstance(obj, mp.mpf):
        return fmt(obj)
    return obj


# ────────────────────────────────────────────────────────────────────
# Classical S_n characters (Murnaghan–Nakayama) → LR coefficients
# ────────────────────────────────────────────────────────────────────

@lru_cache(maxsize=None)
def mn_char(lam: tuple, mu: tuple) -> int:
    """Classical S_n character χ^λ(μ) via the Murnaghan–Nakayama rule
    (β-number formulation, exact integers)."""
    lam = tuple(p for p in lam if p > 0)
    if not mu:
        return 1 if not lam else 0
    k, rest = mu[0], mu[1:]
    n_rows = len(lam)
    if n_rows == 0:
        return 0
    beta = [lam[i] + (n_rows - 1 - i) for i in range(n_rows)]
    bset = set(beta)
    total = 0
    for b in beta:
        nb = b - k
        if nb < 0 or nb in bset:
            continue
        height = sum(1 for c in beta if nb < c < b)
        newbeta = sorted((x for x in beta if x != b), reverse=True)
        newbeta.append(nb)
        newbeta.sort(reverse=True)
        m = len(newbeta)
        newlam = tuple(p for p in
                       (newbeta[j] - (m - 1 - j) for j in range(m)) if p > 0)
        total += (-1) ** height * mn_char(newlam, rest)
    return total


# S_3 conjugacy classes: cycle type → class size
S3_CLASSES = {(1, 1, 1): 1, (2, 1): 3, (3,): 2}


@lru_cache(maxsize=None)
def lr_coeff(nu: tuple, lam: tuple, muu: tuple) -> int:
    """Littlewood–Richardson c^ν_{λμ} for λ, μ ⊢ 3, ν ⊢ 6, via
    c = ⟨Res^{S_6}_{S_3×S_3} χ^ν, χ^λ ⊗ χ^μ⟩ (exact)."""
    acc = 0
    for a, sa in S3_CLASSES.items():
        for b, sb in S3_CLASSES.items():
            joint = tuple(sorted(a + b, reverse=True))
            acc += sa * sb * mn_char(nu, joint) * mn_char(lam, a) * mn_char(muu, b)
    if acc % 36 != 0:
        raise RuntimeError(f"non-integral LR coefficient for {nu},{lam},{muu}")
    return acc // 36


# ────────────────────────────────────────────────────────────────────
# Block data at q₀
# ────────────────────────────────────────────────────────────────────

def block_data(q, qi):
    """Per-block (λ ⊢ 3) data: χ^λ(β_Bor) closed forms, dims, and the
    two weight conventions (Jones/TL and Wenzl z-trace)."""
    h = q - qi
    two = q + qi                    # [2]_q
    four = q**3 + q + qi + qi**3    # [4]_q
    chi = {(3,): mp.mpf(1),
           (2, 1): 2 - 3 * h**4 - h**6,
           (1, 1, 1): mp.mpf(1)}
    d = {(3,): 1, (2, 1): 2, (1, 1, 1): 1}
    y_jones = {(3,): four / two**3, (2, 1): 1 / two**2, (1, 1, 1): mp.mpf(0)}
    y_wenzl = {tuple(l): y_lambda_wenzl_bridge_numeric(l, str(q), mp.mp.dps)
               for l in partitions_of(3)}
    return chi, d, y_jones, y_wenzl


def chi21_seminormal_direct(q, qi):
    """Direct 50-dps seminormal cross-check of χ^{(2,1)}((σ1σ2⁻¹)³)."""
    h = q - qi
    a = h / (1 - q**4)
    ap = h / (1 - q**-4)
    b = mp.sqrt(a * ap + 1)
    T1 = mp.matrix([[q, 0], [0, -qi]])
    T2 = mp.matrix([[a, b], [b, ap]])
    M = (T1 * T2**-1) ** 3
    return M[0, 0] + M[1, 1]


# ────────────────────────────────────────────────────────────────────
# Tower variants
# ────────────────────────────────────────────────────────────────────

def make_tower(q, qi):
    h = q - qi
    # convention D (owner ruling 2026-08-15). Was z_C = 1/(sqrt q + sqrt(1/q)).
    # This is a LOCAL z beside this file's own load_q_50dps() call at the
    # bottom, so converting only the helper would have left z_D and z_C in
    # one file — the straddle this excision exists to remove.
    z = _markov_z(q)
    z2 = z * z
    f_pp = z
    f_pn = z
    f_nn = z - h
    E0 = mp.mpf(str(_ME_STR)) / (q * (q - 1))

    def g(x):
        return -li_2_q(-x, q, qi)

    def binding(Z, N, tau_scalar, pair_term):
        """B_can0 and B_tower for (Z, N) with a given scalar trace and
        per-bond pair-term functional pair_term(f_b) → mp.mpf."""
        A = Z + N
        ratio = (f_pp ** max(Z - 1, 0)
                 * (f_pn if Z and N else 1)
                 * f_nn ** max(N - 1, 0))
        trf = tau_scalar ** A
        dtr = trf - trf * ratio
        pair = mp.mpf(0)
        for cnt, fb in ((comb(Z, 2), f_pp), (Z * N, f_pn), (comb(N, 2), f_nn)):
            if cnt:
                pair += cnt * pair_term(fb)
        return E0 * dtr, E0 * (dtr + z2 * pair)

    return g, binding, (z, z2, f_pp, f_pn, f_nn, E0, h)


_ME_STR = None  # set in main() from codata_constants (no inline literal)


def main() -> int:
    global _ME_STR
    set_compute_dps()
    from codata_constants import M_E_MEV
    _ME_STR = str(M_E_MEV)

    q, qi, z_loaded = load_q_50dps()
    h = q - qi
    tau = (4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4)   # pipeline closed form

    chi, d, yJ, yW = block_data(q, qi)
    tau_w = sum(yW[l] * chi[l] for l in chi)          # Wenzl-convention scalar

    # ── structural identities ──
    dev_jones = mp.fabs(sum(yJ[l] * chi[l] for l in chi) - tau)
    dev_chi21 = mp.fabs(chi[(2, 1)] - chi21_seminormal_direct(q, qi))
    dev_m3_J = mp.fabs(sum(yJ[l] * d[l] for l in chi) - 1)
    dev_m3_W = mp.fabs(sum(yW[l] * d[l] for l in chi) - 1)
    convention_gap = mp.fabs(tau - tau_w)

    print("=" * 76)
    print("PROBE 4 (9b, bean v292) — per-λ Borromean brane tower, collapse-last")
    print("=" * 76)
    print(f"  τ (pipeline closed form)        = {mp.nstr(tau, 20)}")
    print(f"  Jones/TL decomposition dev      = {mp.nstr(dev_jones, 5)}")
    print(f"  χ^(2,1) closed vs seminormal    = {mp.nstr(dev_chi21, 5)}")
    print(f"  τ_W (Wenzl z-trace convention)  = {mp.nstr(tau_w, 20)}")
    print(f"  trace-convention gap |τ − τ_W|  = {mp.nstr(convention_gap, 8)}")

    g, binding, (z, z2, f_pp, f_pn, f_nn, E0, _h) = make_tower(q, qi)

    # ── RAW per-block: divergence check (invariant: Li₂^q radius |z| < q) ──
    raw_max_arg = max(mp.fabs(chi[a] * chi[b]) for a in chi for b in chi)
    raw_diverges = raw_max_arg >= q
    print(f"\n  RAW per-block max |χ_λ χ_μ| = {mp.nstr(raw_max_arg, 10)} "
          f"{'≥' if raw_diverges else '<'} q₀ = {mp.nstr(q, 10)}"
          f"  → {'DIVERGES (Li₂^q radius)' if raw_diverges else 'converges'}")

    # ── normalized per-block weights/values ──
    def norm_blocks(y):
        W = {l: y[l] * d[l] for l in y}
        r = {l: chi[l] / d[l] for l in chi}
        return W, r

    WJ, rJ = norm_blocks(yJ)
    WW, rW = norm_blocks(yW)

    def pair_term_scalar(tau_s):
        def pt(fb):
            return g(tau_s * tau_s) - g(tau_s * tau_s * fb)
        return pt

    def pair_term_perblock(W, r):
        def pt(fb):
            acc = mp.mpf(0)
            for a in W:
                if W[a] == 0:
                    continue
                for b in W:
                    if W[b] == 0:
                        continue
                    x = r[a] * r[b]
                    acc += W[a] * W[b] * (g(x) - g(x * fb))
            return acc
        return pt

    # convergence of normalized variants
    def max_arg(W, r):
        vals = [mp.fabs(r[a] * r[b]) for a in W for b in W
                if W[a] != 0 and W[b] != 0]
        return max(vals)

    conv_J = max_arg(WJ, rJ) < q
    conv_W = max_arg(WW, rW) < q

    # ── ambient H_6 per-ν variant (Wenzl weights at n = 6) ──
    parts3 = [tuple(l) for l in partitions_of(3)]
    parts6 = [tuple(l) for l in partitions_of(6)]
    # MN sanity: χ^ν(1^6) = d_ν
    mn_dims_ok = all(
        mn_char(nu, (1, 1, 1, 1, 1, 1)) == classical_dim(list(nu))
        for nu in parts6)
    # LR dimension sum: Σ_ν c^ν_{λμ} d_ν = C(6,3)·d_λ·d_μ
    lr_dims_ok = all(
        sum(lr_coeff(nu, a, b) * classical_dim(list(nu)) for nu in parts6)
        == comb(6, 3) * classical_dim(list(a)) * classical_dim(list(b))
        for a in parts3 for b in parts3)
    chi_pair = {nu: sum(lr_coeff(nu, a, b) * chi[a] * chi[b]
                        for a in parts3 for b in parts3)
                for nu in parts6}
    y6 = {nu: y_lambda_wenzl_bridge_numeric(list(nu), str(q), mp.mp.dps)
          for nu in parts6}
    # Wenzl disjoint multiplicativity validates the LR machinery:
    dev_mult = mp.fabs(sum(y6[nu] * chi_pair[nu] for nu in parts6) - tau_w**2)
    W6 = {nu: y6[nu] * classical_dim(list(nu)) for nu in parts6}
    r6 = {nu: chi_pair[nu] / classical_dim(list(nu)) for nu in parts6}
    conv_6 = max_arg(W6, r6) < q

    def pair_term_ambient(fb):
        acc = mp.mpf(0)
        for nu in parts6:
            if W6[nu] == 0:
                continue
            x = r6[nu]
            acc += W6[nu] * (g(x) - g(x * fb))
        return acc

    print(f"  MN dims ok: {mn_dims_ok};  LR dim-sum ok: {lr_dims_ok};  "
          f"Wenzl multiplicativity dev: {mp.nstr(dev_mult, 5)}")
    print(f"  convergence — perλ Jones: {conv_J}, perλ Wenzl: {conv_W}, "
          f"ambient H_6: {conv_6}")

    # ── isotope sweep ──
    variants = {
        "scalar_jones": (tau, pair_term_scalar(tau)),
        "perl_jones": (tau, pair_term_perblock(WJ, rJ)),
        "scalar_wenzl": (tau_w, pair_term_scalar(tau_w)),
        "perl_wenzl": (tau_w, pair_term_perblock(WW, rW)),
        "ambient_h6": (tau_w, pair_term_ambient),
    }

    rows = {}
    print(f"\n{'iso':5s}{'B_AME':>9s} | " + " | ".join(
        f"{v:>13s} err" for v in variants))
    for nm, Z, N, B_AME_str in ISO:
        B_AME = mp.mpf(B_AME_str)
        rows[nm] = {"Z": Z, "N": N, "B_AME": B_AME_str}
        line = f"{nm:5s}{float(B_AME):9.3f} | "
        for vn, (tau_s, pt) in variants.items():
            B0, Bt = binding(Z, N, tau_s, pt)
            # Kept as `mpf`: `B_tower` is read back for arithmetic below
            # (the committed-witness cross-check and the three tower-shift
            # maxima), so it is serialised once at `add_data` instead.
            rows[nm][vn] = {"B_can0": B0, "B_tower": Bt,
                            "errT_AME_over_B": B_AME / Bt}
            line += f"{float(Bt):13.3f} {float(B_AME / Bt):4.2f} | "
        print(line)

    # cross-check the scalar Jones baseline against the committed witness
    committed = record_upstream(HERE / "borromean-binding-recompute.witness.json", _UPSTREAM_RECORDS)
    max_base_dev = mp.mpf(0)
    for row in committed["isotopes"]:
        mine = rows[row["iso"]]["scalar_jones"]["B_tower"]
        dev = abs(mine / row["B_tower"] - 1)
        max_base_dev = max(max_base_dev, mp.mpf(dev))
    print(f"\n  scalar baseline vs committed witness: max rel dev = "
          f"{mp.nstr(max_base_dev, 5)}")

    # headline: does per-λ close the ¹⁶O 2.3×?
    def errT(iso, vn):
        return rows[iso][vn]["errT_AME_over_B"]

    max_shift = max(
        abs(rows[nm][vn]["B_tower"] / rows[nm]["scalar_jones"]["B_tower"] - 1)
        for nm, *_ in [(r[0],) for r in ISO]
        for vn in ("perl_jones",))
    max_shift_w = max(
        abs(rows[nm]["perl_wenzl"]["B_tower"]
            / rows[nm]["scalar_wenzl"]["B_tower"] - 1)
        for nm, *_ in [(r[0],) for r in ISO])
    max_shift_6 = max(
        abs(rows[nm]["ambient_h6"]["B_tower"]
            / rows[nm]["scalar_wenzl"]["B_tower"] - 1)
        for nm, *_ in [(r[0],) for r in ISO])
    print(f"  max |B_tower(per-λ)/B_tower(scalar) − 1|: "
          f"Jones {float(max_shift):.3e}, Wenzl {float(max_shift_w):.3e}, "
          f"ambient-H6 {float(max_shift_6):.3e}")
    print(f"  ¹⁶O errT: scalar {errT('16O', 'scalar_jones'):.4f} → per-λ "
          f"{errT('16O', 'perl_jones'):.4f} (ambient {errT('16O', 'ambient_h6'):.4f})")

    # ── witness ──
    wb = WitnessBuilder("probe-9b-perlambda-brane-tower", engine="mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "PROBE 4 (bean v292): per-λ collapse-last rerun of the single-"
        "pipeline Borromean brane tower. Structural: the pipeline τ is "
        "EXACTLY the SU(2)/TL (Jones) Markov decomposition y₃ᴶ=[4]/[2]³, "
        "y₂₁ᴶ=1/[2]², y_{1³}ᴶ=0 with χ^{(2,1)}=2−3h⁴−h⁶; the corpus "
        "Wenzl z-trace differs by 1.96e-4 (convention gap, recorded). "
        "RAW per-block tower (arguments χ_λχ_μ) DIVERGES — χ^{(2,1)}² "
        "≈ 3.98 > q₀ exceeds the proved Li₂^q radius |z| < q. "
        "NORMALIZED collapse-last towers (W_λ = y_λd_λ, r_λ = χ^λ/d_λ; "
        "Jones, Wenzl, and ambient-H_6 per-ν via exact LR/MN branching) "
        "all converge ∀Z and reproduce the scalar tower to ≤ ~1e-4 — "
        "the Jensen gap of g over the block spread is negligible, so "
        "carrying (y_λ, χ^λ) through g per block does NOT close the "
        "¹⁶O 2.3× normalization (scope-(a): this un-collapsed weighting "
        "alone, as-is). Shape and ∀Z convergence preserved. No new "
        "constants (Δ_λ gate respected)."
    )
    wb.set_audit_only(
        "docs/audits/2026-07-02-9b-probes-alphak-perlambda-tower.md")
    wb.add_parameter("compute_dps", mp.mp.dps)
    wb.add_parameter("q0_source",
                     "q-pinning-50-digit.witness.json (load_q_50dps)")
    wb.add_parameter("E0_MeV", mp.nstr(E0, 30))
    wb.add_data("tau_pipeline", mp.nstr(tau, 40))
    wb.add_data("tau_wenzl_convention", mp.nstr(tau_w, 40))
    wb.add_data("trace_convention_gap", mp.nstr(convention_gap, 12))
    wb.add_data("block_data", {
        "chi": {str(l): mp.nstr(chi[l], 30) for l in chi},
        "dims": {str(l): d[l] for l in d},
        "y_jones": {str(l): mp.nstr(yJ[l], 30) for l in yJ},
        "y_wenzl": {str(l): mp.nstr(yW[l], 30) for l in yW},
    })
    wb.add_data("raw_perblock", {
        "max_abs_chi_pair_arg": mp.nstr(raw_max_arg, 20),
        "q0": mp.nstr(q, 20),
        "diverges": bool(raw_diverges),
        "invariant": "Li₂^q radius |z| < q (proved, _li_2_q_util.li_2_q) "
                     "+ exact χ^{(2,1)}² > q₀",
    })
    wb.add_data("ambient_h6", {
        "wenzl_multiplicativity_dev": mp.nstr(dev_mult, 8),
        "chi_pair_by_nu": {str(nu): mp.nstr(chi_pair[nu], 25)
                           for nu in parts6},
        "converges": bool(conv_6),
    })
    wb.add_data("per_isotope", _serialise(rows))
    wb.add_data("max_tower_shift_vs_scalar", {
        "perl_jones": fmt(max_shift),
        "perl_wenzl": fmt(max_shift_w),
        "ambient_h6": fmt(max_shift_6),
    })

    wb.add_assertion(
        "pipeline_tau_is_jones_tl_decomposition",
        computed=fmt(dev_jones), expected="0", tolerance="1e-40",
        source="τ closed form = [4]/[2]³·1 + 1/[2]²·(2−3h⁴−h⁶) exactly "
               "(SU(2)/TL weights, (1³) killed)",
    )
    wb.add_assertion(
        "chi21_closed_form_vs_seminormal",
        computed=fmt(dev_chi21), expected="0", tolerance="1e-40",
        source="χ^{(2,1)}((σ1σ2⁻¹)³) = 2−3h⁴−h⁶ vs direct Hoefsmit "
               "seminormal matrix product at 50 dps",
    )
    wb.add_assertion(
        "markov_m3_both_conventions",
        computed=fmt(dev_m3_J + dev_m3_W), expected="0", tolerance="1e-40",
        source="Σ y_λ d_λ = 1 under both Jones/TL and Wenzl weights",
    )
    wb.add_assertion(
        "trace_convention_gap_recorded",
        computed=fmt(convention_gap), expected="1.9554e-4", tolerance="1e-6",
        source="|τ_pipeline − τ_Wenzl| ≈ 1.96e-4: the pipeline is the "
               "Jones/TL trace, NOT the corpus-canonical Wenzl z-trace",
    )
    wb.add_assertion(
        "raw_perblock_diverges",
        computed=int(raw_diverges), expected=1, tolerance=0,
        source="χ^{(2,1)}² ≈ 3.98 > q₀ ⇒ raw-χ per-block tower exceeds "
               "the proved Li₂^q radius (invariant-backed exclusion of "
               "the raw variant)",
    )
    wb.add_assertion(
        "normalized_variants_converge_all_Z",
        computed=int(conv_J and conv_W and conv_6), expected=1, tolerance=0,
        source="all normalized per-block pair arguments < q₀ (r_λ = χ/d)",
    )
    wb.add_assertion(
        "lr_mn_machinery_validated",
        computed=int(mn_dims_ok and lr_dims_ok and dev_mult < TOL_CROSS),
        expected=1, tolerance=0,
        source="MN dims + LR dim-sums exact; Σ_ν y_ν⁽⁶⁾χ^ν(β⊗β) = τ_W² "
               f"to {mp.nstr(dev_mult, 3)} (Wenzl §1.7 disjoint "
               "multiplicativity)",
    )
    wb.add_assertion(
        "scalar_baseline_matches_committed_witness",
        computed=fmt(max_base_dev), expected="0", tolerance="1e-6",
        source="scalar Jones tower vs borromean-binding-recompute."
               "witness.json per-isotope B_tower (q-string precision "
               "difference only)",
    )
    wb.add_assertion(
        "perlambda_does_not_close_16O",
        computed=fmt(max(max_shift, max_shift_w, max_shift_6)),
        expected="0", tolerance="0.01",
        source="max per-λ tower shift vs scalar < 1% across all isotopes "
               "and all three collapse-last variants — the ¹⁶O 2.3× "
               "normalization is untouched (REFUTED-scope-(a) for this "
               "un-collapsed (y_λ, χ^λ) weighting alone)",
    )
    wb.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
