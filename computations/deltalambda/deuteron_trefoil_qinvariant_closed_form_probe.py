#!/usr/bin/env python3
"""
Deuteron binding as a closed-form symbolic q-invariant of the sigma_1^3 trefoil.

PROOF-TIER derive-then-check (anti-fit): the deuteron 5.853x binding deficit
collapsed to ONE object -- the transverse NA-Stokes surface-curvature term on
the sigma_1^3 trefoil Seifert surface = first-order per-bond amplitude Delta^1 g
= the fitted C_knot = 5.853.  QUESTION: does a closed-form symbolic q-invariant
of the trefoil (torus knot T(2,3)) at the canonical q0 reproduce C_knot = 5.853
with ZERO free parameters?

Target is LOCKED before compute.  B_AME is used only as a diagnostic ratio,
never inverted.  Every candidate is tagged with its number of free knobs
(0 = canonical/parameter-free; 1 = level/color/normalization free -> a hit is a
FIT, not a derivation; numerology = q0^k coincidence).

The trefoil is the torus knot T(2,3): NON-hyperbolic, so volume/dilog
(Bloch-Wigner) routes give 0 and are excluded a priori (AGENTS.md sec 7b).

Canonical conventions (verified against committed witness):
  A = sqrt(q0)                       ("A" = Kauffman/skein variable)
  z_markov = q^3/(q^2 + 1)           ( convention D, 0.6126880... )
    CORRECTED 2026-08-28: this read 1/(A + 1/A) = z_C and cited the
    committed 0.49932 as its authority.  Those were free-neutron-decay's
    constants_at_q0, corrected to D in the same tranche, so the cited
    authority no longer says that.  Convention D is canonical (owner
    ruling 2026-08-15 R1).
  s_skein  = A - 1/A                 ( committed 0.10439... )
  Hecke:  sigma^2 = s*sigma + 1      (from (sigma-A)(sigma+A^{-1})=0)
"""
import mpmath as mp

mp.mp.dps = 60

# ---------------------------------------------------------------------------
# 0. Canonical constants (LOCKED)
#
# ANCHOR NOTE (2026-08-29).  "LOCKED" above refers to the anti-fit discipline
# -- the target is fixed before compute -- NOT to the anchor.  The q0 below is
# the FROZEN MUON literal, hardcoded: it never consults `q_parameter`, so the
# stem's absence from `q0_anchor_manifest.json` does NOT mean a run resolves to
# proton.  It cannot; nothing here asks.
#
# This file is one of the 248 UNDECLARED hardcodes the corpus's own
# `computations/audits/q0_hardcoded_pin_audit.py` reports.  Re-pinning them is
# the tracked migration (bean qou-1c4y), a scoped sweep -- deliberately NOT
# done here, and NOT to be done file-by-file as a drive-by.
#
# For whoever runs that sweep: the verdict of THIS probe is robust to the
# change.  Proton vs frozen muon is 11.5 ppb in q0 (21.9 ppb in z_markov,
# since d ln z / d ln q = 3 - 2q^2/(q^2+1) = 1.896 at q0), and the verdict
# turns on a 0.6904 % miss -- five orders of magnitude larger.  Every number
# printed below moves in the 8th significant figure; the honest-negative
# stands.
# ---------------------------------------------------------------------------
# q0 RESOLVED, not frozen (2026-08-29, bean qou-1c4y). This was the literal
# 1.10997859555733471..., the SUPERSEDED muon pin A -- it stopped being the
# muon anchor when PR #5500 re-derived that anchor to CODATA-2022. A frozen
# literal cannot follow an anchor move, so the witness kept recording A under
# the label "muon" and the anchor gate scored it Q0_FLIP; re-running could not
# clear it, because the producer was the source of the stale number. It now
# resolves the PROTON pin per the owner directive of 2026-08-15 ("we want
# proton unless for an explicit reason ... otherwise pin proton").
import sys as _sys, pathlib as _pl  # noqa: E402
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401, E402

from substrate.q_parameter import Q_50_DIGIT_STR as _Q0_RESOLVED  # noqa: E402 -- q0 RESOLVED, not frozen (qou-1c4y)

q0 = mp.mpf(_Q0_RESOLVED)
A = mp.sqrt(q0)                      # skein variable sqrt(q)
z = q0 ** 3 / (q0 ** 2 + 1)          # Markov parameter, convention D
s = A - 1 / A                        # skein s (committed s_skein)

# quantum integers [n]_q = (q^{n/2}-q^{-n/2})/(q^{1/2}-q^{-1/2})  (balanced)
def qint(n):
    return (A**n - A**(-n)) / (A - 1 / A)

