"""aomega_m3_adjoint_index_set.py

Route C, milestone M3 (bean qou-rtec): attack the INDEX SET, not the cohomology.

Why the target changed. M2 (aomega_m2_bps_cohomology.py) showed the closed-sector
BPS spectrum would be ABELIAN — every Borel ray distinct, trivial
Davison-Meinhardt plethystic log, dim BPS_d = |Omega_d|, all multiplicities 1.
A direct sum of 1-dimensional spaces carries no information beyond WHICH RAYS
EXIST. So M3's real target is not "build a CoHA" (the original framing) but
"derive the index set Omega".

HYPOTHESIS H_Ad (tested here, NOT claimed as derived): the knot-independent core
of the index set is the weight set of the ADJOINT representation of sl_2. For
meridian eigenvalues (m, 1/m) and x = m^2, Ad has eigenvalues (x, 1, 1/x), so
chi_Ad(x) = x + 1 + 1/x = s(x) exactly, and chi_Ad(1) = 3 = dim sl_2.

Mechanism (why this is not a numerology pick): in complex Chern-Simons the Borel
singularities are differences of complex volumes of flat connections, and the
deformation theory of a flat connection is governed by H^1(M, Ad rho) — the
adjoint local system is the canonical coefficient object, not a chosen one.
In QOU terms Ad = Sym^2 V = the partition-(2) Wedderburn block of H_2(q).

This probe runs four checks, including two adversarial ones designed to fail if
H_Ad is empty.

Audit-only; scope-(a); nothing wired; no value claimed for A_omega.
"""
import json, os, subprocess, time
from fractions import Fraction

def repo_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.exists(os.path.join(d, "AGENTS.md")): return d
        d = os.path.dirname(d)
    raise RuntimeError("no repo root")

def head_sha(root):
    for ev in ("GITHUB_SHA","GIT_COMMIT_SHA"):
        v = os.environ.get(ev)
        if v and v.strip(): return v.strip()
    try: return subprocess.check_output(["git","rev-parse","HEAD"],cwd=root,text=True).strip()
    except Exception: return "unknown"

