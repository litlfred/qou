"""
delta_lambda_full_variance_phase5e_1.py — Phase 5e.1 probe.

Closes the loop on Phase 5d.5b by re-running the K_k* variance test
under the FULL PR #801 depth-stratified formula (with α_k weights
and the (Φ_k_free − Φ_k_atom) difference) instead of the simplified
log|χ|-only version. Also tests the Gram-inverse-weighted variant
(per the repo owner's "using gram inverse basis?" direction) for
H_3-supported K_k* candidates.

FULL FORMULA (per binding_depth_stratified_rust.py):

  α_k:    α_0 = α_1 = α_3 = 1;  α_2 = z²;  α_{k≥4} = m_e · 8G
  Φ_k(β) := Σ_{depth(λ)=k} (dim_q²(λ) / [n]_q!) · log|χ^λ(β) · dim_q(λ)|
  B(K) = Σ_k α_k · (Φ_k(β_K_free) − Φ_k(β_K_atom))

K_k*-WEIGHTED VARIANT:

  ~w_λ^(K_k*) = (dim_q²(λ) / [n]_q!) · χ^λ(e_{K_k*}) / Z_norm(K_k*, k, n)
  Φ_k^FR(β; K_k*) = Σ_{depth(λ)=k} ~w_λ^(K_k*) · log|χ^λ(β) · dim_q(λ)|

GRAM-INVERSE VARIANT (at H_3 only):

  Decompose K_k* in NF basis: K_k* = Σ c_i b_i  (i ∈ {γ, σ_0, σ_1, L_+, L_-, e^-})
  Compute Frobenius dual: K_k*∨ = G^{-1} · c   (G_ij = tr_M(b_i · b_j))
  Use χ^λ(K_k*∨) instead of χ^λ(K_k*) in the FR weight above.

This respects the Markov-trace inner-product structure: the dual basis
is orthonormal w.r.t. tr_M, so the dual-character pullback is the
"orthogonal projection" of the FR weight.

  Ref: gram-matrix-dual.py (H_3 Gram + Frobenius dual infrastructure)
  Ref: depth-stratified-frobenius-reciprocity.md (FR formula)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from witness_base import WitnessBuilder
# 50-dps source. `set_q` does `mp.mpf(str(...))` internally, so a STRING
# input gives the full 50 digits where the f64 `Q` gave 17. Alias renamed
# from Q0_STR: it is no longer a float, and a name that says otherwise is
# the label problem this sweep exists to remove.
from q_parameter import Q_50_DIGIT_STR as Q0_STR
# `qfac` comes from `hecke_characters`, NOT `q_mpmath`.  The two are different
# functions with the same name: `hecke_characters.qfac(n, q=None)` takes an
# explicit anchor (the `dim_q(shape, q)` idiom used throughout this file, bean
# `qou-wee5`), while `q_mpmath.qfac(n)` takes only `n` and reads a module
# global.  Importing the latter shadowed the former and made
# `qfac(n_strands, q)` a hard `TypeError` -- see the note in `main`.
from hecke_characters import chi_lambda_braid_mpf, partitions_of, dim_q, qfac
# `from q_mpmath import set_q, qint, qfac` is gone entirely.  `qint` was never
# used; `qfac` was the shadow described above; and `set_q` -- which configured
# the q_mpmath module global -- had no remaining consumer once `dim_q` and
# `qfac` take their anchor explicitly.  It was also called at IMPORT time, and
# `set_q` builds its mpf at the current `mp.dps`, which at import is mpmath's
# default 15, before `set_compute_dps()` runs: the 50-digit string it was
# handed was truncated to 15 on the way in.

# `numpy` and `pyhecke_native` were imported for the Gram-inverse block alone;
# that block computes nothing now (see the note beside it), so both are gone.
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION, M_E_MEV  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402


def q0_mp() -> mp.mpf:
    """The proton pin as an `mpf`, built at the CURRENT precision.

    Replaces `from qou_substrate.constants import Q as Q0_PROTON`, which is a
    Python float (measured: `type(Q) is float`) and capped every `dim_q` /
    `qfac` call in this file at f64 regardless of `mp.dps`.  A function rather
    than a module constant because `mp.mpf` rounds to `mp.dps` at construction,
    and at import time that is mpmath's default 15.
    """
    return mp.mpf(Q0_STR)


# ATOMS with (Z, N, n_strands, B_AME)
ATOMS = [
    ("D",   1, 1, 6,  AME_B_DEUTERON_MEV_VALIDATION),
    ("T",   1, 2, 9,  AME_B_TRITIUM_MEV_VALIDATION),
    ("3He", 2, 1, 9,  AME_B_HE3_MEV_VALIDATION),
    ("4He", 2, 2, 12, AME_B_HE4_MEV_VALIDATION),
]


KNOT_CANDIDATES = {
    "unknot": [],
    "3_1":    [1, 1, 1],
    "5_1":    [1, 1, 1, 1, 1],
    "6_1":    [1, 1, -2, 1, -3, 2, -3],
    "7_1":    [1, 1, 1, 1, 1, 1, 1],
}

KNOT_TO_PARTICLE = {
    "unknot": "ν",
    "3_1":    "e",
    "5_1":    "μ",
    "7_1":    "τ",
    "6_1":    "chirality",
}


# α_k weights per binding_depth_stratified_rust.py
def alpha_k(k: int) -> mp.mpf:
    Q0 = q0_mp()
    z_mark = Q0**3 / (Q0**2 + 1)   # convention D: z = q³/(q²+1)
    G = mp.catalan
    # Was a hardcoded `mp.mpf("0.51099894999999995")` -- a float64 value written
    # out as a string, tail digits and all, shadowing the imported CODATA
    # `M_E_MEV` under the same name.  The string spelling put it past the
    # `mpf(<float>)` gate while making it exactly what that gate exists to
    # catch.  Now the imported CODATA constant is used.
    if k in (0, 1, 3):
        return mp.mpf(1)
    if k == 2:
        return z_mark ** 2
    return mp.mpf(str(M_E_MEV)) * 8 * G


def depth_k(p: tuple) -> int:
    return len(p) - 1


def _serialise(obj):
    """Render the mpf working state to witness JSON at the LAST moment.

    `B_dim`, `B_MeV`, `B_AME`, `ratio` and `variance` are carried as `mpf`
    through the scan and converted here, once, via `_precision.fmt`.  The
    previous version called `float()` on each of them at the point of
    construction, so the ratios that the variance is a max/min OF -- and the
    sort that picks the best candidate -- were computed on f64.
    """
    if isinstance(obj, dict):
        return {k: _serialise(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_serialise(v) for v in obj]
    if isinstance(obj, mp.mpf):
        return "Infinity" if obj == mp.inf else fmt(obj)
    return obj


# Module-level cache for χ^λ(K) lookups: (K_word_key, lam) → chi.
# The K_k* variance scan repeatedly evaluates the same (K, λ) pairs
# across the (atom, k, K_1*, K_2*) loop; memoising at the module
# level avoids the redundant ~5× recomputation per scan entry.
_CHI_K_CACHE: dict[tuple, mp.mpf] = {}


def chi_K_at_lambda(K_word: list, lam: tuple) -> mp.mpf:
    """Cached evaluation of χ^λ(e_K) at q_0.

    Uses a module-level dict keyed by (tuple(K_word), lam) — both
    arguments are hashable, and `K_word` is short and reused
    across the variance scan.
    """
    cache_key = (tuple(K_word), lam)
    cached = _CHI_K_CACHE.get(cache_key)
    if cached is not None:
        return cached
    if not K_word:
        value = dim_q(lam, q0_mp())
    else:
        # Was `float(chi_lambda_braid(lam, word_m, q_value=Q0_STR))`.  Half the
        # fix was already here -- the 50-digit STRING was being passed -- but
        # the precision TAG was left at its default, which is f64, so the
        # string bought nothing and the result was then cast to `float`
        # anyway.  `chi_lambda_braid_mpf` is the mpfr chokepoint and also
        # marshals the flat signed word itself.
        try:
            value = chi_lambda_braid_mpf(lam, K_word, q_value=Q0_STR)
        except Exception:
            value = mp.mpf(0)
    _CHI_K_CACHE[cache_key] = value
    return value


def phi_k_with_K(by_partition: list, n_strands: int, k: int,
                 K_word: list, use_FR_projector: bool) -> mp.mpf:
    """Φ_k contribution with optional FR projector via K_k*.

    use_FR_projector=False → original (Plancherel-weighted, no K).
    use_FR_projector=True  → FR weight w̃_λ^(K_k*) replaces Plancherel.
    """
    # `qfac` here is `hecke_characters.qfac(n, q)`.  Until this commit the file
    # imported `q_mpmath.qfac(n)` -- a one-argument function of the same name --
    # so this call raised `TypeError: qfac() takes 1 positional argument but 2
    # were given` on the FIRST statement of this function, and this producer
    # could not run at all.  Measured on `main`: exits at line 145 every time,
    # before any witness is written.
    qfact = qfac(n_strands, q0_mp())
    parts_at_k = []
    for p in by_partition:
        shape = tuple(p["partition"])
        if depth_k(shape) == k:
            parts_at_k.append((shape, p))

    if use_FR_projector:
        # Compute FR-restricted weights (normalised)
        weights_raw = {}
        Z_norm = mp.mpf(0)
        for shape, _ in parts_at_k:
            dq = dim_q(shape, q0_mp())
            chi_K = chi_K_at_lambda(K_word, shape)
            w_raw = dq * dq * chi_K
            weights_raw[shape] = w_raw
            Z_norm += w_raw
        if Z_norm == 0:
            return mp.mpf(0)
        weights = {s: w / Z_norm for s, w in weights_raw.items()}
    else:
        # Original Plancherel weight dim_q²/[n]_q!
        weights = {}
        for shape, _ in parts_at_k:
            dq = dim_q(shape, q0_mp())
            weights[shape] = dq * dq / qfact

    total = mp.mpf(0)
    for shape, entry in parts_at_k:
        chi = mp.mpf(str(entry["chi_lambda"]))
        dq = dim_q(shape, q0_mp())
        magnitude = mp.fabs(chi) * dq
        if magnitude < mp.mpf("1e-30"):
            continue
        total += weights[shape] * mp.log(magnitude)
    return total


def compute_B_with_K_k_star(atom_witness: dict, n_strands: int,
                             K_k_stars: dict[int, list]) -> mp.mpf:
    """Full depth-stratified formula with FR projectors at specified k's.

    K_k_stars: {k: K_word} — apply FR projector at curvature ranks k
    that are in this dict; use original Plancherel at others.
    """
    atom_data = atom_witness["atom"]
    free_data = atom_witness["free"]
    B = mp.mpf(0)
    for k in range(n_strands):
        K_word = K_k_stars.get(k)
        use_FR = K_word is not None
        phi_atom = phi_k_with_K(atom_data["by_partition"], n_strands, k,
                                K_word, use_FR)
        phi_free = phi_k_with_K(free_data["by_partition"], n_strands, k,
                                K_word, use_FR)
        delta = phi_free - phi_atom
        B += alpha_k(k) * delta
    return B


def main() -> int:
    set_compute_dps()
    builder = WitnessBuilder("delta-lambda-full-variance-phase5e-1")
    builder.set_description(
        "Phase 5e.1: variance test of K_k* candidate knots using the "
        "FULL PR #801 depth-stratified binding formula (α_k weights + "
        "Φ_k(free) − Φ_k(atom) difference). Tests both standard and "
        "FR-projector-weighted variants. Compares to the Phase 5d.5b "
        "simplified result (chirality K_1* = K_3* = 6_1 wins at 1.49×)."
    )
    builder.set_content_block("prop:depth-stratified-frobenius-reciprocity")
    builder.add_parameter("q_0", Q0_STR)

    # Load atom-chi witnesses
    atom_witnesses = {}
    for atom, Z, N, n_s, B_AME in ATOMS:
        path = HERE / f"atom-chi-rust-{atom.lower()}.witness.json"
        if not path.exists():
            print(f"  WARN: {path.name} missing, skipping")
            continue
        w = json.loads(path.read_text())
        atom_witnesses[atom] = w["data"]
        print(f"  {atom}: loaded {len(w['data']['atom']['by_partition'])} partitions")
    print()

    # A SECOND hardcoded `mp.mpf("0.51099894999999995")` shadowed the imported
    # CODATA `M_E_MEV` here too, inside `main`, so removing only the one in
    # `alpha_k` would have left the MeV conversion below on the f64 literal.
    m_e = mp.mpf(str(M_E_MEV))
    print(f"  α_k weights: α_0=α_1=α_3=1, α_2=z²={float(alpha_k(2)):.6f}, "
          f"α_{{k≥4}}=m_e·8G={float(alpha_k(4)):.6f}")

    # --- Baseline (no FR projector, all Plancherel weights) ---
    print("\n  === Baseline (no FR projector) ===")
    baseline = {}
    for atom, Z, N, n_s, B_AME in ATOMS:
        if atom not in atom_witnesses:
            continue
        B = compute_B_with_K_k_star(atom_witnesses[atom], n_s, {})
        # Convert to MeV via E_0 calibration: B_MeV = B_dim × M_e
        # (per binding_depth_stratified_rust.py)
        B_MeV = B * m_e
        B_AME_mp = mp.mpf(str(B_AME))
        baseline[atom] = {
            "B_dim": B, "B_MeV": B_MeV,
            "B_AME": B_AME_mp,
            "ratio": B_MeV / B_AME_mp if B_AME_mp != 0 else mp.mpf(0),
        }
        print(f"    {atom}: B_dim = {float(B):+.4f}, B_MeV = {float(B_MeV):.4f}, "
              f"ratio = {float(baseline[atom]['ratio']):.4f}")
    ratios = [d["ratio"] for d in baseline.values() if d["ratio"] > 0]
    if len(ratios) >= 2:
        baseline_var = max(ratios) / min(ratios)
        print(f"    baseline variance (max/min): {float(baseline_var):.4f}")
    builder.add_data("baseline", {
        "per_atom": _serialise(baseline),
        "variance": fmt(baseline_var) if len(ratios) >= 2 else None,
    })

    # --- K_k* variance scan (full formula) ---
    K_names = list(KNOT_CANDIDATES.keys())
    print(f"\n  === K_k* full-formula variance scan ===")
    K3_star = KNOT_CANDIDATES["6_1"]  # fixed per catalog

    results = []
    for K1_name in K_names:
        for K2_name in K_names:
            K_k_stars = {
                1: KNOT_CANDIDATES[K1_name],
                2: KNOT_CANDIDATES[K2_name],
                3: K3_star,
            }
            per_atom = {}
            for atom, Z, N, n_s, B_AME in ATOMS:
                if atom not in atom_witnesses:
                    continue
                B = compute_B_with_K_k_star(atom_witnesses[atom], n_s, K_k_stars)
                B_MeV = B * m_e
                B_AME_mp = mp.mpf(str(B_AME))
                per_atom[atom] = {
                    "B_dim": B, "B_MeV": B_MeV,
                    "B_AME": B_AME_mp,
                    "ratio": B_MeV / B_AME_mp if B_AME_mp != 0 else mp.mpf(0),
                }
            ratios = [d["ratio"] for d in per_atom.values() if d["ratio"] > 0]
            if len(ratios) >= 2:
                variance = max(ratios) / min(ratios)
            else:
                variance = mp.inf
            results.append({
                "K_1_star": K1_name, "K_2_star": K2_name, "K_3_star": "6_1",
                "K_1_particle": KNOT_TO_PARTICLE[K1_name],
                "K_2_particle": KNOT_TO_PARTICLE[K2_name],
                "variance": variance,
                "per_atom": per_atom,
            })

    results.sort(key=lambda r: r["variance"] if r["variance"] != mp.inf else mp.mpf("1e9"))
    builder.add_data("full_formula_scan", _serialise(results))

    print(f"  {'K_1*':<8} {'K_2*':<8} {'variance':>10}  {'K_1':<12} {'K_2':<12}")
    for r in results[:10]:
        v_str = f"{float(r['variance']):.4f}" if r['variance'] != mp.inf else "INF"
        print(f"  {r['K_1_star']:<8} {r['K_2_star']:<8} {v_str:>10}  "
              f"{r['K_1_particle']:<12} {r['K_2_particle']:<12}")

    # --- Gram-inverse variant for H_3-supported K candidates ---
    # NF basis at H_3: {1, σ_0, σ_1, σ_0·σ_1, σ_1·σ_0, σ_0·σ_1·σ_0} (6 elements)
    # KNOT_CANDIDATES use 1-indexed braid gens; H_3 uses σ_1, σ_2 (1-indexed)
    # We can decompose K_word for KNOTS that live in B_3 (max gen ≤ 2):
    #   - unknot (empty)
    #   - 3_1 = σ_1·σ_2·σ_1 (need both σ_1, σ_2 — IS in B_3 originally, but
    #         my word 1,1,1 uses only σ_1, that's B_2)
    print(f"\n  === Gram-inverse-weighted variant (H_3 only) — NOT COMPUTED ===")

    # This block used to call `pyhecke_native.gram_inverse(float(Q0_STR))` inside
    # a bare `try`, print a condition number, and record a 6x6 matrix.  It has
    # not done any of that for some time: measured, the call raises
    # `AttributeError: module 'pyhecke_native' has no attribute 'gram_inverse'`,
    # the `except` swallows it, and the committed witness accordingly carries no
    # `gram_inverse_H3` key at all (checked: its data keys are exactly
    # `baseline`, `full_formula_scan`, `lean_uniqueness_ref`).  The swallowing
    # `try` is why that was invisible.
    #
    # It is NOT restored, and the reason is mathematical rather than an API
    # rename.  Under the canonical convention D (`z = q³/(q²+1)`, owner ruling
    # 2026-08-15) the H_3 NF-basis trace form is SINGULAR, so the object this
    # block asks for does not exist.  `pyhecke/gram.py` states it and measures
    # the failure mode: "`np.linalg.inv(G)` does not say so: it raises nothing
    # and returns entries up to 7.6e15 with ||G @ G_INV - I||_max = 1.64".  So
    # rebuilding it as `np.linalg.inv(pyhecke_native.gram_matrix(q))` -- which
    # DOES still exist and does return the right 6x6 NF Gram -- would have
    # replaced a loud absence with a quiet 16-digit-wrong matrix.
    #
    # The honest continuation is `gram_quotient_inverse` (`G_PINV`), the inverse
    # on H_3(q)/rad.  That is a DIFFERENT object from the one the 5e.2 sketch
    # below assumes, and choosing it -- deciding the FR weight should use the
    # quotient dual -- is a modelling decision, not a substitution an agent
    # makes while draining float64.  Left visible.  Bean `qou-cds2`.
    builder.add_data("gram_inverse_variant", {
        "status": "not computed",
        "requested_object": "inverse of the 6x6 H_3 NF-basis Gram G_ij = tr_M(b_i·b_j)",
        "why_not": "G is singular under convention D (z = q^3/(q^2+1)); a 6x6 "
                   "inverse does not exist. np.linalg.inv(G) neither raises nor "
                   "converges: ||G @ G_INV - I||_max = 1.64.",
        "prior_behaviour": "called pyhecke_native.gram_inverse(q) inside a bare "
                           "try/except; that attribute no longer exists, the "
                           "exception was swallowed, and no gram field was ever "
                           "written to this witness",
        "candidate_continuation": "pyhecke.gram.gram_quotient_inverse (G_PINV), "
                                  "the inverse on H_3(q)/rad — a different object; "
                                  "adopting it is a modelling decision for 5e.2",
        "bean": "qou-cds2",
        "source": "tools/pyhecke/python/pyhecke/gram.py, module docstring and "
                  "the RADICAL / G_PINV comments",
    })
    print(f"    G (6x6 NF-basis Gram at H_3) is SINGULAR under convention D, so")
    print(f"    the inverse this variant needs does not exist. Continuation is")
    print(f"    the quotient pseudo-inverse G_PINV — a modelling choice, 5e.2.")

    best_var = min(r["variance"] for r in results if r["variance"] != mp.inf)
    builder.add_assertion(
        "full_formula_variance_below_baseline",
        computed=fmt(best_var),
        expected=fmt(baseline_var) if len(ratios) >= 2 else fmt(mp.mpf(2)),
        tolerance=0.5,
        unit="rel_variance",
        source=(
            f"Best K_k* variance under FULL formula: {float(best_var):.4f}. "
            f"Baseline (no FR projector): {float(baseline_var):.4f}. "
            f"Phase 5d.5b simplified-formula best: 1.4889 (K_1* = 6_1)."
        ),
    )

    # Lean SDP-uniqueness cross-reference (post-#1537 wiring).

    builder.add_data("lean_uniqueness_ref", {

        "generic": "qou:QOU.BraidKnot.@nucleus_uniqueness_closed (3*A)",

        "framework_doc":

            "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",

        "note": "Certifies T_w uniqueness at the abstract empty-constraint SDP level (PR #1537 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md.",

    })


    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