# balanced quantum integer in q (not sqrt q): [n]_{q} = (q^n - q^-n)/(q-q^-1)
def qint_q(n):
    return (q0**n - q0**(-n)) / (q0 - 1 / q0)

# CODATA / AME  (diagnostic only)
m_e = mp.mpf("0.51099895069")        # MeV
B_D = mp.mpf("2.22452")              # MeV, AME2020 deuteron binding
S_D = mp.mpf("0.7438")               # committed |S(D)| Wenzl-signed Markov sum
first_order = m_e * S_D              # = 0.38008 MeV (DT-count derived, #4601)

C_target = B_D / first_order         # LOCKED target multiplier
BDoverme = B_D / m_e                 # alternate: surface applied to m_e directly

print("=" * 78)
print("LOCKED TARGETS (anti-fit, computed before candidate compute)")
print("=" * 78)
print(f"q0            = {mp.nstr(q0, 20)}")
print(f"A = sqrt(q0)  = {mp.nstr(A, 20)}")
print(f"z_markov      = {mp.nstr(z, 20)}   (convention D)")
print(f"s_skein       = {mp.nstr(s, 20)}   (committed 0.10439...)")
print(f"m_e*|S|       = {mp.nstr(first_order, 12)} MeV (first-order)")
print(f"C_knot TARGET = {mp.nstr(C_target, 12)}   [surface multiplier]")
print(f"B_D/m_e       = {mp.nstr(BDoverme, 12)}     [alt target: surface x sum]")
print()

results = []  # (name, value, knobs, note)

def add(name, val, knobs, note=""):
    results.append((name, mp.mpf(val), knobs, note))

# ---------------------------------------------------------------------------
# 1. Chebyshev / Markov-trace closed form for T(2,n) = closure of sigma_1^n
#    sigma^n = a_n(s) sigma + a_{n-1}(s),  a_{n+1}=s a_n + a_{n-1}, a_1=1,a_0=0
#    tr_M(sigma^n) = a_n z + a_{n-1}   (canonical surface state-sum, 0 knobs)
# ---------------------------------------------------------------------------
def cheb_a(n):
    a_prev, a_cur = mp.mpf(0), mp.mpf(1)   # a_0, a_1
    if n == 0:
        return mp.mpf(0)
    for _ in range(n - 1):
        a_prev, a_cur = a_cur, s * a_cur + a_prev
    return a_cur

def trM_torus(n):
    return cheb_a(n) * z + cheb_a(n - 1)

trM_tref = trM_torus(3)               # sigma_1^3 trefoil raw Markov trace
add("tr_M(sigma_1^3) raw Markov trace", trM_tref, 0, "canonical surface state-sum")

# Jones normalization from Markov trace (Jones '87):
#   for beta in B_2, writhe w = 3 (sigma_1^3), n_strands = 2
#   V_L = (-(A^2+A^-2))^{n-1} * (-A^3)^{-w} * (tr_M / z_stab?) ...
# We give the standard *reduced* and *unreduced* Jones of the trefoil directly
# in closed polynomial form (both chiralities, both variable conventions).
t = q0
# right-handed trefoil  V = -t^-4 + t^-3 + t^-1 ; left  V = -t^4 + t^3 + t
add("Jones V_3_1(t=q0) right", -t**-4 + t**-3 + t**-1, 0)
add("Jones V_3_1(t=q0) left",  -t**4 + t**3 + t,        0)
t2 = q0**2
add("Jones V_3_1(t=q0^2) right", -t2**-4 + t2**-3 + t2**-1, 0, "t=q^2 convention")
add("Jones V_3_1(t=q0^2) left",  -t2**4 + t2**3 + t2,        0, "t=q^2 convention")
# unreduced (multiply by quantum dim [2]_q of the fundamental)
d2 = q0 + 1/q0
add("unreduced Jones [2]_q * V_right", d2*(-t**-4 + t**-3 + t**-1), 0)
add("unreduced Jones [2]_q * V_left",  d2*(-t**4 + t**3 + t),        0)

# ---------------------------------------------------------------------------
# 2. Quantum integers / dims / factorials  (0 knobs)
# ---------------------------------------------------------------------------
for n in range(2, 13):
    add(f"[{n}]_q  (balanced, sqrt-q)", qint(n), 0)
for n in range(2, 8):
    add(f"[{n}]_q  (balanced, q)", qint_q(n), 0)
