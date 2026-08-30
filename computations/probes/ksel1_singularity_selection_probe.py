#!/usr/bin/env python3
"""ksel1_singularity_selection_probe.py — KSel-1 (singularity matching):
can RSZ's output-regularity axis, made concrete with QOU data, pin the
(REP) canonical kernel choice — i.e. does a UNIQUE u-translate place the
q-Laplace output's singularities at a corpus-known singularity location?

Bean qou-334t. AUDIT-ONLY — scope-(a), NO FIT, nothing wired; the target
conjecture (conj:schwinger-measure-computational-time, hypothesis (REP))
stays a conjecture. Machinery reused with attribution from
computations/probes/rep_jackson_identification_probe.py (Attack 1, bean
qou-u5p0): the Jackson/theta atomic kernel, the u-translate family, the
reindex identity, measure_eq. Parallel principles KSel-2 (GNS) and
KSel-3 (modular double) are owned by sibling agents — not touched here.

BACKGROUND. The REP audit (docs/audits/2026-08-01-rep-jackson-
identification.md §3) leaves a u-CONTINUUM of positive bar-symmetric
atomic kernels with the balanced moments N^bal(n) =
q^{-(n-1)(n-2)/4}[n-1]_q!: the theta-translate family mu_u (atoms
u·qt^j, qt = sqrt(q), masses ∝ qt^{-j(j+1)/2}u^{-j}), Jackson-convolved.
KSel-1 asks whether the OUTPUT-side analytic structure (RSZ §1.2.1's
"optimality"/regularity remark, made concrete) selects u: each
u-translate shifts the kernel's atom/zero lattice, hence shifts where
the q-Laplace output can be singular; the corpus independently knows
binding-side singularity data (the level-1/2 Borel singularity at
xi = 1/sqrt(2), q = 1 — lever1_borel_half_singularity_probe.py +
lever1_gevrey_order_pin.py + the 2026-07-12 alien-calculus audit).

WHAT THIS PROBE ESTABLISHES (all exact or 60-dps / 1e-30):

  K1  CORPUS SINGULARITY DATUM re-pinned + tiered (q = 1, exact
      integers): level-1/2 Borel coefficients of the binding period
      a_D(n) = I(n)/n are POSITIVE (Pringsheim: the singularity is on
      the positive real axis — exact), the Lean sandwich
      n! <= 4^n I(n)^2 <= 8^n n! holds (mirror of the sorry-free
      QOU/Mass/BindingGevreyHalf.lean, n <= 60), and the root test
      extrapolates to sqrt(2) (location xi* = 1/sqrt(2)). TIER:
      class = Lean-proved; location = classical-asymptote-derived +
      measured scope-(a) (Pade witness lever1-borel-half-singularity-
      probe); NOT a q0-fibre datum.
  K2  THE EXACT MAP u |-> pole set (model leg, q = 1.2): if the input
      (q-Borel-side) function has a pole at xi*, the atomic-kernel
      q-Laplace output L_u(x) = sum_a (c_a/t_a) fhat(x t_a) has pole
      set EXACTLY { xi*/t_a } = xi*(1-p)/u · qt^Z (p = 1/q): the kernel
      support is u/(1-p)·qt^Z (exponent j-2m covers Z, constructive),
      residues cannot cancel (all masses positive), and the map
      u |-> [pole-lattice position] in R_{>0}/qt^Z is a FREE TRANSITIVE
      circle action: translating u by du shifts the lattice by du^{-1}
      exactly. Consequently ONE independently-known output pole location
      x_tgt selects a UNIQUE u = xi*(1-p)/x_tgt mod qt^Z (verified:
      the solved u hits x_tgt to 1e-30; a detuned u misses by the
      detuning). KSel-1 is well-formed and uniquely selective IN FORM.
  K3  THE REAL BINDING DATA FAIL THE HYPOTHESES (q = 1.2 + both q0
      pins; n <= 400 via the exact q-telephone recurrence
      S(n+2) = S(n+1) + [n+1]_q S(n), the REP-R3 q-lift carrier,
      checked = involution numbers at q = 1):
      (a) the q-Borel-side function phi(xi) = sum b^q_n xi^n,
          b^q_n = S(n)/[n]_q!, is ENTIRE at q > 1: b^q_n ~
          q^{-n^2/4}·rho_phi^{-n} with the normalized ratio
          g(n) = (b_{n+1}/b_n)·q^{(2n+1)/4} converging (two-cycle,
          parity-resolved, Cauchy < 1e-8) — there is NO finite
          q-Borel-plane singularity at the fibre for the input-side
          matching to target (NEW sharp finding; the q = 1 datum
          xi = 1/sqrt(2) lives in the classical level-1/2 plane, which
          the corpus already showed collapses at q0).
      (b) the balanced period series sum B^bal_n x^n (B^bal_n =
          b^q_n·N^bal(n)) is GEOMETRIC class at q > 1 with finite
          positive radius r* (NEW measured datum; two-cycle ratio
          geometric mean; exact per-n identity ratB(n) =
          g(n)·q^{1/4-n}[n]_q asserted to 1e-40): r* ~ 0.4681 (q=1.2),
          ~ 0.34039 (both q0 pins, differing only at the pin
          difference). All B^bal_n > 0 => (Pringsheim) the output-side
          singularity sits ON THE POSITIVE REAL AXIS at x* = r*.
          Confluence consistency: at q = 1 the recurrence gives
          B_n = I(n)/n (radius 0, the known Gevrey-1/2 divergence);
          the finite radius is a fibre-level phenomenon.
  K4  THE SELECTION VERDICT — CONTINUUM SURVIVES, EXACTLY: for x > 0
      every term of the kernel output is positive, so (Tonelli
      rearrangement — verified numerically: windowed atomic double sum
      = truncated series to < 1e-25 for u in {1, 1.3, qt^{1/2}}) the
      output equals the u-INDEPENDENT series sum b^q_n N^bal(n) x^n
      wherever it converges and diverges to +inf beyond r* — for EVERY
      u. The positive-axis output singularity (the only corpus-
      computable output datum, K3b) is therefore EXACTLY u-invariant,
      by the same reindex mechanism that makes the moments u-invariant:
      any positive-axis output functional determined by the moments
      cannot see u. KSel-1 has no referent on the input side (phi
      entire, K3a) and is exactly degenerate on the output positive
      axis (this block). No unique u is selected. The honest verdict is
      recorded: the u-circle continuum SURVIVES KSel-1.
  K5  CROSS-CHECKS: balanced moments hold at u = 1, 1.3, AND the two
      bar-reflection self-dual points u = 1, u = qt^{1/2} (u-invariance
      by construction — asserted < 1e-30); the family is a genuine
      circle (mu_{qt·u} = mu_u as normalized measures, 1e-28); the
      reflection sigma: s |-> qt^{-1}/s maps mu_u -> mu_{1/u} and fixes
      exactly the classes u = 1 and u = qt^{1/2}; and the two self-dual
      points' MODEL pole-lattice classes differ by exactly HALF a
      qt-step (|frac - 1/2| < 1e-25) — recorded, not interpreted: since
      KSel-1 selects no u, no selected-u-vs-self-dual (KSel-3)
      coincidence exists to evaluate; the half-step offset is the exact
      discriminant a future measured output pole lattice would use to
      split the two maximal-symmetry candidates.

VERDICT SHAPE (scope-(a)): KSel-1 is a well-formed selection axis with
unique selectivity in form (K2), but for the QOU binding data it
selects nothing: the fibre q-Borel side is entire (no input singularity
to match) and the only computable output-side singularity (positive-
axis wall x* = r*, newly measured here) is exactly u-invariant. The
(REP) canonical-choice continuum survives. Nothing here proves or
refutes the conjecture; no fit; nothing wired.

Exit 0 iff all assertions pass. Witness:
ksel1-singularity-selection.witness.json (audit-only).
Audit doc: docs/audits/2026-08-01-ksel1-singularity-selection.md.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02). Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _bridge

import json  # noqa: E402

import sympy as sp  # noqa: E402
from mpmath import mp, mpf, sqrt as mpsqrt  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

TOL_EXACT = 0        # sympy exact / integer comparisons
TOL_50 = 1e-30       # 60-dps kernel-identity cross-checks
TOL_MEAS = 1e-25     # measure-equality / rearrangement cross-checks
N_MOM = 9            # kernel ds/s-moments checked (k = 0..N_MOM)
N_REC = 400          # carrier recurrence depth for growth/radius pins
U_GENERIC = "1.3"    # generic translate parameter (REP R4 convention)
X_TGT = "0.53"       # generic target output-pole location (K2 demo)

# q0, both pins, 50-digit strings with provenance (muon from the
# canonical witness; proton from qou_substrate.constants
# Q_50_DIGIT_STR) — same sourcing as rep_jackson_identification_probe.
_MUON_WITNESS = _Path(__file__).resolve().parent.parent / \
    "q-pinning-50-digit.witness.json"
Q0_MUON_STR = record_upstream(_MUON_WITNESS, _UPSTREAM_RECORDS)["q0Value"]
Q0_PROTON_STR = "1.1099785827513808075916690956107688798744991218736"

_ii, _jj, _kk, _mm = sp.symbols("i j k m", integer=True)
_us, _xis, _ps, _qts = sp.symbols("u xi p qtilde", positive=True)


# ------------------------------------------------------------ exact helpers

def involution_numbers(n_max: int) -> list[sp.Integer]:
    """I(0..n_max): I(0) = I(1) = 1, I(n+2) = I(n+1) + (n+1)·I(n) —
    the corpus binding-period numerators (sw-classical-jet-exactness;
    QOU.Mass.BindingGevreyHalf.involutionNumber)."""
    I = [sp.Integer(1), sp.Integer(1)]
    for n in range(n_max - 1):
        I.append(I[-1] + (n + 1) * I[-2])
    return I


def mp_qint(q0: mpf, k: int) -> mpf:
    """One-sided [k]_q (corpus convention)."""
    return (q0 ** k - 1) / (q0 - 1)


def build_carrier(q0: mpf, n_max: int):
    """The REP-R3 q-lift carrier: S(n+2) = S(n+1) + [n+1]_q S(n),
    b^q_n = S(n)/[n]_q!, plus [n]_q! itself. Returns (S, qfact) lists
    indexed 0..n_max+1 (qfact) / 0..n_max+1 (S)."""
    S = [mpf(1), mpf(1)]
    for n in range(n_max):
        S.append(S[-1] + mp_qint(q0, n + 1) * S[-2])
    qf = [mpf(1)]
    for n in range(1, n_max + 2):
        qf.append(qf[-1] * mp_qint(q0, n))
    return S, qf


def mp_balanced_normalizer(q0: mpf, qf: list[mpf], n: int) -> mpf:
    """N^bal_q(n) = q^{-(n-1)(n-2)/4}·[n-1]_q! (Attack E balanced
    convention)."""
    m = n - 1
    return q0 ** (-mpf(m * (m - 1)) / 4) * qf[m]


# --------------------------- fibre kernels (Attack B, via the REP probe)

def jackson_factor(q0: mpf, k_max: int, tail_dps: int = 42):
    """Jackson q-Gamma kernel at p = 1/q0 (Attack-B C4a; reused from
    rep_jackson_identification_probe.jackson_factor): atoms
    t_m = p^m/(1-p), masses c_m = p^m·(p^{m+1};p)_inf > 0; moments
    sum c_m t_m^k = [k]_p!."""
    p = 1 / q0
    M = int(tail_dps / -mp.log10(p)) + 60
    pp = [mpf(1)]
    for j in range(1, M + 1):
        pp.append(pp[-1] * (1 - p ** j))
    pp_inf = pp[-1]
    a = 1 / (1 - p)
    atoms = [a * p ** m for m in range(M)]
    masses = [p ** m * pp_inf / pp[m] for m in range(M)]
    moments = [sum(c * t ** k for c, t in zip(masses, atoms))
               for k in range(k_max + 1)]
    return atoms, masses, moments


def theta_translate_factor(q0: mpf, uu: mpf, k_max: int,
                           tail_dps: int = 42):
    """u-translated half-weight theta kernel at qt = sqrt(q0) (reused
    from rep_jackson_identification_probe.theta_translate_factor):
    atoms u·qt^j (j in Z), masses ∝ qt^{-j(j+1)/2}·u^{-j} normalized.
    Moments are u-INDEPENDENT: exactly q0^{k(k-1)/4} (REP R4a reindex
    identity)."""
    qt = mpsqrt(q0)
    J = 10
    while float((J * (J + 1) / 2 - J * (k_max + 4)) * mp.log10(qt)) \
            < tail_dps + 10:
        J += 10
    js = list(range(-J, J + 1))
    w = [qt ** (-mpf(j * (j + 1)) / 2) * uu ** (-j) for j in js]
    Z = sum(w)
    atoms = [uu * qt ** j for j in js]
    masses = [ww / Z for ww in w]
    moments = [sum(c * t ** k for c, t in zip(masses, atoms))
               for k in range(k_max + 1)]
    return js, atoms, masses, moments


def measure_eq(atoms_a, masses_a, atoms_b, masses_b, tol,
               mass_floor=mpf("1e-38")) -> bool:
    """Atomic-measure equality up to truncation dust (reused from
    rep_jackson_identification_probe.measure_eq)."""
    fa = sorted((a, m) for a, m in zip(atoms_a, masses_a) if m > mass_floor)
    fb = sorted((a, m) for a, m in zip(atoms_b, masses_b) if m > mass_floor)
    if len(fa) != len(fb):
        return False
    worst = mpf(0)
    for (aa, ma), (ab, mb) in zip(fa, fb):
        if abs(aa / ab - 1) > mpf("1e-20"):
            return False
        worst = max(worst, abs(ma / mb - 1))
    return worst < tol


def product_kernel(q0: mpf, uu: mpf, k_max: int):
    """Full Attack-B kernel K_u = Jackson ⊛ theta-translate as an
    explicit atomic measure (atom products, mass products)."""
    at_j, ms_j, _ = jackson_factor(q0, k_max)
    _, at_t, ms_t, _ = theta_translate_factor(q0, uu, k_max)
    atoms, masses = [], []
    for tj, cj in zip(at_j, ms_j):
        if cj < mpf("1e-45"):
            continue
        for tt, ct in zip(at_t, ms_t):
            c = cj * ct
            if c < mpf("1e-45"):
                continue
            atoms.append(tj * tt)
            masses.append(c)
    return atoms, masses


def frac_part(x: mpf) -> mpf:
    return x - mp.floor(x)


# ---------------------------------------------------------------- Block K1

def block_k1_corpus_datum(wb: WitnessBuilder) -> None:
    """K1: the corpus's independently-known binding Borel singularity
    datum, re-pinned with its epistemic tier (q = 1, exact integers +
    mpmath; mirrors lever1_borel_half_singularity_probe.py and the
    Lean sandwich of QOU/Mass/BindingGevreyHalf.lean)."""
    NN = 60
    I = involution_numbers(NN)
    # (i) Lean-sandwich mirror, exact integers: n! <= 4^n I(n)^2 <= 8^n n!
    for n in range(NN + 1):
        f = sp.factorial(n)
        assert f <= sp.Integer(4) ** n * I[n] ** 2, n
        assert I[n] ** 2 <= sp.Integer(2) ** n * f, n
    # (ii) Pringsheim positivity of the level-1/2 coefficients (exact):
    # b_n = (I(n)/n)/Gamma(n/2+1) > 0 for all n — the dominant
    # singularity of the level-1/2 Borel transform is on the POSITIVE
    # real axis.
    assert all(I[n] > 0 for n in range(1, NN + 1))
    # (iii) location xi* = 1/sqrt(2): root test + the lever1 3-point
    # extrapolation (model ln r_n = ln rho^{-1} + a/sqrt(n) + c ln n/n).
    b1 = [mpf(int(I[n])) / n / mp.gamma(mpf(n) / 2 + 1)
          for n in range(1, NN + 1)]
    rt = {n: b1[n - 1] ** (mpf(1) / n) for n in (30, 40, 60)}
    A = mp.matrix(3, 3)
    rhs = mp.matrix(3, 1)
    for i, n in enumerate((30, 40, 60)):
        A[i, 0], A[i, 1], A[i, 2] = 1, 1 / mp.sqrt(n), mp.log(n) / n
        rhs[i, 0] = mp.log(rt[n])
    sol = mp.lu_solve(A, rhs)
    r_extrap = mp.e ** sol[0, 0]
    rel = abs(r_extrap / mp.sqrt(2) - 1)
    assert rel < mpf("0.10"), rel
    wb.add_assertion(
        "k1_corpus_singularity_datum_q1", computed=mp.nstr(rel, 5),
        expected="0", tolerance=0.10,
        source="q = 1, exact integers n <= 60 + mpmath 60 dps: the "
               "Lean sandwich n! <= 4^n I(n)^2 <= 8^n n! (mirror of "
               "sorry-free QOU/Mass/BindingGevreyHalf.lean) holds "
               "exactly; the level-1/2 Borel coefficients "
               "(I(n)/n)/Gamma(n/2+1) are all positive (Pringsheim: "
               "dominant singularity ON the positive real axis — "
               "exact); the root test extrapolates to sqrt(2) within "
               "10% (location xi* = 1/sqrt(2)). TIER: growth class "
               "Gevrey-1/2 = Lean-proved; location 1/sqrt(2) = "
               "classical-asymptote-derived + measured scope-(a) "
               "(Pade pole 0.688, 2.6% — witness "
               "lever1-borel-half-singularity-probe; local model + "
               "Stokes constant in lever1-bridge-alien-datum). This "
               "datum lives in the CLASSICAL level-1/2 plane at q = 1; "
               "the corpus (gevrey-order pin) already showed that "
               "plane collapses at q0 (class change to q-Gevrey)")
    wb.add_data("corpus_singularity_tiers", {
        "q1_level_half_location": {
            "value": "xi = 1/sqrt(2) ~ 0.7071, positive real axis, "
                     "non-polar (branch/essential)",
            "tier": "measured scope-(a) + classical-asymptote-derived "
                    "(Pringsheim axis: exact positivity)",
            "witness": "computations/lever1-borel-half-singularity-"
                       "probe.witness.json",
        },
        "q1_growth_class": {
            "value": "Gevrey-1/2",
            "tier": "proved-lean (QOU/Mass/BindingGevreyHalf.lean, "
                    "sorry-free two-sided sandwich)",
        },
        "q1_stokes_datum": {
            "value": "A_omega = 4·sqrt(2)·e^{-3/8}, gamma = 3/2, "
                     "second-level action 1/4",
            "tier": "measured scope-(a) (derived-before-measurement "
                    "local model)",
            "witness": "computations/lever1-bridge-alien-datum."
                       "witness.json",
        },
        "q0_classical_plane": {
            "value": "NO classical Borel-plane singularity: level-1/2 "
                     "radius collapses (class change to q-Gevrey)",
            "tier": "measured scope-(a) (lever1-gevrey-order-pin + "
                    "lever1-borel-half-singularity-probe q0 legs)",
        },
    })


# ---------------------------------------------------------------- Block K2

def block_k2_pole_lattice_map(wb: WitnessBuilder, xi_star: mpf) -> dict:
    """K2 (model leg, q = 1.2): the exact map u |-> output pole set for
    an input with a Borel-plane pole at xi*, and its unique selectivity
    on the circle R_{>0}/qt^Z."""
    # -- exact algebra (sympy): the pole-location identity.
    # Kernel atom t = (p^m/(1-p)) · u·qt^j with p = qt^{-2}; input pole
    # at xi* => output pole at xi*/t = (xi*(1-p)/u)·qt^{2m-j}.
    t_expr = (_ps ** _mm / (1 - _ps)) * _us * _qts ** _jj
    pole_expr = _xis / t_expr
    lattice_expr = (_xis * (1 - _ps) / _us) * _qts ** (2 * _mm - _jj)
    d = sp.simplify(pole_expr.subs(_ps, _qts ** -2)
                    - lattice_expr.subs(_ps, _qts ** -2))
    assert d == 0, d
    # -- exponent coverage: {j - 2m : j in Z, m >= 0} = Z (constructive:
    # k = (k + 2m) - 2m for any m >= 0; exhibit m = 0, j = k).
    for k in range(-8, 9):
        m0, j0 = 0, k
        assert j0 - 2 * m0 == k
    # -- numeric leg at q = 1.2: every pole xi*/t_a lands on the lattice
    # xi*(1-p)/u·qt^Z, and translating u shifts the lattice class by
    # exactly -log_qt(u).
    q0 = mpf("1.2")
    qt = mpsqrt(q0)
    p = 1 / q0
    lnqt = mp.log(qt)
    worst = mpf(0)
    classes = {}
    for uname, uu in (("1", mpf(1)), ("generic", mpf(U_GENERIC)),
                      ("selfdual_half", qt ** mpf("0.5"))):
        atoms, masses = product_kernel(q0, uu, N_MOM)
        assert min(masses) > 0          # positivity: residues cannot cancel
        base = xi_star * (1 - p) / uu
        for t in atoms:
            pole = xi_star / t
            resid = frac_part(mp.log(pole / base) / lnqt)
            resid = min(resid, 1 - resid)
            worst = max(worst, resid)
        classes[uname] = frac_part(mp.log(base) / lnqt)
    assert worst < TOL_50, worst
    # class shift: class(u) - class(1) == -log_qt(u) mod 1 (free action)
    for uname, uu in (("generic", mpf(U_GENERIC)),
                      ("selfdual_half", qt ** mpf("0.5"))):
        pred = frac_part(classes["1"] - mp.log(uu) / lnqt)
        got = classes[uname]
        dshift = min(abs(got - pred), 1 - abs(got - pred))
        worst = max(worst, dshift)
    assert worst < TOL_50, worst
    # -- unique selectivity: solve u for a generic target pole x_tgt.
    x_tgt = mpf(X_TGT)
    u_raw = xi_star * (1 - p) / x_tgt
    kshift = mp.floor(mp.log(u_raw) / lnqt)
    u_sel = u_raw / qt ** kshift          # representative in [1, qt)
    base_sel = xi_star * (1 - p) / u_sel
    hit = frac_part(mp.log(x_tgt / base_sel) / lnqt)
    hit = min(hit, 1 - hit)
    assert hit < TOL_50, hit
    u_off = u_sel * qt ** mpf("0.37")
    base_off = xi_star * (1 - p) / u_off
    miss = frac_part(mp.log(x_tgt / base_off) / lnqt)
    miss = min(miss, 1 - miss)
    assert miss > mpf("0.3"), miss        # detuned u misses by the detuning
    wb.add_assertion(
        "k2_pole_lattice_map_exact_and_uniquely_selective",
        computed=mp.nstr(worst, 5), expected="0", tolerance=TOL_50,
        source=f"q = 1.2, sympy exact + 60 dps: for an input with a "
               f"Borel-plane pole at xi* = 1/sqrt(2) (model), the "
               f"atomic-kernel q-Laplace output's pole set is EXACTLY "
               f"xi*(1-p)/u · qt^Z (identity xi*/t = xi*(1-p)/u·"
               f"qt^(2m-j) exact; exponent set j-2m covers Z; all "
               f"masses positive so residues cannot cancel; every "
               f"computed pole lands on the lattice, rel < 1e-30, for "
               f"u = 1, {U_GENERIC}, qt^(1/2)). The map u |-> "
               f"[lattice class] is a FREE TRANSITIVE circle action "
               f"(class shift = -log_qt u exactly), so ONE known "
               f"output pole location selects a UNIQUE u mod qt^Z: "
               f"the solved u places a pole on x_tgt = {X_TGT} to "
               f"< 1e-30 while a qt^0.37-detuned u misses by 0.37 of "
               f"a step. KSel-1 is well-formed and uniquely selective "
               f"IN FORM — given an input-side singularity and an "
               f"output-side datum")
    wb.add_data("k2_classes_frac_log_qt",
                {k: mp.nstr(v, 12) for k, v in classes.items()})
    return classes


# ---------------------------------------------------------------- Block K3

def block_k3_real_data(wb: WitnessBuilder, q_name: str,
                       q_str: str) -> dict:
    """K3 at one q: growth class of the q-Borel-side carrier (entire)
    and the finite radius r* of the balanced period series (the
    output-side positive-axis singularity)."""
    q0 = mpf(q_str)
    S, qf = build_carrier(q0, N_REC + 1)
    b = [None] + [S[n] / qf[n] for n in range(1, N_REC + 2)]

    def g(n: int) -> mpf:
        return (b[n + 1] / b[n]) * q0 ** (mpf(2 * n + 1) / 4)

    def ratB(n: int) -> mpf:
        # exact identity: B^bal_{n+1}/B^bal_n = g(n)·q^{1/4-n}·[n]_q
        return g(n) * q0 ** (mpf(1) / 4 - n) * mp_qint(q0, n)

    # (0) q = 1 confluence of the carrier: the recurrence with [k]_1 = k
    # is the involution recurrence (exact integers).
    I = involution_numbers(62)
    S1 = [sp.Integer(1), sp.Integer(1)]
    for n in range(60):
        S1.append(S1[-1] + (n + 1) * S1[-2])
    assert all(S1[n] == I[n] for n in range(62))

    # (i) exact per-n identity ratB(n) == B^bal_{n+1}/B^bal_n (code
    # self-consistency, pure algebra at working precision).
    worst_id = mpf(0)
    for n in (10, 100, 300):
        Bb_n = b[n] * mp_balanced_normalizer(q0, qf, n)
        Bb_n1 = b[n + 1] * mp_balanced_normalizer(q0, qf, n + 1)
        worst_id = max(worst_id, abs(ratB(n) / (Bb_n1 / Bb_n) - 1))
    assert worst_id < mpf("1e-40"), worst_id

    # (ii) phi entire: parity-resolved Cauchy convergence of g(n)
    # (b^q_n ~ q^{-n^2/4}·rho_phi^{-n}·(two-cycle fluctuation)).
    cauchy_g = max(abs(g(N_REC) / g(N_REC - 2) - 1),
                   abs(g(N_REC - 1) / g(N_REC - 3) - 1))
    assert cauchy_g < mpf("1e-8"), cauchy_g
    assert g(N_REC) > 0
    # direct shadow of infinite radius: |b_n|^{1/n} -> 0
    root_b = b[N_REC] ** (mpf(1) / N_REC)
    assert root_b < mpf("0.01"), root_b
    rho_phi_even = 1 / g(N_REC)
    rho_phi_odd = 1 / g(N_REC - 1)

    # (iii) r*: two-cycle geometric mean of the balanced-series ratio;
    # Cauchy-converged; all coefficients positive (Pringsheim).
    r_star = 1 / mpsqrt(ratB(N_REC - 1) * ratB(N_REC))
    r_star_prev = 1 / mpsqrt(ratB(N_REC - 101) * ratB(N_REC - 100))
    cauchy_r = abs(r_star / r_star_prev - 1)
    assert cauchy_r < mpf("1e-6"), cauchy_r
    assert all(b[n] > 0 for n in range(1, N_REC + 1))
    # divergence/convergence bracketing of the wall on the positive axis
    def Bb(n: int) -> mpf:
        return b[n] * mp_balanced_normalizer(q0, qf, n)
    x_lo, x_hi = mpf("0.9") * r_star, mpf("1.1") * r_star
    assert Bb(N_REC) * x_lo ** N_REC < Bb(300) * x_lo ** 300      # decays
    assert Bb(N_REC) * x_hi ** N_REC > Bb(300) * x_hi ** 300      # grows

    wb.add_assertion(
        f"k3_fibre_growth_and_radius_{q_name}",
        computed=mp.nstr(max(cauchy_g, cauchy_r), 5), expected="0",
        tolerance=1e-6,
        source=f"q = {q_name} ({mp.nstr(q0, 12)}...), 60 dps, "
               f"n <= {N_REC} via the exact q-telephone recurrence "
               f"(= involution numbers at q = 1, checked exact): "
               f"(a) the q-Borel-side carrier b^q_n = S(n)/[n]_q! has "
               f"g(n) = (b_(n+1)/b_n)·q^((2n+1)/4) two-cycle-"
               f"converged (Cauchy {mp.nstr(cauchy_g, 3)}) to "
               f"1/rho_phi with rho_phi ~ "
               f"{mp.nstr((rho_phi_even + rho_phi_odd) / 2, 8)} => "
               f"b^q_n ~ q^(-n^2/4)·rho_phi^(-n): phi(xi) = "
               f"sum b^q_n xi^n is ENTIRE (theta growth class) — NO "
               f"finite q-Borel-plane singularity exists at the fibre "
               f"for input-side singularity matching; (b) the "
               f"balanced period series sum b^q_n·N^bal(n)·x^n is "
               f"GEOMETRIC class with radius r* = "
               f"{mp.nstr(r_star, 10)} (two-cycle geometric mean, "
               f"Cauchy {mp.nstr(cauchy_r, 3)}; exact per-n identity "
               f"ratB(n) = g(n)·q^(1/4-n)·[n]_q asserted < 1e-40; "
               f"wall bracketed: terms decay at 0.9·r*, grow at "
               f"1.1·r*), with ALL coefficients positive => "
               f"Pringsheim: the output-side singularity is ON the "
               f"positive real axis at x* = r*. NEW measured datum "
               f"(scope-(a)); at q = 1 the same recurrence gives the "
               f"known radius-0 Gevrey-1/2 divergence — the finite "
               f"radius is a fibre-level phenomenon")
    return {
        "r_star": mp.nstr(r_star, 14),
        "r_star_parity_pair": [mp.nstr(1 / ratB(N_REC - 1), 14),
                               mp.nstr(1 / ratB(N_REC), 14)],
        "rho_phi_parity_pair": [mp.nstr(rho_phi_odd, 14),
                                mp.nstr(rho_phi_even, 14)],
        "g_cauchy": mp.nstr(cauchy_g, 3),
        "r_cauchy": mp.nstr(cauchy_r, 3),
    }


# ---------------------------------------------------------------- Block K4

def block_k4_selection_verdict(wb: WitnessBuilder) -> None:
    """K4 (q = 1.2): Tonelli rearrangement — the kernel output on the
    positive axis equals the u-independent balanced series for every u;
    the output wall is exactly u-invariant; verdict recorded."""
    _ok: list[bool] = []
    q0 = mpf("1.2")
    qt = mpsqrt(q0)
    NTR = 30
    S, qf = build_carrier(q0, NTR + 2)
    b = [None] + [S[n] / qf[n] for n in range(1, NTR + 2)]
    xx = mpf("0.3")
    series = sum(b[n] * mp_balanced_normalizer(q0, qf, n) * xx ** n
                 for n in range(1, NTR + 1))
    at_j, ms_j, _ = jackson_factor(q0, NTR)
    worst = mpf(0)
    for uu in (mpf(1), mpf(U_GENERIC), qt ** mpf("0.5")):
        _, at_t, ms_t, _ = theta_translate_factor(q0, uu, NTR)
        dsum = mpf(0)
        # full nested double sum over kernel atoms (NO mass floor — the
        # theta/Jackson windows are sized for the moment order NTR)
        for tj, cj in zip(at_j, ms_j):
            for tt, ct in zip(at_t, ms_t):
                t = tj * tt
                # fhat_N(x·t)/t with fhat_N = sum_{n<=N} b_n xi^n (n>=1)
                xi = xx * t
                acc = b[NTR]
                for n in range(NTR - 1, 0, -1):     # Horner
                    acc = acc * xi + b[n]
                dsum += cj * ct * acc * xi / t
        worst = max(worst, abs(dsum / series - 1))
    _ok.append(bool(worst < TOL_MEAS))
    assert _ok[-1], worst
    wb.add_assertion(
        "k4_output_positive_axis_u_invariant", computed=mp.nstr(worst, 5),
        expected="0", tolerance=TOL_MEAS,
        source=f"q = 1.2, 60 dps, truncation N = {NTR}, x = 0.3: the "
               f"atomic-kernel double sum sum_a c_a·fhat_N(x t_a)/t_a "
               f"equals the u-INDEPENDENT truncated balanced series "
               f"sum b^q_n·N^bal(n)·x^n to rel < 1e-25 for u = 1, "
               f"{U_GENERIC}, and qt^(1/2) (extends the REP R3 "
               f"falsifier per-u). Since every term is positive for "
               f"x > 0, Tonelli rearrangement makes this exact at the "
               f"function level: the kernel output on the positive "
               f"real axis IS the u-independent series wherever it "
               f"converges and +inf beyond r* — for EVERY u. The "
               f"positive-axis output singularity x* = r* (K3b) is "
               f"therefore EXACTLY u-invariant, by the same reindex "
               f"mechanism that makes the moments u-invariant")
    wb.add_assertion(
        "k4_ksel1_verdict_continuum_survives", computed=all(_ok),
        expected=True, tolerance=TOL_EXACT,
        source="VERDICT (scope-(a)): the u-translate CONTINUUM "
               "SURVIVES KSel-1 (singularity matching). The principle "
               "is well-formed and uniquely selective in form (K2: an "
               "input Borel-plane pole + one output pole datum pin a "
               "unique u mod qt^Z, free transitive circle action), "
               "but the QOU binding data fail both hypotheses: "
               "(input) the fibre q-Borel-side carrier is ENTIRE — "
               "b^q_n ~ q^(-n^2/4)·rho_phi^(-n), no finite "
               "singularity to match (K3a, both q0 pins); (output) "
               "the only corpus-computable output singularity — the "
               "positive-axis wall at x* = r* ~ 0.34042 (q0), newly "
               "measured in K3b — is EXACTLY u-invariant by Tonelli + "
               "moment u-invariance (K4); and the only independently-"
               "known corpus singularity datum (xi = 1/sqrt(2)) lives "
               "at q = 1 in the classical level-1/2 plane, where the "
               "kernel class is already the Carleman singleton and u "
               "is not a parameter (K1 tier table). No unique u is "
               "selected; no fit; nothing wired; the (REP) canonical-"
               "choice premise stays open. A future selection would "
               "need an OFF-positive-axis output datum (e.g. the "
               "negative-axis / complex pole lattice of the analytic "
               "continuation past r*, which IS u-dependent per K2's "
               "mechanism) — not currently in the corpus")


# ---------------------------------------------------------------- Block K5

def block_k5_crosschecks(wb: WitnessBuilder,
                         k2_classes: dict) -> None:
    """K5 (q = 1.2): balanced moments at the self-dual points; circle
    structure; reflection self-duality; the half-step offset between
    the two self-dual pole-lattice classes."""
    q0 = mpf("1.2")
    qt = mpsqrt(q0)
    _, _, mom_j = jackson_factor(q0, N_MOM)
    # (i) balanced moments u-invariant, including both sigma-self-dual
    # points u = 1 and u = qt^{1/2} (and the generic u).
    worst = mpf(0)
    for uu in (mpf(1), mpf(U_GENERIC), qt ** mpf("0.5")):
        _, _, _, mom_t = theta_translate_factor(q0, uu, N_MOM)
        for k in range(N_MOM + 1):
            # N^bal(k+1) = q^{-k(k-1)/4}·[k]_q!
            full = mom_j[k] * mom_t[k]
            nbal = q0 ** (-mpf(k * (k - 1)) / 4)
            for jx in range(1, k + 1):
                nbal *= mp_qint(q0, jx)
            worst = max(worst, abs(full / nbal - 1))
    assert worst < TOL_50, worst
    # (ii) circle structure: mu_{qt·u} = mu_u as normalized measures.
    uu = mpf(U_GENERIC)
    _, at_a, ms_a, _ = theta_translate_factor(q0, uu, N_MOM)
    _, at_b, ms_b, _ = theta_translate_factor(q0, qt * uu, N_MOM)
    assert measure_eq(at_a, ms_a, at_b, ms_b, mpf(TOL_MEAS))
    # (iii) reflection sigma: s -> qt^{-1}/s: sigma(mu_u) = mu_{1/u};
    # self-dual exactly at u = 1 and u = qt^{1/2}.
    _, at_u, ms_u, _ = theta_translate_factor(q0, uu, N_MOM)
    at_ref = [qt ** (-1) / a for a in at_u]
    _, at_inv, ms_inv, _ = theta_translate_factor(q0, 1 / uu, N_MOM)
    assert measure_eq(at_ref, ms_u, at_inv, ms_inv, mpf(TOL_MEAS))
    for uself in (mpf(1), qt ** mpf("0.5")):
        _, at_s, ms_s, _ = theta_translate_factor(q0, uself, N_MOM)
        at_s_ref = [qt ** (-1) / a for a in at_s]
        assert measure_eq(at_s_ref, ms_s, at_s, ms_s, mpf(TOL_MEAS))
    # (iv) the two self-dual points' MODEL pole-lattice classes differ
    # by exactly half a qt-step (recorded, not interpreted).
    d = abs(k2_classes["1"] - k2_classes["selfdual_half"])
    d = min(d, 1 - d)
    off = abs(d - mpf("0.5"))
    assert off < TOL_MEAS, off
    wb.add_assertion(
        "k5_selfdual_moments_circle_and_halfstep",
        computed=mp.nstr(max(worst, off), 5), expected="0",
        tolerance=TOL_50 * 1e5,
        source="q = 1.2, 60 dps: (i) the full kernel's ds/s-moments "
               "equal N^bal at u = 1, 1.3, AND the sigma-self-dual "
               "point u = qt^(1/2) (rel < 1e-30 — u-invariance holds "
               "at the KSel-3 maximal-symmetry candidates, as forced "
               "by the REP R4a reindex identity); (ii) the family is "
               "a genuine circle: mu_(qt·u) = mu_u as normalized "
               "measures (< 1e-25); (iii) sigma: s -> qt^(-1)/s maps "
               "mu_u -> mu_(1/u) and fixes exactly the classes u = 1 "
               "and u = qt^(1/2) (measure equalities < 1e-25); "
               "(iv) the two self-dual points' model pole-lattice "
               "classes differ by exactly HALF a qt-step "
               "(|frac - 1/2| < 1e-25). RECORDED, NOT INTERPRETED: "
               "KSel-1 selects no u (K4), so no selected-u-vs-self-"
               "dual coincidence exists to evaluate; the half-step "
               "offset is the exact discriminant a future measured "
               "output pole lattice would use to split the two "
               "KSel-3 symmetry-maximal candidates")


def main() -> int:
    set_compute_dps(60)
    wb = WitnessBuilder("ksel1-singularity-selection",
                        engine="sympy+mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "KSel-1 (singularity matching) on the (REP) canonical-choice "
        "continuum (bean qou-334t; audit-only, scope-(a), NO FIT, "
        "nothing wired; machinery reused with attribution from "
        "rep_jackson_identification_probe / bean qou-u5p0). K1: the "
        "corpus's independently-known binding Borel singularity datum "
        "re-pinned with tiers — q = 1 level-1/2 plane, xi* = "
        "1/sqrt(2) on the positive real axis (Pringsheim exact; class "
        "Lean-proved Gevrey-1/2; location measured scope-(a)); at q0 "
        "the corpus already showed that classical plane collapses. "
        "K2 (model leg): the exact map u |-> output pole set derived "
        "and verified — an input Borel-plane pole at xi* puts the "
        "atomic-kernel q-Laplace output's poles EXACTLY on "
        "xi*(1-p)/u·qt^Z (positivity forbids residue cancellation); "
        "u |-> [lattice class] is a free transitive circle action, "
        "so one output-pole datum would select a UNIQUE u mod qt^Z: "
        "KSel-1 is uniquely selective IN FORM. K3 (q = 1.2 + both q0 "
        "pins, n <= 400): the REAL binding data fail both hypotheses "
        "— the q-Borel-side carrier b^q_n = S(n)/[n]_q! satisfies "
        "b^q_n ~ q^(-n^2/4)·rho_phi^(-n) (two-cycle-converged), so "
        "phi is ENTIRE (no input singularity to match); the balanced "
        "period series is GEOMETRIC with newly measured radius r* "
        "(~0.46807 at q = 1.2; ~0.34039 at both q0 pins), all "
        "coefficients positive => the output-side singularity is the "
        "positive-axis wall x* = r*. K4: by Tonelli (positivity) + "
        "moment u-invariance the kernel output on the positive axis "
        "IS the u-independent series for EVERY u (verified < 1e-25 "
        "at u = 1, 1.3, qt^(1/2)) — the wall x* = r* is EXACTLY "
        "u-invariant. VERDICT: the u-continuum SURVIVES KSel-1 — no "
        "unique u; the selection axis is degenerate on the positive "
        "axis for the same reindex reason the moments are u-"
        "invariant, and has no input-side referent (phi entire). K5: "
        "balanced moments hold at the sigma-self-dual points u = 1 "
        "and u = qt^(1/2) (u-invariance asserted); the family is a "
        "circle (mu_(qt·u) = mu_u); the two self-dual points' model "
        "pole-lattice classes differ by exactly half a qt-step — "
        "recorded, not interpreted (no selected u exists for a "
        "KSel-3 coincidence). Nothing here proves or refutes the "
        "conjecture.")
    wb.set_audit_only(
        "docs/audits/2026-08-01-ksel1-singularity-selection.md")

    xi_star = 1 / mpsqrt(2)

    block_k1_corpus_datum(wb)
    print("K1: corpus singularity datum (q=1 level-1/2, xi*=1/sqrt(2), "
          "positive axis) re-pinned + tiered.")
    k2_classes = block_k2_pole_lattice_map(wb, xi_star)
    print("K2: exact map u -> pole lattice xi*(1-p)/u·qt^Z; free "
          "transitive circle action; uniquely selective IN FORM.")
    r_data = {}
    for name, qs in (("test", "1.2"), ("muon", Q0_MUON_STR),
                     ("proton", Q0_PROTON_STR)):
        r_data[name] = block_k3_real_data(wb, name, qs)
        print(f"K3[{name}]: phi ENTIRE (no input singularity); balanced "
              f"series radius r* = {r_data[name]['r_star']}.")
    block_k4_selection_verdict(wb)
    print("K4: positive-axis output wall EXACTLY u-invariant (Tonelli); "
          "VERDICT: continuum survives — KSel-1 selects no u.")
    block_k5_crosschecks(wb, k2_classes)
    print("K5: moments hold at self-dual points; circle structure; "
          "half-step offset between the two self-dual classes.")

    wb.add_data("q0_pins", {
        "muon": Q0_MUON_STR, "proton": Q0_PROTON_STR,
        "source": "computations/q-pinning-50-digit.witness.json (muon, "
                  "canonical 3-CAL layer); qou_substrate.constants."
                  "Q_50_DIGIT_STR (proton, precision layer)"})
    wb.add_data("balanced_series_radius_r_star", r_data)
    wb.add_data("selection_verdict", {
        "verdict": "continuum-survives",
        "unique_u": None,
        "mechanism": "input side: q-Borel carrier entire at q > 1 (no "
                     "singularity to match); output side: positive-"
                     "axis wall x* = r* exactly u-invariant (Tonelli "
                     "+ the REP R4a reindex identity); the q = 1 "
                     "datum xi = 1/sqrt(2) lives where the kernel "
                     "class is the Carleman singleton",
        "what_would_select": "an off-positive-axis output datum (the "
                             "pole lattice of the continuation past "
                             "r*) or a fibre-level input singularity "
                             "— neither currently in the corpus; "
                             "given either, K2's free transitive "
                             "action pins u uniquely mod qt^Z",
    })
    wb.save()
    print("\nwitness saved; all assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
