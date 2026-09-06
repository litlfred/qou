"""
fr_pullback_k3_test.py — empirical test of conj:depth-stratified-
frobenius-reciprocity at k=3 (chirality channel).

Per prop:plancherel-term-7-formulation, "at low strata k ≤ 3 the
restricted Frobenius integral factors through specific hyperbolic-knot
ideals (e.g. 6_1 at k=3, the chirality channel)."

Per conj:depth-stratified-frobenius-reciprocity, the FR pullback
modifies the Wedderburn weight at depth k via:

  ~w_λ^{(K_k*)} := dim_q²(λ) · |χ^λ(e_{K_k*})| /
                   (Σ_μ dim_q²(μ) · |χ^μ(e_{K_k*})|)
                   · S_uniform_k

where S_uniform_k = Σ_{μ:depth=k} dim_q²(μ) / Σ_ν dim_q²(ν) is the
total uniform-Plancherel weight at depth k (preserved by the FR
pullback, which only REDISTRIBUTES weight within the depth-k stratum,
not rescales it).

NORMALIZATION CORRECTED 2026-09-04 (bean qou-7o7h): the denominator was
[n]_q!, which is NOT a probability measure in the balanced q-integer
convention this corpus uses, and whose defect c_n GROWS with n — so it
distorted this test's cross-atom metric. Fixing it REVERSED the knot
ranking; see the verdict note in the witness and
docs/audits/2026-09-04-plancherel-convention-gap.md. The chi path was
moved from the f64 kernel to MPFR at the same time.

This script tests the FR pullback at k=3 with candidate distinguished
knots K_3* ∈ {4_1, 5_2, 6_1} using the repo's canonical braid words
from `_deprecated/hyperbolic_knot_db_extended.py`.

Reference: prop:plancherel-term-7-formulation,
           conj:depth-stratified-frobenius-reciprocity.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

import pyhecke_native  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    M_E_MEV,
)
from functools import lru_cache  # noqa: E402
from mass_at_3A_proper import qfac  # noqa: E402  (dim_q now local, mpmath)
from q_parameter import Q as Q0, Q_50_DIGIT_STR  # noqa: E402
from qou_substrate.constants import Q as Q0_PROTON  # noqa: E402 — anchor-independent proton pin (qou-6p3b Tranche C)


# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

B_AME = {
    "D":   AME_B_DEUTERON_MEV_VALIDATION,
    "T":   AME_B_TRITIUM_MEV_VALIDATION,
    "3He": AME_B_HE3_MEV_VALIDATION,
    "4He": AME_B_HE4_MEV_VALIDATION,
}

ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}


# Distinguished hyperbolic-knot candidates at depth k=3.
# Braid words taken from the repo's canonical table:
#   `_deprecated/hyperbolic_knot_db_extended.py:43-46`
# Format: tuple of signed gen indices (Conway form), where positive
# = σ_g, negative = σ_g^{-1}.
CANDIDATE_KNOTS_CONWAY = {
    "4_1": ((1, -2, 1, -2), "2.0298832"),
    "5_2": ((1, 1, 1, -2, 1, -2), "2.8281220"),
    "6_1": ((1, 1, -2, 1, -2, -2), "3.1639633"),
}


def conway_to_pyhecke(word_signed: tuple[int, ...]) -> list[tuple[int, int]]:
    """Convert Conway-signed braid word to pyhecke_native (sign, |gen|)."""
    out: list[tuple[int, int]] = []
    for s in word_signed:
        sign = 1 if s > 0 else -1
        g = abs(s)
        out.append((sign, g))
    return out


CANDIDATE_KNOTS = {
    name: conway_to_pyhecke(w_signed)
    for name, (w_signed, _vol) in CANDIDATE_KNOTS_CONWAY.items()
}


def vanishing_threshold() -> mp.mpf:
    """Threshold for treating |z| as zero, tied to current mp.dps."""
    return mp.mpf(10) ** (5 - mp.mp.dps)


def alpha_k(k: int) -> mp.mpf:
    """Structural prefactor per prop:plancherel-term-7-formulation."""
    z_mark = Q0**3 / (Q0**2 + 1)
    G = mp.catalan
    if k in (0, 1, 3):
        return mp.mpf(1)
    if k == 2:
        return z_mark ** 2
    return M_E_MEV * 8 * G


def embed_knot_braid(knot_word: list[tuple[int, int]],
                      n_strands: int) -> list[tuple[int, int]]:
    """Embed a small braid word into H_n via Wenzl.

    H_n has generators σ_1..σ_{n-1} (1-indexed), so the max
    generator index used must be ≤ n - 1.
    """
    max_gen = max(g for _, g in knot_word)
    if max_gen > n_strands - 1:
        raise ValueError(
            f"Knot braid uses gen {max_gen} but H_{n_strands} only "
            f"has generators 1..{n_strands - 1}")
    return knot_word


def chi_lambda_braid_via_rust(shape: list[int],
                                braid_word_signed: list,
                                q_str: str) -> mp.mpf:
    """χ^λ(β) at q via pyhecke_native, MPFR tier (50 dps).

    FIXED 2026-09-04 (bean qou-7o7h follow-up): this took `q: float` and
    called the f64 kernel, so every FR weight in this test carried ~1e-16
    rounding — a NO-FLOAT64 violation on the production path, and one
    that a caller could not see because the f64-ness was buried behind a
    `q_f64 = float(Q0)` two frames up. `chi_lambda_braid_mpfr` takes the
    q as a DECIMAL STRING precisely to avoid the lossy f64 boundary
    conversion, and returns a decimal string for the caller to parse.
    """
    word = [(int(s), int(g)) for (s, g) in braid_word_signed]
    return mp.mpf(pyhecke_native.chi_lambda_braid_mpfr(
        list(shape), word, str(q_str), 50))


def _hooks(shape: tuple) -> list:
    """Hook lengths of a Young diagram, as a flat list."""
    conj = [sum(1 for r in shape if r > c) for c in range(shape[0])]
    return [shape[i] - j + conj[j] - i - 1
            for i in range(len(shape)) for j in range(shape[i])]


@lru_cache(maxsize=None)
def _qint_mp(k: int) -> mp.mpf:
    """Balanced q-integer [k]_q at the 50-digit q₀, in mpmath."""
    q = mp.mpf(Q_50_DIGIT_STR)
    return (q ** k - (1 / q) ** k) / (q - 1 / q)


@lru_cache(maxsize=None)
def dim_q_mp(shape: tuple) -> mp.mpf:
    """d_q(λ) by the q-hook-length formula, in MPFR at the 50-digit q₀.

    ADDED 2026-09-05 (bean qou-u6zt). This test used
    `hecke_characters.dim_q(shape, Q0_PROTON)`, and BOTH halves of that
    were float64:

      - `Q0_PROTON` is `qou_substrate.constants.Q`, a Python float —
        2.7e-17 from the 50-digit string. Note `q_parameter.Q`, the
        other q imported here, is the SAME float, so swapping one for
        the other fixes nothing; the fix has to reach the string.
      - more importantly `hecke_characters.dim_q` computes with
        `math.prod` over `math`-level q-integers, so it is float64 **by
        construction** and cannot carry a higher-precision q at all.

    That mattered here beyond the usual NO-FLOAT64 grounds: the χ path
    of this test was moved to the MPFR kernel on 2026-09-04, so the
    products `|χ| · d_q` were mixing a 50-dps character with a float64
    dimension — the weaker factor silently capping the pair. Computing
    d_q in mpmath is what makes that χ upgrade mean anything.
    """
    n = sum(shape)
    num = mp.mpf(1)
    for k in range(1, n + 1):
        num *= _qint_mp(k)
    den = mp.mpf(1)
    for hk in _hooks(shape):
        den *= _qint_mp(hk)
    return num / den


@lru_cache(maxsize=None)
def _qfactorial_mp(n: int) -> mp.mpf:
    """[n]_q! = ∏_{k=1}^n [k]_q, in MPFR at the 50-digit q₀."""
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= _qint_mp(k)
    return out


@lru_cache(maxsize=None)
def _f_lambda(shape: tuple) -> int:
    """#SYT(λ) by the classical hook-length formula — exact integer.

    This is the CLASSICAL Wedderburn block dimension. By Tits deformation
    `H_n(q) ≅ ℂ[S_n]` at generic q, so the block indexed by λ really does
    have dimension `f^λ`, not `d_q(λ)` — which is the structural reason the
    Molien numerator carries one of each rather than two quantum dimensions.
    """
    n = sum(shape)
    num = 1
    for k in range(1, n + 1):
        num *= k
    den = 1
    for h in _hooks(shape):
        den *= h
    assert num % den == 0, "hook-length formula must divide exactly"
    return num // den


@lru_cache(maxsize=None)
def _content_sum(shape: tuple) -> int:
    """κ_λ = Σ_□ c(□), c(□) = j − i. Equals n(λ') − n(λ)."""
    return sum(j - i for i in range(len(shape)) for j in range(shape[i]))


@lru_cache(maxsize=None)
def molien_weight_mp(shape: tuple) -> mp.mpf:
    """The Molien / fake-degree weight `f^λ · q^{−κ_λ} · d_q(λ) / [n]_q!`.

    CANONICAL as of the owner ruling of 2026-09-05 (bean `qou-oots`). Three
    facts decided it, all measured rather than argued:

      - It sums to 1 **by an identity**, every n and every q>1
        (`QOU.MathlibExt.NormalizedSumUnconditional.molienSum_eq_qFactorial`,
        Lean, sorry-free) — where `d_q²/D²` divides by whatever makes the
        sum 1, and the historical `d_q²/[n]_q!` is not normalised at all.
      - The κ exponent is **forced**, not chosen: over c ∈ [−3,3] only
        c = ±1 makes `f^λ q^{cκ} d_q` a measure, and those two are one
        measure on transposed diagrams
        (`probes/plancherel_deformation_uniqueness_probe.py`).
      - It **is** the literature's q-Plancherel measure `M_{n,q²}` — exact
        equality of rationals over every partition of n ≤ 9
        (`probes/molien_feray_meliot_bridge_probe.py`) — so Féray–Méliot's
        asymptotics apply to it and to nothing else in the corpus.

    The `q^{−κ}` is load-bearing, not decoration: drop it and the sum is
    ≈0.457 at n=6 rather than 1. That mistake was made and caught while
    writing the uniqueness probe.
    """
    q = mp.mpf(Q_50_DIGIT_STR)
    return (mp.mpf(_f_lambda(shape)) * q ** (-_content_sum(shape))
            * dim_q_mp(shape) / _qfactorial_mp(sum(shape)))


# The two arms. Molien is canonical; `dimq2_selfnorm` is retained as a
# LABELLED comparison arm, not as a fallback — see the module docstring.
WEIGHT_FAMILIES = ("molien", "dimq2_selfnorm")
PRIMARY_FAMILY = "molien"


def base_weights(by_partition: list, family: str) -> dict:
    """Normalised base weight per partition, for one weight family.

    Both arms are probability measures on the SAME index set (all λ ⊢ n), so
    they are directly comparable per partition — unlike the `V^{⊗n}`
    Schur–Weyl share, which lives on λ with ≤ N rows and is therefore not a
    third arm here.

    They are NOT close, which is why both are reported rather than one being
    a sanity check on the other. Measured: the ratio `w_molien/w_dimq2`,
    normalised to its own mean, spreads 1.87× at n=3, 22.9× at n=6 and
    **1831× at n=9** — monotone from the single row to the single column,
    which is `q^{−κ}` doing what it should. Since `n = 3A`, n=9 is A=3.
    """
    if family == "molien":
        return {tuple(p["partition"]): molien_weight_mp(tuple(p["partition"]))
                for p in by_partition}
    if family == "dimq2_selfnorm":
        denom = selfnorm_denominator(by_partition, 0)
        out = {}
        for p in by_partition:
            shape = tuple(p["partition"])
            dq = dim_q_mp(shape)
            out[shape] = (dq * dq) / denom
        return out
    raise ValueError(f"unknown weight family {family!r}; "
                     f"expected one of {WEIGHT_FAMILIES}")


def selfnorm_denominator(by_partition: list, n_strands: int) -> mp.mpf:
    """Σ_μ dim_q²(μ) — the SELF-NORMALIZING denominator.

    CORRECTED 2026-09-04 (bean qou-7o7h).  This test previously divided
    dim_q² by [n]_q!, the textbook q-Plancherel form, which is a
    probability measure at q = 1 and **at q = 1 only** — c_n =
    Σ_λ dim_q²/[n]_q! is 0.991 / 1.111 / 1.517 at n = 6/9/12 and grows
    with n.

    (An earlier version of this docstring said the textbook form is also
    a measure "in the ASYMMETRIC q-integer convention", i.e. that the
    failure was a convention artifact. That was WRONG and is retracted:
    measured, the asymmetric convention is *further* from 1 at five of
    six n. The defect is structural — the q-deformation breaks Burnside
    Σ_λ (f^λ)² = n! — and no convention restores it.)

    Because the binding functional is linear in the weights, the whole
    effect is that B scales by c_n: harmless within one atom, and NOT
    harmless across atoms, since n = 3A differs.  This test's headline
    metric is max/min ACROSS atoms, so it was distorted — it inflated
    ⁴He (largest n) by 1.517 for every candidate knot, which pinned ⁴He
    as the max and swamped the real spread.  See
    docs/audits/2026-09-04-plancherel-convention-gap.md.
    """
    total = mp.mpf(0)
    for p in by_partition:
        dq = dim_q_mp(tuple(p["partition"]))
        total += dq * dq
    return total


def fr_pullback_weight_per_partition(
    by_partition: list, n_strands: int, k_depth: int,
    knot_word: list, q_str: str, family: str = PRIMARY_FAMILY
) -> tuple[dict, dict]:
    """Compute FR-pullback weight + errors per partition, for one family.

    Returns (fr_weights, errors):
      - fr_weights at depth k_depth: redistribute the family's base weight
        proportionally to |χ^λ(K_dist)|, preserving total depth-k mass.
      - errors: any per-partition chi-computation failures
        (specific exceptions only; bugs propagate).

    PARAMETERISED BY FAMILY 2026-09-05 (bean `qou-oots`, owner ruling). The
    redistribution rule and the base measure are two independent choices and
    both have to be named; this function used to hard-code the second as
    `d_q²/Σd_q²`. The rule itself is family-agnostic — it rescales whatever
    base weights it is handed so that the depth-k stratum keeps its total —
    so nothing about the FR mechanism changes with the arm.
    """
    base = base_weights(by_partition, family)
    eps = vanishing_threshold()

    fr_weights: dict = {}
    errors: dict = {}
    chi_at_k_dist: dict = {}
    z_norm_unweighted = mp.mpf(0)  # Σ w_base · |χ| at depth k
    s_uniform_at_depth = mp.mpf(0)  # Σ w_base at depth k

    for p in by_partition:
        shape = tuple(p["partition"])
        depth = len(shape) - 1
        w0 = base[shape]
        if depth != k_depth:
            fr_weights[shape] = w0
            continue
        s_uniform_at_depth += w0
        try:
            chi_K = chi_lambda_braid_via_rust(list(shape), knot_word, q_str)
        except (ValueError, RuntimeError, OverflowError) as exc:
            chi_K = mp.mpf(0)
            errors[shape] = f"{type(exc).__name__}: {exc}"
        chi_at_k_dist[shape] = chi_K
        z_norm_unweighted += w0 * mp.fabs(chi_K)

    # Normalize so FR-pulled-back weights at depth k SUM to the base-measure
    # total at depth k (preserves total depth-3 mass; FR only redistributes
    # within the stratum).
    if z_norm_unweighted < eps:
        for shape in chi_at_k_dist:
            fr_weights[shape] = base[shape]
    else:
        scale = s_uniform_at_depth / z_norm_unweighted
        for shape, chi_K in chi_at_k_dist.items():
            fr_weights[shape] = base[shape] * mp.fabs(chi_K) * scale
    return fr_weights, errors


def phi_k_with_weights(
    by_partition: list, n_strands: int, k: int,
    weights: dict
) -> mp.mpf:
    """Φ_k(K, T) using arbitrary weight per partition."""
    total = mp.mpf(0)
    eps = vanishing_threshold()
    for p in by_partition:
        shape = tuple(p["partition"])
        if len(shape) - 1 != k:
            continue
        chi = mp.mpf(str(p["chi_lambda"]))
        dq = dim_q_mp(shape)
        magnitude = mp.fabs(chi) * dq
        if magnitude < eps:
            continue
        w = weights.get(shape, mp.mpf(0))
        total += w * mp.log(magnitude)
    return total


def precompute_uniform_weights(by_partition: list, n_strands: int,
                               family: str = PRIMARY_FAMILY) -> dict:
    """Base (un-pulled-back) weights for one family — see `base_weights`."""
    return base_weights(by_partition, family)


def compute_atom_binding_fr(atom: str, knot_word: list[tuple[int, int]],
                             knot_name: str,
                             family: str = PRIMARY_FAMILY) -> dict:
    """Compute B(K) with FR pullback through `knot_word` at k=3."""
    Z, N = ZN[atom]
    A = Z + N
    n_strands = 3 * A
    w_path = HERE / f"atom-chi-rust-{atom.lower()}.witness.json"
    if not w_path.exists():
        return {"deferred": True,
                "reason": f"Run compute_atom_chi_rust.py {atom} first"}
    w = json.loads(w_path.read_text())
    atom_data = w["data"]["atom"]
    free_data = w["data"]["free"]
    upstream_sha = w.get("commitSha", "unknown")

    embedded_word = embed_knot_braid(knot_word, n_strands)
    q_str = str(Q0)

    fr_atom_weights, atom_errors = fr_pullback_weight_per_partition(
        atom_data["by_partition"], n_strands, 3, embedded_word, q_str, family)
    fr_free_weights, free_errors = fr_pullback_weight_per_partition(
        free_data["by_partition"], n_strands, 3, embedded_word, q_str, family)

    uniform_atom_weights = precompute_uniform_weights(
        atom_data["by_partition"], n_strands, family)
    uniform_free_weights = precompute_uniform_weights(
        free_data["by_partition"], n_strands, family)

    # FR at depth 3, uniform elsewhere
    final_atom_weights = dict(uniform_atom_weights)
    final_free_weights = dict(uniform_free_weights)
    for shape, w in fr_atom_weights.items():
        if len(shape) - 1 == 3:
            final_atom_weights[shape] = w
    for shape, w in fr_free_weights.items():
        if len(shape) - 1 == 3:
            final_free_weights[shape] = w

    delta_phi_total = mp.mpf(0)
    for d in range(n_strands):
        phi_atom = phi_k_with_weights(
            atom_data["by_partition"], n_strands, d, final_atom_weights)
        phi_free = phi_k_with_weights(
            free_data["by_partition"], n_strands, d, final_free_weights)
        delta_phi_total += alpha_k(d) * (phi_free - phi_atom)

    return {
        "Z": Z, "N": N, "A": A, "n_strands": n_strands,
        "knot_name": knot_name,
        "weight_family": family,
        "B_MeV": fmt(delta_phi_total),
        "B_pred_sign": "+" if delta_phi_total > 0 else "-",
        "upstream_witness": f"atom-chi-rust-{atom.lower()}.witness.json",
        "upstream_commitSha": upstream_sha,
        "atom_chi_errors_count": len(atom_errors),
        "free_chi_errors_count": len(free_errors),
    }


def compute_atom_binding_no_fr(atom: str,
                               family: str = PRIMARY_FAMILY) -> dict:
    """B(K) with NO FR pullback — uniform weights at every depth.

    ADDED 2026-09-04 (bean qou-7o7h). The baseline was previously the
    hardcoded literal `1.82`, carried from a run under the OLD textbook
    normalization. Once the weights here are self-normalized, comparing
    corrected FR figures against that literal straddles two
    normalizations and overstates every improvement — it reported 6_1 as
    "+42.4% vs baseline" when the like-for-like figure is much smaller.
    The baseline is now COMPUTED through the same path as the FR
    variants, so both sides always share a normalization.
    """
    Z, N = ZN[atom]
    A = Z + N
    n_strands = 3 * A
    w_path = HERE / f"atom-chi-rust-{atom.lower()}.witness.json"
    w = json.loads(w_path.read_text())
    atom_data = w["data"]["atom"]
    free_data = w["data"]["free"]

    wA = precompute_uniform_weights(atom_data["by_partition"], n_strands, family)
    wF = precompute_uniform_weights(free_data["by_partition"], n_strands, family)

    delta_phi_total = mp.mpf(0)
    for d in range(n_strands):
        phi_atom = phi_k_with_weights(
            atom_data["by_partition"], n_strands, d, wA)
        phi_free = phi_k_with_weights(
            free_data["by_partition"], n_strands, d, wF)
        delta_phi_total += alpha_k(d) * (phi_free - phi_atom)
    return {"A": A, "weight_family": family, "B_MeV": fmt(delta_phi_total),
            "B_pred_sign": "+" if delta_phi_total > 0 else "-"}


def main() -> int:
    set_compute_dps()
    builder = WitnessBuilder("fr-pullback-k3-test")
    builder.set_description(
        "Empirical test of conj:depth-stratified-frobenius-reciprocity "
        "at k=3 with candidate distinguished knots {4_1, 5_2, 6_1} "
        "via Wenzl embedding into H_{3A}. "
        "TWO ARMS, reported side by side (owner ruling 2026-09-05, bean "
        "qou-oots). PRIMARY / CANONICAL: the Molien weight "
        "f^lam*q^{-kappa}*d_q/[n]_q!, which is the unique corpus numerator "
        "normalised by an IDENTITY rather than by division (Lean "
        "molienSum_eq_qFactorial, sorry-free, all n and all q>1), whose "
        "kappa exponent is FORCED up to conjugation, and which IS the "
        "literature's q-Plancherel measure M_{n,q^2} (exact over every "
        "partition of n<=9), so Feray-Meliot's asymptotics apply to it and "
        "to nothing else here. SECOND ARM, labelled not fallback: "
        "d_q^2/D^2 (self-normalized, Reshetikhin-Turaev / Verlinde). "
        "WHY BOTH: the R1/R2/R3 requirement set does NOT separate them -- "
        "R2 asks only that the normaliser be n-independent and both "
        "satisfy it -- and they are not close, the ratio between them "
        "spreading 1.87x / 22.9x / 1831x at n = 3/6/9 (n = 3A, so n=9 is "
        "A=3). Quoting only the primary would be an overclaim. "
        "THE FR pullback redistributes within a depth stratum and "
        "preserves that stratum's total, so the redistribution rule and "
        "the base measure are two independent choices; the rule is "
        "family-agnostic and is unchanged between arms. "
        "THE TWO ARMS DISAGREE ON THE BEST KNOT, which is the whole "
        "reason for reporting both: Molien -> 5_2 (+21.4% vs its own "
        "baseline 1.5489x, with 6_1 at 1.6068x, WORSE than baseline); "
        "d_q^2/D^2 -> 6_1 (+1.7% vs its own baseline 1.0660x). The "
        "canonical arm gives the FR MECHANISM stronger support and the "
        "paper's 6_1 NAMING none. "
        "COMPARABILITY: the 1.82x baseline / 1.5015x best-4_1 figures "
        "quoted downstream are from a PRE-MIGRATION d_q^2/[n]_q! run and "
        "are NOT comparable with either arm here. "
        "FULL FAMILY SURVEY (bean qou-oots, same harness): "
        "d_q^2/[n]_q! -> 4_1 best; d_q^2/D^2 -> 6_1; Molien -> 5_2; "
        "y_lambda -> vacuous (SU(N) row cap zeroes depth >= 2). So no "
        "k=3 knot conclusion from this producer is interpretable "
        "without naming the family it was computed under. "
        "SCOPE: this is the FR-VARIANCE route. The corpus's structural "
        "6_1 naming at curvature-rank 3 comes from the GB-filtration "
        "route (prop:curvature-rank-gb-stratification), which carries "
        "no weight family at all and is untouched by any of the above. "
        "Braid words sourced from "
        "_deprecated/hyperbolic_knot_db_extended.py canonical table."
    )
    builder.add_parameter("m_e_CAL1_MeV", str(M_E_MEV))
    builder.add_parameter("q0_50dps", str(Q0))

    builder.add_data("candidate_knots", {
        name: {
            "conway_word": list(w_signed),
            "hyperbolic_volume_cross_check": vol,
            "n_crossings": len(w_signed),
        }
        for name, (w_signed, vol) in CANDIDATE_KNOTS_CONWAY.items()
    })

    upstream_witnesses = []
    for atom in ("D", "T", "3He", "4He"):
        w_path = HERE / f"atom-chi-rust-{atom.lower()}.witness.json"
        if w_path.exists():
            upstream_witnesses.append(
                str(w_path.relative_to(HERE.parent.parent)))
    builder.add_data("upstream_witnesses", upstream_witnesses)

    def run_family(family: str) -> dict:
        """The whole k=3 comparison under ONE weight family."""
        all_results = {}
        for knot_name, knot_word in CANDIDATE_KNOTS.items():
            print(f"\n=== [{family}] FR pullback at k=3 via {knot_name} "
                  f"(braid len {len(knot_word)}) ===")
            print(f"{'atom':<6} {'A':>3} {'B_MeV':>10} {'B_AME':>10} "
                  f"{'ratio':>8} {'sign':>5}")
            results = {}
            for atom in ("D", "T", "3He", "4He"):
                r = compute_atom_binding_fr(atom, knot_word, knot_name, family)
                if r.get("deferred"):
                    continue
                B_pred = mp.mpf(r["B_MeV"])
                B_emp = B_AME[atom]
                ratio = B_pred / B_emp
                r["B_AME_MeV"] = fmt(B_emp)
                r["ratio_pred_over_AME"] = fmt(ratio)
                results[atom] = r
                print(f"  {atom:<6} {r['A']:>3} {float(B_pred):>10.4f} "
                      f"{float(B_emp):>10.4f} {float(ratio):>8.4f} "
                      f"{r['B_pred_sign']:>5}")
            ratios = [abs(mp.mpf(r["ratio_pred_over_AME"]))
                      for r in results.values()]
            if ratios:
                rmin, rmax = min(ratios), max(ratios)
                mom = rmax / rmin if rmin > 0 else mp.inf
                signs_correct = all(r["B_pred_sign"] == "+"
                                    for r in results.values())
                print(f"  max/min = {float(mom):.4f}, "
                      f"signs +: {signs_correct}")
                all_results[knot_name] = {
                    "per_atom": results,
                    "max_over_min": fmt(mom),
                    "all_signs_correct": signs_correct,
                }
        base_ratios = [abs(mp.mpf(compute_atom_binding_no_fr(a, family)["B_MeV"])
                           / B_AME[a]) for a in ("D", "T", "3He", "4He")]
        bl = max(base_ratios) / min(base_ratios)
        best_knot, best_mom = None, bl
        for kname, r in all_results.items():
            mom = mp.mpf(r["max_over_min"])
            if r["all_signs_correct"] and mom < best_mom:
                best_mom, best_knot = mom, kname
        return {"weight_family": family, "baseline_variance_no_fr": fmt(bl),
                "per_knot": all_results, "best_knot": best_knot,
                "best_max_over_min": fmt(best_mom)}

    # ── TWO ARMS ────────────────────────────────────────────────────────
    # Owner ruling 2026-09-05 (bean qou-oots): Molien is canonical. The
    # `dim_q²/D²` arm is retained as a LABELLED comparison, not a fallback.
    # Both are reported because they are not close — the ratio between them
    # spreads 1831× at n=9 (= A=3), so this is two answers side by side, not
    # a primary with a sanity check. Reporting only the primary would be the
    # overclaim, since the requirement set R1/R2/R3 does not separate them.
    arms = {fam: run_family(fam) for fam in WEIGHT_FAMILIES}
    builder.add_data("weight_family_arms", arms)
    builder.add_data("primary_weight_family", PRIMARY_FAMILY)
    builder.add_data("weight_family_ruling",
                     "Molien f^λ·q^{-κ}·d_q/[n]_q! is CANONICAL (owner "
                     "ruling 2026-09-05, bean qou-oots). It is the unique "
                     "corpus numerator normalised by an IDENTITY rather "
                     "than by division (Lean molienSum_eq_qFactorial, "
                     "sorry-free, all n, all q>1); its κ exponent is forced "
                     "up to conjugation; and it IS the literature's "
                     "q-Plancherel measure M_{n,q²} (exact, all partitions "
                     "of n≤9), so Féray–Méliot's asymptotics apply to it "
                     "and to nothing else here. dim_q²/D² is kept as a "
                     "labelled second arm because the requirement set does "
                     "NOT separate the two — both are legitimate "
                     "probability measures — and they differ by up to "
                     "1831× per partition at n=9.")

    # Everything below reports the PRIMARY arm; the second arm is in
    # `weight_family_arms` and in the cross-arm comparison at the end.
    all_results = arms[PRIMARY_FAMILY]["per_knot"]

    # Baseline COMPUTED through the same path (see
    # compute_atom_binding_no_fr) so it shares the FR variants'
    # normalization; it used to be the literal 1.82 from a textbook-
    # normalized run, which straddled two normalizations once the
    # weights here were corrected.
    baseline = mp.mpf(arms[PRIMARY_FAMILY]["baseline_variance_no_fr"])
    builder.add_data("baseline_variance_no_fr", fmt(baseline))
    builder.add_data("baseline_provenance",
                     "computed in-run via compute_atom_binding_no_fr under "
                     "the PRIMARY family (Molien), so it shares the FR "
                     "variants' measure. Was the hardcoded literal 1.82 "
                     "under the old textbook normalization — bean "
                     "qou-7o7h. The second arm's baseline is in "
                     "weight_family_arms.dimq2_selfnorm.")
    builder.add_data("per_knot", all_results)

    print("\n=== Cross-arm comparison (both weight families) ===")
    print(f"{'family':<18} {'baseline':>10} {'best knot':>10} {'best m/m':>10}")
    for fam, a in arms.items():
        tag = "  <- CANONICAL" if fam == PRIMARY_FAMILY else "  (comparison)"
        print(f"  {fam:<18} {float(mp.mpf(a['baseline_variance_no_fr'])):>10.4f} "
              f"{str(a['best_knot']):>10} "
              f"{float(mp.mpf(a['best_max_over_min'])):>10.4f}{tag}")
    arms_agree = (arms["molien"]["best_knot"]
                  == arms["dimq2_selfnorm"]["best_knot"])
    builder.add_data("arms_agree_on_best_knot", arms_agree)
    print(f"  arms agree on best knot: {arms_agree}")

    print("\n=== Summary: variance comparison (PRIMARY arm: "
          f"{PRIMARY_FAMILY}) ===")
    print(f"{'knot':<6} {'max/min':>10} {'signs +':>8} {'vs baseline':>14}")
    print(f"  {'(none)':<6} {float(baseline):>10.4f} "
          f"{'(yes)':>8} {'baseline':>14}")
    best_knot = None
    best_mom = baseline
    for kname, r in all_results.items():
        mom = mp.mpf(r["max_over_min"])
        improvement = (baseline - mom) / baseline * 100
        sign = "+" if r["all_signs_correct"] else "-"
        print(f"  {kname:<6} {float(mom):>10.4f} {sign:>8} "
              f"{float(improvement):>+11.1f}%")
        if r["all_signs_correct"] and mom < best_mom:
            best_mom = mom
            best_knot = kname

    paper_knot = "6_1"
    paper_knot_mom = (all_results.get(paper_knot, {}).get("max_over_min")
                      if paper_knot in all_results else None)
    paper_naming_validated = (best_knot == paper_knot)
    n_beating_baseline = sum(1 for r in all_results.values()
                             if mp.mpf(r["max_over_min"]) < baseline)
    if best_knot:
        # Grade by improvement RELATIVE to the baseline, not by an
        # absolute cut on best_mom. RECALIBRATED 2026-09-04 (bean
        # qou-7o7h): the old rule was `STRONG if best_mom < 1.5`, which
        # was tuned when the baseline was the textbook-normalized 1.82.
        # Against the corrected baseline (~1.07) that cut is satisfied
        # by anything at all, so it reported "STRONG support" for what
        # is in fact a ~2% improvement. An absolute threshold cannot
        # survive a change in the baseline it was calibrated against.
        gain = (baseline - best_mom) / baseline
        general_support = ("STRONG" if gain > 0.25 else
                           "MODEST" if gain > 0.05 else "MARGINAL")
        other_fam = [f for f in WEIGHT_FAMILIES if f != PRIMARY_FAMILY][0]
        arm_note = (f" SECOND ARM ({other_fam}): best knot "
                    f"{arms[other_fam]['best_knot']} at "
                    f"{float(mp.mpf(arms[other_fam]['best_max_over_min'])):.4f}× "
                    f"vs its own baseline "
                    f"{float(mp.mpf(arms[other_fam]['baseline_variance_no_fr'])):.4f}×; "
                    f"the two arms "
                    f"{'AGREE' if arms_agree else 'DISAGREE'} on the best "
                    f"knot. Both arms are reported because the R1/R2/R3 "
                    f"requirement set does not separate them and they are "
                    f"not close (up to 1831× per partition at n=9 = A=3) — "
                    f"quoting only the primary would be an overclaim.")
        if paper_naming_validated:
            verdict = (f"[PRIMARY ARM: {PRIMARY_FAMILY}, canonical per owner "
                       f"ruling 2026-09-05] FR conjecture {general_support} "
                       f"support: K_3* = {best_knot} (matches paper) is the "
                       f"best candidate at {float(best_mom):.4f}× vs a no-FR "
                       f"baseline of {float(baseline):.4f}× — an improvement of "
                       f"{float(gain) * 100:.1f}%. {n_beating_baseline} of "
                       f"{len(all_results)} candidates beat the baseline "
                       f"at all; the others make the cross-atom variance "
                       f"WORSE. The previously published 1.82× baseline was "
                       f"inflated by the textbook dim_q²/[n]_q! form, so the "
                       f"large apparent variance closure it implied was "
                       f"mostly a normalization artifact." + arm_note)
        else:
            paper_str = (f"{float(mp.mpf(paper_knot_mom)):.3f}×"
                          if paper_knot_mom else "n/a")
            verdict = (
                f"[PRIMARY ARM: {PRIMARY_FAMILY}, canonical per owner ruling "
                f"2026-09-05] FR conjecture {general_support} support: "
                f"empirically best K_3* = {best_knot} ({float(best_mom):.3f}×, "
                f"baseline {float(baseline):.4f}×); paper's named K_3* = "
                f"{paper_knot} gives {paper_str} (NOT empirically best under "
                f"this arm). Paper's naming K_3* = 6_1 NOT validated by the "
                f"FR-VARIANCE route under this weight family — note the "
                f"corpus's structural 6_1 naming comes from the "
                f"GB-filtration route (prop:curvature-rank-gb-stratification), "
                f"which carries NO weight family and is untouched by this "
                f"test either way (bean qou-9b50)." + arm_note)
    else:
        verdict = ("No candidate knot improves variance; "
                   "FR-pullback form or specific knot identity may "
                   "need refinement.")
    builder.add_data("verdict", verdict)
    builder.add_data("best_knot", best_knot)
    builder.add_data("best_max_over_min", best_mom)
    builder.add_data("paper_named_knot", paper_knot)
    builder.add_data("paper_named_knot_max_over_min",
                      fmt(mp.mpf(paper_knot_mom))
                      if paper_knot_mom else None)
    builder.add_data("paper_naming_validated", paper_naming_validated)
    print(f"\n  {verdict}")

    builder.add_assertion(
        "data_loaded",
        computed=fmt(B_AME["D"]),
        expected=fmt(AME_B_DEUTERON_MEV_VALIDATION),
        tolerance=1e-10,
        unit="B(D) MeV",
        source="AME 2020 deuteron binding — SELF-COMPARISON, see caveat",
    )
    builder.add_caveat(
        "SELF-FULFILLING ASSERTION (recorded, not repaired): "
        "`data_loaded` compares B_AME['D'] against a literal copy of the "
        "same number typed a few hundred lines away — x == x with a "
        "tolerance, so it can only pass and gates nothing. Noticed "
        "2026-09-04 while clearing this producer's raw-float64 fields "
        "(the literal was the last one). Repairing it properly means "
        "rebuilding the four B_AME entries from the CODATA mass-excess "
        "table so the check has an independent second source — the same "
        "fix fr_pullback_borromean_h3a_test already carries as "
        "`b_ame_cross_check`. That is a content change to this "
        "producer's inputs and is deliberately NOT bundled into a "
        "normalization fix; it is the honest next step, not this one.")
    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