fact = mp.mpf(1)
for n in range(1, 7):
    fact *= qint(n)
    if n >= 3:
        add(f"[{n}]_q! (sqrt-q)", fact, 0)

# ---------------------------------------------------------------------------
# 3. HOMFLY / Alexander of trefoil (0 knobs, framework variables)
#    Alexander Delta_3_1(t) = t - 1 + t^-1
# ---------------------------------------------------------------------------
add("Alexander Delta(q0) = q-1+1/q", q0 - 1 + 1/q0, 0)
add("Alexander Delta(q0^2)", q0**2 - 1 + q0**-2, 0)

# ---------------------------------------------------------------------------
# 4. Colored Jones J_N(trefoil)  (1 knob = color N -> hit is a FIT)
#    J_N(T(2,3)) via Habiro / Rosso-Jones; use the cyclotomic sum.
#    Reduced colored Jones normalized J_1 = 1.  Use the standard closed form
#    for the trefoil:  J_N = q^{1-N} sum_{k=0}^{N-1} q^{-k N} prod_{j=1}^{k}(1-q^{j-N})
# ---------------------------------------------------------------------------
def colored_jones_trefoil(N, qq):
    # Habiro's formula for the (left) trefoil, normalized J_1=1
    total = mp.mpf(0)
    for k in range(0, N):
        prod = mp.mpf(1)
        for j in range(1, k + 1):
            prod *= (1 - qq**(j - N)) * (1 - qq**(j + N))  # (q^{N};..)-type; approx
        total += qq**(-k * (k + 2)) * prod  # Habiro trefoil: sum q^{-k(k+2)}(q^{1-N};q)_k(q^{1+N};q)_k
    return total
for N in range(2, 6):
    try:
        add(f"colored Jones J_{N}(trefoil, q0)", colored_jones_trefoil(N, q0), 1, "color N free -> FIT")
    except Exception as e:
        pass

# ---------------------------------------------------------------------------
# 5. Verlinde dim of SU(2)_k TQFT on genus-1 surface  (1 knob = level k -> FIT)
#    Seifert surface of trefoil is genus 1.  dim V_{g=1} = number of primaries
#    = k+1  (trivial for torus); genus-1 partition = k+1.  Include Verlinde
#    S-matrix weighted sums for completeness.
# ---------------------------------------------------------------------------
for k in range(1, 12):
    add(f"Verlinde dim genus-1 SU(2)_{k} = k+1", mp.mpf(k + 1), 1, "level k free -> FIT")

# ---------------------------------------------------------------------------
# 6. q0^k numerology  (already flagged coincidence in #4556 sec 4)
# ---------------------------------------------------------------------------
for k in range(1, 21):
    add(f"q0^{k}", q0**k, 0, "numerology (see #4556 s4)")

# ---------------------------------------------------------------------------
# 7. Torus-knot trace RATIOS (F3 surface-curvature Chebyshev structure)
# ---------------------------------------------------------------------------
for (a, b) in [(9, 3), (5, 2), (5, 3), (6, 3), (3, 2), (9, 6)]:
    add(f"tr_M(T(2,{a}))/tr_M(T(2,{b}))", trM_torus(a) / trM_torus(b), 0, "knot-pair selection = hidden knob")

# ---------------------------------------------------------------------------
# CLOSENESS ANALYSIS vs both targets
# ---------------------------------------------------------------------------
def report(target, label):
    print("=" * 78)
    print(f"CLOSENESS to {label} = {mp.nstr(target,12)}")
    print("=" * 78)
    rows = []
    for (name, val, knobs, note) in results:
        if val == 0:
            continue
        err = abs(val - target) / abs(target)
        rows.append((err, name, val, knobs, note))
    rows.sort()
    print(f"{'rel.err':>12}  {'knobs':>5}  {'value':>16}  name")
    for (err, name, val, knobs, note) in rows[:18]:
        tag = "" if err > mp.mpf("1e-4") else "  <== EXACT-ish"
        n = f" [{note}]" if note else ""
        print(f"{mp.nstr(err,4):>12}  {knobs:>5}  {mp.nstr(val,12):>16}  {name}{n}{tag}")
    print()

report(C_target, "C_knot (surface multiplier)")
report(BDoverme, "B_D/m_e (surface x sum)")

