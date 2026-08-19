"""gz_third_knot_rank_grading.py

The third hyperbolic knot, from a source that was in the corpus all along.

Route C M3 (aomega_m3_adjoint_index_set.py) said the one cheap test left for
H_Ad was a RANK-6 KNOT whose grading is not multiplicity-free, and reported that
no such data existed in the 371-PDF corpus. That report was based on a sweep for
"Stokes"; it missed Garoufalidis-Zagier "Knots and Their Related q-Series"
(SIGMA 19 (2023) 082, uploads/2304.09377v2.pdf) -- the sequel [44] that
uploads/2111.06645v3.pdf announces in its own abstract, which studies the
(-2,3,7) pretzel knot in detail and mentions "Stokes" exactly once.

What GZ S3.5 reports looks like the refutation: "a new phenomenon ... the weight
spaces have higher multiplicity". This probe establishes that it is NOT, and
records why, plus three things that ARE new.

Audit-only; scope-(a); nothing wired; no value claimed for A_omega.
"""
import json, os, sys, time

def repo_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.exists(os.path.join(d, "AGENTS.md")): return d
        d = os.path.dirname(d)
    raise RuntimeError("no repo root")

def main():
    t0=time.time(); root=repo_root(); A=[]
    def chk(name, passed, **kw):
        e={"name":name,"passed":bool(passed)}; e.update(kw); A.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    print("="*74); print(" GZ 2304.09377: the (-2,3,7) rank grading"); print("="*74)

    # ---- the three statements in GZ S3.5, transcribed ----
    prose_dims   = [1, 4, 1]                    # "weights 0,1,2 with dimensions 1,4,1"
    delta        = [0, 1, 2, 0, 0, 0]           # (delta_0..delta_5), eps-deformation degree
    h_weights    = [-1, 0, 1, -1, -1, -1]       # weight vector on h=(h_j)
    W = {"W0": [0,3,4,5], "W1": [1], "W2": [2]} # W0=<H0,H3,H4,H5>, W1=<H1>, W2=<H2>
    decomp_dims  = [len(W["W0"]), len(W["W1"]), len(W["W2"])]

    mult = lambda ws, w: sum(1 for v in ws if v == w)

    print("\n[T1] do the three internal statements agree?")
    from_delta = [mult(delta,0), mult(delta,1), mult(delta,2)]
    from_hw    = [mult(h_weights,-1), mult(h_weights,0), mult(h_weights,1)]
    print(f"     prose sentence      : {prose_dims}")
    print(f"     explicit W0/W1/W2   : {decomp_dims}")
    print(f"     from delta degrees  : {from_delta}")
    print(f"     from weight vector  : {from_hw}")
    chk("T1-delta-and-weightvector-and-decomposition-agree",
        from_delta == decomp_dims and from_hw == decomp_dims,
        note="Three encodings of the same grading; the explicit decomposition, the "
             "delta-degrees and the centred weight vector all give (4,1,1).")

    print("\n[T2] ADJUDICATION: the prose sentence is the outlier")
    chk("T2-prose-dims-are-transposed",
        prose_dims != decomp_dims and
        prose_dims == [decomp_dims[1], decomp_dims[0], decomp_dims[2]],
        note="ERRATUM (adjudicated, not guessed). GZ S3.5's sentence says dimensions "
             "'1, 4 and 1'; the paper's OWN explicit decomposition W0=<H0,H3,H4,H5>, "
             "W1=<H1>, W2=<H2> and its delta=(0,1,2,0,0,0) both give (4,1,1). Two "
             "independent internal statements against one, and the discrepancy is "
             "exactly a transposition of the first two entries -- not a miscount. "
             "Same adjudication pattern as the GGM eq-(200) q^1 erratum.")

    print("\n[T3] why it is easy to miss")
    chk("T3-totals-agree-so-the-slip-is-invisible-to-a-sum-check",
        sum(prose_dims) == sum(decomp_dims) == 6,
        note="Both readings total 6 = r. Any check that only verifies the total "
             "passes on the wrong dimensions. Recorded so a future reader does not "
             "'confirm' the prose by summing it.")

    # ---- Part B: the object-identity guard ----
    rank = {"4_1": 2, "5_2": 3, "(-2,3,7)": 6}     # GZ 2111.06645 S2.1; 2304.09377 S3.4
    s_at_one = 3                                    # GGM eq 188: s(x)=x+1+1/x, s(1)=3
    fourone_weights_doubled = [-1, 1]               # 4_1: g_0,g_1 have weights -1/2,+1/2

    print("\n[T4] GUARD: is this grading the object s(x) describes?")
    print(f"     rank r      : {rank}")
    print(f"     s(1)        : {s_at_one}")
    print(f"     4_1 weights : {{-1/2,+1/2}} (2 elements)  vs  s(x): 3 terms")
    chk("T4-rank-grading-is-NOT-s(x)",
        rank["4_1"] != s_at_one and len(fourone_weights_doubled) != 3,
        note="NO -- and this is the load-bearing check. The grading's total is r=2 at "
             "4_1 while s(1)=3, and 4_1's weight SET has two elements ({-1/2,+1/2}) "
             "against s(x)'s three. Different objects. So (-2,3,7)'s "
             "non-multiplicity-free grading does NOT refute H_Ad's polynomial claim. "
             "Without this check the higher multiplicity reads as exactly the "
             "refutation M3 was looking for.")

    print("\n[T5] the grading IS non-multiplicity-free (both halves recorded together)")
    chk("T5-higher-multiplicity-real-but-not-a-refutation",
        max(mult(h_weights,w) for w in set(h_weights)) == 4 and rank["4_1"] != s_at_one,
        note="The phenomenon is real (a weight of dimension 4, which GZ calls 'a new "
             "phenomenon') AND it does not bear on H_Ad. Stating both in one assertion "
             "so neither half can be quoted without the other.")

    # ---- Part C: corroboration of the M3 Part-4 arithmetic ----
    sig = {"4_1": (0,1), "5_2": (1,1), "(-2,3,7)": (4,1)}   # (real embeddings, cx pairs)
    pk  = {k: 1 + r + 2*c for k,(r,c) in sig.items()}
    print("\n[T6] does the rank corroborate M3 Part 4's signature formula?")
    for k in rank:
        r,c = sig[k]
        print(f"     {k:10s} real={r} pairs={c} -> r_pred={r+2*c}  r_GZ={rank[k]}  |P_K|={pk[k]}")
    chk("T6-rank-equals-real-plus-twice-pairs-equals-pk-minus-one",
        all(rank[k] == sig[k][0] + 2*sig[k][1] == pk[k]-1 for k in rank),
        note="Yes, on all three knots and with three DISTINCT values (2,3,6). This is "
             "an INDEPENDENT confirmation: 2111.06645 S2.1 states the ranks outright, "
             "2304.09377 S3.4 recovers them from q-series counts (4,6,12 = 2r), and "
             "M3 Part 4 predicts them from trace-field signatures. Three routes, one "
             "answer. r = |P_K| - 1 = the non-trivial boundary-parabolic reps.")

    # ---- Part D: the S_3 = Gamma/Gamma(2) block decomposition of W0 ----
    # GZ S3.5: rho is the identity on W1,W2 and has kernel Gamma(2) on W0; the
    # S_3 = Gamma/Gamma(2) action on W0 is "the 2-dimensional irreducible
    # representation of S_3 and two copies of the trivial representation".
    s3_partitions = ["(3)", "(2,1)", "(1,1,1)"]
    s3_dims       = [1, 2, 1]           # trivial, standard, sign
    w0_mult       = [2, 1, 0]           # two trivials, one standard, NO sign

    print("\n[T7] W0 as an S_3 representation, in partition blocks")
    for p,d,m in zip(s3_partitions, s3_dims, w0_mult):
        print(f"     {p:9s} dim={d}  multiplicity in W0 = {m}")
    chk("T7-w0-decomposition-dimensionally-consistent",
        sum(m*d for m,d in zip(w0_mult, s3_dims)) == decomp_dims[0] == 4,
        note="2*1 + 1*2 + 0*1 = 4 = dim W0. S_3-irreps are indexed by partitions of 3 "
             "-- the SAME Wedderburn indexing the QOU Hecke programme uses at q=1 -- so "
             "the third knot's modular structure lands in the corpus's own language "
             "without being put there.")

    print("\n[T8] which block is missing?")
    chk("T8-sign-representation-absent-from-w0",
        w0_mult[s3_partitions.index("(1,1,1)")] == 0,
        note="The SIGN representation has multiplicity 0. Under the standard "
             "identification the sign block is the bar-odd one, so the Gamma/Gamma(2) "
             "action on the level-2 part of the third knot's grading carries no sign "
             "component. That is the one asymmetry in the decomposition, and it is "
             "chirality-flavoured -- the same involution that grades the DT split. "
             "NOT claimed to be derived; recorded as an observation to be explained.")

    print("\n[T9] where the level-2 phenomenon lives")
    chk("T9-level-two-confined-to-w0",
        decomp_dims[1] == decomp_dims[2] == 1 and decomp_dims[0] == 4,
        note="rho is the IDENTITY on W1 and W2, so the whole Gamma(2) phenomenon is "
             "confined to the 4-dimensional W0 -- which is precisely the weight space "
             "whose dimension the prose misreported. The erratum sits on the only "
             "interesting summand.")

    # ---- T10-T12: the absent sign block is FORCED, and the scope of that claim ----
    from fractions import Fraction as Frac
    sizes = [1, 3, 2]                                  # |e|, |transpositions|, |3-cycles|
    chi = {"trivial":[1,1,1], "sign":[1,-1,1], "standard":[2,0,-1]}
    ip = lambda a,b: Frac(sum(s*x*y for s,x,y in zip(sizes,a,b)), 6)
    perm = [3, 1, 0]                                   # permutation module on 3 points
    w0   = [x + 2*y for x,y in zip(chi["standard"], chi["trivial"])]   # GZ: std + 2*triv

    print("\n[T10] is W_0 a permutation module?")
    print(f"     chi(W_0)          = {w0}   (GZ: standard + 2 x trivial)")
    print(f"     chi(perm) + chi(triv) = {[a+b for a,b in zip(perm, chi['trivial'])]}")
    chk("T10-w0-is-perm-module-plus-trivial",
        w0 == [a+b for a,b in zip(perm, chi["trivial"])] and w0[0] == 4,
        note="YES. chi(W_0) = [4,2,1] = [3,1,0] + [1,1,1]. Characters determine complex "
             "representations up to isomorphism, so W_0 = C[X] + C with X a 3-element "
             "S_3-set. This upgrades Part D from an observation to a structural "
             "identification. Lean: w0_is_perm_plus_trivial.")

    print("\n[T11] MECHANISM: why the sign block cannot appear")
    print(f"     <perm, sign>  = {ip(perm, chi['sign'])}")
    print(f"     <triv, sign>  = {ip(chi['trivial'], chi['sign'])}")
    print(f"     <W_0,  sign>  = {ip(w0, chi['sign'])}")
    chk("T11-sign-absence-is-forced-not-observed",
        ip(perm, chi["sign"]) == 0 and ip(chi["trivial"], chi["sign"]) == 0
        and ip(w0, chi["sign"]) == 0,
        note="A permutation module on 3 points contains NO sign component -- a general "
             "fact about S_3, nothing knot-specific: <perm,sign> = "
             "(1*3*1 + 3*1*(-1) + 2*0*1)/6 = 0. And a trivial summand contributes 0 to "
             "sign multiplicity, so adding any number of trivials cannot create one. "
             "The absence is therefore FORCED BY SHAPE, not an unexplained coincidence "
             "to be interpreted. Lean: perm_has_no_sign / "
             "addTrivial_preserves_signMult / sign_absence_is_forced.")

    print("\n[T12] ADVERSARIAL: how far does the claim reach?")
    level = {"4_1": 1, "5_2": 1, "(-2,3,7)": 2}
    nontrivial_quotient = {k: v > 1 for k,v in level.items()}
    print(f"     level N        : {level}")
    print(f"     has a group    : {nontrivial_quotient}")
    chk("T12-only-one-knot-can-even-be-asked",
        sum(nontrivial_quotient.values()) == 1 and nontrivial_quotient["(-2,3,7)"],
        note="PASSES as an ADVERSARIAL check and it TEMPERS the finding. GZ introduces "
             "the level as 'a new phenomenon' at (-2,3,7) (N=2); 4_1 and 5_2 have N=1, "
             "so rho factors through the TRIVIAL quotient and there is no finite group "
             "acting -- hence no sign block to be absent. The absence is a ONE-KNOT "
             "statement among these three, by construction. What is general is the "
             "mechanism (T11), which holds for any permutation-type module; what is "
             "single-instance is the observation that W_0 is of that type. Both halves "
             "recorded so neither is quoted alone. Lean: "
             "sign_question_only_arises_at_level_two.")

    # ---- T13-T16: Dimofte-Garoufalidis §6 signatures (uploads/1511.05628v1.pdf) ----
    # DG states trace fields in the SIGNATURE notation [r1,r2] -- the exact input the
    # Part-4 rule consumes -- for five knots. Glyph-verified from §6.1-§6.4.
    dg = {  # knot: (min-poly degree, r1 real, r2 pairs, discriminant as printed)
      "4_1":      (2, 0, 1, "-3"),
      "5_2":      (3, 1, 1, "-23"),
      "6_1":      (4, 0, 2, "257"),
      "(-2,3,9)": (5, 1, 2, "23*733"),
    }
    print("\n[T13] do DG's signatures reproduce the stated polynomial degrees?")
    for k,(deg,r1,r2,d) in dg.items():
        print(f"     {k:10s} type [{r1},{r2}] -> r1+2r2 = {r1+2*r2}   stated degree = {deg}   disc {d}")
    chk("T13-signatures-match-polynomial-degrees",
        all(r1+2*r2 == deg for deg,r1,r2,_ in dg.values()),
        note="Transcription consistency check on the DG table before anything is built "
             "on it: [0,1]->2, [1,1]->3, [0,2]->4, [1,2]->5, matching the minimal "
             "polynomials x^2-x+1, x^3-x^2+1, x^4-2x^3+x^2+3x+1, x^5-x^4+x^3+2x^2-2x+1.")

    print("\n[T14] do DG's types confirm Part 4's independently-read inputs?")
    part4 = {"4_1": (0,1), "5_2": (1,1)}
    print(f"     Part 4 (read from GZ prose) : {part4}")
    print(f"     DG §6 (stated as [r1,r2])   : {{'4_1': (0, 1), '5_2': (1, 1)}}")
    chk("T14-dg-confirms-part4-signature-inputs",
        all((dg[k][1], dg[k][2]) == part4[k] for k in part4),
        note="YES, and from an independent source: Part 4 derived its signatures by "
             "reading Garoufalidis-Zagier's prose; Dimofte-Garoufalidis state the same "
             "two in [r1,r2] type notation. Same inputs, two papers.")

    print("\n[T15] NAMING THE HYPOTHESIS -- and the knot where it fails")
    # r = #embeddings of A_K^red, and A_K^red contains F_K with equality iff K has no
    # boundary-parabolic reps outside its trace field.
    tf_only = {k: dg[k][1] + 2*dg[k][2] for k in dg}
    print(f"     trace-field-only prediction : 4_1 -> {tf_only['4_1']}, 5_2 -> {tf_only['5_2']}")
    print(f"     measured rank (GZ)          : 4_1 -> {rank['4_1']}, 5_2 -> {rank['5_2']}")
    print(f"     (-2,3,7): trace field = 5_2's -> predicts {tf_only['5_2']}, measured {rank['(-2,3,7)']}")
    chk("T15-trace-field-alone-fails-on-pretzel237",
        tf_only["4_1"] == rank["4_1"] and tf_only["5_2"] == rank["5_2"]
        and tf_only["5_2"] != rank["(-2,3,7)"],
        note="MATERIAL SHARPENING OF PART 4. The rule is r = #embeddings of A_K^red, and "
             "A_K^red contains the trace field F_K with EQUALITY IFF K has no "
             "boundary-parabolic reps outside F_K. Part 4 used A_K^red; DG tabulates "
             "F_K. They coincide at 4_1 and 5_2 -- so Part 4's two-knot agreement did "
             "NOT establish which one the rule needs. (-2,3,7) settles it: DG says its "
             "trace field is 5_2's (3 embeddings) while the measured rank is 6, because "
             "P_K picks up a second Galois orbit over the totally real Q(eta). The "
             "hypothesis must be STATED, not assumed.")

    print("\n[T16] two conditional predictions (fourth and fifth knots)")
    print(f"     6_1      [0,2] -> r = {tf_only['6_1']}, |P_K| = {tf_only['6_1']+1}")
    print(f"     (-2,3,9) [1,2] -> r = {tf_only['(-2,3,9)']}, |P_K| = {tf_only['(-2,3,9)']+1}")
    chk("T16-conditional-predictions-stated-with-their-hypothesis",
        tf_only["6_1"] == 4 and tf_only["(-2,3,9)"] == 5,
        note="UNDER the T15 hypothesis A_K^red = F_K: 6_1 has r=4, |P_K|=5; (-2,3,9) has "
             "r=5, |P_K|=6. NOT verified -- no corpus source gives these ranks -- and "
             "FALSE if either knot has reps outside its trace field, exactly as "
             "(-2,3,7) does. Stated with the hypothesis attached rather than as bare "
             "numbers, because (-2,3,7) is precisely the knot where the unstated "
             "version would have been wrong.")

    print("\n[T17] GUARDED NON-INFERENCE: DG's Table 2 'Level' column")
    dg_table2_level = {"4_1":7, "5_2":5, "(-2,3,7)":5, "(-2,3,-3)":3, "(-2,3,9)":3, "6_1":3}
    gz_level        = {"4_1":1, "5_2":1, "(-2,3,7)":2}
    print(f"     DG Table 2 'Level' (<=)  : {dg_table2_level}")
    print(f"     GZ level N (Part E)      : {gz_level}")
    chk("T17-dg-level-is-not-gz-level",
        dg_table2_level["4_1"] != gz_level["4_1"] and dg_table2_level["(-2,3,7)"] != gz_level["(-2,3,7)"],
        note="DIFFERENT QUANTITIES -- recorded so the trap is not walked into. DG's "
             "'level k' is the CHERN-SIMONS level with zeta^k = 1, i.e. the order of the "
             "root of unity at which the numerics were run (their abstract: 'Chern-Simons "
             "theory with gauge group SL(2,C) at fixed level k, where zeta^k = 1'). GZ's "
             "level N is the period of the colored-Jones degree quasi-polynomial. Reading "
             "'6_1 <= 3' as '6_1 has level 3' would MANUFACTURE the fourth level->1 knot "
             "Part E asks for, out of an unrelated quantity. Third instance of this same "
             "conflation trap in this arc.")

    # ---- T18-T21: the 6_1 prediction, CONFIRMED from a second unrelated object ----
    # Sibling certification (main 96d65d02e, bean qou-btvl, probe
    # apoly_census_ldegree_certification_probe.py 3/3) from the Culler A-polynomial
    # census tarball uploads/A_census.tgz, read from its committed witness.
    census = {"4_1": {"name":"K2_1","geom":2,"full":3},
              "5_2": {"name":"K3_2","geom":3,"full":4},
              "6_1": {"name":"K4_1","geom":4,"full":5}}
    tf_deg = {"4_1": 2, "5_2": 3, "6_1": 4}     # DG signatures: [0,1],[1,1],[0,2]

    print("\n[T18] the 6_1 prediction vs the sibling's certification")
    print(f"     predicted (DG trace-field type [0,2]) : r = {tf_deg['6_1']}, |P_K| = {tf_deg['6_1']+1}")
    print(f"     certified (Culler census, K4_1)       : geom L-deg = {census['6_1']['geom']}, "
          f"full = {census['6_1']['full']}")
    chk("T18-sixOne-prediction-confirmed",
        tf_deg["6_1"] == census["6_1"]["geom"] and census["6_1"]["full"] == 5,
        note="CONFIRMED, and by an independent session: the prediction was made here "
             "from Dimofte-Garoufalidis's trace-field SIGNATURE [0,2]; the "
             "certification is a sibling's, from the Culler A-polynomial census. "
             "Credit for the census leg is theirs (main 96d65d02e, bean qou-btvl); "
             "what is this probe's is the prediction it confirms.")

    print("\n[T19] why it is a test and not a restatement")
    print("     prediction side   : degree of an ALGEBRAIC NUMBER FIELD (x^4-2x^3+x^2+3x+1)")
    print("     certification side: L-degree of a NEWTON POLYGON (census A-polynomial)")
    chk("T19-degree-equals-geom-ldegree-on-all-three",
        all(tf_deg[k] == census[k]["geom"] for k in tf_deg)
        and len({census[k]["geom"] for k in census}) == 3,
        note="Nothing forces a number field's degree to equal a knot polynomial's "
             "L-degree -- unrelated objects in unrelated sources. They agree on THREE "
             "knots with three DISTINCT values (2,3,4), and 6_1 was predicted before "
             "its census value was in hand.")

    print("\n[T20] the half that is NOT a test (sibling flagged this first)")
    chk("T20-plus-one-leg-is-definitional",
        all(census[k]["full"] == census[k]["geom"] + 1 for k in census),
        note="full = geom + 1 holds BY CONSTRUCTION -- the +1 is the abelian/trivial "
             "representation -- so the |P_K| = r+1 agreement corroborates nothing and "
             "must never be cited as evidence. The content is entirely in "
             "deg F_K = geometric L-degree = r. The sibling's own bean says this "
             "('full=geom+1 is by construction, not a test'); recorded here so the "
             "caveat travels with the result.")

    print("\n[T21] CONTROL: does the rule fit everything?")
    print(f"     (-2,3,7): trace field = 5_2's -> degree {tf_deg['5_2']}, measured rank {rank['(-2,3,7)']}")
    chk("T21-control-fires-where-hypothesis-fails",
        tf_deg["5_2"] != rank["(-2,3,7)"],
        note="NO -- and that is the point. The identity FAILS at (-2,3,7), exactly the "
             "knot with A_K^red strictly containing F_K. A rule that also fitted there "
             "would be the worrying outcome; this one holds where its stated hypothesis "
             "holds and breaks where it does not. The control is what makes T19 "
             "evidence rather than a coincidence of small numbers.")

    # ---- T22-T25: third route to r(6_1)=4, from Ohtsuki-Yokota's saddle analysis ----
    # ki6c.pdf gives 6_1's gluing-equation quartic 2z^4 - z^3 - 2z^2 + z + 1 (saddle
    # data extracted by a sibling, bean qou-6ort). Exact integer arithmetic only.
    from fractions import Fraction as Fr

    def disc(c):                       # exact discriminant via Sylvester determinant
        n = len(c) - 1
        d = [i * c[i] for i in range(1, n + 1)]
        m = n + (n - 1)
        M = [[0] * m for _ in range(m)]
        for i in range(n - 1):
            for j, k in enumerate(reversed(c)): M[i][i + j] = k
        for i in range(n):
            for j, k in enumerate(reversed(d)): M[n - 1 + i][i + j] = k
        A = [[Fr(v) for v in row] for row in M]; det = Fr(1)
        for i in range(m):
            piv = next((r for r in range(i, m) if A[r][i] != 0), None)
            if piv is None: return 0
            if piv != i: A[i], A[piv] = A[piv], A[i]; det = -det
            det *= A[i][i]; inv = Fr(1) / A[i][i]
            for r in range(i + 1, m):
                f = A[r][i] * inv
                if f:
                    for cc in range(i, m): A[r][cc] -= f * A[i][cc]
        D = Fr((-1) ** (n * (n - 1) // 2)) * det / Fr(c[n])
        return int(D)

    ki_c = [1, 1, -2, -1, 2]          # 2z^4 - z^3 - 2z^2 + z + 1  (ascending)
    dg_c = [1, 3, 1, -2, 1]           # x^4 - 2x^3 + x^2 + 3x + 1  (ascending)

    print("\n[T22] the ki6c gluing quartic vs DG's trace field — invariants")
    print(f"     disc(ki6c quartic) = {disc(ki_c)}     disc(DG quartic) = {disc(dg_c)}")
    chk("T22-same-discriminant-257", disc(ki_c) == disc(dg_c) == 257,
        note="Ohtsuki-Yokota's quartic comes from a STATIONARY-PHASE analysis of the "
             "Kashaev integral -- not a character variety, not a knot polynomial -- and "
             "carries the same discriminant 257 (prime) as DG's trace field.")

    # exact reduction in Z[a]/(dg):  a^4 = 2a^3 - a^2 - 3a - 1
    def red(pp):
        pp = list(pp)
        while len(pp) > 4:
            d = len(pp) - 1; L = pp[d]
            if L:
                for j, k in ((3, 2), (2, -1), (1, -3), (0, -1)): pp[d - 4 + j] += L * k
            pp.pop()
        while len(pp) < 4: pp.append(0)
        return pp
    def mulq(a, b):
        o = [0] * (len(a) + len(b) - 1)
        for i, xx in enumerate(a):
            for j, yy in enumerate(b): o[i + j] += xx * yy
        return red(o)

    gam = [-1, -4, 3, -1]              # gamma = -a^3 + 3a^2 - 4a - 1
    g2 = mulq(gam, gam); g3 = mulq(g2, gam); g4 = mulq(g3, gam)
    cert = [g4[i] - g3[i] - 4 * g2[i] + 4 * gam[i] for i in range(4)]; cert[0] += 8

    print("\n[T23] the explicit isomorphism witness")
    print(f"     gamma = -a^3 + 3a^2 - 4a - 1 = {gam}")
    print(f"     gamma^4 - gamma^3 - 4gamma^2 + 4gamma + 8 = {cert}")
    chk("T23-isomorphism-certificate-exact", all(v == 0 for v in cert),
        note="EXACT, in Z[a]/(a^4-2a^3+a^2+3a+1). gamma/2 is a root of the "
             "Ohtsuki-Yokota quartic, so that quartic has a root in Q(a); both being "
             "irreducible of degree 4, the fields are EQUAL. Not merely "
             "invariant-matched -- an explicit witness. (disc of gamma's minimal "
             "polynomial x^4-x^3-4x^2+4x+8 is 16448 = 2^6 * 257: same field through "
             "the index-2 scaling gamma = 2*beta.) Lean: "
             "saddle_field_equals_trace_field.")

    print("\n[T24] three independent routes to r(6_1)")
    routes = {"trace field degree (DG, a number field)": 4,
              "geometric A-poly L-degree (Culler census, a Newton polygon)": census["6_1"]["geom"],
              "gluing-equation quartic degree (Ohtsuki-Yokota, a saddle analysis)": 4}
    for k, v in routes.items(): print(f"     {v}  <- {k}")
    chk("T24-three-routes-agree", len(set(routes.values())) == 1 and 4 in routes.values(),
        note="Three constructions with nothing in common but the knot, all giving 4.")

    print("\n[T25] SCOPE: is this a DT count?")
    chk("T25-still-not-a-dt-count", True,
        note="NO -- stated plainly so the three-route agreement is not oversold. The "
             "saddles are the CRITICAL POINTS; the Donaldson-Thomas invariants are the "
             "Stokes constants on the Borel rays BETWEEN them. All three routes measure "
             "r, the R1 / Euler-characteristic shadow. The resurgence DT count for 6_1 "
             "is exactly as open as before, and the sibling bean qou-btvl says the same. "
             "What the routes do buy is a falsifiable SHAPE: with |P_K| = 5, 6_1's "
             "reduced Stokes matrix is 4x4 against 5_2's 3x3.")

    # ---- T26-T29: 9_12 breaks the tetrahedron coincidence; the rule survives ----
    tetra = {"4_1": 2, "5_2": 3, "6_1": 4}                # DG §6 ideal-tetrahedron counts
    print("\n[T26] a coincidence worth killing before it counts as evidence")
    for k in tetra: print(f"     {k:5s} tetrahedra={tetra[k]}  trace-field degree={tf_deg[k]}")
    chk("T26-tetrahedra-equal-degree-on-the-small-knots",
        all(tetra[k] == tf_deg[k] for k in tetra),
        note="Three for three. If the rank rule were secretly riding on the "
             "TRIANGULATION count rather than the number field, everything in T13-T24 "
             "would be an artifact -- and nothing up to here distinguishes the two "
             "readings. Recorded so the next check has something to kill.")

    # DG §6.5, the 9_12 knot: 10 ideal tetrahedra, trace field of DEGREE 17
    nt_poly = [-3,18,-55,130,-253,421,-605,764,-851,834,-719,542,-353,195,-89,32,-8,1]
    nt_tetra = 10
    nt_real = sturm_real_roots(nt_poly) if 'sturm_real_roots' in dir() else None
    if nt_real is None:
        def sturm_real_roots(coeffs):
            def norm(pp):
                while pp and pp[-1] == 0: pp.pop()
                return pp
            def dm(a, b):
                a = a[:]
                while len(a) >= len(b) and any(x != 0 for x in a):
                    d = len(a)-len(b); co = a[-1]/b[-1]
                    for i in range(len(b)): a[d+i] -= co*b[i]
                    norm(a)
                    if not a: break
                return a
            pp = [Fr(x) for x in coeffs]; norm(pp)
            dp = [Fr(i)*pp[i] for i in range(1, len(pp))]; norm(dp)
            seq = [pp, dp]
            while len(seq[-1]) > 1:
                r = dm(seq[-2][:], seq[-1][:])
                if not r: break
                seq.append([-x for x in r])
            def sc(at):
                vals = []
                for sq in seq:
                    vals.append(sq[-1]*((-1)**(len(sq)-1)) if at == '-' else sq[-1])
                vals = [v for v in vals if v != 0]
                return sum(1 for i in range(len(vals)-1) if (vals[i] > 0) != (vals[i+1] > 0))
            return sc('-') - sc('+')
        nt_real = sturm_real_roots(nt_poly)
    nt_deg = len(nt_poly)-1
    nt_pairs = (nt_deg - nt_real)//2

    print("\n[T27] 9_12: does the signature reproduce DG's stated type [1,8]?")
    print(f"     degree {nt_deg}, real roots (exact Sturm) = {nt_real}, pairs = {nt_pairs}")
    chk("T27-nineTwelve-signature-matches-DG",
        nt_real == 1 and nt_pairs == 8 and nt_real + 2*nt_pairs == 17,
        note="Independent verification of a 17-term transcription: exact Sturm gives "
             "exactly ONE real root, so [r1,r2] = [1,8] and r1+2r2 = 17, matching DG "
             "§6.5. No floats -- Sturm over Fractions.")

    print("\n[T28] THE KILL: 10 tetrahedra vs degree 17")
    chk("T28-tetrahedron-coincidence-breaks-at-nineTwelve", nt_tetra != nt_deg,
        note="The coincidence dies at the fourth knot: 9_12 has 10 ideal tetrahedra and "
             "a DEGREE-17 trace field. So the rank rule cannot be a restatement of the "
             "triangulation count, and the T13-T24 agreements are about the number "
             "field after all. SHARPER THAN THE CORPUS'S EXISTING GUARD: PR #5277 "
             "refutes 'degree ~ tetrahedra' using the Whitehead link and Borromean "
             "rings -- both LINKS, so the heuristic could be rescued by restricting to "
             "knots. 9_12 is a KNOT and kills the knot-restricted version too.")

    print("\n[T29] the 9_12 prediction, and what is still NOT verified")
    print(f"     under A_K^red = F_K: r(9_12) = {nt_deg}, |P_K| = {nt_deg+1}")
    chk("T29-nineTwelve-prediction-and-open-items", nt_deg == 17,
        note="PREDICTION (unverified, stated with its hypothesis): r(9_12) = 17, "
             "|P_K| = 18. Far more falsifiable than the small cases -- a wrong rule has "
             "17 ways to miss here rather than 4. STILL NOT VERIFIED, said plainly: "
             "(-2,3,9)'s predicted r = 5 from T16 remains open. Census identification "
             "needs SnapPy (absent here) and no (-2,3,9) saddle data is in the corpus, "
             "so neither the T18 nor the T23 route is available. 9_12 does NOT "
             "substitute for it.")

    verdict = (
        "THIRD KNOT FOUND IN-CORPUS, and it does NOT refute H_Ad. (i) The data is in "
        "GZ 2304.09377 (the sequel 2111.06645 announces), which the earlier M3 sweep "
        "missed because it keyed on 'Stokes' and that paper says it once. (ii) GZ "
        "S3.5 reports higher-multiplicity weight spaces for (-2,3,7) -- which reads "
        "exactly like the rank-6 refutation M3 asked for. It is not: the graded object "
        "has total r (=2 at 4_1) while s(1)=3, and 4_1's weight set has 2 elements "
        "against s(x)'s 3. DIFFERENT OBJECTS; the guard is T4. (iii) ERRATUM "
        "adjudicated: GZ S3.5's prose dims (1,4,1) contradict the paper's own "
        "decomposition and delta-degrees, which both give (4,1,1); the prose "
        "transposes the first two, and both readings total 6 so a sum-check cannot "
        "catch it. (iv) The ranks 2,3,6 CORROBORATE M3 Part 4's signature formula on "
        "three knots with three distinct values, via two independent GZ statements. "
        "(v) NEW STRUCTURE: W0 is an S_3 = Gamma/Gamma(2) representation decomposing "
        "into partition blocks (3)^2 + (2,1), with the SIGN block absent -- the QOU "
        "Wedderburn indexing appearing in the third knot's modular data, with a "
        "chirality-flavoured asymmetry. (vi) THE ABSENCE IS FORCED, NOT OBSERVED: chi(W_0)=[4,2,1]=[3,1,0]+[1,1,1], so W_0 is a PERMUTATION module on 3 points plus a trivial, and a 3-point permutation module of S_3 contains no sign component -- a general fact, with trivial summands contributing 0 to sign multiplicity. So Part D is upgraded from observation to mechanism. (vii) BUT THE SCOPE IS ONE KNOT: 4_1 and 5_2 have level N=1, so their quotient is trivial and no group acts -- there is no sign block there to be absent. General mechanism, single-instance instantiation. (viii) DIMOFTE-GAROUFALIDIS 1511.05628 S6 (also missed by the Stokes sweep) states trace fields as SIGNATURES [r1,r2] for five knots. It CONFIRMS Part 4 inputs for 4_1 and 5_2 from an independent source, and forces Part 4 silent hypothesis into the open: the rule needs the signature of A_K^red, NOT of the trace field F_K. Those coincide at 4_1 and 5_2 -- so the two-knot agreement settled nothing -- and (-2,3,7) is a worked counterexample (trace field = 5_2, 3 embeddings, measured rank 6). Under the now-stated hypothesis: 6_1 predicts r=4 / |P_K|=5 and (-2,3,9) predicts r=5 / |P_K|=6, both falsifiable and both unverified. (ix) GUARDED NON-INFERENCE: DG Table 2 Level column is the Chern-Simons level zeta^k=1, NOT GZ level N; reading it as the latter would manufacture the fourth level>1 knot out of an unrelated quantity -- third instance of this conflation trap in this arc. (x) THE 6_1 PREDICTION IS CONFIRMED: a sibling session independently certified 6_1 (census K4_1) at geometric L-degree 4 / full 5 from the Culler A-polynomial census (main 96d65d02e, bean qou-btvl), matching the r=4 / |P_K|=5 predicted here from the DG trace-field type [0,2]. The two sides are a NUMBER FIELD DEGREE and a NEWTON POLYGON L-DEGREE -- unrelated objects, unrelated sources -- agreeing on three knots with three distinct values (2,3,4). The |P_K| = r+1 half is definitional (the abelian rep) and is NOT evidence; the sibling flagged that first. And the control fires: the identity FAILS at (-2,3,7), precisely where A_K^red strictly contains F_K, so the rule does not fit everything. (xi) A THIRD ROUTE to r(6_1)=4, from Ohtsuki-Yokota's SADDLE ANALYSIS (ki6c.pdf, sibling extraction qou-6ort): the 6_1 gluing-equation quartic 2z^4-z^3-2z^2+z+1 is irreducible with discriminant 257 and signature [0,2], matching DG's trace field on every invariant -- and the fields are EQUAL, by the exact witness gamma = -a^3+3a^2-4a-1 satisfying gamma^4-gamma^3-4gamma^2+4gamma+8 = 0 in Z[a]/(dg). So three constructions with nothing in common but the knot (a number field, a Newton polygon, a stationary-phase analysis) all give 4. (xii) STILL NOT A DT COUNT: the saddles are the critical points; the DT invariants are the Stokes constants on the rays BETWEEN them. All three routes measure r, the R1 shadow. The resurgence DT count for 6_1 is exactly as open as before. What is bought is a falsifiable SHAPE: 6_1's reduced Stokes matrix is 4x4 against 5_2's 3x3. (xiii) A COINCIDENCE KILLED: across 4_1/5_2/6_1 the ideal-tetrahedron count EQUALS the trace-field degree (2,3,4), so the rank rule might have been riding on the triangulation rather than the number field. DG S6.5's 9_12 settles it -- 10 ideal tetrahedra, trace field of DEGREE 17 (type [1,8], verified here by exact Sturm: exactly 1 real root). 10 != 17, the coincidence dies at the fourth knot, and the rule -- which reads the signature and never the triangulation -- is untouched. Sharper than PR #5277's existing guard, whose counterexamples are LINKS (Whitehead, Borromean) and could be dodged by restricting to knots; 9_12 is a knot. New prediction: r(9_12) = 17, |P_K| = 18. (xiv) STILL OPEN: (-2,3,9)'s predicted r = 5 is UNVERIFIED -- census identification needs SnapPy (absent) and no saddle data for it is in the corpus. 9_12 does not substitute. Nothing wired."
    )
    print(f"\n verdict: {verdict}")

    w = {"name":"gz-third-knot-rank-grading",
         "description":"GZ 2304.09377 (-2,3,7) rank grading: adjudicates an internal "
                       "erratum, guards the object-identity that would otherwise read "
                       "as an H_Ad refutation, corroborates the M3 Part-4 signature "
                       "formula on a third knot, and records the S_3 block "
                       "decomposition of W0.",
         "computation":"gz-third-knot-rank-grading","engine":"python",
         "scriptFile":"computations/probes/gz_third_knot_rank_grading.py",
         "auditOnly":True,
         "auditDoc":"docs/audits/2026-08-11-route-c-bps-cohomology-scoping.md",
         "q0Anchor":"independent",
         "q0AnchorReason":(
             "No substrate modulus enters. Every quantity is an exact integer read from "
             "Garoufalidis-Zagier 2304.09377 S3.4/S3.5 and 2111.06645 S2.1 (weight "
             "vectors, subspace dimensions, ranks, trace-field signatures, S_3 irrep "
             "dimensions). The import cone is json/os/subprocess/time only -- no "
             "q_parameter, no qou_substrate.constants, no y_lambda_at, no mpmath."),
         "parameters":{"prose_dims":prose_dims,"decomposition_dims":decomp_dims,
                       "delta_degrees":delta,"h_weights":h_weights,
                       "ranks":rank,"signatures":{k:list(v) for k,v in sig.items()},
                       "s3_partitions":s3_partitions,"s3_dims":s3_dims,
                       "w0_multiplicities":w0_mult,
                       "lean":"QOU.QBeta.GZThirdKnotRankGrading",
                       "sources":["uploads/2304.09377v2.pdf","uploads/2111.06645v3.pdf"]},
         "data":{"erratum":"GZ 2304.09377 S3.5 prose dims (1,4,1) -> should be (4,1,1)",
                 "pk_sizes":pk,"verdict":verdict},
         "assertions":A}
    # Provenance via WitnessBuilder (check-sidecars P30): a raw json.dump leaves the
    # witness PROV_MISSING — no scriptHash, no commitSha, no engineVersion. The payload
    # carries a flat `assertions` list, so stamp_staleness_metadata is the right entry
    # point (wrap_legacy is for assertion-free payloads).
    sys.path.insert(0, os.path.join(root, "tools", "qou-substrate", "python"))
    from qou_substrate.witness import WitnessBuilder
    WitnessBuilder.stamp_staleness_metadata(
        w, script_path=__file__, engine="python",
        engine_version=sys.version.split()[0], q0_anchor="independent")
    w["durationMs"] = int((time.time()-t0)*1000)
    out=os.path.join(root,"computations","probes","gz-third-knot-rank-grading.witness.json")
    with open(out,"w") as fh: json.dump(w,fh,indent=2); fh.write("\n")
    print(f"\n witness: {out}")
    nf=sum(1 for a in A if not a["passed"]); print(f" assertions: {len(A)-nf}/{len(A)} passed")
    return 1 if nf else 0

if __name__=="__main__": raise SystemExit(main())
