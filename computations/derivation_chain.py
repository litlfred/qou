#!/usr/bin/env python3
# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Derivation-chain registry — every numerical claim must trace back
to first principles step by step.

Per the QOU methodology directive (post-PR-#472): existing
computational scripts are **not** trusted by default.  Every
numerical value used in the paper must declare a `DerivationChain`
that walks step-by-step from one of the seven first-principles
entrypoints down to the final value, with explicit:

  - **jet order** at each step (jet-k reduction of the underlying
    object),
  - **GB filtration level** (`J^ℓ / J^{ℓ+1}` stratum), and
  - **spectral stratum** (which residue / cyclotomic root, if any).

Every step also declares its **trust basis**: how do we know the
step is valid?  The seven first-principles entrypoints are
`axiom`-trust; downstream steps must be `lean-proven`,
`mathlib-cited`, `script-cited` (existing computation, marked but
not yet derived), or `derived` (this chain itself).

The validator performs structural and trust-basis checks, and
validates selected computational claims where explicit evaluators
are implemented (currently the COMPUTATIONAL leaf and a small set
of recognised algebraic patterns such as `c_q = 1/(q-1)`).  It
does NOT, in general, re-evaluate every declared step operation —
that would require either a Lean-kernel-style symbolic engine or
domain-specific evaluators per first-principles entrypoint.

Schema is JSON-serializable so chains can be stored alongside
witnesses (`*.derivation.json`) and rebuilt incrementally.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import enum
import json
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Optional, Union


# ── Shared constants ───────────────────────────────────────────

# Canonical substrate parameter — imported from q_parameter (the single
# source of truth; proton-pinned per the #1422 re-pin).  Other modules
# may import `Q_0` from here for back-compat; new code should import
# from q_parameter directly.
from q_parameter import Q as Q_0  # noqa: E402

# Canonical atom-target Markov-trace values at q_0 — match the
# committed `*-tr-M-q0.derivation.json` leaf values exactly.  Per
# Copilot review on #473: re-running any builder must produce
# bit-stable JSON, so the literals must be the single source of
# truth.  Other modules import these rather than redefining.
#
# Canonical Wenzl-bridge convention (PR #612): values match
# `cross-check-trM-1ppb.witness.json` (1 ppb canonical 50-dps
# reducer) and `markov_peel.tr_M_atomic` (production canonical
# Markov trace).  The legacy 2-variable Schur convention was
# deprecated per `docs/audits/2026-05-08-p3-h-3a-divergence.md`
# (it vanished for partitions with > 2 rows, dropping the sign-rep
# contribution).
#
# RESOLVED 2026-05-29 (#1422, decision A'):
# The 2026-05-11 escalation framed three τ_M values as a "conflation"
# of conventions (Jones-Markov vs Schur-Weyl).  Re-reading the audit
# doc itself, the from_scratch number 1.7339 is reported "from the
# single-component FREE-PROTON braid, not the 11-crossing canonical
# recipe" — i.e. it is tr_M of a DIFFERENT braid, not a different
# convention of the same braid.  The values below are the canonical
# Jones-Markov tr_M of the 11-crossing canonical braid at the
# proton-pinned q₀:
#
#   p = 1.1457596924573009  n = 0.9877436881158096  D = 0.5751722439177719
#
# Four independent production methods (`atomic_tr_m_mpfr_50dps`
# Hoefsmit, `markov_peel`, chi-cache combiner, Habiro `a_m` integer
# coefficients) were reported to derive these to ≤ 2e-15 at 50 dps. That
# agreement was established for the CONVENTION-C values these entries used to
# hold and has NOT been re-established for the convention-D values now here
# (2026-08-30, bean qou-46ab) — do not cite it as current cross-validation. The Lean theorem
# `qou_markov_trace_is_jones_markov`
# (`folio/quantum-observable-universe/mass-theory/markov-trace-frobenius-selection.lean`,
# sorry-free, axiomatising Wenzl / Jones Markov-trace uniqueness via a
# `MarkovTraceUniqueness` class) proves τ_M is *the* unique
# non-degenerate Frobenius form on H_n(q).  `from_scratch/` (different
# braid) is deprecated for production — kept as pedagogy, not
# re-pursued.  τ_SW (Schur–Weyl) and its supporting Lean theorems were
# fully purged 2026-05-29 per #1422 (decision A' uniqueness refactor;
# see `docs/uniqueness-theorems-backlog.md`).
#
# Audit: `docs/audits/2026-05-11-why-individual-mass-residuals-fit-not-derive.md`
# §"Resolution 2026-05-29".
# CONVENTION FIX (2026-08-30, bean qou-46ab). These were CONVENTION C.
# `p` matched the C-frame value to 3.3e-20 — i.e. exactly, proved by
# `audits/he4_witness_convention_attribution_probe.py` — while convention D
# has been canonical since the owner ruling of 2026-08-15.
#
# `D` (deuteron) was ALSO WRONG IN A SECOND, SEPARATE WAY and that is worth
# keeping: it matched neither convention. It sat 1.82e-4 from the C-frame
# deuteron (0.3883571887237810073, computed from `chi-deuteron-h6.witness.json`)
# and 0.325 from the D-frame one. So it was not simply a C-era value; it had an
# additional ~2e-4 discrepancy of unestablished origin on top of the convention.
# Replacing it with the D value fixes the convention and removes that anomaly
# in the same stroke — but the anomaly is NOT explained, only superseded.
# ══════════════════════════════════════════════════════════════════════════
# ⚠ GROUPED-ERA. THIS REGISTRY IS ONE ORDERING RULING BEHIND CANON.
#
# MEASURED 2026-09-13 (bean `qou-4383`), not inferred. Every entry below, and
# every entry of TR_M_AT_Q0_50DPS, reproduces to 50 significant digits when
# `atom_braid_word_3A` is forced to `intra_order="grouped"`. Under the
# canonical `borromean` word — the 2026-09-05 owner ruling, bean `qou-hu1f` —
# the same computation gives
#
#     p  0.62932840220292191816534574677848592760021940063436
#     n  0.47513351715568221250609023267500579955840763470875
#     D  0.15196833920423160759266569775106614127124096465527
#
# i.e. the proton entry is 82 % high and the neutron 108 % high.
#
# DELIBERATELY NOT CHANGED HERE. `trm_proton_five_values_census.py` (bean
# `qou-soj6`) settled the policy for this exact constant: "TR_M_AT_Q0 feeds
# live producers, so correcting it moves published numbers and is its own
# tranche." Twelve live modules import it (outside `_deprecated`):
# applied_uniqueness_mass_table, audits/canonical_a_k_magnitude_audit,
# audits/derivation_convention_frame_audit, the deuteron and neutron
# build_markov_trace_assembly chains, build_proton_mass_50dps_chain,
# build_six_term_substrate_model_b, canonical_derivation_pipeline_compliance,
# markov/assembly_chain_11_letter_recompute_probe,
# phase5/phase2_proton_m_e_hecke_diagnostic, probes/graded_hecke_energy_probe
# and the census itself. Flipping three numbers here moves all of them at once,
# which is a tranche with an owner call in it, not a sweep.
#
# HISTORY WORTH KNOWING BEFORE YOU DO FLIP IT. This registry has already been
# corrected once and went stale again five days later: `qou-soj6` found it
# holding 1.6331535640480814 (the convention-C / muon-pin value, 13.33 % off),
# and the fix landed the then-canonical grouped value — which the 2026-09-05
# ruling superseded. So the failure mode here is not "nobody looked"; it is
# that a hardcoded constant does not track a ruling. Prefer
# `canonical_trm_reference.tr_m_nucleon()` — but read the correction below
# before trusting that advice, because as first written here it was wrong.
#
# ⚠ CORRECTION, same day. This said `canonical_trm_reference` "selects by
# recorded q0 and cannot silently serve the wrong frame". The first half is
# true; the second was FALSE AS DEPLOYED, and measurably so — the module was
# itself returning the GROUPED values for all five atoms. It selects by PIN and
# has no notion of the intra-nucleon ordering at all, so it guards a cross-pin
# read while being blind to exactly the frame at issue here.
#
# The cause was its input, not its logic: it reads
# `atomic-tr-m-mpfr-50dps-proton.witness.json`, dated 2026-08-19 and therefore
# pre-ruling. Note why this went unseen — the CANONICAL-pin witness was the
# stale one (proton, 2026-08-19) while the RETIRED-pin witness was fresh (muon,
# 2026-09-07). Regenerated 2026-09-13 with
#
#     QOU_Q0_ANCHOR=proton python3 computations/atomic_tr_m_mpfr_50dps.py \
#         --anchor proton
#
# after which the module serves the canonical values listed above; the
# producer's own bridge-vs-peel cross-check agrees to 4.3e-51.
#
# So the advice holds NOW and did not before. One gap remains, unfixed:
# `canonical_trm_reference` validates the pin and not the ordering, so a future
# ruling can stale it again just as silently. An ordering assertion there is
# the durable version of this recommendation.
# ══════════════════════════════════════════════════════════════════════════
# NOW A LIVE VIEW, NOT A FROZEN COPY (bean qou-4383, 2026-09-13).
# Both registries are served lazily by the module `__getattr__` at the bottom
# of this file, reading `canonical_trm_reference`. The literals that stood here
# are recorded in that function; do not restore them.
_TR_M_KEYS = ("p", "n", "D")

# ── 50-dps decimal-string companion to TR_M_AT_Q0 ──────────────────
# The float-typed registry above is preserved bit-for-bit (per the
# bit-stable JSON requirement on #473) but is float64-limited (~15-17
# digits).  Per gemini review on PR #640 (line 93): callers needing
# the full 50-dps precision claimed by the "50dps derivation chain"
# objective should consume these decimal strings via
# `mp.mpf(TR_M_AT_Q0_50DPS["p"])`.  Source: atomic-tr-m-mpfr-50dps.witness.json
# (1ppb canonical 50-dps reducer) and markov_peel.tr_M_atomic (the
# production canonical Markov trace).
# Convention D, at the PROTON pin, read from
# `atomic-tr-m-mpfr-50dps-proton.witness.json`. Prefer
# `canonical_trm_reference.tr_m_nucleon()` in new code — it selects the witness
# by its own recorded q0 and so cannot silently serve the other LAYER. It can
# still serve the wrong ORDERING, which it did until 2026-09-13; see the
# correction above the float registry.
# TR_M_AT_Q0_50DPS is served by the same lazy accessor. See the bottom of this
# file. Callers wanting full precision still do `mp.mpf(TR_M_AT_Q0_50DPS["p"])`;
# the strings now come from the witness rather than from a literal.

# Default Model B (SDP-canonical low-strand) τ_M values at q_0 ───────
# Per owner directive 2026-05-11 ("migrate all compute to default B").
#
# Model B uses the canonical hyperbolic knot for each isotope in the
# minimum-strand braid group:
#
#   p, n : 11-crossing typed B_3 braid (operator-valued, with σ/σ^{-1}
#          /averaged crossings encoding quark composition uud / udd);
#          ρ = 1; canonical via atomic-braid-recipe-{p,n}.derivation.json.
#          At A = 1, Model A and Model B converge (both use B_3 with
#          typed crossings — there's no lower-strand braid).  Value
#          source: canonical Wenzl-bridge τ_M via markov_peel.tr_M_atomic
#          (same as TR_M_AT_Q0 above).
#   D    : 6_2     in B_3,  ρ = 1, braid = [1, -2, 1, 1, 1, -2]
#   T    : 8_11    in B_5,  ρ = 2, braid = [-1, 2, -3, 2, 1, -3, -3,
#                                            4, -3, -2, -3, -4, -3, 2]
#   ³He  : L6a4    in B_3,  ρ = 2, braid = [-1, 2, -1, 2, -1, 2]
#                                  (= bare Borromean β_Bor)
#   ⁴He  : open Model B canonical knot (12-strand atomic-braid-recipe-4he
#          is the Model A 3A-strand encoding, not a low-strand knot).
#
# Source of truth for D, T, ³He: probe-sdp-canonical-paper-formula.witness.json.
# Source of truth for p, n:      atomic-braid-recipe-{p,n}.derivation.json
#                                (= Wenzl-bridge τ_M, identical to Model A
#                                at A=1).
#
# n_canon (strand count of the canonical braid):
#   p, n: 3, D: 3, T: 5, ³He: 3, ⁴He: open
_TR_M_CANONICAL_B_KNOT_ROWS: dict[str, float] = {
    # CONVENTION FIX (2026-08-30, bean qou-46ab). `p` and `n` were the
    # convention-C values, and this dict's OWN comment above is why they had to
    # move with the Model A ones: it states that at A = 1 the two models
    # converge and that the source is "the same as TR_M_AT_Q0 above". They are
    # the same quantity, so leaving these at C while fixing that one would have
    # split a documented identity.
    #
    # D / T / 3He are NOT touched here. They are SDP-canonical low-strand knots
    # (6_2, 8_11, L6a4) — different quantities, not this trace under another
    # convention — and they already carry their own "#1422-recompute pending"
    # marker. Changing them would need those recomputes, not a substitution.
    # SECOND ORDERING FIX (2026-09-13, bean qou-4383). `p` and `n` were still
    # the GROUPED values, for the same reason and by the same argument the
    # convention-C note above gives: this dict's own comment says that at A = 1
    # the two models converge and the source is "the same as TR_M_AT_Q0 above",
    # so the two must move together or a documented identity splits. They are
    # now served by the same lazy accessor at the bottom of this file, reading
    # `canonical_trm_reference`.
    #
    # D / T / 3He STAY LITERAL, and that is not an oversight — the note above
    # is explicit that they are SDP-canonical low-strand knots (6_2, 8_11,
    # L6a4), a DIFFERENT QUANTITY from this trace under another convention.
    # Substituting a nucleon |tr_M| for a knot invariant would be a category
    # error dressed as a frame fix.
    "D":   0.288326,            # knot 6_2, SDP-canonical  (#1422-recompute pending)
    "T":   0.012889,            # knot 8_11, SDP-canonical (H_5)  (#1422-recompute pending)
    "3He": 0.998367,            # L6a4 = β_Bor (the bare Borromean)  (#1422-recompute pending)
}

# Per-isotope Model B canonical-braid metadata (knot, strand count,
# topological prefactor ρ).
#
# 🛑 THE DEUTERON ROW CARRIES A RETIRED ASSIGNMENT (flagged 2026-08-30, bean
# `qou-imkb`). `"D": {"knot": "6_2", ...}` below is the option the owner
# REJECTED on 2026-08-29: the ruling
# (docs/audits/2026-08-29-deuteron-knot-owner-decision.md, bean `qou-e5jf`) is
# that the deuteron knot is the CANONICAL BRAID CLOSURE (trefoil / Hopf,
# Vol = 0), and that "the 6_2 census assignment is retired as a bare lookup".
# Option B put to the owner was literally "the deuteron knot is 6_2
# (Vol = 4.40)" — so this is a ruling about the KNOT IDENTITY, not only about
# whether the binding is a volume term.
#
# This is the SECOND live site for that retired assignment; the first is
# `build_six_term_substrate_model_b.py::MODEL_B_BRAID_REGISTRY[(1,1)]`, and the
# `TR_M_CANONICAL_B_AT_Q0["D"] = 0.288326` entry above is a THIRD (a value
# derived from the retired knot, already marked "#1422-recompute pending").
#
# Flagged rather than changed, for the same reason as the other two: choosing
# the replacement is a modelling decision. At A=2 the canonical braid closure is
# the object Model A already uses, so adopting it may collapse Model B's
# deuteron entry into Model A's — and whether that is correct, or whether Model
# B keeps a distinct A=2 object, is not something a comment can settle. Nothing
# recomputes from these rows today: the Model B T1 witness has no producer
# (`qou-imkb`), so the whole Model B path raises before reaching them.
MODEL_B_BRAID_META: dict[str, dict] = {
    "p":   {"knot": "11-crossing typed B_3 (uud)", "n_canon": 3, "rho": 1},
    "n":   {"knot": "11-crossing typed B_3 (udd)", "n_canon": 3, "rho": 1},
    "D":   {"knot": "6_2",                         "n_canon": 3, "rho": 1},
    "T":   {"knot": "8_11",                        "n_canon": 5, "rho": 2},
    "3He": {"knot": "L6a4",                        "n_canon": 3, "rho": 2},
    "4He": {"knot": "open (B_12 atomic-recipe is Model A)",
            "n_canon": None, "rho": None},
}

# Atom-target Markov-trace values in cat-units (Hecke-pipeline output)
# at q_0 — partial Path A T1+T4 derivation per Workplan 2 Phase 2
# (`docs/audits/2026-05-10-1ppb-workplan-update.md §Phase 2`).
#
# 2026-05-10 — DEPRECATED-LITERAL → DERIVATION REPLACEMENT
#
# History: the original literals
#     {"e": 0.0007783, "p": 1.4283}
# were marked DEPRECATED 2026-05-09 (per
# `docs/audits/2026-05-09-proton-m_e-anomaly.md §9`). Their ratio
# 1.4283/0.0007783 = 1835.15 sits at CODATA `(m_p − m_e)/m_e`, not
# `m_p/m_e` — a 472 ppb numerological tuning whose origin is
# unattributable (no committed computation produces those values).
#
# Per owner directive 2026-05-10 ("do workplans 2 phase 2. make sure
# no fitting. all should be derived"), this dict now consumes the
# **partial Path A T1+T4 derivation** from the trustable subset of
# the six-term unified mass formula:
#
#   * `derive_m_p_hecke_path_a.m_p_hecke_path_a_at_q0()`
#     → reads T1 (descended Markov trace) + T4 (Frobenius co-Casimir
#       per-vortex) for the proton at H_3 from
#       `mass-formula-6term-mpfr-50dps.witness.json`.
#
#   * `derive_m_e_hecke_path_a.m_e_hecke_path_a_cat_units_at_q0()`
#     → closed-form construction at H_2 (electron is the identity
#       2-strand braid) from CAL-1 m_e + CAL-2 q_0 alone.
#
# T2/T3/T5/T6 are quarantined per the Phase 2 diagnostic finding
# (A=1 brane tower structurally empty; T5 sign-indefinite; T6
# small Habiro tail). The resulting predicted m_p will be **wildly
# off CODATA** (~0.6 MeV vs 938 MeV) — that residual is what
# Phase 2 EXPOSES, not what it tries to fit. Closing the residual
# is the work of Phase 3+ (T2/T3 brane-tower closure via the
# z-Habiro level-selection rule, T5 chirality-BW sign resolution,
# T6 Habiro-tail integration).
#
# DO NOT ADD ALGEBRAIC +1 OR ANY OTHER TUNING TO MAKE THE NUMBERS
# MATCH. The honest residual is the deliverable.

def _path_a_at_q0() -> dict[str, "mp.mpf"]:
    """Lazy resolver — calls derive_m_{p,n,e}_hecke_path_a on first use.

    Lazy because (a) we don't want to import-time read JSON witnesses
    on every consumer, and (b) audit-only scripts that consume the
    DEPRECATED legacy dict (e.g. proton_m_e_anomaly_audit.py) need
    the legacy values for their "expose-the-anomaly" purpose; they
    use M_HECKE_PIPELINE_AT_Q0_LEGACY directly.
    """
    # Local import so derivation_chain.py stays import-light.
    from derive_m_p_hecke_path_a import m_p_hecke_path_a_at_q0
    from derive_m_n_hecke_path_a import m_n_hecke_path_a_at_q0
    from derive_m_e_hecke_path_a import m_e_hecke_path_a_cat_units_at_q0
    # Keep the values as mp.mpf to preserve 50-dps precision per the
    # no-float64 directive. Legacy float-typed consumers can still
    # `float(M_HECKE_PIPELINE_AT_Q0["p"])` if they need a Python float.
    return {
        "p": m_p_hecke_path_a_at_q0(),
        "n": m_n_hecke_path_a_at_q0(),
        "e": m_e_hecke_path_a_cat_units_at_q0(),
    }


# Legacy DEPRECATED placeholder values — kept for audit-only scripts
# that document the pre-Phase-2 anomaly. Production consumers use
# M_HECKE_PIPELINE_AT_Q0 (the dict below), which now returns derived
# values.
M_HECKE_PIPELINE_AT_Q0_LEGACY: dict[str, float] = {
    "e": 0.0007783,  # numerological placeholder (audit only)
    "p": 1.4283,     # numerological placeholder (audit only)
}


# Production dict — populated lazily on first attribute read.
class _PathADict(dict):
    """Dict that resolves Path A values lazily on first key lookup."""
    _resolved = False

    def _resolve(self):
        if not self._resolved:
            self.clear()
            self.update(_path_a_at_q0())
            self._resolved = True

    def __getitem__(self, key):
        self._resolve()
        return super().__getitem__(key)

    def get(self, key, default=None):
        self._resolve()
        return super().get(key, default)

    def __contains__(self, key):
        self._resolve()
        return super().__contains__(key)

    def __iter__(self):
        self._resolve()
        return super().__iter__()

    def __len__(self):
        self._resolve()
        return super().__len__()

    def __repr__(self):
        self._resolve()
        return super().__repr__()

    def items(self):
        self._resolve()
        return super().items()

    def keys(self):
        self._resolve()
        return super().keys()

    def values(self):
        self._resolve()
        return super().values()


M_HECKE_PIPELINE_AT_Q0: dict[str, mp.mpf] = _PathADict()


# ── E_0 conventions registry ───────────────────────────────────
#
# Per `docs/audits/2026-05-10-hbar-q-scaling-audit.md` finding:
# THREE distinct E_0 conventions co-exist in folio-assistant/
# computations/, each correct for a specific operator class. Each
# carries its own ℏ_q scaling. Conflating them at consumer sites
# silently double-counts or omits ℏ_q factors.
#
# This registry surfaces the convention choice at every consumer
# site. Each entry documents:
#   * value_MeV   — numerical E_0 at q_0
#   * scaling     — ℏ_q power signature (×ℏ_q^k for k an integer)
#   * derivation  — how it's structurally derived
#   * operator_class — which knot operators it correctly scales
#   * canonical_for — which consumer chain treats this as primary
#
# The framework's structurally-canonical derivation is the LP-dual
# shadow price y_0^* of the net constraint in
# `prop:operator-selection-lp` (strong duality:
# Σ t_i x_i^* = n_target · y_0^*). All three conventions below are
# expected to agree at leading order via LP-duality; the differences
# capture different operator scales / brane-tower depths.

E_0_CONVENTIONS: dict[str, dict] = {
    "A_single_hecke_tick": {
        "value_MeV": "m_e / (q_0 (q_0 - 1)) ≈ 4.186 MeV",
        "scaling": "ℏ_q^1 (× m_e c_q^2)",
        "hecke_level": "H_3 (single-nucleon, d = 6 NF basis)",
        "strand_count": "3",
        "derivation": (
            "Closed-form algebraic substitution from CAL-1 m_e + "
            "CAL-2 q_0. Single-Hecke-reduction-step cost per "
            "`prop:beta-decay-energy-scale` / `rem:energy-scale-planck`. "
            "Conjecturally equivalent to the LP-dual y_0^* · m_e at "
            "the appropriate normalization; the existing direct LP-dual "
            "probe at H_3 (derive_e_0_lp_dual_h3.py) reports y_0^* "
            "DIMENSIONLESS, far from 4.186 MeV — so the MeV scale of "
            "E_0 still comes from CAL-1 + CAL-2 outside the LP, not "
            "from the LP dual directly. See convention D below."
        ),
        "operator_class": (
            "β-decay single-wrap Δ_NF = (h^2/2)γ - (h/2)σ_0 - (h/2)σ_1 "
            "in H_3(q). Δ(net) = h(h-2)/2 with h = q - q^{-1}."
        ),
        "canonical_for": [
            "derived_masses.e_0_full_mev",
            "q_beta_predicted.py",
            "prop:neutron-qvalue-symbolic",
        ],
        "validity": (
            "Q_β prediction within 0.168% / 1.31 keV of CODATA "
            "(commit 4649650f). Residual sits inside the structural "
            "ℏ_q^{2(N+1)} bound at N=0 per `per-braid-mass-tower.md`."
        ),
    },
    "B_q_value_absorbed": {
        "value_MeV": "Q_β^CODATA ≈ 0.7823 MeV",
        "scaling": "ℏ_q^0 (|Δ(net)| = 1 implicit; ℏ_q^2 absorbed into the calibration)",
        "hecke_level": "H_{3A} (atom-level: H_6 D, H_9 T/³He, H_12 ⁴He)",
        "strand_count": "3·A (whole atom braid)",
        "derivation": (
            "Calibration to CAL-3 P_avg^π(n) directly. Sets the operator "
            "Δ_NF ≡ 1 in cat-units; canonical for "
            "`hecke_core._canon` style chains where the operator "
            "difference |tr_M(W_free)| - |tr_M(W_atom)| is "
            "dimensionless and carries its own ℏ_q powers."
        ),
        "operator_class": (
            "Atom-level binding B(Z, N) = E_0 · (|tr_M(W_free)| - "
            "|tr_M(W_atom)|) at H_{3A}. The trace-difference operator "
            "carries the ℏ_q^2 scaling; E_0 is the unit-action scale."
            "\n\n"
            "⚠ CORRECTED 2026-08-31 (bean `qou-zrx2`). MEASURED, the "
            "trace-difference operator carries NEITHER an ℏ_q^2 leading "
            "term NOR a vanishing classical limit. Swept along q = exp(η) "
            "over four decades it is\n"
            "    tr_M(W_free) − tr_M(W_atom) = c₀(A) + c₁·ℏ_q + O(ℏ_q²)\n"
            "with c₀(A) = 2^{-A} − 2^{1-2A} for m=1 (and more generally "
            "c₀(A, O) = 2^{-A}(1 − 2^{-O}) with O odd-multiplicity "
            "inter-nucleon interfaces, vanishing at O = 0), DERIVED "
            "(Schur–Weyl at q = 1 gives tr_M = 2^{c(σ)−n}, and the m=1 braid "
            "words have c_free = 2A, c_atom = A+1 for A = 2..20). So the "
            "operator is ℏ_q^0 + ℏ_q^1, not ℏ_q^2. At q₀ on the canonical "
            "Borromean word (`intra_order='borromean'`, owner ruling "
            "`qou-92u9`) the ℏ_q^0 floor is 85.01 % of the deuteron value "
            "(0.125 / 0.14704668) and 9.61 % of ⁴He's (0.0546875 / "
            "0.56898916); on the historical pre-2026-09-05 grouped word it "
            "was 22.46 % at D and 4.88 % at ⁴He. See "
            "computations/probes/classical_floor_derivation_probe.py, "
            "QOU/MassTheory/ClassicalTraceFloor.lean, and "
            "QOU/MassTheory/ClassicalTraceFloorParity.lean (sorry-free).\n\n"
            "CONSEQUENCE, and it points the other way from `validity` below: "
            "subtract the floor and Δtr − c₀(A) is a pure ℏ_q^1 observable, "
            "which pairs with convention **A** (ℏ_q^1) to total ℏ_q^2 — the "
            "same bookkeeping as Δ(net) × A, which predicts Q_β to 0.168 %. "
            "So on ℏ_q grounds the corrected atom-level observable takes A, "
            "not B. Before the subtraction NO convention paired consistently, "
            "because the operator's two parts sat at different orders. "
            "Recorded as a measured fact; re-designating the canonical "
            "convention is an owner decision and is NOT taken here."
        ),
        "canonical_for": [
            "hecke_core.E_0_CALIBRATION_MEV (line 2922)",
            "canonical_tower.py (lines 446-528)",
            "hecke_characters.py (line 39)",
            "mass_at_3A_proper.py (line 676)",
            "adjacent_vs_full_probe.py (line 46)",
        ],
        "validity": (
            "Phase 3+ Triton / ³He / ⁴He binding MUST use this "
            "convention. Naively using convention A with a Δ(net)-"
            "style operator difference would miss the 1/ℏ_q^2 factor "
            "(≈ 102× error)."
            "\n\n"
            "⚠ THE ≈102× WARNING CANNOT BE RECOMPUTED AS STATED (2026-08-31, "
            "bean `qou-zrx2`). 1/ℏ_q² = 101.862 is arithmetically right, but "
            "its premise — that this operator class is ℏ_q^2 — is measured "
            "false (see `operator_class`). The mismatch between using A and "
            "using B on the SAME trace difference is the scale ratio "
            "E_0^A/E_0^B = 5.35, not 102, and two live producers currently "
            "differ by exactly that: binding_canonical uses B (deuteron "
            "0.4354 MeV) while derive_binding_chain_cooperative uses A "
            "(2.3297 MeV). The 'MUST use B' rule above therefore rests on a "
            "wrong index and cannot adjudicate them. Not resolved here — "
            "picking the convention that lands closer to AME is the fit this "
            "lane has withdrawn three times."
        ),
    },
    "C_proton_back_fit": {
        "value_MeV": "(M_p^CODATA - t_6(p)) / total_hecke(p) ≈ 200 MeV",
        "scaling": "ℏ_q^? (calibrated, not derived)",
        "hecke_level": "H_{3A} (atom-level T1+T2+T3+T4 sum)",
        "strand_count": "3·A",
        "derivation": (
            "Back-fit to CODATA m_p via "
            "`atomic_braid_mass_table.py:441`. NOT a structural "
            "derivation. Flagged as 4th-calibration violation under "
            "Workplan 0b §5. To be replaced by LP-dual shadow-price "
            "scheme of `prop:operator-selection-lp`."
        ),
        "operator_class": (
            "Strategy-3 multi-term atomic mass assembly "
            "(T1+T2+T3+T4 cat-units → MeV via E_0 back-fit)."
        ),
        "canonical_for": ["atomic_braid_mass_table.py"],
        "validity": (
            "⚠️ DISCIPLINE VIOLATION. Do not consume in new "
            "production chains; use convention B instead."
        ),
    },
    "D_lp_dual_decomposition": {
        "value_MeV": (
            "N/A — y_0^* is DIMENSIONLESS (cat-units). LP-dual is a "
            "structural decomposition tool, NOT an E_0 derivation."
        ),
        "scaling": "n/a (dimensionless; MeV scale is external)",
        "hecke_level": (
            "Either H_3 (β-decay, d=6 — tractable; LP solved in "
            "derive_e_0_lp_dual_h3.py) OR H_{3A} (atom binding: H_6 D "
            "d=720 tractable; H_9 T/³He d=362880 requires per-"
            "Wedderburn-block reduction; H_12 ⁴He d=4.79e8 requires "
            "Rust kernel per `prop:atomic-tr-m-canonical`)"
        ),
        "strand_count": "3 (β-decay) or 3·A (atom binding)",
        "derivation": (
            "Per `prop:operator-selection-lp` strong duality: "
            "Σ t_i x_i^* = n_target · y_0^*. y_0^* is the marginal "
            "*action* per unit target net — DIMENSIONLESS in "
            "cat-units. NEGATIVE FINDING 2026-05-10 "
            "(derive_e_0_lp_dual_h3.py): y_0^* · m_e ≠ E_0_MeV. "
            "For n_target=1, the LP picks x*=(0,...,0,1) (pure e^- "
            "channel) with y_0^* = 0.1245, giving 0.064 MeV — not "
            "the 4.186 MeV of convention A. The MeV scale must "
            "come from OUTSIDE the LP. The LP-dual remains a "
            "valuable DECOMPOSITION tool (active-set identification, "
            "channel shadow prices y_i^*, strong-duality audit), but "
            "is NOT an alternative derivation of E_0 in MeV."
        ),
        "operator_class": "any (universal — Gram + cost vector)",
        "canonical_for": [
            "lp_dual_solver.solve_operator_selection_lp",
            "lp_dual_solver.solve_psd_operator_selection_sdp",
            "derive_e_0_lp_dual_h3.py",
        ],
        "validity": (
            "Wired at H_3 (commit pending). y_0^* recovered for "
            "four substrate-derived n_target choices; all in "
            "cat-units, none MeV-bearing. The structural E_0 in "
            "MeV remains convention A (single-tick m_e c_q^2 ℏ_q). "
            "The 0.17% Q_β residual is NOT closable via LP-dual "
            "alone — closure requires the brane-tower extension of "
            "convention A (Workplan 2+ open R&D)."
        ),
    },
}


def e_0_convention(script_name: str) -> str:
    """Return the convention key (A/B/C/D) that `script_name` consumes.

    Falls back to "unknown" for scripts not yet audited. Useful for
    cross-consistency checks at consumer sites.
    """
    for key, entry in E_0_CONVENTIONS.items():
        if any(script_name in c for c in entry["canonical_for"]):
            return key
    return "unknown"


# Pre-compiled module-level regex for SCRIPT_CITED `notes` validation
# (per Gemini PR #484 review): tolerates leading whitespace after the
# colon AND requires a path-like token ending in a recognisable
# extension (`.py`, `.sh`, …).  Compiled once rather than rebuilt on
# every step check.
_SCRIPT_NOTE_RE = re.compile(r"script:\s*\S+\.\w+", re.IGNORECASE)


# ── First principles ────────────────────────────────────────────

class FirstPrinciple(str, enum.Enum):
    """The seven canonical entrypoints; everything traces back here.

    Each member's value is the canonical Lean / content-block
    reference for that entrypoint.
    """
    HECKE_ENERGY        = "Hecke.Energy"
    CATEGORICAL_ACTION  = "Cat.Action"
    FROBENIUS_PAIRING   = "Frobenius.Pairing"
    NONABELIAN_STOKES   = "Nonabelian.Stokes"
    WEDDERBURN          = "Wedderburn"
    SCHUR               = "Schur"
    FINITE_JONES        = "FiniteJones"


# ── Trust basis ────────────────────────────────────────────────

class TrustBasis(str, enum.Enum):
    """How do we know this step is valid?

    Ordering is roughly strongest → weakest:

      AXIOM            — first-principles entrypoint (the seven canonical refs).
      LEAN_PROVEN      — backed by a Lean theorem with no `sorry`.
      MATHLIB_CITED    — invokes a Mathlib lemma (axiom-checked upstream).
      DERIVED          — proven within this chain by a sequence of LEAN_PROVEN /
                         MATHLIB_CITED / AXIOM steps.
      SCRIPT_CITED     — references an existing computation script; the script
                         itself is currently "computational-only" trust pending
                         its own derivation chain.  Use sparingly.
      COMPUTATIONAL    — bare numerical computation (sympy / mpmath / numpy);
                         only acceptable as the final evaluation step at the
                         leaf of an otherwise fully-trusted chain.
    """
    AXIOM           = "axiom"
    LEAN_PROVEN     = "lean-proven"
    MATHLIB_CITED   = "mathlib-cited"
    DERIVED         = "derived"
    SCRIPT_CITED    = "script-cited"
    COMPUTATIONAL   = "computational"


# ── Step ────────────────────────────────────────────────────────

@dataclass
class DerivationStep:
    """One step in a derivation chain.

    Fields
    ------
    name : str
        Human-readable step label (e.g. "Schur–Weyl decomposition of H_3(q)").
    operation : str
        Mathematical operation applied at this step.
    inputs : list[str]
        Names of upstream `DerivationStep`s OR string-encoded
        `FirstPrinciple` values.  All inputs must be defined earlier
        in the chain.
    output_name : str
        Symbolic name of this step's output (referenced by downstream
        steps).
    output_value : Any
        The actual computed value (number, polynomial string, etc.).
        Verified by the validator.
    jet_order : Optional[int]
        Jet order of the object at this step.  None when the concept
        of jet order doesn't apply.
    gb_filtration_level : Optional[int]
        GB-filtration stratum `J^ℓ / J^{ℓ+1}` (the `ℓ`).  None when
        the step is filtration-independent.
    spectral_stratum : Optional[str]
        Spectral stratum identifier (e.g. "ζ_3", "n=2 cyclotomic").
        None when the step is not spectral.
    trust_basis : TrustBasis
        Declared justification for the step.
    lean_ref : Optional[str]
        Pointer to the Lean declaration that formalises this step,
        in `pkg:Decl.Path` form.  Required when trust_basis is
        LEAN_PROVEN, MATHLIB_CITED, or AXIOM.
    citation : Optional[str]
        Reference key from `folio/schema/references.ts` or
        manuscript label (e.g. "habiro2004", "manuscript:§6.3").
    notes : Optional[str]
        Additional commentary; especially useful to flag SCRIPT_CITED
        steps with the script path + commit.
    """
    name: str
    operation: str
    inputs: list[str]
    output_name: str
    output_value: Any
    trust_basis: TrustBasis
    jet_order: Optional[int] = None
    gb_filtration_level: Optional[int] = None
    spectral_stratum: Optional[str] = None
    lean_ref: Optional[str] = None
    citation: Optional[str] = None
    notes: Optional[str] = None

    def to_dict(self) -> dict:
        d = asdict(self)
        d["trust_basis"] = self.trust_basis.value
        return {k: v for k, v in d.items() if v is not None}


# ── Chain ───────────────────────────────────────────────────────

@dataclass
class DerivationChain:
    """A complete chain of derivation steps for one named claim.

    Fields
    ------
    target : str
        The final claim being derived (e.g. "tr_M(p, q_0)").
    target_value : Any
        The final numerical value being certified.
    target_tolerance : float
        Acceptable relative tolerance when the validator re-walks
        the chain.
    steps : list[DerivationStep]
        Steps in order; each step's `inputs` must reference earlier
        step `output_name`s or `FirstPrinciple` enum values.
    content_block : Optional[str]
        Content block label this chain certifies (e.g.
        "prop:full-pole-structure-mass-trace").
    description : Optional[str]
        Free-form description of the chain's scope.
    """
    target: str
    target_value: Any
    target_tolerance: float
    steps: list[DerivationStep]
    content_block: Optional[str] = None
    description: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "target": self.target,
            "target_value": self.target_value,
            "target_tolerance": self.target_tolerance,
            "content_block": self.content_block,
            "description": self.description,
            "steps": [s.to_dict() for s in self.steps],
        }

    def save(self, path: Union[str, Path]) -> Path:
        p = Path(path)
        with p.open("w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2, ensure_ascii=False)
            f.write("\n")
        return p

    # ── Structural validation ──────────────────────────────────

    def structural_check(self) -> tuple[bool, list[str]]:
        """Verify the chain is well-formed: every step's inputs are
        defined earlier (either as a previous step's output_name or
        as a FirstPrinciple).  Returns (ok, list-of-issues)."""
        defined: set[str] = {fp.value for fp in FirstPrinciple}
        issues: list[str] = []

        for step in self.steps:
            for inp in step.inputs:
                if inp not in defined:
                    issues.append(
                        f"step {step.name!r}: input {inp!r} not defined "
                        "(must be a previous step's output_name or a "
                        "FirstPrinciple value)"
                    )
            # First-principle steps must have AXIOM trust + a lean_ref.
            if step.trust_basis == TrustBasis.AXIOM:
                if step.lean_ref is None:
                    issues.append(
                        f"AXIOM step {step.name!r} must declare lean_ref"
                    )
            # Lean / Mathlib steps must have a lean_ref.
            if step.trust_basis in (TrustBasis.LEAN_PROVEN, TrustBasis.MATHLIB_CITED):
                if step.lean_ref is None:
                    issues.append(
                        f"{step.trust_basis.value} step {step.name!r} "
                        "must declare lean_ref"
                    )
            # SCRIPT_CITED steps should record the script path in notes.
            if step.trust_basis == TrustBasis.SCRIPT_CITED:
                # Accept either `script:` or `Script:` (legacy chains)
                # via the module-level pre-compiled `_SCRIPT_NOTE_RE`.
                if step.notes is None or not _SCRIPT_NOTE_RE.search(step.notes):
                    issues.append(
                        f"SCRIPT_CITED step {step.name!r} should record "
                        "the script path in `notes` (e.g. 'script: foo.py @ <sha>')"
                    )
            # COMPUTATIONAL is the leaf only — numerical eval may not
            # appear in the middle of a chain (per the docstring of
            # TrustBasis.COMPUTATIONAL).  Enforced per Gemini #473.
            if step.trust_basis == TrustBasis.COMPUTATIONAL and step is not self.steps[-1]:
                issues.append(
                    f"COMPUTATIONAL step {step.name!r} is not the leaf; "
                    "numerical evaluation is only permitted as the final step."
                )
            defined.add(step.output_name)

        return (not issues, issues)

    def trust_summary(self) -> dict[str, int]:
        """Count steps by trust basis — a quick read on chain quality."""
        counts: dict[str, int] = {tb.value: 0 for tb in TrustBasis}
        for s in self.steps:
            counts[s.trust_basis.value] += 1
        return counts


# ── Quick sanity test ─────────────────────────────────────────

if __name__ == "__main__":
    # Smoke test: construct a trivial chain and validate it.
    chain = DerivationChain(
        target="trivial-test",
        target_value=42,
        target_tolerance=0.0,
        steps=[
            DerivationStep(
                name="constant 42",
                operation="literal",
                inputs=[FirstPrinciple.HECKE_ENERGY.value],
                output_name="x",
                output_value=42,
                trust_basis=TrustBasis.AXIOM,
                lean_ref="qou:QOU.Test.fortyTwo",
            ),
        ],
        description="smoke test: 42 derived from the Hecke energy axiom",
    )
    ok, issues = chain.structural_check()
    print(f"structural_check: {'OK' if ok else 'FAIL'}")
    for i in issues:
        print(f"  - {i}")
    print(f"trust_summary: {chain.trust_summary()}")


# ══════════════════════════════════════════════════════════════════════════
# LAZY REGISTRY ACCESS (PEP 562). Bean qou-4383, 2026-09-13.
#
# `TR_M_AT_Q0` and `TR_M_AT_Q0_50DPS` used to be literal dicts holding
#
#     p 1.1457596924573009   n 0.9877436881158096   D 0.5751722439177719
#
# in the GROUPED intra-nucleon frame — correct when written, superseded by the
# 2026-09-05 ordering ruling (`qou-hu1f`). Every live consumer was migrated to
# `canonical_trm_reference` earlier today, leaving exactly one importer:
# `build_six_term_substrate_model_b`, which raises FileNotFoundError before the
# line that reads this (bean `qou-imkb`). So the registry had ZERO reachable
# consumers while holding values 82% and 108% off canon — dead weight that a
# future reader would have found and used.
#
# WHY LAZY, and not simply better literals. Typing canonical numbers here would
# reproduce the exact defect this bean exists to close: a hardcoded constant
# cannot track a ruling, and this registry has already gone stale twice (the
# convention-C 1.63315 corrected by `qou-soj6`, then the grouped value the
# ruling superseded five days later). Reading makes it a view.
#
# WHY `__getattr__` AND NOT A MODULE-LEVEL READ. 17 modules import
# `derivation_chain`. A read at import time would make all 17 do file I/O and,
# because `canonical_trm_reference` REFUSES an unstamped or wrong-ordering
# witness (bean `qou-y4gi`), would let a stale witness break every one of them
# at import. PEP 562 defers the cost to actual access, so the 17 importers pay
# nothing and only a module that genuinely asks can be affected.
#
# THE EXISTENCE QUESTION IS STILL OPEN and is deliberately not answered here.
# With no reachable consumers, this may simply want deleting; that is an owner
# call. What this change does is make it harmless either way.
def __getattr__(name: str):
    if name == "TR_M_CANONICAL_B_AT_Q0":
        # Model B at A = 1 is the same quantity as Model A — this dict's own
        # comment says so — so p/n come from the reference while the
        # knot-invariant rows stay as authored. Zero consumers either way
        # (measured 2026-09-13); this exists so the file holds no stale trace.
        base = dict(_TR_M_CANONICAL_B_KNOT_ROWS)
        live = __getattr__("TR_M_AT_Q0")
        base.update({"p": live["p"], "n": live["n"]})
        return base
    if name in ("TR_M_AT_Q0", "TR_M_AT_Q0_50DPS"):
        import sys as _sys
        from pathlib import Path as _Path
        _c = str(_Path(__file__).resolve().parent)
        if _c not in _sys.path:
            _sys.path.insert(0, _c)
        from canonical_trm_reference import tr_m_nucleon   # noqa: PLC0415
        _atom = {"p": "proton", "n": "neutron", "D": "deuteron"}
        vals = {k: tr_m_nucleon(a) for k, a in _atom.items()}
        if name == "TR_M_AT_Q0":
            return {k: float(v) for k, v in vals.items()}
        return {k: str(v) for k, v in vals.items()}
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