# ---------------------------------------------------------------------------
# WITNESS emission
# ---------------------------------------------------------------------------
import json, hashlib, os
best_zero = min(
    ((abs(v - C_target) / C_target, n, v) for (n, v, k, _) in results if k == 0 and v != 0),
    key=lambda r: r[0],
)
best_struct = min(  # best 0-knob that is NOT q0^k numerology
    ((abs(v - C_target) / C_target, n, v)
     for (n, v, k, note) in results if k == 0 and v != 0 and "numerology" not in note),
    key=lambda r: r[0],
)
src = open(__file__, "rb").read()
witness = {
    # Emitted BY THE PRODUCER.  These three were backfilled into the committed
    # witness by a provenance tool, not written here, so every regeneration
    # silently dropped them -- the qou-4un2 provenance-loss class.  q0 above is
    # RESOLVED from substrate.q_parameter, not frozen; the anchor is recorded as
    # what it actually is rather than inferred from a call site.
    #
    # These three said "muon" until 2026-08-30, describing the hard-coded muon
    # literal that the qou-1c4y migration (2026-08-29) had already DELETED four
    # lines up.  That same edit introduced the bare-name import with no sys.path
    # bootstrap, so the producer could not run and nothing ever exercised the
    # contradiction it had just created.
    "q0Anchor": "proton",
    "q0Value": mp.nstr(q0, 50),
    "q0AnchorReason": (
        "emitted by the producer: q0 is RESOLVED from "
        "substrate.q_parameter.Q_50_DIGIT_STR, which returns the experimental "
        "(proton) pin per the owner directive of 2026-08-15; this probe holds "
        "no q0 literal"),
    "schema": "witness/v1",
    "computation": "deuteron_trefoil_qinvariant_closed_form_probe",
    "description": "Derive-then-check: does a 0-parameter closed-form q-invariant of the "
                   "sigma_1^3 trefoil (T(2,3)) at q0 reproduce the deuteron C_knot=5.853? "
                   "VERDICT: honest negative -- no parameter-free hit within exactness threshold.",
    "q0_anchor": "proton",
    "free_parameters": 0,
    "b_ame_role": "diagnostic-ratio-only-never-inverted",
    "targets": {
        "C_knot_surface_multiplier": mp.nstr(C_target, 30),
        "B_D_over_m_e": mp.nstr(BDoverme, 30),
    },
    "inputs": {
        "q0": mp.nstr(q0, 50),
        "z_markov": mp.nstr(z, 30),
        "s_skein": mp.nstr(s, 30),
        "m_e_MeV": str(m_e), "B_D_MeV": str(B_D), "S_D": str(S_D),
    },
    "best_0knob_candidate": {
        "name": best_zero[1], "value": mp.nstr(best_zero[2], 20),
        "rel_err": mp.nstr(best_zero[0], 6),
    },
    "best_0knob_structural_non_numerology": {
        "name": best_struct[1], "value": mp.nstr(best_struct[2], 20),
        "rel_err": mp.nstr(best_struct[0], 6),
    },
    "exactness_threshold_rel_err": "1e-6",
    "verdict": "honest-negative: no 0-parameter closed-form q-invariant of the trefoil "
               "reproduces C_knot to exactness; nearest 0-knob is q0^17 (0.69%, ruled-out "
               "numerology #4556 s4); nearest structural single [3]_q! is 3.0% off; "
               "objects landing within ~2.5% carry a free level/color knob (= fit).",
    "scriptHash": hashlib.sha256(src).hexdigest()[:12],
}
outp = os.path.join(os.path.dirname(__file__),
                    "deuteron_trefoil_qinvariant_closed_form.witness.json")
with open(outp, "w") as f:
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    # q0_anchor was `False`, i.e. "this witness carries no q0-dependent field".
    # Untrue: this producer reads q0 and records it, so the false declaration
    # DELETED the anchor stamp on every run, converting a visible Q0_FLIP into a
    # silent Q0_ANCHOR_MISSING (bean qou-1c4y). Resolving is the default.
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None)
    json.dump(witness, f, indent=2)
print(f"\nwitness -> {outp}")
print(f"VERDICT: {witness['verdict']}")

# ---------------------------------------------------------------------------
# Best 0-knob candidate + honest verdict data
# ---------------------------------------------------------------------------
zero_knob = [(abs(v - C_target)/C_target, n, v) for (n, v, k, _) in results if k == 0 and v != 0]
zero_knob.sort()
print("=" * 78)
print("BEST 0-KNOB (parameter-free) CANDIDATE vs C_knot target:")
best = zero_knob[0]
print(f"  {best[1]} = {mp.nstr(best[2],12)}  (rel.err {mp.nstr(best[0],4)})")
print(f"  -> {mp.nstr(best[0]*100,4)} % off.  A parameter-free HIT requires rel.err < ~1e-6.")
print("=" * 78)
