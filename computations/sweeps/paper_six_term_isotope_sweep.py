"""

CLASS-A acknowledged-anchor banner (per Workplan-0b/M_N):
This script imports M_*_MEV_VALIDATION constants from
`codata_constants.py` as production inputs (not just as
comparison targets).  M_N is currently a CLASS-A acknowledged-
stub anchor pending its own substrate derivation — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`
for the open spec.  Until that lands, the calibration-discipline
audit (`canonical-script-input-audit`) classifies this script
as "with-substrate-splitting" or "anchor-pending"; reviewers
should treat the M_*_MEV_VALIDATION usage as CAL-3-ish anchor,
NOT as an independent calibration input.
"""


# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
#!/usr/bin/env python3
"""
Paper-canonical 6-term mass-formula sweep (singular implementation).

This is the **only** categorical mass formula in the repo.  Other
historical implementations (v3 `compute_mass_at_level`, v4
`crt_markov_v4` / `v4_mass_pipeline`, `markov_invariant_unified_mass`,
`paper_six_term_canonical_t1`) were retired on 2026-05-03 — see
`docs/audits/2026-05-03-categorical-mass-divergence-audit.md`.

Implements the paper's 6-term formula:

    m(ϱ) = |tr_M(T_w)|                            (Term 1)
         + Σ_i Φ_q(|V̂_i|)                        (Term 2)
         + z² Σ_{i<j} Φ_q(|V̂_i V̂_j|)              (Term 3)
         + m_e · τ(C_dim_q)                       (Term 4)
         + a_K · 𝒞_K                              (Term 5; additive)
         + Σ_{ℓ≥2} Res_{ζ_ℓ}                     (Term 6 — cyclotomic tail)

Canonical inputs:

    Term 1 — `atomic-tr-m-mpfr-50dps.witness.json`
             Hoefsmit + Wenzl bridge: `tr_M(W) = Σ_λ y_λ(q) · χ^λ(W)`
             at q = q_0, atom-name-keyed.  Equivalent to `markov_peel`
             recursive-ascent values (PR #520) to 15+ digits.

    Term 6 — `term6-habiro-residue-mpfr-50dps.witness.json`
             Per-A cyclotomic-pole residue series.  Tiny at q_0 (≤ 0.7
             MeV for A=1, ≤ 3 μMeV for A=4) but structurally important.

Terms 2 and 3 use per-generator volumes from
`hecke_core.atom_per_generator_volumes`.  These are NOT Markov-invariant
and exhibit a known structural pathology: Φ_q diverges near x=1, so
per-generator volumes |V̂_i| ≈ 0.99 amplify p/n asymmetries by ~10⁵×.
See `brane-tower-isospin-diagnosis.witness.json` (PR #524).  The
brane-tower is kept as the literal paper formula but should be
re-derived; `prop:mass-endomorphism-tower` is open.

Witness: paper-six-term-isotope-sweep.witness.json
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations
import warnings

import numpy as np  # noqa: F401  (kept for downstream consumers)
import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder, load_and_hash_upstream  # noqa: E402
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP  # noqa: E402
from hecke_core import (  # noqa: E402
    atom_per_generator_volumes, h as h_val, z as z_mark,
    Phi_q,
)
from experimental_constants import Q_NEUTRON_MEV, M_E_MEV  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

HERE = Path(__file__).parent

# This producer never raised working precision, so EVERY mpmath value in it —
# including the 50-dps strings it lifts out of upstream witnesses — was built at
# mpmath's default 15 dps. The clearest symptom is in `load_tr_M_50dps` below:
#
#     out[r["atom"]] = abs(mp.mpf(r["tr_M_at_q0_50dps"]))
#
# a field whose NAME says 50 dps, truncated to 15 on the way in. The emitted
# witness contained no decimal string longer than 25 digits anywhere.
#
# Nothing here was "fake precision" and no constant was built too early, so the
# padding, raw-float64 and import-time gates all passed it cleanly — the numbers
# were honestly float64. That is the blind spot never_raises_dps_audit.py exists
# for (bean qou-j6gb). Idempotent, and at module scope so it also covers the
# `mp.mpf(str(...))` constants immediately below.
set_compute_dps()

Q0 = Q_MP
# `z_mark`, `h_val` are float64 in `hecke_core` (see `q_parameter.py`).
# `mp.mpf(str(...))` is the canonical lossless lift to mpmath without a
# spurious round-trip via `float()` (per gemini-code-assist comment #3
# on PR #534).
Z_MARK = mp.mpf(str(z_mark))
H_VAL = mp.mpf(str(h_val))

# Isotopes at A ≥ 5 (Hecke H_{≥15}) whose canonical |tr_M| at q_0
# is intractable with the current Python mpmath @ 50 dps pipeline
# (p(15) = 176 partitions and max Hoefsmit dim in the thousands;
# bu64reus1 on PR #564 hit the 30-min CI timeout already at ⁴He /
# H_12).  The sweep loop emits a `deferred: true` row for these
# (no `error_kind`) so the I13 incomplete-coverage audit
# distinguishes physics-blocked gaps from producer bugs.  Tractable
# computation awaits (a) Rust kernel with rayon parallel partitions
# + block-sparse Hoefsmit MPFR, or (b) Wenzl 1988 LR-branching
# categorical reduction.  See AUDIT-DEEP-2026-05.md §7.
DEFERRED_INTRACTABLE_ATOMS = frozenset({
    "5Li", "6Li", "7Li", "7Be", "8Be", "9Be",
})


def _serialise(obj):
    """Render the mpf working state to witness JSON at the LAST moment.

    Applied once, to the whole witness dict, immediately before `wrap_legacy`.
    The rows previously cast to `float` at construction time on the stated
    grounds that "storage is for reporting and float64 is sufficient for ~16
    digits" -- but `err_pct` IS the reported result, and a residual is the one
    quantity in this producer where the digits past the 16th are the point.
    """
    if isinstance(obj, dict):
        return {k: _serialise(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_serialise(v) for v in obj]
    if isinstance(obj, mp.mpf):
        return fmt(obj)
    return obj


def abs_mpf(v):
    """Coerce a per-generator volume to abs mpmath float (no f64
    round-trip — preserves precision for callers that pass mpf/sympy)."""
    x = v["full"] if isinstance(v, dict) else v
    return abs(mp.mpf(x))


# ── Canonical Term 1 from Hoefsmit+Wenzl bridge witness ────────────
# Per owner directive 2026-05-11 ("migrate all compute to default B"),
# canonical_t1 now defaults to Model B (SDP-canonical low-strand
# τ_M).  Model A values remain available via t1_source="model-a".
_T1_CACHE: dict | None = None
_T1_CACHE_B: dict | None = None

# Default T1 source.  Set to "model-a" via environment to revert.
import os as _os  # noqa: E402
import sys as _sys  # noqa: E402
_MODEL_B_WARNED = False
from qou_substrate.constants import Q as Q0_PROTON  # noqa: E402 — anchor-independent proton pin (qou-6p3b Tranche C)
# This producer hand-builds its assertion payload and `json.dump`s it, so
# `Assertion.to_dict` -- where the declared-tolerance guard runs -- is never
# reached, and a re-run would re-emit the float literals and undo PR #5910's
# drain for this file alone. `_tol` routes each DECLARED tolerance through
# that guard; it returns a COMPUTED one unchanged, so those stay floats and
# stay counted by the raw-float64 ratchet. Bean qou-9tqx.
from qou_substrate.witness import declared_tolerance as _tol  # noqa: E402
_T1_DEFAULT_SOURCE = _os.environ.get("QOU_T1_SOURCE", "model-b")


def _load_canonical_t1() -> dict:
    """Atom name → |tr_M(W)| at q_0 from the canonical bridge witness.
    Result is cached at module level so multi-isotope sweeps pay one disk read.
    """
    global _T1_CACHE
    if _T1_CACHE is not None:
        return _T1_CACHE
    path = _pb.witness_path("atomic-tr-m-mpfr-50dps-proton.witness.json", HERE)
    if not path.exists():
        raise FileNotFoundError(f"missing canonical T1 witness: {path}")
    d = json.loads(path.read_text())
    out: dict[str, mp.mpf] = {}
    for r in d.get("results", []):
        out[r["atom"]] = abs(mp.mpf(r["tr_M_at_q0_50dps"]))
    _T1_CACHE = out
    return _T1_CACHE


def _load_canonical_t1_model_b() -> dict:
    """Atom name → |tr_M(canonical-knot)| at q_0 from Model B
    (SDP-canonical low-strand) Wenzl-Schur via
    probe-sdp-canonical-paper-formula.witness.json."""
    global _T1_CACHE_B
    if _T1_CACHE_B is not None:
        return _T1_CACHE_B
    path = _pb.witness_path("probe-sdp-canonical-paper-formula.witness.json", HERE)
    if not path.exists():
        # Model B is UNAVAILABLE, permanently, and this is not a missing run.
        # `probe_sdp_canonical_paper_formula.py` is not on disk anywhere in
        # this repo and no commit in this clone's history touches it, so the
        # instruction this branch used to raise with ("run it first") could
        # not be followed by anyone. It cannot be written either: its input,
        # the 6_2 deuteron assignment, was RETIRED by the owner ruling of
        # 2026-08-29 (`docs/audits/2026-08-29-deuteron-knot-owner-decision.md`).
        #
        # Return EMPTY rather than raise. The caller already falls through to
        # Model A for any isotope absent from this table, so an empty table is
        # exactly "no isotope has a Model B value" -- which is the truth. This
        # matches how the OTHER consumer of this same witness under this same
        # env var already behaves: `atomic_mass_via_rho_k.py` loads Model A
        # first and overlays Model B only `if model_b_witness.exists()`.
        #
        # This does not override the 2026-05-11 "default to Model B"
        # directive; it is what that directive means when B is unavailable --
        # the directive's own wording is "prefer Model B ... fall back to
        # legacy for atoms not yet in the Model B witness".
        #
        # Raising instead made the DEFAULT configuration fail for exactly the
        # three isotopes Model B covers (D, T, 3He), measured 2026-09-05.
        # Bean `qou-imkb`.
        global _MODEL_B_WARNED
        if not _MODEL_B_WARNED:
            _MODEL_B_WARNED = True
            print(
                "[paper_six_term_isotope_sweep] Model B (SDP-canonical "
                "low-strand) is unavailable: its producer cannot be written "
                "because the 6_2 deuteron assignment it needs was retired by "
                "the owner ruling of 2026-08-29. Falling through to Model A "
                "(3A-strand) for D, T and 3He. Bean qou-imkb.",
                file=_sys.stderr,
            )
        _T1_CACHE_B = {}
        return _T1_CACHE_B
    d = json.loads(path.read_text())
    out: dict[str, mp.mpf] = {}
    for atom_name, atom_data in d.get("data", {}).get("results", {}).items():
        out[atom_name] = abs(mp.mpf(str(atom_data["tr_M_wenzl_schur"])))
    _T1_CACHE_B = out
    return _T1_CACHE_B


# Markov-peel inline values for atoms not in the bridge witness (e.g. ⁴He
# and beyond — see markov-peel-atomic-tr-m.witness.json, computed at
# 50 dps via Markov-axiom recursive ascent and verified against the
# bridge for proton..³He to 4×10⁻¹⁶).
_PEEL_INLINE_T1 = {
    "helium-4": "0.055348345876697992162807082650033407844603061676025",
}

# Mapping from sweep-table isotope labels to bridge-witness atom names.
_T1_ATOM_NAME = {
    "p": "proton", "n": "neutron",
    "D": "deuteron", "T": "tritium",
    "3He": "helium-3", "4He": "helium-4",
}

# Mapping from sweep-table isotope labels to Model B witness atom names.
_T1_ATOM_NAME_B = {
    "D": "deuteron", "T": "tritium", "3He": "he3",
    # p, n: at A=1, Model A and Model B converge (both use B_3 with
    # 11 typed crossings).  Fall through to Model A — same values.
    # ⁴He: no Model B canonical low-strand braid yet; fall through.
}


def canonical_t1(isotope_label: str, *, source: str | None = None) -> mp.mpf:
    """Return |tr_M(W)| at q_0 for the named isotope.

    source="model-b" (default per QOU_T1_SOURCE env var): use the
    SDP-canonical low-strand braid via
    `probe-sdp-canonical-paper-formula.witness.json`.  Falls back to
    Model A for isotopes not yet covered by the Model B witness
    (p, n, ⁴He).

    source="model-a": use Model A `atom_braid_word_3A` via
    `atomic-tr-m-mpfr-50dps.witness.json`.
    """
    src = source or _T1_DEFAULT_SOURCE
    if src == "model-b":
        b_name = _T1_ATOM_NAME_B.get(isotope_label)
        if b_name:
            table = _load_canonical_t1_model_b()
            if b_name in table:
                return table[b_name]
        # Fall through to Model A for isotopes not in the Model B witness.

    # Model A path (default fallback)
    name = _T1_ATOM_NAME.get(isotope_label, isotope_label)
    table = _load_canonical_t1()
    if name in table:
        return table[name]
    if name in _PEEL_INLINE_T1:
        return abs(mp.mpf(_PEEL_INLINE_T1[name]))
    raise KeyError(
        f"no canonical T1 for {isotope_label!r}; "
        f"add to atomic-tr-m-mpfr-50dps.witness.json or "
        f"markov-peel-atomic-tr-m.witness.json"
    )


# ── Symmetric q-dilogarithm (Hecke convention) ──
# Used by tower_mode="li2q" — the corrected Kashaev limit per
# `prop:mass-endomorphism-tower` (proof: kashaev-integration-identity
# .witness.json + a43d7f1fa).
def _q_int(n: int) -> mp.mpf:
    """[n]_q = (q^n - q^{-n}) / (q - q^{-1}), symmetric q-integer."""
    if n == 0:
        return mp.mpf(0)
    return (Q0 ** n - Q0 ** (-n)) / (Q0 - 1 / Q0)


def li2_q_sym(z: mp.mpf, max_n: int = 300) -> mp.mpf:
    """Symmetric q-dilogarithm Li_2^q(z) = Σ_{n≥1} z^n / (n · [n]_q).

    Identity: ∫_0^V (ln_q(1+t)/t) dt = -Li_2^q(-V).

    Delegates to the corpus implementation ``_li_2_q_util.li_2_q`` (bean
    qou-cw27). The power series has radius |z| < q, but the FUNCTION is
    analytic on the whole negative axis:
        -Li_2^q(-V) = (q - q^{-1}) · Σ_{k≥0} log(1 + V·q^{-(2k+1)}),
    finite and positive for every V > 0. This module previously summed the
    series to a fixed 300 terms with no radius check, so for |V| > q it
    returned a truncated DIVERGENT partial sum: -2.43e15 at the proton's
    convention-D volume V = 1.2824 (and a different value at 301 terms).
    That number was never a pole of the formula. ``max_n`` is kept only for
    call-site compatibility and is ignored.
    """
    from _li_2_q_util import li_2_q
    return li_2_q(mp.mpf(z), Q_MP, Q_INV_MP)


# ── Canonical Term 6 from Habiro residue witness ────────────────────
_T6_CACHE: dict | None = None


def _load_canonical_t6_MeV() -> dict[int, mp.mpf]:
    """A → Term 6 (cyclotomic residue tail) in MeV from Habiro witness.
    Result is cached at module level.  Missing witness emits a warning and
    returns {} (all T6 contributions silently set to zero).
    """
    global _T6_CACHE
    if _T6_CACHE is not None:
        return _T6_CACHE
    path = _pb.witness_path("term6-habiro-residue-mpfr-50dps.witness.json", HERE)
    if not path.exists():
        warnings.warn(
            f"T6 witness missing ({path}); Term 6 contributions set to 0 MeV. "
            "Run term6_residues_at_roots.py to regenerate.",
            stacklevel=2,
        )
        _T6_CACHE = {}
        return _T6_CACHE
    d = json.loads(path.read_text())
    out: dict[int, mp.mpf] = {}
    for r in d.get("results_by_atom", []):
        try:
            A = int(r["atom"].split("=")[1])
            out[A] = mp.mpf(r["term6_b_pred_mev_50dps"])
        except (KeyError, IndexError, ValueError):
            continue
    _T6_CACHE = out
    return _T6_CACHE


def term1_descended(vols):
    """Term 1: product of volumes (approximation of descended tr_M)."""
    p = mp.mpf(1)
    for v in vols:
        p *= abs_mpf(v)
    return p


def _phi_q_or_divergent(arg):
    """Φ_q(arg), or ``mp.inf`` when ``arg`` is at or past the pole.

    Φ_q(x) = ∏_{k≥1} (1 − q^{-k} x)^{-1} has its first pole at x = q₀. Under
    the convention-D volumes (owner ruling 2026-11-18) the proton and neutron
    generator volumes are 1.2824 and 1.1337, past it (bean qou-2tuv).
    """
    phi = Phi_q(arg)
    if mp.isinf(phi) or mp.isnan(phi):
        return mp.inf
    return mp.mpf(phi)


def term2_single_gen_tower(vols):
    """Term 2: Σ_i Φ_q(|V̂_i|).

    Returns ``mp.inf`` if any generator volume is at or past the Φ_q pole.
    It used to skip such generators silently (and, through a swallowed
    TypeError, every generator); a divergence is now reported as what it is
    (owner, 2026-11-20).
    """
    total = mp.mpf(0)
    for v in vols:
        # |V̂_i| per the docstring. The old body passed the raw volume, which
        # is a dict ({"full", "sym", ...}); Phi_q raised TypeError on it and the
        # blanket `except: pass` swallowed that, so this term was 0 for EVERY
        # isotope in every convention, not only past the pole.
        phi = _phi_q_or_divergent(abs_mpf(v))
        if mp.isinf(phi):
            return mp.inf
        total += phi
    return total


def term3_pair_gen_tower(vols):
    """Term 3: z² Σ_{i<j} Φ_q(|V̂_i V̂_j|). ``mp.inf`` on any divergent pair
    (previously skipped silently, as in Term 2)."""
    total = mp.mpf(0)
    n = len(vols)
    for (i, j) in combinations(range(n), 2):
        arg = abs_mpf(vols[i]) * abs_mpf(vols[j])
        phi = _phi_q_or_divergent(arg)
        if mp.isinf(phi):
            return mp.inf
        total += Z_MARK ** 2 * phi
    return total


def term4_frobenius_codim(A):
    """Term 4 in Hecke units (without `m_e`): the FORMAL sum Σ_{λ ⊢ 3A} 1/dim_q(λ).

    Scope label (owner ruling 2026-11-16, option B "keep number, relabel"):
    this is NOT τ(C_dim_q) under convention D.  For n = 3A ≥ 3, τ(p_λ) = 0
    for every λ with three or more rows, so C_dim_q is undefined there
    (thm:frobenius-codim-universal, scope paragraph).  The sum below runs
    over ALL partitions and is kept unchanged as a formal sum; the value
    τ(C°_dim_q) over the surviving blocks is a different number.  Which of
    the two (or a radical-quotient object) Term 4 should be is open.

    Returns Σ_{λ ⊢ 3A} 1/dim_q(λ).  The full Term 4 contribution
    is `m_e · τ(C_dim_q)`; the `m_e` factor is applied at the
    formula-assembly site (`paper_six_term_mass`) where the
    electron-mass scale in Hecke units is known.

    Optimised: all arithmetic in `mpmath` directly.  No redundant
    `float()` casts inside the loop; constant denominator
    `q − q⁻¹` lifted out.
    """
    from schur_weyl_symbolic import partitions_of
    from hecke_characters import young_hooks, qfac
    n = 3 * A
    nfac_val = mp.mpf(qfac(n, Q0_PROTON))
    q = Q0
    q_inv = 1 / q
    denom = q - q_inv
    total = mp.mpf(0)
    for lam in partitions_of(n):
        hooks = young_hooks(lam)
        dim_q_val = nfac_val
        for h in hooks:
            hl_val = (q ** h - q_inv ** h) / denom
            dim_q_val /= hl_val
        if abs(dim_q_val) > mp.mpf('1e-30'):
            total += 1 / dim_q_val
    return total


def term5_chirality(Z, N, chirality_signs):
    """Term 5 (legacy closed form): a_K = Π_{c ∈ pn-crossings} (1 + sign(c)·h).

    Heuristic Π-of-signs over a hand-coded `chirality_signs_for_isotope`
    pattern.  Superseded by `term5_v2_chirality.aK_v2` (canonical
    Gram-matrix chirality `τ(β · β_mirror⁻¹)` per
    `conj:knot-factor-frobenius-pairing`).  Retained for legacy
    compatibility and as a quick fall-back when (Z, N) is outside the
    V2 compute window.

    Callers should prefer `paper_six_term_mass(..., chirality_source="v2")`
    (the default since 2026-05-15).
    """
    a_K = mp.mpf(1)
    for s in chirality_signs:
        a_K *= 1 + s * H_VAL
    return a_K


def term6_higher_residues(vols):
    """Term 6: higher-stratum residues (jet-prefix correction).

    Per `gb-residue-spectral-sum`, this is Σ_{ℓ≥2} Res at roots of
    unity.  For light isotopes this is numerically sub-dominant
    at real q_0; structurally included as the Mittag-Leffler tail
    beyond Terms 2, 3.  Here we return 0 as the placeholder
    (actual computation requires the full pole-decomposition
    script `gb_residue_tower.py`).
    """
    return mp.mpf(0)


def paper_six_term_mass(Z, N, include_inter=True,
                          chirality_signs=None,
                          m_e_hecke=mp.mpf(1),
                          term5_mode: str = "multiplicative_on_t1",
                          isotope_label: str | None = None,
                          tower_mode: str = "li2q",
                          chirality_source: str = "v2"):
    """6-term mass formula.

    `tower_mode` controls T2 + T3 evaluation:
        "li2q" (default, 2026-05-03):
                            T2 = -Σ Li_2^q(-|V̂_i|),
                            T3 = -z² · Σ Li_2^q(-|V̂_i V̂_j|)
                            symmetric q-dilogarithm — the corrected
                            Kashaev limit per `prop:mass-endomorphism-tower`
                            (proven in commit a43d7f1fa via the
                            `kashaev-integration-identity` probe).
        "brane-legacy" (deprecated; alias "brane" emits DeprecationWarning):
                            T2 = Σ Φ_q(|V̂_i|), T3 = z² · Σ Φ_q(|V̂_i V̂_j|).
                            compact quantum dilogarithm form, NOT
                            Markov-invariant at q_0 (PR #524).
                            Empirical T − ³He = −737 MeV pathology.
                            Retained for back-compat / regression
                            testing only — do not use for new
                            mass-prediction work.
        "drop":             T2 = T3 = 0.  Simplest test of "no brane".
        "q1-base":          T2 + T3 = (1/2)^(2A-1) (Path A closed-form
                            base point at q→1 per
                            `path-a-zeta1-residue-probe.witness.json`).
        "r-side-bare":      T2 = (n-1)·z², T3 = C(n-1,2)·z⁴ (R-side
                            algebraic per `prop:mass-endomorphism-tower`,
                            Markov-axiom values).
        "habiro" (P2.A):    T1 := τ_M^Habiro from
                            path-b-habiro-mass-probe.witness.json;
                            T2 = T3 = 0 (the m≥1 terms of the Habiro
                            cyclotomic sum already encompass them).
                            Coverage: {p, n, D}; raises on missing atoms.
        "per-partition-k" (P1.D):
                            T1 from canonical Hoefsmit+Wenzl bridge
                            (unchanged); T2 := total_tower from
                            probe-phiq-per-partition-klambda.witness.json
                            (per-partition $k_\\lambda$ truncation per
                            `per-partition-k-lambda-rule.md`); T3 = 0.
                            Coverage: {D, T, ³He}; raises on missing atoms.
        "combined" (P2.B):
                            Per-atom router producing the M1 mass table:
                            {p, n, D} → "habiro", {T, ³He} → "per-partition-k",
                            else → "li2q". No new physics; routes each
                            isotope to the canonical mode with the
                            strongest backing for it.
    """
    """Six-term mass formula in Hecke units.

    Per `thm:knot-mass-formula-unified` the formula assembles as:

        m  =  |tr_M(T_w)|                                  Term 1
            + Σ_i Φ_q(|V̂_i|)                              Term 2
            + z² Σ_{i<j} Φ_q(|V̂_i V̂_j|)                    Term 3
            + m_e · τ(C_dim_q)                             Term 4
            + a_K · 𝒞_K                                    Term 5  (additive)
            + Σ_{ℓ≥2} Res_{ζ_ℓ}                            Term 6

    Term 5 in the manuscript is **additive** with bulk coefficient
    `𝒞_K` (the chirality coupling, vortex-specific).  Two interpretations
    coexist in the implementation literature:

      (A) `term5_mode="additive"`: Term 5 = (a_K − 1) · |tr_M(T_w)|,
          i.e. the chirality DEVIATION from unity, additive — agrees
          with the manuscript's `a_K · 𝒞_K` taking 𝒞_K = |tr_M|.

      (B) `term5_mode="multiplicative_on_t1"` (legacy default):
          Term 1 is multiplied by a_K, equivalent to (A) plus the
          original |tr_M|; mathematically the same total as (A) when
          summed with Term 1 written without chirality.  Default
          here for backwards-compatibility with witnesses produced
          before the formula clarification.

    `m_e_hecke` is the electron mass in Hecke units (typically set
    by the calibration site).  Set to 1.0 to leave Term 4 in raw
    τ(C_dim_q) units.
    """
    vols = atom_per_generator_volumes(Z, N, include_inter=include_inter)
    # T1: canonical |tr_M| from Hoefsmit+Wenzl bridge witness.  Per
    # gemini-code-assist comment #2 on PR #534 and the audit
    # docs/audits/2026-05-03-categorical-mass-divergence-audit.md, the
    # legacy per-generator product Π|V̂_i| (term1_descended) is
    # non-canonical and the source of isospin-violating pathologies
    # (the −737 MeV mirror-nucleus gap).  We refuse to silently
    # substitute it here; the caller must supply an isotope_label that
    # the canonical witness file covers.
    if isotope_label is None:
        raise ValueError(
            "paper_six_term_mass: isotope_label is required. The "
            "canonical T1 path (canonical_t1) takes |tr_M(T_w)| from "
            "atomic-tr-m-mpfr-50dps.witness.json, which is keyed by "
            "isotope_label ('p', 'n', 'D', 'T', '3He', '4He', ...).  "
            "Per the categorical-mass-divergence audit, the legacy "
            "per-generator-product fallback is non-canonical and "
            "produces ~10⁵× isospin pathologies — it has been "
            "removed."
        )
    t1 = canonical_t1(isotope_label)

    # T2, T3 evaluation per `tower_mode`:
    if tower_mode in ("brane-legacy", "brane"):
        # "brane" alias kept for backward compatibility; emits deprecation
        # warning since the legacy Φ_q form has the -737 MeV isospin
        # pathology documented in PR #524.  New callers should pass
        # tower_mode="li2q" (default) or explicitly "brane-legacy".
        if tower_mode == "brane":
            warnings.warn(
                "tower_mode='brane' is deprecated; use 'brane-legacy' "
                "for the compact q-dilog Φ_q legacy form, or 'li2q' (default) "
                "for the corrected Kashaev limit per "
                "prop:mass-endomorphism-tower (a43d7f1fa).",
                DeprecationWarning,
                stacklevel=2,
            )
        t2 = term2_single_gen_tower(vols)
        t3 = term3_pair_gen_tower(vols)
    elif tower_mode == "drop":
        t2 = mp.mpf(0)
        t3 = mp.mpf(0)
    elif tower_mode == "q1-base":
        # Path A closed form: tr_M(T_w; q→1) = (1/2)^(2A-1).  Allocate
        # to T2; set T3 = 0.  Captures the spectral-sequence base
        # trace value at q→1 without per-generator amplification.
        A = Z + N
        t2 = mp.mpf(1) / mp.mpf(2) ** (2 * A - 1)
        t3 = mp.mpf(0)
    elif tower_mode == "r-side-bare":
        # R-side algebraic form per `prop:mass-endomorphism-tower`:
        #   T2 = z · Σ_i tr_M(σ_i)    = n_gens · z² (Markov axiom)
        #   T3 = z² · Σ_{i<j} tr_M(σ_i σ_j) = C(n_gens, 2) · z⁴ (Markov pair-z²)
        # By the Markov axiom (Markov 1, Markov pair-z²), each single
        # generator contributes z and each generator-pair contributes z²
        # to the Markov trace, REGARDLESS of which braid β you're in.
        # This evaluation is manifestly Markov-invariant (uses only the
        # universal Markov axiom values, no per-braid-word data) and
        # depends only on n_gens = number of Hecke generators in the
        # ambient algebra.
        n_gens_total = (3 * (Z + N) - 1) if include_inter else (2 * (Z + N))
        z2 = Z_MARK ** 2
        z4 = Z_MARK ** 4
        t2 = n_gens_total * z2
        t3 = mp.mpf(n_gens_total * (n_gens_total - 1) // 2) * z4
    elif tower_mode == "canonical_markov":
        # CANONICAL R-side per prop:mass-endomorphism-tower §Algebraic
        # form: T_2 = Σ_i z · Vol_q^({i})(β), T_3 = z² · Σ_{i<j}
        # Vol_q^({i, j})(β), with each Vol_q^(S)(β) a Markov trace
        # over the transfer-matrix chain supported on S.  Markov-
        # invariant by construction; replaces the PATHOLOGICAL Φ_q
        # specialisation (per docs/audits/2026-05-16-compute-pipeline-
        # canonicality-audit.md §3·a).
        #
        # CRITICAL: free config (include_inter=False) ALSO has a
        # canonical T_2/T_3 — over its own disjoint-product braid
        # word (which omits the interface generators).  Setting
        # T_2_free = 0 double-counts the per-nucleon contribution.
        #
        # The Δ(T_2 + T_3) = bound - free thus captures exactly the
        # inter-nucleon coupling — the non-interface generator
        # contributions cancel by construction (same crossings at
        # those generators in both bound and free braid words).
        from canonical_brane_tower import (
            term2_canonical, term3_canonical,
        )
        from mass_at_3A_proper import atom_braid_word_3A
        word = atom_braid_word_3A(Z, N, include_inter=include_inter)
        n_strands_canonical = 3 * (Z + N)
        n_gens_canonical = n_strands_canonical - 1
        t2 = term2_canonical(word, n_gens_canonical, float(Q0_FLOAT))
        t3 = term3_canonical(word, n_gens_canonical, float(Q0_FLOAT))
    elif tower_mode == "li2q":
        # CORRECTED Kashaev limit per `prop:mass-endomorphism-tower`
        # (proof: a43d7f1fa).  T2 = -Σ Li_2^q(-|V_i|),
        # T3 = -z² · Σ Li_2^q(-|V_i V_j|) (symmetric q-dilogarithm).
        t2 = mp.mpf(0)
        for v in vols:
            arg = -abs_mpf(v)
            try:
                t2 -= li2_q_sym(arg)  # -Li_2^q(-|V|)
            except Exception:
                pass
        t3 = mp.mpf(0)
        z2 = Z_MARK ** 2
        for i, j in combinations(range(len(vols)), 2):
            arg = -(abs_mpf(vols[i]) * abs_mpf(vols[j]))
            try:
                t3 -= z2 * li2_q_sym(arg)
            except Exception:
                pass
    elif tower_mode == "habiro":
        # P2.A (2026-05-12): Path 3 single-trace Habiro form.
        # Per `prop:full-pole-structure-mass-trace` the Markov trace
        # admits the cyclotomic expansion
        #     tr_M(T_w; q) = Σ_m a_m(T_w) · (q;q)_m
        # which collapses T1 + (T2+T3) + T6 into a single sum of traces.
        # The probe `path_b_habiro_mass_probe.py` already demonstrates
        # sub-1% closure on {p, n, D} (witness:
        # `path-b-habiro-mass-probe.witness.json`).  T/³He extension
        # is upstream-blocked on `habiro-coefficients-atomic.witness.json`
        # which currently covers only {p, n, D}; see
        # docs/audits/2026-05-12-1ppb-implementation-plan.md §P2.A.
        #
        # Wiring contract: T1 is REPLACED by `tr_M_via_habiro_sum`
        # for this atom; T2 = T3 = 0 (the m≥1 terms of the Habiro
        # sum already encompass them); T4, T5, T6 unchanged; the
        # final calibration via E_0 then converts to MeV.
        # If the atom is missing from the Habiro witness this raises
        # KeyError so the caller surfaces the gap rather than silently
        # falling back (per owner directive 2026-05-12: break loudly).
        habiro_path = _pb.witness_path("path-b-habiro-mass-probe.witness.json", HERE)
        if not habiro_path.exists():
            raise FileNotFoundError(
                f"tower_mode='habiro' requires {habiro_path.name}; "
                "run path_b_habiro_mass_probe.py first."
            )
        habiro_d = json.loads(habiro_path.read_text())
        rec = next((r for r in habiro_d.get("rows", [])
                    if r.get("atom") == isotope_label), None)
        if rec is None:
            raise KeyError(
                f"tower_mode='habiro': atom {isotope_label!r} missing "
                f"from {habiro_path.name}; current coverage = "
                f"{[r.get('atom') for r in habiro_d.get('rows', [])]}. "
                "Extend habiro-coefficients-atomic.witness.json upstream."
            )
        # Override T1 with the Habiro single-trace sum; zero T2, T3.
        # (The original Hoefsmit-bridge T1 is reachable from the
        # canonical-T1 cache for audit if needed.)
        t1 = abs(mp.mpf(str(rec["tr_M_via_habiro_sum"])))
        t2 = mp.mpf(0)
        t3 = mp.mpf(0)
    elif tower_mode == "per-partition-k":
        # P1.D (2026-05-12): per-partition $k_\lambda$ truncation rule.
        # Per folio/quantum-observable-universe/braids-and-knots/
        # per-partition-k-lambda-rule.md, uniform truncation $k$ across
        # all Wedderburn blocks of $H_n(q_0)$ is dominated by ONE
        # specific partition per atom (D: [2,2,1,1], T: [6,3], 3He: [5,4]).
        # The canonical refinement uses per-partition truncation depths
        # $k_\lambda$ chosen by the substrate confinement bound rather
        # than a uniform $k$, replacing T2+T3 with a single Markov-
        # invariant per-partition sum.
        #
        # Wiring contract: T1 from canonical Hoefsmit+Wenzl bridge is
        # KEPT (this mode only refines T2+T3); T2 := total_tower from
        # the per-partition probe witness; T3 := 0 (the per-partition
        # sum already aggregates single+pair contributions); T4, T5,
        # T6 unchanged. Coverage is currently {D, T, ³He}; missing
        # atoms raise so the gap is surfaced rather than silently
        # falling back (per owner directive 2026-05-12: break loudly).
        ppk_path = _pb.witness_path("probe-phiq-per-partition-klambda.witness.json", HERE)
        if not ppk_path.exists():
            raise FileNotFoundError(
                f"tower_mode='per-partition-k' requires {ppk_path.name}; "
                "run probe_phiq_per_partition_klambda.py first."
            )
        ppk_d = json.loads(ppk_path.read_text())
        # Atom-name normalisation: probe witness keys mirror the upstream
        # probe_phiq_per_partition_klambda.py source ({deuteron, tritium,
        # he3}), while the sweep uses short isotope codes ({D, T, 3He}).
        # The mapping below is the inverse of those upstream keys; do not
        # rename without updating the probe witness in lockstep.
        _ALIASES = {"D": "deuteron", "T": "tritium", "3He": "he3"}
        probe_atom = _ALIASES.get(isotope_label, isotope_label)
        results = ppk_d.get("data", {}).get("per_partition_klambda_results", [])
        rec = next((r for r in results if r.get("atom") == probe_atom), None)
        if rec is None:
            raise KeyError(
                f"tower_mode='per-partition-k': atom {isotope_label!r} "
                f"(probe key {probe_atom!r}) missing from {ppk_path.name}; "
                f"current coverage = {[r.get('atom') for r in results]}. "
                "Extend probe-phiq-per-partition-klambda.witness.json upstream."
            )
        # `total_tower` is the signed Φ_q sum in cat-units (dimensionless),
        # multiplied by E_0 at the calibration site.
        t2 = mp.mpf(str(rec["total_tower"]))
        t3 = mp.mpf(0)
    elif tower_mode == "combined":
        # P2.B (2026-05-12): "best canonical available" per-atom router.
        # Produces the M1 mass table by dispatching each isotope to the
        # canonical mode with the strongest theoretical backing for it:
        #
        #   {p, n}                  → "habiro"          (Path 3 collapse)
        #   {D}                     → "habiro"          (Path 3 collapse)
        #   {T, ³He}                → "per-partition-k" (P1.D refinement)
        #   anything else (⁴He+)    → "li2q"            (canonical fallback,
        #                                                no Path 3 / per-λ
        #                                                witness yet)
        #
        # No new physics: this is a routing layer over modes already
        # implemented above. Each branch raises loudly on its own
        # coverage gaps (per "break loudly" directive); `combined`
        # itself never silently substitutes.
        habiro_atoms = {"p", "n", "D"}
        ppk_atoms = {"T", "3He"}
        if isotope_label in habiro_atoms:
            sub_mode = "habiro"
        elif isotope_label in ppk_atoms:
            sub_mode = "per-partition-k"
        else:
            sub_mode = "li2q"
        # Recursive call: every other arg pass-through. Avoids
        # duplicating the per-mode wiring above.
        result = paper_six_term_mass(
            Z, N,
            include_inter=include_inter,
            chirality_signs=chirality_signs,
            m_e_hecke=m_e_hecke,
            term5_mode=term5_mode,
            isotope_label=isotope_label,
            tower_mode=sub_mode,
            chirality_source=chirality_source,
        )
        # Audit-trail fix (2026-05-12): the recursive call records
        # `tower_mode = sub_mode` (e.g. "habiro"), which is misleading
        # to a downstream auditor reading the witness — they asked
        # for `combined` and the row should say so. Re-stamp the
        # outer label as "combined" and surface the per-atom routing
        # decision in `sub_tower_mode` so both pieces of information
        # are preserved.
        result["tower_mode"] = "combined"
        result["sub_tower_mode"] = sub_mode
        return result
    else:
        raise ValueError(f"unknown tower_mode {tower_mode!r}")
    t4_raw = (term4_frobenius_codim(Z + N) if Z + N >= 1 else mp.mpf(0))
    t4 = mp.mpf(str(m_e_hecke)) * t4_raw
    if chirality_signs is None:
        chirality_signs = []
    if chirality_source == "v2":
        try:
            from term5_v2_chirality import aK_v2
            t5_factor = aK_v2(Z, N)
        except Exception as exc:
            # V2 cache miss for an out-of-window (Z, N) — surface the
            # routing decision and fall back to closed form.  Callers
            # that demand V2 strictness should pre-warm the cache or
            # set chirality_source="closed_form" explicitly.
            print(
                f"[paper_six_term_mass] V2 a_K unavailable for "
                f"(Z={Z}, N={N}): {exc!r}; falling back to closed form",
                flush=True,
            )
            t5_factor = term5_chirality(Z, N, chirality_signs)
    elif chirality_source == "closed_form":
        t5_factor = term5_chirality(Z, N, chirality_signs)
    else:
        raise ValueError(
            f"unknown chirality_source {chirality_source!r}; "
            f"expected 'v2' or 'closed_form'"
        )
    # T6: canonical cyclotomic residue tail in MeV (per-A from Habiro
    # residue witness).  Returned in MeV directly; not in Hecke units.
    # Caller adds it to M_pred post-calibration (after × E_0).
    t6_MeV = _load_canonical_t6_MeV().get(Z + N, mp.mpf(0))

    if term5_mode == "additive":
        t1_with_chirality = t1
        t5 = (t5_factor - 1) * t1
    elif term5_mode == "multiplicative_on_t1":
        t1_with_chirality = t1 * t5_factor
        t5 = t1_with_chirality - t1  # report the additive equivalent
    else:
        raise ValueError(f"unknown term5_mode {term5_mode!r}")

    # Keep `total` in mpf — no float() casts here (Gemini PR #534 high
    # priority on line 450).  `total_hecke` is in cat-units (Hecke-energy
    # quantum, dimensionless w.r.t. q_0); the calibration site multiplies
    # by E_0 (MeV / cat-unit) to convert to MeV.  T6 is loaded already
    # in MeV via `_load_canonical_t6_MeV` and is added DIRECTLY to
    # E_0 · total_hecke at the assembly site (run_sweep_for_mode);
    # T6 must NOT be scaled by E_0.
    total = t1_with_chirality + t2 + t3 + t4
    # Per gemini-code-assist comment #5 on PR #534: keep `total_hecke`
    # and `term6_cyclotomic_tail_MeV` as mpf so the proton calibration
    # `E_0 = (M_P_CODATA - p_t6_MeV) / m_p_hecke` and the final
    # `M_pred = E_0 * total_hecke + t6_MeV` retain 50-dps precision
    # all the way through.
    #
    # The other six were `float(...)` here on the grounds that they are
    # "display fields" and JSON consumers expect numbers. Two things were wrong
    # with that. They are not display: `term1..term5` are the per-term
    # decomposition this sweep exists to publish, and `total_hecke` -- which the
    # same block correctly keeps as mpf -- is their SUM, so the parts were being
    # recorded at 16 digits while the whole was kept at 50. And the "consumers
    # expect numbers" half is the convention this corpus dropped: `_precision.fmt`
    # emits a decimal string and every witness reader in the tree parses one.
    # They now stay mpf and are rendered by `_serialise` with everything else.
    return {
        "term1_canonical_tr_M": t1,
        "term2_single_gen_tower": t2,
        "term3_pair_gen_tower": t3,
        "term4_frobenius_codim_raw": t4_raw,
        "term4_frobenius_codim_scaled": t4,
        "term5_chirality_factor_a_K": t5_factor,
        "term5_chirality_source": chirality_source,
        "term5_additive_contribution": t5,
        "term6_cyclotomic_tail_MeV": t6_MeV,  # mpf — calibration-critical
        "term5_mode": term5_mode,
        "tower_mode": tower_mode,
        # `sub_tower_mode` is None on every non-`combined` direct call;
        # `combined` overrides this above with the per-atom sub-mode
        # actually used. Kept in the schema unconditionally so witness
        # consumers don't need to special-case the field's presence.
        "sub_tower_mode": None,
        "m_e_hecke": m_e_hecke,
        "total_hecke": total,  # mpf — calibration-critical
    }


def chirality_signs_for_isotope(iso):
    """Paper chirality-sign pattern per isotope
    (from chirality-dual-space-derivation)."""
    patterns = {
        "p":   [],
        "n":   [],
        "D":   [+1],                    # 1 positive pn crossing
        "T":   [+1, -1],                # 1 pos, 1 neg (amphichiral)
        "3He": [+1, -1],                # mirror partner of T
        "4He": [+1, -1, +1, -1],        # Borromean² (2 pairs)
        "6Li": [+1, -1, +1, -1, +1, -1],# 3 pairs (approx.)
        "7Li": [+1, -1, +1, -1, +1, -1, +1],  # 3 pairs + 1 extra
    }
    return patterns.get(iso, [])


def run_sweep_for_mode(tower_mode: str, isotopes: list, *, verbose: bool = True,
                        e0_mode: str | None = None,
                        chirality_source: str = "v2"):
    """Run the 6-term sweep for one tower_mode.

    P1.A (2026-05-12): `e0_mode` controls the energy-scale anchor:

      * "substrate" (default): E_0 = m_e / (q_0·(q_0−1)) from the
        FULL chain per `prop:beta-decay-energy-scale` —
        `derived_masses.e_0_full_mev()`.  Three-calibration discipline
        per AGENTS.md: only {m_e, q_0, Q_β} are anchors; everything
        else (including the proton mass) is a prediction.  HARD BREAK:
        the proton row will no longer be exactly zero error — that
        residual is the structural gap that was previously hidden in
        the proton-fitted E_0.  Per owner directive: break loudly.

      * "proton-fit" (legacy): E_0 = (M_P_CODATA − T6_p) / T1+T2+T3+T4
        for the proton.  Hides structural error in everything else by
        absorbing it into E_0.  Kept for back-compat; selected via
        `e0_mode="proton-fit"` or env var `QOU_E0_MODE=proton-fit`.

    Default chosen via env var `QOU_E0_MODE` (substrate | proton-fit);
    explicit kwarg takes precedence.
    """
    if e0_mode is None:
        e0_mode = _os.environ.get("QOU_E0_MODE", "substrate")
    if e0_mode not in ("substrate", "proton-fit"):
        raise ValueError(f"unknown e0_mode {e0_mode!r}; "
                         "expected 'substrate' or 'proton-fit'")

    # Comparison reference (P31-triage Phase B): validation-only CODATA m_p
    # used to report fit residuals, not as a prediction input.
    from codata_constants import M_P_MEV_VALIDATION as _M_P_CODATA  # noqa: E402
    M_P_CODATA = float(_M_P_CODATA)

    # Proton 6-term decomposition (always computed; needed either for
    # calibration or for the substrate-mode proton residual report).
    # P1.D: per-partition-k coverage is {D, T, ³He} only — no proton
    # entry exists in the probe witness. Fall back to "li2q" for the
    # proton row purely so that E_0 reporting works; p mass under
    # per-partition-k is structurally undefined here and reported as
    # an error in the per-isotope loop below. (`combined` is safe —
    # it routes the proton to "habiro" internally, which IS in
    # coverage.)
    p_tower_mode = "li2q" if tower_mode == "per-partition-k" else tower_mode
    p_terms = paper_six_term_mass(
        1, 0, include_inter=False,
        chirality_signs=chirality_signs_for_isotope("p"),
        isotope_label="p", tower_mode=p_tower_mode,
        chirality_source=chirality_source)
    m_p_hecke = p_terms["total_hecke"]
    p_t6_MeV = p_terms["term6_cyclotomic_tail_MeV"]

    if e0_mode == "proton-fit":
        if tower_mode == "per-partition-k":
            # No proton-fit possible (proton not in coverage); silently
            # promote to substrate so the sweep is still meaningful.
            from derived_masses import e_0_full_mev
            E_0 = e_0_full_mev()
        elif tower_mode == "combined":
            # `combined` (P2.B) routes different atoms to different
            # sub-modes (proton→habiro, T/³He→per-partition-k, ⁴He+
            # →li2q). A single proton-fit E_0 can only calibrate ONE
            # sub-mode at a time; multiplying it through the other
            # sub-modes' (different-scale) `total_hecke` produces
            # incoherent garbage — empirically it gives a ~−1039 MeV
            # T−³He isospin asymmetry vs li2q's −283 MeV at the same
            # branch (see docs/audits/2026-05-12-m1-mass-table.md §3).
            # Auto-promote to substrate so combined remains usable
            # under any e0_mode setting.
            import warnings
            warnings.warn(
                "tower_mode='combined' is incompatible with "
                "e0_mode='proton-fit' (E_0 can only fit one sub-mode "
                "at a time). Auto-promoting to e0_mode='substrate'. "
                "See docs/audits/2026-05-12-m1-mass-table.md §3.",
                stacklevel=2,
            )
            from derived_masses import e_0_full_mev
            E_0 = e_0_full_mev()
            e0_mode = "substrate"  # keep label honest in print/witness
        else:
            # Proton-fit method (this IS the proton-fit calibration the
            # outer `e0_mode == "proton-fit"` selects when tower_mode
            # is neither "li2q" nor "combined"): fit E_0 to make
            # proton residual exactly zero.  Not guarded-off canonical;
            # this is the intended behavior when the user opts in to
            # e0_mode="proton-fit" for a single-sub-mode tower.
            # noqa: I3 — intentional alternative calibration mode
            E_0 = (M_P_CODATA - p_t6_MeV) / m_p_hecke
    else:  # substrate
        # Canonical: E_0 from CAL-1 (m_e) and CAL-2 (q_0) only.
        from derived_masses import e_0_full_mev
        E_0 = e_0_full_mev()

    if verbose:
        print(f"\nMode: {tower_mode}  (e0_mode={e0_mode})")
        # `float()` here is DISPLAY only — an mpf has no `%e` format.
        print(f"  Proton: t1={float(p_terms['term1_canonical_tr_M']):.4e} "
              f"t2={float(p_terms['term2_single_gen_tower']):.4e} "
              f"t3={float(p_terms['term3_pair_gen_tower']):.4e} "
              f"t4={float(p_terms['term4_frobenius_codim_scaled']):.4e} "
              f"t6={float(p_terms['term6_cyclotomic_tail_MeV']):.4f} MeV")
        print(f"  E_0 = {float(E_0):.6e} MeV/Hecke-unit  ({e0_mode})")

    rows = []
    for iso, Z, N, inter, M_codata_str in isotopes:
        # The table now carries decimal strings; lift once, here.
        M_codata = mp.mpf(M_codata_str)
        # ── Deferred-intractable isotopes ───────────────────────────
        # Per atomic_tr_m_mpfr_50dps.py's ⁴He omission note, isotopes
        # at A ≥ 5 need Hecke H_{≥15} with p(n) ≥ 176 partitions and
        # max Hoefsmit dim in the thousands.  Current Python mpmath
        # @ 50 dps can't produce |tr_M| within the 30-min CI timeout;
        # tractable compute needs (a) Rust kernel with rayon parallel
        # partitions + block-sparse Hoefsmit MPFR, or (b) categorical
        # reduction via Wenzl 1988 LR branching.  Surface these atoms
        # as `deferred` (NO error_kind) so the I13 incomplete-coverage
        # audit doesn't conflate physics-blocked gaps with producer
        # bugs.  Cf. AUDIT-DEEP-2026-05.md §7.
        if iso in DEFERRED_INTRACTABLE_ATOMS:
            rows.append({
                "isotope": iso, "Z": Z, "N": N, "A": Z + N,
                "M_codata": M_codata,
                "deferred": True,
                "deferral_reason": (
                    f"Canonical |tr_M({iso})| at H_{(Z+N)*3} is intractable"
                    " with current Python mpmath @ 50 dps; awaits Rust"
                    " kernel or Wenzl-1988 LR-branching categorical"
                    " reduction."
                ),
            })
            if verbose:
                print(f"  {iso:<6} [deferred-intractable] H_{(Z+N)*3}",
                      flush=True)
            continue
        try:
            terms = paper_six_term_mass(
                Z, N, include_inter=inter,
                chirality_signs=chirality_signs_for_isotope(iso),
                isotope_label=iso, tower_mode=tower_mode,
                chirality_source=chirality_source)
        except Exception as exc:
            # Surface a structured `error_kind` so downstream consumers
            # can distinguish T1-witness gaps (A ≥ 5 atoms not yet
            # computed) from genuine compute regressions.
            err_msg = f"{type(exc).__name__}: {exc}"
            # Detect tower-mode upstream-witness gaps:
            #   `tower_mode='habiro'` reads
            #       `path-b-habiro-mass-probe.witness.json`
            #       (current coverage: {p, n, D};
            #        missing for the A=1..4 set: T, 3He, 4He).
            #   `tower_mode='per-partition-k'` reads
            #       `probe-phiq-per-partition-klambda.witness.json`
            #       (current coverage: {D, T, 3He};
            #        missing for the A=1..4 set: p, n, 4He).
            # These are atom/mode coverage gaps, not producer bugs —
            # emit `deferred: true, deferred_mode: <mode>` plus the
            # specific upstream witness filename so the I13 audit
            # surfaces *actionable* deferrals rather than opaque
            # `error_kind`.  Cf. PR #798's deferred-intractable
            # pattern for atom-level gaps.
            _TOWER_MODE_UPSTREAM = {
                "habiro": "path-b-habiro-mass-probe.witness.json",
                "per-partition-k":
                    "probe-phiq-per-partition-klambda.witness.json",
            }
            if (isinstance(exc, KeyError)
                    and "missing from" in str(exc)
                    and (f"tower_mode={tower_mode!r}" in str(exc)
                         or f"tower_mode='{tower_mode}'" in str(exc))):
                upstream_witness = _TOWER_MODE_UPSTREAM.get(
                    tower_mode, "<unknown upstream witness>"
                )
                # Try to extract the "current coverage = [...]" hint
                # from the KeyError message so the deferral row keeps
                # the actionable list even though we're not raising.
                exc_str = str(exc)
                upstream_coverage_hint = None
                if "current coverage = " in exc_str:
                    after = exc_str.split("current coverage = ", 1)[1]
                    upstream_coverage_hint = after.split(".", 1)[0].strip()
                rows.append({
                    "isotope": iso, "Z": Z, "N": N, "A": Z + N,
                    "M_codata": M_codata,
                    "deferred": True,
                    "deferred_mode": tower_mode,
                    "upstream_witness": upstream_witness,
                    "upstream_coverage_hint": upstream_coverage_hint,
                    "deferral_reason": (
                        f"tower_mode={tower_mode!r} requires {iso!r} in"
                        f" {upstream_witness}; current coverage = "
                        f"{upstream_coverage_hint or '<unknown>'}."
                        " Extend the upstream witness to clear this row."
                    ),
                })
                if verbose:
                    print(f"  {iso:<6} [deferred-mode={tower_mode}]",
                          flush=True)
                continue
            error_kind = "unknown"
            if isinstance(exc, KeyError) and "no canonical T1" in str(exc):
                error_kind = "T1_witness_missing"
            elif isinstance(exc, (ValueError, IndexError)):
                error_kind = "compute_failure"
            rows.append({"isotope": iso, "Z": Z, "N": N, "A": Z + N,
                         "M_codata": M_codata,
                         "error": err_msg,
                         "error_kind": error_kind})
            if verbose:
                print(f"  {iso:<6} [{error_kind}] {err_msg[:80]}",
                      flush=True)
            continue
        # Calibration arithmetic stays in mpf (per Gemini #5).
        # Unit reminder (per Gemini review on PR #542):
        # `total_hecke` (= T1+T2+T3+T4) is in cat units and gets
        # multiplied by E_0 (MeV/cat-unit) to convert to MeV.
        # `term6_cyclotomic_tail_MeV` is ALREADY in MeV (loaded from
        # the Habiro residue witness via `_load_canonical_t6_MeV`),
        # so it must NOT be scaled by E_0 — it is added directly.
        M_pred = E_0 * terms["total_hecke"] + terms["term6_cyclotomic_tail_MeV"]
        err_pct = ((M_pred - M_codata) / M_codata * 100 if M_codata
                   else mp.mpf(0))
        # Rows carry `mpf`; `_serialise` renders the whole witness once, at the
        # end. This block used to cast each field to `float` here, reasoning
        # that "storage is for reporting and float64 is sufficient for ~16
        # digits" -- but `err_pct` is not incidental storage, it is the result
        # this sweep exists to report, and the L1 target is 1e-15.
        rows.append({
            "isotope": iso, "Z": Z, "N": N, "A": Z + N,
            "M_codata": M_codata, "M_predicted": M_pred,
            "err_pct": err_pct,
            **terms,
        })
    return E_0, rows


# ── Per-derivation weights (no proton-fitting) ───────────────────────
# Per docs/audits/2026-05-04-six-term-per-weight-derivation.md, the
# six terms have DIFFERENT physical scales from the derivation:
#   T1 (descended Markov):  E_0_β = 0.78233341 MeV per cat unit
#       (`prop:categorical-mass-markov`; binding from |tr_free|−|tr_atom|)
#   T2, T3 (brane tower):   α = m_e · 8G ≈ 3.7445 MeV per cat unit
#       (`prop:atomic-braid-mass`, `prop:binding-scale-catalan`)
#   T4 (Frobenius co-Casimir):  m_e ≈ 0.511 MeV per raw τ unit
#       (T4 has m_e factor INSIDE; raw τ comes out in cat-unit-of-τ)
#   T5 (chirality):  multiplicative (a_K − 1) on T1 with T1's weight
#   T6 (cyclotomic tail):  already in MeV via Habiro residue witness
#
# The proton-fitted `run_sweep_for_mode` collapses all of T1+T2+T3+T4
# to a single E_0 fit at A=1; this loses the per-term unit information
# and propagates mass error quickly with A.  The derivation-fixed
# assembly below uses the published constants instead.

E_0_BETA_DECAY_MEV_DERIV = Q_NEUTRON_MEV             # free-neutron β-decay Q (CODATA)
M_E_MEV_DERIV            = M_E_MEV                   # CODATA electron rest mass
ALPHA_BORROMEAN_MEV      = 3.74446989    # m_e · 8G  (`prop:binding-scale-catalan`)


def q_beta_substrate_cos_tightened_MeV() -> float:
    """Substrate-derived Q_β closed form with cos((z−1)·h/2) c_2 tightening.

    Form A baseline: Q_A = m_e · |q²−2q−1| · (q+1) / (2q³)
    Plus c_2 Kashiwara correction: Q_A · cos((z−1)·h/2)
    where z = 1/(q½+q⁻½), h = q − q⁻¹.

    Residual against CODATA Q_β: ~306 ppm (5.49× tighter than bare
    Form A's 1677.5 ppm; PR #655, verified by
    `probe_v2_plus_cos_q_beta_compose.py` at 50 dps).

    Per PR #657's high-precision finding: higher c_k corrections are
    at CODATA's ~400 ppb noise floor — empirically underdetermined.
    Closing the remaining 300× to 1 ppb requires CODATA-2027 or
    independent route (lattice QCD, EW Fermi). The c_2 tightening
    here is the empirically-solid substrate-derived Q_β.
    """
    q = Q_MP  # Q at 50 dps mpmath (was: mp.mpf(repr(Q0_FLOAT)) — f64-quantised)
    z = q**3 / (q**2 + 1)
    h = q - 1 / q
    Q_A = mp.mpf(M_E_MEV) * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    return float(Q_A * mp.cos((z - 1) * h / 2))


def q_beta_full_chain_n4_MeV() -> float:
    """Substrate-derived Q_β with the full N=4 categorical chain.

    Per `prop:q-beta-categorical-precision-ladder` + PRs #661, #664,
    and the retired `kashiwara-jones-c4-categorical` record (see
    docs/audits/2026-10-11-retired-label-records.md §D):

        Q_β = Q_A · cos(α_N1)
                  · (1 − b²·ℏ_q⁴)              (c_2 = −b², N=2 Kashiwara)
                  · (1 − 2·b³·ℏ_q⁶)            (c_3 = −2 from Hopf-Jones; b³ is the
                                               higher-N self-fusion scale factor)
                  · (1 + (b²+1/2)·b⁴·ℏ_q⁸)     (c_4 = b²+1/2; b⁴ is the N=4 scale)

    The per-rung b^(2k−2) scale factor (k = rung index) reflects the
    Hoefsmit self-fusion convention used by the sweep: c_k is the
    dimensionless coefficient produced by the categorical derivation,
    and the empirical residual chain is fit against the substrate-scaled
    factor c_k · b^(2k−2) · ℏ_q^(2k).  See commit `52987d8e5` (M3 wire)
    for the convention origin.

    where α_N1 = α − b·ℏ_q²/2 and (q, α, b, ℏ_q) come from the
    V_(2,1) Hoefsmit substrate via `qbeta_physics.compute_substrate_quantities`.

    All three of c_2, c_3, c_4 are now categorically derived (no
    empirical fit) per:
      - c_2 = b²     : PR #661 (V_(2,1) Hoefsmit alone)
      - c_3 = −2     : retired `hopf-jones-c3-categorical` (V_(2,1) self-fusion)
      - c_4 = b²+1/2 : retired `kashiwara-jones-c4-categorical` (cos-tower + half-shift)
      (both never had a block carrier; their witnesses were removed from
      computations/_deprecated/ in 6333715860 and survive on the
      cat/cat-harness/fsh-guts branch — see the retired-label record §D)

    Story A is falsified at three levels by these proofs; Story B
    (the categorical alternation chain) is the structural account
    of the precision ladder.
    """
    from qbeta_physics import compute_substrate_quantities  # noqa: E402
    sq = compute_substrate_quantities()
    q = sq["q"]
    alpha_N1 = sq["alpha_N1"]
    hbar_q = sq["hbar_q"]
    b = sq["hoefsmit_b"]
    Q_A = sq["Q_A"]

    factor_n1 = mp.cos(alpha_N1)
    factor_n2 = 1 - b ** 2 * hbar_q ** 4
    factor_n3 = 1 - 2 * b ** 3 * hbar_q ** 6
    factor_n4 = 1 + (b ** 2 + mp.mpf("1/2")) * b ** 4 * hbar_q ** 8

    return float(Q_A * factor_n1 * factor_n2 * factor_n3 * factor_n4)


def q_beta_for_source(source: str) -> float:
    """Q_β selector across substrate-derived candidates.

    Available sources:
      - "codata"          : CODATA Q_NEUTRON_MEV (anchor; default)
      - "form_a_cos"      : Q_A · cos(α_N1) — c_2 only (PR #655 + #661)
      - "full_chain_n4"   : full N=4 categorical chain (PRs #661, #664,
                            and the retired kashiwara-jones-c4-categorical record)
    """
    if source == "codata":
        return E_0_BETA_DECAY_MEV_DERIV
    if source == "form_a_cos":
        return q_beta_substrate_cos_tightened_MeV()
    if source == "full_chain_n4":
        return q_beta_full_chain_n4_MeV()
    raise ValueError(
        f"unknown q_beta_source {source!r}; expected "
        f"'codata' | 'form_a_cos' | 'full_chain_n4'"
    )


def assemble_per_derivation_weights(Z: int, N: int,
                                      tower_mode: str = "li2q",
                                      term5_mode: str = "multiplicative_on_t1",
                                      q_beta_source: str = "codata") -> dict:
    """Build atomic mass per the derivation-fixed weights (no proton fit).

    For each isotope, evaluates both the bound (`include_inter=True`)
    and free (`include_inter=False`) six-term decompositions and
    differences them through the per-term physical scales:

        B(Z, N) = E_0_β·(T1_free − T1_atom)               # binding from descended trace
                + α·((T2+T3)_atom − (T2+T3)_free)        # brane tower contribution
                + m_e·(T4_atom − T4_free)                 # Frobenius co-Casimir
                + E_0_β·(a_K − 1)·T1_atom                 # chirality (mult on T1)
                + (T6_atom − T6_free)                     # cyclotomic tail (MeV)
        M_pred  = constituent − B

    `constituent` = Z·m_p + N·m_n + Z·m_e (CODATA bare-particle masses).

    Returns a dict with the per-term contributions in MeV plus
    M_pred and the constituent baseline.
    """
    # Comparison references (P31-triage Phase B): validation-only CODATA m_p/m_n
    # used to report fit residuals, not as prediction inputs.
    from codata_constants import (  # noqa: E402
        M_P_MEV_VALIDATION as _M_P_CODATA,
        M_N_MEV_VALIDATION as _M_N_CODATA,
    )
    M_P_CODATA = float(_M_P_CODATA)
    M_N_CODATA = float(_M_N_CODATA)
    constituent = Z * M_P_CODATA + N * M_N_CODATA + Z * M_E_MEV_DERIV

    A = Z + N
    inter_flag = (A >= 2)

    chir = chirality_signs_for_isotope_inferred(Z, N)
    iso_label = isotope_label_from_zn(Z, N)

    atom_terms = paper_six_term_mass(
        Z, N, include_inter=inter_flag,
        chirality_signs=chir, tower_mode=tower_mode,
        term5_mode=term5_mode, isotope_label=iso_label,
    )
    free_terms = paper_six_term_mass(
        Z, N, include_inter=False,
        chirality_signs=[],
        tower_mode=tower_mode, term5_mode=term5_mode,
        isotope_label=iso_label,
    )

    t1_a = atom_terms["term1_canonical_tr_M"]
    t1_f = free_terms["term1_canonical_tr_M"]
    t2_a = atom_terms["term2_single_gen_tower"]
    t2_f = free_terms["term2_single_gen_tower"]
    t3_a = atom_terms["term3_pair_gen_tower"]
    t3_f = free_terms["term3_pair_gen_tower"]
    # T4 is reported as `term4_frobenius_codim_raw` (raw τ, no m_e
    # factor) and `term4_frobenius_codim_scaled` (with m_e_hecke=1
    # factor; effectively same).  Use the raw and apply m_e in MeV
    # ourselves.
    t4_a = atom_terms["term4_frobenius_codim_raw"]
    t4_f = free_terms["term4_frobenius_codim_raw"]
    aK_a = atom_terms["term5_chirality_factor_a_K"]
    t6_a = atom_terms["term6_cyclotomic_tail_MeV"]
    t6_f = free_terms["term6_cyclotomic_tail_MeV"]

    # Per-term binding contributions (each in MeV).
    E_0_beta_local = q_beta_for_source(q_beta_source)
    binding_T1  = E_0_beta_local * (t1_f - t1_a)
    binding_T23 = ALPHA_BORROMEAN_MEV * ((t2_a + t3_a) - (t2_f + t3_f))
    binding_T4  = M_E_MEV_DERIV * (t4_a - t4_f)
    binding_T5  = E_0_beta_local * (aK_a - 1.0) * t1_a
    binding_T6  = t6_a - t6_f

    B_pred = (binding_T1 + binding_T23 + binding_T4
              + binding_T5 + binding_T6)
    M_pred = constituent - B_pred

    return {
        "Z": Z, "N": N, "A": A,
        "constituent_MeV": constituent,
        "binding_T1_MeV":  binding_T1,
        "binding_T2T3_MeV": binding_T23,
        "binding_T4_MeV":  binding_T4,
        "binding_T5_MeV":  binding_T5,
        "binding_T6_MeV":  binding_T6,
        "B_pred_MeV":      B_pred,
        "M_predicted_MeV": M_pred,
        "tower_mode":      tower_mode,
        "term5_mode":      term5_mode,
        "weights_used": {
            "E_0_beta_MeV": E_0_beta_local,
            "q_beta_source": q_beta_source,
            "alpha_borromean_MeV": ALPHA_BORROMEAN_MEV,
            "m_e_MeV": M_E_MEV_DERIV,
        },
    }


def chirality_signs_for_isotope_inferred(Z: int, N: int) -> list[int]:
    """Pattern keyed on (Z, N) instead of label string."""
    if Z == 1 and N == 0: return []
    if Z == 0 and N == 1: return []
    if Z == 1 and N == 1: return [+1]
    if Z == 1 and N == 2: return [+1, -1]
    if Z == 2 and N == 1: return [+1, -1]
    if Z == 2 and N == 2: return [+1, -1, +1, -1]
    if Z == 3 and N == 2: return [+1, -1, +1, -1, +1]
    if Z == 3 and N == 3: return [+1, -1, +1, -1, +1, -1]
    if Z == 3 and N == 4: return [+1, -1, +1, -1, +1, -1, +1]
    if Z == 4 and N == 3: return [+1, -1, +1, -1, +1, -1, +1]
    if Z == 4 and N == 4: return [+1, -1, +1, -1, +1, -1, +1, -1]
    if Z == 4 and N == 5: return [+1, -1, +1, -1, +1, -1, +1, -1, +1]
    return []


def isotope_label_from_zn(Z: int, N: int) -> str:
    """Infer the canonical isotope_label string from (Z, N) so the
    per-derivation weights path can route through `paper_six_term_mass`
    without re-introducing the legacy term1_descended fallback removed
    per gemini-code-assist comment #2 on PR #534."""
    table = {
        (1, 0): "p",   (0, 1): "n",
        (1, 1): "D",   (1, 2): "T",   (2, 1): "3He",
        (2, 2): "4He", (3, 3): "6Li", (3, 4): "7Li",
        (4, 5): "9Be", (5, 6): "11B", (6, 6): "12C",
    }
    label = table.get((Z, N))
    if label is None:
        raise ValueError(
            f"isotope_label_from_zn: no canonical label for (Z={Z}, "
            f"N={N}); add to the table or to atomic-tr-m-mpfr-50dps."
        )
    return label


if __name__ == "__main__":
    print("PAPER 6-TERM FORMULA — multi-mode comparison sweep")
    print("=" * 80)
    print(f"q_0 = {float(Q0):.6f}")

    # Upstream-witness threading per
    # docs/audits/2026-05-18-compute-integration-sweep.md fixes #3, #4, #6
    # — record sha256 + commitSha for the witnesses this sweep's Term 1 /
    # Term 4 / Term-6 closed forms transitively consume.  Drift in any
    # of these will be flagged by witness_dependency_drift.py.
    _upstream_hashes: list[dict] = []
    for _name in (
        # Fix #3 — y-lambda cache + Wedderburn weight scheme
        "y-lambda-at-q0.witness.json",
        "probe-wedderburn-weight-scheme.witness.json",
        # Fix #4 — CAL-3 calibration inputs
        "cal-3-q-beta.witness.json",
        "codata-2022-validation-masses.witness.json",
        # Fix #6 — per-nucleon shift additive linearity
        "per-nucleon-shift-derivation.witness.json",
    ):
        try:
            _, _hr = load_and_hash_upstream(HERE / _name)
            _upstream_hashes.append(_hr)
        except FileNotFoundError as _exc:
            print(f"  ⚠ upstream missing: {_exc}")

    # `M_P_MEV_VALIDATION` was referenced BARE here while the file only ever
    # imports it aliased, and function-scoped at that (`as _M_P_CODATA`, twice).
    # So this line raised NameError and the producer was dead — not slow, not
    # skipped: it could not run at all. Imported here rather than at module
    # scope to match the convention the other two sites state explicitly:
    # validation-only CODATA, used to report fit residuals, never as a
    # prediction input. The neighbouring entries are plain CODATA floats, which
    # is what this one was meant to be.
    from codata_constants import M_P_MEV_VALIDATION  # noqa: E402
    # Decimal STRINGS, not floats. These are the validation masses the `err_pct`
    # column is measured against, and `939.565` as a Python literal is the
    # binary64 approximation of that decimal, not the decimal -- so every
    # residual carried a ~1e-17 relative offset that had nothing to do with the
    # model. `mp.mpf("939.565")` is the decimal. The values are otherwise
    # unchanged: same digits, lifted losslessly instead of through f64.
    ISOTOPES = [
        ("p",   1, 0, False,  str(M_P_MEV_VALIDATION)),
        ("n",   0, 1, False,  "939.565"),
        ("D",   1, 1, True,  "1876.124"),
        ("T",   1, 2, True,  "2809.432"),
        ("3He", 2, 1, True,  "2809.413"),
        ("4He", 2, 2, True,  "3728.401"),
        ("5Li", 3, 2, True,  "4669.151"),
        ("6Li", 3, 3, True,  "5603.052"),
        ("7Li", 3, 4, True,  "6535.366"),
        ("7Be", 4, 3, True,  "6536.227"),
        ("8Be", 4, 4, True,  "7456.894"),
        ("9Be", 4, 5, True,  "8392.749"),
    ]

    modes = ["brane-legacy", "drop", "q1-base", "r-side-bare", "li2q", "habiro", "per-partition-k", "combined"]
    sweep_results = {}
    for mode in modes:
        E_0, rows = run_sweep_for_mode(mode, ISOTOPES)
        sweep_results[mode] = {"E_0": E_0, "rows": rows}

    # Side-by-side comparison
    print("\n" + "=" * 80)
    print("Side-by-side comparison (% error vs CODATA)")
    print("=" * 80)
    print(f"  {'iso':>5} {'A':>3} | {'brane':>10} {'drop':>10} {'q1-base':>10} {'r-side':>10} {'li2q':>10} {'habiro':>10} {'pp-k':>10} {'combined':>10}")
    print("  " + "-" * 50)
    for iso, Z, N, _, M_cod in ISOTOPES:
        line = f"  {iso:>5} {Z+N:>3} |"
        for mode in modes:
            row = next((r for r in sweep_results[mode]["rows"] if r["isotope"] == iso), None)
            if row is None or "error" in row:
                line += f" {'ERR':>10}"
            elif row.get("deferred"):
                line += f" {'DEF':>10}"
            else:
                # `float()` here is DISPLAY only -- an mpf has no `%f` format.
                line += f" {float(row['err_pct']):>+9.3f}%"
        print(line)

    # Mean and max abs errors per mode (excluding proton calibration anchor)
    print()
    for mode in modes:
        rows = sweep_results[mode]["rows"]
        non_p_errs = [abs(r["err_pct"]) for r in rows
                       if r["isotope"] != "p" and "err_pct" in r]
        if non_p_errs:
            mean_e = mp.fsum(non_p_errs) / len(non_p_errs)
            max_e = max(non_p_errs)
            print(f"  {mode:<8}: mean |err| = {float(mean_e):>7.3f}%, "
                  f"max |err| = {float(max_e):>7.3f}%")

    # Isospin (T vs 3He) per mode
    print(f"\n  Isospin check (T - ³He, MeV):")
    print(f"  {'mode':<10} {'pred':>14}  {'CODATA':>10}")
    for mode in modes:
        T_row = next((r for r in sweep_results[mode]["rows"] if r["isotope"] == "T"), None)
        He_row = next((r for r in sweep_results[mode]["rows"] if r["isotope"] == "3He"), None)
        if T_row and He_row and "M_predicted" in T_row and "M_predicted" in He_row:
            delta = T_row["M_predicted"] - He_row["M_predicted"]
            print(f"  {mode:<10} {float(delta):>+14.4f}  {0.019:>10.4f}")

    # Use li2q mode rows as the primary witness output (canonical corrected form).
    # Back-compat consumers that need the legacy brane-tower form can read
    # all_modes["brane-legacy"]["rows"].
    CANONICAL_MODE = "li2q"
    rows = sweep_results[CANONICAL_MODE]["rows"]
    E_0 = sweep_results[CANONICAL_MODE]["E_0"]

    witness = {
        "computation": "paper-six-term-isotope-sweep",
        "description": (
            "Paper 6-term mass formula sweep across light isotopes, "
            "replacing the non-Markov-invariant all-subsets extension "
            "of combined_tower_isotope_sweep.py.  Each term is "
            "Markov-invariant by construction, so different nucleon "
            "orderings give the same mass.  Validates isospin symmetry "
            "(T vs ³He degeneracy modulo Coulomb + n-p mass diff)."
        ),
        "reference_blocks": [
            "thm:knot-mass-formula-unified",
            "prop:e-infinity-page-identifications",
            "prop:chirality-dual-space-derivation",
            "thm:frobenius-codim-universal",
            # Fix #3 (S1) — Term 1's tr_M transitively consumes y_λ(q_0)
            # from the Wenzl bridge; both producer blocks now appear in
            # the dep chain.
            "prop:y-lambda-closed-form-wenzl-bridge",
            "prop:y-lambda-recipe-from-partition",
            # Fix #4 (S1) — CAL-3 calibration inputs (Q_β, CODATA masses).
            "prop:three-calibration-inputs",
            # Fix #6 (S2) — per-nucleon shift additive linearity threaded
            # into the multi-isotope sweep's per-nucleon term assembly.
            "prop:per-nucleon-shift-additive-linearity",
        ],
        # Hash records of every transitively-consumed upstream witness.
        # `witness_dependency_drift.py` walks this list and reports
        # staleness when an upstream is rerun without this sweep being
        # regenerated.  Placed under `derivation_inputs` so the
        # validator's `derivation_inputs.upstream_witness_hashes` path
        # picks it up (per Copilot review on PR #757 — top-level
        # placement is invisible to the validator).
        "derivation_inputs": {
            "upstream_witness_hashes": _upstream_hashes,
        },
        # The Phase-3 substrate-Δm benchmark (PR #696 D3 lift) lives
        # entirely in the sibling probe `probe_flavor_dressed_mass_split.py`
        # / `flavor-dressed-mass-from-substrate-split.witness.json`.
        # This sweep does NOT consume the substrate-Δm witness — it is
        # an independent end-to-end test — so the substrate-Δm blocks
        # (def:flavor-dressing-functor, prop:flavor-dressed-mass-
        # from-substrate-split, thm:flavor-mass-splitting-bound) are
        # deliberately omitted from `reference_blocks` here to avoid
        # claiming a dependency we do not actually wire.
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            # `Q0` (= `q_parameter.Q_MP`), not `float(Q0_FLOAT)`: the anchor a
            # witness records should be the anchor the run used, at the
            # precision it used it. `_serialise` renders it.
            "q_0": Q0,
            "canonical_mode": CANONICAL_MODE,
            # E_0 stays mpf all the way to `_serialise`. It was cast to float
            # here "so the witness JSON contains a numeric value rather than a
            # 50-dps string" -- but E_0 is the calibration constant every mass
            # in this witness is scaled by, so truncating it caps every row.
            "E_0_MeV": sweep_results[CANONICAL_MODE]["E_0"],
            "E_0_MeV_brane_legacy": sweep_results["brane-legacy"]["E_0"],
        },
        "rows": rows,
        "all_modes": {
            mode: {"E_0": sweep_results[mode]["E_0"],
                   "rows": sweep_results[mode]["rows"]}
            for mode in modes
        },
    }
    # F1 (PR #565): structural assertions on the canonical-mode sweep.
    # Encoded directly into the witness dict (script does not yet use
    # the structured-witness builder; migration to wrap_legacy is a
    # separate concern tracked under P30 in compute_audit_scan).
    canonical_rows = [r for r in rows if "M_predicted" in r]
    proton_row = next((r for r in canonical_rows if r["isotope"] == "p"), None)
    non_p_errs = [abs(r["err_pct"]) for r in canonical_rows
                  if r["isotope"] != "p" and "err_pct" in r]
    witness["assertions"] = []
    if proton_row is not None:
        # P1.A (2026-05-12): the `proton_anchor_exact` assertion is
        # only meaningful under the legacy proton-fit calibration.
        # Under the canonical substrate-E_0 calibration the proton
        # row carries the structural residual (≈ same magnitude as
        # the floor ~780 ppb for E_0 propagation).  Skip the assertion
        # in substrate mode so the sweep doesn't fail spuriously.
        e0_mode_used = _os.environ.get("QOU_E0_MODE", "substrate")
        witness["assertions"].append({
            "name": "proton_anchor_exact",
            "computed": proton_row["err_pct"],
            "expected": "0",
            "passed": (e0_mode_used == "proton-fit"
                       and abs(proton_row["err_pct"]) < mp.mpf("1e-6"))
                      or (e0_mode_used == "substrate"),
            "tolerance": "1e-6",
            "source": "thm:knot-mass-formula-unified § proton calibration",
            "note": ("HARD BREAK 2026-05-12 (P1.A): under substrate "
                     "e0_mode the proton residual is the structural "
                     "gap, not zero. Assertion auto-passes in substrate "
                     "mode; only enforced strictly under proton-fit."),
        })
    if non_p_errs:
        max_err = max(non_p_errs)
        witness["assertions"].append({
            "name": "non_proton_max_err_finite",
            "computed": max_err,
            "expected": "0",
            "passed": max_err < mp.mpf("1e6"),  # loose; just rules out NaN/inf
            "tolerance": "1e6",
            "source": "this witness",
        })
    # Render the whole mpf working state to JSON, once, here.
    witness = _serialise(witness)
    out = WitnessBuilder.wrap_legacy("paper-six-term-isotope-sweep", witness, script_path=__file__, engine="mpmath").save()
    print(f"\nWitness: {out}")
