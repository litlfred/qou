#!/usr/bin/env python3
# polynomial_q_not_applicable: derived-quantity module; consumes
# upstream beta-decay-energy-scale witness, exposes predicted MeV
# observables.
"""
**CONTEXT (per prop:li2q-phiq-bar-symmetrization).** This module
predicts both **MASS** observables (m_p, m_n, m_e via β-decay scale)
and **BINDING-derived** quantities (Q_β, isotope binding via mass
differences). Φ_q usage in this script is in the MASS leg (anchor
chain); the binding-energy derivations cancel mass scales at the
output level and inherit Li_2^q via downstream callers. Migration to
Li_2^q would require structural revision per the SUPERSEDED banner
in `mass-endomorphism-tower.md` — tracked under Stage-1 in
`docs/coordination/1ppb-categorical-chain.md`.

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
═══════════════════════════════════════════════════════════════

Framework-derived energy observables for the QOU mass / β-decay
sector.

Predictions come from the **FULL** chain per
[`prop:beta-decay-energy-scale`](../../content/quantum-observable-universe/particle-interactions/beta-decay-energy-scale.md)
and [`prop:meson-to-proton-via-borromean`](../../content/quantum-observable-universe/archimedean-universe/meson-to-proton-via-borromean.md),
NOT from the LO simplification (where |tr_M| cancels exactly between
numerator and denominator of ρ_K^LO and the prediction reduces to
the constituent sum Z·m_p + N·m_n; cf.
`atomic_mass_via_rho_k.py:188-194`). The LO form is structurally
unable to predict binding — it returns CODATA inputs verbatim. Use
the FULL form below.

══════════════════════════════════════════════════════════════════
 FULL CHAIN FOR β-DECAY (Q_β prediction)
══════════════════════════════════════════════════════════════════

The β-decay Q-value is a FRAMEWORK PREDICTION (not a calibration
input) via the symbolic single-wrap closed form:

    Q_β = m_e · |q_0² - 2 q_0 - 1| · (q_0 + 1) / (2 q_0³)
                                                  ≈ 0.7836 MeV
                                              (vs CODATA 0.7823; 0.168% err)

(uses CAL-1 m_e and CAL-2 q_0 only; CAL-3 𝔇_π is the OUTPUT)

The +1.31 keV residual is the brane-tower truncation residual at
N=0; exact tower-summed E_0 closes it (Workplan 2 Phase 2).

LEGACY typed-crossings form (kept for cross-check only):

    E_0 = m_e / (q_0 · (q_0 - 1)) = m_e · c_q² · ℏ_q   ≈ 4.186 MeV
    Q_β = |Δ(net)| · E_0                              ≈ 0.788 MeV
                                                  (vs CODATA 0.78233341; 0.75% err)

with Δ(net) = net(n) - net(p) the difference of GS-NF coefficient
sums between the canonical neutron and proton braids
(`free-neutron-decay.witness.json` typed crossings):

#     net(n) = +0.81083, net(p) = +0.99913  →  Δ(net) = -0.18829

These two are exposed as `target_net_neutron()` / `target_net_proton()`
below, read from the witness at full precision.  They were written here
as bare `TARGET_NET_NEUTRON = 0.81083` / `TARGET_NET_PROTON = 0.99913`
lines, which LOOK like module-level assignments but sit inside this
docstring (lines 5-128) and so define nothing -- see those accessors for
what that cost.

══════════════════════════════════════════════════════════════════
 OBSERVABLE vs VIRTUAL DECOMPOSITION
══════════════════════════════════════════════════════════════════

For β-decay specifically, NF terms split by Coxeter length ℓ
(per beta-decay-energy-scale.md §"Observable vs virtual"):

  * **Observable** (ℓ ≥ 2): Hopf links L_±, trefoil e^-
    — topologically non-trivial, physically observable
    Δ(obs) = -0.11007 → Q_obs ≈ 0.457 MeV (58.5% of Q_β)

  * **Virtual** (ℓ < 2): identity γ, single crossings σ_0, σ_1
    — topologically trivial, gauge / off-shell debt
    Δ(virt) = -0.07822 → Q_virt ≈ 0.325 MeV (41.5% of Q_β)

The observable-only Q is the part that corresponds to physical
kinetic energy released in the β-decay event; the virtual part is
the framework's gauge / vacuum-debt contribution that cancels in
asymptotic states.

══════════════════════════════════════════════════════════════════
 NUCLEON MASSES — FULL CHAIN NOT YET WIRED
══════════════════════════════════════════════════════════════════

The proton and neutron rest masses in the FULL form require the
multi-term unified knot mass formula
([`prop:atom-knot-mass-derivation`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)):

    M(𝔥) = ρ · [|tr_M(T_w)| + tower(T_w) + tr_M(C_dim_q)]
    m_𝔥 = m_e · M(𝔥)|_{q = q_0}

with T_w = atom_braid_word_3A(Z, N).

The Strategy-3 implementation in `atomic_braid_mass_table.py` has
a known structural bug (multiplicative T1 base instead of additive
LP active-set; see lines 24-46 of that file) that produces 8-54 %
residuals on n, D, T, ³He. The LO implementation in
`atomic_mass_via_rho_k.py` is structurally tautological. Neither
is the framework's FULL prediction.

So `proton_mass_mev()` and `neutron_mass_mev()` raise
`NotImplementedError` until either (a) the multiplicative-T1 bug
is fixed via the LP-dual shadow-price scheme of
[`prop:operator-selection-lp`](../../content/quantum-observable-universe/braids-and-knots/operator-selection-lp.md),
or (b) a separate brane-tower-clean derivation is wired (Workplan 2
Phase 2 50-dps m_e_Hecke).

For now, consumers should:
  * Use `q_beta_predicted_mev()` for Q_β predictions
  * Use `q_beta_observable_mev()` / `q_beta_virtual_mev()` for the
    decomposition
  * Use `e_0_full_mev()` for the energy-scale anchor
  * NOT consume CODATA `M_P_MEV_VALIDATION` / `M_N_MEV_VALIDATION`
    as inputs to mass-prediction scripts (discipline violation,
    Workplan 0b)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
from functools import lru_cache
from pathlib import Path

import mpmath as mp

from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: F401  (re-export)

_HERE = Path(__file__).resolve().parent
_BETA_DECAY_WITNESS = _pb.witness_path("beta-decay-energy-scale.witness.json", _HERE)
_Q_PINNING_WITNESS = _pb.witness_path("q-pinning-50-digit.witness.json", _HERE)
_FREE_NEUTRON_WITNESS = _pb.witness_path("free-neutron-decay.witness.json", _HERE)

#: dps for the net-coefficient accessors. The witness stores them as JSON
#: floats (~17 significant digits), so 30 holds the source exactly with room
#: to spare; the ambient default of 15 would truncate.
_NET_COEFF_DPS = 30


@lru_cache(maxsize=None)
def _q_0() -> mp.mpf:
    """Substrate parameter q_0 at 50-dps from the q-pinning witness.

    Pulled from `q-pinning-50-digit.witness.json:derived_50_digit.q`
    (the canonical CAL-2-derived q_0); legacy float64 fallback in
    `q_parameter.Q_50_DIGIT_STR` is identical to ~50 digits.
    """
    with _Q_PINNING_WITNESS.open() as fh:
        d = json.load(fh)
    return mp.mpf(d["derived_50_digit"]["q"])


@lru_cache(maxsize=None)
def _beta_witness() -> dict:
    """Read the β-decay-energy-scale witness."""
    if not _BETA_DECAY_WITNESS.exists():
        raise FileNotFoundError(
            f"derived_masses: β-decay witness not found at "
            f"{_BETA_DECAY_WITNESS}. Run the beta-decay-energy-scale "
            f"compute first."
        )
    with _BETA_DECAY_WITNESS.open() as fh:
        return json.load(fh)


@lru_cache(maxsize=None)
def _free_neutron_witness() -> dict:
    """Read the free-neutron-decay witness (typed-crossing net coefficients)."""
    if not _FREE_NEUTRON_WITNESS.exists():
        raise FileNotFoundError(
            f"derived_masses: free-neutron-decay witness not found at "
            f"{_FREE_NEUTRON_WITNESS}. Run the free-neutron-decay compute first."
        )
    with _FREE_NEUTRON_WITNESS.open() as fh:
        return json.load(fh)


@lru_cache(maxsize=None)
def target_net_proton() -> mp.mpf:
    """GS-NF net coefficient of the canonical proton braid.

    Read from `free-neutron-decay.witness.json:proton.net_coefficient`.

    THIS REPLACES A NAME THAT NEVER EXISTED. `TARGET_NET_PROTON` appears at
    column 0 of this module -- inside the 5..128 docstring, so it defined
    nothing -- and `confinement-operator-selection.py` imported it anyway.
    That producer has been dead at import ever since, while three consumers
    read the witness it is supposed to emit. A line-anchored grep cannot
    tell docstring text from code, which is what made the name look real.

    Reading the witness also recovers the precision the docstring dropped:
    it records `0.9991251252427813`, not the 5-digit `0.99913` the prose
    quotes -- a 1.3e-6 relative difference that would have been baked into
    a ranking key had the constant simply been promoted as written.
    """
    # Construct under an explicit workdps: at the ambient default (15) an
    # `mpf` built from a 17-significant-digit source is silently truncated,
    # which is exactly what the never-raises-dps ratchet exists to catch.
    with mp.workdps(_NET_COEFF_DPS):
        return mp.mpf(str(_free_neutron_witness()["proton"]["net_coefficient"]))


@lru_cache(maxsize=None)
def target_net_neutron() -> mp.mpf:
    """GS-NF net coefficient of the canonical neutron braid.

    Read from `free-neutron-decay.witness.json:neutron.net_coefficient`
    (`0.8108345052316609`; the docstring above quotes it to 5 digits).
    See `target_net_proton` for why these are functions and not constants.
    """
    with mp.workdps(_NET_COEFF_DPS):
        return mp.mpf(str(_free_neutron_witness()["neutron"]["net_coefficient"]))


# ── Energy scale (FULL chain, derived from CAL-1 + CAL-2) ───────

@lru_cache(maxsize=None)
def e_0_n0_mev() -> mp.mpf:
    """Single-tick (Planck-tick, N=0) energy scale.

    E_0^{(N=0)} = m_e / (q_0 · (q_0 - 1))   ≈ 4.186 MeV at q_0 ≈ 1.110.

    Equivalent form `m_e · c_q² · ℏ_q` (with `c_q = 1/(q-1)` per the
    notation register Ch 11 and `ℏ_q = (q-1)/q`) — derivation given
    in
    [`beta-decay-energy-scale.md`](../../content/quantum-observable-universe/particle-interactions/beta-decay-energy-scale.md).
    Stick to the explicit `m_e / (q_0 (q_0-1))` form here to avoid
    ambiguity over which `c_q` convention is in scope.

    This is the **leading term** of the brane-tower geometric series;
    use `e_0_full_mev()` for the full tower (N → ∞) value or
    `e_0_n_mev(n)` for an explicit truncation depth.
    """
    q0 = _q_0()
    return M_E_MEV / (q0 * (q0 - 1))


@lru_cache(maxsize=None)
def e_0_n_mev(n: int) -> mp.mpf:
    """Tower truncation at depth N.

    E_0^{(N)} = E_0^{(N=0)} · Σ_{k=0}^{N} ℏ_q^{2k}
              = E_0^{(N=0)} · (1 − ℏ_q^{2(N+1)}) / (1 − ℏ_q²)

    Per [`q_beta_form_a_n1_extension.py`](./q_beta_form_a_n1_extension.py)
    lines 32–38. For N=0 this returns the single-tick value;
    for N → ∞ it converges to `e_0_full_mev()`.
    """
    if n < 0:
        raise ValueError(f"e_0_n_mev: depth n must be ≥ 0, got {n}")
    q0 = _q_0()
    hbar_q = (q0 - 1) / q0
    geometric = (1 - hbar_q ** (2 * (n + 1))) / (1 - hbar_q ** 2)
    return e_0_n0_mev() * geometric


def li2q_symmetric(z, q, terms: int | None = None):
    """Symmetric q-dilogarithm Li_2^q(z) = Σ_{n≥1} z^n / (n · [n]_q).

    With symmetric q-integer [n]_q = (q^n − q^{-n})/(q − q^{-1}).
    Per [`prop:mass-endomorphism-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md)
    lines 162–183 (the bounded Kashaev specialisation, distinct from
    the divergent compact q-dilog Φ_q). Series converges for |z| < 1.

    When `terms` is None (default), the count is **dynamically scaled
    to `mp.mp.dps`** so the truncation error stays below the current
    precision floor: terms ≈ dps · ln(10) / (-ln|z|) + 20-term margin.
    For |z| near 1 (e.g. per-atom Wedderburn volumes |V_i| ≈ 0.989),
    this picks ~1100 terms at 50 dps; for small |z| (substrate
    ℏ_q² ≈ 0.0098), ~30 terms suffice.

    No `lru_cache` — `mp.mp.dps` is global state and a stale cached
    result at lower precision would silently leak under a precision
    bump. The series is cheap enough to recompute.

    Uses incremental powers (q_pow *= q, q_inv_pow /= q) to avoid
    repeated O(n) exponentiation in the tight loop.
    """
    if terms is None:
        abs_z = abs(z)
        if abs_z >= 1:
            raise ValueError(
                f"li2q_symmetric: series diverges for |z| >= 1 (got {abs_z})"
            )
        if abs_z < mp.mpf("1e-12"):
            terms = 50
        else:
            terms = int(mp.ceil(mp.mp.dps * mp.ln(10) / (-mp.ln(abs_z)))) + 20
            terms = max(50, terms)
    q_minus_qinv = q - 1 / q
    total = mp.mpf(0)
    z_pow = mp.mpf(1)
    q_pow = q
    q_inv_pow = 1 / q
    for n in range(1, terms + 1):
        z_pow *= z
        n_q = (q_pow - q_inv_pow) / q_minus_qinv
        total += z_pow / (n * n_q)
        q_pow *= q
        q_inv_pow /= q
    return total


# Back-compat alias for any callers using the private name.
_li2q_symmetric = li2q_symmetric


@lru_cache(maxsize=None)
def e_0_full_mev() -> mp.mpf:
    """E_0 from the FULL chain, tower-summed (N → ∞), geometric form.

    E_0^{full,geom} = E_0^{(N=0)} / (1 − ℏ_q²)
                    = m_e / (q_0 · (q_0 - 1)) · 1/(1 − ℏ_q²)

    Per the geometric brane-tower series derived symbolically in
    [`q_beta_form_a_n1_extension.py`](./q_beta_form_a_n1_extension.py)
    lines 32–38. Returns ≈ 4.228 MeV at q_0 ≈ 1.110 (≈ +0.99% over
    the N=0 single-tick 4.186 MeV).

    Derived from CAL-1 m_e and CAL-2 q_0 only — no CAL-3 (Q_β) input.
    CAL-3 becomes the *prediction*, not an input.

    **Two candidate closed forms.** The substrate brane-tower
    resummation $\\sum_k \\alpha_k \\cdot \\hbar_q^{2k}$ admits at least
    two candidate closed forms — the (unbounded) geometric series
    wired here, and the **bounded** symmetric q-dilogarithm form
    `e_0_full_li2q_mev()`. The categorical question of which is the
    correct resummation of the $\\alpha_k$ stratum prefactors
    ([`prop:alpha-k-derivation-procedure`](../../content/quantum-observable-universe/braids-and-knots/alpha-k-derivation-procedure.md))
    is open — see
    [`conj:alpha-k-categorical-closure`](../../content/quantum-observable-universe/braids-and-knots/alpha-k-categorical-closure.md).
    The empirical $\\alpha_k$ values at $H_3$ (1, 0, $z^2$,
    $z(1+q^{1/2}-q^{-1/2})$) do **not** match the naive geometric
    recursion $\\alpha_k = \\hbar_q^{2(k-1)}\\alpha_{k-1}$.

    **Direction of the residual.** Wiring the geometric tower form
    makes the framework-derived E_0 *larger* than the CODATA-
    calibrated value (`e_0_calibrated_mev()` ≈ 4.155 MeV), not
    smaller. The N=0 derived overshoots by +0.75%; the geometric
    tower form overshoots by ≈ +1.75%. The Li_2^q candidate (see
    `e_0_full_li2q_mev`) gives a numerically close value — the two
    candidates differ at higher correction orders, and the
    categorical resolution awaits the conjecture above.
    """
    q0 = _q_0()
    hbar_q = (q0 - 1) / q0
    return e_0_n0_mev() / (1 - hbar_q ** 2)


@lru_cache(maxsize=None)
def e_0_full_li2q_mev() -> mp.mpf:
    """Bounded Li_2^q tower form (substrate level, candidate).

    E_0^{full,Li2q} := E_0^{(N=0)} · (1 + (−Li_2^q(−ℏ_q²)))

    Per [`prop:mass-endomorphism-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md)
    lines 162–183, the **bounded** Kashaev specialisation of the
    brane-tower integral is $-\\mathrm{Li}_2^q(-V)$, not the
    divergent $\\Phi_q(V)$ — the 2026-05-03 audit verified the
    integration identity $\\int_0^V \\ln_q(1+t)/t\\,dt = -\\mathrm{Li}_2^q(-V)$
    holds to all displayed digits at $q_0$, while the asserted
    $\\Phi_q$ form is off by 10⁶ at the high end.

    At the **substrate** level (no atom, single Planck-tick
    expansion variable $x = \\hbar_q^2$) the bounded analog factor
    $1 + (-\\mathrm{Li}_2^q(-x))$ matches the geometric factor
    $1/(1-x) = 1 + x + x^2 + \\ldots$ at leading order in $x$
    (since $-\\mathrm{Li}_2^q(-x) = x/[1]_q + x^2/(2 [2]_q) + \\ldots$
    with $[1]_q = 1$) but differs at higher orders, *without* the
    divergence as $x \\to 1$.

    **Empirical finding at $q_0 \\approx 1.110$:** the substrate
    Li_2^q form returns ≈ 4.227 MeV — only ≈ 0.012% smaller than
    the geometric form's 4.227 MeV. Both **overshoot** the CODATA-
    calibrated 4.155 MeV by ≈ +1.74% (Li_2^q) vs +1.75% (geometric).
    The bounded substrate form **does not** close CAL-3 in the
    correct direction at this level. The per-atom Li_2^q evaluation
    from `prop:mass-endomorphism-tower` (summing
    $-\\mathrm{Li}_2^q(-|\\hat V_i|)$ over generators with proper
    $|\\hat V_i|$ values) requires atomic-braid input; see
    [`conj:alpha-k-categorical-closure`](../../content/quantum-observable-universe/braids-and-knots/alpha-k-categorical-closure.md)
    for the open question of which categorical resummation closes
    CAL-3 in the correct direction.
    """
    q0 = _q_0()
    hbar_q = (q0 - 1) / q0
    hbar_q_sq = hbar_q ** 2
    # -Li_2^q(-x) = x/[1]_q + x²/(2[2]_q) - x³/(3[3]_q) + … which at
    # leading order in x matches the geometric correction x = ℏ_q²;
    # higher-order terms are *bounded* (no divergence as x → 1).
    li2q_val = li2q_symmetric(-hbar_q_sq, q0)
    correction = 1 + (-li2q_val)
    return e_0_n0_mev() * correction


@lru_cache(maxsize=None)
def e_0_calibrated_mev() -> mp.mpf:
    """E_0 cross-check via CODATA Q_β / |Δ(net)| ≈ 4.155 MeV.

    Reads `Q_decay_MeV / hecke_nf_differences.delta_net` from the
    β-decay witness. Used only for the 0.75% derived-vs-calibrated
    consistency check, not for mass predictions.
    """
    w = _beta_witness()
    q_beta_codata = mp.mpf(str(w["observed"]["Q_decay_MeV"]))
    delta_net = mp.mpf(str(w["hecke_nf_differences"]["delta_net"]))
    return q_beta_codata / abs(delta_net)


# ── Q_β predictions (FULL framework chain) ──────────────────────

@lru_cache(maxsize=None)
def q_beta_predicted_mev() -> mp.mpf:
    """Q_β prediction via the symbolic single-wrap closed form.

    Per [`prop:neutron-qvalue-symbolic`](../../content/quantum-observable-universe/particle-interactions/neutron-qvalue-symbolic.md):

        Q_β = m_e · |q_0² - 2q_0 - 1| · (q_0 + 1) / (2 q_0³)

    This is the canonical closed-form expression at single wrap. The
    L_± and e^- contributions cancel exactly in Δ(net) = h(h-2)/2
    with h = q - q^{-1}; only the γ, σ_0, σ_1 channels carry the
    Q-value. Result ≈ 0.7836 MeV vs CODATA 0.7823 MeV (+0.18%).

    Replaces the earlier typed-crossings implementation that used
    Δ(net) = -0.18829 from beta-decay-energy-scale.witness.json
    (which gave +0.747% — the residual was finite-size noise from
    the 6-term decomposition's L_±/e^- channels picking up small
    asymmetric pieces that should cancel exactly at single wrap).

    The remaining +0.18% is the brane-tower truncation residual:
    the derived E_0 = m_e/(q_0(q_0-1)) uses the single-level
    (Planck-tick) approximation; the exact tower-summed E_0 would
    absorb this 0.18% / 1.3 keV residual. Closure path: Workplan 2
    Phase 2 50-dps m_e_Hecke lift.
    """
    q0 = _q_0()
    return M_E_MEV * abs(q0 ** 2 - 2 * q0 - 1) * (q0 + 1) / (2 * q0 ** 3)


@lru_cache(maxsize=None)
def q_beta_kashiwara_n2_mev() -> mp.mpf:
    """Q_β via the parameter-free Kashiwara b² truncation (N=2).

    Canonical near-match Q_β used for the production neutron mass
    (`m_n = m_p + Q_β + m_e`). Refines the single-wrap closed form
    `q_beta_predicted_mev()` (= Q_A, +1677 ppm on Q_β) by the first two
    parameter-free Kashiwara brane-tower corrections — all functions of
    q_0 alone, NO experimental input:

        Q_A   = m_e·|q²−2q−1|(q+1)/(2q³)            (= q_beta_predicted_mev)
        z     = 1/(√q + 1/√q),  h = q − q⁻¹,  ℏ_q = (q−1)/q
        α     = (z − 1)·h / 2
        b     = √(1 − q²/(q²+1)²)                     (Hoefsmit b)
        Q_N1  = Q_A · cos(α − b·ℏ_q²/2)               (N=1, +73.8 ppm on Q_β)
        Q_N2  = Q_N1 · (1 − b²·ℏ_q⁴)                  (N=2, +1.25 ppm on Q_β)

    TIER: **near-match** (not proved). The b^k recursion is the Kashiwara
    crystal brane-tower of `prop:tau-M-asymptotic-rep-theory` (authorNote
    status: experimental); N=2 is a truncation order chosen by target
    precision — the same convergent-ladder discipline as the Q_β c_k
    framing (`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`).
    The experimental Q_β (Q_AME) enters only the probe's *error metric*,
    never the value. Exact closure is gated on the s5-so3 / Habiro-element
    keystone (`conj:s5-so3-fiber-action`, bean s5bb).

    On the neutron, Q_β is only ~0.083 % of m_n, so the 1.25 ppm Q-error
    becomes ~1 ppb on m_n — vs the flavor-split route's −1.76 ppm.

    Probe: `probe_q_beta_operator_valued_N3.py`
    (witness `q-beta-operator-valued-N3.witness.json`: Q_N2, eps_N2 ≈ 1.25 ppm).
    """
    q = _q_0()
    Q_A = q_beta_predicted_mev()
    h = q - 1 / q
    z = q**3 / (q**2 + 1)
    hbar_q = (q - 1) / q
    alpha = (z - 1) * h / 2
    q_sq = q ** 2
    b = mp.sqrt(1 - q_sq / (q_sq + 1) ** 2)        # Hoefsmit b (= probe's d1·d2+1)
    Q_N1 = Q_A * mp.cos(alpha - b * hbar_q ** 2 / 2)
    return Q_N1 * (1 - b ** 2 * hbar_q ** 4)


@lru_cache(maxsize=None)
def q_beta_toroidal_mev() -> mp.mpf:
    """Q_β via the Toroidal Harmonic basis / Weber ODE ansatz (N=4 probe).

    ⚠ PROBE / near-match — NOT canonical, NOT wired to production.
    The canonical production Q_β for the neutron mass is
    ``q_beta_kashiwara_n2_mev`` (what the m-p-substrate-identity witness
    and ``canonical_mass.py`` use); this toroidal tower is an exploratory
    N=4 fixed-real-coefficient variant kept for comparison only. It was
    unwired from ``canonical_mass.py`` on 2026-07-19 (owner directive
    "canonical derivation only — no silent fallback"; the 2026-07-06
    ruling "do not re-wire q_beta_toroidal_mev into canonical_mass.py").

        Q_A   = m_e·|q²−2q−1|(q+1)/(2q³)
        z     = 1/(√q + 1/√q),  h = q − q⁻¹,  ℏ_q = (q−1)/q
        α     = (z − 1)·h / 2
        b     = √(1 − q²/(q²+1)²)
        u     = b·ℏ_q²
        Q_N1  = Q_A · cos(α − u/2)
        Q_Tor = Q_N1 · (1 - u² - 2·u³ + 2·u⁴)

    Coefficient tiers (ck-dk-canonical-registry.md §3 — NOT "exact"):
      • c_2 = −1 : PROVED, Taylor-exact, anchor-stable (the only canonical rung).
      • c_3 = −2 : EMPIRICAL — near-match, REFUTED as a real-q fibre element
                   (~2.6–3% cross-anchor swing; dc_3/dq ≈ 4.6×10⁶; no fixed
                   real c_3 holds across anchors — SRigidityPrune).
      • c_4 = +2 : Parabolic-Cylinder ansatz ESTIMATE; the registry's
                   CODATA-residual fit for c_4 is −0.97157 (a fit/artifact),
                   not +2 — the two disagree, so +2 is not derived either.

    The (A=2, C=−22) Parabolic Cylinder / half-integer toroidal basis
    P_{n-1/2}^m is the ansatz that motivates the coefficients, not a proof
    of them. Audit: docs/audits/2026-07-19-qbeta-toroidal-tower-overclaim-audit.md.
    """
    q = _q_0()
    Q_A = q_beta_predicted_mev()
    h = q - 1 / q
    z = q**3 / (q**2 + 1)
    hbar_q = (q - 1) / q
    alpha = (z - 1) * h / 2
    q_sq = q ** 2
    b = mp.sqrt(1 - q_sq / (q_sq + 1) ** 2)
    u = b * hbar_q ** 2
    Q_N1 = Q_A * mp.cos(alpha - u / 2)
    return Q_N1 * (1 - u**2 - 2 * u**3 + 2 * u**4)



@lru_cache(maxsize=None)
def q_beta_predicted_typed_crossing_mev() -> mp.mpf:
    """Q_β via typed-crossings 6-term decomposition (LEGACY, +0.747% err).

    Reads `Δ(net) = -0.18829` from beta-decay-energy-scale.witness
    and multiplies by E_0_full. Kept for cross-check against the
    symbolic single-wrap form; do not use for production predictions.
    """
    w = _beta_witness()
    delta_net = mp.mpf(str(w["hecke_nf_differences"]["delta_net"]))
    return abs(delta_net) * e_0_full_mev()


@lru_cache(maxsize=None)
def q_beta_observable_mev() -> mp.mpf:
    """Q_β observable component = |Δ(obs)| · E_0.

    Observable terms have Coxeter length ℓ ≥ 2 (Hopf links L_±,
    trefoil e^-) — topologically non-trivial, physically observed.
    ≈ 0.457 MeV (58.5% of full Q_β).

    Per [`beta-decay-energy-scale`](../../content/quantum-observable-universe/particle-interactions/beta-decay-energy-scale.md)
    §"Observable vs virtual: Q_{≥2}".
    """
    w = _beta_witness()
    delta_obs = mp.mpf(str(w["observable_split"]["delta_obs"]))
    return abs(delta_obs) * e_0_full_mev()


@lru_cache(maxsize=None)
def q_beta_virtual_mev() -> mp.mpf:
    """Q_β virtual component = |Δ(virt)| · E_0.

    Virtual terms have Coxeter length ℓ < 2 (identity γ, single
    crossings σ_0, σ_1) — topologically trivial, gauge / vacuum
    debt. ≈ 0.325 MeV (41.5% of full Q_β).

    Sums to q_beta_predicted_mev() within rounding.
    """
    w = _beta_witness()
    delta_virt = mp.mpf(str(w["observable_split"]["delta_virt"]))
    return abs(delta_virt) * e_0_full_mev()


# ── Nucleon + light-nucleus masses (FULL chain not yet wired) ──

def _full_chain_stub(observable: str, blocker: str) -> mp.mpf:
    raise NotImplementedError(
        f"derived_masses.{observable}: FULL-chain prediction not yet "
        f"wired. {blocker} The LO chain in atomic_mass_via_rho_k.py "
        f"is structurally tautological (|tr_M| cancels in ρ_K · m_e · "
        f"|tr_M|, so M_pred = Z·m_p + N·m_n with CODATA inputs); the "
        f"Strategy-3 chain in atomic_braid_mass_table.py uses a "
        f"multiplicative T1 base that's structurally wrong (atomic-"
        f"scale composition is additive, not multiplicative; see lines "
        f"24-46 of that file). Neither is the FULL framework "
        f"prediction. Per owner directive 2026-05-10: do not consume "
        f"either as a substitute. Wire the FULL multi-term unified "
        f"knot mass formula (prop:atom-knot-mass-derivation) once the "
        f"LP-dual shadow-price closure (prop:operator-selection-lp) "
        f"or Phase 2 m_e_Hecke 50-dps lift lands."
    )


def proton_mass_mev() -> mp.mpf:
    return _full_chain_stub(
        "proton_mass_mev",
        "Proton-specific blocker: the brane tower component "
        "tower(T_w) at H_3 with T_w = atom_braid_word_3A(1, 0) "
        "needs the Φ_q-tower truncation to <1 ppb (currently ~1.8% "
        "systematic in mass_endomorphism.py:5,26).",
    )


def neutron_mass_mev() -> mp.mpf:
    return _full_chain_stub(
        "neutron_mass_mev",
        "Neutron-specific blocker: same as proton, plus the n/p "
        "split should reproduce Q_β + m_e to <1 ppb under the "
        "FULL chain (currently checked only via |Δ(net)| · E_0 = "
        "0.788 MeV vs CODATA 0.78233341 MeV at 0.75%).",
    )


def deuteron_mass_mev() -> mp.mpf:
    return _full_chain_stub(
        "deuteron_mass_mev",
        "Light-nucleus blocker: requires nucleon FULL chain plus "
        "categorical Δ_λ derivation (open per recomputed-low-isotope-"
        "mass-table.md:99; 5 closure principles tested in PRs "
        "#600/#602/#603, all fail or reproduce Occam).",
    )


def triton_mass_mev() -> mp.mpf:
    return _full_chain_stub("triton_mass_mev", "Same as deuteron.")


def helium3_mass_mev() -> mp.mpf:
    return _full_chain_stub("helium3_mass_mev", "Same as deuteron.")


def helium4_mass_mev() -> mp.mpf:
    return _full_chain_stub(
        "helium4_mass_mev",
        "Light-nucleus blocker: same as deuteron, plus ⁴He H_12 "
        "Wenzl-bridge intractable in current Python mpmath (77 "
        "partitions, max dim 7700, ~2×10¹³ ops/partition × 47 "
        "crossings); needs Rust kernel or Wenzl 1988 LR branching.",
    )


def derivation_summary() -> dict:
    """Document the current state for sibling-agent / consumer use."""
    w = _beta_witness()
    return {
        "phase": "0b.4 (FULL Q_β chain wired; nucleon + light-nucleus masses stubbed)",
        "calibration_inputs_loaded": {
            "CAL-1_m_e_MeV": str(M_E_MEV),
            "CAL-2_q_0": str(_q_0()),
            "CAL-3_Q_beta_MeV": str(Q_BETA_MEV) + " (cross-check only; predicted by framework below)",
        },
        "wired_predictions": {
            "E_0_N0_MeV": str(e_0_n0_mev()),
            "E_0_full_MeV": str(e_0_full_mev()),
            "E_0_calibrated_MeV": str(e_0_calibrated_mev()),
            "E_0_N0_vs_calibrated_pct": float(
                (e_0_n0_mev() - e_0_calibrated_mev()) / e_0_calibrated_mev() * 100
            ),
            "E_0_full_vs_calibrated_pct": float(
                (e_0_full_mev() - e_0_calibrated_mev()) / e_0_calibrated_mev() * 100
            ),
            "Q_beta_predicted_MeV": str(q_beta_predicted_mev()),
            "Q_beta_observable_MeV": str(q_beta_observable_mev()),
            "Q_beta_virtual_MeV": str(q_beta_virtual_mev()),
            "Q_beta_codata_MeV": str(w["observed"]["Q_decay_MeV"]),
            "Q_beta_pred_vs_codata_pct": float(
                (q_beta_predicted_mev() - mp.mpf(str(w["observed"]["Q_decay_MeV"])))
                / mp.mpf(str(w["observed"]["Q_decay_MeV"])) * 100
            ),
            "Q_beta_observable_fraction": float(
                q_beta_observable_mev() / q_beta_predicted_mev()
            ),
        },
        "stubbed_predictions": [
            "proton_mass_mev", "neutron_mass_mev",
            "deuteron_mass_mev", "triton_mass_mev",
            "helium3_mass_mev", "helium4_mass_mev",
        ],
        "owner_directive_2026_05_10": (
            "do not use LO -- use full. look at discussion on observable "
            "vs nonobservable energy in case of beta decay. Per this "
            "directive: do NOT pull mass predictions from LO ρ_K (which "
            "is tautological by |tr_M| cancellation) or Strategy-3 "
            "(which has the multiplicative T1 bug). Q_β has a clean FULL "
            "chain — wired above. Nucleon + light-nucleus masses don't "
            "yet have a FULL chain implementation; stubs raise "
            "NotImplementedError pointing at the blockers."
        ),
        "handoff_doc": (
            "docs/audits/2026-05-10-workplan-0b-script-rewire-handoff.md"
        ),
    }


__all__ = [
    "e_0_n0_mev", "e_0_n_mev", "e_0_full_mev", "e_0_full_li2q_mev",
    "e_0_calibrated_mev",
    "q_beta_predicted_mev", "q_beta_observable_mev", "q_beta_virtual_mev",
    "q_beta_kashiwara_n2_mev", "q_beta_toroidal_mev",
    "proton_mass_mev", "neutron_mass_mev",
    "deuteron_mass_mev", "triton_mass_mev",
    "helium3_mass_mev", "helium4_mass_mev",
    "derivation_summary",
]


if __name__ == "__main__":
    print(json.dumps(derivation_summary(), indent=2))
