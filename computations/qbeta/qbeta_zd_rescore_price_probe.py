#!/usr/bin/env python3
"""qou-99qc item (iii): price the dashboard re-score on the RULED z_D base.

# Ref: .beans/qou-99qc--...md  (OWNER RULING 2026-09-08: eps := tr at z_D)
# Ref: computations/per_observable_100x_status.py  (the L2 dashboard producer)
# Ref: docs/audits/2026-09-05-qbeta-functional-decision-options.md  (the cells)

WHY THIS EXISTS.  The owner ruled on 2026-09-08 that `eps` in the Q_beta ansatz
is the Markov trace at `z_D = q^3/(q^2+1)`.  Consequence (iii) of that ruling --
re-scoring the dashboard rows Q_beta / m_n / Delta_pn on the ruled base -- has
been declined in two sessions as "ask-before-change", which is correct: it moves
the L2 headline.  But it was declined WITHOUT THE NUMBERS, so the owner has been
asked to authorise a change whose size nobody had measured.  This measures it.

IT CHANGES NOTHING.  No witness is re-scored, no producer is edited, no row is
moved.  Measuring is not changing (AGENTS.md).

THE CALIBRATION THAT MAKES IT TRUSTWORTHY, and it can fail.  CHECK 2 reproduces
the dashboard's CURRENT m_n and Delta_pn rows from its CURRENT Q_beta via the
producer's own stated relation `m_n = m_p(substrate) + Q_beta + m_e`.  If that
does not reproduce, the re-scored numbers below would be about my arithmetic
rather than about the dashboard, and the check says so instead of proceeding.

SCOPE, and it is the load-bearing caveat.  The z_D figure is the BASE -- zero
c_k rungs.  No ladder has been derived on an admissible base (qou-cds1, blocked
on the phase qou-pdix).  On the z=1 base the five rungs bought 1677569 -> 37.7
ppb, about 4.5 orders of magnitude, so a z_D ladder could move these numbers a
long way.  These are therefore NOT "what convention D gives"; they are what the
ruled base gives before any ladder exists.  Quoting them as D's accuracy would
repeat exactly the mislabelling this bean already had to retract once.
"""
import sys, json, pathlib

# ROOT-ABSOLUTE, not cwd-relative.  A cwd-relative sys.path entry makes the probe
# runnable only from the repo root -- the root-relative-producer trap AGENTS.md
# records (a sweep running with cwd=<producer dir> reports such a script broken).
# `witness_base` lives in computations/substrate/, not computations/.
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / p) for p in
                ("computations", "computations/substrate", "tools/qou-substrate/python")]
from mpmath import mp, mpf, nstr

mp.dps = 70
PPB = mpf(10) ** 9
failures = []
# Every check is recorded so the witness carries the VERDICTS, not merely the
# data they were computed from. A witness reporting "0 assertions" for a probe
# whose whole content is eight checks is not self-describing: a reader has to
# re-derive the conclusions from the payload, which is the same failure mode as
# a producer whose prose and computed table disagree.
ASSERTS: list[tuple[str, bool, str]] = []

def check(label, ok, detail=""):
    print(f"  {'ok  ' if ok else 'FAIL'} {label}" + (f"   {detail}" if detail else ""))
    ASSERTS.append((label, bool(ok), detail))
    if not ok:
        failures.append(label)

# ── inputs, all from the corpus ─────────────────────────────────────────────
import qou_substrate.constants as C
M_E = mpf(str(C.M_E_MEV))
DASH = json.load(open(ROOT / "computations/per-observable-100x-status.witness.json"))
rows = {r["obs"]: r for r in (DASH.get("data", {}).get("rows") or DASH.get("rows"))}

# CODATA references (the comparison boundary)
QB_COD, MN_COD, MP_COD = mpf("0.7823334"), mpf("939.56542194"), mpf("938.27208943")
DPN_COD = MN_COD - MP_COD

# the three admissible/inadmissible cells, from the audit's enumeration
CELLS = {
    "z=1 (published, INADMISSIBLE)": mpf("0.7836465"),
    "z_D (RULED 2026-09-08)":        mpf("0.4447004"),
    "z=q (augmentation)":            mpf("0.8798906"),
}

print("CHECK 1 - the dashboard is still on the inadmissible base")
adm = json.dumps(DASH).lower()
knows = "inadmissible" in adm
still_open = "open owner decision" in adm
check("dashboard carries an admissibility annotation", knows)
print(f"       dashboard Q_beta row: err {rows['Q_beta']['err_ppb']} ppb, miss {rows['Q_beta']['miss_factor']}x")

print("\nCHECK 2 - CALIBRATION: reproduce the CURRENT dependent rows from the CURRENT Q_beta")
# invert the dashboard's own Q_beta row to the MeV value it scored
qb_err = mpf(str(rows["Q_beta"]["err_ppb"])) / PPB
qb_now = QB_COD * (1 + qb_err)            # sign: the published base overshoots
mn_now = MP_COD + qb_now + M_E
dpn_now = qb_now + M_E
pred_mn = abs(mn_now - MN_COD) / MN_COD * PPB
pred_dpn = abs(dpn_now - DPN_COD) / DPN_COD * PPB
obs_mn = mpf(str(rows["m_n"]["err_ppb"]))
obs_dpn = mpf(str(rows["Delta_pn"]["err_ppb"]))
print(f"       Q_beta scored  = {nstr(qb_now,12)} MeV  (from its own {rows['Q_beta']['err_ppb']} ppb row)")
print(f"       m_n      predicted {nstr(pred_mn,6)} ppb   vs dashboard {obs_mn}")
print(f"       Delta_pn predicted {nstr(pred_dpn,6)} ppb   vs dashboard {obs_dpn}")
# the relation is the producer's own; allow an order of magnitude for rung/frame detail
mn_ratio = pred_mn / obs_mn if obs_mn else mpf("inf")
dpn_ratio = pred_dpn / obs_dpn if obs_dpn else mpf("inf")
calibrated = mpf("0.1") < mn_ratio < 10 and mpf("0.1") < dpn_ratio < 10
check("m_n / Delta_pn reproduce from Q_beta within 10x",
      calibrated, f"ratios {nstr(mn_ratio,4)} / {nstr(dpn_ratio,4)}")