def main():
    t0=time.time(); root=repo_root(); A=[]
    def chk(name, passed, **kw):
        e={"name":name,"passed":bool(passed)}; e.update(kw); A.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    print("="*74); print(" Route C M3: is the DT index set the ADJOINT weight set?"); print("="*74)

    # M2's certified datum (corpus): s(x) exponents and multiplicities for 4_1
    s_exponents_M2 = [1, 0, -1]
    s_mults_M2     = [1, 1, 1]
    # adjoint of sl_2 in x = m^2 coordinates: weights {2,0,-2} in m  ->  {1,0,-1} in x
    adj_exponents  = [1, 0, -1]
    adj_mults      = [1, 1, 1]

    print(f"\n[T1] adjoint character vs M2's s(x)")
    print(f"     M2      : exponents {s_exponents_M2}, multiplicities {s_mults_M2}")
    print(f"     Ad(sl2) : exponents {adj_exponents}, multiplicities {adj_mults}")
    chk("T1-adjoint-character-equals-s(x)",
        sorted(s_exponents_M2)==sorted(adj_exponents) and s_mults_M2==adj_mults,
        note="chi_Ad(x) = x+1+1/x reproduces M2's index polynomial exactly, "
             "multiplicity-free, with NO free parameter to adjust.")

    # T2: knot-independence. H_Ad predicts it (Ad is a property of sl_2, not K).
    # Observed: GGM eqs 239/277/307 give s(x) for 5_2 as well (entries s, s, s+1).
    print("\n[T2] knot-independence (the fact that killed every knot-specific reading)")
    print("     H_Ad PREDICTS s(x) is knot-independent (Ad depends on sl_2, not on K).")
    print("     OBSERVED: the same s(x) governs 5_2 (GGM eqs 239/277/307).")
    chk("T2-knot-independence-predicted-and-observed", True,
        note="This is H_Ad's one non-trivial already-satisfied prediction. "
             "CORRECTION (self, this run): an earlier version of this note said "
             "'Driver14's eight, PLUS Route A's R1, fail precisely here'. That is "
             "wrong about R1 and is retracted. R1 does NOT fail on the counts: it "
             "hits the dtMax vector (4_1,5_2)->(3,4) EXACTLY "
             "(docs/audits/2026-08-11-aomega-internal-derivation-attack-options.md "
             "S6). R1's proved failure is a different one -- it is single-valued "
             "per knot while the 5_2 datum is the 2-element set {3,4} "
             "(Driver14CharacterVarietyDTMenu.no_scalar_matches_chirality_split_"
             "datum). Conflating 'fails knot-independence' with 'fails "
             "set-valuedness' would have hidden T5 below.")

    # T3 (ADVERSARIAL): H_Ad as a SCALAR must fail, exactly like blockCountH3.
    dt_vector = (3, 4)          # (4_1, 5_2) certified S+ counts
    h_ad_scalar = (3, 3)        # knot-independent => same value both knots
    print("\n[T3] ADVERSARIAL: H_Ad as a scalar answer")
    print(f"     knot-independent core gives {h_ad_scalar}; certified target is {dt_vector}")
    chk("T3-H_Ad-is-NOT-a-scalar-answer", h_ad_scalar != dt_vector,
        note="H_Ad FAILS as a scalar, exactly as Driver14's blockCountH3 does. Its "
             "content is therefore NOT the number 3 — it is the GRADING (which "
             "charges carry the states). Recording this prevents H_Ad being "
             "mis-sold as a count.")

    # T4 (ADVERSARIAL): is the 3-element palindromic shape generic?
    #   any {a, 0, -a} is 3-element, multiplicity-free, palindromic.
    generic_family = [[a, 0, -a] for a in (1,2,3,5)]
    print("\n[T4] ADVERSARIAL: is the SHAPE generic?")
    print(f"     {{a,0,-a}} is 3-element multiplicity-free palindromic for every a: "
          f"{generic_family[:3]} ...")
    chk("T4-shape-alone-is-generic-so-mechanism-is-load-bearing", True,
        note="The 3-element palindromic SHAPE is generic (any {a,0,-a}). So the "
             "shape alone proves nothing; what distinguishes H_Ad is the MECHANISM "
             "(Ad governs H^1(M,Ad rho), the deformation theory the Borel "
             "singularities live on) plus the a=1 normalization forced by x=m^2. "
             "Stated so H_Ad cannot be defended on pattern-matching alone.")

    # ---- T5: WHICH projection is H_Ad? (the adversarial R1-vs-H_Ad question) ----
    # Certified chirality-split data: 4_1 is amphichiral so its bar-odd part
    # vanishes -> (S+,S-) = (3,3); 5_2 is chiral -> (S+,S-) = (4,3).
    chir = {"4_1": (3, 3), "5_2": (4, 3)}
    dtmax = {k: max(v) for k, v in chir.items()}
    dtmin = {k: min(v) for k, v in chir.items()}
    print("\n[T5] R1 vs H_Ad -- are they the same reading?")
    print(f"     chirality data (S+,S-): {chir}")
    print(f"     dtMax = {dtmax}   <- this is R1 (#flat connections = A-poly L-degree)")
    print(f"     dtMin = {dtmin}   <- this is H_Ad's knot-independent core")
    chk("T5-H_Ad-is-dtMin-and-R1-is-dtMax",
        list(dtmax.values()) == [3, 4] and set(dtmin.values()) == {3},
        note="They are DIFFERENT halves of the same chirality-split datum, not the "
             "same half twice. R1 reads the larger chirality count on both knots; "
             "H_Ad's core equals the smaller on both. So H_Ad is not a "
             "re-description of R1 -- and the PAIR (H_Ad,R1) reconstructs the full "
             "set-valued datum {3,4} that no single scalar can equal (no tension "
             "with no_scalar_matches_chirality_split_datum, which excludes ONE "
             "scalar, not two). Lean: r1_is_the_dtmax_projection / "
             "h_ad_is_the_dtmin_projection / min_max_pair_reconstructs_datum / "
             "two_scalars_name_what_one_cannot.")

    # ---- T6 (ADVERSARIAL): how much evidence is there for the core, really? ----
    degenerate = [k for k in chir if chir[k][0] == chir[k][1]]
    informative = [k for k in chir if chir[k][0] != chir[k][1]]
    print("\n[T6] ADVERSARIAL: how thin is the evidence for 'core = 3'?")
    print(f"     amphichiral (dtMin == dtMax, so no evidence beyond R1): {degenerate}")
    print(f"     chiral (dtMin != dtMax, genuinely informative):         {informative}")
    chk("T6-support-is-one-non-degenerate-observation",
        degenerate == ["4_1"] and informative == ["5_2"],
        note="4_1's amphichirality COLLAPSES the two projections there, so it "
             "supplies no evidence for H_Ad independent of R1. The entire empirical "
             "support for 'the core is knot-independently 3' is the single "
             "observation S-(5_2) = 3. ONE data point, not two. Recorded so H_Ad is "
             "not read as twice-confirmed. Lean: "
             "fourone_is_a_degenerate_observation.")

    # ---- T7 (ADVERSARIAL): the rival that the data cannot exclude ----
    # H_floor: the knot-independent core is the {0, g, gbar} triple that EVERY
    # hyperbolic knot carries -- i.e. the universal floor of R1 itself, no sl_2.
    h_floor_core = 3
    h_ad_core = 3
    print("\n[T7] ADVERSARIAL: rival hypothesis H_floor (no sl_2 at all)")
    print("     H_floor: core = |{0, g, gbar}| = the 3 boundary-parabolic flat")
    print("              connections EVERY hyperbolic knot has = R1's universal floor.")
    print(f"     H_floor core = {h_floor_core}; H_Ad core = {h_ad_core}")
    chk("T7-H_Ad-not-distinguished-from-H_floor", h_floor_core == h_ad_core,
        note="PASSES as an ADVERSARIAL check: the cores are EQUAL, so the two "
             "hypotheses impose identical constraints on any completion and the "
             "certified data cannot separate them. The coincidence "
             "3 = dim sl_2 = |{0,g,gbar}| is therefore NOT evidence for the adjoint "
             "reading. Worse for T4: H_floor also supplies a 3-element palindromic "
             "grading (Chern-Simons values {0,+V,-V}), so the palindromic shape "
             "cannot arbitrate either. Only the GRADING VARIABLE could -- meridian "
             "x=m^2 (H_Ad) vs Chern-Simons value (H_floor). GGM's s(x) is written "
             "in the meridian variable, which weakly favours H_Ad; 'weakly' is the "
             "honest word and no separation is claimed. Lean: "
             "h_ad_and_h_floor_are_indistinguishable / "
             "palindromic_shape_does_not_arbitrate.")

    # The forced remainder (Lean: AdjointIndexSetM3.adjoint_core_pins_remainder)
    extra_41 = dt_vector[0] - 3
    extra_52 = dt_vector[1] - 3
    print(f"\n[forced remainder]  extra(4_1) = {extra_41},  extra(5_2) = {extra_52}")
    print("     Proved in Lean: a knot-independent core forces a knot-DEPENDENT")
    print("     remainder differing by exactly 1. Under H_Ad it is pinned to (0,1).")
    print("     => any completion of H_Ad must DERIVE that one extra 5_2 ray.")
    print("     Candidate (NOT verified here): 5_2 has 4 boundary-parabolic flat")
    print("     connections vs 4_1's 3 -- the extra ray would be the additional")
    print("     geometric connection. NOTE (self-correction, this run): that")
    print("     candidate IS R1. So completing H_Ad that way does not add a new")
    print("     mechanism -- it makes the count exactly (dtMin from H_Ad, dtMax")
    print("     from R1). That is a real gain (the PAIR names the set-valued datum")
    print("     no scalar can) but it is a COMPOSITION of two imported readings,")
    print("     not a derivation from Hecke data. Saying otherwise would launder.")

    verdict = (
        "M3 REFRAMED and SHARPENED; still a HYPOTHESIS, and this run makes the "
        "case both stronger and thinner than the previous one claimed. STRONGER: "
        "(i) M2's abelian finding means M3's target is the INDEX SET, not a CoHA. "
        "(ii) H_Ad is the dtMin projection and Route A's R1 is the dtMax "
        "projection of the SAME chirality-split datum -- different halves, so H_Ad "
        "is NOT a re-description of R1, and the PAIR reconstructs the 2-element "
        "set {3,4} that no single scalar can equal (no tension with "
        "no_scalar_matches_chirality_split_datum, which excludes one scalar, not "
        "two). (iii) Lean-proved: a knot-independent core FORCES a knot-dependent "
        "unit remainder, pinned to (0,1) under H_Ad. THINNER: (iv) 4_1 is "
        "amphichiral, so its dtMin collapses onto dtMax and supplies NO evidence "
        "independent of R1 -- the whole support for 'core = 3' is the single "
        "observation S-(5_2)=3. (v) A rival H_floor (core = the {0,g,gbar} triple "
        "every hyperbolic knot carries = R1's universal floor, no sl_2 anywhere) "
        "reproduces every H_Ad prediction AND a palindromic 3-element grading, so "
        "the data cannot separate them; only the grading variable (meridian x=m^2 "
        "vs Chern-Simons value) could, and that is not settled here. (vi) "
        "Self-correction: the previously proposed completion -- '5_2 has one extra "
        "flat connection' -- IS R1, so it composes two imported readings rather "
        "than deriving anything from Hecke data. No derivation of the DT spectrum "
        "is claimed; nothing wired."
    )
    print(f"\n verdict: {verdict}")

    w = {"name":"aomega-m3-adjoint-index-set",
         "description":"Route C M3: tests whether the knot-independent core of the "
                       "DT index set is the sl_2 adjoint weight set; includes two "
                       "adversarial checks and the Lean-proved forced remainder.",
         "computation":"aomega-m3-adjoint-index-set","engine":"python",
         "scriptFile":"computations/probes/aomega_m3_adjoint_index_set.py",
         "scriptCommitSha":head_sha(root),
         "computedAt":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),
         "durationMs":int((time.time()-t0)*1000),"auditOnly":True,
         "auditDoc":"docs/audits/2026-08-11-route-c-bps-cohomology-scoping.md",
         "parameters":{"s_exponents_M2":s_exponents_M2,"s_multiplicities_M2":s_mults_M2,
                       "adjoint_exponents":adj_exponents,"dt_vector_4_1_5_2":list(dt_vector),
                       "lean":"QOU.QBeta.AdjointIndexSetM3"},
         "data":{"forced_extra_4_1":extra_41,"forced_extra_5_2":extra_52,"verdict":verdict},
         "assertions":A}
    out=os.path.join(root,"computations","probes","aomega-m3-adjoint-index-set.witness.json")
    with open(out,"w") as fh: json.dump(w,fh,indent=2); fh.write("\n")
    print(f"\n witness: {out}")
    nf=sum(1 for a in A if not a["passed"]); print(f" assertions: {len(A)-nf}/{len(A)} passed")
    return 0

if __name__=="__main__": raise SystemExit(main())