if not calibrated:
    print("       -> the dependent rows are NOT a plain function of the scored Q_beta;")
    print("          the re-score below is therefore an UPPER-BOUND sketch, not the row.")

print("\nCHECK 3 - the re-score, all three rows, on each cell")
print(f"       {'cell':32} {'Q_beta ppb':>14} {'m_n ppb':>14} {'Delta_pn ppb':>14}")
priced = {}
for lab, qb in CELLS.items():
    e_qb = abs(qb - QB_COD) / QB_COD * PPB
    e_mn = abs((MP_COD + qb + M_E) - MN_COD) / MN_COD * PPB
    e_dpn = abs((qb + M_E) - DPN_COD) / DPN_COD * PPB
    priced[lab] = {
        "Q_beta_MeV": nstr(qb, 10), "Q_beta_err_ppb": nstr(e_qb, 8),
        "m_n_err_ppb": nstr(e_mn, 8), "Delta_pn_err_ppb": nstr(e_dpn, 8),
        "Q_beta_miss": nstr(e_qb / mpf(str(rows["Q_beta"]["target_100x_ppb"])), 7),
        "m_n_miss": nstr(e_mn / mpf(str(rows["m_n"]["target_100x_ppb"])), 7),
        "Delta_pn_miss": nstr(e_dpn / mpf(str(rows["Delta_pn"]["target_100x_ppb"])), 7),
    }
    print(f"       {lab:32} {nstr(e_qb,8):>14} {nstr(e_mn,8):>14} {nstr(e_dpn,8):>14}")
check("the RULED cell is priced", "z_D (RULED 2026-09-08)" in priced)

print("\nCHECK 4 - the ruled cell is the WORSE admissible one (the ruling was not by accuracy)")
zd = mpf(priced["z_D (RULED 2026-09-08)"]["Q_beta_err_ppb"])
aug = mpf(priced["z=q (augmentation)"]["Q_beta_err_ppb"])
check("z_D is farther from CODATA than the augmentation", zd > aug,
      f"z_D {nstr(zd,6)} ppb  >  aug {nstr(aug,6)} ppb  (ratio {nstr(zd/aug,5)}x)")
print("       So re-scoring on the ruling DEGRADES the headline. That is the")
print("       anti-fit directive working as designed: derivational cleanliness")
print("       first, accuracy as a diagnostic -- not a tie-breaker.")

print("\nCHECK 5 - the producer's own prose is STALE against the ruling")
src = (ROOT / "computations/per_observable_100x_status.py").read_text()
stale_open = "open owner decision" in src
names_aug_best = "best_admissible_err_pct" in src and "augmentation" in src
check("producer still calls the functional an open owner decision", stale_open,
      "ruled 2026-09-08 -- this is a staleness, reported not fixed here")
check("producer names the augmentation as the best admissible cell", names_aug_best,
      "the ruling chose z_D, the worse-fitting cell")

print(f"\n=== {len(ASSERTS) - len(failures)}/{len(ASSERTS)} checks ok" if not failures
      else f"\n=== FAILURES: {failures}")

try:
    from witness_base import WitnessBuilder
    w = WitnessBuilder("qbeta-zd-rescore-price")
    w.set_description(
        "Prices consequence (iii) of the 2026-09-08 owner ruling (eps := Markov trace "
        "at z_D): what the L2 dashboard rows Q_beta / m_n / Delta_pn become on the ruled "
        "base. Measures only -- no row is moved. The z_D figures are the BASE: no c_k "
        "ladder exists on an admissible base (qou-cds1, blocked on qou-pdix), and on the "
        "z=1 base five rungs bought ~4.5 orders, so these are NOT convention D's accuracy."
    )
    w.add_data("cells", priced)
    w.add_data("dashboard_current", {k: {"err_ppb": rows[k]["err_ppb"],
                                        "miss_factor": rows[k]["miss_factor"]}
                                     for k in ("Q_beta", "m_n", "Delta_pn")})
    w.add_data("calibration_ratios", {"m_n": nstr(mn_ratio, 6), "Delta_pn": nstr(dpn_ratio, 6)})
    w.add_data("ruled_cell_is_worse_admissible", bool(zd > aug))
    w.add_data("producer_prose_stale_against_ruling", bool(stale_open))
    w.add_data("ladder_on_zD_base_exists", False)
    # Boolean checks carry no numeric pair, so they are recorded as the
    # string verdict against the string "true" -- with tolerance None,
    # `Assertion.passed` is string equality, which is the honest comparison
    # for a predicate. `detail` rides in the assertion name so nothing is lost.
    for label, ok, detail in ASSERTS:
        w.add_assertion(f"{label}{' -- ' + detail if detail else ''}",
                        computed="true" if ok else "false", expected="true")
    w.save()
    print("witness written")
except Exception as e:                                    # pragma: no cover
    print(f"witness skipped: {type(e).__name__}: {e}")

sys.exit(1 if failures else 0)
